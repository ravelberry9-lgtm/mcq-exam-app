from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,hashlib

ROOT=Path(__file__).resolve().parents[1]
CAT=json.loads((ROOT/'static/textbooks/geography/catalogue.json').read_text(encoding='utf-8'))

class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=='a' and d.get('href'):self.links.append(d['href'])
        if tag=='img' and d.get('src'):self.links.append(d['src'])

def test_catalogue_routes_full_text_and_assets(client):
    assert [len(u['lessons']) for u in CAT['units']]==[4,4,5,5,4,5,4,4,4,4,20,4,4,4,4,4]
    hub=client.get('/learn/').data
    assert hub.count(b'data-geography-subject=')==1
    assert b'data-subject="indian_geography"' not in hub
    assert b'data-subject="ap_geography"' not in hub
    index=client.get('/learn/geography/')
    assert index.status_code==200 and index.data.count(b'data-geography-unit=')==16
    ids=[]
    for u in CAT['units']:
        page=client.get(f"/learn/geography/unit/{u['id']}")
        assert page.status_code==200
        assert page.data.count(b'data-geography-lesson=')==len(u['lessons'])
        for l in u['lessons']:
            ids.append(l['id']);response=client.get('/learn/geography/lesson/'+l['id'])
            assert response.status_code==200
            source=(ROOT/'static/textbooks/geography/lessons'/l['file']).read_bytes()
            assert response.data==source and len(source)>3000
            parser=Links();parser.feed(response.data.decode('utf-8'))
            for link in parser.links:
                parsed=urlsplit(link)
                if parsed.scheme or parsed.netloc or not parsed.path:continue
                if parsed.path.startswith('/static/'):
                    path=ROOT/'static'/unquote(parsed.path.removeprefix('/static/'))
                    assert path.is_file(),link
                else:
                    assert client.get(parsed.path).status_code==200,link
    assert len(ids)==len(set(ids))==83
    assert client.get('/learn/geography/unit/17').status_code==404
    assert client.get('/learn/geography/lesson/99').status_code==404
    assert client.get('/learn/geography/lesson/../../app/config.py').status_code==404

def test_manifest_hashes():
    for name,sha in CAT['files'].items():
        assert hashlib.sha256((ROOT/'static/textbooks/geography'/name).read_bytes()).hexdigest()==sha