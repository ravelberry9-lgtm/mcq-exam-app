"""Phase 3 smoke tests for admin blueprint."""
import pytest
from app.models import Subject, Chapter, Note
from app.db import db


def test_admin_login_page_renders(client):
    r = client.get("/admin/login")
    assert r.status_code == 200
    assert b"PIN" in r.data


def test_admin_index_requires_auth(client):
    r = client.get("/admin/", follow_redirects=False)
    assert r.status_code == 302
    assert "/admin/login" in r.headers["Location"]


def test_admin_login_wrong_pin(client):
    r = client.post("/admin/login", data={"pin": "9999"})
    assert r.status_code == 200
    assert b"Incorrect" in r.data


def test_admin_login_correct_pin(client):
    r = client.post("/admin/login", data={"pin": "1234"}, follow_redirects=True)
    assert r.status_code == 200
    assert b"Admin" in r.data


def test_admin_notes_list_requires_auth(client):
    r = client.get("/admin/notes", follow_redirects=False)
    assert r.status_code == 302


def test_admin_notes_list_after_login(client, app):
    with app.app_context():
        subj = Subject(slug="test_admin", name_en="Test", name_te="టెస్ట్", sort_order=99)
        db.session.add(subj)
        db.session.flush()
        ch = Chapter(subject_id=subj.id, chapter_num=1,
                     title_en="Test Ch", title_te="టెస్ట్ ch")
        db.session.add(ch)
        db.session.commit()
        ch_id = ch.id

    with client.session_transaction() as sess:
        import hashlib
        sess["admin_token"] = hashlib.sha256(b"admin:1234").hexdigest()

    r = client.get("/admin/notes")
    assert r.status_code == 200
    assert b"Test" in r.data


def test_admin_notes_edit_get(client, app):
    with app.app_context():
        subj = Subject(slug="test_edit", name_en="Edit Subject",
                       name_te="ఎడిట్", sort_order=99)
        db.session.add(subj)
        db.session.flush()
        ch = Chapter(subject_id=subj.id, chapter_num=1,
                     title_en="Edit Ch", title_te="ఎడిట్ ch")
        db.session.add(ch)
        db.session.commit()
        ch_id = ch.id

    with client.session_transaction() as sess:
        import hashlib
        sess["admin_token"] = hashlib.sha256(b"admin:1234").hexdigest()

    r = client.get(f"/admin/notes/{ch_id}/edit")
    assert r.status_code == 200
    assert b"Edit Ch" in r.data
    assert b"body_te" in r.data
    assert b"body_en" in r.data


def test_admin_notes_edit_post_saves(client, app):
    with app.app_context():
        subj = Subject(slug="test_save", name_en="Save Subject",
                       name_te="సేవ్", sort_order=99)
        db.session.add(subj)
        db.session.flush()
        ch = Chapter(subject_id=subj.id, chapter_num=1,
                     title_en="Save Ch", title_te="సేవ్ ch")
        db.session.add(ch)
        db.session.commit()
        ch_id = ch.id

    with client.session_transaction() as sess:
        import hashlib
        sess["admin_token"] = hashlib.sha256(b"admin:1234").hexdigest()

    r = client.post(f"/admin/notes/{ch_id}/edit", data={
        "body_en": "<p>Hello <script>bad()</script> World</p>",
        "body_te": "<p>నమస్కారం</p>",
        "heading_en": "Test Section",
        "heading_te": "పరీక్ష",
    }, follow_redirects=True)
    assert r.status_code == 200

    with app.app_context():
        note = Note.query.filter_by(chapter_id=ch_id, section_num=1).first()
        assert note is not None
        assert "Hello" in note.body_en
        assert "<script>" not in note.body_en  # bleach stripped it
        assert "నమస్కారం" in note.body_te
