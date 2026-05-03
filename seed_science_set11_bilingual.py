import sqlite3, os

SOURCE = 'Science_Set11_Human_System2'
DB = os.path.join(os.path.dirname(__file__), 'mnt/mcq_app/database.db')

questions = [
    # Q1
    (
        "For transfusion, the 'O' blood group of a donor can be accepted by a person having blood group\nతెలుగు: రక్త మార్పిడి (transfusion) కోసం, 'O' రక్తపు గ్రూపు ఉన్న దాత నుండి రక్తాన్ని కింది ఏ రక్తపు గ్రూపు ఉన్న వ్యక్తి స్వీకరించవచ్చు?",
        "A / A",
        "B / B",
        "AB / AB",
        "All of these / ఇవన్నీ",
        "D", "E",
        "O blood group = Universal Donor. O group has NO antigens (A or B) on RBC surface → no agglutination reaction with any recipient's antibodies. "
        "O blood can be given to ALL blood groups: A, B, AB, and O. "
        "O రక్తపు గ్రూపు = విశ్వ దాత; RBC పై యాంటీజన్లు లేవు → A, B, AB, O అన్ని గ్రూపులవారికి ఇవ్వవచ్చు.",
        1
    ),
    # Q2
    (
        "Which of the following structures (glands) is concerned with the production of cortisone hormone in man?\nతెలుగు: మానవులలో కార్టిసోన్ హార్మోన్ ఉత్పత్తికి కింది ఏ నిర్మాణాలు (గ్రంథులు) సంబంధించినవి?",
        "Thyroid / థైరాయిడ్",
        "Testis / ముష్కాలు",
        "Adrenal / అడ్రినల్",
        "Pancreas / క్లోమం",
        "C", "M",
        "CORTISONE (cortisol) = glucocorticoid hormone secreted by the ADRENAL CORTEX (outer layer of adrenal gland). "
        "Adrenal cortex secretes: Glucocorticoids (cortisol/cortisone → stress response, anti-inflammatory), Mineralocorticoids (aldosterone → BP regulation), Sex hormones (DHEA). "
        "Adrenal medulla secretes: Adrenaline and Noradrenaline. "
        "కార్టిసోన్ = అడ్రినల్ కార్టెక్స్ (బాహ్య పొర) స్రవించే గ్లూకోకార్టికాయిడ్ హార్మోన్; ఒత్తిడి నిర్వహణ, వాపు వ్యతిరేక చర్యలకు సహాయపడుతుంది.",
        2
    ),
    # Q3
    (
        "The largest gland in the human body is\nతెలుగు: మానవ శరీరంలో అతిపెద్ద గ్రంథి ఏది?",
        "Heart / గుండె",
        "Liver / కాలేయం",
        "Kidney / మూత్రపిండం",
        "Brain / మెదడు",
        "B", "E",
        "LIVER = largest GLAND in the human body (weighs ~1.2–1.5 kg in adults). Also the largest INTERNAL ORGAN (if skin is excluded). "
        "Functions: Bile production, glycogen storage, protein synthesis (fibrinogen, albumin), detoxification, urea formation, bilirubin formation. "
        "Largest organ overall = SKIN. Largest internal organ = Liver. Largest gland = Liver. Smallest endocrine gland = Pineal. "
        "కాలేయం = మానవ శరీరంలో అతిపెద్ద గ్రంథి (~1.2-1.5 kg); పైత్య రసం ఉత్పత్తి, గ్లైకోజెన్ నిల్వ, డిటాక్సిఫికేషన్ విధులు.",
        3
    ),
    # Q4
    (
        "The most important function of perspiration is to\nతెలుగు: చెమట పట్టడం (perspiration) యొక్క అత్యంత ముఖ్యమైన విధి ఏమిటి?",
        "Lubricate the skin / చర్మాన్ని మృదువుగా ఉంచడం",
        "Get rid of the body wastes / శరీర వ్యర్థాలను వదిలించుకోవడం",
        "Regulate body temperature / శరీర ఉష్ణోగ్రతను నియంత్రించడం",
        "Regulate body wastes / శరీర వ్యర్థాలను నియంత్రించడం",
        "B", "H",
        "⚠ Exam key: (b) Get rid of body wastes. Scientifically: The PRIMARY function of perspiration = THERMOREGULATION (c) — sweat evaporates and cools the body. "
        "Secondary function = excretion of wastes (urea, salts, water). For exam, follow answer key (b). "
        "⚠ పరీక్ష కీ: (b) వ్యర్థాలను వదిలించుకోవడం. శాస్త్రీయంగా: చెమట పట్టడం ప్రధానంగా శరీర ఉష్ణోగ్రతను నియంత్రించడానికి (c). పరీక్షలో (b) గుర్తించండి.",
        4
    ),
    # Q5
    (
        "DNA polymerase catalyses the addition of nucleotides during DNA replication. Its main role is to:\nతెలుగు: DNA ప్రతికృతి (replication) సమయంలో న్యూక్లియోటైడ్ల చేరికను DNA పాలిమరేస్ ఉత్ప్రేరకపరుస్తుంది. దాని ప్రధాన పాత్ర ఏమిటి?",
        "Ligate Okazaki fragments together / ఒకజాకి ఖండితాలను కలపడం",
        "Remove RNA primers from the lagging strand / లాగింగ్ స్ట్రాండ్ నుండి RNA ప్రైమర్లను తొలగించడం",
        "Synthesise new DNA strands complementary to the template / మూసకు పరిపూరకమైన కొత్త DNA పోచలను సంశ్లేషణ చేయడం",
        "Unwind the DNA double helix / DNA డబుల్ హెలిక్స్‌ను విడదీయడం",
        "C", "H",
        "DNA Polymerase III = main enzyme in DNA replication; adds nucleotides in 5'→3' direction complementary to template strand. "
        "Other roles in replication: Helicase = unwinds double helix (d); DNA Ligase = joins Okazaki fragments (a); RNase H / DNA Pol I = removes RNA primers (b). "
        "DNA పాలిమరేస్ III: మూస (template) కు పరిపూరకమైన కొత్త DNA పోచలను సంశ్లేషణ చేస్తుంది; 5'→3' దిశలో న్యూక్లియోటైడ్లను చేరుస్తుంది.",
        5
    ),
    # Q6
    (
        "A heart beat requires approximately\nతెలుగు: ఒక గుండె స్పందనకు (heart beat) సుమారుగా ఎంత సమయం పడుతుంది?",
        "0.5 second / 0.5 సెకను",
        "0.8 second / 0.8 సెకను",
        "0.5 minute / 0.5 నిమిషం",
        "1 minute / 1 నిమిషం",
        "B", "E",
        "One complete cardiac cycle (heartbeat) = approximately 0.8 seconds at normal resting heart rate (~72-75 bpm). "
        "Cardiac cycle: Atrial systole (0.1 sec) + Ventricular systole (0.3 sec) + Diastole/relaxation (0.4 sec) = 0.8 sec total. "
        "Calculation: 60 sec ÷ 72 bpm ≈ 0.83 sec per beat. "
        "ఒక గుండె చక్రం (cardiac cycle): ~0.8 సెకండ్లు; కర్ణిక సంకోచం (0.1 s) + జఠర సంకోచం (0.3 s) + వ్యాకోచం (0.4 s) = 0.8 s.",
        6
    ),
    # Q7
    (
        "Which of the following glands in the human body is popularly called 'Adam's apple'?\nతెలుగు: మానవ శరీరంలోని ఏ గ్రంథిని సాధారణంగా 'ఆడమ్స్ యాపిల్' (Adam's apple) అని పిలుస్తారు?",
        "Adrenal / అడ్రినల్",
        "Pituitary / పిట్యూటరీ",
        "Thyroid / థైరాయిడ్",
        "Thymus / థైమస్",
        "C", "M",
        "Adam's apple = the visible laryngeal prominence of the THYROID CARTILAGE in the neck (not the thyroid gland itself). "
        "The exam treats the answer as (c) Thyroid because it is the associated structure. More prominent in males (testosterone-driven growth during puberty). "
        "Thyroid gland = butterfly-shaped gland at the base of the neck; secretes Thyroxine (T3/T4). "
        "'ఆడమ్స్ యాపిల్' = మెడలో థైరాయిడ్ కార్టిలేజ్ యొక్క దృశ్యమాన ఉబ్బు; పరీక్ష సమాధానం (c) థైరాయిడ్; పురుషులలో ఎక్కువగా కనిపిస్తుంది.",
        7
    ),
    # Q8
    (
        "Human body needs a constant supply of proteins to survive. The first part of the digestive system to begin digesting proteins is\nతెలుగు: ప్రోటీన్లను జీర్ణం చేయడం ప్రారంభించే జీర్ణవ్యవస్థలోని మొదటి భాగం ఏది?",
        "Mouth / నోరు",
        "Stomach / జీర్ణాశయం",
        "Small intestine / చిన్న ప్రేగు",
        "Large intestine / పెద్ద ప్రేగు",
        "B", "E",
        "Protein digestion starts in the STOMACH. Gastric juice contains: HCl (denatures proteins, activates pepsinogen) + PEPSIN (active enzyme that digests proteins → peptides). "
        "Note: Mouth — salivary amylase digests starch only, no protein. Small intestine — further protein digestion by trypsin (pancreatic), chymotrypsin, peptidases. "
        "ప్రోటీన్ జీర్ణం: జీర్ణాశయంలో మొదలవుతుంది; HCl + పెప్సిన్ (pepsin) ప్రోటీన్లను పెప్టైడ్‌లుగా మారుస్తాయి. నోటిలో పిండి మాత్రమే జీర్ణమవుతుంది.",
        8
    ),
    # Q9
    (
        "Ultrafiltering unit of kidney is known as\nతెలుగు: మూత్రపిండం యొక్క అల్ట్రాఫిల్టరింగ్ (సూక్ష్మ వడపోత) యూనిట్‌ను ఏమంటారు?",
        "Nephron / నెఫ్రాన్",
        "Glomerulus / గ్లోమెరులస్",
        "Tubule / ట్యూబ్యూల్",
        "Venacava / వెనాకావా",
        "B", "M",
        "GLOMERULUS = the ultrafiltering unit — a tuft of capillaries inside the Bowman's capsule that filters blood under pressure (ultrafiltration). "
        "NEPHRON = structural and functional unit of kidney (includes glomerulus + tubules + collecting duct). "
        "Filtration rate: ~125 mL/min (GFR); ~180 L/day filtered → ~1.5-2 L urine/day. "
        "గ్లోమెరులస్ = మూత్రపిండం యొక్క అల్ట్రాఫిల్టరింగ్ యూనిట్; బౌమాన్స్ కాప్సూల్‌లో రక్తాన్ని వడపోస్తుంది. నెఫ్రాన్ = నిర్మాణ + క్రియాత్మక యూనిట్.",
        9
    ),
    # Q10
    (
        "In the human body, the leg bones are\nతెలుగు: మానవ శరీరంలో కాలి ఎముకలు ఏవి?",
        "Humerus & Femur / హ్యూమరస్ & ఫీమర్",
        "Fibula & Tibia / ఫైబులా & టిబియా",
        "Fibula & Ulna / ఫైబులా & ఉల్నా",
        "Tibia & Radius / టిబియా & రేడియస్",
        "B", "E",
        "Leg bones (lower leg/shin area): TIBIA (shinbone, larger — weight bearing) and FIBULA (smaller, lateral). "
        "Upper leg = FEMUR (thighbone, longest/strongest bone). Knee = Patella. "
        "Arm bones: Humerus (upper arm); Radius + Ulna (forearm). Ulna + Fibula confusion: both are smaller bones in a pair (arm vs leg). "
        "కాలి ఎముకలు (lower leg): టిబియా (shinbone) + ఫైబులా. తొడ ఎముక = ఫీమర్ (శరీరంలో అతిపెద్ద ఎముక). చేయి: హ్యూమరస్ (పై), రేడియస్ + ఉల్నా (ముంచేయి).",
        10
    ),
    # Q11
    (
        "All the veins carry deoxygenated blood, except\nతెలుగు: దేనిలో తప్ప, మిగతా అన్ని సిరలు (veins) ఆక్సిజన్ లేని (deoxygenated) రక్తాన్ని తీసుకువెళతాయి?",
        "Hepatic vein / హెపాటిక్ సిర",
        "Subclavian vein / సబ్‌క్లావియన్ సిర",
        "Pulmonary vein / పల్మనరీ సిర (పుపుస సిర)",
        "Portal vein / పోర్టల్ సిర",
        "C", "M",
        "PULMONARY VEIN = the ONLY vein that carries OXYGENATED blood. It carries blood from lungs (after oxygenation) to the LEFT ATRIUM of heart. "
        "Similarly: PULMONARY ARTERY carries deoxygenated blood (only artery to do so) from right ventricle to lungs. "
        "Memory: Veins normally carry deoxygenated blood to heart; Pulmonary vein is the exception (lungs → heart). "
        "పల్మనరీ సిర = ఏకైక సిర ఆక్సిజన్ కలిగిన రక్తాన్ని తీసుకువెళ్ళేది (ఊపిరితిత్తులు → హృదయం). పల్మనరీ ధమని = ఏకైక ధమని డీఆక్సిజన్ రక్తాన్ని తీసుకువెళ్ళేది.",
        11
    ),
    # Q12
    (
        "Insulin is secreted in\nతెలుగు: ఇన్సులిన్ (Insulin) దేనిలో స్రవిస్తుంది?",
        "Pituitary / పిట్యూటరీ",
        "Liver / కాలేయం",
        "Pancreas / ప్యాంక్రియాస్ (క్లోమం)",
        "Parathyroid / పారాథైరాయిడ్",
        "C", "E",
        "INSULIN = secreted by BETA (β) cells of the Islets of Langerhans in the PANCREAS. "
        "Glucagon = secreted by ALPHA (α) cells of Islets of Langerhans. "
        "Insulin lowers blood glucose; Glucagon raises blood glucose. Insulin deficiency → Diabetes Mellitus (Type 1 = no insulin; Type 2 = insulin resistance). "
        "ఇన్సులిన్: క్లోమంలోని ల్యాంగర్‌హాన్స్ ద్వీపాల బీటా (β) కణాలు స్రవిస్తాయి. ఇన్సులిన్ లోపం → డయాబెటిస్ మెల్లిటస్. గ్లుకగాన్ = ఆల్ఫా (α) కణాలు.",
        12
    ),
    # Q13
    (
        "The organ in the body which accumulates iodine is\nతెలుగు: శరీరంలో అయోడిన్‌ను నిల్వచేసే అవయవం ఏది?",
        "Pituitary gland / పిట్యూటరీ గ్రంథి",
        "Thymus / థైమస్",
        "Thyroid gland / థైరాయిడ్ గ్రంథి",
        "Spleen / ప్లీహం",
        "C", "E",
        "THYROID GLAND accumulates iodine to synthesize thyroid hormones T3 (Triiodothyronine) and T4 (Thyroxine). "
        "T4 has 4 iodine atoms; T3 has 3 iodine atoms. Iodine is actively transported into thyroid cells (iodine trap). "
        "Iodine deficiency → goiter (enlarged thyroid), hypothyroidism. Iodized salt prevents iodine deficiency. "
        "థైరాయిడ్ గ్రంథి అయోడిన్‌ను నిల్వ చేసి T3 మరియు T4 (థైరాక్సిన్) హార్మోన్లను తయారు చేస్తుంది. అయోడిన్ లోపం → గాయిటర్.",
        13
    ),
    # Q14
    (
        "In metabolism, enzymes act as\nతెలుగు: జీవక్రియలో (metabolism), ఎంజైమ్‌లు దేనిగా పనిచేస్తాయి?",
        "Promoter / ప్రమోటర్",
        "Catalyst / ఉత్ప్రేరకం",
        "Oxidant / ఆక్సిడెంట్",
        "Reductant / రిడక్టెంట్",
        "B", "E",
        "ENZYMES = biological CATALYSTS (speed up chemical reactions without being consumed). They lower the activation energy of metabolic reactions. "
        "Properties: Specific (lock-and-key model), reusable, sensitive to temperature (denatured above ~40-50°C) and pH. "
        "Most enzymes are proteins (except ribozymes which are RNA). Key metabolic enzymes: Amylase, Pepsin, Lipase, ATP synthase, DNA polymerase. "
        "ఎంజైమ్‌లు = జీవ ఉత్ప్రేరకాలు; జీవక్రియలను వేగవంతం చేస్తాయి; తాము మారవు. యాక్టివేషన్ శక్తిని తగ్గిస్తాయి; ప్రోటీన్లు (రైబోజైమ్‌లు తప్ప).",
        14
    ),
    # Q15
    (
        "The life of RBC (Red Blood Cell) in human blood is\nతెలుగు: మానవ రక్తంలో ఎర్ర రక్త కణాల (RBC) జీవితకాలం ఎంత?",
        "30 days / 30 రోజులు",
        "60 days / 60 రోజులు",
        "120 days / 120 రోజులు",
        "15 hours / 15 గంటలు",
        "C", "E",
        "RBC (Erythrocyte) lifespan = 120 days (approximately 4 months). After 120 days, old RBCs are destroyed by Spleen (graveyard of RBCs). "
        "RBCs are produced in Red bone marrow (hematopoiesis). In adults, production occurs in flat bones (sternum, ribs, skull). "
        "Comparison: WBC lifespan = days to years (varies by type); Platelet lifespan = 7–10 days. "
        "RBC జీవితకాలం = 120 రోజులు; తర్వాత ప్లీహంలో నాశనం; ఎముక మజ్జలో (hematopoiesis) ఉత్పత్తి. ఫలకికలు = 7-10 రోజులు.",
        15
    ),
    # Q16
    (
        "The phenomenon of 'Test Tube Baby' refers to\nతెలుగు: 'టెస్ట్ ట్యూబ్ బేబీ' (Test Tube Baby) అనే దృగ్విషయం దేనిని సూచిస్తుంది?",
        "When every process of embryo formation is in the test tube / పిండం ఏర్పడే ప్రతి ప్రక్రియ టెస్ట్ ట్యూబ్‌లోనే జరిగినప్పుడు",
        "When the embryo develops in a test tube / పిండం టెస్ట్ ట్యూబ్‌లో అభివృద్ధి చెందినప్పుడు",
        "When the fertilization is external and development is internal / ఫలదీకరణం బాహ్యంగా మరియు అభివృద్ధి అంతర్గతంగా జరిగినప్పుడు",
        "When the fertilization is internal and development is external / ఫలదీకరణం అంతర్గతంగా మరియు అభివృద్ధి బాహ్యంగా జరిగినప్పుడు",
        "B", "H",
        "⚠ Exam key: (b). Scientifically: IVF (In Vitro Fertilization) = fertilization occurs OUTSIDE the body (in lab dish/test tube) → then embryo is transferred to uterus for development (c is scientifically more precise). "
        "First test tube baby = Louise Brown (1978, UK); IVF pioneers = Robert Edwards and Patrick Steptoe. "
        "⚠ పరీక్ష కీ: (b) పిండం టెస్ట్ ట్యూబ్‌లో అభివృద్ధి చెందడం. శాస్త్రీయంగా: ఫలదీకరణం బయట జరిగి, అభివృద్ధి గర్భంలో జరుగుతుంది (c సరైనది). పరీక్షకు (b).",
        16
    ),
    # Q17
    (
        "Red blood corpuscles are formed in\nతెలుగు: ఎర్ర రక్త కణాలు ఎక్కడ ఏర్పడతాయి?",
        "Liver / కాలేయం",
        "Small intestine / చిన్న ప్రేగు",
        "Kidneys / మూత్రపిండాలు",
        "Bone marrow / ఎముక మజ్జ",
        "D", "E",
        "RBCs are produced in RED BONE MARROW (hematopoiesis/erythropoiesis). In adults: flat bones (sternum, ribs, vertebrae, skull, pelvis). "
        "In foetal stage: Liver → Spleen → Bone marrow (sequence of sites). "
        "Erythropoietin (EPO) hormone from kidneys stimulates RBC production. RBCs lack a nucleus (anucleate) in mature form in mammals. "
        "RBC లు ఎర్ర ఎముక మజ్జలో (hematopoiesis) తయారవుతాయి. పిండ దశలో: కాలేయం → ప్లీహం → ఎముక మజ్జ. EPO హార్మోన్ (మూత్రపిండాల నుండి) RBC ఉత్పత్తిని ప్రేరేపిస్తుంది.",
        17
    ),
    # Q18
    (
        "In a healthy human eye, the focusing is done by\nతెలుగు: ఆరోగ్యవంతమైన మానవ కంటిలో, కేంద్రీకరించడం (focusing) దేని ద్వారా జరుగుతుంది?",
        "To and fro movement of the eye lens / కంటి కటకం ముందుకు వెనుకకు కదలడం ద్వారా",
        "Changing curvature of the retina / రెటీనా వక్రతను మార్చడం ద్వారా",
        "Change in the convexity of the lens through ciliary muscles / సిలియరీ కండరాల ద్వారా కటకం యొక్క కుంభాకారతలో మార్పు ద్వారా",
        "Change in the refractive index of the eye fluid / కంటి ద్రవం యొక్క వక్రీభవన గుణకంలో మార్పు ద్వారా",
        "C", "M",
        "EYE ACCOMMODATION: The eye lens changes its curvature (convexity) through CILIARY MUSCLES. "
        "Near object: Ciliary muscles contract → suspensory ligaments relax → lens becomes MORE CONVEX (thicker) → higher power → near focus. "
        "Far object: Ciliary muscles relax → ligaments taut → lens becomes LESS CONVEX (thinner) → lower power → far focus. "
        "కంటి కేంద్రీకరణ (accommodation): సిలియరీ కండరాలు కటకం కుంభాకారత మారుస్తాయి; దగ్గరి వస్తువుకు = కటకం మందంగా (ఎక్కువ కుంభాకారం); దూర వస్తువుకు = తక్కువ కుంభాకారం.",
        18
    ),
    # Q19
    (
        "Which of the following is not present in the blood?\nతెలుగు: కింది వాటిలో రక్తంలో లేనిది ఏది?",
        "RBCs (Red Blood Cells) / ఎర్ర రక్త కణాలు",
        "WBCs (White Blood Cells) / తెల్ల రక్త కణాలు",
        "Placenta (Plasanta) / ప్లాసెంటా (జరాయువు)",
        "Plasma / ప్లాస్మా",
        "C", "E",
        "PLACENTA = organ that forms during pregnancy; connects mother and foetus via umbilical cord; NOT present in blood. "
        "Blood contains: RBCs, WBCs, Platelets (formed elements = 45%) + Plasma (liquid = 55%). "
        "Note: 'Plasanta' in the question is a typo for 'Placenta'. Placenta enables exchange of nutrients, O₂, and waste between mother and foetus. "
        "ప్లాసెంటా = గర్భావస్థలో ఏర్పడే అవయవం; అమ్మ మరియు పిండాన్ని కలుపుతుంది; రక్తంలో ఉండదు. రక్తంలో ఉండేవి: RBC, WBC, ఫలకికలు, ప్లాస్మా.",
        19
    ),
    # Q20
    (
        "The thyroid gland is situated near which of the following organs?\nతెలుగు: థైరాయిడ్ గ్రంథి కింది ఏ అవయవాల దగ్గర అమరి ఉంటుంది?",
        "Liver / కాలేయం",
        "Spleen / ప్లీహం",
        "Larynx / స్వరపేటిక",
        "Kidney / మూత్రపిండం",
        "C", "E",
        "THYROID GLAND = butterfly-shaped gland located in the NECK, anterior to the TRACHEA, just below the LARYNX (voice box). "
        "Has two lobes connected by isthmus. Secretes T3, T4 (with iodine), and Calcitonin. "
        "Adam's apple = thyroid cartilage of larynx (just above thyroid gland). "
        "థైరాయిడ్ గ్రంథి: మెడలో స్వరపేటిక (larynx) కింద, శ్వాసనాళం (trachea) ముందు ఉంటుంది; సీతాకోకచిలుక ఆకారంలో ఉంటుంది.",
        20
    ),
    # Q21
    (
        "The salivary glands secrete saliva which contains the enzyme\nతెలుగు: లాలాజల గ్రంథులు స్రవించే లాలాజలంలో ఉండే ఎంజైమ్ ఏది?",
        "Pepsin / పెప్సిన్",
        "Renin / రెనిన్",
        "Ptyalin / టయలిన్",
        "Lipase / లైపేజ్",
        "C", "E",
        "PTYALIN (Salivary Amylase) = enzyme in saliva; digests STARCH → Maltose (partial digestion in mouth). "
        "Saliva also contains: Mucin (lubricates food), Lysozyme (antibacterial), Water (99.5%), IgA antibodies. "
        "Note: Pepsin = stomach (protein digestion); Lipase = pancreas/small intestine (fat); Rennin/Chymosin = stomach enzyme in infants that curdles milk protein (NOT the same as Renin, which is a kidney enzyme for BP regulation). "
        "టయలిన్ (సెలైవరీ అమైలేజ్): లాలాజలంలోని ఎంజైమ్; స్టార్చ్ → మాల్టోస్. పెప్సిన్ = జీర్ణాశయం; లైపేజ్ = కొవ్వులు; రెనిన్/Chymosin = పాల ప్రోటీన్ గడ్డ కట్టించే ఎంజైమ్ (శిశువులలో); మూత్రపిండాల రెనిన్ ≠ ఇది.",
        21
    ),
    # Q22
    (
        "Convex lenses are used for the correction of\nతెలుగు: కుంభాకార కటకాలను (Convex lenses) దేనిని సరిచేయడానికి ఉపయోగిస్తారు?",
        "Astigmatism / ఆస్టిగ్మాటిజం",
        "Short-sightedness / హ్రస్వదృష్టి",
        "Cataract / కంటిశుక్లం",
        "Long-sightedness / దీర్ఘదృష్టి",
        "D", "M",
        "CONVEX (converging) lens corrects HYPERMETROPIA (Long-sightedness/Farsightedness). "
        "Hypermetropia: eyeball too short → image forms behind retina → convex lens converges light to bring image onto retina. "
        "CONCAVE (diverging) lens corrects MYOPIA (Short-sightedness). "
        "Astigmatism = corrected by cylindrical lens; Cataract = treated by surgery (lens replacement). "
        "కుంభాకార కటకం → దీర్ఘదృష్టి (Hypermetropia) సరిదిద్దుతుంది. పుటాకార కటకం → హ్రస్వదృష్టి (Myopia). ఆస్టిగ్మాటిజం → సిలిండ్రికల్ కటకం.",
        22
    ),
    # Q23
    (
        "How much blood does an average adult have in the body?\nతెలుగు: సగటు వయోజనుడి శరీరంలో ఎంత రక్తం ఉంటుంది?",
        "3-4 litres / 3-4 లీటర్లు",
        "4-5 litres / 4-5 లీటర్లు",
        "5-6 litres / 5-6 లీటర్లు",
        "6-7 litres / 6-7 లీటర్లు",
        "C", "E",
        "Average adult human blood volume = 5–6 litres (approximately 7–8% of body weight). "
        "Male: ~5.5–6 L; Female: ~4.5–5 L (slightly less due to smaller body mass). "
        "Blood volume decreases significantly → shock; Rapid loss of >30% = hypovolemic shock. "
        "సగటు వయోజనుడి రక్తం = 5-6 లీటర్లు (శరీర బరువులో ~7-8%); పురుషులు ~5.5-6 L; స్త్రీలు ~4.5-5 L.",
        23
    ),
    # Q24
    (
        "Which sugar is present in considerable amounts in the blood?\nతెలుగు: రక్తంలో గణనీయమైన పరిమాణంలో ఉండే చక్కెర ఏది?",
        "Glucose / గ్లూకోజ్",
        "Fructose / ఫ్రక్టోజ్",
        "Galactose / గెలాక్టోజ్",
        "Sucrose / సుక్రోజ్",
        "A", "E",
        "GLUCOSE = the primary sugar in blood (blood sugar). Normal fasting blood glucose = 70–100 mg/dL. "
        "Fructose and Galactose are absorbed in small intestine and converted to glucose in liver. Sucrose (table sugar) is a disaccharide — broken down before absorption. "
        "Insulin regulates blood glucose by promoting uptake into cells. Glucagon raises blood glucose from glycogen stores. "
        "రక్తంలో ప్రధాన చక్కెర = గ్లూకోజ్ (blood sugar); సాధారణ స్థాయి = 70-100 mg/dL. ఇన్సులిన్ రక్తంలో గ్లూకోజ్‌ను తగ్గిస్తుంది; గ్లుకగాన్ పెంచుతుంది.",
        24
    ),
    # Q25
    (
        "Foetus development in a woman's womb can be ascertained by\nతెలుగు: స్త్రీ గర్భంలో పిండం అభివృద్ధిని దేని ద్వారా నిర్ధారించవచ్చు?",
        "CAT scanning / CAT స్కానింగ్",
        "PTT scanning / PTT స్కానింగ్",
        "Ultrasound / అల్ట్రాసౌండ్",
        "Co-27 experiment / Co-27 ప్రయోగం",
        "C", "E",
        "ULTRASOUND (Sonography) = safe, non-invasive imaging technique used to visualize foetus development in the womb. Uses high-frequency sound waves (>20,000 Hz). "
        "CAT scan = Computed Axial Tomography (uses X-rays — not used during pregnancy due to radiation risk). "
        "Ultrasound detects: foetal heartbeat, position, size, anomalies, multiple pregnancies, gestational age. "
        "అల్ట్రాసౌండ్ (సోనోగ్రఫీ): అధిక పౌనఃపున్య ధ్వని తరంగాలు (~20,000 Hz పైన); గర్భంలో పిండం అభివృద్ధిని చూడడానికి సురక్షితమైన పద్ధతి. CAT స్కాన్ = X-కిరణాలు (గర్భంలో వాడరు).",
        25
    ),
    # Q26
    (
        "The internal secretion of _____ helps in digestion.\nతెలుగు: కింది వాటిలో దేని అంతర్గత స్రావం జీర్ణక్రియకు సహాయపడుతుంది?",
        "Citric acid / సిట్రిక్ ఆమ్లం",
        "Sulphuric acid / సల్ఫ్యూరిక్ ఆమ్లం",
        "Acetic acid / ఎసిటిక్ ఆమ్లం",
        "Hydrochloric acid / హైడ్రోక్లోరిక్ ఆమ్లం",
        "D", "E",
        "HYDROCHLORIC ACID (HCl) is secreted by parietal cells of the stomach and helps in digestion: "
        "1. Converts pepsinogen → pepsin (active protein-digesting enzyme). 2. Provides acidic pH (~1.5–2) for pepsin activity. 3. Kills ingested bacteria. 4. Denatures food proteins for easier digestion. "
        "HCl (హైడ్రోక్లోరిక్ ఆమ్లం): జీర్ణాశయంలో పారైటల్ కణాలు స్రవిస్తాయి; పెప్సినోజెన్ → పెప్సిన్ మారుస్తుంది; ఆమ్ల వాతావరణం (pH 1.5-2) కల్పిస్తుంది; బ్యాక్టీరియాను చంపుతుంది.",
        26
    ),
    # Q27
    (
        "Saliva in humans is\nతెలుగు: మానవులలో లాలాజలం ఏ స్వభావాన్ని కలిగి ఉంటుంది?",
        "Acidic / ఆమ్ల",
        "Alkaline / క్షార",
        "Neutral / తటస్థ",
        "None of these / ఇవేవీ కావు",
        "B", "H",
        "⚠ Exam key: (b) Alkaline. Scientifically: Saliva pH ≈ 6.2–7.4 (slightly acidic to neutral, average ~6.8). "
        "For amylase (ptyalin) to work optimally, saliva should be slightly alkaline (~pH 7-8); however, measured pH is slightly acidic. "
        "For exam purposes, follow answer key (b) Alkaline. "
        "⚠ పరీక్ష కీ: (b) క్షార. శాస్త్రీయంగా: లాలాజలం pH ≈ 6.2-7.4 (సాధారణంగా కొద్దిగా ఆమ్లం). పరీక్షలో (b) అనుసరించండి.",
        27
    ),
    # Q28
    (
        "Muscles are of three types. Which of the following is NOT one of them?\nతెలుగు: కండరాలు మూడు రకాలు. కింది వాటిలో వాటికి చెందనిది ఏది?",
        "Sesamoids / సెసామాయిడ్స్",
        "Smooth / నునుపు కండరాలు",
        "Cardiac / హృదయ కండరాలు",
        "Skeletal / అస్థి కండరాలు",
        "A", "E",
        "Three types of muscles: 1. SKELETAL (striated/voluntary) — attached to bones; under conscious control. "
        "2. SMOOTH (non-striated/involuntary) — in walls of internal organs (stomach, intestine, uterus, blood vessels). "
        "3. CARDIAC (striated/involuntary) — only in the heart; myogenic (generates its own impulse). "
        "SESAMOIDS = small bones embedded in tendons (e.g., patella/kneecap), NOT a type of muscle. "
        "కండర రకాలు 3: అస్థి (ఐచ్ఛిక), నునుపు (అనైచ్ఛిక), హృదయ (అనైచ్ఛిక). సెసామాయిడ్స్ = అస్థిబంధాలలో పొందుపడిన చిన్న ఎముకలు (కండరాలు కాదు).",
        28
    ),
    # Q29
    (
        "Any foreign particle that stimulates the formation of antibodies is called\nతెలుగు: ప్రతిరక్షకాల (antibodies) ఏర్పాటును ప్రేరేపించే ఏదైనా విదేశీ కణాన్ని ఏమంటారు?",
        "Histone / హిస్టోన్",
        "Antigen / యాంటిజెన్ (ప్రతిజనకం)",
        "Receptor / రిసెప్టార్",
        "Antibiotic / యాంటీబయాటిక్",
        "B", "E",
        "ANTIGEN (Antibody Generator) = any substance (usually protein/polysaccharide on pathogens) that stimulates the immune system to produce ANTIBODIES. "
        "Antibodies = immunoglobulins (Y-shaped proteins) produced by B lymphocytes/plasma cells; bind specifically to antigens. "
        "Note: Histone = proteins that package DNA; Receptor = cell surface protein that binds specific molecules; Antibiotic = drug that kills bacteria. "
        "యాంటిజెన్ = ప్రతిరక్షకాల ఏర్పాటును ప్రేరేపించే విదేశీ పదార్థం; యాంటీబాడీలు = B లింఫోసైట్లు ఉత్పత్తి చేసే Y-ఆకార ప్రోటీన్లు.",
        29
    ),
    # Q30
    (
        "Which of the following statements about the liver is true?\n"
        "1. It secretes bile enzyme.\n"
        "2. It forms fibrinogen that helps in clotting of blood.\n"
        "3. It produces heparin which prevents blood clotting in blood vessels.\n"
        "4. It is affected by excessive alcohol intake.\n"
        "తెలుగు: కాలేయానికి సంబంధించి కింది ఏ వాక్యాలు సరైనవి?\n"
        "1. ఇది పైత్యరస ఎంజైమ్‌ను స్రవిస్తుంది. 2. ఇది ఫైబ్రినోజెన్‌ను ఏర్పరుస్తుంది. 3. ఇది హెపారిన్‌ను ఉత్పత్తి చేస్తుంది. 4. ఇది అధిక మద్యపానంతో ప్రభావితమవుతుంది.",
        "1 and 4 / 1 మరియు 4",
        "1, 2, and 3 / 1, 2, మరియు 3",
        "1, 2, and 4 / 1, 2, మరియు 4",
        "1, 2, 3, and 4 / 1, 2, 3, మరియు 4",
        "C", "H",
        "Exam key: (c) Statements 1, 2, and 4 are true. Statement 3 is excluded because Heparin is primarily produced by MAST CELLS and basophils (not mainly by liver). "
        "True liver functions: 1. Bile (not enzyme, but bile juice) production ✓; 2. Fibrinogen synthesis ✓ (clotting factor I); 4. Alcohol metabolism/liver damage (cirrhosis) ✓. "
        "Statement 3 (Heparin from liver) is debated — liver produces some heparin but not the primary source. "
        "కాలేయం: పైత్యరసం స్రవిస్తుంది ✓; ఫైబ్రినోజెన్ తయారుచేస్తుంది ✓; మద్యపానంతో దెబ్బతింటుంది ✓. హెపారిన్ ప్రధానంగా మాస్ట్ కణాలు/బేసోఫిల్లు ఉత్పత్తి చేస్తాయి (కాలేయం కాదు).",
        30
    ),
    # Q31
    (
        "The main constituent of hemoglobin is\nతెలుగు: హిమోగ్లోబిన్‌లో ఉండే ప్రధాన అంశం ఏది?",
        "Iron / ఇనుము",
        "Magnesium / మెగ్నీషియం",
        "Calcium / కాల్షియం",
        "Chlorine / క్లోరిన్",
        "A", "E",
        "Hemoglobin (Hb) = iron-containing metalloprotein in RBCs that carries oxygen. Structure: 4 globin chains + 4 HEME groups. "
        "Each HEME group contains one Fe²⁺ (ferrous iron) ion that binds one O₂ molecule. "
        "1 Hb molecule carries 4 O₂ molecules. Normal Hb: Males ~13.5–17.5 g/dL; Females ~12–15.5 g/dL. Iron deficiency → Anemia. "
        "హిమోగ్లోబిన్: 4 గ్లోబిన్ గొలుసులు + 4 హీమ్ సమూహాలు; ప్రతి హీమ్‌లో Fe²⁺ అయాన్ ఒక O₂ ను బంధిస్తుంది. ఇనుము లోపం → రక్తహీనత (anemia).",
        31
    ),
    # Q32
    (
        "The maximum temperature the human skin can tolerate without getting blisters is\nతెలుగు: పొక్కులు (blisters) రాకుండా మానవ చర్మం తట్టుకోగల గరిష్ట ఉష్ణోగ్రత ఎంత?",
        "40°C / 40°C",
        "60°C / 60°C",
        "80°C / 80°C",
        "100°C / 100°C",
        "B", "E",
        "Human skin can tolerate up to approximately 60°C without getting blisters (as per standard exam sources). Above 60°C → protein denaturation in skin → tissue damage → blisters/burns. "
        "Note: Normal body temp = 37°C; Fever = >37.5°C; Heat stroke = >40°C (dangerous). "
        "మానవ చర్మం పొక్కులు లేకుండా ~60°C వరకు తట్టుకుంటుంది (పరీక్ష ప్రమాణం). 60°C పైన ప్రోటీన్ denaturation → కణజాల నష్టం → పొక్కులు/కాలిన గాయాలు.",
        32
    ),
    # Q33
    (
        "Temperature in human beings is controlled by\nతెలుగు: మానవులలో ఉష్ణోగ్రత దేని ద్వారా నియంత్రించబడుతుంది?",
        "Pituitary gland / పిట్యూటరీ గ్రంథి",
        "Adrenal gland / అడ్రినల్ గ్రంథి",
        "Thyroid gland / థైరాయిడ్ గ్రంథి",
        "Hypothalamus gland / హైపోథాలమస్ గ్రంథి",
        "D", "E",
        "HYPOTHALAMUS = thermoregulation center (body's thermostat). Maintains body temperature at 37°C. "
        "When hot: signals sweat glands to produce sweat (evaporation cools), dilates skin blood vessels. "
        "When cold: signals shivering (generates heat), constricts blood vessels. "
        "Note: The option says 'Hypothalamus gland' — Hypothalamus is technically a brain region (part of diencephalon), not a true gland, but exam options use this term. "
        "Hypothalamus also controls: hunger, thirst, sleep, circadian rhythms, and hormonal regulation (controls pituitary). "
        "హైపోథాలమస్ = శరీర ఉష్ణోగ్రత నియంత్రణ కేంద్రం (thermostat); 37°C నిర్వహిస్తుంది. (నోట్: హైపోథాలమస్ మెదడులో భాగం, గ్రంథి కాదు; పరీక్ష ప్రశ్నలో 'gland' అని పేర్కొంటారు.)",
        33
    ),
    # Q34
    (
        "How many teeth are known as milk teeth in human beings?\nతెలుగు: మనుషులలో పాల దంతాలు (milk teeth) అని ఎన్ని దంతాలను పిలుస్తారు?",
        "4 / 4",
        "12 / 12",
        "20 / 20",
        "28 / 28",
        "C", "E",
        "MILK TEETH (Deciduous/Primary teeth) = 20 in humans (10 upper + 10 lower): 4 incisors + 2 canines + 4 molars per jaw = 20 total. "
        "Appear from 6 months to 2 years; shed by age 12. Replaced by PERMANENT (secondary) teeth. "
        "PERMANENT teeth = 32 (including 4 wisdom teeth) or 28 (without wisdom teeth). "
        "పాల దంతాలు (Deciduous teeth) = 20 (పై 10 + కింది 10); 6 నెలల నుండి 2 సంవత్సరాల వయసులో వస్తాయి; 12 సంవత్సరాల వయసులో పడిపోతాయి. శాశ్వత దంతాలు = 32.",
        34
    ),
    # Q35
    (
        "In which part are carbohydrates stored as glycogen in the human body?\nతెలుగు: మానవ శరీరంలో కార్బోహైడ్రేట్లు గ్లైకోజెన్‌గా ఏ భాగంలో నిల్వ చేయబడతాయి?",
        "Stomach / జీర్ణాశయం",
        "Pancreas / క్లోమం",
        "Liver / కాలేయం",
        "Duodenum / డ్యూయోడెనమ్",
        "C", "M",
        "GLYCOGEN (animal starch) is stored primarily in: 1. LIVER (hepatic glycogen — released when blood glucose falls); 2. SKELETAL MUSCLES (muscle glycogen — used for muscle contraction). "
        "Liver glycogen → maintains blood glucose levels. Muscle glycogen → fuel for exercise. "
        "Insulin stimulates glycogen synthesis (glycogenesis); Glucagon stimulates glycogen breakdown (glycogenolysis). "
        "గ్లైకోజెన్ నిల్వ: ప్రధానంగా కాలేయంలో + అస్థి కండరాలలో. ఇన్సులిన్ → గ్లైకోజెన్ తయారీని ప్రేరేపిస్తుంది; గ్లుకగాన్ → గ్లైకోజెన్ విచ్ఛిన్నాన్ని ప్రేరేపిస్తుంది.",
        35
    ),
    # Q36
    (
        "Which of the following is connected with blood pressure?\nతెలుగు: కింది వాటిలో రక్తపోటుకు సంబంధించినది ఏది?",
        "Liver / కాలేయం",
        "Testis / ముష్కాలు",
        "Pancreas / క్లోమం",
        "Adrenal / అడ్రినల్",
        "D", "E",
        "ADRENAL GLAND regulates blood pressure via two pathways: "
        "Adrenal medulla → Epinephrine/Norepinephrine (adrenaline) → increases heart rate and BP in fight-or-flight response. "
        "Adrenal cortex → Aldosterone (mineralocorticoid) → increases Na⁺ and water reabsorption in kidneys → increases blood volume → increases BP. "
        "అడ్రినల్ గ్రంథి: అడ్రినలిన్ + నోరడ్రినలిన్ → BP, హృదయ స్పందన పెరుగుతాయి; అల్డోస్టిరాన్ → సోడియం నిలుపుదల → BP పెరుగుతుంది.",
        36
    ),
    # Q37
    (
        "Blood does not clot in the absence of Vitamin K because it is:\nతెలుగు: విటమిన్ K లేనప్పుడు రక్తం గడ్డకట్టదు, ఎందుకంటే ఇది:",
        "Essential for synthesis of prothrombin / ప్రోథ్రాంబిన్ సంశ్లేషణకు అవసరం",
        "Essential for synthesis of fibrinogen / ఫైబ్రినోజెన్ సంశ్లేషణకు అవసరం",
        "An essential component of the clot / గడ్డకట్టడంలో ఒక ముఖ్యమైన భాగం",
        "An essential component of the platelets / ఫలకికలలో ఒక ముఖ్యమైన భాగం",
        "A", "M",
        "VITAMIN K = fat-soluble vitamin essential for synthesis of clotting factors: II (Prothrombin), VII, IX, X. "
        "Prothrombin → Thrombin (activated by thromboplastin + Ca²⁺) → Fibrinogen → Fibrin clot. "
        "Vitamin K deficiency → inadequate prothrombin → blood cannot clot → hemorrhage. "
        "Anticoagulant Warfarin = Vitamin K antagonist. Newborns given Vitamin K injection at birth (insufficient gut bacteria). "
        "విటమిన్ K: ప్రోథ్రాంబిన్ (Factor II), VII, IX, X సంశ్లేషణకు అవసరం. విటమిన్ K లోపం → ప్రోథ్రాంబిన్ తగ్గుతుంది → రక్తం గడ్డకట్టదు. వార్ఫారిన్ = విటమిన్ K ప్రత్యర్థి.",
        37
    ),
    # Q38
    (
        "Which of the following is known as the 'graveyard of RBCs'?\nతెలుగు: కింది వాటిలో దేనిని 'RBC ల స్మశానవాటిక' (graveyard of RBCs) అని పిలుస్తారు?",
        "Liver / కాలేయం",
        "Bone marrow / ఎముక మజ్జ",
        "Spleen / ప్లీహం",
        "Appendix / అపెండిక్స్",
        "C", "E",
        "SPLEEN = 'graveyard of RBCs'. Old/damaged RBCs (after 120-day lifespan) are destroyed by macrophages in the spleen. "
        "Hemoglobin is broken down: heme → bilirubin (excreted in bile → gives yellow colour to faeces/urine); iron → recycled via transferrin → bone marrow. "
        "Spleen also: filters blood, stores platelets, produces lymphocytes (WBCs), site of immune response. "
        "ప్లీహం = 'RBC ల స్మశానవాటిక'; పాత RBC లను (120 రోజుల తర్వాత) నాశనం చేస్తుంది; హిమోగ్లోబిన్ → బిలిరుబిన్ (పైత్యరసంలో విసర్జన) + ఇనుము (పునర్వినియోగం).",
        38
    ),
    # Q39
    (
        "The proportion of red blood corpuscles and white blood corpuscles in the human body is:\nతెలుగు: మానవ శరీరంలో ఎర్ర రక్త కణాలు మరియు తెల్ల రక్త కణాల నిష్పత్తి:",
        "5:1 / 5:1",
        "50:1 / 50:1",
        "500:1 / 500:1",
        "5000:1 / 5000:1",
        "D", "H",
        "⚠ Exam key: (d) 5000:1. Scientific normal ratio: RBC (~5 million/mm³) : WBC (~5,000–10,000/mm³) ≈ 500:1 to 1000:1 (approximately 600:1). "
        "The ratio varies: at 5 million RBC and 10,000 WBC → 500:1; at 5 million RBC and 5,000 WBC → 1000:1. "
        "5000:1 is higher than typical physiological values. Follow exam key (d) for exam. "
        "⚠ పరీక్ష కీ: (d) 5000:1. శాస్త్రీయంగా: RBC ~500 మందికి WBC 1 నిష్పత్తి (~600:1). పరీక్షలో (d) అనుసరించండి.",
        39
    ),
    # Q40
    (
        "In mammals, the sequence of bones from shoulder to fingertips is:\nతెలుగు: క్షీరదాలలో, భుజం నుండి వేలికొనల వరకు ఉండే ఎముకల క్రమం ఏది?",
        "Humerus, radius-ulna, carpals, metacarpals, phalanges / హ్యూమరస్, రేడియస్-ఉల్నా, కార్పెల్స్, మెటాకార్పెల్స్, ఫాలాంజెస్",
        "Humerus, metacarpals, carpals, radius-ulna, phalanges / హ్యూమరస్, మెటాకార్పెల్స్, కార్పెల్స్, రేడియస్-ఉల్నా, ఫాలాంజెస్",
        "Radius-ulna, humerus, metacarpals, carpals, phalanges / రేడియస్-ఉల్నా, హ్యూమరస్, మెటాకార్పెల్స్, కార్పెల్స్, ఫాలాంజెస్",
        "Humerus, radius-ulna, metacarpals, carpals, phalanges / హ్యూమరస్, రేడియస్-ఉల్నా, మెటాకార్పెల్స్, కార్పెల్స్, ఫాలాంజెస్",
        "A", "M",
        "Arm bone sequence (shoulder to fingertips): HUMERUS (upper arm) → RADIUS + ULNA (forearm) → CARPALS (wrist, 8 bones) → METACARPALS (palm, 5 bones) → PHALANGES (fingers, 14 bones). "
        "Memory trick: Humerus, Radius-Ulna, Carpals, Metacarpals, Phalanges = 'HURCMP' or 'Humming RC Makes People' "
        "భుజం నుండి వేళ్ళ వరకు: హ్యూమరస్ (పై చేయి) → రేడియస్+ఉల్నా (ముంచేయి) → కార్పెల్స్ (మణికట్టు) → మెటాకార్పెల్స్ (అరచేయి) → ఫాలాంజెస్ (వేళ్ళు).",
        40
    ),
    # Q41
    (
        "Which of the following metal ion is present in haemoglobin?\nతెలుగు: కింది వాటిలో హిమోగ్లోబిన్‌లో ఉండే లోహపు అయాన్ ఏది?",
        "Zinc / జింక్",
        "Iron / ఇనుము",
        "Copper / రాగి",
        "Magnesium / మెగ్నీషియం",
        "B", "E",
        "Hemoglobin contains IRON (Fe²⁺ — ferrous ion) in its heme group. Iron binds O₂ reversibly → Oxyhemoglobin (HbO₂) in lungs; releases O₂ in tissues. "
        "Compare: Chlorophyll contains MAGNESIUM (Mg²⁺). Hemocyanin (in molluscs/arthropods) contains COPPER (Cu²⁺). "
        "Iron-deficiency → less hemoglobin → anemia → fatigue, pale skin, shortness of breath. "
        "హిమోగ్లోబిన్: హీమ్ సమూహంలో Fe²⁺ (ఫెర్రస్ అయాన్) ఉంటుంది. క్లోరోఫిల్ = Mg²⁺; హిమోసయానిన్ = Cu²⁺. ఇనుము లోపం → రక్తహీనత.",
        41
    ),
    # Q42
    (
        "Retina in the eyes acts as a:\nతెలుగు: కళ్ళలోని రెటీనా దేనిలా పనిచేస్తుంది?",
        "Lens in the camera / కెమెరాలోని కటకం",
        "Shutter in the camera / కెమెరాలోని షట్టర్",
        "Film in the camera / కెమెరాలోని ఫిల్మ్",
        "None of these / ఇవేవీ కావు",
        "C", "M",
        "EYE ↔ CAMERA analogy: Retina = FILM (detects light and forms image) | Lens = Lens | Iris/Pupil = Aperture/Shutter | Cornea = front lens. "
        "RETINA = innermost layer of eye; contains photoreceptors: RODS (dim light/black-white) and CONES (colour vision, 3 types: red, green, blue). "
        "Image forms on retina → electrical signals → optic nerve → brain (occipital cortex). "
        "రెటీనా = కెమెరాలో ఫిల్మ్ లాంటిది; రాడ్లు (మసక వెలుతురు) + కోన్లు (రంగు దృష్టి) ఉంటాయి; ప్రతిబింబం → విద్యుత్ సంకేతాలు → మెదడుకు.",
        42
    ),
    # Q43
    (
        "The largest part of the human brain is:\nతెలుగు: మానవ మెదడులో అతిపెద్ద భాగం ఏది?",
        "Cerebellum / సెరిబెల్లమ్ (అనుమస్తిష్కం)",
        "Cerebrum / సెరిబ్రమ్ (మస్తిష్కం)",
        "Medulla oblongata / మెడుల్లా అబ్లాంగేటా (మజ్జాముఖం)",
        "Pons / పాన్స్",
        "B", "E",
        "CEREBRUM = largest part of human brain (~85% of total brain weight). Divided into two hemispheres; surface = cerebral cortex (grey matter). "
        "Functions: Intelligence, memory, voluntary movements, language, reasoning, sensory processing. "
        "Cerebellum = second largest (~10%); balance and coordination. Medulla oblongata = vital reflexes (breathing, heartbeat). "
        "సెరిబ్రమ్ = మానవ మెదడులో అతిపెద్ద భాగం (~85%); రెండు అర్ధగోళాలు; బుద్ధి, జ్ఞాపకం, ఐచ్ఛిక చర్యలు. సెరిబెల్లమ్ = సమతుల్యత (2వ పెద్ద భాగం).",
        43
    ),
    # Q44
    (
        "Iron is present in the blood in the form of a\nతెలుగు: రక్తంలో ఇనుము ఏ రూపంలో ఉంటుంది?",
        "free salt / స్వేచ్ఛా లవణం",
        "compound / సమ్మేళనం",
        "mixture / మిశ్రమం",
        "complex / సంక్లిష్టం",
        "B", "H",
        "⚠ Exam key: (b) compound. Scientifically: Iron in blood is present as a COMPLEX (metalloprotein complex) in HEMOGLOBIN. "
        "Heme = iron-porphyrin complex (Fe²⁺ coordinated in porphyrin ring); Hemoglobin = 4 heme groups + 4 globin polypeptides = metalloprotin/complex. "
        "For exam purposes, follow answer key (b) compound. "
        "⚠ పరీక్ష కీ: (b) సమ్మేళనం (compound). శాస్త్రీయంగా: ఇనుము హిమోగ్లోబిన్‌లో 'సంక్లిష్టం' (complex/metalloprotein) రూపంలో ఉంటుంది. పరీక్షలో (b).",
        44
    ),
    # Q45
    (
        "The glands of the body which pour their secretions directly into the blood stream are known as\nతెలుగు: తమ స్రావాలను నేరుగా రక్తప్రవాహంలోకి విడుదల చేసే శరీరంలోని గ్రంథులను ఏమంటారు?",
        "Exocrine glands / ఎక్సోక్రైన్ గ్రంథులు",
        "Endocrine glands / ఎండోక్రైన్ గ్రంథులు",
        "Heterocrine glands / హెటెరోక్రైన్ గ్రంథులు",
        "Compound glands / కాంపౌండ్ గ్రంథులు",
        "B", "E",
        "ENDOCRINE GLANDS (ductless glands) = pour secretions (hormones) DIRECTLY into the bloodstream → carried to target organs. "
        "Examples: Pituitary, Thyroid, Parathyroid, Adrenal, Pancreas (islets), Pineal, Gonads. "
        "EXOCRINE GLANDS = have ducts; secrete onto body surfaces or into body cavities. Examples: Salivary, sweat, sebaceous, pancreas (digestive enzymes). "
        "MIXED (Heterocrine): Pancreas = both exocrine (digestive enzymes via duct) and endocrine (insulin/glucagon into blood). "
        "ఎండోక్రైన్ గ్రంథులు = నాళాలు లేకుండా నేరుగా రక్తప్రవాహంలోకి హార్మోన్లు విడుదల చేస్తాయి. ఎక్సోక్రైన్ = నాళాల ద్వారా విడుదల. క్లోమం = రెండూ.",
        45
    ),
    # Q46
    (
        "If father and mother are possessing Rh+ve and Rh-ve respectively, their children will have the blood group\nతెలుగు: తండ్రి మరియు తల్లికి వరుసగా Rh+ve మరియు Rh-ve రక్తపు గ్రూపులు ఉంటే, వారి పిల్లలకు ఏ రక్తపు గ్రూపు ఉంటుంది?",
        "Rh+ve / Rh+ve",
        "Rh-ve / Rh-ve",
        "Rh neutral / Rh తటస్థ",
        "None of these / ఇవేవీ కావు",
        "A", "M",
        "Rh factor (D antigen) is dominant. If Father = Rh+ (dominant, could be RR or Rr) × Mother = Rh- (rr). "
        "If father is homozygous (RR): all children = Rr = Rh+ (100% Rh+). If father is heterozygous (Rr): children = Rr (Rh+) or rr (Rh-) — 50:50. "
        "Exam answer = (a) Rh+ve (assuming dominant Rh+ trait from father prevails). "
        "Rh incompatibility in pregnancy: Rh- mother + Rh+ foetus → erythroblastosis fetalis (haemolytic disease of newborn) in subsequent pregnancies. "
        "Rh ఫ్యాక్టర్ (D యాంటీజెన్) డామినెంట్. తండ్రి Rh+ (RR అనుకుంటే) × తల్లి Rh- (rr) → పిల్లలు Rh+ (Rr). పరీక్ష సమాధానం (a).",
        46
    ),
    # Q47
    (
        "The radio active element used in heart pacemakers is\nతెలుగు: హార్ట్ పేస్‌మేకర్‌లలో ఉపయోగించే రేడియోధార్మిక మూలకం ఏది?",
        "Uranium / యురేనియం",
        "Deuterium / డ్యుటీరియం",
        "Plutonium / ప్లూటోనియం",
        "Radium / రేడియం",
        "C", "H",
        "PLUTONIUM-238 (Pu-238) was used in nuclear-powered pacemakers (1970s–1980s). Pu-238 has long half-life (~87.7 years) → provided power for ~10+ years. "
        "Modern pacemakers use lithium-iodide batteries (not radioactive). "
        "Note: Deuterium is an isotope of hydrogen (H-2), NOT radioactive in the traditional sense. Pacemaker role: sends electrical pulses to maintain heart rate. "
        "ప్లూటోనియం-238: గతంలో (1970-80లు) న్యూక్లియర్ పేస్‌మేకర్లలో వాడేవారు; అర్ధజీవితం ~87.7 సంవత్సరాలు. ఆధునిక పేస్‌మేకర్లు లిథియం-అయోడైడ్ బ్యాటరీలు వాడతాయి.",
        47
    ),
    # Q48
    (
        "Which of the following makes skin layer impervious to water?\nతెలుగు: కింది వాటిలో చర్మపు పొరను నీరు చొరబడని విధంగా చేసేది ఏది?",
        "Collagen / కొల్లాజెన్",
        "Melanin / మెలనిన్",
        "Keratin / కెరాటిన్",
        "Chitin / కైటిన్",
        "C", "E",
        "KERATIN = tough, fibrous structural protein in skin (epidermis), hair, and nails. Makes the outer skin layer (stratum corneum) waterproof and impervious to water. "
        "Also in: hair, nails, claws, horns, feathers, hooves (α-keratin). "
        "Collagen = structural protein in connective tissue, tendons, bone (NOT waterproofing). Melanin = pigment (skin color, UV protection). Chitin = structural polysaccharide in insect exoskeletons. "
        "కెరాటిన్ = చర్మం, జుట్టు, గోళ్ళలోని ఫైబరస్ ప్రోటీన్; బాహ్య చర్మపొరను (stratum corneum) నీటికి చొరబడకుండా చేస్తుంది. మెలనిన్ = వర్ణద్రవ్యం (చర్మపు రంగు, UV రక్షణ).",
        48
    ),
    # Q49
    (
        "The ligaments join\nతెలుగు: స్నాయువులు (Ligaments) వేటిని కలుపుతాయి?",
        "muscle to muscle / కండరాన్ని కండరానికి",
        "bone to bone / ఎముకను ఎముకకు",
        "muscle to bone / కండరాన్ని ఎముకకు",
        "None of these / ఇవేవీ కావు",
        "B", "E",
        "LIGAMENTS = dense fibrous connective tissue that joins BONE to BONE at joints. Made of collagen fibres; provide stability to joints. "
        "TENDONS = join MUSCLE to BONE (e.g., Achilles tendon connects calf muscle to heel bone). "
        "Memory: Ligament = bond between bones (L for links); Tendon = connects to bone (T for tethers). "
        "కీళ్ళ దగ్గర ఎముకలను ఎముకలకు కలిపేవి స్నాయువులు (Ligaments). కండరాలను ఎముకలకు కలిపేవి అనుకూపాలు (Tendons). గుర్తు: L = links bones; T = tethers muscle.",
        49
    ),
    # Q50
    (
        "Which of the following is produced during allergic reactions?\nతెలుగు: అలెర్జీ ప్రతిచర్యల (allergic reactions) సమయంలో ఉత్పత్తి అయ్యేది ఏది?",
        "Heparin / హెపారిన్",
        "Histamine / హిస్టామిన్",
        "Serotonin / సెరోటోనిన్",
        "Selastamine / సెలాస్టమైన్",
        "B", "E",
        "HISTAMINE = released from MAST CELLS and BASOPHILS during ALLERGIC reactions. Causes: vasodilation, increased vascular permeability, itching, sneezing, watery eyes, bronchoconstriction. "
        "Antihistamines (e.g., cetirizine, loratadine) block histamine receptors → relieve allergy symptoms. "
        "Note: Heparin is also released from mast cells but is an anticoagulant (not primary in allergy); Serotonin = neurotransmitter; Selastamine = antihistamine drug. "
        "హిస్టామిన్: మాస్ట్ కణాలు మరియు బేసోఫిల్లు అలెర్జీ ప్రతిచర్యలలో విడుదల చేస్తాయి; దురద, తుమ్ములు, నీళ్ళ కళ్ళు, బ్రాంకోకాన్‌స్ట్రిక్షన్ కలిగిస్తుంది. యాంటీహిస్టమిన్‌లు లక్షణాలను తగ్గిస్తాయి.",
        50
    ),
]

def seed():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("DELETE FROM questions WHERE source_file=?", (SOURCE,))
    cur.executemany(
        """INSERT INTO questions
           (folder, topic, source_file, question_text,
            option_a, option_b, option_c, option_d,
            correct_answer, difficulty, explanation, question_order)
           VALUES ('GK','General_Science',?,?,?,?,?,?,?,?,?,?)""",
        [(SOURCE, *q) for q in questions]
    )
    con.commit()
    n = cur.execute("SELECT COUNT(*) FROM questions WHERE source_file=?", (SOURCE,)).fetchone()[0]
    total = cur.execute("SELECT COUNT(*) FROM questions WHERE topic='General_Science'").fetchone()[0]
    con.close()
    print(f"✓ Inserted {n} questions from {SOURCE}")
    print(f"✓ Total General_Science questions in DB: {total}")

if __name__ == '__main__':
    seed()
