from pathlib import Path
from urllib.parse import urlsplit,parse_qs
import hashlib,json,re
from bs4 import BeautifulSoup
from app.services import geography_pyqs as service

ROOT=Path(__file__).resolve().parents[1]
PARAMS={'unit':'1','lesson':'04','exam':'Group II Services','year':'2024','paper':'Screening Test','mode':'scored'}

def test_continue_opens_filtered_question_instead_of_another_list(client):
    response=client.get('/learn/geography/pyqs',query_string={**PARAMS,'start':'1'})
    assert response.status_code==302
    assert '/pyq/APPSC-G2-GEO-0041?' in response.location
    assert {k:v[0] for k,v in parse_qs(urlsplit(response.location).query).items()}==PARAMS
    page=client.get(response.location)
    assert page.status_code==200 and page.data.count(b'data-geography-pyq=')==1
    assert b'Identify the incorrect statement' in page.data
    assert b'data-correct=' not in page.data


def test_paper_filter_historical_source_and_empty_result(client):
    raw=json.loads((ROOT/'content/geography/pyqs.json').read_text(encoding='utf-8'))['records']
    expected=[r for r in raw if r['source']['exam']=='Group II Services' and r['source']['year']==2011 and r['source']['paper']=='Paper III']
    assert len(expected)==32
    response=client.get('/learn/geography/pyqs',query_string={'exam':'Group II Services','year':'2011','paper':'Paper III','start':'1'})
    assert expected[0]['source']['id'] in response.location
    assert client.get(response.location).status_code==200
    page=client.get('/learn/geography/pyqs?unit=1&lesson=44&start=1')
    assert page.status_code==200 and b'No matching questions' in page.data
    assert b'data-geography-pyq=' not in page.data
    assert client.get('/learn/geography/pyqs?paper=nonexistent&start=1').status_code==200


def test_review_excerpt_section_and_back_round_trip_preserves_filters_and_answer(client):
    page=client.post('/learn/geography/pyq/APPSC-G2-GEO-0041/answer',query_string=PARAMS,data={'choice':'4'})
    assert b'data-score="1"' in page.data
    soup=BeautifulSoup(page.data,'html.parser');excerpt=soup.select_one('[data-chapter-excerpt]')
    assert excerpt and 'focus' in excerpt.get_text().lower()
    href=soup.select_one('[data-chapter-link]')['href'];parts=urlsplit(href)
    assert parts.fragment=='focus-epicentre'
    notes=client.get(parts.path+'?'+parts.query);ns=BeautifulSoup(notes.data,'html.parser')
    assert ns.find(id=parts.fragment)
    back=ns.select_one('[data-note-back]')['href'];qs=parse_qs(urlsplit(back).query)
    for k,v in PARAMS.items():assert qs[k]==[v]
    assert qs['choice']==['4'] and qs['review']==['1']
    returned=client.get(back)
    assert returned.status_code==200 and b'data-score="1"' in returned.data
    assert b'data-chapter-excerpt' in returned.data
    next_link=BeautifulSoup(returned.data,'html.parser').select('[aria-label="PYQ navigation"] a')[-1]['href']
    assert '/APPSC-G2-GEO-0042?' in next_link and parse_qs(urlsplit(next_link).query)['paper']==['Screening Test']
    assert client.get(next_link).status_code==200


def test_all_excerpt_text_and_anchors_come_from_the_actual_chapters(app):
    data=json.loads((ROOT/'content/geography/chapter_context.json').read_text(encoding='utf-8'))['records']
    assert len(data)==976
    soups={}
    for record in service.records():
        contexts=service.chapter_context(record)
        assert len(contexts)==len(record['routes'])
        for context in contexts:
            path=ROOT/'static/textbooks/geography/lessons'/context['file']
            assert hashlib.sha256(path.read_bytes()).hexdigest()==context['source_html_sha256']
            if path not in soups:soups[path]=BeautifulSoup(path.read_bytes(),'html.parser')
            soup=soups[path]
            if not context.get('dynamic_anchor'):assert soup.find(id=context['anchor']),context
            assert re.sub(r'\s+',' ',context['source_paragraph']) in re.sub(r'\s+',' ',soup.find('article').get_text(' ',strip=True))
            assert context['source_paragraph'].startswith(context['excerpt'].removesuffix('…'))


def test_held_review_never_scores_and_still_shows_chapter_context(client):
    page=client.get('/learn/geography/pyq/APPSC-G2-GEO-0040?review=1&choice=1')
    assert page.status_code==200 and b'data-result="unscored"' in page.data
    assert b'data-score=' not in page.data and b'data-chapter-excerpt' in page.data
    assert b'is-correct' not in page.data and b'is-wrong' not in page.data


def test_note_return_is_internal_and_works_without_question_context(client):
    page=client.get('/learn/geography/lesson/04')
    soup=BeautifulSoup(page.data,'html.parser')
    assert soup.select_one('[data-note-back]')['href']=='/learn/geography/unit/1'
    page=client.get('/learn/geography/lesson/04?back=https://evil.invalid&question=%3Cscript%3E')
    soup=BeautifulSoup(page.data,'html.parser')
    assert soup.select_one('[data-note-back]')['href']=='/learn/geography/unit/1'
    assert b'evil.invalid' not in page.data
    assert client.get('/learn/geography/reference/nonexistent.html').status_code==404


def test_start_can_find_questions_for_every_unit_and_chapter(client):
    cat=json.loads((ROOT/'static/textbooks/geography/catalogue.json').read_text(encoding='utf-8'))
    for unit in cat['units']:
        response=client.get('/learn/geography/pyqs',query_string={'unit':str(unit['id']),'start':'1'})
        assert response.status_code==302,unit['id']
        assert client.get(response.location).status_code==200
        for lesson in unit['lessons']:
            response=client.get('/learn/geography/pyqs',query_string={'unit':str(unit['id']),'lesson':lesson['id'],'start':'1'})
            mapped=any(any(route['lesson_id']==lesson['id'] for route in record['routes']) for record in service.records())
            if mapped:
                assert response.status_code==302,lesson['id']
                assert client.get(response.location).status_code==200
            else:
                assert response.status_code==200 and b'No matching questions' in response.data
