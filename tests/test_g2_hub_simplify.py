"""Hub simplification: subject page redirect, tappable stat cards, no duplicate tiles, infographics picker."""
from bs4 import BeautifulSoup


def _soup(client, url):
    r = client.get(url)
    assert r.status_code == 200, url
    return BeautifulSoup(r.get_data(as_text=True), 'html.parser')


def test_subject_page_redirects_to_hub(client):
    r = client.get('/learn/geography/')
    assert r.status_code == 302 and r.headers['Location'].endswith('/learn/geography/g2')
    learn = _soup(client, '/learn/')
    assert learn.select_one('[data-geography-subject]')['href'].endswith('/learn/geography/g2')


def test_stat_cards_are_links_and_no_duplicate_tiles(client):
    s = _soup(client, '/learn/geography/g2')
    hrefs = [a['href'] for a in s.select('[data-g2-stats] a.st')]
    assert len(hrefs) == 4
    assert hrefs[0] == '#lessons' and 'kind=bank' in hrefs[1] and '/library' in hrefs[2] and 'kind=pyq' in hrefs[2]
    assert 'only=done' in hrefs[3]
    tiles = [a['href'] for a in s.select('nav.g2-quick a')]
    assert len(tiles) == 6 and not any('/library' in h for h in tiles)
    assert any(h.endswith('/g2/infographics') for h in tiles)


def test_only_done_filter(client):
    s = _soup(client, '/learn/geography/g2?only=done')
    assert s.select_one('[data-only-done]') and not s.select('a.u6-chcard')
    client.post('/learn/geography/g2/3/progress', data={'completed': '1'})
    s = _soup(client, '/learn/geography/g2?only=done')
    assert [a['href'].rsplit('/', 1)[1] for a in s.select('a.u6-chcard')] == ['3']
    assert client.get('/learn/geography/g2?only=x').status_code == 404


def test_infographics_picker_and_full_page_gallery(client):
    s = _soup(client, '/learn/geography/g2/infographics')
    picks = s.select('a.g2-pick')
    assert len(picks) == 34 and len(s.select('details.g2-group')) == 2
    g = _soup(client, '/learn/geography/g2/14/infographics?ilang=en')
    assert g.select_one('.g2-gallery.full') and g.select('a[data-zoom] img')
    nxt = g.select_one('[data-next-lesson]')
    assert nxt and '/g2/15/infographics' in nxt['href'] and 'ilang=en' in nxt['href']
