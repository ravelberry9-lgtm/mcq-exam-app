import sqlite3, os

SOURCE = 'Science_Set3B_Elements_Periodic_Table_Ext'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    ('How many elements are in the modern periodic table?\\nతెలుగు: ఆధునిక ఆవర్తన పట్టికలో ఎన్ని మూలకాలు ఉన్నాయి?', '108 / 108', '116 / 116', '118 / 118', '120 / 120', 'C', 'M', '', 1),
    ('Who developed the Modern Periodic Table?\\nతెలుగు: ఆధునిక ఆవర్తన పట్టికను ఎవరు రూపొందించారు?', 'Dalton / డాల్టన్', 'Mendeleev / మెండలీవ్', 'Moseley / మోస్లీ', 'Bohr / బోర్', 'C', 'M', '', 2),
    ('The number of periods in the modern periodic table is\\nతెలుగు: ఆధునిక ఆవర్తన పట్టికలో ఎన్ని పీరియడ్లు ఉన్నాయి?', '5 / 5', '6 / 6', '7 / 7', '8 / 8', 'C', 'M', '', 3),
    ('Noble gases belong to which group?\\nతెలుగు: నోబుల్ వాయువులు ఏ గ్రూప్‌కు చెందుతాయి?', 'Group 1 / గ్రూప్ 1', 'Group 16 / గ్రూప్ 16', 'Group 17 / గ్రూప్ 17', 'Group 18 / గ్రూప్ 18', 'D', 'M', '', 4),
    ('The most electronegative element is\\nతెలుగు: అత్యంత ఎలక్ట్రాన్ ఆకర్షణ శక్తి కలిగిన మూలకం ఏది?', 'Oxygen / ఆక్సిజన్', 'Chlorine / క్లోరిన్', 'Fluorine / ఫ్లోరిన్', 'Nitrogen / నైట్రోజన్', 'C', 'M', '', 5),
    ('Which group elements are called alkali metals?\\nతెలుగు: ఏ గ్రూప్ మూలకాలను క్షార లోహాలు అంటారు?', 'Group 1 / గ్రూప్ 1', 'Group 2 / గ్రూప్ 2', 'Group 17 / గ్రూప్ 17', 'Group 18 / గ్రూప్ 18', 'A', 'M', '', 6),
    ('The halogen group number is\\nతెలుగు: హాలోజన్ గ్రూప్ నంబర్ ఏమిటి?', '15 / 15', '16 / 16', '17 / 17', '18 / 18', 'C', 'M', '', 7),
    ('Atomic number of carbon is\\nతెలుగు: కార్బన్ యొక్క పరమాణు సంఖ్య ఎంత?', '4 / 4', '6 / 6', '8 / 8', '12 / 12', 'B', 'M', '', 8),
    ('Which is the first element in the periodic table?\\nతెలుగు: ఆవర్తన పట్టికలో మొదటి మూలకం ఏది?', 'Helium / హీలియం', 'Hydrogen / హైడ్రోజన్', 'Lithium / లిథియం', 'Oxygen / ఆక్సిజన్', 'B', 'M', '', 9),
    ('Isotopes have the same\\nతెలుగు: ఐసోటోప్‌లకు ఏది సమానంగా ఉంటుంది?', 'Mass number / ద్రవ్యరాశి సంఖ్య', 'Neutron number / న్యూట్రాన్ సంఖ్య', 'Atomic number / పరమాణు సంఖ్య', 'Atomic mass / పరమాణు ద్రవ్యరాశి', 'C', 'M', '', 10),
    ('Which element is known as the king of chemicals?\\nతెలుగు: రసాయనాల రాజు అని పిలువబడే మూలకం ఏది?', 'HCl / HCl', 'HNO3 / HNO3', 'H2SO4 / H2SO4', 'H3PO4 / H3PO4', 'C', 'M', '', 11),
    ('Litmus turns red in\\nతెలుగు: లిట్మస్ ఏ ద్రావణంలో ఎరుపు రంగు మారుతుంది?', 'Base / క్షారం', 'Neutral / తటస్థ', 'Acid / ఆమ్లం', 'Salt / లవణం', 'C', 'M', '', 12),
    ('The formula of nitric acid is\\nతెలుగు: నైట్రిక్ ఆమ్లం యొక్క రసాయన సూత్రం ఏమిటి?', 'HCl / HCl', 'HNO3 / HNO3', 'H2SO4 / H2SO4', 'H3PO4 / H3PO4', 'B', 'M', '', 13),
    ('When an acid reacts with a base the products are\\nతెలుగు: ఆమ్లం క్షారంతో చర్య జరిపినప్పుడు ఏర్పడే ఉత్పత్తులు ఏవి?', 'Acid + Water / ఆమ్లం + నీరు', 'Salt + Water / లవణం + నీరు', 'Base + Water / క్షారం + నీరు', 'Gas + Water / వాయువు + నీరు', 'B', 'M', '', 14),
    ('The atomic number of oxygen is\\nతెలుగు: ఆక్సిజన్ యొక్క పరమాణు సంఖ్య ఎంత?', '6 / 6', '8 / 8', '16 / 16', '18 / 18', 'B', 'M', '', 15),
    ('NaOH is a\\nతెలుగు: NaOH అనేది ఏమిటి?', 'Acid / ఆమ్లం', 'Base / క్షారం', 'Salt / లవణం', 'Neutral / తటస్థం', 'B', 'M', '', 16),
    ('Which is the most abundant element in the universe?\\nతెలుగు: విశ్వంలో అత్యంత సమృద్ధిగా ఉండే మూలకం ఏది?', 'Oxygen / ఆక్సిజన్', 'Carbon / కార్బన్', 'Hydrogen / హైడ్రోజన్', 'Helium / హీలియం', 'C', 'M', '', 17),
    ('The chemical formula of common washing soda is\\nతెలుగు: వాషింగ్ సోడా యొక్క రసాయన సూత్రం ఏమిటి?', 'Na2CO3.10H2O / Na2CO3.10H2O', 'NaCl / NaCl', 'NaHCO3 / NaHCO3', 'NaOH / NaOH', 'A', 'M', '', 18),
    ('Which element has the highest melting point?\\nతెలుగు: అత్యంత ఎక్కువ ద్రవీభవన స్థానం కలిగిన మూలకం ఏది?', 'Iron / ఇనుము', 'Tungsten / టంగ్స్టన్', 'Carbon / కార్బన్', 'Platinum / ప్లాటినం', 'B', 'M', '', 19),
    ('The symbol of Potassium is\\nతెలుగు: పొటాషియం యొక్క రసాయన చిహ్నం ఏమిటి?', 'P / P', 'Po / Po', 'K / K', 'Pt / Pt', 'C', 'M', '', 20),
    ('Alkalis are oxides or hydroxides of\\nతెలుగు: క్షారాలు ఏ లోహాల ఆక్సైడులు లేదా హైడ్రాక్సైడులు?', 'Noble metals / నోబుల్ లోహాలు', 'Transition metals / పరివర్తన లోహాలు', 'Active metals / చురుకైన లోహాలు', 'Metalloids / అర్ధలోహాలు', 'C', 'M', '', 21),
    ('The number of valence electrons in chlorine is\\nతెలుగు: క్లోరిన్‌లో వేలెన్స్ ఎలక్ట్రాన్ల సంఖ్య ఎంత?', '5 / 5', '6 / 6', '7 / 7', '8 / 8', 'C', 'M', '', 22),
    ('Atomic mass of Sodium is\\nతెలుగు: సోడియం యొక్క పరమాణు ద్రవ్యరాశి ఎంత?', '11 / 11', '23 / 23', '35 / 35', '40 / 40', 'B', 'M', '', 23),
    ('Which indicator turns pink in basic solution?\\nతెలుగు: క్షార ద్రావణంలో పింక్ రంగు మారే సూచిక ఏది?', 'Litmus / లిట్మస్', 'Phenolphthalein / ఫినాల్ఫ్తలీన్', 'Methyl orange / మిథైల్ ఆరెంజ్', 'Turmeric / పసుపు', 'B', 'M', '', 24),
    ('The formula of bleaching powder is\\nతెలుగు: బ్లీచింగ్ పౌడర్ యొక్క రసాయన సూత్రం ఏమిటి?', 'Ca(OCl)Cl / Ca(OCl)Cl', 'CaCl2 / CaCl2', 'Ca(OH)2 / Ca(OH)2', 'CaO / CaO', 'A', 'M', '', 25),
    ('Which gas turns lime water milky?\\nతెలుగు: సున్నపు నీటిని పాలవలె తెల్లగా మార్చే వాయువు ఏది?', 'O2 / ఆక్సిజన్', 'CO2 / కార్బన్ డైయాక్సైడ్', 'H2 / హైడ్రోజన్', 'N2 / నైట్రోజన్', 'B', 'M', '', 26),
    ('The atomc number of iron is\\nతెలుగు: ఇనుము యొక్క పరమాణు సంఖ్య ఎంత?', '24 / 24', '26 / 26', '28 / 28', '30 / 30', 'B', 'M', '', 27),
    ('The element used in matchsticks is\\nతెలుగు: అగ్గిపెట్టెల్లో ఉపయోగించే మూలకం ఏది?', 'Sulphur / సల్ఫర్', 'Phosphorus / ఫాస్పరస్', 'Carbon / కార్బన్', 'Silicon / సిలికాన్', 'B', 'M', '', 28),
    ('Heavy water is used as\\nతెలుగు: హెవీ వాటర్ దేనిగా ఉపయోగిస్తారు?', 'Fuel / ఇంధనం', 'Moderator in nuclear reactors / అణు రియాక్టర్లలో మాడరేటర్', 'Coolant in engines / ఇంజన్లలో శీతలకారి', 'Solvent / ద్రావకం', 'B', 'M', '', 29),
    ('Which element is called the backbone of organic chemistry?\\nతెలుగు: సేంద్రీయ రసాయన శాస్త్రానికి వెన్నెముక అయిన మూలకం ఏది?', 'Nitrogen / నైట్రోజన్', 'Hydrogen / హైడ్రోజన్', 'Carbon / కార్బన్', 'Oxygen / ఆక్సిజన్', 'C', 'M', '', 30),
    ('Which acid is used in car batteries?\\nతెలుగు: కారు బ్యాటరీలలో ఉపయోగించే ఆమ్లం ఏది?', 'Hydrochloric acid / హైడ్రోక్లోరిక్ ఆమ్లం', 'Sulphuric acid / సల్ఫ్యూరిక్ ఆమ్లం', 'Nitric acid / నైట్రిక్ ఆమ్లం', 'Acetic acid / ఎసిటిక్ ఆమ్లం', 'B', 'M', '', 31),
    ('The formula of table salt is\\nతెలుగు: టేబుల్ సాల్ట్ యొక్క రసాయన సూత్రం ఏమిటి?', 'KCl / KCl', 'NaCl / NaCl', 'NaOH / NaOH', 'Na2CO3 / Na2CO3', 'B', 'M', '', 32),
    ('Dry ice is solid\\nతెలుగు: డ్రై ఐస్ అంటే ఘన రూపంలో ఉండే ఏ పదార్థం?', 'H2O / H2O', 'CO2 / CO2', 'N2 / N2', 'SO2 / SO2', 'B', 'M', '', 33),
    ('Which gas is used in filling weather balloons?\\nతెలుగు: వాతావరణ బెలూన్లను నింపే వాయువు ఏది?', 'Hydrogen / హైడ్రోజన్', 'Helium / హీలియం', 'Nitrogen / నైట్రోజన్', 'Oxygen / ఆక్సిజన్', 'B', 'M', '', 34),
    ('Which element is the best conductor of heat?\\nతెలుగు: ఉష్ణానికి అత్యంత మంచి వాహకం ఏ మూలకం?', 'Copper / రాగి', 'Silver / వెండి', 'Gold / బంగారం', 'Diamond / హీరా', 'D', 'M', '', 35),
    ('Ozone layer protects us from\\nతెలుగు: ఓజోన్ పొర మనల్ని ఏ వికిరణం నుండి రక్షిస్తుంది?', 'Infrared rays / పరారుణ కిరణాలు', 'Radio waves / రేడియో తరంగాలు', 'Ultraviolet rays / అతినీలలోహిత కిరणాలు', 'Cosmic rays / కాస్మిక్ కిరణాలు', 'C', 'M', '', 36),
    ('The valency of carbon is\\nతెలుగు: కార్బన్ యొక్క సంయోజకత ఎంత?', '2 / 2', '3 / 3', '4 / 4', '6 / 6', 'C', 'M', '', 37),
    ('Which element is used in making fireworks?\\nతెలుగు: బాణాసంచా తయారీలో ఉపయోగించే మూలకం ఏది?', 'Sulphur / సల్ఫర్', 'Potassium nitrate / పొటాషియం నైట్రేట్', 'Magnesium / మాగ్నీషియం', 'All of these / ఇవన్నీ', 'D', 'M', '', 38),
    ('The formula of calcium hydroxide is\\nతెలుగు: కాల్షియం హైడ్రాక్సైడ్ యొక్క రసాయన సూత్రం ఏమిటి?', 'CaO / CaO', 'Ca(OH)2 / Ca(OH)2', 'CaCO3 / CaCO3', 'CaCl2 / CaCl2', 'B', 'M', '', 39),
    ('Sodium bicarbonate is used in\\nతెలుగు: సోడియం బైకార్బొనేట్ దేనిలో ఉపయోగిస్తారు?', 'Baking / వంట', 'Cleaning / శుభ్రపరచడం', 'Welding / వెల్డింగ్', 'Painting / రంగువేయడం', 'A', 'M', '', 40),
    ('Which metal forms an oxide that is amphoteric?\\nతెలుగు: ఉభయగుణ (amphoteric) ఆక్సైడ్ ఏర్పరిచే లోహం ఏది?', 'Sodium / సోడియం', 'Calcium / కాల్షియం', 'Aluminium / అల్యూమినియం', 'Iron / ఇనుము', 'C', 'M', '', 41),
    ('The atomic number of nitrogen is\\nతెలుగు: నైట్రోజన్ యొక్క పరమాణు సంఖ్య ఎంత?', '5 / 5', '6 / 6', '7 / 7', '8 / 8', 'C', 'M', '', 42),
    ('Which gas is produced when bleaching powder reacts with dilute acid?\\nతెలుగు: బ్లీచింగ్ పౌడర్ పలుచన ఆమ్లంతో చర్య జరిపినపుడు వెలువడే వాయువు ఏది?', 'Oxygen / ఆక్సిజన్', 'Chlorine / క్లోరిన్', 'Hydrogen / హైడ్రోజన్', 'CO2 / CO2', 'B', 'M', '', 43),
    ('The mass number is the sum of\\nతెలుగు: ద్రవ్యరాశి సంఖ్య అంటే ఏమిటి?', 'Protons and electrons / ప్రోటాన్లు మరియు ఎలక్ట్రాన్లు', 'Protons and neutrons / ప్రోటాన్లు మరియు న్యూట్రాన్లు', 'Neutrons and electrons / న్యూట్రాన్లు మరియు ఎలక్ట్రాన్లు', 'Protons only / ప్రోటాన్లు మాత్రమే', 'B', 'M', '', 44),
    ('Which of the following is not an element?\\nతెలుగు: కింది వాటిలో మూలకం కానిది ఏది?', 'Gold / బంగారం', 'Silver / వెండి', 'Water / నీరు', 'Oxygen / ఆక్సిజన్', 'C', 'M', '', 45),
    ('Dilute HCl + NaOH gives\\nతెలుగు: HCl + NaOH చర్య వల్ల ఏమి ఏర్పడుతుంది?', 'NaCl + H2O / NaCl + H2O', 'Na2CO3 + H2 / Na2CO3 + H2', 'NaHCO3 + H2O / NaHCO3 + H2O', 'NaOH + HCl / NaOH + HCl', 'A', 'M', '', 46),
    ('The symbol of Tungsten is\\nతెలుగు: టంగ్స్టన్ యొక్క రసాయన చిహ్నం ఏమిటి?', 'T / T', 'Tu / Tu', 'W / W', 'Tg / Tg', 'C', 'M', '', 47),
    ('Elements in the same period have the same\\nతెలుగు: ఒకే పీరియడ్‌లోని మూలకాలకు ఏది సమానంగా ఉంటుంది?', 'Number of shells / కక్ష్యల సంఖ్య', 'Valence electrons / వేలెన్స్ ఎలక్ట్రాన్లు', 'Atomic number / పరమాణు సంఖ్య', 'Atomic mass / పరమాణు ద్రవ్యరాశి', 'A', 'M', '', 48),
    ('Which is the most reactive halogen?\\nతెలుగు: అత్యంత చురుకైన హాలోజన్ ఏది?', 'Iodine / అయోడిన్', 'Bromine / బ్రోమిన్', 'Chlorine / క్లోరిన్', 'Fluorine / ఫ్లోరిన్', 'D', 'M', '', 49),
    ('Hydrogen bonding is strongest in\\nతెలుగు: హైడ్రోజన్ బంధం బలంగా ఉండే సమ్మేళనం ఏది?', 'HF / HF', 'H2O / H2O', 'NH3 / NH3', 'HCl / HCl', 'A', 'M', '', 50),
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