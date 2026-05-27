"""Phase 4 — Notes routes + chapter progress API tests."""
import json
import pytest
from app import create_app
from app.config import Config
from app.db import db as _db
from app.models import Subject, Chapter, Note, ChapterProgress


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SECRET_KEY = "test"


@pytest.fixture()
def app():
    app = create_app(TestConfig)
    with app.app_context():
        _db.create_all()
        yield app
        _db.session.remove()
        _db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def seeded_app(app):
    """App with one subject, two chapters, and notes."""
    with app.app_context():
        s = Subject(slug="polity", name_en="Polity", name_te="పాలిటీ")
        _db.session.add(s)
        _db.session.flush()
        c1 = Chapter(subject_id=s.id, chapter_num=1,
                     title_en="Preamble", title_te="ప్రవేశిక", est_read_minutes=10)
        c2 = Chapter(subject_id=s.id, chapter_num=2,
                     title_en="Fundamental Rights", title_te="ప్రాథమిక హక్కులు")
        _db.session.add_all([c1, c2])
        _db.session.flush()
        n1 = Note(chapter_id=c1.id, section_num=1,
                  heading_en="Introduction", heading_te="పరిచయం",
                  body_en="<p>The preamble is the soul of the Constitution.</p>",
                  body_te="<p>ప్రవేశిక రాజ్యాంగం యొక్క ఆత్మ.</p>")
        n2 = Note(chapter_id=c1.id, section_num=2,
                  heading_en="Key Terms", heading_te="కీలక పదాలు",
                  body_en="<p>Sovereign, Socialist, Secular.</p>",
                  body_te="<p>సార్వభౌమ, సామ్యవాద, లౌకిక.</p>")
        _db.session.add_all([n1, n2])
        _db.session.commit()
    return app


@pytest.fixture()
def seeded_client(seeded_app):
    return seeded_app.test_client()


# ── Chapter list ─────────────────────────────────────────────────

def test_chapter_list_returns_200(seeded_client):
    r = seeded_client.get("/notes/polity")
    assert r.status_code == 200


def test_chapter_list_shows_chapters(seeded_client):
    r = seeded_client.get("/notes/polity")
    assert b"Preamble" in r.data
    assert b"Fundamental Rights" in r.data


def test_chapter_list_404_unknown_subject(seeded_client):
    r = seeded_client.get("/notes/nonexistent_subject")
    assert r.status_code == 404


def test_chapter_list_shows_notes_link(seeded_client):
    """Chapter list page links to the note reader."""
    r = seeded_client.get("/notes/polity")
    assert b"/notes/polity/1" in r.data


# ── Note reader ──────────────────────────────────────────────────

def test_reader_returns_200(seeded_client):
    r = seeded_client.get("/notes/polity/1")
    assert r.status_code == 200


def test_reader_shows_note_content(seeded_client):
    r = seeded_client.get("/notes/polity/1")
    assert b"preamble is the soul" in r.data
    assert b"Sovereign, Socialist" in r.data


def test_reader_404_wrong_chapter(seeded_client):
    r = seeded_client.get("/notes/polity/99")
    assert r.status_code == 404


def test_reader_has_next_link(seeded_client):
    """Chapter 1 should have a Next link to chapter 2."""
    r = seeded_client.get("/notes/polity/1")
    assert b"/notes/polity/2" in r.data


def test_reader_last_chapter_no_next(seeded_client):
    """Chapter 2 (last) should not have a Next link."""
    r = seeded_client.get("/notes/polity/2")
    assert b"/notes/polity/3" not in r.data


def test_reader_shows_mark_complete_button(seeded_client):
    r = seeded_client.get("/notes/polity/1")
    assert b"btn-complete" in r.data


def test_reader_empty_chapter_shows_message(seeded_client, seeded_app):
    """Chapter with no notes shows empty state message."""
    r = seeded_client.get("/notes/polity/2")
    assert r.status_code == 200
    assert b"No notes" in r.data or "లేవు".encode("utf-8") in r.data


# ── Progress API ─────────────────────────────────────────────────

def test_progress_complete_upserts(seeded_client, seeded_app):
    """POST /notes/api/progress/<id>/complete creates a ChapterProgress row."""
    with seeded_app.app_context():
        ch = Chapter.query.filter_by(chapter_num=1).first()
        cid = ch.id

    r = seeded_client.post(f"/notes/api/progress/{cid}/complete")
    assert r.status_code == 200
    data = r.get_json()
    assert data["status"] == "completed"
    assert data["chapter_id"] == cid


def test_progress_complete_persists_in_db(seeded_client, seeded_app):
    with seeded_app.app_context():
        ch = Chapter.query.filter_by(chapter_num=1).first()
        cid = ch.id

    seeded_client.post(f"/notes/api/progress/{cid}/complete")

    with seeded_app.app_context():
        prog = ChapterProgress.query.filter_by(chapter_id=cid).first()
        assert prog is not None
        assert prog.status == "completed"
        assert prog.marked_complete_at is not None


def test_progress_complete_idempotent(seeded_client, seeded_app):
    """Calling complete twice doesn't break anything."""
    with seeded_app.app_context():
        ch = Chapter.query.filter_by(chapter_num=1).first()
        cid = ch.id

    r1 = seeded_client.post(f"/notes/api/progress/{cid}/complete")
    r2 = seeded_client.post(f"/notes/api/progress/{cid}/complete")
    assert r1.status_code == 200
    assert r2.status_code == 200


def test_progress_open_sets_in_progress(seeded_client, seeded_app):
    with seeded_app.app_context():
        ch = Chapter.query.filter_by(chapter_num=1).first()
        cid = ch.id

    r = seeded_client.post(f"/notes/api/progress/{cid}/open")
    assert r.status_code == 200
    data = r.get_json()
    assert data["status"] == "in_progress"


def test_progress_open_does_not_downgrade_completed(seeded_client, seeded_app):
    """Once completed, /open should not set status back to in_progress."""
    with seeded_app.app_context():
        ch = Chapter.query.filter_by(chapter_num=1).first()
        cid = ch.id

    seeded_client.post(f"/notes/api/progress/{cid}/complete")
    r = seeded_client.post(f"/notes/api/progress/{cid}/open")
    data = r.get_json()
    assert data["status"] == "completed"


def test_completed_chapter_shows_badge(seeded_client, seeded_app):
    """After marking complete, reader shows completed badge instead of button."""
    with seeded_app.app_context():
        ch = Chapter.query.filter_by(chapter_num=1).first()
        cid = ch.id

    seeded_client.post(f"/notes/api/progress/{cid}/complete",
                       headers={"Cookie": "device_id=testdevice"})
    r = seeded_client.get("/notes/polity/1",
                          headers={"Cookie": "device_id=testdevice"})
    assert b"complete-badge" in r.data
