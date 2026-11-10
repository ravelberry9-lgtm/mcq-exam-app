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
