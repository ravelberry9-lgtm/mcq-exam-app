// Recall hub: show known / revise counts per deck from that deck's own localStorage key ({ cardId: "k" | "x" }).
(function () {
  "use strict";
  [].forEach.call(document.querySelectorAll(".rh-tile[data-store]"), function (a) {
    var p = {};
    try { p = JSON.parse(localStorage.getItem(a.dataset.store) || "{}") || {}; } catch (e) { p = {}; }
    var k = 0, x = 0, total = +a.dataset.total || 0;
    Object.keys(p).forEach(function (id) { if (/^TH-/.test(id)) return; /* theme tiles are not cards */ if (p[id] === "k") k++; else if (p[id] === "x") x++; });
    k = Math.min(k, total); x = Math.min(x, total - k);
    if (!k && !x) return;
    var pr = a.querySelector(".rh-prog");
    if (pr) pr.textContent = a.classList.contains("pr-tile") ? " · " + k + " ✓ " + x + " ↻" : " · " + k + " known · " + x + " to revise";
    var bar = a.querySelector(".rh-bar");
    bar.style.setProperty("--k", (k / total * 100) + "%");
    bar.style.setProperty("--x", (x / total * 100) + "%");
    bar.classList.add("on");
  });
})();
