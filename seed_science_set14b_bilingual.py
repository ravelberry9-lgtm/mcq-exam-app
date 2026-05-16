import sqlite3, os

SOURCE = 'Science_Set14B_Living_Organisms_Ext'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    ('Who is called the father of cell biology?\\nతెలుగు: సెల్ బయాలజీ పితామహుడు అని పిలువబడేవారు ఎవరు?', 'Robert Hooke / రాబర్ట్ హుక్', 'Louis Pasteur / లూయీ పాశ్చర్', 'Charles Darwin / చార్లెస్ డార్విన్', 'Gregor Mendel / గ్రెగర్ మెండెల్', 'A', 'M', '', 1),
    ('What is the powerhouse of the cell?\\nతెలుగు: కణం యొక్క విద్యుత్ కేంద్రం ఏది?', 'Mitochondria / మైటోకాండ్రియా', 'Nucleus / కేంద్రకం', 'Ribosome / రైబోజోమ్', 'Chloroplast / క్లోరోప్లాస్ట్', 'A', 'M', '', 2),
    ('Which organelle is responsible for protein synthesis?\\nతెలుగు: ప్రోటీన్ సంశ్లేషణకు బాధ్యత వహించే అంగాంశం ఏది?', 'Ribosome / రైబోజోమ్', 'Mitochondria / మైటోకాండ్రియా', 'Golgi apparatus / గాల్జీ పరికరం', 'Lysosome / లైసోజోమ్', 'A', 'M', '', 3),
    ('What is the fluid-filled space inside a cell called?\\nతెలుగు: కణంలో ద్రవంతో నిండిన స్థలాన్ని ఏమంటారు?', 'Cytoplasm / సైటోప్లాజమ్', 'Nucleoplasm / న్యూక్లియోప్లాజమ్', 'Vacuole / వాక్యువోల్', 'Cell sap / కణ రసం', 'A', 'M', '', 4),
    ('Which cell organelle is called the suicidal bag?\\nతెలుగు: ఆత్మహత్య సంచి అని పిలువబడే కణ అంగాంశం ఏది?', 'Lysosome / లైసోజోమ్', 'Ribosome / రైబోజోమ్', 'Mitochondria / మైటోకాండ్రియా', 'Peroxisome / పెరాక్సిజోమ్', 'A', 'M', '', 5),
    ('DNA is found mainly in which part of the cell?\\nతెలుగు: DNA కణంలో ప్రధానంగా ఏ భాగంలో ఉంటుంది?', 'Nucleus / కేంద్రకం', 'Cytoplasm / సైటోప్లాజమ్', 'Cell membrane / కణ పొర', 'Ribosome / రైబోజోమ్', 'A', 'M', '', 6),
    ('Which process produces energy in the mitochondria?\\nతెలుగు: మైటోకాండ్రియాలో శక్తి ఉత్పత్తి చేసే ప్రక్రియ ఏది?', 'Cellular respiration / కణ శ్వాసక్రియ', 'Photosynthesis / కిరణజన్య సంయోగం', 'Fermentation / పులియబెట్టడం', 'Glycolysis only / కేవలం గ్లైకోలైసిస్', 'A', 'M', '', 7),
    ('The cell membrane is made of?\\nతెలుగు: కణ పొర దేనితో తయారవుతుంది?', 'Phospholipid bilayer / ఫాస్ఫోలిపిడ్ ద్విపొర', 'Cellulose / సెల్యులోజ్', 'Protein only / కేవలం ప్రోటీన్', 'Chitin / చిటిన్', 'A', 'M', '', 8),
    ('What is the difference between plant and animal cells?\\nతెలుగు: మొక్క మరియు జంతు కణాల మధ్య తేడా ఏమిటి?', 'Plant cells have cell wall and chloroplasts / మొక్క కణాలకు కణ గోడ మరియు క్లోరోప్లాస్ట్లు ఉంటాయి', 'Animal cells have cell wall / జంతు కణాలకు కణ గోడ ఉంటుంది', 'Plant cells have no nucleus / మొక్క కణాలకు కేంద్రకం లేదు', 'Animal cells are larger / జంతు కణాలు పెద్దవి', 'A', 'M', '', 9),
    ('Cell division by which new cells have same chromosome number as parent?\\nతెలుగు: ఏ కణ విభజనలో కొత్త కణాలకు తల్లి కణమంత క్రోమోజోమ్ సంఖ్య ఉంటుంది?', 'Mitosis / మైటోసిస్', 'Meiosis / మెయోసిస్', 'Binary fission / ద్విభాజనం', 'Budding / మొగ్గ వేయడం', 'A', 'M', '', 10),
    ('Who is called the father of genetics?\\nతెలుగు: జెనెటిక్స్ పితామహుడు అని పిలువబడేవారు ఎవరు?', 'Gregor Mendel / గ్రెగర్ మెండెల్', 'Charles Darwin / చార్లెస్ డార్విన్', 'Robert Hooke / రాబర్ట్ హుక్', 'Louis Pasteur / లూయీ పాశ్చర్', 'A', 'M', '', 11),
    ('What is DNA full form?\\nతెలుగు: DNA పూర్తి పేరు ఏమిటి?', 'Deoxyribonucleic Acid / డీఆక్సీరైబోన్యూక్లిక్ యాసిడ్', 'Deoxyribose Nucleotide Acid / డీఆక్సీరైబోజ్ న్యూక్లియోటైడ్ యాసిడ్', 'Double Nucleic Acid / డబుల్ న్యూక్లియిక్ యాసిడ్', 'Denatured Amino Acid / డెనేచర్డ్ అమినో యాసిడ్', 'A', 'M', '', 12),
    ('How many chromosomes does a human body cell have?\\nతెలుగు: మానవ శరీర కణంలో ఎన్ని క్రోమోజోమ్లు ఉంటాయి?', '46 / 46', '23 / 23', '48 / 48', '44 / 44', 'A', 'M', '', 13),
    ('What are alleles?\\nతెలుగు: ఆలీల్స్ అంటే ఏమిటి?', 'Alternate forms of a gene / ఒక జన్యువు యొక్క ప్రత్యామ్నాయ రూపాలు', 'Different chromosomes / వేర్వేరు క్రోమోజోమ్లు', 'DNA segments / DNA సెగ్మెంట్లు', 'Protein variants / ప్రోటీన్ రూపాంతరాలు', 'A', 'M', '', 14),
    ('What is the genotype?\\nతెలుగు: జీనోటైప్ అంటే ఏమిటి?', 'Genetic makeup of an organism / జీవి యొక్క జన్యు నిర్మాణం', 'Physical appearance / శారీరక రూపం', 'Chromosome number / క్రోమోజోమ్ సంఖ్య', 'Protein composition / ప్రోటీన్ కూర్పు', 'A', 'M', '', 15),
    ('What is the phenotype?\\nతెలుగు: ఫినోటైప్ అంటే ఏమిటి?', 'Observable characteristics / గమనించదగిన లక్షణాలు', 'Genetic composition / జన్యు కూర్పు', 'DNA sequence / DNA క్రమం', 'Mutation type / మ్యుటేషన్ రకం', 'A', 'M', '', 16),
    ('Mendel\'s law of segregation states?\\nతెలుగు: మెండెల్ వేర్పాటు నియమం ఏమి చెప్తుంది?', 'Two alleles separate during gamete formation / గేమీట్ ఏర్పాటు సమయంలో రెండు ఆలీల్స్ వేరవుతాయి', 'Genes are linked together / జన్యువులు కలిసి ఉంటాయి', 'All traits are dominant / అన్ని లక్షణాలు ప్రబలంగా ఉంటాయి', 'Mutations occur randomly / మ్యుటేషన్లు యాదృచ్ఛికంగా జరుగుతాయి', 'A', 'M', '', 17),
    ('A mutation is?\\nతెలుగు: మ్యుటేషన్ అంటే ఏమిటి?', 'A change in DNA sequence / DNA క్రమంలో మార్పు', 'Normal cell division / సాధారణ కణ విభజన', 'Protein synthesis / ప్రోటీన్ సంశ్లేషణ', 'Gene expression / జన్యు వ్యక్తీకరణ', 'A', 'M', '', 18),
    ('Sex chromosomes in human females are?\\nతెలుగు: మానవ స్త్రీలలో లింగ క్రోమోజోమ్లు ఏవి?', 'XX / XX', 'XY / XY', 'YY / YY', 'XO / XO', 'A', 'M', '', 19),
    ('DNA double helix was discovered by?\\nతెలుగు: DNA డబుల్ హెలిక్స్ ఎవరిచే కనుగొనబడింది?', 'Watson and Crick / వాట్సన్ మరియు క్రిక్', 'Mendel and Darwin / మెండెల్ మరియు డార్విన్', 'Hooke and Brown / హుక్ మరియు బ్రౌన్', 'Pasteur and Koch / పాశ్చర్ మరియు కాక్', 'A', 'M', '', 20),
    ('What is the binomial nomenclature?\\nతెలుగు: ద్వినామ నామకరణం అంటే ఏమిటి?', 'Two-part scientific naming system / రెండు-భాగాల శాస్త్రీయ నామకరణ వ్యవస్థ', 'Classification of animals / జంతువుల వర్గీకరణ', 'Study of genes / జన్యువుల అధ్యయనం', 'Taxonomy ranking / వర్గీకరణ శ్రేణీకరణ', 'A', 'M', '', 21),
    ('Who developed the system of binomial nomenclature?\\nతెలుగు: ద్వినామ నామకరణ వ్యవస్థను ఎవరు అభివృద్ధి చేశారు?', 'Carl Linnaeus / కార్ల్ లిన్నేయస్', 'Gregor Mendel / గ్రెగర్ మెండెల్', 'Charles Darwin / చార్లెస్ డార్విన్', 'Robert Hooke / రాబర్ట్ హుక్', 'A', 'M', '', 22),
    ('What is the correct order of biological classification?\\nతెలుగు: జీవ వర్గీకరణ యొక్క సరైన క్రమం ఏమిటి?', 'Kingdom→Phylum→Class→Order→Family→Genus→Species', 'Kingdom→Class→Order→Phylum→Family→Genus→Species', 'Species→Genus→Family→Order→Class→Phylum→Kingdom', 'Phylum→Kingdom→Class→Order→Family→Genus→Species', 'A', 'M', '', 23),
    ('Prokaryotic cells lack?\\nతెలుగు: ప్రోకార్యోటిక్ కణాలకు ఏది లేదు?', 'Membrane-bound nucleus / పొర-బద్ధ కేంద్రకం', 'Cell wall / కణ గోడ', 'Ribosomes / రైబోజోమ్లు', 'DNA / DNA', 'A', 'M', '', 24),
    ('Viruses are classified as?\\nతెలుగు: వైరస్‌లను ఏమిగా వర్గీకరిస్తారు?', 'Non-living outside host, living inside / హోస్ట్ వెలుపల నిర్జీవి, లోపల జీవి', 'Always living / ఎప్పుడూ జీవి', 'Always non-living / ఎప్పుడూ నిర్జీవి', 'A type of bacteria / ఒక రకమైన బాక్టీరియా', 'A', 'M', '', 25),
    ('Which kingdom includes fungi?\\nతెలుగు: ఫంగైని ఏ రాజ్యంలో చేర్చారు?', 'Fungi / ఫంగి', 'Protista / ప్రోటిస్టా', 'Monera / మోనెరా', 'Plantae / ప్లాంటే', 'A', 'M', '', 26),
    ('Which is the largest kingdom?\\nతెలుగు: అతిపెద్ద రాజ్యం ఏది?', 'Animalia / అనిమాలియా', 'Plantae / ప్లాంటే', 'Fungi / ఫంగి', 'Protista / ప్రోటిస్టా', 'A', 'M', '', 27),
    ('The scientific name of humans is?\\nతెలుగు: మానవుల శాస్త్రీయ నామం ఏమిటి?', 'Homo sapiens / హోమో సేపియన్స్', 'Homo erectus / హోమో ఎరెక్టస్', 'Pan troglodytes / పాన్ ట్రాగ్లోడైట్స్', 'Homo habilis / హోమో హాబిలిస్', 'A', 'M', '', 28),
    ('Meiosis results in cells with how many chromosomes?\\nతెలుగు: మెయోసిస్ ఫలితంగా ఎన్ని క్రోమోజోమ్లు ఉన్న కణాలు వస్తాయి?', 'Half the original number (haploid) / అసలు సంఖ్యలో సగం (హాప్లాయిడ్)', 'Same number (diploid) / అదే సంఖ్య (డిప్లాయిడ్)', 'Double the number / రెండింతలు', 'No chromosomes / క్రోమోజోమ్లు లేవు', 'A', 'M', '', 29),
    ('What are stem cells?\\nతెలుగు: స్టెమ్ కణాలు అంటే ఏమిటి?', 'Undifferentiated cells that can become any cell type / ఏ కణ రకంలోనైనా మారగల అభేదీకృత కణాలు', 'Brain cells / మెదడు కణాలు', 'Muscle cells / కండర కణాలు', 'Blood cells / రక్త కణాలు', 'A', 'M', '', 30),
    ('Which base pairs with Adenine in DNA?\\nతెలుగు: DNA లో అడెనైన్‌తో జతకూడే బేస్ ఏది?', 'Thymine / థైమిన్', 'Guanine / గ్వానైన్', 'Cytosine / సైటోసిన్', 'Uracil / యురాసిల్', 'A', 'M', '', 31),
    ('Sickle cell anemia is an example of?\\nతెలుగు: సికిల్ సెల్ అనీమియా ఏ రకానికి ఉదాహరణ?', 'Genetic disorder / జన్యు రుగ్మత', 'Bacterial infection / బాక్టీరియా సంక్రమణ', 'Viral disease / వైరల్ వ్యాధి', 'Nutritional deficiency / పోషకాహార లోపం', 'A', 'M', '', 32),
    ('Which type of RNA carries genetic info from DNA to ribosome?\\nతెలుగు: DNA నుండి రైబోజోమ్‌కు జన్యు సమాచారాన్ని తీసుకువెళ్ళే RNA రకం ఏది?', 'mRNA (messenger RNA) / mRNA (మెసెంజర్ RNA)', 'tRNA (transfer RNA) / tRNA (ట్రాన్స్‌ఫర్ RNA)', 'rRNA (ribosomal RNA) / rRNA (రైబోజోమల్ RNA)', 'snRNA / snRNA', 'A', 'M', '', 33),
    ('Down syndrome is caused by?\\nతెలుగు: డౌన్ సిండ్రోమ్ దేని వల్ల వస్తుంది?', 'Extra chromosome 21 / అదనపు క్రోమోజోమ్ 21', 'Missing chromosome / తప్పిపోయిన క్రోమోజోమ్', 'Viral infection / వైరల్ సంక్రమణ', 'Nutritional deficiency / పోషకాహార లోపం', 'A', 'M', '', 34),
    ('The endoplasmic reticulum functions in?\\nతెలుగు: ఎండోప్లాస్మిక్ రెటిక్యులమ్ ఏ పనిలో పాల్గొంటుంది?', 'Protein and lipid synthesis and transport / ప్రోటీన్ మరియు లిపిడ్ సంశ్లేషణ మరియు రవాణా', 'Energy production / శక్తి ఉత్పత్తి', 'Cell division / కణ విభజన', 'DNA replication / DNA ప్రతిరూపణ', 'A', 'M', '', 35),
    ('Bacteria belong to which kingdom?\\nతెలుగు: బాక్టీరియా ఏ రాజ్యానికి చెందుతాయి?', 'Monera / మోనెరా', 'Protista / ప్రోటిస్టా', 'Fungi / ఫంగి', 'Animalia / అనిమాలియా', 'A', 'M', '', 36),
    ('What is the function of the Golgi apparatus?\\nతెలుగు: గాల్జీ పరికరం యొక్క పని ఏమిటి?', 'Packages and ships proteins / ప్రోటీన్లను ప్యాక్ చేసి పంపిస్తుంది', 'Produces energy / శక్తి ఉత్పత్తి చేస్తుంది', 'Digests waste / వ్యర్థాలను జీర్ణిస్తుంది', 'Synthesizes DNA / DNA సంశ్లేషిస్తుంది', 'A', 'M', '', 37),
    ('Inheritance of blood groups follows which law?\\nతెలుగు: రక్త సమూహాల వారసత్వం ఏ నియమాన్ని అనుసరిస్తుంది?', 'Mendelian genetics with codominance / కోడామినెన్స్‌తో మెండెలియన్ జెనెటిక్స్', 'Only dominant traits / కేవలం ప్రబల లక్షణాలు', 'Random inheritance / యాదృచ్ఛిక వారసత్వం', 'No genetic basis / జన్యు ఆధారం లేదు', 'A', 'M', '', 38),
    ('Which organelle has its own DNA?\\nతెలుగు: తమ స్వంత DNA ఉన్న అంగాంశం ఏది?', 'Mitochondria / మైటోకాండ్రియా', 'Ribosome / రైబోజోమ్', 'Lysosome / లైసోజోమ్', 'Golgi body / గాల్జీ బాడీ', 'A', 'M', '', 39),
    ('What is cloning?\\nతెలుగు: క్లోనింగ్ అంటే ఏమిటి?', 'Creating genetically identical organisms / జన్యుపరంగా సమానమైన జీవులను సృష్టించడం', 'Modifying DNA / DNA మార్చడం', 'Selective breeding / ఎంపిక సంయోగం', 'Gene therapy / జన్యు చికిత్స', 'A', 'M', '', 40),
    ('Which kingdom does Amoeba belong to?\\nతెలుగు: అమీబా ఏ రాజ్యానికి చెందుతుంది?', 'Protista / ప్రోటిస్టా', 'Monera / మోనెరా', 'Fungi / ఫంగి', 'Animalia / అనిమాలియా', 'A', 'M', '', 41),
    ('The process of making RNA from DNA is called?\\nతెలుగు: DNA నుండి RNA తయారు చేసే ప్రక్రియ ఏమిటి?', 'Transcription / ట్రాన్స్‌క్రిప్షన్', 'Translation / అనువాదం', 'Replication / ప్రతిరూపణ', 'Mutation / మ్యుటేషన్', 'A', 'M', '', 42),
    ('Which phylum do insects belong to?\\nతెలుగు: కీటకాలు ఏ ఫైలమ్‌కు చెందుతాయి?', 'Arthropoda / ఆర్థ్రోపోడా', 'Chordata / కోర్డేటా', 'Mollusca / మొల్యూస్కా', 'Annelida / యానెలిడా', 'A', 'M', '', 43),
    ('What is the role of tRNA in protein synthesis?\\nతెలుగు: ప్రోటీన్ సంశ్లేషణలో tRNA పాత్ర ఏమిటి?', 'Brings amino acids to ribosome / అమినో ఆసిడ్లను రైబోజోమ్‌కు తీసుకొస్తుంది', 'Carries genetic code / జన్యు సంకేతాన్ని మోస్తుంది', 'Makes up ribosome structure / రైబోజోమ్ నిర్మాణం చేస్తుంది', 'Copies DNA / DNA ని కాపీ చేస్తుంది', 'A', 'M', '', 44),
    ('Plasmids are found in?\\nతెలుగు: ప్లాస్మిడ్లు ఎక్కడ కనుగొనబడతాయి?', 'Bacteria / బాక్టీరియా', 'Human cells / మానవ కణాలు', 'Plant cells / మొక్క కణాలు', 'Animal cells / జంతు కణాలు', 'A', 'M', '', 45),
    ('In genetics, dominant allele is represented by?\\nతెలుగు: జెనెటిక్స్‌లో ప్రబల ఆలీల్ దేనిచే సూచించబడుతుంది?', 'Capital letter / పెద్ద అక్షరం', 'Small letter / చిన్న అక్షరం', 'Number / సంఖ్య', 'Symbol / చిహ్నం', 'A', 'M', '', 46),
    ('What does PCR stand for in molecular biology?\\nతెలుగు: మాలిక్యులర్ బయాలజీలో PCR అంటే ఏమిటి?', 'Polymerase Chain Reaction / పాలిమరేజ్ చెయిన్ రియాక్షన్', 'Protein Coding Region / ప్రోటీన్ కోడింగ్ ప్రాంతం', 'Plasma Cell Response / ప్లాస్మా సెల్ రెస్పాన్స్', 'Phenotype Control Ratio / ఫినోటైప్ నియంత్రణ నిష్పత్తి', 'A', 'M', '', 47),
    ('Which kingdom includes mushrooms?\\nతెలుగు: పుట్టగొడుగులను ఏ రాజ్యంలో చేర్చారు?', 'Fungi / ఫంగి', 'Plantae / ప్లాంటే', 'Protista / ప్రోటిస్టా', 'Monera / మోనెరా', 'A', 'M', '', 48),
    ('Genetic engineering involves?\\nతెలుగు: జన్యు ఇంజినీరింగ్ దేన్ని కలిగి ఉంటుంది?', 'Direct manipulation of DNA / DNA యొక్క ప్రత్యక్ష మార్పిడి', 'Selective breeding only / కేవలం ఎంపిక సంయోగం', 'Vaccination / వ్యాక్సినేషన్', 'Cell division study / కణ విభజన అధ్యయనం', 'A', 'M', '', 49),
    ('What are chromosomes made of?\\nతెలుగు: క్రోమోజోమ్లు దేనితో తయారవుతాయి?', 'DNA and proteins / DNA మరియు ప్రోటీన్లు', 'RNA only / కేవలం RNA', 'Lipids / లిపిడ్లు', 'Carbohydrates / కార్బోహైడ్రేట్లు', 'A', 'M', '', 50),
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