"""PYQ coverage metrics for the Polity recall decks (subject page + recall hub).

Bank   = the master Indian Polity PYQ bank, content/polity/pyq_bank/indian_polity_pyq_bank_v3.71.0.json.
         Every record counts (a question asked again in another exam/year is a separate record);
         repeat_groups.json clusters records of the same question, so 'distinct' counts each question once.
         The app's unit-6 PYQ-Set copies are NOT counted: they are the same master records (source_record_id).
Card's PYQs = master record ids in its exam.pyqs (master_id / master_ids, or id 'PYQ-<record_id>')
              ∪ pyq_map.json[card id], limited to bank ids.
waiting_for_card.json = records about an Article / Schedule / Preamble with no card yet.
Units  = each bank record's syllabus unit (6-10) from the chapter PYQ files (PYQ-Set.json / PYQ-Bank-Set.json,
         source_record_id); records in no chapter file are 'Not in Units 6-10'.
Cached on a version string built from recall_decks.data_version() + bank and chapter PYQ file mtimes.
"""
import hashlib
import json
from pathlib import Path

from . import recall_decks as _recall

ROOT = Path(__file__).resolve().parents[2] / 'content' / 'polity'
BANK_DIR = ROOT / 'pyq_bank'
BANK_FILE = BANK_DIR / 'indian_polity_pyq_bank_v3.71.0.json'
GROUPS_FILE = BANK_DIR / 'repeat_groups.json'
WAITING_FILE = BANK_DIR / 'waiting_for_card.json'
MAP_FILE = _recall.DIR / 'pyq_map.json'

# (id, label_en, label_te) — display order
FAMILIES = [
    ('appsc', 'APPSC', 'APPSC'),
    ('upsc', 'UPSC', 'UPSC'),
    ('aphc', 'AP High Court', 'AP హైకోర్టు'),
    ('ssc', 'SSC', 'SSC'),
    ('other', 'Others (TSPSC/TGPSC, RRB)', 'ఇతరాలు (TSPSC/TGPSC, RRB)'),
]
APPSC_GROUPS = [('APPSC Group I', 'Group 1', 'గ్రూప్ 1'), ('APPSC Group II', 'Group 2', 'గ్రూప్ 2'), ('APPSC Group IV', 'Group 4', 'గ్రూప్ 4')]
APPSC_OTHER = ('Other APPSC posts (Lecturers, Forest, DEO, JA, Gazetted…)', 'ఇతర APPSC పోస్టులు (లెక్చరర్లు, అటవీ, DEO, JA, గెజిటెడ్…)')


def family(exam):
    e = _recall.exam_label(exam).upper()
    if e.startswith('APPSC'):
        return 'appsc'
    if e.startswith('UPSC'):
        return 'upsc'
    if 'HIGH COURT' in e:
        return 'aphc'
    if e.startswith('SSC'):
        return 'ssc'
    return 'other'


G2 = ROOT / 'g2'
UNIT_PYQ_FILES = ('PYQ-Set.json', 'PYQ-Bank-Set.json')
UNITS = (6, 7, 8, 9, 10)


def unit_files():
    return sorted(f for name in UNIT_PYQ_FILES for f in G2.glob('*.*/*/' + name))


def bank_files():
    return [f for f in (BANK_FILE, GROUPS_FILE, WAITING_FILE) if f.exists()] + unit_files()


def unit_of_records():
    """{bank record_id: unit} from the chapter PYQ files; first file in sorted order wins."""
    out = {}
    for f in unit_files():
        try:
            unit = int(f.parent.name.split('.')[0])
        except ValueError:
            continue
        for q in (_load(f, {}).get('questions') or []):
            rid = q.get('source_record_id') or _rid(q.get('id'))
            if rid and unit in UNITS:
                out.setdefault(rid, unit)
    return out


def _load(f, default):
    try:
        return json.loads(f.read_text(encoding='utf-8'))
    except (ValueError, OSError):
        return default


def bank():
    """{record_id: exam} for every master record that is not marked duplicate_of another record
    and not excluded by the key audit (key_audit.excluded, e.g. a fabricated question)."""
    return {r['record_id']: r.get('exam') or '' for r in _load(BANK_FILE, [])
            if not (r.get('duplicate_of') or '').strip() and not (r.get('key_audit') or {}).get('excluded')}


def group_of(b):
    """{record_id: question id}; records outside a repeat group are their own question."""
    g = {rid: rid for rid in b}
    for gid, rids in (_load(GROUPS_FILE, {}).get('groups') or {}).items():
        for rid in rids:
            if rid in g:
                g[rid] = gid
    return g


def _rid(x):
    return x[4:] if x and x.startswith('PYQ-') else x


def card_pyqs(card, pmap, known):
    ids = set()
    for q in ((card.get('exam') or {}).get('pyqs') or []):
        if q.get('kind') != 'pyq':
            continue
        ids |= set(q.get('master_ids') or [])
        ids.add(q.get('master_id') or _rid(q.get('id') or q.get('qid')))
    ids |= {_rid(x) for x in pmap.get(card['id']) or []}
    return {i for i in ids if i in known}


def compute():
    b = bank()
    g = group_of(b)
    pmap = _load(MAP_FILE, {})
    waiting = set((_load(WAITING_FILE, {}).get('records') or {})) & set(b)
    appsc = {i for i, e in b.items() if family(e) == 'appsc'}

    def distinct(ids):
        return len({g[i] for i in ids})

    def repeated(ids):
        n = {}
        for i in ids:
            n[g[i]] = n.get(g[i], 0) + 1
        return sum(1 for v in n.values() if v > 1)

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
                      'pyqs': a['pyqs'], 'distinct': distinct(a['ids']), 'repeated': repeated(a['ids']), 'cards': a['cards'],
                      'appsc_pyqs': p['pyqs'], 'appsc_cards': p['cards'], '_ids': a['ids']})

    fam_rows = []
    for fid, en, te in FAMILIES:
        keep = {i for i, e in b.items() if family(e) == fid}
        if keep:
            fam_rows.append({'id': fid, 'en': en, 'te': te, 'bank': len(keep), 'mapped': len(keep & mapped),
                             'decks': [len(keep & d['_ids']) for d in decks]})
    groups = []
    for name, en, te in APPSC_GROUPS:
        keep = {i for i, e in b.items() if e == name}
        if keep:
            groups.append({'en': en, 'te': te, 'bank': len(keep), 'mapped': len(keep & mapped), 'decks': [len(keep & d['_ids']) for d in decks]})
    named = {name for name, _, _ in APPSC_GROUPS}
    keep = {i for i in appsc if b[i] not in named}
    if keep:
        groups.append({'en': APPSC_OTHER[0], 'te': APPSC_OTHER[1], 'bank': len(keep), 'mapped': len(keep & mapped),
                       'decks': [len(keep & d['_ids']) for d in decks]})
    for d in decks:
        d.pop('_ids')
    where = unit_of_records()

    def row(label, keep):
        return {'en': label, 'total': len(keep), 'appsc': len(keep & appsc),
                'groups': [len({i for i in keep if b[i] == name}) for name, _, _ in APPSC_GROUPS]
                + [len({i for i in keep & appsc if b[i] not in {n for n, _, _ in APPSC_GROUPS}})],
                'families': [len({i for i in keep if family(b[i]) == fid}) for fid, _, _ in FAMILIES if fid != 'appsc']}
    unit_rows = [row(f'Unit {u}', {i for i in b if where.get(i) == u}) for u in UNITS]
    unit_rows.append(row('Not in Units 6-10', {i for i in b if i not in where}))
    return {'total': len(b), 'distinct_total': distinct(b), 'repeated_total': repeated(b),
            'mapped': len(mapped), 'distinct_mapped': distinct(mapped),
            'appsc_total': len(appsc), 'appsc_mapped': len(appsc & mapped),
            'waiting': len(waiting), 'waiting_unmapped': len(waiting - mapped),
            'decks': decks, 'by_deck': {d['id']: d for d in decks}, 'families': fam_rows, 'appsc_groups': groups,
            'units': unit_rows, 'unit_group_labels': ['G1', 'G2', 'G4', 'Other APPSC'],
            'unit_family_labels': ['UPSC', 'AP HC', 'SSC', 'Other']}


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
