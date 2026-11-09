"""Complete Unit 6 learner entry point backed by immutable authored records."""
import os,random,uuid
from datetime import datetime,timedelta
from flask import Blueprint,abort,current_app,redirect,render_template,request,url_for,make_response
from ..db import db
from ..polity_models import PolityUnit6State,PolityUnit6Progress,PolityUnit6Exam
from ..services.device import device_id
from .polity_maps import CONTENT,read,records,catalog
from ..services.polity_sections import section_links,directory
import re as _re
_JARGON=_re.compile(r'(fact register|bank key|authenticated pairing|tests separately|untested|source[- ]bank|content team|GBK paragraph|Laxmikanth paragraph)',_re.I)
_IDS=_re.compile(r'\s*[\(\[]?\b(?:POL|APPSC|BK|GBK\d*|PYQ)-[A-Za-z0-9._-]+\b[\)\]]?')
def clean_text(t):
    if not t:return t
    t=_IDS.sub('',t)
    parts=_re.split(r'(?<=[.!?।])\s+',t)
    kept=[x for x in parts if not _JARGON.search(x)]
    return ' '.join(kept) if kept else t

bp=Blueprint('polity_unit6',__name__,url_prefix='/learn/polity/unit6')
@bp.app_template_filter('clean_expl')
def _clean_expl(t):return clean_text(t)

def enabled():return current_app.config.get('POLITY_UNIT6_ENABLED',os.environ.get('POLITY_UNIT6_ENABLED','0')=='1')
@bp.before_request
def availability():
    if not enabled():abort(404)

def chapters():
    return [c for u in read(CONTENT/'MASTER-INDEX.json')['units'] if u['unit']==6 for s in u['sections'] for c in s['chapters']]
def chapter_or_404(cid):
    return next((c for c in chapters() if c['id']==cid),None) or abort(404)
VISIBLE_KINDS=('bank','pyq','primary_pyq')
def visible(q):return q['_kind'] in VISIBLE_KINDS
def scoreable(q):
    return q['_scored'] and q['_answer'] in (1,2,3,4) and q.get('key_status') not in ('disputed','no_official_key','needs_user_decision')
def state_for(item_id):
    key=(device_id(),item_id);state=db.session.get(PolityUnit6State,key)
    if state is None:
        state=PolityUnit6State(device_id=key[0],item_id=item_id,saved=False,seen_count=0,wrong_count=0);db.session.add(state)
    return state
def test_records(cid):
    chapter_or_404(cid);p=CONTENT/'.'.join(cid.split('.')[:2])/cid/'Chapter-Test.json'
    if not p.is_file():return []
    d=read(p);ids=[q['id'] for q in d.get('questions',[])]+d.get('question_ids',[])
    corpus=records();return [corpus[i] for i in dict.fromkeys(ids) if i in corpus]

@bp.get('/')
def home():
    units=read(CONTENT/'MASTER-INDEX.json')['units']
    return render_template('ds/polity_subject.html',units=units)

@bp.get('/unit')
def unit():
    corpus=records();rows=[]
    progress={p.chapter_id:p for p in PolityUnit6Progress.query.filter_by(device_id=device_id())}
    for c in chapters():
        own=[q for q in corpus.values() if q['_chapter']==c['id'] and visible(q)]
        rows.append(dict(chapter=c,total=len(own),unscored=sum(not q['_scored'] for q in own),completed=bool(progress.get(c['id']) and progress[c['id']].completed)))
    return render_template('ds/polity_browse.html',mode='unit',rows=rows)

@bp.get('/chapters/<chapter_id>')
def chapter(chapter_id):
    c=chapter_or_404(chapter_id)
    own=[q for q in records().values() if q['_chapter']==chapter_id and visible(q)]
    progress=db.session.get(PolityUnit6Progress,(device_id(),chapter_id))
    return render_template('ds/polity_browse.html',mode='chapter',chapter=c,total=len(own),unscored=sum(not q['_scored'] for q in own),progress=progress)

def filters(default_chapter=''):
    values={k:request.args.get(k,'').strip() for k in ('chapter','kind','q','view','map')}
    if values['map'] and values['map'] not in catalog():abort(404)
    if not any(k in request.args for k in values):values['chapter']=default_chapter
    if values['chapter']:chapter_or_404(values['chapter'])
    return values

def selection(values):
    chapter,kind,query,view=(values[k] for k in ('chapter','kind','q','view'))
    if values.get('map'):
        corpus=records();qs=[corpus[l['item_id']] for l in catalog()[values['map']]['links'] if l['item_id'] in corpus and visible(corpus[l['item_id']])]
        return list({q['id']:q for q in qs}.values())
    qs=test_records(chapter) if kind=='chaptertest' and chapter else list(records().values())
    if chapter:qs=[q for q in qs if q['_chapter']==chapter]
    if kind and kind!='chaptertest':qs=[q for q in qs if q['_kind']==kind or kind=='pyq' and q['_kind']=='primary_pyq']
    if kind=='chaptertest' and not chapter:qs=[q for c in chapters() for q in test_records(c['id'])]
    if kind!='chaptertest':qs=[q for q in qs if visible(q)]
    if query:qs=[q for q in qs if query.casefold() in (q.get('question_en','')+' '+q.get('question_te','')+' '+q['id']).casefold()]
    if view in ('saved','mistakes'):
        states=PolityUnit6State.query.filter_by(device_id=device_id()).all()
        ids={s.item_id for s in states if s.saved} if view=='saved' else {s.item_id for s in states if s.wrong_count>0}
        qs=[q for q in qs if q['id'] in ids]
    return list({q['id']:q for q in qs}.values())

def language():
    lang=request.args.get('qlang','te')
    if lang not in ('te','en','both'):abort(400)
    return lang

@bp.get('/library')
def library():
    values=filters();qs=selection(values)
    page=max(1,request.args.get('page',1,type=int));total=len(qs)
    return render_template('ds/polity_browse.html',mode='library',questions=qs[(page-1)*40:page*40],total=total,page=page,filters=values,lang=language(),start=qs[0]['id'] if qs else None)

def question_page(q,choice=None,review=False,qs=None):
    values=filters(q['_chapter']);qs=selection(values) if qs is None else qs
    pos=next((i for i,r in enumerate(qs) if r['id']==q['id']),None)
    # A bookmarked question may disappear from the filter after an action; keep it
    # visible without silently switching to the full bank.
    if pos is None:qs=[q];pos=0
    lang=language();feedback=None
    if review:feedback=('correct' if choice==q['_answer'] else 'incorrect') if scoreable(q) else 'unscored'
    context={**values,'qlang':lang}
    review_args={'review':'1','choice':choice} if review and choice in (1,2,3,4) else {}
    notes=url_for('.notes',chapter_id=q['_chapter'],item_id=q['id'],**context,**review_args)
    locators=section_links(q)
    links=[dict(url=notes+'#'+l['anchor'],basis=l['basis']) for l in locators]
    if not links:links=[dict(url=notes+'#question-explanation',basis='explanation')]
    return render_template('ds/polity_question.html',question=q,choice=choice,feedback=feedback,lang=lang,context=context,
        state=db.session.get(PolityUnit6State,(device_id(),q['id'])),position=pos+1,total=len(qs),
        previous=qs[pos-1]['id'] if pos else None,following=qs[pos+1]['id'] if pos+1<len(qs) else None,
        notes_url=notes,section_links=links,review_args=review_args)

@bp.get('/chapters/<chapter_id>/notes')
def notes(chapter_id):
    chapter_or_404(chapter_id);item_id=request.args.get('item_id');q=records().get(item_id) if item_id else None
    if item_id and (not q or q['_chapter']!=chapter_id):abort(404)
    content=(directory(chapter_id)/'Notes.html').read_text(encoding='utf-8-sig')
    back=url_for('.chapter',chapter_id=chapter_id)
    target=None
    if q:
        args={**filters(chapter_id),'qlang':language()}
        choice=request.args.get('choice',type=int)
        if request.args.get('review')=='1' and choice in (1,2,3,4):args.update(review='1',choice=choice)
        target=url_for('.practice',item_id=q['id'],**args)+'#answer-result'
    toolbar=render_template('ds/polity_note_toolbar.html',chapter_url=back,question_url=target)
    import re
    content=re.sub(r'(<body\b[^>]*>)',lambda m:m.group(1)+toolbar,content,count=1,flags=re.I)
    if q and not section_links(q):
        appendix=render_template('ds/polity_note_explanation.html',question=q,lang=language())
        content=re.sub(r'</body>',lambda m:appendix+m.group(0),content,count=1,flags=re.I)
    response=make_response(content);response.headers['Content-Type']='text/html; charset=utf-8'
    return response

@bp.get('/practice/<item_id>')
def practice(item_id):
    q=records().get(item_id)
    if q is None:
        alias=next((r.get('canonical_question_id') for r in read(CONTENT/'_shared/Expected-Questions.json') if r['id']==item_id),None)
        if alias in records():return redirect(url_for('.practice',item_id=alias))
        abort(404)
    choice=request.args.get('choice',type=int)
    return question_page(q,choice,request.args.get('review')=='1' and choice in (1,2,3,4))

@bp.post('/practice/<item_id>')
def answer(item_id):
    q=records().get(item_id) or abort(404);state=state_for(item_id)
    if request.form.get('action')=='bookmark':
        state.saved=not state.saved;db.session.commit()
        args={**filters(q['_chapter']),'qlang':language()}
        choice=request.args.get('choice',type=int)
        if request.args.get('review')=='1' and choice in (1,2,3,4):args.update(review='1',choice=choice)
        return redirect(url_for('.practice',item_id=item_id,**args))
    selected=request.form.get('answer',type=int)
    if selected not in (1,2,3,4):abort(400)
    qs=selection(filters(q['_chapter']))
    state.seen_count+=1;state.last_seen_at=datetime.utcnow()
    feedback='unscored'
    if scoreable(q):
        feedback='correct' if selected==q['_answer'] else 'incorrect'
        if feedback=='incorrect':state.wrong_count+=1
        else:state.wrong_count=0
    db.session.commit()
    return question_page(q,selected,True,qs)

@bp.post('/progress/<chapter_id>')
def progress(chapter_id):
    chapter_or_404(chapter_id);key=(device_id(),chapter_id)
    p=db.session.get(PolityUnit6Progress,key)
    if p is None:p=PolityUnit6Progress(device_id=key[0],chapter_id=chapter_id);db.session.add(p)
    p.completed=request.form.get('completed')=='1';p.updated_at=datetime.utcnow();db.session.commit()
    return redirect(url_for('.chapter',chapter_id=chapter_id))

@bp.post('/tests')
def start_test():
    cid=request.form.get('chapter','');chapter_mode=request.form.get('kind')=='chaptertest'
    if cid:chapter_or_404(cid)
    qs=test_records(cid) if chapter_mode and cid else [q for q in records().values() if visible(q) and (not cid or q['_chapter']==cid)]
    qs=[q for q in qs if scoreable(q)]
    count=min(100,max(1,request.form.get('count',25,type=int)));minutes=min(180,max(1,request.form.get('minutes',30,type=int)))
    if not chapter_mode:random.SystemRandom().shuffle(qs)
    qs=qs[:count]
    if not qs:abort(400,description='No scored questions available for this selection.')
    now=datetime.utcnow();exam=PolityUnit6Exam(id=str(uuid.uuid4()),device_id=device_id(),questions=qs,answers={},started_at=now,deadline=now+timedelta(minutes=minutes))
    db.session.add(exam);db.session.commit();return redirect(url_for('.exam',exam_id=exam.id))

@bp.route('/tests/<exam_id>',methods=['GET','POST'])
def exam(exam_id):
    e=PolityUnit6Exam.query.filter_by(id=exam_id,device_id=device_id()).with_for_update().first_or_404()
    now=datetime.utcnow()
    if not e.submitted_at and (request.method=='POST' or now>=e.deadline):
        answers=dict(e.answers or {})
        # Never accept answers received after the server deadline.
        if now<e.deadline:
            for q in e.questions:
                a=request.form.get(q['id'],type=int)
                if a in (1,2,3,4):answers[q['id']]=a
        e.answers=answers;e.score=sum(answers.get(q['id'])==q['_answer'] for q in e.questions);e.submitted_at=now
        for q in e.questions:
            if q['id'] not in answers:continue
            s=state_for(q['id']);s.seen_count+=1;s.last_seen_at=now
            if answers[q['id']]!=q['_answer']:s.wrong_count+=1
            else:s.wrong_count=0
        db.session.commit()
    return render_template('ds/polity_unit6.html',mode='exam',exam=e,seconds=max(0,int((e.deadline-now).total_seconds())))

@bp.post('/tests/<exam_id>/save')
def save_exam_answer(exam_id):
    e=PolityUnit6Exam.query.filter_by(id=exam_id,device_id=device_id()).with_for_update().first_or_404()
    if e.submitted_at or datetime.utcnow()>=e.deadline:abort(409)
    item_id=request.form.get('item_id');answer=request.form.get('answer',type=int)
    if item_id not in {q['id'] for q in e.questions} or answer not in (1,2,3,4):abort(400)
    e.answers={**(e.answers or {}),item_id:answer};db.session.commit()
    return {'saved':True}
