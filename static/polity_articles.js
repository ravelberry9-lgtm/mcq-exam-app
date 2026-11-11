// Unit 6 recall decks (articles, amendments, cases ...): setup screen -> full-screen card matrix -> full-screen detail view.
// Vanilla JS, no inline handlers. The deck comes from data-* on #ac. Progress: localStorage <data-store> = { cardId: "k" | "x" }
// (articles keeps u6_artcards_v1, unchanged; every other deck has its own key).
(function () {
  "use strict";
  var root = document.getElementById("ac");
  if (!root) return;

  var D = root.dataset;
  var KEY = D.store || "u6_artcards_v1";            // progress
  var LANG_KEY = D.langStore || "u6_artcards_lang"; // older saved language choice
  var SETUP_KEY = D.setupStore || "u6_artcards_setup"; // last setup choices
  var deepLink = false, POS_KEY = SETUP_KEY + "_pos"; // last run: card order + page + open card, for "Continue where you left off"
  var TEXT_FRONT = D.kind === "text";
  var THEMES = D.themes === "1"; // cases: direction B is a theme view (one tile per theme, opened = its cases)
  var LANGS = ["te", "en", "both"];
  var LANG_LABEL = { te: "తె", en: "EN", both: "తె+EN" };
  var LANG_NAME = { te: "Telugu", en: "English", both: "Telugu and English" };
  var GRIDS = { "18": [3, 6], "32": [4, 8] };   // columns x rows for a portrait phone

  var $ = function (id) { return document.getElementById(id); };
  var form = $("ac-setup"), stage = $("ac-stage"), grid = $("ac-grid"), detail = $("ac-detail"), sum = $("ac-sum"), live = $("ac-live");
  // Lazy deck: the page embeds only light tile data (#ac-data JSON). Each card's full detail markup is fetched on open
  // from data-card-url (cached in memory, next / previous prefetched). Stub .ac-src elements carry the tile parts only.
  var DATA = {};
  try { DATA = JSON.parse(($("ac-data") || {}).textContent || "{}"); } catch (e) { DATA = {}; }
  var CARDS = DATA.cards || [], PARTS = DATA.parts || {};
  var info = {}, byId = {};
  function bt(v) { v = v || ["", ""]; return '<span class="ac-te" lang="te">' + esc(v[1] || v[0]) + '</span><span class="ac-en" lang="en">' + esc(v[0]) + "</span>"; }
  function stub(o) {
    var el = document.createElement("article");
    el.className = "ac-src";
    el.dataset.id = o.id; el.dataset.ch = o.ch || ""; el.dataset.acc = o.acc || ""; el.dataset.ink = o.ink || "";
    el.dataset.src = o.src || ""; el.dataset.two = o.two ? "1" : "0";
    if (o.theme) el.dataset.themeTile = "1";
    el.innerHTML = '<div class="s-num">' + esc(o.n) + '</div><div class="s-front">' + bt(o.f) + "</div>" +
      (o.short ? '<div class="s-short">' + bt(o.short) + '</div><div class="s-vs">' + (o.vs ? bt(o.vs) : "") + "</div>" : "") +
      '<div class="s-sub">' + esc(o.s || "") + '</div><div class="s-con">' + bt(o.c) + "</div>" +
      (o.band ? '<div class="s-band">' + bt(o.band) + "</div>" : "") + (o.pop ? '<div class="s-pop">' + bt(o.pop) + "</div>" : "");
    return el;
  }
  CARDS.concat(DATA.themes || []).forEach(function (o) { info[o.id] = o; byId[o.id] = stub(o); });
  var deck = CARDS.map(function (o) { return byId[o.id]; });
  var themeTiles = (DATA.themes || []).map(function (o) { return byId[o.id]; });
  function isTheme(id) { return !!byId[id].dataset.themeTile; }
  function passes(o, c) {
    return (!c.chapter || o.ch === c.chapter) && (c.newer !== false || o.src !== "new") &&
      (!c.parts || !c.parts.length || c.parts.indexOf(o.p) >= 0) && (!c.unit || String(o.u) === String(c.unit)) && (!c.pyq || o.q > 0);
  }
  // ids of a theme tile's cases that pass the run's filters
  function themeRows(src, c) {
    return (info[src.dataset.id].cases || []).filter(function (id) { return info[id] && passes(info[id], c); });
  }

  // ── lazy full cards: in-memory cache + in-flight promises ──
  var full = {}, inflight = {};
  function cardUrl(id) { return (D.cardUrl || "").replace("__ID__", encodeURIComponent(id)) + (DATA.v ? "?v=" + DATA.v : ""); }
  function load(id) {
    if (full[id]) return Promise.resolve(full[id]);
    if (inflight[id]) return inflight[id];
    inflight[id] = fetch(cardUrl(id), { credentials: "same-origin" }).then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.text();
    }).then(function (html) {
      var box = document.createElement("div");
      box.innerHTML = html;
      var el = box.querySelector(".ac-src");
      if (!el) throw new Error("bad card");
      full[id] = el;
      delete inflight[id];
      return el;
    }, function (err) { delete inflight[id]; throw err; });
    return inflight[id];
  }
  function prefetch(id) { if (id && !full[id] && !inflight[id]) load(id).catch(function () { /* retried on open */ }); }

  var progress = readJSON(KEY);
  var run = null; // { base, ids, order, page, cur, marks:{}, mode, lang, density, chapter }
  var ORDERS = ["seq", "rand"];
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ── storage: private mode / blocked storage must never break the page ──
  function readJSON(key) {
    try { return JSON.parse(localStorage.getItem(key) || "{}") || {}; } catch (e) { return {}; }
  }
  function writeJSON(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); } catch (e) { /* ignore */ }
  }
  function readRaw(key) {
    try { return localStorage.getItem(key); } catch (e) { return null; }
  }

  // ── small helpers ──
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (ch) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[ch]; });
  }
  function biText(en, te) {
    return '<span class="ac-te" lang="te">' + te + '</span><span class="ac-en" lang="en">' + en + "</span>";
  }
  function num(id) { return byId[id].querySelector(".s-num").textContent.trim(); }
  function frontEn(id) { return byId[id].querySelector(".s-front .ac-en").textContent.trim(); }
  function sub(id) { return byId[id].querySelector(".s-sub").textContent.trim(); }
  function conceptEn(id) { return byId[id].querySelector(".s-con .ac-en").textContent.trim(); }
  var anyTwoWay = deck.some(function (s) { return s.dataset.two === "1"; });
  function canB(id) { return byId[id].dataset.two === "1"; }
  function shuffled(list) {
    var a = list.slice();
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }

  // ── setup screen ──
  function choices() {
    var f = form.elements;
    return {
      chapter: f.chapter && f.chapter.checked ? f.chapter.value : "", parts: pickedParts(), unit: f.unit.value, mode: f.mode.value, lang: f.lang.value, density: f.density.value,
      only: f.only.checked, order: f.order.value, newer: f.newer ? f.newer.checked : true, pyq: f.pyq ? f.pyq.checked : false
    };
  }
  function pickedParts() {
    return [].filter.call(form.querySelectorAll('input[name="part"]'), function (i) { return i.checked; }).map(function (i) { return i.value; });
  }
  // Part chips: 'All' is on exactly when no single Part is picked
  function onPartChange(e) {
    var t = e.target;
    if (t.name === "partall") {
      if (t.checked) [].forEach.call(form.querySelectorAll('input[name="part"]'), function (i) { i.checked = false; });
      else if (!pickedParts().length) t.checked = true;
    } else if (t.name === "part") form.elements.partall.checked = !pickedParts().length;
  }
  function setRadio(name, value) {
    var r = form.querySelector('input[name="' + name + '"][value="' + value + '"]');
    if (r) r.checked = true;
  }
  function restoreChoices() {
    var saved = readJSON(SETUP_KEY);
    var urlChapter = root.dataset.chapter, langFromUrl = root.dataset.langSet === "1";
    if (!urlChapter && Array.isArray(saved.parts)) {
      [].forEach.call(form.querySelectorAll('input[name="part"]'), function (i) { i.checked = saved.parts.indexOf(i.value) >= 0; });
      form.elements.partall.checked = !pickedParts().length;
    }
    if (!urlChapter && saved.unit) { var ur = form.querySelector('input[name="unit"][value="' + saved.unit + '"]'); if (ur && !ur.disabled) ur.checked = true; }
    if (/^[ab]$/.test(saved.mode) && (saved.mode === "a" || anyTwoWay)) setRadio("mode", saved.mode);
    if (form.elements.newer && saved.newer === false) form.elements.newer.checked = false;
    if (GRIDS[saved.density]) setRadio("density", saved.density);
    var lang = saved.lang || readRaw(LANG_KEY);
    if (!langFromUrl && LANGS.indexOf(lang) >= 0) setRadio("lang", lang);
    form.elements.only.checked = !!saved.only;
    if (form.elements.pyq) form.elements.pyq.checked = !!saved.pyq;
    var order = ORDERS.indexOf(saved.order) >= 0 ? saved.order : saved.shuffle ? "rand" : "seq"; // older saves had a Shuffle toggle
    setRadio("order", order);
  }
  function saveChoices() {
    var c = choices();
    if (run) { c.mode = run.mode; c.lang = run.lang; c.order = run.order; }
    writeJSON(SETUP_KEY, c);
  }
  function pickIds(c) {
    if (THEMES && c.mode === "b") {
      return themeTiles.filter(function (s) {
        return themeRows(s, c).length && (!c.only || progress[s.dataset.id] === "x");
      }).map(function (s) { return s.dataset.id; });
    }
    return CARDS.filter(function (o) {
      return passes(o, c) && (!c.only || progress[o.id] === "x") && (c.mode !== "b" || o.two);
    }).map(function (o) { return o.id; });
  }
  function countState(ids, v) {
    return ids.filter(function (id) { return progress[id] === v; }).length;
  }
  // "More options" summary: one line naming what the folded options are set to
  var MORE_KEY = SETUP_KEY + "_more";
  function paintMore(c) {
    var el = $("ac-more-sum");
    if (!el) return;
    var L = { te: ["తెలుగు", "Telugu"], en: ["ఇంగ్లీష్", "English"], both: ["రెండూ", "Both"] }[c.lang] || ["", ""];
    var te = [c.density === "32" ? "4×8" : "3×6", L[0], c.order === "rand" ? "కలగలుపు" : "వరుసగా"], en = [c.density === "32" ? "4×8" : "3×6", L[1], c.order === "rand" ? "Random" : "In order"];
    if (c.only) { te.push("మళ్ళీ చూడాల్సినవి"); en.push("Revise only"); }
    if (form.elements.newer && !c.newer) { te.push("కొత్తవి లేకుండా"); en.push("No newer"); }
    if (c.pyq) { te.push("PYQ వచ్చినవి"); en.push("PYQ cards"); }
    el.innerHTML = biText(esc(en.join(", ")), esc(te.join(", ")));
  }
  function paintSetup() {
    var c = choices();
    paintMore(c);
    root.dataset.lang = c.lang;
    var inChapter = pickIds({ chapter: c.chapter, parts: c.parts, unit: c.unit, only: false, newer: c.newer, pyq: c.pyq });
    // Part counts follow the unit / chapter / newer filters
    [].forEach.call(form.querySelectorAll("[data-pcount]"), function (el) {
      var p = el.dataset.pcount;
      el.textContent = CARDS.filter(function (o) { return passes(o, { chapter: c.chapter, unit: c.unit, newer: c.newer, pyq: c.pyq, parts: p ? [p] : [] }); }).length;
      el.closest(".ac-part").classList.toggle("none", el.textContent === "0");
    });
    var ids = pickIds(c);
    var k = countState(inChapter, "k"), x = countState(inChapter, "x");
    $("ac-xcount").textContent = x ? " (" + x + ")" : "";
    var unit = THEMES && c.mode === "b" ? ["theme", "themes"] : ["card", "cards"];
    $("ac-start-n").textContent = ids.length + " " + unit[ids.length === 1 ? 0 : 1];
    $("ac-start").disabled = !ids.length;
    $("ac-saved").textContent = (k || x) ? "Saved on this device: " + k + " known, " + x + " to revise" : "";
    var msg = $("ac-msg");
    msg.hidden = ids.length > 0;
    msg.textContent = ids.length ? "" : "No cards here are marked Revise yet. Turn off ‘Only cards to revise’ to study them all.";
    var pc = c.parts.length === 1 && PARTS[c.parts[0]];
    form.style.setProperty("--acc", pc ? pc[2] : "#0F766E");
    form.style.setProperty("--acc-ink", pc ? pc[3] : "#5EEAD4");
  }
  function resetProgress() {
    if (!window.confirm("Reset all " + (D.title || "").toLowerCase() + " card progress?\nపురోగతి మొత్తం రీసెట్ చేయాలా?")) return;
    progress = {};
    writeJSON(KEY, progress);
    paintSetup();
  }
  function onStart(e) {
    e.preventDefault();
    var c = choices();
    writeJSON(SETUP_KEY, c);
    startRun(pickIds(c), c);
  }

  // ── run lifecycle ──
  // ids always arrive in the server's order: one ascending article sequence (natural sort, article_cards.article_key),
  // across chapters when All is picked. In order uses it as is; Random shuffles a copy. Never re-sorted here.
  function savePos() {
    if (!run || deepLink) return; // a deep link (?open=) is a detour, not a study session
    writeJSON(POS_KEY, { ids: run.ids, base: run.base, page: run.page, cur: run.cur, t: Date.now(),
      c: { chapter: run.chapter, parts: run.parts, unit: run.unit, mode: run.mode, lang: run.lang, density: run.density, order: run.order, only: run.only, newer: run.newer, pyq: run.pyq } });
  }
  function savedPos() {
    var p = readJSON(POS_KEY);
    if (!Array.isArray(p.ids) || !p.c) return null;
    var ids = p.ids.filter(function (id) { return byId[id]; });
    return ids.length ? { ids: ids, base: (p.base || ids).filter(function (id) { return byId[id]; }), page: +p.page || 0, cur: +p.cur, c: p.c } : null;
  }
  function paintContinue() {
    var p = savedPos(), b = $("ac-cont");
    b.hidden = !p;
    if (!p) return;
    var pages = Math.max(1, Math.ceil(p.ids.length / (+p.c.density || 18)));
    $("ac-cont-n").textContent = p.cur >= 0 ? "Card " + (p.cur + 1) + " of " + p.ids.length : "Page " + (Math.min(p.page, pages - 1) + 1) + " of " + pages + " · " + p.ids.length + " cards";
  }
  function continueRun() {
    var p = savedPos();
    if (!p) return;
    startRun(p.ids, Object.assign({}, p.c, { order: "seq" }));
    run.order = p.c.order === "rand" ? "rand" : "seq"; run.base = p.base.length ? p.base : p.ids.slice();
    run.page = Math.min(Math.max(0, p.page), pageCount() - 1);
    renderMatrix();
    var i = p.cur >= 0 && p.cur < run.ids.length ? p.cur : run.page * perPage();
    focusTile(i);
    if (p.cur >= 0 && p.cur < run.ids.length) openDetail(i);
  }
  function startRun(ids, c) {
    if (!ids.length) return;
    var order = c.order === "rand" ? "rand" : "seq";
    run = {
      all: c.all || pickIds({ chapter: c.chapter, parts: c.parts, unit: c.unit, only: c.only, newer: c.newer, pyq: c.pyq, mode: "a" }),
      base: ids.slice(), ids: order === "rand" ? shuffled(ids) : ids.slice(), order: order, page: 0, cur: -1, marks: {},
      mode: c.mode, lang: c.lang, density: c.density || "18", chapter: c.chapter || "", parts: (c.parts || []).slice(), unit: c.unit || "", only: !!c.only, newer: c.newer !== false, pyq: !!c.pyq
    };
    sum.hidden = true;
    detail.hidden = true;
    openStage();
    renderMatrix();
    focusTile(0);
    savePos();
  }
  function openStage() {
    if (stage.parentNode !== document.body) document.body.appendChild(stage);
    stage.hidden = false;
    document.documentElement.classList.add("ac-studying");
    var app = document.querySelector(".app");
    if (app) app.inert = true;
    if (!history.state || !history.state.acStudy) history.pushState({ acStudy: 1 }, "");
  }
  function closeStage() {
    stage.hidden = true;
    detail.hidden = true;
    sum.hidden = true;
    document.documentElement.classList.remove("ac-studying");
    var app = document.querySelector(".app");
    if (app) app.inert = false;
    if (run) { setRadio("order", run.order); setRadio("mode", run.mode); setRadio("lang", run.lang); }
    run = null;
    paintSetup();
    paintContinue();
    $("ac-start").focus({ preventScroll: true });
  }
  function exitStudy() {
    if (FOR && BACK) { location.href = BACK.url; return; } // ?for= matrix: Back returns to the card it came from
    if (history.state && history.state.acDetail) { history.go(-2); return; }
    if (history.state && history.state.acStudy) history.back(); // popstate closes the stage
    else closeStage();
  }
  function onPop() {
    if (stage.hidden) return;
    var st = history.state || {};
    if (!detail.hidden && !st.acDetail) hideDetail();
    if (!st.acStudy) closeStage();
  }

  // ── matrix ──
  function perPage() { return +run.density; }
  function pageCount() { return Math.max(1, Math.ceil(run.ids.length / perPage())); }
  // Portrait phones use columns x rows; wide screens swap them. Pick whichever gives tiles closest to a soft square.
  function gridShape() {
    var g = GRIDS[run.density], w = grid.clientWidth || window.innerWidth, h = grid.clientHeight || (window.innerHeight - 44);
    var a = (w / g[0]) / (h / g[1]), b = (w / g[1]) / (h / g[0]);
    var fit = function (r) { return Math.abs(Math.log(r / 1.15)); };
    return fit(a) <= fit(b) ? { cols: g[0], rows: g[1] } : { cols: g[1], rows: g[0] };
  }
  function applyShape() {
    var s = gridShape();
    grid.style.setProperty("--cols", s.cols);
    grid.style.setProperty("--rows", s.rows);
    grid.dataset.density = run.density;
  }
  function tileHTML(id, index) {
    var src = byId[id], state = progress[id] || "";
    var n = num(id), stateText = state === "k" ? "known" : state === "x" ? "to revise" : "not marked yet";
    var sb = sub(id);
    var band = src.querySelector(".s-band");
    var label = (run.mode === "a" ? frontEn(id) + (sb ? " " + sb : "") : conceptEn(id)) + (band ? "" : ", chapter " + src.dataset.ch) +
      (info[id] && info[id].q ? ", " + info[id].q + " PYQs" : "") + ", " + stateText;
    var cue;
    if (isTheme(id)) {
      var n = themeRows(src, run).length;
      label = "Theme: " + conceptEn(id) + ", " + n + " cases, " + stateText;
      cue = '<span class="t-front">' + src.querySelector(".s-front").innerHTML + '<span class="t-sub">' + biText(n + " cases", n + " కేసులు") + "</span></span>";
    } else if (run.mode === "b") cue = '<span class="t-con">' + src.querySelector(".s-con").innerHTML + "</span>";
    else if (src.querySelector(".s-short")) {
      var vsEl = src.querySelector(".s-vs");
      cue = '<span class="t-front t-case"><span class="t-p1">' + src.querySelector(".s-short").innerHTML + "</span>" +
        (vsEl && vsEl.textContent.trim() ? '<span class="t-vs">' + vsEl.innerHTML + "</span>" : "") + (sb ? '<span class="t-sub">' + esc(sb) + "</span>" : "") + popHTML(src) + "</span>";
    }
    else if (TEXT_FRONT) cue = '<span class="t-front">' + src.querySelector(".s-front").innerHTML + (sb ? '<span class="t-sub">' + esc(sb) + "</span>" : "") + popHTML(src) + "</span>";
    else if (sb && D.deck !== "articles") cue = '<span class="t-numwrap"><b class="t-num" style="--len:' + Math.max(3, n.length) + '">' + esc(n) + '</b><span class="t-sub">' + esc(sb) + "</span></span>";
    else cue = '<b class="t-num" style="--len:' + Math.max(3, n.length) + '">' + esc(n) + "</b>";
    return '<button type="button" class="ac-tile" data-i="' + index + '" data-state="' + state + '" style="--acc:' + src.dataset.acc + ';--acc-ink:' + (src.dataset.ink || '') +
      '" aria-label="' + esc(label) + '"><span class="t-ch' + (band ? " t-band" : "") + '" aria-hidden="true">' + (band ? band.innerHTML : src.dataset.ch) +
      '</span><span class="t-mark" aria-hidden="true"></span><span class="t-cue">' + cue + "</span>" +
      (info[id] && info[id].q ? '<span class="t-pyq" aria-hidden="true">PYQ ' + info[id].q + "</span>" : "") + "</button>";
  }
  // popular name ('Cross Roads case') under the year: 3 x 6 only, and fitTiles drops it when it would shrink the cue
  function popHTML(src) {
    var p = src.querySelector(".s-pop");
    return p && run.density === "18" ? '<span class="t-pop">' + p.innerHTML + "</span>" : "";
  }
  function renderMatrix() {
    stage.dataset.lang = run.lang;
    stage.dataset.mode = run.mode;
    stage.dataset.kind = (run.mode === "a" || THEMES) && TEXT_FRONT ? "text" : run.mode === "a" ? "num" : "cue";
    stage.dataset.themes = THEMES ? "1" : "";
    stage.dataset.one = run.chapter ? "1" : "";
    applyShape();
    var start = run.page * perPage(), html = "";
    for (var i = start; i < start + perPage(); i++) {
      html += i < run.ids.length ? tileHTML(run.ids[i], i) : '<span class="ac-slot" aria-hidden="true"></span>';
    }
    grid.innerHTML = html;
    paintBar();
    fitTiles();
  }
  // One colour slice per chapter in the run, for the "All" chip's dot.
  function chapterDots(ids) {
    var seen = {}, cols = [];
    ids.forEach(function (id) { var s = byId[id]; if (!seen[s.dataset.ch]) { seen[s.dataset.ch] = 1; cols.push(s.dataset.acc); } });
    if (cols.length < 2) return cols[0] || "#0f766e";
    var step = 360 / cols.length;
    return "conic-gradient(" + cols.map(function (c, i) { return c + " " + (i * step) + "deg " + ((i + 1) * step) + "deg"; }).join(",") + ")";
  }
  function paintBar() {
    var pages = pageCount(), ids = run.ids;
    var where = $("ac-where");
    var pl = run.parts.map(function (p) { return p.replace(/^Part /, ""); });
    if (FOR) {
      where.innerHTML = '<span class="w-chip w-for">' + biText(esc(FOR.en), esc(FOR.te)) + "</span>";
      where.setAttribute("aria-label", "Linked to " + FOR.en);
    } else if (run.chapter) {
      where.innerHTML = '<span class="w-chip">' + esc(run.chapter) + "</span>";
      where.setAttribute("aria-label", "Chapter " + run.chapter);
    } else if (pl.length) {
      var p0 = PARTS[run.parts[0]] || [];
      where.innerHTML = '<span class="w-chip w-part" style="--pc:' + (run.parts.length === 1 ? p0[2] : "var(--ink)") + '">' +
        esc(pl.length > 2 ? pl.slice(0, 2).join(" · ") + " +" + (pl.length - 2) : pl.join(" · ")) + "</span>";
      where.setAttribute("aria-label", (run.parts.length === 1 ? "" : "Parts ") + run.parts.join(", "));
    } else if (run.unit) {
      where.innerHTML = '<span class="w-chip">' + biText("Unit " + esc(run.unit), "యూనిట్ " + esc(run.unit)) + "</span>";
      where.setAttribute("aria-label", "Unit " + run.unit);
    } else {
      where.innerHTML = '<span class="w-chip all" style="--dots:' + chapterDots(ids) + '"><i class="w-dot" aria-hidden="true"></i><span class="w-txt">' +
        biText("All", "అన్ని") + "</span></span>";
      where.setAttribute("aria-label", "All chapters");
    }
    stage.style.setProperty("--acc", run.chapter ? byId[ids[0]].dataset.acc : "#0F766E");
    stage.style.setProperty("--acc-ink", run.chapter ? byId[ids[0]].dataset.ink : "#5EEAD4");
    $("ac-pager").hidden = pages < 2;
    $("ac-page").textContent = (run.page + 1) + "/" + pages;
    $("ac-pprev").disabled = run.page === 0;
    $("ac-pnext").disabled = run.page >= pages - 1;
    var modeBtn = $("ac-mode");
    modeBtn.setAttribute("aria-pressed", run.mode === "b" ? "true" : "false");
    modeBtn.hidden = !anyTwoWay;
    modeBtn.setAttribute("aria-label", run.mode === "a" ? "Showing the card fronts. Show the ideas instead" : "Showing the ideas. Show the card fronts instead");
    var rand = run.order === "rand", orderBtn = $("ac-order");
    stage.dataset.order = run.order;
    orderBtn.setAttribute("aria-pressed", rand ? "true" : "false");
    orderBtn.setAttribute("aria-label", rand ? "Cards in random order. Switch to " + (D.orderEn || "In order").toLowerCase() : "Cards " + (D.orderEn || "in order").toLowerCase() + ". Switch to random order");
    $("ac-reshuffle").hidden = !rand;
    var langBtn = $("ac-lang");
    langBtn.textContent = LANG_LABEL[run.lang];
    langBtn.setAttribute("aria-label", "Language: " + LANG_NAME[run.lang] + ". Change language");
    var k = countState(ids, "k"), x = countState(ids, "x"), meter = $("ac-meter");
    meter.style.setProperty("--k", (k / ids.length * 100) + "%");
    meter.style.setProperty("--x", (x / ids.length * 100) + "%");
  }
  // Shrink concept cues until they fit; tiles on one page share a size (the median fit) so the matrix reads evenly.
  // An ellipsis clamp is used only when a cue cannot fit even at the minimum size.
  var MIN_FS = 11;
  function fitTiles() {
    if (!run || (run.mode !== "b" && !TEXT_FRONT)) return;
    var boxes = [].slice.call(grid.querySelectorAll(".t-cue"));
    if (!boxes.length) return;
    var b0 = boxes[0];
    var max = run.mode === "a" || THEMES ? Math.max(13, Math.min(30, Math.round(Math.min(b0.clientWidth / 5.5, b0.clientHeight / 3.2))))
      : Math.max(13, Math.min(26, Math.round(Math.min(b0.clientWidth / 6.5, b0.clientHeight / 4))));
    var fits = boxes.map(function (box) {
      var fs = fitOne(box, max), pop = box.querySelector(".t-pop");
      if (!pop) return fs;
      var hold = pop.parentNode, next = pop.nextSibling;
      hold.removeChild(pop);
      var bare = fitOne(box, max);
      if (bare > fs || box.classList.contains("clamp")) return bare; // never crowd: keep the name only when the cue keeps its size
      hold.insertBefore(pop, next);
      return fitOne(box, max);
    });
    var sorted = fits.slice().sort(function (a, b) { return a - b; });
    var common = sorted[Math.floor(sorted.length / 2)];
    boxes.forEach(function (box, i) { if (fits[i] > common) fitOne(box, common); });
  }
  function fitOne(box, max) {
    var con = box.firstChild, h = box.clientHeight;
    box.classList.remove("no-en", "clamp");
    con.style.removeProperty("--clamp");
    if (!h) return max;
    for (var pass = 0; pass < 2; pass++) {
      for (var fs = max; fs >= MIN_FS; fs--) {
        box.style.fontSize = fs + "px";
        if (con.scrollHeight <= h + 1 && con.scrollWidth <= box.clientWidth + 1) return fs;
      }
      if (run.lang !== "both" || pass) break;
      box.classList.add("no-en"); // drop the English line before clamping Telugu
    }
    box.classList.add("clamp");
    con.style.setProperty("--clamp", Math.max(1, Math.floor(h / (MIN_FS * 1.4))));
    return MIN_FS;
  }
  function goPage(step) {
    var p = run.page + step;
    if (p < 0 || p >= pageCount()) return;
    run.page = p;
    renderMatrix();
    savePos();
    live.textContent = "Page " + (p + 1) + " of " + pageCount();
  }
  function focusTile(index) {
    var t = grid.querySelector('.ac-tile[data-i="' + index + '"]') || grid.querySelector(".ac-tile");
    if (t) t.focus({ preventScroll: true });
  }
  // Direction B shows only two-way cards (a cue that maps to exactly one front); switching re-filters and keeps marks.
  function toggleMode() {
    if (!anyTwoWay) return;
    var mode = run.mode === "a" ? "b" : "a";
    var ids = THEMES ? pickIds({ chapter: run.chapter, parts: run.parts, unit: run.unit, only: run.only, newer: run.newer, pyq: run.pyq, mode: mode })
      : run.all.filter(function (id) { return mode === "a" || canB(id); });
    if (!ids.length) { toast("No two-way cards here", "ఇక్కడ రెండు వైపుల కార్డులు లేవు"); return; }
    if (THEMES) toast(mode === "b" ? "Theme → Cases" : "Case → Issue", mode === "b" ? "అంశం → కేసులు" : "కేసు → అంశం");
    if (THEMES || ids.length !== run.base.length) {
      run.base = ids;
      run.ids = run.order === "rand" ? shuffled(ids) : ids.slice();
      run.page = 0;
      if (mode === "b" && !THEMES) toast(ids.length + " two-way cards", ids.length + " రెండు వైపుల కార్డులు");
    }
    run.mode = mode;
    saveChoices();
    renderMatrix();
  }
  function cycleLang() {
    run.lang = LANGS[(LANGS.indexOf(run.lang) + 1) % LANGS.length];
    detail.dataset.lang = run.lang;
    saveChoices();
    renderMatrix();
    live.textContent = "Language: " + LANG_NAME[run.lang];
  }

  // Order <-> Random. Switching (or reshuffling) keeps every mark, since marks are per card id, and starts again at page 1.
  var toastTimer = 0;
  function toast(en, te) {
    var t = $("ac-toast");
    t.innerHTML = biText(en, te);
    t.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { t.hidden = true; }, 1600);
  }
  function setOrder(order) {
    run.order = order;
    run.ids = order === "rand" ? shuffled(run.base) : run.base.slice();
    run.page = 0;
    run.cur = -1;
    saveChoices();
    renderMatrix();
    grid.scrollTop = 0;
  }
  function toggleOrder() {
    var rand = run.order !== "rand";
    setOrder(rand ? "rand" : "seq");
    if (rand) toast("Random order", "యాదృచ్ఛిక క్రమం"); else toast(D.orderEn || "In order", D.orderTe || "క్రమంగా");
    live.textContent = rand ? "Cards shuffled into random order" : "Cards back in order";
  }
  function reshuffle() {
    setOrder("rand");
    toast("Reshuffled", "మళ్ళీ కలిపాం");
    live.textContent = "Cards reshuffled";
    $("ac-reshuffle").focus({ preventScroll: true });
  }

  // ── detail view ──
  function fillDetail(index) {
    var id = run.ids[index], n = esc(num(id));
    run.cur = index;
    savePos();
    $("ac-pos").textContent = (index + 1) + " / " + run.ids.length;
    $("ac-prev").disabled = index === 0;
    $("ac-next").disabled = index >= run.ids.length - 1;
    var src = full[id];
    if (!src) { paintLoading(index); return; }
    detail.removeAttribute("aria-busy");
    detail.dataset.loading = "";
    detail.style.setProperty("--acc", src.dataset.acc);
    detail.style.setProperty("--acc-ink", src.dataset.ink);
    detail.dataset.lang = run.lang;
    detail.dataset.state = progress[id] || "";
    var topic = src.querySelector(".s-topic"), heroX = src.querySelector(".s-hero");
    $("ac-dchap").innerHTML = src.querySelector(".s-chap").innerHTML + (topic ? " " + topic.innerHTML : "");
    var sb = esc(sub(id)), pill = isTheme(id) ? biText("Theme", "అంశం") : biText(D.pillEn || "Article", D.pillTe || "ప్రకరణ");
    var pEl = src.querySelector(".s-parties"), sameName = pEl && frontEn(id) === pEl.querySelector(".ac-en").textContent.trim();
    var head = pEl
      ? '<span class="ac-pill txt ac-case"><small>' + pill + '</small><span class="p-parties">' + pEl.innerHTML + "</span>" +
        (sameName ? "" : '<span class="p-short">' + src.querySelector(".s-front").innerHTML + "</span>") + (sb ? '<span class="p-sub">' + sb + "</span>" : "") + "</span>"
      : TEXT_FRONT
      ? '<span class="ac-pill txt"><small>' + pill + "</small>" + src.querySelector(".s-front").innerHTML + (sb ? '<span class="p-sub">' + sb + "</span>" : "") + "</span>"
      : '<span class="ac-pill"><small>' + pill + "</small>" + n + (sb && D.deck !== "articles" ? '<span class="p-sub">' + sb + "</span>" : "") + "</span>";
    var popl = src.querySelector(".s-popline");
    $("ac-dtitle").innerHTML = head + (popl ? '<div class="ch-hero">' + popl.innerHTML + "</div>" : "") + (isTheme(id) ? "" : '<span class="ac-anstext">' + src.querySelector(".s-title").innerHTML + "</span>") +
      (heroX ? '<div class="ch-hero">' + heroX.innerHTML + "</div>" : "");
    $("ac-dbody").innerHTML = src.querySelector(".s-back").innerHTML;
    detail.dataset.theme = isTheme(id) ? "1" : "";
    if (isTheme(id)) {
      var keep = themeRows(src, run);
      [].forEach.call($("ac-dbody").querySelectorAll(".ac-thlist li"), function (li) { if (keep.indexOf(li.dataset.id) < 0) li.remove(); });
    }
    // chain timeline: a step can jump only to a card that is in this run
    [].forEach.call($("ac-dbody").querySelectorAll("[data-jump]"), function (b) {
      if (run.ids.indexOf(b.dataset.jump) < 0) { b.disabled = true; b.removeAttribute("data-jump"); }
    });
    $("ac-dscroll").scrollTop = 0;
    live.textContent = frontEn(id) + ", card " + (index + 1) + " of " + run.ids.length;
    prefetch(run.ids[index + 1]);
    prefetch(run.ids[index - 1]);
  }
  // Not fetched yet: show the card face at once (front + cue from the light data), then fill when it arrives.
  function paintLoading(index, failed) {
    var id = run.ids[index], src = byId[id];
    detail.style.setProperty("--acc", src.dataset.acc);
    detail.style.setProperty("--acc-ink", src.dataset.ink);
    detail.dataset.lang = run.lang;
    detail.dataset.state = progress[id] || "";
    detail.dataset.loading = failed ? "fail" : "1";
    detail.setAttribute("aria-busy", failed ? "false" : "true");
    $("ac-dchap").innerHTML = "";
    var sb = sub(id);
    $("ac-dtitle").innerHTML = '<span class="ac-pill txt"><small>' + (isTheme(id) ? biText("Theme", "అంశం") : biText(D.pillEn || "Article", D.pillTe || "ప్రకరణ")) + "</small>" +
      src.querySelector(".s-front").innerHTML + (sb ? '<span class="p-sub">' + esc(sb) + "</span>" : "") + "</span>" +
      '<span class="ac-anstext">' + src.querySelector(".s-con").innerHTML + "</span>";
    $("ac-dbody").innerHTML = failed
      ? '<div class="ac-lfail" role="alert"><p>' + biText("This card did not load. Check your connection and try again.", "ఈ కార్డు లోడ్ కాలేదు. ఇంటర్నెట్ చూసి మళ్ళీ ప్రయత్నించండి.") +
        '</p><button type="button" class="ac-ghost" data-retry="1">' + biText("Try again", "మళ్ళీ ప్రయత్నించండి") + "</button></div>"
      : '<div class="ac-lbones" aria-hidden="true"><i></i><i></i><i></i><i></i><i class="s"></i></div>';
    $("ac-dscroll").scrollTop = 0;
    if (failed) return;
    load(id).then(function () {
      if (run && run.ids[run.cur] === id) fillDetail(run.cur);
    }, function () {
      if (run && run.ids[run.cur] === id) paintLoading(run.cur, true);
    });
  }
  function tileRect(index) {
    var t = grid.querySelector('.ac-tile[data-i="' + index + '"]');
    return t && !stage.hidden ? t.getBoundingClientRect() : null;
  }
  function clipFrom(r) {
    var W = window.innerWidth, H = window.innerHeight;
    return "inset(" + r.top + "px " + (W - r.right) + "px " + (H - r.bottom) + "px " + r.left + "px round 12px)";
  }
  function animateClip(from, to, done) {
    if (reduceMotion || !detail.animate) { if (done) done(); return; }
    var a = detail.animate([{ clipPath: from }, { clipPath: to }], { duration: 260, easing: "cubic-bezier(.2,.7,.2,1)" });
    a.onfinish = done || null;
  }
  function openDetail(index) {
    fillDetail(index);
    detail.hidden = false;
    var r = tileRect(index);
    if (r) animateClip(clipFrom(r), "inset(0px 0px 0px 0px round 0px)");
    if (!history.state || !history.state.acDetail) history.pushState({ acStudy: 1, acDetail: 1 }, "");
    $("ac-collapse").focus({ preventScroll: true });
  }
  function collapse() {
    if (history.state && history.state.acDetail) history.back(); // popstate hides the detail
    else hideDetail();
  }
  function hideDetail() {
    backStack = []; bootBack = false; paintBack();
    var index = run.cur;
    var page = Math.floor(index / perPage());
    if (page !== run.page) run.page = page;
    run.cur = -1; savePos(); run.cur = index;
    renderMatrix();
    var r = tileRect(index);
    var finish = function () {
      detail.hidden = true;
      if (!run) return;
      focusTile(index);
      if (Object.keys(run.marks).length === run.ids.length) showSummary();
    };
    if (r) animateClip("inset(0px 0px 0px 0px round 0px)", clipFrom(r), finish); else finish();
  }
  function jumpTo(id) {
    var i = run.ids.indexOf(id);
    if (i >= 0 && i !== run.cur) step(i - run.cur);
  }
  function step(d) {
    var i = run.cur + d;
    if (i < 0 || i >= run.ids.length) return;
    fillDetail(i);
    var body = $("ac-dscroll");
    if (!reduceMotion && body.animate) body.animate([{ opacity: 0, transform: "translateX(" + (Math.sign(d) * 24) + "px)" }, { opacity: 1, transform: "none" }], { duration: 180, easing: "ease-out" });
  }
  function nav(d) { backStack = []; bootBack = false; step(d); paintBack(); }
  function judge(value) {
    var id = run.ids[run.cur];
    progress[id] = value;
    writeJSON(KEY, progress);
    run.marks[id] = value;
    detail.dataset.state = value;
    collapse();
  }

  // Cases practice MCQ: one try, then the right option turns green, a wrong pick red, and the reason shows.
  function answerPractice(b) {
    var box = b.closest(".ct-prac");
    if (!box || box.dataset.done) return;
    var ans = box.dataset.ans, ok = b.dataset.opt === ans;
    box.dataset.done = ok ? "ok" : "no";
    [].forEach.call(box.querySelectorAll(".ct-opt"), function (o) {
      o.disabled = true;
      if (o.dataset.opt === ans) o.dataset.res = "ok"; else if (o === b) o.dataset.res = "no";
    });
    var why = box.querySelector(".ct-why");
    why.insertAdjacentHTML("afterbegin", "<b>" + (ok ? biText("Correct", "సరైనది") : biText("Not quite", "సరైనది కాదు")) + "</b>");
    why.hidden = false;
    live.textContent = ok ? "Correct" : "Wrong. The answer is option " + "ABCD".charAt(ans - 1);
  }

  // ── summary ──
  function showSummary() {
    var k = 0, x = 0;
    Object.keys(run.marks).forEach(function (id) { if (run.marks[id] === "k") k++; else x++; });
    sum.querySelector('[data-n="k"]').textContent = k;
    sum.querySelector('[data-n="x"]').textContent = x;
    var missed = sum.querySelector('[data-act="missed"]');
    missed.hidden = !x;
    sum.hidden = false;
    live.textContent = "All cards marked: " + k + " known, " + x + " to revise";
    (x ? missed : sum.querySelector('[data-act="back"]')).focus({ preventScroll: true });
  }
  function reviseMissed() {
    var ids = run.base.filter(function (id) { return run.marks[id] === "x"; });
    startRun(ids, { order: run.order, mode: run.mode, lang: run.lang, density: run.density, chapter: run.chapter, parts: run.parts, unit: run.unit, all: ids.slice() });
  }
  function dismissSummary() {
    sum.hidden = true;
    run.marks = {}; // looking again starts a fresh tally
    focusTile(run.page * perPage());
  }

  // ── events ──
  var actions = {
    "ac-exit": exitStudy, "ac-mode": toggleMode, "ac-lang": cycleLang, "ac-order": toggleOrder, "ac-reshuffle": reshuffle,
    "ac-pprev": function () { goPage(-1); }, "ac-pnext": function () { goPage(1); },
    "ac-collapse": collapse, "ac-prev": function () { nav(-1); }, "ac-next": function () { nav(1); }
  };
  // ── interlinking: .xl links and Related chips open a card; same deck in place (with a back stack), other decks by URL ──
  var backStack = [];
  var BACK = D.backUrl ? { url: D.backUrl, deck: D.backDeck, en: D.backEn, te: D.backTe } : null;
  var FOR = D.forId ? { id: D.forId, ids: (D.forIds || "").split(",").filter(function (x) { return x && byId[x]; }), en: D.forEn, te: D.forTe } : null;
  var bootBack = false; // this page was opened from another deck's card and still shows that first card
  function frontTe(id) { var e = byId[id].querySelector(".s-front .ac-te"); return e ? e.textContent.trim() : frontEn(id); }
  function showCard(id) {
    var i = run.ids.indexOf(id);
    if (i < 0) { run.ids.push(id); i = run.ids.length - 1; } // linked card outside this run's filter: visit it at the end
    step(i - run.cur);
    paintBack();
  }
  function go(id, href) {
    var cur = run && run.cur >= 0 ? run.ids[run.cur] : "";
    if (byId[id] && !isTheme(id)) {
      if (!cur || id === cur) return;
      if (detail.hidden) { openDetail(run.ids.indexOf(id) >= 0 ? run.ids.indexOf(id) : (run.ids.push(id), run.ids.length - 1)); paintBack(); return; }
      backStack.push(cur);
      bootBack = false;
      return showCard(id);
    }
    // another deck: remember this card in our own URL (Back / reload reopens it), then go
    try { history.replaceState(history.state, "", location.pathname + "?open=" + encodeURIComponent(cur)); } catch (e) { /* ignore */ }
    location.href = href + (href.indexOf("?") < 0 ? "?" : "&") + "back=" + encodeURIComponent(D.deck + ":" + cur);
  }
  function paintBack() {
    var b = $("ac-xback"), prev = backStack[backStack.length - 1];
    if (prev) b.querySelector(".xb-name").innerHTML = biText(esc(frontEn(prev)), esc(frontTe(prev)));
    else if (bootBack && BACK) b.querySelector(".xb-name").innerHTML = biText(esc(BACK.en), esc(BACK.te));
    b.hidden = !(prev || (bootBack && BACK));
  }
  function goBack() {
    if (backStack.length) return showCard(backStack.pop());
    if (!bootBack || !BACK) return;
    // came here from another deck: step back through our own study entries to that page; else load it
    if (document.referrer.indexOf("/recall/" + BACK.deck) >= 0 && history.state && history.state.acDetail && history.length > 3) history.go(-3);
    else location.href = BACK.url;
  }
  actions["ac-xback"] = goBack;

  function onStageClick(e) {
    var fa = e.target.closest("a[data-for]");
    if (fa && run && run.cur >= 0) {
      try { history.replaceState(history.state, "", location.pathname + "?open=" + encodeURIComponent(run.ids[run.cur])); } catch (er) { /* ignore */ }
      return; // the link itself navigates
    }
    var pq = e.target.closest("a[data-pyq]");
    if (pq) { e.preventDefault(); return showPyqs(pq.dataset.pyq); }
    var all = e.target.closest("button[data-pyqall]");
    if (all) return togglePyqAll(all);
    var a = e.target.closest("a[data-go]");
    if (a && run) { e.preventDefault(); return go(a.dataset.go, a.getAttribute("href")); }
    var b = e.target.closest("button");
    if (!b || !run) return;
    if (actions[b.id]) return actions[b.id]();
    if (b.classList.contains("ac-tile")) return openDetail(+b.dataset.i);
    if (b.dataset.opt) return answerPractice(b);
    if (b.dataset.retry) return fillDetail(run.cur);
    if (b.dataset.jump) return jumpTo(b.dataset.jump);
    if (b.dataset.tab) return chainTab(b);
    if (b.dataset.judge) return judge(b.dataset.judge);
    if (b.dataset.act === "missed") return reviseMissed();
    if (b.dataset.act === "back") return exitStudy();
    if (b.dataset.act === "stay") return dismissSummary();
  }
  // jump row 'PYQs N' chip: scroll the open card to its PYQ list (no hash change: history drives the card view)
  function showPyqs(listId) {
    var el = document.getElementById(listId);
    if (!el) return;
    for (var p = el.parentElement; p && p !== detail; p = p.parentElement) if (p.tagName === "DETAILS") p.open = true;
    el.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "start" });
    try { el.focus({ preventScroll: true }); } catch (er) { el.focus(); }
  }
  // long PYQ lists (> 12) show 6 first; the button reveals / hides the rest
  function togglePyqAll(b) {
    var ol = document.getElementById(b.dataset.pyqall);
    if (!ol) return;
    var open = b.getAttribute("aria-expanded") !== "true";
    [].forEach.call(ol.querySelectorAll("[data-more]"), function (li) { li.hidden = !open; });
    b.setAttribute("aria-expanded", open ? "true" : "false");
    b.hidden = open;
  }
  // a card in several story chains: tabs switch which chain's timeline is shown
  function chainTab(b) {
    var box = b.closest(".ct-chains");
    [].forEach.call(box.querySelectorAll("[data-tab]"), function (t) { t.setAttribute("aria-selected", t === b ? "true" : "false"); });
    [].forEach.call(box.querySelectorAll("[data-panel]"), function (p) { p.hidden = p.dataset.panel !== b.dataset.tab; });
  }
  function onKey(e) {
    if (stage.hidden || !run || e.altKey || e.ctrlKey || e.metaKey) return;
    var inDetail = !detail.hidden, inSum = !sum.hidden;
    if (e.key === "Escape") {
      e.preventDefault();
      if (inSum) return dismissSummary();
      return inDetail ? collapse() : exitStudy();
    }
    if (inSum || (e.key !== "ArrowLeft" && e.key !== "ArrowRight")) return;
    e.preventDefault();
    var d = e.key === "ArrowRight" ? 1 : -1;
    if (inDetail) step(d); else goPage(d);
  }
  var touch = null;
  function onTouchStart(e) {
    var t = e.touches[0];
    touch = e.touches.length === 1 ? { x: t.clientX, y: t.clientY } : null;
  }
  function onTouchEnd(e) {
    if (!touch || !run || !sum.hidden) return;
    var t = e.changedTouches[0], dx = t.clientX - touch.x, dy = t.clientY - touch.y;
    touch = null;
    if (Math.abs(dx) < 60 || Math.abs(dx) < 1.5 * Math.abs(dy)) return;
    if (!detail.hidden) step(dx < 0 ? 1 : -1); else goPage(dx < 0 ? 1 : -1);
  }
  var resizeTimer = 0;
  function onResize() {
    if (!run || stage.hidden) return;
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () { applyShape(); fitTiles(); }, 80);
  }

  form.addEventListener("change", function (e) { onPartChange(e); paintSetup(); });
  form.addEventListener("submit", onStart);
  $("ac-reset").addEventListener("click", resetProgress);
  $("ac-cont").addEventListener("click", continueRun);
  stage.addEventListener("click", onStageClick);
  stage.addEventListener("touchstart", onTouchStart, { passive: true });
  stage.addEventListener("touchend", onTouchEnd, { passive: true });
  document.addEventListener("keydown", onKey);
  window.addEventListener("popstate", onPop);
  window.addEventListener("resize", onResize);

  // ── init ──
  if (history.state && (history.state.acStudy || history.state.acDetail)) history.replaceState(null, ""); // reload mid-study: start at setup
  restoreChoices();
  var more = $("ac-more");
  if (more) {
    if (readRaw(MORE_KEY) === "1") more.open = true;
    more.addEventListener("toggle", function () { try { localStorage.setItem(MORE_KEY, more.open ? "1" : "0"); } catch (e) { /* ignore */ } });
  }
  paintSetup();
  paintContinue();
  // ?open=<id>: skip setup and open that card (linked from another card); &back=<deck>:<id> shows the way back
  if (FOR && FOR.ids.length) {
    // ?for=<card>: a matrix of exactly the cards linked to that card; the exit button goes back to it
    deepLink = true;
    var cf = choices();
    startRun(FOR.ids, { chapter: "", parts: [], unit: "", mode: "a", lang: cf.lang, density: cf.density, order: "seq", only: false, newer: true });
  } else if (D.open && byId[D.open]) {
    deepLink = true;
    var c0 = choices();
    var ids0 = pickIds({ chapter: "", parts: [], unit: "", only: false, newer: true, mode: "a" });
    if (ids0.indexOf(D.open) < 0) ids0.push(D.open);
    load(D.open).catch(function () { /* the detail view shows a retry */ });
    startRun(ids0, { chapter: "", parts: [], unit: "", mode: "a", lang: c0.lang, density: c0.density, order: "seq", only: false, newer: true });
    bootBack = !!BACK;
    openDetail(run.ids.indexOf(D.open));
    paintBack();
  }
})();
