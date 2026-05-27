# seed_polity_ch3.py
# Chapter 3: Salient Features & Concept of the Constitution
# (రాజ్యాంగం యొక్క భావన, ప్రముఖ లక్షణాలు)
# Standard : APPSC Group 2 | Source: Lakshmikanth Indian Polity
# Total Sections: 11 | Total MCQs: 92 | PYQs: 12
# Difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
# PYQ: 10th element (index 9) = 'APPSC' or 'UPSC'
# ─────────────────────────────────────────────

import json as _json

POLITY_CH3_SECTIONS = [
    {
        "title": "3.1 విశాలత మరియు మూలాలు — పరిచయం",
        "sub": "Longest Written Constitution · 395 Articles · GoI Act 1935",
        "audio": """భారత రాజ్యాంగం ప్రపంచంలోనే అతిపెద్ద లిఖిత రాజ్యాంగం (Largest Written Constitution in the World).

అసలు రాజ్యాంగం (1949):
• 395 ఆర్టికల్స్ (Articles)
• 22 భాగాలు (Parts)
• 8 షెడ్యూల్స్ (Schedules)

ప్రస్తుత రాజ్యాంగం (సవరణల తర్వాత):
• దాదాపు 448 ఆర్టికల్స్
• 25 భాగాలు
• 12 షెడ్యూల్స్

ఏకైక అతిపెద్ద స్రోతం (Single Biggest Source):
• Government of India Act 1935 — దాదాపు 250 నిబంధనలు భారత రాజ్యాంగంలో చేర్చారు.

ఇది పెద్దగా ఎందుకు?
• భారతదేశం వైవిధ్యం — భాష, సంస్కృతి, మతం
• పాలనా అనుభవం నుండి నేర్చుకున్నారు
• USA, UK, కెనడా, ఆస్ట్రేలియా మొదలైన దేశాల రాజ్యాంగాల నుండి మంచి అంశాలు తీసుకున్నారు"""
    },
    {
        "title": "3.2 వివిధ దేశాల స్రోతాలు",
        "sub": "UK · USA · Ireland · Canada · Australia · Germany · France",
        "audio": """భారత రాజ్యాంగం వివిధ దేశాల రాజ్యాంగాల నుండి స్వీకరించిన అంశాలు:

🇬🇧 బ్రిటన్ (UK) నుండి:
• పార్లమెంటరీ పాలన విధానం
• Rule of Law
• Cabinet System (మంత్రి మండలి)
• Single Citizenship (ఒకే పౌరసత్వం)
• Bicameralism (ద్విసభా పద్ధతి)
• Speaker — విధులు, అధికారాలు

🇺🇸 అమెరికా (USA) నుండి:
• మూల హక్కులు (Fundamental Rights)
• న్యాయ సమీక్ష (Judicial Review)
• స్వతంత్ర న్యాయవ్యవస్థ (Independent Judiciary)
• రాష్ట్రపతిపై అభిశంసన (Impeachment of President)
• ఉపరాష్ట్రపతి పదవి

🍀 ఐర్లాండ్ (Ireland) నుండి:
• ఆదేశిక సూత్రాలు (DPSP — Directive Principles of State Policy)
• రాజ్యసభకు సభ్యుల నామినేషన్ పద్ధతి
• రాష్ట్రపతి ఎన్నిక పద్ధతి

🍁 కెనడా (Canada) నుండి:
• సమాఖ్య వ్యవస్థ + కేంద్రం బలంగా ఉండడం
• అవశేష అధికారాలు కేంద్రానికి
• గవర్నర్ నియామకం కేంద్రం చేయడం

🦘 ఆస్ట్రేలియా (Australia) నుండి:
• Concurrent List (ఉమ్మడి జాబితా)
• పార్లమెంట్ ఉభయ సభల సంయుక్త సమావేశం (Joint Sitting)

🇩🇪 జర్మనీ (Germany — Weimar) నుండి:
• అత్యవసర పరిస్థితిలో మూల హక్కుల నిలిపివేత

🇫🇷 ఫ్రాన్స్ (France) నుండి:
• గణతంత్రం (Republic) భావన
• స్వేచ్ఛ, సమానత్వం, సోదరభావం (Liberty, Equality, Fraternity)

🇿🇦 దక్షిణాఫ్రికా (South Africa) నుండి:
• రాజ్యాంగ సవరణ విధానం
• రాజ్యసభ సభ్యుల ఎన్నిక విధానం

🇯🇵 జపాన్ (Japan) నుండి:
• చట్టం ద్వారా నిర్ణయించిన పద్ధతి (Procedure Established by Law)

🇷🇺 సోవియట్ యూనియన్ (USSR) నుండి:
• మౌలిక విధులు (Fundamental Duties)
• న్యాయం — సామాజిక, ఆర్థిక, రాజకీయ (Preamble Ideals)"""
    },
    {
        "title": "3.3 సమాఖ్య వ్యవస్థ — కేంద్ర పక్షపాతంతో",
        "sub": "Federal Features · Unitary Features · Quasi-Federal",
        "audio": """భారతదేశం: సమాఖ్య వ్యవస్థ + కేంద్ర పక్షపాతం (Federal System with Strong Centre / Quasi-Federal)

సమాఖ్య లక్షణాలు (Federal Features):
1. లిఖిత రాజ్యాంగం — Written Constitution
2. అధికారాల విభజన — Three lists (Union, State, Concurrent)
3. స్వతంత్ర న్యాయవ్యవస్థ
4. ద్విసభా పార్లమెంట్ (Lok Sabha + Rajya Sabha)
5. రాజ్యాంగ సర్వోన్నతత (Constitutional Supremacy)

ఏకీకృత / కేంద్రాభిముఖ లక్షణాలు (Unitary Features):
1. ఒకే రాజ్యాంగం (కేంద్రం + రాష్ట్రాలు ఒకే రాజ్యాంగంలో)
2. ఒకే పౌరసత్వం (Single Citizenship)
3. అవశేష అధికారాలు కేంద్రానికి (Residuary Powers with Union)
4. గవర్నర్ నియామకం కేంద్రం చేస్తుంది
5. అఖిల భారత సేవలు (All India Services)
6. ఏకీకృత న్యాయవ్యవస్థ (Integrated Judiciary)
7. అత్యవసరంలో రాష్ట్ర రాజ్యాంగం నిలిపివేత

K.C. Wheare భారతదేశాన్ని: "Quasi-Federal" లేదా "Federal in form, Unitary in spirit" అన్నారు."""
    },
    {
        "title": "3.4 పార్లమెంటరీ పాలన విధానం",
        "sub": "Westminster Model · Nominal Head · Real Executive",
        "audio": """భారత్ పార్లమెంటరీ పాలన విధానం — UK Westminster Model ఆధారంగా.

ముఖ్య లక్షణాలు:
• రాష్ట్రపతి — నామమాత్రపు అధినేత (Nominal/Constitutional Head)
• ప్రధానమంత్రి — నిజమైన కార్యనిర్వాహకుడు (Real Executive)
• మంత్రి మండలి లోక్ సభకు సమష్టిగా బాధ్యత వహిస్తుంది (Collective Responsibility)
• మంత్రులు పార్లమెంట్ సభ్యులు (No Separation of Powers between Legislature & Executive)
• ప్రధానమంత్రి — మెజారిటీ పార్టీ నాయకుడు
• అవిశ్వాస తీర్మానం ద్వారా ప్రభుత్వాన్ని తొలగించవచ్చు

పార్లమెంటరీ vs అధ్యక్ష పద్ధతి:
• పార్లమెంటరీ: UK, India, Canada, Australia, Japan
• అధ్యక్ష పద్ధతి (Presidential): USA, Brazil, France (Semi-Presidential)

భారత్ ఎందుకు పార్లమెంటరీ ఎంచుకుంది?
• బ్రిటిష్ పాలనలో పరిచయం ఉంది
• బాధ్యత (Accountability) మరియు స్థిరత్వం (Stability) రెండూ ఉంటాయి
• విభిన్న సమాజానికి అనుకూలం"""
    },
    {
        "title": "3.5 మూల హక్కులు మరియు ఆదేశిక సూత్రాలు",
        "sub": "Fundamental Rights Part III · DPSP Part IV · Key Distinctions",
        "audio": """మూల హక్కులు (Fundamental Rights — FR):
• భాగం III (Part III), ఆర్టికల్ 12–35
• స్రోతం: USA రాజ్యాంగం
• లక్షణం: న్యాయస్థానాల్లో అమలు చేయించుకోవచ్చు (Justiciable)
• ప్రధానంగా రాజ్య (State) ప్రవర్తనపై పరిమితులు

ఆదేశిక సూత్రాలు (Directive Principles of State Policy — DPSP):
• భాగం IV (Part IV), ఆర్టికల్ 36–51
• స్రోతం: ఐర్లాండ్ రాజ్యాంగం
• లక్షణం: న్యాయస్థానాల్లో అమలు చేయించుకోలేరు (Non-Justiciable)
• కానీ పాలనలో మూలభూతం (Fundamental in Governance)

తేడా:
• FR = ప్రతికూల (Negative) — రాజ్యాన్ని నిరోధించే హక్కులు
• DPSP = సానుకూల (Positive) — రాజ్యం చేయవలసిన విషయాలు

మూల హక్కులు ఆర్టికల్ 13 ప్రకారం రాజ్య నిర్మించే చట్టాలకు తాకట్టుగా పనిచేస్తాయి.

గ్రాన్విల్ ఆస్టిన్ FR మరియు DPSP ను "రాజ్యాంగంలో ఆత్మ" అన్నారు. ఒకటి లేకుండా మరొకటి అసంపూర్ణం."""
    },
    {
        "title": "3.6 మౌలిక విధులు (Bilingual)",
        "sub": "Fundamental Duties · 42nd Amendment 1976 · 86th Amendment 2002",
        "audio": """మౌలిక విధులు (Fundamental Duties) — ఆర్టికల్ 51A:
• స్రోతం: సోవియట్ యూనియన్ (USSR) రాజ్యాంగం
• స్వరణ్ సింగ్ కమిటీ సిఫారసుపై చేర్చారు

📅 42వ రాజ్యాంగ సవరణ 1976:
• మొదట 10 మౌలిక విధులు చేర్చారు

📅 86వ రాజ్యాంగ సవరణ 2002:
• 11వ విధి చేర్చారు: 6–14 సంవత్సరాల పిల్లలకు విద్యా అవకాశం కల్పించడం
  (Parents/Guardian duty to provide education to children aged 6–14)

ప్రస్తుతం మొత్తం: 11 మౌలిక విధులు

ముఖ్య విధుల్లో కొన్ని:
1. రాజ్యాంగాన్ని గౌరవించడం
2. జాతీయ పతాకం, జాతీయ గీతాన్ని గౌరవించడం
3. దేశ సార్వభౌమత్వాన్ని కాపాడడం
4. శాస్త్రీయ దృష్టి పెంపొందించడం
5. ప్రజా ఆస్తిని కాపాడడం

గమనిక: మౌలిక విధులు Non-Justiciable (న్యాయస్థానాల్లో అమలు చేయించుకోలేరు).
అయితే వాటిని ఉల్లంఘిస్తే శిక్ష విధించే చట్టాలు రూపొందించవచ్చు."""
    },
    {
        "title": "3.7 లౌకిక రాజ్యం మరియు వయోజన ఓటు హక్కు (Bilingual)",
        "sub": "Secular State · Universal Adult Franchise · 61st Amendment 1989",
        "audio": """లౌకిక రాజ్యం (Secular State):
• భారత్ అన్ని మతాలను సమానంగా గౌరవిస్తుంది
• ప్రభుత్వానికి అధికారిక మతం లేదు
• 42వ రాజ్యాంగ సవరణ 1976: ప్రస్తావనకు (Preamble) 'Secular' పదం చేర్చారు

సార్వత్రిక వయోజన ఓటు హక్కు (Universal Adult Franchise):
• 18+ సంవత్సరాల పౌరులందరికీ ఓటు హక్కు
• మూలంలో: 21 సంవత్సరాలు ఉండేది
• 61వ రాజ్యాంగ సవరణ 1989: ఓటు హక్కు వయస్సు 21 నుండి 18 కి తగ్గించారు

ఒకే పౌరసత్వం (Single Citizenship):
• భారత పౌరులందరూ ఒకే జాతీయ పౌరత్వం — రాష్ట్ర పౌరత్వం లేదు
• USA కి భిన్నంగా (USA లో dual citizenship ఉంది — Federal + State)

స్వతంత్ర సంస్థలు (Independent Bodies):
• ఎన్నికల సంఘం (Election Commission — Art 324)
• కాగ్ (CAG — Comptroller and Auditor General — Art 148)
• UPSC (Union Public Service Commission — Art 315)
• ఫైనాన్స్ కమిషన్ (Finance Commission — Art 280)"""
    },
    {
        "title": "3.8 అత్యవసర నిబంధనలు మరియు ఇతర లక్షణాలు (Bilingual)",
        "sub": "3 Types of Emergency · Three-tier Govt · Co-operative Societies",
        "audio": """అత్యవసర నిబంధనలు (Emergency Provisions):

మూడు రకాల అత్యవసర పరిస్థితులు:
1. జాతీయ అత్యవసర పరిస్థితి (National Emergency — Article 352)
   • యుద్ధం, బాహ్య దాడి, సాయుధ తిరుగుబాటు

2. రాష్ట్ర అత్యవసర పరిస్థితి / రాష్ట్రపతి పాలన (President's Rule — Article 356)
   • రాష్ట్రంలో రాజ్యాంగ యంత్రాంగం విఫలమైతే

3. ఆర్థిక అత్యవసర పరిస్థితి (Financial Emergency — Article 360)
   • భారతదేశ ఆర్థిక స్థిరత్వం ప్రమాదంలో పడినప్పుడు

స్రోతం: జర్మనీ (Weimar Constitution) — అత్యవసరంలో FR నిలిపివేత

త్రిస్థాయి పాలన (Three-tier Government):
• 73వ సవరణ 1992 → పంచాయతీ రాజ్ (గ్రామీణ స్వపాలన)
• 74వ సవరణ 1992 → పురపాలక సంఘాలు (పట్టణ స్వపాలన)

సహకార సంఘాలు (Co-operative Societies):
• 97వ రాజ్యాంగ సవరణ 2011 — Part IX-B (Articles 243ZH–243ZT) చేర్చారు

పూర్తిగా మరియు పాక్షికంగా అనమ్య రాజ్యాంగం (Partly Rigid, Partly Flexible):
• కొన్ని ఆర్టికల్స్ — పార్లమెంట్ సాధారణ మెజారిటీతో మార్చవచ్చు
• కొన్ని — ప్రత్యేక మెజారిటీ + రాష్ట్రాల ఆమోదం అవసరం"""
    },
    {
        "title": "3.9 సినిమాటిక్ కథ — రాజ్యాంగ లక్షణాలు",
        "sub": "Full Chapter Story · Sources · Features · Salient",
        "audio": """అంబేడ్కర్ CA లో చెప్పారు: "ఈ రాజ్యాంగం మంచి చేతుల్లో ఉంటే మంచి పని చేస్తుంది. చెడు చేతుల్లో ఉంటే దాన్ని రక్షించే శక్తి ఏ రాజ్యాంగానికి ఉండదు."

అప్పుడు ఒక జర్నలిస్ట్ B.N. Rau ను అడిగాడు: "మీరు రాజ్యాంగాన్ని ఏ దేశాల నుండి తీసుకున్నారు?"

B.N. Rau నవ్వారు: "మేము ప్రపంచం నుండి నేర్చుకున్నాం. UK నుండి Cabinet System, USA నుండి Judicial Review, Ireland నుండి DPSP, Canada నుండి Federation — మంచిది ఎక్కడ ఉన్నా తీసుకున్నాం."

"కానీ అది అప్పు తెచ్చిన రాజ్యాంగం కాదా?" — జర్నలిస్ట్.

B.N. Rau: "ప్రపంచపు మంచి ఆలోచనలు స్వీకరించడం బలహీనత కాదు. అది జ్ఞానం."

ఈ రాజ్యాంగం 395 ఆర్టికల్స్ తో పుట్టింది. ప్రపంచంలోనే అతిపెద్ద లిఖిత రాజ్యాంగం.

GoI Act 1935 — 250 నిబంధనలు.
UK — Cabinet System.
USA — Fundamental Rights.
Ireland — DPSP.
Canada — Strong Centre.

"ఇంత నేర్చుకుని, ఇంత కష్టపడి రాశారు — ఇప్పటికీ జీవిస్తోంది ఈ రాజ్యాంగం" — అంబేడ్కర్ ఆత్మ చిరునవ్వు నవ్వింది."""
    },
    {
        "title": "3.10 రాజ్యాంగ భావన — లిఖిత/అలిఖిత, దృఢ/సౌమ్య",
        "sub": "Written vs Unwritten · Rigid vs Flexible · Enacted vs Evolved · Bryce & Wheare",
        "audio": """రాజ్యాంగ భావన (Concept of Constitution):

రాజ్యాంగం అంటే: రాజ్యం యొక్క ప్రాథమిక చట్టం — ప్రభుత్వ నిర్మాణం, అధికారాల పంపిణీ, పౌరుల హక్కులను నిర్ణయించే సర్వోన్నత చట్టం.

రాజ్యాంగాల వర్గీకరణ — జేమ్స్ బ్రైస్ (James Bryce):

1. లిఖిత రాజ్యాంగం (Written Constitution):
• ఒక నిర్దిష్ట సమయంలో రాసి ఆమోదించిన పత్రం.
• ఉదాహరణ: భారత్, USA, ఫ్రాన్స్, జపాన్
• 'Enacted Constitution' అని కూడా అంటారు.

2. అలిఖిత రాజ్యాంగం (Unwritten Constitution):
• పార్లమెంట్ చట్టాలు, న్యాయ తీర్పులు, సంప్రదాయాల ద్వారా పెరిగింది.
• ఉదాహరణ: United Kingdom (Britain), New Zealand, Israel
• 'Evolved Constitution' అని కూడా అంటారు.

3. దృఢ రాజ్యాంగం (Rigid Constitution):
• సవరించడానికి ప్రత్యేక కఠిన విధానం అవసరం.
• ఉదాహరణ: USA (2/3 Congress + 3/4 States)
• భారత్ — పాక్షికంగా దృఢం (Art. 368 — కొన్ని అంశాలకు రాష్ట్రాల ఆమోదం కావాలి)

4. సౌమ్య రాజ్యాంగం (Flexible Constitution):
• సాధారణ చట్టసభ మెజారిటీతో సవరించవచ్చు.
• ఉదాహరణ: United Kingdom

భారత్ రాజ్యాంగం — మిశ్రమ (Neither purely rigid nor purely flexible):
• కొన్ని నిబంధనలు సాధారణ మెజారిటీతో సవరించవచ్చు.
• కొన్ని నిబంధనలు 2/3 మెజారిటీ + రాష్ట్రాల ఆమోదం అవసరం.
• K.C. Wheare: భారత రాజ్యాంగం "partly flexible and partly rigid"

K.C. Wheare — రాజ్యాంగ పండితుడు:
• Modern Constitutions పుస్తకం రాశారు.
• భారత రాజ్యాంగాన్ని "Quasi-Federal" అన్నారు.
• UK రాజ్యాంగం — అలిఖిత + సౌమ్య (Unwritten + Flexible)"""
    },
    {
        "title": "3.11 సమాఖ్య, ఏకీకృత, అర్ధ-సమాఖ్య స్వభావం",
        "sub": "Federal · Unitary · Quasi-Federal · Nature of Indian Constitution",
        "audio": """రాజ్యాంగాల స్వభావం — అధికారాల పంపిణీ ఆధారంగా:

1. సమాఖ్య రాజ్యాంగం (Federal Constitution):
• కేంద్రం + రాష్ట్రాల మధ్య అధికారాలు రాజ్యాంగబద్ధంగా విభజించబడతాయి.
• ఉదాహరణ: USA, ఆస్ట్రేలియా, స్విట్జర్లాండ్
• లక్షణాలు: లిఖిత రాజ్యాంగం, న్యాయ సమీక్ష, ద్విసభ విధానం, రాజ్యాంగ సర్వోన్నతత

2. ఏకీకృత రాజ్యాంగం (Unitary Constitution):
• అన్ని అధికారాలు కేంద్రంలో కేంద్రీకృతమవుతాయి.
• ఉదాహరణ: UK, France, Japan, China
• రాష్ట్రాలు కేంద్రం సృష్టించిన అధికార కేంద్రాలు మాత్రమే.

3. భారత్ — అర్ధ-సమాఖ్య (Quasi-Federal):
• K.C. Wheare: భారత్ "quasi-federal" — federal రూపంలో ఉంటూ unitary spirit కలది.
• Paul Appleby: "Extremely federalized" అన్నారు.
• Ivor Jennings: "Federation with strong centralizing tendency" అన్నారు.

సమాఖ్య లక్షణాలు (Federal Features) — భారత్:
• లిఖిత రాజ్యాంగం, అధికారాల విభజన (3 Lists)
• స్వతంత్ర న్యాయవ్యవస్థ, ద్విసభా పార్లమెంట్
• రాజ్యాంగ సర్వోన్నతత

ఏకీకృత లక్షణాలు (Unitary Features) — భారత్:
• అవశేష అధికారాలు కేంద్రానికి (ధర్మనిరపేక్ష అంశాలు)
• ఒకే పౌరసత్వం, ఒకే సమగ్ర న్యాయవ్యవస్థ
• గవర్నర్ నియామకం కేంద్రం చేయడం
• అత్యవసర పరిస్థితిలో రాష్ట్రాల అధికారాలు కేంద్రానికి మారడం
• రాష్ట్ర అంశాలపై పార్లమెంట్ చట్టాలు చేయగల అధికారం (Art.249, 252, 253)
• All India Services (IAS, IPS) — కేంద్రం నియంత్రించడం
• రాష్ట్ర జాబితాపై సవరణ చేయగల అధికారం

SR Bommai కేసు (1994): రాష్ట్రాలు కేంద్రానికి "satellite" కాదు; Federal democracy నిజమైనది."""
    },
]

# ─────────────────────────────────────────────
#  MCQ DATA
#  (sec_idx, difficulty, q_te, a, b, c, d, correct, explanation_te)
#  difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
#  exam_type:  appended as 10th element (index 9) when PYQ ('APPSC'/'UPSC'), else omitted
# ─────────────────────────────────────────────

POLITY_CH3_MCQS = [

    # ══════════════ SECTION 0 — Salient Features Overview ══════════════

    (0, 1,
     "Which country has the largest written constitution in the world?\nతెలుగు: ప్రపంచంలో అతిపెద్ద లిఖిత రాజ్యాంగం ఏ దేశానిది?",
     "USA / అమెరికా",
     "Australia / ఆస్ట్రేలియా",
     "India / భారతదేశం (correct)",
     "Canada / కెనడా",
     "c",
     "India has the LARGEST written constitution. Original: 395 Articles + 22 Parts + 8 Schedules."),

    (0, 1,
     "How many Articles were there in the original Indian Constitution (1949)?\nతెలుగు: అసలు భారత రాజ్యాంగంలో (1949) ఎన్ని ఆర్టికల్స్ ఉన్నాయి?",
     "448",
     "395 / 395 (original)",
     "460",
     "350",
     "b",
     "Original (1949) Constitution had 395 Articles. Today it has ~470 (after amendments)."),

    (0, 1,
     "What is the single largest source of the Indian Constitution?\nతెలుగు: భారత రాజ్యాంగం తయారీలో అతిపెద్ద ఏకైక స్రోతం ఏది?",
     "USA Constitution / అమెరికా రాజ్యాంగం",
     "UK Constitution / బ్రిటన్ రాజ్యాంగం",
     "Government of India Act 1935 / GoI Act 1935 (correct — ~250 provisions borrowed)",
     "Ireland Constitution / ఐర్లాండ్ రాజ్యాంగం",
     "c",
     "Government of India Act 1935 contributed about 250 provisions — the single largest source. Other countries' constitutions provided specific features."),

    (0, 2,
     "How many Parts and Schedules were in the original Constitution?\nతెలుగు: భారత రాజ్యాంగ అసలు రూపంలో పార్ట్స్ మరియు షెడ్యూల్స్ ఎన్ని?",
     "25 Parts, 12 Schedules",
     "22 Parts, 8 Schedules / 22 Parts, 8 Schedules (correct)",
     "22 Parts, 12 Schedules",
     "20 Parts, 10 Schedules",
     "b",
     "Original 1949: 22 Parts + 8 Schedules. Today: 25 Parts + 12 Schedules (after amendments)."),

    (0, 2,
     "How many provisions were borrowed from GoI Act 1935 into the Indian Constitution?\nతెలుగు: GoI Act 1935 నుండి భారత రాజ్యాంగంలో దాదాపు ఎన్ని నిబంధనలు చేర్చారు?",
     "100",
     "150",
     "250 / 250 (approx)",
     "350",
     "c",
     "Approximately 250 provisions were borrowed from GoI Act 1935 — making it the single largest source."),

    (0, 3,
     "Which of the following statements about the original Constitution is INCORRECT?\n(1) 395 Articles\n(2) 22 Parts\n(3) 12 Schedules\n(4) GoI Act 1935 = Single Biggest Source\nతెలుగు: కింది వాటిలో అసలు భారత రాజ్యాంగంపై తప్పు ఏది?\n(1) 395 ఆర్టికల్స్\n(2) 22 పార్ట్స్\n(3) 12 షెడ్యూల్స్\n(4) GoI Act 1935 = అతిపెద్ద స్రోతం",
     "Statement 3 wrong — original had 8 Schedules / 3 తప్పు — అసలు 8 Schedules",
     "Statement 1 wrong — original had 448 Articles / 1 తప్పు — 448",
     "Statement 2 wrong — original had 25 Parts / 2 తప్పు — 25 Parts",
     "Statement 4 wrong — USA was biggest source / 4 తప్పు — USA",
     "a",
     "Statement 3 is wrong — original (1949) had 8 SCHEDULES (not 12). 12 came after amendments."),

    (0, 4,
     "Assertion (A): Indian Constitution is called the longest written constitution in the world.\nReason (R): It originally contained 395 Articles, 22 Parts, and 8 Schedules, and was influenced by the Government of India Act 1935 which provided approximately 250 provisions.\nతెలుగు: అభికథనం-కారణం సరైనవా?",
     "Both correct, R explains A / రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "Both correct, R doesn't explain / రెండూ సరైనవి, R వివరణ కాదు",
     "A correct, R wrong / A సరైనది, R తప్పు",
     "A wrong, R correct / A తప్పు, R సరైనది",
     "a",
     "Both A and R are correct, and R precisely explains the length — the heavy borrowing from GoI 1935 + comprehensive original framework gave India the longest written constitution."),

    (0, 2,
     "Which is the largest written constitution in the world? [APPSC Group 2]\nతెలుగు: ప్రపంచంలో అతి పెద్ద లిఖిత రాజ్యాంగం ఏది?",
     "USA Constitution / USA రాజ్యాంగం",
     "Indian Constitution / భారత రాజ్యాంగం (correct)",
     "Canada Constitution / కెనడా రాజ్యాంగం",
     "Australia Constitution / ఆస్ట్రేలియా రాజ్యాంగం",
     "b",
     "భారత రాజ్యాంగమే ప్రపంచంలో అతి పెద్ద లిఖిత రాజ్యాంగం. APPSC Group 2 లో తరచుగా అడిగే ప్రశ్న.",
     "APPSC"),

    # ══════════════ SECTION 1 — Sources of the Constitution ══════════════

    (1, 1,
     "Fundamental Rights in the Indian Constitution were borrowed from which country?\nతెలుగు: భారత రాజ్యాంగంలో మూల హక్కులు ఏ దేశం నుండి స్వీకరించారు?",
     "UK / యూకే",
     "Ireland / ఐర్లాండ్",
     "USA / అమెరికా (correct)",
     "Canada / కెనడా",
     "c",
     "Fundamental Rights (Part III, Articles 12-35) were borrowed from the USA — based on the US Bill of Rights."),

    (1, 1,
     "DPSP (Directive Principles of State Policy) was borrowed from?\nతెలుగు: ఆదేశిక సూత్రాలు ఏ దేశం నుండి స్వీకరించారు?",
     "UK / యూకే",
     "Australia / ఆస్ట్రేలియా",
     "USA / అమెరికా",
     "Ireland / ఐర్లాండ్ (correct)",
     "d",
     "DPSP (Part IV, Articles 36-51) was borrowed from the Irish Constitution (1937)."),

    (1, 1,
     "From which country was the Parliamentary System borrowed?\nతెలుగు: పార్లమెంటరీ పాలన విధానం ఏ దేశం నుండి స్వీకరించారు?",
     "USA / అమెరికా",
     "Canada / కెనడా",
     "UK (Britain) / యూకే (correct)",
     "France / ఫ్రాన్స్",
     "c",
     "Parliamentary System (Cabinet, PM as head, accountability to legislature) — borrowed from the United Kingdom."),

    (1, 2,
     "Are these source-feature pairs correctly matched? Which is INCORRECT?\n(P) USA — Fundamental Rights\n(Q) Ireland — DPSP\n(R) Canada — Concurrent List\n(S) Australia — Joint Sitting of Parliament\nతెలుగు: కింది జంటలు సరిగ్గా జోడించబడ్డాయా? తప్పు ఏది?\n(P) USA — Fundamental Rights\n(Q) Ireland — DPSP\n(R) Canada — Concurrent List\n(S) Australia — Joint Sitting of Parliament",
     "P, Q correct; R wrong — Concurrent List = Australia / R తప్పు — Concurrent List = Australia",
     "Q, R wrong / Q మరియు R తప్పు",
     "Only R wrong — Concurrent List = Canada / R మాత్రమే తప్పు — Canada",
     "All correct / అన్నీ సరైనవే",
     "a",
     "Pair R is wrong — Concurrent List was borrowed from AUSTRALIA (not Canada). Pair S is also wrong (Joint Sitting = Australia). Canada gave Federalism + Residuary Powers."),

    (1, 2,
     "Which of the following are borrowed from the UK Constitution?\n(1) Cabinet System\n(2) Rule of Law\n(3) Judicial Review\n(4) Single Citizenship\nతెలుగు: కింది వాటిలో UK నుండి స్వీకరించిన అంశాలు ఏవి?\n(1) Cabinet System\n(2) Rule of Law\n(3) Judicial Review\n(4) Single Citizenship",
     "1, 2 and 4 only / 1, 2 మరియు 4 మాత్రమే",
     "1 and 3 only / 1 మరియు 3 మాత్రమే",
     "All four / అన్నీ",
     "2 and 4 only / 2 మరియు 4 మాత్రమే",
     "a",
     "Cabinet, Rule of Law, Single Citizenship = UK. Judicial Review = USA (NOT UK). Statement 3 is wrong, hence option (a)."),

    (1, 3,
     "Suspension of Fundamental Rights during Emergency was borrowed from which country?\nతెలుగు: అత్యవసర పరిస్థితిలో మూల హక్కుల నిలిపివేత ఏ దేశం నుండి స్వీకరించారు?",
     "USA / అమెరికా",
     "USSR / సోవియట్ యూనియన్",
     "France / ఫ్రాన్స్",
     "Germany (Weimar) / జర్మనీ (Weimar) (correct)",
     "d",
     "Suspension of FRs during emergency was borrowed from Germany's Weimar Constitution."),

    (1, 4,
     "Which of the following Source-Feature pairs are correctly matched, and which is wrong?\n(1) South Africa — Amendment Procedure, Election of RS members\n(2) Japan — Procedure Established by Law\n(3) USSR — DPSP\n(4) France — Republic, Liberty, Equality, Fraternity\nతెలుగు: కింది అన్నీ సరైన జంటలు ఏవి?\n(1) South Africa — Amendment Procedure, RS Election\n(2) Japan — Procedure Established by Law\n(3) USSR — DPSP\n(4) France — Republic + Liberty/Equality/Fraternity",
     "1, 2 and 4 correct; 3 wrong / 1, 2, 4 సరైనవి; 3 తప్పు",
     "All correct / అన్నీ సరైనవి",
     "2 and 3 wrong / 2 మరియు 3 తప్పు",
     "Only 1 and 4 correct / 1 మరియు 4 మాత్రమే",
     "a",
     "Pair 3 is wrong — DPSP came from IRELAND (not USSR). USSR contributed Fundamental Duties. The other three pairs are correct."),

    (1, 2,
     "From which country's constitution were the Directive Principles of State Policy inspired? [UPSC Style]\nతెలుగు: DPSPలు ఏ దేశ రాజ్యాంగం నుండి స్ఫూర్తి పొందాయి?",
     "United States of America / USA",
     "United Kingdom / UK",
     "Canada / కెనడా",
     "Ireland / ఐర్లాండ్ (correct)",
     "d",
     "DPSPs were inspired by the Irish Constitution (1937). Ireland in turn borrowed from Spain.",
     "UPSC"),

    # ══════════════ SECTION 2 — Federal vs Unitary Features ══════════════

    (2, 1,
     "Where do Residuary Powers reside in the Indian Constitution?\nతెలుగు: భారత రాజ్యాంగంలో అవశేష అధికారాలు ఎవరికి ఉంటాయి?",
     "State Governments / రాష్ట్ర ప్రభుత్వాలు",
     "Supreme Court / సుప్రీం కోర్టు",
     "Union Government / కేంద్ర ప్రభుత్వం (correct — Union)",
     "Election Commission / ఎన్నికల సంఘం",
     "c",
     "Article 248: Residuary Powers vest with the UNION (Centre) — borrowed from Canada. (USA gives them to states.)"),

    (2, 1,
     "Who described India as a 'Quasi-Federal' state?\nతెలుగు: భారతదేశాన్ని 'Quasi-Federal' రాజ్యమని ఎవరు అన్నారు?",
     "Dr. B.R. Ambedkar / అంబేడ్కర్",
     "K.C. Wheare / K.C. వేర్ (correct)",
     "Jawaharlal Nehru / నెహ్రూ",
     "Granville Austin / గ్రాన్‌విల్ ఆస్టిన్",
     "b",
     "K.C. Wheare called India 'Quasi-Federal' due to strong centralising tendencies despite federal structure."),

    (2, 1,
     "Single Citizenship in India is which type of feature?\nతెలుగు: ఒకే పౌరసత్వం ఇది ఏ లక్షణం?",
     "Federal Feature / సమాఖ్య లక్షణం",
     "Unitary Feature / ఏకీకృత లక్షణం (correct)",
     "Parliamentary Feature / పార్లమెంటరీ లక్షణం",
     "Judicial Feature / న్యాయపర లక్షణం",
     "b",
     "Single Citizenship is a UNITARY feature. (USA has dual citizenship — federal + state. India = single, borrowed from UK.)"),

    (2, 2,
     "Which of the following are Federal Features of the Indian Constitution?\n(1) Written Constitution\n(2) Residuary Powers to Centre\n(3) Division of Powers (3 Lists)\n(4) Single Citizenship\nతెలుగు: కింది వాటిలో సమాఖ్య లక్షణాలు ఏవి?\n(1) లిఖిత రాజ్యాంగం\n(2) అవశేష అధికారాలు కేంద్రానికి\n(3) అధికారాల విభజన (3 Lists)\n(4) ఒకే పౌరసత్వం",
     "1 and 3 only / 1 మరియు 3 మాత్రమే (correct)",
     "1, 2 and 3 / 1, 2 మరియు 3",
     "1, 3 and 4 / 1, 3 మరియు 4",
     "2 and 4 only / 2 మరియు 4 మాత్రమే",
     "a",
     "Federal: Written Constitution (1), Division of Powers (3). Residuary to Centre (2) = UNITARY tilt. Single Citizenship (4) = UNITARY."),

    (2, 2,
     "Which of the following are Unitary Features of the Indian Constitution?\n(1) Centre appoints Governors\n(2) Equal representation of states in Rajya Sabha\n(3) All India Services\n(4) Integrated Judiciary\nతెలుగు: కింది వాటిలో ఏకీకృత లక్షణాలు ఏవి?\n(1) గవర్నర్ నియామకం కేంద్రం\n(2) రాజ్యసభలో అన్ని రాష్ట్రాలకు సమాన ప్రాతినిధ్యం\n(3) అఖిల భారత సేవలు\n(4) ఏకీకృత న్యాయవ్యవస్థ",
     "1, 3 and 4 only / 1, 3 మరియు 4 మాత్రమే (correct)",
     "1, 2 and 3 / 1, 2 మరియు 3",
     "2 and 4 only / 2 మరియు 4 మాత్రమే",
     "All four / అన్నీ",
     "a",
     "Unitary tilt: Centre-appointed Governors (1), All India Services (3), Integrated Judiciary (4). RS Equal representation (2) = FEDERAL feature (USA model)."),

    (2, 3,
     "Key difference between Indian and American Federalism?\nతెలుగు: USA మరియు భారత్ ఫెడరల్ వ్యవస్థల మధ్య ముఖ్య తేడా ఏది?",
     "India has written, USA doesn't / భారత్ లిఖిత, USA కాదు",
     "USA: Residuary Powers with States; India: with Centre / USA లో రాష్ట్రాలు, భారత్ లో కేంద్రం (correct)",
     "India bicameral, USA unicameral / భారత్ ద్విసభ, USA ఏకసభ",
     "USA no Judicial Review, India has / USA లో న్యాయ సమీక్ష లేదు",
     "b",
     "USA = Residuary Powers with States (10th Amendment). India = Residuary Powers with CENTRE (Article 248). Both have written Constitution + Judicial Review."),

    (2, 4,
     "Regarding rigid/flexible nature of the Indian Constitution, which is correct?\nతెలుగు: భారత రాజ్యాంగం Rigid or Flexible గురించి సరైనది?",
     "Completely Rigid — needs 2/3 + state ratification for all amendments / పూర్తిగా అనమ్యం",
     "Completely Flexible — simple majority for all / పూర్తిగా సౌమ్యం",
     "Partly Rigid, Partly Flexible / పాక్షికంగా దృఢం, పాక్షికంగా సౌమ్యం (correct)",
     "Cannot be amended / సవరణలు నిషిద్ధం",
     "c",
     "Article 368 has THREE amendment routes: simple majority + 2/3 majority + 2/3 + state ratification. So Constitution is BOTH rigid and flexible — partly each."),

    (2, 2,
     "Who described India's federal system as 'Quasi-Federal'? [APPSC Group 2]\nతెలుగు: భారత సమాఖ్య వ్యవస్థను 'Quasi-Federal' అని ఎవరు అన్నారు?",
     "Dr. B.R. Ambedkar / అంబేడ్కర్",
     "Granville Austin / గ్రాన్‌విల్ ఆస్టిన్",
     "K.C. Wheare / K.C. వేర్ (correct)",
     "Jawaharlal Nehru / నెహ్రూ",
     "c",
     "K.C. Wheare's famous description: India is a 'Quasi-Federal' state — federal structure with strong centralising tendencies.",
     "APPSC"),

    # ══════════════ SECTION 3 — Parliamentary System ══════════════

    (3, 1,
     "What kind of head is the Indian President?\nతెలుగు: భారత రాష్ట్రపతి ఏ రకమైన అధినేత?",
     "Real Executive / నిజమైన కార్యనిర్వాహకుడు",
     "Nominal/Constitutional Head / నామమాత్రపు రాజ్యాంగపు అధినేత (correct)",
     "Independent Ruler / స్వతంత్ర పాలకుడు",
     "Head of Parliament / Parliament అధ్యక్షుడు",
     "b",
     "President is the NOMINAL/CONSTITUTIONAL head. Real executive power lies with the Council of Ministers (PM-led)."),

    (3, 1,
     "To which house is the Council of Ministers collectively responsible in India?\nతెలుగు: మంత్రి మండలి ఏ సభకు సమష్టి బాధ్యత వహిస్తుంది?",
     "Rajya Sabha / రాజ్యసభ",
     "Lok Sabha / లోక్ సభ (correct)",
     "President / రాష్ట్రపతి",
     "Supreme Court / సుప్రీం కోర్టు",
     "b",
     "Article 75(3): Council of Ministers is collectively responsible to LOK SABHA. They must resign if Lok Sabha passes a no-confidence motion."),

    (3, 1,
     "From which country was the Parliamentary System borrowed?\nతెలుగు: పార్లమెంటరీ పద్ధతి ఏ దేశం నుండి స్వీకరించారు?",
     "USA / అమెరికా",
     "Australia / ఆస్ట్రేలియా",
     "UK (Britain) / యూకే (correct)",
     "Canada / కెనడా",
     "c",
     "Parliamentary System (Cabinet government, PM accountable to legislature) — directly borrowed from the United Kingdom."),

    (3, 2,
     "Key difference between Parliamentary and Presidential systems?\nతెలుగు: పార్లమెంటరీ vs అధ్యక్ష పద్ధతి ముఖ్య తేడా?",
     "Parliamentary: President is real executive / అధ్యక్షుడు నిజ కార్యనిర్వాహకుడు",
     "Presidential: executive accountable to legislature / కార్యనిర్వాహకుడు శాసనసభకు బాధ్యుడు",
     "Parliamentary: PM accountable to Lok Sabha; Presidential: President independent of legislature / పార్లమెంటరీ లో PM బాధ్యుడు; అధ్యక్ష పద్ధతిలో అధ్యక్షుడు స్వతంత్రుడు (correct)",
     "No difference / తేడా లేదు",
     "c",
     "Parliamentary (UK, India): PM accountable to legislature, can be voted out. Presidential (USA): President fixed term, separately elected, NOT accountable to legislature."),

    (3, 2,
     "In which Articles is the office of Prime Minister mentioned?\nతెలుగు: ప్రధానమంత్రి పదవి ఏ ఆర్టికల్‌లో పేర్కొన్నారు?",
     "Article 52 / అధికరణం 52",
     "Article 53 / అధికరణం 53",
     "Articles 74 and 75 / అధికరణాలు 74 మరియు 75 (correct)",
     "Article 79 / అధికరణం 79",
     "c",
     "Articles 74 (Council of Ministers) + 75 (PM appointment, oath, salary). Article 52 = President. Article 79 = Parliament."),

    (3, 3,
     "Against whom can a No-Confidence Motion be passed?\nతెలుగు: అవిశ్వాస తీర్మానం ఎవరికి వ్యతిరేకంగా?",
     "President / రాష్ట్రపతి",
     "Council of Ministers / మంత్రి మండలి (correct)",
     "Supreme Court Judge / సుప్రీం కోర్టు జడ్జి",
     "Vice-President / ఉపరాష్ట్రపతి",
     "b",
     "No-Confidence Motion (Rule 198, Lok Sabha) is moved against the COUNCIL OF MINISTERS. If passed, the entire Cabinet must resign."),

    (3, 4,
     "How does Indian Parliament differ from UK Parliament?\nతెలుగు: భారత vs UK Parliament ఎలా భిన్నం?",
     "India: PM is real executive; UK: monarch is real executive / భారత్ PM, UK రాజు",
     "India: President under constitutional checks; UK: Parliament Sovereign / భారత్ రాష్ట్రపతి రాజ్యాంగ నిర్బంధంలో; UK Sovereign",
     "India: Judicial Review present; UK: Parliamentary Sovereignty — courts cannot strike down laws / భారత్ లో Judicial Review; UK లో Parliamentary Sovereignty (correct)",
     "India: PM removed by RS; UK: by House of Lords / India PM ను RS తొలగిస్తుంది",
     "c",
     "Key difference: Indian Constitution allows JUDICIAL REVIEW (courts can strike down unconstitutional laws). UK has Parliamentary Sovereignty — no court can override Parliament."),

    (3, 2,
     "To which house is the Council of Ministers collectively responsible? [APPSC Group 2]\nతెలుగు: మంత్రి మండలి ఏ సభకు సమష్టి బాధ్యత వహిస్తుంది?",
     "Rajya Sabha / రాజ్యసభ",
     "Lok Sabha / లోక్ సభ (correct)",
     "President / రాష్ట్రపతి",
     "Supreme Court / సుప్రీం కోర్టు",
     "b",
     "Article 75(3): Council of Ministers is collectively responsible to LOK SABHA only. APPSC Group 2 frequent question.",
     "APPSC"),

    # ══════════════ SECTION 4 — FRs and DPSP ══════════════

    (4, 1,
     "In which Part of the Indian Constitution are Fundamental Rights?\nతెలుగు: మూల హక్కులు భారత రాజ్యాంగంలో ఏ భాగంలో ఉన్నాయి?",
     "Part II / భాగం II",
     "Part III / భాగం III (correct — Articles 12-35)",
     "Part IV / భాగం IV",
     "Part V / భాగం V",
     "b",
     "Fundamental Rights are in Part III (Articles 12-35) of the Indian Constitution."),

    (4, 1,
     "In which Part are the Directive Principles of State Policy?\nతెలుగు: ఆదేశిక సూత్రాలు ఏ భాగంలో ఉన్నాయి?",
     "Part III / భాగం III",
     "Part IV-A / భాగం IV-A",
     "Part IV / భాగం IV (correct — Articles 36-51)",
     "Part V / భాగం V",
     "c",
     "DPSPs are in Part IV (Articles 36-51). Part IV-A (Article 51A) contains Fundamental Duties."),

    (4, 2,
     "Key difference between Fundamental Rights (FRs) and DPSP?\nతెలుగు: FR vs DPSP ముఖ్య తేడా?",
     "FR Non-Justiciable; DPSP Justiciable / FR న్యాయేతర; DPSP న్యాయపర",
     "FR Justiciable; DPSP Non-Justiciable / FR న్యాయపర; DPSP న్యాయేతర (correct)",
     "FR Part IV; DPSP Part III / తారుమారు",
     "FR Ireland; DPSP USA / తారుమారు",
     "b",
     "FRs are JUSTICIABLE (enforceable by courts). DPSPs are NON-JUSTICIABLE (not directly enforceable; merely guidelines for the State)."),

    (4, 2,
     "Regarding DPSP, which of the following are CORRECT?\n(1) Located in Part IV\n(2) Borrowed from Ireland\n(3) Justiciable — enforceable in courts\n(4) Articles 36-51\nతెలుగు: DPSP గురించి సరైనవి ఏవి?\n(1) Part IV లో\n(2) Ireland నుండి\n(3) Justiciable — న్యాయస్థానాల్లో అమలు\n(4) Articles 36-51",
     "1, 2 and 4 only / 1, 2 మరియు 4 మాత్రమే (correct)",
     "All four / అన్నీ",
     "2 and 3 only / 2 మరియు 3 మాత్రమే",
     "3 and 4 only / 3 మరియు 4 మాత్రమే",
     "a",
     "Statements 1, 2, 4 correct. Statement 3 wrong — DPSPs are NON-justiciable (cannot be enforced in courts)."),

    (4, 3,
     "How did Granville Austin describe FRs and DPSPs?\nతెలుగు: Granville Austin FR + DPSP ను ఏమని వర్ణించారు?",
     "Heart and Soul of the Constitution / రాజ్యాంగ హృదయం + ఆత్మ (correct)",
     "Two wheels of a chariot / రెండు చక్రాలు",
     "Two contradictory elements / విరుద్ధ అంశాలు",
     "Conscience of the Constitution / అంతర్మనస్సు",
     "a",
     "Granville Austin called FRs and DPSPs together the 'Conscience of the Indian Constitution' — but in popular usage 'Heart and Soul' is also attributed (Ambedkar called Article 32 the 'Heart and Soul')."),

    (4, 4,
     "Assertion (A): Fundamental Rights are justiciable but Directive Principles are not.\nReason (R): DPSPs are ideals and objectives for the state to pursue, but courts cannot enforce them against the government like Fundamental Rights.\nతెలుగు: అభికథనం-కారణం సరైనవా?",
     "Both correct, R explains A / రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "Both correct, R doesn't explain / రెండూ సరైనవి, R వివరణ కాదు",
     "A correct, R wrong / A సరైనది, R తప్పు",
     "A wrong, R correct / A తప్పు, R సరైనది",
     "a",
     "Both A and R correct. R precisely explains A — DPSPs being IDEALS (not enforceable rights) is exactly why they're non-justiciable."),

    (4, 2,
     "Which Part and Articles of the Indian Constitution deal with DPSP? [UPSC Style]\nతెలుగు: DPSPలు ఏ భాగం + ఆర్టికల్స్?",
     "Part III, Articles 12-35 / Part III, 12-35",
     "Part IV, Articles 36-51 / Part IV, 36-51 (correct)",
     "Part IV-A, Article 51A / Part IV-A, 51A",
     "Part V, Articles 52-78 / Part V, 52-78",
     "b",
     "DPSPs: Part IV, Articles 36-51. Part IV-A (51A) = Fundamental Duties. Part III (12-35) = Fundamental Rights.",
     "UPSC"),

    (4, 2,
     "From which country were Fundamental Rights borrowed? [APPSC Group 2]\nతెలుగు: మూల హక్కులు ఏ దేశం నుండి?",
     "UK / యూకే",
     "Ireland / ఐర్లాండ్",
     "USA / అమెరికా (correct)",
     "Canada / కెనడా",
     "c",
     "Fundamental Rights are based on the US Bill of Rights. Borrowed from the USA Constitution.",
     "APPSC"),

    # ══════════════ SECTION 5 — Fundamental Duties ══════════════

    (5, 1,
     "In which Article are Fundamental Duties mentioned?\nతెలుగు: మౌలిక విధులు ఏ ఆర్టికల్‌లో ఉన్నాయి?",
     "Article 51 / అధికరణం 51",
     "Article 51A / అధికరణం 51A (correct)",
     "Article 12 / అధికరణం 12",
     "Article 36 / అధికరణం 36",
     "b",
     "Fundamental Duties are in Article 51A (Part IV-A). Added by the 42nd Amendment 1976."),

    (5, 1,
     "Which Constitutional Amendment first added Fundamental Duties?\nతెలుగు: మౌలిక విధులు ఏ సవరణ ద్వారా చేర్చారు?",
     "40th Amendment 1976 / 40వ సవరణ",
     "42nd Amendment 1976 / 42వ సవరణ 1976 (correct)",
     "44th Amendment 1978 / 44వ సవరణ",
     "86th Amendment 2002 / 86వ సవరణ",
     "b",
     "42nd Amendment 1976 — the 'Mini Constitution' — added Fundamental Duties (initially 10) on the recommendation of Swaran Singh Committee."),

    (5, 2,
     "What is the 11th Fundamental Duty added by the 86th Amendment 2002?\nతెలుగు: 86వ సవరణ ద్వారా చేర్చిన 11వ మౌలిక విధి ఏది?",
     "Respect national flag / జాతీయ పతాకాన్ని గౌరవించడం",
     "Develop scientific temper / శాస్త్రీయ దృష్టి అభివృద్ధి",
     "Parents to provide education to children aged 6-14 / 6–14 సం. పిల్లలకు విద్య (correct)",
     "Protect public property / ప్రజా ఆస్తి కాపాడడం",
     "c",
     "86th Amendment 2002 added the 11th Fundamental Duty: parents/guardians to provide opportunities for education to children aged 6-14 years (linked to Article 21A — Right to Education)."),

    (5, 2,
     "Regarding Fundamental Duties, which of the following are CORRECT?\n(1) 42nd Amendment 1976 — initially 10 duties\n(2) 86th Amendment 2002 — 11th duty added\n(3) Justiciable — enforceable in courts\n(4) Inspired by USSR Constitution\nతెలుగు: మౌలిక విధుల గురించి సరైనవి ఏవి?\n(1) 42వ సవరణ — మొదట 10 విధులు\n(2) 86వ సవరణ — 11వ విధి\n(3) Justiciable\n(4) USSR నుండి స్ఫూర్తి",
     "1, 2 and 4 only / 1, 2 మరియు 4 మాత్రమే (correct)",
     "All four / అన్నీ",
     "2 and 3 only / 2 మరియు 3 మాత్రమే",
     "1 and 4 only / 1 మరియు 4 మాత్రమే",
     "a",
     "Statements 1, 2, 4 correct. Statement 3 wrong — Fundamental Duties are NON-JUSTICIABLE (not directly enforceable, like DPSPs)."),

    (5, 3,
     "Which Committee recommended the addition of Fundamental Duties?\nతెలుగు: మౌలిక విధుల కోసం సిఫారసు చేసిన కమిటీ ఏది?",
     "Balwant Rai Mehta Committee / బల్వంత్ రాయ్ మెహతా",
     "Swaran Singh Committee / స్వరణ్ సింగ్ కమిటీ (correct)",
     "L.M. Singhvi Committee / L.M. సింఘ్వి",
     "Ashok Mehta Committee / అశోక్ మెహతా",
     "b",
     "Swaran Singh Committee (1976) — appointed by PM Indira Gandhi — recommended adding Fundamental Duties. Implemented via 42nd Amendment 1976."),

    (5, 4,
     "Which of the following pairs are ALL correctly matched?\n(1) 42nd Amendment 1976 — 10 Fundamental Duties added\n(2) 86th Amendment 2002 — 11th duty (education for 6-14)\n(3) Fundamental Duties in Article 51\n(4) Recommended by Swaran Singh Committee\nతెలుగు: కింది అన్నీ సరైన జంటలు ఏవి?\n(1) 42వ సవరణ — 10 విధులు\n(2) 86వ సవరణ — 11వ విధి\n(3) మౌలిక విధులు Article 51 లో\n(4) స్వరణ్ సింగ్ కమిటీ",
     "1, 2 and 4 only correct / 1, 2 మరియు 4 మాత్రమే సరైనవి (correct)",
     "All four correct / అన్నీ సరైనవి",
     "Only 2 and 3 / 2 మరియు 3 మాత్రమే",
     "3 and 4 wrong / 3 మరియు 4 తప్పు",
     "a",
     "Pair 3 is wrong — Fundamental Duties are in Article 51A (NOT 51). Article 51 = DPSP about international peace. Pairs 1, 2, 4 correct."),

    (5, 2,
     "How many Fundamental Duties were initially added by the 42nd Amendment 1976? [APPSC Group 2]\nతెలుగు: మొదట ఎన్ని మౌలిక విధులు 42వ సవరణ ద్వారా చేర్చారు?",
     "8",
     "10 / 10 (correct)",
     "11",
     "12",
     "b",
     "42వ సవరణ 1976 ద్వారా మొదట 10 మౌలిక విధులు చేర్చారు. 86వ సవరణ 2002 ద్వారా 11వ విధి (విద్య) చేర్చారు. Total = 11.",
     "APPSC"),

    # ══════════════ SECTION 6 — Secularism, Universal Franchise, Independent Bodies ══════════════

    (6, 1,
     "Which amendment added 'Secular' to the Preamble?\nతెలుగు: 'Secular' పదాన్ని ప్రస్తావనలో ఏ సవరణ ద్వారా చేర్చారు?",
     "40th Amendment 1975 / 40వ సవరణ",
     "42nd Amendment 1976 / 42వ సవరణ 1976 (correct)",
     "44th Amendment 1978 / 44వ సవరణ",
     "52nd Amendment 1985 / 52వ సవరణ",
     "b",
     "42nd Amendment (Mini Constitution) added 'Secular', 'Socialist', and 'Integrity' to the Preamble (originally read 'Sovereign Democratic Republic')."),

    (6, 1,
     "The 61st Amendment 1989 reduced voting age from — to — ?\nతెలుగు: 61వ సవరణ ఓటు హక్కు వయస్సును ఎంత నుండి ఎంతకి తగ్గించింది?",
     "25 to 21 / 25 → 21",
     "21 to 18 / 21 → 18 (correct)",
     "18 to 16 / 18 → 16",
     "21 to 16 / 21 → 16",
     "b",
     "61st Amendment (1989) under PM V.P. Singh reduced voting age from 21 to 18 — expanding universal adult franchise."),

    (6, 1,
     "Election Commission of India is established under which Article?\nతెలుగు: ఎన్నికల సంఘం ఏ ఆర్టికల్ ద్వారా ఏర్పాటైంది?",
     "Article 315 / అధికరణం 315",
     "Article 324 / అధికరణం 324 (correct)",
     "Article 280 / అధికరణం 280",
     "Article 148 / అధికరణం 148",
     "b",
     "Article 324 establishes the ECI. Article 315 = UPSC; Article 280 = Finance Commission; Article 148 = CAG."),

    (6, 2,
     "Single Citizenship in India is which feature?\nతెలుగు: 'ఒకే పౌరసత్వం' ఏ లక్షణం?",
     "Federal Feature / సమాఖ్య లక్షణం",
     "Unitary Feature / ఏకీకృత లక్షణం (correct)",
     "Parliamentary Feature / పార్లమెంటరీ లక్షణం",
     "International Feature / అంతర్జాతీయ లక్షణం",
     "b",
     "Single Citizenship is a UNITARY feature — borrowed from UK. (USA has dual citizenship — federal + state.)"),

    (6, 2,
     "Match the following independent constitutional bodies with their Articles:\n(P) Election Commission — (1) Article 280\n(Q) CAG — (2) Article 324\n(R) Finance Commission — (3) Article 315\n(S) UPSC — (4) Article 148\nతెలుగు: కింది స్వతంత్ర సంస్థలను వాటి ఆర్టికల్‌తో జోడించండి:\n(P) ECI — (1) Article 280\n(Q) CAG — (2) Article 324\n(R) Finance Commission — (3) Article 315\n(S) UPSC — (4) Article 148",
     "P-2, Q-4, R-1, S-3 (correct)",
     "P-1, Q-2, R-3, S-4",
     "P-2, Q-1, R-4, S-3",
     "P-3, Q-4, R-1, S-2",
     "a",
     "ECI = 324 (2); CAG = 148 (4); FC = 280 (1); UPSC = 315 (3). Hence P-2, Q-4, R-1, S-3."),

    (6, 3,
     "What does Secularism mean in the Indian context?\nతెలుగు: భారత రాజ్యాంగంలో లౌకికత అంటే ఏమిటి?",
     "Government prohibits all religions / అన్ని మతాలను నిరోధిస్తుంది",
     "Government has an official religion / అధికారిక మతం ఉంటుంది",
     "Equal respect to all religions; no official religion / అన్ని మతాలను సమానంగా గౌరవిస్తుంది (correct)",
     "Religion is banned / మతం నిషిద్ధం",
     "c",
     "Indian Secularism = 'Sarva Dharma Sambhava' (equal respect to all religions). State has NO official religion but treats all faiths equally — different from French strict secularism."),

    (6, 4,
     "Assertion (A): India follows Universal Adult Franchise since the Constitution came into force.\nReason (R): The 61st Constitutional Amendment 1989 reduced voting age from 21 to 18.\nతెలుగు: అభికథనం-కారణం సరైనవా?",
     "Both correct, R explains A / రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "Both correct, R doesn't explain / రెండూ సరైనవి, R వివరణ కాదు (correct)",
     "A correct, R wrong / A సరైనది, R తప్పు",
     "A wrong, R correct / A తప్పు, R సరైనది",
     "b",
     "Both A and R are correct, but R does NOT explain A. India had Universal Adult Franchise from 1950 itself (with age 21). The 61st Amendment merely EXPANDED it to age 18 in 1989 — it didn't create the concept."),

    (6, 2,
     "What change did the 61st Constitutional Amendment 1989 bring? [APPSC Group 2]\nతెలుగు: 61వ సవరణ ఏ మార్పు తీసుకువచ్చింది?",
     "Added Fundamental Duties / మౌలిక విధులు",
     "Reduced voting age from 21 to 18 / ఓటు హక్కు వయస్సు 21→18 (correct)",
     "Added Secular and Socialist to Preamble / Secular/Socialist Preamble లో",
     "Gave constitutional status to Panchayati Raj / Panchayati Raj కు రాజ్యాంగ హోదా",
     "b",
     "61వ సవరణ 1989 ఓటు హక్కు వయస్సును 21 నుండి 18 కి తగ్గించింది. PM V.P. Singh హయాంలో.",
     "APPSC"),

    (6, 2,
     "Which Independent Constitutional Body is established under Article 324? [UPSC Style]\nతెలుగు: అధికరణం 324 కింద ఏ స్వతంత్ర సంస్థ?",
     "UPSC / UPSC",
     "CAG / CAG",
     "Election Commission of India / ఎన్నికల సంఘం (correct)",
     "Finance Commission / Finance Commission",
     "c",
     "Article 324 establishes the ECI. Articles: ECI=324, UPSC=315, CAG=148, FC=280, AG=76.",
     "UPSC"),

    # ══════════════ SECTION 7 — Emergency Provisions, Panchayati Raj, Misc ══════════════

    (7, 1,
     "Under which Article can National Emergency be proclaimed?\nతెలుగు: జాతీయ అత్యవసర పరిస్థితి ఏ ఆర్టికల్?",
     "Article 356 / అధికరణం 356",
     "Article 352 / అధికరణం 352 (correct)",
     "Article 360 / అధికరణం 360",
     "Article 368 / అధికరణం 368",
     "b",
     "Article 352 = National Emergency. Article 356 = President's Rule (state); Article 360 = Financial Emergency; Article 368 = Amendment procedure."),

    (7, 1,
     "Which Amendment gave constitutional status to Panchayati Raj?\nతెలుగు: Panchayati Raj కు రాజ్యాంగ హోదా ఏ సవరణ ద్వారా?",
     "42nd Amendment 1976 / 42వ సవరణ",
     "61st Amendment 1989 / 61వ సవరణ",
     "73rd Amendment 1992 / 73వ సవరణ 1992 (correct)",
     "97th Amendment 2011 / 97వ సవరణ",
     "c",
     "73rd Amendment 1992 gave constitutional status to Panchayati Raj (rural local govt) — Part IX, Articles 243-243O. 74th Amendment did the same for Urban Local Bodies."),

    (7, 2,
     "Match the three types of emergency with their Articles:\n(P) National Emergency — (1) Article 360\n(Q) President's Rule — (2) Article 352\n(R) Financial Emergency — (3) Article 356\nతెలుగు: అత్యవసర పరిస్థితులను వాటి ఆర్టికల్‌తో జోడించండి:\n(P) National Emergency — (1) Article 360\n(Q) President's Rule — (2) Article 352\n(R) Financial Emergency — (3) Article 356",
     "P-2, Q-3, R-1 (correct)",
     "P-1, Q-2, R-3",
     "P-3, Q-1, R-2",
     "P-2, Q-1, R-3",
     "a",
     "National = 352 (P-2); President's Rule = 356 (Q-3); Financial = 360 (R-1). Hence P-2, Q-3, R-1."),

    (7, 2,
     "Match the following Constitutional Amendments correctly:\n(1) 42nd Amendment 1976 — Secular, Socialist added to Preamble\n(2) 61st Amendment 1989 — Voting age 21→18\n(3) 73rd Amendment 1992 — Urban Local Bodies\n(4) 86th Amendment 2002 — 11th Fundamental Duty\nతెలుగు: రాజ్యాంగ సవరణలను సరిగ్గా జోడించండి:\n(1) 42వ సవరణ — Secular/Socialist Preamble\n(2) 61వ సవరణ — ఓటు 21→18\n(3) 73వ సవరణ — Urban Local Bodies\n(4) 86వ సవరణ — 11వ విధి",
     "1, 2 and 4 only correct / 1, 2 మరియు 4 మాత్రమే సరైనవి (correct)",
     "All four correct / అన్నీ సరైనవి",
     "2 and 3 only / 2 మరియు 3 మాత్రమే",
     "1 and 4 only / 1 మరియు 4 మాత్రమే",
     "a",
     "Pair 3 is wrong — 73rd Amendment was for Panchayati Raj (RURAL local bodies). Urban Local Bodies came via 74th Amendment."),

    (7, 3,
     "Under which Article is President's Rule imposed when state Constitutional machinery fails?\nతెలుగు: రాష్ట్రపతి పాలన ఏ ఆర్టికల్?",
     "Article 352 / అధికరణం 352",
     "Article 356 / అధికరణం 356 (correct)",
     "Article 360 / అధికరణం 360",
     "Article 368 / అధికరణం 368",
     "b",
     "Article 356 = President's Rule (Failure of Constitutional Machinery in States). Triggered by Governor's report OR President's own satisfaction."),

    (7, 4,
     "Assertion (A): Co-operative Societies were given constitutional recognition through the 97th Constitutional Amendment 2011.\nReason (R): The 97th Amendment inserted Part IX-B (Articles 243ZH to 243ZT) into the Constitution dealing with Co-operative Societies.\nతెలుగు: అభికథనం-కారణం సరైనవా?",
     "Both correct, R explains A / రెండూ సరైనవి, R అనేది A కి సరైన వివరణ (correct)",
     "Both correct, R doesn't explain / రెండూ సరైనవి, R వివరణ కాదు",
     "A correct, R wrong / A సరైనది, R తప్పు",
     "A wrong, R correct / A తప్పు, R సరైనది",
     "a",
     "Both A and R correct, R precisely explains A — Part IX-B (Articles 243ZH to 243ZT) is exactly what gave Co-operative Societies constitutional recognition via 97th Amendment 2011."),

    (7, 2,
     "Under which Article can the President proclaim Financial Emergency? [UPSC Style]\nతెలుగు: ఆర్థిక అత్యవసర పరిస్థితి ఏ ఆర్టికల్?",
     "Article 352 / అధికరణం 352",
     "Article 356 / అధికరణం 356",
     "Article 360 / అధికరణం 360 (correct)",
     "Article 368 / అధికరణం 368",
     "c",
     "Article 360 = Financial Emergency. Has never been invoked in Indian history.",
     "UPSC"),

    # ══════════════ SECTION 9 — Constitution Classification ══════════════

    (9, 1,
     "Who classified constitutions into 'Written' and 'Unwritten'?\nతెలుగు: రాజ్యాంగాలను 'Written' + 'Unwritten' గా వర్గీకరించిన పండితుడు?",
     "K.C. Wheare / K.C. వేర్",
     "James Bryce / జేమ్స్ బ్రైస్ (correct)",
     "Ivor Jennings / ఐవర్ జెన్నింగ్స్",
     "Paul Appleby / పాల్ ఆపిల్‌బీ",
     "b",
     "James Bryce — eminent constitutional scholar — classified constitutions into Written (codified) vs Unwritten (uncodified)."),

    (9, 1,
     "Which country has an Unwritten Constitution?\nతెలుగు: అలిఖిత రాజ్యాంగం ఉన్న దేశం?",
     "USA / అమెరికా",
     "France / ఫ్రాన్స్",
     "United Kingdom / యూకే (correct)",
     "Japan / జపాన్",
     "c",
     "UK has an UNWRITTEN/UNCODIFIED constitution — based on conventions, statutes, judicial decisions, royal prerogatives. NOT a single document."),

    (9, 1,
     "What is meant by an 'Enacted Constitution'?\nతెలుగు: 'Enacted Constitution' అంటే?",
     "Constitution that grew gradually through parliamentary debate / క్రమంగా పెరిగిన",
     "Constitution incorporating customs and traditions / సంప్రదాయాల ద్వారా",
     "Constitution written and adopted at one specific time by a body / నిర్దిష్ట సమావేశం ద్వారా రాసి ఆమోదించిన (correct)",
     "Constitution shaped by court rulings / కోర్టు తీర్పుల ద్వారా",
     "c",
     "Enacted Constitution = formally drafted, written and adopted at a specific time by a legislature/constituent body (e.g., India, USA). Opposite = Evolved (UK)."),

    (9, 2,
     "What is the key feature of a 'Rigid Constitution'?\nతెలుగు: దృఢ రాజ్యాంగం ముఖ్య లక్షణం?",
     "Can be amended by simple majority / సాధారణ మెజారిటీ",
     "Requires a special, more difficult procedure to amend / కఠిన విధానం (correct)",
     "Amendments are impossible / సాధ్యం కాదు",
     "Only Constitutional Court can amend / కోర్టు మాత్రమే",
     "b",
     "Rigid Constitution = requires special amendment procedure (e.g., 2/3 majority + state ratification). Examples: USA (rigid), UK (flexible)."),

    (9, 2,
     "USA Constitution belongs to which category?\nతెలుగు: USA రాజ్యాంగం ఏ వర్గం?",
     "Flexible + Unwritten / Flexible + Unwritten",
     "Rigid + Written / Rigid + Written (correct)",
     "Flexible + Written / Flexible + Written",
     "Rigid + Unwritten / Rigid + Unwritten",
     "b",
     "USA Constitution = WRITTEN (codified single document) + RIGID (requires 2/3 + 3/4 state ratification for amendments)."),

    (9, 2,
     "UK Constitution belongs to which category?\nతెలుగు: UK రాజ్యాంగం ఏ వర్గం?",
     "Written + Rigid",
     "Written + Flexible",
     "Unwritten + Flexible / Unwritten + Flexible (correct)",
     "Unwritten + Rigid",
     "c",
     "UK = UNWRITTEN (uncodified) + FLEXIBLE (Parliament can amend by simple majority since Parliament is sovereign)."),

    (9, 2,
     "Indian Constitution in terms of Rigid vs Flexible?\nతెలుగు: భారత రాజ్యాంగం Rigid/Flexible ఏ వర్గం?",
     "Completely Rigid / పూర్తిగా అనమ్యం",
     "Completely Flexible / పూర్తిగా సౌమ్యం",
     "Partly Rigid, Partly Flexible / పాక్షికంగా (correct)",
     "Cannot be amended / సవరించలేరు",
     "c",
     "Indian Constitution = PARTLY rigid + PARTLY flexible. Article 368 has 3 amendment routes: simple majority + 2/3 majority + 2/3 + state ratification."),

    (9, 3,
     "K.C. Wheare is famous for which book in constitutional scholarship?\nతెలుగు: K.C. Wheare ఏ పుస్తకానికి ప్రసిద్ధులు?",
     "Federal Government / Federal Government",
     "Modern Constitutions / Modern Constitutions (correct)",
     "The Constitution of Liberty / Liberty",
     "Constitutional Government / Constitutional Govt",
     "b",
     "K.C. Wheare's 'Modern Constitutions' (1966) is a landmark work classifying constitutions worldwide. He famously called India 'Quasi-Federal'."),

    (9, 3,
     "What does it mean for a constitution to be 'Supreme'?\nతెలుగు: 'Supreme Constitution' అంటే ఏమిటి?",
     "President can change the Constitution / రాష్ట్రపతి మార్చగలడు",
     "Constitution is supreme over all laws; unconstitutional laws are invalid / రాజ్యాంగం సర్వోన్నతం (correct)",
     "Parliament can change anytime / Parliament ఎప్పుడైనా",
     "Courts can strike down Constitution / కోర్టులు రద్దు చేయవచ్చు",
     "b",
     "Supreme Constitution = the Constitution is HIGHER than ordinary laws. Any law contravening it is invalid (Judicial Review). India and USA = Supreme. UK = Parliament Sovereign instead."),

    (9, 2,
     "In which country does Parliamentary Sovereignty prevail (not Constitutional supremacy)?\nతెలుగు: 'Parliamentary Sovereignty' ఏ దేశంలో?",
     "USA / అమెరికా",
     "India / భారత్",
     "Australia / ఆస్ట్రేలియా",
     "United Kingdom / యూకే (correct)",
     "d",
     "UK has PARLIAMENTARY SOVEREIGNTY — Parliament can pass any law and courts cannot strike it down. India + USA have Constitutional Supremacy instead."),

    (9, 2,
     "Israel and New Zealand constitutions belong to which category?\nతెలుగు: Israel + New Zealand రాజ్యాంగం ఏ వర్గం?",
     "Written + Rigid",
     "Unwritten + Flexible / Unwritten + Flexible (correct)",
     "Written + Flexible",
     "Rigid + Federal",
     "b",
     "Like UK, Israel and New Zealand have UNWRITTEN/UNCODIFIED + FLEXIBLE constitutions — based on Basic Laws, parliamentary statutes, conventions."),

    (9, 3,
     "What are 'Organic Laws' in the constitutional context?\nతెలుగు: 'Organic Laws' అంటే ఏమిటి?",
     "Agriculture-related laws / వ్యవసాయ చట్టాలు",
     "Constitutional amendment laws / సవరణ చట్టాలు",
     "Fundamental laws acting as the constitution / రాజ్యాంగంగా పని చేసే ప్రాథమిక చట్టాలు (correct)",
     "Environmental protection laws / పర్యావరణ చట్టాలు",
     "c",
     "Organic Laws = the foundational/basic laws that effectively function as a constitution in countries without a single codified document (e.g., Israel's Basic Laws)."),

    (9, 2,
     "For ordinary Constitutional amendments under Art.368, what minimum majority is needed? [APPSC Group 2]\nతెలుగు: సవరణకు కనీస మెజారిటీ?",
     "Simple majority / సాధారణ మెజారిటీ",
     "2/3 of present and voting + more than half of total membership / 2/3 + సగం (correct)",
     "3/4 majority + state ratification / 3/4 + రాష్ట్రాల ఆమోదం",
     "Unanimous resolution / ఏకగ్రీవం",
     "b",
     "Article 368 special majority: (a) majority of total membership of each House AND (b) 2/3 of members present and voting. Some amendments also need state ratification.",
     "APPSC"),

    (9, 3,
     "What is special about an 'Evolved Constitution'?\nతెలుగు: 'Evolved Constitution' ప్రత్యేకత?",
     "Written after a revolution / విప్లవం తర్వాత",
     "Written after independence / స్వాతంత్ర్యం తర్వాత",
     "Gradually shaped through customs, statutes, court rulings / సంప్రదాయాలు, చట్టాలు, కోర్టు తీర్పుల ద్వారా క్రమంగా (correct)",
     "Translated from foreign constitutions / విదేశీ నుండి అనువదన",
     "c",
     "Evolved Constitution = developed organically over time through usages, statutes, court decisions (UK is the classic example). Opposite of Enacted (India, USA)."),

    # ══════════════ SECTION 10 — Federalism Deep Dive ══════════════

    (10, 1,
     "How did K.C. Wheare describe the Indian Constitution?\nతెలుగు: K.C. Wheare భారత రాజ్యాంగాన్ని ఏ పదంతో వర్ణించారు?",
     "Federal / Federal",
     "Unitary / Unitary",
     "Quasi-Federal / Quasi-Federal (correct)",
     "Confederate / Confederate",
     "c",
     "K.C. Wheare's classic description: India is a 'Quasi-Federal' state — federal in form but with strong unitary tendencies."),

    (10, 1,
     "Which of the following has a Unitary Constitution?\nతెలుగు: ఏకీకృత రాజ్యాంగం ఉన్న దేశం?",
     "USA / అమెరికా",
     "Australia / ఆస్ట్రేలియా",
     "France / ఫ్రాన్స్ (correct)",
     "Switzerland / స్విట్జర్లాండ్",
     "c",
     "France has a UNITARY system. USA, Australia, Switzerland are all Federal."),

    (10, 1,
     "In USA, where do Residuary Powers reside?\nతెలుగు: USA లో అవశేష అధికారాలు ఎక్కడ?",
     "Federal Government / కేంద్ర ప్రభుత్వం",
     "States or the people / రాష్ట్రాలు లేదా ప్రజలు (correct)",
     "Supreme Court / సుప్రీం కోర్టు",
     "President / అధ్యక్షుడు",
     "b",
     "USA 10th Amendment: 'Powers not delegated to the United States by the Constitution... are reserved to the States respectively, or to the people.' India is opposite — Centre holds residuary powers (Article 248)."),

    (10, 2,
     "Under which Article are Residuary Powers vested in the Centre in India?\nతెలుగు: భారత్‌లో అవశేష అధికారాలు ఏ ఆర్టికల్ ద్వారా కేంద్రానికి?",
     "Article 246 / అధికరణం 246",
     "Article 247 / అధికరణం 247",
     "Article 248 / అధికరణం 248 (correct)",
     "Article 249 / అధికరణం 249",
     "c",
     "Article 248: Residuary Powers (subjects NOT in Union/State/Concurrent lists) belong to PARLIAMENT (Centre). Borrowed from Canada (NOT USA model)."),

    (10, 2,
     "Which scholar described India as 'Federation with strong centralising tendency'?\nతెలుగు: ఎవరు ఈ వాక్యం చెప్పారు?",
     "K.C. Wheare / K.C. వేర్",
     "Paul Appleby / పాల్ ఆపిల్‌బీ",
     "Ivor Jennings / ఐవర్ జెన్నింగ్స్ (correct)",
     "Granville Austin / గ్రాన్‌విల్ ఆస్టిన్",
     "c",
     "Ivor Jennings described India as a 'Federation with strong centralising tendency'. K.C. Wheare's term was 'Quasi-Federal' — both authors highlighted the Centre's dominance."),

    (10, 2,
     "Which of these reflects the Unitary character of the Indian Constitution?\nతెలుగు: భారత రాజ్యాంగంలో ఏకీకృత స్వభావాన్ని చూపే లక్షణం?",
     "Division of Powers (Three Lists) / అధికారాల విభజన",
     "Independent Judiciary / స్వతంత్ర న్యాయ వ్యవస్థ",
     "Residuary Powers to Centre / అవశేష అధికారాలు కేంద్రం (correct)",
     "Bicameral Parliament / ద్విసభా Parliament",
     "c",
     "Residuary Powers to Centre = strong UNITARY feature. Three Lists, Independent Judiciary, Bicameralism are FEDERAL features."),

    (10, 2,
     "Which of the following is essential for a Federal System?\nతెలుగు: సమాఖ్యకు అవసరమైన ముఖ్య పరిస్థితి?",
     "Single party rule / ఒకే పార్టీ పాలన",
     "Constitutional supremacy + Division of Powers / రాజ్యాంగ సర్వోన్నతత + అధికారాల విభజన (correct)",
     "Single citizenship only / ఒకే పౌరసత్వం",
     "Directly elected President / ప్రత్యక్ష అధ్యక్షుడు",
     "b",
     "Federal System essentials: (1) Written Constitution, (2) Constitutional Supremacy, (3) Division of Powers between Centre and States, (4) Independent Judiciary."),

    (10, 3,
     "What did the Supreme Court decide about India's federal character in S.R. Bommai vs UoI (1994)?\nతెలుగు: S.R. Bommai 1994 కేసులో సుప్రీం కోర్టు ఏమి నిర్ణయించింది?",
     "India is fully Unitary / పూర్తిగా Unitary",
     "States are 'satellites' of Centre / రాష్ట్రాలు satellites",
     "Federalism is part of the Basic Structure of the Constitution / సమాఖ్యత Basic Structure లో భాగం (correct)",
     "Federalism can be suspended in emergency / అత్యవసరంలో రద్దు",
     "c",
     "S.R. Bommai vs UoI (1994): SC held that FEDERALISM is part of the BASIC STRUCTURE of the Constitution and cannot be amended away. Limits on Article 356 misuse."),

    (10, 2,
     "Single Citizenship in India is borrowed from which country?\nతెలుగు: ఒకే పౌరసత్వం ఏ దేశం నుండి?",
     "USA / అమెరికా",
     "Australia / ఆస్ట్రేలియా",
     "Canada / కెనడా",
     "UK / యూకే (correct)",
     "d",
     "Single Citizenship borrowed from UK. (USA = Dual Citizenship — federal + state.)"),

    (10, 3,
     "Who identified 'Cooperative Federalism' as a feature of the Indian Constitution?\nతెలుగు: 'Cooperative Federalism' ఎవరు గుర్తించారు?",
     "K.C. Wheare / K.C. వేర్",
     "Ivor Jennings / ఐవర్ జెన్నింగ్స్",
     "Granville Austin / గ్రాన్‌విల్ ఆస్టిన్ (correct)",
     "Paul Appleby / పాల్ ఆపిల్‌బీ",
     "c",
     "Granville Austin identified India's federalism as 'Cooperative Federalism' — Centre and States working in partnership rather than rigid separation."),

    (10, 3,
     "Who appoints the Governor in India — and what character does this reflect?\nతెలుగు: గవర్నర్ నియామకం ఎవరు; ఏ స్వభావం?",
     "State people directly elect — Federal / రాష్ట్ర ప్రజలు; Federal",
     "State legislature elects — Federal / రాష్ట్ర శాసనసభ; Federal",
     "President appoints — Unitary / రాష్ట్రపతి నియామకం; Unitary (correct)",
     "Supreme Court appoints — Judicial / సుప్రీం కోర్టు; Judicial",
     "c",
     "Article 155: Governor is APPOINTED by the President of India (= Centre). This reflects strong UNITARY tilt — states can't pick their own Governor."),

    (10, 2,
     "Key difference between Confederation and Federation?\nతెలుగు: Confederation vs Federation తేడా?",
     "Confederation has written constitution; Federation doesn't / Confederation లిఖిత",
     "Confederation strong centre; Federation strong states / Confederation బలమైన కేంద్రం",
     "Confederation: member states retain independence; Federation: Constitution is supreme / Confederation లో రాష్ట్రాలు స్వతంత్రం (correct)",
     "Federation single citizenship; Confederation dual / Federation ఒకే పౌరసత్వం",
     "c",
     "Confederation = loose alliance; member states keep sovereignty + can secede. Federation = states surrender some sovereignty to Constitution; cannot secede. India = Federation, NOT Confederation."),

    (10, 2,
     "Under Article 249, when can Parliament legislate on State List items?\nతెలుగు: Art.249 ద్వారా Parliament రాష్ట్ర జాబితా పై ఎప్పుడు చట్టం?",
     "By President's Order / రాష్ట్రపతి ఉత్తర్వు",
     "By 2/3 Rajya Sabha resolution citing national interest / రాజ్యసభ 2/3 తీర్మానం (correct)",
     "By Lok Sabha simple majority / Lok Sabha సాధారణ మెజారిటీ",
     "Not possible without state's consent / రాష్ట్ర అనుమతి అవసరం",
     "b",
     "Article 249: If RAJYA SABHA passes a resolution by 2/3 majority citing 'national interest', Parliament can make laws on State List for up to 1 year (renewable)."),

    (10, 3,
     "Why are All India Services considered a Unitary feature? [APPSC Group 2]\nతెలుగు: All India Services Unitary feature ఎందుకు?",
     "Used only by Centre / కేవలం కేంద్రం",
     "Parliament can abolish / Parliament రద్దు చేయగలదు",
     "Centre-controlled but serve in States — central dominance / కేంద్రం నియంత్రణలో; రాష్ట్రాలలో పని (correct)",
     "Need state consent / రాష్ట్ర అనుమతి అవసరం",
     "c",
     "All India Services (IAS, IPS, IFoS) are recruited and controlled by the CENTRE but serve in both Centre and States. Centre can transfer/discipline officers serving in states — strong UNITARY tilt.",
     "APPSC"),

    (10, 3,
     "Which is NOT a Federal Feature of the Indian Constitution? [APPSC PYQ]\nతెలుగు: భారత రాజ్యాంగంలో సమాఖ్య లక్షణం కానిది?",
     "Division of Powers / అధికారాల విభజన",
     "Independent Judiciary / స్వతంత్ర న్యాయ వ్యవస్థ",
     "Bicameralism / ద్విసభ Parliament",
     "Single Citizenship / ఒకే పౌరసత్వం (correct — UNITARY)",
     "d",
     "Single Citizenship is a UNITARY feature (NOT federal). USA has dual citizenship; India copied UK's single. The other three options are all federal features.",
     "APPSC"),
]


# ─────────────────────────────────────────────
#  SEED FUNCTIONS
# ─────────────────────────────────────────────

def _seed_polity_ch3_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
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
        (3, 'Indian_Polity'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True,
                'message': 'Polity Ch3 notes already seeded.'}
    if row and force:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (3, 'Indian_Polity'))
    if use_postgres:
        conn.commit()

    db_exec_fn(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'Indian_Polity', '', 3,
         'రాజ్యాంగం యొక్క ప్రముఖ లక్షణాలు',
         'Salient Features of the Constitution',
         'Ch.3',
         _json.dumps(POLITY_CH3_SECTIONS, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'Polity Ch3 notes seeded!'}


def _seed_polity_ch3_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
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
        (3, 'Indian_Polity'))
    row = cur.fetchone()
    if not row:
        _seed_polity_ch3_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)
        cur = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (3, 'Indian_Polity'))
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
    for mcq in POLITY_CH3_MCQS:
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

    total = len(POLITY_CH3_MCQS)
    return {
        'success': True,
        'message': f'Polity Ch3 MCQs seeded! Total: {total}',
        'inserted': total,
        'easy': easy, 'medium': medium, 'hard': hard,
        'toughest': toughest, 'pyq': pyq
    }
