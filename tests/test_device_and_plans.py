"""Device identity, study-plan ownership and input handling, and the 'GET never writes' rule (with its one documented exception)."""
import hashlib
import json
import re
from datetime import date, datetime, timedelta

import pytest
from bs4 import BeautifulSoup

from app.db import db
from app.models import Chapter, Exam, ExamSession, Question, StudyPlan, UserQuestionState
from app.services import device
from tests.test_exam_and_banks import real  # noqa: F401  (fixture: real content slice + exam tree)

A = "device-A-0123456789abcdef0123456789"
B = "device-B-0123456789abcdef0123456789"


def soup(r):
    return BeautifulSoup(r.get_data(as_text=True), "html.parser")


def client_for(app, dev=None):
    cl = app.test_client()
    if dev:
        cl.set_cookie("device_id", dev)
    return cl


def tok(cl, url="/plan/new"):
    return soup(cl.get(url)).select_one('input[name=csrf_token], meta[name=csrf-token]').get("value") or \
        soup(cl.get(url)).select_one("meta[name=csrf-token]")["content"]


def set_cookie_headers(r):
    return [h for h in r.headers.getlist("Set-Cookie") if h.startswith("device_id=")]


# ── device cookie ────────────────────────────────────────────────────────────────────────────────────
def test_first_visit_gets_a_server_issued_high_entropy_httponly_cookie(app):
    r = app.test_client().get("/learn/")
    (hdr,) = set_cookie_headers(r)
    value = hdr.split(";")[0].split("=", 1)[1]
    assert re.fullmatch(r"[A-Za-z0-9_-]{32}", value)                       # token_urlsafe(24): 192 bits
    assert "HttpOnly" in hdr and "SameSite=Lax" in hdr and "Max-Age=31536000" in hdr


def test_returning_visitor_keeps_the_cookie_and_is_not_reissued(app):
    cl = app.test_client(); cl.get("/learn/")
    assert set_cookie_headers(cl.get("/learn/")) == []


def test_every_new_visitor_gets_a_different_id(app):
    ids = {set_cookie_headers(app.test_client().get("/learn/"))[0].split(";")[0] for _ in range(30)}
    assert len(ids) == 30


@pytest.mark.parametrize("bad", ["anon", "legacy", "dev", "x" * 100, "../../etc/passwd", "a b c d e f g h i j k l m n o p q r s", "d-",
                                 "d-UPPER", "short", "ä" * 40])
def test_malformed_or_chosen_cookie_values_are_replaced(app, bad):
    cl = app.test_client(); cl.set_cookie("device_id", bad)
    r = cl.get("/learn/")
    (hdr,) = set_cookie_headers(r)
    assert hdr.split(";")[0].split("=", 1)[1] != bad and device.valid(hdr.split(";")[0].split("=", 1)[1])


def test_old_client_issued_ids_are_still_honoured_but_never_issued(app):
    cl = app.test_client(); cl.set_cookie("device_id", "d-abc123xyz45k9f")
    assert set_cookie_headers(cl.get("/learn/")) == []
    assert not device.NEW_FORMAT.match("d-abc123xyz45k9f")


def test_static_files_do_not_set_the_cookie(app):
    assert set_cookie_headers(app.test_client().get("/static/app.css")) == []


def test_cookie_is_secure_when_the_app_is_configured_secure(app):
    app.config["SESSION_COOKIE_SECURE"] = True
    (hdr,) = set_cookie_headers(app.test_client().get("/learn/"))
    assert "Secure" in hdr


def test_nothing_is_ever_stored_under_anon(app, real):  # noqa: F811
    cl = app.test_client()
    q = Question.query.filter(Question.chapter_id.isnot(None)).first()
    t = soup(cl.get("/learn/subject/indian_history")).select_one("meta[name=csrf-token]")["content"]
    r = cl.post("/api/answer", data=json.dumps({"question_id": q.id, "chosen": q.correct_answer}),
                content_type="application/json", headers={"X-CSRF-Token": t})
    assert r.status_code == 200
    (row,) = UserQuestionState.query.all()
    assert row.device_id != "anon" and device.NEW_FORMAT.match(row.device_id)


def test_scripts_never_read_or_write_the_device_cookie():
    for js in ("static/app.js", "static/ds.js"):
        text = open(js, encoding="utf-8").read()
        assert "device_id" not in text.replace("HttpOnly cookie issued by the server", "") .replace("device id is an", ""), js
        assert "Math.random" not in text, js


# ── study plans: ownership ───────────────────────────────────────────────────────────────────────────
@pytest.fixture()
def plans(app):
    e = Exam(slug="e1", name_en="E1", name_te="ఇ1", active=True)
    off = Exam(slug="e2", name_en="E2", name_te="ఇ2", active=False)
    db.session.add_all([e, off]); db.session.commit()
    a, b = client_for(app, A), client_for(app, B)
    t = tok(a); a.post("/plan/create", data={"name": "A plan", "csrf_token": t})
    tb = tok(b); b.post("/plan/create", data={"name": "B plan", "csrf_token": tb})
    return {"a": a, "b": b, "exam": e, "inactive": off,
            "pa": StudyPlan.query.filter_by(device_id=A).one(), "pb": StudyPlan.query.filter_by(device_id=B).one()}


@pytest.mark.parametrize("action", ["pause", "resume"])
def test_another_device_cannot_pause_or_resume_my_plan(plans, action):
    b, pa = plans["b"], plans["pa"]
    before = pa.status
    r = b.post(f"/plan/api/{pa.id}/{action}", headers={"X-CSRF-Token": tok(b)})
    assert r.status_code == 404
    db.session.expire_all()
    assert db.session.get(StudyPlan, pa.id).status == before == "active"


def test_foreign_and_nonexistent_plans_look_identical(plans):
    b = plans["b"]
    h = {"X-CSRF-Token": tok(b)}
    assert b.post(f"/plan/api/{plans['pa'].id}/pause", headers=h).status_code == b.post("/plan/api/99999/pause", headers=h).status_code == 404


def test_owner_pause_redirects_form_back_to_the_dashboard(plans):
    a, pa = plans["a"], plans["pa"]
    r = a.post(f"/plan/api/{pa.id}/pause", data={"csrf_token": tok(a)})
    assert r.status_code == 302 and r.headers["Location"].endswith("/plan/")
    db.session.expire_all()
    assert db.session.get(StudyPlan, pa.id).status == "paused"


def test_scripts_can_ask_for_json(plans):
    a, pa = plans["a"], plans["pa"]
    r = a.post(f"/plan/api/{pa.id}/pause", headers={"X-CSRF-Token": tok(a), "Accept": "application/json"})
    assert r.status_code == 200 and r.get_json() == {"status": "paused"}
    r = a.post(f"/plan/api/{pa.id}/resume", headers={"X-CSRF-Token": tok(a), "Accept": "application/json"})
    assert r.get_json() == {"status": "active"}


def test_dashboard_pause_button_works_end_to_end(plans):
    a = plans["a"]
    form = soup(a.get("/plan/")).select_one("form[action*='/pause']")
    assert form and form.select_one("input[name=csrf_token]")
    r = a.post(form["action"], data={"csrf_token": form.select_one("input[name=csrf_token]")["value"]})
    assert r.status_code == 302


def test_resume_leaves_one_active_plan_per_device(plans, app):
    a = plans["a"]
    first = plans["pa"].id
    a.post("/plan/create", data={"name": "second", "csrf_token": tok(a)})
    assert StudyPlan.query.filter_by(device_id=A, status="active").count() == 1
    a.post(f"/plan/api/{first}/resume", data={"csrf_token": tok(a)})
    db.session.expire_all()
    active = StudyPlan.query.filter_by(device_id=A, status="active").all()
    assert [p.id for p in active] == [first]
    assert db.session.get(StudyPlan, plans["pb"].id).status == "active"          # the other device is untouched


def test_dashboards_are_per_device(plans):
    assert "A plan" in plans["a"].get("/plan/").get_data(as_text=True)
    assert "B plan" not in plans["a"].get("/plan/").get_data(as_text=True)


# ── study plans: exam_id handling ────────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("bad", ["abc", "1e3", "-1", "+1", " 1 2", "٣", "١", "99999999999999", "0", "99999", "1;drop"])
def test_bad_exam_id_is_a_friendly_400_and_changes_nothing(plans, bad):
    a = plans["a"]
    before = StudyPlan.query.count()
    r = a.post("/plan/create", data={"name": "x", "exam_id": bad, "csrf_token": tok(a)})
    assert r.status_code == 400
    page = soup(r)
    assert page.select_one(".form-error") and page.select_one("form.plan-form")
    assert StudyPlan.query.count() == before
    assert StudyPlan.query.filter_by(device_id=A, status="active").count() == 1          # existing plan not paused


def test_inactive_exam_is_rejected_and_active_exam_accepted(plans):
    a = plans["a"]
    assert a.post("/plan/create", data={"exam_id": plans["inactive"].id, "csrf_token": tok(a)}).status_code == 400
    assert a.post("/plan/create", data={"exam_id": plans["exam"].id, "csrf_token": tok(a)}).status_code == 302
    assert StudyPlan.query.filter_by(device_id=A, status="active").one().exam_id == plans["exam"].id


def test_empty_exam_means_no_specific_exam_and_long_names_are_trimmed(plans):
    a = plans["a"]
    assert a.post("/plan/create", data={"exam_id": "", "name": "n" * 500, "csrf_token": tok(a)}).status_code == 302
    p = StudyPlan.query.filter_by(device_id=A, status="active").one()
    assert p.exam_id is None and len(p.name) == 128


def test_wizard_keeps_the_name_the_user_typed_after_an_error(plans):
    a = plans["a"]
    r = a.post("/plan/create", data={"name": "My own name", "exam_id": "zzz", "csrf_token": tok(a)})
    assert 'value="My own name"' in r.get_data(as_text=True)


# ── GET does not write, with one documented exception ────────────────────────────────────────────────
def db_fingerprint():
    h = hashlib.sha256()
    for table in db.metadata.sorted_tables:
        rows = db.session.execute(table.select()).fetchall()
        h.update(table.name.encode()); h.update(str(len(rows)).encode())
        h.update(repr(sorted(map(repr, rows))).encode())
    return h.hexdigest()


def fill_get(rule):
    vals = {}
    for arg, conv in rule._converters.items():
        vals[arg] = 1 if conv.__class__.__name__ == "IntegerConverter" else (
            "11111111-1111-4111-8111-111111111111" if arg == "session_id" else ("pyq" if arg == "bank" else "indian_history"))
    return rule.build(vals)[1]


def test_no_get_request_changes_the_database(app, real):  # noqa: F811
    """Every GET route, with plausible ids, on a live (unexpired) data set. The only GET writes are the lazy finalisation of
    an *expired* exam session in `take` / `results`; see the next test."""
    cl = app.test_client()
    es = ExamSession(id="22222222-2222-4222-8222-222222222222", device_id=A, config={"duration_min": 60},
                     question_ids=[Question.query.first().id], answers={}, confidences={}, started_at=datetime.utcnow())
    db.session.add(es); db.session.commit()
    urls = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and rule.endpoint != "static" and not rule.rule.startswith("/admin"):
            urls.append(fill_get(rule) if rule._converters else rule.rule)
    urls += ["/learn/subject/ap_history/pyq?i=1", "/learn/subject/indian_history/practice?i=1&new=1", "/exam-session/" + es.id,
             "/exam-session/" + es.id + "/results", "/practice/indian_history?i=3", "/plan/", "/plan/new"]
    before = db_fingerprint()
    for u in urls:
        assert app.test_client().get(u).status_code < 500, u
    cl2 = app.test_client()
    for u in urls:
        cl2.get(u)
    db.session.expire_all()
    assert db_fingerprint() == before, "a GET request wrote to the database"


def test_documented_exception_expired_exam_take_and_results_finalise_idempotently(app, real):  # noqa: F811
    q = Question.query.first()
    es = ExamSession(id="33333333-3333-4333-8333-333333333333", device_id=A, config={"duration_min": 5},
                     question_ids=[q.id], answers={str(q.id): q.correct_answer}, confidences={},
                     started_at=datetime.utcnow() - timedelta(hours=2))
    db.session.add(es); db.session.commit()
    cl = app.test_client()
    assert cl.get(f"/exam-session/{es.id}").status_code == 302                  # take: closes the expired session
    db.session.expire_all()
    first = db.session.get(ExamSession, es.id)
    stamp, score = first.submitted_at, first.score
    assert stamp == first.started_at + timedelta(minutes=5) and score == 1
    assert cl.get(f"/exam-session/{es.id}/results").status_code == 200          # results: no further change
    cl.get(f"/exam-session/{es.id}")
    db.session.expire_all()
    again = db.session.get(ExamSession, es.id)
    assert (again.submitted_at, again.score) == (stamp, score)
