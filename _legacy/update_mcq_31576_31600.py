#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add Telugu translations to MCQs 31576-31600
"""

import re

# Read the seed file
with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Define MCQ updates with Telugu translations
updates = {
    31576: {
        'question': "'రాజ్య సేవా శ్రేష్ఠత్వ సూచిక' (GSEI) 2024 నుండి కార్యచరణ ప్రారంభించినది ప్రభుత్వ సేవలను ఎన్ని ప్రమాణీకృత కొలతల ద్వారా మూల్యాంకనం చేస్తుంది?\n(The 'Government Service Excellence Index' (GSEI) operational since 2024 evaluates government services on how many standardized dimensions?)",
        'options': {
            'A': "'ఎight కొలతలు: పనితీరు, నాణ్యత, సరాసరి సులభం, పారదర్శకత, ప్రతిక్రియాశీలత, జవాబుదారితనం, సమానత్వం మరియు ఆవిష్కరణ / Eight dimensions: efficiency, quality, accessibility, transparency, responsiveness, accountability, equity, and innovation'",
            'B': "'ఒక కొలత మాత్రమే / Single metric only'",
            'C': "'పన్నెండు ఏకపక్ష కొలతలు / Twelve arbitrary measures'",
            'D': "'ప్రమాణీకృత మూల్యాంకనం లేనిది / No standardized evaluation'"
        }
    },
    31577: {
        'question': "'సమన్విత జిల్లా పరిపాలన' (IDA) మోడల్ 34 జిల్లాలలో అమలు చేయబడినది ఏ యంత్రం ద్వారా జిల్లా-స్థాయి సమన్వయాన్ని సమీకరించాలి?\n(The 'Integrated District Administration' (IDA) model implemented in 34 districts consolidates district-level coordination through which mechanism?)",
        'options': {
            'A': "'ఎక జిల్లా-స్థాయి పాలన సెల్‌ అన్నీ జిల్లా ఏజెంసీలు మరియు సేవలపై సమన్వయ పాత్రతో / Single district-level governance cell with coordinating role across all district agencies and services'",
            'B': "'జిల్లా పరిపాలన యొక్క తొలగింపు / Elimination of district administration'",
            'C': "'ఏజెన్సీ విकేంద్రీకరణ సమన్వయ లేకుండా / Agency decentralization without coordination'",
            'D': "'రాష్ట్ర రాజధానులకు కేంద్రీకరణ / Centralization to state capitals'"
        }
    },
    31578: {
        'question': "'ఖచ్చితమైన పరిస్థితి బహిర్గతకారి సంరక్షణ మరియు ప్రేరణ పథకం' (WPIS) 2024 ఏ నిర్దిష్ట సంరక్షణలు మరియు ప్రోత్సాహనలను అందిస్తుంది?\n(The 'Whistleblower Protection and Incentivization Scheme' (WPIS) of 2024 provides which specific protections and incentives?)",
        'options': {
            'A': "'రహస్య ఫిర్యాదు చానెల్‌లు, సమాచారం బహిర్గతం చేసే అధికారుల స్థానాంతర సంరక్షణలు మరియు అవిశ్వాస్యతా సమాచారం కోసం నిర్ణయించిన వేతనాలు / Confidential complaint channels, transfer protections for reporting officials, and financial rewards for corruption-exposing information'",
            'B': "'పగటాలు నుండి ఉరకాటి కాదు / No protection from retaliation'",
            'C': "'బహిర్గతకారుల సమర్థ సార్వజనిక గుర్తింపు నిర్దేశన / Mandatory public identification of whistleblowers'",
            'D': "'సమాచారం ఫిర్యాదు యంత్రాల తొలగింపు / Elimination of reporting mechanisms'"
        }
    },
    31579: {
        'question': "'సమీకరణ పరిపాలన' 2025 సంచారం విధానం చేయడం మరియు అమలు చేయడంలో ఏ పరిపాలన సూత్రాన్ని ఎక్కువగా చేస్తుంది?\n(The 'Adaptive Governance' initiative of 2025 emphasizes which administrative principle in policy-making and implementation?)",
        'options': {
            'A': "'నిరంతర మూల్యాంకనం మరియు వాస్తవ-సంచారం అభిజ్ఞతా ఫిర్యాదు మరియు ఫలితం ఆధారిత విధానం సమీకరణ / Continuous evaluation and iterative policy adjustment based on real-world implementation feedback and outcome data'",
            'B': "'సమాచారం ఉనికోకు విధానాలు మార్చుకోను / Fixed policies unchanged despite evidence'",
            'C': "'విధానం సాక్ష్యాన్ని తొలగింపు / Elimination of policy evaluation'",
            'D': "'సమీకరణ సమీకరణ నుండి నాగరిక ఫిర్యాదు విస్మరణ / Exclusion of citizen feedback from policy'"
        }
    },
    31580: {
        'question': "'ఆర్థిక అభివృద్ధి కోసం పాలన' 2025 పరిపాలన జవాబుదారితనాన్ని విధానం లక్ష్యాన్ని సాధించడంతో ఏ ఫలితం కొలతలను సమీకరిస్తుంది?\n(India's 'Governance for Development' framework of 2025 integrates administrative accountability with which outcome measurement?)",
        'options': {
            'A': "'విధానం లక్ష్యాల సాధన (దారిద్ర్య నిమ్నీకరణ, విద్యా సంభందం, ఆరోగ్య ఫలితాలు) పరిపాలన కార్యకర్త సంబంధిత సమీకరణ సూచికలుగా / Achievement of development objectives (poverty reduction, education access, health outcomes) as determinants of administrative effectiveness evaluation'",
            'B': "'పలు గణన కొలతలు విధానం తక్కువ విషయమైతే / Only output metrics regardless of outcomes'",
            'C': "'దారిద్ర్య నిమ్నీకరణ ఫోకస్ యొక్క తొలగింపు / Elimination of poverty reduction focus'",
            'D': "'ఆరోగ్య ఫలితాల సంబంధిత సమీకరణ నుండి విస్మరణ / Exclusion of health outcomes from assessment'"
        }
    },
    31581: {
        'question': "డిసెంబర్ 2018లో ప్రారంభించిన PM-కిసాన్ పథకం యొక్క ప్రధాన లక్ష్యం ఏమిటి?\n(What is the primary objective of PM-KISAN scheme launched in December 2018?)",
        'options': {
            'A': "'అన్ని భూ-సంధ్య సంధ్యకులకు సమర్థ ఆదాయ సహాయం ఇవ్వడం / Provide direct income support to all farmers'",
            'B': "'సిద్ధం బునియాది ఢాంచా అభివృద్ధి / Develop irrigation infrastructure'",
            'C': "'సహజ గృహ నిర్మాణ కోసం ప్రోత్సాహన / Promote organic farming'",
            'D': "'సారం ఏ సంబంధిత సాధనాలకు అందుబాటు / Subsidize fertilizers and pesticides'"
        }
    },
    31582: {
        'question': "2026లో PM-కిసాన్ పథకం ప్రకారం పట్టి సంధ్య సంధ్యకులకు వార్షిక ఎంత ఆర్థిక సహాయం ఇవ్వబడుతుంది?\n(Under PM-KISAN scheme, how much financial assistance is provided annually to eligible farmers in 2026?)",
        'options': {
            'A': "'రూ. 2,000 / Rs. 2,000'",
            'B': "'రూ. 4,000 / Rs. 4,000'",
            'C': "'రూ. 6,000 / Rs. 6,000'",
            'D': "'రూ. 8,000 / Rs. 8,000'"
        }
    },
    31583: {
        'question': "PM గతి శక్తి జాతీయ మాస్టర్ ప్లాన్ అమలుకోసం ఏ మంత్రాలయ విధానం ఉండాలి?\n(Which ministry oversees the implementation of PM Gati Shakti National Master Plan?)",
        'options': {
            'A': "'గ్రామీణ అభివృద్ధి మంత్రాలయ / Ministry of Rural Development'",
            'B': "'వాణిజ్యం మరియు పరిశ్రమ మంత్రాలయ / Ministry of Commerce & Industry'",
            'C': "'బునియాది ఢాంచా, గృహ నిర్మాణం మరియు నగర విషయాల మంత్రాలయ / Ministry of Infrastructure, Housing and Urban Affairs'",
            'D': "'ఆర్థిక మంత్రాలయ / Ministry of Finance'"
        }
    },
    31584: {
        'question': "PM గతి శక్తి జాతీయ మాస్టర్ ప్లాన్ (2021-2026) కోసం కుల బడ్జెట్ నిధులు ఎంత?\n(What is the total budget allocation for PM Gati Shakti National Master Plan (2021-2026)?)",
        'options': {
            'A': "'రూ. 50 లక్ష కోట్లు / Rs. 50 lakh crore'",
            'B': "'రూ. 111 లక్ష కోట్లు / Rs. 111 lakh crore'",
            'C': "'రూ. 150 లక్ష కోట్లు / Rs. 150 lakh crore'",
            'D': "'రూ. 200 లక్ష కోట్లు / Rs. 200 lakh crore'"
        }
    },
    31585: {
        'question': "NRLM (జాతీయ గ్రామీణ జీవనోపాధి కర్మసూచి) ప్రధానంగా గ్రామీణ అభివృద్ధిలో ఏ అంశంపై ఫోకస్ చేస్తుంది?\n(NRLM (National Rural Livelihoods Mission) primarily focuses on which aspect of rural development?)",
        'options': {
            'A': "'భూమి పునర్విభజన కార్యక్రమాలు / Land redistribution programs'",
            'B': "'ఉపयोగ అభివృద్ధి మరియు స్వ-ఉపజీవనం ద్వారా దరిద్రత్వ తగ్గింపు / Poverty reduction through skill development and self-employment'",
            'C': "'ఆహార ధాన్య పంపిణీ / Food grain distribution'",
            'D': "'జల సంపద నిర్వహణ / Water resource management'"
        }
    },
    31586: {
        'question': "మే 2026 నాటికి NRLM ప్రకారం ఎన్ని స్వయం సహాయ సమూహాలు (SHGs) ఏర్పాటయ్యాయి?\n(How many Self Help Groups (SHGs) have been formed under NRLM as of May 2026?)",
        'options': {
            'A': "'75 లక్ష / 75 lakh'",
            'B': "'1.25 కోటి / 1.25 crore'",
            'C': "'1.75 కోటి / 1.75 crore'",
            'D': "'2.5 కోటి / 2.5 crore'"
        }
    },
    31587: {
        'question': "ప్రధాన మంత్రి కౌశల్ విकాస యోజన (PMKVY) ప్రకారం ప్రధాన ఫోకస్ ఏమిటి?\n(Under the Pradhan Mantri Kaushal Vikas Yojana (PMKVY), what is the primary focus?)",
        'options': {
            'A': "'కృషి ఉపయోగ అభివృద్ధి / Agricultural skill development'",
            'B': "'పారిశ్రామిక ఉపయోగ అభివృద్ధి మరియు వృత్తిమత్తర శిక్షణ / Industrial skill development and vocational training'",
            'C': "'IT సెక్టర్ శిక్షణ / IT sector training'",
            'D': "'భాష నేర్చుకోవడం కార్యక్రమాలు / Language learning programs'"
        }
    },
    31588: {
        'question': "మే 2026 నాటికి, PMKVY ప్రకారం సుమారుగా ఎన్ని యువకులకు శిక్షణ ఇవ్వబడింది?\n(As of May 2026, approximately how many youth have been trained under PMKVY?)",
        'options': {
            'A': "'6 కోటి / 6 crore'",
            'B': "'9 కోటి / 9 crore'",
            'C': "'1.2 కోటి / 1.2 crore'",
            'D': "'1.8 కోటి / 1.8 crore'"
        }
    },
    31589: {
        'question': "ఏ ప్రభుత్వ పథకం ఆర్థిక సంభందం ద్వారా మహిళా సాధికారత లక్ష్యీకరిస్తుంది?\n(Which government scheme specifically targets women empowerment through financial inclusion?)",
        'options': {
            'A': "'సుకన్య సమృద్ధి యోజన / Sukanya Samriddhi Yojana'",
            'B': "'ప్రధాన మంత్రి మహిళా శక్తి కేంద్రం / Pradhan Mantri Mahila Shakti Kendra'",
            'C': "'ప్రధాన మంత్రి ముద్రా యోజన / Pradhan Mantri Mudra Yojana'",
            'D': "'ఉజ్జ్వల యోజన / Ujjwala Yojana'"
        }
    },
    31590: {
        'question': "మే 2026 నాటికి, ప్రధాన మంత్రి ముద్రా యోజన ప్రకారం కుల వితరణ చేసిన మొత్తం ఎంత?\n(As of May 2026, what is the total amount disbursed under Pradhan Mantri Mudra Yojana?)",
        'options': {
            'A': "'రూ. 5 లక్ష కోట్లు / Rs. 5 lakh crore'",
            'B': "'రూ. 10 లక్ష కోట్లు / Rs. 10 lakh crore'",
            'C': "'రూ. 20 లక్ష కోట్లు / Rs. 20 lakh crore'",
            'D': "'రూ. 30 లక్ష కోట్లు / Rs. 30 lakh crore'"
        }
    },
    31591: {
        'question': "ప్రధాన మంత్రి వయ వందన యోజన (PMVVY) యొక్క ప్రధాన లక్ష్యం ఏమిటి?\n(What is the primary objective of the Pradhan Mantri Vaya Vandana Yojana (PMVVY)?)",
        'options': {
            'A': "'వయస్సైన నాగరికులకు ఆరోగ్య బీమా ఇవ్వడం / Provide health insurance to senior citizens'",
            'B': "'60 సంవత్సరాలు మరియు అంతకంటే ఎక్కువ వయస్సు నాగరికులకు పენ్షన్ సహాయం ఇవ్వడం / Provide pension support to senior citizens aged 60 and above'",
            'C': "'వయస్సైన నాగరికులకు సబ్సిడీ ఆవాస ఇవ్వడం / Provide subsidized housing to senior citizens'",
            'D': "'వయస్సైన నాగరికులకు ఉచిత కదలిక సాధనాలు ఇవ్వడం / Provide free mobility aids to senior citizens'"
        }
    },
    31592: {
        'question': "మే 2026 నాటికి, ప్రధాన మంత్రి వయ వందన యోజన ప్రకారం ఎన్ని వయస్సైన నాగరికులను నమోదు చేసారు?\n(How many senior citizens have been enrolled under Pradhan Mantri Vaya Vandana Yojana as of May 2026?)",
        'options': {
            'A': "'50 లక్ష / 50 lakh'",
            'B': "'1 కోటి / 1 crore'",
            'C': "'1.8 కోటి / 1.8 crore'",
            'D': "'2.5 కోటి / 2.5 crore'"
        }
    },
    31593: {
        'question': "ఏ పథకం వికలాంగ వ్యక్తుల పునర్వాస మరియు సంక్షేమ కోసం ఆర్థిక సహాయం ఇస్తుంది?\n(Which scheme provides financial assistance for the rehabilitation and welfare of persons with disabilities?)",
        'options': {
            'A': "'ఇందిరా గాంధీ జాతీయ వికలాంగత పెన్షన్ పథకం / Indira Gandhi National Disability Pension Scheme'",
            'B': "'రాజీవ్ గాంధీ కిశోరీ సాధికారత పథకం / Rajiv Gandhi Scheme for Empowerment of Adolescent Girls'",
            'C': "'జాతీయ బాల శ్రమ ప్రకల్పన / National Child Labour Project'",
            'D': "'సమన్విత బాల అభివృద్ధి పథకం / Integrated Child Development Scheme'"
        }
    },
    31594: {
        'question': "మే 2026 నాటికి, వికలాంగత పెన్షన్ పథకాల ప్రకారం ఎన్ని వికలాంగ వ్యక్తులు చేర్చబడ్డారు?\n(As of May 2026, how many persons with disabilities have been covered under disability pension schemes?)",
        'options': {
            'A': "'1.5 కోటి / 1.5 crore'",
            'B': "'2.3 కోటి / 2.3 crore'",
            'C': "'3.2 కోటి / 3.2 crore'",
            'D': "'4.5 కోటి / 4.5 crore'"
        }
    },
    31595: {
        'question': "ప్రధాన మంత్రి మాతృత్వ వందన యోజన (PMMVY) యొక్క ప్రధాన ఫోకస్ ఏమిటి?\n(What is the primary focus of the Pradhan Mantri Matritva Vandana Yojana (PMMVY)?)",
        'options': {
            'A': "'బాలికల విద్యకు విద్య ఉపకరణాలు ఇవ్వడం / Provide scholarships for girls' education'",
            'B': "'గర్భవతి మహిళలకు మరియు పాలిస్తున్న తల్లులకు ప్రసవ లాభాలు మరియు నగదు సహాయం ఇవ్వడం / Provide maternity benefits and cash assistance to pregnant women and lactating mothers'",
            'C': "'మహిళలకు ఉచిత ఆరోగ్యసేవలు ఇవ్వడం / Provide free healthcare to women'",
            'D': "'గర్భవతి మహిళలకు సబ్సిడీ పోషకాహార భోజనం ఇవ్వడం / Provide subsidized nutritious food to pregnant women'"
        }
    },
    31596: {
        'question': "మే 2026 నాటికి, ఎన్ని గర్భవతి మహిళలకు మరియు పాలిస్తున్న తల్లులకు PMMVY నుండి లాభం పొందారు?\n(As of May 2026, how many pregnant women and lactating mothers have benefited from PMMVY?)",
        'options': {
            'A': "'75 లక్ష / 75 lakh'",
            'B': "'1.2 కోటి / 1.2 crore'",
            'C': "'2.1 కోటి / 2.1 crore'",
            'D': "'3 కోటి / 3 crore'"
        }
    },
    31597: {
        'question': "ప్రధాన మంత్రి ఆవాస యోజన (సొందరికి ఆవాస) యొక్క ప్రధాన ఉద్దేశ్యం ఏమిటి?\n(What is the key objective of the Pradhan Mantri Awas Yojana (Housing for All)?)",
        'options': {
            'A': "'భారతదేశ వ్యాపకంగా వాణిజ్య భవనాల నిర్మాణం / Construct commercial buildings across India'",
            'B': "'2023 నాటికి (2025 నాటికి పెరిగి) అన్ని భారతీయ కుటుంబాలకు సస్తతరమైన ఆవాసం ఇవ్వడం / Provide affordable housing to all Indian families by 2023 (extended to 2025)'",
            'C': "'అధిక-ఆదాయ కుటుంబాలకు విలాసవంత ఆవాస ఇవ్వడం / Provide luxury housing to high-income families'",
            'D': "'పట్టణ ప్రాంతాలలో వాణిజ్య రియల్ ఎస్టేట్ అభివృద్ధి / Develop commercial real estate in urban areas'"
        }
    },
    31598: {
        'question': "మే 2026 నాటికి, ప్రధాన మంత్రి ఆవాస యోజన ప్రకారం ఎన్ని ఇళ్ళు పూర్తిచేసారు?\n(As of May 2026, how many houses have been completed under Pradhan Mantri Awas Yojana?)",
        'options': {
            'A': "'1 కోటి / 1 crore'",
            'B': "'1.8 కోటి / 1.8 crore'",
            'C': "'2.8 కోటి / 2.8 crore'",
            'D': "'3.5 కోటి / 3.5 crore'"
        }
    },
    31599: {
        'question': "ఆధార్-ఆధారిత చెల్లింపు వ్యవస్థ ద్వారా పేదలకు నేరుగా నగదు బదిలీ సహాయం ఇస్తున్న ఏ పథకం ఉందని?\n(Which scheme provides direct cash transfer assistance to the poor through Aadhaar-based payment systems?)",
        'options': {
            'A': "'సార్వజనిక పంపిణీ వ్యవస్థ / Public Distribution System'",
            'B': "'ప్రధాన మంత్రి జన ధన్ యోజన / Pradhan Mantri Jan Dhan Yojana'",
            'C': "'వయస్సైన నాగరికుల సేవల సమీకృత పథకం / Integrated Scheme for Services to Senior Citizens'",
            'D': "'జాతీయ ఆహార సంరక్షణ పథకం / National Food Security Scheme'"
        }
    },
    31600: {
        'question': "మే 2026 నాటికి, PMJDY ప్రకారం ఎన్ని జన ధన్ ఖాతాలు తెరవబడ్డాయి?\n(As of May 2026, how many Jan Dhan accounts have been opened under PMJDY?)",
        'options': {
            'A': "'25 కోటి / 25 crore'",
            'B': "'35 కోటి / 35 crore'",
            'C': "'48 కోటి / 48 crore'",
            'D': "'55 కోటి / 55 crore'"
        }
    }
}

# Now let's create the replacements for the seed file
for mcq_id in range(31576, 31601):
    if mcq_id in updates:
        update_info = updates[mcq_id]

        # Pattern to find MCQ - using more flexible regex
        # This will match the tuple structure for this specific MCQ ID

print("Updates prepared for MCQs 31576-31600")
print(f"Total updates: {len(updates)}")
for mcq_id in sorted(updates.keys()):
    print(f"  {mcq_id}: Ready")
