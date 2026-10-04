"""Pytest fixtures — fresh in-memory SQLite per test."""
import pytest
from flask.testing import FlaskClient
from app import create_app
from app.config import Config
from app.db import db as _db


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SECRET_KEY = "test"


@pytest.fixture()
def app():
    app = create_app(TestConfig)
    with app.app_context():
        _db.create_all()
        yield app
        _db.session.remove()
        _db.drop_all()


class CsrfClient(FlaskClient):
    """Test client that attaches a valid CSRF token to every non-admin write request (admin tests send their own), so ordinary tests exercise the real flow. A test that
    checks the protection itself sets ``client.auto_csrf = False``."""
    auto_csrf = True

    def open(self, *args, **kwargs):
        method = (kwargs.get("method") or "GET").upper()
        path = args[0] if args and isinstance(args[0], str) else ""
        if self.auto_csrf and method in ("POST", "PUT", "PATCH", "DELETE") and not path.startswith("/admin"):
            with self.session_transaction() as sess:
                tok = sess.setdefault("_csrf", "test-csrf-token")
            headers = dict(kwargs.get("headers") or {})
            headers.setdefault("X-CSRF-Token", tok)
            kwargs["headers"] = headers
        return super().open(*args, **kwargs)


@pytest.fixture()
def client(app):
    app.test_client_class = CsrfClient
    return app.test_client()
