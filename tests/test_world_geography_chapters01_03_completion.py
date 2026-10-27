import hashlib
import json
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]

def load(rel): return json.loads((ROOT / rel).read_text(encoding="utf-8"))
def digest(rel): return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()

def bilingual_map(number):
    if number == 1: return load("content/geography/chapter01_bilingual.json")["questions"]
    if number == 2: return load("content/geography/chapter02_bilingual.json")["questions"]
    return load("content/geography/solar_bilingual.json")["original"]

def test_chapters_01_03_are_in_the_canonical_world_index():
    index = load("content/geography/world_chapters/manifest.json")
    assert index["display_range"] == "01-29"
    assert [row["display_chapter"] for row in index["chapters"]] == list(range(1, 30))
    assert index["deployment"] == "held"

def test_chapter_manifests_hashes_counts_and_deployment_hold():
    expected = {1: 198, 2: 242, 3: 531}
    for number, count in expected.items():
        m = load(f"content/geography/world_chapters/{number}/manifest.json")
        assert m["display_chapter"] == number and m["question_count"] == count
        assert m["railway_deployed"] is False and "manually-reviewed" in m["manual_review_status"]
        for rel in m["notes_files"]: assert digest(rel) == m["notes_sha256"][Path(rel).name]
        for rel in m["question_banks"]: assert digest(rel) == m["questions_sha256"][Path(rel).name]
        rel = m["bilingual_question_bank"]
        assert digest(rel) == m["questions_sha256"][Path(rel).name]

def test_all_971_bilingual_questions_are_complete_and_exactly_linked():
    expected = {1: 198, 2: 242, 3: 531}
    total = 0
    for number, count in expected.items():
        m = load(f"content/geography/world_chapters/{number}/manifest.json")
        note = BeautifulSoup((ROOT / m["notes_files"][0]).read_text(encoding="utf-8"), "html.parser")
        bank = bilingual_map(number)
        assert len(bank) == count
        for qid, item in bank.items():
            assert item["answer"] in (1, 2, 3, 4)
            assert note.find(id=item["section"]) is not None, (qid, item["section"])
            for lang in ("te", "en"):
                variant = item["variants"][lang]
                assert variant["question"] and variant["explanation"]
                assert len(variant["options"]) == 4
                assert len(variant["option_explanations"]) == 4
        total += len(bank)
    assert total == 971

def test_every_printed_page_2_24_has_bilingual_mapped_questions():
    expected_pages = {str(n) for n in range(2, 25)}
    covered = set()
    for number in (1, 2, 3):
        original = load(f"content/geography/original_practice/{number:02}.json")["questions"]
        bilingual = bilingual_map(number)
        for item in original:
            page = item.get("source_page")
            if page is None: continue
            assert item["id"] in bilingual
            covered.add(str(page))
    assert covered == expected_pages

def test_printed_pyqs_on_foundation_pages_remain_unscored_without_official_keys():
    records = load("content/geography/book_pyq_intake.json")["records"]
    foundation = [r for r in records if str(r["source"]["printed_page"]) in {"9", "17"}]
    assert {r["source"]["printed_page"] for r in foundation} == {9, 17}
    for item in foundation:
        assert item["scorable"] is False
        assert not item.get("official_final_key_evidence")
        assert item["hold_reasons"] and item["display_label"]

def test_chapters_01_03_completion_ledger():
    ledger = load("docs/world_geography_chapters01_03_completion_audit.json")
    assert ledger["chapter_count"] == 3 and ledger["bilingual_question_count"] == 971
    assert ledger["source_pages"] == [str(n) for n in range(2, 25)]
    assert ledger["all_bilingual_questions_exactly_linked"] is True
    assert ledger["deployment"]["railway_deployed"] is False
