"""Unit 6 recall decks: one generic card schema behind the full-screen recall UI.

Generic item fields: id, deck, chapter, sort, front_en/te, front_sub, cue_en/te, two_way, title_en/te, says_en/te,
points_en/te, trap_en/te, articles, laxmikanth, gbk, card_ids, tested_count, as_of, flag, source ('laxmikanth'|'new').
Data: content/polity/g2/recall_decks/<deck>.json (+ <deck>_new.json). The articles deck adapts article_cards.
"""
import json
import re
from functools import lru_cache
from pathlib import Path

from . import article_cards as _art

DIR = Path(__file__).resolve().parents[2] / 'content' / 'polity' / 'g2' / 'recall_decks'

TEXT_FIELDS = ('front', 'cue', 'title', 'says')

DECKS = {
    'articles': {
        'id': 'articles', 'title_en': 'Articles', 'title_te': 'ప్రకరణలు', 'icon': '§',
        'desc_en': 'Article number ↔ what it says', 'desc_te': 'ప్రకరణ సంఖ్య ↔ అది ఏమి చెబుతుంది',
        'dir_a_en': 'Article → Concept', 'dir_a_te': 'ప్రకరణ → భావన', 'dir_b_en': 'Concept → Article', 'dir_b_te': 'భావన → ప్రకరణ',
        'front_kind': 'number', 'pill_en': 'Article', 'pill_te': 'ప్రకరణ', 'glyph': '21',
        'order_en': 'In article order', 'order_te': 'ప్రకరణల క్రమంలో',
        'prompt_en': 'Recall the article, then check', 'prompt_te': 'ప్రకరణను గుర్తు చేసుకుని, సరిచూసుకోండి',
        'store': 'u6_artcards_v1', 'setup_store': 'u6_artcards_setup', 'lang_store': 'u6_artcards_lang',
    },
    'amendments': {
        'id': 'amendments', 'title_en': 'Amendments', 'title_te': 'సవరణలు', 'icon': '✎',
        'desc_en': 'Amendment number ↔ what it changed', 'desc_te': 'సవరణ సంఖ్య ↔ అది చేసిన మార్పు',
        'dir_a_en': 'Amendment → What it did', 'dir_a_te': 'సవరణ → ఏమి చేసింది', 'dir_b_en': 'Idea → Amendment', 'dir_b_te': 'అంశం → సవరణ',
        'front_kind': 'number', 'pill_en': 'Amendment', 'pill_te': 'సవరణ', 'glyph': '42',
        'order_en': 'In amendment order', 'order_te': 'సవరణల క్రమంలో',
        'prompt_en': 'Recall the amendment, then check', 'prompt_te': 'సవరణను గుర్తు చేసుకుని, సరిచూసుకోండి',
    },
    'cases': {
        'id': 'cases', 'title_en': 'Cases', 'title_te': 'కేసులు', 'icon': '⚖',
        'desc_en': 'Case ↔ the issue it decided · theme ↔ its cases', 'desc_te': 'కేసు ↔ అది తేల్చిన అంశం · అంశం ↔ దాని కేసులు',
        'dir_a_en': 'Case → Issue', 'dir_a_te': 'కేసు → అంశం', 'dir_b_en': 'Theme → Cases', 'dir_b_te': 'అంశం → కేసులు',
        'front_kind': 'text', 'pill_en': 'Case', 'pill_te': 'కేసు', 'glyph': '⚖', 'themes': True,
        'order_en': 'Grouped by theme', 'order_te': 'అంశాల వారీగా',
        'prompt_en': 'Recall the case, then check', 'prompt_te': 'కేసును గుర్తు చేసుకుని, సరిచూసుకోండి',
    },
}
# Cases are tested as CASE -> ISSUE and THEME -> which cases belong (match / odd one out), not by year.
# One fixed theme list; the data carries theme_en/theme_te (must match a row here). Order = 'In order' for cases.
# (id, theme_en, theme_te, short_en, short_te, colour)
THEMES = [
    ('basic', 'Amending power & basic structure', 'సవరణ అధికారం, మౌలిక స్వరూపం', 'Basic str.', 'మౌలిక', '#6d28d9'),
    ('property', 'Right to property & Ninth Schedule', 'ఆస్తి హక్కు, తొమ్మిదో షెడ్యూల్', 'Property', 'ఆస్తి', '#a16207'),
    ('liberty', 'Life & personal liberty (Article 21)', 'జీవించే హక్కు, వ్యక్తిగత స్వేచ్ఛ (ప్రకరణ 21)', 'Art 21', 'ప్ర.21', '#0f766e'),
    ('art21plus', 'Rights read into Article 21', 'ప్రకరణ 21 లోకి చేర్చిన హక్కులు', 'Art 21 +', 'ప్ర.21 +', '#15803d'),
    ('equality', 'Equality & reservation', 'సమానత్వం, రిజర్వేషన్లు', 'Equality', 'సమానత్వం', '#1d4ed8'),
    ('gender', 'Privacy, gender & personal law', 'గోప్యత, లింగ సమానత్వం, వ్యక్తిగత చట్టాలు', 'Privacy·gender', 'గోప్యత', '#be185d'),
    ('freedoms', 'Speech, religion & minority rights', 'భావ ప్రకటన, మతం, మైనారిటీ హక్కులు', 'Freedoms', 'స్వేచ్ఛలు', '#c2410c'),
    ('dpsp', 'DPSP & Fundamental Duties', 'ఆదేశిక సూత్రాలు, ప్రాథమిక విధులు', 'DPSP·duties', 'ఆదేశిక', '#4d7c0f'),
    ('federal', 'Federalism & Emergency', 'సమాఖ్య వ్యవస్థ, అత్యవసర పరిస్థితి', 'Federal', 'సమాఖ్య', '#0e7490'),
    ('elections', 'Elections & democracy', 'ఎన్నికలు, ప్రజాస్వామ్యం', 'Elections', 'ఎన్నికలు', '#b91c1c'),
    ('judiciary', 'Judiciary & tribunals', 'న్యాయవ్యవస్థ, ట్రిబ్యునళ్లు', 'Judiciary', 'న్యాయ', '#334155'),
    ('preamble', 'Preamble, citizenship & territory', 'ప్రవేశిక, పౌరసత్వం, భూభాగం', 'Preamble', 'ప్రవేశిక', '#57534e'),
]
THEME_BY_EN = {t[1]: i for i, t in enumerate(THEMES)}


def _theme_fields(it):
    i = THEME_BY_EN.get(it.get('theme_en'))
    if i is None:
        return
    t = THEMES[i]
    it.update(theme_i=i, theme_id=t[0], theme_te=it.get('theme_te') or t[2], theme_short_en=t[3], theme_short_te=t[4], theme_acc=t[5])


def themes(deck_id):
    """Theme tiles for a deck with a theme view: [{id, i, en, te, short_en, short_te, acc, cases:[item...]}] in list order."""
    if not DECKS.get(deck_id, {}).get('themes'):
        return []
    its = items(deck_id)
    out = []
    for i, t in enumerate(THEMES):
        cs = [c for c in its if c.get('theme_i') == i]
        if cs:
            out.append({'id': 'TH-' + t[0], 'i': i, 'en': t[1], 'te': t[2], 'short_en': t[3], 'short_te': t[4], 'acc': t[5], 'cases': cs})
    return out


for _d in DECKS.values():
    _d.setdefault('store', f"u6_recall_{_d['id']}_v1")
    _d.setdefault('setup_store', f"u6_recall_{_d['id']}_setup")
    _d.setdefault('lang_store', 'u6_artcards_lang')


def _article_item(c):
    return {
        'id': c['id'], 'deck': 'articles', 'chapter': c['chapter'], 'sort': _art.article_key(c['article']),
        'front_en': f"Article {c['article']}", 'front_te': f"ప్రకరణ {c['article']}", 'front_short': c['article'],
        'front_sub': c.get('part') or '',
        'cue_en': c['concept_en'], 'cue_te': c['concept_te'], 'two_way': True,
        'title_en': c['concept_en'], 'title_te': c['concept_te'], 'says_en': c['says_en'], 'says_te': c['says_te'],
        'points_en': [], 'points_te': [], 'trap_en': c.get('trap_en'), 'trap_te': c.get('trap_te'),
        'articles': [], 'laxmikanth': c.get('laxmikanth'), 'gbk': c.get('gbk'), 'card_ids': c.get('card_ids') or [],
        'tested_count': c.get('tested_count', 0), 'as_of': c.get('as_of'), 'flag': c.get('flag'), 'source': 'laxmikanth',
        'part': c.get('part'),
    }


def deck_files(deck_id):
    return [p for p in (DIR / f'{deck_id}.json', DIR / f'{deck_id}_new.json') if p.is_file()]


def _short(item):
    m = re.match(r'\s*(\d+\w*)', item.get('front_en') or '')
    return m.group(1) if m else (item.get('front_en') or '')


@lru_cache(maxsize=None)
def items(deck_id):
    if deck_id not in DECKS:
        return []
    if deck_id == 'articles':
        return [_article_item(c) for c in _art.all_cards()]
    out = []
    for f in deck_files(deck_id):
        try:
            data = json.loads(f.read_text(encoding='utf-8'))
        except (ValueError, OSError):
            continue
        for it in data if isinstance(data, list) else data.get('items', []):
            it = dict(it)
            it.setdefault('source', 'new' if f.stem.endswith('_new') else 'laxmikanth')
            it.setdefault('two_way', True)
            for k in ('points_en', 'points_te', 'articles', 'card_ids'):
                it[k] = it.get(k) or []
            it.setdefault('front_short', _short(it))
            _theme_fields(it)
            out.append(it)
    if DECKS[deck_id].get('themes'):  # grouped by theme (list order), then by year: doctrine develops case by case
        return sorted(out, key=lambda i: (i.get('theme_i', 99), i.get('sort') or 0, i['front_en'].lower()))
    return sorted(out, key=lambda i: (i.get('sort') or 0, i['id']))


def deck(deck_id):
    d = DECKS.get(deck_id)
    if not d:
        return None
    its = items(deck_id)
    return dict(d, count=len(its), two_way=sum(1 for i in its if i['two_way']), new=sum(1 for i in its if i['source'] == 'new'))


def all_decks():
    return [deck(k) for k in DECKS]
