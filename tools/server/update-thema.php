<?php
/**
 * Tijdelijk hulpmiddel op de server (map www van de oude site): haalt de nieuwste thema-zip
 * uit de GitHub-repo en zet hem in nieuw.triami.nl/wp-content/themes/triami.
 * Aanroep: /update-thema.php?token=<code>. Met &wxr=1 wordt ook de pagina-import ververst.
 * Verwijderen zodra de staging-fase voorbij is (of aanroepen met &weg=1).
 */
declare(strict_types=1);
header('Content-Type: text/plain; charset=utf-8');
define('TRIAMI_TOKEN', 'KIES-ZELF-EEN-CODE');
if (TRIAMI_TOKEN === 'KIES-ZELF-EEN-CODE' || ($_GET['token'] ?? '') !== TRIAMI_TOKEN) { http_response_code(403); exit("Geen toegang.\n"); }
if (isset($_GET['weg'])) { @unlink(__FILE__); exit("update-thema.php verwijderd.\n"); }

$doel = dirname(__DIR__) . '/nieuw';
$themes = "$doel/wp-content/themes";
if (!is_dir($themes)) exit("FOUT: $themes bestaat niet\n");
$zipUrl = 'https://raw.githubusercontent.com/emielsanders/website-Triami/main/playground/dist/triami.zip?t=' . time();
$tmp = tempnam(sys_get_temp_dir(), 'triami');
$ctx = stream_context_create(['http' => ['timeout' => 60, 'user_agent' => 'triami-updater']]);
if (!copy($zipUrl, $tmp, $ctx) || filesize($tmp) < 1000) exit("FOUT: download mislukt\n");
$zip = new ZipArchive();
if ($zip->open($tmp) !== true) exit("FOUT: zip niet te openen\n");
// oude thema-map leegmaken zodat verwijderde bestanden niet achterblijven
$rm = function (string $d) use (&$rm): void { if (!is_dir($d)) return; foreach (scandir($d) as $n) { if ($n === '.' || $n === '..') continue; $p = "$d/$n"; is_dir($p) ? $rm($p) : unlink($p); } rmdir($d); };
$rm("$themes/triami");
$zip->extractTo($themes); $zip->close(); unlink($tmp);
echo "thema bijgewerkt: " . count(iterator_to_array(new RecursiveIteratorIterator(new RecursiveDirectoryIterator("$themes/triami", FilesystemIterator::SKIP_DOTS)))) . " bestanden\n";
if (isset($_GET['wxr'])) {
    @mkdir("$doel/wp-content/triami-import", 0755);
    copy('https://raw.githubusercontent.com/emielsanders/website-Triami/main/playground/dist/triami-paginas-import.xml?t=' . time(), "$doel/wp-content/triami-import/triami-paginas-import.xml", $ctx);
    echo "pagina-import ververst\n";
}
echo "klaar " . date('H:i:s') . "\n";
