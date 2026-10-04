"""Database URL handling: the exact URL shapes Railway supplies must select psycopg2.

Regression for the first Railway staging deploy: Railway provides a bare
``postgresql://`` URL; SQLAlchemy 2.1 maps that to the ``psycopg`` (v3) driver, which
is not installed, so ``alembic upgrade head`` died with ``No module named 'psycopg'``.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import make_url

from app.config import normalize_database_url

ROOT = Path(__file__).resolve().parent.parent

# The shape Railway's ${{Postgres.DATABASE_URL}} reference resolves to.
RAILWAY_BARE = "postgresql://postgres:s3cr%40t@postgres.railway.internal:5432/railway"
HEROKU_STYLE = "postgres://postgres:s3cr%40t@postgres.railway.internal:5432/railway"


def _driver(url):
    return make_url(url).get_dialect().driver


def test_bare_postgresql_url_selects_psycopg2():
    out = normalize_database_url(RAILWAY_BARE)
    assert out.startswith("postgresql+psycopg2://")
    assert _driver(out) == "psycopg2"
    # Credentials, host, port, database are untouched (including percent-encoding).
    before, after = make_url(RAILWAY_BARE), make_url(out)
    assert (before.username, before.password, before.host, before.port, before.database) == \
           (after.username, after.password, after.host, after.port, after.database)


def test_postgres_scheme_url_selects_psycopg2():
    out = normalize_database_url(HEROKU_STYLE)
    assert out.startswith("postgresql+psycopg2://")
    assert _driver(out) == "psycopg2"


def test_normalised_url_creates_an_engine_with_the_installed_driver():
    """create_engine imports the DBAPI immediately, so a missing driver fails here, offline."""
    engine = create_engine(normalize_database_url(RAILWAY_BARE))
    assert engine.dialect.driver == "psycopg2"
    assert engine.dialect.dbapi.__name__ == "psycopg2"
    engine.dispose()


def test_raw_bare_url_is_what_would_have_broken_without_the_fix():
    """Documents the failure mode: on SQLAlchemy >= 2.1 the bare URL means psycopg v3."""
    import sqlalchemy
    major_minor = tuple(int(x) for x in sqlalchemy.__version__.split(".")[:2])
    if major_minor < (2, 1):
        pytest.skip("bare postgresql:// still maps to psycopg2 before SQLAlchemy 2.1")
    assert _driver(RAILWAY_BARE) == "psycopg"
    assert _driver(normalize_database_url(RAILWAY_BARE)) == "psycopg2"


@pytest.mark.parametrize("url", [
    "postgresql+psycopg2://u:p@h:5432/db",
    "postgresql+psycopg://u:p@h:5432/db",
    "postgresql+asyncpg://u:p@h:5432/db",
    "sqlite:///app_v3.db",
    "sqlite://",
    "mysql+pymysql://u:p@h/db",
])
def test_urls_that_already_name_a_driver_are_unchanged(url):
    assert normalize_database_url(url) == url


@pytest.mark.parametrize("raw,expected", [
    ("", ""),
    (None, ""),
    ("   ", ""),
    ("  postgres://u:p@h/db  ", "postgresql+psycopg2://u:p@h/db"),
])
def test_empty_and_padded_values(raw, expected):
    assert normalize_database_url(raw) == expected


def test_query_string_survives_normalisation():
    url = "postgresql://u:p@h:5432/db?sslmode=require&connect_timeout=5"
    assert normalize_database_url(url) == "postgresql+psycopg2://u:p@h:5432/db?sslmode=require&connect_timeout=5"


def _config_uri(env_value):
    env = {k: v for k, v in os.environ.items() if k != "DATABASE_URL"}
    if env_value is not None:
        env["DATABASE_URL"] = env_value
    code = "from app.config import Config; print(Config.SQLALCHEMY_DATABASE_URI)"
    out = subprocess.run([sys.executable, "-c", code], cwd=ROOT, env=env,
                         capture_output=True, text=True, check=True)
    return out.stdout.strip()


def test_app_config_applies_the_normalisation_from_the_environment():
    assert _config_uri(RAILWAY_BARE).startswith("postgresql+psycopg2://")
    assert _config_uri(HEROKU_STYLE).startswith("postgresql+psycopg2://")
    assert _config_uri("postgresql+psycopg2://u:p@h/db") == "postgresql+psycopg2://u:p@h/db"
    assert _config_uri(None).startswith("sqlite:///")


def test_requirements_are_pinned_to_exact_versions():
    """A floating requirement let SQLAlchemy 2.1 change the default Postgres driver silently."""
    lines = [ln.strip() for ln in (ROOT / "requirements.txt").read_text().splitlines()]
    reqs = [ln for ln in lines if ln and not ln.startswith("#")]
    assert reqs, "requirements.txt is empty"
    unpinned = [r for r in reqs if not re.fullmatch(r"[A-Za-z0-9_.\-]+==[0-9][A-Za-z0-9.\-+!]*", r)]
    assert not unpinned, f"requirements must use exact == pins: {unpinned}"
    names = {r.split("==")[0].lower() for r in reqs}
    # Every library the app imports directly in production must be pinned.
    assert {"flask", "flask-sqlalchemy", "sqlalchemy", "alembic", "psycopg2-binary",
            "gunicorn", "bleach", "pyyaml", "markdown", "beautifulsoup4",
            "python-dotenv"} <= names


@pytest.mark.skipif(not os.environ.get("TEST_PG_URL"),
                    reason="set TEST_PG_URL=postgresql+psycopg2://... (a server where a scratch database can be created)")
def test_alembic_runs_against_the_exact_railway_url_shape():
    """End to end: the pre-deploy command, with a bare postgresql:// DATABASE_URL, production mode.

    Uses its own throw-away database on the TEST_PG_URL server so it never touches the
    other PostgreSQL tests' scratch database.
    """
    import uuid
    import psycopg2

    base = make_url(os.environ["TEST_PG_URL"])
    scratch = "rwy_regress_" + uuid.uuid4().hex[:10]
    admin = psycopg2.connect(host=base.host, port=base.port or 5432, user=base.username,
                             password=base.password, dbname=base.database)
    admin.autocommit = True
    try:
        admin.cursor().execute(f'CREATE DATABASE "{scratch}"')
        bare = base.set(drivername="postgresql", database=scratch).render_as_string(hide_password=False)
        assert bare.startswith("postgresql://")
        env = {k: v for k, v in os.environ.items() if k not in ("ALEMBIC_DATABASE_URL", "TEST_PG_URL")}
        env.update({
            "DATABASE_URL": bare,
            "APP_ENV": "production",
            "SECRET_KEY": "k" * 48 + "-regression-only",
            "ADMIN_PIN": "regression-only-pin-0001",
        })
        for cmd in (["upgrade", "head"], ["current"], ["check"]):
            res = subprocess.run([sys.executable, "-m", "alembic", *cmd], cwd=ROOT, env=env,
                                 capture_output=True, text=True)
            assert res.returncode == 0, f"alembic {' '.join(cmd)} failed:\n{res.stdout}\n{res.stderr}"
            assert "No module named" not in res.stderr
        current = subprocess.run([sys.executable, "-m", "alembic", "current"], cwd=ROOT, env=env,
                                 capture_output=True, text=True).stdout
        assert "(head)" in current
    finally:
        try:
            admin.cursor().execute(f'DROP DATABASE IF EXISTS "{scratch}"')
        finally:
            admin.close()
