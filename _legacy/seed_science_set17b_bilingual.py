import sqlite3, os

SOURCE = 'Science_Set17B_Plants2_Ext'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    ('What is pollination?\\nతెలుగు: పరాగ సంపర్కం అంటే ఏమిటి?', 'Transfer of pollen from anther to stigma / పుప్పొడి మకరందం నుండి కళంకానికి బదిలీ', 'Fertilization of egg / గుడ్డు ఫలదీకరణం', 'Seed germination / విత్తన మొలకెత్తడం', 'Fruit formation / ఫలం ఏర్పడటం', 'A', 'M', '', 1),
    ('Which part of the flower becomes the fruit?\\nతెలుగు: పూలలో ఏ భాగం ఫలంగా మారుతుంది?', 'Ovary / అండాశయం', 'Petals / రేకులు', 'Sepals / వికలాలు', 'Stamens / కేసరాలు', 'A', 'M', '', 2),
    ('Cross-pollination occurs between flowers of?\\nతెలుగు: శిలువ పరాగ సంపర్కం ఏ పూల మధ్య జరుగుతుంది?', 'Different plants of same species / అదే జాతికి చెందిన వేర్వేరు మొక్కలు', 'Same flower / అదే పూ', 'Same plant / అదే మొక్క', 'Artificial means only / కేవలం కృత్రిమ మార్గాల ద్వారా', 'A', 'M', '', 3),
    ('Seed dispersal by wind is called?\\nతెలుగు: గాలి ద్వారా విత్తన వ్యాప్తిని ఏమంటారు?', 'Anemochory / అనిమోకోరీ', 'Zoochory / జూకోరీ', 'Hydrochory / హైడ్రోకోరీ', 'Autochory / ఆటోకోరీ', 'A', 'M', '', 4),
    ('What is vegetative propagation?\\nతెలుగు: వృద్ధిమంత వ్యాప్తి అంటే ఏమిటి?', 'Growing new plants from non-reproductive parts / జనన రహిత భాగాల నుండి కొత్త మొక్కలు పెంచడం', 'Seed germination / విత్తన మొలకెత్తడం', 'Pollination / పరాగ సంపర్కం', 'Fertilization / ఫలదీకరణం', 'A', 'M', '', 5),
    ('Which agent is NOT a pollinating agent?\\nతెలుగు: పరాగ సంపర్కం చేసే కారకం కానిది ఏది?', 'Earthworm / వానపాముట', 'Wind / గాలి', 'Bees / తేనెటీగలు', 'Water / నీరు', 'A', 'M', '', 6),
    ('Double fertilization is a feature of?\\nతెలుగు: రెట్టింపు ఫలదీకరణం ఏ జాతికి లక్షణం?', 'Angiosperms (flowering plants) / ఆంజియోస్పర్మ్లు (పుష్పించే మొక్కలు)', 'Gymnosperms / జిమ్నోస్పర్మ్లు', 'Bryophytes / బ్రయోఫైట్లు', 'Pteridophytes / టెరిడోఫైట్లు', 'A', 'M', '', 7),
    ('What is the function of the endosperm in seeds?\\nతెలుగు: విత్తనాలలో ఎండోస్పర్మ్ యొక్క పని ఏమిటి?', 'Provides nutrition to developing embryo / అభివృద్ధి చెందుతున్న పిండానికి పోషణ అందిస్తుంది', 'Protects the seed / విత్తనాన్ని రక్షిస్తుంది', 'Forms the new root / కొత్త మూలం ఏర్పరుస్తుంది', 'Produces pollen / పుప్పొడి ఉత్పత్తి చేస్తుంది', 'A', 'M', '', 8),
    ('Fruits protect seeds and aid in their?\\nతెలుగు: ఫలాలు విత్తనాలను రక్షిస్తాయి మరియు వాటి దేనికి సహాయపడతాయి?', 'Dispersal / వ్యాప్తికి', 'Photosynthesis / కిరణజన్య సంయోగానికి', 'Growth / వృద్ధికి', 'Respiration / శ్వాసక్రియకి', 'A', 'M', '', 9),
    ('Spore formation is a method of reproduction in?\\nతెలుగు: బీజ ఏర్పాటు ఏ జాతిలో పునరుత్పత్తి పద్ధతి?', 'Ferns and mosses / ఫెర్న్లు మరియు నాచులు', 'Flowering plants / పుష్పించే మొక్కలు', 'Gymnosperms / జిమ్నోస్పర్మ్లు', 'All plants / అన్ని మొక్కలు', 'A', 'M', '', 10),
    ('Which plant gives us cotton?\\nతెలుగు: మనకు పత్తి ఇచ్చే మొక్క ఏది?', 'Gossypium (cotton plant) / గాసిపియం (పత్తి మొక్క)', 'Linum (flax) / లినమ్ (అవిసె)', 'Bamboo / వెదురు', 'Jute plant / జనపనార మొక్క', 'A', 'M', '', 11),
    ('Rubber is obtained from which plant?\\nతెలుగు: రబ్బరు ఏ మొక్క నుండి పొందబడుతుంది?', 'Hevea brasiliensis (rubber tree) / హేవియా బ్రాసిలియెన్సిస్ (రబ్బరు చెట్టు)', 'Acacia / అకేషియా', 'Eucalyptus / యూకలిప్టస్', 'Bamboo / వెదురు', 'A', 'M', '', 12),
    ('Tea is made from the leaves of?\\nతెలుగు: టీ ఏ మొక్క ఆకుల నుండి తయారవుతుంది?', 'Camellia sinensis / కెమెలియా సైనెన్సిస్', 'Coffea arabica / కొఫేయా అరేబికా', 'Cocoa plant / కోకో మొక్క', 'Mint / మింట్', 'A', 'M', '', 13),
    ('Which part of the paddy plant gives us rice?\\nతెలుగు: వరి మొక్కలో ఏ భాగం మనకు వరి ఇస్తుంది?', 'Grain/seed / గింజ/విత్తనం', 'Stem / కాండం', 'Leaves / ఆకులు', 'Root / మూలం', 'A', 'M', '', 14),
    ('Turmeric is obtained from which part of the plant?\\nతెలుగు: పసుపు మొక్కలో ఏ భాగం నుండి పొందబడుతుంది?', 'Rhizome / రైజోమ్', 'Root / మూలం', 'Leaf / ఆకు', 'Bark / బెరడు', 'A', 'M', '', 15),
    ('Which plant is the source of quinine (antimalarial drug)?\\nతెలుగు: క్వినైన్ (మలేరియా వ్యతిరేక ఔషధం) యొక్క మూలం ఏ మొక్క?', 'Cinchona (bark) / సింకోనా (బెరడు)', 'Neem / వేప', 'Tulsi / తులసి', 'Aloe vera / అలోవేరా', 'A', 'M', '', 16),
    ('Coffee is made from the seeds of?\\nతెలుగు: కాఫీ ఏ మొక్క విత్తనాల నుండి తయారవుతుంది?', 'Coffea arabica / కొఫేయా అరేబికా', 'Camellia sinensis / కెమెలియా సైనెన్సిస్', 'Theobroma cacao / తియోబ్రోమా కాకాయో', 'Vanilla plant / వెనీలా మొక్క', 'A', 'M', '', 17),
    ('Which is the tallest grass in the world?\\nతెలుగు: ప్రపంచంలో అత్యంత ఎత్తైన గడ్డి ఏది?', 'Bamboo / వెదురు', 'Sugarcane / చెరకు', 'Wheat / గోధుమ', 'Corn / మొక్కజొన్న', 'A', 'M', '', 18),
    ('Which plant gives us jute fiber?\\nతెలుగు: మనకు జనపనార పీచు ఇచ్చే మొక్క ఏది?', 'Corchorus (jute plant) / కార్కోరస్ (జనపనార మొక్క)', 'Linum (flax) / లినమ్ (అవిసె)', 'Gossypium (cotton) / గాసిపియం (పత్తి)', 'Agave / అగేవ్', 'A', 'M', '', 19),
    ('Neem has which property useful in medicines?\\nతెలుగు: వేపకు ఔషధాలలో ఉపయోగపడే ఏ గుణం ఉంది?', 'Antibacterial and antifungal / యాంటీబాక్టీరియల్ మరియు యాంటీఫంగల్', 'Only antiviral / కేవలం యాంటీవైరల్', 'Only pain relief / కేవలం నొప్పి నివారణ', 'Only nutritional / కేవలం పోషకమైన', 'A', 'M', '', 20),
    ('What causes powdery mildew in plants?\\nతెలుగు: మొక్కలలో పౌడరీ మిల్డ్యూ దేని వల్ల వస్తుంది?', 'Fungal infection / శిలీంద్ర సంక్రమణ', 'Bacterial infection / బాక్టీరియా సంక్రమణ', 'Viral infection / వైరల్ సంక్రమణ', 'Insect attack / కీటక దాడి', 'A', 'M', '', 21),
    ('Late blight of potato is caused by?\\nతెలుగు: బంగాళాదుంప లేట్ బ్లైట్ దేని వల్ల వస్తుంది?', 'Phytophthora infestans (water mould) / ఫైటాఫ్తోరా ఇన్‌ఫెస్టాన్స్', 'Bacteria / బాక్టీరియా', 'Virus / వైరస్', 'Nematode / నెమటోడ్', 'A', 'M', '', 22),
    ('Mosaic disease in plants is caused by?\\nతెలుగు: మొక్కలలో మొజాయిక్ వ్యాధి దేని వల్ల వస్తుంది?', 'Virus / వైరస్', 'Bacteria / బాక్టీరియా', 'Fungi / ఫంగై', 'Insects / కీటకాలు', 'A', 'M', '', 23),
    ('What is a biological control method for plant pests?\\nతెలుగు: మొక్కల తెగుళ్ళకు జీవ నియంత్రణ పద్ధతి ఏమిటి?', 'Using natural predators / సహజ వేటగాళ్ళను ఉపయోగించడం', 'Chemical pesticides / రసాయన పురుగు మందులు', 'Burning crops / పంటలను కాల్చడం', 'Using antibiotics / యాంటీబయోటిక్స్ ఉపయోగించడం', 'A', 'M', '', 24),
    ('Crown gall disease in plants is caused by?\\nతెలుగు: మొక్కలలో క్రౌన్ గాల్ వ్యాధి దేని వల్ల వస్తుంది?', 'Agrobacterium tumefaciens (bacteria) / అగ్రోబాక్టీరియం ట్యూమిఫేసియన్స్ (బాక్టీరియా)', 'Fungi / ఫంగై', 'Virus / వైరస్', 'Nematode / నెమటోడ్', 'A', 'M', '', 25),
    ('The scientific name of rice is?\\nతెలుగు: వరి యొక్క శాస్త్రీయ నామం ఏమిటి?', 'Oryza sativa / ఒరైజా సటివా', 'Triticum aestivum / ట్రిటికమ్ ఏస్టివమ్', 'Zea mays / జియా మేస్', 'Hordeum vulgare / హోర్డియమ్ వల్గేర్', 'A', 'M', '', 26),
    ('Which plant produces latex used to make rubber?\\nతెలుగు: రబ్బరు తయారుచేయడానికి లాటెక్స్ ఉత్పత్తి చేసే మొక్క ఏది?', 'Rubber tree (Hevea brasiliensis) / రబ్బరు చెట్టు', 'Sunflower / పొద్దుతిరుగుడు', 'Opium poppy / నల్లమందు పప్పి', 'Sugarcane / చెరకు', 'A', 'M', '', 27),
    ('Clove is the dried flower bud of?\\nతెలుగు: లవంగం ఏ మొక్క యొక్క ఎండిన పుష్ప మొగ్గ?', 'Syzygium aromaticum / సైజిగియం అరోమాటికమ్', 'Cinnamomum verum / సిన్నమోమమ్ వెరమ్', 'Piper nigrum / పైపర్ నిగ్రమ్', 'Elettaria cardamomum / ఎలెట్టేరియా కార్డమోమమ్', 'A', 'M', '', 28),
    ('Cinnamon is obtained from which part of the tree?\\nతెలుగు: దాల్చిన చెక్క చెట్టు యొక్క ఏ భాగం నుండి పొందబడుతుంది?', 'Bark / బెరడు', 'Root / మూలం', 'Leaf / ఆకు', 'Seed / విత్తనం', 'A', 'M', '', 29),
    ('Aloe vera gel is used for its?\\nతెలుగు: అలోవేరా జెల్ దేని కోసం ఉపయోగించబడుతుంది?', 'Medicinal and skin care properties / ఔషధ మరియు చర్మ సంరక్షణ గుణాలు', 'Timber / చెక్క', 'Food source / ఆహార వనరు', 'Dye production / రంగు ఉత్పత్తి', 'A', 'M', '', 30),
    ('Wheat is a?\\nతెలుగు: గోధుమ ఏ రకానికి చెందుతుంది?', 'Cereal / తృణధాన్యం', 'Legume / పప్పుధాన్యం', 'Oil seed / నూనె విత్తనం', 'Fiber crop / పీచు పంట', 'A', 'M', '', 31),
    ('Photosynthesis produces which carbohydrate as end product?\\nతెలుగు: కిరణజన్య సంయోగం చివర ఉత్పత్తి చేసే కార్బోహైడ్రేట్ ఏది?', 'Glucose / గ్లూకోజ్', 'Starch / పిండి పదార్థం', 'Cellulose / సెల్యులోజ్', 'Sucrose / సుక్రోజ్', 'A', 'M', '', 32),
    ('Onion bulb is a modification of?\\nతెలుగు: ఉల్లి బల్బ్ దేని మార్పు?', 'Leaf base / ఆకు ఆధారం', 'Root / మూలం', 'Stem / కాండం', 'Flower / పువ్వు', 'A', 'M', '', 33),
    ('What is vernalization in plants?\\nతెలుగు: మొక్కలలో వెర్నలైజేషన్ అంటే ఏమిటి?', 'Cold treatment to induce flowering / పుష్పీభవనం ప్రేరేపించడానికి చలి చికిత్స', 'Heat treatment / వేడి చికిత్స', 'Water treatment / నీటి చికిత్స', 'Light treatment / కాంతి చికిత్స', 'A', 'M', '', 34),
    ('Which of these is a parasitic plant?\\nతెలుగు: ఇవి పరాన్నభోజన మొక్కలలో ఏది?', 'Cuscuta (dodder) / కస్కుటా (డాడర్)', 'Wheat / గోధుమ', 'Sunflower / పొద్దుతిరుగుడు', 'Mango / మామిడి', 'A', 'M', '', 35),
    ('Photoperiodism refers to plant response to?\\nతెలుగు: ఫోటోపీరియడిజం మొక్కలు దేనికి స్పందించడం?', 'Length of day and night / పగటి మరియు రాత్రి నిడివికి', 'Intensity of light / కాంతి తీవ్రతకు', 'Color of light / కాంతి రంగుకు', 'Temperature / ఉష్ణోగ్రతకు', 'A', 'M', '', 36),
    ('Saprophytic plants get nutrition from?\\nతెలుగు: సాప్రోఫైటిక్ మొక్కలు పోషణ ఎక్కడ నుండి పొందుతాయి?', 'Dead and decaying organic matter / చనిపోయిన మరియు కుళ్ళుతున్న సేంద్రియ పదార్థం', 'Living organisms / జీవుల నుండి', 'Photosynthesis / కిరణజన్య సంయోగం', 'Soil minerals only / కేవలం మట్టి ఖనిజాలు', 'A', 'M', '', 37),
    ('Insectivorous plants supplement their nutrition by digesting?\\nతెలుగు: కీటకభక్షక మొక్కలు దేన్ని జీర్ణించుకొని తమ పోషణను పూర్తి చేస్తాయి?', 'Insects and small animals / కీటకాలు మరియు చిన్న జంతువులు', 'Dead leaves / మృత ఆకులు', 'Soil / మట్టి', 'Fungi / ఫంగై', 'A', 'M', '', 38),
    ('Vegetative propagation through stem cuttings is common in?\\nతెలుగు: కాండం కత్తిళ్ళ ద్వారా వృద్ధిమంత వ్యాప్తి ఏ మొక్కలలో సాధారణంగా జరుగుతుంది?', 'Rose, sugarcane / గులాబి, చెరకు', 'Wheat, rice / గోధుమ, వరి', 'Mango only / కేవలం మామిడి', 'All grasses / అన్ని గడ్డులు', 'A', 'M', '', 39),
    ('The scientific name of mango is?\\nతెలుగు: మామిడి యొక్క శాస్త్రీయ నామం ఏమిటి?', 'Mangifera indica / మాంగిఫెరా ఇండికా', 'Azadirachta indica / అజాడిరాక్టా ఇండికా', 'Carica papaya / కారికా పాపయా', 'Psidium guajava / పీడియమ్ గ్వాజావా', 'A', 'M', '', 40),
    ('Bark of which tree is used as a spice?\\nతెలుగు: ఏ చెట్టు బెరడు సుగంధ ద్రవ్యంగా ఉపయోగించబడుతుంది?', 'Cinnamon tree / దాల్చిన చెక్క చెట్టు', 'Neem tree / వేప చెట్టు', 'Mango tree / మామిడి చెట్టు', 'Bamboo / వెదురు', 'A', 'M', '', 41),
    ('The study of fungi is called?\\nతెలుగు: ఫంగైని అధ్యయనం చేయడాన్ని ఏమంటారు?', 'Mycology / మైకాలజీ', 'Botany / వృక్షశాస్త్రం', 'Phycology / ఫైకాలజీ', 'Virology / వైరాలజీ', 'A', 'M', '', 42),
    ('Which crop is grown in waterlogged conditions?\\nతెలుగు: నీరు నిల్వ ఉండే పరిస్థితులలో ఏ పంట పెరుగుతుంది?', 'Rice / వరి', 'Wheat / గోధుమ', 'Cotton / పత్తి', 'Groundnut / వేరుశెనగ', 'A', 'M', '', 43),
    ('Which plant product is used as a natural insecticide?\\nతెలుగు: సహజ పురుగు మందుగా ఉపయోగించే మొక్క ఉత్పత్తి ఏది?', 'Neem oil / వేప నూనె', 'Coconut oil / కొబ్బరి నూనె', 'Sunflower oil / పొద్దుతిరుగుడు నూనె', 'Castor oil / ఆముదం నూనె', 'A', 'M', '', 44),
    ('What is a hybrid plant?\\nతెలుగు: హైబ్రిడ్ మొక్క అంటే ఏమిటి?', 'A plant produced by crossing two different varieties / రెండు వేర్వేరు రకాలను దాటించి ఉత్పత్తి చేయబడిన మొక్క', 'A genetically modified plant / జన్యుపరంగా మార్చబడిన మొక్క', 'A plant grown without soil / మట్టి లేకుండా పెరిగిన మొక్క', 'A wild plant / అడవి మొక్క', 'A', 'M', '', 45),
    ('Soil erosion can be prevented by?\\nతెలుగు: నేల కోతను ఏ ద్వారా నివారించవచ్చు?', 'Planting trees and ground cover plants / చెట్లు మరియు భూ కప్పు మొక్కలు నాటడం', 'Removing all vegetation / అన్ని వృక్షసంపదను తొలగించడం', 'Increasing irrigation / నీటిపారుదల పెంచడం', 'Tilling more soil / ఎక్కువ నేల దున్నడం', 'A', 'M', '', 46),
    ('What is a carnivorous plant?\\nతెలుగు: కార్నివోరస్ మొక్క అంటే ఏమిటి?', 'A plant that traps and digests insects / కీటకాలను పట్టుకొని జీర్ణించే మొక్క', 'A plant that eats other plants / ఇతర మొక్కలను తినే మొక్క', 'A plant that grows in deserts / ఎడారులలో పెరిగే మొక్క', 'A plant that doesn\'t photosynthesize / కిరణజన్య సంయోగం చేయని మొక్క', 'A', 'M', '', 47),
    ('Tissue culture is used to?\\nతెలుగు: టిష్యూ కల్చర్ ఏ కోసం ఉపయోగించబడుతుంది?', 'Grow plants from small tissue samples / చిన్న కణజాల నమూనాల నుండి మొక్కలు పెంచడం', 'Study animal tissues / జంతు కణజాలాలు అధ్యయనం చేయడం', 'Produce vaccines / వ్యాక్సిన్లు ఉత్పత్తి చేయడం', 'Test soil quality / మట్టి నాణ్యత పరీక్షించడం', 'A', 'M', '', 48),
    ('Which gas do plants release during photosynthesis?\\nతెలుగు: కిరణజన్య సంయోగం సమయంలో మొక్కలు ఏ వాయువు విడుదల చేస్తాయి?', 'Oxygen / ఆక్సిజన్', 'Carbon dioxide / కార్బన్ డయాక్సైడ్', 'Nitrogen / నైట్రోజన్', 'Water vapor / నీటి ఆవిరి', 'A', 'M', '', 49),
    ('Grafting in plants is a technique used to?\\nతెలుగు: మొక్కలలో గ్రాఫ్టింగ్ ఏ పద్ధతి?', 'Join parts of two plants to grow as one / రెండు మొక్కల భాగాలను ఒకటిగా పెరగడానికి కలపడం', 'Grow plants from seeds / విత్తనాల నుండి మొక్కలు పెంచడం', 'Study plant diseases / మొక్కల వ్యాధులు అధ్యయనం చేయడం', 'Control plant growth / మొక్కల వృద్ధి నియంత్రించడం', 'A', 'M', '', 50),
]

def seed():
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("DELETE FROM questions WHERE source_file=?", (SOURCE,))
    cur.executemany(
        """INSERT INTO questions (folder,topic,source_file,question_text,option_a,option_b,option_c,option_d,correct_answer,difficulty,explanation,question_order)
           VALUES ('GK','General_Science',?,?,?,?,?,?,?,?,?,?)""",
        [(SOURCE, *q) for q in questions])
    con.commit()
    n = cur.execute("SELECT COUNT(*) FROM questions WHERE source_file=?",(SOURCE,)).fetchone()[0]
    con.close(); print(f"Inserted {n} from {SOURCE}")

if __name__ == '__main__': seed()