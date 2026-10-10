from app.services import science_content
import json
import shutil
from pathlib import Path


SLUG = "st3-ecosystem-biodiversity"


def test_science_catalogue_and_chapter(client):
    hub = client.get("/learn/")
    assert hub.status_code == 200
    assert b'data-science-subject="science-technology"' in hub.data
    index = client.get("/learn/science-technology/")
    assert index.status_code == 200
    assert b"Ecosystems and Biodiversity" in index.data
    chapter = client.get(f"/learn/science-technology/{SLUG}/")
    assert chapter.status_code == 200
    assert b"1360 MCQs" in chapter.data


def test_science_textbook_navigation(client):
    index = client.get(f"/learn/science-technology/{SLUG}/textbook")
    assert index.status_code == 200
    assert b"st3-l01-ecology-foundations" in index.data
    lesson = client.get(f"/learn/science-technology/{SLUG}/textbook/st3-l01-ecology-foundations")
    assert lesson.status_code == 200
    assert b"biotic factors" in lesson.data
    assert b"st3-l02-population-community-succession" in lesson.data


def test_science_package_exposes_only_approved_questions(app):
    with app.app_context():
        book = science_content.load_book(SLUG)
        assert book and len(book["lessons"]) == 9
        summary = science_content.question_summary(SLUG)
        assert summary == {"total": 1360, "approved": 1360, "draft": 0}
        assert len(science_content.approved_questions(SLUG)) == 1360
        assert len(science_content.approved_questions(SLUG, collection="integrative")) == 70
        assert len(science_content.approved_questions(SLUG, collection="current-affairs")) == 10


def test_science_practice_uses_approved_sidecar(client):
    page = client.get(f"/learn/science-technology/{SLUG}/practice?i=1")
    assert page.status_code == 200
    assert b'data-science-question' in page.data
    assert b"1 / 1360" in page.data
    lesson = client.get(
        f"/learn/science-technology/{SLUG}/practice"
        "?lesson=st3-l01-ecology-foundations&i=156")
    assert lesson.status_code == 200
    assert b"156 / 156" in lesson.data
    integrated = client.get(
        f"/learn/science-technology/{SLUG}/practice?collection=integrative&i=1")
    assert integrated.status_code == 200 and b"1 / 70" in integrated.data
    current = client.get(
        f"/learn/science-technology/{SLUG}/practice?collection=current-affairs&i=1")
    assert current.status_code == 200 and b"1 / 10" in current.data
    assert client.get(
        f"/learn/science-technology/{SLUG}/practice?collection=unknown"
    ).status_code == 404
    assert client.get(
        f"/learn/science-technology/{SLUG}/practice?lesson=not-a-lesson"
    ).status_code == 404


def test_unknown_science_chapter_is_404(client):
    assert client.get("/learn/science-technology/not-a-chapter/").status_code == 404


def test_science_questions_fail_closed_on_unknown_lesson(app, tmp_path):
    source = Path(app.config["TEXTBOOK_ROOT"]) / SLUG
    target = tmp_path / SLUG
    shutil.copytree(source, target)
    qpath = target / "questions.jsonl"
    rows = qpath.read_text(encoding="utf-8").splitlines()
    first = json.loads(rows[0])
    first["lesson_id"] = "unknown-lesson"
    rows[0] = json.dumps(first, ensure_ascii=False, separators=(",", ":"))
    qpath.write_text("\n".join(rows) + "\n", encoding="utf-8")
    app.config["TEXTBOOK_ROOT"] = tmp_path
    with app.app_context():
        assert science_content.question_summary(SLUG) == {
            "total": 0, "approved": 0, "draft": 0}
        assert science_content.approved_questions(SLUG) == []


def test_science_hub_hides_missing_package(client, app, tmp_path):
    app.config["TEXTBOOK_ROOT"] = tmp_path
    page = client.get("/learn/")
    assert page.status_code == 200
    assert b'data-science-subject="science-technology"' not in page.data
