import sqlite3, os

SOURCE = 'Science_Set9_Appliances_Devices'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    (
        'In an ordinary dry cell, the electrolyte is\nతెలుగు: సాధారణ డ్రై సెల్ (పొడి ఘటం)లో ఎలక్ట్రోలైట్ (విద్యుద్విశ్లేష్యము) ఏది',
        'sulphuric acid / సల్ఫ్యూరిక్ ఆమ్లం',
        'manganese dioxide / మాంగనీస్ డయాక్సైడ్',
        'ammonium chloride / అమ్మోనియం క్లోరైడ్',
        'zinc / జింక్',
        'C',
        'M',
        '',
        1
    ),
    (
        'Cylinder 2. Spark plug 3. Piston\nతెలుగు: డీజిల్ ఇంజిన్\u200cలో కింది వాటిలో ఏవి ఉపయోగించబడతాయి?',
        '1, 2 and 3',
        '1 and 2',
        '2 and 3',
        '1 and 3',
        'D',
        'M',
        '',
        1
    ),
    (
        'Safety wire used in domestic electrical appliances is made of a metal of\nతెలుగు: గృహ విద్యుత్ పరికరాలలో ఉపయోగించే సేఫ్టీ వైర్ (ఫ్యూజ్ తీగ) దేనితో తయారు చేయబడుతుంది',
        'low melting point / తక్కువ ద్రవీభవన స్థానం (low melting point) గల లోహంతో',
        'low specific gravity / తక్కువ విశిష్ట గురుత్వం గల లోహంతో',
        'low resistance / తక్కువ నిరోధం గల లోహంతో',
        'None of the above / పైవేవీ కావు',
        'A',
        'M',
        '',
        2
    ),
    (
        'The device that separates light into its component wave length is\nతెలుగు: కాంతిని దాని అనుబంధ తరంగదైర్ఘ్యాలుగా విభజించే పరికరం ఏది',
        'Photometer / ఫోటోమీటర్',
        'Interferometer / ఇంటర్\u200cఫెరోమీటర్',
        'Spectrometer / స్పెక్ట్రోమీటర్',
        'Polarimeter / పోలారిమీటర్',
        'B',
        'M',
        '',
        3
    ),
    (
        "Which of the following works on Bernoulli's principle\nతెలుగు: కింది వాటిలో బెర్నౌలీ సూత్రంపై (Bernoulli's principle) పనిచేసేది ఏది",
        'Gas lighter / గ్యాస్ లైటర్',
        'Gas stove / గ్యాస్ స్టవ్',
        'Bunsen burner / బున్సెన్ బర్నర్',
        'None of these / ఇవేవీ కావు',
        'C',
        'M',
        '',
        4
    ),
    (
        "The term 'Black Box' is more commonly used in relation to which of the following\nతెలుగు: 'బ్లాక్ బాక్స్' (Black Box) అనే పదాన్ని సాధారణంగా కింది వాటిలో దేనికి సంబంధించి ఉపయోగిస్తారు",
        'It is a box in which high grade uranium is kept to prevent radiation. / వికిరణాన్ని నివారించడానికి హై-గ్రేడ్ యురేనియం ఉంచబడిన పెట్టె.',
        'It is a time capsule in which records of important events are kept to be opened at a later date. / ముఖ్యమైన సంఘటనల రికార్డులను భవిష్యత్తు కోసం భద్రపరిచే టైమ్ క్యాప్సూల్.',
        'It is a flight recorder in an airplane. / విమానంలోని ఫ్లైట్ రికార్డర్.',
        'None of these / ఇవేవీ కావు.',
        'C',
        'M',
        '',
        5
    ),
    (
        'Fish plates in railway track are used\nతెలుగు: రైల్వే ట్రాక్\u200cలో ఫిష్ ప్లేట్\u200cలను (Fish plates) ఎందుకు ఉపయోగిస్తారు',
        'To join two coaches / రెండు కోచ్\u200cలను కలపడానికి',
        '& / &',
        'above / రెండూ',
        'Both / పై',
        'B',
        'M',
        '',
        6
    ),
    (
        'The mixed oxide fuel is used for which of the following\nతెలుగు: మిక్స్\u200cడ్ ఆక్సైడ్ ఇంధనాన్ని (mixed oxide fuel) కింది వాటిలో దేనికి ఉపయోగిస్తారు',
        'Nuclear Reactors / న్యూక్లియర్ రియాక్టర్లు',
        'Aeroplanes / విమానాలు',
        'Cryogenic Engines / క్రయోజెనిక్ ఇంజన్లు',
        'PSLV rockets / PSLV రాకెట్లు',
        'A',
        'M',
        '',
        7
    ),
    (
        'The jet plane engine works on the principle of\nతెలుగు: జెట్ విమాన ఇంజిన్ ఏ సూత్రంపై పనిచేస్తుంది',
        'Mass / ద్రవ్యరాశి',
        'Linear momentum / రేఖీయ ద్రవ్యవేగం (Linear momentum)',
        'Energy / శక్తి',
        'Angular momentum / కోణీయ ద్రవ్యవేగం',
        'B',
        'M',
        '',
        8
    ),
    (
        'Sodium vapour lamps are preferred over incandescent lamp because of\nతెలుగు: ప్రకాశించే (incandescent) బల్బుల కంటే సోడియం వేపర్ ల్యాంప్\u200cలకు ప్రాధాన్యత ఇవ్వడానికి కారణం ఏమిటి',
        'Higher tolerance to voltage fluctuation / వోల్టేజ్ హెచ్చుతగ్గులను ఎక్కువగా తట్టుకోవడం',
        'Higher intensity of illumination / అధిక కాంతి తీవ్రత (Higher intensity of illumination)',
        'Easy installation / సులభమైన ఇన్\u200cస్టాలేషన్',
        'None of these / ఇవేవీ కావు',
        'B',
        'M',
        '',
        9
    ),
    (
        'The principle of working of periscope is based on\nతెలుగు: పెరిస్కోప్ పనిచేసే సూత్రం దేనిపై ఆధారపడి ఉంటుంది',
        'Reflection only / పరావర్తనం (Reflection) మాత్రమే',
        'Refraction only / వక్రీభవనం మాత్రమే',
        'Reflection and refraction / పరావర్తనం మరియు వక్రీభవనం',
        'Reflection and interference / పరావర్తనం మరియు వ్యతికరణం',
        'A',
        'M',
        '',
        10
    ),
    (
        "A pyranometer is a measuring instrument, commonly used for climate research or monitoring weather performance.\nతెలుగు: వాతావరణ పరిశోధనలలో సాధారణంగా ఉపయోగించే కొలిచే పరికరం 'పైరనోమీటర్' (pyranometer) దేనిని కొలుస్తుంది",
        'Solar irradiance / సౌర వికిరణం (Solar irradiance)',
        'Atmospheric pressure / వాతావరణ పీడనం',
        'Wind speed / గాలి వేగం',
        'Cloud ceiling / క్లౌడ్ సీలింగ్',
        'A',
        'M',
        '',
        11
    ),
    (
        'Conversion of chemical energy into electrical energy occurs in\nతెలుగు: రసాయన శక్తి విద్యుత్ శక్తిగా ఎందులో మారుతుంది',
        'Dynamos / డైనమోలు',
        'Electric heaters / ఎలక్ట్రిక్ హీటర్లు',
        'Battery / బ్యాటరీ',
        'Atomic bombs / ఆటం బాంబులు',
        'C',
        'M',
        '',
        12
    ),
    (
        'With which of the following instruments can a sailor in a submarine see the objects on the surface of sea\nతెలుగు: జలాంతర్గామిలోని నావికుడు సముద్ర ఉపరితలంపై ఉన్న వస్తువులను ఏ పరికరం ద్వారా చూడగలడు',
        'Periscope / పెరిస్కోప్ (Periscope)',
        'Telescope / టెలిస్కోప్',
        'Gyroscope / గైరోస్కోప్',
        'Steroscope / స్టీరియోస్కోప్',
        'A',
        'M',
        '',
        13
    ),
    (
        'The working of the quartz crystal in the watch is based on\nతెలుగు: గడియారంలో క్వార్ట్జ్ స్పటికం (quartz crystal) పనిచేసే విధానం దేనిపై ఆధారపడి ఉంటుంది',
        'Johnson effect / జాన్సన్ ఎఫెక్ట్',
        'Photoelectric effect / ఫోటోఎలక్ట్రిక్ ఎఫెక్ట్',
        'Edison effect / ఎడిసన్ ఎఫెక్ట్',
        'Piezo electric effect / పీజో ఎలక్ట్రిక్ ఎఫెక్ట్ (Piezo electric effect)',
        'D',
        'M',
        '',
        14
    ),
    (
        'Dialyzer is a/an\nతెలుగు: డయలైజర్ (Dialyzer) అనేది:',
        'Meter used for controlling volume of sound / ధ్వని పరిమాణాన్ని నియంత్రించడానికి ఉపయోగించే మీటర్',
        'Apparatus used for recharging batteries / బ్యాటరీలను రీఛార్జ్ చేయడానికి ఉపయోగించే ఉపకరణం',
        'Special clock which indicates the day and date / రోజు మరియు తేదీని సూచించే ప్రత్యేక గడియారం',
        'Apparatus sometimes used in patients with defective renal function / మూత్రపిండాల (renal) పనితీరు లోపించిన రోగులలో ఉపయోగించే పరికరం',
        'D',
        'M',
        '',
        15
    ),
    (
        "The number of points in a Mariner's compass is\nతెలుగు: మ్యాగ్నెటిక్ కంపాస్ (Mariner's compass) లో ఎన్ని పాయింట్లు ఉంటాయి",
        '64 / 64',
        '32 / 32',
        '24 / 24',
        '8 / 8',
        'B',
        'M',
        '',
        16
    ),
    (
        'Which of the following combinations of aperture and shutter speed of a camera will allow the maximum exposure\nతెలుగు: కెమెరా యొక్క ఎపర్చరు మరియు షట్టర్ స్పీడ్ కలయికలలో కింది వాటిలో ఏది గరిష్ట ఎక్స్\u200cపోజర్\u200cను అనుమతిస్తుంది',
        'F 5.6, 1/1000 / F 5.6, 1/1000',
        'F-8, 1/250 / F-8, 1/250',
        'F-16, 1/125 / F-16, 1/125',
        'F-22, 1/60 / F-22, 1/60',
        'B',
        'M',
        '',
        17
    ),
    (
        'Hardware is related to\nతెలుగు: హార్డ్\u200cవేర్ (Hardware) కింది వాటిలో దేనికి సంబంధించినది',
        'Calculator / క్యాలిక్యులేటర్',
        'Computers / కంప్యూటర్లు (Computers)',
        'Acids / ఆమ్లాలు',
        'Heavy metals / భార లోహాలు',
        'B',
        'M',
        '',
        18
    ),
    (
        'Which of the following is the combination of the three primary colours used in colour TV\nతెలుగు: కలర్ టీవీలో ఉపయోగించే మూడు ప్రాథమిక రంగుల కలయిక ఏది',
        'Green, Blue, Red / ఆకుపచ్చ, నీలం, ఎరుపు (Green, Blue, Red)',
        'Red, Green, Yellow / ఎరుపు, ఆకుపచ్చ, పసుపు',
        'Green, Yellow, Blue / ఆకుపచ్చ, పసుపు, నీలం',
        'Yellow, Blue, Red / పసుపు, నీలం, ఎరుపు',
        'A',
        'M',
        '',
        20
    ),
    (
        'AC cannot be used in\nతెలుగు: AC (ఆల్టర్నేటింగ్ కరెంట్) ని దేనిలో ఉపయోగించలేము',
        'Amplifier / యాంప్లిఫైయర్',
        'Transformer / ట్రాన్స్\u200cఫార్మర్',
        'Voltmeter / వోల్టమీటర్',
        'Galvanometer / గాల్వనోమీటర్',
        'D',
        'M',
        '',
        21
    ),
    (
        'Which of the following best explains the phenomenon \\"Simple Harmonic Motion\\"\nతెలుగు: \\"సింపుల్ హార్మోనిక్ మోషన్\\" (సరళ హరాత్మక చలనం) దృగ్విషయాన్ని కింది వాటిలో ఏది ఉత్తమంగా వివరిస్తుంది',
        'Cylinder / స్తూపం (Cylinder)',
        'Disc / డిస్క్',
        'Pendulum / లోలకం (Pendulum)',
        'None of these / ఇవేవీ కావు',
        'C',
        'M',
        '',
        22
    ),
    (
        'Match the following: A. Petrol engine 1. Compression B. Diesel engine 2. Spark plug C. Ship 3. Turboprop D. Jet aircraft 4. Propeller\nతెలుగు: కింది వాటిని జతపరచండి: A. పెట్రోల్ ఇంజిన్ - 1. కంప్రెషన్ B. డీజిల్ ఇంజిన్ - 2. స్పార్క్ ప్లగ్ C. ఓడ - 3. టర్బోప్రాప్ D. జెట్ విమానం - 4. ప్రొపెల్లర్',
        '1, 2, 3, 4 / A-1, B-2, C-3, D-4',
        '2, 1, 4, 3 / A-2, B-1, C-4, D-3',
        '1, 2, 4, 3 / A-1, B-2, C-4, D-3',
        '2, 1, 3, 4 / A-2, B-1, C-3, D-4',
        'B',
        'M',
        '',
        23
    ),
    (
        'For which of the following is a diode used\nతెలుగు: కింది వాటిలో దేనికి డయోడ్\u200cను (diode) ఉపయోగిస్తారు',
        'Rectification / ఏకదిక్కరణం (Rectification)',
        'Amplification / యాంప్లిఫికేషన్',
        'Modulation / మాడ్యులేషన్',
        'Oscillation / ఆసిలేషన్',
        'A',
        'M',
        '',
        24
    ),
    (
        'Jet engines are\nతెలుగు: జెట్ ఇంజన్లు అనేవి ఏ రకమైన ఇంజన్లు',
        'Rotary engines / రోటరీ ఇంజన్లు',
        'Turbine engines / టర్బైన్ ఇంజన్లు',
        'External combustion engines / బాహ్య దహన యంత్రాలు',
        'Reaction engines / రియాక్షన్ ఇంజన్లు (Reaction engines)',
        'D',
        'M',
        '',
        25
    ),
    (
        'Rocket works on the principle of\nతెలుగు: రాకెట్ ఏ సూత్రం ఆధారంగా పనిచేస్తుంది',
        'Conservation of mass / ద్రవ్యరాశి నిత్యత్వ నియమం',
        'Conservation of energy / శక్తి నిత్యత్వ నియమం',
        'Conservation of momentum / ద్రవ్యవేగ నిత్యత్వ నియమం (Conservation of momentum)',
        'None of these / ఇవేవీ కావు',
        'C',
        'M',
        '',
        26
    ),
    (
        'The spring balance works on the principle of\nతెలుగు: స్ప్రింగ్ బ్యాలెన్స్ (స్ర్పింగ్ త్రాసు) ఏ సూత్రంపై పనిచేస్తుంది',
        "Boyle's law / బాయిల్ నియమం",
        "Hooke's law / హుక్ నియమం (Hooke's law)",
        "Bernoulli's principle / బెర్నౌలీ సూత్రం",
        "Pascal's law / పాస్కల్ నియమం",
        'B',
        'M',
        '',
        27
    ),
    (
        'What is the nature of motion of machine needle\nతెలుగు: కుట్టు యంత్రం సూది యొక్క చలన స్వభావం ఏమిటి',
        'Rotatory and oscillatory / భ్రమణ మరియు డోలన చలనం',
        'Oscillatory and translatory / డోలన మరియు స్థానాంతర చలనం (Oscillatory and translatory)',
        'Rotatory and translatory / భ్రమణ మరియు స్థానాంతర చలనం',
        'Vibratory and rotator / కంపన మరియు భ్రమణ చలనం',
        'B',
        'M',
        '',
        28
    ),
    (
        'In an engine run on diesel, ignition is caused through-\nతెలుగు: డీజిల్\u200cతో నడిచే ఇంజిన్\u200cలో ఇగ్నిషన్ (మండటం) దేని ద్వారా జరుగుతుంది',
        'Friction / ఘర్షణ',
        'Automatic starter / ఆటోమేటిక్ స్టార్టర్',
        'Spark plug / స్పార్క్ ప్లగ్',
        'Compression / కంప్రెషన్ (కుదింపు/Compression)',
        'D',
        'M',
        '',
        29
    ),
    (
        'In an electronic watch, the component corresponding to the pendulum of a pendulum clock is\nతెలుగు: ఎలక్ట్రానిక్ గడియారంలో, లోలక గడియారం యొక్క లోలకానికి (pendulum) సమానమైన భాగం ఏది',
        'Transistor / ట్రాన్సిస్టర్',
        'Balance Wheel / బ్యాలెన్స్ వీల్',
        'Crystal Oscillator / క్రిస్టల్ ఆసిలేటర్ (Crystal Oscillator)',
        'Diode / డయోడ్',
        'C',
        'M',
        '',
        30
    ),
    (
        'The silvered surface of thermos flask prevents transfer of heat by\nతెలుగు: థర్మోస్ ఫ్లాస్క్ లోపలి వెండి పూత దేని ద్వారా ఉష్ణ బదిలీని నిరోధిస్తుంది',
        'Conduction / ఉష్ణ వాహనం',
        'Convection / ఉష్ణ సంవహనం',
        'Radiation / ఉష్ణ వికిరణం (Radiation)',
        'All of these / ఇవన్నీ',
        'C',
        'M',
        '',
        31
    ),
    (
        'The hydraulic brakes used in automobiles is a direct application of\nతెలుగు: వాహనాలలో ఉపయోగించే హైడ్రాలిక్ బ్రేక్\u200cలు దేని యొక్క ప్రత్యక్ష అనువర్తనం',
        "Archimedes' Principle / ఆర్కిమెడిస్ సూత్రం",
        'Toricellian law / టోరిసెల్లి నియమం',
        "Bernoulli's theorem / బెర్నౌలీ సిద్ధాంతం",
        "Pascal's law / పాస్కల్ నియమం (Pascal's law)",
        'D',
        'M',
        '',
        32
    ),
    (
        'Cryogenic engines find applications in\nతెలుగు: క్రయోజెనిక్ ఇంజన్ల అనువర్తనం కింది వాటిలో ఎందులో ఉంటుంది',
        'Rocket technology / రాకెట్ టెక్నాలజీ',
        'Frost free refrigerators / ఫ్రాస్ట్ ఫ్రీ రిఫ్రిజిరేటర్లు',
        'Sub-marine propulsion / సబ్\u200cమెరైన్ ప్రొపల్షన్',
        'Researches in superconductivity / సూపర్\u200cకండక్టివిటీ పరిశోధనలు',
        'A',
        'M',
        '',
        33
    ),
    (
        'Ball bearing are used to reduce friction by\nతెలుగు: బాల్ బేరింగ్\u200cలను ఉపయోగించి ఘర్షణను ఎలా తగ్గిస్తారు',
        'Applying lubricants to the balls used / బంతులకు కందెనలు రాయడం ద్వారా',
        'Reducing the area of contact with the use of metallic balls / లోహపు బంతులను ఉపయోగించి స్పర్శా వైశాల్యాన్ని (area of contact) తగ్గించడం ద్వారా',
        'Increasing the area contact with the use of metallic balls / లోహపు బంతులను ఉపయోగించి స్పర్శా వైశాల్యాన్ని పెంచడం ద్వారా',
        'None of these / ఇవేవీ కావు',
        'B',
        'M',
        '',
        34
    ),
    (
        'The anode in a dry cell consists of\nతెలుగు: డ్రై సెల్ (పొడి ఘటం) లోని యానోడ్ (anode) దేనితో తయారవుతుంది',
        'Graphite / గ్రాఫైట్',
        'Zinc / జింక్',
        'Copper / రాగి',
        'Cadmium / కాడ్మియం',
        'A',
        'M',
        '',
        35
    ),
    (
        'Theodolite is an instrument used by\nతెలుగు: థియోడోలైట్ (Theodolite) అనేది ఎవరు ఉపయోగించే పరికరం',
        'Pilots / పైలట్లు',
        'Navigators / నావిగేటర్లు',
        'Cartographers / కార్టోగ్రాఫర్లు',
        'Surveyors / సర్వేయర్లు (Surveyors)',
        'D',
        'M',
        '',
        36
    ),
    (
        'A triode differs from a diode\nతెలుగు: ట్రయోడ్ (triode), డయోడ్ (diode) నుండి ఏ విధంగా భిన్నంగా ఉంటుంది',
        'It has vacuum inside / దాని లోపల శూన్యం ఉంటుంది',
        'Its current is caused by photoelectric effect / దాని కరెంట్ ఫోటోఎలక్ట్రిక్ ఎఫెక్ట్ వల్ల ఏర్పడుతుంది',
        'It can amplify a signal / ఇది సిగ్నల్\u200cను యాంప్లిఫై (amplify) చేయగలదు',
        'It has a heated cathode / ఇది వేడిచేసిన కాథోడ్\u200cను కలిగి ఉంటుంది',
        'C',
        'M',
        '',
        37
    ),
    (
        'In a refrigerator, cooling is produced by\nతెలుగు: రిఫ్రిజిరేటర్\u200cలో, శీతలీకరణ (cooling) దేని ద్వారా ఉత్పత్తి అవుతుంది',
        'The ice which deposits on the freezer / ఫ్రీజర్\u200cపై పేరుకుపోయే మంచు ద్వారా',
        'The sudden expansion of a compressed gas / కంప్రెస్డ్ గ్యాస్ ఆకస్మిక వ్యాకోచం ద్వారా',
        'The evaporation of a volatile liquid / బాష్పశీల ద్రవం యొక్క భాష్పీభవనం ద్వారా (evaporation of a volatile liquid)',
        'None of these / ఇవేవీ కావు',
        'C',
        'M',
        '',
        38
    ),
    (
        'The conversion of electrical energy into chemical energy is observed in\nతెలుగు: విద్యుత్ శక్తి రసాయన శక్తిగా మారడాన్ని ఎందులో గమనించవచ్చు',
        'Fan / ఫ్యాన్',
        'Storage battery / స్టోరేజ్ బ్యాటరీ (Storage battery)',
        'Heater / హీటర్',
        'Incandescent bulb / ప్రకాశించే బల్బ్',
        'B',
        'M',
        '',
        39
    ),
    (
        'The most efficient engine is\nతెలుగు: అత్యంత సమర్థవంతమైన (efficient) ఇంజిన్ ఏది',
        'Petrol / పెట్రోల్',
        'Diesel / డీజిల్',
        'Electric / ఎలక్ట్రిక్ (Electric)',
        'Steam / స్టీమ్',
        'C',
        'M',
        '',
        40
    ),
    (
        'Match the following: Instrument - use A. Microscope - 1. To see objects on the surface by an observer in a trench B. Telescope - 2. To see small particles C. Periscope - 3. To see distant objects D. Gramophone - 4. To detect the direction by sailors 5. To hear music or songs\nతెలుగు: కింది పరికరాలను వాటి ఉపయోగాలతో జతపరచండి: A. మైక్రోస్కోప్ - 1. కందకంలో ఉన్న పరిశీలకుడు ఉపరితలంపై ఉన్న వస్తువులను చూడటానికి B. టెలిస్కోప్ - 2. చిన్న కణాలను చూడటానికి C. పెరిస్కోప్ - 3. సుదూర వస్తువులను చూడటానికి D. గ్రామఫోన్ - 4. నావికులు దిశను గుర్తించడానికి 5. సంగీతం లేదా పాటలు వినడానికి',
        '1, 2, 3, 5 / A-1, B-2, C-3, D-5',
        '2, 3, 5, 1 / A-2, B-3, C-5, D-1',
        '2, 3, 1, 5 / A-2, B-3, C-1, D-5',
        '2, 1, 5, 4 / A-2, B-1, C-5, D-4',
        'C',
        'M',
        '',
        41
    ),
    (
        'The tape of a tape recorder is coated with\nతెలుగు: టేప్ రికార్డర్ యొక్క టేప్\u200cపై దేని పూత ఉంటుంది',
        'Zinc oxide / జింక్ ఆక్సైడ్',
        'Copper sulphate / కాపర్ సల్ఫేట్',
        'Mica / మైకా',
        'Ferromagnetic powder / ఫెర్రో అయస్కాంత పొడి (Ferromagnetic powder)',
        'D',
        'M',
        '',
        42
    ),
    (
        'The technique used to transmit audio signals in television broadcasts is\nతెలుగు: టెలివిజన్ ప్రసారాలలో ఆడియో సిగ్నల్\u200cలను ప్రసారం చేయడానికి ఉపయోగించే పద్ధతి ఏది',
        'Amplitude Modulation / ఆంప్లిట్యూడ్ మాడ్యులేషన్ (AM)',
        'Frequency Modulation / ఫ్రీక్వెన్సీ మాడ్యులేషన్ (FM)',
        'Pulse Code Modulation / పల్స్ కోడ్ మాడ్యులేషన్',
        'Time Division Multiplexing / టైమ్ డివిజన్ మల్టీప్లెక్సింగ్',
        'B',
        'M',
        '',
        43
    ),
    (
        'Distant objects can be seen with the help of\nతెలుగు: సుదూర వస్తువులను కింది వాటిలో దేని సహాయంతో చూడవచ్చు',
        'Cronometer / క్రోనోమీటర్',
        'Microscope / మైక్రోస్కోప్',
        'Telescope / టెలిస్కోప్ (Telescope)',
        'Spectroscope / స్పెక్ట్రోస్కోప్',
        'C',
        'M',
        '',
        44
    ),
    (
        'The safety fuse should have\nతెలుగు: సేఫ్టీ ఫ్యూజ్ (Safety fuse) కు ఏ లక్షణాలు ఉండాలి',
        'High resistance and high melting point / అధిక నిరోధం మరియు అధిక ద్రవీభవన స్థానం',
        'High resistance and low melting point / అధిక నిరోధం మరియు తక్కువ ద్రవీభవన స్థానం (High resistance and low melting point)',
        'Low resistance and high melting point / తక్కువ నిరోధం మరియు అధిక ద్రవీభవన స్థానం',
        'Low resistance and low melting / తక్కువ నిరోధం మరియు తక్కువ ద్రవీభవన స్థానం',
        'B',
        'M',
        '',
        45
    ),
    (
        'Aviation fuel fro jet aeroplanes consists of purified\nతెలుగు: జెట్ విమానాలకు ఉపయోగించే ఏవియేషన్ ఇంధనంలో శుద్ధి చేయబడిన ఏది ఉంటుంది',
        'Petrol / పెట్రోల్',
        'Kerosene / కిరోసిన్ (Kerosene)',
        'Gasoline / గ్యాసోలిన్',
        'Diesel / డీజిల్',
        'B',
        'M',
        '',
        46
    ),
    (
        'Filter Beds used to remove suspended impurities from municipal water consist of\nతెలుగు: మున్సిపల్ నీటి నుండి తేలియాడే మలినాలను తొలగించడానికి ఉపయోగించే ఫిల్టర్ బెడ్\u200cలలో ఏముంటాయి',
        'Fine sand / సన్నని ఇసుక',
        'Gravel / కంకర (Gravel)',
        'Charcoal / చార్\u200cకోల్',
        'All of these / ఇవన్నీ (All of these)',
        'D',
        'M',
        '',
        47
    ),
    (
        'The best colour(s) for a sun umbrella will be\nతెలుగు: ఎండ గొడుగు (sun umbrella) కు ఉత్తమమైన రంగు(లు) ఏవి',
        'Black / నలుపు',
        'Black on top and white on the inside / పైభాగంలో నలుపు మరియు లోపలి భాగంలో తెలుపు',
        'White on top and black on the inside / పైభాగంలో తెలుపు మరియు లోపలి భాగంలో నలుపు',
        'Printed with all the seven colours of rainbow / ఇంద్రధనుస్సులోని ఏడు రంగులతో ముద్రించినది',
        'C',
        'M',
        '',
        48
    ),
    (
        'A transistor is most likely to be found in a\nతెలుగు: ట్రాన్సిస్టర్\u200cను కింది వాటిలో దేనిలో కనుగొనే అవకాశం ఎక్కువగా ఉంది',
        'Wrist watch / చేతి గడియారం',
        'Fused / ఫ్యూజ్డ్',
        'Hearing aid / హియరింగ్ ఎయిడ్ (వినే పరికరం)',
        'Fluorescent lamp / ఫ్లోరోసెంట్ దీపం',
        'C',
        'M',
        '',
        49
    ),
    (
        'Which of the following polymers is widely used for making bullet proof material\nతెలుగు: బుల్లెట్ ప్రూఫ్ మెటీరియల్ తయారీకి కింది పాలిమర్\u200cలలో ఏది విస్తృతంగా ఉపయోగించబడుతుంది',
        'Polyethylene / పాలిథిలిన్',
        'Polyamides / పాలిమైడ్లు',
        'Polyvinyl chloride / పాలీ వినైల్ క్లోరైడ్',
        'Polycarbonates / పాలికార్బోనేట్లు',
        'A',
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
