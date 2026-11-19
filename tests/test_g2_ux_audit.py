"""G2 UX audit: stem layout, code options, infographic viewer hooks, counts on every Geography entry point."""
from app.routes.geography_g2_plus import g2_stem_text, g2_code_option
from app.routes.polity_unit6 import format_stem


def test_inline_statements_split_and_question_tail():
    h = str(format_stem(g2_stem_text("Consider the statements. I. Herodotus is x. II. Strabo wrote 17 books. Which statements are correct?")))
    assert 'u6-stmts' in h and h.count('<li>') == 2 and 'u6-tail' in h and 'Which statements are correct?' in h


def test_inline_match_and_codes_line():
    h = str(format_stem(g2_stem_text("Match: List I—(A) Tashkent (B) Karachi; List II—(1) 1816 treaty (2) 1972 truce")))
    assert 'u6-match' in h
    assert 'a b c d' not in g2_stem_text("Match\nI. Winds\nII. Ice\nCodes: a b c d")
    opts = ['(1) I II III IV', '(2) II I IV III', '(3) III I IV II', '(4) III IV I II']
    assert g2_code_option(opts[1], opts) == 'A–II · B–I · C–IV · D–III'
    assert g2_code_option('A–4; B–2', ['A–4; B–2']) is None


def test_question_page_viewer_and_dedup(client):
    r = client.get('/learn/geography/g2/14/practice/PYQ-APPSC-D63D002BFD?qlang=both&review=1&choice=1')
    t = r.get_data(as_text=True)
    assert r.status_code == 200 and 'g2_viewer.js' in t and 'data-zoom' in t and 'tabindex="-1"' in t
    assert 'A–II · B–I · C–IV · D–III' in t and t.count('A–II · B–I · C–IV · D–III') == 1


def test_counts_on_entry_points(client):
    for url in ('/learn/', '/learn/geography/', '/learn/geography/g2'):
        t = client.get(url).get_data(as_text=True)
        assert 'MCQs' in t and 'PYQs' in t, url
    assert 'data-g2-counts' in client.get('/learn/geography/').get_data(as_text=True)
