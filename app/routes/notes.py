"""Notes routes: chapter list + note reader + progress API."""
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from datetime import datetime
from ..db import db
from ..models import Subject, Chapter, Note, ChapterProgress

bp = Blueprint("notes", __name__, url_prefix="/notes")


def _device_id():
    return request.cookies.get("device_id", "anon")


@bp.route("/<subject_slug>")
def chapter_list(subject_slug):
    """List all chapters for a subject with progress status."""
    subject = Subject.query.filter_by(slug=subject_slug).first_or_404()
    chapters = (
        Chapter.query
        .filter_by(subject_id=subject.id)
        .order_by(Chapter.chapter_num)
        .all()
    )
    device_id = _device_id()
    # Build a progress dict keyed by chapter_id
    progress_rows = ChapterProgress.query.filter_by(device_id=device_id).all()
    progress_map = {p.chapter_id: p.status for p in progress_rows}

    chapters_with_progress = []
    for ch in chapters:
        note_count = Note.query.filter_by(chapter_id=ch.id).count()
        chapters_with_progress.append({
            "chapter": ch,
            "note_count": note_count,
            "status": progress_map.get(ch.id, "not_started"),
        })

    return render_template(
        "notes/chapter_list.html",
        subject=subject,
        chapters=chapters_with_progress,
    )


@bp.route("/<subject_slug>/<int:chapter_num>")
def reader(subject_slug, chapter_num):
    """Display all note sections for a chapter."""
    subject = Subject.query.filter_by(slug=subject_slug).first_or_404()
    chapter = (
        Chapter.query
        .filter_by(subject_id=subject.id, chapter_num=chapter_num)
        .first_or_404()
    )
    notes = (
        Note.query
        .filter_by(chapter_id=chapter.id)
        .order_by(Note.section_num)
        .all()
    )
    device_id = _device_id()
    progress = ChapterProgress.query.filter_by(
        device_id=device_id, chapter_id=chapter.id
    ).first()
    progress_status = progress.status if progress else "not_started"

    # Prev / next chapter navigation
    all_chapters = (
        Chapter.query
        .filter_by(subject_id=subject.id)
        .order_by(Chapter.chapter_num)
        .all()
    )
    nums = [c.chapter_num for c in all_chapters]
    idx = nums.index(chapter_num) if chapter_num in nums else -1
    prev_num = nums[idx - 1] if idx > 0 else None
    next_num = nums[idx + 1] if idx >= 0 and idx < len(nums) - 1 else None

    has_content = any((n.body_en or n.body_te) for n in notes)

    return render_template(
        "notes/reader.html",
        subject=subject,
        chapter=chapter,
        notes=notes,
        has_content=has_content,
        progress_status=progress_status,
        prev_num=prev_num,
        next_num=next_num,
    )


# ââ Progress API ââââââââââââââââââââââââââââââââââââââââââââââââââ

@bp.route("/api/progress/<int:chapter_id>/complete", methods=["POST"])
def progress_complete(chapter_id):
    """Upsert ChapterProgress to 'completed'."""
    chapter = Chapter.query.get_or_404(chapter_id)
    device_id = _device_id()
    prog = ChapterProgress.query.filter_by(
        device_id=device_id, chapter_id=chapter.id
    ).first()
    if prog is None:
        prog = ChapterProgress(device_id=device_id, chapter_id=chapter.id)
        db.session.add(prog)
    prog.status = "completed"
    prog.marked_complete_at = datetime.utcnow()
    prog.last_opened_at = datetime.utcnow()
    db.session.commit()
    return jsonify({"status": "completed", "chapter_id": chapter_id})


@bp.route("/api/progress/<int:chapter_id>/open", methods=["POST"])
def progress_open(chapter_id):
    """Record a chapter open â sets status to in_progress if not already completed."""
    chapter = Chapter.query.get_or_404(chapter_id)
    device_id = _device_id()
    prog = ChapterProgress.query.filter_by(
        device_id=device_id, chapter_id=chapter.id
    ).first()
    if prog is None:
        prog = ChapterProgress(device_id=device_id, chapter_id=chapter.id)
        db.session.add(prog)
    if prog.status in (None, "not_started"):
        prog.status = "in_progress"
    prog.last_opened_at = datetime.utcnow()
    db.session.commit()
    return jsonify({"status": prog.status, "chapter_id": chapter_id})
