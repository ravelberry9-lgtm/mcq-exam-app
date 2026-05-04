import sqlite3, os

SOURCE = 'Science_Set14_Living_Organisms'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    (
        'Lichens are formed due to the symbiotic association of:\nతెలుగు: లైకెన్\u200cలు దేని సహజీవన సంబంధం వల్ల ఏర్పడతాయి',
        'moss and fungi / నాచు మరియు శిలీంధ్రాలు',
        'bacteria and fungi / బ్యాక్టీరియా మరియు శిలీంధ్రాలు',
        'algae and fungi / శైవలాలు మరియు శిలీంధ్రాలు (algae and fungi)',
        'None of these / ఇవేవీ కావు',
        'C',
        'M',
        '',
        1
    ),
    (
        'A reptile with a four-chambered heart is:\nతెలుగు: నాలుగు గదుల గుండె కలిగిన సరీసృపం ఏది',
        'Crocodile / మొసలి (Crocodile)',
        'Turtle / తాబేలు',
        'Snake / పాము',
        'Lizard / బల్లి',
        'A',
        'M',
        '',
        2
    ),
    (
        'Insects form the largest class of animals living on land and sea. They are grouped into:\nతెలుగు: కీటకాలను ఎన్ని క్రమాలుగా విభజించారు',
        '22 orders / 22 క్రమాలు',
        '26 orders / 26 క్రమాలు (26 orders)',
        '29 orders / 29 క్రమాలు',
        '32 orders / 32 క్రమాలు',
        'B',
        'M',
        '',
        3
    ),
    (
        'Which of the following statements is true for planktons\nతెలుగు: ప్లవకాలకు సంబంధించి కింది వాక్యాలలో ఏది సరైనది',
        'They live on the surface of lake water / అవి సరస్సు నీటి ఉపరితలంపై నివసిస్తాయి',
        'They live on the bottom of lakes / అవి సరస్సుల అడుగుభాగంలో నివసిస్తాయి',
        'They live on the plants growing in water / అవి నీటిలో పెరిగే మొక్కలపై నివసిస్తాయి',
        'They live in the water column / అవి నీటి నిలువు వరుసలో నివసిస్తాయి',
        'C',
        'M',
        '',
        4
    ),
    (
        'Which of the following is the largest living mammal\nతెలుగు: కింది వాటిలో జీవించి ఉన్న అతిపెద్ద క్షీరదం ఏది',
        'Giraffe / జిరాఫీ',
        'White elephant / తెల్ల ఏనుగు',
        'Rhinoceros / ఖడ్గమృగం',
        'Blue whale / నీలి తిమింగలం (Blue whale)',
        'D',
        'M',
        '',
        5
    ),
    (
        'Silkworms are fed on:\nతెలుగు: పట్టుపురుగులకు వేటిని ఆహారంగా ఇస్తారు',
        'Insects / కీటకాలు',
        'Mulberry leaves / మల్బరీ ఆకులు (Mulberry leaves)',
        'Grass / గడ్డి',
        'None of these / ఇవేవీ కావు',
        'B',
        'M',
        '',
        6
    ),
    (
        'Yeast is used in making bread because it produces:\nతెలుగు: బ్రెడ్ తయారీలో ఈస్ట్\u200cను ఎందుకు ఉపయోగిస్తారు',
        'CO2 / CO2 (కార్బన్ డైయాక్సైడ్)',
        'O2 / O2',
        'Sugar / చక్కెర',
        'Bacteria / బ్యాక్టీరియా',
        'A',
        'M',
        '',
        7
    ),
    (
        'Which of the following has the smallest egg\nతెలుగు: కింది వాటిలో అతి చిన్న గుడ్డును కలిగి ఉండేది ఏది',
        'Ostrich / ఆస్ట్రిచ్',
        'Hummingbird / హమ్మింగ్\u200cబర్డ్',
        'Pigeon / పావురం',
        'Homo sapiens / హోమో సేపియన్స్ (మానవుడు)',
        'D',
        'M',
        '',
        8
    ),
    (
        'The study of algae is called\nతెలుగు: శైవలాల అధ్యయనాన్ని ఏమంటారు',
        'Phycology / ఫైకాలజీ (Phycology)',
        'Melittology / మెలిట్టాలజీ',
        'Anthropology / ఆంత్రోపాలజీ',
        'Acarology / అకారోలజీ',
        'A',
        'M',
        '',
        9
    ),
    (
        'Which animal produces the biggest baby\nతెలుగు: అతిపెద్ద పిల్లకు జన్మనిచ్చే జంతువు ఏది',
        'Whale / తిమింగలం',
        'Lion / సింహం',
        'Otter / ఓటర్',
        'Blue whale / నీలి తిమింగలం (Blue whale)',
        'D',
        'M',
        '',
        10
    ),
    (
        'Poison glands of snakes are homologous to:\nతెలుగు: పాముల విష గ్రంథులు వేటికి సజాతీయంగా ఉంటాయి',
        'stings of rays / రే చేపల కుట్టే భాగాలు',
        'salivary glands of vertebrates / సకశేరుకాల లాలాజల గ్రంథులు (salivary glands of vertebrates)',
        'electric organs of fishes / చేపల విద్యుత్ అవయవాలు',
        'sebaceous glands of mammals / క్షీరదాల సేబాషియస్ గ్రంథులు',
        'B',
        'M',
        '',
        11
    ),
    (
        'The phylum chordata is characterized by the presence of:\nతెలుగు: కార్డేటా వర్గం దేని ఉనికిని బట్టి వర్గీకరించబడింది',
        'spinal cord / వెన్నుపాము',
        'notochord / పృష్ఠవంశం (notochord)',
        'nerve chord / నరాల తీగ',
        'None of these / ఇవేవీ కావు',
        'B',
        'M',
        '',
        12
    ),
    (
        'Which of the following activities is suppressed by the presence of auxins in plants\nతెలుగు: మొక్కలలో ఆక్సిన్\u200cల ఉనికి వల్ల కింది ఏ చర్య అణచివేయబడుతుంది',
        'Growth of lateral buds / పార్శ్వ మొగ్గల పెరుగుదల',
        'Cell division / కణ విభజన',
        'Root initiation / మూలాల ప్రారంభం',
        'Development of fleshy fruits / కండగల పండ్ల అభివృద్ధి',
        'D',
        'M',
        '',
        13
    ),
    (
        'The only snake that builds a nest is:\nతెలుగు: గూడు కట్టుకునే ఏకైక పాము ఏది',
        'Krait / కట్లపాము',
        'King cobra / కింగ్ కోబ్రా (King cobra)',
        'Chain viper / చైన్ వైపర్',
        'Saw-scaled viper / సా-స్కేల్డ్ వైపర్',
        'B',
        'M',
        '',
        14
    ),
    (
        'Hemoglobin is dissolved in the plasma of:\nతెలుగు: కింది వాటిలో దేని ప్లాస్మాలో హిమోగ్లోబిన్ కరిగి ఉంటుంది',
        'man / మానవుడు',
        'fish / చేప',
        'frog / కప్ప',
        'earthworm / వానపాము (earthworm)',
        'D',
        'M',
        '',
        15
    ),
    (
        'Which among the following are known for cooperation and division of labor\nతెలుగు: కింది వాటిలో సహకారం మరియు శ్రమ విభజనకు ప్రసిద్ధి చెందినవి ఏవి',
        'Fireflies / మిణుగురు పురుగులు',
        'Cockroaches / బొద్దింకలు',
        'Ants / చీమలు (Ants)',
        'Bed bugs / నల్లులు',
        'C',
        'M',
        '',
        16
    ),
    (
        'An ant can see the objects all around it due to the presence of:\nతెలుగు: చీమ తన చుట్టూ ఉన్న వస్తువులను దేని ఉనికి వల్ల చూడగలదు',
        'simple eyes / సరళ నేత్రాలు',
        'eyes over the head / తల పైన ఉన్న కళ్ళు',
        'well-developed eyes / బాగా అభివృద్ధి చెందిన కళ్ళు',
        'compound eyes / సంయుక్త నేత్రాలు (compound eyes)',
        'D',
        'M',
        '',
        17
    ),
    (
        'Which of the following is a flightless bird\nతెలుగు: కింది వాటిలో ఎగరలేని పక్షి ఏది',
        'Emu / ఈము (Emu)',
        'Hen / కోడి',
        'Swan / హంస',
        'None of these / ఇవేవీ కావు',
        'A',
        'M',
        '',
        18
    ),
    (
        'The fact which supports the idea that viruses are living is that they:\nతెలుగు: వైరస్\u200cలు సజీవమైనవి అనే భావనకు మద్దతు ఇచ్చే వాస్తవం ఏమిటి',
        'can be crystallized / వాటిని స్ఫటికాలుగా మార్చవచ్చు',
        'are made up of common chemicals / అవి సాధారణ రసాయనాలతో తయారవుతాయి',
        'duplicate themselves / అవి తమను తాము ప్రతికృతి చేసుకుంటాయి (duplicate themselves)',
        'penetrate cell membranes / అవి కణ త్వచాలను చొచ్చుకునిపోతాయి',
        'C',
        'M',
        '',
        19
    ),
    (
        'Which one of the following structures present in mammalian skin directly helps in keeping warm\nతెలుగు: క్షీరదాల చర్మంలో ఉండే కింది ఏ నిర్మాణం శరీరాన్ని వెచ్చగా ఉంచడంలో ప్రత్యక్షంగా సహాయపడుతుంది',
        'Pigmented cells / వర్ణద్రవ్య కణాలు',
        'Sweat glands / స్వేద గ్రంథులు (Sweat glands)',
        'Lymph vessels / శోషరస నాళాలు',
        'Blood capillaries / రక్త కేశనాళికలు',
        'B',
        'M',
        '',
        20
    ),
    (
        'The sound-producing organ in birds is:\nతెలుగు: పక్షులలో శబ్దాన్ని ఉత్పత్తి చేసే అవయవం ఏది',
        'trachea / వాయునాళం',
        'bronchus / బ్రోంకస్',
        'larynx / స్వరపేటిక',
        'syrinx / సిరింక్స్ (syrinx)',
        'D',
        'M',
        '',
        21
    ),
    (
        'Summer sleep of animals is termed as:\nతెలుగు: జంతువుల వేసవి నిద్రను ఏమని పిలుస్తారు',
        'hibernation / హైబర్నేషన్',
        'incubation / ఇంక్యుబేషన్',
        'aestivation / ఈస్టివేషన్ (aestivation)',
        'gestation / గర్భధారణ',
        'C',
        'M',
        '',
        22
    ),
    (
        'Which of the following is a cold-blooded animal\nతెలుగు: కింది వాటిలో శీతల రక్త జంతువు ఏది',
        'Whale / తిమింగలం',
        'Penguin / పెంగ్విన్',
        'Otter / ఓటర్',
        'Tortoise / తాబేలు (Tortoise)',
        'D',
        'M',
        '',
        23
    ),
    (
        'Which of the following is the group with closely related animal types\nతెలుగు: కింది వాటిలో ఒకే వర్గానికి దగ్గరి సంబంధం ఉన్న జంతు రకాల సమూహం ఏది',
        'Sea-star, Sea-lily, Sea-hare / సీ-స్టార్, సీ-లిల్లీ, సీ-హేర్',
        'Dog-fish, Silver-fish, Cray-fish / డాగ్-ఫిష్, సిల్వర్-ఫిష్, క్రే-ఫిష్',
        'Leech, Louse, Snail / జలగ, పేను, నత్త',
        'Jellyfish, Sea-fan, Sea-anemone / జెల్లీఫిష్, సీ-ఫ్యాన్, సీ-అనిమోన్',
        'D',
        'M',
        '',
        24
    ),
    (
        'The bats are able to fly in the dark since their wings produce:\nతెలుగు: గబ్బిలాలు చీకటిలో ఎగరగలవు ఎందుకంటే వాటి రెక్కలు దేనిని ఉత్పత్తి చేస్తాయి',
        'sound waves / ధ్వని తరంగాలు',
        'ultrasonic waves / అతిధ్వని తరంగాలు (ultrasonic waves)',
        'infrared rays / పరారుణ కిరణాలు',
        'ultraviolet rays / అతినీలలోహిత కిరణాలు',
        'B',
        'M',
        '',
        25
    ),
    (
        'Which of the following is true\nతెలుగు: కింది వాటిలో సరైనది ఏది',
        'All bacteria respire / అన్ని బ్యాక్టీరియాలు శ్వాసిస్తాయి',
        'All bacteria are anaerobic / అన్ని బ్యాక్టీరియాలు అవాయు జీవులు',
        'All bacteria are photosynthetic / అన్ని బ్యాక్టీరియాలు కిరణజన్య సంయోగక్రియ జరుపుతాయి',
        'All bacteria are non-photosynthetic / అన్ని బ్యాక్టీరియాలు కిరణజన్య సంయోగక్రియ జరపవు',
        'A',
        'M',
        '',
        26
    ),
    (
        'The earthworm increases the fertility of soil because it:\nతెలుగు: వానపాము నేల సారాన్ని పెంచుతుంది ఎందుకంటే:',
        'adds nitrogen to it / ఇది నేలకు నైట్రోజన్\u200cను జోడిస్తుంది',
        'survives by eating harmful bacteria of soil / నేలలోని హానికరమైన బ్యాక్టీరియాను తినడం ద్వారా జీవిస్తుంది',
        'turns over large masses of soil / ఇది పెద్ద మొత్తంలో నేలను తలక్రిందులు చేస్తుంది (turns over large masses of soil)',
        'its secretion makes fertilizers easily dissolvable / దాని స్రావం ఎరువులను సులభంగా కరిగేలా చేస్తుంది',
        'C',
        'M',
        '',
        27
    ),
    (
        'Silk is produced by:\nతెలుగు: పట్టు దేని ద్వారా ఉత్పత్తి చేయబడుతుంది',
        'egg of silkworm / పట్టుపురుగు గుడ్డు',
        'pupa of silkworm / పట్టుపురుగు ప్యూపా',
        'larva of silkworm / పట్టుపురుగు లార్వా (larva of silkworm)',
        'insect itself / కీటకం దానంతటదే',
        'C',
        'M',
        '',
        28
    ),
    (
        'About 80% of the body weight in most organisms is:\nతెలుగు: చాలా జీవులలో దాదాపు 80% శరీర బరువు దేనితో ఉంటుంది',
        'protein / ప్రోటీన్',
        'minerals / ఖనిజాలు',
        'water / నీరు (water)',
        'fat / కొవ్వు',
        'C',
        'M',
        '',
        29
    ),
    (
        'In a bee-hive, there is a division of labor. Workers which collect honey from flowers are:\nతెలుగు: తేనెతుట్టెలో శ్రమ విభజన ఉంటుంది. పూల నుండి తేనెను సేకరించే శ్రామిక ఈగలు ఏవి',
        'males / మగ ఈగలు',
        'females / ఆడ ఈగలు (females)',
        'sterile / వంధ్య ఈగలు',
        'intersexes / ఇంటర్\u200cసెక్స్ ఈగలు',
        'B',
        'M',
        '',
        30
    ),
    (
        'One of the characters that distinguishes a frog from a toad is:\nతెలుగు: కప్పను గోదురుకప్ప నుండి వేరు చేసే లక్షణాలలో ఒకటి ఏది',
        'External ear / బాహ్య చెవి',
        'Tail / తోక',
        'Warty skin / పులిపిర్లు ఉన్న చర్మం (Warty skin)',
        'Tongue / నాలుక',
        'C',
        'M',
        '',
        31
    ),
    (
        'The artificial rearing of honey bees is called:\nతెలుగు: తేనెటీగలను కృత్రిమంగా పెంచడాన్ని ఏమంటారు',
        'sylviculture / సిల్వికల్చర్',
        'sericulture / సెరికల్చర్',
        'apiculture / ఎపికల్చర్ (apiculture)',
        'lociculture / లాసికల్చర్',
        'C',
        'M',
        '',
        32
    ),
    (
        'In crustaceans (i.e. crabs, shrimps and sea fish, etc.), the metallic base of the respiratory pigment is made up of:\nతెలుగు: క్రస్టేషియన్లలో శ్వాసకోశ వర్ణద్రవ్యం యొక్క లోహ ఆధారం దేనితో తయారవుతుంది',
        'iron / ఇనుము',
        'copper / రాగి (copper)',
        'magnesium / మెగ్నీషియం',
        'potassium / పొటాషియం',
        'B',
        'M',
        '',
        33
    ),
    (
        'Penicillin is produced from:\nతెలుగు: పెన్సిలిన్ దేని నుండి ఉత్పత్తి చేయబడుతుంది',
        'yeast / ఈస్ట్',
        'algae / శైవలాలు',
        'mould / బూజు (mould)',
        'mushroom / పుట్టగొడుగు',
        'C',
        'M',
        '',
        34
    ),
    (
        'Which of the following is the correct sequel in which the given animal groups appeared on the earth during the course of evolution\nతెలుగు: పరిణామ క్రమంలో జంతు సమూహాలు కనిపించిన సరైన క్రమం ఏది',
        'Porifera → Annelida → Coelenterata → Protozoa / పోరిఫెరా → అనెలిడా → సీలెంటిరేటా → ప్రోటోజోవా',
        'Protozoa → Coelenterata → Porifera → Annelida / ప్రోటోజోవా → సీలెంటిరేటా → పోరిఫెరా → అనెలిడా',
        'Annelida → Porifera → Protozoa → Coelenterata / అనెలిడా → పోరిఫెరా → ప్రోటోజోవా → సీలెంటిరేటా',
        'Protozoa → Porifera → Coelenterata → Annelida / ప్రోటోజోవా → పోరిఫెరా → సీలెంటిరేటా → అనెలిడా',
        'D',
        'M',
        '',
        35
    ),
    (
        'Insects that make a clicking sound are:\nతెలుగు: క్లికింగ్ శబ్దం చేసే కీటకాలు ఏవి',
        'flies / ఈగలు',
        'crickets / కీచురాళ్లు (crickets)',
        'beetles / బీటిల్స్',
        'cockroaches / బొద్దింకలు',
        'B',
        'M',
        '',
        36
    ),
    (
        'Which of the following animals has the longest lifespan\nతెలుగు: కింది జంతువులలో అత్యధిక జీవితకాలం ఉన్నది ఏది',
        'Elephant / ఏనుగు',
        'Crocodile / మొసలి',
        'Dog / కుక్క',
        'Tortoise / తాబేలు (Tortoise)',
        'D',
        'M',
        '',
        37
    ),
    (
        'The functional kidney in adult amphibians is:\nతెలుగు: ప్రౌఢ ఉభయచరాలలో పనిచేసే మూత్రపిండం ఏది',
        'Pronephros / ప్రోనెఫ్రోస్',
        'Metanephros / మెటానెఫ్రోస్',
        'Mesonephros / మీసోనెఫ్రోస్ (Mesonephros)',
        'Opisthonephros / ఓపిస్తోనెఫ్రోస్',
        'C',
        'M',
        '',
        38
    ),
    (
        'Bee dances are meant for:\nతెలుగు: తేనెటీగల నృత్యాలు దేని కోసం ఉద్దేశించబడ్డాయి',
        'communication / కమ్యూనికేషన్ (సమాచార మార్పిడి / communication)',
        'recreation / వినోదం',
        'courtship / కోర్ట్\u200cషిప్',
        'None of these / ఇవేవీ కావు',
        'A',
        'M',
        '',
        39
    ),
    (
        'Which of the following belongs to the family fishes\nతెలుగు: కింది వాటిలో చేపల కుటుంబానికి చెందినది ఏది',
        'Silverfish / సిల్వర్ ఫిష్',
        'Starfish / స్టార్ ఫిష్',
        'Cuttlefish / కటిల్ ఫిష్',
        'Shark / సొరచేప (Shark)',
        'D',
        'M',
        '',
        40
    ),
    (
        'Change of the color of the skin is observed in:\nతెలుగు: చర్మం రంగు మార్చుకోవడం దేనిలో గమనించవచ్చు',
        'prawn / రొయ్య',
        'starfish / స్టార్ ఫిష్',
        'chameleon / ఊసరవెల్లి (chameleon)',
        'shark / సొరచేప',
        'C',
        'M',
        '',
        41
    ),
    (
        'Pearls are formed inside:\nతెలుగు: ముత్యాలు దేని లోపల ఏర్పడతాయి',
        'squids / స్క్విడ్స్',
        'oysters / ఆయిస్టర్స్',
        'snails / నత్తలు',
        'molluscs / మొలస్క్\u200cలు (molluscs)',
        'D',
        'M',
        '',
        42
    ),
    (
        'Two punctures will appear on the part bitten by a:\nతెలుగు: కింది వాటిలో ఏది కరిచిన ప్రదేశంలో రెండు గాట్లు కనిపిస్తాయి',
        'bee / తేనెటీగ',
        'wasp / కందిరీగ',
        'scorpion / తేలు',
        'poisonous snake / విషపు పాము (poisonous snake)',
        'D',
        'M',
        '',
        43
    ),
    (
        'Camel uses its hump for:\nతెలుగు: ఒంటె తన మూపురాన్ని దేనికి ఉపయోగిస్తుంది',
        'storing fat / కొవ్వును నిల్వ చేయడానికి (storing fat)',
        'temperature regulation / ఉష్ణోగ్రత నియంత్రణకు',
        'storing water / నీటిని నిల్వ చేయడానికి',
        'balancing the body during walking in desert sand / ఎడారి ఇసుకలో నడిచేటప్పుడు శరీరాన్ని సమతుల్యం చేయడానికి',
        'A',
        'M',
        '',
        44
    ),
    (
        'The organism in which RNA is the genetic material is:\nతెలుగు: RNA ను జన్యు పదార్ధంగా కలిగిన జీవి ఏది',
        'Rabies virus / రాబిస్ వైరస్',
        'Staphylococcus / స్టెఫిలోకాకస్',
        'Plasmodium / ప్లాస్మోడియం',
        'Tobacco mosaic virus / టొబాకో మొజాయిక్ వైరస్ (Tobacco mosaic virus)',
        'D',
        'M',
        '',
        45
    ),
    (
        'Vitamin C deficient diet produces no deficiency symptoms in:\nతెలుగు: విటమిన్ C లోపించిన ఆహారం దేనిలో లోప లక్షణాలను కలిగించదు',
        'monkey / కోతి',
        'dog / కుక్క (dog)',
        'man / మనిషి',
        'guinea pig / గినియా పంది',
        'B',
        'M',
        '',
        46
    ),
    (
        'The function of the tongue in snakes is to:\nతెలుగు: పాములలో నాలుక యొక్క ప్రధాన విధి ఏమిటి',
        'taste the food / ఆహారాన్ని రుచి చూడటం',
        'smell the food / ఆహారాన్ని వాసన చూడటం (smell the food)',
        'catch the food / ఆహారాన్ని పట్టుకోవడం',
        'detect the food / ఆహారాన్ని గుర్తించడం',
        'B',
        'M',
        '',
        47
    ),
    (
        'In herbivorous mammals, cellulose is digested in:\nతెలుగు: శాకాహార క్షీరదాలలో సెల్యులోజ్ ఎక్కడ జీర్ణమవుతుంది',
        'ileum / ఇలియం',
        'colon / కోలన్',
        'cecum / అంధనాళం (cecum)',
        'rectum / పురీషనాళం',
        'C',
        'M',
        '',
        48
    ),
    (
        'Which of the following is a non-poisonous snake\nతెలుగు: కింది వాటిలో విషరహిత పాము ఏది',
        'Krait / కట్లపాము',
        'Python / కొండచిలువ (Python)',
        'Naja / నాజా',
        'Viper / వైపర్',
        'B',
        'M',
        '',
        49
    ),
    (
        'Which of the following animals stores water in the intestine\nతెలుగు: కింది వాటిలో ప్రేగులలో నీటిని నిల్వ చేసే జంతువు ఏది',
        'Zebra / జీబ్రా',
        'Camel / ఒంటె (Camel)',
        'Moloch / మోలోక్',
        'Uromastix / యూరోమాస్టిక్స్',
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
