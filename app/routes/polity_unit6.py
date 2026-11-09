"""Complete Unit 6 learner entry point backed by immutable authored records."""
import os,random,uuid
from datetime import datetime,timedelta
from flask import Blueprint,abort,current_app,redirect,render_template,request,url_for
from ..db import db
from ..polity_models import PolityUnit6State,PolityUnit6Progress,PolityUnit6Exam
from ..services.device import device_id
from .polity_maps import CONTENT,read,records
bp=Blueprint('polity_unit6',__name__,url_prefix='/learn/polity/unit6')

def enabled():return current_app.config.get('POLITY_UNIT6_ENABLED',os.environ.get('POLITY_UNIT6_ENABLED','0')=='1')
@bp.before_request
def availability():
    if not enabled():abort(404)

def chapters():
    return [c for u in read(CONTENT/'MASTER-INDEX.json')['units'] if u['unit']==6 for s in u['sections'] for c in s['chapters']]
def chapter_or_404(cid):
    return next((c for c in chapters() if c['id']==cid),None) or abort(404)
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
    corpus=records();rows=[]
    progress={p.chapter_id:p for p in PolityUnit6Progress.query.filter_by(device_id=device_id())}
    for c in chapters():
        own=[q for q in corpus.values() if q['_chapter']==c['id']]
        rows.append(dict(chapter=c,total=len(own),unscored=sum(not q['_scored'] for q in own),completed=bool(progress.get(c['id']) and progress[c['id']].completed)))
    return render_template('ds/polity_unit6.html',mode='home',rows=rows)

@bp.get('/library')
def library():
    chapter=request.args.get('chapter','');kind=request.args.get('kind','');query=request.args.get('q','').strip().casefold();view=request.args.get('view','')
    if chapter:chapter_or_404(chapter)
    qs=test_records(chapter) if kind=='chaptertest' and chapter else list(records().values())
    if chapter:qs=[q for q in qs if q['_chapter']==chapter]
    if kind and kind!='chaptertest':qs=[q for q in qs if q['_kind']==kind or kind=='pyq' and q['_kind']=='primary_pyq']
    if kind=='chaptertest' and not chapter:qs=[q for c in chapters() for q in test_records(c['id'])]
    if query:qs=[q for q in qs if query in (q.get('question_en','')+' '+q.get('question_te','')+' '+q['id']).casefold()]
    if view in ('saved','mistakes'):
        states=PolityUnit6State.query.filter_by(device_id=device_id()).all()
        ids={s.item_id for s in states if s.saved} if view=='saved' else {s.item_id for s in states if s.wrong_count>0}
        qs=[q for q in qs if q['id'] in ids]
    page=max(1,request.args.get('page',1,type=int));total=len(qs)
    return render_template('ds/polity_unit6.html',mode='library',questions=qs[(page-1)*40:page*40],total=total,page=page,chapter=chapter,kind=kind,query=request.args.get('q',''),view=view)

@bp.get('/practice/<item_id>')
def practice(item_id):
    q=records().get(item_id)
    if q is None:
        alias=next((r.get('canonical_question_id') for r in read(CONTENT/'_shared/Expected-Questions.json') if r['id']==item_id),None)
        if alias in records():return redirect(url_for('.practice',item_id=alias))
        abort(404)
    state=db.session.get(PolityUnit6State,(device_id(),item_id))
    return render_template('ds/polity_unit6.html',mode='question',question=q,state=state,feedback=None)

@bp.post('/practice/<item_id>')
def answer(item_id):
    q=records().get(item_id) or abort(404);state=state_for(item_id)
    if request.form.get('action')=='bookmark':
        state.saved=not state.saved;db.session.commit();return redirect(url_for('.practice',item_id=item_id))
    selected=request.form.get('answer',type=int)
    if selected not in (1,2,3,4):abort(400)
    state.seen_count+=1;state.last_seen_at=datetime.utcnow()
    feedback='unscored'
    if scoreable(q):
        feedback='correct' if selected==q['_answer'] else 'incorrect'
        if feedback=='incorrect':state.wrong_count+=1
        else:state.wrong_count=0
    db.session.commit()
    return render_template('ds/polity_unit6.html',mode='question',question=q,state=state,feedback=feedback)

@bp.post('/progress/<chapter_id>')
def progress(chapter_id):
    chapter_or_404(chapter_id);key=(device_id(),chapter_id)
    p=db.session.get(PolityUnit6Progress,key)
    if p is None:p=PolityUnit6Progress(device_id=key[0],chapter_id=chapter_id);db.session.add(p)
    p.completed=request.form.get('completed')=='1';p.updated_at=datetime.utcnow();db.session.commit()
    return redirect(url_for('.home'))

@bp.post('/tests')
def start_test():
    cid=request.form.get('chapter','');chapter_mode=request.form.get('kind')=='chaptertest'
    if cid:chapter_or_404(cid)
    qs=test_records(cid) if chapter_mode and cid else [q for q in records().values() if not cid or q['_chapter']==cid]
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
