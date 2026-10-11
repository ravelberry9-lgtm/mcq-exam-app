"""Read-only Science & Technology textbook catalogue and sidecar metadata."""
import json
from pathlib import Path

from flask import current_app

from . import textbook


CHAPTERS = (
    {
        "slug": "st3-ecosystem-biodiversity",
        "title_en": "Ecosystems and Biodiversity",
        "title_te": "పర్యావరణ వ్యవస్థలు మరియు జీవ వైవిధ్యం",
        "part_en": "Science & Technology · Environment",
        "part_te": "సైన్స్ & టెక్నాలజీ · పర్యావరణం",
    },
)


def _root() -> Path:
    return Path(current_app.config["TEXTBOOK_ROOT"]).resolve()


def chapter(slug: str):
    return next((item for item in CHAPTERS if item["slug"] == slug), None)


def load_book(slug: str):
    """Load an approved Science package without changing AP History's feature flag."""
    meta = chapter(slug)
    if not meta:
        return None
    root = _root()
    path = (root / slug / "manifest.json").resolve()
    if not path.is_relative_to(root) or not path.is_file():
        return None
    try:
        data = textbook.validate(json.loads(path.read_text(encoding="utf-8")), slug)
    except (ValueError, TypeError, KeyError, OSError):
        current_app.logger.warning("Science textbook package rejected for %s", slug)
        return None
    return data if data["status"] == "approved" else None


def question_summary(slug: str):
    """Count a structurally and referentially valid question sidecar."""
    rows = _validated_questions(slug)
    if rows is None:
        return {"total": 0, "approved": 0, "draft": 0}
    total = len(rows)
    approved = sum(row["review_status"] == "bilingual_approved" for row in rows)
    return {"total": total, "approved": approved, "draft": total - approved}


def approved_questions(slug: str, lesson_id: str | None = None,
                       collection: str | None = None):
    """Load only individually bilingual-approved sidecar questions."""
    rows = _validated_questions(slug)
    if rows is None:
        return []
    return [row for row in rows if row["review_status"] == "bilingual_approved"
            and (not lesson_id or row["lesson_id"] == lesson_id)
            and (not collection or row.get("collection") == collection)]


def approved_question(slug: str, question_id: str):
    """Return one approved question without exposing draft sidecar rows."""
    return next((row for row in approved_questions(slug)
                 if row["id"] == question_id), None)


def load_concept_map(slug: str):
    """Load the optional, reviewed MCQ-to-infographic concept catalogue."""
    root = _root()
    package = (root / slug).resolve()
    path = (package / "concept_map.json").resolve()
    if not path.is_relative_to(package) or not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        concepts = data.get("concepts")
        overrides = data.get("question_overrides")
        if data.get("chapter_slug") != slug or not isinstance(concepts, list) or \
                not isinstance(overrides, dict):
            raise ValueError("invalid concept map header")
        ids = set()
        filenames = set()
        required = ("id", "section_id", "title", "concept_file", "full_file")
        for concept in concepts:
            if not isinstance(concept, dict) or any(
                    not isinstance(concept.get(key), str) or not concept[key].strip()
                    for key in required):
                raise ValueError("invalid concept")
            if concept["id"] in ids:
                raise ValueError("duplicate concept id")
            ids.add(concept["id"])
            files = (concept["concept_file"], concept["full_file"])
            if any(Path(filename).name != filename or not filename.endswith(".png")
                   for filename in files) or any(filename in filenames for filename in files):
                raise ValueError("unsafe or duplicate concept filename")
            filenames.update(files)
            fact_ids = concept.get("fact_ids")
            if not isinstance(fact_ids, list) or any(
                    not isinstance(fact_id, str) or not fact_id.strip()
                    for fact_id in fact_ids):
                raise ValueError("invalid concept facts")
        if any(not isinstance(question_id, str) or
               (concept_id is not None and concept_id not in ids)
               for question_id, concept_id in overrides.items()):
            raise ValueError("invalid question override")
        return data
    except (ValueError, TypeError, OSError, json.JSONDecodeError):
        current_app.logger.warning("Science concept map rejected for %s", slug)
        return None


def concept_for_question(slug: str, question: dict):
    """Resolve one MCQ to its narrowest reviewed visual concept.

    Explicit overrides are authoritative for synthesis/review questions.  A null
    override intentionally suppresses concept-level imagery when the question's
    main teaching concept belongs to another lesson.  Ordinary questions are
    resolved by their audited fact IDs.
    """
    mapping = load_concept_map(slug)
    if not mapping or question.get("lesson_id") != mapping.get("lesson_id"):
        return None
    question_id = question.get("id")
    overrides = mapping["question_overrides"]
    if question_id in overrides:
        concept_id = overrides[question_id]
        if concept_id is None:
            return None
        return next((item for item in mapping["concepts"]
                     if item["id"] == concept_id), None)

    fact_ids = set(question.get("fact_ids", ()))
    ranked = []
    for index, concept in enumerate(mapping["concepts"]):
        overlap = len(fact_ids.intersection(concept["fact_ids"]))
        if overlap:
            ranked.append((overlap, -index, concept))
    if not ranked:
        return None
    ranked.sort(reverse=True, key=lambda item: (item[0], item[1]))
    if len(ranked) > 1 and ranked[0][0] == ranked[1][0]:
        return None
    return ranked[0][2]


def section_for_question(slug: str, question: dict):
    """Resolve an MCQ to its reviewed textbook section mapping."""
    book = load_book(slug)
    if not book:
        return None, None
    lesson = next((item for item in book["lessons"]
                   if item["id"] == question["lesson_id"]), None)
    if not lesson:
        return None, None
    section_ids = {item["id"] for item in lesson["sections"]}
    section_id = question.get("section_id")
    if section_id not in section_ids:
        path = (_root() / slug / "section_map.json").resolve()
        if not path.is_relative_to(_root() / slug) or not path.is_file():
            return lesson, None
        try:
            mapping = json.loads(path.read_text(encoding="utf-8"))
            section_id = next((sid for sid, value in mapping.items()
                               if sid in section_ids and
                               question["id"] in value.get("mcq_ids", [])), None)
            if not section_id:
                fact_ids = set(question.get("fact_ids", []))
                section_id = next((sid for sid, value in mapping.items()
                                   if sid in section_ids and fact_ids.intersection(
                                       value.get("fact_ids", []))), None)
        except (ValueError, TypeError, OSError, json.JSONDecodeError):
            section_id = None
    return lesson, next((item for item in lesson["sections"]
                         if item["id"] == section_id), None)


def _validated_questions(slug: str):
    """Validate the complete sidecar atomically; any defect hides the whole bank."""
    book = load_book(slug)
    if not book:
        return None
    root = _root()
    package = (root / slug).resolve()
    qpath, fpath = package / "questions.jsonl", package / "facts.jsonl"
    if not package.is_relative_to(root) or not qpath.is_file() or not fpath.is_file():
        return None
    try:
        facts = set()
        for line in fpath.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            fact = json.loads(line)
            if isinstance(fact.get("fact_id"), str):
                facts.add(fact["fact_id"])
            facts.update(x for x in fact.get("fact_ids", []) if isinstance(x, str))
        lessons = {item["id"] for item in book["lessons"]}
        rows, ids = [], set()
        required_text = ("id", "lesson_id", "question_en", "question_te",
                         "explanation_en", "explanation_te", "difficulty", "qtype")
        for line in qpath.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if not isinstance(row, dict) or any(
                    not isinstance(row.get(key), str) or not row[key].strip()
                    for key in required_text):
                raise ValueError("missing question field")
            if row["id"] in ids or row["lesson_id"] not in lessons:
                raise ValueError("duplicate id or unknown lesson")
            ids.add(row["id"])
            if set(row.get("options_en", {})) != {"a", "b", "c", "d"} or \
                    set(row.get("options_te", {})) != {"a", "b", "c", "d"}:
                raise ValueError("invalid option map")
            if any(not isinstance(value, str) or not value.strip()
                   for options in (row["options_en"], row["options_te"])
                   for value in options.values()):
                raise ValueError("empty option")
            if row.get("correct_answer") not in {"a", "b", "c", "d"}:
                raise ValueError("invalid answer")
            fact_ids = row.get("fact_ids")
            if not isinstance(fact_ids, list) or not fact_ids or any(
                    not isinstance(fid, str) or fid not in facts for fid in fact_ids):
                raise ValueError("unknown fact")
            if row.get("review_status") not in {"bilingual_approved", "content-reviewed",
                                                 "content_review_required", "semantic-qa-reviewed"}:
                raise ValueError("invalid review status")
            rows.append(row)
        return rows
    except (ValueError, TypeError, KeyError, OSError, json.JSONDecodeError):
        current_app.logger.warning("Science question sidecar rejected for %s", slug)
        return None

