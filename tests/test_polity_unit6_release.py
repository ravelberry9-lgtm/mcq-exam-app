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
