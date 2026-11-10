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
  var TEXT_FRONT = D.kind === "text";
  var THEMES = D.themes === "1"; // cases: direction B is a theme view (one tile per theme, opened = its cases)
  var LANGS = ["te", "en", "both"];
  var LANG_LABEL = { te: "తె", en: "EN", both: "తె+EN" };
  var LANG_NAME = { te: "Telugu", en: "English", both: "Telugu and English" };
  var GRIDS = { "18": [3, 6], "32": [4, 8] };   // columns x rows for a portrait phone

  var $ = function (id) { return document.getElementById(id); };
  var form = $("ac-setup"), stage = $("ac-stage"), grid = $("ac-grid"), detail = $("ac-detail"), sum = $("ac-sum"), live = $("ac-live");
  var all = [].slice.call(root.querySelectorAll(".ac-src"));
  var byId = {};
  all.forEach(function (s) { byId[s.dataset.id] = s; });
  var deck = all.filter(function (s) { return !s.dataset.themeTile; });
  var themeTiles = all.filter(function (s) { return s.dataset.themeTile; });
  function isTheme(id) { return !!byId[id].dataset.themeTile; }
  // cases of a theme tile that pass the run's chapter / newer filters
  function themeRows(src, c) {
    return [].filter.call(src.querySelectorAll(".ac-thlist li"), function (li) {
      return (!c.chapter || li.dataset.ch === c.chapter) && (c.newer !== false || li.dataset.src !== "new");
    });
  }

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
      chapter: f.chapter.value, mode: f.mode.value, lang: f.lang.value, density: f.density.value,
      only: f.only.checked, order: f.order.value, newer: f.newer ? f.newer.checked : true
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
    if (/^[ab]$/.test(saved.mode) && (saved.mode === "a" || anyTwoWay)) setRadio("mode", saved.mode);
    if (form.elements.newer && saved.newer === false) form.elements.newer.checked = false;
    if (GRIDS[saved.density]) setRadio("density", saved.density);
    var lang = saved.lang || readRaw(LANG_KEY);
    if (!langFromUrl && LANGS.indexOf(lang) >= 0) setRadio("lang", lang);
    form.elements.only.checked = !!saved.only;
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
    return deck.filter(function (s) {
      return (!c.chapter || s.dataset.ch === c.chapter) && (!c.only || progress[s.dataset.id] === "x") &&
        (c.newer !== false || s.dataset.src !== "new") && (c.mode !== "b" || s.dataset.two === "1");
    }).map(function (s) { return s.dataset.id; });
  }
  function countState(ids, v) {
    return ids.filter(function (id) { return progress[id] === v; }).length;
  }
  function paintSetup() {
    var c = choices();
    root.dataset.lang = c.lang;
    var inChapter = pickIds({ chapter: c.chapter, only: false, newer: c.newer });
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
    var acc = form.querySelector('input[name="chapter"]:checked').closest(".ac-ch").style.getPropertyValue("--acc");
    form.style.setProperty("--acc", acc);
    form.style.setProperty("--acc-ink", form.querySelector('input[name="chapter"]:checked').closest(".ac-ch").style.getPropertyValue("--acc-ink"));
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
  function startRun(ids, c) {
    if (!ids.length) return;
    var order = c.order === "rand" ? "rand" : "seq";
    run = {
      all: c.all || pickIds({ chapter: c.chapter, only: c.only, newer: c.newer, mode: "a" }),
      base: ids.slice(), ids: order === "rand" ? shuffled(ids) : ids.slice(), order: order, page: 0, cur: -1, marks: {},
      mode: c.mode, lang: c.lang, density: c.density || "18", chapter: c.chapter || "", only: !!c.only, newer: c.newer !== false
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
    if (run) { setRadio("order", run.order); setRadio("mode", run.mode); setRadio("lang", run.lang); }
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
    var sb = sub(id);
    var band = src.querySelector(".s-band");
    var label = (run.mode === "a" ? frontEn(id) + (sb ? " " + sb : "") : conceptEn(id)) + (band ? "" : ", chapter " + src.dataset.ch) + ", " + stateText;
    var cue;
    if (isTheme(id)) {
      var n = themeRows(src, run).length;
      label = "Theme: " + conceptEn(id) + ", " + n + " cases, " + stateText;
      cue = '<span class="t-front">' + src.querySelector(".s-front").innerHTML + '<span class="t-sub">' + biText(n + " cases", n + " కేసులు") + "</span></span>";
    } else if (run.mode === "b") cue = '<span class="t-con">' + src.querySelector(".s-con").innerHTML + "</span>";
    else if (TEXT_FRONT) cue = '<span class="t-front">' + src.querySelector(".s-front").innerHTML + (sb ? '<span class="t-sub">' + esc(sb) + "</span>" : "") + "</span>";
    else if (sb && D.deck !== "articles") cue = '<span class="t-numwrap"><b class="t-num" style="--len:' + Math.max(3, n.length) + '">' + esc(n) + '</b><span class="t-sub">' + esc(sb) + "</span></span>";
    else cue = '<b class="t-num" style="--len:' + Math.max(3, n.length) + '">' + esc(n) + "</b>";
    return '<button type="button" class="ac-tile" data-i="' + index + '" data-state="' + state + '" style="--acc:' + src.dataset.acc + ';--acc-ink:' + (src.dataset.ink || '') +
      '" aria-label="' + esc(label) + '"><span class="t-ch' + (band ? " t-band" : "") + '" aria-hidden="true">' + (band ? band.innerHTML : src.dataset.ch) +
      '</span><span class="t-mark" aria-hidden="true"></span><span class="t-cue">' + cue + "</span></button>";
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
    if (run.chapter) {
      where.innerHTML = '<span class="w-chip">' + esc(run.chapter) + "</span>";
      where.setAttribute("aria-label", "Chapter " + run.chapter);
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
  // Direction B shows only two-way cards (a cue that maps to exactly one front); switching re-filters and keeps marks.
  function toggleMode() {
    if (!anyTwoWay) return;
    var mode = run.mode === "a" ? "b" : "a";
    var ids = THEMES ? pickIds({ chapter: run.chapter, only: run.only, newer: run.newer, mode: mode })
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
    var id = run.ids[index], src = byId[id], n = esc(num(id));
    run.cur = index;
    detail.style.setProperty("--acc", src.dataset.acc);
    detail.style.setProperty("--acc-ink", src.dataset.ink);
    detail.dataset.lang = run.lang;
    detail.dataset.state = progress[id] || "";
    $("ac-dchap").innerHTML = src.querySelector(".s-chap").innerHTML;
    var sb = esc(sub(id)), pill = isTheme(id) ? biText("Theme", "అంశం") : biText(D.pillEn || "Article", D.pillTe || "ప్రకరణ");
    var head = TEXT_FRONT
      ? '<span class="ac-pill txt"><small>' + pill + "</small>" + src.querySelector(".s-front").innerHTML + (sb ? '<span class="p-sub">' + sb + "</span>" : "") + "</span>"
      : '<span class="ac-pill"><small>' + pill + "</small>" + n + (sb && D.deck !== "articles" ? '<span class="p-sub">' + sb + "</span>" : "") + "</span>";
    $("ac-dtitle").innerHTML = head + (isTheme(id) ? "" : '<span class="ac-anstext">' + src.querySelector(".s-title").innerHTML + "</span>");
    $("ac-dbody").innerHTML = src.querySelector(".s-back").innerHTML;
    detail.dataset.theme = isTheme(id) ? "1" : "";
    if (isTheme(id)) {
      var keep = themeRows(src, run).map(function (li) { return [].indexOf.call(li.parentNode.children, li); });
      [].forEach.call($("ac-dbody").querySelectorAll(".ac-thlist li"), function (li, i) { if (keep.indexOf(i) < 0) li.remove(); });
    }
    // chain timeline: a step can jump only to a card that is in this run
    [].forEach.call($("ac-dbody").querySelectorAll("[data-jump]"), function (b) {
      if (run.ids.indexOf(b.dataset.jump) < 0) { b.disabled = true; b.removeAttribute("data-jump"); }
    });
    $("ac-dscroll").scrollTop = 0;
    $("ac-pos").textContent = (index + 1) + " / " + run.ids.length;
    $("ac-prev").disabled = index === 0;
    $("ac-next").disabled = index >= run.ids.length - 1;
    live.textContent = frontEn(id) + ", card " + (index + 1) + " of " + run.ids.length;
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
    startRun(ids, { order: run.order, mode: run.mode, lang: run.lang, density: run.density, chapter: run.chapter, all: ids.slice() });
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
    "ac-collapse": collapse, "ac-prev": function () { step(-1); }, "ac-next": function () { step(1); }
  };
  function onStageClick(e) {
    var b = e.target.closest("button");
    if (!b || !run) return;
    if (actions[b.id]) return actions[b.id]();
    if (b.classList.contains("ac-tile")) return openDetail(+b.dataset.i);
    if (b.dataset.opt) return answerPractice(b);
    if (b.dataset.jump) return jumpTo(b.dataset.jump);
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
