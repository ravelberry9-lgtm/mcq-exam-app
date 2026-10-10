from app.services import science_content
import json
import shutil
from pathlib import Path


SLUG = "st3-ecosystem-biodiversity"


def test_science_catalogue_and_chapter(client):
    hub = client.get("/learn/")
    assert hub.status_code == 200
    assert b'data-science-subject="science-technology"' in hub.data
    assert b'data-subject="science_technology"' not in hub.data
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
    assert b'integrated-bilingual' in lesson.data
    assert b'<details class="textbook-section card"' in lesson.data
    assert b'id="reading-mode"' in lesson.data
    assert b'id="study-level"' not in lesson.data
    assert b'class="textbook-copy en"' in lesson.data
    assert b'class="langsw"' not in lesson.data
    assert b'class="bottomnav"' not in lesson.data
    assert b"biotic factors" in lesson.data
    assert b'textbook-visual-gallery' in lesson.data
    assert b'01-ecological-levels-bilingual.png' in lesson.data
    assert b'10-chapter-1-rapid-revision-bilingual.png' in lesson.data
    assert b'loading="lazy"' in lesson.data
    assert b"st3-l02-population-community-succession" in lesson.data


def test_science_visual_pilot_does_not_replace_other_lessons(client):
    lesson = client.get(
        f"/learn/science-technology/{SLUG}/textbook/"
        "st3-l02-population-community-succession")
    assert lesson.status_code == 200
    assert b'textbook-visual-gallery' not in lesson.data
    assert b'01-ecological-levels-bilingual.png' not in lesson.data


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
    assert b'<details class="card science-explanation"' in page.data
    assert b'Open content and infography' in page.data
    assert b'Show explanation' in page.data
    assert b'class="langsw"' not in page.data
    assert b'class="bottomnav"' not in page.data
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


def test_science_question_explanation_links_section_and_visual_pair(client):
    page = client.get(
        f"/learn/science-technology/{SLUG}/practice/explanation/"
        "st3-l01-01c-q001")
    assert page.status_code == 200
    assert b'id="content-tab"' in page.data
    assert b'id="infography-tab"' in page.data
    assert b'data-slide="1"' in page.data
    assert b'data-slide="2"' in page.data
    assert b'id="exit-infography"' in page.data
    assert b'id="visual-next"' not in page.data
    assert b'id="visual-position"' not in page.data
    assert b'swipe-hint' not in page.data
    assert b'<figcaption>' not in page.data
    assert b'infography-reading' in page.data
    assert b'<header class="card">' not in page.data
    assert b'How Organisms Respond to Environmental Variation' in page.data
    assert b'03-organism-responses-bilingual.png' in page.data
    assert b'13-section-1c-full-explanation-bilingual.png' in page.data
    assert page.data.count(b'<figure data-slide=') == 2


def test_science_question_explanation_rejects_unknown_question(client):
    assert client.get(
        f"/learn/science-technology/{SLUG}/practice/explanation/not-a-question"
    ).status_code == 404


def test_every_lesson_one_mcq_resolves_to_section_and_two_visuals(app):
    from app.routes.science import SECTION_VISUAL_PAIRS

    with app.test_request_context():
        questions = science_content.approved_questions(
            SLUG, lesson_id="st3-l01-ecology-foundations")
        assert len(questions) == 156
        for question in questions:
            lesson, section = science_content.section_for_question(SLUG, question)
            assert lesson is not None, question["id"]
            assert section is not None, question["id"]
            assert len(SECTION_VISUAL_PAIRS.get(section["id"], ())) == 2, question["id"]


def test_all_lesson_one_visual_pair_files_exist(app):
    from app.routes.science import SECTION_VISUAL_PAIRS

    root = Path(app.static_folder) / "infographics" / "science" / \
        "st3-l01-ecology-foundations"
    for pair in SECTION_VISUAL_PAIRS.values():
        assert len(pair) == 2
        assert all((root / filename).is_file() for filename in pair)


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


def test_design_system_pages_are_installable(client):
    page = client.get("/learn/")
    assert b'rel="manifest"' in page.data
    assert b'id="pwa-install"' in page.data
    worker = client.get("/sw.js")
    assert worker.status_code == 200
    assert worker.headers["Service-Worker-Allowed"] == "/"
    manifest = client.get("/static/manifest.json").get_json()
    assert manifest["start_url"] == "/learn/"
    assert manifest["scope"] == "/"
