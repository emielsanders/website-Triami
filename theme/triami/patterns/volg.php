<?php
/**
 * Title: Volg Triami (Strava, Spond, Instagram)
 * Slug: triami/volg
 * Categories: triami
 * Description: Drie kaarten met de kanalen van de club: Strava-club, Spond (leden, uitnodiging na aanmelding) en Instagram.
 */
?>
<!-- wp:group {"className":"triami-volg","layout":{"type":"constrained","contentSize":"1200px"},"style":{"spacing":{"padding":{"top":"4rem","bottom":"4rem"}}}} -->
<div class="wp-block-group triami-volg" style="padding-top:4rem;padding-bottom:4rem">
<!-- wp:heading {"className":"is-style-hartslag"} -->
<h2 class="wp-block-heading is-style-hartslag">Volg Triami</h2>
<!-- /wp:heading -->
<!-- wp:paragraph {"fontSize":"groot"} -->
<p class="has-groot-font-size">Trainingen delen we op Strava, afspraken regelen leden in Spond, en de mooiste momenten komen op Instagram.</p>
<!-- /wp:paragraph -->
<!-- wp:group {"layout":{"type":"grid","minimumColumnWidth":"18rem"},"style":{"spacing":{"blockGap":"1.5rem","margin":{"top":"2rem"}}}} -->
<div class="wp-block-group" style="margin-top:2rem">

<!-- wp:group {"className":"is-style-kaart triami-kanaal triami-kanaal-strava","layout":{"type":"default"}} -->
<div class="wp-block-group is-style-kaart triami-kanaal triami-kanaal-strava">
<!-- wp:html -->
<p class="triami-kanaal-kop"><svg aria-hidden="true" viewBox="0 0 24 24" width="28" height="28"><path fill="currentColor" d="M3 17 9 5l3 6h-3l-3 6zm9-6 3 6 3-6h-2l-1 2-1-2z"/><path fill="currentColor" d="m12 11 3-6 6 12h-3l-3-6z" opacity=".55"/></svg><span>Strava-club</span></p>
<!-- /wp:html -->
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Train virtueel mee op Strava</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>In de club zie je wie er getraind heeft, de wekelijkse klassementen en de gezamenlijke kilometers. Word lid en train virtueel mee.</p>
<!-- /wp:paragraph -->
<!-- wp:buttons -->
<div class="wp-block-buttons">
<!-- wp:button {"className":"is-style-outline-zwart"} -->
<div class="wp-block-button is-style-outline-zwart"><a class="wp-block-button__link wp-element-button" href="https://www.strava.com/clubs/triami" target="_blank" rel="noopener">Volg de club op Strava</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-kaart triami-kanaal triami-kanaal-spond","layout":{"type":"default"}} -->
<div class="wp-block-group is-style-kaart triami-kanaal triami-kanaal-spond">
<!-- wp:html -->
<p class="triami-kanaal-kop"><svg aria-hidden="true" viewBox="0 0 24 24" width="28" height="28"><rect x="3" y="5" width="18" height="16" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 10h18M8 3v4M16 3v4" stroke="currentColor" stroke-width="2" fill="none"/><path d="m8 15 2.5 2.5L16 12" stroke="currentColor" stroke-width="2" fill="none"/></svg><span>Spond · voor leden</span></p>
<!-- /wp:html -->
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Trainingen en activiteiten in Spond</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Leden melden zich in Spond aan voor trainingen, het trainingsweekend en wedstrijden. Daar staan ook de exacte tijden en locaties. Nieuwe leden krijgen de uitnodiging in de welkomstmail.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-kaart triami-kanaal triami-kanaal-instagram","layout":{"type":"default"}} -->
<div class="wp-block-group is-style-kaart triami-kanaal triami-kanaal-instagram">
<!-- wp:html -->
<p class="triami-kanaal-kop"><svg aria-hidden="true" viewBox="0 0 24 24" width="28" height="28"><path d="M4 8.5A2.5 2.5 0 0 1 6.5 6H8l1.2-2h5.6L16 6h1.5A2.5 2.5 0 0 1 20 8.5v8a2.5 2.5 0 0 1-2.5 2.5h-11A2.5 2.5 0 0 1 4 16.5z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12.5" r="3.2" fill="none" stroke="currentColor" stroke-width="2"/></svg><span>Instagram</span></p>
<!-- /wp:html -->
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">De club in beeld</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Trainingen, wedstrijden en het trainingsweekend: de laatste foto's van de club verschijnen hier automatisch.</p>
<!-- /wp:paragraph -->
<!-- wp:shortcode -->
[instagram-feed feed=1 num=6 cols=3 showheader=false showbutton=false showfollow=false imagepadding=3 imagepaddingunit=px]
<!-- /wp:shortcode -->
<!-- wp:buttons -->
<div class="wp-block-buttons">
<!-- wp:button {"className":"is-style-outline-zwart"} -->
<div class="wp-block-button is-style-outline-zwart"><a class="wp-block-button__link wp-element-button" href="https://www.instagram.com/triami_triathlon/" target="_blank" rel="noopener">Volg @triami_triathlon</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</div>
<!-- /wp:group -->

</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->
