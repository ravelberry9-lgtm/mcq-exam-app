import sqlite3, os

SOURCE = 'Science_Set5B_Synthetic_Materials_Ext'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    ('What is a polymer?\\nతెలుగు: పాలీమర్ అంటే ఏమిటి?', 'A single molecule / ఒకే అణువు', 'A long chain of repeating units / పునరావృత యూనిట్ల పొడవైన గొలుసు', 'An acid / ఒక ఆమ్లం', 'A metal / ఒక లోహం', 'B', 'M', '', 1),
    ('Nylon is a\\nతెలుగు: నైలాన్ అంటే ఏమిటి?', 'Natural fibre / సహజ నార', 'Synthetic fibre / కృత్రిమ నార', 'Protein fibre / ప్రోటీన్ నార', 'Cellulose fibre / సెల్యులోస్ నార', 'B', 'M', '', 2),
    ('PVC stands for\\nతెలుగు: PVC అంటే ఏమిటి?', 'Polyvinyl chloride / పాలీవినైల్ క్లోరైడ్', 'Polyvinyl carbon / పాలీవినైల్ కార్బన్', 'Polyvoltage chloride / పాలీవోల్టేజ్ క్లోరైడ్', 'Polyviscous compound / పాలీవిస్కస్ సమ్మేళనం', 'A', 'M', '', 3),
    ('Natural rubber is obtained from\\nతెలుగు: సహజ రబ్బరు దేని నుండి తీయబడుతుంది?', 'Cotton plant / పత్తి మొక్క', 'Hevea tree / హీవియా చెట్టు', 'Pine tree / పైన్ చెట్టు', 'Bamboo / వెదురు', 'B', 'M', '', 4),
    ('Vulcanization of rubber involves adding\\nతెలుగు: రబ్బరు వల్కనీకరణలో ఏమి కలుపుతారు?', 'Nitrogen / నైట్రోజన్', 'Sulphur / సల్ఫర్', 'Carbon / కార్బన్', 'Chlorine / క్లోరిన్', 'B', 'M', '', 5),
    ('Teflon is used in making\\nతెలుగు: టెఫ్లాన్ దేని తయారీలో ఉపయోగిస్తారు?', 'Non-stick cookware / నాన్-స్టిక్ వంట పాత్రలు', 'Clothing / దుస్తులు', 'Medicines / మందులు', 'Fuel / ఇంధనం', 'A', 'M', '', 6),
    ('Rayon is made from\\nతెలుగు: రేయాన్ దేని నుండి తయారవుతుంది?', 'Petroleum / పెట్రోలియం', 'Cellulose / సెల్యులోస్', 'Protein / ప్రోటీన్', 'Coal / బొగ్గు', 'B', 'M', '', 7),
    ('The monomer of polyethylene is\\nతెలుగు: పాలీఎథిలీన్ యొక్క మోనోమర్ ఏమిటి?', 'Styrene / స్టైరీన్', 'Ethylene / ఎథిలీన్', 'Propylene / ప్రొపీలీన్', 'Vinyl chloride / వినైల్ క్లోరైడ్', 'B', 'M', '', 8),
    ('Which synthetic fibre is also called artificial silk?\\nతెలుగు: కృత్రిమ పట్టు అని పిలువబడే సింథటిక్ నార ఏది?', 'Nylon / నైలాన్', 'Polyester / పాలీయెస్టర్', 'Rayon / రేయాన్', 'Acrylic / ఆక్రిలిక్', 'C', 'M', '', 9),
    ('Bakelite is used in making\\nతెలుగు: బేకేలైట్ దేని తయారీలో వాడతారు?', 'Electrical switches / విద్యుత్ స్విచ్‌లు', 'Clothing / దుస్తులు', 'Food packaging / ఆహార ప్యాకేజింగ్', 'Medicines / మందులు', 'A', 'M', '', 10),
    ('Aspirin is chemically\\nతెలుగు: ఆస్పిరిన్ రసాయనికంగా ఏమిటి?', 'Acetylsalicylic acid / ఎసిటైల్ సాలిసిలిక్ ఆమ్లం', 'Paracetamol / పారాసిటమాల్', 'Ibuprofen / ఐబుప్రోఫెన్', 'Codeine / కోడీన్', 'A', 'M', '', 11),
    ('Polystyrene is used in\\nతెలుగు: పాలీస్టైరీన్ దేనిలో ఉపయోగిస్తారు?', 'Packaging and insulation / ప్యాకేజింగ్ మరియు ఇన్సులేషన్', 'Food / ఆహారం', 'Medicines / మందులు', 'Textiles / వస్త్రాలు', 'A', 'M', '', 12),
    ('The first synthetic plastic was\\nతెలుగు: మొదటి సింథటిక్ ప్లాస్టిక్ ఏమిటి?', 'PVC / PVC', 'Nylon / నైలాన్', 'Bakelite / బేకేలైట్', 'Polyester / పాలీయెస్టర్', 'C', 'M', '', 13),
    ('Which polymer is used to make bulletproof vests?\\nతెలుగు: బుల్లెట్‌ప్రూఫ్ వెస్ట్‌లు తయారీలో ఉపయోగించే పాలీమర్ ఏది?', 'Nylon / నైలాన్', 'Kevlar / కెవ్లార్', 'Polyester / పాలీయెస్టర్', 'Acrylic / ఆక్రిలిక్', 'B', 'M', '', 14),
    ('Synthetic rubber is also called\\nతెలుగు: సింథటిక్ రబ్బర్‌ను మరేమని పిలుస్తారు?', 'Buna-S / బూనా-S', 'Natural latex / సహజ లాటెక్స్', 'Teflon / టెఫ్లాన్', 'Bakelite / బేకేలైట్', 'A', 'M', '', 15),
    ('Which acid is used in making nylon?\\nతెలుగు: నైలాన్ తయారీలో ఉపయోగించే ఆమ్లం ఏది?', 'Acetic acid / ఎసిటిక్ ఆమ్లం', 'Adipic acid / ఎడిపిక్ ఆమ్లం', 'Citric acid / సిట్రిక్ ఆమ్లం', 'Sulphuric acid / సల్ఫ్యూరిక్ ఆమ్లం', 'B', 'M', '', 16),
    ('Plastics that can be softened on heating are called\\nతెలుగు: వేడిచేసినప్పుడు మెత్తబడే ప్లాస్టిక్‌లను ఏమంటారు?', 'Thermosetting plastics / థర్మోసెట్టింగ్ ప్లాస్టిక్‌లు', 'Thermoplastics / థర్మోప్లాస్టిక్‌లు', 'Elastomers / ఎలాస్టోమర్లు', 'Composites / సమ్మిశ్రమాలు', 'B', 'M', '', 17),
    ('DDT is a\\nతెలుగు: DDT అంటే ఏమిటి?', 'Fertiliser / ఎరువు', 'Pesticide / పురుగుమందు', 'Antibiotic / యాంటిబయాటిక్', 'Dye / రంగు', 'B', 'M', '', 18),
    ('Which synthetic material is used in making ropes?\\nతెలుగు: తాళ్ళ తయారీలో ఉపయోగించే సింథటిక్ పదార్థం ఏది?', 'Nylon / నైలాన్', 'Silk / పట్టు', 'Cotton / పత్తి', 'Wool / ఉన్ని', 'A', 'M', '', 19),
    ('Penicillin was discovered by\\nతెలుగు: పెన్సిలిన్‌ను ఎవరు కనుగొన్నారు?', 'Louis Pasteur / లూయిస్ పాశ్చర్', 'Alexander Fleming / అలెగ్జాండర్ ఫ్లెమింగ్', 'Edward Jenner / ఎడ్వర్డ్ జెన్నర్', 'Robert Koch / రాబర్ట్ కాక్', 'B', 'M', '', 20),
    ('Polythene is used for\\nతెలుగు: పాలిథీన్ దేని కోసం ఉపయోగిస్తారు?', 'Making carry bags / క్యారీ బ్యాగ్‌లు తయారీ', 'Making medicines / మందుల తయారీ', 'Making circuits / సర్కిట్‌ల తయారీ', 'Making glass / గాజు తయారీ', 'A', 'M', '', 21),
    ('The raw material for most synthetic fibres is\\nతెలుగు: చాలా సింథటిక్ నారల ముడి పదార్థం ఏమిటి?', 'Wood / కలప', 'Petroleum / పెట్రోలియం', 'Sand / ఇసుక', 'Water / నీరు', 'B', 'M', '', 22),
    ('LPG stands for\\nతెలుగు: LPG అంటే ఏమిటి?', 'Liquid petroleum gas / లిక్విడ్ పెట్రోలియం గ్యాస్', 'Light petroleum gas / లైట్ పెట్రోలియం గ్యాస్', 'Low pressure gas / లో ప్రెషర్ గ్యాస్', 'Liquefied propane gas / లిక్విఫైడ్ ప్రొపేన్ గ్యాస్', 'A', 'M', '', 23),
    ('CNG stands for\\nతెలుగు: CNG అంటే ఏమిటి?', 'Compressed natural gas / కంప్రెస్డ్ నేచురల్ గ్యాస్', 'Carbon natural gas / కార్బన్ నేచురల్ గ్యాస్', 'Chemical nitrogen gas / కెమికల్ నైట్రోజన్ గ్యాస్', 'Condensed nitrogen gas / కండెన్స్డ్ నైట్రోజన్ గ్యాస్', 'A', 'M', '', 24),
    ('Which plastic is used in making water bottles?\\nతెలుగు: నీటి బాటిళ్ళ తయారీలో ఉపయోగించే ప్లాస్టిక్ ఏది?', 'PET / PET', 'PVC / PVC', 'HDPE / HDPE', 'Polystyrene / పాలీస్టైరీన్', 'A', 'M', '', 25),
    ('Glass fibre is a type of\\nతెలుగు: గ్లాస్ ఫైబర్ ఏ రకమైన పదార్థం?', 'Natural material / సహజ పదార్థం', 'Composite material / సమ్మిశ్రమ పదార్థం', 'Metal alloy / లోహ మిశ్రమం', 'Ceramic / సిరామిక్', 'B', 'M', '', 26),
    ('Terylene is a brand name for\\nతెలుగు: టెరిలీన్ అంటే దేని బ్రాండ్ నామం?', 'Nylon / నైలాన్', 'Polyester / పాలీయెస్టర్', 'Acrylic / ఆక్రిలిక్', 'Rayon / రేయాన్', 'B', 'M', '', 27),
    ('Which gas is used in making PVC?\\nతెలుగు: PVC తయారీలో ఉపయోగించే వాయువు ఏది?', 'Vinyl chloride / వినైల్ క్లోరైడ్', 'Ethylene / ఎథిలీన్', 'Propylene / ప్రొపీలీన్', 'Styrene / స్టైరీన్', 'A', 'M', '', 28),
    ('The property of rubber to return to original shape is called\\nతెలుగు: రబ్బర్ తన అసలు ఆకారానికి తిరిగి వచ్చే లక్షణాన్ని ఏమంటారు?', 'Plasticity / సుఘటనీయత', 'Elasticity / స్థితిస్థాపకత', 'Ductility / తన్యత', 'Malleability / పిండనీయత', 'B', 'M', '', 29),
    ('The full form of HDPE is\\nతెలుగు: HDPE యొక్క పూర్తి రూపం ఏమిటి?', 'High density polyethylene / హై డెన్సిటీ పాలీఎథిలీన్', 'High definition polyester / హై డెఫినిషన్ పాలీయెస్టర్', 'Heavy duty plastic electrode / హెవీ డ్యూటీ ప్లాస్టిక్ ఎలక్ట్రోడ్', 'Hydrocarbon density plastic electric / హైడ్రోకార్బన్ డెన్సిటీ ప్లాస్టిక్', 'A', 'M', '', 30),
    ('Insecticides and pesticides are examples of\\nతెలుగు: పురుగుమందులు మరియు కీటకనాశనులు ఏ రకమైన సమ్మేళనాలు?', 'Natural chemicals / సహజ రసాయనాలు', 'Agrochemicals / వ్యవసాయ రసాయనాలు', 'Food additives / ఆహార సంయుక్తాలు', 'Dyes / రంగులు', 'B', 'M', '', 31),
    ('The term polymer comes from Greek words meaning\\nతెలుగు: పాలీమర్ అనే పదం గ్రీకు భాషలో దేనిని సూచిస్తుంది?', 'One unit / ఒక యూనిట్', 'Many parts / చాలా భాగాలు', 'Long chain / పొడవైన గొలుసు', 'Branched structure / శాఖలు కలిగిన నిర్మాణం', 'B', 'M', '', 32),
    ('Which polymer is used in making transparent sheets?\\nతెలుగు: పారదర్శక రేకుల తయారీలో ఉపయోగించే పాలీమర్ ఏది?', 'Polycarbonate / పాలీకార్బొనేట్', 'PVC / PVC', 'Nylon / నైలాన్', 'Polyester / పాలీయెస్టర్', 'A', 'M', '', 33),
    ('The natural polymer used in making tyres before vulcanization was\\nతెలుగు: వల్కనీకరణకు ముందు టైర్ల తయారీలో ఉపయోగించిన సహజ పాలీమర్ ఏమిటి?', 'Latex / లాటెక్స్', 'Cellulose / సెల్యులోస్', 'Starch / స్టార్చ్', 'Protein / ప్రోటీన్', 'A', 'M', '', 34),
    ('Dyes used in textiles are mainly\\nతెలుగు: వస్త్రాలలో వాడే రంగులు ప్రధానంగా ఏ రకమైనవి?', 'Natural dyes / సహజ రంగులు', 'Synthetic dyes / కృత్రిమ రంగులు', 'Metal-based dyes / లోహ ఆధారిత రంగులు', 'Vegetable dyes / కూరగాయల రంగులు', 'B', 'M', '', 35),
    ('The first antibiotic was\\nతెలుగు: మొదటి యాంటిబయాటిక్ ఏమిటి?', 'Streptomycin / స్ట్రెప్టోమైసిన్', 'Tetracycline / టెట్రాసైక్లిన్', 'Penicillin / పెన్సిలిన్', 'Amoxicillin / అమాక్సిసిలిన్', 'C', 'M', '', 36),
    ('Bio-degradable plastics are preferred because\\nతెలుగు: బయో-డీగ్రేడబుల్ ప్లాస్టిక్‌లు ఎందుకు ప్రాధాన్యత ఉన్నాయి?', 'They are cheaper / అవి చౌకగా ఉంటాయి', 'They decompose naturally / అవి సహజంగా కుళ్ళిపోతాయి', 'They are stronger / అవి బలంగా ఉంటాయి', 'They are transparent / అవి పారదర్శకంగా ఉంటాయి', 'B', 'M', '', 37),
    ('The polymer used in making contact lenses is\\nతెలుగు: కాంటాక్ట్ లెన్స్‌ల తయారీలో ఉపయోగించే పాలీమర్ ఏది?', 'PMMA / PMMA', 'PVC / PVC', 'Nylon / నైలాన్', 'Polyester / పాలీయెస్టర్', 'A', 'M', '', 38),
    ('Shellac is a\\nతెలుగు: షెల్లాక్ అంటే ఏమిటి?', 'Synthetic polymer / సింథటిక్ పాలీమర్', 'Natural resin / సహజ రెజిన్', 'Metal alloy / లోహ మిశ్రమం', 'Synthetic fibre / సింథటిక్ నార', 'B', 'M', '', 39),
    ('The main component of LPG is\\nతెలుగు: LPG యొక్క ప్రధాన భాగం ఏమిటి?', 'Methane / మీథేన్', 'Ethane / ఇథేన్', 'Butane and Propane / బ్యుటేన్ మరియు ప్రొపేన్', 'Hydrogen / హైడ్రోజన్', 'C', 'M', '', 40),
    ('Rubber trees originally belong to\\nతెలుగు: రబ్బరు చెట్లు మొదట్లో ఏ దేశానికి చెందినవి?', 'India / భారతదేశం', 'Brazil / బ్రెజిల్', 'Malaysia / మలేషియా', 'Indonesia / ఇండోనేషియా', 'B', 'M', '', 41),
    ('Which plastic is used for making toys?\\nతెలుగు: బొమ్మల తయారీలో వాడే ప్లాస్టిక్ ఏది?', 'PVC / PVC', 'Bakelite / బేకేలైట్', 'Polystyrene / పాలీస్టైరీన్', 'Kevlar / కెవ్లార్', 'C', 'M', '', 42),
    ('Synthetic detergents are derived from\\nతెలుగు: సింథటిక్ డిటర్జెంట్లు దేని నుండి తయారవుతాయి?', 'Animal fat / జంతువుల కొవ్వు', 'Petroleum products / పెట్రోలియం ఉత్పత్తులు', 'Plant oils / మొక్కల నూనెలు', 'Minerals / ఖనిజాలు', 'B', 'M', '', 43),
    ('Melamine is used in making\\nతెలుగు: మెలమైన్ దేని తయారీలో వాడతారు?', 'Crockery / గిన్నెలు', 'Clothing / దుస్తులు', 'Ropes / తాళ్ళు', 'Explosives / పేలుళ్ళు', 'A', 'M', '', 44),
    ('Which is a thermosetting plastic?\\nతెలుగు: థర్మోసెట్టింగ్ ప్లాస్టిక్ ఏది?', 'Polythene / పాలిథీన్', 'PVC / PVC', 'Bakelite / బేకేలైట్', 'Polystyrene / పాలీస్టైరీన్', 'C', 'M', '', 45),
    ('Carbon fibre is used in\\nతెలుగు: కార్బన్ ఫైబర్ దేనిలో ఉపయోగిస్తారు?', 'Aircraft and sports equipment / విమానాలు మరియు క్రీడా సామగ్రి', 'Food packaging / ఆహార ప్యాకేజింగ్', 'Medicines / మందులు', 'Clothing / దుస్తులు', 'A', 'M', '', 46),
    ('The main source of petrochemicals is\\nతెలుగు: పెట్రో కెమికల్స్ యొక్క ప్రధాన వనరు ఏమిటి?', 'Coal / బొగ్గు', 'Crude oil / ముడి చమురు', 'Wood / కలప', 'Natural gas / సహజ వాయువు', 'B', 'M', '', 47),
    ('Formica is a brand name of\\nతెలుగు: ఫార్మికా అంటే ఏ పదార్థం బ్రాండ్ నేమ్?', 'Nylon / నైలాన్', 'Laminated plastic sheets / లామినేటెడ్ ప్లాస్టిక్ రేకులు', 'Rubber / రబ్బర్', 'PVC pipe / PVC పైపు', 'B', 'M', '', 48),
    ('The monomer of natural rubber is\\nతెలుగు: సహజ రబ్బర్ యొక్క మోనోమర్ ఏమిటి?', 'Styrene / స్టైరీన్', 'Isoprene / ఐసోప్రీన్', 'Ethylene / ఎథిలీన్', 'Propylene / ప్రొపీలీన్', 'B', 'M', '', 49),
    ('Synthetic fibres are generally\\nతెలుగు: సింథటిక్ నారలు సాధారణంగా ఎలా ఉంటాయి?', 'Biodegradable / జీవ క్షయం చెందేవి', 'Non-biodegradable / జీవ క్షయం చెందనివి', 'Soluble in water / నీటిలో కరిగేవి', 'Magnetic / అయస్కాంత గుణం ఉన్నవి', 'B', 'M', '', 50),
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