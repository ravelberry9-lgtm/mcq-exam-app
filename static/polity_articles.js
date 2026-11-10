// Unit 6 article recall cards: setup screen -> full-screen card matrix -> full-screen detail view.
// Vanilla JS, no inline handlers. Progress format is unchanged: localStorage u6_artcards_v1 = { cardId: "k" | "x" }.
(function () {
  "use strict";
  var root = document.getElementById("ac");
  if (!root) return;

  var KEY = "u6_artcards_v1";          // progress (unchanged format)
  var LANG_KEY = "u6_artcards_lang";   // older saved language choice
  var SETUP_KEY = "u6_artcards_setup"; // last setup choices
  var LANGS = ["te", "en", "both"];
  var LANG_LABEL = { te: "తె", en: "EN", both: "తె+EN" };
  var LANG_NAME = { te: "Telugu", en: "English", both: "Telugu and English" };
  var GRIDS = { "18": [3, 6], "32": [4, 8] };   // columns x rows for a portrait phone

  var $ = function (id) { return document.getElementById(id); };
  var form = $("ac-setup"), stage = $("ac-stage"), grid = $("ac-grid"), detail = $("ac-detail"), sum = $("ac-sum"), live = $("ac-live");
  var deck = [].slice.call(root.querySelectorAll(".ac-src"));
  var byId = {};
  deck.forEach(function (s) { byId[s.dataset.id] = s; });

  var progress = readJSON(KEY);
  var run = null; // { ids, page, cur, marks:{}, mode, lang, density, chapter }
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
  function conceptEn(id) { return byId[id].querySelector(".s-con .ac-en").textContent.trim(); }
  function shuffled(list) {
    var a = list.slice();
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }

  // ── setup screen ──
  function choices() {
    var f = form.elements;
    return {
      chapter: f.chapter.value, mode: f.mode.value, lang: f.lang.value, density: f.density.value,
      only: f.only.checked, shuffle: f.shuffle.checked
    };
  }
  function setRadio(name, value) {
    var r = form.querySelector('input[name="' + name + '"][value="' + value + '"]');
    if (r) r.checked = true;
  }
  function restoreChoices() {
    var saved = readJSON(SETUP_KEY);
    var urlChapter = root.dataset.chapter, langFromUrl = root.dataset.langSet === "1";
    if (!urlChapter && typeof saved.chapter === "string") setRadio("chapter", saved.chapter);
    if (/^[ab]$/.test(saved.mode)) setRadio("mode", saved.mode);
    if (GRIDS[saved.density]) setRadio("density", saved.density);
    var lang = saved.lang || readRaw(LANG_KEY);
    if (!langFromUrl && LANGS.indexOf(lang) >= 0) setRadio("lang", lang);
    form.elements.only.checked = !!saved.only;
    form.elements.shuffle.checked = !!saved.shuffle;
  }
  function saveChoices() {
    var c = choices();
    if (run) { c.mode = run.mode; c.lang = run.lang; }
    writeJSON(SETUP_KEY, c);
  }
  function pickIds(c) {
    return deck.filter(function (s) {
      return (!c.chapter || s.dataset.ch === c.chapter) && (!c.only || progress[s.dataset.id] === "x");
    }).map(function (s) { return s.dataset.id; });
  }
  function countState(ids, v) {
    return ids.filter(function (id) { return progress[id] === v; }).length;
  }
  function paintSetup() {
    var c = choices();
    root.dataset.lang = c.lang;
    var inChapter = pickIds({ chapter: c.chapter, only: false });
    var ids = pickIds(c);
    var k = countState(inChapter, "k"), x = countState(inChapter, "x");
    $("ac-xcount").textContent = x ? " (" + x + ")" : "";
    $("ac-start-n").textContent = ids.length + (ids.length === 1 ? " card" : " cards");
    $("ac-start").disabled = !ids.length;
    $("ac-saved").textContent = (k || x) ? "Saved on this device: " + k + " known, " + x + " to revise" : "";
    var msg = $("ac-msg");
    msg.hidden = ids.length > 0;
    msg.textContent = ids.length ? "" : "No cards here are marked Revise yet. Turn off ‘Only cards to revise’ to study them all.";
    var acc = form.querySelector('input[name="chapter"]:checked').closest(".ac-ch").style.getPropertyValue("--acc");
    form.style.setProperty("--acc", acc);
  }
  function resetProgress() {
    if (!window.confirm("Reset all article card progress?\nపురోగతి మొత్తం రీసెట్ చేయాలా?")) return;
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
  function startRun(ids, c) {
    if (!ids.length) return;
    run = {
      ids: c.shuffle ? shuffled(ids) : ids, page: 0, cur: -1, marks: {},
      mode: c.mode, lang: c.lang, density: c.density || "18", chapter: c.chapter || ""
    };
    sum.hidden = true;
    detail.hidden = true;
    openStage();
    renderMatrix();
    focusTile(0);
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
    run = null;
    paintSetup();
    $("ac-start").focus({ preventScroll: true });
  }
  function exitStudy() {
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
    var label = run.mode === "a"
      ? "Article " + n + ", chapter " + src.dataset.ch + ", " + stateText
      : conceptEn(id) + ", chapter " + src.dataset.ch + ", " + stateText;
    var cue = run.mode === "a"
      ? '<b class="t-num" style="--len:' + Math.max(3, n.length) + '">' + esc(n) + "</b>"
      : '<span class="t-con">' + src.querySelector(".s-con").innerHTML + "</span>";
    return '<button type="button" class="ac-tile" data-i="' + index + '" data-state="' + state + '" style="--acc:' + src.dataset.acc +
      '" aria-label="' + esc(label) + '"><span class="t-ch" aria-hidden="true">' + src.dataset.ch +
      '</span><span class="t-mark" aria-hidden="true"></span><span class="t-cue">' + cue + "</span></button>";
  }
  function renderMatrix() {
    stage.dataset.lang = run.lang;
    stage.dataset.mode = run.mode;
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
  function paintBar() {
    var pages = pageCount(), ids = run.ids;
    var where = run.chapter ? byId[ids[0]].querySelector(".s-chap").innerHTML : biText("All chapters", "అన్ని అధ్యాయాలు");
    $("ac-where").innerHTML = '<span class="w-ch">' + where + "</span>";
    stage.style.setProperty("--acc", run.chapter ? byId[ids[0]].dataset.acc : "#0f766e");
    $("ac-pager").hidden = pages < 2;
    $("ac-page").textContent = (run.page + 1) + "/" + pages;
    $("ac-pprev").disabled = run.page === 0;
    $("ac-pnext").disabled = run.page >= pages - 1;
    var modeBtn = $("ac-mode");
    modeBtn.setAttribute("aria-pressed", run.mode === "b" ? "true" : "false");
    modeBtn.setAttribute("aria-label", run.mode === "a" ? "Showing article numbers. Show concepts instead" : "Showing concepts. Show article numbers instead");
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
    if (!run || run.mode !== "b") return;
    var boxes = [].slice.call(grid.querySelectorAll(".t-cue"));
    if (!boxes.length) return;
    var b0 = boxes[0];
    var max = Math.max(13, Math.min(26, Math.round(Math.min(b0.clientWidth / 6.5, b0.clientHeight / 4))));
    var fits = boxes.map(function (box) { return fitOne(box, max); });
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
    live.textContent = "Page " + (p + 1) + " of " + pageCount();
  }
  function focusTile(index) {
    var t = grid.querySelector('.ac-tile[data-i="' + index + '"]') || grid.querySelector(".ac-tile");
    if (t) t.focus({ preventScroll: true });
  }
  function toggleMode() {
    run.mode = run.mode === "a" ? "b" : "a";
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

  // ── detail view ──
  function fillDetail(index) {
    var id = run.ids[index], src = byId[id], n = esc(num(id));
    run.cur = index;
    detail.style.setProperty("--acc", src.dataset.acc);
    detail.dataset.lang = run.lang;
    detail.dataset.state = progress[id] || "";
    $("ac-dchap").innerHTML = src.querySelector(".s-chap").innerHTML;
    $("ac-dtitle").innerHTML = '<span class="ac-pill"><small>' + biText("Article", "ప్రకరణ") + "</small>" + n + "</span>" +
      '<span class="ac-anstext">' + src.querySelector(".s-con").innerHTML + "</span>";
    $("ac-dbody").innerHTML = src.querySelector(".s-back").innerHTML;
    $("ac-dscroll").scrollTop = 0;
    $("ac-pos").textContent = (index + 1) + " / " + run.ids.length;
    $("ac-prev").disabled = index === 0;
    $("ac-next").disabled = index >= run.ids.length - 1;
    live.textContent = "Article " + num(id) + ", card " + (index + 1) + " of " + run.ids.length;
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
    var index = run.cur;
    var page = Math.floor(index / perPage());
    if (page !== run.page) run.page = page;
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
  function step(d) {
    var i = run.cur + d;
    if (i < 0 || i >= run.ids.length) return;
    fillDetail(i);
    var body = $("ac-dscroll");
    if (!reduceMotion && body.animate) body.animate([{ opacity: 0, transform: "translateX(" + (d * 24) + "px)" }, { opacity: 1, transform: "none" }], { duration: 180, easing: "ease-out" });
  }
  function judge(value) {
    var id = run.ids[run.cur];
    progress[id] = value;
    writeJSON(KEY, progress);
    run.marks[id] = value;
    detail.dataset.state = value;
    collapse();
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
    var ids = run.ids.filter(function (id) { return run.marks[id] === "x"; });
    startRun(ids, { shuffle: false, mode: run.mode, lang: run.lang, density: run.density, chapter: run.chapter });
  }
  function dismissSummary() {
    sum.hidden = true;
    run.marks = {}; // looking again starts a fresh tally
    focusTile(run.page * perPage());
  }

  // ── events ──
  var actions = {
    "ac-exit": exitStudy, "ac-mode": toggleMode, "ac-lang": cycleLang,
    "ac-pprev": function () { goPage(-1); }, "ac-pnext": function () { goPage(1); },
    "ac-collapse": collapse, "ac-prev": function () { step(-1); }, "ac-next": function () { step(1); }
  };
  function onStageClick(e) {
    var b = e.target.closest("button");
    if (!b || !run) return;
    if (actions[b.id]) return actions[b.id]();
    if (b.classList.contains("ac-tile")) return openDetail(+b.dataset.i);
    if (b.dataset.judge) return judge(b.dataset.judge);
    if (b.dataset.act === "missed") return reviseMissed();
    if (b.dataset.act === "back") return exitStudy();
    if (b.dataset.act === "stay") return dismissSummary();
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

  form.addEventListener("change", paintSetup);
  form.addEventListener("submit", onStart);
  $("ac-reset").addEventListener("click", resetProgress);
  stage.addEventListener("click", onStageClick);
  stage.addEventListener("touchstart", onTouchStart, { passive: true });
  stage.addEventListener("touchend", onTouchEnd, { passive: true });
  document.addEventListener("keydown", onKey);
  window.addEventListener("popstate", onPop);
  window.addEventListener("resize", onResize);

  // ── init ──
  if (history.state && (history.state.acStudy || history.state.acDetail)) history.replaceState(null, ""); // reload mid-study: start at setup
  restoreChoices();
  paintSetup();
})();
