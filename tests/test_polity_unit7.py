"""Unit 7 (legislature, executive, judiciary) is served by the same data-driven Polity routes as Unit 6."""
from bs4 import BeautifulSoup
from app.routes.polity_maps import records

U7=['7.1.1','7.2.1','7.2.2','7.2.3','7.2.4','7.3.1','7.3.2','7.3.3','7.3.4','7.3.5','7.3.6','7.4.1','7.4.2','7.4.3','7.4.4','7.5.1','7.6.1','7.6.2']

def soup(r):return BeautifulSoup(r.data,'html.parser')
def on(app):app.config['POLITY_UNIT6_ENABLED']=True

def test_polity_unit7_on_subject_page(client,app):
    on(app);page=soup(client.get('/learn/polity/unit6/'))
    u7=[s for s in page.select('.u6-unit') if 'Unit 7' in s.get_text()][0]
    assert u7.select_one('a.u6-unit-h')['href'].endswith('/unit/7') and 'Coming soon' not in u7.get_text()

def test_polity_unit7_chapters_and_records(client,app):
    on(app)
    r=client.get('/learn/polity/unit6/unit/7');assert r.status_code==200
    assert len(soup(r).select('a.u6-chcard'))==len(U7)
    with app.app_context():
        qs=[q for q in records().values() if q['_chapter'].startswith('7.')]
    assert {q['_chapter'] for q in qs}>=set(U7)-{'7.2.3'} or {q['_chapter'] for q in qs}==set(U7)
    assert sum(q['_kind']=='bank' for q in qs)>=800 and sum(q['_kind'] in ('pyq','primary_pyq') for q in qs)>=380  # 386 after the 2026-11-11 chapter remap
    assert all(q['_answer'] in (1,2,3,4) for q in qs if q['_kind']=='bank')
    # official keys are never rewritten: disputed ones keep their recorded key and are flagged
    # (3 of the 7 Unit 7 audit records now sit in their syllabus chapters in Units 8-9, so count across units)
    with app.app_context():
        d=[q for q in records().values() if q.get('audit_note')]
    # the 2026-11-11 full key verification corrected some of them against the official paper (scored on the audited key)
    fixed=[q for q in d if (q.get('key_audit') or {}).get('scored')]
    assert len(d)==5 and all(q.get('official_key') for q in d)  # 2 superseded by verbatim UPSC records 2026-11-11
    assert all(q['key_status']=='confirmed' and q['study_answer']==q['official_key']==q['key_audit']['study_answer'] for q in fixed)
    assert all(q['key_status']=='disputed' for q in d if q not in fixed)

def test_polity_unit7_chapter_notes_practice_descriptive(client,app):
    on(app)
    for cid in U7:
        assert client.get(f'/learn/polity/unit6/chapters/{cid}').status_code==200,cid
        assert client.get(f'/learn/polity/unit6/chapters/{cid}/notes').status_code==200,cid
    with app.app_context():
        q=next(q for q in records().values() if q['_chapter']=='7.3.2' and q['_kind'] in ('pyq','primary_pyq'))
    r=client.post('/learn/polity/unit6/practice/'+q['id'],data={'answer':q['_answer']})
    assert r.status_code==200 and b'answer-result' in r.data
    assert client.get('/learn/polity/unit6/library?kind=pyq&unit=7').status_code==200
    page=soup(client.get('/learn/polity/unit6/descriptive?chapter=7.1.1'))
    arts=page.select('article.u6-desc');assert arts and all(a.get_text(strip=True) for a in arts)

def test_polity_unit7_telugu_terms():
    import glob,json,re
    bad=re.compile(r'\d+వ సవరణ ప్రకరణ|ప్రాథమిక నిర్మాణ|అధికరణ')
    for f in glob.glob('content/polity/g2/7.*/7.*/Questions.json'):
        for q in json.load(open(f,encoding='utf-8-sig'))['questions']:
            assert not bad.search(q['question_te']+' '.join(q['options_te'])),q['id']
