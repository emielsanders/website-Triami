<?php
// Lader op de server (map www van de oude site): haalt beheer.php uit GitHub en voert hem uit.
define('TRIAMI_TOKEN', 'KIES-ZELF-EEN-CODE');
if (TRIAMI_TOKEN === 'KIES-ZELF-EEN-CODE' || ($_GET['token'] ?? '') !== TRIAMI_TOKEN) { http_response_code(403); exit('Geen toegang.'); }
if (($_GET['actie'] ?? '') === 'weg') { @unlink(__FILE__); exit("lader verwijderd\n"); }
$f = __DIR__ . '/triami-beheer-run.php';
file_put_contents($f, file_get_contents('https://raw.githubusercontent.com/emielsanders/website-Triami/main/tools/server/beheer.php?t=' . time()));
register_shutdown_function(function () use ($f) { @unlink($f); });
require $f;
