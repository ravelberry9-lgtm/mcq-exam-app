import sqlite3, os

SOURCE = 'Science_Set13_Human_System4'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    (
        'The blood pressure (systolic and diastolic) of a healthy man is\nతెలుగు: ఆరోగ్యవంతమైన మనిషి యొక్క రక్తపోటు ఎంత',
        '120 mm and 80 mm / 120 mm మరియు 80 mm',
        '201 mm and 110 mm / 201 mm మరియు 110 mm',
        '90 mm and 60 mm / 90 mm మరియు 60 mm',
        '85 mm and 55 mm / 85 mm మరియు 55 mm',
        'A',
        'M',
        '',
        1
    ),
    (
        'Bile juice is secreted by\nతెలుగు: బైల్ జ్యూస్ దేని ద్వారా స్రవించబడుతుంది',
        'Pancreas / ప్యాంక్రియాస్',
        'Liver / కాలేయం (Liver)',
        'Spleen / ప్లీహం',
        'Gall bladder / గాల్ బ్లాడర్',
        'B',
        'M',
        '',
        2
    ),
    (
        'Veins differ from arteries in having\nతెలుగు: ధమనుల నుండి సిరలు ఏ లక్షణాన్ని కలిగి ఉండటంలో భిన్నంగా ఉంటాయి',
        'thinner walls / పలచని గోడలు',
        'strong walls / బలమైన గోడలు',
        'narrower lumen / ఇరుకైన ల్యూమన్',
        'valves to control direction of flow / ప్రవాహ దిశను నియంత్రించడానికి కవాటాలను కలిగి ఉండటం',
        'D',
        'M',
        '',
        3
    ),
    (
        'The smallest cells in the human body are\nతెలుగు: మానవ శరీరంలో అతి చిన్న కణాలు ఏవి',
        'muscle cells / కండర కణాలు',
        'nerve cells / నాడీ కణాలు',
        'blood cells / రక్త కణాలు (blood cells)',
        'epithelial cells / ఎపిథీలియల్ కణాలు',
        'C',
        'M',
        '',
        4
    ),
    (
        'The largest endocrine gland of the human body is\nతెలుగు: మానవ శరీరంలో అతిపెద్ద వినాళ గ్రంథి ఏది',
        'Pituitary / పిట్యూటరీ',
        'Adrenal / అడ్రినల్',
        'Thymus / థైమస్',
        'Thyroid / థైరాయిడ్ (Thyroid)',
        'D',
        'M',
        '',
        5
    ),
    (
        'What is the main function of insulin in the human body\nతెలుగు: మానవ శరీరంలో ఇన్సులిన్ యొక్క ప్రధాన విధి ఏమిటి',
        'To maintain blood pressure / రక్తపోటును నిర్వహించడం',
        'To help in digestion of food / ఆహారం జీర్ణం కావడానికి సహాయపడటం',
        'To control the level of sugar in the body / శరీరంలో చక్కెర స్థాయిని నియంత్రించడం',
        'To check the level of iodine in the body / శరీరంలో అయోడిన్ స్థాయిని తనిఖీ చేయడం',
        'C',
        'M',
        '',
        6
    ),
    (
        'An enzyme that works in an acidic medium is\nతెలుగు: ఆమ్ల యానకంలో పనిచేసే ఎంజైమ్ ఏది',
        'pepsin / పెప్సిన్ (pepsin)',
        'trypsin / ట్రిప్సిన్',
        'ptyalin / టయలిన్',
        'maltase / మాల్టేజ్',
        'A',
        'M',
        '',
        7
    ),
    (
        'Food is mainly digested in\nతెలుగు: ఆహారం ప్రధానంగా ఎక్కడ జీర్ణమవుతుంది',
        'liver / కాలేయం',
        'large intestine / పెద్ద ప్రేగు',
        'small intestine / చిన్న ప్రేగు (small intestine)',
        'mouth / నోరు',
        'C',
        'M',
        '',
        8
    ),
    (
        'Impure blood from various parts of the body enters into the\nతెలుగు: శరీరంలోని వివిధ భాగాల నుండి అశుద్ధ రక్తం గుండెలోని ఏ గదిలోకి ప్రవేశిస్తుంది',
        'left auricle / ఎడమ కర్ణిక',
        'right auricle / కుడి కర్ణిక (right auricle)',
        'left ventricle / ఎడమ జఠరిక',
        'right ventricle / కుడి జఠరిక',
        'B',
        'M',
        '',
        9
    ),
    (
        'The number of ribs in the human body is\nతెలుగు: మానవ శరీరంలో పక్కటెముకల సంఖ్య ఎంత',
        '12 / 12',
        '18 / 18',
        '20 / 20',
        '24 / 24',
        'D',
        'M',
        '',
        10
    ),
    (
        'Which enzyme converts milk into casein\nతెలుగు: పాలను కేసిన్\u200cగా మార్చే ఎంజైమ్ ఏది',
        'Pepsin / పెప్సిన్',
        'Lipase / లైపేజ్',
        'Trypsin / ట్రిప్సిన్',
        'Renin / రెనిన్ (Renin)',
        'D',
        'M',
        '',
        11
    ),
    (
        'The skull is constituted of bones in number\nతెలుగు: పుర్రె ఎన్ని ఎముకలతో నిర్మితమై ఉంటుంది',
        '2 / 2',
        '3 / 3',
        '4 / 4',
        '5 / 5',
        'D',
        'M',
        '',
        12
    ),
    (
        'The largest lymphatic organ of the body is\nతెలుగు: శరీరంలో అతిపెద్ద శోషరస అవయవం ఏది',
        'liver / కాలేయం',
        'spleen / ప్లీహం (spleen)',
        'pancreas / క్లోమం',
        'duodenum / ఆంత్రమూలం',
        'B',
        'M',
        '',
        13
    ),
    (
        'The blood pressure is the pressure of blood in\nతెలుగు: రక్తపోటు అనేది దేనిలో ప్రవహించే రక్తం యొక్క పీడనం',
        'arteries / ధమనులు (arteries)',
        'veins / సిరలు',
        'auricles / కర్ణికలు',
        'ventricles / జఠరికలు',
        'A',
        'M',
        '',
        14
    ),
    (
        'The longest bone in the human body is\nతెలుగు: మానవ శరీరంలో అతి పొడవైన ఎముక ఏది',
        'stirrup / స్టెర్రప్',
        'back bone / వెన్నెముక',
        'thigh bone / తొడ ఎముక (thigh bone)',
        'gullet / గొంతు',
        'C',
        'M',
        '',
        15
    ),
    (
        'The total number of bones in the human skull are\nతెలుగు: మానవ పుర్రెలో ఉండే మొత్తం ఎముకల సంఖ్య ఎంత',
        '8 / 8',
        '12 / 12',
        '22 / 22',
        '32 / 32',
        'C',
        'M',
        '',
        16
    ),
    (
        'Which of the following blood groups is a universal recipient\nతెలుగు: కింది వాటిలో ఏ రక్తపు గ్రూపు విశ్వ గ్రహీత',
        'A / A',
        'B / B',
        'AB / AB',
        'O / O',
        'C',
        'M',
        '',
        17
    ),
    (
        'Which of the following glands controls the development of sex organs in humans\nతెలుగు: కింది ఏ గ్రంథి మానవులలో లైంగిక అవయవాల అభివృద్ధిని నియంత్రిస్తుంది',
        'Pancreas / క్లోమం',
        'Thyroid / థైరాయిడ్',
        'Adrenal / అడ్రినల్',
        'Pituitary / పిట్యూటరీ (Pituitary)',
        'D',
        'M',
        '',
        18
    ),
    (
        'Which of the following helps us in protecting from infection\nతెలుగు: ఇన్ఫెక్షన్ల నుండి మనలను రక్షించడంలో కింది వాటిలో ఏది సహాయపడుతుంది',
        'RBC / ఎర్ర రక్త కణాలు',
        'WBC / తెల్ల రక్త కణాలు (WBC)',
        'Blood Plasma / రక్త ప్లాస్మా',
        'Haemoglobin / హిమోగ్లోబిన్',
        'B',
        'M',
        '',
        19
    ),
    (
        'Oxygen is transported to every cell of the human body by\nతెలుగు: మానవ శరీరంలోని ప్రతి కణానికి ఆక్సిజన్ దేని ద్వారా రవాణా చేయబడుతుంది',
        'red blood cells / ఎర్ర రక్త కణాలు (red blood cells)',
        'blood platelets / రక్త ఫలకికలు',
        'white blood cells / తెల్ల రక్త కణాలు',
        'hormones / హార్మోన్లు',
        'A',
        'M',
        '',
        20
    ),
    (
        'Within the cardiac conduction system, which structure is the primary pacemaker responsible for initiating each heartbeat\nతెలుగు: గుండె ప్రసరణ వ్యవస్థలో ప్రతి హృదయ స్పందనను ప్రారంభించే ప్రాథమిక పేస్\u200cమేకర్ ఏది',
        'Bundle of His / హిస్ కట్ట',
        'Sinoatrial SA node / సినోఏట్రియల్ SA నోడ్',
        'Atrioventricular AV node / AV నోడ్',
        'Purkinje fibers / పుర్కింజే తంతువులు',
        'B',
        'M',
        '',
        21
    ),
    (
        'Which of the following is a mixed gland (i.e. secretes both enzymes and hormones)\nతెలుగు: కింది వాటిలో ఏది మిశ్రమ గ్రంథి',
        'Salivary / లాలాజల గ్రంథి',
        'Thyroid / థైరాయిడ్',
        'Liver / కాలేయం',
        'Pancreas / ప్యాంక్రియాస్ (Pancreas)',
        'D',
        'M',
        '',
        22
    ),
    (
        'Match disease to organ. Tuberculosis-Lungs, Hepatitis-Liver, Gonorrhea-Reproductive tract, Mumps-Salivary glands. Pick the correct mapping.\nతెలుగు: వ్యాధులను అవయవాలతో జతపరచండి.',
        'i-c, ii-a, iii-b, iv-d / i-c, ii-a, iii-b, iv-d',
        'i-c, ii-d, iii-a, iv-b / i-c, ii-d, iii-a, iv-b',
        'i-c, ii-d, iii-b, iv-a / i-c, ii-d, iii-b, iv-a',
        'i-d, ii-c, iii-b, iv-a / i-d, ii-c, iii-b, iv-a',
        'C',
        'M',
        '',
        23
    ),
    (
        'Name the virus spread by mosquitoes that causes inflammation in the brain\nతెలుగు: మెదడులో వాపు కలిగించే మరియు దోమల ద్వారా వ్యాపించే వైరస్ పేరు ఏమిటి',
        'Lymphatic filariasis / లింఫాటిక్ ఫైలేరియాసిస్',
        'Japanese encephalitis / జపనీస్ ఎన్సెఫాలిటిస్ (Japanese encephalitis)',
        'Francisella tularensis / ఫ్రాన్సిసెల్లా',
        'Yellow fever virus / ఎల్లో ఫీవర్ వైరస్',
        'B',
        'M',
        '',
        24
    ),
    (
        'If a person can see an object clearly when it is placed at about 25 cm away from him, he is suffering from\nతెలుగు: ఒక వ్యక్తి తన నుండి సుమారు 25 సెం.మీ దూరంలో ఉంచిన వస్తువును స్పష్టంగా చూడగలిగితే, అతను ఏ వ్యాధితో బాధపడుతున్నాడు',
        'myopia / మయోపియా',
        'hypermetropia / హైపర్\u200cమెట్రోపియా',
        'astigmatism / ఆస్టిగ్మాటిజం',
        'None of these / ఇవేవీ కావు',
        'D',
        'M',
        '',
        25
    ),
    (
        'The main function of white blood cells is\nతెలుగు: తెల్ల రక్త కణాల ప్రధాన విధి ఏమిటి',
        'Transport of oxygen / ఆక్సిజన్ రవాణా',
        'Transport of carbon dioxide / కార్బన్ డైయాక్సైడ్ రవాణా',
        'To develop resistance towards disease / వ్యాధుల పట్ల నిరోధకతను పెంపొందించడం',
        'None of the above / పైవేవీ కావు',
        'C',
        'M',
        '',
        26
    ),
    (
        'Which of the following is not a function of Kidneys\nతెలుగు: కింది వాటిలో మూత్రపిండాల విధి కానిది ఏది',
        'Regulation of blood pressure / రక్తపోటు నియంత్రణ',
        'Secretion of antibiotics / యాంటీబయాటిక్స్ స్రావం (Secretion of antibiotics)',
        'Removal of urine / మూత్రం తొలగింపు',
        'Regulation of acidity of body fluids / శరీర ద్రవాల ఆమ్లత్వ నియంత్రణ',
        'B',
        'M',
        '',
        27
    ),
    (
        'Pituitary gland is present\nతెలుగు: పిట్యూటరీ గ్రంథి ఎక్కడ ఉంటుంది',
        'Below the brain / మెదడు కింద (Below the brain)',
        'Above the brain / మెదడు పైన',
        'Inside the brain / మెదడు లోపల',
        'Nowhere near the brain / మెదడు దరిదాపుల్లో ఎక్కడా లేదు',
        'A',
        'M',
        '',
        28
    ),
    (
        'Element present in the largest amount in the human body is\nతెలుగు: మానవ శరీరంలో అత్యధిక పరిమాణంలో ఉండే మూలకం ఏది',
        'Hydrogen / హైడ్రోజన్',
        'Nitrogen / నైట్రోజన్',
        'Oxygen / ఆక్సిజన్ (Oxygen)',
        'Carbon / కార్బన్',
        'C',
        'M',
        '',
        29
    ),
    (
        'The viscous nature of human blood is due to\nతెలుగు: మానవ రక్తం యొక్క స్నిగ్ధతకు కారణం ఏమిటి',
        'Proteins in blood / రక్తంలోని ప్రోటీన్లు (Proteins in blood)',
        'Platelets in plasma / ప్లేట్\u200cలెట్లు',
        'RBC and WBC in blood / RBC మరియు WBC',
        'All of the above / పైవన్నీ',
        'A',
        'M',
        '',
        30
    ),
    (
        'How many bones are there in the human body\nతెలుగు: మానవ శరీరంలో ఎన్ని ఎముకలు ఉంటాయి',
        '180 / 180',
        '198 / 198',
        '206 / 206',
        '210 / 210',
        'C',
        'M',
        '',
        31
    ),
    (
        'Which of the following organs is used in the purification of blood in the human body\nతెలుగు: మానవ శరీరంలో రక్తాన్ని శుద్ధి చేయడానికి ఏ అవయవం ఉపయోగించబడుతుంది',
        'Liver / కాలేయం',
        'Kidney / మూత్రపిండం (Kidney)',
        'Spleen / ప్లీహం',
        'Lungs / ఊపిరితిత్తులు',
        'B',
        'M',
        '',
        32
    ),
    (
        'In Homo sapiens, fertilization occurs in the\nతెలుగు: హోమో సేపియన్స్ లో ఫలదీకరణం ఎక్కడ జరుగుతుంది',
        'uterus / గర్భాశయం',
        'ovary / అండాశయం',
        'vagina / యోని',
        'oviduct / అండవాహిక (oviduct)',
        'D',
        'M',
        '',
        33
    ),
    (
        'The chief nitrogenous waste in humans is\nతెలుగు: మానవులలో ప్రధాన నత్రజని సంబంధిత వ్యర్థం ఏది',
        'ammonia / అమ్మోనియా',
        'ammonium nitrate / అమ్మోనియం నైట్రేట్',
        'urea / యూరియా (urea)',
        'uric acid / యూరిక్ ఆమ్లం',
        'C',
        'M',
        '',
        34
    ),
    (
        'The prenatal technique used to see an image of the growing fetus in the womb is called\nతెలుగు: గర్భంలో పెరుగుతున్న పిండం యొక్క చిత్రాన్ని చూడటానికి ఉపయోగించే ప్రినేటల్ టెక్నిక్\u200cను ఏమంటారు',
        'Radiotherapy / రేడియోథెరపీ',
        'X-ray marking / ఎక్స్-రే మార్కింగ్',
        'Ultrasound / అల్ట్రాసౌండ్ (Ultrasound)',
        'Amniocentesis / అమ్నియోసెంటెసిస్',
        'C',
        'M',
        '',
        35
    ),
    (
        'The first human hormone synthesized with the help of biotechnology was\nతెలుగు: బయోటెక్నాలజీ సహాయంతో సంశ్లేషణ చేయబడిన మొదటి మానవ హార్మోన్ ఏది',
        'Prostaglandin / ప్రోస్టాగ్లాండిన్ (Prostaglandin)',
        'Interferon / ఇంటర్\u200cఫెరాన్',
        'Pituitary hormone / పిట్యూటరీ హార్మోన్',
        'Somatostatin / సోమాటోస్టాటిన్',
        'A',
        'M',
        '',
        36
    ),
    (
        'Sweat glands occur in the greatest number in the skin of the\nతెలుగు: స్వేద గ్రంథులు ఏ భాగపు చర్మంలో అత్యధిక సంఖ్యలో ఉంటాయి',
        'forehead / నుదురు',
        'armpits / చంకలు (armpits)',
        'back / వీపు',
        'palm of hand / అరచేయి',
        'B',
        'M',
        '',
        37
    ),
    (
        'Which of the following organs converts glycogen into glucose and purifies the blood\nతెలుగు: కింది ఏ అవయవం గ్లైకోజెన్\u200cను గ్లూకోజ్\u200cగా మారుస్తుంది మరియు రక్తాన్ని శుద్ధి చేస్తుంది',
        'Liver / కాలేయం (Liver)',
        'Kidney / మూత్రపిండాలు',
        'Lungs / ఊపిరితిత్తులు',
        'Spleen / ప్లీహం',
        'A',
        'M',
        '',
        38
    ),
    (
        'Cornea is a part of which of the following of the human body\nతెలుగు: కార్నియా మానవ శరీరంలోని కింది ఏ భాగంలో ఉంటుంది',
        'Eye / కన్ను (Eye)',
        'Ear / చెవి',
        'Nose / ముక్కు',
        'Heart / గుండె',
        'A',
        'M',
        '',
        39
    ),
    (
        'What is Funny Bone\nతెలుగు: ఫన్నీ బోన్ అంటే ఏమిటి',
        'A muscle / ఒక కండరం',
        'A nerve / ఒక నరం (A nerve)',
        'A bone / ఒక ఎముక',
        'A blood vessel / ఒక రక్త నాళం',
        'B',
        'M',
        '',
        40
    ),
    (
        'The blood cholesterol level in 100 ml of blood in a normal person varies between\nతెలుగు: సాధారణ వ్యక్తి యొక్క 100 ml రక్తంలో కొలెస్ట్రాల్ స్థాయి దేని మధ్య మారుతూ ఉంటుంది',
        '50 to 100 mg / 50 నుండి 100 mg',
        '100 to 150 mg / 100 నుండి 150 mg',
        '150 to 250 mg / 150 నుండి 250 mg (150 to 250 mg)',
        '250 to 350 mg / 250 నుండి 350 mg',
        'C',
        'M',
        '',
        41
    ),
    (
        'Formation of WBC and destruction of RBC takes place in\nతెలుగు: WBC ఉత్పత్తి మరియు RBC విధ్వంసం ఎక్కడ జరుగుతుంది',
        'Lymph gland / శోషరస గ్రంథి',
        'Spleen / ప్లీహం (Spleen)',
        'Pancreas / క్లోమం',
        'Liver / కాలేయం',
        'B',
        'M',
        '',
        42
    ),
    (
        'Which of the following when taken by pregnant women is found to be the cause of deformed children\nతెలుగు: గర్భిణీ స్త్రీలు తీసుకోవడం వల్ల పిల్లలలో వైకల్యాలు రావడానికి కారణమైన మందు ఏది',
        'Glycerol / గ్లిసరాల్',
        'Xylidine / జైలిడిన్',
        'Thalidomide / థాలిడోమైడ్ (Thalidomide)',
        'None of these / ఇవేవీ కావు',
        'C',
        'M',
        '',
        43
    ),
    (
        'The diploid number of chromosomes in the human body is\nతెలుగు: మానవ శరీరంలో క్రోమోజోమ్\u200cల ద్వయస్థితిక సంఖ్య ఎంత',
        '24 / 24',
        '40 / 40',
        '46 / 46 (23 జతలు)',
        '48 / 48',
        'C',
        'M',
        '',
        44
    ),
    (
        'The largest cell in the human body is\nతెలుగు: మానవ శరీరంలో అతిపెద్ద కణం ఏది',
        'Nerve cell / నాడీ కణం (Nerve cell)',
        'Muscle cell / కండర కణం',
        'Liver cell / కాలేయ కణం',
        'Kidney cell / కిడ్నీ కణం',
        'A',
        'M',
        '',
        45
    ),
    (
        'In our body, the tissues are bathed in\nతెలుగు: మన శరీరంలో కణజాలాలు దేనిలో మునిగి ఉంటాయి',
        'water / నీరు',
        'blood / రక్తం',
        'lymph / శోషరసం (lymph)',
        'plasma / ప్లాస్మా',
        'C',
        'M',
        '',
        46
    ),
    (
        'Mala-D, a female contraceptive, prevents\nతెలుగు: మాలా-D దేనిని నిరోధిస్తుంది',
        'ovulation / అండోత్సర్గం (ovulation)',
        'fertilization / ఫలదీకరణం',
        'entry of the egg into the oviduct / అండవాహికలోకి అండం ప్రవేశించడాన్ని',
        'implantation of the fertilized egg / ఇంప్లాంటేషన్',
        'A',
        'M',
        '',
        47
    ),
    (
        'A man cannot see objects distinctly at a distance less than 1 meter. He is suffering from\nతెలుగు: ఒక వ్యక్తి 1 మీటరు కంటే తక్కువ దూరంలో ఉన్న వస్తువులను స్పష్టంగా చూడలేడు. అతను ఏ వ్యాధితో బాధపడుతున్నాడు',
        'old-age sight / వృద్ధాప్య దృష్టి',
        'short-sightedness / హ్రస్వదృష్టి',
        'long-sightedness / దీర్ఘదృష్టి (long-sightedness)',
        'opaqueness of the lens / కటకం అపారదర్శకత',
        'C',
        'M',
        '',
        48
    ),
    (
        'Identical twins are born when\nతెలుగు: ఐడెంటికల్ ట్విన్స్ ఎప్పుడు పుడతారు',
        'two sperms fertilize one ovum / రెండు శుక్రకణాలు ఒక అండాన్ని ఫలదీకరణం చేసినప్పుడు',
        'two sperms fertilize two ovums / రెండు శుక్రకణాలు రెండు అండాలను ఫలదీకరణం చేసినప్పుడు',
        'one sperm fertilizes two ovums / ఒక శుక్రకణం రెండు అండాలను ఫలదీకరణం చేసినప్పుడు',
        'one sperm fertilizes the ovum and the zygote splits into two parts each developing independently / ఒక శుక్రకణం అండాన్ని ఫలదీకరణం చేసిన తర్వాత జైగోట్ రెండు భాగాలుగా విడిపోయినప్పుడు',
        'D',
        'M',
        '',
        49
    ),
    (
        'Percentage of water in plasma is\nతెలుగు: రక్త ప్లాస్మాలో నీటి శాతం ఎంత',
        '60% / 60%',
        '70% / 70%',
        '80% / 80%',
        '90% / 90%',
        'D',
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
