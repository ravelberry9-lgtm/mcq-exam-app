"""Practice tab audit: subject cards with counts, Geography goes straight to setup, whole-selection runs
for Polity and Geography, Polity-style G2 result, folded study-tools dock, nav 'soon' dot."""
import re
from bs4 import BeautifulSoup


def _soup(r):
    assert r.status_code == 200
    return BeautifulSoup(r.get_data(as_text=True), 'html.parser')


def _pos_total(html):
    m = re.search(r'(\d+)\s*/\s*(\d+)', BeautifulSoup(html, 'html.parser').select_one('.geo-qheader').get_text(' '))
    return int(m.group(1)), int(m.group(2))


def test_practice_tab_cards(client, app):
    app.config['POLITY_UNIT6_ENABLED'] = True
    s = _soup(client.get('/learn/practice'))
    pol = s.select_one('[data-subject=polity]')
    geo = s.select_one('[data-subject=geography]')
    assert pol and geo
    assert pol.select_one('a.ps-card')['href'] == '/learn/polity/unit6/practice-start'
    assert geo.select_one('a.ps-card')['href'] == '/learn/geography/g2/practice'
    for card, te in ((pol, 'భారత రాజ్యాంగం'), (geo, 'భూగోళశాస్త్రం')):
        txt = card.get_text(' ')
        assert te in txt and re.search(r'\d+ PYQs · \d+ MCQs', txt)
    assert not s.select('.ps-chip')          # nothing answered yet: no chips


def test_practice_tab_wrong_and_continue_chips(client, app):
    app.config['POLITY_UNIT6_ENABLED'] = True
    # one wrong Geography answer and one wrong Polity answer
    client.post('/learn/geography/g2/1/practice/GEO-ORIG-01-001/answer?qlang=te', data={'answer': '1'})
    client.get('/learn/polity/unit6/practice/POL-6.1-P01-01?qlang=en&chapter=')
    client.post('/learn/polity/unit6/practice/POL-6.1-P01-01?qlang=en&chapter=', data={'answer': '1'})
    s = _soup(client.get('/learn/practice'))
    geo = [a['href'] for a in s.select('[data-subject=geography] .ps-chip')]
    assert any(h.endswith('/learn/geography/g2/mistakes') for h in geo)
    pol = s.select('[data-subject=polity] .ps-chip')
    assert any('view=mistakes' in a['href'] for a in pol)
    assert any('POL-6.1-P01-01' in a['href'] and 'Continue' in a.get_text() for a in pol)
    for a in s.select('.ps-chip'):
        assert client.get(a['href']).status_code in (200, 302)


def test_g2_setup_start_walks_whole_selection(client):
    s = _soup(client.get('/learn/geography/g2/practice'))
    count = int(s.select_one('.ph-count b').get_text())
    start = s.select_one('a.ph-go')['href']
    assert 'run=1' in start
    r = client.get(start, follow_redirects=True)
    assert _pos_total(r.get_data(as_text=True)) == (1, count)
    q = _soup(r)
    assert q.select_one('.geo-qheader a')['href'].startswith('/learn/geography/g2/practice')
    # answering records into the run; the run result has Polity's layout and retry button
    path = r.request.path
    client.post(path + '/answer?qlang=te&run=1', data={'answer': '1' if 'GEO-ORIG-01-001' not in path else '1'})
    res = _soup(client.get('/learn/geography/g2/run/result?run=1&qlang=te'))
    assert res.select_one('.rs-big') and res.select_one('.rs-act')


def test_g2_setup_shows_mistake_and_bookmark_shortcuts(client):
    assert not _soup(client.get('/learn/geography/g2/practice')).select('.g2-quick')
    client.post('/learn/geography/g2/1/practice/GEO-ORIG-01-001/answer?qlang=te', data={'answer': '1'})
    client.post('/learn/geography/g2/1/practice/GEO-ORIG-01-002/answer?qlang=te', data={'action': 'bookmark'})
    s = _soup(client.get('/learn/geography/g2/practice'))
    hrefs = [a['href'] for a in s.select('.g2-quick a')]
    assert any('/g2/mistakes' in h for h in hrefs) and any('/g2/bookmarks' in h for h in hrefs)
    res = _soup(client.get('/learn/geography/g2/1/result?qlang=te'))
    retry = res.select_one('.rs-btn.primary')
    assert retry and 'view=mistakes' in retry['href']


def test_g2_run_flag_is_validated(client):
    assert client.get('/learn/geography/g2/practice?run=2').status_code == 404


def test_polity_all_start_is_not_limited_to_first_chapter(client, app):
    app.config['POLITY_UNIT6_ENABLED'] = True
    s = _soup(client.get('/learn/polity/unit6/practice'))
    count = int(s.select_one('.ph-count b').get_text())
    start = s.select_one('a.ph-go')['href']
    assert 'chapter=' in start
    r = client.get(start, follow_redirects=True)
    assert _pos_total(r.get_data(as_text=True)) == (1, count)
    # a chosen chapter still limits the run
    s = _soup(client.get('/learn/polity/unit6/practice?chapter=6.1.1'))
    n = int(s.select_one('.ph-count b').get_text())
    r = client.get(s.select_one('a.ph-go')['href'], follow_redirects=True)
    assert _pos_total(r.get_data(as_text=True)) == (1, n)


def test_bottom_nav_soon_is_a_dot_and_dock_folds(client):
    html = client.get('/learn/practice').get_data(as_text=True)
    s = BeautifulSoup(html, 'html.parser')
    off = s.select('.bottomnav .navoff')
    assert off and all(o.select_one('.soon') and o.get('title') and '<' not in o['title'] for o in off)
    css = open('static/ds.css', encoding='utf-8').read()
    soon = re.search(r'\.bottomnav \.soon\{[^}]*\}', css).group(0)
    assert 'width:8px' in soon and 'font-size:0' in soon
    js = open('static/study_tools.js', encoding='utf-8').read()
    assert 'mk-dock-toggle' in js and 'setDockOpen' in js
    assert '.mk-dock:not(.mk-open)' in open('static/study_tools.css', encoding='utf-8').read()
