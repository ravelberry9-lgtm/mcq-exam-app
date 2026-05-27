"""Public routes: home, subjects, practice, exam, settings, answer API."""
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, make_response
from sqlalchemy import func
from datetime import datetime
from ..db import db
from ..models import (
    Subject, Chapter, Question, UserQuestionState,
    Exam, ExamPaper, ExamSection, ExamSyllabusItem,
)

bp = Blueprint("public", __name__)

DIFFICULTY_LABEL = {
    "E": "Easy · సులభం",
    "M": "Medium · మధ్యమం",
    "H": "Hard · కష్టం",
}


def _device_id():
    return request.cookies.get("device_id", "anon")


@bp.route("/")
def home():
    quick = (
        db.session.query(Subject)
        .join(Question, Question.subject_id == Subject.id)
        .group_by(Subject.id)
        .order_by(Subject.sort_order)
        .limit(4)
        .all()
    )
    return render_template("home.html", quick_subjects=quick)


@bp.route("/subjects")
def subjects():
    rows = (
        db.session.query(
            Subject,
            func.count(func.distinct(Chapter.id)).label("chapter_count"),
            func.count(func.distinct(Question.id)).label("question_count"),
        )
        .outerjoin(Chapter, Chapter.subject_id == Subject.id)
        .outerjoin(Question, Question.subject_id == Subject.id)
        .group_by(Subject.id)
        .order_by(Subject.sort_order)
        .all()
    )
    subjects_list = [
        {"slug": s.slug, "name_en": s.name_en, "name_te": s.name_te,
         "chapter_count": ch, "question_count": qc}
        for s, ch, qc in rows
    ]
    return render_template("subjects.html", subjects=subjects_list)


@bp.route("/subject/<slug>")
def subject_detail(slug):
    return redirect(url_for("public.practice", subject_slug=slug))


@bp.route("/practice/<subject_slug>")
def practice(subject_slug):
    subject = Subject.query.filter_by(slug=subject_slug).first_or_404()
    q_idx = int(request.args.get("i", 1))
    questions = Question.query.filter_by(subject_id=subject.id).order_by(Question.id).all()
    q_total = len(questions)
    if q_total == 0:
        return render_template("practice.html", subject=subject, question=None, chapter=None)
    q_idx = max(1, min(q_idx, q_total))
    question = questions[q_idx - 1]
    chapter = Chapter.query.get(question.chapter_id) if question.chapter_id else None
    if chapter is None:
        chapter = type("Anon", (), {"title_en": "—", "title_te": "—"})()
    progress_pct = round((q_idx - 1) / max(q_total, 1) * 100)
    next_url = (
        url_for("public.practice", subject_slug=subject_slug, i=q_idx + 1)
        if q_idx < q_total else url_for("public.subjects")
    )
    return render_template(
        "practice.html",
        subject=subject, chapter=chapter, question=question,
        q_index=q_idx, q_total=q_total,
        difficulty_label=DIFFICULTY_LABEL.get(question.difficulty, question.difficulty),
        progress_pct=progress_pct, next_url=next_url,
    )


@bp.route("/exam/<slug>")
def exam_detail(slug):
    """Render an exam's syllabus tree: papers -> sections -> chapters."""
    exam = Exam.query.filter_by(slug=slug).first_or_404()
    papers_data = []
    papers = ExamPaper.query.filter_by(exam_id=exam.id).order_by(ExamPaper.paper_num).all()
    for paper in papers:
        sections_data = []
        sections = ExamSection.query.filter_by(paper_id=paper.id).order_by(ExamSection.sort_order).all()
        for section in sections:
            items = ExamSyllabusItem.query.filter_by(section_id=section.id).order_by(ExamSyllabusItem.sort_order).all()
            chapters_data = []
            for item in items:
                ch = Chapter.query.get(item.chapter_id)
                if ch is None:
                    continue
                subj = Subject.query.get(ch.subject_id)
                q_count = Question.query.filter_by(chapter_id=ch.id).count()
                chapters_data.append({
                    "id": ch.id,
                    "title_en": ch.title_en, "title_te": ch.title_te,
                    "subject_slug": subj.slug if subj else "",
                    "q_count": q_count,
                })
            sections_data.append({
                "section_label": section.section_label,
                "name_en": section.name_en, "name_te": section.name_te,
                "marks": section.marks,
                "chapters": chapters_data,
            })
        papers_data.append({
            "paper_num": paper.paper_num,
            "name_en": paper.name_en, "name_te": paper.name_te,
            "total_marks": paper.total_marks, "duration_min": paper.duration_min,
            "sections": sections_data,
        })
    return render_template("exam.html", exam=exam, papers=papers_data)


@bp.route("/api/answer", methods=["POST"])
def api_answer():
    payload = request.get_json(force=True, silent=True) or {}
    qid = payload.get("question_id")
    chosen = (payload.get("chosen") or "").lower()
    confidence = int(payload.get("confidence") or 0)
    if not qid or chosen not in ("a", "b", "c", "d", "e"):
        return jsonify({"error": "invalid payload"}), 400
    q = Question.query.get_or_404(qid)
    correct = chosen == q.correct_answer

    device_id = _device_id()
    state = UserQuestionState.query.filter_by(device_id=device_id, question_id=q.id).first()
    if state is None:
        state = UserQuestionState(device_id=device_id, question_id=q.id, seen_count=0, wrong_count=0)
        db.session.add(state)
    state.seen_count = (state.seen_count or 0) + 1
    if not correct:
        state.wrong_count = (state.wrong_count or 0) + 1
    state.last_confidence = confidence
    state.last_seen_at = datetime.utcnow()
    db.session.commit()

    return jsonify({
        "correct": correct, "correct_answer": q.correct_answer,
        "chosen": chosen, "confidence": confidence,
        "coaching_te": _coaching_te(correct, confidence),
        "coaching_en": _coaching_en(correct, confidence),
    })


def _coaching_te(correct, confidence):
    if correct and confidence >= 4:
        return "మంచిది! మీరు సరెనే జవాబు ఇచ్చారు."
    if correct and confidence <= 2:
        return "సరైంది, కానీ మీ బుద్ధిని నమ్మండి."
    if not correct and confidence >= 4:
        return "మీరు ఖచ్చితంగా అన్నారు, కానీ తప్పు. నెమ్మదిగా చదవండి."
    return "తప్పయింది. వివరణ చూడండి."


def _coaching_en(correct, confidence):
    if correct and confidence >= 4:
        return "Good — your confidence matched the outcome."
    if correct and confidence <= 2:
        return "Correct, but you weren't sure. Trust your reasoning more next time."
    if not correct and confidence >= 4:
        return "You were confident but wrong — slow down on similar questions."
    return "Wrong this time. Read the explanation."


@bp.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        lang = request.form.get("lang", "both")
        if lang not in ("te", "en", "both"):
            lang = "both"
        resp = make_response(redirect(url_for("public.settings")))
        resp.set_cookie("lang", lang, max_age=60 * 60 * 24 * 365, samesite="Lax")
        return resp
    return render_template("settings.html")


@bp.route("/healthz")
def healthz():
    return {"status": "ok", "phase": "1"}, 200
