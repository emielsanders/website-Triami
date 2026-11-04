<?php
/**
 * Title: Logo (header)
 * Slug: triami/logo
 * Inserter: no
 */
$logo = esc_url( get_template_directory_uri() . '/assets/img/logo.svg' );
?>
<!-- wp:html -->
<a class="triami-logo" href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home" aria-label="Triami – naar de homepage"><img src="<?php echo $logo; ?>" alt="Triami Triathlonvereniging Deventer" width="151" height="48" style="height:48px;width:auto;display:block"></a>
<!-- /wp:html -->
