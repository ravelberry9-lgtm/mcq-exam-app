"""App-wide access code: a 6-digit code (set by the admin) that a device enters once.

The code is stored hashed in ``app_setting``. A device that enters it gets a long-lived HttpOnly cookie holding an HMAC
of the current code hash, so changing the code in the admin panel makes every device enter the new code once.
If no code is set, the gate is off. Admin pages, the health check and static files are never gated.
"""
import hashlib
import hmac
import secrets
import time

from flask import current_app, jsonify, redirect, request, url_for

from ..account_models import AppSetting
from ..db import db

COOKIE = 'app_access'
TEN_YEARS = 60 * 60 * 24 * 3650
KEY = 'access_code_hash'
_ready, _cache = [], {'t': 0, 'v': None}
OPEN_PREFIXES = ('/static/', '/admin', '/access', '/healthz', '/sw.js', '/manifest', '/favicon', '/robots.txt')


def _is_open(p):
    # match whole path segments, so '/administrator' or '/accessible-notes' are NOT open just because of their prefix
    return any(p == o.rstrip('/') or p.startswith(o.rstrip('/') + '/') or (o in ('/sw.js', '/robots.txt') and p == o)
               or (o in ('/manifest', '/favicon') and p.startswith(o + '.')) for o in OPEN_PREFIXES)


def _table():
    if not _ready:
        AppSetting.__table__.create(db.engine, checkfirst=True)
        _ready.append(1)


def code_hash():
    """Current stored hash ('' = gate off). Cached for 30 s to avoid a DB hit on every request."""
    if time.time() - _cache['t'] > 30:
        _table()
        row = db.session.get(AppSetting, KEY)
        _cache['v'], _cache['t'] = (row.value if row else ''), time.time()
    return _cache['v'] or ''


def hash_code(code, stored=None):
    """'s1$<salt>$<hex>' with a random salt kept in the row, so changing SECRET_KEY does not lock everyone out.
    Hashes from the first version (salted with SECRET_KEY, no prefix) are still checked."""
    if stored and not stored.startswith('s1$'):
        return hashlib.pbkdf2_hmac('sha256', code.encode(), str(current_app.config['SECRET_KEY']).encode(), 200_000).hex()
    salt = stored.split('$')[1] if stored else secrets.token_hex(16)
    return 's1$' + salt + '$' + hashlib.pbkdf2_hmac('sha256', code.encode(), salt.encode(), 200_000).hex()


def check_code(code, stored):
    return bool(stored) and hmac.compare_digest(hash_code(code, stored), stored)


def set_code(code):
    _table()
    row = db.session.get(AppSetting, KEY) or AppSetting(key=KEY)
    row.value = hash_code(code) if code else ''
    db.session.merge(row)
    db.session.commit()
    _cache['t'] = 0


def pass_token(h):
    return hmac.new(str(current_app.config['SECRET_KEY']).encode(), ('access:' + h).encode(), 'sha256').hexdigest()


def has_pass():
    h = code_hash()
    if not h:
        return True
    return hmac.compare_digest(request.cookies.get(COOKIE, ''), pass_token(h))


def init_access_gate(app):
    @app.before_request
    def _gate():
        p = request.path
        if request.endpoint == 'static' or _is_open(p) or app.config.get('TESTING') and not app.config.get('ACCESS_GATE_IN_TESTS'):
            return None
        if has_pass():
            return None
        if request.method != 'GET' or '/api' in p or p.endswith('.json'):
            return jsonify(error='access code required'), 401
        nxt = request.full_path if request.query_string else p
        return redirect(url_for('access.enter', next=nxt))
