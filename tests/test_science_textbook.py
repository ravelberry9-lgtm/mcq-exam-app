from collections import Counter
import json
import shutil
import struct
from pathlib import Path

from app.services import science_content


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
    assert b"1297 MCQs" in chapter.data


def test_science_textbook_navigation(client):
    index = client.get(f"/learn/science-technology/{SLUG}/textbook")
    assert index.status_code == 200
    assert b"st3-l01-ecology-foundations" in index.data
    lesson = client.get(f"/learn/science-technology/{SLUG}/textbook/st3-l01-ecology-foundations")
    assert lesson.status_code == 200
    assert b'integrated-bilingual' in lesson.data
    assert b'<section class="editorial-section"' in lesson.data
    assert b'id="reading-mode"' in lesson.data
    assert b'id="study-level"' not in lesson.data
    assert b'data-editorial-html="true"' in lesson.data
    assert b'class="editorial-lesson"' in lesson.data
    assert b'class="textbook-copy en"' not in lesson.data
    assert b'class="langsw"' not in lesson.data
    assert b'class="bottomnav"' not in lesson.data
    assert b"biotic factors" in lesson.data
    assert b'textbook-visual-gallery' in lesson.data
    assert b'01-ecological-levels-bilingual.png' in lesson.data
    assert b'10-chapter-1-rapid-revision-bilingual.png' in lesson.data
    assert b'loading="lazy"' in lesson.data
    assert b"st3-l02-population-community-succession" in lesson.data


def test_lesson_five_uses_editorial_html_pilot(client):
    page = client.get(
        f"/learn/science-technology/{SLUG}/textbook/"
        "st3-l05-biodiversity-loss-conservation")
    assert page.status_code == 200
    assert b'data-editorial-html="true"' in page.data
    assert b'class="editorial-lesson"' in page.data
    assert b"Species richness" in page.data
    assert b"textbook-copy en" not in page.data
    for section_id in (
        "st3-l05-biodiversity-l5-a", "st3-l05-biodiversity-l5-b",
        "st3-l05-biodiversity-l5-c", "st3-l05-biodiversity-l5-d",
    ):
        assert f'id="{section_id}"'.encode() in page.data


def test_lessons_one_to_four_use_colorful_editorial_html(client):
    expected = {
        "st3-l01-ecology-foundations": 8,
        "st3-l02-population-community-succession": 10,
        "st3-l03-ecosystem-structure-energy-cycles": 9,
        "st3-l04-ecosystem-types-indian-biogeography": 3,
    }
    for lesson_id, section_count in expected.items():
        page = client.get(
            f"/learn/science-technology/{SLUG}/textbook/{lesson_id}")
        assert page.status_code == 200
        assert b'data-editorial-html="true"' in page.data
        assert b'class="chapter-map"' in page.data
        assert page.data.count(b'class="editorial-section"') == section_count
        assert page.data.count(b'class="concept-ribbon"') == section_count
        assert b'class="textbook-copy en"' not in page.data


def test_lesson_six_editorial_html_and_question_mappings(client, app):
    lesson_id = "st3-l06-global-frameworks-conventions"
    page = client.get(
        f"/learn/science-technology/{SLUG}/textbook/{lesson_id}")
    assert page.status_code == 200
    assert b'data-editorial-html="true"' in page.data
    assert b"Global Biodiversity Governance" in page.data
    assert page.data.count(b'class="editorial-section"') == 4
    with app.app_context():
        questions = science_content.approved_questions(SLUG, lesson_id)
    assert len(questions) == 144
    assert all(question.get("section_id") for question in questions)
    assert all(question["section_id"].startswith(
        "st3-l06-global-biodiversity-governance-l6-")
        for question in questions)


def test_lesson_seven_editorial_html_and_question_mappings(client, app):
    lesson_id = "st3-l07-indian-law-protected-areas-institutions"
    page = client.get(
        f"/learn/science-technology/{SLUG}/textbook/{lesson_id}")
    assert page.status_code == 200
    assert b'data-editorial-html="true"' in page.data
    assert b"Indian Conservation Law and Institutions" in page.data
    assert page.data.count(b'class="editorial-section"') == 4
    with app.app_context():
        questions = science_content.approved_questions(SLUG, lesson_id)
    assert len(questions) == 151
    assert all(question.get("section_id") in {"l7-a", "l7-b", "l7-c", "l7-d"}
               for question in questions)


def test_lesson_seven_concept_map_covers_every_question_and_asset(app, client):
    lesson_id = "st3-l07-indian-law-protected-areas-institutions"
    with app.app_context():
        mapping = science_content.load_concept_map(SLUG, lesson_id)
        questions = science_content.approved_questions(SLUG, lesson_id)
        assert mapping is not None
        assert len(mapping["concepts"]) == 26
        assert len(questions) == 151
        assert all(science_content.concept_for_question(SLUG, question)
                   for question in questions)
    root = Path(app.static_folder) / "infographics" / "science" / lesson_id / "concept-pairs"
    for concept in mapping["concepts"]:
        assert (root / concept["concept_file"]).is_file()
        assert (root / concept["full_file"]).is_file()
    explanation = client.get(
        f"/learn/science-technology/{SLUG}/practice/explanation/st3-l07-a-q001")
    assert explanation.status_code == 200
    assert explanation.data.count(b"<figure data-slide=") == 2
    assert b"a01-wpa-framework-amendment-concept.png" in explanation.data
    assert b"a01-wpa-framework-amendment-full.png" in explanation.data


def test_lesson_eight_editorial_html_and_question_mappings(client, app):
    lesson_id = "st3-l08-wildlife-conservation-monitoring"
    page = client.get(
        f"/learn/science-technology/{SLUG}/textbook/{lesson_id}")
    assert page.status_code == 200
    assert b'data-editorial-html="true"' in page.data
    assert b"Wildlife Conservation, Recovery and Monitoring" in page.data
    assert page.data.count(b'class="editorial-section"') == 4
    for section_id in ("l8-a", "l8-b", "l8-c", "l8-d"):
        assert (
            f'id="st3-l08-wildlife-conservation-monitoring-{section_id}"'
            .encode() in page.data
        )
    with app.app_context():
        questions = science_content.approved_questions(SLUG, lesson_id)
    assert len(questions) == 210


def test_lesson_eight_concept_map_covers_every_question_and_asset(app, client):
    lesson_id = "st3-l08-wildlife-conservation-monitoring"
    with app.app_context():
        mapping = science_content.load_concept_map(SLUG, lesson_id)
        questions = science_content.approved_questions(SLUG, lesson_id)

    assert mapping is not None
    assert len(mapping["concepts"]) == 31
    assert len({concept["id"] for concept in mapping["concepts"]}) == 31
    assert len(questions) == 210
    assert all(
        science_content.concept_for_question(SLUG, question)
        for question in questions
    )

    root = (
        Path(app.static_folder) / "infographics" / "science" / lesson_id
        / mapping["asset_directory"]
    )
    referenced = {
        filename
        for concept in mapping["concepts"]
        for filename in (concept["concept_file"], concept["full_file"])
    }
    assert len(referenced) == 62
    for filename in referenced:
        path = root / filename
        assert path.is_file()
        with path.open("rb") as image_file:
            assert image_file.read(8) == b"\x89PNG\r\n\x1a\n"
            chunk_length = struct.unpack(">I", image_file.read(4))[0]
            assert image_file.read(4) == b"IHDR"
            assert chunk_length == 13
            width, height = struct.unpack(">II", image_file.read(8))
        assert (width, height) == (1024, 1536)

    explanation = client.get(
        f"/learn/science-technology/{SLUG}/practice/explanation/"
        "st3-l08-a-q001")
    assert explanation.status_code == 200
    assert explanation.data.count(b"<figure data-slide=") == 2
    assert b"a01-iucn-status-ladder-concept.png" in explanation.data
    assert b"a01-iucn-status-ladder-full.png" in explanation.data


def test_lesson_nine_editorial_html_and_question_mappings(client, app):
    lesson_id = "st3-l09-andhra-pradesh-ecosystems-biodiversity"
    page = client.get(
        f"/learn/science-technology/{SLUG}/textbook/{lesson_id}")
    assert page.status_code == 200
    assert b'data-editorial-html="true"' in page.data
    assert b"Andhra Pradesh Ecosystems and Biodiversity" in page.data
    assert page.data.count(b'class="editorial-section"') == 4
    for section_id in ("l9-a", "l9-b", "l9-c", "l9-d"):
        assert f'id="{lesson_id}-{section_id}"'.encode() in page.data
    with app.app_context():
        questions = science_content.approved_questions(SLUG, lesson_id)
    assert len(questions) == 136


def test_lesson_nine_concept_map_covers_every_question_and_asset(app, client):
    lesson_id = "st3-l09-andhra-pradesh-ecosystems-biodiversity"
    with app.app_context():
        mapping = science_content.load_concept_map(SLUG, lesson_id)
        questions = science_content.approved_questions(SLUG, lesson_id)

    assert mapping is not None
    assert len(mapping["concepts"]) == 28
    assert len({concept["id"] for concept in mapping["concepts"]}) == 28
    assert len(questions) == 136
    assert all(
        science_content.concept_for_question(SLUG, question)
        for question in questions
    )

    root = (
        Path(app.static_folder) / "infographics" / "science" / lesson_id
        / mapping["asset_directory"]
    )
    referenced = {
        filename
        for concept in mapping["concepts"]
        for filename in (concept["concept_file"], concept["full_file"])
    }
    assert len(referenced) == 56
    for filename in referenced:
        path = root / filename
        assert path.is_file()
        with path.open("rb") as image_file:
            assert image_file.read(8) == b"\x89PNG\r\n\x1a\n"
            chunk_length = struct.unpack(">I", image_file.read(4))[0]
            assert image_file.read(4) == b"IHDR"
            assert chunk_length == 13
            width, height = struct.unpack(">II", image_file.read(8))
        assert (width, height) == (1024, 1536)

    explanation = client.get(
        f"/learn/science-technology/{SLUG}/practice/explanation/"
        "st3-l09-a-q001")
    assert explanation.status_code == 200
    assert explanation.data.count(b"<figure data-slide=") == 2
    assert b"a01-ap-biogeographic-units-concept.png" in explanation.data
    assert b"a01-ap-biogeographic-units-full.png" in explanation.data


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
        assert summary == {"total": 1297, "approved": 1297, "draft": 0}
        assert len(science_content.approved_questions(SLUG)) == 1297
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
    assert b"1 / 1297" in page.data
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
    assert b'draggable="false"' in page.data
    assert b'infography-reading' in page.data
    assert b'<header class="card">' not in page.data
    assert b'How Organisms Respond to Environmental Variation' in page.data
    assert b'concept-pairs/1c-c01-four-responses-concept.png' in page.data
    assert b'concept-pairs/1c-c01-four-responses-full.png' in page.data
    assert page.data.count(b'<figure data-slide=') == 2


def test_infography_reader_is_responsive_and_keeps_native_zoom(client):
    css = client.get("/static/ds.css")
    assert css.status_code == 200
    assert b"scroll-snap-type:x mandatory" in css.data
    assert b"scroll-snap-stop:always" in css.data
    assert b"touch-action:pan-x pan-y pinch-zoom" in css.data
    assert b".infography-reading body{padding:0" in css.data
    assert b".infography-reading .question-visual-pair img{width:min(100%,900px);height:auto;max-width:none;max-height:none;object-fit:contain}" in css.data

    page = client.get(
        f"/learn/science-technology/{SLUG}/practice/explanation/"
        "st3-l01-01a-q001")
    assert page.status_code == 200
    assert b'width=device-width,initial-scale=1,viewport-fit=cover' in page.data
    assert b'user-scalable=no' not in page.data
    assert page.data.count(b'id="exit-infography"') == 1


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


def test_lesson_one_concept_map_covers_every_applicable_mcq(app):
    with app.app_context():
        mapping = science_content.load_concept_map(SLUG)
        assert mapping is not None
        assert len(mapping["concepts"]) == 38
        assert len({item["id"] for item in mapping["concepts"]}) == 38

        questions = science_content.approved_questions(
            SLUG, lesson_id="st3-l01-ecology-foundations")
        resolved = {
            question["id"]: science_content.concept_for_question(SLUG, question)
            for question in questions
        }
        assert [question_id for question_id, concept in resolved.items()
                if concept is None] == ["st3-int-a-q003"]
        assert resolved["st3-int-a-q001"]["id"] == "1e-c06"
        assert resolved["st3-int-a-q002"]["id"] == "1e-c03"
        assert resolved["st3-int-a-q004"]["id"] == "1e-c05"
        assert resolved["st3-l01-01b-i-q008"]["id"] == "1b-c07"
        assert resolved["st3-l01-01b-i-q009"]["id"] == "1b-c11"


def test_per_lesson_concept_map_is_selected_without_replacing_lesson_one(
        app, tmp_path):
    source = Path(app.config["TEXTBOOK_ROOT"]) / SLUG
    target = tmp_path / SLUG
    shutil.copytree(source, target)
    lesson_two = "st3-l02-population-community-succession"
    concept_dir = target / "concept_maps"
    concept_dir.mkdir(exist_ok=True)
    lesson_two_map = {
        "chapter_slug": SLUG,
        "lesson_id": lesson_two,
        "asset_directory": "concept-pairs",
        "concepts": [{
            "id": "2a-c01",
            "section_id": f"{lesson_two}-section-2a",
            "title": "Population attributes",
            "concept_file": "2a-c01-concept.png",
            "full_file": "2a-c01-full.png",
            "fact_ids": ["st3-l02-02a-f001"],
        }],
        "question_overrides": {},
    }
    (concept_dir / f"{lesson_two}.json").write_text(
        json.dumps(lesson_two_map), encoding="utf-8")
    app.config["TEXTBOOK_ROOT"] = tmp_path

    with app.app_context():
        legacy = science_content.load_concept_map(SLUG)
        lesson_one = science_content.load_concept_map(
            SLUG, "st3-l01-ecology-foundations")
        selected = science_content.load_concept_map(SLUG, lesson_two)
        wrong_lesson_question = {
            "id": "synthetic-l01", "lesson_id": "st3-l01-ecology-foundations",
            "fact_ids": ["st3-l02-02a-f001"],
        }
        lesson_two_question = {
            "id": "synthetic-l02", "lesson_id": lesson_two,
            "fact_ids": ["st3-l02-02a-f001"],
        }

        assert legacy["lesson_id"] == "st3-l01-ecology-foundations"
        assert lesson_one == legacy
        assert selected["lesson_id"] == lesson_two
        assert science_content.concept_for_question(
            SLUG, lesson_two_question)["id"] == "2a-c01"
        assert science_content.concept_for_question(
            SLUG, wrong_lesson_question) is None


def test_per_lesson_concept_map_rejects_unsafe_lesson_path(app):
    with app.app_context():
        assert science_content.load_concept_map(SLUG, "../concept_map") is None
        assert science_content.load_concept_map(SLUG, "lesson/two") is None


def test_lesson_one_mapped_facts_have_exactly_one_concept_owner(app):
    with app.app_context():
        mapping = science_content.load_concept_map(SLUG)
    owners = Counter(
        fact_id
        for concept in mapping["concepts"]
        for fact_id in concept["fact_ids"]
        if fact_id
    )
    assert owners
    assert all(count == 1 for count in owners.values())
    owner = next(concept["id"] for concept in mapping["concepts"]
                 if "st3-l01-01b-i-f005" in concept["fact_ids"])
    assert owner == "1b-c11"


def test_existing_concept_pair_assets_are_declared(app):
    with app.app_context():
        mapping = science_content.load_concept_map(SLUG)
    declared = {
        filename
        for concept in mapping["concepts"]
        for filename in (concept["concept_file"], concept["full_file"])
    }
    root = Path(app.static_folder) / "infographics" / "science" / \
        "st3-l01-ecology-foundations" / mapping["asset_directory"]
    existing = {path.name for path in root.glob("*.png")}
    assert len(declared) == 76
    assert existing == declared
    assert all((root / filename).stat().st_size > 0 for filename in declared)


def test_lesson_two_concept_map_and_assets_are_complete(app):
    lesson_id = "st3-l02-population-community-succession"
    with app.app_context():
        mapping = science_content.load_concept_map(SLUG, lesson_id)

    assert mapping is not None
    assert len(mapping["concepts"]) == 13
    assert len({item["id"] for item in mapping["concepts"]}) == 13

    owners = Counter(
        fact_id
        for concept in mapping["concepts"]
        for fact_id in concept["fact_ids"]
        if fact_id
    )
    assert len(owners) == 96
    assert all(count == 1 for count in owners.values())

    declared = {
        filename
        for concept in mapping["concepts"]
        for filename in (concept["concept_file"], concept["full_file"])
    }
    root = Path(app.static_folder) / "infographics" / "science" / \
        lesson_id / mapping["asset_directory"]
    existing = {path.name for path in root.glob("*.png")}
    assert len(declared) == 26
    assert existing == declared
    assert all((root / filename).stat().st_size > 0 for filename in declared)


def test_lesson_two_question_opens_its_concept_pair(client):
    page = client.get(
        f"/learn/science-technology/{SLUG}/practice/explanation/"
        "st3-l02-02a-q001")
    assert page.status_code == 200
    assert b"concept-pairs/2a-c01-population-density-age-pyramids-concept.png" in page.data
    assert b"concept-pairs/2a-c01-population-density-age-pyramids-full.png" in page.data
    assert page.data.count(b'<figure data-slide=') == 2


def test_every_lesson_two_mcq_has_a_concept_pair(app):
    lesson_id = "st3-l02-population-community-succession"
    with app.app_context():
        questions = science_content.approved_questions(
            SLUG, lesson_id=lesson_id)
        unresolved = [
            question["id"] for question in questions
            if science_content.concept_for_question(SLUG, question) is None
        ]
    assert len(questions) == 171
    assert unresolved == []


def test_lesson_three_concept_map_fact_owners_and_assets_are_complete(app):
    lesson_id = "st3-l03-ecosystem-structure-energy-cycles"
    with app.app_context():
        mapping = science_content.load_concept_map(SLUG, lesson_id)

    assert mapping is not None
    assert len(mapping["concepts"]) == 15
    assert len({item["id"] for item in mapping["concepts"]}) == 15

    owners = Counter(
        fact_id
        for concept in mapping["concepts"]
        for fact_id in concept["fact_ids"]
        if fact_id
    )
    fact_path = Path(app.config["TEXTBOOK_ROOT"]) / SLUG / "facts.jsonl"
    lesson_fact_ids = {
        row["fact_id"]
        for line in fact_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
        for row in [json.loads(line)]
        if row.get("lesson_id") == lesson_id
    }
    assert len(lesson_fact_ids) == 71
    assert set(owners) == lesson_fact_ids
    assert all(count == 1 for count in owners.values())

    declared = {
        filename
        for concept in mapping["concepts"]
        for filename in (concept["concept_file"], concept["full_file"])
    }
    root = Path(app.static_folder) / "infographics" / "science" / \
        lesson_id / mapping["asset_directory"]
    existing = {path.name for path in root.glob("*.png")}
    assert len(declared) == 30
    assert existing == declared
    assert all((root / filename).stat().st_size > 0 for filename in declared)


def test_every_lesson_three_core_mcq_has_a_concept_pair(app):
    lesson_id = "st3-l03-ecosystem-structure-energy-cycles"
    with app.app_context():
        lesson_questions = science_content.approved_questions(
            SLUG, lesson_id=lesson_id)
        core_questions = [
            question for question in lesson_questions
            if question.get("collection") is None
        ]
        unresolved = [
            question["id"] for question in core_questions
            if science_content.concept_for_question(SLUG, question) is None
        ]
    assert len(core_questions) == 76
    assert unresolved == []


def test_lesson_three_question_opens_exactly_two_concept_slides(client):
    page = client.get(
        f"/learn/science-technology/{SLUG}/practice/explanation/"
        "st3-l03-3d-manual-q001")
    assert page.status_code == 200
    assert b"concept-pairs/3d-c01-productivity-gpp-npp-stocks-concept.png" in page.data
    assert b"concept-pairs/3d-c01-productivity-gpp-npp-stocks-full.png" in page.data
    assert page.data.count(b'<figure data-slide=') == 2


def test_lesson_four_concept_map_fact_owners_and_assets_are_complete(app):
    lesson_id = "st3-l04-ecosystem-types-indian-biogeography"
    with app.app_context():
        mapping = science_content.load_concept_map(SLUG, lesson_id)

    assert mapping is not None
    assert len(mapping["concepts"]) == 20
    assert len({item["id"] for item in mapping["concepts"]}) == 20

    owners = Counter(
        fact_id
        for concept in mapping["concepts"]
        for fact_id in concept["fact_ids"]
        if fact_id
    )
    fact_path = Path(app.config["TEXTBOOK_ROOT"]) / SLUG / "facts.jsonl"
    lesson_fact_ids = {
        row["fact_id"]
        for line in fact_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
        for row in [json.loads(line)]
        if row.get("lesson_id") == lesson_id
    }
    assert len(lesson_fact_ids) == 101
    assert set(owners) == lesson_fact_ids
    assert all(count == 1 for count in owners.values())

    declared = {
        filename
        for concept in mapping["concepts"]
        for filename in (concept["concept_file"], concept["full_file"])
    }
    root = Path(app.static_folder) / "infographics" / "science" / \
        lesson_id / mapping["asset_directory"]
    existing = {path.name for path in root.glob("*.png")}
    assert len(declared) == 40
    assert existing == declared
    assert all((root / filename).stat().st_size > 0 for filename in declared)


def test_every_lesson_four_core_mcq_has_a_concept_pair(app):
    lesson_id = "st3-l04-ecosystem-types-indian-biogeography"
    with app.app_context():
        lesson_questions = science_content.approved_questions(
            SLUG, lesson_id=lesson_id)
        core_questions = [
            question for question in lesson_questions
            if question.get("collection") is None
        ]
        unresolved = [
            question["id"] for question in core_questions
            if science_content.concept_for_question(SLUG, question) is None
        ]
    assert len(core_questions) == 120
    assert unresolved == []


def test_lesson_four_question_opens_exactly_two_concept_slides(client):
    page = client.get(
        f"/learn/science-technology/{SLUG}/practice/explanation/"
        "st3-l04-04d04f-manual-q001")
    assert page.status_code == 200
    assert (
        b"concept-pairs/04d-c01-freshwater-systems-horizontal-lake-zones-"
        b"concept.png" in page.data
    )
    assert (
        b"concept-pairs/04d-c01-freshwater-systems-horizontal-lake-zones-"
        b"full.png" in page.data
    )
    assert page.data.count(b'<figure data-slide=') == 2


def test_lesson_five_concept_map_fact_owners_and_assets_are_complete(app):
    lesson_id = "st3-l05-biodiversity-loss-conservation"
    with app.app_context():
        mapping = science_content.load_concept_map(SLUG, lesson_id)

    assert mapping is not None
    assert len(mapping["concepts"]) == 18
    assert len({item["id"] for item in mapping["concepts"]}) == 18

    owners = Counter(
        fact_id
        for concept in mapping["concepts"]
        for fact_id in concept["fact_ids"]
        if fact_id
    )
    fact_path = Path(app.config["TEXTBOOK_ROOT"]) / SLUG / "facts.jsonl"
    lesson_fact_ids = {
        row["fact_id"]
        for line in fact_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
        for row in [json.loads(line)]
        if row.get("lesson_id") == lesson_id
    }
    assert len(lesson_fact_ids) == 77
    assert set(owners) == lesson_fact_ids
    assert all(count == 1 for count in owners.values())

    declared = {
        filename
        for concept in mapping["concepts"]
        for filename in (concept["concept_file"], concept["full_file"])
    }
    root = Path(app.static_folder) / "infographics" / "science" / \
        lesson_id / mapping["asset_directory"]
    existing = {path.name for path in root.glob("*.png")}
    assert len(declared) == 36
    assert existing == declared
    assert all((root / filename).stat().st_size > 0 for filename in declared)


def test_every_lesson_five_core_mcq_has_a_concept_pair(app):
    lesson_id = "st3-l05-biodiversity-loss-conservation"
    with app.app_context():
        lesson_questions = science_content.approved_questions(
            SLUG, lesson_id=lesson_id)
        core_questions = [
            question for question in lesson_questions
            if question.get("collection") is None
        ]
        unresolved = [
            question["id"] for question in core_questions
            if science_content.concept_for_question(SLUG, question) is None
        ]
    assert len(core_questions) == 96
    assert unresolved == []


def test_lesson_five_question_opens_exactly_two_concept_slides(client):
    page = client.get(
        f"/learn/science-technology/{SLUG}/practice/explanation/"
        "st3-l05-a-manual-q001")
    assert page.status_code == 200
    assert (
        b"concept-pairs/05a-c01-biodiversity-levels-richness-evenness-"
        b"indices-concept.png" in page.data
    )
    assert (
        b"concept-pairs/05a-c01-biodiversity-levels-richness-evenness-"
        b"indices-full.png" in page.data
    )
    assert page.data.count(b'<figure data-slide=') == 2


def test_lesson_six_concept_map_fact_owners_and_assets_are_complete(app):
    lesson_id = "st3-l06-global-frameworks-conventions"
    with app.app_context():
        mapping = science_content.load_concept_map(SLUG, lesson_id)

    assert mapping is not None
    assert len(mapping["concepts"]) == 37
    assert len({item["id"] for item in mapping["concepts"]}) == 37

    owners = Counter(
        fact_id
        for concept in mapping["concepts"]
        for fact_id in concept["fact_ids"]
        if fact_id
    )
    fact_path = Path(app.config["TEXTBOOK_ROOT"]) / SLUG / "facts.jsonl"
    lesson_fact_ids = {
        row["fact_id"]
        for line in fact_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
        for row in [json.loads(line)]
        if row.get("lesson_id") == lesson_id
    }
    assert len(lesson_fact_ids) == 65
    assert set(owners) == lesson_fact_ids
    assert all(count == 1 for count in owners.values())

    declared = {
        filename
        for concept in mapping["concepts"]
        for filename in (concept["concept_file"], concept["full_file"])
    }
    root = Path(app.static_folder) / "infographics" / "science" / \
        lesson_id / mapping["asset_directory"]
    existing = {path.name for path in root.glob("*.png")}
    assert len(declared) == 74
    assert existing == declared
    assert all((root / filename).stat().st_size > 0 for filename in declared)


def test_every_lesson_six_mcq_has_a_concept_pair(app):
    lesson_id = "st3-l06-global-frameworks-conventions"
    with app.app_context():
        lesson_questions = science_content.approved_questions(
            SLUG, lesson_id=lesson_id)
        unresolved = [
            question["id"] for question in lesson_questions
            if science_content.concept_for_question(SLUG, question) is None
        ]
    assert len(lesson_questions) == 144
    assert unresolved == []


def test_lesson_six_question_opens_concept_and_explanation_images(client):
    page = client.get(
        f"/learn/science-technology/{SLUG}/practice/explanation/"
        "st3-l06-a-q049")
    assert page.status_code == 200
    assert b"concept-pairs/l6-a-01-concept.png" in page.data
    assert b"concept-pairs/l6-a-01-full.png" in page.data
    assert page.data.count(b'<figure data-slide=') == 2


def test_question_uses_exact_concept_pair_when_both_assets_exist(client):
    page = client.get(
        f"/learn/science-technology/{SLUG}/practice/explanation/"
        "st3-l01-01a-q001")
    assert page.status_code == 200
    assert b"concept-pairs/1a-c01-ecology-meaning-concept.png" in page.data
    assert b"concept-pairs/1a-c01-ecology-meaning-full.png" in page.data
    assert page.data.count(b'<figure data-slide=') == 2


def test_cross_lesson_population_regulation_is_not_mapped_to_niche(client):
    page = client.get(
        f"/learn/science-technology/{SLUG}/practice/explanation/"
        "st3-int-a-q003")
    assert page.status_code == 200
    assert b"concept-pairs/1d-c02" not in page.data
    assert b"concept-pairs/1d-c03" not in page.data
    assert b"05-habitat-vs-niche-bilingual.png" in page.data
    assert b"14-section-1d-full-explanation-bilingual.png" in page.data


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
