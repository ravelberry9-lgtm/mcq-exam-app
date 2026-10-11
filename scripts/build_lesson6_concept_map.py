import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "content" / "textbooks" / "st3-ecosystem-biodiversity"
BLUEPRINT = BOOK / "drafts" / "l6_infographic_blueprint.json"
OUTPUT = BOOK / "concept_maps" / "st3-l06-global-frameworks-conventions.json"

SECTION_IDS = {
    "A": "st3-l06-global-biodiversity-governance-l6-a",
    "B": "st3-l06-global-biodiversity-governance-l6-b",
    "C": "st3-l06-global-biodiversity-governance-l6-c",
    "D": "st3-l06-global-biodiversity-governance-l6-d",
}

# One primary visual owner per fact. Cross-links remain in the lesson prose.
FACTS = {
    "l6-a-01": ["st3-l06-a-f022"],
    "l6-a-02": ["st3-l06-a-f002", "st3-l06-a-f003", "st3-l06-a-f004", "st3-l06-a-f023"],
    "l6-a-03": ["st3-l06-a-f005"],
    "l6-a-04": ["st3-l06-a-f006", "st3-l06-a-f007"],
    "l6-a-05": ["st3-l06-a-f008", "st3-l06-a-f010", "st3-l06-a-f025"],
    "l6-a-06": ["st3-l06-a-f009", "st3-l06-a-f024"],
    "l6-a-07": ["st3-l06-a-f011", "st3-l06-a-f028"],
    "l6-a-08": ["st3-l06-a-f012", "st3-l06-a-f013", "st3-l06-a-f014", "st3-l06-a-f026"],
    "l6-a-09": ["st3-l06-a-f015"],
    "l6-a-10": ["st3-l06-a-f016"],
    "l6-a-11": ["st3-l06-a-f017", "st3-l06-a-f018", "st3-l06-a-f019"],
    "l6-a-12": ["st3-l06-a-f020", "st3-l06-a-f027"],
    "l6-a-13": ["st3-l06-a-f021"],
    "l6-b-01": ["st3-l06-b-f001"],
    "l6-b-02": ["st3-l06-b-f002", "st3-l06-b-f003", "st3-l06-b-f012", "st3-l06-b-f013"],
    "l6-b-03": ["st3-l06-b-f006"],
    "l6-b-04": ["st3-l06-b-f014"],
    "l6-b-05": ["st3-l06-b-f004"],
    "l6-b-06": ["st3-l06-b-f015"],
    "l6-b-07": ["st3-l06-b-f007", "st3-l06-b-f009"],
    "l6-b-08": ["st3-ca-2026-cms-cop15-f001"],
    "l6-b-09": ["st3-l06-b-f016"],
    "l6-b-10": ["st3-l06-b-f010"],
    "l6-b-11": ["st3-l06-b-f011"],
    "l6-c-01": ["st3-l06-l6c-f001"],
    "l6-c-02": ["st3-l06-l6c-f003", "st3-l06-l6c-f004", "st3-l06-l6c-f006", "st3-l06-c-f010"],
    "l6-c-03": ["st3-l06-l6c-f005"],
    "l6-c-04": ["st3-l06-l6c-f002", "st3-l06-c-f012"],
    "l6-c-05": ["st3-l06-l6c-f008", "st3-l06-c-f011"],
    "l6-c-06": ["st3-l06-l6c-f009"],
    "l6-d-01": [],
    "l6-d-02": ["st3-l06-d-f008"],
    "l6-d-03": ["st3-l06-d-f009"],
    "l6-d-04": ["st3-l06-d-f001", "st3-l06-d-f002", "st3-l06-d-f003", "st3-ca-2026-bbnj-eif-f001"],
    "l6-d-05": ["st3-l06-d-f004", "st3-l06-d-f005", "st3-l06-d-f010"],
    "l6-d-06": ["st3-l06-d-f011"],
    "l6-d-07": ["st3-l06-d-f006", "st3-l06-d-f007"],
}


def main():
    blueprint = json.loads(BLUEPRINT.read_text(encoding="utf-8"))
    concepts = []
    for source in blueprint["concepts"]:
        concept_id = source["id"]
        concepts.append({
            "id": concept_id,
            "section_id": SECTION_IDS[source["section"]],
            "title": source["title"],
            "concept_file": source["concept"]["file"],
            "full_file": source["full"]["file"],
            "fact_ids": FACTS[concept_id],
        })
    payload = {
        "format": "science-concept-visual-map-v1",
        "chapter_slug": "st3-ecosystem-biodiversity",
        "lesson_id": "st3-l06-global-frameworks-conventions",
        "asset_directory": "concept-pairs",
        "concepts": concepts,
        "question_overrides": {
            "st3-ca-q002": "l6-d-04",
            "st3-ca-q004": "l6-d-04",
            "st3-ca-q005": "l6-b-08",
        },
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
