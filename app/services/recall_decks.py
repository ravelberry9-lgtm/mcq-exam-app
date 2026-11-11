"""Unit 6 recall decks: one generic card schema behind the full-screen recall UI.

Generic item fields: id, deck, chapter, sort, front_en/te, front_sub, cue_en/te, two_way, title_en/te, says_en/te,
points_en/te, trap_en/te, articles, laxmikanth, gbk, card_ids, tested_count, as_of, flag, source ('laxmikanth'|'new').
Data: content/polity/g2/recall_decks/<deck>.json (+ <deck>_new.json). The articles deck adapts article_cards.
"""
import json
import re
from functools import lru_cache
from pathlib import Path

from markupsafe import Markup, escape

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
# (id, theme_en, theme_te, short_en, short_te, colour (light fill), ink (dark-mode text))
THEMES = [
    ('basic', 'Amending power & basic structure', 'సవరణ అధికారం, మౌలిక నిర్మాణం', 'Basic str.', 'మౌలిక', '#6B21A8', '#D8B4FE'),
    ('property', 'Right to property & Ninth Schedule', 'ఆస్తి హక్కు, తొమ్మిదో షెడ్యూల్', 'Property', 'ఆస్తి', '#854D0E', '#FDE68A'),
    ('liberty', 'Life & personal liberty (Article 21)', 'జీవించే హక్కు, వ్యక్తిగత స్వేచ్ఛ (ప్రకరణ 21)', 'Art 21', 'ప్ర.21', '#0F766E', '#5EEAD4'),
    ('art21plus', 'Rights read into Article 21', 'ప్రకరణ 21 లోకి చేర్చిన హక్కులు', 'Art 21 +', 'ప్ర.21 +', '#115E59', '#99F6E4'),
    ('equality', 'Equality & reservation', 'సమానత్వం, రిజర్వేషన్లు', 'Equality', 'సమానత్వం', '#4338CA', '#A5B4FC'),
    ('gender', 'Privacy, gender & personal law', 'గోప్యత, లింగ సమానత్వం, వ్యక్తిగత చట్టాలు', 'Privacy·gender', 'గోప్యత', '#BE185D', '#F9A8D4'),
    ('freedoms', 'Speech, religion & minority rights', 'భావ ప్రకటన, మతం, మైనారిటీ హక్కులు', 'Freedoms', 'స్వేచ్ఛలు', '#7C2D12', '#FDBA74'),
    ('dpsp', 'DPSP & Fundamental Duties', 'ఆదేశిక సూత్రాలు, ప్రాథమిక విధులు', 'DPSP·duties', 'ఆదేశిక', '#3F6212', '#BEF264'),
    ('federal', 'Federalism & Emergency', 'సమాఖ్య వ్యవస్థ, అత్యవసర పరిస్థితి', 'Federal', 'సమాఖ్య', '#0E7490', '#67E8F9'),
    ('elections', 'Elections & democracy', 'ఎన్నికలు, ప్రజాస్వామ్యం', 'Elections', 'ఎన్నికలు', '#9F1239', '#FDA4AF'),
    ('executive', 'Parliament & Union executive', 'పార్లమెంటు, కేంద్ర కార్యనిర్వాహక వ్యవస్థ', 'Union', 'కేంద్రం', '#1E40AF', '#93C5FD'),
    ('judiciary', 'Judiciary & tribunals', 'న్యాయవ్యవస్థ, ట్రిబ్యునళ్లు', 'Judiciary', 'న్యాయ', '#334155', '#CBD5E1'),
    ('preamble', 'Preamble, citizenship & territory', 'ప్రవేశిక, పౌరసత్వం, భూభాగం', 'Preamble', 'ప్రవేశిక', '#57534E', '#D6D3D1'),
]
THEME_BY_EN = {t[1]: i for i, t in enumerate(THEMES)}


def _theme_fields(it):
    i = THEME_BY_EN.get(it.get('theme_en'))
    if i is None:
        return
    t = THEMES[i]
    it.update(theme_i=i, theme_id=t[0], theme_te=it.get('theme_te') or t[2], theme_short_en=t[3], theme_short_te=t[4], theme_acc=t[5], theme_ink=t[6])


def themes(deck_id):
    """Theme tiles for a deck with a theme view: [{id, i, en, te, short_en, short_te, acc, cases:[item...]}] in list order."""
    if not DECKS.get(deck_id, {}).get('themes'):
        return []
    its = items(deck_id)
    out = []
    for i, t in enumerate(THEMES):
        cs = [c for c in its if c.get('theme_i') == i or t[0] in (c.get('also_themes') or [])]
        if cs:
            out.append({'id': 'TH-' + t[0], 'i': i, 'en': t[1], 'te': t[2], 'short_en': t[3], 'short_te': t[4], 'acc': t[5], 'ink': t[6], 'cases': cs})
    return out


for _d in DECKS.values():
    _d.setdefault('store', f"u6_recall_{_d['id']}_v1")
    _d.setdefault('setup_store', f"u6_recall_{_d['id']}_setup")
    _d.setdefault('lang_store', 'u6_artcards_lang')


ARTICLE_RICH = ('one_line_en', 'one_line_te', 'text_en', 'text_te', 'text_te_note', 'clauses', 'meaning_en', 'meaning_te',
                'implications_en', 'implications_te', 'origin_en', 'origin_te', 'amendments', 'cases', 'remember_en', 'remember_te', 'exam')


def _article_item(c):
    rich = {k: c[k] for k in ARTICLE_RICH if c.get(k)}
    return rich | {
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


# ── Part-wise organisation: every card gets 'part' (Constitution Part / 'Schedules' / 'Preamble' / 'General') and 'unit' (6-10) ──
# (first article, last article, part) by natural article order; 243 splits into IX / IXA / IXB by its letter suffix.
PART_RANGES = [(1, 4, 'Part I'), (5, 11, 'Part II'), (12, 35, 'Part III'), (36, 51, 'Part IV'), (52, 151, 'Part V'), (152, 237, 'Part VI'),
               (238, 238, 'Part VII'), (239, 242, 'Part VIII'), (244, 244, 'Part X'), (245, 263, 'Part XI'), (264, 300, 'Part XII'),
               (301, 307, 'Part XIII'), (308, 323, 'Part XIV'), (324, 329, 'Part XV'), (330, 342, 'Part XVI'), (343, 351, 'Part XVII'),
               (352, 360, 'Part XVIII'), (361, 367, 'Part XIX'), (368, 368, 'Part XX'), (369, 392, 'Part XXI'), (393, 395, 'Part XXII')]
# (part, short_en, short_te, unit, colour, dark ink) in Constitution order: the setup chips follow this list.
PARTS = [
    ('Preamble', 'Preamble', 'ప్రవేశిక', 6, '#57534E', '#D6D3D1'),
    ('Part I', 'Union & territory', 'సమాఖ్య, భూభాగం', 6, '#0F766E', '#5EEAD4'),
    ('Part II', 'Citizenship', 'పౌరసత్వం', 6, '#0E7490', '#67E8F9'),
    ('Part III', 'Fundamental Rights', 'ప్రాథమిక హక్కులు', 6, '#7C2D12', '#FDBA74'),
    ('Part IV', 'Directive Principles', 'ఆదేశిక సూత్రాలు', 6, '#3F6212', '#BEF264'),
    ('Part IVA', 'Fundamental Duties', 'ప్రాథమిక విధులు', 6, '#854D0E', '#FDE68A'),
    ('Part V', 'The Union', 'కేంద్ర ప్రభుత్వం', 7, '#4338CA', '#A5B4FC'),
    ('Part VI', 'The States', 'రాష్ట్రాలు', 7, '#6B21A8', '#D8B4FE'),
    ('Part VII', 'Part B States (repealed)', 'పార్ట్ B రాష్ట్రాలు (రద్దు)', 7, '#64748B', '#CBD5E1'),
    ('Part VIII', 'Union Territories', 'కేంద్రపాలిత ప్రాంతాలు', 7, '#155E75', '#A5F3FC'),
    ('Part IX', 'Panchayats', 'పంచాయతీలు', 10, '#166534', '#86EFAC'),
    ('Part IXA', 'Municipalities', 'పురపాలికలు', 10, '#15803D', '#BBF7D0'),
    ('Part IXB', 'Co-operative societies', 'సహకార సంఘాలు', 10, '#4D7C0F', '#D9F99D'),
    ('Part X', 'Scheduled & tribal areas', 'షెడ్యూల్డ్, గిరిజన ప్రాంతాలు', 8, '#9A3412', '#FED7AA'),
    ('Part XI', 'Union–State relations', 'కేంద్ర–రాష్ట్ర సంబంధాలు', 8, '#1E40AF', '#BFDBFE'),
    ('Part XII', 'Finance & property', 'ఆర్థికం, ఆస్తి', 8, '#A16207', '#FEF08A'),
    ('Part XIII', 'Trade & commerce', 'వర్తకం, వాణిజ్యం', 8, '#B45309', '#FDE68A'),
    ('Part XIV', 'Services', 'సర్వీసులు', 8, '#475569', '#E2E8F0'),
    ('Part XIVA', 'Tribunals', 'ట్రిబ్యునళ్లు', 7, '#334155', '#CBD5E1'),
    ('Part XV', 'Elections', 'ఎన్నికలు', 9, '#9F1239', '#FDA4AF'),
    ('Part XVI', 'Special provisions for classes', 'కొన్ని వర్గాలకు ప్రత్యేక నిబంధనలు', 6, '#4F46E5', '#C7D2FE'),
    ('Part XVII', 'Official language', 'అధికార భాష', 8, '#0369A1', '#BAE6FD'),
    ('Part XVIII', 'Emergency', 'అత్యవసర పరిస్థితి', 8, '#B91C1C', '#FCA5A5'),
    ('Part XIX', 'Miscellaneous', 'ఇతర నిబంధనలు', 7, '#57534E', '#E7E5E4'),
    ('Part XX', 'Amendment', 'రాజ్యాంగ సవరణ', 6, '#A21CAF', '#F0ABFC'),
    ('Part XXI', 'Temporary & special provisions', 'తాత్కాలిక, ప్రత్యేక నిబంధనలు', 8, '#BE185D', '#F9A8D4'),
    ('Part XXII', 'Short title & repeals', 'సంక్షిప్త నామం, రద్దులు', 6, '#78716C', '#D6D3D1'),
    ('Schedules', 'Schedules', 'షెడ్యూళ్లు', 6, '#0F766E', '#99F6E4'),
    ('General', 'General', 'సాధారణ', 6, '#475569', '#CBD5E1'),
]
PART_BY = {p[0]: p for p in PARTS}
PART_ORDER = {p[0]: i for i, p in enumerate(PARTS)}
UNITS = (6, 7, 8, 9, 10)


def norm_part(p):
    """'Part XIV-A' -> 'Part XIVA'; unknown / empty -> None."""
    p = re.sub(r'\s+', ' ', str(p or '')).strip().replace('-', '')
    p = re.sub(r'^part ', 'Part ', p, flags=re.I)
    return p if p in PART_BY else None


def part_of_article(no):
    """Constitution Part of an article label: '21' -> 'Part III', '51A(a)' -> 'Part IVA', '243ZH' -> 'Part IXB', 'Preamble' -> 'Preamble'."""
    s = str(no or '').strip()
    if re.match(r'preamble', s, re.I):
        return 'Preamble'
    if re.search(r'schedule', s, re.I):
        return 'Schedules'
    m = re.match(r'(\d+)([A-Z]*)', s.upper())
    if not m:
        return None
    n, suf = int(m.group(1)), m.group(2)
    if (n, suf) == (51, 'A'):
        return 'Part IVA'
    if n == 323 and suf in ('A', 'B'):
        return 'Part XIVA'
    if n == 243:
        if not suf or (len(suf) == 1 and suf <= 'O'):
            return 'Part IX'
        return 'Part IXA' if len(suf) == 1 or suf <= 'ZG' else 'Part IXB'
    for a, b, part in PART_RANGES:
        if a <= n <= b:
            return part
    return None


def _first_part(nos):
    for no in nos:
        p = part_of_article(no)
        if p:
            return p
    return None


def classify(it):
    """Fill it['part'] / it['unit'] when missing (in place). Articles: their own number; amendments: the articles they changed
    (changes first, then articles); cases: their articles, else 'General'. Unit: the card's chapter ('6.4' -> 6), else the Part's unit."""
    d = it.get('deck') or deck_of(it.get('id'))
    part = norm_part(it.get('part'))
    if not part:
        if d == 'articles':
            part = part_of_article(it.get('front_short'))
        else:
            nos = [str(ch.get('article_id') or ch.get('article') or '').rsplit('-', 1)[-1] for ch in it.get('changes') or [] if isinstance(ch, dict)]
            part = _first_part(nos + [str(a) for a in it.get('articles') or []] + list(it.get('schedules') or []))
    it['part'] = part or 'General'
    try:
        unit = int(it.get('unit') or str(it.get('chapter') or '').split('.')[0])
    except ValueError:
        unit = None
    it['unit'] = unit if unit in UNITS else PART_BY[it['part']][3]
    _pp = PART_BY[it['part']]
    it['part_label_en'] = _pp[0] if _pp[0] in ('Preamble', 'Schedules', 'General') else _pp[0] + ' · ' + _pp[1]
    it['part_label_te'] = ('భాగం ' + _pp[0][5:] + ' · ' + _pp[2]) if _pp[0].startswith('Part ') else _pp[2]
    return it


def part_counts(its):
    """[(part tuple, count)] for the Parts present, in Constitution order."""
    c = {}
    for i in its:
        c[i['part']] = c.get(i['part'], 0) + 1
    return [(PART_BY[p], c[p]) for p in sorted(c, key=lambda p: PART_ORDER.get(p, 99))]


def unit_counts(its):
    c = {u: 0 for u in UNITS}
    for i in its:
        c[i['unit']] = c.get(i['unit'], 0) + 1
    return c


def _tile_sub(it):
    s = str(it.get('front_sub') or '')
    return s[:4] if s[:4].isdigit() else s


def light(it, deck_cfg):
    """The tile / index data of one card (embedded in the deck page; the full card is fetched on open)."""
    th = deck_cfg.get('themes') and it.get('theme_acc')
    o = {'id': it['id'], 'n': it.get('front_short') or '', 'f': [it.get('front_en') or '', it.get('front_te') or ''],
         'c': [it.get('cue_en') or '', it.get('cue_te') or ''], 's': _tile_sub(it), 'ch': it.get('chapter') or '',
         'p': it['part'], 'u': it['unit'], 'src': it.get('source') or '', 'two': 1 if it.get('two_way') else 0}
    if th:
        o.update(acc=it['theme_acc'], ink=it['theme_ink'], th=it.get('theme_id'), band=[it.get('theme_short_en'), it.get('theme_short_te')])
    if it.get('parties_en'):
        vte = re.sub(r'\s*\([^)]*\)', '', it.get('vs_te') or '').strip()
        o['short'] = [it.get('short_en') or '', it.get('short_te') or it.get('short_en') or '']
        o['vs'] = [it.get('vs_en') or '', vte or it.get('vs_en') or ''] if it.get('vs_en') else None
    if it.get('popular_en'):
        o['pop'] = [it['popular_en'], it.get('popular_te') or it['popular_en']]
    return o


def light_themes(deck_id):
    return [{'id': t['id'], 'n': str(t['i'] + 1), 'f': [t['en'], t['te']], 'c': [t['en'], t['te']], 'acc': t['acc'], 'ink': t['ink'],
             'band': [t['short_en'], t['short_te']], 'cases': [c['id'] for c in t['cases']], 'theme': 1} for t in themes(deck_id)]


def data_version():
    """Changes whenever a deck / article / chain / links file or the card template changes (ETag + fetch URL)."""
    import hashlib
    root = Path(__file__).resolve().parents[2]
    files = sorted(DIR.glob('*.json')) + sorted(_art.DIR.glob('*.json')) + [root / 'app' / 'templates' / 'ds' / 'polity_recall_card.html']
    h = hashlib.sha1()
    for f in files:
        try:
            st = f.stat()
            h.update(f'{f.name}:{st.st_mtime_ns}:{st.st_size};'.encode())
        except OSError:
            continue
    return h.hexdigest()[:12]


_SEEN = {'v': None}


def refresh():
    """Drop cached decks when any source file changed (a running server otherwise keeps stale counts, e.g. 140 of 174 cases)."""
    v = data_version()
    if _SEEN['v'] not in (None, v):
        for mod in (globals(), vars(_art)):
            for f in list(mod.values()):
                if callable(getattr(f, 'cache_clear', None)) and getattr(f, '__module__', '') in (__name__, _art.__name__):
                    f.cache_clear()
    _SEEN['v'] = v
    return v


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
        return [classify(_article_item(c)) for c in _art.all_cards()]
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
            out.append(classify(it))
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


CHAINS_FILE = DIR / 'case_chains.json'


@lru_cache(maxsize=None)
def chains():
    """{chain_id: chain} from case_chains.json ({chains:[{chain_id,title_te/en,intro_te/en,steps[...]}]}); missing/bad -> {}."""
    try:
        data = json.loads(CHAINS_FILE.read_text(encoding='utf-8'))
    except (ValueError, OSError):
        return {}
    out = {}
    for ch in (data.get('chains') if isinstance(data, dict) else data) or []:
        if isinstance(ch, dict) and ch.get('chain_id'):
            ch = dict(ch, steps=sorted(ch.get('steps') or [], key=lambda s: s.get('step') or 0))
            out[ch['chain_id']] = ch
    return out


# A case's own theme decides which of its chains is shown first (and which chain the theme view shows).
THEME_CHAIN = {'Amending power & basic structure': 'CH-amending-power', 'Right to property & Ninth Schedule': 'CH-property-ninth-schedule',
               'Equality & reservation': 'CH-reservation', 'Life & personal liberty (Article 21)': 'CH-article-21',
               'Rights read into Article 21': 'CH-article-21', 'Privacy, gender & personal law': 'CH-article-21',
               'DPSP & Fundamental Duties': 'CH-fr-dpsp', 'Judiciary & tribunals': 'CH-tribunals'}


def card_chains(c):
    """[(chain, step)] for every chain that lists card c — from c['chains'] (or legacy c['chain']); the card's theme chain first."""
    allc = chains()
    refs = c.get('chains') or ([c['chain']] if isinstance(c.get('chain'), dict) else [])
    out = [(allc[r['chain_id']], r.get('step')) for r in refs if isinstance(r, dict) and r.get('chain_id') in allc]
    home = THEME_CHAIN.get(c.get('theme_en'))
    out.sort(key=lambda x: x[0]['chain_id'] != home)
    return out


def ref_url(ref):
    """Deck URL of a chain step's card, or None when the ref is not a card."""
    return card_url(ref) if ref and ref in index()['cards'] else None


_EXAM_PREFIX = re.compile(r'^\s*other\s+credible\s+examinations\s*(?:-|–|—)\s*', re.I)


def exam_label(s):
    """'Other credible examinations - TSPSC Group IV' -> 'TSPSC Group IV'."""
    return _EXAM_PREFIX.sub('', s or '')


# ── interlinking: links.json + mention index + auto-linking ──
LINKS_FILE = DIR / 'links.json'
DECK_OF = {'AC': 'articles', 'AM': 'amendments', 'CS': 'cases'}
KIND = {'articles': 'art', 'amendments': 'am', 'cases': 'case'}


def deck_of(card_id):
    return DECK_OF.get(str(card_id or '')[:2])


@lru_cache(maxsize=None)
def links():
    """{card_id: {articles:[ids], amendments:[ids], cases:[ids]}}; missing/bad file -> {}."""
    try:
        data = json.loads(LINKS_FILE.read_text(encoding='utf-8'))
    except (ValueError, OSError):
        return {}
    return data if isinstance(data, dict) else {}


def _ord(n):
    n = int(n)
    return f"{n}{'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"


def _variants(it):
    """Name variants a text may use for this card (English, Telugu)."""
    d, v = it.get('deck') or deck_of(it['id']), []
    if d == 'articles':
        a = it.get('front_short') or ''
        v = [f'Article {a}', f'Art. {a}', f'Art {a}', f'ప్రకరణ {a}', f'ప్రకరణ (Article) {a}', f'ప్ర. {a}']
    elif d == 'amendments':
        n = str(it.get('sort') or '')
        if n.isdigit():
            v = [f'{_ord(n)} Amendment', f'{_ord(n)} Constitutional Amendment', f'{n}వ సవరణ', f'{n}వ రాజ్యాంగ సవరణ']
        v += [it.get('front_en') or '', it.get('front_te') or '']
    elif d == 'cases':
        fe, ft = it.get('front_en') or '', it.get('front_te') or ''
        v = [fe, re.sub(r'\s+case$', '', fe, flags=re.I), ft, re.sub(r'\s*కేసు$', '', ft), it.get('short_en') or '', it.get('short_te') or '']
        # popular names ('Cross Roads case', 'Mandal case') only in full: the bare words ('Fundamental Rights') are too generic
        v += [p for p in (it.get('popular_en'), it.get('popular_te')) if p and p.strip().lower() not in GENERIC]
        for p in (it.get('parties_en'), it.get('parties_te')):
            if p:
                v += [p, re.sub(r'\s*\([^)]*\)', '', p)]
    return [x.strip() for x in dict.fromkeys(v) if x and len(x.strip()) >= 4]


GENERIC = {'case', 'the case', 'కేసు', 'fundamental rights', 'privacy', 'emergency', 'equality', 'reservation'}

_INDEX = {}


def index():
    """{'cards': {id: item}, 'names': {variant: id}, 'rx': compiled regex} over all three decks (rebuilt when items change)."""
    lists = [items(k) for k in DECKS]
    key = tuple(id(x) for x in lists)
    if _INDEX.get('key') == key:
        return _INDEX
    cards, names, dup = {}, {}, set()
    for lst in lists:
        for it in lst:
            cards[it['id']] = it
            for n in _variants(it):
                if n in names and names[n] != it['id']:
                    dup.add(n)
                names.setdefault(n, it['id'])
    for n in dup:  # a name shared by two cards is ambiguous: never auto-link it
        names.pop(n)
    alts = sorted(names, key=len, reverse=True)
    rx = re.compile('(?<![0-9A-Za-z])(' + '|'.join(re.escape(str(escape(n))) for n in alts) + ')(?![0-9A-Za-z])') if alts else None
    _INDEX.clear()
    _INDEX.update(key=key, cards=cards, names={str(escape(k)): v for k, v in names.items()}, rx=rx)
    return _INDEX


def card_url(card_id, **kw):
    from flask import url_for
    return url_for('polity_unit6.recall_deck', deck_id=deck_of(card_id), open=card_id, **kw)


def autolink(text, own_id=None):
    """Escape text and wrap mentions of OTHER cards in <a class="xl xl-art|xl-am|xl-case" data-go=id>; one link per target."""
    if not text:
        return Markup('')
    s, ix = str(escape(text)), index()
    if not ix['rx']:
        return Markup(s)
    seen = set()

    def rep(m):
        cid = ix['names'].get(m.group(1))
        if not cid or cid == own_id or cid in seen:
            return m.group(0)
        seen.add(cid)
        d = deck_of(cid)
        return f'<a class="xl xl-{KIND[d]}" data-go="{cid}" data-deck="{d}" href="{escape(card_url(cid))}">{m.group(0)}</a>'
    return Markup(ix['rx'].sub(rep, s))


def label(card_id):
    """Short chip label (en, te): 'Art 21A', '42nd Amdt', 'Maneka Gandhi'."""
    it = index()['cards'].get(card_id)
    if not it:
        return None
    d = deck_of(card_id)
    if d == 'articles':
        return f"Art {it['front_short']}", f"ప్ర. {it['front_short']}"
    if d == 'amendments':
        n = str(it.get('sort') or '')
        return (f'{_ord(n)} Amdt', f'{n}వ సవరణ') if n.isdigit() else (it['front_en'], it['front_te'])
    return it.get('short_en') or re.sub(r'\s+case$', '', it['front_en'], flags=re.I), it.get('short_te') or re.sub(r'\s*కేసు$', '', it.get('front_te') or '')


def _ids(v):
    for x in v or []:
        yield x.get('id') if isinstance(x, dict) else x


def related(it):
    """{'articles': [...], 'amendments': [...], 'cases': [...]} of {id, deck, en, te, url}, from links.json + structured fields."""
    ix = index()
    art_by_no = {c.get('front_short'): c['id'] for c in ix['cards'].values() if c.get('deck') == 'articles' or c['id'].startswith('AC-')}
    want = {k: list(v) for k, v in (links().get(it['id']) or {}).items() if k in KIND}
    for k in KIND:
        for x in _ids(it.get(k) if isinstance(it.get(k), list) else []):
            if k == 'articles' and x and not str(x).startswith('AC-'):
                x = art_by_no.get(str(x))
            want.setdefault(k, []).append(x)
        for ch in it.get('changes') or []:  # amendment changes -> articles
            if k == 'articles' and ch.get('article'):
                want.setdefault(k, []).append(ch['article'] if str(ch['article']).startswith('AC-') else art_by_no.get(str(ch['article'])))
    out = {}
    for k in KIND:
        ids = [x for x in dict.fromkeys(want.get(k) or []) if x and x != it['id'] and x in ix['cards']]
        if k == 'articles':
            ids.sort(key=lambda x: ix['cards'][x].get('sort') or ())
        out[k] = [{'id': x, 'deck': k, 'en': label(x)[0], 'te': label(x)[1], 'url': card_url(x)} for x in ids]
    return out


def art_ref(no):
    """(card_id, url) of the articles-deck card for an article number ('21', '19(1)(g)' -> Art 19 if no exact card), else None."""
    s = str(no or '').strip()
    if not s:
        return None
    by = {c.get('front_short'): c['id'] for c in index()['cards'].values() if c['id'].startswith('AC-')}
    cid = by.get(s) or by.get(re.sub(r'\(.*$', '', s))
    return (cid, card_url(cid)) if cid else None
