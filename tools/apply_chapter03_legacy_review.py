import hashlib
import json
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "content" / "geography" / "india_ap_chapters" / "3"
PROGRESS = CHAPTER / "legacy_mcq_review_progress.json"
NOTES = CHAPTER / "Notes.html"
OUTPUT = CHAPTER / "Questions.json"
MANIFEST = CHAPTER / "manifest.json"
ENRICHMENT = CHAPTER / "manual_enrichment_questions.json"
INDEX = CHAPTER.parent / "manifest.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json_crlf(path: Path, value):
    text = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    path.write_bytes(text.replace("\n", "\r\n").encode("utf-8"))


def sha256(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


progress = load_json(PROGRESS)
reviewed_ids = progress["reviewed_ids"]
if len(reviewed_ids) != 120 or len(set(reviewed_ids)) != 120:
    raise SystemExit("Expected exactly 120 uniquely reviewed legacy questions")

fixes = progress["fixes"]
if set(fixes) != set(reviewed_ids):
    raise SystemExit("Every reviewed id must have exactly one recorded fix")

source_questions = {}
for lesson in (23, 24, 25, 26, 27):
    bank = load_json(ROOT / "content" / "geography" / "original_practice" / f"{lesson}.json")
    for question in bank["questions"]:
        if question["id"] in set(reviewed_ids):
            source_questions[question["id"]] = question

if set(source_questions) != set(reviewed_ids):
    missing = sorted(set(reviewed_ids) - set(source_questions))
    raise SystemExit(f"Reviewed source questions missing: {missing}")

notes_html = NOTES.read_text(encoding="utf-8-sig")
soup = BeautifulSoup(notes_html, "html.parser")
all_anchors = {tag.get("id") for tag in soup.find_all(attrs={"id": True})}


def exact_source_paragraph(anchor: str):
    node = soup.find(id=anchor)
    if node is None:
        raise SystemExit(f"Missing notes anchor: {anchor}")
    section = node if node.name == "section" else node.find_parent("section")
    if section is None:
        section = node.parent
    paragraph = section.find("p")
    target = paragraph if paragraph is not None else section
    return " ".join(target.get_text(" ", strip=True).split())


questions = []
for question_id in reviewed_ids:
    question = dict(source_questions[question_id])
    question.update(fixes[question_id])
    question["chapter"] = "IA-03"
    question["language"] = "bilingual"
    question["difficulty"] = question.get("difficulty", "medium")
    question.setdefault("fact_ids", [])
    question["manual_review_status"] = "manually-reviewed-preserved-legacy"
    question["reviewed_on"] = "2026-11-01"
    question.pop("options", None)
    question.pop("option_explanations", None)
    question.pop("excerpt", None)
    question.pop("heading", None)

    section = question["section"]
    related = question.get("related_sections", [])
    missing_anchors = [anchor for anchor in [section, *related] if anchor not in all_anchors]
    if missing_anchors:
        raise SystemExit(f"{question_id} has missing anchors: {missing_anchors}")
    question["source_paragraph"] = exact_source_paragraph(section)

    for field in ("options_en", "options_te", "option_explanations_en", "option_explanations_te"):
        if len(question.get(field, [])) != 4:
            raise SystemExit(f"{question_id}: {field} must contain four entries")
    if question["answer"] not in (1, 2, 3, 4):
        raise SystemExit(f"{question_id}: invalid answer")
    questions.append(question)

enrichment = load_json(ENRICHMENT)["questions"]
existing_ids = {question["id"] for question in questions}
for question in enrichment:
    if question["id"] in existing_ids:
        raise SystemExit(f"Duplicate enrichment id: {question['id']}")
    missing_anchors = [
        anchor for anchor in [question["section"], *question.get("related_sections", [])]
        if anchor not in all_anchors
    ]
    if missing_anchors:
        raise SystemExit(f"{question['id']} has missing anchors: {missing_anchors}")
    question = dict(question)
    question["source_paragraph"] = exact_source_paragraph(question["section"])
    for field in ("options_en", "options_te", "option_explanations_en", "option_explanations_te"):
        if len(question.get(field, [])) != 4:
            raise SystemExit(f"{question['id']}: {field} must contain four entries")
    questions.append(question)
    existing_ids.add(question["id"])

output = {
    "format": "india-ap-consolidated-questions-v1",
    "display_chapter": 3,
    "title": "Drainage Systems and Rivers",
    "release_ready": False,
    "questions": questions,
}
write_json_crlf(OUTPUT, output)

manifest = load_json(MANIFEST)
manifest["question_count"] = len(questions)
manifest["notes_sha256"] = sha256(NOTES)
manifest["questions_sha256"] = sha256(OUTPUT)
manifest["release_ready"] = False
manifest["railway_deployed"] = False
write_json_crlf(MANIFEST, manifest)

index = load_json(INDEX)
chapter_manifests = [
    load_json(CHAPTER.parent / str(display_chapter) / "manifest.json")
    for display_chapter in range(1, 21)
]
index["chapters"] = chapter_manifests
index["question_count"] = sum(item["question_count"] for item in chapter_manifests)
index["chapter_question_total"] = index["question_count"]
index["release_ready"] = False
index["railway_deployed"] = False
write_json_crlf(INDEX, index)

print(json.dumps({
    "question_count": len(questions),
    "notes_sha256": sha256(NOTES),
    "questions_sha256": sha256(OUTPUT),
}, indent=2))
