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
<figure class="wp-block-image size-large triami-demo"><img src="<?php echo esc_url( $d . 'fietsen-herfst.jpg' ); ?>" alt="Triamist fietst over een bospad in de herfst" width="1024" height="640"/></figure>
<!-- /wp:image -->
<!-- wp:image {"sizeSlug":"large","className":"triami-demo"} -->
<figure class="wp-block-image size-large triami-demo"><img src="<?php echo esc_url( $d . 'looptraining-baan.jpg' ); ?>" alt="Looptraining van Triami op de atletiekbaan in de avond" width="1467" height="917"/></figure>
<!-- /wp:image -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->
