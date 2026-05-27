import sqlite3, os

SOURCE = 'Science_Set6B_Reactions_Changes_Separation_Ext'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    ('A catalyst changes the rate of a reaction but\\nతెలుగు: ఉత్ప్రేరకం చర్య వేగాన్ని మారుస్తుంది కానీ?', 'Is consumed / వినియోగమవుతుంది', 'Is not consumed / వినియోగం కాదు', 'Raises temperature / ఉష్ణోగ్రత పెంచుతుంది', 'Changes products / ఉత్పత్తులు మారుస్తుంది', 'B', 'M', '', 1),
    ('Electrolysis means decomposition by\\nతెలుగు: ఎలక్ట్రోలైసిస్ అంటే ఏ శక్తి ద్వారా విచ్ఛేదనం?', 'Heat / వేడి', 'Light / వెలుతురు', 'Electric current / విద్యుత్ ప్రవాహం', 'Pressure / పీడనం', 'C', 'M', '', 2),
    ('Which separation technique uses differences in boiling points?\\nతెలుగు: మరుగు స్థానాల తేడా ఆధారంగా వేరుచేయు పద్ధతి ఏది?', 'Filtration / వడపోత', 'Distillation / స్వేదనం', 'Evaporation / బాష్పీభవనం', 'Centrifugation / సెంట్రిఫ్యుగేషన్', 'B', 'M', '', 3),
    ('In oxidation the element\\nతెలుగు: ఆక్సీకరణంలో మూలకం ఏమి చేస్తుంది?', 'Gains electrons / ఎలక్ట్రాన్లు పొందుతుంది', 'Loses electrons / ఎలక్ట్రాన్లు కోల్పోతుంది', 'Gains protons / ప్రోటాన్లు పొందుతుంది', 'Loses protons / ప్రోటాన్లు కోల్పోతుంది', 'B', 'M', '', 4),
    ('Exothermic reactions\\nతెలుగు: ఉష్ణమోచక చర్యలు?', 'Absorb heat / వేడిని గ్రహిస్తాయి', 'Release heat / వేడిని విడుదల చేస్తాయి', 'Require light / వెలుతురు అవసరమవుతుంది', 'Produce gas only / వాయువు మాత్రమే ఉత్పత్తి చేస్తాయి', 'B', 'M', '', 5),
    ('Chromatography separates mixtures based on\\nతెలుగు: క్రోమటోగ్రఫీ దేని ఆధారంగా మిశ్రమాలను వేరుచేస్తుంది?', 'Boiling point / మరుగు స్థానం', 'Density / సాంద్రత', 'Differential migration on stationary phase / స్తబ్ధ దశపై వేర్వేరు చలనం', 'Magnetic properties / అయస్కాంత గుణాలు', 'C', 'M', '', 6),
    ('A reversible reaction can proceed in\\nతెలుగు: వ్యతిక్రమ చర్య ఏ దిశల్లో సాగుతుంది?', 'One direction only / ఒకే దిశలో', 'Both directions / రెండు దిశల్లో', 'No direction / ఏ దిశలో సాగదు', 'Depends on catalyst / ఉత్ప్రేరకంపై ఆధారపడుతుంది', 'B', 'M', '', 7),
    ('What is a precipitate?\\nతెలుగు: అవక్షేపం అంటే ఏమిటి?', 'A gas formed in reaction / చర్యలో ఏర్పడే వాయువు', 'An insoluble solid formed in solution / ద్రావణంలో ఏర్పడే అద్రావణ ఘన పదార్థం', 'A colour change / రంగు మార్పు', 'An acid formed / ఏర్పడే ఆమ్లం', 'B', 'M', '', 8),
    ('The pH of a neutral solution is\\nతెలుగు: తటస్థ ద్రావణం యొక్క pH ఎంత?', '0 / 0', '7 / 7', '14 / 14', '4 / 4', 'B', 'M', '', 9),
    ('Which gas is produced when marble reacts with HCl?\\nతెలుగు: మార్బుల్ HCl తో చర్య జరిపినపుడు వెలువడే వాయువు ఏది?', 'H2 / H2', 'O2 / O2', 'CO2 / CO2', 'Cl2 / Cl2', 'C', 'M', '', 10),
    ('Burning of fuel is an example of\\nతెలుగు: ఇంధనం మండటం ఏ రకమైన చర్యకు ఉదాహరణ?', 'Physical change / భౌతిక మార్పు', 'Combination reaction / సంయోజన చర్య', 'Combustion reaction / దహన చర్య', 'Displacement reaction / స్థానభ్రంశ చర్య', 'C', 'M', '', 11),
    ('The process of dissolving a solid in liquid is\\nతెలుగు: ఘన పదార్థాన్ని ద్రవంలో కరిగించే ప్రక్రియ ఏమిటి?', 'Evaporation / బాష్పీభవనం', 'Solution formation / ద్రావణం ఏర్పడటం', 'Sublimation / ఊర్ధ్వపాతనం', 'Condensation / సంఘనీభవనం', 'B', 'M', '', 12),
    ('Reduction is the process of\\nతెలుగు: క్షయకరణం అంటే ఏమిటి?', 'Gaining electrons / ఎలక్ట్రాన్లు పొందటం', 'Losing electrons / ఎలక్ట్రాన్లు కోల్పోవడం', 'Gaining oxygen / ఆక్సిజన్ పొందటం', 'Losing hydrogen / హైడ్రోజన్ కోల్పోవడం', 'A', 'M', '', 13),
    ('Sublimation is the direct conversion of\\nతెలుగు: ఊర్ధ్వపాతనం అంటే ఏమిటి?', 'Liquid to gas / ద్రవం నుండి వాయువు', 'Solid to liquid / ఘనం నుండి ద్రవం', 'Solid to gas / ఘనం నుండి వాయువు', 'Gas to solid / వాయువు నుండి ఘనం', 'C', 'M', '', 14),
    ('Which gas is produced during photosynthesis?\\nతెలుగు: కిరణజన్య సంయోగక్రియ సమయంలో ఉత్పత్తి అయ్యే వాయువు ఏది?', 'CO2 / CO2', 'H2 / H2', 'O2 / O2', 'N2 / N2', 'C', 'M', '', 15),
    ('A double displacement reaction involves\\nతెలుగు: ద్వంద్వ స్థానభ్రంశ చర్యలో ఏమి జరుగుతుంది?', 'Exchange of ions between two compounds / రెండు సమ్మేళనాల మధ్య అయాన్ల మార్పిడి', 'One metal displacing another / ఒక లోహం మరొకదాన్ని స్థానభ్రంశం చేయడం', 'Addition of oxygen / ఆక్సిజన్ చేరడం', 'Removal of water / నీరు తొలగడం', 'A', 'M', '', 16),
    ('Fermentation is carried out by\\nతెలుగు: పులియబెట్టడం ఎవరిచే జరుగుతుంది?', 'Fungi / శిలీంధ్రాలు', 'Yeast / ఈస్ట్', 'Bacteria / బ్యాక్టీరియా', 'All of these / ఇవన్నీ', 'D', 'M', '', 17),
    ('Electrolysis of water produces\\nతెలుగు: నీటి విద్యుత్ విఘటనం వల్ల ఉత్పత్తి అయ్యేవి ఏవి?', 'H2 and N2 / H2 మరియు N2', 'H2 and O2 / H2 మరియు O2', 'CO2 and H2O / CO2 మరియు H2O', 'O2 and N2 / O2 మరియు N2', 'B', 'M', '', 18),
    ('Le Chatelier\'s principle states that\\nతెలుగు: లె చాటెలియర్ నియమం ఏమి చెప్తుంది?', 'Catalysts speed up reactions / ఉత్ప్రేరకాలు చర్య వేగం పెంచుతాయి', 'Equilibrium shifts to counteract change / సమతాస్థితి మార్పును నివారించేలా మారుతుంది', 'Acids neutralise bases / ఆమ్లాలు క్షారాలను తటస్థపరుస్తాయి', 'Temperature has no effect / ఉష్ణోగ్రత ప్రభావం లేదు', 'B', 'M', '', 19),
    ('Paper chromatography is used to separate\\nతెలుగు: పేపర్ క్రోమటోగ్రఫీ దేని వేరీకరణకు వాడతారు?', 'Metals / లోహాలు', 'Dyes and pigments / రంగులు మరియు వర్ణకాలు', 'Gases / వాయువులు', 'Radioactive elements / రేడియోధార్మిక మూలకాలు', 'B', 'M', '', 20),
    ('A catalyst that increases reaction rate is called\\nతెలుగు: చర్య వేగాన్ని పెంచే ఉత్ప్రేరకాన్ని ఏమంటారు?', 'Negative catalyst / ప్రతికూల ఉత్ప్రేరకం', 'Positive catalyst / అనుకూల ఉత్ప్రేరకం', 'Autocatalyst / స్వయం ఉత్ప్రేరకం', 'Inhibitor / నిరోధకం', 'B', 'M', '', 21),
    ('Decomposition reaction breaks down\\nతెలుగు: విఘటన చర్య అంటే?', 'Two compounds forming one / రెండు సమ్మేళనాలు ఒకటిగా ఏర్పడటం', 'One compound into simpler substances / ఒక సమ్మేళనం సరళ పదార్థాలుగా విడిపోవడం', 'A metal reacting with acid / లోహం ఆమ్లంతో చర్య జరపడం', 'Gas dissolving in liquid / వాయువు ద్రవంలో కరగడం', 'B', 'M', '', 22),
    ('The removal of water of crystallisation is called\\nతెలుగు: స్ఫటికీకరణ నీటిని తొలగించడాన్ని ఏమంటారు?', 'Dehydration / నిర్జలీకరణం', 'Hydration / జలీకరణం', 'Condensation / సంఘనీభవనం', 'Calcination / కాల్సినేషన్', 'A', 'M', '', 23),
    ('Which of the following is a redox reaction?\\nతెలుగు: కింది వాటిలో రెడాక్స్ చర్య ఏది?', 'NaCl dissolving in water / NaCl నీటిలో కరగడం', 'Combustion of carbon / కార్బన్ మండటం', 'Mixing salt and pepper / ఉప్పు మరియు మిరియాలు కలపడం', 'Melting of ice / మంచు కరగడం', 'B', 'M', '', 24),
    ('The Haber process produces\\nతెలుగు: హేబర్ ప్రక్రియ ద్వారా ఏమి తయారవుతుంది?', 'Sulphuric acid / సల్ఫ్యూరిక్ ఆమ్లం', 'Ammonia / అమోనియా', 'Nitric acid / నైట్రిక్ ఆమ్లం', 'Hydrochloric acid / హైడ్రోక్లోరిక్ ఆమ్లం', 'B', 'M', '', 25),
    ('Rate of reaction increases with\\nతెలుగు: చర్య వేగం దేనితో పెరుగుతుంది?', 'Decrease in temperature / ఉష్ణోగ్రత తగ్గడం', 'Increase in temperature / ఉష్ణోగ్రత పెరగడం', 'Decrease in concentration / సాంద్రత తగ్గడం', 'Increase in particle size / కణాల పరిమాణం పెరగడం', 'B', 'M', '', 26),
    ('Saponification is the process of making\\nతెలుగు: సపోనిఫికేషన్ అంటే ఏ తయారీ ప్రక్రియ?', 'Soap / సబ్బు', 'Plastic / ప్లాస్టిక్', 'Rubber / రబ్బర్', 'Dye / రంగు', 'A', 'M', '', 27),
    ('Centrifugation separates mixtures based on\\nతెలుగు: సెంట్రిఫ్యుగేషన్ దేని ఆధారంగా వేరుచేస్తుంది?', 'Boiling point / మరుగు స్థానం', 'Density difference / సాంద్రత తేడా', 'Solubility / కరిగే శక్తి', 'Magnetic property / అయస్కాంత గుణం', 'B', 'M', '', 28),
    ('A reaction where heat is absorbed is called\\nతెలుగు: వేడి గ్రహించే చర్యను ఏమంటారు?', 'Exothermic / ఉష్ణమోచక', 'Endothermic / ఉష్ణగ్రాహక', 'Thermoneutral / ఉష్ణ తటస్థ', 'Photochemical / కాంతి రసాయన', 'B', 'M', '', 29),
    ('Which is used to separate sand from water?\\nతెలుగు: నీటి నుండి ఇసుకను వేరుచేయడానికి ఏ పద్ధతి వాడతారు?', 'Distillation / స్వేదనం', 'Filtration / వడపోత', 'Crystallisation / స్ఫటికీకరణ', 'Chromatography / క్రోమటోగ్రఫీ', 'B', 'M', '', 30),
    ('The Contact process is used to manufacture\\nతెలుగు: కాంటాక్ట్ ప్రక్రియ ద్వారా ఏమి తయారు చేస్తారు?', 'HCl / HCl', 'H2SO4 / H2SO4', 'HNO3 / HNO3', 'NH3 / NH3', 'B', 'M', '', 31),
    ('A physical change is one that\\nతెలుగు: భౌతిక మార్పు అంటే ఏమిటి?', 'Forms new substances / కొత్త పదార్థాలు ఏర్పడతాయి', 'Is irreversible / తిరిగి మారదు', 'Does not form new substances / కొత్త పదార్థాలు ఏర్పడవు', 'Changes chemical properties / రసాయన లక్షణాలు మారతాయి', 'C', 'M', '', 32),
    ('Crystallisation is used to\\nతెలుగు: స్ఫటికీకరణ ఏ పని చేస్తుంది?', 'Separate gases / వాయువులను వేరుచేయడం', 'Purify solids / ఘన పదార్థాలను శుద్ధి చేయడం', 'Separate liquids / ద్రవాలను వేరుచేయడం', 'Detect elements / మూలకాలను గుర్తించడం', 'B', 'M', '', 33),
    ('The law of conservation of mass states\\nతెలుగు: ద్రవ్యరాశి సంరక్షణ నియమం ఏమి చెప్తుంది?', 'Mass increases in reactions / చర్యలో ద్రవ్యరాశి పెరుగుతుంది', 'Mass is neither created nor destroyed / ద్రవ్యరాశి సృష్టించబడదు లేదా నశించదు', 'Mass decreases in reactions / చర్యలో ద్రవ్యరాశి తగ్గుతుంది', 'Mass changes with temperature / ఉష్ణోగ్రతతో ద్రవ్యరాశి మారుతుంది', 'B', 'M', '', 34),
    ('Tyndall effect is shown by\\nతెలుగు: టిండాల్ ప్రభావం ఏ మిశ్రమంలో కనిపిస్తుంది?', 'True solutions / నిజమైన ద్రావణాలు', 'Colloids / కొల్లాయిడ్లు', 'Pure water / స్వచ్ఛమైన నీరు', 'Suspensions / నిలకడ మిశ్రమాలు', 'B', 'M', '', 35),
    ('Which of the following is a combination reaction?\\nతెలుగు: కింది వాటిలో సంయోజన చర్య ఏది?', 'CaCO3 → CaO + CO2', '2H2 + O2 → 2H2O', 'AB → A + B', 'A + BC → AC + B', 'B', 'M', '', 36),
    ('The industrial synthesis of ammonia uses\\nతెలుగు: పరిశ్రమలో అమోనియా సంశ్లేషణలో ఉపయోగించే ఉత్ప్రేరకం ఏమిటి?', 'Platinum / ప్లాటినం', 'Iron / ఇనుము', 'Nickel / నికెల్', 'Vanadium pentoxide / వెనాడియం పెంటాక్సైడ్', 'B', 'M', '', 37),
    ('Evaporation is a process where\\nతెలుగు: బాష్పీభవనం అంటే ఏమిటి?', 'Solid turns to liquid / ఘనం ద్రవంగా మారుతుంది', 'Liquid turns to gas at the surface / ఉపరితలంలో ద్రవం వాయువుగా మారుతుంది', 'Gas turns to liquid / వాయువు ద్రవంగా మారుతుంది', 'Solid turns to gas / ఘనం వాయువుగా మారుతుంది', 'B', 'M', '', 38),
    ('Hydrolysis means decomposition by\\nతెలుగు: జల విఘటనం అంటే ఏ శక్తి ద్వారా విఘటనం?', 'Electricity / విద్యుత్', 'Heat / వేడి', 'Water / నీరు', 'Light / వెలుతురు', 'C', 'M', '', 39),
    ('The process of heating ore in limited air to remove volatile impurities is\\nతెలుగు: తక్కువ గాలిలో ఖనిజాన్ని వేడిచేసి మలినాలు తొలగించే ప్రక్రియ ఏది?', 'Smelting / స్మెల్టింగ్', 'Calcination / కాల్సినేషన్', 'Roasting / రోస్టింగ్', 'Leaching / లీచింగ్', 'B', 'M', '', 40),
    ('Chemical equilibrium is a state where\\nతెలుగు: రసాయన సమతాస్థితి అంటే ఏమిటి?', 'Reaction stops completely / చర్య పూర్తిగా ఆగిపోతుంది', 'Forward and reverse rates are equal / ముందు మరియు వెనుక రేట్లు సమానంగా ఉంటాయి', 'Only reactants remain / ప్రతిక్రియకాలు మాత్రమే మిగులుతాయి', 'Only products remain / ఉత్పత్తులు మాత్రమే మిగులుతాయి', 'B', 'M', '', 41),
    ('Soap works as a cleanser because of its\\nతెలుగు: సబ్బు శుభ్రపరిచే గుణం దేని వల్ల కలుగుతుంది?', 'Alkaline nature / క్షార స్వభావం', 'Emulsification property / ఎమల్సిఫికేషన్ గుణం', 'Acidic nature / ఆమ్ల స్వభావం', 'High melting point / అధిక ద్రవీభవన స్థానం', 'B', 'M', '', 42),
    ('Smelting is used to extract metals from their\\nతెలుగు: స్మెల్టింగ్ పద్ధతి ద్వారా ఏమి నుండి లోహాలు వెలికితీస్తారు?', 'Alloys / మిశ్రమ లోహాలు', 'Ores / ఖనిజాలు', 'Solutions / ద్రావణాలు', 'Atmosphere / వాతావరణం', 'B', 'M', '', 43),
    ('A substance that slows down a chemical reaction is called\\nతెలుగు: రసాయన చర్యను నెమ్మదింపజేసే పదార్థాన్ని ఏమంటారు?', 'Catalyst / ఉత్ప్రేరకం', 'Inhibitor / నిరోధకం', 'Activator / సక్రియ పదార్థం', 'Promoter / ప్రమోటర్', 'B', 'M', '', 44),
    ('Combustion always requires\\nతెలుగు: దహనానికి ఎల్లప్పుడూ ఏమి కావాలి?', 'Water / నీరు', 'Oxygen / ఆక్సిజన్', 'Nitrogen / నైట్రోజన్', 'Carbon dioxide / కార్బన్ డైయాక్సైడ్', 'B', 'M', '', 45),
    ('Alloys are formed by\\nతెలుగు: మిశ్రమ లోహాలు ఎలా ఏర్పడతాయి?', 'Physical mixing of metals / లోహాల భౌతిక మిశ్రమం', 'Chemical reaction of metals / లోహాల రసాయన చర్య', 'Electrolysis of metals / లోహాల విద్యుత్ విఘటనం', 'Heating metals with acid / లోహాలను ఆమ్లంతో వేడిచేయడం', 'A', 'M', '', 46),
    ('The law of definite proportions was proposed by\\nతెలుగు: నిర్దిష్ట నిష్పత్తుల నియమాన్ని ఎవరు ప్రతిపాదించారు?', 'Dalton / డాల్టన్', 'Proust / ప్రౌస్ట్', 'Avogadro / అవగాడ్రో', 'Gay-Lussac / గే-లుస్సాక్', 'B', 'M', '', 47),
    ('Fractional distillation separates\\nతెలుగు: భాగిక స్వేదనం దేనిని వేరుచేస్తుంది?', 'Solids from liquids / ఘన పదార్థాల నుండి ద్రవాలు', 'Miscible liquids with different boiling points / వేర్వేరు మరుగు స్థానాలు కలిగిన కలుపుగుణం ద్రవాలు', 'Insoluble solids from liquids / అద్రావణ ఘనాల నుండి ద్రవాలు', 'Gases from liquids / వాయువులను ద్రవాల నుండి', 'B', 'M', '', 48),
    ('Activation energy is the\\nతెలుగు: సక్రియణ శక్తి అంటే ఏమిటి?', 'Energy released in reaction / చర్యలో విడుదలయ్యే శక్తి', 'Minimum energy needed to start reaction / చర్య ప్రారంభించడానికి కావలసిన కనిష్ట శక్తి', 'Energy stored in bonds / బంధాలలో నిల్వ ఉన్న శక్తి', 'Energy of catalyst / ఉత్ప్రేరకం యొక్క శక్తి', 'B', 'M', '', 49),
    ('Weathering of rocks is a\\nతెలుగు: శిలల వాతావరణ క్రియ ఏ రకమైన మార్పు?', 'Physical change / భౌతిక మార్పు', 'Chemical change / రసాయన మార్పు', 'Both physical and chemical / భౌతిక మరియు రసాయన రెండూ', 'Nuclear change / అణు మార్పు', 'C', 'M', '', 50),
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