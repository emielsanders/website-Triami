<?php
/**
 * Triami block theme – minimale functions.php.
 *
 * Alles wat met vormgeving te maken heeft staat in theme.json en assets/css/triami.css.
 * Hier alleen: ondersteuning aanzetten, stylesheet en fonts laden, patterncategorie registreren.
 */

defined( 'ABSPATH' ) || exit;

define( 'TRIAMI_VERSION', '0.1.0' );

add_action( 'after_setup_theme', function () {
	add_theme_support( 'wp-block-styles' );
	add_theme_support( 'editor-styles' );
	add_editor_style( 'assets/css/triami.css' );
	load_theme_textdomain( 'triami', get_template_directory() . '/languages' );
} );

/**
 * Fonts: lokaal gehost via theme.json (assets/fonts/*.woff2, AVG-proof).
 * Alleen als de fontbestanden ontbreken (bv. in de Playground-demo) valt het thema terug op Google Fonts.
 */
function triami_google_fonts_url() {
	return 'https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Source+Sans+3:wght@400;600&display=swap';
}
function triami_fonts_missing() {
	return ! file_exists( get_template_directory() . '/assets/fonts/montserrat-latin.woff2' );
}

add_action( 'wp_enqueue_scripts', function () {
	if ( triami_fonts_missing() ) {
		wp_enqueue_style( 'triami-fonts', triami_google_fonts_url(), array(), null );
	}
	wp_enqueue_style( 'triami-style', get_template_directory_uri() . '/assets/css/triami.css', array(), TRIAMI_VERSION . '.' . filemtime( get_template_directory() . '/assets/css/triami.css' ) );
} );

add_action( 'enqueue_block_editor_assets', function () {
	if ( triami_fonts_missing() ) {
		wp_enqueue_style( 'triami-fonts-editor', triami_google_fonts_url(), array(), null );
	}
} );

// Favicon uit het thema zolang er geen site-icoon is ingesteld.
add_action( 'wp_head', function () {
	if ( ! has_site_icon() ) {
		echo '<link rel="icon" type="image/svg+xml" href="' . esc_url( get_template_directory_uri() . '/assets/img/favicon.svg' ) . '">' . "\n";
	}
}, 5 );

/**
 * SEO-basis zonder plugin: meta description, canonical en Open Graph.
 * Zodra een SEO-plugin actief is (The SEO Framework, Rank Math, Yoast) doet die het werk.
 */
function triami_seo_plugin_active() {
	return defined( 'THE_SEO_FRAMEWORK_VERSION' ) || defined( 'RANK_MATH_VERSION' ) || defined( 'WPSEO_VERSION' );
}
function triami_meta_description() {
	if ( is_front_page() ) {
		return get_bloginfo( 'description' ) . '. Zwemmen, fietsen en hardlopen onder begeleiding van gediplomeerde trainers. Train vrijblijvend mee.';
	}
	if ( is_singular() ) {
		$post = get_queried_object();
		if ( has_excerpt( $post ) ) {
			return wp_strip_all_tags( get_the_excerpt( $post ) );
		}
		$blocks = parse_blocks( $post->post_content );
		foreach ( $blocks as $block ) {
			if ( 'core/paragraph' === $block['blockName'] ) {
				$text = trim( wp_strip_all_tags( $block['innerHTML'] ) );
				if ( strlen( $text ) > 40 ) {
					return wp_html_excerpt( $text, 155, '…' );
				}
			}
		}
	}
	return get_bloginfo( 'description' );
}
add_action( 'wp_head', function () {
	if ( triami_seo_plugin_active() ) {
		return;
	}
	$desc  = esc_attr( triami_meta_description() );
	$title = esc_attr( wp_get_document_title() );
	$url   = esc_url( is_singular() ? get_permalink() : home_url( '/' ) );
	$img   = esc_url( get_template_directory_uri() . '/assets/img/og-image.png' );
	if ( is_singular() && has_post_thumbnail() ) {
		$img = esc_url( get_the_post_thumbnail_url( null, 'large' ) );
	}
	echo "<meta name=\"description\" content=\"{$desc}\">\n";
	echo "<meta property=\"og:type\" content=\"website\">\n";
	echo "<meta property=\"og:site_name\" content=\"" . esc_attr( get_bloginfo( 'name' ) ) . "\">\n";
	echo "<meta property=\"og:title\" content=\"{$title}\">\n";
	echo "<meta property=\"og:description\" content=\"{$desc}\">\n";
	echo "<meta property=\"og:url\" content=\"{$url}\">\n";
	echo "<meta property=\"og:image\" content=\"{$img}\">\n";
	echo "<meta property=\"og:locale\" content=\"nl_NL\">\n";
	echo "<meta name=\"twitter:card\" content=\"summary_large_image\">\n";
	if ( is_front_page() ) {
		$ld = array(
			'@context' => 'https://schema.org',
			'@type'    => 'SportsClub',
			'name'     => 'Triami Triathlonvereniging',
			'url'      => home_url( '/' ),
			'logo'     => get_template_directory_uri() . '/assets/img/logo.svg',
			'email'    => 'secretaris@triami.nl',
			'sport'    => 'Triathlon',
			'address'  => array( '@type' => 'PostalAddress', 'addressLocality' => 'Deventer', 'addressCountry' => 'NL' ),
			'sameAs'   => array( 'https://www.strava.com/clubs/triami' ),
		);
		echo '<script type="application/ld+json">' . wp_json_encode( $ld, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . "</script>\n";
	}
}, 6 );

// Taal van de site: Nederlands, ook als de WordPress-taal nog niet is ingesteld.
add_filter( 'language_attributes', function ( $output ) {
	return 'en_US' === get_locale() ? 'lang="nl"' : $output;
} );

// Redirects van oude URL's (oude site) naar de nieuwe pagina's.
add_action( 'template_redirect', function () {
	$map = array(
		'/lidmaatschap-2/' => '/lidmaatschap/',
		'/bestuur/huishoudelijk-reglement-vastgesteld-19-1-2025/' => '/bestuur/',
	);
	$path = wp_parse_url( $_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH );
	if ( $path && isset( $map[ $path ] ) ) {
		wp_safe_redirect( home_url( $map[ $path ] ), 301 );
		exit;
	}
} );

add_action( 'init', function () {
	register_block_pattern_category( 'triami', array( 'label' => __( 'Triami', 'triami' ) ) );
	register_block_style( 'core/group', array( 'name' => 'kaart', 'label' => __( 'Kaart', 'triami' ) ) );
	register_block_style( 'core/group', array( 'name' => 'donker', 'label' => __( 'Donker', 'triami' ) ) );
	register_block_style( 'core/button', array( 'name' => 'outline-wit', 'label' => __( 'Omlijnd wit', 'triami' ) ) );
	register_block_style( 'core/button', array( 'name' => 'outline-zwart', 'label' => __( 'Omlijnd zwart', 'triami' ) ) );
	register_block_style( 'core/heading', array( 'name' => 'hartslag', 'label' => __( 'Met hartslaglijn', 'triami' ) ) );
} );

// Geen WordPress-versie in de HTML, geen emoji-script, geen XML-RPC.
remove_action( 'wp_head', 'wp_generator' );
remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
remove_action( 'wp_print_styles', 'print_emoji_styles' );
add_filter( 'xmlrpc_enabled', '__return_false' );

/**
 * Shortcodes in het shortcode-blok ook uitvoeren als het blok in een thema-patroon of
 * template staat (bijv. de Instagram-feed in het patroon Volg Triami).
 */
add_filter( 'render_block_core/shortcode', function ( $content ) {
	return do_shortcode( $content );
} );

/**
 * E-mailadressen beschermen tegen adresverzamelaars: mailto-links en zichtbare adressen
 * worden met antispambot() als HTML-entiteiten uitgevoerd. Ze blijven klikbaar en leesbaar
 * voor bezoekers en schermlezers.
 */
add_filter( 'render_block', function ( $content ) {
	if ( false === strpos( $content, '@' ) ) {
		return $content;
	}
	$content = preg_replace_callback(
		'/href="mailto:([^"?]+)(\?[^"]*)?"/i',
		function ( $m ) {
			return 'href="' . antispambot( 'mailto:' ) . antispambot( $m[1] ) . ( $m[2] ?? '' ) . '"';
		},
		$content
	);
	return preg_replace_callback(
		'/>([^<>\s]+@triami\.nl)</i',
		function ( $m ) {
			return '>' . antispambot( $m[1] ) . '<';
		},
		$content
	);
}, 20 );
