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
    # relations point forward in time, only between an amendment and a case, never the weak 'linked to'
    assert all(by[r[0]]['y'] >= n['y'] and by[r[0]]['k'] != n['k'] and r[1] != 'linked to' for n in rel for r in n['r'])
    gn = by.get('CS-golaknath-1967')
    if gn and by.get('AM-024'):
        assert ['AM-024', 'Parliament replied with the'] in [r[:2] for r in gn.get('r', [])]
    if by.get('AM-099') and by.get('CS-njac-2015'):
        assert any(r[1] == 'Struck down in' for r in by['AM-099'].get('r', []))
    assert all(len(n['l'][0]) <= 140 and not n['l'][0].endswith('…') and not n['l'][1].endswith('…') for n in d['nodes'])


def test_polity_trees_line_is_a_complete_holding_sentence():
    from app.services.recall_decks import best_line
    one = ("When U.P. nationalised bus routes under a 1955 law, private operators like Deep Chand challenged it; in 1959 the "
           "Supreme Court upheld the Act and held that the doctrine of eclipse applies only to old laws.")
    got = best_line([one, 'It was void. Yes, said the Court.'], 'Still-born law', 120, 'case')
    assert got.startswith('In 1959 the Supreme Court upheld') and got.endswith('.') and len(got) <= 120
    # nothing standalone and short enough: the cue, never a cut fragment
    assert best_line(['It said so; and then more of the same, without any subject at all, for a very long while indeed.'], 'Cue text', 120, 'am') == 'Cue text'
    assert best_line(['The 61st Amendment, 1988 lowered the voting age from 21 to 18 years.'], 'x', 120, 'am').startswith('The 61st Amendment')
