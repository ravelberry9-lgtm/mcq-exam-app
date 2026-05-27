"""Phase 4.5 — Study Plan tests."""
import pytest
from datetime import date, timedelta
from app import create_app
from app.config import Config
from app.db import db as _db
from app.models import Subject, Chapter, Exam, ExamPaper, ExamSection, ExamSyllabusItem, StudyPlan, ChapterProgress


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SECRET_KEY = "test"


@pytest.fixture()
def app():
    a = create_app(TestConfig)
    with a.app_context():
        _db.create_all()
        yield a
        _db.session.remove()
        _db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def seeded(app):
    with app.app_context():
        s = Subject(slug="polity", name_en="Polity", name_te="पालिटी")
        _db.session.add(s)
        _db.session.flush()
        c1 = Chapter(subject_id=s.id, chapter_num=1, title_en="Preamble", title_te="प्रवेशिक")
        c2 = Chapter(subject_id=s.id, chapter_num=2, title_en="Rights", title_te="हक्कुलु")
        _db.session.add_all([c1, c2])
        _db.session.flush()
        e = Exam(slug="appsc_g2", name_en="APPSC Group 2", name_te="ग्रूप् 2")
        _db.session.add(e)
        _db.session.flush()
        p = ExamPaper(exam_id=e.id, paper_num=1, name_en="Paper I", name_te="पेपर् I", total_marks=150)
        _db.session.add(p)
        _db.session.flush()
        sec = ExamSection(paper_id=p.id, section_label="A", name_en="Polity", name_te="पालिटी", marks=75)
        _db.session.add(sec)
        _db.session.flush()
        _db.session.add(ExamSyllabusItem(section_id=sec.id, chapter_id=c1.id))
        _db.session.add(ExamSyllabusItem(section_id=sec.id, chapter_id=c2.id))
        _db.session.commit()
        return {"exam_id": e.id, "exam_slug": e.slug, "c1_id": c1.id, "c2_id": c2.id}


# ── New plan page ─────────────────────────────────────────────────────────────────

def test_new_plan_page_returns_200(client, seeded):
    r = client.get("/plan/new")
    assert r.status_code == 200


def test_new_plan_shows_exam_options(client, seeded):
    r = client.get("/plan/new")
    assert b"APPSC Group 2" in r.data


# ── Create plan ────────────────────────────────────────────────────────────────────

def test_create_plan_redirects_to_dashboard(client, seeded):
    target = (date.today() + timedelta(days=60)).isoformat()
    r = client.post("/plan/create", data={
        "name": "Test Plan",
        "exam_id": seeded["exam_id"],
        "target_date": target,
    })
    assert r.status_code == 302
    assert "/plan/" in r.headers["Location"]


def test_create_plan_persists(client, app, seeded):
    target = (date.today() + timedelta(days=60)).isoformat()
    client.post("/plan/create", data={
        "name": "My Plan",
        "exam_id": seeded["exam_id"],
        "target_date": target,
    })
    with app.app_context():
        plan = StudyPlan.query.first()
        assert plan is not None
        assert plan.name == "My Plan"
        assert plan.status == "active"


def test_create_plan_pauses_existing(client, app, seeded):
    target = (date.today() + timedelta(days=60)).isoformat()
    client.post("/plan/create", data={"name": "Plan 1", "target_date": target})
    client.post("/plan/create", data={"name": "Plan 2", "target_date": target})
    with app.app_context():
        plans = StudyPlan.query.all()
        active = [p for p in plans if p.status == "active"]
        paused = [p for p in plans if p.status == "paused"]
        assert len(active) == 1
        assert len(paused) == 1


# ── Dashboard ──────────────────────────────────────────────────────────────────────

def test_dashboard_redirects_to_new_if_no_plan(client):
    r = client.get("/plan/")
    assert r.status_code == 302
    assert "/plan/new" in r.headers["Location"]


def test_dashboard_returns_200_with_plan(client, seeded):
    target = (date.today() + timedelta(days=60)).isoformat()
    client.post("/plan/create", data={
        "name": "Test Plan", "exam_id": seeded["exam_id"], "target_date": target
    })
    r = client.get("/plan/")
    assert r.status_code == 200


def test_dashboard_shows_chapters(client, seeded):
    target = (date.today() + timedelta(days=60)).isoformat()
    client.post("/plan/create", data={
        "name": "Test Plan", "exam_id": seeded["exam_id"], "target_date": target
    })
    r = client.get("/plan/")
    assert b"Preamble" in r.data


def test_dashboard_shows_completion_pct(client, seeded):
    target = (date.today() + timedelta(days=60)).isoformat()
    client.post("/plan/create", data={
        "name": "Test Plan", "exam_id": seeded["exam_id"], "target_date": target
    })
    r = client.get("/plan/")
    assert b"%" in r.data


def test_dashboard_reflects_completed_chapter(client, app, seeded):
    target = (date.today() + timedelta(days=60)).isoformat()
    client.post("/plan/create", data={
        "name": "Test Plan", "exam_id": seeded["exam_id"], "target_date": target
    })
    # Mark c1 as completed via notes API
    client.post(f"/notes/api/progress/{seeded['c1_id']}/complete")
    r = client.get("/plan/")
    assert b"completed" in r.data


# ── Pause plan ──────────────────────────────────────────────────────────────────────

def test_pause_plan(client, app, seeded):
    target = (date.today() + timedelta(days=60)).isoformat()
    client.post("/plan/create", data={"name": "Plan", "target_date": target})
    with app.app_context():
        plan_id = StudyPlan.query.first().id
    r = client.post(f"/plan/api/{plan_id}/pause")
    assert r.status_code == 200
    with app.app_context():
        assert StudyPlan.query.get(plan_id).status == "paused"
