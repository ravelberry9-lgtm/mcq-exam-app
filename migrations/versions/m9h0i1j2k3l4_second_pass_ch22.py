"""Add verified APSCHE Individual Satyagraha and Quit India details to Chapter 22.

Revision ID: m9h0i1j2k3l4
Revises: l8g9h0i1j2k3
"""
from datetime import datetime
import hashlib
import json

from alembic import op
import sqlalchemy as sa


revision = "m9h0i1j2k3l4"
down_revision = "l8g9h0i1j2k3"
branch_labels = None
depends_on = None

BATCH = "ap-history-apsche-second-pass-ch22-20261019"
MARKER = '<section class="apsche-second-pass-ch22" data-source="APSCHE second slow pass">'
ADDITION = MARKER + r'''
<h2>APSCHE రెండో పరిశీలన — వ్యక్తిగత సత్యాగ్రహం నుంచి క్విట్ ఇండియా నిర్బంధం వరకు</h2>
<blockquote><strong>మూల పరిరక్షణ:</strong> ఈ భాగం Chapter 22లో ఇప్పటికే ఉన్న RR/HR కథనం లేదా వాక్యాలను మార్చదు. APSCHE పాఠ్యంలో స్పష్టంగా కనిపించిన అదనపు సందర్భం, ఆంధ్రకు సంబంధించిన పరిపాలనా చర్యలు, పరీక్షోపయోగ గణాంకాలను మాత్రమే జతచేస్తుంది.</blockquote>

<h3>1940: వ్యక్తిగత సత్యాగ్రహం — వాక్యాన్ని సరిగ్గా అర్థం చేసుకోవాలి</h3>
<p>రెండో ప్రపంచ యుద్ధంలో భారత ప్రజల సమ్మతి లేకుండానే బ్రిటిష్ ప్రభుత్వం భారతదేశాన్ని భాగస్వామిని చేసింది. దీనికి నిరసనగా కాంగ్రెస్ మంత్రివర్గాలు 1939లో రాజీనామా చేశాయి. యుద్ధకాలంలో వెంటనే సామూహిక ఉద్యమం చేపట్టకుండా, యుద్ధాన్ని వ్యతిరేకించే హక్కును ప్రకటించే పరిమిత అహింసా నిరసనగా గాంధీ <strong>వ్యక్తిగత సత్యాగ్రహాన్ని 17 అక్టోబర్ 1940న</strong> ప్రారంభించారు. <strong>వినోబా భావే</strong> తొలి వ్యక్తిగత సత్యాగ్రహి; ఆయన <strong>వర్ధా సమీపంలోని పవనార్ గ్రామంలో</strong> సత్యాగ్రహం చేశారు. ఉద్యమం 1941 చివరి వరకు కొనసాగింది.</p>
<p class="exam-note"><strong>పరీక్ష జాగ్రత్త:</strong> ఇది ‘ఆంధ్రలో తొలి వ్యక్తిగత సత్యాగ్రహి’ అని APSCHE చెప్పిన వాక్యం కాదు. పాఠ్యంలోని సూచన భారతదేశవ్యాప్త ఉద్యమ ప్రారంభం—వినోబా భావే, పవనార్, 17 అక్టోబర్ 1940.</p>

<h3>1942: ఆంధ్రలో క్విట్ ఇండియా ఉద్యమాన్ని అణచివేసిన విధానం</h3>
<p>ఆగస్టు 1942లో నాయకులను అరెస్టు చేసిన తరువాత ఉద్యమం నాయకత్వరహితంగా, ఆకస్మికంగా, కొన్ని చోట్ల హింసాత్మకంగా విస్తరించింది. టెలిఫోన్–టెలిగ్రాఫ్ తీగలు తెంచడం, రైల్వే పట్టాలు లేదా రహదారులను దెబ్బతీయడం, పోలీస్ స్టేషన్లు–ప్రభుత్వ కార్యాలయాలపై దాడులు వంటి చర్యలు చోటుచేసుకున్నాయి. ప్రభుత్వం కాంగ్రెస్‌తో పాటు <strong>National Students’ Organisation</strong>, <strong>National Youth League</strong> వంటి విద్యార్థి–యువజన సంస్థలను చట్టవిరుద్ధమని ప్రకటించింది.</p>
<table><thead><tr><th>నిర్బంధ చర్య</th><th>APSCHEలో ఇచ్చిన వివరాలు</th></tr></thead><tbody>
<tr><td>నిషేధాజ్ఞలు</td><td>అనేక చోట్ల <strong>సెక్షన్ 144</strong> విధించి బహిరంగ సమావేశాలను నిషేధించారు.</td></tr>
<tr><td>కర్ఫ్యూ పట్టణాలు</td><td><strong>చీరాల, పొన్నూరు, నిడుబ్రోలు, బాపట్ల</strong>లో ఒకటి నుంచి రెండు నెలల వరకు కర్ఫ్యూ విధించారు.</td></tr>
<tr><td>కర్ఫ్యూ సమయం</td><td>APSCHE తెలుగు పాఠ్యంలో సాయంత్రం <strong>6:30 నుంచి ఉదయం 5:00</strong> వరకు ప్రజలు బయటకు రావద్దని టాం-టాం ద్వారా ప్రకటించినట్లు ఉంది.</td></tr>
<tr><td>సామూహిక జరిమానాలు</td><td>అనంతపురం, కడప, పశ్చిమ గోదావరి, గుంటూరు, కృష్ణా, కర్నూలు, నెల్లూరు—ఈ ఏడు ఆంధ్ర జిల్లాల నుంచి వసూలు చేశారు.</td></tr>
<tr><td>అత్యధిక జరిమానా</td><td><strong>గుంటూరు — ₹3,21,681</strong>.</td></tr>
<tr><td>రెండో స్థానం</td><td><strong>పశ్చిమ గోదావరి — ₹2,48,285</strong>.</td></tr>
</tbody></table>
<p>ఈ గణాంకాల అర్థం కేవలం మొత్తాలను జ్ఞాపకం పెట్టుకోవడం కాదు. ఏడు జిల్లాలకు సామూహిక జరిమానాలు విస్తరించడం ఉద్యమం ఒకే పట్టణానికి పరిమితం కాలేదని చూపుతుంది; గుంటూరు, పశ్చిమ గోదావరి మొత్తాలు అక్కడి ఉద్యమ తీవ్రతకు పరిపాలనా ప్రతిస్పందన ఎంత కఠినంగా ఉందో సూచిస్తాయి.</p>
</section>'''


def _q(qid, question, options, explanation, difficulty="M", qtype="direct"):
    keys = ("a", "b", "c", "d")
    shift = (int(qid.rsplit("-", 1)[1]) - 1) % 4
    if shift:
        options = options[-shift:] + options[:-shift]
    return {
        "qid": qid,
        "question": question,
        "options": dict(zip(keys, options)),
        "answer": keys[shift],
        "explanation": explanation,
        "difficulty": difficulty,
        "qtype": qtype,
    }


QUESTIONS = [
    _q("CH22-APSCHE2-001", "1940లో ప్రారంభమైన వ్యక్తిగత సత్యాగ్రహంలో తొలి సత్యాగ్రహి ఎవరు?", ["వినోబా భావే", "జవహర్‌లాల్ నెహ్రూ", "సర్దార్ పటేల్", "సి. రాజగోపాలాచారి"], "గాంధీ ఎంపిక చేసిన తొలి వ్యక్తిగత సత్యాగ్రహి వినోబా భావే."),
    _q("CH22-APSCHE2-002", "వ్యక్తిగత సత్యాగ్రహం ప్రారంభమైన తేదీ ఏది?", ["17 అక్టోబర్ 1940", "8 ఆగస్టు 1942", "26 జనవరి 1930", "12 మార్చి 1930"], "వ్యక్తిగత సత్యాగ్రహం 17 అక్టోబర్ 1940న ప్రారంభమైంది."),
    _q("CH22-APSCHE2-003", "వినోబా భావే తొలి వ్యక్తిగత సత్యాగ్రహం చేసిన పవనార్ గ్రామం దేనికి సమీపంలో ఉంది?", ["వర్ధా", "బొంబాయి", "అలహాబాద్", "అహ్మదాబాద్"], "APSCHE ప్రకారం వినోబా భావే వర్ధా సమీపంలోని పవనార్ గ్రామంలో సత్యాగ్రహం చేశారు."),
    _q("CH22-APSCHE2-004", "APSCHE ప్రకారం వ్యక్తిగత సత్యాగ్రహ ఉద్యమం ఎప్పటి వరకు కొనసాగింది?", ["1941 చివరి వరకు", "1940 డిసెంబర్ వరకు", "1942 ఆగస్టు వరకు", "1945 చివరి వరకు"], "1940 అక్టోబరులో ప్రారంభమైన వ్యక్తిగత సత్యాగ్రహం 1941 చివరి వరకు కొనసాగింది."),
    _q("CH22-APSCHE2-005", "క్విట్ ఇండియా ఉద్యమ సమయంలో కర్ఫ్యూ విధించిన ఆంధ్ర పట్టణాల సరైన సమూహం ఏది?", ["చీరాల–పొన్నూరు–నిడుబ్రోలు–బాపట్ల", "విజయవాడ–గుంటూరు–నెల్లూరు–కర్నూలు", "విశాఖపట్నం–కాకినాడ–ఏలూరు–మచిలీపట్నం", "తెనాలి–ఒంగోలు–కడప–అనంతపురం"], "APSCHEలో చీరాల, పొన్నూరు, నిడుబ్రోలు, బాపట్లలో ఒకటి నుంచి రెండు నెలల వరకు కర్ఫ్యూ విధించినట్లు ఉంది.", "H", "grouping"),
    _q("CH22-APSCHE2-006", "క్విట్ ఇండియా ఉద్యమంలో సామూహిక జరిమానాలకు సంబంధించి జతలను పరిశీలించండి: 1. గుంటూరు—₹3,21,681; 2. పశ్చిమ గోదావరి—₹2,48,285. సరైనది ఏది?", ["1, 2 రెండూ సరైనవి", "1 మాత్రమే సరైనది", "2 మాత్రమే సరైనది", "1, 2 రెండూ తప్పు"], "APSCHE గణాంకాల్లో అత్యధిక మొత్తం గుంటూరు నుంచి, రెండో అత్యధిక మొత్తం పశ్చిమ గోదావరి నుంచి వసూలైంది.", "H", "statements"),
    _q("CH22-APSCHE2-007", "APSCHE ప్రకారం క్విట్ ఇండియా కాలంలో ఆంధ్రలో సామూహిక జరిమానాలు విధించిన జిల్లాల సంఖ్య ఎంత?", ["ఏడు", "నాలుగు", "ఐదు", "తొమ్మిది"], "అనంతపురం, కడప, పశ్చిమ గోదావరి, గుంటూరు, కృష్ణా, కర్నూలు, నెల్లూరు—మొత్తం ఏడు జిల్లాలు."),
    _q("CH22-APSCHE2-008", "వాదన (A): క్విట్ ఇండియా ఉద్యమ సమయంలో ఆంధ్రలో నిర్బంధ చర్యలు అనేక జిల్లాలకు విస్తరించాయి. కారణం (R): ఏడు జిల్లాల నుంచి సామూహిక జరిమానాలు వసూలు చేయడంతో పాటు అనేక చోట్ల సెక్షన్ 144 అమలు చేశారు.", ["A, R రెండూ సరైనవి; R, Aకు సరైన వివరణ", "A, R రెండూ సరైనవి; R సరైన వివరణ కాదు", "A సరైనది; R తప్పు", "A తప్పు; R సరైనది"], "సెక్షన్ 144, కర్ఫ్యూలు, ఏడు జిల్లాల్లో జరిమానాలు—నిర్బంధం విస్తృతిని నేరుగా చూపుతాయి.", "H", "assertion_reason"),
]


def _vals(table, values):
    return {key: value for key, value in values.items() if key in table.c}


def upgrade():
    bind = op.get_bind()
    meta = sa.MetaData()
    subjects = sa.Table("subjects", meta, autoload_with=bind)
    chapters = sa.Table("chapters", meta, autoload_with=bind)
    canonical = sa.Table("syllabus_chapters", meta, autoload_with=bind)
    notes = sa.Table("notes", meta, autoload_with=bind)
    questions = sa.Table("questions", meta, autoload_with=bind)

    subject_id = bind.execute(sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")).scalar_one()
    chapter_id = bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id == subject_id, chapters.c.chapter_num == 22)).scalar_one()
    syllabus_chapter_id = bind.execute(sa.select(canonical.c.id).where(canonical.c.subject_id == subject_id, canonical.c.chapter_num == 22)).scalar_one()
    note = bind.execute(sa.select(notes).where(notes.c.chapter_id == chapter_id).order_by(notes.c.section_num)).mappings().first()
    original = note["body_te"] or ""
    if MARKER in original:
        raise RuntimeError("Chapter 22 already has second-pass marker")
    prefix_hash = hashlib.sha256(original.encode()).hexdigest()
    updated = original + "\n\n" + ADDITION
    if not updated.startswith(original):
        raise RuntimeError("Source-preservation guard failed")
    bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=updated))

    existing = bind.execute(sa.select(sa.func.count()).select_from(questions).where(questions.c.subject_id == subject_id, questions.c.batch_id == BATCH)).scalar_one()
    if existing:
        raise RuntimeError(f"Unexpected existing batch rows: {existing}")
    slug = bind.execute(sa.select(canonical.c.slug).where(canonical.c.id == syllabus_chapter_id)).scalar_one()
    now = datetime.utcnow()
    for question in QUESTIONS:
        trace = {
            "source_label": "APSCHE second slow pass",
            "source": "APSCHE History & Culture of Andhra (1512-1956)",
            "scope": "individual satyagraha context and Andhra Quit India repression details",
            "preservation": "appended_only_rr_hr_unchanged",
            "chapter_note_prefix_sha256": prefix_hash,
            "review_status": "manual_line_comparison",
        }
        values = {
            "subject_id": subject_id,
            "chapter_id": chapter_id,
            "source_type": "chapter",
            "question_en": "",
            "question_te": question["question"],
            "options_en": {key: "" for key in "abcd"},
            "options_te": question["options"],
            "correct_answer": question["answer"],
            "explanation_en": "",
            "explanation_te": question["explanation"] + "\n" + json.dumps(trace, ensure_ascii=False),
            "difficulty": question["difficulty"],
            "qtype": question["qtype"],
            "syllabus_chapter_id": syllabus_chapter_id,
            "source": "APSCHE",
            "source_file": "APSCHE Modern AP History Telugu PDF - second pass",
            "source_qid": question["qid"],
            "source_chapter": "22",
            "review_status": "author_reviewed",
            "batch_id": BATCH,
            "content_hash": hashlib.md5((question["qid"] + question["question"]).encode()).hexdigest(),
            "q_hash": hashlib.md5((question["question"] + json.dumps(question["options"], ensure_ascii=False, sort_keys=True)).encode()).hexdigest(),
            "note_target_slug": slug + "-main",
            "source_trace": trace,
            "created_at": now,
            "updated_at": now,
        }
        bind.execute(questions.insert().values(**_vals(questions, values)))


def downgrade():
    bind = op.get_bind()
    meta = sa.MetaData()
    subjects = sa.Table("subjects", meta, autoload_with=bind)
    chapters = sa.Table("chapters", meta, autoload_with=bind)
    notes = sa.Table("notes", meta, autoload_with=bind)
    questions = sa.Table("questions", meta, autoload_with=bind)
    subject_id = bind.execute(sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")).scalar_one()
    bind.execute(questions.delete().where(questions.c.subject_id == subject_id, questions.c.batch_id == BATCH))
    chapter_id = bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id == subject_id, chapters.c.chapter_num == 22)).scalar_one()
    note = bind.execute(sa.select(notes).where(notes.c.chapter_id == chapter_id).order_by(notes.c.section_num)).mappings().first()
    body = note["body_te"] or ""
    marker_at = body.find("\n\n" + MARKER)
    if marker_at < 0:
        raise RuntimeError("Cannot safely remove Chapter 22 second-pass enrichment")
    bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=body[:marker_at]))
