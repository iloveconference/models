"""Test cases for fair module."""
# flake8: noqa

from models.load_fairs import load_fairs


html = """
<!DOCTYPE html>
<html lang="en-US">
<head >
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />
<link rel="alternate" hreflang="en" href="https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29" />
<link rel="alternate" hreflang="x-default" href="https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29" />

	<!-- This site is optimized with the Yoast SEO Premium plugin v21.5 (Yoast SEO v21.5) - https://yoast.com/wordpress/plugins/seo/ -->
	<title>The CES Letter Rebuttal - Part 29 - FAIR</title>
	<link rel="canonical" href="https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="The CES Letter Rebuttal -- Part 29" />
	<meta property="og:description" content="Part 29: CES Letter Prophet Questions [Section C] by Sarah Allen &nbsp; Today, we’re going to talk about one of my favorite weird/controversial topics of Church history, Blood Atonement and the way it was so badly misconstrued. You can see a highly biased approach to the topic here for an example of what I’m talking [&hellip;]" />
	<meta property="og:url" content="https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29" />
	<meta property="og:site_name" content="FAIR" />
	<meta property="article:published_time" content="2021-11-26T19:57:33+00:00" />
	<meta property="article:modified_time" content="2021-11-28T19:30:18+00:00" />
	<meta property="og:image" content="https://ci6.googleusercontent.com/proxy/Mbq6sHeBf0Gv9-j8ncMb5qQsswLfb9RfWICZo8FjyWUsF6PcxzlK6AInZrcOz7MOTAXan___-tG31EbsY3LK66zLGc8EKJ3vr45SueVkkv92lASa79Uir8ks0RTA43kT-g4=s0-d-e1-ft#https://www.fairlatterdaysaints.org/wp-content/uploads/2021/08/me-1-150x150.png" />
	<meta name="author" content="Jeff Markham" />
	<meta name="twitter:label1" content="Written by" />
	<meta name="twitter:data1" content="Jeff Markham" />
	<meta name="twitter:label2" content="Est. reading time" />
	<meta name="twitter:data2" content="27 minutes" />
	<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"Article","@id":"https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29#article","isPartOf":{"@id":"https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29"},"author":{"name":"Jeff Markham","@id":"https://www.fairlatterdaysaints.org/#/schema/person/d54f6236bf0b83573dd0d615df471842"},"headline":"The CES Letter Rebuttal &#8212; Part 29","datePublished":"2021-11-26T19:57:33+00:00","dateModified":"2021-11-28T19:30:18+00:00","mainEntityOfPage":{"@id":"https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29"},"wordCount":6404,"commentCount":0,"publisher":{"@id":"https://www.fairlatterdaysaints.org/#organization"},"image":{"@id":"https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29#primaryimage"},"thumbnailUrl":"https://ci6.googleusercontent.com/proxy/Mbq6sHeBf0Gv9-j8ncMb5qQsswLfb9RfWICZo8FjyWUsF6PcxzlK6AInZrcOz7MOTAXan___-tG31EbsY3LK66zLGc8EKJ3vr45SueVkkv92lASa79Uir8ks0RTA43kT-g4=s0-d-e1-ft#https://www.fairlatterdaysaints.org/wp-content/uploads/2021/08/me-1-150x150.png","articleSection":["Anti-Mormon critics","Apologetics","CES Letter","Faith Crisis","LDS History"],"inLanguage":"en-US","potentialAction":[{"@type":"CommentAction","name":"Comment","target":["https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29#respond"]}]},{"@type":"WebPage","@id":"https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29","url":"https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29","name":"The CES Letter Rebuttal - Part 29 - FAIR","isPartOf":{"@id":"https://www.fairlatterdaysaints.org/#website"},"primaryImageOfPage":{"@id":"https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29#primaryimage"},"image":{"@id":"https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29#primaryimage"},"thumbnailUrl":"https://ci6.googleusercontent.com/proxy/Mbq6sHeBf0Gv9-j8ncMb5qQsswLfb9RfWICZo8FjyWUsF6PcxzlK6AInZrcOz7MOTAXan___-tG31EbsY3LK66zLGc8EKJ3vr45SueVkkv92lASa79Uir8ks0RTA43kT-g4=s0-d-e1-ft#https://www.fairlatterdaysaints.org/wp-content/uploads/2021/08/me-1-150x150.png","datePublished":"2021-11-26T19:57:33+00:00","dateModified":"2021-11-28T19:30:18+00:00","breadcrumb":{"@id":"https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29"]}]},{"@type":"ImageObject","inLanguage":"en-US","@id":"https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29#primaryimage","url":"https://ci6.googleusercontent.com/proxy/Mbq6sHeBf0Gv9-j8ncMb5qQsswLfb9RfWICZo8FjyWUsF6PcxzlK6AInZrcOz7MOTAXan___-tG31EbsY3LK66zLGc8EKJ3vr45SueVkkv92lASa79Uir8ks0RTA43kT-g4=s0-d-e1-ft#https://www.fairlatterdaysaints.org/wp-content/uploads/2021/08/me-1-150x150.png","contentUrl":"https://ci6.googleusercontent.com/proxy/Mbq6sHeBf0Gv9-j8ncMb5qQsswLfb9RfWICZo8FjyWUsF6PcxzlK6AInZrcOz7MOTAXan___-tG31EbsY3LK66zLGc8EKJ3vr45SueVkkv92lASa79Uir8ks0RTA43kT-g4=s0-d-e1-ft#https://www.fairlatterdaysaints.org/wp-content/uploads/2021/08/me-1-150x150.png"},{"@type":"BreadcrumbList","@id":"https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Blog","item":"https://www.fairlatterdaysaints.org/blog"},{"@type":"ListItem","position":2,"name":"The CES Letter Rebuttal &#8212; Part 29"}]},{"@type":"WebSite","@id":"https://www.fairlatterdaysaints.org/#website","url":"https://www.fairlatterdaysaints.org/","name":"FAIR","description":"Faithful Answers, Informed Response","publisher":{"@id":"https://www.fairlatterdaysaints.org/#organization"},"potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://www.fairlatterdaysaints.org/?s={search_term_string}"},"query-input":"required name=search_term_string"}],"inLanguage":"en-US"},{"@type":"Organization","@id":"https://www.fairlatterdaysaints.org/#organization","name":"FAIR","url":"https://www.fairlatterdaysaints.org/","logo":{"@type":"ImageObject","inLanguage":"en-US","@id":"https://www.fairlatterdaysaints.org/#/schema/logo/image/","url":"https://www.fairlatterdaysaints.org/wp-content/uploads/2021/02/2021_fair_logo_quaternary2.png","contentUrl":"https://www.fairlatterdaysaints.org/wp-content/uploads/2021/02/2021_fair_logo_quaternary2.png","width":805,"height":155,"caption":"FAIR"},"image":{"@id":"https://www.fairlatterdaysaints.org/#/schema/logo/image/"}},{"@type":"Person","@id":"https://www.fairlatterdaysaints.org/#/schema/person/d54f6236bf0b83573dd0d615df471842","name":"Jeff Markham","image":{"@type":"ImageObject","inLanguage":"en-US","@id":"https://www.fairlatterdaysaints.org/#/schema/person/image/","url":"https://secure.gravatar.com/avatar/b02b7f71a6432aa99986552b9bb5aeb9?s=96&d=mm&r=g","contentUrl":"https://secure.gravatar.com/avatar/b02b7f71a6432aa99986552b9bb5aeb9?s=96&d=mm&r=g","caption":"Jeff Markham"},"url":"https://www.fairlatterdaysaints.org/blog/author/jmarkham"}]}</script>
	<!-- / Yoast SEO Premium plugin. -->


<script type='application/javascript'>console.log('PixelYourSite Free version 9.4.7.1');</script>
<link rel='dns-prefetch' href='//www.fairlatterdaysaints.org' />
<link rel='dns-prefetch' href='//www.googletagmanager.com' />
<link rel='dns-prefetch' href='//fonts.googleapis.com' />
		<!-- This site uses the Google Analytics by MonsterInsights plugin v8.21.0 - Using Analytics tracking - https://www.monsterinsights.com/ -->
							<script src="//www.googletagmanager.com/gtag/js?id=G-64574D0HQS"  data-cfasync="false" data-wpfc-render="false" type="text/javascript" async></script>
			<script data-cfasync="false" data-wpfc-render="false" type="text/javascript">
				var mi_version = '8.21.0';
				var mi_track_user = true;
				var mi_no_track_reason = '';

								var disableStrs = [
										'ga-disable-G-64574D0HQS',
									];

				/* Function to detect opted out users */
				function __gtagTrackerIsOptedOut() {
					for (var index = 0; index < disableStrs.length; index++) {
						if (document.cookie.indexOf(disableStrs[index] + '=true') > -1) {
							return true;
						}
					}

					return false;
				}

				/* Disable tracking if the opt-out cookie exists. */
				if (__gtagTrackerIsOptedOut()) {
					for (var index = 0; index < disableStrs.length; index++) {
						window[disableStrs[index]] = true;
					}
				}

				/* Opt-out function */
				function __gtagTrackerOptout() {
					for (var index = 0; index < disableStrs.length; index++) {
						document.cookie = disableStrs[index] + '=true; expires=Thu, 31 Dec 2099 23:59:59 UTC; path=/';
						window[disableStrs[index]] = true;
					}
				}

				if ('undefined' === typeof gaOptout) {
					function gaOptout() {
						__gtagTrackerOptout();
					}
				}
								window.dataLayer = window.dataLayer || [];

				window.MonsterInsightsDualTracker = {
					helpers: {},
					trackers: {},
				};
				if (mi_track_user) {
					function __gtagDataLayer() {
						dataLayer.push(arguments);
					}

					function __gtagTracker(type, name, parameters) {
						if (!parameters) {
							parameters = {};
						}

						if (parameters.send_to) {
							__gtagDataLayer.apply(null, arguments);
							return;
						}

						if (type === 'event') {
														parameters.send_to = monsterinsights_frontend.v4_id;
							var hookName = name;
							if (typeof parameters['event_category'] !== 'undefined') {
								hookName = parameters['event_category'] + ':' + name;
							}

							if (typeof MonsterInsightsDualTracker.trackers[hookName] !== 'undefined') {
								MonsterInsightsDualTracker.trackers[hookName](parameters);
							} else {
								__gtagDataLayer('event', name, parameters);
							}

						} else {
							__gtagDataLayer.apply(null, arguments);
						}
					}

					__gtagTracker('js', new Date());
					__gtagTracker('set', {
						'developer_id.dZGIzZG': true,
											});
										__gtagTracker('config', 'G-64574D0HQS', {"forceSSL":"true","anonymize_ip":"true"} );
															window.gtag = __gtagTracker;										(function () {
						/* https://developers.google.com/analytics/devguides/collection/analyticsjs/ */
						/* ga and __gaTracker compatibility shim. */
						var noopfn = function () {
							return null;
						};
						var newtracker = function () {
							return new Tracker();
						};
						var Tracker = function () {
							return null;
						};
						var p = Tracker.prototype;
						p.get = noopfn;
						p.set = noopfn;
						p.send = function () {
							var args = Array.prototype.slice.call(arguments);
							args.unshift('send');
							__gaTracker.apply(null, args);
						};
						var __gaTracker = function () {
							var len = arguments.length;
							if (len === 0) {
								return;
							}
							var f = arguments[len - 1];
							if (typeof f !== 'object' || f === null || typeof f.hitCallback !== 'function') {
								if ('send' === arguments[0]) {
									var hitConverted, hitObject = false, action;
									if ('event' === arguments[1]) {
										if ('undefined' !== typeof arguments[3]) {
											hitObject = {
												'eventAction': arguments[3],
												'eventCategory': arguments[2],
												'eventLabel': arguments[4],
												'value': arguments[5] ? arguments[5] : 1,
											}
										}
									}
									if ('pageview' === arguments[1]) {
										if ('undefined' !== typeof arguments[2]) {
											hitObject = {
												'eventAction': 'page_view',
												'page_path': arguments[2],
											}
										}
									}
									if (typeof arguments[2] === 'object') {
										hitObject = arguments[2];
									}
									if (typeof arguments[5] === 'object') {
										Object.assign(hitObject, arguments[5]);
									}
									if ('undefined' !== typeof arguments[1].hitType) {
										hitObject = arguments[1];
										if ('pageview' === hitObject.hitType) {
											hitObject.eventAction = 'page_view';
										}
									}
									if (hitObject) {
										action = 'timing' === arguments[1].hitType ? 'timing_complete' : hitObject.eventAction;
										hitConverted = mapArgs(hitObject);
										__gtagTracker('event', action, hitConverted);
									}
								}
								return;
							}

							function mapArgs(args) {
								var arg, hit = {};
								var gaMap = {
									'eventCategory': 'event_category',
									'eventAction': 'event_action',
									'eventLabel': 'event_label',
									'eventValue': 'event_value',
									'nonInteraction': 'non_interaction',
									'timingCategory': 'event_category',
									'timingVar': 'name',
									'timingValue': 'value',
									'timingLabel': 'event_label',
									'page': 'page_path',
									'location': 'page_location',
									'title': 'page_title',
									'referrer' : 'page_referrer',
								};
								for (arg in args) {
																		if (!(!args.hasOwnProperty(arg) || !gaMap.hasOwnProperty(arg))) {
										hit[gaMap[arg]] = args[arg];
									} else {
										hit[arg] = args[arg];
									}
								}
								return hit;
							}

							try {
								f.hitCallback();
							} catch (ex) {
							}
						};
						__gaTracker.create = newtracker;
						__gaTracker.getByName = newtracker;
						__gaTracker.getAll = function () {
							return [];
						};
						__gaTracker.remove = noopfn;
						__gaTracker.loaded = true;
						window['__gaTracker'] = __gaTracker;
					})();
									} else {
										console.log("");
					(function () {
						function __gtagTracker() {
							return null;
						}

						window['__gtagTracker'] = __gtagTracker;
						window['gtag'] = __gtagTracker;
					})();
									}
			</script>
				<!-- / Google Analytics by MonsterInsights -->
		<script type="text/javascript">
/* <![CDATA[ */
window._wpemojiSettings = {"baseUrl":"https:\\/\\/s.w.org\\/images\\/core\\/emoji\\/14.0.0\\/72x72\\/","ext":".png","svgUrl":"https:\\/\\/s.w.org\\/images\\/core\\/emoji\\/14.0.0\\/svg\\/","svgExt":".svg","source":{"concatemoji":"https:\\/\\/www.fairlatterdaysaints.org\\/wp-includes\\/js\\/wp-emoji-release.min.js?ver=6.4.1"}};
/*! This file is auto-generated */
!function(i,n){var o,s,e;function c(e){try{var t={supportTests:e,timestamp:(new Date).valueOf()};sessionStorage.setItem(o,JSON.stringify(t))}catch(e){}}function p(e,t,n){e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(t,0,0);var t=new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data),r=(e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(n,0,0),new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data));return t.every(function(e,t){return e===r[t]})}function u(e,t,n){switch(t){case"flag":return n(e,"\ud83c\udff3\ufe0f\u200d\u26a7\ufe0f","\ud83c\udff3\ufe0f\u200b\u26a7\ufe0f")?!1:!n(e,"\ud83c\uddfa\ud83c\uddf3","\ud83c\uddfa\u200b\ud83c\uddf3")&&!n(e,"\ud83c\udff4\udb40\udc67\udb40\udc62\udb40\udc65\udb40\udc6e\udb40\udc67\udb40\udc7f","\ud83c\udff4\u200b\udb40\udc67\u200b\udb40\udc62\u200b\udb40\udc65\u200b\udb40\udc6e\u200b\udb40\udc67\u200b\udb40\udc7f");case"emoji":return!n(e,"\ud83e\udef1\ud83c\udffb\u200d\ud83e\udef2\ud83c\udfff","\ud83e\udef1\ud83c\udffb\u200b\ud83e\udef2\ud83c\udfff")}return!1}function f(e,t,n){var r="undefined"!=typeof WorkerGlobalScope&&self instanceof WorkerGlobalScope?new OffscreenCanvas(300,150):i.createElement("canvas"),a=r.getContext("2d",{willReadFrequently:!0}),o=(a.textBaseline="top",a.font="600 32px Arial",{});return e.forEach(function(e){o[e]=t(a,e,n)}),o}function t(e){var t=i.createElement("script");t.src=e,t.defer=!0,i.head.appendChild(t)}"undefined"!=typeof Promise&&(o="wpEmojiSettingsSupports",s=["flag","emoji"],n.supports={everything:!0,everythingExceptFlag:!0},e=new Promise(function(e){i.addEventListener("DOMContentLoaded",e,{once:!0})}),new Promise(function(t){var n=function(){try{var e=JSON.parse(sessionStorage.getItem(o));if("object"==typeof e&&"number"==typeof e.timestamp&&(new Date).valueOf()<e.timestamp+604800&&"object"==typeof e.supportTests)return e.supportTests}catch(e){}return null}();if(!n){if("undefined"!=typeof Worker&&"undefined"!=typeof OffscreenCanvas&&"undefined"!=typeof URL&&URL.createObjectURL&&"undefined"!=typeof Blob)try{var e="postMessage("+f.toString()+"("+[JSON.stringify(s),u.toString(),p.toString()].join(",")+"));",r=new Blob([e],{type:"text/javascript"}),a=new Worker(URL.createObjectURL(r),{name:"wpTestEmojiSupports"});return void(a.onmessage=function(e){c(n=e.data),a.terminate(),t(n)})}catch(e){}c(n=f(s,u,p))}t(n)}).then(function(e){for(var t in e)n.supports[t]=e[t],n.supports.everything=n.supports.everything&&n.supports[t],"flag"!==t&&(n.supports.everythingExceptFlag=n.supports.everythingExceptFlag&&n.supports[t]);n.supports.everythingExceptFlag=n.supports.everythingExceptFlag&&!n.supports.flag,n.DOMReady=!1,n.readyCallback=function(){n.DOMReady=!0}}).then(function(){return e}).then(function(){var e;n.supports.everything||(n.readyCallback(),(e=n.source||{}).concatemoji?t(e.concatemoji):e.wpemoji&&e.twemoji&&(t(e.twemoji),t(e.wpemoji)))}))}((window,document),window._wpemojiSettings);
/* ]]> */
</script>
<link rel='stylesheet' id='fairmormon-genesis-css' href='https://www.fairlatterdaysaints.org/wp-content/themes/genesis-fairmormon/style.css?ver=1.0.0' type='text/css' media='all' />
<style id='wp-emoji-styles-inline-css' type='text/css'>

	img.wp-smiley, img.emoji {
		display: inline !important;
		border: none !important;
		box-shadow: none !important;
		height: 1em !important;
		width: 1em !important;
		margin: 0 0.07em !important;
		vertical-align: -0.1em !important;
		background: none !important;
		padding: 0 !important;
	}
</style>
<link rel='stylesheet' id='wp-block-library-css' href='https://www.fairlatterdaysaints.org/wp-includes/css/dist/block-library/style.min.css?ver=6.4.1' type='text/css' media='all' />
<link rel='stylesheet' id='activecampaign-form-block-css' href='https://www.fairlatterdaysaints.org/wp-content/plugins/activecampaign-subscription-forms/activecampaign-form-block/build/style-index.css?ver=1696888809' type='text/css' media='all' />
<style id='powerpress-player-block-style-inline-css' type='text/css'>


</style>
<style id='classic-theme-styles-inline-css' type='text/css'>
/*! This file is auto-generated */
.wp-block-button__link{color:#fff;background-color:#32373c;border-radius:9999px;box-shadow:none;text-decoration:none;padding:calc(.667em + 2px) calc(1.333em + 2px);font-size:1.125em}.wp-block-file__button{background:#32373c;color:#fff;text-decoration:none}
</style>
<style id='global-styles-inline-css' type='text/css'>
body{--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgba(255, 255, 255, 1), 6px 6px rgba(0, 0, 0, 1);--wp--preset--shadow--crisp: 6px 6px 0px rgba(0, 0, 0, 1);}:where(.is-layout-flex){gap: 0.5em;}:where(.is-layout-grid){gap: 0.5em;}body .is-layout-flow > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}body .is-layout-flow > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}body .is-layout-flow > .aligncenter{margin-left: auto !important;margin-right: auto !important;}body .is-layout-constrained > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}body .is-layout-constrained > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}body .is-layout-constrained > .aligncenter{margin-left: auto !important;margin-right: auto !important;}body .is-layout-constrained > :where(:not(.alignleft):not(.alignright):not(.alignfull)){max-width: var(--wp--style--global--content-size);margin-left: auto !important;margin-right: auto !important;}body .is-layout-constrained > .alignwide{max-width: var(--wp--style--global--wide-size);}body .is-layout-flex{display: flex;}body .is-layout-flex{flex-wrap: wrap;align-items: center;}body .is-layout-flex > *{margin: 0;}body .is-layout-grid{display: grid;}body .is-layout-grid > *{margin: 0;}:where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}:where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
.wp-block-navigation a:where(:not(.wp-element-button)){color: inherit;}
:where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}
:where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}
.wp-block-pullquote{font-size: 1.5em;line-height: 1.6;}
</style>
<link rel='stylesheet' id='wpml-legacy-horizontal-list-0-css' href='https://www.fairlatterdaysaints.org/wp-content/plugins/sitepress-multilingual-cms/templates/language-switchers/legacy-list-horizontal/style.min.css?ver=1' type='text/css' media='all' />
<link rel='stylesheet' id='fairmormon-fonts-css' href='//fonts.googleapis.com/css?family=Roboto%3A300%2C400%2C400i%2C600%2C700%2C700i&#038;ver=1.0.0' type='text/css' media='all' />
<link rel='stylesheet' id='dashicons-css' href='https://www.fairlatterdaysaints.org/wp-includes/css/dashicons.min.css?ver=6.4.1' type='text/css' media='all' />
<link rel='stylesheet' id='tablepress-default-css' href='https://www.fairlatterdaysaints.org/wp-content/tablepress-combined.min.css?ver=27' type='text/css' media='all' />
<link rel='stylesheet' id='tablepress-responsive-tables-css' href='https://www.fairlatterdaysaints.org/wp-content/plugins/tablepress-responsive-tables/css/tablepress-responsive.min.css?ver=1.8' type='text/css' media='all' />
<link rel='stylesheet' id='elementor-frontend-css' href='https://www.fairlatterdaysaints.org/wp-content/uploads/elementor/css/custom-frontend.min.css?ver=1699455031' type='text/css' media='all' />
<link rel='stylesheet' id='eael-general-css' href='https://www.fairlatterdaysaints.org/wp-content/plugins/essential-addons-for-elementor-lite/assets/front-end/css/view/general.min.css?ver=5.9' type='text/css' media='all' />
<script type="text/javascript" src="https://www.fairlatterdaysaints.org/wp-content/plugins/google-analytics-premium/assets/js/frontend-gtag.min.js?ver=8.21.0" id="monsterinsights-frontend-script-js"></script>
<script data-cfasync="false" data-wpfc-render="false" type="text/javascript" id='monsterinsights-frontend-script-js-extra'>/* <![CDATA[ */
var monsterinsights_frontend = {"js_events_tracking":"true","download_extensions":"doc,pdf,ppt,zip,xls,docx,pptx,xlsx","inbound_paths":"[]","home_url":"https:\\/\\/www.fairlatterdaysaints.org","hash_tracking":"false","v4_id":"G-64574D0HQS"};/* ]]> */
</script>
<script type="text/javascript" src="https://www.fairlatterdaysaints.org/wp-includes/js/jquery/jquery.min.js?ver=3.7.1" id="jquery-core-js"></script>
<script type="text/javascript" src="https://www.fairlatterdaysaints.org/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.4.1" id="jquery-migrate-js"></script>
<script type="text/javascript" src="https://www.fairlatterdaysaints.org/wp-content/plugins/pixelyoursite/dist/scripts/jquery.bind-first-0.2.3.min.js?ver=6.4.1" id="jquery-bind-first-js"></script>
<script type="text/javascript" src="https://www.fairlatterdaysaints.org/wp-content/plugins/pixelyoursite/dist/scripts/js.cookie-2.1.3.min.js?ver=2.1.3" id="js-cookie-pys-js"></script>
<script type="text/javascript" id="pys-js-extra">
/* <![CDATA[ */
var pysOptions = {"staticEvents":[],"dynamicEvents":[],"triggerEvents":[],"triggerEventTypes":[],"debug":"","siteUrl":"https:\\/\\/www.fairlatterdaysaints.org","ajaxUrl":"https:\\/\\/www.fairlatterdaysaints.org\\/wp-admin\\/admin-ajax.php","ajax_event":"8adc6c6dcd","enable_remove_download_url_param":"1","cookie_duration":"7","last_visit_duration":"60","enable_success_send_form":"","ajaxForServerEvent":"1","send_external_id":"1","external_id_expire":"180","gdpr":{"ajax_enabled":false,"all_disabled_by_api":false,"facebook_disabled_by_api":false,"analytics_disabled_by_api":false,"google_ads_disabled_by_api":false,"pinterest_disabled_by_api":false,"bing_disabled_by_api":false,"externalID_disabled_by_api":false,"facebook_prior_consent_enabled":true,"analytics_prior_consent_enabled":true,"google_ads_prior_consent_enabled":null,"pinterest_prior_consent_enabled":true,"bing_prior_consent_enabled":true,"cookiebot_integration_enabled":false,"cookiebot_facebook_consent_category":"marketing","cookiebot_analytics_consent_category":"statistics","cookiebot_tiktok_consent_category":"marketing","cookiebot_google_ads_consent_category":null,"cookiebot_pinterest_consent_category":"marketing","cookiebot_bing_consent_category":"marketing","consent_magic_integration_enabled":false,"real_cookie_banner_integration_enabled":false,"cookie_notice_integration_enabled":false,"cookie_law_info_integration_enabled":false},"cookie":{"disabled_all_cookie":false,"disabled_advanced_form_data_cookie":false,"disabled_landing_page_cookie":false,"disabled_first_visit_cookie":false,"disabled_trafficsource_cookie":false,"disabled_utmTerms_cookie":false,"disabled_utmId_cookie":false},"woo":{"enabled":false},"edd":{"enabled":false}};
/* ]]> */
</script>
<script type="text/javascript" src="https://www.fairlatterdaysaints.org/wp-content/plugins/pixelyoursite/dist/scripts/public.js?ver=9.4.7.1" id="pys-js"></script>

<!-- Google Analytics snippet added by Site Kit -->
<script type="text/javascript" src="https://www.googletagmanager.com/gtag/js?id=UA-227265837-1" id="google_gtagjs-js" async></script>
<script type="text/javascript" id="google_gtagjs-js-after">
/* <![CDATA[ */
window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}
gtag('set', 'linker', {"domains":["www.fairlatterdaysaints.org"]} );
gtag("js", new Date());
gtag("set", "developer_id.dZTNiMT", true);
gtag("config", "UA-227265837-1", {"anonymize_ip":true});
gtag("config", "G-64574D0HQS");
/* ]]> */
</script>

<!-- End Google Analytics snippet added by Site Kit -->
<link rel="https://api.w.org/" href="https://www.fairlatterdaysaints.org/wp-json/" /><link rel="alternate" type="application/json" href="https://www.fairlatterdaysaints.org/wp-json/wp/v2/posts/29906" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://www.fairlatterdaysaints.org/xmlrpc.php?rsd" />
<meta name="generator" content="WordPress 6.4.1" />
<link rel='shortlink' href='https://www.fairlatterdaysaints.org/?p=29906' />
<link rel="alternate" type="application/json+oembed" href="https://www.fairlatterdaysaints.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.fairlatterdaysaints.org%2Fblog%2F2021%2F11%2F26%2Fthe-ces-letter-rebuttal-part-29" />
<link rel="alternate" type="text/xml+oembed" href="https://www.fairlatterdaysaints.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.fairlatterdaysaints.org%2Fblog%2F2021%2F11%2F26%2Fthe-ces-letter-rebuttal-part-29&#038;format=xml" />
<meta name="generator" content="WPML ver:4.6.7 stt:1,3,42,2;" />
<meta name="generator" content="Site Kit by Google 1.114.0" /><script type="text/javascript"><!--
function powerpress_pinw(pinw_url){window.open(pinw_url, 'PowerPressPlayer','toolbar=0,status=0,resizable=1,width=460,height=320');	return false;}
//-->
</script>
<meta name="p:domain_verify" content="80b3e17da364889494768bef3ae164fe"/>
<meta name="follow.it-verification-code" content="shW4S5TXDzcfXYJXtRxy"/><style type="text/css">.site-title a { background: url(https://www.fairlatterdaysaints.org/wp-content/uploads/2021/02/cropped-2021_fair_logo_quaternary2-1.png) no-repeat !important; }</style>
<meta name="generator" content="Elementor 3.17.3; features: e_dom_optimization, e_optimized_assets_loading, additional_custom_breakpoints; settings: css_print_method-internal, google_font-enabled, font_display-auto">
<style type="text/css">.recentcomments a{display:inline !important;padding:0 !important;margin:0 !important;}</style><script type='application/javascript'>console.warn('PixelYourSite: no pixel configured.');</script>


		<!-- MonsterInsights Media Tracking -->
		<script data-cfasync="false" data-wpfc-render="false" type="text/javascript">
			var monsterinsights_tracked_video_marks = {};
			var monsterinsights_youtube_percentage_tracking_timeouts = {};

			/* Works for YouTube and Vimeo */
			function monsterinsights_media_get_id_for_iframe( source, service ) {
				var iframeUrlParts = source.split('?');
				var stripedUrl = iframeUrlParts[0].split('/');
				var videoId = stripedUrl[ stripedUrl.length - 1 ];

				return service + '-player-' + videoId;
			}

			function monsterinsights_media_record_video_event( provider, event, label, parameters = {} ) {
				__gtagTracker('event', event, {
					event_category: 'video-' + provider,
					event_label: label,
					non_interaction: event === 'impression',
					...parameters
				});
			}

			function monsterinsights_media_maybe_record_video_progress( provider, label, videoId, videoParameters ) {
				var progressTrackingAllowedMarks = [10,25,50,75];

				if ( typeof monsterinsights_tracked_video_marks[ videoId ] == 'undefined' ) {
					monsterinsights_tracked_video_marks[ videoId ] = [];
				}

				var { video_percent } = videoParameters;

				if ( progressTrackingAllowedMarks.includes( video_percent ) && !monsterinsights_tracked_video_marks[ videoId ].includes( video_percent ) ) {
					monsterinsights_media_record_video_event( provider, 'video_progress', label, videoParameters );

					/* Prevent multiple records for the same percentage */
					monsterinsights_tracked_video_marks[ videoId ].push( video_percent );
				}
			}

			/* --- Vimeo --- */
            var monsterinsights_media_vimeo_plays = {};

            function monsterinsights_setup_vimeo_events_for_iframe(iframe, title, player) {
                var playerId = iframe.getAttribute('id');
                var videoLabel = title || iframe.title || iframe.getAttribute('src');

                if ( !playerId ) {
                    playerId = monsterinsights_media_get_id_for_iframe( iframe.getAttribute('src'), 'vimeo' );
                    iframe.setAttribute( 'id', playerId );
                }

                monsterinsights_media_vimeo_plays[playerId] = 0;

                var videoParameters = {
                    video_provider: 'vimeo',
                    video_title: title,
                    video_url: iframe.getAttribute('src')
                };

                /**
                 * Record Impression
                 **/
                monsterinsights_media_record_video_event( 'vimeo', 'impression', videoLabel, videoParameters );

                /**
                 * Record video start
                 **/
                player.on('play', function(data) {
                    let playerId = this.element.id;
                    if ( monsterinsights_media_vimeo_plays[playerId] === 0 ) {
                        monsterinsights_media_vimeo_plays[playerId]++;

                        videoParameters.video_duration = data.duration;
                        videoParameters.video_current_time = data.seconds;
                        videoParameters.video_percent = 0;

                        monsterinsights_media_record_video_event( 'vimeo', 'video_start', videoLabel, videoParameters );
                    }
                });

                /**
                 * Record video progress
                 **/
                player.on('timeupdate', function(data) {
                    var progress = Math.floor(data.percent * 100);

                    videoParameters.video_duration = data.duration;
                    videoParameters.video_current_time = data.seconds;
                    videoParameters.video_percent = progress;

                    monsterinsights_media_maybe_record_video_progress( 'vimeo', videoLabel, playerId, videoParameters );
                });

                /**
                 * Record video complete
                 **/
                player.on('ended', function(data) {
                    videoParameters.video_duration = data.duration;
                    videoParameters.video_current_time = data.seconds;
                    videoParameters.video_percent = 100;

                    monsterinsights_media_record_video_event( 'vimeo', 'video_complete', videoLabel, videoParameters );
                });
            }

			function monsterinsights_on_vimeo_load() {

				var vimeoIframes = document.querySelectorAll("iframe[src*='vimeo']");

				vimeoIframes.forEach(function( iframe ) {
                    //  Set up the player
					var player = new Vimeo.Player(iframe);

                    //  The getVideoTitle function returns a promise
                    player.getVideoTitle().then(function(title) {
                        /*
                         * Binding the events inside this callback guarantees that we
                         * always have the correct title for the video
                         */
                        monsterinsights_setup_vimeo_events_for_iframe(iframe, title, player)
                    });
				});
			}

			function monsterinsights_media_init_vimeo_events() {
				var vimeoIframes = document.querySelectorAll("iframe[src*='vimeo']");

				if ( vimeoIframes.length ) {

					/* Maybe load Vimeo API */
					if ( window.Vimeo === undefined ) {
						var tag = document.createElement("script");
						tag.src = "https://player.vimeo.com/api/player.js";
						tag.setAttribute("onload", "monsterinsights_on_vimeo_load()");
						document.body.append(tag);
					} else {
						/* Vimeo API already loaded, invoke callback */
						monsterinsights_on_vimeo_load();
					}
				}
			}

			/* --- End Vimeo --- */

			/* --- YouTube --- */
			function monsterinsights_media_on_youtube_load() {
				var monsterinsights_media_youtube_plays = {};

				function __onPlayerReady(event) {
					monsterinsights_media_youtube_plays[event.target.h.id] = 0;

					var videoParameters = {
						video_provider: 'youtube',
						video_title: event.target.videoTitle,
						video_url: event.target.playerInfo.videoUrl
					};
					monsterinsights_media_record_video_event( 'youtube', 'impression', videoParameters.video_title, videoParameters );
				}

				/**
				 * Record progress callback
				 **/
				function __track_youtube_video_progress( player, videoLabel, videoParameters ) {
					var { playerInfo } = player;
					var playerId = player.h.id;

					var duration = playerInfo.duration; /* player.getDuration(); */
					var currentTime = playerInfo.currentTime; /* player.getCurrentTime(); */

					var percentage = (currentTime / duration) * 100;
					var progress = Math.floor(percentage);

					videoParameters.video_duration = duration;
					videoParameters.video_current_time = currentTime;
					videoParameters.video_percent = progress;

					monsterinsights_media_maybe_record_video_progress( 'youtube', videoLabel, playerId, videoParameters );
				}

				function __youtube_on_state_change( event ) {
					var state = event.data;
					var player = event.target;
					var { playerInfo } = player;
					var playerId = player.h.id;

					var videoParameters = {
						video_provider: 'youtube',
						video_title: player.videoTitle,
						video_url: playerInfo.videoUrl
					};

					/**
					 * YouTube's API doesn't offer a progress or timeupdate event.
					 * We have to track progress manually by asking the player for the current time, every X milliseconds, using an
    interval
					 **/

					if ( state === YT.PlayerState.PLAYING) {
						if ( monsterinsights_media_youtube_plays[playerId] === 0 ) {
							monsterinsights_media_youtube_plays[playerId]++;
							/**
							 * Record video start
							 **/
							videoParameters.video_duration = playerInfo.duration;
							videoParameters.video_current_time = playerInfo.currentTime;
							videoParameters.video_percent = 0;

							monsterinsights_media_record_video_event( 'youtube', 'video_start', videoParameters.video_title, videoParameters );
						}

						monsterinsights_youtube_percentage_tracking_timeouts[ playerId ] = setInterval(
							__track_youtube_video_progress,
							500,
							player,
							videoParameters.video_title,
							videoParameters
						);
					} else if ( state === YT.PlayerState.PAUSED ) {
						/* When the video is paused clear the interval */
						clearInterval( monsterinsights_youtube_percentage_tracking_timeouts[ playerId ] );
					} else if ( state === YT.PlayerState.ENDED ) {

						/**
						 * Record video complete
						 **/
						videoParameters.video_duration = playerInfo.duration;
						videoParameters.video_current_time = playerInfo.currentTime;
						videoParameters.video_percent = 100;

						monsterinsights_media_record_video_event( 'youtube', 'video_complete', videoParameters.video_title, videoParameters );
						clearInterval( monsterinsights_youtube_percentage_tracking_timeouts[ playerId ] );
					}
				}

				var youtubeIframes = document.querySelectorAll("iframe[src*='youtube'],iframe[src*='youtu.be']");

				youtubeIframes.forEach(function( iframe ) {
					var playerId = iframe.getAttribute('id');

					if ( !playerId ) {
						playerId = monsterinsights_media_get_id_for_iframe( iframe.getAttribute('src'), 'youtube' );
						iframe.setAttribute( 'id', playerId );
					}

					new YT.Player(playerId, {
						events: {
							onReady: __onPlayerReady,
							onStateChange: __youtube_on_state_change
						}
					});
				});
			}

			function monsterinsights_media_load_youtube_api() {
				if ( window.YT ) {
					return;
				}

				var youtubeIframes = document.querySelectorAll("iframe[src*='youtube'],iframe[src*='youtu.be']");
				if ( 0 === youtubeIframes.length ) {
					return;
				}

				var tag = document.createElement("script");
				tag.src = "https://www.youtube.com/iframe_api";
				var firstScriptTag = document.getElementsByTagName('script')[0];
				firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
			}

			function monsterinsights_media_init_youtube_events() {
				/* YouTube always looks for a function called onYouTubeIframeAPIReady */
				window.onYouTubeIframeAPIReady = monsterinsights_media_on_youtube_load;
			}
			/* --- End YouTube --- */

			/* --- HTML Videos --- */
			function monsterinsights_media_init_html_video_events() {
				var monsterinsights_media_html_plays = {};
				var videos = document.querySelectorAll('video');
				var videosCount = 0;

				videos.forEach(function( video ) {

					var videoLabel = video.title;

					if ( !videoLabel ) {
						var videoCaptionEl = video.nextElementSibling;

						if ( videoCaptionEl && videoCaptionEl.nodeName.toLowerCase() === 'figcaption' ) {
							videoLabel = videoCaptionEl.textContent;
						} else {
							videoLabel = video.getAttribute('src');
						}
					}

					var videoTitle = videoLabel;

					var playerId = video.getAttribute('id');

					if ( !playerId ) {
						playerId = 'html-player-' + videosCount;
						video.setAttribute('id', playerId);
					}

					monsterinsights_media_html_plays[playerId] = 0

					var videoParameters = {
						video_provider: 'html',
						video_title: videoTitle,
						video_url: video.getAttribute('src')
					};

					/**
					 * Record Impression
					 **/
					monsterinsights_media_record_video_event( 'html', 'impression', videoLabel, videoParameters );

					/**
					 * Record video start
					 **/
					video.addEventListener('play', function(event) {
						let playerId = event.target.id;
						if ( monsterinsights_media_html_plays[playerId] === 0 ) {
							monsterinsights_media_html_plays[playerId]++;

							videoParameters.video_duration = video.duration;
							videoParameters.video_current_time = video.currentTime;
							videoParameters.video_percent = 0;

							monsterinsights_media_record_video_event( 'html', 'video_start', videoLabel, videoParameters );
						}
					}, false );

					/**
					 * Record video progress
					 **/
					video.addEventListener('timeupdate', function() {
						var percentage = (video.currentTime / video.duration) * 100;
						var progress = Math.floor(percentage);

						videoParameters.video_duration = video.duration;
						videoParameters.video_current_time = video.currentTime;
						videoParameters.video_percent = progress;

						monsterinsights_media_maybe_record_video_progress( 'html', videoLabel, playerId, videoParameters );
					}, false );

					/**
					 * Record video complete
					 **/
					video.addEventListener('ended', function() {
						var percentage = (video.currentTime / video.duration) * 100;
						var progress = Math.floor(percentage);

						videoParameters.video_duration = video.duration;
						videoParameters.video_current_time = video.currentTime;
						videoParameters.video_percent = progress;

						monsterinsights_media_record_video_event( 'html', 'video_complete', videoLabel, videoParameters );
					}, false );

					videosCount++;
				});
			}
			/* --- End HTML Videos --- */

			function monsterinsights_media_init_video_events() {
				/**
				 * HTML Video - Attach events & record impressions
				 */
				monsterinsights_media_init_html_video_events();

				/**
				 * Vimeo - Attach events & record impressions
				 */
				monsterinsights_media_init_vimeo_events();

				monsterinsights_media_load_youtube_api();
			}

			/* Attach events */
			function monsterinsights_media_load() {

				if ( typeof(__gtagTracker) === 'undefined' ) {
					setTimeout(monsterinsights_media_load, 200);
					return;
				}

				if ( window.addEventListener ) {
					window.addEventListener( "load", monsterinsights_media_init_video_events, false );
				} else if ( window.attachEvent ) {
					window.attachEvent( "onload", monsterinsights_media_init_video_events);
				}

				/**
				 * YouTube - Attach events & record impressions.
				 * We don't need to attach this into page load event
				 * because we already use YT function "onYouTubeIframeAPIReady"
				 * and this will help on using onReady event with the player instantiation.
				 */
				monsterinsights_media_init_youtube_events();
			}

			monsterinsights_media_load();
		</script>
		<!-- End MonsterInsights Media Tracking -->


<link rel="icon" href="https://www.fairlatterdaysaints.org/wp-content/uploads/2021/02/cropped-2021_fair_logo_social_fb-32x32.png" sizes="32x32" />
<link rel="icon" href="https://www.fairlatterdaysaints.org/wp-content/uploads/2021/02/cropped-2021_fair_logo_social_fb-192x192.png" sizes="192x192" />
<link rel="apple-touch-icon" href="https://www.fairlatterdaysaints.org/wp-content/uploads/2021/02/cropped-2021_fair_logo_social_fb-180x180.png" />
<meta name="msapplication-TileImage" content="https://www.fairlatterdaysaints.org/wp-content/uploads/2021/02/cropped-2021_fair_logo_social_fb-270x270.png" />
		<style type="text/css" id="wp-custom-css">
			/* #_form_5B074FC86CDF0_ {
	margin: 30px auto !important;
	width: 100% !important;
}

@media screen and (min-width: 960px) {
	#_form_5B074FC86CDF0_ {
		float: right;
		width: 45% !important;
		margin: 0 0 0 40px !important;
	}
} */



.widget .rss-widget-icon { display: none; }

/* Responsive table for FM Conference; added by Mike Parker, 21 July 2017 */
@media screen and (max-width: 750px) {
.divTable {
  }
.divTableBody {
  }
.divTableRow {
  margin-top: 10px;
  }
.divTableHead, .divTableHeader {
  display: none;
  }
.divTableCellNoWrap, .divTableCellWrap, .divTableHeader {
  display: block;
  empty-cells: hide;
  }
}
@media screen and (min-width: 751px) {
.divTable {
  display: table;
  empty-cells: show;
  }
.divTableBody {
  display: table-row-group;
  }
.divTableHead, .divTableRow {
  display: table-row;
  }
.divTableHeader {
  font-weight: bold;
  }
.divTableCellNoWrap, .divTableCellWrap, .divTableHeader {
  display: table-cell;
  border-bottom: 1px solid gray;
  padding: 3px 10px;
  }
.divTableCellNoWrap {
  max-width:100%;
  white-space:nowrap;
  }
}

/* Sale! banner on Bookstore nav */
.menu-item-14493 a span:after {
    content: "Sale!";
    background: #009abf;
    color: #fff;
    font-size: .7em;
    display: inline-block;
    text-align: center;
    padding: 2px;
    border-radius: 10px;
    width: 50px;
    margin-left: 10px;
    position: relative;
    top: -2px;
}

/* Bring nav items closer together when Sale banner is active since it takes up room and pushes search icon to next line on 13in laptops */
/* .genesis-nav-menu a {
    padding: 9px 16px 20px;
} */
.aboutus__title {
	font-size: 36px;
}

/* wide width image */
.alignfull {
	  margin: 32px calc(50% - 50vw);
	  max-width: 100vw;
	  width: 100vw;
	  overflow: hidden; width: 100%;
}

		</style>
		</head>
<body class="post-template-default single single-post postid-29906 single-format-standard custom-header header-image content-sidebar genesis-breadcrumbs-hidden genesis-footer-widgets-visible elementor-default elementor-kit-23333"><div class="site-container"><ul class="genesis-skip-link"><li><a href="#genesis-nav-primary" class="screen-reader-shortcut"> Skip to primary navigation</a></li><li><a href="#genesis-content" class="screen-reader-shortcut"> Skip to main content</a></li><li><a href="#genesis-sidebar-primary" class="screen-reader-shortcut"> Skip to primary sidebar</a></li><li><a href="#genesis-footer-widgets" class="screen-reader-shortcut"> Skip to footer</a></li></ul><header class="site-header"><div class="wrap"><div class="title-area"><p class="site-title"><a href="https://www.fairlatterdaysaints.org/">FAIR</a></p></div><div class="widget-area header-widget-area"><section id="text-3" class="widget widget_text"><div class="widget-wrap">			<div class="textwidget"><p><strong><a href="https://www.fairlatterdaysaints.org/fair-come-follow-me-2023">Faithful Study Resources for Come, Follow Me</a></strong></p>
</div>
		</div></section>
</div></div></header><nav class="nav-primary" aria-label="Main" id="genesis-nav-primary"><div class="wrap"><ul id="menu-main-menu" class="menu genesis-nav-menu menu-primary js-superfish"><li id="menu-item-14463" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14463"><a href="https://www.fairlatterdaysaints.org/find-answers"><span >Find Answers</span></a></li>
<li id="menu-item-16747" class="menu-item menu-item-type-post_type menu-item-object-page current_page_parent menu-item-16747"><a href="https://www.fairlatterdaysaints.org/blog"><span >Blog</span></a></li>
<li id="menu-item-14481" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14481"><a href="https://www.fairlatterdaysaints.org/media"><span >Media &#038; Apps</span></a></li>
<li id="menu-item-14485" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14485"><a href="https://www.fairlatterdaysaints.org/conference"><span >Conference</span></a></li>
<li id="menu-item-14493" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-14493"><a href="http://www.fairlatterdaysaints.org/store/"><span >Bookstore</span></a></li>
<li id="menu-item-14502" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14502"><a href="https://www.fairlatterdaysaints.org/archive"><span >Archive</span></a></li>
<li id="menu-item-14507" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14507"><a href="https://www.fairlatterdaysaints.org/about"><span >About</span></a></li>
<li id="menu-item-18132" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-18132"><a href="https://www.fairlatterdaysaints.org/get-involved"><span >Get Involved</span></a></li>
<li id="menu-item-14732" class="menu-item__search menu-item menu-item-type-post_type menu-item-object-page menu-item-14732"><a href="https://www.fairlatterdaysaints.org/search"><span >Search</span></a></li>
</ul></div></nav><div class="site-inner"><div class="content-sidebar-wrap"><main class="content" id="genesis-content"><article class="post-29906 post type-post status-publish format-standard category-anti-mormon-critics category-apologetics category-ces-letter category-faith-crisis category-lds-history entry" aria-label="The CES Letter Rebuttal &#8212; Part 29"><header class="entry-header"><h1 class="entry-title">The CES Letter Rebuttal &#8212; Part 29</h1>
<p class="entry-meta"><time class="entry-time">November 26, 2021</time> by <span class="entry-author"><a href="https://www.fairlatterdaysaints.org/blog/author/jmarkham" class="entry-author-link" rel="author"><span class="entry-author-name">Jeff Markham</span></a></span>  </p></header><div class="entry-content"><h2>Part 29: CES Letter Prophet Questions [Section C]</h2>
<h4>by Sarah Allen</h4>
<p>&nbsp;</p>
<p>Today, we’re going to talk about one of my favorite weird/controversial topics of Church history, Blood Atonement and the way it was so badly misconstrued. <a href="https://www.jstor.org/stable/pdf/25101102.pdf">You can see a highly biased approach to the topic here for an example of what I’m talking about</a>. It’s such a caricature of the actual teaching, I honestly thought it was facetious satire at first before I realized the author was serious. To be honest, on its own, Blood Atonement is just not that interesting or even very strange. It’s basically just exaggerated rhetoric to make a point.</p>
<p>In my free time, though, I like to write fiction. I love stories: watching them, reading them, writing them, imagining them. It’s one of the reasons I enjoy history so much, because it’s just a compilation of a million different stories. Because of that, I love the larger mythology of Blood Atonement and the way something so simple could become so exaggerated and ludicrous and take on a life of its own. It’s fascinating to me. This is why, later in the post, I also want to touch on the stories of the Danites and also Mountain Meadows, and how they both tie into the folklore surrounding Blood Atonement. I’m going to try to put it all into some historical context for you guys so that it all makes sense.<span id="more-29906"></span></p>
<p>Remember last week when I talked about Brigham Young’s theatrical style of preaching? That comes heavily into play this week. Part of the “<a href="https://en.wikipedia.org/wiki/Fire_and_brimstone">fire and brimstone</a>” style of preaching was exaggerated, over-the-top, violent imagery, like sermons about being cast into the fire or hewn down by the Lord in graphic detail, that kind thing. It’s out of place in our society today, but in the 1800s it was a popular style in Protestant circles, from which many of the early Saints converted. You don’t have to look any farther than Sidney Rigdon to see that style in practice. His infamous <a href="http://www.sidneyrigdon.com/rigd1838.htm">Independence Day speech</a> and so-called “<a href="https://en.wikipedia.org/wiki/Salt_Sermon">Salt Sermon</a>” are prime examples. [Note: The text of the Salt Sermon does not exist anymore; all we have are references to its content.] Jonathan Edwards’s “<a href="https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1053&amp;context=etas">Sinners in the Hands of an Angry God</a>” is another such surviving sermon that is still well-known today.</p>
<p>The early Saints were familiar with this style of preaching and <a href="https://www.youtube.com/watch?v=poMERlofOcM">many found it to be highly entertaining</a>. They knew that Brigham cared about them and wanted to see them stay strong in the gospel, so they understood that his words were often for effect or sometimes for shock value rather than his legitimate views.</p>
<p><a href="https://sunstonemagazine.com/wp-content/uploads/sbi/articles/039-04-09.pdf">One quote of Brigham’s says</a>:</p>
<blockquote><p><em>When you wish the people to feel what you say, you have got to use language that they will remember, or else the ideas are lost to them. Consequently, in many instances we use language that we would rather not use.  </em></p></blockquote>
<p>It’s something that often gets lost in translation today. When we read over his words, they come across differently to us than they would have in person at the time, because we aren’t familiar with that style of teaching. We don’t know Brigham, we don’t know what the atmosphere was like at those events, we aren’t familiar with the social climate of that society, and the rhetoric often comes across as extreme and bizarre to us. But that isn’t the way it came across to the Saints under Brigham’s leadership. He liked to bluster and he could be difficult in several ways, no doubt, but for the most part, they loved him and knew that he loved them in return. This is demonstrated by many of the quotes found in the previously linked article.</p>
<p>These are things we need to keep in mind while diving into this section, because the language used while discussing Blood Atonement definitely lands on the extreme side of things at times.</p>
<p>Jeremy begins with this:</p>
<p><strong><em>Along with Adam-God, Brigham taught a doctrine known as “Blood Atonement” where a person’s blood had to be shed to atone for their own sins as it was beyond the atonement of Jesus Christ.</em></strong></p>
<p><strong><em>“There are sins that men commit for which they cannot receive forgiveness in this world, or in that which is to come, and if they had their eyes open to see their true condition, they would be perfectly willing to have their blood spilt upon the ground, that the smoke thereof might ascend to heaven as an offering for their sins; and the smoking incense would atone for their sins, whereas, if such is not the case, they will stick to them and remain upon them in the spirit world.</em></strong></p>
<p><strong><em>I know, when you hear my brethren telling about cutting people off from the earth, that you consider it is strong doctrine; but it is to save them, not to destroy them…</em></strong></p>
<p><strong><em>And furthermore, I know that there are transgressors, who, if they knew themselves, and the only condition upon which they can obtain forgiveness, would beg of their brethren to shed their blood, that the smoke thereof might ascend to God as an offering to appease the wrath that is kindled against them, and that the law might have its course. I will say further;</em></strong></p>
<p><strong><em>I have had men come to me and offer their lives to atone for their sins. It is true that the blood of the Son of God was shed for sins through the fall and those committed by men, yet men can commit sins which it can never remit&#8230;There are sins that can be atoned for by an offering upon an altar, as in ancient days; and there are sins that the blood of a lamb, or a calf, or of turtle dove, cannot remit, but they must be atoned for by the blood of the man.” </em></strong><strong>– Journal of Discourses 4:53-54</strong></p>
<p>Yes. Again, though, this is from the <em>Journal of Discourses</em>, so we need to understand that, while Brigham certainly taught something like this, <a href="https://byustudies.byu.edu/article/the-prophets-have-spoken-but-what-did-they-say-examining-the-differences-between-george-d-watts-original-shorthand-notes-and-the-sermons-published-in-the-journal-of-discourses/?post_type=article&amp;p=8081">the actual wording may be quite different</a>. I’m not saying this quote is inaccurate, but I am saying that we can’t be certain of that. <a href="https://catalog.churchofjesuschrist.org/record/5df3b7da-d0a5-437b-8268-7dde8a87c76e/ec1c0cde-2383-437c-b325-84314950c287?view=browse">This is not a sermon we have the shorthand transcript for</a>, so we don’t know what was altered.</p>
<p>Regardless, yes, this is the gist of Blood Atonement, at least as far as anyone alive today is aware. Basically, the teaching was that there are some sins we can’t fully be forgiven for. For example, <a href="https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/132.39?lang=eng#p38">D&amp;C 132:39</a> teaches us that David lost his exaltation, and <a href="https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/132.19?lang=eng#p18">verse 19</a> and <a href="https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/132.27?lang=eng#p26">verse 27</a> teach us why: he deliberately, with premeditation, shed innocent blood after entering into his covenants. These verses seem to be the basis of this teaching of Blood Atonement.</p>
<p>As all-encompassing as the Atonement is, there’s a reason why people who have committed murder outside of military or law enforcement situations <a href="https://www.churchofjesuschrist.org/study/manual/general-handbook/38-church-policies-and-guidelines?lang=eng">need the First Presidency’s permission to be baptized</a>. There are some things, including murder after making our temple covenants, that can make us lose our exaltation. Because of that, the First Presidency needs to make sure that people in that situation fully understand the gravity of what they’ve done and that they really have <a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/mosiah/5.2?lang=eng&amp;clang=eng#p2">made that mighty change in their hearts</a>. If they were to enter into those covenants without having made that full repentance, and they did it again down the line, they’d be under worse condemnation than they would have been had they never been baptized or endowed at all.</p>
<p>So, taking all of that into consideration, <a href="https://www.fairlatterdaysaints.org/answers/Mormonism_and_doctrine/Repudiated_concepts/Blood_atonement">the idea behind Blood Atonement</a> is that making amends is an integral part of the repentance process. But when you murder someone, you can’t really make restitution for that because you can’t restore someone’s life to them after you take it away. So, in order to make as full of a restitution as you possibly could, you would offer up your own life in return and volunteer for death. This idea of voluntary restitution by shedding your own blood <a href="http://www.shields-research.org/General/blood_atonement.htm">was also taught to be only required in a complete theocracy</a>. This is <em>not</em> the death penalty, nor is it vigilante lynchings, the way you so often hear it portrayed as. This is the killer willingly giving up his life and having his blood spilled in return for spilling someone else’s, because he feels so bad for what he’s done, he knows he took something away which he can never give back, and because he fears for his own immortal soul. However, while it is not the death penalty <em>per se</em>, it could be construed as another form of capital punishment as the act of having his blood spilled should be enacted by the presiding legal authority so long as the execution is voluntary and requested by the killer. It’s not the result of a trial; it’s the result of a confession and a pleading for the execution to take place. But even so, it still has to be carried out by the proper legal authority, not by anyone else.</p>
<p>Obviously, this is a corrupted view of the doctrine that our Church actually teaches, and Christ shed His blood so that we wouldn’t have to. We can’t atone for our own sins, and we don’t need to because our Savior did it for us. All we can do is show Him the love, gratitude, and respect He deserves by doing our best and repenting whenever we fall short.</p>
<p>Most likely, <a href="https://www.fairlatterdaysaints.org/answers/Mormonism_and_doctrine/Repudiated_concepts/Blood_atonement#Question:_What_is_.22blood_atonement.22.3F">this was stated for effect</a>, to demonstrate how serious it was to break your covenants. We don’t live in a theocracy and are not under this commandment, so whether it might apply in a theocracy or not simply doesn’t matter, you know?</p>
<p>Of course, it’s a little tricky because we don’t know whether this quote from Brigham Young is word-for-word accurate or not. But as far as can be determined, just like with the Adam-God theory, this seems to be one of those times when Brigham let his own speculation run a little too far off course and started teaching something that was a personal theory rather than revealed doctrine. Or, as stated, equally likely it was one of those times when Brigham exaggerated something for effect to drive home the seriousness of the topic, which he was prone to do.</p>
<p>When you get right down to the brass tacks of it, <a href="https://www.fairlatterdaysaints.org/archive/publications/dead-men-tell-no-tales">it was a fairly benign teaching that was heavily twisted by outside forces</a> into something it was never meant to be. There were hyperbolic stories of marauding bands of Mormon vigilantes who were murdering their way across Utah to the point where the roads ran red with blood and apostates and innocents were disappearing left and right. If you asked them to provide proof, they never could. Some of this folklore stems from the Danites and some from the Mountain Meadows Massacre. (It doesn’t help that a prominent figure of both groups was the same man, which I’ll get to later.) Mostly, though, it was because our critics like to twist anything they can use against us. Unfortunately, the violent rhetoric gave them plenty of ammunition in this case.</p>
<p>These stories originate with <a href="https://www.fairlatterdaysaints.org/answers/Mormonism_and_persecution/Danites">the Danites</a>, another element in our history that took on a mythology and life of its own. The Danites had several names prior to settling on that one, including “<a href="https://www.jstor.org/stable/43042337">The Brothers of Gideon</a>” and, inexplicably, “<a href="https://byustudies.byu.edu/wp-content/uploads/2020/01/14.4GentryDanite.pdf">The Daughters of Zion</a>.”</p>
<p>Backing up a bit, in 1838 tensions in and around Far West, Missouri, were running high between the Saints and the locals <a href="https://en.wikipedia.org/wiki/1838_Mormon_War">in what would become known as the Missouri-Mormon War, or the 1838 Mormon War</a>. The situation had been escalating for years, though there was a cooling off period after <a href="https://en.wikipedia.org/wiki/Caldwell_County,_Missouri">Caldwell County was created specifically for Latter-day Saint settlement in 1836</a>. Far West, located in Caldwell County, was the main settlement of the Saints in Missouri.</p>
<p>The tension simmered for a few years, until it exploded in 1838. In 1837, the church in Kirtland fractured and many Saints flocked to Missouri, rapidly increasing the population and spilling out into neighboring counties. The local Missourians saw this as a violation of the compromise of giving them their own county. Because the Latter-day Saint population in some of those other counties grew so large it could sway elections, and because <a href="https://en.wikipedia.org/wiki/Missouri_Compromise">Missouri had long been the center of the slavery debate in the United States</a> by that time, the situation quickly grew deadly.</p>
<p>The Saints were also undergoing their own internal struggles at the time. The Missouri leaders had frequently ignored directions from Ohio and kind of did their own thing, which led to numerous rebukes in the Doctrine and Covenants and some sharply worded letters and visits from the Church leadership. Eventually, when the main body of the Church moved to Missouri, things came to a head and several prominent “dissenters”—Oliver Cowdery, David and John Whitmer, W.W. Phelps, Hiram Page, and others—were excommunicated. However, they did not go quietly. They’d bought up a bunch of land acting as agents for the Church and wanted to keep it as personal property, so they were threatening lawsuits.</p>
<p>That’s when Sidney Rigdon gave his infamous “Salt Sermon” and more than 80 well-known Saints (including Hyrum Smith) signed what came to be known as <a href="http://www.olivercowdery.com/smithhome/1838Sent.htm#pg06b">the Danite Manifesto</a>.</p>
<p>Full disclosure: one of my ancestors signed that document, and was listed among the officers of the Danite band by Reed Peck, a prominent former member of the faction. He was also a captain in the Missouri Militia and a major in the Armies of Israel Mormon Militia created to defend the Saints against the mobs. He even led one of the raiding parties we’ll talk about later. Beyond those few details, though, the extent of his involvement with the Danites isn’t known because he didn’t leave any records of it. He was a personal friend of Joseph’s, however, and he was not one of those members later excommunicated for participation in Danite activities, so I assume he was one of those deceived by Sampson Avard into believing that Joseph was the one secretly giving the orders.</p>
<p>Anyway, that manifesto was basically a letter telling the “dissenters” to get out of town, since Rigdon had declared that they were like salt that had lost its flavor and should be cast out and trodden under the feet of men. It was not exactly subtle and the men took them at their word. They fled Caldwell County and their stories fed into the anti-LDS sentiment brewing in the outside counties.</p>
<p>Two weeks later, Rigdon gave another speech, <a href="http://www.sidneyrigdon.com/rigd1838.htm">the Fourth of July address</a> I mentioned earlier. In that speech, he told the Missourians that the Saints would no longer sit passively by while their homes and property were destroyed, and that they would begin to fight back. Only, he used more extreme language than that:</p>
<blockquote><p><em>We take God and all the holy angels to witness this day, that we warn all men in the name of Jesus Christ, to come on us no more forever, for from this hour, we will bear it no more. Our rights shall no more be trampled on with impunity. <strong>The man or the set of men who attempts it does it at the expense of their lives. And that mob that comes on us to disturb us, it shall be between us and them a war of extermination, for we will follow them till the last drop of their blood is spilled, or else they will have to exterminate us: for we will carry the seat of war to their own houses, and their own families, and one party or the other shall be utterly destroyed.</strong> Remember it then </em>all men<em>.</em></p></blockquote>
<p>He followed it up by saying that the Saints would never be the aggressors, but obviously, this speech didn’t go over well with the Missourians. It caused such a stir that <a href="https://contentdm.lib.byu.edu/digital/collection/NCMP1820-1846/id/8317">Brigham later stated</a>, “Elder Rigdon was the prime cause of our troubles in Missouri, by his fourth of July ovation.”</p>
<p>About a month later, there was a big brawl in Gallatin County when some of the Missourians tried to stop some of the Mormons from voting. At the start of it, someone yelled out that it was a job for the Danites, several of whom must have been in attendance. They were able to drive back the mob long enough to escape mostly uninjured.</p>
<p>Other than the manifesto, that was the first public mention of the group.</p>
<p>Mob activity and other skirmishes escalated, and homes and property were burned. People were held prisoner and beaten. Outlying homes and settlements were primary targets. The Saints were forced out of De Witt in Carroll County after a measure was placed on the county ballot to expel them and the town was placed under siege. When Governor Boggs was begged to intervene, <a href="https://www.amazon.com/1838-Mormon-War-Missouri/dp/0826207294">his response was to let the Mormons and the mobs fight it out</a>. The Saints agreed to leave, and several women and children later died from the effects of exposure during the exodus.</p>
<p><a href="https://www.churchofjesuschrist.org/study/manual/gospel-topics-essays/peace-and-violence-among-19th-century-latter-day-saints?lang=eng">The Saints weren’t taking any of this lying down</a>, and formed the Armies of Israel militia to help protect the members from the mobs. <a href="https://www.fairlatterdaysaints.org/answers/Mormonism_and_persecution/Danites">The Danites were active at this time as well</a>, sort of an unofficial arm of the militia, carrying out raiding parties and inflicting property damage of their own. There was crossover between the two groups and many Danite members also belonged to the county militia.</p>
<p>Around this time a large group of 100+ men that included Joseph Smith also went around to the homes of various judges and sheriffs and other prominent citizens of Daviess County, ironically demanding that they sign affidavits saying they wouldn’t engage in mob activity against the Saints. Those men who were accosted later gave testimony stating they felt threatened and signed the affidavits because they were worried about what might happen to them if they didn’t.</p>
<p>On October 18<sup>th</sup>, some of the Caldwell County militia groups, along with aid from the Danites (and remember, there was some overlap between the two groups) formed raiding parties into Daviess County and burned homes and businesses and stole property. Lyman Wight led the group that attacked the town of Millport. David Patten led the group that attacked the town of Gallatin, and reports were that it was hit so badly, only a single shoe store remained untouched. And my ancestor, Seymour Brunson, led the group that attacked Grindstone Fork. Another smaller settlement, Splawn’s Ridge, was also sacked, but it’s unclear who led that raid. In a giant facepalm moment, the stolen goods from these towns ended up in the bishop’s storehouse in Adam-ondi-Ahman. It wasn’t just hostile Missourians who were attacked. Even those previously friendly to the Saints were not spared in these raids. Lyman Wight then led another group (or possibly the same one, it’s unclear) to go after outlying homes in the area. Altogether, a good 50 buildings were destroyed and approximately 100 families were left homeless from the attacks.</p>
<p>Many of the Saints were disturbed by these actions, as they should have been.</p>
<p>There is some evidence that Joseph knew and approved of the public actions and intentions of the Danites, but what was going on in secret was unknown even to him. Sampson Avard, the leader of the Danites, essentially turned it into a secret combination, <a href="http://www.lawenforcementservices.biz/law_enforcement_services,_llc/Church_History_files/The%20Danite%20Band%20of%201838.pdf">complete with secret gestures, signals, and phrases used to identify each other</a>, just like the Gadianton Robbers had. He told some of the members that Joseph was really the one calling the shots and giving the orders through him, but no evidence has ever been found to back up his claims. Joseph seemed as blindsided by the news of Avard’s deceit as everyone else when it finally came out, and after these raids, Joseph did publicly and privately speak out against them as a secret combination and an evil organization.</p>
<p>As can be expected, the retaliation was immediate.</p>
<p>On October 24<sup>th</sup> was what came to be known as the <a href="https://en.wikipedia.org/wiki/Battle_of_Crooked_River">Battle of Crooked River</a>. A segment of the Missouri militia was supposed to be patrolling the unincorporated strip between Caldwell and Ray Counties, but instead, the militia leader moved into Caldwell County, the home of the Saints, and started disarming them. The news reached Far West, and a rescue party went out to drive the militia back. It was an armed battle, and one Missouri militia member died and so did two of the Saints, including David Patten.</p>
<p>In revenge for the death of their friend, vigilante Missouri militiamen began attacking the Saints more heavily, and the leaders of the state militia started calling in for reinforcements to subdue the antagonists and keep the peace. At least one of those leaders, Alexander Doniphan, had proven himself a friend of the Saints in the past and was still on their side in the whole thing. But rumors that the entire militia segment involved at Crooked River had been slaughtered were flying around the state, and <a href="https://www.sos.mo.gov/cmsimages/archives/resources/findingaids/miscMormRecs/eo/18381027_ExtermOrder.pdf">Governor Boggs issued his infamous extermination order on October 27<sup>th</sup></a><sup>. </sup>On October 30<sup>th</sup> was the <a href="https://www.churchofjesuschrist.org/study/history/topics/hawns-mill-massacre?lang=eng">Haun’s Mill Massacre</a>. The <a href="https://www.churchofjesuschrist.org/study/history/topics/mormon-missouri-war-of-1838?lang=eng">siege at Far West began on October 31<sup>st</sup></a>.</p>
<p>Due to a betrayal by George Hinkle, Joseph and other leaders were arrested and the men at Far West were ordered to surrender their weapons. At the trial, <a href="https://www.jefflindsay.com/LDSFAQ/FQ_Danites.shtml">Sampson Avard took the stand as the prosecution’s chief witness and openly declared that Joseph was running the Danites</a> and all of the crimes they’d committed had been done on his express orders. Joseph, as mentioned earlier, was stunned. There’s not much other evidence showing that Joseph was involved with the inner workings of the Danites, and he seems to have only been aware of their public façade until this point.</p>
<p>The testimony circulated wildly, though, and in 19<sup>th</sup> Century folklore, <a href="https://www.youtube.com/watch?v=V9vMCc8rR1s">the Danites became this mythological group of “Avenging Angels of Mormonism,” Joseph’s own personal hit squad</a>. There were <a href="https://www.jstor.org/stable/43042337?read-now=1&amp;refreqid=excelsior%3A992a9a8fd0e35a5848683fdf5b834a06&amp;seq=1#page_scan_tab_contents">longstanding rumors and legends about this secretive group</a>, which included the idea that Porter Rockwell tried to murder Governor Boggs as part of a Danite oath to destroy anyone who threatened the Church, and those rumors carried on to Utah. The Danites were said to have been roaming the state, “blood atoning” anyone who got in their way.</p>
<p>So, regardless of the fact that there’s no evidence whatsoever that the two are linked in any way, that’s one of the reasons that Blood Atonement took off the way it did and why it led to so many exaggerated stories about Mormon Murder Squads and such.</p>
<p>The other thing we should touch on briefly—and it will be a much briefer treatment than the topic deserves—is the Mountain Meadows Massacre. This is a tragedy that deserves a much deeper dive, which I may do at some point. For now, though, I’m just going to cover the basics and encourage you all to read <a href="https://mountainmeadowsmassacre.com/massacre"><em>Massacre at Mountain Meadows</em></a> by Ronald Walker, Richard Turley Jr., and Glen Leonard. It’s the best book on the subject to date. Much of the information I’m about to share came from that book and <a href="https://www.churchofjesuschrist.org/study/ensign/2007/09/the-mountain-meadows-massacre?lang=eng">from this article announcing the book</a>.</p>
<p>If you read through any of the sources I linked above, you may have recognized the name of the man who described the secret oaths and gestures of the Danites, John D. Lee. Lee is one of the more notorious figures in Latter-day Saint history, and in large part, that stems from his involvement in this horrifying tragedy.</p>
<p>So, to set the scene, it was September of 1857. It was ten years after the Saints had settled the Utah Territory, Brigham Young was both prophet and governor, beloved Apostle <a href="https://en.wikipedia.org/wiki/Parley_P._Pratt#Death_and_legacy">Parley P. Pratt had been murdered in Arkansas</a> in May (which will come into play later), and in July President James Buchanan had sent a company of 1500 soldiers to start marching across the plains to Utah to remove Brigham as governor and install a non-Latter-day Saint in the position in what would eventually become known as <a href="https://en.wikipedia.org/wiki/Utah_War">the Utah War</a>. The Saints were terrified by the news, believing that a full-scale war was coming that would lead them to be hunted down and killed or forced to flee their homes yet again. In order to prepare for that possibility, Brigham and the rest of the Quorum of the Twelve began trying to make alliances with the local Native American tribes against the invading army. They also started issuing orders to the Saints to stockpile their grain, cattle, and ammunition and to start hiding it in caches in the mountains, rather than selling to the wagon trains who were coming through the area on their way to California.</p>
<p>However, over the past decade, Utah had become a waystation for the wagon trains crossing the plains, and many would only carry enough supplies to get them to Utah, where they could then restock their supplies for the final leg of the journey to California or Oregon. The Saints refusing to sell to the wagon trains would leave many of them ill-equipped to make it to their final destinations.</p>
<p>The Baker-Fancher train was one such company making its way through Utah that September, and finding the locals wary and unwilling to sell them food or other supplies. Because their own supplies were dwindling, this caused immediate tension with the train, which was from Arkansas—a state sharing a border with Missouri and the place where Parley Pratt was murdered.</p>
<p>Another thing that caused some issues was that the cattle in the train had a bovine sickness that caused some of them to die and the bodies were left behind, sometimes inside the town limits. Locals were infected due to handling the carcasses with open wounds on their hands or possibly due to eating the contaminated meat. Because they then became seriously ill, rumors began to spread that the wagon train was poisoning the cattle or the well-water deliberately to infect the locals.</p>
<p>As they reached Cedar City, the last city where they could restock before heading to California, things took a major turn for the worse. In their bitterness at being denied or badly overcharged for their supplies, some members of the wagon company bragged about taking part in the persecutions against the Saints a few decades prior, with one even claiming to have one of the guns that murdered Joseph Smith. Some threatened to join the army in helping to annihilate the Saints. Isaac Haight, in order to drum up support for his actions taken against the company, also later spread rumors that some of them had participated in the Haun’s Mill Massacre and in the murder of Parley Pratt, so all of that was swirling around as the company departed Cedar City.</p>
<p>Anyway, Alexander Fancher, the company’s leader, rebuked the company members for making those comments, and they took their leave. The people believed them, though, and the town marshal tried to arrest them, but was forced to let them go because he was outnumbered. The city leaders, including the mayor/militia major/stake president in the Church Isaac Haight, decided to call out the militia to go after the train and arrest them and fine them some cattle. Haight asked the local militia leader to do it, who declined to get involved unless the angry words turned to violence.</p>
<p>So, since the militia wouldn’t help, it’d stand to reason that they’d just let the wagon train go on their way, right? Wrong. Instead, the city leaders decided they’d have to take matters into their own hands and get the local Paiute tribe to kill a few of them and steal their cattle, giving some to the townspeople for helping arrange the whole thing.</p>
<p>They planned the attack for halfway between Cedar City and St. George, in Santa Clara Canyon. They chose that spot because it was secluded and because it fell under the jurisdiction of a different militia, this one led by Major John D. Lee. Lee was also a federal Indian Agent who was on good terms with the Paiutes and was assigned to help teach them how to run large farms of their own, with advanced tools and farming methods.</p>
<p>In a late-night planning meeting with Haight, Lee admitted that he believed the Paiutes would kill the entire train instead of just a few of the men. Haight agreed, so they plotted how best to blame the Paiutes for the entire thing and hide their own involvement. I’m telling you, Lee did love himself a good secret combination. It’s insane to me that at no point did any of them say, “Hey, you know what? They’re gone, let’s just let it go.”</p>
<p>The Paiutes weren’t initially interested, because that wasn’t really their style. They didn’t make large attacks on equally large wagon companies. They usually just picked off a few cattle here and there. So, the city leaders convinced them that the train was working with the approaching army and would help slaughter the Paiutes as well as the Mormons.</p>
<p>Once they finally agreed, Haight then presented his plan to a council formed of local Church, city, and militia leaders, who were shocked and appalled at what they were hearing. One of them finally asked him to send an express rider to Salt Lake to get Brigham Young’s take on the situation, since he was the governor and the leader of the Church.</p>
<p>Haight agreed and did so in a highly misleading retelling of the events and the plan, but the very next day, September 7<sup>th</sup>, Lee, some militia men under his command, and the Paiutes made an initial attack, not waiting for Young’s advice or even for the wagon train to reach Santa Clara Canyon. Instead, they attacked at Mountain Meadows. It didn’t go as planned, with the wagon train managing to fight them off and circle the wagons. It resulted in a five-day siege. There were a few more attacks, but only a few of the wagon train had died by that point. Two men were caught sneaking away from the train to get help by some militia members, who killed one but allowed the other to escape with the news that their attackers were not just Native Americans, but also white Mormon militia men. If the train was to leave, they’d share the news that it was the Saints who had attacked them, and the approaching army would retaliate hard against them for it.</p>
<p>On September 9<sup>th</sup>, Haight went back to his own militia leader to ask for help, and that leader, William Dame, held a council which decided they should go to the aid of the wagon train and help them escape the situation. Afterward, Haight and a colleague pulled Dame aside and told him the truth, and got him to cave in against sending the militia to help the wagon train. Instead, Haight left feeling like he’d been given permission to bring the militia along to finish them off.</p>
<p>On September 11<sup>th</sup>, with the militia gathered, Lee raised a white flag and went to the train, telling them that the militia would help them talk down the Native Americans and get them back to town safely, if they’d just disarm themselves. The train members were suspicious, since they knew that white men had been helping the Paiutes, but didn’t have a choice because they were low on supplies and ammunition and some of them badly needed medical attention, so they agreed. After the surrender, all but the children under the age of six or seven where murdered. I’ll spare the details of the attack, but it was horrific and resulted in the death of approximately 120 people.</p>
<p>Brigham Young’s response arrived two days later, telling them to let the wagon train leave in peace and to remember that God would protect them against their enemies.</p>
<p>Brigham and the other leaders learned of the massacre, but didn’t learn of the extent of the involvement of the Saints until much later. That coverup and the intention to blame it entirely on the Paiutes was in full swing. But in 1859, two years later, everyone who was involved in the planning of the attack was released from their callings, and in 1870, as more information came to light, Haight and Lee were excommunicated. Many of the militia men involved believed they were acting on Brigham’s orders, as that’s what they’d been told, so they were treated more lightly for their roles. Nine indictments were handed down, with many of them being arrested, but only Lee was tried and executed for his crimes.</p>
<p>When he was killed, <a href="https://en.wikipedia.org/wiki/John_D._Lee">Lee’s demeanor and quotes</a>, as well as <a href="https://www.amazon.com/Mormonism-Unveiled-John-D-Lee/dp/1117993116/">his book</a>, led many to believe this execution was an example of Blood Atonement, and again, the stories took off. Even today, those twisted stories still get tossed around. There was a movie made about it in 2007 starring Jon Voight as Brigham Young called <em>September Dawn</em>, painting Young as the instigator and chief conspirator of the entire thing. It’s all absurd, but it all ties back to Blood Atonement and the very twisted mythology surrounding it, rather than any of the actual words or concepts.</p>
<p>Anyway, Jeremy finishes off his Blood Atonement section with this:</p>
<p><strong><em>UPDATE: The Church now confirms in its </em></strong><strong>Peace and Violence among the 19<sup>th</sup>-Century Latter-day Saints<em> essay that Blood Atonement was taught by the prophet Brigham Young.</em></strong></p>
<p>Yes. As with all of these “now confirms” items, the Church never denied that. This was hardly the first time it was mentioned. Anybody reading the <em>Journal of Discourses</em> would have known that. It was never focused on because it was never formalized, official doctrine, but the teachings were out there and were being addressed repeatedly.</p>
<p><strong><em>As with the Adam-God Theory, the Blood Atonement doctrine was later declared false by subsequent prophets and apostles.</em></strong></p>
<p>Yep. Because it was exaggerated rhetoric to make a point, that likely included some personal speculation gone too far. But it was never doctrine, and it was always taught as something speculative that might exist in a full theocracy, but that did not apply to the Saints at the time or today.</p>
<p>And a repeat of his favorite closing line:</p>
<p><strong><em>Yesterday’s doctrine is today’s false doctrine. Yesterday’s prophet is today’s heretic.</em></strong></p>
<p>Nope. Again, not doctrine, and again, deliberately exaggerated speeches do not make someone a heretic. Certainly, nobody ever labeled Brigham Young as such except for Jeremy. It was a preaching style, and Brigham was not telling us to go out and murder apostates. He was saying that apostatizing from the Church after making temple covenants was a grievously serious sin, and there may be no full repentance for that in the next life if you don’t make amends while you still can in this one.</p>
<p>***</p>
<p>Sources in this entry:</p>
<p><a href="https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/132.39?lang=eng#p38">https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/132.39?lang=eng#p38</a></p>
<p><a href="https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/132.19?lang=eng#p18">https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/132.19?lang=eng#p18</a></p>
<p><a href="https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/132.27?lang=eng#p26">https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/132.27?lang=eng#p26</a></p>
<p><a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/mosiah/5.2?lang=eng&amp;clang=eng#p2">https://www.churchofjesuschrist.org/study/scriptures/bofm/mosiah/5.2?lang=eng&amp;clang=eng#p2</a></p>
<p><a href="https://en.wikipedia.org/wiki/Fire_and_brimstone">https://en.wikipedia.org/wiki/Fire_and_brimstone</a></p>
<p><a href="https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1053&amp;context=etas">https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1053&amp;context=etas</a></p>
<p><a href="https://www.youtube.com/watch?v=poMERlofOcM">https://www.youtube.com/watch?v=poMERlofOcM</a></p>
<p><a href="http://www.sidneyrigdon.com/rigd1838.htm">http://www.sidneyrigdon.com/rigd1838.htm</a></p>
<p><a href="https://en.wikipedia.org/wiki/Salt_Sermon">https://en.wikipedia.org/wiki/Salt_Sermon</a></p>
<p><a href="http://www.olivercowdery.com/smithhome/1838Sent.htm#pg06b">http://www.olivercowdery.com/smithhome/1838Sent.htm#pg06b</a></p>
<p><a href="https://byustudies.byu.edu/article/the-prophets-have-spoken-but-what-did-they-say-examining-the-differences-between-george-d-watts-original-shorthand-notes-and-the-sermons-published-in-the-journal-of-discourses/?post_type=article&amp;p=8081">https://byustudies.byu.edu/article/the-prophets-have-spoken-but-what-did-they-say-examining-the-differences-between-george-d-watts-original-shorthand-notes-and-the-sermons-published-in-the-journal-of-discourses/?post_type=article&amp;p=8081</a></p>
<p><a href="https://catalog.churchofjesuschrist.org/record/5df3b7da-d0a5-437b-8268-7dde8a87c76e/ec1c0cde-2383-437c-b325-84314950c287?view=browse">https://catalog.churchofjesuschrist.org/record/5df3b7da-d0a5-437b-8268-7dde8a87c76e/ec1c0cde-2383-437c-b325-84314950c287?view=browse</a></p>
<p><a href="https://www.churchofjesuschrist.org/study/manual/general-handbook/38-church-policies-and-guidelines?lang=eng">https://www.churchofjesuschrist.org/study/manual/general-handbook/38-church-policies-and-guidelines?lang=eng</a></p>
<p><a href="https://www.fairlatterdaysaints.org/answers/Mormonism_and_doctrine/Repudiated_concepts/Blood_atonement">https://www.fairlatterdaysaints.org/answers/Mormonism_and_doctrine/Repudiated_concepts/Blood_atonement</a></p>
<p><a href="https://sunstonemagazine.com/wp-content/uploads/sbi/articles/039-04-09.pdf">https://sunstonemagazine.com/wp-content/uploads/sbi/articles/039-04-09.pdf</a></p>
<p><a href="http://www.shields-research.org/General/blood_atonement.htm">http://www.shields-research.org/General/blood_atonement.htm</a></p>
<p><a href="https://www.fairlatterdaysaints.org/answers/Mormonism_and_doctrine/Repudiated_concepts/Blood_atonement#Question:_What_is_.22blood_atonement.22.3F">https://www.fairlatterdaysaints.org/answers/Mormonism_and_doctrine/Repudiated_concepts/Blood_atonement#Question:_What_is_.22blood_atonement.22.3F</a></p>
<p><a href="https://www.fairlatterdaysaints.org/archive/publications/dead-men-tell-no-tales">https://www.fairlatterdaysaints.org/archive/publications/dead-men-tell-no-tales</a></p>
<p><a href="https://www.fairlatterdaysaints.org/answers/Mormonism_and_persecution/Danites">https://www.fairlatterdaysaints.org/answers/Mormonism_and_persecution/Danites</a></p>
<p><a href="https://en.wikipedia.org/wiki/1838_Mormon_War">https://en.wikipedia.org/wiki/1838_Mormon_War</a></p>
<p><a href="https://en.wikipedia.org/wiki/Caldwell_County,_Missouri">https://en.wikipedia.org/wiki/Caldwell_County,_Missouri</a></p>
<p><a href="https://en.wikipedia.org/wiki/Missouri_Compromise">https://en.wikipedia.org/wiki/Missouri_Compromise</a></p>
<p><a href="http://www.olivercowdery.com/smithhome/1838Sent.htm#pg06b">http://www.olivercowdery.com/smithhome/1838Sent.htm#pg06b</a></p>
<p><a href="https://www.jstor.org/stable/43042337">https://www.jstor.org/stable/43042337</a></p>
<p><a href="https://byustudies.byu.edu/wp-content/uploads/2020/01/14.4GentryDanite.pdf">https://byustudies.byu.edu/wp-content/uploads/2020/01/14.4GentryDanite.pdf</a></p>
<p><a href="https://contentdm.lib.byu.edu/digital/collection/NCMP1820-1846/id/8317">https://contentdm.lib.byu.edu/digital/collection/NCMP1820-1846/id/8317</a></p>
<p><a href="https://www.amazon.com/1838-Mormon-War-Missouri/dp/0826207294">https://www.amazon.com/1838-Mormon-War-Missouri/dp/0826207294</a></p>
<p><a href="https://www.churchofjesuschrist.org/study/manual/gospel-topics-essays/peace-and-violence-among-19th-century-latter-day-saints?lang=eng">https://www.churchofjesuschrist.org/study/manual/gospel-topics-essays/peace-and-violence-among-19th-century-latter-day-saints?lang=eng</a></p>
<p><a href="http://www.lawenforcementservices.biz/law_enforcement_services,_llc/Church_History_files/The%20Danite%20Band%20of%201838.pdf">http://www.lawenforcementservices.biz/law_enforcement_services,_llc/Church_History_files/The%20Danite%20Band%20of%201838.pdf</a></p>
<p><a href="https://en.wikipedia.org/wiki/Battle_of_Crooked_River">https://en.wikipedia.org/wiki/Battle_of_Crooked_River</a></p>
<p><a href="https://www.sos.mo.gov/cmsimages/archives/resources/findingaids/miscMormRecs/eo/18381027_ExtermOrder.pdf">https://www.sos.mo.gov/cmsimages/archives/resources/findingaids/miscMormRecs/eo/18381027_ExtermOrder.pdf</a></p>
<p><a href="https://www.churchofjesuschrist.org/study/history/topics/hawns-mill-massacre?lang=eng">https://www.churchofjesuschrist.org/study/history/topics/hawns-mill-massacre?lang=eng</a></p>
<p><a href="https://www.churchofjesuschrist.org/study/history/topics/mormon-missouri-war-of-1838?lang=eng">https://wwwchurchofjesuschrist.org/study/history/topics/mormon-missouri-war-of-1838?lang=eng</a></p>
<p><a href="https://www.youtube.com/watch?v=V9vMCc8rR1s">https://www.youtube.com/watch?v=V9vMCc8rR1s</a></p>
<p><a href="https://www.jstor.org/stable/43042337?read-now=1&amp;refreqid=excelsior%3A992a9a8fd0e35a5848683fdf5b834a06&amp;seq=1#page_scan_tab_contents">https://www.jstor.org/stable/43042337?read-now=1&amp;refreqid=excelsior%3A992a9a8fd0e35a5848683fdf5b834a06&amp;seq=1#page_scan_tab_contents</a></p>
<p><a href="https://www.fairlatterdaysaints.org/answers/Mormonism_and_persecution/Danites">https://www.fairlatterdaysaints.org/answers/Mormonism_and_persecution/Danites</a></p>
<p><a href="https://www.jefflindsay.com/LDSFAQ/FQ_Danites.shtml">https://www.jefflindsay.com/LDSFAQ/FQ_Danites.shtml</a></p>
<p><a href="https://en.wikipedia.org/wiki/Utah_War">https://en.wikipedia.org/wiki/Utah_War</a></p>
<p><a href="https://en.wikipedia.org/wiki/Parley_P._Pratt#Death_and_legacy">https://en.wikipedia.org/wiki/Parley_P._Pratt#Death_and_legacy</a></p>
<p><a href="https://www.churchofjesuschrist.org/study/ensign/2007/09/the-mountain-meadows-massacre?lang=eng">https://www.churchofjesuschrist.org/study/ensign/2007/09/the-mountain-meadows-massacre?lang=eng</a></p>
<p><a href="https://en.wikipedia.org/wiki/John_D._Lee">https://en.wikipedia.org/wiki/John_D._Lee</a></p>
<p><a href="https://www.amazon.com/Mormonism-Unveiled-John-D-Lee/dp/1117993116/">https://www.amazon.com/Mormonism-Unveiled-John-D-Lee/dp/1117993116/</a></p>
<p>&nbsp;</p>
<p><a href="https://www.fairlatterdaysaints.org/wp-content/uploads/2021/08/me-1.png" rel="noopener" data-saferedirecturl="https://www.google.com/url?q=https://www.fairlatterdaysaints.org/wp-content/uploads/2021/08/me-1.png&amp;source=gmail&amp;ust=1635370480825000&amp;usg=AFQjCNEOxDxaayAteShDgl3XYA2rBjhC-Q"><img decoding="async" class="alignleft" src="https://ci6.googleusercontent.com/proxy/Mbq6sHeBf0Gv9-j8ncMb5qQsswLfb9RfWICZo8FjyWUsF6PcxzlK6AInZrcOz7MOTAXan___-tG31EbsY3LK66zLGc8EKJ3vr45SueVkkv92lASa79Uir8ks0RTA43kT-g4=s0-d-e1-ft#https://www.fairlatterdaysaints.org/wp-content/uploads/2021/08/me-1-150x150.png" alt="" width="150" height="150" /></a>Sarah Allen is brand new in her affiliation with FAIR. By profession, she works in mortgage compliance and is a freelance copyeditor. A voracious reader, she loves studying the Gospel and the history of the restored Church. After watching some of her lose their testimonies, she became interested in helping others through their faith crises and began sharing what she learned through her studies. She’s grateful to those at FAIR who have given her the opportunity to share her testimony with a wider audience.</p>
</div><footer class="entry-footer"><p class="entry-meta"><span class="entry-categories">Filed Under: <a href="https://www.fairlatterdaysaints.org/blog/category/anti-mormon-critics" rel="category tag">Anti-Mormon critics</a>, <a href="https://www.fairlatterdaysaints.org/blog/category/apologetics" rel="category tag">Apologetics</a>, <a href="https://www.fairlatterdaysaints.org/blog/category/ces-letter" rel="category tag">CES Letter</a>, <a href="https://www.fairlatterdaysaints.org/blog/category/faith-crisis" rel="category tag">Faith Crisis</a>, <a href="https://www.fairlatterdaysaints.org/blog/category/lds-history" rel="category tag">LDS History</a></span> </p></footer></article></main><aside class="sidebar sidebar-primary widget-area" role="complementary" aria-label="Primary Sidebar" id="genesis-sidebar-primary"><h2 class="genesis-sidebar-title screen-reader-text">Primary Sidebar</h2><section id="text-4" class="widget widget_text"><div class="widget-wrap"><h3 class="widgettitle widget-title">Subscribe to Blog</h3>
			<div class="textwidget"><style>@import url('https://fonts.googleapis.com/css?family=Montserrat:700');@import url('https://fonts.googleapis.com/css?family=Montserrat:400');
.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .form-preview {
  display: flex !important;
  flex-direction: column !important;
  justify-content: center !important;
  margin-top: 30px !important;
  padding: clamp(17px, 5%, 40px) clamp(17px, 7%, 50px) !important;
  max-width: none !important;
  border-radius: 6px !important;
}
.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .form-preview,
.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .form-preview *{
  box-sizing: border-box !important;
}
.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .form-preview .preview-heading {
  width: 100% !important;
}
.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .form-preview .preview-heading h5{
  margin-top: 0 !important;
  margin-bottom: 0 !important;
}
.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .form-preview .preview-input-field {
  margin-top: 20px !important;
  width: 100% !important;
}
.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .form-preview .preview-input-field input {
  width: 100% !important;
  height: 40px !important;
  border-radius: 6px !important;
  border: 2px solid #e9e8e8 !important;
  background-color: #fff !important;
  outline: none !important;
}
.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .form-preview .preview-input-field input {
  color: #000000 !important;
  font-family: "Montserrat" !important;
  font-size: 14px !important;
  font-weight: 400 !important;
  line-height: 20px !important;
  text-align: center !important;
}
.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .form-preview .preview-input-field input::placeholder {
  color: #000000 !important;
  opacity: 1 !important;
}

.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .form-preview .preview-input-field input:-ms-input-placeholder {
  color: #000000 !important;
}

.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .form-preview .preview-input-field input::-ms-input-placeholder {
  color: #000000 !important;
}
.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .form-preview .preview-submit-button {
  margin-top: 10px !important;
  width: 100% !important;
}
.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .form-preview .preview-submit-button button {
  width: 100% !important;
  height: 40px !important;
  border: 0 !important;
  border-radius: 6px !important;
  line-height: 0px !important;
}
.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .form-preview .preview-submit-button button:hover {
  cursor: pointer !important;
}
.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .powered-by-line {
  color: #231f20 !important;
  font-family: "Montserrat" !important;
  font-size: 13px !important;
  font-weight: 400 !important;
  line-height: 25px !important;
  text-align: center !important;
  text-decoration: none !important;
  display: flex !important;
  width: 100% !important;
  justify-content: center !important;
  align-items: center !important;
  margin-top: 10px !important;
}
.followit--follow-form-container[attr-a][attr-b][attr-c][attr-d][attr-e][attr-f] .powered-by-line img {
  margin-left: 10px !important;
  height: 1.13em !important;
  max-height: 1.13em !important;
}
</style><div class="followit--follow-form-container" attr-a attr-b attr-c attr-d attr-e attr-f><form data-v-2f850a8c="" action="https://api.follow.it/subscription-form/bDFmNnh6UENzQ1o2SnpGT1FNWjg2ZHlzZUtURWttTTA2QndJK3BCVDJUVHkxdVAxVFhISU90NFNRVWQ5cHc1cjRVYk5GNWtZTjVFWGlaUTlDemJaSFBuSks0TVFyZFQxUDRQRDdPZ3pSR0g4WlpYUnowSG9WZmJIMXVucURsVXh8dXkzOWtGblE5aS8zZFA3RGVUU3RGRjI5L3VQT2ZaU1VjNW5zV0xiYmVEND0=/8" method="post"><div data-v-2f850a8c="" class="form-preview" style="background-color: rgb(255, 255, 255); border-style: solid; border-width: 1px; border-color: rgb(204, 204, 204); position: relative;"><div data-v-2f850a8c="" class="preview-heading"><h5 data-v-2f850a8c="" style="text-transform: none !important; font-family: Montserrat; font-weight: bold; color: rgb(0, 0, 0); font-size: 16px; text-align: center;">
                  Enter your email address:
                </h5></div> <div data-v-2f850a8c="" class="preview-input-field"><input data-v-2f850a8c="" type="email" name="email" required="required" placeholder="" spellcheck="false" style="text-transform: none !important; font-family: Montserrat; font-weight: normal; color: rgb(0, 0, 0); font-size: 14px; text-align: center; background-color: rgb(255, 255, 255);"></div> <div data-v-2f850a8c="" class="preview-submit-button"><button data-v-2f850a8c="" type="submit" style="text-transform: none !important; font-family: Montserrat; font-weight: bold; color: rgb(255, 255, 255); font-size: 16px; text-align: center; background-color: rgb(0, 0, 0);">
                  Subscribe
                </button></div></div></form></div></div>
		</div></section>
<section id="text-5" class="widget widget_text"><div class="widget-wrap"><h3 class="widgettitle widget-title">Subscribe to Podcast</h3>
			<div class="textwidget"><a href="https://www.fairlatterdaysaints.org/feed/podcast/"><img src="https://www.fairlatterdaysaints.org/wp-content/uploads/podcast.jpg" alt="Podcast icon" width="61px" height="62px" /></a>
<br/>
<a href="http://itunes.apple.com/us/podcast/mormon-fair-cast/id397315546">Subscribe to podcast in iTunes</a>
<br>
<a href="https://www.fairlatterdaysaints.org/feed/podcast/">Subscribe to podcast elsewhere</a>
<br>
Listen with FAIR app<br>
<a href="https://play.google.com/store/apps/details?id=com.andromo.dev133584.app131088"><img class="" src="https://play.google.com/intl/en_us/badges/images/apps/en-play-badge-border.png" alt="Android app on Google Play" width="189" height="71" /></a>
<a href="https://apps.apple.com/us/app/faithful-answers/id6470235837?itsct=apps_box_badge&amp;itscg=30200" style="display: inline-block; overflow: hidden; border-radius: 13px; width: 189px; height: 71px;"><img src="https://tools.applemediaservices.com/api/badges/download-on-the-app-store/black/en-us?size=250x83&amp;releaseDate=1700352000" alt="Download on the App Store" style="border-radius: 13px; width: 189px; height: 71px;"></a>
</div>
		</div></section>
<section id="nav_menu-5" class="widget widget_nav_menu"><div class="widget-wrap"><h3 class="widgettitle widget-title">Pages</h3>
<div class="menu-blog-sidebar-container"><ul id="menu-blog-sidebar" class="menu"><li id="menu-item-16893" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-16893"><a href="https://www.fairlatterdaysaints.org/blog-guidelines">Blog Guidelines</a></li>
</ul></div></div></section>

		<section id="recent-posts-3" class="widget widget_recent_entries"><div class="widget-wrap">
		<h3 class="widgettitle widget-title">FAIR Latest</h3>

		<ul>
											<li>
					<a href="https://www.fairlatterdaysaints.org/blog/2023/11/26/have-you-tried-our-faithful-answers-app">Have you tried our Faithful Answers app?</a>
									</li>
											<li>
					<a href="https://www.fairlatterdaysaints.org/blog/2023/11/22/how-one-womans-scholarship-helps-us-better-understand-church-history">How One Woman’s Scholarship Helps Us Better Understand Church History</a>
									</li>
											<li>
					<a href="https://www.fairlatterdaysaints.org/blog/2023/11/22/letter-for-my-wife-rebuttal-part-24-blood-atonement">Letter For My Wife Rebuttal, Part 24: Blood Atonement</a>
									</li>
											<li>
					<a href="https://www.fairlatterdaysaints.org/blog/2023/11/20/come-follow-me-with-fair-faithful-answers-to-new-testament-questions-1-and-2-peter">Come, Follow Me with FAIR: Faithful Answers to New Testament Questions – 1 and 2 Peter</a>
									</li>
											<li>
					<a href="https://www.fairlatterdaysaints.org/blog/2023/11/13/come-follow-me-with-fair-faithful-answers-to-new-testament-questions-james">Come, Follow Me with FAIR: Faithful Answers to New Testament Questions – James</a>
									</li>
					</ul>

		</div></section>
<section id="categories-3" class="widget widget_categories"><div class="widget-wrap"><h3 class="widgettitle widget-title">Blog Categories</h3>
<form action="https://www.fairlatterdaysaints.org" method="get"><label class="screen-reader-text" for="cat">Blog Categories</label><select  name='cat' id='cat' class='postform'>
	<option value='-1'>Select Category</option>
	<option class="level-0" value="1152">Abuse&nbsp;&nbsp;(3)</option>
	<option class="level-0" value="40">Administrative notices&nbsp;&nbsp;(19)</option>
	<option class="level-0" value="1136">Amber Rothamer&nbsp;&nbsp;(2)</option>
	<option class="level-0" value="41">Anti-Mormon critics&nbsp;&nbsp;(303)</option>
	<option class="level-0" value="42">Apologetics&nbsp;&nbsp;(397)</option>
	<option class="level-0" value="888">Apostasy&nbsp;&nbsp;(35)</option>
	<option class="level-0" value="889">Archaeology&nbsp;&nbsp;(9)</option>
	<option class="level-0" value="90">Articles of Faith&nbsp;&nbsp;(34)</option>
	<option class="level-0" value="43">Atheism&nbsp;&nbsp;(15)</option>
	<option class="level-0" value="91">Best of Fair&nbsp;&nbsp;(5)</option>
	<option class="level-0" value="44">Bible&nbsp;&nbsp;(217)</option>
	<option class="level-0" value="92">Book of Abraham&nbsp;&nbsp;(69)</option>
	<option class="level-0" value="45">Book of Mormon&nbsp;&nbsp;(355)</option>
	<option class="level-0" value="93">Book of Moses&nbsp;&nbsp;(48)</option>
	<option class="level-0" value="46">Book reviews&nbsp;&nbsp;(90)</option>
	<option class="level-0" value="1150">By Study and Faith&nbsp;&nbsp;(9)</option>
	<option class="level-0" value="1132">CES Letter&nbsp;&nbsp;(70)</option>
	<option class="level-0" value="47">Chastity&nbsp;&nbsp;(24)</option>
	<option class="level-0" value="1122">Come Follow Me&nbsp;&nbsp;(156)</option>
	<option class="level-0" value="1139">Come Follow Me&nbsp;&nbsp;(2)</option>
	<option class="level-0" value="1141">Come Follow Me with FAIR&nbsp;&nbsp;(46)</option>
	<option class="level-0" value="48">Conversion&nbsp;&nbsp;(74)</option>
	<option class="level-0" value="1145">Cornerstone: A FAIR Temple Preparation Podcast&nbsp;&nbsp;(5)</option>
	<option class="level-0" value="49">Dead Sea Scrolls&nbsp;&nbsp;(6)</option>
	<option class="level-0" value="50">DNA&nbsp;&nbsp;(15)</option>
	<option class="level-0" value="51">Doctrine&nbsp;&nbsp;(168)</option>
	<option class="level-0" value="1125">Doctrine and Covenants&nbsp;&nbsp;(80)</option>
	<option class="level-0" value="52">Early Christianity&nbsp;&nbsp;(51)</option>
	<option class="level-0" value="53">Evidences&nbsp;&nbsp;(154)</option>
	<option class="level-0" value="1133">FAIR Conference&nbsp;&nbsp;(20)</option>
	<option class="level-0" value="54">FAIR Conference&nbsp;&nbsp;(167)</option>
	<option class="level-0" value="94">Fair Issues&nbsp;&nbsp;(26)</option>
	<option class="level-0" value="95">Fair Mormon Front Page News Review&nbsp;&nbsp;(11)</option>
	<option class="level-0" value="1121">FAIR Voice&nbsp;&nbsp;(28)</option>
	<option class="level-0" value="748">FairMormon Conference&nbsp;&nbsp;(66)</option>
	<option class="level-0" value="55">FairMormon Papers and Reviews&nbsp;&nbsp;(1)</option>
	<option class="level-0" value="96">Faith and Reason&nbsp;&nbsp;(33)</option>
	<option class="level-0" value="56">Faith Crisis&nbsp;&nbsp;(239)</option>
	<option class="level-0" value="1135">Faithfully Informed&nbsp;&nbsp;(2)</option>
	<option class="level-0" value="1146">Finances&nbsp;&nbsp;(1)</option>
	<option class="level-0" value="57">First Vision&nbsp;&nbsp;(28)</option>
	<option class="level-0" value="58">Gender Issues&nbsp;&nbsp;(29)</option>
	<option class="level-0" value="59">General&nbsp;&nbsp;(128)</option>
	<option class="level-0" value="60">General Conference&nbsp;&nbsp;(39)</option>
	<option class="level-0" value="61">Geography&nbsp;&nbsp;(47)</option>
	<option class="level-0" value="97">Gospel Doctrine: D&amp;C&nbsp;&nbsp;(62)</option>
	<option class="level-0" value="1120">Hanna Seariac&nbsp;&nbsp;(31)</option>
	<option class="level-0" value="62">Homosexuality&nbsp;&nbsp;(50)</option>
	<option class="level-0" value="98">Hosts&nbsp;&nbsp;(142)</option>
	<option class="level-0" value="1128">Hugh Nibley Observed&nbsp;&nbsp;(11)</option>
	<option class="level-0" value="63">Interfaith Dialogue&nbsp;&nbsp;(53)</option>
	<option class="level-0" value="1144">Jacob Crapo&nbsp;&nbsp;(5)</option>
	<option class="level-0" value="1140">Jennifer Roach&nbsp;&nbsp;(46)</option>
	<option class="level-0" value="1127">Jesus Christ&nbsp;&nbsp;(125)</option>
	<option class="level-0" value="64">Joseph Smith&nbsp;&nbsp;(293)</option>
	<option class="level-0" value="99">Julianne Dehlin Hatton&nbsp;&nbsp;(32)</option>
	<option class="level-0" value="1131">Languages&nbsp;&nbsp;(5)</option>
	<option class="level-0" value="747">Latter-day Saint Scholars Testify&nbsp;&nbsp;(2)</option>
	<option class="level-0" value="65">LDS Culture&nbsp;&nbsp;(66)</option>
	<option class="level-0" value="66">LDS History&nbsp;&nbsp;(327)</option>
	<option class="level-0" value="67">LDS Scriptures&nbsp;&nbsp;(81)</option>
	<option class="level-0" value="68">Lesson Aids&nbsp;&nbsp;(82)</option>
	<option class="level-0" value="69">Marriage&nbsp;&nbsp;(44)</option>
	<option class="level-0" value="70">Masonry&nbsp;&nbsp;(24)</option>
	<option class="level-0" value="5">Media&nbsp;&nbsp;(12)</option>
	<option class="level-0" value="1117">Mental Health&nbsp;&nbsp;(12)</option>
	<option class="level-0" value="71">Michael R. Ash&nbsp;&nbsp;(70)</option>
	<option class="level-0" value="1091">Missionary Work&#8217;&nbsp;&nbsp;(12)</option>
	<option class="level-0" value="72">Mormon Defense League&nbsp;&nbsp;(2)</option>
	<option class="level-0" value="73">Mormon Voices&nbsp;&nbsp;(54)</option>
	<option class="level-0" value="100">Ned Scarisbrick&nbsp;&nbsp;(88)</option>
	<option class="level-0" value="1119">New Testament&nbsp;&nbsp;(75)</option>
	<option class="level-0" value="74">News from FAIR&nbsp;&nbsp;(63)</option>
	<option class="level-0" value="75">News stories&nbsp;&nbsp;(69)</option>
	<option class="level-0" value="1124">Newsletter&nbsp;&nbsp;(12)</option>
	<option class="level-0" value="101">Nick Galieti&nbsp;&nbsp;(69)</option>
	<option class="level-0" value="1134">Old Testament&nbsp;&nbsp;(58)</option>
	<option class="level-0" value="4">Perspective&nbsp;&nbsp;(51)</option>
	<option class="level-0" value="76">Philosophy&nbsp;&nbsp;(33)</option>
	<option class="level-0" value="77">Podcast&nbsp;&nbsp;(577)</option>
	<option class="level-0" value="78">Politics&nbsp;&nbsp;(47)</option>
	<option class="level-0" value="79">Polygamy&nbsp;&nbsp;(80)</option>
	<option class="level-0" value="80">pornography&nbsp;&nbsp;(8)</option>
	<option class="level-0" value="81">Power of Testimony&nbsp;&nbsp;(82)</option>
	<option class="level-0" value="1118">Priesthood&nbsp;&nbsp;(37)</option>
	<option class="level-0" value="82">Prophets&nbsp;&nbsp;(162)</option>
	<option class="level-0" value="6">Questions&nbsp;&nbsp;(129)</option>
	<option class="level-0" value="83">Racial Issues&nbsp;&nbsp;(55)</option>
	<option class="level-0" value="7">Resources&nbsp;&nbsp;(74)</option>
	<option class="level-0" value="1129">Revelation&nbsp;&nbsp;(60)</option>
	<option class="level-0" value="84">RiseUp&nbsp;&nbsp;(35)</option>
	<option class="level-0" value="85">Science&nbsp;&nbsp;(51)</option>
	<option class="level-0" value="102">SteveDensleyJr&nbsp;&nbsp;(8)</option>
	<option class="level-0" value="86">Suicide&nbsp;&nbsp;(5)</option>
	<option class="level-0" value="87">Temples&nbsp;&nbsp;(133)</option>
	<option class="level-0" value="744">Testimonies&nbsp;&nbsp;(73)</option>
	<option class="level-0" value="1">Uncategorized&nbsp;&nbsp;(60)</option>
	<option class="level-0" value="1153">Wilford Woodruff Papers&nbsp;&nbsp;(11)</option>
	<option class="level-0" value="88">Women&nbsp;&nbsp;(96)</option>
	<option class="level-0" value="89">Youth&nbsp;&nbsp;(30)</option>
	<option class="level-0" value="1151">Zachary Wright&nbsp;&nbsp;(9)</option>
</select>
</form><script type="text/javascript">
/* <![CDATA[ */

(function() {
	var dropdown = document.getElementById( "cat" );
	function onCatChange() {
		if ( dropdown.options[ dropdown.selectedIndex ].value > 0 ) {
			dropdown.parentNode.submit();
		}
	}
	dropdown.onchange = onCatChange;
})();

/* ]]> */
</script>
</div></section>
<section id="recent-comments-3" class="widget widget_recent_comments"><div class="widget-wrap"><h3 class="widgettitle widget-title">Recent Comments</h3>
<ul id="recentcomments"><li class="recentcomments"><span class="comment-author-link">Dennis Horne</span> on <a href="https://www.fairlatterdaysaints.org/blog/2023/11/22/letter-for-my-wife-rebuttal-part-24-blood-atonement#comment-131162">Letter For My Wife Rebuttal, Part 24: Blood Atonement</a></li><li class="recentcomments"><span class="comment-author-link">Trevor Holyoak</span> on <a href="https://www.fairlatterdaysaints.org/blog/2023/10/10/fair-questions-what-did-president-nelson-mean-by-the-kind-of-body-with-which-you-will-be-resurrected-in-his-general-conference-talk#comment-130123">FAIR Questions: What did President Nelson mean by &#8220;the kind of body with which you will be resurrected&#8221; in his General Conference talk?</a></li><li class="recentcomments"><span class="comment-author-link">CortC</span> on <a href="https://www.fairlatterdaysaints.org/blog/2023/10/10/fair-questions-what-did-president-nelson-mean-by-the-kind-of-body-with-which-you-will-be-resurrected-in-his-general-conference-talk#comment-130089">FAIR Questions: What did President Nelson mean by &#8220;the kind of body with which you will be resurrected&#8221; in his General Conference talk?</a></li><li class="recentcomments"><span class="comment-author-link">Andrew Miller</span> on <a href="https://www.fairlatterdaysaints.org/blog/2023/11/03/a-mortal-davidic-servant#comment-130056">A Mortal Davidic Servant?</a></li><li class="recentcomments"><span class="comment-author-link">Dennis Horne</span> on <a href="https://www.fairlatterdaysaints.org/blog/2023/11/03/a-mortal-davidic-servant#comment-130038">A Mortal Davidic Servant?</a></li></ul></div></section>
<section id="archives-3" class="widget widget_archive"><div class="widget-wrap"><h3 class="widgettitle widget-title">Archives</h3>
		<label class="screen-reader-text" for="archives-dropdown-3">Archives</label>
		<select id="archives-dropdown-3" name="archive-dropdown">

			<option value="">Select Month</option>
				<option value='https://www.fairlatterdaysaints.org/blog/2023/11'> November 2023 &nbsp;(9)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2023/10'> October 2023 &nbsp;(9)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2023/09'> September 2023 &nbsp;(13)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2023/08'> August 2023 &nbsp;(8)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2023/07'> July 2023 &nbsp;(19)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2023/06'> June 2023 &nbsp;(15)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2023/05'> May 2023 &nbsp;(11)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2023/04'> April 2023 &nbsp;(12)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2023/03'> March 2023 &nbsp;(25)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2023/02'> February 2023 &nbsp;(10)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2023/01'> January 2023 &nbsp;(6)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2022/12'> December 2022 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2022/11'> November 2022 &nbsp;(10)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2022/10'> October 2022 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2022/09'> September 2022 &nbsp;(18)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2022/08'> August 2022 &nbsp;(10)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2022/07'> July 2022 &nbsp;(12)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2022/06'> June 2022 &nbsp;(11)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2022/05'> May 2022 &nbsp;(6)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2022/04'> April 2022 &nbsp;(12)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2022/03'> March 2022 &nbsp;(16)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2022/02'> February 2022 &nbsp;(13)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2022/01'> January 2022 &nbsp;(17)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2021/12'> December 2021 &nbsp;(19)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2021/11'> November 2021 &nbsp;(21)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2021/10'> October 2021 &nbsp;(16)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2021/09'> September 2021 &nbsp;(17)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2021/08'> August 2021 &nbsp;(10)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2021/07'> July 2021 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2021/06'> June 2021 &nbsp;(6)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2021/05'> May 2021 &nbsp;(15)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2021/04'> April 2021 &nbsp;(13)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2021/03'> March 2021 &nbsp;(8)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2021/02'> February 2021 &nbsp;(12)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2021/01'> January 2021 &nbsp;(6)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2020/12'> December 2020 &nbsp;(4)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2020/11'> November 2020 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2020/10'> October 2020 &nbsp;(4)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2020/09'> September 2020 &nbsp;(11)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2020/08'> August 2020 &nbsp;(15)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2020/07'> July 2020 &nbsp;(16)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2020/06'> June 2020 &nbsp;(4)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2020/05'> May 2020 &nbsp;(6)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2020/04'> April 2020 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2020/03'> March 2020 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2020/02'> February 2020 &nbsp;(6)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2020/01'> January 2020 &nbsp;(2)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2019/12'> December 2019 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2019/11'> November 2019 &nbsp;(2)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2019/10'> October 2019 &nbsp;(8)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2019/09'> September 2019 &nbsp;(7)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2019/08'> August 2019 &nbsp;(7)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2019/07'> July 2019 &nbsp;(8)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2019/06'> June 2019 &nbsp;(7)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2019/05'> May 2019 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2019/04'> April 2019 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2019/03'> March 2019 &nbsp;(4)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2019/02'> February 2019 &nbsp;(10)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2019/01'> January 2019 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2018/12'> December 2018 &nbsp;(11)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2018/11'> November 2018 &nbsp;(10)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2018/10'> October 2018 &nbsp;(11)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2018/09'> September 2018 &nbsp;(8)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2018/08'> August 2018 &nbsp;(8)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2018/07'> July 2018 &nbsp;(10)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2018/06'> June 2018 &nbsp;(11)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2018/05'> May 2018 &nbsp;(11)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2018/04'> April 2018 &nbsp;(10)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2018/03'> March 2018 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2018/02'> February 2018 &nbsp;(14)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2018/01'> January 2018 &nbsp;(12)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2017/12'> December 2017 &nbsp;(1)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2017/11'> November 2017 &nbsp;(2)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2017/10'> October 2017 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2017/09'> September 2017 &nbsp;(4)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2017/08'> August 2017 &nbsp;(1)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2017/06'> June 2017 &nbsp;(2)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2017/05'> May 2017 &nbsp;(1)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2017/04'> April 2017 &nbsp;(1)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2017/03'> March 2017 &nbsp;(1)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2017/02'> February 2017 &nbsp;(1)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2017/01'> January 2017 &nbsp;(1)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2016/12'> December 2016 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2016/11'> November 2016 &nbsp;(2)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2016/10'> October 2016 &nbsp;(2)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2016/09'> September 2016 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2016/08'> August 2016 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2016/07'> July 2016 &nbsp;(2)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2016/06'> June 2016 &nbsp;(10)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2016/05'> May 2016 &nbsp;(13)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2016/04'> April 2016 &nbsp;(8)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2016/03'> March 2016 &nbsp;(7)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2016/02'> February 2016 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2016/01'> January 2016 &nbsp;(7)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2015/12'> December 2015 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2015/11'> November 2015 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2015/10'> October 2015 &nbsp;(6)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2015/09'> September 2015 &nbsp;(4)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2015/08'> August 2015 &nbsp;(14)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2015/07'> July 2015 &nbsp;(6)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2015/06'> June 2015 &nbsp;(11)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2015/05'> May 2015 &nbsp;(19)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2015/04'> April 2015 &nbsp;(12)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2015/03'> March 2015 &nbsp;(19)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2015/02'> February 2015 &nbsp;(14)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2015/01'> January 2015 &nbsp;(28)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2014/12'> December 2014 &nbsp;(9)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2014/11'> November 2014 &nbsp;(17)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2014/10'> October 2014 &nbsp;(31)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2014/09'> September 2014 &nbsp;(21)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2014/08'> August 2014 &nbsp;(29)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2014/07'> July 2014 &nbsp;(21)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2014/06'> June 2014 &nbsp;(16)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2014/05'> May 2014 &nbsp;(21)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2014/04'> April 2014 &nbsp;(9)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2014/03'> March 2014 &nbsp;(12)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2014/02'> February 2014 &nbsp;(13)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2014/01'> January 2014 &nbsp;(14)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2013/12'> December 2013 &nbsp;(13)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2013/11'> November 2013 &nbsp;(6)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2013/10'> October 2013 &nbsp;(11)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2013/09'> September 2013 &nbsp;(2)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2013/08'> August 2013 &nbsp;(9)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2013/07'> July 2013 &nbsp;(15)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2013/06'> June 2013 &nbsp;(13)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2013/05'> May 2013 &nbsp;(7)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2013/04'> April 2013 &nbsp;(12)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2013/03'> March 2013 &nbsp;(12)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2013/02'> February 2013 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2013/01'> January 2013 &nbsp;(7)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2012/12'> December 2012 &nbsp;(9)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2012/11'> November 2012 &nbsp;(15)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2012/10'> October 2012 &nbsp;(11)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2012/09'> September 2012 &nbsp;(9)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2012/08'> August 2012 &nbsp;(10)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2012/07'> July 2012 &nbsp;(12)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2012/06'> June 2012 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2012/05'> May 2012 &nbsp;(13)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2012/04'> April 2012 &nbsp;(4)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2012/03'> March 2012 &nbsp;(8)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2012/02'> February 2012 &nbsp;(10)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2012/01'> January 2012 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2011/12'> December 2011 &nbsp;(9)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2011/11'> November 2011 &nbsp;(12)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2011/10'> October 2011 &nbsp;(7)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2011/09'> September 2011 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2011/08'> August 2011 &nbsp;(9)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2011/07'> July 2011 &nbsp;(13)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2011/06'> June 2011 &nbsp;(11)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2011/05'> May 2011 &nbsp;(11)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2011/04'> April 2011 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2011/03'> March 2011 &nbsp;(2)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2011/02'> February 2011 &nbsp;(2)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2011/01'> January 2011 &nbsp;(1)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2010/12'> December 2010 &nbsp;(1)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2010/11'> November 2010 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2010/10'> October 2010 &nbsp;(7)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2010/09'> September 2010 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2010/08'> August 2010 &nbsp;(4)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2010/07'> July 2010 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2010/06'> June 2010 &nbsp;(4)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2010/05'> May 2010 &nbsp;(4)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2010/04'> April 2010 &nbsp;(9)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2010/03'> March 2010 &nbsp;(1)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2010/02'> February 2010 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2010/01'> January 2010 &nbsp;(4)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2009/12'> December 2009 &nbsp;(2)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2009/11'> November 2009 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2009/10'> October 2009 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2009/09'> September 2009 &nbsp;(8)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2009/08'> August 2009 &nbsp;(11)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2009/07'> July 2009 &nbsp;(6)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2009/06'> June 2009 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2009/05'> May 2009 &nbsp;(4)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2009/04'> April 2009 &nbsp;(1)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2009/03'> March 2009 &nbsp;(3)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2009/02'> February 2009 &nbsp;(4)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2009/01'> January 2009 &nbsp;(2)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2008/12'> December 2008 &nbsp;(6)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2008/11'> November 2008 &nbsp;(5)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2008/10'> October 2008 &nbsp;(10)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2008/09'> September 2008 &nbsp;(8)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2008/08'> August 2008 &nbsp;(6)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2008/07'> July 2008 &nbsp;(9)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2008/06'> June 2008 &nbsp;(4)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2008/05'> May 2008 &nbsp;(8)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2008/04'> April 2008 &nbsp;(9)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2008/03'> March 2008 &nbsp;(14)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2008/02'> February 2008 &nbsp;(18)</option>
	<option value='https://www.fairlatterdaysaints.org/blog/2008/01'> January 2008 &nbsp;(24)</option>

		</select>

			<script type="text/javascript">
/* <![CDATA[ */

(function() {
	var dropdown = document.getElementById( "archives-dropdown-3" );
	function onSelectChange() {
		if ( dropdown.options[ dropdown.selectedIndex ].value !== '' ) {
			document.location.href = this.options[ this.selectedIndex ].value;
		}
	}
	dropdown.onchange = onSelectChange;
})();

/* ]]> */
</script>
</div></section>
</aside></div></div><div class="footer-widgets" id="genesis-footer-widgets"><h2 class="genesis-sidebar-title screen-reader-text">Footer</h2><div class="wrap"><div class="widget-area footer-widgets-1 footer-widget-area"><section id="fairmormon_about-2" class="widget widget_fairmormon_about"><div class="widget-wrap"><article class="fairmormon-about-widget"><img class="fairmormon-about-widget-image" src="https://www.fairlatterdaysaints.org/wp-content/uploads/2021/01/2021_fair_logo_primary.png" alt="FairMormon Logo" /><p class="fairmormon-about-widget-message">FAIR is a non-profit organization dedicated to providing well-documented answers to criticisms of the doctrine, practice, and history of The Church of Jesus Christ of Latter-day Saints.</p></article></div></section>
</div><div class="widget-area footer-widgets-2 footer-widget-area"><section id="nav_menu-3" class="widget widget_nav_menu"><div class="widget-wrap"><h3 class="widgettitle widget-title">Our Friends</h3>
<div class="menu-our-friends-container"><ul id="menu-our-friends" class="menu"><li id="menu-item-25350" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-25350"><a href="https://rsc.byu.edu/">BYU Religious Studies Center</a></li>
<li id="menu-item-25741" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-25741"><a href="https://byustudies.byu.edu/">BYU Studies</a></li>
<li id="menu-item-25349" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-25349"><a href="https://bookofmormoncentral.org/">Book of Mormon Central</a></li>
<li id="menu-item-31417" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-31417"><a href="https://thefamilyproclamation.org/">TheFamilyProclamation.org</a></li>
<li id="menu-item-25348" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-25348"><a href="https://interpreterfoundation.org/">Interpreter Foundation</a></li>
<li id="menu-item-25352" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-25352"><a href="https://wilfordwoodruffpapers.org/">Wilford Woodruff Papers Project</a></li>
</ul></div></div></section>
</div><div class="widget-area footer-widgets-3 footer-widget-area"><section id="nav_menu-4" class="widget widget_nav_menu"><div class="widget-wrap"><h3 class="widgettitle widget-title">Follow Us</h3>
<div class="menu-social-navigation-container"><ul id="menu-social-navigation" class="menu"><li id="menu-item-14533" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-14533"><a href="https://www.facebook.com/fairlatterdaysaints">Facebook</a></li>
<li id="menu-item-14534" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-14534"><a href="https://twitter.com/ldsfair">Twitter</a></li>
<li id="menu-item-14537" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-14537"><a href="http://itunes.apple.com/us/podcast/mormon-fair-cast/id397315546">iTunes</a></li>
<li id="menu-item-14536" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-14536"><a href="https://www.youtube.com/user/fairldsorg">YouTube</a></li>
</ul></div></div></section>
<section id="custom_html-4" class="widget_text widget widget_custom_html"><div class="widget_text widget-wrap"><div class="textwidget custom-html-widget"><a href="https://play.google.com/store/apps/details?id=com.andromo.dev133584.app131088"><img src="https://play.google.com/intl/en_us/badges/images/apps/en-play-badge-border.png" alt="Android app on Google Play" width="135" height="40" /></a>
<a href="https://apps.apple.com/us/app/faithful-answers/id6470235837?itsct=apps_box_badge&amp;itscg=30200" ><img src="https://tools.applemediaservices.com/api/badges/download-on-the-app-store/black/en-us?size=250x83&amp;releaseDate=1700352000" alt="Download on the App Store" style="width: 135px; height: 40px;"></a>
</div></div></section>
</div><div class="widget-area footer-widgets-4 footer-widget-area"><section id="fairmormon_donation-2" class="widget widget_fairmormon_donation"><div class="widget-wrap"><article class="fairmormon-donation-widget"><h3 class="widgettitle widget-title">Donate to FAIR</h3>
<p class="fairmormon-donation-widget-message">We are a volunteer organization. We invite you to give back.</p><a class="fairmormon-donation-widget-button" href="https://www.fairlatterdaysaints.org/donate">Donate Now</a></article></div></section>
</div></div></div><footer class="site-footer"><div class="wrap"><aside class="widget-area"><h2 class="genesis-sidebar-title screen-reader-text">Site Footer</h2><div class="footer-copyright"><p>Copyright &copy; 1997-2023 by The Foundation for Apologetic Information and Research, Inc. All Rights Reserved.</p><p>The views and opinions expressed do not necessarily reflect the views or opinions of FAIR, its officers, directors or supporters.</p><p>No portion of this site may be reproduced without the express written consent of The Foundation for Apologetic Information and Research, Inc.</p><p>Any opinions expressed, implied, or included in or with the goods and services offered by FAIR are solely those of FAIR and not those of The Church of Jesus Christ of Latter-day Saints.</p></div><div class="footer-author"><img src="https://www.fairlatterdaysaints.org/wp-content/themes/genesis-fairmormon/images/fair_logo.png" alt="Foundation for Apologetic Information and Research (FAIR) Logo" /><p>FAIR is controlled and operated by the Foundation for Apologetic Information and Research (FAIR)</p></div></aside></div></footer></div><script type="text/javascript">
		/* MonsterInsights Scroll Tracking */
		if ( typeof(jQuery) !== 'undefined' ) {
		jQuery( document ).ready(function(){
		function monsterinsights_scroll_tracking_load() {
		if ( ( typeof(__gaTracker) !== 'undefined' && __gaTracker && __gaTracker.hasOwnProperty( "loaded" ) && __gaTracker.loaded == true ) || ( typeof(__gtagTracker) !== 'undefined' && __gtagTracker ) ) {
		(function(factory) {
		factory(jQuery);
		}(function($) {

		/* Scroll Depth */
		"use strict";
		var defaults = {
		percentage: true
		};

		var $window = $(window),
		cache = [],
		scrollEventBound = false,
		lastPixelDepth = 0;

		/*
		* Plugin
		*/

		$.scrollDepth = function(options) {

		var startTime = +new Date();

		options = $.extend({}, defaults, options);

		/*
		* Functions
		*/

		function sendEvent(action, label, scrollDistance, timing) {
		if ( 'undefined' === typeof MonsterInsightsObject || 'undefined' === typeof MonsterInsightsObject.sendEvent ) {
		return;
		}
			var paramName = action.toLowerCase();
	var fieldsArray = {
	send_to: 'G-64574D0HQS',
	non_interaction: true
	};
	fieldsArray[paramName] = label;

	if (arguments.length > 3) {
	fieldsArray.scroll_timing = timing
	MonsterInsightsObject.sendEvent('event', 'scroll_depth', fieldsArray);
	} else {
	MonsterInsightsObject.sendEvent('event', 'scroll_depth', fieldsArray);
	}
			}

		function calculateMarks(docHeight) {
		return {
		'25%' : parseInt(docHeight * 0.25, 10),
		'50%' : parseInt(docHeight * 0.50, 10),
		'75%' : parseInt(docHeight * 0.75, 10),
		/* Cushion to trigger 100% event in iOS */
		'100%': docHeight - 5
		};
		}

		function checkMarks(marks, scrollDistance, timing) {
		/* Check each active mark */
		$.each(marks, function(key, val) {
		if ( $.inArray(key, cache) === -1 && scrollDistance >= val ) {
		sendEvent('Percentage', key, scrollDistance, timing);
		cache.push(key);
		}
		});
		}

		function rounded(scrollDistance) {
		/* Returns String */
		return (Math.floor(scrollDistance/250) * 250).toString();
		}

		function init() {
		bindScrollDepth();
		}

		/*
		* Public Methods
		*/

		/* Reset Scroll Depth with the originally initialized options */
		$.scrollDepth.reset = function() {
		cache = [];
		lastPixelDepth = 0;
		$window.off('scroll.scrollDepth');
		bindScrollDepth();
		};

		/* Add DOM elements to be tracked */
		$.scrollDepth.addElements = function(elems) {

		if (typeof elems == "undefined" || !$.isArray(elems)) {
		return;
		}

		$.merge(options.elements, elems);

		/* If scroll event has been unbound from window, rebind */
		if (!scrollEventBound) {
		bindScrollDepth();
		}

		};

		/* Remove DOM elements currently tracked */
		$.scrollDepth.removeElements = function(elems) {

		if (typeof elems == "undefined" || !$.isArray(elems)) {
		return;
		}

		$.each(elems, function(index, elem) {

		var inElementsArray = $.inArray(elem, options.elements);
		var inCacheArray = $.inArray(elem, cache);

		if (inElementsArray != -1) {
		options.elements.splice(inElementsArray, 1);
		}

		if (inCacheArray != -1) {
		cache.splice(inCacheArray, 1);
		}

		});

		};

		/*
		* Throttle function borrowed from:
		* Underscore.js 1.5.2
		* http://underscorejs.org
		* (c) 2009-2013 Jeremy Ashkenas, DocumentCloud and Investigative Reporters & Editors
		* Underscore may be freely distributed under the MIT license.
		*/

		function throttle(func, wait) {
		var context, args, result;
		var timeout = null;
		var previous = 0;
		var later = function() {
		previous = new Date;
		timeout = null;
		result = func.apply(context, args);
		};
		return function() {
		var now = new Date;
		if (!previous) previous = now;
		var remaining = wait - (now - previous);
		context = this;
		args = arguments;
		if (remaining <= 0) {
		clearTimeout(timeout);
		timeout = null;
		previous = now;
		result = func.apply(context, args);
		} else if (!timeout) {
		timeout = setTimeout(later, remaining);
		}
		return result;
		};
		}

		/*
		* Scroll Event
		*/

		function bindScrollDepth() {

		scrollEventBound = true;

		$window.on('scroll.scrollDepth', throttle(function() {
		/*
		* We calculate document and window height on each scroll event to
		* account for dynamic DOM changes.
		*/

		var docHeight = $(document).height(),
		winHeight = window.innerHeight ? window.innerHeight : $window.height(),
		scrollDistance = $window.scrollTop() + winHeight,

		/* Recalculate percentage marks */
		marks = calculateMarks(docHeight),

		/* Timing */
		timing = +new Date - startTime;

		checkMarks(marks, scrollDistance, timing);
		}, 500));

		}

		init();
		};

		/* UMD export */
		return $.scrollDepth;

		}));

		jQuery.scrollDepth();
		} else {
		setTimeout(monsterinsights_scroll_tracking_load, 200);
		}
		}
		monsterinsights_scroll_tracking_load();
		});
		}
		/* End MonsterInsights Scroll Tracking */

</script><script type="text/javascript" id="site_tracking-js-extra">
/* <![CDATA[ */
var php_data = {"ac_settings":{"tracking_actid":475441427,"site_tracking_default":1},"user_email":""};
/* ]]> */
</script>
<script type="text/javascript" src="https://www.fairlatterdaysaints.org/wp-content/plugins/activecampaign-subscription-forms/site_tracking.js?ver=6.4.1" id="site_tracking-js"></script>
<script type="text/javascript" src="https://www.fairlatterdaysaints.org/wp-includes/js/hoverIntent.min.js?ver=1.10.2" id="hoverIntent-js"></script>
<script type="text/javascript" src="https://www.fairlatterdaysaints.org/wp-content/themes/genesis/lib/js/menu/superfish.min.js?ver=1.7.10" id="superfish-js"></script>
<script type="text/javascript" src="https://www.fairlatterdaysaints.org/wp-content/themes/genesis/lib/js/menu/superfish.args.min.js?ver=3.4.0" id="superfish-args-js"></script>
<script type="text/javascript" src="https://www.fairlatterdaysaints.org/wp-content/themes/genesis/lib/js/skip-links.min.js?ver=3.4.0" id="skip-links-js"></script>
<script type="text/javascript" id="genesis-fairmormon-responsive-menu-js-extra">
/* <![CDATA[ */
var genesisSampleL10n = {"mainMenu":"Navigate & Search","subMenu":"Menu"};
/* ]]> */
</script>
<script type="text/javascript" src="https://www.fairlatterdaysaints.org/wp-content/themes/genesis-fairmormon/js/responsive-menu.js?ver=1.0.0" id="genesis-fairmormon-responsive-menu-js"></script>
<script type="text/javascript" id="eael-general-js-extra">
/* <![CDATA[ */
var localize = {"ajaxurl":"https:\\/\\/www.fairlatterdaysaints.org\\/wp-admin\\/admin-ajax.php","nonce":"80d73f1925","i18n":{"added":"Added ","compare":"Compare","loading":"Loading..."},"eael_translate_text":{"required_text":"is a required field","invalid_text":"Invalid","billing_text":"Billing","shipping_text":"Shipping","fg_mfp_counter_text":"of"},"page_permalink":"https:\\/\\/www.fairlatterdaysaints.org\\/blog\\/2021\\/11\\/26\\/the-ces-letter-rebuttal-part-29","cart_redirectition":"","cart_page_url":"","el_breakpoints":{"mobile":{"label":"Mobile Portrait","value":719,"default_value":767,"direction":"max","is_enabled":true},"mobile_extra":{"label":"Mobile Landscape","value":880,"default_value":880,"direction":"max","is_enabled":false},"tablet":{"label":"Tablet Portrait","value":1119,"default_value":1024,"direction":"max","is_enabled":true},"tablet_extra":{"label":"Tablet Landscape","value":1200,"default_value":1200,"direction":"max","is_enabled":false},"laptop":{"label":"Laptop","value":1366,"default_value":1366,"direction":"max","is_enabled":false},"widescreen":{"label":"Widescreen","value":2400,"default_value":2400,"direction":"min","is_enabled":false}}};
/* ]]> */
</script>
<script type="text/javascript" src="https://www.fairlatterdaysaints.org/wp-content/plugins/essential-addons-for-elementor-lite/assets/front-end/js/view/general.min.js?ver=5.9" id="eael-general-js"></script>
</body></html>
"""


def test_load_fairs() -> None:
    """It returns a valid Document for a fair."""
    url = "https://www.fairlatterdaysaints.org/blog/2021/11/26/the-ces-letter-rebuttal-part-29"
    result = load_fairs(url, html)
    assert len(result.page_content) > 0
    assert result.metadata["url"] == url
    assert result.metadata["title"] == "The CES Letter Rebuttal — Part 29"
    assert result.page_content.startswith("## Part 29:")
