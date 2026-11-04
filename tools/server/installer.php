<?php
/**
 * Eenmalig installatiescript voor nieuw.triami.nl op de bestaande webspace (Versio/PCextreme).
 *
 * Wat het doet, stap voor stap (elke stap meldt zich op het scherm):
 *  1. zoekt wp-config.php van de huidige site (zelfde webspace) en leest de databasegegevens;
 *  2. maakt naast de map van triami.nl de map nieuw.triami.nl (virtual_document_root → subdomein);
 *  3. downloadt WordPress (nl_NL) van wordpress.org en pakt het uit in die map;
 *  4. schrijft wp-config.php met dezelfde database en het voorvoegsel nieuw_ (eigen tabellen);
 *  5. downloadt het Triami-thema en de pagina-import uit de GitHub-repo;
 *  6. verwijdert zichzelf.
 * Daarna: https://nieuw.triami.nl/ openen en de WordPress-installatie doorlopen.
 *
 * Gebruik: lader.php (met een zelfgekozen code) in de webroot van de oude site zetten en
 * aanroepen met ?token=<code>. De lader haalt dit bestand op en voert het uit.
 */
declare(strict_types=1);
@set_time_limit(600);
@ini_set('display_errors', '1');
error_reporting(E_ALL);
header('Content-Type: text/plain; charset=utf-8');

const SUBDOMEIN  = 'nieuw.triami.nl';
const PREFIX     = 'nieuw_';
const WP_ZIP     = 'https://nl.wordpress.org/latest-nl_NL.zip';
const THEMA_ZIP  = 'https://raw.githubusercontent.com/emielsanders/website-Triami/main/playground/dist/triami.zip';
const WXR_URL    = 'https://raw.githubusercontent.com/emielsanders/website-Triami/main/playground/dist/triami-paginas-import.xml';

// De toegangscode staat NIET in dit bestand (openbare repo) maar in lader.php op de server.
if (!defined('TRIAMI_TOKEN') || TRIAMI_TOKEN === '' || ($_GET['token'] ?? '') !== TRIAMI_TOKEN) { http_response_code(403); exit("Geen toegang.\n"); }

function stap(string $t): void { echo "• $t\n"; @ob_flush(); @flush(); }
function fout(string $t): never { echo "\nFOUT: $t\n"; exit(1); }

function download(string $url, string $naar): void {
    $ctx = stream_context_create(['http' => ['timeout' => 120, 'user_agent' => 'triami-installer']]);
    $in = @fopen($url, 'rb', false, $ctx);
    if (!$in) fout("kan $url niet downloaden (allow_url_fopen uit?)");
    $out = fopen($naar, 'wb');
    stream_copy_to_stream($in, $out);
    fclose($in); fclose($out);
    if (filesize($naar) < 1000) fout("download van $url is leeg");
}

function kopieer_map(string $van, string $naar): void {
    if (!is_dir($naar)) mkdir($naar, 0755, true);
    foreach (scandir($van) as $n) {
        if ($n === '.' || $n === '..') continue;
        $a = "$van/$n"; $b = "$naar/$n";
        is_dir($a) ? kopieer_map($a, $b) : copy($a, $b);
    }
}

function verwijder_map(string $d): void {
    if (!is_dir($d)) return;
    foreach (scandir($d) as $n) { if ($n === '.' || $n === '..') continue; $p = "$d/$n"; is_dir($p) ? verwijder_map($p) : unlink($p); }
    rmdir($d);
}

// 1. wp-config van de oude site
$hier = __DIR__;
$config = null;
foreach ([$hier, dirname($hier), dirname($hier, 2)] as $d) {
    if (is_file("$d/wp-config.php")) { $config = "$d/wp-config.php"; break; }
}
if (!$config) fout('wp-config.php van de huidige site niet gevonden');
$oudroot = dirname($config);
$src = file_get_contents($config);
$db = [];
foreach (['DB_NAME', 'DB_USER', 'DB_PASSWORD', 'DB_HOST'] as $k) {
    if (!preg_match("/define\(\s*['\"]{$k}['\"]\s*,\s*['\"](.*?)['\"]\s*\)/", $src, $m)) fout("$k niet gevonden in wp-config.php");
    $db[$k] = $m[1];
}
stap("databasegegevens gelezen uit $config (database {$db['DB_NAME']}, host {$db['DB_HOST']})");

// 2. doelmap naast de oude site
$ouder = dirname($oudroot);
$doel = "$ouder/" . SUBDOMEIN;
if (is_file("$doel/wp-config.php")) fout("$doel bevat al een WordPress-installatie; stop.");
if (!is_dir($doel) && !mkdir($doel, 0755)) fout("kan $doel niet aanmaken");
stap("doelmap: $doel");

// 3. WordPress downloaden en uitpakken
$tmp = sys_get_temp_dir() . '/triami-' . bin2hex(random_bytes(4));
mkdir($tmp);
download(WP_ZIP, "$tmp/wp.zip");
stap('WordPress gedownload (' . round(filesize("$tmp/wp.zip") / 1e6, 1) . ' MB)');
$zip = new ZipArchive();
if ($zip->open("$tmp/wp.zip") !== true) fout('kan wp.zip niet openen');
$zip->extractTo($tmp); $zip->close();
kopieer_map("$tmp/wordpress", $doel);
stap('WordPress uitgepakt in de doelmap');

// 4. wp-config.php schrijven
$salt = @file_get_contents('https://api.wordpress.org/secret-key/1.1/salt/');
if (!$salt) { $salt = ''; foreach (['AUTH_KEY','SECURE_AUTH_KEY','LOGGED_IN_KEY','NONCE_KEY','AUTH_SALT','SECURE_AUTH_SALT','LOGGED_IN_SALT','NONCE_SALT'] as $k) $salt .= "define('$k', '" . bin2hex(random_bytes(32)) . "');\n"; }
$cfg = "<?php\n"
  . "define( 'DB_NAME', '" . addslashes($db['DB_NAME']) . "' );\n"
  . "define( 'DB_USER', '" . addslashes($db['DB_USER']) . "' );\n"
  . "define( 'DB_PASSWORD', '" . addslashes($db['DB_PASSWORD']) . "' );\n"
  . "define( 'DB_HOST', '" . addslashes($db['DB_HOST']) . "' );\n"
  . "define( 'DB_CHARSET', 'utf8mb4' );\ndefine( 'DB_COLLATE', '' );\n\n"
  . $salt . "\n"
  . "\$table_prefix = '" . PREFIX . "';\n\n"
  . "define( 'WP_DEBUG', false );\n"
  . "define( 'DISALLOW_FILE_EDIT', true );\n"
  . "define( 'WP_AUTO_UPDATE_CORE', 'minor' );\n"
  . "define( 'FS_METHOD', 'direct' );\n\n"
  . "if ( ! defined( 'ABSPATH' ) ) { define( 'ABSPATH', __DIR__ . '/' ); }\n"
  . "require_once ABSPATH . 'wp-settings.php';\n";
file_put_contents("$doel/wp-config.php", $cfg);
stap('wp-config.php geschreven (zelfde database, voorvoegsel ' . PREFIX . ')');

// 5. thema en import
download(THEMA_ZIP, "$tmp/triami.zip");
$zip = new ZipArchive();
if ($zip->open("$tmp/triami.zip") !== true) fout('kan triami.zip niet openen');
$zip->extractTo("$doel/wp-content/themes/"); $zip->close();
stap('thema triami geplaatst in wp-content/themes/triami');
@mkdir("$doel/wp-content/triami-import", 0755);
download(WXR_URL, "$doel/wp-content/triami-import/triami-paginas-import.xml");
stap('pagina-import (WXR) geplaatst in wp-content/triami-import/');
// standaardthema's en Hello Dolly opruimen hoeft niet; WordPress-installer regelt de rest.

// 6. opruimen
verwijder_map($tmp);
@unlink(__FILE__);
stap('tijdelijke bestanden en dit script verwijderd');

echo "\nKLAAR. Open nu https://" . SUBDOMEIN . "/ en doorloop de WordPress-installatie (taal Nederlands, sitetitel 'Triami Triathlonvereniging', vink 'Zoekmachines ontmoedigen' aan).\n";
