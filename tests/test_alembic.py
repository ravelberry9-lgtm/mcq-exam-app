"""Migrations: fresh install, legacy (pre-Alembic) databases, idempotence, and no startup DB writes."""
import sqlite3
from pathlib import Path

import pytest
import sqlalchemy as sa
from alembic import command
from alembic.config import Config as AlembicConfig

ROOT = Path(__file__).resolve().parent.parent
HEAD = "b2c3d4e5f6a7"


def _cfg(url, monkeypatch):
    monkeypatch.setenv("ALEMBIC_DATABASE_URL", url)
    cfg = AlembicConfig(str(ROOT / "alembic.ini"))
    cfg.set_main_option("script_location", str(ROOT / "migrations"))
    return cfg


@pytest.fixture()
def dburl(tmp_path):
    return f"sqlite:///{tmp_path / 'm.db'}"


def _tables(url):
    return set(sa.inspect(sa.create_engine(url)).get_table_names()) - {"alembic_version"}


def test_fresh_upgrade_matches_models(dburl, monkeypatch):
    cfg = _cfg(dburl, monkeypatch)
    command.upgrade(cfg, "head")
    assert len(_tables(dburl)) == 15
    command.check(cfg)                      # raises if models and migrations have drifted


def test_upgrade_is_idempotent_and_downgrade_works(dburl, monkeypatch):
    cfg = _cfg(dburl, monkeypatch)
    command.upgrade(cfg, "head"); command.upgrade(cfg, "head")
    command.downgrade(cfg, "base")
    assert _tables(dburl) == set()


# Shape of the real pre-Alembic content.db: nullable INTEGER PRIMARY KEY, TEXT types, no ON DELETE CASCADE,
# no passage FK, legacy idx_q_* indexes and a q_hash fingerprint column.
LEGACY = """
CREATE TABLE subjects (id INTEGER PRIMARY KEY, slug TEXT NOT NULL UNIQUE, name_en TEXT NOT NULL, name_te TEXT NOT NULL, sort_order INTEGER);
CREATE TABLE chapters (id INTEGER PRIMARY KEY, subject_id INTEGER NOT NULL REFERENCES subjects(id), chapter_num INTEGER NOT NULL,
                       title_en TEXT NOT NULL, title_te TEXT NOT NULL, est_read_minutes INTEGER, UNIQUE(subject_id, chapter_num));
CREATE TABLE notes (id INTEGER PRIMARY KEY, chapter_id INTEGER NOT NULL REFERENCES chapters(id), section_num INTEGER NOT NULL,
                    heading_en TEXT, heading_te TEXT, body_en TEXT, body_te TEXT, UNIQUE(chapter_id, section_num));
CREATE TABLE questions (id INTEGER PRIMARY KEY, subject_id INTEGER NOT NULL REFERENCES subjects(id), chapter_id INTEGER REFERENCES chapters(id),
                        source_type TEXT NOT NULL, q_hash TEXT, correct_answer TEXT NOT NULL, question_en TEXT, options_en TEXT, passage_id INTEGER);
CREATE INDEX idx_q_subj ON questions(subject_id);
CREATE INDEX idx_q_ch ON questions(chapter_id);
CREATE INDEX idx_q_hash ON questions(q_hash);
INSERT INTO subjects VALUES (1,'polity','Polity','పాలిటీ',1);
INSERT INTO chapters VALUES (7,1,1,'Preamble','ప్రవేశిక',5);
INSERT INTO notes VALUES (1,7,1,'Intro','పరిచయం','<p>en</p>','<p>te</p>');
INSERT INTO questions VALUES (1,1,7,'chapter','h1','a','Q one','{"a": "x"}',NULL), (2,1,NULL,'practice','h2','b','Q two',NULL,NULL);
"""
LEGACY_DATA = {
    "subjects": "SELECT id, slug, name_en, name_te, sort_order FROM subjects ORDER BY id",
    "chapters": "SELECT id, subject_id, chapter_num, title_en, title_te, est_read_minutes FROM chapters ORDER BY id",
    "notes": "SELECT id, chapter_id, section_num, heading_en, heading_te, body_en, body_te FROM notes ORDER BY id",
    "questions": "SELECT id, subject_id, chapter_id, source_type, q_hash, correct_answer, question_en FROM questions ORDER BY id",
}


def _make_legacy(dburl, script=LEGACY):
    con = sqlite3.connect(dburl.replace("sqlite:///", "")); con.executescript(script); con.commit(); con.close()


def _snapshot(dburl):
    con = sqlite3.connect(dburl.replace("sqlite:///", ""))
    try:
        return {k: con.execute(q).fetchall() for k, q in LEGACY_DATA.items()}
    finally:
        con.close()


def test_legacy_database_is_adopted_converges_to_the_model_and_keeps_every_row(dburl, monkeypatch):
    _make_legacy(dburl)
    before = _snapshot(dburl)
    cfg = _cfg(dburl, monkeypatch)
    command.upgrade(cfg, "head")
    command.check(cfg)                                   # legacy schema now agrees with the models (not just fresh installs)

    assert _snapshot(dburl) == before                    # every row identical, q_hash preserved
    assert len(_tables(dburl)) == 15
    eng = sa.create_engine(dburl); insp = sa.inspect(eng)
    assert not any(ix["name"].startswith("idx_q_") for ix in insp.get_indexes("questions"))
    assert any(fk["options"].get("ondelete") == "CASCADE" for fk in insp.get_foreign_keys("notes"))
    assert any(fk["referred_table"] == "passages" for fk in insp.get_foreign_keys("questions"))
    with eng.connect() as c:
        assert c.execute(sa.text("SELECT version_num FROM alembic_version")).scalar() == HEAD
    con = sqlite3.connect(dburl.replace("sqlite:///", ""))
    assert con.execute("PRAGMA foreign_key_check").fetchall() == []
    assert con.execute("PRAGMA integrity_check").fetchone() == ("ok",)


# ── P2: detection is structural, not tied to one symptom ──────────────────────────
def _fresh_head_with_rows(dburl, monkeypatch):
    cfg = _cfg(dburl, monkeypatch)
    command.upgrade(cfg, "head")
    con = sqlite3.connect(dburl.replace("sqlite:///", ""))
    con.executescript("""
    INSERT INTO subjects (id,slug,name_en,name_te) VALUES (1,'polity','Polity','పాలిటీ');
    INSERT INTO chapters (id,subject_id,chapter_num,title_en,title_te) VALUES (7,1,1,'Preamble','ప్రవేశిక');
    INSERT INTO notes (id,chapter_id,section_num,heading_en,body_en) VALUES (1,7,1,'Intro','<p>x</p>');
    INSERT INTO questions (id,subject_id,chapter_id,source_type,correct_answer,question_en) VALUES (1,1,7,'chapter','a','Q');
    """); con.commit(); con.close()
    return cfg


def _replace_table(dburl, name, ddl):
    """Recreate `name` with different DDL, keeping its rows (simulates a drifted pre-Alembic table)."""
    con = sqlite3.connect(dburl.replace("sqlite:///", ""))
    cols = sorted(r[1] for r in con.execute(f"PRAGMA table_info({name})"))
    rows = con.execute(f"SELECT {','.join(cols)} FROM {name}").fetchall()
    con.execute("PRAGMA legacy_alter_table=ON")          # keep other tables' FKs pointing at the *name*
    con.execute(f"ALTER TABLE {name} RENAME TO {name}_old"); con.executescript(ddl)
    con.executemany(f"INSERT INTO {name} ({','.join(cols)}) VALUES ({','.join('?' * len(cols))})", rows)
    con.execute(f"DROP TABLE {name}_old"); con.commit(); con.close()
    return rows


def _stamp_back(cfg):
    command.stamp(cfg, "a1b2c3d4e5f6")


def test_correct_tables_are_not_rebuilt(dburl, monkeypatch):
    import importlib.util
    cfg = _cfg(dburl, monkeypatch); command.upgrade(cfg, "head")
    spec = importlib.util.spec_from_file_location("conv", next((ROOT / "migrations" / "versions").glob("*converge_legacy*")))
    conv = importlib.util.module_from_spec(spec); spec.loader.exec_module(conv)
    insp = sa.inspect(sa.create_engine(dburl))
    assert [t.name for t in conv._REBUILD_ORDER if conv._needs_rebuild(insp, t)] == []


NOTES_NO_CASCADE = """CREATE TABLE notes (id INTEGER NOT NULL, chapter_id INTEGER NOT NULL, section_num INTEGER NOT NULL,
  heading_en VARCHAR(256), heading_te VARCHAR(256), body_en TEXT, body_te TEXT, PRIMARY KEY (id),
  FOREIGN KEY(chapter_id) REFERENCES chapters (id), UNIQUE (chapter_id, section_num));"""
QUESTIONS_NO_PASSAGE_FK = """CREATE TABLE questions (id INTEGER NOT NULL, subject_id INTEGER NOT NULL, chapter_id INTEGER,
  source_type VARCHAR(16) NOT NULL, q_hash VARCHAR(32), pyq_year VARCHAR(8), pyq_paper VARCHAR(64), difficulty VARCHAR(2),
  question_en TEXT, question_te TEXT, options_en JSON, options_te JSON, correct_answer VARCHAR(1) NOT NULL,
  explanation_en TEXT, explanation_te TEXT, passage_id INTEGER, created_at DATETIME, updated_at DATETIME, PRIMARY KEY (id),
  FOREIGN KEY(chapter_id) REFERENCES chapters (id), FOREIGN KEY(subject_id) REFERENCES subjects (id));"""
CHAPTERS_NULLABLE_TITLE = """CREATE TABLE chapters (id INTEGER NOT NULL, subject_id INTEGER NOT NULL, chapter_num INTEGER NOT NULL,
  title_en VARCHAR(256), title_te VARCHAR(256) NOT NULL, est_read_minutes INTEGER, PRIMARY KEY (id),
  FOREIGN KEY(subject_id) REFERENCES subjects (id) ON DELETE CASCADE, UNIQUE (subject_id, chapter_num));"""


@pytest.mark.parametrize("table,ddl,probe", [
    ("notes", NOTES_NO_CASCADE,
     lambda insp: any(f["options"].get("ondelete") == "CASCADE" for f in insp.get_foreign_keys("notes"))),
    ("questions", QUESTIONS_NO_PASSAGE_FK,
     lambda insp: any(f["referred_table"] == "passages" for f in insp.get_foreign_keys("questions"))),
    ("chapters", CHAPTERS_NULLABLE_TITLE,
     lambda insp: not [c for c in insp.get_columns("chapters") if c["name"] == "title_en"][0]["nullable"]),
], ids=["missing-cascade", "missing-passage-fk", "nullable-title"])
def test_drifted_table_with_proper_primary_key_is_still_converged(dburl, monkeypatch, table, ddl, probe):
    """Each of these has a correct NOT NULL primary key, so only a structural check can notice the drift."""
    cfg = _fresh_head_with_rows(dburl, monkeypatch)
    rows = _replace_table(dburl, table, ddl)
    insp = sa.inspect(sa.create_engine(dburl))
    assert not probe(insp)                          # the drift exists before the upgrade
    _stamp_back(cfg)
    command.upgrade(cfg, "head")
    command.check(cfg)                              # now agrees with the model
    assert probe(sa.inspect(sa.create_engine(dburl)))
    con = sqlite3.connect(dburl.replace("sqlite:///", ""))
    cols = sorted(r[1] for r in con.execute(f"PRAGMA table_info({table})"))
    assert con.execute(f"SELECT {','.join(cols)} FROM {table}").fetchall() == rows     # rows untouched (compared by column name)
    assert con.execute("PRAGMA foreign_key_check").fetchall() == []


def test_downgrade_refuses_to_delete_existing_data(dburl, monkeypatch):
    """The baseline may have adopted tables it did not create, so it must never drop populated ones."""
    _make_legacy(dburl)
    cfg = _cfg(dburl, monkeypatch)
    command.upgrade(cfg, "head")
    before = _snapshot(dburl)
    with pytest.raises(RuntimeError, match="Refusing to downgrade"):
        command.downgrade(cfg, "base")
    assert _snapshot(dburl) == before and len(_tables(dburl)) == 15


def test_downgrade_of_a_fresh_populated_database_is_also_refused(dburl, monkeypatch):
    cfg = _cfg(dburl, monkeypatch)
    command.upgrade(cfg, "head")
    con = sqlite3.connect(dburl.replace("sqlite:///", ""))
    con.execute("INSERT INTO subjects (slug,name_en,name_te) VALUES ('s','S','ఎస్')"); con.commit(); con.close()
    with pytest.raises(RuntimeError, match="subjects"):
        command.downgrade(cfg, "base")


def test_questions_without_a_subject_are_never_guessed(dburl, monkeypatch):
    """Older DB with no questions.subject_id: chapter rows inherit, orphan rows stop the upgrade until assigned."""
    old = """
    CREATE TABLE subjects (id INTEGER PRIMARY KEY, slug TEXT NOT NULL UNIQUE, name_en TEXT NOT NULL, name_te TEXT NOT NULL, sort_order INTEGER);
    CREATE TABLE chapters (id INTEGER PRIMARY KEY, subject_id INTEGER NOT NULL, chapter_num INTEGER NOT NULL, title_en TEXT NOT NULL, title_te TEXT NOT NULL, est_read_minutes INTEGER);
    CREATE TABLE questions (id INTEGER PRIMARY KEY, chapter_id INTEGER, source_type TEXT NOT NULL, correct_answer TEXT NOT NULL, question_en TEXT);
    INSERT INTO subjects VALUES (1,'polity','Polity','పాలిటీ',1);
    INSERT INTO chapters VALUES (7,1,1,'Preamble','ప్రవేశిక',5);
    INSERT INTO questions VALUES (1,7,'chapter','a','with chapter'), (2,NULL,'practice','b','orphan');
    """
    _make_legacy(dburl, old)
    cfg = _cfg(dburl, monkeypatch)
    with pytest.raises(RuntimeError, match="1 question"):
        command.upgrade(cfg, "head")
    con = sqlite3.connect(dburl.replace("sqlite:///", ""))
    assert con.execute("SELECT COUNT(*) FROM questions").fetchone()[0] == 2            # nothing deleted
    con.execute("UPDATE questions SET subject_id = 1 WHERE subject_id IS NULL"); con.commit(); con.close()
    command.upgrade(cfg, "head")                                                         # operator assigned them; now it adopts
    command.check(cfg)
    con = sqlite3.connect(dburl.replace("sqlite:///", ""))
    assert con.execute("SELECT id, subject_id FROM questions ORDER BY id").fetchall() == [(1, 1), (2, 1)]


@pytest.mark.skipif(not __import__("os").environ.get("TEST_PG_URL"),
                    reason="set TEST_PG_URL=postgresql+psycopg2://... (an empty scratch database) to run the PostgreSQL checks")
def test_postgresql_fresh_legacy_check_and_downgrade_safety(monkeypatch):
    import os
    url = os.environ["TEST_PG_URL"]
    eng = sa.create_engine(url)
    with eng.begin() as c:
        c.execute(sa.text("DROP SCHEMA public CASCADE")); c.execute(sa.text("CREATE SCHEMA public"))
    cfg = _cfg(url, monkeypatch)
    command.upgrade(cfg, "head"); command.check(cfg); command.upgrade(cfg, "head")
    # legacy: what the older release had: no alembic_version, no subject_id, no q_hash
    with eng.begin() as c:
        c.execute(sa.text("INSERT INTO subjects (id,slug,name_en,name_te) VALUES (1,'polity','Polity','పాలిటీ')"))
        c.execute(sa.text("INSERT INTO chapters (id,subject_id,chapter_num,title_en,title_te) VALUES (7,1,1,'Preamble','ప్రవేశిక')"))
        c.execute(sa.text("INSERT INTO questions (id,subject_id,chapter_id,source_type,correct_answer,question_en) VALUES (1,1,7,'chapter','a','Q')"))
        c.execute(sa.text("DROP INDEX ix_questions_subject_id")); c.execute(sa.text("DROP INDEX ix_questions_q_hash"))
        c.execute(sa.text("ALTER TABLE questions DROP COLUMN subject_id")); c.execute(sa.text("ALTER TABLE questions DROP COLUMN q_hash"))
        c.execute(sa.text("DROP TABLE alembic_version"))
    command.upgrade(cfg, "head"); command.check(cfg)
    with eng.connect() as c:
        assert c.execute(sa.text("SELECT subject_id FROM questions WHERE id=1")).scalar() == 1
        assert [x for x in sa.inspect(eng).get_columns("questions") if x["name"] == "subject_id"][0]["nullable"] is False
    with pytest.raises(RuntimeError, match="Refusing to downgrade"):
        command.downgrade(cfg, "base")
    with eng.connect() as c:
        assert c.execute(sa.text("SELECT COUNT(*) FROM questions")).scalar() == 1


def test_app_startup_never_modifies_the_database(tmp_path):
    """create_app() must not create tables or alter schema; Alembic is the only schema writer."""
    from app import create_app
    from app.config import Config

    db_file = tmp_path / "untouched.db"

    class C(Config):
        TESTING = True
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_file}"

    app = create_app(C)
    with app.test_client() as c:
        c.get("/healthz")
    assert not db_file.exists() or _tables(f"sqlite:///{db_file}") == set()
    src = (ROOT / "app" / "__init__.py").read_text(encoding="utf-8")
    assert "create_all" not in src and "_patch_schema" not in src


def test_no_destructive_or_implicit_schema_code_anywhere_in_the_app():
    """Release blocker: origin/main once shipped _patch_schema() with DROP TABLE questions CASCADE plus create_all()
    at startup. No file under app/ or wsgi.py may contain startup DDL again, whatever a merge resolves to."""
    import re
    bad = re.compile(r"DROP\s+TABLE|drop_all\s*\(|create_all\s*\(|_patch_schema", re.I)
    offenders = []
    for path in list((ROOT / "app").rglob("*.py")) + [ROOT / "wsgi.py"]:
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if bad.search(line):
                offenders.append(f"{path.relative_to(ROOT)}:{n}: {line.strip()[:80]}")
    assert offenders == []
