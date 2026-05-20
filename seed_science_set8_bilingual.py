import sqlite3, os

SOURCE = 'Science_Set8_Light_Sound_Wave'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    (
        'Which type of wave is a sound wave in air\nతెలుగు: గాలిలో ధ్వని తరంగం ఏ రకమైన తరంగం',
        'Longitudinal / అనుదైర్ఘ్య తరంగం (Longitudinal)',
        'Transverse / తిర్యక్ తరంగం (Transverse)',
        'Electromagnetic / విద్యుదయస్కాంత తరంగం',
        'Standing / స్థిర తరంగం (Standing)',
        'A',
        'M',
        '',
        1
    ),
    (
        'Which of the following colour of light deviates least through the prism\nతెలుగు: కింది వాటిలో పట్టకం గుండా వెళ్ళినప్పుడు అతి తక్కువగా విచలనం (deviate) చెందే కాంతి రంగు ఏది',
        'Yellow / పసుపు',
        'Green / ఆకుపచ్చ',
        'Violet / వైలెట్ (ఊదా)',
        'Red / ఎరుపు (Red)',
        'D',
        'M',
        '',
        2
    ),
    (
        'Rainbow is formed due to-\nతెలుగు: ఇంద్రధనుస్సు దేని కారణంగా ఏర్పడుతుంది',
        'Refraction and Dispersion / వక్రీభవనం మరియు విక్షేపణం',
        'Scattering and Refraction / పరిక్షేపణం మరియు వక్రీభవనం',
        'Diffraction and Refraction / వివర్తనం మరియు వక్రీభవనం',
        'Reflection and Refraction / పరావర్తనం మరియు వక్రీభవనం (Reflection and Refraction)',
        'D',
        'M',
        '',
        3
    ),
    (
        'The sky appears blue due to\nతెలుగు: ఆకాశం నీలంగా కనిపించడానికి కారణం:',
        'Rayleigh scattering / రేలీ పరిక్షేపణం (Rayleigh scattering)',
        'Mie scattering / మై పరిక్షేపణం',
        'Back scattering / బ్యాక్ స్కాటరింగ్',
        'None of the above / పైవేవీ కావు',
        'A',
        'M',
        '',
        4
    ),
    (
        'The Phenomenon which causes mirage is-\nతెలుగు: ఎండమావులు (mirage) ఏర్పడటానికి కారణమయ్యే దృగ్విషయం ఏది',
        'Interference / వ్యతికరణం (Interference)',
        'Diffraction / వివర్తనం (Diffraction)',
        'Polarization / ధ్రువణం (Polarization)',
        'Total Internal Reflection / సంపూర్ణాంతర పరావర్తనం (Total Internal Reflection)',
        'D',
        'M',
        '',
        5
    ),
    (
        'Optical fibre works on the principle of\nతెలుగు: ఆప్టికల్ ఫైబర్ (దృశ్య తంతువు) ఏ సూత్రంపై పనిచేస్తుంది',
        'Refraction / వక్రీభవనం',
        'Scattering / పరిక్షేపణం',
        'Interference / వ్యతికరణం',
        'Total Internal Reflection / సంపూర్ణాంతర పరావర్తనం (Total Internal Reflection)',
        'D',
        'M',
        '',
        6
    ),
    (
        'The phenomenon of change in direction of light when it passes from one medium to another is called\nతెలుగు: కాంతి ఒక యానకం నుండి మరొక యానకంలోకి ప్రయాణించినప్పుడు దాని దిశ మారే దృగ్విషయాన్ని ఏమంటారు',
        'Propagation / ప్రసారం',
        'Reflection / పరావర్తనం (Reflection)',
        'Refraction / వక్రీభవనం (Refraction)',
        'Dispersion / విక్షేపణం (Dispersion)',
        'C',
        'M',
        '',
        7
    ),
    (
        'A star appears twinkling in the sky because of-\nతెలుగు: ఆకాశంలో నక్షత్రాలు మినుకుమినుకుమంటూ (twinkling) కనిపించడానికి కారణం:',
        'Scattering of light by atmosphere / వాతావరణం ద్వారా కాంతి పరిక్షేపణం',
        'Reflection of light by atmosphere / వాతావరణం ద్వారా కాంతి పరావర్తనం',
        'Refraction of light by atmosphere / వాతావరణం ద్వారా కాంతి వక్రీభవనం (Refraction of light by atmosphere)',
        'Diffraction of light by atmosphere / వాతావరణం ద్వారా కాంతి వివర్తనం',
        'C',
        'M',
        '',
        8
    ),
    (
        'The head mirror used by ENT doctors is\nతెలుగు: ENT వైద్యులు ఉపయోగించే హెడ్ మిర్రర్ (తల అద్దం) ఏది',
        'Concave / పుటాకార (Concave)',
        'Convex / కుంభాకార (Convex)',
        'Plane / సమతల (Plane)',
        'Plano-convex / సమతల-కుంభాకార',
        'A',
        'M',
        '',
        9
    ),
    (
        'Vehicles use ___ to see the objects coming from behind-\nతెలుగు: వాహనాలలో వెనుక నుండి వచ్చే వస్తువులను చూడటానికి దేనిని ఉపయోగిస్తారు',
        'Concave Lens / పుటాకార కటకం',
        'Convex Lens / కుంభాకార కటకం',
        'Concave Mirror / పుటాకార దర్పణం',
        'Convex Mirror / కుంభాకార దర్పణం (Convex Mirror)',
        'D',
        'M',
        '',
        10
    ),
    (
        'Magnifying Glass is basically a-\nతెలుగు: భూతద్దం (Magnifying Glass) అనేది ప్రాథమికంగా ఒక:',
        'Plano-concave lens / సమతల-పుటాకార కటకం',
        'Concave lens / పుటాకార కటకం',
        'Convex lens / కుంభాకార కటకం (Convex lens)',
        'Cylindrical lens / స్తూపాకార కటకం',
        'C',
        'M',
        '',
        11
    ),
    (
        'Shaving Mirror is-\nతెలుగు: షేవింగ్ మిర్రర్ ఏ రకమైన దర్పణం',
        'Convex / కుంభాకార',
        'Concave / పుటాకార (Concave)',
        'Plane / సమతల',
        'Parabolic / పరావలయ (Parabolic)',
        'B',
        'M',
        '',
        12
    ),
    (
        'Which type of mirror is used in the head lights of vehicles-\nతెలుగు: వాహనాల హెడ్\u200cలైట్లలో ఏ రకమైన దర్పణాన్ని ఉపయోగిస్తారు',
        'Plane Mirror / సమతల దర్పణం',
        'Concave Mirror / పుటాకార దర్పణం (Concave Mirror)',
        'Convex Mirror / కుంభాకార దర్పణం',
        'Parabolic Mirror / పరావలయ దర్పణం',
        'B',
        'M',
        '',
        13
    ),
    (
        'A periscope works on the principle of\nతెలుగు: పెరిస్కోప్ ఏ సూత్రం ఆధారంగా పనిచేస్తుంది',
        'Refraction / వక్రీభవనం',
        'Total Internal Reflection / సంపూర్ణాంతర పరావర్తనం',
        'Diffraction / వివర్తనం',
        'Reflection / పరావర్తనం (Reflection)',
        'D',
        'M',
        '',
        14
    ),
    (
        'A sound wave with a period of 0.01 seconds has a frequency of:\nతెలుగు: 0.01 సెకన్ల ఆవర్తన కాలం (period) ఉన్న ధ్వని తరంగం యొక్క పౌనఃపున్యం (frequency) ఎంత',
        '1000 Hz / 1000 Hz',
        '10 Hz / 10 Hz',
        '0.1 Hz / 0.1 Hz',
        '100 Hz / 100 Hz',
        'D',
        'M',
        '',
        15
    ),
    (
        'To get the magnified and virtual image mirror is used-\nతెలుగు: వస్తువు కంటే పెద్దదైన మరియు మిథ్యా ప్రతిబింబాన్ని (magnified and virtual image) పొందడానికి ఏ దర్పణాన్ని ఉపయోగిస్తారు',
        'Plane Mirror / సమతల దర్పణం',
        'Convex Mirror / కుంభాకార దర్పణం',
        'Concave Mirror / పుటాకార దర్పణం (Concave Mirror)',
        'Concave Lens / పుటాకార కటకం',
        'C',
        'M',
        '',
        16
    ),
    (
        'Dioptre is the unit of-\nతెలుగు: డయాప్టర్ (Dioptre) దేని ప్రమాణం',
        'Power of lens / కటక సామర్థ్యం (Power of lens)',
        'Focal length of lens / కటక నాభ్యాంతరం',
        'Intensity of lens / కటక తీవ్రత',
        'Intensity of sound / ధ్వని తీవ్రత',
        'A',
        'M',
        '',
        17
    ),
    (
        'The amount of sound energy passing each second through unit area is called the ___ of sound.\nతెలుగు: ప్రమాణ వైశాల్యం గుండా ప్రతి సెకనుకు ప్రవహించే ధ్వని శక్తి పరిమాణాన్ని ధ్వని యొక్క _____ అంటారు.',
        'Loudness / శబ్ద తీవ్రత/పెద్దదనం (Loudness)',
        'Intensity / తీవ్రత (Intensity)',
        'Audible Range / వినగలిగే పరిధి',
        'Reverberation / ప్రతిధ్వని (Reverberation)',
        'B',
        'M',
        '',
        18
    ),
    (
        'The power of a lens is measured in\nతెలుగు: కటక సామర్థ్యాన్ని దేనిలో కొలుస్తారు',
        'Dioptre / డయాప్టర్ (Dioptre)',
        'Aeon / అయోన్',
        'Lumen / ల్యూమెన్',
        'Candela / కాండెలా',
        'A',
        'M',
        '',
        19
    ),
    (
        'Person who is color blind can not distinguish between-\nతెలుగు: వర్ణాంధత్వం (color blindness) ఉన్న వ్యక్తి ఏ రంగుల మధ్య తేడాను గుర్తించలేడు',
        'Black and yellow / నలుపు మరియు పసుపు',
        'Red and green / ఎరుపు మరియు ఆకుపచ్చ (Red and green)',
        'Yellow and white / పసుపు మరియు తెలుపు',
        'Green and blue / ఆకుపచ్చ మరియు నీలం',
        'B',
        'M',
        '',
        20
    ),
    (
        'The least distance of distinct Vision is\nతెలుగు: స్పష్టమైన దృష్టి కనీస దూరం ఎంత',
        '35 cm / 35 సెం.మీ',
        '25 cm / 25 సెం.మీ',
        '45 cm / 45 సెం.మీ',
        '15 cm / 15 సెం.మీ',
        'B',
        'M',
        '',
        21
    ),
    (
        'Sensitivity of human eye is maximum in the\nతెలుగు: మానవ కంటి సున్నితత్వం ఏ రంగు కాంతి ప్రాంతంలో గరిష్టంగా ఉంటుంది',
        'Violet region / వయొలెట్ ప్రాంతం',
        'Green region / ఆకుపచ్చ ప్రాంతం (Green region)',
        'Blue region / నీలి ప్రాంతం',
        'Red region / ఎరుపు ప్రాంతం',
        'B',
        'M',
        '',
        22
    ),
    (
        'Hypermetropia or long sightedness can be corrected by using\nతెలుగు: హైపర్\u200cమెట్రోపియా (దీర్ఘదృష్టి) ని వేటిని ఉపయోగించి సరిచేయవచ్చు',
        'Bifocal lenses / బైఫోకల్ కటకాలు',
        'Cylindrical lenses / స్తూపాకార కటకాలు',
        'Concave lenses / పుటాకార కటకాలు',
        'Convex lenses / కుంభాకార కటకాలు (Convex lenses)',
        'D',
        'M',
        '',
        23
    ),
    (
        'Short-sight in human eye can be corrected by using proper\nతెలుగు: మానవ కంటిలోని హ్రస్వదృష్టి (Myopia) ని సరైన ఏ కటకాన్ని ఉపయోగించి సరిచేయవచ్చు',
        'Convex lens / కుంభాకార కటకం',
        'Concave lens / పుటాకార కటకం (Concave lens)',
        'Cylindrical lens / స్తూపాకార కటకం',
        'Bifocal lens / బైఫోకల్ కటకం',
        'B',
        'M',
        '',
        24
    ),
    (
        'Which colour is the complementary colour of yellow\nతెలుగు: పసుపు రంగుకు పూరక రంగు (complementary colour) ఏది',
        'Blue / నీలం (Blue)',
        'Green / ఆకుపచ్చ',
        'Orange / ఆరెంజ్',
        'Red / ఎరుపు',
        'A',
        'M',
        '',
        25
    ),
    (
        'Which of the following purpose optical fibre is used for\nతెలుగు: ఆప్టికల్ ఫైబర్ (దృశ్య తంతువు) కింది ఏ ప్రయోజనం కోసం ఉపయోగించబడుతుంది',
        'Weaving / నేత',
        'Musical Instrument / సంగీత వాయిద్యం',
        'Eye Surgery / కంటి శస్త్రచికిత్స',
        'Communication / సమాచార ప్రసారం (Communication)',
        'D',
        'M',
        '',
        26
    ),
    (
        'Light Waves are\nతెలుగు: కాంతి తరంగాలు అనేవి:',
        'Electric Wave / విద్యుత్ తరంగం',
        'Magnetic Wave / అయస్కాంత తరంగం',
        'Electromagnetic Wave / విద్యుదయస్కాంత తరంగం (Electromagnetic Wave)',
        'Electrostatic Wave / స్థిర విద్యుత్ తరంగం',
        'C',
        'M',
        '',
        27
    ),
    (
        'Speed of light is maximum in\nతెలుగు: కాంతి వేగం దేనిలో గరిష్టంగా ఉంటుంది',
        'Vacuum / శూన్యం (Vacuum)',
        'Solids / ఘన పదార్థాలు',
        'Liquids / ద్రవ పదార్థాలు',
        'Gases / వాయువులు',
        'A',
        'M',
        '',
        28
    ),
    (
        'Which colour is formed when Red and Green are mixed\nతెలుగు: ఎరుపు మరియు ఆకుపచ్చ రంగులను కలిపినప్పుడు ఏ రంగు ఏర్పడుతుంది',
        'Light blue / లేత నీలం',
        'Yellow / పసుపు (Yellow)',
        'White / తెలుపు',
        'Grey / బూడిద రంగు',
        'B',
        'M',
        '',
        29
    ),
    (
        'The crest of a wave is the point where the disturbance is at:\nతెలుగు: తరంగం యొక్క శృంగం (crest) వద్ద మాధ్యమంలోని కణాల అలజడి (disturbance) ఎలా ఉంటుంది',
        'Constant point / స్థిరంగా',
        'Zero point / శూన్యం',
        'Maximum point / గరిష్టంగా (Maximum point)',
        'Minimum point / కనిష్టంగా',
        'C',
        'M',
        '',
        30
    ),
    (
        'Sound travels fastest in\nతెలుగు: ధ్వని కింది వాటిలో దేని గుండా అత్యంత వేగంగా ప్రయాణిస్తుంది',
        'Steel / స్టీల్/ఉక్కు (Steel)',
        'Air / గాలి',
        'Water / నీరు',
        'Vacuum / శూన్యం',
        'A',
        'M',
        '',
        31
    ),
    (
        'The waves used in sonography are-\nతెలుగు: సోనోగ్రఫీలో ఉపయోగించే తరంగాలు ఏవి',
        'Micro waves / మైక్రో తరంగాలు',
        'Infra-red waves / పరారుణ తరంగాలు',
        'Sound waves / ధ్వని తరంగాలు',
        'Ultrasonic waves / అతిధ్వని తరంగాలు (Ultrasonic waves)',
        'D',
        'M',
        '',
        32
    ),
    (
        'Echo is produced due to\nతెలుగు: ప్రతిధ్వని (Echo) దేని వల్ల ఏర్పడుతుంది',
        'Reflection of sound / ధ్వని పరావర్తనం (Reflection of sound)',
        'Refraction of sound / ధ్వని వక్రీభవనం',
        'Resonance / అనునాదం (Resonance)',
        'None of these / ఇవేవీ కావు',
        'A',
        'M',
        '',
        33
    ),
    (
        'What is the nature of wavefront from a point source in an isotropic medium\nతెలుగు: ఐసోట్రోపిక్ యానకంలో ఒక బిందు మూలం (point source) నుండి వెలువడే తరంగాగ్రం (wavefront) స్వభావం ఎలా ఉంటుంది',
        'Cylindrical / స్తూపాకార',
        'Spherical / గోళాకార (Spherical)',
        'Elliptical / దీర్ఘ వృత్తాకార',
        'Plane / సమతల',
        'B',
        'M',
        '',
        34
    ),
    (
        'Conversion of sound energy into electrical energy is done by-\nతెలుగు: ధ్వని శక్తిని విద్యుత్ శక్తిగా మార్చే పరికరం ఏది',
        'Solar cell / సోలార్ సెల్',
        'Gramophone / గ్రామఫోన్',
        'Microphone / మైక్రోఫోన్ (Microphone)',
        'Loud speaker / లౌడ్ స్పీకర్',
        'C',
        'M',
        '',
        35
    ),
    (
        'Women have shrill voice because of\nతెలుగు: స్త్రీల గొంతు కీచుగా (shrill) ఉండటానికి కారణం:',
        'Low frequency / తక్కువ పౌనఃపున్యం',
        'High frequency / అధిక పౌనఃపున్యం (High frequency)',
        'Shrill vocals / కీచు స్వరాలు',
        'Strong epiglottis / బలమైన ఎపిగ్లోటిస్',
        'B',
        'M',
        '',
        36
    ),
    (
        'Which of the following has the lowest frequency\nతెలుగు: కింది వాటిలో అత్యల్ప పౌనఃపున్యం కలిగినవి ఏవి',
        'Visible Ray / దృశ్య కాంతి కిరణం (Visible Ray)',
        'Gamma Ray / గామా కిరణం',
        'X-Ray / ఎక్స్-కిరణం',
        'Ultraviolet Rays / అతినీలలోహిత కిరణాలు',
        'A',
        'M',
        '',
        37
    ),
    (
        'Which of the following is not true about X-rays\nతెలుగు: ఎక్స్-కిరణాలకు (X-rays) సంబంధించి కింది వాటిలో ఏది నిజం కాదు',
        'Have low penetrating power / చొచ్చుకుపోయే శక్తి తక్కువగా ఉంటుంది (Have low penetrating power)',
        'Travel with the speed of light / కాంతి వేగంతో ప్రయాణిస్తాయి',
        'Can be reflected or refracted / పరావర్తనం లేదా వక్రీభవనం చెందగలవు',
        'Can affect photographic plates. / ఫోటోగ్రాఫిక్ ప్లేట్లను ప్రభావితం చేయగలవు',
        'A',
        'M',
        '',
        38
    ),
    (
        'Gamma rays can cause\nతెలుగు: గామా కిరణాలు కింది వాటిలో దేనికి కారణమవుతాయి',
        'Gene mutation / జన్యు ఉత్పరివర్తనలు (Gene mutation)',
        'Sneezing / తుమ్ములు',
        'Burning / కాలడం',
        'Fever / జ్వరం',
        'A',
        'M',
        '',
        39
    ),
    (
        'Ultraviolet rays can be used in water treatment as\nతెలుగు: నీటి శుద్ధి ప్రక్రియలో అతినీలలోహిత కిరణాలను (UV rays) దేనిగా ఉపయోగించవచ్చు',
        'Precipitator / అవక్షేపకారిణి',
        'Hydrolyser / జలవిశ్లేషకారిణి',
        'Disinfectant / క్రిమిసంహారిణి (Disinfectant)',
        'Flocculator / ఫ్లోక్యులేటర్',
        'C',
        'M',
        '',
        40
    ),
    (
        'Radar is used to-\nతెలుగు: రాడార్ (Radar) దేనికి ఉపయోగించబడుతుంది',
        'To locate submerged submarines. / మునిగిపోయిన జలాంతర్గాములను కనుగొనడానికి',
        'Receive signal from radio receivers. / రేడియో రిసీవర్ల నుండి సిగ్నల్స్ స్వీకరించడానికి',
        'Detect and locate distant objects. / సుదూర వస్తువులను గుర్తించడానికి మరియు కనుగొనడానికి (Detect and locate distant objects)',
        'Locate geostationary satellites. / జియోస్టేషనరీ ఉపగ్రహాలను కనుగొనడానికి',
        'C',
        'M',
        '',
        41
    ),
    (
        'Which of the following waves has the highest frequency\nతెలుగు: కింది వాటిలో అత్యధిక పౌనఃపున్యం కలిగిన తరంగాలు ఏవి',
        'Radio / రేడియో',
        'Infrared / పరారుణ',
        'Microwaves / మైక్రోవేవ్స్',
        'Gamma-rays / గామా-కిరణాలు (Gamma-rays)',
        'D',
        'M',
        '',
        42
    ),
    (
        'Which of the following causes more burn\nతెలుగు: కింది వాటిలో ఏది తీవ్రమైన గాయానికి (మంటకు) కారణమవుతుంది',
        'Boiling water / మరుగుతున్న నీరు',
        'Hot water / వేడి నీరు',
        'Steam / నీటి ఆవిరి (Steam)',
        'None of these / ఇవేవీ కావు',
        'C',
        'M',
        '',
        43
    ),
    (
        'Which of the following metal has the maximum thermal conductivity\nతెలుగు: కింది వాటిలో గరిష్ట ఉష్ణ వాహకత (thermal conductivity) కలిగిన లోహం ఏది',
        'Iron / ఇనుము',
        'Aluminium / అల్యూమినియం',
        'Copper / రాగి',
        'Silver / వెండి (Silver)',
        'D',
        'M',
        '',
        44
    ),
    (
        'Energy travels from sun to earth by which of the following method\nతెలుగు: సూర్యుని నుండి భూమికి శక్తి ఏ పద్ధతి ద్వారా ప్రయాణిస్తుంది',
        'Conduction / ఉష్ణ వాహనం (Conduction)',
        'Insolation / ఇన్సోలేషన్',
        'Radiation / ఉష్ణ వికిరణం (Radiation)',
        'Modulation / మాడ్యులేషన్',
        'C',
        'M',
        '',
        45
    ),
    (
        'The hottest part of gas flame is known as\nతెలుగు: గ్యాస్ మంటలో అత్యంత వేడిగా ఉండే భాగాన్ని ఏమంటారు',
        'Non luminous zone / నాన్ ల్యూమినస్ జోన్ / కాంతివిహీన ప్రాంతం (Non luminous zone)',
        'Blue zone / బ్లూ జోన్',
        'Luminous zone / ల్యూమినస్ జోన్ / కాంతివంతమైన ప్రాంతం',
        'Dark zone / డార్క్ జోన్',
        'A',
        'M',
        '',
        46
    ),
    (
        'Which one of the following is an insulator\nతెలుగు: కింది వాటిలో అవాహకం (insulator) ఏది',
        'Copper / రాగి',
        'Wood / చెక్క (Wood)',
        'Mercury / పాదరసం',
        'Aluminium / అల్యూమినియం',
        'B',
        'M',
        '',
        47
    ),
    (
        'Which of the following are methods of heat transfer\nతెలుగు: కింది వాటిలో ఉష్ణ బదిలీ (heat transfer) పద్ధతులు ఏవి',
        'Convection / ఉష్ణ సంవహనం (Convection)',
        'Evaporation / భాష్పీభవనం',
        'Revolution / భ్రమణం',
        'Thermal Expansion / ఉష్ణ వ్యాకోచం',
        'A',
        'M',
        '',
        48
    ),
    (
        'The freezing point of fresh water is:\nతెలుగు: స్వచ్ఛమైన నీటి ఘనీభవన స్థానం (freezing point) ఎంత',
        '3°C / 3°C',
        '5°C / 5°C',
        '0°C / 0°C',
        '4°C / 4°C',
        'C',
        'M',
        '',
        49
    ),
    (
        'What determines the colour of a star\nతెలుగు: నక్షత్రం యొక్క రంగును ఏది నిర్ణయిస్తుంది',
        'Temperature / ఉష్ణోగ్రత (Temperature)',
        'Distance / దూరం',
        'Radius / వ్యాసార్ధం',
        'Atmospheric Pressure / వాతావరణ పీడనం',
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
