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
<p>Drie trainingen per week onder leiding van gediplomeerde trainers, plus extra momenten waarop leden samen zwemmen en fietsen. Exacte tijden en locaties krijg je zodra je je aanmeldt om mee te trainen; leden vinden alles actueel in de app Spond.</p>
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
<p class="triami-tijd">Dinsdag- en donderdagavond</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"textColor":"tekst-gedempt","fontSize":"klein"} -->
<p class="has-tekst-gedempt-color has-text-color has-klein-font-size">In een binnenbad in Deventer, met techniek en conditie.</p>
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
<p class="triami-tijd">Woensdagavond</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"textColor":"tekst-gedempt","fontSize":"klein"} -->
<p class="has-tekst-gedempt-color has-text-color has-klein-font-size">Op de atletiekbaan in Deventer, met loopscholing.</p>
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
<h3 class="wp-block-heading">Samen zwemmen</h3>
<!-- /wp:heading -->
<!-- wp:paragraph {"className":"triami-tijd"} -->
<p class="triami-tijd">Extra zwemmomenten</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"textColor":"tekst-gedempt","fontSize":"klein"} -->
<p class="has-tekst-gedempt-color has-text-color has-klein-font-size">Vrijdag vroeg zwemmen, in de winter samen op zondag en in de zomer samen openwaterzwemmen, veelal op maandagavond.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"className":"triami-label","fontSize":"klein"} -->
<p class="triami-label has-klein-font-size">Onderling</p>
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
<p class="triami-tijd">Op afspraak, vaak in het weekend</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"textColor":"tekst-gedempt","fontSize":"klein"} -->
<p class="has-tekst-gedempt-color has-text-color has-klein-font-size">Leden spreken samen ritten af: samen uit, samen thuis.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"className":"triami-label","fontSize":"klein"} -->
<p class="triami-label has-klein-font-size">Onderling</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->
<!-- wp:buttons {"style":{"spacing":{"margin":{"top":"1.5rem"}}}} -->
<div class="wp-block-buttons" style="margin-top:1.5rem">
<!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/lidmaatschap/#meetrainen">Kom kennismaken</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</div>
<!-- /wp:group -->
