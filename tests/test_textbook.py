import copy
import json
import pytest
from app.db import db
from app.models import Subject, SyllabusChapter, SyllabusSubtopic, ChapterCollectionSetting, FRESH_COLLECTION_ID
from app.services import ap_canonical, textbook

CH = 'u1-c01-region-people-sources'


def bi(en='Teaching text', te='పాఠ్య విషయం'):
    return {'en': en, 'te': te}


def package(status='draft'):
    node = {'title': bi(), 'body': bi(), 'fact_ids': ['fact-one']}
    return {'format': 'ap-textbook-v1', 'chapter_slug': CH, 'status': status, 'version': 'test', 'title': bi(), 'lessons': [
        {'id': 'sources', 'title': bi(), 'subtopic_slugs': ['u1-c01-inscriptions'],
         'sections': [{'id': 'first', 'level': 'group2', 'title': bi(), 'paragraphs': [bi()], 'fact_ids': ['fact-one'], 'source_ids': ['book']},
                      {'id': 'depth', 'level': 'group1', 'title': bi(), 'paragraphs': [bi()], 'fact_ids': ['fact-one'], 'source_ids': ['book']}],
         'sources': [{'id': 'book', 'label': 'Reference book', 'locator': 'p.13'}], 'note_anchors': {'CH01-S01': 'first'},
         'review': dict.fromkeys(['coverage', 'factual', 'language', 'infographics'], True),
         'infographics': [{'kind': k, 'title': bi(), 'nodes': [copy.deepcopy(node)]} for k in ['teaching', 'revision']]}
    ]}


@pytest.fixture()
def setup_book(app, tmp_path):
    app.config.update(TEXTBOOK_ENABLED=True, TEXTBOOK_ROOT=tmp_path)
    with app.app_context():
        db.session.add(Subject(slug='ap_history', name_en='AP', name_te='ఆంధ్ర'))
        db.session.commit()
        ap_canonical.seed()
        ch = SyllabusChapter.query.filter_by(slug=CH).one()
        db.session.add(SyllabusSubtopic(chapter_id=ch.id, slug='u1-c01-inscriptions', subtopic_en='Inscriptions', subtopic_te='శాసనాలు'))
        db.session.add(ChapterCollectionSetting(syllabus_chapter_id=ch.id, active_collection=FRESH_COLLECTION_ID))
        db.session.commit()
    target = tmp_path / CH / 'manifest.json'
    target.parent.mkdir()
    target.write_text(json.dumps(package(), ensure_ascii=False), encoding='utf-8')
    return target


def test_draft_admin_only(client, setup_book, monkeypatch):
    url = f'/learn/ap-history/{CH}/textbook'
    assert client.get(url).status_code == 404
    monkeypatch.setattr('app.routes.learn._is_admin', lambda: True)
    assert b'textbook-draft' in client.get(url).data
    r = client.get(url + '/sources')
    assert r.status_code == 200 and 'పాఠ్య విషయం' in r.get_data(as_text=True)
    assert b'reading-mode' in r.data and b'teaching' in r.data and b'Quick revision' in r.data


def test_approved_and_disabled(client, app, setup_book):
    setup_book.write_text(json.dumps(package('approved')), encoding='utf-8')
    assert client.get(f'/learn/ap-history/{CH}/textbook/sources').status_code == 200
    app.config['TEXTBOOK_ENABLED'] = False
    assert client.get(f'/learn/ap-history/{CH}/textbook').status_code == 404


def test_escape_and_unknown_mapping(client, setup_book, monkeypatch):
    monkeypatch.setattr('app.routes.learn._is_admin', lambda: True)
    data = package()
    data['lessons'][0]['sections'][0]['paragraphs'][0]['en'] = '<script>alert(1)</script>'
    setup_book.write_text(json.dumps(data), encoding='utf-8')
    response = client.get(f'/learn/ap-history/{CH}/textbook/sources')
    assert b'&lt;script&gt;alert(1)&lt;/script&gt;' in response.data
    assert client.get(f'/learn/ap-history/{CH}/textbook/not-a-lesson').status_code == 404
    data['lessons'][0]['subtopic_slugs'] = ['wrong-chapter']
    setup_book.write_text(json.dumps(data), encoding='utf-8')
    assert client.get(f'/learn/ap-history/{CH}/textbook').status_code == 404


@pytest.mark.parametrize('mutation', ['language', 'duplicate', 'source', 'url', 'fact', 'coverage', 'review', 'types', 'anchor', 'group1', 'review-shape', 'source-shape', 'graphic-shape', 'anchor-shape'])
def test_refusals(mutation):
    d = package('approved')
    l = d['lessons'][0]
    if mutation == 'language': l['sections'][0]['paragraphs'][0]['te'] = ''
    if mutation == 'duplicate': d['lessons'].append(copy.deepcopy(l))
    if mutation == 'source': l['sections'][0]['source_ids'] = ['missing']
    if mutation == 'url': l['sources'][0]['url'] = 'javascript:alert(1)'
    if mutation == 'fact': l['infographics'][0]['nodes'][0]['fact_ids'] = ['invented']
    if mutation == 'coverage': l['sections'][0]['fact_ids'].append('omitted')
    if mutation == 'review': l['review']['factual'] = False
    if mutation == 'types': l['infographics'].pop()
    if mutation == 'anchor': l['note_anchors']['CH01-S01'] = 'missing'
    if mutation == 'group1': l['sections'].pop()
    if mutation == 'review-shape': l['review'] = 'approved'
    if mutation == 'source-shape': l['sections'][0]['source_ids'] = [{}]
    if mutation == 'graphic-shape': l['infographics'][0]['nodes'][0]['fact_ids'] = [{}]
    if mutation == 'anchor-shape': l['note_anchors']['CH01-S01'] = []
    with pytest.raises(textbook.PackageError): textbook.validate(d, CH)


def test_note_bridge():
    d = textbook.validate(package(), CH)
    assert textbook.note_target(d, 'CH01-S01') == ('sources', 'first')
    assert textbook.note_target(d, 'unknown') is None


@pytest.mark.parametrize('mutation', [None, 'text', 'omission', 'duplicate', 'level', 'source'])
def test_full_paragraph_atlas_integrity(mutation):
    data = package()
    lesson = data['lessons'][0]
    lesson['sections'][1]['fact_ids'] = ['fact-two']
    atlas = lesson['infographics'][0]
    atlas['coverage_type'] = 'full-paragraph-atlas'
    atlas['nodes'] = [dict(title=s['title'], body=s['paragraphs'][0].copy(), fact_ids=s['fact_ids'].copy(),
                           section_id=s['id'], level=s['level'], source_ids=s['source_ids'].copy())
                      for s in lesson['sections']]
    if mutation == 'text': atlas['nodes'][0]['body']['te'] = 'వేరే విషయం'
    if mutation == 'omission': atlas['nodes'].pop()
    if mutation == 'duplicate': atlas['nodes'][1] = copy.deepcopy(atlas['nodes'][0])
    if mutation == 'level': atlas['nodes'][0]['level'] = 'group1'
    if mutation == 'source': atlas['nodes'][0]['source_ids'] = ['other']
    if mutation:
        with pytest.raises(textbook.PackageError): textbook.validate(data, CH)
    else:
        assert textbook.validate(data, CH) is data


def test_corrupt_and_path_fail_closed(app, setup_book):
    with app.app_context():
        assert textbook.load('../bad', True) is None
        setup_book.write_text('{broken', encoding='utf-8')
        assert textbook.load(CH, True) is None


def test_wrong_canonical_mapping_hides_chapter_link(client, setup_book, monkeypatch):
    monkeypatch.setattr('app.routes.learn._is_admin', lambda: True)
    data = package()
    data['lessons'][0]['subtopic_slugs'] = ['u1-c02-wrong-chapter']
    setup_book.write_text(json.dumps(data), encoding='utf-8')
    response = client.get(f'/learn/ap-history/{CH}')
    assert response.status_code == 200
    assert f'/learn/ap-history/{CH}/textbook'.encode() not in response.data
