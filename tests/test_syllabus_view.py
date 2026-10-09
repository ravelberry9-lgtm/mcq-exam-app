"""Canonical AP History learner pages: read-only, bilingual, supplementary chapters visibly distinct, nothing dead-ends."""
import pytest
from bs4 import BeautifulSoup

from app.db import db
from app.models import Chapter, Question, Subject
from app.services import ap_canonical as canon


@pytest.fixture()
def hist(app):
    s = Subject(slug="ap_history", name_en="AP History", name_te="ఆంధ్రప్రదేశ్ చరిత్ర")
    db.session.add(s); db.session.commit()
    return s


@pytest.fixture()
def seeded(hist):
    canon.seed(); canon.seed_taxonomy()
    return hist


def _q(subject, chapter, slug, n):
    return Question(subject_id=subject.id, chapter_id=chapter.id, source_type="chapter", difficulty="E", question_en=f"q{n}",
                    question_te=f"ప్ర{n}", options_en={"a": "A", "b": "B"}, options_te={"a": "అ", "b": "బ"}, correct_answer="a",
                    note_target_slug=slug, import_ref=f"aph-test-{n}")


def test_outline_before_the_structure_is_seeded_is_a_calm_empty_state(client, hist):
    r = client.get("/learn/ap-history")
    assert r.status_code == 200 and "not available yet" in r.get_data(as_text=True)


def test_outline_lists_5_units_31_core_and_4_distinct_supplementary_chapters(client, seeded):
    soup = BeautifulSoup(client.get("/learn/ap-history").data, "html.parser")
    assert len(soup.select("section[aria-labelledby^=u]")) == 5
    links = [a["href"] for a in soup.select("a.card")]
    assert len(links) == 35
    assert len(soup.select("#supp ~ div a.card, section[aria-labelledby=supp] a.card")) == 4
    assert "Supplementary" in soup.select_one("section[aria-labelledby=supp]").get_text()
    assert "Not counted in syllabus completion" in soup.get_text()
    assert BeautifulSoup(client.get("/learn/ap-history").data, "html.parser").select_one("a[data-testid=back-to-learn]")["href"] == "/learn/"


def test_every_outline_link_opens_and_chapters_are_bilingual(client, seeded):
    soup = BeautifulSoup(client.get("/learn/ap-history").data, "html.parser")
    for a in soup.select("a.card"):
        r = client.get(a["href"])
        assert r.status_code == 200, a["href"]
    page = client.get("/learn/ap-history/u1-c04-satavahanas").get_data(as_text=True)
    assert "Satavahanas" in page and "శాతవాహనులు" in page


def test_question_counts_follow_the_note_target_prefix_and_practice_opens_canonical_chapter(client, seeded):
    ch = Chapter(subject_id=seeded.id, chapter_num=5, title_en="Satavahana (legacy)", title_te="శాతవాహన")
    db.session.add(ch); db.session.flush()
    db.session.add_all([_q(seeded, ch, "u1-c04-political-history", 1), _q(seeded, ch, "u1-c04-religion", 2)])
    db.session.commit()
    out = client.get("/learn/ap-history").get_data(as_text=True)
    assert "2 questions" in out
    d = client.get("/learn/ap-history/u1-c04-satavahanas")
    soup = BeautifulSoup(d.data, "html.parser")
    practice_url = soup.select_one("a.card")["href"]
    assert practice_url == "/learn/ap-history/u1-c04-satavahanas/practice"
    assert client.get(practice_url).status_code == 200
    empty = client.get("/learn/ap-history/u1-c05-ikshvakus").get_data(as_text=True)
    assert "No notes or questions linked" in empty


def test_supplementary_chapter_has_no_subtopics_and_is_labelled(client, seeded):
    page = client.get("/learn/ap-history/supp-dynasties-overview").get_data(as_text=True)
    assert "Supplementary" in page and "reference chapter" in page


def test_unknown_chapter_is_404_and_subject_page_uses_outline_only_when_loaded(client, hist):
    assert client.get("/learn/ap-history/nope").status_code == 404
    assert b"canonical-outline" not in client.get("/learn/subject/ap_history").data
    canon.seed()
    response = client.get("/learn/subject/ap_history")
    assert response.status_code == 302
    assert response.location == "/learn/ap-history"


def test_pages_are_read_only(client, seeded):
    assert client.post("/learn/ap-history").status_code == 405


def test_canonical_practice_filters_shared_legacy_chapters_and_combines_multiple_homes(client, seeded):
    chapters = [Chapter(subject_id=seeded.id, chapter_num=n, title_en=f"Legacy {n}", title_te="అధ్యాయం") for n in (1, 2)]
    db.session.add_all(chapters); db.session.flush()
    rows = [_q(seeded, chapters[0], "u1-c04-politics", 101),
            _q(seeded, chapters[1], "u1-c04-religion", 102),
            _q(seeded, chapters[0], "u1-c05-politics", 103),
            _q(seeded, chapters[0], None, 104)]
    db.session.add_all(rows); db.session.commit()
    base = "/learn/ap-history/u1-c04-satavahanas/practice"
    for i, expected in ((1, "q101"), (2, "q102")):
        soup = BeautifulSoup(client.get(f"{base}?i={i}").data, "html.parser")
        assert expected in soup.select_one("#qcard").get_text()
        assert "2" in soup.select_one("#counter").get_text()
        assert "canonical-u1-c04-satavahanas" == soup.select_one("#qcard")["data-topic"]
    assert b'id="summary"' in client.get(f"{base}?i=3").data
    assert b"q101" in client.get(f"{base}?i=-1").data
    assert client.get("/learn/ap-history/unknown/practice").status_code == 404


def test_hub_counts_only_mapped_ap_questions_and_legacy_banks_redirect_without_deletion(client, seeded):
    ch = Chapter(subject_id=seeded.id, chapter_num=1, title_en="Legacy", title_te="అధ్యాయం")
    db.session.add(ch); db.session.flush()
    mapped = _q(seeded, ch, "u1-c04-politics", 1)
    legacy = _q(seeded, ch, None, 2)
    legacy.source_type = "practice"
    db.session.add_all([mapped, legacy]); db.session.commit()
    from app.services.learn import subject_entries
    entry = next(e for e in subject_entries() if e["subject"].id == seeded.id)
    assert entry["chapter_count"] == 31
    assert entry["question_count"] == 1
    for bank in ("practice", "pyq"):
        response = client.get(f"/learn/subject/ap_history/{bank}")
        assert response.status_code == 302 and response.location == "/learn/ap-history"
    assert Question.query.count() == 2


def test_practice_keeps_exact_notes_link_and_empty_state(client, seeded):
    from app.models import Note
    ch = Chapter(subject_id=seeded.id, chapter_num=5, title_en="Satavahana notes", title_te="శాతవాహనులు")
    db.session.add(ch); db.session.flush()
    question = _q(seeded, ch, "u1-c04-politics", 1)
    question.note_section_num = 2
    db.session.add_all([question, Note(chapter_id=ch.id, section_num=2, heading_en="Politics", heading_te="రాజకీయం", body_en="Notes", body_te="నోట్స్")])
    db.session.commit()
    base = "/learn/ap-history/u1-c04-satavahanas"
    soup = BeautifulSoup(client.get(base + "/practice").data, "html.parser")
    link = soup.select_one('[data-testid="read-in-notes"]')
    assert link["data-exact"] == "true"
    assert link["href"] == f"/learn/topic/{ch.id}/notes?section=2"
    assert f'/learn/topic/{ch.id}/notes' in client.get(base).get_data(as_text=True)
    empty = client.get("/learn/ap-history/u1-c05-ikshvakus/practice")
    assert empty.status_code == 200 and b'id="qcard"' not in empty.data
