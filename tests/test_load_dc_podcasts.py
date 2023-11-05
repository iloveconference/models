"""Test cases for the load_know module."""
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
	<title>First Vision Ep. 1 - Why Are There Different Accounts of the First Vision?​ | Doctrine and Covenants Central</title>
	<link rel="canonical" href="https://doctrineandcovenantscentral.org/podcast-episode/why-are-there-different-accounts-of-the-first-vision​/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="First Vision Ep. 1 - Why Are There Different Accounts of the First Vision?​ | Doctrine and Covenants Central" />
	<meta property="og:url" content="https://doctrineandcovenantscentral.org/podcast-episode/why-are-there-different-accounts-of-the-first-vision​/" />
	<meta property="og:site_name" content="Doctrine and Covenants Central" />
	<meta property="article:modified_time" content="2023-10-30T06:08:29+00:00" />
	<meta name="twitter:card" content="summary_large_image" />
	<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://doctrineandcovenantscentral.org/#organization","name":"Doctrine and Covenants Central","url":"https://doctrineandcovenantscentral.org/","sameAs":["https://www.youtube.com/channel/UCqtKadDOHIbx_Zjq9BhxQYg"],"logo":{"@type":"ImageObject","@id":"https://doctrineandcovenantscentral.org/#logo","inLanguage":"en-US","url":"https://doctrineandcovenantscentral.org/wp-content/uploads/2020/12/DC-1.png","width":3300,"height":1752,"caption":"Doctrine and Covenants Central"},"image":{"@id":"https://doctrineandcovenantscentral.org/#logo"}},{"@type":"WebSite","@id":"https://doctrineandcovenantscentral.org/#website","url":"https://doctrineandcovenantscentral.org/","name":"Doctrine and Covenants Central","description":"","publisher":{"@id":"https://doctrineandcovenantscentral.org/#organization"},"potentialAction":[{"@type":"SearchAction","target":"https://doctrineandcovenantscentral.org/?s={search_term_string}","query-input":"required name=search_term_string"}],"inLanguage":"en-US"},{"@type":"WebPage","@id":"https://doctrineandcovenantscentral.org/podcast-episode/why-are-there-different-accounts-of-the-first-vision%e2%80%8b/#webpage","url":"https://doctrineandcovenantscentral.org/podcast-episode/why-are-there-different-accounts-of-the-first-vision%e2%80%8b/","name":"First Vision Ep. 1 - Why Are There Different Accounts of the First Vision?\u200b | Doctrine and Covenants Central","isPartOf":{"@id":"https://doctrineandcovenantscentral.org/#website"},"datePublished":"2023-07-31T22:11:24+00:00","dateModified":"2023-10-30T06:08:29+00:00","breadcrumb":{"@id":"https://doctrineandcovenantscentral.org/podcast-episode/why-are-there-different-accounts-of-the-first-vision%e2%80%8b/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https://doctrineandcovenantscentral.org/podcast-episode/why-are-there-different-accounts-of-the-first-vision%e2%80%8b/"]}]},{"@type":"BreadcrumbList","@id":"https://doctrineandcovenantscentral.org/podcast-episode/why-are-there-different-accounts-of-the-first-vision%e2%80%8b/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"item":{"@type":"WebPage","@id":"https://doctrineandcovenantscentral.org/","url":"https://doctrineandcovenantscentral.org/","name":"Home"}},{"@type":"ListItem","position":2,"item":{"@type":"WebPage","@id":"https://doctrineandcovenantscentral.org/podcast-episode/","url":"https://doctrineandcovenantscentral.org/podcast-episode/","name":"Podcast Episodes"}},{"@type":"ListItem","position":3,"item":{"@type":"WebPage","@id":"https://doctrineandcovenantscentral.org/podcast-episode/why-are-there-different-accounts-of-the-first-vision%e2%80%8b/","url":"https://doctrineandcovenantscentral.org/podcast-episode/why-are-there-different-accounts-of-the-first-vision%e2%80%8b/","name":"First Vision Ep. 1 &#8211; Why Are There Different Accounts of the First Vision?\u200b"}}]}]}</script>
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
<link rel='stylesheet' id='670754473-css'  href='https://doctrineandcovenantscentral.org/wp-content/uploads/essential-addons-elementor/670754473.min.css?ver=1699164202' media='all' />
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
<link rel="https://api.w.org/" href="https://doctrineandcovenantscentral.org/wp-json/" /><link rel="alternate" type="application/json" href="https://doctrineandcovenantscentral.org/wp-json/wp/v2/podcast-episode/31910" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://doctrineandcovenantscentral.org/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://doctrineandcovenantscentral.org/wp-includes/wlwmanifest.xml" />
<meta name="generator" content="WordPress 5.7.10" />
<link rel='shortlink' href='https://doctrineandcovenantscentral.org/?p=31910' />
<link rel="alternate" type="application/json+oembed" href="https://doctrineandcovenantscentral.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fdoctrineandcovenantscentral.org%2Fpodcast-episode%2Fwhy-are-there-different-accounts-of-the-first-vision%25e2%2580%258b%2F" />
<link rel="alternate" type="text/xml+oembed" href="https://doctrineandcovenantscentral.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fdoctrineandcovenantscentral.org%2Fpodcast-episode%2Fwhy-are-there-different-accounts-of-the-first-vision%25e2%2580%258b%2F&#038;format=xml" />
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
<body class="podcast-episode-template-default single single-podcast-episode postid-31910 wp-custom-logo wp-embed-responsive has-sidebar title-tagline-hidden colors-light elementor-default elementor-template-full-width elementor-kit-10 elementor-page-31897">
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
				<div data-elementor-type="single-post" data-elementor-id="31897" class="elementor elementor-31897 elementor-location-single post-31910 podcast-episode type-podcast-episode status-publish hentry category-first-vision" data-elementor-settings="[]">
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
												<img width="228" height="227" src="https://doctrineandcovenantscentral.org/wp-content/uploads/2023/07/First-Vision-Pic.png" class="attachment-large size-large" alt="" loading="lazy" srcset="https://doctrineandcovenantscentral.org/wp-content/uploads/2023/07/First-Vision-Pic.png 228w, https://doctrineandcovenantscentral.org/wp-content/uploads/2023/07/First-Vision-Pic-150x150.png 150w, https://doctrineandcovenantscentral.org/wp-content/uploads/2023/07/First-Vision-Pic-100x100.png 100w" sizes="100vw" />														</div>
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
			<h2 class="elementor-heading-title elementor-size-default"> Episode 1</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-524f0398 elementor-widget elementor-widget-heading" data-id="524f0398" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Why Are There Different Accounts of the First Vision?​</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-7e3e7a59 elementor-widget elementor-widget-heading" data-id="7e3e7a59" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">53 min</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-37fcf4e2 elementor-widget elementor-widget-text-editor" data-id="37fcf4e2" data-element_type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
								<div class="elementor-text-editor elementor-clearfix">
					<p>Joseph Smith’s First Vision is foundational to our narrative of the Restoration today, but it was not always so from the Church’s beginning. So how did the First Vision go from what began as a very personal experience of Joseph’s, to growing in institutional significance for the whole Church as it has today? Also, given that there are unique differences in Joseph Smith&#8217;s 4 separate accounts of his First Vision, what role does our personal &#8220;hermeneutic&#8221; play in how we make sense of these? And what might a letter Joseph wrote from Indiana to his wife Emma tell us about the context of his 1832 account of his vision?</p>
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
					<div class="elementor-shortcode"><iframe height="150" width="100%" style="border: none;height:150px" scrolling="no" src="https://www.podbean.com/player-v2/?from=embed&amp;i=v5a67-13ae8f3-pb&amp;share=1&amp;download=1&amp;fonts=Arial&amp;skin=1&amp;font-color=&amp;rtl=0&amp;logo_link=&amp;btn-skin=8bbb4e&amp;size=150"></iframe></div>
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
<li>Joseph Smith&#8217;s four accounts of his First Vision were written or dictated under four very unique and distinct circumstances which influence how he recounted his vision and what details he provided or omitted as he did so. When viewed through the &#8220;hermeneutic of trust,&#8221; the differences in these accounts nuance and enhance rather than cast suspicion upon the reality of Joseph&#8217;s vision.</li>
<li>Joseph&#8217;s 1832 account was rediscovered and made publicly available in the 2nd half of the 20th century. It is unclear why he wrote it and who his intended audience may have been, but Matthew Godfrey&#8217;s 2018 article offers a solid hypothesis which Casey and Scott weigh in on.</li>
<li>His 1832 account is the most intimate of Joseph&#8217;s four recitals of his First Vision. It discloses his inner world far more than the other accounts, and it also contains more words from the Savior than any other account.</li>
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
<p class="p1">Harper, Steven C. “<a class="blue-link" href="https://archive.bookofmormoncentral.org/content/raising-stakes-how-joseph-smith%E2%80%99s-first-vision-became-all-or-nothing">Raising the Stakes: How Joseph Smith’s First Vision Became All or Nothing</a>.” BYU Studies Quarterly 59, no. 2 (2020): 23-58.</p>
<p>Steven C. Harper, “<a class="blue-link" href="https://rsc.byu.edu/no-weapon-shall-prosper/suspicion-trust-reading-accounts-joseph-smiths-first-vision">Suspicion or Trust: Reading the Accounts of Joseph Smith&#8217;s First Vision</a>,&#8221; in <em>No Weapon Shall Prosper: New Light on Sensitive Issues</em>, ed. Robert L. Millet (Provo, UT: Religious Studies Center, Brigham Young University; Salt Lake City: Deseret Book, 2011), 63–75.</p>
<p>Matthew C. Godfrey, “The Second Sacred Grove: The Influence of Greenville, Indiana, on Joseph Smith’s 1832 First Vision Account,” <em>Journal of Mormon History</em> 44, no. 4 (October 2018): 1–18.</p>
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
					<p>Scott Woodward:  <br />
Hello. This is Scott Woodward with Scripture Central. I am delighted and excited to announce our new podcast about church history topics called <em>Church History Matters</em>. In this podcast, my good friend Casey Griffiths and I pick a rich and important and sometimes controversial church history topic and explore it in depth together. Casey and I have both been studying and teaching Latter-day Saint church history topics in one way or another for over 20 years. So if you&#8217;re like us and can&#8217;t seem to get enough of church history, or if you&#8217;ve got questions on any of these topics we&#8217;re discussing and want to do a deep dive with us, then you&#8217;re in the right place. We&#8217;re excited and happy to have you along for the ride. For our first series, we chose to discuss Joseph Smith&#8217;s First Vision because that seemed like a great place to start. So here we go. Enjoy our first episode. Joseph Smith&#8217;s First Vision is foundational to our narrative of the Restoration today, but it was not always so from the church&#8217;s beginning. In fact, some early converts join the church without ever having heard of Joseph&#8217;s First Vision, since he seems to have rarely shared this experience publicly. So how did the First Vision go from what began as a very personal experience of Joseph&#8217;s to growing in institutional significance for the whole church as it has today? Joseph also wrote or dictated essentially four separate accounts of his First Vision over a 10-year period, from 1832 to 1842, and each account contains unique differences from the others, sometimes significant ones. Some details, like Joseph&#8217;s age at the time and the number of beings he saw in the vision can also be perceived as possibly contradictory or at least ambiguous. So how are we to make sense of these differences, possible contradictions, and ambiguities? And what role does our personal hermeneutic play in how we do so? Also, did you know that Joseph Smith&#8217;s first recorded account of his vision, written in 1832, was also his last account to come to light? It wasn&#8217;t rediscovered and made publicly available until the second half of the 20th century. What&#8217;s the story behind that? There&#8217;s also a letter Joseph Smith wrote to his wife, Emma, while he was stuck in Indiana, that has recently been suggested by one scholar as offering clues to the obscure historical context behind his 1832 account. What unique elements are explained by this new Indiana framing of the historical context? All of this and more coming your way on today&#8217;s episode of <em>Church History Matters</em>, a podcast of Scripture Central. I&#8217;m Scott Woodward, a managing director at Scripture Central, and my co-host is Casey Griffiths, also a managing director at Scripture Central. And today Casey and I dive into our first episode in this series dealing with Joseph Smith&#8217;s First Vision.</p>
<p>Casey Paul Griffiths: <br />
Today we&#8217;re going to tackle one of my favorite subjects in church history, and that is the accounts of the First Vision. So let&#8217;s talk a little bit about this topic and why it&#8217;s such a big deal. First of all, is it a big deal? Is this a nice story, or is it a key pillar of the Restoration? Scott, what&#8217;s you&#8217;re feeling on that?</p>
<p>Scott Woodward:  <br />
I would call this a foundational topic. In fact, can I share a quote?</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm. Yeah.</p>
<p>Scott Woodward:  <br />
Then this one&#8217;s from President Ezra Taft Benson. He just said it nice and succinctly, so we&#8217;ll use this one: He said, “The First Vision constitutes the heart and the foundation of the church. If Joseph Smith&#8217;s testimony of seeing God the Father and his Son Jesus Christ is not true, then Mormonism represents a false system of belief. But if this vision was reality, then the Church of Jesus Christ was and is restored on earth again.” So there you go. I think President Benson, if he was here, he would say, yeah, this is foundational. This is heart and soul of the church. Everything&#8217;s going to rise or fall based on the veracity or falsity of the First Vision.</p>
<p>Casey Paul Griffiths: <br />
You share that Ezra Teff Benson quote. There&#8217;s a Gordon B. Hinckley quote that says the same thing, and there&#8217;s a Thomas S. Monson quote that says the same thing, and President Nelson issued the Restoration proclamation. Like, there&#8217;s no backing off on how important this is.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
But one thing we ought to mention is as important as the First Vision is to us today, I don&#8217;t know if it&#8217;s always been considered to be central. There&#8217;s a great article by Steve Harper called “Raising the Stakes: How Joseph Smith&#8217;s First Vision became All or Nothing,” where he talks about how in the early church, it doesn&#8217;t seem like the First Vision was held up as, like, the central or first thing that you teach everybody. Like, when I was a missionary in the late ’90s, we went to a person&#8217;s house, we introduced God and Jesus Christ, prophets, and then bam: First Vision.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
But indications are that in the early church, the First Vision wasn&#8217;t the first thing that you would teach somebody. In fact, the Book of Mormon, and its miraculous translation, was kind of the go-to first discussion material.</p>
<p>Scott Woodward:  <br />
Yeah. I think in the first 10 years for sure of the church, the major evidence that Joseph Smith was a true prophet and that there was new revelation was the Book of Mormon. Absolutely. That was the message, and that was the evidence. In fact, it might strike some listeners as peculiar to note that some members of the church in the 1830s may not have even known that there was a First Vision.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
This is not something that Joseph led out with. It doesn&#8217;t seem that to him this was institutionally significant early on, but that over time this is going to grow in institutional significance to Joseph. Of course, it was always deeply, personally significant to Joseph, right?</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
But in terms of what meaning and significance his very personal, visionary encounter with God might have for members of the church and for the narrative of our church&#8217;s history, I think that came gradually for him. Over time he appears to grow in both confidence in sharing the vision and in his belief that it would matter to his hearers.</p>
<p>Casey Paul Griffiths: <br />
Yeah, and I think that&#8217;s understandable, right? First of all, while Joseph Smith is alive, building the institution around an experience that&#8217;s so linked to him could be seen as maybe a little arrogant or egotistical.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
There&#8217;s also indications that Joseph used this as a personal experience that he in time sort of come to a realization of how important it would be for other people to know this. And then there&#8217;s just the material argument. The Book of Mormon is something you can put into someone&#8217;s hands. You can say, “read this.” You can touch it. You can feel it. You can turn to Moroni&#8217;s promise at the end and read through that and say, “Here&#8217;s the process prescribed for how we come to know if these things are true.”</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
So it makes sense to me that that would be the first discussion of Joseph Smith&#8217;s era, but I can also see why the First Vision has, over time, really grown to become this key experience in what makes Latter-day Saints what they are, because—you know, one biography of Joseph Smith calls him the first Mormon. I know we don&#8217;t use that term very much anymore, but if our religion is built around the idea of personal revelation, of everybody seeking a witness from God for themselves through the Holy Spirit, Joseph Smith is a great example of how that process works.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
And the First Vision itself illustrates that God will answer anybody that seeks to know, even a pathetic little farm boy that lives in a rural town in upstate New York. If he&#8217;ll answer him, he&#8217;ll answer you.</p>
<p>Scott Woodward:  <br />
Yeah. I think that impulse, that was always there from the beginning, but it seemed over time. I think—my reading on this is that, yeah, that Joseph Smith&#8217;s experience started to become sort of a prototype of how we could get our own witness from God, the James 1:5, right? I learned from myself that James was telling the truth that any of you, “if any of you lack wisdom,” you can ask of God.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
His experience was more dramatic. His was definitely a much more of a theophany than any of us would expect, but the pattern of God revealing to sincere seekers, I think it was there from the beginning, but I think that has definitely, at least in the 20th and 21st century, that&#8217;s definitely how we tend to use the story of the First Vision.</p>
<p>Casey Paul Griffiths: <br />
It&#8217;s such a good way of teaching that revelatory pattern of ask, pray, receive an answer.</p>
<p>Scott Woodward:  <br />
Totally.</p>
<p>Casey Paul Griffiths: <br />
Joseph Smith writes five different accounts of the First Vision. Really, four major ones, I guess we&#8217;d say.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
There&#8217;s 1832, which is a private account. It&#8217;s never published within his own lifetime, and we&#8217;ll talk about why that may have been. In 1835, and he writes an account that&#8217;s captured in his journal. It&#8217;s an exchange he has with a man named Robert Matthews, and it&#8217;s recorded by one of his scribes. In his journal, he tells the story of the First Vision to Robert Matthews. It&#8217;s written down.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
In 1838, Joseph Smith writes his official history. This is the one that most people are familiar with, the one that&#8217;s in the Pearl of Great Price that&#8217;s considered canon by Latter-day Saints, and then in 1842 he writes what&#8217;s popularly known as the Wentworth Letter.</p>
<p>Scott Woodward:  <br />
Mm-hmm.</p>
<p>Casey Paul Griffiths: <br />
The Wentworth letter written to John Wentworth, editor of the Chicago Democrat, is published in the Times and Seasons just as church history. That&#8217;s what you&#8217;d find it under, if you look for the Joseph Smith Papers site.</p>
<p>Scott Woodward:  <br />
Mm-hmm.</p>
<p>Casey Paul Griffiths: <br />
And then there&#8217;s an extension off that that&#8217;s sometimes counted as a separate account, too, but it&#8217;s very, very close to the ’38 history as well. So those are the five things that come from him. And why, Scott, would these five be considered more important than, say, other people, like Orson Pratt or Orson Hyde or Levi Williams, that also wrote accounts of the First Vision?</p>
<p>Scott Woodward:  <br />
Yeah. These accounts—as all good historical researchers know, firsthand accounts are always best, right?</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm.</p>
<p>Scott Woodward:  <br />
As we&#8217;re trying to piece together the First Vision, we&#8217;re not piecing it together from recollections of what people remember hearing Joseph say; these accounts are from Joseph directly, right? So that&#8217;s historical gold, isn&#8217;t it?</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm.</p>
<p>Scott Woodward:  <br />
I mean, this—firsthand accounts are—we call them primary sources, right? And so a primary source is always going to be better than a secondhand, thirdhand account. We value secondhand accounts, especially those who are close to Joseph, but firsthand accounts are the historical gold standard for sure.</p>
<p>Casey Paul Griffiths: <br />
Yeah. And it&#8217;s just logical that if you want to know what happened, you talk to someone that was actually there.</p>
<p>Scott Woodward:  <br />
Mm-hmm.</p>
<p>Casey Paul Griffiths: <br />
Orson Pratt, for instance, writes a great account of the First Vision, one account that we think influenced Joseph Smith and how he writes the 1842 account, but Orson Pratt wasn&#8217;t there. He heard it probably from Joseph Smith directly, which makes him a secondhand witness, which could be a really, really big deal.</p>
<p>Scott Woodward:  <br />
Mm-hmm.</p>
<p>Casey Paul Griffiths: <br />
But in historical discourse, we&#8217;re going to go with a primary source over a secondary source, and that&#8217;s why we&#8217;re going to focus first on how Joseph Smith recorded the First Vision, and then we&#8217;ll spend a little bit of time on contemporary witnesses that also recorded the First Vision.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
People like Orson Pratt, who was assigned to write the First Vision, or people like Levi Williams or Alexander Neibaur, who are there when he recites the First Vision and they record it in their journals or whatever.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
Or even a guy named David Nye White, who was a reporter from a newspaper who Joseph Smith told the story of the First Vision to, and he publishes it in his newspaper. All of those are going to help us fill in the details, but the substance here, the first place that we want to start, is primary sources.</p>
<p>Scott Woodward:  <br />
Mm-hmm.</p>
<p>Casey Paul Griffiths: <br />
Something that was written by a direct participant.</p>
<p>Scott Woodward:  <br />
Awesome. Okay, so with all these different accounts, there must be some differences in these accounts. Are there inconsistencies? Are there discrepancies? When you actually sit down and read these, what do you see?</p>
<p>Casey Paul Griffiths: <br />
Yeah. This is where we get into historiography, or kind of how messy it is to make a historical account, because most people would read something like the 1838 history and just say, “Yep. Okay. He told this story,” and not realize how messy creating a historical account is. Like, I do an experiment with my students in class where I just say, “Hey, turn to a partner and tell them what happened last weekend.” So they have one minute they have to say what happened over the weekend, and they tell this story, and at the end I stand up and say, “You&#8217;ve just created a historical account, but answer a couple questions: Did you edit this?” And all of them are like, “No, I just told them what happened.” I&#8217;m like, “Okay. Did you say everything that happened, first of all?” “No. We only had a minute.” And then I say something like, “Would you have told the story differently if you were talking to a different person? Like, what if you&#8217;re talking to your best friend? Would you have told the story differently? What if you were talking to your mom? Would you have told the story differently?”</p>
<p>Scott Woodward:  <br />
Yeah. What if it was a newspaper reporter who asked you what happened?</p>
<p>Casey Paul Griffiths: <br />
Yeah. We naturally edit what happens in our lives as we tell stories based on the audiences that we&#8217;re talking to.</p>
<p>Scott Woodward:  <br />
Yeah, totally.</p>
<p>Casey Paul Griffiths: <br />
If somebody from a newspaper calls me, I&#8217;m going to know that what I&#8217;m saying goes on public record, and I&#8217;m going to be very cautious about what I say.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
If I&#8217;m, on the other hand, talking to, you know, a close friend, I might be more candid as to how I feel or what went on. There&#8217;s a natural editing process that we just do automatically.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
And the First Vision accounts do have discrepancies within them, but they come under varying circumstances and sometimes years apart in Joseph Smith&#8217;s life, and you can see that at certain points and times his priorities have changed or he&#8217;s realized something new, and so he tells the story differently than when he told it earlier. Doesn&#8217;t mean that the story isn&#8217;t true. It means that he is adjusting the story based on who he&#8217;s talking to or based on his understanding of what the story actually means.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
Like, when I tell my kids the story of how I met my wife, I&#8217;m telling it from the perspective of she is now my wife. If it hadn&#8217;t worked out between us. I might tell that story totally differently. In fact, my wife has pointed out the first time she is mentioned in my journal, and I keep a decent journal, is the night we got engaged. Like, we had dated for seven months before we got engaged, but the first night, her name appears in my journal is “Tonight I got engaged to Elizabeth Ottley.” She&#8217;s like, “What the heck was going on?” And I&#8217;ve told her, like, “I thought you were out of my league. I didn&#8217;t think it was going to work out, and frankly, I didn&#8217;t want to revisit those painful memories, so I didn&#8217;t put you in here until I had everything locked down, basically. I was hedging my bets,” right? And if some future historian 200 years from now reads my journal, is he going to be like, “He just got engaged to someone he just barely met, because there&#8217;s no mention of her up to that point,” when in reality we&#8217;d been dating for seven months.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
When I tell my kids the story of how I met their mother, all that stuff goes into the narrative, but in 2000, when we got engaged, I was crafting a narrative that I thought would cause me minimum amounts of pain.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
And so I manipulated the narrative. I didn&#8217;t do it to be malicious. I wasn&#8217;t lying. I was doing it to try and protect my own fragile ego. because I was dating somebody I thought was way out of my league. I was editing, right, without even knowing I was editing.</p>
<p>Scott Woodward:  <br />
Yeah. And that&#8217;s not a dishonest practice. That just depends on context.</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm.</p>
<p>Scott Woodward:  <br />
And, you know, I mean, it&#8217;s obvious to say that there are differences in these accounts, but what I like to explain to my students is what you make of these differences depends on your hermeneutic.</p>
<p>Casey Paul Griffiths: <br />
That&#8217;s a big word, Scott. You better explain what hermeneutics are.</p>
<p>Scott Woodward:  <br />
Yeah. We&#8217;re dropping it here on our podcast.</p>
<p>Casey Paul Griffiths: <br />
Yeah. Yeah. Bring it on.</p>
<p>Scott Woodward:  <br />
A hermeneutic is the lens by which you interpret what you see, hear, read—it&#8217;s usually used in reading. I think this is a Stephen Harper phrase, actually. I think as I listened to him talk about the First Vision, yeah, I think he brought this up, so let me give credit to Steve. The phrase he used was a hermeneutic of suspicion versus the hermeneutic of trust. That if you come at the First Vision accounts with a hermeneutic of suspicion, right? That is, you are already jaded. You already believe that Joseph Smith is a fraud and a liar, and that he&#8217;s just getting up this religion for some personal aggrandizement or whatever—</p>
<p>Casey Paul Griffiths: <br />
Right.</p>
<p>Scott Woodward:  <br />
—then that&#8217;s going to color your lens by which you read the accounts and therefore is going to color how you make sense of the differences in the accounts.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
And so for someone who comes at it like I do, with a hermeneutic of trust—I believe Joseph is honest. I believe he&#8217;s imperfect for sure, but, I believe he&#8217;s telling something that really occurred and something that&#8217;s very significant to him, and so when you come at it with a hermeneutic of trust, you&#8217;re now going to be reading these accounts and the differences in the accounts with trust. So, for instance, in the 1940s, Fawn Brodie, a woman who left the church and kind of on her way out of the church she wrote a book, a biography of Joseph Smith, <em>No Man Knows My History</em>, and it was kind of her way of making sense of her faith experience, making sense of Joseph. If you leave the church, you have to explain Joseph Smith, right? And this is her effort to explain Joseph Smith.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
With her hermeneutic of suspicion, she reads the differences in these accounts with the interpretation that what Joseph was doing was he was embellishing the story over time, right? She calls it the elaboration of some half-remembered dream. So she thinks that he&#8217;s kind of—you know, the fish gets bigger every time he tells the story, whereas with the hermeneutic of trust, you rejoice. It thrills your soul to get additional details about this experience, and at the end of the day, they don&#8217;t contradict, they actually enhance. And so I think that&#8217;s just important to point out is that the differences are just the differences,</p>
<p>Casey Paul Griffiths: <br />
Right.</p>
<p>Scott Woodward:  <br />
How you interpret the differences really is going to depend upon your hermeneutic.</p>
<p>Casey Paul Griffiths: <br />
Yeah. And to be honest with you, it&#8217;s just like you said, from a hermeneutic of trust, when you read a new account of the First Vision that you&#8217;re not familiar with, it&#8217;s something to rejoice over.</p>
<p>Scott Woodward:  <br />
That&#8217;s right.</p>
<p>Casey Paul Griffiths: <br />
To say, “Hey, here&#8217;s some new details on a beloved story that I wasn&#8217;t aware of.”</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
History is messy, and to me, differences in the accounts isn&#8217;t a sign that it&#8217;s made up. It&#8217;s a sign that it&#8217;s organic.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
That Joseph Smith didn&#8217;t have a memorized script that he recited every time he wanted to tell this story. That over time its significance may have changed. He may have realized, oh, this detail, which I overlooked, was really significant. I need to emphasize that.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
And another thing that we might point out here, too, is there&#8217;s places in the Bible. Like, one is Paul&#8217;s vision on the road to Damascus. That&#8217;s told in three different places in the Book of Acts, same teller each time. Paul, same writer each time, Luke, but each account has minor discrepancies within it. Does that mean that the story&#8217;s false? No. The essence of the story is still there and still the same over time. Jesus appeared to Paul. Paul was called to the ministry. Why did Paul sometimes vary—or was it Luke, the person that&#8217;s writing it down that varied? I have no idea, but each account should help us get a little bit closer.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
All of those things together combined for an organic narrative. So what we want to do is take each account and say, “Here&#8217;s the context of what was going on. Here&#8217;s why Joseph Smith may have written the vision at this time.”</p>
<p>Scott Woodward:  <br />
Mm-hmm.</p>
<p>Casey Paul Griffiths: <br />
And then try and say what is unique about each vision. So let&#8217;s start with 1832.</p>
<p>Scott Woodward:  <br />
This was the last copy of the First Vision, last account that we discovered, isn&#8217;t that correct?</p>
<p>Casey Paul Griffiths: <br />
Yeah. It&#8217;s interesting because even though this is the earliest account, it&#8217;s kind of the last one that comes to light.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
It&#8217;s written in 1832, but it never shows up in any church publication in Joseph Smith&#8217;s lifetime. In fact, it seems like it just got packed away in a box somewhere and comes to light in the 20th century. And today we look at that with the Joseph Smith Papers and every possible document that Joseph Smith wrote being published and put out to the world, but it&#8217;s very, very understandable that this was, unfortunately, sort of lost and then rediscovered.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
So it winds up in the church archives, which—in my understanding, you go back and read guys like Leonard Arrington, in the early 20th century the church archives were kind of a mess. There was all kinds of profound, amazing stuff in it, but it just hadn&#8217;t been well organized. And some worker, were not even sure who, found this. There&#8217;s evidence that it was repaired in the 1930s, like somebody had put some cellophane tape on it that came from the 1930s, but that nobody had thought, “Whoa. This is something we need to get out to the world.”</p>
<p>Scott Woodward:  <br />
Hmm.</p>
<p>Casey Paul Griffiths: <br />
In the 1960s Paul Cheesman, who&#8217;s a BYU guy, puts this in his thesis as an appendix, and then a couple years later, I believe it&#8217;s James Allen publishes a seminal article on all the different accounts of the First Vision. He includes this, and then we&#8217;re off to the races. Again, if you understand how historiography works, especially how—the church archives, I&#8217;ve got to be honest with you, weren&#8217;t always as well organized as they are today. In fact, it&#8217;s really been the last 30 or 40 years that we went in and systematically organized what&#8217;s there.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
And so just a hidden gem that I&#8217;m so grateful we have access to. I think this account of the First Vision needs to receive more circulation because it&#8217;s just beautiful and profound. I think it&#8217;s a great thing.</p>
<p>Scott Woodward:  <br />
Amen.</p>
<p>Casey Paul Griffiths: <br />
This is the first of five times that Joseph Smith is going to write the story, though there&#8217;s indications that he told the story to a lot of people on a regular basis. This is the first time it&#8217;s in writing, and the 1832 history is interesting because it&#8217;s in Joseph Smith&#8217;s own handwriting as well.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
At least the first of it. Then he switches over to Frederick G. Williams‘ handwriting, who—Frederick G. Williams is going to be placed in the First Presidency in a couple months after this, and a lot of this account is written in Frederick G. Williams&#8217; handwriting.</p>
<p>Scott Woodward:  <br />
Mm-hmm.</p>
<p>Casey Paul Griffiths: <br />
And we&#8217;re not even sure the exact date here. If you look up this document on the Joseph Smith Papers site, it will say circa summer 1832. So we&#8217;re using external clues.</p>
<p>Scott Woodward:  <br />
Yeah. So that&#8217;s I think—what? July is when he becomes Joseph&#8217;s kind of right-hand man, his scribe. And so that&#8217;s why we think it&#8217;s got to be no earlier than July 1832.</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm.</p>
<p>Scott Woodward:  <br />
And then in September, section 84 is received by Joseph, which sort of alters the lexicon by which he refers to priesthood, right? Greater priesthood, high priesthood, lower priesthood.</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm.</p>
<p>Scott Woodward:  <br />
He doesn&#8217;t quite know what to call those. In this account, there&#8217;s a phrase about receiving the holy priesthood from John the Baptist, and then the high priesthood. Like, he&#8217;s not really differentiating these. But then in September, section 84 is received, and we get this lexical change in how he&#8217;s talking about priesthood. And so it seems it&#8217;s got to be before September, but after Frederick G. Williams comes on. So that July to September timeframe.</p>
<p>Casey Paul Griffiths: <br />
Yeah. 1832, good year, bad year for Joseph Smith. Good stuff, bad stuff going on.</p>
<p>Scott Woodward:  <br />
Yes. Good stuff and bad stuff.</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm.</p>
<p>Scott Woodward:  <br />
1832 is a great year in some ways. This is the year that Joseph&#8217;s going to, for instance, get section 76, of the Doctrine and Covenants—the vision, it&#8217;ll be called—section 84, section 88. Some of these doctrinally amazing, like, watershed revelations that are just remarkable. Missionary work is going great. Joseph Smith Translation of the Bible&#8217;s proceeding very well. But on the other hand, Joseph and Sidney had been tarred and feathered in March of that year in Hiram, Ohio, and that caused Joseph Smith&#8217;s son to die that night. The door was left open when they dragged Joseph out of his home, and his son, who was already sick, just a baby at the time, because of exposure that night passed away. So Emma is grieving over that, and so is Joseph, of course, but Joseph needs to then leave and go to Missouri to attend to some of the business of the church over in Missouri. The revelation had commanded him to go, and so he&#8217;s left his wife grieving. He&#8217;s grieving. They go to Missouri, and on his way back, something happened. You want to tell that story?</p>
<p>Casey Paul Griffiths: <br />
Yeah. So a historian named Matt Godfrey who works with the Joseph Smith Papers project has made a really compelling case for why Joseph Smith may have written the First Vision and where and when he wrote it.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
So he and Sidney Rigdon are on their way back from this trip to Missouri. The church is split between two areas, right? In Kirtland, Ohio; Independence, Missouri. More church members are in Missouri than in Ohio at this point. On their way back, they&#8217;re riding in a stage coach near Greenville, Indiana, and the stage coach has a runaway, and they have to jump out. And Joseph&#8217;s friend, Newell K. Whitney, gets caught on the door and breaks his leg in a couple different places. Now these men have all been gone from their families for a couple weeks. They&#8217;re anxious to go home, but Newell can&#8217;t travel. He&#8217;s too badly beat up, and so Newell has to stay. Joseph Smith volunteers to stay behind with Newell in Greenville while everybody else goes on. During this time, another indication that Joseph Smith may have written the 1832 account of the First Vision is a letter that he writes to Emma Smith.</p>
<p>Scott Woodward:  <br />
Mm-hmm.</p>
<p>Casey Paul Griffiths: <br />
You can find this letter on the Joseph Smith Papers site. He writes her from Greenville, and he gives a lot of contextual clues here that he&#8217;s thinking about his life and, like, why is there so much going on right now that is so difficult to deal with? He writes her and says, “My situation is a very unpleasant one, although I will endeavor to be contented, the Lord assisting me. I have visited a grove, which is just in the back of town, almost every day, where I can be secluded from the eyes of any mortal and there give vent to all the feelings of my heart.” So he&#8217;s visiting a grove near town. Does that sound familiar?</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
There&#8217;s a good reason why this may have brought to mind a specific event in his life. He even says, “In meditation and prayer, I&#8217;ve called to mind all the past moments of my life, and I am left to mourn and shed tears of sorrow for my folly in suffering the adversary of my soul to have so much power over me as he has had in times past.” So he&#8217;s calling to his mind everything that&#8217;s happened, including his failures, the moments where he&#8217;s failed. But as the letter continues, he brightens a little bit. Here&#8217;s the next thing that he writes: “But God is merciful and has forgiven my sins, and I rejoice that he sendeth forth the comforter unto as many as believe and humbleth themselves before him. I shall try to be contended with my lot, knowing that God is my friend. In him I shall find comfort. I&#8217;ve given my life unto his hands and am prepared to go at his call. I desire to be with Christ.” So there&#8217;s so many contextual clues there that maybe the reason why he writes his history down for the first time is he just has a moment to pause. He can&#8217;t go anywhere or do anything. He has to stay and take care of Newell.</p>
<p>Scott Woodward:  <br />
So he&#8217;s stuck there with Newell.</p>
<p>Casey Paul Griffiths: <br />
He&#8217;s in quarantine.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
That resonates with everybody out there.</p>
<p>Scott Woodward:  <br />
Yeah. Just waiting for his friend to heal, his leg to heal enough to travel.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
Yeah. He&#8217;s there for a month.</p>
<p>Casey Paul Griffiths: <br />
Yeah. So it would make sense that while he has some time—he says in his letter to Emma, “I&#8217;ve called to mind all the events of my past”—that maybe he&#8217;s sitting down, trying to write it, which does suggest one compelling reason to write the history at this point. He might be writing the history for himself. He&#8217;s had so many difficult things happen, including Sidney Rigdon is really negatively affected by the mob attack. Later on in the summer, Sidney Rigdon is going to say some crazy things, and Joseph Smith is going to have to remove his preaching license for a little while. It&#8217;s possible that he&#8217;s writing this to remember that he has received a remission of his sins and that he has this divine call. I think that the possible audience for the 1832 history might be Joseph Smith: that he&#8217;s writing to make sense of his feelings and to work it out, because the indications are that the document we have right now, the one you&#8217;d see on the Joseph Smith Papers site was copied from some kind of earlier document. So Matt Godfrey&#8217;s theory is that he may have written it while he&#8217;s in Greenville, and then when he gets to Kirtland, he enlists Frederick G. Williams and records it in a more permanent form into this notebook that we have today as the 1832 account of the First Vision.</p>
<p>Scott Woodward:  <br />
Yeah. So you&#8217;re suggesting that perhaps his audience was himself, as maybe a self reassurance to think about the marvelous experiences. That&#8217;s the phrase he uses, right? The “marvelous experiences” that I have experienced. So can I throw out an alternate there?</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm.</p>
<p>Scott Woodward:  <br />
How about Sidney Rigdon, in that tarring and feathering he had severely lacerated his head. He&#8217;d been thumped along a frozen ground for, what, 50 yards or so?</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
Yeah. He was delirious for several days. Then he started saying stuff like, “The keys of the kingdom are lost, the keys of the kingdom are lost,” right? And Joseph had to reassure the Saints and say, no, the keys of the kingdom are right here. The keys of the kingdom have been given to me, and they&#8217;re not going anywhere.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
So maybe an alternate reading is that he is going to write this account because members of the church are a little confused by Sidney and Joseph maybe perhaps realizes he&#8217;s never told his story. He&#8217;s never told his own personal history as to where he received his prophetic authority. That&#8217;s never been made fully explicit. The Book of Mormon is evidence that he is a prophet, but what were the foundational stories that gave Joseph Smith legitimacy as a prophet?</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm.</p>
<p>Scott Woodward:  <br />
And again, we don&#8217;t know because Joseph never does anything with the 1832 history. It&#8217;s six pages long, and it goes nowhere, right? So we don&#8217;t know his intentions, whether it was meant to be published or whether it was meant to be personal, so I like your theory, I just am throwing out another theory that perhaps this was to help reassure the saints that, based on a few key experiences in his early life, he does have legitimate authority. And you don&#8217;t have to worry about this weird stuff that a head trauma—Sidney Rigdon has been spouting off in his kind of fits of momentary frenzy.</p>
<p>Casey Paul Griffiths: <br />
Yeah. And honestly, it might be a little bit of both.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
When he gets to Kirtland, Sidney Rigdon is already the guy in charge.</p>
<p>Scott Woodward:  <br />
Mm-hmm.</p>
<p>Casey Paul Griffiths: <br />
Like, most of the converts in Kirtland are Sidney Rigdon’s congregants.</p>
<p>Scott Woodward:  <br />
Mm-hmm.</p>
<p>Casey Paul Griffiths: <br />
And so he&#8217;s really let Sidney Rigdon drive the car, be the voice of the church.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
When Sidney starts to falter because of his injuries in that mob attack, it&#8217;s possible that Joseph Smith did say, I need to be more assertive in letting them know who I am, where my authority comes from, and what&#8217;s happened to me.</p>
<p>Scott Woodward:  <br />
Yeah. Are we getting right into the text now?</p>
<p>Casey Paul Griffiths: <br />
Yeah, let&#8217;s get to the text.</p>
<p>Scott Woodward:  <br />
Sweet.</p>
<p>Casey Paul Griffiths: <br />
So this account is probably the most different of the four that we&#8217;re going to deal with, and because of that, probably the most controversial.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
You can read all of these accounts on the Joseph Smith Papers site. They&#8217;re also in Gospel Library. I would say read them yourself and make your own judgments.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
But let me just point out a couple highlights, okay? He starts out the First Vision portion of the narrative saying, “At about the age of 12 years, my mind became seriously impressed with regard to the all-important concerns for the welfare of my immortal soul, which led me to searching the scriptures.”</p>
<p>Scott Woodward:  <br />
So he—when he’s 12 years old.</p>
<p>Casey Paul Griffiths: <br />
When he’s 12 years old, yeah.</p>
<p>Scott Woodward:  <br />
We don&#8217;t know that from any other accounts, do we?</p>
<p>Casey Paul Griffiths: <br />
Yeah. Yeah.</p>
<p>Scott Woodward:  <br />
He started this search when he was 12.</p>
<p>Casey Paul Griffiths: <br />
Yeah. And then later on, he says, “From the age of 12 years to 15, I pondered many things in my heart concerning the situation of the world of mankind. The contentions and the visions, the wickedness and abominations, and the darkness which pervaded the minds of mankind.” This is a big deal, because it&#8217;s not like he just went to a couple meetings and then prayed and got his vision.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
This is extending the search to three years, at least, of his young life, where he&#8217;s going to different meetings and listening to different philosophies and kind of weighing the possibilities and trying to figure out which church he should join. This actually answers one of the big, classic attacks on the First Vision. Back in the 1950s there was a guy, Wesley Walters, who was an evangelical, who was kind of the first one to launch a sophisticated attack on the First Vision. Like, rather than just saying Joseph Smith was a liar, so the First Vision isn&#8217;t true, Wesley Walters used historical methodology to attack the First Vision. He looked up a bunch of Methodist records—and Joseph Smith mentions he was drawn to the Methodist sect—and says there was no Methodist revival in Palmyra in 1820. So Joseph Smith&#8217;s whole story must be untrue.</p>
<p>Scott Woodward:  <br />
Mm-hmm.</p>
<p>Casey Paul Griffiths: <br />
The 1832 account actually fixes that, because it gives us a span of years where he could have been going to these meetings, several years where he&#8217;s searching, and a wider span for the story to have taken place.</p>
<p>Scott Woodward:  <br />
Mm-hmm.</p>
<p>Casey Paul Griffiths: <br />
Now, Richard Bushman already took apart Wesley Walters, too, by saying, hey, what if every meeting wasn&#8217;t kept record of? What if he&#8217;s going to smaller meetings? If you look in the accounts, he doesn&#8217;t say big or small. He just mentions, “I attended there several meetings as often as occasion would permit,” which gives us plenty of wiggle room, but it&#8217;s just nice to know that this does confirm that we&#8217;re talking about a lot bigger span of time. There&#8217;s plenty of time here for him to visit all these churches if it&#8217;s a three-year search instead of just a short period of time before the First Vision.</p>
<p>Scott Woodward:  <br />
Okay. Can I point out another thing that&#8217;s awesome in this?</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm. Mm-hmm.</p>
<p>Scott Woodward:  <br />
That—I think that&#8217;s different than the one we&#8217;re more familiar with in the Pearl of Great Price. He says, “My mind became exceedingly distressed, for I became convicted of my sins.” The 1832 account is a story of a convicted sinner.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
Right? He is convicted of his sins, and as he looks around in society, he finds they’re no better. He says, “I felt to mourn for my own sins and for the sins of the world, for I learned that in the scriptures that God was the same yesterday, today, and forever and that he was no respecter of persons, for he was God.” So, you know, this is Joseph seeking personal redemption, primarily, in the 1832 account.</p>
<p>Casey Paul Griffiths: <br />
Yeah. This really fits that narrative that the First Vision starts out as a personal thing for him.</p>
<p>Scott Woodward:  <br />
Yes.</p>
<p>Casey Paul Griffiths: <br />
And then he sort of realizes it&#8217;s theological implications for other people. The 1832 account is deeply personal. It&#8217;s about him and his sins and his struggle to overcome his weaknesses, and you can see that—we don&#8217;t know what this was intended for; it&#8217;s never published—but you can see that he&#8217;s working through his conversion story.</p>
<p>Scott Woodward:  <br />
The one thing that&#8217;s kind of conspicuously missing is that he&#8217;s not trying to decide which church to join explicitly. He does say, “I had found that mankind did not come unto the Lord, but that they had apostatized from the true and living faith, and there was no society or denomination that was built upon the gospel of Jesus Christ as recorded in the New Testament.” So he is denominationally aware, but his question that&#8217;s front and center here in the 1832 account is about his sinfulness rather than about which church I should join.</p>
<p>Casey Paul Griffiths: <br />
Yeah. Yeah.</p>
<p>Scott Woodward:  <br />
Again, different details, different audiences, different context that he&#8217;s writing to. If this is a personal account, he&#8217;s writing in Greenville, Indiana, and he&#8217;s very contemplative about his own sinfulness there, right? I&#8217;ve been visiting a grove every day outside of town. He&#8217;s thinking about his sinfulness, and so as he writes this story, no doubt that would be the thing that is front and center in the account, not so much about which church is right.</p>
<p>Casey Paul Griffiths: <br />
Right.</p>
<p>Scott Woodward:  <br />
Interesting.</p>
<p>Casey Paul Griffiths: <br />
Now, the idea that there was no church that could help him is kind of underwritten into the narrative.</p>
<p>Scott Woodward:  <br />
Yes.</p>
<p>Casey Paul Griffiths: <br />
For instance, he says, “I cried unto the Lord for mercy, for there was none else to whom I could go and obtain mercy.” He doesn&#8217;t find an institutional answer to the question of remission of his sins.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
But that actually leads into the most controversial part of the 1832 account—</p>
<p>Scott Woodward:  <br />
Dun, dun, dun.</p>
<p>Casey Paul Griffiths: <br />
—which is the way he describes the theophany, so—</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
—here&#8217;s the wording from 1832, okay? “And the Lord heard my cry in the wilderness, and while in the attitude of calling upon the Lord in the 16th year of my age, a pillar of light, above the brightness of the sun at noonday, came down from above and rested upon me. I was filled with the Spirit of the Lord, and the Lord opened the heavens upon me, and I saw the ” now there&#8217;s some question there as to is this just a singular appearance?</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
What&#8217;s he describing here? But you can see the obvious place where a person might use this to attack you to basically say, “Well, he says he&#8217;s just seeing the Lord, which seems to be a reference to Jesus Christ.”</p>
<p>Scott Woodward:  <br />
Yeah. Well, I was just thinking in that paragraph. There&#8217;s actually kind of two attacks here, aren&#8217;t there? There&#8217;s from the hermeneutic of suspicion, as you read this, he says, “It was in the 16th year of my age that a pillar of light above the brightness . . . noonday rested upon me,” and then “the Lord opened the heavens upon me, and I saw the Lord” is the second attack. So in one paragraph here, you get two points of controversy: that was he in the 16th year of his age or was he in the 15th year of his age, right, according to other accounts? And was there two personages, or was there one?</p>
<p>Casey Paul Griffiths: <br />
Yeah. Yeah.</p>
<p>Scott Woodward:  <br />
Okay. So let&#8217;s just make a comment about the line where he says, “While in the attitude of calling upon the Lord in the 16th year of my age, a pillar of light above the brightness of sun,” et cetera. So that bit about in the 16th year of my age has been a little burr under some people&#8217;s saddle, because all the other accounts say he was in the 15th year of his age, or that he was 14 years old, right?</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm.</p>
<p>Scott Woodward:  <br />
14 going on 15, and yet this one says, “In the 16th year of my age.” So there&#8217;s a few things about that maybe we should note. First of all, that was not in Joseph Smith&#8217;s handwriting. Joseph Smith wrote that “while in the attitude of calling upon the Lord, a pillar of light above the brightness of the sun at noonday came down.” That&#8217;s it. That is a nice, complete sentence there.</p>
<p>Casey Paul Griffiths: <br />
Right.</p>
<p>Scott Woodward:  <br />
And then Frederick G. Williams comes later and does the little carat above there and says—and you can look at this on Joseph Smith Papers. You can go zoom in as close as you want on the original document, and it says, kind of interlinear-ly, “in the 16th year of my age” in Frederick G. Williams&#8217; handwriting.</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm.</p>
<p>Scott Woodward:  <br />
So not sure what—like, when he wrote that, did he write that at Joseph Smith&#8217;s request? Did he infer from earlier on when Joseph said, “Thus, from the age of 12 years to 15, I pondered many things in my heart concerning the situation of the world.” Did he then infer from that, well, then he would be in his 16th year?</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm.</p>
<p>Scott Woodward:  <br />
So we don&#8217;t know when Frederick G. Williams inserted it, why he did, if Joseph asked him to, if he&#8217;s making some inference based on that 12 to 15 thing.</p>
<p>Casey Paul Griffiths: <br />
Mm-hmm.</p>
<p>Scott Woodward:  <br />
All the other accounts are consistent that he was 14 going on 15.</p>
<p>Casey Paul Griffiths: <br />
Can I make one more argument too?</p>
<p>Scott Woodward:  <br />
Yeah. Please.</p>
<p>Casey Paul Griffiths: <br />
Getting upset about the 16th year comment is very much presentism.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
You know? In our current day and age, we&#8217;ve got clocks everywhere and we&#8217;re overscheduled, and we&#8217;ve got dates and times. In Joseph Smith&#8217;s day, I mean, life was seasonal. It was based on your harvest and your planting seasons and everything like that. And if this is his first stab at the history and it&#8217;s 12 years later, It&#8217;s very understandable that he would be like, I&#8217;m not even sure how old I was when that occurred. Now, when he writes his 1838 history, which is intended for the public, he pins down the dates, okay? I mean, it&#8217;s in the spring of 1820. He still doesn&#8217;t know the exact day, but it was in the spring of 1820 when I was in my 15th year. Later on, Moroni appears when I&#8217;m 17, and by then you can tell that he&#8217;s working with a team, okay, who&#8217;s pressing him to say, let&#8217;s be specific about everything as much as possible.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
The 1832 history is very much exploratory. He&#8217;s writing to work through his feelings, and it includes a lot of superfluous stuff, you know? I would also say it&#8217;s probably the most flowery of any of the ones that he writes, too. The 1838 account, the canon account, has been praised for how direct it is. This one has all kinds of digressions where, I reflected on, you know, the, the wind and the seasons and the way that the Lord does things, and all kinds of stuff like that.</p>
<p>Scott Woodward:  <br />
The stars shining in their courses, and . . .</p>
<p>Casey Paul Griffiths: <br />
Yeah. Yeah. I mean, let me, “I looked upon the sun,” this is an excerpt, “the glorious luminary of the earth, and also on the moon, rolling in their majesty through the heavens, and also the stars shining in their courses and the earth also, upon which I set”—I mean, he just goes on and on, when later on, in the 1838 account, he&#8217;s down to business when he&#8217;s writing an official public history. But in this one, he&#8217;s writing to, like, work through his feelings, to sort out what&#8217;s going on in his life.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
And again, there&#8217;s the possibility that Frederick G. Williams grabbed him and said, when did this all happen? And Joseph said, I don&#8217;t know. When I was 15 or 16.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
That&#8217;s not a big discrepancy, really, when you look at how history was written back then and that, frankly, these aren&#8217;t professional historians that are writing to begin with.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
They tighten up their historical enterprise a little bit later on, but this early one is pretty loosey-goosey.</p>
<p>Scott Woodward:  <br />
So I think it&#8217;s fair to say that the 16th year of my age insert by Frederick G. Williams is a nothing burger.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
It is nothing to be concerned about at all, and it throws no suspicion on the account itself. Absolutely not.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
But I think with the, “the Lord opened the heavens upon me, and I saw the Lord,” there&#8217;s a few things. So if you go to Joseph Smith Papers, you can actually look at the handwriting of this, right? And this is in Joseph Smith&#8217;s handwriting. It&#8217;s actually awesome. You can see Joseph&#8217;s handwriting, and you can see that there&#8217;s moments where he actually misses words, and then he goes back and writes in words. One of the words is Lord. It actually says on the Joseph Smith Papers, it says, “And the [blank] opened the heavens upon me, and I saw the Lord.”</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
And then later on comes back and puts a little carat, realizing he had missed the word, and he put “Lord.” So “the Lord opened the heavens . . . and I saw the Lord.” So I&#8217;m not convinced that He&#8217;s saying that&#8217;s only one being, if he&#8217;s using Lord, both for God, the Father and Jesus Christ, which they did back then, by the way.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
That&#8217;s something—they would use the word Lord to refer to God the Father. We typically in the church today don&#8217;t do that. Usually if we say Lord, we mean Jesus, but in Joseph&#8217;s day, it was not pinned down.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
There&#8217;s several accounts where Lord is used to refer to God the Father, so I&#8217;m not convinced that this is only talking about one person.</p>
<p>Casey Paul Griffiths: <br />
Yeah. Some people have taken this passage to say, well, Joseph Smith hadn&#8217;t developed the idea that God the Father and Jesus were separate by 1832, but I think there&#8217;s a number of reasons why that argument doesn&#8217;t hold water.</p>
<p>Scott Woodward:  <br />
Mm-hmm.</p>
<p>Casey Paul Griffiths: <br />
We sometimes forget that Section 76, which contains Joseph Smith&#8217;s most famous statement about the living Christ, was written before this was.</p>
<p>Scott Woodward:  <br />
Mm-hmm.</p>
<p>Casey Paul Griffiths: <br />
Section 76 is received in February of 1832. This account is written in the summer of 1832, and here&#8217;s a couple excerpts from Section 76: “We beheld the glory of the Son on the right hand of the Father and received of his fulness.” Again, two separate beings. The son on the right hand of the Father.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
“We saw the holy angels and them who were sanctified before his throne worshiping God and the Lamb,” comma, and the Lamb, “who worship him forever and ever. And now, of all the many testimonies which have been given of him, this is the testimony last of all, which we give of him: that he lives. For we saw him, even on the right hand of God, and we heard the voice bearing record . . . He is the only begotten of the Father.” All those passages strongly indicate a separation between the two, that he&#8217;s seeing them as two separate beings in this vision.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
And I tell my students sometimes that “the vision,” section 76, that&#8217;s how we refer to it, as the vision, is really the First Vision. It&#8217;s the First Vision that Joseph Smith writes down at length in any of his historiography. And it seems pretty clear from that that he&#8217;s already seeing God and Jesus as separate, so—</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
—either, you know, that explanation that Lord is a reference to Jesus and Heavenly Father, or I just don&#8217;t know why he only mentioned the Savior in this one, I don&#8217;t think you can make the argument that he hasn&#8217;t worked out that the Father and the Son are separate, or that he believes in the Trinity at this point. That doesn&#8217;t seem to hold water to me.</p>
<p>Scott Woodward:  <br />
No. Well, and even earlier, I think 2 Nephi 31, that&#8217;s 1829, right?</p>
<p>Casey Paul Griffiths: <br />
Right.</p>
<p>Scott Woodward:  <br />
2 Nephi 31 is when God the Father, speaks to Nephi about baptism and then the voice of God the Son speaks to him about baptism, and they&#8217;re kind of going back and forth. The Father speaks, and then the Son speaks. I mean, that&#8217;s probably our clearest example—earliest example of the separation there. So, yeah, I don&#8217;t buy that hermeneutic of suspicion attack on this, saying that this is early Joseph theology that develops later over time and that he&#8217;s going to separate the Godhead later, in his 1835 telling. That just doesn&#8217;t hold up under close scrutiny.</p>
<p>Casey Paul Griffiths: <br />
Yeah, I don&#8217;t think so either. This account has, if you compare all of them, the biggest statement from the Savior. A couple years ago the church made a harmony of all these. They made a movie to show at the Church History Museum that was a harmonized account of all of them, and almost all the text in that movie is taken from the 1832 account because it&#8217;s the most detailed description of what the Savior said. In fact, this is worth reading. This is what he records the Savior as saying. “He spake unto me, saying, ‘Joseph, my son, thy sins are forgiven thee. Go thy way. Walk in my statutes, and keep my commandments. Behold, I am the Lord of glory. I was crucified for all the world that those who believe on my name may have eternal life. Behold, the world lith and sin at this time, and none doeth good. No, not one. They have turned aside from the gospel and keep not my commandments. They draw near to me with their lips while their hearts are far from me, and mine anger is kindling against the inhabitants of the earth to visit them according to their ungodliness and to bring to pass that which hath been spoken by the mouth of prophets and apostles. Behold and lo, I come quickly, as it is written of me, in the cloud, clothed in the glory of my father.’” Now, there&#8217;s a lot there to digest.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
But it&#8217;s also clear this account has the longest statement from the Savior, the most of the words that he said to Joseph Smith.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
Another significant thing about this account, too, is, like, like we said, going back to the personal nature: First statement is “Joseph, my son, thy sins are forgiven thee.”</p>
<p>Scott Woodward:  <br />
Mm-hmm.</p>
<p>Casey Paul Griffiths: <br />
That&#8217;s not mentioned in the 1838 account, because that&#8217;s a public account of the First Vision. He&#8217;s writing this down to remember, like he says in that letter to Emma, that God has forgiven me of my sins. God is my friend. In him I can find strength.</p>
<p>Scott Woodward:  <br />
Yeah. So Joseph goes into the grove in 1832 account as a convicted sinner, “convicted for my sins,” and he leaves with the Son of God&#8217;s declaration ringing in his ears, “Joseph, my son, thy sins are forgiven thee.” No mention of, don&#8217;t join these other churches, or anything like that, right? That is not where the spotlight is in 1832.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
The spotlight is shining directly on this sinfulness piece, and it&#8217;s, I think—I find it beautiful.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
That&#8217;s so good.</p>
<p>Casey Paul Griffiths: <br />
I just want to read one more excerpt. The last thing: “My soul was filled with love. For many days I could rejoice with great joy. The Lord was with me. But I could find none who would believe the heavenly vision. Nevertheless, I pondered these things in my heart.” Again, the one weird thing is is this is the controversial account of the First Vision, right? And yet, when I teach undergrads, this is the account that seems to resonate the most with them.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
This account finds resonance with my students because it teaches really simply two general principles: number one, God knows who you are, like, right down to your first name.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
And number two, God is willing to forgive you of your sins if you&#8217;ll approach him, that God isn&#8217;t the sort of person who will strike you down if you even dare come into his presence. He&#8217;s inviting. He&#8217;s accepting. He wants to forgive you of what you&#8217;ve done wrong, and what Joseph Smith did is something that anybody could do.</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
Could approach God and receive forgiveness of your sins.</p>
<p>Scott Woodward:  <br />
If you just have the faith to ask. That&#8217;s why I love this account, is because I, too, am a convicted sinner, and yeah, that mercy—he says, “I cried unto the Lord for mercy,” and then it came. The mercy came without any chance of misunderstanding, “Joseph, my son, thy sins are forgiven thee.” I just—no wonder your students and mine and me and—we resonate with this, because—maybe our quest today isn&#8217;t so much about which church is true, but can I really be forgiven of my sins?</p>
<p>Casey Paul Griffiths: <br />
Yeah. Does God know who I am, and can I be forgiven?</p>
<p>Scott Woodward:  <br />
Yeah.</p>
<p>Casey Paul Griffiths: <br />
At BYU we have this little sacred grove in the middle of the religion building where we have a statue of Joseph Smith, and President Henry B. Eyring came and dedicated that atrium, and when he dedicated it—this is the only place I&#8217;ve ever seen this. We have a little plaque there. President Eyring pointed out a really significant thing that we wouldn&#8217;t know if we didn&#8217;t have the 1832 I&#8217;ve been forgiven of my sins account. He said this, “The First Vision represents the moment when Joseph learned there was a way for the power of the Atonement to be unlocked fully. Because of what Joseph saw and what began at this moment, the Savior was able, through this great and valiant servant and through others that he sent, to restore power and privilege. That power and privilege allows us and all who will live to have the benefit of Jesus Christ&#8217;s Atonement work in our lives.” President Eyring’s kind of arguing the point that if the First Vision is the starting point of the Restoration, what&#8217;s the first thing that gets restored? And not necessarily priesthood or doctrine: that comes later. The first thing that has to be restored is our connection to the Savior and his Atonement. The power to be forgiven of sins. And I just love that idea, that the very first thing that&#8217;s restored in the course of the Restoration is the ability to receive forgiveness of your sins. That’s a neat insight to me.</p>
<p>Scott Woodward:  <br />
Yeah. So you look: Here we are, two guys reading through the hermeneutic of trust, and here we are getting some beautiful things out of some uniqueness in this account that&#8217;s not in the others. I&#8217;m just grateful for that. It thrills me that there is this—it&#8217;s so personal and so good, and yeah, just—thank you for being someone who reads through the hermeneutic of trust. It&#8217;s refreshing. You know the history as good as anyone, Casey Griffiths, and yet this hermeneutic of trust helps you to see the beauty in this.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
I think just one more thing I would just add as we kind of land the plane, then, today on this is to notice the influence of the context on the text. The context is that this is a very personal history, and therefore notice that the text deals more than any other account with Joseph Smith&#8217;s internal world, right?</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
He uses feeling words. He said he was feeling convicted for his own sins. He was mourning for both his sins and those of the world. He talks about his awe and pondering on the majesty of God. He mentions Jesus&#8217;s tender declaration that his sins were forgiven. Highly personal issue. He talks about how his soul was filled with love for many days thereafter, and how he pondered these things in his heart. This is very internal. This is Joseph&#8217;s internal world. And so just noticing context. Context, context, context.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
All the differences in the accounts can satisfactorily be explained when you sufficiently understand the context.</p>
<p>Casey Paul Griffiths: <br />
Yeah.</p>
<p>Scott Woodward:  <br />
And I think this is a perfect example of that, that this highly personal history has a ton of personal internal world details, which some of the more public accounts lack, and that makes sense in context.</p>
<p>Casey Paul Griffiths: <br />
And that makes this a real, like I said, hidden gem. It&#8217;s deeply personal. It may have been intended for the public. It may have not been intended for the public. At any rate, it&#8217;s really a great starting point to understand Joseph Smith and his perspective on God. And that letter to Emma Smith that we quoted earlier, I think, makes a sweet connection, too, that 12 years later he&#8217;s still wrestling with questions of worthiness, with questions of ability, with, hey, I&#8217;ve been asked to do this huge thing. Am I up to it? The First Vision helped give him the courage that he needed to keep doing what he was doing, to have the fortitude to move forward with what was always a really difficult prophetic mission, but he had confidence in his past experiences. There&#8217;s days when I have to look back and say, “Gosh, I don&#8217;t know if I can do what I have to do right now, but I&#8217;ve done things in the past that were beyond my capability with the Lord&#8217;s help. If he helped me then, I believe he can help me now.”</p>
<p>Scott Woodward:  <br />
Thank you for listening to this episode of <em>Church History Matters</em>. Next week we continue this series on Joseph Smith&#8217;s First Vision by exploring his 1835 account, written as a journal entry about a conversation with an eccentric visitor who styled himself as a Jewish prophet. We will also explore the 1838 account, which was a public-facing, official history written under Joseph&#8217;s direction in Far West, Missouri in the aftermath of rumors, slander, and even death threats against Joseph and other Saints. As with the 1832 account, understanding the historical context surrounding the 1835 and 1838 accounts will help us make sense of why Joseph chose to share certain details about his vision in each account. Today&#8217;s episode was produced by Zander Sturgill and Nick Galieti, edited by Scott Woodward and Nick Galieti, with show notes and transcript by Gabe Davis. <em>Church History Matters</em> is a podcast of Scripture Central, a nonprofit which exists to help build enduring faith in Jesus Christ by making Latter-day Saint scripture and church history accessible, comprehensible, and defensible to people everywhere. For more resources to enhance your gospel study, go to scripturecentral.org, where everything is available for free because of the generous donations of people like you. Thank you so much for being a part of this with us.</p>
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
var eae = {"ajaxurl":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-admin\\/admin-ajax.php","current_url":"aHR0cHM6Ly9kb2N0cmluZWFuZGNvdmVuYW50c2NlbnRyYWwub3JnL3BvZGNhc3QtZXBpc29kZS93aHktYXJlLXRoZXJlLWRpZmZlcmVudC1hY2NvdW50cy1vZi10aGUtZmlyc3QtdmlzaW9uJWUyJTgwJThiLw==","breakpoints":{"xs":0,"sm":480,"md":768,"lg":1025,"xl":1440,"xxl":1600}};
var eae_editor = {"plugin_url":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/plugins\\/addon-elements-for-elementor-page-builder\\/"};
</script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/js/eae.min.js?ver=1.0' id='eae-main-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/js/animated-main.min.js?ver=1.0' id='animated-main-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/js/particles.min.js?ver=1.0' id='eae-particles-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/lib/magnific.min.js?ver=1.9' id='wts-magnific-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/lib/vegas/vegas.min.js?ver=2.4.0' id='vegas-js'></script>
<script id='670754473-js-extra'>
var localize = {"ajaxurl":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-admin\\/admin-ajax.php","nonce":"f0799d4cb4","i18n":{"added":"Added ","compare":"Compare","loading":"Loading..."}};
</script>
<script src='https://doctrineandcovenantscentral.org/wp-content/uploads/essential-addons-elementor/670754473.min.js?ver=1699164202' id='670754473-js'></script>
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
var ElementPackConfig = {"ajaxurl":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-admin\\/admin-ajax.php","nonce":"104413a6d9","contact_form":{"sending_msg":"Sending message please wait...","captcha_nd":"Invisible captcha not defined!","captcha_nr":"Could not get invisible captcha response!"},"elements_data":{"sections":[],"columns":[],"widgets":[]}};
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
var elementorFrontendConfig = {"environmentMode":{"edit":false,"wpPreview":false,"isScriptDebug":false},"i18n":{"shareOnFacebook":"Share on Facebook","shareOnTwitter":"Share on Twitter","pinIt":"Pin it","download":"Download","downloadImage":"Download image","fullscreen":"Fullscreen","zoom":"Zoom","share":"Share","playVideo":"Play Video","previous":"Previous","next":"Next","close":"Close"},"is_rtl":false,"breakpoints":{"xs":0,"sm":480,"md":768,"lg":1025,"xl":1440,"xxl":1600},"responsive":{"breakpoints":{"mobile":{"label":"Mobile","value":767,"direction":"max","is_enabled":true},"mobile_extra":{"label":"Mobile Extra","value":880,"direction":"max","is_enabled":false},"tablet":{"label":"Tablet","value":1024,"direction":"max","is_enabled":true},"tablet_extra":{"label":"Tablet Extra","value":1365,"direction":"max","is_enabled":false},"laptop":{"label":"Laptop","value":1620,"direction":"max","is_enabled":false},"widescreen":{"label":"Widescreen","value":2400,"direction":"min","is_enabled":false}}},"version":"3.2.3","is_static":false,"experimentalFeatures":{"form-submissions":true},"urls":{"assets":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/plugins\\/elementor\\/assets\\/"},"settings":{"page":[],"editorPreferences":[]},"kit":{"active_breakpoints":["viewport_mobile","viewport_tablet"],"global_image_lightbox":"yes","lightbox_enable_counter":"yes","lightbox_enable_fullscreen":"yes","lightbox_enable_zoom":"yes","lightbox_enable_share":"yes","lightbox_title_src":"title","lightbox_description_src":"description"},"post":{"id":31910,"title":"First%20Vision%20Ep.%201%20%E2%80%93%20Why%20Are%20There%20Different%20Accounts%20of%20the%20First%20Vision%3F%E2%80%8B%20%E2%80%93%20Doctrine%20and%20Covenants%20Central","excerpt":"","featuredImage":false}};
</script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/js/frontend.min.js?ver=3.2.3' id='elementor-frontend-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/bdthemes-element-pack-lite/assets/js/element-pack-site.min.js?ver=2.9.2' id='element-pack-site-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor-pro/assets/js/webpack-pro.runtime.min.js?ver=3.2.2' id='elementor-pro-webpack-runtime-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor-pro/assets/lib/sticky/jquery.sticky.min.js?ver=3.2.2' id='elementor-sticky-js'></script>
<script id='elementor-pro-frontend-js-before'>
var ElementorProFrontendConfig = {"ajaxurl":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-admin\\/admin-ajax.php","nonce":"9bc1af2482","urls":{"assets":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/plugins\\/elementor-pro\\/assets\\/"},"i18n":{"toc_no_headings_found":"No headings were found on this page."},"shareButtonsNetworks":{"facebook":{"title":"Facebook","has_counter":true},"twitter":{"title":"Twitter"},"google":{"title":"Google+","has_counter":true},"linkedin":{"title":"LinkedIn","has_counter":true},"pinterest":{"title":"Pinterest","has_counter":true},"reddit":{"title":"Reddit","has_counter":true},"vk":{"title":"VK","has_counter":true},"odnoklassniki":{"title":"OK","has_counter":true},"tumblr":{"title":"Tumblr"},"digg":{"title":"Digg"},"skype":{"title":"Skype"},"stumbleupon":{"title":"StumbleUpon","has_counter":true},"mix":{"title":"Mix"},"telegram":{"title":"Telegram"},"pocket":{"title":"Pocket","has_counter":true},"xing":{"title":"XING","has_counter":true},"whatsapp":{"title":"WhatsApp"},"email":{"title":"Email"},"print":{"title":"Print"}},"facebook_sdk":{"lang":"en_US","app_id":""},"lottie":{"defaultAnimationUrl":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/plugins\\/elementor-pro\\/modules\\/lottie\\/assets\\/animations\\/default.json"}};
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


def test_load_dc_places() -> None:
    """It returns a valid Document for a D&C podcast."""
    url = "https://doctrineandcovenantscentral.org/podcast-episode/why-are-there-different-accounts-of-the-first-vision%e2%80%8b/"
    result = load_dc_podcasts(url, html)
    assert len(result.page_content) > 0
    assert result.metadata["url"] == url
    assert result.metadata["title"] == "Why Are There Different Accounts of the First Vision?"
    assert result.page_content.startswith("Scott Woodward:\n\nHello. This is Scott Woodward")
