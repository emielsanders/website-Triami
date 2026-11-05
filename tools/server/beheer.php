<?php
/**
 * Tijdelijk beheerhulpmiddel voor de staging-site nieuw.triami.nl (staat in de map www van de
 * oude site; verwijderen na de staging-fase met ?actie=weg).
 *
 * Acties (?token=<code>&actie=...):
 *  thema    thema-zip uit GitHub ophalen en vervangen (+ &wxr=1: pagina-import verversen)
 *  import   pagina's importeren uit wp-content/triami-import/triami-paginas-import.xml
 *  opties   sitetitel, ondertitel, permalinks, tijdzone, berichtenpagina, zoekmachines ontmoedigen
 *  status   overzicht: thema, aantal pagina's, opties
 *  weg      dit bestand verwijderen
 */
declare(strict_types=1);
@set_time_limit(300);
header('Content-Type: text/plain; charset=utf-8');
// De code staat in de kleine lader op de server (beheer-lader.php), niet in deze repo.
if (!defined('TRIAMI_TOKEN') || ($_GET['token'] ?? '') !== TRIAMI_TOKEN) { http_response_code(403); exit("Geen toegang.\n"); }

$actie = $_GET['actie'] ?? 'status';
$doel = dirname(__DIR__) . '/nieuw';
$ctx = stream_context_create(['http' => ['timeout' => 60, 'user_agent' => 'triami-beheer']]);
$raw = 'https://raw.githubusercontent.com/emielsanders/website-Triami/main/playground/dist/';

if ($actie === 'weg') { @unlink(__FILE__); exit("beheer.php verwijderd.\n"); }

if ($actie === 'thema') {
    $themes = "$doel/wp-content/themes";
    $tmp = tempnam(sys_get_temp_dir(), 'triami');
    if (!copy($raw . 'triami.zip?t=' . time(), $tmp, $ctx) || filesize($tmp) < 1000) exit("FOUT: download mislukt\n");
    $zip = new ZipArchive();
    if ($zip->open($tmp) !== true) exit("FOUT: zip niet te openen\n");
    $rm = function (string $d) use (&$rm): void { if (!is_dir($d)) return; foreach (scandir($d) as $n) { if ($n === '.' || $n === '..') continue; $p = "$d/$n"; is_dir($p) ? $rm($p) : unlink($p); } rmdir($d); };
    $rm("$themes/triami");
    $zip->extractTo($themes); $zip->close(); unlink($tmp);
    echo "thema vervangen\n";
    if (isset($_GET['wxr'])) {
        @mkdir("$doel/wp-content/triami-import", 0755);
        copy($raw . 'triami-paginas-import.xml?t=' . time(), "$doel/wp-content/triami-import/triami-paginas-import.xml", $ctx);
        echo "pagina-import ververst\n";
    }
    exit("klaar\n");
}

// Vanaf hier draait WordPress van de nieuwe site mee.
define('WP_USE_THEMES', false);
@ini_set('display_errors', '1'); error_reporting(E_ALL);
set_exception_handler(function (Throwable $e) { echo "FOUT: " . get_class($e) . ': ' . $e->getMessage() . ' in ' . $e->getFile() . ':' . $e->getLine() . "\n"; });
register_shutdown_function(function () { $e = error_get_last(); if ($e && in_array($e['type'], [E_ERROR, E_PARSE, E_CORE_ERROR, E_COMPILE_ERROR], true)) echo "FATAAL: {$e['message']} in {$e['file']}:{$e['line']}\n"; });
require "$doel/wp-load.php";
$admins = get_users(['role' => 'administrator', 'number' => 1, 'orderby' => 'ID']);
if (!$admins) exit("FOUT: geen beheerder gevonden\n");
wp_set_current_user($admins[0]->ID);

if ($actie === 'status') {
    echo "site:        " . get_option('blogname') . " — " . get_option('blogdescription') . "\n";
    echo "thema:       " . wp_get_theme()->get('Name') . ' ' . wp_get_theme()->get('Version') . "\n";
    echo "pagina's:    " . wp_count_posts('page')->publish . " gepubliceerd\n";
    echo "permalinks:  " . get_option('permalink_structure') . "\n";
    echo "berichtenpagina: " . get_option('page_for_posts') . ", zoekmachines: " . (get_option('blog_public') ? 'toegestaan' : 'ontmoedigd') . "\n";
    echo "taal: " . get_locale() . ", tijdzone: " . get_option('timezone_string') . ", PHP " . PHP_VERSION . ", WP " . get_bloginfo('version') . "\n";
    exit;
}

if ($actie === 'opties') {
    $r = update_option('blogname', 'Triami Triathlonvereniging');
    echo 'update blogname: ' . var_export($r, true) . ' -> ' . get_option('blogname') . ' (db-prefix ' . $GLOBALS['wpdb']->prefix . ', db ' . DB_NAME . ")\n";
    $GLOBALS['wpdb']->show_errors(); if ($GLOBALS['wpdb']->last_error) echo 'db-fout: ' . $GLOBALS['wpdb']->last_error . "\n";
    update_option('blogdescription', 'Dé triathlonvereniging van Deventer en omstreken');
    update_option('timezone_string', 'Europe/Amsterdam');
    update_option('date_format', 'j F Y');
    update_option('time_format', 'H:i');
    update_option('start_of_week', 1);
    update_option('blog_public', 0);
    update_option('default_comment_status', 'closed');
    update_option('default_pingback_flag', 0);
    update_option('default_ping_status', 'closed');
    update_option('permalink_structure', '/%postname%/');
    $n = get_page_by_path('nieuws');
    if ($n) update_option('page_for_posts', $n->ID);
    foreach ([1, 2, 3] as $id) { $p = get_post($id); if ($p && in_array($p->post_name, ['hallo-wereld', 'hello-world', 'voorbeeld-pagina', 'sample-page', 'privacybeleid', 'privacy-policy'], true)) wp_delete_post($id, true); }
    flush_rewrite_rules();
    exit("opties gezet, voorbeeldinhoud verwijderd, permalinks ververst\n");
}

if ($actie === 'import') {
    // Eigen, minimale WXR-import: alleen pagina's (titel, slug, inhoud, volgorde). Bestaande slug = bijwerken.
    $file = "$doel/wp-content/triami-import/triami-paginas-import.xml";
    if (!is_file($file)) exit("FOUT: $file ontbreekt\n");
    $xml = simplexml_load_file($file);
    if (!$xml) exit("FOUT: XML niet leesbaar\n");
    $ns = $xml->getNamespaces(true);
    $n = 0; $u = 0;
    foreach ($xml->channel->item as $item) {
        $wp = $item->children($ns['wp']); $content = $item->children($ns['content']);
        if ((string) $wp->post_type !== 'page') continue;
        $slug = (string) $wp->post_name;
        $data = ['post_type' => 'page', 'post_status' => 'publish', 'post_title' => (string) $item->title, 'post_name' => $slug,
                 'post_content' => (string) $content->encoded, 'menu_order' => (int) $wp->menu_order, 'comment_status' => 'closed', 'ping_status' => 'closed'];
        $bestaand = get_page_by_path($slug);
        if ($bestaand) { $data['ID'] = $bestaand->ID; wp_update_post($data); $u++; } else { $id = wp_insert_post($data, true); if (is_wp_error($id)) { echo "FOUT bij $slug: " . $id->get_error_message() . "\n"; continue; } $n++; }
        echo "• $slug\n";
    }
    $nieuws = get_page_by_path('nieuws'); if ($nieuws) update_option('page_for_posts', $nieuws->ID);
    flush_rewrite_rules();
    exit("klaar: $n nieuw, $u bijgewerkt; pagina's nu: " . wp_count_posts('page')->publish . "\n");
}

exit("onbekende actie\n");
