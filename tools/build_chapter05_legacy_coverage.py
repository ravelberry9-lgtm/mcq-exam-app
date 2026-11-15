import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "content" / "geography" / "india_ap_chapters" / "5"

# This mapping records only direct coverage in the preserved legacy bank. It is
# deliberately conservative: a vaguely related question is not counted.
ANCHOR_QUESTIONS = {
    "texture-structure": ["GEO-ORIG-30-005", "GEO-ORIG-30-006", "GEO-ORIG-30-007", "GEO-ORIG-30-008", "GEO-ORIG-30-014", "GEO-ORIG-30-018", "GEO-ORIG-30-019"],
    "loam-texture": ["GEO-ORIG-30-007", "GEO-ORIG-30-014"],
    "soil-water-air": ["GEO-ORIG-30-010", "GEO-ORIG-30-020", "GEO-ORIG-31-009", "GEO-ORIG-31-015", "GEO-ORIG-31-020"],
    "humus-organic-matter": ["GEO-ORIG-30-012", "GEO-ORIG-30-015", "GEO-ORIG-30-021"],
    "red-yellow-properties": ["GEO-ORIG-30-002", "GEO-ORIG-30-013", "GEO-ORIG-30-016"],
    "black-properties": ["GEO-ORIG-30-003", "GEO-ORIG-30-013", "GEO-ORIG-30-017", "GEO-ORIG-30-024"],
    "laterite-properties": ["GEO-ORIG-30-004", "GEO-ORIG-30-013", "GEO-ORIG-30-017"],
    "ap-red-soils": ["GEO-ORIG-30-002", "GEO-ORIG-30-016"],
    "ap-black-soils": ["GEO-ORIG-30-003", "GEO-ORIG-30-017", "GEO-ORIG-30-024"],
    "ap-alluvial-soils": ["GEO-ORIG-30-001", "GEO-ORIG-30-016", "GEO-ORIG-30-023"],
    "ap-lateritic-soils": ["GEO-ORIG-30-004", "GEO-ORIG-30-017"],
    "ap-coastal-soils": ["GEO-ORIG-30-009", "GEO-ORIG-30-022", "GEO-ORIG-30-023"],
    "saline-sodic": ["GEO-ORIG-30-009", "GEO-ORIG-30-015", "GEO-ORIG-30-020", "GEO-ORIG-30-022", "GEO-ORIG-31-010", "GEO-ORIG-31-015", "GEO-ORIG-31-020", "GEO-ORIG-31-023"],
    "erosion-process": ["GEO-ORIG-30-011", "GEO-ORIG-30-015", "GEO-ORIG-30-021"],
    "water-erosion-types": ["GEO-ORIG-31-001", "GEO-ORIG-31-002", "GEO-ORIG-31-003", "GEO-ORIG-31-013", "GEO-ORIG-31-016", "GEO-ORIG-31-017"],
    "bank-coastal-erosion": ["GEO-ORIG-31-004", "GEO-ORIG-31-013", "GEO-ORIG-31-017"],
    "conservation-practices": ["GEO-ORIG-31-005", "GEO-ORIG-31-006", "GEO-ORIG-31-007", "GEO-ORIG-31-008", "GEO-ORIG-31-014", "GEO-ORIG-31-018", "GEO-ORIG-31-019", "GEO-ORIG-31-022"],
    "conservation-diagram": ["GEO-ORIG-31-005", "GEO-ORIG-31-006", "GEO-ORIG-31-007", "GEO-ORIG-31-008", "GEO-ORIG-31-014"],
}


def main() -> None:
    ledger = json.loads((CHAPTER / "page_fact_ledger.json").read_text(encoding="utf-8"))
    bank = json.loads((CHAPTER / "Questions.json").read_text(encoding="utf-8"))["questions"]
    direct_fact_questions = {}
    for question in bank:
        for fact_id in question.get("fact_ids", []):
            direct_fact_questions.setdefault(fact_id, []).append(question["id"])
    rows = []
    for page in ledger["pages"]:
        for fact in page["facts"]:
            questions = list(dict.fromkeys(
                ANCHOR_QUESTIONS.get(fact["anchor"], []) + direct_fact_questions.get(fact["id"], [])
            ))
            rows.append({
                "fact_id": fact["id"],
                "page": page["page"],
                "anchor": fact["anchor"],
                "question_ids": questions,
                "status": "covered_by_legacy_bank" if questions else "new_manual_mcq_required",
            })
    result = {
        "format": "india-ap-fact-question-coverage-v1",
        "chapter": 5,
        "rule": "Only a question that directly tests the printed fact counts as coverage.",
        "total_facts": len(rows),
        "covered_facts": sum(bool(row["question_ids"]) for row in rows),
        "open_facts": sum(not row["question_ids"] for row in rows),
        "facts": rows,
    }
    (CHAPTER / "fact_question_coverage.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline=""
    )


if __name__ == "__main__":
    main()
