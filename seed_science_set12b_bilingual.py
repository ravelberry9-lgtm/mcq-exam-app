import sqlite3, os

SOURCE = 'Science_Set12B_Human_System3_Ext'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    ('What is the basic unit of the nervous system?\\nతెలుగు: నాడీ వ్యవస్థ యొక్క ప్రాథమిక యూనిట్ ఏది?', 'Neuron / న్యూరాన్', 'Cell / కణం', 'Axon / యాక్సాన్', 'Synapse / సైనాప్స్', 'A', 'M', '', 1),
    ('Which part of the brain controls balance and coordination?\\nతెలుగు: మెదడులో సమతుల్యత మరియు సమన్వయాన్ని నియంత్రించే భాగం ఏది?', 'Cerebellum / సెరెబెల్లమ్', 'Cerebrum / సెరిబ్రమ్', 'Medulla / మెడుల్లా', 'Hypothalamus / హైపోథాలమస్', 'A', 'M', '', 2),
    ('The largest part of the brain is the?\\nతెలుగు: మెదడులో అతిపెద్ద భాగం ఏది?', 'Cerebrum / సెరిబ్రమ్', 'Cerebellum / సెరెబెల్లమ్', 'Brain stem / మెదడు కాండం', 'Medulla oblongata / మెడుల్లా ఆబ్లాంగేటా', 'A', 'M', '', 3),
    ('What is the speed of nerve impulse approximately?\\nతెలుగు: నాడీ ఆవేగం యొక్క వేగం సుమారు ఎంత?', '120 m/s / 120 మీ/సె', '10 m/s / 10 మీ/సె', '1000 m/s / 1000 మీ/సె', '1 m/s / 1 మీ/సె', 'A', 'M', '', 4),
    ('The gap between two neurons is called?\\nతెలుగు: రెండు న్యూరాన్ల మధ్య అంతరాన్ని ఏమంటారు?', 'Synapse / సైనాప్స్', 'Axon / యాక్సాన్', 'Dendrite / డెండ్రైట్', 'Node of Ranvier / నోడ్ ఆఫ్ రాన్వియర్', 'A', 'M', '', 5),
    ('Which part of the neuron receives signals?\\nతెలుగు: సంకేతాలను స్వీకరించే న్యూరాన్ భాగం ఏది?', 'Dendrite / డెండ్రైట్', 'Axon / యాక్సాన్', 'Myelin sheath / మైలిన్ శ్రేణి', 'Cell body / కణ శరీరం', 'A', 'M', '', 6),
    ('Which part of the nervous system controls reflex actions?\\nతెలుగు: రిఫ్లెక్స్ చర్యలను నియంత్రించే నాడీ వ్యవస్థ భాగం ఏది?', 'Spinal cord / వెన్నుపాము', 'Brain / మెదడు', 'Cerebellum / సెరెబెల్లమ్', 'Autonomic nervous system / స్వయంచాలక నాడీ వ్యవస్థ', 'A', 'M', '', 7),
    ('How many pairs of cranial nerves are in humans?\\nతెలుగు: మానవులలో ఎన్ని జతల క్రానియల్ నరాలు ఉంటాయి?', '12 pairs / 12 జతలు', '10 pairs / 10 జతలు', '8 pairs / 8 జతలు', '14 pairs / 14 జతలు', 'A', 'M', '', 8),
    ('The cerebrum is divided into how many hemispheres?\\nతెలుగు: సెరిబ్రమ్ ఎన్ని అర్ధగోళాలుగా విభజించబడింది?', 'Two / రెండు', 'Three / మూడు', 'Four / నాలుగు', 'One / ఒకటి', 'A', 'M', '', 9),
    ('What chemical transmits signals across a synapse?\\nతెలుగు: సైనాప్స్ అంతటా సంకేతాలు ప్రసారం చేసే రసాయనం ఏది?', 'Neurotransmitter / న్యూరోట్రాన్స్‌మిటర్', 'Hormone / హార్మోన్', 'Enzyme / ఎంజైమ్', 'Vitamin / విటమిన్', 'A', 'M', '', 10),
    ('Alzheimer\'s disease affects which organ?\\nతెలుగు: అల్జీమర్స్ వ్యాధి ఏ అవయవాన్ని ప్రభావితం చేస్తుంది?', 'Brain / మెదడు', 'Kidney / మూత్రపిండం', 'Liver / కాలేయం', 'Heart / హృదయం', 'A', 'M', '', 11),
    ('The autonomic nervous system controls which functions?\\nతెలుగు: స్వయంచాలక నాడీ వ్యవస్థ ఏ విధులను నియంత్రిస్తుంది?', 'Involuntary body functions / అప్రమేయ శరీర విధులు', 'Voluntary movements / స్వేచ్ఛా కదలికలు', 'Thinking / ఆలోచన', 'Memory / జ్ఞాపకం', 'A', 'M', '', 12),
    ('Which part of the brain controls hunger and thirst?\\nతెలుగు: ఆకలి మరియు దాహాన్ని నియంత్రించే మెదడు భాగం ఏది?', 'Hypothalamus / హైపోథాలమస్', 'Cerebrum / సెరిబ్రమ్', 'Thalamus / థాలమస్', 'Hippocampus / హిప్పోకాంపస్', 'A', 'M', '', 13),
    ('CSF stands for?\\nతెలుగు: CSF అంటే ఏమిటి?', 'Cerebrospinal Fluid / సెరెబ్రోస్పైనల్ ద్రవం', 'Central Spinal Fiber / సెంట్రల్ స్పైనల్ ఫైబర్', 'Cerebral Signal Flow / సెరెబ్రల్ సిగ్నల్ ఫ్లో', 'Cranial Sensory Function / క్రానియల్ సెన్సరీ ఫంక్షన్', 'A', 'M', '', 14),
    ('Which lobe of the cerebrum is associated with vision?\\nతెలుగు: సెరిబ్రమ్ యొక్క ఏ లోబ్ దృష్టితో సంబంధం ఉంది?', 'Occipital lobe / ఆక్సిపిటల్ లోబ్', 'Frontal lobe / ఫ్రంటల్ లోబ్', 'Temporal lobe / టెంపోరల్ లోబ్', 'Parietal lobe / పేరియటల్ లోబ్', 'A', 'M', '', 15),
    ('Which gland is called the master gland?\\nతెలుగు: మాస్టర్ గ్రంధి అని పిలువబడే గ్రంధి ఏది?', 'Pituitary gland / పిట్యుటరీ గ్రంధి', 'Thyroid gland / థైరాయిడ్ గ్రంధి', 'Adrenal gland / అడ్రినల్ గ్రంధి', 'Pancreas / క్లోమం', 'A', 'M', '', 16),
    ('Insulin is produced by which organ?\\nతెలుగు: ఇన్సులిన్ ఏ అవయవం ద్వారా ఉత్పత్తి అవుతుంది?', 'Pancreas / క్లోమం', 'Liver / కాలేయం', 'Kidney / మూత్రపిండం', 'Adrenal gland / అడ్రినల్ గ్రంధి', 'A', 'M', '', 17),
    ('Deficiency of which hormone causes diabetes mellitus?\\nతెలుగు: ఏ హార్మోన్ లోపం వల్ల డయాబెటిస్ మెల్లిటస్ వస్తుంది?', 'Insulin / ఇన్సులిన్', 'Glucagon / గ్లూకాగాన్', 'Adrenaline / అడ్రినలిన్', 'Thyroxine / థైరాక్సిన్', 'A', 'M', '', 18),
    ('Which hormone is responsible for the fight-or-flight response?\\nతెలుగు: ఫైట్-ఆర్-ఫ్లైట్ ప్రతిస్పందనకు బాధ్యత వహించే హార్మోన్ ఏది?', 'Adrenaline / అడ్రినలిన్', 'Insulin / ఇన్సులిన్', 'Melatonin / మెలటోనిన్', 'Cortisol / కార్టిసోల్', 'A', 'M', '', 19),
    ('Where is the thyroid gland located?\\nతెలుగు: థైరాయిడ్ గ్రంధి ఎక్కడ ఉంటుంది?', 'Neck / మెడలో', 'Chest / ఛాతీలో', 'Abdomen / పొట్టలో', 'Brain / మెదడులో', 'A', 'M', '', 20),
    ('Thyroxine hormone is produced by which gland?\\nతెలుగు: థైరాక్సిన్ హార్మోన్ ఏ గ్రంధి ద్వారా ఉత్పత్తి అవుతుంది?', 'Thyroid gland / థైరాయిడ్ గ్రంధి', 'Pituitary gland / పిట్యుటరీ గ్రంధి', 'Adrenal gland / అడ్రినల్ గ్రంధి', 'Parathyroid gland / పారాథైరాయిడ్ గ్రంధి', 'A', 'M', '', 21),
    ('Goitre is caused by deficiency of?\\nతెలుగు: గాయిటర్ దేని లోపం వల్ల వస్తుంది?', 'Iodine / అయోడిన్', 'Iron / ఇనుము', 'Calcium / కాల్షియం', 'Zinc / జింక్', 'A', 'M', '', 22),
    ('Which hormone controls the sleep cycle?\\nతెలుగు: నిద్ర చక్రాన్ని నియంత్రించే హార్మోన్ ఏది?', 'Melatonin / మెలటోనిన్', 'Serotonin / సెరోటోనిన్', 'Dopamine / డోపమైన్', 'Oxytocin / ఆక్సిటోసిన్', 'A', 'M', '', 23),
    ('Which gland produces growth hormone?\\nతెలుగు: వృద్ధి హార్మోన్ ఉత్పత్తి చేసే గ్రంధి ఏది?', 'Pituitary gland / పిట్యుటరీ గ్రంధి', 'Thyroid gland / థైరాయిడ్ గ్రంధి', 'Adrenal gland / అడ్రినల్ గ్రంధి', 'Pineal gland / పైనియల్ గ్రంధి', 'A', 'M', '', 24),
    ('Cortisol is produced by which gland?\\nతెలుగు: కార్టిసోల్ ఏ గ్రంధి ద్వారా ఉత్పత్తి అవుతుంది?', 'Adrenal gland / అడ్రినల్ గ్రంధి', 'Thyroid gland / థైరాయిడ్ గ్రంధి', 'Pituitary gland / పిట్యుటరీ గ్రంధి', 'Pancreas / క్లోమం', 'A', 'M', '', 25),
    ('Parathyroid hormone regulates which mineral?\\nతెలుగు: పారాథైరాయిడ్ హార్మోన్ ఏ ఖనిజాన్ని నియంత్రిస్తుంది?', 'Calcium / కాల్షియం', 'Iron / ఇనుము', 'Sodium / సోడియం', 'Potassium / పొటాషియం', 'A', 'M', '', 26),
    ('Which organ is both an endocrine and exocrine gland?\\nతెలుగు: ఎండోక్రైన్ మరియు ఎక్సోక్రైన్ రెండూ అయిన అవయవం ఏది?', 'Pancreas / క్లోమం', 'Liver / కాలేయం', 'Kidney / మూత్రపిండం', 'Spleen / ప్లీహం', 'A', 'M', '', 27),
    ('Estrogen is primarily produced by?\\nతెలుగు: ఈస్ట్రోజెన్ ప్రధానంగా ఎక్కడ ఉత్పత్తి అవుతుంది?', 'Ovaries / అండాశయాలు', 'Adrenal gland / అడ్రినల్ గ్రంధి', 'Pituitary gland / పిట్యుటరీ గ్రంధి', 'Thyroid gland / థైరాయిడ్ గ్రంధి', 'A', 'M', '', 28),
    ('Testosterone is produced by?\\nతెలుగు: టెస్టోస్టెరోన్ ఎక్కడ ఉత్పత్తి అవుతుంది?', 'Testes / వృషణాలు', 'Adrenal gland / అడ్రినల్ గ్రంధి', 'Pituitary gland / పిట్యుటరీ గ్రంధి', 'Liver / కాలేయం', 'A', 'M', '', 29),
    ('Which endocrine gland is associated with puberty?\\nతెలుగు: యుక్తవయసుతో సంబంధం ఉన్న ఎండోక్రైన్ గ్రంధి ఏది?', 'Gonads / గోనాడ్స్', 'Thyroid / థైరాయిడ్', 'Adrenal / అడ్రినల్', 'Pituitary / పిట్యుటరీ', 'A', 'M', '', 30),
    ('Parkinson\'s disease is caused by deficiency of which neurotransmitter?\\nతెలుగు: పార్కిన్సన్స్ వ్యాధి ఏ న్యూరోట్రాన్స్‌మిటర్ లోపం వల్ల వస్తుంది?', 'Dopamine / డోపమైన్', 'Serotonin / సెరోటోనిన్', 'Acetylcholine / అసిటైల్‌కోలైన్', 'GABA / గాబా', 'A', 'M', '', 31),
    ('Which neurotransmitter is responsible for mood regulation?\\nతెలుగు: మూడ్ నియంత్రణకు బాధ్యత వహించే న్యూరోట్రాన్స్‌మిటర్ ఏది?', 'Serotonin / సెరోటోనిన్', 'Dopamine / డోపమైన్', 'Adrenaline / అడ్రినలిన్', 'Glutamate / గ్లూటమేట్', 'A', 'M', '', 32),
    ('The pineal gland is located in?\\nతెలుగు: పైనియల్ గ్రంధి ఎక్కడ ఉంటుంది?', 'Brain / మెదడు', 'Neck / మెడ', 'Chest / ఛాతీ', 'Abdomen / పొట్ట', 'A', 'M', '', 33),
    ('Hypothyroidism results from deficiency of?\\nతెలుగు: హైపోథైరాయిడిజం ఏ లోపం వల్ల వస్తుంది?', 'Thyroxine / థైరాక్సిన్', 'Insulin / ఇన్సులిన్', 'Cortisol / కార్టిసోల్', 'Adrenaline / అడ్రినలిన్', 'A', 'M', '', 34),
    ('Which hormone is released during stress?\\nతెలుగు: ఒత్తిడి సమయంలో విడుదలయ్యే హార్మోన్ ఏది?', 'Cortisol / కార్టిసోల్', 'Insulin / ఇన్సులిన్', 'Oxytocin / ఆక్సిటోసిన్', 'Melatonin / మెలటోనిన్', 'A', 'M', '', 35),
    ('The nervous system is divided into how many main parts?\\nతెలుగు: నాడీ వ్యవస్థ ఎన్ని ప్రధాన భాగాలుగా విభజించబడింది?', 'Two / రెండు (CNS & PNS)', 'Three / మూడు', 'Four / నాలుగు', 'Five / అయిదు', 'A', 'M', '', 36),
    ('The spinal cord is protected by?\\nతెలుగు: వెన్నుపాము ఏ ద్వారా రక్షించబడుతుంది?', 'Vertebral column / వెర్టిబ్రల్ కాలమ్', 'Ribcage / పక్కటెముకలు', 'Skull / పుర్రె', 'Pelvis / పెల్విస్', 'A', 'M', '', 37),
    ('What is the role of myelin sheath around axon?\\nతెలుగు: యాక్సాన్ చుట్టూ మైలిన్ శ్రేణి పాత్ర ఏమిటి?', 'Insulates and speeds up impulse / ఆవేగాన్ని అలగోడుతుంది మరియు వేగవంతం చేస్తుంది', 'Produces neurotransmitters / న్యూరోట్రాన్స్‌మిటర్లు ఉత్పత్తి చేస్తుంది', 'Connects neurons / న్యూరాన్లను కలుపుతుంది', 'Stores memories / జ్ఞాపకాలు నిల్వ చేస్తుంది', 'A', 'M', '', 38),
    ('Which part of the brain is involved in memory?\\nతెలుగు: జ్ఞాపకంతో సంబంధం ఉన్న మెదడు భాగం ఏది?', 'Hippocampus / హిప్పోకాంపస్', 'Cerebellum / సెరెబెల్లమ్', 'Medulla / మెడుల్లా', 'Pons / పాన్స్', 'A', 'M', '', 39),
    ('Endocrine glands release hormones directly into?\\nతెలుగు: ఎండోక్రైన్ గ్రంధులు హార్మోన్లను నేరుగా ఎక్కడ విడుదల చేస్తాయి?', 'Bloodstream / రక్తప్రవాహంలో', 'Lymph system / లింఫ్ వ్యవస్థలో', 'Ducts / నాళాల ద్వారా', 'Intestine / పేగులో', 'A', 'M', '', 40),
    ('Which cranial nerve controls vision?\\nతెలుగు: దృష్టిని నియంత్రించే క్రానియల్ నరం ఏది?', 'Optic nerve / ఆప్టిక్ నరం', 'Olfactory nerve / ఆల్ఫాక్టరీ నరం', 'Vagus nerve / వేగస్ నరం', 'Facial nerve / ముఖ నరం', 'A', 'M', '', 41),
    ('The fight-or-flight response involves which nervous system division?\\nతెలుగు: ఫైట్-ఆర్-ఫ్లైట్ ప్రతిస్పందన నాడీ వ్యవస్థ యొక్క ఏ విభాగాన్ని కలిగి ఉంది?', 'Sympathetic nervous system / సానుభూతి నాడీ వ్యవస్థ', 'Parasympathetic nervous system / పారాసానుభూతి నాడీ వ్యవస్థ', 'Somatic nervous system / శారీరక నాడీ వ్యవస్థ', 'Enteric nervous system / ఎంటెరిక్ నాడీ వ్యవస్థ', 'A', 'M', '', 42),
    ('Which hormone controls blood sugar levels?\\nతెలుగు: రక్తంలో చక్కెర స్థాయిలను నియంత్రించే హార్మోన్ ఏది?', 'Insulin and Glucagon / ఇన్సులిన్ మరియు గ్లూకాగాన్', 'Thyroxine only / కేవలం థైరాక్సిన్', 'Adrenaline only / కేవలం అడ్రినలిన్', 'Cortisol only / కేవలం కార్టిసోల్', 'A', 'M', '', 43),
    ('Acromegaly is caused by excess of which hormone?\\nతెలుగు: అక్రోమెగలీ ఏ హార్మోన్ అధికం వల్ల వస్తుంది?', 'Growth hormone / వృద్ధి హార్మోన్', 'Insulin / ఇన్సులిన్', 'Thyroxine / థైరాక్సిన్', 'Cortisol / కార్టిసోల్', 'A', 'M', '', 44),
    ('How many lobes does the cerebrum have?\\nతెలుగు: సెరిబ్రమ్‌కు ఎన్ని లోబులు ఉంటాయి?', 'Four / నాలుగు', 'Two / రెండు', 'Six / ఆరు', 'Three / మూడు', 'A', 'M', '', 45),
    ('Which hormone promotes water retention in kidneys?\\nతెలుగు: మూత్రపిండాలలో నీటి నిధారణను ప్రోత్సహించే హార్మోన్ ఏది?', 'ADH (Vasopressin) / ADH (వాసోప్రెసిన్)', 'Aldosterone / ఆల్డోస్టెరోన్', 'Oxytocin / ఆక్సిటోసిన్', 'Cortisol / కార్టిసోల్', 'A', 'M', '', 46),
    ('Neurons that carry impulses towards the brain are called?\\nతెలుగు: మెదడు వైపు ఆవేగాలు మోసుకెళ్ళే న్యూరాన్లను ఏమంటారు?', 'Afferent/sensory neurons / అఫెరెంట్/ఇంద్రియ న్యూరాన్లు', 'Efferent/motor neurons / ఎఫెరెంట్/మోటార్ న్యూరాన్లు', 'Interneurons / ఇంటర్న్యూరాన్లు', 'Relay neurons / రిలే న్యూరాన్లు', 'A', 'M', '', 47),
    ('The pons is located in which part of the brain?\\nతెలుగు: పాన్స్ మెదడులో ఏ భాగంలో ఉంటుంది?', 'Brain stem / మెదడు కాండం', 'Cerebrum / సెరిబ్రమ్', 'Cerebellum / సెరెబెల్లమ్', 'Thalamus / థాలమస్', 'A', 'M', '', 48),
    ('Which chemical in the brain is linked to happiness?\\nతెలుగు: మెదడులో ఆనందానికి సంబంధించిన రసాయనం ఏది?', 'Dopamine / డోపమైన్', 'Adrenaline / అడ్రినలిన్', 'Cortisol / కార్టిసోల్', 'Histamine / హిస్టమైన్', 'A', 'M', '', 49),
    ('Reflex arc involves which pathway?\\nతెలుగు: రిఫ్లెక్స్ ఆర్క్ ఏ మార్గాన్ని కలిగి ఉంటుంది?', 'Sensory neuron → Spinal cord → Motor neuron / ఇంద్రియ న్యూరాన్ → వెన్నుపాము → మోటార్ న్యూరాన్', 'Brain → Spinal cord → Muscle / మెదడు → వెన్నుపాము → కండరం', 'Eye → Brain → Muscle / కన్ను → మెదడు → కండరం', 'Hormone → Blood → Organ / హార్మోన్ → రక్తం → అవయవం', 'A', 'M', '', 50),
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