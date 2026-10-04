"""Exam session routes: start, take, answer, submit, results."""
import uuid
from datetime import datetime
from flask import (
    Blueprint, render_template, request, jsonify,
    redirect, url_for, abort
)
from ..db import db
from ..services import exam_rules, qdisplay
from ..models import (
    Exam, ExamPaper, ExamSection, ExamSyllabusItem,
    Question, ExamSession,
)

bp = Blueprint("exam_session", __name__)


def _device_id():
    return request.cookies.get("device_id", "anon")


# ── Start an exam session ─────────────────────────────────────────

@bp.route("/exam/<slug>/paper/<int:paper_num>/start", methods=["POST"])
def start(slug, paper_num):
    """Create an ExamSession and redirect to the take page.

    ``mode=official`` is allowed only for papers whose rules are verified (``exam_rules.VERIFIED_RULES``, empty for now).
    The default ``mode=practice`` builds an unofficial test of a user-chosen, capped size from the answerable questions
    of the paper's syllabus chapters, spread over its sections. A session never holds every eligible question.
    """
    exam = Exam.query.filter_by(slug=slug).first_or_404()
    paper = ExamPaper.query.filter_by(exam_id=exam.id, paper_num=paper_num).first_or_404()
    mode = request.form.get("mode", "practice")
    rules = exam_rules.verified_rules(slug, paper_num)
    if mode == "official":
        if rules is None:
            abort(403, "The official test is not available: its question count, duration and negative marking "
                       "have not been verified yet. Start an unofficial practice test instead.")
        count, minutes = rules["question_count"], rules["duration_min"]
    elif mode == "practice":
        try:
            count, minutes = exam_rules.clamp_practice(request.form.get("count"), request.form.get("minutes"))
        except ValueError:
            abort(400, "Question count and minutes must be numbers.")
    else:
        abort(400, "Unknown mode.")

    # answerable questions per section (options exist and the correct answer is one of them)
    per_section = []
    for section in ExamSection.query.filter_by(paper_id=paper.id).all():
        chapter_ids = [i.chapter_id for i in ExamSyllabusItem.query.filter_by(section_id=section.id).all()]
        if not chapter_ids:
            continue
        rows = Question.query.filter(Question.chapter_id.in_(chapter_ids)).order_by(Question.id).all()
        per_section.append([q.id for q in rows if qdisplay.is_answerable(q)])
    seed = uuid.uuid4().int % (2 ** 31)
    question_ids = exam_rules.pick_questions(per_section, count, seed)
    if not question_ids:
        abort(400, "No answerable questions are mapped to this paper's syllabus yet.")

    unofficial = mode != "official"
    session_id = str(uuid.uuid4())
    es = ExamSession(
        id=session_id,
        device_id=_device_id(),
        config={
            "exam_slug": slug,
            "exam_name_en": exam.name_en,
            "exam_name_te": exam.name_te,
            "paper_num": paper_num,
            "paper_name_en": paper.name_en,
            "paper_name_te": paper.name_te,
            "unofficial": unofficial,
            "mode": mode,
            "question_count": len(question_ids),
            "requested_count": count,
            "duration_min": minutes,
            # the seeded paper marks are unverified, so they are not copied into a session
            "total_marks": None,
            "negative_marking": None,
            "rules_source": rules["source"] if rules else None,
            "seed": seed,
        },
        question_ids=question_ids,
        answers={},
        confidences={},
    )
    db.session.add(es)
    db.session.commit()
    return redirect(url_for("exam_session.take", session_id=session_id))


# ── Take exam ────────────────────────────────────────────────────

@bp.route("/exam-session/<session_id>")
def take(session_id):
    es = ExamSession.query.get_or_404(session_id)
    if es.submitted_at:
        return redirect(url_for("exam_session.results", session_id=session_id))

    q_idx = int(request.args.get("q", 1))
    q_idx = max(1, min(q_idx, len(es.question_ids)))
    current_qid = es.question_ids[q_idx - 1]
    question = Question.query.get_or_404(current_qid)

    elapsed_seconds = int(
        (datetime.utcnow() - es.started_at).total_seconds()
    )
    duration_seconds = es.config.get("duration_min", 150) * 60
    remaining_seconds = max(0, duration_seconds - elapsed_seconds)

    return render_template(
        "exam_session/take.html",
        es=es,
        question=question,
        q_idx=q_idx,
        q_total=len(es.question_ids),
        remaining_seconds=remaining_seconds,
        answered_count=len(es.answers),
        current_answer=es.answers.get(str(current_qid)),
    )


# ── Record an answer (AJAX) ───────────────────────────────────────

@bp.route("/exam-session/<session_id>/answer", methods=["POST"])
def answer(session_id):
    es = ExamSession.query.get_or_404(session_id)
    if es.submitted_at:
        return jsonify({"error": "already submitted"}), 400

    payload = request.get_json(force=True, silent=True) or {}
    qid = str(payload.get("question_id", ""))
    chosen = (payload.get("chosen") or "").lower()
    confidence = int(payload.get("confidence") or 0)

    if not qid or chosen not in ("a", "b", "c", "d", "e", ""):
        return jsonify({"error": "invalid payload"}), 400

    # Update answers dict (merge, not replace)
    answers = dict(es.answers or {})
    confidences = dict(es.confidences or {})
    if chosen:
        answers[qid] = chosen
        if confidence:
            confidences[qid] = confidence
    else:
        # Empty chosen = clear answer
        answers.pop(qid, None)
        confidences.pop(qid, None)

    es.answers = answers
    es.confidences = confidences
    db.session.commit()
    return jsonify({"saved": True, "answered_count": len(answers)})


# ── Submit exam ──────────────────────────────────────────────────

@bp.route("/exam-session/<session_id>/submit", methods=["POST"])
def submit(session_id):
    es = ExamSession.query.get_or_404(session_id)
    if es.submitted_at:
        return redirect(url_for("exam_session.results", session_id=session_id))

    # Score it
    score = 0
    for qid_str, chosen in (es.answers or {}).items():
        q = Question.query.get(int(qid_str))
        if q and chosen == q.correct_answer:
            score += 1

    es.submitted_at = datetime.utcnow()
    es.score = score
    es.total = len(es.question_ids)
    db.session.commit()
    return redirect(url_for("exam_session.results", session_id=session_id))


# ── Results ──────────────────────────────────────────────────────

@bp.route("/exam-session/<session_id>/results")
def results(session_id):
    es = ExamSession.query.get_or_404(session_id)
    if not es.submitted_at:
        return redirect(url_for("exam_session.take", session_id=session_id))

    # Build per-question review data
    review = []
    for qid in es.question_ids:
        q = Question.query.get(qid)
        if not q:
            continue
        chosen = (es.answers or {}).get(str(qid))
        correct = chosen == q.correct_answer if chosen else False
        review.append({
            "question": q,
            "chosen": chosen,
            "correct": correct,
            "skipped": chosen is None,
        })

    attempted = sum(1 for r in review if not r["skipped"])
    correct = sum(1 for r in review if r["correct"])
    wrong = attempted - correct
    skipped = len(review) - attempted
    pct = round(correct / max(len(review), 1) * 100)
    duration = None
    if es.submitted_at and es.started_at:
        delta = es.submitted_at - es.started_at
        total_s = int(delta.total_seconds())
        duration = f"{total_s // 60}m {total_s % 60}s"

    return render_template(
        "exam_session/results.html",
        es=es,
        review=review,
        attempted=attempted,
        correct=correct,
        wrong=wrong,
        skipped=skipped,
        pct=pct,
        duration=duration,
    )
