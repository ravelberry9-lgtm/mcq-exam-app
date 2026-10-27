"""Original, source-linked baseline practice; no learner-state writes."""
from pathlib import Path
from functools import lru_cache
from urllib.parse import urlsplit
import json,hashlib,re
from bs4 import BeautifulSoup
from flask import current_app

def _root(): return Path(current_app.root_path).parent

def manifest():
    return json.loads((_root()/'content/geography/original_practice_manifest.json').read_text(encoding='utf-8'))

@lru_cache(maxsize=100)
def _read(path,mtime,pin,bookpath,booktime):
    raw=Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=pin: raise ValueError('Original practice fingerprint mismatch')
    data=json.loads(raw);book=Path(bookpath).read_bytes()
    if hashlib.sha256(book).hexdigest()!=data['chapter_sha256']:raise ValueError('Original chapter fingerprint mismatch')
    soup=BeautifulSoup(book,'html.parser');seen=set()
    for q in data['questions']:
        if q['id'] in seen or type(q['answer']) is not int or q['answer'] not in (1,2,3,4):raise ValueError('Invalid original question')
        seen.add(q['id'])
        if len(q['options'])!=4 or len(set(q['options']))!=4 or len(q['option_explanations'])!=4:raise ValueError('Invalid original options')
        node=soup.find(id=q['section'])
        if not node or not q['question_te'] or not q['explanation_te'] or not all(q['option_explanations']):raise ValueError('Missing original explanation or anchor')
        norm=lambda s:re.sub(r'\s+',' ',s).strip()
        if norm(q['source_paragraph']) not in norm(soup.article.get_text(' ',strip=True)):raise ValueError('Missing literal original snippet')
        if not q['source_urls'] or any(urlsplit(u).scheme!='https' for u in q['source_urls']):raise ValueError('Invalid original learning source')
    return data

def chapter(cid):
    entry=manifest()['chapters'].get(cid)
    if not entry:return None
    r=_root();p=r/'content/geography/original_practice'/f'{cid}.json';b=r/'static/textbooks/geography/lessons'/entry['file']
    return _read(str(p),p.stat().st_mtime_ns,entry['sha256'],str(b),b.stat().st_mtime_ns)

def question(cid,qid):
    d=chapter(cid)
    return next((q for q in d['questions'] if q['id']==qid),None) if d else None

def grade(q,choice):
    if q.get('chapter') in ('01','02'):
        from .chapter01_bilingual import is_held
        if is_held(q['id'],q['chapter']):return {'score':None,'correct':None,'status':'unscored'}
    if type(choice) is not int or choice not in (1,2,3,4):raise ValueError('Choose 1 to 4')
    return {'score':int(choice==q['answer']),'correct':choice==q['answer'],'status':'scored'}

@lru_cache(maxsize=4)
def _difficulty_review(path, stamp, bank_pin):
    data=json.loads(Path(path).read_bytes())
    if data.get('format')!='geography-difficulty-review-v1' or data.get('source_bank_sha256')!=bank_pin:
        raise ValueError('Difficulty review does not match the current question bank')
    if any(v.get('level') not in ('easy','moderate','hard') or not v.get('reason') for v in data['questions'].values()):
        raise ValueError('Invalid difficulty review entry')
    return data['questions']


def difficulty(q):
    if q.get('chapter')=='02':
        path=_root()/'content/geography/chapter02_difficulty_review.json'
        if path.exists():
            return _difficulty_review(str(path),path.stat().st_mtime_ns,manifest()['chapters']['02']['sha256'])[q['id']]
    return {'level':q.get('difficulty'),'reason':q.get('difficulty_reason')}
