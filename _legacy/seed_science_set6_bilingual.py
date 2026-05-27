import sqlite3, os

SOURCE = 'Science_Set6_Reactions_Changes_Separation'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    (
        'Solubility of CH3COOH decreases in presence of CH3COONa due to:\nతెలుగు: CH3COONa సమక్షంలో CH3COOH యొక్క ద్రావణీయత (Solubility) దేని కారణంగా తగ్గుతుంది',
        'Common ion effect / ఉమ్మడి అయాన్ ప్రభావం (Common ion effect)',
        'Increased temperature / పెరిగిన ఉష్ణోగ్రత',
        'Ion pairing / అయాన్ జతకట్టడం',
        'Oxidation / ఆక్సీకరణ (Oxidation)',
        'A',
        'M',
        '',
        1
    ),
    (
        'Which unit is used to measure the concentration of contaminants in soil and sediment\nతెలుగు: నేల మరియు అవక్షేపాలలో (sediment) కాలుష్య కారకాల గాఢతను (concentration) కొలవడానికి ఏ యూనిట్\u200cను ఉపయోగిస్తారు',
        'PPBB / PPBB',
        'TDS / TDS',
        'DPMO / DPMO',
        'PPM / PPM',
        'B',
        'M',
        '',
        2
    ),
    (
        'In which of the following liquids would anthracene dissolve easily\nతెలుగు: కింది ఏ ద్రవాలలో ఆంత్రాసీన్ (anthracene) సులభంగా కరుగుతుంది',
        'Water / నీరు',
        'Benzene / బెంజీన్',
        'Methane / మీథేన్',
        'Sodium chloride / సోడియం క్లోరైడ్',
        'B',
        'M',
        '',
        3
    ),
    (
        'Which of the following are true regarding a catalyst? Statements: (1) increases reaction rate, (2) reduces activation energy, (3) increases activation energy, (4) is consumed.\nతెలుగు: ఉత్ప్రేరకానికి (catalyst) సంబంధించి కింది వాటిలో ఏది సరైనది? వ్యాఖ్యలు: (1) చర్య రేటును పెంచుతుంది (2) ఉత్తేజిత శక్తిని తగ్గిస్తుంది (3) ఉత్తేజిత శక్తిని పెంచుతుంది (4) చర్యలో వినియోగించబడుతుంది',
        '1 and 2 / 1 మరియు 2',
        '2 and 3 / 2 మరియు 3',
        '3 and 4 / 3 మరియు 4',
        '1 and 4 / 1 మరియు 4',
        'A',
        'M',
        '',
        4
    ),
    (
        'Rusting of iron involves:\nతెలుగు: ఇనుము తుప్పు పట్టడం (Rusting of iron) లో ఇమిడి ఉన్న ప్రక్రియ ఏది',
        'Oxidation / ఆక్సీకరణ (Oxidation)',
        'Reduction / క్షయకరణ (Reduction)',
        'Decomposition / వియోగం (Decomposition)',
        'Displacement / స్థానభ్రంశం (Displacement)',
        'A',
        'M',
        '',
        5
    ),
    (
        'Which of the following is a chemical change\nతెలుగు: కింది వాటిలో రసాయన మార్పు ఏది',
        'Rusting of iron / ఇనుము తుప్పు పట్టడం',
        'Tempering of iron / ఇనుము టెంపరింగ్',
        'Melting of iron / ఇనుము కరగడం',
        'Bending of iron / ఇనుము వంగడం',
        'A',
        'M',
        '',
        6
    ),
    (
        'Which of the following is a physical change\nతెలుగు: కింది వాటిలో భౌతిక మార్పు ఏది',
        'Oxidation / ఆక్సీకరణ',
        'Reduction / క్షయకరణ',
        'Sublimation / ఉత్పతనం (Sublimation)',
        'Decomposition / వియోగం',
        'C',
        'M',
        '',
        7
    ),
    (
        'A mixture of water and alcohol can be separated by:\nతెలుగు: నీరు మరియు ఆల్కహాల్ మిశ్రమాన్ని ఏ పద్ధతి ద్వారా వేరు చేయవచ్చు',
        'Filtration / వడపోత',
        'Evaporation / బాష్పీభవనం',
        'Distillation / స్వేదనం (Distillation)',
        'Decantation / డీకాంటేషన్',
        'C',
        'M',
        '',
        8
    ),
    (
        'A substance that changes readily into vapor without heating is called:\nతెలుగు: వేడి చేయకుండానే సులభంగా ఆవిరిగా మారే పదార్థాన్ని ఏమంటారు',
        'Efflorescent / ఎఫ్లోరసెంట్',
        'Synthetic / సింథటిక్',
        'Volatile / వోలటైల్ (బాష్పశీల)',
        'Effervescent / ఎఫెర్వెసెంట్',
        'C',
        'M',
        '',
        9
    ),
    (
        'Catalytic properties of a substance may be best defined as a phenomenon of:\nతెలుగు: ఒక పదార్థం యొక్క ఉత్ప్రేరక ధర్మాలను ఏ ప్రక్రియగా ఉత్తమంగా నిర్వచించవచ్చు',
        'Absorption / శోషణ (Absorption)',
        'Chemisorption / రసాయన అధిశోషణం (Chemisorption)',
        'Adsorption / అధిశోషణం (Adsorption)',
        'None of these / ఇవేవీ కావు',
        'B',
        'M',
        '',
        10
    ),
    (
        'Which of the following is NOT the use of baking soda in the kitchen\nతెలుగు: వంటగదిలో బేకింగ్ సోడా యొక్క ఉపయోగం కానిది ఏది',
        'For food colouring / ఆహారానికి రంగు వేయడానికి',
        'In fire extinguishers / మంటలను ఆర్పే సాధనాలలో',
        'As a leavening agent / పులియబెట్టే కారకంగా',
        'As an ingredient in antacids / యాంటాసిడ్లలో ఒక పదార్థంగా',
        'A',
        'M',
        '',
        11
    ),
    (
        'Cooking oil can be converted into vegetable ghee by the process of\nతెలుగు: వంట నూనెను ఏ ప్రక్రియ ద్వారా వెజిటబుల్ నెయ్యిగా మార్చవచ్చు',
        'Oxidation / ఆక్సీకరణ',
        'Hydrogenation / హైడ్రోజనీకరణ (Hydrogenation)',
        'Distillation / స్వేదనం',
        'Crystallization / స్పటికీకరణ',
        'B',
        'M',
        '',
        12
    ),
    (
        'Which of the following is a monoatomic gas\nతెలుగు: కింది వాటిలో ఏకపరమాణు (monoatomic) వాయువు ఏది',
        'Chlorine / క్లోరిన్',
        'Hydrogen / హైడ్రోజన్',
        'Xenon / జెనాన్',
        'Oxygen / ఆక్సిజన్',
        'C',
        'M',
        '',
        13
    ),
    (
        'Photosynthesis is\nతెలుగు: కిరణజన్య సంయోగక్రియ (Photosynthesis) అనేది:',
        'An exothermic process / ఉష్ణమోచక ప్రక్రియ',
        'An endothermic process / ఉష్ణగ్రాహక ప్రక్రియ (endothermic)',
        'A neutral process / తటస్థ ప్రక్రియ',
        'A thermostatic process / థర్మోస్టాటిక్ ప్రక్రియ',
        'B',
        'M',
        '',
        14
    ),
    (
        'Which of the following substances exhibit the property of sublimation\nతెలుగు: కింది ఏ పదార్థం ఉత్పతనం (sublimation) లక్షణాన్ని ప్రదర్శిస్తుంది',
        'Ice / మంచు',
        'Wax / మైనపు',
        'Camphor / కర్పూరం (Camphor)',
        'Ethyl alcohol / ఇథైల్ ఆల్కహాల్',
        'C',
        'M',
        '',
        15
    ),
    (
        'The hydrogenation of vegetable oils takes place in the presence of finely divided\nతెలుగు: వృక్ష సంబంధిత నూనెల హైడ్రోజనీకరణ కింది ఏ సూక్ష్మ చూర్ణం సమక్షంలో జరుగుతుంది',
        'Aluminium / అల్యూమినియం',
        'Charcoal / చార్\u200cకోల్',
        'Silica / సిలికా',
        'Nickel / నికెల్',
        'D',
        'M',
        '',
        16
    ),
    (
        'Combustion is the process in which\nతెలుగు: దహనం (Combustion) అనే ప్రక్రియలో ఏమి జరుగుతుంది',
        'Heat is produced / ఉష్ణం ఉత్పత్తి అవుతుంది',
        'Light is produced / కాంతి ఉత్పత్తి అవుతుంది',
        'Heat and light are produced / ఉష్ణం మరియు కాంతి రెండూ ఉత్పత్తి అవుతాయి',
        'None of these / ఇవేవీ కావు',
        'C',
        'M',
        '',
        17
    ),
    (
        'The chemical used as a fixer in photography is\nతెలుగు: ఫోటోగ్రఫీలో ఫిక్సర్ గా ఉపయోగించే రసాయనం ఏది',
        'Borax / బోరాక్స్',
        'Sodium thiosulfate / సోడియం థయోసల్ఫేట్',
        'Sodium sulfate / సోడియం సల్ఫేట్',
        'Ammonium persulfate / అమ్మోనియం పర్సల్ఫేట్',
        'B',
        'M',
        '',
        18
    ),
    (
        'A mixture of iron filings and sand can be separated by\nతెలుగు: ఇనుప రజను మరియు ఇసుక మిశ్రమాన్ని దేని ద్వారా వేరు చేయవచ్చు',
        'Heating / వేడి చేయడం ద్వారా',
        'Sublimation / ఉత్పతనం ద్వారా',
        'Hand picking / ఏరివేయడం',
        'Magnetic separation / అయస్కాంత వేర్పాటు (Magnetic separation)',
        'D',
        'M',
        '',
        19
    ),
    (
        'In which of the following processes is Vanadium pentoxide used as a catalyst\nతెలుగు: కింది ఏ ప్రక్రియలో వెనాడియం పెంటాక్సైడ్\u200cను ఉత్ప్రేరకంగా ఉపయోగిస్తారు',
        'Contact process / కాంటాక్ట్ ప్రక్రియ (Contact process)',
        "Haber's process / హేబర్ ప్రక్రియ",
        'Solvay process / సాల్వే ప్రక్రియ',
        'None of these / ఇవేవీ కావు',
        'A',
        'M',
        '',
        20
    ),
    (
        'Conversion of a substance directly from the solid to vapor state is known as\nతెలుగు: ఒక పదార్థం ఘన స్థితి నుండి నేరుగా ఆవిరి స్థితికి మారడాన్ని ఏమంటారు',
        'Ionization / అయనీకరణం',
        'Evaporation / బాష్పీభవనం',
        'Vaporization / వేపరైజేషన్',
        'Sublimation / ఉత్పతనం (Sublimation)',
        'D',
        'M',
        '',
        21
    ),
    (
        'The rate of chemical reaction does not depend upon\nతెలుగు: రసాయన చర్య రేటు కింది వాటిలో దేనిపై ఆధారపడి ఉండదు',
        'Concentration / గాఢత',
        'Catalyst / ఉత్ప్రేరకం',
        'Temperature / ఉష్ణోగ్రత',
        'Pressure / పీడనం (Pressure)',
        'D',
        'M',
        '',
        22
    ),
    (
        'Which industries commonly used Tetrachloromethane as a degreasing agent\nతెలుగు: ఏ పరిశ్రమలలో టెట్రాక్లోరోమీథేన్\u200cను డీగ్రీజింగ్ ఏజెంట్\u200cగా సాధారణంగా ఉపయోగిస్తారు',
        'Textile industries / వస్త్ర పరిశ్రమలు',
        'Food processing industries / ఫుడ్ ప్రాసెసింగ్ పరిశ్రమలు',
        'Manufacturing and mechanical industries / తయారీ మరియు మెకానికల్ పరిశ్రమలు',
        'Bottling industries / బాట్లింగ్ పరిశ్రమలు',
        'C',
        'M',
        '',
        23
    ),
    (
        'The Contact Process is involved in the manufacture of\nతెలుగు: కాంటాక్ట్ ప్రక్రియ ద్వారా దేనిని ఉత్పత్తి చేస్తారు',
        'Nitric acid / నైట్రిక్ ఆమ్లం',
        'Sulphuric acid / సల్ఫ్యూరిక్ ఆమ్లం (Sulphuric acid)',
        'Ammonia / అమ్మోనియా',
        'Caustic soda / కాస్టిక్ సోడా',
        'B',
        'M',
        '',
        24
    ),
    (
        'Which of the following metals can displace hydrogen from dilute acids\nతెలుగు: కింది ఏ లోహం విలీన ఆమ్లాల నుండి హైడ్రోజన్\u200cను స్థానభ్రంశం చేయగలదు',
        'Zinc / జింక్ (Zinc)',
        'Gold / బంగారం',
        'Copper / రాగి',
        'Silver / వెండి',
        'A',
        'M',
        '',
        25
    ),
    (
        'The reaction of alcohol with a carboxylic acid is known as\nతెలుగు: ఆల్కహాల్ మరియు కార్బాక్సిలిక్ ఆమ్లాల మధ్య జరిగే చర్యను ఏమంటారు',
        'Substitution reaction / ప్రతిక్షేపణ చర్య',
        'Addition reaction / సంకలన చర్య',
        'Esterification / ఎస్టరిఫికేషన్ (Esterification)',
        'Hydrogenation / హైడ్రోజనీకరణ',
        'C',
        'M',
        '',
        26
    ),
    (
        'Saponification involves the hydrolysis of fats and oils by\nతెలుగు: సపోనిఫికేషన్ ప్రక్రియలో కొవ్వులు మరియు నూనెల జలవిశ్లేషణ దేని ద్వారా జరుగుతుంది',
        'Water / నీరు',
        'Washing soda / వాషింగ్ సోడా',
        'Stearic acid / స్టియరిక్ ఆమ్లం',
        'Caustic soda / కాస్టిక్ సోడా (Caustic soda)',
        'D',
        'M',
        '',
        27
    ),
    (
        'Which of the following reagents gives a silver mirror test when added to aldehydes\nతెలుగు: ఆల్డిహైడ్\u200cలకు కలిపినప్పుడు సిల్వర్ మిర్రర్ పరీక్షను ఇచ్చే కారకం ఏది',
        "Fehling's Solution / ఫెహ్లింగ్ ద్రావణం",
        "Tollen's Reagent / టోలెన్స్ కారకం (Tollen's Reagent)",
        "Baeyer's Reagent / బేయర్స్ కారకం",
        "Nessler's Reagent / నెస్లర్స్ కారకం",
        'B',
        'M',
        '',
        28
    ),
    (
        'Which of the following is a correct balanced chemical equation\nతెలుగు: కింది వాటిలో తుల్యం చేయబడిన సరైన రసాయన సమీకరణం ఏది',
        '2C4H10 + 12O2 → 8CO2 + 10H2O / 2C4H10 + 12O2 → 8CO2 + 10H2O',
        'C4H10 + 13O2 → 4CO2 + 10H2O / C4H10 + 13O2 → 4CO2 + 10H2O',
        '2C4H10 + 10O2 → 8CO2 + 10H2O / 2C4H10 + 10O2 → 8CO2 + 10H2O',
        '2C4H10 + 13O2 → 8CO2 + 10H2O / 2C4H10 + 13O2 → 8CO2 + 10H2O',
        'D',
        'M',
        '',
        29
    ),
    (
        'Which of the following foods would you advise to neutralise excess stomach acids\nతెలుగు: పొట్టలో ఉన్న అదనపు ఆమ్లాలను తటస్థీకరించడానికి కింది ఏ ఆహారాన్ని మీరు సిఫార్సు చేస్తారు',
        'Baking soda / బేకింగ్ సోడా (Baking soda)',
        'Vinegar / వెనిగర్',
        'Boiling water / వేడి నీరు',
        'Spicy peppers / కారంగా ఉండే మిరియాలు',
        'A',
        'M',
        '',
        30
    ),
    (
        'The gas liberated during the reaction of copper with dilute nitric acid is\nతెలుగు: రాగి విలీన నైట్రిక్ ఆమ్లంతో చర్య జరిపినప్పుడు విడుదలయ్యే వాయువు ఏది',
        'NO2 / NO2',
        'N2O5 / N2O5',
        'O2 / O2',
        'NO / NO',
        'D',
        'M',
        '',
        31
    ),
    (
        'Which of the following substances undergoes a chemical change on heating\nతెలుగు: కింది పదార్థాలలో దేనిని వేడి చేసినప్పుడు రసాయన మార్పుకు గురవుతుంది',
        'Sodium chloride / సోడియం క్లోరైడ్',
        'Silica / సిలికా',
        'Lead nitrate / లెడ్ నైట్రేట్ (Lead nitrate)',
        'Platinum wire / ప్లాటినం వైర్',
        'C',
        'M',
        '',
        32
    ),
    (
        'Which chemical is used for whitening of cloth in cloth industries\nతెలుగు: వస్త్ర పరిశ్రమలలో బట్టలను తెల్లగా చేయడానికి ఏ రసాయనాన్ని ఉపయోగిస్తారు',
        'Calcium oxychloride / కాల్షియం ఆక్సీక్లోరైడ్ (బ్లీచింగ్ పౌడర్)',
        'Sodium hydrogen-carbonate / సోడియం హైడ్రోజన్ కార్బోనేట్',
        'Calcium chloride / కాల్షియం క్లోరైడ్',
        'Sodium carbonate / సోడియం కార్బోనేట్',
        'A',
        'M',
        '',
        33
    ),
    (
        'Water is neither acidic nor alkaline because\nతెలుగు: నీరు ఆమ్లం కాదు మరియు క్షారం కాదు ఎందుకంటే:',
        'It cannot accept or donate protons / ఇది ప్రోటాన్\u200cలను స్వీకరించలేదు లేదా దానం చేయలేదు',
        'It boils at a high temperature / ఇది అధిక ఉష్ణోగ్రత వద్ద మరుగుతుంది',
        'It can dissociate into an equal number of hydrogen ions and hydroxyl ions / ఇది సమాన సంఖ్యలో హైడ్రోజన్ అయాన్లుగా మరియు హైడ్రాక్సిల్ అయాన్లుగా విడిపోగలదు',
        'It cannot donate or accept electrons / ఇది ఎలక్ట్రాన్\u200cలను దానం చేయలేదు లేదా స్వీకరించలేదు',
        'C',
        'M',
        '',
        34
    ),
    (
        'A 100 mL solution having 0.01 moles of NaOH dissolved in it. The pH of the solution is:\nతెలుగు: 100 mL ద్రావణంలో 0.01 మోల్స్ NaOH కరిగి ఉంది. అయితే ఆ ద్రావణం యొక్క pH ఎంత',
        '13 / 13',
        '1 / 1',
        '10 / 10',
        '2 / 2',
        'A',
        'M',
        '',
        35
    ),
    (
        'Superphosphate fertilizer is prepared by the reaction between\nతెలుగు: సూపర్ ఫాస్ఫేట్ ఎరువు వేటి మధ్య జరిగే చర్య ద్వారా తయారవుతుంది',
        'Calcium phosphate and Sulphuric acid / కాల్షియం ఫాస్ఫేట్ మరియు సల్ఫ్యూరిక్ ఆమ్లం',
        'Sodium phosphate and Sodium nitrate / సోడియం ఫాస్ఫేట్ మరియు సోడియం నైట్రేట్',
        'Magnesium phosphate and Sodium nitrate / మెగ్నీషియం ఫాస్ఫేట్ మరియు సోడియం నైట్రేట్',
        'Sodium sulfate and Phosphoric acid / సోడియం సల్ఫేట్ మరియు ఫాస్పోరిక్ ఆమ్లం',
        'A',
        'M',
        '',
        36
    ),
    (
        'The final products of combustion of ethane are\nతెలుగు: ఈథేన్ దహనం చెందినప్పుడు ఏర్పడే తుది ఉత్పత్తులు ఏవి',
        'Carbon and Oxygen / కార్బన్ మరియు ఆక్సిజన్',
        'Ethylene and Hydrogen / ఇథిలీన్ మరియు హైడ్రోజన్',
        'Water and Carbon monoxide / నీరు మరియు కార్బన్ మోనాక్సైడ్',
        'Carbon dioxide and water / కార్బన్ డైయాక్సైడ్ మరియు నీరు',
        'D',
        'M',
        '',
        37
    ),
    (
        'Which of the following metals can displace zinc from a solution of zinc sulfate\nతెలుగు: జింక్ సల్ఫేట్ ద్రావణం నుండి కింది ఏ లోహం జింక్\u200cను స్థానభ్రంశం చేయగలదు',
        'Lead / సీసం',
        'Magnesium / మెగ్నీషియం (Magnesium)',
        'Iron / ఇనుము',
        'Mercury / పాదరసం',
        'B',
        'M',
        '',
        38
    ),
    (
        'Chemical change does not take place in the case of\nతెలుగు: కింది వాటిలో దేనిలో రసాయన మార్పు జరగదు',
        'Souring of milk into curd / పాలు పులిసి పెరుగుగా మారడం',
        'Rusting of iron in the atmosphere / వాతావరణంలో ఇనుము తుప్పు పట్టడం',
        'Burning of magnesium ribbon in air / గాలిలో మెగ్నీషియం రిబ్బన్ మండటం',
        'Emitting of light by a red-hot platinum wire / ఎర్రగా కాలిన ప్లాటినం తీగ నుండి కాంతి వెలువడటం',
        'D',
        'M',
        '',
        39
    ),
    (
        'Which of the following is an example of a chemical change\nతెలుగు: కింది వాటిలో రసాయన మార్పుకు ఉదాహరణ ఏది',
        'Burning wood / కలప మండటం (Burning wood)',
        'Cutting paper / కాగితాన్ని కత్తిరించడం',
        'Boiling water / నీరు మరగడం',
        'Melting ice / మంచు కరగడం',
        'A',
        'M',
        '',
        40
    ),
    (
        'Which of the following causes the rusting of iron? Statements: (1) Oxidation, (2) Reduction, (3) Reaction with oxygen, (4) Reaction with CO2.\nతెలుగు: ఇనుము తుప్పు పట్టడానికి కారణమయ్యేవి కింది వాటిలో ఏవి? వ్యాఖ్యలు: (1) ఆక్సీకరణ (2) క్షయకరణ (3) ఆక్సిజన్\u200cతో రసాయన చర్య (4) CO2 తో రసాయన చర్య',
        '1 and 2 / 1 మరియు 2',
        '2 and 3 / 2 మరియు 3',
        '1 and 3 / 1 మరియు 3',
        '3 and 4 / 3 మరియు 4',
        'C',
        'M',
        '',
        41
    ),
    (
        'Which of the following solutions is slightly acidic due to hydrolysis\nతెలుగు: జలవిశ్లేషణ కారణంగా కింది ఏ ద్రావణం కొద్దిగా ఆమ్లత్వాన్ని కలిగి ఉంటుంది',
        'NH4CH3COO / NH4CH3COO',
        'NH4Cl / NH4Cl',
        'Na2CO3 / Na2CO3',
        'CH3COONa / CH3COONa',
        'B',
        'M',
        '',
        42
    ),
    (
        'What happens to the particles of a substance when it is heated\nతెలుగు: ఒక పదార్థాన్ని వేడి చేసినప్పుడు దానిలోని కణాలకు ఏమవుతుంది',
        'They stop moving / కదలడం ఆగిపోతాయి',
        'They disappear / అదృశ్యమవుతాయి',
        'They move faster / అవి వేగంగా కదులుతాయి',
        'They move slower / అవి నెమ్మదిగా కదులుతాయి',
        'C',
        'M',
        '',
        43
    ),
    (
        "The pink color of Baeyer's reagent is discharged when acetylene is passed through it. This is due to the formation of\nతెలుగు: బేయర్స్ కారకం గుండా ఎసిటిలీన్\u200cను పంపినప్పుడు దాని గులాబీ రంగు తొలగిపోతుంది. ఇది దేని ఏర్పాటు కారణంగా జరుగుతుంది",
        'Acetic acid / ఎసిటిక్ ఆమ్లం',
        'Ethylene / ఇథిలీన్',
        'Water / నీరు',
        'Oxalic acid / ఆక్సాలిక్ ఆమ్లం (Oxalic acid)',
        'D',
        'M',
        '',
        44
    ),
    (
        'The process of separating grains from the chaff is known as\nతెలుగు: పొట్టు నుండి ధాన్యపు గింజలను వేరుచేసే పద్ధతిని ఏమంటారు',
        'Weeding / కలుపు తీయడం',
        'Harvesting / కోత కోయడం',
        'Threshing / నూర్పిడి చేయడం',
        'Winnowing / తూర్పారబట్టడం (Winnowing)',
        'D',
        'M',
        '',
        45
    ),
    (
        'Match the following: A. Hydrogenation, B. Evaporation, C. Distillation, D. Polymerisation paired with: 1. Vanaspati, 2. Common salt, 3. Ethyl alcohol, 4. Nylon.\nతెలుగు: కింది వాటిని జతపరచండి: A. హైడ్రోజనీకరణ B. భాష్పీభవనం C. స్వేదనం D. పాలిమరైజేషన్ తో జతపరచండి: 1. వనస్పతి 2. సాధారణ ఉప్పు 3. ఇథైల్ ఆల్కహాల్ 4. నైలాన్',
        'A-1, B-2, C-3, D-4 / A-1, B-2, C-3, D-4',
        'A-2, B-1, C-3, D-4 / A-2, B-1, C-3, D-4',
        'A-2, B-4, C-1, D-3 / A-2, B-4, C-1, D-3',
        'A-3, B-2, C-1, D-4 / A-3, B-2, C-1, D-4',
        'A',
        'M',
        '',
        46
    ),
    (
        'A mixture of salt and sand can be separated by\nతెలుగు: ఉప్పు మరియు ఇసుకల మిశ్రమాన్ని ఏ విధంగా వేరు చేయవచ్చు',
        'Sublimation / ఉత్పతనం',
        'Dissolving in water / నీటిలో కరిగించడం (Dissolving in water)',
        'Gravity separation / గురుత్వాకర్షణ వేర్పాటు',
        'Dry distillation / డ్రై డిస్టిలేషన్',
        'B',
        'M',
        '',
        47
    ),
    (
        'The process by which an organic compound breaks down into simpler compounds on heating to high temperature is known as\nతెలుగు: కర్బన సమ్మేళనాన్ని అధిక ఉష్ణోగ్రతకు వేడి చేయడం ద్వారా సరళమైన సమ్మేళనాలుగా విడగొట్టే ప్రక్రియను ఏమంటారు',
        'Aromatization / ఆరోమాటిజేషన్',
        'Polymerization / పాలిమరైజేషన్',
        'Pyrolysis / పైరాలసిస్ (Pyrolysis)',
        'Reduction / క్షయకరణ',
        'C',
        'M',
        '',
        48
    ),
    (
        'Which of the following metals react with nitrogen at room temperature to form nitride\nతెలుగు: గది ఉష్ణోగ్రత వద్ద నైట్రోజన్\u200cతో చర్య జరిపి నైట్రైడ్\u200cను ఏర్పరిచే లోహం కింది వాటిలో ఏది',
        'Sodium / సోడియం',
        'Potassium / పొటాషియం',
        'Magnesium / మెగ్నీషియం (Magnesium)',
        'None of these / ఇవేవీ కావు',
        'C',
        'M',
        '',
        49
    ),
    (
        'What happens when an acid or a base is mixed with water\nతెలుగు: ఒక ఆమ్లాన్ని లేదా క్షారాన్ని నీటితో కలిపినప్పుడు ఏమి జరుగుతుంది',
        'Increase in concentration of ions per litre / లీటరు ఘనపరిమాణంలో అయాన్ల గాఢత పెరుగుతుంది',
        'Decrease in concentration of ions per litre / లీటరు ఘనపరిమాణంలో అయాన్ల గాఢత తగ్గుతుంది',
        'Increase in concentration of ions per unit volume / ప్రమాణ ఘనపరిమాణంలో అయాన్ల గాఢత పెరుగుతుంది',
        'Decrease in concentration of ions per unit volume / ప్రమాణ ఘనపరిమాణంలో అయాన్ల గాఢత తగ్గుతుంది',
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
