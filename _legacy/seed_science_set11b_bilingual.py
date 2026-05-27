import sqlite3, os

SOURCE = 'Science_Set11B_Human_System2_Ext'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    ('Which gas is exchanged in the alveoli of the lungs?\\nతెలుగు: ఊపిరితిత్తుల అల్వియోలైలో ఏ వాయువు మార్పిడి జరుగుతుంది?', 'Oxygen and Carbon dioxide / ఆక్సిజన్ మరియు కార్బన్ డయాక్సైడ్', 'Only Oxygen / కేవలం ఆక్సిజన్ మాత్రమే', 'Only Carbon dioxide / కేవలం కార్బన్ డయాక్సైడ్ మాత్రమే', 'Nitrogen / నైట్రోజన్', 'A', 'M', '', 1),
    ('What is the normal breathing rate in humans at rest?\\nతెలుగు: విశ్రాంతిలో మానవులలో సాధారణ శ్వాస రేటు ఎంత?', '12-20 breaths/min / 12-20 శ్వాసలు/నిమిషం', '5-8 breaths/min / 5-8 శ్వాసలు/నిమిషం', '25-30 breaths/min / 25-30 శ్వాసలు/నిమిషం', '40-50 breaths/min / 40-50 శ్వాసలు/నిమిషం', 'A', 'M', '', 2),
    ('What is the main muscle involved in breathing?\\nతెలుగు: శ్వాసలో పాల్గొనే ప్రధాన కండరం ఏది?', 'Diaphragm / డయాఫ్రమ్', 'Biceps / బైసెప్స్', 'Triceps / ట్రైసెప్స్', 'Deltoid / డెల్టాయిడ్', 'A', 'M', '', 3),
    ('The voice box in humans is called?\\nతెలుగు: మానవులలో వాయిస్ బాక్స్‌ని ఏమంటారు?', 'Larynx / లారింక్స్', 'Pharynx / ఫారింక్స్', 'Trachea / శ్వాసనాళం', 'Bronchus / బ్రాంకస్', 'A', 'M', '', 4),
    ('Which part of the respiratory system prevents food from entering the airway?\\nతెలుగు: శ్వాసనాళంలోకి ఆహారం ప్రవేశించకుండా నిరోధించే భాగం ఏది?', 'Epiglottis / ఎపిగ్లాటిస్', 'Tonsils / టాన్సిల్స్', 'Uvula / ఉవులా', 'Adenoids / అడెనాయిడ్స్', 'A', 'M', '', 5),
    ('How many lobes does the right lung have?\\nతెలుగు: కుడి ఊపిరితిత్తికి ఎన్ని లోబులు ఉంటాయి?', 'Three / మూడు', 'Two / రెండు', 'Four / నాలుగు', 'One / ఒకటి', 'A', 'M', '', 6),
    ('What is the capacity of air lungs can hold at maximum?\\nతెలుగు: ఊపిరితిత్తులు గరిష్టంగా ఎంత గాలిని పట్టుకోగలవు?', 'About 6 litres / సుమారు 6 లీటర్లు', 'About 2 litres / సుమారు 2 లీటర్లు', 'About 10 litres / సుమారు 10 లీటర్లు', 'About 1 litre / సుమారు 1 లీటరు', 'A', 'M', '', 7),
    ('Which cells in blood carry oxygen?\\nతెలుగు: రక్తంలో ఆక్సిజన్ మోసుకెళ్ళే కణాలు ఏవి?', 'Red Blood Cells / ఎరుపు రక్త కణాలు', 'White Blood Cells / తెలుపు రక్త కణాలు', 'Platelets / ప్లేట్‌లెట్లు', 'Plasma / ప్లాస్మా', 'A', 'M', '', 8),
    ('What disease is caused by smoking that damages the alveoli?\\nతెలుగు: ధూమపానం వల్ల అల్వియోలైలు దెబ్బతినే వ్యాధి ఏది?', 'Emphysema / ఎంఫిసెమా', 'Asthma / ఆస్తమా', 'Pneumonia / న్యుమోనియా', 'Bronchitis / బ్రాంకైటిస్', 'A', 'M', '', 9),
    ('What is the windpipe also known as?\\nతెలుగు: విండ్‌పైప్‌ని మరొక పేరేమిటి?', 'Trachea / ట్రాకియా', 'Esophagus / అన్నవాహిక', 'Bronchus / బ్రాంకస్', 'Alveolus / అల్వియోలస్', 'A', 'M', '', 10),
    ('What is the functional unit of the kidney?\\nతెలుగు: మూత్రపిండం యొక్క క్రియాత్మక యూనిట్ ఏది?', 'Nephron / నెఫ్రాన్', 'Neuron / న్యూరాన్', 'Alveolus / అల్వియోలస్', 'Lobule / లోబ్యూల్', 'A', 'M', '', 11),
    ('How many kidneys does a healthy human have?\\nతెలుగు: ఆరోగ్యవంతమైన మానవుడికి ఎన్ని మూత్రపిండాలు ఉంటాయి?', 'Two / రెండు', 'One / ఒకటి', 'Three / మూడు', 'Four / నాలుగు', 'A', 'M', '', 12),
    ('What is the main nitrogenous waste excreted by humans?\\nతెలుగు: మానవులు విసర్జించే ప్రధాన నత్రజని వ్యర్థం ఏది?', 'Urea / యూరియా', 'Uric acid / యూరిక్ యాసిడ్', 'Ammonia / అమోనియా', 'Creatinine / క్రియాటినిన్', 'A', 'M', '', 13),
    ('Which organ filters blood to produce urine?\\nతెలుగు: మూత్రం ఉత్పత్తి చేయడానికి రక్తాన్ని వడగట్టే అవయవం ఏది?', 'Kidney / మూత్రపిండం', 'Liver / కాలేయం', 'Spleen / ప్లీహం', 'Pancreas / క్లోమం', 'A', 'M', '', 14),
    ('What is the tube that carries urine from kidney to bladder?\\nతెలుగు: మూత్రపిండం నుండి మూత్రాశయానికి మూత్రాన్ని తీసుకువెళ్ళే గొట్టం ఏది?', 'Ureter / యురేటర్', 'Urethra / యూరెత్రా', 'Vas deferens / వాస్ డెఫెరెన్స్', 'Duct / నాళం', 'A', 'M', '', 15),
    ('Which part of the nephron is responsible for reabsorption?\\nతెలుగు: పునశ్శోషణకు బాధ్యత వహించే నెఫ్రాన్ భాగం ఏది?', 'Tubule / ట్యూబ్యూల్', 'Glomerulus / గ్లోమెరులస్', 'Bowman\'s capsule / బోమన్ కాప్సూల్', 'Loop of Henle / హెన్లే లూప్', 'A', 'M', '', 16),
    ('What is the yellow colour of urine due to?\\nతెలుగు: మూత్రం పసుపు రంగుకు కారణం ఏది?', 'Urochrome pigment / యూరోక్రోమ్ వర్ణద్రవ్యం', 'Bilirubin / బిలిరుబిన్', 'Hemoglobin / హిమోగ్లోబిన్', 'Melanin / మెలనిన్', 'A', 'M', '', 17),
    ('Dialysis is performed when which organ fails?\\nతెలుగు: డయాలసిస్ ఏ అవయవం వైఫల్యమైనప్పుడు చేస్తారు?', 'Kidney / మూత్రపిండం', 'Heart / హృదయం', 'Liver / కాలేయం', 'Lung / ఊపిరితిత్తి', 'A', 'M', '', 18),
    ('Which hormone regulates water reabsorption in kidneys?\\nతెలుగు: మూత్రపిండాలలో నీటి పునశ్శోషణను నియంత్రించే హార్మోన్ ఏది?', 'ADH (Antidiuretic hormone) / ADH', 'Insulin / ఇన్సులిన్', 'Adrenaline / అడ్రినలిన్', 'Thyroxine / థైరాక్సిన్', 'A', 'M', '', 19),
    ('Sweat glands in skin perform which excretory function?\\nతెలుగు: చర్మంలో స్వేద గ్రంథులు ఏ విసర్జన పని నిర్వహిస్తాయి?', 'Excrete salts and water / లవణాలు మరియు నీరు విసర్జిస్తాయి', 'Produce hormones / హార్మోన్లు ఉత్పత్తి చేస్తాయి', 'Filter blood / రక్తాన్ని వడగడతాయి', 'Digest proteins / ప్రోటీన్లు జీర్ణిస్తాయి', 'A', 'M', '', 20),
    ('How many bones are there in an adult human body?\\nతెలుగు: పెద్దవారి మానవ శరీరంలో ఎన్ని ఎముకలు ఉంటాయి?', '206 / 206', '212 / 212', '198 / 198', '250 / 250', 'A', 'M', '', 21),
    ('What is the hardest substance in the human body?\\nతెలుగు: మానవ శరీరంలో అత్యంత గట్టి పదార్థం ఏది?', 'Tooth enamel / దంత ఎనామల్', 'Bone / ఎముక', 'Cartilage / కార్టిలేజ్', 'Nail / గోరు', 'A', 'M', '', 22),
    ('What is the largest bone in the human body?\\nతెలుగు: మానవ శరీరంలో అతిపెద్ద ఎముక ఏది?', 'Femur / ఫెమర్ (తొడ ఎముక)', 'Tibia / టిబియా', 'Humerus / హ్యూమెరస్', 'Radius / రేడియస్', 'A', 'M', '', 23),
    ('What is the smallest bone in the human body?\\nతెలుగు: మానవ శరీరంలో అతిచిన్న ఎముక ఏది?', 'Stapes (in ear) / స్టేపెస్ (చెవిలో)', 'Patella / పటెల్లా', 'Coccyx / కాక్సిక్స్', 'Metacarpal / మెటాకార్పల్', 'A', 'M', '', 24),
    ('What type of joint is found at the knee?\\nతెలుగు: మోకాలి వద్ద ఏ రకమైన కీలు ఉంటుంది?', 'Hinge joint / హింజ్ కీలు', 'Ball and socket joint / బాల్ అండ్ సాకెట్ కీలు', 'Pivot joint / పివట్ కీలు', 'Gliding joint / గ్లైడింగ్ కీలు', 'A', 'M', '', 25),
    ('What type of joint is found at the shoulder?\\nతెలుగు: భుజం వద్ద ఏ రకమైన కీలు ఉంటుంది?', 'Ball and socket joint / బాల్ అండ్ సాకెట్ కీలు', 'Hinge joint / హింజ్ కీలు', 'Pivot joint / పివట్ కీలు', 'Fixed joint / స్థిర కీలు', 'A', 'M', '', 26),
    ('What mineral makes bones hard and strong?\\nతెలుగు: ఎముకలను గట్టిగా మరియు బలంగా చేసే ఖనిజం ఏది?', 'Calcium / కాల్షియం', 'Iron / ఇనుము', 'Potassium / పొటాషియం', 'Sodium / సోడియం', 'A', 'M', '', 27),
    ('What is the spine (backbone) made of?\\nతెలుగు: వెన్నెముక దేనితో తయారవుతుంది?', 'Vertebrae / వెర్టిబ్రే', 'Ribs / పక్కటెముకలు', 'Cartilage only / కేవలం కార్టిలేజ్', 'Tendons / టెండాన్లు', 'A', 'M', '', 28),
    ('How many pairs of ribs are there in the human body?\\nతెలుగు: మానవ శరీరంలో ఎన్ని జతల పక్కటెముకలు ఉంటాయి?', '12 pairs / 12 జతలు', '10 pairs / 10 జతలు', '14 pairs / 14 జతలు', '8 pairs / 8 జతలు', 'A', 'M', '', 29),
    ('What connects bone to bone at a joint?\\nతెలుగు: ఒక కీలు వద్ద ఎముకను ఎముకకు కలిపేది ఏది?', 'Ligament / లిగమెంట్', 'Tendon / టెండాన్', 'Cartilage / కార్టిలేజ్', 'Muscle / కండరం', 'A', 'M', '', 30),
    ('What connects muscle to bone?\\nతెలుగు: కండరాన్ని ఎముకకు కలిపేది ఏది?', 'Tendon / టెండాన్', 'Ligament / లిగమెంట్', 'Nerve / నరం', 'Vein / సిర', 'A', 'M', '', 31),
    ('Where is blood produced in the body?\\nతెలుగు: శరీరంలో రక్తం ఎక్కడ ఉత్పత్తి అవుతుంది?', 'Bone marrow / ఎముక మజ్జ', 'Liver / కాలేయం', 'Spleen / ప్లీహం', 'Kidney / మూత్రపిండం', 'A', 'M', '', 32),
    ('What is cartilage?\\nతెలుగు: కార్టిలేజ్ అంటే ఏమిటి?', 'Flexible connective tissue / వంగే కనెక్టివ్ టిష్యూ', 'A type of bone / ఒక రకమైన ఎముక', 'A muscle type / ఒక కండర రకం', 'A nerve fiber / ఒక నరం', 'A', 'M', '', 33),
    ('The kneecap is also called?\\nతెలుగు: మోకాలి చిప్పను ఏమంటారు?', 'Patella / పటెల్లా', 'Clavicle / క్లావికల్', 'Scapula / స్కాప్యులా', 'Sternum / స్టర్నమ్', 'A', 'M', '', 34),
    ('What is the collarbone called?\\nతెలుగు: భుజం ఎముకను ఏమంటారు?', 'Clavicle / క్లావికల్', 'Scapula / స్కాప్యులా', 'Patella / పటెల్లా', 'Tibia / టిబియా', 'A', 'M', '', 35),
    ('The skull protects which organ?\\nతెలుగు: పుర్రె ఏ అవయవాన్ని రక్షిస్తుంది?', 'Brain / మెదడు', 'Eyes / కళ్ళు', 'Ears / చెవులు', 'Nose / ముక్కు', 'A', 'M', '', 36),
    ('What are the floating ribs?\\nతెలుగు: తేలే పక్కటెముకలు అంటే ఏమిటి?', 'Ribs not attached to sternum / స్టర్నమ్‌కు అనుసంధానించబడని పక్కటెముకలు', 'Ribs attached to spine only / వెన్నెముకకు మాత్రమే అనుసంధానించబడినవి', 'Broken ribs / విరిగిన పక్కటెముకలు', 'Extra ribs / అదనపు పక్కటెముకలు', 'A', 'M', '', 37),
    ('Osteoporosis is a disease of which body system?\\nతెలుగు: ఆస్టియోపోరోసిస్ ఏ శారీరక వ్యవస్థ వ్యాధి?', 'Skeletal system / అస్థి వ్యవస్థ', 'Digestive system / జీర్ణ వ్యవస్థ', 'Nervous system / నాడీ వ్యవస్థ', 'Circulatory system / రక్త ప్రసార వ్యవస్థ', 'A', 'M', '', 38),
    ('How many bones are in the human hand including wrist?\\nతెలుగు: మణికట్టుతో సహా మానవ చేతిలో ఎన్ని ఎముకలు ఉంటాయి?', '27 / 27', '20 / 20', '30 / 30', '15 / 15', 'A', 'M', '', 39),
    ('What is the medical term for the shoulder blade?\\nతెలుగు: భుజపు పళ్ళెం యొక్క వైద్య పదం ఏమిటి?', 'Scapula / స్కాప్యులా', 'Clavicle / క్లావికల్', 'Sternum / స్టర్నమ్', 'Humerus / హ్యూమెరస్', 'A', 'M', '', 40),
    ('The process by which kidneys filter blood is called?\\nతెలుగు: మూత్రపిండాలు రక్తాన్ని వడగట్టే ప్రక్రియ ఏమిటి?', 'Filtration / వడపోత', 'Osmosis / అభినేత్రం', 'Diffusion / వ్యాప్తి', 'Absorption / శోషణ', 'A', 'M', '', 41),
    ('Which vitamin is essential for bone health?\\nతెలుగు: ఎముక ఆరోగ్యానికి ఏ విటమిన్ అవసరం?', 'Vitamin D / విటమిన్ D', 'Vitamin C / విటమిన్ C', 'Vitamin A / విటమిన్ A', 'Vitamin K / విటమిన్ K', 'A', 'M', '', 42),
    ('Carbon dioxide is transported in blood mainly as?\\nతెలుగు: రక్తంలో కార్బన్ డయాక్సైడ్ ప్రధానంగా ఏ రూపంలో రవాణా అవుతుంది?', 'Bicarbonate ions / బైకార్బోనేట్ అయాన్లు', 'Dissolved gas / కరిగిన వాయువు', 'Bound to hemoglobin / హిమోగ్లోబిన్‌కు బంధించబడి', 'As carbonic acid / కార్బోనిక్ యాసిడ్‌గా', 'A', 'M', '', 43),
    ('What is the function of the pleura?\\nతెలుగు: ప్లూరా యొక్క పని ఏమిటి?', 'Protects and lubricates lungs / ఊపిరితిత్తులను రక్షిస్తుంది మరియు లూబ్రికేట్ చేస్తుంది', 'Filters air / గాలిని వడగడుతుంది', 'Produces oxygen / ఆక్సిజన్ ఉత్పత్తి చేస్తుంది', 'Stores carbon dioxide / కార్బన్ డయాక్సైడ్ నిల్వ చేస్తుంది', 'A', 'M', '', 44),
    ('Which organ removes excess water from blood?\\nతెలుగు: రక్తం నుండి అదనపు నీటిని తొలగించే అవయవం ఏది?', 'Kidney / మూత్రపిండం', 'Skin / చర్మం', 'Liver / కాలేయం', 'Intestine / పేగు', 'A', 'M', '', 45),
    ('What is the role of red blood cells in respiration?\\nతెలుగు: శ్వాసక్రియలో ఎర్ర రక్త కణాల పాత్ర ఏమిటి?', 'Transport oxygen / ఆక్సిజన్ రవాణా చేయడం', 'Produce oxygen / ఆక్సిజన్ ఉత్పత్తి చేయడం', 'Fight infections / సంక్రమణలతో పోరాడటం', 'Clot blood / రక్తాన్ని గడ్డకట్టించడం', 'A', 'M', '', 46),
    ('What is the name of the protein in RBCs that carries oxygen?\\nతెలుగు: ఆక్సిజన్ మోసుకెళ్ళే RBC ప్రోటీన్ పేరు ఏమిటి?', 'Hemoglobin / హిమోగ్లోబిన్', 'Albumin / అల్బుమిన్', 'Fibrin / ఫైబ్రిన్', 'Globulin / గ్లోబ్యులిన్', 'A', 'M', '', 47),
    ('Bones become brittle due to lack of which mineral?\\nతెలుగు: ఏ ఖనిజం కొరత వల్ల ఎముకలు పెళుసుగా మారతాయి?', 'Calcium / కాల్షియం', 'Iron / ఇనుము', 'Zinc / జింక్', 'Magnesium / మెగ్నీషియం', 'A', 'M', '', 48),
    ('Where does gas exchange occur in the lungs?\\nతెలుగు: ఊపిరితిత్తులలో వాయు మార్పిడి ఎక్కడ జరుగుతుంది?', 'Alveoli / అల్వియోలై', 'Bronchi / బ్రాంకై', 'Trachea / ట్రాకియా', 'Larynx / లారింక్స్', 'A', 'M', '', 49),
    ('Which bones protect the heart and lungs?\\nతెలుగు: హృదయం మరియు ఊపిరితిత్తులను ఏ ఎముకలు రక్షిస్తాయి?', 'Ribs and sternum / పక్కటెముకలు మరియు స్టర్నమ్', 'Skull / పుర్రె', 'Vertebrae / వెర్టిబ్రే', 'Pelvis / పెల్విస్', 'A', 'M', '', 50),
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