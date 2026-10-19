"""Add the APSCHE study roadmap to AP History Chapter 21.

Revision ID: l8g9h0i1j2k3
Revises: k7f8g9h0i1j2
"""
from datetime import datetime
import hashlib
import json
from alembic import op
import sqlalchemy as sa

revision="l8g9h0i1j2k3"; down_revision="k7f8g9h0i1j2"; branch_labels=None; depends_on=None
BATCH="ap-history-apsche-second-pass-ch21-20261019"
MARKER='<section class="apsche-second-pass-ch21" data-source="APSCHE second slow pass">'
ADDITION=MARKER+r'''
<h2>APSCHE రెండో పరిశీలన — ఆంధ్రోద్యమాన్ని నాలుగు దశల్లో ఎలా చదవాలి?</h2>
<blockquote><strong>మూల పరిరక్షణ:</strong> Chapter 21లోని RR/HR సంఘటనలు, సమావేశాలు, నాయకులు మార్చబడలేదు. ఇప్పటికే ఉన్న facts‌ను పునరావృతం చేయకుండా వాటికి ఒక study-map మాత్రమే జతచేస్తున్నాం.</blockquote>
<p>APSCHE ఆంధ్రోద్యమాన్ని రెండు పెద్ద కోణాల్లో చూస్తుంది: <strong>స్వాతంత్ర్యానికి ముందు ఆంధ్రోద్యమం</strong>, <strong>స్వాతంత్ర్యం తరువాత ఆంధ్రోద్యమం</strong>. Chapter 21 ప్రధానంగా మొదటి కోణంలోని ప్రారంభ దశలను వివరిస్తుంది. భాష–సంస్కృతి పరిరక్షణగా మొదలైన భావం, ప్రత్యేక పరిపాలనా యూనిట్ డిమాండ్‌గా, తరువాత రాజకీయ తీర్మానాలు–సంస్థలుగా మారింది.</p>
<table><thead><tr><th>దశ</th><th>కాలం</th><th>చదవాల్సిన ప్రధాన మార్పు</th></tr></thead><tbody>
<tr><td>భావనా దశ</td><td>1904–1912</td><td>భాషా–చారిత్రక ఆత్మగౌరవం; ప్రత్యేక ఆంధ్ర ఆలోచనకు మేధో పునాది</td></tr>
<tr><td>ప్రచార దశ</td><td>1913–1920</td><td>ఆంధ్ర మహాసభలు, తీర్మానాలు, నాయకుల ప్రచారం; డిమాండ్‌కు సంఘటిత రూపం</td></tr>
<tr><td>మరుగునపడిన దశ</td><td>1920–1935</td><td>జాతీయోద్యమానికి ప్రాధాన్యం పెరగడంతో ప్రత్యేక రాష్ట్ర డిమాండ్ తాత్కాలికంగా వెనుకబడటం</td></tr>
<tr><td>తీర్మాన దశ</td><td>1935–1947</td><td>రాజ్యాంగ మార్పులు, ప్రాంతీయ safeguards, ప్రత్యేక రాష్ట్ర ప్రశ్నకు మళ్లీ రాజకీయ బలం</td></tr>
</tbody></table>
<p>ఈ periodisationను గట్టి గోడలుగా చూడకూడదు. ఒక దశలో మొదలైన భావాలు తరువాతి దశలో కొనసాగాయి. దీని ఉపయోగం—పెద్ద Chapter 21/23 కథలో సంఘటన ఎక్కడ సరిపోతుందో గుర్తించడం. ఉదాహరణకు 1913 బాపట్ల సభ ‘ప్రచార దశ’ ప్రారంభానికి ప్రతీక; 1920 తరువాత జాతీయోద్యమం ముందుకు రావడం ‘మరుగునపడిన దశ’ భావాన్ని వివరిస్తుంది.</p>
</section>'''

def _q(qid,question,options,explanation,difficulty="M",qtype="direct"):
 keys=("a","b","c","d"); shift=(int(qid.rsplit("-",1)[1])-1)%4
 if shift: options=options[-shift:]+options[:-shift]
 return {"qid":qid,"question":question,"options":dict(zip(keys,options)),"answer":keys[shift],"explanation":explanation,"difficulty":difficulty,"qtype":qtype}
QUESTIONS=[
 _q("CH21-APSCHE2-001","APSCHE periodisation ప్రకారం ఆంధ్రోద్యమ ‘భావనా దశ’ కాలం ఏది?",["1904–1912","1913–1920","1920–1935","1935–1947"],"భాషా–చారిత్రక ఆత్మగౌరవం ప్రత్యేక రాష్ట్ర ఆలోచనకు పునాది వేసిన 1904–1912 భావనా దశ."),
 _q("CH21-APSCHE2-002","1913–1920 ఆంధ్రోద్యమ దశను APSCHE ఏ పేరుతో చూపుతుంది?",["ప్రచార దశ","భావనా దశ","మరుగునపడిన దశ","తీర్మాన దశ"],"ఆంధ్ర మహాసభలు, తీర్మానాలు, ప్రచారం విస్తరించిన కాలం ప్రచార దశ."),
 _q("CH21-APSCHE2-003","ఆంధ్రోద్యమ నాలుగు దశల సరైన క్రమం ఏది?",["భావనా→ప్రచార→మరుగునపడిన→తీర్మాన","ప్రచార→భావనా→తీర్మాన→మరుగునపడిన","భావనా→తీర్మాన→ప్రచార→మరుగునపడిన","మరుగునపడిన→ప్రచార→భావనా→తీర్మాన"],"కాలక్రమం 1904–12, 1913–20, 1920–35, 1935–47.","H","sequence"),
 _q("CH21-APSCHE2-004","వాదన (A): ఆంధ్రోద్యమ periodisationను పరస్పరం సంబంధంలేని గట్టి విభాగాలుగా చూడకూడదు. కారణం (R): ఒక దశలో మొదలైన భావాలు తరువాతి దశల్లో కూడా కొనసాగాయి.",["A, R రెండూ సరైనవి; R, Aకు సరైన వివరణ","A, R రెండూ సరైనవి; R సరైన వివరణ కాదు","A సరైనది; R తప్పు","A తప్పు; R సరైనది"],"దశలు అధ్యయన సౌలభ్యానికి; చారిత్రక భావాలు నిరంతరంగా కొనసాగుతాయి.","H","assertion_reason"),
]

def _vals(t,v): return {k:x for k,x in v.items() if k in t.c}
def upgrade():
 b=op.get_bind(); m=sa.MetaData(); s=sa.Table("subjects",m,autoload_with=b); ch=sa.Table("chapters",m,autoload_with=b); can=sa.Table("syllabus_chapters",m,autoload_with=b); n=sa.Table("notes",m,autoload_with=b); qt=sa.Table("questions",m,autoload_with=b); sid=b.execute(sa.select(s.c.id).where(s.c.slug=="ap_history")).scalar_one(); cid=b.execute(sa.select(ch.c.id).where(ch.c.subject_id==sid,ch.c.chapter_num==21)).scalar_one(); scid=b.execute(sa.select(can.c.id).where(can.c.subject_id==sid,can.c.chapter_num==21)).scalar_one(); note=b.execute(sa.select(n).where(n.c.chapter_id==cid).order_by(n.c.section_num)).mappings().first(); original=note["body_te"] or ""
 if MARKER in original: raise RuntimeError("Chapter 21 already has second-pass marker")
 ph=hashlib.sha256(original.encode()).hexdigest(); updated=original+"\n\n"+ADDITION
 if not updated.startswith(original): raise RuntimeError("Source-preservation guard failed")
 b.execute(n.update().where(n.c.id==note["id"]).values(body_te=updated)); existing=b.execute(sa.select(sa.func.count()).select_from(qt).where(qt.c.subject_id==sid,qt.c.batch_id==BATCH)).scalar_one()
 if existing: raise RuntimeError(f"Unexpected existing batch rows: {existing}")
 slug=b.execute(sa.select(can.c.slug).where(can.c.id==scid)).scalar_one(); now=datetime.utcnow()
 for q in QUESTIONS:
  trace={"source_label":"APSCHE second slow pass","source":"APSCHE History & Culture of Andhra (1512-1956)","scope":"periodisation only; covered event facts not duplicated","preservation":"appended_only_rr_hr_unchanged","chapter_note_prefix_sha256":ph,"review_status":"manual_line_comparison"}; v={"subject_id":sid,"chapter_id":cid,"source_type":"chapter","question_en":"","question_te":q["question"],"options_en":{k:"" for k in "abcd"},"options_te":q["options"],"correct_answer":q["answer"],"explanation_en":"","explanation_te":q["explanation"]+"\n"+json.dumps(trace,ensure_ascii=False),"difficulty":q["difficulty"],"qtype":q["qtype"],"syllabus_chapter_id":scid,"source":"APSCHE","source_file":"APSCHE Modern AP History Telugu PDF - second pass","source_qid":q["qid"],"source_chapter":"21","review_status":"author_reviewed","batch_id":BATCH,"content_hash":hashlib.md5((q["qid"]+q["question"]).encode()).hexdigest(),"q_hash":hashlib.md5((q["question"]+json.dumps(q["options"],ensure_ascii=False,sort_keys=True)).encode()).hexdigest(),"note_target_slug":slug+"-main","source_trace":trace,"created_at":now,"updated_at":now}; b.execute(qt.insert().values(**_vals(qt,v)))
def downgrade():
 b=op.get_bind(); m=sa.MetaData(); s=sa.Table("subjects",m,autoload_with=b); ch=sa.Table("chapters",m,autoload_with=b); n=sa.Table("notes",m,autoload_with=b); q=sa.Table("questions",m,autoload_with=b); sid=b.execute(sa.select(s.c.id).where(s.c.slug=="ap_history")).scalar_one(); b.execute(q.delete().where(q.c.subject_id==sid,q.c.batch_id==BATCH)); cid=b.execute(sa.select(ch.c.id).where(ch.c.subject_id==sid,ch.c.chapter_num==21)).scalar_one(); note=b.execute(sa.select(n).where(n.c.chapter_id==cid).order_by(n.c.section_num)).mappings().first(); body=note["body_te"] or ""; at=body.find("\n\n"+MARKER)
 if at<0: raise RuntimeError("Cannot safely remove Chapter 21 second-pass enrichment")
 b.execute(n.update().where(n.c.id==note["id"]).values(body_te=body[:at]))
