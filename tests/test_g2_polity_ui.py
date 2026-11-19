"""Group 2 Geography in Polity's design: hub, lesson, practice setup, library, bookmarks/mistakes,
quick revision, timed test and filtered practice runs."""
import re
from app.services import geo_g2 as g2

B = '/learn/geography/g2'


def _pyq(n):
    return next(q for q in g2.lesson_records(n) if q['_kind'] == 'pyq')


def test_hub_totals_tiles_groups(client):
    r = client.get(B);assert r.status_code == 200;h = r.get_data(as_text=True)
    recs = g2.records();pyq = sum(q['_kind'] == 'pyq' for q in recs)
    assert f'<b>{len(recs) - pyq}</b>' in h and f'<b>{pyq}</b>' in h and '<b>34</b>' in h
    for path in ('/g2/practice', '/g2/revise', '/g2/library?kind=pyq', '/g2/bookmarks', '/g2/mistakes', '/g2/tests', '/learn/my-saved/'):
        assert path in h
    assert h.count('class="u6-chcard"') == 34 and h.count('<details class="card g2-group"') == 2
    n18 = g2.lesson_records(18)
    assert f'{sum(q["_kind"]=="pyq" for q in n18)} PYQs' in h


def test_lesson_page_links_and_progress_persists(client):
    h = client.get(B + '/18').get_data(as_text=True)
    for s in ('/g2/18/notes', 'ls=18&amp;kind=pyq', 'ls=18&amp;kind=bank', '/g2/18/infographics', 'revise?lesson=18', 'Mark lesson completed'):
        assert s in h, s
    assert client.post(B + '/18/progress', data={'completed': '1'}).status_code == 302
    assert 'Completed ✓' in client.get(B + '/18').get_data(as_text=True)
    assert '✓ Done' in client.get(B).get_data(as_text=True)
    client.post(B + '/18/progress', data={'completed': '0'})
    assert 'Mark lesson completed' in client.get(B + '/18').get_data(as_text=True)
    assert client.get(B + '/99').status_code == 404


def test_infographics_gallery_language(client):
    n = len(g2.images(1)['images'])
    te = client.get(B + '/1/infographics').get_data(as_text=True);en = client.get(B + '/1/infographics?ilang=en').get_data(as_text=True)
    assert te.count('<figure') == n and '_te.webp' in te and '_en.webp' in en
    assert client.get(B + '/1/infographics?ilang=xx').status_code == 400


def test_practice_setup_counts_and_filters(client):
    def count(q):
        return int(re.search(r'<div class="ph-count"><b>(\d+)</b>', client.get(B + '/practice' + q).get_data(as_text=True)).group(1))
    recs = g2.records()
    assert count('') == len(recs)
    assert count('?kind=pyq') == sum(q['_kind'] == 'pyq' for q in recs)
    assert count('?kind=bank&ls=18') == sum(q['_kind'] == 'bank' and q['_lesson'] == 18 for q in recs)
    assert count('?ls=1,2') == sum(q['_lesson'] in (1, 2) for q in recs)
    up = sum(q['_kind'] == 'pyq' and q['_exam'] == 'upsc' for q in recs)
    assert count('?kind=pyq&exam=upsc') == up
    yr = sum(bool(q['_kind'] == 'pyq' and q['_year'] and 2019 <= q['_year'] <= 2020) for q in recs)
    assert count('?kind=pyq&y1=2019&y2=2020') == yr
    sec = g2.lesson_sections(18)[0]
    assert count(f'?ls=18&sec={sec[0]}') == sec[2]
    assert client.get(B + '/practice?exam=bad').status_code == 404
    assert client.get(B + '/practice?ls=77').status_code == 404


def test_library_labels_search_and_start(client):
    q = _pyq(1);s = q['_src']
    h = client.get(B + '/library?ls=1&kind=pyq').get_data(as_text=True)
    assert f'Q{s["qno"]}' in h and str(s['year']) in h and 'Start from here' in h
    assert f'/g2/1/practice/{q["id"]}?' in h
    h = client.get(B + '/library?q=' + q['id']).get_data(as_text=True)
    assert '1 results' in h


def test_filtered_run_crosses_lessons_and_scores(client):
    qs = [q for q in g2.records() if q['_lesson'] in (1, 2) and q['_kind'] == 'pyq']
    last1 = [q for q in qs if q['_lesson'] == 1][-1];first2 = next(q for q in qs if q['_lesson'] == 2)
    h = client.get(f'{B}/1/practice/{last1["id"]}?kind=pyq&ls=1,2').get_data(as_text=True)
    assert f'/g2/2/practice/{first2["id"]}?' in h and '<b>PYQ</b>' in h
    r = client.post(f'{B}/1/practice/{last1["id"]}/answer?kind=pyq&ls=1,2&qlang=te', data={'answer': str(last1['answer'])})
    assert 'kind=pyq' in r.headers['Location'] and 'ls=1' in r.headers['Location']
    h = client.get(B + '/run/result?kind=pyq&ls=1,2').get_data(as_text=True)
    assert '<p class="rs-big"><b>1</b> / 1</p>' in h  # Polity-style result (PRACTICE_AUDIT)


def test_bookmarks_and_mistakes(client):
    q = g2.lesson_records(3)[0];w = g2.lesson_records(3)[1]
    client.post(f'{B}/3/practice/{q["id"]}/answer', data={'action': 'bookmark'})
    client.post(f'{B}/3/practice/{w["id"]}/answer', data={'answer': str(w['answer'] % 4 + 1)})
    b = client.get(B + '/bookmarks').get_data(as_text=True);m = client.get(B + '/mistakes').get_data(as_text=True)
    assert '1 results' in b and q['id'] in b and '1 results' in m and w['id'] in m
    assert 'Bookmarks (1)' in client.get(B).get_data(as_text=True)
    # only unseen excludes the answered one
    recs3 = g2.lesson_records(3)
    h = client.get(B + '/practice?ls=3&view=unseen').get_data(as_text=True)
    assert f'<b>{len(recs3) - 1}</b>' in h
    # answering a mistake right keeps Next working in the mistakes run
    r = client.get(f'{B}/3/practice/{w["id"]}?view=mistakes');assert r.status_code == 200


def test_quick_revision(client):
    h = client.get(B + '/revise?lesson=18&kind=pyq').get_data(as_text=True)
    n = sum(q['_kind'] == 'pyq' for q in g2.lesson_records(18))
    assert f'<b>{n}</b> PYQs' in h and 'polity_revise.js' in h
    key = re.search(r'data-ch="([^"]+)"', h).group(1)
    p = client.get(f'{B}/revise/18/part?ch={key}&kind=pyq&qlang=both').get_data(as_text=True)
    assert 'rv-ab' in p and 'Tap to see the answer' in p and 'lang="te"' in p and 'lang="en"' in p
    assert client.get(B + '/revise/18/part?ch=nope').status_code == 404


def test_timed_test_flow(client):
    r = client.post(B + '/tests', data={'ls': ['5'], 'count': '3', 'minutes': '5'})
    assert r.status_code == 302;url = r.headers['Location'].split('?')[0]
    h = client.get(url).get_data(as_text=True);assert 'u6-timer' in h
    ids = re.findall(r'name="(GEO[^"]+|PYQ[^"]+)" value="1"', h)
    assert len(ids) == 3
    q = g2.by_id()[ids[0]]
    assert client.post(url + '/save', data={'item_id': ids[0], 'answer': str(q['answer'])}).json == {'saved': True}
    client.post(url, data={})
    h = client.get(url).get_data(as_text=True)
    assert 'Score <b>1</b> / 3' in h and 'Explanation' in h
    assert client.post(url + '/save', data={'item_id': ids[0], 'answer': '1'}).status_code == 409


def test_old_urls_still_work(client):
    for p in ('/1', '/1/practice', '/1/notes', '/1/practice/' + g2.lesson_records(1)[0]['id'], '/1/result'):
        assert client.get(B + p).status_code == 200, p
