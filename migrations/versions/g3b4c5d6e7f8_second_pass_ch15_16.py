"""Add second-pass APSCHE coverage for AP History Chapters 15-16.

Revision ID: g3b4c5d6e7f8
Revises: f2a3b4c5d6e7
"""
from datetime import datetime
import hashlib
import json

from alembic import op
import sqlalchemy as sa


revision = "g3b4c5d6e7f8"
down_revision = "f2a3b4c5d6e7"
branch_labels = None
depends_on = None

BATCH = "ap-history-apsche-second-pass-ch15-16-20261019"
MARKER = '<section class="apsche-second-pass" data-source="APSCHE second slow pass">'

ENRICHMENTS = {
    15: MARKER + r'''
<h2>APSCHE రెండో పరిశీలన — పులికాట్ నాణేల కేంద్రం</h2>
<blockquote><strong>మూల పరిరక్షణ:</strong> ఇది RR/HR లేదా మొదటి APSCHE పాఠ్యాన్ని మార్చదు. రెండో slow passలో నిర్ధారించిన చిన్న Group–2 విస్తరణ.</blockquote>
<p>పులికాట్ కేవలం గోదాం–కోట మాత్రమే కాదు; డచ్చి నాణేల కేంద్రంగా కూడా ఎదిగింది. APSCHE పాఠ్యం డచ్చివారికి సొంత నాణేలు ముద్రించుకునే అనుమతి లభించిందని చెబుతుంది. చారిత్రక ఆధారాల్లో పులికాట్‌లో VOC గుర్తు, పులికాట్‌ను సూచించే అక్షరంతో రాగి నాణేలు ముద్రించినట్లు తెలుస్తుంది. అయితే నాణేల ముద్రణ ప్రారంభం, అధికారిక రాజముద్ర హక్కు పొందిన దశలను వేర్వేరు ఆధారాలు వేర్వేరుగా చూపుతాయి. అందువల్ల పరీక్షలో తేదీని ఊహించకుండా <strong>పులికాట్—డచ్చి కోట, ప్రధాన వర్తక కేంద్రం, నాణేల కేంద్రం</strong> అనే సురక్షిత జతను గుర్తుంచుకోవాలి.</p>
</section>''',
    16: MARKER + r'''
<h2>APSCHE రెండో పరిశీలన — కర్ణాటక యుద్ధాల్లో సైనిక పాఠం, రాజకీయ వెనుకడుగు</h2>
<blockquote><strong>మూల పరిరక్షణ:</strong> క్రింది భాగం RR/HR కథనాన్ని మార్చదు. మొదటి APSCHE enrichmentలో మిగిలిన కారణ–ఫలిత సంబంధాలను మాత్రమే పూర్తి చేస్తుంది.</blockquote>
<h3>మొదటి యుద్ధం చెప్పిన సైనిక పాఠం</h3>
<p>ఐరోపాలో ఆస్ట్రియా వారసత్వ యుద్ధం ప్రారంభమైన తరువాత దాని ఆంగ్ల–ఫ్రెంచి పోటీ భారత తీరానికి చేరింది. ఫ్రెంచి గవర్నర్ డూప్లే మొదట యుద్ధాన్ని నివారించే మార్గం గురించి పూర్వ గవర్నర్ డ్యూమాను సంప్రదించాడు; అన్వరుద్దీన్ కూడా తన రాజ్యంలో పోరు వద్దని కోరాడు. కానీ ఆంగ్ల నౌకాదళ చర్యలు మొదలైన తరువాత డూప్లే మారిషస్‌లోని లా బోర్డొనైస్ సహాయం కోరాడు; ఫ్రెంచివారు మద్రాసును స్వాధీనం చేసుకున్నారు.</p>
<p>నవాబు కుమారుడు మహఫుజ్ ఖాన్ సేన మద్రాసును తిరిగి పొందడానికి కదిలింది. అడయార్ నది–శాన్ థోమ్ సమీపంలో పరాడిస్ నాయకత్వంలోని చిన్న, క్రమశిక్షణగల ఫ్రెంచి దళం సంఖ్యలో ఎంతో పెద్ద నవాబు సేనను ఓడించింది. పరీక్షకు యుద్ధం పేరు మాత్రమే కాక దాని భావం ముఖ్యము: <strong>శిక్షణ, సమన్వయం, తుపాకీ వినియోగం ఉన్న చిన్న దళం పెద్ద సంప్రదాయ సేనను ఓడించగలదని ఈ సంఘటన చూపింది.</strong> ఈ సైనిక పాఠమే తరువాత యూరోపియన్ కంపెనీలు భారతీయ వారసత్వ వివాదాల్లో ధైర్యంగా జోక్యం చేసుకోవడానికి ఒక కారణమైంది. 1748 ఐక్స్-లా-చాపెల్ ఒప్పందంతో మొదటి కర్ణాటక యుద్ధం ముగిసింది.</p>
<h3>రెండవ యుద్ధం—విజయాల నుంచి ఒప్పందానికి</h3>
<p>1749 ఆగస్టు 3 అంబూరు యుద్ధంలో అన్వరుద్దీన్ మరణించాడు. చందా సాహెబ్–ముజఫర్ జంగ్ పక్షానికి ఫ్రెంచి మద్దతు, ముహమ్మద్ అలీ–నాసిర్ జంగ్ పక్షానికి ఆంగ్ల మద్దతు లభించడం వల్ల స్థానిక వారసత్వ వివాదం యూరోపియన్ ప్రతిష్ఠా పోరుగా మారింది. క్లైవ్ ఆర్కాటును ఆక్రమించడం, కావేరీపాక్ వంటి యుద్ధాలు ఫ్రెంచి అనుకూల పక్షాన్ని బలహీనపరిచాయి.</p>
<p>1754లో డూప్లేను వెనక్కి పిలిపించి గోదెహ్యూను నియమించారు. గోదెహ్యూ–సాండర్స్ ఒప్పందంలో ఇరుకంపెనీలు స్థానిక పాలకుల రాజకీయ వివాదాల్లో జోక్యాన్ని తగ్గించాలని, యుద్ధంలో పొందిన ప్రాంతాలను తిరిగి ఇవ్వాలని అంగీకరించాయి. దీనివల్ల డూప్లే నిర్మించిన రాజకీయ ప్రభావం బలహీనపడింది; ముహమ్మద్ అలీ స్థానం బలపడింది. అంటే రెండవ యుద్ధం ముగింపు కేవలం సైనిక ఓటమి కాదు—ఫ్రెంచి రాజకీయ వ్యూహం ఒప్పందం ద్వారా వెనక్కి తగ్గిన దశ.</p>
</section>''',
}


def _q(chapter, qid, question, options, explanation, difficulty="M", qtype="direct"):
    keys = ("a", "b", "c", "d")
    shift = (int(qid.rsplit("-", 1)[1]) - 1) % 4
    if shift:
        options = options[-shift:] + options[:-shift]
    return {"chapter": chapter, "qid": qid, "question": question,
            "options": dict(zip(keys, options)), "answer": keys[shift],
            "explanation": explanation, "difficulty": difficulty, "qtype": qtype}


QUESTIONS = [
    _q(15,"CH15-APSCHE2-001","డచ్చివారి కోట, కోరమాండల్ ప్రధాన వర్తక కేంద్రం మరియు నాణేల ముద్రణతో సంబంధం ఉన్న స్థలం ఏది?",["పులికాట్","సూరత్","బొంబాయి","కలకత్తా"],"పులికాట్ డచ్చివారి కోట–వర్తక–నాణేల కేంద్రంగా ఎదిగింది; నాణేల హక్కు దశల ఖచ్చిత తేదీలపై మూలభేదం ఉన్నందున స్థలం–కార్య జతనే గుర్తుంచుకోవాలి."),
    _q(16,"CH16-APSCHE2-001","మొదటి కర్ణాటక యుద్ధంలో మద్రాసును స్వాధీనం చేసుకోవడానికి డూప్లే సహాయం కోరిన మారిషస్ ఫ్రెంచి అధికారి ఎవరు?",["లా బోర్డొనైస్","గోదెహ్యూ","బుస్సీ","ఐర్ కూట్"],"మారిషస్‌లోని లా బోర్డొనైస్ నౌకాదళ సహాయంతో ఫ్రెంచివారు మద్రాసును స్వాధీనం చేసుకున్నారు."),
    _q(16,"CH16-APSCHE2-002","అడయార్/శాన్ థోమ్ యుద్ధంలో చిన్న ఫ్రెంచి దళానికి నాయకత్వం వహించినవాడు ఎవరు?",["పరాడిస్","మహఫుజ్ ఖాన్","అన్వరుద్దీన్","చందా సాహెబ్"],"పరాడిస్ నాయకత్వంలోని క్రమశిక్షణగల ఫ్రెంచి దళం మహఫుజ్ ఖాన్‌కు చెందిన పెద్ద నవాబు సేనను ఓడించింది."),
    _q(16,"CH16-APSCHE2-003","వాదన (A): అడయార్ యుద్ధం భారతదేశంలోని యూరోపియన్ రాజకీయ జోక్యానికి ముఖ్యమైన మానసిక మలుపు. కారణం (R): శిక్షణ–సమన్వయం కలిగిన చిన్న యూరోపియన్ దళం సంఖ్యలో పెద్ద సంప్రదాయ సేనను ఓడించగలదని అది చూపింది.",["A, R రెండూ సరైనవి; R, Aకు సరైన వివరణ","A, R రెండూ సరైనవి; R సరైన వివరణ కాదు","A సరైనది; R తప్పు","A తప్పు; R సరైనది"],"అడయార్ ఫలితం సైన్య పరిమాణం కన్నా శిక్షణ, క్రమశిక్షణ, ఆయుధ వినియోగం ప్రాముఖ్యతను చూపింది.","H","assertion_reason"),
    _q(16,"CH16-APSCHE2-004","1748లో మొదటి కర్ణాటక యుద్ధాన్ని ముగించిన ఒప్పందం ఏది?",["ఐక్స్-లా-చాపెల్ ఒప్పందం","పారిస్ ఒప్పందం","అలహాబాద్ ఒప్పందం","సాల్బాయి ఒప్పందం"],"1748 ఐక్స్-లా-చాపెల్ ఒప్పందంతో మొదటి కర్ణాటక యుద్ధం ముగిసింది."),
    _q(16,"CH16-APSCHE2-005","అంబూరు యుద్ధానికి సరైన తేదీ ఏది?",["1749 ఆగస్టు 3","1748 అక్టోబరు 3","1754 ఆగస్టు 3","1760 జనవరి 22"],"1749 ఆగస్టు 3న అంబూరు యుద్ధంలో అన్వరుద్దీన్ మరణించాడు.","H"),
    _q(16,"CH16-APSCHE2-006","రెండవ కర్ణాటక యుద్ధం చివర్లో డూప్లే స్థానంలో వచ్చి ఆంగ్ల ప్రతినిధి సాండర్స్‌తో ఒప్పందం చేసినవాడు ఎవరు?",["గోదెహ్యూ","లా బోర్డొనైస్","పరాడిస్","కౌంట్ డి లాలీ"],"1754లో గోదెహ్యూ–సాండర్స్ ఒప్పందం యూరోపియన్ కంపెనీల స్థానిక రాజకీయ జోక్యాన్ని తగ్గించే దిశగా సాగింది.","H"),
    _q(16,"CH16-APSCHE2-007","కర్ణాటక యుద్ధాల సరైన ఫలిత క్రమాన్ని గుర్తించండి: 1. అడయార్‌లో సైనిక క్రమశిక్షణ ప్రభావం 2. గోదెహ్యూ ఒప్పందంతో ఫ్రెంచి రాజకీయ వెనుకడుగు 3. వాండివాష్‌లో నిర్ణాయక ఆంగ్ల విజయం",["1-2-3","2-1-3","1-3-2","3-2-1"],"మొదటి యుద్ధం అడయార్ పాఠం, రెండవ యుద్ధం 1754 ఒప్పందం, మూడవ యుద్ధం 1760 వాండివాష్ విజయం అనే క్రమం.","H","sequence"),
]


def _vals(table, values):
    return {k: v for k, v in values.items() if k in table.c}


def upgrade():
    bind = op.get_bind(); meta = sa.MetaData()
    subjects = sa.Table("subjects", meta, autoload_with=bind)
    chapters = sa.Table("chapters", meta, autoload_with=bind)
    canonical = sa.Table("syllabus_chapters", meta, autoload_with=bind)
    notes = sa.Table("notes", meta, autoload_with=bind)
    questions = sa.Table("questions", meta, autoload_with=bind)
    sid = bind.execute(sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")).scalar_one()
    chapter_ids = {}; canonical_ids = {}; hashes = {}
    for number, addition in ENRICHMENTS.items():
        cid = bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id == sid, chapters.c.chapter_num == number)).scalar_one()
        scid = bind.execute(sa.select(canonical.c.id).where(canonical.c.subject_id == sid, canonical.c.chapter_num == number)).scalar_one()
        note = bind.execute(sa.select(notes).where(notes.c.chapter_id == cid).order_by(notes.c.section_num)).mappings().first()
        original = note["body_te"] or ""
        if MARKER in original: raise RuntimeError(f"Chapter {number} already has second-pass marker")
        hashes[number] = hashlib.sha256(original.encode("utf-8")).hexdigest()
        updated = original + "\n\n" + addition
        if not updated.startswith(original): raise RuntimeError("Source-preservation guard failed")
        bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=updated))
        chapter_ids[number] = cid; canonical_ids[number] = scid
    existing = bind.execute(sa.select(sa.func.count()).select_from(questions).where(questions.c.subject_id == sid, questions.c.batch_id == BATCH)).scalar_one()
    if existing: raise RuntimeError(f"Unexpected existing batch rows: {existing}")
    slugs = dict(bind.execute(sa.select(canonical.c.chapter_num, canonical.c.slug).where(canonical.c.subject_id == sid, canonical.c.chapter_num.in_(tuple(ENRICHMENTS)))).all())
    now = datetime.utcnow()
    for q in QUESTIONS:
        trace = {"source_label":"APSCHE second slow pass","source":"APSCHE History & Culture of Andhra (1512-1956)","preservation":"appended_only_rr_hr_unchanged","chapter_note_prefix_sha256":hashes[q["chapter"]],"review_status":"manual_line_comparison"}
        values = {"subject_id":sid,"chapter_id":chapter_ids[q["chapter"]],"source_type":"chapter","question_en":"","question_te":q["question"],"options_en":{k:"" for k in "abcd"},"options_te":q["options"],"correct_answer":q["answer"],"explanation_en":"","explanation_te":q["explanation"]+"\n"+json.dumps(trace,ensure_ascii=False),"difficulty":q["difficulty"],"qtype":q["qtype"],"syllabus_chapter_id":canonical_ids[q["chapter"]],"source":"APSCHE","source_file":"APSCHE Modern AP History Telugu PDF - second pass","source_qid":q["qid"],"source_chapter":str(q["chapter"]),"review_status":"author_reviewed","batch_id":BATCH,"content_hash":hashlib.md5((q["qid"]+q["question"]).encode()).hexdigest(),"q_hash":hashlib.md5((q["question"]+json.dumps(q["options"],ensure_ascii=False,sort_keys=True)).encode()).hexdigest(),"note_target_slug":slugs[q["chapter"]]+"-main","source_trace":trace,"created_at":now,"updated_at":now}
        bind.execute(questions.insert().values(**_vals(questions, values)))


def downgrade():
    bind = op.get_bind(); meta = sa.MetaData()
    subjects = sa.Table("subjects", meta, autoload_with=bind); chapters = sa.Table("chapters", meta, autoload_with=bind)
    notes = sa.Table("notes", meta, autoload_with=bind); questions = sa.Table("questions", meta, autoload_with=bind)
    sid = bind.execute(sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")).scalar_one()
    bind.execute(questions.delete().where(questions.c.subject_id == sid, questions.c.batch_id == BATCH))
    for number in ENRICHMENTS:
        cid = bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id == sid, chapters.c.chapter_num == number)).scalar_one()
        note = bind.execute(sa.select(notes).where(notes.c.chapter_id == cid).order_by(notes.c.section_num)).mappings().first()
        body = note["body_te"] or ""; at = body.find("\n\n" + MARKER)
        if at < 0: raise RuntimeError(f"Cannot safely remove Chapter {number} second-pass enrichment")
        bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=body[:at]))
