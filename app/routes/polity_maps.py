"""Unit 6 map reader. Manifests are data; missing maps never create buttons."""
from pathlib import Path
import hashlib
import json
import re
from flask import Blueprint, abort, current_app, g, has_request_context, make_response, redirect, render_template, request, send_from_directory, url_for

bp = Blueprint('polity_maps', __name__, url_prefix='/learn/polity/unit6')
ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT/'content/polity/g2'
MAPS = ROOT/'static/polity/unit6/maps'

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

_record_cache = (None, None)
_CHAPTER_DIR=re.compile(r'^(?:[6-9]|10)\.\d+\.\d+$')
def chapter_dirs():
    """Chapter folders of syllabus units 6-10 (content/polity/g2/<unit>.<sec>/<unit>.<sec>.<ch>)."""
    return sorted((d for d in CONTENT.glob('*.*/*') if d.is_dir() and _CHAPTER_DIR.match(d.name) and d.parent.name==d.name.rsplit('.',1)[0]),key=lambda d:[int(x) for x in d.name.split('.')])

def base_records():
    global _record_cache
    paths=sorted(p for d in chapter_dirs() for p in d.glob('*.json'))+sorted((CONTENT/'_shared').glob('*.json'))
    signature=tuple((str(p),p.stat().st_mtime_ns,p.stat().st_size) for p in paths)
    if signature!=_record_cache[0]:
        _record_cache=(signature,_load_records())
    return _record_cache[1]

_admin_tables_ready=set()
def ensure_admin_tables():
    """Create the two additive admin tables if the migration has not been run (idempotent, once per database)."""
    from ..db import db
    from ..polity_models import PolityUnit6Override,PolityUnit6Submission
    key=str(db.engine.url)
    if key in _admin_tables_ready:return
    for t in (PolityUnit6Override.__table__,PolityUnit6Submission.__table__):t.create(db.engine,checkfirst=True)
    _admin_tables_ready.add(key)
EDIT_FIELDS=('question_en','question_te','options_en','options_te','answer','explanation_en','explanation_te')
def overrides():
    if has_request_context() and 'unit6.overrides' in request.environ:return request.environ['unit6.overrides']
    try:
        from ..polity_models import PolityUnit6Override
        from ..db import db
        ensure_admin_tables()
        rows={o.item_id:o for o in PolityUnit6Override.query.all()}
    except Exception:
        try:db.session.rollback()
        except Exception:pass
        rows={}
    if has_request_context():request.environ['unit6.overrides']=rows
    return rows
def records():
    """Authored records with admin overrides applied (copy-on-write; the files are never touched)."""
    base=base_records();ov=overrides()
    if not ov:return base
    out=dict(base)
    for item_id,o in ov.items():
        if item_id not in out:continue
        if o.deleted:out.pop(item_id);continue
        q=dict(out[item_id]);d=o.data or {}
        for k in ('question_en','question_te','options_en','options_te'):
            if d.get(k):q[k]=d[k]
        if d.get('answer') in (1,2,3,4):q['_answer']=d['answer'];q['_scored']=True
        if d.get('explanation_en'):q['_en']=d['explanation_en']
        if d.get('explanation_te'):q['_te']=d['explanation_te']
        q['_edited']=True;out[item_id]=q
    return out

def _load_records():
    result = {}
    shared = read(CONTENT/'_shared/Explanations.json')
    shared_ex = shared.get('questions', shared.get('explanations', {}))
    for chapter in chapter_dirs():
        ex = read(chapter/'Explanations.json') if (chapter/'Explanations.json').is_file() else {}
        ex = {**shared_ex, **ex.get('questions',ex.get('explanations',ex))}
        for filename,kind in [('Chapter-Test.json','chaptertest'),('Questions.json','bank'),('Laxmikanth-Questions.json','bank'),('PYQ-Set.json','pyq'),('PYQ-Bank-Set.json','pyq'),('Publisher-Questions.json','publisher')]:
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
    # Current-affairs MCQs (Nov 2025 – Nov 2026): stored with their topic notes; filed under a related chapter.
    caf=CONTENT/'current-affairs'/'topics.json'
    if caf.is_file():
        for t in read(caf).get('topics',[]):
            for m in t.get('mcqs',[]):
                q={'id':m['id'],'question_en':m['question_en'],'question_te':m.get('question_te',''),'options_en':m['options_en'],'options_te':m.get('options_te',[]),'answer':m['answer']}
                q.update(_kind='bank',_chapter=t.get('host_chapter','6.1.1'),_scored=True,_answer=m['answer'],_en=m.get('explanation_en',''),_te=m.get('explanation_te',''),ca_topic=t['id'],ca_period=t.get('period','recent'),_ca=True,ca_trap=bool(m.get('trap')),ca_pyq=m.get('pyq',''),ca_disputed=bool(m.get('disputed')))
                result.setdefault(q['id'],q)
    v2=read(CONTENT/'_shared/PYQ-Explanations-v2.json') if (CONTENT/'_shared/PYQ-Explanations-v2.json').is_file() else {}
    for qid,x in (v2.get('questions',{}) if isinstance(v2,dict) else {}).items():
        q=result.get(qid)
        if not q or not x.get('lead'):continue
        lines=[x['lead']]+list(x.get('points') or [])+(['Also remember: '+x['also']] if x.get('also') else [])
        q['_en']='\n'.join(lines);q['_te']='';q['_v2']=True;q['explain_table']=x.get('table')
        t=x.get('te') or {}
        if t.get('lead'):q['_te']='\n'.join([t['lead']]+list(t.get('points') or [])+(['ఇది కూడా గుర్తుంచుకోండి: '+t['also']] if t.get('also') else []));q['explain_table_te']=t.get('table')
        if x.get('better_answer') in (1,2,3,4) and x['better_answer']!=q.get('_answer'):q['_better']=x['better_answer'];q['key_status']='disputed';q.setdefault('official_key',q.get('_answer'))
    for q in result.values():
        q['_orig_scored']=q['_scored'];q['_scored']=q['_answer'] in (1,2,3,4)
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

def maps_for_chapter(chapter_id):
    """A map belongs to the chapter that holds most of its linked questions."""
    import collections
    corpus=records();out=[]
    for m in catalog().values():
        c=collections.Counter((corpus.get(l['item_id']) or {}).get('_chapter') for l in m['links'] if (corpus.get(l['item_id']) or {}).get('_kind') in ('bank','pyq','primary_pyq'))
        if c and c.most_common(1)[0][0]==chapter_id:out.append(m)
    return out

@bp.app_context_processor
def map_context():
    return {'unit6_maps_for':maps_for,'unit6_maps_for_chapter':maps_for_chapter}

KIND_GROUPS=(('pyq','Previous year questions / గత ప్రశ్నలు',('pyq','primary_pyq')),('bank','Practice MCQs / సాధన ప్రశ్నలు',('bank',)))

def map_lang():
    lang=request.args.get('qlang','te')
    return lang if lang in ('te','en','both') else 'te'

@bp.get('/maps')
def index():
    return render_template('ds/polity_maps.html',maps=list(catalog().values()),lang=map_lang())

@bp.get('/maps/<map_id>')
def page(map_id):
    m=catalog().get(map_id)
    if not m:abort(404)
    html=(MAPS/m['file']).read_text(encoding='utf-8')
    lang=map_lang()
    count=len([1 for l in m['links'] if (records().get(l['item_id']) or {}).get('_kind') in ('bank','pyq','primary_pyq')])
    bar=render_template('ds/polity_map_bar.html',map=m,lang=lang,count=count)
    html=re.sub(r'<nav style="padding:1rem;overflow-wrap:anywhere"><a href="[^"]*/questions">Linked questions[^<]*</a></nav>','',html,count=1)
    html=re.sub(r'(Linked questions: )\d+',lambda x:x.group(1)+str(count),html)
    html=re.sub(r'(సంబంధిత ప్రశ్నలు: )\d+',lambda x:x.group(1)+str(count),html)
    html=re.sub(r'(<body\b[^>]*>)',lambda x:x.group(1)+bar,html,count=1,flags=re.I)
    resp=make_response(html);resp.headers['Content-Type']='text/html; charset=utf-8'
    return resp

@bp.get('/maps/<map_id>/questions')
def linked_questions(map_id):
    m=catalog().get(map_id)
    if not m:abort(404)
    corpus=records();groups=[]
    for link in m['links']:
        if link['item_id'] not in corpus:abort(500,description='Unresolved map link')
    for kind,label,kinds in KIND_GROUPS:
        rows=[(corpus[l['item_id']],l) for l in m['links'] if corpus[l['item_id']]['_kind'] in kinds]
        rows.sort(key=lambda r:0 if r[1].get('strength')=='DIRECT' else 1)
        if rows:groups.append((kind,label,rows))
    total=sum(len(g[2]) for g in groups)
    return render_template('ds/polity_maps.html',map=m,groups=groups,total=total,lang=map_lang())

@bp.get('/questions/<item_id>')
def question(item_id):
    q=records().get(item_id)
    if not q:abort(404)
    return redirect(url_for('polity_unit6.practice',item_id=item_id))
