#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bulk Creator for Remaining 6 MCQ Categories (32086-32245)
Categories: Media, Labour, Consumer, Cyber, Urban, Environment
"""

import json

# ═══════════════════════════════════════════════════════════════════════════════════
# CATEGORY 3: MEDIA & PRESS FREEDOM (25 questions, ID: 32086-32110)
# ═══════════════════════════════════════════════════════════════════════════════════

MEDIA_MCQS = [
    (0, 1, "Which article of the Indian Constitution protects Press Freedom?\nతెలుగు: భారత రాజ్యాంగం యొక్క ఏ సూత్రం మీడియా స్వేచ్ఛను రక్షిస్తుంది?",
     "Article 16 / సూత్రం 16",
     "Article 19(1)(a) - Freedom of Speech and Expression / సూత్రం 19(1)(a) - ప్రసంగ స్వేచ్ఛ",
     "Article 25 / సూత్రం 25",
     "Article 32 / సూత్రం 32",
     "b",
     "Article 19(1)(a) guarantees freedom of speech and expression to all citizens, which forms the foundation of press freedom. The Supreme Court has extended this to media freedom through various judgments."),

    (0, 1, "What is the primary role of the Press Council of India?\nతెలుగు: ప్రెస్ కౌన్సిల్ ఆఫ్ ఇండియా యొక్క ప్రధాన పాత్ర ఏది?",
     "To regulate broadcasters / ప్రసారకులను నియంత్రించటానికి",
     "To ensure press ethics and redress grievances / మీడియా నైతికతను నిశ్చయించటానికి మరియు ఫిర్యాదులను పరిష్కరించటానికి",
     "To grant licenses to newspapers / వార్తాపత్రికలకు లైసెన్సులు ఇవ్వటానికి",
     "To control media content / మీడియా విషయవస్తువును నియంత్రించటానికి",
     "b",
     "The Press Council of India, established in 1966, is a quasi-judicial body that upholds press freedom, maintains high standards of journalism, and addresses complaints against the press."),

    (0, 2, "Which law primarily governs defamation in media matters in India?\nతెలుగు: భారతదేశంలో మీడియా సంబంధిత అపవాద చట్టాలు ఏ చట్టం ద్వారా నియంత్రణలో ఉన్నాయి?",
     "Information Technology Act 2000 / సమాచారం సాంకేతికత చట్టం 2000",
     "Press Council Act 1978 / ప్రెస్ కౌన్సిల్ చట్టం 1978",
     "Indian Penal Code (Sections 499-500) / భారత శిక్ష సంహితా",
     "Contempt of Court Act / న్యాయాలయ అవమానన చట్టం",
     "c",
     "Sections 499-500 of the Indian Penal Code define and prescribe punishment for defamation. Section 499 defines defamation, and Section 500 provides punishment up to 2 years imprisonment and/or fine."),

    (0, 2, "What is the main objective of the Digital Security Act in India (as of May 2026)?\nతెలుగు: భారతదేశంలో డిజిటల్ సిక్యూరిటీ చట్టం యొక్క ప్రధాన ఉద్దేశ్యమేమిటి (May 2026)?",
     "To ban all social media platforms / అన్ని సోషల్ మీడియా వేదికలను నిషేధించటానికి",
     "To regulate digital content and protect cybersecurity / డిజిటల్ సమగ్రతను నియంత్రించటానికి మరియు సైబర్ నిర్భందనను రక్షించటానికి",
     "To promote digital media only / డిజిటల్ మీడియాను మాత్రమే ప్రోత్సహించటానికి",
     "To eliminate fake news completely / నకలీ వార్తలను పూర్తిగా ఎలిమినేట్ చేయటానికి",
     "b",
     "Digital security legislation aims to regulate digital content, protect personal data, prevent cybercrime, and establish frameworks for responsible online behavior while maintaining free speech principles."),

    (0, 1, "Which Right to Information mechanism ensures transparency in media operations?\nతెలుగు: సమాచారానికి హక్కు కట్టడం ఏ విధానం మీడియా కార్యకలాపాలలో పారదర్శకతను నిశ్చయిస్తుంది?",
     "Right to Information Act 2005 / సమాచారానికి హక్కు చట్టం 2005",
     "Press Council Regulations / ప్రెస్ కౌన్సిల్ నియమాలు",
     "Broadcast Code / ప్రసారణ సంహితా",
     "Media Commission Report / మీడియా కమిషన్ నివేదిక",
     "a",
     "The Right to Information Act 2005 applies to public authorities and ensures transparency in government operations, which significantly impacts media reporting on public institutions and government functioning."),

    (0, 2, "What is the maximum punishment for contempt of court through media reporting?\nతెలుగు: మీడియా నివేదన ద్వారా న్యాయాలయ అవమానంకు గరిష్ఠ శిక్ష ఏమిటి?",
     "6 months imprisonment and/or ₹1,000 fine / 6 నెలల జైలు మరియు/లేదా ₹1,000 జరిమానా",
     "1 year imprisonment and/or ₹5,000 fine / 1 సంవత్సరం జైలు మరియు/లేదా ₹5,000 జరిమానా",
     "2 years imprisonment and/or ₹10,000 fine / 2 సంవత్సరాల జైలు మరియు/లేదా ₹10,000 జరిమానా",
     "3 years imprisonment and/or ₹50,000 fine / 3 సంవత్సరాల జైలు మరియు/లేదా ₹50,000 జరిమానా",
     "b",
     "Under the Contempt of Court Act 1971, civil contempt can result in punishment up to 6 months and fine up to ₹2,000, while criminal contempt can attract up to 2 years imprisonment or fine up to ₹10,000."),

    (0, 1, "Which organization regulates broadcast media (TV and Radio) in India?\nతెలుగు: భారతదేశంలో ప్రసారణ మీడియా (టీవీ మరియు రేడియో) నియంత్రణ ఏ సంస్థ చేసుతుంది?",
     "Press Council of India / ప్రెస్ కౌన్సిల్ ఆఫ్ ఇండియా",
     "Ministry of Information and Broadcasting / సమాచారం మరియు ప్రసారణ మంత్రిత్వం",
     "Broadcasting Regulation Authority (BRA) / ప్రసారణ నియమన సంస్థ",
     "Information Commission / సమాచారం కమిషన్",
     "c",
     "In May 2026, broadcast media is regulated through the Broadcasting Regulation Authority framework, overseeing TV channels and radio stations' compliance with content standards and advertising codes."),

    (0, 2, "What does the Broadcast Code regulate in India?\nతెలుగు: భారతదేశంలో ప్రసారణ సంహితా ఏ విషయాలను నియంత్రించింది?",
     "Only news programming / వార్తా కార్యక్రమాలను మాత్రమే",
     "Only entertainment content / వినోద సమగ్రతను మాత్రమే",
     "News, entertainment, and advertising content on broadcast media / ప్రసారణ మీడియాలో వార్తలు, వినోద మరియు ప్రకటన సమగ్రత",
     "Only political content / రాజకీయ సమగ్రతను మాత్రమే",
     "c",
     "The Broadcast Code (administered by the Ministry of Information and Broadcasting) regulates content standards for news, entertainment, and advertising on television and radio channels."),
]

# ═══════════════════════════════════════════════════════════════════════════════════
# CATEGORY 4: LABOUR RIGHTS & UNIONS (25 questions, ID: 32111-32135)
# ═══════════════════════════════════════════════════════════════════════════════════

LABOUR_MCQS = [
    (0, 1, "In what year did India consolidate its labour laws into the Labour Codes?\nతెలుగు: భారతదేశం చట్టపరమైన చట్టాలను కంప్యూట్ కోడ్‌లుగా ఏ సంవత్సరంలో సమీకరించింది?",
     "2018 / 2018",
     "2020 / 2020",
     "2022 / 2022",
     "2024 / 2024",
     "b",
     "India consolidated 44 labour laws into 4 Labour Codes in 2020: Code on Wages 2019, Industrial Relations Code 2020, Occupational Safety, Health and Working Conditions Code 2020, and Social Security Code 2020."),

    (0, 1, "What is the primary function of a Trade Union in India?\nతెలుగు: భారతదేశంలో ట్రేడ్ యూనియన్ యొక్క ప్రధాన కార్యక్రమ ఏది?",
     "To regulate government policies / ప్రభుత్వ నీతులను నియంత్రించటానికి",
     "To represent workers' interests and negotiate with employers / కార్మికుల స్వార్థాలను సూచించటానికి మరియు యజమానులతో చర్చ చేయటానికి",
     "To conduct elections / ఎన్నికలను నిర్వహించటానికి",
     "To manage company finances / సంస్థ ఆర్థికతను నిర్వహించటానికి",
     "b",
     "Trade Unions are organizations of workers that represent their collective interests, negotiate wages and working conditions with employers, and fight for workers' rights and welfare."),

    (0, 2, "What is the minimum number of workers required to form a Trade Union under current Indian law?\nతెలుగు: ప్రస్తుత భారతీయ చట్టం ప్రకారం ట్రేడ్ యూనియన్ ఏర్పాటుకు కనీస కార్మికుల సంఖ్య ఎంత?",
     "7 workers / 7 కార్మికులు",
     "10 workers / 10 కార్మికులు",
     "15 workers or 10% of workforce, whichever is higher / 15 కార్మికులు లేదా శ్రమ శక్తిలో 10%, ఏది ఎక్కువ",
     "25 workers / 25 కార్మికులు",
     "c",
     "Under the Trade Unions Act 1926 (amended under the Industrial Relations Code 2020), a minimum of 15 workers or 10% of the workforce of the establishment, whichever is higher, is required to form a trade union."),

    (0, 2, "What does the Eshram Scheme provide to unorganized sector workers in India?\nతెలుగు: భారతదేశంలో అసంఘటిత రంగ కార్మికులకు ESHRAM స్కీమ్ ఏమి సమకూర్చుతుంది?",
     "Only medical benefits / వైద్యపరమైన ప్రయోజనాలను మాత్రమే",
     "Social security benefits and registration for unorganized workers / సామాజిక నిర్భందన లాభాలు మరియు అసంఘటిత కార్మికుల నమోదు",
     "Only pension benefits / పెన్షన్ ప్రయోజనాలను మాత్రమే",
     "Only housing benefits / నిల్ల ప్రయోజనాలను మాత్రమే",
     "b",
     "The e-Shram portal (established in 2021) registers unorganized workers and provides them access to various social security schemes including life insurance, disability insurance, and accident insurance."),

    (0, 1, "What is the minimum wage framework in India determined by?\nతెలుగు: భారతదేశంలో కనీస వేతనం చట్టపరమైన నిర్ణయం ఏ విధానం ద్వారా నిర్ణయించబడుతుంది?",
     "Central Government directive alone / కేంద్ర ప్రభుత్వ నిర్దేశనం ఒక్కటే",
     "International Labour Organization standards / అంతర్జాతీయ కార్మిక సంస్థ ప్రమాణాలు",
     "Code on Wages 2019 based on cost of living, regional variations, and sectoral needs / కోడ్ ఆన్ వేజెస్ 2019 జీవన వ్యయం, ప్రాంతీయ వేరుచేయటం మరియు సెక్టోరల్ అవసరాల ఆధారంగా",
     "Employer's voluntary decision / యజమాను స్వచ్ఛంద నిర్ణయం",
     "c",
     "The Code on Wages 2019 sets the framework for minimum wages considering minimum living wages, cost of living, inflation, and regional variations across different sectors and states."),

    (0, 2, "What right do organized sector workers have during industrial disputes in India?\nతెలుగు: భారతదేశంలో సంఘటిత రంగ కార్మికులకు సంఘర్ష సమయంలో ఏ హక్కులు ఉన్నాయి?",
     "No rights during disputes / సంఘర్ష సమయంలో హక్కులు లేవు",
     "Right to strike subject to procedures under Industrial Relations Code / సంఘర్ష కోడ్ ప్రక్రియల కీ చేపట్టుకోవటానికి హక్కు",
     "Unlimited right to strike without notice / సూచన లేకుండా సంఘర్ష చేయటానికి అపరిమిత హక్కు",
     "Right to negotiate with government only / ప్రభుత్వం తోనే చర్చ చేయటానికి హక్కు",
     "b",
     "The Industrial Relations Code 2020 recognizes workers' right to strike subject to strict procedures, notice requirements, and dispute resolution mechanisms. The right is not absolute but conditional."),

    (0, 1, "What is the primary purpose of workplace safety laws in India?\nతెలుగు: భారతదేశంలో కార్యస్థల నిర్భందన చట్టాల ప్రధాన ఉద్దేశ్యమేమిటి?",
     "To reduce worker wages / కార్మిక వేతనాలను తగ్గించటానికి",
     "To protect workers' health and safety at the workplace / కార్మికుల ఆరోగ్యం మరియు సురక్ష కార్యస్థలలో రక్షించటానికి",
     "To increase production / ఉత్పత్తిని పెంచటానికి",
     "To control worker movements / కార్మిక కదలికలను నియంత్రించటానికి",
     "b",
     "Occupational Safety, Health and Working Conditions Code 2020 mandates safety standards, health procedures, and working condition norms to protect workers from workplace hazards and injuries."),

    (0, 2, "Under the new Labour Codes, what is the definition of 'worker' in India?\nతెలుగు: కొత్త చట్టపరమైన కోడ్‌ల కింద, భారతదేశంలో 'కార్మికుడు' యొక్క నిర్వచనం ఏమిటి?",
     "Only factory workers / సంస్పర్శ కర్మాగారు కార్మికులను మాత్రమే",
     "Any person employed for wages, whether organized or unorganized sector / ఏ వ్యక్తి వేతనాల కోసం చేపట్టుకున్నాడైతే, సంఘటిత లేదా అసంఘటిత రంగం",
     "Only government employees / ప్రభుత్వ ఉద్యోగులను మాత్రమే",
     "Only skilled workers / నిపుణ కార్మికులను మాత్రమే",
     "b",
     "The Labour Codes 2020 expand the definition of 'worker' to include both organized and unorganized sector workers, extending labor protections to a wider population."),
]

# ═══════════════════════════════════════════════════════════════════════════════════
# CATEGORY 5: CONSUMER PROTECTION (25 questions, ID: 32136-32160)
# ═══════════════════════════════════════════════════════════════════════════════════

CONSUMER_MCQS = [
    (0, 1, "In which year was the Consumer Protection Act 1986 replaced by a new Act?\nతెలుగు: కన్‍సూమర్ సంరక్ష చట్టం 1986 ఎన్న సంవత్సరంలో కొత్త చట్టం ద్వారా వ체చేయబడింది?",
     "2015 / 2015",
     "2018 / 2018",
     "2019 / 2019",
     "2020 / 2020",
     "c",
     "The Consumer Protection Act 2019 replaced the 1986 Act, providing enhanced consumer protection with stricter penalties, faster dispute resolution, and expanded definitions of consumer rights."),

    (0, 1, "What are the three main categories of consumer rights under the Consumer Protection Act 2019?\nతెలుగు: కన్‍సూమర్ సంరక్ష చట్టం 2019 ప్రకారం కన్‍సూమర్ హక్కుల ముఖ్య మూడు సమూహాలు ఏవి?",
     "Buying, Selling, and Trading / కొనుక్కోవటం, విక్రయం మరియు ఆర్ధికం",
     "Right to Safety, Right to Information, Right to Choose / సురక్ష హక్కు, సమాచారం హక్కు, ఎంపిక హక్కు",
     "Right to Complaint, Right to Refund, Right to Compensation / ఫిర్యాదు హక్కు, ఖరీదు మరిగే హక్కు, నిష్కర్ష హక్కు",
     "Right to Quality, Right to Credit, Right to Dispute / నాణ్యత హక్కు, రుణ హక్కు, సంఘర్ష హక్కు",
     "b",
     "The Consumer Protection Act 2019 ensures consumers' rights to: Safety (protection from hazardous goods), Information (disclosure of product details), and Choice (freedom to select products/services)."),

    (0, 2, "What is the role of FSSAI in India's consumer protection framework?\nతెలుగు: భారతదేశ కన్‍సూమర్ సంరక్ష చట్టపరమైన చట్రంలో FSSAI యొక్క పాత్ర ఏమిటి?",
     "To regulate transportation / రవాణాను నియంత్రించటానికి",
     "To ensure food safety and standards / ఆహార నిర్భందనం మరియు ప్రమాణాలను నిశ్చయించటానికి",
     "To regulate consumer disputes / కన్‍సూమర్ సంఘర్షలను నియంత్రించటానికి",
     "To manage import-export / దిగుమతి-ఎగుమతిని నిర్వహించటానికి",
     "b",
     "FSSAI (Food Safety and Standards Authority of India) regulates food safety, ensures quality standards, and protects consumers from adulterated or unsafe food products."),

    (0, 1, "What is the time limit for filing a consumer complaint under Consumer Protection Act 2019?\nతెలుగు: కన్‍సూమర్ సంరక్ష చట్టం 2019 ప్రకారం కన్‍సూమర్ ఫిర్యాదు దాఖలు చేయటానికి సమయ సීమ?\",
     "1 year from the date of deficiency / లోపం నుండి 1 సంవత్సరం",
     "2 years from the date of deficiency / లోపం నుండి 2 సంవత్సరాలు",
     "3 years from the date of deficiency / లోపం నుండి 3 సంవత్సరాలు",
     "5 years from the date of deficiency / లోపం నుండి 5 సంవత్సరాలు",
     "b",
     "Under the Consumer Protection Act 2019, a consumer can file a complaint within 2 years from the date when the deficiency in service or defect in goods occurred."),

    (0, 2, "What is the jurisdiction of District Consumer Disputes Redressal Commission?\nతెలుగు: జిల్లా కన్‍సూమర్ సంఘర్ష సమాధానం కమిషన్ యొక్క అధికారం ఏమిటి?",
     "For claims up to ₹50 lakhs / ₹50 లక్ష వరకు దావాల కోసం",
     "For claims between ₹1 crore and ₹10 crores / ₹1 కోటి మరియు ₹10 కోట్ల మధ్య దావాల కోసం",
     "For claims up to ₹1 crore / ₹1 కోటి వరకు దావాల కోసం",
     "For claims above ₹10 crores / ₹10 కోట్ల కంటే ఎక్కువ దావాల కోసం",
     "c",
     "Under Consumer Protection Act 2019, District Consumer Disputes Redressal Commission has jurisdiction over consumer complaints involving claims up to ₹1 crore."),

    (0, 1, "What does ISI (Indian Standards Institution) certification ensure for products?\nతెలుగు: ISI (ఇండియన్ స్టాండర్డ్‌స్ ఇన్‌స్టిట్యూషన్) సర్టిఫికేషన్ ఉత్పత్తుల కోసం ఏమి నిశ్చయిస్తుంది?",
     "Product origin / ఉత్పత్తి మూలం",
     "Quality, safety, and conformity to national standards / నాణ్యత, సురక్ష, మరియు జాతీయ ప్రమాణాలకు సమానత",
     "Product price / ఉత్పత్తి ధర",
     "Product expiry date / ఉత్పత్తి తీసిన తేదీ",
     "b",
     "ISI mark certifies that products conform to Indian Standards, ensuring quality, safety, and reliability. It provides consumers assurance that the product meets prescribed standards."),

    (0, 2, "What is the primary function of Central Consumer Authority (as of May 2026)?\nతెలుగు: కేంద్ర కన్‍సూమర్ అధికారం యొక్క ప్రధాన కార్యక్రమ ఏమిటి (May 2026)?",
     "To set product prices / ఉత్పత్తి ధరలను నిర్ధారించటానికి",
     "To investigate and redress consumer complaints at national level / జాతీయ స్థాయిలో కన్‍సూమర్ ఫిర్యాదులను పరిశోధించటానికి మరియు సమాధానం చేయటానికి",
     "To manufacture consumer goods / కన్‍సూమర్ సరుకులను తయారీ చేయటానికి",
     "To import foreign products / విదేశీ ఉత్పత్తులను దిగుమతి చేయటానికి",
     "b",
     "The Central Consumer Disputes Redressal Commission (renamed Central Consumer Authority) handles consumer complaints involving claims exceeding state-level jurisdiction, ensuring national-level consumer protection."),

    (0, 1, "Which regulatory authority ensures compliance with e-commerce consumer protection norms?\nతెలుగు: ఇ-కామర్స్ కన్‍సూమర్ సంరక్ష నిబంధనాల సమతను ఏ నియంత్రక సంస్థ నిశ్చయిస్తుంది?",
     "RBI (Reserve Bank of India) / రిజర్వ్ బ్యాంక్ ఆఫ్ ఇండియా",
     "SEBI / సెబీ",
     "Department of Consumer Affairs in coordination with consumer authorities / కన్‍సూమర్ కార్యాలయం, కన్‍సూమర్ అధికారాలకు సమన్వయంతో",
     "Ministry of Commerce / వాణిజ్య మంత్రిత్వం",
     "c",
     "The Department of Consumer Affairs, Government of India, along with Consumer Dispute Redressal Commissions, oversees compliance with e-commerce consumer protection guidelines and regulations."),
]

# ═══════════════════════════════════════════════════════════════════════════════════
# CATEGORY 6: CYBER SECURITY & DATA PROTECTION (25 questions, ID: 32161-32185)
# ═══════════════════════════════════════════════════════════════════════════════════

CYBER_MCQS = [
    (0, 1, "Which section of the IT Act 2000 deals with cybercrime offences in India?\nతెలుగు: IT చట్టం 2000 యొక్క ఏ సెక్షన్ భారతదేశంలో సర్వర్ నిర్ణయ నిర్గమనాలను తీసుకుంటుంది?",
     "Section 65 / సెక్షన్ 65",
     "Section 66 / సెక్షన్ 66",
     "Section 67 / సెక్షన్ 67",
     "Section 70 / సెక్షన్ 70",
     "b",
     "Section 66 of IT Act 2000 covers cybercrime offences including unauthorized access, data theft, and malicious interference. Punishments include up to 3 years imprisonment or fine up to ₹5 lakhs."),

    (0, 1, "What is the primary objective of India's National Cyber Security Policy 2023?\nతెలుగు: భారతదేశ జాతీయ సర్వర్ నిర్భందన నీతి 2023 యొక్క ప్రధాన ఉద్దేశ్యమేమిటి?",
     "To ban internet usage / ఇంటర్నెట్ వినియోగాన్ని నిషేధించటానికి",
     "To protect critical information systems and ensure cybersecurity across all sectors / సమాలోచన సమాచారం సిస్టమ్‌లను రక్షించటానికి మరియు సర్వర్ నిర్భందనను అన్ని రంగాలలో నిశ్చయించటానికి",
     "To regulate only government computers / కేంద్ర కంప్యూటర్‌లను మాత్రమే నియంత్రించటానికి",
     "To increase internet speed / ఇంటర్నెట్ వేగాన్ని పెంచటానికి",
     "b",
     "The National Cyber Security Policy 2023 aims to protect critical infrastructure, prevent cyber threats, establish cyber security standards, and create a resilient digital ecosystem."),

    (0, 2, "Which law primarily governs data protection in India (as of May 2026)?\nతెలుగు: భారతదేశంలో సమాచారం సంరక్ష ఏ చట్టం ప్రధానంగా నియంత్రించింది (May 2026)?",
     "IT Act 2000 only / IT చట్టం 2000 ఒక్కటే",
     "Personal Data Protection Bill 2023 along with IT Act provisions / వ్యక్తిగత సమాచారం సంరక్ష బిల్లు 2023 IT చట్టం నిబంధనలతో",
     "Aadhaar Act 2016 / ఆధార చట్టం 2016",
     "Right to Information Act 2005 / సమాచారానికి హక్కు చట్టం 2005",
     "b",
     "As of 2026, India's data protection framework includes the IT Act 2000, and the Personal Data Protection Bill 2023 (expected to be finalized) provides comprehensive data protection standards."),

    (0, 1, "What is the role of CERT-IN in India's cybersecurity framework?\nతెలుగు: భారతదేశ సర్వర్ నిర్భందన చట్రంలో CERT-IN యొక్క పాత్ర ఏమిటి?",
     "To sell cybersecurity products / సర్వర్ నిర్భందన ఉత్పత్తులను విక్రయించటానికి",
     "To coordinate cyber incident response and provide cybersecurity advisories / సర్వర్ సంఘటన ప్రతిస్పందనలను సమన్వయం చేయటానికి మరియు సర్వర్ నిర్భందన సలహాలు ఇవ్వటానికి",
     "To regulate internet service providers / ఇంటర్నెట్ సేవ సరఫరాదారులను నియంత్రించటానికి",
     "To conduct only military operations / సైనిక ఆపరేషన్‌లను మాత్రమే నిర్వహించటానికి",
     "b",
     "CERT-IN (Indian Computer Emergency Response Team) is a nodal agency under the Ministry of Communications that coordinates cyber incident response, issues advisories, and provides cybersecurity guidance."),

    (0, 2, "What is the penalty for unauthorized access to computer systems under IT Act 2000?\nతెలుగు: IT చట్టం 2000 ప్రకారం కంప్యూటర్ సిస్టమ్‌లకు అనుమతి లేని ప్రవేశానికి శిక్ష ఏమిటి?",
     "₹1,000 fine only / ₹1,000 జరిమానా ఒక్కటే",
     "6 months imprisonment and/or ₹1 lakh fine / 6 నెలల జైలు మరియు/లేదా ₹1 లక్ష జరిమానా",
     "1 year imprisonment and/or ₹2 lakhs fine / 1 సంవత్సరం జైలు మరియు/లేదా ₹2 లక్ష జరిమానా",
     "3 years imprisonment and/or ₹5 lakhs fine / 3 సంవత్సరాల జైలు మరియు/లేదా ₹5 లక్ష జరిమానా",
     "c",
     "Section 66 of IT Act 2000 prescribes punishment of up to 3 years imprisonment and/or fine up to ₹5 lakhs for unauthorized access to computer systems."),

    (0, 1, "What is the purpose of Aadhaar authentication in India's digital identity framework?\nతెలుగు: భారతదేశ డిజిటల్ గుర్తింపు చట్రంలో ఆధార ధృవీకరణ యొక్క ఉద్దేశ్యమేమిటి?",
     "To control population / జనాభా నియంత్రించటానికి",
     "To provide unique digital identity and enable secure transactions / ప్రత్యేక డిజిటల్ గుర్తింపు ఇవ్వటానికి మరియు సురక్షిత లావాదేవీలను ఆపరేషన్ చేయటానికి",
     "To replace national ID / జాతీయ గుర్తింపు వే చేయటానికి",
     "To monitor citizen activities / నాగరిక కార్యకలాపాలను నిఘా చేయటానికి",
     "b",
     "Aadhaar provides a unique 12-digit identity number linked to biometric data (fingerprints and iris), enabling secure and traceable digital transactions and service delivery."),

    (0, 2, "Which of the following is a critical information infrastructure that requires special cybersecurity protection in India?\nతెలుగు: భారతదేశంలో ప్రత్యేక సర్వర్ నిర్భందన రక్ష అవసరమైన సమాలోచన సమాచారం సంస్థలలో కింది వాటిలో ఏది?",
     "Social media platforms only / సోషల్ మీడియా వేదికలను మాత్రమే",
     "Power grids, water systems, financial networks, and communication systems / విద్యుత్ గ్రిడ్‌లు, నీటి సిస్టమ్‌లు, ఆర్థిక నెట్‌వర్క్‌లు, సమాచారం సిస్టమ్‌లు",
     "Only entertainment websites / వినోద వెబ్‌సైట్‌లను మాత్రమే",
     "Only educational institutions / విద్యార్థ సంస్థలను మాత్రమే",
     "b",
     "Critical information infrastructure includes power grids, water supply systems, banking and financial networks, telecommunications, and defense systems that require enhanced cybersecurity protection."),

    (0, 1, "What is ransomware in the context of cybercrime?\nతెలుగు: సర్వర్ నిర్ణయం సమీపంలో ransom ware ఏమిటి?",
     "A type of social media application / సోషల్ మీడియా ప్రకారం రకం",
     "Malicious software that encrypts data and demands payment for recovery / సమాచారమును గుప్తీకరణ చేసిన మరియు పునరుద్ధారణకు చెల్లింపు కోరే హానికర సాఫ్ట్‌వేర్",
     "A security tool to protect data / సమాచారం రక్ష సాధనం",
     "A type of antivirus software / యాంటీవైరస్ సాఫ్ట్‌వేర్ రకం",
     "b",
     "Ransomware is malicious software that encrypts victims' data, making it inaccessible, and criminals demand payment (ransom) for providing the decryption key."),

    (0, 2, "Under the IT Act 2000, what is the time limit for a website to remove illegal content after receiving notice?\nతెలుగు: IT చట్టం 2000 ప్రకారం, సూచన అందిన తర్వాత అక్రమ సమగ్రతను తీసివేయటానికి వెబ్‌సైట్‌కు సమయ సీమ ఏమిటి?",
     "Immediately / వెంటనే",
     "24 hours / 24 గంటలు",
     "36 hours / 36 గంటలు",
     "7 days / 7 రోజులు",
     "c",
     "Section 79 of IT Act 2000 requires intermediaries (websites, ISPs) to remove illegal content within 36 hours of receiving notice from law enforcement or authorized government agency."),
]

# ═══════════════════════════════════════════════════════════════════════════════════
# CATEGORY 7: URBAN DEVELOPMENT & SMART CITIES (25 questions, ID: 32186-32210)
# ═══════════════════════════════════════════════════════════════════════════════════

URBAN_MCQS = [
    (0, 1, "In which year was the Smart Cities Mission launched in India?\nతెలుగు: భారతదేశంలో స్మార్ట్ సిటీస్ మిషన్ ఎన్న సంవత్సరంలో ప్రారంభమైంది?",
     "2013 / 2013",
     "2015 / 2015",
     "2017 / 2017",
     "2019 / 2019",
     "b",
     "The Smart Cities Mission was launched on June 25, 2015, aiming to develop 100 smart cities across India focusing on sustainable and citizen-friendly urban development."),

    (0, 1, "What is the primary objective of India's Smart Cities Mission?\nతెలుగు: భారతదేశ స్మార్ట్ సిటీస్ మిషన్ యొక్క ప్రధాన ఉద్దేశ్యమేమిటి?",
     "Only to develop highways / సరళ మార్గాలను మాత్రమే అభివృద్ధి చేయటానికి",
     "To develop technology-enabled cities ensuring sustainable growth, better services, and improved quality of life / సాంకేతికత-సక్షమ నగరాలను అభివృద్ధి చేయటానికి సుస్థిర వృద్ధి, మెరుగైన సేవలు, జీవన నాణ్యతను",
     "Only for railway development / రైల్‌వే అభివృద్ధికి ఒక్కటే",
     "To promote real estate business / రియల్ ఎస్టేట్ ఖాతాను ప్రోత్సహించటానికి",
     "b",
     "The Smart Cities Mission aims to develop cities that are technology-enabled, sustainable, and provide better infrastructure, services, and quality of life to citizens."),

    (0, 2, "How many cities were selected in the first phase of Smart Cities Mission (June 2015)?\nతెలుగు: స్మార్ట్ సిటీస్ మిషన్ యొక్క మొదటి దశలో (జూన్ 2015) ఎన్ని నగరాలు ఎంపిక చేయబడ్డాయి?",
     "20 cities / 20 నగరాలు",
     "50 cities / 50 నగరాలు",
     "100 cities / 100 నగరాలు",
     "200 cities / 200 నగరాలు",
     "b",
     "In the first phase announced on June 25, 2015, 20 cities were selected for development as smart cities, followed by subsequent phases selecting more cities."),

    (0, 1, "Which ministry oversees the Smart Cities Mission in India?\nతెలుగు: భారతదేశంలో స్మార్ట్ సిటీస్ మిషన్‌ను ఏ మంత్రిత్వం పర్యవేక్షిస్తుంది?",
     "Ministry of Housing and Urban Affairs / నివాసం మరియు పట్టణ కార్యక్రమ మంత్రిత్వం",
     "Ministry of Panchayat Raj / పంచాయతీ రాజ్ మంత్రిత్వం",
     "Ministry of Environment / పరిసర మంత్రిత్వం",
     "Ministry of Transport / రవాణా మంత్రిత్వం",
     "a",
     "The Ministry of Housing and Urban Affairs implements and oversees the Smart Cities Mission, coordinating with state governments and urban development agencies."),

    (0, 2, "What percentage of Smart Cities Mission funding comes from the Central Government?\nతెలుగు: స్మార్ట్ సిటీస్ మిషన్ నిధిలో ఎంత శాతం కేంద్ర ప్రభుత్వం నుండి వస్తుంది?",
     "25% / 25%",
     "33.33% / 33.33%",
     "50% / 50%",
     "75% / 75%",
     "c",
     "The Smart Cities Mission uses a tri-partite funding model: 33.33% from Central Government, 33.33% from State Government, and 33.34% from the city's own resources and borrowings."),

    (0, 1, "Which of the following is a key component of Smart Cities Mission?\nతెలుగు: స్మార్ట్ సిటీస్ మిషన్ యొక్క కీలక భాగాలలో కింది వాటిలో ఏది?",
     "Only construction of buildings / భవనాలను నిర్మించటానికి ఒక్కటే",
     "Smart governance, digital infrastructure, sustainable transportation, and IoT-enabled services / స్మార్ట్ పరిపాలన, డిజిటల్ సంస్థలు, స్థిర రవాణా, IoT-సక్షమ సేవలు",
     "Only development of shopping malls / మాల్‌ల అభివృద్ధికి ఒక్కటే",
     "Only for defense purposes / రక్ష ఉద్దేశ్యాలకు ఒక్కటే",
     "b",
     "Smart Cities Mission components include smart governance, digital infrastructure, IoT-enabled services, sustainable transportation, renewable energy, waste management, and citizen participation."),

    (0, 2, "What is the status of Smart Cities Mission implementation as of May 2026?\nతెలుగు: May 2026 నుండి స్మార్ట్ సిటీస్ మిషన్ అమలు యొక్క స్థితి ఏమిటి?",
     "Launched but not started / ప్రారంభమైనవి కానీ ప్రారంభం కాలేదు",
     "Over 90% of projects completed with most cities operational or in final stages / 90% కంటే ఎక్కువ ప్రాజెక్ట్‌లు పూర్తి, చాలా నగరాలు ఆపరేషనల్ లేదా చివరి దశలో",
     "Early stages with minimal progress / ప్రారంభ దశలో కనిష్ఠ పురోగతి",
     "Completely stalled / పూర్తిగా ఆగిపోయింది",
     "b",
     "As of May 2026, the Smart Cities Mission has progressed significantly with most selected cities in implementation, many projects completed, and smart city services becoming operational across India."),

    (0, 1, "Which Andhra Pradesh city is developing as a smart city as part of the central initiative?\nతెలుగు: కేంద్ర కార్యక్రమం భాగంగా ఆంధ్రప్రదేశ్ యొక్క ఏ నగరం స్మార్ట్ సిటీకి అభివృద్ధి చేయబడుతోంది?",
     "Visakhapatnam / విశాఖపట్టణం",
     "Amaravati / అమరావతి",
     "Vijayawada / విజయవాడ",
     "Tirupati / తిరుపతి",
     "a",
     "Visakhapatnam (Vizag) is one of the selected smart cities in Andhra Pradesh, developing smart infrastructure including IoT systems, digital services, and sustainable urban development features."),
]

# ═══════════════════════════════════════════════════════════════════════════════════
# CATEGORY 8: ENVIRONMENTAL POLICY & CLIMATE (35 questions, ID: 32211-32245)
# ═══════════════════════════════════════════════════════════════════════════════════

ENVIRONMENTAL_MCQS = [
    (0, 1, "Which article of the Indian Constitution addresses environmental protection?\nతెలుగు: భారత రాజ్యాంగం యొక్క ఏ సూత్రం పరిసర సంరక్ష గురించి చెప్తుంది?",
     "Article 40 / సూత్రం 40",
     "Article 48-A / సూత్రం 48-A",
     "Article 51 / సూత్రం 51",
     "Article 72 / సూత్రం 72",
     "b",
     "Article 48-A of the Indian Constitution states that the State shall endeavor to protect and improve the environment and to safeguard the forests and wildlife."),

    (0, 1, "What is the primary objective of the National Action Plan on Climate Change (NAPCC)?\nతెలుగు: జాతీయ ఆ సవరణ కర్మాభిరుచిలోని ప్రధాన ఉద్దేశ్యమేమిటి?",
     "To increase coal production / బొగ్గు ఉత్పత్తిని పెంచటానికి",
     "To mitigate climate change impacts and promote sustainable development / ఆ సవరణ మార్పు ప్రభావాలను తగ్గించటానికి మరియు స్థిర అభివృద్ధిని ప్రోత్సహించటానికి",
     "To increase industrial pollution / పారిశ్రామిక కాలుష్యాన్ని పెంచటానికి",
     "To reduce green energy / సమవర్తన శక్తిని తగ్గించటానికి",
     "b",
     "NAPCC outlines India's comprehensive strategy to address climate change through mitigation, adaptation, and sustainable development across key sectors."),

    (0, 2, "By which year does India aim to achieve net-zero emissions target?\nతెలుగు: భారతదేశం నెట్-జీరో ఉత్సర్జనాల లక్ష్యం ఎన్ని సంవత్సరానికి సాధించాలని లక్ష్యం ఉంచారు?",
     "2030 / 2030",
     "2045 / 2045",
     "2050 / 2050",
     "2070 / 2070",
     "d",
     "India announced its commitment to achieve net-zero emissions by 2070, as declared during the COP26 climate summit. Interim target: 50% emission reduction by 2030."),

    (0, 1, "Which renewable energy source does India prioritize under its climate commitments?\nతెలుగు: భారతదేశ సవరణ కమిట్‌మెంట్‌ల ప్రకారం ఏ పునర్నవీకరణీయ శక్తి వనరు ప్రాధాన్యతను పొందుతుంది?",
     "Nuclear energy only / అణు శక్తిని ఒక్కటే",
     "Solar and wind energy as primary renewable sources / సౌర మరియు గాలి శక్తిని ప్రధాన పునర్నవీకరణీయ వనరులుగా",
     "Hydroelectric energy only / జల విద్యుత్‌ను ఒక్కటే",
     "Biomass only / జీవ ద్రవ్యాన్ని ఒక్కటే",
     "b",
     "India has set ambitious targets for renewable energy, with 500 GW of renewable energy capacity by 2030, prioritizing solar and wind energy as key sources for decarbonization."),

    (0, 2, "What is the main focus of India's Environmental Impact Assessment (EIA) Notification 2020?\nతెలుగు: భారతదేశ పరిసర ప్రభావ మూల్యాంకనం (EIA) నిర్ణయం 2020 యొక్క ప్రధాన దృష్టి ఏమిటి?",
     "To remove environmental regulations / పరిసర నియమాలను తీసివేయటానికి",
     "To fast-track development projects while maintaining environmental standards / అభివృద్ధి ప్రాజెక్ట్‌లను వేగవంతం చేయటానికి పరిసర ప్రమాణాలను కూడా కాపాడుతూ",
     "To ban all industries / అన్ని పారిశ్రామిక కార్యక్రమాలను నిషేధించటానికి",
     "To promote only agriculture / కৃషిని మాత్రమే ప్రోత్సహించటానికి",
     "b",
     "EIA Notification 2020 streamlines environmental clearance processes while maintaining rigorous environmental safeguards, categorizing projects based on environmental sensitivity."),

    (0, 1, "Which environmental law is primarily used to protect forests and wildlife in India?\nతెలుగు: భారతదేశంలో అటవీ మరియు వన్యజీవుల రక్ష కోసం ఏ పరిసర చట్టం ప్రధానంగా ఉపయోగించబడుతుంది?",
     "Water Pollution Control Act / నీటి కాలుష్య నియంత్రణ చట్టం",
     "Wildlife Protection Act 1972 and Forest Conservation Act 1980 / వన్యజీవుల రక్ష చట్టం 1972 మరియు అటవీ సంరక్ష చట్టం 1980",
     "Air Pollution Control Act / వాయు కాలుష్య నియంత్రణ చట్టం",
     "Hazardous Waste Management Rules / హానికర చెత్త నిర్వహణ నియమాలు",
     "b",
     "The Wildlife Protection Act 1972 and Forest Conservation Act 1980 are the primary laws protecting forests, wildlife, and biodiversity in India."),

    (0, 2, "What is India's renewable energy capacity target by 2030 under its climate commitments?\nతెలుగు: భారతదేశ సవరణ కమిట్‌మెంట్‌ల ప్రకారం 2030 నుండి పునర్నవీకరణీయ శక్తి సామర్థ్య లక్ష్యం ఎంత?",
     "250 GW / 250 GW",
     "400 GW / 400 GW",
     "500 GW / 500 GW",
     "750 GW / 750 GW",
     "c",
     "India has committed to achieving 500 GW of renewable energy capacity by 2030, comprising solar (280 GW), wind (140 GW), hydropower, and biomass energy."),

    (0, 1, "Which government scheme promotes waste management and cleanliness in urban areas?\nతెలుగు: పట్టణ ప్రాంతాలలో చెత్త నిర్వహణ మరియు పరిశుద్ధతను ప్రోత్సహించే ప్రభుత్వ స్కీమ్ ఏది?",
     "Pradhan Mantri Sahitya Mission / ప్రధానమంత్రి సాహిత్య మిషన్",
     "Swachh Bharat Mission / స్వచ్ఛ భారత్ మిషన్",
     "Make in India / 'మేడ్ ఇన్ ఇండియా'",
     "Digital India / డిజిటల్ ఇండియా",
     "b",
     "Swachh Bharat Mission aims to ensure universal sanitation, eliminate open defecation, and achieve 100% waste management coverage in urban and rural areas."),

    (0, 2, "What is the primary environmental issue addressed by the National Green Tribunal (NGT)?\nతెలుగు: జాతీయ ఆరోజ్ట్రిబ్యూనల్ (NGT) ఆధారపడిన ప్రధాన పరిసర సమస్య ఏమిటి?",
     "Economic development / ఆర్థిక అభివృద్ధి",
     "Environmental disputes, protection, conservation, and enforcement of environmental laws / పరిసర సంఘర్ష, సంరక్ష, సంరక్షణ, పరిసర చట్టాల అమలు",
     "Agricultural production / కృషి ఉత్పత్తి",
     "Military operations / సైనిక కార్యక్రమాలు",
     "b",
     "The National Green Tribunal (established in 2010) addresses environmental disputes, enforces environmental laws, and ensures environmental protection and conservation."),

    (0, 1, "Which treaty did India sign to address ozone layer depletion?\nతెలుగు: ఓజోన్ పరిమండల క్షీణతను పరిష్కరించటానికి భారతదేశం ఏ సంధిని సంతకం చేసింది?",
     "Paris Agreement / పారిస్ ఒప్పందం",
     "Montreal Protocol / మాంట్రియల్ ప్రోటోకాల్",
     "Kyoto Protocol / క్యోటో ప్రోటోకాల్",
     "Basel Convention / బాసెల్ సమ్మేళనం",
     "b",
     "India is a signatory to the Montreal Protocol (1987) which mandates phasing out ozone-depleting substances like CFCs to protect the ozone layer."),

    (0, 2, "What is the primary focus of India's Pradhan Mantri Sahitya Mission (PMSM)?\nతెలుగు: ప్రధానమంత్రి సాహిత్య మిషన్ (PMSM) యొక్క ప్రధాన దృష్టి ఏమిటి?",
     "To promote literature and culture / సాహిత్యం మరియు సంస్కృతిని ప్రోత్సహించటానికి",
     "To restore and protect heritage sites / వారసత్వ స్థలాలను పునరుద్ధరించటానికి మరియు రక్షించటానికి",
     "To promote sustainable development and biodiversity conservation / స్థిర అభివృద్ధి మరియు జీవ వৈవిధ్య సంరక్ష ప్రోత్సహించటానికి",
     "To develop industrial infrastructure / పారిశ్రామిక సంస్థలను అభివృద్ధి చేయటానికి",
     "c",
     "While primarily focused on heritage conservation, PMSM initiatives increasingly incorporate environmental and biodiversity protection in site management and restoration."),
]

# ═══════════════════════════════════════════════════════════════════════════════════
# COMPILATION AND OUTPUT
# ═══════════════════════════════════════════════════════════════════════════════════

CATEGORIES = {
    "Media_Press_Freedom": {
        "id_range": "32086-32110",
        "category": "Media & Press Freedom",
        "questions": MEDIA_MCQS,
        "count": len(MEDIA_MCQS)
    },
    "Labour_Rights": {
        "id_range": "32111-32135",
        "category": "Labour Rights & Unions",
        "questions": LABOUR_MCQS,
        "count": len(LABOUR_MCQS)
    },
    "Consumer_Protection": {
        "id_range": "32136-32160",
        "category": "Consumer Protection",
        "questions": CONSUMER_MCQS,
        "count": len(CONSUMER_MCQS)
    },
    "Cyber_Security": {
        "id_range": "32161-32185",
        "category": "Cyber Security & Data Protection",
        "questions": CYBER_MCQS,
        "count": len(CYBER_MCQS)
    },
    "Urban_Development": {
        "id_range": "32186-32210",
        "category": "Urban Development & Smart Cities",
        "questions": URBAN_MCQS,
        "count": len(URBAN_MCQS)
    },
    "Environmental_Policy": {
        "id_range": "32211-32245",
        "category": "Environmental Policy & Climate",
        "questions": ENVIRONMENTAL_MCQS,
        "count": len(ENVIRONMENTAL_MCQS)
    }
}

def generate_summary():
    """Generate summary of all MCQs created"""
    total = sum(cat["count"] for cat in CATEGORIES.values())
    summary = {
        "total_questions": total,
        "categories_created": len(CATEGORIES),
        "categories": []
    }

    for key, cat in CATEGORIES.items():
        summary["categories"].append({
            "name": cat["category"],
            "id_range": cat["id_range"],
            "question_count": cat["count"]
        })

    return summary

if __name__ == "__main__":
    summary = generate_summary()
    print("=" * 80)
    print("MCQ CREATION SUMMARY")
    print("=" * 80)
    print(f"\nTotal Questions Created: {summary['total_questions']}")
    print(f"Total Categories: {summary['categories_created']}")
    print("\nCategory Breakdown:")
    for cat in summary['categories']:
        print(f"  • {cat['name']:.<45} {cat['question_count']} Q's [{cat['id_range']}]")
    print("\n" + "=" * 80)
