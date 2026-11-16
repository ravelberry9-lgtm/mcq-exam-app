// MCQ / PYQ tiles open a chooser: practise the whole unit or one section.
(function () {
  "use strict";
  function close(sheet) { sheet.remove(); document.body.classList.remove("pk-open"); }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a.st.c2, a.st.c3");
    if (!a || e.ctrlKey || e.metaKey) return;
    var u = new URL(a.href, location.href), kind = u.searchParams.get("kind"), unit = u.searchParams.get("unit");
    if (!kind || !unit) return;
    e.preventDefault();
    var api = (a.dataset.pick || "/learn/polity/unit6/pick.json") + "?kind=" + kind + "&unit=" + unit;
    fetch(api, { credentials: "same-origin" }).then(function (r) { if (!r.ok) throw 0; return r.json(); }).then(function (d) {
      var sheet = document.createElement("div");
      sheet.className = "pk-sheet"; sheet.setAttribute("role", "dialog"); sheet.setAttribute("aria-modal", "true");
      var h = '<div class="pk-back" data-x></div><div class="pk-box"><div class="pk-head"><b>' + (kind === "pyq" ? "PYQs" : "MCQs") +
        " · Unit " + unit + '</b><button type="button" class="pk-x" data-x aria-label="Close">✕</button></div><p class="pk-sub">Choose what to practise</p><ul>';
      d.items.forEach(function (it, i) {
        var m = it.label.match(/^(\d+\.\d+\.\d+)\s+(.*)$/);
        h += '<li><a class="pk-item' + (i === 0 ? " pk-all" : "") + '" href="' + it.url + '">' +
          (m ? '<span class="pk-no">' + m[1] + "</span><span class=\"pk-t\">" + m[2].replace(/</g, "&lt;") + "</span>" : '<span class="pk-t">' + it.label + "</span>") +
          '<span class="pk-n">' + it.count + "</span></a></li>";
      });
      h += '</ul><a class="pk-list" href="' + d.list_url + '">See the full question list ›</a></div>';
      sheet.innerHTML = h;
      sheet.addEventListener("click", function (ev) { if (ev.target.hasAttribute("data-x")) close(sheet); });
      document.addEventListener("keydown", function esc(ev) { if (ev.key === "Escape") { close(sheet); document.removeEventListener("keydown", esc); } });
      document.body.appendChild(sheet); document.body.classList.add("pk-open");
      var first = sheet.querySelector(".pk-item"); if (first) first.focus();
    }).catch(function () { location.href = a.href; });
  });
})();
