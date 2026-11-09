// AI teacher chat for Unit 6 descriptive answers. The page sends only the item id; the server reads question and model answer itself.
(function () {
  "use strict";
  var PROMPTS = [
    ["సులభ తెలుగులో", "Explain this answer in simple, natural Telugu like a teacher, step by step."],
    ["తెలుగు + English", "Explain this answer bilingually (simple Telugu first, then English for each point), point by point, like a teacher."],
    ["Simple English", "Explain this answer in simple English like a teacher, step by step."],
    ["గుర్తుంచుకునే ట్రిక్", "Give me an easy way or mnemonic to remember this answer, in Telugu and English."],
    ["150 పదాల జవాబు", "Rewrite this as an exam-ready answer of about 150 words in English, then give the Telugu version."],
    ["ఉదాహరణలు", "Give 3 relevant examples or case laws to add marks to this answer, with a short Telugu note for each."]
  ];
  function csrf() { var m = document.querySelector('meta[name="csrf-token"]'); return m ? m.content : ""; }
  function post(body) {
    return fetch("/api/ai/chat", { method: "POST", credentials: "same-origin", headers: { "Content-Type": "application/json", "X-CSRF-Token": csrf() }, body: JSON.stringify(body) })
      .then(function (r) { if (!r.ok) throw new Error("http " + r.status); return r.json(); });
  }
  function el(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt) e.textContent = txt; return e; }
  function build(box) {
    var id = box.dataset.did, hist = [];
    var body = el("div", "aid-body"), chips = el("div", "aid-chips"), log = el("div", "aid-log"), form = el("form", "aid-form");
    log.setAttribute("aria-live", "polite");
    var input = el("textarea", "aid-in"); input.rows = 2; input.maxLength = 500; input.placeholder = "మీ ప్రశ్న లేదా సూచన రాయండి · Type your own prompt";
    var send = el("button", "btn primary", "పంపు · Send"); send.type = "submit";
    form.appendChild(input); form.appendChild(send);
    function line(who, txt) { var d = el("div", "aid-" + who, txt); log.appendChild(d); if (d.scrollIntoView) d.scrollIntoView({ block: "nearest" }); return d; }
    function ask(m) {
      m = (m || "").trim(); if (!m || send.disabled) return;
      line("me", m); input.value = ""; send.disabled = true; var wait = line("ai", "…");
      post({ polity_desc_id: id, message: m, history: hist.slice(-8) }).then(function (r) {
        wait.textContent = r.reply || ""; hist.push({ role: "user", content: m }, { role: "assistant", content: r.reply || "" });
      }).catch(function (err) {
        var s = String(err && err.message || "");
        wait.textContent = s.indexOf("429") > -1 ? "ఈ రోజు చాట్ పరిమితి అయిపోయింది. · Today's chat limit is used up."
          : s.indexOf("400") > -1 ? "సందేశం చాలా పొడవుగా ఉంది (500 అక్షరాలు). · Message too long (max 500 characters)."
          : "ఇప్పుడు AI చాట్ అందుబాటులో లేదు. · AI chat is not available right now.";
      }).then(function () { send.disabled = false; });
    }
    PROMPTS.forEach(function (p) { var b = el("button", "aid-chip", p[0]); b.type = "button"; b.addEventListener("click", function () { ask(p[1]); }); chips.appendChild(b); });
    form.addEventListener("submit", function (e) { e.preventDefault(); ask(input.value); });
    body.appendChild(el("p", "small", "ఒక సూచన నొక్కండి లేదా మీ సొంత ప్రశ్న రాయండి; తర్వాత చాట్ కొనసాగించవచ్చు. · Tap a prompt or type your own, then keep chatting."));
    body.appendChild(chips); body.appendChild(log); body.appendChild(form);
    box.appendChild(body);
  }
  document.querySelectorAll("details.aid").forEach(function (box) {
    box.addEventListener("toggle", function () { if (box.open && !box.dataset.built) { box.dataset.built = "1"; build(box); } });
  });
})();
