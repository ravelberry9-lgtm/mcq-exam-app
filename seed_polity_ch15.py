# seed_polity_ch15.py
# Chapter 15 – President of India
# (భారత రాష్ట్రపతి)
# Lakshmikanth's Indian Polity | APPSC Group 2 Standard
# Total Sections: 8 | Total MCQs: 63 | PYQs: 5
# Difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
# ─────────────────────────────────────────────────────

import json as _json

POLITY_CH15_SECTIONS = [
    {
        "title": "15.1 రాష్ట్రపతి — ఎన్నిక మరియు అర్హతలు",
        "sub": "Art.52–62 · Electoral College · STV · Qualifications · Term · Oath · CJI",
        "audio": ""
    },
    {
        "title": "15.2 రాష్ట్రపతి — తొలగింపు మరియు ఖాళీ",
        "sub": "Art.61 · Impeachment · 14 Days Notice · 2/3 Majority · Art.65 VP Acting",
        "audio": ""
    },
    {
        "title": "15.3 కార్యనిర్వాహక మరియు శాసన అధికారాలు",
        "sub": "Art.53 · Art.74 · Art.77 · Art.86–87 · Art.108 · Art.111 · CoM Advice",
        "audio": ""
    },
    {
        "title": "15.4 ఆర్థిక మరియు న్యాయ అధికారాలు",
        "sub": "Art.72 · Pardoning Power · Pardon/Commutation/Remission · Art.143 · Finance Commission",
        "audio": ""
    },
    {
        "title": "15.5 ఆర్డినెన్స్ అధికారం",
        "sub": "Art.123 · When Parliament Not in Session · 6 Weeks · D.C. Wadhwa · Repromulgation",
        "audio": ""
    },
    {
        "title": "15.6 అత్యవసర అధికారాలు",
        "sub": "Art.352 · National Emergency · Art.356 · President's Rule · Art.360 · Financial Emergency",
        "audio": ""
    },
    {
        "title": "15.7 వీటో అధికారాలు మరియు విచక్షణాధికారాలు",
        "sub": "Absolute Veto · Suspensive Veto · Pocket Veto · Discretionary Powers · Situational Discretion",
        "audio": ""
    },
    {
        "title": "15.8 కఠిన ప్రశ్నలు — APPSC/UPSC PYQs",
        "sub": "Electoral disputes · Art.71 SC · President vs Governor pardoning · Historical PYQs",
        "audio": ""
    },
]

POLITY_CH15_MCQS = [

    # ── Section 0: Election & Qualifications ─────────────────────────────────────
    (0, 1,
     "భారత రాష్ట్రపతి ఎన్నికకు సంబంధించిన అనుచ్ఛేదం ఏది?\n(Which Article deals with the election of the President of India?)",
     "Art.52", "Art.54",
     "Art.56", "Art.58",
     "b",
     "Art.54: రాష్ట్రపతి ఎన్నిక — ఎలక్టోరల్ కాలేజ్ ద్వారా జరుగుతుంది. Art.52: భారత రాష్ట్రపతి ఉంటారు అని నిర్ణయిస్తుంది.\n(Art.54 deals with election of President through Electoral College. Art.52 establishes the office of President.)"),

    (0, 2,
     "రాష్ట్రపతి ఎలక్టోరల్ కాలేజ్ సభ్యులు ఎవరు?\n(Who are the members of the Electoral College for Presidential election?)",
     "పార్లమెంట్ ఉభయ సభల సభ్యులు మాత్రమే",
     "లోక్‌సభ మాత్రమే",
     "పార్లమెంట్ ఉభయ సభల ఎన్నికైన సభ్యులు + రాష్ట్రాల శాసనసభల ఎన్నికైన సభ్యులు + ఢిల్లీ, పుదుచ్చేరి శాసనసభల ఎన్నికైన సభ్యులు\n(Elected members of both Houses of Parliament + State Legislative Assemblies + Delhi & Puducherry)",
     "రాజ్యసభ నామినేటెడ్ సభ్యులు కూడా ఉంటారు",
     "c",
     "Art.54: రాష్ట్రపతి ఎన్నిక — పార్లమెంట్ ఉభయ సభల ఎన్నికైన సభ్యులు మరియు రాష్ట్రాల శాసనసభల ఎన్నికైన సభ్యులు పాల్గొంటారు. నామినేటెడ్ సభ్యులు పాల్గొనరు. 70వ సవరణ (1992) తర్వాత ఢిల్లీ, పుదుచ్చేరి కూడా చేరాయి.\n(Art.54: Elected members of both LS and RS + elected members of State Legislative Assemblies (incl. Delhi & Puducherry after 70th Amendment 1992). Nominated members excluded.)"),

    (0, 1,
     "రాష్ట్రపతి ఎన్నికలో ఏ పద్ధతి వాడతారు?\n(What method is used in the Presidential election?)",
     "ప్రత్యక్ష ఎన్నిక (Direct Election)",
     "సాధారణ మెజారిటీ",
     "నిష్పత్తి ప్రాతినిధ్యం — ఒకే బదిలీయోగ్య ఓటు పద్ధతి (STV)\n(Proportional Representation — Single Transferable Vote)",
     "పార్లమెంట్ సభ్యులు ఎన్నుకుంటారు మాత్రమే",
     "c",
     "Art.55(3): రాష్ట్రపతి ఎన్నిక నిష్పత్తి ప్రాతినిధ్యం — ఒకే బదిలీయోగ్య ఓటు (Proportional Representation with Single Transferable Vote — STV) పద్ధతిలో జరుగుతుంది. రహస్య బ్యాలెట్ ద్వారా.\n(Art.55(3): Presidential election is by Proportional Representation with Single Transferable Vote (STV) method using secret ballot.)"),

    (0, 2,
     "రాష్ట్రపతి పదవికి అర్హతలు ఏవి? (Art.58)\n(What are the qualifications for President of India under Art.58?)",
     "భారత పౌరుడు, 30 సంవత్సరాలు",
     "భారత పౌరుడు, 35 సంవత్సరాలు, లోక్‌సభ సభ్యత్వానికి అర్హుడు, లాభదాయక పదవిలో లేనివాడు\n(Indian citizen, 35 years, eligible for LS membership, holds no office of profit)",
     "భారత పౌరుడు, 40 సంవత్సరాలు, రాజ్యసభ సభ్యత్వానికి అర్హుడు",
     "భారత పౌరుడు, 25 సంవత్సరాలు",
     "b",
     "Art.58: రాష్ట్రపతి అర్హతలు — (1) భారత పౌరుడు, (2) 35 సంవత్సరాలు పూర్తి, (3) లోక్‌సభ సభ్యత్వానికి అర్హుడు, (4) కేంద్ర లేదా రాష్ట్ర ప్రభుత్వంలో లాభదాయక పదవి లేనివాడు.\n(Art.58: Qualifications — (1) Citizen of India, (2) completed 35 years, (3) eligible for LS membership, (4) holds no office of profit under Govt of India or State Govt.)"),

    (0, 1,
     "రాష్ట్రపతి పదవీ కాలం ఎంత?\n(What is the term of office of the President of India?)",
     "4 సంవత్సరాలు", "5 సంవత్సరాలు",
     "6 సంవత్సరాలు", "పదవీ ప్రమాణం నుండి అనుగ్రహించిన వరకు",
     "b",
     "Art.56: రాష్ట్రపతి పదవీ కాలం 5 సంవత్సరాలు — పదవిలోకి ప్రవేశించిన తేదీ నుండి. Art.57 ప్రకారం పునర్వ్యక్తి ఎన్నికకు అర్హుడు.\n(Art.56: President holds office for 5 years from the date of entering office. Art.57 — eligible for re-election.)"),

    (0, 2,
     "రాష్ట్రపతి ప్రమాణ స్వీకారం ఎవరి సమక్షంలో జరుగుతుంది?\n(In whose presence does the President take the oath of office?)",
     "లోక్‌సభ స్పీకర్",
     "ప్రధానమంత్రి",
     "సుప్రీం కోర్టు ప్రధాన న్యాయమూర్తి — Art.60\n(Chief Justice of India — Art.60)",
     "రాజ్యసభ చైర్మన్",
     "c",
     "Art.60: రాష్ట్రపతి ప్రమాణం సుప్రీం కోర్టు ప్రధాన న్యాయమూర్తి (CJI) లేదా అందుబాటులో ఉన్న సీనియర్ న్యాయమూర్తి సమక్షంలో చేస్తారు.\n(Art.60: President takes oath before the Chief Justice of India, or, in their absence, the most senior judge of the Supreme Court available.)"),

    (0, 3,
     "రాష్ట్రపతి ఎన్నికలో MP ఓటు విలువ ఎలా లెక్కిస్తారు?\n(How is the value of an MP's vote calculated in the Presidential election?)",
     "ప్రతి MP ఓటు విలువ 1",
     "మొత్తం రాష్ట్రాల MLA ఓట్ల మొత్తం విలువ ÷ పార్లమెంట్ ఎన్నికైన సభ్యుల మొత్తం సంఖ్య\n(Total value of all State MLA votes ÷ Total elected MPs of both Houses)",
     "రాష్ట్ర జనాభా ÷ 1000",
     "రాష్ట్రాల సంఖ్య ÷ MP సంఖ్య",
     "b",
     "MP ఓటు విలువ = అన్ని రాష్ట్రాల MLA ఓట్ల మొత్తం ÷ పార్లమెంట్ ఎన్నికైన సభ్యుల మొత్తం. MLA ఓటు విలువ = రాష్ట్ర జనాభా ÷ (రాష్ట్ర ఎన్నికైన MLA సంఖ్య × 1000). ఇది Art.55 కింద అనుపాత ప్రాతినిధ్యం నిర్ధారిస్తుంది.\n(MP vote value = Total value of all State MLA votes ÷ Total elected MPs. MLA vote value = State population ÷ (Elected MLAs × 1000). This ensures uniformity under Art.55.)"),

    (0, 2,
     "రాష్ట్రపతి పదవికి నామినేషన్ దాఖలు చేయడానికి ఎంత మంది ప్రతిపాదకులు అవసరం?\n(How many proposers and seconders are required to file nomination for Presidential election?)",
     "5 ప్రతిపాదకులు, 5 అనుమోదకులు",
     "50 ప్రతిపాదకులు + 50 అనుమోదకులు — ఎలక్టోరల్ కాలేజ్ సభ్యులు\n(50 proposers + 50 seconders — from Electoral College)",
     "25 ప్రతిపాదకులు + 25 అనుమోదకులు",
     "10 ప్రతిపాదకులు + 10 అనుమోదకులు",
     "b",
     "ప్రెసిడెన్షియల్ అండ్ వైస్ ప్రెసిడెన్షియల్ ఎలక్షన్స్ యాక్ట్, 1952 ప్రకారం: 50 ప్రతిపాదకులు (proposers) మరియు 50 అనుమోదకులు (seconders) — ఎలక్టోరల్ కాలేజ్ సభ్యులు. ₹15,000 డిపాజిట్.\n(As per Presidential and Vice-Presidential Elections Act 1952: 50 proposers + 50 seconders from Electoral College. Security deposit: ₹15,000.)"),

    # ── Section 1: Removal & Vacancy ─────────────────────────────────────────────
    (1, 2,
     "రాష్ట్రపతిని తొలగించే (Impeachment) విధానం ఏది?\n(What is the procedure for impeachment of the President?)",
     "లోక్‌సభ మాత్రమే 2/3 మెజారిటీతో తొలగించవచ్చు",
     "రెండు సభలలో ఏ ఒక సభ 14 రోజుల నోటీసుతో 2/3 మెజారిటీతో ప్రవేశపెట్టవచ్చు; ఆ తర్వాత ఇతర సభ విచారించి 2/3 మెజారిటీతో ఆమోదించాలి\n(Either House, 14-day notice, 2/3 of total membership; other House investigates and passes with 2/3 majority)",
     "రాజ్యసభలో మాత్రమే ప్రవేశపెట్టవచ్చు",
     "సుప్రీం కోర్టు సిఫార్సు ఆధారంగా పార్లమెంట్ తొలగిస్తుంది",
     "b",
     "Art.61: Impeachment రెండు సభలలో ఏ ఒక సభలోనైనా ప్రవేశపెట్టవచ్చు. 14 రోజుల నోటీసు — సభ మొత్తం సభ్యత్వంలో కనీసం 1/4 మంది సంతకంతో. ఆ సభ మొత్తం సభ్యత్వంలో 2/3 ఆమోదిస్తే, ఇతర సభ విచారిస్తుంది. ఇతర సభ కూడా మొత్తం సభ్యత్వంలో 2/3 ఆమోదిస్తే రాష్ట్రపతి తొలగించబడతారు.\n(Art.61: Impeachment may be initiated in either House. 14-day notice signed by 1/4 of total House membership. If passed by 2/3 of total membership, other House investigates and must also pass by 2/3 for removal.)"),

    (1, 2,
     "Impeachment నోటీసుకు ఎంత మంది సభ్యుల సంతకం అవసరం?\n(How many members must sign the Impeachment notice?)",
     "సభ మొత్తం సభ్యత్వంలో 1/2",
     "సభ మొత్తం సభ్యత్వంలో 1/4\n(One-fourth of the total membership of the House)",
     "100 మంది సభ్యులు",
     "50 మంది సభ్యులు",
     "b",
     "Art.61(2): Impeachment నోటీసుకు సభ మొత్తం సభ్యత్వంలో కనీసం 1/4 మంది సంతకం అవసరం. తర్వాత 14 రోజుల నోటీసు ఇవ్వాలి. తర్వాత ఆ సభ 2/3 మెజారిటీతో ఆమోదించాలి.\n(Art.61(2): Notice for Impeachment must be signed by at least 1/4 of the total membership of the initiating House, followed by 14 days notice.)"),

    (1, 1,
     "రాష్ట్రపతి పదవిలో ఖాళీ ఏర్పడినప్పుడు ఎవరు ఆ బాధ్యత నిర్వర్తిస్తారు?\n(Who acts as President when the office of President falls vacant?)",
     "ప్రధానమంత్రి",
     "లోక్‌సభ స్పీకర్",
     "ఉపరాష్ట్రపతి — Art.65\n(Vice President — Art.65)",
     "సుప్రీం కోర్టు ప్రధాన న్యాయమూర్తి",
     "c",
     "Art.65: రాష్ట్రపతి పదవి ఖాళీ అయినప్పుడు ఉపరాష్ట్రపతి ఆ బాధ్యత నిర్వర్తిస్తారు. VP కూడా అందుబాటులో లేకపోతే సుప్రీం కోర్టు ప్రధాన న్యాయమూర్తి రాష్ట్రపతి బాధ్యతలు నిర్వర్తిస్తారు.\n(Art.65: Vice President acts as President when the office falls vacant. If VP is also unavailable, the Chief Justice of India acts as President.)"),

    (1, 3,
     "రాష్ట్రపతి Impeachment మరియు No-Confidence Motion మధ్య ముఖ్యమైన తేడా ఏమిటి?\n(Key difference between Presidential Impeachment and No-Confidence Motion?)",
     "రెండూ ఒకటే",
     "NCM లోక్‌సభలో మాత్రమే; Impeachment రెండు సభలలోనూ ప్రారంభించవచ్చు మరియు Impeachmentకు రాజ్యాంగ ఉల్లంఘన నిరూపించాలి\n(NCM only in LS; Impeachment in either House; requires proof of violation of Constitution)",
     "Impeachment లోక్‌సభలో మాత్రమే",
     "NCM సాధారణ మెజారిటీతో ఆమోదించవచ్చు",
     "b",
     "NCM: లోక్‌సభలో మాత్రమే, CoM వ్యతిరేకంగా, సాధారణ బహుమతి. Impeachment: రెండు సభలలోనూ ప్రారంభించవచ్చు, రాష్ట్రపతిపై, రాజ్యాంగ ఉల్లంఘన అవసరం, 2/3 మెజారిటీ (మొత్తం సభ్యత్వం) అవసరం.\n(NCM: Only in LS, against CoM, simple majority. Impeachment: Either House, against President, requires violation of Constitution, needs 2/3 of total membership of each House.)"),

    # ── Section 2: Executive & Legislative Powers ─────────────────────────────────
    (2, 1,
     "సమాఖ్య కార్యనిర్వాహక అధికారం ఎవరికి ఉంది?\n(In whom is the executive power of the Union vested?)",
     "ప్రధానమంత్రి", "మంత్రి మండలి",
     "రాష్ట్రపతి — Art.53\n(President — Art.53)", "లోక్‌సభ",
     "c",
     "Art.53(1): సమాఖ్య కార్యనిర్వాహక అధికారం రాష్ట్రపతిలో నిహితంగా ఉంటుంది. ఈ అధికారాన్ని రాష్ట్రపతి ప్రత్యక్షంగా లేదా అధికారులు/మంత్రుల ద్వారా నిర్వర్తిస్తారు.\n(Art.53(1): The executive power of the Union shall be vested in the President and shall be exercised directly or through subordinate officers.)"),

    (2, 2,
     "44వ రాజ్యాంగ సవరణ (1978) తర్వాత మంత్రి మండలి సలహా రాష్ట్రపతికి బాధ్యకరంగా ఉందా?\n(After 44th Amendment 1978, is the Council of Ministers' advice binding on the President?)",
     "కాదు — రాష్ట్రపతి విచక్షణతో వ్యవహరించవచ్చు",
     "అవును — మంత్రి మండలి సలహా తప్పనిసరిగా పాటించాలి; కానీ రాష్ట్రపతి ఒకసారి పునర్విచారణ కోరవచ్చు\n(Yes — advice is binding; but President may return once for reconsideration)",
     "కేవలం యుద్ధకాలంలో మాత్రమే",
     "రాజ్యసభ చైర్మన్ నిర్ణయిస్తారు",
     "b",
     "Art.74(1) — 44వ సవరణ (1978): మంత్రి మండలి సలహా రాష్ట్రపతికి బాధ్యకరం. కానీ రాష్ట్రపతి మంత్రి మండలి సలహాను ఒకసారి పునర్విచారణ (reconsider) కోసం తిరిగి పంపించవచ్చు. మళ్లీ వచ్చిన సలహా తప్పనిసరి.\n(Art.74(1) after 44th Amendment: CoM advice is binding on President. However, President may return advice once for reconsideration; the reconsidered advice is binding.)"),

    (2, 2,
     "రాష్ట్రపతి పార్లమెంట్‌ను సమావేశ పరచడం, వాయిదా వేయడం, రద్దు చేయడం — ఏ అనుచ్ఛేదం?\n(Under which Article can the President summon, prorogue, and dissolve Parliament?)",
     "Art.80", "Art.83",
     "Art.85", "Art.108",
     "c",
     "Art.85(1): రాష్ట్రపతి ఉభయ సభలను సమావేశ పరుస్తారు (Summon). Art.85(2)(a): రాష్ట్రపతి సమావేశం వాయిదా వేయవచ్చు (Prorogue). Art.85(2)(b): రాష్ట్రపతి లోక్‌సభను రద్దు చేయవచ్చు (Dissolve).\n(Art.85: President summons both Houses; prorogues sessions; and may dissolve Lok Sabha under Art.85(2)(b).)"),

    (2, 2,
     "రాష్ట్రపతి బిల్లుపై 'అసెంట్' ఇవ్వకుండా తిరిగి పంపించవచ్చా?\n(Can the President return a Bill without giving assent — and is this power unlimited?)",
     "కాదు, తప్పనిసరిగా ఆమోదించాలి",
     "అవును, రాష్ట్రపతి మనీ బిల్లు కాకుండా ఏ బిల్లయినా ఒకసారి పునర్విచారణకు తిరిగి పంపించవచ్చు; రెండవ సారి ఆమోదించకపోవడం సాధ్యం కాదు\n(Yes — for non-Money Bills; can return once; if passed again must give assent)",
     "అవును, ఎప్పుడైనా అనేక సార్లు తిరిగి పంపించవచ్చు",
     "కేవలం రాజ్యాంగ సవరణ బిల్లుకు మాత్రమే",
     "b",
     "Art.111: రాష్ట్రపతి (మనీ బిల్లు కాకుండా) బిల్లును ఒకసారి పునర్విచారణకు తిరిగి పంపించవచ్చు. పార్లమెంట్ మళ్లీ ఆమోదిస్తే — సవరణలతో అయినా లేకుండా అయినా — రాష్ట్రపతి తప్పనిసరిగా ఆమోదించాలి. మనీ బిల్లుకు Suspensive Veto వర్తించదు.\n(Art.111: President may return a non-Money Bill once for reconsideration. If Parliament passes it again (with/without amendments), President MUST give assent. Not applicable to Money Bills.)"),

    (2, 3,
     "రాష్ట్రపతి 'ప్రత్యేక సందేశం' (Special Address) ఏ సందర్భంలో ఇస్తారు?\n(When does the President give a 'Special Address' to Parliament?)",
     "ప్రతి సెషన్ మొదటి రోజు",
     "కేవలం జాతీయ అత్యవసర పరిస్థితిలో",
     "ప్రతి సంవత్సరం మొదటి సెషన్‌లో మరియు సార్వత్రిక ఎన్నికల తర్వాత కొత్త లోక్‌సభ మొదటి సమావేశంలో — Art.87\n(Art.87 — at the first session each year and first LS session after general elections)",
     "బడ్జెట్ సమావేశం ముందు మాత్రమే",
     "c",
     "Art.87: రాష్ట్రపతి ప్రతి సంవత్సరం మొదటి సెషన్ ప్రారంభంలో మరియు సార్వత్రిక ఎన్నికల తర్వాత కొత్త లోక్‌సభ మొదటి సమావేశంలో ఉభయ సభల సంయుక్త సమావేశాన్ని ఉద్దేశించి ప్రసంగిస్తారు.\n(Art.87: President addresses joint sitting of both Houses at the commencement of the first session each year and the first session after each general election.)"),

    # ── Section 3: Financial & Judicial Powers ────────────────────────────────────
    (3, 1,
     "రాష్ట్రపతి 'క్షమాభిక్ష అధికారం' ఏ అనుచ్ఛేదం కింద ఉంటుంది?\n(Under which Article does the President have pardoning power?)",
     "Art.70", "Art.72",
     "Art.74", "Art.76",
     "b",
     "Art.72: రాష్ట్రపతి క్షమాభిక్ష అధికారం — Pardon, Reprieve, Respite, Remission, Commutation. ఈ అధికారం కేంద్ర చట్టాల కింద శిక్షకు, కోర్ట్ మార్షల్ శిక్షకు, మరణ శిక్షకు వర్తిస్తుంది.\n(Art.72: President's pardoning power — Pardon, Reprieve, Respite, Remission, Commutation. Applies to offences against Union law, court-martial sentences, and death sentences.)"),

    (3, 2,
     "Art.72 కింద రాష్ట్రపతి క్షమాభిక్ష రకాలు ఏవి?\n(What are the types of Presidential clemency under Art.72?)",
     "Pardon మరియు Commutation మాత్రమే",
     "Pardon, Reprieve, Respite, Remission, Commutation — ఐదు రకాలు\n(Five types: Pardon, Reprieve, Respite, Remission, Commutation)",
     "కేవలం Pardon మాత్రమే",
     "Pardon, Appeal మాత్రమే",
     "b",
     "Art.72 క్షమాభిక్ష రకాలు:\n1) Pardon: శిక్ష పూర్తిగా రద్దు — నేరం మాపు\n2) Commutation: తక్కువ శిక్షగా మార్పు\n3) Remission: శిక్ష కాలం తగ్గించడం (స్వభావం మారదు)\n4) Respite: ప్రత్యేక కారణాల వల్ల తక్కువ శిక్ష\n5) Reprieve: తాత్కాలిక ఆపు (mostly death sentence)\n(5 types: Pardon — full absolution; Commutation — lesser punishment; Remission — shorter period; Respite — lesser sentence for special reasons; Reprieve — temporary suspension.)"),

    (3, 2,
     "రాష్ట్రపతి మరియు గవర్నర్ క్షమాభిక్ష అధికారాలలో ముఖ్యమైన తేడా ఏమిటి?\n(Key difference between President's and Governor's pardoning powers?)",
     "తేడా లేదు, రెండూ ఒకటే",
     "రాష్ట్రపతి మాత్రమే మరణ శిక్ష క్షమించగలరు; రాష్ట్రపతి కోర్ట్ మార్షల్ శిక్ష క్షమించగలరు; గవర్నర్ ఈ రెండూ చేయలేరు\n(President alone can pardon death sentence & court-martial; Governor cannot)",
     "గవర్నర్ మాత్రమే మరణ శిక్ష క్షమించగలరు",
     "రాష్ట్రపతి కేవలం రాష్ట్ర చట్టాల శిక్షలు క్షమించగలరు",
     "b",
     "తేడాలు:\n• రాష్ట్రపతి మాత్రమే మరణ శిక్ష క్షమించగలరు (Art.72) — గవర్నర్ (Art.161) చేయలేరు\n• రాష్ట్రపతి మాత్రమే కోర్ట్ మార్షల్ (Court Martial) శిక్ష క్షమించగలరు\n• గవర్నర్ కేంద్ర చట్టాల కింద శిక్షలు క్షమించలేరు\n(President uniquely: (1) pardon death sentence, (2) pardon court-martial sentences. Governor (Art.161) cannot pardon death sentences or court-martial punishments.)"),

    (3, 3,
     "Art.143 కింద రాష్ట్రపతి సుప్రీం కోర్టు అభిప్రాయం కోరవచ్చా?\n(Can President seek opinion of Supreme Court under Art.143?)",
     "కాదు, రాష్ట్రపతి న్యాయ అభిప్రాయాలు కోరలేరు",
     "అవును — Art.143 కింద రాష్ట్రపతి SC అభిప్రాయం కోరవచ్చు; SC అభిప్రాయం ఇవ్వడం తప్పనిసరి కాదు; అభిప్రాయం బాధ్యకరం కాదు\n(Yes — Art.143 Presidential Reference; SC may or may not give opinion; opinion is advisory not binding)",
     "అవును, SC అభిప్రాయం బాధ్యకరంగా ఉంటుంది",
     "కేవలం అత్యవసర పరిస్థితిలో మాత్రమే",
     "b",
     "Art.143: రాష్ట్రపతి రెఫరెన్స్ (Presidential Reference) — ఏదైనా ముఖ్యమైన చట్టపరమైన లేదా రాజ్యాంగ ప్రశ్నపై SC అభిప్రాయం కోరవచ్చు. SC అభిప్రాయం ఇవ్వడం విచక్షణాధీనం; అభిప్రాయం సలహాగానే ఉంటుంది — బాధ్యకరం కాదు.\n(Art.143: President may refer any question of law or fact of public importance to SC. SC may or may not give opinion; if given, opinion is advisory — not binding on President.)"),

    # ── Section 4: Ordinance Power ───────────────────────────────────────────────
    (4, 1,
     "రాష్ట్రపతి ఆర్డినెన్స్ జారీ చేయగల సందర్భం ఏది?\n(When can the President promulgate an Ordinance?)",
     "పార్లమెంట్ సమావేశంలో ఉన్నప్పుడు",
     "పార్లమెంట్ రెండు సభలూ విరామంలో (recess) ఉన్నప్పుడు మాత్రమే — Art.123\n(Only when both Houses of Parliament are not in session — Art.123)",
     "కేవలం యుద్ధకాలంలో",
     "ఒక సభ అనుమతితో",
     "b",
     "Art.123: రాష్ట్రపతి ఆర్డినెన్స్ జారీ చేయడానికి రెండు సభలూ (LS మరియు RS) సమావేశంలో లేనప్పుడు మాత్రమే అవకాశం ఉంటుంది. ఒక సభ మాత్రమే సమావేశంలో లేకపోయినా సరిపోదు.\n(Art.123: Ordinance can be issued only when BOTH Houses are not in session — not just one House being in recess.)"),

    (4, 2,
     "రాష్ట్రపతి ఆర్డినెన్స్ పార్లమెంట్ ముందు ఎంత కాలంలో ఉంచాలి?\n(Within what period must a Presidential Ordinance be laid before Parliament?)",
     "పార్లమెంట్ సమావేశమైన వెంటనే 30 రోజులలోపు",
     "పార్లమెంట్ సమావేశమైన తర్వాత 6 వారాలలోపు\n(Within 6 weeks of Parliament reassembling)",
     "3 నెలలు",
     "6 నెలలు",
     "b",
     "Art.123(2): ఆర్డినెన్స్ పార్లమెంట్ పునర్ సమావేశమైన తర్వాత 6 వారాలలోపు ఉభయ సభల ముందు ఉంచాలి. 6 వారాల తర్వాత స్వయంచాలకంగా రద్దవుతుంది. పార్లమెంట్ తిరస్కరించినా రద్దవుతుంది.\n(Art.123(2): Ordinance must be laid before both Houses within 6 weeks of Parliament reassembling. It ceases to operate after 6 weeks or if disapproved by Parliament.)"),

    (4, 2,
     "రాష్ట్రపతి ఆర్డినెన్స్ గరిష్ట జీవిత కాలం (Maximum Life) ఎంత?\n(What is the maximum life of a Presidential Ordinance?)",
     "3 నెలలు", "6 నెలలు",
     "6 నెలలు + 6 వారాలు\n(6 months + 6 weeks — approx 7.5 months)",
     "1 సంవత్సరం",
     "c",
     "ఆర్డినెన్స్ జారీ అయిన తర్వాత, పార్లమెంట్ తిరిగి సమావేశమయ్యే వరకు రెండు సభల మధ్య గరిష్ట విరామం 6 నెలలు (Art.85) + 6 వారాలు (Art.123) = మొత్తం దాదాపు 7.5 నెలలు.\n(Max life of Ordinance = Max gap between Parliamentary sessions (6 months under Art.85) + 6 weeks laid-before period = approximately 7.5 months.)"),

    (4, 3,
     "D.C. Wadhwa కేసు (1987) రాష్ట్రపతి ఆర్డినెన్స్‌పై ఏ నిర్ణయం ఇచ్చింది?\n(What did D.C. Wadhwa case 1987 rule about Presidential Ordinances?)",
     "రాష్ట్రపతి ఆర్డినెన్స్‌లు న్యాయసమీక్షకు అతీతం",
     "ఆర్డినెన్స్‌లు పదే పదే పునర్జారీ (Repromulgation) చేయడం రాజ్యాంగవ్యతిరేకం — ఇది పార్లమెంట్ అధికారాలను దెబ్బ తీస్తుంది\n(Repromulgation of Ordinances is unconstitutional — fraud on Constitution)",
     "ఆర్డినెన్స్‌లు కోర్టులలో సవాలు చేయలేరు",
     "ఆర్డినెన్స్‌లు స్వయంచాలకంగా చట్టమవుతాయి",
     "b",
     "D.C. Wadhwa v. State of Bihar (1987): సుప్రీం కోర్టు — ఆర్డినెన్స్‌లను పదే పదే పునర్జారీ చేయడం (Repromulgation without Parliament's approval) రాజ్యాంగంపై మోసం (fraud on Constitution) అని నిర్ణయించింది. పార్లమెంటరీ ప్రజాస్వామ్య సూత్రాలకు విరుద్ధం.\n(D.C. Wadhwa v. State of Bihar 1987: SC held repromulgation of ordinances without placing before Parliament is a fraud on the Constitution and violates parliamentary democracy.)"),

    (4, 2,
     "రాష్ట్రపతి ఆర్డినెన్స్ యొక్క పరిమితులు ఏమిటి?\n(What are the limitations of President's Ordinance-making power?)",
     "ఏ పరిమితులూ లేవు",
     "రాజ్యాంగ సవరణ చేయలేదు; ప్రాథమిక హక్కులు ఉల్లంఘించే ఆర్డినెన్స్ జారీ చేయలేదు; రాష్ట్ర జాబితా అంశంపై జారీ చేయలేదు\n(Cannot amend Constitution; cannot violate Fundamental Rights; cannot relate to State List subjects)",
     "కేవలం ఆర్థిక సంకటంలో మాత్రమే",
     "మంత్రి మండలి అనుమతి తో మాత్రమే",
     "b",
     "రాష్ట్రపతి ఆర్డినెన్స్ పరిమితులు:\n1) రాజ్యాంగ సవరణ చేయలేరు\n2) ప్రాథమిక హక్కులు (Art.13) ఉల్లంఘించే ఆర్డినెన్స్ జారీ చేయలేరు\n3) రాష్ట్ర జాబితా అంశాలకు వర్తించదు\n4) 7వ షెడ్యూల్ పరిమితులు వర్తిస్తాయి\n(Ordinance limitations: cannot amend Constitution; cannot violate Fundamental Rights; does not extend to State List subjects.)"),

    # ── Section 5: Emergency Powers ───────────────────────────────────────────────
    (5, 1,
     "జాతీయ అత్యవసర పరిస్థితి (National Emergency) ఏ అనుచ్ఛేదం కింద విధించవచ్చు?\n(Under which Article can National Emergency be proclaimed?)",
     "Art.356", "Art.352",
     "Art.360", "Art.365",
     "b",
     "Art.352: జాతీయ అత్యవసర పరిస్థితి — యుద్ధం, బాహ్య దాడి లేదా సాయుధ తిరుగుబాటు కారణంగా. 44వ సవరణ (1978) తర్వాత 'అంతర్గత గందరగోళం' (internal disturbance) తొలగించి 'సాయుధ తిరుగుబాటు' (armed rebellion) చేర్చారు.\n(Art.352: National Emergency — war, external aggression, or armed rebellion. 44th Amendment 1978 replaced 'internal disturbance' with 'armed rebellion'.)"),

    (5, 2,
     "రాష్ట్రపతి పాలన (President's Rule) ఏ అనుచ్ఛేదం కింద విధించవచ్చు?\n(Under which Article can President's Rule be imposed?)",
     "Art.352", "Art.356",
     "Art.360", "Art.355",
     "b",
     "Art.356: రాష్ట్ర రాజ్యాంగ యంత్రాంగం వైఫల్యం (failure of constitutional machinery in a state) కారణంగా రాష్ట్రపతి పాలన విధించవచ్చు. గవర్నర్ నివేదిక లేదా రాష్ట్రపతి అభిమతం ఆధారంగా.\n(Art.356: President's Rule imposed when constitutional machinery in a state fails. Based on Governor's report or President's own satisfaction.)"),

    (5, 2,
     "ఆర్థిక అత్యవసర పరిస్థితి (Financial Emergency) ఏ అనుచ్ఛేదం కింద ఉంటుంది?\n(Under which Article is Financial Emergency declared?)",
     "Art.352", "Art.356",
     "Art.360", "Art.370",
     "c",
     "Art.360: ఆర్థిక అత్యవసర పరిస్థితి — భారత్ ఆర్థిక సుస్థిరత లేదా ప్రతిష్ఠ ప్రమాదంలో పడినప్పుడు. ఇప్పటివరకు ఒక్కసారి కూడా విధించలేదు.\n(Art.360: Financial Emergency — when financial stability or credit of India is threatened. Has never been proclaimed in India's history so far.)"),

    (5, 3,
     "జాతీయ అత్యవసర పరిస్థితి విధించడానికి ముందు మంత్రి మండలి లిఖిత సలహా అవసరమా?\n(Is written advice of Cabinet required before proclaiming National Emergency?)",
     "అవసరం లేదు",
     "అవును — 44వ సవరణ (1978) తర్వాత Cabinet లిఖిత సలహా (written advice) తప్పనిసరి\n(Yes — after 44th Amendment 1978, written advice of Cabinet is mandatory)",
     "ప్రధానమంత్రి సలహా మాత్రమే అవసరం",
     "పార్లమెంట్ ముందే ఆమోదించాలి",
     "b",
     "44వ సవరణ (1978): Art.352 సవరణ ప్రకారం రాష్ట్రపతి జాతీయ అత్యవసర పరిస్థితి విధించడానికి ముందు Cabinet లిఖిత సలహా తప్పనిసరి. ఈ సవరణ ముందు PM సలహా మాత్రమే చాలు. Cabinet = PM + Cabinet Rank Ministers.\n(44th Amendment 1978: President must receive written advice of the Cabinet (not just PM) before proclaiming National Emergency under Art.352.)"),

    (5, 2,
     "జాతీయ అత్యవసర పరిస్థితి పార్లమెంట్ ఆమోదం ఎంత కాలంలో తప్పనిసరి?\n(Within what period must Parliament approve National Emergency?)",
     "30 రోజులు", "1 నెల",
     "2 నెలలు\n(2 months — approval within 1 month of sitting; extended to 2 months by 44th Amendment for non-sitting situations)",
     "6 నెలలు",
     "c",
     "44వ సవరణ తర్వాత: జాతీయ అత్యవసర పరిస్థితి ప్రకటన తర్వాత ఒక నెలలోపు పార్లమెంట్ ఆమోదించాలి. ఆ సమయంలో లోక్‌సభ రద్దు అయి ఉంటే రాజ్యసభ ఆమోదం అవసరం + లోక్‌సభ పునర్నిర్మించిన 30 రోజులలోపు ఆమోదించాలి — మొత్తం 2 నెలలు.\n(After 44th Amendment: National Emergency must be approved by Parliament within 1 month. If LS is dissolved, RS approves and reconstituted LS must approve within 30 days — total max 2 months.)"),

    # ── Section 6: Veto Powers & Discretionary Powers ────────────────────────────
    (6, 2,
     "రాష్ట్రపతి 'Absolute Veto' అంటే ఏమిటి?\n(What is the President's 'Absolute Veto'?)",
     "బిల్లుపై ఓటింగ్ జరగకుండా అడ్డుకోవడం",
     "రాష్ట్రపతి బిల్లుకు ఆమోదం తిరస్కరించడం — బిల్లు రద్దవుతుంది; పార్లమెంట్ ఓర్చుకోలేదు\n(President withholds assent — Bill lapses; cannot be overridden by Parliament)",
     "పార్లమెంట్ ఆమోదించిన బిల్లును తిరిగి పంపించడం",
     "బిల్లుపై సుప్రీం కోర్టు అభిప్రాయం కోరడం",
     "b",
     "Absolute Veto: రాష్ట్రపతి బిల్లుకు ఆమోదం తిరస్కరించడం — ఆ బిల్లు రద్దవుతుంది. సాధారణంగా ప్రైవేట్ మెంబర్ బిల్లులు లేదా మంత్రి మండలి అభిప్రాయానికి వ్యతిరేకంగా ఆమోదించబడిన బిల్లులకు వర్తిస్తుంది.\n(Absolute Veto: President withholds assent — Bill lapses; Parliament cannot override. Typically used for Private Member Bills or Bills opposed by Council of Ministers.)"),

    (6, 2,
     "రాష్ట్రపతి 'Suspensive Veto' అంటే ఏమిటి?\n(What is the President's 'Suspensive Veto'?)",
     "బిల్లుకు ఆమోదం నిరాకరించడం",
     "బిల్లు నిర్ణయం తీసుకోకుండా వదిలేయడం",
     "బిల్లును పునర్విచారణకు పార్లమెంట్‌కు తిరిగి పంపించడం — పార్లమెంట్ మళ్లీ ఆమోదిస్తే తప్పనిసరిగా సంతకం చేయాలి\n(Return Bill for reconsideration — if Parliament passes again, assent is mandatory)",
     "రాజ్యసభకు పంపించడం",
     "c",
     "Suspensive Veto: రాష్ట్రపతి బిల్లును పునర్విచారణకు (Art.111) తిరిగి పంపించవచ్చు. పార్లమెంట్ మళ్లీ ఆమోదిస్తే — సవరణలతో అయినా లేకుండా అయినా — రాష్ట్రపతి తప్పనిసరిగా ఆమోదించాలి. మనీ బిల్లుకు వర్తించదు.\n(Suspensive Veto under Art.111: President returns Bill for reconsideration. If Parliament passes again (with/without amendments), President MUST give assent. Not applicable to Money Bills.)"),

    (6, 3,
     "రాష్ట్రపతి 'విచక్షణాధికారాలు' (Discretionary Powers) ఏ సందర్భాలలో వర్తిస్తాయి?\n(In which situations do the President's Discretionary Powers apply?)",
     "ఎప్పుడూ వర్తించవు — President always follows CoM advice",
     "ప్రధానమంత్రి నియామకం (hung parliament లో), లోక్‌సభ రద్దు అభ్యర్థన తిరస్కరణ, Art.143 రిఫరెన్స్ అడగడం\n(PM appointment in hung parliament, refusing dissolution, Art.143 reference)",
     "కేవలం అత్యవసర పరిస్థితిలో",
     "కేవలం రాజ్యాంగ సవరణలలో",
     "b",
     "రాష్ట్రపతి విచక్షణాధికారాలు:\n1) Hung Parliament లో PM నియామకం (no clear majority)\n2) PM తో సహా CoM లోక్‌సభ విశ్వాసం కోల్పోయిన తర్వాత రద్దు తిరస్కరించవచ్చు\n3) Art.74(1) కింద పునర్విచారణ కోసం బిల్లు తిరిగి పంపించడం\n4) Art.143 కింద SC అభిప్రాయం కోరడం\n(Discretionary powers: (1) Appointment of PM when no clear majority, (2) Refusing dissolution when PM lost confidence, (3) Returning Bill for reconsideration, (4) Seeking SC opinion under Art.143.)"),

    (6, 2,
     "రాజ్యపాల రాష్ట్రపతికి 'నామమాత్రపు అధిపతి' (Nominal Head) అని ఎందుకు అంటారు?\n(Why is the President called a 'Nominal Head' of State?)",
     "రాష్ట్రపతికి అధికారాలు లేవు",
     "Art.74 ప్రకారం మంత్రి మండలి సలహా బాధ్యకరంగా ఉంటుంది — రాష్ట్రపతి రాజ్యాంగపరంగా వ్యవహరించాలి, ప్రత్యక్ష రాజకీయ అధికారం లేదు\n(Art.74 — CoM advice is binding; President acts constitutionally, not politically)",
     "రాష్ట్రపతిని ప్రజలు ఎన్నుకోరు కాబట్టి",
     "రాష్ట్రపతి పార్లమెంట్‌లో ఓటు వేయలేరు కాబట్టి",
     "b",
     "రాష్ట్రపతి రాజ్యాంగ అధిపతి (Constitutional Head) — నామమాత్రపు కార్యనిర్వాహకుడు. Art.74 ప్రకారం మంత్రి మండలి సలహా బాధ్యకరం. బ్రిటన్‌లో 'రాజు పాలిస్తారు, ప్రభుత్వం అధికారం నడుపుతుంది' అన్న సూత్రం వలె.\n(President is a Constitutional/Nominal head — real executive power lies with CoM. Like British convention: 'The King reigns but the Government governs'. Art.74 makes CoM advice binding.)"),

    # ── Section 7: Tough PYQs ─────────────────────────────────────────────────────
    (7, 3,
     "రాష్ట్రపతి ఎన్నిక వివాదం ఏ కోర్టు విచారిస్తుంది?\n(Which court adjudicates disputes relating to the election of the President?)",
     "హైకోర్టు", "ఎన్నికల కమిషన్",
     "సుప్రీం కోర్టు — Art.71\n(Supreme Court — Art.71)",
     "పార్లమెంట్",
     "c",
     "Art.71: రాష్ట్రపతి మరియు ఉపరాష్ట్రపతి ఎన్నికకు సంబంధించిన అన్ని వివాదాలను సుప్రీం కోర్టు విచారిస్తుంది. సుప్రీం కోర్టు నిర్ణయం తుది.\n(Art.71: All doubts and disputes arising out of or in connection with the election of President or VP shall be inquired into and decided by the Supreme Court whose decision shall be final.)",
     'APPSC'),

    (7, 3,
     "రాష్ట్రపతి ఎన్నికలో ఏదైనా స్థానం ఖాళీగా ఉంటే అది ఎన్నికను ప్రభావితం చేస్తుందా?\n(Does a vacancy in the Electoral College affect the validity of Presidential election?)",
     "అవును — ఎన్నిక రద్దవుతుంది",
     "కాదు — ఎలక్టోరల్ కాలేజ్‌లో ఖాళీ ఉన్నా ఎన్నిక చెల్లుబాటవుతుంది — Art.71(4)\n(No — election is not invalid due to vacancy in Electoral College — Art.71(4))",
     "రాష్ట్రపతి నిర్ణయిస్తారు",
     "అవును, కనీసం 90% ఎలక్టోరల్ కాలేజ్ ఉండాలి",
     "b",
     "Art.71(4): ఎలక్టోరల్ కాలేజ్‌లో ఏదైనా ఖాళీ ఉన్నందువల్ల రాష్ట్రపతి ఎన్నిక చెల్లుబాటు లేదని చేయలేరు. ఖాళీ ఉన్నా ఎన్నిక చెల్లుతుంది.\n(Art.71(4): The election of the President shall not be called in question on the ground of the existence of any vacancy in the Electoral College.)"),

    (7, 4,
     "రాష్ట్రపతి జైల్ సింగ్ 'Indian Post Office (Amendment) Bill'పై పాకెట్ వీటో వేశారు — దీని ప్రాధాన్యత ఏమిటి?\n(What is the significance of President Zail Singh's Pocket Veto on the Indian Post Office Amendment Bill?)",
     "రాష్ట్రపతికి బిల్లు తిరిగి పంపించే అధికారం లేదని నిరూపించింది",
     "రాజ్యాంగంలో రాష్ట్రపతి నిర్ణయానికి సమయ పరిమితి లేదు — నిర్ణయం తీసుకోకుండా ఉండటమే Pocket Veto; US లో 10 రోజుల పరిమితి ఉంది\n(No time limit in India — indefinite inaction = Pocket Veto; unlike US where 10 days limit exists)",
     "ఆ బిల్లు స్వయంచాలకంగా రద్దవుతుంది అని నిరూపించింది",
     "ఇది రాజ్యాంగ సవరణ అవసరమని చూపించింది",
     "b",
     "రాష్ట్రపతి జైల్ సింగ్ (1982–87) Indian Post Office (Amendment) Bill 1986పై నిర్ణయం తీసుకోకుండా విడిచారు — ఇది Pocket Veto. భారత రాజ్యాంగం Art.111లో రాష్ట్రపతి నిర్ణయానికి సమయ పరిమితి లేదు కాబట్టి ఇది సాధ్యం.\n(Zail Singh exercised 'Pocket Veto' on the Postal Bill 1986 by taking no action. India's Constitution (Art.111) sets no time limit for Presidential action — unlike the US Constitution which has a 10-day limit.)"),

    (7, 3,
     "రాష్ట్రపతి ఇప్పటివరకు ఎన్నిసార్లు Impeachment ప్రక్రియకు గురయ్యారు?\n(How many times has the President of India faced Impeachment proceedings?)",
     "రెండు సార్లు", "మూడు సార్లు",
     "ఒక్కసారి కూడా — భారత చరిత్రలో రాష్ట్రపతి Impeachment జరగలేదు\n(Never — no President has been impeached in India's history)",
     "ఐదు సార్లు",
     "c",
     "భారత చరిత్రలో ఇప్పటివరకు ఏ రాష్ట్రపతిపైనా Impeachment ప్రక్రియ ప్రారంభించలేదు. Art.61 Impeachment అత్యంత కఠినమైన విధానం — రెండు సభలలో 2/3 మెజారిటీ (మొత్తం సభ్యత్వం) అవసరం.\n(No President of India has ever been impeached. Art.61 Impeachment requires 2/3 of total membership of each House — an extremely difficult threshold.)",
     'APPSC'),

    (7, 3,
     "మొదటిసారి మహిళ రాష్ట్రపతిగా ఎవరు?\n(Who was the first woman President of India?)",
     "ఇందిరా గాంధీ", "సరోజిని నాయుడు",
     "ప్రతిభా పాటిల్ — 2007–2012\n(Pratibha Patil — 2007–2012)",
     "ద్రౌపది ముర్ము",
     "c",
     "ప్రతిభా దేవిసింగ్ పాటిల్ భారత 12వ రాష్ట్రపతి (2007–2012) — భారత మొదటి మహిళా రాష్ట్రపతి. ద్రౌపది ముర్ము 15వ రాష్ట్రపతి (2022– ) — మొదటి గిరిజన మహిళ రాష్ట్రపతి.\n(Pratibha Devisingh Patil — 12th President (2007–2012): First woman President. Droupadi Murmu — 15th President (2022–): First tribal woman President.)",
     'APPSC'),

    (7, 4,
     "రాష్ట్రపతి పదవికి అత్యధిక సార్లు ఎన్నికైన వ్యక్తి ఎవరు?\n(Who has been elected President of India the maximum number of times?)",
     "రాజేంద్ర ప్రసాద్ — రెండు సార్లు\n(Rajendra Prasad — twice)",
     "V.V. గిరి",
     "ఇప్పటివరకు ఒక్కరూ రెండు సార్లు ఎన్నికవలేదు",
     "APJ Abdul Kalam",
     "a",
     "డాక్టర్ రాజేంద్ర ప్రసాద్ భారత మొదటి రాష్ట్రపతి (1950–62) — రెండు సార్లు ఎన్నికయ్యారు. ఇప్పటివరకు రాష్ట్రపతి పదవికి ఒక్కరే రెండు సార్లు ఎన్నికయ్యారు.\n(Dr Rajendra Prasad — India's first President (1950–62) — was elected twice. He is the only person to have been elected President twice.)"),

    (7, 3,
     "రాష్ట్రపతి జమ్మూ-కశ్మీర్‌కు సంబంధించి ఏ ప్రత్యేక ప్రావిజన్ ఉండేది?\n(What special provision related to J&K existed regarding the President?)",
     "J&K రాష్ట్రపతి ఎన్నికలో పాల్గొనలేదు",
     "J&K కు Art.356 వర్తించేది కాదు — బదులుగా Art.356A ఉండేది",
     "J&K రాష్ట్రపతి పాలన విధించడానికి Art.356 కాదు, Art.370 కింద ప్రత్యేక ప్రావిజన్ అవసరమైంది; 2019 తర్వాత Art.370 రద్దుతో ఇప్పుడు Art.356 అమలవుతుంది\n(Pre-2019: Special procedure under Art.370 for J&K President's Rule; post-2019 Art.370 abrogation, Art.356 applies directly)",
     "J&K గవర్నర్‌ను రాష్ట్రపతి నేరుగా నియమించేవారు కాదు",
     "c",
     "J&K విలీనానికి ముందు Art.370 కింద ప్రత్యేక స్థానం ఉండేది — J&K పై రాష్ట్రపతి పాలన విధించడానికి Art.370(1)(c) + Art.356 కాంబినేషన్ అవసరమైంది. 2019 ఆగస్టు 5 న Art.370 రద్దుతో J&K కేంద్రపాలిత ప్రాంతంగా మారింది.\n(Before Aug 2019: J&K had special status under Art.370 requiring a different procedure for President's Rule. After Art.370 abrogation on 5 Aug 2019, J&K became a UT and Art.356 applies directly.)"),

    (7, 4,
     "V.V. గిరి 1969లో రాష్ట్రపతి ఎన్నికలో ఏ పద్ధతిలో గెలిచారు — అది ఎందుకు చారిత్రాత్మకం?\n(How did V.V. Giri win the 1969 Presidential election — why was it historic?)",
     "ఆయన ఏకగ్రీవంగా ఎన్నికయ్యారు",
     "ఆయన రెండవ ప్రాధాన్యతా ఓట్ల (Second Preference Votes) ద్వారా గెలిచారు — STV విజయాన్ని నిర్ణయించింది\n(Won through second preference votes — historic use of STV in practice)",
     "ఆయన స్వతంత్ర అభ్యర్థిగా గెలిచారు — Congress మద్దతు లేకుండా",
     "B మరియు C రెండూ నిజమే",
     "d",
     "V.V. గిరి (1969): స్వతంత్ర అభ్యర్థిగా, అధికారిక Congress అభ్యర్థి నీలం సంజీవ రెడ్డికి వ్యతిరేకంగా నిలబడ్డారు. ఇందిరా గాంధీ 'Conscience vote' పిలుపుతో Congress సభ్యుల మద్దతు గిరికి వెళ్లింది. రెండవ ప్రాధాన్యతా ఓట్ల ద్వారా విజయం — STV ప్రాధాన్యత నిరూపితమైంది.\n(V.V. Giri 1969: Stood as independent against official Congress candidate. Won through second preference votes — demonstrating the importance of STV. Indira Gandhi's 'Conscience vote' call split Congress.)",
     'APPSC'),

    # ── Additional MCQs ───────────────────────────────────────────────────────────
    (0, 3,
     "రాష్ట్రపతి పదవికి 'లాభదాయక పదవి' (Office of Profit) యొక్క నిబంధన ఏమిటి?\n(What is the 'Office of Profit' condition for Presidential candidacy?)",
     "ఏ ప్రభుత్వ ఉద్యోగమైనా నిషేధించబడింది",
     "అభ్యర్థి కేంద్ర, రాష్ట్ర, స్థానిక సంస్థ ప్రభుత్వంలో లాభదాయక పదవిలో ఉండకూడదు; రాష్ట్రపతి, ఉపరాష్ట్రపతి, గవర్నర్, మంత్రి పదవులు మినహాయించబడ్డాయి\n(No office of profit under Union/State/local govt; but President, VP, Governor, Minister are exempted)",
     "కేవలం కేంద్ర ప్రభుత్వ ఉద్యోగాలు మాత్రమే నిషేధం",
     "పదవిలో ఉన్నవారు అభ్యర్థులు కాజాలరు",
     "b",
     "Art.58(2): రాష్ట్రపతి అభ్యర్థి కేంద్ర, రాష్ట్ర, స్థానిక ప్రభుత్వంలో ఎలాంటి లాభదాయక పదవిలోనూ ఉండకూడదు. అయితే రాష్ట్రపతి, ఉపరాష్ట్రపతి, గవర్నర్ పదవులు మరియు కేంద్ర లేదా రాష్ట్ర మంత్రి పదవులు 'Office of Profit' నుండి మినహాయించారు.\n(Art.58(2): No office of profit under Union/State/local body. Exemptions: President, VP, Governor, and Union/State Ministers are not disqualified.)"),

    (2, 2,
     "రాష్ట్రపతి అన్ని కేంద్ర ప్రభుత్వ కార్యకలాపాలు ఎవరి పేరు మీద జరుగుతాయి?\n(In whose name is all business of Government of India conducted?)",
     "ప్రధానమంత్రి పేరు మీద",
     "పార్లమెంట్ పేరు మీద",
     "రాష్ట్రపతి పేరు మీద — Art.77\n(In the name of President — Art.77)",
     "మంత్రి మండలి పేరు మీద",
     "c",
     "Art.77(1): కేంద్ర ప్రభుత్వం యొక్క అన్ని కార్యనిర్వాహక చర్యలు రాష్ట్రపతి పేరు మీద జరుగుతాయి మరియు ఆమోదించబడతాయి.\n(Art.77(1): All executive actions of the Government of India shall be expressed to be taken in the name of the President.)"),

    (3, 3,
     "రాష్ట్రపతి క్షమాభిక్ష అభ్యర్థన తిరస్కరణ న్యాయసమీక్షకు లోబడి ఉంటుందా?\n(Is the rejection of a President's mercy petition subject to judicial review?)",
     "కాదు — రాష్ట్రపతి నిర్ణయం తుది",
     "అవును — Epuru Sudhakar Case (2006) ప్రకారం న్యాయసమీక్ష సాధ్యం; కారణాలు అడగవచ్చు; స్వేచ్ఛాయుత నిర్ణయం కాదు\n(Yes — Epuru Sudhakar 2006: Judicial review possible; arbitrary rejection invalid)",
     "కేవలం మరణ శిక్ష విషయంలో మాత్రమే",
     "హైకోర్టు విచారించవచ్చు",
     "b",
     "Epuru Sudhakar v. State of AP (2006): సుప్రీం కోర్టు — రాష్ట్రపతి/గవర్నర్ క్షమాభిక్ష అభ్యర్థన తిరస్కరణ న్యాయసమీక్షకు లోబడి ఉంటుంది. స్వేచ్ఛాయుతంగా (arbitrarily), రాజకీయ కారణాలతో తిరస్కరించడం చెల్లుబాటు కాదు.\n(Epuru Sudhakar v. State of AP 2006: SC held Presidential/Governor clemency decisions are subject to limited judicial review — arbitrary or politically motivated rejections are invalid.)"),

    (4, 3,
     "ఆర్డినెన్స్‌ను పార్లమెంట్ ముందు ఉంచకుండా వెనక్కి తీసుకోవచ్చా?\n(Can an Ordinance be withdrawn without laying before Parliament?)",
     "కాదు — తప్పనిసరిగా పార్లమెంట్ ముందు ఉంచాలి",
     "అవును — రాష్ట్రపతి ఎప్పుడైనా ఆర్డినెన్స్ వెనక్కి తీసుకోవచ్చు\n(Yes — President can withdraw an Ordinance at any time)",
     "కేవలం మంత్రి మండలి సిఫార్సుతో మాత్రమే",
     "కోర్టు అనుమతి అవసరం",
     "b",
     "Art.123(2): రాష్ట్రపతి ఏ సమయంలోనైనా ఆర్డినెన్స్ వెనక్కి తీసుకోవచ్చు (withdraw). ఆర్డినెన్స్ పార్లమెంట్ ఆమోదం పొందకుండా 6 వారాల తర్వాత స్వయంచాలకంగా రద్దవుతుంది.\n(Art.123(2): President may withdraw an Ordinance at any time. It also ceases to operate 6 weeks after Parliament reassembles or if disapproved by either House.)"),

    (5, 3,
     "జాతీయ అత్యవసర పరిస్థితి ప్రకటనను లోక్‌సభ ఎలా రద్దు చేయగలదు?\n(How can Lok Sabha revoke a National Emergency proclamation?)",
     "2/3 మెజారిటీతో",
     "సాధారణ మెజారిటీతో",
     "లోక్‌సభ మొత్తం సభ్యత్వంలో సాధారణ మెజారిటీతో — 44వ సవరణ తర్వాత LS ప్రత్యేక అధికారం\n(Simple majority of total LS membership — special power under 44th Amendment)",
     "రాజ్యసభ ఆమోదంతో మాత్రమే",
     "c",
     "44వ సవరణ (1978): జాతీయ అత్యవసర పరిస్థితిని రద్దు చేయడానికి లోక్‌సభ ప్రత్యేక అధికారం — మొత్తం సభ్యత్వంలో సాధారణ మెజారిటీ (simple majority of total membership) సరిపోతుంది. రాజ్యసభ ఆమోదం అవసరం లేదు.\n(44th Amendment 1978: LS alone can revoke National Emergency by simple majority of its total membership. No RS approval needed — a special safeguard given to directly elected House.)"),

    (6, 3,
     "రాష్ట్రపతి 'రాజ్యపాల' (President of India) పదవికి 'Dignified Executive' అనే పేరు ఎవరు ఇచ్చారు?\n(Who described the Indian President as a 'Dignified Executive'?)",
     "B.R. అంబేడ్కర్",
     "జవహర్‌లాల్ నెహ్రూ",
     "వాల్టర్ బాగెహాట్ — British రాజ్యాంగ విశ్లేషకుడు; భారత రాజ్యాంగానికి వర్తింపజేశారు\n(Walter Bagehot — British constitutional expert; applied to India's President)",
     "కె.ఎం. మున్షి",
     "c",
     "వాల్టర్ బాగెహాట్ (Walter Bagehot) బ్రిటన్ రాజ్యాంగాన్ని 'Efficient' (Cabinet) మరియు 'Dignified' (Monarch) గా వర్గీకరించారు. భారత రాష్ట్రపతి 'Dignified Executive' — నామమాత్రపు అధిపతి; 'Efficient Executive' = ప్రధానమంత్రి నేతృత్వంలో మంత్రి మండలి.\n(Walter Bagehot classified British constitution as 'Efficient' (Cabinet) and 'Dignified' (Monarch). India's President = 'Dignified'; PM + CoM = 'Efficient' executive.)"),

    (7, 3,
     "మొట్టమొదటి లోక్‌సభ ఎన్నికకు ముందే రాష్ట్రపతి పదవి నిర్వర్తించిన వ్యక్తి ఎవరు — ఎందుకు చారిత్రాత్మకం?\n(Who served as President before the first Lok Sabha elections — and why is it historic?)",
     "C. రాజగోపాలాచారి",
     "రాజేంద్ర ప్రసాద్",
     "రాజగోపాలాచారి తాత్కాలిక రాష్ట్రపతి — రాజేంద్ర ప్రసాద్ రాజ్యాంగ అమలుకు ముందు రాష్ట్రపతి\n(Rajagopalachari was interim; Rajendra Prasad was first elected President upon Constitution's commencement)",
     "భీమ్ రావ్ అంబేడ్కర్",
     "c",
     "C. రాజగోపాలాచారి 1948–50 వరకు భారత్ గవర్నర్ జనరల్. 1950 జనవరి 26 న రాజ్యాంగం అమలులోకి రావడంతో రాజేంద్ర ప్రసాద్ మొదటి రాష్ట్రపతిగా ఎన్నికయ్యారు (రాజ్యాంగ అసెంబ్లీ ఎన్నికల ద్వారా). 1952లో మొదటి సార్వత్రిక ఎన్నికలు జరిగాయి.\n(Rajagopalachari was last Governor-General. Dr Rajendra Prasad became first President on 26 Jan 1950 when Constitution commenced, elected by Constituent Assembly. First general elections were in 1952.)"),

    # ── Additional MCQs — filling to ~70 ─────────────────────────────────────────

    (0, 2,
     "రాష్ట్రపతి పదవికి నిర్ణీత పదవీ కాలానికి ముందే రాజీనామా చేయవచ్చా?\n(Can the President resign before the completion of term?)",
     "కాదు — 5 సంవత్సరాలు పూర్తి చేయాలి",
     "అవును — ఉపరాష్ట్రపతికి లిఖిత పూర్వకంగా రాజీనామా ఇవ్వాలి — Art.56(1)(a)\n(Yes — resignation must be addressed to the Vice President — Art.56(1)(a))",
     "లోక్‌సభ స్పీకర్‌కు రాజీనామా ఇవ్వాలి",
     "ప్రధానమంత్రికి రాజీనామా ఇవ్వాలి",
     "b",
     "Art.56(1)(a): రాష్ట్రపతి తన చేతి రాత రాజీనామా లేఖ ఉపరాష్ట్రపతికి ఇవ్వడం ద్వారా రాజీనామా చేయవచ్చు. ఉపరాష్ట్రపతి దీన్ని లోక్‌సభ స్పీకర్‌కు తెలియజేస్తారు.\n(Art.56(1)(a): President may resign by writing under hand addressed to the Vice President, who shall forthwith communicate it to the Speaker of Lok Sabha.)"),

    (0, 2,
     "రాష్ట్రపతి పదవీ కాలం ముగిసినా తర్వాత ఉత్తరాధికారి బాధ్యతలు తీసుకోకపోతే ఏమవుతుంది?\n(If a successor has not assumed office after President's term ends, what happens?)",
     "రాష్ట్రపతి పదవి ఖాళీ అవుతుంది",
     "ప్రధానమంత్రి రాష్ట్రపతి బాధ్యతలు తీసుకుంటారు",
     "మునుపటి రాష్ట్రపతి ఉత్తరాధికారి బాధ్యతలు తీసుకునే వరకు కొనసాగుతారు — Art.56(1)(c)\n(Previous President continues until successor assumes charge — Art.56(1)(c))",
     "సుప్రీం కోర్టు ప్రధాన న్యాయమూర్తి బాధ్యతలు తీసుకుంటారు",
     "c",
     "Art.56(1)(c): పదవీ కాలం ముగిసినా ఉత్తరాధికారి బాధ్యతలు తీసుకోకపోతే మునుపటి రాష్ట్రపతి పదవిలో కొనసాగుతారు. ఇది నిరంతర పాలన నిర్ధారిస్తుంది.\n(Art.56(1)(c): If no successor has assumed office at the expiry of term, the outgoing President continues until a successor enters office — ensures continuity.)"),

    (1, 3,
     "రాష్ట్రపతి Impeachmentకు 'రాజ్యాంగ ఉల్లంఘన' నిర్వచించబడిందా?\n(Is 'violation of Constitution' for Presidential Impeachment defined in the Constitution?)",
     "అవును, స్పష్టంగా నిర్వచించారు",
     "కాదు — రాజ్యాంగంలో 'violation of Constitution' నిర్వచించబడలేదు; పార్లమెంట్ నిర్ణయిస్తుంది\n(No — Constitution does not define 'violation'; Parliament decides)",
     "సుప్రీం కోర్టు నిర్వచిస్తుంది",
     "ఎన్నికల కమిషన్ నిర్వచిస్తుంది",
     "b",
     "రాజ్యాంగంలో 'violation of Constitution' అంటే ఏమిటో నిర్వచించలేదు. ఇది అస్పష్టంగా వదిలారు — పార్లమెంట్ ఈ పదాన్ని నిర్వచించే అధికారం కలిగి ఉంది. ఇది Impeachment ను అత్యంత కఠినం చేస్తుంది.\n(The Constitution does not define 'violation of Constitution' — it is left undefined. Parliament has the power to interpret it. This makes Impeachment a very difficult process.)"),

    (2, 2,
     "Art.78 ప్రకారం ప్రధానమంత్రి రాష్ట్రపతికి ఏ విధులు నిర్వర్తించాలి?\n(What duties must the PM perform towards the President under Art.78?)",
     "బడ్జెట్ ముసాయిదా పంపించడం",
     "మంత్రి మండలి అన్ని నిర్ణయాలు, శాసన ప్రతిపాదనలు తెలపాలి; రాష్ట్రపతి అడిగిన అంశాలపై సమాచారం ఇవ్వాలి\n(PM must communicate all CoM decisions and legislative proposals; provide information as required by President)",
     "రాజ్యసభ సభ్యులు నామినేట్ చేయడానికి సలహా ఇవ్వడం",
     "శాసనసభ ఎన్నికల షెడ్యూల్ పంపించడం",
     "b",
     "Art.78: PM యొక్క బాధ్యతలు: (a) మంత్రి మండలి అన్ని నిర్ణయాలు, శాసన ప్రతిపాదనలు రాష్ట్రపతికి తెలపాలి; (b) రాష్ట్రపతి అభ్యర్థిస్తే కేంద్ర పాలన మరియు శాసన ప్రతిపాదనలకు సంబంధించిన సమాచారం ఇవ్వాలి.\n(Art.78: PM's duties — (a) communicate all CoM decisions and legislative proposals to President; (b) if required, furnish information relating to administration of Union and legislative proposals.)"),

    (2, 3,
     "రాష్ట్రపతి 'Pocket Veto' వర్తించే పరిస్థితులు ఏవి?\n(In what situations can the President exercise 'Pocket Veto'?)",
     "అన్ని బిల్లులకు",
     "కేవలం రాష్ట్ర బిల్లులకు",
     "ప్రధానంగా ప్రైవేట్ మెంబర్ బిల్లులకు మరియు మంత్రి మండలి కోల్పోయిన తర్వాత ప్రభుత్వం ఆమోదించిన బిల్లులకు — Art.111 లో సమయ పరిమితి లేదు\n(Private Member Bills and bills passed after CoM's defeat — Art.111 has no time limit)",
     "ఏ బిల్లుకూ వర్తించదు",
     "c",
     "Pocket Veto: Art.111 లో రాష్ట్రపతి నిర్ణయానికి సమయ పరిమితి లేదు కాబట్టి సాధ్యం. US లో 10 రోజుల పరిమితి ఉంది. Pocket Veto ప్రధానంగా ప్రైవేట్ మెంబర్ బిల్లులకు మరియు పడిపోయిన ప్రభుత్వం ఆమోదించిన బిల్లులకు వర్తిస్తుంది.\n(Pocket Veto is possible because Art.111 sets no time limit — unlike US (10 days). Typically used for Private Member Bills or bills passed by a fallen government.)"),

    (3, 2,
     "కేంద్ర ప్రభుత్వ చట్టాల కింద కాకుండా రాష్ట్ర చట్టాల కింద శిక్ష అనుభవిస్తే — క్షమాభిక్ష ఎవరికి దరఖాస్తు చేయాలి?\n(For punishment under State law — who grants clemency?)",
     "రాష్ట్రపతి (Art.72)",
     "సుప్రీం కోర్టు",
     "గవర్నర్ (Art.161) — రాష్ట్ర చట్టాల కింద శిక్షలపై గవర్నర్ క్షమాభిక్ష ఇవ్వగలరు\n(Governor — Art.161 — grants clemency for punishments under State laws)",
     "హైకోర్టు",
     "c",
     "Art.161: గవర్నర్ రాష్ట్ర చట్టాల కింద శిక్షలను క్షమించవచ్చు. Art.72: రాష్ట్రపతి కేంద్ర చట్టాల కింద, కోర్ట్ మార్షల్, మరణ శిక్షలు క్షమించగలరు. మరణ శిక్ష విషయంలో గవర్నర్‌కు అధికారం లేదు.\n(Art.161: Governor can grant clemency for offences under State law. Art.72: President for Union law, court-martial, death sentences. Governor CANNOT pardon death sentences.)"),

    (4, 2,
     "గవర్నర్ ఆర్డినెన్స్ అధికారం ఏ అనుచ్ఛేదం కింద ఉంటుంది?\n(Under which Article does the Governor have Ordinance-making power?)",
     "Art.123", "Art.213",
     "Art.200", "Art.167",
     "b",
     "Art.213: రాష్ట్ర గవర్నర్ ఆర్డినెన్స్ జారీ చేయగలరు — రాష్ట్ర శాసనసభ సమావేశంలో లేనప్పుడు. Art.123 కేంద్రానికి (రాష్ట్రపతి), Art.213 రాష్ట్రానికి (గవర్నర్) వర్తిస్తుంది.\n(Art.213: Governor's Ordinance-making power — parallel to President's Art.123 for the Union. Art.123 = Centre; Art.213 = State.)"),

    (5, 3,
     "జాతీయ అత్యవసర పరిస్థితి అమలులో ఉండగా రాష్ట్రాల అధికారాలపై ఏ ప్రభావం ఉంటుంది?\n(What happens to State powers during National Emergency?)",
     "రాష్ట్రాలు పూర్తిగా రద్దవుతాయి",
     "పార్లమెంట్ రాష్ట్ర జాబితా అంశాలపై చట్టాలు చేయగలదు; కేంద్రం రాష్ట్రాలకు కార్యనిర్వాహక ఆదేశాలు ఇవ్వగలదు\n(Parliament can legislate on State List; Centre can direct states on executive matters)",
     "రాష్ట్రాల అధికారాలపై ఎటువంటి ప్రభావం ఉండదు",
     "గవర్నర్లు రద్దవుతారు",
     "b",
     "జాతీయ అత్యవసర పరిస్థితి (Art.352) అమలులో:\n• Art.353(a): పార్లమెంట్ రాష్ట్ర జాబితా అంశాలపై చట్టాలు చేయగలదు\n• Art.353(b): కేంద్రం రాష్ట్రాలకు కార్యనిర్వాహక ఆదేశాలు ఇవ్వగలదు\n• Art.354: ఆర్థిక సంబంధాలు మారవచ్చు\n(During National Emergency: Art.353(a) — Parliament can legislate on State List; Art.353(b) — Centre can give executive directions to states; Art.354 — financial relations may change.)"),

    (5, 2,
     "రాష్ట్రపతి పాలన (Art.356) గరిష్ట కాలం ఎంత?\n(What is the maximum duration of President's Rule under Art.356?)",
     "6 నెలలు", "1 సంవత్సరం",
     "3 సంవత్సరాలు\n(3 years — 6 months initial + extensions with Parliamentary approval)",
     "5 సంవత్సరాలు",
     "c",
     "Art.356 రాష్ట్రపతి పాలన:\n• మొదట 6 నెలలు\n• పార్లమెంట్ ఆమోదంతో 6-6 నెలలు పొడిగించవచ్చు\n• గరిష్ట కాలం 3 సంవత్సరాలు (44వ సవరణ తర్వాత: జాతీయ అత్యవసర పరిస్థితి అమలులో ఉంటే 3+ సంవత్సరాలు సాధ్యం)\n(Art.356: Initially 6 months; extended by 6 months each time with Parliamentary approval; maximum 3 years. Beyond 1 year only if National Emergency is in operation or EC certifies polls cannot be held.)"),

    (6, 3,
     "రాష్ట్రపతి 'Pocket Veto' మరియు 'Absolute Veto' మధ్య తేడా ఏమిటి?\n(What is the difference between 'Pocket Veto' and 'Absolute Veto'?)",
     "రెండూ ఒకటే",
     "Absolute Veto: రాష్ట్రపతి స్పష్టంగా ఆమోదం నిరాకరిస్తారు; Pocket Veto: రాష్ట్రపతి ఏ నిర్ణయమూ తీసుకోకుండా నిరవధికంగా వదిలేస్తారు\n(Absolute Veto: explicit refusal; Pocket Veto: indefinite inaction — no decision taken)",
     "Pocket Veto పార్లమెంట్ ఓర్చుకోగలదు",
     "Absolute Veto అర్థం రాజ్యాంగ సవరణకు",
     "b",
     "Absolute Veto: రాష్ట్రపతి స్పష్టంగా ఆమోదం నిరాకరిస్తారు — బిల్లు రద్దవుతుంది. Pocket Veto: రాష్ట్రపతి ఏ నిర్ణయమూ తీసుకోకుండా వదిలేస్తారు — సమయ పరిమితి లేదు కాబట్టి. రెండింటిలోనూ పార్లమెంట్ ఓర్చుకోలేదు.\n(Absolute Veto: President explicitly refuses assent — Bill lapses. Pocket Veto: President takes no action indefinitely — possible because Art.111 has no time limit. Neither can be overridden by Parliament.)"),

    (7, 3,
     "రాష్ట్రపతి పదవికి సంబంధించి Art.59 ఏమి నిర్ణయిస్తుంది?\n(What does Art.59 specify about the President's conditions of office?)",
     "రాష్ట్రపతి పదవీ కాలం",
     "రాష్ట్రపతి వేతనాలు మరియు అనుభవాలు",
     "రాష్ట్రపతి పార్లమెంట్ లేదా రాష్ట్ర శాసనసభ సభ్యుడు కాజాలరు; లాభదాయక పదవి ఉండకూడదు; నివాసం ఉచితంగా లభిస్తుంది; వేతనం-అలవెన్సులు పార్లమెంట్ నిర్ణయిస్తుంది; ఇవి సేవా కాలంలో తగ్గించకూడదు\n(Art.59: Cannot be member of Parliament/State legislature; no office of profit; official residence provided free; emoluments/allowances fixed by Parliament and not reducible)",
     "రాష్ట్రపతి ఎన్నిక విధానం",
     "c",
     "Art.59: రాష్ట్రపతి పదవికి నిబంధనలు — పార్లమెంట్/రాష్ట్ర శాసనసభ సభ్యుడు కాజాలరు; ఎటువంటి లాభదాయక పదవి పట్టుకోకూడదు; అధికారిక నివాసం (రాష్ట్రపతి భవన్) ఉచితం; వేతనాలు పార్లమెంట్ నిర్ణయిస్తుంది — సేవా కాలంలో తగ్గించకూడదు.\n(Art.59: President cannot hold membership of Parliament/State legislature; no office of profit; official residence free; emoluments fixed by Parliament and cannot be reduced during tenure.)"),

    (7, 4,
     "రాష్ట్రపతి 'Immunity from legal proceedings' ఏ అనుచ్ఛేదం కింద ఉంటుంది?\n(Under which Article does the President have immunity from legal proceedings?)",
     "Art.71", "Art.58",
     "Art.361\n(Art.361 — President's immunity)",
     "Art.74",
     "c",
     "Art.361: రాష్ట్రపతి (మరియు గవర్నర్) పదవిలో ఉన్నంత కాలం — అధికారిక చర్యలకు కోర్టులో జవాబు చెప్పక్కర్లేదు; క్రిమినల్ ప్రొసీడింగ్స్ ప్రారంభించలేరు; అరెస్టు లేదా జైలు ఉండదు. పదవీ కాలం ముగిశాక వ్యక్తిగత చర్యలకు జవాబుదారీ.\n(Art.361: President (and Governors) — not answerable to any court for official acts; no criminal proceedings during tenure; no arrest or imprisonment. Civil proceedings for personal acts need 2 months notice.)",
     'APPSC'),

    (0, 3,
     "70వ రాజ్యాంగ సవరణ (1992) రాష్ట్రపతి ఎన్నికను ఎలా ప్రభావితం చేసింది?\n(How did the 70th Constitutional Amendment 1992 affect the Presidential election?)",
     "వోటు విలువ మారింది",
     "ఢిల్లీ మరియు పుదుచ్చేరి శాసనసభ సభ్యులకు ఎలక్టోరల్ కాలేజ్‌లో చేర్పు కల్పించారు\n(Delhi and Puducherry legislative assembly members included in Electoral College)",
     "నేరుగా ప్రజలు ఓటు వేయడం మొదలైంది",
     "రాజ్యసభ నామినేటెడ్ సభ్యులను చేర్చారు",
     "b",
     "70వ రాజ్యాంగ సవరణ (1992): Art.54 సవరణ ద్వారా జాతీయ రాజధాని ప్రాంతం ఢిల్లీ మరియు పుదుచ్చేరి కేంద్రపాలిత ప్రాంతాల శాసనసభ సభ్యులను రాష్ట్రపతి ఎలక్టోరల్ కాలేజ్‌లో చేర్చారు.\n(70th Constitutional Amendment 1992: Amended Art.54 to include elected members of Legislative Assemblies of Delhi (NCT) and Puducherry in the Presidential Electoral College.)"),

]


# ─────────────────────────────────────────────────────────────
def _seed_polity_ch15_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    """Insert Chapter 15 study note row (idempotent)."""
    existing = db_exec_fn(conn,
        "SELECT id FROM study_notes WHERE topic='Indian_Polity' AND chapter_num=15"
    ).fetchone()
    if existing and not force:
        return

    sections_json = _json.dumps(POLITY_CH15_SECTIONS, ensure_ascii=False)
    ph = '%s' if use_postgres else '?'

    if existing and force:
        db_exec_fn(conn,
            f"UPDATE study_notes SET sections_json={ph}, chapter_title_en={ph}, chapter_title_te={ph} "
            f"WHERE topic='Indian_Polity' AND chapter_num=15",
            (sections_json,
             "President of India",
             "భారత రాష్ట్రపతి")
        )
        return

    db_exec_fn(conn,
        f"""INSERT INTO study_notes
            (subject, topic, subtopic, chapter_num,
             chapter_title_te, chapter_title_en, pages_ref, sections_json)
            VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
        ('GK', 'Indian_Polity', 'Lakshmikanth', 15,
         'భారత రాష్ట్రపతి',
         'President of India',
         'Ch.15',
         sections_json)
    )


def _seed_polity_ch15_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
    """Insert Chapter 15 MCQs (skip if already present)."""
    note_row = db_exec_fn(conn,
        "SELECT id FROM study_notes WHERE topic='Indian_Polity' AND chapter_num=15"
    ).fetchone()
    if not note_row:
        return
    note_id = row_to_dict_fn(note_row)['id']

    already = db_exec_fn(conn,
        "SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id=?", (note_id,)
    ).fetchone()
    if already and list(already)[0] > 0:
        return

    diff_map = {"easy": 1, "medium": 2, "hard": 3, "toughest": 4,
                1: 1, 2: 2, 3: 3, 4: 4}

    ph = '%s' if use_postgres else '?'
    for row in POLITY_CH15_MCQS:
        sec_idx, diff_raw, q, a, b, c, d, correct, explanation = row[:9]
        exam_type = row[9] if len(row) > 9 else 'General'
        diff_int = diff_map.get(diff_raw, 2)
        db_exec_fn(conn,
            f"""INSERT INTO chapter_mcqs
                (study_note_id, section_idx, difficulty, exam_type,
                 q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te)
                VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
            (note_id, sec_idx, diff_int, exam_type,
             q, a, b, c, d, str(correct).lower(), explanation)
        )
