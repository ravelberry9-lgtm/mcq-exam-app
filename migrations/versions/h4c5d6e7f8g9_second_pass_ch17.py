"""Add second-pass APSCHE coverage for AP History Chapter 17.

Revision ID: h4c5d6e7f8g9
Revises: g3b4c5d6e7f8
"""
from datetime import datetime
import hashlib
import json

from alembic import op
import sqlalchemy as sa


revision = "h4c5d6e7f8g9"
down_revision = "g3b4c5d6e7f8"
branch_labels = None
depends_on = None

BATCH = "ap-history-apsche-second-pass-ch17-20261019"
MARKER = '<section class="apsche-second-pass-ch17" data-source="APSCHE second slow pass">'

ADDITION = MARKER + r'''
<h2>APSCHE రెండో పరిశీలన — కంపెనీ పాలనలో పరిపాలన, ఆదాయం, ఆర్థిక మార్పులు</h2>
<blockquote><strong>మూల పరిరక్షణ:</strong> ఈ భాగం RR/HR proseను లేదా మొదటి APSCHE enrichmentను మార్చదు. రెండో line-by-line passలో మిగిలిన Group–2 అంశాలను మాత్రమే జతచేస్తుంది.</blockquote>
<h3>జిల్లా పరిపాలన: అధికారాల విభజన ఎందుకు జరిగింది?</h3>
<p>1794 తరువాత జిల్లా కలెక్టర్ భూమిశిస్తు వసూలు, శాంతిభద్రతలు, జిల్లా ప్రధాన మేజిస్ట్రేట్ బాధ్యతలను నిర్వహించాడు. కలెక్టర్, పోలీసు సూపరింటెండెంట్, జిల్లా జడ్జి కంపెనీ జిల్లా పరిపాలనలో మూడు ప్రధాన స్తంభాలుగా నిలిచారు. అయితే ఆదాయాధికారి చేతిలో న్యాయాధికారం కూడా ఉండటం సమస్యలకు దారితీయడంతో 1816లో కలెక్టర్ల న్యాయాధికారాలను తొలగించి ప్రత్యేక న్యాయాధికారులను నియమించారు. అంటే కంపెనీ పాలనలో మొదట అధికారాలు కలెక్టర్ వద్ద కేంద్రీకృతమై, తరువాత ఆదాయం–పోలీసు–న్యాయం వేర్వేరు శాఖలుగా రూపుదిద్దుకున్నాయి.</p>
<p>1766లో గోదావరి ప్రాంతం కంపెనీ ఆధీనంలోకి వచ్చింది. రాజమండ్రి, కాకినాడ కలెక్టరేట్లను రాజమండ్రి జిల్లాలో కలిపారు; తరువాత రాజమండ్రి–మచిలీపట్నం–కృష్ణా ప్రాంతాలను గోదావరి, కృష్ణా జిల్లాలుగా పునర్వ్యవస్థీకరించారు. మధ్య పరగణాల నుంచి భద్రాచలం తాలూకాను విడదీసి 1874లో గోదావరి జిల్లాలో చేర్చారు. ఈ వాక్యశ్రేణి జిల్లాల సరిహద్దులు స్థిరంగా కాక పాలనా అవసరాలకు అనుగుణంగా మారాయని చూపుతుంది.</p>
<h3>భూమిశిస్తు: పేర్లు వేరు, ఆదాయ లక్ష్యం ఒకటే</h3>
<p>ప్రభుత్వ నేరుగా ఆధీనంలోని భూములను హవేలీ భూములు అని, జమీందారుల మధ్యవర్తిత్వంలోని భూములను జమీందారీ భూములు అని పిలిచారు. జమీందారు–ప్రభుత్వం మధ్య స్థిరమైన శిస్తు మొత్తాన్ని నమోదు చేసిన లిఖిత ఒప్పందాన్ని <em>కౌలు</em> అని పేర్కొన్నారు; ప్రభుత్వానికి చెల్లించాల్సిన మొత్తమే పేష్‌కష్. 1793లో కార్న్‌వాలిస్ శాశ్వత జమీందారీ విధానాన్ని స్థిరపరిచాడు. ఇది బెంగాల్–బీహార్–ఒరిస్సాతో పాటు గంజాం నుంచి నెల్లూరు వరకు ఉన్న కోస్తాంధ్ర జిల్లాల్లోనూ అమలైంది.</p>
<p>రైత్వారీలో రైతును భూమి సాగుదారు–యజమానిగా గుర్తించి ప్రభుత్వమే నేరుగా శిస్తు నిర్ణయించింది. మధ్యవర్తి తొలగినా అధిక శిస్తు, అప్పు వల్ల రైతు భూమిని అమ్మడం లేదా తాకట్టు పెట్టడం పెరిగింది. గ్రామ పద్ధతిలో పేష్‌కష్ చెల్లించలేక ప్రభుత్వం స్వాధీనం చేసుకున్న కొన్ని గ్రామాలను గ్రామాధికారుల ఉమ్మడి బాధ్యతకు అప్పగించారు; ఆశించిన ఆదాయం రాకపోవడంతో ఈ ప్రయోగాన్ని విడిచిపెట్టి శాశ్వత లేదా రైత్వారీ పద్ధతులకు తిరిగారు.</p>
<h3>పారిశ్రామిక విప్లవం నుంచి ఆంధ్ర వృత్తుల పతనం వరకు</h3>
<p>ఇంగ్లాండులో యంత్రాలతో పెద్ద మొత్తంలో చౌక వస్త్రాలు తయారయ్యాయి. భారతదేశంలో బ్రిటిష్ వస్తువులకు అనుకూల మార్కెట్ ఏర్పడగా, భారతీయ వస్త్రాలపై ఇంగ్లాండులో అధిక సుంకాలు, నిషేధాలు ఉండేవి. ఈ అసమాన పోటీతో మచిలీపట్నం–విజయనగరం ప్రాంతాల మాంగనీ వంటి ప్రసిద్ధ వస్త్రాలు విదేశీ మార్కెట్లను కోల్పోయాయి. నిరుద్యోగం, మోతుర్ఫా వంటి పన్నుల ఒత్తిడి నేతకార్మికులను బర్మా, మారిషస్, శ్రీలంక వంటి ప్రాంతాలకు వలస వెళ్లేలా చేసింది.</p>
<h3>నీటిపారుదల: ప్రాజెక్టులు మరియు డెల్టా నిర్మాణం</h3>
<p>హెన్రీ మాంట్‌గొమరీ నివేదిక తరువాత కాటన్ గోదావరి–కృష్ణా ప్రాజెక్టులను ముందుకు నడిపాడు. గోదావరి ఆనకట్ట కాలువలను తూర్పు, మధ్య, పశ్చిమ డెల్టా కాలువలుగా నిర్వహించారు. కృష్ణా ఆనకట్టను 1852లో ప్రారంభించి 1855లో పూర్తి చేశారు; తరువాత కృష్ణా నది కాలువలు తూర్పు డెల్టా, పశ్చిమ డెల్టా వ్యవస్థలుగా విస్తరించాయి. కర్నూలు–కడప కాలువ 1863–1870 మధ్య నిర్మితమైంది. ఈ నీటిపారుదల డెల్టా వ్యవసాయాన్ని అభివృద్ధి చేసినప్పటికీ నీరు లేని మెట్ట ప్రాంతాలతో అసమానతను పెంచింది.</p>
<h3>కరవు సంఖ్యలను ఎలా చదవాలి?</h3>
<p>APSCHE పాఠ్యం దత్త మండలాల్లో కరవు మరణాలను 1805లో 3,225; 1806లో 4,902; 1807లో 17,207గా నమోదు చేస్తుంది. 1833 గుంటూరు ‘డొక్కల కరువు’లో సుమారు 50 లక్షల మంది ప్రభావితమై, సుమారు 2 లక్షల మంది మరణించారని అదే పాఠ్యం పేర్కొంటుంది. ఇవి మూలం పేర్కొన్న అంచనా సంఖ్యలు; పరీక్షలో వాటిని APSCHE-source figuresగా గుర్తించాలి. 1839 కరవు, 1865–66 గంజాం కరవు, 1890 కడప కరవు వరుస ఆంధ్రలో కరవు సమస్య నిరంతరతను చూపుతుంది.</p>
<h3>మన్రో ఎదుర్కొన్న పాలెగాళ్ల సమస్య</h3>
<p>APSCHE ప్రకారం 1800లో దత్త మండలాల్లో సుమారు 80 మంది పాలెగాళ్లకు 30,000కు పైగా సాయుధ అనుచరులు ఉండేవారు. మన్రో 1800–1807 మధ్య కలెక్టర్‌గా భూమిశిస్తు, శాంతిభద్రతలను పునర్వ్యవస్థీకరించి రైత్వారీ ప్రయోగాన్ని విస్తరించాడు. ఈ సంఖ్యలు పాలెగాళ్ల ప్రతిఘటన ఒక చిన్న స్థానిక వివాదం కాక, కంపెనీ అధికార స్థాపనకు పెద్ద పరిపాలనా–సైనిక సవాలు అని అర్థం చేయిస్తాయి.</p>
</section>'''


def _q(qid, question, options, explanation, difficulty="M", qtype="direct"):
    keys = ("a", "b", "c", "d")
    shift = (int(qid.rsplit("-", 1)[1]) - 1) % 4
    if shift:
        options = options[-shift:] + options[:-shift]
    return {"chapter": 17, "qid": qid, "question": question,
            "options": dict(zip(keys, options)), "answer": keys[shift],
            "explanation": explanation, "difficulty": difficulty, "qtype": qtype}


QUESTIONS = [
    _q("CH17-APSCHE2-001","కలెక్టర్ల నుంచి న్యాయాధికారాలను తొలగించి ప్రత్యేక న్యాయాధికారులను నియమించిన సంవత్సరం ఏది?",["1816","1794","1808","1858"],"1816లో కలెక్టర్ల న్యాయాధికారాలను తొలగించి ప్రత్యేక న్యాయాధికారులను నియమించారు."),
    _q("CH17-APSCHE2-002","మధ్య పరగణాల నుంచి భద్రాచలం తాలూకాను గోదావరి జిల్లాలో చేర్చిన సంవత్సరం ఏది?",["1874","1766","1855","1911"],"భద్రాచలం తాలూకా 1874లో గోదావరి జిల్లాలో చేరింది.","H"),
    _q("CH17-APSCHE2-003","జమీందారు–ప్రభుత్వం మధ్య స్థిరమైన శిస్తు మొత్తాన్ని నమోదు చేసిన లిఖిత ఒప్పందాన్ని ఏమని పిలిచేవారు?",["కౌలు","పేష్‌కష్","మోతుర్ఫా","ఇనాం"],"లిఖిత ఒప్పందం కౌలు; అందులో నిర్ణయించిన ప్రభుత్వ చెల్లింపు పేష్‌కష్."),
    _q("CH17-APSCHE2-004","శాశ్వత జమీందారీ విధానం అమలైన ఆంధ్ర ప్రాంత విస్తృతిని APSCHE ఎలా పేర్కొంటుంది?",["గంజాం నుంచి నెల్లూరు వరకు కోస్తాంధ్ర జిల్లాలు","రాయలసీమ మాత్రమే","తెలంగాణ జిల్లాలు మాత్రమే","గోదావరి డెల్టా మాత్రమే"],"1793 Permanent Settlement గంజాం నుంచి నెల్లూరు వరకు కోస్తాంధ్ర జిల్లాల్లో అమలైనట్లు పాఠ్యం పేర్కొంటుంది."),
    _q("CH17-APSCHE2-005","వాదన (A): రైత్వారీ పద్ధతిలో మధ్యవర్తి తొలగినా రైతు అప్పు సమస్య అంతరించలేదు. కారణం (R): అధిక శిస్తు వల్ల భూమి అమ్మకం, తాకట్టు పెరిగే అవకాశం ఏర్పడింది.",["A, R రెండూ సరైనవి; R, Aకు సరైన వివరణ","A, R రెండూ సరైనవి; R సరైన వివరణ కాదు","A సరైనది; R తప్పు","A తప్పు; R సరైనది"],"ప్రభుత్వం రైతుతో నేరుగా ఒప్పందం చేసినా అధిక శిస్తు–అప్పు–భూమి తాకట్టు అనే కారణశ్రేణి కొనసాగింది.","H","assertion_reason"),
    _q("CH17-APSCHE2-006","గోదావరి కాలువ వ్యవస్థల సరైన సమూహం ఏది?",["తూర్పు, మధ్య, పశ్చిమ డెల్టాలు","ఉత్తర, దక్షిణ, మధ్య పరగణాలు","కృష్ణా, పెన్నా, తుంగభద్ర","హవేలీ, జమీందారీ, ఇనాందారీ"],"గోదావరి కాలువలు Eastern, Central, Western delta systemsగా నిర్వహించబడ్డాయి.","M","matching"),
    _q("CH17-APSCHE2-007","APSCHEలోని దత్త మండలాల కరవు మరణాల సరైన పెరుగుదల క్రమం ఏది?",["1805—3,225; 1806—4,902; 1807—17,207","1805—17,207; 1806—4,902; 1807—3,225","1805—4,902; 1806—3,225; 1807—17,207","మూడు సంవత్సరాల్లో సమాన సంఖ్య"],"పాఠ్యం వరుసగా 3,225; 4,902; 17,207 మరణాలను నమోదు చేస్తుంది.","H","sequence"),
    _q("CH17-APSCHE2-008","1833 గుంటూరు ‘డొక్కల కరువు’ ప్రభావంపై APSCHE ఇచ్చిన అంచనా జత ఏది?",["సుమారు 50 లక్షల మంది ప్రభావితం; సుమారు 2 లక్షల మరణాలు","5 లక్షల మంది ప్రభావితం; 20 వేల మరణాలు","2 లక్షల మంది ప్రభావితం; 50 లక్షల మరణాలు","మరణాలు లేవు"],"APSCHE source figures ప్రకారం సుమారు 50 లక్షల మంది ప్రభావితమై, సుమారు 2 లక్షల మంది మరణించారు.","H"),
    _q("CH17-APSCHE2-009","1800లో దత్త మండలాల పాలెగాళ్ల బలాన్ని APSCHE ఏ విధంగా సూచిస్తుంది?",["సుమారు 80 పాలెగాళ్లు; 30,000కు పైగా సాయుధ అనుచరులు","8 పాలెగాళ్లు; 300 అనుచరులు","180 పాలెగాళ్లు; 3,000 అనుచరులు","30 పాలెగాళ్లు; 80,000 అనుచరులు"],"ఈ source figure పాలెగాళ్ల సమస్య పరిమాణాన్ని సూచిస్తుంది.","H"),
    _q("CH17-APSCHE2-010","కింది సంఘటనల సరైన కాలక్రమం ఏది? 1. గోదావరి ప్రాంతం కంపెనీ ఆధీనంలోకి రావడం 2. కలెక్టర్ల న్యాయాధికారాల తొలగింపు 3. భద్రాచలం గోదావరి జిల్లాలో చేరిక",["1-2-3","2-1-3","1-3-2","3-2-1"],"సంవత్సరాలు వరుసగా 1766, 1816, 1874.","H","sequence"),
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
    cid = bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id == sid, chapters.c.chapter_num == 17)).scalar_one()
    scid = bind.execute(sa.select(canonical.c.id).where(canonical.c.subject_id == sid, canonical.c.chapter_num == 17)).scalar_one()
    note = bind.execute(sa.select(notes).where(notes.c.chapter_id == cid).order_by(notes.c.section_num)).mappings().first()
    original = note["body_te"] or ""
    if MARKER in original:
        raise RuntimeError("Chapter 17 already has second-pass marker")
    prefix_hash = hashlib.sha256(original.encode("utf-8")).hexdigest()
    updated = original + "\n\n" + ADDITION
    if not updated.startswith(original):
        raise RuntimeError("Source-preservation guard failed")
    bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=updated))
    existing = bind.execute(sa.select(sa.func.count()).select_from(questions).where(questions.c.subject_id == sid, questions.c.batch_id == BATCH)).scalar_one()
    if existing:
        raise RuntimeError(f"Unexpected existing batch rows: {existing}")
    slug = bind.execute(sa.select(canonical.c.slug).where(canonical.c.id == scid)).scalar_one()
    now = datetime.utcnow()
    for q in QUESTIONS:
        trace = {"source_label":"APSCHE second slow pass","source":"APSCHE History & Culture of Andhra (1512-1956)","preservation":"appended_only_rr_hr_unchanged","chapter_note_prefix_sha256":prefix_hash,"review_status":"manual_line_comparison"}
        values = {"subject_id":sid,"chapter_id":cid,"source_type":"chapter","question_en":"","question_te":q["question"],"options_en":{k:"" for k in "abcd"},"options_te":q["options"],"correct_answer":q["answer"],"explanation_en":"","explanation_te":q["explanation"]+"\n"+json.dumps(trace,ensure_ascii=False),"difficulty":q["difficulty"],"qtype":q["qtype"],"syllabus_chapter_id":scid,"source":"APSCHE","source_file":"APSCHE Modern AP History Telugu PDF - second pass","source_qid":q["qid"],"source_chapter":"17","review_status":"author_reviewed","batch_id":BATCH,"content_hash":hashlib.md5((q["qid"]+q["question"]).encode()).hexdigest(),"q_hash":hashlib.md5((q["question"]+json.dumps(q["options"],ensure_ascii=False,sort_keys=True)).encode()).hexdigest(),"note_target_slug":slug+"-main","source_trace":trace,"created_at":now,"updated_at":now}
        bind.execute(questions.insert().values(**_vals(questions, values)))


def downgrade():
    bind = op.get_bind(); meta = sa.MetaData()
    subjects = sa.Table("subjects", meta, autoload_with=bind); chapters = sa.Table("chapters", meta, autoload_with=bind)
    notes = sa.Table("notes", meta, autoload_with=bind); questions = sa.Table("questions", meta, autoload_with=bind)
    sid = bind.execute(sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")).scalar_one()
    bind.execute(questions.delete().where(questions.c.subject_id == sid, questions.c.batch_id == BATCH))
    cid = bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id == sid, chapters.c.chapter_num == 17)).scalar_one()
    note = bind.execute(sa.select(notes).where(notes.c.chapter_id == cid).order_by(notes.c.section_num)).mappings().first()
    body = note["body_te"] or ""; at = body.find("\n\n" + MARKER)
    if at < 0:
        raise RuntimeError("Cannot safely remove Chapter 17 second-pass enrichment")
    bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=body[:at]))
