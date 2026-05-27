"""Phase 5 — Exam session tests."""
import pytest
from app import create_app
from app.config import Config
from app.db import db as _db
from app.models import (
    Subject, Chapter, Question,
    Exam, ExamPaper, ExamSection, ExamSyllabusItem, ExamSession,
)


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
def seeded(app):
    """Full exam tree with questions."""
    with app.app_context():
        s = Subject(slug="polity", name_en="Polity", name_te="पालिटी")
        _db.session.add(s)
        _db.session.flush()

        c = Chapter(subject_id=s.id, chapter_num=1,
                    title_en="Preamble", title_te="प्रवेशिक")
        _db.session.add(c)
        _db.session.flush()

        for i in range(5):
            q = Question(
                subject_id=s.id, chapter_id=c.id,
                source_type="chapter",
                question_en=f"Question {i+1}?", question_te=f"प्रश्न {i+1}?",
                options_en={"a": "A opt", "b": "B opt", "c": "C opt", "d": "D opt"},
                options_te={"a": "A", "b": "B", "c": "C", "d": "D"},
                correct_answer="a", difficulty="M",
            )
            _db.session.add(q)
        _db.session.flush()

        e = Exam(slug="appsc_g2", name_en="APPSC Group 2",
                 name_te="एपीपीएस‍सी ग्रूप् 2", conducting_body="APPSC")
        _db.session.add(e)
        _db.session.flush()

        p = ExamPaper(exam_id=e.id, paper_num=1, name_en="Paper I",
                      name_te="पेपर् I", total_marks=150, duration_min=150)
        _db.session.add(p)
        _db.session.flush()

        sec = ExamSection(paper_id=p.id, section_label="A",
                          name_en="Polity", name_te="पालिटी", marks=75)
        _db.session.add(sec)
        _db.session.flush()

        item = ExamSyllabusItem(section_id=sec.id, chapter_id=c.id)
        _db.session.add(item)
        _db.session.commit()

        return {
            "exam_slug": e.slug,
            "paper_num": p.paper_num,
            "chapter_id": c.id,
        }


def test_start_creates_session(client, seeded):
    r = client.post(f"/exam/{seeded['exam_slug']}/paper/{seeded['paper_num']}/start")
    assert r.status_code == 302
    location = r.headers["Location"]
    assert "/exam-session/" in location


def test_start_404_unknown_exam(client, seeded):
    r = client.post("/exam/nonexistent/paper/1/start")
    assert r.status_code == 404


def test_start_persists_session(client, app, seeded):
    r = client.post(f"/exam/{seeded['exam_slug']}/paper/{seeded['paper_num']}/start")
    location = r.headers["Location"]
    session_id = location.split("/exam-session/")[1].rstrip("/")
    with app.app_context():
        es = ExamSession.query.get(session_id)
        assert es is not None
        assert len(es.question_ids) == 5
        assert es.submitted_at is None


def _start_and_get_id(client, seeded):
    r = client.post(f"/exam/{seeded['exam_slug']}/paper/{seeded['paper_num']}/start")
    location = r.headers["Location"]
    return location.split("/exam-session/")[1].split("?")[0].rstrip("/")


def test_take_page_returns_200(client, seeded):
    sid = _start_and_get_id(client, seeded)
    r = client.get(f"/exam-session/{sid}")
    assert r.status_code == 200


def test_take_page_shows_question(client, seeded):
    sid = _start_and_get_id(client, seeded)
    r = client.get(f"/exam-session/{sid}")
    assert b"Question 1" in r.data or b"1 / 5" in r.data


def test_take_page_shows_timer(client, seeded):
    sid = _start_and_get_id(client, seeded)
    r = client.get(f"/exam-session/{sid}")
    assert b"exam-timer" in r.data


def test_take_redirects_to_results_if_submitted(client, app, seeded):
    sid = _start_and_get_id(client, seeded)
    client.post(f"/exam-session/{sid}/submit")
    r = client.get(f"/exam-session/{sid}")
    assert r.status_code == 302
    assert "results" in r.headers["Location"]


def test_answer_saves(client, app, seeded):
    sid = _start_and_get_id(client, seeded)
    with app.app_context():
        es = ExamSession.query.get(sid)
        qid = es.question_ids[0]

    r = client.post(f"/exam-session/{sid}/answer",
                    json={"question_id": qid, "chosen": "b"})
    assert r.status_code == 200
    data = r.get_json()
    assert data["saved"] is True
    assert data["answered_count"] == 1


def test_answer_persists_in_db(client, app, seeded):
    sid = _start_and_get_id(client, seeded)
    with app.app_context():
        es = ExamSession.query.get(sid)
        qid = es.question_ids[0]

    client.post(f"/exam-session/{sid}/answer",
                json={"question_id": qid, "chosen": "c"})

    with app.app_context():
        es = ExamSession.query.get(sid)
        assert es.answers.get(str(qid)) == "c"


def test_answer_clear(client, app, seeded):
    sid = _start_and_get_id(client, seeded)
    with app.app_context():
        qid = ExamSession.query.get(sid).question_ids[0]

    client.post(f"/exam-session/{sid}/answer",
                json={"question_id": qid, "chosen": "a"})
    client.post(f"/exam-session/{sid}/answer",
                json={"question_id": qid, "chosen": ""})

    with app.app_context():
        es = ExamSession.query.get(sid)
        assert str(qid) not in (es.answers or {})


def test_answer_rejected_after_submit(client, app, seeded):
    sid = _start_and_get_id(client, seeded)
    client.post(f"/exam-session/{sid}/submit")
    with app.app_context():
        qid = ExamSession.query.get(sid).question_ids[0]
    r = client.post(f"/exam-session/{sid}/answer",
                    json={"question_id": qid, "chosen": "a"})
    assert r.status_code == 400


def test_submit_calculates_score(client, app, seeded):
    sid = _start_and_get_id(client, seeded)
    with app.app_context():
        es = ExamSession.query.get(sid)
        for qid in es.question_ids[:3]:
            client.post(f"/exam-session/{sid}/answer",
                        json={"question_id": qid, "chosen": "a"})
        client.post(f"/exam-session/{sid}/answer",
                    json={"question_id": es.question_ids[3], "chosen": "b"})

    client.post(f"/exam-session/{sid}/submit")

    with app.app_context():
        es = ExamSession.query.get(sid)
        assert es.score == 3
        assert es.total == 5
        assert es.submitted_at is not None


def test_submit_idempotent(client, app, seeded):
    sid = _start_and_get_id(client, seeded)
    r1 = client.post(f"/exam-session/{sid}/submit")
    r2 = client.post(f"/exam-session/{sid}/submit")
    assert r1.status_code == 302
    assert r2.status_code == 302


def test_results_page_returns_200(client, seeded):
    sid = _start_and_get_id(client, seeded)
    client.post(f"/exam-session/{sid}/submit")
    r = client.get(f"/exam-session/{sid}/results")
    assert r.status_code == 200


def test_results_shows_score(client, seeded, app):
    sid = _start_and_get_id(client, seeded)
    with app.app_context():
        es = ExamSession.query.get(sid)
        for qid in es.question_ids:
            client.post(f"/exam-session/{sid}/answer",
                        json={"question_id": qid, "chosen": "a"})
    client.post(f"/exam-session/{sid}/submit")
    r = client.get(f"/exam-session/{sid}/results")
    assert b"100%" in r.data


def test_results_redirect_if_not_submitted(client, seeded):
    sid = _start_and_get_id(client, seeded)
    r = client.get(f"/exam-session/{sid}/results")
    assert r.status_code == 302
    assert f"/exam-session/{sid}" in r.headers["Location"]
