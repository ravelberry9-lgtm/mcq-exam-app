// Practice: tapping an option checks it at once (no "Check answer"), and swiping moves to the next / previous question.
(function () {
  "use strict";
  var form = document.querySelector("form fieldset.opts") && document.querySelector("form fieldset.opts").closest("form");
  if (form) document.documentElement.classList.add("pr-instant");
  if (form && !document.getElementById("answer-result")) {
    var sent = false;
    form.addEventListener("change", function (e) {
      if (sent || !e.target.matches('input[type="radio"][name="answer"]')) return;
      sent = true;
      var lab = e.target.closest("label"); if (lab) lab.classList.add("is-picked");
      if (form.requestSubmit) form.requestSubmit(); else form.submit();
    });
  }
  // swipe left = next, swipe right = previous. The page follows the finger, and the
  // neighbouring questions are prefetched so the next one opens quickly.
  ["next", "prev"].forEach(function (rel) {
    var a = document.querySelector('a[rel="' + rel + '"]');
    if (a) { var l = document.createElement("link"); l.rel = "prefetch"; l.href = a.href; document.head.appendChild(l); }
  });
  var pane = document.querySelector("main") || document.body;
  var x0 = 0, y0 = 0, dx = 0, ok = false, horiz = null, going = false;
  function busy() { var s = window.getSelection && getSelection(); return !!(s && !s.isCollapsed); }
  function reset(anim) {
    pane.style.transition = anim ? "transform .18s ease-out, opacity .18s" : "";
    pane.style.transform = ""; pane.style.opacity = "";
  }
  document.addEventListener("touchstart", function (e) {
    if (going || e.touches.length !== 1 || busy()) { ok = false; return; }
    var t = e.target;
    ok = !(t.closest && t.closest(".xp-tw, .mk-ui, input, textarea, select, [data-noswipe], table, pre"));
    x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; dx = 0; horiz = null;
  }, { passive: true });
  document.addEventListener("touchmove", function (e) {
    if (!ok) return;
    var t = e.touches[0], mx = t.clientX - x0, my = t.clientY - y0;
    if (horiz === null && Math.abs(mx) + Math.abs(my) > 10) horiz = Math.abs(mx) > Math.abs(my) * 1.4;
    if (!horiz) return;
    if (busy()) { ok = false; reset(true); return; }
    var link = document.querySelector(mx < 0 ? 'a[rel="next"]' : 'a[rel="prev"]');
    dx = link ? mx : mx * 0.25;                      // resist when there is no next/previous
    pane.style.transition = "none";
    pane.style.transform = "translate3d(" + dx + "px,0,0)";
    pane.style.opacity = String(1 - Math.min(Math.abs(dx) / 600, 0.35));
  }, { passive: true });
  function end() {
    if (!ok) return; ok = false;
    if (!horiz) return;
    var link = document.querySelector(dx < 0 ? 'a[rel="next"]' : 'a[rel="prev"]');
    if (!link || Math.abs(dx) < Math.min(90, innerWidth * 0.22)) { reset(true); return; }
    going = true;
    pane.style.transition = "transform .15s ease-in, opacity .15s";
    pane.style.transform = "translate3d(" + (dx < 0 ? -innerWidth : innerWidth) + "px,0,0)"; pane.style.opacity = "0.2";
    setTimeout(function () { location.href = link.href; }, 120);
  }
  document.addEventListener("touchend", end, { passive: true });
  document.addEventListener("touchcancel", function () { ok = false; reset(true); }, { passive: true });
  window.addEventListener("pageshow", function () { going = false; reset(false); });   // back button restores the page
})();
