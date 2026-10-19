"""Add second-pass APSCHE coverage for AP History Chapter 18.

Revision ID: i5d6e7f8g9h0
Revises: h4c5d6e7f8g9
"""
from datetime import datetime
import hashlib
import json

from alembic import op
import sqlalchemy as sa

revision = "i5d6e7f8g9h0"
down_revision = "h4c5d6e7f8g9"
branch_labels = None
depends_on = None

BATCH = "ap-history-apsche-second-pass-ch18-20261019"
MARKER = '<section class="apsche-second-pass-ch18" data-source="APSCHE second slow pass">'

ADDITION = MARKER + r'''
<h2>APSCHE రెండో పరిశీలన — విద్యా సంస్థలు, మిషనరీ వలయం, బ్రౌన్ తరువాతి జీవితం</h2>
<blockquote><strong>మూల పరిరక్షణ:</strong> RR/HR paragraphs మరియు మొదటి APSCHE enrichment యథాతథంగా ఉంటాయి. క్రింది భాగం రెండో line-by-line passలో నిర్ధారించిన gaps‌ను మాత్రమే జతచేస్తుంది.</blockquote>
<h3>విద్య మార్పు: పాఠశాల నుంచి కొత్త మధ్యతరగతి వరకు</h3>
<p>సంప్రదాయ విద్య ప్రధానంగా బ్రాహ్మణ బాలురకు అందేది; వృత్తి శిక్షణ కుటుంబ–కుల వృత్తుల ద్వారా సాగేది. మహిళలకు విద్యావకాశాలు చాలా తక్కువగా ఉండగా, ముస్లిం విద్యాసంస్థల్లో అరబీ–పారశీక భాషలకు ప్రాధాన్యం ఉండేది. ఆంగ్ల విద్య న్యాయ, బోధన, వైద్య, రెవెన్యూ, clerical ఉద్యోగాలకు మార్గం తెరిచి కొత్త మధ్యతరగతిని నిర్మించింది. ఆ వర్గమే తరువాత పత్రికలు, సంఘాలు, సామాజిక సంస్కరణ, రాజకీయ చైతన్యంలో ముఖ్య పాత్ర పోషించింది.</p>
<h3>సంస్థల chronologyని జాగ్రత్తగా చదవాలి</h3>
<p>మచిలీపట్నంలో రెవరెండ్ రాబర్ట్ టర్లింగ్టన్ నోబుల్, షార్కీ కలిసి 1843 నవంబరు 21న Native English School ప్రారంభించారు; అది 1864లో college grade పొందింది. అందువల్ల ‘నోబుల్ విద్యాసంస్థ’కు సంబంధించిన ప్రశ్నలో <strong>1843—పాఠశాల స్థాపన</strong>, <strong>1864—కళాశాల స్థాయి</strong>లను కలపకూడదు.</p>
<p>రాజమండ్రి Government College చరిత్రలో 1853లో Zilla School, 1868లో Provincial School, 1873లో Second Grade College, 1891లో Madras University affiliation అనే దశలు ఉన్నాయి. APSCHEలో కనిపించే సంక్షిప్త/వేరే year formulationsను ఈ అధికారిక institutional chronologyతో కలపకూడదు. విద్యాసంస్థల అభివృద్ధి ఒక్క తేదీ సంఘటన కాదు—school → provincial school → college → university affiliation అనే మెట్ల క్రమం.</p>
<h3>మిషనరీ వలయం—విద్య, భాష, సామాజిక మార్పు</h3>
<p>London Mission, Church Missionary Society, American Baptist, Canadian Baptist, Lutheran, Free Church, North German Mission వంటి సంస్థలు విశాఖపట్నం, కడప, మచిలీపట్నం, గుంటూరు, ఒంగోలు, నెల్లూరు, రాజమండ్రి ప్రాంతాల్లో కార్యకలాపాలు సాగించాయి. వీటి పాఠశాలలు మహిళలు, సామాజికంగా అణగారిన వర్గాలకు విద్యావకాశాలను విస్తరించాయి; విద్య–వైద్య–సంక్షేమ సేవలతో పాటు మతమార్పిడులు, సామాజిక ఉద్రిక్తతలు, హిందూ సంస్కరణ ప్రతిస్పందనలకు కూడా దారితీశాయి. కాబట్టి దీనిని కేవలం మతప్రచారంగా కాక విద్యా విస్తరణ–సామాజిక ప్రతిస్పందన రెండింటి కథగా చదవాలి.</p>
<h3>సి.పి. బ్రౌన్ సేవ: manuscript నుంచి modern reference వరకు</h3>
<p>కడప కలెక్టర్ జాన్ హాన్‌బరీ తెలుగు పాండిత్యం బ్రౌన్‌కు ప్రేరణగా నిలిచింది. బ్రౌన్ మాట్లాడే తెలుగును నేర్చుకొని, తన జీతంతో పండితులను నియమించి, తాళపత్ర ప్రతులను సేకరించి, పాఠభేదాలను సరిచేసి ముద్రించాడు. వేమన పద్యాల సేకరణ–అనువాదం, తెలుగు–ఇంగ్లీషు మరియు ఇంగ్లీషు–తెలుగు నిఘంటువులు, వ్యాకరణ రచనలు అతని సేవను భాషా పరిరక్షణ నుంచి ఆధునిక reference నిర్మాణం వరకు విస్తరించాయి.</p>
<p>బ్రౌన్ 1855లో కంపెనీ సేవ నుంచి విరమించి లండన్‌కు వెళ్లాడు. Royal Asiatic Society archival account ప్రకారం 1865లో London Universityలో తెలుగు professorగా నియమితుడై నిఘంటువుకు కొత్త పదాలు చేర్చడం కొనసాగించాడు. అందువల్ల ‘1854 నుంచే professor’ అనే సంక్షిప్త formulationకు బదులు <strong>1855—భారత సేవ నుంచి విరమణ; 1865—లండన్‌లో తెలుగు professor</strong> అనే నిర్ధారిత క్రమాన్ని పాటించాలి.</p>
<h3>1857లో ఆంధ్ర స్పందనకు రెండు ముఖాలు</h3>
<p>కడపలో షేక్ పీర్ సాహెబ్ పిలుపు, పార్లాకిమిడి సవర నాయకుడు దండుసేన పోరాటం వంటి ప్రతిఘటనలతో పాటు విశాఖపట్నం, రాజమండ్రి, విజయవాడ, గుంటూరు, నెల్లూరు, చిత్తూరు పట్టణాల్లో కొంత చదువుకున్న వర్గం బ్రిటిష్‌కు విధేయత సమావేశాలు నిర్వహించింది. కాబట్టి ఆంధ్రలో 1857ను ‘తిరుగుబాటు లేదు’ అని కొట్టివేయలేం; అలాగే ఉత్తర భారతదేశంలా విస్తృత సైనిక తిరుగుబాటుగా కూడా చెప్పలేం. పరిమిత ప్రతిఘటన–పట్టణ విధేయత రెండూ కలిసి ఉన్న ప్రాంతీయ స్పందన అది.</p>
</section>'''


def _q(qid, question, options, explanation, difficulty="M", qtype="direct"):
    keys = ("a", "b", "c", "d")
    shift = (int(qid.rsplit("-", 1)[1]) - 1) % 4
    if shift:
        options = options[-shift:] + options[:-shift]
    return {"qid":qid,"question":question,"options":dict(zip(keys,options)),"answer":keys[shift],"explanation":explanation,"difficulty":difficulty,"qtype":qtype}


QUESTIONS = [
    _q("CH18-APSCHE2-001","నోబుల్ విద్యాసంస్థ అభివృద్ధికి సరైన జత ఏది?",["1843—Native English School; 1864—college grade","1843—University; 1864—Zilla School","1853—school; 1891—college grade","1864—school; 1843—college grade"],"రాబర్ట్ నోబుల్–షార్కీ 1843లో పాఠశాల ప్రారంభించారు; అది 1864లో college grade పొందింది.","H","matching"),
    _q("CH18-APSCHE2-002","రాజమండ్రి Government College పూర్వరూపమైన Zilla School ప్రారంభమైన సంవత్సరం ఏది?",["1853","1868","1873","1891"],"అధికారిక institutional history ప్రకారం Zilla School 1853లో ప్రారంభమైంది."),
    _q("CH18-APSCHE2-003","రాజమండ్రి విద్యాసంస్థ అభివృద్ధి సరైన క్రమం ఏది? 1. Zilla School 2. Provincial School 3. Second Grade College 4. Madras University affiliation",["1-2-3-4","2-1-4-3","1-3-2-4","4-3-2-1"],"సంవత్సరాలు వరుసగా 1853, 1868, 1873, 1891.","H","sequence"),
    _q("CH18-APSCHE2-004","కడపలో సి.పి. బ్రౌన్ తెలుగు అభ్యాసానికి ప్రేరణగా నిలిచిన అధికారి ఎవరు?",["జాన్ హాన్‌బరీ","రాబర్ట్ నోబుల్","బెంజమిన్ షుల్ట్జ్","హెన్రీ మాంట్‌గొమరీ"],"కడప కలెక్టర్ జాన్ హాన్‌బరీ తెలుగు పాండిత్యం బ్రౌన్‌ను ప్రభావితం చేసింది."),
    _q("CH18-APSCHE2-005","సి.పి. బ్రౌన్ తరువాతి జీవితానికి సరైన క్రమం ఏది?",["1855—కంపెనీ సేవ విరమణ; 1865—లండన్‌లో తెలుగు professor","1855—తెలుగు professor; 1865—భారత సేవ ప్రారంభం","1854—మరణం; 1865—కడప కలెక్టర్","1865—భారత ప్రవేశం; 1855—నిఘంటువు నిషేధం"],"నిర్ధారిత archival chronology: 1855లో సేవ విరమణ, 1865లో London University Telugu professorship.","H","sequence"),
    _q("CH18-APSCHE2-006","వాదన (A): మిషనరీ కార్యకలాపాలను కేవలం మతప్రచారంగా మాత్రమే చూడటం అసంపూర్ణం. కారణం (R): అవి మహిళలు, అణగారిన వర్గాలకు విద్యను విస్తరించడంతో పాటు సామాజిక ప్రతిస్పందనలకు దారితీశాయి.",["A, R రెండూ సరైనవి; R, Aకు సరైన వివరణ","A, R రెండూ సరైనవి; R సరైన వివరణ కాదు","A సరైనది; R తప్పు","A తప్పు; R సరైనది"],"విద్య–సంక్షేమ విస్తరణ, మతమార్పిడి, సామాజిక ఉద్రిక్తత, సంస్కరణ స్పందన అన్నీ ఒకే చారిత్రక ప్రక్రియలో భాగాలు.","H","assertion_reason"),
    _q("CH18-APSCHE2-007","ఆంగ్ల విద్య వల్ల ఆంధ్రలో ఏర్పడిన కొత్త మధ్యతరగతితో ప్రత్యక్షంగా సంబంధం లేని ఎంపిక ఏది?",["వంశపారంపర్య సైన్యాధిపత్యం మాత్రమే","న్యాయవాద వృత్తి","ఉపాధ్యాయ వృత్తి","clerical ప్రభుత్వ ఉద్యోగాలు"],"ఆంగ్ల విద్య న్యాయ, బోధన, వైద్య, clerical రంగాలను విస్తరించింది; వంశపారంపర్య సైన్యాధిపత్యం దాని ప్రత్యక్ష ఫలితం కాదు.","M"),
    _q("CH18-APSCHE2-008","ఆంధ్రలో 1857 స్పందనను సమగ్రంగా తెలిపేది ఏది?",["పరిమిత స్థానిక ప్రతిఘటనతో పాటు కొన్ని పట్టణాల్లో బ్రిటిష్ విధేయత సమావేశాలు కూడా జరిగాయి","ఉత్తర భారతదేశంతో సమానమైన విస్తృత సైనిక యుద్ధం మాత్రమే జరిగింది","ఎక్కడా ఎలాంటి స్పందన కనిపించలేదు","కేవలం విద్యాసంస్థల స్థాపన మాత్రమే జరిగింది"],"ప్రతిఘటన–విధేయత రెండూ ఉన్న మిశ్రమ ప్రాంతీయ స్పందనగా అధ్యయనం చేయాలి.","H"),
]


def _vals(table, values): return {k:v for k,v in values.items() if k in table.c}


def upgrade():
    bind=op.get_bind(); meta=sa.MetaData()
    subjects=sa.Table("subjects",meta,autoload_with=bind); chapters=sa.Table("chapters",meta,autoload_with=bind)
    canonical=sa.Table("syllabus_chapters",meta,autoload_with=bind); notes=sa.Table("notes",meta,autoload_with=bind); questions=sa.Table("questions",meta,autoload_with=bind)
    sid=bind.execute(sa.select(subjects.c.id).where(subjects.c.slug=="ap_history")).scalar_one()
    cid=bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id==sid,chapters.c.chapter_num==18)).scalar_one()
    scid=bind.execute(sa.select(canonical.c.id).where(canonical.c.subject_id==sid,canonical.c.chapter_num==18)).scalar_one()
    note=bind.execute(sa.select(notes).where(notes.c.chapter_id==cid).order_by(notes.c.section_num)).mappings().first(); original=note["body_te"] or ""
    if MARKER in original: raise RuntimeError("Chapter 18 already has second-pass marker")
    prefix_hash=hashlib.sha256(original.encode("utf-8")).hexdigest(); updated=original+"\n\n"+ADDITION
    if not updated.startswith(original): raise RuntimeError("Source-preservation guard failed")
    bind.execute(notes.update().where(notes.c.id==note["id"]).values(body_te=updated))
    existing=bind.execute(sa.select(sa.func.count()).select_from(questions).where(questions.c.subject_id==sid,questions.c.batch_id==BATCH)).scalar_one()
    if existing: raise RuntimeError(f"Unexpected existing batch rows: {existing}")
    slug=bind.execute(sa.select(canonical.c.slug).where(canonical.c.id==scid)).scalar_one(); now=datetime.utcnow()
    for q in QUESTIONS:
        trace={"source_label":"APSCHE second slow pass","source":"APSCHE History & Culture of Andhra (1512-1956)","verification":"official institution histories and archival biography used where APSCHE dates conflict","preservation":"appended_only_rr_hr_unchanged","chapter_note_prefix_sha256":prefix_hash,"review_status":"manual_line_comparison"}
        values={"subject_id":sid,"chapter_id":cid,"source_type":"chapter","question_en":"","question_te":q["question"],"options_en":{k:"" for k in "abcd"},"options_te":q["options"],"correct_answer":q["answer"],"explanation_en":"","explanation_te":q["explanation"]+"\n"+json.dumps(trace,ensure_ascii=False),"difficulty":q["difficulty"],"qtype":q["qtype"],"syllabus_chapter_id":scid,"source":"APSCHE + verified institutional history","source_file":"APSCHE Modern AP History Telugu PDF - second pass","source_qid":q["qid"],"source_chapter":"18","review_status":"author_reviewed","batch_id":BATCH,"content_hash":hashlib.md5((q["qid"]+q["question"]).encode()).hexdigest(),"q_hash":hashlib.md5((q["question"]+json.dumps(q["options"],ensure_ascii=False,sort_keys=True)).encode()).hexdigest(),"note_target_slug":slug+"-main","source_trace":trace,"created_at":now,"updated_at":now}
        bind.execute(questions.insert().values(**_vals(questions,values)))


def downgrade():
    bind=op.get_bind(); meta=sa.MetaData(); subjects=sa.Table("subjects",meta,autoload_with=bind); chapters=sa.Table("chapters",meta,autoload_with=bind); notes=sa.Table("notes",meta,autoload_with=bind); questions=sa.Table("questions",meta,autoload_with=bind)
    sid=bind.execute(sa.select(subjects.c.id).where(subjects.c.slug=="ap_history")).scalar_one(); bind.execute(questions.delete().where(questions.c.subject_id==sid,questions.c.batch_id==BATCH))
    cid=bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id==sid,chapters.c.chapter_num==18)).scalar_one(); note=bind.execute(sa.select(notes).where(notes.c.chapter_id==cid).order_by(notes.c.section_num)).mappings().first(); body=note["body_te"] or ""; at=body.find("\n\n"+MARKER)
    if at<0: raise RuntimeError("Cannot safely remove Chapter 18 second-pass enrichment")
    bind.execute(notes.update().where(notes.c.id==note["id"]).values(body_te=body[:at]))
