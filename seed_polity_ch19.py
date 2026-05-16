# seed_polity_ch19.py
# Chapter 19 — State Legislature
# Total Sections: 8 | Total MCQs: 56 | PYQs: 5
# Sections:
#   0 — Constitution of State Legislature (8 MCQs)
#   1 — Vidhan Sabha — Composition & Duration (8 MCQs)
#   2 — Vidhan Parishad — Composition & Features (7 MCQs)
#   3 — Speaker & Chairman (7 MCQs)
#   4 — Legislative Procedure in States (7 MCQs)
#   5 — Powers & Privileges of State Legislature (7 MCQs)
#   6 — Disqualification & 10th Schedule (6 MCQs)
#   7 — Miscellaneous / Key Articles (6 MCQs)

_CH = 19
_SUBJECT = 'GK'
_TOPIC   = 'Indian_Polity'
_TITLE_TE = 'రాష్ట్ర శాసనమండలి'
_TITLE_EN = 'State Legislature'
_PAGES    = 'Ch.19 (Lakshmikanth)'

_SECTIONS = [
    "రాష్ట్ర శాసనమండలి నిర్మాణం",
    "విధానసభ — కూర్పు & కాలవ్యవధి",
    "విధానపరిషత్ — కూర్పు & లక్షణాలు",
    "స్పీకర్ & చైర్మన్",
    "రాష్ట్రంలో శాసన ప్రక్రియ",
    "రాష్ట్ర శాసనమండలి అధికారాలు & హక్కులు",
    "అనర్హత & 10వ షెడ్యూల్",
    "విభిన్న కీలక అనుచ్ఛేదాలు",
]

_MCQS = [
    # ── Section 0: Constitution of State Legislature ───────────────────────────
    (0, "easy",
     "భారత రాష్ట్రాల శాసనమండలి నిర్మాణాన్ని ప్రస్తావించే అనుచ్ఛేదం ఏది? / Which Article deals with constitution of state legislatures?",
     "అనుచ్ఛేదం 154 / Art.154",
     "అనుచ్ఛేదం 168 / Art.168",
     "అనుచ్ఛేదం 170 / Art.170",
     "అనుచ్ఛేదం 172 / Art.172",
     "b",
     "అనుచ్ఛేదం 168: ప్రతి రాష్ట్రంలో గవర్నర్ + విధానసభ (+ విధానపరిషత్ ఉంటే) అని ప్రస్తావిస్తుంది. / Art.168: Constitution of legislatures in states — Governor + Legislative Assembly (+ Legislative Council where it exists)."),

    (0, "medium",
     "2024 నాటికి ఏ రాష్ట్రాలకు ద్విసభ శాసనమండలి (Vidhan Parishad) ఉంది? / Which states have bicameral legislature (Vidhan Parishad) as of 2024?",
     "మహారాష్ట్ర, UP, బిహార్, AP, తెలంగాణ, కర్ణాటక / Maharashtra, UP, Bihar, AP, Telangana, Karnataka",
     "కేవలం 3 రాష్ట్రాలు / Only 3 states",
     "అన్ని రాష్ట్రాలూ / All states",
     "కేవలం 4 రాష్ట్రాలు / Only 4 states",
     "a",
     "2024 నాటికి 6 రాష్ట్రాలకు విధానపరిషత్ ఉంది: మహారాష్ట్ర, UP, బిహార్, ఆంధ్రప్రదేశ్, తెలంగాణ, కర్ణాటక. / As of 2024: 6 states have Vidhan Parishad — Maharashtra, UP, Bihar, AP, Telangana, Karnataka."),

    (0, "medium",
     "విధానపరిషత్ ఏర్పాటు చేయడానికి / రద్దు చేయడానికి ఏ అనుచ్ఛేదం అనుమతిస్తుంది? / Which Article allows creation/abolition of Legislative Council?",
     "అనుచ్ఛేదం 168 / Art.168",
     "అనుచ్ఛేదం 169 / Art.169",
     "అనుచ్ఛేదం 171 / Art.171",
     "అనుచ్ఛేదం 172 / Art.172",
     "b",
     "అనుచ్ఛేదం 169: విధానసభ తీర్మానం ఆధారంగా పార్లమెంటు విధానపరిషత్‌ను ఏర్పాటు చేయవచ్చు లేదా రద్దు చేయవచ్చు. / Art.169: Parliament can create or abolish LC on resolution passed by LA."),

    (0, "hard",
     "విధానపరిషత్ ఏర్పాటు/రద్దు విధానంలో పార్లమెంటు ఏ మెజారిటీ అవసరం? / What majority does Parliament need to create/abolish Vidhan Parishad?",
     "సాధారణ మెజారిటీ / Simple majority",
     "ప్రత్యేక మెజారిటీ / Special majority",
     "రాజ్యాంగ సవరణ / Constitutional amendment",
     "సాధారణ చట్టం / Simple legislation",
     "a",
     "అనుచ్ఛేదం 169: విధానపరిషత్ ఏర్పాటు/రద్దుకు పార్లమెంటు సాధారణ మెజారిటీతో చట్టం చేయవచ్చు — ఇది రాజ్యాంగ సవరణ కాదు. / Art.169: Parliament passes simple majority law — not a constitutional amendment."),

    (0, "easy",
     "రాష్ట్ర శాసనమండలి సమావేశాలు ఏర్పాటు చేయడానికి బాధ్యత ఎవరిది? / Who is responsible for summoning state legislature sessions?",
     "ముఖ్యమంత్రి / Chief Minister",
     "స్పీకర్ / Speaker",
     "గవర్నర్ / Governor",
     "రాష్ట్రపతి / President",
     "c",
     "అనుచ్ఛేదం 174: గవర్నర్ రాష్ట్ర శాసనమండలి సమావేశాలు ఏర్పాటు చేయడం, వాయిదా వేయడం, రద్దు చేయడం అధికారం. / Art.174: Governor summons, prorogues, dissolves state legislature."),

    (0, "medium",
     "రాష్ట్ర శాసనమండలి రెండు సమావేశాల మధ్య గరిష్ట అంతరం ఎంత? / Maximum gap between two sessions of state legislature?",
     "3 నెలలు / 3 months",
     "4 నెలలు / 4 months",
     "6 నెలలు / 6 months",
     "1 సంవత్సరం / 1 year",
     "c",
     "రాష్ట్ర శాసనమండలి రెండు సమావేశాల మధ్య 6 నెలలకు మించి అంతరం ఉండకూడదు. / Maximum gap between two sessions of state legislature is 6 months."),

    (0, "hard",
     "కోరమ్ లేకుండా రాష్ట్ర శాసనమండలి సమావేశం జరపవచ్చా? / Can state legislature sit without quorum?",
     "అవును / Yes",
     "లేదు / No",
     "స్పీకర్ అనుమతితో / With Speaker's permission",
     "అత్యవసరంలో మాత్రమే / Only in emergency",
     "a",
     "కోరమ్ లేకపోవడాన్ని గమనించడం స్పీకర్/చైర్మన్ బాధ్యత — కానీ కోరమ్ లేకుండా సమావేశం జరగవచ్చు. రాష్ట్ర శాసనమండలి కోరమ్ = 1/10 మొత్తం సభ్యులు. / Quorum = 1/10 of total members; Speaker notices absence but sitting can continue."),

    (0, "medium",
     "రాష్ట్ర శాసనమండలిలో ఓటింగ్‌ను ప్రస్తావించే అనుచ్ఛేదం ఏది? / Which Article deals with voting in state legislature houses?",
     "అనుచ్ఛేదం 187 / Art.187",
     "అనుచ్ఛేదం 189 / Art.189",
     "అనుచ్ఛేదం 191 / Art.191",
     "అనుచ్ఛేదం 194 / Art.194",
     "b",
     "అనుచ్ఛేదం 189: రాష్ట్ర శాసనమండలి సభల్లో ఓటింగ్ — మెజారిటీ ఓట్లతో నిర్ణయం; సమాన ఓట్లైతే స్పీకర్/చైర్మన్ కాస్టింగ్ ఓటు. / Art.189: Questions decided by majority; casting vote of Speaker/Chairman in tie."),

    # ── Section 1: Vidhan Sabha — Composition & Duration ──────────────────────
    (1, "easy",
     "విధానసభలో గరిష్ట సభ్యుల సంఖ్య ఎంత? / Maximum members in Vidhan Sabha?",
     "250",
     "350",
     "500",
     "600",
     "c",
     "అనుచ్ఛేదం 170: విధానసభలో గరిష్టంగా 500, కనిష్టంగా 60 సభ్యులు ఉంటారు. / Art.170: Max 500, Min 60 members in Vidhan Sabha."),

    (1, "easy",
     "విధానసభ కాలవ్యవధి ఎంత? / What is the duration of Vidhan Sabha?",
     "3 సంవత్సరాలు / 3 years",
     "4 సంవత్సరాలు / 4 years",
     "5 సంవత్సరాలు / 5 years",
     "6 సంవత్సరాలు / 6 years",
     "c",
     "అనుచ్ఛేదం 172(1): విధానసభ 5 సంవత్సరాల కాలవ్యవధి పాటు ఉంటుంది (అత్యవసర పరిస్థితిలో పొడిగించవచ్చు). / Art.172(1): Vidhan Sabha has 5-year term (extendable during National Emergency)."),

    (1, "medium",
     "జాతీయ అత్యవసర పరిస్థితిలో విధానసభ కాలవ్యవధిని ఎంతకాలం పొడిగించవచ్చు? / By how much can Vidhan Sabha duration be extended during National Emergency?",
     "6 నెలలు / 6 months",
     "1 సంవత్సరం / 1 year",
     "2 సంవత్సరాలు / 2 years",
     "అత్యవసర పరిస్థితి ముగిసే వరకు / Until Emergency ends",
     "b",
     "అనుచ్ఛేదం 172: జాతీయ అత్యవసర పరిస్థితి ఉన్నప్పుడు పార్లమెంటు విధానసభ కాలవ్యవధిని ఒక్కో సారి 1 సంవత్సరం చొప్పున పొడిగించవచ్చు. / Art.172: During national emergency, Parliament can extend Vidhan Sabha term by 1 year at a time."),

    (1, "medium",
     "విధానసభ సభ్యత్వానికి కనీస వయస్సు ఎంత? / Minimum age for Vidhan Sabha membership?",
     "18 సంవత్సరాలు / 18 years",
     "21 సంవత్సరాలు / 21 years",
     "25 సంవత్సరాలు / 25 years",
     "30 సంవత్సరాలు / 30 years",
     "c",
     "అనుచ్ఛేదం 173: విధానసభ సభ్యత్వానికి కనీస వయస్సు 25 సంవత్సరాలు. / Art.173: Minimum age for Vidhan Sabha membership is 25 years."),

    (1, "hard",
     "విధానసభ సభ్యత్వానికి అర్హత — ఆ రాష్ట్రంలో ఓటరుగా నమోదు కావాలా? / Must a Vidhan Sabha candidate be registered voter in that state?",
     "అవును, అదే నియోజకవర్గంలో / Yes, in the same constituency",
     "అవును, ఆ రాష్ట్రంలో ఎక్కడైనా / Yes, anywhere in that state",
     "లేదు, దేశంలో ఎక్కడైనా / No, anywhere in India",
     "లేదు, ఓటరు కావాల్సిన అవసరం లేదు / No need to be voter",
     "b",
     "విధానసభ సభ్యత్వానికి ఆ రాష్ట్రంలో ఎక్కడైనా ఓటరుగా నమోదై ఉండాలి — అదే నియోజకవర్గంలో అవసరం లేదు. / Must be registered voter anywhere in that state — not necessarily in the same constituency."),

    (1, "easy",
     "విధానసభ అర్హత కోసం వ్యక్తి ఏ సభకు చెందినవాడు అయి ఉండకూడదు? / A Vidhan Sabha candidate must not be a member of?",
     "రాజ్యసభ / Rajya Sabha",
     "రాష్ట్రసభ (దేశంలో ఏ రాష్ట్రానికైనా) / Any state legislature",
     "ఒకేసారి రెండు సభలకు / Two Houses simultaneously",
     "ఏ పార్లమెంటు సభకైనా / Any House of Parliament",
     "c",
     "ఒకేసారి రెండు సభలకు (పార్లమెంటు లేదా రాష్ట్రం) సభ్యుడుగా ఉండలేరు; ఒక సభ ఎన్నికైతే మరో సభ నుండి నిష్క్రమించాలి. / Cannot be member of two houses simultaneously; must vacate one if elected to another."),

    (1, "medium",
     "గోవా విధానసభలో సభ్యుల సంఖ్య ఎంత? (రాజ్యాంగం నిర్ణయించిన కనిష్ట సంఖ్య అపవాదు) / Goa Vidhan Sabha has how many members? (below constitutional minimum exception)",
     "32",
     "40",
     "45",
     "60",
     "b",
     "గోవా విధానసభకు 40 సభ్యులు ఉంటారు — రాజ్యాంగ కనిష్ట సంఖ్య 60 కానీ చిన్న రాష్ట్రాలకు మినహాయింపు ఉంది. / Goa has 40 seats — exception to the constitutional minimum of 60 for small states."),

    (1, "hard",
     "విధానసభ సభ్యత్వానికి అనర్హత నిర్ణయించే అధికారం ఎవరికి ఉంది? / Who decides disqualification of Vidhan Sabha members?",
     "స్పీకర్ / Speaker",
     "హైకోర్టు / High Court",
     "గవర్నర్ (ఎన్నికల కమిషన్ అభిప్రాయంతో) / Governor (on EC's opinion)",
     "సుప్రీం కోర్ట్ / Supreme Court",
     "c",
     "అనుచ్ఛేదం 192: అనర్హత ప్రశ్న గవర్నర్‌కు నివేదించబడుతుంది; గవర్నర్ ఎన్నికల కమిషన్ అభిప్రాయం మేరకు నిర్ణయిస్తారు. / Art.192: Disqualification question referred to Governor; decides on EC's opinion."),

    # ── Section 2: Vidhan Parishad — Composition & Features ────────────────────
    (2, "easy",
     "విధానపరిషత్ కాలవ్యవధి ఎంత? / What is the duration of Vidhan Parishad?",
     "5 సంవత్సరాలు / 5 years",
     "6 సంవత్సరాలు / 6 years",
     "శాశ్వత సంస్థ / Permanent body",
     "విధానసభ కాలవ్యవధి వరకు / Co-terminus with Vidhan Sabha",
     "c",
     "విధానపరిషత్ శాశ్వత సంస్థ — రద్దు చేయలేరు. 1/3 సభ్యులు ప్రతి 2 సంవత్సరాలకు పదవీ విరమణ చేస్తారు. / Vidhan Parishad is a permanent body — cannot be dissolved. 1/3 retire every 2 years."),

    (2, "medium",
     "విధానపరిషత్ సభ్యుల కనీస వయస్సు ఎంత? / Minimum age for Vidhan Parishad membership?",
     "21 సంవత్సరాలు / 21 years",
     "25 సంవత్సరాలు / 25 years",
     "30 సంవత్సరాలు / 30 years",
     "35 సంవత్సరాలు / 35 years",
     "c",
     "అనుచ్ఛేదం 173: విధానపరిషత్ సభ్యత్వానికి కనీస వయస్సు 30 సంవత్సరాలు. / Art.173: Minimum age for Legislative Council membership is 30 years."),

    (2, "hard",
     "విధానపరిషత్ కూర్పులో గవర్నర్ నామినేట్ చేసే వారి శాతం ఎంత? / What fraction does Governor nominate to Vidhan Parishad?",
     "1/12",
     "1/6",
     "1/3",
     "1/4",
     "b",
     "అనుచ్ఛేదం 171(5): గవర్నర్ విధానపరిషత్ మొత్తం సభ్యుల 1/6 వంతు — కళలు, సాహిత్యం, విజ్ఞానం, సమాజసేవ నిపుణులను నామినేట్ చేస్తారు. / Art.171(5): Governor nominates 1/6th — persons of expertise in arts, literature, science, social service."),

    (2, "medium",
     "విధానపరిషత్ మొత్తం సభ్యులలో విధానసభ ఎన్నుకునే వారి వాటా ఎంత? / Share elected by Vidhan Sabha in Vidhan Parishad?",
     "1/12",
     "1/6",
     "1/3",
     "1/4",
     "c",
     "విధానపరిషత్ కూర్పు: 1/3 — విధానసభ ఎన్నుకుంటుంది; 1/3 — స్థానిక సంస్థలు; 1/12 — పట్టభద్రులు; 1/12 — ఉపాధ్యాయులు; 1/6 — గవర్నర్ నామినేషన్. / VP composition: 1/3 by LA; 1/3 local bodies; 1/12 graduates; 1/12 teachers; 1/6 by Governor."),

    (2, "medium",
     "విధానపరిషత్ గరిష్ట సభ్యుల సంఖ్య ఎంత? / Maximum members in Vidhan Parishad?",
     "విధానసభ సంఖ్యకు 1/2 / 1/2 of Vidhan Sabha",
     "విధానసభ సంఖ్యకు 1/3 లేదా 40 (ఏది ఎక్కువైతే) / 1/3 of Vidhan Sabha or 40 (whichever greater)",
     "250",
     "100",
     "b",
     "అనుచ్ఛేదం 171(1): విధానపరిషత్ సభ్యుల సంఖ్య విధానసభ మొత్తం సంఖ్యకు 1/3 కంటే ఎక్కువ కాకూడదు; కానీ 40 కంటే తక్కువ కాకూడదు. / Art.171(1): Not more than 1/3 of Vidhan Sabha or less than 40 members."),

    (2, "easy",
     "విధానపరిషత్ సభ్యుల పదవీ కాలం ఎంత? / Term of Vidhan Parishad members?",
     "3 సంవత్సరాలు / 3 years",
     "4 సంవత్సరాలు / 4 years",
     "5 సంవత్సరాలు / 5 years",
     "6 సంవత్సరాలు / 6 years",
     "d",
     "విధానపరిషత్ సభ్యుల పదవీ కాలం 6 సంవత్సరాలు — రాజ్యసభ వలె. 1/3 సభ్యులు ప్రతి 2 సంవత్సరాలకు విరమిస్తారు. / VP members serve 6-year term — like Rajya Sabha. 1/3 retire every 2 years."),

    (2, "hard",
     "విధానపరిషత్ లేని రాష్ట్రంలో లెజిస్లేటివ్ కౌన్సిల్ ఏర్పాటు చేయడానికి పార్లమెంటు ముందు ఏ పూర్వ అవసరం ఉంది? / Pre-requisite for Parliament to create Vidhan Parishad in a state?",
     "రాష్ట్రపతి ఆమోదం / President's approval",
     "విధానసభ ప్రత్యేక మెజారిటీ తీర్మానం / Special majority resolution by Vidhan Sabha",
     "విధానసభ సాధారణ మెజారిటీ తీర్మానం / Simple majority resolution by Vidhan Sabha",
     "గవర్నర్ సిఫారసు / Governor's recommendation",
     "c",
     "అనుచ్ఛేదం 169: విధానసభ మొత్తం సభ్యుల మెజారిటీ మరియు హాజరైన-ఓటు వేసిన సభ్యుల 2/3 తీర్మానం తర్వాతే పార్లమెంటు చట్టం చేయగలదు. / Art.169: Vidhan Sabha resolution by total majority + 2/3 of members present & voting required."),

    (2, "medium",
     "విధానపరిషత్ (Vidhan Parishad) సభ్యత్వ కాలవ్యవధి ఎంత? / What is the tenure of Vidhan Parishad members?",
     "5 సంవత్సరాలు / 5 years",
     "6 సంవత్సరాలు / 6 years",
     "గవర్నర్ నిర్ణయం / Governor decides",
     "కాలవ్యవధి లేదు / No fixed tenure",
     "b",
     "విధానపరిషత్ శాశ్వత సంస్థ; ప్రతి 2 సంవత్సరాలకు 1/3 సభ్యులు పదవీ విరమణ చేస్తారు; ప్రతి సభ్యుడి పదవీకాలం 6 సంవత్సరాలు. రాజ్యసభ నమూనాలో రూపొందించబడింది. / Vidhan Parishad is permanent; 1/3 retire every 2 years; each member serves 6 years. Modelled on Rajya Sabha."),

    # ── Section 3: Speaker & Chairman ──────────────────────────────────────────
    (3, "easy",
     "విధానసభ స్పీకర్‌ను ఎవరు ఎన్నుకుంటారు? / Who elects the Speaker of Vidhan Sabha?",
     "గవర్నర్ / Governor",
     "ముఖ్యమంత్రి / Chief Minister",
     "విధానసభ సభ్యులు / Members of Vidhan Sabha",
     "రాష్ట్రపతి / President",
     "c",
     "అనుచ్ఛేదం 178: విధానసభ స్పీకర్ మరియు డిప్యూటీ స్పీకర్‌లను సభ్యులే ఎన్నుకుంటారు. / Art.178: Speaker and Deputy Speaker of Vidhan Sabha are elected by members of the House."),

    (3, "medium",
     "విధానసభ స్పీకర్ తన రాజీనామాను ఎవరికి ఇవ్వాలి? / Speaker of Vidhan Sabha submits resignation to whom?",
     "గవర్నర్ / Governor",
     "ముఖ్యమంత్రి / Chief Minister",
     "డిప్యూటీ స్పీకర్ / Deputy Speaker",
     "హైకోర్టు CJ / HC CJ",
     "c",
     "అనుచ్ఛేదం 179: విధానసభ స్పీకర్ రాజీనామాను డిప్యూటీ స్పీకర్‌కు ఇవ్వాలి; డిప్యూటీ స్పీకర్ స్పీకర్‌కు ఇవ్వాలి. / Art.179: Speaker resigns to Deputy Speaker; Deputy Speaker resigns to Speaker."),

    (3, "medium",
     "విధానపరిషత్ చైర్మన్‌ను ఎవరు ఎన్నుకుంటారు? / Who elects Chairman of Vidhan Parishad?",
     "గవర్నర్ / Governor",
     "విధానపరిషత్ సభ్యులు / Members of Vidhan Parishad",
     "విధానసభ సభ్యులు / Members of Vidhan Sabha",
     "ఉభయ సభల సభ్యులు / Members of both Houses",
     "b",
     "అనుచ్ఛేదం 182: విధానపరిషత్ చైర్మన్ మరియు డిప్యూటీ చైర్మన్‌లను పరిషత్ సభ్యులే ఎన్నుకుంటారు. / Art.182: Chairman and Deputy Chairman of VP are elected by members of VP."),

    (3, "easy",
     "విధానసభ స్పీకర్‌ను తొలగించే తీర్మానం చర్చలో ఉండగా స్పీకర్ పాత్ర ఏమిటి? / What is Speaker's role when removal resolution is under consideration?",
     "అధ్యక్షత వహిస్తారు / Presides",
     "ఓటు వేయవచ్చు కానీ అధ్యక్షత వహించలేరు / Can vote but not preside",
     "అధ్యక్షత వహించలేరు కానీ సభలో ఉండవచ్చు / Cannot preside but may be present",
     "వెంటనే రాజీనామా ఇవ్వాలి / Must resign immediately",
     "b",
     "అనుచ్ఛేదం 181: తన తొలగింపు తీర్మానం పెండింగ్‌లో ఉన్నప్పుడు స్పీకర్ అధ్యక్షత వహించలేరు — కానీ ఆ తీర్మానంపై ఓటు వేయవచ్చు (ఇది లోక్‌సభ నుండి భిన్నం). / Art.181: Speaker cannot preside during resolution for own removal — but can vote (unlike LS Speaker)."),

    (3, "hard",
     "విధానసభ స్పీకర్‌ను తొలగించే తీర్మానానికి ముందు ఎంత నోటీసు అవసరం? / How many days' notice is required before moving removal resolution of Speaker?",
     "7 రోజులు / 7 days",
     "10 రోజులు / 10 days",
     "14 రోజులు / 14 days",
     "30 రోజులు / 30 days",
     "c",
     "విధానసభ స్పీకర్ తొలగింపు తీర్మానానికి 14 రోజుల ముందస్తు నోటీసు అవసరం (లోక్‌సభ వలె). / 14 days' notice required before a resolution to remove the Speaker (same as LS)."),

    (3, "medium",
     "ఒక రాష్ట్రంలో విధానసభ రద్దు అయినా స్పీకర్ ఎంత కాలం పదవిలో ఉంటారు? / How long does Speaker continue after Vidhan Sabha is dissolved?",
     "వెంటనే పదవి కోల్పోతారు / Immediately loses office",
     "6 నెలలు / 6 months",
     "కొత్త విధానసభ సమావేశమయ్యే వరకు / Until new Vidhan Sabha meets",
     "పదవీ కాలం ముగిసే వరకు / Until term expires",
     "c",
     "విధానసభ రద్దు అయినా స్పీకర్ కొత్త విధానసభ మొదటి సమావేశం వరకు పదవిలో ఉంటారు. / Speaker continues until new Vidhan Sabha holds its first sitting after dissolution."),

    (3, "easy",
     "విధానపరిషత్ చైర్మన్ పాత్ర ఏ జాతీయ స్థాయి అధికారిని పోలి ఉంటుంది? / Chairman of Vidhan Parishad resembles which national officer?",
     "లోక్‌సభ స్పీకర్ / Lok Sabha Speaker",
     "రాజ్యసభ చైర్మన్ (ఉప రాష్ట్రపతి) / Rajya Sabha Chairman (VP)",
     "రాష్ట్రపతి / President",
     "CJI",
     "b",
     "విధానపరిషత్ చైర్మన్ పాత్ర రాజ్యసభ చైర్మన్ (ఉప రాష్ట్రపతి) వలె ఉంటుంది — రెండూ ఎగువ సభల అధ్యక్షులు. / VP's Chairman resembles RS Chairman (Vice-President) — both preside over upper houses."),

    (3, "medium",
     "విధానసభ స్పీకర్‌ని తొలగించడానికి ఏ తీర్మానం అవసరం? / What resolution is needed to remove the Vidhan Sabha Speaker?",
     "మెజారిటీ తీర్మానం / Simple majority resolution",
     "2/3 ప్రత్యేక మెజారిటీ / Two-thirds special majority",
     "విధానసభ మొత్తం సభ్యుల ప్రభావ మెజారిటీ — 14 రోజుల ముందస్తు నోటీసుతో / Effective majority of total members — with 14 days' notice",
     "గవర్నర్ ఆమోదం అవసరం / Needs Governor's approval",
     "c",
     "అనుచ్ఛేదం 179: స్పీకర్ తొలగింపుకు విధానసభ మొత్తం సభ్యుల ప్రభావ మెజారిటీ తీర్మానం కావాలి — 14 రోజుల ముందస్తు నోటీసు అవసరం. సాధారణ మెజారిటీ సరిపోదు. / Art.179: Speaker removal requires effective majority (majority of all members) — with 14 days' advance notice. LS Speaker same procedure."),

    # ── Section 4: Legislative Procedure in States ─────────────────────────────
    (4, "easy",
     "రాష్ట్ర మనీ బిల్లు ఏ సభలో మాత్రమే ప్రవేశపెట్టవచ్చు? / State Money Bill can be introduced only in which House?",
     "విధానపరిషత్ / Vidhan Parishad",
     "విధానసభ / Vidhan Sabha",
     "రెండు సభల్లో / Either House",
     "గవర్నర్ ఆమోదంతో ఏ సభలోనైనా / Either House with Governor's approval",
     "b",
     "అనుచ్ఛేదం 198: రాష్ట్ర మనీ బిల్లు విధానసభలో మాత్రమే ప్రవేశపెట్టవచ్చు. / Art.198: State Money Bill can be introduced only in Vidhan Sabha."),

    (4, "medium",
     "రాష్ట్ర మనీ బిల్లు విధానసభ ఆమోదించిన తర్వాత విధానపరిషత్‌కు పంపితే పరిషత్ ఏమి చేయగలదు? / What can Vidhan Parishad do with a Money Bill sent by Vidhan Sabha?",
     "సవరణలు చేయవచ్చు / Can amend",
     "తిరస్కరించవచ్చు / Can reject",
     "14 రోజుల్లో తిరిగి పంపాలి; సిఫారసులు మాత్రమే / Return within 14 days; only recommendations",
     "6 నెలలు నిలిపివేయవచ్చు / Can withhold for 6 months",
     "c",
     "అనుచ్ఛేదం 198: విధానపరిషత్ మనీ బిల్లును 14 రోజుల్లో తిరిగి పంపాలి; కేవలం సిఫారసులు మాత్రమే చేయగలదు; విధానసభ వాటిని పట్టించుకోవాల్సిన అవసరం లేదు. / Art.198: VP must return within 14 days with recommendations only; Vidhan Sabha need not accept them."),

    (4, "medium",
     "విధానసభ ఆమోదించిన సాధారణ బిల్లు విధానపరిషత్ తిరస్కరిస్తే ఏమవుతుంది? / What happens if Vidhan Parishad rejects a Bill passed by Vidhan Sabha?",
     "బిల్లు రద్దవుతుంది / Bill lapses",
     "జాయింట్ సెషన్ పిలుస్తారు / Joint session called",
     "విధానసభ 3 నెలల తర్వాత మళ్ళీ పాస్ చేస్తే గవర్నర్‌కు పంపవచ్చు / After 3 months if VA passes again, can send to Governor",
     "గవర్నర్ ఆమోదం సరిపోతుంది / Governor's assent suffices",
     "c",
     "అనుచ్ఛేదం 197: విధానపరిషత్ బిల్లు తిరస్కరించినా, 3 నెలలు నిలిపినా, లేదా సవరణలు విధానసభ అంగీకరించకుండా పంపినా — విధానసభ మళ్ళీ ఆమోదిస్తే గవర్నర్‌కు పంపవచ్చు. / Art.197: Vidhan Sabha can override VP by passing bill again after 3 months."),

    (4, "hard",
     "రాష్ట్ర శాసనమండలిలో జాయింట్ సెషన్ అవకాశం ఉందా? / Is there a provision for joint sitting in state legislature?",
     "అవును, లోక్‌సభ వలె / Yes, like Lok Sabha",
     "లేదు / No",
     "కేవలం రాష్ట్రపతి ఆమోదంతో / Only with Presidential approval",
     "కేవలం ఆర్థిక బిల్లులకు / Only for financial bills",
     "b",
     "రాష్ట్ర శాసనమండలిలో జాయింట్ సెషన్ అవకాశం లేదు — అనుచ్ఛేదం 108 కేవలం పార్లమెంటుకు మాత్రమే వర్తిస్తుంది. / No joint sitting provision for state legislature — Art.108 applies only to Parliament."),

    (4, "easy",
     "రాష్ట్ర మనీ బిల్లు అని ఎవరు ధృవీకరిస్తారు? / Who certifies a bill as State Money Bill?",
     "గవర్నర్ / Governor",
     "విధానసభ స్పీకర్ / Speaker of Vidhan Sabha",
     "ముఖ్యమంత్రి / Chief Minister",
     "రాష్ట్రపతి / President",
     "b",
     "అనుచ్ఛేదం 199: విధానసభ స్పీకర్ బిల్లును మనీ బిల్లుగా ధృవీకరిస్తారు. / Art.199: Speaker of Vidhan Sabha certifies a bill as Money Bill."),

    (4, "medium",
     "రాష్ట్ర శాసనసభ 'అవిశ్వాస తీర్మానం' (No-confidence motion) ఏ సభలో పెట్టవచ్చు? / No-confidence motion against CM can be moved in which house?",
     "విధానపరిషత్ / Vidhan Parishad",
     "విధానసభ మాత్రమే / Only Vidhan Sabha",
     "రెండు సభల్లోనూ / Both Houses",
     "గవర్నర్ నిర్ణయిస్తారు / Governor decides",
     "b",
     "అవిశ్వాస తీర్మానం విధానసభలో మాత్రమే పెట్టవచ్చు — రాష్ట్ర మంత్రిమండలి విధానసభకు మాత్రమే జవాబుదారీ. / No-confidence only in Vidhan Sabha — state CoM responsible only to Vidhan Sabha."),

    (4, "hard",
     "విధానసభ ఆమోదించిన మనీ బిల్లుకు గవర్నర్ ఆమోదం నిలిపివేయవచ్చా? / Can Governor withhold assent to Money Bill passed by Vidhan Sabha?",
     "అవును / Yes",
     "లేదు / No",
     "రాష్ట్రపతి అనుమతితో / With President's permission",
     "రాష్ట్రపతికి నివేదించవచ్చు / Can reserve for President",
     "d",
     "అనుచ్ఛేదం 200: గవర్నర్ మనీ బిల్లును తిరిగి పంపలేరు; ఆమోదించాలి లేదా రాష్ట్రపతి పరిశీలనకు నివేదించవచ్చు. / Art.200: Governor cannot return Money Bill — must assent or reserve for President."),

    (4, "medium",
     "విధానపరిషత్ ఉన్న రాష్ట్రంలో సాధారణ బిల్లు గురించి విధానపరిషత్ 3 నెలలు ఆలస్యం చేస్తే ఏమవుతుంది? / If Vidhan Parishad delays ordinary Bill for 3 months, what happens?",
     "బిల్లు రద్దవుతుంది / Bill lapses",
     "విధానసభ రెండవ సారి ఆమోదిస్తే బిల్లు ఆమోదించినట్లు / If Vidhan Sabha passes it again, Bill is deemed passed",
     "గవర్నర్ మధ్యవర్తిత్వం చేస్తారు / Governor mediates",
     "సంయుక్త సమావేశం ఏర్పాటవుతుంది / Joint session is held",
     "b",
     "Art.197(1): విధానసభ ఆమోదించిన బిల్లును విధానపరిషత్ తిరస్కరించినా / 3 నెలలు నిలిపివేసినా / సవరణలతో ఆమోదించినా — విధానసభ మళ్ళీ ఆమోదిస్తే (అదే సవరణలతో లేదా లేకుండా) ఆమోదించినట్లు. / Art.197(1): If Vidhan Parishad rejects/delays (3 months)/passes with amendments — Vidhan Sabha can pass again; deemed to have passed both Houses."),

    # ── Section 5: Powers & Privileges of State Legislature ────────────────────
    (5, "easy",
     "రాష్ట్ర శాసనమండలి సభ్యుల అధికారాలు & హక్కులు ఏ అనుచ్ఛేదంలో ఉన్నాయి? / State legislature powers and privileges are in which Article?",
     "అనుచ్ఛేదం 191 / Art.191",
     "అనుచ్ఛేదం 194 / Art.194",
     "అనుచ్ఛేదం 197 / Art.197",
     "అనుచ్ఛేదం 200 / Art.200",
     "b",
     "అనుచ్ఛేదం 194: రాష్ట్ర శాసనమండలి సభలు, వాటి సభ్యులు, కమిటీల అధికారాలు, హక్కులు మరియు మినహాయింపులు. / Art.194: Powers, privileges and immunities of state legislature houses, members and committees."),

    (5, "medium",
     "రాష్ట్ర శాసనమండలి కార్యవిధానపై న్యాయస్థానాలు పరిశీలించగలవా? / Can courts inquire into proceedings of state legislature?",
     "అవును / Yes",
     "లేదు / No",
     "హైకోర్టు మాత్రమే / HC only",
     "సుప్రీం కోర్టు మాత్రమే / SC only",
     "b",
     "అనుచ్ఛేదం 212: కోర్టులు రాష్ట్ర శాసనమండలి కార్యవిధానాన్ని పరిశీలించే అధికారం లేదు. / Art.212: Courts cannot inquire into proceedings of state legislature."),

    (5, "medium",
     "రాష్ట్ర శాసనమండలి సభ్యుల జీతాలు, భత్యాలు ఏ అనుచ్ఛేదంలో ప్రస్తావించబడ్డాయి? / Salaries and allowances of state legislature members are in which Article?",
     "అనుచ్ఛేదం 193 / Art.193",
     "అనుచ్ఛేదం 195 / Art.195",
     "అనుచ్ఛేదం 196 / Art.196",
     "అనుచ్ఛేదం 194 / Art.194",
     "b",
     "అనుచ్ఛేదం 195: రాష్ట్ర శాసనమండలి సభ్యులు రాష్ట్ర శాసనమండలి నిర్ణయించే జీతాలు, భత్యాలు పొందుతారు. / Art.195: Members of state legislature receive salaries and allowances as state legislature determines."),

    (5, "hard",
     "రాష్ట్ర శాసనమండలి సభ్యుడు ప్రమాణం చేయకుండా కూర్చుని ఓటు వేస్తే శిక్ష ఏమిటి? / Penalty for sitting/voting without oath in state legislature?",
     "సభ్యత్వం రద్దు / Membership cancelled",
     "రూ.500 జరిమానా / Rs.500 fine",
     "రూ.500 జరిమానా ప్రతి రోజుకు / Rs.500 fine per day",
     "6 నెలల జైలు / 6 months imprisonment",
     "c",
     "అనుచ్ఛేదం 193: ప్రమాణం చేయకుండా కూర్చుని ఓటు వేస్తే రోజుకు రూ.500 జరిమానా. / Art.193: Penalty for sitting and voting before oath — Rs.500 per day."),

    (5, "easy",
     "రాష్ట్ర శాసనమండలి అదివేష పరిమితులు (కార్యవిధాన నిరోధం) ఏ అనుచ్ఛేదంలో ఉన్నాయి? / Which Article prohibits state legislature discussion on sub-judice matters?",
     "అనుచ్ఛేదం 208 / Art.208",
     "అనుచ్ఛేదం 211 / Art.211",
     "అనుచ్ఛేదం 212 / Art.212",
     "అనుచ్ఛేదం 213 / Art.213",
     "b",
     "అనుచ్ఛేదం 211: న్యాయమూర్తుల ప్రవర్తనపై, న్యాయస్థానాల పరిశీలనలో ఉన్న విషయాలపై చర్చించడాన్ని నిషేధిస్తుంది. / Art.211: Prohibits discussion on conduct of judges and sub-judice matters."),

    (5, "medium",
     "రాష్ట్ర శాసనమండలి వార్షిక ఆర్థిక నివేదిక (State Budget) ఏ సభలో సమర్పించబడుతుంది? / State Annual Financial Statement is laid in which House?",
     "విధానపరిషత్ / Vidhan Parishad",
     "విధానసభ / Vidhan Sabha",
     "రెండు సభల్లోనూ ఒకేసారి / Both Houses simultaneously",
     "ఏ సభలోనైనా / Either House",
     "b",
     "అనుచ్ఛేదం 202: రాష్ట్ర వార్షిక ఆర్థిక నివేదిక విధానసభలో సమర్పించబడుతుంది. / Art.202: Annual Financial Statement (Budget) of state is laid before Vidhan Sabha."),

    (5, "hard",
     "రాష్ట్ర శాసనమండలి సభ్యులు 'ఉపన్యాస స్వేచ్ఛ' కింద ఏ కోర్టులోనూ విచారించబడరు — ఈ హక్కు ఏ అనుచ్ఛేదంలో? / Members' speech freedom in state legislature — cannot be questioned in court — which Article?",
     "అనుచ్ఛేదం 191 / Art.191",
     "అనుచ్ఛేదం 193 / Art.193",
     "అనుచ్ఛేదం 194(2) / Art.194(2)",
     "అనుచ్ఛేదం 212 / Art.212",
     "c",
     "అనుచ్ఛేదం 194(2): రాష్ట్ర శాసనమండలిలో సభ్యుడు చేసిన ఉపన్యాసాలు లేదా ఓటుపై ఏ కోర్టులోనూ విచారించరాదు. / Art.194(2): No proceedings of member in state legislature shall be questioned in any court."),

    (5, "medium",
     "రాష్ట్ర శాసనమండలి సభ్యుల జీతభత్యాలు ఎవరు నిర్ణయిస్తారు? / Who determines salaries and allowances of state legislature members?",
     "గవర్నర్ / Governor",
     "ముఖ్యమంత్రి / Chief Minister",
     "రాష్ట్ర శాసనమండలి చట్టం ద్వారా / State legislature by law",
     "కేంద్ర ఆర్థిక మంత్రిత్వ శాఖ / Union Finance Ministry",
     "c",
     "అనుచ్ఛేదం 195: రాష్ట్ర శాసనమండలి సభ్యుల జీతాలు, భత్యాలు రాష్ట్ర శాసనమండలి చట్టం ద్వారా నిర్ణయించబడతాయి — మరియు అటువంటి చట్టం చేయబడే వరకు రాష్ట్రపతి నిర్దేశించే విధంగా ఉంటాయి. / Art.195: Salaries/allowances of state legislature members = as fixed by state legislature by law; until then as President determines."),

    # ── Section 6: Disqualification & 10th Schedule ─────────────────────────────
    (6, "easy",
     "రాష్ట్ర శాసనమండలి సభ్యుల పార్టీ ఫిరాయింపు వ్యతిరేక నిబంధనలు ఏ షెడ్యూల్‌లో ఉన్నాయి? / Anti-defection provisions for state legislature members are in which Schedule?",
     "8వ షెడ్యూల్ / 8th Schedule",
     "9వ షెడ్యూల్ / 9th Schedule",
     "10వ షెడ్యూల్ / 10th Schedule",
     "11వ షెడ్యూల్ / 11th Schedule",
     "c",
     "10వ షెడ్యూల్ (52వ సవరణ 1985): పార్టీ ఫిరాయింపు వ్యతిరేక చట్టం — పార్లమెంటు మరియు రాష్ట్ర శాసనమండలులకు వర్తిస్తుంది. / 10th Schedule (52nd Amendment 1985): Anti-defection — applies to Parliament and state legislatures."),

    (6, "medium",
     "10వ షెడ్యూల్ కింద అనర్హత నిర్ణయించే అధికారం ఎవరికి ఉంది? / Who decides disqualification under 10th Schedule?",
     "హైకోర్టు / High Court",
     "సుప్రీం కోర్టు / Supreme Court",
     "సభాపతి (స్పీకర్/చైర్మన్) / Presiding Officer (Speaker/Chairman)",
     "ఎన్నికల కమిషన్ / Election Commission",
     "c",
     "10వ షెడ్యూల్: పార్టీ ఫిరాయింపు అనర్హత నిర్ణయం స్పీకర్/చైర్మన్ అధికారం. అయితే కిహోతో హొల్లోహన్ కేసు (1992) ప్రకారం న్యాయ సమీక్షకు అర్హమే. / 10th Schedule: Speaker/Chairman decides defection disqualification; but SC review permitted per Kihoto case 1992."),

    (6, "hard",
     "10వ షెడ్యూల్ కింద విలీనానికి (Merger) అనుమతించే సభ్యుల కనిష్ట శాతం ఎంత? / Minimum % of members required for 'Merger' under 10th Schedule?",
     "50%",
     "2/3",
     "3/4",
     "4/5",
     "b",
     "10వ షెడ్యూల్: పార్టీ మూల శాసనసభా పక్షంలో 2/3 సభ్యులు విలీనానికి అంగీకరిస్తే అది అనర్హత నుండి మినహాయింపు. / 10th Schedule: Merger valid if 2/3 of original legislature party agrees — exempt from disqualification."),

    (6, "medium",
     "శాసనసభ సభ్యుడు 'లాభదాయక పదవి' (office of profit) పొందితే అనర్హుడవుతారు — ఏ అనుచ్ఛేదం? / MLA becomes disqualified for holding 'office of profit' — which Article?",
     "అనుచ్ఛేదం 191(1)(a) / Art.191(1)(a)",
     "అనుచ్ఛేదం 192 / Art.192",
     "అనుచ్ఛేదం 193 / Art.193",
     "10వ షెడ్యూల్ / 10th Schedule",
     "a",
     "అనుచ్ఛేదం 191(1)(a): కేంద్ర లేదా రాష్ట్ర ప్రభుత్వం కింద లాభదాయక పదవి పొందిన వ్యక్తి విధానసభ/పరిషత్ సభ్యత్వానికి అనర్హుడు. / Art.191(1)(a): Disqualification if holding office of profit under Union or State government."),

    (6, "easy",
     "శాసనసభ సభ్యుడు మానసికంగా అస్వస్థుడని ప్రకటించబడితే అనర్హుడవుతాడు — ఏ అనుచ్ఛేదం? / MLA declared of unsound mind is disqualified — which Article?",
     "అనుచ్ఛేదం 191(1)(b) / Art.191(1)(b)",
     "అనుచ్ఛేదం 191(1)(c) / Art.191(1)(c)",
     "అనుచ్ఛేదం 192 / Art.192",
     "అనుచ్ఛేదం 194 / Art.194",
     "a",
     "అనుచ్ఛేదం 191(1)(b): సక్షమ న్యాయస్థానం మానసిక అస్వస్థతగా ప్రకటించిన వ్యక్తి అనర్హుడు. / Art.191(1)(b): Person declared of unsound mind by competent court is disqualified."),

    (6, "hard",
     "10వ షెడ్యూల్ చేర్చబడిన రాజ్యాంగ సవరణ ఏది? / Which Constitutional Amendment added the 10th Schedule?",
     "44వ సవరణ / 44th Amendment",
     "52వ సవరణ / 52nd Amendment",
     "73వ సవరణ / 73rd Amendment",
     "91వ సవరణ / 91st Amendment",
     "b",
     "52వ రాజ్యాంగ సవరణ 1985: పార్టీ ఫిరాయింపు వ్యతిరేక చట్టం రూపకల్పన — 10వ షెడ్యూల్ రాజ్యాంగంలో చేర్చబడింది. / 52nd Constitutional Amendment 1985: Added the anti-defection 10th Schedule."),

    (6, "medium",
     "రాష్ట్ర శాసనమండలి సభ్యుడు స్వచ్ఛంద రాజీనామా లేదా విప్ ఉల్లంఘిస్తే — అనర్హత నిర్ణయం ఎవరు తీసుకుంటారు? / If state legislature member voluntarily gives up membership or votes against party whip — who decides disqualification?",
     "స్పీకర్ లేదా చైర్మన్ / Speaker or Chairman",
     "హైకోర్టు / High Court",
     "గవర్నర్ / Governor",
     "ఎన్నికల కమిషన్ / Election Commission",
     "a",
     "10వ షెడ్యూల్ పారా 6: పార్టీ ఫిరాయింపు అనర్హత — స్పీకర్ (విధానసభకు) లేదా చైర్మన్ (విధానపరిషత్‌కు) నిర్ణయిస్తారు. / 10th Schedule Para 6: Disqualification on defection decided by Speaker (Vidhan Sabha) or Chairman (Vidhan Parishad)."),

    (6, "hard",
     "విధానసభ సభ్యుడు 'నిర్దల' (independent) అభ్యర్థిగా గెలిస్తే పార్టీలో చేరవచ్చా? / If a Vidhan Sabha member wins as independent and then joins a party?",
     "6 నెలలలో చేరవచ్చు / Can join within 6 months",
     "అనర్హత వర్తిస్తుంది — నిర్దల అభ్యర్థి ఏ పార్టీలోనూ చేరలేరు / Disqualified — independent cannot join any party",
     "ఎప్పుడైనా చేరవచ్చు / Can join anytime",
     "స్పీకర్ అనుమతితో చేరవచ్చు / Can join with Speaker's permission",
     "b",
     "10వ షెడ్యూల్ పారా 2(2): నిర్దల అభ్యర్థిగా ఎన్నికైన తర్వాత ఏదైనా రాజకీయ పార్టీలో చేరినట్లయితే అనర్హత వర్తిస్తుంది. ఎన్నికైన తర్వాత ఎప్పుడూ పార్టీలో చేరలేరు. / 10th Schedule Para 2(2): Independent elected member who joins any political party after election becomes disqualified."),

    # ── Section 7: Miscellaneous / Key Articles ─────────────────────────────────
    (7, "easy",
     "విధానసభ సభ్యత్వానికి అర్హతలు ఏ అనుచ్ఛేదంలో ఉన్నాయి? / Qualifications for Vidhan Sabha membership are in which Article?",
     "అనుచ్ఛేదం 170 / Art.170",
     "అనుచ్ఛేదం 173 / Art.173",
     "అనుచ్ఛేదం 175 / Art.175",
     "అనుచ్ఛేదం 177 / Art.177",
     "b",
     "అనుచ్ఛేదం 173: రాష్ట్ర శాసనమండలి సభ్యత్వానికి అర్హతలు — పౌరుడు, వయస్సు, ఓటరు నమోదు, అనర్హతలు లేకుండా ఉండటం. / Art.173: Qualifications for membership of state legislature."),

    (7, "medium",
     "విధానసభ సభ్యుడు ఒక సంవత్సరం పాటు అనుమతి లేకుండా సభకు హాజరు కాకుంటే ఏమవుతుంది? / What happens if MLA absent without permission for one year?",
     "సభ్యత్వం రద్దవుతుంది / Seat declared vacant",
     "జరిమానా విధిస్తారు / Fine imposed",
     "ఆ స్థానం హోల్డ్ అవుతుంది / Seat held",
     "ఎన్నికల కమిషన్ నిర్ణయిస్తుంది / EC decides",
     "a",
     "అనుచ్ఛేదం 190(4): సభ్యుడు 60 రోజులకు మించి అనుమతి లేకుండా సభకు హాజరు కాకుంటే సభ్యత్వం రద్దవుతుంది. / Art.190(4): Seat vacated if member absent without permission for 60 days."),

    (7, "hard",
     "రాష్ట్ర శాసనమండలి సభ్యుల ప్రమాణ పత్రం ఏ షెడ్యూల్‌లో ఉంటుంది? / Oath form for state legislature members is in which Schedule?",
     "రెండో షెడ్యూల్ / 2nd Schedule",
     "మూడో షెడ్యూల్ / 3rd Schedule",
     "నాల్గో షెడ్యూల్ / 4th Schedule",
     "ఆరో షెడ్యూల్ / 6th Schedule",
     "b",
     "తృతీయ షెడ్యూల్ (Third Schedule): రాష్ట్ర శాసనమండలి సభ్యుల ప్రమాణ పత్రాలు కూడా ఇందులోనే ఉంటాయి. / Third Schedule contains oath forms for state legislature members too."),

    (7, "easy",
     "విధానసభ 'ఆప్రోప్రియేషన్ బిల్లు' (Appropriation Bill) ఏ సభలో ప్రవేశపెట్టాలి? / State Appropriation Bill introduced in which House?",
     "విధానపరిషత్ / Vidhan Parishad",
     "విధానసభ / Vidhan Sabha",
     "రెండు సభల్లో ఒకేసారి / Both simultaneously",
     "ఏ సభలోనైనా / Either House",
     "b",
     "అనుచ్ఛేదం 204: రాష్ట్ర ఆప్రోప్రియేషన్ బిల్లు విధానసభలోనే ప్రవేశపెట్టాలి — ఇది మనీ బిల్లు స్వభావం కలిగి ఉంటుంది. / Art.204: State Appropriation Bill introduced only in Vidhan Sabha — it has Money Bill character."),

    (7, "medium",
     "రాష్ట్ర శాసనమండలి భాషను ఏ అనుచ్ఛేదం నిర్ణయిస్తుంది? / Which Article deals with language to be used in state legislature?",
     "అనుచ్ఛేదం 208 / Art.208",
     "అనుచ్ఛేదం 210 / Art.210",
     "అనుచ్ఛేదం 211 / Art.211",
     "అనుచ్ఛేదం 212 / Art.212",
     "b",
     "అనుచ్ఛేదం 210: రాష్ట్ర శాసనమండలిలో హిందీ లేదా రాష్ట్ర అధికారిక భాష వినియోగించాలి. స్పీకర్/చైర్మన్ అనుమతితో ఇతర భాష వాడవచ్చు. / Art.210: Hindi or official language of state used; other language with Speaker's/Chairman's permission."),

    (7, "hard",
     "విధానపరిషత్ రద్దు చేయబడిన తర్వాత ఆ చర్యపై న్యాయస్థానంలో సవాలు చేయవచ్చా? / Can abolition of Vidhan Parishad be challenged in court?",
     "అవును / Yes",
     "లేదు — పార్లమెంటు అధికారం / No — Parliament's power",
     "హైకోర్టులో మాత్రమే / Only in HC",
     "సుప్రీం కోర్టులో మాత్రమే / Only in SC",
     "b",
     "అనుచ్ఛేదం 169 ప్రకారం పార్లమెంటు చేసే చట్టానికి రాజ్యాంగ సవరణ హోదా లేదు — సాధారణ చట్టం. SC సమీక్ష సాంకేతికంగా సాధ్యం, ఆచరణలో పార్లమెంటు అధికారాన్ని సమర్థిస్తారు. / Parliament's law under Art.169 is ordinary legislation; SC review technically possible but Parliament's power generally upheld."),

    (7, "medium",
     "రాష్ట్ర శాసనమండలి సభ్యుల అర్హతలు ఏ అనుచ్ఛేదంలో ఉన్నాయి? / Qualifications for state legislature membership are in which Article?",
     "అనుచ్ఛేదం 173 / Art.173",
     "అనుచ్ఛేదం 191 / Art.191",
     "అనుచ్ఛేదం 192 / Art.192",
     "అనుచ్ఛేదం 172 / Art.172",
     "a",
     "అనుచ్ఛేదం 173: రాష్ట్ర శాసనమండలి సభ్యత్వానికి అర్హతలు — భారత పౌరుడు, విధానసభకు 25 సంవత్సరాలు మరియు విధానపరిషత్‌కు 30 సంవత్సరాలు. అనర్హతలు Art.191 లో ఉన్నాయి. / Art.173: Qualifications — Indian citizen; 25 years for Vidhan Sabha; 30 years for Vidhan Parishad. Disqualifications in Art.191."),

    (7, "hard",
     "అనుచ్ఛేదం 208 రాష్ట్ర శాసనమండలిలో ఏ విషయాన్ని నిర్ణయిస్తుంది? / Art.208 deals with what in state legislature?",
     "వ్యాపార నిర్వహణ నియమాలు / Rules of procedure",
     "సభ్యుల జీతాలు / Members' salaries",
     "కోరం / Quorum",
     "మనీ బిల్లు నిర్వచనం / Definition of Money Bill",
     "a",
     "అనుచ్ఛేదం 208: రాష్ట్ర శాసనమండలి తన వ్యాపారం నిర్వహణకు నియమాలు తయారు చేసుకోవచ్చు. రాష్ట్రపతి ఆమోదం లేకుండా. Art.100(3) = కోరం (1/10 సభ్యులు). / Art.208: State legislature may make rules for regulation of procedure. Quorum = 1/10 of total members (Art.189(3))."),
]


def _seed_polity_ch19_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    ph = '%s' if use_postgres else '?'
    existing = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE subject={ph} AND topic={ph} AND chapter_num={ph}",
        (_SUBJECT, _TOPIC, _CH))
    row = existing.fetchone()
    if row and not force:
        return
    sections_json = __import__('json').dumps(
        [{"title": s, "content": ""} for s in _SECTIONS], ensure_ascii=False)
    if row and force:
        note_id = row_to_dict_fn(row)['id']
        db_exec_fn(conn,
            f"UPDATE study_notes SET chapter_title_te={ph}, chapter_title_en={ph}, "
            f"pages_ref={ph}, sections_json={ph} WHERE id={ph}",
            (_TITLE_TE, _TITLE_EN, _PAGES, sections_json, note_id))
    else:
        db_exec_fn(conn,
            f"INSERT INTO study_notes (subject, topic, chapter_num, chapter_title_te, "
            f"chapter_title_en, pages_ref, sections_json) VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph})",
            (_SUBJECT, _TOPIC, _CH, _TITLE_TE, _TITLE_EN, _PAGES, sections_json))


def _seed_polity_ch19_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
    ph = '%s' if use_postgres else '?'
    diff_map = {"easy": 1, "medium": 2, "hard": 3, "toughest": 4, 1: 1, 2: 2, 3: 3, 4: 4}
    note_cur = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE subject={ph} AND topic={ph} AND chapter_num={ph}",
        (_SUBJECT, _TOPIC, _CH))
    note_row = note_cur.fetchone()
    if not note_row:
        return
    note_id = row_to_dict_fn(note_row)['id']
    existing = db_exec_fn(conn,
        f"SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    if list(existing.fetchone())[0] > 0:
        return
    for row in _MCQS:
        sec_idx = row[0]; diff_int = diff_map.get(row[1], 1)
        q_te = row[2]; opt_a = row[3]; opt_b = row[4]; opt_c = row[5]; opt_d = row[6]
        correct = str(row[7]).lower(); expl = row[8] if len(row) > 8 else ''
        exam_type = row[9] if len(row) > 9 else 'General'
        db_exec_fn(conn,
            f"""INSERT INTO chapter_mcqs (study_note_id, section_idx, difficulty, exam_type,
                 q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te)
                VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
            (note_id, sec_idx, diff_int, exam_type, q_te, opt_a, opt_b, opt_c, opt_d, correct, expl))
