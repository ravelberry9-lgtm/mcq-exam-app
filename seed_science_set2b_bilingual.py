import sqlite3, os

SOURCE = 'Science_Set2B_Elements_Metals_Compounds_Ext'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    ('Which metal is liquid at room temperature?\\nతెలుగు: గది ఉష్ణోగ్రత వద్ద ద్రవ రూపంలో ఉండే లోహం ఏది?', 'Mercury / పాదరసం', 'Gallium / గాలియం', 'Lead / సీసం', 'Bromine / బ్రోమిన్', 'A', 'M', '', 1),
    ('The chemical symbol of Gold is\\nతెలుగు: బంగారం యొక్క రసాయన చిహ్నం ఏమిటి?', 'Go / Go', 'Gd / Gd', 'Au / Au', 'Ag / Ag', 'C', 'M', '', 2),
    ('Which alloy is used in electric fuse wires?\\nతెలుగు: విద్యుత్ ఫ్యూజ్ తీగలలో వాడే మిశ్రమ లోహం ఏది?', 'Zinc / జింక్', 'Tinsel / తారాగణం', 'Tin-Lead alloy / టిన్-లెడ్ మిశ్రమం', 'Steel / స్టీల్', 'C', 'M', '', 3),
    ('Bronze is an alloy of copper and\\nతెలుగు: కంచు అనేది రాగి మరియు ఏ లోహం మిశ్రమం?', 'Zinc / జింక్', 'Tin / టిన్', 'Nickel / నికెల్', 'Lead / సీసం', 'B', 'M', '', 4),
    ('The lightest metal is\\nతెలుగు: అత్యంత తేలికైన లోహం ఏది?', 'Sodium / సోడియం', 'Potassium / పొటాషియం', 'Lithium / లిథియం', 'Beryllium / బెరిలియం', 'C', 'M', '', 5),
    ('Which gas is produced when zinc reacts with dilute sulphuric acid?\\nతెలుగు: జింక్ పలుచన సల్ఫ్యూరిక్ ఆమ్లంతో చర్య జరిపినపుడు వెలువడే వాయువు ఏది?', 'Oxygen / ఆక్సిజన్', 'Nitrogen / నైట్రోజన్', 'Hydrogen / హైడ్రోజన్', 'Carbon dioxide / కార్బన్ డైయాక్సైడ్', 'C', 'M', '', 6),
    ('Rusting of iron is an example of\\nతెలుగు: ఇనుప తుప్పు పట్టడం దేనికి ఉదాహరణ?', 'Physical change / భౌతిక మార్పు', 'Chemical change / రసాయన మార్పు', 'Nuclear change / అణు మార్పు', 'None / ఏదీ కాదు', 'B', 'M', '', 7),
    ('Which metal does not react with water at all?\\nతెలుగు: నీటితో అసలు చర్య జరపని లోహం ఏది?', 'Sodium / సోడియం', 'Potassium / పొటాషియం', 'Gold / బంగారం', 'Calcium / కాల్షియం', 'C', 'M', '', 8),
    ('Galvanisation is the process of coating iron with\\nతెలుగు: గాల్వనైజేషన్ అంటే ఇనుముపై ఏది పూయడం?', 'Tin / టిన్', 'Nickel / నికెల్', 'Zinc / జింక్', 'Copper / రాగి', 'C', 'M', '', 9),
    ('The hardest natural substance is\\nతెలుగు: ప్రకృతిలో అత్యంత కఠినమైన పదార్థం ఏది?', 'Iron / ఇనుము', 'Diamond / హీరా', 'Graphite / గ్రాఫైట్', 'Quartz / క్వార్ట్జ్', 'B', 'M', '', 10),
    ('Stainless steel is an alloy of iron with\\nతెలుగు: స్టెయిన్‌లెస్ స్టీల్ ఇనుముతో ఏ లోహాల మిశ్రమం?', 'Copper and Tin / రాగి మరియు టిన్', 'Chromium and Nickel / క్రోమియం మరియు నికెల్', 'Zinc and Lead / జింక్ మరియు లెడ్', 'Aluminium and Manganese / అల్యూమినియం మరియు మాంగనీస్', 'B', 'M', '', 11),
    ('Which non-metal conducts electricity?\\nతెలుగు: విద్యుత్ వహించే అలోహం ఏది?', 'Sulphur / సల్ఫర్', 'Phosphorus / ఫాస్పరస్', 'Graphite / గ్రాఫైట్', 'Iodine / అయోడిన్', 'C', 'M', '', 12),
    ('The chemical name of common salt is\\nతెలుగు: సాధారణ ఉప్పు యొక్క రసాయన నామం ఏమిటి?', 'Sodium carbonate / సోడియం కార్బొనేట్', 'Sodium chloride / సోడియం క్లోరైడ్', 'Sodium bicarbonate / సోడియం బైకార్బొనేట్', 'Calcium chloride / కాల్షియం క్లోరైడ్', 'B', 'M', '', 13),
    ('Which metal is found in haemoglobin?\\nతెలుగు: హిమోగ్లోబిన్‌లో ఉండే లోహం ఏది?', 'Copper / రాగి', 'Manganese / మాంగనీస్', 'Iron / ఇనుము', 'Zinc / జింక్', 'C', 'M', '', 14),
    ('German silver is an alloy of\\nతెలుగు: జర్మన్ సిల్వర్ అనేది ఏ లోహాల మిశ్రమం?', 'Copper Zinc and Nickel / రాగి జింక్ మరియు నికెల్', 'Silver and Nickel / వెండి మరియు నికెల్', 'Copper and Aluminium / రాగి మరియు అల్యూమినియం', 'Tin and Lead / టిన్ మరియు లెడ్', 'A', 'M', '', 15),
    ('Brass is an alloy of\\nతెలుగు: పితల అనేది ఏ లోహాల మిశ్రమం?', 'Copper and Tin / రాగి మరియు టిన్', 'Copper and Zinc / రాగి మరియు జింక్', 'Copper and Nickel / రాగి మరియు నికెల్', 'Copper and Aluminium / రాగి మరియు అల్యూమినియం', 'B', 'M', '', 16),
    ('Which acid is present in vinegar?\\nతెలుగు: వెనిగర్‌లో ఉండే ఆమ్లం ఏది?', 'Hydrochloric acid / హైడ్రోక్లోరిక్ ఆమ్లం', 'Sulphuric acid / సల్ఫ్యూరిక్ ఆమ్లం', 'Acetic acid / ఎసిటిక్ ఆమ్లం', 'Nitric acid / నైట్రిక్ ఆమ్లం', 'C', 'M', '', 17),
    ('The formula of water is\\nతెలుగు: నీటి రసాయన సూత్రం ఏమిటి?', 'HO / HO', 'H2O / H2O', 'H2O2 / H2O2', 'OH / OH', 'B', 'M', '', 18),
    ('Which element is used in making pencils?\\nతెలుగు: పెన్సిళ్ళ తయారీలో ఉపయోగించే మూలకం ఏది?', 'Graphite / గ్రాఫైట్', 'Diamond / హీరా', 'Lead / సీసం', 'Carbon monoxide / కార్బన్ మోనాక్సైడ్', 'A', 'M', '', 19),
    ('The pH value of pure water is\\nతెలుగు: స్వచ్ఛమైన నీటి pH విలువ ఎంత?', '5 / 5', '7 / 7', '9 / 9', '14 / 14', 'B', 'M', '', 20),
    ('Which metal is extracted from bauxite ore?\\nతెలుగు: బాక్సైట్ ఖనిజం నుండి వెలికితీసే లోహం ఏది?', 'Iron / ఇనుము', 'Aluminium / అల్యూమినియం', 'Copper / రాగి', 'Zinc / జింక్', 'B', 'M', '', 21),
    ('Which acid is present in lemon juice?\\nతెలుగు: నిమ్మరసంలో ఉండే ఆమ్లం ఏది?', 'Oxalic acid / ఆక్సాలిక్ ఆమ్లం', 'Tartaric acid / టార్టారిక్ ఆమ్లం', 'Citric acid / సిట్రిక్ ఆమ్లం', 'Malic acid / మాలిక్ ఆమ్లం', 'C', 'M', '', 22),
    ('The process of extracting metals from ores is called\\nతెలుగు: ఖనిజాల నుండి లోహాలను వేరుచేసే ప్రక్రియను ఏమంటారు?', 'Mechanics / మెకానిక్స్', 'Metallurgy / లోహ విద్య', 'Chromatography / వర్ణ వేర్పాటు', 'Biochemistry / జీవ రసాయనం', 'B', 'M', '', 23),
    ('Magnetite is an ore of\\nతెలుగు: మాగ్నటైట్ ఏ లోహపు ఖనిజం?', 'Aluminium / అల్యూమినియం', 'Copper / రాగి', 'Iron / ఇనుము', 'Zinc / జింక్', 'C', 'M', '', 24),
    ('Which metal is the best conductor of electricity?\\nతెలుగు: విద్యుత్‌కు అత్యంత మంచి వాహకం ఏ లోహం?', 'Copper / రాగి', 'Aluminium / అల్యూమినియం', 'Silver / వెండి', 'Gold / బంగారం', 'C', 'M', '', 25),
    ('Soda water contains\\nతెలుగు: సోడా వాటర్‌లో కరిగించిన వాయువు ఏది?', 'O2 / ఆక్సిజన్', 'CO2 / కార్బన్ డైయాక్సైడ్', 'N2 / నైట్రోజన్', 'H2 / హైడ్రోజన్', 'B', 'M', '', 26),
    ('Which element has the symbol Fe?\\nతెలుగు: Fe చిహ్నం కలిగిన మూలకం ఏది?', 'Fluorine / ఫ్లోరిన్', 'Iron / ఇనుము', 'Francium / ఫ్రాన్సియం', 'Fermium / ఫెర్మియం', 'B', 'M', '', 27),
    ('Acid rain is caused mainly by\\nతెలుగు: ఆమ్ల వర్షానికి ప్రధాన కారణం ఏమిటి?', 'CO2 and O3 / CO2 మరియు O3', 'SO2 and NO2 / SO2 మరియు NO2', 'CH4 and N2O / CH4 మరియు N2O', 'HCl and HF / HCl మరియు HF', 'B', 'M', '', 28),
    ('Which metal is used in thermometers?\\nతెలుగు: థర్మామీటర్‌లో ఉపయోగించే లోహం ఏది?', 'Gallium / గాలియం', 'Mercury / పాదరసం', 'Lead / సీసం', 'Tin / తగరం', 'B', 'M', '', 29),
    ('The chemical formula of marble is\\nతెలుగు: మార్బుల్ యొక్క రసాయన సూత్రం ఏమిటి?', 'CaCO3 / CaCO3', 'CaSO4 / CaSO4', 'Ca(OH)2 / Ca(OH)2', 'CaCl2 / CaCl2', 'A', 'M', '', 30),
    ('Which gas is used in fire extinguishers?\\nతెలుగు: అగ్నిమాపక యంత్రాలలో వాడే వాయువు ఏది?', 'Oxygen / ఆక్సిజన్', 'Nitrogen / నైట్రోజన్', 'Carbon dioxide / కార్బన్ డైయాక్సైడ్', 'Hydrogen / హైడ్రోజన్', 'C', 'M', '', 31),
    ('The formula of caustic soda is\\nతెలుగు: కాస్టిక్ సోడా యొక్క రసాయన సూత్రం ఏమిటి?', 'Na2CO3 / Na2CO3', 'NaHCO3 / NaHCO3', 'NaOH / NaOH', 'NaCl / NaCl', 'C', 'M', '', 32),
    ('Cinnabar is an ore of\\nతెలుగు: సిన్నాబార్ ఏ లోహపు ఖనిజం?', 'Gold / బంగారం', 'Silver / వెండి', 'Mercury / పాదరసం', 'Lead / సీసం', 'C', 'M', '', 33),
    ('Which metal is used in aircraft manufacturing?\\nతెలుగు: విమానాల తయారీలో ఉపయోగించే లోహం ఏది?', 'Iron / ఇనుము', 'Aluminium / అల్యూమినియం', 'Copper / రాగి', 'Titanium / టైటానియం', 'B', 'M', '', 34),
    ('Plaster of Paris is made from\\nతెలుగు: ప్లాస్టర్ ఆఫ్ పారిస్ దేని నుండి తయారవుతుంది?', 'Limestone / లైమ్‌స్టోన్', 'Gypsum / జిప్సం', 'Sand / ఇసుక', 'Clay / బంకమట్టి', 'B', 'M', '', 35),
    ('Which element is a semiconductor?\\nతెలుగు: సెమీకండక్టర్ అయిన మూలకం ఏది?', 'Silicon / సిలికాన్', 'Copper / రాగి', 'Iron / ఇనుము', 'Sulphur / సల్ఫర్', 'A', 'M', '', 36),
    ('The gas used in welding is\\nతెలుగు: వెల్డింగ్‌లో ఉపయోగించే వాయువు ఏది?', 'Hydrogen / హైడ్రోజన్', 'Oxygen / ఆక్సిజన్', 'Acetylene / ఎసిటిలీన్', 'Nitrogen / నైట్రోజన్', 'C', 'M', '', 37),
    ('Washing soda is\\nతెలుగు: వాషింగ్ సోడా అంటే ఏమిటి?', 'NaCl / సోడియం క్లోరైడ్', 'Na2CO3 / సోడియం కార్బొనేట్', 'NaHCO3 / సోడియం బైకార్బొనేట్', 'NaOH / సోడియం హైడ్రాక్సైడ్', 'B', 'M', '', 38),
    ('Which metal is stored in kerosene?\\nతెలుగు: కిరోసిన్‌లో నిల్వ చేసే లోహం ఏది?', 'Sodium / సోడియం', 'Potassium / పొటాషియం', 'Lithium / లిథియం', 'Calcium / కాల్షియం', 'A', 'M', '', 39),
    ('Which acid is present in stomach?\\nతెలుగు: జఠరంలో ఉండే ఆమ్లం ఏది?', 'Sulphuric acid / సల్ఫ్యూరిక్ ఆమ్లం', 'Hydrochloric acid / హైడ్రోక్లోరిక్ ఆమ్లం', 'Nitric acid / నైట్రిక్ ఆమ్లం', 'Acetic acid / ఎసిటిక్ ఆమ్లం', 'B', 'M', '', 40),
    ('The element used in fluorescent lamps is\\nతెలుగు: ఫ్లోరోసెంట్ బల్బులలో వాడే వాయువు ఏది?', 'Neon / నియాన్', 'Argon / ఆర్గాన్', 'Mercury vapour / పాదరసపు ఆవిరి', 'Xenon / జీనాన్', 'C', 'M', '', 41),
    ('Quick lime is\\nతెలుగు: క్విక్ లైమ్ అంటే ఏమిటి?', 'Ca(OH)2 / Ca(OH)2', 'CaCO3 / CaCO3', 'CaO / CaO', 'CaCl2 / CaCl2', 'C', 'M', '', 42),
    ('The chemical formula of baking soda is\\nతెలుగు: బేకింగ్ సోడా యొక్క రసాయన సూత్రం ఏమిటి?', 'NaCl / NaCl', 'Na2CO3 / Na2CO3', 'NaHCO3 / NaHCO3', 'NaOH / NaOH', 'C', 'M', '', 43),
    ('Which element is present in all organic compounds?\\nతెలుగు: అన్ని సేంద్రీయ సమ్మేళనాలలో ఉండే మూలకం ఏది?', 'Nitrogen / నైట్రోజన్', 'Oxygen / ఆక్సిజన్', 'Carbon / కార్బన్', 'Hydrogen / హైడ్రోజన్', 'C', 'M', '', 44),
    ('The pH value of an acidic solution is\\nతెలుగు: ఆమ్ల ద్రావణం యొక్క pH విలువ?', 'Greater than 7 / 7 కంటే ఎక్కువ', 'Less than 7 / 7 కంటే తక్కువ', 'Equal to 7 / 7 కు సమానం', 'Greater than 14 / 14 కంటే ఎక్కువ', 'B', 'M', '', 45),
    ('Which gas is evolved when a metal reacts with an acid?\\nతెలుగు: లోహం ఆమ్లంతో చర్య జరిపినపుడు వెలువడే వాయువు ఏది?', 'Oxygen / ఆక్సిజన్', 'Nitrogen / నైట్రోజన్', 'Hydrogen / హైడ్రోజన్', 'Carbon dioxide / కార్బన్ డైయాక్సైడ్', 'C', 'M', '', 46),
    ('The chemical symbol of silver is\\nతెలుగు: వెండి యొక్క రసాయన చిహ్నం ఏమిటి?', 'Si / Si', 'Sr / Sr', 'Ag / Ag', 'Au / Au', 'C', 'M', '', 47),
    ('Iron pyrite is also known as\\nతెలుగు: ఐరన్ పైరైట్‌ను మరేమని పిలుస్తారు?', 'Real gold / నిజమైన బంగారం', 'Fools gold / మూర్ఖుల బంగారం', 'White gold / తెల్ల బంగారం', 'Black gold / నల్ల బంగారం', 'B', 'M', '', 48),
    ('The formula of sulphuric acid is\\nతెలుగు: సల్ఫ్యూరిక్ ఆమ్లం యొక్క రసాయన సూత్రం ఏమిటి?', 'HCl / HCl', 'HNO3 / HNO3', 'H2SO4 / H2SO4', 'H3PO4 / H3PO4', 'C', 'M', '', 49),
    ('Which metal is used in galvanisation?\\nతెలుగు: గాల్వనైజేషన్‌లో ఉపయోగించే లోహం ఏది?', 'Tin / టిన్', 'Zinc / జింక్', 'Copper / రాగి', 'Nickel / నికెల్', 'B', 'M', '', 50),
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