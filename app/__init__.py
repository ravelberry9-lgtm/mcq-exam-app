"""Flask application factory."""
from flask import Flask, request
from .config import Config
from .db import db


def create_app(config_class: type = Config) -> Flask:
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="../static",
        static_url_path="/static",
    )
    app.config.from_object(config_class)
    from .config import validate_production_config
    validate_production_config(app.config)

    db.init_app(app)

    from .services.csrf import init_csrf
    init_csrf(app)

    from .services.learn import render_note_html

    @app.template_filter("note_html")
    def note_html_filter(html, keep_class=False):
        """Sanitise stored note HTML at render time (never trust what is in the database)."""
        from markupsafe import Markup
        return Markup(render_note_html(html, keep_class))

    @app.after_request
    def security_headers(resp):
        resp.headers.setdefault("X-Content-Type-Options", "nosniff")
        resp.headers.setdefault("X-Frame-Options", "DENY")
        resp.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        resp.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        # Legacy pages still use inline script/style, so those stay allowed for now; framing,
        # plugins and <base> hijacking are blocked. Tighten once the old pages are replaced.
        resp.headers.setdefault(
            "Content-Security-Policy",
            "default-src 'self'; img-src 'self' data: https:; style-src 'self' 'unsafe-inline'; "
            "script-src 'self' 'unsafe-inline'; font-src 'self' data:; connect-src 'self'; "
            "object-src 'none'; base-uri 'self'; frame-ancestors 'none'; form-action 'self'")
        return resp


    from . import models  # noqa: F401
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

    from .routes.learn import bp as learn_bp  # design-system journey (/learn)
    app.register_blueprint(learn_bp)

    from .services import qdisplay
    app.jinja_env.globals.update(bi_kind=qdisplay.bi_kind, option_items=qdisplay.option_items, option_item=qdisplay.option_item)

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
