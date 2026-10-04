"""Content import safety: preview writes nothing; default apply never alters or deletes existing notes;
scoping, transactionality, backup/restore, confirmation, stale-preview refusal, auth/CSRF."""
import hashlib
import json
import sqlite3

import pytest

from app.db import db
from app.models import Chapter, Note, NoteBackup, Question, Subject
from app.services import content_import as ci

SRC_SCHEMA = """
CREATE TABLE subjects(id INTEGER PRIMARY KEY, slug TEXT, name_en TEXT, name_te TEXT, sort_order INT);
CREATE TABLE chapters(id INTEGER PRIMARY KEY, subject_id INT, chapter_num INT, title_en TEXT, title_te TEXT, est_read_minutes INT);
CREATE TABLE notes(id INTEGER PRIMARY KEY, chapter_id INT, section_num INT, heading_en TEXT, heading_te TEXT, body_en TEXT, body_te TEXT);
CREATE TABLE questions(id INTEGER PRIMARY KEY, subject_id INT, chapter_id INT, source_type TEXT, difficulty TEXT,
  question_en TEXT, question_te TEXT, options_en TEXT, options_te TEXT, correct_answer TEXT,
  explanation_en TEXT, explanation_te TEXT, pyq_year TEXT, pyq_paper TEXT);
"""


@pytest.fixture()
def source(tmp_path):
    p = tmp_path / "content.db"
    c = sqlite3.connect(p)
    c.executescript(SRC_SCHEMA)
    c.executemany("INSERT INTO subjects VALUES(?,?,?,?,?)", [(1, "hist", "History", "చరిత్ర", 1), (2, "poly", "Polity", "రాజ్యాంగం", 2)])
    c.executemany("INSERT INTO chapters VALUES(?,?,?,?,?,?)", [(1, 1, 1, "Ancient", "ప్రాచీన", 10), (2, 2, 1, "Preamble", "ప్రవేశిక", 10)])
    c.executemany("INSERT INTO notes VALUES(?,?,?,?,?,?,?)", [
        (1, 1, 1, "H1", "", "<p>source hist 1</p>", ""), (2, 1, 2, "H2", "", "<p>source hist 2</p>", ""),
        (3, 2, 1, "P1", "", "<p>source polity 1</p>", "")])
    c.execute("INSERT INTO questions VALUES(1,1,1,'chapter','M','Who?','',?,?, 'a','','', NULL, NULL)",
              (json.dumps({"a": "x", "b": "y"}), "{}"))
    c.commit(); c.close()
    return p


def _open(source):
    return ci.open_source(source)


def _seed_live():
    h = Subject(slug="hist", name_en="History", name_te="చరిత్ర", sort_order=1)
    p = Subject(slug="poly", name_en="Polity", name_te="రాజ్యాంగం", sort_order=2)
    z = Subject(slug="other", name_en="Other", name_te="ఇతర", sort_order=3)
    db.session.add_all([h, p, z]); db.session.flush()
    hc = Chapter(subject_id=h.id, chapter_num=1, title_en="Ancient", title_te="ప్రాచీన")
    pc = Chapter(subject_id=p.id, chapter_num=1, title_en="Preamble", title_te="ప్రవేశిక")
    zc = Chapter(subject_id=z.id, chapter_num=1, title_en="Z", title_te="Z")
    db.session.add_all([hc, pc, zc]); db.session.flush()
    db.session.add_all([
        Note(chapter_id=hc.id, section_num=1, heading_en="H1", heading_te="", body_en="<p>EDITED BY HAND</p>", body_te=""),
        Note(chapter_id=hc.id, section_num=9, heading_en="Mine", heading_te="", body_en="<p>my own section</p>", body_te=""),
        Note(chapter_id=pc.id, section_num=1, heading_en="P1", heading_te="", body_en="<p>source polity 1</p>", body_te=""),
        Note(chapter_id=zc.id, section_num=1, heading_en="Z", heading_te="", body_en="<p>unrelated</p>", body_te="")])
    db.session.commit()
    return hc.id, pc.id, zc.id


def _snapshot():
    return sorted((n.chapter_id, n.section_num, n.heading_en, n.body_en) for n in Note.query.all())


def _plan(source):
    src, sha = _open(source)
    return src, sha, ci.build_plan(src, sha)


def test_preview_writes_nothing(app, source):
    _seed_live(); before = _snapshot(); counts = (Subject.query.count(), Chapter.query.count(), Question.query.count())
    src, sha, plan = _plan(source)
    assert not db.session.new and not db.session.dirty
    assert _snapshot() == before and (Subject.query.count(), Chapter.query.count(), Question.query.count()) == counts
    hist = next(s for s in plan["subjects"] if s["slug"] == "hist")
    assert hist["notes"] == {"source": 2, "add": 1, "same": 0, "differ": 1, "extra_live": 1}


def test_default_apply_keeps_every_existing_note_and_adds_missing(app, source):
    hc, pc, zc = _seed_live(); before = set(_snapshot())
    src, sha, plan = _plan(source)
    res = ci.apply_import(src, sha, ["hist"], plan["fingerprint"])
    after = set(_snapshot())
    assert before <= after                                   # nothing deleted or altered
    assert after - before == {(hc, 2, "H2", "<p>source hist 2</p>")}
    assert res["added"]["notes"] == 1 and res["notes_kept_differing"] == 1 and res["notes_replaced"] == 0 and res["notes_removed"] == 0
    assert Note.query.filter_by(chapter_id=hc, section_num=1).one().body_en == "<p>EDITED BY HAND</p>"
    assert NoteBackup.query.count() == 0


def test_unselected_subject_is_untouched(app, source):
    _seed_live()
    src, sha, plan = _plan(source)
    ci.apply_import(src, sha, ["hist"], plan["fingerprint"], replace_notes=True, remove_extra=True)
    assert Note.query.filter(Note.body_en == "<p>unrelated</p>").count() == 1
    assert Note.query.filter(Note.body_en == "<p>source polity 1</p>").count() == 1
    assert Note.query.count() == 4 + 1 - 1                    # hist: +1 added, -1 removed (section 9)


def test_unrelated_subject_survives_even_if_all_subjects_selected(app, source):
    _seed_live()
    src, sha, plan = _plan(source)
    ci.apply_import(src, sha, ["hist", "poly"], plan["fingerprint"], replace_notes=True, remove_extra=True)
    assert Note.query.filter(Note.body_en == "<p>unrelated</p>").count() == 1   # 'other' is not in the source


def test_replace_backs_up_and_restore_brings_back(app, source):
    hc, pc, zc = _seed_live()
    src, sha, plan = _plan(source)
    res = ci.apply_import(src, sha, ["hist"], plan["fingerprint"], replace_notes=True)
    assert res["notes_replaced"] == 1
    assert Note.query.filter_by(chapter_id=hc, section_num=1).one().body_en == "<p>source hist 1</p>"
    bak = NoteBackup.query.filter_by(batch_id=res["batch_id"]).one()
    assert bak.reason == "replaced" and bak.body_en == "<p>EDITED BY HAND</p>"
    out = ci.restore_batch(res["batch_id"])
    assert out["restored"] == 1
    assert Note.query.filter_by(chapter_id=hc, section_num=1).one().body_en == "<p>EDITED BY HAND</p>"
    # the restore itself is undoable
    ci.restore_batch(out["batch_id"])
    assert Note.query.filter_by(chapter_id=hc, section_num=1).one().body_en == "<p>source hist 1</p>"


def test_remove_extra_is_opt_in_scoped_and_restorable(app, source):
    hc, pc, zc = _seed_live()
    src, sha, plan = _plan(source)
    res = ci.apply_import(src, sha, ["hist"], plan["fingerprint"], remove_extra=True)
    assert res["notes_removed"] == 1
    assert Note.query.filter_by(chapter_id=hc, section_num=9).count() == 0
    assert Note.query.filter_by(chapter_id=hc, section_num=1).one().body_en == "<p>EDITED BY HAND</p>"   # not replaced
    ci.restore_batch(res["batch_id"])
    assert Note.query.filter_by(chapter_id=hc, section_num=9).one().body_en == "<p>my own section</p>"


def test_failure_mid_import_rolls_everything_back(app, source, monkeypatch):
    _seed_live(); before = _snapshot(); q = Question.query.count(); ch = Chapter.query.count()
    src, sha, plan = _plan(source)

    def boom(_v):                                             # first used when inserting questions, after notes changed
        raise RuntimeError("injected")
    monkeypatch.setattr(ci, "_j", boom)
    with pytest.raises(RuntimeError):
        ci.apply_import(src, sha, ["hist"], plan["fingerprint"], replace_notes=True, remove_extra=True)
    assert _snapshot() == before and Question.query.count() == q and Chapter.query.count() == ch
    assert NoteBackup.query.count() == 0


def test_stale_fingerprint_is_refused(app, source):
    hc, pc, zc = _seed_live()
    src, sha, plan = _plan(source)
    n = Note.query.filter_by(chapter_id=hc, section_num=1).one(); n.body_en = "<p>edited again after preview</p>"; db.session.commit()
    with pytest.raises(ci.ContentImportError):
        ci.apply_import(src, sha, ["hist"], plan["fingerprint"], replace_notes=True)
    assert Note.query.filter_by(chapter_id=hc, section_num=1).one().body_en == "<p>edited again after preview</p>"


def test_requires_a_subject_and_rejects_unknown(app, source):
    _seed_live(); src, sha, plan = _plan(source)
    for bad in ([], ["nope"]):
        with pytest.raises(ci.ContentImportError):
            ci.apply_import(src, sha, bad, plan["fingerprint"])


def test_json_options_stored_as_objects_not_strings(app, source):
    src, sha, plan = _plan(source)
    ci.apply_import(src, sha, ["hist"], plan["fingerprint"])
    q = Question.query.one()
    assert q.options_en == {"a": "x", "b": "y"} and q.options_te == {}


def test_import_is_idempotent(app, source):
    src, sha, plan = _plan(source)
    ci.apply_import(src, sha, ["hist", "poly"], plan["fingerprint"])
    snap = _snapshot(); qn = Question.query.count()
    plan2 = ci.build_plan(src, sha)
    res = ci.apply_import(src, sha, ["hist", "poly"], plan2["fingerprint"])
    assert res["added"] == {"subjects": 0, "chapters": 0, "notes": 0, "questions": 0}
    assert _snapshot() == snap and Question.query.count() == qn


# ── routes ─────────────────────────────────────────────────────────
def _admin(client):
    with client.session_transaction() as s:
        s["admin_token"] = hashlib.sha256(b"admin:1234").hexdigest(); s["_csrf"] = "t"


def _post(client, url, **data):
    return client.post(url, data={"csrf_token": "t", **data})


@pytest.fixture()
def admin_client(app, client, source):
    app.config["CONTENT_SOURCE"] = str(source)
    _admin(client)
    return client


def test_routes_require_login(app, client, source):
    app.config["CONTENT_SOURCE"] = str(source)
    for url in ("/admin/load-content/preview", "/admin/load-content/apply", "/admin/load-content/restore"):
        r = client.post(url, data={"csrf_token": "x"})
        assert r.status_code in (302, 400), url               # never 200
    with client.session_transaction() as s:
        s["_csrf"] = "t"
    for url in ("/admin/load-content/preview", "/admin/load-content/apply", "/admin/load-content/restore"):
        assert client.post(url, data={"csrf_token": "t"}).status_code == 302


def test_routes_require_csrf(admin_client):
    for url in ("/admin/load-content/preview", "/admin/load-content/apply", "/admin/load-content/restore"):
        assert admin_client.post(url, data={}).status_code == 400


def test_old_streaming_post_is_gone(admin_client):
    assert admin_client.post("/admin/load-content", data={"csrf_token": "t"}).status_code == 405


def test_preview_route_writes_nothing_and_preselects_nothing(app, admin_client):
    _seed_live(); before = _snapshot()
    r = _post(admin_client, "/admin/load-content/preview")
    html = r.get_data(as_text=True)
    assert r.status_code == 200 and "Nothing has been changed" in html
    assert 'name="subjects"' in html and "checked" not in html
    assert _snapshot() == before


def test_apply_route_default_preserves_notes(app, admin_client, source):
    hc, pc, zc = _seed_live(); before = set(_snapshot())
    fp = _plan(source)[2]["fingerprint"]
    r = _post(admin_client, "/admin/load-content/apply", subjects="hist", fingerprint=fp)
    assert r.status_code == 200
    assert before <= set(_snapshot())


def test_apply_route_replace_needs_confirm_phrase(app, admin_client, source):
    hc, pc, zc = _seed_live(); before = _snapshot(); fp = _plan(source)[2]["fingerprint"]
    for confirm in ("", "yes", "replace "[:-1].lower()):
        r = _post(admin_client, "/admin/load-content/apply", subjects="hist", fingerprint=fp, replace_notes="1", confirm=confirm)
        assert r.status_code == 400
    assert _snapshot() == before
    r = _post(admin_client, "/admin/load-content/apply", subjects="hist", fingerprint=fp, replace_notes="1", confirm="REPLACE")
    assert r.status_code == 200
    assert Note.query.filter_by(chapter_id=hc, section_num=1).one().body_en == "<p>source hist 1</p>"
    assert NoteBackup.query.count() == 1


def test_apply_route_without_subject_changes_nothing(app, admin_client, source):
    _seed_live(); before = _snapshot(); fp = _plan(source)[2]["fingerprint"]
    assert _post(admin_client, "/admin/load-content/apply", fingerprint=fp).status_code == 400
    assert _snapshot() == before


def test_restore_route_needs_confirm_phrase(app, admin_client, source):
    hc, pc, zc = _seed_live(); src, sha, plan = _plan(source)
    res = ci.apply_import(src, sha, ["hist"], plan["fingerprint"], replace_notes=True)
    assert _post(admin_client, "/admin/load-content/restore", batch_id=res["batch_id"], confirm="no").status_code == 400
    assert Note.query.filter_by(chapter_id=hc, section_num=1).one().body_en == "<p>source hist 1</p>"
    assert _post(admin_client, "/admin/load-content/restore", batch_id=res["batch_id"], confirm="RESTORE").status_code == 200
    assert Note.query.filter_by(chapter_id=hc, section_num=1).one().body_en == "<p>EDITED BY HAND</p>"


def test_page_lists_backup_batches(app, admin_client, source):
    _seed_live(); src, sha, plan = _plan(source)
    res = ci.apply_import(src, sha, ["hist"], plan["fingerprint"], replace_notes=True)
    assert res["batch_id"] in admin_client.get("/admin/load-content").get_data(as_text=True)


def test_no_global_note_delete_anywhere():
    import pathlib, re
    root = pathlib.Path(__file__).resolve().parent.parent
    pat = re.compile(r"Note\.query\.delete\(\)|DELETE\s+FROM\s+notes\b", re.I)
    offenders = [str(p.relative_to(root)) for p in list((root / "app").rglob("*.py")) + list((root / "scripts").rglob("load_content.py"))
                 if pat.search(p.read_text(encoding="utf-8", errors="ignore"))]
    assert offenders == []
