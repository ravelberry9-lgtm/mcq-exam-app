"""Session-bound CSRF token shared by the admin and exam blueprints.

The token lives in the signed Flask session (``_csrf``), is rendered into forms with ``csrf_token()`` and sent by scripts
in the ``X-CSRF-Token`` header. ``failure`` is None when the request carries the right token.
"""
import hmac
import secrets

from flask import request, session


def csrf_token() -> str:
    tok = session.get("_csrf")
    if not tok:
        tok = secrets.token_urlsafe(32)
        session["_csrf"] = tok
    return tok


def token_matches() -> bool:
    sent = request.form.get("csrf_token") or request.headers.get("X-CSRF-Token") or ""
    expected = session.get("_csrf") or ""
    return bool(expected) and hmac.compare_digest(sent, expected)
