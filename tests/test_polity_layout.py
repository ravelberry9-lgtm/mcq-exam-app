from urllib.parse import urlsplit,parse_qs
from bs4 import BeautifulSoup
from app.routes.polity_maps import records
from app.services.polity_sections import section_links,chapter_locators
from app.polity_models import PolityUnit6State
from app.routes import ai_check

from app.routes.polity_unit6 import visible

def soup(response):
    assert response.status_code==200
    return BeautifulSoup(response.data,'html.parser')

def test_hierarchy_and_filtered_previous_next(client,app):
    app.config['POLITY_UNIT6_ENABLED']=True
    subject=soup(client.get('/learn/polity/unit6/'))
    assert subject.select_one('a[href="/learn/polity/unit6/unit"]')
    unit=soup(client.get('/learn/polity/unit6/unit'))
    links=unit.select('a.u6-chcard')
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
    assert '1 / 1700' in soup(client.get(start)).get_text()

def test_every_locator_resolves_and_fallback_returns_without_rescoring(client,app):
    app.config['POLITY_UNIT6_ENABLED']=True
    with app.app_context():
        qs=records()
        assert len(qs)==2324
        for q in qs.values():
            for link in section_links(q):
                if link['anchor'].startswith('u6s-'):
                    from app.routes.polity_unit6 import numbered_notes
                    assert f'id="{link["anchor"]}"' in numbered_notes(q['_chapter'])
                else:assert link['anchor'] in chapter_locators(q['_chapter'])[0]
        q=next(q for q in qs.values() if not section_links(q) and visible(q))
    url='/learn/polity/unit6/practice/'+q['id']+'?chapter='+q['_chapter']+'&kind='+q['_kind']+'&qlang=both'
    answered=soup(client.post(url,data={'answer':'1'}))
    assert answered.select('.is-correct') and 'nscored' not in str(answered)
    notes_url=answered.select_one('[data-chapter-link]')['href']
    assert notes_url.endswith('#question-explanation')
    notes=soup(client.get(notes_url))
    assert notes.select_one('#question-explanation')
    assert notes.select_one('.u6-expl')
    returned=soup(client.get(notes.select_one('[data-return-question]')['href']))
    assert 'Answer:' in returned.get_text() and 'No marks' not in returned.get_text()
    assert returned.select_one('#aichk')
    with app.app_context():
        state=PolityUnit6State.query.filter_by(item_id=q['id']).one()
        assert state.seen_count==1

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
    assert response.status_code==200 and response.json['unscored'] is False
    assert 'STORED ANSWER KEY' in calls[0][1]['content'] and 'FORGED QUESTION' not in str(calls)
    assert client.post('/api/ai/chat',json={'polity_id':q['id'],'message':'Explain this'}).status_code==200
    with app.app_context():
        assert PolityUnit6State.query.count()==0 and records()[q['id']]['_scored'] is True
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


def test_notes_footer_and_telugu_titles(client,app):
    app.config['POLITY_UNIT6_ENABLED']=True
    h=client.get('/learn/polity/unit6/chapters/6.7.1/notes').get_data(as_text=True)
    assert 'u6-notefoot' in h and 'kind=pyq' in h and '6.8.1' in h
    u=client.get('/learn/polity/unit6/unit').get_data(as_text=True)
    assert 'పౌరసత్వం' in u and 'ప్రాథమిక హక్కులు' in u


def test_counts_on_learn_unit_and_subject_pages(client,app):
    import re
    from app.routes.polity_unit6 import unit6_stats
    app.config['POLITY_UNIT6_ENABLED']=True
    with app.test_request_context():
        st=unit6_stats()
    assert (st['chapters'],st['mcq'],st['pyq'])==(14,1210,490)
    learn=client.get('/learn/').get_data(as_text=True)
    assert '14 chapters · 1210 MCQs · 490 PYQs' in learn and '91 chapters' not in learn
    unit=client.get('/learn/polity/unit6/unit').get_data(as_text=True)
    assert '1210' in unit and '490' in unit and unit.count('u6-chcard')>=14
    assert 'MCQs' in client.get('/learn/polity/unit6/').get_data(as_text=True)


def test_heading_level_note_links(client,app):
    import json,re
    from app.routes.polity_maps import CONTENT
    app.config['POLITY_UNIT6_ENABLED']=True
    m=json.load(open(CONTENT/'_shared/Note-Section-Map.json'))['items']
    assert len(m)>1300
    iid,v=next((k,x) for k,x in m.items() if x['chapter']=='6.4.1')
    h=client.get(f'/learn/polity/unit6/practice/{iid}').get_data(as_text=True)
    anchor=f"u6s-{v['heading_idx']}"
    assert f'#{anchor}' in h and 'నోట్స్ చూడండి' in h
    notes=client.get(f'/learn/polity/unit6/chapters/6.4.1/notes?item_id={iid}').get_data(as_text=True)
    assert f'id="{anchor}"' in notes


def test_pyq_source_label_shown(client,app):
    app.config['POLITY_UNIT6_ENABLED']=True
    h=client.get('/learn/polity/unit6/practice/APPSC-G2-2025-C-113').get_data(as_text=True)
    assert 'u6-src' in h and 'APPSC Group II · 2025' in h
    m=client.get('/learn/polity/unit6/practice/PYQ-POL-3570D718DFD1').get_data(as_text=True)
    assert 'SSC CGL · 2022' in m and 'Other credible' not in m


def test_match_following_is_two_independent_columns(client,app):
    from bs4 import BeautifulSoup
    from app.routes.polity_unit6 import format_stem
    h=str(format_stem('Match.\n1. A one\n2. B two\n3. C three\na. x\nb. y\nc. z\nSelect:'))
    s=BeautifulSoup(h,'html.parser')
    cols=s.select('.u6-match .mcol')
    assert len(cols)==2 and len(cols[0].select('.mc'))==3 and 'List II' in cols[1].text
    assert 'Select:' in s.select_one('.u6-tail').text
    plain=str(format_stem('Which is true about the Preamble?'))
    assert 'u6-match' not in plain and 'u6-stmts' not in plain


def test_heading_button_shows_concept_title(client,app):
    import json
    from app.routes.polity_maps import CONTENT
    app.config['POLITY_UNIT6_ENABLED']=True
    iid,v=next((k,x) for k,x in json.load(open(CONTENT/'_shared/Note-Section-Map.json'))['items'].items() if x['title_en'])
    h=client.get(f'/learn/polity/unit6/practice/{iid}').get_data(as_text=True)
    assert v['title_en'] in h


def test_wrong_is_red_points_explanation_and_no_unscored_text(client,app):
    app.config['POLITY_UNIT6_ENABLED']=True
    with app.app_context():
        from app.routes.polity_unit6 import visible
        qs=[q for q in records().values() if visible(q)]
        was_unscored=next(q for q in qs if not q['_orig_scored'])
        multi=next(q for q in qs if q['_en'].count('. ')>=3)
    for q in (was_unscored,multi):
        wrong=q['_answer']%4+1
        page=soup(client.post('/learn/polity/unit6/practice/'+q['id'],data={'answer':str(wrong)}))
        assert page.select('.geo-option.is-wrong') and page.select('.geo-answer.is-wrong') and page.select('.geo-option.is-correct')
        text=page.get_text().lower()
        assert 'unscored' not in text and 'no marks' not in text and 'study only' not in text
        assert page.select('.u6-expl .lead')
    assert soup(client.post('/learn/polity/unit6/practice/'+multi['id'],data={'answer':str(multi['_answer'])})).select('.u6-expl ul.pts li')
    ok=soup(client.post('/learn/polity/unit6/practice/'+multi['id'],data={'answer':str(multi['_answer'])}))
    assert ok.select('.geo-answer.is-right')


def test_notes_have_gbk_and_laxmikanth_tabs(client,app):
    app.config['POLITY_UNIT6_ENABLED']=True
    gbk=soup(client.get('/learn/polity/unit6/chapters/6.4.1/notes'))
    tabs=gbk.select('.u6-tabs a')
    assert len(tabs)==2 and tabs[0].get('aria-current')=='page'
    lax=client.get(tabs[1]['href']);assert lax.status_code==200
    page=soup(lax);assert page.select('.u6-tabs a')[1].get('aria-current')=='page' and '.page{width:auto!important' in lax.get_data(as_text=True)
    assert 'Fundamental Rights' in page.get_text()
    chapter=client.get('/learn/polity/unit6/chapters/6.4.1').get_data(as_text=True)
    assert '/references/laxmikanth/' not in chapter
    multi=soup(client.get('/learn/polity/unit6/chapters/6.5.2/notes?src=lax'))
    assert len(multi.select('.u6-lxsub a'))==3


def test_stat_tiles_open_whole_unit_lists(client,app):
    app.config['POLITY_UNIT6_ENABLED']=True
    page=soup(client.get('/learn/polity/unit6/unit'))
    hrefs=[a['href'] for a in page.select('a.st')]
    assert any('kind=bank' in h for h in hrefs) and any('kind=pyq' in h for h in hrefs)
    assert all('chapter=' not in h for h in hrefs)
    r=client.get([h for h in hrefs if 'kind=pyq' in h][0]);assert r.status_code==200 and '490' in r.get_data(as_text=True)


def test_subject_page_lists_all_units_with_topics(client,app):
    app.config['POLITY_UNIT6_ENABLED']=True
    page=soup(client.get('/learn/polity/unit6/'))
    units=page.select('.u6-unit')
    assert len(units)==5 and page.select_one('a.u6-unit-h')['href'].endswith('/unit')
    assert units[0].select('.u6-topics li') and 'Preamble' in units[0].get_text() and 'Coming soon' in units[1].get_text()
    assert len(page.select('section.card'))==6


def test_descriptive_questions_page(client,app):
    app.config['POLITY_UNIT6_ENABLED']=True
    page=soup(client.get('/learn/polity/unit6/descriptive?qlang=both'))
    assert len(page.select('article.u6-desc'))==82
    assert page.select('details .da') and page.select('.u6-chpills a')
    one=soup(client.get('/learn/polity/unit6/descriptive?chapter=6.4.1'))
    assert len(one.select('article.u6-desc'))==19
    assert any('Descriptive' in a.get_text() for a in soup(client.get('/learn/polity/unit6/unit')).select('a.st'))
    assert client.get('/learn/polity/unit6/descriptive?chapter=9.9').status_code==404
