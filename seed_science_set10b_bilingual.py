import sqlite3, os

SOURCE = 'Science_Set10B_Human_System1_Ext'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    ('How many chambers does the human heart have?\\nతెలుగు: మానవ హృదయానికి ఎన్ని గదులు ఉంటాయి?', '2 / 2', '3 / 3', '4 / 4', '6 / 6', 'C', 'M', '', 1),
    ('The largest artery in the human body is\\nతెలుగు: మానవ శరీరంలో అతిపెద్ద ధమని ఏది?', 'Pulmonary artery / పల్మనరీ ధమని', 'Aorta / ఆయోర్టా', 'Carotid artery / కెరోటిడ్ ధమని', 'Femoral artery / ఫెమోరల్ ధమని', 'B', 'M', '', 2),
    ('Normal human body temperature is\\nతెలుగు: సాధారణ మానవ శరీర ఉష్ణోగ్రత ఎంత?', '36.9°C / 36.9°C', '37°C / 37°C', '38°C / 38°C', '35°C / 35°C', 'B', 'M', '', 3),
    ('The fluid part of blood is called\\nతెలుగు: రక్తంలో ద్రవ భాగాన్ని ఏమంటారు?', 'Serum / సీరమ్', 'Plasma / ప్లాస్మా', 'Haemoglobin / హిమోగ్లోబిన్', 'Lymph / లింఫ్', 'B', 'M', '', 4),
    ('Blood group was discovered by\\nతెలుగు: రక్త గ్రూపులను ఎవరు కనుగొన్నారు?', 'Pasteur / పాశ్చర్', 'Fleming / ఫ్లెమింగ్', 'Landsteiner / లాండ్‌స్టీనర్', 'Harvey / హార్వే', 'C', 'M', '', 5),
    ('Which blood cells are responsible for immunity?\\nతెలుగు: రోగనిరోధకత కోసం బాధ్యత వహించే రక్త కణాలు ఏవి?', 'Red blood cells / ఎర్ర రక్త కణాలు', 'Platelets / ప్లేట్‌లెట్లు', 'White blood cells / తెల్ల రక్త కణాలు', 'Plasma cells / ప్లాస్మా కణాలు', 'C', 'M', '', 6),
    ('The process of digestion begins in the\\nతెలుగు: జీర్ణక్రియ ప్రారంభమయ్యే స్థానం ఏది?', 'Stomach / జఠరం', 'Small intestine / చిన్న ప్రేగు', 'Mouth / నోరు', 'Oesophagus / అన్నవాహిక', 'C', 'M', '', 7),
    ('Saliva contains which enzyme?\\nతెలుగు: లాలాజలంలో ఉండే ఎంజైమ్ ఏది?', 'Pepsin / పెప్సిన్', 'Ptyalin / ప్యాలిన్', 'Trypsin / ట్రిప్సిన్', 'Lipase / లైపేస్', 'B', 'M', '', 8),
    ('The universal blood donor is\\nతెలుగు: యూనివర్సల్ రక్త దాత (donor) ఏ గ్రూపు?', 'AB+ / AB+', 'O- / O-', 'A+ / A+', 'B+ / B+', 'B', 'M', '', 9),
    ('The universal blood recipient is\\nతెలుగు: యూనివర్సల్ రక్త గ్రాహకుడు (recipient) ఏ గ్రూపు?', 'O+ / O+', 'AB+ / AB+', 'A- / A-', 'B- / B-', 'B', 'M', '', 10),
    ('Heartbeat is controlled by\\nతెలుగు: హృదయ స్పందన ఏ కేంద్రం ద్వారా నియంత్రించబడుతుంది?', 'SA node / SA నోడ్', 'AV node / AV నోడ్', 'Cerebrum / మస్తిష్కం', 'Spinal cord / వెన్నుపాము', 'A', 'M', '', 11),
    ('The normal heartbeat of an adult at rest is\\nతెలుగు: విశ్రాంతిలో ఉన్న వయోజనుని సాధారణ హృదయ స్పందన రేటు ఎంత?', '40-60 / 40-60', '60-100 / 60-100', '100-120 / 100-120', '120-140 / 120-140', 'B', 'M', '', 12),
    ('The total number of teeth in adult humans is\\nతెలుగు: వయోజన మానవునిలో పండ్ల సంఖ్య ఎంత?', '28 / 28', '30 / 30', '32 / 32', '36 / 36', 'C', 'M', '', 13),
    ('Bile is stored in\\nతెలుగు: పైత్య రసం ఎక్కడ నిల్వ ఉంటుంది?', 'Liver / కాలేయం', 'Pancreas / క్లోమం', 'Gall bladder / పిత్తాశయం', 'Duodenum / ద్వాదశాంత్రం', 'C', 'M', '', 14),
    ('The iron-containing protein in red blood cells is\\nతెలుగు: ఎర్ర రక్త కణాలలో ఇనుము కలిగిన ప్రోటీన్ ఏమిటి?', 'Albumin / అల్బుమిన్', 'Fibrin / ఫైబ్రిన్', 'Haemoglobin / హిమోగ్లోబిన్', 'Myoglobin / మయోగ్లోబిన్', 'C', 'M', '', 15),
    ('Pepsin is produced by\\nతెలుగు: పెప్సిన్ ఏ అవయవం ఉత్పత్తి చేస్తుంది?', 'Liver / కాలేయం', 'Pancreas / క్లోమం', 'Stomach / జఠరం', 'Small intestine / చిన్న ప్రేగు', 'C', 'M', '', 16),
    ('The longest part of the digestive tract is\\nతెలుగు: జీర్ణ వ్యవస్థలో అత్యంత పొడవైన భాగం ఏది?', 'Stomach / జఠరం', 'Large intestine / పెద్ద ప్రేగు', 'Small intestine / చిన్న ప్రేగు', 'Oesophagus / అన్నవాహిక', 'C', 'M', '', 17),
    ('Blood clotting is helped by\\nతెలుగు: రక్తం గడ్డకట్టడానికి సహాయం చేసే రక్త అంశాలు ఏవి?', 'Red blood cells / ఎర్ర రక్త కణాలు', 'White blood cells / తెల్ల రక్త కణాలు', 'Platelets / ప్లేట్‌లెట్లు', 'Plasma / ప్లాస్మా', 'C', 'M', '', 18),
    ('The circulation of blood was discovered by\\nతెలుగు: రక్త ప్రసరణను ఎవరు కనుగొన్నారు?', 'Harvey / హార్వే', 'Vesalius / వెసాలియస్', 'Pasteur / పాశ్చర్', 'Koch / కాక్', 'A', 'M', '', 19),
    ('Arteries carry blood\\nతెలుగు: ధమనులు ఏ రకమైన రక్తాన్ని తీసుకువెళతాయి?', 'From heart to body / హృదయం నుండి శరీరానికి', 'From body to heart / శరీరం నుండి హృదయానికి', 'Only oxygenated / కేవలం ఆక్సిజన్ కలిగిన', 'Only deoxygenated / కేవలం ఆక్సిజన్ లేని', 'A', 'M', '', 20),
    ('Veins carry blood\\nతెలుగు: సిరలు ఏ రకమైన రక్తాన్ని తీసుకువెళతాయి?', 'From heart to body / హృదయం నుండి శరీరానికి', 'From body to heart / శరీరం నుండి హృదయానికి', 'Only oxygenated / కేవలం ఆక్సిజన్ కలిగిన', 'Backwards / వెనక్కి', 'B', 'M', '', 21),
    ('The largest organ in the human body is\\nతెలుగు: మానవ శరీరంలో అతిపెద్ద అవయవం ఏది?', 'Heart / హృదయం', 'Liver / కాలేయం', 'Brain / మెదడు', 'Skin / చర్మం', 'D', 'M', '', 22),
    ('Gastric juice contains\\nతెలుగు: జఠర రసంలో ఉండేవి ఏవి?', 'HCl and pepsin / HCl మరియు పెప్సిన్', 'NaOH and trypsin / NaOH మరియు ట్రిప్సిన్', 'Bile and lipase / పైత్య రసం మరియు లైపేస్', 'Amylase only / అమైలేస్ మాత్రమే', 'A', 'M', '', 23),
    ('Which vitamin is essential for blood clotting?\\nతెలుగు: రక్తం గడ్డకట్టడానికి అవసరమైన విటమిన్ ఏది?', 'Vitamin A / విటమిన్ A', 'Vitamin C / విటమిన్ C', 'Vitamin D / విటమిన్ D', 'Vitamin K / విటమిన్ K', 'D', 'M', '', 24),
    ('The function of the small intestine is\\nతెలుగు: చిన్న ప్రేగు యొక్క ప్రధాన పని ఏమిటి?', 'Storing food / ఆహారం నిల్వ', 'Absorption of nutrients / పోషకాల శోషణ', 'Producing enzymes / ఎంజైమ్‌లు ఉత్పత్తి', 'Filtering blood / రక్తం వడపోత', 'B', 'M', '', 25),
    ('Anaemia is caused by deficiency of\\nతెలుగు: రక్తహీనత దేని లోపం వల్ల కలుగుతుంది?', 'Iron / ఇనుము', 'Calcium / కాల్షియం', 'Vitamin C / విటమిన్ C', 'Potassium / పొటాషియం', 'A', 'M', '', 26),
    ('The pulmonary vein carries\\nతెలుగు: పల్మనరీ సిర ఏ రకమైన రక్తాన్ని తీసుకువెళుతుంది?', 'Deoxygenated blood / ఆక్సిజన్ లేని రక్తం', 'Oxygenated blood / ఆక్సిజన్ కలిగిన రక్తం', 'Mixed blood / మిశ్రమ రక్తం', 'Plasma only / ప్లాస్మా మాత్రమే', 'B', 'M', '', 27),
    ('Absorption of water mainly occurs in the\\nతెలుగు: నీరు ప్రధానంగా ఏ అవయవంలో శోషణ అవుతుంది?', 'Stomach / జఠరం', 'Small intestine / చిన్న ప్రేగు', 'Large intestine / పెద్ద ప్రేగు', 'Oesophagus / అన్నవాహిక', 'C', 'M', '', 28),
    ('Which blood group is called the universal recipient?\\nతెలుగు: యూనివర్సల్ గ్రాహకుడు అని పిలువబడే రక్త గ్రూపు ఏది?', 'O / O', 'A / A', 'B / B', 'AB / AB', 'D', 'M', '', 29),
    ('The life span of red blood cells is approximately\\nతెలుగు: ఎర్ర రక్త కణాల జీవిత కాలం సుమారు ఎంత?', '7 days / 7 రోజులు', '30 days / 30 రోజులు', '120 days / 120 రోజులు', '365 days / 365 రోజులు', 'C', 'M', '', 30),
    ('Capillaries connect\\nతెలుగు: కేశనాళికలు దేనిని కలుపుతాయి?', 'Heart and lungs / హృదయం మరియు ఊపిరితిత్తులు', 'Arteries and veins / ధమనులు మరియు సిరలు', 'Brain and spinal cord / మెదడు మరియు వెన్నుపాము', 'Liver and kidney / కాలేయం మరియు మూత్రపిండం', 'B', 'M', '', 31),
    ('The enzyme that digests protein in the stomach is\\nతెలుగు: జఠరంలో ప్రోటీన్‌ను జీర్ణించే ఎంజైమ్ ఏది?', 'Amylase / అమైలేస్', 'Lipase / లైపేస్', 'Pepsin / పెప్సిన్', 'Trypsin / ట్రిప్సిన్', 'C', 'M', '', 32),
    ('Rh factor in blood was first studied using\\nతెలుగు: రక్తంలో Rh కారకం మొదట ఏ జంతువులో అధ్యయనం చేయబడింది?', 'Rabbit / కుందేలు', 'Dog / కుక్క', 'Rhesus monkey / రీసస్ కోతి', 'Rat / ఎలుక', 'C', 'M', '', 33),
    ('The cardiac muscle works\\nతెలుగు: హృదయ కండరం ఎలా పనిచేస్తుంది?', 'Voluntarily / స్వచ్ఛందంగా', 'Involuntarily / అనైచ్ఛికంగా', 'Only during exercise / వ్యాయామ సమయంలో మాత్రమే', 'Only during sleep / నిద్రలో మాత్రమే', 'B', 'M', '', 34),
    ('The number of ribs in the human body is\\nతెలుగు: మానవ శరీరంలో పక్కటెముకల సంఖ్య ఎంత?', '20 / 20', '24 / 24', '26 / 26', '28 / 28', 'B', 'M', '', 35),
    ('The digestive enzyme in saliva acts on\\nతెలుగు: లాలాజలంలో ఉండే జీర్ణ ఎంజైమ్ ఏ పదార్థంపై పనిచేస్తుంది?', 'Proteins / ప్రోటీన్లు', 'Fats / కొవ్వులు', 'Starch / పిండి పదార్థం', 'Vitamins / విటమిన్లు', 'C', 'M', '', 36),
    ('The average volume of blood in an adult human is\\nతెలుగు: వయోజన మానవునిలో రక్తం సగటు పరిమాణం ఎంత?', '2-3 litres / 2-3 లీటర్లు', '5-6 litres / 5-6 లీటర్లు', '8-10 litres / 8-10 లీటర్లు', '1-2 litres / 1-2 లీటర్లు', 'B', 'M', '', 37),
    ('Insulin is produced in the pancreas by\\nతెలుగు: క్లోమంలో ఇన్సులిన్ ఉత్పత్తి చేసే కణాలు ఏవి?', 'Alpha cells / ఆల్ఫా కణాలు', 'Beta cells / బీటా కణాలు', 'Delta cells / డెల్టా కణాలు', 'Acinar cells / అసినార్ కణాలు', 'B', 'M', '', 38),
    ('The appendix is attached to\\nతెలుగు: అపెండిక్స్ ఏ అవయవానికి అతికి ఉంటుంది?', 'Stomach / జఠరం', 'Small intestine / చిన్న ప్రేగు', 'Large intestine / పెద్ద ప్రేగు', 'Liver / కాలేయం', 'C', 'M', '', 39),
    ('Lymph nodes filter\\nతెలుగు: లింఫ్ నోడ్లు దేనిని వడపోతాయి?', 'Blood / రక్తం', 'Urine / మూత్రం', 'Lymph fluid / లింఫ్ ద్రవం', 'Bile / పైత్య రసం', 'C', 'M', '', 40),
    ('The largest internal organ is\\nతెలుగు: అతిపెద్ద అంతరంగ అవయవం ఏది?', 'Heart / హృదయం', 'Lungs / ఊపిరితిత్తులు', 'Liver / కాలేయం', 'Kidney / మూత్రపిండం', 'C', 'M', '', 41),
    ('The process by which nutrients enter the bloodstream is called\\nతెలుగు: పోషకాలు రక్తప్రవాహంలోకి ప్రవేశించే ప్రక్రియను ఏమంటారు?', 'Digestion / జీర్ణక్రియ', 'Absorption / శోషణ', 'Assimilation / అనుకలనం', 'Excretion / విసర్జన', 'B', 'M', '', 42),
    ('Double circulation means blood passes through the heart\\nతెలుగు: ద్విచక్రీయ ప్రసరణ అంటే రక్తం హృదయం గుండా ఎలా ప్రవహిస్తుంది?', 'Once / ఒకసారి', 'Twice / రెండుసార్లు', 'Three times / మూడుసార్లు', 'Four times / నాలుగుసార్లు', 'B', 'M', '', 43),
    ('Deficiency of haemoglobin causes\\nతెలుగు: హిమోగ్లోబిన్ లోపం వల్ల వచ్చే వ్యాధి ఏమిటి?', 'Diabetes / మధుమేహం', 'Anaemia / రక్తహీనత', 'Jaundice / కామెర్లు', 'Hypertension / రక్తపోటు', 'B', 'M', '', 44),
    ('The portal vein carries blood from\\nతెలుగు: పోర్టల్ సిర ఎక్కడ నుండి రక్తాన్ని తీసుకువెళుతుంది?', 'Lungs to heart / ఊపిరితిత్తుల నుండి హృదయానికి', 'Digestive organs to liver / జీర్ణ అవయవాల నుండి కాలేయానికి', 'Heart to kidneys / హృదయం నుండి మూత్రపిండాలకు', 'Brain to heart / మెదడు నుండి హృదయానికి', 'B', 'M', '', 45),
    ('The enzymes in pancreatic juice include\\nతెలుగు: క్లోమ రసంలో ఉండే ఎంజైమ్‌లు ఏవి?', 'Pepsin only / పెప్సిన్ మాత్రమే', 'Trypsin lipase and amylase / ట్రిప్సిన్ లైపేస్ మరియు అమైలేస్', 'Ptyalin only / ప్యాలిన్ మాత్రమే', 'HCl and pepsin / HCl మరియు పెప్సిన్', 'B', 'M', '', 46),
    ('ECG is used to study\\nతెలుగు: ECG దేనిని అధ్యయనం చేయడానికి ఉపయోగిస్తారు?', 'Brain function / మెదడు పని', 'Heart function / హృదయ పని', 'Kidney function / మూత్రపిండాల పని', 'Liver function / కాలేయ పని', 'B', 'M', '', 47),
    ('Jaundice affects the\\nతెలుగు: కామెర్లు ఏ అవయవాన్ని ప్రభావితం చేస్తుంది?', 'Kidney / మూత్రపిండం', 'Heart / హృదయం', 'Liver / కాలేయం', 'Lungs / ఊపిరితిత్తులు', 'C', 'M', '', 48),
    ('The smallest blood vessels are\\nతెలుగు: అత్యంత చిన్న రక్తనాళాలు ఏవి?', 'Arteries / ధమనులు', 'Veins / సిరలు', 'Capillaries / కేశనాళికలు', 'Venules / సూక్ష్మ సిరలు', 'C', 'M', '', 49),
    ('Plasma proteins are mainly produced by\\nతెలుగు: ప్లాస్మా ప్రోటీన్లు ప్రధానంగా ఏ అవయవంలో ఉత్పత్తి అవుతాయి?', 'Spleen / ప్లీహం', 'Kidney / మూత్రపిండం', 'Liver / కాలేయం', 'Pancreas / క్లోమం', 'C', 'M', '', 50),
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