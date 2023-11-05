"""Test cases for the load_know module."""
# flake8: noqa

from models.load_dc_places import load_dc_places


html = """
<!DOCTYPE html>
<html lang="en-US">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />		<script>(function(html){html.className = html.className.replace(/\bno-js\b/,'js')})(document.documentElement);</script>
<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />

	<!-- This site is optimized with the Yoast SEO plugin v16.0.2 - https://yoast.com/wordpress/plugins/seo/ -->
	<title>Palmyra-Manchester, New York | Doctrine and Covenants Central</title>
	<link rel="canonical" href="https://doctrineandcovenantscentral.org/palmyra-new-york/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="Palmyra-Manchester, New York | Doctrine and Covenants Central" />
	<meta property="og:description" content="/ Places of the D&amp;C / Palmyra-Manchester, New York Palmyra-Manchester, New York 1820-1830 Photo Credit: Christina Broberg, 2012 Significant Events At a Glance Joseph Smith&#8217;s First Vision Appearances of Moroni Retrieval Site of the Golden Plates Book of Mormon Printed Joseph Sr. and Lucy Smith Homes D&#038;C Sections Received Here (Click for Section Study Helps) &hellip; Continue reading &quot;Palmyra-Manchester, New York&quot;" />
	<meta property="og:url" content="https://doctrineandcovenantscentral.org/palmyra-new-york/" />
	<meta property="og:site_name" content="Doctrine and Covenants Central" />
	<meta property="article:modified_time" content="2021-08-17T20:22:13+00:00" />
	<meta property="og:image" content="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-log-fence.-Christina-Broberg-2012-1-scaled.jpg" />
	<meta property="og:image:width" content="2560" />
	<meta property="og:image:height" content="1707" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:label1" content="Est. reading time">
	<meta name="twitter:data1" content="14 minutes">
	<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://doctrineandcovenantscentral.org/#organization","name":"Doctrine and Covenants Central","url":"https://doctrineandcovenantscentral.org/","sameAs":["https://www.youtube.com/channel/UCqtKadDOHIbx_Zjq9BhxQYg"],"logo":{"@type":"ImageObject","@id":"https://doctrineandcovenantscentral.org/#logo","inLanguage":"en-US","url":"https://doctrineandcovenantscentral.org/wp-content/uploads/2020/12/DC-1.png","width":3300,"height":1752,"caption":"Doctrine and Covenants Central"},"image":{"@id":"https://doctrineandcovenantscentral.org/#logo"}},{"@type":"WebSite","@id":"https://doctrineandcovenantscentral.org/#website","url":"https://doctrineandcovenantscentral.org/","name":"Doctrine and Covenants Central","description":"","publisher":{"@id":"https://doctrineandcovenantscentral.org/#organization"},"potentialAction":[{"@type":"SearchAction","target":"https://doctrineandcovenantscentral.org/?s={search_term_string}","query-input":"required name=search_term_string"}],"inLanguage":"en-US"},{"@type":"ImageObject","@id":"https://doctrineandcovenantscentral.org/palmyra-new-york/#primaryimage","inLanguage":"en-US","url":"https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-log-fence.-Christina-Broberg-2012-1-scaled.jpg","width":2560,"height":1707,"caption":"Photo Credit: Christina Broberg, 2012"},{"@type":"WebPage","@id":"https://doctrineandcovenantscentral.org/palmyra-new-york/#webpage","url":"https://doctrineandcovenantscentral.org/palmyra-new-york/","name":"Palmyra-Manchester, New York | Doctrine and Covenants Central","isPartOf":{"@id":"https://doctrineandcovenantscentral.org/#website"},"primaryImageOfPage":{"@id":"https://doctrineandcovenantscentral.org/palmyra-new-york/#primaryimage"},"datePublished":"2021-01-27T23:13:25+00:00","dateModified":"2021-08-17T20:22:13+00:00","breadcrumb":{"@id":"https://doctrineandcovenantscentral.org/palmyra-new-york/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https://doctrineandcovenantscentral.org/palmyra-new-york/"]}]},{"@type":"BreadcrumbList","@id":"https://doctrineandcovenantscentral.org/palmyra-new-york/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"item":{"@type":"WebPage","@id":"https://doctrineandcovenantscentral.org/","url":"https://doctrineandcovenantscentral.org/","name":"Home"}},{"@type":"ListItem","position":2,"item":{"@type":"WebPage","@id":"https://doctrineandcovenantscentral.org/palmyra-new-york/","url":"https://doctrineandcovenantscentral.org/palmyra-new-york/","name":"Palmyra-Manchester, New York"}}]}]}</script>
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
<link rel='stylesheet' id='843868bf1-css'  href='https://doctrineandcovenantscentral.org/wp-content/uploads/essential-addons-elementor/843868bf1.min.css?ver=1699160209' media='all' />
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
<link rel='stylesheet' id='elementor-post-6942-css'  href='https://doctrineandcovenantscentral.org/wp-content/uploads/elementor/css/post-6942.css?ver=1689746866' media='all' />
<link rel='stylesheet' id='elementor-post-1396-css'  href='https://doctrineandcovenantscentral.org/wp-content/uploads/elementor/css/post-1396.css?ver=1689724145' media='all' />
<link rel='stylesheet' id='elementor-post-1373-css'  href='https://doctrineandcovenantscentral.org/wp-content/uploads/elementor/css/post-1373.css?ver=1689724145' media='all' />
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
<link rel="https://api.w.org/" href="https://doctrineandcovenantscentral.org/wp-json/" /><link rel="alternate" type="application/json" href="https://doctrineandcovenantscentral.org/wp-json/wp/v2/pages/6942" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://doctrineandcovenantscentral.org/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://doctrineandcovenantscentral.org/wp-includes/wlwmanifest.xml" />
<meta name="generator" content="WordPress 5.7.10" />
<link rel='shortlink' href='https://doctrineandcovenantscentral.org/?p=6942' />
<link rel="alternate" type="application/json+oembed" href="https://doctrineandcovenantscentral.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fdoctrineandcovenantscentral.org%2Fpalmyra-new-york%2F" />
<link rel="alternate" type="text/xml+oembed" href="https://doctrineandcovenantscentral.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fdoctrineandcovenantscentral.org%2Fpalmyra-new-york%2F&#038;format=xml" />
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
<body class="page-template page-template-elementor_header_footer page page-id-6942 wp-custom-logo wp-embed-responsive page-two-column title-tagline-hidden colors-light elementor-default elementor-template-full-width elementor-kit-10 elementor-page elementor-page-6942">
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
				<div data-elementor-type="wp-page" data-elementor-id="6942" class="elementor elementor-6942" data-elementor-settings="[]">
						<div class="elementor-inner">
							<div class="elementor-section-wrap">
							<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-55fbffe9 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="55fbffe9" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-3dd7ccb4" data-id="3dd7ccb4" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-4b46ea03 elementor-view-default elementor-widget elementor-widget-icon" data-id="4b46ea03" data-element_type="widget" data-settings="{&quot;_animation&quot;:&quot;none&quot;}" data-widget_type="icon.default">
				<div class="elementor-widget-container">
					<div class="elementor-icon-wrapper">
			<a class="elementor-icon" href="https://doctrineandcovenantscentral.org/">
			<i aria-hidden="true" class="fas fa-home"></i>			</a>
		</div>
				</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-3fd1c7c9" data-id="3fd1c7c9" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-6ebf6c50 elementor-widget elementor-widget-text-editor" data-id="6ebf6c50" data-element_type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
								<div class="elementor-text-editor elementor-clearfix">
					<p>/ <a href="https://doctrineandcovenantscentral.org/places-of-the-doctrine-and-covenants/"><span style="color: #a87a31;">Places of the D&amp;C</span></a> / Palmyra-Manchester, New York</p>					</div>
						</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-09d4b27 places-title-bkgd elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="09d4b27" data-element_type="section" data-settings="{&quot;background_background&quot;:&quot;classic&quot;}">
							<div class="elementor-background-overlay"></div>
							<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-eecf9ec" data-id="eecf9ec" data-element_type="column" data-settings="{&quot;background_background&quot;:&quot;gradient&quot;}">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-8e7942d elementor-widget elementor-widget-heading" data-id="8e7942d" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Palmyra-Manchester, New York</h2>		</div>
				</div>
				<section class="has_eae_slider elementor-section elementor-inner-section elementor-element elementor-element-b4a8c26 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="b4a8c26" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-93dd59a" data-id="93dd59a" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
								</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-83aa478" data-id="83aa478" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-447d744 elementor-widget elementor-widget-heading" data-id="447d744" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">1820-1830</h2>		</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-30b55bb" data-id="30b55bb" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
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
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-b614fa0 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="b614fa0" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-06c0136" data-id="06c0136" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-5d70c4e elementor-widget elementor-widget-heading" data-id="5d70c4e" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Photo Credit: Christina Broberg, 2012</h2>		</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-4e0132c elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="4e0132c" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-e0ff627" data-id="e0ff627" data-element_type="column" data-settings="{&quot;background_background&quot;:&quot;classic&quot;}">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-6bc4678 elementor-widget elementor-widget-heading" data-id="6bc4678" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Significant Events At a Glance</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-34a2bb7 elementor-icon-list--layout-traditional elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list" data-id="34a2bb7" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items">
							<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-check-circle"></i>						</span>
										<span class="elementor-icon-list-text">Joseph Smith's First Vision</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-check-circle"></i>						</span>
										<span class="elementor-icon-list-text">Appearances of Moroni</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-check-circle"></i>						</span>
										<span class="elementor-icon-list-text">Retrieval Site of the Golden Plates</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-check-circle"></i>						</span>
										<span class="elementor-icon-list-text">Book of Mormon Printed</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-check-circle"></i>						</span>
										<span class="elementor-icon-list-text">Joseph Sr. and Lucy Smith Homes</span>
									</li>
						</ul>
				</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-94f62d9" data-id="94f62d9" data-element_type="column" data-settings="{&quot;background_background&quot;:&quot;classic&quot;}">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-0a3e1f5 elementor-widget elementor-widget-heading" data-id="0a3e1f5" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">D&C Sections Received Here</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-38f0cbb elementor-hidden-tablet elementor-hidden-phone elementor-widget elementor-widget-heading" data-id="38f0cbb" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">(Click for Section Study Helps)</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-c4cf18e elementor-hidden-desktop elementor-widget elementor-widget-heading" data-id="c4cf18e" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">(Tap for Section Study Helps)</h2>		</div>
				</div>
				<section class="has_eae_slider elementor-section elementor-inner-section elementor-element elementor-element-1ac462d elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="1ac462d" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-50 elementor-inner-column elementor-element elementor-element-9cef33d" data-id="9cef33d" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-93021b7 elementor-list-item-link-inline elementor-icon-list--layout-traditional elementor-widget elementor-widget-icon-list" data-id="93021b7" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items">
							<li class="elementor-icon-list-item">
					<a href="https://doctrineandcovenantscentral.org/section-2/">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fab fa-slack-hash"></i>						</span>
										<span class="elementor-icon-list-text">Section&nbsp;2</span>
											</a>
									</li>
								<li class="elementor-icon-list-item">
					<a href="https://doctrineandcovenantscentral.org/section-19/">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fab fa-slack-hash"></i>						</span>
										<span class="elementor-icon-list-text">Section 19</span>
											</a>
									</li>
								<li class="elementor-icon-list-item">
					<a href="https://doctrineandcovenantscentral.org/section-22/">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fab fa-slack-hash"></i>						</span>
										<span class="elementor-icon-list-text">Section 22</span>
											</a>
									</li>
						</ul>
				</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-50 elementor-inner-column elementor-element elementor-element-bccfc4b" data-id="bccfc4b" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-50230c9 elementor-list-item-link-inline elementor-icon-list--layout-traditional elementor-widget elementor-widget-icon-list" data-id="50230c9" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items">
							<li class="elementor-icon-list-item">
					<a href="https://doctrineandcovenantscentral.org/section-23/">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fab fa-slack-hash"></i>						</span>
										<span class="elementor-icon-list-text">Section 23</span>
											</a>
									</li>
								<li class="elementor-icon-list-item">
					<a href="https://doctrineandcovenantscentral.org/section-32/">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fab fa-slack-hash"></i>						</span>
										<span class="elementor-icon-list-text">Section 32</span>
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
								</div>
					</div>
		</section>
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-62ee6cd elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="62ee6cd" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-20 elementor-top-column elementor-element elementor-element-01b0467 elementor-hidden-tablet" data-id="01b0467" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
								</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-20 elementor-top-column elementor-element elementor-element-32b5097" data-id="32b5097" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-b98c926 elementor-icon-list--layout-inline elementor-list-item-link-inline elementor-align-center elementor-hidden-phone elementor-widget elementor-widget-icon-list" data-id="b98c926" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items elementor-inline-items">
							<li class="elementor-icon-list-item elementor-inline-item">
					<a href="#1">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-dot-circle"></i>						</span>
										<span class="elementor-icon-list-text">Sacred Grove</span>
											</a>
									</li>
						</ul>
				</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-20 elementor-top-column elementor-element elementor-element-7ecbfd7" data-id="7ecbfd7" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-b2b0974 elementor-icon-list--layout-inline elementor-list-item-link-inline elementor-align-center elementor-hidden-phone elementor-widget elementor-widget-icon-list" data-id="b2b0974" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items elementor-inline-items">
							<li class="elementor-icon-list-item elementor-inline-item">
					<a href="#2">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-dot-circle"></i>						</span>
										<span class="elementor-icon-list-text">Hill Cumorah</span>
											</a>
									</li>
						</ul>
				</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-20 elementor-top-column elementor-element elementor-element-56f1cb2" data-id="56f1cb2" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-9a3892c elementor-icon-list--layout-inline elementor-list-item-link-inline elementor-align-center elementor-hidden-phone elementor-widget elementor-widget-icon-list" data-id="9a3892c" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items elementor-inline-items">
							<li class="elementor-icon-list-item elementor-inline-item">
					<a href="#3">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-dot-circle"></i>						</span>
										<span class="elementor-icon-list-text">Smith Log Home</span>
											</a>
									</li>
						</ul>
				</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-20 elementor-top-column elementor-element elementor-element-18b0d5d elementor-hidden-tablet" data-id="18b0d5d" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
								</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-58c92a2 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="58c92a2" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-20 elementor-top-column elementor-element elementor-element-2383080 elementor-hidden-tablet" data-id="2383080" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
								</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-20 elementor-top-column elementor-element elementor-element-a3aa0a3" data-id="a3aa0a3" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-b100761 elementor-icon-list--layout-inline elementor-list-item-link-inline elementor-align-center elementor-hidden-phone elementor-widget elementor-widget-icon-list" data-id="b100761" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items elementor-inline-items">
							<li class="elementor-icon-list-item elementor-inline-item">
					<a href="#4">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-dot-circle"></i>						</span>
										<span class="elementor-icon-list-text">E. B. Grandin Press</span>
											</a>
									</li>
						</ul>
				</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-20 elementor-top-column elementor-element elementor-element-1a3b26c" data-id="1a3b26c" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-dc2689c elementor-icon-list--layout-inline elementor-list-item-link-inline elementor-align-center elementor-hidden-phone elementor-widget elementor-widget-icon-list" data-id="dc2689c" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items elementor-inline-items">
							<li class="elementor-icon-list-item elementor-inline-item">
					<a href="#5">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-dot-circle"></i>						</span>
										<span class="elementor-icon-list-text">Smith Frame Home</span>
											</a>
									</li>
						</ul>
				</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-20 elementor-top-column elementor-element elementor-element-0f6a139" data-id="0f6a139" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-a274eae elementor-icon-list--layout-inline elementor-list-item-link-inline elementor-align-center elementor-hidden-phone elementor-widget elementor-widget-icon-list" data-id="a274eae" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items elementor-inline-items">
							<li class="elementor-icon-list-item elementor-inline-item">
					<a href="#6">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-dot-circle"></i>						</span>
										<span class="elementor-icon-list-text">Martin Harris Home</span>
											</a>
									</li>
						</ul>
				</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-20 elementor-top-column elementor-element elementor-element-fbf2d5f elementor-hidden-tablet" data-id="fbf2d5f" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
								</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-09ed598 elementor-hidden-desktop elementor-hidden-tablet elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="09ed598" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-5c96b96" data-id="5c96b96" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
								</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-74702e4" data-id="74702e4" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-d50271f elementor-align-center elementor-icon-list--layout-traditional elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list" data-id="d50271f" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items">
							<li class="elementor-icon-list-item">
					<a href="#1">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-dot-circle"></i>						</span>
										<span class="elementor-icon-list-text">Sacred Grove</span>
											</a>
									</li>
								<li class="elementor-icon-list-item">
					<a href="#2">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-dot-circle"></i>						</span>
										<span class="elementor-icon-list-text">Hill Cumorah</span>
											</a>
									</li>
								<li class="elementor-icon-list-item">
					<a href="#3">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-dot-circle"></i>						</span>
										<span class="elementor-icon-list-text">Smith Log Home</span>
											</a>
									</li>
								<li class="elementor-icon-list-item">
					<a href="#4">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-dot-circle"></i>						</span>
										<span class="elementor-icon-list-text">E. B. Grandin Press</span>
											</a>
									</li>
								<li class="elementor-icon-list-item">
					<a href="#5">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-dot-circle"></i>						</span>
										<span class="elementor-icon-list-text">Smith Frame Home</span>
											</a>
									</li>
								<li class="elementor-icon-list-item">
					<a href="#6">						<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-dot-circle"></i>						</span>
										<span class="elementor-icon-list-text">Martin Harris Home</span>
											</a>
									</li>
						</ul>
				</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-c8ba1ad" data-id="c8ba1ad" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
								</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-8a74870 places-place-text elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="8a74870" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-109b6a9" data-id="109b6a9" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-32b011d elementor-widget elementor-widget-menu-anchor" data-id="32b011d" data-element_type="widget" data-widget_type="menu-anchor.default">
				<div class="elementor-widget-container">
					<div id="1" class="elementor-menu-anchor"></div>
				</div>
				</div>
				<div class="elementor-element elementor-element-91ad736 elementor-widget elementor-widget-heading" data-id="91ad736" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Sacred Grove</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-55e1f71 elementor-widget elementor-widget-heading" data-id="55e1f71" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Key Points of Interest</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-3cc3d34 elementor-icon-list--layout-traditional elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list" data-id="3cc3d34" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items">
							<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">Joseph Smith, Jr. saw God the Father and His Son, Jesus Christ, here early in the Spring of 1820</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">The Smiths farmed roughly 60 acres of their 100-acre property and kept about 40 acres for a wood lot. The current Sacred Grove is roughly 10-12 acres within, we believe, the original 40-acre wood plot</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">There are still trees in the Sacred Grove that date back to the time of the first vision—referred to as “witness trees”</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">Joseph showed the golden plates to eight witnesses near here</span>
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
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-7db2696 places-pic-gallery elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="7db2696" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-a19945c" data-id="a19945c" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-3043e2c elementor-hidden-tablet elementor-hidden-phone elementor-widget elementor-widget-heading" data-id="3043e2c" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">(Hover over photo for more information, click to enlarge)</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-32a5257 elementor-hidden-desktop elementor-widget elementor-widget-heading" data-id="32a5257" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">(Tap photo to enlarge and see more information)​</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-e7e5bb8 elementor-widget elementor-widget-gallery" data-id="e7e5bb8" data-element_type="widget" data-settings="{&quot;overlay_title&quot;:&quot;title&quot;,&quot;overlay_description&quot;:&quot;caption&quot;,&quot;gallery_layout&quot;:&quot;justified&quot;,&quot;ideal_row_height&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:200,&quot;sizes&quot;:[]},&quot;ideal_row_height_tablet&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:150,&quot;sizes&quot;:[]},&quot;ideal_row_height_mobile&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:150,&quot;sizes&quot;:[]},&quot;gap&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;gap_tablet&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;gap_mobile&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;link_to&quot;:&quot;file&quot;,&quot;overlay_background&quot;:&quot;yes&quot;,&quot;content_hover_animation&quot;:&quot;fade-in&quot;}" data-widget_type="gallery.default">
				<div class="elementor-widget-container">
					<div class="elementor-gallery__container">
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Sacred-Grove5-tall-trees-drawing-the-eye-heavenward-and-into-the-light.-Janet-Cramer-2018-edit-1.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-e7e5bb8" data-elementor-lightbox-title="Sacred Grove" data-elementor-lightbox-description="Trees stretch high above in the Sacred Grove.
(Photo Credit: Janet Cramer, 2015)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Sacred-Grove5-tall-trees-drawing-the-eye-heavenward-and-into-the-light.-Janet-Cramer-2018-edit-1-768x1024.jpg" data-width="525" data-height="700" alt="An image of trees lit by the sun and covered in green leaves standing in the Sacred Grove." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Sacred Grove</div>
														<div class="elementor-gallery-item__description">Photo Credit: Janet Cramer, 2015</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Sacred-Grove-in-March-ken-mays.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-e7e5bb8" data-elementor-lightbox-title="Sacred Grove in March" data-elementor-lightbox-description="Joseph Smith said he experienced his First Vision in the morning of a spring day in 1820, so this image, taken in the Sacred Grove in March, may represent something closer to what the grove looked like at the time. (Photo Credit: Kenneth Mays, 2006)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Sacred-Grove-in-March-ken-mays-1024x692.jpg" data-width="525" data-height="355" alt="An image of the Sacred Grove in March. The trees have no leaves, as it is early spring." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Sacred Grove in March</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2006</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Sacred-Grove-Oct2019-26.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-e7e5bb8" data-elementor-lightbox-title="Sacred Grove" data-elementor-lightbox-description="Foliage and fallen leaves cover the ground in the Sacred Grove. (Photo Credit: Kenneth Mays, 2019)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Sacred-Grove-Oct2019-26-1024x683.jpg" data-width="525" data-height="350" alt="Fallen trees and dead leaves cover the ground of the grove. Live foliage and trees also stand in the grove" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Sacred Grove</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2019</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Sacred-Grove-Oct2019-07.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-e7e5bb8" data-elementor-lightbox-title="Sacred Grove" data-elementor-lightbox-description="A path winds through trees in the Sacred Grove. (Photo Credit: Kenneth Mays, 2019)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Sacred-Grove-Oct2019-07-1024x683.jpg" data-width="525" data-height="350" alt="A path winds around trees in the Sacred Grove. Some of the trees&#039; leaves are changing colors to yellow and red" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Sacred Grove</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2019</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Sacred-Grove-Jun06-03-ken-mays.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-e7e5bb8" data-elementor-lightbox-title="Sacred Grove in June" data-elementor-lightbox-description="A path runs through the Sacred Grove in June. (Photo Credit: Kenneth Mays, 2003)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Sacred-Grove-Jun06-03-ken-mays.jpg" data-width="525" data-height="381" alt="A path going through a grove of trees and green foliage." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Sacred Grove in June</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2003</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/eight-witnesses.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-e7e5bb8" data-elementor-lightbox-title="Eight Witnesses Plaque" data-elementor-lightbox-description="A plaque at the Sacred Grove details the story of the Eight Witnesses. The Eight Witnesses saw the golden plates on the Smith property here in Palmyra and Manchester in June 1829. (Photo Credit: John W. Welch, 2003)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/eight-witnesses-768x1024.jpg" data-width="525" data-height="700" alt="Eight Witness Plaque" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Eight Witnesses Plaque</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2003</div>
												</div>
									</a>
					</div>
			</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-07290a2 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="07290a2" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-e79bc34" data-id="e79bc34" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-995a00f elementor-widget elementor-widget-heading" data-id="995a00f" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Take a 360<strong style="margin: 0px; padding: 0px; color: rgb(51, 51, 51); font-family: sans-serif; font-size: 19.2px; text-align: start; white-space: normal;">°</strong> Tour of the Sacred Grove</h2>		</div>
				</div>
				<section class="has_eae_slider elementor-section elementor-inner-section elementor-element elementor-element-c6a3357 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="c6a3357" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-d3621f1" data-id="d3621f1" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
								</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-60bcc0e" data-id="60bcc0e" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-ab3d3a3 elementor-grid-1 eael-fg-hoverer-content-align-center elementor-grid-tablet-1 places-360-tour elementor-grid-mobile-1 elementor-widget elementor-widget-eael-filterable-gallery" data-id="ab3d3a3" data-element_type="widget" data-settings="{&quot;columns&quot;:&quot;1&quot;,&quot;columns_tablet&quot;:&quot;1&quot;,&quot;columns_mobile&quot;:&quot;1&quot;,&quot;photo_gallery&quot;:&quot;yes&quot;,&quot;pagination&quot;:&quot;false&quot;}" data-widget_type="eael-filterable-gallery.default">
				<div class="elementor-widget-container">
			        <div id="eael-filter-gallery-wrapper-ab3d3a3" class="eael-filter-gallery-wrapper" data-layout-mode="hoverer" data-mfp_caption="">


            <div class="eael-filter-gallery-container masonry" data-images-per-page="" data-total-gallery-items="1" data-nomore-item-text="" data-settings="{&quot;grid_style&quot;:&quot;masonry&quot;,&quot;popup&quot;:&quot;buttons&quot;,&quot;duration&quot;:500,&quot;gallery_enabled&quot;:&quot;yes&quot;,&quot;post_id&quot;:6942,&quot;widget_id&quot;:&quot;ab3d3a3&quot;}" data-gallery-items="[&quot;&lt;div class=\\&quot;eael-filterable-gallery-item-wrap\\&quot;&gt;\n\t\t\t\t&lt;div class=\\&quot;eael-gallery-grid-item\\&quot;&gt;&lt;div class=\\&quot;gallery-item-thumbnail-wrap\\&quot;&gt;&lt;img src=\\&quot;https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/uploads\\/2021\\/02\\/Sacred-Grove.png\\&quot; data-lazy-src=\\&quot;https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/uploads\\/2021\\/02\\/Sacred-Grove.png\\&quot; alt=\\&quot;Screenshot of the Google Maps 360 view of the Sacred Grove\\&quot; class=\\&quot;gallery-item-thumbnail\\&quot;&gt;&lt;\\/div&gt;&lt;div class=\\&quot;gallery-item-caption-wrap caption-style-hoverer eael-slide-up\\&quot;&gt;&lt;div class=\\&quot;gallery-item-hoverer-bg\\&quot;&gt;&lt;\\/div&gt;&lt;div class=\\&quot;gallery-item-caption-over\\&quot;&gt;&lt;h5 class=\\&quot;fg-item-title\\&quot;&gt;360 Tour of the Sacred Grove&lt;\\/h5&gt;&lt;div class=\\&quot;gallery-item-buttons\\&quot;&gt;&lt;a href=\\&quot;https:\\/\\/goo.gl\\/maps\\/ge2UzEwWWHApMPmZ7\\&quot;target=\\&quot;_blank\\&quot;&gt;&lt;span class=\\&quot;fg-item-icon-inner\\&quot;&gt;&lt;i class=\\&quot;fas fa-link\\&quot; aria-hidden=\\&quot;true\\&quot;&gt;&lt;\\/i&gt;&lt;\\/span&gt;&lt;\\/a&gt;&lt;\\/div&gt;&lt;\\/div&gt;&lt;\\/div&gt;&lt;\\/div&gt;&lt;\\/div&gt;&quot;]" data-init-show="1">
                <div class="eael-filterable-gallery-item-wrap">
				<div class="eael-gallery-grid-item"><div class="gallery-item-thumbnail-wrap"><img src="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Sacred-Grove.png" data-lazy-src="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Sacred-Grove.png" alt="Screenshot of the Google Maps 360 view of the Sacred Grove" class="gallery-item-thumbnail"></div><div class="gallery-item-caption-wrap caption-style-hoverer eael-slide-up"><div class="gallery-item-hoverer-bg"></div><div class="gallery-item-caption-over"><h5 class="fg-item-title">360 Tour of the Sacred Grove</h5><div class="gallery-item-buttons"><a href="https://goo.gl/maps/ge2UzEwWWHApMPmZ7"target="_blank"><span class="fg-item-icon-inner"><i class="fas fa-link" aria-hidden="true"></i></span></a></div></div></div></div></div>            </div>

                    </div>

        		</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-e69d285" data-id="e69d285" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
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
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-8839113 places-place-text elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="8839113" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-539a6ea" data-id="539a6ea" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-89c19fe elementor-widget elementor-widget-menu-anchor" data-id="89c19fe" data-element_type="widget" data-widget_type="menu-anchor.default">
				<div class="elementor-widget-container">
					<div id="2" class="elementor-menu-anchor"></div>
				</div>
				</div>
				<div class="elementor-element elementor-element-9b882a8 elementor-widget elementor-widget-heading" data-id="9b882a8" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Hill Cumorah</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-8aacfa0 elementor-widget elementor-widget-heading" data-id="8aacfa0" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Key Points of Interest</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-4383371 elementor-icon-list--layout-traditional elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list" data-id="4383371" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items">
							<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">Moroni, the final author in and compiler of The Book of Mormon, buried the golden plates in this hill sometime around 421 A.D.</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">On the night of 21 September 1823, Moroni, now a glorified, resurrected being, visited Joseph Smith, Jr. and told him about the plates</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">At Moroni's direction, Joseph went to the hill the next day (22 September 1823) and found the plates but was told he must wait to receive them</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">Joseph met Moroni here on September 22 every year from 1824-1827 and received instruction from him</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">On 22 September 1827, Joseph came to the hill with his wife, Emma, to retrieve the plates</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">The hill is about 117 feet tall, one of the tallest in the area</span>
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
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-af9dae7 places-pic-gallery elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="af9dae7" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-d6b36cd" data-id="d6b36cd" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-336f349 elementor-hidden-tablet elementor-hidden-phone elementor-widget elementor-widget-heading" data-id="336f349" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">(Hover over photo for more information, click to enlarge)</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-d229f30 elementor-hidden-desktop elementor-widget elementor-widget-heading" data-id="d229f30" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">(Tap photo to enlarge and see more information)​</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-4ec52b5 elementor-widget elementor-widget-gallery" data-id="4ec52b5" data-element_type="widget" data-settings="{&quot;overlay_title&quot;:&quot;title&quot;,&quot;overlay_description&quot;:&quot;caption&quot;,&quot;gallery_layout&quot;:&quot;justified&quot;,&quot;lazyload&quot;:&quot;yes&quot;,&quot;ideal_row_height&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:200,&quot;sizes&quot;:[]},&quot;ideal_row_height_tablet&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:150,&quot;sizes&quot;:[]},&quot;ideal_row_height_mobile&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:150,&quot;sizes&quot;:[]},&quot;gap&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;gap_tablet&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;gap_mobile&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;link_to&quot;:&quot;file&quot;,&quot;overlay_background&quot;:&quot;yes&quot;,&quot;content_hover_animation&quot;:&quot;fade-in&quot;}" data-widget_type="gallery.default">
				<div class="elementor-widget-container">
					<div class="elementor-gallery__container">
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-sunset-2002-ken-mays.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-4ec52b5" data-elementor-lightbox-title="Cumorah Sunset" data-elementor-lightbox-description="The sun sets at Hill Cumorah. (Photo Credit: Kenneth Mays, 2002)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-sunset-2002-ken-mays-1024x683.jpg" data-width="525" data-height="350" alt="A view from the top of the Hill Cumorah. The green grass on the hill slopes downward, and the sun sets over two clusters of trees and a grassy field." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Cumorah Sunset</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2002</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-May08-21.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-4ec52b5" data-elementor-lightbox-title="Hill Cumorah Pageant Site" data-elementor-lightbox-description="The Hill Cumorah Pageant was performed on this hillside at the Hill Cumorah. (Photo Credit: Kenneth Mays, 2008)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-May08-21-1024x680.jpg" data-width="525" data-height="349" alt="Green grass, flanked by two groves of trees, covers the site where the Hill Cumorah Pageant was held." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Hill Cumorah Pageant Site</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2008</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Hill-Cumorah-04.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-4ec52b5" data-elementor-lightbox-title="Hill Cumorah with Moroni Monument" data-elementor-lightbox-description="A monument of Moroni rises from Hill Cumorah. (Photo Credit: Kenneth Mays, 2008)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Hill-Cumorah-04-1024x705.jpg" data-width="525" data-height="361" alt="Green grass, flanked by two groves of trees, covers the part of the hill where the Hill Cumorah Pageant was held. Behind it is a stone monument topped by a gold statue of Moroni" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Hill Cumorah with Moroni Monument</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2008</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-monumental-statue-of-the-Angel-Moroni-who-appeared-often-to-Joseph-Smith.-John-W.-Welch-2003.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-4ec52b5" data-elementor-lightbox-title="Cumorah Monument of Angel Moroni" data-elementor-lightbox-description="A monument of Moroni rises from Hill Cumorah. (Photo Credit: John W. Welch, 2003)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-monumental-statue-of-the-Angel-Moroni-who-appeared-often-to-Joseph-Smith.-John-W.-Welch-2003-768x1024.jpg" data-width="525" data-height="700" alt="A granite monument with a gold statue of Moroni on top rises from a slope covered with green grass" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Cumorah Monument of Angel Moroni</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2003</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-granite-base-of-Moroni-statue.-John-W.-Welch-2012.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-4ec52b5" data-elementor-lightbox-title="Granite Base of Monument" data-elementor-lightbox-description="The base of the monument on Hill Cumorah is made of granite and topped by a golden statue of Moroni. (Photo Credit: John W. Welch, 2012)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-granite-base-of-Moroni-statue.-John-W.-Welch-2012-768x1024.jpg" data-width="525" data-height="700" alt="The granite monument at the Hill Cumorah is shown in front of a cloudy sky. The gold statue of Moroni sits on top." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Granite Base of Monument</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2012</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Moroni-statue-2009-ken-mays.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-4ec52b5" data-elementor-lightbox-title="Moroni Statue at Top of Monument" data-elementor-lightbox-description="The statue of Moroni on the monument at Hill Cumorah holds his right arm to the square and holds the golden plates in his left hand (Photo Credit: Kenneth Mays, 2009)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Moroni-statue-2009-ken-mays-651x1024.jpg" data-width="525" data-height="826" alt="The gold Moroni statue at the top of the granite monument at the Hill Cumorah. Moroni&#039;s right arm is raised to the square, and he holds the golden plates." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Moroni Statue at Top of Monument</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2009</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-bronze-relief-on-the-base-of-the-Moroni-statue-showing-Joseph-receiving-the-plates-of-the-Book-of-Mormon.-Christina-Broberg-2012-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-4ec52b5" data-elementor-lightbox-title="Bronze Relief at Base of Monument" data-elementor-lightbox-description="One of several bronze reliefs at the base of a monument on Hill Cumorah shows Joseph Smith, Jr. receiving the golden plates from Moroni. (Photo Credit: Christina Broberg 2012)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-bronze-relief-on-the-base-of-the-Moroni-statue-showing-Joseph-receiving-the-plates-of-the-Book-of-Mormon.-Christina-Broberg-2012-683x1024.jpg" data-width="525" data-height="787" alt="A bronze relief on the base of the granite monument shows Joseph receiving the plates from Moroni." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Bronze Relief at Base of Monument</div>
														<div class="elementor-gallery-item__description">Photo Credit: Christina Broberg 2012</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-wooded-western-hillside-in-the-area-where-Joseph-met-Moroni-each-September.-John-W.-Welch-2003.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-4ec52b5" data-elementor-lightbox-title="Wooded Western Hillside" data-elementor-lightbox-description="Trees and foliage occupy part of the Hill Cumorah. Moroni met Joseph Smith, Jr. on the hill on September 22 every year from 1823 to 1827. (Photo Credit: John W. Welch, 2003)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-wooded-western-hillside-in-the-area-where-Joseph-met-Moroni-each-September.-John-W.-Welch-2003-1024x768.jpg" data-width="525" data-height="394" alt="Trees with green leaves stand in an area on the hill with fallen brown leaves on the ground." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Wooded Western Hillside</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2003</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Hill-Cumorah-2009-ken-mays.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-4ec52b5" data-elementor-lightbox-title="A Stone on Hill Cumorah" data-elementor-lightbox-description="A large boulder sits on the hillside of Hill Cumorah. A stone like this one covered the stone box that contained the golden plates. (Photo Credit: Kenneth Mays, 2009)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Hill-Cumorah-2009-ken-mays-680x1024.jpg" data-width="525" data-height="791" alt="A large stone lies among dead, brown leaves in a cluster of trees without leaves." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">A Stone on Hill Cumorah</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2009</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-distance-2006-ken-mays-1.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-4ec52b5" data-elementor-lightbox-title="Hill Cumorah from a Distance" data-elementor-lightbox-description="Joseph Smith described the Hill Cumorah as &quot;a hill of considerable size, and the most elevated of any in the neighborhood.&quot; (Joseph Smith-History 1:51) (Photo Credit: Kenneth Mays, 2006)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-distance-2006-ken-mays-1-1024x819.jpg" data-width="525" data-height="420" alt="Hill Cumorah is seen behind dead brown grass and trees with brown leaves. The hill is still green with trees and grass." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Hill Cumorah from a Distance</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2006</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-Oct2019-14.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-4ec52b5" data-elementor-lightbox-title="Hill Cumorah Visitors Center" data-elementor-lightbox-description="The Hill Cumorah Visitor&#039;s Center sits on the west side of the hill. (Photo Credit: Kenneth Mays, 2019)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Cumorah-Oct2019-14-1024x683.jpg" data-width="525" data-height="350" alt="A black asphalt parking lot and, behind it, a white one-story building with white arbors in front of it" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Hill Cumorah Visitors Center</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2019</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/55-old-p-679_70-road_hill-cumorah.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-4ec52b5" data-elementor-lightbox-title="Hill Cumorah Old Photo" data-elementor-lightbox-description="This photo depicts the Hill Cumorah with very few trees. The hill has sometimes been bare and sometimes covered with trees. (Photo Credit: Church History Library)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/55-old-p-679_70-road_hill-cumorah.jpg" data-width="525" data-height="394" alt="A black-and-white photo of a Hill Cumorah with no trees" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Hill Cumorah Old Photo</div>
														<div class="elementor-gallery-item__description">Photo Credit: Church History Library</div>
												</div>
									</a>
					</div>
			</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-bedca27 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="bedca27" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-f87dc82" data-id="f87dc82" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-ac72f9d elementor-widget elementor-widget-heading" data-id="ac72f9d" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Take a 360<strong style="margin: 0px; padding: 0px; color: rgb(51, 51, 51); font-family: sans-serif; font-size: 19.2px; text-align: start; white-space: normal;">°</strong> Tour of the Hill Cumorah</h2>		</div>
				</div>
				<section class="has_eae_slider elementor-section elementor-inner-section elementor-element elementor-element-a74c83e elementor-section-height-min-height elementor-section-boxed elementor-section-height-default" data-id="a74c83e" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-2097a65" data-id="2097a65" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
								</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-b249866" data-id="b249866" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-476dbfa elementor-grid-1 eael-fg-hoverer-content-align-center elementor-grid-tablet-1 elementor-grid-mobile-1 elementor-widget elementor-widget-eael-filterable-gallery" data-id="476dbfa" data-element_type="widget" data-settings="{&quot;columns&quot;:&quot;1&quot;,&quot;columns_tablet&quot;:&quot;1&quot;,&quot;columns_mobile&quot;:&quot;1&quot;,&quot;photo_gallery&quot;:&quot;yes&quot;,&quot;pagination&quot;:&quot;false&quot;}" data-widget_type="eael-filterable-gallery.default">
				<div class="elementor-widget-container">
			        <div id="eael-filter-gallery-wrapper-476dbfa" class="eael-filter-gallery-wrapper" data-layout-mode="hoverer" data-mfp_caption="">


            <div class="eael-filter-gallery-container masonry" data-images-per-page="" data-total-gallery-items="1" data-nomore-item-text="" data-settings="{&quot;grid_style&quot;:&quot;masonry&quot;,&quot;popup&quot;:&quot;buttons&quot;,&quot;duration&quot;:500,&quot;gallery_enabled&quot;:&quot;yes&quot;,&quot;post_id&quot;:6942,&quot;widget_id&quot;:&quot;476dbfa&quot;}" data-gallery-items="[&quot;&lt;div class=\\&quot;eael-filterable-gallery-item-wrap\\&quot;&gt;\n\t\t\t\t&lt;div class=\\&quot;eael-gallery-grid-item\\&quot;&gt;&lt;div class=\\&quot;gallery-item-thumbnail-wrap\\&quot;&gt;&lt;img src=\\&quot;https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/uploads\\/2021\\/02\\/Hill-Cumorah.png\\&quot; data-lazy-src=\\&quot;https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/uploads\\/2021\\/02\\/Hill-Cumorah.png\\&quot; alt=\\&quot;Screenshot of the Google Maps 360 view of the Hill Cumorah\\&quot; class=\\&quot;gallery-item-thumbnail\\&quot;&gt;&lt;\\/div&gt;&lt;div class=\\&quot;gallery-item-caption-wrap caption-style-hoverer eael-slide-up\\&quot;&gt;&lt;div class=\\&quot;gallery-item-hoverer-bg\\&quot;&gt;&lt;\\/div&gt;&lt;div class=\\&quot;gallery-item-caption-over\\&quot;&gt;&lt;h5 class=\\&quot;fg-item-title\\&quot;&gt;360 Tour of Hill Cumorah&lt;\\/h5&gt;&lt;div class=\\&quot;gallery-item-buttons\\&quot;&gt;&lt;a href=\\&quot;https:\\/\\/goo.gl\\/maps\\/KD64CszotaC7eTqDA\\&quot;target=\\&quot;_blank\\&quot;&gt;&lt;span class=\\&quot;fg-item-icon-inner\\&quot;&gt;&lt;i class=\\&quot;fas fa-link\\&quot; aria-hidden=\\&quot;true\\&quot;&gt;&lt;\\/i&gt;&lt;\\/span&gt;&lt;\\/a&gt;&lt;\\/div&gt;&lt;\\/div&gt;&lt;\\/div&gt;&lt;\\/div&gt;&lt;\\/div&gt;&quot;]" data-init-show="1">
                <div class="eael-filterable-gallery-item-wrap">
				<div class="eael-gallery-grid-item"><div class="gallery-item-thumbnail-wrap"><img src="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Hill-Cumorah.png" data-lazy-src="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Hill-Cumorah.png" alt="Screenshot of the Google Maps 360 view of the Hill Cumorah" class="gallery-item-thumbnail"></div><div class="gallery-item-caption-wrap caption-style-hoverer eael-slide-up"><div class="gallery-item-hoverer-bg"></div><div class="gallery-item-caption-over"><h5 class="fg-item-title">360 Tour of Hill Cumorah</h5><div class="gallery-item-buttons"><a href="https://goo.gl/maps/KD64CszotaC7eTqDA"target="_blank"><span class="fg-item-icon-inner"><i class="fas fa-link" aria-hidden="true"></i></span></a></div></div></div></div></div>            </div>

                    </div>

        		</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-acb252b" data-id="acb252b" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
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
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-9db92c7 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="9db92c7" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-39d37de" data-id="39d37de" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-9c80de5 elementor-widget elementor-widget-menu-anchor" data-id="9c80de5" data-element_type="widget" data-widget_type="menu-anchor.default">
				<div class="elementor-widget-container">
					<div id="3" class="elementor-menu-anchor"></div>
				</div>
				</div>
				<div class="elementor-element elementor-element-76ccada elementor-widget elementor-widget-heading" data-id="76ccada" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Smith Log Home</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-b122752 elementor-widget elementor-widget-heading" data-id="b122752" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Key Points of Interest</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-1dba52a elementor-icon-list--layout-traditional elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list" data-id="1dba52a" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items">
							<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">Joseph Smith, Sr. and Lucy Mack Smith and their children lived in a log home built on this site</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">The Smith family was living here when Joseph Smith, Jr. experienced his First Vision in the Sacred Grove nearby</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">The angel Moroni first appeared to Joseph Smith, Jr. here on the evening of 21 September 1823</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">Joseph's younger sister Lucy was born here in 1821; Joseph's oldest brother, Alvin, passed away here; and Oliver Cowdery finished the printer's manuscript of The Book of Mormon here</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">After their marriage Hyrum Smith and his wife, Jerusha, lived in this home</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">The Smiths left the home in 1835, and the original home collapsed sometime later; a 1982 archaeological dig revealed the foundation and details about the home's construction</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">The reconstructed log home was built in 1997-1998 on the exact site of the original home, and workers used hand tools to give it an authentic look and feel</span>
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
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-2e706c7 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="2e706c7" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-92b6f6d" data-id="92b6f6d" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-e3344cb elementor-hidden-tablet elementor-hidden-phone elementor-widget elementor-widget-heading" data-id="e3344cb" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">(Hover over photo for more information, click to enlarge)</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-f465efd elementor-hidden-desktop elementor-widget elementor-widget-heading" data-id="f465efd" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">(Tap photo to enlarge and see more information)​</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-d2f9074 elementor-widget elementor-widget-gallery" data-id="d2f9074" data-element_type="widget" data-settings="{&quot;overlay_title&quot;:&quot;title&quot;,&quot;overlay_description&quot;:&quot;caption&quot;,&quot;gallery_layout&quot;:&quot;justified&quot;,&quot;lazyload&quot;:&quot;yes&quot;,&quot;ideal_row_height&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:200,&quot;sizes&quot;:[]},&quot;ideal_row_height_tablet&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:150,&quot;sizes&quot;:[]},&quot;ideal_row_height_mobile&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:150,&quot;sizes&quot;:[]},&quot;gap&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;gap_tablet&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;gap_mobile&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;link_to&quot;:&quot;file&quot;,&quot;overlay_background&quot;:&quot;yes&quot;,&quot;content_hover_animation&quot;:&quot;fade-in&quot;}" data-widget_type="gallery.default">
				<div class="elementor-widget-container">
					<div class="elementor-gallery__container">
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-log-home-2009-31.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-d2f9074" data-elementor-lightbox-title="Front of Rebuilt Smith Log Home" data-elementor-lightbox-description="The reconstructed Smith Log Home was built using hand tools, as the original would have been. (Photo Credit: Kenneth Mays, 2009)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-log-home-2009-31-1024x778.jpg" data-width="525" data-height="399" alt="The front of the Smith Log Home. It&#039;s a small home, with a front door with dings on either side, a shingled roof and a chimney." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Front of Rebuilt Smith Log Home</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2009</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-Smith-Log-House-the-Smith_s-lived-on-this-site-from-1818-1825.-Nearby-is-the-Sacred-Grove.-John-W.-Welch-2003-e1612635817862.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-d2f9074" data-elementor-lightbox-title="Rebuilt Smith Log Home Looking South" data-elementor-lightbox-description="After moving into the log home, the Smiths lived there until 1825. The home is not far from the Sacred Grove, where Joseph Smith, Jr. experienced his first vision. (Photo Credit: John W. Welch, 2003)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-Smith-Log-House-the-Smith_s-lived-on-this-site-from-1818-1825.-Nearby-is-the-Sacred-Grove.-John-W.-Welch-2003-1024x768.jpg" data-width="525" data-height="394" alt="A brown-gray log cabin with a pile of wood next to it." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Rebuilt Smith Log Home Looking South</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2003</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-log-home-2017-06.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-d2f9074" data-elementor-lightbox-title="Rebuilt Smith Log Home Rear" data-elementor-lightbox-description="A rear view of of the log home shows a room that was added on after the home&#039;s initial construction. (Photo Credit: Kenneth Mays, 2017)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-log-home-2017-06-1024x683.jpg" data-width="525" data-height="350" alt="The rear of the log home. Stairs descend from a porch next to an added-on room." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Rebuilt Smith Log Home Rear</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2017</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-Log-home-fireplace.-John-W.-Welch-2003.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-d2f9074" data-elementor-lightbox-title="Rebuilt Smith Log Home Fireplace" data-elementor-lightbox-description="A fireplace provided warmth and a place to cook in the log home. (Photo Credit: John W. Welch, 2003)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-Log-home-fireplace.-John-W.-Welch-2003-1024x768.jpg" data-width="525" data-height="394" alt="A fireplace with various cooking implements." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Rebuilt Smith Log Home Fireplace</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2003</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-Log-House-ground-level-bedroom.-John-W.-Welch-2003.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-d2f9074" data-elementor-lightbox-title="Rebuilt Smith Log Home Ground-level Bedroom" data-elementor-lightbox-description="A bed sits in a corner of the ground-level bedroom at the Smith Log Home. (Photo Credit: John W. Welch, 2003)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-Log-House-ground-level-bedroom.-John-W.-Welch-2003-1024x768.jpg" data-width="525" data-height="394" alt="A bed sits in one corner of the log home." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Rebuilt Smith Log Home Ground-level Bedroom</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2003</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-log-home-int-2008-ken-mays.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-d2f9074" data-elementor-lightbox-title="Rebuilt Smith Log Home Upstairs Bedrooms" data-elementor-lightbox-description="The area upstairs was divided into two rooms: the larger one near the stairs for the boys and the smaller one for the girls. It was here that Joseph Smith, Jr. was visited by Moroni. (Photo Credit: Kenneth Mays, 2008)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-log-home-int-2008-ken-mays-1024x683.jpg" data-width="525" data-height="350" alt="Two rooms divided by a wall make up an upstairs area directly beneath the log home&#039;s roof. Two beds sit in one room." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Rebuilt Smith Log Home Upstairs Bedrooms</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2008</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-Log-home-King-James-Bible-open-to-James-chapter-1-verse-5-which-passage-inspired-Joseph-Smith-to-seek-an-answer-directly-from-God.-Christina-Broberg-2012-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-d2f9074" data-elementor-lightbox-title="King James Bible at Rebuilt Smith Log Home" data-elementor-lightbox-description="A Bible at the Smith Log Home sits open to James chapter 1. James 1:5 inspired Joseph Smith, Jr. to pray to God for answers about which church he should join. (Photo Credit: Christina Broberg, 2012)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-Log-home-King-James-Bible-open-to-James-chapter-1-verse-5-which-passage-inspired-Joseph-Smith-to-seek-an-answer-directly-from-God.-Christina-Broberg-2012-1024x683.jpg" data-width="525" data-height="350" alt="An old King James Bible sits open to James Chapter 1." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">King James Bible at Rebuilt Smith Log Home</div>
														<div class="elementor-gallery-item__description">Photo Credit: Christina Broberg, 2012</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-log-fence.-Christina-Broberg-2012-1-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-d2f9074" data-elementor-lightbox-title="Fence and Rebuilt Smith Log Home" data-elementor-lightbox-description="The Smith Log Home is one of two homes that the Smiths built on the property. (Photo Credit: Christina Broberg, 2012)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-log-fence.-Christina-Broberg-2012-1-1024x683.jpg" data-width="525" data-height="350" alt="A brown-gray log cabin from across a fenced field." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Fence and Rebuilt Smith Log Home</div>
														<div class="elementor-gallery-item__description">Photo Credit: Christina Broberg, 2012</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-Log-Home-fenced-field.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-d2f9074" data-elementor-lightbox-title="Fence on Smith Farm Property in Palmyra" data-elementor-lightbox-description="A fenced field near the Smith Log Home. The Smith family lived on a 100-acre plot. (Photo Credit: John W. Welch, 2003)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-Log-Home-fenced-field-1024x768.jpg" data-width="525" data-height="394" alt="An fence made of logs surrounding a field." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Fence on Smith Farm Property in Palmyra</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2003</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-farm-Oct2019-26.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-d2f9074" data-elementor-lightbox-title="Smith Farm" data-elementor-lightbox-description="The Smith family farmed about 60 acres of their 100-acre plot, using the remaining 40 as a wood lot. (Photo Credit: Kenneth Mays, 2019)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-farm-Oct2019-26-1024x683.jpg" data-width="525" data-height="350" alt="Several fruit trees sit behind fences on the Smith Farm Property" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Smith Farm</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2019</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-creek-running-through-the-Smith-property-where-they-settled-in-1818.-John-W.-Welch-2003-1.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-d2f9074" data-elementor-lightbox-title="Creek on Smith Farm Property in Palmyra" data-elementor-lightbox-description="A creek runs through the Smith property. (Photo Credit: John W. Welch, 2003)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-creek-running-through-the-Smith-property-where-they-settled-in-1818.-John-W.-Welch-2003-1-768x1024.jpg" data-width="525" data-height="700" alt="A creek runs past some green grass and trees on either side." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Creek on Smith Farm Property in Palmyra</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2003</div>
												</div>
									</a>
					</div>
			</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-6791428 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="6791428" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-25724ee" data-id="25724ee" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-24c0a8c elementor-widget elementor-widget-heading" data-id="24c0a8c" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Take a 360<strong style="margin: 0px; padding: 0px; color: rgb(51, 51, 51); font-family: sans-serif; font-size: 19.2px; text-align: start; white-space: normal;">°</strong> Tour of the Smith Log Home</h2>		</div>
				</div>
				<section class="has_eae_slider elementor-section elementor-inner-section elementor-element elementor-element-add9135 elementor-section-height-min-height elementor-section-boxed elementor-section-height-default" data-id="add9135" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-7e4e61e" data-id="7e4e61e" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
								</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-8922a4b" data-id="8922a4b" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-a4ffb8a elementor-grid-1 eael-fg-hoverer-content-align-center elementor-grid-tablet-1 elementor-grid-mobile-1 elementor-widget elementor-widget-eael-filterable-gallery" data-id="a4ffb8a" data-element_type="widget" data-settings="{&quot;columns&quot;:&quot;1&quot;,&quot;columns_tablet&quot;:&quot;1&quot;,&quot;columns_mobile&quot;:&quot;1&quot;,&quot;photo_gallery&quot;:&quot;yes&quot;,&quot;pagination&quot;:&quot;false&quot;}" data-widget_type="eael-filterable-gallery.default">
				<div class="elementor-widget-container">
			        <div id="eael-filter-gallery-wrapper-a4ffb8a" class="eael-filter-gallery-wrapper" data-layout-mode="hoverer" data-mfp_caption="">


            <div class="eael-filter-gallery-container masonry" data-images-per-page="" data-total-gallery-items="1" data-nomore-item-text="" data-settings="{&quot;grid_style&quot;:&quot;masonry&quot;,&quot;popup&quot;:&quot;buttons&quot;,&quot;duration&quot;:500,&quot;gallery_enabled&quot;:&quot;yes&quot;,&quot;post_id&quot;:6942,&quot;widget_id&quot;:&quot;a4ffb8a&quot;}" data-gallery-items="[&quot;&lt;div class=\\&quot;eael-filterable-gallery-item-wrap\\&quot;&gt;\n\t\t\t\t&lt;div class=\\&quot;eael-gallery-grid-item\\&quot;&gt;&lt;div class=\\&quot;gallery-item-thumbnail-wrap\\&quot;&gt;&lt;img src=\\&quot;https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/uploads\\/2021\\/02\\/Smith-Log-Home-1.png\\&quot; data-lazy-src=\\&quot;https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/uploads\\/2021\\/02\\/Smith-Log-Home-1.png\\&quot; alt=\\&quot;Screenshot of the Google Maps 360 view of the Smith Log Home\\&quot; class=\\&quot;gallery-item-thumbnail\\&quot;&gt;&lt;\\/div&gt;&lt;div class=\\&quot;gallery-item-caption-wrap caption-style-hoverer eael-slide-up\\&quot;&gt;&lt;div class=\\&quot;gallery-item-hoverer-bg\\&quot;&gt;&lt;\\/div&gt;&lt;div class=\\&quot;gallery-item-caption-over\\&quot;&gt;&lt;h5 class=\\&quot;fg-item-title\\&quot;&gt;360 Tour of Smith Log Home&lt;\\/h5&gt;&lt;div class=\\&quot;gallery-item-buttons\\&quot;&gt;&lt;a href=\\&quot;https:\\/\\/goo.gl\\/maps\\/arh6896qjhumjopm7\\&quot;target=\\&quot;_blank\\&quot;&gt;&lt;span class=\\&quot;fg-item-icon-inner\\&quot;&gt;&lt;i class=\\&quot;fas fa-link\\&quot; aria-hidden=\\&quot;true\\&quot;&gt;&lt;\\/i&gt;&lt;\\/span&gt;&lt;\\/a&gt;&lt;\\/div&gt;&lt;\\/div&gt;&lt;\\/div&gt;&lt;\\/div&gt;&lt;\\/div&gt;&quot;]" data-init-show="1">
                <div class="eael-filterable-gallery-item-wrap">
				<div class="eael-gallery-grid-item"><div class="gallery-item-thumbnail-wrap"><img src="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-Log-Home-1.png" data-lazy-src="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-Log-Home-1.png" alt="Screenshot of the Google Maps 360 view of the Smith Log Home" class="gallery-item-thumbnail"></div><div class="gallery-item-caption-wrap caption-style-hoverer eael-slide-up"><div class="gallery-item-hoverer-bg"></div><div class="gallery-item-caption-over"><h5 class="fg-item-title">360 Tour of Smith Log Home</h5><div class="gallery-item-buttons"><a href="https://goo.gl/maps/arh6896qjhumjopm7"target="_blank"><span class="fg-item-icon-inner"><i class="fas fa-link" aria-hidden="true"></i></span></a></div></div></div></div></div>            </div>

                    </div>

        		</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-ac56710" data-id="ac56710" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
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
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-5092f5d elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="5092f5d" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-a4de49b" data-id="a4de49b" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-e802e5f elementor-widget elementor-widget-menu-anchor" data-id="e802e5f" data-element_type="widget" data-widget_type="menu-anchor.default">
				<div class="elementor-widget-container">
					<div id="4" class="elementor-menu-anchor"></div>
				</div>
				</div>
				<div class="elementor-element elementor-element-6bc1333 elementor-widget elementor-widget-heading" data-id="6bc1333" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">E. B. Grandin Press</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-332579c elementor-widget elementor-widget-heading" data-id="332579c" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Key Points of Interest</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-ef4bea4 elementor-icon-list--layout-traditional elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list" data-id="ef4bea4" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items">
							<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">This is where the first editions of The Book of Mormon were published—the first run was 5,000 copies and cost $3,000 to produce, $0.60 per copy</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">Joseph purchased the King James Bible he used for the Joseph Smith Translation of the Bible here for $3.75</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">E. B. Grandin only published two books in his career: one was The Book of Mormon, and the other was a math textbook by Tobias Ostrander</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">The Book of Mormon was printed on a Smith Acorn Press (no relation to Joseph Smith or the Smith family), which is now housed in the Church History Museum and has been replaced by a replica</span>
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
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-5848c04 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="5848c04" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-e4a9660" data-id="e4a9660" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-232e573 elementor-hidden-tablet elementor-hidden-phone elementor-widget elementor-widget-heading" data-id="232e573" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">(Hover over photo for more information, click to enlarge)</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-f892b6e elementor-hidden-desktop elementor-widget elementor-widget-heading" data-id="f892b6e" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">(Tap photo to enlarge and see more information)​</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-9f84c8b elementor-widget elementor-widget-gallery" data-id="9f84c8b" data-element_type="widget" data-settings="{&quot;overlay_title&quot;:&quot;title&quot;,&quot;overlay_description&quot;:&quot;caption&quot;,&quot;gallery_layout&quot;:&quot;justified&quot;,&quot;lazyload&quot;:&quot;yes&quot;,&quot;ideal_row_height&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:200,&quot;sizes&quot;:[]},&quot;ideal_row_height_tablet&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:150,&quot;sizes&quot;:[]},&quot;ideal_row_height_mobile&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:150,&quot;sizes&quot;:[]},&quot;gap&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;gap_tablet&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;gap_mobile&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;link_to&quot;:&quot;file&quot;,&quot;overlay_background&quot;:&quot;yes&quot;,&quot;content_hover_animation&quot;:&quot;fade-in&quot;}" data-widget_type="gallery.default">
				<div class="elementor-widget-container">
					<div class="elementor-gallery__container">
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Main-St-2009-ken-mays.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Press Storefront" data-elementor-lightbox-description="The front of the E. B. Grandin building. Grandin&#039;s business was housed in the west half of the brick building, on the left. (Photo Credit: Kenneth Mays, 2009)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Main-St-2009-ken-mays-1024x614.jpg" data-width="525" data-height="315" alt="A red brick building, the E.B. Grandin Press, sits snug between several other buildings on Palmyra&#039;s Main Street." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Press Storefront</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2009</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-bldg-01.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Press Storefront from Right" data-elementor-lightbox-description="The front of the E. B. Grandin building. Grandin&#039;s business was housed in the west half of the brick building, on the left. (Photo Credit: Kenneth Mays, 2006)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-bldg-01-1024x734.jpg" data-width="525" data-height="376" alt="A red brick building with several large windows and a sign that says, &quot;Book of Mormon Historic Publication Site&quot;" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Press Storefront from Right</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2006</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-heater-and-typesetting-desk-near-the-window-for-good-light-in-the-proofreading-process.-John-W.-Welch-2003.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Press Typesetting Desk" data-elementor-lightbox-description="The work of printing The Book of Mormon began with setting type. A typesetting desk near the window offered a place to set the type in order. (Photo Credit: Jack Welch, 2003)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-heater-and-typesetting-desk-near-the-window-for-good-light-in-the-proofreading-process.-John-W.-Welch-2003-768x1024.jpg" data-width="525" data-height="700" alt="A typesetting desk and heater sit near a window." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Press Typesetting Desk</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2003</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-type-boxes-filled-with-individual-letters-of-movable-type.-Christina-Broberg-2012-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Press Type Boxes" data-elementor-lightbox-description="Type boxes in the building house individual letters of metal type, which were arranged into words and sentences for printing. Capital letters were kept in the upper case, and the other letters were kept in the lower case, hence the terms &quot;uppercase&quot; and &quot;lowercase.&quot; (Photo Credit: Christina Broberg, 2012)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-type-boxes-filled-with-individual-letters-of-movable-type.-Christina-Broberg-2012-1024x683.jpg" data-width="525" data-height="350" alt="Boxes holding metal casts of letters, or type, sit near an area where type was set." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Press Type Boxes</div>
														<div class="elementor-gallery-item__description">Photo Credit: Christina Broberg, 2012</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-small-letter-press.-Christina-Broberg-2012-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Small Letter Press" data-elementor-lightbox-description="Once type for all pages was set and put into the iron chase, the large, heavy construction containing the type, was laid on the press bed. The press used to print The Book of Mormon was designed by Peter Smith and is sometimes called an &quot;acorn&quot; press because of its acorn shape. (Photo Credit: Christina Broberg, 2012)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-small-letter-press.-Christina-Broberg-2012-1024x683.jpg" data-width="525" data-height="350" alt="A black printing press" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Small Letter Press</div>
														<div class="elementor-gallery-item__description">Photo Credit: Christina Broberg, 2012</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-small-letter-press.-Janet-Cramer-2018-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Small Letter Press" data-elementor-lightbox-description="The Grandin Building houses a replica of the Smith press used to print The Book of Mormon. The original press now resides in the Church History Museum in Salt Lake City. (Photo Credit: Janet Cramer, 2018)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-small-letter-press.-Janet-Cramer-2018-1024x759.jpg" data-width="525" data-height="389" alt="A black printing press" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Small Letter Press</div>
														<div class="elementor-gallery-item__description">Photo Credit: Janet Cramer, 2018</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-ink-daubers-to-coat-the-type-with-just-the-right-amount-of-ink.-Janet-Cramer-2018-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Press Ink Daubers" data-elementor-lightbox-description="Ink daubers were used to coat the metal type with just the right amount of ink for printing. The ink was a thicker consistency and would be spread on a table, where a worker would pick it up with the ink daubers. (Photo Credit: Janet Cramer, 2018)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-ink-daubers-to-coat-the-type-with-just-the-right-amount-of-ink.-Janet-Cramer-2018-1024x810.jpg" data-width="525" data-height="415" alt="Two ink daubers sit on a table." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Press Ink Daubers</div>
														<div class="elementor-gallery-item__description">Photo Credit: Janet Cramer, 2018</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-laying-out-large-uncut-sheets-one-at-a-time-as-they-came-off-the-press.-Janet-Cramer-2018-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Press Printing Area" data-elementor-lightbox-description="On the left is a replica of the press on which The Book of Mormon was printed. On the right is the press on which Grandin printed a newspaper, the Wayne Sentinel. (Photo Credit: Janet Cramer, 2018)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-laying-out-large-uncut-sheets-one-at-a-time-as-they-came-off-the-press.-Janet-Cramer-2018-1024x768.jpg" data-width="525" data-height="394" alt="The printing area of the E. B. Grandin press, with printed pages, the press, and other equipment." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Press Printing Area</div>
														<div class="elementor-gallery-item__description">Photo Credit: Janet Cramer, 2018</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-printing-area.-Christina-Broberg-2012-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Press with Printed Sheets" data-elementor-lightbox-description="Sheets of printed paper hang from posts in the printing office. About twelve young men would work in this printing area, 12 hours a day, 6 days a week. (Photo Credit: Christina Broberg, 2012)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-printing-area.-Christina-Broberg-2012-1024x683.jpg" data-width="525" data-height="350" alt="Several presses occupy a room, with sheets hanging from the ceiling." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Press with Printed Sheets</div>
														<div class="elementor-gallery-item__description">Photo Credit: Christina Broberg, 2012</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-hanging-up-printed-pages-to-dry.-Christina-Broberg-2012-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Press Printed Sheets" data-elementor-lightbox-description="After being printed, sheets of paper would be hung up so that the ink could dry. Later these pages were cut in half and folded into little pamphlets called &quot;signatures.&quot; (Photo Credit: Christina Broberg, 2012)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-hanging-up-printed-pages-to-dry.-Christina-Broberg-2012-1024x683.jpg" data-width="525" data-height="350" alt="Several large sheets of paper with printed words hang on a rod to dry." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Press Printed Sheets</div>
														<div class="elementor-gallery-item__description">Photo Credit: Christina Broberg, 2012</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Bookstore-equipment-for-binding-books.-John-W.-Welch-2003.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Press Binding Equipment" data-elementor-lightbox-description="From right to left, the equipment pictured was used to press signatures—or pages—together so they would be more compact, clamp the signatures so the edges could be cut with a saw to prepare them for sewing, and to sew the signatures together.(Photo Credit: John W. Welch, 2003)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Bookstore-equipment-for-binding-books.-John-W.-Welch-2003-1024x768.jpg" data-width="525" data-height="394" alt="Equipment for binding books sits in a press building." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Press Binding Equipment</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2003</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Bookstore-tools-and-materials-for-stitching-signatures-together-in-the-binding-process.-Christina-Broberg-2012-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Press Stitching Tools" data-elementor-lightbox-description="These tools were used to stitch the signatures together. After signatures were stitched together their stitched edge would be covered with glue to further secure them together. (Photo Credit: Christina Broberg, 2012)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Bookstore-tools-and-materials-for-stitching-signatures-together-in-the-binding-process.-Christina-Broberg-2012-1024x683.jpg" data-width="525" data-height="350" alt="Tools, string and pages of paper sit on a table" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Press Stitching Tools</div>
														<div class="elementor-gallery-item__description">Photo Credit: Christina Broberg, 2012</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Bookstore-equpiment-for-gluing-books-in-the-binding-process.-Christina-Broberg-2012-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Press Gluing Equipment" data-elementor-lightbox-description="After the signatures were glued together and surrounded with a cover, they were taken here so the title could be stamped on the spine. Dies were heated and used to stamp the title, and then special cutting tools were used to decorate the book&#039;s spine. (Photo Credit: Christina Broberg, 2012)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Bookstore-equpiment-for-gluing-books-in-the-binding-process.-Christina-Broberg-2012-683x1024.jpg" data-width="525" data-height="787" alt="Equipment for gluing books in the binding process hangs on a wall." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Press Gluing Equipment</div>
														<div class="elementor-gallery-item__description">Photo Credit: Christina Broberg, 2012</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Bookstore.-Books-on-sale-many-unbound-and-to-be-individually-bound-as-on-March-27-1830-when-the-Book-of-Mormon-first-went-on-sale.-John-W.-Welch-2003-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Press Bookshelves" data-elementor-lightbox-description="Bookshelves sit full of books at the Grandin Building. Some books were sold without covers, but Joseph wanted The Book of Mormon to be published with a cover. As it was scripture, he wanted it to resemble a Bible. (Photo Credit: John W. Welch, 2003)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Bookstore.-Books-on-sale-many-unbound-and-to-be-individually-bound-as-on-March-27-1830-when-the-Book-of-Mormon-first-went-on-sale.-John-W.-Welch-2003-1024x683.jpg" data-width="525" data-height="350" alt="Books sit on several shelves on a wall." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Press Bookshelves</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2003</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Bookstore-books-for-sale-including-replicas-of-the-Bible-and-Book-of-Mormon.-Christina-Broberg-2012-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Press Bookshelf" data-elementor-lightbox-description="Replicas of the Bible and The Book of Mormon sit on shelves in the Grandin Building. (Photo Credit: Christina Broberg, 2012)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Bookstore-books-for-sale-including-replicas-of-the-Bible-and-Book-of-Mormon.-Christina-Broberg-2012-683x1024.jpg" data-width="525" data-height="787" alt="Books sit on several shelves on a wall." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Press Bookshelf</div>
														<div class="elementor-gallery-item__description">Photo Credit: Christina Broberg, 2012</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-used-by-Abner-Cole-to-print-The-Reflector-copying-some-of-1-Nephi-in-January-1830-in-violation-of-the-copyright-secured-by-Joseph-Smith.-Christina-Broberg-2012-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="Copy of Abner Cole&#039;s &quot;Reflector&quot;" data-elementor-lightbox-description="A man named Abner Cole published a newspaper called &quot;The Reflector&quot; from the Grandin Building while The Book of Mormon was being printed. At one point he printed sections of The Book of Mormon in &quot;The Reflector&quot; and mocked it, but was eventually convinced by Joseph to stop. (Photo Credit: Christina Broberg, 2012)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Press-used-by-Abner-Cole-to-print-The-Reflector-copying-some-of-1-Nephi-in-January-1830-in-violation-of-the-copyright-secured-by-Joseph-Smith.-Christina-Broberg-2012-1024x683.jpg" data-width="525" data-height="350" alt="A copy of Abner Cole&#039;s paper, &quot;The Reflector&quot;" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Copy of Abner Cole's "Reflector"</div>
														<div class="elementor-gallery-item__description">Photo Credit: Christina Broberg, 2012</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Building-law-office-where-Jospeh-Smith-and-Martin-Harris-negotiated-with-John-Grandin-for-the-printing-of-5000-copies-of-the-Book-of-Mormon.-John-W.-Welch-2003.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="E. B. Grandin Press Office" data-elementor-lightbox-description="The Grandin Building also contained a law office, which was leased by Thomas P. Baldwin at the time of the printing of The Book of Mormon. (Photo Credit: John W. Welch, 2003)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Building-law-office-where-Jospeh-Smith-and-Martin-Harris-negotiated-with-John-Grandin-for-the-printing-of-5000-copies-of-the-Book-of-Mormon.-John-W.-Welch-2003-768x1024.jpg" data-width="525" data-height="700" alt="Several chairs and tables sit in an office" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">E. B. Grandin Press Office</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2003</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-pub-math-book-04.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-9f84c8b" data-elementor-lightbox-title="Tobias Ostrander Math Book" data-elementor-lightbox-description="E. B. Grandin only published two books in his lifetime. One was The Book of Mormon, and the other was a math textbook by Tobias Ostrander. This is the title page of the textbook he published. (Photo Credit: Kenneth Mays, 2001)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-pub-math-book-04.jpg" data-width="525" data-height="656" alt="The title page of a book that reads, &quot;The Mathematical Expositor; containing Rules, Theorems, Lemmae, and Explanations of Various Parts of the Mathematical Science,&quot; etc. The bottom of the page indicates that the book was published by E. B. Grandin in 1832" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Tobias Ostrander Math Book</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2001</div>
												</div>
									</a>
					</div>
			</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-82a453f elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="82a453f" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-491f487" data-id="491f487" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-554b853 elementor-widget elementor-widget-heading" data-id="554b853" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Take a 360<strong style="margin: 0px; padding: 0px; color: rgb(51, 51, 51); font-family: sans-serif; font-size: 19.2px; text-align: start; white-space: normal;">°</strong> Tour of the Grandin Building</h2>		</div>
				</div>
				<section class="has_eae_slider elementor-section elementor-inner-section elementor-element elementor-element-bc53793 elementor-section-height-min-height elementor-section-boxed elementor-section-height-default" data-id="bc53793" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-cf0747a" data-id="cf0747a" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
								</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-4db40b1" data-id="4db40b1" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-01c17c7 elementor-grid-1 eael-fg-hoverer-content-align-center elementor-grid-tablet-1 elementor-grid-mobile-1 elementor-widget elementor-widget-eael-filterable-gallery" data-id="01c17c7" data-element_type="widget" data-settings="{&quot;columns&quot;:&quot;1&quot;,&quot;columns_tablet&quot;:&quot;1&quot;,&quot;columns_mobile&quot;:&quot;1&quot;,&quot;photo_gallery&quot;:&quot;yes&quot;,&quot;pagination&quot;:&quot;false&quot;}" data-widget_type="eael-filterable-gallery.default">
				<div class="elementor-widget-container">
			        <div id="eael-filter-gallery-wrapper-01c17c7" class="eael-filter-gallery-wrapper" data-layout-mode="hoverer" data-mfp_caption="">


            <div class="eael-filter-gallery-container masonry" data-images-per-page="" data-total-gallery-items="1" data-nomore-item-text="" data-settings="{&quot;grid_style&quot;:&quot;masonry&quot;,&quot;popup&quot;:&quot;buttons&quot;,&quot;duration&quot;:500,&quot;gallery_enabled&quot;:&quot;yes&quot;,&quot;post_id&quot;:6942,&quot;widget_id&quot;:&quot;01c17c7&quot;}" data-gallery-items="[&quot;&lt;div class=\\&quot;eael-filterable-gallery-item-wrap\\&quot;&gt;\n\t\t\t\t&lt;div class=\\&quot;eael-gallery-grid-item\\&quot;&gt;&lt;div class=\\&quot;gallery-item-thumbnail-wrap\\&quot;&gt;&lt;img src=\\&quot;https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/uploads\\/2021\\/02\\/Grandin-Print-Shop-1.png\\&quot; data-lazy-src=\\&quot;https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/uploads\\/2021\\/02\\/Grandin-Print-Shop-1.png\\&quot; alt=\\&quot;\\&quot; class=\\&quot;gallery-item-thumbnail\\&quot;&gt;&lt;\\/div&gt;&lt;div class=\\&quot;gallery-item-caption-wrap caption-style-hoverer eael-slide-up\\&quot;&gt;&lt;div class=\\&quot;gallery-item-hoverer-bg\\&quot;&gt;&lt;\\/div&gt;&lt;div class=\\&quot;gallery-item-caption-over\\&quot;&gt;&lt;h5 class=\\&quot;fg-item-title\\&quot;&gt;360 Tour of the Grandin Building&lt;\\/h5&gt;&lt;div class=\\&quot;gallery-item-buttons\\&quot;&gt;&lt;a href=\\&quot;https:\\/\\/goo.gl\\/maps\\/M7TmZVxN7EQg8S6P9\\&quot;target=\\&quot;_blank\\&quot;&gt;&lt;span class=\\&quot;fg-item-icon-inner\\&quot;&gt;&lt;i class=\\&quot;fas fa-link\\&quot; aria-hidden=\\&quot;true\\&quot;&gt;&lt;\\/i&gt;&lt;\\/span&gt;&lt;\\/a&gt;&lt;\\/div&gt;&lt;\\/div&gt;&lt;\\/div&gt;&lt;\\/div&gt;&lt;\\/div&gt;&quot;]" data-init-show="1">
                <div class="eael-filterable-gallery-item-wrap">
				<div class="eael-gallery-grid-item"><div class="gallery-item-thumbnail-wrap"><img src="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Print-Shop-1.png" data-lazy-src="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Grandin-Print-Shop-1.png" alt="" class="gallery-item-thumbnail"></div><div class="gallery-item-caption-wrap caption-style-hoverer eael-slide-up"><div class="gallery-item-hoverer-bg"></div><div class="gallery-item-caption-over"><h5 class="fg-item-title">360 Tour of the Grandin Building</h5><div class="gallery-item-buttons"><a href="https://goo.gl/maps/M7TmZVxN7EQg8S6P9"target="_blank"><span class="fg-item-icon-inner"><i class="fas fa-link" aria-hidden="true"></i></span></a></div></div></div></div></div>            </div>

                    </div>

        		</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-5a33f1c" data-id="5a33f1c" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
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
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-7f81931 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="7f81931" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-188653f" data-id="188653f" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-c16b5d4 elementor-widget elementor-widget-menu-anchor" data-id="c16b5d4" data-element_type="widget" data-widget_type="menu-anchor.default">
				<div class="elementor-widget-container">
					<div id="5" class="elementor-menu-anchor"></div>
				</div>
				</div>
				<div class="elementor-element elementor-element-dc01120 elementor-widget elementor-widget-heading" data-id="dc01120" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Smith Frame Home</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-50dd4c9 elementor-widget elementor-widget-heading" data-id="50dd4c9" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Key Points of Interest</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-f57836f elementor-icon-list--layout-traditional elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list" data-id="f57836f" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items">
							<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">Alvin Smith began construction on this larger farmhouse on the Smith property in 1822 but died in 1823. The Smith family was moved into the home by early 1826</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">In January 1827, after their marriage, Joseph and Emma moved into the home with the Smith family</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">After obtaining the golden plates in 1827, Joseph Smith, Jr. hid them several places in and around the frame home to keep them safe</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">At the frame home Joseph learned that Martin Harris lost the 116 pages of manuscript he had translated</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">Oliver Cowdery boarded here with the family from late 1828 to early 1829 and left for Harmony April 1829 to help Joseph with his work</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">The original frame home still stands on its original foundation, and a restoration project in 1998 returned the home to its 1820s appearance</span>
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
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-5e8e684 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="5e8e684" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-1548bb2" data-id="1548bb2" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-043d3e9 elementor-hidden-tablet elementor-hidden-phone elementor-widget elementor-widget-heading" data-id="043d3e9" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">(Hover over photo for more information, click to enlarge)</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-e327103 elementor-hidden-desktop elementor-widget elementor-widget-heading" data-id="e327103" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">(Tap photo to enlarge and see more information)​</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-8242872 elementor-widget elementor-widget-gallery" data-id="8242872" data-element_type="widget" data-settings="{&quot;overlay_title&quot;:&quot;title&quot;,&quot;overlay_description&quot;:&quot;caption&quot;,&quot;gallery_layout&quot;:&quot;justified&quot;,&quot;lazyload&quot;:&quot;yes&quot;,&quot;ideal_row_height&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:200,&quot;sizes&quot;:[]},&quot;ideal_row_height_tablet&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:150,&quot;sizes&quot;:[]},&quot;ideal_row_height_mobile&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:150,&quot;sizes&quot;:[]},&quot;gap&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;gap_tablet&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;gap_mobile&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;link_to&quot;:&quot;file&quot;,&quot;overlay_background&quot;:&quot;yes&quot;,&quot;content_hover_animation&quot;:&quot;fade-in&quot;}" data-widget_type="gallery.default">
				<div class="elementor-widget-container">
					<div class="elementor-gallery__container">
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-frame-home-2009-ken-mays.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-8242872" data-elementor-lightbox-title="Smith Frame Home" data-elementor-lightbox-description="Alvin Smith, the oldest of the Smith sons, supervised construction of this home, but it was unfinished at his passing on 19 Nov. 1823. Construction was then supervised by a neighbor, Russell Stoddard. (Photo Credit: Kenneth Mays, 2009)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-frame-home-2009-ken-mays-1024x786.jpg" data-width="525" data-height="403" alt="A white, two-story home with a red door behind a fence" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Smith Frame Home</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2009</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-frame-home-2009-07.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-8242872" data-elementor-lightbox-title="Smith Frame Home Front" data-elementor-lightbox-description="The frame home was completed enough for the Smiths to live in by early 1826. Joseph Smith, Jr. and Emma Hale Smith came to live in the frame home after their marriage 18 January 1827. (Photo Credit: Kenneth Mays, 2009)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-frame-home-2009-07-1024x683.jpg" data-width="525" data-height="350" alt="A white home with red trim and two windows on either side of the red front door sits within a fenced yard with trees." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Smith Frame Home Front</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2009</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-frame-home-int-2009-41.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-8242872" data-elementor-lightbox-title="Smith Frame Home Bedroom" data-elementor-lightbox-description="At one time the Smith sisters Sophronia and Katherine held and hid the golden plates between them in a bed as they pretended to be asleep. A mob came and ransacked the house but left the sisters alone and did not find the plates. (Photo Credit: Kenneth Mays, 2009)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-frame-home-int-2009-41-1024x701.jpg" data-width="525" data-height="359" alt="A spinning wheel, ned and chairs sit inside a room in the Smith Frame Home" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Smith Frame Home Bedroom</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2009</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-frame-home-int-2009-ken-mays.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-8242872" data-elementor-lightbox-title="Smith Frame Home Interior" data-elementor-lightbox-description="For a time Oliver Cowdery lived in this home with the Smith family, working as a schoolteacher nearby. At that point Joseph and Emma were living in their home in Harmony. (Photo Credit: Kenneth Mays, 2009)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-frame-home-int-2009-ken-mays-1024x680.jpg" data-width="525" data-height="349" alt="Chairs and a dresser line the walls of the interior of the Smith Frame Home." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Smith Frame Home Interior</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2009</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-frame-home-where-Joseph-learned-of-lost-116-pages-ken-mays.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-8242872" data-elementor-lightbox-title="Smith Frame Home Kitchen" data-elementor-lightbox-description="Here in the kitchen of the frame home Joseph Smith learned about the loss of the 116 pages of manuscript he had translated and loaned to Martin Harris. (Photo Credit: Kenneth Mays, 2009)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-frame-home-where-Joseph-learned-of-lost-116-pages-ken-mays-1024x677.jpg" data-width="525" data-height="347" alt="A table sits in front of a hearth in the kitchen of the Smith Frame Home." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Smith Frame Home Kitchen</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2009</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-Lucy-Mack-Smith_s-kitchen-fireplace-and-brick-hearth-in-the-Smith-frame-house.-John-W.-Welch-2018-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-8242872" data-elementor-lightbox-title="Smith Frame Home Fireplace" data-elementor-lightbox-description="Joseph once hid the golden plates under the hearth of this fireplace.(Photo Credit: John W. Welch, 2018)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-Lucy-Mack-Smith_s-kitchen-fireplace-and-brick-hearth-in-the-Smith-frame-house.-John-W.-Welch-2018-1024x768.jpg" data-width="525" data-height="394" alt="Cooking vessels and implements sit on the brick hearth next to a fireplace in the Smith Frame Home" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Smith Frame Home Fireplace</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2018</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-Smith-frame-house-stone-kitchen-sink.-John-W.-Welch-2018-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-8242872" data-elementor-lightbox-title="Smith Frame Home Kitchen Sink" data-elementor-lightbox-description="A dry sink in the Smith Frame Home sits in front of a window. (Photo Credit: John W. Welch, 2018)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-Smith-frame-house-stone-kitchen-sink.-John-W.-Welch-2018-1024x768.jpg" data-width="525" data-height="394" alt="A stone kitchen sink next to a window" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Smith Frame Home Kitchen Sink</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2018</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-frame-home-1985-01-HR-scaled.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-8242872" data-elementor-lightbox-title="Smith Frame Home Before Remodel" data-elementor-lightbox-description="Long after the Smiths had left the house changes were made to it. This is an image of the house in 1985. (Photo Credit: Kenneth Mays, 1985)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-frame-home-1985-01-HR-1024x697.jpg" data-width="525" data-height="357" alt="The front of a white home with a patio" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Smith Frame Home Before Remodel</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 1985</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Frame-home-remodel-ken-mays.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-8242872" data-elementor-lightbox-title="Smith Frame Home During Remodel" data-elementor-lightbox-description="In 1999 the frame home underwent a remodel to restore it to its original appearance. Despite the changes to the home, 85 percent of the home as it now stands is original. (Photo Credit: Kenneth Mays, 1999)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Frame-home-remodel-ken-mays.jpg" data-width="525" data-height="367" alt="Multiple two-by-four beams covered in a plastic sheet lean against a white house." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Smith Frame Home During Remodel</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 1999</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Frame-home-restoration-1999-01.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-8242872" data-elementor-lightbox-title="Smith Frame Home Interior During Remodel" data-elementor-lightbox-description="During the remodel workers revealed whitewashing and the original location of the stairs. (Photo Credit: Kenneth Mays, 1999)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Frame-home-restoration-1999-01-1024x716.jpg" data-width="525" data-height="367" alt="A sign that reads &quot;The original location of the stairs and white washed planks&quot; is taped to a bare wall with signs of wear." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Smith Frame Home Interior During Remodel</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 1999</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Frame-home-remodel-02.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-8242872" data-elementor-lightbox-title="Smith Frame Home and Barn During Remodel" data-elementor-lightbox-description="To restore the original appearance of the site, a barn was also brought from a property originally belonging to Brigham Young. (Photo Credit: Kenneth Mays, 1999)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Frame-home-remodel-02.jpg" data-width="525" data-height="357" alt="A white home, left, sits far behind a light brown wood barn, right" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Smith Frame Home and Barn During Remodel</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 1999</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-Joseph-Smith-Sr.-barn-where-on-one-occasion-Joseph-hid-the-plates-of-Mormon-to-protect-them-from-a-mob-searching-for-them.-John-W.-Welch-2003.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-8242872" data-elementor-lightbox-title="Threshing Barn" data-elementor-lightbox-description="The Smith family&#039;s barn was one of the places Joseph hid the plates when a mob came searching for them. (Photo Credit: John W. Welch, 2003)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Palmyra-Manchester-NY-Joseph-Smith-Sr.-barn-where-on-one-occasion-Joseph-hid-the-plates-of-Mormon-to-protect-them-from-a-mob-searching-for-them.-John-W.-Welch-2003-1024x768.jpg" data-width="525" data-height="394" alt="An old, weathered barn" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Threshing Barn</div>
														<div class="elementor-gallery-item__description">Photo Credit: John W. Welch, 2003</div>
												</div>
									</a>
					</div>
			</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-4857151 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="4857151" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-43a70ee" data-id="43a70ee" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-a5569f5 elementor-widget elementor-widget-heading" data-id="a5569f5" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Take a 360<strong style="margin: 0px; padding: 0px; color: rgb(51, 51, 51); font-family: sans-serif; font-size: 19.2px; text-align: start; white-space: normal;">°</strong> Tour of the Smith Frame Home</h2>		</div>
				</div>
				<section class="has_eae_slider elementor-section elementor-inner-section elementor-element elementor-element-0b7f5bd elementor-section-height-min-height elementor-section-boxed elementor-section-height-default" data-id="0b7f5bd" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-ea16e48" data-id="ea16e48" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
								</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-f417aa2" data-id="f417aa2" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-e03fc1f elementor-grid-1 eael-fg-hoverer-content-align-center elementor-grid-tablet-1 elementor-grid-mobile-1 elementor-widget elementor-widget-eael-filterable-gallery" data-id="e03fc1f" data-element_type="widget" data-settings="{&quot;columns&quot;:&quot;1&quot;,&quot;columns_tablet&quot;:&quot;1&quot;,&quot;columns_mobile&quot;:&quot;1&quot;,&quot;photo_gallery&quot;:&quot;yes&quot;,&quot;pagination&quot;:&quot;false&quot;}" data-widget_type="eael-filterable-gallery.default">
				<div class="elementor-widget-container">
			        <div id="eael-filter-gallery-wrapper-e03fc1f" class="eael-filter-gallery-wrapper" data-layout-mode="hoverer" data-mfp_caption="">


            <div class="eael-filter-gallery-container masonry" data-images-per-page="" data-total-gallery-items="1" data-nomore-item-text="" data-settings="{&quot;grid_style&quot;:&quot;masonry&quot;,&quot;popup&quot;:&quot;buttons&quot;,&quot;duration&quot;:500,&quot;gallery_enabled&quot;:&quot;yes&quot;,&quot;post_id&quot;:6942,&quot;widget_id&quot;:&quot;e03fc1f&quot;}" data-gallery-items="[&quot;&lt;div class=\\&quot;eael-filterable-gallery-item-wrap\\&quot;&gt;\n\t\t\t\t&lt;div class=\\&quot;eael-gallery-grid-item\\&quot;&gt;&lt;div class=\\&quot;gallery-item-thumbnail-wrap\\&quot;&gt;&lt;img src=\\&quot;https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/uploads\\/2021\\/02\\/Smith-Frame-Home.png\\&quot; data-lazy-src=\\&quot;https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/uploads\\/2021\\/02\\/Smith-Frame-Home.png\\&quot; alt=\\&quot;Screenshot of the Google Maps 360 view of the Smith Frame Home\\&quot; class=\\&quot;gallery-item-thumbnail\\&quot;&gt;&lt;\\/div&gt;&lt;div class=\\&quot;gallery-item-caption-wrap caption-style-hoverer eael-slide-up\\&quot;&gt;&lt;div class=\\&quot;gallery-item-hoverer-bg\\&quot;&gt;&lt;\\/div&gt;&lt;div class=\\&quot;gallery-item-caption-over\\&quot;&gt;&lt;h5 class=\\&quot;fg-item-title\\&quot;&gt;360 Tour of the Smith Frame Home&lt;\\/h5&gt;&lt;div class=\\&quot;gallery-item-buttons\\&quot;&gt;&lt;a href=\\&quot;https:\\/\\/goo.gl\\/maps\\/DPdLnHXgD67QaGV18\\&quot;target=\\&quot;_blank\\&quot;&gt;&lt;span class=\\&quot;fg-item-icon-inner\\&quot;&gt;&lt;i class=\\&quot;fas fa-link\\&quot; aria-hidden=\\&quot;true\\&quot;&gt;&lt;\\/i&gt;&lt;\\/span&gt;&lt;\\/a&gt;&lt;\\/div&gt;&lt;\\/div&gt;&lt;\\/div&gt;&lt;\\/div&gt;&lt;\\/div&gt;&quot;]" data-init-show="1">
                <div class="eael-filterable-gallery-item-wrap">
				<div class="eael-gallery-grid-item"><div class="gallery-item-thumbnail-wrap"><img src="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-Frame-Home.png" data-lazy-src="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Smith-Frame-Home.png" alt="Screenshot of the Google Maps 360 view of the Smith Frame Home" class="gallery-item-thumbnail"></div><div class="gallery-item-caption-wrap caption-style-hoverer eael-slide-up"><div class="gallery-item-hoverer-bg"></div><div class="gallery-item-caption-over"><h5 class="fg-item-title">360 Tour of the Smith Frame Home</h5><div class="gallery-item-buttons"><a href="https://goo.gl/maps/DPdLnHXgD67QaGV18"target="_blank"><span class="fg-item-icon-inner"><i class="fas fa-link" aria-hidden="true"></i></span></a></div></div></div></div></div>            </div>

                    </div>

        		</div>
				</div>
						</div>
					</div>
		</div>
				<div class="has_eae_slider elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-6b3b82f" data-id="6b3b82f" data-element_type="column">
			<div class="elementor-column-wrap">
							<div class="elementor-widget-wrap">
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
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-8eb1610 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="8eb1610" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-63e5e46" data-id="63e5e46" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-d88a2a6 elementor-widget elementor-widget-menu-anchor" data-id="d88a2a6" data-element_type="widget" data-widget_type="menu-anchor.default">
				<div class="elementor-widget-container">
					<div id="6" class="elementor-menu-anchor"></div>
				</div>
				</div>
				<div class="elementor-element elementor-element-fb8a068 elementor-widget elementor-widget-heading" data-id="fb8a068" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Martin Harris Farm</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-2e5d641 elementor-widget elementor-widget-heading" data-id="2e5d641" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Key Points of Interest</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-e43d766 elementor-icon-list--layout-traditional elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list" data-id="e43d766" data-element_type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
					<ul class="elementor-icon-list-items">
							<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">Martin Harris was a prosperous and well-respected farmer in Palmyra</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">Martin was living here when the 116 pages of the Book of Mormon manuscript were lost</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">Martin mortgaged his farm as security for the first printing of the Book of Mormon. At that time he owned 240 acres. He later had to sell 151 acres of the farm to pay the debt of $3,000</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">The house built on the farm land is not original: It was built on the site of the original home after the original burned down in 1849</span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<i aria-hidden="true" class="fas fa-circle"></i>						</span>
										<span class="elementor-icon-list-text">Martin's property was once 300 acres—the Church now owns a small parcel of that land</span>
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
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-4c17405 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="4c17405" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-40e5402" data-id="40e5402" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-604472d elementor-hidden-tablet elementor-hidden-phone elementor-widget elementor-widget-heading" data-id="604472d" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">(Hover over photo for more information, click to enlarge)</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-15cd500 elementor-hidden-desktop elementor-widget elementor-widget-heading" data-id="15cd500" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">(Tap photo to enlarge and see more information)​</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-48648cd elementor-widget elementor-widget-gallery" data-id="48648cd" data-element_type="widget" data-settings="{&quot;overlay_title&quot;:&quot;title&quot;,&quot;overlay_description&quot;:&quot;caption&quot;,&quot;gallery_layout&quot;:&quot;justified&quot;,&quot;lazyload&quot;:&quot;yes&quot;,&quot;ideal_row_height&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:200,&quot;sizes&quot;:[]},&quot;ideal_row_height_tablet&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:150,&quot;sizes&quot;:[]},&quot;ideal_row_height_mobile&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:150,&quot;sizes&quot;:[]},&quot;gap&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;gap_tablet&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;gap_mobile&quot;:{&quot;unit&quot;:&quot;px&quot;,&quot;size&quot;:10,&quot;sizes&quot;:[]},&quot;link_to&quot;:&quot;file&quot;,&quot;overlay_background&quot;:&quot;yes&quot;,&quot;content_hover_animation&quot;:&quot;fade-in&quot;}" data-widget_type="gallery.default">
				<div class="elementor-widget-container">
					<div class="elementor-gallery__container">
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Martin-Harris-farm-2006-ken-mays.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-48648cd" data-elementor-lightbox-title="Martin Harris Farm" data-elementor-lightbox-description="The church owns a portion of Martin Harris&#039; original property. The home built on the property is not original—the original frame home of Martin Harris burned down in 1849. (Photo Credit: Kenneth Mays, 2006)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Martin-Harris-farm-2006-ken-mays-1024x686.jpg" data-width="525" data-height="352" alt="A brown, brick, two-story home with two red chimneys sits behind some trees." ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Martin Harris Farm</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2006</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/08/PH_9809_f0631_item_17-Martin_and_Lucy_Harris_farm_and_home-scaled.jpeg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-48648cd" data-elementor-lightbox-title="House on Martin Harris Farm Property" data-elementor-lightbox-description="Martin took out an 18-month mortgage on his farm on 20 August 1829 as security for E. B. Grandin to print 5,000 copies of The Book of Mormon. He ended up selling about 150 acres of the farm on 7 April 1831 to get the money he needed to pay off the mortgage. (Photo Credit: Kenneth Mays, 2006)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/08/PH_9809_f0631_item_17-Martin_and_Lucy_Harris_farm_and_home-1024x681.jpeg" data-width="525" data-height="349" alt="A brown, brick, two-story home with two red chimneys" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">House on Martin Harris Farm Property</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays, 2006</div>
												</div>
									</a>
							<a class="e-gallery-item elementor-gallery-item elementor-animated-content" href="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Lucy-Harris-home-01.jpg" data-elementor-open-lightbox="yes" data-elementor-lightbox-slideshow="all-48648cd" data-elementor-lightbox-title="Original Lucy Harris Home" data-elementor-lightbox-description="Martin deeded 80 acres of the farm to his wife via her brother, Peter Harris, in November 1825. The house she built on that property is still standing and is pictured here. It is not part of the property owned by the church. (Photo Credit: Kenneth Mays)">
					<div class="e-gallery-image elementor-gallery-item__image" data-thumbnail="https://doctrineandcovenantscentral.org/wp-content/uploads/2021/02/Lucy-Harris-home-01-1024x728.jpg" data-width="525" data-height="373" alt="A white, two-story home sits behind some trees" ></div>
										<div class="elementor-gallery-item__overlay"></div>
															<div class="elementor-gallery-item__content">
													<div class="elementor-gallery-item__title">Original Lucy Harris Home</div>
														<div class="elementor-gallery-item__description">Photo Credit: Kenneth Mays</div>
												</div>
									</a>
					</div>
			</div>
				</div>
						</div>
					</div>
		</div>
								</div>
					</div>
		</section>
				<section class="has_eae_slider elementor-section elementor-top-section elementor-element elementor-element-7e17839 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="7e17839" data-element_type="section">
						<div class="elementor-container elementor-column-gap-default">
							<div class="elementor-row">
					<div class="has_eae_slider elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-e6fa05e" data-id="e6fa05e" data-element_type="column">
			<div class="elementor-column-wrap elementor-element-populated">
							<div class="elementor-widget-wrap">
						<div class="elementor-element elementor-element-427952d elementor-widget elementor-widget-heading" data-id="427952d" data-element_type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
			<h2 class="elementor-heading-title elementor-size-default">Directions to Palmyra, NY</h2>		</div>
				</div>
				<div class="elementor-element elementor-element-b83e783 elementor-widget elementor-widget-google_maps" data-id="b83e783" data-element_type="widget" data-widget_type="google_maps.default">
				<div class="elementor-widget-container">
			<div class="elementor-custom-embed"><iframe frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?q=Palmyra%2C%20New%20York&amp;t=m&amp;z=15&amp;output=embed&amp;iwloc=near" title="Palmyra, New York" aria-label="Palmyra, New York"></iframe></div>		</div>
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

<link rel='stylesheet' id='elementor-gallery-css'  href='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/e-gallery/css/e-gallery.min.css?ver=1.2.0' media='all' />
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/toolset-blocks/public/js/views-frontend.js?ver=3.4.2' id='views-blocks-frontend-js'></script>
<script id='eae-main-js-extra'>
var eae = {"ajaxurl":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-admin\\/admin-ajax.php","current_url":"aHR0cHM6Ly9kb2N0cmluZWFuZGNvdmVuYW50c2NlbnRyYWwub3JnL3BhbG15cmEtbmV3LXlvcmsv","breakpoints":{"xs":0,"sm":480,"md":768,"lg":1025,"xl":1440,"xxl":1600}};
var eae_editor = {"plugin_url":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/plugins\\/addon-elements-for-elementor-page-builder\\/"};
</script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/js/eae.min.js?ver=1.0' id='eae-main-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/js/animated-main.min.js?ver=1.0' id='animated-main-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/js/particles.min.js?ver=1.0' id='eae-particles-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/lib/magnific.min.js?ver=1.9' id='wts-magnific-js'></script>
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/lib/vegas/vegas.min.js?ver=2.4.0' id='vegas-js'></script>
<script id='843868bf1-js-extra'>
var localize = {"ajaxurl":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-admin\\/admin-ajax.php","nonce":"f0799d4cb4","i18n":{"added":"Added ","compare":"Compare","loading":"Loading..."}};
</script>
<script src='https://doctrineandcovenantscentral.org/wp-content/uploads/essential-addons-elementor/843868bf1.min.js?ver=1699160209' id='843868bf1-js'></script>
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
<script src='https://doctrineandcovenantscentral.org/wp-content/plugins/elementor/assets/lib/e-gallery/js/e-gallery.min.js?ver=1.2.0' id='elementor-gallery-js'></script>
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
var elementorFrontendConfig = {"environmentMode":{"edit":false,"wpPreview":false,"isScriptDebug":false},"i18n":{"shareOnFacebook":"Share on Facebook","shareOnTwitter":"Share on Twitter","pinIt":"Pin it","download":"Download","downloadImage":"Download image","fullscreen":"Fullscreen","zoom":"Zoom","share":"Share","playVideo":"Play Video","previous":"Previous","next":"Next","close":"Close"},"is_rtl":false,"breakpoints":{"xs":0,"sm":480,"md":768,"lg":1025,"xl":1440,"xxl":1600},"responsive":{"breakpoints":{"mobile":{"label":"Mobile","value":767,"direction":"max","is_enabled":true},"mobile_extra":{"label":"Mobile Extra","value":880,"direction":"max","is_enabled":false},"tablet":{"label":"Tablet","value":1024,"direction":"max","is_enabled":true},"tablet_extra":{"label":"Tablet Extra","value":1365,"direction":"max","is_enabled":false},"laptop":{"label":"Laptop","value":1620,"direction":"max","is_enabled":false},"widescreen":{"label":"Widescreen","value":2400,"direction":"min","is_enabled":false}}},"version":"3.2.3","is_static":false,"experimentalFeatures":{"form-submissions":true},"urls":{"assets":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/plugins\\/elementor\\/assets\\/"},"settings":{"page":[],"editorPreferences":[]},"kit":{"active_breakpoints":["viewport_mobile","viewport_tablet"],"global_image_lightbox":"yes","lightbox_enable_counter":"yes","lightbox_enable_fullscreen":"yes","lightbox_enable_zoom":"yes","lightbox_enable_share":"yes","lightbox_title_src":"title","lightbox_description_src":"description"},"post":{"id":6942,"title":"Palmyra-Manchester%2C%20New%20York%20%E2%80%93%20Doctrine%20and%20Covenants%20Central","excerpt":"","featuredImage":"https:\\/\\/doctrineandcovenantscentral.org\\/wp-content\\/uploads\\/2021\\/02\\/Palmyra-Manchester-log-fence.-Christina-Broberg-2012-1-1024x683.jpg"}};
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
    """It returns a valid Document for a conference talk."""
    url = "https://doctrineandcovenantscentral.org/palmyra-new-york/"
    result = load_dc_places(url, html)
    assert len(result.page_content) > 0
    assert result.metadata["url"] == url
    assert result.metadata["title"] == "Places of the D&C / Palmyra-Manchester, New York"
    assert result.page_content.startswith("## Sacred Grove\n\n")
