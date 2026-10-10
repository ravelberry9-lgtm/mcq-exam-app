// Design-system behaviour: language switch, tabs, note progress, practice. Vanilla JS, no framework.
(function () {
  "use strict";
  var root = document.documentElement;

  function cookie(name) { var m = document.cookie.match(new RegExp("(?:^|; )" + name + "=([^;]*)")); return m ? decodeURIComponent(m[1]) : null; }
  function setCookie(name, value) { document.cookie = name + "=" + encodeURIComponent(value) + "; path=/; max-age=31536000; SameSite=Lax"; }
  function announce(msg) { var l = document.getElementById("live"); if (!l) return; l.textContent = ""; setTimeout(function () { l.textContent = msg; }, 20); }
  function csrf() { var m = document.querySelector('meta[name="csrf-token"]'); return m ? m.content : ""; }
  function post(url, body) {
    return fetch(url, { method: "POST", credentials: "same-origin", headers: { "Content-Type": "application/json", "X-CSRF-Token": csrf() }, body: JSON.stringify(body || {}) })
      .then(function (r) { if (!r.ok) throw new Error("http " + r.status); return r.json(); });
  }

  // the device id is an HttpOnly cookie issued by the server (same one for the older pages); scripts never touch it

  // ── language: Telugu / English / both. Persisted in the 'lang' cookie (server reads it too). ──
  // text that is not wrapped in .en/.te spans (e.g. <option>) is relabelled here
  function relabel(v) {
    document.querySelectorAll("option[data-n]").forEach(function (o) {
      var en = o.dataset.en, te = o.dataset.te, t = v === "te" ? (te || en) : v === "en" ? (en || te) : (en && te && en !== te ? en + " / " + te : (en || te));
      o.textContent = o.dataset.n + ". " + (t || "");
    });
  }
  function applyLang(v) {
    root.setAttribute("data-lang", v); root.setAttribute("lang", v === "te" ? "te" : "en");
    relabel(v);
    document.querySelectorAll("[data-langsw] button").forEach(function (b) { b.setAttribute("aria-checked", b.dataset.v === v ? "true" : "false"); });
  }
  document.querySelectorAll("[data-langsw] button").forEach(function (b) {
    b.addEventListener("click", function () { setCookie("lang", b.dataset.v); applyLang(b.dataset.v); announce(b.getAttribute("aria-label")); });
  });

  // ── tabs ──
  document.querySelectorAll('[role="tablist"]').forEach(function (list) {
    var tabs = Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));
    function select(t) {
      tabs.forEach(function (x) { var on = x === t; x.setAttribute("aria-selected", on ? "true" : "false"); x.tabIndex = on ? 0 : -1; var p = document.getElementById(x.getAttribute("aria-controls")); if (p) p.hidden = !on; });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(t); });
      t.addEventListener("keydown", function (e) { var n = tabs.length, j = e.key === "ArrowRight" ? (i + 1) % n : e.key === "ArrowLeft" ? (i - 1 + n) % n : e.key === "Home" ? 0 : e.key === "End" ? n - 1 : -1; if (j >= 0) { e.preventDefault(); tabs[j].focus(); select(tabs[j]); } });
    });
    select(list.querySelector('[aria-selected="true"]') || tabs[0]);
  });

  // ── notes: remember the section being read; jump menu ──
  var note = document.getElementById("note");
  if (note) post("/learn/api/topic/" + note.dataset.chapter + "/section", { section: parseInt(note.dataset.section, 10) }).catch(function () {});
  var jump = document.querySelector("[data-jump]");
  if (jump) jump.addEventListener("change", function () { location.href = jump.dataset.base + "?section=" + jump.value; });

  // ── topic: mark chapter complete (existing API) ──
  var done = document.getElementById("mark-done");
  if (done) done.addEventListener("click", function () {
    post("/notes/api/progress/" + done.dataset.chapter + "/complete").then(function () { done.hidden = true; announce(done.dataset.doneMsg); location.reload(); }).catch(function () { announce(done.dataset.errMsg); done.setAttribute("data-failed", "1"); });
  });

  // ── practice ──
  function stats(topic) { try { return JSON.parse(sessionStorage.getItem("ds.p." + topic)) || { r: 0, w: 0, s: 0 }; } catch (e) { return { r: 0, w: 0, s: 0 }; } }
  function saveStats(topic, s) { try { sessionStorage.setItem("ds.p." + topic, JSON.stringify(s)); } catch (e) {} }

  var card = document.querySelector("[data-practice]");
  if (card) {
    var topic = card.dataset.topic, st = stats(topic), answered = false;
    if (card.dataset.fresh === "1") { st = { r: 0, w: 0, s: 0 }; saveStats(topic, st); history.replaceState(null, "", location.pathname + "?i=1"); }
    var go = document.getElementById("go"), expl = document.getElementById("expl"), err = document.getElementById("err");
    function state(name) { go.querySelectorAll("[data-state]").forEach(function (s) { s.hidden = s.dataset.state !== name; }); go.className = name === "skip" ? "btn grow" : "btn primary grow"; }
    document.querySelectorAll("#opts input").forEach(function (inp) {
      inp.addEventListener("change", function () {
        if (answered) return; err.hidden = true;
        post("/api/answer", { question_id: parseInt(card.dataset.qid, 10), chosen: inp.value, confidence: 0 }).then(function (res) {
          answered = true;
          document.querySelectorAll("#opts .opt").forEach(function (o) {
            var k = o.dataset.k, inpt = o.querySelector("input"), mark = o.querySelector(".state"); inpt.disabled = true;
            if (k === res.correct_answer) { o.classList.add("is-correct"); mark.textContent = k === res.chosen ? "✓" : "✓"; }
            else if (k === res.chosen) { o.classList.add("is-wrong"); mark.textContent = "✗"; }
          });
          if (res.correct) st.r++; else st.w++; saveStats(topic, st);
          expl.hidden = false; state(card.dataset.last === "1" ? "finish" : "next");
          announce(res.correct ? card.dataset.msgOk : card.dataset.msgBad); expl.scrollIntoView({ block: "nearest" });
        }).catch(function () { inp.checked = false; err.hidden = false; });
      });
    });
    go.addEventListener("click", function () { if (!answered) { st.s++; saveStats(topic, st); } location.href = card.dataset.next; });
  }

  // Science sidecar practice: reveal the answer state and a real expandable explanation.
  var scienceCard = document.querySelector("[data-science-question]");
  var scienceCheck = document.getElementById("science-check");
  if (scienceCard && scienceCheck) {
    scienceCheck.addEventListener("click", function () {
      var picked = document.querySelector('input[name="science-answer"]:checked');
      if (!picked) return;
      document.querySelectorAll("#science-options .opt").forEach(function (option) {
        var input = option.querySelector("input");
        input.disabled = true;
        if (option.dataset.k === scienceCard.dataset.correct) option.classList.add("is-correct");
        if (option.dataset.k === picked.value && picked.value !== scienceCard.dataset.correct) option.classList.add("is-wrong");
      });
      var explanation = document.getElementById("science-explanation");
      explanation.hidden = false;
      explanation.open = true;
      scienceCheck.hidden = true;
      explanation.scrollIntoView({ behavior: "smooth", block: "nearest" });
    });
  }
  var sum = document.getElementById("summary");
  if (sum) { var s = stats(sum.dataset.topic); ["r", "w", "s"].forEach(function (k) { var el = sum.querySelector('[data-stat="' + k + '"]'); if (el) el.textContent = s[k]; }); }
})();
