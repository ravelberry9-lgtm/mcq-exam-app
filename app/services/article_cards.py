"""Article recall deck for Unit 6 (article number <-> concept cards)."""
import json
from functools import lru_cache
from pathlib import Path

DIR = Path(__file__).resolve().parents[2] / 'content' / 'polity' / 'g2' / 'article_cards'


def _sort_key(a):
    s = str(a['article'])
    num = ''.join(ch for ch in s if ch.isdigit())
    return (int(num) if num else 0, s)


@lru_cache(maxsize=1)
def all_cards():
    out = []
    if DIR.is_dir():
        for f in sorted(DIR.glob('6.*.json')):
            try:
                out.extend(json.loads(f.read_text(encoding='utf-8')))
            except (ValueError, OSError):
                continue
    return sorted(out, key=lambda a: (a['chapter'], _sort_key(a)))


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
