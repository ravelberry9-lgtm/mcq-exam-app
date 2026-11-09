"""Unit 6 map reader. Manifests are data; missing maps never create buttons."""
from pathlib import Path
import hashlib
import json
import re
from flask import Blueprint, abort, current_app, g, has_request_context, redirect, render_template, send_from_directory, url_for

bp = Blueprint('polity_maps', __name__, url_prefix='/learn/polity/unit6')
ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT/'content/polity/g2'
MAPS = ROOT/'static/polity/unit6/maps'

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

_record_cache = (None, None)

def records():
    global _record_cache
    paths=sorted(CONTENT.glob('6.*/*/*.json'))+sorted((CONTENT/'_shared').glob('*.json'))
    signature=tuple((str(p),p.stat().st_mtime_ns,p.stat().st_size) for p in paths)
    if signature!=_record_cache[0]:
        _record_cache=(signature,_load_records())
    return _record_cache[1]

def _load_records():
    result = {}
    shared = read(CONTENT/'_shared/Explanations.json')
    shared_ex = shared.get('questions', shared.get('explanations', {}))
    for chapter in sorted(CONTENT.glob('6.*/*')):
        if not chapter.is_dir(): continue
        ex = read(chapter/'Explanations.json') if (chapter/'Explanations.json').is_file() else {}
        ex = {**shared_ex, **ex.get('questions',ex.get('explanations',ex))}
        for filename,kind in [('Chapter-Test.json','chaptertest'),('Questions.json','bank'),('PYQ-Set.json','pyq'),('Publisher-Questions.json','publisher')]:
            path=chapter/filename
            if not path.is_file():continue
            data=read(path)
            for original in data.get('questions',data.get('items',[])):
                q=dict(original)
                # Source statuses govern display; manifest answer_state is never a key.
                q['_kind']=kind;q['_chapter']=chapter.name
                q['_scored']=q.get('scored',True) is True
                q['_answer']=q.get('study_answer') if kind in ('pyq','publisher') or not q['_scored'] else q.get('answer')
                rationale=ex.get(q.get('explanation_id',q['id']),{})
                q['_en']=q.get('explanation_en') or rationale.get('en','')
                q['_te']=q.get('explanation_te') or rationale.get('te','')
                result[q['id']]=q
    mapping=read(CONTENT/'_shared/PYQ-mapping.json')
    for original in read(CONTENT/'_shared/PYQs.json'):
        chapter=mapping.get(original['id'],{}).get('primary_subchapter','')
        if not chapter.startswith('6.'):continue
        q=dict(original);q.update(_kind='primary_pyq',_chapter=chapter,_scored=q.get('scored',True) is True)
        q['_answer']=q.get('answer') if q['_scored'] else q.get('study_answer')
        rationale=shared_ex.get(q.get('explanation_id',q['id']),{})
        q['_en']=q.get('explanation_en') or rationale.get('en','');q['_te']=q.get('explanation_te') or rationale.get('te','')
        result.setdefault(q['id'],q)
    for original in read(CONTENT/'_shared/Expected-Questions.json'):
        chapter=original.get('primary_subchapter','')
        if not chapter.startswith('6.') or 'canonical_question_id' in original:continue
        q=dict(original);q.update(_kind='expected',_chapter=chapter,_scored=q.get('scored',True) is True)
        q['_answer']=q.get('answer') if q['_scored'] else q.get('study_answer')
        rationale=shared_ex.get(q.get('explanation_id',q['id']),{})
        q['_en']=q.get('explanation_en') or rationale.get('en','');q['_te']=q.get('explanation_te') or rationale.get('te','')
        result.setdefault(q['id'],q)
    return result

def catalog():
    if has_request_context() and hasattr(g,'unit6_map_catalog'):
        return g.unit6_map_catalog
    result={}
    if not MAPS.is_dir():return result
    for path in sorted(MAPS.glob('*.json')):
        data=read(path)
        for m in data.get('maps',[]):
            name=m.get('file','');mid=m.get('map_id','')
            if not re.fullmatch(r'[A-Za-z0-9_.-]+',mid) or Path(name).name!=name or not name.endswith('.html'):
                raise ValueError('Unsafe memory-map manifest')
            page=MAPS/name
            if not page.is_file():continue
            if mid in result:raise ValueError('Duplicate memory-map ID')
            if m.get('sha256') and hashlib.sha256(page.read_bytes()).hexdigest()!=m['sha256']:
                raise ValueError('Memory-map checksum mismatch')
            result[mid]=m
    if has_request_context():g.unit6_map_catalog=result
    return result

def maps_for(item_id):
    return [m for m in catalog().values() if any(x['item_id']==item_id for x in m['links'])]

@bp.app_context_processor
def map_context():
    return {'unit6_maps_for':maps_for}

@bp.get('/maps')
def index():
    return render_template('ds/polity_maps.html',maps=list(catalog().values()))

@bp.get('/maps/<map_id>')
def page(map_id):
    m=catalog().get(map_id)
    if not m:abort(404)
    return send_from_directory(MAPS,m['file'])

@bp.get('/maps/<map_id>/questions')
def linked_questions(map_id):
    m=catalog().get(map_id)
    if not m:abort(404)
    corpus=records();items=[]
    for link in m['links']:
        if link['item_id'] not in corpus:abort(500,description='Unresolved map link')
        items.append((corpus[link['item_id']],link))
    return render_template('ds/polity_maps.html',map=m,items=items)

@bp.get('/questions/<item_id>')
def question(item_id):
    q=records().get(item_id)
    if not q:abort(404)
    return redirect(url_for('polity_unit6.practice',item_id=item_id))
