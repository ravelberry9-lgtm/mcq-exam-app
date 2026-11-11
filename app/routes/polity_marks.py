"""Highlights, underlines and bookmarks for Polity pages and cards (per device)."""
from datetime import datetime
from flask import Blueprint, jsonify, request, render_template
from ..db import db
from ..polity_models import PolityMark
from ..services.device import device_id

bp = Blueprint('polity_marks', __name__, url_prefix='/learn/my-saved')
_ready = []
MAX_MARKS = 500
MAX_BODY = 256 * 1024
KINDS = {'hl', 'ul'}
COLORS = {'yellow', 'green', 'pink', 'blue', 'red', 'purple'}


def _table():
    if not _ready:
        PolityMark.__table__.create(db.engine, checkfirst=True)
        _ready.append(1)


def _clean(marks):
    out = []
    if not isinstance(marks, list):
        return out
    for m in marks[:MAX_MARKS]:
        if not isinstance(m, dict):
            continue
        try:
            s, e = int(m['s']), int(m['e'])
        except (KeyError, TypeError, ValueError):
            continue
        if 0 <= s < e <= 200000 and m.get('k') in KINDS and m.get('c') in COLORS:
            out.append({'s': s, 'e': e, 'k': m['k'], 'c': m['c'], 't': str(m.get('t', ''))[:200]})
    return out


@bp.get('/api')
def get_marks():
    _table()
    key = (request.args.get('key') or '')[:200]
    row = db.session.get(PolityMark, (device_id(), key)) if key else None
    return jsonify(marks=row.marks if row else [], bookmarked=bool(row and row.bookmarked))


@bp.post('/api')
def save_marks():
    _table()
    if (request.content_length or 0) > MAX_BODY:
        return jsonify(ok=False), 413
    d = request.get_json(silent=True)
    if not isinstance(d, dict):
        return jsonify(ok=False), 400
    key = str(d.get('key') or '')[:200]
    if not key:
        return jsonify(ok=False), 400
    row = db.session.get(PolityMark, (device_id(), key))
    if row is None:
        row = PolityMark(device_id=device_id(), key=key, marks=[], bookmarked=False)
        db.session.add(row)
    if 'marks' in d:
        row.marks = _clean(d['marks'])
    if 'bookmarked' in d:
        row.bookmarked = bool(d['bookmarked'])
    if d.get('title'):
        row.title = str(d['title'])[:300]
    u = str(d.get('url') or '')
    if u.startswith('/learn/'):
        row.url = u[:500]
    row.updated_at = datetime.utcnow()
    db.session.commit()
    return jsonify(ok=True)


@bp.get('/')
def saved():
    _table()
    rows = [r for r in PolityMark.query.filter_by(device_id=device_id()).order_by(PolityMark.updated_at.desc())
            if (r.bookmarked or r.marks) and r.url]
    return render_template('ds/polity_marks.html', rows=rows)
