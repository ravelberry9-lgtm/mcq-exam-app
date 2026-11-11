// Pink highlighter (tap 🖍 then drag), undo, and page bookmarks — on every page of the app.
// Usage: PolityMarks.attach(rootEl, {key, title, url, starHost}). Marks are stored per device on the server
// (with a localStorage copy so they show instantly and survive a lost connection).
(function () {
  "use strict";
  var API = "/learn/my-saved/api";
  var roots = [];            // attached states

  function csrf() { var m = document.querySelector('meta[name="csrf-token"]'); return m ? m.content : ""; }
  function lsGet(k) { try { return JSON.parse(localStorage.getItem("mk:" + k) || "null"); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem("mk:" + k, JSON.stringify(v)); } catch (e) {} }
  function post(body) {
    return fetch(API, { method: "POST", credentials: "same-origin", headers: { "Content-Type": "application/json", "X-CSRF-Token": csrf() }, body: JSON.stringify(body) }).catch(function () {});
  }

  // ---- text offsets ----
  function texts(root) {
    var out = [], w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) { return n.parentNode.closest(".mk-ui") ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT; }
    });
    while (w.nextNode()) out.push(w.currentNode);
    return out;
  }
  function offsetOf(root, node, off) {
    var r = document.createRange();
    try { r.setStart(root, 0); r.setEnd(node, off); } catch (e) { return -1; }
    return r.toString().length;
  }

  // ---- paint ----
  function unpaint(root) {
    [].slice.call(root.querySelectorAll("span.mk")).forEach(function (sp) {
      var p = sp.parentNode; while (sp.firstChild) p.insertBefore(sp.firstChild, sp); p.removeChild(sp); p.normalize();
    });
  }
  function paint(st) {
    unpaint(st.root);
    st.marks.forEach(function (m, idx) {
      var pos = 0, list = texts(st.root);
      list.forEach(function (tn) {
        var a = pos, b = pos + tn.data.length; pos = b;
        var s = Math.max(m.s, a), e = Math.min(m.e, b);
        if (s >= e || !tn.data.slice(s - a, e - a).trim()) return;
        var mid = tn;
        if (s > a) mid = tn.splitText(s - a);
        if (e < b) mid.splitText(e - s);
        var sp = document.createElement("span");
        sp.className = "mk mk-" + m.k + " mk-" + m.c; sp.dataset.mi = idx;
        mid.parentNode.insertBefore(sp, mid); sp.appendChild(mid);
      });
    });
  }

  // ---- state ----
  function save(st) {
    lsSet(st.key, { marks: st.marks, bm: st.bm });
    clearTimeout(st.t);
    var body = { key: st.key, marks: st.marks, title: st.title, url: st.url }; // capture now: the card may change within 400 ms
    st.t = setTimeout(function () { post(body); }, 400);
  }
  function change(st, next) { st.undo.push(JSON.stringify(st.marks)); if (st.undo.length > 50) st.undo.shift(); st.marks = next; paint(st); save(st); }

  // ---- pink highlighter: tap 🖍, then drag a finger across the text ----
  var pen = false, drag = null, lastSt = null, penBtn = null, undoBtn = null;
  function caretAt(x, y) {
    if (document.caretRangeFromPoint) { var r = document.caretRangeFromPoint(x, y); return r && { node: r.startContainer, off: r.startOffset }; }
    if (document.caretPositionFromPoint) { var p = document.caretPositionFromPoint(x, y); return p && { node: p.offsetNode, off: p.offset }; }
    return null;
  }
  function stateFor(node) {
    for (var i = 0; i < roots.length; i++) if (roots[i].root.isConnected && roots[i].root.contains(node)) return roots[i];
    return null;
  }
  function posAt(st, x, y) {
    var c = caretAt(x, y);
    if (!c || c.node.nodeType !== 3 || !st.root.contains(c.node) || (c.node.parentNode.closest && c.node.parentNode.closest(".mk-ui"))) return -1;
    return offsetOf(st.root, c.node, c.off);
  }
  function wordSnap(txt, s, e) {               // grow to whole words so a rough drag still marks clean words
    while (s > 0 && /\S/.test(txt[s - 1])) s--;
    while (e < txt.length && /\S/.test(txt[e])) e++;
    return [s, e];
  }
  function preview(st, s, e) {
    try {
      var list = texts(st.root), pos = 0, a = null, b = null;
      list.forEach(function (tn) { var n = tn.data.length; if (!a && s <= pos + n) a = [tn, s - pos]; if (!b && e <= pos + n) b = [tn, e - pos]; pos += n; });
      if (!a || !b) return;
      var r = document.createRange(); r.setStart(a[0], a[1]); r.setEnd(b[0], b[1]);
      var sel = getSelection(); sel.removeAllRanges(); sel.addRange(r);
    } catch (err) {}
  }
  function addPink(st, s, e) {
    var txt = st.root.textContent, w = wordSnap(txt, s, e); s = w[0]; e = w[1];
    if (e <= s || !txt.slice(s, e).trim()) return;
    var keep = [], ns = s, ne = e;
    st.marks.forEach(function (m) {            // merge with touching pink highlights
      if (m.k === "hl" && m.s <= ne && m.e >= ns) { ns = Math.min(ns, m.s); ne = Math.max(ne, m.e); } else keep.push(m);
    });
    keep.push({ s: ns, e: ne, k: "hl", c: "pink", t: txt.slice(ns, ne).replace(/\s+/g, " ").trim().slice(0, 1000) });
    keep.sort(function (x, y) { return x.s - y.s; });
    change(st, keep); lastSt = st; refreshUndo();
  }
  function removeMark(st, idx) { change(st, st.marks.filter(function (_, i) { return i !== idx; })); lastSt = st; refreshUndo(); }
  function undo() {
    var st = lastSt && lastSt.root.isConnected ? lastSt : null;
    if (!st || !st.undo.length) { toast("Nothing to undo"); return; }
    st.marks = JSON.parse(st.undo.pop()); paint(st); save(st); refreshUndo();
  }
  function refreshUndo() { if (undoBtn) undoBtn.classList.toggle("off", !(lastSt && lastSt.undo.length)); }
  function setPen(on) {
    pen = on; document.body.classList.toggle("mk-pen-on", on);
    if (penBtn) { penBtn.classList.toggle("on", on); penBtn.setAttribute("aria-pressed", on ? "true" : "false"); }
    if (on) toast("Highlighter on — drag across text. Tap 🖍 again to scroll.");
  }
  document.addEventListener("pointerdown", function (e) {
    if (!pen || e.button > 0 || (e.target.closest && e.target.closest(".mk-ui"))) return;
    var st = stateFor(e.target); if (!st) return;
    e.preventDefault();
    var s = posAt(st, e.clientX, e.clientY);
    drag = { st: st, s: s, e: s, x: e.clientX, y: e.clientY, moved: false, mark: e.target.closest && e.target.closest("span.mk") };
  }, true);
  document.addEventListener("pointermove", function (e) {
    if (!drag) return;
    e.preventDefault();
    if (Math.abs(e.clientX - drag.x) + Math.abs(e.clientY - drag.y) > 8) drag.moved = true;
    var p = posAt(drag.st, e.clientX, e.clientY);
    if (p >= 0 && (drag.s < 0 || Math.abs(p - drag.s) < 3000)) { if (drag.s < 0) drag.s = p; drag.e = p; if (drag.s >= 0) preview(drag.st, Math.min(drag.s, p), Math.max(drag.s, p)); }
  }, true);
  function endDrag() {
    if (!drag) return;
    var d = drag; drag = null;
    try { getSelection().removeAllRanges(); } catch (err) {}
    if (!d.moved) { if (d.mark) removeMark(d.st, +d.mark.dataset.mi); return; }   // tap a pink mark to remove it
    if (d.s < 0 || d.e < 0) return;
    addPink(d.st, Math.min(d.s, d.e), Math.max(d.s, d.e));
  }
  document.addEventListener("pointerup", endDrag, true);
  document.addEventListener("pointercancel", function () { drag = null; }, true);
  document.addEventListener("click", function (e) {      // while the pen is on, taps on text never open links
    if (pen && !(e.target.closest && e.target.closest(".mk-ui")) && stateFor(e.target)) { e.preventDefault(); e.stopPropagation(); }
  }, true);

  // ---- bookmark star ----
  function star(st) {
    if (!st.host) return;
    var b = st.host.querySelector(".mk-star");
    if (!b) {
      b = document.createElement("button"); b.type = "button"; b.className = "mk-ui mk-star";
      b.addEventListener("click", function () {
        var s2 = b._st; s2.bm = !s2.bm; paintStar(s2); lsSet(s2.key, { marks: s2.marks, bm: s2.bm });
        post({ key: s2.key, bookmarked: s2.bm, title: s2.title, url: s2.url });
        toast(s2.bm ? "Bookmarked — find it under My saved pages" : "Bookmark removed");
      });
      st.host.appendChild(b);
    }
    b._st = st; paintStar(st);
  }
  function paintStar(st) {
    var b = st.host && st.host.querySelector(".mk-star"); if (!b) return;
    b.textContent = st.bm ? "★" : "☆"; b.setAttribute("aria-pressed", st.bm ? "true" : "false");
    b.setAttribute("aria-label", st.bm ? "Remove bookmark" : "Bookmark this page");
    b.classList.toggle("on", !!st.bm);
  }
  function toast(msg) {
    var t = document.querySelector(".mk-toast");
    if (!t) { t = document.createElement("p"); t.className = "mk-ui mk-toast"; t.setAttribute("role", "status"); document.body.appendChild(t); }
    t.textContent = msg; t.hidden = false; clearTimeout(t._h); t._h = setTimeout(function () { t.hidden = true; }, 2200);
  }

  function attach(root, opt) {
    if (!root || !opt || !opt.key) return;
    var st = null;
    for (var i = 0; i < roots.length; i++) if (roots[i].root === root) st = roots[i];
    if (!st) { st = { root: root }; roots.push(st); }
    root.classList.add("mk-pen-root");
    st.key = opt.key; st.title = opt.title || document.title; st.url = opt.url || location.pathname + location.search;
    st.host = opt.starHost || null; st.undo = []; st.marks = []; st.bm = false;
    var local = lsGet(st.key);
    if (local) { st.marks = local.marks || []; st.bm = !!local.bm; }
    paint(st); star(st);
    var key = st.key;
    fetch(API + "?key=" + encodeURIComponent(key), { credentials: "same-origin" }).then(function (r) { return r.json(); }).then(function (d) {
      if (st.key !== key) return;            // card changed meanwhile
      if (!local || (d.marks && d.marks.length) || d.bookmarked) { st.marks = d.marks || []; st.bm = !!d.bookmarked; paint(st); paintStar(st); lsSet(key, { marks: st.marks, bm: st.bm }); }
      else if (local && (local.marks.length || local.bm)) post({ key: key, marks: st.marks, bookmarked: st.bm, title: st.title, url: st.url }); // push offline edits
    }).catch(function () {});
  }

  // stop marking a root whose content is being replaced (e.g. a card still loading)
  function detach(root) {
    roots = roots.filter(function (s) { return s.root !== root; }); // a pending save already holds its own copy
    if (drag && drag.st.root === root) drag = null;
  }
  window.PolityMarks = { attach: attach, detach: detach };
  // static pages: any element with data-mk-key
  function scan() {
    var explicit = document.querySelectorAll("[data-mk-key]");
    [].forEach.call(explicit, function (el) {
      attach(el, { key: el.dataset.mkKey, title: el.dataset.mkTitle, starHost: document.querySelector(el.dataset.mkStar || "") });
    });
    // floating dock on every page: page bookmark (when the page has no bookmark of its own) + My saved pages
    var dock = document.createElement("div");
    dock.className = "mk-ui mk-dock";
    var own = explicit.length || document.getElementById("ac-dscroll");
    if (!own && location.pathname.indexOf(window.MK_SAVED || "/learn/my-saved/") !== 0) {
      var root = document.getElementById("main") || document.querySelector("main") || document.body;
      var title = (document.querySelector("h1") || {}).textContent || document.title;
      attach(root, { key: "page:" + location.pathname + location.search, title: (title || "").trim().slice(0, 200), url: location.pathname + location.search, starHost: dock });
    }
    penBtn = document.createElement("button");
    penBtn.type = "button"; penBtn.className = "mk-dock-pen"; penBtn.textContent = "🖍"; penBtn.setAttribute("aria-label", "Pink highlighter on or off"); penBtn.setAttribute("aria-pressed", "false");
    penBtn.addEventListener("click", function () { setPen(!pen); });
    dock.appendChild(penBtn);
    undoBtn = document.createElement("button");
    undoBtn.type = "button"; undoBtn.className = "mk-dock-undo off"; undoBtn.textContent = "↶"; undoBtn.setAttribute("aria-label", "Undo last highlight");
    undoBtn.addEventListener("click", undo);
    dock.appendChild(undoBtn);
    var a = document.createElement("a");
    a.className = "mk-dock-saved"; a.href = window.MK_SAVED || "/learn/my-saved/"; a.setAttribute("aria-label", "My saved pages and account"); a.textContent = "📑";
    dock.appendChild(a);
    document.body.appendChild(dock);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", scan); else scan();
})();
