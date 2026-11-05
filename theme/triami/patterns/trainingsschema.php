<?php
/**
 * Title: Trainingsschema
 * Slug: triami/trainingsschema
 * Categories: triami
 * Description: De vaste wekelijkse trainingen als kaarten met icoon, dag, tijd en locatie. Wordt op de homepage en op de pagina Trainingen gebruikt.
 */
$zwem = '<svg class="triami-icoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M2 17c2 2 4 2 6 0s4-2 6 0 4 2 6 0M2 12c2 2 4 2 6 0s4-2 6 0 4 2 6 0"/><circle cx="17" cy="6" r="2"/></svg>';
$loop = '<svg class="triami-icoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="16" cy="4" r="2"/><path d="M14 8l-4 4 4 3-2 6M10 12l-4 1M14 15l4 3"/></svg>';
$fiets = '<svg class="triami-icoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="5" cy="17" r="3.5"/><circle cx="19" cy="17" r="3.5"/><path d="M5 17l4.5-8.5L11.5 17H5M9.5 8.5h7M11.5 17l5-8.5L19 17M8 6.5h3M16.5 8.5l1-2h1.5a1.5 1.5 0 0 1 0 3h-.5"/></svg>';
?>
<!-- wp:group {"className":"triami-training","backgroundColor":"achtergrond-zacht","layout":{"type":"constrained","contentSize":"1200px"},"style":{"spacing":{"padding":{"top":"4rem","bottom":"4rem"}}}} -->
<div class="wp-block-group triami-training has-achtergrond-zacht-background-color has-background" style="padding-top:4rem;padding-bottom:4rem">
<!-- wp:heading {"className":"is-style-hartslag"} -->
<h2 class="wp-block-heading is-style-hartslag">Wekelijkse trainingen</h2>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Drie trainingen per week onder leiding van gediplomeerde trainers, plus zelfstandige zwemuren. Daarnaast spreken leden veel onderling af om samen te fietsen, te lopen of in open water te zwemmen. Wijzigingen en afgelastingen staan in Spond.</p>
<!-- /wp:paragraph -->
<!-- wp:group {"layout":{"type":"grid","minimumColumnWidth":"15rem"},"style":{"spacing":{"margin":{"top":"1.5rem"}}}} -->
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
<p class="has-tekst-gedempt-color has-text-color has-klein-font-size">Zwembad De Scheg, Piet van Donkplein 1</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"className":"triami-label","fontSize":"klein"} -->
<p class="triami-label has-klein-font-size">Met trainer</p>
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
<p class="triami-tijd">Woensdag 19:30 – 20:45</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"textColor":"tekst-gedempt","fontSize":"klein"} -->
<p class="has-tekst-gedempt-color has-text-color has-klein-font-size">Atletiekbaan AV Daventria, Borgelerdijk 2. Met loopscholing.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"className":"triami-label","fontSize":"klein"} -->
<p class="triami-label has-klein-font-size">Met trainer</p>
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
<p class="has-tekst-gedempt-color has-text-color has-klein-font-size">Borgelerbad, Borgelerdijk 1</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"className":"triami-label","fontSize":"klein"} -->
<p class="triami-label has-klein-font-size">Met trainer</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
<!-- wp:group {"className":"is-style-kaart"} -->
<div class="wp-block-group is-style-kaart">
<!-- wp:html -->
<?php echo $zwem; ?>
<!-- /wp:html -->
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Vroege zwemuur</h3>
<!-- /wp:heading -->
<!-- wp:paragraph {"className":"triami-tijd"} -->
<p class="triami-tijd">Vrijdag 6:00 – 7:00</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"textColor":"tekst-gedempt","fontSize":"klein"} -->
<p class="has-tekst-gedempt-color has-text-color has-klein-font-size">Zwembad De Scheg. Samen met zwemclub <a href="https://www.zwemclubdeventer.nl/" target="_blank" rel="noopener">De IJsel</a>.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"className":"triami-label","fontSize":"klein"} -->
<p class="triami-label has-klein-font-size">Zelfstandig</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
<!-- wp:group {"className":"is-style-kaart"} -->
<div class="wp-block-group is-style-kaart">
<!-- wp:html -->
<?php echo $zwem; ?>
<!-- /wp:html -->
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Bonuszwemuur</h3>
<!-- /wp:heading -->
<!-- wp:paragraph {"className":"triami-tijd"} -->
<p class="triami-tijd">Zondag 12:30 – 13:30 (winter)</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"textColor":"tekst-gedempt","fontSize":"klein"} -->
<p class="has-tekst-gedempt-color has-text-color has-klein-font-size">Borgelerbad. Alleen met kantwacht; aanmelden via Spond.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"className":"triami-label","fontSize":"klein"} -->
<p class="triami-label has-klein-font-size">Zelfstandig</p>
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
<p class="triami-tijd">Op afspraak, vaak zondag</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"textColor":"tekst-gedempt","fontSize":"klein"} -->
<p class="has-tekst-gedempt-color has-text-color has-klein-font-size">Vertrek bij De Scheg. Leden spreken af via Spond: samen uit, samen thuis.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"className":"triami-label","fontSize":"klein"} -->
<p class="triami-label has-klein-font-size">Onderling</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->
