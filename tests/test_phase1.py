"""Phase 1 tests — drawer, subjects, practice, answer scoring."""
import pytest
from app.db import db
from app.models import Subject, Chapter, Question, NavItem


@pytest.fixture()
def seeded(app):
    """Minimal hand-seeded data for Phase 1 routes."""
    with app.app_context():
        s = Subject(slug="polity", name_en="Polity", name_te="పాలిటీ", sort_order=1)
        db.session.add(s); db.session.flush()
        c = Chapter(subject_id=s.id, chapter_num=1, title_en="Preamble", title_te="ప్రవేశిక")
        db.session.add(c); db.session.flush()
        q = Question(
            subject_id=s.id, chapter_id=c.id, source_type="chapter", difficulty="M",
            question_en="What is the Preamble?",
            question_te="ప్రవేశిక ఏమిటి?",
            options_en={"a": "Intro", "b": "Body", "c": "End", "d": "Annex"},
            options_te={"a": "పరిచయం", "b": "ముఖ్య భాగం", "c": "ముగింపు", "d": "అనుబంధం"},
            correct_answer="a",
            explanation_en="The Preamble is the introduction.",
            explanation_te="ప్రవేశిక అనేది పరిచయం.",
        )
        db.session.add(q)
        # Nav items
        home = NavItem(surface="menu", label_en="Home", label_te="హోమ్", action_type="route", action_ref="/", sort_order=0)
        db.session.add(home); db.session.flush()
        subs = NavItem(surface="menu", label_en="Subjects", label_te="విషయాలు", sort_order=10)
        db.session.add(subs); db.session.flush()
        polity = NavItem(surface="menu", parent_id=subs.id, label_en="Polity", label_te="పాలిటీ",
                         action_type="subject", action_ref="polity", sort_order=1)
        db.session.add(polity)
        db.session.commit()
        return {"subject": s.slug, "question_id": q.id}


def test_subjects_page_lists_seeded_subject(client, seeded):
    r = client.get("/subjects")
    assert r.status_code == 200
    assert b"\xe0\xb0\xaa\xe0\xb0\xbe\xe0\xb0\xb2\xe0\xb0\xbf\xe0\xb0\x9f\xe0\xb1\x80" in r.data  # పాలిటీ
    assert b"Polity" in r.data
    assert b"1 chapters" in r.data
    assert b"1 Q" in r.data


def test_drawer_renders_nav_tree(client, seeded):
    r = client.get("/")
    assert r.status_code == 200
    # Top-level items
    assert b"Home" in r.data
    assert b"Subjects" in r.data
    # Nested child
    assert b"Polity" in r.data


def test_practice_page_renders_question(client, seeded):
    r = client.get(f"/practice/{seeded['subject']}")
    assert r.status_code == 200
    assert b"What is the Preamble" in r.data
    assert b"How sure" in r.data
    assert b"Submit answer" in r.data
    # All four options labels
    for letter in [b">A<", b">B<", b">C<", b">D<"]:
        assert letter in r.data


def test_practice_page_with_no_questions_for_subject(client, app):
    """Subject exists but no questions — empty state, not 500."""
    with app.app_context():
        s = Subject(slug="empty_subj", name_en="Empty", name_te="ఖాళీ", sort_order=99)
        db.session.add(s); db.session.commit()
    r = client.get("/practice/empty_subj")
    assert r.status_code == 200
    assert b"No questions yet" in r.data


def test_answer_correct(client, seeded):
    r = client.post("/api/answer", json={
        "question_id": seeded["question_id"], "chosen": "a", "confidence": 4
    })
    assert r.status_code == 200
    data = r.get_json()
    assert data["correct"] is True
    assert data["correct_answer"] == "a"
    assert "coaching_te" in data
    assert "coaching_en" in data


def test_answer_wrong(client, seeded):
    r = client.post("/api/answer", json={
        "question_id": seeded["question_id"], "chosen": "b", "confidence": 5
    })
    data = r.get_json()
    assert data["correct"] is False
    assert data["correct_answer"] == "a"
    assert data["chosen"] == "b"


def test_answer_invalid_payload(client, seeded):
    r = client.post("/api/answer", json={"question_id": seeded["question_id"], "chosen": "z"})
    assert r.status_code == 400


def test_settings_get_and_post_cookie(client):
    r = client.get("/settings")
    assert r.status_code == 200
    assert b"Language" in r.data
    # POST sets cookie
    r = client.post("/settings", data={"lang": "te"}, follow_redirects=False)
    assert r.status_code == 302
    assert any("lang=te" in c for c in r.headers.getlist("Set-Cookie"))


def test_home_shows_quick_chips_when_subjects_exist(client, seeded):
    r = client.get("/")
    assert r.status_code == 200
    # Quick chip for Polity should appear
    assert b"Quick start" in r.data
    assert b"Polity" in r.data
