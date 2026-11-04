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

add_action( 'wp_enqueue_scripts', function () {
	// Google Fonts. Later vervangen door lokaal gehoste woff2 (AVG); zie PROJECT.md.
	wp_enqueue_style(
		'triami-fonts',
		'https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Source+Sans+3:wght@400;600&display=swap',
		array(),
		null
	);
	wp_enqueue_style( 'triami-style', get_template_directory_uri() . '/assets/css/triami.css', array(), TRIAMI_VERSION );
} );

add_action( 'enqueue_block_editor_assets', function () {
	wp_enqueue_style(
		'triami-fonts-editor',
		'https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Source+Sans+3:wght@400;600&display=swap',
		array(),
		null
	);
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
