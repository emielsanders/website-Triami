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
define('TRIAMI_TOKEN', 'KIES-ZELF-EEN-CODE');
if (TRIAMI_TOKEN === 'KIES-ZELF-EEN-CODE' || ($_GET['token'] ?? '') !== TRIAMI_TOKEN) { http_response_code(403); exit("Geen toegang.\n"); }

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
    $file = "$doel/wp-content/triami-import/triami-paginas-import.xml";
    if (!is_file($file)) exit("FOUT: $file ontbreekt\n");
    require_once ABSPATH . 'wp-admin/includes/import.php';
    require_once ABSPATH . 'wp-admin/includes/post.php';
    require_once ABSPATH . 'wp-admin/includes/taxonomy.php';
    require_once ABSPATH . 'wp-admin/includes/comment.php';
    require_once ABSPATH . 'wp-admin/includes/image.php';
    require_once ABSPATH . 'wp-admin/includes/file.php';
    require_once ABSPATH . 'wp-admin/includes/media.php';
    $plugin = WP_PLUGIN_DIR . '/wordpress-importer/wordpress-importer.php';
    if (!is_file($plugin)) exit("FOUT: WordPress Importer-plugin niet geïnstalleerd\n");
    if (!class_exists('WP_Importer')) require_once ABSPATH . 'wp-admin/includes/class-wp-importer.php';
    require_once $plugin;
    $imp = new WP_Import();
    $imp->fetch_attachments = false;
    $_POST['user_map'] = []; $_POST['imported_authors'] = [];
    ob_start();
    $imp->import($file);
    $log = strip_tags(ob_get_clean());
    echo preg_replace('/\n{2,}/', "\n", trim($log)) . "\n";
    echo "pagina's nu: " . wp_count_posts('page')->publish . "\n";
    exit;
}

exit("onbekende actie\n");
