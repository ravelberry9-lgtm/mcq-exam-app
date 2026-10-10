"""Learner-facing Science & Technology textbook routes."""
from types import SimpleNamespace

from flask import Blueprint, abort, render_template, request, url_for

from ..services import science_content as science


bp = Blueprint("science", __name__, url_prefix="/learn/science-technology")


def _context(slug):
    meta = science.chapter(slug) or abort(404)
    book = science.load_book(slug) or abort(404)
    ch = SimpleNamespace(slug=slug, title_en=meta["title_en"], title_te=meta["title_te"])
    return meta, ch, book


@bp.get("/")
def index():
    chapters = []
    for meta in science.CHAPTERS:
        book = science.load_book(meta["slug"])
        if book:
            chapters.append({**meta, "lessons": len(book["lessons"]),
                             "questions": science.question_summary(meta["slug"])})
    return render_template("ds/science_index.html", chapters=chapters)


@bp.get("/<slug>/")
def chapter(slug):
    meta, _ch, book = _context(slug)
    return render_template("ds/science_chapter.html", meta=meta, book=book,
                           questions=science.question_summary(slug))


@bp.get("/<slug>/textbook")
def textbook_index(slug):
    _meta, ch, book = _context(slug)
    return render_template(
        "ds/textbook.html", ch=ch, book=book, lesson=None,
        integrated_bilingual=True,
        chapter_url=url_for("science.chapter", slug=slug),
        textbook_index_endpoint="science.textbook_index",
        textbook_lesson_endpoint="science.textbook_lesson")


@bp.get("/<slug>/textbook/<lesson_id>")
def textbook_lesson(slug, lesson_id):
    _meta, ch, book = _context(slug)
    for i, lesson in enumerate(book["lessons"]):
        if lesson["id"] == lesson_id:
            return render_template(
                "ds/textbook.html", ch=ch, book=book, lesson=lesson,
                integrated_bilingual=True,
                previous=book["lessons"][i - 1] if i else None,
                following=book["lessons"][i + 1] if i + 1 < len(book["lessons"]) else None,
                chapter_url=url_for("science.chapter", slug=slug),
                textbook_index_endpoint="science.textbook_index",
                textbook_lesson_endpoint="science.textbook_lesson")
    abort(404)


@bp.get("/<slug>/practice")
def practice(slug):
    meta, _ch, book = _context(slug)
    lesson_id = request.args.get("lesson") or None
    collection = request.args.get("collection") or None
    if lesson_id and lesson_id not in {item["id"] for item in book["lessons"]}:
        abort(404)
    if collection and collection not in {"integrative", "current-affairs"}:
        abort(404)
    questions = science.approved_questions(slug, lesson_id, collection)
    try:
        i = max(1, int(request.args.get("i", 1)))
    except (TypeError, ValueError):
        i = 1
    question = questions[i - 1] if i <= len(questions) else None
    return render_template(
        "ds/science_practice.html", meta=meta, book=book, question=question,
        total=len(questions), i=i, lesson_id=lesson_id, collection=collection)

