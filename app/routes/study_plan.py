"""Study plan routes: create plan, dashboard, mark chapter done."""
from flask import (
    Blueprint, render_template, request, jsonify,
    redirect, url_for
)
from datetime import datetime, date, timedelta
from ..db import db
from ..models import (
    Exam, Subject, Chapter, ChapterProgress, StudyPlan, ExamSyllabusItem,
    ExamSection, ExamPaper,
)

bp = Blueprint("study_plan", __name__, url_prefix="/plan")


def _device_id():
    return request.cookies.get("device_id", "anon")


# ── Plan wizard ──────────────────────────────────────────────────

@bp.route("/new")
def new():
    """Show the plan creation wizard."""
    exams = Exam.query.filter_by(active=True).order_by(Exam.id).all()
    today = date.today()
    default_date = (today + timedelta(days=90)).isoformat()
    return render_template("study_plan/new.html", exams=exams,
                           today=today.isoformat(), default_date=default_date)


@bp.route("/create", methods=["POST"])
def create():
    """Create a new study plan."""
    device_id = _device_id()
    exam_id = request.form.get("exam_id") or None
    name = request.form.get("name", "").strip() or "My Study Plan"
    target_date_str = request.form.get("target_date", "")
    try:
        target_date = date.fromisoformat(target_date_str)
    except ValueError:
        target_date = date.today() + timedelta(days=90)

    if exam_id:
        exam_id = int(exam_id)

    # Pause any existing active plan for this device
    existing = StudyPlan.query.filter_by(
        device_id=device_id, status="active"
    ).all()
    for p in existing:
        p.status = "paused"

    plan = StudyPlan(
        device_id=device_id,
        exam_id=exam_id,
        name=name,
        target_date=target_date,
        status="active",
    )
    db.session.add(plan)
    db.session.commit()
    return redirect(url_for("study_plan.dashboard"))


# ── Dashboard ────────────────────────────────────────────────────

@bp.route("/")
def dashboard():
    """Show progress dashboard for active plan."""
    device_id = _device_id()
    plan = StudyPlan.query.filter_by(
        device_id=device_id, status="active"
    ).order_by(StudyPlan.id.desc()).first()

    if not plan:
        return redirect(url_for("study_plan.new"))

    chapters_data = _get_plan_chapters(plan)

    progress_rows = ChapterProgress.query.filter_by(device_id=device_id).all()
    progress_map = {p.chapter_id: p.status for p in progress_rows}

    total = len(chapters_data)
    completed = sum(
        1 for ch in chapters_data
        if progress_map.get(ch["id"]) == "completed"
    )
    in_progress = sum(
        1 for ch in chapters_data
        if progress_map.get(ch["id"]) == "in_progress"
    )
    not_started = total - completed - in_progress

    today = date.today()
    days_left = max(0, (plan.target_date - today).days)

    remaining_chapters = total - completed
    pacing = round(remaining_chapters / max(days_left, 1), 1) if days_left > 0 else remaining_chapters

    today_suggestions = [
        ch for ch in chapters_data
        if progress_map.get(ch["id"]) in (None, "not_started", "in_progress")
    ][:5]

    for ch in chapters_data:
        ch["status"] = progress_map.get(ch["id"], "not_started")

    return render_template(
        "study_plan/dashboard.html",
        plan=plan,
        chapters=chapters_data,
        total=total,
        completed=completed,
        in_progress=in_progress,
        not_started=not_started,
        days_left=days_left,
        pacing=pacing,
        today_suggestions=today_suggestions,
        completion_pct=round(completed / max(total, 1) * 100),
    )


def _get_plan_chapters(plan):
    """Return list of chapter dicts for a plan, ordered by exam syllabus or subject."""
    chapters_data = []
    seen = set()

    if plan.exam_id:
        papers = ExamPaper.query.filter_by(exam_id=plan.exam_id).order_by(ExamPaper.paper_num).all()
        for paper in papers:
            sections = ExamSection.query.filter_by(paper_id=paper.id).order_by(ExamSection.sort_order).all()
            for section in sections:
                items = ExamSyllabusItem.query.filter_by(section_id=section.id).order_by(ExamSyllabusItem.sort_order).all()
                for item in items:
                    ch = Chapter.query.get(item.chapter_id)
                    if ch and ch.id not in seen:
                        seen.add(ch.id)
                        subj = Subject.query.get(ch.subject_id)
                        chapters_data.append({
                            "id": ch.id,
                            "chapter_num": ch.chapter_num,
                            "title_en": ch.title_en,
                            "title_te": ch.title_te,
                            "subject_slug": subj.slug if subj else "",
                            "subject_en": subj.name_en if subj else "",
                            "est_read_minutes": ch.est_read_minutes or 20,
                        })
    else:
        chapters = Chapter.query.order_by(Chapter.subject_id, Chapter.chapter_num).all()
        for ch in chapters:
            if ch.id not in seen:
                seen.add(ch.id)
                subj = Subject.query.get(ch.subject_id)
                chapters_data.append({
                    "id": ch.id,
                    "chapter_num": ch.chapter_num,
                    "title_en": ch.title_en,
                    "title_te": ch.title_te,
                    "subject_slug": subj.slug if subj else "",
                    "subject_en": subj.name_en if subj else "",
                    "est_read_minutes": ch.est_read_minutes or 20,
                })

    return chapters_data


# ── API: pause / resume / delete plan ────────────────────────────

@bp.route("/api/<int:plan_id>/pause", methods=["POST"])
def pause_plan(plan_id):
    plan = StudyPlan.query.get_or_404(plan_id)
    plan.status = "paused"
    db.session.commit()
    return jsonify({"status": "paused"})


@bp.route("/api/<int:plan_id>/resume", methods=["POST"])
def resume_plan(plan_id):
    plan = StudyPlan.query.get_or_404(plan_id)
    plan.status = "active"
    db.session.commit()
    return redirect(url_for("study_plan.dashboard"))
