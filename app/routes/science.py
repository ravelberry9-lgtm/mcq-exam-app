"""Learner-facing Science & Technology textbook routes."""
from types import SimpleNamespace

from flask import Blueprint, abort, render_template, request, url_for

from ..services import science_content as science


bp = Blueprint("science", __name__, url_prefix="/learn/science-technology")


CHAPTER_VISUALS = {
    ("st3-ecosystem-biodiversity", "st3-l01-ecology-foundations"): [
        ("01-ecological-levels-bilingual.png", "Ecological levels", "పర్యావరణ స్థాయులు", "Concept visual"),
        ("02-limiting-factors-bilingual.png", "Limiting factors: Liebig and Shelford", "పరిమితి కారకాలు: లీబిగ్ మరియు షెల్ఫర్డ్", "Explanatory visual"),
        ("03-organism-responses-bilingual.png", "Responses to environmental change", "పర్యావరణ మార్పులకు ప్రతిస్పందనలు", "Concept visual"),
        ("04-acclimatisation-vs-adaptation-bilingual.png", "Acclimatisation and adaptation", "అలవాటు పడటం మరియు అనుకూలనం", "Explanatory visual"),
        ("05-habitat-vs-niche-bilingual.png", "Habitat and ecological niche", "ఆవాసం మరియు పర్యావరణ పాత్ర", "Explanatory visual"),
        ("06-major-abiotic-factors-bilingual.png", "Major abiotic factors", "ప్రధాన అజీవ కారకాలు", "Concept visual"),
        ("07-ecological-amplitude-bilingual.png", "Ecological amplitude", "పర్యావరణ సహన పరిధి", "Concept visual"),
        ("08-competition-coexistence-bilingual.png", "Competition and coexistence", "పోటీ మరియు సహజీవనం", "Explanatory visual"),
        ("09-ecosystem-feedback-bilingual.png", "Ecosystem feedback", "పర్యావరణ వ్యవస్థలో ప్రతిపుష్టి", "Explanatory visual"),
        ("10-chapter-1-rapid-revision-bilingual.png", "Chapter 1 rapid revision", "అధ్యాయం 1 త్వరిత పునశ్చరణ", "Revision visual"),
    ]
}

SECTION_VISUAL_PAIRS = {
    "st3-l01-ecology-foundations-section-1a": ("01-ecological-levels-bilingual.png", "10-chapter-1-rapid-revision-bilingual.png"),
    "st3-l01-ecology-foundations-section-1b": ("07-ecological-amplitude-bilingual.png", "02-limiting-factors-bilingual.png"),
    "st3-l01-ecology-foundations-section-1c": ("03-organism-responses-bilingual.png", "04-acclimatisation-vs-adaptation-bilingual.png"),
    "st3-l01-ecology-foundations-section-1d": ("10-chapter-1-rapid-revision-bilingual.png", "05-habitat-vs-niche-bilingual.png"),
    "st3-l01-ecology-foundations-section-1e": ("08-competition-coexistence-bilingual.png", "09-ecosystem-feedback-bilingual.png"),
    "st3-l01-ecology-foundations-section-must-compare": ("07-ecological-amplitude-bilingual.png", "04-acclimatisation-vs-adaptation-bilingual.png"),
    "st3-l01-ecology-foundations-section-quick-facts": ("06-major-abiotic-factors-bilingual.png", "10-chapter-1-rapid-revision-bilingual.png"),
    "st3-l01-ecology-foundations-section-exam-traps": ("07-ecological-amplitude-bilingual.png", "10-chapter-1-rapid-revision-bilingual.png"),
}


def _visuals(slug, lesson_id):
    base = f"infographics/science/{lesson_id}"
    return [
        {"url": url_for("static", filename=f"{base}/{filename}"),
         "title_en": title_en, "title_te": title_te, "kind": kind}
        for filename, title_en, title_te, kind
        in CHAPTER_VISUALS.get((slug, lesson_id), [])
    ]


def _question_visuals(slug, lesson_id, section_id):
    filenames = SECTION_VISUAL_PAIRS.get(section_id, ())
    base = f"infographics/science/{lesson_id}"
    labels = (("Concept image", "భావన చిత్రం"),
              ("Full explanation image", "పూర్తి వివరణ చిత్రం"))
    return [{"url": url_for("static", filename=f"{base}/{filename}"),
             "label_en": labels[i][0], "label_te": labels[i][1]}
            for i, filename in enumerate(filenames)]


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
                visual_infographics=_visuals(slug, lesson_id),
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


@bp.get("/<slug>/practice/explanation/<question_id>")
def practice_explanation(slug, question_id):
    meta, _ch, _book = _context(slug)
    question = science.approved_question(slug, question_id) or abort(404)
    lesson, section = science.section_for_question(slug, question)
    if not lesson or not section:
        abort(404)
    visuals = _question_visuals(slug, lesson["id"], section["id"])
    return render_template(
        "ds/science_explanation.html", meta=meta, question=question,
        lesson=lesson, section=section, visuals=visuals,
        back_url=request.args.get("back") or url_for("science.practice", slug=slug))

