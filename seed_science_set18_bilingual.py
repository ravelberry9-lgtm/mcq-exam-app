import sqlite3, os

SOURCE = 'Science_Set18_Human_System5'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    # ── Digestive System ──
    (
        "Which is the largest part of the human alimentary canal?\nతెలుగు: మానవ జీర్ణాశయ నాళంలో అతిపెద్ద భాగం ఏది?",
        "Stomach / జీర్ణాశయం", "Small intestine / చిన్న ప్రేగు",
        "Large intestine / పెద్ద ప్రేగు", "Esophagus / అన్నవాహిక",
        "B", "E",
        "SMALL INTESTINE = largest part of alimentary canal (~6.5 m long). Three parts: Duodenum (~25 cm), Jejunum (~2.5 m), Ileum (~3.6 m). Major absorption site. చిన్న ప్రేగు = ~6.5 మీటర్లు; జీర్ణాశయ నాళంలో అతిపెద్ద భాగం; ప్రధానంగా శోషణ జరుగుతుంది.", 1
    ),
    (
        "Which enzyme converts starch into maltose in the mouth?\nతెలుగు: నోటిలో పిండి పదార్థాన్ని మాల్టోజ్‌గా మార్చే ఎంజైమ్ ఏది?",
        "Pepsin / పెప్సిన్", "Trypsin / ట్రిప్సిన్",
        "Ptyalin (Salivary amylase) / ప్యాలిన్ (లాలాజల అమైలేస్)", "Lipase / లైపేస్",
        "C", "M",
        "PTYALIN (Salivary Amylase) in saliva converts STARCH → MALTOSE in the mouth. pH range 6.7-7.0. Pepsin (stomach, proteins), Trypsin (pancreatic, proteins), Lipase (fats). ప్యాలిన్ లాలాజలంలో ఉంటుంది; పిండిని మాల్టోజ్‌గా మారుస్తుంది.", 2
    ),
    (
        "The pH of gastric juice is approximately\nతెలుగు: జఠర రసం (gastric juice) యొక్క pH సుమారు ఎంత?",
        "1.5 - 3.5 / 1.5 - 3.5", "5.0 - 6.0 / 5.0 - 6.0",
        "7.0 - 7.4 / 7.0 - 7.4", "8.0 - 9.0 / 8.0 - 9.0",
        "A", "M",
        "Gastric juice pH = 1.5-3.5 (highly ACIDIC) due to HCl secreted by parietal cells. Helps digest proteins, kill bacteria, activate pepsin. Saliva pH ~6.7-7.0; Blood pH ~7.4. జఠర రసం pH = 1.5-3.5; HCl వల్ల అత్యంత ఆమ్లమైనది.", 3
    ),
    (
        "The bile is produced by which organ?\nతెలుగు: పైత్య రసం (bile) ఏ అవయవం నుండి ఉత్పత్తి అవుతుంది?",
        "Pancreas / క్లోమం", "Liver / కాలేయం",
        "Gall bladder / పిత్తాశయం", "Spleen / ప్లీహం",
        "B", "E",
        "BILE is produced by LIVER (hepatocytes) → stored in GALL BLADDER → released into duodenum. Contains bile salts that emulsify fats. No digestive enzymes in bile. పైత్య రసం కాలేయంలో ఉత్పత్తి; పిత్తాశయంలో నిల్వ; కొవ్వుల ఎమల్సిఫికేషన్ చేస్తుంది.", 4
    ),
    (
        "The largest gland in the human body is\nతెలుగు: మానవ శరీరంలో అతిపెద్ద గ్రంథి ఏది?",
        "Pancreas / క్లోమం", "Thyroid / థైరాయిడ్",
        "Liver / కాలేయం", "Adrenal / అడ్రినల్",
        "C", "E",
        "LIVER = largest gland in human body (~1.5 kg). Both EXOCRINE (bile) and ENDOCRINE (insulin-like growth factors) functions. Also largest internal organ. కాలేయం = అతిపెద్ద గ్రంథి (~1.5 kg); బాహ్య + అంతఃస్రావ గ్రంథి.", 5
    ),
    (
        "Vitamin B12 is absorbed in which part of the intestine?\nతెలుగు: విటమిన్ B12 ఏ ప్రేగు భాగంలో శోషణ అవుతుంది?",
        "Duodenum / ద్వాదశాంత్రం", "Jejunum / జెజునమ్",
        "Ileum / ఇలియమ్", "Colon / కోలన్",
        "C", "H",
        "Vitamin B12 (cobalamin) absorbed in ILEUM with help of INTRINSIC FACTOR (from stomach parietal cells). Deficiency → Pernicious anemia. B12 ఇలియమ్‌లో శోషణ; Intrinsic Factor అవసరం; లోపం = పెర్నిషియస్ అనీమియా.", 6
    ),
    (
        "The juice secreted by the pancreas contains which enzymes?\nతెలుగు: క్లోమం స్రవించే రసంలో ఏ ఎంజైమ్‌లు ఉంటాయి?",
        "Pepsin, Renin, Lipase / పెప్సిన్, రెనిన్, లైపేస్",
        "Trypsin, Lipase, Amylase / ట్రిప్సిన్, లైపేస్, అమైలేస్",
        "Ptyalin only / ప్యాలిన్ మాత్రమే",
        "HCl, Pepsin / HCl, పెప్సిన్",
        "B", "M",
        "PANCREATIC JUICE contains: TRYPSIN (proteins), CHYMOTRYPSIN, LIPASE (fats), AMYLASE (starch), Nucleases. Most important digestive juice. క్లోమ రసం: ట్రిప్సిన్, లైపేస్, అమైలేస్; ముఖ్యమైన జీర్ణ రసం.", 7
    ),

    # ── Excretory System ──
    (
        "The structural and functional unit of kidney is\nతెలుగు: మూత్రపిండం యొక్క నిర్మాణ మరియు క్రియాత్మక యూనిట్ ఏది?",
        "Neuron / న్యూరాన్", "Nephron / నెఫ్రాన్",
        "Glomerulus / గ్లోమెరులస్", "Alveolus / ఆల్వియోలస్",
        "B", "E",
        "NEPHRON = structural & functional unit of kidney. Each kidney has ~1 million nephrons. Parts: Bowman's capsule, Glomerulus, PCT, Loop of Henle, DCT, Collecting duct. నెఫ్రాన్ = మూత్రపిండ యూనిట్; ఒక్కో మూత్రపిండంలో ~10 లక్షలు.", 8
    ),
    (
        "Which of these is NOT a function of the kidney?\nతెలుగు: కింది వాటిలో మూత్రపిండం యొక్క విధి కానిది ఏది?",
        "Filtration of blood / రక్త వడపోత",
        "Production of urine / మూత్ర ఉత్పత్తి",
        "Production of bile / పైత్య రసం ఉత్పత్తి",
        "Regulation of blood pressure / రక్తపోటు నియంత్రణ",
        "C", "M",
        "Bile is produced by LIVER, NOT kidney. Kidney functions: filtration, urine formation, water/electrolyte balance, BP regulation (via renin), erythropoietin secretion, vitamin D activation. పైత్య రసం కాలేయం ఉత్పత్తి చేస్తుంది; మూత్రపిండం కాదు.", 9
    ),
    (
        "The yellow colour of urine is due to\nతెలుగు: మూత్రంలో పసుపు రంగుకు కారణం ఏది?",
        "Bilirubin / బిలిరూబిన్", "Urochrome / యూరోక్రోమ్",
        "Carotene / కెరోటిన్", "Melanin / మెలానిన్",
        "B", "M",
        "UROCHROME (yellow pigment) gives urine its yellow color. Derived from breakdown of hemoglobin. Bilirubin is in bile; gives yellow color in jaundice. మూత్రం పసుపు రంగు యూరోక్రోమ్ వల్ల; హిమోగ్లోబిన్ విచ్ఛిన్నం నుండి.", 10
    ),
    (
        "Excessive sugar in urine is called\nతెలుగు: మూత్రంలో అధిక చక్కెర ఉండడాన్ని ఏమంటారు?",
        "Glycosuria / గ్లైకోసురియా", "Hematuria / హిమటురియా",
        "Proteinuria / ప్రోటీనురియా", "Bacteriuria / బాక్టీరియూరియా",
        "A", "M",
        "GLYCOSURIA = sugar in urine; sign of DIABETES MELLITUS. Hematuria = blood in urine; Proteinuria = protein in urine; Bacteriuria = bacteria in urine. మూత్రంలో చక్కెర = గ్లైకోసురియా; మధుమేహం సూచిక.", 11
    ),

    # ── Respiratory System ──
    (
        "The exchange of gases in lungs takes place in\nతెలుగు: ఊపిరితిత్తులలో వాయువుల మార్పిడి ఎక్కడ జరుగుతుంది?",
        "Bronchi / బ్రాంకై", "Bronchioles / బ్రాంకియోల్స్",
        "Alveoli / ఆల్వియోలై", "Trachea / శ్వాసనాళం",
        "C", "E",
        "ALVEOLI (air sacs) = site of gas exchange. ~300 million alveoli in human lungs. Surface area ~70 m². O₂ enters blood, CO₂ leaves blood by diffusion across alveolar membrane. ఆల్వియోలైలో వాయు మార్పిడి; ~30 కోట్ల ఆల్వియోలై; ~70 చ.మీ. ఉపరితల వైశాల్యం.", 12
    ),
    (
        "The breathing rate of a normal adult at rest is\nతెలుగు: సాధారణ వయోజనుడి (విశ్రాంతిలో) శ్వాస రేటు ఎంత?",
        "8 - 10 per minute / నిమిషానికి 8-10",
        "12 - 20 per minute / నిమిషానికి 12-20",
        "25 - 30 per minute / నిమిషానికి 25-30",
        "35 - 40 per minute / నిమిషానికి 35-40",
        "B", "E",
        "Normal adult breathing rate at rest = 12-20 breaths per minute. Newborns: 30-60; Children: 20-30. Increases with exercise, fever, anxiety. వయోజనుడి శ్వాస రేటు = 12-20 / నిమిషం (విశ్రాంతిలో).", 13
    ),
    (
        "The vital capacity of human lungs is approximately\nతెలుగు: మానవ ఊపిరితిత్తుల యొక్క vital capacity సుమారు ఎంత?",
        "500 mL / 500 mL", "1500 mL / 1500 mL",
        "4500 mL / 4500 mL", "6000 mL / 6000 mL",
        "C", "H",
        "VITAL CAPACITY = ~4500-5000 mL = max air exhaled after max inhalation. = Tidal Volume (500 mL) + IRV (3000 mL) + ERV (1100 mL). Total Lung Capacity = ~6000 mL. Vital Capacity = ~4500 mL; మొత్తం ఊపిరితిత్తుల సామర్థ్యం ~6000 mL.", 14
    ),
    (
        "Hemoglobin combines with which gas to form carboxyhemoglobin?\nతెలుగు: కార్బోక్సీహిమోగ్లోబిన్ ఏర్పడటానికి హిమోగ్లోబిన్ ఏ వాయువుతో కలుస్తుంది?",
        "Oxygen / ఆక్సిజన్", "Carbon dioxide / కార్బన్ డయాక్సైడ్",
        "Carbon monoxide / కార్బన్ మోనాక్సైడ్", "Nitrogen / నైట్రోజన్",
        "C", "M",
        "CARBON MONOXIDE (CO) binds to hemoglobin 240x more strongly than O₂ → forms CARBOXYHEMOGLOBIN → blocks O₂ transport → suffocation. Hence CO poisoning is deadly. CO + హిమోగ్లోబిన్ = కార్బోక్సీహిమోగ్లోబిన్; O₂ కంటే 240 రెట్లు ఎక్కువ బంధం.", 15
    ),

    # ── Nervous System ──
    (
        "The largest part of the human brain is\nతెలుగు: మానవ మెదడులో అతిపెద్ద భాగం ఏది?",
        "Cerebellum / మస్తిష్క ఖండం", "Cerebrum / మస్తిష్కం",
        "Medulla oblongata / మెడుల్లా ఆబ్లాంగాటా", "Pons / పోన్స్",
        "B", "E",
        "CEREBRUM = largest part of brain (~85% of brain mass). Site of intelligence, memory, voluntary movement, sensory perception. Divided into 4 lobes: frontal, parietal, temporal, occipital. మస్తిష్కం = అతిపెద్ద భాగం (~85%); బుద్ధి, జ్ఞాపకశక్తి, స్వచ్ఛంద చలనం.", 16
    ),
    (
        "The number of cranial nerves in humans is\nతెలుగు: మానవులలో కపాల నాడుల సంఖ్య ఎంత?",
        "10 / 10", "12 / 12", "20 / 20", "31 / 31",
        "B", "E",
        "12 PAIRS of cranial nerves (originate from brain) + 31 pairs of spinal nerves. Cranial: I-Olfactory, II-Optic, III-Oculomotor, IV-Trochlear, V-Trigeminal, VI-Abducent, VII-Facial, VIII-Auditory, IX-Glossopharyngeal, X-Vagus, XI-Accessory, XII-Hypoglossal. 12 జతల కపాల నాడులు; 31 జతల వెన్ను నాడులు.", 17
    ),
    (
        "Reflex actions are controlled by\nతెలుగు: ప్రతిచర్యలు (reflex actions) దేని ద్వారా నియంత్రించబడతాయి?",
        "Cerebrum / మస్తిష్కం", "Spinal cord / వెన్నుపాము",
        "Cerebellum / మస్తిష్క ఖండం", "Medulla / మెడుల్లా",
        "B", "M",
        "REFLEX ACTIONS controlled by SPINAL CORD (not brain) — hence rapid and involuntary. Examples: knee-jerk, withdrawal from heat. Reflex arc: receptor → afferent → spinal cord → efferent → effector. ప్రతిచర్యలు వెన్నుపాము నియంత్రణలో; వేగవంతం + స్వచ్ఛందం కాదు.", 18
    ),
    (
        "The functional unit of the nervous system is\nతెలుగు: నాడీ వ్యవస్థ యొక్క క్రియాత్మక యూనిట్ ఏది?",
        "Nephron / నెఫ్రాన్", "Neuron / న్యూరాన్",
        "Axon / అక్షతంతువు", "Synapse / సినాప్స్",
        "B", "E",
        "NEURON = functional unit of nervous system. Parts: dendrites (receive signals), cell body, axon (transmits signals), synapse (gap with next neuron). Human brain has ~86 billion neurons. న్యూరాన్ = నాడీ వ్యవస్థ యూనిట్; మెదడులో ~86 బిలియన్.", 19
    ),
    (
        "Which part of the brain controls balance and posture?\nతెలుగు: మెదడులో సమతుల్యత (balance) మరియు భంగిమ (posture) నియంత్రించే భాగం ఏది?",
        "Cerebrum / మస్తిష్కం", "Cerebellum / మస్తిష్క ఖండం",
        "Medulla / మెడుల్లా", "Thalamus / థాలమస్",
        "B", "M",
        "CEREBELLUM = controls balance, posture, coordination of voluntary muscle movements. Located at back of brain. Damage → ataxia (loss of coordination). మస్తిష్క ఖండం = సమతుల్యత, భంగిమ, కండరాల సమన్వయం; మెదడు వెనుక భాగం.", 20
    ),

    # ── Endocrine System ──
    (
        "Insulin is produced by which cells in the pancreas?\nతెలుగు: క్లోమంలో ఇన్సులిన్ ఉత్పత్తి చేసే కణాలు ఏవి?",
        "Alpha cells / ఆల్ఫా కణాలు", "Beta cells / బీటా కణాలు",
        "Delta cells / డెల్టా కణాలు", "Gamma cells / గామా కణాలు",
        "B", "M",
        "INSULIN produced by BETA cells of ISLETS OF LANGERHANS in pancreas. Alpha cells → Glucagon. Delta → Somatostatin. Insulin reduces blood glucose; deficiency = Diabetes mellitus. బీటా కణాలు ఇన్సులిన్ ఉత్పత్తి (లాంగర్‌హాన్స్ ద్వీపాలలో); లోపం = మధుమేహం.", 21
    ),
    (
        "The 'master gland' of the human body is\nతెలుగు: మానవ శరీరంలో 'మాస్టర్ గ్రంథి' ఏది?",
        "Thyroid / థైరాయిడ్", "Pituitary / పిట్యూటరీ",
        "Adrenal / అడ్రినల్", "Pancreas / క్లోమం",
        "B", "E",
        "PITUITARY = 'master gland' — controls other endocrine glands (thyroid, adrenals, gonads). Located at base of brain. Produces: GH, TSH, ACTH, FSH, LH, PRL, ADH, oxytocin. పిట్యూటరీ = మాస్టర్ గ్రంథి; ఇతర గ్రంథులను నియంత్రిస్తుంది.", 22
    ),
    (
        "Thyroxine hormone is secreted by\nతెలుగు: థైరాక్సిన్ హార్మోన్ ఏ గ్రంథి స్రవిస్తుంది?",
        "Pituitary / పిట్యూటరీ", "Thyroid gland / థైరాయిడ్ గ్రంథి",
        "Adrenal gland / అడ్రినల్ గ్రంథి", "Pancreas / క్లోమం",
        "B", "E",
        "THYROXINE (T4) and TRIIODOTHYRONINE (T3) secreted by THYROID gland. Contains iodine. Regulates basal metabolic rate (BMR). Deficiency → Hypothyroidism, Goitre; Excess → Hyperthyroidism. థైరాక్సిన్ = థైరాయిడ్ గ్రంథి; అయోడిన్ కలిగి ఉంటుంది; BMR నియంత్రణ.", 23
    ),
    (
        "Goitre is caused by deficiency of\nతెలుగు: గాయిటర్ ఏ లోపం వల్ల వస్తుంది?",
        "Iron / ఇనుము", "Iodine / అయోడిన్",
        "Calcium / కాల్షియం", "Vitamin C / విటమిన్ C",
        "B", "E",
        "GOITRE (swelling of thyroid gland) caused by IODINE deficiency. Iodine needed to synthesize thyroxine. Hence iodized salt is recommended. గాయిటర్ = అయోడిన్ లోపం; థైరాక్సిన్ తయారీకి అయోడిన్ అవసరం.", 24
    ),
    (
        "Adrenaline (epinephrine) is secreted by\nతెలుగు: అడ్రినలిన్ (ఎపినెఫ్రిన్) ఏ భాగం స్రవిస్తుంది?",
        "Adrenal cortex / అడ్రినల్ కార్టెక్స్", "Adrenal medulla / అడ్రినల్ మెడుల్లా",
        "Pituitary / పిట్యూటరీ", "Hypothalamus / హైపోథాలమస్",
        "B", "M",
        "ADRENALINE (Epinephrine) — 'fight or flight' hormone — secreted by ADRENAL MEDULLA (inner part). Cortex secretes cortisol/aldosterone. Adrenaline: ↑heart rate, ↑BP, ↑glucose. అడ్రినలిన్ = అడ్రినల్ మెడుల్లా; 'fight or flight' హార్మోన్.", 25
    ),

    # ── Sensory Organs ──
    (
        "The ear has how many parts?\nతెలుగు: చెవికి ఎన్ని భాగాలు ఉన్నాయి?",
        "2 / 2", "3 / 3", "4 / 4", "5 / 5",
        "B", "E",
        "EAR has 3 parts: OUTER EAR (pinna + ear canal + tympanic membrane), MIDDLE EAR (malleus, incus, stapes ossicles), INNER EAR (cochlea + semicircular canals). చెవి = 3 భాగాలు; బాహ్య, మధ్య, అంతర చెవి.", 26
    ),
    (
        "Balance is maintained by which part of the ear?\nతెలుగు: చెవిలో సమతుల్యత నియంత్రణ ఏ భాగం చేస్తుంది?",
        "Pinna / కర్ణభేరి", "Cochlea / కోక్లియా",
        "Semicircular canals / అర్ధవృత్తాకార నాళాలు", "Eustachian tube / యూస్టేషియన్ నాళం",
        "C", "M",
        "SEMICIRCULAR CANALS in the inner ear maintain BALANCE and equilibrium. Cochlea is for hearing. Eustachian tube equalizes pressure. అర్ధవృత్తాకార నాళాలు సమతుల్యత; కోక్లియా వినికిడి; యూస్టేషియన్ గాలి పీడన సమతుల్యత.", 27
    ),
    (
        "Number of taste buds in human tongue is approximately\nతెలుగు: మానవ నాలుకలో రుచి కణాల సంఖ్య సుమారు ఎంత?",
        "100 / 100", "500 / 500", "1000 / 1000", "10000 / 10000",
        "D", "H",
        "TASTE BUDS in human tongue ~10,000 (some sources 2,000-8,000). 5 tastes: sweet, sour, salty, bitter, umami. Tip = sweet, sides = salty/sour, back = bitter. రుచి కణాలు ~10,000; 5 రకాల రుచులు.", 28
    ),
    (
        "The five basic tastes are\nతెలుగు: ఐదు ప్రాథమిక రుచులు ఏవి?",
        "Sweet, Sour, Salty, Bitter, Spicy / తీపి, పులుపు, ఉప్పు, చేదు, కారం",
        "Sweet, Sour, Salty, Bitter, Umami / తీపి, పులుపు, ఉప్పు, చేదు, ఉమామి",
        "Sweet, Salty, Spicy, Bitter, Hot / తీపి, ఉప్పు, కారం, చేదు, వేడి",
        "Sweet, Sour, Salty, Spicy, Cold / తీపి, పులుపు, ఉప్పు, కారం, చల్లని",
        "B", "M",
        "5 BASIC TASTES: SWEET, SOUR, SALTY, BITTER, UMAMI (savory/meaty). UMAMI added in 1985 from Japanese (means 'pleasant savory taste'). Spicy is NOT a taste — it's pain (TRP receptors). 5 రుచులు: తీపి, పులుపు, ఉప్పు, చేదు, ఉమామి; కారం రుచి కాదు.", 29
    ),
    (
        "Color blindness is the inability to distinguish\nతెలుగు: వర్ణాంధత్వం (color blindness) ఏ రంగులను గుర్తించలేకపోవడం?",
        "Red and Blue / ఎరుపు, నీలం", "Red and Green / ఎరుపు, ఆకుపచ్చ",
        "Blue and Yellow / నీలం, పసుపు", "Black and White / నలుపు, తెలుపు",
        "B", "M",
        "Most common COLOR BLINDNESS = RED-GREEN (Daltonism). X-linked recessive trait — affects males more (~8% of males vs 0.5% females). Due to defective cone cells in retina. వర్ణాంధత్వం = ఎరుపు-ఆకుపచ్చ; X-సంబంధిత; పురుషులకు ఎక్కువ.", 30
    ),

    # ── Vitamins, Deficiency Diseases ──
    (
        "Scurvy is caused by deficiency of\nతెలుగు: స్కర్వీ ఏ విటమిన్ లోపం వల్ల వస్తుంది?",
        "Vitamin A / విటమిన్ A", "Vitamin B / విటమిన్ B",
        "Vitamin C / విటమిన్ C", "Vitamin D / విటమిన్ D",
        "C", "E",
        "SCURVY = Vitamin C (Ascorbic Acid) deficiency. Symptoms: bleeding gums, slow wound healing, joint pain. Sources: citrus fruits, amla, guava. స్కర్వీ = విటమిన్ C లోపం; చిగుళ్ళ రక్తస్రావం, గాయాలు మెల్లగా మానటం.", 31
    ),
    (
        "Beriberi disease is caused by deficiency of\nతెలుగు: బెరిబెరి వ్యాధి ఏ విటమిన్ లోపం వల్ల వస్తుంది?",
        "Vitamin A / విటమిన్ A", "Vitamin B1 (Thiamine) / విటమిన్ B1 (థయామిన్)",
        "Vitamin C / విటమిన్ C", "Vitamin K / విటమిన్ K",
        "B", "M",
        "BERIBERI = Vitamin B1 (Thiamine) deficiency. Types: Wet (heart failure) & Dry (nervous system). Sources: whole grains, pulses, nuts, meat. బెరిబెరి = B1 (థయామిన్) లోపం; నాడీ + హృదయ సమస్యలు.", 32
    ),
    (
        "Night blindness is caused by deficiency of\nతెలుగు: రాత్రి అంధత్వం ఏ విటమిన్ లోపం?",
        "Vitamin A / విటమిన్ A", "Vitamin B / విటమిన్ B",
        "Vitamin D / విటమిన్ D", "Vitamin E / విటమిన్ E",
        "A", "E",
        "NIGHT BLINDNESS (Nyctalopia) = Vitamin A deficiency. Severe deficiency → Xerophthalmia → blindness. Sources: carrots, spinach, papaya, liver, eggs. రాత్రి అంధత్వం = విటమిన్ A లోపం; క్యారెట్, ఆకు కూరలు.", 33
    ),
    (
        "Rickets in children is caused by deficiency of\nతెలుగు: పిల్లలలో రికెట్స్ ఏ విటమిన్ లోపం వల్ల?",
        "Vitamin A / విటమిన్ A", "Vitamin C / విటమిన్ C",
        "Vitamin D / విటమిన్ D", "Vitamin K / విటమిన్ K",
        "C", "E",
        "RICKETS (children) and OSTEOMALACIA (adults) = Vitamin D deficiency. Causes soft, weak bones, bow legs. Vitamin D made in skin via sunlight. Also calcium absorption needs vitamin D. రికెట్స్ = విటమిన్ D లోపం; ఎముకలు బలహీనం; సూర్యరశ్మిలో శరీరం తయారు చేస్తుంది.", 34
    ),
    (
        "Goitre, mental retardation in children and cretinism are caused by deficiency of\nతెలుగు: గాయిటర్, పిల్లలలో మానసిక వెనుకబాటు, క్రెటినిజం ఏ లోపం వల్ల?",
        "Iron / ఇనుము", "Iodine / అయోడిన్",
        "Calcium / కాల్షియం", "Zinc / జింక్",
        "B", "M",
        "IODINE deficiency → Goitre (adults), Cretinism (children — stunted growth + mental retardation). Iodine needed for thyroxine. Fortified salt = iodized salt to prevent. అయోడిన్ లోపం = గాయిటర్ + క్రెటినిజం; అయోడైజ్డ్ సాల్ట్ నివారణ.", 35
    ),
    (
        "Anemia is generally caused by deficiency of\nతెలుగు: రక్తహీనత (anemia) సాధారణంగా ఏ లోపం వల్ల?",
        "Iron / ఇనుము", "Calcium / కాల్షియం",
        "Sodium / సోడియం", "Potassium / పొటాషియం",
        "A", "E",
        "ANEMIA (low hemoglobin) most commonly due to IRON deficiency — required for Hb synthesis. Sources: green leafy vegetables, red meat, dates, jaggery. Pregnant women particularly susceptible. రక్తహీనత = ఇనుము లోపం; హిమోగ్లోబిన్ తయారీకి ఇనుము అవసరం.", 36
    ),
    (
        "Vitamin K is mainly required for\nతెలుగు: విటమిన్ K ప్రధానంగా దేనికి అవసరం?",
        "Vision / దృష్టి", "Blood clotting / రక్తం గడ్డకట్టడం",
        "Bone formation / ఎముకల ఏర్పాటు", "Energy production / శక్తి ఉత్పత్తి",
        "B", "M",
        "VITAMIN K essential for BLOOD CLOTTING — needed to synthesize PROTHROMBIN (clotting factor II) and other clotting factors. Source: green leafy vegetables, made by gut bacteria. విటమిన్ K = రక్తం గడ్డకట్టడం; ప్రోత్రోంబిన్ తయారీకి అవసరం.", 37
    ),

    # ── Bones and Muscles ──
    (
        "Total number of bones in the adult human body is\nతెలుగు: వయోజన మానవ శరీరంలో మొత్తం ఎముకల సంఖ్య ఎంత?",
        "200 / 200", "206 / 206", "300 / 300", "350 / 350",
        "B", "E",
        "ADULT human body = 206 bones. Newborn has ~270-300 (many fuse during growth). Axial skeleton (skull, vertebrae, ribs) = 80; Appendicular (limbs) = 126. వయోజనుడి = 206 ఎముకలు; నవజాత శిశువు = ~270-300.", 38
    ),
    (
        "The longest bone in the human body is\nతెలుగు: మానవ శరీరంలో అతిపెద్ద ఎముక ఏది?",
        "Tibia / టిబియా", "Femur (thigh bone) / తొడ ఎముక",
        "Humerus / హ్యూమరస్", "Sternum / ఉరోస్థి",
        "B", "E",
        "FEMUR (thigh bone) = longest, strongest, heaviest bone in human body. Length ~26-27% of height. Stapes (ear) = smallest bone. తొడ ఎముక (ఫీమర్) = అతిపెద్ద ఎముక; కర్ణ స్టేపీస్ = అతిచిన్న.", 39
    ),
    (
        "The smallest bone in the human body is\nతెలుగు: మానవ శరీరంలో అతిచిన్న ఎముక ఏది?",
        "Stapes (ear) / స్టేపీస్ (చెవి)", "Coccyx / కాక్సిక్స్",
        "Phalanges / ఫాలాంజెస్", "Patella / మోకాలి చిప్ప",
        "A", "M",
        "STAPES = smallest bone in human body (~3 mm). Part of middle ear ossicles: Malleus, Incus, Stapes. Transmits sound vibrations to inner ear. స్టేపీస్ = అతిచిన్న ఎముక (~3 mm); మధ్య చెవిలో; ధ్వని తరంగాలను అంతర చెవికి.", 40
    ),
    (
        "How many vertebrae are present in the human spinal column?\nతెలుగు: మానవ వెన్నెముకలో ఎన్ని వెన్నెముకలు ఉన్నాయి?",
        "26 / 26", "33 / 33", "12 / 12", "20 / 20",
        "B", "M",
        "33 vertebrae in spinal column: Cervical (7), Thoracic (12), Lumbar (5), Sacral (5 fused into sacrum), Coccygeal (4 fused into coccyx). Adult sometimes counted as 26 (with fusion). వెన్నెముకలు: 7+12+5+5+4 = 33; ఫ్యూజ్ తర్వాత 26.", 41
    ),
    (
        "The largest muscle in the human body is\nతెలుగు: మానవ శరీరంలో అతిపెద్ద కండరం ఏది?",
        "Biceps / బైసెప్స్", "Gluteus maximus / గ్లూటియస్ మాక్సిమస్",
        "Hamstring / హ్యామ్‌స్ట్రింగ్", "Quadriceps / క్వాడ్రిసెప్స్",
        "B", "M",
        "GLUTEUS MAXIMUS (buttock muscle) = largest, strongest muscle in human body. Helps in walking, climbing, standing erect. Stapedius (middle ear) = smallest muscle. గ్లూటియస్ మాక్సిమస్ = అతిపెద్ద కండరం; నడక, నిలబడటం.", 42
    ),

    # ── Reproductive System ──
    (
        "The site of fertilization in human female is\nతెలుగు: మానవ స్త్రీలో ఫలదీకరణ (fertilization) జరిగే స్థలం ఏది?",
        "Ovary / అండాశయం", "Fallopian tube / గర్భ నాళం",
        "Uterus / గర్భాశయం", "Vagina / యోని",
        "B", "M",
        "FERTILIZATION occurs in the AMPULLA of FALLOPIAN TUBE (oviduct). Sperm meets ovum here. Implantation occurs in uterus. Ovum released from ovary travels through fallopian tube. ఫలదీకరణ = గర్భ నాళంలో (ఆంపుల్లా); గర్భధారణ గర్భాశయంలో.", 43
    ),
    (
        "The normal duration of human pregnancy is\nతెలుగు: మానవ గర్భధారణ సాధారణ కాలవ్యవధి ఎంత?",
        "270 days / 270 రోజులు", "280 days (40 weeks) / 280 రోజులు (40 వారాలు)",
        "300 days / 300 రోజులు", "360 days / 360 రోజులు",
        "B", "E",
        "HUMAN PREGNANCY = ~280 days (40 weeks) from last menstrual period = 9 months 7 days. 3 trimesters of ~13 weeks each. మానవ గర్భధారణ = 280 రోజులు (40 వారాలు); 3 త్రైమాసికాలు.", 44
    ),
    (
        "The sex chromosomes in human male are\nతెలుగు: మానవ పురుషుడిలో లింగ క్రోమోజోములు ఏవి?",
        "XX / XX", "XY / XY", "YY / YY", "XYY / XYY",
        "B", "E",
        "MALE = XY chromosomes. FEMALE = XX. Sex determined by sperm (X or Y) at fertilization. Total chromosomes = 46 (23 pairs) including 22 autosomes + 1 sex pair. పురుషుడు = XY; స్త్రీ = XX; మొత్తం 46 క్రోమోజోములు.", 45
    ),

    # ── Heart and Circulation ──
    (
        "Number of chambers in human heart is\nతెలుగు: మానవ హృదయంలో ఎన్ని గదులు ఉన్నాయి?",
        "2 / 2", "3 / 3", "4 / 4", "5 / 5",
        "C", "E",
        "Human heart has 4 CHAMBERS: 2 atria (upper) + 2 ventricles (lower). Right side: deoxygenated blood (to lungs); Left side: oxygenated blood (to body). Left ventricle thickest (pumps to whole body). మానవ హృదయం = 4 గదులు; కుడి = డీఆక్సిజనేటెడ్; ఎడమ = ఆక్సిజనేటెడ్.", 46
    ),
    (
        "The normal heart rate of an adult at rest is\nతెలుగు: విశ్రాంతిలో వయోజనుడి సాధారణ హృదయ స్పందన ఎంత?",
        "40-60 / 40-60", "60-100 per minute / నిమిషానికి 60-100",
        "100-120 / 100-120", "150-180 / 150-180",
        "B", "E",
        "Adult resting heart rate = 60-100 bpm. Bradycardia < 60; Tachycardia > 100. Athletes can have 40-60 (efficient heart). Newborns: 100-160. వయోజనుడి హృదయ రేటు = 60-100/నిమిషం; క్రీడాకారులకు తక్కువ.", 47
    ),
    (
        "Blood pressure is normally measured in which units?\nతెలుగు: రక్తపోటును సాధారణంగా ఏ ప్రమాణాలలో కొలుస్తారు?",
        "mg/dL / mg/dL", "mmHg / mmHg",
        "kPa / kPa", "mL/min / mL/min",
        "B", "E",
        "BLOOD PRESSURE measured in mmHg (millimeters of mercury). Normal = 120/80 (systolic/diastolic). Hypertension > 140/90. Hypotension < 90/60. Instrument: sphygmomanometer. రక్తపోటు = mmHg; సాధారణ 120/80; SPM యంత్రం.", 48
    ),
    (
        "The instrument used to measure blood pressure is\nతెలుగు: రక్తపోటును కొలవడానికి వాడే పరికరం ఏది?",
        "Stethoscope / స్టెథోస్కోప్", "Sphygmomanometer / స్ఫిగ్మోమానోమీటర్",
        "Barometer / బారోమీటర్", "Thermometer / థర్మామీటర్",
        "B", "E",
        "SPHYGMOMANOMETER measures blood pressure. Stethoscope used to hear Korotkoff sounds during measurement. Barometer for atmospheric pressure. స్ఫిగ్మోమానోమీటర్ = రక్తపోటు కొలత; స్టెథోస్కోప్ = హృదయ ధ్వనులు వినడానికి.", 49
    ),
    (
        "The smallest blood vessels in the body are\nతెలుగు: శరీరంలో అతి చిన్న రక్తనాళాలు ఏవి?",
        "Arteries / ధమనులు", "Veins / సిరలు",
        "Capillaries / కేశనాళికలు", "Aorta / మహాధమని",
        "C", "M",
        "CAPILLARIES = smallest blood vessels (~5-10 micrometers diameter). One-cell thick walls allow gas/nutrient exchange between blood and tissues. Connect arterioles to venules. కేశనాళికలు = అతిచిన్న రక్తనాళాలు (~5-10 μm); కణాలతో మార్పిడి.", 50
    ),
]
