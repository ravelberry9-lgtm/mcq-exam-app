// Unit 6 article recall cards: mode, language, reveal, self-check, filters. Vanilla JS, no inline handlers.
(function () {
  "use strict";
  var root = document.getElementById("ac");
  if (!root) return;

  var KEY = "u6_artcards_v1", LANG_KEY = "u6_artcards_lang";
  var cards = [].slice.call(root.querySelectorAll(".ac-card"));
  var bar = document.getElementById("ac-bar");
  var el = function (id) { return document.getElementById(id); };
  var state = load();
  var onlyRevise = false;

  // ── storage (private mode / blocked storage must never break the page) ──
  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { return {}; }
  }
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) { /* ignore */ }
  }
  function pref(key, value) {
    try {
      if (value === undefined) return localStorage.getItem(key);
      localStorage.setItem(key, value);
    } catch (e) { return null; }
  }

  function pressGroup(selector, attr, value) {
    root.querySelectorAll(selector).forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute(attr) === value));
    });
  }

  // ── progress + marks ──
  function paintCard(card) {
    var s = state[card.dataset.id];
    card.classList.toggle("k", s === "k");
    card.classList.toggle("x", s === "x");
    card.querySelector(".ac-mark .sr").textContent = s === "k" ? "Known" : s === "x" ? "To revise" : "";
    card.querySelectorAll("[data-judge]").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.judge === s));
    });
    card.hidden = onlyRevise && s !== "x";
  }
  function paintCounts() {
    var k = 0, x = 0, n = cards.length;
    cards.forEach(function (c) { var s = state[c.dataset.id]; if (s === "k") k++; else if (s === "x") x++; });
    el("ac-nk").textContent = k;
    el("ac-nx").textContent = x;
    el("ac-nn").textContent = n - k - x;
    el("ac-pk").style.width = (n ? (100 * k) / n : 0) + "%";
    el("ac-px").style.width = (n ? (100 * x) / n : 0) + "%";
    el("ac-live").textContent = k + " known, " + x + " to revise, " + (n - k - x) + " left";
  }
  function paint() {
    cards.forEach(paintCard);
    root.querySelectorAll(".ac-sec").forEach(function (sec) {
      sec.hidden = !sec.querySelector(".ac-card:not([hidden])");
    });
    el("ac-empty").hidden = !(onlyRevise && !root.querySelector(".ac-card:not([hidden])"));
    paintCounts();
  }

  // ── reveal ──
  function setOpen(card, open) {
    card.classList.toggle("open", open);
    card.querySelector(".ac-face").setAttribute("aria-expanded", String(open));
    card.querySelector(".ac-back").hidden = !open;
  }
  function closeAll(except) {
    cards.forEach(function (c) { if (c !== except && c.classList.contains("open")) setOpen(c, false); });
  }
  function reveal(card, open) {
    if (open) closeAll(card);
    setOpen(card, open);
    if (open) card.scrollIntoView({ block: "start", behavior: reducedMotion() ? "auto" : "smooth" });
  }
  function reducedMotion() {
    return window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  }

  function judge(card, value) {
    state[card.dataset.id] = value;
    save();
    setOpen(card, false);
    paint();
    var face = card.hidden ? null : card.querySelector(".ac-face");
    if (face) face.focus({ preventScroll: true });
  }

  // Next card not yet marked known, after the current one; wraps around.
  function nextCard() {
    var visible = cards.filter(function (c) { return !c.hidden; });
    if (!visible.length) return;
    var cur = root.querySelector(".ac-card.open") || (document.activeElement && document.activeElement.closest && document.activeElement.closest(".ac-card"));
    var start = Math.max(0, visible.indexOf(cur) + 1);
    var order = visible.slice(start).concat(visible.slice(0, start));
    var target = order.find(function (c) { return state[c.dataset.id] !== "k"; });
    if (!target) { el("ac-live").textContent = "Every card here is marked known."; return; }
    closeAll(null);
    target.scrollIntoView({ block: "start", behavior: reducedMotion() ? "auto" : "smooth" });
    target.querySelector(".ac-face").focus({ preventScroll: true });
    target.classList.remove("ping"); void target.offsetWidth; target.classList.add("ping");
  }

  // ── controls ──
  function setMode(m) {
    root.dataset.mode = m;
    closeAll(null);
    pressGroup("button[data-mode]", "data-mode", m);
  }
  function setLang(l) {
    root.dataset.lang = l;
    pressGroup("[data-l]", "data-l", l);
    pref(LANG_KEY, l);
  }
  function toggleOnlyRevise(btn) {
    onlyRevise = !onlyRevise;
    btn.setAttribute("aria-pressed", String(onlyRevise));
    closeAll(null);
    paint();
  }
  function shuffle(btn) {
    var on = btn.getAttribute("aria-pressed") !== "true";
    root.querySelectorAll(".ac-grid").forEach(function (grid) {
      var items = [].slice.call(grid.children);
      if (on) {
        for (var i = items.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = items[i]; items[i] = items[j]; items[j] = t; }
      } else {
        items.sort(function (a, b) { return a.dataset.i - b.dataset.i; });
      }
      items.forEach(function (n) { grid.appendChild(n); });
    });
    cards = [].slice.call(root.querySelectorAll(".ac-card"));
    btn.setAttribute("aria-pressed", String(on));
  }
  function reset() {
    if (!window.confirm("Reset all article card progress?\nపురోగతి మొత్తం రీసెట్ చేయాలా?")) return;
    state = {};
    save();
    onlyRevise = false;
    el("ac-only").setAttribute("aria-pressed", "false");
    paint();
  }

  root.addEventListener("click", function (e) {
    var t = e.target;
    var b;
    if ((b = t.closest("button[data-mode]"))) return setMode(b.dataset.mode);
    if ((b = t.closest("[data-l]"))) return setLang(b.dataset.l);
    if ((b = t.closest("[data-judge]"))) return judge(b.closest(".ac-card"), b.dataset.judge);
    if ((b = t.closest(".ac-face"))) { var c = b.closest(".ac-card"); return reveal(c, !c.classList.contains("open")); }
  });
  el("ac-next").addEventListener("click", nextCard);
  el("ac-only").addEventListener("click", function () { toggleOnlyRevise(this); });
  el("ac-shuffle").addEventListener("click", function () { shuffle(this); });
  el("ac-reset").addEventListener("click", reset);
  root.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      var open = root.querySelector(".ac-card.open");
      if (open) { setOpen(open, false); open.querySelector(".ac-face").focus(); }
    }
  });

  // Keep scroll targets clear of the sticky bar.
  function measureBar() { root.style.setProperty("--bar-h", (bar.offsetHeight + 12) + "px"); }
  window.addEventListener("resize", measureBar);

  // ── init ──
  cards.forEach(function (c, i) { c.dataset.i = i; });
  var saved = pref(LANG_KEY);
  if (saved && /^(te|en|both)$/.test(saved) && !/[?&]qlang=/.test(location.search)) setLang(saved);
  measureBar();
  paint();
})();
