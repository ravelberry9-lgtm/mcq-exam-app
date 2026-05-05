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

    # ══════════════ SECTION 0 — Article 1 / Union of States ══════════════

    (0, 1,
     "Under Article 1, what type of state is India?\nతెలుగు: ఆర్టికల్ 1 ప్రకారం భారతదేశం ఏ రకమైన రాజ్యం?",
     "Federation of States / రాష్ట్రాల సమాఖ్య",
     "Confederation of States / రాష్ట్రాల కూటమి",
     "Union of States / రాష్ట్రాల యూనియన్ (correct)",
     "Unitary State / ఏకీకృత రాజ్యం",
     "c",
     "Article 1: 'India, that is Bharat, shall be a UNION of States.' Dr. Ambedkar deliberately chose 'Union' (not 'Federation') to emphasize states cannot secede."),

    (0, 1,
     "Under Article 1, how many types of territories does India have?\nతెలుగు: ఆర్టికల్ 1 ప్రకారం భారత భూభాగం ఎన్ని రకాలు?",
     "Two / రెండు రకాలు",
     "Three / మూడు రకాలు (correct)",
     "Four / నాలుగు రకాలు",
     "Five / ఐదు రకాలు",
     "b",
     "Article 1 lists THREE types: (a) Territories of states, (b) Union Territories, (c) Other territories that may be acquired."),

    (0, 1,
     "In which Schedule are the names of states and UTs listed?\nతెలుగు: రాష్ట్రాలు మరియు UTs పేర్లు ఏ షెడ్యూల్‌లో?",
     "Second Schedule / రెండవ షెడ్యూల్",
     "First Schedule / మొదటి షెడ్యూల్ (correct)",
     "Fourth Schedule / నాల్గవ షెడ్యూల్",
     "Seventh Schedule / ఏడవ షెడ్యూల్",
     "b",
     "First Schedule lists names of states and UTs along with their territories. Fourth Schedule = Rajya Sabha seat allocation."),

    (0, 2,
     "Regarding Article 1, which of the following are CORRECT?\n(1) 'India that is Bharat' — both names are official\n(2) India = Union of States\n(3) Indian territory has 4 types\n(4) State names listed in First Schedule\nతెలుగు: కింది వాటిలో ఆర్టికల్ 1 గురించి సరైనవి ఏవి?\n(1) 'India that is Bharat' — రెండు పేర్లు అధికారికం\n(2) India = Union of States\n(3) భూభాగం 4 రకాలు\n(4) First Schedule లో పేర్లు",
     "1, 2 and 4 only / 1, 2 మరియు 4 మాత్రమే (correct)",
     "1 and 2 only / 1 మరియు 2 మాత్రమే",
     "All four / అన్నీ",
     "2, 3 and 4 only / 2, 3 మరియు 4 మాత్రమే",
     "a",
     "Statements 1, 2, 4 correct. Statement 3 wrong — Article 1 lists THREE (not 4) territory types."),

    (0, 2,
     "Difference between 'Union of States' and 'Federation of States' in Article 1?\nతెలుగు: 'Union of States' vs 'Federation of States' తేడా?",
     "Both same meaning / రెండూ ఒకే అర్థం",
     "Union: states have no right to secede; Federation: states can secede / Union లో రాష్ట్రాలకు వేరుపడే హక్కు లేదు (correct)",
     "Federation strong centre; Union strong states / తారుమారు",
     "Different number of states / తేడా రాష్ట్రాల సంఖ్య",
     "b",
     "Ambedkar's deliberate choice: 'Union' = states cannot secede + Indian states are CREATED by the Constitution. 'Federation' (USA) = states retain inherent sovereignty + can theoretically leave."),

    (0, 3,
     "What did Dr. Ambedkar mean by 'India is an Indestructible Union of Destructible States'?\nతెలుగు: అంబేడ్కర్ ఈ వాక్యం అర్థం?",
     "States are permanent; Union changes / రాష్ట్రాలు శాశ్వత",
     "Union is permanent; states can be reorganised / Union స్థిరం; రాష్ట్రాలు మార్చవచ్చు (correct)",
     "Both Union and states are permanent / రెండూ స్థిరం",
     "States are not subject to Union / రాష్ట్రాలు Union కి లోబడవు",
     "b",
     "Ambedkar's famous statement means: the UNION cannot be broken by states leaving (indestructible), but state boundaries/names/numbers CAN be changed by Parliament (destructible)."),

    (0, 4,
     "Assertion (A): India is described as a 'Union of States' and not a 'Federation of States' in Article 1.\nReason (R): In India, the Constitution is supreme, states are created by the Constitution, and they cannot secede from the Union — unlike the USA where states formed the federation.\nతెలుగు: అభికథనం-కారణం సరైనవా?",
     "Both correct, R explains A / రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "Both correct, R doesn't explain / రెండూ సరైనవి, R వివరణ కాదు",
     "A correct, R wrong / A సరైనది, R తప్పు",
     "A wrong, R correct / A తప్పు, R సరైనది",
     "a",
     "Both correct. R precisely explains A — the very reason 'Union' was chosen over 'Federation' is that Indian states cannot secede + were created by the Constitution."),

    (0, 2,
     "What did Article 1 call India? [APPSC Group 2]\nతెలుగు: ఆర్టికల్ 1 ప్రకారం భారత్ ఏమి?",
     "Federation of States / రాష్ట్రాల సమాఖ్య",
     "Union of States / రాష్ట్రాల యూనియన్ (correct)",
     "Unitary Republic / ఏకీకృత గణతంత్రం",
     "Confederation of States / రాష్ట్రాల కూటమి",
     "b",
     "Article 1: 'India, that is Bharat, shall be a UNION of States.' Standard APPSC answer.",
     "APPSC"),

    # ══════════════ SECTION 1 — Articles 2, 3, 4 ══════════════

    (1, 1,
     "What can Parliament do under Article 3?\nతెలుగు: ఆర్టికల్ 3 కింద పార్లమెంట్ ఏమి చేయగలదు?",
     "Form new states, alter boundaries, change names / కొత్త రాష్ట్రాలు, సరిహద్దులు, పేర్లు మార్చడం (correct)",
     "Appoint state governors / గవర్నర్లను నియమించడం",
     "Remove state CMs / ముఖ్యమంత్రులను తొలగించడం",
     "Limit state powers / రాష్ట్ర అధికారాలను పరిమితం చేయడం",
     "a",
     "Article 3: Parliament can (a) form new states, (b) alter areas/boundaries, (c) change names of existing states. Common with Article 2 (admission of new territories)."),

    (1, 1,
     "What majority is required in Parliament under Article 3 to form new states?\nతెలుగు: ఆర్టికల్ 3 కింద కొత్త రాష్ట్రం ఏర్పాటుకు ఏ మెజారిటీ?",
     "2/3 majority + state ratification / 2/3 + రాష్ట్రాల ఆమోదం",
     "Simple Majority / సాధారణ మెజారిటీ (correct)",
     "Joint sitting 2/3 / ఉమ్మడి సమావేశం 2/3",
     "Unanimous / ఏకగ్రీవం",
     "b",
     "Article 3 only requires SIMPLE MAJORITY (not the special majority of Article 368). This is what makes states 'destructible' even though the Union is 'indestructible'."),

    (1, 1,
     "Under Article 3, the affected state legislature's opinion is —\nతెలుగు: సంబంధిత రాష్ట్ర శాసనసభ అభిప్రాయం —",
     "Binding on Parliament / తప్పనిసరిగా అంగీకరించాలి",
     "Not required / అవసరం లేదు",
     "Required but NOT binding on Parliament / తీసుకోవాలి, కానీ Binding కాదు (correct)",
     "President decides / రాష్ట్రపతి నిర్ణయం",
     "c",
     "President MUST refer the bill to the affected state legislature for OPINION, but the opinion is NOT binding on Parliament. Parliament can override or ignore it."),

    (1, 2,
     "Key difference between Article 2 and Article 3?\nతెలుగు: Article 2 vs Article 3 ముఖ్య తేడా?",
     "Article 2 = name change; Article 3 = new states / తారుమారు",
     "Article 2 = admit/establish NEW territories not yet in Union; Article 3 = reorganise EXISTING states / Article 2 బాహ్య; Article 3 ఉన్న రాష్ట్రాలు (correct)",
     "Article 2 = boundary; Article 3 = UT / తారుమారు",
     "Both same / రెండూ ఒకటే",
     "b",
     "Article 2 = ADMISSION of new states (territories not in Union — e.g., Sikkim 1975) OR ESTABLISHMENT of new territories. Article 3 = REORGANISATION of existing states (split, merge, rename)."),

    (1, 2,
     "What condition is mandatory for introducing a Bill under Article 3?\nతెలుగు: Article 3 Bill ప్రవేశపెట్టడానికి తప్పనిసరి?",
     "Rajya Sabha consent first / రాజ్యసభ అనుమతి",
     "President's recommendation is mandatory / రాష్ట్రపతి సిఫారసు తప్పనిసరి (correct)",
     "Supreme Court permission / సుప్రీం కోర్టు అనుమతి",
     "Cabinet unanimity / Cabinet ఏకగ్రీవం",
     "b",
     "Article 3 Bill can only be introduced WITH the prior recommendation of the PRESIDENT. President must also refer the Bill to the affected state legislature for opinion."),

    (1, 3,
     "Which is correct about Article 4?\nతెలుగు: Article 4 గురించి సరైనది?",
     "Article 4 = Constitutional Amendment Procedure (like Article 368) / రాజ్యాంగ సవరణ విధానం",
     "Article 4: Laws under it can amend Schedule 1 and 4 — Article 368 NOT required / Schedule 1 & 4 సవరించవచ్చు; Article 368 అవసరం లేదు (correct)",
     "Article 4 = Power to form new states / కొత్త రాష్ట్రాలు",
     "Article 4 = Bans boundary changes / సరిహద్దు మార్పు నిషేధం",
     "b",
     "Article 4: Laws made under Articles 2 and 3 can amend Schedules 1 and 4 (state names + RS seats), and these are NOT considered Constitutional Amendments under Article 368 — simple majority suffices."),

    (1, 4,
     "Are these pairs all correctly matched?\n(1) Article 1 — Union of States, Territory definition\n(2) Article 2 — Parliament can admit/establish new states\n(3) Article 3 — Parliament can form, alter, rename states — needs President's recommendation\n(4) Article 4 — Alteration of Schedules 1 and 4 treated as Article 368 amendment\nతెలుగు: కింది జంటలు అన్నీ సరైనవేనా?",
     "Only 1, 2 and 3 correct / 1, 2 మరియు 3 మాత్రమే సరైనవి (correct)",
     "All four correct / అన్నీ",
     "2 and 4 wrong / 2 మరియు 4 తప్పు",
     "Only 3 and 4 / 3 మరియు 4 మాత్రమే",
     "a",
     "Pair 4 is WRONG — Article 4 explicitly says these alterations are NOT to be treated as constitutional amendments under Article 368. Pairs 1, 2, 3 correct."),

    (1, 2,
     "Under which Article can Parliament form new states or alter boundaries? [UPSC Style]\nతెలుగు: కొత్త రాష్ట్రాలు ఏర్పాటు ఏ అధికరణం?",
     "Article 1",
     "Article 2",
     "Article 3 (correct)",
     "Article 4",
     "c",
     "Article 3: 'Formation of new states and alteration of areas, boundaries or names of existing states.' Article 2 covers admission of NEW territories only.",
     "UPSC"),

    # ══════════════ SECTION 2 — Federal vs Unitary, India vs USA ══════════════

    (2, 1,
     "What does Ambedkar's 'Indestructible Union of Destructible States' mean?\nతెలుగు: 'Indestructible Union of Destructible States' అంటే?",
     "States are permanent; Union changes / రాష్ట్రాలు శాశ్వతం",
     "Union is permanent; states can be reorganised/split / Union స్థిరం; రాష్ట్రాలు మార్చవచ్చు (correct)",
     "States can leave the Union / రాష్ట్రాలు వెళ్లవచ్చు",
     "Both fixed permanently / రెండూ స్థిరం",
     "b",
     "Union = INDESTRUCTIBLE (states cannot secede). States = DESTRUCTIBLE (Parliament can split/merge/rename them under Article 3)."),

    (2, 1,
     "In USA, states formed the Federation. What happened in India?\nతెలుగు: USA లో రాష్ట్రాలు Federation; India లో ఏమి?",
     "States formed Union too / రాష్ట్రాలు Union ఏర్పాటు",
     "Constitution created the states; states did NOT create the Union / రాజ్యాంగం రాష్ట్రాలను సృష్టించింది (correct)",
     "People created the states / ప్రజలు రాష్ట్రాలను సృష్టించారు",
     "British created the states / బ్రిటిష్ సృష్టించారు",
     "b",
     "Reverse of USA: USA = states pre-existed and joined the Union. India = Constitution CREATED the states; they draw existence from the Constitution → cannot secede."),

    (2, 1,
     "How did K.C. Wheare describe Indian federalism?\nతెలుగు: K.C. Wheare భారత సమాఖ్య వ్యవస్థను ఏమని?",
     "Pure Federal System / పూర్తిగా Federal",
     "Unitary System / Unitary",
     "Quasi-Federal System / Quasi-Federal (correct)",
     "Confederal System / Confederal",
     "c",
     "K.C. Wheare's classic description: 'India is a Quasi-Federal state' — federal in form, but with strong centralising tendencies."),

    (2, 2,
     "What are the differences between USA Federation and Indian Union?\n(1) USA: states formed the Union; India: Constitution created the states\n(2) USA: residuary powers with states; India: with Centre\n(3) USA: states can secede; India: cannot\n(4) Federal Features identical in both\nతెలుగు: USA Federation vs India Union తేడాలు?\n(1) USA లో States Union ఏర్పాటు; India లో Constitution States ఏర్పాటు\n(2) USA లో Residuary States కి; India లో Centre కి\n(3) USA లో States వేరు పడవచ్చు; India లో లేదు\n(4) Federal Features ఒకటే",
     "1, 2 and 3 only correct / 1, 2 మరియు 3 మాత్రమే (correct)",
     "1 and 3 only / 1 మరియు 3 మాత్రమే",
     "All four / అన్నీ",
     "2 and 4 only / 2 మరియు 4 మాత్రమే",
     "a",
     "Pair 4 is wrong — Federal features differ significantly between USA and India. The other three differences are accurate."),

    (2, 2,
     "Who described Indian federalism as 'Cooperative Federalism'?\nతెలుగు: 'Cooperative Federalism' ఎవరు అన్నారు?",
     "K.C. Wheare / K.C. వేర్",
     "Granville Austin / గ్రాన్‌విల్ ఆస్టిన్ (correct)",
     "Dr. Ambedkar / అంబేడ్కర్",
     "Jawaharlal Nehru / నెహ్రూ",
     "b",
     "Granville Austin called it 'Cooperative Federalism' — Centre and States working in partnership, not rigid separation. K.C. Wheare = 'Quasi-Federal'."),

    (2, 3,
     "Absence of states' right to secede in India shows which feature?\nతెలుగు: 'Right to Secede' లేకపోవడం ఏ లక్షణం?",
     "Federal Feature / సమాఖ్య లక్షణం",
     "Unitary Feature — strong Centre / ఏకీకృత లక్షణం (correct)",
     "Parliamentary Feature / పార్లమెంటరీ లక్షణం",
     "Secular Feature / లౌకిక లక్షణం",
     "b",
     "Lack of secession right = strong UNITARY feature. (USA states have inherent sovereignty; Indian states are subordinate to the Constitution — Centre dominates.)"),

    (2, 4,
     "Assertion (A): India is described as a Union, not a Federation, because the states of India have no right to secede.\nReason (R): Unlike the USA, where states came together to form a federation and retain certain inherent rights, the Indian states were created by the Constitution and draw their existence from it.\nతెలుగు: అభికథనం-కారణం సరైనవా?",
     "Both correct, R explains A / రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "Both correct, R doesn't explain / రెండూ సరైనవి, R వివరణ కాదు",
     "A correct, R wrong / A సరైనది, R తప్పు",
     "A wrong, R correct / A తప్పు, R సరైనది",
     "a",
     "Both correct. R precisely explains A — the very fact that the Constitution CREATED Indian states (rather than states forming the Constitution) is why they cannot secede and India is called a Union."),

    # ══════════════ SECTION 3 — Schedules and Article 4 ══════════════

    (3, 1,
     "In which Schedule is Rajya Sabha seat allocation to states?\nతెలుగు: రాజ్యసభలో రాష్ట్రాలకు సీట్ల కేటాయింపు ఏ షెడ్యూల్?",
     "First Schedule / మొదటి షెడ్యూల్",
     "Second Schedule / రెండవ షెడ్యూల్",
     "Third Schedule / మూడవ షెడ్యూల్",
     "Fourth Schedule / నాల్గవ షెడ్యూల్ (correct)",
     "d",
     "Fourth Schedule = Allocation of seats in the Rajya Sabha to states and UTs. First Schedule = state names + territories."),

    (3, 1,
     "Laws under Article 4 can amend which Schedules?\nతెలుగు: Article 4 కింద ఏ Schedules సవరించవచ్చు?",
     "Schedules 1 and 7 / Schedule 1 + 7",
     "Schedules 1 and 4 / Schedule 1 + 4 (correct)",
     "Schedules 4 and 6 / Schedule 4 + 6",
     "Schedules 1 and 2 / Schedule 1 + 2",
     "b",
     "Article 4 allows simple-majority laws under Articles 2 and 3 to amend Schedule 1 (state names) and Schedule 4 (RS seats) WITHOUT triggering Article 368 amendment procedure."),

    (3, 1,
     "When a new state is formed, which Schedule is directly affected?\nతెలుగు: కొత్త రాష్ట్రం ఏర్పాటైతే ఏ Schedule మారుతుంది?",
     "Second Schedule / రెండవ",
     "Third Schedule / మూడవ",
     "First Schedule / మొదటి (correct)",
     "Fifth Schedule / ఐదవ",
     "c",
     "First Schedule directly contains state/UT names + their territorial limits. New state = First Schedule must be updated. Fourth Schedule (RS seats) typically also updated."),

    (3, 2,
     "Are these Schedule pairings correctly matched?\n(P) First Schedule — State and UT names\n(Q) Second Schedule — Rajya Sabha seat allocation\n(R) Fourth Schedule — Rajya Sabha seats\n(S) Seventh Schedule — Three Lists (Union, State, Concurrent)\nతెలుగు: కింది Schedules సరిగ్గా జతగా ఉన్నాయా?\n(P) First — రాష్ట్రాలు + UTs పేర్లు\n(Q) Second — రాజ్యసభ సీట్ల కేటాయింపు\n(R) Fourth — రాజ్యసభ సీట్లు\n(S) Seventh — 3 జాబితాలు",
     "P, R and S correct; Q wrong / P, R, S సరైనవి; Q తప్పు (correct)",
     "P, Q and S correct / P, Q, S సరైనవి",
     "All correct / అన్నీ సరైనవి",
     "Only S wrong / S మాత్రమే తప్పు",
     "a",
     "Pair Q is wrong — Second Schedule = SALARIES of constitutional officials (NOT RS seat allocation). RS seats = Fourth Schedule. P, R, S are correct."),

    (3, 2,
     "Under Article 4, do amendments to Schedules 1 and 4 require Article 368 procedure?\nతెలుగు: Article 4 ద్వారా Schedule 1 + 4 మార్పులకు Article 368 అవసరమా?",
     "Yes, all Schedule changes need Article 368 / అన్ని మార్పులకు అవసరం",
     "No — Article 4 allows simple-majority law to do it / లేదు; సాధారణ చట్టంతో మార్చవచ్చు (correct)",
     "State ratification mandatory / రాష్ట్రాల ఆమోదం",
     "Supreme Court permission / సుప్రీం కోర్టు అనుమతి",
     "b",
     "Article 4 explicitly says these alterations are NOT to be deemed Constitutional Amendments under Article 368 — simple majority is enough."),

    (3, 3,
     "When Telangana was formed in 2014, which Schedules were amended?\nతెలుగు: తెలంగాణ 2014లో ఏర్పాటై ఏ Schedules మారాయి?",
     "Only First Schedule / మొదటి మాత్రమే",
     "Only Fourth Schedule / నాల్గవ మాత్రమే",
     "Both First and Fourth / మొదటి + నాల్గవ రెండూ (correct)",
     "Seventh Schedule / ఏడవ",
     "c",
     "Telangana's formation needed BOTH: First Schedule (added Telangana, modified AP) + Fourth Schedule (allocated 7 RS seats to Telangana, reduced AP from 18 to 11)."),

    (3, 4,
     "Regarding Article 4, which of the following are CORRECT?\n(1) Laws under Articles 2 & 3 can amend Schedule 1 & 4\n(2) These amendments are treated as Article 368 amendments\n(3) Schedule 1 & 4 can be amended by simple majority\n(4) State ratification is mandatory\nతెలుగు: Article 4 గురించి సరైనవి?\n(1) Articles 2 & 3 → Schedule 1 & 4 సవరణ\n(2) ఇవి Article 368 సవరణగా\n(3) సాధారణ మెజారిటీతో సవరణ\n(4) రాష్ట్రాల ఆమోదం తప్పనిసరి",
     "Only 1 and 3 correct / 1 మరియు 3 మాత్రమే సరైనవి (correct)",
     "1, 2 and 3 correct / 1, 2 మరియు 3",
     "All four / అన్నీ",
     "2 and 4 only / 2 మరియు 4 మాత్రమే",
     "a",
     "Only 1 and 3 correct. Statement 2 wrong — Article 4 says these are NOT Article 368 amendments. Statement 4 wrong — state ratification NOT required (just opinion under Article 3)."),

    # ══════════════ SECTION 4 — States Reorganisation Commission ══════════════

    (4, 1,
     "Who was the Chairman of the States Reorganisation Commission 1953?\nతెలుగు: SRC 1953 అధ్యక్షుడు?",
     "K.M. Panikkar / K.M. పన్నికర్",
     "Hriday Nath Kunzru / హృదయ నాథ్ కుంజ్రూ",
     "Fazl Ali / ఫజల్ అలీ (correct)",
     "V.P. Menon / V.P. మేనన్",
     "c",
     "Fazl Ali (Chairman) + K.M. Panikkar + Hriday Nath Kunzru — three-member SRC (1953). Submitted report in 1955; led to States Reorganisation Act 1956."),

    (4, 1,
     "How many states and UTs were created under the States Reorganisation Act 1956?\nతెలుగు: SR Act 1956 ఆధారంగా ఎన్ని రాష్ట్రాలు + UTs?",
     "10 states + 4 UTs / 10 + 4",
     "14 states + 6 UTs / 14 రాష్ట్రాలు + 6 UTs (correct)",
     "12 states + 8 UTs / 12 + 8",
     "17 states + 3 UTs / 17 + 3",
     "b",
     "States Reorganisation Act 1956 created 14 states + 6 UTs — replacing the Part A/B/C/D classification of 1950."),

    (4, 2,
     "Which was the FIRST linguistic state in India?\nతెలుగు: మొట్టమొదటి భాషా రాష్ట్రం?",
     "Karnataka / కర్ణాటక",
     "Maharashtra / మహారాష్ట్ర",
     "Andhra State / ఆంధ్ర రాష్ట్రం (correct — 1953)",
     "Tamil Nadu / తమిళనాడు",
     "c",
     "Andhra State (1953) was India's FIRST linguistic state — formed after Potti Sriramulu's 56-day fast and his death (15 Dec 1952). This led to SRC's appointment."),

    (4, 2,
     "When was Andhra Pradesh formed and who sacrificed for it?\nతెలుగు: AP ఏర్పాటు తేదీ + త్యాగి?",
     "Nov 1, 1956 (SRC) + Potti Sriramulu / 1956 నవంబర్ 1; పొట్టి శ్రీరాములు (correct)",
     "Oct 1, 1953 + B.N. Rau",
     "Jan 26, 1950 + Nehru",
     "Aug 15, 1947 + Ambedkar",
     "a",
     "Andhra Pradesh = formed on November 1, 1956 by merging Telangana (Hyderabad State) with Andhra State. Potti Sriramulu's 1952 fast/death = trigger for ANDHRA STATE (Oct 1, 1953); APP came later."),

    (4, 3,
     "Main basis of the States Reorganisation Act 1956?\nతెలుగు: SR Act 1956 ప్రధాన ఆధారం?",
     "Religion / మతం",
     "Language / భాష (correct)",
     "Population / జనాభా",
     "Historical culture / చారిత్రక సంస్కృతి",
     "b",
     "SR Act 1956 reorganised states ON LINGUISTIC LINES (recommended by SRC). Marked the abandonment of British-era administrative boundaries."),

    (4, 4,
     "Regarding the SRC 1953, which of the following are CORRECT?\n(1) Fazl Ali = Chairman\n(2) K.M. Panikkar = member\n(3) Report submitted in 1954\n(4) Hriday Nath Kunzru = member\nతెలుగు: SRC 1953 గురించి సరైనవి ఏవి?\n(1) Fazl Ali = Chairman\n(2) K.M. Panikkar = సభ్యుడు\n(3) రిపోర్ట్ 1954\n(4) Hriday Nath Kunzru = సభ్యుడు",
     "1, 2 and 4 only / 1, 2 మరియు 4 మాత్రమే (correct)",
     "All four / అన్నీ",
     "2 and 3 only / 2 మరియు 3 మాత్రమే",
     "1 and 3 only / 1 మరియు 3 మాత్రమే",
     "a",
     "Statements 1, 2, 4 correct. Statement 3 wrong — SRC report submitted in 1955 (NOT 1954). SRC was constituted Dec 1953."),

    (4, 2,
     "When and where was the first linguistic state formed in India? [APPSC Group 2]\nతెలుగు: మొదటి భాషా రాష్ట్రం ఏర్పాటు?",
     "Nov 1, 1956 — Andhra Pradesh / 1956 నవంబర్ 1 — AP",
     "Oct 1, 1953 — Andhra State / 1953 అక్టోబర్ 1 — ఆంధ్ర రాష్ట్రం (correct)",
     "Jan 26, 1950 — Karnataka",
     "Aug 15, 1947 — Tamil Nadu",
     "b",
     "October 1, 1953 — Andhra State formed as India's FIRST linguistic state (separated from Madras State). 1956 = AP (merger with Telangana).",
     "APPSC"),

    # ══════════════ SECTION 5 — Goa, Sikkim, Puducherry, Acquired Territories ══════════════

    (5, 1,
     "On which date was Goa liberated?\nతెలుగు: గోవా విముక్తి తేదీ?",
     "August 15, 1947",
     "October 1, 1961",
     "December 19, 1961 / 1961 డిసెంబర్ 19 (correct)",
     "January 26, 1950",
     "c",
     "Goa was liberated on December 19, 1961 (Operation Vijay) by the Indian Army from Portuguese rule — celebrated as Goa Liberation Day."),

    (5, 1,
     "Through which Constitutional Amendment did Sikkim become an Indian state?\nతెలుగు: సిక్కిం భారత రాష్ట్రంగా ఏ సవరణ?",
     "32nd Amendment 1974",
     "35th Amendment 1974",
     "36th Amendment 1975 / 36వ సవరణ 1975 (correct)",
     "37th Amendment 1975",
     "c",
     "36th Constitutional Amendment 1975 made Sikkim the 22nd state of India. Earlier (35th Amendment 1974) Sikkim was an 'Associate State'."),

    (5, 2,
     "When did Puducherry formally merge with India?\nతెలుగు: పుదుచ్చేరి భారత్‌లో ఎప్పుడు?",
     "1947 with Independence / స్వాతంత్ర్యంతో",
     "1954 De facto; 1962 De jure / 1954 De facto; 1962 De jure (correct)",
     "1961 Operation Vijay",
     "1975 — 36th Amendment",
     "b",
     "Puducherry was DE FACTO transferred to India in 1954 (French handed over control). DE JURE (legal) transfer = 1962 by Treaty of Cession ratification."),

    (5, 2,
     "Match the acquired territories with their year of acquisition:\n(P) Goa — (1) 1975\n(Q) Sikkim — (2) 1961\n(R) Puducherry (De jure) — (3) 1962\n(S) Dadra & Nagar Haveli — (4) 1961\nతెలుగు: అర్జిత భూభాగాల జంటలు సరిగ్గా:\n(P) Goa — (1) 1975\n(Q) Sikkim — (2) 1961\n(R) Puducherry (De jure) — (3) 1962\n(S) Dadra & Nagar Haveli — (4) 1961",
     "P-2, Q-1, R-3, S-4 (correct)",
     "P-1, Q-2, R-3, S-4",
     "P-2, Q-3, R-1, S-4",
     "P-4, Q-1, R-2, S-3",
     "a",
     "Goa = 1961 (P-2); Sikkim = 1975 (Q-1); Puducherry De jure = 1962 (R-3); Dadra & Nagar Haveli = 1961 (S-4)."),

    (5, 3,
     "Which state was admitted to India under Article 2?\nతెలుగు: Article 2 కింద ప్రవేశించిన రాష్ట్రం?",
     "Telangana / తెలంగాణ",
     "Andhra Pradesh / ఆంధ్రప్రదేశ్",
     "Sikkim / సిక్కిం (correct)",
     "Goa / గోవా",
     "c",
     "Sikkim was ADMITTED under Article 2 (admission of new states from outside the Union). Telangana, AP = Article 3 (reorganisation of EXISTING states)."),

    (5, 4,
     "Are these pairs all correctly matched?\n(1) Goa Liberation = Dec 19, 1961 (Operation Vijay)\n(2) Sikkim = 36th Amendment 1975 = 22nd state\n(3) Puducherry De jure = 1954\n(4) Dadra & Nagar Haveli = 1961 merger with India\nతెలుగు: కింది జంటలు అన్నీ సరైనవేనా?\n(1) Goa Liberation = 1961 డిసెంబర్ 19\n(2) Sikkim = 36వ సవరణ 1975 = 22వ\n(3) Puducherry De jure = 1954\n(4) Dadra & Nagar Haveli = 1961",
     "1, 2 and 4 only / 1, 2 మరియు 4 మాత్రమే (correct)",
     "All four / అన్నీ",
     "2 and 3 wrong / 2 మరియు 3 తప్పు",
     "1 and 4 only / 1 మరియు 4 మాత్రమే",
     "a",
     "Pair 3 wrong — Puducherry De JURE merger was 1962 (NOT 1954). 1954 was the De FACTO transfer. Pairs 1, 2, 4 correct."),

    # ══════════════ SECTION 6 — J&K Reorganisation 2019 ══════════════

    (6, 1,
     "What major change was made regarding J&K on August 5, 2019?\nతెలుగు: 2019 ఆగస్ట్ 5 లో J&K కి ఏ మార్పు?",
     "Special status of J&K was enhanced / ప్రత్యేక హోదా పెంచారు",
     "Article 370 abrogated; J&K split into 2 UTs / Article 370 రద్దు; J&K రెండు UTs గా (correct)",
     "Given a new constitution / కొత్త రాజ్యాంగం",
     "Handed over to Pakistan / పాకిస్థాన్‌కు",
     "b",
     "On 5 Aug 2019, Article 370 was effectively abrogated and J&K Reorganisation Act 2019 split J&K state into TWO Union Territories: J&K (with Legislature) + Ladakh (without)."),

    (6, 1,
     "Total number of states + UTs in India after 2019 reorganisation?\nతెలుగు: 2019 తర్వాత మొత్తం రాష్ట్రాలు + UTs?",
     "29 states + 7 UTs / 29 + 7",
     "28 states + 8 UTs / 28 + 8 (correct)",
     "30 states + 7 UTs",
     "27 states + 9 UTs",
     "b",
     "After Aug 2019: J&K state removed → 29 minus 1 = 28 states. Two new UTs added (J&K, Ladakh) → 9 UTs. After 2020 (D&NH + D&D merger) → 8 UTs. Total: 28 + 8."),

    (6, 2,
     "Key difference between J&K and Ladakh UTs after 2019?\nతెలుగు: J&K vs Ladakh తేడా?",
     "J&K = UT without Legislature; Ladakh = with Legislature / తారుమారు",
     "J&K = UT with Legislature; Ladakh = without Legislature / J&K = Legislature; Ladakh = లేదు (correct)",
     "Both UT with Legislature / రెండూ Legislature",
     "Both UT without Legislature / రెండూ లేదు",
     "b",
     "J&K = UT WITH Legislature (like Delhi/Puducherry). Ladakh = UT WITHOUT Legislature (centrally administered via Lieutenant Governor)."),

    (6, 2,
     "In 2020, which two UTs merged into one?\nతెలుగు: 2020 లో ఏ రెండు UTs విలీనం?",
     "Goa and Daman & Diu / Goa + Daman & Diu",
     "Chandigarh and Delhi / Chandigarh + Delhi",
     "Dadra & Nagar Haveli and Daman & Diu / Dadra & Nagar Haveli + Daman & Diu (correct)",
     "Puducherry and Lakshadweep",
     "c",
     "January 26, 2020 — Dadra & Nagar Haveli + Daman & Diu merged into ONE UT: 'Dadra and Nagar Haveli and Daman and Diu'. Reduced UTs from 9 to 8."),

    (6, 3,
     "Does Ladakh have a Legislature? What administration?\nతెలుగు: Ladakh లో Legislature ఉందా?",
     "Yes, like J&K / అవును",
     "No Legislature — administered by Lieutenant Governor / లేదు; LG ద్వారా (correct)",
     "Yes, with two Houses / రెండు సభలు",
     "No elections / ఎన్నికలు లేవు",
     "b",
     "Ladakh = UT WITHOUT Legislature. Direct central rule via Lieutenant Governor. Has elected Hill Councils (Leh, Kargil) but NO state-style Legislature."),

    (6, 4,
     "Assertion (A): After the J&K Reorganisation Act 2019, India has 28 states and 8 Union Territories.\nReason (R): J&K was bifurcated into two UTs — J&K (with legislature) and Ladakh (without legislature) — reducing states from 29 to 28.\nతెలుగు: అభికథనం-కారణం సరైనవా?",
     "Both correct, R explains A / రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "Both correct, R doesn't explain / రెండూ సరైనవి, R వివరణ కాదు",
     "A correct, R wrong / A సరైనది, R తప్పు",
     "A wrong, R correct / A తప్పు, R సరైనది",
     "a",
     "Both correct. R explains A — bifurcation of J&K = exactly why states dropped from 29 to 28. (After 2020 D&NH + D&D merger, UTs = 8 too.)"),

    (6, 2,
     "Under J&K Reorganisation Act 2019, what is the status of Jammu & Kashmir? [APPSC Group 2]\nతెలుగు: J&K Reorganisation 2019 ప్రకారం?",
     "Full state with Special Status / పూర్తి రాష్ట్రం",
     "UT with Legislature / శాసనసభతో UT (correct)",
     "UT without Legislature / Legislature లేకుండా UT",
     "Independent territory / స్వతంత్రం",
     "b",
     "J&K = UT with Legislature (similar to Delhi/Puducherry). Ladakh = UT without Legislature.",
     "APPSC"),

    # ══════════════ SECTION 7 — States Today / Telangana / Goa Statehood ══════════════

    (7, 1,
     "How many states does India currently have (as of 2024)?\nతెలుగు: 2024 వరకు భారతదేశంలో మొత్తం రాష్ట్రాలు?",
     "25",
     "27",
     "28 (correct)",
     "29",
     "c",
     "India has 28 STATES + 8 UTs (as of 2024). 28 states since J&K became UT (Aug 2019)."),

    (7, 1,
     "Which UTs have a Legislature?\nతెలుగు: Legislature ఉన్న UTs ఏవి?",
     "Chandigarh and Lakshadweep / Chandigarh + Lakshadweep",
     "Delhi (NCT), Puducherry, J&K / Delhi + Puducherry + J&K (correct)",
     "Andaman & Nicobar and Ladakh / A&N + Ladakh",
     "All UTs / అన్ని UTs",
     "b",
     "Only THREE UTs have a Legislature: Delhi (NCT), Puducherry, and J&K. The other 5 (Chandigarh, A&N, Lakshadweep, Ladakh, D&NH+D&D) are administered by Lieutenant Governor/Administrator."),

    (7, 2,
     "When was Telangana formed as the 29th state?\nతెలుగు: తెలంగాణ ఏర్పాటు తేదీ?",
     "January 1, 2014 / జనవరి 1, 2014",
     "June 2, 2014 / జూన్ 2, 2014 (correct)",
     "October 1, 2014 / అక్టోబర్ 1, 2014",
     "November 1, 2014 / నవంబర్ 1, 2014",
     "b",
     "Telangana = formed on June 2, 2014 — became India's 29th state (now 28 after J&K became UT). Bifurcated from Andhra Pradesh."),

    (7, 2,
     "Match the states with their formation dates:\n(P) Andhra State — (1) Nov 1, 1956\n(Q) Andhra Pradesh — (2) June 2, 2014\n(R) Telangana — (3) Oct 1, 1953\n(S) Goa State — (4) May 30, 1987\nతెలుగు: రాష్ట్రాలు + ఏర్పాటు తేదీలు:\n(P) ఆంధ్ర రాష్ట్రం — (1) Nov 1, 1956\n(Q) AP — (2) June 2, 2014\n(R) Telangana — (3) Oct 1, 1953\n(S) Goa — (4) May 30, 1987",
     "P-3, Q-1, R-2, S-4 (correct)",
     "P-1, Q-3, R-2, S-4",
     "P-3, Q-2, R-1, S-4",
     "P-3, Q-1, R-4, S-2",
     "a",
     "Andhra State = Oct 1, 1953 (P-3); AP = Nov 1, 1956 (Q-1); Telangana = Jun 2, 2014 (R-2); Goa State = May 30, 1987 (S-4)."),

    (7, 3,
     "When did Goa become a state from UT? What number state?\nతెలుగు: Goa ఎప్పుడు రాష్ట్రంగా; ఏ నంబర్?",
     "1961 — 24th state",
     "1975 — 21st state",
     "1987 — 25th state / 1987 — 25వ రాష్ట్రం (correct)",
     "2000 — 26th state",
     "c",
     "Goa = 25th state — granted statehood on May 30, 1987 (separated from Daman & Diu). Goa Liberation = 1961; UT 1961-1987; State since 1987."),

    (7, 4,
     "Which of these pairs are ALL correctly matched?\n(1) 22nd state = Sikkim (1975)\n(2) 25th state = Goa (1987)\n(3) 29th state = Telangana (2014)\n(4) 28th state = Jharkhand (2000)\nతెలుగు: కింది అన్నీ సరైన జంటలు?\n(1) 22వ = సిక్కిం (1975)\n(2) 25వ = గోవా (1987)\n(3) 29వ = తెలంగాణ (2014)\n(4) 28వ = జార్ఖండ్ (2000)",
     "Only 1, 2 and 3 correct / 1, 2 మరియు 3 మాత్రమే",
     "All four / అన్నీ (correct)",
     "Only 2 and 4 wrong / 2 మరియు 4 తప్పు",
     "Only 1 and 3 / 1 మరియు 3 మాత్రమే",
     "b",
     "All four correct: Sikkim (22nd, 1975) + Goa (25th, 1987) + Telangana (29th, 2014) + Jharkhand (28th, 2000). [In 2000, three states formed: Chhattisgarh-26th, Uttarakhand-27th, Jharkhand-28th.]"),

    (7, 2,
     "Which of the following are correctly matched? [UPSC Style]\n(1) Sikkim — 36th Amendment 1975 — 22nd State\n(2) Goa — 25th State — 1987\n(3) Telangana — 28th State — 2014\nతెలుగు: సరైన జంటలు?",
     "1 and 2 only / 1 మరియు 2 మాత్రమే (correct)",
     "2 and 3 only / 2 మరియు 3 మాత్రమే",
     "1 and 3 wrong / 1 మరియు 3 తప్పు",
     "All correct / అన్నీ",
     "a",
     "Pairs 1 and 2 correct. Pair 3 wrong — Telangana was the 29th state (NOT 28th). 28th = Jharkhand (2000).",
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
