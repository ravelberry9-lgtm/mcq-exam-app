"""Enter the app access code (once per device)."""
import time
from flask import Blueprint, make_response, redirect, render_template, request, current_app
import hmac
from ..services import access_gate as ag

bp = Blueprint('access', __name__, url_prefix='/access')
_FAILS = {}


def _safe_next(t):
    # browsers drop tabs/newlines inside URLs ('/\t/evil.com' -> '//evil.com'), so refuse every control char and space
    ok = t and t.startswith('/') and not t.startswith('//') and '\\' not in t and not any(ord(c) < 33 or ord(c) == 127 for c in t)
    return t if ok else '/'


@bp.route('/', methods=['GET', 'POST'])
def enter():
    nxt = _safe_next(request.values.get('next'))
    h = ag.code_hash()
    if not h or ag.has_pass():
        return redirect(nxt)
    if request.method == 'GET':
        return render_template('ds/access.html', nxt=nxt)
    ip = request.remote_addr or '?'
    r = _FAILS.get(ip)
    if r and r['until'] > time.time():
        return render_template('ds/access.html', nxt=nxt, error=f'Too many wrong tries. Wait {int(r["until"]-time.time())+1} seconds.'), 429
    code = ''.join(ch for ch in (request.form.get('code') or '') if ch.isdigit())
    if len(code) != 6 or not ag.check_code(code, h):
        r = _FAILS.setdefault(ip, {'n': 0, 'until': 0}); r['n'] += 1
        if r['n'] >= 5:
            r['until'], r['n'] = time.time() + 300, 0
        return render_template('ds/access.html', nxt=nxt, error='That code is not right.'), 401
    _FAILS.pop(ip, None)
    resp = make_response(redirect(nxt))
    resp.set_cookie(ag.COOKIE, ag.pass_token(h), max_age=ag.TEN_YEARS, httponly=True, samesite='Lax',
                    secure=bool(current_app.config.get('SESSION_COOKIE_SECURE')))
    return resp
