// Unit 6 article recall cards: setup screen + full-screen study mode. Vanilla JS, no inline handlers.
(function () {
  "use strict";
  var root = document.getElementById("ac");
  if (!root) return;

  var KEY = "u6_artcards_v1";          // progress: { cardId: "k" | "x" } (unchanged format)
  var LANG_KEY = "u6_artcards_lang";   // kept for older saved language choice
  var SETUP_KEY = "u6_artcards_setup"; // last setup choices
  var $ = function (id) { return document.getElementById(id); };
  var form = $("ac-setup"), stage = $("ac-stage"), sheet = $("ac-sheet"), live = $("ac-live");
  var deck = [].slice.call(root.querySelectorAll(".ac-src"));
  var byId = {};
  deck.forEach(function (s) { byId[s.dataset.id] = s; });

  var progress = readJSON(KEY);
  var run = null; // { ids, i, flipped, tally:{k,x}, missed:[], mode, lang }

  // ── storage (private mode / blocked storage must never break the page) ──
  function readJSON(key) {
    try { return JSON.parse(localStorage.getItem(key) || "{}") || {}; } catch (e) { return {}; }
  }
  function writeJSON(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); } catch (e) { /* ignore */ }
  }
  function readRaw(key) {
    try { return localStorage.getItem(key); } catch (e) { return null; }
  }

  // ── setup screen ──
  function choices() {
    var f = form.elements;
    return {
      chapter: f.chapter.value, mode: f.mode.value, lang: f.lang.value,
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
    var lang = saved.lang || readRaw(LANG_KEY);
    if (!langFromUrl && /^(te|en|both)$/.test(lang || "")) setRadio("lang", lang);
    form.elements.only.checked = !!saved.only;
    form.elements.shuffle.checked = !!saved.shuffle;
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

  // ── study run ──
  function shuffled(list) {
    var a = list.slice();
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }
  function startRun(ids, c) {
    if (!ids.length) return;
    run = { ids: c.shuffle ? shuffled(ids) : ids, i: 0, flipped: false, tally: { k: 0, x: 0 }, missed: [], mode: c.mode, lang: c.lang };
    openStage();
    showCard();
  }
  function onStart(e) {
    e.preventDefault();
    var c = choices();
    writeJSON(SETUP_KEY, c);
    startRun(pickIds(c), c);
  }

  function openStage() {
    if (stage.parentNode !== document.body) document.body.appendChild(stage);
    stage.dataset.lang = run.lang;
    stage.dataset.mode = run.mode;
    stage.hidden = false;
    document.documentElement.classList.add("ac-studying");
    var app = document.querySelector(".app");
    if (app) app.inert = true;
    if (!history.state || !history.state.acStudy) history.pushState({ acStudy: 1 }, "");
  }
  function closeStage() {
    stage.hidden = true;
    document.documentElement.classList.remove("ac-studying");
    var app = document.querySelector(".app");
    if (app) app.inert = false;
    run = null;
    paintSetup();
    $("ac-start").focus({ preventScroll: true });
  }
  function exitStudy() {
    if (history.state && history.state.acStudy) history.back(); // popstate closes the stage
    else closeStage();
  }

  function fillFrom(src, sel, target) {
    target.innerHTML = src.querySelector(sel).innerHTML;
  }
  function showCard() {
    var id = run.ids[run.i], src = byId[id];
    run.flipped = false;
    stage.style.setProperty("--acc", src.dataset.acc);
    stage.dataset.state = progress[id] || "";
    sheet.innerHTML = $("ac-tpl-card").innerHTML;
    sheet.className = "ac-sheet";
    var num = esc(src.querySelector(".s-num").textContent.trim());
    var concept = src.querySelector(".s-con").innerHTML;
    var label = "<small>" + biText("Article", "ప్రకరణ") + "</small>";
    sheet.querySelectorAll(".ac-chap").forEach(function (n) { fillFrom(src, ".s-chap", n); });
    sheet.querySelector(".ac-cue").innerHTML = run.mode === "a"
      ? label + '<b class="ac-big" style="--len:' + Math.max(2, num.length) + '">' + num + "</b>"
      : '<span class="ac-concept">' + concept + "</span>";
    sheet.querySelector(".ac-ans").innerHTML = (run.mode === "a"
      ? '<span class="ac-pill">' + num + "</span>"
      : '<span class="ac-pill big">' + label + num + "</span>") + '<span class="ac-anstext">' + concept + "</span>";
    fillFrom(src, ".s-back", sheet.querySelector(".ac-body"));
    sheet.querySelector(".ac-count").textContent = (run.i + 1) + " / " + run.ids.length;
    live.textContent = "Card " + (run.i + 1) + " of " + run.ids.length;
    sheet.querySelector(".ac-front").focus({ preventScroll: true });
  }
  function biText(en, te) {
    return '<span class="ac-te" lang="te">' + te + '</span><span class="ac-en" lang="en">' + en + "</span>";
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (ch) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[ch]; });
  }

  function flip(open) {
    if (!run || !sheet.querySelector(".ac-front")) return;
    run.flipped = open;
    sheet.classList.toggle("is-open", open);
    sheet.querySelector(".ac-front").hidden = open;
    sheet.querySelector(".ac-reveal").hidden = !open;
    if (open) {
      sheet.querySelector(".ac-body").scrollTop = 0;
      sheet.querySelector('[data-judge="k"]').focus({ preventScroll: true });
    } else {
      sheet.querySelector(".ac-front").focus({ preventScroll: true });
    }
  }
  function judge(value) {
    var id = run.ids[run.i];
    progress[id] = value;
    writeJSON(KEY, progress);
    run.tally[value]++;
    if (value === "x") run.missed.push(id);
    advance(1);
  }
  function advance(step) {
    if (!run) return;
    if (sheet.querySelector(".ac-done")) { if (step < 0) { run.i = run.ids.length - 1; showCard(); } return; }
    var next = run.i + step;
    if (next < 0) return;
    if (next >= run.ids.length) return showDone();
    run.i = next;
    showCard();
  }
  function showDone() {
    sheet.innerHTML = $("ac-tpl-done").innerHTML;
    sheet.className = "ac-sheet is-done";
    stage.style.setProperty("--acc", "#0f766e");
    stage.dataset.state = "";
    sheet.querySelector('[data-n="k"]').textContent = run.tally.k;
    sheet.querySelector('[data-n="x"]').textContent = run.tally.x;
    var missed = sheet.querySelector('[data-act="missed"]');
    missed.hidden = !run.missed.length;
    live.textContent = "Round finished: " + run.tally.k + " known, " + run.tally.x + " to revise";
    (run.missed.length ? missed : sheet.querySelector('[data-act="back"]')).focus({ preventScroll: true });
  }
  function reviseMissed() {
    var ids = run.missed.slice();
    startRun(ids, { shuffle: false, mode: run.mode, lang: run.lang });
  }

  // ── events ──
  function onStageClick(e) {
    var b = e.target.closest("button");
    if (!b) return;
    if (b.id === "ac-exit") return exitStudy();
    if (b.id === "ac-skip") return advance(1);
    if (b.classList.contains("ac-front")) return flip(true);
    if (b.dataset.judge) return judge(b.dataset.judge);
    if (b.dataset.act === "missed") return reviseMissed();
    if (b.dataset.act === "back") return exitStudy();
  }
  function onKey(e) {
    if (stage.hidden || !run || e.altKey || e.ctrlKey || e.metaKey) return;
    var onButton = e.target.closest && e.target.closest("button, a");
    switch (e.key) {
      case "Escape": e.preventDefault(); return exitStudy();
      case "ArrowRight": e.preventDefault(); return advance(1);
      case "ArrowLeft": e.preventDefault(); return advance(-1);
      case " ": case "Enter":
        if (onButton && !onButton.classList.contains("ac-front")) return; // let focused buttons/links act
        if (sheet.querySelector(".ac-done")) return;
        e.preventDefault(); return flip(!run.flipped);
    }
  }
  var touch = null;
  function onTouchStart(e) {
    var t = e.touches[0];
    touch = e.touches.length === 1 ? { x: t.clientX, y: t.clientY } : null;
  }
  function onTouchEnd(e) {
    if (!touch) return;
    var t = e.changedTouches[0], dx = t.clientX - touch.x, dy = t.clientY - touch.y;
    touch = null;
    if (Math.abs(dx) > 60 && Math.abs(dx) > 1.5 * Math.abs(dy)) advance(dx < 0 ? 1 : -1);
  }
  function onPop() {
    if (!stage.hidden) closeStage();
  }

  form.addEventListener("change", paintSetup);
  form.addEventListener("submit", onStart);
  $("ac-reset").addEventListener("click", resetProgress);
  stage.addEventListener("click", onStageClick);
  stage.addEventListener("touchstart", onTouchStart, { passive: true });
  stage.addEventListener("touchend", onTouchEnd, { passive: true });
  document.addEventListener("keydown", onKey);
  window.addEventListener("popstate", onPop);

  // ── init ──
  if (history.state && history.state.acStudy) history.replaceState(null, ""); // reload mid-study: start at setup
  restoreChoices();
  paintSetup();
})();
