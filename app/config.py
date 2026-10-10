"""
App configuration. Driven by environment variables with sensible defaults
so the app boots on localhost without any setup.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


DEV_SECRET_KEY = "dev-secret-change-me"
DEV_ADMIN_PIN = "1234"


def is_production() -> bool:
    """True on Railway or when APP_ENV=production. Production refuses the public dev credentials."""
    return (os.environ.get("APP_ENV", "").lower() == "production"
            or bool(os.environ.get("RAILWAY_ENVIRONMENT") or os.environ.get("RAILWAY_PROJECT_ID")))


def normalize_database_url(url: str) -> str:
    """Return a SQLAlchemy URL with an explicit driver for PostgreSQL.

    Railway (and Heroku-style platforms) supply ``postgres://`` or a bare
    ``postgresql://``. Since SQLAlchemy 2.1 a bare ``postgresql://`` selects the
    ``psycopg`` (v3) driver, but this app ships ``psycopg2-binary``. Pin the driver
    explicitly so a SQLAlchemy upgrade can never change it silently.

    URLs that already name a driver (``postgresql+psycopg2://``,
    ``postgresql+psycopg://``, ``sqlite:///...``) are returned unchanged.
    """
    url = (url or "").strip()
    for prefix in ("postgres://", "postgresql://"):
        if url.startswith(prefix):
            return "postgresql+psycopg2://" + url[len(prefix):]
    return url


class Config:
    # Flask
    SECRET_KEY = os.environ.get("SECRET_KEY", DEV_SECRET_KEY)
    DEBUG = os.environ.get("FLASK_DEBUG", "0" if is_production() else "1") == "1"

    # Session cookies: HttpOnly always, SameSite=Lax, Secure on production (HTTPS)
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = is_production()
    PERMANENT_SESSION_LIFETIME = 60 * 60 * 12  # admin session: 12 hours

    # Admin brute-force throttle (in memory, per client address)
    ADMIN_MAX_FAILURES = 5
    ADMIN_LOCKOUT_SECONDS = 300

    # Database — SQLite locally, Postgres in production via DATABASE_URL
    _db_url = normalize_database_url(os.environ.get("DATABASE_URL", ""))
    SQLALCHEMY_DATABASE_URI = _db_url or f"sqlite:///{BASE_DIR / 'app_v3.db'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Admin
    ADMIN_PIN = os.environ.get("ADMIN_PIN", DEV_ADMIN_PIN)

    # App settings (replaces app_settings table per v3 decision)
    APP_TITLE = os.environ.get("APP_TITLE", "APPSC prep")
    APP_TITLE_TE = os.environ.get("APP_TITLE_TE", "ఏపీపీఎస్‌సీ తయారీ")
    ACCENT_COLOR = os.environ.get("ACCENT_COLOR", "#1e40af")
    DEFAULT_LANG = os.environ.get("DEFAULT_LANG", "both")  # 'te' | 'en' | 'both'

    # Content sources (for migration)
    LEGACY_DIR = BASE_DIR / "_legacy"
    TEXTBOOK_ROOT = BASE_DIR / "content" / "textbooks"


def validate_production_config(cfg) -> None:
    """Fail fast instead of serving a public site with the development secret or PIN."""
    if not is_production() or cfg.get("TESTING"):
        return
    problems = []
    if cfg.get("SECRET_KEY") in (DEV_SECRET_KEY, "", None) or len(str(cfg.get("SECRET_KEY"))) < 24:
        problems.append("SECRET_KEY must be set to a random value of at least 24 characters")
    pin = str(cfg.get("ADMIN_PIN") or "")
    if pin in (DEV_ADMIN_PIN, "") or len(pin) < 6:
        problems.append("ADMIN_PIN must be set and at least 6 characters (not the default)")
    if problems:
        raise RuntimeError("Unsafe production configuration: " + "; ".join(problems))
