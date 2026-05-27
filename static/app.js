// APPSC prep · v3 · Phase 1 · vanilla JS only
(function () {
  "use strict";

  // ── Device id (cookie, set once) ───────────────────────────
  function ensureDeviceId() {
    if (!document.cookie.match(/(?:^|; )device_id=/)) {
      const id = "d-" + Math.random().toString(36).slice(2) + Date.now().toString(36);
      document.cookie = "device_id=" + id + "; path=/; max-age=31536000; SameSite=Lax";
    }
  }

  // ── Drawer open/close ──────────────────────────────────────
  function bindDrawer() {
    const drawer = document.getElementById("drawer");
    const backdrop = document.getElementById("drawer-backdrop");
    const openBtn = document.getElementById("open-menu");
    const closeBtn = document.getElementById("drawer-close");
    if (!drawer || !backdrop) return;

    function open() {
      drawer.dataset.open = "true";
      drawer.setAttribute("aria-hidden", "false");
      backdrop.hidden = false;
      requestAnimationFrame(() => backdrop.dataset.open = "true");
    }
    function close() {
      drawer.dataset.open = "false";
      drawer.setAttribute("aria-hidden", "true");
      backdrop.dataset.open = "false";
      setTimeout(() => { backdrop.hidden = true; }, 200);
    }
    if (openBtn) openBtn.addEventListener("click", open);
    if (closeBtn) closeBtn.addEventListener("click", close);
    backdrop.addEventListener("click", close);
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") close(); });
  }

  // ── Question card: select option + confidence + submit ─────
  function bindQuestionCard() {
    const card = document.getElementById("qcard");
    if (!card) return;
    const submitBtn = document.getElementById("submit-btn");
    const options = card.querySelectorAll(".option");
    const confPills = card.querySelectorAll(".conf-pill");
    const feedback = document.getElementById("feedback");
    const feedbackMsg = document.getElementById("feedback-msg");

    let chosen = null;
    let confidence = null;

    function refreshSubmit() {
      submitBtn.disabled = !(chosen && confidence);
    }

    options.forEach((opt) => {
      opt.addEventListener("click", () => {
        if (card.dataset.submitted === "true") return;
        options.forEach((o) => o.setAttribute("aria-checked", "false"));
        opt.setAttribute("aria-checked", "true");
        chosen = opt.dataset.key;
        refreshSubmit();
      });
    });

    confPills.forEach((pill) => {
      pill.addEventListener("click", () => {
        if (card.dataset.submitted === "true") return;
        confPills.forEach((p) => p.setAttribute("aria-checked", "false"));
        pill.setAttribute("aria-checked", "true");
        confidence = parseInt(pill.dataset.conf, 10);
        refreshSubmit();
      });
    });

    submitBtn.addEventListener("click", async () => {
      if (!chosen || !confidence) return;
      submitBtn.disabled = true;
      submitBtn.textContent = "Submitting…";

      let res;
      try {
        res = await fetch("/api/answer", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            question_id: parseInt(card.dataset.questionId, 10),
            chosen, confidence,
          }),
        });
      } catch (e) {
        submitBtn.disabled = false;
        submitBtn.textContent = "Submit failed — retry";
        return;
      }
      const data = await res.json();
      card.dataset.submitted = "true";

      // Mark options
      options.forEach((opt) => {
        const k = opt.dataset.key;
        if (k === data.correct_answer) opt.classList.add("is-correct");
        else if (k === data.chosen) opt.classList.add("is-wrong");
        else opt.classList.add("is-dim");
      });

      // Coaching message
      feedbackMsg.classList.add(data.correct ? "is-correct" : "is-wrong");
      const langPref = document.body.dataset.lang || "both";
      const teLine = `<div>${data.coaching_te}</div>`;
      const enLine = `<div style="margin-top:4px;opacity:.85">${data.coaching_en}</div>`;
      if (langPref === "te") feedbackMsg.innerHTML = teLine;
      else if (langPref === "en") feedbackMsg.innerHTML = enLine;
      else feedbackMsg.innerHTML = teLine + enLine;

      feedback.hidden = false;
      submitBtn.hidden = true;
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    ensureDeviceId();
    bindDrawer();
    bindQuestionCard();
  });
})();
