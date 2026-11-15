import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "content" / "geography" / "india_ap_chapters" / "5"
BANK = CHAPTER / "Questions.json"

COMBOS_EN = ["1 and 2 only", "2 and 3 only", "1, 2 and 3 only", "1, 2, 3 and 4"]
COMBOS_TE = ["1, 2 మాత్రమే", "2, 3 మాత్రమే", "1, 2, 3 మాత్రమే", "1, 2, 3, 4 అన్నీ"]

CUSTOM_COMBOS = {
    "IA05-BOOK-P293-001": (
        ["1 and 2 only", "2 and 3 only", "1, 3 and 4 only", "1, 2, 3 and 4"],
        ["1, 2 మాత్రమే", "2, 3 మాత్రమే", "1, 3, 4 మాత్రమే", "1, 2, 3, 4 అన్నీ"],
    ),
    "IA05-BOOK-P297-001": (
        ["1 and 2 only", "2 and 3 only", "1, 2 and 4 only", "1, 2, 3 and 4"],
        ["1, 2 మాత్రమే", "2, 3 మాత్రమే", "1, 2, 4 మాత్రమే", "1, 2, 3, 4 అన్నీ"],
    ),
    "IA05-BOOK-P299-001": (
        ["1 and 2 only", "2 and 3 only", "1, 2 and 4 only", "1, 2, 3 and 4"],
        ["1, 2 మాత్రమే", "2, 3 మాత్రమే", "1, 2, 4 మాత్రమే", "1, 2, 3, 4 అన్నీ"],
    ),
    "IA05-BOOK-P303-001": (
        ["1 and 2 only", "2 and 3 only", "1, 3 and 4 only", "1, 2, 3 and 4"],
        ["1, 2 మాత్రమే", "2, 3 మాత్రమే", "1, 3, 4 మాత్రమే", "1, 2, 3, 4 అన్నీ"],
    ),
}

# Every sentence below was written after the corresponding printed page and the
# integrated note section were manually reviewed. The helper only serialises the
# hand-authored records; it does not compose question prose.
ROWS = [
    {
        "id": "IA05-BOOK-P289-001", "page": 289, "section": "soil-definition",
        "facts": ["IA05-P289-F01", "IA05-P289-F02", "IA05-P289-F03", "IA05-P289-F04", "IA05-P289-F05", "IA05-P289-F06", "IA05-P289-F07", "IA05-P289-F08", "IA05-P289-F09", "IA05-P289-F10"],
        "question_en": "Consider the following about soil. 1. Pedogenesis is controlled by parent material, climate, organisms, relief and time. 2. The 45% mineral–25% water–25% air–5% organic model is an idealised composition, not a fixed law. 3. Texture means the sand–silt–clay proportion, whereas structure means their arrangement into aggregates. 4. Soil water and soil air occupy pore space and support transport and respiration. Which statements are correct?",
        "question_te": "నేల (Soil) గురించి కింది వాక్యాలను పరిశీలించండి. 1. మాతృ పదార్థం (Parent material), వాతావరణం (Climate), జీవులు (Organisms), భూస్వరూపం (Relief), కాలం (Time) నేల ఏర్పాటును (Pedogenesis) ప్రభావితం చేస్తాయి. 2. 45% ఖనిజ పదార్థం–25% నీరు–25% గాలి–5% సేంద్రియ పదార్థం అనే నిష్పత్తి ఆదర్శ నమూనా మాత్రమే; స్థిర నియమం కాదు. 3. ఇసుక–సిల్ట్–బంకమట్టి నిష్పత్తి నేల కణనిర్మాణం (Texture); అవి గుంపులుగా అమరే తీరు నేల నిర్మాణం (Structure). 4. రంధ్రాలలోని నీరు, గాలి ద్రావణాల రవాణా మరియు శ్వాసక్రియకు తోడ్పడతాయి. సరైనవి ఏవి?",
        "answer": 4,
        "explanation_en": "All four are correct. Formation rate and composition vary by site. Clay is generally below 0.002 mm and sand about 0.05–2 mm in the cited system; humus improves aggregation and nutrient and water relations.",
        "explanation_te": "నాలుగు వాక్యాలూ సరైనవే. నేల ఏర్పడే వేగం, పదార్థాల నిష్పత్తి ప్రాంతానుసారం మారతాయి. ఈ పాఠంలో బంకమట్టి (Clay) 0.002 mm కంటే చిన్నది; ఇసుక (Sand) సుమారు 0.05–2 mm. హ్యూమస్ (Humus) గుంపుల నిర్మాణం, పోషక నిల్వ, నీటి సంబంధాలను మెరుగుపరుస్తుంది.",
    },
    {
        "id": "IA05-BOOK-P290-001", "page": 290, "section": "soil-profile-horizons",
        "facts": ["IA05-P290-F01", "IA05-P290-F02", "IA05-P290-F03", "IA05-P290-F04", "IA05-P290-F05", "IA05-P290-F06", "IA05-P290-F07", "IA05-P290-F08", "IA05-P290-F09", "IA05-P290-F10"],
        "question_en": "Consider the following. 1. Neutral soil reaction is pH 7; crop optima are not universal. 2. Colour reflects organic matter, minerals, drainage and oxidation–reduction, so black colour alone does not prove fertility. 3. O–A–E–B–C–R denotes organic layer, topsoil, eluviation, illuviation, altered parent material and bedrock. 4. Residual soil forms over its parent material; transported soil is moved before deposition. Which statements are correct?",
        "question_te": "కింది వాక్యాలను పరిశీలించండి. 1. తటస్థ నేల ప్రతిచర్య (Neutral soil reaction) pH 7; అన్ని పంటలకు ఒకే అనుకూల pH ఉండదు. 2. సేంద్రియ పదార్థం, ఖనిజాలు, నీటి పారుదల, ఆక్సీకరణ–క్షయీకరణ (Oxidation–reduction) నేల రంగును ప్రభావితం చేస్తాయి; నలుపు రంగు ఒక్కటే సారానికి రుజువు కాదు. 3. O–A–E–B–C–R వరుస సేంద్రియ పొర, పైమట్టి, క్షాళనం, నిక్షేపణ, మారిన మాతృ పదార్థం, మూలశిలను సూచిస్తుంది. 4. అవశిష్ట నేల (Residual soil) అదే మాతృ పదార్థంపై ఏర్పడుతుంది; రవాణా నేల (Transported soil) నిక్షేపణకు ముందు తరలించబడుతుంది. సరైనవి ఏవి?",
        "answer": 4,
        "explanation_en": "All four are correct. Soil temperature and depth also vary with climate, season, cover, moisture and landscape; printed single thresholds should not be universalised.",
        "explanation_te": "నాలుగు వాక్యాలూ సరైనవే. నేల ఉష్ణోగ్రత (Soil temperature), లోతు (Depth) వాతావరణం, ఋతువు, ఆవరణం, తేమ, భూస్వరూపాన్ని బట్టి మారతాయి; పుస్తకంలోని ఒక్క సంఖ్యను సార్వత్రిక పరిమితిగా తీసుకోరాదు.",
    },
    {
        "id": "IA05-BOOK-P291-001", "page": 291, "section": "alluvial-subtypes",
        "facts": ["IA05-P291-F01", "IA05-P291-F02", "IA05-P291-F03", "IA05-P291-F04", "IA05-P291-F05", "IA05-P291-F06", "IA05-P291-F07", "IA05-P291-F08", "IA05-P291-F09"],
        "question_en": "Consider the following. 1. Zonal–interzonal–azonal is a historical classification, not current Soil Taxonomy. 2. ICAR history associates the classical alluvial–black–red–lateritic grouping with J. W. Leather; the book's Voelcker attribution needs qualification. 3. Khadar is newer floodplain alluvium, Bhangar older terrace alluvium, Bhabar a coarse piedmont belt and Tarai the wetter belt downslope. 4. All alluvial soil has identical texture and fertility. Which statements are correct?",
        "question_te": "కింది వాక్యాలను పరిశీలించండి. 1. మండల–అంతర్మండల–అమండల (Zonal–interzonal–azonal) వర్గీకరణ చారిత్రక పద్ధతి; ప్రస్తుత నేల వర్గీకరణ (Soil Taxonomy) కాదు. 2. ఒండ్రు–నల్ల–ఎర్ర–లేటరైట్ అనే సంప్రదాయ విభజనను ICAR చరిత్ర J. W. Leatherతో అనుసంధానిస్తుంది; పుస్తకంలోని Voelcker ఆపాదనకు స్పష్టీకరణ అవసరం. 3. ఖాదర్ (Khadar) కొత్త వరదమైదాన ఒండ్రు; భాంగర్ (Bhangar) పాత ఎత్తైన ఒండ్రు; భాబర్ (Bhabar) ముతక పాదపర్వత మండలం; తరాయి (Tarai) దాని దిగువ తడి మండలం. 4. అన్ని ఒండ్రు నేలల కణనిర్మాణం, సారం ఒకేలా ఉంటాయి. సరైనవి ఏవి?",
        "answer": 3,
        "explanation_en": "Statements 1–3 are correct; statement 4 is false. Alluvium ranges from sand to clay and nutrient status varies. The printed eight-group scheme remains useful as a broad Indian-geography classification.",
        "explanation_te": "1–3 సరైనవి; 4 తప్పు. ఒండ్రు నేల (Alluvial soil) ఇసుక నుంచి బంకమట్టి వరకు మారుతుంది; పోషక స్థితి కూడా ఒకేలా ఉండదు. పుస్తకంలోని ఎనిమిది ప్రధాన నేల సమూహాలు స్థూల భారత భూగోళ వర్గీకరణగా ఉపయోగకరమైనవి.",
    },
    {
        "id": "IA05-BOOK-P292-001", "page": 292, "section": "black-properties",
        "facts": ["IA05-P292-F01", "IA05-P292-F02", "IA05-P292-F03", "IA05-P292-F04", "IA05-P292-F05", "IA05-P292-F06", "IA05-P292-F07", "IA05-P292-F08", "IA05-P292-F09"],
        "question_en": "Consider the following. 1. Oxidised iron commonly gives red soils their colour, while hydration may produce yellow shades. 2. Regur is strongly associated with Deccan basalt, but every black soil need not have the same parent material. 3. Smectitic clay causes shrink–swell, deep dry-season cracks and self-mulching in many Vertisols. 4. Strong water retention means all retained water is freely available and drainage is always rapid. Which statements are correct?",
        "question_te": "కింది వాక్యాలను పరిశీలించండి. 1. ఆక్సీకృత ఇనుము (Oxidised iron) ఎర్ర రంగును; జలయుక్త స్థితి (Hydration) పసుపు ఛాయను కలిగించవచ్చు. 2. రేగర్ (Regur) నేలకు దక్కన్ బసాల్ట్‌తో బలమైన సంబంధం ఉన్నా ప్రతి నల్ల నేలకు ఒకే మాతృ పదార్థం ఉండదు. 3. స్మెక్టైట్ బంకమట్టి (Smectitic clay) అనేక వర్టిసాల్స్‌లో (Vertisols) ఉబ్బడం–కుంచించుకోవడం, వేసవి పగుళ్లు, స్వీయ దున్నుకును కలిగిస్తుంది. 4. అధిక నీటి నిల్వ వల్ల నిలిచిన నీరంతా మొక్కలకు సులభంగా లభించి, పారుదల ఎప్పుడూ వేగంగా ఉంటుంది. సరైనవి ఏవి?",
        "answer": 3,
        "explanation_en": "Statements 1–3 are correct. Statement 4 is false: clay can hold water strongly while infiltration, drainage and plant availability remain constrained. Printed national percentages are historical approximations.",
        "explanation_te": "1–3 సరైనవి. 4 తప్పు: బంకమట్టి నీటిని బలంగా పట్టుకున్నా చొరబాటు (Infiltration), పారుదల (Drainage), మొక్కలకు లభ్యత పరిమితం కావచ్చు. పుస్తకంలోని జాతీయ శాతాలు చారిత్రక అంచనాలు.",
    },
    {
        "id": "IA05-BOOK-P293-001", "page": 293, "section": "laterite-formation",
        "facts": ["IA05-P293-F01", "IA05-P293-F02", "IA05-P293-F03", "IA05-P293-F04", "IA05-P293-F05", "IA05-P293-F06", "IA05-P293-F07", "IA05-P293-F08"],
        "question_en": "Consider the following. 1. Laterisation removes silica and bases through intense weathering and leaching, relatively enriching iron and aluminium oxides. 2. Rainfall and temperature alone fully determine laterite; drainage, parent material and landscape position do not matter. 3. Forest and mountain soils vary with altitude, slope, vegetation, parent material and climate. 4. Podzolisation may occur in cool humid coniferous settings but is not universal in every Indian forest. Which statements are correct?",
        "question_te": "కింది వాక్యాలను పరిశీలించండి. 1. తీవ్రమైన శైథిల్యం, క్షాళనం (Leaching) వల్ల సిలికా, క్షారాలు తొలగి ఇనుము–అల్యూమినియం ఆక్సైడ్లు సాపేక్షంగా పెరగడం లేటరైటీకరణ (Laterisation). 2. వర్షపాతం, ఉష్ణోగ్రత మాత్రమే లేటరైట్‌ను పూర్తిగా నిర్ణయిస్తాయి; పారుదల, మాతృ పదార్థం, భూస్వరూప స్థానానికి పాత్ర లేదు. 3. అటవీ–పర్వత నేలలు ఎత్తు, వాలు, వృక్షజాలం, మాతృ పదార్థం, వాతావరణాన్ని బట్టి మారతాయి. 4. చల్లని తేమగల శంకుధారి ప్రాంతాల్లో పోడ్జలీకరణ (Podzolisation) జరగవచ్చు; భారత అటవులన్నిటికీ ఇది వర్తించదు. సరైనవి ఏవి?",
        "answer": 3,
        "explanation_en": "Statements 1, 3 and 4 are correct; statement 2 is false. Laterite distribution and productivity depend on several controls, and management can support plantation crops. The printed TGPSC item remains held and unscored pending an official key.",
        "explanation_te": "1, 3, 4 సరైనవి; 2 తప్పు. లేటరైట్ ఏర్పాటుకు అనేక నియంత్రకాలు ఉంటాయి; సరైన నిర్వహణతో తోట పంటలు సాధ్యమవుతాయి. పుస్తకంలోని TGPSC ప్రశ్న అధికారిక తుది సమాధాన కీ దొరికే వరకు స్కోరింగ్‌లో ఉండదు.",
    },
    {
        "id": "IA05-BOOK-P294-001", "page": 294, "section": "saline-sodic-reclamation",
        "facts": ["IA05-P294-F01", "IA05-P294-F02", "IA05-P294-F03", "IA05-P294-F04", "IA05-P294-F05", "IA05-P294-F06", "IA05-P294-F07", "IA05-P294-F08"],
        "question_en": "Consider the following. 1. Arid soils are often sandy to loamy, low in organic matter and may accumulate carbonates or salts. 2. Irrigation without adequate drainage can cause waterlogging and salinity. 3. Saline soil has excess soluble salts, whereas sodic soil has excessive exchangeable sodium; leaching–drainage and gypsum respectively address these different problems. 4. Peaty soils form under prolonged wetness and oxygen limitation and may be acidic. Which statements are correct?",
        "question_te": "కింది వాక్యాలను పరిశీలించండి. 1. శుష్క నేలలు (Arid soils) సాధారణంగా ఇసుక నుంచి లోమ్ వరకు ఉండి, సేంద్రియ పదార్థం తక్కువగా, కార్బోనేట్లు లేదా లవణాలు పేరుకుపోయే అవకాశంతో ఉంటాయి. 2. సరైన పారుదల లేకుండా నీటిపారుదల చేస్తే నీరు నిలవడం, లవణీకరణ రావచ్చు. 3. లవణ నేలలో (Saline soil) కరిగే లవణాలు అధికం; సోడిక్ నేలలో (Sodic soil) మార్పిడి సోడియం అధికం. మొదటిదానికి క్షాళనం–పారుదల, రెండవదానికి సాధారణంగా జిప్సం అవసరం. 4. ఎక్కువకాలం తడి, ఆక్సిజన్ కొరతలో పీట్ నేలలు (Peaty soils) ఏర్పడి ఆమ్ల స్వభావం కలిగి ఉండవచ్చు. సరైనవి ఏవి?",
        "answer": 4,
        "explanation_en": "All four are correct. Colour alone is not diagnostic, and reclamation must follow soil and irrigation-water analysis. The book's occurrence list is retained as a broad distribution, not a farm-level map.",
        "explanation_te": "నాలుగు వాక్యాలూ సరైనవే. రంగు ఒక్కటే నిర్ధారణ లక్షణం కాదు. పునరుద్ధరణ (Reclamation) ముందు నేల, సాగునీటి పరీక్ష అవసరం. పుస్తకంలోని వ్యాప్తి జాబితా స్థూల వివరణ మాత్రమే.",
    },
    {
        "id": "IA05-BOOK-P295-001", "page": 295, "section": "india-major-soil-map",
        "facts": ["IA05-P295-F01", "IA05-P295-F02", "IA05-P295-F03", "IA05-P295-F04", "IA05-P295-F05"],
        "question_en": "Consider the printed India soil map. 1. It broadly shows alluvial belts in northern plains and east-coast deltas. 2. Red–yellow soils cover much of the peninsular interior and black soils major Deccan tracts. 3. Arid soils dominate western Rajasthan, while lateritic belts occur in humid uplands and parts of the Ghats. 4. Its scale is sufficient to assign a single soil type to every village and farm. Which statements are correct?",
        "question_te": "ముద్రిత భారత నేలల పటాన్ని పరిశీలించండి. 1. ఉత్తర మైదానాలు, తూర్పు తీర డెల్టాల్లో ఒండ్రు నేల మండలాలను స్థూలంగా చూపుతుంది. 2. ద్వీపకల్ప అంతర్భాగంలో ఎర్ర–పసుపు నేలలు, ప్రధాన దక్కన్ ప్రాంతాల్లో నల్ల నేలలు చూపబడ్డాయి. 3. పశ్చిమ రాజస్థాన్‌లో శుష్క నేలలు; తేమగల ఎత్తుభాగాలు, కనుమల్లో లేటరైట్ మండలాలు కనిపిస్తాయి. 4. ప్రతి గ్రామం లేదా పొలానికి ఒకే నేల రకాన్ని నిర్ణయించడానికి ఈ పటపు ప్రమాణం సరిపోతుంది. సరైనవి ఏవి?",
        "answer": 3,
        "explanation_en": "Statements 1–3 are correct; statement 4 is false. A small-scale national map omits local inclusions and transitions; detailed soil survey is required for field decisions.",
        "explanation_te": "1–3 సరైనవి; 4 తప్పు. చిన్న ప్రమాణ పటం (Small-scale map) స్థానిక నేల మిశ్రమాలు, మార్పు మండలాలను చూపదు; పొలస్థాయి నిర్ణయానికి సవివర నేల సర్వే అవసరం.",
    },
    {
        "id": "IA05-BOOK-P296-001", "page": 296, "section": "erosion-process",
        "facts": ["IA05-P296-F01", "IA05-P296-F02", "IA05-P296-F03", "IA05-P296-F04", "IA05-P296-F05", "IA05-P296-F06", "IA05-P296-F07", "IA05-P296-F08"],
        "question_en": "Consider the following. 1. Sheet erosion removes a thin layer, rills are small tillage-removable channels and gullies are larger persistent channels. 2. Ravines are advanced networks of gullies; Chambal is a classic example. 3. Wind transports soil by suspension, saltation and surface creep, while splash begins with raindrop impact. 4. Glacial and wave erosion are geomorphic processes and should not be confused with agricultural topsoil loss. Which statements are correct?",
        "question_te": "కింది వాక్యాలను పరిశీలించండి. 1. పలుచని పొర కోత (Sheet erosion) పలుచని పొరను తొలగిస్తుంది; చిన్న గాడుల కోత (Rill erosion) సాధారణ దున్నుతో చెరిగే గాడులు; పెద్ద గాడుల కోత (Gully erosion) నిలకడైన పెద్ద గాడులు. 2. రవీన్లు (Ravines) అభివృద్ధి చెందిన గల్లీల వలయం; చంబల్ ప్రసిద్ధ ఉదాహరణ. 3. గాలి నేలను నిలంబనం (Suspension), దూకుడు (Saltation), ఉపరితల పాకుడు (Surface creep) ద్వారా తరలిస్తుంది; వర్షబిందువు ఢీకొట్టడంతో చిమ్ముడు కోత (Splash erosion) మొదలవుతుంది. 4. హిమానీనద, అలల కోత భూస్వరూప ప్రక్రియలు; వాటిని వ్యవసాయ పైమట్టి నష్టంతో కలపకూడదు. సరైనవి ఏవి?",
        "answer": 4,
        "explanation_en": "All four are correct. Bank erosion involves channel flow and mass failure. National erosion-area and soil-loss numbers depend on date and method and must be cited as estimates.",
        "explanation_te": "నాలుగు వాక్యాలూ సరైనవే. గట్టు కోత (Bank erosion) ప్రవాహం, సామూహిక జారుడు వల్ల జరుగుతుంది. జాతీయ కోత విస్తీర్ణం, మట్టి నష్టం సంఖ్యలు సంవత్సరం, పద్ధతిపై ఆధారపడే అంచనాలు.",
    },
    {
        "id": "IA05-BOOK-P297-001", "page": 297, "section": "conservation-practices",
        "facts": ["IA05-P297-F01", "IA05-P297-F02", "IA05-P297-F03", "IA05-P297-F04", "IA05-P297-F05", "IA05-P297-F06", "IA05-P297-F07", "IA05-P297-F08", "IA05-P297-F09"],
        "question_en": "Consider the following. 1. Deforestation, overgrazing, unsuitable cultivation, mining and poorly drained irrigation can accelerate degradation. 2. Contour operations cross the slope; terraces shorten effective slope length but need outlets and maintenance. 3. Water harvesting always guarantees groundwater recharge, irrespective of geology and design. 4. Land use should match slope, soil and erosion hazard; vegetation and stocking must suit local ecology. Which statements are correct?",
        "question_te": "కింది వాక్యాలను పరిశీలించండి. 1. అడవుల తొలగింపు, అధిక మేత, అనుచిత సాగు, గనులు, పారుదల లేని నీటిపారుదల నేల క్షీణతను వేగవంతం చేస్తాయి. 2. సమోన్నత చర్యలు (Contour operations) వాలకు అడ్డంగా ఉంటాయి; మెట్ల సాగు (Terracing) ప్రభావవంతమైన వాలు పొడవును తగ్గించినా నీటి వెలికితీత, నిర్వహణ అవసరం. 3. భూగర్భ నిర్మాణం, రూపకల్పన ఎలా ఉన్నా నీటి సేకరణ (Water harvesting) భూగర్భజల పునర్భరణకు హామీ ఇస్తుంది. 4. భూవినియోగం వాలు, నేల, కోత ప్రమాదానికి సరిపోవాలి; మొక్కజాతులు, మేత తీవ్రత స్థానిక పర్యావరణానికి అనుకూలంగా ఉండాలి. సరైనవి ఏవి?",
        "answer": 3,
        "explanation_en": "Statements 1, 2 and 4 are correct; statement 3 is false. Strip cropping, stubble mulch, contour bunds, basin listing, agroforestry and controlled grazing work through different mechanisms and need site-specific design.",
        "explanation_te": "1, 2, 4 సరైనవి; 3 తప్పు. పట్టీల సాగు (Strip cropping), పంట అవశేష కప్పు (Stubble mulch), సమోన్నత గట్లు (Contour bunds), చిన్న గుంతల ఏర్పాటు (Basin listing), వ్యవసాయ–అటవీ విధానం (Agroforestry), నియంత్రిత మేత వేర్వేరు విధానాల్లో పనిచేస్తాయి; ప్రాంతానుసార రూపకల్పన అవసరం.",
    },
    {
        "id": "IA05-BOOK-P298-001", "page": 298, "section": "conservation-diagram",
        "facts": ["IA05-P298-F01", "IA05-P298-F02", "IA05-P298-F03", "IA05-P298-F04", "IA05-P298-F05", "IA05-P298-F06"],
        "question_en": "Consider the conservation diagram. 1. Contour tillage follows equal-elevation lines, while contour bunds are physical embankments. 2. Terraces reshape a slope into steps; basin listing creates smaller storage basins without fully terracing it. 3. Barriers require safe overflow even when they slow runoff and promote infiltration. 4. A capability approach generally reserves very steep erosion-prone land for forestry or protection rather than repeated cultivation. Which statements are correct?",
        "question_te": "నేల సంరక్షణ చిత్రాన్ని పరిశీలించండి. 1. సమోన్నత దున్నకం (Contour tillage) సమాన ఎత్తు రేఖలను అనుసరిస్తుంది; సమోన్నత గట్లు (Contour bunds) భౌతిక కట్టలు. 2. మెట్లు (Terraces) వాలను మెట్లుగా మారుస్తాయి; చిన్న నిల్వ గుంతలు (Basin listing) మొత్తం వాలను మెట్లుగా మార్చవు. 3. అడ్డంకులు ప్రవాహాన్ని తగ్గించి చొరబాటును పెంచినా సురక్షిత అదనపు నీటి వెలికితీత అవసరం. 4. భూసామర్థ్య విధానం (Land-capability approach) చాలా నిటారైన, కోతకు గురయ్యే భూమిని పునరావృత సాగుకంటే అటవీ లేదా రక్షణకు కేటాయిస్తుంది. సరైనవి ఏవి?",
        "answer": 4,
        "explanation_en": "All four are correct. The eight printed panels compare strip cropping, stubble mulch, contour tillage, bunding, terracing, basin listing, water harvesting and slope-based land use.",
        "explanation_te": "నాలుగు వాక్యాలూ సరైనవే. ముద్రిత ఎనిమిది చిత్రాలు పట్టీల సాగు, అవశేష కప్పు, సమోన్నత దున్నకం, గట్లు, మెట్లు, చిన్న గుంతలు, నీటి సేకరణ, వాలు ఆధారిత భూవినియోగాన్ని పోల్చుతాయి.",
    },
    {
        "id": "IA05-BOOK-P299-001", "page": 299, "section": "soil-taxonomy",
        "facts": ["IA05-P299-F01", "IA05-P299-F02", "IA05-P299-F03", "IA05-P299-F04", "IA05-P299-F05", "IA05-P299-F06"],
        "question_en": "Consider the following. 1. Current USDA Soil Taxonomy recognises 12 orders, not the book's incomplete nine-order list. 2. Inceptisols show weak to moderate development, Vertisols have shrink–swell clay and Oxisols are intensely weathered. 3. Printed research-centre and state-area tables may be memorised as timeless current facts without checking institution, year or denominator. 4. The printed 97.85 million ha and 29.77% degradation figures must retain their monitoring period and atlas context. Which statements are correct?",
        "question_te": "కింది వాక్యాలను పరిశీలించండి. 1. ప్రస్తుత USDA నేల వర్గీకరణ (Soil Taxonomy)లో 12 నేల క్రమాలు (Soil orders) ఉన్నాయి; పుస్తకంలోని తొమ్మిది క్రమాల జాబితా అసంపూర్ణం. 2. ఇన్సెప్టిసాల్స్ (Inceptisols)లో తక్కువ–మధ్యస్థ అభివృద్ధి; వర్టిసాల్స్ (Vertisols)లో ఉబ్బే–కుంచే బంకమట్టి; ఆక్సిసాల్స్ (Oxisols)లో తీవ్రమైన శైథిల్యం కనిపిస్తుంది. 3. పరిశోధన కేంద్రాలు, రాష్ట్ర విస్తీర్ణ పట్టికను సంస్థ, సంవత్సరం, ప్రమాణం చూడకుండా ప్రస్తుత శాశ్వత నిజాలుగా గుర్తుంచుకోవచ్చు. 4. 97.85 మిలియన్ ha, 29.77% క్షీణత సంఖ్యలను సంబంధిత పర్యవేక్షణ కాలం, అట్లాస్ సందర్భంతోనే చెప్పాలి. సరైనవి ఏవి?",
        "answer": 3,
        "explanation_en": "Statements 1, 2 and 4 are correct; statement 3 is false. Institutional mandates and statistical denominators change, whereas diagnostic properties define soil orders.",
        "explanation_te": "1, 2, 4 సరైనవి; 3 తప్పు. సంస్థల బాధ్యతలు, గణాంక ప్రమాణాలు మారవచ్చు; నేల క్రమాలను నిర్ధారణ లక్షణాలు (Diagnostic properties) నిర్వచిస్తాయి.",
    },
    {
        "id": "IA05-BOOK-P300-001", "page": 300, "section": "soil-orders-table",
        "facts": ["IA05-P300-F01", "IA05-P300-F02", "IA05-P300-F03", "IA05-P300-F04", "IA05-P300-F05"],
        "question_en": "Consider the following. 1. The three orders omitted by the printed nine-order list are Andisols, Entisols and Gelisols. 2. Alfisols have a clay-enriched subsurface and higher base status than strongly leached Ultisols. 3. Aridisols, Spodosols, Histosols and Mollisols are distinguished by diagnostic arid, spodic, organic and dark base-rich properties respectively. 4. The printed erosion map is schematic and cannot provide a parcel-level hazard assessment. Which statements are correct?",
        "question_te": "కింది వాక్యాలను పరిశీలించండి. 1. పుస్తకంలోని తొమ్మిది క్రమాల జాబితాలో లేని మూడు క్రమాలు ఆండిసాల్స్ (Andisols), ఎంటిసాల్స్ (Entisols), జెలిసాల్స్ (Gelisols). 2. ఆల్ఫిసాల్స్ (Alfisols)లో బంకమట్టి కూడిన ఉపపొర, ఎక్కువ క్షార సంతృప్తి ఉంటాయి; అల్టిసాల్స్ (Ultisols) మరింత క్షాళితమై క్షారాలు తగ్గుతాయి. 3. ఆరిడిసాల్స్, స్పోడోసాల్స్, హిస్టోసాల్స్, మోలిసాల్స్‌ను వరుసగా శుష్క, స్పోడిక్, సేంద్రియ, ముదురు క్షారసమృద్ధి నిర్ధారణ లక్షణాలు వేరు చేస్తాయి. 4. ముద్రిత కోత పటం స్థూల పటం; పొలస్థాయి ప్రమాదాన్ని నిర్ణయించదు. సరైనవి ఏవి?",
        "answer": 4,
        "explanation_en": "All four are correct. The map is useful for regional pattern learning but uses broad categories and older boundaries; detailed assessment is needed locally.",
        "explanation_te": "నాలుగు వాక్యాలూ సరైనవే. పటం ప్రాంతీయ నమూనాల అధ్యయనానికి ఉపయోగపడినా స్థూల వర్గాలు, పాత సరిహద్దులు కలిగి ఉంటుంది; స్థానికంగా సవివర అంచనా అవసరం.",
    },
    {
        "id": "IA05-BOOK-P301-001", "page": 301, "section": "ap-soil-share-table",
        "facts": ["IA05-P301-F01", "IA05-P301-F02", "IA05-P301-F03", "IA05-P301-F04", "IA05-P301-F05", "IA05-P301-F06"],
        "question_en": "Consider the Andhra Pradesh soil profile printed on page 301. 1. It gives the legacy shares red 65%, black 25%, alluvial 5%, coastal sand 3%, laterite 1% and problem soils 1%. 2. The figures must be labelled as a dated legacy profile rather than a current district-wise census. 3. Red soils are widespread in Rayalaseema and uplands, commonly derived from crystalline rocks and variable in texture, depth and nutrients. 4. Groundnut, millets, pulses and oilseeds succeed irrespective of rainfall, irrigation, depth, pH and nutrients. Which statements are correct?",
        "question_te": "301వ పుటలోని ఆంధ్రప్రదేశ్ నేల వివరాలను పరిశీలించండి. 1. పాత అంచనాలో ఎర్ర 65%, నల్ల 25%, ఒండ్రు 5%, తీర ఇసుక 3%, లేటరైట్ 1%, సమస్యాత్మక నేలలు 1%గా ఉన్నాయి. 2. ఇవి ప్రస్తుత జిల్లాల వారీ గణనగా కాక తేదీగల పాత రూపరేఖగా చెప్పాలి. 3. రాయలసీమ, ఎత్తుభాగాల్లో ఎర్ర నేలలు విస్తరించి, సాధారణంగా స్ఫటిక శిలల నుంచి ఏర్పడి కణనిర్మాణం, లోతు, పోషకాల్లో మారుతాయి. 4. వర్షపాతం, నీటిపారుదల, లోతు, pH, పోషకాలు ఎలా ఉన్నా వేరుశనగ, చిరుధాన్యాలు, పప్పులు, నూనెగింజలు తప్పక విజయవంతమవుతాయి. సరైనవి ఏవి?",
        "answer": 3,
        "explanation_en": "Statements 1–3 are correct; statement 4 is false. Crop suitability depends on site conditions. Chalka and Dubba are retained as local red-soil names and should be explained by texture and depth.",
        "explanation_te": "1–3 సరైనవి; 4 తప్పు. పంట అనుకూలత ప్రాంత పరిస్థితులపై ఆధారపడుతుంది. చల్కా (Chalka), దుబ్బ (Dubba) స్థానిక ఎర్ర నేల పేర్లు; వాటిని కణనిర్మాణం, లోతుతో వివరించాలి.",
    },
    {
        "id": "IA05-BOOK-P302-001", "page": 302, "section": "ap-black-soils",
        "facts": ["IA05-P302-F01", "IA05-P302-F02", "IA05-P302-F03", "IA05-P302-F04", "IA05-P302-F05", "IA05-P302-F06", "IA05-P302-F07"],
        "question_en": "Consider the following about Andhra Pradesh soils. 1. Chalka is generally coarser and Dubba finer, but local usage varies. 2. The printed black-soil share and 65–80% clay range are legacy generalisations; shrink–swell, moisture retention and workability constraints are more useful process clues. 3. Alluvial soils occur in Godavari, Krishna and Pennar floodplains and deltas and range from sand to clay. 4. Coastal sands are coarse and permeable, so salinity, nutrients and water retention never constrain them. Which statements are correct?",
        "question_te": "ఆంధ్రప్రదేశ్ నేలల గురించి కింది వాక్యాలను పరిశీలించండి. 1. చల్కా (Chalka) సాధారణంగా ముతకగా, దుబ్బ (Dubba) మెత్తగా ఉంటుంది; స్థానిక వాడుక మారవచ్చు. 2. నల్ల నేల 25%, బంకమట్టి 65–80% అనే సంఖ్యలు పాత సాధారణీకరణలు; ఉబ్బడం–కుంచడం, తేమ నిల్వ, దున్నే ఇబ్బందులు ముఖ్య ప్రక్రియ లక్షణాలు. 3. గోదావరి, కృష్ణా, పెన్నా వరదమైదానాలు, డెల్టాల్లో ఒండ్రు నేలలు ఇసుక నుంచి బంకమట్టి వరకు ఉంటాయి. 4. తీర ఇసుక నేలలు ముతకగా, పారగమ్యంగా ఉండటం వల్ల లవణత, పోషకాలు, నీటి నిల్వ ఎప్పుడూ సమస్య కావు. సరైనవి ఏవి?",
        "answer": 3,
        "explanation_en": "Statements 1–3 are correct; statement 4 is false. Coarse coastal soils often have low nutrient and water retention and may face salinity or groundwater-quality constraints.",
        "explanation_te": "1–3 సరైనవి; 4 తప్పు. ముతక తీర నేలల్లో పోషక, నీటి నిల్వ తక్కువగా ఉండవచ్చు; లవణత, భూగర్భజల నాణ్యత సమస్యలు కూడా రావచ్చు.",
    },
    {
        "id": "IA05-BOOK-P303-001", "page": 303, "section": "ap-percentage-conflicts",
        "facts": ["IA05-P303-F01", "IA05-P303-F02", "IA05-P303-F03", "IA05-P303-F04", "IA05-P303-F05", "IA05-P303-F06"],
        "question_en": "Consider the following. 1. Page 303's laterite 2% and coastal 1% conflict with page 301's laterite 1% and coastal sand 3%. 2. The conflict should be hidden and both sets used simultaneously for scoring. 3. The AP map uses older district boundaries and only broad red, black, alluvial and coastal/other categories. 4. Current APSAC district resource maps are preferable for local interpretation because districts contain soil inclusions and transitions. Which statements are correct?",
        "question_te": "కింది వాక్యాలను పరిశీలించండి. 1. 303వ పుటలో లేటరైట్ 2%, తీర నేల 1%గా ఉండగా 301వ పుటలో లేటరైట్ 1%, తీర ఇసుక 3%గా ఉండి పరస్పర విరుద్ధంగా ఉన్నాయి. 2. ఈ వైరుధ్యాన్ని దాచిపెట్టి రెండు శాతాల సమూహాలనూ ఒకేసారి స్కోరింగ్‌కు వాడాలి. 3. ఆంధ్రప్రదేశ్ పటంలో పాత జిల్లా సరిహద్దులు, ఎర్ర–నల్ల–ఒండ్రు–తీర/ఇతర అనే స్థూల వర్గాలే ఉన్నాయి. 4. జిల్లాల్లో నేల మిశ్రమాలు, మార్పు మండలాలు ఉండటం వల్ల స్థానిక అధ్యయనానికి ప్రస్తుత APSAC జిల్లా వనరుల పటాలు మెరుగైనవి. సరైనవి ఏవి?",
        "answer": 3,
        "explanation_en": "Statements 1, 3 and 4 are correct; statement 2 is false. The contradiction must be displayed and dated, not converted into two simultaneous facts. Upland and forest soils also vary with slope, rock, vegetation and erosion.",
        "explanation_te": "1, 3, 4 సరైనవి; 2 తప్పు. వైరుధ్యాన్ని స్పష్టంగా చూపి మూలం, తేదీతో చెప్పాలి; రెండు సంఖ్యలనూ ఒకేసారి నిజంగా వాడరాదు. ఎత్తుభాగ, అటవీ నేలలు కూడా వాలు, శిల, వృక్షజాలం, కోతను బట్టి మారతాయి.",
    },
]


def main() -> None:
    data = json.loads(BANK.read_text(encoding="utf-8"))
    existing = {q["id"]: index for index, q in enumerate(data["questions"])}
    sources = [
        "https://www.nrcs.usda.gov/resources/education-and-teaching-materials/soil-facts",
        "https://www.nrcs.usda.gov/resources/education-and-teaching-materials/the-twelve-orders-of-soil-taxonomy",
        "https://icar.gov.in/sites/default/files/2025-11/December_2025%20Indian%20Farming.pdf",
        "https://apsac.ap.gov.in/?page_id=179",
    ]
    for row in ROWS:
        answer = row["answer"]
        options_en, options_te = CUSTOM_COMBOS.get(row["id"], (COMBOS_EN, COMBOS_TE))
        option_explanations_en = []
        option_explanations_te = []
        for index, option in enumerate(options_en, 1):
            if index == answer:
                option_explanations_en.append("This combination includes every correct statement and excludes the incorrect statement, if any.")
                option_explanations_te.append("ఈ కలయిక సరైన వాక్యాలన్నిటినీ తీసుకుని, తప్పు వాక్యం ఉంటే దానిని మినహాయిస్తుంది.")
            else:
                option_explanations_en.append("This combination either omits a correct statement or includes the incorrect statement; compare each numbered statement with the explanation.")
                option_explanations_te.append("ఈ కలయిక ఒక సరైన వాక్యాన్ని వదులుతుంది లేదా తప్పు వాక్యాన్ని చేర్చుతుంది; ప్రతి సంఖ్యా వాక్యాన్ని వివరణతో పోల్చాలి.")
        record = {
            "id": row["id"], "chapter": "IA-05", "origin": "book-audit-original",
            "label": "Original APPSC-style practice; not an official previous-year question",
            "language": "bilingual", "kind": "multiple-statements", "difficulty": "moderate",
            "fact_ids": row["facts"], "question_en": row["question_en"], "question_te": row["question_te"],
            "options_en": options_en, "options_te": options_te, "answer": answer,
            "option_explanations_en": option_explanations_en,
            "option_explanations_te": option_explanations_te,
            "explanation_en": row["explanation_en"], "explanation_te": row["explanation_te"],
            "section": row["section"], "related_sections": [],
            "source_paragraph": row["explanation_en"], "source_page": row["page"],
            "source_urls": sources, "reviewed_on": "2026-11-01", "manual_review_status": "reviewed",
        }
        if row["id"] in existing:
            data["questions"][existing[row["id"]]] = record
        else:
            data["questions"].append(record)
    data["questions"].sort(key=lambda q: (0 if q["id"].startswith("GEO-ORIG") else 1, q["id"]))
    BANK.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
