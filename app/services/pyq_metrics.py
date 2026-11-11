"""PYQ coverage metrics for the Polity recall decks (subject page + recall hub).

Bank   = distinct question ids across content/polity/g2/**/PYQ-Set.json (exam name from the bank).
Card's PYQs = ids in its exam.pyqs (kind == 'pyq', id or qid) ∪ pyq_map.json[card id], limited to bank ids.
Cached on a version string built from recall_decks.data_version() + PYQ bank mtimes, so edits show up without a restart.
"""
import hashlib
import json
from pathlib import Path

from . import recall_decks as _recall

ROOT = Path(__file__).resolve().parents[2] / 'content' / 'polity' / 'g2'
MAP_FILE = _recall.DIR / 'pyq_map.json'

# (id, label_en, label_te) — display order
FAMILIES = [
    ('appsc', 'APPSC', 'APPSC'),
    ('upsc', 'UPSC', 'UPSC'),
    ('tspsc', 'TSPSC / TGPSC', 'TSPSC / TGPSC'),
    ('aphc', 'AP High Court', 'AP హైకోర్టు'),
    ('other', 'Others (SSC, RRB…)', 'ఇతరాలు (SSC, RRB…)'),
]
APPSC_GROUPS = [('APPSC Group I', 'Group 1', 'గ్రూప్ 1'), ('APPSC Group II', 'Group 2', 'గ్రూప్ 2'), ('APPSC Group IV', 'Group 4', 'గ్రూప్ 4')]


def family(exam):
    e = _recall.exam_label(exam).upper()
    if e.startswith('APPSC'):
        return 'appsc'
    if e.startswith('UPSC'):
        return 'upsc'
    if e.startswith(('TSPSC', 'TGPSC')):
        return 'tspsc'
    if 'HIGH COURT' in e:
        return 'aphc'
    return 'other'


def bank_files():
    return sorted(ROOT.glob('**/PYQ-Set.json'))


def bank():
    """{pyq id: exam name} — first occurrence wins (an id can sit in two sub-chapter sets)."""
    out = {}
    for f in bank_files():
        try:
            data = json.loads(f.read_text(encoding='utf-8'))
        except (ValueError, OSError):
            continue
        for q in data.get('questions', []) if isinstance(data, dict) else data:
            if q.get('id'):
                out.setdefault(q['id'], q.get('exam') or '')
    return out


def card_pyqs(card, pmap, known):
    ids = {q.get('id') or q.get('qid') for q in ((card.get('exam') or {}).get('pyqs') or []) if q.get('kind') == 'pyq'}
    ids |= set(pmap.get(card['id']) or [])
    return {i for i in ids if i in known}


def compute():
    b = bank()
    try:
        pmap = json.loads(MAP_FILE.read_text(encoding='utf-8'))
    except (ValueError, OSError):
        pmap = {}
    appsc = {i for i, e in b.items() if family(e) == 'appsc'}

    def stats(ids_by_card, keep):
        ids, n = set(), 0
        for s in ids_by_card:
            s = s & keep
            ids |= s
            n += bool(s)
        return {'pyqs': len(ids), 'cards': n, 'ids': ids}

    decks, mapped = [], set()
    for d in _recall.all_decks():
        per = [card_pyqs(c, pmap, b) for c in _recall.items(d['id'])]
        a, p = stats(per, set(b)), stats(per, appsc)
        mapped |= a['ids']
        decks.append({'id': d['id'], 'title_en': d['title_en'], 'title_te': d['title_te'], 'total_cards': d['count'],
                      'pyqs': a['pyqs'], 'cards': a['cards'], 'appsc_pyqs': p['pyqs'], 'appsc_cards': p['cards'], '_ids': a['ids']})

    fam_rows = []
    for fid, en, te in FAMILIES:
        keep = {i for i, e in b.items() if family(e) == fid}
        if not keep:
            continue
        fam_rows.append({'id': fid, 'en': en, 'te': te, 'bank': len(keep), 'mapped': len(keep & mapped),
                         'decks': [len(keep & d['_ids']) for d in decks]})
    groups = []
    for name, en, te in APPSC_GROUPS:
        keep = {i for i, e in b.items() if e == name}
        if keep:
            groups.append({'en': en, 'te': te, 'bank': len(keep), 'mapped': len(keep & mapped), 'decks': [len(keep & d['_ids']) for d in decks]})
    for d in decks:
        d.pop('_ids')
    return {'total': len(b), 'mapped': len(mapped), 'appsc_total': len(appsc), 'appsc_mapped': len(appsc & mapped),
            'decks': decks, 'by_deck': {d['id']: d for d in decks}, 'families': fam_rows, 'appsc_groups': groups}


def version():
    h = hashlib.sha1(_recall.data_version().encode())
    for f in bank_files():
        try:
            st = f.stat()
            h.update(f'{f}:{st.st_mtime_ns}:{st.st_size};'.encode())
        except OSError:
            continue
    return h.hexdigest()[:12]


_CACHE = {'v': None, 'm': None}


def metrics():
    _recall.refresh()
    v = version()
    if _CACHE['v'] != v:
        _CACHE.update(v=v, m=compute())
    return _CACHE['m']
