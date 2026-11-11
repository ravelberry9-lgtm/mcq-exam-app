"""Article recall deck for Unit 6 (article number <-> concept cards)."""
import json
import re
from functools import lru_cache
from pathlib import Path

DIR = Path(__file__).resolve().parents[2] / 'content' / 'polity' / 'g2' / 'article_cards'


_ART = re.compile(r'^\s*(\d+)\s*([A-Za-z]*)\s*(?:\(\s*([^)]*?)\s*\))?(.*)$')


def article_key(article):
    """Natural sort key for an article label.

    Numeric part first, then the letter suffix, then a clause in brackets:
    21 < 21A < 21B < 22; 239A < 239AA < 239B; 243A < 243Z < 243ZA; 371 < 371A .. 371J;
    51A < 51A(a) < 51A(b) .. 51A(k); 394 < 394A < 395. Labels with no leading number sort last.
    """
    s = str(article)
    m = _ART.match(s)
    if not m:
        return (1, 0, '', (), s)
    num, suf, clause, rest = m.groups()
    ck = () if clause is None else ((0, int(clause), '') if clause.isdigit() else (1, 0, clause.lower()),)
    return (0, int(num), suf.upper(), ck, rest)


def _sort_key(a):
    return article_key(a['article'])


@lru_cache(maxsize=1)
def all_cards():
    out = []
    if DIR.is_dir():
        for f in sorted([*DIR.glob('6.*.json'), *DIR.glob('p*.json'), *DIR.glob('omitted.json')]):
            try:
                out.extend(json.loads(f.read_text(encoding='utf-8')))
            except (ValueError, OSError):
                continue
    # one continuous ascending article sequence across chapters; chapter order breaks any tie
    return sorted(out, key=lambda a: (_sort_key(a), a['chapter']))


def omitted_list(c):
    """A card's `omitted` field as a list (whole Article and/or clauses); [] when nothing was omitted."""
    o = c.get('omitted')
    return [x for x in (o if isinstance(o, list) else [o]) if isinstance(x, dict)] if o else []


def omitted_whole(c):
    """True when the whole Article was omitted (an `omitted` entry with no clause label)."""
    return any(not x.get('clause') for x in omitted_list(c))


def chapter_cards(chapter_id=None):
    cards = all_cards()
    return [c for c in cards if not chapter_id or c['chapter'] == chapter_id]


def groups(cards):
    """Preserve first-seen order of (chapter, group)."""
    seen, out = {}, []
    for c in cards:
        k = (c['chapter'], c.get('group_en') or '')
        if k not in seen:
            seen[k] = {'chapter': c['chapter'], 'group_en': k[1], 'group_te': c.get('group_te') or '', 'cards': []}
            out.append(seen[k])
        seen[k]['cards'].append(c)
    return out
