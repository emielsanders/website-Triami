<?php
// Lader voor nieuw.triami.nl. Vervang KIES-ZELF-EEN-CODE door een eigen code (letters/cijfers),
// zet dit bestand als lader.php in de map van www.triami.nl en open: https://www.triami.nl/lader.php?token=<jouw code>
define('TRIAMI_TOKEN', 'KIES-ZELF-EEN-CODE');
if (TRIAMI_TOKEN === 'KIES-ZELF-EEN-CODE' || ($_GET['token'] ?? '') !== TRIAMI_TOKEN) { http_response_code(403); exit('Geen toegang.'); }
$f = __DIR__ . '/triami-installer.php';
file_put_contents($f, file_get_contents('https://raw.githubusercontent.com/emielsanders/website-Triami/main/tools/server/installer.php'));
register_shutdown_function(function () { @unlink(__FILE__); });
require $f;
