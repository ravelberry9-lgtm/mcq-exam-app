"""Migrations: fresh install, legacy (pre-Alembic) databases, idempotence, and no startup DB writes."""
import sqlite3
from pathlib import Path

import pytest
import sqlalchemy as sa
from alembic import command
from alembic.config import Config as AlembicConfig

ROOT = Path(__file__).resolve().parent.parent
HEAD = "a1b2c3d4e5f6"


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


LEGACY = """
CREATE TABLE subjects (id INTEGER PRIMARY KEY, slug TEXT NOT NULL, name_en TEXT NOT NULL, name_te TEXT NOT NULL, sort_order INTEGER);
CREATE TABLE chapters (id INTEGER PRIMARY KEY, subject_id INTEGER NOT NULL, chapter_num INTEGER NOT NULL, title_en TEXT NOT NULL, title_te TEXT NOT NULL, est_read_minutes INTEGER);
CREATE TABLE questions (id INTEGER PRIMARY KEY, chapter_id INTEGER, source_type TEXT NOT NULL, correct_answer TEXT NOT NULL,
                        question_en TEXT, q_hash TEXT);
INSERT INTO subjects VALUES (1,'polity','Polity','పాలిటీ',1);
INSERT INTO chapters VALUES (7,1,1,'Preamble','ప్రవేశిక',5);
INSERT INTO questions VALUES (1,7,'chapter','a','Q one','h1'), (2,NULL,'practice','b','Q two','h2');
"""


def test_legacy_database_is_upgraded_in_place_without_losing_data(dburl, monkeypatch):
    path = dburl.replace("sqlite:///", "")
    con = sqlite3.connect(path); con.executescript(LEGACY); con.commit(); con.close()
    cfg = _cfg(dburl, monkeypatch)
    command.upgrade(cfg, "head")

    eng = sa.create_engine(dburl); insp = sa.inspect(eng)
    assert len(_tables(dburl)) == 15                                   # missing tables created
    assert "subject_id" in {c["name"] for c in insp.get_columns("questions")}   # column added
    with eng.connect() as c:
        rows = c.execute(sa.text("SELECT id, question_en, q_hash, subject_id FROM questions ORDER BY id")).all()
        assert rows == [(1, "Q one", "h1", 1), (2, "Q two", "h2", None)]   # data kept; chapter row backfilled; no guessing
        assert c.execute(sa.text("SELECT title_en FROM chapters")).scalar() == "Preamble"
        assert c.execute(sa.text("SELECT version_num FROM alembic_version")).scalar() == HEAD


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
