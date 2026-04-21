# seed_polity_ch5.py
# Chapter 5: Union and its Territory
# (యూనియన్ మరియు దాని భూభాగం)
# Standard : APPSC Group 2 | Source: Lakshmikanth Indian Polity
# Total Sections: 9 | Total MCQs: 57 | PYQs: 5
# Difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
# PYQ: 10th element (index 9) = 'APPSC' or 'UPSC'
# ─────────────────────────────────────────────

import json as _json

POLITY_CH5_SECTIONS = [
    {
        "title": "5.1 ఆర్టికల్ 1 — యూనియన్ నామం మరియు భూభాగం",
        "sub": "Article 1 · India that is Bharat · Union of States · Three Categories of Territory",
        "audio": """ఆర్టికల్ 1 — భారతదేశం యొక్క నామం మరియు భూభాగం:

"India, that is Bharat, shall be a Union of States."
(భారతదేశం, అనగా భారత్, రాష్ట్రాల సమాఖ్య (Union of States) అవుతుంది.)

ముఖ్యమైన విషయాలు:
• 'Union of States' — 'Federation of States' కాదు
• Dr. Ambedkar ఈ వ్యత్యాసం వివరించారు

ఆర్టికల్ 1 ప్రకారం భారత భూభాగం 3 రకాలు:
1. రాష్ట్రాల భూభాగాలు (Territories of the States)
2. కేంద్ర పాలిత ప్రాంతాలు (Union Territories)
3. అర్జించవలసిన భూభాగాలు (Territories that may be acquired)

'India' మరియు 'Bharat' — రెండూ దేశం అధికారిక పేర్లు:
• రాజ్యాంగంలో రెండు పేర్లు సమానంగా ఉపయోగిస్తారు
• English లో 'India', తెలుగు/హిందీలో 'భారత్'"""
    },
    {
        "title": "5.2 ఆర్టికల్ 2 — కొత్త రాష్ట్రాల ప్రవేశం",
        "sub": "Article 2 · Admission of New States · Parliament's Power",
        "audio": """ఆర్టికల్ 2 — కొత్త రాష్ట్రాల ప్రవేశం / స్థాపన:

"Parliament may by law admit into the Union, or establish, new States on such terms and conditions as it thinks fit."

పార్లమెంట్ అధికారాలు (Article 2):
• కొత్త రాష్ట్రాలను Union లో చేర్చవచ్చు
• కొత్త రాష్ట్రాలు స్థాపించవచ్చు
• సాధారణ మెజారిటీతో సరిపోతుంది

ఉదాహరణ:
• Sikkim — 1975 లో 36వ రాజ్యాంగ సవరణ ద్వారా 22వ రాష్ట్రంగా చేర్చారు

ఆర్టికల్ 2 vs ఆర్టికల్ 3 తేడా:
• Article 2 = కొత్త రాష్ట్రాల ప్రవేశం (అప్పటికి India లో లేని భూభాగాల నుండి)
• Article 3 = ఉన్న రాష్ట్రాల పునర్వ్యవస్థీకరణ, సరిహద్దుల మార్పు"""
    },
    {
        "title": "5.3 ఆర్టికల్ 3 — రాష్ట్రాల మార్పులు",
        "sub": "Article 3 · New States · Alteration · Parliament's Procedure · President's Recommendation",
        "audio": """ఆర్టికల్ 3 — కొత్త రాష్ట్రాల ఏర్పాటు మరియు ఉన్న రాష్ట్రాల మార్పు:

Parliament Article 3 కింద ఏమి చేయగలదు?
1. కొత్త రాష్ట్రాన్ని ఏర్పాటు చేయవచ్చు
2. రాష్ట్ర వైశాల్యం పెంచవచ్చు
3. రాష్ట్ర వైశాల్యం తగ్గించవచ్చు
4. రాష్ట్ర సరిహద్దులు మార్చవచ్చు
5. రాష్ట్ర పేరు మార్చవచ్చు

విధానం (Procedure):
• President సిఫారసు తప్పనిసరి (Bill రాష్ట్రపతి సిఫారసుతో మాత్రమే పార్లమెంట్ లో ప్రవేశపెట్టాలి)
• సంబంధిత రాష్ట్ర శాసనసభ (State Legislature) అభిప్రాయం తీసుకోవాలి
• కానీ రాష్ట్ర అభిప్రాయం పార్లమెంట్ కు బాధ్యత కలిగించదు — కేవలం సలహా
• సాధారణ మెజారిటీతో పార్లమెంట్ ఆమోదిస్తే సరిపోతుంది

ఆర్టికల్ 4:
• Articles 2 మరియు 3 కింద చేసిన చట్టాలు Schedule 1 మరియు Schedule 4 ని సవరించవచ్చు
• ఇది Article 368 కింద రాజ్యాంగ సవరణ కాదు"""
    },
    {
        "title": "5.4 ఎందుకు 'Union of States' — Federation కాదు",
        "sub": "Union vs Federation · Indestructible Union · States Cannot Secede · Ambedkar's Explanation",
        "audio": """'Union of States' — 'Federation of States' కాదు — ఎందుకు?

Dr. B.R. Ambedkar వివరణ:
"The word 'Union' is used not 'Federation' because:
1. States have no right to secede (రాష్ట్రాలకు భారతదేశం నుండి వేరు పడే హక్కు లేదు)
2. India is an indestructible union of destructible states (రాష్ట్రాలు మార్చవచ్చు కానీ Union మారదు)"

USA vs India తేడా:
• USA: రాష్ట్రాలు కలిసి Federation ఏర్పాటు చేశాయి (States formed the Union)
• India: రాజ్యాంగం నుండి రాష్ట్రాలు పుట్టాయి (Union created the States)

"Indestructible Union of Destructible States":
• Union = స్థిరంగా ఉంటుంది
• States = మార్చవచ్చు, పునర్వ్యవస్థీకరించవచ్చు, పేరు మార్చవచ్చు, చీల్చవచ్చు

ఈ లక్షణం:
• USA లో రాష్ట్రాల అధికారాలు బలంగా ఉంటాయి
• Canada లో Centre బలంగా ఉంటుంది — India ఇది అనుసరించింది"""
    },
    {
        "title": "5.5 రాష్ట్రాల పునర్వ్యవస్థీకరణ (Bilingual)",
        "sub": "States Reorganisation · SRC 1953 · Fazl Ali Commission · 1956 Act · Linguistic States",
        "audio": """రాష్ట్రాల పునర్వ్యవస్థీకరణ (States Reorganisation):

States Reorganisation Commission (SRC) 1953:
• Fazl Ali Commission అని కూడా అంటారు
• సభ్యులు: Fazl Ali (Chairman), Hriday Nath Kunzru, K.M. Panikkar
• రిపోర్ట్: 1955

States Reorganisation Act 1956:
• భాష ఆధారంగా రాష్ట్రాల పునర్వ్యవస్థీకరణ
• 14 రాష్ట్రాలు + 6 కేంద్ర పాలిత ప్రాంతాలు ఏర్పడ్డాయి

ఆంధ్ర రాష్ట్రం — మొట్టమొదటి భాషా రాష్ట్రం:
• 1952 Potti Sriramulu ఆమరణ నిరాహార దీక్ష
• అక్టోబర్ 1, 1953 — ఆంధ్ర రాష్ట్రం ఏర్పాటు (మద్రాస్ నుండి వేరు పడింది)
• తెలుగు మాట్లాడే ప్రజలకు మొట్టమొదటి రాష్ట్రం

ఆంధ్రప్రదేశ్:
• నవంబర్ 1, 1956 — ఆంధ్ర రాష్ట్రం + హైదరాబాద్ రాష్ట్రంలో తెలుగు ప్రాంతాలు కలిసి ఆంధ్రప్రదేశ్ ఏర్పాటు
• జూన్ 2, 2014 — తెలంగాణ మరియు ఆంధ్రప్రదేశ్ గా విభజన"""
    },
    {
        "title": "5.6 అర్జిత భూభాగాలు (Bilingual)",
        "sub": "Acquired Territories · Goa 1961 · Sikkim 1975 · Pondicherry 1954 · Dadra & Nagar Haveli",
        "audio": """అర్జిత భూభాగాలు (Acquired Territories) — India Union లో చేరిన ప్రాంతాలు:

1. గోవా, దమన్ మరియు డయ్యూ (Goa, Daman & Diu):
   • December 19, 1961 — Operation Vijay ద్వారా పోర్చుగీసు వారి నుండి విముక్తి
   • 1987 — Goa 25వ రాష్ట్రంగా ఏర్పాటు; Daman & Diu = UT

2. దాద్రా మరియు నగర్ హవేలీ (Dadra and Nagar Haveli):
   • 1961 లో India లో కలిపారు
   • 2020 — Dadra & Nagar Haveli + Daman & Diu కలిసి ఒక UT

3. పాండిచ్చేరి (Puducherry):
   • 1954 — ఫ్రెంచ్ వారు అప్పగించారు (De facto transfer)
   • 1962 — అధికారికంగా India లో విలీనం (De jure)
   • ప్రస్తుతం UT (with Legislature)

4. సిక్కిం (Sikkim):
   • 1975 — 36వ రాజ్యాంగ సవరణ ద్వారా India లో చేరింది
   • 22వ రాష్ట్రంగా మారింది
   • Article 371F — Sikkim కు ప్రత్యేక నిబంధనలు"""
    },
    {
        "title": "5.7 జమ్మూ కాశ్మీర్ మరియు 2019 మార్పు (Bilingual)",
        "sub": "J&K Special Status · Article 370 Abrogation · J&K UT · Ladakh UT · August 5 2019",
        "audio": """జమ్మూ కాశ్మీర్ (Jammu & Kashmir) — ప్రత్యేక చరిత్ర:

మొదటి First Schedule లో:
• J&K రాష్ట్రంగా ఉండేది
• Article 370 — ప్రత్యేక హోదా ఇచ్చింది (తాత్కాలిక నిబంధన)

ఆగస్ట్ 5, 2019 — చారిత్రాత్మక మార్పు:
• Article 370 రద్దు (Abrogation)
• Jammu & Kashmir Reorganisation Act 2019

విభజన:
• జమ్మూ కాశ్మీర్ → UT with Legislature (శాసనసభతో కేంద్ర పాలిత ప్రాంతం)
• లడఖ్ → UT without Legislature (శాసనసభ లేని కేంద్ర పాలిత ప్రాంతం)

అక్టోబర్ 31, 2019 — అమలు:
• మొత్తం రాష్ట్రాలు: 28
• మొత్తం UTs: 8

ప్రస్తుత 8 UTs:
Chandigarh, Delhi (NCT), Puducherry, Lakshadweep, Andaman & Nicobar Islands, Dadra & Nagar Haveli & Daman & Diu (combined 2020), Jammu & Kashmir (with legislature), Ladakh (without legislature)"""
    },
    {
        "title": "5.8 ప్రస్తుత రాష్ట్రాలు మరియు షెడ్యూళ్ళు (Bilingual)",
        "sub": "28 States · 8 UTs · First Schedule · Fourth Schedule · Article 4",
        "audio": """ప్రస్తుత భారతదేశం (2024):
• మొత్తం రాష్ట్రాలు: 28
• మొత్తం కేంద్ర పాలిత ప్రాంతాలు (UTs): 8

మొదటి షెడ్యూల్ (First Schedule):
• రాష్ట్రాలు మరియు UTs పేర్లు మరియు భూభాగాలు
• Article 3, 4 కింద మార్పులు జరిగినప్పుడు ఇది సవరించబడుతుంది

నాల్గవ షెడ్యూల్ (Fourth Schedule):
• రాజ్యసభలో రాష్ట్రాలు మరియు UTs కి సీట్ల కేటాయింపు

ఆర్టికల్ 4:
• Articles 2 మరియు 3 కింద చేసిన చట్టాలు Schedule 1 మరియు 4 ని సవరించవచ్చు
• ఇది Article 368 కింద రాజ్యాంగ సవరణ అవసరం లేదు
• అంటే: సాధారణ మెజారిటీతో రాష్ట్ర పేర్లు, సరిహద్దులు మార్చవచ్చు

గమనిక:
• Legislative Assemblies ఉన్న UTs: Delhi, Puducherry, J&K
• Legislative Assembly లేని UTs: Chandigarh, Lakshadweep, Andaman & Nicobar, Dadra & Nagar Haveli & Daman & Diu, Ladakh"""
    },
    {
        "title": "5.9 సినిమాటిక్ కథ — Union and Territory",
        "sub": "Full Chapter Story · Reorganisation · Potti Sriramulu · Sikkim · J&K",
        "audio": """1947 — స్వాతంత్ర్యం వచ్చింది. కానీ 562 సంస్థానాలు (Princely States) ఉన్నాయి.

సర్దార్ పటేల్ మరియు V.P. Menon అద్భుతమైన పని చేశారు — దాదాపు అన్ని సంస్థానాలు India లో కలిశాయి.

రాజ్యాంగం చెప్పింది: "India, that is Bharat, shall be a Union of States."

ఆ 'Union' అనే మాట — Dr. Ambedkar ఎంచుకున్న మాట.
"Federation కాదు. Union. ఎందుకంటే States మనల్ని వదిలి వెళ్ళలేవు."

1952 — Potti Sriramulu నిరాహార దీక్ష — తెలుగు రాష్ట్రం కోసం.
58 రోజుల తర్వాత మరణం. ఆ త్యాగం ఫలించింది.
1953 అక్టోబర్ 1 — ఆంధ్ర రాష్ట్రం పుట్టింది — దేశంలో మొట్టమొదటి భాషా రాష్ట్రం.

1956 — States Reorganisation Act — 14 రాష్ట్రాలు + 6 UTs.
భాష ఆధారంగా దేశం పునర్నిర్మించారు.

1961 — Operation Vijay. గోవా విముక్తి.
1975 — Sikkim 22వ రాష్ట్రం.
2014 — తెలంగాణ 29వ రాష్ట్రం.
2019 — J&K విభజన. 28 రాష్ట్రాలు, 8 UTs.

ఆ Union — ఇంకా బలంగా ఉంది. విభాజ్యం కాదు."""
    },
]

# ─────────────────────────────────────────────
#  MCQ DATA
#  (sec_idx, difficulty, q_te, a, b, c, d, correct, explanation_te)
#  difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
#  exam_type:  appended as 10th element (index 9) when PYQ ('APPSC'/'UPSC')
# ─────────────────────────────────────────────

POLITY_CH5_MCQS = [

    # ══════════════════════════════════════════
    # SECTION 0 — ఆర్టికల్ 1 — Union నామం మరియు భూభాగం
    # ══════════════════════════════════════════

    # Easy
    (0, 1,
     "ఆర్టికల్ 1 ప్రకారం భారతదేశం ఏ రకమైన రాజ్యం?",
     "రాష్ట్రాల సమాఖ్య (Federation of States)",
     "రాష్ట్రాల కూటమి (Confederation of States)",
     "రాష్ట్రాల యూనియన్ (Union of States)",
     "ఏకీకృత రాజ్యం (Unitary State)",
     "c",
     "ఆర్టికల్ 1: 'India, that is Bharat, shall be a Union of States.' — 'Federation' కాదు, 'Union'. Dr. Ambedkar ఈ మాట ఎంచుకున్నారు ఎందుకంటే రాష్ట్రాలకు వేరుపడే హక్కు లేదు."),

    (0, 1,
     "ఆర్టికల్ 1 ప్రకారం భారత భూభాగం ఎన్ని రకాలు?",
     "రెండు రకాలు", "మూడు రకాలు",
     "నాలుగు రకాలు", "ఐదు రకాలు",
     "b",
     "ఆర్టికల్ 1 ప్రకారం భారత భూభాగం 3 రకాలు: (1) రాష్ట్రాల భూభాగాలు, (2) కేంద్ర పాలిత ప్రాంతాలు, (3) అర్జించవలసిన భూభాగాలు. ఇవి Schedule 1 లో పేర్కొన్నారు."),

    (0, 1,
     "భారత రాజ్యాంగంలో రాష్ట్రాలు మరియు UTs పేర్లు ఏ షెడ్యూల్ లో ఉంటాయి?",
     "రెండవ షెడ్యూల్ (Second Schedule)",
     "మొదటి షెడ్యూల్ (First Schedule)",
     "నాల్గవ షెడ్యూల్ (Fourth Schedule)",
     "ఏడవ షెడ్యూల్ (Seventh Schedule)",
     "b",
     "మొదటి షెడ్యూల్ (First Schedule) లో రాష్ట్రాలు మరియు UTs పేర్లు మరియు వాటి భూభాగాల వివరాలు ఉంటాయి. నాల్గవ షెడ్యూల్ = రాజ్యసభలో సీట్ల కేటాయింపు."),

    # Moderate
    (0, 2,
     "కింది వాటిలో ఆర్టికల్ 1 గురించి సరైనవి ఏవి?\n(1) 'India that is Bharat' — రెండు పేర్లు అధికారికం\n(2) భారత్ = Union of States\n(3) భారత భూభాగం 4 రకాలు\n(4) First Schedule లో రాష్ట్రాలు పేర్లు ఉన్నాయి",
     "1, 2 మరియు 4 మాత్రమే", "1 మరియు 2 మాత్రమే",
     "1, 2, 3 మరియు 4 అన్నీ", "2, 3 మరియు 4 మాత్రమే",
     "a",
     "3 తప్పు — భారత భూభాగం 3 రకాలు (4 కాదు): రాష్ట్రాలు, UTs, అర్జించవలసిన భూభాగాలు. 1 (India=Bharat ✓), 2 (Union of States ✓), 4 (First Schedule ✓)."),

    (0, 2,
     "ఆర్టికల్ 1 లో 'Union of States' మరియు 'Federation of States' మధ్య తేడా ఏమిటి?",
     "రెండూ ఒకే అర్థం — వేర్వేరు భాషలో",
     "Union లో రాష్ట్రాలకు వేరుపడే హక్కు లేదు; Federation లో ఉంటుంది",
     "Federation లో Centre బలంగా ఉంటుంది; Union లో State బలంగా",
     "Union లో రాష్ట్రాలు ఎక్కువగా ఉంటాయి; Federation లో తక్కువ",
     "b",
     "Union — రాష్ట్రాలకు secede (వేరుపడే) హక్కు లేదు. Federation (USA) — రాష్ట్రాలు తమ ఇష్టానుసారం కూడగట్టుకున్నాయి. India లో రాజ్యాంగం నుండి రాష్ట్రాలు పుట్టాయి — కాబట్టి 'Union'. Dr. Ambedkar ఈ వ్యత్యాసం వివరించారు."),

    # Tough
    (0, 3,
     "Dr. Ambedkar 'India is an Indestructible Union of Destructible States' అని ఏమి అర్థంలో చెప్పారు?",
     "రాష్ట్రాలు ఎప్పుడూ నాశనం కావు; Union మారవచ్చు",
     "Union స్థిరంగా ఉంటుంది; రాష్ట్రాలు మార్చవచ్చు / చీల్చవచ్చు / పునర్వ్యవస్థీకరించవచ్చు",
     "రాష్ట్రాలు మరియు Union రెండూ స్థిరంగా ఉంటాయి",
     "రాష్ట్రాలు Union కి లోబడవు",
     "b",
     "India = Indestructible Union (పార్లమెంట్ Union ని రద్దు చేయలేదు) + Destructible States (రాష్ట్రాలను విభజించవచ్చు, కలపవచ్చు, పేరు మార్చవచ్చు). Telangana (2014) మరియు J&K (2019) ఇందుకు ఉదాహరణలు."),

    # Toughest
    (0, 4,
     "అభికథనం-కారణం సరైనవా? / Assertion (A): India is described as a 'Union of States' and not a 'Federation of States' in Article 1.\nReason (R): In India, the Constitution is supreme, states are created by the Constitution, and they cannot secede from the Union — unlike the USA where states formed the federation.",
     "A మరియు R రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "A మరియు R రెండూ సరైనవి, కానీ R వివరణ కాదు",
     "A సరైనది, R తప్పు",
     "A తప్పు, R సరైనది",
     "a",
     "India = 'Union of States' Article 1 లో (A — correct). రాజ్యాంగం సర్వోన్నతం, రాష్ట్రాలకు secede హక్కు లేదు — USA కి భిన్నంగా (R — correct and explains A). Dr. Ambedkar ఈ వ్యత్యాసం వివరించారు."),

    # PYQ — APPSC
    (0, 2,
     "ఆర్టికల్ 1 ప్రకారం భారతదేశాన్ని ఏమని పిలిచారు? [APPSC Group 2]",
     "రాష్ట్రాల సమాఖ్య (Federation of States)",
     "రాష్ట్రాల యూనియన్ (Union of States)",
     "ఏకీకృత గణతంత్రం (Unitary Republic)",
     "రాష్ట్రాల కూటమి (Confederation of States)",
     "b",
     "ఆర్టికల్ 1 ప్రకారం 'India, that is Bharat, shall be a Union of States.' — Federation కాదు Union. APPSC Group 2 లో ఇది అత్యంత తరచుగా వచ్చే ప్రశ్న. Dr. Ambedkar 'Union' అనే మాట ఎందుకు ఎంచుకున్నారో వివరించారు.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 1 — ఆర్టికల్ 2 మరియు 3
    # ══════════════════════════════════════════

    # Easy
    (1, 1,
     "ఆర్టికల్ 3 కింద పార్లమెంట్ ఏ పని చేయగలదు?",
     "కొత్త రాష్ట్రాలు ఏర్పాటు చేయడం, సరిహద్దులు మార్చడం, పేర్లు మార్చడం",
     "రాష్ట్రాల గవర్నర్లను నియమించడం",
     "రాష్ట్ర ముఖ్యమంత్రులను తొలగించడం",
     "రాష్ట్రాల అధికారాలు పరిమితం చేయడం",
     "a",
     "Article 3 కింద Parliament: కొత్త రాష్ట్రం ఏర్పాటు, వైశాల్యం పెంచడం/తగ్గించడం, సరిహద్దులు మార్చడం, పేరు మార్చడం. సాధారణ మెజారిటీతో + President సిఫారసు + రాష్ట్ర అభిప్రాయం (binding కాదు)."),

    (1, 1,
     "ఆర్టికల్ 3 కింద కొత్త రాష్ట్రం ఏర్పాటుకు పార్లమెంట్ లో ఏ రకమైన మెజారిటీ అవసరం?",
     "2/3 మెజారిటీ + రాష్ట్రాల ఆమోదం",
     "సాధారణ మెజారిటీ (Simple Majority)",
     "ఉభయ సభల ఉమ్మడి సమావేశంలో 2/3 మెజారిటీ",
     "సర్వానుమతి (Unanimous)",
     "b",
     "Article 3 కింద పార్లమెంట్ సాధారణ మెజారిటీతో కొత్త రాష్ట్రం ఏర్పాటు చేయగలదు. ఇది Article 368 కింద రాజ్యాంగ సవరణ కాదు. కానీ President సిఫారసు తప్పనిసరి."),

    (1, 1,
     "ఆర్టికల్ 3 కింద కొత్త రాష్ట్రం ఏర్పాటుకు సంబంధిత రాష్ట్ర శాసనసభ అభిప్రాయం —",
     "తప్పనిసరిగా అంగీకరించాలి (Binding on Parliament)",
     "అవసరమే లేదు",
     "తీసుకోవాలి, కానీ Parliament కి Binding కాదు (Non-binding)",
     "రాష్ట్రపతి తుది నిర్ణయం తీసుకుంటారు",
     "c",
     "Article 3 Proviso: సంబంధిత రాష్ట్ర శాసనసభ అభిప్రాయం తీసుకోవాలి (Mandatory procedure). కానీ ఆ అభిప్రాయం Parliament కి Binding కాదు. Parliament సాధారణ మెజారిటీతో నిర్ణయించవచ్చు."),

    # Moderate
    (1, 2,
     "ఆర్టికల్ 2 మరియు ఆర్టికల్ 3 మధ్య ముఖ్య తేడా ఏమిటి?",
     "Article 2 = రాష్ట్రాల పేర్లు మార్చడం; Article 3 = కొత్త రాష్ట్రాలు",
     "Article 2 = ఇప్పుడు Union లో లేని కొత్త భూభాగాల ప్రవేశం; Article 3 = ఉన్న రాష్ట్రాల పునర్వ్యవస్థీకరణ",
     "Article 2 = సరిహద్దు మార్పులు; Article 3 = UT ఏర్పాటు",
     "రెండూ ఒకటే అర్థం",
     "b",
     "Article 2 = అప్పటికి India లో లేని (outside) కొత్త రాష్ట్రాల / భూభాగాల ప్రవేశం. Article 3 = ఇప్పటికే India లో ఉన్న రాష్ట్రాల పునర్వ్యవస్థీకరణ, సరిహద్దు మార్పు, పేరు మార్పు. Sikkim ప్రవేశం = Article 2."),

    (1, 2,
     "Article 3 కింద Bill పార్లమెంట్ లో ప్రవేశపెట్టడానికి ఏ నిబంధన తప్పనిసరి?",
     "రాజ్యసభ అనుమతి మొదట అవసరం",
     "రాష్ట్రపతి సిఫారసు తప్పనిసరి",
     "సుప్రీం కోర్టు అనుమతి అవసరం",
     "Cabinet ఏకగ్రీవ నిర్ణయం అవసరం",
     "b",
     "Article 3 Proviso: Article 3 కింద Bill రాష్ట్రపతి (President's Recommendation) సిఫారసుతో మాత్రమే పార్లమెంట్ లో ప్రవేశపెట్టాలి. ఇది Constitutional Requirement — లేకుండా Bill చెల్లదు."),

    # Tough
    (1, 3,
     "ఆర్టికల్ 4 గురించి సరైనది ఏది?",
     "Article 4 = రాజ్యాంగ సవరణ విధానం (Article 368 వలే)",
     "Article 4 కింద చేసిన చట్టాలు Schedule 1 మరియు 4 సవరించవచ్చు — Article 368 అవసరం లేదు",
     "Article 4 = కొత్త రాష్ట్రాల ఏర్పాటు అధికారం",
     "Article 4 = రాష్ట్రాల సరిహద్దు మార్పు నిషేధం",
     "b",
     "Article 4 ప్రకారం: Articles 2 మరియు 3 కింద చేసిన చట్టాలు First Schedule మరియు Fourth Schedule సవరించవచ్చు — ఇది Article 368 కింద రాజ్యాంగ సవరణ అవసరం లేదు. అందుకే రాష్ట్రాల పేర్లు, సరిహద్దులు సాధారణ చట్టంతో మార్చవచ్చు."),

    # Toughest
    (1, 4,
     "కింది జంటలు అన్నీ సరైనవేనా?\n(1) Article 1 — Union of States, Territory definition\n(2) Article 2 — Parliament can admit/establish new states\n(3) Article 3 — Parliament can form, alter, rename states — needs President's recommendation\n(4) Article 4 — Alteration of Schedules 1 and 4 treated as Article 368 amendment",
     "1, 2 మరియు 3 మాత్రమే సరైనవి", "1, 2, 3 మరియు 4 అన్నీ",
     "2 మరియు 4 తప్పు", "3 మరియు 4 మాత్రమే",
     "a",
     "4 తప్పు — Article 4 కింద Schedule మార్పులు Article 368 రాజ్యాంగ సవరణగా పరిగణించరు — అవి సాధారణ చట్టంగా పరిగణిస్తారు. 1, 2, 3 అన్నీ సరైనవి."),

    # PYQ — UPSC
    (1, 2,
     "కొత్త రాష్ట్రాలు ఏర్పాటు ఏ అధికరణం కింద? / Under which Article of the Indian Constitution can Parliament form new states or alter the areas, boundaries or names of existing states? [UPSC Style]",
     "Article 1", "Article 2",
     "Article 3", "Article 4",
     "c",
     "Article 3 = Parliament ఉన్న రాష్ట్రాలను విభజించడం, కలపడం, సరిహద్దు మార్చడం, పేరు మార్చడం. Article 2 = కొత్త రాష్ట్రాల ప్రవేశం (Union లో లేని భూభాగాలు). Article 4 = ఈ మార్పులకు Schedule 1 & 4 సవరించడం.",
     "UPSC"),

    # ══════════════════════════════════════════
    # SECTION 2 — Union of States vs Federation
    # ══════════════════════════════════════════

    # Easy
    (2, 1,
     "Dr. B.R. Ambedkar ప్రకారం 'Indestructible Union of Destructible States' అంటే ఏమిటి?",
     "రాష్ట్రాలు మారవు; Union మారవచ్చు",
     "Union మారదు; రాష్ట్రాలు విభజించవచ్చు / పునర్వ్యవస్థీకరించవచ్చు",
     "రాష్ట్రాలు Union ని వదిలి వెళ్ళవచ్చు",
     "Union మరియు రాష్ట్రాలు రెండూ స్థిరం",
     "b",
     "Dr. Ambedkar: 'India is an indestructible union of destructible states.' Union = విభాజ్యం కాదు. States = మార్చవచ్చు (విభజన, విలీనం, పేరు మార్పు). ఉదాహరణ: తెలంగాణ వేరు పడడం — State destructed but Union intact."),

    (2, 1,
     "USA లో రాష్ట్రాలు Federation ఏర్పాటు చేశాయి. India లో ఏమి జరిగింది?",
     "India లో కూడా రాష్ట్రాలు Union ఏర్పాటు చేశాయి",
     "India లో రాజ్యాంగం నుండి రాష్ట్రాలు పుట్టాయి — రాష్ట్రాలు Union ని ఏర్పాటు చేయలేదు",
     "India లో ప్రజలు రాష్ట్రాలను ఏర్పాటు చేశారు",
     "India లో బ్రిటిష్ వారు రాష్ట్రాలను ఏర్పాటు చేశారు",
     "b",
     "USA: States → Federation (రాష్ట్రాలు Union ని నిర్మించాయి). India: Constitution → States (రాజ్యాంగం రాష్ట్రాలను నిర్మించింది). అందుకే India లో రాష్ట్రాలు వేరు పడే హక్కు లేదు."),

    (2, 1,
     "K.C. Wheare భారత సమాఖ్య వ్యవస్థను ఏమని వర్ణించారు?",
     "Pure Federal System", "Unitary System",
     "Quasi-Federal System", "Confederal System",
     "c",
     "K.C. Wheare భారతదేశాన్ని 'Quasi-Federal System' అని వర్ణించారు — సమాఖ్య రూపంలో కానీ కేంద్రం బలంగా ఉంటుంది. 'Federal in form, Unitary in spirit' అని కూడా అన్నారు."),

    # Moderate
    (2, 2,
     "కింది విషయాలలో USA Federation మరియు India Union మధ్య తేడా ఏమిటి?\n(1) USA లో States Union ఏర్పాటు చేశాయి; India లో Constitution States ని ఏర్పాటు చేసింది\n(2) USA లో Residuary Powers States కి; India లో Centre కి\n(3) USA లో States వేరు పడవచ్చు; India లో లేదు\n(4) రెండు దేశాల్లో Federal Features ఒకటే",
     "1, 2 మరియు 3 మాత్రమే", "1 మరియు 3 మాత్రమే",
     "1, 2, 3 మరియు 4 అన్నీ", "2 మరియు 4 మాత్రమే",
     "a",
     "4 తప్పు — USA మరియు India Federal Features వేర్వేరు. USA లో Residuary Powers States కి, India లో Centre కి; USA లో States తమ రాజ్యాంగాలు కలిగి ఉన్నాయి, India లో అందరికీ ఒకే రాజ్యాంగం. 1, 2, 3 సరైనవి."),

    (2, 2,
     "భారతదేశాన్ని 'Cooperative Federalism' అని ఎవరు అన్నారు?",
     "K.C. Wheare", "Granville Austin",
     "Dr. Ambedkar", "Jawaharlal Nehru",
     "b",
     "Granville Austin భారత సమాఖ్య వ్యవస్థను 'Cooperative Federalism' అని వర్ణించారు — Centre మరియు States సహకారంతో పని చేస్తాయి. K.C. Wheare దీన్ని 'Quasi-Federal' అన్నారు."),

    # Tough
    (2, 3,
     "భారత రాజ్యాంగంలో రాష్ట్రాలకు వేరుపడే హక్కు (Right to Secede) లేకపోవడం ఏ లక్షణాన్ని చూపిస్తుంది?",
     "సమాఖ్య లక్షణం (Federal Feature)",
     "ఏకీకృత లక్షణం (Unitary Feature) — కేంద్రం బలంగా ఉంటుంది",
     "పార్లమెంటరీ లక్షణం",
     "లౌకిక లక్షణం",
     "b",
     "రాష్ట్రాలకు secede హక్కు లేకపోవడం = ఏకీకృత లక్షణం. ఇది USA Federation కి భిన్నంగా India కి ఉన్న కేంద్రాభిముఖత చూపిస్తుంది. Dr. Ambedkar ఇందుకే 'Union' అనే మాట ఎంచుకున్నారు."),

    # Toughest
    (2, 4,
     "అభికథనం-కారణం సరైనవా? / Assertion (A): India is described as a Union, not a Federation, because the states of India have no right to secede.\nReason (R): Unlike the USA, where states came together to form a federation and retain certain inherent rights, the Indian states were created by the Constitution and draw their existence from it.",
     "A మరియు R రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "A మరియు R రెండూ సరైనవి, కానీ R వివరణ కాదు",
     "A సరైనది, R తప్పు",
     "A తప్పు, R సరైనది",
     "a",
     "India 'Union' ఎందుకంటే States secede హక్కు లేదు (A — correct). USA లో States = Federation ఏర్పాటు చేశాయి; India లో Constitution = States ని ఏర్పాటు చేసింది (R — correct, directly explains A)."),

    # ══════════════════════════════════════════
    # SECTION 3 — Schedules 1 మరియు 4
    # ══════════════════════════════════════════

    # Easy
    (3, 1,
     "భారత రాజ్యాంగంలో రాజ్యసభలో రాష్ట్రాలకు సీట్ల కేటాయింపు ఏ షెడ్యూల్ లో ఉంది?",
     "మొదటి షెడ్యూల్ (First Schedule)",
     "రెండవ షెడ్యూల్ (Second Schedule)",
     "మూడవ షెడ్యూల్ (Third Schedule)",
     "నాల్గవ షెడ్యూల్ (Fourth Schedule)",
     "d",
     "నాల్గవ షెడ్యూల్ (Fourth Schedule) లో రాజ్యసభలో రాష్ట్రాలు మరియు UTs కు సీట్ల కేటాయింపు ఉంటుంది. మొదటి షెడ్యూల్ = రాష్ట్రాల పేర్లు మరియు భూభాగాలు."),

    (3, 1,
     "Article 4 కింద చేసిన చట్టాలు ఏ Schedules సవరించవచ్చు?",
     "Schedule 1 మరియు Schedule 7",
     "Schedule 1 మరియు Schedule 4",
     "Schedule 4 మరియు Schedule 6",
     "Schedule 1 మరియు Schedule 2",
     "b",
     "Article 4: Articles 2 మరియు 3 కింద చేసిన చట్టాలు First Schedule (రాష్ట్రాల పేర్లు) మరియు Fourth Schedule (రాజ్యసభ సీట్లు) సవరించవచ్చు. ఇవి Article 368 రాజ్యాంగ సవరణగా పరిగణించరు."),

    (3, 1,
     "కొత్త రాష్ట్రం ఏర్పాటైతే ఏ Schedule నేరుగా ప్రభావితం అవుతుంది?",
     "Second Schedule", "Third Schedule",
     "First Schedule", "Fifth Schedule",
     "c",
     "కొత్త రాష్ట్రం ఏర్పాటైతే First Schedule (రాష్ట్రాల జాబితా) నేరుగా మారుతుంది. రాజ్యసభ సీట్లు కూడా మారవచ్చు కాబట్టి Fourth Schedule కూడా ప్రభావితం అవుతుంది. Article 4 ఈ మార్పులకు అనుమతిస్తుంది."),

    # Moderate
    (3, 2,
     "కింది Schedules మరియు వాటి విషయాల జంటలు సరిగ్గా ఉన్నాయా?\n(P) First Schedule — రాష్ట్రాలు మరియు UTs పేర్లు\n(Q) Second Schedule — రాజ్యసభ సీట్ల కేటాయింపు\n(R) Fourth Schedule — రాజ్యసభ సీట్లు\n(S) Seventh Schedule — 3 జాబితాలు (Union, State, Concurrent)",
     "P, R మరియు S సరైనవి; Q తప్పు", "P, Q మరియు S సరైనవి",
     "P, Q, R మరియు S అన్నీ సరైనవి", "S మాత్రమే తప్పు",
     "a",
     "Q తప్పు — Second Schedule = రాష్ట్రపతి, గవర్నర్లు, స్పీకర్ మొదలైన వారి జీతాలు. Rajya Sabha seats = Fourth Schedule (R). P (First Schedule ✓), R (Fourth Schedule ✓), S (Seventh Schedule ✓)."),

    (3, 2,
     "Article 4 ప్రకారం Schedule 1 మరియు 4 మార్పులు రాజ్యాంగ సవరణ (Article 368) అవసరమా?",
     "అవును, అన్ని Schedule మార్పులకు Article 368 అవసరం",
     "లేదు — Article 4 కింద ఇవి సాధారణ చట్టంతో మారవచ్చు",
     "రాష్ట్రాల ఆమోదం తప్పనిసరి",
     "సుప్రీం కోర్టు అనుమతి అవసరం",
     "b",
     "Article 4 స్పష్టంగా చెప్తుంది: Articles 2 మరియు 3 కింద Schedule 1 మరియు 4 సవరణలు 'shall not be deemed to be amendments of this Constitution for the purposes of Article 368.' అందుకే సాధారణ మెజారిటీతో సరిపోతుంది."),

    # Tough
    (3, 3,
     "తెలంగాణ రాష్ట్రం 2014 లో ఏర్పాటైనప్పుడు ఏ Schedules మారాయి?",
     "First Schedule మాత్రమే",
     "Fourth Schedule మాత్రమే",
     "First Schedule మరియు Fourth Schedule రెండూ",
     "Seventh Schedule",
     "c",
     "తెలంగాణ (29వ రాష్ట్రం) ఏర్పాటు: First Schedule (కొత్త రాష్ట్రం పేరు జోడింపు) మరియు Fourth Schedule (రాజ్యసభ సీట్ల పునఃకేటాయింపు) రెండూ మారాయి. Article 4 ఈ మార్పులకు అనుమతిస్తుంది."),

    # Toughest
    (3, 4,
     "కింది వాటిలో Article 4 గురించి సరైనవి ఏవి?\n(1) Articles 2 & 3 కింద చేసిన చట్టాలు Schedule 1 & 4 సవరించవచ్చు\n(2) ఈ మార్పులు Article 368 కింద రాజ్యాంగ సవరణగా పరిగణిస్తారు\n(3) సాధారణ మెజారిటీతో Schedule 1 & 4 మార్చవచ్చు\n(4) రాష్ట్రాల ఆమోదం తప్పనిసరి",
     "1 మరియు 3 మాత్రమే సరైనవి", "1, 2 మరియు 3 సరైనవి",
     "1, 2, 3 మరియు 4 అన్నీ", "2 మరియు 4 మాత్రమే",
     "a",
     "2 తప్పు — Article 4 మార్పులు Article 368 రాజ్యాంగ సవరణగా పరిగణించరు. 4 తప్పు — రాష్ట్రాల ఆమోదం అవసరం లేదు (రాష్ట్ర అభిప్రాయం తీసుకుంటారు కానీ Binding కాదు). 1 (✓), 3 (✓)."),

    # ══════════════════════════════════════════
    # SECTION 4 — రాష్ట్రాల పునర్వ్యవస్థీకరణ (Bilingual)
    # ══════════════════════════════════════════

    # Easy — Bilingual
    (4, 1,
     "States Reorganisation Commission (SRC) 1953 అధ్యక్షుడు ఎవరు?\n(Who was the Chairman of the States Reorganisation Commission 1953?)",
     "K.M. Panikkar", "Hriday Nath Kunzru",
     "Fazl Ali", "V.P. Menon",
     "c",
     "States Reorganisation Commission (SRC) 1953 Chairman = Fazl Ali. అందుకే దీన్ని 'Fazl Ali Commission' అంటారు. మిగతా సభ్యులు: Hriday Nath Kunzru మరియు K.M. Panikkar. రిపోర్ట్ 1955 లో ఇచ్చారు."),

    (4, 1,
     "States Reorganisation Act 1956 ఆధారంగా ఏర్పడిన రాష్ట్రాలు మరియు UTs సంఖ్య ఏమిటి?\n(How many states and UTs were created under the States Reorganisation Act 1956?)",
     "10 రాష్ట్రాలు + 4 UTs",
     "14 రాష్ట్రాలు + 6 UTs",
     "12 రాష్ట్రాలు + 8 UTs",
     "17 రాష్ట్రాలు + 3 UTs",
     "b",
     "States Reorganisation Act 1956 ద్వారా 14 రాష్ట్రాలు మరియు 6 కేంద్ర పాలిత ప్రాంతాలు ఏర్పాటయ్యాయి. ఇవి భాష ఆధారంగా పునర్వ్యవస్థీకరించారు."),

    # Moderate — Bilingual
    (4, 2,
     "దేశంలో మొట్టమొదటి భాషా రాష్ట్రం (First Linguistic State) ఏది?\n(Which was the first linguistic state in India?)",
     "కర్ణాటక / Karnataka",
     "మహారాష్ట్ర / Maharashtra",
     "ఆంధ్ర రాష్ట్రం / Andhra State",
     "తమిళనాడు / Tamil Nadu",
     "c",
     "ఆంధ్ర రాష్ట్రం (Andhra State) — అక్టోబర్ 1, 1953న ఏర్పాటు. భారతదేశంలో మొట్టమొదటి భాషా రాష్ట్రం. Potti Sriramulu ఆమరణ నిరాహార దీక్ష (58 రోజులు) ఫలితంగా. మద్రాస్ (తమిళ) రాష్ట్రం నుండి వేరు పడింది."),

    (4, 2,
     "ఆంధ్రప్రదేశ్ ఏర్పాటు ఏ తేదీన జరిగింది? దానికి కారణమైన వ్యక్తి ఎవరు?\n(When was Andhra Pradesh formed? Who sacrificed for it?)",
     "నవంబర్ 1, 1956 — SRC ఆధారంగా; Potti Sriramulu త్యాగం",
     "అక్టోబర్ 1, 1953 — Cabinet Mission; B.N. Rau",
     "జనవరి 26, 1950 — రాజ్యాంగ అమలు; Nehru",
     "ఆగస్ట్ 15, 1947 — స్వాతంత్ర్యం; Ambedkar",
     "a",
     "నవంబర్ 1, 1956 — ఆంధ్ర రాష్ట్రం + హైదరాబాద్ రాష్ట్రంలో తెలుగు ప్రాంతాలు కలిసి ఆంధ్రప్రదేశ్ ఏర్పాటు. Potti Sriramulu ఆమరణ నిరాహార దీక్ష → ఆంధ్ర రాష్ట్రం (1953) → దానికి వ్యాప్తి → AP (1956)."),

    # Tough — Bilingual
    (4, 3,
     "States Reorganisation Act 1956 యొక్క ప్రధాన ఆధారం ఏమిటి?\n(What was the main basis of the States Reorganisation Act 1956?)",
     "మతం ఆధారంగా / On the basis of religion",
     "భాష ఆధారంగా / On the basis of language",
     "జనాభా ఆధారంగా / On the basis of population",
     "చారిత్రక సంస్కృతి ఆధారంగా / On historical culture",
     "b",
     "States Reorganisation Act 1956 ప్రధానంగా భాష (Language) ఆధారంగా రాష్ట్రాలు పునర్వ్యవస్థీకరించింది. Fazl Ali Commission సిఫారసు: భాష ప్రాతిపదిక ముఖ్యమైనది కానీ ఏకైక ఆధారం కాదు అని చెప్పారు. ఆంధ్ర = తెలుగు, కర్ణాటక = కన్నడ."),

    # Toughest — Bilingual
    (4, 4,
     "కింది వాటిలో States Reorganisation Commission 1953 గురించి సరైనవి ఏవి?\n(1) Fazl Ali = Chairman\n(2) K.M. Panikkar = సభ్యుడు\n(3) రిపోర్ట్ 1954 లో ఇచ్చారు\n(4) Hriday Nath Kunzru = సభ్యుడు",
     "1, 2 మరియు 4 మాత్రమే సరైనవి / 1, 2 and 4 only",
     "1, 2, 3 మరియు 4 అన్నీ / All",
     "2 మరియు 3 మాత్రమే / 2 and 3 only",
     "1 మరియు 3 మాత్రమే / 1 and 3 only",
     "a",
     "3 తప్పు — SRC రిపోర్ట్ 1955 లో ఇచ్చారు, 1954 లో కాదు. 1 (Fazl Ali Chairman ✓), 2 (K.M. Panikkar ✓), 4 (Hriday Nath Kunzru ✓). SRC = 3 మంది సభ్యులు."),

    # PYQ — APPSC Bilingual
    (4, 2,
     "భారతదేశంలో మొట్టమొదటి భాషా రాష్ట్రం ఏర్పాటైన తేదీ మరియు రాష్ట్రం ఏది? [APPSC Group 2]",
     "నవంబర్ 1, 1956 — ఆంధ్రప్రదేశ్",
     "అక్టోబర్ 1, 1953 — ఆంధ్ర రాష్ట్రం",
     "జనవరి 26, 1950 — కర్ణాటక",
     "ఆగస్ట్ 15, 1947 — తమిళనాడు",
     "b",
     "అక్టోబర్ 1, 1953 — ఆంధ్ర రాష్ట్రం భారతదేశంలో మొట్టమొదటి భాషా రాష్ట్రంగా ఏర్పాటైంది. Potti Sriramulu 58 రోజుల ఆమరణ నిరాహార దీక్ష ఫలితంగా. ఇది APPSC Group 2 లో తరచుగా వచ్చే ప్రశ్న.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 5 — అర్జిత భూభాగాలు (Bilingual)
    # ══════════════════════════════════════════

    # Easy — Bilingual
    (5, 1,
     "గోవా విముక్తి (Liberation of Goa) ఏ తేదీన జరిగింది?\n(On which date was Goa liberated?)",
     "August 15, 1947", "October 1, 1961",
     "December 19, 1961", "January 26, 1950",
     "c",
     "December 19, 1961 — Operation Vijay ద్వారా గోవా పోర్చుగీసు పాలన నుండి విముక్తి పొందింది. ఇది భారత సైనిక చర్య. 1987 లో Goa 25వ రాష్ట్రంగా ఏర్పాటైంది."),

    (5, 1,
     "సిక్కిం (Sikkim) ఏ రాజ్యాంగ సవరణ ద్వారా భారత రాష్ట్రంగా చేరింది?\n(Through which Constitutional Amendment did Sikkim become a state of India?)",
     "32వ సవరణ 1974", "35వ సవరణ 1974",
     "36వ సవరణ 1975", "37వ సవరణ 1975",
     "c",
     "36వ రాజ్యాంగ సవరణ 1975 ద్వారా సిక్కిం భారత్ లో 22వ రాష్ట్రంగా చేరింది. Article 2 కింద Parliament ద్వారా ప్రవేశం. Article 371F సిక్కిం కు ప్రత్యేక నిబంధనలు ఇస్తుంది."),

    # Moderate — Bilingual
    (5, 2,
     "పాండిచ్చేరి (Puducherry) భారత్ లో ఎప్పుడు కలిసింది?\n(When did Puducherry formally merge with India?)",
     "1947 — స్వాతంత్ర్యం తో పాటు",
     "1954 — De facto; 1962 — De jure (అధికారికంగా)",
     "1961 — Operation Vijay",
     "1975 — 36వ సవరణ",
     "b",
     "పాండిచ్చేరి (ఫ్రెంచ్ కాలనీ): 1954 — De facto transfer (ఫ్రెంచ్ వారు అప్పగించారు). 1962 — De jure (formal legal transfer, అంతర్జాతీయ చట్ట ప్రకారం అధికారికంగా). ప్రస్తుతం UT with Legislature."),

    (5, 2,
     "కింది వాటిలో అర్జిత భూభాగాలు మరియు సంవత్సరాలు సరిగ్గా జోడించండి:\n(P) Goa — (1) 1975\n(Q) Sikkim — (2) 1961\n(R) Puducherry (De jure) — (3) 1962\n(S) Dadra & Nagar Haveli — (4) 1961",
     "P-2, Q-1, R-3, S-4", "P-1, Q-2, R-3, S-4",
     "P-2, Q-3, R-1, S-4", "P-4, Q-1, R-2, S-3",
     "a",
     "Goa = 1961 Operation Vijay (P-2). Sikkim = 1975 (Q-1). Puducherry De jure = 1962 (R-3). Dadra & Nagar Haveli = 1961 India లో కలిపారు (S-4)."),

    # Tough — Bilingual
    (5, 3,
     "Article 2 కింద ప్రవేశించిన రాష్ట్రం ఏది?\n(Which state was admitted to India under Article 2?)",
     "తెలంగాణ (Telangana)", "ఆంధ్రప్రదేశ్ (Andhra Pradesh)",
     "సిక్కిం (Sikkim)", "గోవా (Goa)",
     "c",
     "సిక్కిం = Article 2 కింద (అప్పటికి Union లో లేని కొత్త రాష్ట్రం — 36వ సవరణ 1975 ద్వారా). తెలంగాణ మరియు AP = Article 3 కింద (ఉన్న రాష్ట్రాల పునర్వ్యవస్థీకరణ). Goa = Article 3 కింద 25వ రాష్ట్రంగా 1987 లో."),

    # Toughest — Bilingual
    (5, 4,
     "కింది జంటలు అన్నీ సరైనవేనా?\n(1) Goa Liberation = December 19, 1961 (Operation Vijay)\n(2) Sikkim = 36వ సవరణ 1975 = 22వ రాష్ట్రం\n(3) Puducherry De jure = 1954\n(4) Dadra & Nagar Haveli = 1961 India లో కలిపారు",
     "1, 2 మరియు 4 మాత్రమే సరైనవి / 1, 2 and 4 only",
     "1, 2, 3 మరియు 4 అన్నీ / All",
     "2 మరియు 3 తప్పు / 2 and 3 wrong",
     "1 మరియు 4 మాత్రమే / 1 and 4 only",
     "a",
     "3 తప్పు — Puducherry De facto = 1954, De jure = 1962 (అధికారిక చట్ట బదిలీ). 1954 De facto మాత్రమే. 1 (Operation Vijay 1961 ✓), 2 (36th 1975 ✓), 4 (Dadra 1961 ✓)."),

    # ══════════════════════════════════════════
    # SECTION 6 — J&K మరియు 2019 మార్పు (Bilingual)
    # ══════════════════════════════════════════

    # Easy — Bilingual
    (6, 1,
     "August 5, 2019న భారత ప్రభుత్వం J&K కి సంబంధించి ఏ ముఖ్య మార్పు చేసింది?\n(What major change was made regarding J&K on August 5, 2019?)",
     "J&K కు ప్రత్యేక హోదా పెంచారు",
     "Article 370 రద్దు చేసి J&K ను రెండు UTs గా విభజించారు",
     "J&K కు కొత్త రాజ్యాంగం ఇచ్చారు",
     "J&K ను పాకిస్థాన్ కు అప్పగించారు",
     "b",
     "August 5, 2019 — Article 370 రద్దు (Abrogation) + J&K Reorganisation Act 2019. J&K = UT with Legislature + Ladakh = UT without Legislature. అమలు October 31, 2019."),

    (6, 1,
     "2019 తర్వాత భారతదేశంలో మొత్తం రాష్ట్రాలు మరియు UTs సంఖ్య ఎంత?\n(What is the total number of states and UTs in India after 2019?)",
     "29 రాష్ట్రాలు + 7 UTs", "28 రాష్ట్రాలు + 8 UTs",
     "30 రాష్ట్రాలు + 7 UTs", "27 రాష్ట్రాలు + 9 UTs",
     "b",
     "J&K Reorganisation Act 2019 అమలు తర్వాత (October 31, 2019): 28 రాష్ట్రాలు + 8 UTs. J&K State → UT (with legislature) + Ladakh → UT (without legislature) = 2 UTs పెరిగాయి. ముందు 29 States + 7 UTs ఉండేవి."),

    # Moderate — Bilingual
    (6, 2,
     "J&K మరియు Ladakh మధ్య ముఖ్య తేడా 2019 తర్వాత ఏమిటి?\n(Key difference between J&K and Ladakh UTs after 2019?)",
     "J&K = UT without Legislature; Ladakh = UT with Legislature",
     "J&K = UT with Legislature (శాసనసభతో); Ladakh = UT without Legislature (శాసనసభ లేకుండా)",
     "రెండూ UT with Legislature",
     "రెండూ UT without Legislature",
     "b",
     "J&K = UT with Legislature (శాసనసభ ఉంటుంది — Delhi, Puducherry లాగా). Ladakh = UT without Legislature (శాసనసభ లేదు — Chandigarh, Lakshadweep లాగా). ఇది APPSC మరియు UPSC రెండిటిలో వచ్చే ముఖ్య ప్రశ్న."),

    (6, 2,
     "2020 లో ఏ రెండు UTs కలిసి ఒక UT అయింది?\n(Which two UTs merged into one UT in 2020?)",
     "Goa మరియు Daman & Diu",
     "Chandigarh మరియు Delhi",
     "Dadra & Nagar Haveli మరియు Daman & Diu",
     "Puducherry మరియు Lakshadweep",
     "c",
     "Dadra & Nagar Haveli మరియు Daman & Diu — 2020 లో కలిసి ఒక UT అయ్యాయి. ఫలితంగా UTs సంఖ్య 9 నుండి 8 కి తగ్గింది (J&K కాల మార్పు తర్వాత అంకలు పక్కాగా లెక్కించాలి)."),

    # Tough — Bilingual
    (6, 3,
     "Ladakh లో Legislature ఉందా లేదా? మరియు ఇప్పటికి అక్కడ ఏ రకమైన పాలన ఉంది?\n(Does Ladakh have a Legislature? What type of administration?)",
     "అవును, Legislature ఉంది — J&K లాగా",
     "లేదు, Legislature లేదు — Lieutenant Governor ద్వారా నేరుగా Central పాలన",
     "అవును, రెండు సభలు ఉన్నాయి",
     "లేదు, Ladakh లో ఎన్నికలు జరగవు",
     "b",
     "Ladakh = UT without Legislature. Lieutenant Governor (LG) ద్వారా కేంద్ర పాలన. Chandigarh, Lakshadweep, Andaman & Nicobar వలే. J&K = UT with Legislature (Delhi, Puducherry వలే)."),

    # Toughest — Bilingual
    (6, 4,
     "అభికథనం-కారణం సరైనవా? / Assertion (A): After the J&K Reorganisation Act 2019, India has 28 states and 8 Union Territories.\nReason (R): J&K was bifurcated into two Union Territories — J&K (with legislature) and Ladakh (without legislature) — reducing the number of states from 29 to 28.",
     "A మరియు R రెండూ సరైనవి, R అనేది A కి సరైన వివరణ / Both correct, R explains A",
     "A మరియు R రెండూ సరైనవి, కానీ R వివరణ కాదు / Both correct, R doesn't explain",
     "A సరైనది, R తప్పు / A correct, R wrong",
     "A తప్పు, R సరైనది / A wrong, R correct",
     "a",
     "2019 తర్వాత 28 States + 8 UTs (A — correct). J&K State → 2 UTs: J&K (with legislature) + Ladakh (without legislature), States 29→28 (R — correct and explains the reduction). R అనేది A కి సరైన వివరణ."),

    # PYQ — APPSC Bilingual
    (6, 2,
     "J&K Reorganisation Act 2019 ప్రకారం జమ్మూ కాశ్మీర్ ఏ రూపంలో ఉంది? [APPSC Group 2]",
     "పూర్తి రాష్ట్రంగా — ప్రత్యేక హోదాతో",
     "UT with Legislature (శాసనసభతో కేంద్ర పాలిత ప్రాంతం)",
     "UT without Legislature",
     "స్వతంత్ర ప్రదేశంగా",
     "b",
     "J&K Reorganisation Act 2019 తర్వాత: జమ్మూ కాశ్మీర్ = UT with Legislature (శాసనసభ ఉంటుంది, Lieutenant Governor అధికారి). లడఖ్ = UT without Legislature. APPSC Group 2 లో ఇది ముఖ్యమైన ప్రశ్న.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 7 — ప్రస్తుత రాష్ట్రాలు మరియు Schedules (Bilingual)
    # ══════════════════════════════════════════

    # Easy — Bilingual
    (7, 1,
     "ప్రస్తుతం (2024) భారతదేశంలో మొత్తం రాష్ట్రాలు ఎన్ని?\n(How many states are there in India currently as of 2024?)",
     "25", "27", "28", "29",
     "c",
     "ప్రస్తుతం (2024) భారతదేశంలో 28 రాష్ట్రాలు. 2019 J&K Reorganisation తర్వాత 29 నుండి 28 కి తగ్గింది. మొత్తం 8 UTs ఉన్నాయి."),

    (7, 1,
     "శాసనసభ (Legislature) ఉన్న UTs ఏవి?\n(Which UTs have a Legislature?)",
     "Chandigarh మరియు Lakshadweep",
     "Delhi (NCT), Puducherry మరియు Jammu & Kashmir",
     "Andaman & Nicobar మరియు Ladakh",
     "అన్ని UTs కి Legislature ఉంటుంది",
     "b",
     "Legislature ఉన్న UTs: Delhi (NCT), Puducherry, Jammu & Kashmir (2019 తర్వాత). Legislature లేని UTs: Chandigarh, Lakshadweep, Andaman & Nicobar Islands, Dadra & Nagar Haveli & Daman & Diu, Ladakh."),

    # Moderate — Bilingual
    (7, 2,
     "29వ రాష్ట్రంగా తెలంగాణ ఏర్పాటైన తేదీ ఏది?\n(When was Telangana formed as the 29th state of India?)",
     "జనవరి 1, 2014 / January 1, 2014",
     "జూన్ 2, 2014 / June 2, 2014",
     "అక్టోబర్ 1, 2014 / October 1, 2014",
     "నవంబర్ 1, 2014 / November 1, 2014",
     "b",
     "జూన్ 2, 2014 — తెలంగాణ భారతదేశంలో 29వ రాష్ట్రంగా ఏర్పాటైంది. ఆంధ్రప్రదేశ్ పునర్వ్యవస్థీకరణ చట్టం 2014 ద్వారా. Article 3 కింద పార్లమెంట్ ఆమోదించింది."),

    (7, 2,
     "కింది రాష్ట్రాలు మరియు వాటి ఏర్పాటు తేదీలు సరిగ్గా జోడించండి:\n(P) ఆంధ్ర రాష్ట్రం — (1) నవంబర్ 1, 1956\n(Q) ఆంధ్రప్రదేశ్ — (2) జూన్ 2, 2014\n(R) తెలంగాణ — (3) అక్టోబర్ 1, 1953\n(S) Goa రాష్ట్రం — (4) మే 30, 1987",
     "P-3, Q-1, R-2, S-4", "P-1, Q-3, R-2, S-4",
     "P-3, Q-2, R-1, S-4", "P-3, Q-1, R-4, S-2",
     "a",
     "ఆంధ్ర రాష్ట్రం = October 1, 1953 (P-3). ఆంధ్రప్రదేశ్ = November 1, 1956 (Q-1). తెలంగాణ = June 2, 2014 (R-2). Goa రాష్ట్రం = May 30, 1987 (S-4). Goa UT (1961) → State (1987)."),

    # Tough — Bilingual
    (7, 3,
     "Goa UT నుండి రాష్ట్రంగా ఏ సంవత్సరం మారింది? అది ఏ నంబర్ రాష్ట్రం?\n(In which year did Goa become a state from UT? What number state?)",
     "1961 లో — 24వ రాష్ట్రం", "1975 లో — 21వ రాష్ట్రం",
     "1987 లో — 25వ రాష్ట్రం", "2000 లో — 26వ రాష్ట్రం",
     "c",
     "Goa 1961 లో Operation Vijay ద్వారా విముక్తి పొందింది. తర్వాత UT గా ఉంది. 1987 లో 25వ రాష్ట్రంగా ఏర్పాటైంది. Daman & Diu UT గా వేరుగా ఉంది (తర్వాత Dadra & Nagar Haveli తో కలిసింది 2020)."),

    # Toughest — Bilingual
    (7, 4,
     "కింది వాటిలో అన్నీ సరైన జంటలు ఏవి?\n(1) 22వ రాష్ట్రం = సిక్కిం (1975)\n(2) 25వ రాష్ట్రం = గోవా (1987)\n(3) 29వ రాష్ట్రం = తెలంగాణ (2014)\n(4) 28వ రాష్ట్రం = జార్ఖండ్ (2000)",
     "1, 2 మరియు 3 మాత్రమే సరైనవి", "1, 2, 3 మరియు 4 అన్నీ",
     "2 మరియు 4 తప్పు", "1 మరియు 3 మాత్రమే",
     "b",
     "అన్నీ సరైనవే: సిక్కిం = 22వ రాష్ట్రం 1975 (1), గోవా = 25వ రాష్ట్రం 1987 (2), తెలంగాణ = 29వ రాష్ట్రం 2014 (3), జార్ఖండ్ = 28వ రాష్ట్రం November 15, 2000 (4). ఇవన్నీ సరైనవే."),

    # PYQ — UPSC Bilingual
    (7, 2,
     "కింది జోడీలలో సరైనది ఏది? / Which of the following is/are correctly matched? [UPSC Style]\n(1) Sikkim — 36th Amendment 1975 — 22nd State\n(2) Goa — 25th State — 1987\n(3) Telangana — 28th State — 2014",
     "1 మరియు 2 మాత్రమే / 1 and 2 only",
     "2 మరియు 3 మాత్రమే / 2 and 3 only",
     "1 మరియు 3 తప్పు / 1 and 3 wrong",
     "1, 2 మరియు 3 అన్నీ సరైనవి / All correct",
     "a",
     "3 తప్పు — తెలంగాణ = 29వ రాష్ట్రం (28వ కాదు). 28వ రాష్ట్రం = జార్ఖండ్ (2000). 1 (Sikkim = 22nd State 1975 ✓), 2 (Goa = 25th 1987 ✓). UPSC లో State numbering పై ప్రశ్నలు తరచుగా వస్తాయి.",
     "UPSC"),
]


# ─────────────────────────────────────────────
#  SEED FUNCTIONS
# ─────────────────────────────────────────────

def _seed_polity_ch5_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
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
        (5, 'Indian_Polity'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True,
                'message': 'Polity Ch5 notes already seeded.'}
    if row and force:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (5, 'Indian_Polity'))
    if use_postgres:
        conn.commit()

    db_exec_fn(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'Indian_Polity', '', 5,
         'యూనియన్ మరియు దాని భూభాగం',
         'Union and its Territory',
         'Ch.5',
         _json.dumps(POLITY_CH5_SECTIONS, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'Polity Ch5 notes seeded!'}


def _seed_polity_ch5_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
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
        (5, 'Indian_Polity'))
    row = cur.fetchone()
    if not row:
        _seed_polity_ch5_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)
        cur = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (5, 'Indian_Polity'))
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
    for mcq in POLITY_CH5_MCQS:
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

    total = len(POLITY_CH5_MCQS)
    return {
        'success': True,
        'message': f'Polity Ch5 MCQs seeded! Total: {total}',
        'inserted': total,
        'easy': easy, 'medium': medium, 'hard': hard,
        'toughest': toughest, 'pyq': pyq
    }
