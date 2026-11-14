import re
from datetime import datetime,timedelta
from app.db import db
from app.polity_models import PolityUnit6State,PolityUnit6Exam
from app.routes.polity_maps import records,catalog
from app.routes.polity_unit6 import test_records as chapter_test_records

def enable(app):app.config['POLITY_UNIT6_ENABLED']=True

def added_ids():
    """Ids from the unit-distribution files (PYQ bank v3.71.0 records outside unit 6's reviewed sets, Laxmikanth MCQs)."""
    import json
    from app.routes.polity_maps import CONTENT
    ids=set()
    for name in ('PYQ-Bank-Set.json','Laxmikanth-Questions.json'):
        for f in CONTENT.glob('*.*/*/'+name):ids|={q['id'] for q in json.loads(f.read_text(encoding='utf-8'))['questions']}
    for f in CONTENT.glob('*.*/*/PYQ-Set.json'):
        if not f.parent.name.startswith('6.'):ids|={q['id'] for q in json.loads(f.read_text(encoding='utf-8'))['questions']}
    return ids

def deck_data(page):
    import json
    return json.loads(re.search(r'<script type="application/json" id="ac-data">(.*?)</script>',page,re.S).group(1))

def frag(client,cid):
    """The lazily fetched full card (<article class="ac-src">) of any deck."""
    from app.services import recall_decks as rd
    d='cases' if cid.startswith('TH-') else rd.deck_of(cid)
    r=client.get(f'/learn/polity/unit6/recall/{d}/card/{cid}');assert r.status_code==200,(cid,r.status_code)
    return r.get_data(as_text=True)

def test_entry_flag_and_old_library(client,app):
    assert client.get('/learn/polity/unit6/').status_code==404
    enable(app)
    assert client.get('/learn/subject/indian_constitution').location.endswith('/learn/polity/unit6/')
    assert client.get('/learn/polity/unit6/').status_code==200

def test_all_sources_maps_and_readers(client,app):
    enable(app)
    with app.app_context():
        allqs=records();maps=catalog()
        # Unit 6's authored records are unchanged; bank PYQs / Laxmikanth MCQs added for units 6-10 live in their own files.
        qs={k:q for k,q in allqs.items() if k not in added_ids()}
        assert sum(1 for q in qs.values() if q['_chapter'].startswith('6.'))==2585  # 2315 + 27 PYQs reclassified + 114 new A-R/match + 35 cross-chapter + 94 APPSC PYQ-gap MCQs on 2026-11-12
        qs={k:q for k,q in qs.items() if q['_chapter'].startswith('6.')}
        assert sum(q['_kind']=='expected' for q in qs.values())==32
        assert all(q['_en'] and (q['_te'] or q.get('_v2')) for q in qs.values())  # v2 PYQ explanations are English-only
        assert len(maps)==5
        assert sum(len(m['links']) for m in maps.values())==411
        assert all(x['item_id'] in qs or x['item_id'].startswith('PYQ-POL-WEB-') and x['item_id'] in allqs for m in maps.values() for x in m['links'])  # superseded reworded UPSC copies point to the real v3.71 record
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
        from app.services import concepts as _cg
        q=next(x for x in records().values() if x.get('_kind')=='bank' and x.get('_answer') in (1,2,3,4) and not _cg.subs_for(x['id']))
    r=client.post('/learn/polity/unit6/practice/'+q['id']+'?qlang=both',data={'answer':str(q['_answer'])})
    html=r.get_data(as_text=True)
    assert 'id="concept-notes"' in html and 'cc-allbtn' in html and 'Show all chapter cards' in html and '/cards/' in html
    assert html.index('class="xp"')<html.index('id="concept-notes"')<html.index('id="aichk"')
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
    D=deck_data(h);assert [x['id'] for x in D['cards']]==[c['id'] for c in cards] and 'class="ac-src"' not in h and 'AC-6.4-21A' in h
    assert 'id="ac-setup"' in h and 'id="ac-stage"' in h and 'id="ac-grid"' in h and 'aria-label="Back to card settings"' in h
    # setup offers both matrix densities (3x6 default, 4x8 compact) and every chapter
    assert 'name="density" value="18" checked' in h and 'name="density" value="32"' in h
    # Part filter chips (multi-select, All default) + Unit filter replace the chapter chips
    assert 'name="partall" value="1" checked' in h and all(f'name="part" value="{p}"' in h for p in {x['p'] for x in D['cards']})
    assert 'name="unit" value="" checked' in h and all(f'name="unit" value="{u}"' in h for u in (6,7,8,9,10)) and 'name="chapter"' not in h
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
    nums=[x['n'] for x in deck_data(h)['cards']]
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
        assert len(deck_data(page)['cards'])==len(rd.items(d)) and f'data-store="{rd.DECKS[d]["store"]}"' in page
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
    files=sorted(p for p in rd.DIR.glob('*.json') if p.name not in ('case_chains.json','links.json','pyq_map.json'));assert files
    seen=set()
    for f in files:
        deck=f.stem.removesuffix('_new');assert deck in rd.DECKS,f
        for it in json.loads(f.read_text(encoding='utf-8')):
            assert it['id'] not in seen,it['id'];seen.add(it['id'])
            assert it['deck']==deck and it['source'] in ('laxmikanth','new') and isinstance(it['two_way'],bool)
            assert (it['source']=='new')==f.stem.endswith('_new'),it['id']
            assert isinstance(it['sort'],int) and re.fullmatch(r'6\.[1-9]|polity',it['chapter'])
            for k in ('front','cue','title','says'):assert it[k+'_en'].strip() and it[k+'_te'].strip(),(it['id'],k)
            assert bool(it.get('trap_en'))==bool(it.get('trap_te')) and len(it.get('points_en') or [])==len(it.get('points_te') or [])
            assert re.search(r'[ఀ-౿]',it['front_te']+it['says_te']),it['id']
            # the cue must not give the answer away: no number, name or year from the front
            cue=(it['cue_en']+' '+it['cue_te']).lower()
            num=re.match(r'\d+',it['front_en'])
            if num:assert not re.search(r'(?<!\d)'+num.group()+r'(?!\d)',cue),it['id']
            # party names only: a bracketed alias such as '(Fourth Judges case)' is not checked
            for w in re.findall(r'[A-Za-z]{4,}',re.sub(r'\([^)]*\)','',it['front_en'])):
                if w.lower() not in ('case','amendment','union','state','india','constitution','college','association','foundation','society','students','governor','principal','secretary'):assert w.lower() not in cue,(it['id'],w)
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
    th=rd.themes('cases');assert 8<=len(th)<=16 and sum(len(t['cases']) for t in th)==len(rd.items('cases'))+sum(len(c.get('also_themes') or []) for c in rd.items('cases'))
    assert rd.themes('amendments')==[]
    page=client.get('/learn/polity/unit6/recall/cases').get_data(as_text=True)
    D=deck_data(page);assert [t['id'] for t in D['themes']]==[t['id'] for t in th] and 'data-themes="1"' in page
    for t in th:assert t['te'] in page.encode('ascii','backslashreplace').decode('unicode_escape') or t['te'] in frag(client,t['id'])
    assert all(D['themes'][i]['cases']==[c['id'] for c in t['cases']] for i,t in enumerate(th))
    k=next(c for c in rd.items('cases') if c['id']=='CS-kesavananda-1973')
    src=frag(client,'CS-kesavananda-1973')
    assert '<div class="s-sub">1973' in src  # year is a muted subline on the tile face
    assert 'class="ac-year">1973' in src and k['cue_en'] in src
    am=client.get('/learn/polity/unit6/recall/amendments').get_data(as_text=True)
    assert 'data-theme-tile' not in am and 'data-themes="0"' in am


def test_recall_case_teacher_layout_and_fallback(client,app,monkeypatch):
    from app.services import recall_decks as rd
    enable(app)
    base=rd.items('cases')
    def card(page,cid):return frag(client,cid)
    # fallback: no new fields -> says under 'What the Court said', no exam section, no compare table
    NEW=('one_line','story','question','held','meaning','remember','first_know','argument','next','chain')
    bare=[{k:v for k,v in c.items() if k not in ('compare','exam') and not k.startswith(NEW)} for c in base]
    orig=rd.items
    monkeypatch.setattr(rd,'items',lambda d:bare if d=='cases' else orig(d))
    page=client.get('/learn/polity/unit6/recall/cases').get_data(as_text=True)
    base=bare
    g=card(page,'CS-gopalan-1950');gop=next(c for c in base if c['id']=='CS-gopalan-1950')
    assert 'కోర్టు ఏమంది?' in g and gop['says_en'][:40] in re.sub(r'<[^>]+>','',g) and 'ct-exam' not in g and 'ct-cmp' not in g and 'ct-one' not in g
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
    assert tl.count('aria-current="step"')==1 and 'STEP-GOPALAN' in cur and 'data-go="CS-gopalan-1950"' not in tl
    assert 'data-go="CS-maneka-gandhi-1978"' in tl and 'ct-st am' in tl and 'data-go="AM-44"' not in tl and 'CHAIN-INTRO' not in tl
    assert 'PYQ · TSPSC Group IV 2023' in g and 'Other Credible' not in g
    m=card(page,'CS-maneka-gandhi-1978');mt=m[m.index('class="ct-chain"'):]
    assert 'data-go="CS-gopalan-1950"' in mt and 'data-go="CS-maneka-gandhi-1978"' not in mt
    th=card(page,'TH-liberty')
    assert th.index('class="ct-chain"')<th.index('CHAIN-INTRO')<th.index('ac-thlist') and 'aria-current' not in th and th.count('class="ct-chain"')==1
    from app.services.recall_decks import exam_label
    assert exam_label('other credible examinations - APPSC Group 1')=='APPSC Group 1' and exam_label('APPSC Group II')=='APPSC Group II' and exam_label(None)==''
    monkeypatch.undo();monkeypatch.setattr(rd,'CHAINS_FILE',rd.DIR/'__missing__.json');rd.chains.cache_clear()
    assert rd.chains()=={};rd.chains.cache_clear();enable(app)
    am=frag(client,'AM-042')
    assert 'ct-exam' in am  # amendments now have their own exam section

def test_case_chains_data_complete_dated_and_linked():
    import json
    from app.services import recall_decks as rd
    rd.chains.cache_clear()
    raw=json.loads(rd.CHAINS_FILE.read_text(encoding='utf-8'));ix=rd.index()['cards']
    assert {c['chain_id'] for c in raw}>={'CH-amending-power','CH-article-21','CH-property-ninth-schedule','CH-reservation','CH-tribunals'}
    DATE=re.compile(r'^\d{4}(-\d\d-\d\d)?$')
    listed={}
    for ch in raw:
        assert ch['title_te'] and ch['title_en'] and ch['short_te'] and ch['short_en'] and ch['intro_te'] and ch['intro_en']
        st=ch['steps'];assert [s['step'] for s in st]==list(range(1,len(st)+1)),ch['chain_id']
        for s in st:
            assert s['kind'] in ('case','amendment','event') and DATE.match(s['date']),(ch['chain_id'],s)
            for k in ('label','said','who'):assert s[k+'_te'] and s[k+'_en'],(ch['chain_id'],s['step'],k)
            assert s['source']
            if s['kind']=='event':assert s['ref'] is None
            else:
                assert s['ref'] in ix,(ch['chain_id'],s['ref'])
                assert rd.deck_of(s['ref'])==('cases' if s['kind']=='case' else 'amendments')
                listed.setdefault(s['ref'],set()).add((ch['chain_id'],s['step']))
        refs=[s['ref'] for s in st if s['ref']];assert len(refs)==len(set(refs)),ch['chain_id']
        # strictly chronological; a tie is allowed only for two full, identical dates (same-day judgments)
        for a,b in zip(st,st[1:]):
            da,db_=a['date'],b['date']
            if da[:4]==db_[:4]:assert len(da)==len(db_)==10,(ch['chain_id'],a['step'],b['step'])
            assert da<db_ or (da==db_ and len(da)==10),(ch['chain_id'],a['label_en'],b['label_en'])
    # every card listed in a chain carries that chain (and only chains that list it); no legacy single `chain`
    for c in ix.values():
        assert 'chain' not in c,c['id']
        have={(r['chain_id'],r['step']) for r in c.get('chains') or []}
        assert have==listed.get(c['id'],set()),c['id']
    # the property story starts with the 1st Amendment, then Shankari Prasad, and keeps the compensation cases
    prop=next(c for c in raw if c['chain_id']=='CH-property-ninth-schedule')['steps'];pr=[s['ref'] or s['label_en'] for s in prop]
    assert pr[:3]==['AM-001','CS-shankari-prasad-1951','Bela Banerjee (1953)']
    for x in ('AM-004','AM-017','CS-sajjan-singh-1964','CS-golaknath-1967','CS-rc-cooper-1970','AM-025','CS-kesavananda-1973','AM-044','CS-waman-rao-1980','CS-bhim-singhji-1980','CS-ir-coelho-2007','CS-property-owners-2024'):assert x in pr
    assert pr.index('CS-waman-rao-1980')<pr.index('CS-bhim-singhji-1980')
    res=[s['ref'] for s in next(c for c in raw if c['chain_id']=='CH-reservation')['steps']]
    for x in ('CS-mr-balaji-1962','CS-nm-thomas-1975','CS-indra-sawhney-ii-1999','CS-ajit-singh-ii-1999','CS-ashoka-kumar-thakur-2008','CS-jaishri-patil-2021'):assert x in res
    assert 'AM-025' in [s['ref'] for s in next(c for c in raw if c['chain_id']=='CH-amending-power')['steps']]

def test_theme_chain_map_points_to_real_chains():
    from app.services import recall_decks as rd
    rd.chains.cache_clear()
    assert rd.THEME_CHAIN['Speech, religion & minority rights']=='CH-speech'
    assert set(rd.THEME_CHAIN.values())<=set(rd.chains())

def test_case_card_shows_all_its_chains(client,app):
    from app.services import recall_decks as rd
    rd.chains.cache_clear();enable(app)
    page=client.get('/learn/polity/unit6/recall/cases').get_data(as_text=True)
    def card(cid):return frag(client,cid)
    def panels(g):
        box=g[g.index('class="ct-chains"'):];box=box[:box.index('<nav class="xr"')] if '<nav class="xr"' in box else box
        return box,re.findall(r'<section class="ct-chain" aria-label="([^"]+)" data-panel="(\d)" role="tabpanel"( hidden)?>',box)
    # Waman Rao: property chain first (its theme), then amending power; one current step per timeline
    box,P=panels(card('CS-waman-rao-1980'))
    assert [p[0] for p in P][:1]==['Right to property and the Ninth Schedule'] and 'Amending power and the basic structure' in [p[0] for p in P]
    assert P[0][2]=='' and all(p[2]==' hidden' for p in P[1:]) and box.count('aria-current="step"')==len(P)
    assert box.count('class="ct-tab"')==len(P) and 'data-tab="0"' in box and 'aria-selected="true"' in box
    prop=box[box.index('data-panel="0"'):box.index('data-panel="1"')]
    assert prop.index('data-go="AM-001"')<prop.index('data-go="CS-shankari-prasad-1951"')<prop.index('Bela Banerjee')<prop.index('aria-current="step"')<prop.index('data-go="CS-bhim-singhji-1980"')
    assert 'href="/learn/polity/unit6/recall/amendments?open=AM-001"' in prop and 'data-go="CS-waman-rao-1980"' not in box
    assert 'ct-st ev' in prop  # Bela Banerjee has no card: plain event step, not a link
    # Shankari Prasad: two timelines, amending power first
    box,P=panels(card('CS-shankari-prasad-1951'))
    assert [p[0] for p in P]==['Amending power and the basic structure','Right to property and the Ninth Schedule'] and box.count('aria-current="step"')==2
    # a single-chain case gets a timeline without tabs
    g=card('CS-davinder-singh-2024');assert 'class="ct-chain"' in g and 'ct-tab' not in g
    # theme view: one timeline per chain, each theme's own chain, with intro and no current step
    th=next(t for t in rd.themes('cases') if any(c['id']=='CS-waman-rao-1980' for c in t['cases']))
    tg=card(th['id']);assert tg.count('class="ct-chain"')==1 and 'Right to property and the Ninth Schedule' in tg and 'aria-current' not in tg and 'ct-chintro' in tg
    # amendment card: its chains, current step, cases link across decks
    am=client.get('/learn/polity/unit6/recall/amendments').get_data(as_text=True)
    g=frag(client,'AM-001')
    box,P=panels(g);assert len(P)==4 and box.count('aria-current="step"')==4 and 'href="/learn/polity/unit6/recall/cases?open=CS-shankari-prasad-1951"' in box
    assert 'Article 19 freedoms and their limits' in [p[0] for p in P] and 'href="/learn/polity/unit6/recall/cases?open=CS-romesh-thappar-1950"' in box

def test_case_tiles_and_hero_use_parties(client,app):
    enable(app)
    html=frag(client,'CS-kesavananda-1973')+frag(client,'CS-noise-pollution-2005')
    assert '<div class="s-short"><span class="ac-te" lang="te">కేశవానంద భారతి</span><span class="ac-en" lang="en">Kesavananda Bharati</span></div>' in html
    assert '<span class="ac-en" lang="en">vs State of Kerala</span>' in html
    assert '<span class="ac-en" lang="en">Kesavananda Bharati vs State of Kerala</span></div>' in html
    assert '<div class="s-vs"></div>' in html  # 'In re:' references have no vs line
    js=open('static/polity_articles.js',encoding='utf-8').read()
    assert 't-p1' in js and 't-vs' in js and 'p-parties' in js and 'p-short' in js

def _rich(rd,monkeypatch):
    orig,cache=rd.items,{}
    R={'AC-6.4-21':dict(one_line_en='ONE-21',one_line_te='ఒక్క 21',text_en='No person shall be deprived of his life.',text_te='ఏ వ్యక్తి ప్రాణాన్నీ.',
        meaning_en='MEANING since Maneka Gandhi and the 44th Amendment; Article 21 itself.',meaning_te='మేనకా గాంధీ కేసు తర్వాత అర్థం.',
        implications_en=['IMP Article 20 and Article 20 again'],implications_te=['ప్రకరణ 20'],
        amendments=[{'id':'AM-044','label_en':'44th Amendment (1978)','label_te':'44వ సవరణ','what_en':'WHAT44','what_te':'ఏమి'}],
        cases=[{'id':'CS-maneka-gandhi-1978','label_en':'Maneka Gandhi vs Union of India','label_te':'మేనకా','held_en':'HELD-MG','held_te':'చెప్పింది'}],
        exam={'pyqs':[{'kind':'pyq','exam':'APPSC','q_en':'PYQ Maneka Gandhi Article?','q_te':'మేనకా గాంధీ?','answer_en':'Article 21','answer_te':'ప్రకరణ 21'}]}),
       'AM-042':dict(one_line_en='ONE-42',one_line_te='ఒక్క 42',background_en='WHY-42',background_te='ఎందుకు',
        changes=[{'article':'AC-6.7-368','label_en':'Article 368','label_te':'ప్రకరణ 368','kind':'amended','before_en':'BEFORE','before_te':'ముందు','after_en':'AFTER','after_te':'తర్వాత','what_en':'Struck down in Minerva Mills.','what_te':'కొట్టివేసింది'}],
        cases=[{'id':'CS-minerva-mills-1980','label_en':'Minerva Mills','label_te':'మినర్వా','held_en':'HELD-MM','held_te':'చెప్పింది'}])}
    def items(d):
        if d not in cache:cache[d]=[dict(c,**R[c['id']]) if c['id'] in R else c for c in orig(d)]
        return cache[d]
    monkeypatch.setattr(rd,'items',items)

def test_recall_links_resolve(app):
    from app.services import recall_decks as rd
    L=rd.links();assert L,'links.json missing'
    ids=set(rd.index()['cards'])
    for cid,v in L.items():
        assert cid in ids,cid
        for k in ('articles','amendments','cases'):
            for x in v.get(k,[]):assert x in ids and rd.deck_of(x)==k,(cid,x)
    with app.test_request_context():r=rd.related(rd.index()['cards']['AC-6.4-21'])
    assert any(x['id']=='CS-maneka-gandhi-1978' and x['en']=='Maneka Gandhi' for x in r['cases'])
    assert rd.label('AM-042')==('42nd Amdt','42వ సవరణ') and rd.label('AC-6.4-21')[0]=='Art 21'

def test_recall_autolink_filter(app):
    from app.services import recall_decks as rd
    with app.test_request_context():
        s=str(rd.autolink('Since Maneka Gandhi (1978) and Maneka Gandhi again, Article 21 and Article 21A; the 42nd Amendment <b>; ప్రకరణ 368.','AC-6.4-21'))
    assert s.count('data-go="CS-maneka-gandhi-1978"')==1 and 'class="xl xl-case"' in s  # one link per target per field
    assert 'data-go="AC-6.4-21"' not in s and 'data-go="AC-6.4-21A"' in s  # own name skipped; longest match wins
    assert 'xl-am" data-go="AM-042"' in s and 'data-go="AC-6.7-368"' in s and '&lt;b&gt;' in s  # Telugu variant; text escaped
    assert str(rd.autolink('',None))==''

def test_recall_rich_article_amendment_and_cross_deck(client,app,monkeypatch):
    from app.services import recall_decks as rd
    enable(app);_rich(rd,monkeypatch)
    def card(page,cid):return frag(client,cid)
    page=client.get('/learn/polity/unit6/recall/articles?open=AC-6.4-21&back=cases:CS-maneka-gandhi-1978').get_data(as_text=True)
    assert 'data-open="AC-6.4-21"' in page and 'data-back-url="/learn/polity/unit6/recall/cases?open=CS-maneka-gandhi-1978"' in page and 'data-back-en="Maneka Gandhi case"' in page
    a=card(page,'AC-6.4-21')
    for t in ('ONE-21','ప్రకరణ పాఠం','అనువాదం (translation)','ముఖ్యమైన అంశాలు','WHAT44','HELD-MG','class="xr"','ct-exam'):assert t in a,t
    mean=a[a.index('MEANING'):a.index('MEANING')+900]
    assert 'data-go="CS-maneka-gandhi-1978"' in mean and 'data-go="AM-044"' in mean
    imp=a[a.index('IMP '):a.index('</li>',a.index('IMP '))];assert imp.count('data-go="AC-6.4-20"')==1
    pyq=a[a.index('ct-pyqs'):];pyq=pyq[:pyq.index('</ol>')];assert 'class="xl' not in pyq  # bank text never linked
    assert a.index('class="xr"')<a.index('ct-exam')
    am=card(client.get('/learn/polity/unit6/recall/amendments').get_data(as_text=True),'AM-042')
    for t in ('ONE-42','WHY-42','BEFORE','AFTER','xm-changes','data-go="AC-6.7-368"','HELD-MM','data-go="CS-minerva-mills-1980"'):assert t in am,t
    # unknown ?open / bad back are ignored
    p2=client.get('/learn/polity/unit6/recall/cases?open=NOPE&back=articles:CS-x').get_data(as_text=True)
    assert 'data-open=""' in p2 and 'data-back-url' not in p2

def test_recall_fallback_without_rich_fields_and_links(client,app,monkeypatch):
    from app.services import recall_decks as rd
    enable(app)
    def card(page,cid):return frag(client,cid)
    a=card(client.get('/learn/polity/unit6/recall/articles').get_data(as_text=True),'AC-6.4-21')
    # real data now carries the rich fields
    assert 'ప్రకరణ పాఠం' in a and 'ct-exam' in a
    am=card(client.get('/learn/polity/unit6/recall/amendments').get_data(as_text=True),'AM-042')
    assert 'xm-changes' in am and 'class="xr"' in am and 'ct-exam' in am
    monkeypatch.setattr(rd,'LINKS_FILE',rd.DIR/'__missing__.json');rd.links.cache_clear()
    try:
        assert rd.links()=={}
        a=card(client.get('/learn/polity/unit6/recall/articles').get_data(as_text=True),'AC-6.4-21')
        assert 'ప్రకరణ పాఠం' in a  # structured fields still give a Related strip
    finally:
        monkeypatch.undo();rd.links.cache_clear()

def _lax_fields(rd,monkeypatch):
    """In-memory Laxmikanth ch.91/92 fields: a Romesh Thappar-like card (popular name, topic, schedule) and Puttaswamy (right added to Art 21)."""
    orig,cache=rd.items,{}
    rt=dict(next(c for c in orig('cases') if c['id']=='CS-gopalan-1950'),id='CS-zz-fixture-1950',chains=[],compare=None,
            front_en='Romesh Thappar case',front_te='రొమేష్ థాపర్ కేసు',short_en='Romesh Thappar',short_te='రొమేష్ థాపర్',vs_en='vs State of Madras',vs_te='vs మద్రాస్ రాష్ట్రం',
            parties_en='Romesh Thappar vs State of Madras',parties_te='రొమేష్ థాపర్ vs మద్రాస్ రాష్ట్రం',theme_en='Speech, religion & minority rights',theme_te=None,
            cue_en='Ban on a journal violated free speech',cue_te='పత్రికపై నిషేధం భావ ప్రకటన స్వేచ్ఛకు భంగం',title_en='Romesh Thappar vs State of Madras — press freedom',title_te='రొమేష్ థాపర్ vs మద్రాస్ రాష్ట్రం — పత్రికా స్వేచ్ఛ',
            popular_en='Cross Roads case',popular_te='క్రాస్ రోడ్స్ కేసు',topic_en='Freedom of the press',topic_te='పత్రికా స్వేచ్ఛ',
            articles=['19(1)(a)','19(2)'],schedules=['Ninth Schedule'],
            impact_en='IMPACT-RT: it led to the 1st Amendment, which widened Article 19(2); see Maneka Gandhi case.',impact_te='ప్రభావం: 1వ సవరణ వచ్చింది.')
    put=dict(right_en='Right to privacy',right_te='గోప్యత హక్కు',popular_en='Privacy case',popular_te='ప్రైవసీ కేసు',impact_en=['IMPACT-P1','IMPACT-P2'],impact_te=['ప్రభావం 1','ప్రభావం 2'])
    def items(d):
        if d not in cache:
            L=[dict(c,**put) if c['id']=='CS-puttaswamy-2017' else c for c in orig(d)]
            if d=='cases':L=[c for c in L if c['id']!='CS-romesh-thappar-1950'];L.append(rd._theme_fields(rt) or rt)
            cache[d]=L
        return cache[d]
    monkeypatch.setattr(rd,'items',items)

def test_case_laxmikanth_fields_render_and_fallback(client,app,monkeypatch):
    from app.services import recall_decks as rd
    enable(app)
    def card(page,cid):return frag(client,cid)
    # without the fields: no hero extras, no impact box; article chips still shown
    g=card(client.get('/learn/polity/unit6/recall/cases').get_data(as_text=True),'CS-central-coal-fields-1980')
    for t in ('s-pop','s-topic','ch-right','ct-impact','ch-sch','Popular name'):assert t not in g,t
    assert 'class="s-hero"' in g and 'data-go="AC-' in g
    _lax_fields(rd,monkeypatch)
    page=client.get('/learn/polity/unit6/recall/cases').get_data(as_text=True)
    r=card(page,'CS-zz-fixture-1950')
    assert 'ప్రసిద్ధ పేరు / Popular name:' in r and 'Cross Roads case' in r and 'క్రాస్ రోడ్స్ కేసు' in r
    assert 'అంశం / Topic:' in r and 'Freedom of the press' in r and 'పత్రికా స్వేచ్ఛ' in r
    assert 'class="ac-art ch-sch">Ninth Schedule<' in r and 'data-go="AC-6.4-19"' in r and 'ch-right' not in r
    imp=r[r.index('ct-impact'):];imp=imp[:imp.index('</section>')]
    assert 'తీర్పు ప్రభావం' in imp and 'Impact of the judgement' in imp and 'data-go="CS-maneka-gandhi-1978"' in imp and 'data-go="AM-001"' in imp
    assert r.index('ct-sec ct-mean')<r.index('ct-sec ct-impact')
    p=card(page,'CS-puttaswamy-2017')
    assert 'ప్రకరణ 21 కు జోడించిన హక్కు / Right added to Article 21:' in p and 'Right to privacy' in p and 'గోప్యత హక్కు' in p
    assert p.index('ct-sec ct-mean')<p.index('ct-sec ct-impact')<p.index('ct-sec ct-next') and '<span class="ac-p">IMPACT-P1</span><span class="ac-p">IMPACT-P2</span>' in p
    js=open('static/polity_articles.js',encoding='utf-8').read()
    assert 's-popline' in js and 't-pop' in js and 'run.density === "18"' in js and 's-topic' in js

def test_case_popular_name_autolinks(app,monkeypatch):
    from app.services import recall_decks as rd
    _lax_fields(rd,monkeypatch)
    with app.test_request_context():
        s=str(rd.autolink('The Cross Roads case and the క్రాస్ రోడ్స్ కేసు; Privacy case. Fundamental Rights and privacy are generic.','AC-6.4-21'))
    assert s.count('data-go="CS-zz-fixture-1950"')==1 and s.count('data-go="CS-puttaswamy-2017"')==1
    assert '>Cross Roads case</a>' in s and '>Privacy case</a>' in s and '>privacy<' not in s
    assert 'Fundamental Rights and' in s


def test_recall_lazy_card_endpoint_filters_and_deep_link(client,app):
    from app.services import recall_decks as rd
    enable(app)
    # the deck page carries light tile data only; full cards come from the endpoint
    for d,limit in (('articles',450_000),('amendments',200_000),('cases',400_000)):
        page=client.get(f'/learn/polity/unit6/recall/{d}').get_data(as_text=True)
        assert len(page.encode())<limit,(d,len(page.encode()))
        assert 'class="s-back"' not in page and 'ct-exam' not in page
        assert 'data-card-url="/learn/polity/unit6/recall/%s/card/__ID__"'%d in page
        D=deck_data(page);assert D['v']==rd.data_version() and all({'id','n','f','c','p','u','acc','two'}<=set(x) for x in D['cards'])
    r=client.get('/learn/polity/unit6/recall/cases/card/CS-kesavananda-1973')
    assert r.status_code==200 and r.mimetype=='text/html' and r.get_data(as_text=True).lstrip().startswith('<article class="ac-src"')
    g=r.get_data(as_text=True);assert '<!doctype' not in g.lower() and 'class="s-back"' in g and 'ct-exam' in g and 'class="xr"' in g
    et=r.headers['ETag'];assert rd.data_version() in et and 'no-cache' in r.headers['Cache-Control']
    assert 'max-age' in client.get('/learn/polity/unit6/recall/cases/card/CS-kesavananda-1973?v=x').headers['Cache-Control']
    assert client.get('/learn/polity/unit6/recall/cases/card/CS-kesavananda-1973',headers={'If-None-Match':et}).status_code==304
    assert 'ac-thlist' in client.get('/learn/polity/unit6/recall/cases/card/TH-basic').get_data(as_text=True)
    for u in ('/learn/polity/unit6/recall/cases/card/NOPE','/learn/polity/unit6/recall/cases/card/AC-6.4-21','/learn/polity/unit6/recall/nope/card/AC-6.4-21'):
        assert client.get(u).status_code==404,u
    # ?open= deep link still works (the card is fetched by the page); unknown ids are dropped
    p=client.get('/learn/polity/unit6/recall/amendments?open=AM-042').get_data(as_text=True)
    assert 'data-open="AM-042"' in p and any(x['id']=='AM-042' for x in deck_data(p)['cards'])
    # Part / Unit on every card; filters on the setup screen; ?chapter= still works
    assert rd.part_of_article('21')=='Part III' and rd.part_of_article('51A(a)')=='Part IVA' and rd.part_of_article('243ZH')=='Part IXB'
    assert rd.part_of_article('243P')=='Part IXA' and rd.part_of_article('323A')=='Part XIVA' and rd.part_of_article('Preamble')=='Preamble' and rd.norm_part('Part XIV-A')=='Part XIVA'
    for d in rd.DECKS:
        assert all(i['part'] in rd.PART_BY and i['unit'] in rd.UNITS for i in rd.items(d)),d
    a=next(i for i in rd.items('articles') if i['id']=='AC-6.4-21');assert (a['part'],a['unit'])==('Part III',6)
    m=next(i for i in rd.items('amendments') if i['id']=='AM-044');assert m['part']!='General'
    cases=client.get('/learn/polity/unit6/recall/cases').get_data(as_text=True)
    n3=sum(1 for i in rd.items('cases') if i['part']=='Part III')
    assert f'data-pcount="Part III">{n3}<' in cases and 'name="unit" value="6"' in cases and 'name="chapter"' not in cases
    ch=client.get('/learn/polity/unit6/recall/cases?chapter=6.4').get_data(as_text=True)
    assert 'name="chapter" value="6.4" checked' in ch and 'data-chapter="6.4"' in ch
    js=open('static/polity_articles.js',encoding='utf-8').read()
    for t in ('ac-data','cardUrl','prefetch(','passes(','data-retry','u6_artcards_v1'):assert t in js,t
    # hub renamed, URLs unchanged
    h=client.get('/learn/polity/unit6/recall').get_data(as_text=True)
    assert 'Polity recall cards' in h and '<span class="ac-te" lang="te">పాలిటీ' not in h and '/learn/polity/unit6/recall/cases"' in h


def test_recall_entry_on_polity_page_and_start_first(client,app):
    from app.services import recall_decks as rd
    enable(app)
    h=client.get('/learn/polity/unit6/').get_data(as_text=True)
    # recall decks sit above the units, each tile opens its deck directly (hub skipped) with its count
    assert h.index('class="card pr"')<h.index('u6-unit')
    for d in rd.DECKS:
        assert f'/learn/polity/unit6/recall/{d}?from=polity"' in h and f'data-total="{len(rd.items(d))}"' in h
    assert 'Articles' in h and 'Amendments' in h and 'Cases' in h and 'ప్రకరణలు' not in h and '/learn/polity/unit6/recall"' in h
    c=client.get('/learn/polity/unit6/recall/cases?from=polity').get_data(as_text=True)
    assert '‹ Polity' in c and '‹ Recall cards' in client.get('/learn/polity/unit6/recall/cases').get_data(as_text=True)
    # Start (with live count) comes before every optional filter; Continue sits beside it
    assert c.index('id="ac-start"')<c.index('name="partall"')<c.index('name="order"') and 'id="ac-cont"' in c
    js=open('static/polity_articles.js',encoding='utf-8').read()
    for t in ('POS_KEY','continueRun','savePos','paintContinue'):assert t in js,t
    assert '‹ Polity' in client.get('/learn/polity/unit6/recall').get_data(as_text=True)


def test_recall_refresh_drops_stale_cache(monkeypatch):
    from app.services import recall_decks as rd
    rd.items('cases');rd.refresh();n=rd.items.cache_info().currsize
    monkeypatch.setattr(rd,'data_version',lambda:'changed');rd.refresh()
    assert n and rd.items.cache_info().currsize==0

def test_related_jump_row_and_for_matrix(client,app):
    enable(app)
    from app.services import recall_decks as rd
    with app.test_request_context():
        R=rd.related(rd.index()['cards']['AC-6.1-324'])
    h=frag(client,'AC-6.1-324')
    assert 'class="xj"' in h and h.index('class="xj"')<h.index('class="xr"')  # jump row sits above the Related strip
    assert f'ఈ ప్రకరణపై కేసులు' in h and f'<b class="xj-n">{len(R["cases"])}</b>' in h and f'<b class="xj-n">{len(R["amendments"])}</b>' in h
    assert '?for=AC-6.1-324&amp;back=articles%3AAC-6.1-324' in h
    p=client.get('/learn/polity/unit6/recall/cases?for=AC-6.1-324&back=articles:AC-6.1-324').get_data(as_text=True)
    ids=re.search(r'data-for-ids="([^"]*)"',p).group(1).split(',')
    assert ids==[r['id'] for r in R['cases']] and 'data-for-id="AC-6.1-324"' in p
    assert 'data-back-url=' in p and 'open=AC-6.1-324' in p
    p2=client.get('/learn/polity/unit6/recall/cases?for=AC-6.1-324').get_data(as_text=True)  # back defaults to the source card
    assert 'data-back-deck="articles"' in p2
    assert client.get('/learn/polity/unit6/recall/cases?for=NOPE').status_code==404
    am=frag(client,'AM-007');assert 'Articles changed' in am and 'xj-cases' in h

def test_setup_more_options_and_slim_nav(client,app):
    enable(app)
    p=client.get('/learn/polity/unit6/recall/articles').get_data(as_text=True)
    more=p[p.index('id="ac-more"'):p.index('</details>',p.index('id="ac-more"'))]
    for n in ('density','lang','order','only'):assert f'name="{n}"' in more
    assert 'మరిన్ని ఎంపికలు' in more and 'id="ac-more-sum"' in more
    assert 'name="part"' not in more and 'name="unit"' not in more and p.index('id="ac-start"')<p.index('id="ac-more"')
    assert 'class="nv-l"' in client.get('/learn/').get_data(as_text=True)


def _pyq_bank():
    import json
    from pathlib import Path
    root=Path(__file__).resolve().parents[1]/'content'/'polity'/'g2'
    bank={}
    for f in root.glob('**/PYQ-Set.json'):
        for q in json.loads(f.read_text(encoding='utf-8'))['questions']:bank[q['id']]=(q['question_en'],q['options_en'],q['study_answer'] or q.get('answer'))
    for q in json.loads((root/'_shared'/'PYQs.json').read_text(encoding='utf-8')):bank[q['id']]=(q['question_en'],q['options_en'],q['answer'])
    return root,bank


def test_recall_pyq_count_matches_cards_and_map():
    """Card PYQs are copied exactly from the master bank (content/polity/pyq_bank), key = correct_option's text; repeats grouped."""
    import json,re
    from pathlib import Path
    from app.services import recall_decks as rd
    root=Path(__file__).resolve().parents[1]/'content'/'polity'
    mb={r['record_id']:r for r in json.loads((root/'pyq_bank'/'indian_polity_pyq_bank_v3.71.0.json').read_text(encoding='utf-8'))}
    pm=json.loads((root/'g2'/'recall_decks'/'pyq_map.json').read_text(encoding='utf-8'))
    total=0
    for d in rd.DECKS:
        for it in rd.items(d):
            ps=(it.get('exam') or {}).get('pyqs') or [];real=[p for p in ps if p.get('kind')=='pyq']
            assert it.get('pyq_count',0)==len(real),it['id']
            assert it.get('tested_count',0)==sum(len(p.get('asked') or [1]) for p in real),it['id']
            assert ps[:len(real)]==real,it['id']
            yrs=[int(m.group()) if (m:=re.search(r'\d{4}',str(p.get('year') or ''))) else 0 for p in real];assert yrs==sorted(yrs,reverse=True),it['id']
            mids={x for p in real for x in (p.get('master_ids') or [p.get('master_id')]) if x}
            assert {x[4:] for x in pm.get(it['id'],[])}<=mids,it['id']
            for p in real:
                r=mb.get(p.get('master_id'))
                if not r:
                    continue
                opts=[r[f'option_{k}'] for k in range(1,5)]
                assert p['q_en']==r['question_en'] and p['options_en']==opts,(it['id'],p['id'])
                ka=r.get('key_audit') or {}
                assert not ka.get('excluded'),(it['id'],p['id'])
                if ka.get('study_answer'):  # audited key wins over the recorded correct_option
                    assert p['answer_en']==opts[ka['study_answer']-1] and bool(p.get('disputed'))==(not ka['scored']),(it['id'],p['id'])
                elif ka:
                    assert p.get('disputed'),(it['id'],p['id'])
                elif r['correct_option'] in ('1','2','3','4'):
                    assert p['answer_en']==opts[int(r['correct_option'])-1],(it['id'],p['id'])
                if not r['question_te']:
                    assert p['q_te'] in ('',) or p['id'][4:]==r['record_id'] or p.get('translated')  # empty unless the app's own Telugu exists or ours (translated:true)
            total+=len(real)
    assert total>=600 and len({i for v in pm.values() for i in v})>=300


def test_recall_pyq_chip_badge_and_filter(client,app):
    from app.services import recall_decks as rd
    enable(app)
    its={i['id']:i for i in rd.items('articles')}
    g=frag(client,'AC-6.4-32')
    n=its['AC-6.4-32']['pyq_count'];assert n>12
    assert 'class="xj-go xj-pyq" data-pyq="pyq-AC-6.4-32" href="#pyq-AC-6.4-32"' in g and 'PYQలు' in g and f'<b class="xj-n">{n}</b>' in g
    assert 'id="pyq-AC-6.4-32"' in g and 'data-pyqall="pyq-AC-6.4-32"' in g and g.count('data-more hidden')==n+len([p for p in its['AC-6.4-32']['exam']['pyqs'] if p.get('kind')!='pyq'])-6
    zero=next(i for i in its.values() if not i.get('pyq_count'))
    assert 'xj-pyq' not in frag(client,zero['id'])
    page=client.get('/learn/polity/unit6/recall/articles').get_data(as_text=True)
    assert 'name="pyq"' in page and 'Only asked in PYQs' in page and 'PYQ వచ్చినవి మాత్రమే' in page
    D=deck_data(page);q={x['id']:x.get('q') for x in D['cards']}
    assert q['AC-6.4-32']==n and q[zero['id']] is None
    js=open('static/polity_articles.js',encoding='utf-8').read();assert 'o.q > 0' in js and 't-pyq' in js and 'showPyqs' in js


def test_omitted_articles_data():
    import re
    from app.services import article_cards as ac, recall_decks as rd
    cards={c['id']:c for c in ac.all_cards()};ams={i['id'] for i in rd.items('amendments')}
    om={k:ac.omitted_list(c) for k,c in cards.items() if c.get('omitted')}
    # existing cards carry the omission; whole Articles vs clauses
    for k in ('AC-6.4-31','AC-6.9-2A','AC-6.8-329A'):assert ac.omitted_whole(cards[k]),k
    assert [o['clause'] for o in om['AC-6.4-19']]==['19(1)(f)'] and om['AC-6.4-19'][0]['by']=='AM-044' and not ac.omitted_whole(cards['AC-6.4-19'])
    assert om['AC-p5-132'][0]['clause']=='132(2)' and om['AC-6.4-31'][0]['by']=='AM-044'
    # new compact cards for omitted Articles that had none
    for a in ('31D','32A','131A','144A','226A','228A','238','257A','268A','272','278','291','306','359A','362'):
        c=cards[f'AC-om-{a}'];assert c['article']==a and ac.omitted_whole(c) and c['text_en'].startswith(f'{a}. [') and 'Omitted' in c['text_en']
        assert c['part']==rd.part_of_article(a) and c['unit'] in rd.UNITS and c['exam']['patterns_en'] and len(c['exam']['patterns_en'])==len(c['exam']['patterns_te'])
    assert cards['AC-om-238']['part']=='Part VII' and om['AC-om-291'][0]['by']=='AM-026' and om['AC-om-272'][0]['by'] is None
    for k,L in om.items():
        for o in L:
            for f in ('what_en','what_te','by_label_en','by_label_te','said_en','said_te','why_en','why_te','wef'):assert o.get(f),(k,f)
            assert o['by'] is None or o['by'] in ams,(k,o['by'])
            assert re.fullmatch(r'\d{1,2}-\d{1,2}-\d{4}',o['wef']),k
            assert re.search(r'[ఀ-౿]',o['said_te']+o['why_te']+o['what_te']),k
    assert len({c['id'] for c in cards.values()})==len(cards)


def test_omitted_banner_badge_and_filter(client,app):
    from app.services import recall_decks as rd
    enable(app)
    g=frag(client,'AC-6.4-31')
    assert 'class="om-ban whole"' in g and 'ఈ ప్రకరణను' in g and 'రద్దు చేసింది (Omitted)' in g and 'data-go="AM-044"' in g and '20-6-1979' in g
    g=frag(client,'AC-6.4-19')
    assert 'class="om-ban"' in g and 'class="om-cl"><dt>19(1)(f)<span class="om-tag">' in g and 'ఆస్తి హక్కు' in g and 'తొలగించింది' in g
    assert 'class="om-cl"><dt>132(2)' in frag(client,'AC-p5-132')
    g=frag(client,'AC-om-226A');assert 'om-ban whole' in g and 'data-go="AM-043"' in g and 'PYQ-POL-C150CC03972F' not in g or 'PYQ' in g
    assert 'om-ban' not in frag(client,'AC-6.4-21')
    page=client.get('/learn/polity/unit6/recall/articles').get_data(as_text=True)
    assert 'name="om"' in page and 'Omitted only' in page and 'రద్దయినవి మాత్రమే' in page and 'polity_articles.js?v=st2' in page
    D={x['id']:x.get('om') for x in deck_data(page)['cards']}
    assert D['AC-6.4-31']==2 and D['AC-om-238']==2 and D['AC-6.4-19']==1 and D['AC-6.4-21'] is None
    n=sum(1 for i in rd.items('articles') if i.get('omitted'));assert f'Omitted only' in page and f'<small> ({n})</small>' in page
    js=open('static/polity_articles.js',encoding='utf-8').read();assert 'o.om > 0' in js and 't-om' in js and 'data-om=' in js
    css=open('static/polity_articles.css',encoding='utf-8').read();assert '.om-ban' in css and '.t-om' in css


def test_quick_revision_list(client,app):
    enable(app)
    r=client.get('/learn/polity/unit6/revise?kind=both&qlang=both');html=r.get_data(as_text=True)
    assert r.status_code==200 and 'rv-jump' in html and 'Fundamental Rights' in html
    p=client.get('/learn/polity/unit6/revise/part?ch=lx8&kind=pyq&qlang=en').get_data(as_text=True)
    assert 'rv-ab' in p and 'back=' in p and 'review=1' in p
    assert client.get('/learn/polity/unit6/revise/part?ch=nope&kind=pyq').status_code==404


def test_concept_book(client,app):
    enable(app)
    h=client.get('/learn/polity/unit6/facts').get_data(as_text=True)
    assert 'qb-ch' in h and '<details' in h and 'Historical Background' in h
    p=client.get('/learn/polity/unit6/facts/part?sub=pres-election')
    assert p.status_code==200 and 'cg-glance' in p.get_data(as_text=True)
