from pathlib import Path
from collections import Counter
from urllib.parse import urlsplit,parse_qs
import hashlib,json,re
import pytest
from bs4 import BeautifulSoup
from app.services import solar_practice as solar
from app.services import geography_pyqs as pyqs
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'content/geography/solar_practice.json').read_text(encoding='utf-8'))
IDS=[q['id'] for q in DATA['questions']]

@pytest.mark.parametrize('qid',IDS)
def test_each_question_all_choices_explanations_and_exact_destination(client,qid):
    q=solar.question(qid)
    initial=client.get('/learn/geography/solar-practice/'+qid)
    assert initial.status_code==200
    soup=BeautifulSoup(initial.data,'html.parser')
    assert len(soup.select('input[type=radio]'))==4
    assert b'Correct option:' not in initial.data and b'is-correct' not in initial.data
    assert b'Not an official APPSC question' in initial.data
    for choice in (1,2,3,4):
        response=client.post('/learn/geography/solar-practice/'+qid+'/answer',data={'choice':str(choice),'answer':str(choice),'score':'1'})
        assert response.status_code==200
        assert f'data-score="{int(choice==q["answer"])}"'.encode() in response.data
        parsed=BeautifulSoup(response.data,'html.parser')
        assert len(parsed.select('.solar-option-explanation'))==4
        assert len(parsed.select('.is-correct'))==1
    href=parsed.select_one('[data-chapter-link]')['href'];parts=urlsplit(href)
    notes=BeautifulSoup(client.get(parts.path+'?'+parts.query).data,'html.parser')
    assert notes.find(id=parts.fragment),href
    text=re.sub(r'\s+',' ',notes.article.get_text(' ',strip=True))
    assert re.sub(r'\s+',' ',q['source_paragraph']) in text
    assert q['source_paragraph'].startswith(q['excerpt'].removesuffix('…'))
    back=notes.select_one('[data-note-back]')['href']
    assert '/solar-practice/'+qid in back and parse_qs(urlsplit(back).query)['choice']==['4']
    assert b'data-score=' in client.get(back).data

@pytest.mark.parametrize('topic',range(1,13))
def test_topic_filters_continue_and_navigation(client,topic):
    selected=solar.questions(topic=str(topic));assert len(selected)==6
    start=client.get('/learn/geography/solar-practice',query_string={'topic':topic,'start':'1'})
    assert start.status_code==302 and selected[0]['id'] in start.location
    assert parse_qs(urlsplit(start.location).query)['topic']==[str(topic)]
    soup=BeautifulSoup(client.get(start.location).data,'html.parser')
    next_link=soup.select_one('[aria-label="Solar practice navigation"] a')['href']
    assert selected[1]['id'] in next_link and 'topic='+str(topic) in next_link


def test_formats_empty_intersection_and_invalid_inputs(client):
    for kind in {q['kind'] for q in DATA['questions']}:
        response=client.get('/learn/geography/solar-practice',query_string={'kind':kind,'start':1})
        assert response.status_code==302
        assert client.get(response.location).status_code==200
    assert b'No matching questions' in client.get('/learn/geography/solar-practice?topic=3&kind=calculation&start=1').data
    for query in ['topic=13','topic=x','kind=invalid']:
        assert client.get('/learn/geography/solar-practice?'+query).status_code==400
    for choice in ['', '0', '5', 'abc','1.5']:
        assert client.post('/learn/geography/solar-practice/'+IDS[0]+'/answer',data={'choice':choice}).status_code==400
    assert client.get('/learn/geography/solar-practice/nonexistent').status_code==404
    assert client.get('/learn/geography/solar-practice/'+IDS[0]+'?topic=2').status_code==404


def test_csrf_still_required(client):
    client.auto_csrf=False
    assert client.post('/learn/geography/solar-practice/'+IDS[0]+'/answer',data={'choice':'1'}).status_code==400


def test_original_bank_separation_and_discoverability(client):
    assert len(pyqs.records())==976 and pyqs.summary()=={'total':976,'held':240,'scorable':736}
    assert pyqs.question(IDS[0]) is None
    assert client.get('/learn/geography/pyq/'+IDS[0]).status_code==404
    assert len(solar.questions())==72
    for path in ['/learn/geography/','/learn/geography/unit/1','/learn/geography/lesson/03']:
        assert b'/learn/geography/solar-practice' in client.get(path).data


def test_sources_keys_and_independent_fact_checks(app):
    assert len(set(IDS))==72
    assert Counter(q['topic'] for q in DATA['questions'])=={i:6 for i in range(1,13)}
    # Independently review representative factual and numerical answers, not a copy of answer indexes.
    expected={1:'AU and light-year',2:'299.2 million km',3:'500 seconds',10:'Ceres',13:'Hydrogen fusion into helium in the core',19:'Mercury',21:'Iron oxides in dust and rocks',25:'Ganymede',28:'Uranus',35:'Passes through a debris stream',36:'I only / I మాత్రమే',39:'Venus',41:'Faster near perihelion; slower near aphelion',42:'8years',46:'Io',50:'Tropic of Cancer',54:'23.4°',58:'Rotates once in about its Earth-orbit period',61:'Sun → Moon → Earth',63:'Full moon',70:'1.7m'}
    for n,text in expected.items():
        q=solar.question(f'SOLAR-PRACTICE-{n:03}');assert q['options'][q['answer']-1]==text,(n,q)


def test_fingerprints_fail_closed(app,tmp_path):
    p=tmp_path/'data.json';p.write_text(json.dumps(DATA),encoding='utf-8')
    chapter=ROOT/'static/textbooks/geography/lessons/03_Earth_in_the_Solar_System_Bilingual_Foundation.html'
    with pytest.raises(ValueError,match='release fingerprint'):
        solar._load(str(p),p.stat().st_mtime_ns,str(chapter),chapter.stat().st_mtime_ns,'bad-pin')
    d=dict(DATA);d['chapter_sha256']='bad';p.write_text(json.dumps(d),encoding='utf-8')
    with pytest.raises(ValueError,match='chapter fingerprint'):
        solar._load(str(p),p.stat().st_mtime_ns,str(chapter),chapter.stat().st_mtime_ns,hashlib.sha256(p.read_bytes()).hexdigest())


def test_reader_rejects_external_back_target(client):
    page=client.get('/learn/geography/lesson/03?practice=invalid&back=https://evil.invalid')
    soup=BeautifulSoup(page.data,'html.parser')
    assert soup.select_one('[data-note-back]')['href']=='/learn/geography/unit/1'
    assert b'evil.invalid' not in page.data
