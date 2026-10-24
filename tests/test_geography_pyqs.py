from copy import deepcopy
import hashlib
import json
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import pytest
from app.services import geography_pyqs as service

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "content/geography/release_manifest.json").read_text(encoding="utf-8"))

class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=='a' and 'data-chapter-link' in d:self.links.append(d['href'])

def test_exact_source_preservation_exclusions_and_holds(app):
    release=service.records()
    assert len(release)==976
    assert service.summary()=={'total':976,'held':240,'scorable':736}
    assert {r['source']['id'] for r in release}==set(MANIFEST['included_source_hashes'])
    assert len(MANIFEST['excluded_archive_ids'])==114
    assert not set(MANIFEST['excluded_archive_ids']) & set(MANIFEST['included_source_hashes'])
    for r in release:
        data=json.dumps(r['source'],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
        assert hashlib.sha256(data).hexdigest()==MANIFEST['included_source_hashes'][r['source']['id']]
        assert r['baseline_must_disable_scoring']==(r['source']['id'] in MANIFEST['mandatory_held_ids'])
        assert r['must_disable_scoring']==(r['source']['id'] in MANIFEST['mandatory_held_ids'] and r['source']['id'] not in MANIFEST['cleared_ids'])
        assert r['routes']


def test_all_questions_render_and_all_chapter_links_resolve(client):
    checked=set()
    for record in service.records():
        qid=record['source']['id'];page=client.get('/learn/geography/pyq/'+qid)
        assert page.status_code==200,qid
        parser=Links();parser.feed(page.data.decode())
        assert len(parser.links)==len(record['routes'])
        for link in parser.links:
            if link not in checked:
                assert client.get(urlsplit(link).path).status_code==200,link
                checked.add(link)
        if record['must_disable_scoring']:
            assert b'data-scorable="false"' in page.data and b'data-scoring-hold' in page.data
        assert b'data-correct=' not in page.data
    assert len(checked)>=83

def test_all_mandatory_holds_refuse_forged_scores(client):
    for record in service.records():
        if not record['must_disable_scoring']:continue
        qid=record['source']['id']
        for choice in (1,2,3,4):
            assert service.grade(record,choice)=={'status':'unscored','score':None,'correct':None}
        response=client.post('/learn/geography/pyq/'+qid+'/answer',data={'choice':'1','score':'1','must_disable_scoring':'false','scorable':'true','correct_answer':'1'})
        assert response.status_code==200
        assert b'data-result="unscored"' in response.data
        assert b'data-score=' not in response.data

def test_all_resolved_keys_score_without_overriding_holds(app):
    for record in service.records():
        accepted=service.accepted_options(record)
        if accepted:
            assert not record['must_disable_scoring']
            assert len(service.options(record))==4
            for choice in (1,2,3,4):
                outcome=service.grade(record,choice)
                assert outcome['score']==int(choice in accepted)
        else:assert service.grade(record,1)['score'] is None
    q=service.question('APPSC-G2-GEO-0050')
    assert service.accepted_options(q)==(1,3)
    assert service.grade(q,1)['score']==1 and service.grade(q,3)['score']==1
    assert service.grade(q,2)['score']==0
    held=service.question('APPSC-G2-GEO-0063')
    assert service.accepted_options(held)==() and service.grade(held,1)['score'] is None

def test_missing_conflicting_or_untrusted_keys_fail_closed(app):
    source=service.question('APPSC-G2-GEO-0041')
    for change in ({'answer_index':None,'answer_text':'unavailable'}, {'answer_index':9}, {'answer_text':'Option 1'}, {'practice_scorable':False}, {'editorial_quarantine':True}, {'answer_available':False}):
        q=deepcopy(source);q['source'].update(change)
        assert service.accepted_options(q)==()
    q=deepcopy(source);q['must_disable_scoring']=None;assert not service.accepted_options(q)
    q=deepcopy(source);q['source'].update(options_en=[],options_bilingual=None);assert not service.accepted_options(q)
    assert service.rich('<script>alert(1)</script>').find('<script>')==-1
    assert 'href=' not in service.rich('[unsafe](javascript:alert(1))')

def test_filters_pagination_and_archived_records_are_unreachable(client):
    page=client.get('/learn/geography/pyqs')
    assert page.status_code==200 and b'data-pyq-count="976"' in page.data and b'data-pyq-held="240"' in page.data
    assert page.data.count(b'data-geography-pyq=')==20
    held=service.filtered(mode='held');assert len(held)==240
    for lesson in ('01','44B','68'):
        rows=service.filtered(lesson=lesson)
        assert all(any(x['lesson_id']==lesson for x in r['routes']) for r in rows)
        assert client.get('/learn/geography/pyqs?lesson='+lesson).status_code==200
    assert client.get('/learn/geography/pyqs?unit=17').status_code==404
    assert client.get('/learn/geography/pyqs?lesson=99').status_code==404
    assert client.get('/learn/geography/pyqs?mode=unsafe').status_code==400
    assert client.get('/learn/geography/pyqs?page=bad').status_code==200
    for qid in MANIFEST['excluded_archive_ids']:
        assert client.get('/learn/geography/pyq/'+qid).status_code==404
        assert client.post('/learn/geography/pyq/'+qid+'/answer',data={'choice':'1'}).status_code==404
    response=client.post('/learn/geography/pyq/APPSC-G2-GEO-0041/answer',data={'choice':'99'})
    assert response.status_code==400

def test_answer_route_requires_csrf_and_not_a_client_key(client):
    client.auto_csrf=False
    response=client.post('/learn/geography/pyq/APPSC-G2-GEO-0041/answer',data={'choice':'4'})
    assert response.status_code==400
    client.auto_csrf=True
    page=client.post('/learn/geography/pyq/APPSC-G2-GEO-0041/answer',data={'choice':'1','correct_answer':'1','score':'1'})
    assert page.status_code==200 and b'data-score="0"' in page.data
    page=client.post('/learn/geography/pyq/APPSC-G2-GEO-0050/answer',data={'choice':'3'})
    assert page.status_code==200 and b'data-score="1"' in page.data


def test_decimal_option_contents_are_not_split_as_option_labels(app):
    q=service.question('APPSC-G2-GEO-0011')
    assert [o['text'] for o in service.options(q)]==['1.15; 0.80; 1.52','1.52; 1.15; 0.80','1.52; 0.80; 1.15','1.15; 1.52; 0.80']
    assert service.accepted_options(q)==(1,)


def test_chapter_practice_keeps_its_filter_for_answers_and_navigation(client):
    rows=service.filtered(lesson='04')
    first=rows[0]['source']['id'];second=rows[1]['source']['id']
    page=client.get('/learn/geography/pyq/'+first+'?lesson=04')
    assert page.status_code==200
    assert ('/learn/geography/pyq/'+second+'?lesson=04').encode() in page.data
    assert ('/learn/geography/pyq/'+first+'/answer?lesson=04').encode() in page.data
    page=client.post('/learn/geography/pyq/'+first+'/answer?lesson=04',data={'choice':'1'})
    assert page.status_code==200
    assert ('/learn/geography/pyq/'+second+'?lesson=04').encode() in page.data
    assert client.get('/learn/geography/pyq/'+first+'?lesson=99').status_code==404


def test_reviewed_chart_questions_keep_original_records_and_grade_verified_keys(client):
    for number,answer in [(117,2),(118,4),(119,4),(120,1)]:
        qid=f'APPSC-G1-362016-GEO-{number}';record=service.question(qid)
        assert record['baseline_must_disable_scoring'] is True
        assert record['source']['practice_scorable'] is False
        assert record['source']['editorial_quarantine'] is True
        assert service.accepted_options(record)==(answer,)
        page=client.get('/learn/geography/pyq/'+qid)
        assert page.status_code==200 and b'data-reviewed-chart' in page.data
        assert b'Bean growth chart data' in page.data and b'21' in page.data
        assert b'data-scoring-hold' not in page.data
        for choice in (1,2,3,4):
            page=client.post('/learn/geography/pyq/'+qid+'/answer',data={'choice':str(choice)})
            assert f'data-score="{int(choice==answer)}"'.encode() in page.data
        changed=deepcopy(record);changed['source']['question_en']+=' altered'
        assert service.grade(changed,answer)['score'] is None


def test_review_clearance_fails_closed_if_chart_is_missing_or_corrupt(app,tmp_path,monkeypatch):
    record=service.question('APPSC-G1-362016-GEO-118')
    with app.app_context():
        monkeypatch.setattr(app,'static_folder',str(tmp_path))
        assert service.grade(record,4)['score'] is None
        visual=record['review']['required_visual'];p=tmp_path/visual['path'];p.parent.mkdir(parents=True);p.write_bytes(b'wrong-image')
        assert service.grade(record,4)['score'] is None
        assert service.summary()=={'total':976,'held':244,'scorable':732}


def test_review_file_hash_is_required(tmp_path):
    path=tmp_path/'reviews.json';path.write_text('{"format":"geography-hold-review-v1","reviews":[]}',encoding='utf-8')
    assert service._read_reviews(str(path),path.stat().st_mtime_ns,'0'*64)=={}
