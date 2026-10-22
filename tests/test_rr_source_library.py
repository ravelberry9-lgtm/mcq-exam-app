import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LIBRARY = ROOT / "static" / "notes" / "AP_History" / "source_facsimiles" / "RR_Telugu"


def test_rr_library_has_every_verified_available_page():
    manifest = json.loads((LIBRARY / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["total_source_pdfs"] == 12
    assert manifest["total_scanned_pdf_pages"] == 191
    assert manifest["total_printed_pages"] == 372
    assert manifest["missing_printed_pages"] == [352]
    assert len(manifest["volumes"]) == 12

    pages = [page for volume in manifest["volumes"] for page in volume["printed_pages"]]
    assert len(pages) == 372
    assert all(page["text_status"] == "manually_verified" for page in pages)
    assert all((LIBRARY / page["scan"]).is_file() for page in pages)
    assert all((LIBRARY / page["text"]).is_file() for page in pages)
    assert len(list(LIBRARY.rglob("*.webp"))) == 372
    assert len(list(LIBRARY.rglob("*.txt"))) == 372


def test_rr_chapter_map_covers_app_15_through_41_without_fabricating_39():
    chapter_map = json.loads((LIBRARY / "chapter_map.json").read_text(encoding="utf-8"))
    assert set(chapter_map) == {str(number) for number in range(15, 42)}
    assert chapter_map["15"]["first_printed_page"] == 31
    assert chapter_map["38"]["last_printed_page"] == 351
    assert chapter_map["39"]["volume"] is None
    assert chapter_map["39"]["viewer"] is None
    assert chapter_map["40"]["first_printed_page"] == 353
    assert chapter_map["41"]["last_printed_page"] == 403


def test_each_printed_page_is_a_separate_viewer_card():
    manifest = json.loads((LIBRARY / "manifest.json").read_text(encoding="utf-8"))
    for volume in manifest["volumes"]:
        viewer = (LIBRARY / volume["key"] / "source_pages.html").read_text(encoding="utf-8")
        pages = volume["printed_pages"]
        assert viewer.count("<article id=\"page-") == len(pages)
        assert viewer.count("<div class=\"scan\"><img") == len(pages)
        assert viewer.count("<div class=\"text\"><pre>") == len(pages)
        for page in pages:
            number = page["printed_page"]
            assert f'id="page-{number:03d}"' in viewer


def test_telugu_index_exposes_scan_and_text_choices():
    index = (LIBRARY / "index.html").read_text(encoding="utf-8")
    assert "ముద్రిత పుటలు" in index
    assert "పాఠ్యం" in index
    assert "ముద్రిత పుట 352 లభించలేదు" in index
