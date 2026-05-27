import sqlite3, os

SOURCE = 'Science_Set7_Measurements_Units'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    (
        'Light year is a unit of measurement of\nతెలుగు: కాంతి సంవత్సరం (Light year) దేనిని కొలిచే ప్రమాణం',
        'Speed of light / కాంతి వేగం',
        'Stellar distances / నక్షత్రాల మధ్య దూరం (Stellar distances)',
        'Speed of rockets / రాకెట్ల వేగం',
        'Speed of airplanes / విమానాల వేగం',
        'B',
        'M',
        '',
        2
    ),
    (
        'One micron is equal to\nతెలుగు: ఒక మైక్రాన్ (micron) దేనికి సమానం',
        '1/10 of mm / మి.మీ లో 1/10 వంతు',
        '1/100 of mm / మి.మీ లో 1/100 వంతు',
        '1/1000 of mm / మి.మీ లో 1/1000 వంతు',
        '1/10000 of mm / మి.మీ లో 1/10000 వంతు',
        'C',
        'M',
        '',
        3
    ),
    (
        'Coulomb\nతెలుగు: కింది వాటిని జతపరచండి: భౌతిక రాశి A. విద్యుత్ బలం (Electric force) B. విద్యుత్ ఆవేశం (Electric charge) C. విద్యుత్ పొటెన్షియల్ (Electric potential) D. విద్యుత్ సామర్థ్యం (Electric capacity) ప్రమాణం',
        '4, 2, 3, 1',
        '3, 1, 2, 4',
        '2, 4, 1, 3',
        '1, 3, 4, 2',
        'C',
        'M',
        '',
        4
    ),
    (
        'Hydrometer is an instrument\nతెలుగు: హైడ్రోమీటర్ (Hydrometer) అనేది:',
        'For measuring sound underwater / నీటి అడుగున ధ్వనిని కొలవడానికి',
        'To detect the presence of hydrogen in the atmosphere / వాతావరణంలో హైడ్రోజన్ ఉనికిని గుర్తించడానికి',
        'For measuring the specific gravity of liquids / ద్రవాల విశిష్ట గురుత్వాకర్షణను (specific gravity) కొలవడానికి',
        'To detect changes in atmospheric humidity / వాతావరణ తేమలో మార్పులను గుర్తించడానికి',
        'C',
        'M',
        '',
        4
    ),
    (
        'Pascal-sec\nతెలుగు: కింది వాటిని జతపరచండి: భౌతిక రాశి A. ఘన కోణం (Solid angle) B. ప్రచోదనం (Impulse) C. స్నిగ్ధత (Viscosity) D. పీడనం (Pressure) ప్రమాణం',
        '1, 3, 4, 2',
        '1, 4, 3, 2',
        '2, 4, 3, 1',
        '2, 3, 4, 1',
        'D',
        'M',
        '',
        4
    ),
    (
        'Which thermometer is used to indicate the lowest temperature\nతెలుగు: అత్యల్ప ఉష్ణోగ్రతను సూచించడానికి ఏ థర్మామీటర్\u200cను ఉపయోగిస్తారు',
        'Clinical thermometer / క్లినికల్ థర్మామీటర్',
        'Gas thermometer / గ్యాస్ థర్మామీటర్',
        'Alcohol thermometer / ఆల్కహాల్ థర్మామీటర్',
        'Resistance thermometer / రెసిస్టెన్స్ థర్మామీటర్',
        'C',
        'M',
        '',
        5
    ),
    (
        'One horsepower is equal to\nతెలుగు: ఒక హార్స్ పవర్ (అశ్వ సామర్థ్యం) దేనికి సమానం',
        '736 watts / 736 వాట్స్',
        '746 watts / 746 వాట్స్',
        '748 watts / 748 వాట్స్',
        '756 watts / 756 వాట్స్',
        'B',
        'M',
        '',
        6
    ),
    (
        "'Bar' is the unit of\nతెలుగు: 'బార్' (Bar) అనేది దేని ప్రమాణం",
        'Heat / ఉష్ణం',
        'Temperature / ఉష్ణోగ్రత',
        'Current / విద్యుత్ ప్రవాహం',
        'Atmospheric pressure / వాతావరణ పీడనం (Atmospheric pressure)',
        'D',
        'M',
        '',
        7
    ),
    (
        'A chronometer measures\nతెలుగు: క్రోనోమీటర్ (chronometer) దేనిని కొలుస్తుంది',
        'Sound waves / ధ్వని తరంగాలు',
        'Time / సమయం (Time)',
        'Water waves / నీటి తరంగాలు',
        'Color contrast / రంగుల వ్యత్యాసం',
        'B',
        'M',
        '',
        8
    ),
    (
        'One fathom is equal to\nతెలుగు: ఒక ఫాథమ్ (fathom) దేనికి సమానం',
        '6 meters / 6 మీటర్లు',
        '6 feet / 6 అడుగులు (6 feet)',
        '60 feet / 60 అడుగులు',
        '100 cm / 100 సెం.మీ',
        'B',
        'M',
        '',
        9
    ),
    (
        'What is the number of basic units in the International System of Units\nతెలుగు: అంతర్జాతీయ ప్రమాణాల వ్యవస్థ (SI) లో ప్రాథమిక ప్రమాణాలు ఎన్ని',
        '4 / 4',
        '5 / 5',
        '6 / 6',
        '7 / 7',
        'D',
        'M',
        '',
        10
    ),
    (
        'What is the unit for measuring the pitch or frequency of sound\nతెలుగు: ధ్వని యొక్క పిచ్ లేదా పౌనఃపున్యాన్ని (లేదా తీవ్రతను) కొలవడానికి ఉపయోగించే ప్రమాణం ఏది',
        'Coulomb / కూలుంబ్',
        'Hum / హమ్',
        'Cycles / సైకిల్స్',
        'Decibel / డెసిబెల్ (Decibel)',
        'D',
        'M',
        '',
        11
    ),
    (
        "Knot is a unit of speed of which of the following\nతెలుగు: 'నాట్' (Knot) అనేది దేని వేగాన్ని కొలిచే ప్రమాణం",
        'Light waves / కాంతి తరంగాలు',
        'Ship / ఓడ (Ship)',
        'Sound waves / ధ్వని తరంగాలు',
        'Airplane / విమానం',
        'B',
        'M',
        '',
        12
    ),
    (
        'Electric current is measured by\nతెలుగు: విద్యుత్ ప్రవాహాన్ని (Electric current) దేనితో కొలుస్తారు',
        'Anemometer / అనిమోమీటర్',
        'Voltmeter / వోల్టమీటర్',
        'Ammeter / అమ్మీటర్ (Ammeter)',
        'Commutator / కమ్యుటేటర్',
        'C',
        'M',
        '',
        13
    ),
    (
        'The dynamo is a device for converting\nతెలుగు: డైనమో (dynamo) అనేది దేనిని మార్చే పరికరం',
        'Heat energy into electrical energy / ఉష్ణ శక్తిని విద్యుత్ శక్తిగా',
        'Mechanical energy into electrical energy / యాంత్రిక శక్తిని విద్యుత్ శక్తిగా (Mechanical energy into electrical energy)',
        'Magnetic energy into electrical energy / అయస్కాంత శక్తిని విద్యుత్ శక్తిగా',
        'Chemical energy into electrical energy / రసాయన శక్తిని విద్యుత్ శక్తిగా',
        'B',
        'M',
        '',
        14
    ),
    (
        'The Fathom is the unit of\nతెలుగు: ఫాథమ్ (Fathom) అనేది దేని ప్రమాణం',
        'Sound / ధ్వని',
        'Depth / లోతు (Depth)',
        'Distance / దూరం',
        'Frequency / పౌనఃపున్యం',
        'B',
        'M',
        '',
        15
    ),
    (
        'Which of the following instruments is used for precise measurement of refractive indices\nతెలుగు: వక్రీభవన గుణకాలను కచ్చితంగా కొలవడానికి కింది ఏ పరికరాన్ని ఉపయోగిస్తారు',
        'Photometer / ఫోటోమీటర్',
        'Spectrometer / స్పెక్ట్రోమీటర్ (Spectrometer)',
        'Micrometer / మైక్రోమీటర్',
        'Spherometer / స్ఫెరోమీటర్',
        'B',
        'M',
        '',
        17
    ),
    (
        'Kilohertz is a unit which measures\nతెలుగు: కిలోహెర్ట్జ్ (Kilohertz) దేనిని కొలిచే ప్రమాణం',
        'Electric resistance / విద్యుత్ నిరోధం',
        'Power used by a current of one ampere / ఒక ఆంపియర్ విద్యుత్ ప్రవాహం ఉపయోగించే సామర్థ్యం',
        'Electromagnetic radio wave frequencies / విద్యుదయస్కాంత రేడియో తరంగ పౌనఃపున్యాలు (Electromagnetic radio wave frequencies)',
        'None of these / ఇవేవీ కావు',
        'C',
        'M',
        '',
        18
    ),
    (
        'If you swim one km, how many miles do you swim\nతెలుగు: మీరు ఒక కిలోమీటరు ఈదినట్లయితే, మీరు ఎన్ని మైళ్లు ఈదినట్లు',
        '0.5 / 0.5',
        '0.62 / 0.62',
        '0.84 / 0.84',
        '1.6 / 1.6',
        'B',
        'M',
        '',
        19
    ),
    (
        'Nautical mile is a unit of distance used in\nతెలుగు: నాటికల్ మైల్ (Nautical mile) అనేది ఎందులో ఉపయోగించే దూర ప్రమాణం',
        'Astronomy / ఖగోళ శాస్త్రం',
        'Navigation / నావిగేషన్ (సముద్రయానం/Navigation)',
        'Road mile / రోడ్ మైల్',
        'Measuring the boundaries of a nation / దేశ సరిహద్దులను కొలవడం',
        'B',
        'M',
        '',
        20
    ),
    (
        'Match the following: A. Resistance - 1. Ampere B. Current - 2. Newton C. Force - 3. Watt D. Power - 4. Ohm\nతెలుగు: కింది వాటిని జతపరచండి: A. నిరోధం - 1. ఆంపియర్ B. విద్యుత్ ప్రవాహం - 2. న్యూటన్ C. బలం - 3. వాట్ D. సామర్థ్యం (పవర్) - 4. ఓమ్',
        '2, 1, 3, 4 / A-2, B-1, C-3, D-4',
        '4, 1, 2, 3 / A-4, B-1, C-2, D-3',
        '4, 3, 1, 2 / A-4, B-3, C-1, D-2',
        '4, 3, 2, 1 / A-4, B-3, C-2, D-1',
        'B',
        'M',
        '',
        21
    ),
    (
        'Reading of the barometer going down is an indication of\nతెలుగు: బేరోమీటర్ రీడింగ్ పడిపోవడం అనేది దేనికి సంకేతం',
        'Storm / తుఫాను',
        'Snow / మంచు',
        'Rainfall / వర్షపాతం (Rainfall)',
        'Intense heat / తీవ్రమైన వేడి',
        'C',
        'M',
        '',
        22
    ),
    (
        'Kilowatt is a unit to measure\nతెలుగు: కిలోవాట్ (Kilowatt) అనేది దేనిని కొలవడానికి ఉపయోగిస్తారు',
        'Work / పని',
        'Electricity / విద్యుత్',
        'Power / సామర్థ్యం (పవర్/Power)',
        'Current / విద్యుత్ ప్రవాహం',
        'C',
        'M',
        '',
        23
    ),
    (
        'Very small time intervals are accurately measured by the\nతెలుగు: అతి చిన్న సమయ వ్యవధులను దేని ద్వారా కచ్చితంగా కొలుస్తారు',
        'Pulsars / పల్సార్\u200cలు',
        'Quartz clocks / క్వార్ట్జ్ గడియారాలు',
        'Atomic clocks / అణు గడియారాలు (Atomic clocks)',
        'White dwarfs / వైట్ డ్వార్ఫ్\u200cలు',
        'C',
        'M',
        '',
        24
    ),
    (
        'The unit for measurement of magnetic induction is\nతెలుగు: అయస్కాంత ప్రేరణను (magnetic induction) కొలవడానికి ప్రమాణం ఏది',
        'Joule / జౌల్',
        'Gress / గ్రెస్',
        'Gauss / గాస్ (Gauss)',
        'Weber / వెబర్',
        'C',
        'M',
        '',
        25
    ),
    (
        'The SI unit of electrical resistance of conductor is\nతెలుగు: వాహకం యొక్క విద్యుత్ నిరోధానికి (నిరోధకతకు) SI ప్రమాణం ఏది',
        'Faraday / ఫారడే',
        'Volts / వోల్ట్స్',
        'Ampere / ఆంపియర్',
        'Ohm-metre / ఓమ్-మీటర్ (Ohm-metre)',
        'D',
        'M',
        '',
        26
    ),
    (
        'Decibel is the unit used for\nతెలుగు: డెసిబెల్ (Decibel) అనేది దేనికి ఉపయోగించే ప్రమాణం',
        'Speed of light / కాంతి వేగం',
        'Intensity of heat / ఉష్ణ తీవ్రత',
        'Intensity of sound / ధ్వని తీవ్రత (Intensity of sound)',
        'Radio wave frequency / రేడియో తరంగ పౌనఃపున్యం',
        'C',
        'M',
        '',
        27
    ),
    (
        'Match the following: A. Anemometer - 1. High temperatures B. Tachometer - 2. Power of machine C. Pyrometer - 3. Rotation speed D. Dynamometer - 4. Velocity of fluid\nతెలుగు: కింది వాటిని జతపరచండి: A. అనిమోమీటర్ - 1. అధిక ఉష్ణోగ్రతలు B. టాకోమీటర్ - 2. యంత్ర సామర్థ్యం C. పైరోమీటర్ - 3. భ్రమణ వేగం D. డైనమోమీటర్ - 4. ప్రవాహ వేగం (గాలి/ద్రవ)',
        '2, 1, 3, 4 / A-2, B-1, C-3, D-4',
        '3, 4, 2, 1 / A-3, B-4, C-2, D-1',
        '4, 3, 1, 2 / A-4, B-3, C-1, D-2',
        '4, 3, 2, 1 / A-4, B-3, C-2, D-1',
        'C',
        'M',
        '',
        28
    ),
    (
        'Tesla is unit for\nతెలుగు: టెస్లా (Tesla) అనేది దేని ప్రమాణం',
        'Electric field / విద్యుత్ క్షేత్రం',
        'Inductance / ఇండక్టెన్స్',
        'Magnetic field / అయస్కాంత క్షేత్రం (Magnetic field)',
        'Electrical resistance / విద్యుత్ నిరోధం',
        'C',
        'M',
        '',
        29
    ),
    (
        '1 Joule is equivalent to\nతెలుగు: 1 జౌల్ (Joule) దేనికి సమానం',
        '10^3 ergs / 10^3 ఎర్గ్స్',
        '10^5 ergs / 10^5 ఎర్గ్స్',
        '10^7 ergs / 10^7 ఎర్గ్స్ (10^7 ergs)',
        '10^11 ergs / 10^11 ఎర్గ్స్',
        'C',
        'M',
        '',
        30
    ),
    (
        'The smallest unit of length is-\nతెలుగు: పొడవును కొలిచే అతి చిన్న ప్రమాణం ఏది',
        'Micron / మైక్రాన్',
        'Nanometre / నానోమీటర్',
        'Angstrom / ఆంగ్\u200cస్ట్రామ్',
        'Fermimetre / ఫెర్మిమీటర్ (Fermimetre)',
        'D',
        'M',
        '',
        31
    ),
    (
        'Which of the following is not a physical quantity\nతెలుగు: కింది వాటిలో భౌతిక రాశి (physical quantity) కానిది ఏది',
        'Length / పొడవు',
        'Time / సమయం',
        'Electric current / విద్యుత్ ప్రవాహం',
        'Kilogram (kg) / కిలోగ్రాము (kg)',
        'D',
        'M',
        '',
        32
    ),
    (
        'What is an international (SI) unit of electric current\nతెలుగు: విద్యుత్ ప్రవాహానికి అంతర్జాతీయ (SI) ప్రమాణం ఏమిటి',
        'Ohm / ఓమ్',
        'Volt / వోల్ట్',
        'Ohm-meter / ఓమ్-మీటర్',
        'Ampere / ఆంపియర్ (Ampere)',
        'D',
        'M',
        '',
        33
    ),
    (
        'Which of the following is the SI unit of luminous intensity\nతెలుగు: కింది వాటిలో కాంతి తీవ్రతకు (luminous intensity) SI ప్రమాణం ఏది',
        'Lambert / లాంబెర్ట్',
        'Joule / జౌల్',
        'Candela / కాండెలా (Candela)',
        'Ampere / ఆంపియర్',
        'C',
        'M',
        '',
        34
    ),
    (
        'Which method is used to measure the distance of other planets from the earth\nతెలుగు: భూమి నుండి ఇతర గ్రహాల దూరాన్ని కొలవడానికి ఏ పద్ధతిని ఉపయోగిస్తారు',
        'Parallax Method / పారలాక్స్ పద్ధతి (Parallax Method)',
        'Meter Scale / మీటర్ స్కేల్',
        'Both a and b methods / a మరియు b పద్ధతులు రెండూ',
        'None of the above / పైవేవీ కావు',
        'A',
        'M',
        '',
        35
    ),
    (
        "'Dobson' unit is used for the measurement of\nతెలుగు: 'డాబ్సన్' (Dobson) ప్రమాణాన్ని దేనిని కొలవడానికి ఉపయోగిస్తారు",
        'Thickness of Earth / భూమి మందం',
        'Thickness of Diamond / వజ్రం మందం',
        'Thickness of Ozone layer / ఓజోన్ పొర మందం (Thickness of Ozone layer)',
        'Measurement of Noise / శబ్ద కొలత',
        'C',
        'M',
        '',
        36
    ),
    (
        'Name the instrument used to measure relative humidity\nతెలుగు: సాపేక్ష ఆర్ద్రతను (relative humidity) కొలవడానికి ఉపయోగించే పరికరం పేరు ఏమిటి',
        'Hydrometer / హైడ్రోమీటర్',
        'Hygrometer / హైగ్రోమీటర్ (Hygrometer)',
        'Barometer / బేరోమీటర్',
        'Mercury Thermometer / పాదరస థర్మామీటర్',
        'B',
        'M',
        '',
        37
    ),
    (
        'PARSEC is the unit of\nతెలుగు: పార్సెక్ (PARSEC) అనేది దేని ప్రమాణం',
        'Length / పొడవు / దూరం (Length)',
        'Time / సమయం',
        'Light intensity / కాంతి తీవ్రత',
        'Magnetic force / అయస్కాంత బలం',
        'A',
        'M',
        '',
        38
    ),
    (
        'What is measured in Cusec\nతెలుగు: క్యూసెక్ (Cusec) లలో దేనిని కొలుస్తారు',
        'Purity of water / నీటి స్వచ్ఛత',
        'Depth of water / నీటి లోతు',
        'Flow of water / నీటి ప్రవాహం (Flow of water)',
        'Quantity of water / నీటి పరిమాణం',
        'C',
        'M',
        '',
        39
    ),
    (
        'The telescope is used for viewing-\nతెలుగు: టెలిస్కోప్ (దూరదర్శిని) ను దేనిని చూడటానికి ఉపయోగిస్తారు',
        'Distant objects / సుదూర వస్తువులు (Distant objects)',
        'Near objects / సమీప వస్తువులు',
        'Small objects / చిన్న వస్తువులు',
        'Living cells / సజీవ కణాలు',
        'A',
        'M',
        '',
        40
    ),
    (
        'Joule is the unit of\nతెలుగు: జౌల్ (Joule) అనేది దేని ప్రమాణం',
        'Temperature / ఉష్ణోగ్రత',
        'Pressure / పీడనం',
        'Energy / శక్తి (Energy)',
        'Heat / ఉష్ణం',
        'C',
        'M',
        '',
        41
    ),
    (
        'Velocity of wind is measured by-\nతెలుగు: గాలి వేగాన్ని దేనితో కొలుస్తారు',
        'Speedometer / స్పీడోమీటర్',
        'Tachometer / టాకోమీటర్',
        'Anemometer / అనిమోమీటర్ (Anemometer)',
        'Audiometer / ఆడియోమీటర్',
        'C',
        'M',
        '',
        42
    ),
    (
        'Lux is the SI unit of-\nతెలుగు: లక్స్ (Lux) అనేది దేనికి SI ప్రమాణం',
        'Intensity of illumination / ప్రకాశ తీవ్రత (Intensity of illumination)',
        'Luminous efficiency / కాంతి సామర్థ్యం',
        'Luminous flux / కాంతి అభివాహం',
        'Luminous intensity / కాంతి తీవ్రత',
        'A',
        'M',
        '',
        43
    ),
    (
        'A transformer is used to\nతెలుగు: ట్రాన్స్\u200cఫార్మర్\u200cను దేనికి ఉపయోగిస్తారు',
        'Increase DC voltage / DC వోల్టేజీని పెంచడానికి',
        'Increase or decrease AC voltage / AC వోల్టేజీని పెంచడానికి లేదా తగ్గించడానికి (Increase or decrease AC voltage)',
        'Decrease DC voltage / DC వోల్టేజీని తగ్గించడానికి',
        'Convert DC into AC / DC ని AC గా మార్చడానికి',
        'B',
        'M',
        '',
        44
    ),
    (
        'Which of the following physical quantity is dimensionless\nతెలుగు: కింది భౌతిక రాశులలో దేనికి మితులు (కొలతలు/dimensions) ఉండవు',
        'Angle / కోణం',
        'Specific gravity / విశిష్ట గురుత్వం (Specific gravity)',
        'Strain / వికృతి (Strain)',
        'All of these / ఇవన్నీ (All of these)',
        'D',
        'M',
        '',
        45
    ),
    (
        'The dimensional formula for angular momentum is same as that for:\nతెలుగు: కోణీయ ద్రవ్యవేగం యొక్క మితి ఫార్ములా (dimensional formula) కింది వాటిలో దేనితో సమానంగా ఉంటుంది',
        'Torque / టార్క్',
        "Plank's constant / ప్లాంక్ స్థిరాంకం (Plank's constant)",
        'Gravitational constant / గురుత్వాకర్షణ స్థిరాంకం',
        'Impulse / ప్రచోదనం (Impulse)',
        'B',
        'M',
        '',
        46
    ),
    (
        'The zero error belongs to the category of:\nతెలుగు: జీరో ఎర్రర్ (శూన్య దోషం) అనేది ఏ వర్గానికి చెందుతుంది',
        'Constant error / స్థిర దోషం',
        'Personal error / వ్యక్తిగత దోషం',
        'Accidental error / ఆకస్మిక దోషం',
        'Instrumental error / పరికర దోషం (Instrumental error)',
        'D',
        'M',
        '',
        47
    ),
    (
        'Which one of the following is not the unit of heat\nతెలుగు: కింది వాటిలో ఉష్ణానికి ప్రమాణం కానిది ఏది',
        'Calorie / కేలరీ',
        'Kilocalorie / కిలో కేలరీ',
        'Kilojoule / కిలో జౌల్',
        'Watt / వాట్ (Watt)',
        'D',
        'M',
        '',
        48
    ),
    (
        'Which of the following pairs has the same dimensions\nతెలుగు: కింది జతలలో ఏవి సమానమైన మితులను (dimensions) కలిగి ఉంటాయి',
        'Specific heat and latent heat / విశిష్టోష్ణం మరియు గుప్తోష్ణం',
        'Impulse and momentum / ప్రచోదనం మరియు ద్రవ్యవేగం (Impulse and momentum)',
        'Surface tension and force / తలతన్యత మరియు బలం',
        'Moment of Inertia and torque / జడత్వ భ్రామకం మరియు టార్క్',
        'B',
        'M',
        '',
        49
    ),
    (
        'The dimensions of kinetic energy is same as that of\nతెలుగు: గతి శక్తి యొక్క మితులు (dimensions) దేని మితులతో సమానంగా ఉంటాయి',
        'force / బలం',
        'pressure / పీడనం',
        'work / పని (work)',
        'momentum / ద్రవ్యవేగం',
        'C',
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
