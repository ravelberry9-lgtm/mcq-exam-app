// Highlight / underline / erase / undo and bookmark for Polity cards and question pages.
// Usage: PolityMarks.attach(rootEl, {key, title, url, starHost}). Marks are stored per device on the server
// (with a localStorage copy so they show instantly and survive a lost connection).
(function () {
  "use strict";
  var API = "/learn/my-saved/api";
  var HL = ["yellow", "green", "pink", "blue"], UL = ["red", "green", "purple"];
  var roots = [];            // attached states
  var cur = null;            // state the toolbar is acting on
  var saved = null;          // last non-collapsed selection {st, s, e}
  var tapped = null;         // mark index tapped (for erase)
  var bar, hideT, pinned = false, last = null; // last: selection kept briefly in case a tap clears it (Android)

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

  function selNow() { return saved || (last && Date.now() - last.at < 1500 ? last : null); }
  function addMark(k, c) {
    var sl = selNow();
    if (!sl) { toast("Select some text first, then tap a colour"); return; }
    var st = sl.st, s = sl.s, e = sl.e, txt = st.root.textContent;
    var rest = st.marks.filter(function (m) { return !(m.k === k && m.s < e && m.e > s); }); // same kind replaces overlap
    rest.push({ s: s, e: e, k: k, c: c, t: txt.slice(s, e).replace(/\s+/g, " ").trim().slice(0, 200) });
    rest.sort(function (x, y) { return x.s - y.s; });
    change(st, rest);
    clearSel();
  }
  function erase() {
    var sl = selNow(), st = (sl && sl.st) || cur; if (!st) return;
    var next;
    if (sl) next = st.marks.filter(function (m) { return !(m.s < sl.e && m.e > sl.s); });
    else if (tapped !== null) next = st.marks.filter(function (_, i) { return i !== tapped; });
    else { toast("Select highlighted text (or tap a mark), then tap the eraser"); return; }
    change(st, next); clearSel();
  }
  function undo() {
    var st = cur; if (!st || !st.undo.length) return;
    st.marks = JSON.parse(st.undo.pop()); paint(st); save(st); show(st, false);
  }
  function clearSel() { saved = null; last = null; tapped = null; try { window.getSelection().removeAllRanges(); } catch (e) {} show(cur, false); }

  // ---- toolbar ----
  function build() {
    bar = document.createElement("div");
    bar.className = "mk-ui mk-bar"; bar.hidden = true; bar.setAttribute("role", "toolbar"); bar.setAttribute("aria-label", "Highlight tools");
    var h = "";
    HL.forEach(function (c) { h += '<button type="button" class="mk-sw mk-hl mk-' + c + '" data-k="hl" data-c="' + c + '" aria-label="Highlight ' + c + '"></button>'; });
    h += '<span class="mk-lab" aria-hidden="true"></span>';
    UL.forEach(function (c) { h += '<button type="button" class="mk-sw mk-ulb mk-' + c + '" data-k="ul" data-c="' + c + '" aria-label="Underline ' + c + '"><u>A</u></button>'; });
    h += '<span class="mk-lab" aria-hidden="true"></span>';
    h += '<button type="button" class="mk-tool" data-a="erase" aria-label="Erase"><svg viewBox="0 0 24 24"><path d="M16 3l5 5-11 11H5l-2-2 13-14zM9 19h12"/></svg></button>';
    h += '<button type="button" class="mk-tool" data-a="undo" aria-label="Undo"><svg viewBox="0 0 24 24"><path d="M9 14L4 9l5-5M4 9h10a6 6 0 0 1 0 12h-3"/></svg></button>';
    h += '<button type="button" class="mk-tool" data-a="close" aria-label="Close">✕</button>';
    bar.innerHTML = h;
    // keep the text selection when a button is pressed
    bar.addEventListener("pointerdown", function (e) { e.preventDefault(); });
    bar.addEventListener("mousedown", function (e) { e.preventDefault(); });
    bar.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      if (b.dataset.k) addMark(b.dataset.k, b.dataset.c);
      else if (b.dataset.a === "erase") erase();
      else if (b.dataset.a === "undo") undo();
      else { pinned = false; bar.hidden = true; clearSel(); }
    });
    document.body.appendChild(bar);
  }
  function show(st, sticky) {
    if (!bar) build();
    clearTimeout(hideT);
    if (!st) { if (!pinned) bar.hidden = true; return; }
    cur = st;
    if (sticky) pinned = true;               // once opened, the toolbar stays until ✕ is tapped
    var has = !!saved || tapped !== null;
    bar.classList.toggle("has-sel", has);
    bar.querySelector('[data-a="undo"]').disabled = !st.undo.length;
    bar.hidden = !pinned && !has;
  }

  function stateFor(node) {
    for (var i = 0; i < roots.length; i++) if (roots[i].root.isConnected && roots[i].root.contains(node)) return roots[i];
    return null;
  }
  document.addEventListener("selectionchange", function () {
    var sel = window.getSelection();
    if (!sel || !sel.rangeCount || sel.isCollapsed) { if (saved) { last = { st: saved.st, s: saved.s, e: saved.e, at: Date.now() }; saved = null; show(cur, false); } return; }
    var r = sel.getRangeAt(0), st = stateFor(r.commonAncestorContainer);
    if (!st) return;
    var s = offsetOf(st.root, r.startContainer, r.startOffset), e = offsetOf(st.root, r.endContainer, r.endOffset);
    if (s < 0 || e <= s) return;
    saved = { st: st, s: s, e: e }; tapped = null;
    show(st, true);
  });
  document.addEventListener("click", function (e) {
    var sp = e.target.closest && e.target.closest("span.mk");
    if (!sp || (window.getSelection() && !window.getSelection().isCollapsed)) return;
    var st = stateFor(sp); if (!st) return;
    tapped = +sp.dataset.mi; saved = null; show(st, true);
  });

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
    if (saved && saved.st.root === root) saved = null;
    if (cur && cur.root === root) { cur = null; tapped = null; if (bar) bar.hidden = true; }
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
    var pen = document.createElement("button");
    pen.type = "button"; pen.className = "mk-dock-pen"; pen.textContent = "🖍"; pen.setAttribute("aria-label", "Open highlighter");
    pen.addEventListener("click", function () {
      var st = cur || roots.filter(function (r) { return r.root.isConnected; }).pop();
      if (!st) return;
      if (bar && !bar.hidden && pinned) { pinned = false; bar.hidden = true; return; }
      show(st, true); toast("Select text, then tap a colour");
    });
    dock.appendChild(pen);
    var a = document.createElement("a");
    a.className = "mk-dock-saved"; a.href = window.MK_SAVED || "/learn/my-saved/"; a.setAttribute("aria-label", "My saved pages and account"); a.textContent = "📑";
    dock.appendChild(a);
    document.body.appendChild(dock);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", scan); else scan();
})();
