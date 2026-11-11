"""Sign up / sign in / sign out / password reset for learners.

How it works: the app keeps all personal state under the ``device_id`` cookie. An account stores one device id.
Signing up adopts the current browser's device id (so existing progress is kept). Signing in on another device
switches that browser's cookie to the account's device id, so every device of the learner shares the same state.
Signing out gives the browser a fresh, empty device id.
"""
import re
import secrets
import time
from datetime import datetime

from flask import Blueprint, current_app, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from ..account_models import LearnerAccount
from ..db import db
from ..services.device import NEW_FORMAT
from sqlalchemy.exc import IntegrityError

bp = Blueprint('account', __name__, url_prefix='/account')
USER_RE = re.compile(r'^[a-z0-9_.]{3,30}$')
_ready = []
_FAILS = {}
MAX_FAILS, LOCK_SECONDS = 5, 300
_DUMMY = generate_password_hash(secrets.token_urlsafe(16))


def _table():
    if not _ready:
        LearnerAccount.__table__.create(db.engine, checkfirst=True)
        _ready.append(1)


def current_account():
    _table()
    # The device cookie lasts a year and is the real link to the account; the session flag may expire sooner.
    dev = getattr(g, 'device_id', None)
    return LearnerAccount.query.filter_by(device_id=dev).first() if dev else None


def _use_device(dev):
    """Make this browser use ``dev`` as its device id from now on (cookie re-issued in after_request)."""
    g.device_id, g.device_is_new = dev, True


def _safe_next(t):
    # browsers drop tabs/newlines inside URLs, so "/\t/evil.com" would become "//evil.com": refuse any control char or space
    if not t or not t.startswith('/') or t.startswith('//') or '\\' in t or any(ord(ch) < 33 or ord(ch) == 127 for ch in t):
        return None
    return t


def _locked(key):
    r = _FAILS.get(key)
    return int(r['until'] - time.time()) + 1 if r and r['until'] > time.time() else 0


def _fail(key):
    if len(_FAILS) > 10000:             # keep the in-memory table bounded
        now = time.time()
        for k in [k for k, v in _FAILS.items() if v['until'] < now]:
            _FAILS.pop(k, None)
    r = _FAILS.setdefault(key, {'n': 0, 'until': 0})
    r['n'] += 1
    if r['n'] >= MAX_FAILS:
        r['until'], r['n'] = time.time() + LOCK_SECONDS, 0


def _move_device(acct, new_id):
    """Give the account a fresh device id and move every learner row to it. Old devices keep the old id,
    so they no longer see the account (used on password reset and to replace weak legacy ids)."""
    old = acct.device_id
    for t in db.metadata.sorted_tables:
        if 'device_id' in t.c and t.name != LearnerAccount.__tablename__:
            try:
                db.session.execute(t.update().where(t.c.device_id == old).values(device_id=new_id))
            except Exception:          # table not created yet on this database
                db.session.rollback()
    acct.device_id = new_id


def _start_session(acct):
    csrf = session.get('_csrf')
    session.clear()                       # new session on login (no fixation)
    if csrf:
        session['_csrf'] = csrf
    session['acct'] = acct.id
    session.permanent = True


def _recovery_code():
    a = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'
    raw = ''.join(secrets.choice(a) for _ in range(12))
    return '-'.join(raw[i:i + 4] for i in (0, 4, 8))


def _norm_code(c):
    return re.sub(r'[^A-Z0-9]', '', (c or '').upper())


@bp.get('/')
def home():
    return render_template('ds/account.html', mode='home', acct=current_account(), nxt=_safe_next(request.args.get('next')), fresh=request.args.get('fresh') == '1')


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    _table()
    nxt = _safe_next(request.values.get('next'))
    if request.method == 'GET':
        return render_template('ds/account.html', mode='signup', acct=current_account(), nxt=nxt)
    user = (request.form.get('username') or '').strip().lower()
    pw, pw2 = request.form.get('password') or '', request.form.get('password2') or ''
    err = None
    if not USER_RE.match(user):
        err = 'Username: 3–30 characters, lowercase letters, numbers, dot or underscore.'
    elif len(pw) < 8:
        err = 'Password must be at least 8 characters.'
    elif pw != pw2:
        err = 'The two passwords do not match.'
    elif LearnerAccount.query.filter_by(username=user).first():
        err = 'That username is taken. Try another.'
    elif LearnerAccount.query.filter_by(device_id=g.device_id).first():
        err = 'This device already belongs to an account. Sign in instead, or sign out first.'
    if err:
        return render_template('ds/account.html', mode='signup', error=err, username=user, nxt=nxt), 400
    if not NEW_FORMAT.match(g.device_id or ''):          # old low-entropy id: mint a strong one and move the data
        strong = secrets.token_urlsafe(24)
        for t in db.metadata.sorted_tables:
            if 'device_id' in t.c and t.name != LearnerAccount.__tablename__:
                try:
                    db.session.execute(t.update().where(t.c.device_id == g.device_id).values(device_id=strong))
                except Exception:
                    db.session.rollback()
        _use_device(strong)
    code = _recovery_code()
    acct = LearnerAccount(username=user, pw_hash=generate_password_hash(pw), recovery_hash=generate_password_hash(_norm_code(code)),
                          device_id=g.device_id, last_login_at=datetime.utcnow())
    db.session.add(acct)
    try:
        db.session.commit()
    except IntegrityError:                # two signups raced for the same username or device
        db.session.rollback()
        return render_template('ds/account.html', mode='signup', error='That username is taken. Try another.', username=user, nxt=nxt), 400
    _start_session(acct)
    return render_template('ds/account.html', mode='created', acct=acct, code=code, nxt=nxt)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    _table()
    nxt = _safe_next(request.values.get('next'))
    if request.method == 'GET':
        return render_template('ds/account.html', mode='login', acct=current_account(), nxt=nxt)
    user = (request.form.get('username') or '').strip().lower()
    key = (request.remote_addr or '?') + '|' + user
    wait = _locked(key)
    if wait:
        return render_template('ds/account.html', mode='login', error=f'Too many attempts. Try again in {wait} seconds.', username=user, nxt=nxt), 429
    acct = LearnerAccount.query.filter_by(username=user).first()
    # check a hash even for unknown usernames so response time does not reveal which usernames exist
    if not check_password_hash(acct.pw_hash if acct else _DUMMY, request.form.get('password') or '') or not acct:
        _fail(key)
        return render_template('ds/account.html', mode='login', error='Wrong username or password.', username=user, nxt=nxt), 401
    _FAILS.pop(key, None)
    acct.last_login_at = datetime.utcnow()
    db.session.commit()
    _start_session(acct)
    _use_device(acct.device_id)
    return redirect(url_for('account.home', fresh=1, next=nxt))


@bp.post('/logout')
def logout():
    csrf = session.get('_csrf')
    session.clear()
    if csrf:
        session['_csrf'] = csrf
    _use_device(secrets.token_urlsafe(24))
    return redirect(url_for('account.home', fresh=1))


@bp.route('/reset', methods=['GET', 'POST'])
def reset():
    _table()
    if request.method == 'GET':
        return render_template('ds/account.html', mode='reset')
    user = (request.form.get('username') or '').strip().lower()
    key = (request.remote_addr or '?') + '|reset|' + user
    wait = _locked(key)
    if wait:
        return render_template('ds/account.html', mode='reset', error=f'Too many attempts. Try again in {wait} seconds.', username=user), 429
    acct = LearnerAccount.query.filter_by(username=user).first()
    pw, pw2 = request.form.get('password') or '', request.form.get('password2') or ''
    if not acct or not check_password_hash(acct.recovery_hash, _norm_code(request.form.get('code'))):
        _fail(key)
        return render_template('ds/account.html', mode='reset', error='Username or recovery code is wrong.', username=user), 401
    if len(pw) < 8 or pw != pw2:
        return render_template('ds/account.html', mode='reset', error='New password: at least 8 characters, typed the same twice.', username=user), 400
    code = _recovery_code()                 # the old code is used up; issue a new one
    acct.pw_hash = generate_password_hash(pw)
    acct.recovery_hash = generate_password_hash(_norm_code(code))
    _move_device(acct, secrets.token_urlsafe(24))     # every other device is signed out
    db.session.commit()
    _FAILS.pop(key, None)
    _start_session(acct)
    _use_device(acct.device_id)
    return render_template('ds/account.html', mode='created', acct=acct, code=code, reset=True, fresh=True)
