// Timeline trees: amendments + cases by year (light index embedded), lineages fetched on demand. No libraries.
(function () {
  "use strict";
  var root = document.getElementById("tr");
  if (!root) return;
  var DATA = JSON.parse(document.getElementById("tr-data").textContent);
  var D = root.dataset, NODES = DATA.nodes, BY = {};
  NODES.forEach(function (n) { BY[n.id] = n; });
  var TH = {}; DATA.themes.forEach(function (t) { TH[t[0]] = t; });
  var PT = {}; DATA.parts.forEach(function (p) { PT[p[0]] = p; });
  var LANGS = ["te", "en", "both"], LNAME = { te: "తెలుగు", en: "English", both: "తె + En" };
  var LKEY = "u6_trees_lang", OKEY = "u6_trees_old", OLD = "u6_artcards_lang", POS = "u6_trees_last"; // legacy key, no longer written
  var body = document.getElementById("tr-body"), chipsEl = document.getElementById("tr-chips"),
      jump = document.getElementById("tr-jump"), countEl = document.getElementById("tr-count"),
      qEl = document.getElementById("tr-q"), pyqEl = document.getElementById("tr-pyq"), langBtn = document.getElementById("tr-lang"),
      oldEl = document.getElementById("tr-old"), fBtn = document.getElementById("tr-fbtn"), fN = document.getElementById("tr-fn"), sheet = document.getElementById("tr-sheet");
  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function sget(k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } }
  function sset(k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} }
  var st = { tab: "am", lang: D.lang || "both", chip: "", q: "", pyq: false, chains: null, old: false };
  st.old = get(OKEY) === "1"; oldEl.checked = st.old;
  var saved = get(LKEY) || get(OLD);
  if (saved && saved.charAt(0) === "{") { try { saved = JSON.parse(saved).lang; } catch (e) { saved = null; } }
  if (LANGS.indexOf(saved) >= 0) st.lang = saved;
  var h = location.hash.slice(1); if (["am", "case", "both", "lines"].indexOf(h) >= 0) st.tab = h;
  // Coming back from a card (Back, collapse, phone back): history.state of this entry holds the exact view the student left.
  // A card opened fresh (no history) that returns here by replace leaves only the node id in sessionStorage.
  var HL = "u6_trees_hl", NAV = "u6_nav", pend = null;
  try { pend = history.state && history.state.tr; } catch (e) { pend = null; }
  if (!pend && sget(HL)) { pend = { id: sget(HL) }; var pn = BY[pend.id]; if (pn && st.tab !== "lines" && st.tab !== "both" && st.tab !== pn.k) st.tab = pn.k; }
  sset(HL, "");
  if (pend) {
    if (pend.tab) st.tab = pend.tab;
    st.chip = pend.chip || ""; st.q = pend.q || ""; st.pyq = !!pend.pyq; if (pend.old != null) st.old = !!pend.old;
    if (pend.lang && LANGS.indexOf(pend.lang) >= 0) st.lang = pend.lang;
    qEl.value = st.q; pyqEl.checked = st.pyq; oldEl.checked = st.old;
    if (pend.sheet && st.tab !== "lines") { sheet.hidden = false; fBtn.setAttribute("aria-expanded", "true"); }
    if (BY[pend.id] && BY[pend.id].old && st.tab !== "lines") { st.old = true; oldEl.checked = true; }
  }

  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function T(p) { // [en, te] in the current language; both = Telugu first, English under it
    var en = p[0] || "", te = p[1] || en;
    if (st.lang === "en") return '<span lang="en">' + esc(en) + "</span>";
    if (st.lang === "te" || te === en) return '<span lang="te">' + esc(te) + "</span>";
    return '<span lang="te">' + esc(te) + '</span><span class="e" lang="en">' + esc(en) + "</span>";
  }
  function T1(en, te) { return st.lang === "en" ? en : te; } // one-line UI text
  function url(n) {
    return D.deckUrl.replace("__DECK__", n.k === "am" ? "amendments" : "cases") + "?open=" + encodeURIComponent(n.id) + "&back=trees:" + st.tab;
  }
  function decade(y) { return y < 1950 ? 1940 : Math.floor(y / 10) * 10; }
  function decLabel(d) { return d === 1940 ? "Before 1950" : d + "s"; }

  function match(n) {
    if (st.tab === "am" && n.k !== "am") return false;
    if (st.tab === "case" && n.k !== "case") return false;
    if (st.pyq && !n.q) return false;
    if (n.old && !st.old && !(st.q && !/^\d+$/.test(st.q))) return false;
    if (st.chip) { if (st.tab === "am" && n.p !== st.chip) return false; if (st.tab === "case" && n.th !== st.chip) return false; }
    if (st.q) {
      var q = st.q.toLowerCase();
      if (/^\d+$/.test(q)) return n.k === "am" ? String(n.no) === q : String(n.y) === q;
      var hay = (n.n[0] + " " + n.n[1] + " " + (n.pop ? n.pop[0] + " " + n.pop[1] : "")).toLowerCase();
      if (hay.indexOf(q) < 0) return false;
    }
    return true;
  }
  function tags(n) {
    var t = "";
    if (n.k === "am" && n.p) t += '<span class="tg pt">' + esc(n.p) + "</span>";
    if (n.k === "case" && TH[n.th]) t += '<span class="tg th" style="--a:' + TH[n.th][3] + ";--b:" + TH[n.th][4] + '">' + esc(T1(TH[n.th][1], TH[n.th][2])) + "</span>";
    if (n.pop && st.lang !== "te") t += '<span class="tg pop">' + esc(n.pop[0]) + "</span>";
    if (n.q) t += '<span class="tg q" title="Asked in ' + n.q + ' previous papers">PYQ ' + n.q + "</span>";
    return t;
  }
  function rels(n) { // Together view only: up to 2 forward links (a case Parliament answered; an amendment a later case tested)
    if (st.tab !== "both" || !n.r) return "";
    var out = n.r.filter(function (r) { return BY[r[0]]; }).map(function (r) {
      var m = BY[r[0]];
      return '<a class="rl ' + m.k + '" href="#n-' + esc(m.id) + '" data-go="' + esc(m.id) + '"><span class="rv">' + esc(T1(r[1], r[2])) + '</span> <span class="rt">' + esc(T1(m.n[0], m.n[1])) + " (" + m.y + ")</span></a>";
    }).join("");
    return out ? '<div class="rls">' + out + "</div>" : "";
  }
  function node(n, first) { // every node carries its own year; the first of a year gets the full-size marker
    return '<li class="nd ' + n.k + (first ? " fy" : "") + '" id="n-' + esc(n.id) + '"><span class="yr">' + n.y + '</span><i class="mk ' + n.k + '" aria-hidden="true"></i>' +
      '<div class="bx"><a class="cd" href="' + esc(url(n)) + '" data-id="' + esc(n.id) + '"><b class="nm">' + T(n.n) + '</b><span class="ln">' + T(n.l) + '</span><span class="tgs">' + tags(n) + "</span></a>" + rels(n) + "</div></li>";
  }

  function chips() {
    var list = st.tab === "am" ? DATA.parts.map(function (p) { return [p[0], p[0], p[0], p[3], p[4]]; }) : st.tab === "case" ? DATA.themes.map(function (t) { return [t[0], t[1], t[2], t[3], t[4]]; }) : [];
    chipsEl.hidden = !list.length;
    if (list.length && !list.some(function (c) { return c[0] === st.chip; })) st.chip = "";
    chipsEl.innerHTML = list.length ? '<button type="button" data-chip="" aria-pressed="' + (!st.chip) + '">' + esc(T1("All", "అన్నీ")) + "</button>" + list.map(function (c) {
      return '<button type="button" data-chip="' + esc(c[0]) + '" aria-pressed="' + (st.chip === c[0]) + '" style="--a:' + c[3] + ";--b:" + c[4] + '">' + esc(T1(c[1], c[2])) + "</button>";
    }).join("") : "";
  }

  var job = 0;
  function render() {
    job++;
    root.dataset.lang = st.lang; root.dataset.tab = st.tab;
    langBtn.textContent = LNAME[st.lang];
    document.querySelectorAll(".tr-tabs [role=tab]").forEach(function (b) { b.setAttribute("aria-selected", b.dataset.tab === st.tab); });
    var isLines = st.tab === "lines";
    root.querySelector(".tr-tools").classList.toggle("only-lang", isLines);
    if (isLines) { sheet.hidden = true; fBtn.setAttribute("aria-expanded", "false"); }
    oldEl.closest("label").hidden = st.tab === "am";
    if (isLines) { chipsEl.hidden = true; jump.innerHTML = ""; return renderLines(); }
    chips();
    var nf = (st.chip ? 1 : 0) + (st.pyq ? 1 : 0) + (st.old ? 1 : 0);
    fN.hidden = !nf; fN.textContent = nf;
    var list = NODES.filter(match), groups = [], g = null;
    var hid = st.old || st.tab === "am" ? 0 : NODES.filter(function (n) { return n.old && (st.tab !== "case" || n.k === "case"); }).length;
    list.forEach(function (n) { var d = decade(n.y); if (!g || g.d !== d) groups.push(g = { d: d, ns: [] }); g.ns.push(n); });
    var am = 0, cs = 0; list.forEach(function (n) { if (n.k === "am") am++; else cs++; });
    countEl.classList.toggle("on", !!(st.q || nf));
    countEl.innerHTML = esc(st.tab === "am" ? am + T1(" amendments", " సవరణలు") : st.tab === "case" ? cs + T1(" cases", " కేసులు") : am + T1(" amendments, ", " సవరణలు, ") + cs + T1(" cases", " కేసులు")) +
      (hid ? ' <button type="button" class="tr-old" data-old="1">' + esc(T1("+ " + hid + " pre-1950 & foreign cases", "+ " + hid + " 1950 ముందువి, విదేశీ కేసులు")) + "</button>" : st.old && st.tab !== "am" ? ' <button type="button" class="tr-old" data-old="0">' + esc(T1("Hide pre-1950 cases", "1950 ముందువి దాచు")) + "</button>" : "");
    jump.innerHTML = groups.map(function (g) { return '<a href="#d-' + g.d + '">' + decLabel(g.d) + "</a>"; }).join("");
    if (!groups.length) { body.innerHTML = '<p class="tr-empty">' + esc(T1("Nothing matches. Clear the search or pick All.", "ఏదీ సరిపోలలేదు. వెతుకుడు తీసివేయండి లేదా ‘అన్నీ’ ఎంచుకోండి.")) + "</p>"; return; }
    body.innerHTML = groups.map(function (g) {
      return '<section class="dc" id="d-' + g.d + '"><h2 class="dh"><span class="dn">' + decLabel(g.d) + '</span><span class="dk">' + g.ns.length + "</span></h2><ol class=\"tl\"></ol></section>";
    }).join("");
    // lazy fill: first decades now, the rest in later frames
    var my = job, i = 0, secs = body.querySelectorAll(".tl");
    (function step() {
      if (my !== job) return;
      var t0 = Date.now();
      while (i < groups.length && (Date.now() - t0 < 12 || i < 2)) {
        var last = 0;
        secs[i].innerHTML = groups[i].ns.map(function (n) { var s = n.y !== last; last = n.y; return node(n, s); }).join("");
        i++;
      }
      if (i < groups.length) requestAnimationFrame(step); else restore();
    })();
  }

  function renderLines() {
    countEl.textContent = "";
    if (!st.chains) {
      body.innerHTML = '<p class="tr-empty">' + esc(T1("Loading lineages…", "వంశ వృక్షాలు లోడ్ అవుతున్నాయి…")) + "</p>";
      fetch(D.chainsUrl).then(function (r) { if (!r.ok) throw 0; return r.json(); }).then(function (c) { st.chains = c; if (st.tab === "lines") render(); })
        .catch(function () { body.innerHTML = '<p class="tr-empty">' + esc(T1("Lineages did not load. Check the connection and open the tab again.", "లోడ్ కాలేదు. ఇంటర్నెట్ చూసి మళ్ళీ ఈ ట్యాబ్ తెరవండి.")) + "</p>"; });
      return;
    }
    countEl.textContent = st.chains.length + T1(" lineages — how one question moved between Court and Parliament", " వృక్షాలు — ఒకే ప్రశ్న కోర్టు, పార్లమెంటు మధ్య ఎలా సాగిందో");
    jump.innerHTML = st.chains.map(function (c) { return '<a href="#c-' + esc(c.id) + '">' + esc(T1(c.sh[0], c.sh[1])) + "</a>"; }).join("");
    body.innerHTML = st.chains.map(function (c) {
      return '<section class="ch" id="c-' + esc(c.id) + '"><h2 class="chh">' + T(c.t) + '</h2><p class="chi">' + T(c.i) + '</p><ol class="lt">' + c.st.map(function (s, i) {
        var n = s.id && BY[s.id], k = s.k === "amendment" ? "am" : s.k === "case" ? "case" : "ev";
        var inner = '<span class="ly">' + (s.y || "") + '</span><b class="nm">' + T(s.n) + '</b><span class="ln">' + T(s.s) + "</span>";
        return '<li class="ls ' + k + '">' + (i ? '<span class="who">' + esc(T1(s.w[0], s.w[1])) + "</span>" : "") + '<i class="mk ' + k + '" aria-hidden="true"></i>' +
          (n ? '<a class="cd" href="' + esc(url(n)) + '" data-id="' + esc(n.id) + '">' + inner + "</a>" : '<div class="cd ev">' + inner + "</div>") + "</li>";
      }).join("") + "</ol></section>";
    }).join("");
    restore();
  }

  function findNode(p) {
    var id = String(p.id).replace(/"/g, ""), box = p.cid && document.getElementById(p.cid);
    return (box && box.querySelector('[data-id="' + id + '"]')) || document.getElementById("n-" + id) || body.querySelector('[data-id="' + id + '"]');
  }
  function scroller(el) { // the page scrolls inside <main> in this layout, not the window
    for (var n = el.parentElement; n && n !== document.body; n = n.parentElement) {
      var o = getComputedStyle(n).overflowY;
      if ((o === "auto" || o === "scroll") && n.scrollHeight > n.clientHeight) return n;
    }
    return document.scrollingElement || document.documentElement;
  }
  var hlT = 0;
  function flash(el) {
    body.querySelectorAll(".hl").forEach(function (x) { x.classList.remove("hl"); });
    var it = el.closest(".nd,.ls") || el; it.classList.add("hl");
    clearTimeout(hlT); hlT = setTimeout(function () { it.classList.remove("hl"); }, 2600);
  }
  function restore() { // put the opened node back exactly where it was on screen, and flash it
    var p = pend; if (!p) return;
    pend = null;
    var el = findNode(p); if (!el) return;
    var sc = scroller(el), want = p.top != null ? p.top : window.innerHeight / 2 - 40, n = 0;
    // decades above use content-visibility, so their real height lands a frame or two after the jump: re-aim until steady
    (function aim() { var d = el.getBoundingClientRect().top - want; if (Math.abs(d) > 2) sc.scrollTop += d; if (n++ < 12 && (Math.abs(d) > 2 || n < 4)) requestAnimationFrame(aim); })();
    flash(el);
  }
  window.addEventListener("pageshow", function (e) { // restored from the back-forward cache: same scroll, just flash the node
    if (!e.persisted) return;
    var s = history.state && history.state.tr; if (!s) return;
    var el = findNode(s); if (el) flash(el);
  });

  document.querySelector(".tr-tabs").addEventListener("click", function (e) {
    var b = e.target.closest("[data-tab]"); if (!b || b.dataset.tab === st.tab) return;
    st.tab = b.dataset.tab; st.chip = "";
    try { history.replaceState(null, "", "#" + st.tab); } catch (er) { /* ignore */ }
    render();
  });
  document.querySelector(".tr-tabs").addEventListener("keydown", function (e) {
    if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
    var bs = [].slice.call(this.querySelectorAll("[role=tab]")), i = bs.indexOf(document.activeElement);
    if (i < 0) return; var nb = bs[(i + (e.key === "ArrowRight" ? 1 : bs.length - 1)) % bs.length]; nb.focus(); nb.click();
  });
  chipsEl.addEventListener("click", function (e) { var b = e.target.closest("[data-chip]"); if (!b) return; st.chip = b.dataset.chip; render(); });
  var qt; qEl.addEventListener("input", function () { clearTimeout(qt); qt = setTimeout(function () { st.q = qEl.value.trim(); render(); }, 160); });
  pyqEl.addEventListener("change", function () { st.pyq = pyqEl.checked; render(); });
  function setOld(v) { st.old = v; oldEl.checked = v; set(OKEY, v ? "1" : "0"); render(); }
  oldEl.addEventListener("change", function () { setOld(oldEl.checked); });
  countEl.addEventListener("click", function (e) { var b = e.target.closest("[data-old]"); if (b) setOld(b.dataset.old === "1"); });
  fBtn.addEventListener("click", function () { var o = sheet.hidden; sheet.hidden = !o; fBtn.setAttribute("aria-expanded", String(o)); });
  langBtn.addEventListener("click", function () { st.lang = LANGS[(LANGS.indexOf(st.lang) + 1) % 3]; set(LKEY, st.lang); render(); });
  body.addEventListener("click", function (e) {
    var go = e.target.closest("[data-go]");
    if (go) {
      e.preventDefault();
      var el = document.getElementById("n-" + go.dataset.go);
      if (!el && st.tab !== "both") { st.tab = "both"; st.chip = ""; st.q = ""; qEl.value = ""; history.replaceState(null, "", "#both"); render(); el = document.getElementById("n-" + go.dataset.go); }
      if (!el) { st.pyq = false; pyqEl.checked = false; if (BY[go.dataset.go] && BY[go.dataset.go].old) { st.old = true; oldEl.checked = true; } render(); el = document.getElementById("n-" + go.dataset.go); }
      var tries = 0; (function find() { el = document.getElementById("n-" + go.dataset.go); if (el) { el.scrollIntoView({ block: "center", behavior: "smooth" }); body.querySelectorAll(".hl").forEach(function (x) { x.classList.remove("hl"); }); el.classList.add("hl"); } else if (tries++ < 30) requestAnimationFrame(find); })();
      return;
    }
    var a = e.target.closest("a.cd[data-id]");
    if (a) { // remember the exact view in this history entry, and tell the card page it was reached from here
      var ch = a.closest(".ch"), u = new URL(a.href, location.href);
      try { history.replaceState({ tr: { id: a.dataset.id, cid: ch ? ch.id : "", tab: st.tab, chip: st.chip, q: st.q, pyq: st.pyq, old: st.old, lang: st.lang, sheet: !sheet.hidden, top: (a.closest(".nd,.ls") || a).getBoundingClientRect().top } }, "", "#" + st.tab); } catch (er) { /* ignore */ }
      sset(NAV, JSON.stringify({ to: u.pathname + u.search }));
    }
  });
  render();
})();
