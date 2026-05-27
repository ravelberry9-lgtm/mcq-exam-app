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

    # ══════════════ SECTION 0 — Preamble Overview ══════════════

    (0, 1,
     "From which country's constitution was the Preamble of the Indian Constitution inspired?\nతెలుగు: భారత ప్రస్తావన ఏ దేశ రాజ్యాంగం నుండి స్ఫూర్తి పొందింది?",
     "UK / యూకే",
     "Ireland / ఐర్లాండ్",
     "USA / అమెరికా (correct — 'We the People')",
     "France / ఫ్రాన్స్",
     "c",
     "Indian Preamble was inspired by the USA Constitution which begins with 'We the People of the United States'."),

    (0, 1,
     "On which date was the Indian Preamble adopted?\nతెలుగు: భారత ప్రస్తావన ఆమోదించిన తేదీ ఏది?",
     "January 26, 1950 / జనవరి 26, 1950",
     "August 15, 1947 / ఆగస్ట్ 15, 1947",
     "November 26, 1949 / నవంబర్ 26, 1949 (correct)",
     "December 9, 1946 / డిసెంబర్ 9, 1946",
     "c",
     "The Preamble (along with the rest of the Constitution) was ADOPTED on November 26, 1949. It came into FORCE on January 26, 1950."),

    (0, 1,
     "Who moved the Objective Resolution that became the basis of the Preamble?\nతెలుగు: ప్రస్తావనకు పూర్వ రూపం అయిన లక్ష్య తీర్మానం ఎవరు ప్రవేశపెట్టారు?",
     "Sardar Patel / సర్దార్ పటేల్",
     "Dr. B.R. Ambedkar / అంబేడ్కర్",
     "Jawaharlal Nehru / జవహర్లాల్ నెహ్రూ (correct)",
     "Dr. Rajendra Prasad / రాజేంద్ర ప్రసాద్",
     "c",
     "Nehru moved the Objective Resolution on December 13, 1946. Adopted on January 22, 1947. It became the spirit of the Preamble."),

    (0, 2,
     "Regarding the Indian Preamble, which of the following are CORRECT?\n(1) Inspired by USA Preamble\n(2) Objective Resolution = pre-form of Preamble\n(3) Adopted on January 26, 1950\n(4) Adopted on November 26, 1949\nతెలుగు: కింది వాటిలో భారత ప్రస్తావన గురించి సరైనవి ఏవి?\n(1) USA ప్రస్తావన నుండి స్ఫూర్తి\n(2) Objective Resolution పూర్వ రూపం\n(3) జనవరి 26, 1950న ఆమోదించారు\n(4) నవంబర్ 26, 1949న ఆమోదించారు",
     "1, 2 and 4 only / 1, 2 మరియు 4 మాత్రమే (correct)",
     "1, 2 and 3 only / 1, 2 మరియు 3 మాత్రమే",
     "All four / అన్నీ",
     "2 and 3 only / 2 మరియు 3 మాత్రమే",
     "a",
     "Statements 1, 2, 4 correct. Statement 3 wrong — Preamble was ADOPTED on Nov 26, 1949 (NOT Jan 26, 1950 — that's the commencement date)."),

    (0, 2,
     "The Preamble begins with 'WE, THE PEOPLE OF INDIA' — what does this signify?\nతెలుగు: ప్రస్తావన 'WE, THE PEOPLE OF INDIA' అని మొదలవుతుంది — ఇది ఏమి సూచిస్తుంది?",
     "CA members are the source of constitutional authority / CA సభ్యులు మూలం",
     "People of India are the ultimate source of constitutional authority / భారత ప్రజలే చివరి మూలం (correct)",
     "President is the source / రాష్ట్రపతి మూలం",
     "Parliament is the source / Parliament మూలం",
     "b",
     "'WE, THE PEOPLE OF INDIA' = Popular Sovereignty. The PEOPLE are the ultimate source of all constitutional authority — not any external power, the CA, the King, or any institution."),

    (0, 3,
     "Who described the Preamble as the 'key to open the minds of the makers' of the Constitution?\nతెలుగు: ప్రస్తావనను 'రాజ్యాంగ నిర్మాతల మనసు తెరిచే తాళం చెవి' అని ఎవరు అన్నారు?",
     "K.C. Wheare / K.C. వేర్",
     "Granville Austin / గ్రాన్‌విల్ ఆస్టిన్",
     "Ernest Barker / ఎర్నెస్ట్ బార్కర్ (correct)",
     "Jawaharlal Nehru / నెహ్రూ",
     "c",
     "Sir Ernest Barker famously called the Preamble 'a key to open the minds of the makers' — quoted by him in the foreword to his work 'Principles of Social and Political Theory'."),

    (0, 4,
     "Assertion (A): The Preamble of the Indian Constitution begins with 'WE, THE PEOPLE OF INDIA'.\nReason (R): This phrase signifies that the ultimate source of authority in India is the people, not any external power or the Constituent Assembly.\nతెలుగు: అభికథనం-కారణం సరైనవా?",
     "Both correct, R explains A / రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "Both correct, R doesn't explain / రెండూ సరైనవి, R వివరణ కాదు",
     "A correct, R wrong / A సరైనది, R తప్పు",
     "A wrong, R correct / A తప్పు, R సరైనది",
     "a",
     "Both A and R are correct. R precisely explains A — 'WE THE PEOPLE' is the textual evidence of popular sovereignty."),

    (0, 2,
     "Why does the Preamble begin with 'WE, THE PEOPLE OF INDIA'? [APPSC Group 2]\nతెలుగు: ప్రస్తావనలో 'మేము, భారత ప్రజలు' అని ఎందుకు మొదలవుతుంది?",
     "Because CA members wrote the Constitution / CA సభ్యులే రాశారు",
     "To symbolize PM's authority / ప్రధానమంత్రి అధికారం",
     "To indicate sovereignty rests with the people / సార్వభౌమత్వం ప్రజలలో (correct)",
     "To deliver the Constitution to the people / ప్రజలకు అందించడానికి",
     "c",
     "'WE THE PEOPLE OF INDIA' indicates POPULAR SOVEREIGNTY — that all constitutional authority flows from the people of India.",
     "APPSC"),

    # ══════════════ SECTION 1 — Sovereign, Socialist, Secular, Democratic ══════════════

    (1, 1,
     "Which Constitutional Amendment added 'Socialist' and 'Secular' to the Preamble?\nతెలుగు: 'Socialist' మరియు 'Secular' పదాలు ఏ సవరణ ద్వారా చేర్చారు?",
     "40th Amendment 1975 / 40వ సవరణ",
     "42nd Amendment 1976 / 42వ సవరణ 1976 (correct — Mini Constitution)",
     "44th Amendment 1978 / 44వ సవరణ",
     "52nd Amendment 1985 / 52వ సవరణ",
     "b",
     "42nd Amendment 1976 (Mini Constitution) added three words: SOCIALIST, SECULAR, INTEGRITY. Originally Preamble said 'Sovereign Democratic Republic'."),

    (1, 1,
     "Indian Socialism is which type?\nతెలుగు: భారత సమాజవాదం ఏ రకానిది?",
     "Soviet Communist Socialism / సోవియట్ కమ్యూనిస్ట్",
     "Democratic Socialism — mixed economy / ప్రజాస్వామ్య సమాజవాదం (correct)",
     "Complete nationalization socialism / పూర్తి జాతీయీకరణ",
     "Marxist socialism / మార్క్సిస్ట్",
     "b",
     "India follows DEMOCRATIC SOCIALISM — a mixed economy combining state and private sectors, NOT Marxist/Soviet socialism."),

    (1, 1,
     "What does 'Sovereign' mean in the Preamble?\nతెలుగు: 'Sovereign' అంటే ఏమిటి?",
     "India is subject to UN / UN కు లోబడి",
     "India is not subject to any external power; independent foreign policy / ఏ బాహ్య శక్తికి లోబడదు (correct)",
     "India is constitutional state / రాజ్యాంగ రాజ్యం",
     "President is supreme authority / రాష్ట్రపతి సర్వోన్నతం",
     "b",
     "Sovereign = India is NOT subject to any external power. Free to conduct internal and external affairs independently."),

    (1, 2,
     "Which is correct about a 'Secular' state in the Indian context?\nతెలుగు: 'Secular' రాజ్యం గురించి భారత సందర్భంలో సరైనది?",
     "Government prohibits all religions / అన్ని మతాలను నిషేధం",
     "Hinduism is the official religion / హిందూ మతం అధికారిక",
     "No official religion; equal respect to all religions / అధికారిక మతం లేదు; సమాన గౌరవం (correct)",
     "Citizens have no religious freedom / మతం ఆచరించే స్వేచ్ఛ లేదు",
     "c",
     "Indian Secularism = NO official religion + equal respect/treatment of all religions ('Sarva Dharma Sambhava'). Not the French strict separation, not anti-religious."),

    (1, 2,
     "Which words were NOT in the original Preamble of 1949?\nతెలుగు: మూల ప్రస్తావనలో లేని పదాలు ఏవి?",
     "Sovereign and Democratic / Sovereign + Democratic",
     "Socialist and Secular / Socialist + Secular (correct)",
     "Republic and Justice / Republic + Justice",
     "Liberty and Equality / Liberty + Equality",
     "b",
     "The original 1949 Preamble had: Sovereign Democratic Republic. SOCIALIST + SECULAR were added in 1976 by the 42nd Amendment."),

    (1, 3,
     "Which classification of Preamble terms is CORRECT?\n(1) Sovereign — freedom from external control\n(2) Socialist — democratic socialism (mixed economy)\n(3) Secular — Hindu state\n(4) Democratic — government by public opinion\nతెలుగు: ప్రస్తావన పదాల వర్గీకరణ సరైనది?\n(1) Sovereign — బాహ్య నియంత్రణ నుండి స్వేచ్ఛ\n(2) Socialist — ప్రజాస్వామ్య సమాజవాదం\n(3) Secular — హిందూ రాజ్యం\n(4) Democratic — ప్రజాభిప్రాయ పాలన",
     "1, 2 and 4 only correct / 1, 2 మరియు 4 మాత్రమే సరైనవి (correct)",
     "1, 3 and 4 correct / 1, 3 మరియు 4 సరైనవి",
     "All four / అన్నీ",
     "2 and 3 only / 2 మరియు 3 మాత్రమే",
     "a",
     "Statement 3 is WRONG — Secular = NO official religion (NOT Hindu state). The other three classifications are correct."),

    (1, 4,
     "Are these pairs all correctly matched?\n(1) 'Socialist' added by 42nd Amendment 1976\n(2) 'Secular' added by 42nd Amendment 1976\n(3) 'Sovereign' added by 42nd Amendment 1976\n(4) 'Integrity' added by 42nd Amendment 1976\nతెలుగు: కింది జంటలు అన్నీ సరైనవేనా?\n(1) 'Socialist' — 42వ సవరణ 1976\n(2) 'Secular' — 42వ సవరణ 1976\n(3) 'Sovereign' — 42వ సవరణ 1976\n(4) 'Integrity' — 42వ సవరణ 1976",
     "Only 1, 2 and 4 correct / 1, 2 మరియు 4 మాత్రమే (correct)",
     "All four / అన్నీ",
     "Only 2 and 3 / 2 మరియు 3 మాత్రమే",
     "Only 3 and 4 / 3 మరియు 4 మాత్రమే",
     "a",
     "Pair 3 is WRONG — 'Sovereign' was in the ORIGINAL 1949 Preamble. The 42nd Amendment added Socialist, Secular, and Integrity (NOT Sovereign)."),

    (1, 2,
     "Which words were added to the Preamble by the 42nd Amendment 1976? [UPSC Style]\nతెలుగు: 42వ సవరణ ద్వారా పీఠికకు ఏ పదాలు?",
     "Sovereign and Democratic / Sovereign + Democratic",
     "Republic and Justice / Republic + Justice",
     "Socialist, Secular and Integrity / Socialist + Secular + Integrity (correct)",
     "Liberty, Equality and Fraternity / Liberty + Equality + Fraternity",
     "c",
     "42nd Amendment 1976 added THREE words: Socialist, Secular, Integrity. The other words were in the original Preamble.",
     "UPSC"),

    # ══════════════ SECTION 2 — Republic & Democratic Nature ══════════════

    (2, 1,
     "What does 'Republic' mean in the Indian Preamble?\nతెలుగు: 'Republic' అంటే ఏమిటి?",
     "Hereditary king as head of state / వంశపారంపర్య రాజు",
     "Elected Head of State / ఎన్నికైన రాజ్యాధినేత (correct)",
     "Parliament is supreme / Parliament సర్వోన్నతం",
     "Constitution is supreme / రాజ్యాంగం సర్వోన్నతం",
     "b",
     "Republic = Head of State is ELECTED (President), NOT hereditary. India's President is elected for a 5-year term — unlike UK's hereditary monarch."),

    (2, 1,
     "UK is a democracy but NOT a Republic. Why?\nతెలుగు: UK ప్రజాస్వామ్యమే కానీ Republic కాదు. ఎందుకు?",
     "UK has no Constitution / రాజ్యాంగం లేదు",
     "UK has no Parliament / Parliament లేదు",
     "UK has hereditary monarch as head of state — not elected / రాజ్యాధినేత వంశపారంపర్య (correct)",
     "UK is not Sovereign / Sovereign కాదు",
     "c",
     "UK is a parliamentary DEMOCRACY but a CONSTITUTIONAL MONARCHY (not Republic). King/Queen is hereditary head, not elected. India = elected President = Republic."),

    (2, 1,
     "What does Democracy mean?\nతెలుగు: ప్రజాస్వామ్యం అంటే?",
     "Constitution is supreme / రాజ్యాంగం సర్వోన్నతం",
     "Rule by one person / ఒక వ్యక్తి పాలన",
     "Government of the people, by the people, for the people / ప్రజల యొక్క, ప్రజలచే, ప్రజల కోసం (correct — Lincoln)",
     "Rule by religious clergy / మతాధికారుల పాలన",
     "c",
     "Democracy (Lincoln's definition) = government OF the people, BY the people, FOR the people. India practices representative democracy (indirect)."),

    (2, 2,
     "Which type of democracy does India follow?\nతెలుగు: భారత ప్రజాస్వామ్యం ఏ రకానిది?",
     "Direct Democracy (like Switzerland) / ప్రత్యక్ష (Switzerland)",
     "Indirect / Representative Democracy / పరోక్ష / ప్రాతినిధ్య (correct)",
     "Theocratic Democracy / మతాధార",
     "Presidential Democracy / అధ్యక్ష",
     "b",
     "India = INDIRECT / REPRESENTATIVE Democracy. Citizens elect representatives (MPs/MLAs) who govern on their behalf. Direct democracy (Switzerland) = citizens vote on every issue."),

    (2, 2,
     "Which of the following is NOT a Republic?\nతెలుగు: కింది వాటిలో Republic కానిది?",
     "India / భారత్",
     "USA / అమెరికా",
     "UK / యూకే (correct — constitutional monarchy)",
     "France / ఫ్రాన్స్",
     "c",
     "UK = Constitutional Monarchy (NOT Republic). India, USA, France = Republics with elected heads of state."),

    (2, 3,
     "What does Democratic Republic mean?\nతెలుగు: ప్రజాస్వామ్య గణతంత్రం అంటే ఏమిటి?",
     "Parliamentary authority + hereditary king / Parliament + వంశపారంపర్య రాజు",
     "Representative governance + elected head of state / ప్రజల ప్రాతినిధ్యం + ఎన్నికైన అధినేత (correct)",
     "Judicial governance / న్యాయవ్యవస్థ నేతృత్వం",
     "Theocratic rule / మతాధికారుల పాలన",
     "b",
     "Democratic Republic = (1) Democratic = governance by elected representatives + (2) Republic = elected head of state (President). Both elements together."),

    (2, 4,
     "Assertion (A): India is a Democratic Republic.\nReason (R): In India, the Head of State (President) is elected for a fixed term, and the government derives its authority from the will of the people expressed through elections.\nతెలుగు: అభికథనం-కారణం సరైనవా?",
     "Both correct, R explains A / రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "Both correct, R doesn't explain / రెండూ సరైనవి, R వివరణ కాదు",
     "A correct, R wrong / A సరైనది, R తప్పు",
     "A wrong, R correct / A తప్పు, R సరైనది",
     "a",
     "Both correct, R explains A. The elected President + government deriving authority from people's will = exactly what makes India a Democratic Republic."),

    (2, 2,
     "What does 'Republic' in the Indian Preamble indicate? [APPSC Group 2]\nతెలుగు: 'Republic' ఏమి సూచిస్తుంది?",
     "President is hereditary head / వంశపారంపర్య అధినేత",
     "Constitution is supreme / రాజ్యాంగం సర్వోన్నతం",
     "President is elected head of state — not hereditary / రాష్ట్రపతి ఎన్నికైన (correct)",
     "PM is directly elected by people / PM ప్రత్యక్షంగా ఎన్నిక",
     "c",
     "Republic = elected head of state (NOT hereditary). India's President is elected — making India a Republic.",
     "APPSC"),

    # ══════════════ SECTION 3 — Justice, Liberty, Equality ══════════════

    (3, 1,
     "How many types of Justice are mentioned in the Preamble?\nతెలుగు: 'న్యాయం' ఎన్ని రకాలు?",
     "Two — Social and Economic / రెండు",
     "Three — Social, Economic, Political / మూడు (correct)",
     "Four — Social, Economic, Political, Judicial / నాలుగు",
     "One — Universal / ఒకటి",
     "b",
     "Three types of Justice in Preamble: SOCIAL + ECONOMIC + POLITICAL. Inspired by the Russian Revolution 1917. Judicial Justice is NOT separately listed."),

    (3, 1,
     "How many types of Liberty are mentioned in the Preamble?\nతెలుగు: 'స్వేచ్ఛ' ఎన్ని రకాలు?",
     "Three / మూడు",
     "Four / నాలుగు",
     "Five / ఐదు (correct)",
     "Six / ఆరు",
     "c",
     "FIVE types of Liberty: Thought, Expression, Belief, Faith, Worship — inspired by the French Revolution (1789)."),

    (3, 1,
     "How many types of Equality are mentioned in the Preamble?\nతెలుగు: 'సమానత్వం' ఎన్ని రకాలు?",
     "Three — Status, Opportunity, Economic / మూడు",
     "Two — Equality of Status and Opportunity / రెండు (correct)",
     "One — Universal / ఒకటి",
     "Four / నాలుగు",
     "b",
     "Two types of Equality in Preamble: Equality of STATUS and Equality of OPPORTUNITY. Economic equality is part of DPSP, not Preamble."),

    (3, 2,
     "Which types of Liberty are mentioned in the Preamble?\n(1) Thought\n(2) Expression\n(3) Belief\n(4) Faith\n(5) Worship\nతెలుగు: ప్రస్తావనలో పేర్కొన్న 'Liberty' రకాలు?\n(1) Thought\n(2) Expression\n(3) Belief\n(4) Faith\n(5) Worship",
     "1, 2 and 3 only / 1, 2 మరియు 3 మాత్రమే",
     "1, 2, 3 and 4 only / 1, 2, 3, 4 మాత్రమే",
     "All five / అన్నీ ఐదు (correct)",
     "2 and 5 only / 2 మరియు 5 మాత్రమే",
     "c",
     "All FIVE: Liberty of THOUGHT, EXPRESSION, BELIEF, FAITH, WORSHIP — comprehensive freedom of mind and conscience."),

    (3, 2,
     "Which falls under 'Social Justice' in the Preamble?\nతెలుగు: 'Social Justice' కు చెందిన అంశాలు?",
     "Voting rights and access to office / ఓటు హక్కు, పదవులు",
     "Equal distribution of wealth / సంపద పంపిణీ",
     "Elimination of caste, religion, gender discrimination / కులం, మతం, లింగ వివక్ష నిర్మూలన (correct)",
     "Nationalisation of means of production / జాతీయీకరణ",
     "c",
     "Social Justice = abolishing caste, gender, religion, race-based discrimination. Voting/office = political; wealth distribution = economic."),

    (3, 3,
     "From which historical event were Justice, Liberty, Equality, Fraternity inspired?\nతెలుగు: ప్రస్తావన ఆదర్శాలు ఏ చారిత్రాత్మక సంఘటన నుండి?",
     "American Independence Declaration 1776 / అమెరికా 1776",
     "French Revolution 1789 (Liberty, Equality, Fraternity) / ఫ్రాన్స్ విప్లవం 1789 (correct)",
     "Russian Revolution 1917 / రష్యా విప్లవం",
     "UN Human Rights Declaration 1948 / UN మానవ హక్కులు",
     "b",
     "Liberty, Equality, Fraternity = direct slogans from the FRENCH Revolution (1789). Justice (3 types) inspired by the Russian Revolution 1917."),

    (3, 4,
     "Are these pairs all correctly matched?\n(1) Justice — Social, Economic, Political\n(2) Liberty — Thought, Expression, Belief, Faith, Worship\n(3) Equality — Status, Opportunity, Economic\n(4) Fraternity — Dignity, Unity and Integrity\nతెలుగు: కింది జంటలు అన్నీ సరైనవేనా?\n(1) Justice — Social, Economic, Political\n(2) Liberty — Thought, Expression, Belief, Faith, Worship\n(3) Equality — Status, Opportunity, Economic\n(4) Fraternity — Dignity, Unity and Integrity",
     "Only 1, 2 and 4 correct / 1, 2 మరియు 4 మాత్రమే (correct)",
     "All four / అన్నీ",
     "Only 2 and 3 / 2 మరియు 3 మాత్రమే",
     "Only 1 and 4 / 1 మరియు 4 మాత్రమే",
     "a",
     "Pair 3 wrong — Equality in Preamble has only TWO types (Status + Opportunity), not three. Economic Equality is in DPSP."),

    (3, 2,
     "What types of Justice are mentioned in the Preamble? [UPSC Style]\nతెలుగు: ప్రస్తావనలో న్యాయం రకాలు?",
     "Social and Economic only / Social + Economic",
     "Social, Economic and Political / Social + Economic + Political (correct)",
     "Social, Economic, Political and Judicial / 4 types",
     "Economic and Political only / Economic + Political",
     "b",
     "Three types: Social + Economic + Political. Inspired by the Russian Revolution 1917 (USSR Constitution).",
     "UPSC"),

    # ══════════════ SECTION 4 — Fraternity ══════════════

    (4, 1,
     "What does Fraternity in the Preamble assure?\nతెలుగు: 'Fraternity' (సోదరభావం) ఏమి నిర్థారిస్తుంది?",
     "Only economic equality / కేవలం ఆర్థిక సమానత్వం",
     "Dignity of individual + Unity and Integrity of Nation / వ్యక్తి గౌరవం + దేశ ఐక్యత-సమగ్రత (correct)",
     "Only political rights / కేవలం రాజకీయ హక్కులు",
     "Only religious freedom / కేవలం మత స్వేచ్ఛ",
     "b",
     "Fraternity assures TWO things: (1) the DIGNITY of the individual + (2) UNITY and INTEGRITY of the Nation."),

    (4, 1,
     "Which amendment added 'Integrity' to 'Unity of the Nation'?\nతెలుగు: 'Integrity' పదం ఏ సవరణ ద్వారా చేర్చారు?",
     "40th Amendment / 40వ సవరణ",
     "42nd Amendment 1976 / 42వ సవరణ 1976 (correct)",
     "44th Amendment / 44వ సవరణ",
     "86th Amendment / 86వ సవరణ",
     "b",
     "42nd Amendment 1976 added 'Integrity' to make the phrase 'Unity AND INTEGRITY of the Nation'. Originally just 'Unity of the Nation'."),

    (4, 2,
     "What did Dr. Ambedkar say about Fraternity?\nతెలుగు: అంబేడ్కర్ Fraternity గురించి?",
     "Fraternity = economic equality / ఆర్థిక సమానత్వం",
     "Fraternity means a sense of common brotherhood of all Indians / అందరు భారతీయులు సహోదరులు అనే భావన (correct)",
     "Fraternity = nationalism / జాతీయవాదం",
     "Fraternity = religious tolerance only / కేవలం మత సహనం",
     "b",
     "Ambedkar: 'Fraternity means a sense of common brotherhood of all Indians — Indians being one people.' Without fraternity, equality and liberty would be only paper-thin."),

    (4, 2,
     "Regarding 'Fraternity', which of the following are CORRECT?\n(1) Assures dignity of individual\n(2) Assures unity + integrity of nation\n(3) 'Integrity' added by 42nd Amendment 1976\n(4) Fraternity = economic equality\nతెలుగు: 'Fraternity' గురించి సరైనవి ఏవి?\n(1) వ్యక్తి గౌరవం\n(2) దేశ ఐక్యత + సమగ్రత\n(3) 'Integrity' 42వ సవరణ ద్వారా\n(4) Fraternity = ఆర్థిక సమానత్వం",
     "1, 2 and 3 only / 1, 2 మరియు 3 మాత్రమే (correct)",
     "All four / అన్నీ",
     "2 and 4 only / 2 మరియు 4 మాత్రమే",
     "1 and 4 only / 1 మరియు 4 మాత్రమే",
     "a",
     "Pairs 1, 2, 3 correct. Pair 4 WRONG — Fraternity ≠ economic equality (it's brotherhood/dignity/unity). Economic equality is in DPSP."),

    (4, 3,
     "Assertion (A): Fraternity in the Preamble aims to promote a sense of brotherhood among all citizens.\nReason (R): Without Fraternity, Liberty and Equality remain empty ideals — as Dr. Ambedkar pointed out, Liberty without Fraternity would lead to inequality.\nతెలుగు: అభికథనం-కారణం సరైనవా?",
     "Both correct, R explains A / రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "Both correct, R doesn't explain / రెండూ సరైనవి, R వివరణ కాదు",
     "A correct, R wrong / A సరైనది, R తప్పు",
     "A wrong, R correct / A తప్పు, R సరైనది",
     "a",
     "Both correct. R precisely explains A — Fraternity is the binding glue that makes Liberty and Equality meaningful. Ambedkar's exact insight."),

    (4, 4,
     "Is the classification of Preamble terms below correct?\n(1) Sovereign, Socialist, Secular, Democratic, Republic — Nature of State\n(2) Justice, Liberty, Equality, Fraternity — Objectives for citizens\n(3) 'We the People' — People are the source of authority\n(4) November 26, 1949 — Constitution came into force\nతెలుగు: ప్రస్తావన పదాల వర్గీకరణ సరైనదా?",
     "1, 2, 3 only correct / 1, 2 మరియు 3 మాత్రమే సరైనవి (correct)",
     "All four / అన్నీ సరైనవి",
     "2 and 4 only / 2 మరియు 4 మాత్రమే",
     "1 and 4 only / 1 మరియు 4 మాత్రమే",
     "a",
     "Pair 4 wrong — November 26, 1949 = ADOPTION date (not commencement). Constitution came into FORCE on January 26, 1950. The other three classifications are correct."),

    (4, 2,
     "What does Fraternity in the Preamble assure? [APPSC Group 2]\nతెలుగు: 'Fraternity' వల్ల ఏమి నిర్థారిస్తారు?",
     "Only economic development / కేవలం ఆర్థిక అభివృద్ధి",
     "Dignity of individual + Unity and Integrity of Nation / వ్యక్తి గౌరవం + దేశ ఐక్యత-సమగ్రత (correct)",
     "Only political freedom / కేవలం రాజకీయ స్వేచ్ఛ",
     "Only religious freedom / కేవలం మత స్వేచ్ఛ",
     "b",
     "Fraternity assures: (1) Dignity of the individual + (2) Unity and Integrity of the Nation. APPSC standard answer.",
     "APPSC"),

    # ══════════════ SECTION 5 — Amendments to Preamble ══════════════

    (5, 1,
     "How many times has the Preamble been amended so far?\nతెలుగు: ప్రస్తావన ఇప్పటివరకు ఎన్నిసార్లు సవరించారు?",
     "Twice / రెండు సార్లు",
     "Once / ఒక్కసారి (correct)",
     "Three times / మూడు సార్లు",
     "Never amended / ఎప్పుడూ లేదు",
     "b",
     "Preamble has been amended ONLY ONCE — by the 42nd Amendment 1976 (which added Socialist, Secular, Integrity)."),

    (5, 1,
     "Why is the 42nd Amendment 1976 called 'Mini Constitution'?\nతెలుగు: 42వ సవరణ 1976 ను 'Mini Constitution' ఎందుకు అంటారు?",
     "It was a small amendment / చిన్న సవరణ",
     "It changed many constitutional provisions / రాజ్యాంగంలో చాలా అంశాలను మార్చింది (correct)",
     "It only changed the Preamble / కేవలం ప్రస్తావన",
     "It came during Emergency / Emergency తో",
     "b",
     "42nd Amendment 1976 is called 'Mini Constitution' because it changed MANY provisions: Preamble, Fundamental Duties, DPSPs, Centre-State relations, judicial review, etc."),

    (5, 2,
     "Can the Preamble be amended under Article 368?\nతెలుగు: ప్రస్తావనను Article 368 కింద సవరించవచ్చా?",
     "No, cannot be amended / సవరించలేరు",
     "Yes, but cannot damage Basic Structure / అవును, కానీ Basic Structure దెబ్బతీయకూడదు (correct)",
     "Yes, can be completely amended / పూర్తిగా",
     "No, Preamble is not part of Constitution / రాజ్యాంగంలో భాగం కాదు",
     "b",
     "Yes, the Preamble CAN be amended under Article 368 — but subject to the BASIC STRUCTURE doctrine (Kesavananda Bharati 1973). The 42nd Amendment 1976 successfully amended it."),

    (5, 2,
     "Which were added to the Preamble by the 42nd Amendment 1976?\n(1) Socialist\n(2) Secular\n(3) Integrity\n(4) Democratic\nతెలుగు: 42వ సవరణ ద్వారా చేర్చిన అంశాలు?",
     "1, 2 and 3 only / 1, 2 మరియు 3 మాత్రమే (correct)",
     "All four / అన్నీ",
     "1 and 2 only / 1 మరియు 2 మాత్రమే",
     "2 and 4 only / 2 మరియు 4 మాత్రమే",
     "a",
     "42nd Amendment added Socialist + Secular + Integrity. 'Democratic' was already in the original 1949 Preamble."),

    (5, 3,
     "In which case was the Basic Structure Doctrine propounded?\nతెలుగు: Basic Structure Doctrine ఏ కేసులో ప్రకటించారు?",
     "Berubari Union Case 1960",
     "Golaknath Case 1967",
     "Kesavananda Bharati v. State of Kerala 1973 / Kesavananda Bharati 1973 (correct)",
     "Minerva Mills Case 1980",
     "c",
     "Kesavananda Bharati v. State of Kerala (1973) — landmark 13-judge bench decision. Held: Parliament can amend any part BUT cannot destroy the BASIC STRUCTURE."),

    (5, 4,
     "Match the cases with their rulings:\n(P) Berubari Union Case 1960 — (1) Preamble is part of Constitution\n(Q) Kesavananda Bharati 1973 — (2) Preamble is NOT part of Constitution\n(R) LIC of India Case 1995 — (3) Basic Structure Doctrine + Preamble is part\n(S) Golaknath Case 1967 — (4) Parliament cannot amend FRs\nతెలుగు: కేసులను తీర్పులతో జోడించండి:\n(P) Berubari 1960 — (1) Preamble is part\n(Q) Kesavananda 1973 — (2) Preamble NOT part\n(R) LIC 1995 — (3) Basic Structure + Preamble is part\n(S) Golaknath 1967 — (4) Parliament cannot amend FR",
     "P-2, Q-3, R-1, S-4 (correct)",
     "P-1, Q-2, R-3, S-4",
     "P-3, Q-1, R-2, S-4",
     "P-2, Q-1, R-3, S-4",
     "a",
     "Berubari (1960) = Preamble NOT part of Constitution (P-2); Kesavananda (1973) = Basic Structure + Preamble IS part (Q-3); LIC (1995) = Preamble IS part of Constitution (R-1); Golaknath (1967) = Parliament cannot amend FRs (S-4)."),

    (5, 2,
     "In which case did the Supreme Court rule that the Preamble is part of the Constitution? [UPSC Style]\nతెలుగు: ప్రస్తావన రాజ్యాంగంలో భాగమని ఏ కేసు తేల్చింది?",
     "Berubari Union Case 1960 / Berubari 1960",
     "Golaknath Case 1967 / Golaknath 1967",
     "Kesavananda Bharati Case 1973 / Kesavananda 1973 (correct)",
     "Minerva Mills Case 1980 / Minerva Mills 1980",
     "c",
     "Kesavananda Bharati (1973) overruled Berubari (1960). Now settled law: Preamble IS part of the Constitution.",
     "UPSC"),

    # ══════════════ SECTION 6 — Preamble: Part of Constitution / Enforceability ══════════════

    (6, 1,
     "Is the Preamble part of the Constitution? After which case was this confirmed?\nతెలుగు: ప్రస్తావన రాజ్యాంగంలో భాగమా? ఏ కేసు తర్వాత?",
     "Berubari 1960 — said NOT part of Constitution / Berubari 1960 — భాగం కాదు",
     "Kesavananda Bharati 1973 — said it IS part of Constitution / Kesavananda 1973 — భాగమే (correct)",
     "Never settled / ఎప్పుడూ నిర్ధారించలేదు",
     "Only LIC 1995 settled it / కేవలం LIC 1995",
     "b",
     "Kesavananda Bharati (1973) overruled the earlier Berubari ruling and settled that the Preamble IS part of the Constitution."),

    (6, 1,
     "Can the Preamble be directly enforced in courts?\nతెలుగు: ప్రస్తావన నేరుగా న్యాయస్థానాలలో అమలు చేయించుకోవచ్చా?",
     "Yes, can be directly enforced / అవును, నేరుగా",
     "No, not directly enforceable — but used for interpretation / లేదు, నేరుగా అమలు కాదు; వ్యాఖ్యానానికి (correct)",
     "Yes, like FRs / అవును, FR వలే",
     "No, Preamble is not part of Constitution / రాజ్యాంగంలో భాగం కాదు",
     "b",
     "Preamble is part of the Constitution but is NOT directly enforceable. Courts use it as a guide to INTERPRET ambiguous constitutional provisions."),

    (6, 2,
     "What purpose does the Preamble serve?\nతెలుగు: ప్రస్తావన ఏ పనికి ఉపయోగపడుతుంది?",
     "Grants legal rights directly / నేరుగా చట్టపర హక్కులు",
     "For constitutional interpretation; reveals makers' intent / రాజ్యాంగ వ్యాఖ్యానం + నిర్మాతల ఉద్దేశ్యం (correct)",
     "To impose Emergency / అత్యవసర పరిస్థితి",
     "For direct legislation / శాసన నిర్మాణం",
     "b",
     "Preamble = key to UNDERSTAND/INTERPRET the Constitution. Reveals the philosophy/intent of the framers (Ernest Barker called it 'a key to open the minds of the makers')."),

    (6, 2,
     "Difference between Berubari Union Case (1960) and Kesavananda Bharati (1973)?\n(1) Berubari: Preamble is NOT part of Constitution\n(2) Kesavananda: Preamble IS part of Constitution\n(3) Berubari: Basic Structure Doctrine declared\n(4) Kesavananda: Basic Structure Doctrine declared\nతెలుగు: రెండు కేసుల తేడా?\n(1) Berubari: Preamble రాజ్యాంగంలో భాగం కాదు\n(2) Kesavananda: Preamble భాగమే\n(3) Berubari: Basic Structure ప్రకటన\n(4) Kesavananda: Basic Structure ప్రకటన",
     "1, 2 and 4 only correct / 1, 2 మరియు 4 మాత్రమే సరైనవి (correct)",
     "All four / అన్నీ",
     "1 and 3 only / 1 మరియు 3 మాత్రమే",
     "2 and 3 only / 2 మరియు 3 మాత్రమే",
     "a",
     "Pair 3 wrong — Basic Structure Doctrine was declared in KESAVANANDA (1973), NOT Berubari (1960). The other three are correct."),

    (6, 3,
     "What is the difference between Berubari (1960) and Kesavananda (1973) on the Preamble's status?\nతెలుగు: రెండు కేసులో ప్రస్తావన స్థానం తేడా?",
     "Both ruled Preamble is part / రెండు కేసులో భాగం",
     "Berubari: Preamble NOT part; Kesavananda: Preamble IS part / Berubari భాగం కాదు; Kesavananda భాగమే (correct)",
     "Both ruled Preamble is NOT part / రెండు కేసులో భాగం కాదు",
     "Berubari: Preamble IS part; Kesavananda: NOT part / తారుమారు",
     "b",
     "Berubari (1960) initially held Preamble was NOT part of the Constitution. Kesavananda (1973) reversed this and held Preamble IS part of the Constitution."),

    (6, 4,
     "Assertion (A): The Preamble can be amended by Parliament under Article 368.\nReason (R): In Kesavananda Bharati (1973), the Supreme Court held that the Preamble is part of the Constitution, and Parliament may amend it subject to the Basic Structure limitation.\nతెలుగు: అభికథనం-కారణం సరైనవా?",
     "Both correct, R explains A / రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "Both correct, R doesn't explain / రెండూ సరైనవి, R వివరణ కాదు",
     "A correct, R wrong / A సరైనది, R తప్పు",
     "A wrong, R correct / A తప్పు, R సరైనది",
     "a",
     "Both A and R are correct, and R precisely explains A — Kesavananda's ruling that Preamble is part of the Constitution is exactly what enables Parliament to amend it under Article 368 (subject to Basic Structure)."),

    (6, 2,
     "Which Supreme Court case first declared that the Preamble is part of the Constitution? [APPSC Group 2]\nతెలుగు: ప్రస్తావన రాజ్యాంగంలో భాగమని మొదట ఏ సుప్రీం కోర్టు కేసు?",
     "Berubari Union Case 1960 / Berubari 1960",
     "Golaknath Case 1967 / Golaknath 1967",
     "Kesavananda Bharati Case 1973 / Kesavananda Bharati 1973 (correct)",
     "Minerva Mills Case 1980 / Minerva Mills 1980",
     "c",
     "Kesavananda Bharati (1973) first declared that the Preamble IS part of the Constitution — overruling Berubari (1960). LIC (1995) reaffirmed it.",
     "APPSC"),

    # ══════════════ SECTION 7 — Misc / Summary ══════════════

    (7, 1,
     "How many key 'descriptors of the State' are mentioned in the Preamble?\nతెలుగు: ప్రస్తావనలో దేశ స్వభావ పదాలు ఎన్ని?",
     "Three / మూడు",
     "Four / నాలుగు",
     "Five / ఐదు (correct)",
     "Six / ఆరు",
     "c",
     "FIVE descriptors of the Indian State: Sovereign + Socialist + Secular + Democratic + Republic. (Original 1949 had 3; 42nd Amendment 1976 added Socialist + Secular.)"),

    (7, 1,
     "Inspiration for 'Justice' (Social, Economic, Political) in the Preamble?\nతెలుగు: 'Justice' కి ఆదర్శం/మూలం?",
     "USA Bill of Rights / USA",
     "Russian Revolution 1917 / రష్యా విప్లవం 1917 (correct)",
     "UN Charter / UN",
     "France Revolution / ఫ్రాన్స్ విప్లవం",
     "b",
     "Three types of Justice (Social, Economic, Political) inspired by the Russian Revolution 1917 (USSR Constitution). Liberty/Equality/Fraternity = French Revolution 1789."),

    (7, 2,
     "How many objectives are secured to citizens in the Preamble?\nతెలుగు: పౌరులకు ఎన్ని లక్ష్యాలు?",
     "Two — Justice and Liberty / రెండు",
     "Three — Justice, Liberty, Equality / మూడు",
     "Four — Justice, Liberty, Equality, Fraternity / నాలుగు (correct)",
     "Five — adding Democracy / ఐదు",
     "c",
     "FOUR objectives secured to citizens: JUSTICE + LIBERTY + EQUALITY + FRATERNITY. (Democracy is part of the State's nature, not an objective for citizens.)"),

    (7, 2,
     "Which of the following are CORRECT about the Preamble?\n(1) Inspired by USA Preamble\n(2) Amended only once (42nd Amendment 1976)\n(3) Berubari (1960) — Preamble IS part of Constitution\n(4) Kesavananda (1973) — Preamble IS part of Constitution\nతెలుగు: ప్రస్తావన గురించి సరైనవి?\n(1) USA నుండి స్ఫూర్తి\n(2) ఒక్కసారి సవరణ (42వ 1976)\n(3) Berubari (1960) — Preamble భాగమే\n(4) Kesavananda (1973) — Preamble భాగమే",
     "1, 2 and 4 only correct / 1, 2 మరియు 4 మాత్రమే (correct)",
     "All four / అన్నీ",
     "3 and 4 only / 3 మరియు 4 మాత్రమే",
     "2 and 3 only / 2 మరియు 3 మాత్రమే",
     "a",
     "Pair 3 wrong — Berubari (1960) said Preamble is NOT part of Constitution. Kesavananda (1973) reversed this. The other three are correct."),

    (7, 3,
     "Difference between Social, Economic and Political Justice in the Preamble?\nతెలుగు: సామాజిక, ఆర్థిక, రాజకీయ న్యాయాల తేడా?",
     "All three same meaning / మూడూ ఒకే అర్థం",
     "Social = caste/religion/gender discrimination removal; Economic = wealth equality; Political = voting + opportunity / Social = వివక్ష; Economic = సంపద; Political = ఓటు + అవకాశాలు (correct)",
     "Social = voting; Economic = religion; Political = caste / తారుమారు",
     "Social = political participation; Economic = land reforms; Political = civil rights / తారుమారు",
     "b",
     "SOCIAL Justice = ending caste/religion/gender/race discrimination. ECONOMIC Justice = wealth/income/resource equity. POLITICAL Justice = equal voting rights + access to public office for all citizens."),

    (7, 4,
     "Assertion (A): The Preamble to the Indian Constitution reflects the ideals and aspirations of the people of India.\nReason (R): The Preamble is based on the Objective Resolution moved by Nehru in 1946, which encapsulated the vision of free India, and was used as a guide in drafting the Constitution.\nతెలుగు: అభికథనం-కారణం సరైనవా?",
     "Both correct, R explains A / రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "Both correct, R doesn't explain / రెండూ సరైనవి, R వివరణ కాదు",
     "A correct, R wrong / A సరైనది, R తప్పు",
     "A wrong, R correct / A తప్పు, R సరైనది",
     "a",
     "Both A and R correct, R precisely explains A. The Objective Resolution (1946) → Preamble (1949) lineage is exactly why the Preamble reflects the people's ideals."),

    (7, 2,
     "Which correctly describes what the Preamble IS and IS NOT? [UPSC Style]\nతెలుగు: ప్రస్తావన గురించి సరైన వివరణ?",
     "Enforceable in court + part of Constitution / అమలు + భాగం",
     "Part of Constitution but NOT directly enforceable in court / రాజ్యాంగంలో భాగం కానీ నేరుగా అమలు కాదు (correct)",
     "Neither part of Constitution nor enforceable / ఏదీ కాదు",
     "Part until 1973, removed after Kesavananda / 1973 వరకు భాగం, తర్వాత రద్దు",
     "b",
     "Preamble IS part of the Constitution (Kesavananda 1973) but NOT directly enforceable in court. Used only for interpretation purposes.",
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
