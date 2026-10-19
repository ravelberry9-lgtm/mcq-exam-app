"""Add APSCHE Raghupathi Venkataratnam details to Chapter 41.

Revision ID: r4m5n6o7p8q9
Revises: q3l4m5n6o7p8
"""
from datetime import datetime
import hashlib
import json

from alembic import op
import sqlalchemy as sa


revision = "r4m5n6o7p8q9"
down_revision = "q3l4m5n6o7p8"
branch_labels = None
depends_on = None
BATCH = "ap-history-apsche-second-pass-ch41-20261019"
MARKER = '<section class="apsche-second-pass-ch41" data-source="APSCHE second slow pass">'
ADDITION = MARKER + r'''
<h2>APSCHE రెండో పరిశీలన — రఘుపతి వెంకటరత్నం నాయుడు: సంస్కరణను ప్రాంతాలకు తీసుకెళ్లిన గురువు</h2>
<blockquote><strong>మూల పరిరక్షణ:</strong> పై RR మూలవాక్యాలు, వాటిలోని ఉద్యోగ–పదవీకాల సంవత్సరాలు యథాతథంగా ఉన్నాయి. APSCHE పాఠ్యంలో కనిపించిన అదనపు, పరీక్షోపయోగమైన విషయాలను మాత్రమే ఇక్కడ ప్రత్యేక మూలపొరగా జతచేస్తున్నాం. రెండు మూలాల ఉద్యోగ కాలక్రమం కలవని చోట APSCHE వివరాన్ని RR స్థానంలో పెట్టలేదు.</blockquote>
<p>రఘుపతి వెంకటరత్నం నాయుడు <strong>1 అక్టోబరు 1862</strong>న మచిలీపట్నంలో జన్మించారు. ఆయన సంస్కరణను ఒకే పట్టణంలో నిలిపివేయలేదు. APSCHE ప్రకారం 1894–95లో విజయవాడ, గుంటూరు, రాజమండ్రి, కాకినాడ, ఏలూరు పట్టణాల్లో ఉపన్యాసాలు ఇచ్చి బ్రహ్మసమాజ సిద్ధాంతాలను ప్రజలకు చేరువ చేశారు. ఈ పర్యటనను <strong>ఆలోచన → ఉపన్యాసం → ప్రాంతీయ కేంద్రం → సామాజిక చర్య</strong> అనే క్రమంలో అర్థం చేసుకోవాలి.</p>
<p>ఆ ప్రచారం ఫలితంగా మండపేట, ధర్మవరం, అమలాపురం ప్రాంతాల్లో బ్రహ్మోపాసన కేంద్రాలు ఏర్పడ్డాయని APSCHE చెబుతుంది. పిఠాపురం రాజా సహకారంతో కాకినాడలో బ్రహ్మమందిరం నిర్మాణం, బెంగాలీ బ్రహ్మసమాజ గ్రంథాలను తెలుగులోకి అనువదించేందుకు నిధి ఏర్పాటు—ఇవి ఉద్యమానికి సంస్థాగత రూపం ఇచ్చిన అడుగులు. అంటే వెంకటరత్నం పాత్ర ఉపన్యాసకుడితో ఆగలేదు; కేంద్రాలు, ప్రచురణలు, విద్యార్థులు అనే మూడు మార్గాల్లో ఉద్యమాన్ని నిలబెట్టాడు.</p>
<table><thead><tr><th>సంవత్సరం</th><th>ఘట్టం</th><th>పరీక్షలో గుర్తించాల్సిన సంబంధం</th></tr></thead><tbody>
<tr><td>1885</td><td>బ్రహ్మసమాజ సంస్కరణ కార్యకలాపాల్లో చురుకైన భాగస్వామ్యం</td><td>మత సంస్కరణ నుంచి సామాజిక సేవకు ప్రయాణం</td></tr>
<tr><td>1891</td><td>‘సాంఘిక శుద్ధి’ సమాజ స్థాపన</td><td>అనాచారాలు, మద్యపానం, బాలికల వసతిగృహాలపై కార్యాచరణ</td></tr>
<tr><td>1894–95</td><td>ఐదు ఆంధ్ర పట్టణాల్లో బ్రహ్మసమాజ ప్రచార పర్యటన</td><td>ప్రాంతీయ విస్తరణ</td></tr>
<tr><td>1924</td><td>బ్రిటిష్ ప్రభుత్వం నైట్ బిరుదు</td><td>విద్యా–సంఘసంస్కరణ సేవలకు గుర్తింపు</td></tr>
<tr><td>1927</td><td>ఆంధ్ర విశ్వకళాపరిషత్ తొలి స్నాతకోత్సవంలో గౌరవ డాక్టరేట్</td><td>విశ్వవిద్యాలయ గౌరవం</td></tr>
<tr><td>1932</td><td>‘బ్రహ్మర్షి’ బిరుదు</td><td>70వ జన్మదిన సందర్భపు ప్రజాగౌరవం</td></tr>
</tbody></table>
<p><em>బ్రహ్మప్రకాశిక</em>, <em>Fellow Worker</em>, <em>People's Friend</em> వంటి పత్రికలు/రచనల ద్వారా ఆయన సంస్కరణ భావాలను విస్తరించారు. ‘బ్రహ్మర్షి’, ‘శ్వేతాంబర ఋషి’, ‘అపర సోక్రటీస్’, ‘కులపతి’, ‘దివాన్ బహదూర్’, ‘కైజర్-ఇ-హింద్’, ‘సర్’ అనే బిరుదులు ఆయన వ్యక్తిత్వంలోని ఆధ్యాత్మికత, గురుత్వం, ప్రజాసేవ, ప్రభుత్వ గుర్తింపు అనే వేర్వేరు కోణాలను చూపుతాయి. <strong>26 మే 1939</strong>న ఆయన మరణించారు.</p>
<p><strong>ముఖ్య గమనిక:</strong> APSCHEలో ఉన్న Noble College–Pithapuram Raja College–Madras University ఉద్యోగ సంవత్సరాలు RRలోని సంవత్సరాలతో విభేదిస్తున్నందున అవి ఈ enrichmentలో పరీక్షా నిజాలుగా కలపలేదు. RR కాలక్రమమే ప్రధాన reference layerగా కొనసాగుతుంది.</p>
</section>'''


def _q(qid, question, options, explanation, difficulty="M", qtype="direct"):
    keys = ("a", "b", "c", "d")
    shift = (int(qid.rsplit("-", 1)[1]) - 1) % 4
    if shift:
        options = options[-shift:] + options[:-shift]
    return {"qid": qid, "question": question, "options": dict(zip(keys, options)), "answer": keys[shift], "explanation": explanation, "difficulty": difficulty, "qtype": qtype}


QUESTIONS = [
    _q("CH41-APSCHE2-001", "రఘుపతి వెంకటరత్నం నాయుడు పూర్తి జనన తేదీ ఏది?", ["1 అక్టోబరు 1862", "1 అక్టోబరు 1861", "26 మే 1862", "1 సెప్టెంబరు 1862"], "APSCHE జీవితచరిత్ర ప్రకారం ఆయన 1 అక్టోబరు 1862న మచిలీపట్నంలో జన్మించారు."),
    _q("CH41-APSCHE2-002", "APSCHE ప్రకారం 1894–95లో వెంకటరత్నం బ్రహ్మసమాజ సిద్ధాంతాలను ప్రచారం చేసిన పట్టణాల సరైన సముదాయం ఏది?", ["విజయవాడ–గుంటూరు–రాజమండ్రి–కాకినాడ–ఏలూరు", "తిరుపతి–కడప–కర్నూలు–అనంతపురం–బళ్లారి", "శ్రీకాకుళం–విజయనగరం–పార్వతీపురం–బొబ్బిలి–టెక్కలి", "నెల్లూరు–చిత్తూరు–మదనపల్లె–పుంగనూరు–కాళహస్తి"], "APSCHE ఈ ఐదు పట్టణాల ప్రచార పర్యటనను 1894–95కు అనుసంధానిస్తుంది.", "H", "matching"),
    _q("CH41-APSCHE2-003", "వెంకటరత్నం సంస్కరణ కాలక్రమంలో 1891కు సంబంధించినది ఏది?", ["సాంఘిక శుద్ధి సమాజ స్థాపన", "నైట్ బిరుదు", "గౌరవ డాక్టరేట్", "బ్రహ్మర్షి బిరుదు"], "APSCHE ప్రకారం 1891లో ‘సాంఘిక శుద్ధి’ సమాజాన్ని స్థాపించారు."),
    _q("CH41-APSCHE2-004", "రఘుపతి వెంకటరత్నం నాయుడు గౌరవాల కాలక్రమాన్ని సరిగా చూపే జత ఏది?", ["1924—నైట్ బిరుదు; 1927—గౌరవ డాక్టరేట్", "1924—గౌరవ డాక్టరేట్; 1927—నైట్ బిరుదు", "1927—బ్రహ్మర్షి; 1932—నైట్ బిరుదు", "1891—నైట్ బిరుదు; 1894—గౌరవ డాక్టరేట్"], "1924లో knighthood; 1927లో ఆంధ్ర విశ్వకళాపరిషత్ తొలి స్నాతకోత్సవంలో గౌరవ డాక్టరేట్ లభించాయి.", "H", "matching"),
    _q("CH41-APSCHE2-005", "APSCHE ప్రకారం ‘బ్రహ్మర్షి’ బిరుదు వెంకటరత్నానికి ఏ సంవత్సరంలో లభించింది?", ["1932", "1924", "1927", "1939"], "70వ జన్మదిన సందర్భంలో 1932లో ‘బ్రహ్మర్షి’ బిరుదు లభించింది."),
    _q("CH41-APSCHE2-006", "వెంకటరత్నంతో సంబంధం లేని పత్రిక/రచన ఏది?", ["వివేకవర్ధిని", "బ్రహ్మప్రకాశిక", "Fellow Worker", "People's Friend"], "బ్రహ్మప్రకాశిక, Fellow Worker, People's Friend వెంకటరత్నంతో అనుసంధానమైనవి; వివేకవర్ధిని కందుకూరితో సంబంధించింది.", "H", "negative"),
    _q("CH41-APSCHE2-007", "వెంకటరత్నం బ్రహ్మసమాజ ప్రాంతీయ విస్తరణకు సంబంధించిన సరైన కేంద్రాల సముదాయం ఏది?", ["మండపేట–ధర్మవరం–అమలాపురం", "ఆదోని–నంద్యాల–మార్కాపురం", "కడప–రాయచోటి–పులివెందుల", "నెల్లూరు–కావలి–గూడూరు"], "APSCHEలో మండపేట, ధర్మవరం, అమలాపురం బ్రహ్మోపాసన కేంద్రాలుగా పేర్కొనబడ్డాయి.", "H", "matching"),
    _q("CH41-APSCHE2-008", "రఘుపతి వెంకటరత్నం నాయుడు మరణించిన తేదీ ఏది?", ["26 మే 1939", "27 మే 1919", "17 డిసెంబరు 1959", "24 జూన్ 1980"], "APSCHE జీవనవివరాల ప్రకారం ఆయన 26 మే 1939న మరణించారు."),
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
    chapter_id = bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id == subject_id, chapters.c.chapter_num == 41)).scalar_one()
    syllabus_id = bind.execute(sa.select(canonical.c.id).where(canonical.c.subject_id == subject_id, canonical.c.chapter_num == 41)).scalar_one()
    note = bind.execute(sa.select(notes).where(notes.c.chapter_id == chapter_id).order_by(notes.c.section_num)).mappings().first()
    original = note["body_te"] or ""
    if MARKER in original:
        raise RuntimeError("Chapter 41 already has second-pass marker")
    prefix_hash = hashlib.sha256(original.encode()).hexdigest()
    updated = original + "\n\n" + ADDITION
    if not updated.startswith(original):
        raise RuntimeError("Source-preservation guard failed")
    bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=updated))
    existing = bind.execute(sa.select(sa.func.count()).select_from(questions).where(questions.c.subject_id == subject_id, questions.c.batch_id == BATCH)).scalar_one()
    if existing:
        raise RuntimeError(f"Unexpected existing batch rows: {existing}")
    slug = bind.execute(sa.select(canonical.c.slug).where(canonical.c.id == syllabus_id)).scalar_one()
    now = datetime.utcnow()
    for item in QUESTIONS:
        trace = {"source_label": "APSCHE second slow pass", "source": "APSCHE History & Culture of Andhra (1512-1956)", "scope": "Raghupathi Venkataratnam biography, Brahmo network, honours and publications", "preservation": "appended_only_rr_hr_unchanged", "chapter_note_prefix_sha256": prefix_hash, "review_status": "manual_line_comparison", "conflict_policy": "RR chronology retained; conflicting APSCHE career years excluded"}
        values = {"subject_id": subject_id, "chapter_id": chapter_id, "source_type": "chapter", "question_en": "", "question_te": item["question"], "options_en": {key: "" for key in "abcd"}, "options_te": item["options"], "correct_answer": item["answer"], "explanation_en": "", "explanation_te": item["explanation"] + "\n" + json.dumps(trace, ensure_ascii=False), "difficulty": item["difficulty"], "qtype": item["qtype"], "syllabus_chapter_id": syllabus_id, "source": "APSCHE", "source_file": "APSCHE Modern AP History Telugu PDF - second pass", "source_qid": item["qid"], "source_chapter": "41", "review_status": "author_reviewed", "batch_id": BATCH, "content_hash": hashlib.md5((item["qid"] + item["question"]).encode()).hexdigest(), "q_hash": hashlib.md5((item["question"] + json.dumps(item["options"], ensure_ascii=False, sort_keys=True)).encode()).hexdigest(), "note_target_slug": slug + "-main", "source_trace": trace, "created_at": now, "updated_at": now}
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
    chapter_id = bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id == subject_id, chapters.c.chapter_num == 41)).scalar_one()
    note = bind.execute(sa.select(notes).where(notes.c.chapter_id == chapter_id).order_by(notes.c.section_num)).mappings().first()
    body = note["body_te"] or ""
    at = body.find("\n\n" + MARKER)
    if at < 0:
        raise RuntimeError("Cannot safely remove Chapter 41 second-pass enrichment")
    bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=body[:at]))
