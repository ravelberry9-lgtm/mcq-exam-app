"""PYQ coverage metrics on the Polity subject page / recall hub match a direct recount of the source files."""
import glob
import json
import os
from pathlib import Path

from app.services import pyq_metrics as P
from app.services import recall_decks as R

G2 = Path(__file__).resolve().parents[1] / 'content' / 'polity' / 'g2'


def _recount():
    bank = {}
    for f in sorted(glob.glob(str(G2 / '**' / 'PYQ-Set.json'), recursive=True)):
        for q in json.load(open(f, encoding='utf-8'))['questions']:
            bank.setdefault(q['id'], q['exam'])
    pmap = json.load(open(G2 / 'recall_decks' / 'pyq_map.json', encoding='utf-8'))
    appsc = {i for i, e in bank.items() if 'APPSC' in e}
    out = {}
    for deck in ('articles', 'amendments', 'cases'):
        ids, appsc_ids, n, na = set(), set(), 0, 0
        for c in R.items(deck):
            s = {q.get('id') or q.get('qid') for q in (c.get('exam') or {}).get('pyqs', []) if q.get('kind') == 'pyq'}
            s = (s | set(pmap.get(c['id'], []))) & set(bank)
            ids |= s; appsc_ids |= s & appsc; n += bool(s); na += bool(s & appsc)
        out[deck] = (len(ids), n, len(appsc_ids), na, ids)
    return bank, appsc, out


def test_metrics_match_direct_recount():
    m = P.metrics()
    bank, appsc, out = _recount()
    allm = set().union(*(v[4] for v in out.values()))
    assert m['total'] == len(bank) and m['appsc_total'] == len(appsc)
    assert m['mapped'] == len(allm) and m['appsc_mapped'] == len(allm & appsc)
    for d in m['decks']:
        assert (d['pyqs'], d['cards'], d['appsc_pyqs'], d['appsc_cards']) == out[d['id']][:4]
        assert d['total_cards'] == len(R.items(d['id']))
    assert sum(f['bank'] for f in m['families']) == len(bank)
    assert {f['id']: f['bank'] for f in m['families']}['appsc'] == len(appsc)
    assert sum(g['bank'] for g in m['appsc_groups']) == len(appsc)


def test_metrics_refresh_on_file_change(tmp_path, monkeypatch):
    m1 = P.metrics()
    f = next(iter(P.bank_files()))
    st = f.stat()
    os.utime(f, ns=(st.st_atime_ns, st.st_mtime_ns + 10_000_000))
    try:
        v = P.version()
        assert v != P._CACHE['v'] or m1 is not P._CACHE['m']
        assert P.metrics()['total'] == m1['total'] and P._CACHE['v'] == v
    finally:
        os.utime(f, ns=(st.st_atime_ns, st.st_mtime_ns))


def test_pages_show_pyq_metrics(client, app):
    app.config['POLITY_UNIT6_ENABLED'] = True
    m = P.metrics()
    for url in ('/learn/polity/unit6/', '/learn/polity/unit6/recall'):
        html = client.get(url).get_data(as_text=True)
        assert 'PYQ వివరాలు' in html and 'PYQ details' in html
        assert html.count('class="pq-tile"') == 3
        assert f'<b>{m["total"]}</b>' in html and f'<b>{m["appsc_total"]}</b> APPSC' in html
