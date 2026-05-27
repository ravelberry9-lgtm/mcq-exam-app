"""
App configuration. Driven by environment variables with sensible defaults
so the app boots on localhost without any setup.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    # Flask
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")
    DEBUG = os.environ.get("FLASK_DEBUG", "1") == "1"

    # Database — SQLite locally, Postgres in production via DATABASE_URL
    _db_url = os.environ.get("DATABASE_URL", "")
    if _db_url.startswith("postgres://"):
        _db_url = _db_url.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = _db_url or f"sqlite:///{BASE_DIR / 'app_v3.db'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Admin
    ADMIN_PIN = os.environ.get("ADMIN_PIN", "1234")

    # App settings (replaces app_settings table per v3 decision)
    APP_TITLE = os.environ.get("APP_TITLE", "APPSC prep")
    APP_TITLE_TE = os.environ.get("APP_TITLE_TE", "ఏపీపీఎస్‌సీ తయారీ")
    ACCENT_COLOR = os.environ.get("ACCENT_COLOR", "#1e40af")
    DEFAULT_LANG = os.environ.get("DEFAULT_LANG", "both")  # 'te' | 'en' | 'both'

    # Content sources (for migration)
    LEGACY_DIR = BASE_DIR / "_legacy"
