"""Add second-pass APSCHE coverage for AP History Chapter 20.

Revision ID: k7f8g9h0i1j2
Revises: j6e7f8g9h0i1
"""
from datetime import datetime
import hashlib
import json
from alembic import op
import sqlalchemy as sa

revision="k7f8g9h0i1j2"; down_revision="j6e7f8g9h0i1"; branch_labels=None; depends_on=None
BATCH="ap-history-apsche-second-pass-ch20-20261019"
MARKER='<section class="apsche-second-pass-ch20" data-source="APSCHE second slow pass">'

ADDITION=MARKER+r'''
<h2>APSCHE రెండో పరిశీలన — ప్రజాచైతన్యానికి సాంస్కృతిక పునాది</h2>
<blockquote><strong>మూల పరిరక్షణ:</strong> RR/HR మరియు మొదటి APSCHE enrichment మార్చబడలేదు. Chapter 40లోని విస్తృత సాహిత్య చరిత్రను పునరావృతం చేయకుండా, ఇక్కడ ప్రజాచైతన్యానికి కారణమైన సంబంధాలను మాత్రమే జతచేస్తున్నాం.</blockquote>
<h3>వీరేశలింగానికి ముందే ప్రశ్నలు మొదలయ్యాయి</h3>
<p>ఆంధ్ర సామాజిక సంస్కరణను ఒక్క కందుకూరి వీరేశలింగంతో అకస్మాత్తుగా ప్రారంభమైన ఉద్యమంగా చూడకూడదు. ఏనుగుల వీరాస్వామి, గాజుల లక్ష్మీనరసు శెట్టి, సామినేని ముద్దునరసింహం, పరవస్తు వెంకటరంగాచార్యులు, దేశిరాజు పెదబాపయ్య, గురజాడ అప్పారావు వంటి వ్యక్తులు వివిధ దశల్లో మూఢనమ్మకాలు, కుల కట్టుబాట్లు, స్త్రీల స్థితి, విద్య, సమాజ మార్పు గురించి ప్రశ్నించారు. వీరేశలింగం ప్రత్యేకత—ఇప్పటికే మొదలైన ప్రశ్నలను పత్రిక, సంఘం, పాఠశాల, వితంతు వివాహం వంటి నిరంతర కార్యాచరణగా మార్చడం.</p>
<h3>పత్రికల రెండో వలయం—చర్చ నుంచి సంస్థీకరణకు</h3>
<p>మొదటి enrichmentలోని <em>సత్యదూత–హితవాది–క్రెసెంట్–వివేకవర్ధిని–ఆంధ్ర ప్రకాశిక</em> వరుసకు తోడు, <em>పురుషార్థ ప్రదాయిని</em> (1872), గుంటుపల్లి శేషాచార్యుల <em>శశిరేఖ</em> (1874), దేవగుప్తం శేషాచలపతి యొక్క <em>దేశాభిమాని</em> (1886, గుంటూరు), న్యాపతి సుబ్బారావు <em>చింతామణి</em> వంటి పత్రికలు సామాజిక–రాజకీయ అభిప్రాయాలకు వేదికలయ్యాయి. ఒక పత్రిక సమస్యను పేరు పెట్టింది; పాఠకులు దానిపై చర్చించారు; సంఘాలు ఆ చర్చను కార్యక్రమంగా మార్చాయి—ఇదే ప్రజాచైతన్య విస్తరణ గొలుసు.</p>
<h3>బ్రహ్మసమాజం పట్టణ వలయంగా ఎలా విస్తరించింది?</h3>
<p>రాజమండ్రి నుంచి కాకినాడ, గుంటూరు, బాపట్ల, విజయవాడ, నరసరావుపేట, నెల్లూరు, చీరాల, విశాఖపట్నం, విజయనగరం వరకు బ్రహ్మసమాజ సంస్థలు ఏర్పడ్డాయని APSCHE పేర్కొంటుంది. సత్యసంవర్ధిని, థీయిస్ట్, హిందూ రిఫార్మర్, జనానా వంటి పత్రికలు ఏకేశ్వరవాదం, కులవివక్ష వ్యతిరేకత, స్త్రీ విద్య, సంస్కరణ భావాలను పట్టణాల మధ్య తీసుకెళ్లాయి. అందువల్ల బ్రహ్మసమాజ ప్రభావం ఒకే నాయకుడు లేదా ఒకే పట్టణానికి పరిమితం కాలేదు.</p>
<h3>సాహిత్యం–నాటకం ప్రజా వేదికగా మారిన విధానం</h3>
<p>ముద్రణతో తెలుగు గద్య, వ్యాసం, నవల, నాటకం, విమర్శ విస్తరించాయి. చదవలేని ప్రజలకు కూడా రంగస్థలం ద్వారా సామాజిక సందేశం చేరింది. గుంటూరు హిందూ నాటక సమాజం (1880), బందరు నేషనల్ థియేటర్ (1895), విశాఖపట్నం కళాభిలాష నాటక సమాజం (1895) వంటి సంస్థలు నాటకాన్ని వ్యక్తిగత వినోదం నుంచి సంఘటిత ప్రజా ప్రదర్శనగా మార్చాయి. కాబట్టి పత్రిక–సాహిత్యం–రంగస్థలం మూడు వేరు విషయాలు కావు; ప్రజాభిప్రాయం తయారుచేసిన అనుసంధాన వేదికలు.</p>
<h3>మొత్తం కారణ శ్రేణి</h3>
<p><strong>పాశ్చాత్య/మిషనరీ విద్య → కొత్త మధ్యతరగతి → తొలి సంస్కరణ స్వరాలు → పత్రికా చర్చ → బ్రహ్మసమాజం–స్థానిక సంఘాలు → సాహిత్య/నాటక ప్రజావేదిక → ఆచరణాత్మక సామాజిక సంస్కరణ → రాజకీయ ప్రజాచైతన్యం.</strong></p>
</section>'''

def _q(qid,question,options,explanation,difficulty="M",qtype="direct"):
    keys=("a","b","c","d"); shift=(int(qid.rsplit("-",1)[1])-1)%4
    if shift: options=options[-shift:]+options[:-shift]
    return {"qid":qid,"question":question,"options":dict(zip(keys,options)),"answer":keys[shift],"explanation":explanation,"difficulty":difficulty,"qtype":qtype}

QUESTIONS=[
 _q("CH20-APSCHE2-001","కింది వారిలో ఆంధ్ర తొలి సామాజిక సంస్కరణ స్వరాల సమూహానికి చెందనివాడు ఎవరు?",["సర్ ఐర్ కూట్","ఏనుగుల వీరాస్వామి","సామినేని ముద్దునరసింహం","పరవస్తు వెంకటరంగాచార్యులు"],"ఐర్ కూట్ సైనికాధికారి; మిగిలినవారు తొలి సామాజిక–మేధో చర్చలతో సంబంధం ఉన్నవారు.","M"),
 _q("CH20-APSCHE2-002","‘పురుషార్థ ప్రదాయిని’ పత్రికకు APSCHE పేర్కొన్న సంవత్సరం ఏది?",["1872","1835","1874","1886"],"పురుషార్థ ప్రదాయిని 1872తో ముడిపడి ఉంది."),
 _q("CH20-APSCHE2-003","‘శశిరేఖ’—సంపాదకుడు—సంవత్సరం సరైన జత ఏది?",["గుంటుపల్లి శేషాచార్యులు—1874","న్యాపతి సుబ్బారావు—1886","దేవగుప్తం శేషాచలపతి—1872","కందుకూరి వీరేశలింగం—1841"],"APSCHEలో గుంటుపల్లి శేషాచార్యుల శశిరేఖ 1874గా పేర్కొనబడింది.","H","matching"),
 _q("CH20-APSCHE2-004","‘దేశాభిమాని’ పత్రికతో సంబంధం ఉన్న సరైన జత ఏది?",["దేవగుప్తం శేషాచలపతి—గుంటూరు—1886","న్యాపతి సుబ్బారావు—రాజమండ్రి—1872","గాజుల లక్ష్మీనరసు శెట్టి—మద్రాసు—1844","గుంటుపల్లి శేషాచార్యులు—విశాఖపట్నం—1895"],"దేశాభిమాని పత్రికను దేవగుప్తం శేషాచలపతి గుంటూరులో 1886తో అనుసంధానిస్తారు.","H","matching"),
 _q("CH20-APSCHE2-005","కింది నాటక సంస్థల సరైన కాలక్రమం ఏది? 1. గుంటూరు హిందూ నాటక సమాజం 2. బందరు నేషనల్ థియేటర్ 3. విశాఖపట్నం కళాభిలాష నాటక సమాజం",["1-2/3 (1880 తరువాత రెండూ 1895)","2-1-3","3-2-1","మూడూ 1880లోనే"],"గుంటూరు సంస్థ 1880; బందరు, విశాఖపట్నం సంస్థలు 1895.","H","sequence"),
 _q("CH20-APSCHE2-006","వాదన (A): పత్రికలు మరియు నాటక సమాజాలు ప్రజాచైతన్యానికి పరస్పరపూరక వేదికలు. కారణం (R): పత్రికలు భావాలను చర్చకు తెస్తే, రంగస్థలం వాటిని విస్తృత ప్రజలకు దృశ్యరూపంలో చేరవేసింది.",["A, R రెండూ సరైనవి; R, Aకు సరైన వివరణ","A, R రెండూ సరైనవి; R సరైన వివరణ కాదు","A సరైనది; R తప్పు","A తప్పు; R సరైనది"],"ముద్రణ–రంగస్థలం కలిసి ప్రజాభిప్రాయ నిర్మాణాన్ని విస్తరించాయి.","H","assertion_reason"),
 _q("CH20-APSCHE2-007","ఆంధ్రలో బ్రహ్మసమాజ ప్రభావాన్ని సరిగ్గా అర్థం చేసుకునే విధానం ఏది?",["అనేక పట్టణ సంస్థలు, పత్రికలతో కూడిన వలయం","రాజమండ్రిలోని ఒకే సమావేశం","కేవలం మతమార్పిడి సంస్థ","కేవలం ఎన్నికల సంఘం"],"బ్రహ్మసమాజం అనేక పట్టణాలు, అనుబంధ పత్రికల ద్వారా సంస్కరణ భావాలను విస్తరించింది.","M"),
 _q("CH20-APSCHE2-008","ప్రజాచైతన్య అభివృద్ధి సరైన కారణ శ్రేణి ఏది?",["విద్య→కొత్త మధ్యతరగతి→పత్రికా చర్చ→సంఘాలు/రంగస్థలం→సంస్కరణ–రాజకీయ చైతన్యం","యుద్ధం→పత్రికల నిషేధం→విద్య అంతం→చైతన్యం","జమీందారీ→నౌకాదళం→కరవు→విశ్వవిద్యాలయం","రైల్వే రద్దు→సంఘాల రద్దు→ప్రజాచైతన్యం"],"Chapter 20 కథలో విద్య నుంచి ప్రజా వేదికల ద్వారా సంస్కరణ, రాజకీయ చైతన్యానికి మార్పు ప్రధానమైనది.","H","sequence"),
]

def _vals(t,v): return {k:x for k,x in v.items() if k in t.c}
def upgrade():
 bind=op.get_bind(); m=sa.MetaData(); s=sa.Table("subjects",m,autoload_with=bind); ch=sa.Table("chapters",m,autoload_with=bind); can=sa.Table("syllabus_chapters",m,autoload_with=bind); n=sa.Table("notes",m,autoload_with=bind); qtab=sa.Table("questions",m,autoload_with=bind)
 sid=bind.execute(sa.select(s.c.id).where(s.c.slug=="ap_history")).scalar_one(); cid=bind.execute(sa.select(ch.c.id).where(ch.c.subject_id==sid,ch.c.chapter_num==20)).scalar_one(); scid=bind.execute(sa.select(can.c.id).where(can.c.subject_id==sid,can.c.chapter_num==20)).scalar_one(); note=bind.execute(sa.select(n).where(n.c.chapter_id==cid).order_by(n.c.section_num)).mappings().first(); original=note["body_te"] or ""
 if MARKER in original: raise RuntimeError("Chapter 20 already has second-pass marker")
 ph=hashlib.sha256(original.encode()).hexdigest(); updated=original+"\n\n"+ADDITION
 if not updated.startswith(original): raise RuntimeError("Source-preservation guard failed")
 bind.execute(n.update().where(n.c.id==note["id"]).values(body_te=updated)); existing=bind.execute(sa.select(sa.func.count()).select_from(qtab).where(qtab.c.subject_id==sid,qtab.c.batch_id==BATCH)).scalar_one()
 if existing: raise RuntimeError(f"Unexpected existing batch rows: {existing}")
 slug=bind.execute(sa.select(can.c.slug).where(can.c.id==scid)).scalar_one(); now=datetime.utcnow()
 for q in QUESTIONS:
  trace={"source_label":"APSCHE second slow pass","source":"APSCHE History & Culture of Andhra (1512-1956)","cross_chapter_guard":"Chapter 40 literary survey not duplicated","preservation":"appended_only_rr_hr_unchanged","chapter_note_prefix_sha256":ph,"review_status":"manual_line_comparison"}; v={"subject_id":sid,"chapter_id":cid,"source_type":"chapter","question_en":"","question_te":q["question"],"options_en":{k:"" for k in "abcd"},"options_te":q["options"],"correct_answer":q["answer"],"explanation_en":"","explanation_te":q["explanation"]+"\n"+json.dumps(trace,ensure_ascii=False),"difficulty":q["difficulty"],"qtype":q["qtype"],"syllabus_chapter_id":scid,"source":"APSCHE","source_file":"APSCHE Modern AP History Telugu PDF - second pass","source_qid":q["qid"],"source_chapter":"20","review_status":"author_reviewed","batch_id":BATCH,"content_hash":hashlib.md5((q["qid"]+q["question"]).encode()).hexdigest(),"q_hash":hashlib.md5((q["question"]+json.dumps(q["options"],ensure_ascii=False,sort_keys=True)).encode()).hexdigest(),"note_target_slug":slug+"-main","source_trace":trace,"created_at":now,"updated_at":now}; bind.execute(qtab.insert().values(**_vals(qtab,v)))
def downgrade():
 bind=op.get_bind(); m=sa.MetaData(); s=sa.Table("subjects",m,autoload_with=bind); ch=sa.Table("chapters",m,autoload_with=bind); n=sa.Table("notes",m,autoload_with=bind); q=sa.Table("questions",m,autoload_with=bind); sid=bind.execute(sa.select(s.c.id).where(s.c.slug=="ap_history")).scalar_one(); bind.execute(q.delete().where(q.c.subject_id==sid,q.c.batch_id==BATCH)); cid=bind.execute(sa.select(ch.c.id).where(ch.c.subject_id==sid,ch.c.chapter_num==20)).scalar_one(); note=bind.execute(sa.select(n).where(n.c.chapter_id==cid).order_by(n.c.section_num)).mappings().first(); body=note["body_te"] or ""; at=body.find("\n\n"+MARKER)
 if at<0: raise RuntimeError("Cannot safely remove Chapter 20 second-pass enrichment")
 bind.execute(n.update().where(n.c.id==note["id"]).values(body_te=body[:at]))
