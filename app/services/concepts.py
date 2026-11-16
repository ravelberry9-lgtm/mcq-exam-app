"""Concept cards: topics (Fundamental Rights, Judiciary, ...) made of linked sub-cards, and the question -> sub-card map.

content/polity/g2/concepts/index.json  {"topics":[{"id","title","summary","subs":[{"id","title"}]}], "qmap":{qid:[sub ids, primary first]}}
content/polity/g2/concepts/topics/<topic>.json  {"id","title","summary","subcards":[{id,title,summary,at_a_glance,sections}]}
"""
import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / 'content' / 'polity' / 'g2' / 'concepts'
BLOCKS = {'text', 'points', 'table', 'compare', 'timeline', 'flow', 'tree', 'remember', 'link', 'quote'}


@lru_cache(maxsize=1)
def index():
    p = ROOT / 'index.json'
    d = json.loads(p.read_text(encoding='utf-8')) if p.is_file() else {'topics': [], 'qmap': {}}
    d['sub_topic'] = {s['id']: t['id'] for t in d['topics'] for s in t['subs']}
    d['by_id'] = {t['id']: t for t in d['topics']}
    return d


def topics():
    return index()['topics']


@lru_cache(maxsize=64)
def topic(tid):
    p = ROOT / 'topics' / f'{tid}.json'
    if tid not in index()['by_id'] or not p.is_file():
        return None
    return json.loads(p.read_text(encoding='utf-8'))


def topic_of(sub_id):
    return index()['sub_topic'].get(sub_id)


def subs_for(qid):
    """[(topic id, sub id, sub title)] for a question, primary first."""
    out, ix = [], index()
    for s in ix['qmap'].get(qid, []):
        t = ix['sub_topic'].get(s)
        if t:
            title = next((x['title'] for x in ix['by_id'][t]['subs'] if x['id'] == s), s)
            out.append((t, s, title))
    return out


def link_target(ref):
    """'fr-freedom' or 'fundamental-rights' -> (topic id, sub id or None)."""
    ix = index()
    if ref in ix['sub_topic']:
        return ix['sub_topic'][ref], ref
    if ref in ix['by_id']:
        return ref, None
    return None, None
