/**
 * ATBCmder Documentation - ASCII / Unicode Box Diagram CJK Monospace Normalizer
 *
 * In web browsers, proportional CJK fallback fonts render Chinese characters
 * at 1.0em, whereas Western monospace fonts (Roboto Mono, Menlo, etc.) render
 * at ~0.6em per character (2 chars = 1.2em). This causes lines with Chinese text
 * in ASCII box diagrams to be ~20% narrower, leading to right-border jaggedness.
 *
 * This script identifies code blocks containing box-drawing characters and wraps
 * all CJK characters in <span class="cjk-char"> with CSS `display: inline-block; width: 2ch;`,
 * ensuring mathematical 2:1 alignment without altering clipboard/copy text.
 */
(function () {
  'use strict';

  var CJK_REGEX = /([\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff\u3000-\u303f\uff01-\uff60\uffe0-\uffe6])/g;
  var BOX_CHARS_REGEX = /[┌─│┼├┤┴┬└┘╭╮╰╯═║╔╗╚╝╠╣╦╩╬]/;

  function normalizeCodeBlock(code) {
    if (code.getAttribute('data-ascii-aligned') === 'true') {
      return;
    }

    var text = code.textContent;
    if (!BOX_CHARS_REGEX.test(text) && !(/\+[-=]{2,}\+/.test(text) && text.indexOf('|') !== -1)) {
      return;
    }

    var walker = document.createTreeWalker(code, NodeFilter.SHOW_TEXT, null, false);
    var textNodes = [];
    var node;

    while ((node = walker.nextNode())) {
      CJK_REGEX.lastIndex = 0;
      if (CJK_REGEX.test(node.nodeValue)) {
        textNodes.push(node);
      }
    }

    for (var i = 0; i < textNodes.length; i++) {
      var tn = textNodes[i];
      var parent = tn.parentNode;
      if (parent && parent.classList && parent.classList.contains('cjk-char')) {
        continue;
      }

      var frag = document.createDocumentFragment();
      var str = tn.nodeValue;
      var lastIndex = 0;
      CJK_REGEX.lastIndex = 0;
      var match;

      while ((match = CJK_REGEX.exec(str)) !== null) {
        if (match.index > lastIndex) {
          frag.appendChild(document.createTextNode(str.slice(lastIndex, match.index)));
        }
        var span = document.createElement('span');
        span.className = 'cjk-char';
        span.textContent = match[0];
        frag.appendChild(span);
        lastIndex = CJK_REGEX.lastIndex;
      }

      if (lastIndex < str.length) {
        frag.appendChild(document.createTextNode(str.slice(lastIndex)));
      }

      if (parent) {
        parent.replaceChild(frag, tn);
      }
    }

    code.setAttribute('data-ascii-aligned', 'true');
  }

  function alignAllDiagrams(container) {
    var root = container || document;
    var codeBlocks = root.querySelectorAll('.highlight code, pre code');
    for (var i = 0; i < codeBlocks.length; i++) {
      normalizeCodeBlock(codeBlocks[i]);
    }
  }

  // Initial trigger
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      alignAllDiagrams(document);
    });
  } else {
    alignAllDiagrams(document);
  }

  // Support for Material for MkDocs instant navigation / PJAX
  if (typeof window.document$ !== 'undefined') {
    window.document$.subscribe(function () {
      alignAllDiagrams(document);
    });
  }
})();
