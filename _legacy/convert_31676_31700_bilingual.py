#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert MCQs 31676-31700 to Telugu+English Bilingual Format
National Current Affairs 2026 - Government Schemes & Initiatives
"""

import re
import sys

# Telugu translations for MCQs 31676-31700
TELUGU_TRANSLATIONS = {
    31676: {
        'question': 'రాష్ట్ర సేవా శ్రేష్ఠత్వ సూచిక (GSEI) 2024 నుండి కార్యచరణ ప్రారంభించినది ప్రభుత్వ సేవలను ఎన్ని ప్రమాణీకృత కొలతల ద్వారా మూల్యాంకనం చేస్తుంది?',
        'optA': 'ఎight కొలతలు: కార్యకర్త, నాణ్యత, సరాసరి సులభం, పారదర్శకత, ప్రతిక్రియాశీలత, జవాబుదారితనం, సమానత్వం మరియు ఆవిష్కరణ',
        'optB': 'ఒక కొలత మాత్రమే',
        'optC': 'పన్నెండు ఏకపక్ష కొలతలు',
        'optD': 'ప్రమాణీకృత మూల్యాంకనం లేనిది',
        'explanation': 'GSEI 2024 ప్రభుత్వ సేవలను ఎight ప్రమాణీకృత కొలతల ద్వారా మూల్యాంకనం చేస్తుంది.'
    },
    31677: {
        'question': 'సమన్విత జిల్లా పరిపాలన (IDA) మోడల్ 34 జిల్లాలలో అమలు చేయబడినది ఏ యంత్రం ద్వారా జిల్లా-స్థాయి సమన్వయాన్ని సమీకరిస్తుంది?',
        'optA': 'ఒక జిల్లా-స్థాయి పాలన సెల్‌ అన్నీ జిల్లా ఏజెంసీలు మరియు సేవలపై సమన్వయ పాత్రతో',
        'optB': 'జిల్లా పరిపాలన యొక్క తొలగింపు',
        'optC': 'ఏజెన్సీ వికేంద్రీకరణ సమన్వయ లేకుండా',
        'optD': 'రాష్ట్ర రాజధానులకు కేంద్రీకరణ',
        'explanation': 'IDA మోడల్ 34 జిల్లాలలో సమన్వయ పాలన సెల్ ద్వారా జిల్లా-స్థాయి సమన్వయం సాధించబడుతుంది.'
    },
    31678: {
        'question': 'ఖచ్చితమైన పరిస్థితి బహిర్గతకారి సంరక్షణ మరియు ప్రేరణ పథకం (WPIS) 2024 ఏ నిర్దిష్ట సంరక్షణలు మరియు ప్రోత్సాహనలను అందిస్తుంది?',
        'optA': 'రహస్య ఫిర్యాదు చానెల్‌లు, సమాచారం బహిర్గతం చేసే అధికారుల స్థానాంతర సంరక్షణలు మరియు అవిశ్వాస్యతా సమాచారం కోసం నిర్ణయించిన వేతనాలు',
        'optB': 'పగటాలు నుండి ఉరకాటి కాదు',
        'optC': 'బహిర్గతకారుల సమర్థ సార్వజనిక గుర్తింపు నిర్దేశన',
        'optD': 'సమాచారం ఫిర్యాదు యంత్రాల తొలగింపు',
        'explanation': 'WPIS 2024 రహస్య చానెల్‌లు, స్థానాంతర సంరక్షణలు మరియు ఆర్థిక పురస్కారాలను అందిస్తుంది.'
    },
    31679: {
        'question': 'సమీకరణ పరిపాలన 2025 సంచారం విధానం చేయడం మరియు అమలు చేయడంలో ఏ పరిపాలన సూత్రాన్ని ఎక్కువగా చేస్తుంది?',
        'optA': 'నిరంతర మూల్యాంకనం మరియు వాస్తవ-సంచారం అభిజ్ఞతా ఫిర్యాదు ఆధారిత విధానం సమీకరణ',
        'optB': 'సమాచారం ఉనికోకు విధానాలు మార్చుకోను',
        'optC': 'విధానం సాక్ష్యాన్ని తొలగింపు',
        'optD': 'సమీకరణ సమీకరణ నుండి నాగరిక ఫిర్యాదు విస్మరణ',
        'explanation': 'అడాప్టివ్ గవర్నెన్స్ 2025 నిరంతర మూల్యాంకనం మరియు చేసిన సమీకరణ సూత్రాన్ని ఆధారం చేస్తుంది.'
    },
    31680: {
        'question': 'ఆర్థిక అభివృద్ధి కోసం పాలన 2025 పరిపాలన జవాబుదారితనాన్ని విధానం లక్ష్యాన్ని సాధించడంతో ఏ ఫలితం కొలతలను సమీకరిస్తుంది?',
        'optA': 'విధానం లక్ష్యాల సాధన (దారిద్ర్య నిమ్నీకరణ, విద్యా సంభందం, ఆరోగ్య ఫలితాలు)',
        'optB': 'పలు గణన కొలతలు విధానం తక్కువ విషయమైతే',
        'optC': 'దారిద్ర్య నిమ్నీకరణ ఫోకస్ యొక్క తొలగింపు',
        'optD': 'ఆరోగ్య ఫలితాల సంబంధిత సమీకరణ నుండి విస్మరణ',
        'explanation': 'గవర్నెన్స్ ఫర్ డెవలప్‌మెంట్ 2025 అభివృద్ధి లక్ష్యాల సాధనను పరిపాలన జవాబుదారితనానికి సంయోగం చేస్తుంది.'
    },
    31681: {
        'question': 'డిసెంబర్ 2018లో ప్రారంభించిన PM-కిసాన్ పథకం యొక్క ప్రధాన లక్ష్యం ఏమిటి?',
        'optA': 'అన్ని భూ-సంధ్య సంధ్యకులకు సమర్థ ఆదాయ సహాయం ఇవ్వడం',
        'optB': 'సిద్ధం బునియాది ఢాంచా అభివృద్ధి',
        'optC': 'సహజ గృహ నిర్మాణ కోసం ప్రోత్సాహన',
        'optD': 'సారం ఏ సంబంధిత సాధనాలకు అందుబాటు',
        'explanation': 'PM-కిసాన్ పథకం డిసెంబర్ 2018 నుండి సమర్థ పటి సంధ్యకులకు ఆదాయ సహాయం ఇస్తుంది.'
    },
    31682: {
        'question': '2026లో PM-కిసాన్ పథకం ప్రకారం పట్టి సంధ్య సంధ్యకులకు వార్షిక ఎంత ఆర్థిక సహాయం ఇవ్వబడుతుంది?',
        'optA': 'రూ. 2,000',
        'optB': 'రూ. 4,000',
        'optC': 'రూ. 6,000',
        'optD': 'రూ. 8,000',
        'explanation': 'PM-కిసాన్ సంధ్యకులకు సంవత్సరానికి రూ. 6,000 ఆర్థిక సహాయం ఇస్తుంది.'
    },
    31683: {
        'question': 'PM గతి శక్తి జాతీయ మాస్టర్ ప్లాన్ అమలుకోసం ఏ మంత్రాలయ విధానం ఉండాలి?',
        'optA': 'గ్రామీణ అభివృద్ధి మంత్రాలయ',
        'optB': 'వాణిజ్యం మరియు పరిశ్రమ మంత్రాలయ',
        'optC': 'బునియాది ఢాంచా, గృహ నిర్మాణం మరియు నగర విషయాల మంత్రాలయ',
        'optD': 'ఆర్థిక మంత్రాలయ',
        'explanation': 'PM గతి శక్తి జాతీయ మాస్టర్ ప్లాన్ బునియాది ఢాంచా, గృహ నిర్మాణం మరియు నగర విషయాల మంత్రాలయ ద్వారా పర్యవేక్షించబడుతుంది.'
    },
    31684: {
        'question': 'PM గతి శక్తి జాతీయ మాస్టర్ ప్లాన్ (2021-2026) కోసం కుల బడ్జెట్ నిధులు ఎంత?',
        'optA': 'రూ. 50 లక్ష కోట్లు',
        'optB': 'రూ. 111 లక్ష కోట్లు',
        'optC': 'రూ. 150 లక్ష కోట్లు',
        'optD': 'రూ. 200 లక్ష కోట్లు',
        'explanation': 'PM గతి శక్తి 2021-2026 మాస్టర్ ప్లాన్ కుల బడ్జెట్ రూ. 111 లక్ష కోట్లు.'
    },
    31685: {
        'question': 'NRLM (జాతీయ గ్రామీణ జీవనోపాధి కర్మసూచి) ప్రధానంగా గ్రామీణ అభివృద్ధిలో ఏ అంశంపై ఫోకస్ చేస్తుంది?',
        'optA': 'భూమి పునర్విభజన కార్యక్రమాలు',
        'optB': 'ఉపయోగ అభివృద్ధి మరియు స్వ-ఉపజీవనం ద్వారా దరిద్రత్వ తగ్గింపు',
        'optC': 'ఆహార ధాన్య పంపిణీ',
        'optD': 'జల సంపద నిర్వహణ',
        'explanation': 'NRLM గ్రామీణ ప్రాంతాలలో ఉపయోగ అభివృద్ధి మరియు స్వ-ఉపజీవనం ద్వారా దరిద్రత్వ తగ్గింపుపై ఫోకస్ చేస్తుంది.'
    },
    31686: {
        'question': 'మే 2026 నాటికి NRLM ప్రకారం ఎన్ని స్వయం సహాయ సమూహాలు (SHGs) ఏర్పాటయ్యాయి?',
        'optA': '75 లక్ష',
        'optB': '1.25 కోటి',
        'optC': '1.75 కోటి',
        'optD': '2.5 కోటి',
        'explanation': 'మే 2026 నాటికి సుమారుగా 1.75 కోటి స్వయం సహాయ సమూహాలు (SHGs) NRLM ప్రకారం ఏర్పాటయ్యాయి.'
    },
    31687: {
        'question': 'ప్రధాన మంత్రి కౌశల్ వికాస యోజన (PMKVY) ప్రకారం ప్రధాన ఫోకస్ ఏమిటి?',
        'optA': 'కృషి ఉపయోగ అభివృద్ధి',
        'optB': 'పారిశ్రామిక ఉపయోగ అభివృద్ధి మరియు వృత్తిమత్తర శిక్షణ',
        'optC': 'IT సెక్టర్ శిక్షణ',
        'optD': 'భాష నేర్చుకోవడం కార్యక్రమాలు',
        'explanation': 'PMKVY పారిశ్రామిక ఉపయోగ అభివృద్ధి మరియు వృత్తిమత్తర శిక్షణపై ఫోకస్ చేస్తుంది.'
    },
    31688: {
        'question': 'మే 2026 నాటికి, PMKVY ప్రకారం సుమారుగా ఎన్ని యువకులకు శిక్షణ ఇవ్వబడింది?',
        'optA': '6 కోటి',
        'optB': '9 కోటి',
        'optC': '1.2 కోటి',
        'optD': '1.8 కోటి',
        'explanation': 'మే 2026 నాటికి సుమారుగా 1.2 కోటి యువకులకు PMKVY ప్రకారం శిక్షణ ఇవ్వబడింది.'
    },
    31689: {
        'question': 'ఏ ప్రభుత్వ పథకం ఆర్థిక సంభందం ద్వారా మహిళా సాధికారత లక్ష్యీకరిస్తుంది?',
        'optA': 'సుకన్య సమృద్ధి యోజన',
        'optB': 'ప్రధాన మంత్రి మహిళా శక్తి కేంద్రం',
        'optC': 'ప్రధాన మంత్రి ముద్రా యోజన',
        'optD': 'ఉజ్జ్వల యోజన',
        'explanation': 'PM ముద్రా యోజన ఆర్థిక సంభందం ద్వారా మహిళా సాధికారత లక్ష్యీకరిస్తుంది.'
    },
    31690: {
        'question': 'మే 2026 నాటికి, ప్రధాన మంత్రి ముద్రా యోజన ప్రకారం కుల వితరణ చేసిన మొత్తం ఎంత?',
        'optA': 'రూ. 5 లక్ష కోట్లు',
        'optB': 'రూ. 10 లక్ష కోట్లు',
        'optC': 'రూ. 20 లక్ష కోట్లు',
        'optD': 'రూ. 30 లక్ష కోట్లు',
        'explanation': 'మే 2026 నాటికి PM ముద్రా యోజన ప్రకారం రూ. 20 లక్ష కోట్లు వితరణ చేసారు.'
    },
    31691: {
        'question': 'ప్రధాన మంత్రి వయ వందన యోజన (PMVVY) యొక్క ప్రధాన లక్ష్యం ఏమిటి?',
        'optA': 'వయస్సైన నాగరికులకు ఆరోగ్య బీమా ఇవ్వడం',
        'optB': '60 సంవత్సరాలు మరియు అంతకంటే ఎక్కువ వయస్సు నాగరికులకు పెన్షన్ సహాయం ఇవ్వడం',
        'optC': 'వయస్సైన నాగరికులకు సబ్సిడీ ఆవాస ఇవ్వడం',
        'optD': 'వయస్సైన నాగరికులకు ఉచిత కదలిక సాధనాలు ఇవ్వడం',
        'explanation': 'PMVVY 60 సంవత్సరాలు మరియు అంతకంటే ఎక్కువ వయస్సు నాగరికులకు పెన్షన్ సహాయం ఇస్తుంది.'
    },
    31692: {
        'question': 'మే 2026 నాటికి, ప్రధాన మంత్రి వయ వందన యోజన ప్రకారం ఎన్ని వయస్సైన నాగరికులను నమోదు చేసారు?',
        'optA': '50 లక్ష',
        'optB': '1 కోటి',
        'optC': '1.8 కోటి',
        'optD': '2.5 కోటి',
        'explanation': 'మే 2026 నాటికి సుమారుగా 1.8 కోటి వయస్సైన నాగరికులను PMVVY ప్రకారం నమోదు చేసారు.'
    },
    31693: {
        'question': 'ఏ పథకం వికలాంగ వ్యక్తుల పునర్వాస మరియు సంక్షేమ కోసం ఆర్థిక సహాయం ఇస్తుంది?',
        'optA': 'ఇందిరా గాంధీ జాతీయ వికలాంగత పెన్షన్ పథకం',
        'optB': 'రాజీవ్ గాంధీ కిశోరీ సాధికారత పథకం',
        'optC': 'జాతీయ బాల శ్రమ ప్రకల్పన',
        'optD': 'సమన్విత బాల అభివృద్ధి పథకం',
        'explanation': 'ఇందిరా గాంధీ జాతీయ వికలాంగత పెన్షన్ పథకం వికలాంగ వ్యక్తుల సంక్షేమ కోసం ఆర్థిక సహాయం ఇస్తుంది.'
    },
    31694: {
        'question': 'మే 2026 నాటికి, వికలాంగత పెన్షన్ పథకాల ప్రకారం ఎన్ని వికలాంగ వ్యక్తులు చేర్చబడ్డారు?',
        'optA': '1.5 కోటి',
        'optB': '2.3 కోటి',
        'optC': '3.2 కోటి',
        'optD': '4.5 కోటి',
        'explanation': 'మే 2026 నాటికి సుమారుగా 2.3 కోటి వికలాంగ వ్యక్తులు వికలాంగత పెన్షన్ పథకాల ప్రకారం చేర్చబడ్డారు.'
    },
    31695: {
        'question': 'ప్రధాన మంత్రి మాతృత్వ వందన యోజన (PMMVY) యొక్క ప్రధాన ఫోకస్ ఏమిటి?',
        'optA': 'బాలికల విద్యకు విద్య ఉపకరణాలు ఇవ్వడం',
        'optB': 'గర్భవతి మహిళలకు మరియు పాలిస్తున్న తల్లులకు ప్రసవ లాభాలు మరియు నగదు సహాయం ఇవ్వడం',
        'optC': 'మహిళలకు ఉచిత ఆరోగ్యసేవలు ఇవ్వడం',
        'optD': 'గర్భవతి మహిళలకు సబ్సిడీ పోషకాహార భోజనం ఇవ్వడం',
        'explanation': 'PMMVY గర్భవతి మహిళలకు మరియు పాలిస్తున్న తల్లులకు ప్రసవ లాభాలు మరియు నగదు సహాయం ఇస్తుంది.'
    },
    31696: {
        'question': 'మే 2026 నాటికి, ఎన్ని గర్భవతి మహిళలకు మరియు పాలిస్తున్న తల్లులకు PMMVY నుండి లాభం పొందారు?',
        'optA': '75 లక్ష',
        'optB': '1.2 కోటి',
        'optC': '2.1 కోటి',
        'optD': '3 కోటి',
        'explanation': 'మే 2026 నాటికి సుమారుగా 2.1 కోటి గర్భవతి మహిళలకు మరియు పాలిస్తున్న తల్లులకు PMMVY నుండి లాభం పొందారు.'
    },
    31697: {
        'question': 'ప్రధాన మంత్రి ఆవాస యోజన (సందరికి ఆవాస) యొక్క ప్రధాన ఉద్దేశ్యం ఏమిటి?',
        'optA': 'భారతదేశ వ్యాపకంగా వాణిజ్య భవనాల నిర్మాణం',
        'optB': '2023 నాటికి (2025 నాటికి పెరిగి) అన్ని భారతీయ కుటుంబాలకు సస్త కరమైన ఆవాసం ఇవ్వడం',
        'optC': 'అధిక-ఆదాయ కుటుంబాలకు విలాసవంత ఆవాస ఇవ్వడం',
        'optD': 'పట్టణ ప్రాంతాలలో వాణిజ్య రియల్ ఎస్టేట్ అభివృద్ధి',
        'explanation': 'PM ఆవాస యోజన 2025 నాటికి అన్ని భారతీయ కుటుంబాలకు సస్తకరమైన ఆవాసం ఇవ్వడం లక్ష్యంగా ఉంది.'
    },
    31698: {
        'question': 'మే 2026 నాటికి, ప్రధాన మంత్రి ఆవాస యోజన ప్రకారం ఎన్ని ఇళ్ళు పూర్తిచేసారు?',
        'optA': '1 కోటి',
        'optB': '1.8 కోటి',
        'optC': '2.8 కోటి',
        'optD': '3.5 కోటి',
        'explanation': 'మే 2026 నాటికి సుమారుగా 2.8 కోటి ఇళ్ళు PM ఆవాస యోజన ప్రకారం పూర్తిచేసారు.'
    },
    31699: {
        'question': 'ఆధార్-ఆధారిత చెల్లింపు వ్యవస్థ ద్వారా పేదలకు నేరుగా నగదు బదిలీ సహాయం ఇస్తున్న ఏ పథకం ఉందని?',
        'optA': 'సార్వజనిక పంపిణీ వ్యవస్థ',
        'optB': 'ప్రధాన మంత్రి జన ధన్ యోజన',
        'optC': 'వయస్సైన నాగరికుల సేవల సమీకృత పథకం',
        'optD': 'జాతీయ ఆహార సంరక్షణ పథకం',
        'explanation': 'PM జన ధన్ యోజన ఆధార్-ఆధారిత చెల్లింపు వ్యవస్థ ద్వారా నేరుగా నగదు బదిలీ సహాయం ఇస్తుంది.'
    },
    31700: {
        'question': 'మే 2026 నాటికి, PMJDY ప్రకారం ఎన్ని జన ధన్ ఖాతాలు తెరవబడ్డాయి?',
        'optA': '25 కోటి',
        'optB': '35 కోటి',
        'optC': '48 కోటి',
        'optD': '55 కోటి',
        'explanation': 'మే 2026 నాటికి సుమారుగా 48 కోటి జన ధన్ ఖాతాలు PMJDY ప్రకారం తెరవబడ్డాయి.'
    }
}

# English content from seed file (to be extracted)
ENGLISH_QUESTIONS = {
    31676: "The Government Service Excellence Index (GSEI) operational since 2024 evaluates government services on how many standardized dimensions?",
    31677: "The Integrated District Administration (IDA) model implemented in 34 districts consolidates district-level coordination through which mechanism?",
    31678: "The Whistleblower Protection and Incentivization Scheme (WPIS) of 2024 provides which specific protections and incentives?",
    31679: "The Adaptive Governance initiative of 2025 emphasizes which administrative principle in policy-making and implementation?",
    31680: "India's Governance for Development framework of 2025 integrates administrative accountability with which outcome measurement?",
    31681: "What is the primary objective of PM-KISAN scheme launched in December 2018?",
    31682: "Under PM-KISAN scheme, how much financial assistance is provided annually to eligible farmers in 2026?",
    31683: "Which ministry oversees the implementation of PM Gati Shakti National Master Plan?",
    31684: "What is the total budget allocation for PM Gati Shakti National Master Plan (2021-2026)?",
    31685: "NRLM (National Rural Livelihoods Mission) primarily focuses on which aspect of rural development?",
    31686: "How many Self Help Groups (SHGs) have been formed under NRLM as of May 2026?",
    31687: "Under the Pradhan Mantri Kaushal Vikas Yojana (PMKVY), what is the primary focus?",
    31688: "As of May 2026, approximately how many youth have been trained under PMKVY?",
    31689: "Which government scheme specifically targets women empowerment through financial inclusion?",
    31690: "As of May 2026, what is the total amount disbursed under Pradhan Mantri Mudra Yojana?",
    31691: "What is the primary objective of the Pradhan Mantri Vaya Vandana Yojana (PMVVY)?",
    31692: "How many senior citizens have been enrolled under Pradhan Mantri Vaya Vandana Yojana as of May 2026?",
    31693: "Which scheme provides financial assistance for the rehabilitation and welfare of persons with disabilities?",
    31694: "As of May 2026, how many persons with disabilities have been covered under disability pension schemes?",
    31695: "What is the primary focus of the Pradhan Mantri Matritva Vandana Yojana (PMMVY)?",
    31696: "As of May 2026, how many pregnant women and lactating mothers have benefited from PMMVY?",
    31697: "What is the key objective of the Pradhan Mantri Awas Yojana (Housing for All)?",
    31698: "As of May 2026, how many houses have been completed under Pradhan Mantri Awas Yojana?",
    31699: "Which scheme provides direct cash transfer assistance to the poor through Aadhaar-based payment systems?",
    31700: "As of May 2026, how many Jan Dhan accounts have been opened under PMJDY?"
}

# English options (sample - from existing bilingual file pattern)
ENGLISH_OPTIONS = {
    31676: ["Eight dimensions: efficiency, quality, accessibility, transparency, responsiveness, accountability, equity, and innovation",
            "Single metric only",
            "Twelve arbitrary measures",
            "No standardized evaluation"],
    31677: ["Single district-level governance cell with coordinating role across all district agencies and services",
            "Elimination of district administration",
            "Agency decentralization without coordination",
            "Centralization to state capitals"],
    31678: ["Confidential complaint channels, transfer protections for reporting officials, and financial rewards for corruption-exposing information",
            "No protection from retaliation",
            "Mandatory public identification of whistleblowers",
            "Elimination of reporting mechanisms"],
    31679: ["Continuous evaluation and iterative policy adjustment based on real-world implementation feedback and outcome data",
            "Fixed policies unchanged despite evidence",
            "Elimination of policy evaluation",
            "Exclusion of citizen feedback from policy"],
    31680: ["Achievement of development objectives (poverty reduction, education access, health outcomes) as determinants of administrative effectiveness evaluation",
            "Only output metrics regardless of outcomes",
            "Elimination of poverty reduction focus",
            "Exclusion of health outcomes from assessment"],
    31681: ["Provide direct income support to all farmers",
            "Develop irrigation infrastructure",
            "Promote organic farming",
            "Subsidize fertilizers and pesticides"],
    31682: ["Rs 2,000", "Rs 4,000", "Rs 6,000", "Rs 8,000"],
    31683: ["Ministry of Rural Development", "Ministry of Commerce & Industry", "Ministry of Infrastructure, Housing and Urban Affairs", "Ministry of Finance"],
    31684: ["Rs 50 lakh crore", "Rs 111 lakh crore", "Rs 150 lakh crore", "Rs 200 lakh crore"],
    31685: ["Land redistribution programs", "Poverty reduction through skill development and self-employment", "Food grain distribution", "Water resource management"],
    31686: ["75 lakh", "1.25 crore", "1.75 crore", "2.5 crore"],
    31687: ["Agricultural skill development", "Industrial skill development and vocational training", "IT sector training", "Language learning programs"],
    31688: ["6 crore", "9 crore", "1.2 crore", "1.8 crore"],
    31689: ["Sukanya Samriddhi Yojana", "Pradhan Mantri Mahila Shakti Kendra", "Pradhan Mantri Mudra Yojana", "Ujjwala Yojana"],
    31690: ["Rs 5 lakh crore", "Rs 10 lakh crore", "Rs 20 lakh crore", "Rs 30 lakh crore"],
    31691: ["Provide health insurance to senior citizens", "Provide pension support to senior citizens aged 60 and above", "Provide subsidized housing to senior citizens", "Provide free mobility aids to senior citizens"],
    31692: ["50 lakh", "1 crore", "1.8 crore", "2.5 crore"],
    31693: ["Indira Gandhi National Disability Pension Scheme", "Rajiv Gandhi Scheme for Empowerment of Adolescent Girls", "National Child Labour Project", "Integrated Child Development Scheme"],
    31694: ["1.5 crore", "2.3 crore", "3.2 crore", "4.5 crore"],
    31695: ["Provide scholarships for girls' education", "Provide maternity benefits and cash assistance to pregnant women and lactating mothers", "Provide free healthcare to women", "Provide subsidized nutritious food to pregnant women"],
    31696: ["75 lakh", "1.2 crore", "2.1 crore", "3 crore"],
    31697: ["Construct commercial buildings across India", "Provide affordable housing to all Indian families by 2023 (extended to 2025)", "Provide luxury housing to high-income families", "Develop commercial real estate in urban areas"],
    31698: ["1 crore", "1.8 crore", "2.8 crore", "3.5 crore"],
    31699: ["Public Distribution System", "Pradhan Mantri Jan Dhan Yojana", "Integrated Scheme for Services to Senior Citizens", "National Food Security Scheme"],
    31700: ["25 crore", "35 crore", "48 crore", "55 crore"]
}

ANSWERS = {
    31676: "A", 31677: "A", 31678: "A", 31679: "A", 31680: "A",
    31681: "A", 31682: "C", 31683: "C", 31684: "B", 31685: "B",
    31686: "C", 31687: "B", 31688: "C", 31689: "C", 31690: "C",
    31691: "B", 31692: "C", 31693: "A", 31694: "B", 31695: "B",
    31696: "C", 31697: "B", 31698: "C", 31699: "B", 31700: "C"
}

ENGLISH_EXPLANATIONS = {
    31676: "GSEI is a 2024 governance framework that evaluates government services across eight standardized dimensions including efficiency, quality, accessibility, transparency, responsiveness, accountability, equity, and innovation.",
    31677: "IDA model implemented across 34 districts creates a single coordinated governance cell to streamline district-level administration and service delivery.",
    31678: "WPIS 2024 provides comprehensive protections including confidential channels, transfer protections for reporting officials, and financial rewards for information exposing corruption.",
    31679: "Adaptive Governance 2025 emphasizes continuous evaluation and iterative policy adjustment based on real-world feedback and outcome data.",
    31680: "Governance for Development 2025 framework measures administrative accountability through achievement of development objectives including poverty reduction, education access, and health outcomes.",
    31681: "PM-KISAN scheme launched in December 2018 provides direct income support of Rs 6,000 per year to all eligible farmers in three installments.",
    31682: "PM-KISAN provides annual financial assistance of Rs 6,000 per year in three equal installments of Rs 2,000 each.",
    31683: "PM Gati Shakti National Master Plan is overseen by the Ministry of Infrastructure, Housing and Urban Affairs.",
    31684: "PM Gati Shakti National Master Plan (2021-2026) has total budget allocation of Rs 111 lakh crore for infrastructure development.",
    31685: "NRLM primarily focuses on poverty reduction through skill development and self-employment opportunities in rural areas.",
    31686: "As of May 2026, approximately 1.75 crore Self Help Groups (SHGs) have been formed under NRLM.",
    31687: "PMKVY focuses on industrial skill development and vocational training to enhance employability of youth.",
    31688: "As of May 2026, approximately 1.2 crore youth have been trained under PMKVY across various skill domains.",
    31689: "PM Mudra Yojana specifically targets women empowerment through financial inclusion by providing collateral-free business loans.",
    31690: "As of May 2026, Rs 20 lakh crore has been disbursed under PM Mudra Yojana to approximately 65 crore beneficiaries.",
    31691: "PMVVY provides pension support to senior citizens aged 60 years and above with guaranteed returns on investment.",
    31692: "As of May 2026, approximately 1.8 crore senior citizens have been enrolled under PMVVY.",
    31693: "Indira Gandhi National Disability Pension Scheme provides financial assistance for rehabilitation and welfare of persons with disabilities.",
    31694: "As of May 2026, approximately 2.3 crore persons with disabilities have been covered under various disability pension schemes.",
    31695: "PMMVY provides maternity benefits and cash assistance to pregnant women and lactating mothers for nutrition and child welfare.",
    31696: "As of May 2026, approximately 2.1 crore pregnant women and lactating mothers have benefited from PMMVY.",
    31697: "PM Awas Yojana aims to provide affordable housing to all Indian families by 2025 with focus on low-income groups.",
    31698: "As of May 2026, approximately 2.8 crore houses have been completed under PM Awas Yojana.",
    31699: "PM Jan Dhan Yojana enables direct cash transfer to the poor through Aadhaar-linked bank accounts.",
    31700: "As of May 2026, approximately 48 crore Jan Dhan accounts have been opened under PM Jan Dhan Yojana."
}

def create_bilingual_mcqs():
    """Create bilingual MCQ tuples"""
    mcqs = []

    for mcq_id in range(31676, 31701):
        tel = TELUGU_TRANSLATIONS[mcq_id]

        # Create bilingual question (Telugu\nEnglish)
        bilingual_question = f"{tel['question']}\n{ENGLISH_QUESTIONS[mcq_id]}"

        # Create bilingual options with \n separator
        options = ENGLISH_OPTIONS[mcq_id]
        bilingual_optA = f"{tel['optA']}\n{options[0]}"
        bilingual_optB = f"{tel['optB']}\n{options[1]}"
        bilingual_optC = f"{tel['optC']}\n{options[2]}"
        bilingual_optD = f"{tel['optD']}\n{options[3]}"

        # Create bilingual explanation
        bilingual_explanation = f"{tel['explanation']}\n{ENGLISH_EXPLANATIONS[mcq_id]}"

        # Create 10-tuple
        mcq_tuple = (
            mcq_id,
            bilingual_question,
            bilingual_optA,
            bilingual_optB,
            bilingual_optC,
            bilingual_optD,
            ANSWERS[mcq_id],
            bilingual_explanation,
            "AP_HC",
            "National_Current_Affairs_2026"
        )
        mcqs.append(mcq_tuple)

    return mcqs

if __name__ == "__main__":
    print("Creating bilingual MCQs 31676-31700...")
    mcqs = create_bilingual_mcqs()

    # Show 3 samples
    print("\n=== SAMPLE MCQ 31676 ===")
    mcq = mcqs[0]
    print(f"ID: {mcq[0]}")
    print(f"Question: {mcq[1][:100]}...")
    print(f"Answer: {mcq[6]}")
    print(f"Folder: {mcq[8]}, Topic: {mcq[9]}")

    print("\n=== SAMPLE MCQ 31688 ===")
    mcq = mcqs[12]
    print(f"ID: {mcq[0]}")
    print(f"Question: {mcq[1][:100]}...")
    print(f"Answer: {mcq[6]}")

    print("\n=== SAMPLE MCQ 31700 ===")
    mcq = mcqs[24]
    print(f"ID: {mcq[0]}")
    print(f"Question: {mcq[1][:100]}...")
    print(f"Answer: {mcq[6]}")

    print(f"\nTotal MCQs created: {len(mcqs)}")
    print("Format: 10-tuple (id, question, optA, optB, optC, optD, answer, explanation, folder, topic)")
    print("All questions/options/explanations in bilingual format (Telugu\\nEnglish)")
