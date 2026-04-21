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

    # ══════════════════════════════════════════
    # SECTION 0 — విశాలత మరియు మూలాలు
    # ══════════════════════════════════════════

    # Easy
    (0, 1,
     "ప్రపంచంలోనే అతిపెద్ద లిఖిత రాజ్యాంగం ఏ దేశానిది?",
     "అమెరికా", "ఆస్ట్రేలియా", "భారతదేశం", "కెనడా",
     "c",
     "భారత రాజ్యాంగం ప్రపంచంలోనే అతి పెద్ద లిఖిత రాజ్యాంగం. మూలంలో 395 ఆర్టికల్స్, 22 పార్ట్స్, 8 షెడ్యూల్స్ ఉన్నాయి. ఇప్పుడు సవరణల తర్వాత సంఖ్య పెరిగింది."),

    (0, 1,
     "అసలు భారత రాజ్యాంగంలో (1949) ఎన్ని ఆర్టికల్స్ ఉన్నాయి?",
     "448", "395", "460", "350",
     "b",
     "అసలు భారత రాజ్యాంగంలో 395 ఆర్టికల్స్, 22 పార్ట్స్, 8 షెడ్యూల్స్ ఉన్నాయి. సవరణల తర్వాత ప్రస్తుతం దాదాపు 448 ఆర్టికల్స్ మరియు 12 షెడ్యూల్స్."),

    (0, 1,
     "భారత రాజ్యాంగం తయారీలో అతిపెద్ద ఏకైక స్రోతం ఏది?",
     "అమెరికా రాజ్యాంగం", "బ్రిటన్ రాజ్యాంగం",
     "Government of India Act 1935", "ఐర్లాండ్ రాజ్యాంగం",
     "c",
     "Government of India Act 1935 భారత రాజ్యాంగం తయారీలో అతిపెద్ద స్రోతం. దాదాపు 250 నిబంధనలు ఈ చట్టం నుండి స్వీకరించారు. అందుకే దీన్ని 'రాజ్యాంగం యొక్క జనక చట్టం' అంటారు."),

    # Moderate
    (0, 2,
     "భారత రాజ్యాంగ అసలు రూపంలో పార్ట్స్ మరియు షెడ్యూల్స్ ఎన్ని?",
     "25 Parts, 12 Schedules", "22 Parts, 8 Schedules",
     "22 Parts, 12 Schedules", "20 Parts, 10 Schedules",
     "b",
     "అసలు రాజ్యాంగం (నవంబర్ 26, 1949): 395 Articles, 22 Parts, 8 Schedules. సవరణల తర్వాత: ~448 Articles, 25 Parts, 12 Schedules. రెండు సెట్ల సంఖ్యలు పరీక్షలలో తరచుగా వస్తాయి."),

    (0, 2,
     "Government of India Act 1935 నుండి భారత రాజ్యాంగంలో దాదాపు ఎన్ని నిబంధనలు చేర్చారు?",
     "100", "150", "250", "350",
     "c",
     "GoI Act 1935 నుండి దాదాపు 250 నిబంధనలు భారత రాజ్యాంగంలో చేర్చారు. అందుకే ఇది 'Single Biggest Source'. ఫెడరల్ నిర్మాణం, గవర్నర్ పదవి, ఎమర్జెన్సీ నిబంధనలు, UPSC వంటివి అన్నీ ఇందులో ఉన్నాయి."),

    # Tough
    (0, 3,
     "కింది వాటిలో అసలు భారత రాజ్యాంగంపై సరైన వాటికి చిహ్నం ఉంది — తప్పు ఏది?\n(1) 395 Articles\n(2) 22 Parts\n(3) 12 Schedules\n(4) GoI Act 1935 = Single Biggest Source",
     "3 తప్పు — అసలు 8 Schedules ఉన్నాయి",
     "1 తప్పు — అసలు 448 Articles ఉన్నాయి",
     "2 తప్పు — అసలు 25 Parts ఉన్నాయి",
     "4 తప్పు — USA రాజ్యాంగం అతిపెద్ద స్రోతం",
     "a",
     "అసలు (1949) రాజ్యాంగంలో 8 Schedules మాత్రమే ఉన్నాయి. 12 Schedules = సవరణల తర్వాత. 1 (395 Articles), 2 (22 Parts), 4 (GoI Act 1935 = biggest source) అన్నీ సరైనవి."),

    # Toughest
    (0, 4,
     "అభికథనం-కారణం సరైనవా? / Assertion (A): Indian Constitution is called the longest written constitution in the world.\nReason (R): It originally contained 395 Articles, 22 Parts, and 8 Schedules, and was influenced by the Government of India Act 1935 which provided approximately 250 provisions.",
     "A మరియు R రెండూ సరైనవి, R అనేది A కి సరైన వివరణ",
     "A మరియు R రెండూ సరైనవి, కానీ R వివరణ కాదు",
     "A సరైనది, R తప్పు",
     "A తప్పు, R సరైనది",
     "a",
     "భారత రాజ్యాంగం ప్రపంచంలోనే అతి పెద్ద లిఖిత రాజ్యాంగం (A — true). మూలంలో 395 Articles, 22 Parts, 8 Schedules, GoI Act 1935 నుండి 250 నిబంధనలు (R — true and explains why it is so large)."),

    # PYQ — APPSC
    (0, 2,
     "ప్రపంచంలోనే అతి పెద్ద లిఖిత రాజ్యాంగం ఏది? [APPSC Group 2]",
     "USA రాజ్యాంగం", "భారత రాజ్యాంగం",
     "కెనడా రాజ్యాంగం", "ఆస్ట్రేలియా రాజ్యాంగం",
     "b",
     "భారత రాజ్యాంగం ప్రపంచంలోనే అతిపెద్ద లిఖిత రాజ్యాంగం. ఇది మూలంలో 395 ఆర్టికల్స్ తో ఆరంభమైంది. USA రాజ్యాంగం చాలా చిన్నది — మూలంలో 7 ఆర్టికల్స్ మాత్రమే.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 1 — వివిధ దేశాల స్రోతాలు
    # ══════════════════════════════════════════

    # Easy
    (1, 1,
     "భారత రాజ్యాంగంలో మూల హక్కులు (Fundamental Rights) ఏ దేశం నుండి స్వీకరించారు?",
     "UK", "ఐర్లాండ్", "USA", "కెనడా",
     "c",
     "USA రాజ్యాంగం నుండి భారత రాజ్యాంగంలో మూల హక్కులు (Fundamental Rights), న్యాయ సమీక్ష (Judicial Review), మరియు స్వతంత్ర న్యాయవ్యవస్థ స్వీకరించారు."),

    (1, 1,
     "ఆదేశిక సూత్రాలు (Directive Principles of State Policy — DPSP) ఏ దేశం నుండి స్వీకరించారు?",
     "UK", "ఆస్ట్రేలియా", "USA", "ఐర్లాండ్",
     "d",
     "DPSP (ఆదేశిక సూత్రాలు) ఐర్లాండ్ రాజ్యాంగం నుండి స్వీకరించారు. అలాగే రాజ్యసభకు నామినేషన్ పద్ధతి, రాష్ట్రపతి ఎన్నిక పద్ధతి కూడా ఐర్లాండ్ నుండే వచ్చాయి."),

    (1, 1,
     "భారత రాజ్యాంగంలో పార్లమెంటరీ పాలన విధానం (Parliamentary System) ఏ దేశం నుండి స్వీకరించారు?",
     "USA", "కెనడా", "UK", "ఫ్రాన్స్",
     "c",
     "UK (Britain) నుండి భారత రాజ్యాంగంలో పార్లమెంటరీ పాలన విధానం, Cabinet System, Rule of Law, Single Citizenship, Bicameralism స్వీకరించారు. Westminster Model = UK Parliament."),

    # Moderate
    (1, 2,
     "కింది జంటలు సరిగ్గా జోడించబడ్డాయా? తప్పు ఏది?\n(P) USA — Fundamental Rights\n(Q) Ireland — DPSP\n(R) Canada — Concurrent List\n(S) Australia — Joint Sitting of Parliament",
     "P మరియు Q సరైనవే; R తప్పు — Concurrent List = Australia నుండి",
     "Q మరియు R తప్పు",
     "R మాత్రమే తప్పు — Concurrent List = Canada నుండి",
     "అన్నీ సరైనవే",
     "a",
     "R తప్పు — Concurrent List (ఉమ్మడి జాబితా) ఆస్ట్రేలియా నుండి వచ్చింది, కెనడా నుండి కాదు. కెనడా నుండి వచ్చింది: సమాఖ్య + బలమైన కేంద్రం, అవశేష అధికారాలు కేంద్రానికి. S — Joint Sitting = Australia ✓"),

    (1, 2,
     "కింది వాటిలో UK నుండి భారత రాజ్యాంగంలో స్వీకరించిన అంశాలు ఏవి?\n(1) Cabinet System\n(2) Rule of Law\n(3) Judicial Review\n(4) Single Citizenship",
     "1, 2 మరియు 4 మాత్రమే", "1 మరియు 3 మాత్రమే",
     "1, 2, 3 మరియు 4 అన్నీ", "2 మరియు 4 మాత్రమే",
     "a",
     "3 తప్పు — Judicial Review USA నుండి వచ్చింది, UK నుండి కాదు. UK నుండి వచ్చినవి: Cabinet System (1), Rule of Law (2), Single Citizenship (4), Bicameralism, Speaker విధులు."),

    # Tough
    (1, 3,
     "అత్యవసర పరిస్థితిలో మూల హక్కుల నిలిపివేత (Suspension of Fundamental Rights during Emergency) ఏ దేశం నుండి స్వీకరించారు?",
     "USA", "USSR", "France", "Germany (Weimar Constitution)",
     "d",
     "జర్మనీ వైమర్ రాజ్యాంగం (Weimar Constitution) నుండి అత్యవసర పరిస్థితిలో మూల హక్కుల నిలిపివేత స్వీకరించారు. USSR నుండి Fundamental Duties వచ్చాయి. France నుండి Republic, Liberty, Equality, Fraternity వచ్చాయి."),

    # Toughest
    (1, 4,
     "కింది అన్నీ సరైన జంటలు ఏవి? / తప్పు జంటలు ఏవి?\n(1) South Africa — Amendment Procedure, Election of RS members\n(2) Japan — Procedure Established by Law\n(3) USSR — DPSP\n(4) France — Republic, Liberty, Equality, Fraternity",
     "1, 2 మరియు 4 సరైనవి; 3 తప్పు",
     "1, 2, 3 మరియు 4 అన్నీ సరైనవి",
     "2 మరియు 3 తప్పు",
     "1 మరియు 4 మాత్రమే సరైనవి",
     "a",
     "3 తప్పు — DPSP వచ్చింది ఐర్లాండ్ నుండి, USSR నుండి కాదు. USSR నుండి Fundamental Duties వచ్చాయి. 1 (South Africa ✓), 2 (Japan ✓), 4 (France ✓) అన్నీ సరైనవి."),

    # PYQ — UPSC
    (1, 2,
     "కింది వాటిలో ఏ దేశం DPSPకి స్ఫూర్తి? / Which of the following countries inspired the Directive Principles of State Policy in the Indian Constitution? [UPSC Style]",
     "United States of America", "United Kingdom",
     "Canada", "Ireland",
     "d",
     "Directive Principles of State Policy (DPSP) ఐర్లాండ్ రాజ్యాంగం నుండి స్వీకరించారు. Ireland కూడా ఒక అభివృద్ధి చెందుతున్న దేశం కావడం వల్ల CA దీన్ని ఎంచుకుంది. USA నుండి Fundamental Rights వచ్చాయి.",
     "UPSC"),

    # ══════════════════════════════════════════
    # SECTION 2 — సమాఖ్య వ్యవస్థ — కేంద్ర పక్షపాతంతో
    # ══════════════════════════════════════════

    # Easy
    (2, 1,
     "భారత రాజ్యాంగంలో అవశేష అధికారాలు (Residuary Powers) ఎవరికి ఉంటాయి?",
     "రాష్ట్ర ప్రభుత్వాలకు", "సుప్రీం కోర్టుకు",
     "కేంద్ర ప్రభుత్వానికి (Union)", "ఎన్నికల సంఘానికి",
     "c",
     "భారత రాజ్యాంగంలో అవశేష అధికారాలు (Residuary Powers) కేంద్ర ప్రభుత్వానికి (Union of India) ఉంటాయి. ఇది USA కి భిన్నంగా ఉంది — USA లో అవశేష అధికారాలు రాష్ట్రాలకు. ఈ లక్షణం కెనడా నుండి వచ్చింది."),

    (2, 1,
     "భారతదేశాన్ని 'Quasi-Federal' రాజ్యమని ఎవరు అన్నారు?",
     "Dr. B.R. Ambedkar", "K.C. Wheare",
     "Jawaharlal Nehru", "Granville Austin",
     "b",
     "K.C. Wheare భారతదేశాన్ని 'Quasi-Federal' లేదా 'Federal in form but Unitary in spirit' అని అన్నారు. Granville Austin 'Cooperative Federalism' అన్నారు. భారత రాజ్యాంగం సమాఖ్య మరియు ఏకీకృత లక్షణాలు రెండూ కలిగి ఉంది."),

    (2, 1,
     "భారత రాజ్యాంగంలో ఒకే పౌరసత్వం (Single Citizenship) ఉంది — ఇది ఏ లక్షణం?",
     "సమాఖ్య లక్షణం (Federal Feature)",
     "ఏకీకృత లక్షణం (Unitary Feature)",
     "పార్లమెంటరీ లక్షణం",
     "న్యాయపర లక్షణం",
     "b",
     "ఒకే పౌరసత్వం (Single Citizenship) భారత రాజ్యాంగం యొక్క ఏకీకృత లక్షణం (Unitary Feature). USA లో రెండు పౌరసత్వాలు ఉంటాయి — Federal + State. భారత్ లో కేవలం భారత పౌరత్వం మాత్రమే."),

    # Moderate
    (2, 2,
     "కింది వాటిలో భారత రాజ్యాంగం యొక్క సమాఖ్య లక్షణాలు (Federal Features) ఏవి?\n(1) లిఖిత రాజ్యాంగం\n(2) అవశేష అధికారాలు కేంద్రానికి\n(3) అధికారాల విభజన (3 Lists)\n(4) ఒకే పౌరసత్వం",
     "1 మరియు 3 మాత్రమే", "1, 2 మరియు 3",
     "1, 3 మరియు 4", "2 మరియు 4 మాత్రమే",
     "a",
     "2 మరియు 4 — ఏకీకృత లక్షణాలు (Unitary): అవశేష అధికారాలు కేంద్రానికి (2), ఒకే పౌరసత్వం (4). సమాఖ్య లక్షణాలు: లిఖిత రాజ్యాంగం (1), 3 జాబితాల ద్వారా అధికారాల విభజన (3)."),

    (2, 2,
     "కింది వాటిలో ఏకీకృత లక్షణాలు (Unitary Features) ఏవి?\n(1) గవర్నర్ నియామకం కేంద్రం చేయడం\n(2) రాజ్యసభలో అన్ని రాష్ట్రాలకు సమాన ప్రాతినిధ్యం\n(3) అఖిల భారత సేవలు (All India Services)\n(4) ఏకీకృత న్యాయవ్యవస్థ",
     "1, 3 మరియు 4 మాత్రమే", "1, 2 మరియు 3",
     "2 మరియు 4 మాత్రమే", "1, 2, 3 మరియు 4 అన్నీ",
     "a",
     "2 తప్పు — భారతదేశంలో రాజ్యసభలో అన్ని రాష్ట్రాలకు సమాన ప్రాతినిధ్యం లేదు; జనాభా ఆధారంగా ప్రాతినిధ్యం ఉంటుంది. (USA లో Senate లో సమాన ప్రాతినిధ్యం ఉంటుంది). 1, 3, 4 — నిజమైన ఏకీకృత లక్షణాలు."),

    # Tough
    (2, 3,
     "USA మరియు భారత్ ఫెడరల్ వ్యవస్థల మధ్య ముఖ్యమైన తేడా ఏది?\n(Key difference between Indian and American Federalism)",
     "భారత్ లో లిఖిత రాజ్యాంగం, USA లో లేదు",
     "USA లో అవశేష అధికారాలు రాష్ట్రాలకు; భారత్ లో కేంద్రానికి",
     "భారత్ లో ద్విసభా పార్లమెంట్, USA లో ఏకసభ",
     "USA లో న్యాయ సమీక్ష లేదు; భారత్ లో ఉంది",
     "b",
     "USA లో అవశేష అధికారాలు రాష్ట్రాలకు (10th Amendment); భారత్ లో కేంద్రానికి (Article 248). ఇది ఒక ముఖ్యమైన తేడా. రెండు దేశాలకూ లిఖిత రాజ్యాంగం, ద్విసభా పార్లమెంట్, Judicial Review ఉన్నాయి."),

    # Toughest
    (2, 4,
     "భారత రాజ్యాంగం Rigid or Flexible గురించి కింది వాటిలో సరైనది?\n(Regarding rigid/flexible nature of Indian Constitution)",
     "పూర్తిగా అనమ్యం (Completely Rigid) — అన్ని సవరణలకు 2/3 + రాష్ట్రాల ఆమోదం అవసరం",
     "పూర్తిగా అనమ్యం (Completely Flexible) — అన్ని సవరణలు సాధారణ మెజారిటీతో",
     "పాక్షికంగా అనమ్యం, పాక్షికంగా అనమ్యం (Partly Rigid, Partly Flexible)",
     "సవరణలు పూర్తిగా నిషిద్ధం",
     "c",
     "భారత రాజ్యాంగం Partly Rigid, Partly Flexible. కొన్ని అంశాలకు (ఉదా: FR) 2/3 మెజారిటీ + రాష్ట్రాల ఆమోదం అవసరం. కొన్నిటికి (ఉదా: Citizenship నిబంధనలు) సాధారణ మెజారిటీ సరిపోతుంది."),

    # PYQ — APPSC
    (2, 2,
     "భారత సమాఖ్య వ్యవస్థను 'Quasi-Federal' అని ఎవరు అన్నారు? [APPSC Group 2]",
     "Dr. B.R. Ambedkar", "Granville Austin",
     "K.C. Wheare", "Jawaharlal Nehru",
     "c",
     "K.C. Wheare భారత రాజ్యాంగాన్ని 'Quasi-Federal' అని అన్నారు — సమాఖ్య రూపంలో కానీ ఏకీకృత స్ఫూర్తితో ఉంది. Granville Austin దీన్ని 'Cooperative Federalism' అన్నారు. ఇది APPSC పరీక్షలలో తరచుగా వచ్చే ప్రశ్న.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 3 — పార్లమెంటరీ పాలన విధానం
    # ══════════════════════════════════════════

    # Easy
    (3, 1,
     "భారత రాజ్యాంగంలో రాష్ట్రపతి (President) ఏ రకమైన అధినేత?",
     "నిజమైన కార్యనిర్వాహకుడు / Real Executive",
     "నామమాత్రపు / రాజ్యాంగపు అధినేత / Nominal / Constitutional Head",
     "స్వతంత్ర పాలకుడు / Independent Ruler",
     "పార్లమెంట్ అధ్యక్షుడు / Head of Parliament",
     "b",
     "భారత రాష్ట్రపతి నామమాత్రపు అధినేత (Nominal / Constitutional Head). నిజమైన కార్యనిర్వాహక అధికారం ప్రధానమంత్రి నేతృత్వంలోని మంత్రి మండలికి ఉంటుంది."),

    (3, 1,
     "భారత పార్లమెంటరీ పద్ధతిలో మంత్రి మండలి ఏ సభకు సమష్టి బాధ్యత వహిస్తుంది?",
     "రాజ్యసభకు (Rajya Sabha)", "లోక్ సభకు (Lok Sabha)",
     "రాష్ట్రపతికి", "సుప్రీం కోర్టుకు",
     "b",
     "మంత్రి మండలి (Council of Ministers) లోక్ సభకు సమష్టి బాధ్యత వహిస్తుంది (Collective Responsibility to Lok Sabha). ఆర్టికల్ 75(3) ప్రకారం. ఇది Westminster Model యొక్క ముఖ్య లక్షణం."),

    (3, 1,
     "పార్లమెంటరీ పద్ధతి (Parliamentary System) ఏ దేశం నుండి స్వీకరించారు?",
     "USA", "ఆస్ట్రేలియా", "UK (బ్రిటన్)", "కెనడా",
     "c",
     "భారత పార్లమెంటరీ పద్ధతి UK Westminster Model ఆధారంగా. ప్రధానమంత్రి = నిజమైన కార్యనిర్వాహకుడు, రాష్ట్రపతి = నామమాత్రపు అధినేత. ఇది Cabinet System, Rule of Law తో కూడా UK నుండే వచ్చింది."),

    # Moderate
    (3, 2,
     "పార్లమెంటరీ పద్ధతి మరియు అధ్యక్ష పద్ధతి (Presidential) మధ్య ముఖ్య తేడా ఏమిటి?",
     "పార్లమెంటరీ లో అధ్యక్షుడు నిజమైన కార్యనిర్వాహకుడు",
     "అధ్యక్ష పద్ధతిలో కార్యనిర్వాహకుడు శాసనసభకు బాధ్యుడు",
     "పార్లమెంటరీ లో ప్రధానమంత్రి లోక్ సభకు బాధ్యుడు; అధ్యక్ష పద్ధతిలో అధ్యక్షుడు Congress కు స్వతంత్రుడు",
     "రెండింటిలోనూ తేడా లేదు",
     "c",
     "పార్లమెంటరీ: PM మరియు మంత్రి మండలి Lok Sabha కు బాధ్యులు. అధ్యక్ష పద్ధతి (USA): President Congress కు నేరుగా బాధ్యత వహించడు — Separation of Powers. భారత్ పార్లమెంటరీ పద్ధతి ఎంచుకున్నది బాధ్యత మరియు స్థిరత్వం రెండూ అందిస్తుందని."),

    (3, 2,
     "భారత రాజ్యాంగంలో ప్రధానమంత్రి పదవి (Office of Prime Minister) ఏ ఆర్టికల్ లో పేర్కొన్నారు?",
     "ఆర్టికల్ 52", "ఆర్టికల్ 53",
     "ఆర్టికల్ 74 మరియు 75", "ఆర్టికల్ 79",
     "c",
     "ఆర్టికల్ 74 — రాష్ట్రపతికి సహాయపడటానికి, సలహా ఇవ్వడానికి మంత్రి మండలి ఉంటుంది. ఆర్టికల్ 75 — ప్రధానమంత్రి నియామకం, మంత్రుల నియామకం, మంత్రి మండలి లోక్ సభకు సమష్టి బాధ్యత. Article 52 = రాష్ట్రపతి పదవి."),

    # Tough
    (3, 3,
     "అవిశ్వాస తీర్మానం (No-Confidence Motion) ఎవరికి వ్యతిరేకంగా పెట్టవచ్చు?",
     "రాష్ట్రపతి", "మంత్రి మండలికి (Council of Ministers)",
     "సుప్రీం కోర్టు జడ్జికి", "ఉపరాష్ట్రపతికి",
     "b",
     "అవిశ్వాస తీర్మానం (Vote of No-Confidence) మంత్రి మండలి మొత్తానికి వ్యతిరేకంగా పెట్టవచ్చు. ఇది లోక్ సభలో మాత్రమే పెట్టవచ్చు. ఆమోదమైతే మంత్రి మండలి అంతా రాజీనామా చేయాలి."),

    # Toughest
    (3, 4,
     "భారత పార్లమెంటరీ పద్ధతి UK పద్ధతి నుండి ఏ విధంగా భిన్నంగా ఉంది?\n(How Indian Parliamentary system differs from UK Parliament)",
     "భారత్ లో PM నిజమైన కార్యనిర్వాహకుడు; UK లో రాజు/రాణి నిజమైన కార్యనిర్వాహకుడు",
     "భారత్ లో రాష్ట్రపతి రాజ్యాంగాత్మక నిర్బంధాలకు లోబడి ఉంటాడు; UK లో Parliament Sovereign",
     "భారత్ లో Judicial Review ఉంది; UK లో Parliament Sovereignty — Parliament చట్టాలను న్యాయస్థానాలు రద్దు చేయలేవు",
     "భారత్ లో PM ను రాజ్యసభ తొలగిస్తుంది; UK లో House of Lords తొలగిస్తుంది",
     "c",
     "భారత్ లో Judicial Review ఉంది — రాజ్యాంగ విరుద్ధ చట్టాలను సుప్రీం కోర్టు రద్దు చేయగలదు. UK లో Parliament Sovereignty ఉంది — Parliament చేసిన చట్టాలను న్యాయస్థానాలు రద్దు చేయలేవు. ఇది ఒక ముఖ్యమైన తేడా."),

    # PYQ — APPSC
    (3, 2,
     "భారత రాజ్యాంగంలో మంత్రి మండలి ఏ సభకు సమష్టి బాధ్యత వహిస్తుంది? [APPSC Group 2]",
     "రాజ్యసభకు", "లోక్ సభకు",
     "రాష్ట్రపతికి", "సుప్రీం కోర్టుకు",
     "b",
     "ఆర్టికల్ 75(3) ప్రకారం మంత్రి మండలి లోక్ సభకు సమష్టి బాధ్యత వహిస్తుంది. ఇది భారత పార్లమెంటరీ పద్ధతి యొక్క మూల సూత్రం — Westminster Model నుండి వచ్చింది. APPSC Group 2 లో ఇది తరచుగా వస్తుంది.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 4 — మూల హక్కులు మరియు ఆదేశిక సూత్రాలు (Bilingual)
    # ══════════════════════════════════════════

    # Easy — Bilingual
    (4, 1,
     "మూల హక్కులు (Fundamental Rights) భారత రాజ్యాంగంలో ఏ భాగంలో ఉన్నాయి?\n(In which Part of the Indian Constitution are Fundamental Rights?)",
     "భాగం II / Part II", "భాగం III / Part III",
     "భాగం IV / Part IV", "భాగం V / Part V",
     "b",
     "మూల హక్కులు (Fundamental Rights) భాగం III (Part III), ఆర్టికల్ 12–35 లో ఉన్నాయి. USA రాజ్యాంగం నుండి స్వీకరించారు. వీటిని న్యాయస్థానాల ద్వారా అమలు చేయించుకోవచ్చు (Justiciable)."),

    (4, 1,
     "ఆదేశిక సూత్రాలు (DPSP) భారత రాజ్యాంగంలో ఏ భాగంలో ఉన్నాయి?\n(In which Part of the Indian Constitution are DPSPs?)",
     "భాగం III / Part III", "భాగం IV-A / Part IV-A",
     "భాగం IV / Part IV", "భాగం V / Part V",
     "c",
     "ఆదేశిక సూత్రాలు (DPSP) భాగం IV (Part IV), ఆర్టికల్ 36–51 లో ఉన్నాయి. ఐర్లాండ్ రాజ్యాంగం నుండి స్వీకరించారు. వీటిని న్యాయస్థానాల్లో అమలు చేయించుకోలేరు (Non-Justiciable)."),

    # Moderate — Bilingual
    (4, 2,
     "మూల హక్కులు (FR) మరియు ఆదేశిక సూత్రాలు (DPSP) మధ్య ముఖ్య తేడా ఏమిటి?\n(Key difference between Fundamental Rights and DPSP)",
     "FR = Non-Justiciable; DPSP = Justiciable",
     "FR = Justiciable (న్యాయపర); DPSP = Non-Justiciable (న్యాయేతర)",
     "FR Part IV లో; DPSP Part III లో",
     "FR = Ireland నుండి; DPSP = USA నుండి",
     "b",
     "FR = Justiciable — న్యాయస్థానాల్లో అమలు చేయించుకోవచ్చు. DPSP = Non-Justiciable — న్యాయస్థానాల్లో అమలు చేయించుకోలేరు, కానీ పాలనలో మూలభూతం. FR = Part III, USA. DPSP = Part IV, Ireland."),

    (4, 2,
     "కింది వాటిలో DPSP గురించి సరైనవి ఏవి?\n(1) Part IV లో ఉన్నాయి\n(2) Ireland నుండి స్వీకరించారు\n(3) Justiciable — న్యాయస్థానాల్లో అమలు చేయవచ్చు\n(4) ఆర్టికల్ 36–51 లో ఉన్నాయి",
     "1, 2 మరియు 4 మాత్రమే / 1, 2 and 4 only",
     "1, 2, 3 మరియు 4 అన్నీ / All",
     "2 మరియు 3 మాత్రమే / 2 and 3 only",
     "3 మరియు 4 మాత్రమే / 3 and 4 only",
     "a",
     "3 తప్పు — DPSP Non-Justiciable. న్యాయస్థానాల్లో అమలు చేయించుకోలేరు. కానీ రాజ్యం పాటించాలి. 1 (Part IV ✓), 2 (Ireland ✓), 4 (Art 36-51 ✓)."),

    # Tough — Bilingual
    (4, 3,
     "Granville Austin FR మరియు DPSP ను ఏమని వర్ణించారు?\n(How did Granville Austin describe FRs and DPSPs?)",
     "రాజ్యాంగం యొక్క హృదయం మరియు ఆత్మ / Heart and Soul of the Constitution",
     "రాజ్యాంగంలో ఒక చక్రం యొక్క రెండు చక్రాలు / Two wheels of a chariot",
     "రాజ్యాంగంలో రెండు విరుద్ధ అంశాలు / Two contradictory elements",
     "Conscience of the Constitution (రాజ్యాంగ అంతర్మనస్సు)",
     "a",
     "Granville Austin FR మరియు DPSP ని 'రాజ్యాంగం యొక్క హృదయం మరియు ఆత్మ (Conscience of the Constitution)' అన్నారు. రెండూ కలిసి ఒక 'సమాజ విప్లవ పత్రం (Social Revolutionary Document)' అని అన్నారు."),

    # Toughest — Bilingual
    (4, 4,
     "Assertion (A): Fundamental Rights are justiciable but Directive Principles are not.\nReason (R): DPSPs are ideals and objectives for the state to pursue, but courts cannot enforce them against the government like Fundamental Rights.\n(రెండూ నిజమేనా? R అనేది A కి వివరణా?)",
     "A మరియు R రెండూ సరైనవి, R అనేది A కి సరైన వివరణ / Both correct, R explains A",
     "A మరియు R రెండూ సరైనవి, కానీ R వివరణ కాదు / Both correct, R doesn't explain",
     "A సరైనది, R తప్పు / A correct, R wrong",
     "A తప్పు, R సరైనది / A wrong, R correct",
     "a",
     "FR = Justiciable (A — correct). DPSP పాలన లక్ష్యాలు, courts అమలు చేయలేవు — అయితే రాజ్యం అనుసరించాలి (R — correct, explains A). ఇది పరీక్షలలో తరచుగా వచ్చే Assertion-Reason ప్రశ్న."),

    # PYQ — UPSC Bilingual
    (4, 2,
     "DPSPలు రాజ్యాంగంలో ఏ భాగంలో? / Which Part and Articles of the Indian Constitution deal with Directive Principles of State Policy? [UPSC Style]",
     "Part III, Articles 12-35",
     "Part IV, Articles 36-51",
     "Part IV-A, Articles 51A",
     "Part V, Articles 52-78",
     "b",
     "DPSP = Part IV (భాగం IV), Articles 36–51. ఇది ఐర్లాండ్ రాజ్యాంగం నుండి స్వీకరించారు. Part III, Articles 12-35 = Fundamental Rights. Part IV-A, Article 51A = Fundamental Duties.",
     "UPSC"),

    # PYQ — APPSC Bilingual
    (4, 2,
     "మూల హక్కులు ఏ దేశం రాజ్యాంగం నుండి స్వీకరించారు? [APPSC Group 2]",
     "UK", "Ireland", "USA", "Canada",
     "c",
     "మూల హక్కులు (Fundamental Rights) USA రాజ్యాంగం నుండి స్వీకరించారు. DPSP = Ireland. Fundamental Duties = USSR. Amendment Procedure = South Africa. ఇది APPSC Group 2 లో తరచుగా వచ్చే ప్రశ్న.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 5 — మౌలిక విధులు (Bilingual)
    # ══════════════════════════════════════════

    # Easy — Bilingual
    (5, 1,
     "మౌలిక విధులు (Fundamental Duties) భారత రాజ్యాంగంలో ఏ ఆర్టికల్ లో ఉన్నాయి?\n(In which Article are Fundamental Duties mentioned?)",
     "ఆర్టికల్ 51 / Article 51",
     "ఆర్టికల్ 51A / Article 51A",
     "ఆర్టికల్ 12 / Article 12",
     "ఆర్టికల్ 36 / Article 36",
     "b",
     "మౌలిక విధులు (Fundamental Duties) Article 51A లో ఉన్నాయి. ఇవి Part IV-A లో ఉన్నాయి. 42వ రాజ్యాంగ సవరణ 1976 ద్వారా చేర్చారు."),

    (5, 1,
     "మొట్టమొదట మౌలిక విధులు ఏ రాజ్యాంగ సవరణ ద్వారా చేర్చారు?\n(Which Constitutional Amendment first added Fundamental Duties?)",
     "40వ సవరణ 1976 / 40th Amendment 1976",
     "42వ సవరణ 1976 / 42nd Amendment 1976",
     "44వ సవరణ 1978 / 44th Amendment 1978",
     "86వ సవరణ 2002 / 86th Amendment 2002",
     "b",
     "42వ రాజ్యాంగ సవరణ 1976 (Indira Gandhi ప్రభుత్వం) — మొదట 10 మౌలిక విధులు చేర్చారు. స్వరణ్ సింగ్ కమిటీ సిఫారసుపై. USSR రాజ్యాంగం ఇందుకు స్ఫూర్తి."),

    # Moderate — Bilingual
    (5, 2,
     "86వ రాజ్యాంగ సవరణ 2002 ద్వారా చేర్చిన 11వ మౌలిక విధి ఏమిటి?\n(What is the 11th Fundamental Duty added by 86th Amendment 2002?)",
     "జాతీయ పతాకాన్ని గౌరవించడం / Respect national flag",
     "శాస్త్రీయ దృష్టి అభివృద్ధి / Develop scientific temper",
     "6–14 సంవత్సరాల పిల్లలకు విద్య అందించడం తల్లిదండ్రులు / Parents to provide education to children aged 6-14",
     "ప్రజా ఆస్తిని కాపాడడం / Protect public property",
     "c",
     "86వ రాజ్యాంగ సవరణ 2002 — 11వ మౌలిక విధి: 6–14 సంవత్సరాల మధ్య పిల్లలకు విద్యా అవకాశం కల్పించడం తల్లిదండ్రులు / సంరక్షకుల విధి. ఇది Right to Education (RTE) తో పాటు వచ్చింది."),

    (5, 2,
     "కింది వాటిలో మౌలిక విధుల గురించి సరైనవి ఏవి?\n(1) 42వ సవరణ 1976 — మొదట 10 విధులు\n(2) 86వ సవరణ 2002 — 11వ విధి చేర్చారు\n(3) Justiciable — న్యాయస్థానాల్లో అమలు చేయవచ్చు\n(4) USSR నుండి స్ఫూర్తి",
     "1, 2 మరియు 4 మాత్రమే / 1, 2 and 4 only",
     "1, 2, 3 మరియు 4 అన్నీ / All",
     "2 మరియు 3 మాత్రమే / 2 and 3 only",
     "1 మరియు 4 మాత్రమే / 1 and 4 only",
     "a",
     "3 తప్పు — మౌలిక విధులు Non-Justiciable. న్యాయస్థానాల్లో నేరుగా అమలు చేయించుకోలేరు. 1 (42nd 1976 — 10 duties ✓), 2 (86th 2002 — 11th duty ✓), 4 (USSR ✓)."),

    # Tough — Bilingual
    (5, 3,
     "మౌలిక విధుల కోసం సిఫారసు చేసిన కమిటీ ఏది?\n(Which Committee recommended the addition of Fundamental Duties?)",
     "బల్వంత్ రాయ్ మెహతా కమిటీ / Balwant Rai Mehta Committee",
     "స్వరణ్ సింగ్ కమిటీ / Swaran Singh Committee",
     "L.M. సింఘ్వి కమిటీ / L.M. Singhvi Committee",
     "అశోక్ మెహతా కమిటీ / Ashok Mehta Committee",
     "b",
     "స్వరణ్ సింగ్ కమిటీ (Swaran Singh Committee) సిఫారసుపై మౌలిక విధులను 42వ సవరణ 1976 ద్వారా చేర్చారు. బల్వంత్ రాయ్ మెహతా = పంచాయతీ రాజ్ కమిటీ. L.M. Singhvi = పంచాయతీ రాజ్ రాజ్యాంగ హోదా."),

    # Toughest — Bilingual
    (5, 4,
     "కింది జంటలు అన్నీ సరైనవేనా?\n(1) 42వ సవరణ 1976 — 10 మౌలిక విధులు చేర్చారు\n(2) 86వ సవరణ 2002 — 11వ విధి (6–14 పిల్లలకు విద్య)\n(3) మౌలిక విధులు Article 51 లో ఉన్నాయి\n(4) స్వరణ్ సింగ్ కమిటీ సిఫారసు",
     "1, 2 మరియు 4 మాత్రమే సరైనవి / 1, 2 and 4 correct",
     "1, 2, 3 మరియు 4 అన్నీ సరైనవి / All correct",
     "2 మరియు 3 మాత్రమే సరైనవి / 2 and 3 only",
     "3 మరియు 4 తప్పు / 3 and 4 wrong",
     "a",
     "3 తప్పు — మౌలిక విధులు Article 51A లో, Article 51 లో కాదు. Article 51 = International Peace (DPSP). 1 (42nd 1976 ✓), 2 (86th 2002 ✓), 4 (Swaran Singh Committee ✓)."),

    # PYQ — APPSC Bilingual
    (5, 2,
     "మొదట ఎన్ని మౌలిక విధులు 42వ రాజ్యాంగ సవరణ 1976 ద్వారా చేర్చారు? [APPSC Group 2]",
     "8", "10", "11", "12",
     "b",
     "42వ రాజ్యాంగ సవరణ 1976 ద్వారా మొదట 10 మౌలిక విధులు చేర్చారు. 86వ సవరణ 2002 ద్వారా 11వ విధి చేర్చారు. ప్రస్తుతం మొత్తం 11 మౌలిక విధులు Article 51A లో ఉన్నాయి.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 6 — లౌకిక రాజ్యం మరియు వయోజన ఓటు హక్కు (Bilingual)
    # ══════════════════════════════════════════

    # Easy — Bilingual
    (6, 1,
     "భారత రాజ్యాంగంలో 'Secular' పదాన్ని ప్రస్తావనలో ఏ సవరణ ద్వారా చేర్చారు?\n(Which amendment added 'Secular' to the Preamble?)",
     "40వ సవరణ 1975 / 40th Amendment 1975",
     "42వ సవరణ 1976 / 42nd Amendment 1976",
     "44వ సవరణ 1978 / 44th Amendment 1978",
     "52వ సవరణ 1985 / 52nd Amendment 1985",
     "b",
     "42వ రాజ్యాంగ సవరణ 1976 ద్వారా Preamble లో 'Secular' మరియు 'Socialist' పదాలు చేర్చారు. అంతకు ముందు Preamble లో ఇవి లేవు. ఈ సవరణను 'Mini Constitution' అంటారు."),

    (6, 1,
     "61వ రాజ్యాంగ సవరణ 1989 ద్వారా ఓటు హక్కు వయస్సు ఎంత నుండి ఎంతకి తగ్గించారు?\n(The 61st Amendment 1989 reduced voting age from — to —?)",
     "25 నుండి 21 కి / 25 to 21",
     "21 నుండి 18 కి / 21 to 18",
     "18 నుండి 16 కి / 18 to 16",
     "21 నుండి 16 కి / 21 to 16",
     "b",
     "61వ రాజ్యాంగ సవరణ 1989 ద్వారా ఓటు హక్కు వయస్సు 21 సంవత్సరాల నుండి 18 సంవత్సరాలకు తగ్గించారు. రాజీవ్ గాంధీ ప్రభుత్వ హయాంలో ఈ మార్పు జరిగింది. ఇప్పుడు 18+ పౌరులందరికీ ఓటు హక్కు."),

    (6, 1,
     "భారత రాష్ట్రపతి ఎన్నికలో 'Election Commission of India' స్థాపించబడింది ఏ ఆర్టికల్ ద్వారా?\n(Election Commission of India is established under which Article?)",
     "ఆర్టికల్ 315 / Article 315",
     "ఆర్టికల్ 324 / Article 324",
     "ఆర్టికల్ 280 / Article 280",
     "ఆర్టికల్ 148 / Article 148",
     "b",
     "Election Commission of India (ఎన్నికల సంఘం) Article 324 ద్వారా స్థాపించబడింది. Article 315 = UPSC. Article 280 = Finance Commission. Article 148 = CAG (Comptroller and Auditor General)."),

    # Moderate — Bilingual
    (6, 2,
     "భారత రాజ్యాంగంలో 'ఒకే పౌరసత్వం (Single Citizenship)' ఏ లక్షణం?\n(Single Citizenship in Indian Constitution is a feature of:)",
     "సమాఖ్య లక్షణం / Federal Feature",
     "ఏకీకృత లక్షణం / Unitary Feature",
     "పార్లమెంటరీ లక్షణం / Parliamentary Feature",
     "అంతర్జాతీయ లక్షణం / International Feature",
     "b",
     "ఒకే పౌరసత్వం (Single Citizenship) ఏకీకృత లక్షణం. USA లో dual citizenship ఉంటుంది (Federal + State). భారత్ లో కేవలం భారత జాతీయ పౌరత్వమే — రాష్ట్ర పౌరత్వం లేదు. ఇది UK నుండి స్వీకరించారు."),

    (6, 2,
     "కింది స్వతంత్ర సంస్థలను వాటి ఆర్టికల్ తో సరిగ్గా జోడించండి:\n(P) Election Commission — (1) Article 280\n(Q) CAG — (2) Article 324\n(R) Finance Commission — (3) Article 315\n(S) UPSC — (4) Article 148",
     "P-2, Q-4, R-1, S-3", "P-1, Q-2, R-3, S-4",
     "P-2, Q-1, R-4, S-3", "P-3, Q-4, R-1, S-2",
     "a",
     "Election Commission = Article 324 (P-2). CAG = Article 148 (Q-4). Finance Commission = Article 280 (R-1). UPSC = Article 315 (S-3). ఇవి నాలుగూ స్వతంత్ర రాజ్యాంగ సంస్థలు."),

    # Tough — Bilingual
    (6, 3,
     "భారత రాజ్యాంగంలో లౌకికత (Secularism) యొక్క అర్థం ఏమిటి?\n(What does Secularism mean in the Indian context?)",
     "ప్రభుత్వం అన్ని మతాలను నిరోధిస్తుంది / Government prohibits all religions",
     "ప్రభుత్వానికి అధికారిక మతం ఉంటుంది / Government has an official religion",
     "ప్రభుత్వం అన్ని మతాలను సమానంగా గౌరవిస్తుంది; ఏ మతమూ అధికారిక కాదు / Equal respect to all religions",
     "మతం పూర్తిగా రాజ్యాంగంలో నిషిద్ధం / Religion is banned in Constitution",
     "c",
     "భారత లౌకికత (Secularism) అంటే రాజ్యానికి అధికారిక మతం లేదు; అన్ని మతాలను సమానంగా గౌరవిస్తుంది. ఇది Western Secularism (మతం నుండి రాజ్యం వేరుపడటం) కంటే భిన్నంగా ఉంది. 42వ సవరణ 1976 ద్వారా Preamble లో 'Secular' చేర్చారు."),

    # Toughest — Bilingual
    (6, 4,
     "Assertion (A): India follows the principle of Universal Adult Franchise since the Constitution came into force.\nReason (R): The 61st Constitutional Amendment 1989 reduced the voting age from 21 to 18 years, expanding the scope of franchise.\n(రెండూ నిజమేనా? R అనేది A కి వివరణా?)",
     "A మరియు R రెండూ సరైనవి, R అనేది A కి సరైన వివరణ / Both correct, R explains A",
     "A మరియు R రెండూ సరైనవి, కానీ R వివరణ కాదు / Both correct, R doesn't explain",
     "A సరైనది, R తప్పు / A correct, R wrong",
     "A తప్పు, R సరైనది / A wrong, R correct",
     "b",
     "A — భారత్ రాజ్యాంగం నాటి నుండే Universal Adult Franchise ఉంది (True). R — 61వ సవరణ 1989 ద్వారా 21 నుండి 18 కి తగ్గించారు (True). కానీ R, A కి వివరణ కాదు — ఎందుకంటే Universal Adult Franchise 1950 నుండే ఉంది, 1989 తర్వాత కాదు. R వివరిస్తుంది franchise విస్తరణ, A ప్రారంభాన్ని కాదు."),

    # PYQ — APPSC Bilingual
    (6, 2,
     "61వ రాజ్యాంగ సవరణ 1989 ఏ మార్పు తీసుకువచ్చింది? [APPSC Group 2]",
     "మౌలిక విధులు చేర్చారు",
     "ఓటు హక్కు వయస్సు 21 నుండి 18 కి తగ్గించారు",
     "'Secular' మరియు 'Socialist' పదాలు Preamble లో చేర్చారు",
     "పంచాయతీ రాజ్ కు రాజ్యాంగ హోదా ఇచ్చారు",
     "b",
     "61వ రాజ్యాంగ సవరణ 1989: ఓటు హక్కు వయస్సు 21 నుండి 18 కి తగ్గించారు. 42వ సవరణ 1976 = Secular+Socialist + మౌలిక విధులు. 73వ సవరణ 1992 = పంచాయతీ రాజ్. ఇది APPSC Group 2 లో తరచుగా వచ్చే ప్రశ్న.",
     "APPSC"),

    # PYQ — UPSC Bilingual
    (6, 2,
     "అధికరణం 324 కింద ఏ స్వతంత్ర సంస్థ? / Which Independent Constitutional Body is established under Article 324 of the Indian Constitution? [UPSC Style]",
     "UPSC (Union Public Service Commission)",
     "CAG (Comptroller and Auditor General)",
     "Election Commission of India",
     "Finance Commission",
     "c",
     "Election Commission of India — Article 324 ద్వారా స్థాపించబడింది. CAG = Article 148. UPSC = Article 315. Finance Commission = Article 280. ఇవి నాలుగూ స్వతంత్ర రాజ్యాంగ సంస్థలు.",
     "UPSC"),

    # ══════════════════════════════════════════
    # SECTION 7 — అత్యవసర నిబంధనలు మరియు ఇతర లక్షణాలు (Bilingual)
    # ══════════════════════════════════════════

    # Easy — Bilingual
    (7, 1,
     "భారత రాజ్యాంగంలో జాతీయ అత్యవసర పరిస్థితి (National Emergency) ఏ ఆర్టికల్ ద్వారా విధించవచ్చు?\n(Under which Article can National Emergency be proclaimed?)",
     "ఆర్టికల్ 356 / Article 356",
     "ఆర్టికల్ 352 / Article 352",
     "ఆర్టికల్ 360 / Article 360",
     "ఆర్టికల్ 368 / Article 368",
     "b",
     "జాతీయ అత్యవసర పరిస్థితి (National Emergency) = Article 352. రాష్ట్రపతి పాలన (President's Rule) = Article 356. ఆర్థిక అత్యవసర పరిస్థితి (Financial Emergency) = Article 360. రాజ్యాంగ సవరణ = Article 368."),

    (7, 1,
     "పంచాయతీ రాజ్ (Panchayati Raj) కు రాజ్యాంగ హోదా ఏ సవరణ ద్వారా వచ్చింది?\n(Which Amendment gave constitutional status to Panchayati Raj?)",
     "42వ సవరణ 1976 / 42nd Amendment 1976",
     "61వ సవరణ 1989 / 61st Amendment 1989",
     "73వ సవరణ 1992 / 73rd Amendment 1992",
     "97వ సవరణ 2011 / 97th Amendment 2011",
     "c",
     "73వ రాజ్యాంగ సవరణ 1992 — గ్రామీణ స్వపాలన సంస్థలు (పంచాయతీ రాజ్) కు రాజ్యాంగ హోదా. 74వ సవరణ 1992 — పట్టణ స్వపాలన సంస్థలకు రాజ్యాంగ హోదా. కలిసి 'Narasimha Rao Government' హయాంలో వచ్చాయి."),

    # Moderate — Bilingual
    (7, 2,
     "భారత రాజ్యాంగంలో మూడు రకాల అత్యవసర పరిస్థితులను వాటి ఆర్టికల్ తో సరిగ్గా జోడించండి:\n(P) National Emergency — (1) Article 360\n(Q) President's Rule — (2) Article 352\n(R) Financial Emergency — (3) Article 356",
     "P-2, Q-3, R-1", "P-1, Q-2, R-3",
     "P-3, Q-1, R-2", "P-2, Q-1, R-3",
     "a",
     "National Emergency = Article 352 (P-2). President's Rule = Article 356 (Q-3). Financial Emergency = Article 360 (R-1). ఈ మూడు అత్యవసర నిబంధనలు జర్మనీ Weimar Constitution నుండి స్ఫూర్తి పొందాయి."),

    (7, 2,
     "కింది వాటిలో రాజ్యాంగ సవరణలను సరిగ్గా జోడించండి:\n(1) 42వ సవరణ 1976 — Secular, Socialist Preamble లో చేర్చడం\n(2) 61వ సవరణ 1989 — ఓటు హక్కు వయస్సు 21→18\n(3) 73వ సవరణ 1992 — పురపాలక సంఘాలు (Urban Local Bodies)\n(4) 86వ సవరణ 2002 — 11వ మౌలిక విధి",
     "1, 2 మరియు 4 మాత్రమే సరైనవి / 1, 2 and 4 only",
     "1, 2, 3 మరియు 4 అన్నీ సరైనవి / All correct",
     "2 మరియు 3 మాత్రమే సరైనవి / 2 and 3 only",
     "1 మరియు 4 మాత్రమే సరైనవి / 1 and 4 only",
     "a",
     "3 తప్పు — 73వ సవరణ 1992 = పంచాయతీ రాజ్ (Rural); 74వ సవరణ 1992 = పురపాలక సంఘాలు (Urban). 1 (42nd ✓), 2 (61st ✓), 4 (86th ✓) అన్నీ సరైనవి."),

    # Tough — Bilingual
    (7, 3,
     "రాష్ట్రంలో రాజ్యాంగ యంత్రాంగం విఫలమైనప్పుడు ఏ ఆర్టికల్ ద్వారా రాష్ట్రపతి పాలన విధించవచ్చు?\n(Under which Article is President's Rule imposed when Constitutional machinery of a state fails?)",
     "ఆర్టికల్ 352 / Article 352",
     "ఆర్టికల్ 356 / Article 356",
     "ఆర్టికల్ 360 / Article 360",
     "ఆర్టికల్ 368 / Article 368",
     "b",
     "Article 356 — రాష్ట్రంలో రాజ్యాంగ యంత్రాంగం విఫలమైతే రాష్ట్రపతి పాలన (President's Rule లేదా State Emergency) విధించవచ్చు. ఆర్టికల్ 352 = జాతీయ అత్యవసరం. ఆర్టికల్ 360 = ఆర్థిక అత్యవసరం. ఆర్టికల్ 368 = రాజ్యాంగ సవరణ."),

    # Toughest — Bilingual
    (7, 4,
     "Assertion (A): Co-operative Societies were given constitutional recognition through the 97th Constitutional Amendment 2011.\nReason (R): The 97th Amendment inserted Part IX-B (Articles 243ZH to 243ZT) into the Constitution dealing with Co-operative Societies.\n(రెండూ నిజమేనా?)",
     "A మరియు R రెండూ సరైనవి, R అనేది A కి సరైన వివరణ / Both correct, R explains A",
     "A మరియు R రెండూ సరైనవి, కానీ R వివరణ కాదు / Both correct, R doesn't explain",
     "A సరైనది, R తప్పు / A correct, R wrong",
     "A తప్పు, R సరైనది / A wrong, R correct",
     "a",
     "97వ రాజ్యాంగ సవరణ 2011 సహకార సంఘాలకు (Co-operative Societies) రాజ్యాంగ హోదా ఇచ్చింది (A — correct). Part IX-B, Articles 243ZH to 243ZT చేర్చారు (R — correct, directly explains A)."),

    # PYQ — UPSC Bilingual
    (7, 2,
     "ఆర్థిక అత్యవసర పరిస్థితి ఏ అధికరణం కింద? / Under which Article of the Indian Constitution can the President proclaim Financial Emergency? [UPSC Style]",
     "Article 352", "Article 356",
     "Article 360", "Article 368",
     "c",
     "Financial Emergency (ఆర్థిక అత్యవసర పరిస్థితి) = Article 360. National Emergency = Article 352. President's Rule = Article 356. Amendment of Constitution = Article 368. ఇవి నాలుగూ పరీక్షలలో తరచుగా వచ్చే ముఖ్య ఆర్టికల్స్.",
     "UPSC"),

    # ── Section 9: రాజ్యాంగ భావన — Written/Unwritten & Rigid/Flexible ──────────────
    (9, 1,
     "రాజ్యాంగాలను 'Written' మరియు 'Unwritten' గా వర్గీకరించిన పండితుడు ఎవరు?\n"
     "(Who classified constitutions into 'Written' and 'Unwritten'?)",
     "K.C. Wheare", "James Bryce",
     "Ivor Jennings", "Paul Appleby",
     "b",
     "James Bryce తన 'Studies in History and Jurisprudence' లో రాజ్యాంగాలను Written మరియు Unwritten గా వర్గీకరించారు. K.C. Wheare రాజ్యాంగాలను Federal/Unitary/Quasi-Federal గా వర్గీకరించారు."),

    (9, 1,
     "కింది దేశాలలో 'అలిఖిత రాజ్యాంగం' (Unwritten Constitution) ఉన్న దేశం ఏది?\n"
     "(Which of the following countries has an Unwritten Constitution?)",
     "USA", "France",
     "United Kingdom", "Japan",
     "c",
     "United Kingdom (UK) కి అలిఖిత రాజ్యాంగం ఉంది — Magna Carta (1215), Bill of Rights (1689), Parliament Acts వంటి చట్టాలు, కోర్టు తీర్పులు మరియు సంప్రదాయాల ద్వారా రూపొందినది. USA, France, Japan లకు లిఖిత రాజ్యాంగాలు ఉన్నాయి."),

    (9, 1,
     "'Enacted Constitution' అంటే ఏమిటి?\n"
     "(What is meant by an 'Enacted Constitution'?)",
     "పార్లమెంట్ చర్చ ద్వారా క్రమంగా పెరిగిన రాజ్యాంగం",
     "సంప్రదాయాలు మరియు ఆచారాల ద్వారా విలీనమైన రాజ్యాంగం",
     "నిర్దిష్ట సమావేశం ద్వారా ఒక సమయంలో రాసి ఆమోదించిన రాజ్యాంగం",
     "న్యాయస్థాన తీర్పుల ద్వారా రూపొందిన రాజ్యాంగం",
     "c",
     "Enacted Constitution = లిఖిత రాజ్యాంగం — ఒక నిర్దిష్ట సమావేశం (Constituent Assembly) ద్వారా ఒకే సమయంలో రాసి ఆమోదించబడింది. Evolved Constitution = అలిఖిత రాజ్యాంగం — సంప్రదాయాలు, చట్టాలు మరియు కోర్టు తీర్పుల ద్వారా క్రమంగా పెరిగింది (UK)."),

    (9, 2,
     "'దృఢ రాజ్యాంగం' (Rigid Constitution) యొక్క ముఖ్య లక్షణం ఏమిటి?\n"
     "(What is the key feature of a 'Rigid Constitution'?)",
     "సాధారణ మెజారిటీతో సవరించవచ్చు",
     "సవరించడానికి ప్రత్యేక కఠిన విధానం అవసరం",
     "సవరణలు అసాధ్యం",
     "రాజ్యాంగ కోర్టు మాత్రమే సవరించగలదు",
     "b",
     "Rigid Constitution = సవరించడానికి ప్రత్యేక విధానం అవసరం — సాధారణ చట్టంకంటే కఠినంగా ఉంటుంది. USA రాజ్యాంగం దృఢమైనది: 2/3 Congress ఆమోదం + 3/4 రాష్ట్రాల ఆమోదం అవసరం. Flexible Constitution = UK — సాధారణ పార్లమెంట్ మెజారిటీతో సవరించవచ్చు."),

    (9, 2,
     "అమెరికా (USA) రాజ్యాంగం ఏ వర్గానికి చెందుతుంది?\n"
     "(To which category does the USA Constitution belong?)",
     "Flexible + Unwritten", "Rigid + Written",
     "Flexible + Written", "Rigid + Unwritten",
     "b",
     "USA రాజ్యాంగం Rigid (దృఢ) మరియు Written (లిఖిత). సవరించడానికి 2/3 Congress మెజారిటీ + 3/4 రాష్ట్రాల ఆమోదం అవసరం. 1789 నుండి ఇప్పటి వరకు కేవలం 27 సవరణలు మాత్రమే జరిగాయి. UK రాజ్యాంగం Flexible + Unwritten."),

    (9, 2,
     "UK (బ్రిటన్) రాజ్యాంగం ఏ వర్గానికి చెందుతుంది?\n"
     "(To which category does the UK Constitution belong?)",
     "Written + Rigid", "Written + Flexible",
     "Unwritten + Flexible", "Unwritten + Rigid",
     "c",
     "UK రాజ్యాంగం Unwritten (అలిఖిత) మరియు Flexible (సౌమ్య). Parliament Acts, Magna Carta, Bill of Rights వంటి అనేక చట్టాలు, సంప్రదాయాలు కలిసి రాజ్యాంగంగా పని చేస్తాయి. సాధారణ పార్లమెంట్ మెజారిటీతో మార్చవచ్చు."),

    (9, 2,
     "భారత రాజ్యాంగం 'Rigid' మరియు 'Flexible' విషయంలో ఏ వర్గానికి చెందుతుంది?\n"
     "(In terms of Rigid vs Flexible, how is the Indian Constitution classified?)",
     "పూర్తిగా దృఢమైనది (Completely Rigid)",
     "పూర్తిగా సౌమ్యమైనది (Completely Flexible)",
     "పాక్షికంగా దృఢం, పాక్షికంగా సౌమ్యం (Partly Rigid, Partly Flexible)",
     "సవరించడం అసాధ్యం (Cannot be amended)",
     "c",
     "భారత రాజ్యాంగం మిశ్రమ స్వభావం కలది — K.C. Wheare దీన్ని 'partly flexible and partly rigid' అన్నారు. కొన్ని నిబంధనలు సాధారణ మెజారిటీతో సవరించవచ్చు (Art.368 - Type I). కొన్నింటికి 2/3 మెజారిటీ + రాష్ట్రాల ఆమోదం కావాలి (Art.368 - Type III)."),

    (9, 3,
     "K.C. Wheare రాజ్యాంగ పండితత్వంలో ఏ పుస్తకానికి ప్రసిద్ధులు?\n"
     "(K.C. Wheare is famous for which book in constitutional scholarship?)",
     "Federal Government", "Modern Constitutions",
     "The Constitution of Liberty", "Constitutional Government",
     "b",
     "K.C. Wheare 'Modern Constitutions' (1951) పుస్తకంలో రాజ్యాంగాలను Written/Unwritten, Rigid/Flexible, Federal/Unitary గా వర్గీకరించారు. అదే పుస్తకంలో భారత రాజ్యాంగాన్ని 'Quasi-Federal' అన్నారు. 'Federal Government' కూడా Wheare రాసిన పుస్తకమే, కానీ classification కు 'Modern Constitutions' ప్రసిద్ధం."),

    (9, 3,
     "ఒక రాజ్యాంగం 'Supreme Constitution' (సర్వోన్నత రాజ్యాంగం) అని అనడానికి అర్థం ఏమిటి?\n"
     "(What does it mean for a constitution to be a 'Supreme Constitution'?)",
     "రాష్ట్రపతి రాజ్యాంగాన్ని మార్చగలడు",
     "రాజ్యాంగం అన్ని సాధారణ చట్టాలకంటే ఉన్నతమైనది; రాజ్యాంగ విరుద్ధ చట్టం చెల్లదు",
     "పార్లమెంట్ రాజ్యాంగాన్ని ఏ సమయంలోనైనా మార్చవచ్చు",
     "న్యాయస్థానాలు రాజ్యాంగాన్ని రద్దు చేయవచ్చు",
     "b",
     "Supreme Constitution (రాజ్యాంగ సర్వోన్నతత) = రాజ్యాంగం దేశంలోని అన్ని చట్టాలకు ఉన్నతమైనది. రాజ్యాంగ విరుద్ధంగా చేసిన ఏ చట్టమైనా చెల్లదు (void). USA, భారత్ లలో రాజ్యాంగ సర్వోన్నతత ఉంది. UK లో Parliament Supremacy ఉంది (రాజ్యాంగ సర్వోన్నతత కాదు)."),

    (9, 2,
     "ఏ దేశంలో 'Parliamentary Sovereignty' (పార్లమెంట్ సర్వోన్నతత) ఉంది, రాజ్యాంగ సర్వోన్నతత కాదు?\n"
     "(In which country does 'Parliamentary Sovereignty' prevail, not constitutional supremacy?)",
     "USA", "India",
     "Australia", "United Kingdom",
     "d",
     "UK లో Parliament అత్యున్నత అధికారం కలది — Parliament ఏ చట్టమైనా చేయవచ్చు, మార్చవచ్చు. కోర్టులు పార్లమెంట్ చట్టాన్ని రద్దు చేయలేవు (Unwritten constitution). USA, India, Australia లలో రాజ్యాంగ సర్వోన్నతత ఉంది — court రాజ్యాంగ విరుద్ధ చట్టాన్ని రద్దు చేయగలదు."),

    (9, 2,
     "Israel మరియు New Zealand ల రాజ్యాంగం ఏ వర్గానికి చెందుతుంది?\n"
     "(The constitutions of Israel and New Zealand belong to which category?)",
     "Written + Rigid", "Unwritten + Flexible",
     "Written + Flexible", "Rigid + Federal",
     "b",
     "Israel మరియు New Zealand కి అలిఖిత + సౌమ్య రాజ్యాంగాలు ఉన్నాయి (Unwritten + Flexible) — UK తరహా. UK, Israel, New Zealand — ఈ మూడింటికి లిఖిత రాజ్యాంగం లేదు. Australia, Canada, India, USA లకు లిఖిత రాజ్యాంగాలు ఉన్నాయి."),

    (9, 3,
     "APPSC Polity: 'Organic Laws' అంటే ఏమిటి?\n"
     "('Organic Laws' in constitutional context means?)",
     "వ్యవసాయానికి సంబంధించిన చట్టాలు",
     "రాజ్యాంగ సవరణ చట్టాలు",
     "రాజ్యాంగంగా పని చేసే ప్రాథమిక చట్టాలు",
     "పర్యావరణ పరిరక్షణ చట్టాలు",
     "c",
     "Organic Laws = ఒక దేశంలో రాజ్యాంగంగా పని చేసే ప్రాథమిక చట్టాలు. UK లో Magna Carta, Bill of Rights, Parliament Acts వంటివి organic laws గా పని చేస్తాయి. Israel లో Basic Laws organic laws గా పని చేస్తాయి. భారత్ లో Constitution of India ఒకే organic law."),

    (9, 2,
     "పార్లమెంట్ రాజ్యాంగ సవరణ చేయాలంటే కనీసం ఎంత మెజారిటీ అవసరం (సాధారణ సవరణకు)?\n"
     "(For ordinary constitutional amendments in India under Art.368, minimum majority needed?)",
     "సాధారణ మెజారిటీ (Simple majority)",
     "2/3 హాజరైన సభ్యులు మరియు ఓటేసిన వారిలో + మొత్తం సభ్యత్వంలో సగానికి పైగా",
     "3/4 మెజారిటీ + రాష్ట్రాల ఆమోదం",
     "ఏకగ్రీవ తీర్మానం",
     "b",
     "Art.368 ప్రకారం సాధారణ రాజ్యాంగ సవరణకు: 2/3 హాజరైన & ఓటేసిన సభ్యుల మెజారిటీ + మొత్తు సభ్యత్వంలో సగానికి పైగా (Special Majority). కొన్ని ముఖ్యమైన నిబంధనలకు ఇంకా రాష్ట్రాల ఆమోదం కూడా కావాలి. ఇది USA కంటే తక్కువ దృఢం, UK కంటే ఎక్కువ దృఢం.",
     "APPSC"),

    (9, 3,
     "ఒక సంవిధానం 'Evolved Constitution' అయితే దాని ప్రత్యేకత ఏమిటి?\n"
     "(What is special about an 'Evolved Constitution'?)",
     "ఇది ఒక విప్లవం తర్వాత రాయబడింది",
     "ఇది దేశం స్వాతంత్య్రం పొందిన తర్వాత రాయబడింది",
     "ఇది సంప్రదాయాలు, చట్టాలు, కోర్టు తీర్పుల ద్వారా క్రమంగా రూపొందింది",
     "ఇది విదేశీ రాజ్యాంగాల నుండి నేరుగా అనువదించబడింది",
     "c",
     "Evolved Constitution (అలిఖిత రాజ్యాంగం) = UK రాజ్యాంగం వంటిది — వందల సంవత్సరాలుగా పార్లమెంట్ చట్టాలు (Magna Carta 1215, Petition of Right 1628, Bill of Rights 1689), న్యాయ తీర్పులు, political conventions ద్వారా క్రమంగా పెరిగింది. ఒకే సమయంలో ఒక Constituent Assembly రాయలేదు."),

    # ── Section 10: సమాఖ్య, ఏకీకృత, అర్ధ-సమాఖ్య ──────────────────────────────────
    (10, 1,
     "K.C. Wheare భారత రాజ్యాంగాన్ని ఏ పదంతో వర్ణించారు?\n"
     "(How did K.C. Wheare describe the Indian Constitution?)",
     "Federal", "Unitary",
     "Quasi-Federal", "Confederate",
     "c",
     "K.C. Wheare భారత రాజ్యాంగాన్ని 'Quasi-Federal' (అర్ధ-సమాఖ్య) అన్నారు — Federal రూపంలో ఉంటూ, Unitary ఆత్మ కలది. అవశేష అధికారాలు కేంద్రానికి, అత్యవసర పరిస్థితిలో రాష్ట్రాల అధికారాలు కేంద్రానికి మారడం వంటి Unitary లక్షణాలు ఉన్నాయి."),

    (10, 1,
     "కింది దేశాలలో 'Unitary Constitution' (ఏకీకృత రాజ్యాంగం) ఉన్న దేశం ఏది?\n"
     "(Which of the following has a Unitary Constitution?)",
     "USA", "Australia",
     "France", "Switzerland",
     "c",
     "France ఏకీకృత రాజ్యాంగం కలది — అన్ని అధికారాలు Paris కేంద్రంలో కేంద్రీకృతం. UK కూడా Unitary. USA, Australia, Switzerland లు Federal constitutions కలవి. భారత్ Quasi-Federal."),

    (10, 1,
     "సమాఖ్య రాజ్యాంగం (Federal Constitution) లో అవశేష అధికారాలు (Residuary Powers) ఎక్కడ ఉంటాయి — USA లో?\n"
     "(In the USA federal system, where do Residuary Powers reside?)",
     "కేంద్ర ప్రభుత్వంలో", "రాష్ట్రాలలో లేదా ప్రజలలో",
     "సుప్రీం కోర్టులో", "అధ్యక్షుడిలో",
     "b",
     "USA రాజ్యాంగం 10వ Amendment ప్రకారం: 'Powers not delegated to the US nor prohibited to the States are reserved to the States or the people.' అంటే Residuary Powers రాష్ట్రాలకు లేదా ప్రజలకు. భారత్ లో విరుద్ధంగా — Residuary Powers కేంద్రానికి (Art.248)."),

    (10, 2,
     "భారత రాజ్యాంగంలో అవశేష అధికారాలు (Residuary Powers) ఏ ఆర్టికల్ కింద కేంద్రానికి ఇవ్వబడ్డాయి?\n"
     "(Under which Article are Residuary Powers vested in the Centre in India?)",
     "Article 246", "Article 247",
     "Article 248", "Article 249",
     "c",
     "Article 248: Residuary Powers of legislation — Parliament has exclusive power to make laws on any matter not enumerated in Concurrent List or State List. ఇది USA కు విరుద్ధం (USA లో States కు). Art.246 = 3 Lists విభజన; Art.249 = Rajya Sabha Resolution ద్వారా State List పై Parliament చట్టం."),

    (10, 2,
     "ఏ పండితుడు భారత రాజ్యాంగాన్ని 'Federation with strong centralising tendency' అన్నారు?\n"
     "(Which scholar described India's constitution as a 'Federation with strong centralising tendency'?)",
     "K.C. Wheare", "Paul Appleby",
     "Ivor Jennings", "Granville Austin",
     "c",
     "Ivor Jennings: 'Federation with a strong centralising tendency.' K.C. Wheare: 'Quasi-Federal.' Paul Appleby: 'Extremely federalized.' Granville Austin: 'Cooperative Federalism.' ఇవి నాలుగూ పరీక్షలలో వేరువేరుగా అడుగుతారు — జాగ్రత్తగా గుర్తుపెట్టుకోండి."),

    (10, 2,
     "భారత రాజ్యాంగంలో గల ఈ లక్షణం ఏకీకృత స్వభావాన్ని (Unitary feature) చూపిస్తుంది:\n"
     "(Which of the following features of Indian Constitution reflects its Unitary character?)",
     "అధికారాల విభజన (Three Lists)",
     "స్వతంత్ర న్యాయవ్యవస్థ",
     "అవశేష అధికారాలు కేంద్రానికి",
     "ద్విసభా పార్లమెంట్",
     "c",
     "భారత రాజ్యాంగంలో Unitary Features: (1) అవశేష అధికారాలు కేంద్రానికి (Art.248), (2) ఒకే పౌరసత్వం, (3) Integrated Judiciary, (4) గవర్నర్ నియామకం కేంద్రం, (5) అత్యవసర పరిస్థితిలో రాష్ట్రాల అధికారాలు కేంద్రానికి, (6) All India Services. అధికారాల విభజన మరియు స్వతంత్ర న్యాయవ్యవస్థ Federal features."),

    (10, 2,
     "సమాఖ్య వ్యవస్థకు (Federal System) అవసరమైన ముఖ్యమైన పరిస్థితులు — కింది వాటిలో సమాఖ్యకు అవసరమైనది ఏది?\n"
     "(Which of the following is essential for a Federal System?)",
     "ఒకే పార్టీ పాలన",
     "రాజ్యాంగ సర్వోన్నతత మరియు అధికారాల విభజన",
     "ఒకే పౌరసత్వం మాత్రమే",
     "నేరుగా ఎన్నుకోబడిన అధ్యక్షుడు",
     "b",
     "Federal System కు అవసరమైన లక్షణాలు (K.C. Wheare ప్రకారం): (1) రాజ్యాంగ సర్వోన్నతత, (2) అధికారాల విభజన (Center + States), (3) స్వతంత్ర న్యాయవ్యవస్థ, (4) రాజ్యాంగ కాఠిన్యం (Rigidity). ఒకే పార్టీ, ఒకే పౌరసత్వం Unitary features."),

    (10, 3,
     "SR Bommai vs Union of India (1994) కేసులో సుప్రీం కోర్టు భారత సమాఖ్య స్వభావం గురించి ఏమి నిర్ణయించింది?\n"
     "(What did the Supreme Court decide about India's federal character in SR Bommai vs UoI 1994?)",
     "భారత్ పూర్తిగా Unitary దేశం",
     "రాష్ట్రాలు కేంద్రానికి 'satellite' లాంటివి",
     "Federalism భారత రాజ్యాంగ మూల నిర్మాణంలో భాగం",
     "అత్యవసర పరిస్థితిలో Federalism పూర్తిగా నిలిపివేయవచ్చు",
     "c",
     "SR Bommai Case (1994): రాష్ట్ర ప్రభుత్వాలను కేంద్రం Art.356 ద్వారా రద్దు చేయడాన్ని పరిమితం చేస్తూ, Federalism భారత రాజ్యాంగ 'Basic Structure' లో భాగమని నిర్ణయించింది. 'States are not mere appendages of the Centre.' — రాష్ట్రాలు వారి రంగంలో సర్వోన్నత అధికారం కలవి."),

    (10, 2,
     "భారత రాజ్యాంగంలో 'ఒకే పౌరసత్వం' (Single Citizenship) ఏ దేశ రాజ్యాంగం నుండి స్వీకరించారు?\n"
     "(Single Citizenship in Indian Constitution is borrowed from which country?)",
     "USA", "Australia",
     "Canada", "UK",
     "d",
     "Single Citizenship (ఒకే పౌరసత్వం) UK నుండి స్వీకరించారు. USA లో Dual Citizenship ఉంది — Federal Citizenship + State Citizenship. భారత్ లో ఒకే పౌరసత్వం Unitary feature లో ఒకటి — రాష్ట్ర పౌరసత్వం లేదు, కేవలం భారత పౌరసత్వం మాత్రమే."),

    (10, 3,
     "'Cooperative Federalism' (సహకార సమాఖ్య) భావన భారత రాజ్యాంగంలో ఎవరు గుర్తించారు?\n"
     "('Cooperative Federalism' in Indian Constitution was identified by which scholar?)",
     "K.C. Wheare", "Ivor Jennings",
     "Granville Austin", "Paul Appleby",
     "c",
     "Granville Austin తన 'Working a Democratic Revolution' పుస్తకంలో భారత రాజ్యాంగాన్ని 'Cooperative Federalism' గా వర్ణించారు — కేంద్రం మరియు రాష్ట్రాలు పరస్పర సహకారంతో పని చేస్తాయి. K.C. Wheare: Quasi-Federal; Ivor Jennings: Federation with centralising tendency; Paul Appleby: Extremely federalized."),

    (10, 3,
     "భారత్ లో గవర్నర్ (Governor) నియామకం ఎవరు చేస్తారు — ఇది ఏ స్వభావాన్ని చూపిస్తుంది?\n"
     "(Who appoints the Governor in India — and what constitutional character does this reflect?)",
     "రాష్ట్ర ప్రజలు ప్రత్యక్షంగా ఎన్నుకుంటారు — Federal",
     "రాష్ట్ర శాసనసభ ఎన్నుకుంటుంది — Federal",
     "రాష్ట్రపతి నియమిస్తారు — Unitary",
     "సుప్రీం కోర్టు నియమిస్తుంది — Judicial",
     "c",
     "గవర్నర్ నియామకం రాష్ట్రపతి (కేంద్రం) చేస్తారు — ఇది Unitary feature. USA లో Governor ప్రజలు ఎన్నుకుంటారు (Federal feature). భారత్ లో గవర్నర్ కేంద్రం agent లా పని చేస్తారు, రాష్ట్రం ఎన్నుకున్న ప్రతినిధి కాదు — అందుకే Quasi-Federal."),

    (10, 2,
     "Confederation (సమాఖ్య సమ్మేళనం) మరియు Federation (సమాఖ్య) లో ముఖ్య తేడా ఏమిటి?\n"
     "(Key difference between Confederation and Federation?)",
     "Confederation లో లిఖిత రాజ్యాంగం ఉంటుంది, Federation లో ఉండదు",
     "Confederation లో కేంద్రం బలంగా ఉంటుంది, Federation లో రాష్ట్రాలు బలంగా ఉంటాయి",
     "Confederation లో సభ్య రాష్ట్రాలు స్వతంత్రంగా ఉంటాయి, Federation లో రాజ్యాంగం సర్వోన్నతం",
     "Federation లో ఒకే పౌరసత్వం ఉంటుంది, Confederation లో రెండు పౌరసత్వాలు ఉంటాయి",
     "c",
     "Confederation = loose alliance of independent states (ex: EU partly, old Articles of Confederation USA 1781-1789) — సభ్య రాష్ట్రాలు స్వతంత్రంగా ఉంటాయి, కేంద్ర ప్రభుత్వం బలహీనంగా ఉంటుంది, రాష్ట్రాలు వేరుపడవచ్చు. Federation = రాజ్యాంగ ఆధారంగా కేంద్రం + రాష్ట్రాలు — రాష్ట్రాలు వేరుపడలేవు."),

    (10, 2,
     "Article 249 ద్వారా పార్లమెంట్ ఏ పరిస్థితిలో రాష్ట్ర జాబితా (State List) పై చట్టాలు చేయగలదు?\n"
     "(Under Art.249, when can Parliament legislate on State List items?)",
     "రాష్ట్రపతి ఉత్తర్వు ద్వారా",
     "రాజ్యసభ 2/3 మెజారిటీ తీర్మానం ద్వారా — జాతీయ ప్రయోజనం పేరుతో",
     "లోక్‌సభ సాధారణ మెజారిటీ ద్వారా",
     "రాష్ట్ర అభ్యర్థన లేకుండా సాధ్యం కాదు",
     "b",
     "Art.249: Rajya Sabha 2/3 present & voting మెజారిటీ తీర్మానం — 'National Interest' కారణంగా Parliament రాష్ట్ర జాబితా పై చట్టాలు చేయవచ్చు (1 సంవత్సరం, renewal సాధ్యం). ఇది Unitary feature — కేంద్రం రాష్ట్రాల అంశాలపై అతిక్రమించగలదు."),

    (10, 3,
     "All India Services (IAS, IPS, IFoS) Unitary feature ఎందుకంటారు?\n"
     "(Why are All India Services considered a Unitary feature?)",
     "ఇవి కేవలం కేంద్రం మాత్రమే ఉపయోగించుకుంటుంది",
     "వీటిని పార్లమెంట్ రద్దు చేయగలదు",
     "ఇవి కేంద్రం నియంత్రణలో ఉండి రాష్ట్రాలలో పని చేస్తాయి — కేంద్రీయ ఆధిపత్యం చూపిస్తుంది",
     "వీటికి రాష్ట్ర అనుమతి అవసరం",
     "c",
     "All India Services (Art.312): IAS, IPS, IFoS — UPSC నియమిస్తుంది, కేంద్రం ఆధీనంలో ఉంటాయి, కానీ రాష్ట్రాలలో పని చేస్తాయి. పదోన్నతి, నిర్ణయం కేంద్రం తీసుకుంటుంది. ఇది Unitary feature — USA లో లేదు (each state has its own services). అంబేడ్కర్ వీటిని 'Steel Frame of India' అన్నారు.",
     "APPSC"),

    (10, 3,
     "APPSC PYQ: భారత రాజ్యాంగంలో సమాఖ్య లక్షణంగా (Federal Feature) ఏది లేదు?\n"
     "(APPSC PYQ: Which of the following is NOT a Federal Feature of the Indian Constitution?)",
     "అధికారాల విభజన (Division of Powers)",
     "స్వతంత్ర న్యాయవ్యవస్థ (Independent Judiciary)",
     "ద్విసభా పార్లమెంట్ (Bicameralism)",
     "ఒకే పౌరసత్వం (Single Citizenship)",
     "d",
     "ఒకే పౌరసత్వం (Single Citizenship) = Unitary Feature. Federal feature కాదు. USA లో Dual Citizenship (Federal + State) ఉంది. భారత్ లో రాష్ట్ర పౌరసత్వం లేదు. అధికారాల విభజన, స్వతంత్ర న్యాయవ్యవస్థ, ద్విసభా పార్లమెంట్ — ఇవి Federal features.",
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
