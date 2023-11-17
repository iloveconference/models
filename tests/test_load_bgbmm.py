"""Test cases for bgbmm module."""
# flake8: noqa

from models.load_bgbmm import load_bgbmm


html = """


<!DOCTYPE html>
<html lang="en" dir="ltr" prefix="og: http://ogp.me/ns# content: http://purl.org/rss/1.0/modules/content/ dc: http://purl.org/dc/terms/ foaf: http://xmlns.com/foaf/0.1/ rdfs: http://www.w3.org/2000/01/rdf-schema# sioc: http://rdfs.org/sioc/ns# sioct: http://rdfs.org/sioc/types# skos: http://www.w3.org/2004/02/skos/core# xsd: http://www.w3.org/2001/XMLSchema#">
<head>
  <link rel="profile" href="http://www.w3.org/1999/xhtml/vocab" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="shortcut icon" href="https://archive.bookofmormoncentral.org/sites/all/themes/archive_subtheme/favicon.ico" type="image/vnd.microsoft.icon" />
<meta name="generator" content="Drupal 7 (https://www.drupal.org)" />
<link rel="canonical" href="https://archive.bookofmormoncentral.org/content/1-nephi-1" />
<link rel="shortlink" href="https://archive.bookofmormoncentral.org/node/11936" />
<meta property="og:site_name" content="Book of Mormon Central" />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://archive.bookofmormoncentral.org/content/1-nephi-1" />
<meta property="og:title" content="1 Nephi 1" />
<meta property="og:updated_time" content="2023-10-03T11:29:18-06:00" />
<meta property="og:image:url" content="https://archive.bookofmormoncentral.org/sites/default/files/img/archive-header.jpg" />
<meta property="article:published_time" content="2023-10-03T11:28:52-06:00" />
<meta property="article:modified_time" content="2023-10-03T11:29:18-06:00" />
  <title>1 Nephi 1 | Book of Mormon Central</title>
  <link type="text/css" rel="stylesheet" href="https://archive.bookofmormoncentral.org/sites/default/files/css/css_lQaZfjVpwP_oGNqdtWCSpJT1EMqXdMiU84ekLLxQnc4.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://archive.bookofmormoncentral.org/sites/default/files/css/css_RK0sHeS3golzCjBeqM0XHWJwIKM0UX4uz6NDjTOEKMs.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://archive.bookofmormoncentral.org/sites/default/files/css/css_g_vBW1zlur6XpXGWQ0MquIbttxs0oGgmNc1oEkvxu40.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://archive.bookofmormoncentral.org/sites/default/files/css/css_fvXXP-wW03v1w_oX6VupTZvwB3EaV0yQ1DVeWMc_uZo.css" media="all" />
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

  <script defer="defer" src="https://archive.bookofmormoncentral.org/sites/default/files/google_tag/archive_of_book_of_mormon_central_ga4/google_tag.script.js?s3mzmc"></script>
<script src="https://archive.bookofmormoncentral.org/sites/all/modules/jquery_update/replace/jquery/1.10/jquery.min.js?v=1.10.2"></script>
<script src="https://archive.bookofmormoncentral.org/misc/jquery-extend-3.4.0.js?v=1.10.2"></script>
<script src="https://archive.bookofmormoncentral.org/misc/jquery-html-prefilter-3.5.0-backport.js?v=1.10.2"></script>
<script src="https://archive.bookofmormoncentral.org/misc/jquery.once.js?v=1.2"></script>
<script src="https://archive.bookofmormoncentral.org/misc/drupal.js?s3mzmc"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.js"></script>
<script src="https://archive.bookofmormoncentral.org/sites/all/modules/google_cse/google_cse.js?s3mzmc"></script>
<script src="https://archive.bookofmormoncentral.org/sites/all/modules/service_links/js/google_plus_one.js?s3mzmc"></script>
<script src="https://archive.bookofmormoncentral.org/sites/all/modules/service_links/js/pinterest_button.js?s3mzmc"></script>
<script src="https://archive.bookofmormoncentral.org/sites/all/modules/tb_megamenu/js/tb-megamenu-frontend.js?s3mzmc"></script>
<script src="https://archive.bookofmormoncentral.org/sites/all/modules/service_links/js/facebook_like.js?s3mzmc"></script>
<script src="https://archive.bookofmormoncentral.org/sites/all/modules/service_links/js/twitter_button.js?s3mzmc"></script>
<script src="https://archive.bookofmormoncentral.org/sites/all/modules/service_links/js/facebook_share.js?s3mzmc"></script>
<script src="https://archive.bookofmormoncentral.org/sites/all/modules/tb_megamenu/js/tb-megamenu-touch.js?s3mzmc"></script>
<script src="https://archive.bookofmormoncentral.org/sites/all/themes/bmc/js/custom.js?s3mzmc"></script>
<script src="https://archive.bookofmormoncentral.org/sites/all/themes/bmc/js/masonry.pkgd.min.js?s3mzmc"></script>
<script src="https://archive.bookofmormoncentral.org/sites/all/themes/bmc/js/wow.min.js?s3mzmc"></script>
<script src="https://archive.bookofmormoncentral.org/sites/all/themes/archive_subtheme/js/archive.js?s3mzmc"></script>
<script>jQuery.extend(Drupal.settings, {"basePath":"\\/","pathPrefix":"","ajaxPageState":{"theme":"archive_subtheme","theme_token":"vVP0_ThC4-xrTt3ScUZGqEPY5OrDRcA6lc6uBSQyZ_w","js":{"sites\\/all\\/modules\\/lightbox2\\/js\\/auto_image_handling.js":1,"sites\\/all\\/modules\\/lightbox2\\/js\\/lightbox.js":1,"sites\\/all\\/themes\\/bootstrap\\/js\\/bootstrap.js":1,"https:\\/\\/archive.bookofmormoncentral.org\\/sites\\/default\\/files\\/google_tag\\/archive_of_book_of_mormon_central_ga4\\/google_tag.script.js":1,"sites\\/all\\/modules\\/jquery_update\\/replace\\/jquery\\/1.10\\/jquery.min.js":1,"misc\\/jquery-extend-3.4.0.js":1,"misc\\/jquery-html-prefilter-3.5.0-backport.js":1,"misc\\/jquery.once.js":1,"misc\\/drupal.js":1,"https:\\/\\/cdn.jsdelivr.net\\/npm\\/bootstrap@3.3.7\\/dist\\/js\\/bootstrap.js":1,"sites\\/all\\/modules\\/google_cse\\/google_cse.js":1,"sites\\/all\\/modules\\/service_links\\/js\\/google_plus_one.js":1,"sites\\/all\\/modules\\/service_links\\/js\\/pinterest_button.js":1,"sites\\/all\\/modules\\/tb_megamenu\\/js\\/tb-megamenu-frontend.js":1,"sites\\/all\\/modules\\/service_links\\/js\\/facebook_like.js":1,"sites\\/all\\/modules\\/service_links\\/js\\/twitter_button.js":1,"sites\\/all\\/modules\\/service_links\\/js\\/facebook_share.js":1,"sites\\/all\\/modules\\/tb_megamenu\\/js\\/tb-megamenu-touch.js":1,"sites\\/all\\/themes\\/bmc\\/js\\/custom.js":1,"sites\\/all\\/themes\\/bmc\\/js\\/masonry.pkgd.min.js":1,"sites\\/all\\/themes\\/bmc\\/js\\/wow.min.js":1,"sites\\/all\\/themes\\/archive_subtheme\\/js\\/archive.js":1},"css":{"modules\\/system\\/system.base.css":1,"modules\\/field\\/theme\\/field.css":1,"sites\\/all\\/modules\\/footnotes\\/footnotes.css":1,"sites\\/all\\/modules\\/google_cse\\/google_cse.css":1,"modules\\/node\\/node.css":1,"sites\\/all\\/modules\\/views\\/css\\/views.css":1,"sites\\/all\\/modules\\/ctools\\/css\\/ctools.css":1,"sites\\/all\\/modules\\/lightbox2\\/css\\/lightbox_alt.css":1,"sites\\/all\\/modules\\/biblio\\/biblio.css":1,"sites\\/all\\/modules\\/tb_megamenu\\/css\\/bootstrap.css":1,"sites\\/all\\/modules\\/tb_megamenu\\/css\\/base.css":1,"sites\\/all\\/modules\\/tb_megamenu\\/css\\/default.css":1,"sites\\/all\\/modules\\/tb_megamenu\\/css\\/compatibility.css":1,"sites\\/all\\/modules\\/ds\\/layouts\\/ds_2col_stacked_fluid\\/ds_2col_stacked_fluid.css":1,"sites\\/all\\/modules\\/social_media_links\\/social_media_links.css":1,"sites\\/all\\/libraries\\/fontawesome\\/css\\/font-awesome.css":1,"https:\\/\\/cdn.jsdelivr.net\\/npm\\/bootstrap@3.3.7\\/dist\\/css\\/bootstrap.min.css":1,"sites\\/all\\/themes\\/bmc\\/css\\/style.css":1,"sites\\/all\\/themes\\/bmc\\/css\\/custom.css":1,"sites\\/all\\/themes\\/bmc\\/css\\/animate.css":1,"sites\\/all\\/themes\\/archive_subtheme\\/css\\/archive-styles.css":1}},"googleCSE":{"cx":"001946668175012064535:tb4uxxvjjhw","resultsWidth":600,"domain":"www.google.com","showWaterMark":1},"lightbox2":{"rtl":0,"file_path":"\\/(\\w\\w\\/)public:\\/","default_image":"\\/sites\\/all\\/modules\\/lightbox2\\/images\\/brokenimage.jpg","border_size":10,"font_color":"fff","box_color":"000","top_position":"","overlay_opacity":"0.8","overlay_color":"000","disable_close_click":1,"resize_sequence":0,"resize_speed":400,"fade_in_speed":400,"slide_down_speed":600,"use_alt_layout":1,"disable_resize":0,"disable_zoom":0,"force_show_nav":0,"show_caption":1,"loop_items":0,"node_link_text":"View Image Details","node_link_target":0,"image_count":"Image !current of !total","video_count":"Video !current of !total","page_count":"Page !current of !total","lite_press_x_close":"press \u003Ca href=\u0022#\u0022 onclick=\u0022hideLightbox(); return FALSE;\u0022\u003E\u003Ckbd\u003Ex\u003C\\/kbd\u003E\u003C\\/a\u003E to close","download_link_text":"","enable_login":false,"enable_contact":false,"keys_close":"c x 27","keys_previous":"p 37","keys_next":"n 39","keys_zoom":"z","keys_play_pause":"32","display_image_size":"original","image_node_sizes":"(\\.thumbnail)","trigger_lightbox_classes":"img.thumbnail, img.image-thumbnail","trigger_lightbox_group_classes":"","trigger_slideshow_classes":"","trigger_lightframe_classes":"","trigger_lightframe_group_classes":"","custom_class_handler":0,"custom_trigger_classes":"","disable_for_gallery_lists":1,"disable_for_acidfree_gallery_lists":true,"enable_acidfree_videos":true,"slideshow_interval":5000,"slideshow_automatic_start":true,"slideshow_automatic_exit":true,"show_play_pause":true,"pause_on_next_click":false,"pause_on_previous_click":true,"loop_slides":false,"iframe_width":700,"iframe_height":400,"iframe_border":1,"enable_video":0,"useragent":"Mozilla\\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\\/537.36 (KHTML, like Gecko) Chrome\\/119.0.0.0 Safari\\/537.36 Edg\\/119.0.0.0"},"ws_fs":{"type":"button_count","app_id":"150123828484431","css":"","locale":"en_US"},"ws_fl":{"width":100,"height":21},"ws_gpo":{"size":"","annotation":"","lang":"","callback":"","width":300},"ws_pb":{"countlayout":"horizontal"},"urlIsAjaxTrusted":{"\\/content\\/1-nephi-1":true},"bootstrap":{"anchorsFix":"0","anchorsSmoothScrolling":"0","formHasError":1,"popoverEnabled":1,"popoverOptions":{"animation":1,"html":0,"placement":"right","selector":"","trigger":"click","triggerAutoclose":1,"title":"","content":"","delay":0,"container":"body"},"tooltipEnabled":1,"tooltipOptions":{"animation":1,"html":0,"placement":"auto left","selector":"","trigger":"hover focus","delay":0,"container":"body"}}});</script>
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
<body class="navbar-is-static-top html not-front not-logged-in no-sidebars page-node page-node- page-node-11936 node-type-biblio">

<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KX24VBJ"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

  <div id="skip-link">
    <a href="#main-content" class="element-invisible element-focusable">Skip to main content</a>
  </div>
    <div class="region region-page-top">
    <noscript aria-hidden="true"><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-593TQJZ" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  </div>
  <header id="navbar" role="banner" class="navbar navbar-static-top navbar-default">
  <div class="container">
    <div class="navbar-header">
              <a class="logo navbar-btn pull-left" href="https://bookofmormoncentral.org" title="Home">
          <img src="https://archive.bookofmormoncentral.org/sites/default/files/trazado-171x.png" alt="Home" />
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
    <section id="block-search-form" class="block block-search clearfix archive-search clearfix">


  <form class="google-cse form-search content-search" action="/content/1-nephi-1" method="post" id="search-block-form" accept-charset="UTF-8"><div><div>
      <h2 class="element-invisible">Search form</h2>
    <div class="input-group"><input title="Enter the terms you wish to search for." placeholder="Search" class="form-control form-text" type="text" id="edit-search-block-form--2" name="search_block_form" value="" size="15" maxlength="128" /><span class="input-group-btn"><button type="submit" class="btn btn-primary"><span class="icon glyphicon glyphicon-search" aria-hidden="true"></span>
</button></span></div><div class="form-actions form-wrapper form-group" id="edit-actions"><button class="element-invisible btn btn-primary form-submit" type="submit" id="edit-submit" name="op" value="Search">Search</button>
</div><input type="hidden" name="form_build_id" value="form-9tNrqp7RuJ3dDMl4X6u5BNSHghzwiMypYJxYYgw8gHs" />
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
    <ul  class="tb-megamenu-nav nav level-0 items-8">
  <li  data-id="980" data-level="1" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="center" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-1 mega mega-align-center dropdown">
  <a href="#"  class="dropdown-toggle" title="Come Follow Me">

    Come Follow Me          <span class="caret"></span>
          </a>
  <div  data-class="" data-width="" class="tb-megamenu-submenu dropdown-menu mega-dropdown-menu nav-child">
  <div class="mega-dropdown-inner">
    <div  class="tb-megamenu-row row-fluid">
  <div  data-class="" data-width="12" data-hidewcol="0" id="tb-megamenu-column-1" class="tb-megamenu-column span12  mega-col-nav">
  <div class="tb-megamenu-column-inner mega-inner clearfix">
        <ul  class="tb-megamenu-subnav mega-nav level-1 items-4">
  <li  data-id="1648" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/come-follow-me/old-testament"  title="Old Testament">

    Old Testament          </a>
  </li>

<li  data-id="1627" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/come-follow-me/new-testament-2023"  title="New Testament">

    New Testament          </a>
  </li>

<li  data-id="1625" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/come-follow-me/book-of-mormon-2024"  title="Book of Mormon">

    Book of Mormon          </a>
  </li>

<li  data-id="1626" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
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

<li  data-id="635" data-level="1" data-type="menu_item" data-class="" data-xicon="fa" data-caption="" data-alignsub="center" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-1 mega mega-align-center dropdown">
  <a href="#"  class="dropdown-toggle" title="Research">
          <i class="fa"></i>

    Research          <span class="caret"></span>
          </a>
  <div  data-class="" data-width="" class="tb-megamenu-submenu dropdown-menu mega-dropdown-menu nav-child">
  <div class="mega-dropdown-inner">
    <div  class="tb-megamenu-row row-fluid">
  <div  data-class="" data-width="12" data-hidewcol="0" id="tb-megamenu-column-2" class="tb-megamenu-column span12  mega-col-nav">
  <div class="tb-megamenu-column-inner mega-inner clearfix">
        <ul  class="tb-megamenu-subnav mega-nav level-1 items-5">
  <li  data-id="393" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="http://www.knowhy.bookofmormoncentral.org"  title="Daily Evidences of The Book of Mormon">

    KnoWhys          </a>
  </li>

<li  data-id="1657" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://evidencecentral.org/recency"  title="Evidence Central">

    Evidence Central          </a>
  </li>

<li  data-id="341" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="/"  title="Archive">

    Archive          </a>
  </li>

<li  data-id="1339" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/questions-answers"  title="Q&amp;A">

    Q&A          </a>
  </li>

<li  data-id="1614" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
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

<li  data-id="1635" data-level="1" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="center" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-1 mega mega-align-center dropdown">
  <a href="https://bookofmormoncentral.org/content/media"  class="dropdown-toggle" title="Media">

    Media          <span class="caret"></span>
          </a>
  <div  data-class="" data-width="" class="tb-megamenu-submenu dropdown-menu mega-dropdown-menu nav-child">
  <div class="mega-dropdown-inner">
    <div  class="tb-megamenu-row row-fluid">
  <div  data-class="" data-width="12" data-hidewcol="0" id="tb-megamenu-column-3" class="tb-megamenu-column span12  mega-col-nav">
  <div class="tb-megamenu-column-inner mega-inner clearfix">
        <ul  class="tb-megamenu-subnav mega-nav level-1 items-3">
  <li  data-id="1636" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://www.youtube.com/channel/UCSsrx8lFpeuBjNIE7FNm2CQ/"  title="Videos">

    Videos          </a>
  </li>

<li  data-id="1638" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/content/scripture-central-podcasts"  title="Podcasts">

    Podcasts          </a>
  </li>

<li  data-id="1637" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="/category/media"  title="Artwork">

    Artwork          </a>
  </li>
</ul>
  </div>
</div>
</div>
  </div>
</div>
</li>

<li  data-id="637" data-level="1" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="center" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-1 mega mega-align-center dropdown">
  <a href="#"  class="dropdown-toggle" title="About">

    About          <span class="caret"></span>
          </a>
  <div  data-class="" data-width="" class="tb-megamenu-submenu dropdown-menu mega-dropdown-menu nav-child">
  <div class="mega-dropdown-inner">
    <div  class="tb-megamenu-row row-fluid">
  <div  data-class="" data-width="12" data-hidewcol="0" id="tb-megamenu-column-4" class="tb-megamenu-column span12  mega-col-nav">
  <div class="tb-megamenu-column-inner mega-inner clearfix">
        <ul  class="tb-megamenu-subnav mega-nav level-1 items-3">
  <li  data-id="342" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="http://www.bookofmormoncentral.org/about"  title="About BMC">

    About BMC          </a>
  </li>

<li  data-id="1144" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
  <a href="https://bookofmormoncentral.org/blog"  title="BMC Blog">

    BMC Blog          </a>
  </li>

<li  data-id="713" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega">
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

<li  data-id="1628" data-level="1" data-type="menu_item" data-class="hidden-menu-item" data-xicon="fa fa-th" data-caption="" data-alignsub="right" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-1 mega hidden-menu-item mega-align-right dropdown">
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
  <li  data-id="1629" data-level="2" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="1" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-2 mega mega-group">
  <a href="#"  class="mega-group-title" title="BMC Projects">

    BMC Projects          <span class="caret"></span>
          </a>
  <div  data-class="" data-width="" class="tb-megamenu-submenu mega-group-ct nav-child">
  <div class="mega-dropdown-inner">
    <div  class="tb-megamenu-row row-fluid">
  <div  data-class="" data-width="12" data-hidewcol="0" id="tb-megamenu-column-5" class="tb-megamenu-column span12  mega-col-nav">
  <div class="tb-megamenu-column-inner mega-inner clearfix">
        <ul  class="tb-megamenu-subnav mega-nav level-2 items-11">
  <li  data-id="1630" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://centralldm.es/"  title="BMC en Español">

    BMC en Español          </a>
  </li>

<li  data-id="1639" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://www.youtube.com/channel/UCoreu97W5GDPsIFGm7HBJhg"  title="BMC em Português">

    BMC em Português          </a>
  </li>

<li  data-id="1631" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://www.scriptureplus.org/"  title="ScripturePlus">

    ScripturePlus          </a>
  </li>

<li  data-id="1641" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://doctrineandcovenantscentral.org/"  title="Doctrine and Covenants Central">

    Doctrine and Covenants Central          </a>
  </li>

<li  data-id="1632" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://www.pearlofgreatpricecentral.org/"  title="Pearl of Great Price Central">

    Pearl of Great Price Central          </a>
  </li>

<li  data-id="1633" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://evidencecentral.org/#/landing"  title="Evidence Central">

    Evidence Central          </a>
  </li>

<li  data-id="1634" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="http://especiallyforseminary.org/"  title="Especially For Seminary">

    Especially For Seminary          </a>
  </li>

<li  data-id="1640" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://www.youtube.com/user/messagesofChrist"  title="Messages of Christ">

    Messages of Christ          </a>
  </li>

<li  data-id="1645" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://centraldyc.es/"  title="Central de Doctrina y Convenios">

    Central de Doctrina y Convenios          </a>
  </li>

<li  data-id="1646" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
  <a href="https://centralpgp.es/"  title="Perla de Gran Precio">

    Perla de Gran Precio          </a>
  </li>

<li  data-id="1647" data-level="3" data-type="menu_item" data-class="" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-3 mega">
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

<li  data-id="1617" data-level="1" data-type="menu_item" data-class="btn btn-primary donate-menu-item" data-xicon="" data-caption="" data-alignsub="" data-group="0" data-hidewcol="0" data-hidesub="0" class="tb-megamenu-item level-1 mega btn btn-primary donate-menu-item">
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
    <section id="block-menu-menu-archive-menu" class="block block-menu sub-menu clearfix">

        <h2 class="block-title">Archive Menu</h2>

  <ul class="menu nav"><li class="first leaf"><a href="/category/books" title="">Books</a></li>
<li class="leaf"><a href="/periodicals" title="">Periodicals</a></li>
<li class="leaf"><a href="/category/media" title="">Media</a></li>
<li class="leaf"><a href="/keyword-index" title="">Subject</a></li>
<li class="leaf"><a href="/scripture-filter" title="">Scripture</a></li>
<li class="last leaf"><a href="/authors-index" title="">Author</a></li>
</ul>
</section>
  </div>
  </header> <!-- /#page-header -->

  <div class="row">


    <section class="col-sm-12">
            <h2 class="element-invisible">You are here</h2><div class="breadcrumb"><span class="inline odd first"><a href="https://bookofmormoncentral.org">Book of Mormon Central</a></span> <span class="delimiter">/</span> <span class="inline even"><a href="/">Archive</a></span> <span class="delimiter">/</span> <span class="inline odd last">1 Nephi 1</span></div>      <a id="main-content"></a>
                                                                <div class="region region-content">
    <section id="block-system-main" class="block block-system clearfix">


  <div  about="/content/1-nephi-1" typeof="sioc:Item foaf:Document" class="ds-2col-stacked-fluid node node-biblio node-promoted view-mode-full clearfix">


  <div class="group-header">
    <div class="field field-name-title field-type-ds field-label-hidden"><div class="field-items"><div class="field-item even" property="dc:title"><h1 class="page-title">1 Nephi 1</h1></div></div></div><div class="field field-name-social-media field-type-ds field-label-hidden"><div class="field-items"><div class="field-item even"><section id="block-service-links-service-links" class="block block-service-links clearfix">


  <div class="service-links"><a href="https://archive.bookofmormoncentral.org/content/1-nephi-1" title="Plus it" class="service-links-google-plus-one" rel="nofollow"><span class="element-invisible">Google Plus One</span></a> <a href="https://pinterest.com/pin/create/button/?url=https%3A//archive.bookofmormoncentral.org/content/1-nephi-1&amp;description=&amp;media=" class="pin-it-button service-links-pinterest-button" title="Pin It" rel="nofollow"><span class="element-invisible">Pinterest</span></a> <a href="https://twitter.com/share?url=https%3A//archive.bookofmormoncentral.org/content/1-nephi-1&amp;count=horizontal&amp;via=&amp;text=1%20Nephi%201&amp;counturl=https%3A//archive.bookofmormoncentral.org/content/1-nephi-1" class="twitter-share-button service-links-twitter-widget" title="Tweet This" rel="nofollow"><span class="element-invisible">Tweet Widget</span></a> <a href="https://www.facebook.com/plugins/like.php?href=https%3A//archive.bookofmormoncentral.org/content/1-nephi-1&amp;layout=button_count&amp;show_faces=false&amp;action=like&amp;colorscheme=light&amp;width=100&amp;height=21&amp;font=&amp;locale=&amp;share=false" title="I Like it" class="service-links-facebook-like" rel="nofollow"><span class="element-invisible">Facebook Like</span></a> <a href="https://www.facebook.com/sharer.php" title="Share this post on Facebook" class="service-links-facebook-share" rel="https://archive.bookofmormoncentral.org/content/1-nephi-1"><span class="element-invisible">Share on Facebook</span></a></div>
</section>
</div></div></div>  </div>

      <div class="group-left">
      <div id="biblio-node"><span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.atitle=1+Nephi+1&amp;rft.title=Book+of+Mormon+Minute&amp;rft.btitle=Book+of+Mormon+Minute&amp;rft.date=2019&amp;rft.aulast=Gardner&amp;rft.aufirst=Brant&amp;rft.pub=Book+of+Mormon+Central&amp;rft.place=Springville%2C+UT"></span><div class="table-responsive">
<table class="table table-hover table-striped">
<tbody>
 <tr><td class="biblio-row-title">Title</td><td>1 Nephi 1</td> </tr>
 <tr><td class="biblio-row-title">Publication Type</td><td>Book Chapter</td> </tr>
 <tr><td class="biblio-row-title">Year of Publication</td><td>2019</td> </tr>
 <tr><td class="biblio-row-title">Authors</td><td><a href="/biblio?f%5Bauthor%5D=446" rel="nofollow">Gardner, Brant A.</a></td> </tr>
 <tr><td class="biblio-row-title">Book Title</td><td>Book of Mormon Minute</td> </tr>
 <tr><td class="biblio-row-title">Publisher</td><td>Book of Mormon Central</td> </tr>
 <tr><td class="biblio-row-title">City</td><td>Springville, UT</td> </tr>
 <tr><td class="biblio-row-title">Keywords</td><td><a href="/biblio?f%5Bkeyword%5D=159" rel="nofollow">1 Nephi</a></td> </tr>
</tbody>
</table>
</div>
</div><div class="field-name-field-additional-text"><h1 class="label-above accordion">Show Full Text</h1><div class="accordion-content"><h1 style="text-align: center;">1 Nephi 1</h1>
<h2>Episode 1: Before Beginning to Study the Book of Mormon</h2>
<p style="text-align: justify;">Near the end of his life, Mormon conceived of writing a focused history of his people, the Nephites. He believed that by writing that history, the future descendants of the New World house of Israel would be able to believe that Jesus Christ was the very eternal God, and that the lessons of Nephite history would be beneficial to those future readers.</p>
<p style="text-align: justify;">Joseph Smith received the plates that Mormon wrote, and that were then finished by Mormon’s son, Moroni. The loss of the 116 manuscript pages of the translation means that we are missing a large portion of Mormon’s work. In its place, we have a different record, written for a different reason, and written by different writers. We have what we call the small plates of Nephi.</p>
<p style="text-align: justify;">Nephi created the Nephite tradition of record keeping. The most important record he created was an official governmental history that included the information about the reigns of the kings. Subsequent to Nephi, scribes were appointed to maintain that record. The tradition of recording the deeds of the kings, and their wars, and their contentions continued to the time when Ammaron chose Mormon to become the next and (probably unknown to Ammaron) final Nephite official scribe. This record was Mormon’s principal source for the Book of Mormon.</p>
<p style="text-align: justify;">At some later time, Nephi was inspired to create a different record, which followed a different purpose, and a different line of transmission. The small plates of Nephi were called “small” not because they were physically smaller, but because there were fewer. The large plates were clearly added to throughout history, while the small plates appear to have been created by Nephi, and never had new plates added. They were given to king Benjamin when they were full.</p>
<p style="text-align: justify;">Nephi declared that the small plates would contain the ministry of his people. Even so, only the books of Second Nephi and Jacob say much about ministry. The other books are heavily historical. Nevertheless, it is important to understand that there was no clear division between religion and politics in the ancient world. Men governed according to the will and direction of deity, in Israel as well as in most other nations of the earth. Thus, even the history found in First Nephi can be seen as part of the ministry, because it establishes the rule of a king who governed by Jehovah’s grace, and according to Jehovah’s law.</p>
<p style="text-align: justify;">In the Book of Mormon Minute, we will make succinct comments to, at most, a few verses at a time. These will be comments that look at the text from the perspectives of the times and purposes in which they were written, as well as the purposes for which they were written.</p>
<h2 style="text-align: justify;">Episode 2: Book Header for First Nephi</h2>
<p style="text-align: justify;">An account of Lehi and his wife Sariah, and his four sons, being called, (beginning at the eldest) Laman, Lemuel, Sam, and Nephi. The Lord warns Lehi to depart out of the land of Jerusalem, because he prophesieth unto the people concerning their iniquity and they seek to destroy his life. He taketh three days’ journey into the wilderness with his family. Nephi taketh his brethren and returneth to the land of Jerusalem after the record of the Jews. The account of their sufferings. They take the daughters of Ishmael to wife. They take their families and depart into the wilderness. Their sufferings and afflictions in the wilderness. The course of their travels. They come to the large waters. Nephi’s brethren rebel against him. He confoundeth them, and buildeth a ship. They call the name of the place Bountiful. They cross the large waters into the promised land, and so forth. This is according to the account of Nephi; or in other words, I, Nephi, wrote this record.</p>
<h3 style="text-align: justify;"><strong>Comments</strong></h3>
<p style="text-align: justify;">At the beginning of the Book of Mormon we have the text from the small plates rather than from Mormon’s book. At the beginning of the book of First Nephi, we have a header that gives a description of the events that are to come in the book. Nephi wrote this header, and included one for Second Nephi as well.</p>
<p style="text-align: justify;">The most interesting part of the header for First Nephi is that the nature of the writing changes for the last line. For the most part, the synoptic header is written in the third person, a practice that continues in all other book headers. Then, in the last line, it shifts to first person. We have “This is according to the account of Nephi; or in other words, I, Nephi, wrote this record.” That line is anomalous not only because it is in first person, but because it comes after the header, it describes the last events.</p>
<p style="text-align: justify;">It would be best to consider that line as a chapter header rather than a book header. Nephi will have a chapter header in Second Nephi Chapter 6, so he clearly has that understanding in his literary arsenal. The printer’s manuscript doesn’t separate the headers from the text, so the current division exists because that is the way that the compositor read it. Reconceiving that last line as a chapter header is more consistent with the way the rest of the text is written.</p>
<h2 style="text-align: justify;">Episode 3: 1 Nephi 1:1</h2>
<p style="text-align: justify;">1 I, Nephi, having been born of goodly parents, therefore I was taught somewhat in all the learning of my father; and having seen many afflictions in the course of my days, nevertheless, having been highly favored of the Lord in all my days; yea, having had a great knowledge of the goodness and the mysteries of God, therefore I make a record of my proceedings in my days.</p>
<h3 style="text-align: justify;"><strong>Comments</strong></h3>
<p style="text-align: justify;">One suggestion has been that when Nephi says that he had “goodly parents,” that the intended meaning was that they were wealthy—that they had many “goods.” That is not the meaning that appears in Webster’s 1828 dictionary. It is best to consider that they were simply good. They were wealthy, and that is made clear later, but Nephi is referring to their quality of goodness, not the quantity of their goods.</p>
<p style="text-align: justify;">Nevertheless, it has also been suggested that a possible meaning for Nephi’s name suggested good, or goodness. Thus, this introduction may have been a play on words.</p>
<p style="text-align: justify;">The goodness of his parents allowed Nephi to be “taught somewhat in all the learning of my father.” It would be an unusual child who did not learn from his or her parents, and Nephi’s mention of learning will be reiterated in the second verse. This suggests that Nephi was educated, meaning more than simple parental instruction.</p>
<p style="text-align: justify;">It is clear that Nephi learned something of metalworking from his father, but there are also clues that he was trained to be a scribe. As a fourth son, he was not going to inherit his father’s business. The family economic position was sufficient to send him to scribal school, and much of what Nephi writes later in life depends upon what he learned in scribal school. Beyond the clear ability to read and write, Nephi’s experience with literary forms and expectations of certain types of literature will inform what we read from him in both First and Second Nephi.</p>
<h2 style="text-align: justify;">Episode 4: 1 Nephi 1:2</h2>
<p style="text-align: justify;">2 Yea, I make a record in the language of my father, which consists of the learning of the Jews and the language of the Egyptians.</p>
<h3 style="text-align: justify;"><strong>Comments</strong></h3>
<p style="text-align: justify;">This verse is both extremely important and extremely difficult to completely understand. Nephi says that he is making a record “in the language of my father.” That is a strange statement. Most of us speak “the language or our father.” We learn to speak in the home, and learn to speak the language we hear. It is the language of our fathers, and is so unremarkable that we need not mention it. Yet Nephi does.</p>
<p style="text-align: justify;">When he clarifies that his father’s “language” “consists of the learning of the Jews and the language of the Egyptians” we don’t find that clarifying statement as illuminating as he possibly thought it was.</p>
<p style="text-align: justify;">One suggestion is that he is speaking of using the Hebrew language, but writing in Egyptian characters. This is a possibility, as documents from antiquity exist that demonstrate that very merger of two different cultures. Also, both Hebrew literature and the Egyptian language were taught in Hebrew scribal schools.</p>
<p style="text-align: justify;">In any case, there is something about Egyptian that continues throughout Nephite written history. Late in the text, Moroni says that their characters are “reformed Egyptian.” That strongly suggests that some form of Egyptian writing came to the New World with Nephi. That writing system need not have been hieroglyphs. Hieratic script had been in use long before Nephi’s day, and the Demotic script was invented close to Nephi’s time. Given the timeframes, Hieratic would be the better guess for the script Nephi learned.</p>
<p style="text-align: justify;">Egyptian writing systems were syllabic. That is, a character represented a syllable, not a single sound as in our writing system. Thus, three different characters would represent <em>ba, bo, </em>and <em>bu.</em> Our writing system uses six characters. It may or may not be connected, but the only known writing systems in the New World are also syllabic. That isn’t to say that they were created because of the Nephite importation of Egyptian, but that there was a conceptual similarity that might explain the way in which the original Egyptian might have been reformed using more culturally relevant representations for sounds.</p>
<h2 style="text-align: justify;"><span style="font-size: 1.231em; font-weight: bold;">Episode 5: 1 Nephi 1:3</span></h2>
<p style="text-align: justify;">3 And I know that the record which I make is true; and I make it with mine own hand; and I make it according to my knowledge.</p>
<h3 style="text-align: justify;"><strong>Comments</strong></h3>
<p style="text-align: justify;">Nephi makes an important statement. He gives his personal relationship to the text. He has written it himself, and he declares that it is a true record, according to his knowledge. This statement is a typical addition to an ancient document, and is called a colophon.</p>
<p style="text-align: justify;">A colophon served to identify the important information about the author. It could be found at the end of documents, or, as in this case, at the beginning. In a world before publishing, a document might be hand-copied a number of times. The person whose hand wrote the copy would not necessarily be the person who composed the document. If the colophon was copied, then the reader was to understand that even the copies reflected the original writer rather than the copyist.</p>
<p style="text-align: justify;">High Nibley noted that a typical colophon would contain the writer’s name, the writer’s lineage, and sometimes an affirmation of the written text’s trustworthiness. These are the very things we see in Nephi’s colophon.</p>
<p style="text-align: justify;">When Nephi tells us that he made the text with his own hand, we have a double meaning. We will learn in 1 Nephi 1:17 that Nephi also physically created the plates. It will be on the very plates that Nephi made that his brother, Jacob, will write his own addition to Nephite history.</p>
<h2 style="text-align: justify;"><span style="font-size: 1.231em; font-weight: bold;">Episode 6: 1 Nephi 1:4</span></h2>
<p style="text-align: justify;">4 For it came to pass in the commencement of the first year of the reign of Zedekiah, king of Judah, (my father, Lehi, having dwelt at Jerusalem in all his days); and in that same year there came many prophets, prophesying unto the people that they must repent, or the great city Jerusalem must be destroyed.</p>
<h3 style="text-align: justify;"><strong>Comments</strong></h3>
<p style="text-align: justify;">The prophets were prophesying that Babylon would destroy Jerusalem, but they were probably not believed because Babylon had already dominated Judah and Jerusalem. Zedekiah was king only because the Babylonians installed him. Thus, the prophets were not saying that Babylon would come, because it had already come. They were prophesying an escalation of contention that perhaps was more difficult to see in the year they installed Zedekiah as king.</p>
<p style="text-align: justify;">The first year of the reign of Zedekiah gives us a starting year for the Book of Mormon. It was 597 BC. Jerusalem was destroyed about 10 years later, and Lehi and his family left prior to the destruction, but perhaps not too long before the destruction.</p>
<p style="text-align: justify;">Perhaps ironically, perhaps symbolically, it was about one hundred years earlier that Assyria and invaded Judah and threatened Jerusalem. Prior to both invasions, a king in Judah had attempted to reform Israelite religion, with only temporary success. The people began returning to their previous ideas as soon as the next king was anointed.</p>
<p style="text-align: justify;">These parallel invasions undoubtedly helped convince Nephi to see his family, and later his people, in the context of a scattered people who were to be gathered to Israel. Isaiah was the prophet of the Assyrian invasion, and the scattering and gathering of the ten tribes were important to Isaiah. Nephi certainly likened his own people to Isaiah’s times, and saw Isaiah as particularly poignant for his New World people.</p>
<p style="text-align: justify;">More immediately, however, the fact that both the Assyrians and Babylonians had invaded Judah, but Jerusalem yet stood—must have informed the popular opinion, and provided what must have been seen as the logical argument against the doomsaying prophets,among whom was Lehi.</p>
<p style="text-align: justify;"><span style="font-size: 1.385em; font-weight: bold;">Epi</span><span style="font-size: 1.385em; font-weight: bold;">sode 7: 1 Nephi 1:5–6</span></p>
<p style="text-align: justify;">5 Wherefore it came to pass that my father, Lehi, as he went forth prayed unto the Lord, yea, even with all his heart, in behalf of his people.</p>
<p style="text-align: justify;">6 And it came to pass as he prayed unto the Lord, there came a pillar of fire and dwelt upon a rock before him; and he saw and heard much; and because of the things which he saw and heard he did quake and tremble exceedingly.</p>
<h3 style="text-align: justify;"><strong>Comments</strong></h3>
<p style="text-align: justify;">Nephi began his record by noting that he had goodly parents. He will eventually speak of his own experiences as allowed by those goodly parents, but at this point he is interested in his father. The previous verses noted that there had been prophets in Jerusalem, and now his father will become one of them.</p>
<p style="text-align: justify;">Without expressly saying so, Nephi suggests that the message of those prophets had touched his father, and led to his father praying on behalf of his people. As a response to that prayer, Lehi receives a vision. Nephi says that “he saw and heard much,” but tells us nothing of what he saw or heard. What is important in this part of the story is that a pillar of fire descended and “dwelt upon a rock.” This image intentionally invokes two aspects of Moses’ life.</p>
<p style="text-align: justify;">The first is the burning bush. While no bush burned for Lehi, there was burning on a rock, a similarly miraculous event. Where Moses’ bush was not consumed, Lehi’s pillar of fire burned without terrestrial source. In both events, Jehovah was in the fire.</p>
<p style="text-align: justify;">The second element of the pillar of fire is the image of that pillar of fire guiding the children of Israel as they journeyed in the wilderness. Lehi probably didn’t understand that image at the time, but Nephi—writing long after the fact—certainly saw in the pillar of fire the image of his father leading his family from their old home to a new one across the wilderness.</p>
<h2 style="text-align: justify;"><span style="font-size: 1.231em; font-weight: bold;">Episode 8: 1 Nephi 1:7–8</span></h2>
<p style="text-align: justify;">7 And it came to pass that he returned to his own house at Jerusalem; and he cast himself upon his bed, being overcome with the Spirit and the things which he had seen.</p>
<p style="text-align: justify;">8 And being thus overcome with the Spirit, he was carried away in a vision, even that he saw the heavens open, and he thought he saw God sitting upon his throne, surrounded with numberless concourses of angels in the attitude of singing and praising their God.</p>
<h3 style="text-align: justify;"><strong>Comments</strong></h3>
<p style="text-align: justify;">Lehi had seen and heard much in his vision of the pillar of fire that dwelt on the rock. The power manifest in such a personal revelation left Lehi physically drained. Joseph Smith had a similar experience of feeling drained after his vision following his fervent prayer in the grove.</p>
<p style="text-align: justify;">In the case of Lehi, he was already in a receptive state, and that openness to the Spirit unfolded a second vision. The language in our translation of what Nephi wrote is reminiscent of Luke 2:13: “And suddenly there was with the angel a multitude of the heavenly host praising God.” Although the words are similar, the setting is different.</p>
<p style="text-align: justify;">In Lehi’s call to become a prophet, his vision begins with a vision of God upon his throne. The location is therefore in the heavens, not an earthly presence of the angels announcing Jesus’s birth. Lehi sees God’s heavenly council.</p>
<p style="text-align: justify;">His vision opens with this scene because that is the expected literary form for the call of a prophet. Lehi’s call parallels Ezekiel’s call as a prophet: “I saw the Lord sitting on his throne, and all the host of heaven standing by him on his right hand and on his left (1 Kings 22:19).”</p>
<p style="text-align: justify;">When Nephi describes his father’s vision in this way, it is designed to tell his informed readers that this is Lehi’s divine commission to be a prophet. Because we do not know what Lehi learned in his first vision, we must assume that it was part of a preparation for this divine calling. Contrary to Nephi’s simple statement that his father had received that first vision, he will provide details of what followed this opening scene of the heavenly council.</p>
<h2 style="text-align: justify;"><span style="font-size: 1.231em; font-weight: bold;">Episode 9: 1 Nephi 1:9–12</span></h2>
<p style="text-align: justify;">9 And it came to pass that he saw One descending out of the midst of heaven, and he beheld that his luster was above that of the sun at noon-day.</p>
<p style="text-align: justify;">10 And he also saw twelve others following him, and their brightness did exceed that of the stars in the firmament.</p>
<p style="text-align: justify;">11 And they came down and went forth upon the face of the earth; and the first came and stood before my father, and gave unto him a book, and bade him that he should read.</p>
<p style="text-align: justify;">12 And it came to pass that as he read, he was filled with the Spirit of the Lord.</p>
<h3 style="text-align: justify;"><strong>Comments</strong></h3>
<p style="text-align: justify;">Living, as we do, in a world familiar with Jesus’s earthly mission, we can easily miss the way Lehi would have understood this vision. To us, it is clearly Christ and the apostles. To Lehi, it was Jehovah and representatives of the twelve tribes. Of course, the reason that there were twelve apostles was to represent the whole of the twelve tribes—the whole of the covenant people. For Lehi, Jehovah was the very God who would come down among the children of men. Thus, while Lehi’s labels for what he saw had to be slightly different, it was the same scene with the same meaning—but differently perceived.</p>
<p style="text-align: justify;">The heavenly delegation comes to earth. Lehi is not ascended to heaven to meet them. It is possible that this is a reinforcement of the Nephite teaching that God himself would come down to the earth. Remembering that Jehovah is the premortal name for Jesus, their understanding was literally correct. This part of the vision reinforces that understanding. This may also be the beginning of the continuing emphasis among the Nephite prophets on this God come to earth.</p>
<p style="text-align: justify;">Next, we have the heavenly book. The book is a divine record that could surely reveal the past, but also shows the divinely directed future. Lehi reads from this divine book just as John will in the book of Revelation much later in history.</p>
<h2 style="text-align: justify;"><span style="font-size: 1.231em; font-weight: bold;">Episode 10: 1 Nephi 1:13–15</span></h2>
<p style="text-align: justify;">13 And he read, saying: Wo, wo, unto Jerusalem, for I have seen thine abominations! Yea, and many things did my father read concerning Jerusalem—that it should be destroyed, and the inhabitants thereof; many should perish by the sword, and many should be carried away captive into Babylon.</p>
<p style="text-align: justify;">14 And it came to pass that when my father had read and seen many great and marvelous things, he did exclaim many things unto the Lord; such as: Great and marvelous are thy works, O Lord God Almighty! Thy throne is high in the heavens, and thy power, and goodness, and mercy are over all the inhabitants of the earth; and, because thou art merciful, thou wilt not suffer those who come unto thee that they shall perish!</p>
<p style="text-align: justify;">15 And after this manner was the language of my father in the praising of his God; for his soul did rejoice, and his whole heart was filled, because of the things which he had seen, yea, which the Lord had shown unto him.</p>
<h3 style="text-align: justify;"><strong>Comments</strong></h3>
<p style="text-align: justify;">Lehi receives his important commission for that time. While his ultimate role would be to lead his family to a New World, the prophet of the New World would be Nephi, not Lehi. Lehi’s specific call was to Jerusalem, and to echo the same admonitions that the other prophets had delivered to it. Jerusalem had to repent or be destroyed. Lehi would flee Jerusalem before he witnessed the fulfillment of that prophecy.</p>
<p style="text-align: justify;">What Nephi gives us after the commission, is his father’s reaction. It is one of praise for God. How could it not be, after two such spiritual witnesses? In this case, it is important to note that the language of praise reflects the vision he received. The vision begins in the council of the Gods, with God on his throne. In his praise, Lehi exclaims “thy throne is high in the heavens.” He had just seen that in a vision, and he reprises that experience in his praise.</p>
<p style="text-align: justify;">Given the commission to preach repentance to an unrepentant Jerusalem, the final words that Nephi records are poignant. Lehi saw that Jerusalem would be destroyed and the inhabitants either perish by then sword or be carried away captive into Babylon. After that terrible image, Lehi declares: “because thou art merciful, thou wilt not suffer those who come unto thee that they shall perish!” Jerusalem might not repent, but those individuals who do repent, will not perish.</p>
<h2 style="text-align: justify;">Episode 11: 1 Nephi 1:16–17</h2>
<p style="text-align: justify;">16 And now I, Nephi, do not make a full account of the things which my father hath written, for he hath written many things which he saw in visions and in dreams; and he also hath written many things which he prophesied and spake unto his children, of which I shall not make a full account.</p>
<p style="text-align: justify;">17 But I shall make an account of my proceedings in my days. Behold, I make an abridgment of the record of my father, upon plates which I have made with mine own hands; wherefore, after I have abridged the record of my father then will I make an account of mine own life.</p>
<h3 style="text-align: justify;"><strong>Comments</strong></h3>
<p style="text-align: justify;">These two verses have created an issue for understanding how Nephi wrote. Verse 17 declares that Nephi is abridging his father’s record, and that makes it seem as though he is changing his source. He abridged his father’s record, and now makes an account of his proceedings in his day.</p>
<p style="text-align: justify;">The problem is that in the very next verse, Nephi will again pick up with his father’s story. Clearly, Nephi does not separate his and his father’s accounts at this point, nor anywhere in all of First Nephi. There will be a gradual shift in emphasis from his father’s story to his own, but not one marked by a specific change.</p>
<p style="text-align: justify;">What we are seeing is an aside that Nephi inserted into his planned narrative. He had been speaking of his father’s visions and prophetic calling. As he wrote, that triggered a reference to his writing task. In these verses, he is speaking of his process of writing, not the historical narrative. Nephi is telling his own story, a story that he is in the process of writing on plates he made with his own hands. Yet, he knows he cannot tell his story without speaking of his father. He therefore notes that he will give a short account of his father’s call, and then will tell his story.</p>
<p style="text-align: justify;">We can recognize these verses as an interruption because they follow a pattern that has been called repetitive resumption. In other literature, it might mark an inserted text or story, but in the Book of Mormon it typically represents an author’s insertion into his planned narrative.</p>
<p style="text-align: justify;">The technique gets its name from the way the author returns to the planned narrative. Some essential part of the text from the departure is repeated, notifying the reader that the narrative had returned to the planned text. See Episode 47 for an explanation and examples of repetitive resumption.</p>
<h2 style="text-align: justify;">Episode 12: 1 Nephi 1: 18–20</h2>
<p style="text-align: justify;">18 Therefore, I would that ye should know, that after the Lord had shown so many marvelous things unto my father, Lehi, yea, concerning the destruction of Jerusalem, behold he went forth among the people, and began to prophesy and to declare unto them concerning the things which he had both seen and heard.</p>
<p style="text-align: justify;">19 And it came to pass that the Jews did mock him because of the things which he testified of them; for he truly testified of their wickedness and their abominations; and he testified that the things which he saw and heard, and also the things which he read in the book, manifested plainly of the coming of a Messiah, and also the redemption of the world.</p>
<p style="text-align: justify;">20 And when the Jews heard these things they were angry with him; yea, even as with the prophets of old, whom they had cast out, and stoned, and slain; and they also sought his life, that they might take it away. But behold, I, Nephi, will show unto you that the tender mercies of the Lord are over all those whom he hath chosen, because of their faith, to make them mighty even unto the power of deliverance.</p>
<h3 style="text-align: justify;"><strong>Comments</strong></h3>
<p style="text-align: justify;">After Nephi’s aside in verses 16 and 17, he returns to the important part of his father’s story. It was certainly important to record Lehi’s divine commission as a prophet, and equally important to place that commission in the context of the times and the message. His calling was to cry repentance to Jerusalem. Doubtless, he understood—if he had not seen it in vision—that no repentance would be forthcoming.</p>
<p style="text-align: justify;">When Lehi testifies to those in Jerusalem, they reject him and threaten his life. This leads directly to his departure with his family. In Nephi’s writing, there is no end of a chapter at this point. Our chapters 1–5 were all included in Nephi’s original chapter. Thus, Nephi intended this story to continue immediately after this verse.</p>
<p style="text-align: justify;">It is important to notice, while we are examining the historical context that led to the departure of Lehi’s family from Jerusalem, that there was another message that he preached. Presumably, it was not received any more favorably than the call to repentance. Lehi taught “plainly of the coming of Messiah.” Specifically, this is a Messiah in connection to the redemption of the world. That contrast to the more expected military and royal Messiah will become the quintessential Nephite teaching.</p>
</div></div><div class="field field-name-photo-gallery-view field-type-ds field-label-hidden"><div class="field-items"><div class="field-item even"><section id="block-views-pdf-link-block-2" class="block block-views clearfix">


  <div class="view view-pdf-link view-id-pdf_link view-display-id-block_2 view-dom-id-c99351ada2f04a23e96e54e24283f891">



      <div class="view-content">
        <div class="views-row views-row-1 views-row-odd views-row-first views-row-last">

  <div class="views-field views-field-field-catalogue">        <div class="field-content"></div>  </div>  </div>
    </div>






</div>
</section>
</div></div></div>    </div>

      <div class="group-right">
      <div class="field field-name-pdf-link field-type-ds field-label-hidden"><div class="field-items"><div class="field-item even"><section id="block-views-pdf-link-block" class="block block-views clearfix">


  <div class="view view-pdf-link view-id-pdf_link view-display-id-block view-dom-id-16ec481596c0f53facaebab61af30960">



      <div class="view-content">
        <div class="views-row views-row-1 views-row-odd views-row-first views-row-last">

  <div class="views-field views-field-field-pdf">        <div class="field-content"></div>  </div>
  <div class="views-field views-field-field-image">        <div class="field-content"></div>  </div>  </div>
    </div>






</div>
</section>
</div></div></div><div class="field field-name-copyright-disclaimer field-type-ds field-label-hidden"><div class="field-items"><div class="field-item even"><section id="block-block-5" class="block block-block clearfix">

        <h2 class="block-title">Terms of Use</h2>

  <p style="line-height:1.25em;"><span style="font-size:12px;">Items in the BMC Archive are made publicly available for non-commercial, private use. Inclusion within the BMC Archive does not imply endorsement. Items do not represent the official views of The Church of Jesus Christ of Latter-day Saints or of Book of Mormon Central. </span></p>

</section>
</div></div></div><div class="field-name-book-chapters"><section id="block-views-book-chapters-block" class="block block-views clearfix">

        <h2 class="block-title">Book</h2>

  <div class="view view-book-chapters view-id-book_chapters view-display-id-block view-dom-id-3ff3f342b4275f4085c85c64bb3adb49">



      <div class="view-content">
        <div class="views-row views-row-1 views-row-odd views-row-first views-row-last">

  <div class="views-field views-field-title">        <span class="field-content"><a href="/content/book-mormon-minute">Book of Mormon Minute</a></span>  </div>  </div>
    </div>


      <div class="attachment attachment-after">
      <div class="view view-book-chapters view-id-book_chapters view-display-id-attachment_1">



      <div class="view-content">
        <div class="views-row views-row-1 views-row-odd views-row-first views-row-last">

  <div class="views-field views-field-field-node-reference">    <h2 class="views-label views-label-field-node-reference accordion">Table of Contents</h2>    <div class="field-content accordion-content"><ul><li><a href="/content/title-page-1">Title Page</a></li>
<li><a href="/content/1-nephi-1" class="active">1 Nephi 1</a></li>
<li><a href="/content/1-nephi-2">1 Nephi 2</a></li>
<li><a href="/content/1-nephi-3">1 Nephi 3</a></li>
<li><a href="/content/1-nephi-4">1 Nephi 4</a></li>
<li><a href="/content/1-nephi-5">1 Nephi 5</a></li>
<li><a href="/content/1-nephi-6">1 Nephi 6</a></li>
<li><a href="/content/1-nephi-7">1 Nephi 7</a></li>
<li><a href="/content/1-nephi-8">1 Nephi 8</a></li>
<li><a href="/content/1-nephi-9">1 Nephi 9</a></li>
<li><a href="/content/1-nephi-10">1 Nephi 10</a></li>
<li><a href="/content/1-nephi-11">1 Nephi 11</a></li>
<li><a href="/content/1-nephi-12">1 Nephi 12</a></li>
<li><a href="/content/1-nephi-13">1 Nephi 13</a></li>
<li><a href="/content/1-nephi-14">1 Nephi 14</a></li>
<li><a href="/content/1-nephi-15">1 Nephi 15</a></li>
<li><a href="/content/1-nephi-16">1 Nephi 16</a></li>
<li><a href="/content/1-nephi-17">1 Nephi 17</a></li>
<li><a href="/content/1-nephi-18">1 Nephi 18</a></li>
<li><a href="/content/1-nephi-19">1 Nephi 19</a></li>
<li><a href="/content/1-nephi-20">1 Nephi 20</a></li>
<li><a href="/content/1-nephi-21">1 Nephi 21</a></li>
<li><a href="/content/1-nephi-22">1 Nephi 22</a></li>
<li><a href="/content/2-nephi-1">2 Nephi 1</a></li>
<li><a href="/content/2-nephi-2">2 Nephi 2</a></li>
<li><a href="/content/2-nephi-3">2 Nephi 3</a></li>
<li><a href="/content/2-nephi-4">2 Nephi 4</a></li>
<li><a href="/content/2-nephi-5">2 Nephi 5</a></li>
<li><a href="/content/2-nephi-6">2 Nephi 6</a></li>
<li><a href="/content/2-nephi-7">2 Nephi 7</a></li>
<li><a href="/content/2-nephi-8">2 Nephi 8</a></li>
<li><a href="/content/2-nephi-9">2 Nephi 9</a></li>
<li><a href="/content/2-nephi-10">2 Nephi 10</a></li>
<li><a href="/content/2-nephi-11">2 Nephi 11</a></li>
<li><a href="/content/2-nephi-12">2 Nephi 12</a></li>
<li><a href="/content/2-nephi-13">2 Nephi 13</a></li>
<li><a href="/content/2-nephi-14">2 Nephi 14</a></li>
<li><a href="/content/2-nephi-15">2 Nephi 15</a></li>
<li><a href="/content/2-nephi-16">2 Nephi 16</a></li>
<li><a href="/content/2-nephi-17">2 Nephi 17</a></li>
<li><a href="/content/2-nephi-18">2 Nephi 18</a></li>
<li><a href="/content/2-nephi-19">2 Nephi 19</a></li>
<li><a href="/content/2-nephi-20">2 Nephi 20</a></li>
<li><a href="/content/2-nephi-21">2 Nephi 21</a></li>
<li><a href="/content/2-nephi-22">2 Nephi 22</a></li>
<li><a href="/content/2-nephi-23">2 Nephi 23</a></li>
<li><a href="/content/2-nephi-24">2 Nephi 24</a></li>
<li><a href="/content/2-nephi-25">2 Nephi 25</a></li>
<li><a href="/content/2-nephi-26">2 Nephi 26</a></li>
<li><a href="/content/2-nephi-27">2 Nephi 27</a></li>
<li><a href="/content/2-nephi-28">2 Nephi 28</a></li>
<li><a href="/content/2-nephi-29">2 Nephi 29</a></li>
<li><a href="/content/2-nephi-30">2 Nephi 30</a></li>
<li><a href="/content/2-nephi-31-0">2 Nephi 31</a></li>
<li><a href="/content/2-nephi-32">2 Nephi 32</a></li>
<li><a href="/content/2-nephi-33">2 Nephi 33</a></li>
<li><a href="/content/jacob-1">Jacob 1</a></li>
<li><a href="/content/jacob-2">Jacob 2</a></li>
<li><a href="/content/jacob-3">Jacob 3</a></li>
<li><a href="/content/jacob-4">Jacob 4</a></li>
<li><a href="/content/jacob-5">Jacob 5</a></li>
<li><a href="/content/jacob-6">Jacob 6</a></li>
<li><a href="/content/jacob-7">Jacob 7</a></li>
<li><a href="/content/enos-1">Enos 1</a></li>
<li><a href="/content/jarom-1">Jarom 1</a></li>
<li><a href="/content/omni-1">Omni 1</a></li>
<li><a href="/content/words-mormon-1">Words of Mormon 1</a></li>
<li><a href="/content/mosiah-1">Mosiah 1</a></li>
<li><a href="/content/mosiah-2">Mosiah 2</a></li>
<li><a href="/content/mosiah-3">Mosiah 3</a></li>
<li><a href="/content/mosiah-4">Mosiah 4</a></li>
<li><a href="/content/mosiah-5">Mosiah 5</a></li>
<li><a href="/content/mosiah-6">Mosiah 6</a></li>
<li><a href="/content/mosiah-7">Mosiah 7</a></li>
</ul></div>  </div>  </div>
    </div>






</div>    </div>




</div>
</section>
</div><div class="field field-name-biblio-citation field-type-ds field-label-hidden"><div class="field-items"><div class="field-item even"><section id="block-views-pdf-link-block-1" class="block block-views clearfix">

        <h2 class="block-title">Bibliographic Citation</h2>

  <div class="view view-pdf-link view-id-pdf_link view-display-id-block_1 view-dom-id-965103d43edc1f6c62ce6fa731c5e4b2">



      <div class="view-content">
        <div class="views-row views-row-1 views-row-odd views-row-first views-row-last">

  <div class="views-field views-field-citation">        <span class="field-content"><span class="biblio-authors"><a href="/biblio?f%5Bauthor%5D=446" rel="nofollow">Gardner, Brant A.</a>.</span> "<i><span class="biblio-title-chicago"><a href="/content/1-nephi-1" class="active">1 Nephi 1</a></span></i>." In <i>Book of Mormon Minute</i>. Springville, UT: Book of Mormon Central, 2019.<span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.atitle=1+Nephi+1&amp;rft.title=Book+of+Mormon+Minute&amp;rft.btitle=Book+of+Mormon+Minute&amp;rft.date=2019&amp;rft.aulast=Gardner&amp;rft.aufirst=Brant&amp;rft.pub=Book+of+Mormon+Central&amp;rft.place=Springville%2C+UT"></span></span>  </div>  </div>
    </div>






</div>
</section>
</div></div></div><div class="field-name-field-scripture-reference"><div class="field-label"><h2 class="label-above">Scripture Reference</h2></div><div class="field-items"><div class="field-item">1 Nephi 1:1-22</div></div></div><div class="field field-name-support-block field-type-ds field-label-hidden"><div class="field-items"><div class="field-item even"><section id="block-block-6" class="block block-block clearfix">


  <div class="subscribe-block archive">
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
</div></div></div>    </div>

  <div class="group-footer">
    <ul class="links list-inline"><li class="statistics_counter first"><span>109 reads</span></li>
<li class="0 last"><a href="http://scholar.google.com/scholar?btnG=Search%2BScholar&amp;as_q=%221%2BNephi%2B1%22&amp;as_sauthors=Gardner&amp;as_occt=any&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_sdtAAP=1&amp;as_sdtp=1" title="Click to search Google Scholar for this entry" rel="nofollow">Google Scholar</a></li>
</ul>  </div>

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
<section id="block-block-10" class="block block-block col-xs-12 col-md-4 clearfix">

        <h2 class="block-title">Our Vision</h2>

  <p>We build enduring faith in Jesus Christ by making the Book of Mormon accessible, comprehensible, and defensible to the entire world.</p>

</section>
<section id="block-social-media-links-social-media-links" class="block block-social-media-links clearfix">


  <ul class="social-media-links platforms inline horizontal"><li  class="facebook first"><a href="https://www.facebook.com/bookofmormoncentral/" title="Facebook"><img src="https://archive.bookofmormoncentral.org/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/facebook.png" alt="Facebook icon" /></a></li><li  class="twitter"><a href="http://www.twitter.com/bofmcentral" title="Twitter"><img src="https://archive.bookofmormoncentral.org/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/twitter.png" alt="Twitter icon" /></a></li><li  class="instagram"><a href="http://www.instagram.com/bookofmormoncentral/" title="Instagram"><img src="https://archive.bookofmormoncentral.org/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/instagram.png" alt="Instagram icon" /></a></li><li  class="pinterest"><a href="http://www.pinterest.com/BofMCentral" title="Pinterest"><img src="https://archive.bookofmormoncentral.org/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/pinterest.png" alt="Pinterest icon" /></a></li><li  class="vimeo"><a href="http://www.vimeo.com/bookofmormoncentral" title="Vimeo"><img src="https://archive.bookofmormoncentral.org/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/vimeo.png" alt="Vimeo icon" /></a></li><li  class="youtube_channel last"><a href="http://www.youtube.com/channel/UCSsrx8lFpeuBjNIE7FNm2CQ" title="Youtube (Channel)"><img src="https://archive.bookofmormoncentral.org/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/youtube.png" alt="Youtube (Channel) icon" /></a></li></ul>
</section>
  </div>
    <div class="copyright">Copyright 2023 Book of Mormon Central: A Non-Profit Organization. All rights reserved.<br />Registered 501(c)(3). EIN: 20-5294264</div>
  </footer>

<script>
  new WOW().init();
</script>  <script src="https://archive.bookofmormoncentral.org/sites/all/modules/lightbox2/js/auto_image_handling.js?s3mzmc"></script>
<script src="https://archive.bookofmormoncentral.org/sites/all/modules/lightbox2/js/lightbox.js?s3mzmc"></script>
<script src="https://archive.bookofmormoncentral.org/sites/all/themes/bootstrap/js/bootstrap.js?s3mzmc"></script>
</body>
</html>

"""


def test_load_bgbmm() -> None:
    """It returns a valid Document for a fair."""
    url = "https://archive.bookofmormoncentral.org/content/1-nephi-1"
    result = load_bgbmm(url, html)
    # expected_start = "**Summary**"
    assert len(result.page_content) > 0
    assert result.metadata["url"] == url
    assert result.metadata["title"] == "1 Nephi 1"
    # assert expected_start in result.page_content, f"Expected content to contain '{expected_start}', but it did not."
    assert result.page_content.startswith("## Episode 1")
