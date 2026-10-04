"""Device identity: a high-entropy, server-issued cookie.

``device_id`` scopes personal state (progress, plans, answer history) to one browser. It is NOT authentication: anyone who
obtains the value acts as that browser. So it must be unguessable, issued by the server and never user-chosen.

* New visitors get ``secrets.token_urlsafe(24)`` (192 bits, 32 characters) in an HttpOnly, SameSite=Lax cookie (Secure in production).
* A cookie that is not in that format is ignored and replaced; there is no ``"anon"`` shared identity any more.
* Cookies written by the old client script (``d-`` + Math.random + timestamp, low entropy) are still honoured so existing
  progress is not lost. They are not issued any more. Replacing them means moving the rows, which is a separate decision.
"""
import re
import secrets

from flask import current_app, g, request

NEW_FORMAT = re.compile(r"^[A-Za-z0-9_-]{32,64}$")
LEGACY_FORMAT = re.compile(r"^d-[a-z0-9]{8,40}$")
COOKIE = "device_id"
ONE_YEAR = 60 * 60 * 24 * 365


def valid(value):
    return bool(value) and bool(NEW_FORMAT.match(value) or LEGACY_FORMAT.match(value))


def device_id():
    """The caller's device id for this request (always set, never 'anon')."""
    return g.device_id


def init_device(app):
    @app.before_request
    def _assign_device():
        if request.endpoint == "static":
            return
        cur = request.cookies.get(COOKIE)
        if valid(cur):
            g.device_id, g.device_is_new = cur, False
        else:
            g.device_id, g.device_is_new = secrets.token_urlsafe(24), True

    @app.after_request
    def _issue_device_cookie(resp):
        if getattr(g, "device_is_new", False):
            resp.set_cookie(COOKIE, g.device_id, max_age=ONE_YEAR, httponly=True, samesite="Lax",
                            secure=bool(current_app.config.get("SESSION_COOKIE_SECURE")))
        return resp
