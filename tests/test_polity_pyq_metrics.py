"""PYQ coverage metrics on the Polity subject page / recall hub match a direct recount of the source files."""
import collections
import glob
import json
import os
from pathlib import Path

import markupsafe

from app.services import pyq_metrics as P
from app.services import recall_decks as R

G2 = Path(__file__).resolve().parents[1] / 'content' / 'polity' / 'g2'
BANK = Path(__file__).resolve().parents[1] / 'content' / 'polity' / 'pyq_bank'


def _rid(x):
    return x[4:] if x and x.startswith('PYQ-') else x


def _recount():
    bank = {r['record_id']: r['exam'] for r in json.load(open(BANK / 'indian_polity_pyq_bank_v3.70.0.json', encoding='utf-8'))
            if not r.get('duplicate_of') and not (r.get('key_audit') or {}).get('excluded')}
    grp = {rid: rid for rid in bank}
    for gid, rids in json.load(open(BANK / 'repeat_groups.json', encoding='utf-8'))['groups'].items():
        for rid in rids:
            grp[rid] = gid
    pmap = json.load(open(G2 / 'recall_decks' / 'pyq_map.json', encoding='utf-8'))
    appsc = {i for i, e in bank.items() if e.startswith('APPSC')}
    out = {}
    for deck in ('articles', 'amendments', 'cases'):
        ids, n, na = set(), 0, 0
        for c in R.items(deck):
            s = set()
            for q in (c.get('exam') or {}).get('pyqs', []):
                if q.get('kind') == 'pyq':
                    s |= set(q.get('master_ids') or []) | {q.get('master_id') or _rid(q.get('id'))}
            s = (s | {_rid(x) for x in pmap.get(c['id'], [])}) & set(bank)
            ids |= s; n += bool(s); na += bool(s & appsc)
        rep = collections.Counter(grp[i] for i in ids)
        out[deck] = (len(ids), n, len(ids & appsc), na, len(rep), sum(1 for v in rep.values() if v > 1), ids)
    return bank, grp, appsc, out


def test_metrics_match_direct_recount():
    m = P.metrics()
    bank, grp, appsc, out = _recount()
    allm = set().union(*(v[-1] for v in out.values()))
    assert m['total'] == len(bank) == 1457  # 1458 records minus 1 excluded by the key audit
    assert m['distinct_total'] == len(set(grp.values())) < m['total']
    assert m['appsc_total'] == len(appsc)
    assert m['mapped'] == len(allm) and m['appsc_mapped'] == len(allm & appsc)
    assert m['distinct_mapped'] == len({grp[i] for i in allm})
    for d in m['decks']:
        assert (d['pyqs'], d['cards'], d['appsc_pyqs'], d['appsc_cards'], d['distinct'], d['repeated']) == out[d['id']][:6]
        assert d['total_cards'] == len(R.items(d['id']))
    assert sum(f['bank'] for f in m['families']) == len(bank)
    assert {f['id']: f['bank'] for f in m['families']}['appsc'] == len(appsc)
    assert sum(g['bank'] for g in m['appsc_groups']) == len(appsc)
    waiting = set(json.load(open(BANK / 'waiting_for_card.json', encoding='utf-8'))['records'])
    assert m['waiting'] == len(waiting & set(bank)) and m['waiting_unmapped'] == len(waiting - allm)


def test_app_copies_not_counted_twice():
    """Each unit-6 PYQ-Set question is a master record; card entries reuse the master id."""
    bank = {r['record_id'] for r in json.load(open(BANK / 'indian_polity_pyq_bank_v3.70.0.json', encoding='utf-8'))}
    for f in glob.glob(str(G2 / '**' / 'PYQ-Set.json'), recursive=True):
        for q in json.load(open(f, encoding='utf-8'))['questions']:
            assert q['source_record_id'] in bank
    excluded = {r['record_id'] for r in json.load(open(BANK / 'indian_polity_pyq_bank_v3.70.0.json', encoding='utf-8'))
                if (r.get('key_audit') or {}).get('excluded')}
    assert P.metrics()['total'] == len(bank) - len(excluded)


def test_repeats_grouped_and_untranslated_shows_english(client, app):
    app.config['POLITY_UNIT6_ENABLED'] = True
    cards = [c for d in ('articles', 'amendments', 'cases') for c in R.items(d)]
    rep = next(c for c in cards if any(len(q.get('asked') or []) > 1 for q in (c.get('exam') or {}).get('pyqs', [])))
    html = client.get(f"/learn/polity/unit6/recall/{rep["deck"]}/card/{rep["id"]}").get_data(as_text=True)
    assert 'ct-rep' in html and 'Asked ' in html
    a21 = next(c for c in R.items('articles') if c['front_short'] == '21')
    q = next(q for q in a21['exam']['pyqs'] if q.get('kind') == 'pyq' and not q.get('q_te')) if any(
        q.get('kind') == 'pyq' and not q.get('q_te') for q in a21['exam']['pyqs']) else None
    if q:
        html = client.get(f"/learn/polity/unit6/recall/articles/card/{a21["id"]}").get_data(as_text=True)
        assert html.count(str(markupsafe.escape(q['q_en']))) >= 2  # te slot falls back to English


def test_metrics_refresh_on_file_change(tmp_path, monkeypatch):
    m1 = P.metrics()
    f = P.BANK_FILE
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
        assert 'PYQ details' in html and 'PYQ వివరాలు' not in html
        assert html.count('class="pq-tile"') == 3
        assert f'<b>{m["total"]}</b>' in html and f'<b>{m["appsc_total"]}</b> APPSC' in html
