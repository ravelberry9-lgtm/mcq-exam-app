import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "content" / "textbooks" / "st3-ecosystem-biodiversity"
LESSON = "st3-l07-indian-law-protected-areas-institutions"


def nums(section, values):
    return [f"st3-l07-{section}-f{value:03d}" for value in values]


def span(section, start, stop):
    return nums(section, range(start, stop + 1))


metadata = {}
for filename in ("l7_visual_a.json", "l7_visual_b.json", "l7_visual_cd.json"):
    raw = json.loads((BOOK / "drafts" / filename).read_text(encoding="utf-8"))
    rows = raw if isinstance(raw, list) else raw["concepts"]
    for row in rows:
        key = (row.get("concept_id") or row.get("id")).lower()
        metadata[key] = {
            "title": row["title"],
            "concept_file": Path(row.get("concept_file") or row["concept"]).name,
            "full_file": Path(row.get("full_file") or row["full"]).name,
        }


groups = {
    "a01": nums("a", [2, 3, 4]),
    "a02": nums("a", [5, 6]),
    "a03": nums("a", [7]),
    "a04": nums("a", [8, 13]),
    "a05": nums("a", [10, 11, 12]),
    "a06": nums("a", [14, 15, 16, 17]),
    "a07": nums("a", [18]),
    "b01": nums("b", [1, 2, 103, 104]),
    "b02": nums("b", [3, 4, 5, 6, 33, 34, 35, 36, 37, 38, 80, 81, 82, 100, 117, 118, 119, 120]),
    "b03": nums("b", [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 101, 102]),
    "b04": span("b", 20, 32) + nums("b", [96, 97, 98, 99, 112, 113, 114, 115, 116]),
    "b05": nums("b", [39, 40, 41, 42, 48, 49, 50, 51, 52, 53, 54, 55, 56, 84, 85, 90, 91, 92, 105]),
    "b06": span("b", 43, 47) + nums("b", [86, 87, 106, 107, 108, 109, 110, 111]),
    "b07": span("b", 57, 65) + nums("b", [88, 89]),
    "b08": span("b", 66, 78) + nums("b", [93, 94, 95]),
    "c01": nums("c", [1]),
    "c02": nums("c", [2]),
    "c03": nums("c", [3]),
    "c04": nums("c", [4, 5, 6]) + ["st3-ca-2025-ramsar-cop15-f001"],
    "c05": nums("c", [7, 8, 9, 10]),
    "d01": nums("d", [1, 3, 4]),
    "d02": nums("d", [5, 6, 7, 8]),
    "d03": nums("d", [9, 10, 11]),
    "d04": nums("d", [12, 13, 17]),
    "d05": nums("d", [14, 15, 16]),
    "d06": nums("d", [18, 19, 20, 22, 23, 24, 25, 26, 27]),
}

if set(groups) != set(metadata):
    raise SystemExit(f"concept metadata mismatch: {set(groups) ^ set(metadata)}")

section_for = {prefix: f"l7-{prefix}" for prefix in "abcd"}
concepts = []
for concept_id, fact_ids in groups.items():
    concept = {"id": concept_id, "section_id": section_for[concept_id[0]], **metadata[concept_id], "fact_ids": fact_ids}
    concepts.append(concept)

fact_owner = {}
for concept in concepts:
    for fact_id in concept["fact_ids"]:
        if fact_id in fact_owner:
            raise SystemExit(f"fact mapped twice: {fact_id}")
        fact_owner[fact_id] = concept["id"]

all_facts = [
    json.loads(line) for line in (BOOK / "facts.jsonl").read_text(encoding="utf-8").splitlines()
    if line.strip()
]
lesson_fact_ids = {
    fact["fact_id"] for fact in all_facts
    if fact.get("lesson_id") == LESSON or fact["fact_id"] == "st3-ca-2025-ramsar-cop15-f001"
}
missing_facts = sorted(lesson_fact_ids - set(fact_owner))
if missing_facts:
    raise SystemExit(f"unmapped Lesson 7 facts: {missing_facts}")

questions = [
    json.loads(line) for line in (BOOK / "questions.jsonl").read_text(encoding="utf-8").splitlines()
    if line.strip()
]
lesson_questions = [row for row in questions if row.get("lesson_id") == LESSON]
overrides = {}
for question in lesson_questions:
    owners = [fact_owner[fact_id] for fact_id in question.get("fact_ids", []) if fact_id in fact_owner]
    if not owners:
        default = next(item["id"] for item in concepts if item["section_id"] == question["section_id"])
        overrides[question["id"]] = default
        continue
    counts = {owner: owners.count(owner) for owner in set(owners)}
    best = max(counts.values())
    winners = [owner for owner, count in counts.items() if count == best]
    if len(winners) > 1:
        overrides[question["id"]] = owners[0]

mapping = {
    "chapter_slug": "st3-ecosystem-biodiversity",
    "lesson_id": LESSON,
    "asset_directory": "concept-pairs",
    "concepts": concepts,
    "question_overrides": overrides,
}
target = BOOK / "concept_maps" / f"{LESSON}.json"
target.parent.mkdir(exist_ok=True)
target.write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({
    "concepts": len(concepts),
    "questions": len(lesson_questions),
    "overrides": len(overrides),
    "mapped_facts": len(fact_owner),
}, indent=2))
