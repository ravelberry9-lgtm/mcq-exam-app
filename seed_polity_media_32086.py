# -*- coding: utf-8 -*-
# Indian Polity — CATEGORY 3: Media & Press Freedom (మీడియా & ప్రెస్ స్వేచ్ఛ)
# Press Freedom · Media Regulation · Defamation Law · Right to Information · News Media Policies
# MCQ ID Range: 32086-32110 (25 questions)

import json as _json

POLITY_MEDIA_SECTIONS = [
    {"title": "3.1 ప్రెస్ స్వేచ్ఛ మరియు రాజ్యాంగ సంరక్ష",
     "sub": "Article 19 · Constitutional Protections · Court Judgments · Press Council · Democratic Rights",
     "audio": """ప్రెస్ స్వేచ్ఛ = ప్రజాస్వామిక చేపట్టుకోవటానికి ఊహ, తెలుసుకోవటానికి, సంభాషణ చేయటానికి హక్కు.

📌 రాజ్యాంగ సంరక్ష:
• Article 19(1)(a): ప్రసంగ స్వేచ్ఛ మరియు సమాచారం స్వేచ్ఛ
• Article 19(2): సమర్థించిన నిబంధనలు (రాష్ట్ర సంరక్ష, సందర్భం, చట్టపరమైన నియమాలు)
• ఉమ్మడి నుండి అంచెలు (Reasonable Restrictions)

📌 కీలక న్యాయ నిర్ణయాలు:
• నిరూద్ధ భారత సమాచారం కేసు: సమాచారం స్వేచ్ఛ = జనతా హక్కు
• ప్రెస్ కౌన్సిల్ నిర్ణయాలు: సమాచారం సమర్థన చేయటానికి రుంధుకోవటం కానీ పరిమితం
• అయోధ్య చేపట్టుకోవటం = ఇచ్ఛాధారిత ఎన్నిక న్యాయం

📌 May 2026 సమీక్ష:
• ডిజిటల్ మీడియా వేదికలపై సమాచారం నియంత్రణ = బలుతుంది
• నకలీ సమాచారం నిరసన చట్టాలు = విస్తరిస్తోంది""",
    },
]

POLITY_MEDIA_MCQS = [
    (0, 1, "Which article of the Indian Constitution protects Press Freedom?\nతెలుగు: భారత రాజ్యాంగం యొక్క ఏ సూత్రం మీడియా స్వేచ్ఛను రక్షిస్తుంది?",
     "Article 16 / సూత్రం 16", "Article 19(1)(a) / సూత్రం 19(1)(a)", "Article 25 / సూత్రం 25", "Article 32 / సూత్రం 32", "b",
     "Article 19(1)(a) guarantees freedom of speech and expression to all citizens, which forms the foundation of press freedom under Indian Constitution."),

    (0, 1, "What is the primary role of the Press Council of India?\nతెలుగు: ప్రెస్ కౌన్సిల్ ఆఫ్ ఇండియా యొక్క ప్రధాన పాత్ర ఏది?",
     "To regulate broadcasters", "To ensure press ethics and redress grievances", "To grant licenses to newspapers", "To control media content", "b",
     "Press Council of India (established 1966) upholds press freedom, maintains journalism standards, and addresses complaints against press."),

    (0, 2, "Which law primarily governs defamation in media matters?\nతెలుగు: మీడియా సంబంధిత అపవాద చట్టాలు ఏ చట్టం ద్వారా నియంత్రణలో ఉన్నాయి?",
     "Information Technology Act 2000", "Press Council Act 1978", "Indian Penal Code (Sections 499-500)", "Contempt of Court Act", "c",
     "Sections 499-500 of IPC define defamation and prescribe punishment up to 2 years imprisonment and/or fine."),

    (0, 2, "What is the main objective of the Digital Security Act in India (as of May 2026)?\nతెలుగు: భారతదేశంలో డిజిటల్ సిక్యూరిటీ చట్టం యొక్క ప్రధాన ఉద్దేశ్యమేమిటి?",
     "To ban all social media platforms", "To regulate digital content and protect cybersecurity", "To promote digital media only", "To eliminate fake news completely", "b",
     "Digital security legislation regulates digital content, protects data, prevents cybercrime while maintaining free speech principles."),

    (0, 1, "Which Right to Information mechanism ensures transparency in media operations?\nతెలుగు: సమాచారానికి హక్కు కట్టడం ఏ విధానం మీడియా కార్యకలాపాలలో పారదర్శకతను నిశ్చయిస్తుంది?",
     "Right to Information Act 2005", "Press Council Regulations", "Broadcast Code", "Media Commission Report", "a",
     "RTI Act 2005 applies to public authorities and ensures transparency in government operations impacting media reporting."),

    (0, 2, "What is the maximum punishment for contempt of court through media reporting?\nతెలుగు: మీడియా నివేదన ద్వారా న్యాయాలయ అవమానంకు గరిష్ఠ శిక్ష ఏమిటి?",
     "6 months imprisonment and/or ₹1,000 fine", "1 year imprisonment and/or ₹5,000 fine", "2 years imprisonment and/or ₹10,000 fine", "3 years imprisonment and/or ₹50,000 fine", "b",
     "Under Contempt of Court Act 1971, civil contempt attracts 6 months and ₹2,000 fine; criminal contempt up to 2 years or ₹10,000."),

    (0, 1, "Which organization regulates broadcast media (TV and Radio) in India?\nతెలుగు: భారతదేశంలో ప్రసారణ మీడియా (టీవీ మరియు రేడియో) నియంత్రణ ఏ సంస్థ చేసుతుంది?",
     "Press Council of India", "Ministry of Information and Broadcasting", "Broadcasting Regulation Authority (BRA)", "Information Commission", "c",
     "Broadcasting Regulation Authority oversees TV channels and radio stations' compliance with content standards and advertising codes."),

    (0, 2, "What does the Broadcast Code regulate in India?\nతెలుగు: భారతదేశంలో ప్రసారణ సంహితా ఏ విషయాలను నియంత్రించింది?",
     "Only news programming", "Only entertainment content", "News, entertainment, and advertising content on broadcast media", "Only political content", "c",
     "Broadcast Code regulates content standards for news, entertainment, and advertising on television and radio channels."),

    (0, 1, "In which year was the Press Council of India established?\nతెలుగు: ప్రెస్ కౌన్సిల్ ఆఫ్ ఇండియా ఎన్న సంవత్సరంలో ఏర్పాటు చేయబడింది?",
     "1960 / 1960", "1966 / 1966", "1972 / 1972", "1980 / 1980", "b",
     "Press Council of India was established in 1966 as a quasi-judicial body to safeguard press freedom and maintain journalism standards."),

    (0, 2, "What is the significance of the 'Right to Information' to media organizations?\nతెలుగు: 'సమాచారానికి హక్కు' మీడియా సంస్థలకు ఎటువంటి ప్రాముఖ్యత ఉంది?",
     "To increase government advertisements", "To access public information and hold government accountable to citizens", "To control private businesses", "To determine newspaper circulation", "b",
     "RTI enables media to access government documents and information, enabling investigative journalism and promoting government accountability."),

    (0, 1, "What is the role of the Information Commission in India?\nతెలుగు: సమాచారం కమిషన్ భారతదేశంలో ఏ పాత్ర పోషిస్తుంది?",
     "To regulate media outlets", "To enforce RTI Act and handle RTI appeals", "To control publishing", "To manage government secrets", "b",
     "Information Commissions (Central and State) handle RTI applications, appeals, and ensure public access to government information."),

    (0, 2, "Which of the following is an example of 'reasonable restrictions' on press freedom in India?\nతెలుగు: భారతదేశంలో ప్రెస్ స్వేచ్ఛకు 'సమర్థించిన నిబంధనలు' యొక్క ఉదాహరణ ఏది?",
     "Banning all newspapers", "Restrictions to protect national security or public order", "Stopping all publications", "Controlling all media", "b",
     "Article 19(2) permits reasonable restrictions on press freedom for national security, public order, decency, morality, etc."),

    (0, 1, "What is the main difference between Press Council and Broadcasting Regulation Authority?\nతెలుగు: ప్రెస్ కౌన్సిల్ మరియు ప్రసారణ నియమన సంస్థ మధ్య ప్రధాన వ్యత్యాసం ఏమిటి?",
     "Both are identical", "Press Council regulates print media; Broadcasting Authority regulates electronic media", "Press Council controls politics", "Broadcasting Authority manages newspapers", "b",
     "Press Council oversees print media (newspapers, magazines); Broadcasting Authority regulates TV and radio broadcasting standards."),

    (0, 2, "What is the punishment for publishing seditious material under the Penal Code?\nతెలుగు: శిక్ష సంహితా కింద తిరుగుబాటు సంబంధిత సమగ్రత ప్రకటించటానికి శిక్ష ఏమిటి?",
     "₹500 fine only", "Up to 7 years imprisonment and/or fine", "1 year imprisonment", "No punishment", "b",
     "Section 124A IPC (sedition) prescribes punishment up to 7 years imprisonment and/or fine for seditious publications."),

    (0, 1, "Which section of IT Act 2000 deals with obscene content online?\nతెలుగు: IT చట్టం 2000 యొక్క ఏ సెక్షన్ ఆన్‌లైన్ అసభ్య సమగ్రతను కవర్ చేస్తుంది?",
     "Section 66", "Section 67", "Section 68", "Section 69", "b",
     "Section 67 IT Act 2000 penalizes publication or transmission of obscene material over the internet with up to 3 years imprisonment."),

    (0, 2, "What is the responsibility of media regarding 'hate speech' in India?\nతెలుగు: భారతదేశంలో 'వ్యతిరేక ప్రసంగం' విషయంలో మీడియా యొక్క బాధ్యత ఏమిటి?",
     "To promote hate speech freely", "To prevent dissemination and report to authorities; can face legal consequences", "To stay silent", "To amplify such content", "b",
     "Media has responsibility to prevent hate speech dissemination; violations lead to prosecution under various laws including IPC, IT Act, and broadcast codes."),

    (0, 1, "What is the purpose of the 'Model Code of Conduct' for election coverage?\nతెలుగు: ఎన్నికల నివేదనకు 'నమూనా నిర్దేశన సంహితా' యొక్క ఉద్దేశ్యమేమిటి?",
     "To control media completely", "To ensure fair, balanced, and impartial coverage during elections", "To promote specific parties", "To reduce news coverage", "b",
     "Model Code of Conduct ensures equitable media coverage, prevents bias, and maintains level playing field for all candidates during elections."),

    (0, 2, "What action can be taken against a newspaper that violates Press Council norms?\nతెలుగు: ప్రెస్ కౌన్సిల్ నిబంధనలను ఉల్లంఘించే వార్తాపత్రికకు ఏ చర్య తీసుకోవచ్చు?",
     "Imprisonment of editors", "Warning, reprimand, or published apology; compensation for injured persons", "Immediate closure", "No action possible", "b",
     "Press Council can issue warnings, reprimands, recommend published apologies, and award compensation to aggrieved individuals against media violations."),

    (0, 1, "What does 'yellow journalism' mean in media context?\nతెలుగు: మీడియా సందర్భంలో 'yellow journalism' అంటే ఏమి?",
     "News printed on yellow paper", "Sensationalized reporting to boost circulation without factual accuracy", "Government-controlled media", "Online journalism", "b",
     "Yellow journalism refers to sensationalized, exaggerated, or false reporting prioritizing sales over accuracy and facts."),

    (0, 2, "What is 'self-regulation' in media and why is it important?\nతెలుగు: మీడియాలో 'స్వీయ-నియంత్రణ' అంటే ఏమి మరియు ఇది ఎందుకు ముఖ్యం?",
     "Government controlling all media", "Media industry establishing its own ethical standards and monitoring compliance; important for credibility and freedom", "Reducing news coverage", "Ignoring public complaints", "b",
     "Self-regulation through press councils and codes enables media to maintain standards, credibility, and independence from external control."),

    (0, 1, "Which government ministry oversees media regulation in India?\nతెలుగు: భారతదేశంలో మీడియా నియంత్రణను ఏ ప్రభుత్వ మంత్రిత్వం పర్యవేక్షిస్తుంది?",
     "Ministry of Defence", "Ministry of Information and Broadcasting", "Ministry of Home Affairs", "Ministry of External Affairs", "b",
     "Ministry of Information and Broadcasting (I&B) regulates media, broadcasting, films, and press in India."),

    (0, 2, "What is the legal recourse for a person defamed by media content?\nతెలుగు: మీడియా సమగ్రత ద్వారా అపవాద చేయబడిన వ్యక్తికి చట్టపరమైన ప్రతిఉపాయం ఏమిటి?",
     "No recourse available", "File defamation case under IPC Sections 499-500; seek damages from media organization", "Public apology only", "Media will always correct itself", "b",
     "Defamed persons can file civil defamation suits for damages and/or criminal cases under IPC seeking compensation and punishment."),

    (0, 1, "What is the constitutional status of Right to Information?\nతెలుగు: సమాచారానికి హక్కు యొక్క రాజ్యాంగ స్థితి ఏమిటి?",
     "Not a constitutional right", "Part of Article 19(1)(a) freedom of expression", "Only a statutory right", "Depends on government permission", "b",
     "Right to Information is inherent in Article 19(1)(a) and was formalized through RTI Act 2005 implementing constitutional freedom."),

    (0, 2, "What are the consequences of media non-compliance with information security norms?\nతెలుగు: సమాచారం సిక్యూరిటీ నిబంధనలకు మీడియా సమతకు పరిణామాలు ఏమిటి?",
     "No consequences", "Legal penalties, fines, imprisonment, and civil action under IT Act and other laws", "Just a warning letter", "Loss of circulation only", "b",
     "Media non-compliance with data protection and security norms can result in prosecution under IT Act, with fines and imprisonment up to 3 years."),
]

def get_polity_media_mcqs():
    return {
        "category": "Media & Press Freedom",
        "category_id": 3,
        "total_questions": len(POLITY_MEDIA_MCQS),
        "id_range": "32086-32110",
        "exam_level": "APPSC Group 2 / UPSC CSE",
        "language": "Bilingual (Telugu-English)",
        "sections": POLITY_MEDIA_SECTIONS,
        "mcqs": POLITY_MEDIA_MCQS
    }

if __name__ == "__main__":
    data = get_polity_media_mcqs()
    print(_json.dumps(data, ensure_ascii=False, indent=2))
