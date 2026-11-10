<?php
/**
 * Title: Fotostrook (zwemmen, fietsen, hardlopen)
 * Slug: triami/fotostrook
 * Categories: triami
 * Description: Drie foto's naast elkaar voor de homepage. Clubfoto's; vervangen kan via Weergave → Editor → Home.
 */
$d = get_template_directory_uri() . '/assets/img/foto/';
?>
<!-- wp:group {"className":"triami-fotostrook","layout":{"type":"constrained","contentSize":"1200px"},"style":{"spacing":{"padding":{"top":"0","bottom":"3rem"}}}} -->
<div class="wp-block-group triami-fotostrook" style="padding-top:0;padding-bottom:3rem">
<!-- wp:group {"layout":{"type":"grid","minimumColumnWidth":"16rem"},"style":{"spacing":{"blockGap":"1rem"}}} -->
<div class="wp-block-group">
<!-- wp:image {"sizeSlug":"large","className":"triami-demo"} -->
<figure class="wp-block-image size-large triami-demo"><img src="<?php echo esc_url( $d . 'zwemmen-onder-water.jpg' ); ?>" alt="Zwemmer van Triami onder water tijdens een zwemtraining" width="1600" height="1000"/></figure>
<!-- /wp:image -->
<!-- wp:image {"sizeSlug":"large","className":"triami-demo"} -->
<figure class="wp-block-image size-large triami-demo"><img src="<?php echo esc_url( $d . 'fietsen-langs-het-water.jpg' ); ?>" alt="Triamisten fietsen samen in een rij langs het water" width="1052" height="658"/></figure>
<!-- /wp:image -->
<!-- wp:image {"sizeSlug":"large","className":"triami-demo"} -->
<figure class="wp-block-image size-large triami-demo"><img src="<?php echo esc_url( $d . 'looptraining-baan.jpg' ); ?>" alt="Looptraining van Triami op de atletiekbaan in de avond" width="1467" height="917"/></figure>
<!-- /wp:image -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->
