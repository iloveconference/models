"""Test cases for the load_know module."""
# flake8: noqa

from models import load_know


html = """
<!DOCTYPE html>
<html lang="en" dir="ltr" prefix="og: http://ogp.me/ns# content: http://purl.org/rss/1.0/modules/content/ dc: http://purl.org/dc/terms/ foaf: http://xmlns.com/foaf/0.1/ rdfs: http://www.w3.org/2000/01/rdf-schema# sioc: http://rdfs.org/sioc/ns# sioct: http://rdfs.org/sioc/types# skos: http://www.w3.org/2004/02/skos/core# xsd: http://www.w3.org/2001/XMLSchema#">
<head>
  <link rel="profile" href="http://www.w3.org/1999/xhtml/vocab" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="shortcut icon" href="https://knowhy.bookofmormoncentral.org/sites/all/themes/knowhy_subtheme/favicon.ico" type="image/vnd.microsoft.icon" />
<meta name="description" content="The Know In 1820, as Joseph Smith prayed in the Sacred Grove, he saw God the Father and His Son, Jesus Christ. Joseph, who had been struggling to know where he might find the true church, asked the divine personages “which of all the sects was right (for at this time it had never entered into my heart that all were wrong)—and which I should join” (Joseph Smith—History 1:18)." />
<meta name="abstract" content="The Know In 1820, as Joseph Smith prayed in the Sacred Grove, he saw God the Father and His Son, Jesus Christ. Joseph, who had been struggling to know where he might find the true church, asked the divine personages “which of all the sects was right (for at this time it had never entered into my heart that all were wrong)—and which I should join” (Joseph Smith—History 1:18)." />
<meta name="rating" content="general" />
<meta name="generator" content="Drupal 7 (https://www.drupal.org)" />
<meta name="rights" content="Book of Mormon Central" />
<link rel="image_src" href="https://knowhy.bookofmormoncentral.org/sites/default/files/knowhy-img/2023/10/main/knowhy-695-what-does-new-testament-teach-about-great-apostasy-martyrdom-of-saint-matthew-caravaggio.jpg" />
<link rel="canonical" href="https://knowhy.bookofmormoncentral.org/knowhy/what-does-the-new-testament-teach-about-the-great-apostasy" />
<link rel="shortlink" href="https://knowhy.bookofmormoncentral.org/node/949" />
<meta property="og:site_name" content="Book of Mormon Central" />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://knowhy.bookofmormoncentral.org/knowhy/what-does-the-new-testament-teach-about-the-great-apostasy" />
<meta property="og:title" content="What Does the New Testament Teach about the Great Apostasy?" />
<meta property="og:description" content="The Know In 1820, as Joseph Smith prayed in the Sacred Grove, he saw God the Father and His Son, Jesus Christ. Joseph, who had been struggling to know where he might find the true church, asked the divine personages “which of all the sects was right (for at this time it had never entered into my heart that all were wrong)—and which I should join” (Joseph Smith—History 1:18)." />
<meta property="og:updated_time" content="2023-10-16T22:00:01-06:00" />
<meta property="og:image" content="https://knowhy.bookofmormoncentral.org/sites/default/files/knowhy-img/2023/10/main/knowhy-695-what-does-new-testament-teach-about-great-apostasy-martyrdom-of-saint-matthew-caravaggio.jpg" />
<meta property="article:published_time" content="2023-10-17T00:00:00-06:00" />
<meta property="article:modified_time" content="2023-10-16T22:00:01-06:00" />
  <title>What Does the New Testament Teach about the Great Apostasy? | Book of Mormon Central</title>
  <link type="text/css" rel="stylesheet" href="https://knowhy.bookofmormoncentral.org/sites/default/files/css/css_lQaZfjVpwP_oGNqdtWCSpJT1EMqXdMiU84ekLLxQnc4.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://knowhy.bookofmormoncentral.org/sites/default/files/css/css_Nav1MD3i6avU6kiJAnDriXQirDFfEROUd1BJXva9UMc.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://knowhy.bookofmormoncentral.org/sites/default/files/css/css_WT-pdXN680l-kX7Qj5BpcXXcR6HhN_ILPqsPHH3aZ-s.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://knowhy.bookofmormoncentral.org/sites/default/files/css/css_YXo7edvbC96GERuBr4BMXxBKlnT6R4bjUGQWF68yV3E.css" media="all" />
  <!-- HTML5 element support for IE6-8 -->
  <!--[if lt IE 9]>
    <script src="https://cdn.jsdelivr.net/html5shiv/3.7.3/html5shiv-printshiv.min.js"></script>
  <![endif]-->

<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-KX24VBJ');</script>
<!-- End Google Tag Manager -->

  <script defer="defer" src="https://knowhy.bookofmormoncentral.org/sites/default/files/google_tag/knowhy_of_book_of_mormon_central_ga4/google_tag.script.js?rt4781"></script>
<script src="https://knowhy.bookofmormoncentral.org/sites/all/modules/jquery_update/replace/jquery/1.10/jquery.min.js?v=1.10.2"></script>
<script src="https://knowhy.bookofmormoncentral.org/misc/jquery-extend-3.4.0.js?v=1.10.2"></script>
<script src="https://knowhy.bookofmormoncentral.org/misc/jquery-html-prefilter-3.5.0-backport.js?v=1.10.2"></script>
<script src="https://knowhy.bookofmormoncentral.org/misc/jquery.once.js?v=1.2"></script>
<script src="https://knowhy.bookofmormoncentral.org/misc/drupal.js?rt4781"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.js"></script>
<script src="https://knowhy.bookofmormoncentral.org/sites/all/modules/google_cse/google_cse.js?rt4781"></script>
<script src="https://knowhy.bookofmormoncentral.org/sites/all/modules/lightbox2/js/lightbox.js?rt4781"></script>
<script src="https://knowhy.bookofmormoncentral.org/sites/all/modules/custom_search/js/custom_search.js?rt4781"></script>
<script src="https://knowhy.bookofmormoncentral.org/sites/all/modules/service_links/js/pinterest_button.js?rt4781"></script>
<script src="https://knowhy.bookofmormoncentral.org/sites/all/modules/service_links/js/google_plus_one.js?rt4781"></script>
<script src="https://knowhy.bookofmormoncentral.org/sites/all/modules/tb_megamenu/js/tb-megamenu-frontend.js?rt4781"></script>
<script src="https://knowhy.bookofmormoncentral.org/sites/all/modules/service_links/js/facebook_share.js?rt4781"></script>
<script src="https://knowhy.bookofmormoncentral.org/sites/all/modules/service_links/js/twitter_button.js?rt4781"></script>
<script src="https://knowhy.bookofmormoncentral.org/sites/all/modules/tb_megamenu/js/tb-megamenu-touch.js?rt4781"></script>
<script src="https://knowhy.bookofmormoncentral.org/sites/all/libraries/wow/dist/wow.min.js?rt4781"></script>
<script src="https://knowhy.bookofmormoncentral.org/sites/all/modules/responsive_dropdown_menus/theme/responsive-dropdown-menus.js?rt4781"></script>
<script>window.__insp = window.__insp || [];
__insp.push(['wid', 1855051008]);
(function() {
function ldinsp(){if(typeof window.__inspld != "undefined") return; window.__inspld = 1; var insp = document.createElement('script'); insp.type = 'text/javascript'; insp.async = true; insp.id = "inspsync"; insp.src = ('https:' == document.location.protocol ? 'https' : 'http') + '://cdn.inspectlet.com/inspectlet.js'; var x = document.getElementsByTagName('script')[0]; x.parentNode.insertBefore(insp, x); };
setTimeout(ldinsp, 500); document.readyState != "complete" ? (window.attachEvent ? window.attachEvent('onload', ldinsp) : window.addEventListener('load', ldinsp, false)) : ldinsp();
})();</script>
<script src="https://knowhy.bookofmormoncentral.org/sites/all/themes/bmc/js/custom.js?rt4781"></script>
<script src="https://knowhy.bookofmormoncentral.org/sites/all/themes/bmc/js/masonry.pkgd.min.js?rt4781"></script>
<script src="https://knowhy.bookofmormoncentral.org/sites/all/themes/bmc/js/wow.min.js?rt4781"></script>
<script>jQuery.extend(Drupal.settings, {"basePath":"\\/","pathPrefix":"","ajaxPageState":{"theme":"knowhy_subtheme","theme_token":"z_xEZxfhTpp79-R0pxUDR34yF6byfKPc1azuNcCu2UY","js":{"sites\\/all\\/themes\\/bootstrap\\/js\\/bootstrap.js":1,"https:\\/\\/knowhy.bookofmormoncentral.org\\/sites\\/default\\/files\\/google_tag\\/knowhy_of_book_of_mormon_central_ga4\\/google_tag.script.js":1,"sites\\/all\\/modules\\/jquery_update\\/replace\\/jquery\\/1.10\\/jquery.min.js":1,"misc\\/jquery-extend-3.4.0.js":1,"misc\\/jquery-html-prefilter-3.5.0-backport.js":1,"misc\\/jquery.once.js":1,"misc\\/drupal.js":1,"https:\\/\\/cdn.jsdelivr.net\\/npm\\/bootstrap@3.3.7\\/dist\\/js\\/bootstrap.js":1,"sites\\/all\\/modules\\/google_cse\\/google_cse.js":1,"sites\\/all\\/modules\\/lightbox2\\/js\\/lightbox.js":1,"sites\\/all\\/modules\\/custom_search\\/js\\/custom_search.js":1,"sites\\/all\\/modules\\/service_links\\/js\\/pinterest_button.js":1,"sites\\/all\\/modules\\/service_links\\/js\\/google_plus_one.js":1,"sites\\/all\\/modules\\/tb_megamenu\\/js\\/tb-megamenu-frontend.js":1,"sites\\/all\\/modules\\/service_links\\/js\\/facebook_share.js":1,"sites\\/all\\/modules\\/service_links\\/js\\/twitter_button.js":1,"sites\\/all\\/modules\\/tb_megamenu\\/js\\/tb-megamenu-touch.js":1,"sites\\/all\\/libraries\\/wow\\/dist\\/wow.min.js":1,"sites\\/all\\/modules\\/responsive_dropdown_menus\\/theme\\/responsive-dropdown-menus.js":1,"0":1,"sites\\/all\\/themes\\/bmc\\/js\\/custom.js":1,"sites\\/all\\/themes\\/bmc\\/js\\/masonry.pkgd.min.js":1,"sites\\/all\\/themes\\/bmc\\/js\\/wow.min.js":1},"css":{"modules\\/system\\/system.base.css":1,"sites\\/all\\/modules\\/date\\/date_api\\/date.css":1,"modules\\/field\\/theme\\/field.css":1,"sites\\/all\\/modules\\/footnotes\\/footnotes.css":1,"sites\\/all\\/modules\\/google_cse\\/google_cse.css":1,"modules\\/node\\/node.css":1,"sites\\/all\\/modules\\/views\\/css\\/views.css":1,"sites\\/all\\/libraries\\/animate\\/animate.min.css":1,"sites\\/all\\/modules\\/ctools\\/css\\/ctools.css":1,"sites\\/all\\/modules\\/lightbox2\\/css\\/lightbox_alt.css":1,"sites\\/all\\/modules\\/custom_search\\/custom_search.css":1,"sites\\/all\\/modules\\/tb_megamenu\\/css\\/bootstrap.css":1,"sites\\/all\\/modules\\/tb_megamenu\\/css\\/base.css":1,"sites\\/all\\/modules\\/tb_megamenu\\/css\\/default.css":1,"sites\\/all\\/modules\\/tb_megamenu\\/css\\/compatibility.css":1,"sites\\/all\\/modules\\/flippy\\/flippy.css":1,"sites\\/all\\/modules\\/ds\\/layouts\\/ds_2col_stacked\\/ds_2col_stacked.css":1,"sites\\/all\\/modules\\/responsive_dropdown_menus\\/theme\\/responsive-dropdown-menus.css":1,"sites\\/all\\/modules\\/social_media_links\\/social_media_links.css":1,"sites\\/all\\/libraries\\/fontawesome\\/css\\/font-awesome.css":1,"https:\\/\\/cdn.jsdelivr.net\\/npm\\/bootstrap@3.3.7\\/dist\\/css\\/bootstrap.min.css":1,"sites\\/all\\/themes\\/bmc\\/css\\/style.css":1,"sites\\/all\\/themes\\/bmc\\/css\\/custom.css":1,"sites\\/all\\/themes\\/bmc\\/css\\/animate.css":1,"sites\\/all\\/themes\\/knowhy_subtheme\\/css\\/knowhy-styles.css":1}},"googleCSE":{"cx":"001946668175012064535:tb4uxxvjjhw","resultsWidth":600,"domain":"www.google.com","showWaterMark":1},"lightbox2":{"rtl":0,"file_path":"\\/(\\w\\w\\/)public:\\/","default_image":"\\/sites\\/all\\/modules\\/lightbox2\\/images\\/brokenimage.jpg","border_size":10,"font_color":"fff","box_color":"2E2521","top_position":"","overlay_opacity":"0.8","overlay_color":"000","disable_close_click":1,"resize_sequence":0,"resize_speed":400,"fade_in_speed":400,"slide_down_speed":600,"use_alt_layout":1,"disable_resize":0,"disable_zoom":0,"force_show_nav":1,"show_caption":1,"loop_items":1,"node_link_text":"View Image Details","node_link_target":0,"image_count":"Image !current of !total","video_count":"Video !current of !total","page_count":"Page !current of !total","lite_press_x_close":"press \u003Ca href=\u0022#\u0022 onclick=\u0022hideLightbox(); return FALSE;\u0022\u003E\u003Ckbd\u003Ex\u003C\\/kbd\u003E\u003C\\/a\u003E to close","download_link_text":"","enable_login":false,"enable_contact":false,"keys_close":"c x 27","keys_previous":"p 37","keys_next":"n 39","keys_zoom":"z","keys_play_pause":"32","display_image_size":"original","image_node_sizes":"()","trigger_lightbox_classes":"","trigger_lightbox_group_classes":"","trigger_slideshow_classes":"","trigger_lightframe_classes":"","trigger_lightframe_group_classes":"","custom_class_handler":0,"custom_trigger_classes":"","disable_for_gallery_lists":true,"disable_for_acidfree_gallery_lists":true,"enable_acidfree_videos":true,"slideshow_interval":5000,"slideshow_automatic_start":true,"slideshow_automatic_exit":true,"show_play_pause":true,"pause_on_next_click":false,"pause_on_previous_click":true,"loop_slides":false,"iframe_width":600,"iframe_height":400,"iframe_border":1,"enable_video":0,"useragent":"Mozilla\\/5.0 (X11; Linux x86_64) AppleWebKit\\/537.36 (KHTML, like Gecko) Chrome\\/117.0.0.0 Safari\\/537.36"},"custom_search":{"form_target":"_self","solr":0},"ws_fs":{"type":"button_count","app_id":"150123828484431","css":"","locale":"en_US"},"ws_gpo":{"size":"","annotation":"","lang":"","callback":"","width":300},"ws_pb":{"countlayout":"horizontal"},"urlIsAjaxTrusted":{"\\/knowhy\\/what-does-the-new-testament-teach-about-the-great-apostasy":true},"responsive_dropdown_menus":{"menu-knowhy-menu":"KnoWhy Menu","main-menu":"Main menu","management":"Management","navigation":"Navigation","user-menu":"User menu"},"bootstrap":{"anchorsFix":"0","anchorsSmoothScrolling":"0","formHasError":1,"popoverEnabled":1,"popoverOptions":{"animation":1,"html":0,"placement":"right","selector":"","trigger":"click","triggerAutoclose":1,"title":"","content":"","delay":0,"container":"body"},"tooltipEnabled":1,"tooltipOptions":{"animation":1,"html":0,"placement":"auto left","selector":"","trigger":"hover focus","delay":0,"container":"body"}}});</script>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-71498334-1', 'auto');
  ga('send', 'pageview');

</script>

<!-- Global site tag (gtag.js) - Google Ads: 750349762 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-750349762"></script>
<script>
  window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date());
  gtag('config', 'AW-750349762');
</script>

</head>
<body class="navbar-is-static-top html not-front not-logged-in no-sidebars page-node page-node- page-node-949 node-type-knowhy">

<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KX24VBJ"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

  <div id="skip-link">
    <a href="#main-content" class="element-invisible element-focusable">Skip to main content</a>
  </div>
    <div class="region region-page-top">
    <noscript aria-hidden="true"><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-M6K5JXX" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  </div>
  <header id="navbar" role="banner" class="navbar navbar-static-top navbar-default">
  <div class="container">
    <div class="navbar-header">
              <a class="logo navbar-btn pull-left" href="https://bookofmormoncentral.org" title="Home">
          <img src="https://knowhy.bookofmormoncentral.org/sites/default/files/trazado-171x.png" alt="Home" />
        </a>

        <div class="navbar-brand">
              <a class="name" href="https://bookofmormoncentral.org" title="Home">Book of Mormon Central</a>
                      <div class="slogan">A Non-Profit Organization</div>
    </div>

              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-collapse">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
          </div>

          <div class="navbar-collapse collapse" id="navbar-collapse">
        <nav role="navigation">
          <!--                                                       -->
                        <div class="region region-navigation">
    <section id="block-search-form" class="block block-search clearfix">


  <form class="search-form form-search content-search" role="search" action="/knowhy/what-does-the-new-testament-teach-about-the-great-apostasy" method="post" id="search-block-form" accept-charset="UTF-8"><div><div>
      <h2 class="element-invisible">Search form</h2>
    <div class="input-group"><input title="Enter the terms you wish to search for." class="custom-search-box form-control form-text" placeholder="Search" type="text" id="edit-search-block-form--2" name="search_block_form" value="" size="15" maxlength="128" /><span class="input-group-btn"><button type="submit" class="btn btn-primary"><span class="icon glyphicon glyphicon-search" aria-hidden="true"></span>
</button></span></div><div class="form-actions form-wrapper form-group" id="edit-actions"><button style="display:none;" class="element-invisible btn form-submit" type="submit" id="edit-submit" name="op" value=""></button>
</div><input type="hidden" name="form_build_id" value="form-8YOcY3MQSnhpRWU43xgOxGkn9HcFqpvyaU8I6d8VRBA" />
<input type="hidden" name="form_id" value="search_block_form" />
</div>
</div></form>
</section>
<section id="block-tb-megamenu-main-menu" class="block block-tb-megamenu clearfix">


  <div  class="tb-megamenu tb-megamenu-main-menu">
      <button data-target=".nav-collapse" data-toggle="collapse" class="btn btn-navbar tb-megamenu-button" type="button">
      <i class="fa fa-reorder"></i>
    </button>
    <div class="nav-collapse ">
    <ul  class="tb-megamenu-nav nav level-0 items-9">
  <li  data-id="1050" data-level="1" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="center" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-1 mega mega-align-center dropdown">
  <a href="https://bookofmormoncentral.org/come-follow-me"  class="dropdown-toggle" title="Come Follow Me">

    Come Follow Me          <span class="caret"></span>
          </a>
  <div  data-class="" data-width="" class="tb-megamenu-submenu dropdown-menu mega-dropdown-menu nav-child">
  <div class="mega-dropdown-inner">
    <div  class="tb-megamenu-row row-fluid">
  <div  data-class="" data-width="12" data-hidewcol="0" id="tb-megamenu-column-1" class="tb-megamenu-column span12  mega-col-nav">
  <div class="tb-megamenu-column-inner mega-inner clearfix">
        <ul  class="tb-megamenu-subnav mega-nav level-1 items-4">
  <li  data-id="1778" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/come-follow-me/old-testament"  title="Old Testament">

    Old Testament          </a>
  </li>

<li  data-id="1743" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/come-follow-me/new-testament-2023"  title="New Testament">

    New Testament          </a>
  </li>

<li  data-id="1742" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/come-follow-me/book-of-mormon-2024"  title="Book of Mormon">

    Book of Mormon          </a>
  </li>

<li  data-id="1741" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/come-follow-me/doctrine-and-covenants"  title="Doctrine and Covenants">

    Doctrine and Covenants          </a>
  </li>
</ul>
  </div>
</div>
</div>
  </div>
</div>
</li>

<li  data-id="774" data-level="1" data-type="menu_item" data-class="" data-xicon="fa" data-caption="" data-alignsub="center" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-1 mega mega-align-center dropdown">
  <a href="https://bookofmormoncentral.org/research"  class="dropdown-toggle" title="Research">
          <i class="fa"></i>

    Research          <span class="caret"></span>
          </a>
  <div  data-class="" data-width="" class="tb-megamenu-submenu dropdown-menu mega-dropdown-menu nav-child">
  <div class="mega-dropdown-inner">
    <div  class="tb-megamenu-row row-fluid">
  <div  data-class="" data-width="12" data-hidewcol="0" id="tb-megamenu-column-2" class="tb-megamenu-column span12  mega-col-nav">
  <div class="tb-megamenu-column-inner mega-inner clearfix">
        <ul  class="tb-megamenu-subnav mega-nav level-1 items-5">
  <li  data-id="218" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="/"  title="KnoWhys">

    KnoWhys          </a>
  </li>

<li  data-id="1779" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://evidencecentral.org/recency"  title="Evidence Central">

    Evidence Central          </a>
  </li>

<li  data-id="530" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://archive.bookofmormoncentral.org"  title="Archive">

    Archive          </a>
  </li>

<li  data-id="1286" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/questions-answers"  title="Q&amp;A">

    Q&A          </a>
  </li>

<li  data-id="1731" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/content/additional-book-of-mormon-study-resources"  title="Additional Book of Mormon Study Resources">

    Additional Book of Mormon Study Resources          </a>
  </li>
</ul>
  </div>
</div>
</div>
  </div>
</div>
</li>

<li  data-id="1751" data-level="1" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="center" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-1 mega mega-align-center dropdown">
  <a href="https://bookofmormoncentral.org/content/media"  class="dropdown-toggle" title="Media">

    Media          <span class="caret"></span>
          </a>
  <div  data-class="" data-width="" class="tb-megamenu-submenu dropdown-menu mega-dropdown-menu nav-child">
  <div class="mega-dropdown-inner">
    <div  class="tb-megamenu-row row-fluid">
  <div  data-class="" data-width="12" data-hidewcol="0" id="tb-megamenu-column-3" class="tb-megamenu-column span12  mega-col-nav">
  <div class="tb-megamenu-column-inner mega-inner clearfix">
        <ul  class="tb-megamenu-subnav mega-nav level-1 items-3">
  <li  data-id="1752" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://www.youtube.com/channel/UCSsrx8lFpeuBjNIE7FNm2CQ/"  title="Videos">

    Videos          </a>
  </li>

<li  data-id="1754" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/content/scripture-central-podcasts"  title="Podcasts">

    Podcasts          </a>
  </li>

<li  data-id="1753" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://archive.bookofmormoncentral.org/category/media"  title="Artwork">

    Artwork          </a>
  </li>
</ul>
  </div>
</div>
</div>
  </div>
</div>
</li>

<li  data-id="776" data-level="1" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="center" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-1 mega mega-align-center dropdown">
  <a href="#"  class="dropdown-toggle" title="About">

    About          <span class="caret"></span>
          </a>
  <div  data-class="" data-width="" class="tb-megamenu-submenu dropdown-menu mega-dropdown-menu nav-child">
  <div class="mega-dropdown-inner">
    <div  class="tb-megamenu-row row-fluid">
  <div  data-class="" data-width="12" data-hidewcol="0" id="tb-megamenu-column-4" class="tb-megamenu-column span12  mega-col-nav">
  <div class="tb-megamenu-column-inner mega-inner clearfix">
        <ul  class="tb-megamenu-subnav mega-nav level-1 items-3">
  <li  data-id="341" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/about"  title="About BMC">

    About BMC          </a>
  </li>

<li  data-id="1142" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/blog"  title="BMC Blog">

    BMC Blog          </a>
  </li>

<li  data-id="846" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/events"  title="Events">

    Events          </a>
  </li>
</ul>
  </div>
</div>
</div>
  </div>
</div>
</li>

<li  data-id="1744" data-level="1" data-type="menu_item" data-class="hidden-menu-item" data-xicon="fa fa-th" data-caption="" data-alignsub="right" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-1 mega hidden-menu-item mega-align-right dropdown">
  <a href="#"  class="dropdown-toggle" title=".">
          <i class="fa fa-th"></i>

    .          <span class="caret"></span>
          </a>
  <div  data-class="" data-width="275" style="width: 275px;" class="tb-megamenu-submenu dropdown-menu mega-dropdown-menu nav-child">
  <div class="mega-dropdown-inner">
    <div  class="tb-megamenu-row row-fluid">
  <div  data-class="" data-width="12" data-hidewcol="0" id="tb-megamenu-column-6" class="tb-megamenu-column span12  mega-col-nav">
  <div class="tb-megamenu-column-inner mega-inner clearfix">
        <ul  class="tb-megamenu-subnav mega-nav level-1 items-1">
  <li  data-id="1750" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="1" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega mega-group">
  <a href="#"  class="mega-group-title" title="BMC Projects">

    BMC Projects          <span class="caret"></span>
          </a>
  <div  data-class="" data-width="" class="tb-megamenu-submenu mega-group-ct nav-child">
  <div class="mega-dropdown-inner">
    <div  class="tb-megamenu-row row-fluid">
  <div  data-class="" data-width="12" data-hidewcol="0" id="tb-megamenu-column-5" class="tb-megamenu-column span12  mega-col-nav">
  <div class="tb-megamenu-column-inner mega-inner clearfix">
        <ul  class="tb-megamenu-subnav mega-nav level-2 items-11">
  <li  data-id="1745" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://centralldm.es/"  title="BMC en Español">

    BMC en Español          </a>
  </li>

<li  data-id="1755" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://www.youtube.com/channel/UCoreu97W5GDPsIFGm7HBJhg"  title="BMC em Português">

    BMC em Português          </a>
  </li>

<li  data-id="1746" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://www.scriptureplus.org/"  title="ScripturePlus">

    ScripturePlus          </a>
  </li>

<li  data-id="1757" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://doctrineandcovenantscentral.org/"  title="Doctrine and Covenants Central">

    Doctrine and Covenants Central          </a>
  </li>

<li  data-id="1747" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://www.pearlofgreatpricecentral.org/"  title="Pearl of Great Price Central">

    Pearl of Great Price Central          </a>
  </li>

<li  data-id="1748" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://evidencecentral.org/#/landing"  title="Evidence Central">

    Evidence Central          </a>
  </li>

<li  data-id="1749" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="http://especiallyforseminary.org/"  title="Seminary Central">

    Seminary Central          </a>
  </li>

<li  data-id="1756" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://www.youtube.com/user/messagesofChrist"  title="Messages of Christ">

    Messages of Christ          </a>
  </li>

<li  data-id="1758" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://centraldyc.es/"  title="Central de Doctrina y Convenios">

    Central de Doctrina y Convenios          </a>
  </li>

<li  data-id="1759" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://centralpgp.es/"  title="Perla de Gran Precio">

    Perla de Gran Precio          </a>
  </li>

<li  data-id="1760" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://geografia.centralldm.es/"  title="Geografía del Libro de Mormón">

    Geografía del Libro de Mormón          </a>
  </li>
</ul>
  </div>
</div>
</div>
  </div>
</div>
</li>
</ul>
  </div>
</div>
</div>
  </div>
</div>
</li>

<li  data-id="1739" data-level="1" data-type="menu_item" data-class="btn btn-primary donate-menu-item" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-1 mega btn btn-primary donate-menu-item">
  <a href="https://bookofmormoncentral.org/content/donate"  title="Donate">

    Donate          </a>
  </li>
</ul>
      </div>
  </div>

</section>
  </div>
                  </nav>
      </div>
      </div>
</header>

<div class="main-container container">

  <header role="banner" id="page-header">

      <div class="region region-header">
    <section id="block-menu-menu-knowhy-menu" class="block block-menu sub-menu clearfix">

        <h2 class="block-title">KnoWhy</h2>

  <ul class="menu nav"><li class="first leaf"><a href="/reference-knowhy" title="">All KnoWhys</a></li>
<li class="leaf"><a href="/knowhy-scriptures" title="">Scripture Filter</a></li>
<li class="leaf"><a href="/subject-index" title="">Subject Index</a></li>
<li class="last leaf"><a href="/content/why-knowhy" title="">About KnoWhys</a></li>
</ul>
</section>
  </div>
  </header> <!-- /#page-header -->

  <div class="row">


    <section class="col-sm-12">
            <h2 class="element-invisible">You are here</h2><div class="breadcrumb"><span class="inline odd first"><a href="https://bookofmormoncentral.org">Book of Mormon Central</a></span> <span class="delimiter">/</span> <span class="inline even last"><a href="/">KnoWhys</a></span></div>      <a id="main-content"></a>
                                                                <div class="region region-content">
    <section id="block-system-main" class="block block-system clearfix">


  <div  about="/knowhy/what-does-the-new-testament-teach-about-the-great-apostasy" typeof="sioc:Item foaf:Document" class="ds-2col-stacked node node-knowhy node-promoted view-mode-full  clearfix">


  <div class="group-header clearfix">
    <div class="field field-name-title field-type-ds field-label-hidden"><div class="field-items"><div class="field-item even" property="dc:title"><h1 class="page-title">What Does the New Testament Teach about the Great Apostasy?</h1></div></div></div><div class="field field-name-ds-user-picture field-type-ds field-label-hidden"><div class="field-items"><div class="field-item even"><img typeof="foaf:Image" class="img-responsive" src="https://knowhy.bookofmormoncentral.org/sites/default/files/styles/thumbnail/public/pictures/picture-139-1673300074.png?itok=N8CW5mHH" width="100" height="100" alt="Scripture Central&#039;s picture" title="Scripture Central&#039;s picture" /></div></div></div><div class="field-nam-author text-muted small">Post contributed by Scripture Central</div><div class="field-name-publish-date text-muted small">October 17, 2023</div><div class="field-name-field-knowhy-num text-muted small">KnoWhy #695</div>  </div>

  <div class="group-left">
    <div class="field field-name-field-image field-type-image field-label-hidden"><div class="field-items"><div class="field-item even"><a href="https://knowhy.bookofmormoncentral.org/sites/default/files/knowhy-img/2023/10/main/knowhy-695-what-does-new-testament-teach-about-great-apostasy-martyrdom-of-saint-matthew-caravaggio.jpg" rel="lightbox[field_image][&lt;div class=&quot;field field-name-field-file-image-alt-text field-type-text field-label-hidden&quot;&gt;&lt;div class=&quot;field-items&quot;&gt;&lt;div class=&quot;field-item even&quot;&gt;Detail from “The Martyrdom of Saint Matthew” by Michelangelo Merisi da Caravaggio. Public Domain Image&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;p&gt;&lt;a href=&quot;https://knowhy.bookofmormoncentral.org/sites/default/files/knowhy-img/2023/10/main/knowhy-695-what-does-new-testament-teach-about-great-apostasy-martyrdom-of-saint-matthew-caravaggio.jpg&quot; title=&quot;Download Image&quot; download=&quot;&quot;&gt;Download Image&lt;/a&gt;&lt;/p&gt;]" title="Detail from “The Martyrdom of Saint Matthew” by Michelangelo Merisi da Caravaggio. Public Domain Image"><img typeof="foaf:Image" class="img-responsive" src="https://knowhy.bookofmormoncentral.org/sites/default/files/knowhy-img/2023/10/main/knowhy-695-what-does-new-testament-teach-about-great-apostasy-martyrdom-of-saint-matthew-caravaggio.jpg" width="1920" height="1080" alt="Detail from “The Martyrdom of Saint Matthew” by Michelangelo Merisi da Caravaggio. Public Domain Image" title="Detail from “The Martyrdom of Saint Matthew” by Michelangelo Merisi da Caravaggio. Public Domain Image" /></a></div></div></div><div class="field-name-image-caption text-muted small"><section id="block-views-image-caption-block" class="block block-views clearfix">


  <div class="view view-image-caption view-id-image_caption view-display-id-block view-dom-id-29e44a45c665d968b409f912408056a6">



      <div class="view-content">
        <div>

          Detail from “The Martyrdom of Saint Matthew” by Michelangelo Merisi da Caravaggio. Public Domain Image    </div>
    </div>






</div>
</section>
</div><div class="field field-name-field-scripture-quote field-type-text-long field-label-hidden"><div class="field-items"><div class="field-item even">“Let no man deceive you by any means: for that day shall not come, except there come a falling away first, and that man of sin be revealed, the son of perdition.”</div></div></div><div class="field-name-field-scripture-reference"><h1 class="scripture">2 Thessalonians 2:3</h1></div><div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even" property="content:encoded"><h2>The Know</h2>
<p>In 1820, as Joseph Smith prayed in the Sacred Grove, he saw God the Father and His Son, Jesus Christ. Joseph, who had been struggling to know where he might find the true church, asked the divine personages “which of all the sects was right (for at this time it had never entered into my heart that all were wrong)—and which I should join” (Joseph Smith—History 1:18). The answer Joseph received came as a shock to him and would begin his preparation as a prophet: “I was answered that I must join none of them, for they were all wrong; and the Personage who addressed me said that all their creeds were an abomination in his sight” (Joseph Smith—History 1:19). Because of this, Joseph Smith would be called of God to restore His Church on the earth.</p>
<p>The belief in the Great Apostasy is central to Latter-day Saint teachings—that is, that there was an actual falling away from the gospel as originally taught by Jesus Christ and His Apostles, therefore necessitating a restoration. While this may appear to be a bold claim, closer review of the New Testament shows that the Apostles knew of the forthcoming Apostasy and warned the Church extensively against the false teachers that would come in its wake.</p>
<p>The word <em>apostasy</em> comes from the Greek word <em>apostasia</em>, which literally means “rebellion” and in the New Testament connotes a people rebelling from God.<a class="see-footnote" id="footnoteref1_o76oe6r" title="See James E. Faulconer, “The Concept of the Apostasy in the New Testament,” in Early Christians in Disarray: Contemporary LDS Perspectives on the Christian Apostasy, ed. Noel B. Reynolds (Provo, UT: Foundation for Ancient Research and Mormon Studies [FARMS], 2005), 133–134." href="#footnote1_o76oe6r">1</a> However, the meaning of this word is unfortunately often masked in translations into English. For example, the King James Version of 2 Thessalonians 2:3 translates <em>apostasia</em> as “falling away”: “Let no man deceive you by any means: for that day shall not come, except there come a falling away first, and that man of sin be revealed, the son of perdition.”<a class="see-footnote" id="footnoteref2_e8iwokl" title="It is interesting to note that some second-century Christians recognized the state of the Church following the deaths of the Apostles. For example, citing this verse, Cyril of Jerusalem remarked, “Thus wrote Paul, and now is the falling away. For men have fallen away from the right faith. … And formerly the heretics were manifest; but now the Church is filled with heretics in disguise.” Cyril of Jerusalem, Catechetical Lectures 15:9." href="#footnote2_e8iwokl">2</a> While not always clear in translations of the Bible, the connotation of <em>apostasy</em> as a rebellion against God is clearly described in the Book of Mormon (see 3 Nephi 6:18; 4 Nephi 1:38).</p>
<p>Noel B. Reynolds has noted that in light of the evidence from the New Testament and based on the meaning of <em>apostasy</em> as “rebellion,” it is a myth that “the apostasy happened because of outside persecution.”<a class="see-footnote" id="footnoteref3_ld3k63b" title="Noel B. Reynolds, “Introduction: What Went Wrong for the Early Christians?,” in Early Christians in Disarray, 7." href="#footnote3_ld3k63b">3</a> Rather, the New Testament consistently describes the forthcoming Apostasy as an internal rebellion by members of the early Church against God and His chosen leaders—a rebellion that became more and more prominent as the Apostles wrote earnestly in hopes that the congregations might repent.<a class="see-footnote" id="footnoteref4_are7x7w" title="For a list and brief analysis of over forty New Testament scriptures discussing the apostasy of the early Christian Church, see Noel B. Reynolds, “Appendix C: New Testament Evidences and Prophecies of Apostasy in the First-Century Church,” in Early Christians in Disarray, 355–369." href="#footnote4_are7x7w">4</a></p>
<p>For example, when Paul was returning to Jerusalem from his third missionary journey, he warned the leaders of Ephesus, “After my departing shall grievous wolves enter in among you, not sparing the flock. Also of your own selves shall men arise, speaking perverse things, to draw away disciples after them” (Acts 20:29–30). While the Ephesian Saints were no stranger to persecution from the Greco-Roman world (see Acts 19:24–41), of much greater concern to Paul was that the Ephesian Saints remain loyal to the Lord and their covenants. Moreover, much of Paul’s epistles were written in part to correct false beliefs and attitudes that were arising in the various churches, just as he had foretold.<a class="see-footnote" id="footnoteref5_997m523" title="For a list of relevant passages from Paul’s epistles, see Reynolds, “Appendix C: New Testament Evidences,” 360–366." href="#footnote5_997m523">5</a></p>
<p>Shortly before he was executed under Nero’s command, Paul warned Timothy that the prophesied rebellion was then at hand, as many churches Paul established had forsaken him and the gospel: “All they which are in Asia be turned away from me; of whom are Phygellus and Hermogenes” (2 Timothy 1:15). This rebellion even reached some of Paul’s most trusted missionary companions: “Demas hath forsaken me, having loved this present world, and is departed unto Thessalonica; Crescens to Galatia, Titus unto Dalmatia. Only Luke is with me” (2 Timothy 4:10–11).</p>
<p>Unfortunately, this rebellion against the gospel would only grow worse, for “the time will come when they will not endure sound doctrine; but after their own lusts shall they heap to themselves teachers, having itching ears; and they shall turn away their ears from the truth, and shall be turned unto fables” (2 Timothy 4:3–4). Prophecies regarding the apostasy of the New Testament Church were even made by Jesus Christ Himself, such as in the parable of the wheat and the tares,<a class="see-footnote" id="footnoteref6_0xkdttz" title="See Book of Mormon Central, “What Does the Parable of the Wheat and Tares Teach about the Apostasy? (Matthew 13:24–25),” KnoWhy 660 (February 28, 2023); John W. Welch and Jeannie S. Welch, The Parables of Jesus: Revealing the Plan of Salvation (American Fork, UT: Covenant Communications, 2019), 60–67, 148–151." href="#footnote6_0xkdttz">6</a> and this no doubt influenced how His Apostles shaped their messages.<a class="see-footnote" id="footnoteref7_05bk94w" title="See, for example, Matthew 24:5, 24, in which Jesus warns about false prophets and false Christs who would deceive many people. It is also likely that the Apostasy was a key topic in Jesus’s forty-day ministry. See Book of Mormon Central, “What Might Jesus Have Taught His Apostles for Forty Days? (Acts 1:3),” KnoWhy 678 (July 4, 2023). Some interpreters have erroneously stated that Jesus’s bestowal of the keys to Peter as recorded in Matthew 16:18 demonstrates that Jesus taught there could be no apostasy. However, when read in its proper context, the gates of hell refer specifically to the realms of the dead—thus, Jesus taught that the priesthood authority given to the Apostles would be instrumental in the work of salvation for the dead through proxy ordinances (see Matthew 16:19). The idea that the gates of hell referred to Satan’s power and dominion (which led to the interpretation of Jesus promising the Church would not be overcome by apostasy) is a late addition to the text that would be entirely foreign to the New Testament Church. For a detailed discussion of the gates of hell in this context, see Hugh Nibley, “Baptism for the Dead in Ancient Times,” in Mormonism and Early Christianity (Provo, UT: FARMS; Salt Lake City, UT: Deseret Book, 1987), 105–109; see also Book of Mormon Central, “Why Are People Baptized for the Dead? (1 Corinthians 15:29),” KnoWhy 687 (September 5, 2023)." href="#footnote7_05bk94w">7</a></p>
<p>The concept of apostasy as a rebellion against the Lord has deep roots in Jewish and Christian tradition. Indeed, as James E. Faulconer has observed, both “faithfulness to God and apostasy from him are often spoken of in terms of covenant [throughout the Old Testament]. To be faithful is to keep covenant; to apostatize is to break covenant.”<a class="see-footnote" id="footnoteref8_4wy4d41" title="Faulconer, “Concept of the Apostasy,” 137." href="#footnote8_4wy4d41">8</a> Furthermore, in the Greek Septuagint the word <em>apostasia</em> is used to describe idolatry and forsaking the Lord. Similarly, the same word is used to describe divorce, especially when marriage was used as a metaphor for God’s covenant with Israel. Early Christian texts similarly describe the Apostasy as a corruption of priesthood leaders and a rejection of ordinances and covenants.<a class="see-footnote" id="footnoteref9_2zl1xhd" title="See Faulconer, “Concept of the Apostasy,” 137–138, 143–155. Examples of apostasiaas a description of forsaking the Lord include Joshua 22:22 and 2 Chronicles 29:19." href="#footnote9_2zl1xhd">9</a> As such, apostasy marks the loss of covenants and priesthood authority that can be restored only through a prophet of God.</p>
<h2>The Why</h2>
<p>While it is evident that the New Testament Apostles knew and warned others about the impending Apostasy, they knew that that was not the end of the story. As Peter told the Saints in Jerusalem, “the times of restitution of all things, which God hath spoken by the mouth of all his holy prophets since the world began,” would come (Acts 3:21). This restitution of all things was begun by God the Father and Jesus Christ through the Prophet Joseph Smith.</p>
<p>As Faulconer explained, “We cannot understand what apostasy means for New Testament Christians without understanding that it included the loss of the temple and, so, of the priesthood, for ultimately the rebellion of apostasy involves severing one’s covenant relation to God, a relation manifest through the priesthood, through standing in the presence of God.”<a class="see-footnote" id="footnoteref10_r06qwgu" title="Faulconer, “Concept of the Apostasy,” 162." href="#footnote10_r06qwgu">10</a> A serious part of the Restoration entailed restoring covenants and temples, thereby providing a corrective course to this rebellion that corrupted many early Christian doctrines and beliefs. Covenants are essential to the gospel of Jesus Christ, and they allow us to grow closer to our Savior and become more like Him.</p>
<div class="further-reading">
<h2>Further Reading</h2>
<p>James E. Faulconer, “<a href="https://archive.bookofmormoncentral.org/content/concept-apostasy-new-testament">The Concept of the Apostasy in the New Testament</a>,” in <em>Early Christians in Disarray: Contemporary LDS Perspectives on the Christian Apostasy</em>, ed. Noel B. Reynolds (Provo, UT: Foundation for Ancient Research and Mormon Studies, 2005), 133–162.</p>
<p>Noel B. Reynolds, “<a href="https://archive.bookofmormoncentral.org/content/appendix-c-new-testament-evidences-and-prophecies-apostasy-first-century-church">Appendix C: New Testament Evidences and Prophecies of Apostasy in the First-Century Church</a>,” in <em>Early Christians in Disarray</em>, 355–369.</p>
<p>Kent P. Jackson, “<a href="https://rsc.byu.edu/sperry-symposium-classics-new-testament/new-testament-prophecies-apostasy">New Testament Prophecies of Apostasy</a>,” in <em>Sperry Symposium Classics: The New Testament</em>, ed. Frank F. Judd Jr. and Gaye Strathearn (Provo, UT: Religious Studies Center, Brigham Young University; Salt Lake City, UT: Deseret Book, 2006), 394–406.</p>
<p>Tad R. Callister, <em>The Inevitable Apostasy and the Promised Restoration </em>(Salt Lake City, UT: Deseret Book, 2006), 24–49.</p>
</div>
<ul class="footnotes"><li class="footnote" id="footnote1_o76oe6r"><a class="footnote-label" href="#footnoteref1_o76oe6r">1.</a> See James E. Faulconer, “<a href="https://archive.bookofmormoncentral.org/content/concept-apostasy-new-testament">The Concept of the Apostasy in the New Testament</a>,” in <em>Early Christians in Disarray: Contemporary LDS Perspectives on the Christian Apostasy</em>, ed. Noel B. Reynolds (Provo, UT: Foundation for Ancient Research and Mormon Studies [FARMS], 2005), 133–134.</li>
<li class="footnote" id="footnote2_e8iwokl"><a class="footnote-label" href="#footnoteref2_e8iwokl">2.</a> It is interesting to note that some second-century Christians recognized the state of the Church following the deaths of the Apostles. For example, citing this verse, Cyril of Jerusalem remarked, “Thus wrote Paul, and now is the falling away. For men have fallen away from the right faith. … And formerly the heretics were manifest; but now the Church is filled with heretics in disguise.” Cyril of Jerusalem, <em>Catechetical Lectures</em> 15:9.</li>
<li class="footnote" id="footnote3_ld3k63b"><a class="footnote-label" href="#footnoteref3_ld3k63b">3.</a> Noel B. Reynolds, “Introduction: What Went Wrong for the Early Christians?,” in <em>Early Christians in Disarray</em>, 7.</li>
<li class="footnote" id="footnote4_are7x7w"><a class="footnote-label" href="#footnoteref4_are7x7w">4.</a> For a list and brief analysis of over forty New Testament scriptures discussing the apostasy of the early Christian Church, see Noel B. Reynolds, “<a href="https://archive.bookofmormoncentral.org/content/appendix-c-new-testament-evidences-and-prophecies-apostasy-first-century-church">Appendix C: New Testament Evidences and Prophecies of Apostasy in the First-Century Church</a>,” in <em>Early Christians in Disarray</em>, 355–369.</li>
<li class="footnote" id="footnote5_997m523"><a class="footnote-label" href="#footnoteref5_997m523">5.</a> For a list of relevant passages from Paul’s epistles, see Reynolds, “<a href="https://archive.bookofmormoncentral.org/content/appendix-c-new-testament-evidences-and-prophecies-apostasy-first-century-church">Appendix C: New Testament Evidences</a>,” 360–366.</li>
<li class="footnote" id="footnote6_0xkdttz"><a class="footnote-label" href="#footnoteref6_0xkdttz">6.</a> See Book of Mormon Central, “<a href="https://knowhy.bookofmormoncentral.org/knowhy/what-does-the-parable-of-the-wheat-and-tares-teach-about-the-apostasy">What Does the Parable of the Wheat and Tares Teach about the Apostasy?</a> (Matthew 13:24–25),” <em>KnoWhy</em> 660 (February 28, 2023); John W. Welch and Jeannie S. Welch, <em>The Parables of Jesus: Revealing the Plan of Salvation</em> (American Fork, UT: Covenant Communications, 2019), 60–67, 148–151.</li>
<li class="footnote" id="footnote7_05bk94w"><a class="footnote-label" href="#footnoteref7_05bk94w">7.</a> See, for example, Matthew 24:5, 24, in which Jesus warns about false prophets and false Christs who would deceive many people. It is also likely that the Apostasy was a key topic in Jesus’s forty-day ministry. See Book of Mormon Central, “<a href="https://knowhy.bookofmormoncentral.org/knowhy/what-might-jesus-have-taught-his-apostles-for-forty-days">What Might Jesus Have Taught His Apostles for Forty Days?</a> (Acts 1:3),” <em>KnoWhy</em> 678 (July 4, 2023). Some interpreters have erroneously stated that Jesus’s bestowal of the keys to Peter as recorded in Matthew 16:18 demonstrates that Jesus taught there could be no apostasy. However, when read in its proper context, the gates of hell refer specifically to the realms of the dead—thus, Jesus taught that the priesthood authority given to the Apostles would be instrumental in the work of salvation for the dead through proxy ordinances (see Matthew 16:19). The idea that the gates of hell referred to Satan’s power and dominion (which led to the interpretation of Jesus promising the Church would not be overcome by apostasy) is a late addition to the text that would be entirely foreign to the New Testament Church. For a detailed discussion of the gates of hell in this context, see Hugh Nibley, “Baptism for the Dead in Ancient Times,” in <em>Mormonism and Early Christianity</em> (Provo, UT: FARMS; Salt Lake City, UT: Deseret Book, 1987), 105–109; see also Book of Mormon Central, “<a href="https://knowhy.bookofmormoncentral.org/knowhy/why-are-people-baptized-for-the-dead">Why Are People Baptized for the Dead?</a> (1 Corinthians 15:29),” <em>KnoWhy</em> 687 (September 5, 2023).</li>
<li class="footnote" id="footnote8_4wy4d41"><a class="footnote-label" href="#footnoteref8_4wy4d41">8.</a> Faulconer, “<a href="https://archive.bookofmormoncentral.org/content/concept-apostasy-new-testament">Concept of the Apostasy</a>,” 137.</li>
<li class="footnote" id="footnote9_2zl1xhd"><a class="footnote-label" href="#footnoteref9_2zl1xhd">9.</a> See Faulconer, “<a href="https://archive.bookofmormoncentral.org/content/concept-apostasy-new-testament">Concept of the Apostasy</a>,” 137–138, 143–155. Examples of <em>apostasia</em>as a description of forsaking the Lord include Joshua 22:22 and 2 Chronicles 29:19.</li>
<li class="footnote" id="footnote10_r06qwgu"><a class="footnote-label" href="#footnoteref10_r06qwgu">10.</a> Faulconer, “<a href="https://archive.bookofmormoncentral.org/content/concept-apostasy-new-testament">Concept of the Apostasy</a>,” 162.</li>
</ul></div></div></div>  </div>

  <div class="group-right">
    <div class="field field-name-social-media"><section id="block-service-links-service-links" class="block block-service-links clearfix">

        <h2 class="block-title">Share</h2>

  <div class="service-links"><ul><li><a href="https://knowhy.bookofmormoncentral.org/knowhy/what-does-the-new-testament-teach-about-the-great-apostasy" title="Plus it" class="service-links-google-plus-one" rel="nofollow" target="_blank"><span class="element-invisible">Google Plus One</span></a></li>
<li><a href="https://pinterest.com/pin/create/button/?url=https%3A//knowhy.bookofmormoncentral.org/knowhy/what-does-the-new-testament-teach-about-the-great-apostasy&amp;description=The%20Know%0D%0AIn%201820%2C%20as%20Joseph%20Smith%20prayed%20in%20the%20Sacred%20Grove%2C%20he%20saw%20God%20the%20Father%20and%20His%20Son%2C%20Jesus%20Christ.%20Joseph%2C%20who%20had%20been%20struggling%20to%20know%20where%20he%20might%20find%20the%20true%20church%2C%20asked%20the%20divine%20personages%20%26ldquo%3Bwhich%20of%20all%20the%20sects%20was%20right%20%28for%20at%20this%20time%20it%20had%20never%20entered%20into%20my%20heart%20that%20all%20were%20wrong%29%26mdash%3Band%20which%20I%20should%20join%26rdquo%3B%20%28Joseph%20Smith%26mdash%3BHistory%201%3A18%29.&amp;media=" class="pin-it-button service-links-pinterest-button" title="Pin It" rel="nofollow" target="_blank"><span class="element-invisible">Pinterest</span></a></li>
<li><a href="https://twitter.com/share?url=https%3A//knowhy.bookofmormoncentral.org/knowhy/what-does-the-new-testament-teach-about-the-great-apostasy&amp;count=horizontal&amp;via=&amp;text=What%20Does%20the%20New%20Testament%20Teach%20about%20the%20Great%20Apostasy%3F&amp;counturl=https%3A//knowhy.bookofmormoncentral.org/knowhy/what-does-the-new-testament-teach-about-the-great-apostasy" class="twitter-share-button service-links-twitter-widget" title="Tweet This" rel="nofollow" target="_blank"><span class="element-invisible">Tweet Widget</span></a></li>
<li><a href="https://www.facebook.com/sharer.php" title="Share this post on Facebook" class="service-links-facebook-share" rel="https://knowhy.bookofmormoncentral.org/knowhy/what-does-the-new-testament-teach-about-the-great-apostasy" target="_blank"><span class="element-invisible">Share on Facebook</span></a></li>
</ul></div>
</section>
</div><div class="field field-name-field-tags"><h2 class="label-above">Tags</h2><div class="field-items"><div class="field-item button tag"><a href="/tags/apostasy" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">Apostasy</a></div><div class="field-item button tag"><a href="/tags/new-testament" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">New Testament</a></div><div class="field-item button tag"><a href="/tags/2-thessalonians" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">2 Thessalonians</a></div><div class="field-item button tag"><a href="/tags/paul" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">Paul</a></div><div class="field-item button tag"><a href="/tags/early-christian-church" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">Early Christian Church</a></div><div class="field-item button tag"><a href="/tags/restoration" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">Restoration</a></div></div></div><div class="field field-name-sidebar-ad field-type-ds field-label-hidden"><div class="field-items"><div class="field-item even"><section id="block-block-6" class="block block-block clearfix">


  <p><a href="https://www.scriptureplus.org/" target="_blank"><img alt="Display ad for ScripturePlus app by Book of Mormon Central" src="/sites/default/files/knowhy-img/users/user19/splus-300x600.jpg" style="width: 400px;" /></a></p>

</section>
</div></div></div><div class="field-name-knowhy-citation"><div class="field-item small"><section id="block-views-knowhy-citation-block" class="block block-views clearfix">

        <h2 class="block-title">KnoWhy Citation</h2>

  <div class="view view-knowhy-citation view-id-knowhy_citation view-display-id-block view-dom-id-16ce452ef6c2dc387390b88b301e6861">



      <div class="view-content">
        <div class="views-row views-row-1 views-row-odd views-row-first views-row-last">

  <div class="views-field views-field-nothing">        <span class="field-content">Book of Mormon Central, &ldquo;<a href="/knowhy/what-does-the-new-testament-teach-about-the-great-apostasy" class="active">What Does the New Testament Teach about the Great Apostasy?</a> (2 Thessalonians 2:3),&rdquo; <em>KnoWhy</em> 695 (October 17, 2023).</span>  </div>  </div>
    </div>






</div>
</section>
</div></div><div class="field-name-other"><div class="field-label"><h2 class="label-above">Related KnoWhys</h2></div><div class="field-item"><section id="block-views-date-knowhy-block-1" class="block block-views clearfix">


  <div class="view view-date-knowhy view-id-date_knowhy view-display-id-block_1 view-dom-id-c6fd75e9df9d06cae319cb335e66c9f6">



      <div class="view-content">
        <div class="views-row views-row-1 views-row-odd views-row-first card">

  <div class="views-field views-field-field-image">        <div class="field-content"><a href="/knowhy/why-does-paul-quote-from-an-early-christian-hymn"><img typeof="foaf:Image" class="img-responsive" src="https://knowhy.bookofmormoncentral.org/sites/default/files/styles/knowhy_card/public/knowhy-img/2023/10/main/knowhy-694-brescia-casket-lid-early-christian-art-hymn-paul-quote.jpg?itok=u-9L0KIW" width="300" height="150" alt="Detail from the lid of the Brescia Casket, a carved ivory box from the late 4th century, depicts scenes from the life of Christ, including the arrest in the Garden of Gethsemane and judgment before Pilate. Public Domain Image" title="Detail from the lid of the Brescia Casket, a carved ivory box from the late 4th century, depicts scenes from the life of Christ, including the arrest in the Garden of Gethsemane and judgment before Pilate. Public Domain Image" /></a></div>  </div>
  <div class="views-field views-field-nothing">        <span class="field-content"><div class="card-text">
<div class="field-title"><a href="/knowhy/why-does-paul-quote-from-an-early-christian-hymn">Why Does Paul Quote from an Early Christian Hymn?</a></div>
<div class="field-created overline">October 12, 2023</div>
</div></span>  </div>  </div>
  <div class="views-row views-row-2 views-row-even card">

  <div class="views-field views-field-field-image">        <div class="field-content"><a href="/knowhy/how-often-do-the-articles-of-faith-track-sayings-of-paul"><img typeof="foaf:Image" class="img-responsive" src="https://knowhy.bookofmormoncentral.org/sites/default/files/styles/knowhy_card/public/knowhy-img/2023/10/main/knowhy-693-paul-preaches-peter-john-bible-videos-articles-of-faith.jpg?itok=5rBfKwn2" width="300" height="150" alt="Paul preaches to a crowd with Peter and John. Image from the Bible Videos of The Church of Jesus Christ of Latter-day Saints" title="Paul preaches to a crowd with Peter and John. Image from the Bible Videos of The Church of Jesus Christ of Latter-day Saints" /></a></div>  </div>
  <div class="views-field views-field-nothing">        <span class="field-content"><div class="card-text">
<div class="field-title"><a href="/knowhy/how-often-do-the-articles-of-faith-track-sayings-of-paul">How Often Do the Articles of Faith Track Sayings of Paul?</a></div>
<div class="field-created overline">October 10, 2023</div>
</div></span>  </div>  </div>
  <div class="views-row views-row-3 views-row-odd views-row-last card">

  <div class="views-field views-field-field-image">        <div class="field-content"><a href="/knowhy/what-is-an-evangelist"><img typeof="foaf:Image" class="img-responsive" src="https://knowhy.bookofmormoncentral.org/sites/default/files/styles/knowhy_card/public/knowhy-img/2023/10/main/knowhy-692-evangelist-patriarch-four-evangelists-jacob-jordaens.jpeg?itok=39vma7up" width="300" height="150" alt="“Four Evangelists,” by Jacob Jordaens, depicts the writers of the four gospels, Matthew, Mark, Luke, and John. Public Domain Image." title="“Four Evangelists,” by Jacob Jordaens, depicts the writers of the four gospels, Matthew, Mark, Luke, and John. Public Domain Image." /></a></div>  </div>
  <div class="views-field views-field-nothing">        <span class="field-content"><div class="card-text">
<div class="field-title"><a href="/knowhy/what-is-an-evangelist">What Is an Evangelist?</a></div>
<div class="field-created overline">October 5, 2023</div>
</div></span>  </div>  </div>
    </div>






</div>
</section>
</div></div><div class="field field-name-support-block field-type-ds field-label-hidden"><div class="field-items"><div class="field-item even"><section id="block-block-3" class="block block-block clearfix">


  <div class="subscribe-block">
<h2>
		Subscribe<br /></h2>
<p>
		Get the latest updates on Book of Mormon topics and research for free
	</p>
<!-- AWeber Web Form Generator 3.0.1 --><!--<style type="text/css"><p>#af-form-1645019532 .af-body .af-textWrap, #af-form-1645019532 .af-body .af-selectWrap{width:98%;display:block;float:none;}<br />
#af-form-1645019532 .af-body .privacyPolicy{color:#CCCCCC;font-size:11px;font-family:Verdana, sans-serif;}<br />
#af-form-1645019532 .af-body a{color:#CCCCCC;text-decoration:underline;font-style:normal;font-weight:normal;}<br />
#af-form-1645019532 .af-body input.text, #af-form-1645019532 .af-body textarea{background-color:#FFFFFF;border-color:#D9D9D9;border-width:1px;border-style:solid;color:#C7C7C7;text-decoration:none;font-style:normal;font-weight:normal;font-size:24px;font-family:Trebuchet MS, sans-serif;}<br />
#af-form-1645019532 .af-body input.text:focus, #af-form-1645019532 .af-body textarea:focus{background-color:#FFFAD6;border-color:#030303;border-width:1px;border-style:solid;}<br />
#af-form-1645019532 .af-body label.previewLabel{display:block;float:none;text-align:left;width:auto;color:#59473E;text-decoration:none;font-style:normal;font-weight:normal;font-size:24px;font-family:Helvetica, sans-serif;}<br />
#af-form-1645019532 .af-body{padding-bottom:15px;padding-top:15px;background-repeat:no-repeat;background-position:inherit;background-image:none;color:#CCCCCC;font-size:11px;font-family:Verdana, sans-serif;}<br />
#af-form-1645019532 .af-footer{padding-bottom:0px;padding-top:0px;padding-right:15px;padding-left:15px;background-color:#FFFFFF;background-repeat:no-repeat;background-position:top left;background-image:none;border-width:1px;border-bottom-style:none;border-left-style:none;border-right-style:none;border-top-style:none;color:#CCCCCC;font-size:12px;font-family:Verdana, sans-serif;}<br />
#af-form-1645019532 .af-quirksMode .bodyText{padding-top:2px;padding-bottom:2px;}<br />
#af-form-1645019532 .af-quirksMode{padding-right:60px;padding-left:60px;}<br />
#af-form-1645019532 .af-standards .af-element{padding-right:60px;padding-left:60px;}<br />
#af-form-1645019532 .bodyText p{margin:1em 0;}<br />
#af-form-1645019532 .buttonContainer input.submit{background-image:url("https://forms.aweber.com/images/auto/gradient/button/543.png");background-position:top left;background-repeat:repeat-x;background-color:#352413;border:1px solid #352413;color:#FFFFFF;text-decoration:none;font-style:normal;font-weight:normal;font-size:24px;font-family:Helvetica, sans-serif;}<br />
#af-form-1645019532 .buttonContainer input.submit{width:auto;}<br />
#af-form-1645019532 .buttonContainer{text-align:center;}<br />
#af-form-1645019532 body,#af-form-1645019532 dl,#af-form-1645019532 dt,#af-form-1645019532 dd,#af-form-1645019532 h1,#af-form-1645019532 h2,#af-form-1645019532 h3,#af-form-1645019532 h4,#af-form-1645019532 h5,#af-form-1645019532 h6,#af-form-1645019532 pre,#af-form-1645019532 code,#af-form-1645019532 fieldset,#af-form-1645019532 legend,#af-form-1645019532 blockquote,#af-form-1645019532 th,#af-form-1645019532 td{float:none;color:inherit;position:static;margin:0;padding:0;}<br />
#af-form-1645019532 button,#af-form-1645019532 input,#af-form-1645019532 submit,#af-form-1645019532 textarea,#af-form-1645019532 select,#af-form-1645019532 label,#af-form-1645019532 optgroup,#af-form-1645019532 option{float:none;position:static;margin:0;}<br />
#af-form-1645019532 div{margin:0;}<br />
#af-form-1645019532 fieldset{border:0;}<br />
#af-form-1645019532 form,#af-form-1645019532 textarea,.af-form-wrapper,.af-form-close-button,#af-form-1645019532 img{float:none;color:inherit;position:static;background-color:none;border:none;margin:0;padding:0;}<br />
#af-form-1645019532 input,#af-form-1645019532 button,#af-form-1645019532 textarea,#af-form-1645019532 select{font-size:100%;}<br />
#af-form-1645019532 p{color:inherit;}<br />
#af-form-1645019532 select,#af-form-1645019532 label,#af-form-1645019532 optgroup,#af-form-1645019532 option{padding:0;}<br />
#af-form-1645019532 table{border-collapse:collapse;border-spacing:0;}<br />
#af-form-1645019532 ul,#af-form-1645019532 ol{list-style-image:none;list-style-position:outside;list-style-type:disc;padding-left:40px;}<br />
#af-form-1645019532,#af-form-1645019532 .quirksMode{width:100%;max-width:418px;}<br />
#af-form-1645019532.af-quirksMode{overflow-x:hidden;}<br />
#af-form-1645019532{background-color:#FFFFFF;border-color:#CFCFCF;border-width:1px;border-style:none;}<br />
#af-form-1645019532{display:block;}<br />
#af-form-1645019532{overflow:hidden;}<br />
.af-body .af-textWrap{text-align:left;}<br />
.af-body input.image{border:none!important;}<br />
.af-body input.submit,.af-body input.image,.af-form .af-element input.button{float:none!important;}<br />
.af-body input.submit{white-space:inherit;}<br />
.af-body input.text{width:100%;float:none;padding:2px!important;}<br />
.af-body.af-standards input.submit{padding:4px 12px;}<br />
.af-clear{clear:both;}<br />
.af-element label{text-align:left;display:block;float:left;}<br />
.af-element{padding-bottom:5px;padding-top:5px;}<br />
.af-footer{margin-bottom:0;margin-top:0;padding:10px;}<br />
.af-form-wrapper{text-indent:0;}<br />
.af-form{box-sizing:border-box;text-align:left;margin:auto;}<br />
.af-quirksMode .af-element{padding-left:0!important;padding-right:0!important;}<br />
.lastNameContainer{margin-top:10px;}<br />
.lbl-right .af-element label{text-align:right;}<br />
body {<br />
}</p>
</style><p>-->
<style type="text/css">
<!--/*--><![CDATA[/* ><!--*/
.af-element.af-element-checkbox {text-align: left;}
.af-element.af-element-checkbox .checkbox {display: inline-block;margin: 0 10px 0 0;}
.checkbox-list {}
.af-element .bodyText p {text-align: left; margin: 0; font-weight: bold;}
.af-form-wrapper label {font-weight: normal; font-size: 0.9em;}

/*--><!]]>*/
</style><form accept-charset="UTF-8" action="https://www.aweber.com/scripts/addlead.pl" class="af-form-wrapper" method="post" target="_blank">
<div style="display: none;">
			<input name="meta_web_form_id" type="hidden" value="585301441" /><input name="meta_split_id" type="hidden" value="" /><input name="listname" type="hidden" value="awlist4130227" /><input id="redirect_5ccf2efe35be0c58cc7a4be6551e418a" name="redirect" type="hidden" value="https://www.aweber.com/thankyou-coi.htm?m=text" /><input name="meta_adtracking" type="hidden" value="Daily/Weekly_E-Mail_(Simplified_Update)" /><input name="meta_message" type="hidden" value="1" /><input name="meta_required" type="hidden" value="name (awf_first),name (awf_last),email" /><input name="meta_tooltip" type="hidden" value="name||Full Name" /></div>
<div class="af-form" id="af-form-585301441">
<div class="af-body af-standards" id="af-body-585301441">
<!--
					<div class="af-element" style="text-align: Center;"><p>						<img alt="" src="https://hostedimages-cdn.aweber-static.com/MTAxMzc1NA==/optimized/e753c8f220394e26a7d1fbbc4b1c5b70.png" style="max-width:100%;" /></p>
<div class="af-clear">
							&nbsp;
						</div>
</div>
<p>-->
<div class="af-element">
<!--<label class="previewLabel" for="awf_field-114031221-first">First Name:</label>--><div class="af-textWrap">
						<input class="text" id="awf_field-114031221-first" name="name (awf_first)" onblur="if (this.value == '') { this.value='';} " onfocus=" if (this.value == '') { this.value = ''; }" placeholder="First Name" tabindex="500" type="text" value="" /></div>
<div class="af-clear">

					</div>
</div>
<div class="af-element">
<!--<label class="previewLabel" for="awf_field-114031221-last">Last Name:</label>--><div class="af-textWrap">
						<input class="text" id="awf_field-114031221-last" name="name (awf_last)" onblur="if (this.value == '') { this.value='';} " onfocus=" if (this.value == '') { this.value = ''; }" placeholder="Last Name" tabindex="501" type="text" value="" /></div>
<div class="af-clear">

					</div>
</div>
<div class="af-element">
<!--<label class="previewLabel" for="awf_field-114031222">E-Mail:</label>--><div class="af-textWrap">
						<input class="text" id="awf_field-114031222" name="email" onblur="if (this.value == '') { this.value='';} " onfocus=" if (this.value == '') { this.value = ''; }" placeholder="Email" tabindex="502" type="text" value="" /></div>
<div class="af-clear">

					</div>
</div>
<!--<div class="af-divider" style="border-bottom: 1px dotted #000000;"><p>							&nbsp;
						</div>
<p>-->
<div class="af-element">
<div class="bodyText">
<p>
							Which lists would you like emails from?
						</p>
</div>
<div class="af-clear">

					</div>
</div>
<div class="checkbox-list">
<div class="af-element af-element-checkbox">
<div class="af-checkWrap">
							<input class="checkbox" id="awf_field-114031225" name="custom Book of Mormon Central Daily" tabindex="503" type="checkbox" value="yes" /><label class="choice" for="awf_field-114031225">Daily Email</label> <input name="tagif_custom Book of Mormon Central Daily" type="hidden" value="bmcdailysubscribe" /></div>
<div class="af-clear">

						</div>
</div>
<div class="af-element af-element-checkbox">
<div class="af-checkWrap">
							<input class="checkbox" id="awf_field-114031226" name="custom Book of Mormon Central Weekly" tabindex="504" type="checkbox" value="yes" /><label class="choice" for="awf_field-114031226">Weekly Email</label> <input name="tagif_custom Book of Mormon Central Weekly" type="hidden" value="bmcweeklysubscribe" /></div>
<div class="af-clear">

						</div>
</div>
</div>
<div class="af-element buttonContainer">
					<input class="submit" name="submit" tabindex="505" type="submit" value="Submit" /><div class="af-clear">

					</div>
</div>
<div class="af-element privacyPolicy" style="text-align: center">
<p>
						Signing up for both the Daily and Weekly email lists is not recommended, as you will receive duplicate emails.
					</p>
<p>
						We respect your <a href="https://www.aweber.com/permission.htm" rel="nofollow" target="_blank" title="Privacy Policy">email privacy</a>
					</p>
<div class="af-clear">

					</div>
</div>
</div>
<div class="af-footer" id="af-footer-585301441">
<div class="bodyText">
<p>

					</p>
</div>
</div>
</div>
<div style="display: none;">
			<img alt="" src="https://forms.aweber.com/form/displays.htm?id=rByszAyMLCyM" /></div>
</form>
<script type="text/javascript">
<!--//--><![CDATA[// ><!--

// Special handling for in-app browsers that don't always support new windows
(function() {
    function browserSupportsNewWindows(userAgent) {
        var rules = [
            'FBIOS',
            'Twitter for iPhone',
            'WebView',
            '(iPhone|iPod|iPad)(?!.*Safari\\/)',
            'Android.*(wv|\\.0\\.0\\.0)'
        ];
        var pattern = new RegExp('(' + rules.join('|') + ')', 'ig');
        return !pattern.test(userAgent);
    }

    if (!browserSupportsNewWindows(navigator.userAgent || navigator.vendor || window.opera)) {
        document.getElementById('af-form-585301441').parentElement.removeAttribute('target');
    }
})();

//--><!]]>
</script><script type="text/javascript">
<!--//--><![CDATA[// ><!--

    <!--
    (function() {
        var IE = /*@cc_on!@*/false;
        if (!IE) { return; }
        if (document.compatMode && document.compatMode == 'BackCompat') {
            if (document.getElementById("af-form-585301441")) {
                document.getElementById("af-form-585301441").className = 'af-form af-quirksMode';
            }
            if (document.getElementById("af-body-585301441")) {
                document.getElementById("af-body-585301441").className = "af-body inline af-quirksMode";
            }
            if (document.getElementById("af-header-585301441")) {
                document.getElementById("af-header-585301441").className = "af-header af-quirksMode";
            }
            if (document.getElementById("af-footer-585301441")) {
                document.getElementById("af-footer-585301441").className = "af-footer af-quirksMode";
            }
        }
    })();
    -->

//--><!]]>
</script><!-- /AWeber Web Form Generator 3.0.1 --></div>

</section>
</div></div></div>  </div>

  <div class="group-footer">
    <ul class="flippy">

    <li class="prev">
              <a href="/knowhy/why-does-paul-quote-from-an-early-christian-hymn" title="‹ Previous KnoWhy">‹ Previous KnoWhy</a>          </li>

    <li class="next">
              <a href="/content/what-does-it-mean-be-martyr-1" title="Next KnoWhy ›">Next KnoWhy ›</a>          </li>
  </ul>

  </div>

</div>


</section>
  </div>
    </section>


  </div>
</div>

  <footer class="footer container">
      <div class="region region-footer">
    <section id="block-system-navigation" class="block block-system col-xs-12 col-md-8 block-menu clearfix">


  <ul class="menu nav"><li class="first expanded dropdown"><span title="" class="dropdown-toggle nolink" data-toggle="dropdown" tabindex="0">Site Links <span class="caret"></span></span><ul class="dropdown-menu"><li class="first leaf"><a href="https://bookofmormoncentral.org/about" title="">About</a></li>
<li class="leaf"><a href="https://bookofmormoncentral.org/contact" title="">Contact</a></li>
<li class="leaf"><a href="https://bookofmormoncentral.org/content/policies" title="">Policies</a></li>
<li class="leaf"><a href="https://bookofmormoncentral.org/content/affiliates" title="">Affiliates</a></li>
<li class="last leaf"><a href="https://bookofmormoncentral.org/sitemap.xml" title="">Sitemap</a></li>
</ul></li>
<li class="last expanded dropdown"><span title="" class="dropdown-toggle nolink" data-toggle="dropdown" tabindex="0">Support <span class="caret"></span></span><ul class="dropdown-menu"><li class="first leaf"><a href="https://bookofmormoncentral.org/donate" title="">Donate</a></li>
<li class="leaf"><a href="https://bookofmormoncentral.org/content/donation-instructions" title="">Donor FAQ</a></li>
<li class="last leaf"><a href="https://bookofmormoncentral.org/content/subscribe" title="">Subscribe</a></li>
</ul></li>
</ul>
</section>
<section id="block-block-4" class="block block-block col-xs-12 col-md-4 clearfix">

        <h2 class="block-title">Our Vision</h2>

  <p>We build enduring faith in Jesus Christ by making the Book of Mormon accessible, comprehensible, and defensible to the entire world.</p>

</section>
<section id="block-social-media-links-social-media-links" class="block block-social-media-links clearfix">


  <ul class="social-media-links platforms inline horizontal"><li  class="facebook first"><a href="https://www.facebook.com/bookofmormoncentral/" title="Facebook"><img src="https://knowhy.bookofmormoncentral.org/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/facebook.png" alt="Facebook icon" /></a></li><li  class="twitter"><a href="http://www.twitter.com/bofmcentral" title="Twitter"><img src="https://knowhy.bookofmormoncentral.org/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/twitter.png" alt="Twitter icon" /></a></li><li  class="instagram"><a href="http://www.instagram.com/bookofmormoncentral/" title="Instagram"><img src="https://knowhy.bookofmormoncentral.org/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/instagram.png" alt="Instagram icon" /></a></li><li  class="pinterest"><a href="http://www.pinterest.com/BofMCentral" title="Pinterest"><img src="https://knowhy.bookofmormoncentral.org/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/pinterest.png" alt="Pinterest icon" /></a></li><li  class="vimeo"><a href="http://www.vimeo.com/bookofmormoncentral" title="Vimeo"><img src="https://knowhy.bookofmormoncentral.org/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/vimeo.png" alt="Vimeo icon" /></a></li><li  class="youtube_channel last"><a href="http://www.youtube.com/channel/UCSsrx8lFpeuBjNIE7FNm2CQ" title="Youtube (Channel)"><img src="https://knowhy.bookofmormoncentral.org/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/youtube.png" alt="Youtube (Channel) icon" /></a></li></ul>
</section>
  </div>
    <div class="copyright">Copyright 2023 Book of Mormon Central: A Non-Profit Organization. All rights reserved.<br />Registered 501(c)(3). EIN: 20-5294264</div>
  </footer>

<script>
  new WOW().init();
</script>  <script src="https://knowhy.bookofmormoncentral.org/sites/all/themes/bootstrap/js/bootstrap.js?rt4781"></script>
</body>
</html>
"""


def test_load_knowhy() -> None:
    """It returns a valid Document for a conference talk."""
    url = "https://knowhy.bookofmormoncentral.org/knowhy/what-does-the-new-testament-teach-about-the-great-apostasy"
    result = load_know.load_knowhy(url, html)
    assert len(result.page_content) > 0
    assert result.metadata["url"] == url
    assert result.metadata["title"] == "What Does the New Testament Teach about the Great Apostasy?"
    assert result.metadata["author"] == "Scripture Central"
    assert result.metadata["date"] == "October 17, 2023"
    assert "#footnoteref" not in result.page_content
