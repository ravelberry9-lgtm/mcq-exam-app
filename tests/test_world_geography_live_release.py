from bs4 import BeautifulSoup


def test_geography_learn_page_exposes_world_release(client):
    response=client.get('/learn/geography/')
    assert response.status_code==200
    assert b'/learn/geography/world' in response.data


def test_world_index_has_29_canonical_chapters(client):
    response=client.get('/learn/geography/world')
    soup=BeautifulSoup(response.data,'html.parser')
    assert response.status_code==200
    assert len(soup.select('[data-world-chapter]'))==29
    assert soup.select_one('[data-world-chapter="1"]')
    assert soup.select_one('[data-world-chapter="29"]')


def test_alias_chapter_preserves_existing_notes_and_practice(client):
    response=client.get('/learn/geography/world/4')
    soup=BeautifulSoup(response.data,'html.parser')
    assert response.status_code==200
    assert '/learn/geography/lesson/04' in response.get_data(as_text=True)
    assert '/learn/geography/original-practice?chapter=04' in response.get_data(as_text=True)
    assert not soup.select_one('a[href$="/world/4/notes"]')


def test_native_regional_chapter_notes_and_mcq_round_trip(client):
    chapter=client.get('/learn/geography/world/20')
    assert chapter.status_code==200
    assert b'/learn/geography/world/20/notes' in chapter.data
    practice=client.get('/learn/geography/world/20/practice')
    soup=BeautifulSoup(practice.data,'html.parser')
    start=soup.select_one('a.btn.primary')['href']
    question=client.get(start)
    assert question.status_code==200
    q=BeautifulSoup(question.data,'html.parser')
    assert len(q.select('input[name="choice"]'))==4
    answer=client.post(start.replace('?qlang=te','/answer?qlang=te'),data={'choice':'2'})
    assert answer.status_code==200
    a=BeautifulSoup(answer.data,'html.parser')
    assert a.select_one('#answer-result')
    section=a.select_one('[data-chapter-link]')['href']
    assert '#p149-continent-meaning' in section
    notes=client.get(section.split('#')[0])
    assert notes.status_code==200
    assert BeautifulSoup(notes.data,'html.parser').find(id='p149-continent-meaning')


def test_world_routes_reject_invalid_inputs(client):
    assert client.get('/learn/geography/world/30').status_code==404
    assert client.get('/learn/geography/world/20/practice/WG27-P149-001?qlang=xx').status_code==400
    assert client.post('/learn/geography/world/20/practice/WG27-P149-001/answer?qlang=en',data={'choice':'5'}).status_code==400
