/**
 * ATBCmder Documentation - Automatic Browser Language Detection & Redirection
 * Uses Zensical's extra_javascript feature to seamlessly route users to their preferred language.
 */
(function () {
  'use strict';

  if (window.__atbcmder_lang_detector_initialized) return;
  window.__atbcmder_lang_detector_initialized = true;

  var STORAGE_KEY = 'preferred_language';

  // 1. Helper to extract query parameter (e.g. ?lang=zh or ?lang=en)
  function getQueryParam(name) {
    try {
      var match = RegExp('[?&]' + name + '=([^&]*)').exec(window.location.search);
      return match ? decodeURIComponent(match[1].replace(/\+/g, ' ')) : null;
    } catch (e) {
      return null;
    }
  }

  // Allow explicit language override via URL param
  var explicitLang = getQueryParam('lang');
  if (explicitLang === 'zh' || explicitLang === 'en') {
    try {
      localStorage.setItem(STORAGE_KEY, explicitLang);
    } catch (e) {}
  }

  // 2. Read saved preference
  var savedPreference = null;
  try {
    savedPreference = localStorage.getItem(STORAGE_KEY);
  } catch (e) {}

  var pathname = window.location.pathname;
  var isZhPage = pathname.indexOf('/zh/') !== -1 || pathname.endsWith('/zh');
  var isEnPage = pathname.indexOf('/en/') !== -1 || pathname.endsWith('/en');

  // Only apply language redirection if we are inside a language tree
  if (!isZhPage && !isEnPage) {
    return;
  }

  // 3. If the user arrived by clicking an internal link on the same domain,
  // do not disrupt their active session; save their current browsing language.
  var isInternalNav = false;
  try {
    if (document.referrer && window.location.host) {
      var refUrl = new URL(document.referrer);
      if (refUrl.host === window.location.host) {
        isInternalNav = true;
      }
    }
  } catch (e) {}

  if (!savedPreference && isInternalNav) {
    try {
      localStorage.setItem(STORAGE_KEY, isZhPage ? 'zh' : 'en');
    } catch (e) {}
    savedPreference = isZhPage ? 'zh' : 'en';
  }

  // 4. Evaluate redirection target
  var targetLang = null;
  if (savedPreference === 'zh' || savedPreference === 'en') {
    targetLang = savedPreference;
  } else {
    // Detect browser languages
    var browserLangs = navigator.languages || [navigator.language || navigator.userLanguage || ''];
    var isChinese = false;
    for (var i = 0; i < browserLangs.length; i++) {
      var l = (browserLangs[i] || '').toLowerCase();
      if (l.indexOf('zh') === 0) {
        isChinese = true;
        break;
      }
    }
    targetLang = isChinese ? 'zh' : 'en';
  }

  // 5. Perform redirection if current page language does not match target language
  if (targetLang === 'zh' && isEnPage) {
    var targetUrl = pathname.replace(/\/en(\/|$)/, '/zh$1') + window.location.search + window.location.hash;
    window.location.replace(targetUrl);
    return;
  } else if (targetLang === 'en' && isZhPage) {
    var targetUrl = pathname.replace(/\/zh(\/|$)/, '/en$1') + window.location.search + window.location.hash;
    window.location.replace(targetUrl);
    return;
  }

  // 6. Bind click events to language switchers so manual switches are remembered
  function bindLanguageSwitchers() {
    var switchLinks = document.querySelectorAll('a[href*="/en/"], a[href*="/zh/"]');
    for (var i = 0; i < switchLinks.length; i++) {
      (function (link) {
        var href = link.getAttribute('href') || '';
        if (href.indexOf('/en/') !== -1) {
          link.addEventListener('click', function () {
            try { localStorage.setItem(STORAGE_KEY, 'en'); } catch (e) {}
          });
        } else if (href.indexOf('/zh/') !== -1) {
          link.addEventListener('click', function () {
            try { localStorage.setItem(STORAGE_KEY, 'zh'); } catch (e) {}
          });
        }
      })(switchLinks[i]);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bindLanguageSwitchers);
  } else {
    bindLanguageSwitchers();
  }
})();
