"""Flask application factory."""
from flask import Flask, request
from .config import Config
from .db import db


def _patch_schema(engine) -> None:
    """Idempotently add columns/tables that may be missing in older DB schemas.

    Uses PostgreSQL's ADD COLUMN IF NOT EXISTS so it is safe to run on every
    startup.  SQLite (local dev) doesn't support IF NOT EXISTS on ALTER TABLE,
    so we catch and swallow those errors.
    """
    from sqlalchemy import inspect, text

    insp = inspect(engine)
    existing_tables = set(insp.get_table_names())

    with engine.connect() as conn:
        # ── questions.subject_id ──────────────────────────────────────────
        if "questions" in existing_tables:
            q_cols = {c["name"] for c in insp.get_columns("questions")}
            if "subject_id" not in q_cols:
                try:
                    conn.execute(text(
                        "ALTER TABLE questions "
                        "ADD COLUMN IF NOT EXISTS subject_id INTEGER "
                        "REFERENCES subjects(id)"
                    ))
                    conn.execute(text(
                        "CREATE INDEX IF NOT EXISTS ix_questions_subject_id "
                        "ON questions (subject_id)"
                    ))
                    conn.commit()
                except Exception:
                    conn.rollback()


def create_app(config_class: type = Config) -> Flask:
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="../static",
        static_url_path="/static",
    )
    app.config.from_object(config_class)
    db.init_app(app)

    from . import models  # noqa: F401

    # Apply schema patches then ensure all tables exist
    with app.app_context():
        _patch_schema(db.engine)
        db.create_all()

    from .routes.public import bp as public_bp
    app.register_blueprint(public_bp)

    from .routes.admin import bp as admin_bp
    app.register_blueprint(admin_bp)

    from .routes.notes import bp as notes_bp
    app.register_blueprint(notes_bp)

    from .routes.exam_session import bp as exam_session_bp
    app.register_blueprint(exam_session_bp)

    from .routes.study_plan import bp as study_plan_bp
    app.register_blueprint(study_plan_bp)

    @app.context_processor
    def inject_globals():
        from .services.nav import build_tree
        try:
            menu_tree = build_tree("menu")
        except Exception:
            menu_tree = []
        lang_pref = request.cookies.get("lang", app.config["DEFAULT_LANG"])
        lang_code = "te" if lang_pref in ("te", "both") else "en"
        return {
            "app_title": app.config["APP_TITLE"],
            "app_title_te": app.config["APP_TITLE_TE"],
            "accent_color": app.config["ACCENT_COLOR"],
            "default_lang": app.config["DEFAULT_LANG"],
            "lang_pref": lang_pref,
            "lang_code": lang_code,
            "menu_tree": menu_tree,
            "user_name": "Ravelberry",
        }

    return app
