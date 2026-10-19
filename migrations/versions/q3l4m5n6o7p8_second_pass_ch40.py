"""Add Gurajada biography and Kanyasulkam edition details to Chapter 40.

Revision ID: q3l4m5n6o7p8
Revises: p2k3l4m5n6o7
"""
from datetime import datetime
import hashlib
import json

from alembic import op
import sqlalchemy as sa


revision = "q3l4m5n6o7p8"
down_revision = "p2k3l4m5n6o7"
branch_labels = None
depends_on = None
BATCH = "ap-history-apsche-second-pass-ch40-20261019"
MARKER = '<section class="apsche-second-pass-ch40" data-source="APSCHE second slow pass">'
ADDITION = MARKER + r'''
<h2>APSCHE రెండో పరిశీలన — గురజాడ జీవితం నుంచి కన్యాశుల్కం రంగస్థలం వరకు</h2>
<blockquote><strong>మూల పరిరక్షణ:</strong> Chapter 40లోని RR సాహిత్య చరిత్ర, మొదటి APSCHE enrichment, జాషువా–భీమన్న–కొమర్రాజు భాగాలు మార్చబడలేదు. ఇప్పటివరకు లేని గురజాడ జీవన నేపథ్యం, నాటక ప్రదర్శన–ముద్రణ పరిణామాన్ని మాత్రమే జతచేస్తున్నాం.</blockquote>
<p><strong>గురజాడ అప్పారావు</strong> 2 సెప్టెంబరు 1862న విశాఖపట్నం ప్రాంతంలోని ఎలమంచిలి తాలూకా <strong>ఎస్. రాయవరం</strong>లో జన్మించారు. తల్లిదండ్రులు <strong>వెంకట రామదాసు–కౌసల్యమ్మ</strong>. కుటుంబ పూర్వీకులు కృష్ణా జిల్లాలోని గురజాడ గ్రామం నుంచి వచ్చినందువల్ల ‘గురజాడ’ ఇంటిపేరు స్థిరపడిందని APSCHE వివరిస్తుంది. ఈ నేపథ్యం ఆయనను కేవలం ఒక నాటక రచయితగా కాక, రచయిత–కవి–సంఘసంస్కర్త–వ్యవహారిక భాషావాది అనే సమగ్ర వ్యక్తిత్వంగా చూడటానికి సహాయపడుతుంది.</p>
<p><em>కన్యాశుల్కం</em> ఆనందగజపతి ప్రోత్సాహంతో కన్యాశుల్క దురాచారాన్ని విమర్శించేందుకు రచించబడింది. APSCHE ప్రకారం 1892లో విజయనగరం <strong>జగన్నాథ విలాసినీ సభ</strong> మొదట ప్రదర్శించింది. మొదటి కూర్పు 1897లో 5 అంకాలు, 132 రంగాలు, 109 పేజీలతో వెలువడింది; విస్తరించిన రెండో కూర్పు 1909లో 7 అంకాలు, 133 రంగాలు, 199 పేజీలతో వచ్చింది. సంఖ్యల కంటే ముఖ్యమైన మార్పు—రెండో కూర్పులో పాత్రల లోతు, ముఖ్యంగా గిరీశం–మధురవాణి చిత్రణ మరింత విస్తరించింది.</p>
<table><thead><tr><th>సంవత్సరం</th><th>గురజాడ సాహిత్య ప్రయాణంలో స్థానం</th></tr></thead><tbody>
<tr><td>1892</td><td>జగన్నాథ విలాసినీ సభ ద్వారా <em>కన్యాశుల్కం</em> తొలి ప్రదర్శన</td></tr>
<tr><td>1896</td><td><em>ప్రకాశిక</em> పత్రిక ప్రారంభం</td></tr>
<tr><td>1897</td><td><em>కన్యాశుల్కం</em> మొదటి కూర్పు</td></tr>
<tr><td>1909</td><td>విస్తరించిన రెండో కూర్పు</td></tr>
<tr><td>1910</td><td><em>దేశమును ప్రేమించుమన్నా</em> గేయం</td></tr>
</tbody></table>
<p>ఇక్కడ కథా సూత్రం: <strong>సంఘదురాచారం → రంగస్థల వ్యంగ్యం → వ్యవహారిక భాష → జీవంత పాత్రలు → ఆధునిక తెలుగు సాహిత్యానికి కొత్త దిశ</strong>. అందుకే <em>కన్యాశుల్కం</em>ను తేదీలు, అంకాల సంఖ్య మాత్రమే కాక సామాజిక లక్ష్యం–భాష–పాత్రచిత్రణతో కలిపి చదవాలి.</p>
</section>'''


def _q(qid, question, options, explanation, difficulty="M", qtype="direct"):
    keys=("a","b","c","d"); shift=(int(qid.rsplit("-",1)[1])-1)%4
    if shift: options=options[-shift:]+options[:-shift]
    return {"qid":qid,"question":question,"options":dict(zip(keys,options)),"answer":keys[shift],"explanation":explanation,"difficulty":difficulty,"qtype":qtype}


QUESTIONS=[
 _q("CH40-APSCHE2-001","గురజాడ అప్పారావు జన్మస్థలం ఏది?",["ఎలమంచిలి తాలూకా ఎస్. రాయవరం","కృష్ణా జిల్లా గురజాడ","విజయనగరం పట్టణం","గుంటూరు జిల్లా వినుకొండ"],"APSCHE ప్రకారం గురజాడ 2 సెప్టెంబరు 1862న ఎస్. రాయవరంలో జన్మించారు."),
 _q("CH40-APSCHE2-002","గురజాడ అప్పారావు తల్లిదండ్రుల సరైన జత ఏది?",["వెంకట రామదాసు–కౌసల్యమ్మ","వెంకట సుబ్బయ్య–గంగమ్మ","వీరయ్య–లింగమ్మ","పుల్లయ్య–నాగమ్మ"],"గురజాడ తల్లిదండ్రులు వెంకట రామదాసు, కౌసల్యమ్మ."),
 _q("CH40-APSCHE2-003","‘గురజాడ’ ఇంటిపేరు నేపథ్యంగా APSCHE పేర్కొన్న పూర్వీకుల గ్రామం ఏది?",["కృష్ణా జిల్లాలోని గురజాడ గ్రామం","ఎస్. రాయవరం","చాట్రగడ్డపాడు","మామిడికుదురు"],"కుటుంబ పూర్వీకులు కృష్ణా జిల్లాలోని గురజాడ గ్రామం నుంచి వచ్చినందువల్ల ఇంటిపేరు స్థిరపడిందని పాఠ్యం చెబుతుంది."),
 _q("CH40-APSCHE2-004","1892లో ‘కన్యాశుల్కం’ను మొదట ప్రదర్శించిన సంస్థ ఏది?",["జగన్నాథ విలాసినీ సభ","హితకారిణి సమాజం","విజ్ఞానచంద్రికా మండలి","ఆంధ్ర పరిశోధక మండలి"],"APSCHE ప్రకారం విజయనగరంలోని జగన్నాథ విలాసినీ సభ 1892లో నాటకాన్ని మొదట ప్రదర్శించింది."),
 _q("CH40-APSCHE2-005","‘కన్యాశుల్కం’ మొదటి కూర్పుకు సరైన వివరాలు ఏవి?",["1897—5 అంకాలు—132 రంగాలు—109 పేజీలు","1909—5 అంకాలు—132 రంగాలు—109 పేజీలు","1897—7 అంకాలు—133 రంగాలు—199 పేజీలు","1910—7 అంకాలు—132 రంగాలు—199 పేజీలు"],"APSCHE ఇచ్చిన మొదటి కూర్పు వివరాలు: 1897, 5 అంకాలు, 132 రంగాలు, 109 పేజీలు.","H","matching"),
 _q("CH40-APSCHE2-006","‘కన్యాశుల్కం’ రెండో కూర్పుకు సరైన వివరాలు ఏవి?",["1909—7 అంకాలు—133 రంగాలు—199 పేజీలు","1897—7 అంకాలు—133 రంగాలు—199 పేజీలు","1909—5 అంకాలు—132 రంగాలు—109 పేజీలు","1910—7 అంకాలు—199 రంగాలు—133 పేజీలు"],"విస్తరించిన రెండో కూర్పు 1909లో 7 అంకాలు, 133 రంగాలు, 199 పేజీలతో వచ్చింది.","H","matching"),
 _q("CH40-APSCHE2-007","గురజాడ ప్రారంభించిన ‘ప్రకాశిక’ పత్రిక సంవత్సరం ఏది?",["1896","1892","1897","1910"],"APSCHE జీవితచరిత్రలో ప్రకాశిక పత్రికను 1896లో ప్రారంభించినట్లు ఉంది."),
 _q("CH40-APSCHE2-008","సరైన కాలక్రమం ఏది? 1. కన్యాశుల్కం తొలి ప్రదర్శన 2. ప్రకాశిక 3. మొదటి కూర్పు 4. రెండో కూర్పు 5. దేశమును ప్రేమించుమన్నా",["1-2-3-4-5","2-1-3-5-4","1-3-2-4-5","3-2-1-5-4"],"సంవత్సరాలు వరుసగా 1892, 1896, 1897, 1909, 1910.","H","sequence"),
]


def _vals(t,v): return {k:x for k,x in v.items() if k in t.c}
def upgrade():
 b=op.get_bind(); m=sa.MetaData(); s=sa.Table("subjects",m,autoload_with=b); ch=sa.Table("chapters",m,autoload_with=b); can=sa.Table("syllabus_chapters",m,autoload_with=b); n=sa.Table("notes",m,autoload_with=b); q=sa.Table("questions",m,autoload_with=b)
 sid=b.execute(sa.select(s.c.id).where(s.c.slug=="ap_history")).scalar_one(); cid=b.execute(sa.select(ch.c.id).where(ch.c.subject_id==sid,ch.c.chapter_num==40)).scalar_one(); scid=b.execute(sa.select(can.c.id).where(can.c.subject_id==sid,can.c.chapter_num==40)).scalar_one(); note=b.execute(sa.select(n).where(n.c.chapter_id==cid).order_by(n.c.section_num)).mappings().first(); original=note["body_te"] or ""
 if MARKER in original: raise RuntimeError("Chapter 40 already has second-pass marker")
 ph=hashlib.sha256(original.encode()).hexdigest(); updated=original+"\n\n"+ADDITION
 if not updated.startswith(original): raise RuntimeError("Source-preservation guard failed")
 b.execute(n.update().where(n.c.id==note["id"]).values(body_te=updated)); existing=b.execute(sa.select(sa.func.count()).select_from(q).where(q.c.subject_id==sid,q.c.batch_id==BATCH)).scalar_one()
 if existing: raise RuntimeError(f"Unexpected existing batch rows: {existing}")
 slug=b.execute(sa.select(can.c.slug).where(can.c.id==scid)).scalar_one(); now=datetime.utcnow()
 for item in QUESTIONS:
  trace={"source_label":"APSCHE second slow pass","source":"APSCHE History & Culture of Andhra (1512-1956)","scope":"Gurajada biography and Kanyasulkam edition history","preservation":"appended_only_rr_hr_unchanged","chapter_note_prefix_sha256":ph,"review_status":"manual_line_comparison"}
  v={"subject_id":sid,"chapter_id":cid,"source_type":"chapter","question_en":"","question_te":item["question"],"options_en":{k:"" for k in "abcd"},"options_te":item["options"],"correct_answer":item["answer"],"explanation_en":"","explanation_te":item["explanation"]+"\n"+json.dumps(trace,ensure_ascii=False),"difficulty":item["difficulty"],"qtype":item["qtype"],"syllabus_chapter_id":scid,"source":"APSCHE","source_file":"APSCHE Modern AP History Telugu PDF - second pass","source_qid":item["qid"],"source_chapter":"40","review_status":"author_reviewed","batch_id":BATCH,"content_hash":hashlib.md5((item["qid"]+item["question"]).encode()).hexdigest(),"q_hash":hashlib.md5((item["question"]+json.dumps(item["options"],ensure_ascii=False,sort_keys=True)).encode()).hexdigest(),"note_target_slug":slug+"-main","source_trace":trace,"created_at":now,"updated_at":now}; b.execute(q.insert().values(**_vals(q,v)))
def downgrade():
 b=op.get_bind(); m=sa.MetaData(); s=sa.Table("subjects",m,autoload_with=b); ch=sa.Table("chapters",m,autoload_with=b); n=sa.Table("notes",m,autoload_with=b); q=sa.Table("questions",m,autoload_with=b); sid=b.execute(sa.select(s.c.id).where(s.c.slug=="ap_history")).scalar_one(); b.execute(q.delete().where(q.c.subject_id==sid,q.c.batch_id==BATCH)); cid=b.execute(sa.select(ch.c.id).where(ch.c.subject_id==sid,ch.c.chapter_num==40)).scalar_one(); note=b.execute(sa.select(n).where(n.c.chapter_id==cid).order_by(n.c.section_num)).mappings().first(); body=note["body_te"] or ""; at=body.find("\n\n"+MARKER)
 if at<0: raise RuntimeError("Cannot safely remove Chapter 40 second-pass enrichment")
 b.execute(n.update().where(n.c.id==note["id"]).values(body_te=body[:at]))
