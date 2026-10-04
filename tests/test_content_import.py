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


@pytest.fixture(autouse=True)
def _close_sources():
    yield
    for s in _OPEN:
        s.close()
    _OPEN.clear()


_OPEN = []


def _plan(source):
    src = ci.open_source(source); _OPEN.append(src)
    return src, ci.build_plan(src)


def test_preview_writes_nothing(app, source):
    _seed_live(); before = _snapshot(); counts = (Subject.query.count(), Chapter.query.count(), Question.query.count())
    src, plan = _plan(source)
    assert not db.session.new and not db.session.dirty
    assert _snapshot() == before and (Subject.query.count(), Chapter.query.count(), Question.query.count()) == counts
    hist = next(s for s in plan["subjects"] if s["slug"] == "hist")
    assert hist["notes"] == {"source": 2, "add": 1, "same": 0, "differ": 1, "extra_live": 1}


def test_default_apply_keeps_every_existing_note_and_adds_missing(app, source):
    hc, pc, zc = _seed_live(); before = set(_snapshot())
    src, plan = _plan(source)
    res = ci.apply_import(src, ["hist"], plan["fingerprints"])
    after = set(_snapshot())
    assert before <= after                                   # nothing deleted or altered
    assert after - before == {(hc, 2, "H2", "<p>source hist 2</p>")}
    assert res["added"]["notes"] == 1 and res["notes_kept_differing"] == 1 and res["notes_replaced"] == 0 and res["notes_removed"] == 0
    assert Note.query.filter_by(chapter_id=hc, section_num=1).one().body_en == "<p>EDITED BY HAND</p>"
    assert NoteBackup.query.count() == 0


def test_unselected_subject_is_untouched(app, source):
    _seed_live()
    src, plan = _plan(source)
    ci.apply_import(src, ["hist"], plan["fingerprints"], replace_notes=True, remove_extra=True)
    assert Note.query.filter(Note.body_en == "<p>unrelated</p>").count() == 1
    assert Note.query.filter(Note.body_en == "<p>source polity 1</p>").count() == 1
    assert Note.query.count() == 4 + 1 - 1                    # hist: +1 added, -1 removed (section 9)


def test_unrelated_subject_survives_even_if_all_subjects_selected(app, source):
    _seed_live()
    src, plan = _plan(source)
    ci.apply_import(src, ["hist", "poly"], plan["fingerprints"], replace_notes=True, remove_extra=True)
    assert Note.query.filter(Note.body_en == "<p>unrelated</p>").count() == 1   # 'other' is not in the source


def test_replace_backs_up_and_restore_brings_back(app, source):
    hc, pc, zc = _seed_live()
    src, plan = _plan(source)
    res = ci.apply_import(src, ["hist"], plan["fingerprints"], replace_notes=True)
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
    src, plan = _plan(source)
    res = ci.apply_import(src, ["hist"], plan["fingerprints"], remove_extra=True)
    assert res["notes_removed"] == 1
    assert Note.query.filter_by(chapter_id=hc, section_num=9).count() == 0
    assert Note.query.filter_by(chapter_id=hc, section_num=1).one().body_en == "<p>EDITED BY HAND</p>"   # not replaced
    ci.restore_batch(res["batch_id"])
    assert Note.query.filter_by(chapter_id=hc, section_num=9).one().body_en == "<p>my own section</p>"


def test_failure_mid_import_rolls_everything_back(app, source, monkeypatch):
    _seed_live(); before = _snapshot(); q = Question.query.count(); ch = Chapter.query.count()
    src, plan = _plan(source)

    def boom(_v):                                             # first used when inserting questions, after notes changed
        raise RuntimeError("injected")
    monkeypatch.setattr(ci, "_j", boom)
    with pytest.raises(RuntimeError):
        ci.apply_import(src, ["hist"], plan["fingerprints"], replace_notes=True, remove_extra=True)
    assert _snapshot() == before and Question.query.count() == q and Chapter.query.count() == ch
    assert NoteBackup.query.count() == 0


def test_stale_fingerprint_is_refused(app, source):
    hc, pc, zc = _seed_live()
    src, plan = _plan(source)
    n = Note.query.filter_by(chapter_id=hc, section_num=1).one(); n.body_en = "<p>edited again after preview</p>"; db.session.commit()
    with pytest.raises(ci.ContentImportError):
        ci.apply_import(src, ["hist"], plan["fingerprints"], replace_notes=True)
    assert Note.query.filter_by(chapter_id=hc, section_num=1).one().body_en == "<p>edited again after preview</p>"


def test_requires_a_subject_and_rejects_unknown(app, source):
    _seed_live(); src, plan = _plan(source)
    for bad in ([], ["nope"]):
        with pytest.raises(ci.ContentImportError):
            ci.apply_import(src, bad, plan["fingerprints"])


def test_json_options_stored_as_objects_not_strings(app, source):
    src, plan = _plan(source)
    ci.apply_import(src, ["hist"], plan["fingerprints"])
    q = Question.query.one()
    assert q.options_en == {"a": "x", "b": "y"} and q.options_te == {}


def test_import_is_idempotent(app, source):
    src, plan = _plan(source)
    ci.apply_import(src, ["hist", "poly"], plan["fingerprints"])
    snap = _snapshot(); qn = Question.query.count()
    plan2 = ci.build_plan(src)
    res = ci.apply_import(src, ["hist", "poly"], plan2["fingerprints"])
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
    fp = _plan(source)[1]["fingerprints"]["hist"]
    r = _post(admin_client, "/admin/load-content/apply", subjects="hist", **{"fp.hist": fp})
    assert r.status_code == 200
    assert before <= set(_snapshot())


def test_apply_route_replace_needs_confirm_phrase(app, admin_client, source):
    hc, pc, zc = _seed_live(); before = _snapshot(); fp = _plan(source)[1]["fingerprints"]["hist"]
    for confirm in ("", "yes", "replace "[:-1].lower()):
        r = _post(admin_client, "/admin/load-content/apply", subjects="hist", **{"fp.hist": fp}, replace_notes="1", confirm=confirm)
        assert r.status_code == 400
    assert _snapshot() == before
    r = _post(admin_client, "/admin/load-content/apply", subjects="hist", **{"fp.hist": fp}, replace_notes="1", confirm="REPLACE")
    assert r.status_code == 200
    assert Note.query.filter_by(chapter_id=hc, section_num=1).one().body_en == "<p>source hist 1</p>"
    assert NoteBackup.query.count() == 1


def test_apply_route_without_subject_changes_nothing(app, admin_client, source):
    _seed_live(); before = _snapshot(); fp = _plan(source)[1]["fingerprints"]["hist"]
    assert _post(admin_client, "/admin/load-content/apply", **{"fp.hist": fp}).status_code == 400
    assert _snapshot() == before


def test_restore_route_needs_confirm_phrase(app, admin_client, source):
    hc, pc, zc = _seed_live(); src, plan = _plan(source)
    res = ci.apply_import(src, ["hist"], plan["fingerprints"], replace_notes=True)
    assert _post(admin_client, "/admin/load-content/restore", batch_id=res["batch_id"], confirm="no").status_code == 400
    assert Note.query.filter_by(chapter_id=hc, section_num=1).one().body_en == "<p>source hist 1</p>"
    assert _post(admin_client, "/admin/load-content/restore", batch_id=res["batch_id"], confirm="RESTORE").status_code == 200
    assert Note.query.filter_by(chapter_id=hc, section_num=1).one().body_en == "<p>EDITED BY HAND</p>"


def test_page_lists_backup_batches(app, admin_client, source):
    _seed_live(); src, plan = _plan(source)
    res = ci.apply_import(src, ["hist"], plan["fingerprints"], replace_notes=True)
    assert res["batch_id"] in admin_client.get("/admin/load-content").get_data(as_text=True)


def test_no_global_note_delete_anywhere():
    import pathlib, re
    root = pathlib.Path(__file__).resolve().parent.parent
    pat = re.compile(r"Note\.query\.delete\(\)|DELETE\s+FROM\s+notes\b", re.I)
    offenders = [str(p.relative_to(root)) for p in list((root / "app").rglob("*.py")) + [root / "scripts" / "load_content.py", root / "scripts" / "parse_ap_history_notes.py"]
                 if pat.search(p.read_text(encoding="utf-8", errors="ignore"))]
    assert offenders == []


# ══ follow-up: dedup keeps distinct questions ═════════════════════════════════
def _mk_source(tmp_path, questions, name="q.db"):
    p = tmp_path / name
    c = sqlite3.connect(p); c.executescript(SRC_SCHEMA)
    c.execute("INSERT INTO subjects VALUES(1,'hist','History','',1)")
    c.execute("INSERT INTO subjects VALUES(2,'poly','Polity','',2)")
    c.execute("INSERT INTO chapters VALUES(1,1,1,'A','A',10)")
    for i, q in enumerate(questions, 1):
        c.execute("INSERT INTO questions VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                  (i, q.get("subject", 1), 1, q.get("type", "chapter"), "M", q["q"], "", json.dumps(q.get("opts", {"a": "x", "b": "y"})),
                   "{}", q.get("ans", "a"), "", "", q.get("year"), q.get("paper")))
    c.commit(); c.close()
    return p


STEM = "Which of the following statements about the Satavahanas is correct? " * 3          # > 120 chars, shared stem


def test_questions_sharing_a_long_stem_are_all_kept(app, tmp_path):
    p = _mk_source(tmp_path, [{"q": STEM, "opts": {"a": "one", "b": "two"}}, {"q": STEM, "opts": {"a": "three", "b": "four"}},
                              {"q": STEM, "opts": {"a": "one", "b": "two"}, "ans": "b"}])
    src, plan = _plan(p)
    assert plan["subjects"][0]["questions"] == {"source": 3, "add": 3, "duplicate": 0}
    res = ci.apply_import(src, ["hist"], plan["fingerprints"])
    assert res["added"]["questions"] == 3 and Question.query.count() == 3


def test_same_question_in_two_subjects_and_two_pyq_years_are_distinct(app, tmp_path):
    p = _mk_source(tmp_path, [{"q": "Q?", "subject": 1}, {"q": "Q?", "subject": 2},
                              {"q": "P?", "type": "pyq", "year": "2018", "paper": "G2"}, {"q": "P?", "type": "pyq", "year": "2020", "paper": "G2"}])
    src, plan = _plan(p)
    ci.apply_import(src, ["hist", "poly"], plan["fingerprints"])
    assert Question.query.count() == 4


def test_exact_duplicates_are_skipped_in_source_and_on_rerun(app, tmp_path):
    p = _mk_source(tmp_path, [{"q": "Same?"}, {"q": "Same?"}, {"q": " Same? "}])
    src, plan = _plan(p)
    assert plan["subjects"][0]["questions"] == {"source": 3, "add": 1, "duplicate": 2}
    ci.apply_import(src, ["hist"], plan["fingerprints"])
    assert Question.query.count() == 1
    plan2 = ci.build_plan(src)
    assert plan2["subjects"][0]["questions"]["add"] == 0


def test_preview_counts_match_what_apply_adds(app, tmp_path):
    p = _mk_source(tmp_path, [{"q": STEM, "opts": {"a": str(i)}} for i in range(5)] + [{"q": "dup"}, {"q": "dup"}])
    src, plan = _plan(p)
    want = plan["subjects"][0]["questions"]["add"]
    assert ci.apply_import(src, ["hist"], plan["fingerprints"])["added"]["questions"] == want == 6


# ══ follow-up: stale-preview protection covers everything the apply reads ═════
def _stale_after(app, source, mutate):
    hc, pc, zc = _seed_live(); before = _snapshot(); qn = Question.query.count()
    src, plan = _plan(source)
    mutate(hc)
    db.session.commit()
    mid = (_snapshot(), Question.query.count())
    with pytest.raises(ci.ContentImportError):
        ci.apply_import(src, ["hist"], plan["fingerprints"], replace_notes=True, remove_extra=True)
    assert (_snapshot(), Question.query.count()) == mid and NoteBackup.query.count() == 0     # nothing changed by the refused apply


def test_stale_when_extra_live_note_added(app, source):
    _stale_after(app, source, lambda hc: db.session.add(Note(chapter_id=hc, section_num=20, heading_en="new", body_en="x")))


def test_stale_when_extra_live_note_edited(app, source):
    def m(hc):
        Note.query.filter_by(chapter_id=hc, section_num=9).one().body_en = "<p>edited after preview</p>"
    _stale_after(app, source, m)


def test_stale_when_extra_live_note_deleted(app, source):
    _stale_after(app, source, lambda hc: db.session.delete(Note.query.filter_by(chapter_id=hc, section_num=9).one()))


def test_stale_when_chapter_added(app, source):
    def m(hc):
        sid = Chapter.query.get(hc).subject_id
        db.session.add(Chapter(subject_id=sid, chapter_num=7, title_en="late", title_te="late"))
    _stale_after(app, source, m)


def test_stale_when_live_question_added(app, source):
    def m(hc):
        sid = Chapter.query.get(hc).subject_id
        db.session.add(Question(subject_id=sid, source_type="chapter", question_en="added live", correct_answer="a", options_en={}))
    _stale_after(app, source, m)


def test_stale_when_source_file_changes(app, source):
    _seed_live(); src, plan = _plan(source)
    c = sqlite3.connect(source); c.execute("INSERT INTO notes VALUES(99,1,5,'new','','b','')"); c.commit(); c.close()
    src2 = ci.open_source(source); _OPEN.append(src2)
    with pytest.raises(ci.ContentImportError):
        ci.apply_import(src2, ["hist"], plan["fingerprints"])


def test_change_in_unselected_subject_does_not_block_import(app, source):
    hc, pc, zc = _seed_live(); src, plan = _plan(source)
    Note.query.filter_by(chapter_id=pc).one().body_en = "<p>polity changed</p>"; db.session.commit()
    ci.apply_import(src, ["hist"], plan["fingerprints"])             # polity not selected: still fine
    assert Note.query.filter_by(chapter_id=pc).one().body_en == "<p>polity changed</p>"


# ══ follow-up: the write lock ═════════════════════════════════════════════════
def test_sqlite_lock_blocks_a_concurrent_writer_until_rollback(tmp_path):
    from app import create_app
    from app.config import Config

    class C(Config):
        TESTING = True; SECRET_KEY = "t"; SQLALCHEMY_DATABASE_URI = f"sqlite:///{(tmp_path / 'live.db').as_posix()}"
    app = create_app(C)
    with app.app_context():
        db.create_all()
        db.session.add_all([Subject(slug="s", name_en="S", name_te="S")]); db.session.commit()
        ci.lock_for_import()
        other = sqlite3.connect(tmp_path / "live.db", timeout=0.2)
        with pytest.raises(sqlite3.OperationalError, match="locked"):
            other.execute("UPDATE subjects SET name_en='race'"); other.commit()
        db.session.rollback()
        other.execute("UPDATE subjects SET name_en='after'"); other.commit(); other.close()
        db.session.remove(); db.drop_all()


def test_postgres_lock_blocks_a_concurrent_writer():
    import os
    url = os.environ.get("TEST_PG_URL")
    if not url:
        pytest.skip("TEST_PG_URL not set")
    import sqlalchemy as sa
    from app import create_app
    from app.config import Config

    class C(Config):
        TESTING = True; SECRET_KEY = "t"; SQLALCHEMY_DATABASE_URI = url
    app = create_app(C)
    with app.app_context():
        db.drop_all(); db.create_all()
        try:
            db.session.add(Subject(slug="s", name_en="S", name_te="S")); db.session.commit()
            ci.lock_for_import()
            eng = sa.create_engine(url)
            with eng.connect() as c2:
                c2.execute(sa.text("SET lock_timeout = '300ms'"))
                with pytest.raises(sa.exc.OperationalError, match="lock timeout|canceling statement"):
                    c2.execute(sa.text("UPDATE subjects SET name_en='race'"))
                c2.rollback()
            db.session.rollback()
            with eng.begin() as c3:
                c3.execute(sa.text("UPDATE subjects SET name_en='after'"))
            eng.dispose()
        finally:
            db.session.remove(); db.drop_all()


def test_refusal_after_lock_releases_the_lock(tmp_path):
    from app import create_app
    from app.config import Config

    class C(Config):
        TESTING = True; SECRET_KEY = "t"; SQLALCHEMY_DATABASE_URI = f"sqlite:///{(tmp_path / 'live2.db').as_posix()}"
    app = create_app(C)
    with app.app_context():
        db.create_all()
        p = _mk_source(tmp_path, [{"q": "x"}])
        src = ci.open_source(p)
        with pytest.raises(ci.ContentImportError):
            ci.apply_import(src, ["hist"], {"hist": "stale"})
        src.close()
        other = sqlite3.connect(tmp_path / "live2.db", timeout=0.2)
        other.execute("INSERT INTO subjects(slug,name_en,name_te) VALUES('z','z','z')"); other.commit(); other.close()
        db.session.remove(); db.drop_all()


# ══ follow-up: cleanup ════════════════════════════════════════════════════════
def test_gz_source_temp_dir_is_removed_on_close(tmp_path):
    import gzip, os, shutil
    p = _mk_source(tmp_path, [{"q": "x"}], "plain.db")
    target = tmp_path / "gzcopy.db"
    with open(p, "rb") as fi, gzip.open(str(target) + ".gz", "wb") as fo:
        shutil.copyfileobj(fi, fo)
    src = ci.open_source(target)
    tmp = src._tmpdir
    assert tmp and os.path.isdir(tmp)
    src.close()
    assert not os.path.exists(tmp)


# ══ follow-up: AP History goes through the same flow ═════════════════════════
CHAPTER_HTML = """<html><head><title>x</title></head><body><h1>— {title}</h1>
<section class="section"><h2>1. {h1}</h2><p>{b1}</p></section>
<section class="section"><h2>2. Second</h2><p>{b2}</p></section></body></html>"""


@pytest.fixture()
def ap_dir(tmp_path):
    d = tmp_path / "chapters"; d.mkdir()
    (d / "ch01_prehistoric_cultures.html").write_text(CHAPTER_HTML.format(title="Prehistoric", h1="Stone age", b1="parsed one", b2="parsed two"), encoding="utf-8")
    (d / "ch02_andhrula_parichayam_aadharalu.html").write_text(CHAPTER_HTML.format(title="Andhras", h1="Intro", b1="two one", b2="two two"), encoding="utf-8")
    return d


def _seed_ap():
    s = Subject(slug="ap_history", name_en="AP History", name_te="ఏపీ చరిత్ర", sort_order=5)
    o = Subject(slug="indian_history", name_en="Indian History", name_te="భారత చరిత్ర", sort_order=1)
    db.session.add_all([s, o]); db.session.flush()
    c1 = Chapter(subject_id=s.id, chapter_num=1, title_en="Mine", title_te="Mine")
    c99 = Chapter(subject_id=s.id, chapter_num=99, title_en="Extra chapter", title_te="Extra")
    oc = Chapter(subject_id=o.id, chapter_num=1, title_en="O", title_te="O")
    db.session.add_all([c1, c99, oc]); db.session.flush()
    db.session.add_all([Note(chapter_id=c1.id, section_num=1, heading_en="Hand", body_en="<p>HAND EDITED</p>"),
                        Note(chapter_id=c99.id, section_num=1, heading_en="keep", body_en="<p>chapter 99 note</p>"),
                        Note(chapter_id=oc.id, section_num=1, heading_en="o", body_en="<p>other subject</p>")])
    db.session.commit()
    return c1.id, c99.id, oc.id


def test_ap_history_default_import_preserves_existing_chapters_and_notes(app, ap_dir):
    from app.services import ap_history_parse
    c1, c99, oc = _seed_ap(); before = set(_snapshot())
    with ap_history_parse.build_source(str(ap_dir)) as src:
        plan = ci.build_plan(src)
        assert plan["subjects"][0]["notes"]["differ"] == 1
        res = ci.apply_import(src, ["ap_history"], plan["fingerprints"])
    assert before <= set(_snapshot())
    assert Chapter.query.get(c99) is not None and Chapter.query.get(c1) is not None
    assert Note.query.filter_by(chapter_id=c1, section_num=1).one().body_en == "<p>HAND EDITED</p>"
    assert res["added"]["chapters"] == 1 and res["added"]["notes"] == 3         # ch2 (new, 2 sections) + ch1 section 2
    assert Note.query.filter(Note.body_en == "<p>other subject</p>").count() == 1


def test_ap_history_replace_is_backed_up_scoped_and_restorable(app, ap_dir):
    from app.services import ap_history_parse
    c1, c99, oc = _seed_ap()
    with ap_history_parse.build_source(str(ap_dir)) as src:
        plan = ci.build_plan(src)
        res = ci.apply_import(src, ["ap_history"], plan["fingerprints"], replace_notes=True, remove_extra=True)
    assert res["notes_replaced"] == 1 and res["notes_removed"] == 0            # chapter 99 is not in the source: untouched
    assert Chapter.query.get(c99) is not None and Note.query.filter_by(chapter_id=c99).count() == 1
    assert NoteBackup.query.filter_by(batch_id=res["batch_id"]).one().body_en == "<p>HAND EDITED</p>"
    ci.restore_batch(res["batch_id"])
    assert Note.query.filter_by(chapter_id=c1, section_num=1).one().body_en == "<p>HAND EDITED</p>"


def test_ap_history_requires_the_subject_to_exist(app, ap_dir):
    from app.services import ap_history_parse
    with pytest.raises(ci.ContentImportError):
        ap_history_parse.build_source(str(ap_dir))


def test_ap_history_missing_files_are_reported(app, ap_dir):
    from app.services import ap_history_parse
    _seed_ap()
    with ap_history_parse.build_source(str(ap_dir)) as src:
        plan = ci.build_plan(src)
    assert any("ch03" in w for w in plan["warnings"])


def test_ap_history_routes(app, admin_client, ap_dir):
    app.config["AP_HISTORY_DIR"] = str(ap_dir)
    c1, c99, oc = _seed_ap(); before = _snapshot()
    assert admin_client.post("/admin/parse-ap-history", data={"csrf_token": "t"}).status_code == 405      # old destructive POST is gone
    assert admin_client.get("/admin/parse-ap-history").status_code == 200
    r = _post(admin_client, "/admin/parse-ap-history/preview")
    html = r.get_data(as_text=True)
    assert r.status_code == 200 and "fp.ap_history" in html and "checked" not in html and _snapshot() == before
    import re
    fp = re.search(r'name="fp.ap_history" value="([0-9a-f]+)"', html).group(1)
    assert _post(admin_client, "/admin/parse-ap-history/apply", **{"fp.ap_history": fp}).status_code == 400        # no subject chosen
    assert _post(admin_client, "/admin/parse-ap-history/apply", subjects="ap_history", replace_notes="1", **{"fp.ap_history": fp}).status_code == 400
    assert _snapshot() == before
    assert _post(admin_client, "/admin/parse-ap-history/apply", subjects="ap_history", **{"fp.ap_history": fp}).status_code == 200
    assert Note.query.filter_by(chapter_id=c1, section_num=1).one().body_en == "<p>HAND EDITED</p>"


def test_ap_history_routes_require_login_and_csrf(app, client, ap_dir):
    for url in ("/admin/parse-ap-history/preview", "/admin/parse-ap-history/apply"):
        assert client.post(url, data={"csrf_token": "x"}).status_code in (302, 400)
    with client.session_transaction() as s:
        s["_csrf"] = "t"
    for url in ("/admin/parse-ap-history/preview", "/admin/parse-ap-history/apply"):
        assert client.post(url, data={"csrf_token": "t"}).status_code == 302
