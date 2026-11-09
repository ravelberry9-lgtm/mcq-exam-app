from urllib.parse import urlsplit,parse_qs
from bs4 import BeautifulSoup
from app.routes.polity_maps import records
from app.services.polity_sections import section_links,chapter_locators
from app.polity_models import PolityUnit6State
from app.routes import ai_check

def soup(response):
    assert response.status_code==200
    return BeautifulSoup(response.data,'html.parser')

def test_hierarchy_and_filtered_previous_next(client,app):
    app.config['POLITY_UNIT6_ENABLED']=True
    subject=soup(client.get('/learn/polity/unit6/'))
    assert subject.select_one('a[href="/learn/polity/unit6/unit"]')
    unit=soup(client.get('/learn/polity/unit6/unit'))
    links=unit.select('h2 a')
    assert len(links)==14
    chapter=soup(client.get(links[0]['href']))
    pyq=next(a['href'] for a in chapter.select('a') if 'kind=pyq' in a.get('href',''))
    library=soup(client.get(pyq+'&qlang=en'))
    start=next(a['href'] for a in library.select('a') if 'Start practice' in a.text)
    first=soup(client.get(start))
    assert not first.select_one('a[rel=prev]')
    second_url=first.select_one('a[rel=next]')['href']
    assert parse_qs(urlsplit(second_url).query)['kind']==['pyq']
    assert parse_qs(urlsplit(second_url).query)['qlang']==['en']
    second=soup(client.get(second_url))
    back=urlsplit(second.select_one('a[rel=prev]')['href']);initial=urlsplit(start)
    assert back.path==initial.path and parse_qs(back.query)==parse_qs(initial.query)
    global_library=soup(client.get('/learn/polity/unit6/library'))
    start=next(a['href'] for a in global_library.select('a') if 'Start practice' in a.text)
    assert '1 / 1726' in soup(client.get(start)).get_text()

def test_every_locator_resolves_and_fallback_returns_without_rescoring(client,app):
    app.config['POLITY_UNIT6_ENABLED']=True
    with app.app_context():
        qs=records()
        assert len(qs)==2324 and sum(q['_scored'] for q in qs.values())==1933
        for q in qs.values():
            for link in section_links(q):assert link['anchor'] in chapter_locators(q['_chapter'])[0]
        q=next(q for q in qs.values() if not section_links(q) and not q['_scored'])
    url='/learn/polity/unit6/practice/'+q['id']+'?chapter='+q['_chapter']+'&kind='+q['_kind']+'&qlang=both'
    answered=soup(client.post(url,data={'answer':'1'}))
    assert not answered.select('.is-correct,.is-wrong')
    notes_url=answered.select_one('[data-chapter-link]')['href']
    assert notes_url.endswith('#question-explanation')
    notes=soup(client.get(notes_url))
    assert notes.select_one('#question-explanation')
    assert q['_en'] in notes.get_text() and q['_te'] in notes.get_text()
    returned=soup(client.get(notes.select_one('[data-return-question]')['href']))
    assert 'No marks awarded or deducted' in returned.get_text()
    assert returned.select_one('#aichk')
    with app.app_context():
        state=PolityUnit6State.query.filter_by(item_id=q['id']).one()
        assert state.seen_count==1 and state.wrong_count==0

def test_polity_ai_reads_stored_content_and_never_scores(client,app,monkeypatch):
    app.config['POLITY_UNIT6_ENABLED']=True
    ai_check._CACHE.clear();ai_check._USAGE.clear();ai_check._CHAT_USAGE.clear();ai_check._WEB_USAGE.clear()
    with app.app_context():q=records()['POL-641-C008']
    calls=[]
    def fake(messages,**kw):
        calls.append(messages)
        return {'verdict':'agrees','your_answer':'abcd'[q['_answer']-1],'te':'సలహా','en':'Advice','issues':[]} if kw.get('json_mode',True) else 'Study advice only.'
    monkeypatch.setattr(ai_check,'_call_openai',fake)
    response=client.post('/api/ai/check',json={'polity_id':q['id'],'question':'FORGED QUESTION'})
    assert response.status_code==200 and response.json['unscored'] is True
    assert 'STUDY ANSWER' in calls[0][1]['content'] and 'FORGED QUESTION' not in str(calls)
    assert client.post('/api/ai/chat',json={'polity_id':q['id'],'message':'Explain this'}).status_code==200
    assert 'UNSCORED' in calls[-1][0]['content']
    with app.app_context():
        assert PolityUnit6State.query.count()==0 and records()[q['id']]['_scored'] is False
    assert client.post('/api/ai/check',json={'polity_id':q['id'],'geo_lesson':1}).status_code==400
    assert client.post('/api/ai/check',json={'polity_id':'absent'}).status_code==404
    app.config['POLITY_UNIT6_ENABLED']=False
    assert client.post('/api/ai/check',json={'polity_id':q['id']}).status_code==404


def test_map_questions_are_clean_mcq_pyq_only(client,app):
    app.config['POLITY_UNIT6_ENABLED']=True
    from bs4 import BeautifulSoup
    from app.routes.polity_maps import catalog
    for mid in catalog():
        html=client.get(f'/learn/polity/unit6/maps/{mid}/questions?qlang=te').get_data(as_text=True)
        s=BeautifulSoup(html,'html.parser')
        cards=s.select('a.mm-card')
        assert cards, mid
        text=' '.join(c.get_text(' ',strip=True) for c in cards)
        assert 'POL-' not in text and 'DIRECT' not in text and 'PARTIAL' not in text
        assert not s.select('a.mm-card [lang=en]')
        href=cards[0]['href']
        assert f'map={mid}' in href
        page=client.get(href).get_data(as_text=True)
        assert 'Map questions' in page
        mp=client.get(f'/learn/polity/unit6/maps/{mid}?qlang=en').get_data(as_text=True)
        assert 'u6-mapbar' in mp and 'Practice' in mp


def test_next_stays_inside_map(client,app):
    app.config['POLITY_UNIT6_ENABLED']=True
    from bs4 import BeautifulSoup
    from app.routes.polity_maps import catalog
    mid=next(iter(catalog()))
    s=BeautifulSoup(client.get(f'/learn/polity/unit6/maps/{mid}/questions').get_data(as_text=True),'html.parser')
    first=s.select('a.mm-card')[0]['href']
    p=BeautifulSoup(client.get(first).get_data(as_text=True),'html.parser')
    nxt=p.select_one('a[rel=next]')
    assert nxt and f'map={mid}' in nxt['href']


def test_map_page_has_one_bar_and_matching_count(client,app):
    import re
    from app.routes.polity_maps import catalog
    app.config['POLITY_UNIT6_ENABLED']=True
    for mid in catalog():
        h=client.get(f'/learn/polity/unit6/maps/{mid}').get_data(as_text=True)
        assert h.count('u6-mapbar" aria-label')==1 and 'Linked questions (' not in h
        n=int(re.search(r'Practice (\d+) questions',h).group(1))
        assert f'Linked questions: {n}' in h
