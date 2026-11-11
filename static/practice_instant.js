// Practice: tapping an option checks it at once (no "Check answer"), and swiping moves to the next / previous question.
(function () {
  "use strict";
  var form = document.querySelector("form fieldset.opts") && document.querySelector("form fieldset.opts").closest("form");
  if (form) document.documentElement.classList.add("pr-instant");
  if (form && !document.getElementById("answer-result")) {
    var sent = false;
    form.addEventListener("change", function (e) {
      if (sent || !e.target.matches('input[type="radio"][name="answer"]')) return;
      if (document.body.classList.contains("mk-pen-on")) return;     // highlighter is on: don't answer by accident
      sent = true;
      var lab = e.target.closest("label"); if (lab) lab.classList.add("is-picked");
      if (form.requestSubmit) form.requestSubmit(); else form.submit();
    });
  }
  // swipe left = next, swipe right = previous
  var x0 = 0, y0 = 0, t0 = 0, ok = false;
  document.addEventListener("touchstart", function (e) {
    if (e.touches.length !== 1 || document.body.classList.contains("mk-pen-on")) { ok = false; return; }
    var t = e.target;
    ok = !(t.closest && t.closest(".xp-tw, .mk-ui, input, textarea, select, [data-noswipe]"));   // tables scroll sideways
    x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; t0 = Date.now();
  }, { passive: true });
  document.addEventListener("touchend", function (e) {
    if (!ok) return; ok = false;
    var t = e.changedTouches[0], dx = t.clientX - x0, dy = t.clientY - y0;
    if (Date.now() - t0 > 800 || Math.abs(dx) < 70 || Math.abs(dy) > Math.abs(dx) * 0.6) return;
    var sel = window.getSelection && window.getSelection(); if (sel && !sel.isCollapsed) return;
    var link = document.querySelector(dx < 0 ? 'a[rel="next"]' : 'a[rel="prev"]');
    if (!link) return;
    document.body.classList.add(dx < 0 ? "pr-go-next" : "pr-go-prev");
    location.href = link.href;
  }, { passive: true });
})();
