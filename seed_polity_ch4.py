# seed_polity_ch4.py
# Chapter 4: Preamble of the Constitution
# (రాజ్యాంగ ప్రస్తావన)
# Standard : APPSC Group 2 | Source: Lakshmikanth Indian Polity
# Total Sections: 9 | Total MCQs: 60 | PYQs: 8
# Difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
# PYQ: 10th element (index 9) = 'APPSC' or 'UPSC'
# ─────────────────────────────────────────────

import json as _json

POLITY_CH4_SECTIONS = [
    {
        "title": "4.1 ప్రస్తావన — పరిచయం మరియు మూలం",
        "sub": "Preamble · Objective Resolution · USA Inspiration · Nov 26 1949",
        "audio": """ప్రస్తావన (Preamble) అంటే రాజ్యాంగం ముందు ఉండే పరిచయ వాక్యాలు.
ఇది రాజ్యాంగం యొక్క 'గుండె చప్పుడు' — లక్ష్యాలు, ఆదర్శాలు, ఆత్మ ఇందులో ఉన్నాయి.

మూలం (Source):
• USA రాజ్యాంగం యొక్క ప్రస్తావన నుండి స్ఫూర్తి పొందారు
• కానీ భారత ప్రస్తావన మరింత వివరంగా ఉంది

లక్ష్య తీర్మానం (Objective Resolution) తో సంబంధం:
• నెహ్రూ December 13, 1946న ప్రవేశపెట్టారు
• January 22, 1947న ఆమోదించారు
• ఇదే ప్రస్తావనకు పూర్వ రూపం

తేదీ:
• నవంబర్ 26, 1949 — ప్రస్తావన ఆమోదించిన తేదీ (రాజ్యాంగంతో పాటు)
• ప్రస్తావనలో తేదీ: "ఈ November 26 వ తేదీ రాజ్యాంగ నిర్మాణ సభలో ఆమోదించాం"

ప్రస్తావన పూర్తి పాఠం (Key Words):
"మేము, భారత ప్రజలు — భారతదేశాన్ని సార్వభౌమ, సమాజవాద, లౌకిక, ప్రజాస్వామ్య, గణతంత్ర రాజ్యంగా నిర్మించాలని..."
SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC"""
    },
    {
        "title": "4.2 సార్వభౌమత, సమాజవాదం, లౌకికత",
        "sub": "Sovereign · Socialist · Secular · 42nd Amendment 1976",
        "audio": """ప్రస్తావనలో మొదటి మూడు ముఖ్య పదాలు:

1. సార్వభౌమత (SOVEREIGN):
   • భారతదేశం ఏ బాహ్య శక్తికి లోబడదు
   • స్వతంత్ర విదేశీ విధానం నిర్ణయించుకుంటుంది
   • ఐక్యరాజ్యసమితి (UN) సభ్యత్వం — స్వచ్ఛందంగా అంగీకరించారు

2. సమాజవాదం (SOCIALIST):
   • 42వ రాజ్యాంగ సవరణ 1976 ద్వారా చేర్చారు
   • భారత సమాజవాదం = ప్రజాస్వామ్య సమాజవాదం (Democratic Socialism)
   • పూర్తి జాతీయీకరణ కాదు — మిశ్రమ ఆర్థిక వ్యవస్థ (Mixed Economy)
   • కమ్యూనిస్ట్ సమాజవాదం కాదు

3. లౌకికత (SECULAR):
   • 42వ రాజ్యాంగ సవరణ 1976 ద్వారా చేర్చారు
   • రాజ్యానికి అధికారిక మతం లేదు
   • అన్ని మతాలను సమానంగా గౌరవిస్తుంది
   • Positive Secularism — మతాన్ని నిషేధించదు, అన్నిటిని గౌరవిస్తుంది

గమనిక: 'Socialist' మరియు 'Secular' పదాలు మూల ప్రస్తావనలో లేవు — 1976 లో చేర్చారు."""
    },
    {
        "title": "4.3 ప్రజాస్వామ్యం మరియు గణతంత్రం",
        "sub": "Democratic · Republic · Elected President · France Inspiration",
        "audio": """4. ప్రజాస్వామ్యం (DEMOCRATIC):
   • ప్రజల యొక్క, ప్రజలచే, ప్రజల కోసం పాలన
   • ప్రజలే అధికారం యొక్క చివరి మూలం
   • ప్రత్యక్ష ప్రజాస్వామ్యం (Direct — Switzerland లాగా) కాదు
   • పరోక్ష / ప్రాతినిధ్య ప్రజాస్వామ్యం (Indirect / Representative Democracy)

5. గణతంత్రం (REPUBLIC):
   • రాజ్యాధినేత ఎన్నికైన వ్యక్తి (Elected head of state)
   • వంశపారంపర్య రాజు కాదు (No hereditary monarch)
   • భారత రాష్ట్రపతి = 5 సంవత్సరాలకు ఒకసారి ఎన్నికవుతారు
   • స్ఫూర్తి: ఫ్రాన్స్ (France) నుండి — Republic భావన
   • USA నుండి కూడా — President = elected head

గణతంత్రం = ప్రజాస్వామ్యం అంటే ఒకటే కాదు:
• ప్రజాస్వామ్యం = పాలన పద్ధతి
• గణతంత్రం = రాజ్యాధినేత ఎన్నికైన వ్యక్తి (not a king)

UK = ప్రజాస్వామ్యం + రాజ్యాంగ రాజ్యం (రాజు/రాణి ఉన్నారు — Republic కాదు)
India, France, USA = Republics"""
    },
    {
        "title": "4.4 న్యాయం, స్వేచ్ఛ, సమానత్వం",
        "sub": "Justice · Liberty · Equality · Three Types Each",
        "audio": """ప్రస్తావనలో మూడు ముఖ్య లక్ష్యాలు:

న్యాయం (JUSTICE) — 3 రకాలు:
• సామాజిక న్యాయం (Social Justice) — కులం, మతం, లింగ వివక్ష నిర్మూలన
• ఆర్థిక న్యాయం (Economic Justice) — సంపద అసమానత తగ్గించడం
• రాజకీయ న్యాయం (Political Justice) — ఓటు హక్కు, పదవులకు అవకాశం

స్వేచ్ఛ (LIBERTY) — 5 రకాలు:
• ఆలోచన స్వేచ్ఛ (Thought)
• వ్యక్తీకరణ స్వేచ్ఛ (Expression)
• విశ్వాస స్వేచ్ఛ (Belief)
• మతపర విశ్వాస స్వేచ్ఛ (Faith)
• ఆరాధన స్వేచ్ఛ (Worship)

సమానత్వం (EQUALITY) — 2 రకాలు:
• హోదాలో సమానత్వం (Status)
• అవకాశాల్లో సమానత్వం (Opportunity)

ఈ మూడూ ఫ్రాన్స్ విప్లవ నినాదం (French Revolution 1789) నుండి స్ఫూర్తి పొందాయి:
• Liberté (స్వేచ్ఛ) — Égalité (సమానత్వం) — Fraternité (సోదరభావం)"""
    },
    {
        "title": "4.5 సోదరభావం (Bilingual)",
        "sub": "Fraternity · Dignity of Individual · Unity and Integrity · 42nd Amendment",
        "audio": """సోదరభావం (FRATERNITY):
• వ్యక్తి గౌరవాన్ని నిర్థారించడం (Dignity of the Individual)
• దేశ ఐక్యత మరియు సమగ్రత (Unity and Integrity of the Nation)

'సమగ్రత (Integrity)' పదం:
• మూల ప్రస్తావనలో 'Unity of the Nation' మాత్రమే ఉండేది
• 42వ రాజ్యాంగ సవరణ 1976: 'Unity and Integrity of the Nation' గా మార్చారు

సోదరభావం అంటే ఏమిటి?
• అన్ని పౌరులు కలిసి జీవించే భావన
• కులం, మతం, భాష పేరిట విభేదాలు లేకపోవడం
• జాతీయ ఐక్యత

ప్రస్తావనలో సోదరభావం:
"...and to promote among them all FRATERNITY assuring the dignity of the individual and the unity and integrity of the Nation..."

గమనిక:
• Fraternity లేకుండా Liberty మరియు Equality అర్థం కోల్పోతాయి
• Dr. Ambedkar: "Fraternity means a sense of common brotherhood of all Indians" """
    },
    {
        "title": "4.6 42వ సవరణ మరియు సవరణ సాధ్యత (Bilingual)",
        "sub": "42nd Amendment 1976 · Amendability of Preamble · Basic Structure",
        "audio": """42వ రాజ్యాంగ సవరణ 1976 — ప్రస్తావనలో మార్పులు:

చేర్చిన పదాలు:
1. Socialist (సమాజవాదం)
2. Secular (లౌకికత)
3. Integrity (సమగ్రత) — 'Unity' తో పాటు

ఇది మాత్రమే ప్రస్తావనకు ఏకైక సవరణ — ఇప్పటివరకు ఒక్కసారి మాత్రమే ప్రస్తావన సవరించారు.

ప్రస్తావన సవరించవచ్చా?
• Kesavananda Bharati v. State of Kerala (1973) తీర్పు: ప్రస్తావన రాజ్యాంగంలో భాగమే
• Article 368 కింద పార్లమెంట్ ప్రస్తావనను సవరించవచ్చు
• కానీ Basic Structure ను దెబ్బతీయకూడదు

Basic Structure లో ఉన్నవి:
• Sovereignty (సార్వభౌమత)
• Republic (గణతంత్రం)
• Secular (లౌకికత)
• Democratic (ప్రజాస్వామ్యం)
• Federal character

42వ సవరణకు 'Mini Constitution' అని పేరు — చాలా మార్పులు చేసింది:
• Preamble లో Socialist + Secular + Integrity
• Fundamental Duties చేర్చడం
• Emergency నిబంధనలు మార్చడం"""
    },
    {
        "title": "4.7 ప్రస్తావన — న్యాయపర స్థితి (Bilingual)",
        "sub": "Part of Constitution? · Berubari Case 1960 · Kesavananda 1973 · LIC Case 1995",
        "audio": """ప్రస్తావన రాజ్యాంగంలో భాగమా? — న్యాయపర వివాదం

Berubari Union Case (1960):
• సుప్రీం కోర్టు: ప్రస్తావన రాజ్యాంగంలో భాగం కాదు
• కానీ రాజ్యాంగ వ్యాఖ్యానానికి (Interpretation) ఉపయోగించవచ్చు

Kesavananda Bharati v. State of Kerala (1973):
• ముఖ్య తీర్పు: ప్రస్తావన రాజ్యాంగంలో భాగమే!
• కానీ నేరుగా న్యాయస్థానాల్లో అమలు చేయించుకోలేరు
• Basic Structure సిద్ధాంతం (Basic Structure Doctrine) ప్రకటించారు

LIC of India Case (1995):
• ప్రస్తావన రాజ్యాంగంలో భాగమని మళ్ళీ నిర్ధారించారు

ప్రస్తావన ఏమి చేయగలదు?
✅ రాజ్యాంగ వ్యాఖ్యానంలో సహాయం
✅ శాసనాల ఉద్దేశ్యం అర్థం చేసుకోవడానికి
❌ నేరుగా చట్టపర హక్కులు ఇవ్వదు
❌ న్యాయస్థానాల్లో నేరుగా అమలు చేయించుకోలేరు

ముఖ్యమైన విషయం:
• ప్రస్తావన రాజ్యాంగం యొక్క 'తాళం చెవి' (Key to open the minds of the makers)
• ప్రస్తావన సవరించవచ్చు కానీ Basic Structure దెబ్బతీయకూడదు"""
    },
    {
        "title": "4.8 ప్రస్తావన — సమగ్ర విశ్లేషణ (Bilingual)",
        "sub": "Full Analysis · Sovereignty in People · Date · Authority",
        "audio": """ప్రస్తావన — సమగ్ర విశ్లేషణ:

"మేము, భారత ప్రజలు (WE, THE PEOPLE OF INDIA)"
• సార్వభౌమత్వం ప్రజలలో ఉంది
• రాజ్యాంగానికి అధికారం ప్రజల నుండే

"భారతదేశాన్ని...నిర్మించాలని సంకల్పించాం"
• రాజ్యాంగ నిర్మాణ సభ ప్రజల ప్రతినిధులుగా రాజ్యాంగం రాశారు

"సార్వభౌమ సమాజవాద లౌకిక ప్రజాస్వామ్య గణతంత్ర"
• 5 ముఖ్య లక్షణాలు

"న్యాయం, స్వేచ్ఛ, సమానత్వం"
• పౌరులకు కల్పించాల్సిన 3 లక్ష్యాలు

"సోదరభావం"
• 4వ లక్ష్యం — వ్యక్తి గౌరవం + దేశ ఐక్యత

"November 26, 1949"
• ఈ తేదీన ప్రస్తావన ఆమోదించారు
• రాజ్యాంగ దినం (Constitution Day)

ప్రస్తావన స్ఫూర్తి:
• USA Preamble: "We the People of the United States..."
• కానీ భారత ప్రస్తావన మరింత వివరంగా మరియు ఆదర్శప్రాయంగా ఉంది

అంబేడ్కర్ సూక్తి:
"The Preamble contains the essence of our Constitution." """
    },
    {
        "title": "4.9 సినిమాటిక్ కథ — ప్రస్తావన",
        "sub": "Full Chapter Story · People's Sovereignty · Nehru · Ambedkar",
        "audio": """November 26, 1949. రాజ్యాంగ నిర్మాణ సభ హాలు నిశ్శబ్దంగా ఉంది.

"మేము, భారత ప్రజలు..." — రాజేంద్ర ప్రసాద్ మొదటి వాక్యం చదివారు.

ఆ నాలుగు మాటలు — "WE, THE PEOPLE" — అది ఒక విప్లవం.
బ్రిటిష్ వారు ఇచ్చింది కాదు. రాజులు ఇచ్చింది కాదు.
ప్రజలే తమకు తాముగా ఇచ్చుకున్న రాజ్యాంగం.

నెహ్రూ December 13, 1946న చెప్పారు: "సార్వభౌమ, స్వతంత్ర, గణతంత్ర భారతదేశం పుట్టాలి."
ఆ Objective Resolution — ఈ ప్రస్తావనకు నీడ.

అంబేడ్కర్ ఒక రోజు అన్నారు: "Fraternity లేకుండా Liberty అర్థం కోల్పోతుంది. సోదరభావం లేకుండా స్వేచ్ఛ శూన్యం."

42వ సవరణ 1976 వచ్చింది — Socialist + Secular + Integrity చేర్చారు.
Kesavananda Bharati తీర్పు వచ్చింది — ప్రస్తావన రాజ్యాంగంలో భాగమని నిర్ధారించారు.

ఈ రోజు ఆ ప్రస్తావన ప్రతి రాజ్యాంగ పుస్తకం మొదట్లో ఉంది.
అది కేవలం మాటలు కాదు — అది ఒక ప్రమాణం.
భారత ప్రజలు తమకు తాముగా చేసుకున్న ప్రమాణం."""
    },
]

# ─────────────────────────────────────────────
#  MCQ DATA
#  (sec_idx, difficulty, q_te, a, b, c, d, correct, explanation_te)
#  difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
#  exam_type:  appended as 10th element (index 9) when PYQ ('APPSC'/'UPSC')
# ─────────────────────────────────────────────

POLITY_CH4_MCQS = [

    # ══════════════════════════════════════════
    # SECTION 0 — ప్రస్తావన పరిచయం మరియు మూలం
    # ══════════════════════════════════════════

    # Easy
    (0, 1,
     "భారత రాజ్యాంగ ప్రస్తావన (Preamble) ఏ దేశం రాజ్యాంగం నుండి స్ఫూర్తి పొందింది?",
     "UK", "Ireland", "USA", "France",
     "c",
     "భారత రాజ్యాంగ ప్రస్తావన (Preamble) USA రాజ్యాంగం యొక్క ప్రస్తావన నుండి స్ఫూర్తి పొందింది. USA Preamble: 'We the People of the United States...' కానీ భారత ప్రస్తావన మరింత వివరంగా ఉంది."),

    (0, 1,
     "భారత ప్రస్తావన (Preamble) ఆమోదించబడిన తేదీ ఏది?",
     "జనవరి 26, 1950", "ఆగస్ట్ 15, 1947",
     "నవంబర్ 26, 1949", "డిసెంబర్ 9, 1946",
     "c",
     "ప్రస్తావన రాజ్యాంగంతో పాటు నవంబర్ 26, 1949న ఆమోదించబడింది. అందుకే నవంబర్ 26ను 'రాజ్యాంగ దినం (Constitution Day / Samvidhan Diwas)' గా 2015 నుండి జరుపుకుంటున్నారు."),

    (0, 1,
     "భారత ప్రస్తావనకు పూర్వ రూపం అయిన లక్ష్య తీర్మానం (Objective Resolution) ఎవరు ప్రవేశపెట్టారు?",
     "సర్దార్ పటేల్", "డా. B.R. అంబేడ్కర్",
     "జవహర్లాల్ నెహ్రూ", "డా. రాజేంద్ర ప్రసాద్",
     "c",
     "జవహర్లాల్ నెహ్రూ December 13, 1946న లక్ష్య తీర్మానం (Objective Resolution) ప్రవేశపెట్టారు. ఇది January 22, 1947న ఆమోదించారు. ఇదే ప్రస్తావనకు పూర్వ రూపం."),

    # Moderate
    (0, 2,
     "కింది వాటిలో భారత ప్రస్తావన గురించి సరైనవి ఏవి?\n(1) USA ప్రస్తావన నుండి స్ఫూర్తి పొందారు\n(2) Objective Resolution ప్రస్తావనకు పూర్వ రూపం\n(3) ప్రస్తావన జనవరి 26, 1950న ఆమోదించారు\n(4) ప్రస్తావన నవంబర్ 26, 1949న ఆమోదించారు",
     "1, 2 మరియు 4 మాత్రమే", "1, 2 మరియు 3 మాత్రమే",
     "1, 2, 3 మరియు 4 అన్నీ", "2 మరియు 3 మాత్రమే",
     "a",
     "3 తప్పు — ప్రస్తావన నవంబర్ 26, 1949న ఆమోదించారు (4 సరైనది), జనవరి 26, 1950 కాదు. జనవరి 26, 1950 = రాజ్యాంగం అమలులోకి వచ్చిన తేదీ. 1 (USA ✓), 2 (Objective Resolution ✓), 4 (Nov 26 ✓)."),

    (0, 2,
     "భారత ప్రస్తావన (Preamble) తో 'WE, THE PEOPLE OF INDIA' అని మొదలవుతుంది — ఇది ఏమి సూచిస్తుంది?",
     "CA సభ్యులే రాజ్యాంగ అధికారం యొక్క మూలం",
     "భారత ప్రజలే రాజ్యాంగ అధికారం యొక్క చివరి మూలం",
     "రాష్ట్రపతి రాజ్యాంగ అధికారం యొక్క మూలం",
     "పార్లమెంట్ రాజ్యాంగ అధికారం యొక్క మూలం",
     "b",
     "'WE, THE PEOPLE OF INDIA' అంటే రాజ్యాంగానికి అధికారం, సార్వభౌమత్వం భారత ప్రజల నుండే వస్తోంది. ప్రజలే చివరి అధికార మూలం (Ultimate Source of Authority). ఇది ప్రజాస్వామ్య సూత్రానికి మూలం."),

    # Tough
    (0, 3,
     "భారత ప్రస్తావనను 'రాజ్యాంగ నిర్మాతల మనసు తెరిచే తాళం చెవి' అని ఎవరు వర్ణించారు?",
     "K.C. Wheare", "Granville Austin",
     "Ernest Barker", "Jawaharlal Nehru",
     "c",
     "Sir Ernest Barker భారత ప్రస్తావనను 'Key to open the minds of the makers of the Constitution' అని వర్ణించారు. ఆయన పుస్తకానికి ముందు ప్రస్తావన ముద్రించే అభ్యర్థన చేశారు."),

    # Toughest
    (0, 4,
     "అభికథనం-కారణం సరైనవా? / Assertion (A): The Preamble of the Indian Constitution begins with 'WE, THE PEOPLE OF INDIA'.\nReason (R): This phrase signifies that the ultimate source of authority in India is the people, not any external power or the Constituent Assembly.",
     "A మరియు R రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "A మరియు R రెండూ సరైనవి, కానీ R వివరణ కాదు",
     "A సరైనది, R తప్పు",
     "A తప్పు, R సరైనది",
     "a",
     "'WE, THE PEOPLE OF INDIA' (A — correct) — ఈ మాటలు భారత సార్వభౌమత్వం ప్రజల నుండే అని సూచిస్తాయి (R — correct and directly explains A). CA సభ్యులు ప్రజల ప్రతినిధులుగా రాజ్యాంగం రాశారు."),

    # PYQ — APPSC
    (0, 2,
     "భారత రాజ్యాంగ ప్రస్తావనలో 'మేము, భారత ప్రజలు' (WE, THE PEOPLE OF INDIA) అని ఎందుకు మొదలవుతుంది? [APPSC Group 2]",
     "CA సభ్యులే రాజ్యాంగం రాశారు కాబట్టి",
     "ప్రధానమంత్రి అధికారానికి ప్రతీక కాబట్టి",
     "సార్వభౌమత్వం ప్రజలలో ఉందని చూపడానికి",
     "రాజ్యాంగం ప్రజలకు అందించడానికి",
     "c",
     "'WE, THE PEOPLE' — రాజ్యాంగ అధికారం, సార్వభౌమత్వం ప్రజల నుండే వస్తోంది. ఇది ప్రజాస్వామ్యం యొక్క మూల సూత్రం. APPSC Group 2 లో ఇది తరచుగా వచ్చే ప్రశ్న.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 1 — సార్వభౌమత, సమాజవాదం, లౌకికత
    # ══════════════════════════════════════════

    # Easy
    (1, 1,
     "భారత ప్రస్తావనలో 'Socialist' మరియు 'Secular' పదాలు ఏ రాజ్యాంగ సవరణ ద్వారా చేర్చారు?",
     "40వ సవరణ 1975", "42వ సవరణ 1976",
     "44వ సవరణ 1978", "52వ సవరణ 1985",
     "b",
     "42వ రాజ్యాంగ సవరణ 1976 ద్వారా ప్రస్తావనలో 'Socialist' మరియు 'Secular' పదాలు చేర్చారు. ఈ సవరణను 'Mini Constitution' అంటారు ఎందుకంటే ఇది అత్యంత ముఖ్యమైన మార్పులు చేసింది."),

    (1, 1,
     "భారత సమాజవాదం (Socialism) ఏ రకానిది?",
     "సోవియట్ కమ్యూనిస్ట్ సమాజవాదం",
     "ప్రజాస్వామ్య సమాజవాదం (Democratic Socialism) — మిశ్రమ ఆర్థిక వ్యవస్థ",
     "పూర్తి జాతీయీకరణ సమాజవాదం",
     "మార్క్సిస్ట్ సమాజవాదం",
     "b",
     "భారత సమాజవాదం = ప్రజాస్వామ్య సమాజవాదం (Democratic Socialism) — అంటే మిశ్రమ ఆర్థిక వ్యవస్థ (Mixed Economy). పూర్తి జాతీయీకరణ కాదు. ప్రభుత్వ మరియు ప్రైవేట్ రంగాలు రెండూ ఉంటాయి."),

    (1, 1,
     "భారత రాజ్యాంగ ప్రస్తావనలో 'Sovereign' అంటే ఏమిటి?",
     "భారతదేశం UN కు లోబడి ఉంటుంది",
     "భారతదేశం ఏ బాహ్య శక్తికి లోబడదు — స్వతంత్ర విదేశీ విధానం",
     "భారతదేశం రాజ్యాంగ రాజ్యం",
     "భారత రాష్ట్రపతి సర్వోన్నత అధికారి",
     "b",
     "Sovereign అంటే భారతదేశం ఏ బాహ్య శక్తికి (వేరే దేశానికి లేదా సంస్థకు) లోబడదు. స్వతంత్ర విదేశీ విధానం నిర్ణయించుకుంటుంది. UN సభ్యత్వం స్వచ్ఛందంగా అంగీకరించారు — అది Sovereignty ని దెబ్బ తీయదు."),

    # Moderate
    (1, 2,
     "కింది వాటిలో 'Secular' రాజ్యం గురించి భారత సందర్భంలో సరైనది ఏది?",
     "ప్రభుత్వం అన్ని మతాలను నిషేధిస్తుంది",
     "ప్రభుత్వానికి హిందూ మతం అధికారిక మతం",
     "ప్రభుత్వానికి అధికారిక మతం లేదు; అన్ని మతాలకు సమాన గౌరవం",
     "పౌరులకు మతం ఆచరించే స్వేచ్ఛ లేదు",
     "c",
     "భారత 'Secular' అంటే రాజ్యానికి అధికారిక మతం లేదు. అన్ని మతాలకు సమాన గౌరవం. ఇది 'Positive Secularism' — మతాన్ని నిరోధించదు, అన్నిటిని గౌరవిస్తుంది. 42వ సవరణ 1976 ద్వారా Preamble లో చేర్చారు."),

    (1, 2,
     "మూల ప్రస్తావనలో (1949) ఏ పదాలు లేవు?\n(Which words were NOT in the original Preamble of 1949?)",
     "Sovereign మరియు Democratic",
     "Socialist మరియు Secular",
     "Republic మరియు Justice",
     "Liberty మరియు Equality",
     "b",
     "మూల ప్రస్తావన (1949): Sovereign Democratic Republic — Socialist మరియు Secular పదాలు లేవు. 42వ సవరణ 1976 ద్వారా Socialist మరియు Secular చేర్చారు. 'Integrity' కూడా అప్పుడే చేర్చారు."),

    # Tough
    (1, 3,
     "కింది వాటిలో సరైన వర్గీకరణ ఏది?\n(1) Sovereign — బాహ్య నియంత్రణ నుండి స్వేచ్ఛ\n(2) Socialist — ప్రజాస్వామ్య సమాజవాదం (Mixed Economy)\n(3) Secular — హిందూ రాజ్యం\n(4) Democratic — ప్రజాభిప్రాయ పాలన",
     "1, 2 మరియు 4 మాత్రమే సరైనవి", "1, 3 మరియు 4 సరైనవి",
     "1, 2, 3 మరియు 4 అన్నీ", "2 మరియు 3 మాత్రమే",
     "a",
     "3 తప్పు — Secular అంటే హిందూ రాజ్యం కాదు, అన్ని మతాలకు సమాన గౌరవం. 1 (Sovereign ✓), 2 (Democratic Socialism ✓), 4 (Democratic ✓) సరైనవి."),

    # Toughest
    (1, 4,
     "కింది జంటలు అన్నీ సరైనవేనా?\n(1) 'Socialist' పదం — 42వ సవరణ 1976 ద్వారా చేర్చారు\n(2) 'Secular' పదం — 42వ సవరణ 1976 ద్వారా చేర్చారు\n(3) 'Sovereign' పదం — 42వ సవరణ 1976 ద్వారా చేర్చారు\n(4) 'Integrity' పదం — 42వ సవరణ 1976 ద్వారా చేర్చారు",
     "1, 2 మరియు 4 మాత్రమే సరైనవి", "1, 2, 3 మరియు 4 అన్నీ",
     "2 మరియు 3 మాత్రమే", "3 మరియు 4 మాత్రమే",
     "a",
     "3 తప్పు — 'Sovereign' మూల ప్రస్తావన (1949) లోనే ఉంది; 42వ సవరణ ద్వారా చేర్చలేదు. 1 (Socialist ✓), 2 (Secular ✓), 4 (Integrity ✓) — ఈ మూడూ 42వ సవరణ 1976 ద్వారా చేర్చారు."),

    # PYQ — UPSC
    (1, 2,
     "42వ సవరణ ద్వారా పీఠికకు ఏ పదాలు జోడించారు? / Which words were added to the Preamble of the Indian Constitution by the 42nd Constitutional Amendment Act, 1976? [UPSC Style]",
     "Sovereign and Democratic",
     "Republic and Justice",
     "Socialist, Secular and Integrity",
     "Liberty, Equality and Fraternity",
     "c",
     "42వ రాజ్యాంగ సవరణ 1976 ద్వారా మూడు పదాలు చేర్చారు: Socialist, Secular, మరియు Integrity. ఈ మూడూ పరీక్షలలో చాలా తరచుగా అడుగుతారు. మూల ప్రస్తావనలో Sovereign, Democratic, Republic, Justice, Liberty, Equality, Fraternity ఉన్నాయి.",
     "UPSC"),

    # ══════════════════════════════════════════
    # SECTION 2 — ప్రజాస్వామ్యం మరియు గణతంత్రం
    # ══════════════════════════════════════════

    # Easy
    (2, 1,
     "భారత రాజ్యాంగ ప్రస్తావనలో 'Republic' అంటే ఏమిటి?",
     "రాజ్యాధినేత వంశపారంపర్య రాజు",
     "రాజ్యాధినేత ఎన్నికైన వ్యక్తి (Elected Head of State)",
     "పార్లమెంట్ సర్వోన్నతం",
     "రాజ్యాంగం సర్వోన్నతం",
     "b",
     "Republic అంటే రాజ్యాధినేత ఎన్నికైన వ్యక్తి. భారత రాష్ట్రపతి 5 సంవత్సరాలకు ఒకసారి ఎన్నికవుతారు. UK లో రాజు/రాణి వంశపారంపర్యంగా వస్తారు కాబట్టి UK Republic కాదు. India Republic."),

    (2, 1,
     "UK ప్రజాస్వామ్య దేశమే — కానీ Republic కాదు. ఎందుకు?",
     "UK కి రాజ్యాంగం లేదు",
     "UK కి పార్లమెంట్ లేదు",
     "UK లో రాజ్యాధినేత వంశపారంపర్య రాజు/రాణి — Elected కాదు",
     "UK కి Sovereign లేదు",
     "c",
     "UK అనేది Constitutional Monarchy — రాజ్యాధినేత వంశపారంపర్య రాజు/రాణి. కానీ Republic కాదు ఎందుకంటే Head of State ఎన్నికైన వ్యక్తి కాదు. India, USA, France = Republics (elected head). UK = Democracy but not Republic."),

    (2, 1,
     "ప్రజాస్వామ్యం (Democracy) అంటే ఏమిటి?",
     "రాజ్యాంగం సర్వోన్నతం",
     "ఒక వ్యక్తి పాలన",
     "ప్రజల యొక్క, ప్రజలచే, ప్రజల కోసం పాలన",
     "మతాధికారుల పాలన",
     "c",
     "ప్రజాస్వామ్యం (Democracy) = 'Government of the people, by the people, for the people' — Abraham Lincoln. భారత ప్రజాస్వామ్యం = పరోక్ష / ప్రాతినిధ్య ప్రజాస్వామ్యం (Indirect / Representative Democracy)."),

    # Moderate
    (2, 2,
     "భారత ప్రజాస్వామ్యం ఏ రకానిది?",
     "ప్రత్యక్ష ప్రజాస్వామ్యం (Direct Democracy — Switzerland లాగా)",
     "పరోక్ష / ప్రాతినిధ్య ప్రజాస్వామ్యం (Indirect / Representative Democracy)",
     "మతాధార ప్రజాస్వామ్యం",
     "అధ్యక్ష ప్రజాస్వామ్యం",
     "b",
     "భారత ప్రజాస్వామ్యం = పరోక్ష / ప్రాతినిధ్య ప్రజాస్వామ్యం. ప్రజలు నేరుగా పాలించరు — ప్రతినిధులను ఎన్నుకుంటారు (MPs, MLAs). Switzerland లో ప్రత్యక్ష ప్రజాస్వామ్యం కొంతవరకు ఉంది."),

    (2, 2,
     "కింది దేశాల్లో 'Republic' కానిది ఏది?",
     "India", "USA", "UK", "France",
     "c",
     "UK Republic కాదు — Constitutional Monarchy. రాజు/రాణి వంశపారంపర్యంగా వస్తారు. India, USA, France — Republics, ఎందుకంటే అక్కడ Head of State ఎన్నికైన వ్యక్తి."),

    # Tough
    (2, 3,
     "ప్రజాస్వామ్య గణతంత్రం (Democratic Republic) అంటే ఏమిటి?",
     "పార్లమెంట్ అధికారం + వంశపారంపర్య రాజు",
     "ప్రజల ప్రాతినిధ్య పాలన + ఎన్నికైన రాజ్యాధినేత",
     "న్యాయవ్యవస్థ నేతృత్వంలో పాలన",
     "మతాధికారుల పాలన",
     "b",
     "Democratic = ప్రజాభిప్రాయ పాలన. Republic = ఎన్నికైన రాజ్యాధినేత. రెండూ కలిసిన India = Democratic Republic. పార్లమెంటరీ Democratic Republic (PM నిజమైన కార్యనిర్వాహకుడు, President నామమాత్రుడు)."),

    # Toughest
    (2, 4,
     "అభికథనం-కారణం సరైనవా? / Assertion (A): India is a Democratic Republic.\nReason (R): In India, the Head of State (President) is elected for a fixed term, and the government derives its authority from the will of the people expressed through elections.",
     "A మరియు R రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "A మరియు R రెండూ సరైనవి, కానీ R వివరణ కాదు",
     "A సరైనది, R తప్పు",
     "A తప్పు, R సరైనది",
     "a",
     "India Democratic Republic (A — correct). President ఎన్నికవుతారు (Republic), ప్రజాభిప్రాయం ద్వారా పాలన (Democratic) — R అనేది రెండు అంశాలను వివరిస్తుంది. R — correct and explains A."),

    # PYQ — APPSC
    (2, 2,
     "భారత రాజ్యాంగ ప్రస్తావనలో 'Republic' అనే మాట ఏమి సూచిస్తుంది? [APPSC Group 2]",
     "భారత రాష్ట్రపతి వంశపారంపర్య అధినేత",
     "రాజ్యాంగం సర్వోన్నతం",
     "రాష్ట్రపతి ఎన్నికైన రాజ్యాధినేత — వంశపారంపర్యుడు కాదు",
     "ప్రధానమంత్రి నేరుగా ప్రజలచే ఎన్నికవుతారు",
     "c",
     "Republic అంటే రాష్ట్రపతి ఎన్నికైన రాజ్యాధినేత — వంశపారంపర్యంగా పదవి రాదు. UK లో రాజు/రాణి వంశపారంపర్యంగా వస్తారు కాబట్టి UK Republic కాదు. APPSC Group 2 లో ఇది తరచుగా వచ్చే ప్రశ్న.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 3 — న్యాయం, స్వేచ్ఛ, సమానత్వం
    # ══════════════════════════════════════════

    # Easy
    (3, 1,
     "భారత ప్రస్తావనలో 'న్యాయం (Justice)' ఎన్ని రకాలు పేర్కొన్నారు?",
     "రెండు — సామాజిక మరియు ఆర్థిక",
     "మూడు — సామాజిక, ఆర్థిక, రాజకీయ",
     "నాలుగు — సామాజిక, ఆర్థిక, రాజకీయ, న్యాయపర",
     "ఒకటి — సార్వత్రిక న్యాయం",
     "b",
     "భారత ప్రస్తావనలో మూడు రకాల న్యాయం: సామాజిక (Social), ఆర్థిక (Economic), రాజకీయ (Political). సామాజిక న్యాయం = కులం, మతం, లింగ వివక్ష నిర్మూలన. ఆర్థిక = సంపద సమానత. రాజకీయ = ఓటు హక్కు."),

    (3, 1,
     "భారత ప్రస్తావనలో 'స్వేచ్ఛ (Liberty)' ఎన్ని రకాలు పేర్కొన్నారు?",
     "మూడు", "నాలుగు", "ఐదు", "ఆరు",
     "c",
     "ప్రస్తావనలో 5 రకాల స్వేచ్ఛ: Thought (ఆలోచన), Expression (వ్యక్తీకరణ), Belief (విశ్వాసం), Faith (మత విశ్వాసం), Worship (ఆరాధన). ఇవి FR లో Article 19 (Expression), Article 25 (Religion) తో సంబంధం ఉన్నాయి."),

    (3, 1,
     "భారత ప్రస్తావనలో 'సమానత్వం (Equality)' ఎన్ని రకాలు పేర్కొన్నారు?",
     "మూడు — హోదా, అవకాశం, ఆర్థిక",
     "రెండు — హోదాలో సమానత్వం మరియు అవకాశాల్లో సమానత్వం",
     "ఒకటి — సార్వత్రిక సమానత్వం",
     "నాలుగు — సామాజిక, ఆర్థిక, రాజకీయ, న్యాయపర",
     "b",
     "ప్రస్తావనలో 2 రకాల సమానత్వం: హోదాలో సమానత్వం (Equality of Status) మరియు అవకాశాల్లో సమానత్వం (Equality of Opportunity). ఇవి FR లో Articles 14-18 తో సంబంధం ఉన్నాయి."),

    # Moderate
    (3, 2,
     "కింది వాటిలో ప్రస్తావనలో పేర్కొన్న 'Liberty' (స్వేచ్ఛ) రకాలు ఏవి?\n(1) Thought\n(2) Expression\n(3) Belief\n(4) Faith\n(5) Worship",
     "1, 2 మరియు 3 మాత్రమే", "1, 2, 3 మరియు 4 మాత్రమే",
     "1, 2, 3, 4 మరియు 5 అన్నీ", "2 మరియు 5 మాత్రమే",
     "c",
     "ప్రస్తావనలో 5 రకాల Liberty అన్నీ ఉన్నాయి: Thought, Expression, Belief, Faith, Worship. ఇవన్నీ కలిసి వ్యక్తి స్వేచ్ఛ యొక్క వివిధ కోణాలను సూచిస్తాయి."),

    (3, 2,
     "కింది వాటిలో ప్రస్తావనలో 'సామాజిక న్యాయం (Social Justice)' కి చెందిన అంశాలు ఏవి?",
     "ఓటు హక్కు మరియు పదవులకు అవకాశం",
     "సంపద పంపిణీలో సమానత్వం",
     "కులం, మతం, లింగ వివక్ష నిర్మూలన",
     "ఉత్పత్తి సాధనాల జాతీయీకరణ",
     "c",
     "సామాజిక న్యాయం (Social Justice) = కులం, మతం, లింగ వివక్ష నిర్మూలన, అందరికి సమాన అవకాశాలు. ఆర్థిక న్యాయం = సంపద పంపిణీ. రాజకీయ న్యాయం = ఓటు హక్కు, పదవులకు అవకాశం."),

    # Tough
    (3, 3,
     "భారత ప్రస్తావన Justice, Liberty, Equality, Fraternity అనే భావాలు ఏ చారిత్రాత్మక సంఘటన నుండి స్ఫూర్తి పొందాయి?",
     "అమెరికా స్వాతంత్ర్య ప్రకటన 1776",
     "ఫ్రాన్స్ విప్లవం 1789 (Liberty, Equality, Fraternity)",
     "రష్యా విప్లవం 1917",
     "UN మానవ హక్కుల ప్రకటన 1948",
     "b",
     "ఫ్రాన్స్ విప్లవం 1789 నినాదం: Liberté (స్వేచ్ఛ) - Égalité (సమానత్వం) - Fraternité (సోదరభావం). భారత ప్రస్తావనలో Justice, Liberty, Equality, Fraternity అనే భావాలు ఈ నినాదం నుండి స్ఫూర్తి పొందాయి."),

    # Toughest
    (3, 4,
     "కింది జంటలు అన్నీ సరైనవేనా?\n(1) Justice — Social, Economic, Political\n(2) Liberty — Thought, Expression, Belief, Faith, Worship\n(3) Equality — Status, Opportunity, Economic\n(4) Fraternity — Dignity, Unity and Integrity",
     "1, 2 మరియు 4 మాత్రమే సరైనవి", "1, 2, 3 మరియు 4 అన్నీ",
     "2 మరియు 3 మాత్రమే", "1 మరియు 4 మాత్రమే",
     "a",
     "3 తప్పు — Equality రెండు రకాలు మాత్రమే: Status మరియు Opportunity. Economic Equality ప్రస్తావనలో లేదు (ఆర్థిక న్యాయం = Justice లో ఉంది). 1 (✓), 2 (✓), 4 (✓) సరైనవి."),

    # PYQ — UPSC
    (3, 2,
     "పీఠికలో న్యాయం రకాలు ఏమేమి? / The Preamble of the Indian Constitution mentions 'Justice'. Which of the following are the types of Justice mentioned? [UPSC Style]",
     "Social and Economic only",
     "Social, Economic and Political",
     "Social, Economic, Political and Judicial",
     "Economic and Political only",
     "b",
     "ప్రస్తావనలో మూడు రకాల Justice: Social, Economic, Political. Judicial Justice ప్రస్తావనలో లేదు. ఈ మూడు రకాలు DPSP లో Article 38 తో సంబంధం ఉన్నాయి — సమాజ ఆర్థిక న్యాయం.",
     "UPSC"),

    # ══════════════════════════════════════════
    # SECTION 4 — సోదరభావం (Bilingual)
    # ══════════════════════════════════════════

    # Easy — Bilingual
    (4, 1,
     "భారత ప్రస్తావనలో 'Fraternity' (సోదరభావం) ఏమి నిర్థారిస్తుంది?\n(What does Fraternity in the Preamble assure?)",
     "ఆర్థిక సమానత్వం మాత్రమే / Only economic equality",
     "వ్యక్తి గౌరవం మరియు దేశ ఐక్యత మరియు సమగ్రత / Dignity of individual and Unity and Integrity of Nation",
     "రాజకీయ హక్కులు మాత్రమే / Only political rights",
     "మత స్వేచ్ఛ మాత్రమే / Only religious freedom",
     "b",
     "Fraternity (సోదరభావం) రెండు అంశాలు నిర్థారిస్తుంది: వ్యక్తి గౌరవం (Dignity of the Individual) మరియు దేశ ఐక్యత మరియు సమగ్రత (Unity and Integrity of the Nation). ఇవి ఒకదానిపై ఒకటి ఆధారపడతాయి."),

    (4, 1,
     "ప్రస్తావనలో 'Unity and Integrity of the Nation' లో 'Integrity' పదం ఏ సవరణ ద్వారా చేర్చారు?\n(Which amendment added 'Integrity' to 'Unity of the Nation' in the Preamble?)",
     "40వ సవరణ / 40th Amendment",
     "42వ సవరణ 1976 / 42nd Amendment 1976",
     "44వ సవరణ / 44th Amendment",
     "86వ సవరణ / 86th Amendment",
     "b",
     "మూల ప్రస్తావనలో 'Unity of the Nation' ఉండేది. 42వ రాజ్యాంగ సవరణ 1976 ద్వారా 'Unity and Integrity of the Nation' గా మార్చారు. 'Integrity' అంటే దేశ సమగ్రత — విభజన నిరోధం."),

    # Moderate — Bilingual
    (4, 2,
     "Dr. Ambedkar Fraternity గురించి ఏమన్నారు?\n(What did Dr. Ambedkar say about Fraternity?)",
     "Fraternity = ఆర్థిక సమానత్వం / Fraternity = Economic equality",
     "Fraternity means a sense of common brotherhood of all Indians / సోదరభావం అంటే అందరు భారతీయులు సహోదరులు అనే భావన",
     "Fraternity = జాతీయవాదం / Fraternity = Nationalism",
     "Fraternity = మత సహనం మాత్రమే / Fraternity = Religious tolerance only",
     "b",
     "Dr. Ambedkar: 'Fraternity means a sense of common brotherhood of all Indians.' అన్ని కులాలు, మతాలు, భాషలు ఉన్నా అందరూ ఒకే సోదరత్వంలో ఉండాలని Ambedkar ఆశించారు."),

    (4, 2,
     "కింది వాటిలో 'Fraternity' గురించి సరైనవి ఏవి?\n(1) వ్యక్తి గౌరవాన్ని నిర్థారిస్తుంది\n(2) దేశ ఐక్యత మరియు సమగ్రత నిర్థారిస్తుంది\n(3) 'Integrity' పదం 42వ సవరణ 1976 ద్వారా చేర్చారు\n(4) Fraternity = ఆర్థిక సమానత్వం",
     "1, 2 మరియు 3 మాత్రమే / 1, 2 and 3 only",
     "1, 2, 3 మరియు 4 అన్నీ / All",
     "2 మరియు 4 మాత్రమే / 2 and 4 only",
     "1 మరియు 4 మాత్రమే / 1 and 4 only",
     "a",
     "4 తప్పు — Fraternity = సోదరభావం (Common Brotherhood), ఆర్థిక సమానత్వం కాదు. ఆర్థిక సమానత్వం = Justice (Economic). 1 (Dignity ✓), 2 (Unity+Integrity ✓), 3 (42nd Amendment ✓)."),

    # Tough — Bilingual
    (4, 3,
     "Assertion (A): Fraternity in the Preamble aims to promote a sense of brotherhood among all citizens.\nReason (R): Without Fraternity, Liberty and Equality remain empty ideals — as Dr. Ambedkar pointed out, Liberty without Fraternity would lead to inequality.\n(రెండూ నిజమేనా?)",
     "A మరియు R రెండూ సరైనవి, R అనేది A కి సరైన వివరణ / Both correct, R explains A",
     "A మరియు R రెండూ సరైనవి, కానీ R వివరణ కాదు / Both correct, R doesn't explain",
     "A సరైనది, R తప్పు / A correct, R wrong",
     "A తప్పు, R సరైనది / A wrong, R correct",
     "a",
     "Fraternity = సోదరభావం / Brotherhood (A — correct). Ambedkar Fraternity లేకుండా Liberty అర్థం కోల్పోతుందని హెచ్చరించారు (R — correct and explains why Fraternity is essential)."),

    # Toughest — Bilingual
    (4, 4,
     "కింది ప్రస్తావన పదాల వర్గీకరణ సరైనదా?\n(Is the classification of Preamble terms correct?)\n(1) Sovereign, Socialist, Secular, Democratic, Republic — దేశ స్వభావం\n(2) Justice, Liberty, Equality, Fraternity — పౌరులకు లక్ష్యాలు\n(3) 'We, the People' — ప్రజలే అధికార మూలం\n(4) November 26, 1949 — రాజ్యాంగం అమలులోకి వచ్చిన తేదీ",
     "1, 2 మరియు 3 మాత్రమే సరైనవి / 1, 2 and 3 only",
     "1, 2, 3 మరియు 4 అన్నీ సరైనవి / All correct",
     "2 మరియు 4 మాత్రమే / 2 and 4 only",
     "1 మరియు 4 మాత్రమే / 1 and 4 only",
     "a",
     "4 తప్పు — November 26, 1949 = రాజ్యాంగం ఆమోదించిన తేదీ (Adopted), అమలులోకి వచ్చింది January 26, 1950. 1 (దేశ స్వభావం ✓), 2 (పౌరుల లక్ష్యాలు ✓), 3 (ప్రజాస్వామ్య మూలం ✓)."),

    # PYQ — APPSC Bilingual
    (4, 2,
     "భారత ప్రస్తావనలో 'Fraternity' వల్ల ఏమి నిర్థారిస్తారు? [APPSC Group 2]",
     "ఆర్థిక అభివృద్ధి మాత్రమే",
     "వ్యక్తి గౌరవం మరియు దేశ ఐక్యత-సమగ్రత",
     "రాజకీయ స్వేచ్ఛ మాత్రమే",
     "మత స్వేచ్ఛ మాత్రమే",
     "b",
     "Fraternity రెండు లక్ష్యాలు: వ్యక్తి గౌరవం (Dignity of Individual) + దేశ ఐక్యత మరియు సమగ్రత (Unity and Integrity of Nation). 'Integrity' పదం 42వ సవరణ 1976 ద్వారా చేర్చారు. APPSC Group 2 లో ఇది తరచుగా వచ్చే ప్రశ్న.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 5 — 42వ సవరణ మరియు సవరణ సాధ్యత (Bilingual)
    # ══════════════════════════════════════════

    # Easy — Bilingual
    (5, 1,
     "ప్రస్తావన (Preamble) ఇప్పటివరకు ఎన్నిసార్లు సవరించారు?\n(How many times has the Preamble been amended so far?)",
     "రెండు సార్లు / Twice",
     "ఒక్కసారి / Once",
     "మూడు సార్లు / Three times",
     "ఎప్పుడూ సవరించలేదు / Never amended",
     "b",
     "ప్రస్తావన ఇప్పటివరకు ఒక్కసారి మాత్రమే సవరించారు — 42వ రాజ్యాంగ సవరణ 1976 ద్వారా. Socialist, Secular, Integrity చేర్చారు. మరే ఇతర సవరణ చేయలేదు."),

    (5, 1,
     "42వ రాజ్యాంగ సవరణ 1976 కు 'Mini Constitution' అని ఎందుకు అంటారు?\n(Why is the 42nd Amendment 1976 called 'Mini Constitution'?)",
     "ఇది చాలా చిన్న సవరణ కాబట్టి",
     "ఇది రాజ్యాంగంలో చాలా అంశాలను మార్చింది కాబట్టి",
     "ఇది కేవలం ప్రస్తావన మార్చింది కాబట్టి",
     "ఇది Emergency తో వచ్చింది కాబట్టి",
     "b",
     "42వ సవరణ 1976 — Preamble లో Socialist+Secular+Integrity, Fundamental Duties చేర్చడం, Emergency నిబంధనలు, FR vs DPSP వాదన, Courts అధికారాలు మార్చడం వంటి చాలా అంశాలు మార్చింది. అందుకే 'Mini Constitution'."),

    # Moderate — Bilingual
    (5, 2,
     "ప్రస్తావనను Article 368 కింద సవరించవచ్చా?\n(Can the Preamble be amended under Article 368?)",
     "లేదు, ప్రస్తావన సవరించలేరు / No, Preamble cannot be amended",
     "అవును, కానీ Basic Structure దెబ్బతీయకూడదు / Yes, but Basic Structure cannot be damaged",
     "అవును, పూర్తిగా సవరించవచ్చు / Yes, can be completely amended",
     "లేదు, ప్రస్తావన రాజ్యాంగంలో భాగం కాదు / No, Preamble is not part of Constitution",
     "b",
     "Kesavananda Bharati (1973) తీర్పు ప్రకారం: ప్రస్తావన రాజ్యాంగంలో భాగమే. Article 368 కింద సవరించవచ్చు. కానీ Basic Structure ను దెబ్బతీయకూడదు. 42వ సవరణ 1976 ఈ విధంగానే చేసింది."),

    (5, 2,
     "కింది వాటిలో 42వ సవరణ 1976 ద్వారా ప్రస్తావనలో చేర్చిన అంశాలు ఏవి?\n(1) Socialist\n(2) Secular\n(3) Integrity\n(4) Democratic",
     "1, 2 మరియు 3 మాత్రమే / 1, 2 and 3 only",
     "1, 2, 3 మరియు 4 అన్నీ / All",
     "1 మరియు 2 మాత్రమే / 1 and 2 only",
     "2 మరియు 4 మాత్రమే / 2 and 4 only",
     "a",
     "4 తప్పు — 'Democratic' మూల ప్రస్తావన (1949) లోనే ఉంది. 42వ సవరణ 1976 ద్వారా మూడు పదాలు మాత్రమే చేర్చారు: Socialist (1), Secular (2), Integrity (3)."),

    # Tough — Bilingual
    (5, 3,
     "Basic Structure Doctrine ఏ కేసులో ప్రకటించారు?\n(In which case was the Basic Structure Doctrine propounded?)",
     "Berubari Union Case 1960",
     "Golaknath Case 1967",
     "Kesavananda Bharati v. State of Kerala 1973",
     "Minerva Mills Case 1980",
     "c",
     "Kesavananda Bharati v. State of Kerala (1973) — 13 మంది జడ్జీలు (Largest ever constitutional bench). Basic Structure Doctrine: Parliament రాజ్యాంగం యొక్క Basic Structure ను సవరించలేదు. ప్రస్తావన రాజ్యాంగంలో భాగమని కూడా నిర్ధారించారు."),

    # Toughest — Bilingual
    (5, 4,
     "కింది కేసులను వాటి తీర్పులతో సరిగ్గా జోడించండి:\n(P) Berubari Union Case 1960 — (1) Preamble is part of Constitution\n(Q) Kesavananda Bharati 1973 — (2) Preamble is NOT part of Constitution\n(R) LIC of India Case 1995 — (3) Basic Structure Doctrine + Preamble is part\n(S) Golaknath Case 1967 — (4) Parliament cannot amend FR",
     "P-2, Q-3, R-1, S-4", "P-1, Q-2, R-3, S-4",
     "P-3, Q-1, R-2, S-4", "P-2, Q-1, R-3, S-4",
     "a",
     "Berubari 1960 = Preamble రాజ్యాంగంలో భాగం కాదు (P-2). Kesavananda 1973 = Basic Structure + Preamble is part (Q-3). LIC 1995 = Preamble is part నిర్ధారణ (R-1). Golaknath 1967 = Parliament cannot amend FR (S-4)."),

    # PYQ — UPSC Bilingual
    (5, 2,
     "పీఠిక రాజ్యాంగంలో భాగమని ఏ కేసులో తేల్చారు? / In which case did the Supreme Court rule that the Preamble is a part of the Constitution? [UPSC Style]",
     "Berubari Union Case 1960",
     "Golaknath Case 1967",
     "Kesavananda Bharati Case 1973",
     "Minerva Mills Case 1980",
     "c",
     "Kesavananda Bharati v. State of Kerala (1973) — సుప్రీం కోర్టు Preamble రాజ్యాంగంలో భాగమని నిర్ధారించింది. Berubari 1960 లో Preamble భాగం కాదు అన్నారు — అది Kesavananda తో మారిపోయింది. Basic Structure Doctrine కూడా ఈ కేసులోనే వచ్చింది.",
     "UPSC"),

    # ══════════════════════════════════════════
    # SECTION 6 — ప్రస్తావన న్యాయపర స్థితి (Bilingual)
    # ══════════════════════════════════════════

    # Easy — Bilingual
    (6, 1,
     "ప్రస్తావన (Preamble) రాజ్యాంగంలో భాగమా? ఏ కేసు తర్వాత నిర్ధారించారు?\n(Is the Preamble part of the Constitution? After which case?)",
     "Berubari Case 1960 తర్వాత నిర్ధారించారు — భాగం కాదు అన్నారు",
     "Kesavananda Bharati Case 1973 తర్వాత నిర్ధారించారు — భాగమే అన్నారు",
     "ఎప్పుడూ నిర్ధారించలేదు",
     "LIC Case 1995 మాత్రమే నిర్ధారించింది",
     "b",
     "Kesavananda Bharati v. State of Kerala (1973): ప్రస్తావన రాజ్యాంగంలో భాగమే. Berubari Union Case (1960) లో భాగం కాదు అన్నారు — ఆ అభిప్రాయాన్ని Kesavananda (1973) మార్చింది."),

    (6, 1,
     "ప్రస్తావన నేరుగా న్యాయస్థానాల ద్వారా అమలు చేయించుకోవచ్చా?\n(Can the Preamble be directly enforced in courts?)",
     "అవును, నేరుగా న్యాయస్థానాల్లో అమలు చేయించుకోవచ్చు",
     "లేదు, నేరుగా న్యాయస్థానాల్లో అమలు చేయించుకోలేరు — కానీ వ్యాఖ్యానానికి ఉపయోగం",
     "అవును, FR వలే అమలు చేయించుకోవచ్చు",
     "లేదు, ప్రస్తావన రాజ్యాంగంలో భాగం కాదు",
     "b",
     "ప్రస్తావన నేరుగా న్యాయస్థానాల్లో అమలు చేయించుకోలేరు. కానీ రాజ్యాంగ వ్యాఖ్యానానికి (Constitutional Interpretation) ఉపయోగపడుతుంది. FR వలే Justiciable కాదు."),

    # Moderate — Bilingual
    (6, 2,
     "ప్రస్తావన ఏ పనికి ఉపయోగపడుతుంది?\n(What purpose does the Preamble serve?)",
     "నేరుగా చట్టపర హక్కులు ఇవ్వడానికి / To grant legal rights directly",
     "రాజ్యాంగ వ్యాఖ్యానానికి మరియు నిర్మాతల ఉద్దేశ్యం అర్థం చేసుకోవడానికి / For constitutional interpretation",
     "అత్యవసర పరిస్థితి విధించడానికి / To impose Emergency",
     "శాసన నిర్మాణానికి నేరుగా ఉపయోగం / For direct legislation",
     "b",
     "ప్రస్తావన: ✅ రాజ్యాంగ వ్యాఖ్యానంలో సహాయం ✅ నిర్మాతల ఉద్దేశ్యం అర్థం చేసుకోవడం ❌ నేరుగా చట్టపర హక్కులు ఇవ్వదు ❌ న్యాయస్థానాల్లో నేరుగా అమలు చేయించుకోలేరు."),

    (6, 2,
     "కింది వాటిలో Berubari Union Case (1960) మరియు Kesavananda Bharati Case (1973) తేడా ఏమిటి?\n(1) Berubari: Preamble రాజ్యాంగంలో భాగం కాదు\n(2) Kesavananda: Preamble రాజ్యాంగంలో భాగమే\n(3) Berubari: Basic Structure Doctrine ప్రకటించారు\n(4) Kesavananda: Basic Structure Doctrine ప్రకటించారు",
     "1, 2 మరియు 4 మాత్రమే సరైనవి / 1, 2 and 4 only",
     "1, 2, 3 మరియు 4 అన్నీ / All",
     "1 మరియు 3 మాత్రమే / 1 and 3 only",
     "2 మరియు 3 మాత్రమే / 2 and 3 only",
     "a",
     "3 తప్పు — Berubari (1960) Preamble రాజ్యాంగంలో భాగం కాదు అన్నారు. Basic Structure Doctrine Kesavananda (1973) లో వచ్చింది. 1 (Berubari ✓), 2 (Kesavananda ✓), 4 (Kesavananda ✓)."),

    # Tough — Bilingual
    (6, 3,
     "Berubari Union Case (1960) మరియు Kesavananda Bharati Case (1973) లో ప్రస్తావన స్థానం గురించి వచ్చిన తీర్పుల మధ్య వ్యత్యాసం ఏమిటి?\n(What is the difference between the two cases regarding Preamble?)",
     "రెండు కేసులలో Preamble భాగమని తేల్చారు",
     "Berubari లో Preamble రాజ్యాంగంలో భాగం కాదు; Kesavananda లో భాగమే అని నిర్ధారించారు",
     "రెండు కేసులలో Preamble భాగం కాదని తేల్చారు",
     "Berubari లో Preamble భాగమే; Kesavananda లో భాగం కాదు",
     "b",
     "Berubari Union Case (1960): Preamble రాజ్యాంగంలో భాగం కాదు; వ్యాఖ్యానానికి మాత్రమే. Kesavananda Bharati (1973): Preamble రాజ్యాంగంలో భాగమే — సవరించవచ్చు కానీ Basic Structure దెబ్బతీయకూడదు."),

    # Toughest — Bilingual
    (6, 4,
     "Assertion (A): The Preamble can be amended by Parliament under Article 368.\nReason (R): In the Kesavananda Bharati case (1973), the Supreme Court held that the Preamble is part of the Constitution, and Parliament may amend it subject to the Basic Structure limitation.\n(రెండూ నిజమేనా?)",
     "A మరియు R రెండూ సరైనవి, R అనేది A కి సరైన వివరణ / Both correct, R explains A",
     "A మరియు R రెండూ సరైనవి, కానీ R వివరణ కాదు / Both correct, R doesn't explain",
     "A సరైనది, R తప్పు / A correct, R wrong",
     "A తప్పు, R సరైనది / A wrong, R correct",
     "a",
     "Preamble సవరించవచ్చు Article 368 కింద (A — correct, 42nd Amendment 1976 ద్వారా నిరూపించారు). Kesavananda 1973 Preamble = part of Constitution + Basic Structure limitation (R — correct and directly explains A)."),

    # PYQ — APPSC Bilingual
    (6, 2,
     "ప్రస్తావన రాజ్యాంగంలో భాగమని మొదట ప్రకటించిన సుప్రీం కోర్టు కేసు ఏది? [APPSC Group 2]",
     "Berubari Union Case 1960",
     "Golaknath Case 1967",
     "Kesavananda Bharati Case 1973",
     "Minerva Mills Case 1980",
     "c",
     "Kesavananda Bharati v. State of Kerala (1973) కేసులో సుప్రీం కోర్టు ప్రస్తావన రాజ్యాంగంలో భాగమని తేల్చింది. Berubari (1960) లో భాగం కాదు అన్నారు. APPSC Group 2 లో ఇది తరచుగా వచ్చే ముఖ్యమైన ప్రశ్న.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 7 — ప్రస్తావన సమగ్ర విశ్లేషణ (Bilingual)
    # ══════════════════════════════════════════

    # Easy — Bilingual
    (7, 1,
     "ప్రస్తావనలో మొత్తం ఎన్ని ముఖ్య 'దేశ స్వభావ' పదాలు (descriptors of Indian State) ఉన్నాయి?\n(How many key terms describe the nature of the Indian State in the Preamble?)",
     "మూడు / Three", "నాలుగు / Four",
     "ఐదు / Five", "ఆరు / Six",
     "c",
     "ఐదు పదాలు దేశ స్వభావాన్ని వివరిస్తాయి: Sovereign, Socialist, Secular, Democratic, Republic. ఇవి అన్నీ 'India is a...' అని సూచిస్తాయి."),

    (7, 1,
     "ప్రస్తావనలో 'Justice' కోసం ఏ మూలం / ఆదర్శం తీసుకున్నారు?\n(Inspiration for 'Justice' in Preamble is from which source?)",
     "USA Bill of Rights",
     "Russian Revolution 1917 (సోవియట్ విప్లవం)",
     "UN Charter",
     "France Revolution (ఫ్రాన్స్ విప్లవం)",
     "b",
     "Russian Revolution 1917 నుండి Social, Economic, Political Justice భావనలు స్ఫూర్తి పొందాయి. ఫ్రాన్స్ విప్లవం నుండి Liberty, Equality, Fraternity వచ్చాయి. ఇవి వేర్వేరు మూలాలు."),

    # Moderate — Bilingual
    (7, 2,
     "ప్రస్తావనలో మొత్తం ఎన్ని లక్ష్యాలు / ఆదర్శాలు పౌరులకు కల్పించాలని చెప్పారు?\n(How many objectives are mentioned to be secured to citizens in the Preamble?)",
     "రెండు — Justice మరియు Liberty",
     "మూడు — Justice, Liberty, Equality",
     "నాలుగు — Justice, Liberty, Equality, Fraternity",
     "ఐదు — Justice, Liberty, Equality, Fraternity, Democracy",
     "c",
     "ప్రస్తావనలో నాలుగు లక్ష్యాలు: Justice (3 రకాలు), Liberty (5 రకాలు), Equality (2 రకాలు), Fraternity (2 అంశాలు). Democracy ప్రత్యేక లక్ష్యం కాదు — అది దేశ స్వభావాన్ని వివరిస్తుంది."),

    (7, 2,
     "కింది వాటిలో ప్రస్తావనకు సంబంధించి సరైనవి ఏవి?\n(1) USA ప్రస్తావన నుండి స్ఫూర్తి పొందారు\n(2) ఒక్కసారి మాత్రమే సవరించారు (42వ సవరణ 1976)\n(3) Berubari (1960) — Preamble రాజ్యాంగంలో భాగమే\n(4) Kesavananda (1973) — Preamble రాజ్యాంగంలో భాగమే",
     "1, 2 మరియు 4 మాత్రమే / 1, 2 and 4 only",
     "1, 2, 3 మరియు 4 అన్నీ / All",
     "3 మరియు 4 మాత్రమే / 3 and 4 only",
     "2 మరియు 3 మాత్రమే / 2 and 3 only",
     "a",
     "3 తప్పు — Berubari (1960) లో Preamble భాగం కాదు అన్నారు. 1 (USA స్ఫూర్తి ✓), 2 (ఒక్కసారి 42nd 1976 ✓), 4 (Kesavananda 1973 — భాగమే ✓)."),

    # Tough — Bilingual
    (7, 3,
     "ప్రస్తావనలో 'Justice' కు సంబంధించి — సామాజిక, ఆర్థిక, రాజకీయ న్యాయాల మధ్య తేడా ఏమిటి?\n(Difference between Social, Economic and Political Justice in the Preamble)",
     "మూడూ ఒకే అర్థం",
     "Social = కులం/మతం వివక్ష తొలగించడం; Economic = సంపద సమానత; Political = ఓటు హక్కు + అవకాశాలు",
     "Social = ఓటు హక్కు; Economic = మతస్వేచ్ఛ; Political = కులం వివక్ష తొలగించడం",
     "Social = రాజకీయ భాగస్వామ్యం; Economic = భూ సంస్కరణలు; Political = పౌర హక్కులు",
     "b",
     "Social Justice = కులం, మతం, లింగ వివక్ష నిర్మూలన, సమాన అవకాశాలు. Economic Justice = సంపద పంపిణీ సమానత, దోపిడీ నిరోధం. Political Justice = ఓటు హక్కు, పదవులకు సమాన అవకాశాలు — ఇవి మూడు వేర్వేరు కోణాలు."),

    # Toughest — Bilingual
    (7, 4,
     "అభికథనం-కారణం సరైనవా? / Assertion (A): The Preamble to the Indian Constitution reflects the ideals and aspirations of the people of India.\nReason (R): The Preamble is based on the Objective Resolution moved by Nehru in 1946, which encapsulated the vision of free India, and was used as a guide in drafting the Constitution.",
     "A మరియు R రెండూ సరైనవి, R అనేది A కి సరైన వివరణ / Both correct, R explains A",
     "A మరియు R రెండూ సరైనవి, కానీ R వివరణ కాదు / Both correct, R doesn't explain",
     "A సరైనది, R తప్పు / A correct, R wrong",
     "A తప్పు, R సరైనది / A wrong, R correct",
     "a",
     "ప్రస్తావన భారత ప్రజల ఆదర్శాలు మరియు ఆశలు ప్రతిఫలిస్తుంది (A — correct). Objective Resolution (December 1946 — Nehru) ప్రస్తావనకు పూర్వ రూపం — రాజ్యాంగ నిర్మాణంలో మార్గదర్శకంగా ఉంది (R — correct and explains A)."),

    # PYQ — UPSC Bilingual
    (7, 2,
     "పీఠిక గురించి సరైన వివరణ ఏది? / Consider the Preamble of the Indian Constitution. Which of the following correctly describes what the Preamble IS and IS NOT? [UPSC Style]",
     "It is enforceable in court and is part of the Constitution",
     "It is part of the Constitution but not directly enforceable in court",
     "It is neither part of the Constitution nor enforceable",
     "It was part of the Constitution until 1973 but removed after Kesavananda",
     "b",
     "ప్రస్తావన రాజ్యాంగంలో భాగమే (Kesavananda 1973). కానీ నేరుగా న్యాయస్థానాల్లో అమలు చేయించుకోలేరు — FR వలే కాదు. రాజ్యాంగ వ్యాఖ్యానానికి ఉపయోగపడుతుంది.",
     "UPSC"),
]


# ─────────────────────────────────────────────
#  SEED FUNCTIONS
# ─────────────────────────────────────────────

def _seed_polity_ch4_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    ph = '%s' if use_postgres else '?'
    try:
        conn.execute("""CREATE TABLE IF NOT EXISTS study_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL DEFAULT 'GK',
            topic TEXT NOT NULL DEFAULT 'Indian_Polity',
            subtopic TEXT DEFAULT '',
            chapter_num INTEGER NOT NULL,
            chapter_title_te TEXT NOT NULL DEFAULT '',
            chapter_title_en TEXT NOT NULL DEFAULT '',
            pages_ref TEXT DEFAULT '',
            sections_json TEXT NOT NULL DEFAULT '[]',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")
        if use_postgres: conn.commit()
    except Exception:
        pass

    cur = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (4, 'Indian_Polity'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True,
                'message': 'Polity Ch4 notes already seeded.'}
    if row and force:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (4, 'Indian_Polity'))
    if use_postgres:
        conn.commit()

    db_exec_fn(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'Indian_Polity', '', 4,
         'రాజ్యాంగ ప్రస్తావన',
         'Preamble of the Constitution',
         'Ch.4',
         _json.dumps(POLITY_CH4_SECTIONS, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'Polity Ch4 notes seeded!'}


def _seed_polity_ch4_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
    ph = '%s' if use_postgres else '?'

    try:
        conn.execute("""CREATE TABLE IF NOT EXISTS chapter_mcqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            study_note_id INTEGER NOT NULL,
            section_idx INTEGER NOT NULL DEFAULT 0,
            difficulty INTEGER NOT NULL DEFAULT 1,
            exam_type TEXT NOT NULL DEFAULT 'General',
            q_te TEXT NOT NULL,
            opt_a TEXT NOT NULL,
            opt_b TEXT NOT NULL,
            opt_c TEXT NOT NULL,
            opt_d TEXT NOT NULL,
            correct TEXT NOT NULL,
            explanation_te TEXT NOT NULL DEFAULT '',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")
        if use_postgres: conn.commit()
    except Exception:
        pass

    cur = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (4, 'Indian_Polity'))
    row = cur.fetchone()
    if not row:
        _seed_polity_ch4_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)
        cur = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (4, 'Indian_Polity'))
        row = cur.fetchone()

    note_id = row_to_dict_fn(row)['id']
    db_exec_fn(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))

    insert_sql = (
        f"INSERT INTO chapter_mcqs "
        f"(study_note_id, section_idx, difficulty, exam_type, "
        f"q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    )

    easy = medium = hard = toughest = pyq = 0
    for mcq in POLITY_CH4_MCQS:
        sec_idx, diff, q, a, b, c, d, correct, expl = mcq[:9]
        exam_type = mcq[9] if len(mcq) > 9 else 'General'
        db_exec_fn(conn, insert_sql,
                   (note_id, sec_idx, diff, exam_type, q, a, b, c, d,
                    str(correct).lower(), expl))
        if exam_type in ('APPSC', 'UPSC'):
            pyq += 1
        elif diff == 1: easy += 1
        elif diff == 2: medium += 1
        elif diff == 3: hard += 1
        elif diff == 4: toughest += 1

    if use_postgres: conn.commit()
    conn.commit()

    total = len(POLITY_CH4_MCQS)
    return {
        'success': True,
        'message': f'Polity Ch4 MCQs seeded! Total: {total}',
        'inserted': total,
        'easy': easy, 'medium': medium, 'hard': hard,
        'toughest': toughest, 'pyq': pyq
    }
