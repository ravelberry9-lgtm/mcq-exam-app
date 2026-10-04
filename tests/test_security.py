"""Security regressions: stored XSS, production config, admin login/CSRF/throttle, headers."""
import hashlib

import pytest

from app import create_app
from app.config import Config
from app.db import db
from app.models import Chapter, Note, Subject
from app.routes import admin as admin_mod

PAYLOAD = ('<p>ok</p><script>alert(1)</script><style>body{display:none}</style>'
           '<img src="x" onerror="alert(2)"><a href="javascript:alert(3)">l</a>'
           '<p onclick="alert(4)" style="color:red">t</p><iframe src="//evil"></iframe>')


@pytest.fixture()
def note_world(app):
    s = Subject(slug="polity", name_en="Polity", name_te="పాలిటీ")
    db.session.add(s); db.session.flush()
    c = Chapter(subject_id=s.id, chapter_num=1, title_en="Preamble", title_te="ప్రవేశిక")
    db.session.add(c); db.session.flush()
    db.session.add(Note(chapter_id=c.id, section_num=1, heading_en="H", heading_te="హె",
                        body_en=PAYLOAD, body_te=PAYLOAD))
    db.session.commit()
    return c.id


def _assert_clean(html):
    low = html.lower()
    for bad in ("alert(1)", "alert(2)", "alert(3)", "alert(4)", "onerror", "onclick",
                "javascript:", "<iframe", "display:none", "color:red"):
        assert bad not in low, bad
    assert "<p>ok</p>" in low


def test_legacy_reader_sanitises_stored_html(client, note_world):
    r = client.get("/notes/polity/1")
    assert r.status_code == 200
    _assert_clean(r.get_data(as_text=True).split('id="note-reader"', 1)[1])


def test_admin_preview_sanitises_stored_html(client, note_world):
    with client.session_transaction() as s:
        s["admin_token"] = hashlib.sha256(b"admin:1234").hexdigest()
    html = client.get(f"/admin/notes/{note_world}/edit").get_data(as_text=True)
    preview = html.split('class="preview-section"', 1)[1]
    _assert_clean(preview)


def test_admin_save_strips_style_and_scripts(client, note_world):
    with client.session_transaction() as s:
        s["admin_token"] = hashlib.sha256(b"admin:1234").hexdigest(); s["_csrf"] = "t"
    client.post(f"/admin/notes/{note_world}/edit",
                data={"csrf_token": "t", "body_en": PAYLOAD, "body_te": PAYLOAD})
    n = Note.query.filter_by(chapter_id=note_world, section_num=1).first()
    assert "style" not in n.body_en.lower() and "onclick" not in n.body_en and "javascript:" not in n.body_en


# ── production configuration ───────────────────────────────────────
class ProdCfg(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


@pytest.mark.parametrize("secret,pin", [
    ("dev-secret-change-me", "483920"), ("a" * 40, "1234"), ("short", "483920"), ("a" * 40, "123"),
])
def test_production_refuses_default_or_weak_credentials(monkeypatch, secret, pin):
    monkeypatch.setenv("APP_ENV", "production")
    class C(ProdCfg):
        SECRET_KEY = secret; ADMIN_PIN = pin
    with pytest.raises(RuntimeError, match="Unsafe production configuration"):
        create_app(C)


def test_production_accepts_strong_credentials_and_secure_cookie(monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")
    class C(ProdCfg):
        SECRET_KEY = "x" * 40; ADMIN_PIN = "482915"
    create_app(C)


def test_cookie_defaults():
    assert Config.SESSION_COOKIE_HTTPONLY is True and Config.SESSION_COOKIE_SAMESITE == "Lax"


# ── admin login ────────────────────────────────────────────────────
@pytest.fixture(autouse=True)
def _reset_throttle():
    admin_mod._FAILS.clear(); yield; admin_mod._FAILS.clear()


def _login(client, pin="1234", next_="", csrf="t"):
    with client.session_transaction() as s:
        s["_csrf"] = "t"
    url = "/admin/login" + (f"?next={next_}" if next_ else "")
    return client.post(url, data={"pin": pin, "csrf_token": csrf})


@pytest.mark.parametrize("nxt", ["https://evil.example/", "//evil.example/x", "javascript:alert(1)", "/\\evil.example"])
def test_login_rejects_external_next(client, nxt):
    r = _login(client, next_=nxt)
    assert r.status_code == 302
    assert "evil" not in r.headers["Location"] and "javascript" not in r.headers["Location"]


def test_login_allows_local_next(client):
    assert _login(client, next_="/admin/notes").headers["Location"].endswith("/admin/notes")


def test_login_requires_csrf(client):
    assert _login(client, csrf="wrong").status_code == 400
    assert client.post("/admin/login", data={"pin": "1234"}).status_code == 400


def test_login_lockout_after_repeated_failures(client):
    for _ in range(5):
        assert _login(client, pin="0000").status_code == 200
    r = _login(client, pin="1234")             # correct PIN is refused while locked
    assert r.status_code == 429
    assert b"Too many attempts" in r.data


def test_admin_posts_need_csrf_and_logout_is_post(client, note_world):
    with client.session_transaction() as s:
        s["admin_token"] = hashlib.sha256(b"admin:1234").hexdigest(); s["_csrf"] = "t"
    assert client.post(f"/admin/notes/{note_world}/edit", data={"body_en": "x"}).status_code == 400
    assert client.get("/admin/logout").status_code == 405
    assert client.post("/admin/logout", data={"csrf_token": "t"}).status_code == 302
    assert client.get("/admin/", follow_redirects=False).status_code == 302


def test_admin_pages_embed_csrf_token(client):
    with client.session_transaction() as s:
        s["admin_token"] = hashlib.sha256(b"admin:1234").hexdigest()
    html = client.get("/admin/").get_data(as_text=True)
    assert 'name="csrf_token"' in html and 'action="/admin/logout"' in html


# ── headers ────────────────────────────────────────────────────────
def test_security_headers_present(client):
    h = client.get("/healthz").headers
    assert h["X-Content-Type-Options"] == "nosniff" and h["X-Frame-Options"] == "DENY"
    assert "frame-ancestors 'none'" in h["Content-Security-Policy"]
    assert h["Referrer-Policy"]
