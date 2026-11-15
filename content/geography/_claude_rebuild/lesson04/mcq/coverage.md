# Lesson 4 — fact coverage and new MCQs

Source: ch04/FINAL/lesson_04_rebuilt.md — 178 `::: fact` blocks, numbered F001–F178 in lesson order (facts.txt). Existing = mcq04/FINAL/04.patched.json, only questions with a non-null `lesson04_section` (268), matched to facts by meaning (existing_map.py). Ids shortened: `P025-F005` = GEO-BOOK-P025-F005, `O001` = GEO-ORIG-04-001, `N012` = GEO-NEW-04-012 (new_questions.json).

## Totals

- Facts: 178. Tested by existing questions: 144. Previously untested facts now covered by new questions: 34. Left without any question: 0.
- New questions: 55. Answer key spread: A=12, B=14, C=14, D=15.
- Format mix: concept 18, reasoning 13, assertion-reason 7, application 6, statements 5, matching 4, sequence 2. Assertion–reason keys: A=2, B=1, C=2, D=2. Match keys: A–2;B–4;C–3;D–1, A–3;B–2;C–1;D–4, A–2;B–1;C–3;D–4, A–4;B–2;C–3;D–1.
- "How to answer" questions for the changing facts (flag `how_to_answer: true`; the rule is in the explanation, the stem is a plain question): N005, N015, N039, N042, N051 — in that order: shadow-zone angles, inner-core radius, Earth's age, ICS dates, Homo sapiens age.
- Validator (build.py): 0 length flags, 0 errors, 0 warnings.

## Per section

| Section | Facts | Existing-covered | New-covered | New Qs | Why/how new Qs |
|---|---|---|---|---|---|
| interior-evidence | 5 | 5 | 2 | 1 | N001 |
| depth-changes | 8 | 8 | 4 | 2 | N003 |
| seismic-evidence | 12 | 12 | 6 | 3 | N004 |
| crust | 15 | 12 | 8 | 5 | N009 |
| mantle-core | 15 | 13 | 9 | 5 | N016 |
| mechanical-layers | 6 | 5 | 5 | 3 | N019 |
| mineral-rock | 9 | 7 | 6 | 3 | N022 |
| igneous | 15 | 15 | 3 | 3 | N023 |
| sedimentary | 21 | 18 | 4 | 3 | N028 |
| metamorphic | 16 | 12 | 7 | 5 | N036 |
| rock-cycle | 2 | 0 | 2 | 2 | N033 |
| chondrite | 1 | 1 | 1 | 1 | N035 |
| earth-age | 6 | 4 | 4 | 4 | N037, N040 |
| time-scale | 8 | 7 | 4 | 3 | N043 |
| precambrian | 7 | 3 | 5 | 4 | N045, N047 |
| paleozoic | 11 | 10 | 3 | 1 | N048 |
| meso-cenozoic | 13 | 11 | 4 | 3 | N050 |
| ap-link | 8 | 1 | 8 | 4 | N052 |

## Fact table

| Fact | Section | Fact (short) | Existing | New | Note |
|---|---|---|---|---|---|
| F001 | interior-evidence | ప్రపంచంలో అత్యంత లోతైన Borehole రష్యాలోని Kola Superdeep Borehole; 1989 లో సుమార… | P025-F005 | — |  |
| F002 | interior-evidence | 1960 లో Trieste వాహనంలో Jacques Piccard, Don Walsh Mariana Trench లోని Challenge… | P025-F004 | — |  |
| F003 | interior-evidence | గనులు (Mines), Boreholes, అగ్నిపర్వత పదార్థాలు భూమి లోపలికి ప్రత్యక్ష ఆధారాలు (D… | P025-F002, P025-F008 | — |  |
| F004 | interior-evidence | Seismic waves, Gravity, Magnetic field, Heat flow, Meteorites భూమి లోపలికి పరోక్… | P025-F003, P026-F006 | N001 |  |
| F005 | interior-evidence | భూమి లోపలి నిర్మాణానికి అత్యంత బలమైన ఆధారం Seismic waves. | P026-F005 (partial) | N001 |  |
| F006 | depth-changes | లోతుకు వెళ్లే కొద్దీ ఒక ప్రమాణ లోతుకు Temperature మారే రేటును Geothermal gradien… | P025-F009 | N002 |  |
| F007 | depth-changes | ఉపరితలం దగ్గర ప్రతి 32 m లోతుకు సుమారు 1°C Temperature పెరుగుతుంది (NCERT). | P025-F010 | N002 |  |
| F008 | depth-changes | భూమి కేంద్రం Temperature సుమారు 5,000–6,000°C. | P025-F012 | — |  |
| F009 | depth-changes | ఒక చదరపు ప్రమాణ వైశాల్యం మీద పడే బలాన్ని Pressure (పీడనం) అంటారు. | P026-F001 | — |  |
| F010 | depth-changes | పై పొరల బరువు వల్ల లోతుకు వెళ్లే కొద్దీ Pressure పెరుగుతుంది. | P026-F004 | — |  |
| F011 | depth-changes | భూమి సగటు Density సుమారు 5.51 g/cm³ (NASA: 5.513 g/cm³). | P025-F014 | N003 |  |
| F012 | depth-changes | లోతుకు వెళ్లే కొద్దీ Density పెరుగుతుంది; పొరల సరిహద్దుల దగ్గర హఠాత్తుగా పెరుగుత… | P025-F013 | N003 |  |
| F013 | depth-changes | Inner core Density సుమారు 13 g/cm³. | P025-F015 | — |  |
| F014 | seismic-evidence | P wave Compressional (Longitudinal) Body wave; ఘనం, ద్రవం, వాయువు మూడింటిలోనూ ప్… | P035-F001, P035-F002, O013 | — |  |
| F015 | seismic-evidence | P wave అన్ని Seismic waves కంటే వేగవంతమైనది; అందుకే మొదట చేరుతుంది. | P035-F001, P035-F006 | — |  |
| F016 | seismic-evidence | S wave Shear (Transverse) wave; కణాలు తరంగ దిశకు లంబంగా కదులుతాయి. | P035-F004, O014 | — |  |
| F017 | seismic-evidence | Shear rigidity లేనందువల్ల S wave ద్రవాల్లో ప్రయాణించదు. | P035-F005 | N004 |  |
| F018 | seismic-evidence | P waves, S waves ను Body waves అంటారు. | P035-F009 | — |  |
| F019 | seismic-evidence | Seismic waves చేరే క్రమం: P wave, తరువాత S wave, చివరగా Surface waves. | P035-F017 | — |  |
| F020 | seismic-evidence | Seismic waves వేగం పదార్థం Elastic properties, Density, స్థితి (ఘనం/ద్రవం) మీద ఆ… | P035-F003, P027-F003 | — |  |
| F021 | seismic-evidence | S wave shadow zone: భూకంప కేంద్రం నుంచి సుమారు 103° దాటిన ప్రాంతం. | P035-F008, P035-M002 | N004, N005 |  |
| F022 | seismic-evidence | P wave shadow zone: భూకంప కేంద్రం నుంచి సుమారు 103° నుంచి 140° మధ్య ప్రాంతం. | P035-F007 | N005 |  |
| F023 | seismic-evidence | S waves Core దాటలేకపోవడం Outer core ద్రవం అనడానికి ప్రధాన ఆధారం. | P027-F014 (explanation only) | N004 |  |
| F024 | seismic-evidence | 1906 లో R. D. Oldham భూమికి Core ఉందని Seismic నమోదుల నుంచి గుర్తించాడు. | P027-F018 | N006 |  |
| F025 | seismic-evidence | 1936 లో Inge Lehmann Inner core ను కనుగొంది. | P028-F001 | N006 |  |
| F026 | crust | కూర్పు బట్టి చేసిన విభజనలో భూమి పైపొర Crust (భూపటలం). | O001, P026-F011, P026-F010 | — |  |
| F027 | crust | Oceanic crust మందం సుమారు 5–10 km; ఇది Basalt, Gabbro తో ఏర్పడింది. | P026-F012, P027-F001 | — |  |
| F028 | crust | Continental crust మందం సుమారు 30–70 km, సగటు సుమారు 35 km; ఇది Granitic శిలలతో ఏ… | P026-F013, P026-F018 | — |  |
| F029 | crust | పెద్ద పర్వతాల కింద Crust మందంగా, Mantle లోకి వేర్లు (Roots) లాగా దిగి ఉంటుంది. | P026-F014 | N009 |  |
| F030 | crust | తేలికైన Crust బరువైన Mantle మీద సమతుల్యంగా తేలే సూత్రాన్ని Isostasy (సమస్థితి) అ… | — | N007, N009 |  |
| F031 | crust | Isostasy కి George Airy (పర్వతాల వేర్ల లోతు తేడా), John Pratt (శిలల Density తేడా… | — | N008 |  |
| F032 | crust | Oceanic crust (సుమారు 3.0 g/cm³) Continental crust (సుమారు 2.7 g/cm³) కంటే బరువై… | P027-F002 | — |  |
| F033 | crust | Crust భూమి ద్రవ్యరాశిలో 1% కంటే తక్కువ. | P026-F015 | — |  |
| F034 | crust | Silica, Aluminium ఎక్కువగా ఉండే ఖండ Crust ను SIAL అంటారు. | P026-F007 | N011 |  |
| F035 | crust | Silica, Magnesium ఎక్కువగా ఉండే సముద్ర Crust ను SIMA అంటారు. | P026-F008 | N011 |  |
| F036 | crust | Continental crust పై, కింది భాగాల మధ్య సరిహద్దును Conrad discontinuity అంటారు. | P026-F017 | — |  |
| F037 | crust | Crust, Mantle మధ్య సరిహద్దును Moho (Mohorovičić discontinuity) అంటారు. | O007, P027-F004 | N013 |  |
| F038 | crust | Crust లో అత్యధికంగా ఉండే మూలకం Oxygen (సుమారు 46.6%), రెండోది Silicon (సుమారు 27… | P028-F013, F014, F015, M004, M005 | — |  |
| F039 | crust | Crust లో అత్యధికంగా ఉండే లోహం Aluminium; రెండోది Iron. | — | N010 |  |
| F040 | crust | భూమి మొత్తం ద్రవ్యరాశిలో అత్యధికంగా ఉండే మూలకం Iron. | P028-F012 | N010 |  |
| F041 | mantle-core | Mantle (ప్రావారం) Crust, Core మధ్య ఉండే Silicate రాతి పొర; Moho నుంచి సుమారు 2,8… | O002, P027-F005 | — |  |
| F042 | mantle-core | Mantle భూమి ద్రవ్యరాశిలో సుమారు 67–68%; ఇది భూమిలో అతి పెద్ద పొర. | P027-F007 | — |  |
| F043 | mantle-core | Mantle Density సుమారు 3.3 నుంచి 5.6 g/cm³ వరకు పెరుగుతుంది. | P027-F008 | — |  |
| F044 | mantle-core | Mantle ఎక్కువగా ఘనం; అయినా చాలా ఎక్కువ కాలంలో నెమ్మదిగా ప్రవహిస్తుంది. | P027-F006 | — |  |
| F045 | mantle-core | సుమారు 660 km లోతులో ఖనిజాల Phase change Upper mantle, Lower mantle ను వేరు చేస్… | P027-F010 | N012 |  |
| F046 | mantle-core | Upper mantle, Lower mantle మధ్య సరిహద్దును Repetti discontinuity అంటారు (సుమారు … | — | N012, N013 |  |
| F047 | mantle-core | భూమి లోపలి వేడి వల్ల Mantle లో నెమ్మదైన Convection జరుగుతుంది. | P027-F013 | — |  |
| F048 | mantle-core | Mantle, Outer core మధ్య సుమారు 2,890 km లోతులో ఉండే సరిహద్దును Gutenberg discont… | P027-F014, O008 | N013 |  |
| F049 | mantle-core | Core వ్యాసార్ధం సుమారు 3,480 km; ఇది ప్రధానంగా Iron, Nickel తో పాటు కొన్ని తేలిక… | P027-F015, P027-F016 | N015 |  |
| F050 | mantle-core | Nickel, Ferrum (Iron) తో ఏర్పడిన Core ను NIFE అంటారు. | P026-F009 | — |  |
| F051 | mantle-core | Outer core ద్రవ Iron మిశ్రమం; సుమారు 2,890 km నుంచి 5,150 km లోతు వరకు, మందం సుమ… | O003, P028-F002, P028-F003 | N015 |  |
| F052 | mantle-core | Outer core లో ద్రవ Iron కదలిక (Geodynamo) భూమి Magnetic field ను సృష్టిస్తుంది. | P027-F017 | N016 |  |
| F053 | mantle-core | Inner core వ్యాసార్ధం సుమారు 1,220 km; భారీ Pressure వల్ల ఇది ఘనంగా ఉంది. | O004, P028-F004, P028-F005 | N015 |  |
| F054 | mantle-core | Outer core, Inner core మధ్య సుమారు 5,150 km లోతులో ఉండే సరిహద్దును Lehmann disco… | — | N013 |  |
| F055 | mantle-core | పాత విభజనలో Pyrosphere అంటే దాదాపు Mantle; Barysphere అంటే భూమి లోపలి బరువైన భాగ… | P028-F010 (Barysphere only) | N014 |  |
| F056 | mechanical-layers | భూమి పొరలను రెండు విధాలుగా విభజిస్తారు: Composition బట్టి (Crust, Mantle, Core),… | P028-F006, P026-F010 | — |  |
| F057 | mechanical-layers | Crust, దాని కింద ఉండే గట్టి Mantle పై భాగం, ఈ రెండూ కలిసి Lithosphere (శిలావరణం)… | O005, P027-F012, P028-F007 | N018 |  |
| F058 | mechanical-layers | Lithosphere కింద ఉండే Mantle భాగం Asthenosphere; ఇది ఎక్కువగా ఘనమే, కానీ మెత్తగా… | O006, P027-F009, O030 | N019 |  |
| F059 | mechanical-layers | Asthenosphere మందం ప్రాంతాన్ని బట్టి మారుతుంది; NCERT ప్రకారం సుమారు 400 km లోతు… | P028-F008 (no figure) | N018, N019 |  |
| F060 | mechanical-layers | Asthenosphere కింద గట్టిగా ఉండే Mantle భాగాన్ని Mesosphere అంటారు. | P028-F009 | N018 |  |
| F061 | mechanical-layers | అగ్నిపర్వతాల Magma కు ప్రధాన మూలం Asthenosphere (NCERT). | — | N017 |  |
| F062 | mineral-rock | సహజంగా ఏర్పడిన, Inorganic, ఘన పదార్థం; లోపల క్రమమైన Crystal structure, నిర్దిష్ట… | P042-F001 | N022 |  |
| F063 | mineral-rock | Rock (శిల) అంటే ఒకటి లేదా అంతకంటే ఎక్కువ Minerals కలిసిన సహజ ఘన పదార్థం. | P042-F002 (implicit) | N022 |  |
| F064 | mineral-rock | Crust లో అత్యధికంగా ఉండే Mineral గుంపు Feldspar. | — | N020 |  |
| F065 | mineral-rock | Rock salt లో ముఖ్య Mineral Halite; Quartzite లో ముఖ్య Mineral Quartz. | P042-F003 | — |  |
| F066 | mineral-rock | Dunite అనేది దాదాపు పూర్తిగా Olivine తో నిండిన Ultramafic శిల. | P042-F004 | — |  |
| F067 | mineral-rock | Mica (అభ్రకం) అనేది పలుచని పొరలుగా విడిపోయే Silicate minerals గుంపు. | P042-F022, P043-F018 | N021 |  |
| F068 | mineral-rock | Andhra Pradesh లోని Nellore Mica belt భారతదేశంలో ప్రసిద్ధ Mica ప్రాంతం. | — | N021 |  |
| F069 | mineral-rock | Mohs scale లో Talc కాఠిన్యం 1 (అత్యంత మెత్తనిది), Diamond కాఠిన్యం 10 (అత్యంత గట… | P043-F023, P043-F024 | N022 |  |
| F070 | mineral-rock | పుట్టుక (Origin) ఆధారంగా శిలలు మూడు రకాలు: Igneous, Sedimentary, Metamorphic. | P042-F005, O019 | — |  |
| F071 | igneous | Magma (శిలాద్రవం) అంటే భూ ఉపరితలం కింద ఉండే కరిగిన లేదా సగం కరిగిన శిల; అది ఉపరి… | O012 | — |  |
| F072 | igneous | Magma లేదా Lava చల్లబడి గట్టిపడి ఏర్పడే శిలలను Igneous rocks (అగ్ని శిలలు) అంటార… | P042-F006, O009 (formation only) | N023 |  |
| F073 | igneous | భూమి లోపల లోతులో నెమ్మదిగా చల్లబడటం వల్ల Plutonic rocks లో పెద్ద Crystals (Coars… | P042-F007 | — |  |
| F074 | igneous | తక్కువ లోతులో గట్టిపడే Intrusive శిలలను Hypabyssal rocks అంటారు; Dolerite (Diaba… | P042-F008, P042-F011 | — |  |
| F075 | igneous | Lava త్వరగా చల్లబడటం వల్ల Volcanic (Extrusive) rocks లో చిన్న Crystals గానీ Glas… | P042-F009 | — |  |
| F076 | igneous | Granite, Syenite, Gabbro, Diorite లు Plutonic rocks; Dolerite Hypabyssal rock; B… | P042-F010, P042-F012, O032 | — |  |
| F077 | igneous | Basalt (45–52% Silica) Mafic; Andesite (57–63%) Intermediate; Rhyolite (సుమారు 6… | P040-F003, P040-F004, P040-F005 | — |  |
| F078 | igneous | Gabbro Mafic, Diorite Intermediate, Granite Felsic plutonic rock; Dunite, Perido… | P042-M002/M003 (partial) | N024 |  |
| F079 | igneous | Oceanic crust లో ఎక్కువగా ఉండే శిల Basalt; Continental crust లో ఎక్కువగా ఉండేది … | P027-F001, P026-F018 | — |  |
| F080 | igneous | Trachyte, Alkali ఎక్కువ ఉండే Intermediate volcanic rock; దీని Plutonic జంట Syeni… | P042-F013 (name only) | N025 |  |
| F081 | igneous | Lava గట్టిపడేటప్పుడు వాయు బుడగలు వదిలిన ఖాళీలను Vesicles అంటారు; Pumice, Scoria … | P042-F015 | — |  |
| F082 | igneous | Magma, Lava అధిక ఉష్ణోగ్రత జీవ అవశేషాలను నాశనం చేస్తుంది కాబట్టి Igneous rocks ల… | P042-F016 | — |  |
| F083 | igneous | Kimberlite అనేది Mantle లోతుల నుంచి వచ్చిన Ultramafic igneous rock; కొన్ని Kimbe… | P040-F006 | — |  |
| F084 | igneous | Kimberlite ఎక్కువగా నిలువు క్యారెట్ ఆకారపు గొట్టాలుగా (Kimberlite pipes) దొరుకుత… | P040-M002 (partial) | — |  |
| F085 | igneous | Tokapal Kimberlite వ్యవస్థ ఉన్న Bastar, Chhattisgarh రాష్ట్రంలో ఉంది. | P040-F008 | — |  |
| F086 | sedimentary | శిల ఉన్న చోటే పగలడం Weathering; ఆ ముక్కలను వేరే చోటికి మోసుకుపోవడం Erosion — ఈ క… | P042-F017 | — |  |
| F087 | sedimentary | వదులుగా ఉన్న Sediment నొక్కుకుపోయి, సిమెంట్ లా అతుక్కుని గట్టి శిలగా మారడాన్ని L… | P042-F018 | — |  |
| F088 | sedimentary | Sediment పేరుకుపోయి Lithification చెందడం వల్ల, లేదా రసాయన / జీవ పదార్థాలు పేరుకు… | O010 | — |  |
| F089 | sedimentary | Conglomerate లో పెద్ద ముక్కలు గుండ్రంగా (Rounded) ఉంటాయి; Breccia లో పెద్ద ముక్క… | P042-F019 | — |  |
| F090 | sedimentary | ఇసుక గింజలు పేరుకుపోయి సిమెంట్ తో అతుక్కుంటే Sandstone ఏర్పడుతుంది. | P042-F023 | — |  |
| F091 | sedimentary | సన్నని Silt, Clay గింజలు పేరుకుపోయి గట్టిపడితే Shale, Mudstone ఏర్పడతాయి. | P042-F024 | — |  |
| F092 | sedimentary | గాలి మోసుకొచ్చి పేర్చిన, ముఖ్యంగా Silt తో కూడిన Sediment ను Loess అంటారు. | P042-F020 | — |  |
| F093 | sedimentary | Glacier నేరుగా వదిలిన Sediment ను Till అంటారు; Till గట్టిపడితే Tillite అవుతుంది;… | P042-F021 | — |  |
| F094 | sedimentary | ఉప్పు నీరు ఆవిరైపోయి, కరిగిన లవణాలు పేరుకుపోతే Rock salt ఏర్పడుతుంది. | P042-F025 | — |  |
| F095 | sedimentary | Gypsum, Anhydrite రెండూ Calcium sulphate Minerals; Gypsum లో నీరు ఉంటుంది, Anhyd… | P042-F026 | — |  |
| F096 | sedimentary | Chert ముఖ్యంగా చాలా సన్నని Quartz తో తయారవుతుంది; Flint అనేది Chert లో ఒక రకం. | P042-F027 | — |  |
| F097 | sedimentary | Iron అధికంగా ఉండే పొరలు, Silica (Chert) అధికంగా ఉండే పొరలు మార్చి మార్చి ఉండే Se… | P042-F028 | N047 |  |
| F098 | sedimentary | సముద్ర జీవుల Calcium carbonate గవ్వలు పేరుకుపోయి Limestone ఏర్పడుతుంది; Chalk అన… | P042-F029 | — |  |
| F099 | sedimentary | మొక్కల అవశేషాలు పేరుకుపోయి, చాలా కాలం లోతులో కూరుకుపోయి మారితే Coal ఏర్పడుతుంది. | P042-F030, P030-F001 | — |  |
| F100 | sedimentary | భారతదేశ బొగ్గు (Singareni, Godavari లోయ, Damodar లోయ) ఎక్కువగా Permian కాలపు Gon… | — | N026 |  |
| F101 | sedimentary | Calcium, Magnesium carbonate తో ఏర్పడిన Limestone లాంటి Sedimentary శిలను Dolomi… | — | N027 |  |
| F102 | sedimentary | ఖండాల ఉపరితలంలో సుమారు 75% ను Sedimentary శిలలు కప్పుతాయి; కానీ Crust Volume లో … | — | N028 |  |
| F103 | sedimentary | Sedimentary శిలల్లోని పొరలు అవి పేరుకుపోయిన చరిత్రను చూపిస్తాయి; తరువాత ఈ పొరలు … | P043-F001 | — |  |
| F104 | sedimentary | Sedimentary శిలల గట్టిదనం వాటి Minerals, Cementation, Weathering స్థితిని బట్టి … | P043-F002 | — |  |
| F105 | sedimentary | Sediment జీవ అవశేషాలను కప్పేసి, ఎక్కువ వేడి లేకుండానే శిలగా మారుతుంది కాబట్టి Fo… | P043-F003 | — |  |
| F106 | sedimentary | Petroleum, Natural gas ముఖ్యంగా జీవ పదార్థం ఉన్న, సరైన లోతు–వేడి చరిత్ర ఉన్న Sed… | P043-F004 | — |  |
| F107 | metamorphic | ఉన్న శిలలోని Minerals, నిర్మాణం ముఖ్యంగా ఘన స్థితిలోనే వేడి, పీడనం, ద్రవాల వల్ల … | P043-F005, O011, O029 | — |  |
| F108 | metamorphic | Metamorphism కు ముందు ఉన్న అసలు శిలను Protolith అంటారు. | P043-F006 | — |  |
| F109 | metamorphic | వేడి Magma తాకిడి వల్ల పక్క శిలలు ఘన స్థితిలోనే వేడితో మారడాన్ని Contact metamor… | P043-F007 | — |  |
| F110 | metamorphic | Fault వెంట కదలిక వల్ల శిలలు నలిగి, పగిలి, వికృతమవడాన్ని Dynamic metamorphism అంట… | P043-F008 | — |  |
| F111 | metamorphic | పర్వతాలు ఏర్పడేటప్పుడు విశాల ప్రాంతంలో వేడి, పీడనం, వంగడం కలిసి శిలలను మార్చడాన్… | P043-F009 | N036 |  |
| F112 | metamorphic | ద్రవాలు పదార్థాన్ని చేర్చి లేదా తీసివేసి శిల మొత్తం రసాయన కూర్పును గణనీయంగా మార్… | P043-F010 | — |  |
| F113 | metamorphic | Dunite లోకి ద్రవాలు చేరితే Serpentinisation జరిగి Serpentinite గానీ, Talc అధికంగ… | P043-F019 | — |  |
| F114 | metamorphic | Metamorphic grade పెరిగే క్రమం: Shale → Slate → Phyllite → Schist → Gneiss. | — | N030 |  |
| F115 | metamorphic | Schist ను గుర్తించడానికి ముఖ్య లక్షణం Mica వంటి Minerals ఒకే దిశలో పేర్చుకొని ఉం… | P043-F011 | N036 |  |
| F116 | metamorphic | Gneiss లో వేర్వేరు Mineral గుంపులతో ఏర్పడిన లేత, ముదురు పట్టీలు (Bands) ఉంటాయి. | P043-F012 | — |  |
| F117 | metamorphic | Sandstone → Quartzite, Limestone → Marble, Shale → Slate, Granite → Gneiss, Basa… | P043-F013, F014, F015, F016, F017, F021, M004 | — |  |
| F118 | metamorphic | Carbon శాతం పెరిగే క్రమంలో బొగ్గు రకాలు: Peat → Lignite → Bituminous → Anthracit… | P043-M006 (partial) | N029 |  |
| F119 | metamorphic | Anthracite అత్యధిక Carbon (సుమారు 80–95%; కొన్ని Geology పుస్తకాల్లో 86–97%) ఉండ… | P043-F022 | — |  |
| F120 | metamorphic | Charnockite అనేది Orthopyroxene (Hypersthene) ఉండే Granite లాంటి ఎక్కువ స్థాయి M… | — | N031, N032 |  |
| F121 | metamorphic | Charnockite ను మొదట Chennai లోని St. Thomas Mount నుంచి వివరించారు. | — | N032 |  |
| F122 | metamorphic | Khondalite కు Odisha లోని Khond గిరిజనుల పేరు మీద పేరు వచ్చింది; ఇది Eastern Gha… | — | N031 |  |
| F123 | rock-cycle | Rock cycle లో ఏ రకం శిల అయినా మిగతా రెండు రకాల్లో దేనిగానైనా, ఎన్నో దారుల్లో మార… | — | N033 |  |
| F124 | rock-cycle | శిల Weathering చెంది, Humus, నీరు, గాలి కలిస్తే Soil (నేల) ఏర్పడుతుంది. | — | N034 |  |
| F125 | chondrite | Chondrite అనేది ఒక రకం Stony meteorite; తొలి Solar System పదార్థాన్ని అధ్యయనం చే… | P042-F014 | N035, N040 |  |
| F126 | earth-age | భూమి వయస్సు సుమారు 4.54 billion years (454 కోట్ల సంవత్సరాలు). | P029-F001 | N039, N040 |  |
| F127 | earth-age | Radiometric dating లో Parent–Daughter isotope నిష్పత్తి, తెలిసిన decay వేగం ఆధార… | P029-F002 | N037 |  |
| F128 | earth-age | Uranium-238 Half-life (అర్ధాయుష్షు) సుమారు 4.47 billion years. | P029-F003 | — |  |
| F129 | earth-age | Carbon-14 Half-life సుమారు 5,730 సంవత్సరాలు; సుమారు 50,000 సంవత్సరాల లోపు జీవ అవ… | — | N037 |  |
| F130 | earth-age | భూ సంఘటనల కాలాన్ని, శిలల వయస్సును అధ్యయనం చేసే శాస్త్రాన్ని Geochronology అంటారు… | P029-F004 | — |  |
| F131 | earth-age | Ma అంటే million years ago (మిలియన్ సంవత్సరాల క్రితం). | — | N038 |  |
| F132 | time-scale | భారతదేశ Gondwana శిలలు Late Carboniferous నుంచి Early Cretaceous వరకు ఏర్పడ్డాయి… | — | N041, N050 |  |
| F133 | time-scale | భూవైజ్ఞానిక కాల విభజన క్రమం: Eon → Era → Period → Epoch → Age. | P029-F005 | N042, N043 |  |
| F134 | time-scale | Hadean, Archean, Proterozoic అనే మూడు Eons ను కలిపి Precambrian అంటారు. | P029-F006 | — |  |
| F135 | time-scale | కంటికి కనిపించే Fossils పుష్కలంగా ఉన్నందున Phanerozoic ను "కనిపించే జీవం" Eon అం… | P029-F017 | N043 |  |
| F136 | time-scale | Phanerozoic లోని మూడు Eras: Paleozoic, Mesozoic, Cenozoic. | P029-M002 (partial) | N042 |  |
| F137 | time-scale | Mesozoic Periods క్రమం: Triassic → Jurassic → Cretaceous. | P030-F005 | — |  |
| F138 | time-scale | Cenozoic Era సుమారు 66 Ma నుంచి ఇప్పటి వరకు ఉంది. | P030-F010, P030-F026 | — |  |
| F139 | time-scale | Tertiary ఇప్పుడు అధికారిక Period కాదు; దాని కాలాన్ని Paleogene, Neogene చూపిస్తా… | P030-F011 | — |  |
| F140 | precambrian | Hadean Eon లో భూమి Accretion, చల్లబడడం, తొలి Crust, తొలి నీరు ఏర్పడడం జరిగాయి. | P029-F007 | — |  |
| F141 | precambrian | Archean Eon శిలల్లో ప్రాచీన సూక్ష్మజీవుల (Microbial life) ఆధారాలు ఉన్నాయి. | P029-F008 | — |  |
| F142 | precambrian | సూక్ష్మజీవుల పొరలు మట్టిని పట్టుకుని పేర్చిన దిబ్బలను Stromatolites అంటారు; అతి … | — | N044 |  |
| F143 | precambrian | Oxygen ను వదిలిన తొలి సూక్ష్మజీవులు Cyanobacteria (నీలి–ఆకుపచ్చ బాక్టీరియా). | — | N045, N047 |  |
| F144 | precambrian | Cambrian కు ముందు, Proterozoic చివరి Period Ediacaran (సుమారు 635–538.8 Ma). | — | N046 |  |
| F145 | precambrian | Proterozoic Eon లో Oxygen పెరుగుదల దశలు, Eukaryotes, Multicellular జీవుల పరిణామం… | P029-F009 | N047 |  |
| F146 | precambrian | సుమారు 2.4 Ga క్రితం వాతావరణంలో Oxygen పెరిగిన ఘటనను Great Oxidation Event అంటార… | — | N045 |  |
| F147 | paleozoic | Cambrian లో అనేక సముద్ర జంతు సమూహాలు విస్తరించాయి; జీవం అంతకు ముందే ఉంది. | P029-F011 | — |  |
| F148 | paleozoic | Trilobites అంతరించిపోయిన సముద్ర Arthropods (సంధిపాదులు). | P029-F012 | — |  |
| F149 | paleozoic | Ordovician కాలం సముద్ర జీవ వైవిధ్య విస్తరణకు ప్రసిద్ధి. | P029-F013 | — |  |
| F150 | paleozoic | Silurian లో నేల మొక్కలు, నీటి Vertebrates లో ముఖ్యమైన మార్పులు జరిగాయి. | P029-F014 | — |  |
| F151 | paleozoic | Vertebrates కు వెన్నెముక (Backbone) ఉంటుంది; Invertebrates కు ఉండదు. | P029-F015 | — |  |
| F152 | paleozoic | Devonian అనే పేరు ఇంగ్లండ్‌లోని Devon నుంచి వచ్చింది; దీని ముద్దుపేరు "Age of Fi… | P029-F016, P029-M004 | N031 |  |
| F153 | paleozoic | తొలి Tetrapods ఆధారాలు Late Devonian లో ఉన్నాయి; Amphibian సమూహాలు Carboniferous… | P030-F002 | — |  |
| F154 | paleozoic | భారతదేశ బొగ్గు ఎక్కువగా Lower Gondwana (Permian) శిలల్లో ఉంది; Upper Gondwana లో… | — | N026 |  |
| F155 | paleozoic | Amniotes తొలి ముఖ్య Fossil ఆధారాలు Carboniferous లో ఉన్నాయి. | P030-F003 | — |  |
| F156 | paleozoic | Permian చివర సుమారు 251.9 Ma క్రితం భూమి చరిత్రలో అతి పెద్ద Mass extinction జరిగ… | P030-F004 | N048 |  |
| F157 | paleozoic | Pangaea Paleozoic చివర్లో ఏర్పడి, Mesozoic లో విడిపోవడం మొదలైంది. | P029-F010 | — |  |
| F158 | meso-cenozoic | Triassic లో తొలి Dinosaurs, Mammaliaforms ఆధారాలు ఉన్నాయి. | P030-F006 | — |  |
| F159 | meso-cenozoic | Jurassic లో అనేక Dinosaur సమూహాలు విస్తరించాయి; తొలి పక్షుల ఆధారాలు ఉన్నాయి. | P030-F007 | — |  |
| F160 | meso-cenozoic | Flowering plants (పూల మొక్కలు) స్పష్టమైన తొలి Fossils, విస్తరణ Cretaceous లో జరి… | P030-F009 | — |  |
| F161 | meso-cenozoic | Cretaceous చివర Mass extinction సుమారు 66 Ma క్రితం జరిగింది. | P030-F008 | — |  |
| F162 | meso-cenozoic | Paleocene లో అప్పటికే ఉన్న క్షీరద సమూహాలు ఇంకా విస్తరించాయి. | P030-F012 | — |  |
| F163 | meso-cenozoic | Eocene లో తొలి గుర్రాల వంశం, తొలి తిమింగలాల బంధువుల ఆధారాలు ఉన్నాయి. | P030-F013 | — |  |
| F164 | meso-cenozoic | Oligocene, Miocene కాలాల్లో Primate వంశాలు వేర్వేరు దశల్లో విస్తరించాయి. | P030-F014 | — |  |
| F165 | meso-cenozoic | Pliocene తొలి Hominin వంశాలకు ముఖ్యమైన కాలం. | P030-F015 | — |  |
| F166 | meso-cenozoic | Homo sapiens అతి పాత ఆధారాలు ఆఫ్రికాలో (Jebel Irhoud, Morocco) సుమారు 3,00,000 స… | P030-F016 | N051 |  |
| F167 | meso-cenozoic | Pleistocene లో చల్లని Glacial దశలు, వెచ్చని Interglacial దశలు మళ్లీ మళ్లీ మారాయి… | P030-F017 | N051 |  |
| F168 | meso-cenozoic | Holocene సుమారు 11,700 సంవత్సరాల క్రితం మొదలైంది. | P030-F018 | — |  |
| F169 | meso-cenozoic | Pangaea ఉత్తర భాగాన్ని Laurasia అని, దక్షిణ భాగాన్ని Gondwana అని అంటారు. | — | N049, N050 |  |
| F170 | meso-cenozoic | భారతదేశం Gondwana నుంచి అనేక దశల్లో విడిపోయి ఉత్తరం వైపు కదిలింది. | — | N049 |  |
| F171 | ap-link | Dharwar Craton దక్షిణ భారతదేశపు అతి పాత, స్థిరమైన భూభాగం; Dharwar System అందులోన… | — | N031, N053 |  |
| F172 | ap-link | AP లో Dharwar Schist belts Nellore, Prakasam, Anantapur, Kurnool, Kadapa, Chitto… | — | N054 |  |
| F173 | ap-link | Eastern Ghats (తూర్పు కనుమలు) లో Khondalite, Charnockite శిలలు ఉంటాయి. | — | N052, N054 |  |
| F174 | ap-link | భారీ వర్షం, వేడి Khondalite నుంచి Silica ను కడిగేయగా మిగిలిన Aluminium వల్ల ఉత్త… | — | N052 |  |
| F175 | ap-link | Wajrakarur Kimberlite Field ఆంధ్రప్రదేశ్‌లోని Anantapur జిల్లాలో ఉంది. | P040-F007 | N053 |  |
| F176 | ap-link | Cuddapah Basin లో Proterozoic కాలపు Sedimentary శిలలు (Cuddapah Supergroup) ఉన్న… | — | N053 |  |
| F177 | ap-link | Krishna–Godavari (KG) Basin Sedimentary పొరల్లో చమురు, సహజ వాయువు దొరుకుతాయి. | — | N053, N054 |  |
| F178 | ap-link | Andhra Pradesh ఎక్కువగా Seismic Zone II, III లో ఉంది. | — | N055 |  |
