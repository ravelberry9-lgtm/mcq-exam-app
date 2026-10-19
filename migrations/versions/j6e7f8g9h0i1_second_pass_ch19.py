"""Add source-aware APSCHE coverage for AP History Chapter 19.

Revision ID: j6e7f8g9h0i1
Revises: i5d6e7f8g9h0
"""
from datetime import datetime
import hashlib
import json

from alembic import op
import sqlalchemy as sa

revision = "j6e7f8g9h0i1"
down_revision = "i5d6e7f8g9h0"
branch_labels = None
depends_on = None

BATCH = "ap-history-apsche-second-pass-ch19-20261019"
MARKER = '<section class="apsche-second-pass-ch19" data-source="APSCHE second slow pass">'

ADDITION = MARKER + r'''
<h2>APSCHE రెండో పరిశీలన — 1857 హైదరాబాద్ రెసిడెన్సీ దాడి</h2>
<blockquote><strong>ప్రాధాన్య సూచన:</strong> ఇది ప్రధానంగా హైదరాబాద్/తెలంగాణ నేపథ్యం. APPSC Group–2లో ఆంధ్ర 1857 స్పందనకు సందర్భం ఇచ్చే పరిమిత bridge topicగా చదవాలి. RR/HR వాక్యాలు మార్చబడలేదు.</blockquote>
<p>1857 జూలై 17న మౌల్వీ అల్లావుద్దీన్, తుర్రెబాజ్ ఖాన్ నాయకత్వంలో రోహిల్లాలు మరియు వారిని అనుసరించిన జనసమూహం కోఠీలోని బ్రిటిష్ రెసిడెన్సీపై దాడి చేసింది. అప్పటి బ్రిటిష్ రెసిడెంట్ కల్నల్ కత్బర్ట్ డేవిడ్‌సన్ ముందుగానే రక్షణ ఏర్పాట్లు చేయడంతో దాడి విఫలమైంది. ఈ సంఘటన హైదరాబాద్‌లో 1857 స్పందన పూర్తిగా నిశ్శబ్దం కాదని చూపుతుంది.</p>
<p>సాలార్‌జంగ్ తిరుగుబాటును అణచడంలో బ్రిటిషువారికి సహకరించి శాంతిభద్రతలను కాపాడాడు. ఈ సహకారమే RRలో ఉన్న “1857–58 సేవలను బ్రిటిష్ ప్రతినిధులు గుర్తించి తరువాత అతని దివాను పదవిని రక్షించారు” అనే వాక్యానికి రాజకీయ నేపథ్యం. అంటే ఒకవైపు తుర్రెబాజ్ ఖాన్–అల్లావుద్దీన్ ప్రతిఘటన; మరోవైపు నిజాం ప్రభుత్వం–సాలార్‌జంగ్ బ్రిటిష్ అనుకూల వైఖరి అనే రెండు ప్రవాహాలు ఒకేసారి కనిపించాయి.</p>
<p><strong>సంఖ్యపై మూలభేదం:</strong> APSCHE పాఠ్యం దాడికి వచ్చినవారిని 5,000గా చెబుతుంది. వివరమైన తెలంగాణ చారిత్రక ఆధారాలు సుమారు 500 మంది రోహిల్లాలు, వారిని అనుసరించిన పెద్ద జనసమూహం అని వివరిస్తాయి. ఈ భేదం వల్ల సంఖ్యను నిర్ధిష్ట answer-key factగా మార్చలేదు. పరీక్షలో మూలం స్పష్టంగా అడిగితే మాత్రమే ఆ మూలంలోని సంఖ్యను అనుసరించాలి.</p>
</section>'''


def _q(qid, question, options, explanation, difficulty="M", qtype="direct"):
    keys=("a","b","c","d"); shift=(int(qid.rsplit("-",1)[1])-1)%4
    if shift: options=options[-shift:]+options[:-shift]
    return {"qid":qid,"question":question,"options":dict(zip(keys,options)),"answer":keys[shift],"explanation":explanation,"difficulty":difficulty,"qtype":qtype}


QUESTIONS = [
    _q("CH19-APSCHE2-001","1857 జూలై 17న హైదరాబాద్ బ్రిటిష్ రెసిడెన్సీపై దాడికి నాయకత్వం వహించిన జత ఏది?",["తుర్రెబాజ్ ఖాన్–మౌల్వీ అల్లావుద్దీన్","సాలార్‌జంగ్–డేవిడ్‌సన్","షేక్ పీర్ సాహెబ్–దండుసేన","నానాసాహెబ్–తాంతియా తోపే"],"హైదరాబాద్ రెసిడెన్సీ దాడికి తుర్రెబాజ్ ఖాన్, మౌల్వీ అల్లావుద్దీన్ నాయకత్వం వహించారు.","M","matching"),
    _q("CH19-APSCHE2-002","1857 హైదరాబాద్ దాడికి లక్ష్యమైన బ్రిటిష్ స్థావరం ఏది?",["కోఠీలోని బ్రిటిష్ రెసిడెన్సీ","సికింద్రాబాద్ రైల్వే స్టేషన్","చందా రైల్వే కార్యాలయం","బీరారు ఖజానా"],"దాడి కోఠీలోని British Residencyపై జరిగింది."),
    _q("CH19-APSCHE2-003","1857 సమయంలో హైదరాబాద్ బ్రిటిష్ రెసిడెంట్ ఎవరు?",["కల్నల్ కత్బర్ట్ డేవిడ్‌సన్","కల్నల్ మెట్‌కాఫ్","మేజర్ మన్రో","సర్ ఐర్ కూట్"],"కల్నల్ కత్బర్ట్ డేవిడ్‌సన్ ముందస్తు రక్షణ ఏర్పాట్లతో రెసిడెన్సీ దాడిని ఎదుర్కొన్నాడు.","H"),
    _q("CH19-APSCHE2-004","వాదన (A): 1857లో హైదరాబాద్ స్పందన ఏకరూపంగా లేదు. కారణం (R): తుర్రెబాజ్ ఖాన్–అల్లావుద్దీన్ ప్రతిఘటించగా, సాలార్‌జంగ్ బ్రిటిషువారికి సహకరించాడు.",["A, R రెండూ సరైనవి; R, Aకు సరైన వివరణ","A, R రెండూ సరైనవి; R సరైన వివరణ కాదు","A సరైనది; R తప్పు","A తప్పు; R సరైనది"],"ప్రతిఘటన, నిజాం ప్రభుత్వ బ్రిటిష్ అనుకూల వైఖరి రెండూ ఒకేసారి కనిపించాయి.","H","assertion_reason"),
]


def _vals(table,values): return {k:v for k,v in values.items() if k in table.c}


def upgrade():
    bind=op.get_bind(); meta=sa.MetaData(); subjects=sa.Table("subjects",meta,autoload_with=bind); chapters=sa.Table("chapters",meta,autoload_with=bind); canonical=sa.Table("syllabus_chapters",meta,autoload_with=bind); notes=sa.Table("notes",meta,autoload_with=bind); questions=sa.Table("questions",meta,autoload_with=bind)
    sid=bind.execute(sa.select(subjects.c.id).where(subjects.c.slug=="ap_history")).scalar_one(); cid=bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id==sid,chapters.c.chapter_num==19)).scalar_one(); scid=bind.execute(sa.select(canonical.c.id).where(canonical.c.subject_id==sid,canonical.c.chapter_num==19)).scalar_one()
    note=bind.execute(sa.select(notes).where(notes.c.chapter_id==cid).order_by(notes.c.section_num)).mappings().first(); original=note["body_te"] or ""
    if MARKER in original: raise RuntimeError("Chapter 19 already has second-pass marker")
    prefix_hash=hashlib.sha256(original.encode("utf-8")).hexdigest(); updated=original+"\n\n"+ADDITION
    if not updated.startswith(original): raise RuntimeError("Source-preservation guard failed")
    bind.execute(notes.update().where(notes.c.id==note["id"]).values(body_te=updated))
    existing=bind.execute(sa.select(sa.func.count()).select_from(questions).where(questions.c.subject_id==sid,questions.c.batch_id==BATCH)).scalar_one()
    if existing: raise RuntimeError(f"Unexpected existing batch rows: {existing}")
    slug=bind.execute(sa.select(canonical.c.slug).where(canonical.c.id==scid)).scalar_one(); now=datetime.utcnow()
    for q in QUESTIONS:
        trace={"source_label":"APSCHE second slow pass","source":"APSCHE History & Culture of Andhra (1512-1956)","source_conflict":"APSCHE says 5,000; detailed Telangana histories say about 500 Rohillas plus a larger following; no numeric MCQ created","preservation":"appended_only_rr_hr_unchanged","chapter_note_prefix_sha256":prefix_hash,"review_status":"manual_line_comparison"}
        values={"subject_id":sid,"chapter_id":cid,"source_type":"chapter","question_en":"","question_te":q["question"],"options_en":{k:"" for k in "abcd"},"options_te":q["options"],"correct_answer":q["answer"],"explanation_en":"","explanation_te":q["explanation"]+"\n"+json.dumps(trace,ensure_ascii=False),"difficulty":q["difficulty"],"qtype":q["qtype"],"syllabus_chapter_id":scid,"source":"APSCHE verified","source_file":"APSCHE Modern AP History Telugu PDF - second pass","source_qid":q["qid"],"source_chapter":"19","review_status":"author_reviewed","batch_id":BATCH,"content_hash":hashlib.md5((q["qid"]+q["question"]).encode()).hexdigest(),"q_hash":hashlib.md5((q["question"]+json.dumps(q["options"],ensure_ascii=False,sort_keys=True)).encode()).hexdigest(),"note_target_slug":slug+"-main","source_trace":trace,"created_at":now,"updated_at":now}
        bind.execute(questions.insert().values(**_vals(questions,values)))


def downgrade():
    bind=op.get_bind(); meta=sa.MetaData(); subjects=sa.Table("subjects",meta,autoload_with=bind); chapters=sa.Table("chapters",meta,autoload_with=bind); notes=sa.Table("notes",meta,autoload_with=bind); questions=sa.Table("questions",meta,autoload_with=bind)
    sid=bind.execute(sa.select(subjects.c.id).where(subjects.c.slug=="ap_history")).scalar_one(); bind.execute(questions.delete().where(questions.c.subject_id==sid,questions.c.batch_id==BATCH)); cid=bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id==sid,chapters.c.chapter_num==19)).scalar_one(); note=bind.execute(sa.select(notes).where(notes.c.chapter_id==cid).order_by(notes.c.section_num)).mappings().first(); body=note["body_te"] or ""; at=body.find("\n\n"+MARKER)
    if at<0: raise RuntimeError("Cannot safely remove Chapter 19 second-pass enrichment")
    bind.execute(notes.update().where(notes.c.id==note["id"]).values(body_te=body[:at]))
