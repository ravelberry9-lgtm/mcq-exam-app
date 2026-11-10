from datetime import datetime,timedelta
from app.db import db
from app.polity_models import PolityUnit6State,PolityUnit6Exam
from app.routes.polity_maps import records,catalog
from app.routes.polity_unit6 import test_records as chapter_test_records

def enable(app):app.config['POLITY_UNIT6_ENABLED']=True

def test_entry_flag_and_old_library(client,app):
    assert client.get('/learn/polity/unit6/').status_code==404
    enable(app)
    assert client.get('/learn/subject/indian_constitution').location.endswith('/learn/polity/unit6/')
    assert client.get('/learn/polity/unit6/').status_code==200

def test_all_sources_maps_and_readers(client,app):
    enable(app)
    with app.app_context():
        qs=records();maps=catalog()
        assert len(qs)==2324
        assert sum(q['_kind']=='expected' for q in qs.values())==32
        assert all(q['_en'] and q['_te'] for q in qs.values())
        assert len(maps)==5
        assert sum(len(m['links']) for m in maps.values())==411
        assert all(x['item_id'] in qs for m in maps.values() for x in m['links'])
        assert sum(len(chapter_test_records(c)) for c in {q['_chapter'] for q in qs.values()})==90
        for chapter in sorted({q['_chapter'] for q in qs.values()}):
            a,b,c=chapter.split('.')
            for suffix in ('','Notes.html','Group-I.html'):
                response=client.get(f'/learn/polity/g2/{a}/{b}/{c}/'+suffix)
                assert response.status_code==200,(chapter,suffix,response.status_code)

def test_unscored_never_incorrect_or_marked_wrong(client,app):
    enable(app);item='POL-641-C008'
    r=client.post('/learn/polity/unit6/practice/'+item,data={'action':'answer','answer':'1'})
    assert r.status_code==200
    assert b'No marks' not in r.data and b'nscored' not in r.data and (b'Correct' in r.data or b'Incorrect' in r.data)
    with app.app_context():
        s=PolityUnit6State.query.filter_by(item_id=item).one()
        assert s.seen_count==1
    r=client.post('/learn/polity/unit6/practice/'+item,data={'action':'bookmark'},follow_redirects=True)
    assert r.status_code==200
    assert item.encode() in client.get('/learn/polity/unit6/library?view=saved').data

def test_scored_mistakes_and_progress(client,app):
    enable(app)
    with app.app_context():q=next(q for q in records().values() if q['_kind']=='bank' and q['_scored'] and q['_answer'] in (1,2,3,4))
    wrong=q['_answer']%4+1
    assert client.post('/learn/polity/unit6/practice/'+q['id'],data={'answer':wrong}).status_code==200
    assert q['id'].encode() in client.get('/learn/polity/unit6/library?view=mistakes').data
    assert client.post('/learn/polity/unit6/practice/'+q['id'],data={'answer':q['_answer']}).status_code==200
    assert q['id'].encode() not in client.get('/learn/polity/unit6/library?view=mistakes').data
    assert client.post('/learn/polity/unit6/progress/6.9.2',data={'completed':'1'},follow_redirects=True).status_code==200

def test_search_and_missing_map(client,app):
    enable(app)
    assert b'POL-641-C008' in client.get('/learn/polity/unit6/library?q=POL-641-C008').data
    assert client.get('/learn/polity/unit6/maps/absent').status_code==404
    assert client.get('/learn/polity/unit6/practice/absent').status_code==404
    assert client.get('/learn/polity/unit6/practice/POL-EXP-REF-614-P38-08').location.endswith('/POL-6.1.4-P38-08')

def test_test_excludes_unscored_and_is_owned(client,app):
    enable(app)
    r=client.post('/learn/polity/unit6/tests',data={'count':'100','minutes':'30'})
    assert r.status_code==302
    with app.app_context():
        e=PolityUnit6Exam.query.one();eid=e.id
        assert len(e.questions)==100 and all(q['_scored'] for q in e.questions)
        answers={q['id']:q['_answer'] for q in e.questions}
    other=app.test_client()
    assert other.get(r.location).status_code==404
    result=client.post(r.location,data=answers)
    assert result.status_code==200
    with app.app_context():
        e=db.session.get(PolityUnit6Exam,eid);assert e.score==100
    client.post(r.location,data={})
    with app.app_context():assert db.session.get(PolityUnit6Exam,eid).score==100

def test_expiry_preserves_saved_answers_and_rejects_late_changes(client,app):
    enable(app)
    r=client.post('/learn/polity/unit6/tests',data={'count':'1','minutes':'1'})
    with app.app_context():e=PolityUnit6Exam.query.one();q=e.questions[0];eid=e.id
    assert client.post(r.location+'/save',data={'item_id':q['id'],'answer':q['_answer']}).status_code==200
    with app.app_context():
        e=db.session.get(PolityUnit6Exam,eid);e.deadline=datetime.utcnow()-timedelta(seconds=1);db.session.commit()
    assert client.post(r.location+'/save',data={'item_id':q['id'],'answer':q['_answer']%4+1}).status_code==409
    assert client.get(r.location).status_code==200
    with app.app_context():assert db.session.get(PolityUnit6Exam,eid).score==1


def test_descriptive_ai_teacher_chat(client,app,monkeypatch):
    enable(app)
    from app.routes import ai_check
    from app.routes.polity_unit6 import descriptive_items
    ai_check._CHAT_USAGE.clear()
    with app.app_context():d=descriptive_items()[0]
    seen=[]
    def fake(messages,**kw):
        seen.append((messages,kw));return 'ఉపాధ్యాయ వివరణ'
    monkeypatch.setattr(ai_check,'_call_openai',fake)
    r=client.post('/api/ai/chat',json={'polity_desc_id':d['id'],'message':'Explain in simple Telugu','history':[]})
    assert r.status_code==200 and r.json['reply']=='ఉపాధ్యాయ వివరణ'
    system=seen[0][0][0]['content']
    assert 'MODEL ANSWER' in system and d['q_en'][:30] in system and seen[0][1]['max_tokens']>=1000
    assert client.post('/api/ai/chat',json={'polity_desc_id':'absent','message':'x'}).status_code==404
    assert client.post('/api/ai/chat',json={'polity_desc_id':d['id'],'polity_id':'x','message':'x'}).status_code==400
    assert client.post('/api/ai/check',json={'polity_desc_id':d['id']}).status_code==400
    page=client.get('/learn/polity/unit6/descriptive').get_data(as_text=True)
    assert 'details class="aid"' in page and 'ai_desc.js' in page


def _admin(client,app):
    from app.routes.admin import _make_token
    with client.session_transaction() as s:s['admin_token']=_make_token(app.config['ADMIN_PIN'])

def test_admin_requires_login_then_edits_deletes_and_stores_text(client,app):
    enable(app)
    r=client.get('/learn/polity/unit6/admin/');assert r.status_code==302 and '/admin/login' in r.location
    assert client.get('/learn/polity/unit6/admin/q/POL-641-C008').status_code==302
    _admin(client,app)
    assert client.get('/learn/polity/unit6/admin/').status_code==200
    with app.app_context():q=next(q for q in records().values() if q['_kind']=='bank' and q['_answer'] in (1,2,3,4))
    base=client.get('/learn/polity/unit6/practice/'+q['id']+'?qlang=en').get_data(as_text=True)
    new=q['_answer']%4+1
    form={'action':'save','question_en':'EDITED STEM TEXT','answer':str(new),'explanation_en':'Edited explanation sentence one. Second sentence here.',
          **{f'option{i}_en':f'Edited option {i}' for i in range(1,5)},**{f'option{i}_te':f'సవరించిన ఎంపిక {i}' for i in range(1,5)}}
    assert client.post('/learn/polity/unit6/admin/q/'+q['id'],data=form).status_code==302
    page=client.get('/learn/polity/unit6/practice/'+q['id']+'?qlang=en').get_data(as_text=True)
    assert 'EDITED STEM TEXT' in page and 'Edited option 2' in page and 'EDITED STEM TEXT' not in base
    r=client.post('/learn/polity/unit6/practice/'+q['id']+'?qlang=en',data={'answer':str(new)});assert b'Correct' in r.data
    assert client.post('/learn/polity/unit6/admin/q/'+q['id'],data={'action':'reset'}).status_code==302
    assert 'EDITED STEM TEXT' not in client.get('/learn/polity/unit6/practice/'+q['id']+'?qlang=en').get_data(as_text=True)
    assert client.post('/learn/polity/unit6/admin/q/'+q['id'],data={'action':'delete'}).status_code==302
    assert client.get('/learn/polity/unit6/practice/'+q['id']).status_code==404
    assert client.post('/learn/polity/unit6/admin/q/'+q['id'],data={'action':'restore'}).status_code==302
    assert client.get('/learn/polity/unit6/practice/'+q['id']).status_code==200
    assert client.post('/learn/polity/unit6/admin/submit',data={'text':'Who wrote X?\nA) a\nB) b\nAnswer: B','chapter':'6.4.1'}).status_code==302
    sub=client.get('/learn/polity/unit6/admin/submissions.json');assert sub.status_code==200 and 'Who wrote X?' in sub.get_data(as_text=True)
    assert 'Who wrote X?' in client.get('/learn/polity/unit6/admin/').get_data(as_text=True)


def test_admin_controls_inline_for_admin_only(client,app):
    enable(app)
    with app.app_context():q=next(q for q in records().values() if q['_kind']=='bank' and q['_answer'] in (1,2,3,4))
    url='/learn/polity/unit6/practice/'+q['id']
    assert 'u6-adminbar' not in client.get(url).get_data(as_text=True) and 'u6-adminbar' not in client.get('/learn/polity/unit6/chapters/6.4.1').get_data(as_text=True)
    _admin(client,app)
    page=client.get(url).get_data(as_text=True)
    assert 'u6-adminbar' in page and 'Edit this question' in page and 'Delete' in page
    assert 'u6-adminbar' in client.get('/learn/polity/unit6/chapters/6.4.1').get_data(as_text=True)
    r=client.post('/learn/polity/unit6/admin/submit',data={'text':'Q?\nA) 1\nAnswer: A','chapter':q['_chapter'],'back':url});assert r.status_code==302 and r.location.endswith(url)
    r=client.post('/learn/polity/unit6/admin/submit',data={'text':'Q2?','chapter':q['_chapter'],'back':'https://evil.example/x'});assert 'evil' not in r.location
    r=client.post('/learn/polity/unit6/admin/q/'+q['id'],data={'action':'delete','back':url.replace(q['id'],'x')});assert r.status_code==302
    assert client.get(url).status_code==404


def test_concept_notes_after_explanation_and_expand(client,app):
    from app.routes.polity_maps import records
    enable(app)
    with app.app_context():
        q=next(x for x in records().values() if x['_chapter'].startswith('6.6') and x.get('_kind')=='bank' and x.get('_answer') in (1,2,3,4))
    r=client.post('/learn/polity/unit6/practice/'+q['id']+'?qlang=both',data={'answer':str(q['_answer'])})
    html=r.get_data(as_text=True)
    assert 'id="concept-notes"' in html and 'cc-allbtn' in html and 'Show all chapter cards' in html and '/cards/' in html
    assert html.index('class="u6-expl"')<html.index('id="concept-notes"')<html.index('id="aichk"')
    assert 'Memory map' not in html
    # not shown before answering
    assert 'concept-notes' not in client.get('/learn/polity/unit6/practice/'+q['id']).get_data(as_text=True)


def test_concept_cards_page_and_notes_tab(client,app):
    enable(app)
    r=client.get('/learn/polity/unit6/cards/6.8.1?hl=CC-6.8-01')
    assert r.status_code==200 and '[id="CC-6.8-01"]{' in r.get_data(as_text=True) and 'class="page"' in r.get_data(as_text=True)
    assert client.get('/learn/polity/unit6/cards/9.9').status_code==404
    n=client.get('/learn/polity/unit6/chapters/6.6.1/notes').get_data(as_text=True)
    assert 'Concept cards / కార్డులు' not in n


def test_concept_cards_full_page_looks_like_notes(client,app):
    from app.routes.polity_maps import records
    enable(app)
    with app.app_context():
        q=next(x for x in records().values() if x['_chapter']=='6.6.1' and x.get('_kind')=='bank' and x.get('_answer') in (1,2,3,4))
    h=client.get('/learn/polity/unit6/cards/6.6.1?item_id='+q['id']+'&hl=CC-6.6-01').get_data(as_text=True)
    assert 'u6-reader-nav' in h and 'data-return-question' in h and 'class="u6-tabs"' not in h and '[id="CC-6.6-01"]{' in h and 'id="recap"' in h and 'id="full-details"' in h and 'class="sh"' in h

def test_article_cards_page(client,app):
    import re
    from app.services import article_cards as ac
    enable(app)
    cards=ac.all_cards()
    assert len(cards)>=150 and len({c['id'] for c in cards})==len(cards)
    for c in cards:
        assert not re.search(r'\d',c['concept_en']+c['concept_te']) or c['article'] not in c['concept_en']
        assert c['says_en'] and c['says_te'] and c['concept_te']
    h=client.get('/learn/polity/unit6/articles').get_data(as_text=True)
    # every card is embedded for the full-screen study deck; setup screen offers every chapter
    assert 'data-id="AC-6.4-21A"' in h and h.count('class="ac-src"')==len(cards)
    assert 'id="ac-setup"' in h and 'id="ac-stage"' in h and 'id="ac-grid"' in h and 'aria-label="Back to card settings"' in h
    # setup offers both matrix densities (3x6 default, 4x8 compact) and every chapter
    assert 'name="density" value="18" checked' in h and 'name="density" value="32"' in h
    assert all(f'name="chapter" value="{ch}"' in h for ch in {c['chapter'] for c in cards})
    # card order: setup offers In order (default) / Random; the matrix bar can switch live and reshuffle
    assert 'name="order" value="seq" checked' in h and 'name="order" value="rand"' in h and 'name="shuffle"' not in h
    # matrix bar: page arrows, cue-mode and language toggles; detail view: collapse + prev/next + self-check; summary overlay
    for el in ('ac-pprev','ac-pnext','ac-page','ac-mode','ac-lang','ac-order','ac-reshuffle','ac-detail','ac-collapse','ac-prev','ac-next','ac-sum'):assert f'id="{el}"' in h
    assert 'aria-label="Collapse to card matrix"' in h and 'aria-label="Previous card"' in h and 'aria-label="Next card"' in h
    assert 'data-judge="k"' in h and 'data-judge="x"' in h and 'data-act="missed"' in h and 'data-act="back"' in h
    assert not re.search(r'\son(click|change|keydown)=', h.split('id="ac"')[1])
    assert 'polity_articles.js?v=' in h and 'polity_articles.css?v=' in h
    h=client.get('/learn/polity/unit6/articles?chapter=6.4&qlang=en').get_data(as_text=True)
    assert 'value="6.4" checked' in h and 'value="en" checked' in h and 'data-lang-set="1"' in h
    assert client.get('/learn/polity/unit6/articles?chapter=9.9').status_code==404


def test_article_key_natural_sort():
    from app.services.article_cards import article_key as k
    assert sorted(['22','21A','21','21B'],key=k)==['21','21A','21B','22']
    assert sorted(['243ZA','243B','243A','243Z','243'],key=k)==['243','243A','243B','243Z','243ZA']
    assert sorted(['371J','371','371A','371D','372'],key=k)==['371','371A','371D','371J','372']
    assert sorted(['51A(k)','51A(b)','51A','51A(a)','51','52'],key=k)==['51','51A','51A(a)','51A(b)','51A(k)','52']
    assert sorted(['395','394A','394','60','324'],key=k)==['60','324','394','394A','395']
    assert sorted(['239B','239AA','239A'],key=k)==['239A','239AA','239B']


def test_article_cards_embedded_in_ascending_article_order(client,app):
    import re
    from app.services import article_cards as ac
    enable(app)
    cards=ac.all_cards()
    keys=[ac.article_key(c['article']) for c in cards]
    assert keys==sorted(keys) and len({c['chapter'] for c in cards})>1
    h=client.get('/learn/polity/unit6/articles').get_data(as_text=True)
    nums=re.findall(r'<div class="s-num">([^<]+)</div>',h)
    assert nums==[c['article'] for c in cards] and [ac.article_key(n) for n in nums]==sorted(ac.article_key(n) for n in nums)
    i=nums.index;assert i('12')<i('21')<i('21A')<i('22')<i('51A(a)')<i('51A(k)')<i('60')<i('324')<i('394')<i('394A')<i('395')


def test_recall_hub_and_decks(client,app):
    from app.services import recall_decks as rd
    enable(app)
    h=client.get('/learn/polity/unit6/recall').get_data(as_text=True)
    assert client.get('/learn/polity/unit6/recall').status_code==200
    for d in rd.DECKS:
        assert f'/learn/polity/unit6/recall/{d}"' in h
        r=client.get(f'/learn/polity/unit6/recall/{d}');assert r.status_code==200,d
        page=r.get_data(as_text=True)
        assert page.count('class="ac-src"')==len(rd.items(d)) and f'data-store="{rd.DECKS[d]["store"]}"' in page
    assert client.get('/learn/polity/unit6/recall/nope').status_code==404
    assert client.get('/learn/polity/unit6/recall/cases?chapter=9.9').status_code==404
    # articles deck keeps its URL and its localStorage key
    a=client.get('/learn/polity/unit6/articles?chapter=6.4').get_data(as_text=True)
    assert 'data-store="u6_artcards_v1"' in a and 'data-setup-store="u6_artcards_setup"' in a and 'value="6.4" checked' in a
    assert len({d['store'] for d in rd.DECKS.values()})==len(rd.DECKS)
    c=client.get('/learn/polity/unit6/recall/cases').get_data(as_text=True)
    assert 'Case → Issue' in c and 'Theme → Cases' in c and 'data-kind="text"' in c and 'Kesavananda Bharati case' in c
    u=client.get('/learn/polity/unit6/unit').get_data(as_text=True)
    assert 'Recall cards / రీకాల్ కార్డులు' in u and '/learn/polity/unit6/recall"' in u


def test_recall_sort_order():
    from app.services import recall_decks as rd
    assert [i['sort'] for i in rd.items('amendments')]==sorted(i['sort'] for i in rd.items('amendments'))
    cs=[(i['theme_i'],i['sort'],i['front_en'].lower()) for i in rd.items('cases')];assert cs==sorted(cs)


def test_recall_deck_files_schema():
    import json,re
    from pathlib import Path
    from app.services import recall_decks as rd
    root=Path(rd.__file__).resolve().parents[2]/'content'/'polity'/'g2'
    card_ids={c['id'] for f in (root/'concept_cards').glob('cards_*.json') for c in json.loads(f.read_text(encoding='utf-8'))}
    files=sorted(p for p in rd.DIR.glob('*.json') if p.name!='case_chains.json');assert files
    seen=set()
    for f in files:
        deck=f.stem.removesuffix('_new');assert deck in rd.DECKS,f
        for it in json.loads(f.read_text(encoding='utf-8')):
            assert it['id'] not in seen,it['id'];seen.add(it['id'])
            assert it['deck']==deck and it['source'] in ('laxmikanth','new') and isinstance(it['two_way'],bool)
            assert (it['source']=='new')==f.stem.endswith('_new'),it['id']
            assert isinstance(it['sort'],int) and re.fullmatch(r'6\.[1-9]',it['chapter'])
            for k in ('front','cue','title','says'):assert it[k+'_en'].strip() and it[k+'_te'].strip(),(it['id'],k)
            assert bool(it.get('trap_en'))==bool(it.get('trap_te')) and len(it.get('points_en') or [])==len(it.get('points_te') or [])
            assert re.search(r'[ఀ-౿]',it['front_te']+it['says_te']),it['id']
            # the cue must not give the answer away: no number, name or year from the front
            cue=(it['cue_en']+' '+it['cue_te']).lower()
            num=re.match(r'\d+',it['front_en'])
            if num:assert not re.search(r'(?<!\d)'+num.group()+r'(?!\d)',cue),it['id']
            # party names only: a bracketed alias such as '(Fourth Judges case)' is not checked
            for w in re.findall(r'[A-Za-z]{4,}',re.sub(r'\([^)]*\)','',it['front_en'])):
                if w.lower() not in ('case','amendment','union','state','india','constitution','college','association','foundation','society','students'):assert w.lower() not in cue,(it['id'],w)
            if it.get('front_sub'):assert str(it['front_sub']) not in cue,it['id']
            assert all(c in card_ids for c in it['card_ids']),it['id']


def test_recall_case_themes_and_theme_view(client,app):
    import json,re
    from app.services import recall_decks as rd
    enable(app)
    names={t[1]:t[2] for t in rd.THEMES}
    for f in rd.deck_files('cases'):
        for it in json.loads(f.read_text(encoding='utf-8')):
            assert it.get('theme_en') in names and it.get('theme_te')==names[it['theme_en']],it['id']
            assert '(' not in it['front_en'] or 'Judges' in it['front_en'],it['id']  # no descriptive brackets on the tile face
    th=rd.themes('cases');assert 8<=len(th)<=12 and sum(len(t['cases']) for t in th)==len(rd.items('cases'))
    assert rd.themes('amendments')==[]
    page=client.get('/learn/polity/unit6/recall/cases').get_data(as_text=True)
    assert page.count('data-theme-tile="1"')==len(th) and 'data-themes="1"' in page
    for t in th:assert f'data-id="{t["id"]}"' in page and t['te'] in page
    k=next(c for c in rd.items('cases') if c['id']=='CS-kesavananda-1973')
    src=page[page.index('data-id="CS-kesavananda-1973"'):];src=src[:src.index('</article>')]
    assert re.search(r'<div class="s-sub">\s*</div>',src)  # year is not on the tile face
    assert 'class="ac-year">1973' in src and k['cue_en'] in src
    am=client.get('/learn/polity/unit6/recall/amendments').get_data(as_text=True)
    assert 'data-theme-tile' not in am and 'data-themes="0"' in am


def test_recall_case_teacher_layout_and_fallback(client,app,monkeypatch):
    from app.services import recall_decks as rd
    enable(app)
    base=rd.items('cases')
    def card(page,cid):
        s=page[page.index(f'data-id="{cid}"'):];return s[:s.index('</article>')]
    # fallback: no new fields -> says under 'What the Court said', no exam section, no compare table
    NEW=('one_line','story','question','held','meaning','remember','first_know','argument','next','chain')
    bare=[{k:v for k,v in c.items() if k not in ('compare','exam') and not k.startswith(NEW)} for c in base]
    orig=rd.items
    monkeypatch.setattr(rd,'items',lambda d:bare if d=='cases' else orig(d))
    page=client.get('/learn/polity/unit6/recall/cases').get_data(as_text=True)
    base=bare
    g=card(page,'CS-gopalan-1950');gop=next(c for c in base if c['id']=='CS-gopalan-1950')
    assert 'కోర్టు ఏమంది?' in g and gop['says_en'][:40] in g and 'ct-exam' not in g and 'ct-cmp' not in g and 'ct-one' not in g
    extra=dict(one_line_en='ONE-LINE-EN',one_line_te='ఒకటి',story_en='STORY-EN',story_te='కథ',question_en='Q-EN',question_te='ప్ర',
               held_en='HELD-EN',held_te='చెప్పింది',meaning_en='MEAN-EN',meaning_te='అర్థం',remember_en=['HOOK-EN'],remember_te=['హుక్'],
               compare={'with_id':'CS-maneka-gandhi-1978','rows':[{'label_en':'L','label_te':'ల','this_en':'NARROW','this_te':'ఇ','other_en':'WIDE','other_te':'వి'}]},
               exam={'patterns_en':['PAT-EN'],'patterns_te':['ప'],'pyqs':[{'qid':'PYQ-X','kind':'pyq','exam':'APPSC Group II','year':2011,'q_en':'PYQ-Q','q_te':'ప్రశ్న','answer_en':'ANS-EN','answer_te':'జ'}],
                     'practice':{'q_en':'PR-Q','q_te':'ప్ర','options_en':['a','b','c','d'],'options_te':['అ','ఆ','ఇ','ఈ'],'answer':2,'why_en':'WHY-EN','why_te':'ఎందుకు'}})
    monkeypatch.setattr(rd,'items',lambda d:[dict(c,**extra) if c['id']=='CS-gopalan-1950' else c for c in base] if d=='cases' else base)
    g=card(client.get('/learn/polity/unit6/recall/cases').get_data(as_text=True),'CS-gopalan-1950')
    order=[g.index(k) for k in ('ONE-LINE-EN','STORY-EN','Q-EN','HELD-EN','MEAN-EN','class="ct-cmp"','HOOK-EN','ac-trap','class="ac-ref"','class="ct-exam"','PAT-EN','PYQ-Q','PR-Q')]
    assert order==sorted(order)
    assert gop['says_en'][:40] not in g and 'Maneka Gandhi case' in g and 'NARROW' in g and 'WIDE' in g
    assert 'PYQ · APPSC Group II 2011' in g and 'ANS-EN' in g and '<details class="ct-reveal">' in g
    assert 'data-ans="2"' in g and g.count('class="ct-opt"')==4 and 'WHY-EN' in g
    # fallback: no first_know/argument/next/chain -> none of those boxes, no timeline
    assert 'ct-know' not in g and 'ct-arg' not in g and 'ct-next' not in g and 'ct-chain' not in g
    # new boxes, chain timeline, exam label stripping
    CH={'c1':{'chain_id':'c1','title_en':'CHAIN-T','title_te':'గొలుసు','intro_en':'CHAIN-INTRO','intro_te':'పరిచయం','steps':[
        {'step':2,'kind':'case','ref':'CS-maneka-gandhi-1978','label_en':'STEP-MANEKA','label_te':'మేనకా','said_en':'S2'},
        {'step':1,'kind':'case','ref':'CS-gopalan-1950','label_en':'STEP-GOPALAN','label_te':'గోపాలన్','said_en':'S1'},
        {'step':3,'kind':'amendment','ref':'AM-44','label_en':'STEP-AM44','label_te':'44','said_en':'S3'}]}}
    monkeypatch.setattr(rd,'chains',lambda:CH)
    ex2=dict(extra,first_know_en='KNOW-EN',first_know_te='తెలుసు',argument_en='ARG-EN',argument_te='వాదం',next_en='NEXT-EN',next_te='తర్వాత',
             chain={'chain_id':'c1','step':1},exam=dict(extra['exam'],pyqs=[dict(extra['exam']['pyqs'][0],exam='Other Credible Examinations — TSPSC Group IV',year=2023)]))
    cs=[dict(c,**ex2) if c['id']=='CS-gopalan-1950' else dict(c,chain={'chain_id':'c1','step':2}) if c['id']=='CS-maneka-gandhi-1978' else c for c in base]
    monkeypatch.setattr(rd,'items',lambda d:cs if d=='cases' else base)
    page=client.get('/learn/polity/unit6/recall/cases').get_data(as_text=True)
    g=card(page,'CS-gopalan-1950')
    order=[g.index(k) for k in ('ONE-LINE-EN','class="ct-know"','STORY-EN','Q-EN','ARG-EN','HELD-EN','MEAN-EN','NEXT-EN','HOOK-EN','class="ct-chain"','class="ct-exam"')]
    assert order==sorted(order)
    assert 'ముందు ఇది తెలుసుకోండి' in g and 'వాదన' in g and 'తర్వాత ఏమైంది?' in g
    tl=g[g.index('class="ct-chain"'):g.index('class="ct-exam"')]
    assert tl.index('STEP-GOPALAN')<tl.index('STEP-MANEKA')<tl.index('STEP-AM44')  # sorted by step
    cur=tl[tl.index('aria-current="step"')-80:tl.index('STEP-MANEKA')]
    assert tl.count('aria-current="step"')==1 and 'STEP-GOPALAN' in cur and 'data-jump="CS-gopalan-1950"' not in tl
    assert 'data-jump="CS-maneka-gandhi-1978"' in tl and 'ct-st am' in tl and 'data-jump="AM-44"' not in tl and 'CHAIN-INTRO' not in tl
    assert 'PYQ · TSPSC Group IV 2023' in g and 'Other Credible' not in g
    m=card(page,'CS-maneka-gandhi-1978');mt=m[m.index('class="ct-chain"'):]
    assert 'data-jump="CS-gopalan-1950"' in mt and 'data-jump="CS-maneka-gandhi-1978"' not in mt
    th=card(page,'TH-liberty')
    assert th.index('class="ct-chain"')<th.index('CHAIN-INTRO')<th.index('ac-thlist') and 'aria-current' not in th and th.count('class="ct-chain"')==1
    from app.services.recall_decks import exam_label
    assert exam_label('other credible examinations - APPSC Group 1')=='APPSC Group 1' and exam_label('APPSC Group II')=='APPSC Group II' and exam_label(None)==''
    monkeypatch.undo();monkeypatch.setattr(rd,'CHAINS_FILE',rd.DIR/'__missing__.json');rd.chains.cache_clear()
    assert rd.chains()=={};rd.chains.cache_clear();enable(app)
    am=client.get('/learn/polity/unit6/recall/amendments').get_data(as_text=True)
    assert 'ct-exam' not in am and 'ct-one' not in am
