<?php
/**
 * Title: Logo wit (footer)
 * Slug: triami/logo-wit
 * Inserter: no
 */
$logo = esc_url( get_template_directory_uri() . '/assets/img/logo.svg' );
?>
<!-- wp:html -->
<a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home" aria-label="Triami – naar de homepage"><img src="<?php echo $logo; ?>" alt="Triami Triathlonvereniging Deventer" width="126" height="40" style="height:40px;width:auto;display:block;filter:brightness(0) invert(1)"></a>
<!-- /wp:html -->
