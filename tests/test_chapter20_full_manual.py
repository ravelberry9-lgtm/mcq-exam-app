"""Full integrity checks for canonical World Geography Chapter 20."""

import hashlib
import json
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
CHAPTER_ROOT = ROOT / "content/geography/world_chapters/20"
BANK = CHAPTER_ROOT / "Questions.json"
NOTES = CHAPTER_ROOT / "Notes.html"
MANIFEST = CHAPTER_ROOT / "manifest.json"


def _payload():
    return json.loads(BANK.read_text(encoding="utf-8-sig"))


def test_chapter20_manual_bilingual_bank():
    rows = _payload()["questions"]
    assert len(rows) == 99
    for q in rows:
        assert q["language"] == "bilingual"
        assert q["difficulty"] in {"easy", "medium", "hard"}
        assert len(q["options_te"]) == len(q["options_en"]) == 4
        assert len(set(q["options_te"])) == len(set(q["options_en"])) == 4
        assert len(q["option_explanations_te"]) == len(q["option_explanations_en"]) == 4
        assert len(set(q["option_explanations_te"])) == 4
        assert len(set(q["option_explanations_en"])) == 4
        assert q["explanation_te"] == q["option_explanations_te"][q["answer"] - 1]
        assert q["explanation_en"] == q["option_explanations_en"][q["answer"] - 1]


def test_chapter20_links_and_hashes():
    payload = _payload()
    rows = payload["questions"]
    soup = BeautifulSoup(NOTES.read_text(encoding="utf-8"), "html.parser")
    assert [(q["id"], q["section"]) for q in rows if not soup.find(id=q["section"])] == []
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8-sig"))
    assert manifest["question_count"] == len(rows) == 99
    assert manifest["notes_sha256"] == hashlib.sha256(NOTES.read_bytes()).hexdigest()
    assert manifest["questions_sha256"] == hashlib.sha256(BANK.read_bytes()).hexdigest()
    assert manifest["railway_deployed"] is False


def test_chapter20_canonical_routes(client):
    assert client.get("/learn/geography/world/20").status_code == 200
    assert client.get("/learn/geography/world/20/notes").status_code == 200
    assert client.get("/learn/geography/world/20/practice").status_code == 200
    sample = _payload()["questions"][0]
    for lang in ("te", "en"):
        response = client.get(
            f'/learn/geography/world/20/practice/{sample["id"]}',
            query_string={"qlang": lang},
        )
        assert response.status_code == 200
        assert sample[f"question_{lang}"] in BeautifulSoup(
            response.get_data(as_text=True), "html.parser"
        ).get_text(" ", strip=True)
    response = client.post(
        f'/learn/geography/world/20/practice/{sample["id"]}/answer?qlang=en',
        data={"choice": str(sample["answer"])},
    )
    assert response.status_code == 200 and b"answer-result" in response.data
