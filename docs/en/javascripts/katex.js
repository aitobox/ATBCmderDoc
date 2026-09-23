/**
 * ATBCmder Documentation - KaTeX Auto-Render Initializer
 * Renders mathematical expressions processed by pymdownx.arithmatex.
 */
(function () {
  "use strict";

  function renderKatexMath(container) {
    if (typeof renderMathInElement === "undefined") {
      return;
    }
    var root = container || document.body;
    renderMathInElement(root, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false },
        { left: "\\(", right: "\\)", display: false },
        { left: "\\[", right: "\\]", display: true }
      ],
      throwOnError: false
    });
  }

  // Initial trigger
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      renderKatexMath(document.body);
    });
  } else {
    renderKatexMath(document.body);
  }

  // Support for Material for MkDocs instant navigation / PJAX
  if (typeof window.document$ !== "undefined") {
    window.document$.subscribe(function () {
      renderKatexMath(document.body);
    });
  }
})();
