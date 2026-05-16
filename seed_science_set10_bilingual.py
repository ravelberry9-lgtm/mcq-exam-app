import sqlite3, os

SOURCE = 'Science_Set10_Human_System1'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    (
        'Which of the following organs are NOT parts of the Alimentary canal\nతెలుగు: కింది అవయవాలలో ఆహార నాళంలో (Alimentary canal) భాగం కానివి ఏవి',
        'Colon and rectum / పెద్దప్రేగు మరియు పురీషనాళం (Colon and rectum)',
        'Stomach and intestine / జీర్ణాశయం మరియు ప్రేగు',
        'Liver and pancreas / కాలేయం మరియు క్లోమం (Liver and pancreas)',
        'Buccal cavity and Oesophagus / ఆస్యకుహరం మరియు ఆహారవాహిక (Buccal cavity and Oesophagus)',
        'C',
        'M',
        '',
        2
    ),
    (
        'Parathyroid – Thyroxine\nతెలుగు: కింది జతలలో ఏది/ఏవి సరిగ్గా జతపరచబడ్డాయి?గ్రంథి - హార్మోన్లు',
        '1 only',
        '1 and 2',
        '3 only',
        '1, 2 and 3',
        'A',
        'M',
        '',
        3
    ),
    (
        'Shortsightedness is due to\nతెలుగు: హ్రస్వదృష్టి (Shortsightedness/Myopia) దేని వలన వస్తుంది',
        'Shifting of the iris / ఐరిస్ స్థానం మారడం వలన',
        'Weaker muscles / కండరాలు బలహీనపడటం వలన',
        'Elongation of eye balls / కనుగుడ్లు సాగడం/పొడవు పెరగడం వలన (Elongation of eye balls)',
        'Weakening of the retina / రెటీనా బలహీనపడటం వలన',
        'C',
        'M',
        '',
        3
    ),
    (
        "Alzheimer's disease in human beings is characterized by the degeneration of\nతెలుగు: మానవులలో అల్జీమర్స్ వ్యాధి (Alzheimer's disease) కింది ఏ కణాల క్షీణత (degeneration) వల్ల వస్తుంది",
        'Kidney cells / మూత్రపిండాల కణాలు',
        'Nerve cells / నాడీ కణాలు',
        'Brain cells / మెదడు కణాలు (Brain cells)',
        'Liver cells / కాలేయ కణాలు',
        'C',
        'M',
        '',
        4
    ),
    (
        'Which is a small conical gland-like structure of unknown function found in the brain of vertebrates\nతెలుగు: సకశేరుకాల (vertebrates) మెదడులో కనిపించే, ఖచ్చితమైన విధి తెలియని చిన్న శంఖాకార గ్రంథి లాంటి నిర్మాణం ఏది',
        'Cerebellum / సెరిబెల్లమ్ (అనుమస్తిష్కం)',
        'Medulla / మెడుల్లా (మజ్జాముఖం)',
        'Pineal body / పీనియల్ దేహం (Pineal body)',
        'Pleura body / ప్లూరా దేహం',
        'C',
        'M',
        '',
        5
    ),
    (
        'The yellow color of urine is due to the presence of\nతెలుగు: మూత్రం పసుపు రంగులో ఉండటానికి కారణమైన పదార్థం ఏది',
        'Bile / బైల్ (పైత్యరసం)',
        'Lymph / శోషరసం (Lymph)',
        'Cholesterol / కొలెస్ట్రాల్',
        'Urochrome / యూరోక్రోమ్ (Urochrome)',
        'D',
        'M',
        '',
        6
    ),
    (
        'Target tissue of insulin is\nతెలుగు: ఇన్సులిన్ (insulin) యొక్క లక్ష్య కణజాలం (Target tissue) ఏది',
        'Red Blood Cell / ఎర్ర రక్త కణాలు',
        'Kidney tissues / మూత్రపిండ కణజాలాలు',
        'Small intestinal tissues / చిన్న ప్రేగు కణజాలాలు',
        'None of the above / పైవేవీ కావు (None of the above)',
        'D',
        'M',
        '',
        7
    ),
    (
        'Which of the following is essential for blood clotting\nతెలుగు: రక్తం గడ్డకట్టడానికి కింది వాటిలో ఏది అత్యవసరం',
        'RBC / ఎర్ర రక్త కణాలు (RBC)',
        'WBC / తెల్ల రక్త కణాలు (WBC)',
        'Blood platelets / రక్త ఫలకికలు (Blood platelets)',
        'Lymph / శోషరసం (Lymph)',
        'C',
        'M',
        '',
        8
    ),
    (
        'The tooth with three roots is\nతెలుగు: మూడు మూలాలు (Three roots) కలిగిన దంతం ఏది',
        'Molar / మోలార్ (చార్వణకం/Molar)',
        'Pre-molar / ప్రీ-మోలార్ (అగ్రచార్వణకం)',
        'Incisor / ఇన్సిజర్ (కుంతకం)',
        'Canine / కనైన్ (రదనిక)',
        'A',
        'M',
        '',
        9
    ),
    (
        'Which one of the following is the natural auxin\nతెలుగు: కింది వాటిలో సహజ ఆక్సిన్ (Natural auxin) ఏది',
        'NAA / NAA',
        'IAA / IAA (Indole-3-acetic acid)',
        '2,4-D / 2,4-D',
        'IBA / IBA',
        'B',
        'M',
        '',
        10
    ),
    (
        'Which part of the bifocal lens facilitates near vision\nతెలుగు: బైఫోకల్ కటకంలో (bifocal lens) దగ్గరి చూపును సులభతరం చేసే భాగం ఏది',
        'Lower part with concave lens / పుటాకార కటకంతో ఉన్న కింది భాగం',
        'Upper part with convex lens / కుంభాకార కటకంతో ఉన్న పై భాగం',
        'Lower part with convex lens / కుంభాకార కటకంతో ఉన్న కింది భాగం (Lower part with convex lens)',
        'Upper part with concave lens / పుటాకార కటకంతో ఉన్న పై భాగం',
        'C',
        'M',
        '',
        11
    ),
    (
        'A person will have brown eyes, blue eyes or black eyes depending upon the particular pigment present in the\nతెలుగు: ఒక వ్యక్తి కళ్ళు గోధుమ, నీలం లేదా నలుపు రంగులో ఉండటం అనేది దేనిలో ఉండే వర్ణద్రవ్యం (pigment) పై ఆధారపడి ఉంటుంది',
        'Pupil / కనుపాప (Pupil)',
        'Cornea / కార్నియా (శుక్లపటలం)',
        'Iris / ఐరిస్ (Iris / కృష్ణపటలం)',
        'Choroid / కోరాయిడ్ (రక్తపటలం)',
        'C',
        'M',
        '',
        12
    ),
    (
        'Which key event in the life cycle of Plasmodium causes rupture of red blood cells\nతెలుగు: ప్లాస్మోడియం (మలేరియా పరాన్నజీవి) జీవిత చక్రంలో ఎర్ర రక్త కణాలు పగిలిపోవడానికి కారణమయ్యే ముఖ్యమైన సంఘటన ఏది',
        'Maturation and multiplication of merozoites inside the RBCs / RBC ల లోపల మెరోజోయిట్\u200cల పరిపక్వత మరియు గుణకారం',
        'Sexual reproduction inside mosquitoes in the erythrocytes / ఎరిత్రోసైట్\u200cలలోని దోమల లోపల లైంగిక పునరుత్పత్తి',
        'Conversion into sporozoites / స్పోరోజోయిట్\u200cలుగా మారడం',
        'Multiplication inside liver cells / కాలేయ కణాల లోపల గుణకారం',
        'A',
        'M',
        '',
        13
    ),
    (
        'A color-blind person has difficulty in distinguishing between which colors\nతెలుగు: వర్ణాంధత్వం (Color-blindness) ఉన్న వ్యక్తి ఏ రంగుల మధ్య తేడాను గుర్తించడంలో ఇబ్బంది పడతాడు',
        'Black and Blue / నలుపు మరియు నీలం',
        'Green and Violet / ఆకుపచ్చ మరియు వయొలెట్',
        'White and Yellow / తెలుపు మరియు పసుపు',
        'Green and Red / ఆకుపచ్చ మరియు ఎరుపు (Green and Red)',
        'D',
        'M',
        '',
        14
    ),
    (
        'In absence of ADH, the disease caused is\nతెలుగు: ADH (యాంటీ డైయూరిటిక్ హార్మోన్) లోపం వల్ల వచ్చే వ్యాధి ఏది',
        'Diabetes mellitus / డయాబెటిస్ మెల్లిటస్',
        'Diabetes insipidus / డయాబెటిస్ ఇన్\u200cసిపిడస్ (Diabetes insipidus / అతిమూత్ర వ్యాధి)',
        'Oliguria / ఒలిగురియా',
        'Acromegaly / ఆక్రోమెగాలీ',
        'B',
        'M',
        '',
        15
    ),
    (
        'Reflex action in the body is controlled by\nతెలుగు: శరీరంలోని అసంకల్పిత ప్రతీకార చర్య (Reflex action) దేని ద్వారా నియంత్రించబడుతుంది',
        'Sensory nerves / జ్ఞాన నాడులు',
        'Central nervous system / కేంద్ర నాడీ వ్యవస్థ',
        'Motor nerves / చాలక నాడులు (Motor nerves)',
        'Sympathetic nervous system / సహానుభూత నాడీ వ్యవస్థ',
        'C',
        'M',
        '',
        16
    ),
    (
        'What is the maximum limit of sound intensity in decibel units beyond which a person cannot hear\nతెలుగు: ఒక వ్యక్తి వినలేని/తట్టుకోలేని గరిష్ట ధ్వని తీవ్రత (డెసిబెల్ యూనిట్లలో) పరిమితి ఎంత',
        '50 / 50',
        '70 / 70',
        '85 / 85',
        '95 / 95',
        'C',
        'M',
        '',
        17
    ),
    (
        'Which of the following glands is situated beneath the brain and whose oversecretion produces giant-size children\nతెలుగు: మెదడు కింద భాగంలో ఉండి, దాని అధిక స్రావం వల్ల పిల్లలు అతిభారీ ఆకారంలో (giant-size) పెరగడానికి కారణమయ్యే గ్రంథి ఏది',
        'Pituitary / పిట్యూటరీ (పీయూష గ్రంథి)',
        'Thyroid / థైరాయిడ్',
        'Adrenal / అడ్రినల్ (అధివృక్క గ్రంథి)',
        'Pancreas / ప్యాంక్రియాస్ (క్లోమం)',
        'A',
        'M',
        '',
        18
    ),
    (
        'There are approximately......... muscles in the human body.\nతెలుగు: మానవ శరీరంలో సుమారుగా ......... కండరాలు ఉన్నాయి.',
        '200 / 200',
        '350 / 350',
        '500 / 500',
        '700 / 700',
        'D',
        'M',
        '',
        19
    ),
    (
        'The organ which destroys worn-out RBCs in the body of a vertebrate is\nతెలుగు: సకశేరుకాల శరీరంలో పాతబడిన/పాడైన ఎర్ర రక్త కణాలను (RBCs) నాశనం చేసే అవయవం ఏది',
        'Pancreas / క్లోమం',
        'Liver / కాలేయం',
        'Bone marrow / ఎముక మజ్జ',
        'Spleen / ప్లీహం (Spleen)',
        'D',
        'M',
        '',
        20
    ),
    (
        'A person born with inner ear missing\nతెలుగు: పుట్టుకతోనే లోపలి చెవి (inner ear) లేకుండా పుట్టిన వ్యక్తి:',
        'Would never be able to hear sound / శబ్దాన్ని ఎప్పటికీ వినలేడు',
        'Could only hear a loud explosion / పెద్ద పేలుడు శబ్దాన్ని మాత్రమే వినగలడు',
        'Would be able to hear only with an electronic hearing aid / ఎలక్ట్రానిక్ వినికిడి పరికరంతో మాత్రమే వినగలడు',
        'None of these / ఇవేవీ కావు',
        'A',
        'M',
        '',
        21
    ),
    (
        'Which of the following is a membrane that protects the developing embryo from desiccation\nతెలుగు: అభివృద్ధి చెందుతున్న పిండాన్ని ఎండిపోకుండా (desiccation) రక్షించే పొర ఏది',
        'Amnion / ఉల్బం (Amnion)',
        'Allantois / అల్లంటోయిస్',
        'Chorion / పరాయువు (Chorion)',
        'Yolk sac / సొన సంచి (Yolk sac)',
        'A',
        'M',
        '',
        22
    ),
    (
        'Pituitary gland is located in -\nతెలుగు: పిట్యూటరీ గ్రంథి ఎక్కడ ఉంటుంది',
        'Intestine / ప్రేగు',
        'Liver / కాలేయం',
        'Kidney / మూత్రపిండం',
        'Brain / మెదడు (Brain)',
        'D',
        'M',
        '',
        23
    ),
    (
        'Which of the following combinations of chromosomes is present in males\nతెలుగు: కింది వాటిలో పురుషులలో ఉండే క్రోమోజోమ్\u200cల కలయిక ఏది',
        'XX / XX',
        'XXX / XXX',
        'XY / XY',
        'XYX / XYX',
        'C',
        'M',
        '',
        24
    ),
    (
        'The saliva helps in the digestion of\nతెలుగు: లాలాజలం కింది వాటిలో దేనిని జీర్ణం చేయడంలో సహాయపడుతుంది',
        'Proteins / ప్రోటీన్లు',
        'Fats / కొవ్వులు',
        'Fibers / ఫైబర్స్ (పీచుపదార్థాలు)',
        'Starch / పిండిపదార్థం (Starch)',
        'D',
        'M',
        '',
        25
    ),
    (
        'Detection of Rh factor is an example of\nతెలుగు: Rh ఫ్యాక్టర్\u200cను గుర్తించడం అనేది కింది వాటిలో దేనికి ఉదాహరణ',
        'Enzymatic reaction / ఎంజైమాటిక్ చర్య',
        'Chemical reaction / రసాయన చర్య',
        'Phagocytic reaction / ఫాగోసైటిక్ చర్య',
        'Immunologic reaction / రోగనిరోధక చర్య (Immunologic reaction)',
        'D',
        'M',
        '',
        26
    ),
    (
        'Inside the body, blood does not coagulate due to the presence of\nతెలుగు: శరీరంలో రక్తం గడ్డకట్టకుండా ఉండటానికి కారణమైన పదార్థం ఏది',
        'Fibrin / ఫైబ్రిన్',
        'Hemoglobin / హిమోగ్లోబిన్',
        'Heparin / హెపారిన్ (Heparin)',
        'Thromboplastin / థ్రోంబోప్లాస్టిన్',
        'C',
        'M',
        '',
        27
    ),
    (
        "Biological death of a patient means death of tissues of the\nతెలుగు: ఒక రోగి యొక్క 'జీవ మరణం' (Biological death) అంటే ఏ అవయవ కణజాలాలు చనిపోవడం",
        'Kidney / మూత్రపిండాలు',
        'Heart / గుండె',
        'Lungs / ఊపిరితిత్తులు',
        'Brain / మెదడు (Brain)',
        'D',
        'M',
        '',
        28
    ),
    (
        "Radial keratotomy, a surgical procedure, is used to cure\nతెలుగు: 'రేడియల్ కెరటోటమీ' అనే శస్త్రచికిత్సా విధానాన్ని దేనిని నయం చేయడానికి ఉపయోగిస్తారు",
        'Cataract / కంటిశుక్లం (Cataract)',
        'Myopia / మయోపియా (హ్రస్వదృష్టి / Myopia)',
        'Astigmatism / ఆస్టిగ్మాటిజం',
        'Hypermetropia / హైపర్\u200cమెట్రోపియా (దీర్ఘదృష్టి)',
        'B',
        'M',
        '',
        29
    ),
    (
        'Lymph vessels of human beings are inhabited by\nతెలుగు: మానవుల శోషరస నాళాలలో (Lymph vessels) నివసించే పరాన్నజీవి ఏది',
        'Plasmodium / ప్లాస్మోడియం',
        'Tapeworm / బద్దెపురుగు (Tapeworm)',
        'Wuchereria / వుచెరేరియా (Wuchereria - ఫైలేరియా పురుగు)',
        'Euglena / యూగ్లీనా',
        'C',
        'M',
        '',
        30
    ),
    (
        'The pitch of the voice of women is generally\nతెలుగు: స్త్రీల గొంతు యొక్క పిచ్ (శృతి) సాధారణంగా ఎలా ఉంటుంది',
        'Same as that of men / పురుషులతో సమానంగా ఉంటుంది',
        'Higher than that of men / పురుషుల కంటే ఎక్కువగా ఉంటుంది (Higher than that of men)',
        'Much lower than that of men / పురుషుల కంటే చాలా తక్కువగా ఉంటుంది',
        'None of these / ఇవేవీ కావు',
        'B',
        'M',
        '',
        31
    ),
    (
        '______ is the smallest gland in human body.\nతెలుగు: మానవ శరీరంలో అత్యంత చిన్న గ్రంథి ఏది',
        'Parotid gland / పెరోటిడ్ గ్రంథి',
        'Apocrine sweat gland / అపోక్రైన్ చెమట గ్రంథి',
        'Pineal gland / పీనియల్ గ్రంథి (Pineal gland)',
        "Ebner's gland / ఎబ్నర్స్ గ్రంథి",
        'C',
        'M',
        '',
        32
    ),
    (
        'The normal temperature of the human body on the Kelvin scale is\nతెలుగు: కెల్విన్ స్కేల్\u200cపై మానవ శరీరం సాధారణ ఉష్ణోగ్రత ఎంత',
        '280 / 280',
        '290 / 290',
        '300 / 300',
        '310 / 310',
        'D',
        'M',
        '',
        33
    ),
    (
        'Clotting of blood vessels is called\nతెలుగు: రక్త నాళాలలో రక్తం గడ్డకట్టడాన్ని ఏమంటారు',
        'Thrombosis / థ్రాంబోసిస్ (Thrombosis)',
        'Rheumatism / రుమాటిజం',
        'Agglutination / అగ్లుటినేషన్',
        'Fibrosis / ఫైబ్రోసిస్',
        'A',
        'M',
        '',
        34
    ),
    (
        'Blood group of an individual is controlled by\nతెలుగు: ఒక వ్యక్తి యొక్క రక్తపు గ్రూపు (Blood group) దేని ద్వారా నియంత్రించబడుతుంది',
        'Shape of RBC / RBC ఆకారం',
        'Shape of WBC / WBC ఆకారం',
        'Genes / జన్యువులు (Genes)',
        'Hemoglobin / హిమోగ్లోబిన్',
        'C',
        'M',
        '',
        35
    ),
    (
        'Which of the following forms an irreversible complex with hemoglobin of blood\nతెలుగు: కింది వాటిలో ఏది రక్తంలోని హిమోగ్లోబిన్\u200cతో తిరిగి వేరుకాని (irreversible) సమ్మేళనాన్ని ఏర్పరుస్తుంది',
        'Carbon monoxide / కార్బన్ మోనాక్సైడ్',
        'Carbon dioxide / కార్బన్ డైయాక్సైడ్',
        'Pure nitrogen gas / స్వచ్ఛమైన నైట్రోజన్ వాయువు',
        'A mixture of carbon dioxide and helium / కార్బన్ డైయాక్సైడ్ మరియు హీలియం మిశ్రమం',
        'A',
        'M',
        '',
        36
    ),
    (
        "The term 'complementary' in the context of DNA refers to which of the following properties\nతెలుగు: DNA సందర్భంలో 'కాంప్లిమెంటరీ' (పరిపూరకమైన) అనే పదం కింది ఏ లక్షణాన్ని సూచిస్తుంది",
        'Identical chemical composition of both strands / రెండు పోచల (strands) ఒకే రసాయన కూర్పు',
        'Parallel orientation of nucleotide chains / న్యూక్లియోటైడ్ గొలుసుల సమాంతర ధోరణి',
        'Matching number of sugar-phosphate units / చక్కెర-ఫాస్ఫేట్ యూనిట్ల సరిపోలే సంఖ్య',
        'Hydrogen bonding potential based on base specificity / క్షారాల విశిష్టత ఆధారంగా హైడ్రోజన్ బంధ సామర్థ్యం (Hydrogen bonding potential based on base specificity)',
        'D',
        'M',
        '',
        37
    ),
    (
        'Lungs are situated in\nతెలుగు: ఊపిరితిత్తులు ఎక్కడ అమరి ఉంటాయి',
        'Buccal cavity / ఆస్య కుహరం',
        'Pericardial cavity / పెరికార్డియల్ కుహరం (హృదయావరణ కుహరం)',
        'Thoracic cavity / ఉరః కుహరం (Thoracic cavity)',
        'Abdominal cavity / ఉదర కుహరం',
        'C',
        'M',
        '',
        38
    ),
    (
        'If the father has blood group A and the mother has blood group O, then which of the following blood groups may be found in their son\nతెలుగు: తండ్రి రక్తపు గ్రూపు A మరియు తల్లి రక్తపు గ్రూపు O అయితే, వారి కుమారునిలో కింది ఏ రక్తపు గ్రూపు ఉండవచ్చు',
        'O / O',
        'B / B',
        'AB / AB',
        'B, AB, or O / B, AB, లేదా O',
        'A',
        'M',
        '',
        39
    ),
    (
        'Blood pressure in human body is controlled by\nతెలుగు: మానవ శరీరంలో రక్తపోటు దేని ద్వారా నియంత్రించబడుతుంది',
        'Adrenal gland / అడ్రినల్ గ్రంథి (Adrenal gland)',
        'Thyroid gland / థైరాయిడ్ గ్రంథి',
        'Thymus gland / థైమస్ గ్రంథి (బాల గ్రంథి)',
        'Corpus luteum / కార్పస్ లూటియం',
        'A',
        'M',
        '',
        40
    ),
    (
        'Why do two eyes give better vision than one\nతెలుగు: ఒక కన్ను కంటే రెండు కళ్ళు ఎందుకు మెరుగైన దృష్టిని ఇస్తాయి',
        'Because two lenses together impart a higher converging power so that a sharp image is formed on the retina. / ఎందుకంటే రెండు కటకాలు కలిసి అధిక కేంద్రీకరణ సామర్థ్యాన్ని ఇస్తాయి, తద్వారా రెటీనాపై స్పష్టమైన ప్రతిబింబం ఏర్పడుతుంది.',
        'Because two eyes do not form exactly similar images and the fusion of these two dissimilar images in the brain gives the three-dimensional or stereoscopic vision. / ఎందుకంటే రెండు కళ్ళు కచ్చితంగా ఒకే రకమైన ప్రతిబింబాలను ఏర్పరచవు, మరియు ఈ రెండు విభిన్న ప్రతిబింబాలు మెదడులో కలవడం వల్ల త్రిమితీయ లేదా స్టీరియోస్కోపిక్ దృష్టి వస్తుంది.',
        'Because both the eyes are connected by nerves to the brain and hence transmit the message more quickly to the brain. / ఎందుకంటే రెండు కళ్ళు నాడుల ద్వారా మెదడుకు అనుసంధానించబడి ఉంటాయి, కాబట్టి సందేశాన్ని మెదడుకు వేగంగా పంపుతాయి.',
        'None of these / ఇవేవీ కావు',
        'B',
        'M',
        '',
        41
    ),
    (
        'Which of the following hormones contains iodine\nతెలుగు: కింది హార్మోన్లలో అయోడిన్\u200cను కలిగి ఉండేది ఏది',
        'Adrenaline / అడ్రినలిన్',
        'Insulin / ఇన్సులిన్',
        'Testosterone / టెస్టోస్టిరాన్',
        'Thyroxine / థైరాక్సిన్ (Thyroxine)',
        'D',
        'M',
        '',
        42
    ),
    (
        'Respiratory center is situated in\nతెలుగు: శ్వాస కేంద్రం (Respiratory center) ఎక్కడ ఉంటుంది',
        'Cerebrum / సెరిబ్రమ్ (మస్తిష్కం)',
        'Cerebellum / సెరిబెల్లమ్ (అనుమస్తిష్కం)',
        'Medulla oblongata / మజ్జాముఖం (Medulla oblongata)',
        'Diencephalon / డయాన్సెఫలాన్ (ద్వారగోర్ధం)',
        'C',
        'M',
        '',
        43
    ),
    (
        "During sleep, the man's blood pressure\nతెలుగు: నిద్రపోతున్నప్పుడు మనిషి రక్తపోటు:",
        'Decreases / తగ్గుతుంది',
        'Increases / పెరుగుతుంది',
        'Fluctuates / హెచ్చుతగ్గులకు గురవుతుంది (Fluctuates)',
        'Remains constant / స్థిరంగా ఉంటుంది',
        'C',
        'M',
        '',
        44
    ),
    (
        "A person with AB blood group is sometimes called a universal recipient because of the\nతెలుగు: AB రక్తపు గ్రూపు ఉన్న వ్యక్తిని 'విశ్వ గ్రహీత' (universal recipient) అని పిలవడానికి కారణం:",
        'Presence of antibodies in his blood / అతని రక్తంలో ప్రతిరక్షకాలు (antibodies) ఉండటం వల్ల',
        'Lack of antibodies in his blood / అతని రక్తంలో ప్రతిరక్షకాలు లేకపోవడం వల్ల (Lack of antibodies in his blood)',
        'Lack of antigen in his blood / అతని రక్తంలో ప్రతిజనకం (antigen) లేకపోవడం వల్ల',
        'Lack of both antigens and antibodies / ప్రతిజనకాలు మరియు ప్రతిరక్షకాలు రెండూ లేకపోవడం వల్ల',
        'B',
        'M',
        '',
        46
    ),
    (
        "Which of the following glands is also known as 'master gland'\nతెలుగు: కింది వాటిలో ఏ గ్రంథిని 'మాస్టర్ గ్లాండ్' (ప్రధాన గ్రంథి) అని కూడా పిలుస్తారు",
        'Pituitary / పిట్యూటరీ (Pituitary / పీయూష గ్రంథి)',
        'Adrenal / అడ్రినల్ (అధివృక్క గ్రంథి)',
        'Pancreas / ప్యాంక్రియాస్ (క్లోమం)',
        'Hypothalamus / హైపోథాలమస్',
        'A',
        'M',
        '',
        47
    ),
    (
        'The number of factors required for blood clotting is\nతెలుగు: రక్తం గడ్డకట్టడానికి అవసరమైన కారకాల (factors) సంఖ్య ఎంత',
        '7 / 7',
        '11 / 11',
        '13 / 13',
        '15 / 15',
        'C',
        'M',
        '',
        48
    ),
    (
        'SA node in the heart is also known as\nతెలుగు: గుండెలోని SA నోడ్ (సినోఆట్రియల్ నోడ్) ను ఏమని పిలుస్తారు',
        'Pacemaker / పేస్\u200cమేకర్ (Pacemaker)',
        'Pacesetter / పేస్\u200cసెట్టర్',
        'Pace regulator / పేస్ రెగ్యులేటర్',
        'Pace coordinator / పేస్ కోఆర్డినేటర్',
        'A',
        'M',
        '',
        49
    ),
    (
        'Which level of the food chain includes millipede, springtails, woodlice, dung flies and slugs that feed on the dead or decaying plants or animals\nతెలుగు: చనిపోయిన లేదా కుళ్ళిపోతున్న మొక్కలు లేదా జంతువులను తినే మిల్లీపెడ్, స్ప్రింగ్\u200cటైల్స్, ఉడ్\u200cలైస్, పేడ ఈగలు మరియు నత్తలు (slugs) ఏ ఆహారపు గొలుసు స్థాయికి (level of food chain) చెందుతాయి',
        'Carnivores / మాంసాహారులు',
        'Detritivores / డెట్రిటివోర్స్ (Detritivores / మృతకళేబరాలను తినేవి)',
        'Omnivores / సర్వభక్షకులు',
        'Herbivores / శాకాహారులు',
        'B',
        'M',
        '',
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
    print(f"Inserted {n} questions from {SOURCE}")
    print(f"Total General_Science questions in DB: {total}")

if __name__ == '__main__':
    seed()
