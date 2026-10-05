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


def test_question_counts_follow_the_note_target_prefix_and_practice_opens_the_holding_chapter(client, seeded):
    ch = Chapter(subject_id=seeded.id, chapter_num=5, title_en="Satavahana (legacy)", title_te="శాతవాహన")
    db.session.add(ch); db.session.flush()
    db.session.add_all([_q(seeded, ch, "u1-c04-political-history", 1), _q(seeded, ch, "u1-c04-religion", 2)])
    db.session.commit()
    out = client.get("/learn/ap-history").get_data(as_text=True)
    assert "2 questions" in out
    d = client.get("/learn/ap-history/u1-c04-satavahanas")
    soup = BeautifulSoup(d.data, "html.parser")
    assert soup.select_one("a.card")["href"] == f"/learn/topic/{ch.id}"
    assert client.get(f"/learn/topic/{ch.id}").status_code == 200
    empty = client.get("/learn/ap-history/u1-c05-ikshvakus").get_data(as_text=True)
    assert "No notes or questions linked" in empty


def test_supplementary_chapter_has_no_subtopics_and_is_labelled(client, seeded):
    page = client.get("/learn/ap-history/supp-dynasties-overview").get_data(as_text=True)
    assert "Supplementary" in page and "reference chapter" in page


def test_unknown_chapter_is_404_and_subject_page_links_the_outline_only_when_loaded(client, hist):
    assert client.get("/learn/ap-history/nope").status_code == 404
    assert b"canonical-outline" not in client.get("/learn/subject/ap_history").data
    canon.seed()
    assert b"canonical-outline" in client.get("/learn/subject/ap_history").data


def test_pages_are_read_only(client, seeded):
    assert client.post("/learn/ap-history").status_code == 405
