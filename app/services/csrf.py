"""Session-bound CSRF protection for every state-changing request in the app.

The token lives in the signed Flask session (``_csrf``). Pages render it with ``csrf_token()`` (hidden form fields and a
``<meta name="csrf-token">`` that scripts read), and scripts send it in the ``X-CSRF-Token`` header. ``init_csrf`` installs one
app-wide check for POST / PUT / PATCH / DELETE, so a new form or endpoint is protected by default instead of by remembering
to add a check. The only exemption is the static files route, which has no write methods.
"""
import hmac
import secrets

from flask import abort, jsonify, request, session

UNSAFE = ("POST", "PUT", "PATCH", "DELETE")


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


def _wants_json() -> bool:
    p = request.path
    return request.is_json or "/api/" in p or p.endswith("/answer") or "application/json" in request.headers.get("Accept", "")


def init_csrf(app):
    app.add_template_global(csrf_token, "csrf_token")

    @app.before_request
    def _csrf_protect():
        if request.method in UNSAFE and request.endpoint != "static" and not token_matches():
            if _wants_json():
                return jsonify({"error": "missing or invalid CSRF token; reload the page and try again"}), 400
            abort(400, "Missing or invalid CSRF token. Reload the page and try again.")
