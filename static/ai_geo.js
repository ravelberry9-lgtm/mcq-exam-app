// AI check + follow-up chat for Group 2 Geography question pages (same server endpoints as the practice pages).
// The page sends only the lesson number and question id; the server reads the question from its own files.
(function () {
  "use strict";
  var box = document.getElementById("aichk");
  if (!box) return;
  var ref = { geo_lesson: parseInt(box.dataset.lesson, 10), geo_qid: box.dataset.qid };
  function csrf() { var m = document.querySelector('meta[name="csrf-token"]'); return m ? m.content : ""; }
  function post(url, body) {
    return fetch(url, { method: "POST", credentials: "same-origin", headers: { "Content-Type": "application/json", "X-CSRF-Token": csrf() }, body: JSON.stringify(body) })
      .then(function (r) { if (!r.ok) throw new Error("http " + r.status); return r.json(); });
  }
  var chatForm = document.getElementById("aichat-form"), chatIn = document.getElementById("aichat-in"), chatLog = document.getElementById("aichat-log"),
    chatSend = document.getElementById("aichat-send"), chatWeb = document.getElementById("aichat-web"), chatHist = [];
  function chatLine(who, txt) {
    var d = document.createElement("div"); d.className = "aichat-" + who; d.textContent = txt;
    d.style.cssText = "margin-top:6px;padding:8px 10px;border-radius:10px;white-space:pre-wrap;" + (who === "me" ? "background:rgba(127,127,127,.18);margin-left:24px" : "background:rgba(127,127,127,.08);margin-right:24px");
    chatLog.appendChild(d); if (d.scrollIntoView) d.scrollIntoView({ block: "nearest" }); return d;
  }
  if (chatForm) chatForm.addEventListener("submit", function (e) {
    e.preventDefault(); var m = chatIn.value.trim(); if (!m || chatSend.disabled) return;
    var useWeb = !!(chatWeb && chatWeb.checked);
    chatLine("me", m); chatIn.value = ""; chatSend.disabled = true; var wait = chatLine("ai", useWeb ? "🌐 …" : "…");
    post("/api/ai/chat", Object.assign({ message: m, history: chatHist.slice(-8), web: useWeb }, ref)).then(function (r) {
      wait.textContent = r.reply || "";
      if (r.sources && r.sources.length) {
        var b = document.createElement("div"); b.style.cssText = "margin-top:8px;font-size:13px"; b.appendChild(document.createTextNode("🌐 వెబ్ మూలాలు · Web sources:"));
        r.sources.forEach(function (s) { if (!/^https?:\/\//.test(s.url)) return; var a = document.createElement("a"); a.href = s.url; a.target = "_blank"; a.rel = "noopener noreferrer"; a.textContent = s.title || s.url; a.style.cssText = "display:block;overflow-wrap:anywhere;text-decoration:underline;color:inherit"; b.appendChild(a); });
        wait.appendChild(b);
      }
      chatHist.push({ role: "user", content: m }, { role: "assistant", content: r.reply || "" });
    }).catch(function (err) {
      var s = String(err && err.message || "");
      wait.textContent = s.indexOf("429") > -1 && useWeb ? "ఈ రోజు వెబ్ శోధన పరిమితి అయిపోయింది — టిక్ తీసేసి అడగండి. · Today's web search limit is used up. Untick the box and ask again."
        : s.indexOf("429") > -1 ? "ఈ రోజు చాట్ పరిమితి అయిపోయింది. · Today's chat limit is used up."
        : s.indexOf("400") > -1 ? "సందేశం చాలా పొడవుగా ఉంది. · That message is too long (max 500 characters)."
        : "ఇప్పుడు AI చాట్ అందుబాటులో లేదు. · AI chat is not available right now.";
    }).then(function () { chatSend.disabled = false; });
  });
  var aiBtn = document.getElementById("aichk-btn"), aiOut = document.getElementById("aichk-out");
  if (aiBtn && aiOut) aiBtn.addEventListener("click", function () {
    aiBtn.disabled = true; aiOut.hidden = false; aiOut.textContent = "తనిఖీ చేస్తున్నాను… Checking…";
    post("/api/ai/check", ref).then(function (r) {
      var badge = { agrees: "✅ AI ఏకీభవిస్తోంది · AI agrees with the answer key", disagrees: "⚠️ AI ఏకీభవించలేదు · AI disagrees with the answer key", unsure: "❓ AI ఖచ్చితంగా చెప్పలేదు · AI is not sure" }[r.verdict] || "";
      aiOut.textContent = "";
      function line(txt, bold) { var d = document.createElement(bold ? "strong" : "div"); d.textContent = txt; d.style.display = "block"; d.style.marginTop = "4px"; aiOut.appendChild(d); }
      line(badge, true);
      if (r.verdict !== "agrees" && r.your_answer) line("AI: " + r.your_answer + " · Key: " + r.stored_answer);
      if (r.te) line(r.te); if (r.en) line(r.en);
      (r.issues || []).forEach(function (i) { line("• " + i); });
      line("AI సలహా మాత్రమే — సందేహం ఉంటే నోట్స్ చూడండి. · AI advice only; verify in your notes.");
    }).catch(function () {
      aiOut.textContent = "ఇప్పుడు AI తనిఖీ అందుబాటులో లేదు. · AI check is not available right now."; aiBtn.disabled = false;
    });
  });
})();
