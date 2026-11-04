<?php
/**
 * Title: Trainingsschema
 * Slug: triami/trainingsschema
 * Categories: triami
 * Description: De vaste wekelijkse trainingen als kaarten met icoon, dag, tijd en locatie. Wordt op de homepage en op de pagina Trainingen gebruikt.
 */
$zwem = '<svg class="triami-icoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M2 17c2 2 4 2 6 0s4-2 6 0 4 2 6 0M2 12c2 2 4 2 6 0s4-2 6 0 4 2 6 0"/><circle cx="17" cy="6" r="2"/></svg>';
$loop = '<svg class="triami-icoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="16" cy="4" r="2"/><path d="M14 8l-4 4 4 3-2 6M10 12l-4 1M14 15l4 3"/></svg>';
$fiets = '<svg class="triami-icoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="6" cy="17" r="4"/><circle cx="18" cy="17" r="4"/><path d="M6 17l4-8h5l3 8M10 9l-2-3h4"/></svg>';
?>
<!-- wp:group {"className":"triami-training","backgroundColor":"achtergrond-zacht","layout":{"type":"constrained","contentSize":"1200px"},"style":{"spacing":{"padding":{"top":"4rem","bottom":"4rem"}}}} -->
<div class="wp-block-group triami-training has-achtergrond-zacht-background-color has-background" style="padding-top:4rem;padding-bottom:4rem">
<!-- wp:heading {"className":"is-style-hartslag"} -->
<h2 class="wp-block-heading is-style-hartslag">Wekelijkse trainingen</h2>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Alle trainingen zijn onder leiding van gediplomeerde trainers. Afgelastingen en wijzigingen melden we via Spond. Op feestdagen vervallen de trainingen; het zwemmen kent een zomerstop.</p>
<!-- /wp:paragraph -->
<!-- wp:group {"layout":{"type":"grid","columnCount":4,"minimumColumnWidth":null},"style":{"spacing":{"margin":{"top":"1.5rem"}}}} -->
<div class="wp-block-group" style="margin-top:1.5rem">
<!-- wp:group {"className":"is-style-kaart"} -->
<div class="wp-block-group is-style-kaart">
<!-- wp:html -->
<?php echo $zwem; ?>
<!-- /wp:html -->
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Zwemmen</h3>
<!-- /wp:heading -->
<!-- wp:paragraph {"className":"triami-tijd"} -->
<p class="triami-tijd">Dinsdag 19:30 – 20:30</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"textColor":"tekst-gedempt","fontSize":"klein"} -->
<p class="has-tekst-gedempt-color has-text-color has-klein-font-size">Zwembad De Scheg, volgens jaarschema</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
<!-- wp:group {"className":"is-style-kaart"} -->
<div class="wp-block-group is-style-kaart">
<!-- wp:html -->
<?php echo $zwem; ?>
<!-- /wp:html -->
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Zwemmen</h3>
<!-- /wp:heading -->
<!-- wp:paragraph {"className":"triami-tijd"} -->
<p class="triami-tijd">Donderdag 20:45 – 21:45</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"textColor":"tekst-gedempt","fontSize":"klein"} -->
<p class="has-tekst-gedempt-color has-text-color has-klein-font-size">Borgelerbad, volgens jaarschema</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
<!-- wp:group {"className":"is-style-kaart"} -->
<div class="wp-block-group is-style-kaart">
<!-- wp:html -->
<?php echo $loop; ?>
<!-- /wp:html -->
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Hardlopen</h3>
<!-- /wp:heading -->
<!-- wp:paragraph {"className":"triami-tijd"} -->
<p class="triami-tijd">Woensdag 19:30 – 20:30</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"textColor":"tekst-gedempt","fontSize":"klein"} -->
<p class="has-tekst-gedempt-color has-text-color has-klein-font-size">Atletiekbaan AV Daventria, met loopscholing</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
<!-- wp:group {"className":"is-style-kaart"} -->
<div class="wp-block-group is-style-kaart">
<!-- wp:html -->
<?php echo $fiets; ?>
<!-- /wp:html -->
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Fietsen</h3>
<!-- /wp:heading -->
<!-- wp:paragraph {"className":"triami-tijd"} -->
<p class="triami-tijd">In overleg</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"textColor":"tekst-gedempt","fontSize":"klein"} -->
<p class="has-tekst-gedempt-color has-text-color has-klein-font-size">Leden spreken af via Spond of WhatsApp. Samen uit, samen thuis.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->
