"""Test cases for the load_redeemer module."""
# flake8: noqa

from models import load_redeemer


html = """


<!DOCTYPE html>
<html class='v2' dir='ltr' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
<head>
<link href='https://www.blogger.com/static/v1/widgets/3566091532-css_bundle_v2.css' rel='stylesheet' type='text/css'/>
<meta content='IE=EmulateIE7' http-equiv='X-UA-Compatible'/>
<meta content='width=1100' name='viewport'/>
<meta content='text/html; charset=UTF-8' http-equiv='Content-Type'/>
<meta content='blogger' name='generator'/>
<link href='https://www.redeemerofisrael.org/favicon.ico' rel='icon' type='image/x-icon'/>
<link href='http://www.redeemerofisrael.org/' rel='canonical'/>
<link rel="alternate" type="application/atom+xml" title="Redeemer of Israel - Atom" href="https://www.redeemerofisrael.org/feeds/posts/default" />
<link rel="alternate" type="application/rss+xml" title="Redeemer of Israel - RSS" href="https://www.redeemerofisrael.org/feeds/posts/default?alt=rss" />
<link rel="service.post" type="application/atom+xml" title="Redeemer of Israel - Atom" href="https://www.blogger.com/feeds/4667816923565672485/posts/default" />
<link rel="me" href="https://www.blogger.com/profile/15148760171162762788" />
<!--Can't find substitution for tag [blog.ieCssRetrofitLinks]-->
<meta content='http://www.redeemerofisrael.org/' property='og:url'/>
<meta content='Redeemer of Israel' property='og:title'/>
<meta content='' property='og:description'/>
<title>Redeemer of Israel</title>
<style id='page-skin-1' type='text/css'><!--
/*-----------------------------------------------
Blogger Template Style
Name:     Picture Window
Designer: Josh Peterson
URL:      www.noaesthetic.com
----------------------------------------------- */
/* Variable definitions
====================
<Variable name="keycolor" description="Main Color" type="color" default="#1a222a"/>
<Variable name="body.background" description="Body Background" type="background"
color="#dddddd" default="#111111 url(//themes.googleusercontent.com/image?id=1OACCYOE0-eoTRTfsBuX1NMN9nz599ufI1Jh0CggPFA_sK80AGkIr8pLtYRpNUKPmwtEa) repeat-x fixed top center"/>
<Group description="Page Text" selector="body">
<Variable name="body.font" description="Font" type="font"
default="normal normal 15px Arial, Tahoma, Helvetica, FreeSans, sans-serif"/>
<Variable name="body.text.color" description="Text Color" type="color" default="#333333"/>
</Group>
<Group description="Backgrounds" selector=".body-fauxcolumns-outer">
<Variable name="body.background.color" description="Outer Background" type="color" default="#296695"/>
<Variable name="header.background.color" description="Header Background" type="color" default="transparent"/>
<Variable name="post.background.color" description="Post Background" type="color" default="#ffffff"/>
</Group>
<Group description="Links" selector=".main-outer">
<Variable name="link.color" description="Link Color" type="color" default="#336699"/>
<Variable name="link.visited.color" description="Visited Color" type="color" default="#6699cc"/>
<Variable name="link.hover.color" description="Hover Color" type="color" default="#33aaff"/>
</Group>
<Group description="Blog Title" selector=".header h1">
<Variable name="header.font" description="Title Font" type="font"
default="normal normal 36px Arial, Tahoma, Helvetica, FreeSans, sans-serif"/>
<Variable name="header.text.color" description="Text Color" type="color" default="#ffffff" />
</Group>
<Group description="Tabs Text" selector=".tabs-inner .widget li a">
<Variable name="tabs.font" description="Font" type="font"
default="normal normal 15px Arial, Tahoma, Helvetica, FreeSans, sans-serif"/>
<Variable name="tabs.text.color" description="Text Color" type="color" default="#ffffff"/>
<Variable name="tabs.selected.text.color" description="Selected Color" type="color" default="#992211"/>
</Group>
<Group description="Tabs Background" selector=".tabs-outer .PageList">
<Variable name="tabs.background.color" description="Background Color" type="color" default="transparent"/>
<Variable name="tabs.selected.background.color" description="Selected Color" type="color" default="transparent"/>
<Variable name="tabs.separator.color" description="Separator Color" type="color" default="transparent"/>
</Group>
<Group description="Post Title" selector="h3.post-title, .comments h4">
<Variable name="post.title.font" description="Title Font" type="font"
default="normal normal 18px Arial, Tahoma, Helvetica, FreeSans, sans-serif"/>
</Group>
<Group description="Date Header" selector=".date-header">
<Variable name="date.header.color" description="Text Color" type="color" default="#333333"/>
</Group>
<Group description="Post" selector=".post">
<Variable name="post.footer.text.color" description="Footer Text Color" type="color" default="#999999"/>
<Variable name="post.border.color" description="Border Color" type="color" default="#dddddd"/>
</Group>
<Group description="Gadgets" selector="h2">
<Variable name="widget.title.font" description="Title Font" type="font"
default="bold normal 13px Arial, Tahoma, Helvetica, FreeSans, sans-serif"/>
<Variable name="widget.title.text.color" description="Title Color" type="color" default="#888888"/>
</Group>
<Group description="Footer" selector=".footer-outer">
<Variable name="footer.text.color" description="Text Color" type="color" default="#cccccc"/>
<Variable name="footer.widget.title.text.color" description="Gadget Title Color" type="color" default="#aaaaaa"/>
</Group>
<Group description="Footer Links" selector=".footer-outer">
<Variable name="footer.link.color" description="Link Color" type="color" default="#99ccee"/>
<Variable name="footer.link.visited.color" description="Visited Color" type="color" default="#77aaee"/>
<Variable name="footer.link.hover.color" description="Hover Color" type="color" default="#33aaff"/>
</Group>
<Variable name="content.margin" description="Content Margin Top" type="length" default="20px"/>
<Variable name="content.padding" description="Content Padding" type="length" default="0"/>
<Variable name="content.background" description="Content Background" type="background"
default="transparent none repeat scroll top left"/>
<Variable name="content.border.radius" description="Content Border Radius" type="length" default="0"/>
<Variable name="content.shadow.spread" description="Content Shadow Spread" type="length" default="0"/>
<Variable name="header.padding" description="Header Padding" type="length" default="0"/>
<Variable name="header.background.gradient" description="Header Gradient" type="url"
default="none"/>
<Variable name="header.border.radius" description="Header Border Radius" type="length" default="0"/>
<Variable name="main.border.radius.top" description="Main Border Radius" type="length" default="20px"/>
<Variable name="footer.border.radius.top" description="Footer Border Radius Top" type="length" default="0"/>
<Variable name="footer.border.radius.bottom" description="Footer Border Radius Bottom" type="length" default="20px"/>
<Variable name="region.shadow.spread" description="Main and Footer Shadow Spread" type="length" default="3px"/>
<Variable name="region.shadow.offset" description="Main and Footer Shadow Offset" type="length" default="1px"/>
<Variable name="tabs.background.gradient" description="Tab Background Gradient" type="url" default="none"/>
<Variable name="tab.selected.background.gradient" description="Selected Tab Background" type="url"
default="url(//www.blogblog.com/1kt/transparent/white80.png)"/>
<Variable name="tab.background" description="Tab Background" type="background"
default="transparent url(//www.blogblog.com/1kt/transparent/black50.png) repeat scroll top left"/>
<Variable name="tab.border.radius" description="Tab Border Radius" type="length" default="10px" />
<Variable name="tab.first.border.radius" description="First Tab Border Radius" type="length" default="10px" />
<Variable name="tabs.border.radius" description="Tabs Border Radius" type="length" default="0" />
<Variable name="tabs.spacing" description="Tab Spacing" type="length" default=".25em"/>
<Variable name="tabs.margin.bottom" description="Tab Margin Bottom" type="length" default="0"/>
<Variable name="tabs.margin.sides" description="Tab Margin Sides" type="length" default="20px"/>
<Variable name="main.background" description="Main Background" type="background"
default="transparent url(//www.blogblog.com/1kt/transparent/white80.png) repeat scroll top left"/>
<Variable name="main.padding.sides" description="Main Padding Sides" type="length" default="20px"/>
<Variable name="footer.background" description="Footer Background" type="background"
default="transparent url(//www.blogblog.com/1kt/transparent/black50.png) repeat scroll top left"/>
<Variable name="post.margin.sides" description="Post Margin Sides" type="length" default="-20px"/>
<Variable name="post.border.radius" description="Post Border Radius" type="length" default="5px"/>
<Variable name="widget.title.text.transform" description="Widget Title Text Transform" type="string" default="uppercase"/>
<Variable name="mobile.background.overlay" description="Mobile Background Overlay" type="string"
default="transparent none repeat scroll top left"/>
<Variable name="startSide" description="Side where text starts in blog language" type="automatic" default="left"/>
<Variable name="endSide" description="Side where text ends in blog language" type="automatic" default="right"/>
*/
/* Content
----------------------------------------------- */
body, .body-fauxcolumn-outer {
font: normal normal 15px Arial, Tahoma, Helvetica, FreeSans, sans-serif;
color: #333333;
background: #dddddd url(//2.bp.blogspot.com/-TaEizMqaT7o/TgZEmqnropI/AAAAAAAAAbk/OjPtwyEtT7g/s0/Jerusalem-Sunset.jpg) repeat fixed top left;
}
html body .region-inner {
min-width: 0;
max-width: 100%;
width: auto;
}
.content-outer {
font-size: 90%;
}
a:link {
text-decoration:none;
color: #992211;
}
a:visited {
text-decoration:none;
color: #771100;
}
a:hover {
text-decoration:underline;
color: #cc4411;
}
.content-outer {
background: transparent url(//www.blogblog.com/1kt/transparent/white80.png) repeat scroll top left;
-moz-border-radius: 15px;
-webkit-border-radius: 15px;
-goog-ms-border-radius: 15px;
border-radius: 15px;
-moz-box-shadow: 0 0 3px rgba(0, 0, 0, .15);
-webkit-box-shadow: 0 0 3px rgba(0, 0, 0, .15);
-goog-ms-box-shadow: 0 0 3px rgba(0, 0, 0, .15);
box-shadow: 0 0 3px rgba(0, 0, 0, .15);
margin: 30px auto;
}
.content-inner {
padding: 15px;
}
/* Header
----------------------------------------------- */
.header-outer {
background: #992211 url(//www.blogblog.com/1kt/transparent/header_gradient_shade.png) repeat-x scroll top left;
_background-image: none;
color: #ffffff;
-moz-border-radius: 10px;
-webkit-border-radius: 10px;
-goog-ms-border-radius: 10px;
border-radius: 10px;
}
.Header img, .Header #header-inner {
-moz-border-radius: 10px;
-webkit-border-radius: 10px;
-goog-ms-border-radius: 10px;
border-radius: 10px;
}
.header-inner .Header .titlewrapper,
.header-inner .Header .descriptionwrapper {
padding-left: 30px;
padding-right: 30px;
}
.Header h1 {
font: normal normal 60px Arial, Tahoma, Helvetica, FreeSans, sans-serif;
text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
}
.Header h1 a {
color: #ffffff;
}
.Header .description {
font-size: 130%;
}
/* Tabs
----------------------------------------------- */
.tabs-inner {
margin: .5em 0 0;
padding: 0;
}
.tabs-inner .section {
margin: 0;
}
.tabs-inner .widget ul {
padding: 0;
background: #f5f5f5 url(//www.blogblog.com/1kt/transparent/tabs_gradient_shade.png) repeat scroll bottom;
-moz-border-radius: 10px;
-webkit-border-radius: 10px;
-goog-ms-border-radius: 10px;
border-radius: 10px;
}
.tabs-inner .widget li {
border: none;
}
.tabs-inner .widget li a {
display: inline-block;
padding: .5em 1em;
margin-right: 0;
color: #992211;
font: normal normal 15px Arial, Tahoma, Helvetica, FreeSans, sans-serif;
-moz-border-radius: 0 0 0 0;
-webkit-border-top-left-radius: 0;
-webkit-border-top-right-radius: 0;
-goog-ms-border-radius: 0 0 0 0;
border-radius: 0 0 0 0;
background: transparent none no-repeat scroll top left;
border-right: 1px solid #cccccc;
}
.tabs-inner .widget li:first-child a {
padding-left: 1.25em;
-moz-border-radius-topleft: 10px;
-moz-border-radius-bottomleft: 10px;
-webkit-border-top-left-radius: 10px;
-webkit-border-bottom-left-radius: 10px;
-goog-ms-border-top-left-radius: 10px;
-goog-ms-border-bottom-left-radius: 10px;
border-top-left-radius: 10px;
border-bottom-left-radius: 10px;
}
.tabs-inner .widget li.selected a,
.tabs-inner .widget li a:hover {
position: relative;
z-index: 1;
background: #ffffff url(//www.blogblog.com/1kt/transparent/tabs_gradient_shade.png) repeat scroll bottom;
color: #000000;
-moz-box-shadow: 0 0 0 rgba(0, 0, 0, .15);
-webkit-box-shadow: 0 0 0 rgba(0, 0, 0, .15);
-goog-ms-box-shadow: 0 0 0 rgba(0, 0, 0, .15);
box-shadow: 0 0 0 rgba(0, 0, 0, .15);
}
/* Headings
----------------------------------------------- */
h2 {
font: bold normal 13px Arial, Tahoma, Helvetica, FreeSans, sans-serif;
text-transform: uppercase;
color: #666666;
margin: .5em 0;
}
/* Main
----------------------------------------------- */
.main-outer {
background: transparent none repeat scroll top center;
-moz-border-radius: 0 0 0 0;
-webkit-border-top-left-radius: 0;
-webkit-border-top-right-radius: 0;
-webkit-border-bottom-left-radius: 0;
-webkit-border-bottom-right-radius: 0;
-goog-ms-border-radius: 0 0 0 0;
border-radius: 0 0 0 0;
-moz-box-shadow: 0 0 0 rgba(0, 0, 0, .15);
-webkit-box-shadow: 0 0 0 rgba(0, 0, 0, .15);
-goog-ms-box-shadow: 0 0 0 rgba(0, 0, 0, .15);
box-shadow: 0 0 0 rgba(0, 0, 0, .15);
}
.main-inner {
padding: 15px 5px 20px;
}
.main-inner .column-center-inner {
padding: 0 0;
}
.main-inner .column-left-inner {
padding-left: 0;
}
.main-inner .column-right-inner {
padding-right: 0;
}
/* Posts
----------------------------------------------- */
h3.post-title {
margin: 0;
font: normal normal 18px Arial, Tahoma, Helvetica, FreeSans, sans-serif;
}
.comments h4 {
margin: 1em 0 0;
font: normal normal 18px Arial, Tahoma, Helvetica, FreeSans, sans-serif;
}
.date-header span {
color: #333333;
}
.post-outer {
background-color: #ffffff;
border: solid 1px #dddddd;
-moz-border-radius: 10px;
-webkit-border-radius: 10px;
border-radius: 10px;
-goog-ms-border-radius: 10px;
padding: 15px 20px;
margin: 0 -20px 20px;
}
.post-body {
line-height: 1.4;
font-size: 110%;
position: relative;
}
.post-header {
margin: 0 0 1.5em;
color: #999999;
line-height: 1.6;
}
.post-footer {
margin: .5em 0 0;
color: #999999;
line-height: 1.6;
}
#blog-pager {
font-size: 140%
}
#comments .comment-author {
padding-top: 1.5em;
border-top: dashed 1px #ccc;
border-top: dashed 1px rgba(128, 128, 128, .5);
background-position: 0 1.5em;
}
#comments .comment-author:first-child {
padding-top: 0;
border-top: none;
}
.avatar-image-container {
margin: .2em 0 0;
}
/* Comments
----------------------------------------------- */
.comments .comments-content .icon.blog-author {
background-repeat: no-repeat;
background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEgAACxIB0t1+/AAAAAd0SU1FB9sLFwMeCjjhcOMAAAD+SURBVDjLtZSvTgNBEIe/WRRnm3U8RC1neQdsm1zSBIU9VVF1FkUguQQsD9ITmD7ECZIJSE4OZo9stoVjC/zc7ky+zH9hXwVwDpTAWWLrgS3QAe8AZgaAJI5zYAmc8r0G4AHYHQKVwII8PZrZFsBFkeRCABYiMh9BRUhnSkPTNCtVXYXURi1FpBDgArj8QU1eVXUzfnjv7yP7kwu1mYrkWlU33vs1QNu2qU8pwN0UpKoqokjWwCztrMuBhEhmh8bD5UDqur75asbcX0BGUB9/HAMB+r32hznJgXy2v0sGLBcyAJ1EK3LFcbo1s91JeLwAbwGYu7TP/3ZGfnXYPgAVNngtqatUNgAAAABJRU5ErkJggg==);
}
.comments .comments-content .loadmore a {
border-top: 1px solid #cc4411;
border-bottom: 1px solid #cc4411;
}
.comments .continue {
border-top: 2px solid #cc4411;
}
/* Widgets
----------------------------------------------- */
.widget ul, .widget #ArchiveList ul.flat {
padding: 0;
list-style: none;
}
.widget ul li, .widget #ArchiveList ul.flat li {
border-top: dashed 1px #ccc;
border-top: dashed 1px rgba(128, 128, 128, .5);
}
.widget ul li:first-child, .widget #ArchiveList ul.flat li:first-child {
border-top: none;
}
.widget .post-body ul {
list-style: disc;
}
.widget .post-body ul li {
border: none;
}
/* Footer
----------------------------------------------- */
.footer-outer {
color:#eeeeee;
background: transparent url(//www.blogblog.com/1kt/transparent/black50.png) repeat scroll top left;
-moz-border-radius: 10px 10px 10px 10px;
-webkit-border-top-left-radius: 10px;
-webkit-border-top-right-radius: 10px;
-webkit-border-bottom-left-radius: 10px;
-webkit-border-bottom-right-radius: 10px;
-goog-ms-border-radius: 10px 10px 10px 10px;
border-radius: 10px 10px 10px 10px;
-moz-box-shadow: 0 0 0 rgba(0, 0, 0, .15);
-webkit-box-shadow: 0 0 0 rgba(0, 0, 0, .15);
-goog-ms-box-shadow: 0 0 0 rgba(0, 0, 0, .15);
box-shadow: 0 0 0 rgba(0, 0, 0, .15);
}
.footer-inner {
padding: 10px 5px 20px;
}
.footer-outer a {
color: #ffffdd;
}
.footer-outer a:visited {
color: #cccc99;
}
.footer-outer a:hover {
color: #ffffff;
}
.footer-outer .widget h2 {
color: #bbbbbb;
}
/* Mobile
----------------------------------------------- */
html body.mobile {
height: auto;
}
html body.mobile {
min-height: 480px;
background-size: 100% auto;
}
.mobile .body-fauxcolumn-outer {
background: transparent none repeat scroll top left;
}
html .mobile .mobile-date-outer, html .mobile .blog-pager {
border-bottom: none;
background: transparent none repeat scroll top center;
margin-bottom: 10px;
}
.mobile .date-outer {
background: transparent none repeat scroll top center;
}
.mobile .header-outer, .mobile .main-outer,
.mobile .post-outer, .mobile .footer-outer {
-moz-border-radius: 0;
-webkit-border-radius: 0;
-goog-ms-border-radius: 0;
border-radius: 0;
}
.mobile .content-outer,
.mobile .main-outer,
.mobile .post-outer {
background: inherit;
border: none;
}
.mobile .content-outer {
font-size: 100%;
}
.mobile-link-button {
background-color: #992211;
}
.mobile-link-button a:link, .mobile-link-button a:visited {
color: #ffffff;
}
.mobile-index-contents {
color: #333333;
}
.mobile .tabs-inner .PageList .widget-content {
background: #ffffff url(//www.blogblog.com/1kt/transparent/tabs_gradient_shade.png) repeat scroll bottom;
color: #000000;
}
.mobile .tabs-inner .PageList .widget-content .pagelist-arrow {
border-left: 1px solid #cccccc;
}

--></style>
<style id='template-skin-1' type='text/css'><!--
body {
min-width: 920px;
}
.content-outer, .content-fauxcolumn-outer, .region-inner {
min-width: 920px;
max-width: 920px;
_width: 920px;
}
.main-inner .columns {
padding-left: 0;
padding-right: 180px;
}
.main-inner .fauxcolumn-center-outer {
left: 0;
right: 180px;
/* IE6 does not respect left and right together */
_width: expression(this.parentNode.offsetWidth -
parseInt("0") -
parseInt("180px") + 'px');
}
.main-inner .fauxcolumn-left-outer {
width: 0;
}
.main-inner .fauxcolumn-right-outer {
width: 180px;
}
.main-inner .column-left-outer {
width: 0;
right: 100%;
margin-left: -0;
}
.main-inner .column-right-outer {
width: 180px;
margin-right: -180px;
}
#layout {
min-width: 0;
}
#layout .content-outer {
min-width: 0;
width: 800px;
}
#layout .region-inner {
min-width: 0;
width: auto;
}
--></style>
<script type='text/javascript'>

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-12198915-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();



</script>
<link href='https://www.blogger.com/dyn-css/authorization.css?targetBlogID=4667816923565672485&amp;zx=86d269d7-629c-4265-bd16-445e383c2d83' media='none' onload='if(media!=&#39;all&#39;)media=&#39;all&#39;' rel='stylesheet'/><noscript><link href='https://www.blogger.com/dyn-css/authorization.css?targetBlogID=4667816923565672485&amp;zx=86d269d7-629c-4265-bd16-445e383c2d83' rel='stylesheet'/></noscript>
<meta name='google-adsense-platform-account' content='ca-host-pub-1556223355139109'/>
<meta name='google-adsense-platform-domain' content='blogspot.com'/>

</head>
<body class='loading'>
<div class='navbar section' id='navbar'><div class='widget Navbar' data-version='1' id='Navbar1'><script type="text/javascript">
    function setAttributeOnload(object, attribute, val) {
      if(window.addEventListener) {
        window.addEventListener('load',
          function(){ object[attribute] = val; }, false);
      } else {
        window.attachEvent('onload', function(){ object[attribute] = val; });
      }
    }
  </script>
<div id="navbar-iframe-container"></div>
<script type="text/javascript" src="https://apis.google.com/js/platform.js"></script>
<script type="text/javascript">
      gapi.load("gapi.iframes:gapi.iframes.style.bubble", function() {
        if (gapi.iframes && gapi.iframes.getContext) {
          gapi.iframes.getContext().openChild({
              url: 'https://www.blogger.com/navbar.g?targetBlogID\x3d4667816923565672485\x26blogName\x3dRedeemer+of+Israel\x26publishMode\x3dPUBLISH_MODE_HOSTED\x26navbarType\x3dLIGHT\x26layoutType\x3dLAYOUTS\x26searchRoot\x3dhttps://www.redeemerofisrael.org/search\x26blogLocale\x3den\x26v\x3d2\x26homepageUrl\x3dhttps://www.redeemerofisrael.org/\x26vt\x3d-6679262127714164091',
              where: document.getElementById("navbar-iframe-container"),
              id: "navbar-iframe"
          });
        }
      });
    </script><script type="text/javascript">
(function() {
var script = document.createElement('script');
script.type = 'text/javascript';
script.src = '//pagead2.googlesyndication.com/pagead/js/google_top_exp.js';
var head = document.getElementsByTagName('head')[0];
if (head) {
head.appendChild(script);
}})();
</script>
</div></div>
<div class='body-fauxcolumns'>
<div class='fauxcolumn-outer body-fauxcolumn-outer'>
<div class='cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left'>
<div class='fauxborder-right'></div>
<div class='fauxcolumn-inner'>
</div>
</div>
<div class='cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
</div>
<div class='content'>
<div class='content-fauxcolumns'>
<div class='fauxcolumn-outer content-fauxcolumn-outer'>
<div class='cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left'>
<div class='fauxborder-right'></div>
<div class='fauxcolumn-inner'>
</div>
</div>
<div class='cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
</div>
<div class='content-outer'>
<div class='content-cap-top cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left content-fauxborder-left'>
<div class='fauxborder-right content-fauxborder-right'></div>
<div class='content-inner'>
<header>
<div class='header-outer'>
<div class='header-cap-top cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left header-fauxborder-left'>
<div class='fauxborder-right header-fauxborder-right'></div>
<div class='region-inner header-inner'>
<div class='header section' id='header'><div class='widget Header' data-version='1' id='Header1'>
<div id='header-inner'>
<div class='titlewrapper'>
<h1 class='title'>
Redeemer of Israel
</h1>
</div>
<div class='descriptionwrapper'>
<p class='description'><span>
</span></p>
</div>
</div>
</div></div>
</div>
</div>
<div class='header-cap-bottom cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
</header>
<div class='tabs-outer'>
<div class='tabs-cap-top cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left tabs-fauxborder-left'>
<div class='fauxborder-right tabs-fauxborder-right'></div>
<div class='region-inner tabs-inner'>
<div class='tabs section' id='crosscol'><div class='widget PageList' data-version='1' id='PageList1'>
<h2>Pages</h2>
<div class='widget-content'>
<ul>
<li class='selected'>
<a href='https://www.redeemerofisrael.org/'>Home</a>
</li>
<li>
<a href='https://www.redeemerofisrael.org/p/holy-week.html'>Holy Week</a>
</li>
<li>
<a href='https://www.redeemerofisrael.org/p/passover.html'>Passover</a>
</li>
<li>
<a href='https://www.redeemerofisrael.org/p/christmas.html'>Christmas</a>
</li>
<li>
<a href='https://www.redeemerofisrael.org/p/blog-topics.html'>Blog Topics</a>
</li>
<li>
<a href='https://www.redeemerofisrael.org/p/visual-aids.html'>Visual Aids</a>
</li>
<li>
<a href='https://www.redeemerofisrael.org/p/about-me.html'>About Me</a>
</li>
<li>
<a href='https://www.redeemerofisrael.org/p/email-signup.html'>Email Signup</a>
</li>
</ul>
<div class='clear'></div>
</div>
</div></div>
<div class='tabs no-items section' id='crosscol-overflow'></div>
</div>
</div>
<div class='tabs-cap-bottom cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
<div class='main-outer'>
<div class='main-cap-top cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left main-fauxborder-left'>
<div class='fauxborder-right main-fauxborder-right'></div>
<div class='region-inner main-inner'>
<div class='columns fauxcolumns'>
<div class='fauxcolumn-outer fauxcolumn-center-outer'>
<div class='cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left'>
<div class='fauxborder-right'></div>
<div class='fauxcolumn-inner'>
</div>
</div>
<div class='cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
<div class='fauxcolumn-outer fauxcolumn-left-outer'>
<div class='cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left'>
<div class='fauxborder-right'></div>
<div class='fauxcolumn-inner'>
</div>
</div>
<div class='cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
<div class='fauxcolumn-outer fauxcolumn-right-outer'>
<div class='cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left'>
<div class='fauxborder-right'></div>
<div class='fauxcolumn-inner'>
</div>
</div>
<div class='cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
<!-- corrects IE6 width calculation -->
<div class='columns-inner'>
<div class='column-center-outer'>
<div class='column-center-inner'>
<div class='main section' id='main'><div class='widget Blog' data-version='1' id='Blog1'>
<div class='blog-posts hfeed'>

          <div class="date-outer">

<h2 class='date-header'><span>November 12, 2023</span></h2>

          <div class="date-posts">

<div class='post-outer'>
<div class='post hentry'>
<a name='4655270520604121467'></a>
<h3 class='post-title entry-title'>
<a href='https://www.redeemerofisrael.org/2023/11/finding-christ-in-ark-of-covenant.html'>Finding Christ in the Ark of the Covenant</a>
</h3>
<div class='post-header'>
<div class='post-header-line-1'></div>
</div>
<div class='post-body entry-content' id='post-body-4655270520604121467'>
<p style="text-align: center;">&nbsp;<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/3a9g8Q7_Wpk?si=FWBtpeErRKjGgqMy&amp;controls=0" title="YouTube video player" width="560"></iframe></p><p>The Ark of the Covenant is perhaps one of the most sacred and well-known artifacts from the pages of the Bible. Countless movies and documentaries have been made discussing its mystical power and supposed whereabouts. While we won&#8217;t attempt to answer what may have happened to the Ark over the centuries, we will discuss why this holy object was so significant and how it can teach us about the atoning power of Jesus Christ.</p><p>First, it may be helpful to give a bit of context about the ancient Israelite Tabernacle, where the ark was first placed. While Moses was on Mount Sinai, the Lord appeared to him and gave him tablets of stone, upon which were engraved the Ten Commandments. These essential laws represented God&#8217;s covenant with Israel. If the people would obey God, he would provide for them, give them his priesthood power, and allow all who were worthy to enter his presence. They would become a &#8220;kingdom of priests, and an holy nation&#8221; (<a href="https://www.churchofjesuschrist.org/study/scriptures/ot/ex/19?lang=eng&amp;id=6#p6" target="_blank">Exodus 19:6</a>).</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdm3ZqM7dzcpRo0biA6nDx6HMAyLah8ttA5FbCb-QN5brIb2pczJMwTLvp7s0s7pZRT90xa9HTPjlMFHucNhruavHxqkYnZ4PaWhWjkACNVJN4ZvKWzznO6RPX3uLk6loG8mrHLNKwaFSMkwP9r8EqHXIAtR1raCGGqo-fNQ2vE6gIlPFNxEjrONvo32HV/s2667/Moses%20with%20ten%20commandments.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdm3ZqM7dzcpRo0biA6nDx6HMAyLah8ttA5FbCb-QN5brIb2pczJMwTLvp7s0s7pZRT90xa9HTPjlMFHucNhruavHxqkYnZ4PaWhWjkACNVJN4ZvKWzznO6RPX3uLk6loG8mrHLNKwaFSMkwP9r8EqHXIAtR1raCGGqo-fNQ2vE6gIlPFNxEjrONvo32HV/w640-h360/Moses%20with%20ten%20commandments.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Moses with the Ten Commandments (photo by <a href="https://www.appianmedia.org/" target="_blank">Appian Media</a>)</td></tr></tbody></table><p>However, seeing the thunderings and lightning on Mount Sinai, the people were fearful and instead asked that Moses speak with the Lord on their behalf (<a href="https://www.churchofjesuschrist.org/study/scriptures/ot/ex/20-21?lang=eng&amp;id=18#p18" target="_blank">Exodus 20:18&#8211;21</a>). In other words, because of doubt and fear, they rejected the opportunity to enter God&#8217;s presence. As a temporary solution, the Lord commanded that Aaron, the high priest, would go on their behalf, acting as a mediator between the people and their God.</p><p>To facilitate this process, the Lord commanded Moses to build a Tabernacle in the wilderness. It served as a prototype for returning to God&#8217;s presence, showing Israel how to symbolically enter into sacred space through the mediation of God&#8217;s appointed priests. As worshipers approached the Tabernacle, they could only enter through the colorful gate on the east side. It taught Israel that there was only one entrance to begin their journey back to God. Next was found the altar of sacrifice, where Israel was taught that it was only through the shedding of blood that they could become reconciled with God. In front of the altar was the bronze laver, where the priests ritually washed their hands and feet before entering the Tabernacle, symbolizing the need for spiritual purity.</p><p>Upon entering the main structure into the room called the holy place, the priests encountered the beautiful golden menorah, the table of showbread with its twelve loaves of bread, and the golden altar of incense. These objects represented light, nourishment, and the ability to pray and address God before the veil. At the far end of the room was a large veil embroidered with cherubim, or angelic beings, who guarded the presence of God. Only the high priest could go beyond the veil, and only on one day a year, called the Day of Atonement.</p><p>&nbsp;After passing through the veil, the high priest encountered the Ark of the Covenant at the center of a room called the Holy of Holies. This most sacred space is where the Lord would commune with his people, and where the high priest would ritually intercede on their behalf.&nbsp;</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLSZ8ttONVCDTWxzO5edN8Wz7l7ihyphenhyphen0k50r9o8n2lfK6YvVr4G3BBcaG64iJRjRDUBp5O-VaZNIVp5mQRlYdmu8Afwyn2Ri1dIbLDMSH6wlbHWGYu_Ldf6BxrUtcgpPJofVSWXmEkuh63TT1UbOoFSlkhZ4fiwClq0LMP_yjbUjtew7qfeseyYU7Tpv9JK/s2048/High%20Priest%20with%20blood%2001.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1365" data-original-width="2048" height="426" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLSZ8ttONVCDTWxzO5edN8Wz7l7ihyphenhyphen0k50r9o8n2lfK6YvVr4G3BBcaG64iJRjRDUBp5O-VaZNIVp5mQRlYdmu8Afwyn2Ri1dIbLDMSH6wlbHWGYu_Ldf6BxrUtcgpPJofVSWXmEkuh63TT1UbOoFSlkhZ4fiwClq0LMP_yjbUjtew7qfeseyYU7Tpv9JK/w640-h426/High%20Priest%20with%20blood%2001.JPG" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">The high priest entering the Holy of Holies on the Day of Atonement</td></tr></tbody></table><p>With this background, let&#8217;s now talk about the actual Ark itself. The Ark of the Covenant was a wooden box made from acacia (or shittim wood) overlaid with gold. The acacia tree is one of the few trees that grow in the deserts where the children of Israel wandered for 40 years. Because of the harsh climate with little moisture and scorching heat, the acacia wood is extremely durable and is an excellent choice for such a precious piece of furniture. Some writers have suggested that the durable desert acacia wood overlaid with gold could be a symbol of the Savior, who was raised in the dry land of Israel (see <a href="https://www.churchofjesuschrist.org/study/scriptures/ot/isa/53?lang=eng&amp;id=2#p2" target="_blank">Isaiah 53:2</a>) yet overlaid with the divinity of God. (David Levy, The Tabernacle, 26).</p><p>The box was rectangular in shape and around the size of a hope chest or seaman&#8217;s chest. On the top was the mercy seat, a solid gold lid that had two beautiful cherubim hammered and shaped from the gold. On the sides were four gold rings where two poles could be inserted to carry the ark. These staves, unlike the poles for the other Tabernacle furniture, were never to be removed from the rings (<a href="https://www.churchofjesuschrist.org/study/scriptures/ot/ex/25?lang=eng&amp;id=15#p15" target="_blank">Exodus 25:15</a>).</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6dsBmIssfJA7RIK0Y7CVziVSS3677gRoIvy3HfpE2L0KJdomc-hspg8d136kSxufpw9T1vJcoOxgc_F0Q1Q1Vhtd1AqeJCORpilzP-QSuyRme78eFI8hV_9oI-Gkl_MEWc9u8zY2poApHfkGUWkh0ujO2HS6qZvfOf-RidqplfYOsTN81rLIORnSwiaDC/s2667/Ark%20of%20the%20covenant.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6dsBmIssfJA7RIK0Y7CVziVSS3677gRoIvy3HfpE2L0KJdomc-hspg8d136kSxufpw9T1vJcoOxgc_F0Q1Q1Vhtd1AqeJCORpilzP-QSuyRme78eFI8hV_9oI-Gkl_MEWc9u8zY2poApHfkGUWkh0ujO2HS6qZvfOf-RidqplfYOsTN81rLIORnSwiaDC/w640-h360/Ark%20of%20the%20covenant.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">The Ark of the Covenant in the Holy of Holies of the Tabernacle</td></tr></tbody></table><p>The placement of the Ark at the center of the Holy of Holies hints at its supreme importance. As part of the sacred ritual for the Day of Atonement, the high priest would select two goats, and draw lots on each of them. One, called the scapegoat, would have all the sins of Israel symbolically placed on its head, and then the goat would be driven into the wilderness to die. The other goat was sacrificed, and its blood was taken into the Holy of Holies and sprinkled on the Ark of the Covenant seven times. The word atonement comes from the Hebrew word, kaphar, which means to cover or blot out. The ritual taught Israel that it was only through the shedding of blood that one could enter the presence of God.</p><p>Inside the box was stored a bowl of manna, the stone tablets, and the rod of Aaron that had blossomed (<a href="https://www.churchofjesuschrist.org/study/scriptures/nt/heb/9?lang=eng&amp;id=4#p4" target="_blank">Hebrews 9:4</a>). It was called the Ark of the Covenant, because these three sacred relics reminded or commemorated the covenant made between the Lord and his people.</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikoO0jn-DUvBVXLM4aBsTMxYgpMJgKO_OFCTfEzIh2WLcw0Q6eygHfLc9CpBCqnMtVpTjnDDk43D1hTRbN7qnOCAvj2jD5q3YfVZ8TKsKT3i9RnZNPF22nxWy-yxyE9WAi9651Kv9XWQY-2jolKzoriHZYh4wDFN_SWFmyDyJ4TVCWejwqRw5KAkWLcY3H/s2667/Items%20inside%20of%20ark%20of%20covenant.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikoO0jn-DUvBVXLM4aBsTMxYgpMJgKO_OFCTfEzIh2WLcw0Q6eygHfLc9CpBCqnMtVpTjnDDk43D1hTRbN7qnOCAvj2jD5q3YfVZ8TKsKT3i9RnZNPF22nxWy-yxyE9WAi9651Kv9XWQY-2jolKzoriHZYh4wDFN_SWFmyDyJ4TVCWejwqRw5KAkWLcY3H/w640-h360/Items%20inside%20of%20ark%20of%20covenant.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">The tablets of stone, bowl of manna, and rod of Aaron inside the Ark of the Covenant</td></tr></tbody></table><p>The bowl of manna symbolized God&#8217;s providence. It was a physical reminder that the Lord had given daily bread to Israel during their time in the desolate wilderness. The Savior, after feeding the 5000, taught that while God had provided manna for Israel, they all had died. He then identified himself as the true and eternally enduring manna from heaven, stating, &#8220;I am the bread of life: he that cometh to me shall never hunger.&#8221; (John 6:35).&nbsp;</p><p>The two tablets of stone contained the Ten Commandments, as given to Moses by the Lord. As mentioned, God promised that if Israel would obey his laws, then he would protect them. Recall, however, that these laws&#8212;which everyone but Jesus Christ has broken to some degree or another&#8212;were covered by the mercy seat. It is almost as if the stone tablets are to remind us that while God&#8217;s laws of justice are enduring, they can be superseded or overpowered by his mercy. This was symbolized by the high priest sprinkling the blood of the sacrifice on the mercy seat, representing the blood of Christ which mercifully protects his true followers from the full punishment of the law.&nbsp;</p><p>The rod of Aaron was placed inside the ark to remind Israel of the priesthood power that came through Aaron. When Israel had questioned the authority of Aaron and the tribe of Levi, God commanded that a staff from every tribe was to be brought to the Tabernacle. Each rod was placed before the ark, but only the rod of Aaron blossomed. It was a powerful witness, showing that only the tribe of Levi, who Aaron represented, was authorized to perform priesthood rituals on behalf of the people.</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjGheNJnRkh71Vx9EPz3wwwVMF9Rj6H-I3ozDwIi75FEZHt_wQoYpigPlaFoxPfeNT-Q_2rtDkaEG5OJM4rK0RPlz1IaYOUgFdjM1R1FuukOQfTcCYxucfH-uYsXdQa5SeTAIo5ss0X19G0fwyvyEmze4KPjqBU6FT9v7HD2-5H-IIkJ2RTes2zdkM_T-sv/s2667/Rod%20of%20Aaron%20blossoming.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjGheNJnRkh71Vx9EPz3wwwVMF9Rj6H-I3ozDwIi75FEZHt_wQoYpigPlaFoxPfeNT-Q_2rtDkaEG5OJM4rK0RPlz1IaYOUgFdjM1R1FuukOQfTcCYxucfH-uYsXdQa5SeTAIo5ss0X19G0fwyvyEmze4KPjqBU6FT9v7HD2-5H-IIkJ2RTes2zdkM_T-sv/w640-h360/Rod%20of%20Aaron%20blossoming.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">The rod of Aaron with the other tribal rods placed before the Ark of the Covenant</td></tr></tbody></table><p>In a way, the Ark of the Covenant can almost be seen as a type of safety deposit box. It held some of the most significant historical relics of Israel&#8217;s past, providing an enduring testament of his covenantal promises. These physical objects, situated at the center of the Holy of Holies, reminded them of God&#8217;s law and teachings, of his appointed priesthood authority to govern his people, and of his promise to nourish and protect them if they would only keep their covenants. Perhaps most important of all is that these items were covered by the mercy seat, showing that God&#8217;s laws, ordinances, and blessings are all facilitated through the merciful and atoning blood of Jesus Christ&#8212;the true Lamb of God.&nbsp;</p><p>In the book of Hebrews, the writer describes in great detail the Tabernacle and ancient rituals. He explains that the high priest had to enter the Holy of Holies each year to make atonement for sin. This showed that this ordnance was not permanent or final, but had to be repeated on a regular basis. He then explains how Jesus Christ is our Great High Priest, who only had to enter once and for all (see <a href="https://www.churchofjesuschrist.org/study/scriptures/nt/heb/9?lang=eng&amp;id=12#p12" target="_blank">Hebrews 9:12</a>). When the Savior gave his life, there was no more need for animal sacrifice. Atonement had been made and will cover all who repent of their sins and place their faith in Christ. The writer of Hebrews then gives these powerful words regarding entering the Holy of Holies, &#8220;Let us therefore come boldly to the throne of grace, that we may obtain mercy and find grace to help in time of need&#8221; (<a href="https://www.churchofjesuschrist.org/study/scriptures/nt/heb/4?lang=eng&amp;id=16#p16" target="_blank">Hebrews 4:16</a>).</p><p>How grateful we all can be, that we have a Great High Priest, even Jesus Christ, who has taken the sins of the world upon him. Like the ancient high priest, the Savior mediates between us and God, and because of his blood that he shed in Gethsemane and on the cross, we can all return to the presence of the Father, purified and without fear!</p>
<div style='clear: both;'></div>
</div>
<div class='post-footer'>
<div class='post-footer-line post-footer-line-1'><span class='post-comment-link'>
<a class='comment-link' href='https://www.redeemerofisrael.org/2023/11/finding-christ-in-ark-of-covenant.html#comment-form' onclick=''>0
comments</a>
</span>
<span class='post-icons'>
<span class='item-action'>
<a href='https://www.blogger.com/email-post.g?blogID=4667816923565672485&postID=4655270520604121467' title='Email Post'>
<img alt="" class="icon-action" height="13" src="//img1.blogblog.com/img/icon18_email.gif" width="18">
</a>
</span>
</span>
<div class='post-share-buttons goog-inline-block'>
<a class='goog-inline-block share-button sb-email' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=4655270520604121467&target=email' target='_blank' title='Email This'><span class='share-button-link-text'>Email This</span></a><a class='goog-inline-block share-button sb-blog' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=4655270520604121467&target=blog' onclick='window.open(this.href, "_blank", "height=270,width=475"); return false;' target='_blank' title='BlogThis!'><span class='share-button-link-text'>BlogThis!</span></a><a class='goog-inline-block share-button sb-twitter' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=4655270520604121467&target=twitter' target='_blank' title='Share to Twitter'><span class='share-button-link-text'>Share to Twitter</span></a><a class='goog-inline-block share-button sb-facebook' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=4655270520604121467&target=facebook' onclick='window.open(this.href, "_blank", "height=430,width=640"); return false;' target='_blank' title='Share to Facebook'><span class='share-button-link-text'>Share to Facebook</span></a><a class='goog-inline-block share-button sb-pinterest' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=4655270520604121467&target=pinterest' target='_blank' title='Share to Pinterest'><span class='share-button-link-text'>Share to Pinterest</span></a>
</div>
</div>
<div class='post-footer-line post-footer-line-2'></div>
<div class='post-footer-line post-footer-line-3'></div>
</div>
</div>
</div>

          </div></div>


          <div class="date-outer">

<h2 class='date-header'><span>May 21, 2023</span></h2>

          <div class="date-posts">

<div class='post-outer'>
<div class='post hentry'>
<a name='742267067073565596'></a>
<h3 class='post-title entry-title'>
<a href='https://www.redeemerofisrael.org/2023/05/the-widows-mite.html'>The Widow's Mite</a>
</h3>
<div class='post-header'>
<div class='post-header-line-1'></div>
</div>
<div class='post-body entry-content' id='post-body-742267067073565596'>
<p style="text-align: center;"><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/FQzQ9YfONAE?controls=0" title="YouTube video player" width="560"></iframe></p><p>The story of the widow&#8217;s mite is widely viewed as a model of true and meaningful sacrifice. This woman&#8217;s example teaches us that it is far more important where our heart is when we give than the amount of our gift. If we give or serve out of love and devotion to God, then even a small gift can be a great sacrifice.</p><p>To more fully appreciate the significance of this widow&#8217;s donation, let&#8217;s explore its historical setting.[1] First, we&#8217;ll look at where the story took place: the temple in Jerusalem.</p><p>During the time of Christ, the temple was in the middle of an over 80-year reconstruction project that began under King Herod and was thus known as Herod&#8217;s Temple.[2] As one of the largest structures in the world at that time, its beauty and grandeur was beyond comparison. High on the hilltop of Mount Moriah it could be seen for miles round about Jerusalem.&nbsp;</p><p>While the temple itself stood at a majestic 150 feet tall, the temple complex was also massive, totaling about 37 acres, or approximately the equivalent of 26 football fields. Understandably, a project this extensive was quite costly, requiring significant donations and taxes from the people.&nbsp;</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh17RsnSfZY_2hd_W76WO14IIBM1KuK00_ugViA6UT5e23vRg0LdYlA3gE4L1LdI44axHPvweg6iRADjA7yEytmQvBea08-y1Im-uOP_Z_BwKxoeHT52nyQou8jUwsgWFaEgA0RmwZjD7ixnRZ0YXNkw_WSrxxU9JCHKe2txWYwWN2UB_PDNhBE6KqcwA/s2667/Court%20of%20the%20women.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh17RsnSfZY_2hd_W76WO14IIBM1KuK00_ugViA6UT5e23vRg0LdYlA3gE4L1LdI44axHPvweg6iRADjA7yEytmQvBea08-y1Im-uOP_Z_BwKxoeHT52nyQou8jUwsgWFaEgA0RmwZjD7ixnRZ0YXNkw_WSrxxU9JCHKe2txWYwWN2UB_PDNhBE6KqcwA/w640-h360/Court%20of%20the%20women.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Court of the Women in the temple of Herod</td></tr></tbody></table><p>Towards the center of the temple complex was the court of the women, also known as the treasury (see for example Mark 12:41 and John 8:20). Thirteen collection boxes were placed here, each chest labeled for the various types of offerings that could be given.[3] On top of each box was a trumpet-shaped receptacle where donations could be made. As one can imagine, the coins falling down the shaft of the trumpet made a noise loud enough for others to hear. The larger the donation, the louder the sound. When teaching his followers about almsgiving, Christ may have been referring to these money boxes when stating, &#8220;do not sound a trumpet before thee, as the hypocrites do ... that they may have glory of men. Verily I say unto you, They have their reward.&#8221; (Matthew 6:2).</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgO_QVNOkCs3JYh91nCMi9eoaQeJClswWR0qp83lfPlXb-7tH55B2yxWZu9mRvJF1GQjAjMYEFMKynXF_bT2a-_X1xF79l3s-n0mdyT0LqyXJoPK3hW-oD2daCn5wv9XcepIgKKTGnnW_6PSYkVyh4gL0b38RsZCClmpLdBDlt635vjl6DnRirFMCRO0g/s2667/Trumpet%20shaped%20donation%20box.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgO_QVNOkCs3JYh91nCMi9eoaQeJClswWR0qp83lfPlXb-7tH55B2yxWZu9mRvJF1GQjAjMYEFMKynXF_bT2a-_X1xF79l3s-n0mdyT0LqyXJoPK3hW-oD2daCn5wv9XcepIgKKTGnnW_6PSYkVyh4gL0b38RsZCClmpLdBDlt635vjl6DnRirFMCRO0g/w640-h360/Trumpet%20shaped%20donation%20box.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">The trumpet shaped donation boxes in the Court of the Women</td></tr></tbody></table><p>The temple was meant to be a place where God&#8217;s people could come to worship, make sacrifices, and learn to serve others. Instead, it was being corrupted by pride and hypocrisy&#8212;especially among the wealthy and religious elite.&nbsp;</p><p>With this temple setting in mind, let&#8217;s now consider when the widow&#8217;s donation occurred.&nbsp;</p><p>The Savior&#8217;s observance of this woman took place during the last week of his life, now known as Holy Week. At this time, Jews from all over came to Jerusalem to celebrate the Passover. And for many pilgrims, this involved paying taxes and making donations at the temple.&nbsp;</p><p>While anyone could freely donate any amount into the designated boxes, all Jewish males were required to pay a half-shekel once each year. The temple authorities, however, required that inferior Jewish coins be exchanged for Roman coins which had a higher percentage of silver. In order to make an exchange, the people were charged about an 8% fee, which was most likely pocketed by the corrupt temple priests along with a portion of the collected donations.[4]</p><p>When Jesus encountered this type of corruption at the temple, he overturned the tables where the money was exchanged, proclaiming they had made his Father&#8217;s house into a den of thieves (Matthew 21:13).&nbsp;</p><p>Yet this isn&#8217;t the only money-related teaching leading up to the story of the widow&#8217;s mite. There&#8217;s also the account of a rich man named Zacchæus (Luke 19:1-11), the parable of the pounds (Luke 19:12-26), and Christ&#8217;s teachings about taxes (Luke 20:20-26). And then just before the story of the widow&#8217;s mite, Jesus gives this powerful rebuke: &#8220;Beware of the scribes, which desire &#8230; the highest seats in the synagogues, &#8230; which devour widows&#8217; houses, and for a shew make long prayers: the same shall receive greater damnation.&#8221; (Luke 20:46-47 KJV).</p><p>Together these teachings make it clear that Jesus wasn&#8217;t happy with the attitudes towards wealth and status that were being promoted by the religious leaders of the day.&nbsp;</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGsHm_aeFRJYNEP7aa2QENguryWv512kuiPQyVVHpqgYMv5rlt0y65kXyn8eALUvkz-6JpnUtBqHPpIqfvGuN4MzYAwXcT5BQZV6djDxGAYflIkZpFcPzKjmst9F41iIIc8GumZYNE_C65m0Gm5gsEYygwPehPsKLMrlskAzlNA3mfS5vngYGSreE6nA/s2667/Court%20of%20women%20porch.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGsHm_aeFRJYNEP7aa2QENguryWv512kuiPQyVVHpqgYMv5rlt0y65kXyn8eALUvkz-6JpnUtBqHPpIqfvGuN4MzYAwXcT5BQZV6djDxGAYflIkZpFcPzKjmst9F41iIIc8GumZYNE_C65m0Gm5gsEYygwPehPsKLMrlskAzlNA3mfS5vngYGSreE6nA/w640-h360/Court%20of%20women%20porch.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Decorative opus sectile floors under the porch of the Court of the Women</td></tr></tbody></table><p>With this context in mind, let&#8217;s take a closer look at the story of the widow&#8217;s mite. As Jesus was teaching at the temple during his final week, he looked up and saw rich men casting their coins noisily into the donation boxes. But then he noticed another coming to make her own donation. She was a poor widow. Surrounded by the beautiful grandeur of the temple, she approached the court of the women and offered all that she had. But it was only two mites&#8212;what an average wage earner would receive for just about 12 minutes of labor.[5] Unlike the repeated and noisy clanking of larger coins made by wealthy patrons, her meager donation would have been almost imperceptible as it fell into the box below.&nbsp;</p><p>Yet Jesus taught that this widow had put in more than all the others. For they &#8220;gave their gifts out of their wealth; but she out of her poverty put in all she had to live on.&#8221;&nbsp;(Luke 21:3-4 NIV). In other words, it isn&#8217;t the worldly worth of a gift that matters, but rather the degree of personal sacrifice and devotion involved. Whether we are a poor widow or a rich young ruler, God wants us to be willing, if needed, to give up everything to follow him. The irony is that the law of Moses teaches that widows are to be cared for, but it is this woman who is freely giving to the very ones who should be caring for her.&nbsp;</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_Vl1SRjm7m4AnZvTc201IRVeHhiSH-cV9FyOfMW9tsCNp4NAghQN78fa6dPB_ZGRAsRQxRMEem7u-QSTHYfBAdVMHUupNKrMzISMpYIoTC5zceFQwCgJPAwTiV2GJQFNCAxY0NuB_McQXE09DhhUYEeCSeXEvxoGWShZlT-Vg6ZefIE5a2w-sQF-2pw/s5200/The%20pharisee%20and%20the%20poor%20widow.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="2803" data-original-width="5200" height="344" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_Vl1SRjm7m4AnZvTc201IRVeHhiSH-cV9FyOfMW9tsCNp4NAghQN78fa6dPB_ZGRAsRQxRMEem7u-QSTHYfBAdVMHUupNKrMzISMpYIoTC5zceFQwCgJPAwTiV2GJQFNCAxY0NuB_McQXE09DhhUYEeCSeXEvxoGWShZlT-Vg6ZefIE5a2w-sQF-2pw/w640-h344/The%20pharisee%20and%20the%20poor%20widow.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">The widow giving her two mites in the temple treasury by Milo Winter</td></tr></tbody></table><p>There&#8217;s more to the message, though, for Jesus knew that despite the efforts being made to renovate the temple, in only a few decades it would be destroyed. Directly following His teachings about the widow, He prophesied of the temple that &#8220;the time will come when not one stone will be left on another; every one of them will be thrown down.&#8221; (Luke 21:6 NIV).&nbsp;&nbsp;</p><p>For his listeners who were marveling at that very moment at the beauty and splendor of the temple, this must have been a shocking and disturbing message. How could such devastation come to such a holy place? And why would God allow it? The answer, at least in part, may be that it wasn&#8217;t nearly as holy as the people thought.&nbsp;</p><p>Unlike this widow, who humbly consecrated all she had towards establishing the house of the Lord, the Scribes and Pharisees were making unacceptable offerings. In their pride and greed, they were desecrating the temple and using it to their personal advantage. So, God would eventually take the temple from them, much like they were defrauding poor widows out of their property. This prophesied destruction took place nearly 40 years later by a Roman army, who indeed dismantled the temple block by block.</p><p>As typified by the destruction of the temple, attitudes of pride and greed have a tendency to destroy the very things they are trying to lift up. In the end, God is simply not impressed by those who loudly proclaim their generosity while ignoring those suffering nearby.&nbsp;</p><p>The poor widow who cast in her two mites may not have thought much of her meager offering. Perhaps she thought no one noticed. But Jesus did. Our Father in Heaven sees every good thing we do. He knows our hearts and minds. He sees our sacrifices and efforts, no matter how small or unimportant they may outwardly seem. Buildings may be destroyed, legacies may be forgotten, leaders may fall, but our humble service rendered to others will always be seen and remembered by the Lord.</p><p><i>Script written by Heather Ruth Pack and edited by Ryan Dahle</i></p><p>________________________________________</p><p>[1] The terms &#8220;mite&#8221; and &#8220;farthing&#8221; are used in the King James Version as they are British terms to denote a coin with low value. During the time of Christ, the widow would have donated a lepton or two lepta, a small, crude coin used in Judea.&nbsp;</p><p>[2] The construction of Herod&#8217;s temple began in 20 B.C. and was completed before the Jewish revolt in 66 A.D. It was destroyed by Romans in 70 A.D.&nbsp;</p><p>[3] The boxes were used for various donations such as new shekel dues, wood, bird offering, frankincense, gold for the mercy seat, and six for free-will offerings.&nbsp;</p><p>[4] Richard Neitzel Holzaphel, Jesus Christ and the World of the New Testament, pg. 122.</p><p>[5] <a href="https://en.wikipedia.org/wiki/Lesson_of_the_widow%27s_mite#:~:text=The%20Gospel%20of%20Mark%20specifies,of%20an%20average%20daily%20wage." target="_blank">Lesson of the widow&#8217;s mite</a>, Wikipedia.</p><p></p>
<div style='clear: both;'></div>
</div>
<div class='post-footer'>
<div class='post-footer-line post-footer-line-1'><span class='post-comment-link'>
<a class='comment-link' href='https://www.redeemerofisrael.org/2023/05/the-widows-mite.html#comment-form' onclick=''>0
comments</a>
</span>
<span class='post-icons'>
<span class='item-action'>
<a href='https://www.blogger.com/email-post.g?blogID=4667816923565672485&postID=742267067073565596' title='Email Post'>
<img alt="" class="icon-action" height="13" src="//img1.blogblog.com/img/icon18_email.gif" width="18">
</a>
</span>
</span>
<div class='post-share-buttons goog-inline-block'>
<a class='goog-inline-block share-button sb-email' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=742267067073565596&target=email' target='_blank' title='Email This'><span class='share-button-link-text'>Email This</span></a><a class='goog-inline-block share-button sb-blog' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=742267067073565596&target=blog' onclick='window.open(this.href, "_blank", "height=270,width=475"); return false;' target='_blank' title='BlogThis!'><span class='share-button-link-text'>BlogThis!</span></a><a class='goog-inline-block share-button sb-twitter' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=742267067073565596&target=twitter' target='_blank' title='Share to Twitter'><span class='share-button-link-text'>Share to Twitter</span></a><a class='goog-inline-block share-button sb-facebook' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=742267067073565596&target=facebook' onclick='window.open(this.href, "_blank", "height=430,width=640"); return false;' target='_blank' title='Share to Facebook'><span class='share-button-link-text'>Share to Facebook</span></a><a class='goog-inline-block share-button sb-pinterest' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=742267067073565596&target=pinterest' target='_blank' title='Share to Pinterest'><span class='share-button-link-text'>Share to Pinterest</span></a>
</div>
</div>
<div class='post-footer-line post-footer-line-2'></div>
<div class='post-footer-line post-footer-line-3'></div>
</div>
</div>
</div>

          </div></div>


          <div class="date-outer">

<h2 class='date-header'><span>March 30, 2023</span></h2>

          <div class="date-posts">

<div class='post-outer'>
<div class='post hentry'>
<a name='4912078560509667939'></a>
<h3 class='post-title entry-title'>
<a href='https://www.redeemerofisrael.org/2023/03/jesus-heals-lame-man-at-pool-of-bethesda.html'>Jesus Heals a Lame Man at the Pool of Bethesda</a>
</h3>
<div class='post-header'>
<div class='post-header-line-1'></div>
</div>
<div class='post-body entry-content' id='post-body-4912078560509667939'>
<p style="text-align: center;"><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/VlnVY5Ty3TQ?controls=0" title="YouTube video player" width="560"></iframe></p><p>In John chapter 5, we learn of the story of Jesus healing a lame man at the Pool of Bethesda. According to some Bible translations, an angel stirred up the waters which allowed whoever entered them first to be miraculously healed. Yet, the earliest copies of the Gospel of John only mention the movement of the water and say nothing about the angel. So, what caused this troubling of the waters, and, more importantly, what can this story teach us about becoming whole through the atonement of Jesus Christ?</p><p>The story begins with Jesus traveling to Jerusalem during one of the Jewish feasts (John 5:1). While John doesn&#8217;t mention which feast it was, some scholars suggest it might have been the Feast of Weeks, or Pentecost (Brown, 206). Before a pilgrim could enter the temple, they had to become ritually clean by immersing in what is known as a mikvah filled with living water. Living water came from a natural source of moving water such as a spring, rainwater, or a stream. If even just a small amount of living water was added to water that was stagnant or not moving, all of it would then be considered &#8220;living,&#8221; and thus suitable for purification.</p><p>With tens of thousands of Jews coming to Jerusalem during such feasts, many ritual bathes or mikvot were constructed around the temple to accommodate the large crowds. The Pool of Bethesda is believed to be one of these ritual washing areas. Bethesda had two large pools surrounded by porches on all four sides, with a fifth porch, as referenced in John 5:2, dividing the two pools. Both pools were massive in size and together were about the dimensions of a standard soccer field. The pools were located at the bottom of a small valley north of the temple. During the rainy season, runoff water would funnel down the valley and collect into the northern pool. Today the northern pool has been mostly covered by centuries of soil and later structures making it almost impossible to visualize.</p><p>The southern pool had large steps and landings that led down to the water level. It was likely on one of these landings where the lame man rested. Visitors today can still see at least some of these steps, which have been exposed by archeologists. The steps are surprisingly tall as one climbs up them, making it understandable why the lame man was unable to easily climb down them.</p><p>The thick wall dividing the two pools, or the fifth porch, has a shaft that goes down to the bottom and connects the two pools. One could climb up and down the shaft because of small footholds that had been carved in the side of the wall, creating a sort of ladder. Climbing down, a person could open recesses in the shaft, allowing the water to drain from the northern pool to the southern pool. This would bring the &#8220;living&#8221; rain water from the north pool in contact with the stagnant water in the southern pool, making it usable for ritual purposes. As Jewish pilgrims came to Jerusalem, they could come to this pool, or one of the many others, and climb down the steps until they arrived at the water level. Once they had been immersed in the water, they were then considered ritually clean to worship at the temple.</p><p>Thus, rather than being the result of angelic power, the moving of the water seems to have been caused by water coming from the northern pool, bubbling up as it came through the drainage tunnel. With this setting in mind, let&#8217;s now dive into the story of the healing of the lame man by Jesus.</p><p>The day was the Sabbath. Many people with physical illnesses had gathered on the steps and large landings, where they waited for the movement of the water. Apparently, they believed that whoever was able to get into the moving waters first would be healed. As Jesus entered Bethesda, he was drawn to a particular man whom Jesus somehow knew had been afflicted for many years. We don&#8217;t know this man&#8217;s age, but for 38 years he had suffered, longing for a miraculous healing that never came.</p><p>Jesus walked up to him and asked, &#8220;Do you want to be made well?&#8221; (John 5:6 NKJV). Instead of answering with a simple yes or no, the man replied that he had no one to help him into the pool when the waters were troubled. In essence, the man focused on what he perceived as the main obstacle that stopped him from being healed. In great power, Jesus simply stated, &#8220;Rise, take up thy bed, and walk&#8221; (John 5:8).&nbsp;</p><p>The man was instantly healed and took up his bed to leave as commanded by the Savior. Yet as he proceeded on his way, he was confronted by Jewish leaders who accused him of breaking the Sabbath. The Law of Moses didn&#8217;t actually prohibit the carrying of a bed on the Sabbath, but later Jewish traditions apparently did. As Jesus did so many times, he seemed to have purposefully healed this man on the Sabbath day, as it provided him an opportunity to teach about the true purpose of the Sabbath. Keeping the Sabbath is not about obeying contrived lists of dos and don&#8217;ts. Rather, the Sabbath should be a day for spiritual and even physical renewal and healing. It should be a day where we focus on reaching out to heal and lift others.</p><p>The occurrence of this miracle during a Jewish feast should also not be overlooked. Around this time, thousands of pilgrims would have been ritually bathing in these pools after a long journey toward the temple. We may ask ourselves, where did this man first go after he was bid to rise and walk. Perhaps it was to the temple, where, for the first time in nearly four decades, he would be able to participate in its sacred rituals (Razafiarivony).&nbsp;</p><p>For those who have struggled for years with heart-wrenching physical or spiritual challenges, for those who feel no one is there to assist or heal them, the words of Jesus to the man at Bethesda can offer powerful comfort and encouragement. As Isaiah so beautifully wrote, &#8220;But they that wait upon the Lord shall renew their strength; they shall mount up with wings as eagles; they shall run, and not be weary; and they shall walk, and not faint.&#8221; (Isaiah 40:31).</p><p>This story teaches that Jesus is the true source of living water. No matter how long we have to endure hardships, we can trust that he will never forsake us. He can pick us out of any crowd and knows precisely what we need most. Whatever&#8217;s keeping us from progressing on our journey towards God&#8217;s presence, Jesus can lift us up and help us on our way. If it&#8217;s the stagnant or corrosive elements of sin that are keeping us down, the healing waters of Christ&#8217;s atonement can make us clean and whole.&nbsp;</p><p>Even death itself can&#8217;t conquer us, seeing that through Christ all will someday rise up, walk, and live forever! &#8220;For as in Adam all die, even so in Christ shall all be made alive&#8221; (1 Corinthians 15:22). In a way, no matter our circumstances, Jesus is bidding each of us to take up our beds and walk&#8212;to walk with him, to walk for him, to walk and follow him. As we act in faith, we&#8217;ll find that we have the power to do whatever he commands, because he has lifted us up and made us whole.</p>
<div style='clear: both;'></div>
</div>
<div class='post-footer'>
<div class='post-footer-line post-footer-line-1'><span class='post-comment-link'>
<a class='comment-link' href='https://www.redeemerofisrael.org/2023/03/jesus-heals-lame-man-at-pool-of-bethesda.html#comment-form' onclick=''>0
comments</a>
</span>
<span class='post-icons'>
<span class='item-action'>
<a href='https://www.blogger.com/email-post.g?blogID=4667816923565672485&postID=4912078560509667939' title='Email Post'>
<img alt="" class="icon-action" height="13" src="//img1.blogblog.com/img/icon18_email.gif" width="18">
</a>
</span>
</span>
<div class='post-share-buttons goog-inline-block'>
<a class='goog-inline-block share-button sb-email' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=4912078560509667939&target=email' target='_blank' title='Email This'><span class='share-button-link-text'>Email This</span></a><a class='goog-inline-block share-button sb-blog' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=4912078560509667939&target=blog' onclick='window.open(this.href, "_blank", "height=270,width=475"); return false;' target='_blank' title='BlogThis!'><span class='share-button-link-text'>BlogThis!</span></a><a class='goog-inline-block share-button sb-twitter' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=4912078560509667939&target=twitter' target='_blank' title='Share to Twitter'><span class='share-button-link-text'>Share to Twitter</span></a><a class='goog-inline-block share-button sb-facebook' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=4912078560509667939&target=facebook' onclick='window.open(this.href, "_blank", "height=430,width=640"); return false;' target='_blank' title='Share to Facebook'><span class='share-button-link-text'>Share to Facebook</span></a><a class='goog-inline-block share-button sb-pinterest' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=4912078560509667939&target=pinterest' target='_blank' title='Share to Pinterest'><span class='share-button-link-text'>Share to Pinterest</span></a>
</div>
</div>
<div class='post-footer-line post-footer-line-2'></div>
<div class='post-footer-line post-footer-line-3'></div>
</div>
</div>
</div>

          </div></div>


          <div class="date-outer">

<h2 class='date-header'><span>February 16, 2023</span></h2>

          <div class="date-posts">

<div class='post-outer'>
<div class='post hentry'>
<a name='8337114021112512863'></a>
<h3 class='post-title entry-title'>
<a href='https://www.redeemerofisrael.org/2023/02/finding-christ-in-altar-of-incense.html'> Finding Christ in the Altar of Incense</a>
</h3>
<div class='post-header'>
<div class='post-header-line-1'></div>
</div>
<div class='post-body entry-content' id='post-body-8337114021112512863'>
<p style="text-align: center;"><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/ZS79wnUUl7A?controls=0" title="YouTube video player" width="560"></iframe></p><p>The golden altar of incense was placed before the veil of the Tabernacle of Moses. Every morning and evening the priest burned incense there, offering prayers on behalf of all Israel. Through the symbolism of this sacred altar, we can learn of the powerful connection between the power of prayer and the Savior&#8217;s suffering and sacrifice.</p><p>The altar of incense, which was located in the Holy Place, shared many characteristics with the altar of sacrifice, situated in the courtyard. Both were made from acacia wood and overlaid with metal (the altar of sacrifice in bronze, the altar of incense in gold). Both were square in shape, had horns on each of their four corners, and had rings and staves for transporting. These similarities suggest there was a connection between these two altars. (Compare Exodus 30:1-10 and Exodus 27:1-8).</p><p>Each morning and evening, at the time of prayer, the priest, who represented all of Israel, would first wash his hands and feet at the bronze laver (Exodus 30:20-21), and then he would offer a lamb as a burnt offering on the altar of sacrifice (Exodus 29:38-41). He would then wash again before entering the Holy Place, taking with him a coal from the altar in the courtyard. Originally, the fire at the altar of sacrifice was lit by God when He first accepted the Tabernacle (Leviticus 9:24), and it had continued burning uninterrupted, because of the maintenance of the priests (Leviticus 6:9, 12, 13). This means that each day the incense was ignited from a coal that was originally lit by the Lord himself.&nbsp;</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqmZolSbPJXSgeCDCLtqPx7X8NbljUeptjNBasMRa8kwAhY36g_WY78vy1wC5RosFH0zRDd01F5ZH3xBx3LuFIaSMjEruIfSGC617DuEZGPYmlHSQdR5X3n_khrKPJFLheZ3cddEEE0jvCePjIHe3-v_Cg-z6CDP68bF59cfGw3NHztOGDZw0h8RxEfQ/s2667/Pillar%20of%20fire.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqmZolSbPJXSgeCDCLtqPx7X8NbljUeptjNBasMRa8kwAhY36g_WY78vy1wC5RosFH0zRDd01F5ZH3xBx3LuFIaSMjEruIfSGC617DuEZGPYmlHSQdR5X3n_khrKPJFLheZ3cddEEE0jvCePjIHe3-v_Cg-z6CDP68bF59cfGw3NHztOGDZw0h8RxEfQ/w640-h360/Pillar%20of%20fire.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Pillar of fire lighting down on the altar of the Tabernacle of Moses</td></tr></tbody></table><p>With the incense burning on the altar in front of the veil, the priest would then offer a prayer with raised hands, requesting blessings and redemption for all of Israel. The rising smoke represented the prayers of the saints ascending to God before the veil. The Psalmist wrote, &#8220;Let my prayer be set forth before thee as incense; and the lifting up of my hands as the evening sacrifice&#8221; (Psalm 141:2; see also&nbsp;Revelation 5:8 and&nbsp;Revelation 8:3).</p><p>The substance burned at the altar was to be made from a combination of spices and incense, including frankincense, one of the gifts later given to the young Jesus by the wise men. These ingredients were to be finely ground down to a powder, which produced a sweet-smelling fragrance when burned at the altar (see&nbsp;Exodus 30:34-36). The grinding down of the incense can be seen as a symbol of the Savior, who was ground down and burned in the fire of affliction, that our prayers might be answered before the throne of God.</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyEjJhE5oVDzHR9WnOcWPi5Y-LW3AcJASGZ7Eo-nl3eRFkaoO-zHTmNOUN9KWUL_5v0nMiKji_nXcRNqIlF9ifykWdlYwbK8K2gk4Rr6ghXXKR4jSXY2-pDryIpCu5EAkjaqhFFaiMbF7E3Eml0aziJRW-8Z3PDdGdHtYC60q4quQ-mquza8G3aFi_hA/s2667/Altar%20of%20Incense.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyEjJhE5oVDzHR9WnOcWPi5Y-LW3AcJASGZ7Eo-nl3eRFkaoO-zHTmNOUN9KWUL_5v0nMiKji_nXcRNqIlF9ifykWdlYwbK8K2gk4Rr6ghXXKR4jSXY2-pDryIpCu5EAkjaqhFFaiMbF7E3Eml0aziJRW-8Z3PDdGdHtYC60q4quQ-mquza8G3aFi_hA/w640-h360/Altar%20of%20Incense.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">A priest praying with raised hands at the altar of incense at the Tabernacle</td></tr></tbody></table><p>As we study these morning and evening rituals enacted by the priests, we can learn several valuable lessons that can help us as we seek to approach the throne of God through prayer. First, just as the priest had to symbolically wash and offer a lamb as part of the daily prayers, we should seek daily repentance as we petition the Lord. Moreover, as we place our faith in the Lamb of God, we become spiritually clean through his atonement. As the writer of Hebrews wrote, &#8220;Let us draw near with a true heart in full assurance of faith, having our hearts sprinkled from an evil conscience, and our bodies washed with pure water&#8221; (Hebrews 10:22).</p><p>With the offering of the lamb on the altar, the priest could then enter the Holy Place, having been washed, clothed, and permitted to proceed to this sacred room. Here before the presence of the Lord, he could offer prayer for all of Israel. The similarities between the altars of sacrifice and incense show a progression of sacredness in the offerings given. In the outer courtyard, the sacrifice of an animal can be seen as a symbol of our sins and iniquities that must be placed on the altar. The death of this innocent animal is a type and shadow of the suffering and death of our Savior. In contrast, the burning of the finely ground incense and spices can represent a sweeter savor and a more sacred offering to the Lord. The pleasant aroma rising towards heaven could symbolize our prayer, service, devotion, and consecrated efforts to build the Kingdom of God. It focuses our attention on praying for others and lifting and serving those in need.&nbsp;</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj08kzLwqiLKHtuyVn6VybgaR6qYjRMaytL-Cz6CJ7i7ztURlC2iueYYbfNMOtQ70Z1nmonVkjayQF1Brp-nQaVhmBpRX7OPf8ZuFy56H61C4jXMg6eKVajy03_t-1l8EnOFIv9jTbF_5Tx5lWKORRnoeNMulesyDcYaCM_6Re9j7ntHlolZ21M4F6nJg/s2667/Holy%20Place.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj08kzLwqiLKHtuyVn6VybgaR6qYjRMaytL-Cz6CJ7i7ztURlC2iueYYbfNMOtQ70Z1nmonVkjayQF1Brp-nQaVhmBpRX7OPf8ZuFy56H61C4jXMg6eKVajy03_t-1l8EnOFIv9jTbF_5Tx5lWKORRnoeNMulesyDcYaCM_6Re9j7ntHlolZ21M4F6nJg/w640-h360/Holy%20Place.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Smoke rising in front of the veil from the altar of incense</td></tr></tbody></table><p>In our own daily prayers, we can follow this pattern by first seeking daily forgiveness of our wrongs as if at the altar of sacrifice. This gives us the chance to have a new start each day. Once washed and cleansed through the blood of the Lamb, we then symbolically approach the throne of God and pray for those around us who might be in need of the Lord&#8217;s comfort or support. After we finish our prayers, we then allow the Savior to work through us, as we serve and bless the lives of others through acts of kindness and love.&nbsp;</p><p>Just before the birth of Christ, the priest Zacharias was chosen to offer the incense and pray on behalf of Israel in Herod&#8217;s Temple. While he prayed an angel appeared on the side of the altar and told him that his wife, Elizabeth, would have a son. The angel then prophesied that this son, John the Baptist, would prepare the way for the coming Messiah. For hundreds of years, priests had offered countless prayers at this altar, petitioning for blessings upon Israel. Now, those prayers had been heard, the Messiah would come! Redemption for Israel was near! This can teach us that answers to prayers don&#8217;t always come when we might hope, but answers will always come in the timing of the Lord!</p><p>We each have the opportunity, like the ancient priests, to offer our prayers before the Lord, morning and evening and throughout each day. As we find our own sacred and holy space, we can symbolically be washed through the blood of Christ, and then enter the holy presence of the Lord to request blessings for ourselves and others. How glorious it is that our Father in Heaven allows us to approach Him in prayer, and that because of the sacrifice of his Son&#8212;the Lamb of God&#8212;we can find the answers, comfort, and blessing that we seek!</p>
<div style='clear: both;'></div>
</div>
<div class='post-footer'>
<div class='post-footer-line post-footer-line-1'><span class='post-comment-link'>
<a class='comment-link' href='https://www.redeemerofisrael.org/2023/02/finding-christ-in-altar-of-incense.html#comment-form' onclick=''>0
comments</a>
</span>
<span class='post-icons'>
<span class='item-action'>
<a href='https://www.blogger.com/email-post.g?blogID=4667816923565672485&postID=8337114021112512863' title='Email Post'>
<img alt="" class="icon-action" height="13" src="//img1.blogblog.com/img/icon18_email.gif" width="18">
</a>
</span>
</span>
<div class='post-share-buttons goog-inline-block'>
<a class='goog-inline-block share-button sb-email' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=8337114021112512863&target=email' target='_blank' title='Email This'><span class='share-button-link-text'>Email This</span></a><a class='goog-inline-block share-button sb-blog' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=8337114021112512863&target=blog' onclick='window.open(this.href, "_blank", "height=270,width=475"); return false;' target='_blank' title='BlogThis!'><span class='share-button-link-text'>BlogThis!</span></a><a class='goog-inline-block share-button sb-twitter' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=8337114021112512863&target=twitter' target='_blank' title='Share to Twitter'><span class='share-button-link-text'>Share to Twitter</span></a><a class='goog-inline-block share-button sb-facebook' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=8337114021112512863&target=facebook' onclick='window.open(this.href, "_blank", "height=430,width=640"); return false;' target='_blank' title='Share to Facebook'><span class='share-button-link-text'>Share to Facebook</span></a><a class='goog-inline-block share-button sb-pinterest' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=8337114021112512863&target=pinterest' target='_blank' title='Share to Pinterest'><span class='share-button-link-text'>Share to Pinterest</span></a>
</div>
</div>
<div class='post-footer-line post-footer-line-2'></div>
<div class='post-footer-line post-footer-line-3'></div>
</div>
</div>
</div>

          </div></div>


          <div class="date-outer">

<h2 class='date-header'><span>February 2, 2023</span></h2>

          <div class="date-posts">

<div class='post-outer'>
<div class='post hentry'>
<a name='3501546863468720173'></a>
<h3 class='post-title entry-title'>
<a href='https://www.redeemerofisrael.org/2023/02/jesus-and-synagogue.html'>Jesus and the Synagogue</a>
</h3>
<div class='post-header'>
<div class='post-header-line-1'></div>
</div>
<div class='post-body entry-content' id='post-body-3501546863468720173'>
<p style="text-align: center;">&nbsp;<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/Nvb3dyY6PDs" title="YouTube video player" width="560"></iframe></p><p>Shortly after Jesus fasted in the wilderness for 40 days, He came to Nazareth, His hometown, and entered the synagogue to declare that He was the promised Messiah (Luke 4:16&#8211;30).</p><p>Understanding synagogues at the time of Jesus can help us better visualize this pivotal moment, when, according to Luke, Jesus began His ministry. Several ancient synagogues dating to the time of Christ have been excavated in Israel, giving us a remarkable view of what it might have been like to worship and hear the Savior&#8217;s words as He taught on this occasion.</p><p>Synagogues were the main civic and religious center of Jewish life. The main worship area was generally rectangular in shape with stone benches around the sides where people could sit. Unlike most religious churches today&#8212;with pews facing one direction towards a pulpit&#8212;these stone perimeter benches allowed for more of a discussion or debate. Pillars within the chamber held up the ceiling, and thus blocked the view of some of the participants. This suggests that the building was designed primarily for hearing instead of seeing the speaker. Both men and women were allowed to attend, though women possibly sat in a separate area from the men and likely had minimal involvement except to listen to the teachings.&nbsp;</p><p>As the townspeople entered the synagogue, the best seats were reserved for the higher-ranking officials (see Matthew 23:6). These were likely on one of the lower benches, or a single bench against the wall. These would have provided more space while separating them from the commoners. In addition, these reserved benches were likely not placed behind any of the pillars, allowing an unobstructed view of the reading and study of the Torah.</p><p>Synagogues were normally quite plain in design. The floors would have been made of packed dirt or plaster. The walls would also have been plastered, though we do find some examples of colorfully painted frescos.&nbsp;</p><p>The Magdala synagogue is one of the best-preserved synagogues from the time of Jesus. While still fairly modest, some of its floors were decked with beautiful mosaic tiles, including in the main worship area around the perimeter of the room and also the room where the torah scrolls may have been stored. The walls had beautiful frescoed panels. Several of the original remains still show the vivid colors of the original paint, and even the pillars themselves were plastered and painted in red.</p><p>In the center of the main room stood an impressive stone-carved bench or podium, depicting one of the earliest examples of the tabernacle or temple menorah. The stone also portrayed other temple-related objects, including the table of showbread, the altar of incense, and the holy of holies with the presence of God. It&#8217;s thought that this stone served as a base for a wooden stand, upon which the torah scroll could be read. Others have suggested that it also could have been used as a bench for sitting, or as a table for offerings brought to the synagogue, such as the offering of the first fruits.</p><p>Some synagogues also had secondary rooms which were likely used for small study groups. At the Magdala Synagogue, this type of room features a large rectangular stone with two carved notches. This stone may have been for holding open a torah scroll as it was studied. Because the stone is low to the ground and surrounded by benches, it would have allowed multiple students to gather around the scroll as they learned to read and study the scriptures. It was also common to have a small storage room off the main room for holding the torah scrolls.&nbsp;</p><p>Each Sabbath, as the townspeople gathered at the synagogue, one person was assigned to read from the torah. An attendant would retrieve a scroll from the torah room or from a portable storage box and place it on the table at the center of the room. The book of scripture and specific passages would already have been likely selected beforehand, so the reader would simply open the scroll to the designated location and begin to recite its words. Once finished, he would return to his bench and sit down to expound on what he had just read. It&#8217;s been suggested that standing while reading showed respect for the sacred text of the scriptures, while sitting signaled that the individual was no longer reading the word of God, but instead giving his own interpretation.</p><p>With this background, let&#8217;s now study the story of Jesus as He taught in the synagogue at his hometown of Nazareth. No doubt, the people there had heard about his profound miracles and were possibly hoping for some type of spectacle! Jesus certainly stirred things up, but probably not in the way they expected. After entering the synagogue, Jesus stepped to the center of the room, was given the scroll of Isaiah, and began to read: &#8220;The Spirit of the Lord is upon me, because he hath anointed me to preach the gospel to the poor; he hath sent me to heal the brokenhearted, to preach deliverance to the captives, and recovering of sight to the blind, to set at liberty them that are bruised, To preach the acceptable year of the Lord.&#8221; (Luke 4:18&#8211;19).</p><p>Jesus then returned the scroll to the attendant and sat down, stating, &#8220;This day is this scripture fulfilled in your ears&#8221; (Luke 4:21). This bold declaration shocked his listeners, and for good reason. Jesus had just declared that He was the promised Messiah! The word often translated as Messiah or Christ in the New Testament comes from a Hebrew word meaning &#8220;anointed.&#8221; While prophets, priests, and kings were all anointed in ancient times&#8212;thus making them all types of a messiah&#8212;this passage from Isaiah was thought to refer to the promised Messiah, who would come to save or redeem Israel.</p><p>Sadly, the people who had watched Jesus grow up in their midst could not see him as anything but the son of Joseph (see Luke 4:22). How could He be more than a common carpenter, like his earthy father! In rage, they took hold of Jesus, thrust him out of their village, and then attempted to kill him by throwing him off a cliff. However, his time had not yet come, and Jesus miraculously escaped through the crowd. (Luke 4:28&#8211;30).</p><p>If only the people of Nazareth had been more patient, they may have seen that each of the prophecies that Jesus read from Isaiah were fulfilled during His earthly ministry. In his sermon on the Mount, Jesus taught the gospel to the poor, saying &#8220;Blessed are the poor in spirit: for theirs is the kingdom of heaven&#8221; (Matthew 5:3). He healed the brokenhearted, not only by blessing and curing the masses, but also as He ministered to the one. On the cross, Jesus proclaimed deliverance to the thief who hung next to him, stating, &#8220;today you will be with Me in Paradise&#8221; (Luke 23:43 NKJV). Lastly, of all the miracles in the Bible, the only person that is claimed to restore sight to the blind was Jesus himself, which he did on several occasions. So there&#8217;s no question that his personal ministry adequately fulfilled Isaiah&#8217;s prophecy.</p><p>Yet, perhaps even more meaningful today, is that Jesus Christ is still fulfilling Isaiah&#8217;s words. In one way or another, we are all spiritually poor or weak. We&#8217;re all blind to important sacred truths. And we&#8217;re all in spiritual captivity or bondage, due to sin. The question we must ask is how do we see the Savior of the world? Do we see him just as a common man, a carpenter, the son of Joseph? Or do we see him as the promised Messiah!</p><p>As we come unto Christ and recognize him as our personal Lord and Savior, Isaiah&#8217;s words will be realized in our own lives on a daily basis. Jesus is the only one who can deliver us from spiritual poverty, captivity, sickness, and death. He truly is the Christ, the Anointed One&#8212;the Messiah foretold by ancient prophets.</p>
<div style='clear: both;'></div>
</div>
<div class='post-footer'>
<div class='post-footer-line post-footer-line-1'><span class='post-comment-link'>
<a class='comment-link' href='https://www.redeemerofisrael.org/2023/02/jesus-and-synagogue.html#comment-form' onclick=''>0
comments</a>
</span>
<span class='post-icons'>
<span class='item-action'>
<a href='https://www.blogger.com/email-post.g?blogID=4667816923565672485&postID=3501546863468720173' title='Email Post'>
<img alt="" class="icon-action" height="13" src="//img1.blogblog.com/img/icon18_email.gif" width="18">
</a>
</span>
</span>
<div class='post-share-buttons goog-inline-block'>
<a class='goog-inline-block share-button sb-email' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=3501546863468720173&target=email' target='_blank' title='Email This'><span class='share-button-link-text'>Email This</span></a><a class='goog-inline-block share-button sb-blog' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=3501546863468720173&target=blog' onclick='window.open(this.href, "_blank", "height=270,width=475"); return false;' target='_blank' title='BlogThis!'><span class='share-button-link-text'>BlogThis!</span></a><a class='goog-inline-block share-button sb-twitter' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=3501546863468720173&target=twitter' target='_blank' title='Share to Twitter'><span class='share-button-link-text'>Share to Twitter</span></a><a class='goog-inline-block share-button sb-facebook' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=3501546863468720173&target=facebook' onclick='window.open(this.href, "_blank", "height=430,width=640"); return false;' target='_blank' title='Share to Facebook'><span class='share-button-link-text'>Share to Facebook</span></a><a class='goog-inline-block share-button sb-pinterest' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=3501546863468720173&target=pinterest' target='_blank' title='Share to Pinterest'><span class='share-button-link-text'>Share to Pinterest</span></a>
</div>
</div>
<div class='post-footer-line post-footer-line-2'></div>
<div class='post-footer-line post-footer-line-3'></div>
</div>
</div>
</div>

          </div></div>


          <div class="date-outer">

<h2 class='date-header'><span>April 28, 2022</span></h2>

          <div class="date-posts">

<div class='post-outer'>
<div class='post hentry'>
<a name='3902833559589154899'></a>
<h3 class='post-title entry-title'>
<a href='https://www.redeemerofisrael.org/2022/04/finding-christ-in-golden-menorah.html'>Finding Christ in the Golden Menorah</a>
</h3>
<div class='post-header'>
<div class='post-header-line-1'></div>
</div>
<div class='post-body entry-content' id='post-body-3902833559589154899'>
<p style="text-align: center;"><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/S9wLTu1ygSo" title="YouTube video player" width="560"></iframe>&nbsp;</p><p>The menorah is one of the most recognized objects of the Jewish faith. It is a sacred lampstand used for worship and remembrance. Within the Tabernacle of Moses the only source of light was the oil-lit menorah. The symbolism of the menorah can teach us about our true source of light, even Jesus Christ, who lights our path as we make our journey back to the presence of God.</p><p>As the priest entered the Tabernacle, the first thing that would likely draw their eye was the beautiful golden menorah. The menorah was to be made of a talent of pure gold, or about 75 pounds or 34 kilos. This means we know the weight of the menorah, but we don&#8217;t know its dimensions. Unlike the recognizable Hanukkah menorah with 9 branches, the Tabernacle menorah had 7 branches. The number seven often represents perfection or completion. When one considers the story of the creation, for example, it was not perfect or complete until the Sabbath day when God rested having finished His work. Likewise, our week is not complete without the Sabbath day.</p><p>The menorah arms were decorated with almond buds, blossoms, and flowers reminiscent of an almond tree, the first tree in Israel to blossom in springtime. This could be symbolic of Christ, who was the first fruits of the resurrection. The rod of Aaron within the ark of the covenant was also flowered with almond blossoms. According to Jewish tradition, the decorated menorah also represented the Tree of Life in the Garden of Eden. Thus, as the priest entered the holy place, he would find several symbols of Eden, the menorah, representing the tree of life and the cherubim on the veil, which guarded the way back to the presence of God. In Solomon&#8217;s temple, the room also had beautiful flowers and palm trees engraved on the walls, again connecting this sacred space with the symbolic journey back into the garden where God dwells.</p><p>The Bible teaches us that these beautiful tree-like details of the menorah were to be hammered into shape. This likely happened first by pouring the molten gold into a mold to get the general form, and then hammering the gold into shape. Through the hammering and beating of the gold, the beauty of the menorah came forth. Likewise, it is by the beating from the whip and the incredible suffering, bruising, and anguish of the Savior, which brought forth the resultant beauty of the atonement of Jesus Christ.</p><p>At the top of each of the seven branches was an oil lamp, which provided the only source of light for the Tabernacle. Only the purest of olive oil was used as fuel for the lamps to light the Holy Place. Olive oil was made by harvesting olives from an olive tree and then crushing the olives with a huge rolling stone. The mash of the olives were then placed into flat sacks and stacked beneath the olive press. A large beam with weights was cinched down, applying an incredible amount of pressure, causing the oil to run. The first oil to emerge was colored a dark red, almost the color of blood. The oil was then allowed to sit, the clean and clear oil rising to the top. Only the first pressing, which was the highest of quality, was used for lighting the temple menorah and anointing the priests. This pure oil would burn clean and clear because it had very few contaminants that would cause smoke. The next pressed oil, which was accomplished by adding more weight to the press, was used for cooking and for healing purposes. The last pressed oil was used for lighting the everyday Israelite home. This means that only the purest of the pressed oil was used to light the house of the Lord.</p><p>Beautiful symbolism that points to the Savior, can be found in the use of olive oil within the Tabernacle. Just before his crucifixion, the Savior prayed in what we often call the Garden of Gethsemane. The word gethsemane in Hebrew actually means an olive press, meaning that Jesus prayed in a garden that had an olive press. When describing this prayer, Luke wrote of the Savior, &#8220;And being in an agony he prayed more earnestly: and his sweat was as it were great drops of blood falling down to the ground&#8221; (Luke 22:44). Similar to the pressed down crushed olives, the Savior was pressed down by the sins of the world, the weight causing him to bleed from every pore. Just as the incredible pressure of the olive press is used to bring forth light, healing and anointing power, so too the suffering of the Savior brought forth the power of the atonement that gives light to those in darkness, healing balm from the sins and sorrows of the world, and anointing power to sustain us on our journey back to God.</p><p>Every morning and evening, these oil lamps were to be cared for to ensure that they were always burning. Aaron, the first high priest, was the first to have this responsibility. Aaron would trim away the blackened, burned portions of the wick and replace the spent oil. This twice daily service to trim, fill, and tend to the menorah coincided with the morning and evening prayers and sacrifices. Later, other priests were assigned to help with this duty. Just as the high priest Aaron tended daily to the oil lamps to keep them lit, we too must allow Christ, the Great High Priest, to tend to us each morning and evening so that we may&nbsp; have His light.&nbsp;</p><p>Just as the menorah was the only source of light for the entire Tabernacle, Jesus Christ teaches us that He is the one true source of our light. &#8220;I am the light of the world: he that followeth me shall not walk in darkness, but shall have the light of life&#8221; (John 8:12). Each of us has the daily opportunity to not walk in darkness by drawing near unto God in prayer every morning and evening and always. This simple yet powerful act can allow the Savior to trim the black-sooted parts of our lives as we experience sin, grief, and pain. He can refill our lamps with the essential oil needed in every aspect of our life. Our path back to God is lit by the Light of Christ, only made possible because of the suffering, death, and resurrection of the Savior.&nbsp;</p><div><div><i>Script written by Heather Ruth Pack and Daniel Smith</i></div><div><i><br /></i></div><div><i>Special thanks to Elder Alex Ducos, Ethan Fullmer, Elder Ryan Sampson, and Brian Olson for their help with creating the 3D model of the Tabernacle.</i></div></div>
<div style='clear: both;'></div>
</div>
<div class='post-footer'>
<div class='post-footer-line post-footer-line-1'><span class='post-comment-link'>
<a class='comment-link' href='https://www.redeemerofisrael.org/2022/04/finding-christ-in-golden-menorah.html#comment-form' onclick=''>0
comments</a>
</span>
<span class='post-icons'>
<span class='item-action'>
<a href='https://www.blogger.com/email-post.g?blogID=4667816923565672485&postID=3902833559589154899' title='Email Post'>
<img alt="" class="icon-action" height="13" src="//img1.blogblog.com/img/icon18_email.gif" width="18">
</a>
</span>
</span>
<div class='post-share-buttons goog-inline-block'>
<a class='goog-inline-block share-button sb-email' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=3902833559589154899&target=email' target='_blank' title='Email This'><span class='share-button-link-text'>Email This</span></a><a class='goog-inline-block share-button sb-blog' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=3902833559589154899&target=blog' onclick='window.open(this.href, "_blank", "height=270,width=475"); return false;' target='_blank' title='BlogThis!'><span class='share-button-link-text'>BlogThis!</span></a><a class='goog-inline-block share-button sb-twitter' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=3902833559589154899&target=twitter' target='_blank' title='Share to Twitter'><span class='share-button-link-text'>Share to Twitter</span></a><a class='goog-inline-block share-button sb-facebook' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=3902833559589154899&target=facebook' onclick='window.open(this.href, "_blank", "height=430,width=640"); return false;' target='_blank' title='Share to Facebook'><span class='share-button-link-text'>Share to Facebook</span></a><a class='goog-inline-block share-button sb-pinterest' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=3902833559589154899&target=pinterest' target='_blank' title='Share to Pinterest'><span class='share-button-link-text'>Share to Pinterest</span></a>
</div>
</div>
<div class='post-footer-line post-footer-line-2'></div>
<div class='post-footer-line post-footer-line-3'></div>
</div>
</div>
</div>

          </div></div>


          <div class="date-outer">

<h2 class='date-header'><span>April 13, 2022</span></h2>

          <div class="date-posts">

<div class='post-outer'>
<div class='post hentry'>
<a name='3666089728096912975'></a>
<h3 class='post-title entry-title'>
<a href='https://www.redeemerofisrael.org/2022/04/finding-christ-in-table-of-showbread.html'>Finding Christ in the Table of Showbread</a>
</h3>
<div class='post-header'>
<div class='post-header-line-1'></div>
</div>
<div class='post-body entry-content' id='post-body-3666089728096912975'>
<p style="text-align: center;"><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/HnIOkumUNTw" title="YouTube video player" width="560"></iframe>&nbsp;</p><p>Within the Tabernacle main structure was the beautiful table of showbread. Every Sabbath the priests would partake of the twelve loaves on this table, representing a communal meal with God. The bread was to be placed before the presence of the Lord and can be a reminder of our own need to partake of the true Bread of Life, even Jesus Christ.</p><p>The table of showbread was made of acacia wood overlaid with gold. Four golden rings were attached to the legs where wooden poles overlaid with gold could be inserted used for transporting. The table also had a golden crown molding and what appeared to be some sort of ledge that kept the objects on the table from sliding off as it was transported (see Exodus 25:25). Two stacks of six loaves, for a total of twelve, were placed on the table, likely representing the twelve tribes of Israel. This bread was called the showbread, bread of the face, or the bread of the presence because it was placed before where the presence of God would dwell. Surprisingly, each loaf was made from approximately 5-6 pounds of finely ground flour (see Leviticus 24:5), about the amount of a standard bag of flour! This would mean that the total weight of all the twelve loaves of bread would be around 60-75 pounds. The table also had a pitcher of wine that was used for the drink offering (Exodus 37:16).&nbsp;</p><p>Before we study the meaning of the table of showbread, it will be helpful to first understand the importance of bread in the Bible. Anciently, bread was a highly significant part of every meal. Because bread was one of the cheaper items that could feed a family, large quantities of bread would be used. For this reason, bread was often called the bread of life, or the daily bread (see Matthew 6:11), because it literally sustained life. The task of making bread lay mostly with women, who would spend many hours each day grinding and sifting the wheat, then making it into small flatbread, and then cooking it over a fire. In addition, to being life-sustaining, the breaking and eating of bread could symbolize becoming at peace with your enemy. Inviting someone into your home to share a meal signified that you trusted them and also that you would protect them while they were under your roof. It was a sign of fellowship and unity. Bread also represented God&#8217;s provision to the people.</p><p>With this in mind, let&#8217;s now return to the meaning of the table of showbread. Though only the priests could enter the Tabernacle proper to partake of the showbread each Sabbath, because the priests represented all of Israel, it was as if all the twelve tribes were partaking of the bread. Included on the table were also two bowls of frankincense that would be burned on the altar of incense each Sabbath, as a &#8220;memorial&#8221; or &#8220;offering made by fire to the Lord&#8221; (Leviticus 24:7). In essence, the Lord partook of His portion of the bread, symbolized by the burning of the frankincense, thus sharing a meal with the priests. After eating the bread, the showbread would be replaced by new loaves of bread which would stay on the table till the next Sabbath, meaning the bread would be week-old bread!</p><p>Though the scriptures do not directly relate the partaking of the showbread with the sacrament or communion, the symbols are too strong not to mention. Each Sabbath Christians around the world partake of broken bread and wine or water, to represent and remember the flesh and blood of Christ. Just as anciently, the priests are the ones who break and bless the bread, but today all followers of the Lord, not just the priests, are able to participate in the meal. Similar to ancient times, the partaking of the broken bread&#8212;a symbol of the broken flesh of Christ&#8212;symbolizes that we can become at peace with God through the sacrifice of the Savior. During His mortal ministry, Jesus taught &#8220;I am the bread of life: he that cometh to me shall never hunger; and he that believeth on me shall never thirst&#8221; (John 6:35). As we enter our sacred places of worship each Sabbath, just like the priests entering the Tabernacle each Sabbath, we become at one with God, or at peace with Him, through the breaking of bread. Through this symbolic meal, we are nourished and strengthened, the bread literally becoming a part of us giving us life. So too the atonement of the Savior carries us from day to day, allowing us ultimately to have eternal life through Jesus Christ.</p><p>Another fascinating connection is that each loaf of showbread was to be made of two-tenths of an epha of flour&#8211;about two quarts or two liters (see Leviticus 24:5). This was the same amount of manna the children of Israel were to collect in preparation for the Sabbath day (see Exodus 16:22). This showbread would thus connect the collected Sabbath manna, with this symbolic meal. During the mortal ministry of Jesus, after he miraculously fed the multitude, the next day the people listening to Jesus asked for manna from heaven. In response, the Savior taught, &#8220;I am the living bread which came down from heaven: if any man eat of this bread, he shall live for ever:&#8221; (John 6:51). Just as ancient Israel had to daily gather manna, we must daily feast upon the Word so that we can be nourished and strengthened. As we prepare for the Sabbath, we too should collect a double portion of this &#8220;living bread&#8221; so that we might be able to come into the presence of the Lord and feast with Him!</p><p>It is noteworthy that Jesus Christ was born in Bethlehem, which in Hebrew means the &#8220;house of bread.&#8221; Just as the showbread was finely ground and placed in the fire to cook, so too our Savior was ground down under the weight of our sins and sorrows and placed in the fiery furnace of affliction for our sakes. Truly it is through His suffering that we receive the true bread of life. Bread that if we will partake of, we will have eternal life!</p><div><div><i>Script written by Heather Ruth Pack and Daniel Smith</i></div><div><i><br /></i></div><div><i>Special thanks to Elder Alex Ducos, Ethan Fullmer, Elder Ryan Sampson, and Brian Olson for their help with creating the 3D model of the Tabernacle.</i></div></div>
<div style='clear: both;'></div>
</div>
<div class='post-footer'>
<div class='post-footer-line post-footer-line-1'><span class='post-comment-link'>
<a class='comment-link' href='https://www.redeemerofisrael.org/2022/04/finding-christ-in-table-of-showbread.html#comment-form' onclick=''>0
comments</a>
</span>
<span class='post-icons'>
<span class='item-action'>
<a href='https://www.blogger.com/email-post.g?blogID=4667816923565672485&postID=3666089728096912975' title='Email Post'>
<img alt="" class="icon-action" height="13" src="//img1.blogblog.com/img/icon18_email.gif" width="18">
</a>
</span>
</span>
<div class='post-share-buttons goog-inline-block'>
<a class='goog-inline-block share-button sb-email' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=3666089728096912975&target=email' target='_blank' title='Email This'><span class='share-button-link-text'>Email This</span></a><a class='goog-inline-block share-button sb-blog' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=3666089728096912975&target=blog' onclick='window.open(this.href, "_blank", "height=270,width=475"); return false;' target='_blank' title='BlogThis!'><span class='share-button-link-text'>BlogThis!</span></a><a class='goog-inline-block share-button sb-twitter' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=3666089728096912975&target=twitter' target='_blank' title='Share to Twitter'><span class='share-button-link-text'>Share to Twitter</span></a><a class='goog-inline-block share-button sb-facebook' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=3666089728096912975&target=facebook' onclick='window.open(this.href, "_blank", "height=430,width=640"); return false;' target='_blank' title='Share to Facebook'><span class='share-button-link-text'>Share to Facebook</span></a><a class='goog-inline-block share-button sb-pinterest' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=3666089728096912975&target=pinterest' target='_blank' title='Share to Pinterest'><span class='share-button-link-text'>Share to Pinterest</span></a>
</div>
</div>
<div class='post-footer-line post-footer-line-2'></div>
<div class='post-footer-line post-footer-line-3'></div>
</div>
</div>
</div>

          </div></div>


          <div class="date-outer">

<h2 class='date-header'><span>March 30, 2022</span></h2>

          <div class="date-posts">

<div class='post-outer'>
<div class='post hentry'>
<a name='7297835070317338893'></a>
<h3 class='post-title entry-title'>
<a href='https://www.redeemerofisrael.org/2022/04/finding-christ-in-bronze-laver.html'>Finding Christ in the Bronze Laver</a>
</h3>
<div class='post-header'>
<div class='post-header-line-1'></div>
</div>
<div class='post-body entry-content' id='post-body-7297835070317338893'>
<p style="text-align: center;"><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/5W0drJ2ClQw" title="YouTube video player" width="560"></iframe></p><p>The bronze laver in the Tabernacle of Moses was the location where ritual washings took place. It was here that priests were washed, clothed, and anointed prior to becoming a priest and where they became ritually clean before serving and representing Israel. These cleansing waters of the laver can teach us that it is only through the Savior that we can become spiritually clean.</p><p>The bronze laver was located in the courtyard of the Tabernacle and was placed between the altar of sacrifice and the door of the sanctuary. Of the six pieces of furniture in the Tabernacle, the laver has the fewest details. The one verse description only records that it had some sort of bronze bowl that held water, and that it had a base or stand that held it off the ground. The size of the laver is not given. In Exodus 38:8 we also learn that the laver was made &#8220;from the mirrors of the women who served at the entrance to the tent of meeting&#8221; (Exodus 38:8 NIV). Sadly, the Bible does not give us any details on what type of service these faithful women gave, but it does show that women not only contributed to the construction of the Tabernacle, but also somehow served there. These bronze mirrors would not be like our modern-day glass mirrors, but instead would be made from a polished piece of bronze that gave a vague reflection of the person. These donated mirrors were then likely hammered into shape, or melted down to create the laver.</p><p>The bronze laver was used only by the priests for ritual washing. Normal Israelites could only come to the altar of sacrifice and thus would not be ritually washed here. Animals sacrificed at the altar were also not washed here, but instead once they were killed were washed and cut into pieces on tables next to the altar.</p><p>Two main types of ritual washings of the priests took place at the laver. The first type of washing occurred prior to a high priest or a priest being able to serve at the Tabernacle or later Temples. This washing, clothing, and anointing ritual was preparatory for them before they could represent the people, and occurred only once in their life. In Exodus 40 it reads, &#8220;And thou shalt bring Aaron and his sons unto the door of the tabernacle of the congregation, and wash them with water. And thou shalt put upon Aaron the holy garments, and anoint him, and sanctify him; that he may minister unto me in the priest's office.&#8221; (Exodus 40:12-13). This consecration of the priests included three important and symbolic acts: washing, clothing, and anointing. These gestures were to demonstrate and teach Israel that the priests were authorized to act on their behalf.</p><p></p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdW2aJ6cNTrvDaZ6TDiTAb-9OyQWzqLOjyUetHTeEogeT-9B4Hk0ubo_4BIIxd0DmatUACS5xCFrSmDZTxhWVG56fkapUVdyGiOJIC0cKkxdyGZLxDIB_JjysNiIaAl-PDCllLEXZrHH7irdnGlH1MoSWAcfv6gdLitAt3ar5YL-WTV89KONeJ0q9rkw/s2048/Anointing%2002.JPG" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1365" data-original-width="2048" height="426" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdW2aJ6cNTrvDaZ6TDiTAb-9OyQWzqLOjyUetHTeEogeT-9B4Hk0ubo_4BIIxd0DmatUACS5xCFrSmDZTxhWVG56fkapUVdyGiOJIC0cKkxdyGZLxDIB_JjysNiIaAl-PDCllLEXZrHH7irdnGlH1MoSWAcfv6gdLitAt3ar5YL-WTV89KONeJ0q9rkw/w640-h426/Anointing%2002.JPG" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Moses anoints Aaron as high priest with a horn of oil</td></tr></tbody></table><p></p><p>The priest would first be washed with water from the laver. The Bible does not give any details on this washing, but it would strictly be a ritual washing, meaning that it was not like washing with soap and water, but instead designed to symbolically show that the priest was now ritually clean to serve.</p><p>Once washed, the priests were then clothed with the holy garments. The bestowing of clothing in ancient times was highly symbolic and demonstrated a significant gift or endowing of power or authority. Similar rituals can be seen today with the wearing of robes during a graduation, or by a judge in a court. These ceremonial robes represent the receiving of power or special knowledge by the person wearing them.</p><p>Next, Moses was to anoint Aaron and his sons with sacred anointing oil and blood from the sacrifice. The oil would likely be stored in the horn of an animal, the horn a symbol of power and strength. The Bible does not give any details on the anointing process with oil, but we are told about the process of anointing with blood, which might give us hints to the full process. [3] Moses would first take the blood of the sacrifice of a ram and place a small amount of the blood on the right ear of the priest, then on his right thumb, and then on his right toe. (Exodus 29:20 and Leviticus 8:23-24).</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_JvyuiW1y9oDQuhQN9iUGdkf5s5kaCKgDwUGXyEl2Z0Btnq3jthNPHcx27DjOCIDGhnjq-g1pgXEH_fz-uV3CSTEzPL6hvC2Anb9pSPy1gZ_nLBPY_jP9K5qpGB4HLpNMJHokjHLu498tbK3iwbzROX7WSamDvQ6HdDWo1WBU9fTKYY039bkvLglO_A/s2048/Moses%20placing%20blood%20on%20ear.JPG" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1365" data-original-width="2048" height="266" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_JvyuiW1y9oDQuhQN9iUGdkf5s5kaCKgDwUGXyEl2Z0Btnq3jthNPHcx27DjOCIDGhnjq-g1pgXEH_fz-uV3CSTEzPL6hvC2Anb9pSPy1gZ_nLBPY_jP9K5qpGB4HLpNMJHokjHLu498tbK3iwbzROX7WSamDvQ6HdDWo1WBU9fTKYY039bkvLglO_A/w400-h266/Moses%20placing%20blood%20on%20ear.JPG" width="400" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Moses places blood on the right ear of Aaron</td></tr></tbody></table><br /><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVozZjicLQo4Iwsb0q13Mb_Lu-E8sSkp45d7XFUAiQ7M5HabEHYbUBxL7_2nKbWY0KkQLxi_VvRaJgZj0WrvnHeMU-ltUkTzj8UxA1e1IJKLR5PNAgz3_YoMUVBOqLJBi-JW4SgHYBuhC47eJngwrxaLr6b-aqEd0tEYXsnk_jKjEvqn9HmzgkTkD1dQ/s2048/Moses%20placing%20blood%20on%20thumb.JPG" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1365" data-original-width="2048" height="266" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVozZjicLQo4Iwsb0q13Mb_Lu-E8sSkp45d7XFUAiQ7M5HabEHYbUBxL7_2nKbWY0KkQLxi_VvRaJgZj0WrvnHeMU-ltUkTzj8UxA1e1IJKLR5PNAgz3_YoMUVBOqLJBi-JW4SgHYBuhC47eJngwrxaLr6b-aqEd0tEYXsnk_jKjEvqn9HmzgkTkD1dQ/w400-h266/Moses%20placing%20blood%20on%20thumb.JPG" width="400" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Blood is placed on the right thumb of Aaron</td></tr></tbody></table><br /><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgy04r4b_FP_FgJW3574FNDhzdn6brqsdyDZ5o4ZgRhHw0ITkiJaWV65_1X-4ckHVNX-UFlKsyvDaE7E5TQkcGzi-oeDaBTqwpM0ufVEuCTMoofwhPlVvhnA9g_ZNRp0fzV5pIshXM3TnWTYU1kVNZ6478crrJI2jl7Ikr3yudJBhZ5oSDdvuWz_T4kQ/s2048/Moses%20placing%20blood%20on%20toe.JPG" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1365" data-original-width="2048" height="266" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgy04r4b_FP_FgJW3574FNDhzdn6brqsdyDZ5o4ZgRhHw0ITkiJaWV65_1X-4ckHVNX-UFlKsyvDaE7E5TQkcGzi-oeDaBTqwpM0ufVEuCTMoofwhPlVvhnA9g_ZNRp0fzV5pIshXM3TnWTYU1kVNZ6478crrJI2jl7Ikr3yudJBhZ5oSDdvuWz_T4kQ/w400-h266/Moses%20placing%20blood%20on%20toe.JPG" width="400" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Blood is dabbed on the right toe of Aaron</td></tr></tbody></table><p>While this ritual will seem quite strange to modern readers, the symbolism behind it is quite powerful. First it is important to remember that the Hebrew word for atonement simply means to cover, or blot out. Thus this act of covering with blood could directly relate to the act of atonement. Second, each of the body parts covered with blood can represent important aspects of service at the Tabernacle or Temple. The right ear can symbolize the need for the priest to listen to the word of the Lord as they serve and represent the people. The right thumb can represent the actions and labors of the priest. The right toe can symbolize the need for the priest to walk in the paths of righteousness. By covering each of these parts of the body with blood, it would hopefully remind the priest that it is only through the shedding of blood that they can be cleansed and thus be worthy to represent the people in the Tabernacle.</p><p></p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJQjf6NkkK4E-5r-G3S1fd8O8IEsvjyOt-7sSLXTu81cJCsFES6kfE4flmC6Z6VCqeOjurCozaz_sKQWVNLDvw6di-xU7grMzER31jvfssG_S_9pgHmTgverafHHSSJvpkRTPZxHgG2zmcCl_izIq08M7orSzohFLixk3FkEphwOMdb7QyPvtS7Ta6ew/s2048/Priest%20washing%20hands%2001.JPG" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1365" data-original-width="2048" height="426" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJQjf6NkkK4E-5r-G3S1fd8O8IEsvjyOt-7sSLXTu81cJCsFES6kfE4flmC6Z6VCqeOjurCozaz_sKQWVNLDvw6di-xU7grMzER31jvfssG_S_9pgHmTgverafHHSSJvpkRTPZxHgG2zmcCl_izIq08M7orSzohFLixk3FkEphwOMdb7QyPvtS7Ta6ew/w640-h426/Priest%20washing%20hands%2001.JPG" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">A priest washing his hands at the bronze laver</td></tr></tbody></table><p></p><p>The second type of ritual washing at the laver took place each time the priest served. Before the priest would offer sacrifice at the altar, he would first come and wash his hands and feet. Again, this was not a washing like we might think with soap and water, but only a ritual washing. Once the priest had offered sacrifice at the altar, he would then wash again before entering the holy place when lighting the menorah, replacing and eating the showbread, or when praying at the altar of incense. Similar to the anointing process, the washing of the hands and feet can be a symbol of the required purity of the priest&#8217;s actions and their walk in the service of the Lord.</p><p>From these two main ritual washings, we can see that the laver was designed to be a constant reminder for the priests that they were to be clean before serving in the house of the Lord. It would be a physical act that would daily remind them of the importance of being spiritually clean. With this in mind, it is quite remarkable that the laver was made from bronze mirrors, an item used to inspect yourself. As the priests used the laver, they would look into the reflective bronze and water, and perhaps be reminded of their need to inspect their spiritual cleanliness on a daily basis.</p><p>These ritual washings at the laver can be reminiscent of baptism and other cleansing rituals that help teach us of the importance of becoming spiritually clean. Similar to the priests, as followers of the Savior, we each should daily inspect our lives and actions. We should ask ourselves if we reflect the countenance or image of Christ in our lives (see Alma 5:14). As we serve in the house of the Lord, however that might look for us, do we come prepared, clean, and clothed in the power of God? And perhaps most important, do we remember that it is only because of the blood of Christ that we can become clean and pure. While we always must seek to reflect the Savior in our lives and actions, it is ultimately only because of his atonement that we can become worthy to enter into his presence.&nbsp;</p><p><i>Script written by Heather Ruth Pack and Daniel Smith</i></p><p><i>Special thanks to Elder Alex Ducos, Ethan Fullmer, Elder Ryan Sampson, and Brian Olson for their help with creating the 3D model of the Tabernacle.</i></p>
<div style='clear: both;'></div>
</div>
<div class='post-footer'>
<div class='post-footer-line post-footer-line-1'><span class='post-comment-link'>
<a class='comment-link' href='https://www.redeemerofisrael.org/2022/04/finding-christ-in-bronze-laver.html#comment-form' onclick=''>0
comments</a>
</span>
<span class='post-icons'>
<span class='item-action'>
<a href='https://www.blogger.com/email-post.g?blogID=4667816923565672485&postID=7297835070317338893' title='Email Post'>
<img alt="" class="icon-action" height="13" src="//img1.blogblog.com/img/icon18_email.gif" width="18">
</a>
</span>
</span>
<div class='post-share-buttons goog-inline-block'>
<a class='goog-inline-block share-button sb-email' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=7297835070317338893&target=email' target='_blank' title='Email This'><span class='share-button-link-text'>Email This</span></a><a class='goog-inline-block share-button sb-blog' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=7297835070317338893&target=blog' onclick='window.open(this.href, "_blank", "height=270,width=475"); return false;' target='_blank' title='BlogThis!'><span class='share-button-link-text'>BlogThis!</span></a><a class='goog-inline-block share-button sb-twitter' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=7297835070317338893&target=twitter' target='_blank' title='Share to Twitter'><span class='share-button-link-text'>Share to Twitter</span></a><a class='goog-inline-block share-button sb-facebook' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=7297835070317338893&target=facebook' onclick='window.open(this.href, "_blank", "height=430,width=640"); return false;' target='_blank' title='Share to Facebook'><span class='share-button-link-text'>Share to Facebook</span></a><a class='goog-inline-block share-button sb-pinterest' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=7297835070317338893&target=pinterest' target='_blank' title='Share to Pinterest'><span class='share-button-link-text'>Share to Pinterest</span></a>
</div>
</div>
<div class='post-footer-line post-footer-line-2'></div>
<div class='post-footer-line post-footer-line-3'></div>
</div>
</div>
</div>

          </div></div>


          <div class="date-outer">

<h2 class='date-header'><span>March 4, 2022</span></h2>

          <div class="date-posts">

<div class='post-outer'>
<div class='post hentry'>
<a name='871885249602642265'></a>
<h3 class='post-title entry-title'>
<a href='https://www.redeemerofisrael.org/2022/03/finding-christ-in-altar-of-sacrifice.html'>Finding Christ in the Altar of Sacrifice</a>
</h3>
<div class='post-header'>
<div class='post-header-line-1'></div>
</div>
<div class='post-body entry-content' id='post-body-871885249602642265'>
<p style="text-align: center;">&nbsp;<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/-c5uWzQfILg" title="YouTube video player" width="560"></iframe>&nbsp;</p><div><div>The <a href="https://youtu.be/luYWCpE_P_U" target="_blank">altar of sacrifice</a> in the Tabernacle of Moses, is one of the more powerful types and shadows of the suffering and death of Jesus Christ. The altar was used by the priests for sacrifices and burnt offerings and was the place where Israel could be reconciled with God. Here Israel learned that the remission of sins could only come through the shedding of blood, ultimately pointing to the death of Christ on the cross.</div><div><br /></div><div>Long before Moses was commanded to build the brazen altar, followers of God built altars where they could pray and come near to the Lord. Prophets such as Adam, Noah, and Abraham all built altars to offer sacrifice. These altars were built of uncut stones, which set them apart from the more permanent, yet portable brazen altar of the Tabernacle.</div><div><br /></div><div>The altar of sacrifice was the largest of the pieces of furniture of the Tabernacle. It was constructed of shitim or better translated as acacia wood overlaid with bronze. The acacia tree is one of the few trees that grows naturally in the deserts where the Israelites wandered. Because the tree must grow with very little water, its wood is quite dense making it resistant to rot or decay. Overlaying the acacia wood with bronze made the altar able to withstand the fires of the many sacrifices. Bronze in scripture is often a symbol of judgment, as is seen in the story of the brazen serpent that was lifted up in the wilderness. The Israelites who trusted in the Lord&#8217;s promise of healing power, and looked to the brazen serpent, were healed from their poisonous bites. Likewise, as we look to the Savior on the cross, who was lifted up on our behalf, we can be healed of our sins and sorrows.</div><div><br /></div><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCsGgzcqx_ukBplhrSpgaQD4oR1Qe3EnTxPC2HCgZPyRb_qbr3a3Nm8ioD7ySweiY9Me_mat0UFEIqwFP--wdQPSbzOjthlzRYwAQ1PpEAxqkjCRm_VWd_mWnVHj87FjAAwvTEEWdJPjgSJLh0THFiVu5Pp6NWxArYITzf0MtDlvcNIlPwezMf7ox5XQ/s2667/Brazen%20serpent.jpg" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCsGgzcqx_ukBplhrSpgaQD4oR1Qe3EnTxPC2HCgZPyRb_qbr3a3Nm8ioD7ySweiY9Me_mat0UFEIqwFP--wdQPSbzOjthlzRYwAQ1PpEAxqkjCRm_VWd_mWnVHj87FjAAwvTEEWdJPjgSJLh0THFiVu5Pp6NWxArYITzf0MtDlvcNIlPwezMf7ox5XQ/w640-h360/Brazen%20serpent.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">The brazen serpent lifted up by Moses</td></tr></tbody></table><div>The altar itself was square in shape, which set it apart from all the other furniture except for the altar of incense which shared many similarities. On the four corners were horns, likewise made of acacia wood overlaid with bronze. In ancient times horns were seen as a symbol of power or strength. The altar horns were also a symbol of refuge, as Israelites who had sinned, could take hold of the horn and be promised safety and refuge until they could have a fair trial (see 1 Kings 1:50). The number four is often a symbol representing the four corners of the earth, perhaps pointing to the infinite sacrifice of Christ, which has power to reach to the four ends of the earth. The altar also had four rings, two each placed on the opposite sides. Two long poles made of acacia wood overlaid with bronze could be inserted into the rings allowing the altar to be carried as the Israelites traveled in the wilderness.</div><div><br /></div><div>In Leviticus the Lord commanded three separate times that the fire of the altar was to be kept burning at all times (<a href="https://www.churchofjesuschrist.org/study/scriptures/ot/lev/6.9?lang=eng&amp;clang=eng#p9" target="_blank">Leviticus 6:9</a>, <a href="https://www.churchofjesuschrist.org/study/scriptures/ot/lev/6.12-13?lang=eng&amp;clang=eng#p12" target="_blank">12-13</a>). This is likely because the Lord himself lit the fire, (<a href="https://www.churchofjesuschrist.org/study/scriptures/ot/lev/9.24?lang=eng&amp;clang=eng#p24" target="_blank">Leviticus 9:24</a>) consuming the first sacrifice offered by Aaron. As followers of Christ we too should always seek to keep the fires of our offering burning. While animal sacrifice was done away with by the death of Christ, we can offer to the Lord sacrifices of thanksgiving (<a href="https://www.churchofjesuschrist.org/study/scriptures/ot/ps/107.22?lang=eng&amp;clang=eng#p22" target="_blank">Psalms 107:22</a>), praise (Hebrews 13:15), and service towards others (<a href="https://www.churchofjesuschrist.org/study/scriptures/nt/rom/12.1?lang=eng&amp;clang=eng#p1" target="_blank">Romans 12:1</a>).&nbsp;</div><div><br /></div><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirbxZw3dIyDKPUXsRO4nfz0HAzYKRcdwlcWIkxdrLse-LnxmzcYKMw6wOYohLQT1rQ0g6zBEocN5MC36Ysv6Q3oB4Q-gpV9FO0GfycfsPuiYWcB805HtO5whC2tZpEFt8Pe55SuQ-Jmt4xYg9erStjCPuYhRcXY6Yn3OXCyVKLDhK6QN3kPzRq3GqMlA/s2667/Pillar%20of%20fire.jpg" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirbxZw3dIyDKPUXsRO4nfz0HAzYKRcdwlcWIkxdrLse-LnxmzcYKMw6wOYohLQT1rQ0g6zBEocN5MC36Ysv6Q3oB4Q-gpV9FO0GfycfsPuiYWcB805HtO5whC2tZpEFt8Pe55SuQ-Jmt4xYg9erStjCPuYhRcXY6Yn3OXCyVKLDhK6QN3kPzRq3GqMlA/w640-h360/Pillar%20of%20fire.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Pillar of fire lighting the altar of sacrifice</td></tr></tbody></table><div>The Bible also describes the bronze tools used for sacrifice, including basins and shovels for removing the ashes, bowls to hold the blood, meat forks used to place the sacrifice on the altar, and firepans used for taking coals from the altar to be used in burning incense.</div><div><br /></div><div>In Leviticus 1-5 the Lord prescribed five different types of sacrifices that were to be offered at the altar, the burnt offering, the peace offering, the meat or grain offering, the sin offering, and the trespass offering. Each of these sacrifices varied in what type of animal or offering could be made and how they were ritually offered. Most of these were sacrifices of animals, but there were also offerings of grain as well. While we won&#8217;t attempt to cover the complexity of these five types of offerings here, there were common elements to most of these sacrifices.</div><div><br /></div><div>First, the Israelite or priest would bring the animal through the gate and have the animal inspected to ensure it was without blemish. Next, the person would then lay their hands on the head of the animal which could be seen as symbolically transferring their sins to the sacrifice. The person then slit the throat of the animal, with the priest collecting the blood in a dish. Notice that for an individual sacrifice, it was the person who killed the animal, not the priest. This would vividly convey to the Israelites that it was their sins that caused the death of the animal and that the consequence of sin is death (<a href="https://www.churchofjesuschrist.org/study/scriptures/nt/rom/6.23?lang=eng&amp;clang=eng#p23" target="_blank">Romans 6:23</a>).</div><div><br /></div><div>The collected blood, depending on the type of sacrifice, was then dabbed on the horns, splashed on the sides, or poured out at the base of the altar. The word atonement, or <i>kaphar</i> in Hebrew, actually means to cover or blot out. Blood represented the life of the animal, and thus by covering parts of the altar with blood, the priest was symbolically showing that atonement had been made because of the shedding of blood.</div><div><br /></div><div>The animal was then cut into pieces, and depending on the type of sacrifice, parts of the meat were burned on the altar and the remainder of the meat was eaten by the priests or the family. Only in the case of the burnt offering was the entire animal completely burned on the altar. The eating of a portion of the sacrifice as part of a meal, is highly significant. Meat was rarely a part of daily meals and was mostly reserved for religious feasts and significant events. Because animals provide wool and hair for clothing, and milk and cheese for food, animals were far more valuable alive than dead!&nbsp;</div><div><br /></div><div>In addition, anciently the breaking of bread and eating a meal together often symbolized friendship between two parties. Enemies did not sign peace treaties like today to show they desired unity, but instead broke bread together. It was in the breaking of bread and sharing a meal that covenants were established and friendships renewed. Thus, it is significant that for most sacrifices at the altar, the partaking of a meal was a central part. God partook of His portion of the offering as it was burned on the altar, and then shared the remainder of the meal with the priests or family of the offeror.</div><div><br /></div><div>Because of our sins, we are all enemies of God. Yet, each Sabbath, the Lord invites us to come to His table, and to partake of a communal meal that demonstrates that He is at peace with us. The tokens of the sacrament or communion, blessed by the priests, teach us that it is only because of Christ&#8217;s sacrifice that we can enjoy the friendship and presence of God.&nbsp;</div><div><br /></div><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqKXFLsGmUtuusiD8cmAbjSA0BRB4z40RiwP2-uw2G29cZGhFhJaIoL6BPp-tF0RwnSAsRrC_eQZIbMQ2B2zNxnOlVPL8-UBao4pFGN2nh7suLRIcoLKLtJ4X3plavqQHu3YjWtra6Z2JlB2m2Q_kb7lTYTbvF9q3rsjXJyg59l1cf_TxUutiSOT7V0A/s2667/Tabernacle%20altar.jpg" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqKXFLsGmUtuusiD8cmAbjSA0BRB4z40RiwP2-uw2G29cZGhFhJaIoL6BPp-tF0RwnSAsRrC_eQZIbMQ2B2zNxnOlVPL8-UBao4pFGN2nh7suLRIcoLKLtJ4X3plavqQHu3YjWtra6Z2JlB2m2Q_kb7lTYTbvF9q3rsjXJyg59l1cf_TxUutiSOT7V0A/w640-h360/Tabernacle%20altar.jpg" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Bronze altar of sacrifice</td></tr></tbody></table><div>The ancient altar of sacrifice taught Israel and all of us that before we can come into the presence of the Lord, we first must be reconciled with God. Death is the requirement for sin, yet God in His infinite mercy provided that another could be killed in our stead, that we might live. Just as Israel symbolically laid their sins on the head of the sacrifice, so too Isaiah taught that &#8220;the LORD has laid on him the iniquity of us all&#8221; (<a href="https://www.churchofjesuschrist.org/study/scriptures/ot/isa/52.6?lang=eng&amp;clang=eng#p6" target="_blank">Isaiah 52:6</a>). Similarly, as these animals were bled out, so too the Savior bled in Gethsemane and on the cross that we might have our sins blotted out or covered over. Because of God&#8217;s mercy, as we come to the altar of the Lord, we can find refuge, protection, and forgiveness because of the atoning blood of Jesus Christ.</div></div><div><br /></div><div><i>(Special thanks to Elder Alex Ducos, Ethan Fullmer, Elder Ryan Sampson, and Brian Olson for their help with creating the 3D model of the Tabernacle.)</i></div>
<div style='clear: both;'></div>
</div>
<div class='post-footer'>
<div class='post-footer-line post-footer-line-1'><span class='post-comment-link'>
<a class='comment-link' href='https://www.redeemerofisrael.org/2022/03/finding-christ-in-altar-of-sacrifice.html#comment-form' onclick=''>0
comments</a>
</span>
<span class='post-icons'>
<span class='item-action'>
<a href='https://www.blogger.com/email-post.g?blogID=4667816923565672485&postID=871885249602642265' title='Email Post'>
<img alt="" class="icon-action" height="13" src="//img1.blogblog.com/img/icon18_email.gif" width="18">
</a>
</span>
</span>
<div class='post-share-buttons goog-inline-block'>
<a class='goog-inline-block share-button sb-email' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=871885249602642265&target=email' target='_blank' title='Email This'><span class='share-button-link-text'>Email This</span></a><a class='goog-inline-block share-button sb-blog' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=871885249602642265&target=blog' onclick='window.open(this.href, "_blank", "height=270,width=475"); return false;' target='_blank' title='BlogThis!'><span class='share-button-link-text'>BlogThis!</span></a><a class='goog-inline-block share-button sb-twitter' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=871885249602642265&target=twitter' target='_blank' title='Share to Twitter'><span class='share-button-link-text'>Share to Twitter</span></a><a class='goog-inline-block share-button sb-facebook' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=871885249602642265&target=facebook' onclick='window.open(this.href, "_blank", "height=430,width=640"); return false;' target='_blank' title='Share to Facebook'><span class='share-button-link-text'>Share to Facebook</span></a><a class='goog-inline-block share-button sb-pinterest' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=871885249602642265&target=pinterest' target='_blank' title='Share to Pinterest'><span class='share-button-link-text'>Share to Pinterest</span></a>
</div>
</div>
<div class='post-footer-line post-footer-line-2'></div>
<div class='post-footer-line post-footer-line-3'></div>
</div>
</div>
</div>

          </div></div>


          <div class="date-outer">

<h2 class='date-header'><span>February 6, 2022</span></h2>

          <div class="date-posts">

<div class='post-outer'>
<div class='post hentry'>
<a name='8765475225235362138'></a>
<h3 class='post-title entry-title'>
<a href='https://www.redeemerofisrael.org/2022/02/finding-christ-in-tabernacle-gate.html'>Finding Christ in the Tabernacle Gate and Courtyard</a>
</h3>
<div class='post-header'>
<div class='post-header-line-1'></div>
</div>
<div class='post-body entry-content' id='post-body-8765475225235362138'>
<p style="text-align: center;"><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/9opTZb54IA8" title="YouTube video player" width="560"></iframe></p><p>The very first thing that Israelite worshipers would see as they came to the beautiful Tabernacle was the large white linen fence of the <a href="https://youtu.be/aq0jhO1KDw4" target="_blank">courtyard and the beautiful and colorful gate</a>. The Tabernacle was the place where Israel learned of the importance of repentance, atonement, and sacrifice and could symbolically reenter the presence of God through the priests. Learning of the gate and courtyard can help us better understand that it is only through the Savior that we can return to the presence of the Lord.</p><p>Before we can understand the gate of the Tabernacle, we first must understand the importance of gates in ancient times. The city gate was a place of protection and strength. Its fortified towers were one of the safest places of any ancient city. The excavated gates at Megiddo and Tel Dan are excellent examples of this with their massive fortified structures and flanking chambers. During an attack on the city, these chambers could be used to protect soldiers from invaders.</p><p>Ancient gates were also a place to perform covenants and contractual agreements. After the death of Sarah, Abraham stood at the city gate to negotiate and purchase the tomb where Sarah would be buried (<a href="https://www.churchofjesuschrist.org/study/scriptures/ot/gen/23.10,%2018?lang=eng&amp;clang=eng#p9" target="_blank">Genesis 23:10</a>, <a href="https://www.churchofjesuschrist.org/study/scriptures/ot/gen/23.18?lang=eng&amp;clang=eng#p17" target="_blank">18</a>). When Ruth was to be married to Boaz, under the levirate law, he likewise did this at the city gate (<a href="https://www.churchofjesuschrist.org/study/scriptures/ot/ruth/4.1?lang=eng&amp;clang=eng#p1" target="_blank">Ruth 4:1</a>, <a href="https://www.churchofjesuschrist.org/study/scriptures/ot/ruth/4.10-11?lang=eng&amp;clang=eng#p9" target="_blank">10-11</a>). Being at the gate, allowed all the city to witness the covenant or contract, becoming witnesses to the agreement.</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEhNdlFvmemRfF0cbOJsP_3icY8QvY9CwCYRI1IlPKida2IOBlFoXJgzczzam9kURflSrM92SdKqWQhuXR7S_ai-7yB9ah_tLhWTOnD55c_jEtgAOL2I-PLup6wuUNiFcTYJtC2bfbduvgyb8sIS8qRmciO3d9VZnAUrbfniovvBcDviPXbZNdoRYwZGQw=s2667" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/a/AVvXsEhNdlFvmemRfF0cbOJsP_3icY8QvY9CwCYRI1IlPKida2IOBlFoXJgzczzam9kURflSrM92SdKqWQhuXR7S_ai-7yB9ah_tLhWTOnD55c_jEtgAOL2I-PLup6wuUNiFcTYJtC2bfbduvgyb8sIS8qRmciO3d9VZnAUrbfniovvBcDviPXbZNdoRYwZGQw=w640-h360" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Reconstruction of Tel Dan judgment seat (left); Tel Dan today (right, photo by&nbsp;Todd Bolen)</td></tr></tbody></table><p>The Law of Moses also prescribed that those who had been accused of sin should be brought to the gate, making it a place of judgment (<a href="https://www.churchofjesuschrist.org/study/scriptures/ot/deut/21.19?lang=eng&amp;clang=eng#p18" target="_blank">Deuteronomy 21:19</a>). In fact, ancient city gates often even included an elevated seat, such as the one discovered at Tel Dan. Here the king or ruler would come and sit in judgment and hear the cases brought forward by his people. Because so many people entered and exited the city gate, it was also an excellent place to market goods and services. With the high amount of traffic, ancient prophets also found it an ideal place to preach to the people. Jeremiah stood at the gates when he called the people to repentance, proclaiming that Jerusalem would be destroyed if they did not repent (<a href="https://www.churchofjesuschrist.org/study/scriptures/ot/jer/7.2?lang=eng&amp;clang=eng#p1" target="_blank">Jeremiah 7:2</a>). Thus, the ancient gate was seen as a place of protection, covenant-making, judgment, and a place where the word of God could be heard.</p><p>Similarly, the Tabernacle gate had many of these same characteristics. As sinners, we all must come to the house of the Lord and seek protection and refuge through the grace of Christ. The Tabernacle and later temples in Jerusalem were also a place of covenant-making, where Israel could promise to obey the Lord. It also is a place of judgment, where Israel was to bring their sins to the Lord, and symbolically have them placed on the altar through the death of an innocent animal. The Tabernacle gate was also a place where Israel could hear the word of the Lord, proclaimed by prophets.</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEgvDnWnJLVzMQqLlv1EeHlxfwr6VyGAY8zOolQkO-QMDZMtP4NtAgHDTEyX05IVIUbz-Y_AVFL50UHzzKVpLi-B8xJLCqbalFtAotj9d-RzcCU-CHNkfL1kdEuk6gQkCOGIg9iFCLnV1ZDNenCVlS0i1iTQQCLXyuOPAy5BqBPT5L0pY4BX5-_YRAPT5Q=s2667" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/a/AVvXsEgvDnWnJLVzMQqLlv1EeHlxfwr6VyGAY8zOolQkO-QMDZMtP4NtAgHDTEyX05IVIUbz-Y_AVFL50UHzzKVpLi-B8xJLCqbalFtAotj9d-RzcCU-CHNkfL1kdEuk6gQkCOGIg9iFCLnV1ZDNenCVlS0i1iTQQCLXyuOPAy5BqBPT5L0pY4BX5-_YRAPT5Q=w640-h360" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">3D model of Tabernacle gate from the entrance</td></tr></tbody></table><p>With this background, let&#8217;s now examine the construction of the Tabernacle gate and courtyard. Unlike ancient cities with their towering gates and walls of protection, the Tabernacle courtyard had only a linen fabric wall that separated the world from the sacred. This of course was largely because Israel needed the Tabernacle to be a portable structure that could move with them as they traveled in the wilderness. This outer fence was made from white fine linen, the same fabric used in the clothing of the priests. John the Revelator wrote that &#8220;the fine linen is the righteousness of saints&#8221; (<a href="https://www.churchofjesuschrist.org/study/scriptures/nt/rev/19.8?lang=eng&amp;clang=eng#p7" target="_blank">Revelation 19:8</a>). In ancient times the color white in fabric was very difficult to produce, having to go through a laborious process of bleaching or fulling. This would make it uncommon to see white fabrics used except for the wealthy and elite. These white fine linen walls would also stand in stark contrast to the thousands of black coarse goat hair tents. The white linen creates beautiful symbolism of a sacred space that is set apart from the contrasting surroundings.</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEhv2p4d7gCPy0cfnMeNICKMnevpTCcrKynRPMkDR_1KZGyYqcDluLfislbHXZZe2jb_n6CWIutM5Ruu62UZvQdOfxQGP1cuuU6sxtm_vW6g7DkoxrgGGesD22GXgtGRo7VM6zYRpN0ziztDAnkWpBES94ZsTbSkTru0XiNZOe-q6cJH3LWOePJGYmvm-g=s2667" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/a/AVvXsEhv2p4d7gCPy0cfnMeNICKMnevpTCcrKynRPMkDR_1KZGyYqcDluLfislbHXZZe2jb_n6CWIutM5Ruu62UZvQdOfxQGP1cuuU6sxtm_vW6g7DkoxrgGGesD22GXgtGRo7VM6zYRpN0ziztDAnkWpBES94ZsTbSkTru0XiNZOe-q6cJH3LWOePJGYmvm-g=w640-h360" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Bronze bases and silver bands for the courtyard posts of the Tabernacle</td></tr></tbody></table><p>This outer linen fence was hung on 60 wooden pillars. Unlike the inner sanctuary walls that rested on a foundation of silver bases, these outer pillars rested on bronze bases. These different metals show the levels of gradation of holiness. The outer courtyard is least sacred so bronze is used for most of the items, including the bases of the pillars. As you progress towards more sacred areas, silver and gold are used more prominently to show the symbolic progression of holiness. This outer linen fence was about 7.5 feet or just over 2 meters tall. Being above eye level would create a visible barrier that separated the profane from the sacred, blocking the view of those on the outside. This would mean that the only way to see inside was to enter through the colorful gate.</p><p>The Tabernacle gate itself was made of blue, purple, and scarlet fabric woven into white linen. The colorful gate was surprisingly wide at about 35 feet or over 10 meters, perhaps symbolically showing how despite the fact that there is only one way to enter God&#8217;s presence, it is wide enough to allow all who desire to enter. The Psalms gives us the requirement for entering by saying: &#8220;Who shall ascend into the hill of the LORD? or who shall stand in his holy place? He that hath clean hands, and a pure heart&#8221; (<a href="https://www.churchofjesuschrist.org/study/scriptures/ot/ps/24.3-4?lang=eng&amp;clang=eng#p2" target="_blank">Psalms 24:3-4</a>).</p><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEjhwGF_-z4VAPGU2IL4ou9Y04s8xlAhmfMzoata-fEg8TFW1LN9671A0RJ7sJ0GdCDBENuKgJ0CwKOh2eZDtkqYB-z_z7auCSKOiw3XSZ8dg2OmxPCbpwIjniLP88D6U-yQkvICH3i64ZkPxjE_FTUhnoMDNWAsksGuSdg63eYEDcMupYC2a92oVLJACg=s2667" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="1500" data-original-width="2667" height="360" src="https://blogger.googleusercontent.com/img/a/AVvXsEjhwGF_-z4VAPGU2IL4ou9Y04s8xlAhmfMzoata-fEg8TFW1LN9671A0RJ7sJ0GdCDBENuKgJ0CwKOh2eZDtkqYB-z_z7auCSKOiw3XSZ8dg2OmxPCbpwIjniLP88D6U-yQkvICH3i64ZkPxjE_FTUhnoMDNWAsksGuSdg63eYEDcMupYC2a92oVLJACg=w640-h360" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">3D model of the Tabernacle gate</td></tr></tbody></table><p>The gate was located on the east side of the courtyard. This meant that as an Israelite entered the courtyard they went in a westward direction. When Adam and Eve partook of the forbidden fruit and were cast out of the presence of the Lord, we are told that they went in an eastward direction. This means that to reenter the garden, they would have to turn around and then go westward, passing the cherubim who guarded the tree of life. Ancient Jews saw the similarities between the Garden of Eden and how the High Priest, who represented all of Israel, reversed the steps of Adam and Eve, bringing Israel back into the presence of the Lord.&nbsp;</p><p>Beautiful symbolism can be found in both the outer fence and gate of the Tabernacle that point us to the Lord Jesus Christ. As we draw closer to the Savior, one of the first things that often will catch our eye is His purity and perfection (symbolized by the white linen fence). In many ways, we may want to turn away because of our own lack of cleanliness, but the Lord beckons us forward, showing us how we can become pure like He is pure. The fine linen used for the outer fence may also remind us of the fine linen strips that were used to wrap the lifeless body of Christ at his burial (<a href="https://www.churchofjesuschrist.org/study/scriptures/nt/mark/15.46?lang=eng&amp;clang=eng#p45" target="_blank">Mark 15:46</a>). The colors of the outer gate could symbolize the perfection and attributes of the Savior. The color blue in ancient times often symbolized heaven, the color purple royalty, and the color red death, blood, mortality and sacrifice. These same colors will be replicated throughout the Tabernacle, in the beautiful garments of the High Priest (himself a type of Christ), and the veils of the Tabernacle.</p><p>While teaching in the Temple at Jerusalem, Jesus taught: &#8220;I am the gate; whoever enters through me will be saved&#8221; (<a href="https://www.biblegateway.com/passage/?search=John%2010%3A9&amp;version=NIV" target="_blank">John 10:9 NIV</a>), teaching us that to return to God, the very first thing we must do is pass through the Savior. It is as if the Savior (represented by the beautiful colors) as the Great High Priest, stands at each of the main areas of division, the gate of the courtyard, the door of the Tabernacle, and the veil going into the Holy of Holies. From the very beginning to the very end of our journey back to God, the Savior stands beckoning us to enter through Him. As we pass from one point to the next on our journey back to God, it is always through Him and because of His infinite sacrifice and resurrection that we can progress back into the presence of the Lord!</p><p>See&nbsp;<a href="https://www.churchofjesuschrist.org/study/scriptures/ot/ex/27.9-19?lang=eng&amp;clang=eng#p8" target="_blank">Exodus 27:9-19</a> and <a href="https://www.churchofjesuschrist.org/study/scriptures/ot/ex/38.9-20?lang=eng&amp;clang=eng#p8" target="_blank">Exodus 38:9-20</a> for the description of the Courtyard and Tabernacle.</p><p><i>(Special thanks to Elder Alex Ducos, Ethan Fullmer, and Brian Olson for their help with creating the 3D model of the Tabernacle, and for&nbsp;Audra Coulson for help with the Tel Dan 3D model.).</i></p><p></p>
<div style='clear: both;'></div>
</div>
<div class='post-footer'>
<div class='post-footer-line post-footer-line-1'><span class='post-comment-link'>
<a class='comment-link' href='https://www.redeemerofisrael.org/2022/02/finding-christ-in-tabernacle-gate.html#comment-form' onclick=''>0
comments</a>
</span>
<span class='post-icons'>
<span class='item-action'>
<a href='https://www.blogger.com/email-post.g?blogID=4667816923565672485&postID=8765475225235362138' title='Email Post'>
<img alt="" class="icon-action" height="13" src="//img1.blogblog.com/img/icon18_email.gif" width="18">
</a>
</span>
</span>
<div class='post-share-buttons goog-inline-block'>
<a class='goog-inline-block share-button sb-email' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=8765475225235362138&target=email' target='_blank' title='Email This'><span class='share-button-link-text'>Email This</span></a><a class='goog-inline-block share-button sb-blog' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=8765475225235362138&target=blog' onclick='window.open(this.href, "_blank", "height=270,width=475"); return false;' target='_blank' title='BlogThis!'><span class='share-button-link-text'>BlogThis!</span></a><a class='goog-inline-block share-button sb-twitter' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=8765475225235362138&target=twitter' target='_blank' title='Share to Twitter'><span class='share-button-link-text'>Share to Twitter</span></a><a class='goog-inline-block share-button sb-facebook' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=8765475225235362138&target=facebook' onclick='window.open(this.href, "_blank", "height=430,width=640"); return false;' target='_blank' title='Share to Facebook'><span class='share-button-link-text'>Share to Facebook</span></a><a class='goog-inline-block share-button sb-pinterest' href='https://www.blogger.com/share-post.g?blogID=4667816923565672485&postID=8765475225235362138&target=pinterest' target='_blank' title='Share to Pinterest'><span class='share-button-link-text'>Share to Pinterest</span></a>
</div>
</div>
<div class='post-footer-line post-footer-line-2'></div>
<div class='post-footer-line post-footer-line-3'></div>
</div>
</div>
</div>

        </div></div>

</div>
<div class='blog-pager' id='blog-pager'>
<span id='blog-pager-older-link'>
<a class='blog-pager-older-link' href='https://www.redeemerofisrael.org/search?updated-max=2022-02-06T09:32:00-07:00&max-results=13' id='Blog1_blog-pager-older-link' title='Older Posts'>Older Posts</a>
</span>
<a class='home-link' href='https://www.redeemerofisrael.org/'>Home</a>
</div>
<div class='clear'></div>
<div class='blog-feeds'>
<div class='feed-links'>
Subscribe to:
<a class='feed-link' href='https://www.redeemerofisrael.org/feeds/posts/default' target='_blank' type='application/atom+xml'>Posts (Atom)</a>
</div>
</div>
</div></div>
</div>
</div>
<div class='column-left-outer'>
<div class='column-left-inner'>
<aside>
</aside>
</div>
</div>
<div class='column-right-outer'>
<div class='column-right-inner'>
<aside>
<div class='sidebar section' id='sidebar-right-1'><div class='widget Subscribe' data-version='1' id='Subscribe1'>
<div style='white-space:nowrap'>
<h2 class='title'>Subscribe To</h2>
<div class='widget-content'>
<div class='subscribe-wrapper subscribe-type-POST'>
<div class='subscribe expanded subscribe-type-POST' id='SW_READER_LIST_Subscribe1POST' style='display:none;'>
<div class='top'>
<span class='inner' onclick='return(_SW_toggleReaderList(event, "Subscribe1POST"));'>
<img class='subscribe-dropdown-arrow' src='https://resources.blogblog.com/img/widgets/arrow_dropdown.gif'/>
<img align='absmiddle' alt='' border='0' class='feed-icon' src='https://resources.blogblog.com/img/icon_feed12.png'/>
Posts
</span>
<div class='feed-reader-links'>
<a class='feed-reader-link' href='https://www.netvibes.com/subscribe.php?url=https%3A%2F%2Fwww.redeemerofisrael.org%2Ffeeds%2Fposts%2Fdefault' target='_blank'>
<img src='https://resources.blogblog.com/img/widgets/subscribe-netvibes.png'/>
</a>
<a class='feed-reader-link' href='https://add.my.yahoo.com/content?url=https%3A%2F%2Fwww.redeemerofisrael.org%2Ffeeds%2Fposts%2Fdefault' target='_blank'>
<img src='https://resources.blogblog.com/img/widgets/subscribe-yahoo.png'/>
</a>
<a class='feed-reader-link' href='https://www.redeemerofisrael.org/feeds/posts/default' target='_blank'>
<img align='absmiddle' class='feed-icon' src='https://resources.blogblog.com/img/icon_feed12.png'/>
                  Atom
                </a>
</div>
</div>
<div class='bottom'></div>
</div>
<div class='subscribe' id='SW_READER_LIST_CLOSED_Subscribe1POST' onclick='return(_SW_toggleReaderList(event, "Subscribe1POST"));'>
<div class='top'>
<span class='inner'>
<img class='subscribe-dropdown-arrow' src='https://resources.blogblog.com/img/widgets/arrow_dropdown.gif'/>
<span onclick='return(_SW_toggleReaderList(event, "Subscribe1POST"));'>
<img align='absmiddle' alt='' border='0' class='feed-icon' src='https://resources.blogblog.com/img/icon_feed12.png'/>
Posts
</span>
</span>
</div>
<div class='bottom'></div>
</div>
</div>
<div class='subscribe-wrapper subscribe-type-COMMENT'>
<div class='subscribe expanded subscribe-type-COMMENT' id='SW_READER_LIST_Subscribe1COMMENT' style='display:none;'>
<div class='top'>
<span class='inner' onclick='return(_SW_toggleReaderList(event, "Subscribe1COMMENT"));'>
<img class='subscribe-dropdown-arrow' src='https://resources.blogblog.com/img/widgets/arrow_dropdown.gif'/>
<img align='absmiddle' alt='' border='0' class='feed-icon' src='https://resources.blogblog.com/img/icon_feed12.png'/>
All Comments
</span>
<div class='feed-reader-links'>
<a class='feed-reader-link' href='https://www.netvibes.com/subscribe.php?url=https%3A%2F%2Fwww.redeemerofisrael.org%2Ffeeds%2Fcomments%2Fdefault' target='_blank'>
<img src='https://resources.blogblog.com/img/widgets/subscribe-netvibes.png'/>
</a>
<a class='feed-reader-link' href='https://add.my.yahoo.com/content?url=https%3A%2F%2Fwww.redeemerofisrael.org%2Ffeeds%2Fcomments%2Fdefault' target='_blank'>
<img src='https://resources.blogblog.com/img/widgets/subscribe-yahoo.png'/>
</a>
<a class='feed-reader-link' href='https://www.redeemerofisrael.org/feeds/comments/default' target='_blank'>
<img align='absmiddle' class='feed-icon' src='https://resources.blogblog.com/img/icon_feed12.png'/>
                  Atom
                </a>
</div>
</div>
<div class='bottom'></div>
</div>
<div class='subscribe' id='SW_READER_LIST_CLOSED_Subscribe1COMMENT' onclick='return(_SW_toggleReaderList(event, "Subscribe1COMMENT"));'>
<div class='top'>
<span class='inner'>
<img class='subscribe-dropdown-arrow' src='https://resources.blogblog.com/img/widgets/arrow_dropdown.gif'/>
<span onclick='return(_SW_toggleReaderList(event, "Subscribe1COMMENT"));'>
<img align='absmiddle' alt='' border='0' class='feed-icon' src='https://resources.blogblog.com/img/icon_feed12.png'/>
All Comments
</span>
</span>
</div>
<div class='bottom'></div>
</div>
</div>
<div style='clear:both'></div>
</div>
</div>
<div class='clear'></div>
</div><div class='widget Image' data-version='1' id='Image2'>
<div class='widget-content'>
<a href="//www.youtube.com/user/messagesofChrist">
<img alt='' height='255' id='Image2_img' src='//3.bp.blogspot.com/-G0at0rCveXQ/USw1Fj3ap7I/AAAAAAAAA6g/BwO13waLgck/s1600/YouTube-Channel-button.jpg' width='149'/>
</a>
<br/>
</div>
<div class='clear'></div>
</div><div class='widget BlogSearch' data-version='1' id='BlogSearch1'>
<h2 class='title'>Search This Blog</h2>
<div class='widget-content'>
<div id='BlogSearch1_form'>
<form action='https://www.redeemerofisrael.org/search' class='gsc-search-box' target='_top'>
<table cellpadding='0' cellspacing='0' class='gsc-search-box'>
<tbody>
<tr>
<td class='gsc-input'>
<input autocomplete='off' class='gsc-input' name='q' size='10' title='search' type='text' value=''/>
</td>
<td class='gsc-search-button'>
<input class='gsc-search-button' title='search' type='submit' value='Search'/>
</td>
</tr>
</tbody>
</table>
</form>
</div>
</div>
<div class='clear'></div>
</div><div class='widget BlogArchive' data-version='1' id='BlogArchive2'>
<h2>Blog Archive</h2>
<div class='widget-content'>
<div id='ArchiveList'>
<div id='BlogArchive2_ArchiveList'>
<select id='BlogArchive2_ArchiveMenu'>
<option value=''>Blog Archive</option>
<option value='https://www.redeemerofisrael.org/2009/01/'>January 2009 (2)</option>
<option value='https://www.redeemerofisrael.org/2009/02/'>February 2009 (4)</option>
<option value='https://www.redeemerofisrael.org/2009/03/'>March 2009 (5)</option>
<option value='https://www.redeemerofisrael.org/2009/04/'>April 2009 (5)</option>
<option value='https://www.redeemerofisrael.org/2009/05/'>May 2009 (2)</option>
<option value='https://www.redeemerofisrael.org/2009/06/'>June 2009 (1)</option>
<option value='https://www.redeemerofisrael.org/2009/10/'>October 2009 (1)</option>
<option value='https://www.redeemerofisrael.org/2009/11/'>November 2009 (3)</option>
<option value='https://www.redeemerofisrael.org/2009/12/'>December 2009 (2)</option>
<option value='https://www.redeemerofisrael.org/2010/01/'>January 2010 (2)</option>
<option value='https://www.redeemerofisrael.org/2010/03/'>March 2010 (2)</option>
<option value='https://www.redeemerofisrael.org/2010/05/'>May 2010 (1)</option>
<option value='https://www.redeemerofisrael.org/2011/01/'>January 2011 (4)</option>
<option value='https://www.redeemerofisrael.org/2011/02/'>February 2011 (1)</option>
<option value='https://www.redeemerofisrael.org/2011/03/'>March 2011 (1)</option>
<option value='https://www.redeemerofisrael.org/2011/04/'>April 2011 (3)</option>
<option value='https://www.redeemerofisrael.org/2011/05/'>May 2011 (1)</option>
<option value='https://www.redeemerofisrael.org/2011/06/'>June 2011 (2)</option>
<option value='https://www.redeemerofisrael.org/2011/07/'>July 2011 (1)</option>
<option value='https://www.redeemerofisrael.org/2011/08/'>August 2011 (1)</option>
<option value='https://www.redeemerofisrael.org/2012/03/'>March 2012 (1)</option>
<option value='https://www.redeemerofisrael.org/2012/04/'>April 2012 (2)</option>
<option value='https://www.redeemerofisrael.org/2012/05/'>May 2012 (1)</option>
<option value='https://www.redeemerofisrael.org/2012/07/'>July 2012 (1)</option>
<option value='https://www.redeemerofisrael.org/2012/08/'>August 2012 (1)</option>
<option value='https://www.redeemerofisrael.org/2012/12/'>December 2012 (3)</option>
<option value='https://www.redeemerofisrael.org/2013/01/'>January 2013 (1)</option>
<option value='https://www.redeemerofisrael.org/2013/03/'>March 2013 (3)</option>
<option value='https://www.redeemerofisrael.org/2013/07/'>July 2013 (1)</option>
<option value='https://www.redeemerofisrael.org/2013/09/'>September 2013 (1)</option>
<option value='https://www.redeemerofisrael.org/2013/11/'>November 2013 (1)</option>
<option value='https://www.redeemerofisrael.org/2013/12/'>December 2013 (2)</option>
<option value='https://www.redeemerofisrael.org/2014/01/'>January 2014 (6)</option>
<option value='https://www.redeemerofisrael.org/2014/02/'>February 2014 (4)</option>
<option value='https://www.redeemerofisrael.org/2014/03/'>March 2014 (1)</option>
<option value='https://www.redeemerofisrael.org/2014/04/'>April 2014 (4)</option>
<option value='https://www.redeemerofisrael.org/2014/05/'>May 2014 (1)</option>
<option value='https://www.redeemerofisrael.org/2014/07/'>July 2014 (1)</option>
<option value='https://www.redeemerofisrael.org/2014/08/'>August 2014 (1)</option>
<option value='https://www.redeemerofisrael.org/2014/09/'>September 2014 (1)</option>
<option value='https://www.redeemerofisrael.org/2014/10/'>October 2014 (1)</option>
<option value='https://www.redeemerofisrael.org/2014/12/'>December 2014 (5)</option>
<option value='https://www.redeemerofisrael.org/2015/01/'>January 2015 (1)</option>
<option value='https://www.redeemerofisrael.org/2015/02/'>February 2015 (1)</option>
<option value='https://www.redeemerofisrael.org/2015/04/'>April 2015 (1)</option>
<option value='https://www.redeemerofisrael.org/2015/05/'>May 2015 (2)</option>
<option value='https://www.redeemerofisrael.org/2015/06/'>June 2015 (1)</option>
<option value='https://www.redeemerofisrael.org/2015/07/'>July 2015 (2)</option>
<option value='https://www.redeemerofisrael.org/2015/08/'>August 2015 (2)</option>
<option value='https://www.redeemerofisrael.org/2015/09/'>September 2015 (1)</option>
<option value='https://www.redeemerofisrael.org/2015/11/'>November 2015 (2)</option>
<option value='https://www.redeemerofisrael.org/2015/12/'>December 2015 (4)</option>
<option value='https://www.redeemerofisrael.org/2016/01/'>January 2016 (2)</option>
<option value='https://www.redeemerofisrael.org/2016/02/'>February 2016 (2)</option>
<option value='https://www.redeemerofisrael.org/2016/03/'>March 2016 (4)</option>
<option value='https://www.redeemerofisrael.org/2016/07/'>July 2016 (1)</option>
<option value='https://www.redeemerofisrael.org/2016/08/'>August 2016 (2)</option>
<option value='https://www.redeemerofisrael.org/2016/09/'>September 2016 (1)</option>
<option value='https://www.redeemerofisrael.org/2016/11/'>November 2016 (1)</option>
<option value='https://www.redeemerofisrael.org/2017/02/'>February 2017 (1)</option>
<option value='https://www.redeemerofisrael.org/2017/04/'>April 2017 (6)</option>
<option value='https://www.redeemerofisrael.org/2017/05/'>May 2017 (1)</option>
<option value='https://www.redeemerofisrael.org/2018/03/'>March 2018 (2)</option>
<option value='https://www.redeemerofisrael.org/2018/04/'>April 2018 (1)</option>
<option value='https://www.redeemerofisrael.org/2018/05/'>May 2018 (1)</option>
<option value='https://www.redeemerofisrael.org/2018/07/'>July 2018 (1)</option>
<option value='https://www.redeemerofisrael.org/2018/09/'>September 2018 (1)</option>
<option value='https://www.redeemerofisrael.org/2018/12/'>December 2018 (1)</option>
<option value='https://www.redeemerofisrael.org/2019/01/'>January 2019 (2)</option>
<option value='https://www.redeemerofisrael.org/2019/02/'>February 2019 (4)</option>
<option value='https://www.redeemerofisrael.org/2019/03/'>March 2019 (3)</option>
<option value='https://www.redeemerofisrael.org/2019/04/'>April 2019 (1)</option>
<option value='https://www.redeemerofisrael.org/2019/05/'>May 2019 (1)</option>
<option value='https://www.redeemerofisrael.org/2019/06/'>June 2019 (1)</option>
<option value='https://www.redeemerofisrael.org/2019/09/'>September 2019 (1)</option>
<option value='https://www.redeemerofisrael.org/2019/10/'>October 2019 (2)</option>
<option value='https://www.redeemerofisrael.org/2019/12/'>December 2019 (2)</option>
<option value='https://www.redeemerofisrael.org/2020/02/'>February 2020 (1)</option>
<option value='https://www.redeemerofisrael.org/2020/03/'>March 2020 (1)</option>
<option value='https://www.redeemerofisrael.org/2020/04/'>April 2020 (4)</option>
<option value='https://www.redeemerofisrael.org/2020/05/'>May 2020 (2)</option>
<option value='https://www.redeemerofisrael.org/2020/06/'>June 2020 (1)</option>
<option value='https://www.redeemerofisrael.org/2020/07/'>July 2020 (2)</option>
<option value='https://www.redeemerofisrael.org/2020/08/'>August 2020 (1)</option>
<option value='https://www.redeemerofisrael.org/2020/09/'>September 2020 (3)</option>
<option value='https://www.redeemerofisrael.org/2020/10/'>October 2020 (1)</option>
<option value='https://www.redeemerofisrael.org/2020/11/'>November 2020 (3)</option>
<option value='https://www.redeemerofisrael.org/2020/12/'>December 2020 (2)</option>
<option value='https://www.redeemerofisrael.org/2021/01/'>January 2021 (1)</option>
<option value='https://www.redeemerofisrael.org/2021/02/'>February 2021 (1)</option>
<option value='https://www.redeemerofisrael.org/2021/03/'>March 2021 (1)</option>
<option value='https://www.redeemerofisrael.org/2021/04/'>April 2021 (1)</option>
<option value='https://www.redeemerofisrael.org/2021/12/'>December 2021 (1)</option>
<option value='https://www.redeemerofisrael.org/2022/01/'>January 2022 (2)</option>
<option value='https://www.redeemerofisrael.org/2022/02/'>February 2022 (1)</option>
<option value='https://www.redeemerofisrael.org/2022/03/'>March 2022 (2)</option>
<option value='https://www.redeemerofisrael.org/2022/04/'>April 2022 (2)</option>
<option value='https://www.redeemerofisrael.org/2023/02/'>February 2023 (2)</option>
<option value='https://www.redeemerofisrael.org/2023/03/'>March 2023 (1)</option>
<option value='https://www.redeemerofisrael.org/2023/05/'>May 2023 (1)</option>
<option value='https://www.redeemerofisrael.org/2023/11/'>November 2023 (1)</option>
</select>
</div>
</div>
<div class='clear'></div>
</div>
</div><div class='widget Label' data-version='1' id='Label1'>
<h2>Labels by Frequency</h2>
<div class='widget-content list-label-widget-content'>
<ul>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Jesus%20Christ'>Jesus Christ</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Holy%20Week'>Holy Week</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Old%20Testament'>Old Testament</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Law%20of%20Moses'>Law of Moses</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Christmas'>Christmas</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/High%20Priest'>High Priest</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Replicas'>Replicas</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Temples'>Temples</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Women'>Women</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Tabernacle%20of%20Moses'>Tabernacle of Moses</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Atonement'>Atonement</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Sacrifices'>Sacrifices</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Last%20Supper'>Last Supper</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Christlike%20Attributes'>Christlike Attributes</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Passover'>Passover</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Resurrection'>Resurrection</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Triclinium'>Triclinium</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Sacrament'>Sacrament</a>
</li>
<li>
<a dir='ltr' href='https://www.redeemerofisrael.org/search/label/Museum'>Museum</a>
</li>
</ul>
<div class='clear'></div>
</div>
</div>
</div>
</aside>
</div>
</div>
</div>
<div style='clear: both'></div>
<!-- columns -->
</div>
<!-- main -->
</div>
</div>
<div class='main-cap-bottom cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
<footer>
<div class='footer-outer'>
<div class='footer-cap-top cap-top'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
<div class='fauxborder-left footer-fauxborder-left'>
<div class='fauxborder-right footer-fauxborder-right'></div>
<div class='region-inner footer-inner'>
<div class='foot no-items section' id='footer-1'></div>
<table border='0' cellpadding='0' cellspacing='0' class='section-columns columns-2'>
<tbody>
<tr>
<td class='first columns-cell'>
<div class='foot no-items section' id='footer-2-1'></div>
</td>
<td class='columns-cell'>
<div class='foot no-items section' id='footer-2-2'></div>
</td>
</tr>
</tbody>
</table>
<!-- outside of the include in order to lock Attribution widget -->
<div class='foot section' id='footer-3'><div class='widget Attribution' data-version='1' id='Attribution1'>
<div class='widget-content' style='text-align: center;'>
&#169; 2020 Daniel Smith. Powered by <a href='https://www.blogger.com' target='_blank'>Blogger</a>.
</div>
<div class='clear'></div>
</div></div>
</div>
</div>
<div class='footer-cap-bottom cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
</footer>
<!-- content -->
</div>
</div>
<div class='content-cap-bottom cap-bottom'>
<div class='cap-left'></div>
<div class='cap-right'></div>
</div>
</div>
</div>
<script type='text/javascript'>
    window.setTimeout(function() {
        document.body.className = document.body.className.replace('loading', '');
      }, 10);
  </script>

<script type="text/javascript" src="https://www.blogger.com/static/v1/widgets/1966103537-widgets.js"></script>
<script type='text/javascript'>
window['__wavt'] = 'AOuZoY6SLOrsp1yGitJzOC3ECGGH2Y-GHg:1700025967511';_WidgetManager._Init('//www.blogger.com/rearrange?blogID\x3d4667816923565672485','//www.redeemerofisrael.org/','4667816923565672485');
_WidgetManager._SetDataContext([{'name': 'blog', 'data': {'blogId': '4667816923565672485', 'title': 'Redeemer of Israel', 'url': 'https://www.redeemerofisrael.org/', 'canonicalUrl': 'http://www.redeemerofisrael.org/', 'homepageUrl': 'https://www.redeemerofisrael.org/', 'searchUrl': 'https://www.redeemerofisrael.org/search', 'canonicalHomepageUrl': 'http://www.redeemerofisrael.org/', 'blogspotFaviconUrl': 'https://www.redeemerofisrael.org/favicon.ico', 'bloggerUrl': 'https://www.blogger.com', 'hasCustomDomain': true, 'httpsEnabled': true, 'enabledCommentProfileImages': true, 'gPlusViewType': 'FILTERED_POSTMOD', 'adultContent': false, 'analyticsAccountNumber': '', 'encoding': 'UTF-8', 'locale': 'en', 'localeUnderscoreDelimited': 'en', 'languageDirection': 'ltr', 'isPrivate': false, 'isMobile': false, 'isMobileRequest': false, 'mobileClass': '', 'isPrivateBlog': false, 'isDynamicViewsAvailable': true, 'feedLinks': '\x3clink rel\x3d\x22alternate\x22 type\x3d\x22application/atom+xml\x22 title\x3d\x22Redeemer of Israel - Atom\x22 href\x3d\x22https://www.redeemerofisrael.org/feeds/posts/default\x22 /\x3e\n\x3clink rel\x3d\x22alternate\x22 type\x3d\x22application/rss+xml\x22 title\x3d\x22Redeemer of Israel - RSS\x22 href\x3d\x22https://www.redeemerofisrael.org/feeds/posts/default?alt\x3drss\x22 /\x3e\n\x3clink rel\x3d\x22service.post\x22 type\x3d\x22application/atom+xml\x22 title\x3d\x22Redeemer of Israel - Atom\x22 href\x3d\x22https://www.blogger.com/feeds/4667816923565672485/posts/default\x22 /\x3e\n', 'meTag': '\x3clink rel\x3d\x22me\x22 href\x3d\x22https://www.blogger.com/profile/15148760171162762788\x22 /\x3e\n', 'adsenseHostId': 'ca-host-pub-1556223355139109', 'adsenseHasAds': false, 'adsenseAutoAds': false, 'boqCommentIframeForm': true, 'loginRedirectParam': '', 'view': '', 'dynamicViewsCommentsSrc': '//www.blogblog.com/dynamicviews/4224c15c4e7c9321/js/comments.js', 'dynamicViewsScriptSrc': '//www.blogblog.com/dynamicviews/f2ce4ca2a82a1b0c', 'plusOneApiSrc': 'https://apis.google.com/js/platform.js', 'disableGComments': true, 'interstitialAccepted': false, 'sharing': {'platforms': [{'name': 'Get link', 'key': 'link', 'shareMessage': 'Get link', 'target': ''}, {'name': 'Facebook', 'key': 'facebook', 'shareMessage': 'Share to Facebook', 'target': 'facebook'}, {'name': 'BlogThis!', 'key': 'blogThis', 'shareMessage': 'BlogThis!', 'target': 'blog'}, {'name': 'Twitter', 'key': 'twitter', 'shareMessage': 'Share to Twitter', 'target': 'twitter'}, {'name': 'Pinterest', 'key': 'pinterest', 'shareMessage': 'Share to Pinterest', 'target': 'pinterest'}, {'name': 'Email', 'key': 'email', 'shareMessage': 'Email', 'target': 'email'}], 'disableGooglePlus': true, 'googlePlusShareButtonWidth': 0, 'googlePlusBootstrap': '\x3cscript type\x3d\x22text/javascript\x22\x3ewindow.___gcfg \x3d {\x27lang\x27: \x27en\x27};\x3c/script\x3e'}, 'hasCustomJumpLinkMessage': false, 'jumpLinkMessage': 'Read more', 'pageType': 'index', 'pageName': '', 'pageTitle': 'Redeemer of Israel'}}, {'name': 'features', 'data': {}}, {'name': 'messages', 'data': {'edit': 'Edit', 'linkCopiedToClipboard': 'Link copied to clipboard!', 'ok': 'Ok', 'postLink': 'Post Link'}}, {'name': 'template', 'data': {'name': 'custom', 'localizedName': 'Custom', 'isResponsive': false, 'isAlternateRendering': false, 'isCustom': true}}, {'name': 'view', 'data': {'classic': {'name': 'classic', 'url': '?view\x3dclassic'}, 'flipcard': {'name': 'flipcard', 'url': '?view\x3dflipcard'}, 'magazine': {'name': 'magazine', 'url': '?view\x3dmagazine'}, 'mosaic': {'name': 'mosaic', 'url': '?view\x3dmosaic'}, 'sidebar': {'name': 'sidebar', 'url': '?view\x3dsidebar'}, 'snapshot': {'name': 'snapshot', 'url': '?view\x3dsnapshot'}, 'timeslide': {'name': 'timeslide', 'url': '?view\x3dtimeslide'}, 'isMobile': false, 'title': 'Redeemer of Israel', 'description': '', 'url': 'https://www.redeemerofisrael.org/', 'type': 'feed', 'isSingleItem': false, 'isMultipleItems': true, 'isError': false, 'isPage': false, 'isPost': false, 'isHomepage': true, 'isArchive': false, 'isLabelSearch': false}}]);
_WidgetManager._RegisterWidget('_NavbarView', new _WidgetInfo('Navbar1', 'navbar', document.getElementById('Navbar1'), {}, 'displayModeFull'));
_WidgetManager._RegisterWidget('_HeaderView', new _WidgetInfo('Header1', 'header', document.getElementById('Header1'), {}, 'displayModeFull'));
_WidgetManager._RegisterWidget('_PageListView', new _WidgetInfo('PageList1', 'crosscol', document.getElementById('PageList1'), {'title': 'Pages', 'links': [{'isCurrentPage': true, 'href': 'https://www.redeemerofisrael.org/', 'title': 'Home'}, {'isCurrentPage': false, 'href': 'https://www.redeemerofisrael.org/p/holy-week.html', 'id': '3543842903603747224', 'title': 'Holy Week'}, {'isCurrentPage': false, 'href': 'https://www.redeemerofisrael.org/p/passover.html', 'id': '3246544022961846801', 'title': 'Passover'}, {'isCurrentPage': false, 'href': 'https://www.redeemerofisrael.org/p/christmas.html', 'id': '3690315866070986191', 'title': 'Christmas'}, {'isCurrentPage': false, 'href': 'https://www.redeemerofisrael.org/p/blog-topics.html', 'id': '7171833425063885276', 'title': 'Blog Topics'}, {'isCurrentPage': false, 'href': 'https://www.redeemerofisrael.org/p/visual-aids.html', 'id': '8252979906330255368', 'title': 'Visual Aids'}, {'isCurrentPage': false, 'href': 'https://www.redeemerofisrael.org/p/about-me.html', 'id': '4689971554714094885', 'title': 'About Me'}, {'isCurrentPage': false, 'href': 'https://www.redeemerofisrael.org/p/email-signup.html', 'id': '8915291657705972090', 'title': 'Email Signup'}], 'mobile': false, 'showPlaceholder': false, 'hasCurrentPage': true}, 'displayModeFull'));
_WidgetManager._RegisterWidget('_BlogView', new _WidgetInfo('Blog1', 'main', document.getElementById('Blog1'), {'cmtInteractionsEnabled': false, 'lightboxEnabled': true, 'lightboxModuleUrl': 'https://www.blogger.com/static/v1/jsbin/1601036468-lbx.js', 'lightboxCssUrl': 'https://www.blogger.com/static/v1/v-css/3268905543-lightbox_bundle.css'}, 'displayModeFull'));
_WidgetManager._RegisterWidget('_SubscribeView', new _WidgetInfo('Subscribe1', 'sidebar-right-1', document.getElementById('Subscribe1'), {}, 'displayModeFull'));
_WidgetManager._RegisterWidget('_ImageView', new _WidgetInfo('Image2', 'sidebar-right-1', document.getElementById('Image2'), {'resize': false}, 'displayModeFull'));
_WidgetManager._RegisterWidget('_BlogSearchView', new _WidgetInfo('BlogSearch1', 'sidebar-right-1', document.getElementById('BlogSearch1'), {}, 'displayModeFull'));
_WidgetManager._RegisterWidget('_BlogArchiveView', new _WidgetInfo('BlogArchive2', 'sidebar-right-1', document.getElementById('BlogArchive2'), {'languageDirection': 'ltr', 'loadingMessage': 'Loading\x26hellip;'}, 'displayModeFull'));
_WidgetManager._RegisterWidget('_LabelView', new _WidgetInfo('Label1', 'sidebar-right-1', document.getElementById('Label1'), {}, 'displayModeFull'));
_WidgetManager._RegisterWidget('_AttributionView', new _WidgetInfo('Attribution1', 'footer-3', document.getElementById('Attribution1'), {}, 'displayModeFull'));
</script>
</body>
</html>


"""


def test_load_redeemer() -> None:
    """It returns a valid Document for redeemer of israel."""
    url = "https://www.redeemerofisrael.org"
    result = load_redeemer.load_redeemer(url, html)
    assert len(result.page_content) > 0
    assert result.metadata["url"] == url
    assert result.metadata["title"] == '"Finding Christ in the Ark of the Covenant"'
    assert result.page_content.startswith("[See this page")
