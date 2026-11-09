"""Admin tools for Unit 6 (uses the existing /admin PIN login). Edits are stored as database overrides; content files are never modified."""
import csv,io,json
from datetime import datetime
from flask import Blueprint,Response,abort,flash,redirect,render_template,request,url_for
from ..db import db
from ..polity_models import PolityUnit6Override,PolityUnit6Submission
from .admin import _is_authed
from .polity_maps import base_records,records,overrides,ensure_admin_tables
from .polity_unit6 import chapters,enabled,chapter_or_404

bp=Blueprint('polity_admin',__name__,url_prefix='/learn/polity/unit6/admin')

@bp.before_request
def guard():
    if not enabled():abort(404)
    if not _is_authed():return redirect(url_for('admin.login',next=request.path))
    ensure_admin_tables()

def _clean(v,limit=2000):
    return (v or '').replace('\r\n','\n').strip()[:limit]

@bp.get('/')
def home():
    chapter=request.args.get('chapter','');q=_clean(request.args.get('q'),100).lower();show=request.args.get('show','')
    page=max(1,request.args.get('page',1,type=int))
    ov=overrides();base=base_records()
    rows=[]
    for r in base.values():
        if r['_kind'] not in ('bank','pyq','primary_pyq'):continue
        if chapter and r['_chapter']!=chapter:continue
        o=ov.get(r['id'])
        if show=='deleted' and not (o and o.deleted):continue
        if show=='edited' and not (o and not o.deleted):continue
        if not show and o and o.deleted:continue
        if q and q not in (r['id']+' '+(r.get('question_en') or '')+' '+(r.get('question_te') or '')).lower():continue
        rows.append(dict(id=r['id'],chapter=r['_chapter'],kind=r['_kind'],text=(r.get('question_en') or r.get('question_te') or '')[:140],deleted=bool(o and o.deleted),edited=bool(o and not o.deleted)))
    total=len(rows)
    subs=PolityUnit6Submission.query.order_by(PolityUnit6Submission.id.desc()).all()
    return render_template('ds/polity_admin.html',rows=rows[(page-1)*30:page*30],total=total,page=page,chapters=chapters(),chapter=chapter,q=q,show=show,subs=subs)

@bp.route('/q/<item_id>',methods=['GET','POST'])
def edit(item_id):
    base=base_records().get(item_id) or abort(404)
    o=db.session.get(PolityUnit6Override,item_id)
    if request.method=='POST':
        action=request.form.get('action')
        if action=='reset':
            if o:db.session.delete(o);db.session.commit()
            flash('Restored the original / అసలు తిరిగి వచ్చింది');return redirect(url_for('.edit',item_id=item_id))
        if action=='delete':
            if not o:o=PolityUnit6Override(item_id=item_id,data={});db.session.add(o)
            o.deleted=True;o.updated_at=datetime.utcnow();db.session.commit()
            flash('Deleted (hidden from learners; can be restored) / తొలగించబడింది');return redirect(url_for('.home'))
        if action=='restore':
            if o:o.deleted=False;db.session.commit()
            flash('Restored / తిరిగి చేర్చబడింది');return redirect(url_for('.edit',item_id=item_id))
        f=request.form;d={}
        for k in ('question_en','question_te','explanation_en','explanation_te'):
            v=_clean(f.get(k),4000)
            if v:d[k]=v
        for lang in ('en','te'):
            opts=[_clean(f.get(f'option{i}_{lang}'),500) for i in range(1,5)]
            if all(opts):d['options_'+lang]=opts
        a=f.get('answer',type=int)
        if a in (1,2,3,4):d['answer']=a
        if not o:o=PolityUnit6Override(item_id=item_id,data={});db.session.add(o)
        o.data=d;o.deleted=False;o.updated_at=datetime.utcnow();db.session.commit()
        flash('Saved / సేవ్ అయింది');return redirect(url_for('.edit',item_id=item_id))
    cur=records().get(item_id) or base
    return render_template('ds/polity_admin_edit.html',q=cur,base=base,o=o,item_id=item_id)

@bp.post('/submit')
def submit():
    text=_clean(request.form.get('text'),8000)
    cid=request.form.get('chapter','')
    if cid:chapter_or_404(cid)
    if not text:flash('Nothing to save / ఏమీ రాయలేదు');return redirect(url_for('.home'))
    db.session.add(PolityUnit6Submission(chapter_id=cid,text=text));db.session.commit()
    flash('Saved to the database. It will be placed properly later / డేటాబేస్‌లో సేవ్ అయింది');return redirect(url_for('.home')+'#submissions')

@bp.post('/submission/<int:sid>')
def submission(sid):
    s=db.session.get(PolityUnit6Submission,sid) or abort(404)
    if request.form.get('action')=='delete':db.session.delete(s)
    else:s.status='placed' if s.status!='placed' else 'new'
    db.session.commit();return redirect(url_for('.home')+'#submissions')

@bp.get('/submissions.json')
def submissions_json():
    data=[dict(id=s.id,chapter=s.chapter_id,status=s.status,created_at=s.created_at.isoformat(),text=s.text) for s in PolityUnit6Submission.query.order_by(PolityUnit6Submission.id)]
    return Response(json.dumps(data,ensure_ascii=False,indent=1),mimetype='application/json',headers={'Content-Disposition':'attachment; filename=unit6-submissions.json'})

@bp.get('/changes.json')
def changes_json():
    data=[dict(item_id=o.item_id,deleted=o.deleted,changes=o.data,updated_at=o.updated_at.isoformat()) for o in overrides().values()]
    return Response(json.dumps(data,ensure_ascii=False,indent=1),mimetype='application/json',headers={'Content-Disposition':'attachment; filename=unit6-admin-changes.json'})

@bp.app_context_processor
def _admin_ctx():
    return {'unit6_is_admin':lambda:_is_authed()}
