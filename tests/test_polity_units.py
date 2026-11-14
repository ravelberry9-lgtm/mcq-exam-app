"""Units 7-10 use the same practice routes as Unit 6: PYQ distribution, Next/Previous, key markers, Telugu fallback."""
import json
from urllib.parse import parse_qs, urlsplit

from bs4 import BeautifulSoup

from app.routes.polity_maps import CONTENT, records
from app.services import pyq_metrics as P

BANK = CONTENT.parent / 'pyq_bank' / 'indian_polity_pyq_bank_v3.71.0.json'


def soup(r):
    assert r.status_code == 200, r.status_code
    return BeautifulSoup(r.data, 'html.parser')


def enable(app):
    app.config['POLITY_UNIT6_ENABLED'] = True


def pyq_files():
    for name in ('PYQ-Set.json', 'PYQ-Bank-Set.json'):
        for f in sorted(CONTENT.glob('*.*/*/' + name)):
            yield f, json.loads(f.read_text(encoding='utf-8-sig'))['questions']


def test_unit_pages_for_all_five_units(client, app):
    enable(app)
    for n in (6, 7, 8, 9, 10):
        page = soup(client.get(f'/learn/polity/unit6/unit/{n}', follow_redirects=True))
        assert f'Unit {n}' in page.select_one('h1').text
        assert page.select('a.u6-chcard')
    assert client.get('/learn/polity/unit6/unit/11').status_code == 404
    assert client.get('/learn/polity/unit6/unit').status_code == 200  # Unit 6 keeps its old URL


def test_bank_records_copied_exactly_once():
    bank = {r['record_id']: r for r in json.loads(BANK.read_text(encoding='utf-8'))}
    seen = {}
    for f, qs in pyq_files():
        for q in qs:
            rid = q.get('source_record_id')
            if rid not in bank:
                continue  # separately transcribed source-paper PYQs (not bank records)
            assert rid not in seen, (rid, f, seen.get(rid))
            seen[rid] = f
            if f.name == 'PYQ-Set.json' and f.parent.name.startswith(('6.', '7.')):
                continue  # reviewed sets (Unit 6 review; Unit 7 is integrated and audited separately)
            r = bank[rid]
            assert q['question_en'] == r['question_en'] and q['options_en'] == [r['option_%d' % i] for i in range(1, 5)]
            k = int(r['correct_option']) if r['correct_option'] in '1234' and r['correct_option'] else None
            ka = r.get('key_audit') or {}  # audited key: corrected/reworded -> scored on the audited answer; else disputed
            assert not ka.get('excluded'), rid
            if ka.get('scored'):
                assert q['study_answer'] == q['official_key'] == ka['study_answer'] and q['scored'] is True and q['key_status'] == 'confirmed'
            elif ka:
                assert q['study_answer'] == ka.get('study_answer') and q['key_status'] == 'disputed' and q['scored'] is False
            else:
                assert q['study_answer'] in (k, None) and q['official_key'] in (k, None)
            assert q['chapter'] == f.parent.name
    assert len(seen) >= 1350  # every bank record except ones outside units 6-10
    units = {int(f.parent.name.split('.')[0]) for f in seen.values()}
    assert {6, 8, 9, 10} <= units


def test_pyq_practice_next_previous_and_finish_units_8_to_10(client, app):
    enable(app)
    for n in (8, 9, 10):
        lib = soup(client.get(f'/learn/polity/unit6/library?kind=pyq&unit={n}&qlang=en'))
        start = next(a['href'] for a in lib.select('a') if 'Start practice' in a.text)
        first = soup(client.get(start))
        nxt = first.select_one('.geo-question-nav a[rel=next]')
        assert nxt and 'Next' in nxt.text and not first.select_one('a[rel=prev]')
        assert parse_qs(urlsplit(nxt['href']).query)['unit'] == [str(n)]
        second = soup(client.get(nxt['href']))
        assert second.select_one('a[rel=prev]') and second.select_one('a[rel=next]')
        total = int(first.select_one('.geo-qheader strong').text.split('/')[1])
        assert total >= 50 if n == 8 else total >= 20


def test_answer_panel_has_inline_next_and_finish_on_last(client, app):
    enable(app)
    with app.app_context():
        qs = [q for q in records().values() if q['_chapter'] == '10.3.2' and q['_kind'] == 'pyq' and q['_answer'] in (1, 2, 3, 4)]
    qs.sort(key=lambda q: q['id'])
    args = 'chapter=10.3.2&kind=pyq&qlang=en'
    page = soup(client.post(f"/learn/polity/unit6/practice/{qs[0]['id']}?{args}", data={'answer': '1'},follow_redirects=True))
    assert page.select_one('#answer-result .u6-next-inline a[data-next]')
    lib = soup(client.get('/learn/polity/unit6/library?' + args))
    links = [a['href'] for a in lib.select('.geo-question-list a')]
    last = soup(client.get(links[-1]))
    assert not last.select_one('.geo-question-nav a[rel=next]') and 'Finish' in last.select_one('.geo-question-nav').text


def test_question_leaving_mistakes_view_keeps_next(client, app):
    enable(app)
    with app.app_context():
        qs = sorted((q for q in records().values() if q['_chapter'] == '8.1.1' and q['_kind'] == 'pyq' and q['_answer'] in (1, 2, 3, 4)), key=lambda q: q['id'])
    a, b, c = qs[:3]
    for q in (a, b, c):  # make three mistakes
        client.post(f"/learn/polity/unit6/practice/{q['id']}?chapter=8.1.1&kind=pyq", data={'answer': str(q['_answer'] % 4 + 1)},follow_redirects=True)
    client.post(f"/learn/polity/unit6/practice/{b['id']}?chapter=8.1.1&kind=pyq", data={'answer': str(b['_answer'])},follow_redirects=True)  # b fixed
    page = soup(client.get(f"/learn/polity/unit6/practice/{b['id']}?chapter=8.1.1&kind=pyq&view=mistakes"))
    assert page.select_one('a[rel=next]') and page.select_one('a[rel=prev]')


def test_unconfirmed_key_marker_and_telugu_fallback(client, app):
    enable(app)
    with app.app_context():
        q = next(q for q in records().values() if q['_chapter'].startswith('8.') and q.get('key_status') == 'no_official_key' and q['_answer'] in (1, 2, 3, 4) and not q.get('question_te'))
    page = soup(client.post(f"/learn/polity/unit6/practice/{q['id']}?chapter={q['_chapter']}&kind=pyq&qlang=te", data={'answer': str(q['_answer'])},follow_redirects=True))
    assert page.select_one('.xp-key[data-key-status=no_official_key]')
    stem = page.select_one('.geo-question').get_text()
    assert q['question_en'].split('\n')[0][:40] in stem and 'Telugu text not available' in stem
    assert all(o.get_text(strip=True) for o in page.select('.geo-option-text'))


def test_laxmikanth_mcqs_labelled_and_in_practice(client, app):
    enable(app)
    files = sorted(CONTENT.glob('*.*/*/Laxmikanth-Questions.json'))
    assert files
    q = json.loads(files[0].read_text(encoding='utf-8'))['questions'][0]
    assert q['answer'] in (1, 2, 3, 4) and 'Laxmikanth' in q['source']
    page = soup(client.get(f"/learn/polity/unit6/practice/{q['id']}?chapter={q['chapter']}&kind=bank"))
    assert 'Laxmikanth' in page.select_one('.geo-question').get_text()


def test_chapter_without_notes_has_no_dead_notes_link(client, app):
    enable(app)
    page = soup(client.get('/learn/polity/unit6/chapters/8.1.1'))
    assert not [a for a in page.select('a') if a.get('href', '').endswith('/notes')]
    assert client.get('/learn/polity/unit6/chapters/8.1.1/notes').status_code == 404


def test_pyq_metrics_per_unit_sum_to_bank():
    m = P.compute()
    assert [u['en'] for u in m['units']] == ['Unit 6', 'Unit 7', 'Unit 8', 'Unit 9', 'Unit 10', 'Not in Units 6-10']
    assert sum(u['total'] for u in m['units']) == m['total']
    assert sum(u['appsc'] for u in m['units']) == m['appsc_total']
    for u in m['units']:
        assert sum(u['groups']) == u['appsc'] and u['appsc'] + sum(u['families']) == u['total']
