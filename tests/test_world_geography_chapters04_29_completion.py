import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def load(path): return json.loads((ROOT / path).read_text(encoding="utf-8"))
def sha256(path): return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
def questions(payload): return payload if isinstance(payload, list) else payload.get("questions", [])

def test_canonical_sequence_covers_every_display_chapter_and_source_page():
    chapters = load("docs/world_geography_chapters_04_29_final_sequence.json")["chapters"]
    assert [row["n"] for row in chapters] == list(range(4, 30))
    assigned = [str(page) for row in chapters for page in row["pages"]]
    assert len(assigned) == len(set(assigned)) and assigned
    covered = set()
    for bank_path in (ROOT / "content/geography/original_practice").glob("[0-9][0-9].json"):
        for item in questions(json.loads(bank_path.read_text(encoding="utf-8"))):
            page = item.get("source_page")
            if page is None or str(page) not in assigned: continue
            if not str(item.get("manual_review_status", "")).startswith("manually-authored") or item.get("language") != "bilingual": continue
            assert item.get("question_te") and item.get("question_en")
            assert item.get("explanation_te") and item.get("explanation_en") and item.get("section")
            assert len(item.get("options_te", [])) == len(item.get("options_en", [])) == 4
            assert len(item.get("option_explanations_te", [])) == len(item.get("option_explanations_en", [])) == 4
            note_files = [p for p in (ROOT / "static/textbooks/geography/lessons").glob(f"{bank_path.stem}_*.html") if ".pre-" not in p.name]
            assert any(f'id="{item["section"]}"' in p.read_text(encoding="utf-8") for p in note_files), (bank_path.name, item["id"], item["section"], [p.name for p in note_files])
            covered.add(str(page))
    assert covered == set(assigned)

def test_all_chapter_manifests_are_hash_valid_and_not_deployed():
    root_manifest = load("content/geography/world_chapters/manifest.json")
    assert [row["display_chapter"] for row in root_manifest["chapters"] if row["display_chapter"] >= 4] == list(range(4, 30))
    assert root_manifest["deployment"] == "held"
    for number in range(4, 30):
        manifest = load(f"content/geography/world_chapters/{number}/manifest.json")
        assert manifest["display_chapter"] == number and manifest["railway_deployed"] is False
        assert "manual" in manifest["manual_review_status"]
        if "notes_file" in manifest:
            assert sha256(f"content/geography/world_chapters/{number}/Notes.html") == manifest["notes_sha256"]
            assert sha256(f"content/geography/world_chapters/{number}/Questions.json") == manifest["questions_sha256"]
        else:
            for filename, expected in manifest["notes_sha256"].items():
                path = ROOT / "static/textbooks/geography/lessons" / filename
                assert hashlib.sha256(path.read_bytes()).hexdigest() == expected
            for filename, expected in manifest["questions_sha256"].items():
                path = ROOT / "content/geography/original_practice" / filename
                assert hashlib.sha256(path.read_bytes()).hexdigest() == expected

def test_synthesis_chapters_have_complete_bilingual_mcqs_and_exact_links():
    for number in (27, 28, 29):
        manifest = load(f"content/geography/world_chapters/{number}/manifest.json")
        note = (ROOT / f"content/geography/world_chapters/{number}/Notes.html").read_text(encoding="utf-8")
        bank = questions(load(f"content/geography/world_chapters/{number}/Questions.json"))
        assert len(bank) == manifest["question_count"]
        for item in bank:
            assert item.get("question_te") and item.get("question_en")
            assert item.get("explanation_te") and item.get("explanation_en")
            assert len(item.get("options_te", [])) == len(item.get("options_en", [])) == 4
            assert len(item.get("option_explanations_te", [])) == len(item.get("option_explanations_en", [])) == 4
            assert f'id="{item["section"]}"' in note

def test_book_attributed_pyqs_preserve_provenance_and_unverified_items_are_unscored():
    intake = load("content/geography/book_pyq_intake.json")
    assert intake["record_count"] == len(intake["records"])
    for item in intake["records"]:
        assert item["question_type"].startswith("book_attributed_pyq")
        assert item["display_label"] and item["source"]["printed_page"]
        assert item["source"]["evidence_file"] and item["source"]["sha256"]
        if not item.get("official_final_key_evidence"):
            assert item["scorable"] is False and item["hold_reasons"]

def test_completion_ledger_matches_verified_state():
    ledger = load("docs/world_geography_chapters04_29_completion_audit.json")
    assert ledger["display_chapters"] == list(range(4, 30)) and ledger["chapter_count"] == 26
    assert ledger["all_assigned_pages_have_manual_bilingual_mcqs"] is True
    assert ledger["all_exact_section_links_validated"] is True
    assert ledger["printed_pyq_policy"]["unverified_items_scorable"] is False
    assert ledger["deployment"]["railway_deployed"] is False






