"""Flask application factory."""
from flask import Flask, request
from .config import Config
from .db import db


# v3 columns that must exist on the questions table
_V3_QUESTION_COLS = {"subject_id", "chapter_id", "source_type", "options_en"}


def _patch_schema(engine) -> None:
    """Ensure the DB schema matches v3.

    The Railway Postgres DB may contain tables from the legacy app with an
    older schema.  This function detects and fixes those mismatches on every
    startup so the app never crashes due to missing columns.

    Strategy:
    - If the questions table is missing v3-required columns, drop it (and its
      dependents) so db.create_all() can recreate it with the full v3 layout.
    - Otherwise just add the subject_id column if somehow still missing.
    """
    from sqlalchemy import inspect, text

    insp = inspect(engine)
    existing_tables = set(insp.get_table_names())

    if "questions" not in existing_tables:
        return  # nothing to patch; db.create_all() will create it fresh

    q_cols = {c["name"] for c in insp.get_columns("questions")}

    if not _V3_QUESTION_COLS.issubset(q_cols):
        # Old-schema questions table — drop it and let create_all() rebuild
        with engine.connect() as conn:
            try:
                conn.execute(text("DROP TABLE IF EXISTS user_question_state CASCADE"))
                conn.execute(text("DROP TABLE IF EXISTS questions CASCADE"))
                conn.commit()
            except Exception:
                conn.rollback()
        return  # create_all() will rebuild with correct schema

    # Table has v3 columns — nothing to do
    return


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

    # Fix any legacy schema mismatches, then ensure all tables exist
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
