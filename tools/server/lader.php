<?php // Lader: haalt installer.php van GitHub en voert hem uit. Zelfde token als installer.php.
if (($_GET['token'] ?? '') !== 'triami-2026-nieuw') { http_response_code(403); exit; }
file_put_contents(__DIR__ . '/triami-installer.php', file_get_contents('https://raw.githubusercontent.com/emielsanders/website-Triami/main/tools/server/installer.php'));
header('Location: triami-installer.php?token=triami-2026-nieuw');
