"""Test cases for the load_dc_podcasts module."""
# flake8: noqa

from models.load_dc_podcasts import load_dc_podcasts


html = """

<!DOCTYPE html>
<html lang="en-US">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />		<script>(function(html){html.className = html.className.replace(/\bno-js\b/,'js')})(document.documentElement);</script>
<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />

	<!-- This site is optimized with the Yoast SEO plugin v16.0.2 - https://yoast.com/wordpress/plugins/seo/ -->
	<title>First Vision Ep. 4 - How Do 2nd and 3rd Hand Accounts Add to Our Understanding of the First Vision?​ | Doctrine and Covenants Central</title>
	<link rel="canonical" href="https://doctrineandcovenantscentral.org/podcast-episode/how-do-2nd-and-3rd-hand-accounts-add-to-our-understanding-of-the-first-vision​/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="First Vision Ep. 4 - How Do 2nd and 3rd Hand Accounts Add to Our Understanding of the First Vision?​ | Doctrine and Covenants Central" />
	<meta property="og:url" content="https://doctrineandcovenantscentral.org/podcast-episode/how-do-2nd-and-3rd-hand-accounts-add-to-our-understanding-of-the-first-vision​/" />
	<meta property="og:site_name" content="Doctrine and Covenants Central" />
	<meta property="article:modified_time" content="2023-11-27T20:36:29+00:00" />
	<meta name="twitter:card" content="summary_large_image" />
	<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://doctrineandcovenantscentral.org/#organization","name":"Doctrine and Covenants Central","url":"https://doctrineandcovenantscentral.org/","sameAs":["https://www.youtube.com/channel/UCqtKadDOHIbx_Zjq9BhxQYg"],"logo":{"@type":"ImageObject","@id":"https://doctrineandcovenantscentral.org/#logo","inLanguage":"en-US","url":"https://doctrineandcovenantscentral.org/wp-content/uploads/2020/12/DC-1.png","width":3300,"height":1752,"caption":"Doctrine and Covenants Central"},"image":{"@id":"https://doctrineandcovenantscentral.org/#logo"}},{"@type":"WebSite","@id":"https://doctrineandcovenantscentral.org/#website","url":"https://doctrineandcovenantscentral.org/","name":"Doctrine and Covenants Central","description":"","publisher":{"@id":"https://doctrineandcovenantscentral.org/#organization"},"potentialAction":[{"@type":"SearchAction","target":"https://doctrineandcovenantscentral.org/?s={search_term_string}","query-input":"required name=search_term_string"}],"inLanguage":"en-US"},{"@type":"WebPage","@id":"https://doctrineandcovenantscentral.org/podcast-episode/how-do-2nd-and-3rd-hand-accounts-add-to-our-understanding-of-the-first-vision%e2%80%8b/#webpage","url":"https://doctrineandcovenantscentral.org/podcast-episode/how-do-2nd-and-3rd-hand-accounts-add-to-our-understanding-of-the-first-vision%e2%80%8b/","name":"First Vision Ep. 4 - How Do 2nd and 3rd Hand Accounts Add to Our Understanding of the First Vision?\u200b | Doctrine and Covenants Central","isPartOf":{"@id":"https://doctrineandcovenantscentral.org/#website"},"datePublished":"2023-07-31T22:19:29+00:00","dateModified":"2023-11-27T20:36:29+00:00","breadcrumb":{"@id":"https://doctrineandcovenantscentral.org/podcast-episode/how-do-2nd-and-3rd-hand-accounts-add-to-our-understanding-of-the-first-vision%e2%80%8b/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https://doctrineandcovenantscentral.org/podcast-episode/how-do-2nd-and-3rd-hand-accounts-add-to-our-understanding-of-the-first-vision%e2%80%8b/"]}]},{"@type":"BreadcrumbList","@id":"https://doctrineandcovenantscentral.org/podcast-episode/how-do-2nd-and-3rd-hand-accounts-add-to-our-understanding-of-the-first-vision%e2%80%8b/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"item":{"@type":"WebPage","@id":"https://doctrineandcovenantscentral.org/","url":"https://doctrineandcovenantscentral.org/","name":"Home"}},{"@type":"ListItem","position":2,"item":{"@type":"WebPage","@id":"https://doctrineandcovenantscentral.org/podcast-episode/","url":"https://doctrineandcovenantscentral.org/podcast-episode/","name":"Podcast Episodes"}},{"@type":"ListItem","position":3,"item":{"@type":"WebPage","@id":"https://doctrineandcovenantscentral.org/podcast-episode/how-do-2nd-and-3rd-hand-accounts-add-to-our-understanding-of-the-first-vision%e2%80%8b/","url":"https://doctrineandcovenantscentral.org/podcast-episode/how-do-2nd-and-3rd-hand-accounts-add-to-our-understanding-of-the-first-vision%e2%80%8b/","name":"First Vision Ep. 4 &#8211; How Do 2nd and 3rd Hand Accounts Add to Our Understanding of the First Vision?\u200b"}}]}]}</script>
	<!-- / Yoast SEO plugin. -->


<link rel='dns-prefetch' href='//cdnjs.cloudflare.com' />
<link rel='dns-prefetch' href='//fonts.googleapis.com' />
<link rel='dns-prefetch' href='//s.w.org' />
<link href='https://fonts.gstatic.com' crossorigin rel='preconnect' />
<link rel="alternate" type="application/rss+xml" title="Doctrine and Covenants Central &raquo; Feed" href="https://doctrineandcovenantscentral.org/feed/" />
<link rel="alternate" type="application/rss+xml" title="Doctrine and Covenants Central &raquo; Comments Feed" href="https://doctrineandcovenantscentral.org/comments/feed/" />
		<script>
			window._wpemojiSettings = {"baseUrl":"https:\\/\\/s.w.org\\/images\\/core\\/emoji\\/13.0.1\\/72x72\\/","ext":".png","svgUrl":"https:\\/\\/s.w.org\\/images\\/core\\/emoji\\/13.0.1\\/svg\\/","svgExt":".svg","source":{"concatemoji":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-includes\\/js\\/wp-emoji-release.min.js?ver=5.7.10"}};
			!function(e,a,t){var n,r,o,i=a.createElement("canvas"),p=i.getContext&&i.getContext("2d");function s(e,t){var a=String.fromCharCode;p.clearRect(0,0,i.width,i.height),p.fillText(a.apply(this,e),0,0);e=i.toDataURL();return p.clearRect(0,0,i.width,i.height),p.fillText(a.apply(this,t),0,0),e===i.toDataURL()}function c(e){var t=a.createElement("script");t.src=e,t.defer=t.type="text/javascript",a.getElementsByTagName("head")[0].appendChild(t)}for(o=Array("flag","emoji"),t.supports={everything:!0,everythingExceptFlag:!0},r=0;r<o.length;r++)t.supports[o[r]]=function(e){if(!p||!p.fillText)return!1;switch(p.textBaseline="top",p.font="600 32px Arial",e){case"flag":return s([127987,65039,8205,9895,65039],[127987,65039,8203,9895,65039])?!1:!s([55356,56826,55356,56819],[55356,56826,8203,55356,56819])&&!s([55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447],[55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128,56430,8203,56128,56423,8203,56128,56447]);case"emoji":return!s([55357,56424,8205,55356,57212],[55357,56424,8203,55356,57212])}return!1}(o[r]),t.supports.everything=t.supports.everything&&t.supports[o[r]],"flag"!==o[r]&&(t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&t.supports[o[r]]);t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&!t.supports.flag,t.DOMReady=!1,t.readyCallback=function(){t.DOMReady=!0},t.supports.everything||(n=function(){t.readyCallback()},a.addEventListener?(a.addEventListener("DOMContentLoaded",n,!1),e.addEventListener("load",n,!1)):(e.attachEvent("onload",n),a.attachEvent("onreadystatechange",function(){"complete"===a.readyState&&t.readyCallback()})),(n=t.source||{}).concatemoji?c(n.concatemoji):n.wpemoji&&n.twemoji&&(c(n.twemoji),c(n.wpemoji)))}(window,document,window._wpemojiSettings);
		</script>
		<style>
img.wp-smiley,
img.emoji {
	display: inline !important;
	border: none !important;
	box-shadow: none !important;
	height: 1em !important;
	width: 1em !important;
	margin: 0 .07em !important;
	vertical-align: -0.1em !important;
	background: none !important;
	padding: 0 !important;
}
</style>
	<link rel='stylesheet' id='toolset-common-es-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/toolset-blocks/vendor/toolset/common-es/public/toolset-common-es.css?ver=140000' media='all' />
<link rel='stylesheet' id='toolset_blocks-style-css-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/toolset-blocks/vendor/toolset/blocks/public/css/style.css?ver=1.4.1' media='all' />
<link rel='stylesheet' id='bdt-uikit-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/bdthemes-element-pack-lite/assets/css/bdt-uikit.css?ver=3.2' media='all' />
<link rel='stylesheet' id='element-pack-site-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/bdthemes-element-pack-lite/assets/css/element-pack-site.css?ver=2.9.2' media='all' />
<link rel='stylesheet' id='wp-block-library-css'  href='https://doctrineandcovenantscentral.org/wp-includes/css/dist/block-library/style.min.css?ver=5.7.10' media='all' />
<link rel='stylesheet' id='wp-block-library-theme-css'  href='https://doctrineandcovenantscentral.org/wp-includes/css/dist/block-library/theme.min.css?ver=5.7.10' media='all' />
<link rel='stylesheet' id='simple-sitemap-css-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/simple-sitemap/lib/assets/css/simple-sitemap.css?ver=5.7.10' media='all' />
<link rel='stylesheet' id='view_editor_gutenberg_frontend_assets-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/toolset-blocks/public/css/views-frontend.css?ver=3.4.2' media='all' />
<link rel='stylesheet' id='eae-css-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/css/eae.min.css?ver=5.7.10' media='all' />
<link rel='stylesheet' id='font-awesome-4-shim-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/font-awesome/css/v4-shims.min.css?ver=5.7.10' media='all' />
<link rel='stylesheet' id='font-awesome-5-all-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/font-awesome/css/all.min.css?ver=5.7.10' media='all' />
<link rel='stylesheet' id='vegas-css-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/lib/vegas/vegas.min.css?ver=5.7.10' media='all' />
<link rel='stylesheet' id='font-awesome-5-free-css'  href='//cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.2/css/all.min.css?ver=5.7.10' media='all' />
<link rel='stylesheet' id='2f9091768-css'  href='https://doctrineandcovenantscentral.org/wp-content/uploads/essential-addons-elementor/2f9091768.min.css?ver=1701117769' media='all' />
<link rel='stylesheet' id='twentyseventeen-fonts-css'  href='https://fonts.googleapis.com/css?family=Libre+Franklin%3A300%2C300i%2C400%2C400i%2C600%2C600i%2C800%2C800i&#038;subset=latin%2Clatin-ext&#038;display=fallback' media='all' />
<link rel='stylesheet' id='twentyseventeen-style-css'  href='https://doctrineandcovenantscentral.org/wp-content/themes/twentyseventeen/style.css?ver=20190507' media='all' />
<link rel='stylesheet' id='twentyseventeen-block-style-css'  href='https://doctrineandcovenantscentral.org/wp-content/themes/twentyseventeen/assets/css/blocks.css?ver=20190105' media='all' />
<!--[if lt IE 9]>
<link rel='stylesheet' id='twentyseventeen-ie8-css'  href='https://doctrineandcovenantscentral.org/wp-content/themes/twentyseventeen/assets/css/ie8.css?ver=20161202' media='all' />
<![endif]-->
<link rel='stylesheet' id='dflip-icons-style-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/3d-flipbook-dflip-lite/assets/css/themify-icons.min.css?ver=1.7.5.1' media='all' />
<link rel='stylesheet' id='dflip-style-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/3d-flipbook-dflip-lite/assets/css/dflip.min.css?ver=1.7.5.1' media='all' />
<link rel='stylesheet' id='elementor-icons-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/eicons/css/elementor-icons.min.css?ver=5.11.0' media='all' />
<style id='elementor-icons-inline-css'>

		.elementor-add-new-section .elementor-add-templately-promo-button{
            background-color: #5d4fff;
            background-image: url(https://doctrineandcovenantscentral.org/wp-content/plugins/essential-addons-for-elementor-lite/assets/admin/images/templately/logo-icon.svg);
            background-repeat: no-repeat;
            background-position: center center;
            margin-left: 5px;
            position: relative;
            bottom: 5px;
        }
</style>
<link rel='stylesheet' id='elementor-animations-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/animations/animations.min.css?ver=3.2.3' media='all' />
<link rel='stylesheet' id='elementor-frontend-legacy-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/css/frontend-legacy.min.css?ver=3.2.3' media='all' />
<link rel='stylesheet' id='elementor-frontend-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/css/frontend.min.css?ver=3.2.3' media='all' />
<style id='elementor-frontend-inline-css'>
@font-face{font-family:eicons;src:url(https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/eicons/fonts/eicons.eot?5.10.0);src:url(https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/eicons/fonts/eicons.eot?5.10.0#iefix) format("embedded-opentype"),url(https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/eicons/fonts/eicons.woff2?5.10.0) format("woff2"),url(https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/eicons/fonts/eicons.woff?5.10.0) format("woff"),url(https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/eicons/fonts/eicons.ttf?5.10.0) format("truetype"),url(https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/eicons/fonts/eicons.svg?5.10.0#eicon) format("svg");font-weight:400;font-style:normal}
</style>
<link rel='stylesheet' id='elementor-post-10-css'  href='https://doctrineandcovenantscentral.org/wp-content/uploads/elementor/css/post-10.css?ver=1689724144' media='all' />
<link rel='stylesheet' id='elementor-pro-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor-pro/assets/css/frontend.min.css?ver=3.2.2' media='all' />
<link rel='stylesheet' id='elementor-global-css'  href='https://doctrineandcovenantscentral.org/wp-content/uploads/elementor/css/global.css?ver=1689724144' media='all' />
<link rel='stylesheet' id='elementor-post-1396-css'  href='https://doctrineandcovenantscentral.org/wp-content/uploads/elementor/css/post-1396.css?ver=1689724145' media='all' />
<link rel='stylesheet' id='elementor-post-1373-css'  href='https://doctrineandcovenantscentral.org/wp-content/uploads/elementor/css/post-1373.css?ver=1689724145' media='all' />
<link rel='stylesheet' id='elementor-post-31897-css'  href='https://doctrineandcovenantscentral.org/wp-content/uploads/elementor/css/post-31897.css?ver=1690999111' media='all' />
<link rel='stylesheet' id='mediaelement-css'  href='https://doctrineandcovenantscentral.org/wp-includes/js/mediaelement/mediaelementplayer-legacy.min.css?ver=4.2.16' media='all' />
<link rel='stylesheet' id='wp-mediaelement-css'  href='https://doctrineandcovenantscentral.org/wp-includes/js/mediaelement/wp-mediaelement.min.css?ver=5.7.10' media='all' />
<link rel='stylesheet' id='views-pagination-style-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/toolset-blocks/embedded/res/css/wpv-pagination.css?ver=3.4.2' media='all' />
<style id='views-pagination-style-inline-css'>
.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-default > span.wpv-sort-list,.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-default .wpv-sort-list-item {border-color: #cdcdcd;}.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-default .wpv-sort-list-item a {color: #444;background-color: #fff;}.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-default a:hover,.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-default a:focus {color: #000;background-color: #eee;}.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-default .wpv-sort-list-item.wpv-sort-list-current a {color: #000;background-color: #eee;}.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-grey > span.wpv-sort-list,.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-grey .wpv-sort-list-item {border-color: #cdcdcd;}.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-grey .wpv-sort-list-item a {color: #444;background-color: #eeeeee;}.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-grey a:hover,.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-grey a:focus {color: #000;background-color: #e5e5e5;}.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-grey .wpv-sort-list-item.wpv-sort-list-current a {color: #000;background-color: #e5e5e5;}.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-blue > span.wpv-sort-list,.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-blue .wpv-sort-list-item {border-color: #0099cc;}.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-blue .wpv-sort-list-item a {color: #444;background-color: #cbddeb;}.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-blue a:hover,.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-blue a:focus {color: #000;background-color: #95bedd;}.wpv-sort-list-dropdown.wpv-sort-list-dropdown-style-blue .wpv-sort-list-item.wpv-sort-list-current a {color: #000;background-color: #95bedd;}
</style>
<link rel='stylesheet' id='google-fonts-1-css'  href='https://fonts.googleapis.com/css?family=Raleway%3A100%2C100italic%2C200%2C200italic%2C300%2C300italic%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic%2C800%2C800italic%2C900%2C900italic%7CGoudy+Bookletter+1911%3A100%2C100italic%2C200%2C200italic%2C300%2C300italic%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic%2C800%2C800italic%2C900%2C900italic%7CCinzel%3A100%2C100italic%2C200%2C200italic%2C300%2C300italic%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic%2C800%2C800italic%2C900%2C900italic&#038;display=auto&#038;ver=5.7.10' media='all' />
<link rel='stylesheet' id='elementor-icons-shared-0-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/font-awesome/css/fontawesome.min.css?ver=5.15.1' media='all' />
<link rel='stylesheet' id='elementor-icons-fa-solid-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/font-awesome/css/solid.min.css?ver=5.15.1' media='all' />
<link rel='stylesheet' id='elementor-icons-fa-brands-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/font-awesome/css/brands.min.css?ver=5.15.1' media='all' />
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/toolset-blocks/vendor/toolset/common-es/public/toolset-common-es-frontend.js?ver=140000' id='toolset-common-es-frontend-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-includes/js/jquery/jquery.min.js?ver=3.5.1' id='jquery-core-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.3.2' id='jquery-migrate-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/font-awesome/js/v4-shims.min.js?ver=5.7.10' id='font-awesome-4-shim-js'></script>
<!--[if lt IE 9]>
<script src='https://doctrineandcovenantscentral.org/wp-content/themes/twentyseventeen/assets/js/html5.js?ver=20161020' id='html5-js'></script>
<![endif]-->
<link rel="https://api.w.org/" href="https://doctrineandcovenantscentral.org/wp-json/" /><link rel="alternate" type="application/json" href="https://doctrineandcovenantscentral.org/wp-json/wp/v2/podcast-episode/31913" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://doctrineandcovenantscentral.org/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://doctrineandcovenantscentral.org/wp-includes/wlwmanifest.xml" />
<meta name="generator" content="WordPress 5.7.10" />
<link rel='shortlink' href='https://doctrineandcovenantscentral.org/?p=31913' />
<link rel="alternate" type="application/json+oembed" href="https://doctrineandcovenantscentral.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fdoctrineandcovenantscentral.org%2Fpodcast-episode%2Fhow-do-2nd-and-3rd-hand-accounts-add-to-our-understanding-of-the-first-vision%25e2%2580%258b%2F" />
<link rel="alternate" type="text/xml+oembed" href="https://doctrineandcovenantscentral.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fdoctrineandcovenantscentral.org%2Fpodcast-episode%2Fhow-do-2nd-and-3rd-hand-accounts-add-to-our-understanding-of-the-first-vision%25e2%2580%258b%2F&#038;format=xml" />
<script data-cfasync="false"> var dFlipLocation = "https://doctrineandcovenantscentral.org/wp-content/plugins/3d-flipbook-dflip-lite/assets/"; var dFlipWPGlobal = {"text":{"toggleSound":"Turn on\\/off Sound","toggleThumbnails":"Toggle Thumbnails","toggleOutline":"Toggle Outline\\/Bookmark","previousPage":"Previous Page","nextPage":"Next Page","toggleFullscreen":"Toggle Fullscreen","zoomIn":"Zoom In","zoomOut":"Zoom Out","toggleHelp":"Toggle Help","singlePageMode":"Single Page Mode","doublePageMode":"Double Page Mode","downloadPDFFile":"Download PDF File","gotoFirstPage":"Goto First Page","gotoLastPage":"Goto Last Page","share":"Share","mailSubject":"I wanted you to see this FlipBook","mailBody":"Check out this site {{url}}","loading":"DearFlip: Loading "},"moreControls":"download,pageMode,startPage,endPage,sound","hideControls":"","scrollWheel":"true","backgroundColor":"#777","backgroundImage":"","height":"auto","paddingLeft":"20","paddingRight":"20","controlsPosition":"bottom","duration":800,"soundEnable":"true","enableDownload":"true","enableAnnotation":"false","enableAnalytics":"false","webgl":"true","hard":"none","maxTextureSize":"1600","rangeChunkSize":"524288","zoomRatio":1.5,"stiffness":3,"pageMode":"0","singlePageMode":"0","pageSize":"0","autoPlay":"false","autoPlayDuration":5000,"autoPlayStart":"false","linkTarget":"2","sharePrefix":"dearflip-"};</script>		<style id="twentyseventeen-custom-header-styles" type="text/css">
				.site-title,
		.site-description {
			position: absolute;
			clip: rect(1px, 1px, 1px, 1px);
		}
				</style>
		<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-PRSSCPC');</script>
<!-- End Google Tag Manager --><link rel="icon" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2020/12/cropped-DC-1-1-32x32.png" sizes="32x32" />
<link rel="icon" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2020/12/cropped-DC-1-1-192x192.png" sizes="192x192" />
<link rel="apple-touch-icon" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2020/12/cropped-DC-1-1-180x180.png" />
<meta name="msapplication-TileImage" content="https://doctrineandcovenantscentral.org/wp-content/uploads/2020/12/cropped-DC-1-1-270x270.png" />
</head>
<body class="podcast-episode-template-default single single-podcast-episode postid-31913 wp-custom-logo wp-embed-responsive has-sidebar title-tagline-hidden colors-light elementor-default elementor-template-full-width elementor-kit-10 elementor-page-31897">
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PRSSCPC"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

		<div data-elementor-type="header" data-elementor-id="1396" class="elementor elementor-1396 elementor-location-header" data-elementor-settings="[]">
		<div class="elementor-section-wrap">
					<div class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-d6b945a elementor-section-height-min-height elementor-section-content-top elementor-section-full_width elementor-section-height-default elementor-section-items-middle" data-id="d6b945a" data-element_type="section" data-settings="{&quot;background_background&quot;:&quot;classic&quot;,&quot;sticky&quot;:&quot;top&quot;,&quot;sticky_on&quot;:[&quot;desktop&quot;],&quot;sticky_offset&quot;:0,&quot;sticky_effects_offset&quot;:0}">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-1adcfc5b" data-id="1adcfc5b" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-54319142 elementor-widget__width-auto elementor-widget-tablet__width-auto elementor-widget elementor-widget-image" data-id="54319142" data-element_type="widget" data-widget_type="image.default">
				<div class="elementor-widget-container">
								<div class="elementor-image">
													<a href="https://doctrineandcovenantscentral.org">
							<img width="300" height="126" src="https://doctrineandcovenantscentral.org/wp-content/uploads/2020/12/DC-1-crop-300x126.png" class="attachment-medium size-medium" alt="" loading="lazy" srcset="https://doctrineandcovenantscentral.org/wp-content/uploads/2020/12/DC-1-crop-300x126.png 300w, https://doctrineandcovenantscentral.org/wp-content/uploads/2020/12/DC-1-crop-1024x432.png 1024w, https://doctrineandcovenantscentral.org/wp-content/uploads/2020/12/DC-1-crop-768x324.png 768w, https://doctrineandcovenantscentral.org/wp-content/uploads/2020/12/DC-1-crop-1536x647.png 1536w, https://doctrineandcovenantscentral.org/wp-content/uploads/2020/12/DC-1-crop-2048x863.png 2048w" sizes="100vw" />								</a>
														</div>
						</div>
				</div>
				<div class="elementor-element elementor-element-91e3eb5 elementor-widget__width-auto elementor-widget elementor-widget-heading" data-id="91e3eb5" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default"><a href="/">Doctrine and <br>Covenants Central</a></h2>		</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-741791c9" data-id="741791c9" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-7f969a2a elementor-nav-menu__align-right elementor-nav-menu--stretch elementor-nav-menu__text-align-center elementor-nav-menu--indicator-classic elementor-nav-menu--dropdown-tablet elementor-nav-menu--toggle elementor-nav-menu--burger elementor-widget elementor-widget-nav-menu" data-id="7f969a2a" data-element_type="widget" data-settings="{&quot;full_width&quot;:&quot;stretch&quot;,&quot;layout&quot;:&quot;horizontal&quot;,&quot;toggle&quot;:&quot;burger&quot;}" data-widget_type="nav-menu.default">
				<div class="elementor-widget-container">
						<nav role="navigation" class="elementor-nav-menu--main elementor-nav-menu__container elementor-nav-menu--layout-horizontal e--pointer-none"><ul id="menu-1-7f969a2a" class="elementor-nav-menu"><li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-333"><a href="/sections/" class="elementor-item">Sections</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-114"><a class="elementor-item">Overviews</a>
<ul class="sub-menu elementor-nav-menu--dropdown">
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-17849"><a href="/people-of-the-dc" class="elementor-sub-item">People of the D&#038;C</a></li>
	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-7759"><a href="https://doctrineandcovenantscentral.org/places-of-the-doctrine-and-covenants/" class="elementor-sub-item">Places of the D&#038;C</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-31822"><a href="https://doctrineandcovenantscentral.org/church-history-matters-podcast/" class="elementor-item">Podcast</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-22083"><a href="https://doctrineandcovenantscentral.org/knowhys" class="elementor-item">KnoWhys</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-116"><a class="elementor-item">Media</a>
<ul class="sub-menu elementor-nav-menu--dropdown">
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-19999"><a href="https://www.youtube.com/channel/UCqtKadDOHIbx_Zjq9BhxQYg/featured" class="elementor-sub-item">Videos</a></li>
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-20000"><a href="https://archive.bookofmormoncentral.org/category/media" class="elementor-sub-item">Images</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-20142"><a href="https://doctrineandcovenantscentral.org/library/" class="elementor-item">Library</a></li>
</ul></nav>
					<div class="elementor-menu-toggle" role="button" tabindex="0" aria-label="Menu Toggle" aria-expanded="false">
			<i class="eicon-menu-bar" aria-hidden="true"></i>
			<span class="elementor-screen-only">Menu</span>
		</div>
			<nav class="elementor-nav-menu--dropdown elementor-nav-menu__container" role="navigation" aria-hidden="true"><ul id="menu-2-7f969a2a" class="elementor-nav-menu"><li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-333"><a href="/sections/" class="elementor-item">Sections</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-114"><a class="elementor-item">Overviews</a>
<ul class="sub-menu elementor-nav-menu--dropdown">
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-17849"><a href="/people-of-the-dc" class="elementor-sub-item">People of the D&#038;C</a></li>
	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-7759"><a href="https://doctrineandcovenantscentral.org/places-of-the-doctrine-and-covenants/" class="elementor-sub-item">Places of the D&#038;C</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-31822"><a href="https://doctrineandcovenantscentral.org/church-history-matters-podcast/" class="elementor-item">Podcast</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-22083"><a href="https://doctrineandcovenantscentral.org/knowhys" class="elementor-item">KnoWhys</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-116"><a class="elementor-item">Media</a>
<ul class="sub-menu elementor-nav-menu--dropdown">
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-19999"><a href="https://www.youtube.com/channel/UCqtKadDOHIbx_Zjq9BhxQYg/featured" class="elementor-sub-item">Videos</a></li>
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-20000"><a href="https://archive.bookofmormoncentral.org/category/media" class="elementor-sub-item">Images</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-20142"><a href="https://doctrineandcovenantscentral.org/library/" class="elementor-item">Library</a></li>
</ul></nav>
				</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</div>
				</div>
		</div>
				<div data-elementor-type="single-post" data-elementor-id="31897" class="elementor elementor-31897 elementor-location-single post-31913 podcast-episode type-podcast-episode status-publish hentry category-first-vision" data-elementor-settings="[]">
		<div class="elementor-section-wrap">
					<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-697675b4 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="697675b4" data-element_type="section" data-settings="{&quot;background_background&quot;:&quot;classic&quot;}">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-7abd009e" data-id="7abd009e" data-element_type="column" data-settings="{&quot;background_background&quot;:&quot;classic&quot;}">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-563f4fb8 elementor-icon-list--layout-traditional elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list" data-id="563f4fb8" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items">
							<li class="elementor-icon-list-item">
					<a href="https://doctrineandcovenantscentral.org/podcast-first-vision/">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-arrow-left"></i>						</span>
										<span class="elementor-icon-list-text">Back</span>
											</a>
									</li>
						</ul>
				</div>
				</div>
				<div class="elementor-element elementor-element-3b2c9b89 elementor-widget elementor-widget-image" data-id="3b2c9b89" data-element_type="widget" data-widget_type="image.default">
				<div class="elementor-widget-container">
								<div class="elementor-image">
												<img width="525" height="525" src="https://doctrineandcovenantscentral.org/wp-content/uploads/2023/07/first-visions-anthony-sweat-square-crop-1024x1024.jpeg" class="attachment-large size-large" alt="Detail from “The First Visions” by Anthony Sweat" loading="lazy" srcset="https://doctrineandcovenantscentral.org/wp-content/uploads/2023/07/first-visions-anthony-sweat-square-crop-1024x1024.jpeg 1024w, https://doctrineandcovenantscentral.org/wp-content/uploads/2023/07/first-visions-anthony-sweat-square-crop-300x300.jpeg 300w, https://doctrineandcovenantscentral.org/wp-content/uploads/2023/07/first-visions-anthony-sweat-square-crop-150x150.jpeg 150w, https://doctrineandcovenantscentral.org/wp-content/uploads/2023/07/first-visions-anthony-sweat-square-crop-768x768.jpeg 768w, https://doctrineandcovenantscentral.org/wp-content/uploads/2023/07/first-visions-anthony-sweat-square-crop-100x100.jpeg 100w, https://doctrineandcovenantscentral.org/wp-content/uploads/2023/07/first-visions-anthony-sweat-square-crop.jpeg 1080w" sizes="100vw" />														</div>
						</div>
				</div>
				<div class="elementor-element elementor-element-466d9d4 elementor-widget elementor-widget-heading" data-id="466d9d4" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Art Credit:&nbsp;Anthony Sweat</h2>		</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-2a780d2d" data-id="2a780d2d" data-element_type="column" data-settings="{&quot;background_background&quot;:&quot;classic&quot;}">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-11be19d0 elementor-widget elementor-widget-heading" data-id="11be19d0" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Joseph Smith's First Vision&nbsp;|&nbsp;</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-6fcc9d0c elementor-widget elementor-widget-heading" data-id="6fcc9d0c" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default"> Episode 4</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-524f0398 elementor-widget elementor-widget-heading" data-id="524f0398" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">How Do 2nd and 3rd Hand Accounts Add to Our Understanding of the First Vision?​</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-7e3e7a59 elementor-widget elementor-widget-heading" data-id="7e3e7a59" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">47 min</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-37fcf4e2 elementor-widget elementor-widget-text-editor" data-id="37fcf4e2" data-element_type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
								<div class="elementor-text-editor elementor-clearfix">
					<p>Thousands of people heard Joseph Smith’s testimony first hand. Some of those testimonies included him telling about his First Vision experience. Some of those people who heard his witness wrote down the details of what they heard. Luckily, a few of those handwritten accounts have survived until today and some of them contain even more details about Joseph’s vision which add to our understanding of what happened in 1820 in the Sacred Grove in Palmyra, New York. In today&#8217;s episode we explore three of these second hand accounts and then one bonus third-hand account which contains a significant detail that no other account ever mentions.</p>
					</div>
						</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-13b45d73 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="13b45d73" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-ce89e9c" data-id="ce89e9c" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-3d0322c8 elementor-widget elementor-widget-heading" data-id="3d0322c8" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Joseph Smith's First Vision | </h2>		</div>
				</div>
				<section class="has_eae_slider elementor-section elementor-inner-section elementor-element elementor-element-1028e89e elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="1028e89e" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-inner-column elementor-element elementor-element-324d2474" data-id="324d2474" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-3a9e6ff2 elementor-widget elementor-widget-shortcode" data-id="3a9e6ff2" data-element_type="widget" data-widget_type="shortcode.default">
				<div class="elementor-widget-container">
					<div class="elementor-shortcode"><iframe height="150" width="100%" style="border: none;height:150px" scrolling="no" src="https://www.podbean.com/player-v2/?from=embed&amp;i=ndm2r-13c0495-pb&amp;share=1&amp;download=1&amp;fonts=Arial&amp;skin=1&amp;font-color=&amp;rtl=0&amp;logo_link=&amp;btn-skin=7&amp;size=150"></iframe></div>
				</div>
				</div>
				<div class="elementor-element elementor-element-3101fa02 elementor-widget elementor-widget-eael-adv-tabs" data-id="3101fa02" data-element_type="widget" data-widget_type="eael-adv-tabs.default">
				<div class="elementor-widget-container">
			        <div id="eael-advance-tabs-3101fa02" class="eael-advance-tabs eael-tabs-horizontal active-caret-on" data-tabid="3101fa02">
            <div class="eael-tabs-nav">
                <ul class="eael-tab-inline-icon">
                                            <li class="inactive">
                                                         <span class="eael-tab-title">Show Notes</span>
                        </li>
                                            <li class="inactive">
                                                         <span class="eael-tab-title">Transcript</span>
                        </li>
                                    </ul>
            </div>
            <div class="eael-tabs-content">

                    <div class="clearfix inactive">
                                                    <style>.elementor-31853 .elementor-element.elementor-element-326b558 .elementor-heading-title{color:var( --e-global-color-text );font-family:"Raleway", Sans-serif;font-size:1em;font-weight:600;font-style:normal;}.elementor-31853 .elementor-element.elementor-element-22bf92a .elementor-heading-title{color:var( --e-global-color-text );font-family:"Raleway", Sans-serif;font-size:1em;font-weight:600;font-style:normal;}.elementor-31853 .elementor-element.elementor-element-ef2fb4d{font-family:"Raleway", Sans-serif;font-size:1em;font-weight:400;}.elementor-31853 .elementor-element.elementor-element-937dc7f .elementor-heading-title{color:var( --e-global-color-text );font-family:"Raleway", Sans-serif;font-size:1em;font-weight:600;font-style:normal;}/* Start custom CSS for text-editor, class: .elementor-element-ef2fb4d */.elementor-31853 .elementor-element.elementor-element-ef2fb4d ul li{
    margin-bottom:1em;
}


.elementor-31853 .elementor-element.elementor-element-ef2fb4d ul li ol li {
    margin-bottom:0em;
    margin-top:.4em;
}/* End custom CSS */</style>		<div data-elementor-type="section" data-elementor-id="31853" class="elementor elementor-31853 elementor-location-single" data-elementor-settings="[]">
		<div class="elementor-section-wrap">
					<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-a42ed86 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="a42ed86" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-18f40bb" data-id="18f40bb" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-a6391fd elementor-widget elementor-widget-text-editor" data-id="a6391fd" data-element_type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
								<div class="elementor-text-editor elementor-clearfix">
										</div>
						</div>
				</div>
				<div class="elementor-element elementor-element-22bf92a elementor-widget elementor-widget-heading" data-id="22bf92a" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Key Takeaways</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-ef2fb4d elementor-widget elementor-widget-text-editor" data-id="ef2fb4d" data-element_type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
								<div class="elementor-text-editor elementor-clearfix">
					<ul>
<li>Levi Richards&#8217; account of Joseph Smith&#8217;s first vision adds a key reference to God&#8217;s everlasting covenant—shedding light on what&#8217;s at the heartbeat of the purpose of the Restoration.</li>
<li>David Nye White was a a non-Latter-day Saint who interviewed Joseph Smith and then published his account.</li>
<li>Alexander Neibaur, a German convert whom Joseph Smith was close to, recorded some unique details about the description of the God the Father that are not found in any other account.</li>
</ul>
					</div>
						</div>
				</div>
				<div class="elementor-element elementor-element-937dc7f elementor-widget elementor-widget-heading" data-id="937dc7f" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Related Resources</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-6729dbb elementor-widget elementor-widget-text-editor" data-id="6729dbb" data-element_type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
								<div class="elementor-text-editor elementor-clearfix">
					<p class="p1">Gospel Topics Essay, “<a class="blue-link" href="https://www.churchofjesuschrist.org/study/manual/gospel-topics-essays/first-vision-accounts?lang=eng">First Vision Accounts</a>.” churchofjesuschrist.org.</p>
<p class="p1">“<a class="blue-link" href="https://www.josephsmithpapers.org/site/accounts-of-the-first-vision">Accounts of Joseph Smith’s First Vision</a>,” josephsmithpapers.org.</p>
					</div>
						</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				</div>
		</div>
		                                            </div>

                    <div class="clearfix inactive">
                                                    <style></style>		<div data-elementor-type="section" data-elementor-id="31877" class="elementor elementor-31877 elementor-location-single" data-elementor-settings="[]">
		<div class="elementor-section-wrap">
					<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-fe6aa09 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="fe6aa09" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-d2b1db0" data-id="d2b1db0" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-dc21b84 elementor-widget elementor-widget-text-editor" data-id="dc21b84" data-element_type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
								<div class="elementor-text-editor elementor-clearfix">
					<p>Scott Woodward:   <br />
Hi. This is Scott from Church History Matters. As we near the end of this series, we want to hear your questions about Joseph Smith&#8217;s First Vision. Next week we will be honored to have with us a special guest, Dr. Steven C. Harper, a church historian and scholar of the First Vision, to help us respond to your questions. So you can record yourself asking your question anytime up to March 29, 2023. That&#8217;s tomorrow if you&#8217;re listening to this on today&#8217;s episode&#8217;s release date. And send it in to info@scripturecentral.org. Let us know your name, where you&#8217;re from, and try to keep it to about 20 seconds or so. Also, please transcribe your question when you email it in. That helps out a lot. Okay. Now on to the episode. Thousands of people heard Joseph Smith&#8217;s testimony firsthand. Some of those testimonies included him telling about his First Vision experience, and some of those people who heard his witness wrote down the details of what they heard. Luckily, a few of those accounts have survived until today, and some of them contain even more details about Joseph&#8217;s vision, which add to our understanding of what happened in 1820 in the Sacred Grove in Palmyra, New York. Today on Church History Matters, we explore three of these secondhand accounts, and then one bonus thirdhand account, which contains a significant detail that no other account ever mentions. I&#8217;m Scott Woodward, a Managing Director at Scripture Central, and my co-host is Casey Griffiths, also a Managing Director at Scripture Central. This is our fourth episode in this series dealing with Joseph Smith&#8217;s First Vision. Now, let&#8217;s get into it.</p>
<p>Casey Paul Griffiths: <br />
All right. Hi, Scott.</p>
<p>Scott Woodward:   <br />
Hi, Casey.</p>
<p>Casey Paul Griffiths: <br />
How we doing?</p>
<p>Scott Woodward:   <br />
So good. So excited to dig into some more First Vision.</p>
<p>Casey Paul Griffiths: <br />
Good. Well, we&#8217;re just gonna dive right in.</p>
<p>Scott Woodward:   <br />
Yes.</p>
<p>Casey Paul Griffiths: <br />
Let&#8217;s recap really fast what we&#8217;ve talked about, and then we&#8217;ll get to our subject today. So Scott, give us a little recap of where we&#8217;ve been already.</p>
<p>Scott Woodward:   <br />
Okay. Well, in this series, we&#8217;ve been talking about Joseph Smith&#8217;s First Vision as a foundational narrative of The Church of Jesus Christ of Latter-day Saints. We&#8217;ve talked about how, over time, it&#8217;s grown in its significance for members of the church and for how we tell the narrative of our church&#8217;s history. It&#8217;s become just central to that story.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
And in our last few episodes, we&#8217;ve been diving into Joseph Smith&#8217;s four firsthand accounts of his First Vision: the 1832, ’35, ’38, and 1842 accounts. And what we&#8217;ve been trying to do is first to explain the context in which each account was written and then to look at the unique elements of each account and then, third, to highlight how the context helps illuminate the content, right? Why would Joseph say that, or why would he withhold certain details or facts based on the people to whom he&#8217;s speaking? And so should we try this? Should we try to do a quick—how fast do you think we can recap this?</p>
<p>Casey Paul Griffiths: <br />
Pretty fast. I&#8217;ll do 1832.</p>
<p>Scott Woodward:   <br />
Okay. Let&#8217;s see it.</p>
<p>Casey Paul Griffiths: <br />
1832 is the earliest account, but the last known to the general public. It&#8217;s very personal. It represents a soul searching on Joseph Smith&#8217;s part.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
It includes a lot of personal details about Joseph Smith&#8217;s kind of inner world, but it&#8217;s also a little bit controversial, because it could be interpreted to read that Joseph just saw Jesus Christ. So it&#8217;s maybe the juiciest of the accounts, but it&#8217;s also beautiful and really wonderful.</p>
<p>Scott Woodward:   <br />
Well, I just have to say you were so good at highlighting when we talked about that that Joseph had just been in Indiana, and he had just been, like, soul searching in a grove there.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
You know, he&#8217;s kind of in a introspective, reflective mode during that time period. I thought that was really interesting historical context.</p>
<p>Casey Paul Griffiths: <br />
Yeah. My read is that he&#8217;s sorting through some feelings.</p>
<p>Scott Woodward:   <br />
Yes. 1835 account.</p>
<p>Casey Paul Griffiths: <br />
1835, let&#8217;s hear it.</p>
<p>Scott Woodward:   <br />
So this is written—it&#8217;s a journal entry from one of Joseph&#8217;s scribes. Joseph had a conversation with a really interesting fellow, an odd duck, a visitor who&#8217;d just come into Kirtland named Joshua. He had styled himself as a Jewish prophet, and before Joseph learned that he was actually, like, a guy who&#8217;d been tried for murder and manslaughter and child abuse, Joseph had shared with him an account of his First Vision. The two, I think, most important and interesting things about the context on this one were first, that this is to a stranger, and I think that accounts well for why Joseph focuses on objective details with very little personal feeling, right, in contrast to 1832 account. And the second, I think, important historical context is that Joseph understood that he was talking to a Jew.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
Which explains why he de-emphasized the more Christian cultural aspects of his experience, like the revivals and the search for the true Christian church, right? He just talked about looking for different systems of religion, right? And it also, I think, highlights why he, why he highlights more Jewish-friendly aspects of the vision, like his wrestle with darkness, this ordeal, and pillar of fire. That&#8217;s the only account he uses fire, and that&#8217;s very Old Testament, shekhinah-type language. The many angels, he mentions the many angels in this account, which is a nod to the divine counsel. So ’35 is interesting because it&#8217;s to a Jewish stranger. Okay, how about ’38? You want to do a ’38?</p>
<p>Casey Paul Griffiths: <br />
’38 is the one most people are familiar with. It&#8217;s the canonized accounts found in the Pearl of Great Price. It happens in the midst of serious persecution, both internal and external. Joseph Smith has fled from Kirtland because of internal problems, gets to Missouri where there&#8217;s external problems happening, and so it has kind of a defensive tone. I&#8217;m telling this to let people know exactly what happened, to put inquirers after the truth into possession of the facts. Joseph goes into a lot of things about grounding his experiences in the Bible. It also presents a good model for how any seeker can find the truth themselves, that you study the scriptures, ask God, expect opposition, but God will speak to you and give you the answer, and then you can expect opposition again, because another thing the 1838 account emphasizes is the reception of the First Vision, that Joseph Smith went and told a clergyman about it and didn&#8217;t really get the nicest response. So it&#8217;s the one most people are familiar with, and probably the most polished of the First Vision accounts, because Joseph Smith has several people help him with it when he&#8217;s writing.</p>
<p>Scott Woodward:   <br />
Excellent. Okay, 1842. That was our last episode. We talked about that this account comes because of an invitation of a non-Latter-day-Saint newspaper editor named John Wentworth. And so he asked Joseph to compose a sketch of the rise and progress and persecution and faith of Latter-day Saints. Wentworth actually was requesting his history on behalf of his friend George Barstow, who was then preparing a history of the state of New Hampshire. But in Wentworth&#8217;s request, Joseph seemed to sense an opportunity to capitalize on the growing national interest in the church.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
This is at the height of Joseph&#8217;s strength and prosperity. The church has become more respected, more of a force to be reckoned with, especially politically, in the public mind.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
So this time Joseph is more bold and confident than ever, and that, I think, explains the real self-assured, straightforward, matter-of-fact tone of this account. You know, for example, he&#8217;ll say that none of the churches were acknowledged of God as his church and kingdom. I think that&#8217;s pretty bold to say. But he was promised that the fulness of the gospel should at some future time be made known to him. And the fact that this is to a genuinely interested but non-LDS audience signals this missionary nature of the text, right? This is very much a missionary text.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
In fact, we talked about how Joseph will borrow language, sometimes exact phrases, for this account from Orson Pratt&#8217;s 1840 missionary pamphlet that he published in Scotland.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
Pratt&#8217;s was already a polished, concise, informative telling of the details of Joseph&#8217;s experience, and it was already calibrated as a missionary text, and so I just think it&#8217;s real interesting that 1842 is actually intended as a missionary text, but we often will quote from 1838 as missionaries. It could be used, of course, as a missionary text, 1838, but ’42 was, like, deliberately written in that way, so . . .</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
Anyways, there you go. There&#8217;s ’42. How&#8217;d we do?</p>
<p>Casey Paul Griffiths: <br />
Good. Good. Now, we mentioned briefly Orson Pratt. Orson Pratt and Orson Hyde both give official church publications that are accounts of the First Vision. Orson Pratt&#8217;s is published in Scotland. It&#8217;s actually the first published account of the First Vision. Orson Hyde&#8217;s is published in Germany, has to be translated from German, but you can found it at the Joseph Smith Papers site. And with that lead-in, today we&#8217;re going to be talking about some other secondary accounts of the First Vision. Orson Pratt and Orson Hyde are the most famous. But we&#8217;ve picked a couple here. We didn&#8217;t pick all of them, because there&#8217;s actually a lot more than you think once you start digging into it, but most of them are just brief references to Joseph testified that he&#8217;d seen the Father and the Son. These ones are ones that contain details and that came from someone—we made one exception—that heard it directly from Joseph Smith himself, but wrote it down.</p>
<p>Scott Woodward:   <br />
Yes.</p>
<p>Casey Paul Griffiths: <br />
We&#8217;re going to start with Levi Richards. Levi Richards’ account was recorded in June of 1843, 11th June 1843. And so let me tell you a little bit about Levi here. Levi is one of those people that pops up a lot in early church history but isn&#8217;t well-known. He is the older brother of Willard Richards, who&#8217;s a member of the Quorum of the Twelve and a member of the First Presidency. And Levi was in the middle of things. In Nauvoo, he&#8217;s a member of the Council of Fifty. He is a member of the Anointed Quorum. That&#8217;s the group that receives the temple ordinances first.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
He&#8217;s a Latter-day Saint from 1836 on, gets baptized, goes to Ohio, goes to Nauvoo, also serves a mission in Britain, actually winds up in the mission presidency of the British mission. Like I said, is in the middle of things. In fact, Nauvoo might be when Levi Richards was most closely involved in things and plays a big role there.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
Travels west. He lives in downtown Salt Lake, right where the City Creek Center is located today, is a patriarch in the church when he dies. So he&#8217;s true blue, through and through, all the way Latter-day Saint, but he does record some interesting details about the First Vision that we don&#8217;t see other places and that might be interesting, given the context that this happens in Nauvoo. So, Scott, you want to tell us a little bit about his account and what he says?</p>
<p>Scott Woodward:   <br />
Yeah, you bet. So this comes from his own history, his own journal, on the 11th of June, 1843. In fact, I talked to Andrew Ehat, who&#8217;s done a ton of research. He put together a fantastic book called The Words of Joseph Smith, kind of recollections of people in Nauvoo, their written accounts of Joseph&#8217;s sermons. I actually gave a presentation once about this account, or this was a heavy piece of my presentation, and I didn&#8217;t know that Andy Ehat was actually in the audience, and he came up afterwards and he said, “Hey, so you like that account I found?” And I said, “You found this?” He said, “Yeah.” He said, “Yeah, that was a gem.” I can&#8217;t remember where he told me he found it, but he was excited that it was being used and that we&#8217;re talking about it. I&#8217;ll just read a little bit of an excerpt from it. He says he attended a meeting at the temple. The weather was very fine, warm. And then Joseph Smith preached from Matthew. And then another guy got up and preached from the Hebrews chapter 6. And then there&#8217;s a break, and it says “At 6 a. m.,” And Andy Ehat said, “I am almost positive that should be p. m., but it seems like he made a mistake there.” Otherwise, that previous meeting was, uh, very early in the morning.</p>
<p>Casey Paul Griffiths: <br />
The long meeting. Yeah, very long.</p>
<p>Scott Woodward:   <br />
Yeah. So, probably 6 p. m. This is key context. He said, “He heard Elder George Adams preach upon the Book of Mormon, and he proved from the 24th, 28th, and 29th chapters of Isaiah that, ‘the everlasting covenant set by Christ and the apostles had been broken.’” Isaiah uses that phrase, that they&#8217;ve “broken mine everlasting covenant.” And then he says that Joseph, after George Adams had taught that, used that phrase, the everlasting covenant has been broken, that seemed to trigger something in Joseph&#8217;s mind. Because Joseph Smith then will preach again right after that. He says, “President Joseph Smith bore testimony to the same,” meaning to that same truth, that the everlasting covenant had been broken, “saying that when he was a youth, he began to think about these things but could not find out which of all the sects were right. He went into the grove and inquired of the Lord which of all the sects were right. He received for answer that none of them were right, that they were all wrong, and that the everlasting covenant was broken.” That&#8217;s a detail we did not have in any of Joseph&#8217;s first ten accounts, and that&#8217;s a big deal. What we did have was in the ’42 account that the Lord said that the fullness of the everlasting gospel was soon to be, or would at some future day be made known unto him, right? But he didn&#8217;t say anything about everlasting covenant. Later on, in the Doctrine and Covenants, the Lord will actually equate those terms. He&#8217;ll equate everlasting covenant and the fulness of the gospel. I&#8217;ll just throw out a few references, like D&amp;C 66:2, he says, “mine everlasting covenant, even the fulness of my gospel.” D&amp;C 39:11, “the fullness of my gospel, the covenant which I&#8217;ve sent forth.” One more, D&amp;C 133:57. He says, “the Lord sent forth the fullness of his gospel, his everlasting covenant.” And so I think that&#8217;s important to tie Levi Richards’ account to the 1842 account. The Lord said that the fullness of the gospel would at some future day be made known unto him, and the Levi Richards account’s saying that the everlasting covenant had been broken. Whatever the gospel plan is and whatever the ancients understood it to be and what Joseph would understand it to be, that system was not working in 1820. And the Lord declared as much, according to Levi Richards’ account, saying that that everlasting covenant’s not working. It&#8217;s not fully functioning. There&#8217;s pieces missing, or there&#8217;s some functionality that&#8217;s missing.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
One more thought on that is D&amp;C section 1, and this is, what, 1831 November? A little more than a year and a half since the church has been organized. He was talking about the idolatry in the world, and he&#8217;s talking about people in the world, and he says, “they have strayed from my ordinances,” that would mean, like, my laws, “and have broken mine everlasting covenant.” There&#8217;s that phrase again. And then he makes a case for why he called Joseph Smith to be his servant in the last days. One of the reasons is verse 22, “that mine everlasting covenant might be established.” Next verse, “that the fulness of my gospel might be proclaimed by the weak and simple unto the ends of the world.” so this seems to be, like, at the heartbeat of the Restoration is we need to get back into place the fulness of the gospel or the everlasting covenant, the way by which mankind and God can cooperate and collaborate together to help bring about the salvation of mankind, so . . .</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
I find that to be a really interesting detail, and it seems to have been sparked by George Adams’ preaching. He mentioned the phrase, and Joseph says, I&#8217;d like to second that. And then he tells that little detail about the First Vision after George had sparked that memory in his mind, so . . .</p>
<p>Casey Paul Griffiths: <br />
Yeah. Two things stand out to me: In Levi&#8217;s notes, he says, “One of the people that preached, Elder D. Wolf, an Episcopalian clergyman,” and I don&#8217;t know if this means he was an Episcopalian clergyman that converted and had immigrated to Nauvoo or if he was just—Joseph Smith would often have people from other faiths come and talk to the Saints.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
But in that clergyman&#8217;s presence, Joseph Smith has no problem saying, I inquired of the Lord which of the sects were right and received the answer that none of them were right. If this guy is an Episcopalian clergyman, Joseph Smith is bold about it. The other thing that struck me is Richards is part of the Anointed Quorum. So at this point, the temple ordinances have been put back in place, and Joseph Smith is performing sealings in Nauvoo.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
And you can look up the page that Levi writes these notes on. He—it looks like he&#8217;s just writing as fast as he can. I think that would have stood out to Levi, that he&#8217;s already been engaged in these ceremonies that are supposed to restore the everlasting covenant, and so he writes down that this was in the works since 1820. It&#8217;s 23 years later, and they&#8217;re finally putting the last pieces in place that will restore the everlasting covenant once and for all, so. . .</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
It&#8217;s a little gem of an account there. It&#8217;s not very long, but it does have some really fascinating details to it.</p>
<p>Scott Woodward:   <br />
Yeah. Could I say one more thing about this idea that all the sects were wrong? That&#8217;s the quote. “That they were all wrong, and that the everlasting covenant was broken.”</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
I do worry sometimes that that comes across as so condemnatory of our brothers and sisters who are Christian, or disrespectful, or really bad PR, or I don&#8217;t know what. It doesn&#8217;t land very well: “They were all wrong.”</p>
<p>Casey Paul Griffiths: <br />
Right.</p>
<p>Scott Woodward:   <br />
But Joseph also will say in Nauvoo that, do the Presbyterians have any truth? Yes. Do the Baptists have truth? Yes. He said they all have truth, mingled with some error. He said in our job as Mormons, true Mormonism, he said, is to receive all truth, let it come from whence it may. You can get truth from the Baptists and the Presbyterians and the Catholics and Methodists. They&#8217;ve all got truth. When it says they were all wrong, it doesn&#8217;t mean that they completely believe in falsehood, right? I think tying it to the everlasting covenant is the key here. What makes them wrong is that they have a form of godliness, but they can&#8217;t tap into the power thereof.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
The ordinances, the laws by which you connect formally with God and thereby become his children and heirs of the kingdom of God, that formal process, was broken. Therefore, none of the religions was “right,” air quotes, in that sense, because no matter what truth they&#8217;re teaching, it&#8217;s all—it&#8217;s true. They&#8217;re teaching from the Bible. They’ve got a lot of truth. But ultimately, propositional statements from the Bible that are true are not going to help you connect directly with God in that formal, born again process and then growing up to becoming heirs of the kingdom of God. You have to have the power of godliness to do that, and that&#8217;s only made possible through the everlasting covenant.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
So I think that&#8217;s the context. They were all wrong because the everlasting covenant&#8217;s broken. That&#8217;s the way in which they&#8217;re wrong, if that makes sense.</p>
<p>Casey Paul Griffiths: <br />
Right. That makes sense. All right, let&#8217;s keep moving along. The next one is same summer. Levi&#8217;s account is written down in June. This one&#8217;s written down on the 21st of August, 1843. And what&#8217;s interesting about this one is it&#8217;s given to a reporter, a non-Latter-day Saint, David Nye White. White is an interesting fellow. He&#8217;s a reporter for the Pittsburgh Gazette. He&#8217;s also the editor, partial owner of the Pittsburgh Gazette, and he&#8217;s in Nauvoo looking for stories, basically. We don&#8217;t know a lot about the context of why he comes to Nauvoo, but a big scan of his life is that he was an abolitionist. In fact, ten years after this, in 1855, he calls for a new party, and several people gather with him, they nominate a ticket, and this is one of the attributed starting points of the Republican Party, which aren&#8217;t big fans of the Saints in the 19th century, but the Saints become big fans of them later on a little bit, so this is Joseph Smith speaking to someone who has no background, probably has not read the Book of Mormon or other similar restoration scriptures or any church tracts, and it&#8217;s someone looking at it with a reporter&#8217;s eye. So it&#8217;s a very succinct account, but it does contain a couple of details that aren’t found in other accounts, too. For instance—and by the way, when you look up the earliest version of this, which you can do on the Joseph Smith Papers site, you&#8217;ll see a newspaper article, not a written journal. So we don&#8217;t know how Knight may have edited this, too, that we should take it carefully there, but it reads, “I immediately went out into the woods, where my father had a clearing, went to the stump where I had stuck my axe when I had quit work, and kneeled down and prayed, saying, ‘O, Lord, what church shall I join?’ Directly I saw light, and then a glorious personage in the light, and then another personage, and the first personage said to the second, ‘Behold, my Beloved Son. Hear Him.’ I then addressed the second person saying, ‘O, Lord, what church shall I join?’ He replied, ‘Don&#8217;t join any of them. They are all corrupt.’ The vision then vanished, and when I came to myself, I was sprawling on my back, and it was some time before my strength returned. So a number of interesting details here, the stump and the axe, which if you&#8217;ve seen videos of the First Vision, the latest one, Ask of God, actually shows the stump and the axe that he goes to.</p>
<p>Scott Woodward:   <br />
Wow.</p>
<p>Casey Paul Griffiths: <br />
“O, Lord, what church shall I join?” His strength returning, which I think are in some of the other accounts, but this is kind of a matter-of-fact newspaper reporter writes down the account, give us a couple interesting details here.</p>
<p>Scott Woodward:   <br />
It almost sounds like a super simplified, like, children&#8217;s version. You know what I mean?</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
He goes out into a clearing where there&#8217;s a stump with an axe, and he kneels down, and he asks, ”O, Lord, what church shall I join?” Like, simple, simple, simple. Doesn&#8217;t go through any of the wrestle, none of the juicy details that the other accounts have. Nothing about seeking forgiveness of sin. This is all just a glorious personage comes, and then a second personage comes, and then he asked the second person, “O, Lord, what church shall I join?” I mean, it seems so simple. You know what I mean?</p>
<p>Casey Paul Griffiths: <br />
Yep.</p>
<p>Scott Woodward:   <br />
It just seems like a kid could just—I feel like I could see this in, like, a picture book version, like cartoon. I wonder how much David White simplified what he heard. Maybe this is his distillation of what Joseph told him, but regardless, it&#8217;s interesting.</p>
<p>Casey Paul Griffiths: <br />
It&#8217;s straightforward, right?</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
And this one probably does have a missionary track to it. Again, the question is where are White&#8217;s fingerprints on this? How does he manipulate or edit the record or change it or anything like that?</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
But it leaves out things like the opposition Joseph faced, the struggle leading up to it, even the searching for churches. It&#8217;s just pretty straightforward.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
And again, I mean, it&#8217;s written to an audience that would have almost no background in understanding it, so maybe if it&#8217;s directly from Joseph Smith without manipulation, it&#8217;s Joseph Smith saying, bare bones, here&#8217;s what happened.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
I prayed. I saw God. I saw Jesus Christ. I was told not to join any church, and then I moved on. Here I am in Nauvoo all these years later.</p>
<p>Scott Woodward:   <br />
Yeah. This is the elevator version, right? You&#8217;re on floor one, and by the time you get to floor seven, you have to tell them everything. So, bing! Here we go, 30 seconds. So what happened, Mr. Smith? Boom. That&#8217;s the elevator version.</p>
<p>Casey Paul Griffiths: <br />
Yeah, and that&#8217;s it. Pretty straightforward.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
White actually makes it into—he&#8217;s a collector for internal revenue in the state of Pennsylvania, member of the state House of Representatives, president at the Constitutional Convention in 1873–74, I assume that&#8217;s Pennsylvania&#8217;s constitution, but outside of that we don&#8217;t know a ton about him. We don&#8217;t have a ton of the context as to what questions were being asked, what was happening in their conversation as they met.</p>
<p>Scott Woodward:   <br />
And do we know when he published this?</p>
<p>Casey Paul Griffiths: <br />
Good question.</p>
<p>Scott Woodward:   <br />
Is that on—I should check that out on Joseph Smith Papers. Did he publish it within Joseph&#8217;s lifetime? I know the interview is the 29th of August, 1843. Do we know when that paper was published?</p>
<p>Casey Paul Griffiths: <br />
I don&#8217;t know, but I would guess not very long after.</p>
<p>Scott Woodward:   <br />
I&#8217;m looking right now. Oh, here you go. I just found it. An article that he called “The Prairies, Nauvoo, Joe Smith, the Temple, the Mormons, etc.” Pittsburgh Weekly Gazette, 15th of September, 1843. So, yeah, definitely in Joseph Smith&#8217;s lifetime. Cool.</p>
<p>Casey Paul Griffiths: <br />
Yep, so just a couple weeks after he gets back from Nauvoo, it sounds like he writes all this down and publishes it in his paper, so . . .</p>
<p>Scott Woodward:   <br />
Yeah, okay.</p>
<p>Casey Paul Griffiths: <br />
Very succinct, very straightforward.</p>
<p>Scott Woodward:   <br />
Nice.</p>
<p>Casey Paul Griffiths: <br />
Next one is Alexander Neibaur, and I hope I&#8217;m saying that right, could be nye-bower, is an interesting figure. He&#8217;s a dentist. He is the first Jewish person we know of to join The Church of Jesus Christ of Latter-day Saints. He is German by nativity. He&#8217;s fluent in seven languages.</p>
<p>Scott Woodward:   <br />
Wow.</p>
<p>Casey Paul Griffiths: <br />
Was an establisher of dental schools in America, and at first was going to be a rabbi, but then decided to change the course of his career and be a surgeon and a dentist. So he moves to Preston, England, and it&#8217;s in England, I believe, that he converts. He reads the Book of Mormon, the whole thing in three days—</p>
<p>Scott Woodward:   <br />
Wow.</p>
<p>Casey Paul Griffiths: <br />
—but put off being baptized until the following spring and then gets baptized on the 9th of April, 1838. He emigrates to America, where he becomes fast friends with Joseph Smith. He&#8217;s the dentist in Nauvoo, so you imagine this German dentist down the road. He also has a knowledge of Hebrew and apparently was Joseph Smith&#8217;s tutor when it came to German and Hebrew. And so you see, when you read the King Follett Sermon, for instance, that Joseph Smith says, “I think the Germans have got a better translation of the Bible than anybody else.” That&#8217;s probably Alexander Niebaur helping him out there. Joseph Smith also, later on in his life, liked to play around with Hebrew phraseology in the King Follett sermon. So that&#8217;s probably Alexander Niebaur’s doing. And just of interest to us, Niebaur emigrates to Utah, continues to practice dentistry. He is the progenitor of a number of important folks, like Charles Nibley is linked to him, and his descendants are Hugh Nibley, Reed Nibley, Richard Nibley, all these great gospel scholars that kind of come into their prominence in the 20th century are linked back to Alexander Niebaur, so he&#8217;s kind of an intellectual fellow.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
Fluent in different languages, steeped in Judaism, delivers an interesting account of the First Vision. Scott, why don&#8217;t you tell us a little bit about his account and what it says?</p>
<p>Scott Woodward:   <br />
Yeah. This is from his journal, 24th of May, 1844. So that&#8217;s really about one month before Joseph Smith dies, right? Joseph will die on June 27th.</p>
<p>Casey Paul Griffiths: <br />
Yep.</p>
<p>Scott Woodward:   <br />
So just a month before Joseph&#8217;s death, he says this, according to Alexander&#8217;s Journal: “His tongue was cleaveth to his roof,” cleaving to the roof of his mouth, “could not utter a word, felt easier after a while, saw a fire towards heaven, came nearer and nearer, saw a personage in the fire, light complexion, blue eyes, a piece of white cloth drawn over his shoulders, his right arm bare,” and then he says, “After a while, another person came to the side of the first.” Okay, so let&#8217;s just pause right there. That&#8217;s awesome. Two things stand out to me here: number one, he&#8217;s speaking to a guy who&#8217;s a former Jew, and he uses fire again. Joseph only uses fire twice, and in both contexts, it was to people who had Jewish backgrounds.</p>
<p>Casey Paul Griffiths: <br />
Or he thought had Jewish backgrounds, yeah.</p>
<p>Scott Woodward:   <br />
Exactly, yeah, with the first guy, yeah. But Joseph&#8217;s brain is calibrated toward his Jewish audience, that&#8217;s right. I saw fire, it came nearer and nearer, and then of course the second, the first person, who&#8217;s got to be God the Father, he said had light complexion, blue eyes, and a piece of white cloth drawn over his shoulders, but his right arm was bare, and then after a while, which accords with the other accounts, except 1838 doesn&#8217;t mention this, but after a while, another person came to the side of the first. Wow. And then he says, “Mr. Smith then asked, ‘Must I join the Methodist church?’ ‘No. They are not my people. They have all gone astray. There is none that doeth good, no, not one. But this is my Beloved Son. Hearken ye Him.’” And then he says, “The fire drew nigher, rested upon the tree, enveloped him.” That one actually has some potential issues, doesn&#8217;t it, in terms of chronology in comparison with the other accounts? In this case, he&#8217;s saying that God the Father is the one that answered him not to join any church, and then he said, “This is my Beloved Son. Hearken ye Him.” And then the fire drew nigh and rested on him and enveloped him. So his chronology is a little off on all of this, and even who&#8217;s speaking, if we&#8217;re going to judge this account by the composite of the other accounts, we&#8217;re going to say he got a few of those details wrong. But also some interesting details to think about.</p>
<p>Casey Paul Griffiths: <br />
And it looks like the account&#8217;s written in shorthand. Like, if you could look this up on the page, it’s him writing fast. It&#8217;s a little bit messy. But I&#8217;d also say this one&#8217;s significant because, like you mentioned, this is just over a month before Joseph Smith is going to go to Carthage Jail and is going to die. It’s him holding fast to what he&#8217;s always maintained: This is what I saw. This is what was important to me. I wonder sometimes about the details in this account, too. Like, the light complexion, blue eyes, cloth drawn over his shoulders.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
That&#8217;s interesting in the context in which this is happening in Nauvoo. And I don&#8217;t know why he says things like that to Niebaur specifically, but in the context of Nauvoo, those details are interesting.</p>
<p>Scott Woodward:   <br />
And why do you say in context of Nauvoo? What are you thinking about with Nauvoo?</p>
<p>Casey Paul Griffiths: <br />
Well, he&#8217;s talking about how they&#8217;re dressed, right? And some of these things he&#8217;s saying about how they&#8217;re dressed have, I don&#8217;t know, links to maybe temple clothing?</p>
<p>Scott Woodward:   <br />
Oh, like temple robes or something.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
I see.</p>
<p>Casey Paul Griffiths: <br />
That he&#8217;s describing them, you know, wearing clothes that might be similar to what Joseph is initiating into the temple ceremonies here.</p>
<p>Scott Woodward:   <br />
Oh, that&#8217;s interesting. And if you&#8217;re not familiar with the temple robes, I think the church has done a good job. There&#8217;s a little video that they&#8217;ve done showing the temple garment and robes. You can check that out to see what you think about that connection. That&#8217;s interesting.</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm.</p>
<p>Scott Woodward:   <br />
Because, yeah, there&#8217;s—you can see on the church&#8217;s video that it would kind of go over the shoulder. In this case it sounds like Niebaur’s saying they go over—it went over both shoulders. “Cloth was drawn over his shoulders, but his right arm was bare.’ That&#8217;s interesting.</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm. And after a while, the other person came to the side of the first. Yeah. And he also ties into the Methodist church, which goes back to the ’38 account where Joseph Smith says the church he felt most drawn to was the Methodist church. He felt some desire to be united with them. But, “This is my Beloved Son. Hearken ye Him.” “The fire drew nigher and rested upon the tree and enveloped him.” So a lot of cool different details in this one.</p>
<p>Scott Woodward:   <br />
Yeah. I just, I don&#8217;t know what—I don&#8217;t know what to do with this one in terms of, you know, because his chronology&#8217;s off. Maybe—I guess I&#8217;ve taken notes before, and if I wasn&#8217;t taking notes in the very moment it was being said, as I&#8217;m recalling, I could see how he&#8217;d get some of those details out of order, or which being was speaking. I&#8217;m gonna give him a charitable pass on the chronology and who was speaking and just say that those are some cool details that he&#8217;s highlighting there.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
What do you think about that? Charitable pass on the chronology?</p>
<p>Casey Paul Griffiths: <br />
Let&#8217;s give him a charitable pass. It&#8217;s not perfect, but I think the problem isn&#8217;t with the message, it&#8217;s just with the writing as fast as he can. He may have been recalling after the fact this conversation that he had and putting it down. But again, the last contemporary account before Joseph Smith goes to Carthage Jail.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
Now, we&#8217;ve got one more, and this one I kind of slipped in because it&#8217;s a sentimental favorite. The historical background of this one is a little shaky, to be honest with you, but it comes from a young man named Charles Lowe Walker, and it&#8217;s actually not his account of the First Vision. So this is technically a thirdhand account of the First Vision, and yet no reason to disbelieve it. Charles Walker is a young man in, I believe, Logan, Utah, who goes to testimony meeting and hears a man named John Alger share his testimony of hearing the First Vision when he was a young man. Now, information we have on John Alger is a little fragmentary, but we do know John Alger was baptized at age 11 in 1832, which means he would have been contemporary with Joseph Smith. That&#8217;s what it sounds like.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
He says, I heard this when I was a small boy. He travels in the Brigham Young Company, actually, in 1848 to Utah, stays there, and beyond that, we don&#8217;t know a lot about this fellow. But Charles Walker goes to the meeting. In fact, let me just read what Charles Walker&#8217;s journal says, because there&#8217;s some neat stuff in here we might need to process. “2nd of February, Thursday, 1893.” So that&#8217;s another thing is it&#8217;s a very late account. We&#8217;re talking 73 years after the event would have taken place, probably 60 years after John Alger heard Joseph Smith relate this. He said, “I attended fast meeting. Brother John Alger said while speaking of the prophet Joseph that when he, John, was a small boy, he heard the prophet Joseph relate his vision of seeing the Father and the Son, that God touched his eyes with His finger and said, ‘Joseph, this is my Beloved Son. Hear Him.’ As soon as the Lord had touched his eyes with his finger, he immediately saw the Savior.” Charles Walker even adds, “After the meeting, a few of us questioned him about the matter. He told us at the bottom of the meetinghouse steps that he was in the house of Father Smith in Kirtland when Joseph Smith made this declaration and that Joseph, while speaking of it, put his finger to his right eye, suiting the action with the word so as to illustrate and at the same time impress the occurrence on the minds of those unto whom he was speaking.” So that adds in one detail that is not found in any of the accounts.</p>
<p>Scott Woodward:   <br />
No.</p>
<p>Casey Paul Griffiths: <br />
That God touched Joseph Smith. So what do we do with this one, Scott? What do you think about this one?</p>
<p>Scott Woodward:   <br />
Yeah, it&#8217;s so interesting, right? You&#8217;ve highlighted the problem. So, historically speaking, right, history is just so inaccessible. We can&#8217;t actually get at it. The best we can do are these little, flickering flames of recollections, and this one, yeah, so this—he was a kid. He says he was a small boy when he heard it, it was over 60 years after the event, and this is now a thirdhand account. This is Charles Walker telling us what John Alger said at this meeting, so those things are—they&#8217;re not deal breakers. Doesn&#8217;t mean it couldn&#8217;t have happened.</p>
<p>Casey Paul Griffiths: <br />
Right.</p>
<p>Scott Woodward:   <br />
The biggest, I think, issue for me is that nobody else—we have no other accounts of anybody else talking about this.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
Like, that—I feel like if God the Father touched Joseph Smith&#8217;s right—by his right eye, and then that&#8217;s when he saw the Son, like, that seems like a really important detail that a lot of people would remember, and the fact that we only have one account 60 years after he heard Joseph purportedly say it . . .</p>
<p>Casey Paul Griffiths: <br />
Right.</p>
<p>Scott Woodward:   <br />
So there&#8217;s a few question marks in my mind in terms of confidence. Like, am I 100 percent confident that that really happened? Uh, no. Do I throw it out only because we have one account? No, not exactly.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:   <br />
So somewhere in that gray area, but I do think there&#8217;s one interesting precedent to this which corresponds in an interesting way chronologically. If this—he said it happened in Kirtland, and that would have been the time about when Joseph Smith had translated the Book of Abraham. And in Abraham Chapter 3, listen to this verse in light of that: verse 12, Abraham 3:12, “God said to me, Abraham, my son, my son, and his hand was stretched out. Behold, I will show you all these. And he put his hand upon mine eyes, and I saw those things which his hands had made, which were many.” And then he goes on, but, ooh, that&#8217;s interesting, right? God “put his hand upon mine eyes,” Abraham said, “and [then] I saw.” That is the pattern Joseph is saying here if this is what Joseph really said according to this account. Let me read it again. “God touched his eyes with his finger and then said, ‘Joseph, this is my Beloved Son. Hear Him.’ And as soon as the Lord had touched his eyes, that&#8217;s when he saw the Savior.” So I see a little overlap there. Again, maybe through the translation of the Book of Abraham, this sparked a detail that Joseph thought would be interesting for one audience to hear from his own First Vision which he had not told anybody else, right? If we&#8217;re leaning toward the believing side of this, assuming John Alger got the details right, perhaps it&#8217;s in that same time period of when Joseph had just translated that verse, which keyed the memory, which then evoked it in his telling of the story. And that&#8217;s the best I can do in terms of trying to puzzle this together.</p>
<p>Casey Paul Griffiths: <br />
Well, and I think, you know, speaking for the fidelity of the account—</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
—Charles Walker follows up with John Alger, said, I met him outside the church, because it sounds like Charles Walker was also sort of stunned by that detail. And he said, you know, I verified with the guy, did I mishear you when you said that God touched his eye? John Alger says, no, I remember Joseph Smith taking his finger and touching it to his right eye to emphasize that this actually happened. So it&#8217;s interesting that it doesn&#8217;t show up in any other account, but it&#8217;s a cool detail.</p>
<p>Scott Woodward:   <br />
Yeah, for sure.</p>
<p>Casey Paul Griffiths: <br />
I had a young lady in my class come up and say, “Hey, was this a vision or was it an appearance?” what she was getting at was were the Father and Son physically in the grove? And I just kind of considered the Wentworth Letter say, I was removed from my surroundings, which makes it sound like it was a vision, but this one really makes it sound like they were there physically and they interacted physically with Joseph, which I think is just kind of a neat thing.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
And she followed up and said, “Well, why is it called a vision, then?” I gave her my best shot, which was it was first published in a pamphlet called “An Interesting Account of Several Remarkable Visions.” I think that that word just stuck.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
But this is evidence that it was an appearance, that he wasn&#8217;t just seeing someplace far off, that it didn&#8217;t just happen in his mind, but that the Father and Son physically were in the grove, which I think adds significance when a person visits the grove. I mean, you were in the grove last week, weren&#8217;t you? And . . .</p>
<p>Scott Woodward:   <br />
I was in the grove last week. Yeah.</p>
<p>Casey Paul Griffiths: <br />
Yeah. You posted a video on social media, what the grove would have looked like in early spring—</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
—that I thought was fascinating.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
And that feeling of them actually being there, I think adds significance and weight.</p>
<p>Scott Woodward:   <br />
And to add to that, yeah, the accounts that talk about how he was surprised that the leaves weren&#8217;t consumed by the fire, right? That they touched the trees and nothing was consumed, I think also adds to the strength of the argument that it was actually happening in the grove, not just somehow in Joseph&#8217;s mind or seeing through some dimensional portal or whatever, however you want to depict a vision happening. And I just would be careful what assumptions we bring to the word vision. Like, if you&#8217;ve never had one, then, you know, you probably don&#8217;t want to weigh in as some kind of expert or somehow—you know what I mean? Or at least, at least not, you know, raise an eyebrow of suspicion. Why would we call it a vision if they—it&#8217;s like, well, what else are we going to call that? If that&#8217;s a phrase that Joseph felt comfortable with, as a person who&#8217;s never seen a vision, I&#8217;m just going to go ahead and trust Joseph on that one.</p>
<p>Casey Paul Griffiths: <br />
Yeah, and I want to go on record as saying I&#8217;m fine if it&#8217;s a vision or an appearance. I mean, there&#8217;s other events, like section 76, where it clearly is a vision. You know, there were other people in the room while they&#8217;re having the vision, and—</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
Philo Dibble said, I saw the glory and felt the power but did not see the vision, meaning this was clearly not a physical appearance of the Father and Son in section 76. They&#8217;re seeing a vision.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
But I think when you put all the accounts together, you can make the case to say this was an appearance.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
That they were physically there in the grove, though it doesn&#8217;t matter either way. I just think it&#8217;s one of those interesting things to deal with.</p>
<p>Scott Woodward:   <br />
I mean, that question came up last week. I was leading a church history tour, and another place where Joseph saw the Father and the Son was at the Isaac Morley farm and we were at the Isaac Morley farm, and so someone just had to ask, you know, they raised their hand like, ah, like, “Were they, like, here? Or did he just see them in a vision?” I was like, oh, that&#8217;s such a good question. I wish Joseph Smith was here. I wish he could weigh in on your question because I am not qualified to answer that. But anyway, it was just—that is an important question. I think it comes up. I just feel totally and completely unqualified to answer since that&#8217;s not a realm I&#8217;ve been in. It&#8217;s not the water I&#8217;ve swum in, so Joseph has to answer that one.</p>
<p>Casey Paul Griffiths: <br />
It does speak to the reality of the experience, right, though?</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
Sometimes people who view this through the hermeneutic of doubt would say, “Well, maybe he just hallucinated this whole thing.”</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
Charles Walker&#8217;s account makes it sound like, no, there was tangible, physical touch involved in the vision, which means it was an appearance. It was two people interacting physically and not something that just occurred in Joseph&#8217;s mind. Which, it&#8217;s kind of a big deal.</p>
<p>Scott Woodward:   <br />
Yeah. Wow.</p>
<p>Casey Paul Griffiths: <br />
There&#8217;s the accounts we chose. We could have chosen other ones. Like I mentioned, several people say, I heard Joseph Smith testify of the Father and the Son, but these are the ones that kind of have the meat there on their bones.</p>
<p>Scott Woodward:   <br />
Yeah, they tend to actually add something, right? They add some substantive details that are not in any other accounts.</p>
<p>Casey Paul Griffiths: <br />
That&#8217;s correct, yeah.</p>
<p>Scott Woodward:   <br />
Well chosen.</p>
<p>Casey Paul Griffiths: <br />
And one thing that makes me a little sad is, I mean, all those people who said, I heard him testify of the Father and Son are relating it without saying, I wrote down the details. I mean, we could have had dozens of more accounts like the ones we&#8217;ve considered today if people kept notes and wrote journals.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
It doesn&#8217;t seem like it was something that came up just on special occasions: that especially towards the end of his life, Joseph was very willing to talk about this experience, and it was important to him. So as a prophet of God that speaks to us, it&#8217;s important to us as well.</p>
<p>Scott Woodward:   <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
Well, and one interesting thing as we&#8217;ve considered the First Vision is that it&#8217;s interesting how it&#8217;s kind of shifted in importance. We mentioned in our first podcast that it wasn&#8217;t viewed as, like, the seminal event of the Restoration by the early saints. That was the coming forth of the Book of Mormon. That was something tangible, physical you could put into someone&#8217;s hands. And yet I think there&#8217;s a good reason why the First Vision has increased in importance.</p>
<p>Scott Woodward:   <br />
Oh, yeah.</p>
<p>Casey Paul Griffiths: <br />
It lays out this great pattern that anybody can follow to get answers to their prayers. It also just kind of plants a flag in the ground and says, hey, we&#8217;re not backing off on our truth claims. Look at the language President Hinckley uses. He says, “Two beings of substance were before him. He saw them. They were in form like men, only much more glorious in their appearance. He spoke to them. They spoke to him. They were not amorphous spirits. Each had a distinct personality. They were beings of flesh and bone whose nature was reaffirmed in later revelations which came to the prophet.” And then he makes some pretty black and white statements here. “Our entire case as members of the Church of Jesus Christ of Latter-day Saints rests on the validity of this glorious First Vision. Nothing on which we base our doctrine, nothing we teach, nothing we live by is of greater importance than this initial declaration. I submit that if Joseph Smith talked with God the Father and his Beloved Son, then all else of which he spoke is true. This is the hinge on which turns the gate that leads to the path of salvation and eternal life.” I mean, President Hinckley wasn&#8217;t a man known to make wild statements, right? He was a conservative individual. But in this particular case, and this is a 1998 talk called, “What Are People Asking About Us?” It was in general conference. He just kind of throws the gauntlet down, says, yeah, we&#8217;re not going to back off on this. This is how important it is to us. This is where the Restoration begins. And if this is true, we have to take seriously everything that comes after. So let&#8217;s wrap this up. Scott, what are your closing thoughts on the First Vision?</p>
<p>Scott Woodward:   <br />
Well, I was in the Sacred Grove last week. I almost had the Sacred Grove to myself, I felt like. We had a little tour there, and the Sacred Grove&#8217;s pretty big. 10, 15 acres I think is kept up by the church and there&#8217;s little trails that meander through the Sacred Grove, and you can just kind of go get lost in there and get lost in your thoughts. And, you know, we&#8217;ve been talking about this for several episodes now and thinking about it there. I had a quote from President Hinckley going through my mind. He said, “I recently visited Palmyra, New York.” He said, “Of the events that occurred in that area, one is led to conclude they either happened or they did not. There can be no gray area,” he said. “No middle ground.” And as I was walking through the grove, President Hinckley was in my mind. And I was thinking, Scott Woodward, do you really believe that Joseph Smith was telling the truth? What he said happened here either happened or it did not, and I am just happy to report that I am on the believing side of that equation. I have done everything in my power that I know how to do academically, spiritually, to verify. I&#8217;ve considered Joseph&#8217;s entire life of sincerity and devotion, the goodness, the depth, the richness of his theology, all the good fruit and beautiful effect that it&#8217;s had in my own life, the thousand little evidences that have built up to create my own testimony, and as I think about that, I believe he&#8217;s telling the truth. Something significant happened in that grove, because of which the world will never be the same. I know my world will never be the same. So, mark me down as a believer, Casey Griffiths. Mark me down as a believer. Thank you for listening to this episode of Church History Matters. Next week we wrap up this series by responding to your questions about the First Vision, and we will be honored to have with us Dr. Steven C. Harper, a church historian and scholar of the First Vision, to help us respond to your questions. So again, please send in your questions to info@scripturecentral.org by March 29th, 2023. Again, record yourself asking the question in about 20 seconds or so and provide a written transcription as well, and we will do our best to give you a solid response. Today&#8217;s episode was produced by Zander Sturgill and Scott Woodward, edited by Nick Galieti and Scott Woodward, with show notes and transcript by Gabe Davis. Church History Matters is a podcast of Scripture Central, a nonprofit which exists to help build enduring faith in Jesus Christ by making Latter-day Saint scripture and church history accessible, comprehensible, and defensible to people everywhere. For more resources to enhance your gospel study, go to scripturecentral.org, where everything is available for free because of the generous donations of people like you. Thank you so much for being a part of this with us.</p>
					</div>
						</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				</div>
		</div>
		                                            </div>
                            </div>
        </div>
		</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				<section class="has_eae_slider elementor-section elementor-inner-section elementor-element elementor-element-38f68b33 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="38f68b33" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-inner-column elementor-element elementor-element-768c3b0b" data-id="768c3b0b" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-28fb8978 elementor-widget elementor-widget-text-editor" data-id="28fb8978" data-element_type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
								<div class="elementor-text-editor elementor-clearfix">
					<p>Show produced by Zander Sturgill and Scott Woodward, edited by Nick Galieti and Scott Woodward, with show notes by Gabe Davis.</p>
<p>Church History Matters is a Podcast of Scripture Central. For more resources to enhance your gospel study go to ScriptureCentral.org where everything is available for free because of the generous donations of people like you.</p>
					</div>
						</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				</div>
		</div>
				<div data-elementor-type="footer" data-elementor-id="1373" class="elementor elementor-1373 elementor-location-footer" data-elementor-settings="[]">
		<div class="elementor-section-wrap">
					<footer class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-3def5fd0 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="3def5fd0" data-element_type="section" data-settings="{&quot;background_background&quot;:&quot;classic&quot;}">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-8164ae2" data-id="8164ae2" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-5d41ff4 elementor-widget elementor-widget-heading" data-id="5d41ff4" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h4 class="elementor-heading-title elementor-size-default">Our Vision</h4>		</div>
				</div>
				<div class="elementor-element elementor-element-644765aa elementor-widget elementor-widget-text-editor" data-id="644765aa" data-element_type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
								<div class="elementor-text-editor elementor-clearfix">
					<p>We build enduring faith in Jesus Christ by making the Doctrine and Covenants accessible, comprehensible, and defensible to people everywhere.</p>					</div>
						</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-44c5d2" data-id="44c5d2" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-6520707a elementor-widget elementor-widget-heading" data-id="6520707a" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h4 class="elementor-heading-title elementor-size-default">Navigation</h4>		</div>
				</div>
				<section class="has_eae_slider elementor-section elementor-inner-section elementor-element elementor-element-6b460ff9 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="6b460ff9" data-element_type="section">
						<div class="elementor-container elementor-column-gap-no">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-50 elementor-inner-column elementor-element elementor-element-5340fd7c" data-id="5340fd7c" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-68daa4f0 elementor-align-left elementor-icon-list--layout-traditional elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list" data-id="68daa4f0" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items">
							<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-caret-right"></i>						</span>
										<span class="elementor-icon-list-text">About</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-caret-right"></i>						</span>
										<span class="elementor-icon-list-text">Policies</span>
									</li>
								<li class="elementor-icon-list-item">
					<a href="/sitemap/">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-caret-right"></i>						</span>
										<span class="elementor-icon-list-text">Sitemap</span>
											</a>
									</li>
						</ul>
				</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-50 elementor-inner-column elementor-element elementor-element-1ae48387" data-id="1ae48387" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-234c24e6 elementor-align-left elementor-icon-list--layout-traditional elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list" data-id="234c24e6" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items">
							<li class="elementor-icon-list-item">
					<a href="https://bookofmormoncentral.org/content/donate">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-caret-right"></i>						</span>
										<span class="elementor-icon-list-text">Donate</span>
											</a>
									</li>
								<li class="elementor-icon-list-item">
					<a href="https://bookofmormoncentral.org/content/donor-frequently-asked-questions">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-caret-right"></i>						</span>
										<span class="elementor-icon-list-text">Donor FAQ</span>
											</a>
									</li>
						</ul>
				</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-4e2ce41 elementor-hidden-desktop elementor-hidden-tablet elementor-hidden-phone" data-id="4e2ce41" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
								</div>
					</div>
		</div>
								</div>
					</div>
		</footer>
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-5d7f3bf3 elementor-section-height-min-height elementor-section-content-middle elementor-section-boxed elementor-section-height-default elementor-section-items-middle" data-id="5d7f3bf3" data-element_type="section" data-settings="{&quot;background_background&quot;:&quot;classic&quot;}">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-df45028" data-id="df45028" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-26015b8b elementor-shape-square elementor-grid-0 e-grid-align-center elementor-widget elementor-widget-social-icons" data-id="26015b8b" data-element_type="widget" data-widget_type="social-icons.default">
				<div class="elementor-widget-container">
					<div class="elementor-social-icons-wrapper elementor-grid">
							<div class="elementor-grid-item">
					<a class="elementor-icon elementor-social-icon elementor-social-icon-facebook-f elementor-repeater-item-3d4d16f" href="https://www.facebook.com/bookofmormoncentral/" target="_blank">
						<span class="elementor-screen-only">Facebook-f</span>
						<i class="fab fa-facebook-f"></i>					</a>
				</div>
							<div class="elementor-grid-item">
					<a class="elementor-icon elementor-social-icon elementor-social-icon-twitter elementor-repeater-item-12db40b" href="https://twitter.com/bofmcentral" target="_blank">
						<span class="elementor-screen-only">Twitter</span>
						<i class="fab fa-twitter"></i>					</a>
				</div>
							<div class="elementor-grid-item">
					<a class="elementor-icon elementor-social-icon elementor-social-icon-youtube elementor-repeater-item-166d599" href="https://www.youtube.com/channel/UCqtKadDOHIbx_Zjq9BhxQYg" target="_blank">
						<span class="elementor-screen-only">Youtube</span>
						<i class="fab fa-youtube"></i>					</a>
				</div>
					</div>
				</div>
				</div>
				<div class="elementor-element elementor-element-e7ab805 elementor-widget elementor-widget-heading" data-id="e7ab805" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<p class="elementor-heading-title elementor-size-default">COPYRIGHT 2023 BOOK OF MORMON CENTRAL: A NON-PROFIT ORGANIZATION. ALL RIGHTS RESERVED. REGISTERED 501(C)(3). EIN: 20-5294264</p>		</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				</div>
		</div>

<link rel='stylesheet' id='elementor-post-31853-css'  href='https://doctrineandcovenantscentral.org/wp-content/uploads/elementor/css/post-31853.css?ver=1690840952' media='all' />
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/toolset-blocks/public/js/views-frontend.js?ver=3.4.2' id='views-blocks-frontend-js'></script>
<script id='eae-main-js-extra'>
var eae = {"ajaxurl":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-admin\\/admin-ajax.php","current_url":"aHR0cHM6Ly9kb2N0cmluZWFuZGNvdmVuYW50c2NlbnRyYWwub3JnL3BvZGNhc3QtZXBpc29kZS9ob3ctZG8tMm5kLWFuZC0zcmQtaGFuZC1hY2NvdW50cy1hZGQtdG8tb3VyLXVuZGVyc3RhbmRpbmctb2YtdGhlLWZpcnN0LXZpc2lvbiVlMiU4MCU4Yi8=","breakpoints":{"xs":0,"sm":480,"md":768,"lg":1025,"xl":1440,"xxl":1600}};
var eae_editor = {"plugin_url":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/plugins\\/addon-elements-for-elementor-page-builder\\/"};
</script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/js/eae.min.js?ver=1.0' id='eae-main-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/js/animated-main.min.js?ver=1.0' id='animated-main-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/js/particles.min.js?ver=1.0' id='eae-particles-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/lib/magnific.min.js?ver=1.9' id='wts-magnific-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/lib/vegas/vegas.min.js?ver=2.4.0' id='vegas-js'></script>
<script id='2f9091768-js-extra'>
var localize = {"ajaxurl":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-admin\\/admin-ajax.php","nonce":"75245142b0","i18n":{"added":"Added ","compare":"Compare","loading":"Loading..."}};
</script>
<script src='https://doctrineandcovenantscentral.org/wp-content/uploads/essential-addons-elementor/2f9091768.min.js?ver=1701117769' id='2f9091768-js'></script>
<script id='twentyseventeen-skip-link-focus-fix-js-extra'>
var twentyseventeenScreenReaderText = {"quote":"<svg class=\"icon icon-quote-right\" aria-hidden=\"true\" role=\"img\"> <use href=\"#icon-quote-right\" xlink:href=\"#icon-quote-right\"><\\/use> <\\/svg>","expand":"Expand child menu","collapse":"Collapse child menu","icon":"<svg class=\"icon icon-angle-down\" aria-hidden=\"true\" role=\"img\"> <use href=\"#icon-angle-down\" xlink:href=\"#icon-angle-down\"><\\/use> <span class=\"svg-fallback icon-angle-down\"><\\/span><\\/svg>"};
</script>
<script src='https://doctrineandcovenantscentral.org/wp-content/themes/twentyseventeen/assets/js/skip-link-focus-fix.js?ver=20161114' id='twentyseventeen-skip-link-focus-fix-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/themes/twentyseventeen/assets/js/navigation.js?ver=20161203' id='twentyseventeen-navigation-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/themes/twentyseventeen/assets/js/global.js?ver=20190121' id='twentyseventeen-global-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/themes/twentyseventeen/assets/js/jquery.scrollTo.js?ver=2.1.2' id='jquery-scrollto-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/3d-flipbook-dflip-lite/assets/js/dflip.min.js?ver=1.7.5.1' id='dflip-script-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-includes/js/wp-embed.min.js?ver=5.7.10' id='wp-embed-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor-pro/assets/lib/smartmenus/jquery.smartmenus.min.js?ver=1.0.1' id='smartmenus-js'></script>
<script id='bdt-uikit-js-extra'>
var element_pack_ajax_login_config = {"ajaxurl":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-admin\\/admin-ajax.php","loadingmessage":"Sending user info, please wait..."};
var ElementPackConfig = {"ajaxurl":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-admin\\/admin-ajax.php","nonce":"62bf16c738","contact_form":{"sending_msg":"Sending message please wait...","captcha_nd":"Invisible captcha not defined!","captcha_nr":"Could not get invisible captcha response!"},"elements_data":{"sections":[],"columns":[],"widgets":[]}};
</script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/bdthemes-element-pack-lite/assets/js/bdt-uikit.min.js?ver=2.9.2' id='bdt-uikit-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/js/webpack.runtime.min.js?ver=3.2.3' id='elementor-webpack-runtime-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/js/frontend-modules.min.js?ver=3.2.3' id='elementor-frontend-modules-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/waypoints/waypoints.min.js?ver=4.0.2' id='elementor-waypoints-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-includes/js/jquery/ui/core.min.js?ver=1.12.1' id='jquery-ui-core-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/swiper/swiper.min.js?ver=5.3.6' id='swiper-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/share-link/share-link.min.js?ver=3.2.3' id='share-link-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/dialog/dialog.min.js?ver=4.8.1' id='elementor-dialog-js'></script>
<script id='elementor-frontend-js-before'>
var elementorFrontendConfig = {"environmentMode":{"edit":false,"wpPreview":false,"isScriptDebug":false},"i18n":{"shareOnFacebook":"Share on Facebook","shareOnTwitter":"Share on Twitter","pinIt":"Pin it","download":"Download","downloadImage":"Download image","fullscreen":"Fullscreen","zoom":"Zoom","share":"Share","playVideo":"Play Video","previous":"Previous","next":"Next","close":"Close"},"is_rtl":false,"breakpoints":{"xs":0,"sm":480,"md":768,"lg":1025,"xl":1440,"xxl":1600},"responsive":{"breakpoints":{"mobile":{"label":"Mobile","value":767,"direction":"max","is_enabled":true},"mobile_extra":{"label":"Mobile Extra","value":880,"direction":"max","is_enabled":false},"tablet":{"label":"Tablet","value":1024,"direction":"max","is_enabled":true},"tablet_extra":{"label":"Tablet Extra","value":1365,"direction":"max","is_enabled":false},"laptop":{"label":"Laptop","value":1620,"direction":"max","is_enabled":false},"widescreen":{"label":"Widescreen","value":2400,"direction":"min","is_enabled":false}}},"version":"3.2.3","is_static":false,"experimentalFeatures":{"form-submissions":true},"urls":{"assets":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/plugins\\/elementor\\/assets\\/"},"settings":{"page":[],"editorPreferences":[]},"kit":{"active_breakpoints":["viewport_mobile","viewport_tablet"],"global_image_lightbox":"yes","lightbox_enable_counter":"yes","lightbox_enable_fullscreen":"yes","lightbox_enable_zoom":"yes","lightbox_enable_share":"yes","lightbox_title_src":"title","lightbox_description_src":"description"},"post":{"id":31913,"title":"First%20Vision%20Ep.%204%20%E2%80%93%20How%20Do%202nd%20and%203rd%20Hand%20Accounts%20Add%20to%20Our%20Understanding%20of%20the%20First%20Vision%3F%E2%80%8B%20%E2%80%93%20Doctrine%20and%20Covenants%20Central","excerpt":"","featuredImage":false}};
</script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/js/frontend.min.js?ver=3.2.3' id='elementor-frontend-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/bdthemes-element-pack-lite/assets/js/element-pack-site.min.js?ver=2.9.2' id='element-pack-site-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor-pro/assets/js/webpack-pro.runtime.min.js?ver=3.2.2' id='elementor-pro-webpack-runtime-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor-pro/assets/lib/sticky/jquery.sticky.min.js?ver=3.2.2' id='elementor-sticky-js'></script>
<script id='elementor-pro-frontend-js-before'>
var ElementorProFrontendConfig = {"ajaxurl":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-admin\\/admin-ajax.php","nonce":"f779c2c9aa","urls":{"assets":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/plugins\\/elementor-pro\\/assets\\/"},"i18n":{"toc_no_headings_found":"No headings were found on this page."},"shareButtonsNetworks":{"facebook":{"title":"Facebook","has_counter":true},"twitter":{"title":"Twitter"},"google":{"title":"Google+","has_counter":true},"linkedin":{"title":"LinkedIn","has_counter":true},"pinterest":{"title":"Pinterest","has_counter":true},"reddit":{"title":"Reddit","has_counter":true},"vk":{"title":"VK","has_counter":true},"odnoklassniki":{"title":"OK","has_counter":true},"tumblr":{"title":"Tumblr"},"digg":{"title":"Digg"},"skype":{"title":"Skype"},"stumbleupon":{"title":"StumbleUpon","has_counter":true},"mix":{"title":"Mix"},"telegram":{"title":"Telegram"},"pocket":{"title":"Pocket","has_counter":true},"xing":{"title":"XING","has_counter":true},"whatsapp":{"title":"WhatsApp"},"email":{"title":"Email"},"print":{"title":"Print"}},"facebook_sdk":{"lang":"en_US","app_id":""},"lottie":{"defaultAnimationUrl":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/plugins\\/elementor-pro\\/modules\\/lottie\\/assets\\/animations\\/default.json"}};
</script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor-pro/assets/js/frontend.min.js?ver=3.2.2' id='elementor-pro-frontend-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor-pro/assets/js/preloaded-elements-handlers.min.js?ver=3.2.2' id='pro-preloaded-elements-handlers-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/js/preloaded-modules.min.js?ver=3.2.3' id='preloaded-modules-js'></script>
<svg style="position: absolute; width: 0; height: 0; overflow: hidden;" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<defs>
<symbol id="icon-behance" viewBox="0 0 37 32">
<path class="path1" d="M33 6.054h-9.125v2.214h9.125v-2.214zM28.5 13.661q-1.607 0-2.607 0.938t-1.107 2.545h7.286q-0.321-3.482-3.571-3.482zM28.786 24.107q1.125 0 2.179-0.571t1.357-1.554h3.946q-1.786 5.482-7.625 5.482-3.821 0-6.080-2.357t-2.259-6.196q0-3.714 2.33-6.17t6.009-2.455q2.464 0 4.295 1.214t2.732 3.196 0.902 4.429q0 0.304-0.036 0.839h-11.75q0 1.982 1.027 3.063t2.973 1.080zM4.946 23.214h5.286q3.661 0 3.661-2.982 0-3.214-3.554-3.214h-5.393v6.196zM4.946 13.625h5.018q1.393 0 2.205-0.652t0.813-2.027q0-2.571-3.393-2.571h-4.643v5.25zM0 4.536h10.607q1.554 0 2.768 0.25t2.259 0.848 1.607 1.723 0.563 2.75q0 3.232-3.071 4.696 2.036 0.571 3.071 2.054t1.036 3.643q0 1.339-0.438 2.438t-1.179 1.848-1.759 1.268-2.161 0.75-2.393 0.232h-10.911v-22.5z"></path>
</symbol>
<symbol id="icon-deviantart" viewBox="0 0 18 32">
<path class="path1" d="M18.286 5.411l-5.411 10.393 0.429 0.554h4.982v7.411h-9.054l-0.786 0.536-2.536 4.875-0.536 0.536h-5.375v-5.411l5.411-10.411-0.429-0.536h-4.982v-7.411h9.054l0.786-0.536 2.536-4.875 0.536-0.536h5.375v5.411z"></path>
</symbol>
<symbol id="icon-medium" viewBox="0 0 32 32">
<path class="path1" d="M10.661 7.518v20.946q0 0.446-0.223 0.759t-0.652 0.313q-0.304 0-0.589-0.143l-8.304-4.161q-0.375-0.179-0.634-0.598t-0.259-0.83v-20.357q0-0.357 0.179-0.607t0.518-0.25q0.25 0 0.786 0.268l9.125 4.571q0.054 0.054 0.054 0.089zM11.804 9.321l9.536 15.464-9.536-4.75v-10.714zM32 9.643v18.821q0 0.446-0.25 0.723t-0.679 0.277-0.839-0.232l-7.875-3.929zM31.946 7.5q0 0.054-4.58 7.491t-5.366 8.705l-6.964-11.321 5.786-9.411q0.304-0.5 0.929-0.5 0.25 0 0.464 0.107l9.661 4.821q0.071 0.036 0.071 0.107z"></path>
</symbol>
<symbol id="icon-slideshare" viewBox="0 0 32 32">
<path class="path1" d="M15.589 13.214q0 1.482-1.134 2.545t-2.723 1.063-2.723-1.063-1.134-2.545q0-1.5 1.134-2.554t2.723-1.054 2.723 1.054 1.134 2.554zM24.554 13.214q0 1.482-1.125 2.545t-2.732 1.063q-1.589 0-2.723-1.063t-1.134-2.545q0-1.5 1.134-2.554t2.723-1.054q1.607 0 2.732 1.054t1.125 2.554zM28.571 16.429v-11.911q0-1.554-0.571-2.205t-1.982-0.652h-19.857q-1.482 0-2.009 0.607t-0.527 2.25v12.018q0.768 0.411 1.58 0.714t1.446 0.5 1.446 0.33 1.268 0.196 1.25 0.071 1.045 0.009 1.009-0.036 0.795-0.036q1.214-0.018 1.696 0.482 0.107 0.107 0.179 0.161 0.464 0.446 1.089 0.911 0.125-1.625 2.107-1.554 0.089 0 0.652 0.027t0.768 0.036 0.813 0.018 0.946-0.018 0.973-0.080 1.089-0.152 1.107-0.241 1.196-0.348 1.205-0.482 1.286-0.616zM31.482 16.339q-2.161 2.661-6.643 4.5 1.5 5.089-0.411 8.304-1.179 2.018-3.268 2.643-1.857 0.571-3.25-0.268-1.536-0.911-1.464-2.929l-0.018-5.821v-0.018q-0.143-0.036-0.438-0.107t-0.42-0.089l-0.018 6.036q0.071 2.036-1.482 2.929-1.411 0.839-3.268 0.268-2.089-0.643-3.25-2.679-1.875-3.214-0.393-8.268-4.482-1.839-6.643-4.5-0.446-0.661-0.071-1.125t1.071 0.018q0.054 0.036 0.196 0.125t0.196 0.143v-12.393q0-1.286 0.839-2.196t2.036-0.911h22.446q1.196 0 2.036 0.911t0.839 2.196v12.393l0.375-0.268q0.696-0.482 1.071-0.018t-0.071 1.125z"></path>
</symbol>
<symbol id="icon-snapchat-ghost" viewBox="0 0 30 32">
<path class="path1" d="M15.143 2.286q2.393-0.018 4.295 1.223t2.92 3.438q0.482 1.036 0.482 3.196 0 0.839-0.161 3.411 0.25 0.125 0.5 0.125 0.321 0 0.911-0.241t0.911-0.241q0.518 0 1 0.321t0.482 0.821q0 0.571-0.563 0.964t-1.232 0.563-1.232 0.518-0.563 0.848q0 0.268 0.214 0.768 0.661 1.464 1.83 2.679t2.58 1.804q0.5 0.214 1.429 0.411 0.5 0.107 0.5 0.625 0 1.25-3.911 1.839-0.125 0.196-0.196 0.696t-0.25 0.83-0.589 0.33q-0.357 0-1.107-0.116t-1.143-0.116q-0.661 0-1.107 0.089-0.571 0.089-1.125 0.402t-1.036 0.679-1.036 0.723-1.357 0.598-1.768 0.241q-0.929 0-1.723-0.241t-1.339-0.598-1.027-0.723-1.036-0.679-1.107-0.402q-0.464-0.089-1.125-0.089-0.429 0-1.17 0.134t-1.045 0.134q-0.446 0-0.625-0.33t-0.25-0.848-0.196-0.714q-3.911-0.589-3.911-1.839 0-0.518 0.5-0.625 0.929-0.196 1.429-0.411 1.393-0.571 2.58-1.804t1.83-2.679q0.214-0.5 0.214-0.768 0-0.5-0.563-0.848t-1.241-0.527-1.241-0.563-0.563-0.938q0-0.482 0.464-0.813t0.982-0.33q0.268 0 0.857 0.232t0.946 0.232q0.321 0 0.571-0.125-0.161-2.536-0.161-3.393 0-2.179 0.482-3.214 1.143-2.446 3.071-3.536t4.714-1.125z"></path>
</symbol>
<symbol id="icon-yelp" viewBox="0 0 27 32">
<path class="path1" d="M13.804 23.554v2.268q-0.018 5.214-0.107 5.446-0.214 0.571-0.911 0.714-0.964 0.161-3.241-0.679t-2.902-1.589q-0.232-0.268-0.304-0.643-0.018-0.214 0.071-0.464 0.071-0.179 0.607-0.839t3.232-3.857q0.018 0 1.071-1.25 0.268-0.339 0.705-0.438t0.884 0.063q0.429 0.179 0.67 0.518t0.223 0.75zM11.143 19.071q-0.054 0.982-0.929 1.25l-2.143 0.696q-4.911 1.571-5.214 1.571-0.625-0.036-0.964-0.643-0.214-0.446-0.304-1.339-0.143-1.357 0.018-2.973t0.536-2.223 1-0.571q0.232 0 3.607 1.375 1.25 0.518 2.054 0.839l1.5 0.607q0.411 0.161 0.634 0.545t0.205 0.866zM25.893 24.375q-0.125 0.964-1.634 2.875t-2.42 2.268q-0.661 0.25-1.125-0.125-0.25-0.179-3.286-5.125l-0.839-1.375q-0.25-0.375-0.205-0.821t0.348-0.821q0.625-0.768 1.482-0.464 0.018 0.018 2.125 0.714 3.625 1.179 4.321 1.42t0.839 0.366q0.5 0.393 0.393 1.089zM13.893 13.089q0.089 1.821-0.964 2.179-1.036 0.304-2.036-1.268l-6.75-10.679q-0.143-0.625 0.339-1.107 0.732-0.768 3.705-1.598t4.009-0.563q0.714 0.179 0.875 0.804 0.054 0.321 0.393 5.455t0.429 6.777zM25.714 15.018q0.054 0.696-0.464 1.054-0.268 0.179-5.875 1.536-1.196 0.268-1.625 0.411l0.018-0.036q-0.411 0.107-0.821-0.071t-0.661-0.571q-0.536-0.839 0-1.554 0.018-0.018 1.339-1.821 2.232-3.054 2.679-3.643t0.607-0.696q0.5-0.339 1.161-0.036 0.857 0.411 2.196 2.384t1.446 2.991v0.054z"></path>
</symbol>
<symbol id="icon-vine" viewBox="0 0 27 32">
<path class="path1" d="M26.732 14.768v3.536q-1.804 0.411-3.536 0.411-1.161 2.429-2.955 4.839t-3.241 3.848-2.286 1.902q-1.429 0.804-2.893-0.054-0.5-0.304-1.080-0.777t-1.518-1.491-1.83-2.295-1.92-3.286-1.884-4.357-1.634-5.616-1.259-6.964h5.054q0.464 3.893 1.25 7.116t1.866 5.661 2.17 4.205 2.5 3.482q3.018-3.018 5.125-7.25-2.536-1.286-3.982-3.929t-1.446-5.946q0-3.429 1.857-5.616t5.071-2.188q3.179 0 4.875 1.884t1.696 5.313q0 2.839-1.036 5.107-0.125 0.018-0.348 0.054t-0.821 0.036-1.125-0.107-1.107-0.455-0.902-0.92q0.554-1.839 0.554-3.286 0-1.554-0.518-2.357t-1.411-0.804q-0.946 0-1.518 0.884t-0.571 2.509q0 3.321 1.875 5.241t4.768 1.92q1.107 0 2.161-0.25z"></path>
</symbol>
<symbol id="icon-vk" viewBox="0 0 35 32">
<path class="path1" d="M34.232 9.286q0.411 1.143-2.679 5.25-0.429 0.571-1.161 1.518-1.393 1.786-1.607 2.339-0.304 0.732 0.25 1.446 0.304 0.375 1.446 1.464h0.018l0.071 0.071q2.518 2.339 3.411 3.946 0.054 0.089 0.116 0.223t0.125 0.473-0.009 0.607-0.446 0.491-1.054 0.223l-4.571 0.071q-0.429 0.089-1-0.089t-0.929-0.393l-0.357-0.214q-0.536-0.375-1.25-1.143t-1.223-1.384-1.089-1.036-1.009-0.277q-0.054 0.018-0.143 0.063t-0.304 0.259-0.384 0.527-0.304 0.929-0.116 1.384q0 0.268-0.063 0.491t-0.134 0.33l-0.071 0.089q-0.321 0.339-0.946 0.393h-2.054q-1.268 0.071-2.607-0.295t-2.348-0.946-1.839-1.179-1.259-1.027l-0.446-0.429q-0.179-0.179-0.491-0.536t-1.277-1.625-1.893-2.696-2.188-3.768-2.33-4.857q-0.107-0.286-0.107-0.482t0.054-0.286l0.071-0.107q0.268-0.339 1.018-0.339l4.893-0.036q0.214 0.036 0.411 0.116t0.286 0.152l0.089 0.054q0.286 0.196 0.429 0.571 0.357 0.893 0.821 1.848t0.732 1.455l0.286 0.518q0.518 1.071 1 1.857t0.866 1.223 0.741 0.688 0.607 0.25 0.482-0.089q0.036-0.018 0.089-0.089t0.214-0.393 0.241-0.839 0.17-1.446 0-2.232q-0.036-0.714-0.161-1.304t-0.25-0.821l-0.107-0.214q-0.446-0.607-1.518-0.768-0.232-0.036 0.089-0.429 0.304-0.339 0.679-0.536 0.946-0.464 4.268-0.429 1.464 0.018 2.411 0.232 0.357 0.089 0.598 0.241t0.366 0.429 0.188 0.571 0.063 0.813-0.018 0.982-0.045 1.259-0.027 1.473q0 0.196-0.018 0.75t-0.009 0.857 0.063 0.723 0.205 0.696 0.402 0.438q0.143 0.036 0.304 0.071t0.464-0.196 0.679-0.616 0.929-1.196 1.214-1.92q1.071-1.857 1.911-4.018 0.071-0.179 0.179-0.313t0.196-0.188l0.071-0.054 0.089-0.045t0.232-0.054 0.357-0.009l5.143-0.036q0.696-0.089 1.143 0.045t0.554 0.295z"></path>
</symbol>
<symbol id="icon-search" viewBox="0 0 30 32">
<path class="path1" d="M20.571 14.857q0-3.304-2.348-5.652t-5.652-2.348-5.652 2.348-2.348 5.652 2.348 5.652 5.652 2.348 5.652-2.348 2.348-5.652zM29.714 29.714q0 0.929-0.679 1.607t-1.607 0.679q-0.964 0-1.607-0.679l-6.125-6.107q-3.196 2.214-7.125 2.214-2.554 0-4.884-0.991t-4.018-2.679-2.679-4.018-0.991-4.884 0.991-4.884 2.679-4.018 4.018-2.679 4.884-0.991 4.884 0.991 4.018 2.679 2.679 4.018 0.991 4.884q0 3.929-2.214 7.125l6.125 6.125q0.661 0.661 0.661 1.607z"></path>
</symbol>
<symbol id="icon-envelope-o" viewBox="0 0 32 32">
<path class="path1" d="M29.714 26.857v-13.714q-0.571 0.643-1.232 1.179-4.786 3.679-7.607 6.036-0.911 0.768-1.482 1.196t-1.545 0.866-1.83 0.438h-0.036q-0.857 0-1.83-0.438t-1.545-0.866-1.482-1.196q-2.821-2.357-7.607-6.036-0.661-0.536-1.232-1.179v13.714q0 0.232 0.17 0.402t0.402 0.17h26.286q0.232 0 0.402-0.17t0.17-0.402zM29.714 8.089v-0.438t-0.009-0.232-0.054-0.223-0.098-0.161-0.161-0.134-0.25-0.045h-26.286q-0.232 0-0.402 0.17t-0.17 0.402q0 3 2.625 5.071 3.446 2.714 7.161 5.661 0.107 0.089 0.625 0.527t0.821 0.67 0.795 0.563 0.902 0.491 0.768 0.161h0.036q0.357 0 0.768-0.161t0.902-0.491 0.795-0.563 0.821-0.67 0.625-0.527q3.714-2.946 7.161-5.661 0.964-0.768 1.795-2.063t0.83-2.348zM32 7.429v19.429q0 1.179-0.839 2.018t-2.018 0.839h-26.286q-1.179 0-2.018-0.839t-0.839-2.018v-19.429q0-1.179 0.839-2.018t2.018-0.839h26.286q1.179 0 2.018 0.839t0.839 2.018z"></path>
</symbol>
<symbol id="icon-close" viewBox="0 0 25 32">
<path class="path1" d="M23.179 23.607q0 0.714-0.5 1.214l-2.429 2.429q-0.5 0.5-1.214 0.5t-1.214-0.5l-5.25-5.25-5.25 5.25q-0.5 0.5-1.214 0.5t-1.214-0.5l-2.429-2.429q-0.5-0.5-0.5-1.214t0.5-1.214l5.25-5.25-5.25-5.25q-0.5-0.5-0.5-1.214t0.5-1.214l2.429-2.429q0.5-0.5 1.214-0.5t1.214 0.5l5.25 5.25 5.25-5.25q0.5-0.5 1.214-0.5t1.214 0.5l2.429 2.429q0.5 0.5 0.5 1.214t-0.5 1.214l-5.25 5.25 5.25 5.25q0.5 0.5 0.5 1.214z"></path>
</symbol>
<symbol id="icon-angle-down" viewBox="0 0 21 32">
<path class="path1" d="M19.196 13.143q0 0.232-0.179 0.411l-8.321 8.321q-0.179 0.179-0.411 0.179t-0.411-0.179l-8.321-8.321q-0.179-0.179-0.179-0.411t0.179-0.411l0.893-0.893q0.179-0.179 0.411-0.179t0.411 0.179l7.018 7.018 7.018-7.018q0.179-0.179 0.411-0.179t0.411 0.179l0.893 0.893q0.179 0.179 0.179 0.411z"></path>
</symbol>
<symbol id="icon-folder-open" viewBox="0 0 34 32">
<path class="path1" d="M33.554 17q0 0.554-0.554 1.179l-6 7.071q-0.768 0.911-2.152 1.545t-2.563 0.634h-19.429q-0.607 0-1.080-0.232t-0.473-0.768q0-0.554 0.554-1.179l6-7.071q0.768-0.911 2.152-1.545t2.563-0.634h19.429q0.607 0 1.080 0.232t0.473 0.768zM27.429 10.857v2.857h-14.857q-1.679 0-3.518 0.848t-2.929 2.134l-6.107 7.179q0-0.071-0.009-0.223t-0.009-0.223v-17.143q0-1.643 1.179-2.821t2.821-1.179h5.714q1.643 0 2.821 1.179t1.179 2.821v0.571h9.714q1.643 0 2.821 1.179t1.179 2.821z"></path>
</symbol>
<symbol id="icon-twitter" viewBox="0 0 30 32">
<path class="path1" d="M28.929 7.286q-1.196 1.75-2.893 2.982 0.018 0.25 0.018 0.75 0 2.321-0.679 4.634t-2.063 4.437-3.295 3.759-4.607 2.607-5.768 0.973q-4.839 0-8.857-2.589 0.625 0.071 1.393 0.071 4.018 0 7.161-2.464-1.875-0.036-3.357-1.152t-2.036-2.848q0.589 0.089 1.089 0.089 0.768 0 1.518-0.196-2-0.411-3.313-1.991t-1.313-3.67v-0.071q1.214 0.679 2.607 0.732-1.179-0.786-1.875-2.054t-0.696-2.75q0-1.571 0.786-2.911 2.161 2.661 5.259 4.259t6.634 1.777q-0.143-0.679-0.143-1.321 0-2.393 1.688-4.080t4.080-1.688q2.5 0 4.214 1.821 1.946-0.375 3.661-1.393-0.661 2.054-2.536 3.179 1.661-0.179 3.321-0.893z"></path>
</symbol>
<symbol id="icon-facebook" viewBox="0 0 19 32">
<path class="path1" d="M17.125 0.214v4.714h-2.804q-1.536 0-2.071 0.643t-0.536 1.929v3.375h5.232l-0.696 5.286h-4.536v13.554h-5.464v-13.554h-4.554v-5.286h4.554v-3.893q0-3.321 1.857-5.152t4.946-1.83q2.625 0 4.071 0.214z"></path>
</symbol>
<symbol id="icon-github" viewBox="0 0 27 32">
<path class="path1" d="M13.714 2.286q3.732 0 6.884 1.839t4.991 4.991 1.839 6.884q0 4.482-2.616 8.063t-6.759 4.955q-0.482 0.089-0.714-0.125t-0.232-0.536q0-0.054 0.009-1.366t0.009-2.402q0-1.732-0.929-2.536 1.018-0.107 1.83-0.321t1.679-0.696 1.446-1.188 0.946-1.875 0.366-2.688q0-2.125-1.411-3.679 0.661-1.625-0.143-3.643-0.5-0.161-1.446 0.196t-1.643 0.786l-0.679 0.429q-1.661-0.464-3.429-0.464t-3.429 0.464q-0.286-0.196-0.759-0.482t-1.491-0.688-1.518-0.241q-0.804 2.018-0.143 3.643-1.411 1.554-1.411 3.679 0 1.518 0.366 2.679t0.938 1.875 1.438 1.196 1.679 0.696 1.83 0.321q-0.696 0.643-0.875 1.839-0.375 0.179-0.804 0.268t-1.018 0.089-1.17-0.384-0.991-1.116q-0.339-0.571-0.866-0.929t-0.884-0.429l-0.357-0.054q-0.375 0-0.518 0.080t-0.089 0.205 0.161 0.25 0.232 0.214l0.125 0.089q0.393 0.179 0.777 0.679t0.563 0.911l0.179 0.411q0.232 0.679 0.786 1.098t1.196 0.536 1.241 0.125 0.991-0.063l0.411-0.071q0 0.679 0.009 1.58t0.009 0.973q0 0.321-0.232 0.536t-0.714 0.125q-4.143-1.375-6.759-4.955t-2.616-8.063q0-3.732 1.839-6.884t4.991-4.991 6.884-1.839zM5.196 21.982q0.054-0.125-0.125-0.214-0.179-0.054-0.232 0.036-0.054 0.125 0.125 0.214 0.161 0.107 0.232-0.036zM5.75 22.589q0.125-0.089-0.036-0.286-0.179-0.161-0.286-0.054-0.125 0.089 0.036 0.286 0.179 0.179 0.286 0.054zM6.286 23.393q0.161-0.125 0-0.339-0.143-0.232-0.304-0.107-0.161 0.089 0 0.321t0.304 0.125zM7.036 24.143q0.143-0.143-0.071-0.339-0.214-0.214-0.357-0.054-0.161 0.143 0.071 0.339 0.214 0.214 0.357 0.054zM8.054 24.589q0.054-0.196-0.232-0.286-0.268-0.071-0.339 0.125t0.232 0.268q0.268 0.107 0.339-0.107zM9.179 24.679q0-0.232-0.304-0.196-0.286 0-0.286 0.196 0 0.232 0.304 0.196 0.286 0 0.286-0.196zM10.214 24.5q-0.036-0.196-0.321-0.161-0.286 0.054-0.25 0.268t0.321 0.143 0.25-0.25z"></path>
</symbol>
<symbol id="icon-bars" viewBox="0 0 27 32">
<path class="path1" d="M27.429 24v2.286q0 0.464-0.339 0.804t-0.804 0.339h-25.143q-0.464 0-0.804-0.339t-0.339-0.804v-2.286q0-0.464 0.339-0.804t0.804-0.339h25.143q0.464 0 0.804 0.339t0.339 0.804zM27.429 14.857v2.286q0 0.464-0.339 0.804t-0.804 0.339h-25.143q-0.464 0-0.804-0.339t-0.339-0.804v-2.286q0-0.464 0.339-0.804t0.804-0.339h25.143q0.464 0 0.804 0.339t0.339 0.804zM27.429 5.714v2.286q0 0.464-0.339 0.804t-0.804 0.339h-25.143q-0.464 0-0.804-0.339t-0.339-0.804v-2.286q0-0.464 0.339-0.804t0.804-0.339h25.143q0.464 0 0.804 0.339t0.339 0.804z"></path>
</symbol>
<symbol id="icon-google-plus" viewBox="0 0 41 32">
<path class="path1" d="M25.661 16.304q0 3.714-1.554 6.616t-4.429 4.536-6.589 1.634q-2.661 0-5.089-1.036t-4.179-2.786-2.786-4.179-1.036-5.089 1.036-5.089 2.786-4.179 4.179-2.786 5.089-1.036q5.107 0 8.768 3.429l-3.554 3.411q-2.089-2.018-5.214-2.018-2.196 0-4.063 1.107t-2.955 3.009-1.089 4.152 1.089 4.152 2.955 3.009 4.063 1.107q1.482 0 2.723-0.411t2.045-1.027 1.402-1.402 0.875-1.482 0.384-1.321h-7.429v-4.5h12.357q0.214 1.125 0.214 2.179zM41.143 14.125v3.75h-3.732v3.732h-3.75v-3.732h-3.732v-3.75h3.732v-3.732h3.75v3.732h3.732z"></path>
</symbol>
<symbol id="icon-linkedin" viewBox="0 0 27 32">
<path class="path1" d="M6.232 11.161v17.696h-5.893v-17.696h5.893zM6.607 5.696q0.018 1.304-0.902 2.179t-2.42 0.875h-0.036q-1.464 0-2.357-0.875t-0.893-2.179q0-1.321 0.92-2.188t2.402-0.866 2.375 0.866 0.911 2.188zM27.429 18.714v10.143h-5.875v-9.464q0-1.875-0.723-2.938t-2.259-1.063q-1.125 0-1.884 0.616t-1.134 1.527q-0.196 0.536-0.196 1.446v9.875h-5.875q0.036-7.125 0.036-11.554t-0.018-5.286l-0.018-0.857h5.875v2.571h-0.036q0.357-0.571 0.732-1t1.009-0.929 1.554-0.777 2.045-0.277q3.054 0 4.911 2.027t1.857 5.938z"></path>
</symbol>
<symbol id="icon-quote-right" viewBox="0 0 30 32">
<path class="path1" d="M13.714 5.714v12.571q0 1.857-0.723 3.545t-1.955 2.92-2.92 1.955-3.545 0.723h-1.143q-0.464 0-0.804-0.339t-0.339-0.804v-2.286q0-0.464 0.339-0.804t0.804-0.339h1.143q1.893 0 3.232-1.339t1.339-3.232v-0.571q0-0.714-0.5-1.214t-1.214-0.5h-4q-1.429 0-2.429-1t-1-2.429v-6.857q0-1.429 1-2.429t2.429-1h6.857q1.429 0 2.429 1t1 2.429zM29.714 5.714v12.571q0 1.857-0.723 3.545t-1.955 2.92-2.92 1.955-3.545 0.723h-1.143q-0.464 0-0.804-0.339t-0.339-0.804v-2.286q0-0.464 0.339-0.804t0.804-0.339h1.143q1.893 0 3.232-1.339t1.339-3.232v-0.571q0-0.714-0.5-1.214t-1.214-0.5h-4q-1.429 0-2.429-1t-1-2.429v-6.857q0-1.429 1-2.429t2.429-1h6.857q1.429 0 2.429 1t1 2.429z"></path>
</symbol>
<symbol id="icon-mail-reply" viewBox="0 0 32 32">
<path class="path1" d="M32 20q0 2.964-2.268 8.054-0.054 0.125-0.188 0.429t-0.241 0.536-0.232 0.393q-0.214 0.304-0.5 0.304-0.268 0-0.42-0.179t-0.152-0.446q0-0.161 0.045-0.473t0.045-0.42q0.089-1.214 0.089-2.196 0-1.804-0.313-3.232t-0.866-2.473-1.429-1.804-1.884-1.241-2.375-0.759-2.75-0.384-3.134-0.107h-4v4.571q0 0.464-0.339 0.804t-0.804 0.339-0.804-0.339l-9.143-9.143q-0.339-0.339-0.339-0.804t0.339-0.804l9.143-9.143q0.339-0.339 0.804-0.339t0.804 0.339 0.339 0.804v4.571h4q12.732 0 15.625 7.196 0.946 2.393 0.946 5.946z"></path>
</symbol>
<symbol id="icon-youtube" viewBox="0 0 27 32">
<path class="path1" d="M17.339 22.214v3.768q0 1.196-0.696 1.196-0.411 0-0.804-0.393v-5.375q0.393-0.393 0.804-0.393 0.696 0 0.696 1.196zM23.375 22.232v0.821h-1.607v-0.821q0-1.214 0.804-1.214t0.804 1.214zM6.125 18.339h1.911v-1.679h-5.571v1.679h1.875v10.161h1.786v-10.161zM11.268 28.5h1.589v-8.821h-1.589v6.75q-0.536 0.75-1.018 0.75-0.321 0-0.375-0.375-0.018-0.054-0.018-0.625v-6.5h-1.589v6.982q0 0.875 0.143 1.304 0.214 0.661 1.036 0.661 0.857 0 1.821-1.089v0.964zM18.929 25.857v-3.518q0-1.304-0.161-1.768-0.304-1-1.268-1-0.893 0-1.661 0.964v-3.875h-1.589v11.839h1.589v-0.857q0.804 0.982 1.661 0.982 0.964 0 1.268-0.982 0.161-0.482 0.161-1.786zM24.964 25.679v-0.232h-1.625q0 0.911-0.036 1.089-0.125 0.643-0.714 0.643-0.821 0-0.821-1.232v-1.554h3.196v-1.839q0-1.411-0.482-2.071-0.696-0.911-1.893-0.911-1.214 0-1.911 0.911-0.5 0.661-0.5 2.071v3.089q0 1.411 0.518 2.071 0.696 0.911 1.929 0.911 1.286 0 1.929-0.946 0.321-0.482 0.375-0.964 0.036-0.161 0.036-1.036zM14.107 9.375v-3.75q0-1.232-0.768-1.232t-0.768 1.232v3.75q0 1.25 0.768 1.25t0.768-1.25zM26.946 22.786q0 4.179-0.464 6.25-0.25 1.054-1.036 1.768t-1.821 0.821q-3.286 0.375-9.911 0.375t-9.911-0.375q-1.036-0.107-1.83-0.821t-1.027-1.768q-0.464-2-0.464-6.25 0-4.179 0.464-6.25 0.25-1.054 1.036-1.768t1.839-0.839q3.268-0.357 9.893-0.357t9.911 0.357q1.036 0.125 1.83 0.839t1.027 1.768q0.464 2 0.464 6.25zM9.125 0h1.821l-2.161 7.125v4.839h-1.786v-4.839q-0.25-1.321-1.089-3.786-0.661-1.839-1.161-3.339h1.893l1.268 4.696zM15.732 5.946v3.125q0 1.446-0.5 2.107-0.661 0.911-1.893 0.911-1.196 0-1.875-0.911-0.5-0.679-0.5-2.107v-3.125q0-1.429 0.5-2.089 0.679-0.911 1.875-0.911 1.232 0 1.893 0.911 0.5 0.661 0.5 2.089zM21.714 3.054v8.911h-1.625v-0.982q-0.946 1.107-1.839 1.107-0.821 0-1.054-0.661-0.143-0.429-0.143-1.339v-7.036h1.625v6.554q0 0.589 0.018 0.625 0.054 0.393 0.375 0.393 0.482 0 1.018-0.768v-6.804h1.625z"></path>
</symbol>
<symbol id="icon-dropbox" viewBox="0 0 32 32">
<path class="path1" d="M7.179 12.625l8.821 5.446-6.107 5.089-8.75-5.696zM24.786 22.536v1.929l-8.75 5.232v0.018l-0.018-0.018-0.018 0.018v-0.018l-8.732-5.232v-1.929l2.625 1.714 6.107-5.071v-0.036l0.018 0.018 0.018-0.018v0.036l6.125 5.071zM9.893 2.107l6.107 5.089-8.821 5.429-6.036-4.821zM24.821 12.625l6.036 4.839-8.732 5.696-6.125-5.089zM22.125 2.107l8.732 5.696-6.036 4.821-8.821-5.429z"></path>
</symbol>
<symbol id="icon-instagram" viewBox="0 0 27 32">
<path class="path1" d="M18.286 16q0-1.893-1.339-3.232t-3.232-1.339-3.232 1.339-1.339 3.232 1.339 3.232 3.232 1.339 3.232-1.339 1.339-3.232zM20.75 16q0 2.929-2.054 4.982t-4.982 2.054-4.982-2.054-2.054-4.982 2.054-4.982 4.982-2.054 4.982 2.054 2.054 4.982zM22.679 8.679q0 0.679-0.482 1.161t-1.161 0.482-1.161-0.482-0.482-1.161 0.482-1.161 1.161-0.482 1.161 0.482 0.482 1.161zM13.714 4.75q-0.125 0-1.366-0.009t-1.884 0-1.723 0.054-1.839 0.179-1.277 0.33q-0.893 0.357-1.571 1.036t-1.036 1.571q-0.196 0.518-0.33 1.277t-0.179 1.839-0.054 1.723 0 1.884 0.009 1.366-0.009 1.366 0 1.884 0.054 1.723 0.179 1.839 0.33 1.277q0.357 0.893 1.036 1.571t1.571 1.036q0.518 0.196 1.277 0.33t1.839 0.179 1.723 0.054 1.884 0 1.366-0.009 1.366 0.009 1.884 0 1.723-0.054 1.839-0.179 1.277-0.33q0.893-0.357 1.571-1.036t1.036-1.571q0.196-0.518 0.33-1.277t0.179-1.839 0.054-1.723 0-1.884-0.009-1.366 0.009-1.366 0-1.884-0.054-1.723-0.179-1.839-0.33-1.277q-0.357-0.893-1.036-1.571t-1.571-1.036q-0.518-0.196-1.277-0.33t-1.839-0.179-1.723-0.054-1.884 0-1.366 0.009zM27.429 16q0 4.089-0.089 5.661-0.179 3.714-2.214 5.75t-5.75 2.214q-1.571 0.089-5.661 0.089t-5.661-0.089q-3.714-0.179-5.75-2.214t-2.214-5.75q-0.089-1.571-0.089-5.661t0.089-5.661q0.179-3.714 2.214-5.75t5.75-2.214q1.571-0.089 5.661-0.089t5.661 0.089q3.714 0.179 5.75 2.214t2.214 5.75q0.089 1.571 0.089 5.661z"></path>
</symbol>
<symbol id="icon-flickr" viewBox="0 0 27 32">
<path class="path1" d="M22.286 2.286q2.125 0 3.634 1.509t1.509 3.634v17.143q0 2.125-1.509 3.634t-3.634 1.509h-17.143q-2.125 0-3.634-1.509t-1.509-3.634v-17.143q0-2.125 1.509-3.634t3.634-1.509h17.143zM12.464 16q0-1.571-1.107-2.679t-2.679-1.107-2.679 1.107-1.107 2.679 1.107 2.679 2.679 1.107 2.679-1.107 1.107-2.679zM22.536 16q0-1.571-1.107-2.679t-2.679-1.107-2.679 1.107-1.107 2.679 1.107 2.679 2.679 1.107 2.679-1.107 1.107-2.679z"></path>
</symbol>
<symbol id="icon-tumblr" viewBox="0 0 19 32">
<path class="path1" d="M16.857 23.732l1.429 4.232q-0.411 0.625-1.982 1.179t-3.161 0.571q-1.857 0.036-3.402-0.464t-2.545-1.321-1.696-1.893-0.991-2.143-0.295-2.107v-9.714h-3v-3.839q1.286-0.464 2.304-1.241t1.625-1.607 1.036-1.821 0.607-1.768 0.268-1.58q0.018-0.089 0.080-0.152t0.134-0.063h4.357v7.571h5.946v4.5h-5.964v9.25q0 0.536 0.116 1t0.402 0.938 0.884 0.741 1.455 0.25q1.393-0.036 2.393-0.518z"></path>
</symbol>
<symbol id="icon-dockerhub" viewBox="0 0 24 28">
<path class="path1" d="M1.597 10.257h2.911v2.83H1.597v-2.83zm3.573 0h2.91v2.83H5.17v-2.83zm0-3.627h2.91v2.829H5.17V6.63zm3.57 3.627h2.912v2.83H8.74v-2.83zm0-3.627h2.912v2.829H8.74V6.63zm3.573 3.627h2.911v2.83h-2.911v-2.83zm0-3.627h2.911v2.829h-2.911V6.63zm3.572 3.627h2.911v2.83h-2.911v-2.83zM12.313 3h2.911v2.83h-2.911V3zm-6.65 14.173c-.449 0-.812.354-.812.788 0 .435.364.788.812.788.447 0 .811-.353.811-.788 0-.434-.363-.788-.811-.788"></path>
<path class="path2" d="M28.172 11.721c-.978-.549-2.278-.624-3.388-.306-.136-1.146-.91-2.149-1.83-2.869l-.366-.286-.307.345c-.618.692-.8 1.845-.718 2.73.063.651.273 1.312.685 1.834-.313.183-.668.328-.985.434-.646.212-1.347.33-2.028.33H.083l-.042.429c-.137 1.432.065 2.866.674 4.173l.262.519.03.048c1.8 2.973 4.963 4.225 8.41 4.225 6.672 0 12.174-2.896 14.702-9.015 1.689.085 3.417-.4 4.243-1.968l.211-.4-.401-.223zM5.664 19.458c-.85 0-1.542-.671-1.542-1.497 0-.825.691-1.498 1.541-1.498.849 0 1.54.672 1.54 1.497s-.69 1.498-1.539 1.498z"></path>
</symbol>
<symbol id="icon-dribbble" viewBox="0 0 27 32">
<path class="path1" d="M18.286 26.786q-0.75-4.304-2.5-8.893h-0.036l-0.036 0.018q-0.286 0.107-0.768 0.295t-1.804 0.875-2.446 1.464-2.339 2.045-1.839 2.643l-0.268-0.196q3.286 2.679 7.464 2.679 2.357 0 4.571-0.929zM14.982 15.946q-0.375-0.875-0.946-1.982-5.554 1.661-12.018 1.661-0.018 0.125-0.018 0.375 0 2.214 0.786 4.223t2.214 3.598q0.893-1.589 2.205-2.973t2.545-2.223 2.33-1.446 1.777-0.857l0.661-0.232q0.071-0.018 0.232-0.063t0.232-0.080zM13.071 12.161q-2.143-3.804-4.357-6.75-2.464 1.161-4.179 3.321t-2.286 4.857q5.393 0 10.821-1.429zM25.286 17.857q-3.75-1.071-7.304-0.518 1.554 4.268 2.286 8.375 1.982-1.339 3.304-3.384t1.714-4.473zM10.911 4.625q-0.018 0-0.036 0.018 0.018-0.018 0.036-0.018zM21.446 7.214q-3.304-2.929-7.732-2.929-1.357 0-2.768 0.339 2.339 3.036 4.393 6.821 1.232-0.464 2.321-1.080t1.723-1.098 1.17-1.018 0.67-0.723zM25.429 15.875q-0.054-4.143-2.661-7.321l-0.018 0.018q-0.161 0.214-0.339 0.438t-0.777 0.795-1.268 1.080-1.786 1.161-2.348 1.152q0.446 0.946 0.786 1.696 0.036 0.107 0.116 0.313t0.134 0.295q0.643-0.089 1.33-0.125t1.313-0.036 1.232 0.027 1.143 0.071 1.009 0.098 0.857 0.116 0.652 0.107 0.446 0.080zM27.429 16q0 3.732-1.839 6.884t-4.991 4.991-6.884 1.839-6.884-1.839-4.991-4.991-1.839-6.884 1.839-6.884 4.991-4.991 6.884-1.839 6.884 1.839 4.991 4.991 1.839 6.884z"></path>
</symbol>
<symbol id="icon-skype" viewBox="0 0 27 32">
<path class="path1" d="M20.946 18.982q0-0.893-0.348-1.634t-0.866-1.223-1.304-0.875-1.473-0.607-1.563-0.411l-1.857-0.429q-0.536-0.125-0.786-0.188t-0.625-0.205-0.536-0.286-0.295-0.375-0.134-0.536q0-1.375 2.571-1.375 0.768 0 1.375 0.214t0.964 0.509 0.679 0.598 0.714 0.518 0.857 0.214q0.839 0 1.348-0.571t0.509-1.375q0-0.982-1-1.777t-2.536-1.205-3.25-0.411q-1.214 0-2.357 0.277t-2.134 0.839-1.589 1.554-0.598 2.295q0 1.089 0.339 1.902t1 1.348 1.429 0.866 1.839 0.58l2.607 0.643q1.607 0.393 2 0.643 0.571 0.357 0.571 1.071 0 0.696-0.714 1.152t-1.875 0.455q-0.911 0-1.634-0.286t-1.161-0.688-0.813-0.804-0.821-0.688-0.964-0.286q-0.893 0-1.348 0.536t-0.455 1.339q0 1.643 2.179 2.813t5.196 1.17q1.304 0 2.5-0.33t2.188-0.955 1.58-1.67 0.589-2.348zM27.429 22.857q0 2.839-2.009 4.848t-4.848 2.009q-2.321 0-4.179-1.429-1.375 0.286-2.679 0.286-2.554 0-4.884-0.991t-4.018-2.679-2.679-4.018-0.991-4.884q0-1.304 0.286-2.679-1.429-1.857-1.429-4.179 0-2.839 2.009-4.848t4.848-2.009q2.321 0 4.179 1.429 1.375-0.286 2.679-0.286 2.554 0 4.884 0.991t4.018 2.679 2.679 4.018 0.991 4.884q0 1.304-0.286 2.679 1.429 1.857 1.429 4.179z"></path>
</symbol>
<symbol id="icon-foursquare" viewBox="0 0 23 32">
<path class="path1" d="M17.857 7.75l0.661-3.464q0.089-0.411-0.161-0.714t-0.625-0.304h-12.714q-0.411 0-0.688 0.304t-0.277 0.661v19.661q0 0.125 0.107 0.018l5.196-6.286q0.411-0.464 0.679-0.598t0.857-0.134h4.268q0.393 0 0.661-0.259t0.321-0.527q0.429-2.321 0.661-3.411 0.071-0.375-0.205-0.714t-0.652-0.339h-5.25q-0.518 0-0.857-0.339t-0.339-0.857v-0.75q0-0.518 0.339-0.848t0.857-0.33h6.179q0.321 0 0.625-0.241t0.357-0.527zM21.911 3.786q-0.268 1.304-0.955 4.759t-1.241 6.25-0.625 3.098q-0.107 0.393-0.161 0.58t-0.25 0.58-0.438 0.589-0.688 0.375-1.036 0.179h-4.839q-0.232 0-0.393 0.179-0.143 0.161-7.607 8.821-0.393 0.446-1.045 0.509t-0.866-0.098q-0.982-0.393-0.982-1.75v-25.179q0-0.982 0.679-1.83t2.143-0.848h15.857q1.696 0 2.268 0.946t0.179 2.839zM21.911 3.786l-2.821 14.107q0.071-0.304 0.625-3.098t1.241-6.25 0.955-4.759z"></path>
</symbol>
<symbol id="icon-wordpress" viewBox="0 0 32 32">
<path class="path1" d="M2.268 16q0-2.911 1.196-5.589l6.554 17.946q-3.5-1.696-5.625-5.018t-2.125-7.339zM25.268 15.304q0 0.339-0.045 0.688t-0.179 0.884-0.205 0.786-0.313 1.054-0.313 1.036l-1.357 4.571-4.964-14.75q0.821-0.054 1.571-0.143 0.339-0.036 0.464-0.33t-0.045-0.554-0.509-0.241l-3.661 0.179q-1.339-0.018-3.607-0.179-0.214-0.018-0.366 0.089t-0.205 0.268-0.027 0.33 0.161 0.295 0.348 0.143l1.429 0.143 2.143 5.857-3 9-5-14.857q0.821-0.054 1.571-0.143 0.339-0.036 0.464-0.33t-0.045-0.554-0.509-0.241l-3.661 0.179q-0.125 0-0.411-0.009t-0.464-0.009q1.875-2.857 4.902-4.527t6.563-1.67q2.625 0 5.009 0.946t4.259 2.661h-0.179q-0.982 0-1.643 0.723t-0.661 1.705q0 0.214 0.036 0.429t0.071 0.384 0.143 0.411 0.161 0.375 0.214 0.402 0.223 0.375 0.259 0.429 0.25 0.411q1.125 1.911 1.125 3.786zM16.232 17.196l4.232 11.554q0.018 0.107 0.089 0.196-2.25 0.786-4.554 0.786-2 0-3.875-0.571zM28.036 9.411q1.696 3.107 1.696 6.589 0 3.732-1.857 6.884t-4.982 4.973l4.196-12.107q1.054-3.018 1.054-4.929 0-0.75-0.107-1.411zM16 0q3.25 0 6.214 1.268t5.107 3.411 3.411 5.107 1.268 6.214-1.268 6.214-3.411 5.107-5.107 3.411-6.214 1.268-6.214-1.268-5.107-3.411-3.411-5.107-1.268-6.214 1.268-6.214 3.411-5.107 5.107-3.411 6.214-1.268zM16 31.268q3.089 0 5.92-1.214t4.875-3.259 3.259-4.875 1.214-5.92-1.214-5.92-3.259-4.875-4.875-3.259-5.92-1.214-5.92 1.214-4.875 3.259-3.259 4.875-1.214 5.92 1.214 5.92 3.259 4.875 4.875 3.259 5.92 1.214z"></path>
</symbol>
<symbol id="icon-stumbleupon" viewBox="0 0 34 32">
<path class="path1" d="M18.964 12.714v-2.107q0-0.75-0.536-1.286t-1.286-0.536-1.286 0.536-0.536 1.286v10.929q0 3.125-2.25 5.339t-5.411 2.214q-3.179 0-5.42-2.241t-2.241-5.42v-4.75h5.857v4.679q0 0.768 0.536 1.295t1.286 0.527 1.286-0.527 0.536-1.295v-11.071q0-3.054 2.259-5.214t5.384-2.161q3.143 0 5.393 2.179t2.25 5.25v2.429l-3.482 1.036zM28.429 16.679h5.857v4.75q0 3.179-2.241 5.42t-5.42 2.241q-3.161 0-5.411-2.223t-2.25-5.366v-4.786l2.339 1.089 3.482-1.036v4.821q0 0.75 0.536 1.277t1.286 0.527 1.286-0.527 0.536-1.277v-4.911z"></path>
</symbol>
<symbol id="icon-digg" viewBox="0 0 37 32">
<path class="path1" d="M5.857 5.036h3.643v17.554h-9.5v-12.446h5.857v-5.107zM5.857 19.661v-6.589h-2.196v6.589h2.196zM10.964 10.143v12.446h3.661v-12.446h-3.661zM10.964 5.036v3.643h3.661v-3.643h-3.661zM16.089 10.143h9.518v16.821h-9.518v-2.911h5.857v-1.464h-5.857v-12.446zM21.946 19.661v-6.589h-2.196v6.589h2.196zM27.071 10.143h9.5v16.821h-9.5v-2.911h5.839v-1.464h-5.839v-12.446zM32.911 19.661v-6.589h-2.196v6.589h2.196z"></path>
</symbol>
<symbol id="icon-spotify" viewBox="0 0 27 32">
<path class="path1" d="M20.125 21.607q0-0.571-0.536-0.911-3.446-2.054-7.982-2.054-2.375 0-5.125 0.607-0.75 0.161-0.75 0.929 0 0.357 0.241 0.616t0.634 0.259q0.089 0 0.661-0.143 2.357-0.482 4.339-0.482 4.036 0 7.089 1.839 0.339 0.196 0.589 0.196 0.339 0 0.589-0.241t0.25-0.616zM21.839 17.768q0-0.714-0.625-1.089-4.232-2.518-9.786-2.518-2.732 0-5.411 0.75-0.857 0.232-0.857 1.143 0 0.446 0.313 0.759t0.759 0.313q0.125 0 0.661-0.143 2.179-0.589 4.482-0.589 4.982 0 8.714 2.214 0.429 0.232 0.679 0.232 0.446 0 0.759-0.313t0.313-0.759zM23.768 13.339q0-0.839-0.714-1.25-2.25-1.304-5.232-1.973t-6.125-0.67q-3.643 0-6.5 0.839-0.411 0.125-0.688 0.455t-0.277 0.866q0 0.554 0.366 0.929t0.92 0.375q0.196 0 0.714-0.143 2.375-0.661 5.482-0.661 2.839 0 5.527 0.607t4.527 1.696q0.375 0.214 0.714 0.214 0.518 0 0.902-0.366t0.384-0.92zM27.429 16q0 3.732-1.839 6.884t-4.991 4.991-6.884 1.839-6.884-1.839-4.991-4.991-1.839-6.884 1.839-6.884 4.991-4.991 6.884-1.839 6.884 1.839 4.991 4.991 1.839 6.884z"></path>
</symbol>
<symbol id="icon-soundcloud" viewBox="0 0 41 32">
<path class="path1" d="M14 24.5l0.286-4.304-0.286-9.339q-0.018-0.179-0.134-0.304t-0.295-0.125q-0.161 0-0.286 0.125t-0.125 0.304l-0.25 9.339 0.25 4.304q0.018 0.179 0.134 0.295t0.277 0.116q0.393 0 0.429-0.411zM19.286 23.982l0.196-3.768-0.214-10.464q0-0.286-0.232-0.429-0.143-0.089-0.286-0.089t-0.286 0.089q-0.232 0.143-0.232 0.429l-0.018 0.107-0.179 10.339q0 0.018 0.196 4.214v0.018q0 0.179 0.107 0.304 0.161 0.196 0.411 0.196 0.196 0 0.357-0.161 0.161-0.125 0.161-0.357zM0.625 17.911l0.357 2.286-0.357 2.25q-0.036 0.161-0.161 0.161t-0.161-0.161l-0.304-2.25 0.304-2.286q0.036-0.161 0.161-0.161t0.161 0.161zM2.161 16.5l0.464 3.696-0.464 3.625q-0.036 0.161-0.179 0.161-0.161 0-0.161-0.179l-0.411-3.607 0.411-3.696q0-0.161 0.161-0.161 0.143 0 0.179 0.161zM3.804 15.821l0.446 4.375-0.446 4.232q0 0.196-0.196 0.196-0.179 0-0.214-0.196l-0.375-4.232 0.375-4.375q0.036-0.214 0.214-0.214 0.196 0 0.196 0.214zM5.482 15.696l0.411 4.5-0.411 4.357q-0.036 0.232-0.25 0.232-0.232 0-0.232-0.232l-0.375-4.357 0.375-4.5q0-0.232 0.232-0.232 0.214 0 0.25 0.232zM7.161 16.018l0.375 4.179-0.375 4.393q-0.036 0.286-0.286 0.286-0.107 0-0.188-0.080t-0.080-0.205l-0.357-4.393 0.357-4.179q0-0.107 0.080-0.188t0.188-0.080q0.25 0 0.286 0.268zM8.839 13.411l0.375 6.786-0.375 4.393q0 0.125-0.089 0.223t-0.214 0.098q-0.286 0-0.321-0.321l-0.321-4.393 0.321-6.786q0.036-0.321 0.321-0.321 0.125 0 0.214 0.098t0.089 0.223zM10.518 11.875l0.339 8.357-0.339 4.357q0 0.143-0.098 0.241t-0.241 0.098q-0.321 0-0.357-0.339l-0.286-4.357 0.286-8.357q0.036-0.339 0.357-0.339 0.143 0 0.241 0.098t0.098 0.241zM12.268 11.161l0.321 9.036-0.321 4.321q-0.036 0.375-0.393 0.375-0.339 0-0.375-0.375l-0.286-4.321 0.286-9.036q0-0.161 0.116-0.277t0.259-0.116q0.161 0 0.268 0.116t0.125 0.277zM19.268 24.411v0 0zM15.732 11.089l0.268 9.107-0.268 4.268q0 0.179-0.134 0.313t-0.313 0.134-0.304-0.125-0.143-0.321l-0.25-4.268 0.25-9.107q0-0.196 0.134-0.321t0.313-0.125 0.313 0.125 0.134 0.321zM17.5 11.429l0.25 8.786-0.25 4.214q0 0.196-0.143 0.339t-0.339 0.143-0.339-0.143-0.161-0.339l-0.214-4.214 0.214-8.786q0.018-0.214 0.161-0.357t0.339-0.143 0.33 0.143 0.152 0.357zM21.286 20.214l-0.25 4.125q0 0.232-0.161 0.393t-0.393 0.161-0.393-0.161-0.179-0.393l-0.107-2.036-0.107-2.089 0.214-11.357v-0.054q0.036-0.268 0.214-0.429 0.161-0.125 0.357-0.125 0.143 0 0.268 0.089 0.25 0.143 0.286 0.464zM41.143 19.875q0 2.089-1.482 3.563t-3.571 1.473h-14.036q-0.232-0.036-0.393-0.196t-0.161-0.393v-16.054q0-0.411 0.5-0.589 1.518-0.607 3.232-0.607 3.482 0 6.036 2.348t2.857 5.777q0.946-0.393 1.964-0.393 2.089 0 3.571 1.482t1.482 3.589z"></path>
</symbol>
<symbol id="icon-codepen" viewBox="0 0 32 32">
<path class="path1" d="M3.857 20.875l10.768 7.179v-6.411l-5.964-3.982zM2.75 18.304l3.446-2.304-3.446-2.304v4.607zM17.375 28.054l10.768-7.179-4.804-3.214-5.964 3.982v6.411zM16 19.25l4.857-3.25-4.857-3.25-4.857 3.25zM8.661 14.339l5.964-3.982v-6.411l-10.768 7.179zM25.804 16l3.446 2.304v-4.607zM23.339 14.339l4.804-3.214-10.768-7.179v6.411zM32 11.125v9.75q0 0.732-0.607 1.143l-14.625 9.75q-0.375 0.232-0.768 0.232t-0.768-0.232l-14.625-9.75q-0.607-0.411-0.607-1.143v-9.75q0-0.732 0.607-1.143l14.625-9.75q0.375-0.232 0.768-0.232t0.768 0.232l14.625 9.75q0.607 0.411 0.607 1.143z"></path>
</symbol>
<symbol id="icon-twitch" viewBox="0 0 32 32">
<path class="path1" d="M16 7.75v7.75h-2.589v-7.75h2.589zM23.107 7.75v7.75h-2.589v-7.75h2.589zM23.107 21.321l4.518-4.536v-14.196h-21.321v18.732h5.821v3.875l3.875-3.875h7.107zM30.214 0v18.089l-7.75 7.75h-5.821l-3.875 3.875h-3.875v-3.875h-7.107v-20.679l1.946-5.161h26.482z"></path>
</symbol>
<symbol id="icon-meanpath" viewBox="0 0 27 32">
<path class="path1" d="M23.411 15.036v2.036q0 0.429-0.241 0.679t-0.67 0.25h-3.607q-0.429 0-0.679-0.25t-0.25-0.679v-2.036q0-0.429 0.25-0.679t0.679-0.25h3.607q0.429 0 0.67 0.25t0.241 0.679zM14.661 19.143v-4.464q0-0.946-0.58-1.527t-1.527-0.58h-2.375q-1.214 0-1.714 0.929-0.5-0.929-1.714-0.929h-2.321q-0.946 0-1.527 0.58t-0.58 1.527v4.464q0 0.393 0.375 0.393h0.982q0.393 0 0.393-0.393v-4.107q0-0.429 0.241-0.679t0.688-0.25h1.679q0.429 0 0.679 0.25t0.25 0.679v4.107q0 0.393 0.375 0.393h0.964q0.393 0 0.393-0.393v-4.107q0-0.429 0.25-0.679t0.679-0.25h1.732q0.429 0 0.67 0.25t0.241 0.679v4.107q0 0.393 0.393 0.393h0.982q0.375 0 0.375-0.393zM25.179 17.429v-2.75q0-0.946-0.589-1.527t-1.536-0.58h-4.714q-0.946 0-1.536 0.58t-0.589 1.527v7.321q0 0.375 0.393 0.375h0.982q0.375 0 0.375-0.375v-3.214q0.554 0.75 1.679 0.75h3.411q0.946 0 1.536-0.58t0.589-1.527zM27.429 6.429v19.143q0 1.714-1.214 2.929t-2.929 1.214h-19.143q-1.714 0-2.929-1.214t-1.214-2.929v-19.143q0-1.714 1.214-2.929t2.929-1.214h19.143q1.714 0 2.929 1.214t1.214 2.929z"></path>
</symbol>
<symbol id="icon-pinterest-p" viewBox="0 0 23 32">
<path class="path1" d="M0 10.661q0-1.929 0.67-3.634t1.848-2.973 2.714-2.196 3.304-1.393 3.607-0.464q2.821 0 5.25 1.188t3.946 3.455 1.518 5.125q0 1.714-0.339 3.357t-1.071 3.161-1.786 2.67-2.589 1.839-3.375 0.688q-1.214 0-2.411-0.571t-1.714-1.571q-0.179 0.696-0.5 2.009t-0.42 1.696-0.366 1.268-0.464 1.268-0.571 1.116-0.821 1.384-1.107 1.545l-0.25 0.089-0.161-0.179q-0.268-2.804-0.268-3.357 0-1.643 0.384-3.688t1.188-5.134 0.929-3.625q-0.571-1.161-0.571-3.018 0-1.482 0.929-2.786t2.357-1.304q1.089 0 1.696 0.723t0.607 1.83q0 1.179-0.786 3.411t-0.786 3.339q0 1.125 0.804 1.866t1.946 0.741q0.982 0 1.821-0.446t1.402-1.214 1-1.696 0.679-1.973 0.357-1.982 0.116-1.777q0-3.089-1.955-4.813t-5.098-1.723q-3.571 0-5.964 2.313t-2.393 5.866q0 0.786 0.223 1.518t0.482 1.161 0.482 0.813 0.223 0.545q0 0.5-0.268 1.304t-0.661 0.804q-0.036 0-0.304-0.054-0.911-0.268-1.616-1t-1.089-1.688-0.58-1.929-0.196-1.902z"></path>
</symbol>
<symbol id="icon-periscope" viewBox="0 0 24 28">
<path class="path1" d="M12.285,1C6.696,1,2.277,5.643,2.277,11.243c0,5.851,7.77,14.578,10.007,14.578c1.959,0,9.729-8.728,9.729-14.578 C22.015,5.643,17.596,1,12.285,1z M12.317,16.551c-3.473,0-6.152-2.611-6.152-5.664c0-1.292,0.39-2.472,1.065-3.438 c0.206,1.084,1.18,1.906,2.352,1.906c1.322,0,2.393-1.043,2.393-2.333c0-0.832-0.447-1.561-1.119-1.975 c0.467-0.105,0.955-0.161,1.46-0.161c3.133,0,5.81,2.611,5.81,5.998C18.126,13.94,15.449,16.551,12.317,16.551z"></path>
</symbol>
<symbol id="icon-get-pocket" viewBox="0 0 31 32">
<path class="path1" d="M27.946 2.286q1.161 0 1.964 0.813t0.804 1.973v9.268q0 3.143-1.214 6t-3.259 4.911-4.893 3.259-5.973 1.205q-3.143 0-5.991-1.205t-4.902-3.259-3.268-4.911-1.214-6v-9.268q0-1.143 0.821-1.964t1.964-0.821h25.161zM15.375 21.286q0.839 0 1.464-0.589l7.214-6.929q0.661-0.625 0.661-1.518 0-0.875-0.616-1.491t-1.491-0.616q-0.839 0-1.464 0.589l-5.768 5.536-5.768-5.536q-0.625-0.589-1.446-0.589-0.875 0-1.491 0.616t-0.616 1.491q0 0.911 0.643 1.518l7.232 6.929q0.589 0.589 1.446 0.589z"></path>
</symbol>
<symbol id="icon-vimeo" viewBox="0 0 32 32">
<path class="path1" d="M30.518 9.25q-0.179 4.214-5.929 11.625-5.946 7.696-10.036 7.696-2.536 0-4.286-4.696-0.786-2.857-2.357-8.607-1.286-4.679-2.804-4.679-0.321 0-2.268 1.357l-1.375-1.75q0.429-0.375 1.929-1.723t2.321-2.063q2.786-2.464 4.304-2.607 1.696-0.161 2.732 0.991t1.446 3.634q0.786 5.125 1.179 6.661 0.982 4.446 2.143 4.446 0.911 0 2.75-2.875 1.804-2.875 1.946-4.393 0.232-2.482-1.946-2.482-1.018 0-2.161 0.464 2.143-7.018 8.196-6.821 4.482 0.143 4.214 5.821z"></path>
</symbol>
<symbol id="icon-reddit-alien" viewBox="0 0 32 32">
<path class="path1" d="M32 15.107q0 1.036-0.527 1.884t-1.42 1.295q0.214 0.821 0.214 1.714 0 2.768-1.902 5.125t-5.188 3.723-7.143 1.366-7.134-1.366-5.179-3.723-1.902-5.125q0-0.839 0.196-1.679-0.911-0.446-1.464-1.313t-0.554-1.902q0-1.464 1.036-2.509t2.518-1.045q1.518 0 2.589 1.125 3.893-2.714 9.196-2.893l2.071-9.304q0.054-0.232 0.268-0.375t0.464-0.089l6.589 1.446q0.321-0.661 0.964-1.063t1.411-0.402q1.107 0 1.893 0.777t0.786 1.884-0.786 1.893-1.893 0.786-1.884-0.777-0.777-1.884l-5.964-1.321-1.857 8.429q5.357 0.161 9.268 2.857 1.036-1.089 2.554-1.089 1.482 0 2.518 1.045t1.036 2.509zM7.464 18.661q0 1.107 0.777 1.893t1.884 0.786 1.893-0.786 0.786-1.893-0.786-1.884-1.893-0.777q-1.089 0-1.875 0.786t-0.786 1.875zM21.929 25q0.196-0.196 0.196-0.464t-0.196-0.464q-0.179-0.179-0.446-0.179t-0.464 0.179q-0.732 0.75-2.161 1.107t-2.857 0.357-2.857-0.357-2.161-1.107q-0.196-0.179-0.464-0.179t-0.446 0.179q-0.196 0.179-0.196 0.455t0.196 0.473q0.768 0.768 2.116 1.214t2.188 0.527 1.625 0.080 1.625-0.080 2.188-0.527 2.116-1.214zM21.875 21.339q1.107 0 1.884-0.786t0.777-1.893q0-1.089-0.786-1.875t-1.875-0.786q-1.107 0-1.893 0.777t-0.786 1.884 0.786 1.893 1.893 0.786z"></path>
</symbol>
<symbol id="icon-whatsapp" viewBox="0 0 32 32">
<path d="M15.968 2.003a14.03 13.978 0 0 0-14.03 13.978 14.03 13.978 0 0 0 2.132 7.391L1.938 29.96l6.745-2.052a14.03 13.978 0 0 0 7.285 2.052 14.03 13.978 0 0 0 14.03-13.978 14.03 13.978 0 0 0-14.03-13.978z" stroke-width=".2000562"/>
<path d="M10.454 8.236a2.57 3.401 51.533 0 0-1.475 3.184v.015c.01 2.04 4.045 10.076 10.017 12.688l.017-.013a2.57 3.401 51.533 0 0 3.454-.706 2.57 3.401 51.533 0 0 1.064-4.129 2.57 3.401 51.533 0 0-4.262.103 2.57 3.401 51.533 0 0-.505.473c-1.346-.639-2.952-1.463-4.168-2.98-.771-.962-1.257-2.732-1.549-4.206a2.57 3.401 51.533 0 0 .605-.403 2.57 3.401 51.533 0 0 1.064-4.129 2.57 3.401 51.533 0 0-4.262.103z" stroke-width=".372"/>
</symbol>
<symbol id="icon-telegram" viewBox="0 0 32 32">
<path d="M30.8,2.2L0.6,13.9c-0.8,0.3-0.7,1.3,0,1.6l7.4,2.8l2.9,9.2c0.2,0.6,0.9,0.8,1.4,0.4l4.1-3.4 c0.4-0.4,1-0.4,1.5,0l7.4,5.4c0.5,0.4,1.2,0.1,1.4-0.5L32,3.2C32.1,2.5,31.4,1.9,30.8,2.2z M25,8.3l-11.9,11 c-0.4,0.4-0.7,0.9-0.8,1.5l-0.4,3c-0.1,0.4-0.6,0.4-0.7,0.1l-1.6-5.5c-0.2-0.6,0.1-1.3,0.6-1.6l14.4-8.9C25,7.7,25.3,8.1,25,8.3z"/>
</symbol>
<symbol id="icon-hashtag" viewBox="0 0 32 32">
<path class="path1" d="M17.696 18.286l1.143-4.571h-4.536l-1.143 4.571h4.536zM31.411 9.286l-1 4q-0.125 0.429-0.554 0.429h-5.839l-1.143 4.571h5.554q0.268 0 0.446 0.214 0.179 0.25 0.107 0.5l-1 4q-0.089 0.429-0.554 0.429h-5.839l-1.446 5.857q-0.125 0.429-0.554 0.429h-4q-0.286 0-0.464-0.214-0.161-0.214-0.107-0.5l1.393-5.571h-4.536l-1.446 5.857q-0.125 0.429-0.554 0.429h-4.018q-0.268 0-0.446-0.214-0.161-0.214-0.107-0.5l1.393-5.571h-5.554q-0.268 0-0.446-0.214-0.161-0.214-0.107-0.5l1-4q0.125-0.429 0.554-0.429h5.839l1.143-4.571h-5.554q-0.268 0-0.446-0.214-0.179-0.25-0.107-0.5l1-4q0.089-0.429 0.554-0.429h5.839l1.446-5.857q0.125-0.429 0.571-0.429h4q0.268 0 0.446 0.214 0.161 0.214 0.107 0.5l-1.393 5.571h4.536l1.446-5.857q0.125-0.429 0.571-0.429h4q0.268 0 0.446 0.214 0.161 0.214 0.107 0.5l-1.393 5.571h5.554q0.268 0 0.446 0.214 0.161 0.214 0.107 0.5z"></path>
</symbol>
<symbol id="icon-chain" viewBox="0 0 30 32">
<path class="path1" d="M26 21.714q0-0.714-0.5-1.214l-3.714-3.714q-0.5-0.5-1.214-0.5-0.75 0-1.286 0.571 0.054 0.054 0.339 0.33t0.384 0.384 0.268 0.339 0.232 0.455 0.063 0.491q0 0.714-0.5 1.214t-1.214 0.5q-0.268 0-0.491-0.063t-0.455-0.232-0.339-0.268-0.384-0.384-0.33-0.339q-0.589 0.554-0.589 1.304 0 0.714 0.5 1.214l3.679 3.696q0.482 0.482 1.214 0.482 0.714 0 1.214-0.464l2.625-2.607q0.5-0.5 0.5-1.196zM13.446 9.125q0-0.714-0.5-1.214l-3.679-3.696q-0.5-0.5-1.214-0.5-0.696 0-1.214 0.482l-2.625 2.607q-0.5 0.5-0.5 1.196 0 0.714 0.5 1.214l3.714 3.714q0.482 0.482 1.214 0.482 0.75 0 1.286-0.554-0.054-0.054-0.339-0.33t-0.384-0.384-0.268-0.339-0.232-0.455-0.063-0.491q0-0.714 0.5-1.214t1.214-0.5q0.268 0 0.491 0.063t0.455 0.232 0.339 0.268 0.384 0.384 0.33 0.339q0.589-0.554 0.589-1.304zM29.429 21.714q0 2.143-1.518 3.625l-2.625 2.607q-1.482 1.482-3.625 1.482-2.161 0-3.643-1.518l-3.679-3.696q-1.482-1.482-1.482-3.625 0-2.196 1.571-3.732l-1.571-1.571q-1.536 1.571-3.714 1.571-2.143 0-3.643-1.5l-3.714-3.714q-1.5-1.5-1.5-3.643t1.518-3.625l2.625-2.607q1.482-1.482 3.625-1.482 2.161 0 3.643 1.518l3.679 3.696q1.482 1.482 1.482 3.625 0 2.196-1.571 3.732l1.571 1.571q1.536-1.571 3.714-1.571 2.143 0 3.643 1.5l3.714 3.714q1.5 1.5 1.5 3.643z"></path>
</symbol>
<symbol id="icon-thumb-tack" viewBox="0 0 21 32">
<path class="path1" d="M8.571 15.429v-8q0-0.25-0.161-0.411t-0.411-0.161-0.411 0.161-0.161 0.411v8q0 0.25 0.161 0.411t0.411 0.161 0.411-0.161 0.161-0.411zM20.571 21.714q0 0.464-0.339 0.804t-0.804 0.339h-7.661l-0.911 8.625q-0.036 0.214-0.188 0.366t-0.366 0.152h-0.018q-0.482 0-0.571-0.482l-1.357-8.661h-7.214q-0.464 0-0.804-0.339t-0.339-0.804q0-2.196 1.402-3.955t3.17-1.759v-9.143q-0.929 0-1.607-0.679t-0.679-1.607 0.679-1.607 1.607-0.679h11.429q0.929 0 1.607 0.679t0.679 1.607-0.679 1.607-1.607 0.679v9.143q1.768 0 3.17 1.759t1.402 3.955z"></path>
</symbol>
<symbol id="icon-arrow-left" viewBox="0 0 43 32">
<path class="path1" d="M42.311 14.044c-0.178-0.178-0.533-0.356-0.711-0.356h-33.778l10.311-10.489c0.178-0.178 0.356-0.533 0.356-0.711 0-0.356-0.178-0.533-0.356-0.711l-1.6-1.422c-0.356-0.178-0.533-0.356-0.889-0.356s-0.533 0.178-0.711 0.356l-14.578 14.933c-0.178 0.178-0.356 0.533-0.356 0.711s0.178 0.533 0.356 0.711l14.756 14.933c0 0.178 0.356 0.356 0.533 0.356s0.533-0.178 0.711-0.356l1.6-1.6c0.178-0.178 0.356-0.533 0.356-0.711s-0.178-0.533-0.356-0.711l-10.311-10.489h33.778c0.178 0 0.533-0.178 0.711-0.356 0.356-0.178 0.533-0.356 0.533-0.711v-2.133c0-0.356-0.178-0.711-0.356-0.889z"></path>
</symbol>
<symbol id="icon-arrow-right" viewBox="0 0 43 32">
<path class="path1" d="M0.356 17.956c0.178 0.178 0.533 0.356 0.711 0.356h33.778l-10.311 10.489c-0.178 0.178-0.356 0.533-0.356 0.711 0 0.356 0.178 0.533 0.356 0.711l1.6 1.6c0.178 0.178 0.533 0.356 0.711 0.356s0.533-0.178 0.711-0.356l14.756-14.933c0.178-0.356 0.356-0.711 0.356-0.889s-0.178-0.533-0.356-0.711l-14.756-14.933c0-0.178-0.356-0.356-0.533-0.356s-0.533 0.178-0.711 0.356l-1.6 1.6c-0.178 0.178-0.356 0.533-0.356 0.711s0.178 0.533 0.356 0.711l10.311 10.489h-33.778c-0.178 0-0.533 0.178-0.711 0.356-0.356 0.178-0.533 0.356-0.533 0.711v2.311c0 0.178 0.178 0.533 0.356 0.711z"></path>
</symbol>
<symbol id="icon-play" viewBox="0 0 22 28">
<path d="M21.625 14.484l-20.75 11.531c-0.484 0.266-0.875 0.031-0.875-0.516v-23c0-0.547 0.391-0.781 0.875-0.516l20.75 11.531c0.484 0.266 0.484 0.703 0 0.969z"></path>
</symbol>
<symbol id="icon-pause" viewBox="0 0 24 28">
<path d="M24 3v22c0 0.547-0.453 1-1 1h-8c-0.547 0-1-0.453-1-1v-22c0-0.547 0.453-1 1-1h8c0.547 0 1 0.453 1 1zM10 3v22c0 0.547-0.453 1-1 1h-8c-0.547 0-1-0.453-1-1v-22c0-0.547 0.453-1 1-1h8c0.547 0 1 0.453 1 1z"></path>
</symbol>
</defs>
</svg>

</body>
</html>

"""


def test_load_dc_podcasts_extra() -> None:
    """It returns a valid Document for a D&C podcast."""
    url = "https://doctrineandcovenantscentral.org/podcast-episode/how-do-2nd-and-3rd-hand-accounts-add-to-our-understanding-of-the-first-vision%e2%80%8b/"
    result = load_dc_podcasts(url, html)
    assert len(result.page_content) > 0
    assert result.metadata["url"] == url
    assert result.metadata["title"] == "How Do 2nd and 3rd Hand Accounts Add to Our Understanding of the First Vision?"
    assert result.page_content.startswith("Scott Woodward:\n\nHi. This is Scott from Church History Matters")
