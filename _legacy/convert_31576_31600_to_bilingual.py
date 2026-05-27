#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert MCQs 31576-31600 from Hindi to Telugu+English bilingual format
Reading from seed_national_ca_2026_mcq.py
"""

import re
import sys

# MCQ data from the update_mcq_31576_31600.py with bilingual Telugu+English questions
mcq_bilingual_data = {
    31576: {
        'question': "రాజ్య సేవా శ్రేష్ఠత్వ సూచిక' (GSEI) 2024 నుండి కార్యచరణ ప్రారంభించినది ప్రభుత్వ సేవలను ఎన్ని ప్రమాణీకృత కొలతల ద్వారా మూల్యాంకనం చేస్తుంది?\n(The 'Government Service Excellence Index' (GSEI) operational since 2024 evaluates government services on how many standardized dimensions?)",
        'optA': "Eight dimensions: efficiency, quality, accessibility, transparency, responsiveness, accountability, equity, and innovation\nఎight కొలతలు: పనితీరు, నాణ్యత, సరాసరి సులభం, పారదర్శకత, ప్రతిక్రియాశీలత, జవాబుదారితనం, సమానత్వం మరియు ఆవిష్కరణ",
        'optB': "Single metric only\nఒక కొలత మాత్రమే",
        'optC': "Twelve arbitrary measures\nపన్నెండు ఏకపక్ష కొలతలు",
        'optD': "No standardized evaluation\nప్రమాణీకృత మూల్యాంకనం లేనిది",
        'answer': 'A',
    },
    31577: {
        'question': "సమన్విత జిల్లా పరిపాలన' (IDA) మోడల్ 34 జిల్లాలలో అమలు చేయబడినది ఏ యంత్రం ద్వారా జిల్లా-స్థాయి సమన్వయాన్ని సమీకరించాలి?\n(The 'Integrated District Administration' (IDA) model implemented in 34 districts consolidates district-level coordination through which mechanism?)",
        'optA': "Single district-level governance cell with coordinating role across all district agencies and services\nఎక జిల్లా-స్థాయి పాలన సెల్‌ అన్నీ జిల్లా ఏజెంసీలు మరియు సేవలపై సమన్వయ పాత్రతో",
        'optB': "Elimination of district administration\nజిల్లా పరిపాలన యొక్క తొలగింపు",
        'optC': "Agency decentralization without coordination\nఏజెన్సీ వికేంద్రీకరణ సమన్వయ లేకుండా",
        'optD': "Centralization to state capitals\nరాష్ట్ర రాజధానులకు కేంద్రీకరణ",
        'answer': 'A',
    },
    31578: {
        'question': "ఖచ్చితమైన పరిస్థితి బహిర్గతకారి సంరక్షణ మరియు ప్రేరణ పథకం' (WPIS) 2024 ఏ నిర్దిష్ట సంరక్షణలు మరియు ప్రోత్సాహనలను అందిస్తుంది?\n(The 'Whistleblower Protection and Incentivization Scheme' (WPIS) of 2024 provides which specific protections and incentives?)",
        'optA': "Confidential complaint channels, transfer protections for reporting officials, and financial rewards for corruption-exposing information\nరహస్య ఫిర్యాదు చానెల్‌లు, సమాచారం బహిర్గతం చేసే అధికారుల స్థానాంతర సంరక్షణలు మరియు అవిశ్వాస్యతా సమాచారం కోసం నిర్ణయించిన వేతనాలు",
        'optB': "No protection from retaliation\nపగటాలు నుండి ఉరకాటి కాదు",
        'optC': "Mandatory public identification of whistleblowers\nబహిర్గతకారుల సమర్థ సార్వజనిక గుర్తింపు నిర్దేశన",
        'optD': "Elimination of reporting mechanisms\nసమాచారం ఫిర్యాదు యంత్రాల తొలగింపు",
        'answer': 'A',
    },
    31579: {
        'question': "సమీకరణ పరిపాలన' 2025 సంచారం విధానం చేయడం మరియు అమలు చేయడంలో ఏ పరిపాలన సూత్రాన్ని ఎక్కువగా చేస్తుంది?\n(The 'Adaptive Governance' initiative of 2025 emphasizes which administrative principle in policy-making and implementation?)",
        'optA': "Continuous evaluation and iterative policy adjustment based on real-world implementation feedback and outcome data\nనిరంతర మూల్యాంకనం మరియు వాస్తవ-సంచారం అభిజ్ఞతా ఫిర్యాదు మరియు ఫలితం ఆధారిత విధానం సమీకరణ",
        'optB': "Fixed policies unchanged despite evidence\nసమాచారం ఉనికోకు విధానాలు మార్చుకోను",
        'optC': "Elimination of policy evaluation\nవిధానం సాక్ష్యాన్ని తొలగింపు",
        'optD': "Exclusion of citizen feedback from policy\nసమీకరణ సమీకరణ నుండి నాగరిక ఫిర్యాదు విస్మరణ",
        'answer': 'A',
    },
    31580: {
        'question': "ఆర్థిక అభివృద్ధి కోసం పాలన' 2025 పరిపాలన జవాబుదారితనాన్ని విధానం లక్ష్యాన్ని సాధించడంతో ఏ ఫలితం కొలతలను సమీకరిస్తుంది?\n(India's 'Governance for Development' framework of 2025 integrates administrative accountability with which outcome measurement?)",
        'optA': "Achievement of development objectives (poverty reduction, education access, health outcomes) as determinants of administrative effectiveness evaluation\nవిధానం లక్ష్యాల సాధన (దారిద్ర్య నిమ్నీకరణ, విద్యా సంభందం, ఆరోగ్య ఫలితాలు) పరిపాలన కార్యకర్త సంబంధిత సమీకరణ సూచికలుగా",
        'optB': "Only output metrics regardless of outcomes\nపలు గణన కొలతలు విధానం తక్కువ విషయమైతే",
        'optC': "Elimination of poverty reduction focus\nదారిద్ర్య నిమ్నీకరణ ఫోకస్ యొక్క తొలగింపు",
        'optD': "Exclusion of health outcomes from assessment\nఆరోగ్య ఫలితాల సంబంధిత సమీకరణ నుండి విస్మరణ",
        'answer': 'A',
    },
    31581: {
        'question': "డిసెంబర్ 2018లో ప్రారంభించిన PM-కిసాన్ పథకం యొక్క ప్రధాన లక్ష్యం ఏమిటి?\n(What is the primary objective of PM-KISAN scheme launched in December 2018?)",
        'optA': "Provide direct income support to all farmers\nఅన్ని భూ-సంధ్య సంధ్యకులకు సమర్థ ఆదాయ సహాయం ఇవ్వడం",
        'optB': "Develop irrigation infrastructure\nసిద్ధం బునియాది ఢాంచా అభివృద్ధి",
        'optC': "Promote organic farming\nసహజ గృహ నిర్మాణ కోసం ప్రోత్సాహన",
        'optD': "Subsidize fertilizers and pesticides\nసారం ఏ సంబంధిత సాధనాలకు అందుబాటు",
        'answer': 'A',
    },
    31582: {
        'question': "2026లో PM-కిసాన్ పథకం ప్రకారం పట్టి సంధ్య సంధ్యకులకు వార్షిక ఎంత ఆర్థిక సహాయం ఇవ్వబడుతుంది?\n(Under PM-KISAN scheme, how much financial assistance is provided annually to eligible farmers in 2026?)",
        'optA': "Rs. 2,000\nరూ. 2,000",
        'optB': "Rs. 4,000\nరూ. 4,000",
        'optC': "Rs. 6,000\nరూ. 6,000",
        'optD': "Rs. 8,000\nరూ. 8,000",
        'answer': 'C',
    },
    31583: {
        'question': "PM గతి శక్తి జాతీయ మాస్టర్ ప్లాన్ అమలుకోసం ఏ మంత్రాలయ విధానం ఉండాలి?\n(Which ministry oversees the implementation of PM Gati Shakti National Master Plan?)",
        'optA': "Ministry of Rural Development\nగ్రామీణ అభివృద్ధి మంత్రాలయ",
        'optB': "Ministry of Commerce & Industry\nవాణిజ్యం మరియు పరిశ్రమ మంత్రాలయ",
        'optC': "Ministry of Infrastructure, Housing and Urban Affairs\nబునియాది ఢాంచా, గృహ నిర్మాణం మరియు నగర విషయాల మంత్రాలయ",
        'optD': "Ministry of Finance\nఆర్థిక మంత్రాలయ",
        'answer': 'C',
    },
    31584: {
        'question': "PM గతి శక్తి జాతీయ మాస్టర్ ప్లాన్ (2021-2026) కోసం కుల బడ్జెట్ నిధులు ఎంత?\n(What is the total budget allocation for PM Gati Shakti National Master Plan (2021-2026)?)",
        'optA': "Rs. 50 lakh crore\nరూ. 50 లక్ష కోట్లు",
        'optB': "Rs. 111 lakh crore\nరూ. 111 లక్ష కోట్లు",
        'optC': "Rs. 150 lakh crore\nరూ. 150 లక్ష కోట్లు",
        'optD': "Rs. 200 lakh crore\nరూ. 200 లక్ష కోట్లు",
        'answer': 'B',
    },
    31585: {
        'question': "NRLM (జాతీయ గ్రామీణ జీవనోపాధి కర్మసూచి) ప్రధానంగా గ్రామీణ అభివృద్ధిలో ఏ అంశంపై ఫోకస్ చేస్తుంది?\n(NRLM (National Rural Livelihoods Mission) primarily focuses on which aspect of rural development?)",
        'optA': "Land redistribution programs\nభూమి పునర్విభజన కార్యక్రమాలు",
        'optB': "Poverty reduction through skill development and self-employment\nఉపయోగ అభివృద్ధి మరియు స్వ-ఉపజీవనం ద్వారా దరిద్రత్వ తగ్గింపు",
        'optC': "Food grain distribution\nఆహార ధాన్య పంపిణీ",
        'optD': "Water resource management\nజల సంపద నిర్వహణ",
        'answer': 'B',
    },
    31586: {
        'question': "మే 2026 నాటికి NRLM ప్రకారం ఎన్ని స్వయం సహాయ సమూహాలు (SHGs) ఏర్పాటయ్యాయి?\n(How many Self Help Groups (SHGs) have been formed under NRLM as of May 2026?)",
        'optA': "75 lakh\n75 లక్ష",
        'optB': "1.25 crore\n1.25 కోటి",
        'optC': "1.75 crore\n1.75 కోటి",
        'optD': "2.5 crore\n2.5 కోటి",
        'answer': 'C',
    },
    31587: {
        'question': "ప్రధాన మంత్రి కౌశల్ వికాస యోజన (PMKVY) ప్రకారం ప్రధాన ఫోకస్ ఏమిటి?\n(Under the Pradhan Mantri Kaushal Vikas Yojana (PMKVY), what is the primary focus?)",
        'optA': "Agricultural skill development\nకృషి ఉపయోగ అభివృద్ధి",
        'optB': "Industrial skill development and vocational training\nపారిశ్రామిక ఉపయోగ అభివృద్ధి మరియు వృత్తిమత్తర శిక్షణ",
        'optC': "IT sector training\nIT సెక్టర్ శిక్షణ",
        'optD': "Language learning programs\nభాష నేర్చుకోవడం కార్యక్రమాలు",
        'answer': 'B',
    },
    31588: {
        'question': "మే 2026 నాటికి, PMKVY ప్రకారం సుమారుగా ఎన్ని యువకులకు శిక్షణ ఇవ్వబడింది?\n(As of May 2026, approximately how many youth have been trained under PMKVY?)",
        'optA': "6 crore\n6 కోటి",
        'optB': "9 crore\n9 కోటి",
        'optC': "1.2 crore\n1.2 కోటి",
        'optD': "1.8 crore\n1.8 కోటి",
        'answer': 'C',
    },
    31589: {
        'question': "ఏ ప్రభుత్వ పథకం ఆర్థిక సంభందం ద్వారా మహిళా సాధికారత లక్ష్యీకరిస్తుంది?\n(Which government scheme specifically targets women empowerment through financial inclusion?)",
        'optA': "Sukanya Samriddhi Yojana\nసుకన్య సమృద్ధి యోజన",
        'optB': "Pradhan Mantri Mahila Shakti Kendra\nప్రధాన మంత్రి మహిళా శక్తి కేంద్రం",
        'optC': "Pradhan Mantri Mudra Yojana\nప్రధాన మంత్రి ముద్రా యోజన",
        'optD': "Ujjwala Yojana\nఉజ్జ్వల యోజన",
        'answer': 'C',
    },
    31590: {
        'question': "మే 2026 నాటికి, ప్రధాన మంత్రి ముద్రా యోజన ప్రకారం కుల వితరణ చేసిన మొత్తం ఎంత?\n(As of May 2026, what is the total amount disbursed under Pradhan Mantri Mudra Yojana?)",
        'optA': "Rs. 5 lakh crore\nరూ. 5 లక్ష కోట్లు",
        'optB': "Rs. 10 lakh crore\nరూ. 10 లక్ష కోట్లు",
        'optC': "Rs. 20 lakh crore\nరూ. 20 లక్ష కోట్లు",
        'optD': "Rs. 30 lakh crore\nరూ. 30 లక్ష కోట్లు",
        'answer': 'C',
    },
    31591: {
        'question': "ప్రధాన మంత్రి వయ వందన యోజన (PMVVY) యొక్క ప్రధాన లక్ష్యం ఏమిటి?\n(What is the primary objective of the Pradhan Mantri Vaya Vandana Yojana (PMVVY)?)",
        'optA': "Provide health insurance to senior citizens\nవయస్సైన నాగరికులకు ఆరోగ్య బీమా ఇవ్వడం",
        'optB': "Provide pension support to senior citizens aged 60 and above\n60 సంవత్సరాలు మరియు అంతకంటే ఎక్కువ వయస్సు నాగరికులకు పెన్షన్ సహాయం ఇవ్వడం",
        'optC': "Provide subsidized housing to senior citizens\nవయస్సైన నాగరికులకు సబ్సిడీ ఆవాస ఇవ్వడం",
        'optD': "Provide free mobility aids to senior citizens\nవయస్సైన నాగరికులకు ఉచిత కదలిక సాధనాలు ఇవ్వడం",
        'answer': 'B',
    },
    31592: {
        'question': "మే 2026 నాటికి, ప్రధాన మంత్రి వయ వందన యోజన ప్రకారం ఎన్ని వయస్సైన నాగరికులను నమోదు చేసారు?\n(How many senior citizens have been enrolled under Pradhan Mantri Vaya Vandana Yojana as of May 2026?)",
        'optA': "50 lakh\n50 లక్ష",
        'optB': "1 crore\n1 కోటి",
        'optC': "1.8 crore\n1.8 కోటి",
        'optD': "2.5 crore\n2.5 కోటి",
        'answer': 'C',
    },
    31593: {
        'question': "ఏ పథకం వికలాంగ వ్యక్తుల పునర్వాస మరియు సంక్షేమ కోసం ఆర్థిక సహాయం ఇస్తుంది?\n(Which scheme provides financial assistance for the rehabilitation and welfare of persons with disabilities?)",
        'optA': "Indira Gandhi National Disability Pension Scheme\nఇందిరా గాంధీ జాతీయ వికలాంగత పెన్షన్ పథకం",
        'optB': "Rajiv Gandhi Scheme for Empowerment of Adolescent Girls\nరాజీవ్ గాంధీ కిశోరీ సాధికారత పథకం",
        'optC': "National Child Labour Project\nజాతీయ బాల శ్రమ ప్రకల్పన",
        'optD': "Integrated Child Development Scheme\nసమన్విత బాల అభివృద్ధి పథకం",
        'answer': 'A',
    },
    31594: {
        'question': "మే 2026 నాటికి, వికలాంగత పెన్షన్ పథకాల ప్రకారం ఎన్ని వికలాంగ వ్యక్తులు చేర్చబడ్డారు?\n(As of May 2026, how many persons with disabilities have been covered under disability pension schemes?)",
        'optA': "1.5 crore\n1.5 కోటి",
        'optB': "2.3 crore\n2.3 కోటి",
        'optC': "3.2 crore\n3.2 కోటి",
        'optD': "4.5 crore\n4.5 కోటి",
        'answer': 'B',
    },
    31595: {
        'question': "ప్రధాన మంత్రి మాతృత్వ వందన యోజన (PMMVY) యొక్క ప్రధాన ఫోకస్ ఏమిటి?\n(What is the primary focus of the Pradhan Mantri Matritva Vandana Yojana (PMMVY)?)",
        'optA': "Provide scholarships for girls' education\nబాలికల విద్యకు విద్య ఉపకరణాలు ఇవ్వడం",
        'optB': "Provide maternity benefits and cash assistance to pregnant women and lactating mothers\nగర్భవతి మహిళలకు మరియు పాలిస్తున్న తల్లులకు ప్రసవ లాభాలు మరియు నగదు సహాయం ఇవ్వడం",
        'optC': "Provide free healthcare to women\nమహిళలకు ఉచిత ఆరోగ్యసేవలు ఇవ్వడం",
        'optD': "Provide subsidized nutritious food to pregnant women\nగర్భవతి మహిళలకు సబ్సిడీ పోషకాహార భోజనం ఇవ్వడం",
        'answer': 'B',
    },
    31596: {
        'question': "మే 2026 నాటికి, ఎన్ని గర్భవతి మహిళలకు మరియు పాలిస్తున్న తల్లులకు PMMVY నుండి లాభం పొందారు?\n(As of May 2026, how many pregnant women and lactating mothers have benefited from PMMVY?)",
        'optA': "75 lakh\n75 లక్ష",
        'optB': "1.2 crore\n1.2 కోటి",
        'optC': "2.1 crore\n2.1 కోటి",
        'optD': "3 crore\n3 కోటి",
        'answer': 'C',
    },
    31597: {
        'question': "ప్రధాన మంత్రి ఆవాస యోజన (సొందరికి ఆవాస) యొక్క ప్రధాన ఉద్దేశ్యం ఏమిటి?\n(What is the key objective of the Pradhan Mantri Awas Yojana (Housing for All)?)",
        'optA': "Construct commercial buildings across India\nభారతదేశ వ్యాపకంగా వాణిజ్య భవనాల నిర్మాణం",
        'optB': "Provide affordable housing to all Indian families by 2023 (extended to 2025)\n2023 నాటికి (2025 నాటికి పెరిగి) అన్ని భారతీయ కుటుంబాలకు సస్తతరమైన ఆవాసం ఇవ్వడం",
        'optC': "Provide luxury housing to high-income families\nఅధిక-ఆదాయ కుటుంబాలకు విలాసవంత ఆవాస ఇవ్వడం",
        'optD': "Develop commercial real estate in urban areas\nపట్టణ ప్రాంతాలలో వాణిజ్య రియల్ ఎస్టేట్ అభివృద్ధి",
        'answer': 'B',
    },
    31598: {
        'question': "మే 2026 నాటికి, ప్రధాన మంత్రి ఆవాస యోజన ప్రకారం ఎన్ని ఇళ్ళు పూర్తిచేసారు?\n(As of May 2026, how many houses have been completed under Pradhan Mantri Awas Yojana?)",
        'optA': "1 crore\n1 కోటి",
        'optB': "1.8 crore\n1.8 కోటి",
        'optC': "2.8 crore\n2.8 కోటి",
        'optD': "3.5 crore\n3.5 కోటి",
        'answer': 'C',
    },
    31599: {
        'question': "ఆధార్-ఆధారిత చెల్లింపు వ్యవస్థ ద్వారా పేదలకు నేరుగా నగదు బదిలీ సహాయం ఇస్తున్న ఏ పథకం ఉందని?\n(Which scheme provides direct cash transfer assistance to the poor through Aadhaar-based payment systems?)",
        'optA': "Public Distribution System\nసార్వజనిక పంపిణీ వ్యవస్థ",
        'optB': "Pradhan Mantri Jan Dhan Yojana\nప్రధాన మంత్రి జన ధన్ యోజన",
        'optC': "Integrated Scheme for Services to Senior Citizens\nవయస్సైన నాగరికుల సేవల సమీకృత పథకం",
        'optD': "National Food Security Scheme\nజాతీయ ఆహార సంరక్షణ పథకం",
        'answer': 'B',
    },
    31600: {
        'question': "మే 2026 నాటికి, PMJDY ప్రకారం ఎన్ని జన ధన్ ఖాతాలు తెరవబడ్డాయి?\n(As of May 2026, how many Jan Dhan accounts have been opened under PMJDY?)",
        'optA': "25 crore\n25 కోటి",
        'optB': "35 crore\n35 కోటి",
        'optC': "48 crore\n48 కోటి",
        'optD': "55 crore\n55 కోటి",
        'answer': 'C',
    },
}

# Now let's generate the output with the proper format
output_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MCQ 31576-31600 Telugu+English Bilingual Format
National Current Affairs 2026 - Government Schemes & Initiatives
Bilingual Telugu-English Format with 10-tuple structure
folder='AP_HC', topic='National_Current_Affairs_2026'
"""

def seed():
    """Insert bilingual MCQs 31576-31600"""
    questions = [
'''

for mcq_id in range(31576, 31601):
    if mcq_id in mcq_bilingual_data:
        data = mcq_bilingual_data[mcq_id]
        # Add dummy explanation for now (will be enhanced)
        explanation = f"Government scheme details and statistics for May 2026. This question tests knowledge of key social welfare, skill development, and infrastructure programs under the current Indian administration."

        output_content += f'''        ({mcq_id},
         "{data['question']}",
         "{data['optA']}",
         "{data['optB']}",
         "{data['optC']}",
         "{data['optD']}",
         "{data['answer']}",
         "{explanation}",
         "AP_HC",
         "National_Current_Affairs_2026"),

'''

output_content += '''    ]
    return questions
'''

# Write the output file
with open('seed_national_ca_2026_mcq_bilingual_31576_31600.py', 'w', encoding='utf-8') as f:
    f.write(output_content)

print(f"Generated bilingual MCQ file for 31576-31600")
print(f"Total MCQs: {len(mcq_bilingual_data)}")
print("\nSample MCQ 31576:")
if 31576 in mcq_bilingual_data:
    data = mcq_bilingual_data[31576]
    print(f"Question:\n{data['question']}\n")
    print(f"Option A: {data['optA']}\n")
    print(f"Answer: {data['answer']}\n")

print("\nSample MCQ 31588:")
if 31588 in mcq_bilingual_data:
    data = mcq_bilingual_data[31588]
    print(f"Question:\n{data['question']}\n")
    print(f"Option A: {data['optA']}\n")
    print(f"Answer: {data['answer']}\n")

print("\nSample MCQ 31600:")
if 31600 in mcq_bilingual_data:
    data = mcq_bilingual_data[31600]
    print(f"Question:\n{data['question']}\n")
    print(f"Option A: {data['optA']}\n")
    print(f"Answer: {data['answer']}\n")
