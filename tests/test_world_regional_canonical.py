import hashlib
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "content" / "geography" / "world_chapters"
SOURCE_BANK = ROOT / "content" / "geography" / "original_practice" / "27.json"
CASES = {
    20: ({str(x) for x in range(149, 157)}, 99),
    21: ({"158", "158b", "159", "160"}, 48),
    22: ({"161", "162", "163", "164"}, 54),
    23: ({"165", "166", "167"}, 38),
    24: ({"170", "171", "172", "173"}, 52),
    25: ({"174", "175", "176"}, 36),
    26: ({"168", "169"}, 28),
}


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_canonical_regional_index_is_complete_and_held():
    index = load_json(BASE / "manifest.json")
    assert index["deployment"] == "held"
    regional = [c for c in index["chapters"] if c["display_chapter"] in CASES]
    assert [c["display_chapter"] for c in regional] == list(CASES)
    assert sum(c["question_count"] for c in regional) == 355


def test_canonical_regional_content_preserves_source_and_links():
    source = load_json(SOURCE_BANK)["questions"]
    all_ids = []
    for number, (pages, count) in CASES.items():
        folder = BASE / str(number)
        manifest = load_json(folder / "manifest.json")
        payload = load_json(folder / "Questions.json")
        questions = payload["questions"]
        notes_path = folder / "Notes.html"
        notes = BeautifulSoup(notes_path.read_text(encoding="utf-8-sig"), "html.parser")
        notes_text = re.sub(r"\s+", " ", notes.get_text(" ", strip=True))
        expected = [q for q in source if q.get("source_page") in pages]
        assert len(questions) == len(expected) == count
        assert [(q["id"], q["answer"], q.get("kind")) for q in questions] == [
            (q["id"], q["answer"], q.get("kind")) for q in expected
        ]
        assert {q["source_page"] for q in questions} == pages
        assert manifest["source_pages"] == sorted(pages)
        assert manifest["routing_mode"] == "display-alias-preserve-legacy"
        assert manifest["original_ids_preserved"] and manifest["answer_keys_preserved"]
        assert not manifest["railway_deployed"]
        assert manifest["notes_sha256"] == hashlib.sha256(notes_path.read_bytes()).hexdigest()
        assert manifest["questions_sha256"] == hashlib.sha256((folder / "Questions.json").read_bytes()).hexdigest()
        for q in questions:
            assert q["question_te"] and q["question_en"]
            assert q["explanation_te"] and q["explanation_en"]
            assert len(q["options_te"]) == len(q["options_en"]) == 4
            assert len(q["option_explanations_te"]) == len(q["option_explanations_en"]) == 4
            assert q["difficulty"] in {"easy", "medium", "hard"}
            assert q["manual_review_status"] == "manually-authored-2026-10-27"
            assert notes.find(id=q["section"])
            assert re.sub(r"\s+", " ", q["source_paragraph"]).strip() in notes_text
            all_ids.append(q["id"])
    assert len(all_ids) == len(set(all_ids)) == 355


