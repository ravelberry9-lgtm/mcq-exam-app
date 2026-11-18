"""Group 2 Geography in Polity's design: hub, lesson page, practice setup, library, bookmarks/mistakes,
quick revision and timed tests. Reuses Polity's tables (no schema change): PolityUnit6State (seen /
bookmark / mistakes), PolityUnit6Progress (chapter_id 'g2-<n>') and PolityUnit6Exam (timed tests)."""
import random
import uuid
from datetime import datetime, timedelta
from flask import abort, redirect, render_template, request, session, url_for
from .geography import bp
from ..db import db
from ..services import geo_g2 as g2
from ..services.device import device_id

EXAM_GROUPS=[('upsc','UPSC'),('g2','APPSC Group 2'),('g1','APPSC Group 1'),('tspsc','TSPSC / TGPSC'),('appsc','APPSC other'),('other','Other')]
VIEWS={'unseen':'చూడనివి మాత్రమే · Only unseen','mistakes':'తప్పులు మాత్రమే · Only mistakes','saved':'గుర్తుపెట్టినవి మాత్రమే · Only bookmarked'}
FILTER_KEYS=('kind','ls','sec','exam','y1','y2','view','q')
LANGS=('te','en','both')

def _models():
    from ..polity_models import PolityUnit6State,PolityUnit6Progress,PolityUnit6Exam
    return PolityUnit6State,PolityUnit6Progress,PolityUnit6Exam
def lang():
    l=request.args.get('qlang','te')
    if l not in LANGS:abort(400)
    return l
def states():
    S,_,_=_models()
    try:return {s.item_id:s for s in S.query.filter_by(device_id=device_id()).all()}
    except Exception:db.session.rollback();return {}
def progress_map():
    _,P,_=_models()
    try:return {p.chapter_id:p.completed for p in P.query.filter_by(device_id=device_id()).all() if p.chapter_id.startswith('g2-')}
    except Exception:db.session.rollback();return {}

# ---- filters (shared by practice setup, library, question run, revise) ----
def _lessons_arg(raw):
    out=[]
    for x in (raw or '').replace(' ','').split(','):
        if not x:continue
        if not x.isdigit() or not g2.chapter(int(x)):abort(404)
        out.append(int(x))
    return sorted(set(out))
def filters(args=None):
    a=request.args if args is None else args
    v={k:(a.get(k) or '').strip() for k in FILTER_KEYS}
    if v['kind'] not in ('','pyq','bank'):abort(404)
    if v['exam'] and v['exam'] not in dict(EXAM_GROUPS):abort(404)
    if v['view'] and v['view'] not in VIEWS:abort(404)
    for y in ('y1','y2'):
        if v[y] and not (v[y].isdigit() and len(v[y])==4):abort(404)
    _lessons_arg(v['ls'])
    if v['sec'] and len(_lessons_arg(v['ls']))!=1:v['sec']=''
    if v['kind']=='bank':v.update(exam='',y1='',y2='')
    return v
def active(v):return {k:x for k,x in v.items() if x}
def selection(v,st=None,ignore_view=False):
    qs=g2.records();ls=_lessons_arg(v.get('ls'))
    if ls:qs=[q for q in qs if q['_lesson'] in ls]
    if v.get('sec'):qs=[q for q in qs if q.get('section')==v['sec']]
    if v.get('kind'):qs=[q for q in qs if q['_kind']==v['kind']]
    if v.get('exam'):qs=[q for q in qs if q['_exam']==v['exam']]
    if v.get('y1'):qs=[q for q in qs if q['_kind']=='pyq' and (q['_year'] or 0)>=int(v['y1'])]
    if v.get('y2'):qs=[q for q in qs if q['_kind']=='pyq' and q['_year'] and q['_year']<=int(v['y2'])]
    if v.get('q'):
        t=v['q'].casefold();qs=[q for q in qs if t in ((q.get('question_en') or '')+' '+(q.get('question_te') or '')+' '+q['id']).casefold()]
    if v.get('view') and not ignore_view:
        st=states() if st is None else st
        if v['view']=='saved':qs=[q for q in qs if q['id'] in st and st[q['id']].saved]
        elif v['view']=='mistakes':qs=[q for q in qs if q['id'] in st and st[q['id']].wrong_count>0]
        else:qs=[q for q in qs if not (q['id'] in st and st[q['id']].seen_count)]
    return qs
def qurl(q,v,**extra):
    return url_for('geography.g2_question',number=q['_lesson'],qid=q['id'],**active(v),**extra)

@bp.app_template_global('g2_pyq_label')
def _label(q):return g2.pyq_label(q if '_kind' in q else g2.by_id().get(q['id'],q))

# ---- 1. hub ----
@bp.get('/g2')
def g2_index():
    st=states();prog=progress_map();recs=g2.records()
    rows={}
    for c in g2.index()['chapters']:
        n=c['display_chapter'];own=g2.lesson_records(n)
        rows[n]=dict(ch=c,mcq=sum(q['_kind']=='bank' for q in own),pyq=sum(q['_kind']=='pyq' for q in own),total=len(own),
                     seen=sum(1 for q in own if q['id'] in st and st[q['id']].seen_count),done=bool(prog.get('g2-%d'%n)),
                     images=len(g2.images(n).get('images',{})))
    totals=dict(lessons=len(rows),mcq=sum(q['_kind']=='bank' for q in recs),pyq=sum(q['_kind']=='pyq' for q in recs),
                images=sum(r['images'] for r in rows.values()),done=sum(r['done'] for r in rows.values()),
                saved=sum(1 for s in st.values() if s.saved and s.item_id in g2.by_id()),
                wrong=sum(1 for s in st.values() if s.wrong_count and s.item_id in g2.by_id()))
    return render_template('ds/g2_geography.html',data=g2.index(),rows=rows,groups=g2.GROUPS,totals=totals)

# ---- 2. lesson ----
@bp.get('/g2/<int:number>')
def g2_chapter(number):
    ch=g2.chapter(number) or abort(404);own=g2.lesson_records(number);st=states()
    _,P,_=_models()
    try:p=db.session.get(P,(device_id(),'g2-%d'%number))
    except Exception:db.session.rollback();p=None
    return render_template('ds/g2_chapter.html',ch=ch,number=number,mcq=sum(q['_kind']=='bank' for q in own),pyq=sum(q['_kind']=='pyq' for q in own),
        total=len(own),seen=sum(1 for q in own if q['id'] in st and st[q['id']].seen_count),images=len(g2.images(number).get('images',{})),
        done=bool(p and p.completed),has_notes=g2.notes_path(number).is_file(),sections=g2.lesson_sections(number),
        prev_ch=g2.chapter(number-1),next_ch=g2.chapter(number+1))

@bp.post('/g2/<int:number>/progress')
def g2_progress(number):
    g2.chapter(number) or abort(404);_,P,_=_models();key=(device_id(),'g2-%d'%number)
    p=db.session.get(P,key)
    if p is None:p=P(device_id=key[0],chapter_id=key[1]);db.session.add(p)
    p.completed=request.form.get('completed')=='1';p.updated_at=datetime.utcnow();db.session.commit()
    return redirect(url_for('geography.g2_chapter',number=number))

@bp.get('/g2/<int:number>/infographics')
def g2_infographics(number):
    ch=g2.chapter(number) or abort(404);il=request.args.get('ilang','te')
    if il not in ('te','en'):abort(400)
    return render_template('ds/g2_infographics.html',ch=ch,number=number,images=g2.lesson_images(number),il=il)

# ---- 3. practice setup ----
@bp.get('/g2/practice')
def g2_practice_setup():
    v=filters();l=lang();st=states();qs=selection(v,st)
    allq=g2.records();ls=_lessons_arg(v['ls'])
    base=selection({**v,'ls':'','sec':''},st)
    lesson_counts={c['display_chapter']:0 for c in g2.index()['chapters']}
    for q in base:lesson_counts[q['_lesson']]+=1
    pyqs=[q for q in allq if q['_kind']=='pyq']
    years=sorted({q['_year'] for q in pyqs if q['_year']})
    secs=g2.lesson_sections(ls[0]) if len(ls)==1 else []
    sec_counts={}
    if secs:
        for q in selection({**v,'sec':''},st):sec_counts[q.get('section') or '']=sec_counts.get(q.get('section') or '',0)+1
    return render_template('ds/g2_practice_setup.html',v=v,lang=l,count=len(qs),start=qurl(qs[0],v,qlang=l,fresh='1') if qs else None,
        groups=EXAM_GROUPS,exam_counts={g:sum(1 for q in pyqs if q['_exam']==g) for g,_ in EXAM_GROUPS},years=years,
        lessons=[(c,lesson_counts[c['display_chapter']]) for c in g2.index()['chapters']],ls=ls,secs=secs,sec_counts=sec_counts,
        views=VIEWS,totals={'pyq':len(pyqs),'bank':len(allq)-len(pyqs)},list_url=url_for('geography.g2_library',**active(v),qlang=l))

# ---- 4/5. library, bookmarks, mistakes ----
def _library(view_title=None,force_view=None):
    v=filters()
    if force_view:v['view']=force_view
    l=lang();qs=selection(v);page=max(1,request.args.get('page',1,type=int));total=len(qs)
    rows=qs[(page-1)*40:page*40]
    return render_template('ds/g2_library.html',v=v,lang=l,questions=rows,total=total,page=page,pages=(total+39)//40,
        start=qurl(qs[0],v,qlang=l,fresh='1') if qs else None,qurl=qurl,view_title=view_title,force_view=force_view,
        lessons=g2.index()['chapters'],endpoint=request.endpoint,
        fa={k:x for k,x in active(v).items() if not (force_view and k=='view')},setup_args=active(v))
@bp.get('/g2/library')
def g2_library():return _library()
@bp.get('/g2/bookmarks')
def g2_bookmarks():return _library('గుర్తుపెట్టినవి · Bookmarks','saved')
@bp.get('/g2/mistakes')
def g2_mistakes():return _library('తప్పులు · Mistakes','mistakes')

# ---- 6. quick revision (Polity's revise page + polity_revise.js; sections load lazily) ----
REV_KINDS={'pyq':'PYQs','bank':'MCQs','both':'PYQs + MCQs'}
def _rev_kind():
    k=request.args.get('kind','both');return k if k in REV_KINDS else 'both'
def _rev_sections(n,kind):
    out=[];start=1
    for sid,title,_ in g2.lesson_sections(n):
        ids=[q for q in g2.lesson_records(n) if (q.get('section') or '')==sid and (kind=='both' or q['_kind']==kind)]
        if ids:out.append(dict(key='s-'+(sid or 'other'),sid=sid,title=title,qs=ids,count=len(ids),start=start));start+=len(ids)
    return out,start-1
@bp.get('/g2/revise')
def g2_revise():
    n=request.args.get('lesson',1,type=int);ch=g2.chapter(n) or abort(404);kind=_rev_kind();l=lang()
    secs,total=_rev_sections(n,kind)
    return render_template('ds/g2_revise.html',ch=ch,number=n,kind=kind,kinds=REV_KINDS,lang=l,chapters=secs,total=total,
        lessons=g2.index()['chapters'],open_ch=request.args.get('ch',''))
@bp.get('/g2/revise/<int:n>/part')
def g2_revise_part(n):
    g2.chapter(n) or abort(404);kind=_rev_kind();l=lang()
    secs,_=_rev_sections(n,kind);c=next((x for x in secs if x['key']==request.args.get('ch')),None) or abort(404)
    back=url_for('geography.g2_revise',lesson=n,kind=kind,qlang=l,ch=c['key'])
    return render_template('ds/g2_revise_part.html',c=c,lang=l,number=n,back=back)

# ---- 7. timed test ----
@bp.get('/g2/tests')
def g2_test_setup():
    return render_template('ds/g2_test_setup.html',lessons=g2.index()['chapters'],lang=lang(),
        counts={c['display_chapter']:len(g2.lesson_records(c['display_chapter'])) for c in g2.index()['chapters']})
def _snap(q):
    keep=('id','question_te','question_en','options_te','options_en','answer','section','explanation_te','explanation_en','_lesson','_kind')
    return {**{k:q.get(k) for k in keep},'_answer':q['answer'],'_g2':True,'_chapter':'g2-%d'%q['_lesson']}
@bp.post('/g2/tests')
def g2_start_test():
    ls=_lessons_arg(','.join(request.form.getlist('ls')) or request.form.get('lsc',''))
    kind=request.form.get('kind','')
    if kind not in ('','pyq','bank'):abort(400)
    qs=selection({'ls':','.join(map(str,ls)),'kind':kind})
    count=min(100,max(1,request.form.get('count',25,type=int)));minutes=min(180,max(1,request.form.get('minutes',30,type=int)))
    qs=list(qs);random.SystemRandom().shuffle(qs);qs=qs[:count]
    if not qs:abort(400,description='No questions for this selection.')
    _,_,E=_models();now=datetime.utcnow()
    e=E(id=str(uuid.uuid4()),device_id=device_id(),questions=[_snap(q) for q in qs],answers={},started_at=now,deadline=now+timedelta(minutes=minutes))
    db.session.add(e);db.session.commit()
    return redirect(url_for('geography.g2_test',exam_id=e.id,qlang=lang()))
@bp.route('/g2/tests/<exam_id>',methods=['GET','POST'])
def g2_test(exam_id):
    S,_,E=_models()
    e=E.query.filter_by(id=exam_id,device_id=device_id()).first_or_404()
    if not all(q.get('_g2') for q in e.questions):abort(404)
    now=datetime.utcnow()
    if not e.submitted_at and (request.method=='POST' or now>=e.deadline):
        answers=dict(e.answers or {})
        if now<e.deadline:
            for q in e.questions:
                a=request.form.get(q['id'],type=int)
                if a in (1,2,3,4):answers[q['id']]=a
        e.answers=answers;e.score=sum(answers.get(q['id'])==q['_answer'] for q in e.questions);e.submitted_at=now
        for q in e.questions:
            if q['id'] not in answers:continue
            key=(device_id(),q['id']);s=db.session.get(S,key)
            if s is None:s=S(device_id=key[0],item_id=q['id'],saved=False,seen_count=0,wrong_count=0);db.session.add(s)
            s.seen_count+=1;s.last_seen_at=now;s.wrong_count=0 if answers[q['id']]==q['_answer'] else s.wrong_count+1
        db.session.commit()
        if request.method=='POST':return redirect(url_for('geography.g2_test',exam_id=e.id,qlang=lang()))
    from .geography_g2 import _view
    def full(i):
        q=g2.by_id().get(i);return _view(q) if q else None
    return render_template('ds/g2_test.html',exam=e,lang=lang(),full=full,seconds=max(0,int((e.deadline-now).total_seconds())))
@bp.post('/g2/tests/<exam_id>/save')
def g2_test_save(exam_id):
    _,_,E=_models()
    e=E.query.filter_by(id=exam_id,device_id=device_id()).first_or_404()
    if e.submitted_at or datetime.utcnow()>=e.deadline:abort(409)
    item=request.form.get('item_id');a=request.form.get('answer',type=int)
    if item not in {q['id'] for q in e.questions} or a not in (1,2,3,4):abort(400)
    e.answers={**(e.answers or {}),item:a};db.session.commit()
    return {'saved':True}

# ---- practice run (filtered set across lessons) score ----
@bp.get('/g2/run/result')
def g2_run_result():
    from .geography_g2 import _run
    v=filters();l=lang();r=_run('run');recs=g2.by_id()
    if request.args.get('reset')=='1':
        allr=dict(session.get('g2run') or {});allr.pop('run',None);session['g2run']=allr
        return redirect(url_for('geography.g2_practice_setup',**active(v),qlang=l))
    wrong=[recs[i] for i in r['wrong'] if i in recs]
    return render_template('ds/g2_result.html',number=None,ch=None,run=r,wrong=wrong,lang=l,v=v,va=active(v),qurl=qurl)
