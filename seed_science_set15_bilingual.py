import sqlite3, os

SOURCE = 'Science_Set15_LivingOrganisms_GK'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    (
        'Who described the algae Spirogyra in 1674 and named the motile organisms Animalcules meaning little animals\nతెలుగు: 1674లో స్పైరోగైరా అనే శైవలాన్ని వర్ణించి, మరియు కదిలే సూక్ష్మజీవులకు యానిమల్\u200cక్యూల్స్ అని పేరు పెట్టింది ఎవరు',
        'Maurice Wilkins / మారిస్ విల్కిన్స్',
        'Anton Van Leeuwenhoek / ఆంటోనీ వాన్ లీవెన్\u200cహుక్ (Anton Van Leeuwenhoek)',
        'Robert Remak / రాబర్ట్ రెమాక్',
        'Barthelemy Dumortier / బార్తెలెమీ డ్యుమోర్టియర్',
        'B',
        'M',
        '',
        1
    ),
    (
        'The largest living bird is\nతెలుగు: జీవించి ఉన్న అతిపెద్ద పక్షి ఏది',
        'Duck / బాతు',
        'Dodo / డోడో',
        'Ostrich / ఆస్ట్రిచ్ (Ostrich)',
        'Peacock / నెమలి',
        'C',
        'M',
        '',
        2
    ),
    (
        'Birds get thrust and lift from\nతెలుగు: పక్షులు థ్రస్ట్ మరియు లిఫ్ట్ దేని ద్వారా పొందుతాయి',
        'Air sacs / వాయు గోణులు',
        'Flapping of wings / రెక్కలు ఊపడం ద్వారా (Flapping of wings)',
        'Twisting of feathers / ఈకలను మెలితిప్పడం ద్వారా',
        'Shape of wings similar to airplane blades / విమానం బ్లేడ్\u200cల మాదిరిగా రెక్కల ఆకారం ద్వారా',
        'B',
        'M',
        '',
        3
    ),
    (
        'Which bacteria have a thick cell wall with several layers of peptidoglycan and teichoic acid\nతెలుగు: పెప్టిడోగ్లైకాన్ మరియు టెయికోయిక్ ఆమ్లం యొక్క మందపాటి కణ కవచాన్ని ఏ బ్యాక్టీరియా కలిగి ఉంటుంది',
        'Salmonella enterica / సాల్మొనెల్లా',
        'Staphylococcus aureus / స్టెఫిలోకాకస్ ఆరియస్ (Staphylococcus aureus)',
        'Pseudomonas aeruginosa / సూడోమోనాస్',
        'Escherichia coli / ఎస్చెరిచియా కోలి',
        'B',
        'M',
        '',
        4
    ),
    (
        'Hormones are normally absent in\nతెలుగు: హార్మోన్లు సాధారణంగా కింది వాటిలో వేటిలో ఉండవు',
        'Rat / ఎలుక',
        'Monkey / కోతి',
        'Bacteria / బ్యాక్టీరియా (Bacteria)',
        'Cat / పిల్లి',
        'C',
        'M',
        '',
        5
    ),
    (
        'The blood-sucking organisms are\nతెలుగు: రక్తాన్ని పీల్చే జీవులు ఏవి',
        'Hookworms / హుక్\u200cవార్మ్స్',
        'Earthworms / వానపాములు',
        'Leeches / జలగలు (Leeches)',
        'Pinworms / పిన్\u200cవార్మ్స్',
        'C',
        'M',
        '',
        6
    ),
    (
        'From which stage of silkmoth is silk obtained\nతెలుగు: పట్టుపురుగు ఏ దశలో ఉన్నప్పుడు పట్టు పొందబడుతుంది',
        'Caterpillar / గొంగళిపురుగు',
        'Pupa / ప్యూపా',
        'Cocoon / కోకూన్ (Cocoon)',
        'Adult / ప్రౌఢ దశ',
        'C',
        'M',
        '',
        7
    ),
    (
        'The gestation period of cows is\nతెలుగు: ఆవుల గర్భధారణ కాలం ఎంత',
        '150 days / 150 రోజులు',
        '280 days / 280 రోజులు (280 days)',
        '300 days / 300 రోజులు',
        '365 days / 365 రోజులు',
        'B',
        'M',
        '',
        8
    ),
    (
        'Taenia solium (Tapeworm) lives as a parasite in\nతెలుగు: టీనియా సోలియం (బద్దెపురుగు) దేనిలో పరాన్నజీవిగా నివసిస్తుంది',
        'Pig / పంది',
        'Abdomen of man / మనిషి ఉదరం',
        'Intestine of man / మనిషి ప్రేగు (Intestine of man)',
        'Liver of man / మనిషి కాలేయం',
        'C',
        'M',
        '',
        9
    ),
    (
        'Which of the following is an egg-laying mammal\nతెలుగు: కింది వాటిలో గుడ్లు పెట్టే క్షీరదం ఏది',
        'Bat / గబ్బిలం',
        'Scaly ant-eater / పొలుసుల చీమలభక్షి',
        'Whale / తిమింగలం',
        'Spiny ant-eater / ముళ్ల చీమలభక్షి (ఎకిడ్నా / Spiny ant-eater)',
        'D',
        'M',
        '',
        10
    ),
    (
        'The human immunodeficiency virus (HIV) is a living entity because it can\nతెలుగు: HIV ని సజీవ అస్తిత్వంగా ఎందుకు పరిగణిస్తారు',
        'Move from one cell to another / ఇది కణాల మధ్య కదలగలదు',
        'Undergo auto-reproduction / ఇది స్వీయ-పునరుత్పత్తి చెందగలదు (auto-reproduction)',
        'Disturb host cell respiration / అతిధేయి కణ శ్వాసక్రియకు ఆటంకం కలిగిస్తుంది',
        'Excrete in human sperm / మానవ శుక్రకణాలలో విసర్జిస్తుంది',
        'B',
        'M',
        '',
        11
    ),
    (
        'Feeding of colostrum is important for young calves because\nతెలుగు: లేగదూడలకు ముర్రుపాలు పట్టించడం ఎందుకు ముఖ్యం',
        'It is tasty / అవి రుచిగా ఉంటాయి',
        'It contains iron / వాటిలో ఇనుము ఉంటుంది',
        'It contains antibodies / వాటిలో ప్రతిరక్షకాలు ఉంటాయి (antibodies)',
        'It supplies growth proteins / పెరుగుదలకు ప్రోటీన్లను సరఫరా చేస్తాయి',
        'C',
        'M',
        '',
        12
    ),
    (
        'Which of the following animals is called a living fossil\nతెలుగు: కింది జంతువులలో దేనిని సజీవ శిలాజం అని పిలుస్తారు',
        'Polystomella / పాలిస్టోమెల్లా',
        'Peripatus / పెరిపాటస్ (Peripatus)',
        'Sea cucumber / సీ కుకుంబర్',
        'Sacculina / సాక్యులీనా',
        'B',
        'M',
        '',
        13
    ),
    (
        'If the cerebellum of a pigeon were destroyed, the bird would not be able to\nతెలుగు: పావురం యొక్క అనుమస్తిష్కం దెబ్బతిన్నట్లయితే, ఆ పక్షి దేనిని చేయలేకపోతుంది',
        'Fly / ఎగరడం (Fly)',
        'Breathe / శ్వాస పీల్చుకోవడం',
        'Digest food / ఆహారాన్ని జీర్ణం చేసుకోవడం',
        'Oxidize food / ఆహారాన్ని ఆక్సీకరణం చేయడం',
        'A',
        'M',
        '',
        14
    ),
    (
        'Mule is the hybrid of\nతెలుగు: కంచరగాడిద దేని సంకరజాతి',
        'male horse and mare / మగ గుర్రం మరియు ఆడ గుర్రం',
        'female horse and male donkey / ఆడ గుర్రం మరియు మగ గాడిద (female horse and male donkey)',
        'male horse and female zebra / మగ గుర్రం మరియు ఆడ జీబ్రా',
        'female horse and male zebra / ఆడ గుర్రం మరియు మగ జీబ్రా',
        'B',
        'M',
        '',
        15
    ),
    (
        'The characteristic feature of virus is that\nతెలుగు: వైరస్ యొక్క ముఖ్యమైన లక్షణం ఏమిటి',
        'it lacks chlorophyll / దానికి క్లోరోఫిల్ ఉండదు',
        'it multiplies only on dead animals / ఇది చనిపోయిన జంతువులపై మాత్రమే వృద్ధి చెందుతుంది',
        'it is made of fats / ఇది కొవ్వులతో తయారవుతుంది',
        'it multiplies only on hosts / ఇది అతిధేయిల పై మాత్రమే వృద్ధి చెందుతుంది',
        'D',
        'M',
        '',
        16
    ),
    (
        'Which of the following has no blood but respires\nతెలుగు: కింది వాటిలో రక్తం లేకపోయినా శ్వాసించే జీవి ఏది',
        'Fish / చేప',
        'Earthworm / వానపాము',
        'Hydra / హైడ్రా (Hydra)',
        'Cockroach / బొద్దింక',
        'C',
        'M',
        '',
        17
    ),
    (
        'The organism living at the bottom of the water mass is called\nతెలుగు: సముద్రం లేదా సరస్సు అడుగు భాగంలో నివసించే జీవులను ఏమంటారు',
        'Nekton / నెక్టన్',
        'Neuston / న్యూస్టన్',
        'Benthos / బెంథోస్ (Benthos)',
        'Plankton / ప్లవకాలు',
        'C',
        'M',
        '',
        18
    ),
    (
        'Which of the following pairs is not correctly matched\nతెలుగు: కింది జతలలో సరిగ్గా జతపరచబడనిది ఏది',
        'Annelida – Leech / అనెలిడా - జలగ',
        'Mammalia – Bat / క్షీరదం - గబ్బిలం',
        'Insecta – Prawn / ఇన్\u200cసెక్టా - రొయ్య',
        'Amphibia – Toad / ఉభయచరం - గోదురుకప్ప',
        'C',
        'M',
        '',
        19
    ),
    (
        'Which of the following have the highest upper limit of audible range\nతెలుగు: కింది వాటిలో వినగలిగే పౌనఃపున్య పరిధి గరిష్టంగా ఉండే జీవి ఏది',
        'Human beings / మానవులు',
        'Dogs / కుక్కలు',
        'Whales / తిమింగలాలు',
        'Bats / గబ్బిలాలు (Bats)',
        'D',
        'M',
        '',
        20
    ),
    (
        'Which of the following birds has webbed feet\nతెలుగు: కింది వాటిలో వేళ్ల మధ్య చర్మం ఉన్న పక్షి ఏది',
        'Hen / కోడి',
        'Duck / బాతు (Duck)',
        'Peacock / నెమలి',
        'Pigeon / పావురం',
        'B',
        'M',
        '',
        21
    ),
    (
        'The unicellular algae which is used in space programs to regulate the supply of oxygen is\nతెలుగు: ఆక్సిజన్ సరఫరాను నియంత్రించడానికి అంతరిక్ష కార్యక్రమాలలో ఉపయోగించే ఏకకణ శైవలం ఏది',
        'Chlamydomonas / క్లామిడోమోనాస్',
        'Codium / కోడియమ్',
        'Chlorella / క్లోరెల్లా (Chlorella)',
        'Spirogyra / స్పైరోగైరా',
        'C',
        'M',
        '',
        22
    ),
    (
        'Which of the following enzymes secreted by the pancreas helps predatory mammals to digest the blood they drink from their prey\nతెలుగు: ప్యాంక్రియాస్ ద్వారా స్రవించే ఏ ఎంజైమ్ ప్రెడేటరీ క్షీరదాలు రక్తాన్ని జీర్ణం చేసుకోవడానికి సహాయపడుతుంది',
        'Pepsin / పెప్సిన్',
        'Fibrin / ఫైబ్రిన్',
        'Trypsin / ట్రిప్సిన్ (Trypsin)',
        'Ptyalin / టయలిన్',
        'C',
        'M',
        '',
        23
    ),
    (
        'Mycorrhiza is a symbiotic association between\nతెలుగు: మైకోరైజా అనేది వేటి మధ్య సహజీవన సంబంధం',
        'Algae and roots of orchids / ఆర్కిడ్స్ వేర్లు మరియు శైవలాలు',
        'Protozoa and roots of higher plants / మొక్కల వేర్లు మరియు ప్రోటోజోవా',
        'Bacteria and roots of higher plants / మొక్కల వేర్లు మరియు బ్యాక్టీరియా',
        'Fungi and roots of higher plants / ఉన్నత జాతి మొక్కల వేర్లు మరియు శిలీంధ్రాలు (Fungi)',
        'D',
        'M',
        '',
        24
    ),
    (
        'Which of the following is a short-tailed rodent used in scientific experiments\nతెలుగు: శాస్త్రీయ ప్రయోగాలలో ఉపయోగించే చిన్న తోక గల రోడెంట్ ఏది',
        'Rat / ఎలుక',
        'Rabbit / కుందేలు',
        'Guinea pig / గినియా పంది (Guinea pig)',
        'Squirrel / ఉడుత',
        'C',
        'M',
        '',
        25
    ),
    (
        'The insect not useful to man is\nతెలుగు: మనిషికి ఉపయోగపడని కీటకం ఏది',
        'Lac insect / లాక్ కీటకం',
        'Rice weevil / రైస్ వీవిల్ (Rice weevil)',
        'Silkworm / పట్టుపురుగు',
        'Honey bee / తేనెటీగ',
        'B',
        'M',
        '',
        26
    ),
    (
        'Which of the following is not a rabid animal\nతెలుగు: కింది వాటిలో రేబిస్ వ్యాధిని కలిగించని జంతువు ఏది',
        'Dog / కుక్క',
        'Cat / పిల్లి',
        'Deer / జింక (Deer)',
        'Fox / నక్క',
        'C',
        'M',
        '',
        27
    ),
    (
        'Snake bite first affects the\nతెలుగు: పాము కాటు ముందుగా దేనిని ప్రభావితం చేస్తుంది',
        'Nervous system / నాడీ వ్యవస్థ',
        'Lungs / ఊపిరితిత్తులు',
        'Blood circulation / రక్త ప్రసరణ వ్యవస్థ (Blood circulation)',
        'Brain / మెదడు',
        'C',
        'M',
        '',
        28
    ),
    (
        'Which of the following is not a breed of dog\nతెలుగు: కింది వాటిలో కుక్క జాతికి చెందనిది ఏది',
        'Rottweiler / రోట్\u200cవీలర్',
        'Plymouth rock / ప్లైమౌత్ రాక్ (Plymouth rock)',
        'Bull Mastiff / బుల్ మాస్టిఫ్',
        'Springer Spaniel / స్ప్రింగర్ స్పానియల్',
        'B',
        'M',
        '',
        29
    ),
    (
        'What is a sponge\nతెలుగు: స్పంజ్ అంటే ఏమిటి',
        'A plant / ఒక మొక్క',
        'An animal / ఒక జంతువు (An animal)',
        'A fungus / ఒక శిలీంధ్రం',
        'A fossil / ఒక శిలాజం',
        'B',
        'M',
        '',
        30
    ),
    (
        'Which of the following is a hermaphroditic organism\nతెలుగు: కింది వాటిలో ఉభయలింగ జీవి ఏది',
        'Mosquito / దోమ',
        'Hookworm / హుక్\u200cవార్మ్',
        'Bed bug / నల్లి',
        'Earthworm / వానపాము (Earthworm)',
        'D',
        'M',
        '',
        31
    ),
    (
        'The greatest value of bees to mankind is in\nతెలుగు: మానవాళికి తేనెటీగల వల్ల కలిగే అతిపెద్ద ప్రయోజనం ఏమిటి',
        "Storing honey for man's use / తేనెను నిల్వ చేయడం",
        'Supplying food for birds / పక్షులకు ఆహారాన్ని సరఫరా చేయడం',
        'Ensuring pollination of certain crop plants / పంట మొక్కలలో పరాగసంపర్కం (Pollination)',
        'Furnishing beeswax needed in certain industries / మైనపును సరఫరా చేయడం',
        'C',
        'M',
        '',
        32
    ),
    (
        'Difference between GMT and IST is\nతెలుగు: GMT మరియు IST మధ్య వ్యత్యాసం ఎంత',
        '2 hours 30 minutes / 2 గంటల 30 నిమిషాలు',
        '5 hours 30 minutes / 5 గంటల 30 నిమిషాలు (5h 30m)',
        '6 hours 30 minutes / 6 గంటల 30 నిమిషాలు',
        '4 hours 30 minutes / 4 గంటల 30 నిమిషాలు',
        'B',
        'M',
        '',
        33
    ),
    (
        'Which British ruler introduced the Police Administration in India\nతెలుగు: భారతదేశంలో పోలీసు యంత్రాంగాన్ని ప్రవేశపెట్టిన బ్రిటిష్ పాలకుడు ఎవరు',
        'Lord Cornwallis / లార్డ్ కార్న్\u200cవాలిస్ (Lord Cornwallis)',
        'Lord Wellesley / లార్డ్ వెల్లెస్లీ',
        'Lord Dalhousie / లార్డ్ డల్హౌసీ',
        'Lord Bentinck / లార్డ్ బెంటింక్',
        'A',
        'M',
        '',
        34
    ),
    (
        'In which year was Brahmo Samaj established\nతెలుగు: ఏ సంవత్సరంలో బ్రహ్మ సమాజం స్థాపించబడింది',
        '1830 AD / 1830',
        '1828 AD / 1828 (1828 AD)',
        '1800 AD / 1800',
        '1784 AD / 1784',
        'B',
        'M',
        '',
        35
    ),
    (
        'Solar energy is due to\nతెలుగు: సౌర శక్తి దేని వల్ల జనిస్తుంది',
        'Chemical reaction / రసాయన చర్య',
        'Combustion reaction / దహన చర్య',
        'Nuclear fission reaction / కేంద్రక విచ్ఛిత్తి',
        'Nuclear fusion reaction / కేంద్రక సంలీన చర్య (Nuclear fusion reaction)',
        'D',
        'M',
        '',
        36
    ),
    (
        'In which of the following diseases the immune system breaks down\nతెలుగు: కింది ఏ వ్యాధిలో శరీర రోగనిరోధక వ్యవస్థ విచ్ఛిన్నమవుతుంది',
        'Diabetes / మధుమేహం',
        'AIDS / ఎయిడ్స్ (AIDS)',
        'Black fever / కాలా అజార్',
        'Diarrhoea / అతిసారం',
        'B',
        'M',
        '',
        37
    ),
    (
        'Which one of the following elements is considered as a micronutrient in plants\nతెలుగు: కింది మూలకాలలో మొక్కలలో సూక్ష్మ పోషకంగా పరిగణించబడేది ఏది',
        'P Phosphorus / P (స్థూల పోషకం)',
        'Mg Magnesium / Mg (స్థూల పోషకం)',
        'Ca Calcium / Ca (స్థూల పోషకం)',
        'Zn Zinc / Zn (Zinc - సూక్ష్మ పోషకం)',
        'D',
        'M',
        '',
        38
    ),
    (
        "Nil Darpan The drama was composed by\nతెలుగు: 'నీల్ దర్పణ్' అనే నాటకాన్ని రచించింది ఎవరు",
        'Michael Madhusudan Dutt / మైఖేల్ మధుసూదన్ దత్',
        'Dinabandhu Mitra / దీనబంధు మిత్ర (Dinabandhu Mitra)',
        'Bankim Chandra Chattopadhyay / బంకిమ్ చంద్ర',
        'Subhas Chandra Bose / సుభాష్ చంద్రబోస్',
        'B',
        'M',
        '',
        39
    ),
    (
        'Audible sound has the frequency range of\nతెలుగు: వినగలిగే శబ్ద పౌనఃపున్య పరిధి ఎంత',
        '20 Hz to 20000 Hz / 20 Hz నుండి 20000 Hz',
        '2 Hz to 20000 Hz / 2 Hz నుండి 20000 Hz',
        '20 Hz to 2000 Hz / 20 Hz నుండి 2000 Hz',
        '200 Hz to 20000 Hz / 200 Hz నుండి 20000 Hz',
        'A',
        'M',
        '',
        40
    ),
    (
        'Doldrums means\nతెలుగు: డోల్\u200cడ్రమ్స్ అనగా ఏమిటి',
        'A region of calm climate / ప్రశాంత వాతావరణ ప్రాంతం (calm climate)',
        'A region of stormy climate / తుఫానులతో కూడిన ప్రాంతం',
        'A region of cold climate / శీతల వాతావరణ ప్రాంతం',
        'A region of dry climate / పొడి వాతావరణ ప్రాంతం',
        'A',
        'M',
        '',
        41
    ),
    (
        'The rock composed of Quartz, Feldspar, Mica and Hornblend is\nతెలుగు: క్వార్ట్జ్, ఫెల్డ్\u200cస్పార్, మైకా మరియు హార్న్\u200cబ్లెండ్\u200cలతో కూడిన శిల ఏది',
        'Quartzite / క్వార్ట్\u200cజైట్',
        'Granite / గ్రానైట్ (Granite)',
        'Basalt / బసాల్ట్',
        'Limestone / సున్నపురాయి',
        'B',
        'M',
        '',
        42
    ),
    (
        'Tasmania is separated from Australia by\nతెలుగు: టాస్మానియా, ఆస్ట్రేలియా నుండి దేని ద్వారా వేరు చేయబడింది',
        'Cook Strait / కుక్ జలసంధి',
        'Bass Strait / బాస్ జలసంధి (Bass Strait)',
        'Bering Strait / బేరింగ్ జలసంధి',
        'Luzon Strait / లుజోన్ జలసంధి',
        'B',
        'M',
        '',
        43
    ),
    (
        'The gas present in the highest proportion in air is\nతెలుగు: గాలిలో అత్యధిక నిష్పత్తిలో ఉండే వాయువు ఏది',
        'Oxygen / ఆక్సిజన్ (21%)',
        'Nitrogen / నైట్రోజన్ (78% / Nitrogen)',
        'Hydrogen / హైడ్రోజన్',
        'Carbon dioxide / కార్బన్ డైయాక్సైడ్',
        'B',
        'M',
        '',
        44
    ),
    (
        'The human cell contains\nతెలుగు: మానవ కణంలో ఎన్ని క్రోమోజోమ్\u200cలు ఉంటాయి',
        '44 chromosomes / 44',
        '48 chromosomes / 48',
        '46 chromosomes / 46 (46 chromosomes - 23 జతలు)',
        '23 chromosomes / 23',
        'C',
        'M',
        '',
        45
    ),
    (
        'Jhum is\nతెలుగు: ఝుమ్ అనగా ఏమిటి',
        'A folk dance / ఒక జానపద నృత్యం',
        'The name of a river / ఒక నది పేరు',
        'A tribe / ఒక తెగ',
        'A type of cultivation / ఒక రకమైన సాగు (పోడు వ్యవసాయం)',
        'D',
        'M',
        '',
        46
    ),
    (
        'Ramsar site is connected with\nతెలుగు: రామ్\u200cసర్ సైట్ దేనికి సంబంధించినది',
        'Wetland / చిత్తడి నేలలు (Wetland)',
        'Grassland / గడ్డిభూములు',
        'Forestland / అటవీభూమి',
        'Valley / లోయ',
        'A',
        'M',
        '',
        47
    ),
    (
        'The state of Telangana was formed in the year\nతెలుగు: తెలంగాణ రాష్ట్రం ఏ సంవత్సరంలో ఏర్పడింది',
        '2011 / 2011',
        '2012 / 2012',
        '2013 / 2013',
        '2014 / 2014 (జూన్ 2)',
        'D',
        'M',
        '',
        48
    ),
    (
        'Who among the following scientists was associated with the theory of Relativity\nతెలుగు: సాపేక్షత సిద్ధాంతంతో సంబంధం ఉన్న శాస్త్రవేత్త ఎవరు',
        'Niels Bohr / నీల్స్ బోర్',
        'Heisenberg / హైసెన్\u200cబర్గ్',
        'Einstein / ఐన్\u200cస్టీన్ (Einstein)',
        'Madam Curie / మేడమ్ క్యూరీ',
        'C',
        'M',
        '',
        49
    ),
    (
        'Which mammal lays eggs\nతెలుగు: గుడ్లు పెట్టే క్షీరదం ఏది',
        'Dolphin / డాల్ఫిన్',
        'Duck-billed Platypus / డక్-బిల్డ్ ప్లాటిపస్ (Duck-billed Platypus)',
        'Whale / తిమింగలం',
        'Dugong / దుగోంగ్',
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
