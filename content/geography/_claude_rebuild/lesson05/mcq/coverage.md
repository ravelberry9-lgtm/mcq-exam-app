# Lesson 5 — fact coverage and new MCQs

Source: ch05/FINAL/lesson_05_rebuilt.md — 174 `::: fact` blocks, numbered F001–F174 in lesson order (facts.txt). Existing = mcq05/FINAL/lesson05_questions.json, only questions with a non-null `lesson05_section` (288), matched to facts by meaning (existing_map.py; "(partial)" marks a question that tests only part of the fact). Ids shortened: `P031-F001` = GEO-BOOK-P031-F001, `O001` = GEO-ORIG-05-001, `04-015` / `06-001` = GEO-ORIG-04-015 / GEO-ORIG-06-001, `N012` = GEO-NEW-05-012 (new_questions.json).

## Totals

- Facts: 174. Tested (fully or partly) by existing questions: 114. Previously untested facts now covered by new questions: 60. Left without any question: 0.
- New questions: 87. Answer key spread: A=23, B=23, C=20, D=21.
- Format mix: concept 43, reasoning 15, assertion-reason 9, statements 8, matching 7, sequence 4, application 1. Assertion–reason keys: A=3, B=2, C=3, D=1. Statement keys: A=3, B=3, C=2. Match keys: A–3;B–1;C–4;D–2, A–4;B–3;C–1;D–2, A–2;B–4;C–1;D–3, A–3;B–2;C–1;D–4, A–1;B–3;C–4;D–2, A–4;B–1;C–3;D–2, A–2;B–1;C–4;D–3.
- "How to answer" questions for the changing / book-differing facts (flag `how_to_answer: true`; the rule is in the explanation, the stem is a plain question): N009, N015, N017, N020, N034, N035, N038, N040, N042, N044, N045, N047, N053, N057, N058, N059, N062, N068, N069, N072, N073, N079. Topics: Holmes year, plate count 7 vs 8, Indian Plate class, Morgan/McKenzie, Mauna Kea vs Everest, Vindhya by age vs origin, Great Dividing Range, 2,135 m mountain definition, Koyna type and magnitude by catalogue, seismic zones (four; Zone I removed 2002; Zone VI announced 2025 and withdrawn March 2026), focal depth 60 vs 70 km, energy per magnitude step (32 vs 30), Richter open-ended, Mw for large quakes, Mercalli damage level VI vs VIII, Deccan area and age, acidic lava 63 vs 65%, active-volcano counts 1,350 / 500, Kilimanjaro "extinct" in old books, Ring of Fire 75% vs half.
- Indian earthquakes and AP / Telugu-state links: Koyna (N044, N045), Latur/Bhuj/Assam, Hyderabad Zone II, NCS, INCOIS Hyderabad (ITEWC), Singareni Pranhita–Godavari graben, Rajahmundry Traps.
- Validator (build.py): 0 length flags, 0 errors, 0 warnings.

## Per section

| Section | Facts | Existing-covered | New-covered | New Qs | Why/how new Qs |
|---|---|---|---|---|---|
| forces | 8 | 0 | 8 | 5 | N003 |
| drift | 12 | 10 | 5 | 3 | N008 |
| seafloor-spreading | 10 | 3 | 10 | 6 | N011, N012 |
| plates | 14 | 11 | 7 | 8 | N019 |
| boundaries | 14 | 11 | 7 | 5 | N026, N027 |
| folds-faults | 11 | 4 | 10 | 5 | N030 |
| mountains | 12 | 0 | 12 | 10 | N038 |
| earthquake | 11 | 7 | 7 | 11 | N048, N049, N053 |
| seismic-records | 8 | 6 | 3 | 3 | N055, N056 |
| magnitude | 9 | 8 | 6 | 6 | N061 |
| tsunami | 7 | 6 | 2 | 2 | N064 |
| volcano-anatomy | 15 | 12 | 8 | 6 | N070 |
| volcano-types | 14 | 13 | 4 | 4 | N074 |
| intrusive | 3 | 3 | 1 | 1 | N075 |
| volcano-products | 4 | 4 | 1 | 1 | N076 |
| hot-springs | 5 | 4 | 3 | 2 | N078 |
| volcano-distribution | 2 | 1 | 2 | 2 | N080 |
| weathering | 6 | 3 | 3 | 3 | N081 |
| mass-wasting | 4 | 3 | 3 | 2 | N085 |
| erosion-deposition | 5 | 5 | 2 | 2 | N087 |

## Fact table

| Fact | Section | Fact (short) | Existing | New | Note |
|---|---|---|---|---|---|
| F001 | forces | భూమి లోపలి వేడి నుంచి శక్తి పొంది భూపటలాన్ని కదిలించే శక్తులను Endogenic forces … | — | N002, N003 |  |
| F002 | forces | సూర్యుడి శక్తి, Gravity సహాయంతో భూమి ఉపరితలం మీద పని చేసే శక్తులను Exogenic forc… | — | N002, N003 |  |
| F003 | forces | Endogenic forces నేల ఎత్తులను పెంచుతాయి; Exogenic forces ఆ ఎత్తులను అరగదీసి నేలన… | — | N002, N003 |  |
| F004 | forces | పొరలు ముడత పడి పర్వతాలు పుట్టే ప్రక్రియను Orogeny అంటారు. | — | N001, N004 |  |
| F005 | forces | ఖండంలోని విశాల ప్రాంతం ముడతలు లేకుండా పైకి లేవడం లేదా కిందకు దిగడాన్ని Epeirogen… | — | N001, N004 |  |
| F006 | forces | Gradation = Degradation (Denudation) + Aggradation. ఎత్తులను తొలిచి దించడం Degra… | — | N004 |  |
| F007 | forces | Weathering, Mass wasting, Erosion, Transportation కలిపి ఉపరితలాన్ని తొలిచే ప్రక్… | — | N004 |  |
| F008 | forces | పర్వతాలు, పీఠభూములు, మైదానాలను ద్వితీయ శ్రేణి భూస్వరూపాలు (Second order landform… | — | N005 |  |
| F009 | drift | ఖండాలు ఒకప్పుడు కలిసి ఉండేవని 1596 లో Abraham Ortelius అనే పటాల తయారీదారు సూచించ… | P032-F002 | — |  |
| F010 | drift | Continental drift theory (ఖండచలన సిద్ధాంతం) ను జర్మన్ వాతావరణ శాస్త్రవేత్త Alfre… | P032-F001, P032-M001 | — |  |
| F011 | drift | Wegener తన పుస్తకం *The Origin of Continents and Oceans* ను 1915 లో జర్మన్ భాషలో… | P032-F001 | — |  |
| F012 | drift | అన్ని ఖండాలూ కలిసి ఉన్న మహాఖండాన్ని Pangaea అని, దాని చుట్టూ ఉన్న మహాసముద్రాన్ని… | P031-F001, P031-F002, P031-M001 | — |  |
| F013 | drift | Pangaea లో Tethys సముద్రానికి ఉత్తరాన Laurasia, దక్షిణాన Gondwana ఉండేవి. | P031-F003, P031-F004, P031-F005 | — |  |
| F014 | drift | భారతదేశం Gondwana లో భాగంగా ఉండేది; ఆఫ్రికా, దక్షిణ అమెరికా, ఆస్ట్రేలియా, అంటార్… | P031-F005, P031-F011 | — |  |
| F015 | drift | Gondwana, Tethys పేర్లు పెట్టింది Eduard Suess; Laurasia పేరు వాడింది Alexander … | — | N006 |  |
| F016 | drift | Glossopteris మొక్క శిలాజాలు భారతదేశం, ఆఫ్రికా, అంటార్కిటికా, ఆస్ట్రేలియా, దక్షిణ… | P031-F010 (fossils, generic) | N007 |  |
| F017 | drift | Mesosaurus, Lystrosaurus, Cynognathus శిలాజాలు వేర్వేరు దక్షిణ ఖండాల్లో దొరకడం అ… | — | N007 |  |
| F018 | drift | ఒకే వయసు శిలలు వేర్వేరు ఖండాల్లో వేర్వేరు ధ్రువ స్థానాలను చూపడం (Polar wandering… | P031-F010 (old magnetism, generic) | N008 |  |
| F019 | drift | ఖండాలను కదిలించే నమ్మదగ్గ శక్తిని (Mechanism) చూపించలేకపోవడమే Wegener సిద్ధాంతంల… | P032-F003 | — |  |
| F020 | drift | ఖండాలు కదిలినప్పుడు కొన్ని సముద్రాలు తెరుచుకుంటాయి (Atlantic), మరికొన్ని ఇరుకై మ… | P031-F012, P033-F012 | N023 |  |
| F021 | seafloor-spreading | Mantle లోని Convection currents (సంవహన ప్రవాహాలు) ఖండాలను కదిలించే శక్తి అని Art… | P032-F004 (idea, no year) | N009 |  |
| F022 | seafloor-spreading | సముద్రం అడుగున Plates దూరం జరిగే చోట ఏర్పడే పొడవైన నీటి అడుగు పర్వత వరుసను Mid-o… | P032-F015 (definition, no length) | N013, N014 |  |
| F023 | seafloor-spreading | అరేబియా సముద్రంలోని Carlsberg Ridge, హిందూ మహాసముద్రంలోని Central Indian Ridge భ… | — | N013 |  |
| F024 | seafloor-spreading | Mid-ocean ridge, దాని మధ్యలోని Rift valley ను 1950 లలో Marie Tharp, Bruce Heezen… | — | N010 |  |
| F025 | seafloor-spreading | Seafloor spreading (సముద్ర భూతల వ్యాప్తి) భావనను Harry Hess 1960 లో ప్రతిపాదించా… | P032-F005 | N010 |  |
| F026 | seafloor-spreading | "Seafloor spreading" అనే పేరును 1961 లో Robert Dietz వాడాడు. | — | N010 |  |
| F027 | seafloor-spreading | Mid-ocean ridge కు రెండు వైపులా అద్దంలో ప్రతిబింబంలా ఉండే అయస్కాంత చారలు Seafloo… | — | N010, N011 |  |
| F028 | seafloor-spreading | శిలల్లో భద్రమైన పురాతన భూ అయస్కాంత దిశను Paleomagnetism అంటారు. | — | N011 |  |
| F029 | seafloor-spreading | సముద్ర భూతలం Mid-ocean ridge దగ్గర అతి కొత్తగా, Ridge నుంచి దూరం వెళ్లే కొద్దీ ప… | — | N012, N014 |  |
| F030 | seafloor-spreading | ఈ రోజు ఉన్న అతి పాత సముద్ర భూతలం వయసు సుమారు 18–20 కోట్ల సంవత్సరాలు (Jurassic); … | — | N012 |  |
| F031 | plates | Lithosphere లోని గట్టి ముక్కను Plate (పలక) అంటారు; ఇది Crust, Mantle పై భాగం కలి… | — | N022 |  |
| F032 | plates | African, Antarctic, Australian Plates లో ఆ ఖండాలతో పాటు చుట్టూ ఉన్న సముద్ర భూతలం… | P033-F007, P033-F008, P033-F009 | — |  |
| F033 | plates | Plates అనే ఆలోచనను, Transform faults ను 1965 లో కెనడా శాస్త్రవేత్త J. Tuzo Wilso… | P032-F006 | — |  |
| F034 | plates | Plate tectonics సిద్ధాంతాన్ని 1967–68 లో W. Jason Morgan, Dan McKenzie–Robert Pa… | P032-F007 (partial, no names) | N020 |  |
| F035 | plates | Plates ను కదిలించే బలాలు Mantle convection, Ridge push, Slab pull; వీటిలో Slab p… | — | N019 |  |
| F036 | plates | 2 కోట్ల km² కంటే పెద్దవి Major plates; 10 లక్షల నుంచి 2 కోట్ల km² మధ్యవి Minor p… | P032-F017, P032-F018, P032-F019, P032-M005 | N017 |  |
| F037 | plates | విస్తీర్ణంలో అన్నిటికంటే పెద్ద Plate, Pacific Plate (సుమారు 10.3 కోట్ల km²); రెం… | P032-F020 (largest only) | N018 |  |
| F038 | plates | ఏడు పెద్ద Plates: Pacific, North American, Eurasian, African, Antarctic, Indo-Au… | P032-F016 (partial), P032-F021 | N015, N016 |  |
| F039 | plates | దక్షిణ అమెరికాకు పడమర Nazca Plate, మధ్య అమెరికాకు పడమర Cocos Plate ఉన్నాయి. | P032-F023, P032-F024, P033-F005 | — |  |
| F040 | plates | ఉత్తర అమెరికా వాయవ్య తీరంలో Cascadia Subduction zone కు కారణమైన చిన్న Plate, Jua… | P033-F004 | — |  |
| F041 | plates | Indian Plate కు ఉత్తరాన హిమాలయ ఢీ, తూర్పున Andaman–Sumatra Trench, పడమర Chaman F… | — | N021 |  |
| F042 | plates | ప్రపంచ పటాన్ని Pacific ప్రాంతంలో కత్తిరించి గీయడం వల్ల Pacific Plate పటానికి రెం… | P033-F013 | — |  |
| F043 | plates | Plate సరిహద్దు Lithosphere కదలికను చూపిస్తుంది; రాజకీయ సరిహద్దు మనుషులు గీసిన పర… | P033-F001 | — |  |
| F044 | plates | Plates ఈ రోజు కదలికల ఆధారంగా సుమారు 25 కోట్ల సంవత్సరాల తరువాత ఏర్పడవచ్చని భావించ… | P032-F022 | — |  |
| F045 | boundaries | Divergent boundary లో Plates దూరం జరుగుతాయి; Mid-ocean ridge దగ్గర కొత్త సముద్ర … | 06-001, P032-F009, P032-F014, P033-F011 | — |  |
| F046 | boundaries | ఖండంలో Divergent boundary మొదలైతే Rift valley (పగులు లోయ) ఏర్పడుతుంది; East Afri… | P032-F027, P032-F029 (partial) | N023 |  |
| F047 | boundaries | Convergent boundary లో ఢీకొనే Plates రకాన్ని బట్టి Subduction గానీ, ఖండాల ఢీ (Co… | 06-002, P032-F008 | — |  |
| F048 | boundaries | బరువైన Plate ఇంకో Plate కిందకు Mantle లోకి మునగడాన్ని Subduction అంటారు; ఆ చోట స… | 06-002 (partial) | N027 |  |
| F049 | boundaries | Nazca Plate, South American Plate కిందకు మునగడం (సముద్ర–ఖండ Subduction) వల్ల And… | P032-F012, P033-F003, 06-022 | N027 |  |
| F050 | boundaries | Indian Plate ఉత్తరానికి కదిలి Eurasian Plate ను ఢీకొనడం (ఖండ–ఖండ Collision) వల్ల… | P032-F011, P033-F002 | — |  |
| F051 | boundaries | సముద్ర–సముద్ర Plates కలిసే చోట Trench, దాని పక్కన Island arc (అగ్నిపర్వత దీవుల వ… | — | N024 |  |
| F052 | boundaries | Rocky పర్వతాల Laramide orogeny కి Farallon Plate ఉత్తర అమెరికా కిందకు తక్కువ వాల… | P032-F013 | — |  |
| F053 | boundaries | Transform boundary లో Plates అడ్డంగా (Horizontal) ఒకదాని పక్కన ఒకటి జారుతాయి; Cr… | 06-003, P032-F010 | — |  |
| F054 | boundaries | San Andreas Fault (California) Pacific, North American Plates మధ్య ఉన్న Transfor… | — | N025 |  |
| F055 | boundaries | Plate సరిహద్దుకు దూరంగా, Plate మధ్యలో Mantle plume వల్ల అగ్నిపర్వతాలు పుట్టే చోట… | 06-004 | N026 |  |
| F056 | boundaries | Pacific Plate వాయవ్యానికి కదలడం వల్ల Hawaii దీవులు వాయవ్యానికి వెళ్లే కొద్దీ పాత… | P041-F011 | — |  |
| F057 | boundaries | Iceland లో Mid-Atlantic Ridge, Hotspot రెండూ కలిసి ఉన్నాయి. | P041-F010 | — |  |
| F058 | boundaries | Deccan Traps Lava ప్రవాహాలు నేటి Réunion Hotspot తో ముడిపడి ఉన్నాయని భావిస్తారు. | — | N026 |  |
| F059 | folds-faults | రాయి మీద పనిచేసే Stress మూడు రకాలు: Compression (నొక్కడం), Tension (లాగడం), Shea… | 06-006 (compression only) | N032 |  |
| F060 | folds-faults | పైకి తోరణంలా వంగిన Fold భాగాన్ని Anticline (భూ అభినతి) అంటారు. | — | N028 |  |
| F061 | folds-faults | కిందకు తొట్టిలా వంగిన Fold భాగాన్ని Syncline (భూ అపనతి) అంటారు. | — | N028 |  |
| F062 | folds-faults | Recumbent fold విరిగి, దూరం ముందుకు జరిగితే దాన్ని Nappe అంటారు. | — | N028 |  |
| F063 | folds-faults | Normal fault లో Tension వల్ల Hanging wall, Footwall కంటే కిందకు జారుతుంది. | 06-005, 06-024 | N031 |  |
| F064 | folds-faults | Reverse fault లో Compression వల్ల Hanging wall, Footwall మీదకు పైకి ఎక్కుతుంది. | 06-006, 06-018 | — |  |
| F065 | folds-faults | Thrust fault అంటే తక్కువ వాలు ఉన్న Reverse fault. | — | N028 |  |
| F066 | folds-faults | Strike-slip fault లో కదలిక ప్రధానంగా అడ్డంగా, Fault దిశకు సమాంతరంగా ఉంటుంది. | 06-007, 06-019 | N032 |  |
| F067 | folds-faults | రెండు Normal faults మధ్య కిందకు జారిన దిమ్మను Graben అని, పైకి నిలిచిన దిమ్మను H… | — | N029, N031, N038 |  |
| F068 | folds-faults | పొడవైన Graben ను Rift valley (పగులు లోయ) అంటారు; Narmada, Tapi Rift valleys లో ప… | — | N029, N031 |  |
| F069 | folds-faults | Singareni బొగ్గు ఉన్న Pranhita–Godavari లోయ ఒక Graben; Damodar, Mahanadi లోయలు క… | — | N030 |  |
| F070 | mountains | పర్వతాల అధ్యయనాన్ని Orology అంటారు. | — | N033 |  |
| F071 | mountains | సముద్రమట్టం నుంచి ఎత్తైన శిఖరం Everest (8,848.86 m, 2020 సర్వే); అడుగు నుంచి శిఖ… | — | N034, N042 |  |
| F072 | mountains | J. D. Dana విస్తరణ బట్టి పర్వతాలను Ridge, Range, System, Chain, Cordillera గా వి… | — | N036 |  |
| F073 | mountains | వయస్సు బట్టి పర్వతాల దశలు నాలుగు: Precambrian, Caledonian, Hercynian, Alpine. | — | N035 |  |
| F074 | mountains | Himalaya, Alps, Rockies, Andes, Atlas Alpine దశలో (Tertiary కాలంలో) ఏర్పడ్డాయి. | — | N035, N040 |  |
| F075 | mountains | Urals, Vosges, Black Forest Hercynian దశ పర్వతాలు. | — | N035 |  |
| F076 | mountains | Geosyncline అంటే మట్టి పొరలు మందంగా పేరుకునే పొడవైన, కుంగే సముద్రపు గుంట; ఆలోచన … | — | N037 |  |
| F077 | mountains | Geosyncline పర్వత నిర్మాణ సిద్ధాంతం Leopold Kober (1921) ది; ఆయన ప్రకారం Himalay… | — | N037 |  |
| F078 | mountains | Horst రూపంలో పైకి లేచిన పర్వతాలను Block mountains (ఖండ పర్వతాలు) అంటారు; Vindhya… | — | N038 |  |
| F079 | mountains | అరిగిపోయి మిగిలిన పాత పర్వతాలను Residual mountains (అవశిష్ట పర్వతాలు) అంటారు. | — | N039 |  |
| F080 | mountains | Lava, బూడిద పేరుకుపోయి ఏర్పడినందువల్ల Volcanic mountains ను సంచిత పర్వతాలు అంటార… | — | N039 |  |
| F081 | mountains | Andes ప్రపంచంలో పొడవైన ఖండాంతర పర్వత శ్రేణి; ఏడు దేశాల గుండా వెళ్తుంది. | — | N041 |  |
| F082 | earthquake | భూమి లోపల దాగిన శక్తి ఒక్కసారిగా విడుదలై, Seismic waves గా ప్రయాణించి నేలను కుది… | P034-F001 | — |  |
| F083 | earthquake | 1906 San Francisco భూకంపం తరువాత H. F. Reid Elastic rebound theory ఇచ్చాడు: Faul… | P034-F004 (no Reid) | N043, N048 |  |
| F084 | earthquake | భూమి లోపల భూకంపం మొదలయ్యే బిందువును Focus (నాభి) లేదా Hypocentre అంటారు. | P034-F002, 04-015 | — |  |
| F085 | earthquake | Focus కు సరిగ్గా పైన, ఉపరితలం మీద ఉండే బిందువును Epicentre (అధికేంద్రం) అంటారు. | P034-F003, 04-016 | — |  |
| F086 | earthquake | భూకంపాలకు అతి ముఖ్యమైన, అతి బలమైన కారణం Tectonic కదలికలు (Faults వెంట రాయి జారడం… | P034-F004 | N048 |  |
| F087 | earthquake | జలాశయం నీటి బరువు, ఒత్తిడి వల్ల వచ్చే భూకంపాన్ని Reservoir-induced earthquake అం… | — | N044, N045 |  |
| F088 | earthquake | USGS ప్రకారం Shallow భూకంపాలు 0–70 km, Intermediate 70–300 km, Deep 300–700 km ల… | P034-F010, P034-F011, P034-F012 | — |  |
| F089 | earthquake | Focus లోతు పెరిగితే కుదుపు తెలిసే ప్రాంతం పెరుగుతుంది, ఒక్కో చోట తీవ్రత తగ్గుతుం… | P034-F013 (partial) | N053 |  |
| F090 | earthquake | అన్ని భూకంపాల్లో సుమారు 90%, అతి పెద్ద భూకంపాల్లో సుమారు 81% Circum-Pacific belt… | — | N051 |  |
| F091 | earthquake | భారతదేశంలో భూకంపాలను పర్యవేక్షించి సమాచారం ఇచ్చే సంస్థ National Center for Seism… | — | N052 |  |
| F092 | earthquake | Koyna 1967 (Reservoir-induced), Latur 1993 (Maharashtra, M6.2), Bhuj 2001 (Gujar… | — | N045, N046, N047, N049, N050 |  |
| F093 | seismic-records | Surface waves (L waves) ఉపరితలం వెంట ప్రయాణిస్తాయి; అన్నిటికంటే నెమ్మదిగా వెళ్లి… | P035-F010 | N056 |  |
| F094 | seismic-records | Rayleigh wave ను Lord Rayleigh (1885), Love wave ను A. E. H. Love (1911) గణితంతో… | — | N054 |  |
| F095 | seismic-records | Love wave లో నేల తరంగ దిశకు లంబంగా, అడ్డంగా పక్కకు–పక్కకు ఊగుతుంది. | P035-F011 | — |  |
| F096 | seismic-records | Rayleigh wave లో నేల కణాలు పైకీ కిందకూ, ముందుకూ వెనక్కూ కలిపి దీర్ఘవృత్తంలో దొర్… | P035-F012 | — |  |
| F097 | seismic-records | భూకంపాలు, Seismic waves అధ్యయనాన్ని Seismology అంటారు. | P036-F001 | — |  |
| F098 | seismic-records | భూకంపాన్ని నమోదు చేసే యంత్రం Seismograph (భూకంప లేఖిని); అది గీసే రికార్డు Seism… | P035-F015, P035-F016 | — |  |
| F099 | seismic-records | Seismograph లో Mass Inertia వల్ల నిలిచి ఉంటుంది, నేలకు బిగించిన చట్రం కదులుతుంది… | P036-F017 | — |  |
| F100 | seismic-records | మూడు Seismographs నుంచి దూరాలతో Epicentre ను కనుక్కునే పద్ధతిని Triangulation అం… | — | N055 |  |
| F101 | magnitude | Magnitude భూకంపం మొత్తం పరిమాణాన్ని (విడుదలైన శక్తిని) చెప్తుంది; ఒక భూకంపానికి … | P036-F004 | — |  |
| F102 | magnitude | Intensity ఒక ప్రదేశంలో కుదుపు, ప్రభావం, నష్టాన్ని చెప్తుంది; ప్రదేశాన్ని బట్టి మ… | P034-F014, 04-031 | — |  |
| F103 | magnitude | Modified Mercalli Intensity (MMI) scale కుదుపు ప్రభావాలను బట్టి Intensity ను I న… | P036-F002 (no levels) | N061, N062 |  |
| F104 | magnitude | Magnitude ఒక అంకె పెరిగితే Amplitude 10 రెట్లు, శక్తి సుమారు 32 (31.6) రెట్లు పె… | P036-F006, P036-F007, P036-F008 | N057, N058 |  |
| F105 | magnitude | Magnitude 2 అంకెలు పెరిగితే (ఉదా: M5 నుంచి M7) శక్తి సుమారు 1,000 రెట్లు. | P036-F009 | N057 |  |
| F106 | magnitude | 1935 లో Charles F. Richter (Beno Gutenberg తో కలిసి) Local magnitude (Richter) s… | P036-F003 | N054 |  |
| F107 | magnitude | ఇప్పటివరకు నమోదైన అతి పెద్ద భూకంపం 1960 Chile భూకంపం (Mw 9.5). | — | N060 |  |
| F108 | magnitude | 1979 లో Hanks, Kanamori Moment magnitude (Mw) scale ఇచ్చారు; ఇది Fault వైశాల్యం,… | P036-F005 (no names, year) | N054, N059 |  |
| F109 | magnitude | ఒకే Magnitude భూకంపాల నష్టం Focus లోతు, దూరం, నేల రకం, నిర్మాణ నాణ్యత, జనాభాను బ… | P036-F010, 04-031 | — |  |
| F110 | tsunami | Tsunami Japanese పదం; Tsu = రేవు (Harbour), Nami = అల; అంటే "రేవు అల" (Harbour w… | P036-F011 | — |  |
| F111 | tsunami | సముద్రం అడుగు ఒక్కసారిగా నిలువుగా కదిలి పై నీటిని తోసినప్పుడు Tsunami పుడుతుంది. | P036-F012 | — |  |
| F112 | tsunami | భూకంపాలతో పాటు సముద్రం లోపలి కొండచరియలు, అగ్నిపర్వత విస్ఫోటనాలు, అరుదుగా ఉల్కాపా… | P036-F013 | — |  |
| F113 | tsunami | లోతైన సముద్రంలో Tsunami వేగం ఎక్కువ (గంటకు సుమారు 800 km), ఎత్తు తక్కువ; తీరం దగ… | P036-F014 (no speed) | N064 |  |
| F114 | tsunami | 26 డిసెంబర్ 2004 Indian Ocean Tsunami కి కారణం ఉత్తర Sumatra దగ్గర వచ్చిన Sumatr… | P036-F015 | — |  |
| F115 | tsunami | 2004 Tsunami లో భారతదేశంలో అత్యంత తీవ్రంగా నష్టపోయిన జిల్లా Tamil Nadu లోని Naga… | P036-F016 | — |  |
| F116 | tsunami | భారత Tsunami ముందస్తు హెచ్చరిక కేంద్రం (ITEWC) Hyderabad లోని INCOIS లో ఉంది; 20… | — | N063 |  |
| F117 | volcano-anatomy | Buoyancy, వాయువుల ఒత్తిడి, రాతి పగుళ్లు, Tectonic పరిస్థితులు కలిసి Magma ను పైక… | P037-F020 | — |  |
| F118 | volcano-anatomy | అగ్నిపర్వత వాయువుల్లో నీటి ఆవిరి (Water vapour) అత్యధికం; తరువాత Carbon dioxide,… | P037-F003, P040-F001 | — |  |
| F119 | volcano-anatomy | భూమి లోపల Magma నిలిచి ఉండే స్థలాన్ని Magma chamber (శిలాద్రవపు నిలువ) అంటారు. | P037-F004 | — |  |
| F120 | volcano-anatomy | Magma chamber నుంచి Magma పైకి వచ్చే మార్గాన్ని Volcanic pipe లేదా Conduit అంటార… | P037-F005, P037-F006 | — |  |
| F121 | volcano-anatomy | Vent చుట్టూ ఉండే గిన్నె ఆకారపు గుంటను Crater అంటారు; అందులో నీరు చేరితే Crater l… | P037-F007 (no crater lake) | N067 |  |
| F122 | volcano-anatomy | Magma chamber ఖాళీ అయి శిఖరం లోపలికి కూలడం వల్ల ఏర్పడే పెద్ద గుంటను (సాధారణంగా 1… | P037-F008, 06-011 | — |  |
| F123 | volcano-anatomy | Maharashtra లోని Buldhana జిల్లాలో ఉన్న Lonar సరస్సు ఉల్కాపాతం (Meteorite impact… | P037-F009 | — |  |
| F124 | volcano-anatomy | ఒకే ప్రధాన Vent గుండా జరిగే విస్ఫోటనాన్ని Central eruption (కేంద్ర విస్ఫోటనం) అం… | P037-F010 | — |  |
| F125 | volcano-anatomy | పొడవైన పగుళ్ల వెంట పల్చని Lava బయటికి ప్రవహించడాన్ని Fissure eruption (విదర విస్… | P037-F014 | N068 |  |
| F126 | volcano-anatomy | Deccan Traps Fissure eruption వల్ల ఏర్పడిన Flood basalt; ప్రధాన దశ సుమారు 6.6 కో… | P037-F015 (age only) | N026, N068 |  |
| F127 | volcano-anatomy | Andhra Pradesh లో Rajahmundry దగ్గర ఉన్న Rajahmundry Traps, Deccan Lava ప్రవాహాల… | — | N065 |  |
| F128 | volcano-anatomy | Silica శాతం పెరిగితే Lava Viscosity పెరుగుతుంది; వాయువు బయటికి పోలేక విస్ఫోటనం ప… | P037-F017, 06-023 | N069, N074, N076 |  |
| F129 | volcano-anatomy | Silica 63% పైన ఉన్న Lava ఆమ్ల లావా (Acidic, Felsic); Silica 45–52% ఉన్న Basalt L… | P037-F018, P037-F019 | N069 |  |
| F130 | volcano-anatomy | విస్ఫోటన రకాలు తక్కువ నుంచి ఎక్కువ ఉగ్రానికి: Hawaiian, Strombolian, Vulcanian, … | — | N066 |  |
| F131 | volcano-anatomy | నునుపైన, తాళ్ల లాంటి Lava ఉపరితలం Pahoehoe; గరుకైన, ముక్కల Lava ఉపరితలం Aa; నీటి… | — | N067, N070 |  |
| F132 | volcano-types | పలుచని Basalt Lava ప్రవాహాలతో వెడల్పుగా, మెల్లగా వాలుగా ఏర్పడే అగ్నిపర్వతాన్ని S… | 06-009 | N074 |  |
| F133 | volcano-types | Lava ప్రవాహాలు, Pyroclast పొరలు మార్చి మార్చి పేరుకుని ఏర్పడే అగ్నిపర్వతాన్ని Co… | 06-010, P037-F013 | — |  |
| F134 | volcano-types | Vent చుట్టూ రాలిన చిన్న రాతి ముక్కలతో ఏర్పడే చిన్న, నిటారు కొండను Cinder cone అం… | P037-F011 | — |  |
| F135 | volcano-types | చిక్కని Lava Vent దగ్గరే ఉబ్బి గుమ్మటంలా పేరుకుంటే దాన్ని Lava dome అంటారు. | P037-F012 | — |  |
| F136 | volcano-types | NCERT ప్రకారం అగ్నిపర్వతాల రకాలు ఐదు: Shield, Composite, Caldera, Flood basalt p… | — | N071 |  |
| F137 | volcano-types | మళ్లీ బద్దలయ్యే అవకాశం ఉండి ప్రస్తుతం నిశ్శబ్దంగా ఉన్న అగ్నిపర్వతాన్ని Dormant v… | P038-F002 | N072, N073 |  |
| F138 | volcano-types | భవిష్యత్తులో బద్దలయ్యే అవకాశం లేదని చరిత్ర, Magma ఆధారాలు చూపే అగ్నిపర్వతాన్ని E… | P038-F003 | N072, N073 |  |
| F139 | volcano-types | Ojos del Salado (Chile–Argentina సరిహద్దు) సముద్ర మట్టం నుంచి ప్రపంచంలో ఎత్తైన అ… | P038-F006 | — |  |
| F140 | volcano-types | తరచు జరిగే చిన్న పేలుళ్ల వల్ల Italy లోని Stromboli ని "Lighthouse of the Mediter… | P038-F008 | — |  |
| F141 | volcano-types | Merapi, Bromo, Semeru అగ్నిపర్వతాలు Indonesia లోని Java దీవిలో ఉన్నాయి. | P038-F011 | — |  |
| F142 | volcano-types | Andaman సముద్రంలోని Barren Island భారతదేశంలో ఏకైక చురుకైన అగ్నిపర్వతం. | P038-F012 | — |  |
| F143 | volcano-types | USGS ప్రకారం Mount Rainier చురుకైన అగ్నిపర్వతం; దాని ముఖ్య ప్రమాదం Lahar. | P038-F016 | — |  |
| F144 | volcano-types | వేడి వాయువు, బూడిద, రాతి ముక్కలు కలిసి నేలను అంటుకుని వేగంగా దూసుకుపోయే ప్రవాహాన… | 06-012, P038-F018 | — |  |
| F145 | volcano-types | అగ్నిపర్వతపు బూడిద, రాళ్లు నీటితో కలిసి లోయల వెంట పారే బురద ప్రవాహాన్ని Lahar అం… | P038-F019 | — |  |
| F146 | intrusive | రాతి పొరలను అడ్డంగా కోస్తూ నిలువుగా గట్టిపడిన Magma పలకను Dyke (డైక్) అంటారు. | P038-F020 | — |  |
| F147 | intrusive | రాతి పొరలకు సమాంతరంగా వాటి మధ్య గట్టిపడిన Magma పలకను Sill (సిల్) అంటారు. | P038-F021 | — |  |
| F148 | intrusive | ఆకారాలు: Laccolith = గుమ్మటం పైకప్పు; Lopolith = సాసర్; Phacolith = ముడత వంపులో … | P039-F001 to P039-F006, P039-M001 | N075 |  |
| F149 | volcano-products | అగ్నిపర్వత పేలుడులో పుట్టి బయటికి విసిరిన రాతి ముక్కలను Pyroclast అంటారు. | P039-F010 | N076 |  |
| F150 | volcano-products | 2 mm కంటే చిన్న Pyroclast ను Volcanic ash, 2–64 mm వాటిని Lapilli అంటారు. | P039-F011, P039-F012 | — |  |
| F151 | volcano-products | ఎక్కువ రంధ్రాల వల్ల బరువు తక్కువై నీటిలో తేలే అగ్నిపర్వత శిల Pumice. | P039-F015 | — |  |
| F152 | volcano-products | పలుచని Lava సాగి చల్లబడి ఏర్పడే సన్నని గాజు దారాలను Pele's hair అంటారు. | P039-F017 | — |  |
| F153 | hot-springs | భూమి లోపల వేడెక్కిన భూగర్భ జలం సహజంగా పైకి వచ్చే చోటును Hot spring (వేడి నీటి బు… | P040-F009 | — |  |
| F154 | hot-springs | సన్నని లోపలి దారి, వేడి, ఒత్తిడి వల్ల విరామాలతో వేడి నీరు, ఆవిరి చిమ్మే బుగ్గను … | P040-F012 | N078 |  |
| F155 | hot-springs | ప్రధానంగా ఆవిరి, వాయువులు మాత్రమే బయటికి వచ్చే రంధ్రాన్ని Fumarole అంటారు. | P040-F014 | — |  |
| F156 | hot-springs | భారతదేశంలో Mud volcanoes ముఖ్యంగా Andaman లోని Baratang దీవిలో ఉన్నాయి. | — | N077 |  |
| F157 | hot-springs | భూమి లోపలి వేడి నుంచి పొందే శక్తిని Geothermal energy అంటారు. | P040-F010 | N078 |  |
| F158 | volcano-distribution | Pacific మహాసముద్రం చుట్టూ Subduction zones, అగ్నిపర్వతాలు, భూకంపాలు ఉన్న పట్టీని… | P041-F001 | N080 |  |
| F159 | volcano-distribution | ప్రపంచ అగ్నిపర్వతాల్లో సుమారు 75% Pacific Ring of Fire లో ఉన్నాయి. | — | N079 |  |
| F160 | weathering | రాయి పగుళ్లలోని నీరు పదే పదే గడ్డకట్టి కరుగుతూ పగుళ్లను వెడల్పు చేయడాన్ని Frost … | O005 | — |  |
| F161 | weathering | రాయి బయటి పొరలు ఉల్లిపాయ పొట్టులా ఊడటాన్ని Exfoliation అంటారు; దీనికి కారణాలు పగ… | — | N081 |  |
| F162 | weathering | Carbon dioxide కలిసిన నీరు Carbonic acid గా మారి సున్నపురాయిని కరిగించడాన్ని Car… | O007 | — |  |
| F163 | weathering | ఇనుము ఉన్న ఖనిజాలు ఆక్సిజన్‌తో చర్య జరిపి ఎరుపు–గోధుమ రంగుకు మారడాన్ని Oxidation… | O006 | — |  |
| F164 | weathering | నీటితో చర్య వల్ల Feldspar బంకమట్టిగా మారడం Hydrolysis కు ఉదాహరణ. | — | N082 |  |
| F165 | weathering | శైథిల్యం వల్ల రాయి మీద ఏర్పడే వదులు ముక్కల పొరను Regolith అంటారు; Weathering వల్… | — | N083 |  |
| F166 | mass-wasting | Gravity వల్ల వాలు మీది మట్టి, రాళ్లు మొత్తంగా కిందకు కదలడాన్ని Mass wasting (Mas… | O023 | — |  |
| F167 | mass-wasting | వాలు మీది మట్టి కంటికి కనిపించనంత నెమ్మదిగా కిందకు జరగడాన్ని Soil creep అంటారు; … | O010 | N085 |  |
| F168 | mass-wasting | NCERT ప్రకారం Mass movements: నెమ్మదివి Creep, Solifluction; వేగమైనవి Earthflow,… | O009, O012, O015 (partial) | N084 |  |
| F169 | mass-wasting | భారతదేశంలో కొండచరియల (Landslides) అధ్యయనానికి కేంద్ర సంస్థ Geological Survey of … | — | N085 |  |
| F170 | erosion-deposition | పారే నీరు, గాలి, మంచు, అలలు వంటి Agents రాయిని, మట్టిని తొలగించడాన్ని Erosion (క… | O002, O001 | — |  |
| F171 | erosion-deposition | Agent తొలగించిన పదార్థం దానితో పాటు కదులుతూ ఉండే దశను Transportation అంటారు; Sol… | O003 (no modes) | N086, N087 |  |
| F172 | erosion-deposition | Agent వేగం, మోసే శక్తి తగ్గినప్పుడు అది మోస్తున్న పదార్థాన్ని వదిలి పేరుకోవడాన్న… | O004 | N087 |  |
| F173 | erosion-deposition | Meander మలుపులో బయటి ఒడ్డు కోతకు గురవుతుంది, లోపలి ఒడ్డున ఇసుక పేరుకుంటుంది. | O022 | — |  |
| F174 | erosion-deposition | మెత్తని రాయి త్వరగా కోసుకుపోయి గట్టి రాయి ఎత్తుగా మిగలడాన్ని Differential erosio… | O024 | — |  |
