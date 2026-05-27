"""Exam session routes: start, take, answer, submit, results."""
import uuid
from datetime import datetime
from flask import (
    Blueprint, render_template, request, jsonify,
    redirect, url_for, abort
)
from ..db import db
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
    """
    Create an ExamSession and redirect to the take page.
    Picks questions from the chapters mapped in the exam syllabus.
    Config stores paper_num, total_marks, duration_min.
    """
    exam = Exam.query.filter_by(slug=slug).first_or_404()
    paper = ExamPaper.query.filter_by(
        exam_id=exam.id, paper_num=paper_num
    ).first_or_404()

    # Gather question IDs from syllabus chapters for this paper
    question_ids = []
    sections = ExamSection.query.filter_by(paper_id=paper.id).all()
    for section in sections:
        items = ExamSyllabusItem.query.filter_by(section_id=section.id).all()
        for item in items:
            qs = (
                Question.query
                .filter_by(chapter_id=item.chapter_id)
                .order_by(Question.id)
                .all()
            )
            question_ids.extend([q.id for q in qs])

    # Deduplicate preserving order
    seen = set()
    unique_ids = []
    for qid in question_ids:
        if qid not in seen:
            seen.add(qid)
            unique_ids.append(qid)

    if not unique_ids:
        abort(400, "No questions mapped to this paper's syllabus yet.")

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
            "total_marks": paper.total_marks,
            "duration_min": paper.duration_min or 150,
        },
        question_ids=unique_ids,
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

    answers = dict(es.answers or {})
    confidences = dict(es.confidences or {})
    if chosen:
        answers[qid] = chosen
        if confidence:
            confidences[qid] = confidence
    else:
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
