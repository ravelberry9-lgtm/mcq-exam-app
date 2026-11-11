import json
from bs4 import BeautifulSoup
from app.services import recall_decks as R

B = '/learn/polity/unit6'


def _data(client):
    r = client.get(B + '/recall/trees')
    assert r.status_code == 200
    s = BeautifulSoup(r.data, 'html.parser')
    return s, json.loads(s.select_one('#tr-data').string)


def test_polity_trees_route_and_order(client, app):
    app.config['POLITY_UNIT6_ENABLED'] = True
    s, d = _data(client)
    assert {b['data-tab'] for b in s.select('[role=tab]')} == {'am', 'case', 'both', 'lines'}
    ys = [n['y'] for n in d['nodes']]
    assert ys == sorted(ys) and d['counts']['am'] == len(R.items('amendments')) and d['counts']['case'] == len(R.items('cases'))
    ams = [n['no'] for n in d['nodes'] if n['k'] == 'am' and n.get('no')]
    assert ams == sorted(ams)


def test_polity_trees_nodes_link_to_real_cards(client, app):
    app.config['POLITY_UNIT6_ENABLED'] = True
    _, d = _data(client)
    have = {'am': {c['id'] for c in R.items('amendments')}, 'case': {c['id'] for c in R.items('cases')}}
    ids = {n['id'] for n in d['nodes']}
    for n in d['nodes']:
        assert n['id'] in have[n['k']]
        for r in n.get('r', []) + [[x] for x in n.get('ln', [])]:
            assert r[0] in ids
    deep = client.get(B + '/recall/amendments?open=AM-024&back=trees:both')
    assert deep.status_code == 200 and b'data-back-url="/learn/polity/unit6/recall/trees#both"' in deep.data
    ch = client.get(B + '/recall/trees/chains.json').get_json()
    assert ch and all(st['id'] is None or st['id'] in ids for c in ch for st in c['st'])


def test_polity_trees_tile_on_subject_and_hub(client, app):
    app.config['POLITY_UNIT6_ENABLED'] = True
    for path in (B + '/', B + '/recall'):
        s = BeautifulSoup(client.get(path).data, 'html.parser')
        a = s.select_one('a[href="/learn/polity/unit6/recall/trees"]')
        assert a and 'Trees' in a.get_text() and 'amendments' in a.get_text() and 'cases' in a.get_text()


def test_polity_trees_compact_controls_old_cases_and_relations(client, app):
    app.config['POLITY_UNIT6_ENABLED'] = True
    s, d = _data(client)
    assert '1950–' in s.select_one('.tr-sub').get_text()
    assert s.select_one('#tr-fbtn') and s.select_one('#tr-sheet #tr-pyq') and s.select_one('#tr-sheet #tr-old')
    old = [n for n in d['nodes'] if n['y'] < 1950]
    assert old and all(n.get('old') for n in old) and not any(n.get('old') for n in d['nodes'] if n['y'] >= 1950)
    by = {n['id']: n for n in d['nodes']}
    rel = [n for n in d['nodes'] if n.get('r')]
    assert rel and all(len(n['r']) <= 2 and all(r[0] != n['id'] and r[1] and r[2] for r in n['r']) for n in rel)
    am24 = by.get('AM-024')
    if am24:
        assert any(r[1] == 'reply to' for r in am24.get('r', []))
    assert all(len(n['l'][0]) <= 111 for n in d['nodes'])
