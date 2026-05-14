import sqlite3, os

SOURCE = 'Science_Set4B_Atoms_Radioactivity_Nuclear_Ext'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    ('Who proposed the atomic theory?\\nతెలుగు: పరమాణు సిద్ధాంతాన్ని ఎవరు ప్రతిపాదించారు?', 'Thomson / థామ్సన్', 'Dalton / డాల్టన్', 'Bohr / బోర్', 'Rutherford / రదర్‌ఫర్డ్', 'B', 'M', '', 1),
    ('Which particle has no charge?\\nతెలుగు: ఏ కణానికి విద్యుత్ భారం ఉండదు?', 'Proton / ప్రోటాన్', 'Electron / ఎలక్ట్రాన్', 'Neutron / న్యూట్రాన్', 'Positron / పాజిట్రాన్', 'C', 'M', '', 2),
    ('Alpha particles are identical to\\nతెలుగు: ఆల్ఫా కణాలు దేనితో సమానంగా ఉంటాయి?', 'Hydrogen nucleus / హైడ్రోజన్ కేంద్రకం', 'Helium nucleus / హీలియం కేంద్రకం', 'Electron / ఎలక్ట్రాన్', 'Neutron / న్యూట్రాన్', 'B', 'M', '', 3),
    ('Which radiation has the highest penetrating power?\\nతెలుగు: అత్యంత ఎక్కువ చొచ్చుకుపోయే శక్తి కలిగిన వికిరణం ఏది?', 'Alpha / ఆల్ఫా', 'Beta / బీటా', 'Gamma / గామా', 'X-ray / ఎక్స్-కిరణాలు', 'C', 'M', '', 4),
    ('Nuclear fission means\\nతెలుగు: న్యూక్లియర్ ఫిషన్ అంటే ఏమిటి?', 'Two nuclei joining / రెండు కేంద్రకాలు కలవడం', 'One nucleus splitting / ఒక కేంద్రకం విడిపోవడం', 'Electron emission / ఎలక్ట్రాన్ వెలువడటం', 'Neutron absorption / న్యూట్రాన్ శోషణ', 'B', 'M', '', 5),
    ('The first controlled nuclear fission was achieved by\\nతెలుగు: మొట్టమొదటి నియంత్రిత అణు విభజన ఎవరు సాధించారు?', 'Fermi / ఫెర్మి', 'Bohr / బోర్', 'Einstein / ఐన్‌స్టీన్', 'Hahn / హాన్', 'A', 'M', '', 6),
    ('The unit of radioactivity is\\nతెలుగు: రేడియోధార్మికత యొక్క ప్రమాణం ఏమిటి?', 'Decibel / డెసిబెల్', 'Curie / క్యూరీ', 'Joule / జూల్', 'Tesla / టెస్లా', 'B', 'M', '', 7),
    ('Carbon-14 dating is used to\\nతెలుగు: కార్బన్-14 పద్ధతి దేనికి ఉపయోగిస్తారు?', 'Find element composition / మూలక కూర్పు కనుగొనడానికి', 'Determine age of fossils / శిలాజాల వయస్సు నిర్ణయించడానికి', 'Measure temperature / ఉష్ణోగ్రత కొలవడానికి', 'Identify metals / లోహాలను గుర్తించడానికి', 'B', 'M', '', 8),
    ('The nucleus of an atom consists of\\nతెలుగు: పరమాణు కేంద్రకంలో ఉండేవి ఏవి?', 'Protons only / ప్రోటాన్లు మాత్రమే', 'Protons and neutrons / ప్రోటాన్లు మరియు న్యూట్రాన్లు', 'Electrons and neutrons / ఎలక్ట్రాన్లు మరియు న్యూట్రాన్లు', 'All three / మూడూ', 'B', 'M', '', 9),
    ('The half-life of a radioactive element is the time taken for\\nతెలుగు: రేడియోధార్మిక మూలకం అర్ధ జీవితకాలం అంటే ఏమిటి?', 'All atoms to decay / అన్ని పరమాణువులు క్షయించడం', 'Half the atoms to decay / సగం పరమాణువులు క్షయించడం', 'Quarter atoms to decay / పాతికభాగం క్షయించడం', 'One atom to decay / ఒక పరమాణువు క్షయించడం', 'B', 'M', '', 10),
    ('Nuclear fusion occurs in\\nతెలుగు: న్యూక్లియర్ ఫ్యూజన్ ఎక్కడ జరుగుతుంది?', 'Nuclear power plants / అణు విద్యుత్ కేంద్రాలు', 'The Sun / సూర్యుడు', 'X-ray machines / ఎక్స్-రే యంత్రాలు', 'CT scanners / CT స్కానర్లు', 'B', 'M', '', 11),
    ('The charge of a beta particle is\\nతెలుగు: బీటా కణం యొక్క విద్యుత్ భారం ఏమిటి?', 'Zero / శూన్యం', '+1 / +1', '-1 / -1', '+2 / +2', 'C', 'M', '', 12),
    ('Uranium is used as fuel in nuclear reactors because it\\nతెలుగు: అణు రియాక్టర్లలో యురేనియం ఇంధనంగా ఉపయోగిస్తారు, ఎందుకంటే?', 'Is cheap / చౌకగా ఉంటుంది', 'Undergoes fission / విభజన చెందుతుంది', 'Is a good conductor / మంచి వాహకం', 'Reacts with water / నీటితో చర్య జరుపుతుంది', 'B', 'M', '', 13),
    ('Radioactivity was discovered by\\nతెలుగు: రేడియోధార్మికతను ఎవరు కనుగొన్నారు?', 'Marie Curie / మేరీ క్యూరీ', 'Henri Becquerel / హెన్రీ బెక్వెరెల్', 'Rutherford / రదర్‌ఫర్డ్', 'Fermi / ఫెర్మి', 'B', 'M', '', 14),
    ('The number of protons in an atom is called its\\nతెలుగు: పరమాణువులో ప్రోటాన్ల సంఖ్యను ఏమంటారు?', 'Mass number / ద్రవ్యరాశి సంఖ్య', 'Atomic number / పరమాణు సంఖ్య', 'Neutron number / న్యూట్రాన్ సంఖ్య', 'Valency / సంయోజకత', 'B', 'M', '', 15),
    ('The moderator used in nuclear reactors is\\nతెలుగు: అణు రియాక్టర్లలో మాడరేటర్‌గా ఉపయోగించేది ఏది?', 'Heavy water / హెవీ వాటర్', 'Normal water / సాధారణ నీరు', 'Graphite / గ్రాఫైట్', 'Both A and C / A మరియు C రెండూ', 'D', 'M', '', 16),
    ('Which radiation cannot be deflected by magnetic field?\\nతెలుగు: అయస్కాంత క్షేత్రం ద్వారా వంగని వికిరణం ఏది?', 'Alpha / ఆల్ఫా', 'Beta / బీటా', 'Gamma / గామా', 'All are deflected / అన్నీ వంగుతాయి', 'C', 'M', '', 17),
    ('The atomic model with orbits was proposed by\\nతెలుగు: కక్ష్యలతో కూడిన పరమాణు నమూనాను ఎవరు ప్రతిపాదించారు?', 'Dalton / డాల్టన్', 'Thomson / థామ్సన్', 'Rutherford / రదర్‌ఫర్డ్', 'Bohr / బోర్', 'D', 'M', '', 18),
    ('The process in which a nucleus emits an alpha particle is called\\nతెలుగు: కేంద్రకం ఆల్ఫా కణాన్ని వెలువరించే ప్రక్రియను ఏమంటారు?', 'Beta decay / బీటా క్షయం', 'Alpha decay / ఆల్ఫా క్షయం', 'Gamma emission / గామా వెలువడటం', 'Fission / విభజన', 'B', 'M', '', 19),
    ('The energy released in nuclear reactions is explained by\\nతెలుగు: అణు చర్యలలో విడుదలయ్యే శక్తిని వివరించే నియమం ఏమిటి?', 'Newton\'s law / న్యూటన్ నియమం', 'Einstein\'s E=mc2 / ఐన్‌స్టీన్ E=mc2', 'Boyle\'s law / బాయిల్ నియమం', 'Ohm\'s law / ఓమ్ నియమం', 'B', 'M', '', 20),
    ('Isobars have the same\\nతెలుగు: ఐసోబార్‌లకు ఏది సమానంగా ఉంటుంది?', 'Atomic number / పరమాణు సంఖ్య', 'Number of neutrons / న్యూట్రాన్ల సంఖ్య', 'Mass number / ద్రవ్యరాశి సంఖ్య', 'Number of electrons / ఎలక్ట్రాన్ల సంఖ్య', 'C', 'M', '', 21),
    ('Nuclear power in India is regulated by\\nతెలుగు: భారతదేశంలో అణు శక్తిని నియంత్రించే సంస్థ ఏది?', 'ISRO / ఇస్రో', 'BARC / బార్క్', 'DRDO / DRDO', 'CSIR / CSIR', 'B', 'M', '', 22),
    ('Alpha radiation can be stopped by\\nతెలుగు: ఆల్ఫా వికిరణాన్ని ఆపగలిగేది ఏది?', 'A thick lead sheet / మందమైన సీసపు రేకు', 'A few centimetres of air / కొన్ని సెంటీమీటర్ల గాలి', 'A thin sheet of paper / పాత్మైన కాగితం', 'Concrete wall / కాంక్రీట్ గోడ', 'C', 'M', '', 23),
    ('The splitting of one heavy nucleus into smaller ones is\\nతెలుగు: ఒక భారమైన కేంద్రకం చిన్న కేంద్రకాలుగా విడిపోవడాన్ని ఏమంటారు?', 'Fusion / సంలయం', 'Fission / విభజన', 'Decay / క్షయం', 'Transmutation / రూపాంతరం', 'B', 'M', '', 24),
    ('Gamma rays are\\nతెలుగు: గామా కిరణాలు ఏమిటి?', 'Charged particles / విద్యుత్ భారిత కణాలు', 'High energy electromagnetic waves / అధిక శక్తి విద్యుత్ అయస్కాంత తరంగాలు', 'Sound waves / శబ్ద తరంగాలు', 'Electrons / ఎలక్ట్రాన్లు', 'B', 'M', '', 25),
    ('The chain reaction in a nuclear bomb is\\nతెలుగు: అణు బాంబులో చైన్ రియాక్షన్ అంటే ఏమిటి?', 'Controlled / నియంత్రితం', 'Uncontrolled / అనియంత్రితం', 'Slow / నెమ్మదిగా', 'Stopped / ఆగిపోయిన', 'B', 'M', '', 26),
    ('X-rays were discovered by\\nతెలుగు: ఎక్స్-కిరణాలను ఎవరు కనుగొన్నారు?', 'Becquerel / బెక్వెరెల్', 'Curie / క్యూరీ', 'Roentgen / రాంట్‌జెన్', 'Thomson / థామ్సన్', 'C', 'M', '', 27),
    ('Radioactive decay is a\\nతెలుగు: రేడియోధార్మిక క్షయం ఏ రకమైన చర్య?', 'Physical change / భౌతిక మార్పు', 'Chemical change / రసాయన మార్పు', 'Nuclear change / అణు మార్పు', 'Biological change / జీవ మార్పు', 'C', 'M', '', 28),
    ('Isoelectronic species have the same number of\\nతెలుగు: ఐసో ఎలక్ట్రానిక్ జాతులకు ఏది సమానంగా ఉంటుంది?', 'Protons / ప్రోటాన్లు', 'Neutrons / న్యూట్రాన్లు', 'Electrons / ఎలక్ట్రాన్లు', 'Mass number / ద్రవ్యరాశి సంఖ్య', 'C', 'M', '', 29),
    ('The first element to be made artificially is\\nతెలుగు: కృత్రిమంగా తయారుచేసిన మొదటి మూలకం ఏది?', 'Plutonium / ప్లూటోనియం', 'Technetium / టెక్నీషియం', 'Americium / అమెరీషియం', 'Curium / క్యూరియం', 'B', 'M', '', 30),
    ('The number of electrons in a neutral atom equals\\nతెలుగు: తటస్థ పరమాణువులో ఎలక్ట్రాన్ల సంఖ్య దేనికి సమానం?', 'Neutrons / న్యూట్రాన్లు', 'Protons / ప్రోటాన్లు', 'Mass number / ద్రవ్యరాశి సంఖ్య', 'Valency / సంయోజకత', 'B', 'M', '', 31),
    ('The symbol for Uranium is\\nతెలుగు: యురేనియం యొక్క రసాయన చిహ్నం ఏమిటి?', 'Ur / Ur', 'Un / Un', 'U / U', 'Ua / Ua', 'C', 'M', '', 32),
    ('Which country first used an atomic bomb?\\nతెలుగు: అణు బాంబును మొదటగా ఉపయోగించిన దేశం ఏది?', 'Russia / రష్యా', 'UK / UK', 'USA / USA', 'Germany / జర్మనీ', 'C', 'M', '', 33),
    ('What is the atomic number of helium?\\nతెలుగు: హీలియం యొక్క పరమాణు సంఖ్య ఎంత?', '1 / 1', '2 / 2', '4 / 4', '8 / 8', 'B', 'M', '', 34),
    ('In Bohr\'s model electrons move in\\nతెలుగు: బోర్ నమూనాలో ఎలక్ట్రాన్లు ఎక్కడ కదులుతాయి?', 'Random paths / యాదృచ్ఛిక మార్గాల్లో', 'Fixed circular orbits / నిర్దిష్ట వర్తుల కక్ష్యల్లో', 'Elliptical orbits / దీర్ఘవృత్తాకార కక్ష్యల్లో', 'Straight lines / సరళ రేఖల్లో', 'B', 'M', '', 35),
    ('The radiation used in cancer treatment is\\nతెలుగు: క్యాన్సర్ చికిత్సలో ఉపయోగించే వికిరణం ఏది?', 'Alpha / ఆల్ఫా', 'Beta / బీటా', 'Gamma / గామా', 'X-rays / ఎక్స్ కిరణాలు', 'C', 'M', '', 36),
    ('Neutrons were discovered by\\nతెలుగు: న్యూట్రాన్‌లను ఎవరు కనుగొన్నారు?', 'Rutherford / రదర్‌ఫర్డ్', 'Thomson / థామ్సన్', 'Chadwick / చాడ్విక్', 'Bohr / బోర్', 'C', 'M', '', 37),
    ('The atomic mass unit (amu) is defined as\\nతెలుగు: పరమాణు ద్రవ్యరాశి యూనిట్ (amu) ఎలా నిర్వచిస్తారు?', '1/12 mass of C-12 / C-12 ద్రవ్యరాశిలో 1/12 వ వంతు', 'Mass of one proton / ఒక ప్రోటాన్ ద్రవ్యరాశి', 'Mass of one electron / ఒక ఎలక్ట్రాన్ ద్రవ్యరాశి', 'Mass of one neutron / ఒక న్యూట్రాన్ ద్రవ్యరాశి', 'A', 'M', '', 38),
    ('Nuclear energy is produced due to\\nతెలుగు: అణు శక్తి ఏ కారణంగా ఉత్పత్తి అవుతుంది?', 'Chemical reactions / రసాయన చర్యలు', 'Mass defect / ద్రవ్యరాశి లోటు', 'Electron transitions / ఎలక్ట్రాన్ మార్పులు', 'Heat energy / ఉష్ణ శక్తి', 'B', 'M', '', 39),
    ('Protons were discovered by\\nతెలుగు: ప్రోటాన్‌లను ఎవరు కనుగొన్నారు?', 'Rutherford / రదర్‌ఫర్డ్', 'Thomson / థామ్సన్', 'Chadwick / చాడ్విక్', 'Dalton / డాల్టన్', 'A', 'M', '', 40),
    ('The radioactive isotope used in thyroid treatment is\\nతెలుగు: థైరాయిడ్ చికిత్సలో ఉపయోగించే రేడియోధార్మిక ఐసోటోప్ ఏది?', 'Iodine-131 / అయోడిన్-131', 'Carbon-14 / కార్బన్-14', 'Uranium-235 / యురేనియం-235', 'Cobalt-60 / కోబాల్ట్-60', 'A', 'M', '', 41),
    ('Thomson\'s atomic model is called\\nతెలుగు: థామ్సన్ పరమాణు నమూనాను ఏమంటారు?', 'Plum pudding model / ప్లమ్ పుడ్డింగ్ నమూనా', 'Planetary model / గ్రహ నమూనా', 'Nuclear model / అణు నమూనా', 'Wave model / తరంగ నమూనా', 'A', 'M', '', 42),
    ('The process of combining two light nuclei to form a heavier nucleus is\\nతెలుగు: రెండు తేలికైన కేంద్రకాలు కలిసి భారమైన కేంద్రకం ఏర్పడే ప్రక్రియను ఏమంటారు?', 'Fission / విభజన', 'Fusion / సంలయం', 'Decay / క్షయం', 'Transmutation / రూపాంతరం', 'B', 'M', '', 43),
    ('The electrons discovered by Thomson were called\\nతెలుగు: థామ్సన్ కనుగొన్న ఎలక్ట్రాన్లు ముందు ఏమని పిలువబడ్డాయి?', 'Protons / ప్రోటాన్లు', 'Corpuscles / కార్పస్కిల్స్', 'Neutrons / న్యూట్రాన్లు', 'Photons / ఫోటాన్లు', 'B', 'M', '', 44),
    ('The mass of an electron is approximately\\nతెలుగు: ఒక ఎలక్ట్రాన్ ద్రవ్యరాశి సుమారు ఎంత?', 'Equal to proton / ప్రోటాన్ కు సమానం', '1/1836 of proton / ప్రోటాన్ కు 1/1836 వంతు', 'Twice of proton / ప్రోటాన్ కంటే రెట్టింపు', 'Half of proton / ప్రోటాన్ సగం', 'B', 'M', '', 45),
    ('Which isotope is used as fuel in nuclear power plants?\\nతెలుగు: అణు విద్యుత్ కేంద్రాలలో ఇంధనంగా ఉపయోగించే ఐసోటోప్ ఏది?', 'U-235 / U-235', 'U-238 / U-238', 'Pu-239 / Pu-239', 'Both A and C / A మరియు C రెండూ', 'D', 'M', '', 46),
    ('Electron was discovered by\\nతెలుగు: ఎలక్ట్రాన్‌ను ఎవరు కనుగొన్నారు?', 'Rutherford / రదర్‌ఫర్డ్', 'Thomson / థామ్సన్', 'Bohr / బోర్', 'Chadwick / చాడ్విక్', 'B', 'M', '', 47),
    ('The penetrating power of alpha particle compared to beta is\\nతెలుగు: బీటాతో పోలిస్తే ఆల్ఫా కణం చొచ్చుకుపోయే శక్తి ఎలా ఉంటుంది?', 'Higher / ఎక్కువ', 'Lower / తక్కువ', 'Same / సమానం', 'Depends on element / మూలకంపై ఆధారపడుతుంది', 'B', 'M', '', 48),
    ('Cosmic rays mainly consist of\\nతెలుగు: కాస్మిక్ కిరణాలు ప్రధానంగా ఏవి?', 'Gamma rays / గామా కిరణాలు', 'High energy protons / అధిక శక్తి ప్రోటాన్లు', 'Electrons / ఎలక్ట్రాన్లు', 'Neutrons / న్యూట్రాన్లు', 'B', 'M', '', 49),
    ('The minimum energy needed to remove an electron from an atom is\\nతెలుగు: పరమాణువు నుండి ఎలక్ట్రాన్‌ను తొలగించడానికి కావలసిన కనిష్ట శక్తిని ఏమంటారు?', 'Electron affinity / ఎలక్ట్రాన్ ఆకర్షణ', 'Ionization energy / అయనీకరణ శక్తి', 'Electronegativity / ఎలక్ట్రో ఋణాత్మకత', 'Bond energy / బంధ శక్తి', 'B', 'M', '', 50),
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