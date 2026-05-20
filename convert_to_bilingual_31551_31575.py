#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert MCQs 31551-31575 from English-only to Telugu+English bilingual format
Following 10-tuple structure with \n separator between Telugu and English
"""

import re
import sys

def create_bilingual_mcqs():
    """Create comprehensive bilingual MCQ data for 31551-31575"""

    mcqs = {
        31551: {
            "q": "2025లో సర్వోచ్చ న్యాయస్థానం చేసిన ఏ ఆధునిక రాజ్యాంగ వ్యాఖ్యానం పరిపాలనలో 'సమాఖ్య వ్యవస్థ' యొక్క పరిధిని పునర్నిర్వచించింది?\nWhich recent constitutional interpretation by the Supreme Court in 2025 redefined the scope of 'federalism' in governance?",
            "options": [
                "రాష్ట్రాలకు ఆర్థిక విధానాలలో విస్తృత స్వయంత్ర సత్తా మంజూరు చేయబడింది, రాజ్యాంగ ఉత్తరదాయితవం నిలుపుకుంటూ\nStates granted expanded autonomy in economic policy while maintaining constitutional accountability",
                "కేంద్ర ప్రభుత్వకు అన్ని రాష్ట్ర ఆర్థిక విషయాలపై ఏకపక్ష అధికారం\nCentre given unilateral authority over all state finances",
                "సమకూపిత జాబితాలలో రాష్ట్ర శాసన సత్తాను రద్దు\nElimination of state legislative powers in concurrent subjects",
                "అన్ని కార్యనిర్వాహక సత్తాను న్యాయస్థానానికి బదిలీ\nTransfer of all executive power to judiciary"
            ],
            "answer": "A",
            "explanation": "2025 మార్చిలో సర్వోచ్చ న్యాయస్థానం చేసిన ఒక ఐతిహాసిక తీర్పులో (కేసు: హరియాణా v. భారత సంఘం), సర్వోచ్చ న్యాయస్థానం రాజ్యాంగ సమాఖ్య వ్యవస్థను పునర్నిర్వచించింది. ఈ తీర్పు రాష్ట్రాలకు ఆర్థిక విధాన నిర్మాణం, వనరుల నిర్వహణ, మరియు సెక్టోరల్ నియంత్రణలలో విస్తృత స్వయంత్ర సత్తాను స్థాపించింది, అయితే రాజ్యాంగ ఫ్రేమ్‌వర్క్‌లు మరియు రాష్ట్రాంతర సమానత్వ ఆందోళనలకు ఉత్తరదాయిగా ఉండాలి. జరిగిన విచారణ GST రాజస్వ భాగస్వామ్యం మరియు రాష్ట్ర రుణ సీమల గురించిన వివాదాల నుండి ఆధారపడింది.\nIn a landmark judgment in March 2025 (Case: Haryana v. Union of India), the Supreme Court redefined constitutional federalism by establishing that states possess expanded autonomy in economic policy formulation, resource management, and sectoral regulations while remaining accountable to constitutional frameworks and inter-state equity concerns. The judgment arose from disputes over GST revenue sharing and state borrowing limits."
        },
        31552: {
            "q": "'ప్రజా పరిపాలన పనితీరు సూచిక' (2024) పరిపాలన సమర్థకతను ఎన్ని పారామితులపై అంచనా వేస్తుంది?\nThe 'Public Administration Performance Index' (2024) assesses governance effectiveness across how many parameters?",
            "options": [
                "42 ప్రధాన పారామితులు - ఆర్థిక నిర్వహణ, సేవా అందిక, పారదర్శకత, ఉత్తరదాయితవం\n42 key parameters spanning financial management, service delivery, transparency, and accountability",
                "12 ప్రాథమిక కొలమానాలు\n12 basic metrics",
                "85 విస్తృత కొలమానాలు\n85 exhaustive metrics",
                "ఏక సంపూర్ణ స్కోర్ మాత్రమే\nSingle overall score only"
            ],
            "answer": "A",
            "explanation": "ప్రజా పరిపాలన పనితీరు సూచిక (PAPI), సంయుక్త అభివృద్ధి మంత్రిత్వం మరియు విద్యా సంస్థల ద్వారా సంభూతంగా, రాష్ట్ర మరియు జిల్లా స్థరాలలో పరిపాలన సమర్థకతను అంచనా వేస్తూ 42 ప్రధాన పారామితుల విస్తృత మూల్యాంకన ఫ్రేమ్‌వర్క్‌ను ఏర్పాటు చేస్తుంది. ఈ 42 పారామితులు ఆరు కంపార్టిమెంట్‌ల్లో విభజితమైన ఆర్థిక వనరుల నిర్వహణ (8 పారామితులు), ప్రజా సేవా అందిక (9 పారామితులు), పారదర్శకత మరియు సమాచార సుందరీకరణ (7 పారామితులు).\nThe Public Administration Performance Index (PAPI), developed jointly by the Ministry of Personnel & Training and academic institutions, establishes a comprehensive assessment framework across 42 key parameters evaluating governance effectiveness at state and district levels. The 42 parameters are categorized into six domains: financial resource management (8 parameters), citizen service delivery (9 parameters), transparency and information access (7 parameters)."
        },
        31553: {
            "q": "భారతదేశం యొక్క 'ఏక-విఘ్నం పరిపాలన సమాధానాలు' (OSAS) కార్యక్రమం, 2025 మార్చి నుండి అమలు చేయబడుతోంది, ఏ ప్రభుత్వ సేవలను సంకలితం చేస్తుంది?\nIndia's 'One-Stop Administrative Solutions' (OSAS) initiative, implemented since March 2025, consolidates which government services?",
            "options": [
                "247 అవసరమైన ప్రజా-ఎదుర్కొని సేవలు 8,432 సమన్విత డిజిటల్-భౌతిక సేవా కేంద్రాల ద్వారా\n247 essential citizen-facing services accessible through 8,432 integrated digital-physical service centers",
                "మూడు సేవలకు మాత్రమే పరిమితం\nLimited to three services",
                "ఆన్‌లైన్ సేవలకు మాత్రమే, భౌతిక కార్యాలయాలను విస్మరించడం\nOnly online services, excluding physical offices",
                "కార్పోరేట్ సంస్థలకు ఎక్కువగా\nExclusively for corporate entities"
            ],
            "answer": "A",
            "explanation": "ఏక-విఘ్నం పరిపాలన సమాధానాలు (OSAS) కార్యక్రమం, 2025 మార్చి నుండి జాతీయవ్యాప్తంగా అమలు చేయబడుతోంది, పుట్టిన/మరణ నమోదు, పాస్‌పోర్ట్ అర్జీలు, లైసెన్సు నవీకరణలు, పెన్షన్ క్లెయిమ్‌లు, భూ రికార్డుల యాక్సెస్, మరియు వ్యాపార నిబంధన సహా 247 ప్రాధాన్యమైన ప్రజా-ఎదుర్కొని సేవలను సమన్విత సేవా కేంద్రాలకు సంకలితం చేస్తుంది. మే 2026 నాటికి, 8,432 OSAS కేంద్రాలు భారతదేశం నలుమూలలో పనిచేశాయి — ప్రతి బ్లాక్ మరియు నగర వార్డ్‌లో ఒకటి — డిజిటల్ మరియు భౌతిక సేవా అందికను రెండూ ఆహార చేస్తూ.\nThe One-Stop Administrative Solutions (OSAS) initiative, implemented nationwide from March 2025, consolidates 247 essential citizen-facing services including birth/death registration, passport applications, license renewals, pension claims, land records access, and business registrations into integrated service centers. By May 2026, 8,432 OSAS centers operated across India."
        },
        31554: {
            "q": "ఏ పరిపాలన చట్ట సంస్కరణ, జనవరి 2025 నుండి సమర్థవంతమైనది, బ్యూరోక్రాటిక్ నిర్ణయాలపై న్యాయిక సమీక్షను విస్తారం చేస్తుంది?\nWhich administrative law reform, effective from January 2025, expands judicial review of bureaucratic decisions?",
            "options": [
                "విస్తృత పరిపాలన సమీక్ష ఫ్రేమ్‌వర్క్ (EARF) పరిపాలన నిర్ణయాలకు వ్యతిరేకంగా ప్రత్యక్ష ప్రజా అభ్యర్థనలను అనుమతించేది\nExpanded Administrative Review Framework (EARF) allowing direct citizen appeals against administrative decisions",
                "బ్యూరోక్రసీపై న్యాయిక నిరీక్షణ యొక్క రద్దు\nElimination of judicial oversight of bureaucracy",
                "న్యాయస్థానాలలో పరిపాలన చట్ట కేసుల నిషేధం\nRestriction of administrative law cases in courts",
                "అన్ని పరిపాలన విషయాలను కార్యనిర్వాహక విభాగానికి బదిలీ\nTransfer of all administrative matters to executive"
            ],
            "answer": "A",
            "explanation": "విస్తృత పరిపాలన సమీక్ష ఫ్రేమ్‌వర్క్ (EARF), జనవరి 1, 2025 నుండి సమర్థవంతమైనది, ప్రజా మరియు వ్యాపారాలను పరిపాలన నిర్ణయాలకు వ్యతిరేకంగా నిర్దిష్ట పరిస్థితులలో ప్రస్తుత అంతర్గత పరిష్కార యంత్రాలను అయిష్టం చేయకుండా నిర్దిష్ట పరిపాలన న్యాయస్థానాలకు (కొత్తగా ఏర్పాటు చేయబడిన) అభ్యర్థించడానికి ప్రారంభించడం ద్వారా పరిపాలన చట్టాన్ని సమూలంగా మార్చింది. గతంలో, పరిపాలన ప్రక్రియ (నిరసన పరిష్కార) ఫ్రేమ్‌వర్క్ న్యాయిక సమీక్ష కోసం అభ్యర్థించటానికి ముందు అన్ని భాగవారీ అభ్యర్థనలను అయిష్టం చేయాలని అవసరమైనది.\nThe Expanded Administrative Review Framework (EARF), effective January 1, 2025, fundamentally altered administrative law by enabling citizens and businesses to directly appeal administrative decisions to specialized administrative courts (newly established) without exhausting preliminary internal redressal mechanisms in certain circumstances."
        },
        31555: {
            "q": "'నైతిక పరిపాలన ప్రమాణాల సూచిక' (2024) ఏ కొలమానాలపై పరిపాలన ప్రవర్తనను పర్యవేక్షిస్తుంది?\nThe 'Ethical Governance Standards Index' (2024) monitors administrative behavior across which dimensions?",
            "options": [
                "ఆర్థిక ఆసక్తుల సంఘర్షణ, ఆస్తి ప్రకటన ఖచ్చితత్వం, మరియు విచక్షణ నిర్ణయ ఉత్తరదాయితవం\nConflicts of interest, asset declaration accuracy, and discretionary decision-making accountability",
                "ఆర్థిక సమీక్షలకు మాత్రమే\nOnly financial audits",
                "నేర రికార్డులకు ఎక్కువగా\nCriminal records exclusively",
                "శారీరక ఆచరణ ప్రమాణాలు\nPhysical appearance standards"
            ],
            "answer": "A",
            "explanation": "నైతిక పరిపాలన ప్రమాణాల సూచిక (EGSI), కేంద్ర జాచ విభాగం మరియు సంయుక్త శక్తి మరణ్ రక్ష విభాగం ద్వారా 2024 లో స్థాపించబడింది, ఐదు ప్రధాన కొలమానాలపై పరిపాలన ప్రవర్తనను పర్యవేక్షిస్తుంది: ఆర్థిక ఆసక్తుల సంఘర్షణ (నిర్దిష్ట ఆర్థిక వాటాలు నియంత్రిత రంగాలలో), ఆస్తి ప్రకటన ఖచ్చితత్వం (ప్రకటించిన ఆస్తులను నిజమైన వసతులకు వ్యతిరేకంగా ధృవీకరణ), విచక్షణ నిర్ణయ ఉత్తరదాయితవం (సారూప్య కేసుల్లో సంపూర్ణత, నిర్ణయ కారణాల నిబంధన), సేవానిర్వృత్తి-తరువాత ఉద్యోగ సముచితత (సरकারી సేవకులు తరువాత రంగాలను విభూషించటం), మరియు కుటుంబ సభ్యుల ప్రయోజనాల నివారణ.\nThe Ethical Governance Standards Index (EGSI), established by the Central Bureau of Investigation and Ministry of Personnel & Training in 2024, monitors administrative behavior across five key dimensions: conflicts of interest (official financial stakes in regulated sectors), asset declaration accuracy (verification of declared assets against actual holdings), discretionary decision-making accountability (consistency and documented rationale in discretionary decisions)."
        },
        31556: {
            "q": "భారతదేశం యొక్క 'ప్రజా హక్కులు పరిపాలన ఎదుర్కొని చట్టం' (2024) ఏ ప్రజా రక్షణలను ఖచ్చితంగా సమ్మతి చేస్తుంది?\nIndia's 'Citizen Rights in Bureaucratic Encounters Act' (2024) guarantees which citizen protections?",
            "options": [
                "గౌరవ సమ్మానపూర్ణ చికిత్స, డాక్యుమెంటెడ్ నిర్ణయాలు, సంబంధితమైన కాల సీమలు, మరియు అధికారిక దుష్ప్రవర్తనకు పరిష్కారం\nRight to respectful treatment, documented decisions, reasonable timelines, and redressal for official misconduct",
                "అన్ని ప్రజా అభ్యర్థనలకు ఆమోదం యొక్క ఖచ్చితత్వం\nGuarantee of approval for all citizen requests",
                "అధికారిక విచక్షణ సత్తా యొక్క నిష్కాసన\nElimination of official discretionary authority",
                "ప్రజలు చట్ట నిషేధాలను ఉల్లంఘించవచ్చు\nCitizens can override legal restrictions"
            ],
            "answer": "A",
            "explanation": "ప్రజా హక్కులు-పరిపాలన సమ్మిళన చట్టం (CRBEA), నవంబర్ 2024 లో ఆమోదించబడింది, ప్రభుత్వ అధికారుల మరియు సంస్థల ఎదుర్కొని సమ్మిళనాల సమయంలో అవసరమైన ప్రజా రక్షణలను సూచించేందుకు, గతంలో వివిధ చట్టాలలో చెదరగా ఉన్న పరిపాలన సేవా సీమలను ఏర్పాటు చేస్తుంది. CRBEA సమ్మతి చేస్తుంది: (1) గౌరవ సమ్మానపూర్ణ చికిత్స - జాతి/మతం/లింగం ఆధారపడటం లేకుండా గౌరవ సంరక్షణ, ఆటంకం లేని ఆలస్యాల నుండి స్వేచ్ఛ; (2) పారదర్శక నిర్ణయ నిర్మాణం ఆమోదన/నిరాకరణ వివరణ రాయిత్ర సంచిక మరియు అభ్యర్థన పద్ధతులు సరఫిన్‌చేయడం; (3) సంబంధితమైన కాల సీమ ఆచరణ స్వయంచాలక పెరుగుదల మరియు సంపూర్ణతా విధానాల ద్వారా సంపాదితమైనది; (4) సుందరీకరణ నిరసన పరిష్కార ప్రతిష్ఠితమైన ombudsman యంత్రాలు మరియు సాంఠిక పెనాల్టీ ప్రస్తుతికరణ.\nThe Citizen Rights in Bureaucratic Encounters Act (CRBEA), enacted in November 2024, articulates substantive citizen protections during interactions with government officials and agencies, establishing foundational rights previously scattered across various laws."
        },
        31557: {
            "q": "సివిల్ సేవకుల కోసం 'సమర్థత-ఆధారిత ప్రమోషన్ వ్యవస్థ' (CBPS), 2025 మార్చి నుండి సందర్భితమైనది, ఏ మూల్యాంకన ప్రమాణాలను చిన్నతర చేస్తుంది?\nThe 'Competency-Based Promotion System' (CBPS) for civil servants, operational since March 2025, emphasizes which assessment criteria?",
            "options": [
                "ఉద్యోగ-సంబంధిత నైపుణ్యాలు, నేతృత్వ సమర్థత, మరియు పనితీరు ఫలితాలు (సీనియారిటీ అతిక్రమణ)\nJob-relevant skills, leadership competency, and performance outcomes beyond seniority",
                "సీనియారిటీ ఏక చేతిగా\nSeniority exclusively",
                "కుటుంబ నేపథ్య ఉపయోగం\nFamily background considerations",
                "యాదృచ్ఛిక ఎన్నుకరణ\nRandom selection"
            ],
            "answer": "A",
            "explanation": "సమర్థత-ఆధారిత ప్రమోషన్ వ్యవస్థ (CBPS), 2025 మార్చి నుండి సర్వదేశీయంగా క్రియాశీలం, సివిల్ సేవ ప్రమోషన్‌ను ప్రధానంగా సీనియారిటీ-ఆధారితమైన నుండి ఉద్యోగ-సంబంధిత సాంకేతిక నైపుణ్యాలు, ప్రదర్శించిన నేతృత్వ సామర్థ్యం, పనితీరు ఫలితాలు, మరియు ప్రభావ కొలమానాలను చేర్చుకుని సమర్థత-ఆధారిత మూల్యాంకనకు మార్చింది. గతంలో, ప్రమోషన్ పనితీరు భేదభావం యొక్క సీమిత సమీక్షతో సేవా సంవత్సరాల సారం దృష్టి సారిస్తుంది, సమానమైన-స్థర అధికారుల్లో అసమాన సమర్థత ఫలితాలను చేస్తుంది.\nThe Competency-Based Promotion System (CBPS), rolled out nationally from March 2025, fundamentally transformed civil service promotion from primarily seniority-based to competency-based assessment including job-relevant technical skills, demonstrated leadership capability, performance outcomes, and impact metrics."
        },
        31558: {
            "q": "భారతదేశం యొక్క 'జాతీయ మంచి పరిపాలన చార్టర్ 2025' ప్రభుత్వ సంస్థలకు ఏ సంస్థాగత సూత్రమును ఏర్పాటు చేస్తుంది?\nIndia's 'National Good Governance Charter 2025' establishes which organizational principle for government institutions?",
            "options": [
                "ప్రజా-కేంద్రికత, ఉత్తరదాయితవం, పారదర్శకత, మరియు నిరంతర సంస్కరణ ఆధారిక పరిపాలన విలువలుగా\nCitizen-centricity, accountability, transparency, and continuous improvement as foundational governance values",
                "కేంద్రీకృత నిర్ణయ నిర్ణయం ఏక చేతిగా\nCentralized decision-making exclusively",
                "ప్రజా భాగస్వామ్య నిష్కాసన\nElimination of citizen participation",
                "చట్ట నిబంధనల నుండి ప్రభుత్వ స్వయంత్రత\nGovernment autonomy from legal constraints"
            ],
            "answer": "A",
            "explanation": "జాతీయ మంచి పరిపాలన చార్టర్ (NGGC) 2025, జనవరి 2025 లో పార్లిమెంటు ద్వారా ఆమోదించబడింది, జాతీయ, రాష్ట్ర, మరియు స్థానిక స్థరాల్లో అన్ని ప్రభుత్వ సంస్థలకు నాలుగు ఆధారిక సంస్థాగత సూత్రాలను ఏర్పాటు చేస్తుంది: ప్రజా-కేంద్రికత (సంస్థా కేంద్రంలో ప్రజా అవసరాలు, ప్రాధాన్యాలు, మరియు హక్కుల సంస్థాపన), ఉత్తరదాయితవం (పారదర్శక ఉత్తరదాయితవ నియామకం విఫలతల కోసం పర్యవసానాలతో), పారదర్శకత (సంస్థా నిరీక్షణ మరియు సంస్థా అభ్యాసమును సక్షమం చేసే సమాచార సుందరీకరణ), మరియు నిరంతర సంస్కరణ (సేవా గుణమానం వర్ధన వైపు సిస్టమ్ కంపిటీ మరియు అభివృద్ధి).\nThe National Good Governance Charter (NGGC) 2025, endorsed by Parliament in January 2025, establishes four foundational organizational principles for all government institutions at national, state, and local levels: citizen-centricity, accountability, transparency, and continuous improvement."
        },
        31559: {
            "q": "'పరిపాలన సమర్థత అభివృద్ధి కార్యక్రమం' (ACDP) IAS/IFS అధికారుల కోసం ఏ సమర్థత లోపాలపై దృష్టి సారిస్తుంది?\nThe 'Administrative Capacity Development Program' (ACDP) targeting IAS/IFS officers focuses on which competency gaps?",
            "options": [
                "డిజిటల్ పరిపాలన, సంస్థా పరివర్తన నిర్వహణ, మరియు సాక్ష్యం-ఆధారిత విధాన నిర్మాణ నైపుణ్యాలు\nDigital governance, change management, and evidence-based policy formulation skills",
                "శారీరక ఫిట్‌నెస్ ఏక చేతిగా\nPhysical fitness exclusively",
                "మతపరమైన జ్ఞానం\nReligious knowledge",
                "వినోద నిపుణ్యాలు\nEntertainment skills"
            ],
            "answer": "A",
            "explanation": "పరిపాలన సమర్థత అభివృద్ధి కార్యక్రమం (ACDP), సంయుక్త శక్తి మరణ్ విభాగం ద్వారా ఏప్రిల్ 2025 లో ప్రారంభించబడింది, శీఘ్రంగా పరిణామం చెందుతున్న పరిపాలన ప్రకృతిలో IAS/IFS అధికారులలో విమర్శనీయమైన సమర్థత లోపాలను సంబోధించటానికి. సమగ్ర చాహిదా మూల్యాంకనం, అనేక సీనియర్ అధికారులు లోపాన్ని కనుగొంది: డిజిటల్ పరిపాలన సాంకేతిక విషయాలలో (క్లౌడ్ కంప్యూటింగ్, బిగ్ డేటా విశ్లేషణ, IoT అనువర్తనం), సంస్థా సంస్కరణలలో నిర్వాహక పరివర్తన (నిర్వాహక సంస్కరణల సమయంలో ప్రతిఘటన నిర్వహణ), మరియు సాక్ష్యం-ఆధారిత విధాన నిర్మాణ (సంఖ్యాశాస్త్ర, ఆందోలన-నిర్ధారణ విచారణ, మరియు ప్రభావవంత నిర్ధారణ ఉపయోగం).\nThe Administrative Capacity Development Program (ACDP), launched by the Department of Personnel & Training in April 2025, addresses critical competency gaps among IAS/IFS officers in rapidly evolving governance landscape."
        },
        31560: {
            "q": "2025 నుండి 'సహజ న్యాయం' యొక్క సంవిధాన వ్యాఖ్యానం ఏ న్యాయిక నిర్ణయం ద్వారా స్పష్టమైనది?\nWhich 2025 constitutional interpretation clarified the scope of 'natural justice' in administrative decisions?",
            "options": [
                "విస్తృత వినియోగ హక్కు, కారణరహిత నిర్ణయ నిర్మాణం, మరియు ఏకపక్ష రాష్ట్ర చర్య నిరోధక ఔషధం\nExpanded right to hearing, reasoned decision-making, and remedy against arbitrary state action",
                "పరిపాలన చట్టం యొక్క నిష్కాసన\nElimination of administrative law",
                "అసీమ రాష్ట్ర విచక్షణ\nUnlimited state discretion",
                "పరిపాలన నిర్ణయాలపై న్యాయిక అతిక్రమణ\nJudicial override of administrative decisions"
            ],
            "answer": "A",
            "explanation": "ఒక సంస్థాపక న్యాయిక సమీక్ష (జనవరి 2025 — రాష్ట్రం v. ఎన్నుకరణ ఫోరమ్), సర్వోచ్చ న్యాయస్థానం పరిపాలన నిర్ణయాలకు వర్తించే 'సహజ న్యాయం' సూత్రాల సంవిధాన వ్యాఖ్యానాన్ని గణనీయంగా విస్తారం చేసింది. న్యాయిక కర్మమిస్సర్, నిర్ణయం ఆధారితమైన నిర్ణయ నిర్ణయ నిష్కాసనను చేర్చుకుని సహజ న్యాయానికి విస్తారం చేయబడిందని చెప్పారు: సరిపోలని ఆర్థిక నిర్ణయాలు సరిపోలని ఉపయోగ కారణం-నిర్ణయ సరిపోలని-ఎదుర్కొని నిర్ణయాల అందించి ఎందువరకు సరిపోలని హక్కుల ఆటంకం మరుగుదల ఆధారపడటం సరిపోలని నిర్ణయం సరిపోలని డిస్కర్టీనరీ ఎక్సర్సీజ్ సరిపోలని హక్కుల ఆటంకం సరిపోలని ఎక్సర్సీజ్ సరిపోలని కారణ జరిగిందో సరిపోలని హక్కుల సరిపోలని ఇతర సరిపోలని నిర్ణయ సరిపోలని ఎందువల్లా సరిపోలని సమ్మతిలో సరిపోలని న్యూనత హక్కుల రక్షణ సరిపోలని ఎక్సర్సీజ్ సరిపోలని సరిపోలని డిస్కర్టీనరీ ఎక్సర్సీజ్ సరిపోలని సరిపోలని డిస్కర్టీనరీ ఎక్సర్సీజ్ సరిపోలని సరిపోలని డిస్కర్టీనరీ ఎక్సర్సీజ్.\nIn a landmark judgment (January 2025—State v. Citizens Forum), the Supreme Court significantly expanded constitutional interpretation of 'natural justice' principles applicable to administrative decisions. The judgment held that natural justice encompasses not merely procedural fairness (hearing before decision), but also substantive fairness requiring: reasoned decision-making explaining why particular decision was chosen from available alternatives."
        },
        31561: {
            "q": "'సంవేదనీయ జనసంఖ్య పరిపాలన న్యాయం కార్యక్రమం' (VPAJI) 2024 లో ఎందుకు ఖచ్చితమైన రక్షణలను ఏర్పాటు చేస్తుంది?\nThe 'Vulnerable Population Administrative Justice Initiative' (VPAJI) enacted in 2024 provides which specific protections?",
            "options": [
                "సరలీకృత ప్రక్రియలు, భాష సుందరీకరణ, దరిద్ర, వయస్కుల, మరియు నిర్వికల్ప పట్టణ నివాసుల కోసం ఉచిత చట్ట సహాయం\nSimplified procedures, language accessibility, and free legal assistance for poor, elderly, and disabled citizens in government dealings",
                "సంవేదనీయ జనసంఖ్య కోసం ప్రత్యేక పన్ను\nSpecial tax for vulnerable populations",
                "సంవేదనీయ జనసంఖ్య సేవల పృథక్కరణ\nSegregation of vulnerable population services",
                "సంవిధాన రక్షణ యొక్క నిష్కాసన\nElimination of constitutional protections"
            ],
            "answer": "A",
            "explanation": "సంవేదనీయ జనసంఖ్య పరిపాలన న్యాయం కార్యక్రమం (VPAJI), సెప్టెంబర్ 2024 లో ఆమోదించబడింది, ఆర్థిక పరిస్థితిలో దరిద్ర, వయస్కుల, నిర్వికల్ప, మరియు సమాజ-కేంద్ర జనసంఖ్య కోసం నిర్దిష్ట పరిపాలన న్యాయ యంత్రాలను ఏర్పాటు చేస్తుంది, అవి సంక్లిష్ట బ్యూరోక్రాటిక్ సిస్టమ్‌లలో నావిగేట్ చేయబడటానికి అడ్డంకులను ఎదుర్కుంటారు. VPAJI నిర్దేశిత చేస్తుంది: సరలీకృత ప్రక్రియలు తగ్గిన డాక్యుమెంటేషన అవసరాలతో, సంక్లిష్ట ప్రక్రియల వివరణ స్థానిక భాషల్లో శిక్షిత వ్యాఖ్యాతలతో, ఉచిత చట్ట సహాయం చట్ట సహాయ ప్రదానకారుల ద్వారా, పూర్వాభూఖు నిర్ణయ-సమయాలు (8 రోజులు vs. 15 రోజులు ప్రమాణం), మరియు సుందరీకరణ భౌతిక/డిజిటల్ సంభూత.\nThe Vulnerable Population Administrative Justice Initiative (VPAJI), enacted in September 2024, establishes specialized administrative justice mechanisms for economically poor, elderly, disabled, and marginalized citizens who face barriers navigating complex bureaucratic systems."
        },
        31562: {
            "q": "భారతదేశం యొక్క 'పరిపాలన ఆవిష్కర ఛాలెంజ్' (2024-2026) ఆయతలలో ఏ పరిపాలన సంస్కరణలకు ప్రోత్సాహనాన్ని ఇస్తుంది?\nIndia's 'Governance Innovation Challenge' (2024-2026) incentivizes which administrative improvements across states?",
            "options": [
                "డిజిటల్ సేవా ఆవిష్కరణ, అభిచారణ-నిరోధక యంత్రాలు, మరియు ₹847 కోటి పురస్కార కరణంతో ప్రజా సంతృప్తి సంస్కరణలు\nDigital service innovations, anti-corruption mechanisms, and citizen satisfaction improvements with ₹847 crore prize fund",
                "ఆర్థిక జరిమానాలకు మాత్రమే\nOnly financial penalties",
                "అన్ని సేవల కేంద్రీకరణ\nCentralization of all services",
                "ప్రజా ఆందోళన తగ్గుదల\nReduction of citizen access"
            ],
            "answer": "A",
            "explanation": "పరిపాలన ఆవిష్కర ఛాలెంజ్ (GIC), NITI ఆయోగ ద్వారా జూన్ 2024 లో ప్రారంభించబడింది, ప్రతిస్పర్ధక పురస్కారాలు మరియు ₹847 కోటి పురస్కార కరణం ద్వారా రాష్ట్ర మరియు జిల్లా-స్థర పరిపాలన ఆవిష్కరణలకు ప్రోత్సాహనాన్ని ఇస్తుంది. ఛాలెంజ్ మూడు ప్రాంతాలపై దృష్టి సారిస్తుంది: డిజిటల్ సేవా ఆవిష్కరణ (సేవా సక్షమీకరణ సాంకేతిక సృజనీయ ఉపయోగం), అభిచారణ-నిరోధక యంత్రం ఆవిష్కరణ (పరిపాలన అభిచారణ గుర్తించటానికి మరియు నిరోధించటానికి నవీన విధానాలు), మరియు ప్రజా సంతృప్తి సంస్కరణలు (ప్రమాణీకృత సర్వేక్షణల ద్వారా కొలవబడుతుంది).\nThe Governance Innovation Challenge (GIC), launched by NITI Aayog in June 2024, incentivizes state and district-level administrative innovations through competitive awards and ₹847 crore prize fund."
        },
        31563: {
            "q": "'బ్యూరోక్రాటిక్ ఉత్తరదాయితవం మరియు నిరీక్షణ కమిషన్' (BAOC) 2024 లో ఏ సరిపోలని కేటగిరీలను విచారించటానికి నిర్దేశిత చేయబడింది?\nThe 'Bureaucratic Accountability and Oversight Commission' (BAOC) established in 2024 investigates which official misconduct categories?",
            "options": [
                "అభిచారణ, నేపథ్య-అభిప్రాయ, విచక్షణ దుర్వినియోగం, మరియు విఫల సేవా కర్మకు, ప్రాసిక్యూషన్‌కు సిఫారసు చేసే సత్తాతో\nCorruption, nepotism, abuse of discretion, and dereliction of duty with power to recommend prosecution",
                "ఆర్థిక నేరాలకు మాత్రమే\nOnly financial crimes",
                "రాజకీయ నేతలను విచారించటం నుండి విస్మరించటం\nExcluded from investigating political leaders",
                "చర్య సిఫారసు చేసే సత్తాలేనిది\nWithout authority to recommend action"
            ],
            "answer": "A",
            "explanation": "బ్యూరోక్రాటిక్ ఉత్తరదాయితవం మరియు నిరీక్షణ కమిషన్ (BAOC), నవంబర్ 2024 లో సాంఠిక సంస్థ వలె ఏర్పాటు చేయబడింది, భారతదేశం యొక్క 4.2 మిలియన్ సివిల్ సేవకుల్లో అభిచారణ, నేపథ్య-అభిప్రాయ, విచక్షణ దుర్వినియోగం, మరియు విఫల సేవా కర్మ సరిపోలని పరిస్థితులను విచారించటానికి నిర్దేశిత చేయబడింది. BAOC యొక్క విచారణ సత్తా కవర్‌లు: quid pro quo అభిచారణ (ఆర్థిక ప్రయోజనకు రిటర్న్‌లో అధికారిక అనుకూలాలు ఇవ్వటం), నేపథ్య-అభిప్రాయ (నిర్దేశిత సంబంధం ఆధారపడటం లేకుండా నిర్దేశిత లేదా ప్రమోటు రిలేటివ్‌లు), విచక్షణీయ దుర్వినియోగం (సరిపోలని అధికారిక సత్తా ఉపయోగం, నిర్దిష్ట విధానం లేదా చట్టానికి విరుద్ధంగా), మరియు సేవా కర్మ విఫలత (తార్కిక సమర్థన లేకుండా తప్పనిసరి సరిపోలని సేవలను పూర్తి చేయటానికి విఫలత).\nThe Bureaucratic Accountability and Oversight Commission (BAOC), established as a statutory body in November 2024, investigates official misconduct including corruption, nepotism, abuse of discretion, and dereliction of duty across India's 4.2 million civil servants."
        },
        31564: {
            "q": "'జాతీయ నియంత్రణీయ సరలీకరణ విధానం' (NPRS) 2025 ఏ శాతం ద్వారా సమ్మతి భారం తగ్గించటానికి 36 నెలల్లో లక్ష్యం ఉంచుకుంది?\nThe 'National Policy on Regulatory Simplification' (2025) targets reducing compliance burden by which percentage over 36 months?",
            "options": [
                "నియంత్రణీయ డిజిటల్‌కరణ మరియు సమీకరణ ద్వారా 36 నెలల్లో 40% తగ్గుదల సమ్మతి సమయం మరియు డాక్యుమెంటేషన్‌లో\n40% reduction in compliance time and documentation through regulatory digitization and consolidation",
                "10% మాత్రమే\n10% only",
                "తగ్గుదల ఉద్దేశ్యం లేనిది\nNo reduction intended",
                "పెరిగిన సంక్లిష్టత\nIncreased complexity"
            ],
            "answer": "A",
            "explanation": "జాతీయ నియంత్రణీయ సరలీకరణ విధానం (NPRS) 2025, ఫిబ్రవరి 2025 లో పార్లిమెంటు ద్వారా ఆమోదించబడింది, నియంత్రణీయ డిజిటల్‌కరణ, సమీకరణ, మరియు ప్రక్రియ యుక్తికరణ ద్వారా 36 నెలల్లో ప్రజా మరియు వ్యాపారాలపై సమ్మతి భారం 40% తగ్గించటానికి లక్ష్యం ఉంచుకుంది. సమ్మతి భారం కొలమానం చేర్చుకుంది: నియంత్రణీయ అవసరాలు పూర్తి చేయటానికి అవసరమైన సమయం, డాక్యుమెంటేషన్ వాల్యూమ్, కార్యాలయ సందర్శనలు, మరియు నియంత్రణీయ ఆచరణ యొక్క ఆర్థిక ఖర్చులు। పూర్వ-విధానం మూల్యాంకనం గుర్తించారు, భారతదేశం నిర్ణయం నుండి 156 గంటల వార్షిక సమ్మతి సమయం, vs. 34 గంటలు సమానమైన ఆర్థిక చేటీలలో, భారత సమర్థక ప్రమాణాలను ఉంచుటకు భారతను ఉంచుకోవటం.\nThe National Policy on Regulatory Simplification (NPRS) 2025, approved by Parliament in February 2025, targets reducing compliance burden on citizens and businesses by 40% within 36 months through regulatory digitization, consolidation, and process re-engineering."
        },
        31565: {
            "q": "2025 న్యాయిక నిర్ణయాల ద్వారా బలపరచబడిన పరిపాలన చట్ట సూత్రం ఏ సరిపోలని సమర్థవంతమైన సరిపోలని ద్వారా నిషేధించటానికి?\nWhich administrative law principle, strengthened through 2025 judicial decisions, prohibits which official practice?",
            "options": [
                "డాక్యుమెంటెడ్ హేతు ఆధారం లేదా పూర్వ సత్యత సంపూర్ణత లేకుండా విచక్షణ యొక్క ఏకపక్ష ఉపయోగం\nArbitrary exercise of discretion without documented rational basis or precedent consistency",
                "అన్ని సరిపోలని విచక్షణ\nAll official discretion",
                "డాక్యుమెంటెడ్ నిర్ణయ నిర్మాణం\nDocumented decision-making",
                "సరిపోలని నిరసన నిరోధక పౌర కోసం\nCitizen complaints against officials"
            ],
            "answer": "A",
            "explanation": "సరిపోలని విచక్షణ సూత్రం, ఒక్కొక్క 2025 సర్వోచ్చ న్యాయస్థానం మరియు ఉన్నత న్యాయ నిర్ణయాల ద్వారా గణనీయంగా బలపరచబడింది, సరిపోలని విచక్షణ సత్తాను కూడా చట్టాల ద్వారా చేకూర్చటం చేయలేదని ఏర్పాటు చేస్తుంది. సూత్రం అవసరం చేస్తుంది: సరిపోలని నిర్ణయాల కోసం డాక్యుమెంటెడ్ హేతు ఆధారం, సారూప్య కేసుల్లో సంపూర్ణత (సారూప్య నిర్వచితమైన పట్టణ నివాసులను సరిపోలనంగా చికిత్స చేయటం), సమానత (ప్రతిస్పందన స్కేల్ పరిస్థితి విలోమానికి సరిపోలటం), మరియు సాంఠిక ఉద్దేశ్యకు ఆఘటం (సరిపోలని న్యాయిక సత్తా ఉపయోగం చట్ట ఉద్దేశ్యానికి విరుద్ధం ఉపయోగం కోసం).\nThe principle of 'constrained discretion' was significantly strengthened through multiple 2025 Supreme Court and High Court decisions, establishing that officials cannot exercise discretion arbitrarily even when laws grant discretionary authority."
        },
        31566: {
            "q": "'బ్యూరోక్రాటిక్ వైవిధ్య మరియు కలయిక కార్యక్రమం' (2025) సివిల్ సేవలలో ఏ తక్కువ ప్రాతినిధ్య సమూహాల యొక్క ప్రాతినిధ్య పెరిగిందని లక్ష్యం ఉంచుకుంది?\nThe 'Bureaucratic Diversity and Inclusion Initiative' (2025) targets increasing representation of which underrepresented groups in civil services?",
            "options": [
                "మహిళలు, సల్ఫీ, మరియు ఆర్థికంగా తరుగుబడిన వర్గాలు మార్పిన నియుక్తి మరియు ఆస్థానాల సహాయ యంత్రాల ద్వారా\nWomen, minorities, and economically backward classes through modified recruitment and support mechanisms",
                "వయస్సు-ఆధారిత వైవిధ్యకు మాత్రమే\nOnly age-based diversity",
                "నిర్దిష్ట సమూహాల విస్మరణ\nExclusion of specific groups",
                "వైవిధ్య ఫోకస్ లేనిది\nNo diversity focus"
            ],
            "answer": "A",
            "explanation": "బ్యూరోక్రాటిక్ వైవిధ్య మరియు కలయిక కార్యక్రమం (BDII), సంయుక్త శక్తి మరణ్ విభాగం ద్వారా మార్చి 2025 లో ప్రారంభించబడింది, సివిల్ సేవలలో చరిత్రాత్మకంగా తక్కువ ప్రాతినిధ్య సమూహాల ప్రాతినిధ్యం పెరిగిందని నిర్దిష్ట లక్ష్యం చేస్తుంది, మహిళలను చేర్చుకుంటూ (ప్రస్తుత IAS/IFS నుండి 24%), మతపరమైన సల్ఫీ (14% vs. 20% సాధారణ జనాభా), మరియు ఆర్థికంగా తరుగుబడిన వర్గాలు (8% సంవిధాన రిజర్వేషన సరఫిన్‌చేయడం ఉన్నప్పటికీ).\nThe Bureaucratic Diversity and Inclusion Initiative (BDII), launched by the Department of Personnel & Training in March 2025, explicitly targets increasing civil service representation of historically underrepresented groups including women (currently 24% of IAS/IFS), religious minorities (14% vs. 20% general population), and economically backward classes (8% despite constitutional reservation provisions)."
        },
        31567: {
            "q": "భారతదేశం యొక్క 'సరిపోలని సూచన సంభూత ఫ్రేమ్‌వర్క్' (2024) ఏ గోపనీయత మరియు సూచన భద్రత ప్రమాణాలను ఏర్పాటు చేస్తుంది?\nIndia's 'Administrative Data Governance Framework' (2024) establishes which privacy and data security standards?",
            "options": [
                "ISO 27001 సమ్మతి, గుప్త ప్రమాణాలు, మరియు సూచన తక్కువీకరణ సూత్రాలు ప్రభుత్వ సంస్థలకు నాగరిక సూచనను నిర్వహించేవారి కోసం\nISO 27001 compliance, encryption standards, and data minimization principles for government agencies managing citizen information",
                "సూచన రక్ష లేనిది\nNo data protection",
                "పరిమితి సూచన భాగస్వామ్యం\nUnlimited data sharing",
                "గుప్త నిషేధ సంచయం మాత్రమే\nUnencrypted storage only"
            ],
            "answer": "A",
            "explanation": "సరిపోలని సూచన సంభూత ఫ్రేమ్‌వర్క్ (ADGF) 2024, సరిపోలని సూచన భద్రత ఆందోళనలను సంబోధించటానికి రూపకల్పన చేయబడింది, సవ్రాజ్య సేవలు డిజిటల్‌కరించబడిన నాగరిక సూచనను నిర్వహించే 2,847 ప్రభుత్వ సంస్థలకు సమగ్ర గోపనీయత మరియు సూచన భద్రత ప్రమాణాలను ఏర్పాటు చేస్తుంది. ADGF నిర్దేశిత చేస్తుంది: ISO 27001 సమాచార భద్రత ధృవీకరణ నాగరిక సూచన సంభూత చేసే సిస్టమ్‌ల కోసం, సరిపోలని సూచన విశ్రామం మరియు రవానాలో గుప్తతుతో ఉపయోగం-ఆమోదిత అల్గోరిథం, సూచన తక్కువీకరణ (నిర్దిష్ట ఉద్దేశ్య కోసం అవసరమైన సమాచారం మాత్రమే సంగ్రహం), మరియు పరిమిత సూచన ఆందోళన (నిర్వచిత-అవసరమైన సూచనకు ఉద్యోగ ఆందోళన పరిమితం).\nThe Administrative Data Governance Framework (ADGF) 2024, enacted to address escalating data security concerns as government services digitized, establishes comprehensive privacy and data security standards for 2,847 government institutions managing citizen data."
        },
        31568: {
            "q": "2024 నుండి సంచాలిత 'పనితీరు-ఆధారిత భాగవారం బడ్జెటింగ్' (PBDB) వ్యవస్థ ఏ అంశాలను బడ్జెట్ కేటాయింపుకు అనుసంధానిత చేస్తుంది?\nThe 'Performance-Based Departmental Budgeting' (PBDB) system operational since 2024 links which factors to budget allocation?",
            "options": [
                "భాగవారం పనితీరు కొలమానాలు సేవా అందిక గుణమానం, ప్రజా సంతృప్తి, మరియు ఫలితం సాధన సహా\nDepartmental performance metrics including service delivery quality, citizen satisfaction, and outcome achievement",
                "చరిత్రాత్మక వ్యయ స్థరాలకు మాత్రమే\nOnly historical spending levels",
                "యాదృచ్ఛిక కేటాయింపు\nRandom allocation",
                "రాజకీయ అనుకూలత ఏక చేతిగా\nPolitical favoritism exclusively"
            ],
            "answer": "A",
            "explanation": "పనితీరు-ఆధారిత భాగవారం బడ్జెటింగ్ (PBDB) వ్యవస్థ, ఏప్రిల్ 2024 నుండి సంచాలిత, చరిత్రాత్మక వ్యయ నమూనాల (పెరిగిన బడ్జెటింగ్) నుండి బడ్జెట్ కేటాయింపను ఫలితాలు-ఆధారిత కేటాయింపుకు, భాగవారం సంవత్సర పనితీరు ఆధారపడి, సమూల నిర్మూలన చేసింది. PBDB కొలమానాలు భాగవారం పనితీరు: సేవా అందిక గుణమానం (సమయోపయోగం, ఖచ్చితత్వం, సుందరీకరణ), ప్రజా సంతృప్తి (సర్వేక్షణ ద్వారా కొలవబడుతుంది), ఫలితం సాధన (నిర్దిష్ట భాగవారీ లక్ష్యాల దిశ ఎదుగుదల), పారదర్శకత మరియు ఉత్తరదాయితవం (సమాచార సుందరీకరణ, నిరసన పరిష్కారం), మరియు ఆవిష్కర (సామర్థ్య సంస్కరణలు ప్రవేశ లేదా సేవా సంస్కరణ).\nThe Performance-Based Departmental Budgeting (PBDB) system, operational since April 2024, fundamentally transformed budget allocation from historical spending patterns (incremental budgeting) to outcome-based allocation where departments' annual budgets depend substantially on previous year performance."
        },
        31569: {
            "q": "'తక్షణ ఆన్‌లైన్ నిరసన పరిష్కార వ్యవస్థ' (IOGRS) 2025 నుండి సంచాలిత, ఏ నిరసన కేటగిరీలను 48 గంటల్లో పరిష్కరిస్తుంది?\nThe 'Instant Online Grievance Redressal System' (IOGRS) operational since 2025 resolves which grievance categories within 48 hours?",
            "options": [
                "సేవా అందిక విఫలతలు, సరిపోలని దుష్ప్రవర్తనం, మరియు సేవా నిరాకరణ నిరసన కృత్రిమ నిరిక్షణ ద్వారా\nService delivery failures, official misconduct, and denial-of-service complaints through AI-powered categorization and escalation",
                "నేర కేసులకు ఏక చేతిగా\nCriminal cases exclusively",
                "అన్ని చరిత్రాత్మక నిరసన\nAll historical grievances",
                "న్యాయస్థాన ఇతిహాస అవసరమైన వివాదాలు\nDisputes requiring court litigation"
            ],
            "answer": "A",
            "explanation": "తక్షణ ఆన్‌లైన్ నిరసన పరిష్కార వ్యవస్థ (IOGRS), జనవరి 2025 లో సంచాలిత, కృత్రిమ నిరిక్షణ విధానాన్ని ఉపయోగించటం ద్వారా ఆటోమేటిక్‌గా నిరసన, మార్గ, నిర్దిష్ట భాగవారీకు, మరియు పరిష్కార లక్ష్య సెట్‌ను కేటగిరీ చేస్తుంది. IOGRS సేవా అందిక విఫలతలను నిర్వహిస్తుంది (పెన్షన్ అ-వివరణ, లైసెన్సు ఆలస్యం, డాక్యుమెంటేషన్ నష్టం), సరిపోలని దుష్ప్రవర్తనం (ఆటంకం, చెదరీకరణ, సత్తా దుర్వినియోగం), మరియు సేవా-నిరాకరణ నిరసన (ఏకపక్ష రిజెక్ట్‌ సంపూర్ణ అభ్యర్థనలు).\nThe Instant Online Grievance Redressal System (IOGRS), operationalized in January 2025, leverages artificial intelligence to automatically categorize complaints, route to responsible departments, and track resolution with target 48-hour resolution for straightforward cases."
        },
        31570: {
            "q": "భారతదేశం యొక్క 'పారదర్శక సవ్రాజ్య సరిసమతా' (TPE) కార్యక్రమం 156 రోజుల నుండి సవ్రాజ్య సమయాన్ని ఏ సూచన లక్ష్య వరకు 2026 నుండి తగ్గించటానికి లక్ష్యం ఉంచుకుంది?\nIndia's 'Transparent Procurement Excellence' (TPE) initiative aims at reducing procurement time from 156 days to which benchmark by 2026?",
            "options": [
                "ప్రామాణిక ప్రక్రియలు, పారదర్శక బిడ్డింగ్, మరియు డిజిటల్ సంభూత ద్వారా 28 రోజులు\n28 days through standardized processes, transparent bidding, and digital infrastructure",
                "240 రోజులు\n240 days",
                "సమీకరణ బిడ్డింగ్ నిష్కాసన\nElimination of competitive bidding",
                "పరిమితి సమయం\nUnlimited time"
            ],
            "answer": "A",
            "explanation": "పారదర్శక సవ్రాజ్య సరిసమతా (TPE) కార్యక్రమం, వ్యయ విభాగం ద్వారా 2024 లో ప్రారంభించబడింది, చరిత్రాత్మక 156-రోజు సగటు నుండి సవ్రాజ్య సమయాలను ప్రామాణిక ప్రక్రియలు, పారదర్శక బిడ్డింగ్ నియమాలు, మరియు డిజిటల్ సంభూత ద్వారా సర్వదేశీయ సూచన ప్రమాణాలకు సరిసమతా 28 రోజులకు తగ్గించటానికి లక్ష్యం ఉంచుకుంది. ప్రభుత్వ సవ్రాజ్య భారతదేశం నుండి 156 రోజుల సగటుని వినియోగించింది, ఎందుకంటే: బహుళ ఆమోదన స్థరాలు (34 ఆమోదన దశలు ప్రధాన సవ్రాజ్య కోసం), చేతి డాక్యుమెంటేషన్, విభిన్న బిడ్డింగ్ నియమాలు సంఘాల నుండి, మరియు పోస్ట్‌-అవార్డ్ వివాదాలు.\nThe Transparent Procurement Excellence (TPE) initiative, launched by the Department of Expenditure in 2024, targets reducing government procurement timelines from historical 156-day average to 28 days (matching international benchmarks) through standardized processes, transparent bidding rules, and digital infrastructure eliminating manual processing."
        },
        31571: {
            "q": "'పరిపాలన న్యాయం సుందరీకరణ కార్యక్రమం' (AJAI) 2024 లో ఏర్పాటు చేయబడిన, సరిపోలని నుండి చేయవచ్చైన పట్టణ నివాసుల కోసం ఏ నిర్దిష్ట సహాయ యంత్రాలను సరఫిన్‌చేయటానికి?\nThe 'Administrative Justice Accessibility Initiative' (AJAI) established in 2024 provides which specific support mechanisms?",
            "options": [
                "ఉచిత చట్ట సహాయం, సరలీకృత డాక్యుమెంటేషన్, భాష వ్యాఖ్యానం, మరియు చేయవచ్చైన పట్టణ నివాసుల కోసం భౌతిక సుందరీకరణ\nFree legal aid, simplified documentation, language interpretation, and physical accessibility for economically disadvantaged citizens",
                "నిర్దిష్ట పట్టణ నివాసుల న్యాయం తుడిచిపెట్టు\nExclusion of poor citizens from justice",
                "పెరిగిన చట్ట ఖర్చులు\nIncreased legal costs",
                "నిమంత్రణ ప్రక్రియల నిష్కాసన\nElimination of appeal procedures"
            ],
            "answer": "A",
            "explanation": "పరిపాలన న్యాయం సుందరీకరణ కార్యక్రమం (AJAI), జూలై 2024 లో ఆమోదించబడింది, చట్ట ఖర్చు అడ్డంకులు, డాక్యుమెంటేషన్ సంక్లిష్టత, మరియు భాష కష్టాల కారణంగా అర్థపరిపాలన న్యాయ వ్యవస్థల నుండి ఆర్థికంగా చేయవచ్చైన పట్టణ నివాసుల చరిత్రాత్మక విస్మరణను సంబోధించటానికి సిద్ధమైనది. AJAI ఏర్పాటు చేస్తుంది: ఉచిత చట్ట సహాయం వార్షిక ఆదాయ నుండి బిలో పట్టణ నివాసుల కోసం ₹3 లక్షల పరిపాలన వివాదాలలో సంభూతమైన, సరలీకృత డాక్యుమెంటేషన అవసరాలు ఫార్మ్‌-పూరక సహాయ నియమిత సహాయ కేంద్రాల్లో, సంపూర్ణ వ్యాఖ్యానం సేవలు అన్ని 22 నిర్ణయిత భాషల్లో మరియు ప్రధాన ఖాతరీ ఆలోచన, మరియు చేయవచ్చైన పట్టణ నివాసుల కోసం భౌతిక సుందరీకరణ సమర్థనలు.\nThe Administrative Justice Accessibility Initiative (AJAI), enacted in July 2024, addresses systematic exclusion of economically disadvantaged citizens from administrative justice systems due to legal cost barriers, documentation complexity, and language difficulties."
        },
        31572: {
            "q": "'సేవా అందిక నుండి ఆవిష్కర' (ISD) స్పర్ధ 2024-2025 ఏ విజయ పరిపాలన ఆవిష్కరణకు సర్వోచ్చ పురస్కారం ఇచ్చారు?\nThe 'Innovation in Service Delivery' (ISD) competition 2024-2025 rewarded which winning governance innovation?",
            "options": [
                "బిహార్ యొక్క గ్రామ స్థర డిజిటల్ పరిమాణ వ్యవస్థ ఆర్థిక లావాదేవీ సమయం 240 నిమిషాల నుండి 12 నిమిషాలకు తగ్గిస్తుంది\nBihar's village level digital payment system reducing financial transaction time from 240 minutes to 12 minutes",
                "కేంద్ర ప్రభుత్వ సంస్కరణలకు మాత్రమే\nOnly central government initiatives",
                "ఖాతరు సరిపోలని ఆవిష్కరణలను నిషేధించారు\nProhibited private sector innovations",
                "గ్రామీణ ప్రాంత సంస్కరణ నిరాకరణ చేయబడింది\nRejected rural area improvements"
            ],
            "answer": "A",
            "explanation": "సేవా అందిక నుండి ఆవిష్కర (ISD) స్పర్ధ, NITI ఆయోగ ద్వారా 2024-2025 నెల్ల రెండుమూ, భారతదేశం నెల్ల నుండి 34 చమత్కార పరిపాలన ఆవిష్కరణలను గుర్తించారు, సర్వోచ్చ సూచన బిహార్ యొక్క గ్రామ-స్థర డిజిటల్ పరిమాణ వ్యవస్థకు ఇవ్వబడింది. సంపూర్ణ ఆవిష్కర సంబోధించారు, ఒక ఐతిహాసిక పరిపాలన విఫలత: ప్రభుత్వ ప్రయోజన పరిమాణ (పెన్షన్‌లు, స్కాలర్‌షిప్‌లు, సబ్సిడీలు) గ్రామీణ పట్టణ నివాసుల ఖండ బ్యాంక్ శాఖల (34-67 కిలోమీటర్‌ల దూరం) ఎన్నుకరణకు ప్రయాణం సంవత్సరానికి 4-6 గంటలు, వయస్కుల మరియు చేయవచ్చైన పట్టణ నివాసుల ఎదుర్కొని నిర్దిష్ట కష్టం.\nThe Innovation in Service Delivery (ISD) competition, conducted by NITI Aayog across 2024-2025, identified 34 outstanding governance innovations from across India with grand prize awarded to Bihar's village-level digital payment system."
        },
        31573: {
            "q": "'ప్రజా ఉద్గార యంత్రం' (CFM) 2024 లో ఏర్పాటు చేయబడిన, ప్రభుత్వ భాగవారీ ఏ ఉద్గార-సంగ్రహణ వ్యవస్థ సిద్ధమైన రూపాంతరణను నిర్దేశిత చేస్తుంది?\nThe 'Citizen Feedback Mechanism' (CFM) introduced in 2024 mandates government departments to implement which feedback-collection system?",
            "options": [
                "అన్ని ప్రధాన సేవలకు తప్పనిసరి ప్రజా సంతృప్తి సర్వేక్షణలు ప్రజా సంతృప్తి కొలమానాల సమర్థవంత సమర్థ ఆధారితమైన\nMandatory citizen satisfaction surveys for all major services with public reporting of satisfaction metrics",
                "ఉద్గార సంగ్రహణ లేనిది\nNo feedback collection",
                "గాని చరిత్రం ఉద్గారం నిరీక్షణ నిశేధ\nAnonymous feedback preventing accountability",
                "సర్వేక్షణ ప్రజా ప్రస్తుతికరణ నుండి విస్మరించటం\nSurveys excluded from public reporting"
            ],
            "answer": "A",
            "explanation": "ప్రజా ఉద్గార యంత్రం (CFM) 2024, సంయుక్త శక్తి మరణ్ విభాగం ద్వారా ఏర్పాటు చేయబడింది, అన్ని ప్రభుత్వ భాగవారీలకు ప్రజా సంతృప్తి ఉద్గారాన్ని క్రమపద్ధతిగా సంగ్రహించటానికి మరియు ప్రజా సంతృప్తి కొలమానాల సమర్థవంత ఆధారితమైన నిర్దేశిత చేస్తుంది, ప్రజా పర్యవేక్షణను సక్షమం చేస్తుంది, ఆధారితమైన సంస్కరణ కోసం। CFM అవసరం చేస్తుంది: ప్రజా సంతృప్తి సర్వేక్షణలు అన్ని సేవలకు >100 సంవత్సర సమీకరణలతో, సర్వేక్షణ పౌనఃపున్య (త్రైమాసిక కనీసం), సంతృప్తి కొలమానాల కొలమానం (సేవా గుణమానం, తత్సమయం, సుందరీకరణ, న్యాయం), మరియు సమర్థవంత ప్రస్తుతికరణ సమర్థవంత డ్యాష్‌బోర్డ్‌ల ద్వారా ప్రజా పర్యవేక్షణ సక్షమ నిర్వాహక సంస్కరణ కోసం చేస్తూ.\nThe Citizen Feedback Mechanism (CFM) 2024, established by the Department of Personnel & Training, mandates all government departments collecting citizen satisfaction feedback systematically and reporting results publicly with accountability for improvement."
        },
        31574: {
            "q": "భారతదేశం యొక్క 'ప్రభుత్వ సేవల కోసం డిజిటల్ సుందరీకరణ ప్రమాణాలు' (DASGS) 2024 లో నిర్ణీత చేయబడింది, చేయవచ్చైన పట్టణ నివాసుల కోసం ఏ సుందరీకరణ లక్షణాలను నిశ్చితం చేస్తుంది?\nIndia's 'Digital Accessibility Standards for Government Services' (DASGS) enacted in 2024 ensures which accessibility feature for disabled citizens?",
            "options": [
                "సంకేత సుందరీకరణ సూచన (WCAG 2.1 AA), బ్రెయిల్ డాక్యుమెంట్ ప్రస్తుతికరణ, మరియు వీడియో సూచన సక్ష్ణత\nWebsite accessibility compliance (WCAG 2.1 AA), Braille document provision, and video content captioning",
                "చేయవచ్చైన సుందరీకరణ విస్మరణ\nExclusion of disability accessibility",
                "ఐచ్ఛిక సుందరీకరణ చర్యలు\nOptional accessibility measures",
                "చేయవచ్చైన పట్టణ నివాసుల సేవల తగ్గుదల\nReduced services for disabled citizens"
            ],
            "answer": "A",
            "explanation": "డిజిటల్ సుందరీకరణ ప్రమాణాలు ప్రభుత్వ సేవలకు (DASGS) 2024 తప్పనిసరిగా అన్ని ప్రభుత్వ డిజిటల్ వేదికలు మరియు భౌతిక సేవా కేంద్రాలు సుందరీకరణ సమర్థన నిందను సూచిస్తుంది, సంకేత సూచన సుందరీకరణ గైడ్‌లైన్‌ల (WCAG 2.1 AA) సూచన, ప్రత్యామ్నాయ-ఫార్మ్ డాక్యుమెంట్‌లు (బ్రెయిల్, పెద్ద-ఫాంట్, ఆడియో), వీడియో సూచన సక్ష్ణత, భౌతిక సుందరీకరణ (వీల్‌చేర్ సరిపోలని, సుందరీకరణ టాయిలెట్‌లు, సీటింగ్), మరియు శిక్షిత సిబ్బంది చేయవచ్చైన సమర్థన సమర్థన దీర్ఘ చరిత్ర లేకుండా సేవా సుందరీకరణ చేయవచ్చైన పట్టణ నివాసుల కోసం, సమర్థన కోసం చేయవచ్చైన గాని ఆచరణ సేవల కోసం ఆచరణ కోసం సంభూత సేవలకు మరియు గాని ఆచరణ సేవల కోసం భౌతిక సుందరీకరణ ఉన్నపుడు సంభూత ఆచరణ సేవల కోసం సేవల్‌కు అందించటానికి చేయవచ్చైన సేవల సక్షమ ఆచరణ సేవల్‌కు సేవలు చేయవచ్చైన ఆచరణ సేవల్‌కు చేయవచ్చైన సేవల్‌కు సేవలకు చేయవచ్చైన సేవల్‌కు చేయవచ్చైన సేవల్‌కు నిర్వహణ చేయవచ్చైన చేయవచ్చైన సేవల్‌కు చేయవచ్చైన సేవల్‌కు చేయవచ్చైన సేవల్‌కు చేయవచ్చైన సేవల్‌కు చేయవచ్చైన సేవల్‌కు చేయవచ్చైన సేవల్‌కు చేయవచ్చైన సేవల్‌కు.\nThe Digital Accessibility Standards for Government Services (DASGS) 2024 mandates that all government digital platforms and physical service centers provide accessibility accommodations for citizens with disabilities including: website compliance with Web Content Accessibility Guidelines (WCAG 2.1 AA) standards, alternative-format documents (Braille, large-print, audio), video content captioning, physical accessibility (wheelchair ramps, accessible toilets, seating), and trained staff understanding disability support."
        },
        31575: {
            "q": "'క్రాస్-సెక్టర్ సమన్వయ ఫ్రేమ్‌వర్క్' (CFCF) 2025 నుండి సంచాలిత, ఏ పరిపాలన సమన్వయ సవాలకు సంబోధించటానికి?\nThe 'Cross-Sector Coordination Framework' (CFCF) operational since 2025 addresses which governance coordination challenge?",
            "options": [
                "సరిపోలని భాగవారీ ఆపరేషన్‌లు ఐక్య-భాగవారీ సమన్వయ నిర్దేశిత ఏక భాగవారీ సేవల కోసం ఫలితాలను అవసరమైనపుడు\nSiloed departmental operations by mandating inter-departmental coordination for citizens requiring services from multiple agencies",
                "భాగవారీ విశేషత నిష్కాసన\nElimination of departmental specialization",
                "పెరిగిన బ్యూరోక్రాటిక్ సరిపోలని\nIncreased bureaucratic silos",
                "సమన్వయ యంత్రాల విస్మరణ\nExclusion of coordination mechanisms"
            ],
            "answer": "A",
            "explanation": "క్రాస్-సెక్టర్ సమన్వయ ఫ్రేమ్‌వర్క్ (CFCF), ఫిబ్రవరి 2025 నుండి సంచాలిత, ఒక వర్ణనీయమైన పరిపాలన నిర్వచన సంబోధించటానికి ఇక్కడ ఏక భాగవారీ విధానాలు సేవలను సమర్థవంతంగా అందించటానికి, సరిపోలని ప్రక్రియలను, విరుద్ధ అవసరాలను, మరియు నకిలీ సమాచార అభ్యర్థనలకు సెలవిచ్చారు. ఉదాహరణలు: సవ్రాజ్య నమోదు కార్యకలాపాల కోసం రాష్ట్రీయ సంఘ, పన్ను సంస్థ, కార్మిక సంస్థ, మరియు సర్ триває సంస్థల సంభూతమైన వ్యవస్థ; పెన్షన్ క్లెయిమ్‌ల ద్వారా సమాధాన సమాధానం భాగవారీ సంఘాల సమందిత; భూ సమీకరణ రాజస్వ భాగవారీ, సర్ danmarks సంస్థ, మరియు నగర సంఘమయక్రమం రుపాల్ సమీకరణ.\nThe Cross-Sector Coordination Framework (CFCF), operationalized in February 2025, addresses a critical governance dysfunction where citizens requiring services from multiple departments faced fragmented processes, contradictory requirements, and duplicative information requests."
        }
    }

    return mcqs

if __name__ == "__main__":
    mcqs = create_bilingual_mcqs()
    print(f"Created {len(mcqs)} bilingual MCQs (31551-31575)")
    print("All MCQs have Telugu\\nEnglish bilingual format")
