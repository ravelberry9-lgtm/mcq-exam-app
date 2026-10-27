"""Original solar-system practice; separate from immutable historical PYQs."""
from functools import lru_cache
from pathlib import Path
from urllib.parse import urlsplit
import hashlib,json
from flask import current_app

@lru_cache(maxsize=4)
def _load(path,mtime,chapter_path,chapter_mtime,pin):
    raw=Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=pin:
        raise ValueError('Solar practice release fingerprint differs')
    payload=json.loads(raw)
    chapter=Path(chapter_path).read_bytes()
    if payload.get('format')!='solar-original-practice-v1' or len(payload.get('questions',[]))!=96:
        raise ValueError('Invalid solar practice release')
    if hashlib.sha256(chapter).hexdigest()!=payload.get('chapter_sha256'):
        raise ValueError('Solar practice chapter fingerprint differs')
    records=payload['questions'];ids=set()
    for q in records:
        if q['id'] in ids or type(q['answer']) is not int or q['answer'] not in (1,2,3,4):
            raise ValueError('Invalid solar practice answer or ID')
        ids.add(q['id'])
        if (len(q['options'])!=4 or len(set(q['options']))!=4 or len(q['option_explanations'])!=4
            or not q['question_te'] or not q['explanation_te'] or not q['excerpt']
            or ('id="'+q['section']+'"').encode() not in chapter):
            raise ValueError('Incomplete solar practice question')
        if not q['source_urls'] or any(urlsplit(u).scheme!='https' or not urlsplit(u).netloc for u in q['source_urls']):
            raise ValueError('Invalid learning source')
    return payload

def payload():
    root=Path(current_app.root_path).parent
    path=root/'content/geography/solar_practice.json'
    chapter=root/'static/textbooks/geography/lessons/03_Earth_in_the_Solar_System_Bilingual_Foundation.html'
    pin=json.loads((root/'content/geography/solar_manifest.json').read_text(encoding='utf-8'))['payload_sha256']
    return _load(str(path),path.stat().st_mtime_ns,str(chapter),chapter.stat().st_mtime_ns,pin)

def questions(topic=None,kind=None,qlang=None):
    return [q for q in payload()['questions'] if (not topic or str(q['topic'])==str(topic)) and (not kind or q['kind']==kind)]

def question(qid):
    return next((q for q in questions() if q['id']==qid),None)

def grade(q,choice):
    if type(choice) is not int or choice not in (1,2,3,4):
        raise ValueError('Choose an option from 1 to 4')
    return {'status':'scored','score':int(choice==q['answer']),'correct':choice==q['answer']}
