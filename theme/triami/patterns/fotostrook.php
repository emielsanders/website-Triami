<?php
/**
 * Title: Fotostrook (zwemmen, fietsen, hardlopen)
 * Slug: triami/fotostrook
 * Categories: triami
 * Description: Drie foto's naast elkaar voor de homepage. Nu demo-afbeeldingen; vervang ze via Weergave → Editor → Home.
 */
$d = get_template_directory_uri() . '/assets/img/demo/';
?>
<!-- wp:group {"className":"triami-fotostrook","layout":{"type":"constrained","contentSize":"1200px"},"style":{"spacing":{"padding":{"top":"0","bottom":"3rem"}}}} -->
<div class="wp-block-group triami-fotostrook" style="padding-top:0;padding-bottom:3rem">
<!-- wp:group {"layout":{"type":"grid","minimumColumnWidth":"16rem"},"style":{"spacing":{"blockGap":"1rem"}}} -->
<div class="wp-block-group">
<!-- wp:image {"sizeSlug":"large","className":"triami-demo"} -->
<figure class="wp-block-image size-large triami-demo"><img src="<?php echo esc_url( $d . 'zwemmen.jpg' ); ?>" alt="Demo-afbeelding: zwemtraining. Wordt vervangen door een echte foto." width="1600" height="1000"/></figure>
<!-- /wp:image -->
<!-- wp:image {"sizeSlug":"large","className":"triami-demo"} -->
<figure class="wp-block-image size-large triami-demo"><img src="<?php echo esc_url( $d . 'fietsen.jpg' ); ?>" alt="Demo-afbeelding: samen fietsen. Wordt vervangen door een echte foto." width="1600" height="1000"/></figure>
<!-- /wp:image -->
<!-- wp:image {"sizeSlug":"large","className":"triami-demo"} -->
<figure class="wp-block-image size-large triami-demo"><img src="<?php echo esc_url( $d . 'hardlopen.jpg' ); ?>" alt="Demo-afbeelding: looptraining. Wordt vervangen door een echte foto." width="1600" height="1000"/></figure>
<!-- /wp:image -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->
