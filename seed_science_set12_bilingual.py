import sqlite3, os

SOURCE = 'Science_Set12_Human_System3'
DB = os.path.join(os.path.dirname(__file__), 'mnt/mcq_app/database.db')

questions = [
    # Q1
    (
        "Which of the following is not a bone in the human body?\nతెలుగు: మానవ శరీరంలో ఎముక కానిది కింది వాటిలో ఏది?",
        "Sternum / స్టెర్నమ్ (ఉరోస్థి)",
        "Humerus / హ్యూమరస్",
        "Pericardium / పెరికార్డియం (హృదయావరణం)",
        "Tibia / టిబియా",
        "C", "E",
        "PERICARDIUM = double-layered membranous sac that surrounds and protects the HEART — it is NOT a bone. "
        "Sternum = breastbone (flat bone protecting thorax); Humerus = upper arm bone; Tibia = shinbone (lower leg). "
        "Note: Q1 and Q13 are complementary — Q1 establishes Pericardium is NOT a bone; Q13 identifies it as the membrane covering the heart. "
        "పెరికార్డియం = గుండె చుట్టూ ఉండే రెండు పొరల పదార్థ సంచి; ఇది ఎముక కాదు. స్టెర్నమ్/హ్యూమరస్/టిబియా = అన్నీ ఎముకలే.",
        1
    ),
    # Q2
    (
        "A round worm that enters man's body through the soles of the feet is\nతెలుగు: పాదాల అరికాళ్ళ ద్వారా మనిషి శరీరంలోకి ప్రవేశించే గుండ్రటి పురుగు (రౌండ్‌వార్మ్) ఏది?",
        "Leech / జలగ",
        "Hookworm / హుక్‌వార్మ్",
        "Tapeworm / బద్దెపురుగు",
        "Trichina / ట్రికినా",
        "B", "E",
        "HOOKWORM (Ancylostoma duodenale / Necator americanus) = enters human body by PENETRATING the skin of soles of bare feet (filariform larvae in soil). "
        "Route: Soil → skin (feet) → bloodstream → lungs → trachea → swallowed → small intestine (adult worm). "
        "Leech = attaches externally to skin (NOT a roundworm). Tapeworm = ingested via undercooked meat. Trichina = ingested via undercooked pork. "
        "హుక్‌వార్మ్: అరికాళ్ళ చర్మం ద్వారా (నేల నుండి) శరీరంలోకి ప్రవేశిస్తుంది → రక్తం → ఊపిరితిత్తులు → మింగబడి → చిన్న ప్రేగులో నివసిస్తుంది.",
        2
    ),
    # Q3
    (
        "The enzymes involved in the digestion of fats and proteins are\nతెలుగు: కొవ్వులు మరియు ప్రోటీన్ల జీర్ణక్రియలో పాల్గొనే ఎంజైమ్‌లు ఏవి?",
        "Trypsin and ptyalin / ట్రిప్సిన్ మరియు టయలిన్",
        "Pepsin and lipase / పెప్సిన్ మరియు లైపేజ్",
        "Erypsin and trypsin / ఎరిప్సిన్ మరియు ట్రిప్సిన్",
        "Erypsin and ptyalin / ఎరిప్సిన్ మరియు టయలిన్",
        "B", "M",
        "PEPSIN = protein-digesting enzyme (stomach, activated by HCl); LIPASE = fat-digesting enzyme (pancreas → small intestine). "
        "Together they cover PROTEINS + FATS digestion. "
        "Other enzymes: Ptyalin (Salivary Amylase) = STARCH; Trypsin = protein (small intestine, from pancreas); Erypsin = peptidase (small intestine, final protein breakdown). "
        "పెప్సిన్ = ప్రోటీన్ జీర్ణం (జీర్ణాశయం); లైపేజ్ = కొవ్వు జీర్ణం (క్లోమం → చిన్న ప్రేగు). టయలిన్ = పిండి పదార్థాలు; ట్రిప్సిన్ = ప్రోటీన్ (చిన్న ప్రేగు).",
        3
    ),
    # Q4
    (
        "What should be the minimum interval between two successive blood donations?\nతెలుగు: రెండు వరుస రక్తదానాల మధ్య కనీస విరామం ఎంత ఉండాలి?",
        "6 weeks / 6 వారాలు",
        "3 months / 3 నెలలు",
        "6 months / 6 నెలలు",
        "8 months / 8 నెలలు",
        "B", "E",
        "Minimum interval between blood donations = 3 MONTHS (approximately 12–16 weeks / 56+ days as per WHO/Indian guidelines for whole blood). "
        "Rationale: RBCs take ~120 days to regenerate; after donation, blood volume recovers in 24–48 hrs; iron stores take 8–12 weeks; plasma recovers in 24 hrs. "
        "Blood volume donated = approximately 350–450 mL per donation. "
        "రక్తదానాల మధ్య కనీస విరామం = 3 నెలలు (~12-16 వారాలు); RBC లు పూర్తిగా తిరిగి తయారవడానికి ~120 రోజులు పడుతుంది.",
        4
    ),
    # Q5
    (
        "In a normal human being, food takes about ....... hours to reach the end of the intestine for complete absorption.\nతెలుగు: సాధారణ మానవునిలో, ఆహారం పూర్తిగా శోషించబడటానికి ప్రేగు చివరకు చేరుకోవడానికి సుమారు ఎన్ని గంటల సమయం పడుతుంది?",
        "4 / 4 గంటలు",
        "8 / 8 గంటలు",
        "12 / 12 గంటలు",
        "16 / 16 గంటలు",
        "C", "E",
        "Food transit time for complete intestinal absorption ≈ 12 HOURS (in the small intestine where 90% of absorption occurs). "
        "Full GI transit breakdown: Mouth → Stomach = 2–4 hrs; Small intestine absorption = 4–8 hrs (total ~12 hrs from eating); Large intestine = 10–59 hrs. "
        "Small intestine = ~6–7 m long; where proteins, fats, carbohydrates, vitamins, and minerals are absorbed. "
        "సాధారణ మానవునిలో ఆహారం పూర్తి శోషణకు ~12 గంటలు (చిన్న ప్రేగులో); మొత్తం GI transit = 24-72 గంటలు.",
        5
    ),
    # Q6
    (
        "The gland that directly regulates the rate of metabolism is the\nతెలుగు: జీవక్రియ రేటును (metabolism) ప్రత్యక్షంగా నియంత్రించే గ్రంథి ఏది?",
        "Pituitary / పిట్యూటరీ",
        "Thymus / థైమస్",
        "Thyroid / థైరాయిడ్",
        "Parathyroid / పారాథైరాయిడ్",
        "C", "M",
        "THYROID GLAND directly regulates the METABOLIC RATE via hormones T3 (Triiodothyronine) and T4 (Thyroxine). "
        "T3/T4 increase basal metabolic rate (BMR) — speed of energy use in cells. "
        "Hypothyroidism (low T3/T4) → slow metabolism, weight gain, fatigue, goiter. Hyperthyroidism → high metabolism, weight loss, rapid heartbeat. "
        "Pituitary controls thyroid INDIRECTLY via TSH (Thyroid Stimulating Hormone). Parathyroid → calcium regulation. Thymus → immunity/T-cells. "
        "థైరాయిడ్: T3 మరియు T4 హార్మోన్ల ద్వారా జీవక్రియ రేటు (BMR) నేరుగా నియంత్రిస్తుంది. హైపోథైరాయిడిజం → బరువు పెరగడం; హైపర్‌థైరాయిడిజం → బరువు తగ్గడం.",
        6
    ),
    # Q7
    (
        "According to the induced-fit model of enzyme action, substrate binding\nతెలుగు: ఎంజైమ్ చర్య యొక్క ఇండ్యూస్డ్-ఫిట్ మోడల్ (induced-fit model) ప్రకారం, సబ్‌స్ట్రేట్ బంధం:",
        "Induces a conformational change that optimises the active site for catalysis / ఉత్ప్రేరణ కోసం క్రియాశీల సైట్‌ను ఆప్టిమైజ్ చేసే నిర్మాణ మార్పును ప్రేరేపిస్తుంది",
        "Inhibits the enzyme by permanently altering its structure / ఎంజైమ్ నిర్మాణాన్ని శాశ్వతంగా మార్చడం ద్వారా దానిని నిరోధిస్తుంది",
        "Occurs without any change to the enzyme's active site / ఎంజైమ్ యొక్క క్రియాశీల సైట్‌లో ఎలాంటి మార్పు లేకుండా జరుగుతుంది",
        "Leads to immediate release of the substrate without transformation / రూపాంతరం లేకుండా సబ్‌స్ట్రేట్‌ను వెంటనే విడుదల చేయడానికి దారితీస్తుంది",
        "A", "H",
        "INDUCED-FIT MODEL (Daniel Koshland, 1958): Substrate binding INDUCES a CONFORMATIONAL CHANGE in the enzyme's active site → optimises fit for catalysis (like a hand fitting into a glove). "
        "Contrasts with LOCK-AND-KEY MODEL (Emil Fischer, 1890): rigid active site; substrate fits exactly (like key in lock). "
        "Induced-fit explains: enzyme specificity, allosteric regulation, and why similar substrates have different reaction rates. "
        "After reaction: enzyme returns to original shape (NOT permanently altered). "
        "ఇండ్యూస్డ్-ఫిట్ మోడల్ (Koshland 1958): సబ్‌స్ట్రేట్ ఎంజైమ్ క్రియాశీల సైట్‌లో నిర్మాణ మార్పు కలిగిస్తుంది (చేయి + గ్లోవ్ వలె). Lock-and-key = Fischer (1890), దృఢమైన సైట్.",
        7
    ),
    # Q8
    (
        "Duodenum is situated\nతెలుగు: డ్యూయోడెనమ్ (ఆంత్రమూలం) ఎక్కడ ఉంటుంది?",
        "At the uppermost part of the small intestine / చిన్న ప్రేగు యొక్క పైభాగంలో",
        "Near the lungs / ఊపిరితిత్తుల దగ్గర",
        "In the brain / మెదడులో",
        "At the tail end of the intestine / ప్రేగు చివరి భాగంలో",
        "A", "E",
        "DUODENUM = first and UPPERMOST part of the small intestine (about 25–30 cm / 12 finger-widths long — 'duodenum' means 'twelve' in Latin). "
        "Connects stomach (via pyloric sphincter) to jejunum. Receives: Bile (from liver/gallbladder) and Pancreatic juice → neutralizes acidic chyme from stomach. "
        "Small intestine sequence: Duodenum → Jejunum → Ileum. Most digestion and some absorption occurs in duodenum. "
        "డ్యూయోడెనమ్ = చిన్న ప్రేగు యొక్క మొదటి భాగం (~25-30 cm); జీర్ణాశయం నుండి పైత్యరసం + క్లోమ రసాన్ని స్వీకరిస్తుంది; ఆమ్ల chyme ను నిర్వీర్యం చేస్తుంది.",
        8
    ),
    # Q9
    (
        "Only glucose is used for energy requirement by\nతెలుగు: శక్తి అవసరాల కోసం గ్లూకోజ్‌ను మాత్రమే ఉపయోగించుకునేది ఏది?",
        "Kidney / మూత్రపిండం",
        "Muscles / కండరాలు",
        "Brain / మెదడు",
        "Liver / కాలేయం",
        "C", "M",
        "BRAIN uses ONLY GLUCOSE as its energy source (under normal conditions). "
        "Reason: Fatty acids CANNOT cross the blood-brain barrier (BBB); only glucose (and ketone bodies in starvation) can enter brain cells. "
        "Brain glucose needs: ~120 g/day (~20% of total body glucose despite being only 2% of body weight). "
        "In starvation: Brain adapts to use KETONE BODIES (from fat breakdown), but glucose remains primary. Kidneys, muscles, liver = can use fatty acids, amino acids, and glucose. "
        "మెదడు శక్తి కోసం గ్లూకోజ్‌ను మాత్రమే వాడుతుంది (BBB కారణంగా కొవ్వు ఆమ్లాలు వెళ్ళలేవు); ~120 g/day అవసరం. పస్తు పరిస్థితిలో: కీటోన్ బాడీలు వాడతాయి.",
        9
    ),
    # Q10
    (
        "Dental formula of man is\nతెలుగు: మానవుని దంత సూత్రం (Dental formula):",
        "1232/1232",
        "2123/2123",
        "2132/2132",
        "2023/2023",
        "B", "M",
        "Human dental formula = 2123/2123 (per half jaw, upper/lower): "
        "2 Incisors (కుంతకాలు) + 1 Canine (రదనిక) + 2 Premolars (ముందు చార్వణకాలు) + 3 Molars (చార్వణకాలు) = 8 teeth per half jaw × 4 = 32 teeth total. "
        "Formula reads: I(2/2) C(1/1) P(2/2) M(3/3) = 2123/2123. "
        "Milk teeth (deciduous) formula = 2102/2102 = 20 teeth (no premolars, 2 molars). "
        "మానవ దంత సూత్రం = 2123/2123; 2 కుంతకాలు + 1 రదనిక + 2 ముందు చార్వణకాలు + 3 చార్వణకాలు = 8/హాఫ్ జా × 4 = 32 మొత్తం.",
        10
    ),
    # Q11
    (
        "How many pairs of salivary glands are there in human body?\nతెలుగు: మానవ శరీరంలో ఎన్ని జతల లాలాజల గ్రంథులు ఉంటాయి?",
        "1 / 1 జత",
        "2 / 2 జతలు",
        "3 / 3 జతలు",
        "4 / 4 జతలు",
        "C", "E",
        "3 PAIRS of salivary glands (6 glands total): "
        "1. PAROTID glands (largest) — near ear (parotid = 'near ear'); affected in mumps. "
        "2. SUBMANDIBULAR glands — below the jaw; produce mixed saliva (mucous + serous). "
        "3. SUBLINGUAL glands (smallest) — under the tongue; produce mainly mucous saliva. "
        "All secrete saliva containing: Ptyalin (amylase), Mucin, Lysozyme, Water (~99.5%), IgA antibodies. "
        "3 జతల లాలాజల గ్రంథులు: పారోటిడ్ (అతిపెద్ద, చెవి దగ్గర — గవదబిళ్ళలో ప్రభావితం), సబ్‌మాండిబ్యులర్ (దవడ కింద), సబ్‌లింగువల్ (నాలుక కింద, అతిచిన్న).",
        11
    ),
    # Q12
    (
        "Nervous system is affected by the shortage of\nతెలుగు: దేని కొరత వల్ల నాడీ వ్యవస్థ (Nervous system) ప్రభావితమవుతుంది?",
        "Oxygen / ఆక్సిజన్",
        "Sulphur / సల్ఫర్",
        "Carbon / కార్బన్",
        "Sodium / సోడియం",
        "D", "M",
        "SODIUM (Na⁺) deficiency (hyponatremia) directly affects the nervous system. "
        "Na⁺ is essential for: 1. Nerve impulse conduction (action potential via Na⁺/K⁺ pump). 2. Maintaining resting membrane potential (-70 mV). "
        "Hyponatremia → confusion, seizures, headache, coma (in severe cases). "
        "Na⁺/K⁺-ATPase pump: pumps 3 Na⁺ out and 2 K⁺ in per cycle → maintains electrochemical gradient → nerve signals. "
        "సోడియం (Na⁺) లోపం: నాడీ ఆవేగ ప్రసారానికి Na⁺ అవసరం (Na⁺/K⁺ పంప్); లోపం → గందరగోళం, మూర్ఛ. ఆక్సిజన్ కొరత = అన్ని కణాలను ప్రభావితం చేస్తుంది.",
        12
    ),
    # Q13
    (
        "The heart is covered by a membrane called\nతెలుగు: గుండెను కప్పి ఉంచే పొరను ఏమంటారు?",
        "Epidermis / ఎపిడెర్మిస్",
        "Dermis / డెర్మిస్",
        "Epicardium / ఎపికార్డియం",
        "Pericardium / పెరికార్డియం",
        "D", "E",
        "PERICARDIUM = double-layered membranous sac enclosing the heart: Outer = fibrous pericardium (tough, protective); Inner = serous pericardium (2 layers: parietal + visceral). "
        "Visceral layer = EPICARDIUM (outermost layer of heart wall itself). "
        "Pericardial fluid (25–50 mL) between layers = reduces friction during heartbeats. "
        "Inflammation of pericardium = PERICARDITIS. "
        "Epidermis/Dermis = skin layers. "
        "పెరికార్డియం = గుండెను కప్పే రెండు పొరల సంచి; పెరికార్డియల్ ద్రవం (25-50 mL) రాపిడిని తగ్గిస్తుంది. ఎపికార్డియం = గుండె గోడ యొక్క బాహ్య పొర.",
        13
    ),
    # Q14
    (
        "Heart attack occurs due to\nతెలుగు: గుండెపోటు (Heart attack) దేని వల్ల వస్తుంది?",
        "Bacterial attack on the heart / గుండెపై బ్యాక్టీరియా దాడి వల్ల",
        "Stopping of heart beat / గుండె కొట్టుకోవడం ఆగిపోవడం వల్ల",
        "Lack of blood supply to the heart itself / గుండెకు రక్త సరఫరా లేకపోవడం వల్ల",
        "Impairment of heart's working due to unknown reasons / తెలియని కారణాల వల్ల గుండె పనితీరు దెబ్బతినడం వల్ల",
        "C", "M",
        "HEART ATTACK (Myocardial Infarction / MI) = blockage of coronary arteries → NO blood supply to heart muscle → heart muscle cells DIE (infarction). "
        "Coronary arteries = vessels supplying blood TO the heart muscle itself (not blood the heart pumps). "
        "Main cause: Atherosclerosis (plaque buildup in coronary arteries) → thrombosis (clot) → complete blockage. "
        "Symptoms: Chest pain (angina), radiating arm/jaw pain, sweating, shortness of breath. "
        "Note: Cardiac arrest = heart STOPS beating (different from heart attack). "
        "గుండెపోటు (MI): కరోనరీ ధమనులు మూసుకుపోవడం → గుండె కండరానికి రక్తం రాకపోవడం → కండర కణాలు మరణం. అథెరోస్క్లెరోసిస్ = ప్రధాన కారణం.",
        14
    ),
    # Q15
    (
        "Allergy is caused due to\nతెలుగు: అలెర్జీ (Allergy) దేని వల్ల వస్తుంది?",
        "Inflammation of upper respiratory tract / ఎగువ శ్వాసకోశ మార్గం వాపు వల్ల",
        "Inhalation of pollens / పుప్పొడి పీల్చడం వల్ల",
        "Introduction of foreign material in the body / శరీరంలోకి విదేశీ పదార్థాల ప్రవేశం వల్ల",
        "Antigen antibody reaction / యాంటిజెన్ యాంటీబాడీ ప్రతిచర్య",
        "D", "M",
        "ALLERGY = hypersensitivity reaction caused by an ANTIGEN-ANTIBODY reaction (specifically IgE-mediated Type I hypersensitivity). "
        "Mechanism: Allergen (antigen) → B cells produce IgE antibodies → IgE binds to MAST CELLS → on re-exposure: mast cells release HISTAMINE → allergic symptoms. "
        "Options (b) inhalation of pollens and (c) foreign materials are TRIGGERS (allergens), not the fundamental cause. The CAUSE is the antigen-antibody reaction itself. "
        "Symptoms: Itching, sneezing, runny nose, hives, anaphylaxis. Treatment: Antihistamines. "
        "అలెర్జీ = యాంటిజెన్-యాంటీబాడీ (IgE) ప్రతిచర్య; మాస్ట్ కణాల నుండి హిస్టామిన్ విడుదల → లక్షణాలు. పుప్పొడి/విదేశీ పదార్థాలు = ప్రేరేపకాలు (triggers).",
        15
    ),
    # Q16
    (
        "About ....... of the total calcium present in the human body is in the blood.\nతెలుగు: మానవ శరీరంలో ఉన్న మొత్తం కాల్షియంలో సుమారు ఎంత శాతం రక్తంలో ఉంటుంది?",
        "99% / 99%",
        "70% / 70%",
        "5% / 5%",
        "0.5% / 0.5% (లేదా దాదాపు 1%)",
        "D", "M",
        "Calcium distribution in the body: 99% in BONES and TEETH (as hydroxyapatite). 1% = soft tissues + blood. "
        "Of the blood calcium (~0.5% of total body calcium): 50% ionized Ca²⁺ (free/active), 40% protein-bound (albumin), 10% complexed. "
        "Normal blood calcium = 8.5–10.5 mg/dL. "
        "Functions of blood calcium: Blood clotting (Factor IV), muscle contraction, nerve transmission, enzyme activation. "
        "Regulated by: Parathyroid Hormone (PTH → raises Ca²⁺) and Calcitonin (lowers Ca²⁺). "
        "కాల్షియం: 99% ఎముకలు + దంతాలలో; ~0.5-1% రక్తంలో. రక్తంలో Ca²⁺ = రక్తం గడ్డకట్టడం, కండర సంకోచం, నాడీ ప్రసారానికి అవసరం. PTH → Ca²⁺ పెంచుతుంది.",
        16
    ),
    # Q17
    (
        "Phenylketonuria is an example of an inborn error of metabolism. This 'error' refers to:\nతెలుగు: ఫినైల్‌కెటోన్యూరియా (PKU) అనేది జీవక్రియ యొక్క పుట్టుకతో వచ్చే లోపానికి ఉదాహరణ. ఈ 'లోపం' దేనిని సూచిస్తుంది?",
        "Hormonal overproduction / హార్మోన్ల అధిక ఉత్పత్తి",
        "Non disjunction / నాన్ డిస్‌జంక్షన్",
        "Atrophy of endocrine glands / ఎండోక్రైన్ గ్రంథుల క్షీణత",
        "Inherited lack of an enzyme / ఎంజైమ్ యొక్క వారసత్వ లోపం",
        "D", "H",
        "PHENYLKETONURIA (PKU) = autosomal recessive disorder caused by INHERITED LACK of enzyme PHENYLALANINE HYDROXYLASE (PAH). "
        "Without PAH: Phenylalanine (amino acid from diet) → cannot be converted to Tyrosine → accumulates → toxic to brain → intellectual disability. "
        "'Inborn error of metabolism' = inherited enzyme deficiency. "
        "Treatment: Low-phenylalanine diet (avoid high-protein foods); detected at birth via newborn screening (Guthrie test). "
        "Non-disjunction = chromosomal error (e.g., Down syndrome). "
        "PKU = ఫినైల్‌అలనిన్ హైడ్రాక్సిలేస్ ఎంజైమ్ వారసత్వ లోపం; ఫినైల్‌అలనిన్ మెదడులో పేరుకుపోవడం → మేధా వైకల్యం. చికిత్స: తక్కువ phenylalanine ఆహారం.",
        17
    ),
    # Q18
    (
        "Which part of the donor's eye is used for grafting in order to cure certain diseases of blindness?\nతెలుగు: అంధత్వానికి సంబంధించిన కొన్ని వ్యాధులను నయం చేయడానికి దాత కంటిలో ఏ భాగాన్ని అంటుకట్టడానికి (grafting) ఉపయోగిస్తారు?",
        "Retina / రెటీనా",
        "Cornea / కార్నియా (శుక్లపటలం)",
        "Lens / కటకం",
        "Eye-ball / కనుగుడ్డు",
        "B", "E",
        "CORNEA TRANSPLANT (Keratoplasty) = most common and successful eye transplant; donated cornea replaces diseased/damaged cornea. "
        "Cornea = transparent front layer of the eye (no blood vessels → avascular → less immune rejection). "
        "Conditions treated: Corneal scarring, keratoconus, bullous keratopathy, corneal dystrophy. "
        "Retina and Lens CANNOT be transplanted (too complex, blood supply issues). Eye-ball = entire organ transplant not possible. "
        "Note: Eye donation ≠ whole eye transplant — only cornea is used. "
        "కార్నియా (శుక్లపటలం) మాత్రమే మార్పిడి చేయవచ్చు (keratoplasty); రక్తనాళాలు లేవు → తక్కువ రోగనిరోధక తిరస్కరణ. రెటీనా/కటకం మార్పిడి చేయడం సాధ్యం కాదు.",
        18
    ),
    # Q19
    (
        "Match the following:\nTeeth — Used for\nA. Incisor — 1. Cutting\nB. Canine — 1. Tearing/Cutting\nC. Molar — 2. Grinding\n(a) 1, 2, 1  (b) 2, 1, 1  (c) 1, 1, 2  (d) 1, 2, 2\nతెలుగు: దంతాలు — ఉపయోగం: A. ఇన్సిజర్స్ = కత్తిరించడం; B. కనైన్స్ = చీల్చడం; C. మోలార్స్ = నమలడం",
        "(a) 1, 2, 1 / A=1, B=2, C=1",
        "(b) 2, 1, 1 / A=2, B=1, C=1",
        "(c) 1, 1, 2 / A=1, B=1, C=2",
        "(d) 1, 2, 2 / A=1, B=2, C=2",
        "C", "E",
        "Dental function matching: A. INCISOR = Code 1 (CUTTING — chisel-shaped front teeth); B. CANINE = Code 1 (TEARING/CUTTING — pointed; also called cuspid); C. MOLAR = Code 2 (GRINDING/chewing — flat, broad surface). "
        "Answer (c): 1, 1, 2 → Incisor=Cutting(1), Canine=Tearing(1), Molar=Grinding(2). "
        "All teeth types: Incisor (cutting) + Canine (tearing) + Premolar (crushing) + Molar (grinding). "
        "దంత విధులు: ఇన్సిజర్ = కత్తిరించడం (1); కనైన్ = చీల్చడం (1); మోలార్ = నమలడం (2); జవాబు = (c) 1, 1, 2.",
        19
    ),
    # Q20
    (
        "As in the arms and legs, blood flows against gravity and is prevented from flowing back by:\nతెలుగు: చేతులు మరియు కాళ్ళలో వలె, రక్తం గురుత్వాకర్షణకు వ్యతిరేకంగా ప్రవహిస్తుంది మరియు వెనక్కి ప్రవహించకుండా దేని ద్వారా నిరోధించబడుతుంది?",
        "The extremely low pressure of venous blood / సిరల రక్తం యొక్క అతి తక్కువ పీడనం",
        "Valves / కవాటాలు",
        "Movements in the surrounding muscles / చుట్టుపక్కల కండరాల కదలికలు",
        "The narrowing down of the lumen of veins / సిరల ల్యూమన్ ఇరుకుగా మారడం",
        "B", "M",
        "VALVES in veins prevent BACKFLOW of blood. Veins contain semilunar (bicuspid) VALVES that open when blood flows toward the heart and close when blood would flow backward. "
        "Mechanism in limbs: Valves + muscle pump (surrounding skeletal muscles squeeze veins pushing blood toward heart). "
        "Varicose veins = damaged/incompetent valves → blood pools in veins. "
        "Note: Arteries do NOT have valves (blood pressure is high enough); Veins = low pressure, need valves. "
        "Heart valves: Tricuspid (right AV), Bicuspid/Mitral (left AV), Pulmonary semilunar, Aortic semilunar. "
        "సిరలలో కవాటాలు (valves) వెనక్కి ప్రవహించకుండా నిరోధిస్తాయి; కండర పంప్ + కవాటాలు కలిసి పనిచేస్తాయి. వెరికోస్ సిరలు = కవాటాలు దెబ్బతినడం.",
        20
    ),
    # Q21
    (
        "The weight of an average human male brain is about:\nతెలుగు: సగటు మానవ పురుషుని మెదడు బరువు సుమారుగా:",
        "1 kg / 1 కిలో",
        "1200 gms / 1200 గ్రాములు",
        "1350 gms / 1350 గ్రాములు",
        "1500 gms / 1500 గ్రాములు",
        "C", "E",
        "Average MALE human brain weight ≈ 1350 grams (1.35 kg). Female brain ≈ 1200–1250 g (slightly lighter due to body size difference, NOT intellect). "
        "Brain = ~2% of body weight but uses ~20% of energy (glucose) and ~15% of cardiac output. "
        "Brain is 60% fat (myelin-rich), 73–78% water. "
        "Comparison: Elephant brain ≈ 5 kg; Blue whale ≈ 7 kg; Sperm whale (largest) ≈ 8 kg; but brain:body ratio = humans highest. "
        "సగటు మానవ పురుషుని మెదడు ≈ 1350 గ్రాములు; స్త్రీ మెదడు ≈ 1200-1250 గ్రాములు. శరీర బరువులో 2% మాత్రమే కానీ 20% శక్తి వినియోగిస్తుంది.",
        21
    ),
    # Q22
    (
        "On sudden cardiac arrest, which of the following is advised as a first step to revive the functioning of the human heart?\nతెలుగు: ఆకస్మిక కార్డియాక్ అరెస్ట్ జరిగినప్పుడు, మొదటి దశగా కింది వాటిలో ఏది సూచించబడుతుంది?",
        "Sprinkling water on the face / ముఖంపై నీళ్లు చల్లడం",
        "Giving cool water to drink / చల్లని నీరు ఇవ్వడం",
        "Mouth to mouth resuscitation / నోటి ద్వారా శ్వాస అందించడం",
        "Giving external cardiac massage (CPR) / బాహ్య కార్డియాక్ మసాజ్ (CPR)",
        "C", "H",
        "Exam key: (c) Mouth-to-mouth resuscitation (artificial respiration). "
        "⚠ Note: Modern guidelines (AHA, 2010+) recommend CHEST COMPRESSIONS (CPR) as the FIRST step for cardiac arrest, not mouth-to-mouth. Current sequence: CAB = Compressions → Airway → Breathing. "
        "For exam purposes, follow key (c). "
        "Mouth-to-mouth: 2 breaths after every 30 chest compressions in CPR. Defibrillator (AED) = restores rhythm. "
        "పరీక్ష కీ: (c) నోటి ద్వారా శ్వాస అందించడం. ⚠ ఆధునిక మార్గదర్శకాలు (AHA 2010+): మొదట చెస్ట్ కంప్రెషన్స్ (CPR) సిఫార్సు చేస్తాయి. పరీక్షలో (c) అనుసరించండి.",
        22
    ),
    # Q23
    (
        "Identical twins arise when two:\nతెలుగు: ఐడెంటికల్ ట్విన్స్ (ఒకేలా ఉండే కవలలు) ఎప్పుడు ఏర్పడతారు?",
        "Cells develop independently from the same zygote / ఒకే జైగోట్ నుండి రెండు కణాలు స్వతంత్రంగా అభివృద్ధి చెందినప్పుడు",
        "Gametes develop independently / సంయోగబీజాలు స్వతంత్రంగా అభివృద్ధి చెందినప్పుడు",
        "Sperms develop independently / శుక్రకణాలు స్వతంత్రంగా అభివృద్ధి చెందినప్పుడు",
        "Ova develop independently / అండాలు స్వతంత్రంగా అభివృద్ధి చెందినప్పుడు",
        "A", "M",
        "IDENTICAL TWINS (Monozygotic) = arise from ONE ZYGOTE that splits into TWO cells/embryos, each developing independently → same genetic material (same DNA). "
        "FRATERNAL TWINS (Dizygotic) = two separate eggs fertilized by two separate sperms → different genetic material (like siblings). "
        "Identical twins: same sex, blood group, fingerprints similar but not identical; share one chorion (often). "
        "Conjoined twins = incomplete separation of the single zygote. "
        "ఐడెంటికల్ ట్విన్స్ (Monozygotic): ఒకే జైగోట్ → రెండుగా విభజన → ఒకే DNA. ఫ్రెటర్నల్ ట్విన్స్ (Dizygotic): రెండు అండాలు + రెండు శుక్రకణాలు → వేరే DNA.",
        23
    ),
    # Q24
    (
        "The image formed on the retina of the eye is:\nతెలుగు: కంటి రెటీనాపై ఏర్పడే ప్రతిబింబం ఎలా ఉంటుంది?",
        "Real and upright / నిజమైనది మరియు నిటారుగా ఉన్నది",
        "Real and inverted / నిజమైనది మరియు తలక్రిందులైనది",
        "Virtual and upright / మిథ్యా మరియు నిటారుగా ఉన్నది",
        "Real and enlarged / నిజమైనది మరియు పెద్దదిగా ఉన్నది",
        "B", "M",
        "Image on RETINA = REAL (formed by actual light rays converging) and INVERTED (upside down) — like a camera. "
        "The eye lens converges light rays from the object onto the retina, forming a real, inverted, and diminished image. "
        "The brain (occipital cortex via optic nerve) CORRECTS the inverted image so we perceive it as upright. "
        "Eye ↔ Camera: Retina = film; Cornea+Lens = lens; Iris = aperture; Pupil = opening. "
        "రెటీనాపై ప్రతిబింబం = నిజమైనది మరియు తలక్రిందులైనది (real & inverted); కటకం కాంతి పుంజాలను కేంద్రీకరిస్తుంది; మెదడు దాన్ని నిటారుగా మారుస్తుంది.",
        24
    ),
    # Q25
    (
        "Element that is not found in blood is:\nతెలుగు: రక్తంలో కనిపించని మూలకం ఏది?",
        "Iron / ఇనుము",
        "Copper / రాగి",
        "Chromium / క్రోమియం",
        "Magnesium / మెగ్నీషియం",
        "C", "M",
        "CHROMIUM is NOT normally found in blood in significant/detectable amounts (for standard exam purposes). "
        "Elements normally found in blood: IRON (Fe — hemoglobin), COPPER (Cu — ceruloplasmin, enzymes), MAGNESIUM (Mg — enzyme cofactor, ATP, chlorophyll analogy), Zinc, Calcium, Sodium, Potassium. "
        "Note: Chromium (Cr) is a trace element used in glucose metabolism (enhances insulin action) but is present in extremely small amounts and not considered a standard blood element. "
        "రక్తంలో సాధారణంగా లేని మూలకం = క్రోమియం (Cr). రక్తంలో ఉండే మూలకాలు: Fe (హిమోగ్లోబిన్), Cu (సెరులోప్లాస్మిన్), Mg (ఎంజైమ్ కోఫ్యాక్టర్), Ca, Na, K.",
        25
    ),
    # Q26
    (
        "Scratching eases itching because:\nతెలుగు: గోకడం వల్ల దురద తగ్గుతుంది, ఎందుకంటే:",
        "It kills germs / ఇది సూక్ష్మక్రిములను చంపుతుంది",
        "It suppresses the production of enzymes which cause itching / దురద కలిగించే ఎంజైమ్‌ల ఉత్పత్తిని అణిచివేస్తుంది",
        "It removes the outer dust in the skin / చర్మంలోని బయటి దుమ్మును తొలగిస్తుంది",
        "It stimulates certain nerves which direct the brain to increase the production of antihistaminic chemicals / కొన్ని నాడులను ప్రేరేపించి, యాంటీహిస్టామినిక్ రసాయనాల ఉత్పత్తిని పెంచమని మెదడును నిర్దేశిస్తుంది",
        "D", "H",
        "Scratching relieves itching via the GATE CONTROL THEORY of pain (Melzack & Wall, 1965): "
        "Scratching stimulates touch/pressure nerves (A-β fibres) which CLOSE THE GATE in the spinal cord → inhibit itch signals (C fibres). "
        "Also: scratching stimulates nerve fibres → brain releases SEROTONIN → can override itch signals → also signals release of antihistaminic substances. "
        "Downside: Scratching can worsen itch-scratch cycle (repeated scratching releases more histamine). "
        "గోకడం వల్ల దురద తగ్గడం = GATE CONTROL THEORY; A-β నాడి తంతువులు మూసుకు పోతాయి → itch సంకేతాలు తగ్గుతాయి; మెదడు సెరోటోనిన్ విడుదల చేస్తుంది.",
        26
    ),
    # Q27
    (
        "The gland which in relation to body size is largest at birth and then gradually shrinks after puberty, is:\nతెలుగు: పుట్టినప్పుడు శరీర పరిమాణంతో పోలిస్తే అతిపెద్దదిగా ఉండి, యుక్తవయస్సు తర్వాత క్రమంగా కుంచించుకుపోయే గ్రంథి ఏది?",
        "Thyroid / థైరాయిడ్",
        "Pituitary / పిట్యూటరీ",
        "Thymus / థైమస్ (బాల గ్రంథి)",
        "Adrenal / అడ్రినల్",
        "C", "M",
        "THYMUS GLAND = largest relative to body size at birth; gradually shrinks (involutes) after puberty via INVOLUTION. "
        "By adulthood: mostly replaced by fat. "
        "Function: T-CELL MATURATION — naive T-lymphocytes from bone marrow migrate to thymus → mature into immunocompetent T-cells → enter bloodstream. "
        "Thymic hormones: Thymosin, Thymolin, Thymopoietin → promote T-cell development. "
        "Disease: DiGeorge syndrome = thymus absent → severe immune deficiency. "
        "థైమస్ (బాల గ్రంథి): పుట్టినప్పుడు చాలా పెద్దది; యుక్తవయస్సు తర్వాత కుంచించుకుపోతుంది; T-కణాల పరిపక్వతకు అవసరం; థైమోసిన్ హార్మోన్ స్రవిస్తుంది.",
        27
    ),
    # Q28
    (
        "The first organ to be transplanted was:\nతెలుగు: మొట్టమొదట మార్పిడి (transplant) చేయబడిన అవయవం ఏది?",
        "Kidney / మూత్రపిండం",
        "Lung / ఊపిరితిత్తులు",
        "Heart / గుండె",
        "Liver / కాలేయం",
        "C", "H",
        "⚠ Exam key: (c) Heart. Referring to the famous 1967 heart transplant by Dr. Christiaan Barnard at Groote Schuur Hospital, Cape Town, South Africa. "
        "Scientific note: The FIRST SUCCESSFUL organ transplant was a KIDNEY (a) — performed by Dr. Joseph Murray in 1954 at Peter Bent Brigham Hospital, Boston (Nobel Prize 1990). "
        "1967 heart transplant patient (Louis Washkansky) survived only 18 days. "
        "For EXAM: follow key (c) Heart. Scientifically, Kidney was first. "
        "⚠ పరీక్ష కీ: (c) గుండె (1967, Dr. Barnard). శాస్త్రీయంగా: మొదటి విజయవంతమైన మార్పిడి = మూత్రపిండం (1954, Dr. Murray). పరీక్షలో (c) అనుసరించండి.",
        28
    ),
    # Q29
    (
        "Which of the following human bones is the knee bone?\nతెలుగు: కింది మానవ ఎముకలలో మోకాలి ఎముక (knee bone) ఏది?",
        "Stapes / స్టేపిస్ (కర్ణాంతరాస్థి)",
        "Clavicle / క్లావికిల్ (జత్రుక)",
        "Phalanx / ఫాలాంక్స్ (వేలి ఎముక)",
        "Patella / పటెల్లా (మోచిప్ప)",
        "D", "E",
        "PATELLA = knee bone (kneecap); a sesamoid bone embedded in the quadriceps tendon. "
        "Stapes = smallest bone in human body (in the middle ear — one of the 3 ossicles: Malleus, Incus, Stapes). "
        "Clavicle = collarbone (connects sternum to shoulder/scapula). "
        "Phalanx = bones of fingers and toes (14 phalanges per hand). "
        "పటెల్లా = మోకాలి ఎముక (kneecap); సెసామాయిడ్ ఎముక. స్టేపిస్ = శరీరంలో అతిచిన్న ఎముక (చెవి); క్లావికిల్ = కాలర్‌బోన్; ఫాలాంక్స్ = వేలి ఎముక.",
        29
    ),
    # Q30
    (
        "A human sperm may contain:\n1. X-chromosome\n2. Y-chromosome\n3. XY-chromosome\nతెలుగు: మానవ శుక్రకణం (sperm) దేనిని కలిగి ఉండవచ్చు?\n1. X-క్రోమోజోమ్\n2. Y-క్రోమోజోమ్\n3. XY-క్రోమోజోమ్",
        "(a) 1 only / 1 మాత్రమే (X)",
        "(b) 2 only / 2 మాత్రమే (Y)",
        "(c) 1 and 2 / 1 మరియు 2 (X లేదా Y)",
        "(d) 1, 2, and 3 / 1, 2, మరియు 3",
        "C", "M",
        "Human sperm contains either X or Y chromosome (NOT both simultaneously). "
        "Males (XY): During meiosis → 50% sperm carry X chromosome; 50% carry Y chromosome. Each sperm = haploid (n = 23 chromosomes). "
        "If X-sperm fertilizes egg (X) → XX = FEMALE. If Y-sperm fertilizes egg (X) → XY = MALE. "
        "Sex determination is by FATHER (sperm) — the egg always carries X. "
        "Option 3 (XY) is wrong — a sperm cannot carry both sex chromosomes (would be non-disjunction abnormality). "
        "శుక్రకణం: X లేదా Y క్రోమోజోమ్ మాత్రమే (ఒకేసారి రెండూ కాదు); X-శుక్రకణం + అండం = XX (ఆడ); Y-శుక్రకణం + అండం = XY (మగ). లింగ నిర్ణయం = తండ్రి (శుక్రకణం) నిర్ణయిస్తాడు.",
        30
    ),
    # Q31
    (
        "The amount of light entering the eye is regulated by:\nతెలుగు: కంటిలోకి ప్రవేశించే కాంతి పరిమాణం దేని ద్వారా నియంత్రించబడుతుంది?",
        "Cornea / కార్నియా (శుక్లపటలం)",
        "Pupil / కనుపాప",
        "Iris / ఐరిస్ (కృష్ణపటలం)",
        "Sclera / స్క్లెరా",
        "C", "M",
        "IRIS regulates the amount of light entering the eye by controlling the size of the PUPIL. "
        "Iris = colored circular muscular diaphragm; contains sphincter (constricts in bright light) and dilator (dilates in dim light) muscles. "
        "Bright light → Iris constricts → SMALLER PUPIL → less light in. Dim light → Iris dilates → LARGER PUPIL → more light in. "
        "Note: PUPIL (b) is merely the opening/hole in the iris; the IRIS (c) is the structure that controls the size of the pupil → iris is the more precise answer. "
        "Cornea = transparent refractive surface; Sclera = white protective outer coat. "
        "ఐరిస్ = కనుపాప యొక్క పరిమాణాన్ని మార్చడం ద్వారా కాంతి పరిమాణాన్ని నియంత్రిస్తుంది. కనుపాప = ఐరిస్‌లో రంధ్రం మాత్రమే; ఐరిస్ = కండర నిర్మాణం.",
        31
    ),
    # Q32
    (
        "The heart of a human embryo starts beating:\nతెలుగు: మానవ పిండం యొక్క గుండె ఎప్పుడు కొట్టుకోవడం ప్రారంభమవుతుంది?",
        "In the first week of its development / మొదటి వారంలో",
        "In the third week of its development / మూడవ వారంలో",
        "In the fourth week of its development / నాల్గవ వారంలో",
        "In the sixth week of its development / ఆరవ వారంలో",
        "D", "M",
        "Embryo heart starts beating at approximately the 6th WEEK of development (as per exam key; some sources cite day 21-22 = 3rd week as first electrical activity). "
        "Cardiac development: Week 3 = heart tube forms; Week 4 = first contractions; Week 6 = visible heartbeat on ultrasound. "
        "Exam standard: 6th week = when heartbeat is clearly detectable by ultrasound. "
        "By week 8 = 4-chambered heart formed; at birth = ductus arteriosus closes, foramen ovale closes → adult circulation. "
        "మానవ పిండం గుండె ≈ 6వ వారంలో కొట్టుకోవడం ప్రారంభమవుతుంది (అల్ట్రాసౌండ్‌లో కనిపించే స్పందన). వారం 3 = హృదయ గొట్టం ఏర్పడటం; వారం 8 = 4 గదులు పూర్తవడం.",
        32
    ),
    # Q33
    (
        "A person's blood group will not have any antibodies if it is:\nతెలుగు: ఒక వ్యక్తికి ఏ రక్తపు గ్రూపు ఉంటే వారి రక్తంలో ఎలాంటి ప్రతిరక్షకాలు (antibodies) ఉండవు?",
        "A / A",
        "B / B",
        "O / O",
        "AB / AB",
        "D", "M",
        "AB blood group = UNIVERSAL RECIPIENT — has BOTH A and B antigens on RBC surface → has NO anti-A or anti-B antibodies in plasma (would destroy own cells). "
        "Blood group antibody summary: Group A = has anti-B antibodies; Group B = has anti-A antibodies; Group O = has BOTH anti-A and anti-B (cannot receive A, B, or AB); Group AB = NO antibodies. "
        "AB = Universal Recipient (accepts all groups); O = Universal Donor (donates to all groups). "
        "రక్తపు గ్రూపు AB: RBC పై A మరియు B రెండు యాంటీజన్లు → ప్లాస్మాలో ఎలాంటి యాంటీబాడీలు లేవు → అన్ని గ్రూపుల నుండి రక్తం తీసుకోవచ్చు (విశ్వ గ్రహీత).",
        33
    ),
    # Q34
    (
        "Which of the following is not a bone in the legs of the human body?\nతెలుగు: కింది వాటిలో మానవ శరీరంలోని కాళ్ళలో లేని ఎముక ఏది?",
        "Radius / రేడియస్ (చేయి ఎముక)",
        "Tibia / టిబియా",
        "Femur / ఫీమర్",
        "Fibula / ఫైబులా",
        "A", "E",
        "RADIUS = forearm bone (ARM, not leg) — paired with ULNA in the forearm; below the humerus. "
        "Leg bones: FEMUR (thigh/upper leg — longest and strongest bone in body); TIBIA (shinbone, lower leg); FIBULA (smaller lateral lower leg bone). "
        "Foot bones: Tarsals, Metatarsals, Phalanges. Knee = Patella. "
        "Arm bones: Humerus (upper arm) + Radius + Ulna (forearm). "
        "రేడియస్ = చేయి ఎముక (forearm = ముంచేయి), కాలి ఎముక కాదు. కాలి ఎముకలు: ఫీమర్ (తొడ) + టిబియా + ఫైబులా (కింది కాలు). శరీరంలో అతిపెద్ద ఎముక = ఫీమర్.",
        34
    ),
    # Q35
    (
        "Which of the following practices can prevent blood coagulation?\n1. Chilling\n2. Thermal treatment\n3. Adding oxalate\nతెలుగు: కింది పద్ధతులలో ఏవి రక్తం గడ్డకట్టడాన్ని (coagulation) నిరోధించగలవు?\n1. చల్లబరచడం (Chilling)\n2. ఉష్ణ చికిత్స\n3. ఆక్సలేట్ కలపడం",
        "(a) 1 and 2 / 1 మరియు 2",
        "(b) 2 and 3 / 2 మరియు 3",
        "(c) 1 and 3 / 1 మరియు 3",
        "(d) 1, 2, and 3 / 1, 2, మరియు 3",
        "C", "M",
        "Anticoagulation methods: "
        "1. CHILLING (low temperature) ✓ — slows enzyme activity of clotting factors; blood banks store blood at 4°C. "
        "2. THERMAL TREATMENT ✗ — heat/boiling denatures proteins, but Thermal treatment does NOT reliably prevent clotting (may destroy/denature clotting factors but this is not a standard anticoagulation method). "
        "3. ADDING OXALATE ✓ — oxalate chelates/binds Ca²⁺ → removes Ca²⁺ → clotting cascade cannot proceed (Ca²⁺ is essential for multiple clotting steps). "
        "Other anticoagulants: Citrate (chelates Ca²⁺), Heparin (activates antithrombin), Warfarin (Vit K antagonist), EDTA. "
        "1. చల్లబరచడం ✓ (ఎంజైమ్ చర్య తగ్గుతుంది); 3. ఆక్సలేట్ ✓ (Ca²⁺ తొలగిస్తుంది → గడ్డకట్టడం నిరోధం); 2. ఉష్ణ చికిత్స = ప్రమాణిత పద్ధతి కాదు.",
        35
    ),
    # Q36
    (
        "Respiratory quotient is the ratio of:\nతెలుగు: రెస్పిరేటరీ కోషెంట్ (శ్వాసక్రియ నిష్పత్తి) అంటే దేని నిష్పత్తి?",
        "CO2/H2O",
        "O2/CO2",
        "O2/H2O",
        "CO2/O2",
        "D", "E",
        "RESPIRATORY QUOTIENT (RQ) = Volume of CO₂ produced / Volume of O₂ consumed. "
        "RQ values by substrate: Carbohydrates = 1.0 (equal CO₂ produced and O₂ consumed); Fats = 0.7 (more O₂ needed); Proteins = 0.8 (intermediate). Mixed diet RQ ≈ 0.85. "
        "Formula: C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O → RQ = 6CO₂/6O₂ = 1.0 "
        "High RQ (>1) = anaerobic fermentation (CO₂ produced without O₂ used). RQ < 0.7 = starvation/excess fat oxidation. "
        "RQ = CO₂ ఉత్పత్తి / O₂ వినియోగం. కార్బోహైడ్రేట్లు = 1.0; కొవ్వులు = 0.7; ప్రోటీన్లు = 0.8. మిశ్రమ ఆహారం ≈ 0.85.",
        36
    ),
    # Q37
    (
        "Which can bind O2 molecules?\nతెలుగు: O2 (ఆక్సిజన్) అణువులను ఏవి బంధించగలవు?",
        "Red blood cells / ఎర్ర రక్త కణాలు",
        "White blood cells / తెల్ల రక్త కణాలు",
        "Vitamin B12 / విటమిన్ B12",
        "Vitamin E / విటమిన్ E",
        "A", "E",
        "RED BLOOD CELLS (RBCs/Erythrocytes) bind O₂ via HEMOGLOBIN (Fe²⁺ in heme group). Each RBC contains ~280 million hemoglobin molecules; each Hb carries 4 O₂. "
        "Oxyhemoglobin (HbO₂) = Hb bound to O₂ (bright red, in arteries). Deoxyhemoglobin = Hb without O₂ (dark red/purple, in veins). "
        "White blood cells = immune function (no hemoglobin, no O₂ binding). "
        "Vitamin B12 (cobalamin) = contains cobalt, involved in DNA synthesis and nerve function (NOT O₂ binding). Vitamin E = antioxidant. "
        "RBC లు హిమోగ్లోబిన్ (Fe²⁺) ద్వారా O₂ ను బంధిస్తాయి. ఆక్సీహిమోగ్లోబిన్ (HbO₂) = ప్రకాశవంతమైన ఎరుపు. విటమిన్ B12 = కోబాల్ట్ కలిగి ఉంటుంది; O₂ బంధించదు.",
        37
    ),
    # Q38
    (
        "Bleeding from an artery is characterized by which of the following?\n1. Blood is red.\n2. Blood is purple.\n3. Bleeding is continuous.\n4. Bleeding is intermittent.\nతెలుగు: ధమని (artery) నుండి రక్తస్రావం యొక్క లక్షణాలు ఏవి?",
        "(a) 1 and 3 / 1 మరియు 3",
        "(b) 2 and 3 / 2 మరియు 3",
        "(c) 1 and 4 / 1 మరియు 4",
        "(d) 2 and 4 / 2 మరియు 4",
        "B", "H",
        "⚠ Exam key: (b) 2 and 3 (purple blood, continuous bleeding). Scientifically INCORRECT for arteries. "
        "ARTERIAL BLEEDING (Scientifically): Blood = BRIGHT RED (oxygenated), Bleeding = SPURTS/INTERMITTENT (pulsatile — follows heartbeat). → Correct answer should be (c) 1 and 4. "
        "VENOUS BLEEDING: Blood = DARK PURPLE/MAROON (deoxygenated), Bleeding = CONTINUOUS (steady flow). → Options 2 and 3 describe VENOUS bleeding. "
        "The exam key (b) appears to be a printing error — it describes venous, not arterial bleeding. For exam: mark (b). Scientifically: arterial = bright red + intermittent (1 and 4). "
        "⚠ పరీక్ష కీ: (b) — శాస్త్రీయంగా తప్పు! ధమని రక్తం = ప్రకాశవంతమైన ఎరుపు (1) + అడపా దడపా (4). పరీక్ష కీ (b) = సిర లక్షణాలు వర్ణిస్తుంది. పరీక్షలో (b) గుర్తించండి.",
        38
    ),
    # Q39
    (
        "Which of the following is not a vestigial organ?\nతెలుగు: కింది వాటిలో అవశేష అవయవం (vestigial organ) కానిది ఏది?",
        "Centriole / సెంట్రియోల్",
        "Molar tooth / మోలార్ టూత్ (జ్ఞానదంతం)",
        "Appendix / అపెండిక్స్ (ఉండుకం)",
        "Diaphragm / డయాఫ్రాగమ్ (విభాజక పటలం)",
        "D", "M",
        "DIAPHRAGM = dome-shaped muscle separating thorax from abdomen; ESSENTIAL for breathing (contracts → expands lungs → inhalation) — NOT a vestigial organ. "
        "Vestigial organs (reduced-function evolutionary remnants): APPENDIX (remnant of cecum, site of gut bacteria in ancestors); WISDOM TEETH/Molar 3 (jaw has shrunk in evolution); CENTRIOLE (disputed — may function in cell division). "
        "Other vestigial organs: Plica semilunaris (inner corner of eye = remnant of nictitating membrane), Arrector pili muscles (goosebumps = useless in humans), Coccyx (tailbone). "
        "డయాఫ్రాగమ్ = శ్వాసక్రియకు అత్యావశ్యక కండరం → అవశేష అవయవం కాదు. అవశేష అవయవాలు: అపెండిక్స్, జ్ఞానదంతాలు, సెంట్రియోల్, coccyx.",
        39
    ),
    # Q40
    (
        "Which of the following bone articulations forms the gliding joint?\nతెలుగు: కింది వాటిలో గ్లైడింగ్ జాయింట్ (జారే కీలు) ను ఏర్పరిచే ఎముకల కలయిక ఏది?",
        "Humerus and radius / హ్యూమరస్ మరియు రేడియస్",
        "Carpals / కార్పెల్స్ (మణికట్టు ఎముకలు)",
        "Hip girdle and femur / హిప్ గిర్డిల్ మరియు ఫీమర్",
        "Skull & neck vertebrae / పుర్రె & మెడ వెన్నుపూస",
        "B", "M",
        "GLIDING JOINT (Plane/Arthrodial joint) = flat articular surfaces that slide/glide past each other; limited movement. "
        "Formed by: CARPALS (wrist bones) and TARSALS (ankle bones) — glide against each other. Also: between vertebral articular facets. "
        "Other joint types: Ball-and-socket = Hip (femur + acetabulum of pelvis) and Shoulder (c = ball-and-socket). Pivot = Atlas-Axis (skull rotation, d). Hinge = Elbow (humerus + radius, a). Condylar = Wrist (radius + carpals). "
        "గ్లైడింగ్ జాయింట్ = కార్పెల్స్ (మణికట్టు ఎముకలు) మధ్య ఏర్పడుతుంది; అల్పమైన సరికి కదులుతాయి. Ball-and-socket = హిప్ (c); Pivot = Atlas-Axis (d); Hinge = మోచేయి (a).",
        40
    ),
    # Q41
    (
        "Ovulation is prevented by using:\nతెలుగు: అండోత్సర్గం (Ovulation) దేనిని ఉపయోగించడం ద్వారా నిరోధించబడుతుంది?",
        "IUD (Intrauterine Device) / IUD (గర్భాశయ పరికరం)",
        "Copper T / కాపర్ T",
        "Infanticide / శిశుహత్య",
        "Pills / మాత్రలు",
        "D", "E",
        "ORAL CONTRACEPTIVE PILLS (OCPs) = contain synthetic ESTROGEN + PROGESTERONE → suppress FSH and LH → PREVENT OVULATION (egg not released). "
        "IUD (a) and Copper T (b) = prevent IMPLANTATION of fertilized egg in uterus (NOT ovulation); also may inhibit sperm motility. "
        "Infanticide (c) = killing of born infant — NOT a contraceptive method (illegal and unethical). "
        "Other contraceptive methods: Barrier (condom, diaphragm), Surgical (vasectomy, tubectomy), Emergency pills (Plan B — prevents ovulation/implantation). "
        "OCP లు (గర్భనిరోధక మాత్రలు): ఈస్ట్రోజెన్ + ప్రొజెస్టిరోన్ → FSH/LH అణిచివేయడం → అండోత్సర్గం నిరోధించడం. IUD/కాపర్ T = అమర్పు (implantation) నిరోధిస్తాయి.",
        41
    ),
    # Q42
    (
        "Color of the skin is due to the presence of:\nతెలుగు: చర్మం రంగు దేని ఉనికి వల్ల వస్తుంది?",
        "Rennin / రెన్నిన్",
        "Melanin / మెలనిన్",
        "Mesotosin / మెసోటోసిన్",
        "Metatorin / మెటాటోరిన్",
        "B", "E",
        "MELANIN = pigment produced by MELANOCYTES (cells in the basal layer of epidermis) that determines skin color, hair color, and iris color. "
        "Types: Eumelanin (brown/black); Pheomelanin (red/yellow). "
        "Functions: Absorbs UV radiation → protects DNA from UV damage → prevents skin cancer. "
        "More melanin → darker skin; Less melanin → lighter skin. Sun exposure → more melanin → tanning. "
        "Albinism = inability to produce melanin. Vitiligo = patchy loss of melanin. "
        "Rennin = stomach enzyme (milk coagulation in infants). Mesotosin/Metatorin = fictitious names. "
        "మెలనిన్: మెలనోసైట్ కణాలు ఉత్పత్తి చేస్తాయి; చర్మం/జుట్టు/కళ్ళ రంగు; UV రక్షణ. ఆల్బినిజం = మెలనిన్ లేకపోవడం.",
        42
    ),
    # Q43
    (
        "Pancreas secretes hormones which help in:\nతెలుగు: ప్యాంక్రియాస్ (క్లోమం) స్రవించే హార్మోన్లు దేనికి సహాయపడతాయి?",
        "Blood clotting / రక్తం గడ్డకట్టడానికి",
        "Production of antibodies / ప్రతిరక్షకాల ఉత్పత్తికి",
        "Growth of the body / శరీర పెరుగుదలకు",
        "Keeping sugar balance in the body / శరీరంలో చక్కెర సమతుల్యతను ఉంచడానికి",
        "D", "E",
        "PANCREAS endocrine hormones: INSULIN (β cells of Islets of Langerhans) → lowers blood glucose (promotes uptake by cells); GLUCAGON (α cells) → raises blood glucose (promotes glycogenolysis in liver). "
        "Together = maintain blood SUGAR BALANCE (glucose homeostasis). "
        "Pancreas is also exocrine: produces digestive enzymes (amylase, lipase, trypsinogen) via pancreatic duct into duodenum. "
        "Insulin deficiency/resistance → Diabetes Mellitus. "
        "క్లోమం హార్మోన్లు: ఇన్సులిన్ (β కణాలు) → రక్తంలో చక్కెర తగ్గించడం; గ్లుకగాన్ (α కణాలు) → రక్తంలో చక్కెర పెంచడం. కలిసి = రక్తంలో చక్కెర సమతుల్యత నిర్వహిస్తాయి.",
        43
    ),
    # Q44
    (
        "Inspection and dissection of a body after death in human beings, as for determination of the cause of death is called:\nతెలుగు: మరణానికి గల కారణాన్ని నిర్ణయించడానికి మరణం తర్వాత మానవ శరీరాన్ని తనిఖీ చేయడం మరియు కోయడాన్ని ఏమంటారు?",
        "Autograft / ఆటోగ్రాఫ్ట్",
        "Autotomy / ఆటోటోమీ",
        "Autopsy / ఆటోప్సీ (శవపరీక్ష)",
        "Autoesism / ఆటోయిసిజం",
        "C", "E",
        "AUTOPSY (post-mortem examination) = from Greek 'autos' (self) + 'opsis' (sight) = 'seeing for oneself'. "
        "Process: External examination + internal dissection of organs → determine cause/manner of death, find disease, identify injuries, or for research/education. "
        "Types: Forensic autopsy (legal/criminal cases), Clinical/Medical autopsy (disease study), Academic (education). "
        "Autograft = transplanting tissue from one part of a person's own body to another (e.g., skin graft). "
        "Autotomy = self-amputation (lizard tail dropping). Autoesism = fictitious term. "
        "ఆటోప్సీ (శవపరీక్ష) = మరణ కారణం నిర్ణయించడానికి శరీర పరీక్ష + విచ్ఛేదన. ఆటోగ్రాఫ్ట్ = స్వీయ కణజాల మార్పిడి. ఆటోటోమీ = స్వీయ అవయవ కోత (బల్లి తోక).",
        44
    ),
    # Q45
    (
        "Anticoagulants citrate and oxalates prevent blood clotting. This is done by removing:\nతెలుగు: ప్రతిస్కందకాలు (Anticoagulants) అయిన సిట్రేట్ మరియు ఆక్సలేట్‌లు రక్తం గడ్డకట్టడాన్ని నిరోధిస్తాయి. ఇవి దేనిని తొలగించడం ద్వారా ఇది చేస్తాయి?",
        "Na+ (Sodium) / Na+ (సోడియం)",
        "K+ (Potassium) / K+ (పొటాషియం)",
        "Ca++ (Calcium) / Ca++ (కాల్షియం)",
        "None of these / ఇవేవీ కావు",
        "C", "E",
        "CITRATE and OXALATE = anticoagulants that prevent clotting by CHELATING (binding/removing) Ca²⁺ (Calcium ions). "
        "Ca²⁺ is ESSENTIAL for multiple steps in the clotting cascade (Factor IV): activates thrombin (Factor IIa), required for factors VII, IX, X activation. "
        "Without Ca²⁺ → clotting cascade cannot proceed → no fibrin clot. "
        "Sodium citrate = used in blood banks (stored blood); Sodium oxalate = laboratory anticoagulant; EDTA = chelates Ca²⁺ (used in CBC blood samples). "
        "సిట్రేట్ + ఆక్సలేట్ = Ca²⁺ (కాల్షియం) ను బంధించి తొలగిస్తాయి → గడ్డకట్టే క్రమానికి Ca²⁺ లేకపోవడం → గడ్డకట్టడం ఆగుతుంది. రక్త బ్యాంకులలో sodium citrate వాడతారు.",
        45
    ),
    # Q46
    (
        "Which of the following best explains why uracil is used in RNA instead of thymine?\nతెలుగు: RNA లో థైమిన్‌కు బదులుగా యురేసిల్ ఎందుకు ఉపయోగించబడుతుందో కింది వాటిలో ఏది ఉత్తమంగా వివరిస్తుంది?",
        "Uracil enhances RNA splicing / యురేసిల్ RNA స్ప్లైసింగ్‌ను పెంచుతుంది",
        "Thymine is not recognized by ribosomes / థైమిన్ రైబోజోమ్‌లచే గుర్తించబడదు",
        "Thymine inhibits transcription / థైమిన్ ట్రాన్స్‌క్రిప్షన్‌ను నిరోధిస్తుంది",
        "Uracil is energetically cheaper to synthesise / యురేసిల్ సంశ్లేషణ చేయడం శక్తిపరంగా చవకైనది",
        "D", "H",
        "URACIL is used in RNA instead of Thymine because Uracil is ENERGETICALLY CHEAPER to synthesize. "
        "Thymine = methylated uracil (Uracil + methyl group CH₃ at C-5) → requires additional energy for methylation. "
        "Since RNA is short-lived and produced in large quantities, it's more efficient to use Uracil. "
        "DNA uses Thymine for STABILITY — Cytosine deaminates to Uracil (mutation); if Uracil were in DNA, repair machinery couldn't distinguish 'normal' Uracil from mutated Cytosine → DNA uses Thymine to flag mutations for repair. "
        "DNA = stable, permanent → Thymine. RNA = transient, temporary → Uracil (cheaper). "
        "RNA లో యురేసిల్: సంశ్లేషణ చేయడానికి శక్తి తక్కువ (థైమిన్ = మిథైలేట్ చేయాలి). DNA లో థైమిన్: సైటోసిన్ → యురేసిల్ మ్యుటేషన్‌లను గుర్తించడానికి.",
        46
    ),
    # Q47
    (
        "ECG records\nతెలుగు: ECG (ఎలక్ట్రోకార్డియోగ్రామ్) దేనిని రికార్డ్ చేస్తుంది?",
        "Rate of heartbeats / హృదయ స్పందన రేటు (మరియు విద్యుత్ కార్యకలాపాలు)",
        "Shape of Heart / గుండె ఆకారం",
        "Ventricular concentration / వెంట్రిక్యులర్ ఏకాగ్రత",
        "Volume of blood pumped / పంప్ చేయబడిన రక్త పరిమాణం",
        "A", "E",
        "ECG (Electrocardiogram) = records ELECTRICAL ACTIVITY of the heart — rate, rhythm, and pattern of electrical impulses. "
        "ECG waves: P wave (atrial depolarization/contraction), QRS complex (ventricular depolarization/contraction), T wave (ventricular repolarization/relaxation). "
        "Uses: Diagnose arrhythmias (abnormal rhythms), heart attacks (MI), heart block, pericarditis. "
        "Echocardiogram (Echo/Ultrasound) = shows heart SHAPE and structure. Cardiac output/volume measured by other methods (not ECG). "
        "ECG (ఎలక్ట్రోకార్డియోగ్రామ్) = గుండె విద్యుత్ కార్యకలాపాలు రికార్డ్ చేస్తుంది (రేటు, లయ). P తరంగం (కర్ణిక), QRS సంకీర్ణం (జఠరిక), T తరంగం (వ్యాకోచం).",
        47
    ),
    # Q48
    (
        "Cylindrical glasses are advised to a person suffering from:\nతెలుగు: స్థూపాకార అద్దాలను (Cylindrical glasses) ఏ వ్యాధితో బాధపడుతున్న వ్యక్తికి సూచిస్తారు?",
        "Nightblindness / రేచీకటి",
        "Myopia / మయోపియా (హ్రస్వదృష్టి)",
        "Astigmatism / ఆస్టిగ్మాటిజం",
        "Hypermetropia / హైపర్‌మెట్రోపియా (దీర్ఘదృష్టి)",
        "C", "E",
        "ASTIGMATISM = irregular curvature of the cornea or lens → different focal lengths in different planes → blurred vision at all distances. "
        "Corrected by: CYLINDRICAL (Toric) lenses — different focal power in different meridians to compensate for uneven curvature. "
        "Myopia = concave lens; Hypermetropia = convex lens; Astigmatism = cylindrical/toric lens; Presbyopia (old-age) = bifocal. "
        "Nightblindness = Vitamin A deficiency (rod cells fail) → NOT corrected by glasses (requires Vitamin A). "
        "ఆస్టిగ్మాటిజం = కార్నియా/కటకం అసమాన వక్రత → అన్ని దూరాల్లో అస్పష్టత → స్థూపాకార (cylindrical) అద్దాలు. హ్రస్వదృష్టి = పుటాకార; దీర్ఘదృష్టి = కుంభాకార.",
        48
    ),
    # Q49
    (
        "A person with high blood pressure is advised to reduce the intake of\nతెలుగు: అధిక రక్తపోటు ఉన్న వ్యక్తి దేనిని తక్కువగా తీసుకోవాలని సూచిస్తారు?",
        "Magnesium / మెగ్నీషియం",
        "Potassium / పొటాషియం (option b)",
        "Potassium / పొటాషియం (option c — print error)",
        "Sodium / సోడియం (ఉప్పు)",
        "D", "E",
        "SODIUM (Na⁺) intake should be REDUCED in high blood pressure (hypertension). "
        "Mechanism: High sodium → water retention (osmosis) → increased blood volume → increased cardiac output → higher blood pressure. "
        "Normal sodium intake: <2300 mg/day (WHO); For hypertensives: <1500 mg/day. "
        "Note: Options (b) and (c) both say 'Potassium' — this is a PRINTING ERROR in the original question. Potassium actually LOWERS blood pressure (relaxes blood vessel walls). "
        "Correct answer is always (d) Sodium (salt/NaCl). DASH diet = low sodium + high potassium for hypertension. "
        "అధిక రక్తపోటుకు = సోడియం (ఉప్పు) తీసుకోవడం తగ్గించాలి. అధిక Na⁺ → నీటి నిలుపుదల → రక్త పరిమాణం పెరుగుతుంది → BP పెరుగుతుంది. (b)/(c) = ముద్రణ తప్పిదం — రెండూ 'Potassium' అని చూపుతాయి.",
        49
    ),
    # Q50
    (
        "What helps making the acidic food alkaline that is coming from the stomach?\nతెలుగు: జీర్ణాశయం (కడుపు) నుండి వచ్చే ఆమ్ల (acidic) ఆహారాన్ని క్షారంగా (alkaline) మార్చడానికి ఏది సహాయపడుతుంది?",
        "Pepsin / పెప్సిన్",
        "Gastric juice / జఠర రసం",
        "Hydrochloric acid / హైడ్రోక్లోరిక్ ఆమ్లం",
        "Bile juice / బైల్ జ్యూస్ (పైత్యరసం)",
        "D", "E",
        "BILE JUICE (secreted by liver, stored in gallbladder) = alkaline (pH 7.6–8.6, contains bile salts, bile pigments, cholesterol). "
        "When acidic CHYME (partially digested food, pH ~2) enters the DUODENUM from stomach → Bile juice (and pancreatic juice — also alkaline) neutralizes it → creates alkaline environment (pH ~7–8) required for intestinal enzymes to work. "
        "Bile also emulsifies fats → increases surface area for lipase. "
        "Pepsin = stomach enzyme (works in acidic pH); Gastric juice + HCl = make food MORE acidic; both wrong. "
        "పైత్యరసం (Bile): కాలేయం తయారు చేస్తుంది; పిత్తాశయంలో నిల్వ; క్షార స్వభావం (pH 7.6-8.6) → డ్యూయోడెనమ్‌లో ఆమ్ల chyme ను నిర్వీర్యం చేస్తుంది + కొవ్వులను emulsify చేస్తుంది.",
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
