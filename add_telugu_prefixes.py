#!/usr/bin/env python3
"""
Add Telugu bilingual prefixes to every MCQ question in 5 seed files ch86-ch90.
Format: "Telugu keyword phrase ఏమిటి/ఏది/ఎవరు/ఎప్పుడు/ఎందుకు? / Original English question unchanged"
"""

import re

def get_telugu_question_word(english_q):
    q_lower = english_q.lower().strip()
    if re.search(r'\bhow many\b|\bhow much\b', q_lower):
        return 'ఎంత?'
    if re.search(r'\bwho\b', q_lower):
        return 'ఎవరు?'
    if re.search(r'\bwhen\b|\bwhich year\b|\bin which year\b|\bwhat year\b', q_lower):
        return 'ఎప్పుడు?'
    if re.search(r'\bwhy\b|\bwhat.*reason\b|\breason.*for\b', q_lower):
        return 'ఎందుకు?'
    if re.search(r'\bwhich\b', q_lower):
        return 'ఏది?'
    if re.search(r'\bwhat\b|\bdefine\b|\bexplain\b|\bmean\b', q_lower):
        return 'ఏమిటి?'
    if re.search(r'\bhow\b', q_lower):
        return 'ఎలా?'
    return 'ఏమిటి?'

def make_prefix_ch86(q):
    ql = q.lower()
    qw = get_telugu_question_word(q)
    if 'ficci' in ql and ('establish' in ql or 'found' in ql or 'year' in ql): return f'FICCI స్థాపన {qw}'
    if 'ficci' in ql: return f'FICCI ఒత్తిడి సమూహం {qw}'
    if 'nasscom' in ql: return f'NASSCOM IT సమూహం {qw}'
    if 'nira radia' in ql or 'radia tapes' in ql: return f'నీరా రాడియా వ్యవహారం {qw}'
    if 'revolving door' in ql: return f'రివాల్వింగ్ డోర్ లాబీయింగ్ {qw}'
    if 'iron triangle' in ql: return f'Iron Triangle భావన {qw}'
    if "dahl's plurali" in ql or ('robert dahl' in ql and 'plurali' in ql): return f'Dahl బహుళత్వ సిద్ధాంతం {qw}'
    if 'polyarchy' in ql: return f'Polyarchy భావన {qw}'
    if 'corporat' in ql and 'plurali' in ql: return f'కార్పొరేటిజం vs బహుళత్వం {qw}'
    if 'corporat' in ql: return f'కార్పొరేటిజం సిద్ధాంతం {qw}'
    if 'plurali' in ql: return f'బహుళత్వ సిద్ధాంతం {qw}'
    if 'pucl' in ql and 'nota' in ql: return f'PUCL NOTA పిటిషన్ {qw}'
    if 'pucl' in ql and ('found' in ql or 'establish' in ql): return f'PUCL స్థాపన {qw}'
    if 'pucl' in ql: return f'PUCL సంస్థ {qw}'
    if 'nota' in ql: return f'NOTA హక్కు {qw}'
    if 'anna hazare' in ql and ('fast' in ql or 'lokpal' in ql or '2011' in ql): return f'Anna Hazare లోక్పాల్ ఉద్యమం {qw}'
    if 'anna hazare' in ql: return f'Anna Hazare ఉద్యమం {qw}'
    if 'jan lokpal' in ql or 'lokpal bill' in ql: return f'జన్ లోక్పాల్ బిల్లు {qw}'
    if 'lokpal' in ql: return f'లోక్పాల్ చట్టం {qw}'
    if 'mkss' in ql or 'mazdoor kisan shakti' in ql: return f'MKSS సంస్థ {qw}'
    if 'jan sunwai' in ql: return f'జన్ సున్వాయి విధానం {qw}'
    if 'right to information' in ql or ql.startswith('rti') or ' rti ' in ql or ql.endswith('rti'): return f'సమాచార హక్కు చట్టం {qw}'
    if 'narmada' in ql: return f'నర్మదా బచావో ఆందోళన్ {qw}'
    if 'chipko' in ql: return f'చిప్కో ఉద్యమం {qw}'
    if 'forest conservation' in ql or 'forest rights' in ql or 'forest act' in ql: return f'అటవీ సంరక్షణ చట్టం {qw}'
    if 'bahuguna' in ql: return f'సుందర్లాల్ బహుగుణ {qw}'
    if 'medha patkar' in ql: return f'మేధా పాట్కర్ ఉద్యమం {qw}'
    if 'ela bhatt' in ql or 'ela bhat' in ql: return f'ఎలా భట్ SEWA {qw}'
    if 'sewa' in ql and ('found' in ql or 'city' in ql or 'ahmedabad' in ql): return f'SEWA స్థాపన {qw}'
    if 'sewa' in ql: return f'SEWA మహిళా సంఘం {qw}'
    if 'aruna roy' in ql: return f'అరుణా రాయ్ MKSS {qw}'
    if 'samyukta kisan' in ql or ('farm law' in ql and 'repeal' in ql) or ('farmer' in ql and 'repeal' in ql): return f'వ్యవసాయ చట్టాల రద్దు {qw}'
    if 'tikait' in ql or 'bku' in ql or 'boat club' in ql: return f'BKU రైతు సంఘం {qw}'
    if 'kisan' in ql and 'union' in ql: return f'రైతు సంఘం ఉద్యమం {qw}'
    if 'intuc' in ql: return f'INTUC కార్మిక సంఘం {qw}'
    if 'bms' in ql and ('affiliate' in ql or 'rss' in ql or 'trade union' in ql): return f'BMS కార్మిక సంఘం {qw}'
    if 'aituc' in ql: return f'AITUC కార్మిక సంఘం {qw}'
    if 'citu' in ql: return f'CITU కార్మిక సంఘం {qw}'
    if 'trade union' in ql: return f'కార్మిక సంఘం {qw}'
    if 'bentley' in ql: return f'Arthur Bentley రాజకీయ విజ్ఞానం {qw}'
    if 'david truman' in ql or "truman's" in ql: return f'David Truman సిద్ధాంతం {qw}'
    if 'almond' in ql or 'anomic' in ql: return f'Almond-Powell వర్గీకరణ {qw}'
    if 'allen potter' in ql: return f'ఒత్తిడి సమూహ వర్గీకరణ {qw}'
    if 'promotional' in ql and 'sectional' in ql: return f'ఒత్తిడి సమూహ వర్గీకరణ {qw}'
    if 'promotional' in ql: return f'ప్రచారాత్మక ఒత్తిడి సమూహం {qw}'
    if 'sectional' in ql: return f'వర్గ ఒత్తిడి సమూహం {qw}'
    if 'symbiosi' in ql: return f'ఒత్తిడి సమూహం-పార్టీ సంబంధం {qw}'
    if 'aam aadmi' in ql or 'india against corruption' in ql or 'kejriwal' in ql: return f'IAC ఉద్యమం AAP స్థాపన {qw}'
    if 'caste association' in ql or 'kshatriya' in ql or 'maratha' in ql: return f'కుల సంఘాల పాత్ర {qw}'
    if 'vhp' in ql or ('rss' in ql and 'pressure' in ql) or 'vishwa hindu' in ql: return f'VHP/RSS ఒత్తిడి సమూహం {qw}'
    if 'bar council' in ql: return f'బార్ కౌన్సిల్ సంస్థ {qw}'
    if ('cii' in ql or 'ficci' in ql) and ('budget' in ql or 'finance' in ql or 'tax' in ql): return f'CII/FICCI బడ్జెట్ సిఫారసులు {qw}'
    if 'common cause' in ql or 'shourie' in ql: return f'Common Cause సంస్థ {qw}'
    if 'sunita narain' in ql or 'centre for science' in ql: return f'CSE పర్యావరణ సంస్థ {qw}'
    if 'public interest litigation' in ql or 'pil' in ql: return f'ప్రజాహిత వ్యాజ్యం {qw}'
    if 'bandh' in ql or 'hartal' in ql or 'general strike' in ql or 'strike' in ql: return f'సమ్మె పద్ధతి {qw}'
    if 'standing committee' in ql or 'parliamentary committee' in ql: return f'పార్లమెంట్ కమిటీ {qw}'
    if 'lobbying' in ql or 'lobby' in ql: return f'లాబీయింగ్ పద్ధతి {qw}'
    if 'pressure group' in ql and 'political party' in ql: return f'ఒత్తిడి సమూహం vs రాజకీయ పార్టీ {qw}'
    if 'pressure group' in ql and ('define' in ql or 'best defined' in ql or 'character' in ql): return f'ఒత్తిడి సమూహం నిర్వచనం {qw}'
    if 'pressure group' in ql: return f'ఒత్తిడి సమూహం {qw}'
    if 'demerit' in ql or ('undemocratic' in ql and 'pressure' in ql): return f'ఒత్తిడి సమూహాల లోపాలు {qw}'
    if 'merit' in ql and 'pressure' in ql: return f'ఒత్తిడి సమూహాల ప్రయోజనాలు {qw}'
    return f'ఒత్తిడి సమూహం {qw}'

def make_prefix_ch87(q):
    ql = q.lower()
    qw = get_telugu_question_word(q)
    if 'morley-minto' in ql or 'separate electorate' in ql: return f'Morley-Minto సంస్కరణలు {qw}'
    if 'babri masjid' in ql or 'ayodhya' in ql: return f'బాబ్రీ మసీదు ఘటన {qw}'
    if 'two-nation' in ql or 'two nation theory' in ql: return f'రెండు జాతుల సిద్ధాంతం {qw}'
    if 'partition' in ql and '1947' in ql: return f'దేశ విభజన 1947 {qw}'
    if 'golwalkar' in ql: return f'గోల్వాల్కర్ సిద్ధాంతం {qw}'
    if 'patel' in ql and ('princely' in ql or 'integrat' in ql or 'iron man' in ql): return f'సర్దార్ పటేల్ సంస్థాన విలీనం {qw}'
    if 'ekta diwas' in ql or 'national unity day' in ql or 'october 31' in ql: return f'ఏకతా దివస్ {qw}'
    if 'nfch' in ql or 'national foundation for communal harmony' in ql: return f'NFCH సంస్థ {qw}'
    if 'national integration council' in ql and ('chair' in ql or 'head' in ql): return f'జాతీయ సమైక్యతా మండలి {qw}'
    if 'national integration council' in ql and ('year' in ql or 'establish' in ql or '1961' in ql): return f'NIC స్థాపన సంవత్సరం {qw}'
    if 'national integration council' in ql: return f'జాతీయ సమైక్యతా మండలి {qw}'
    if '42nd amendment' in ql or ('42nd' in ql and 'preamble' in ql): return f'42వ రాజ్యాంగ సవరణ {qw}'
    if 'preamble' in ql and ('integrity' in ql or 'unity' in ql or 'secular' in ql): return f'ప్రవేశిక సవరణ {qw}'
    if 'unity in diversity' in ql: return f'వైవిధ్యంలో ఐకమత్యం {qw}'
    if 'communalism' in ql and ('define' in ql or 'best defined' in ql or 'meaning' in ql or 'primarily' in ql): return f'మత విద్వేషం నిర్వచనం {qw}'
    if 'communalism' in ql: return f'మత విద్వేషం {qw}'
    if 'regionalism' in ql and 'son of soil' in ql: return f'Sons of Soil ప్రాంతీయవాదం {qw}'
    if 'regionalism' in ql and ('separate state' in ql or 'demand' in ql): return f'ప్రాంతీయ రాష్ట్ర డిమాండ్ {qw}'
    if 'regionalism' in ql: return f'ప్రాంతీయవాదం {qw}'
    if 'casteism' in ql or ('caste' in ql and 'threat' in ql): return f'కుల వివక్ష సమస్య {qw}'
    if 'linguistic' in ql and ('state' in ql or 'reorganis' in ql or 'reorganiz' in ql): return f'భాషా ప్రాతిపదికన రాష్ట్రాల ఏర్పాటు {qw}'
    if ('language' in ql and 'chauvinism' in ql) or 'linguistic' in ql: return f'భాషా చావినిజం {qw}'
    if 'dravida' in ql or 'dmk' in ql or ('tamil' in ql and 'separ' in ql): return f'ద్రావిడ ఉద్యమం {qw}'
    if 'northeast' in ql or 'north east' in ql or 'north-east' in ql: return f'ఈశాన్య భారత సమస్య {qw}'
    if 'naxal' in ql: return f'నక్సలిజం సమస్య {qw}'
    if 'terrorism' in ql or 'terrorist' in ql: return f'ఉగ్రవాదం సమస్య {qw}'
    if 'insurgency' in ql: return f'తిరుగుబాటు సమస్య {qw}'
    if 'kashmir' in ql or 'jammu' in ql: return f'కాశ్మీర్ సమస్య {qw}'
    if 'article 356' in ql or "president's rule" in ql or 'president rule' in ql: return f'అధికరణ 356 అనువర్తనం {qw}'
    if 'secularism' in ql: return f'లౌకికవాదం భావన {qw}'
    if 'national integration' in ql and ('mean' in ql or 'define' in ql or 'primarily' in ql): return f'జాతీయ సమైక్యత అర్థం {qw}'
    if 'national integration' in ql: return f'జాతీయ సమైక్యత {qw}'
    if 'nehru' in ql: return f'నెహ్రూ జాతీయ సమైక్యత {qw}'
    return f'జాతీయ సమైక్యత {qw}'

def make_prefix_ch88(q):
    ql = q.lower()
    qw = get_telugu_question_word(q)
    if 'panchsheel' in ql: return f'పంచశీల సూత్రాలు {qw}'
    if 'non-aligned' in ql or 'non aligned' in ql or ql.startswith('nam ') or ' nam ' in ql: return f'NAM జతకట్టని ఉద్యమం {qw}'
    if 'bandung' in ql: return f'బాండుంగ్ సమావేశం {qw}'
    if 'look east' in ql: return f'Look East విధానం {qw}'
    if 'act east' in ql: return f'Act East విధానం {qw}'
    if 'quad' in ql: return f'QUAD కూటమి {qw}'
    if 'pokhran' in ql or ('nuclear test' in ql and ('1974' in ql or '1998' in ql)): return f'పోఖ్రాన్ అణు పరీక్ష {qw}'
    if 'nuclear doctrine' in ql or 'no first use' in ql: return f'భారత అణు సిద్ధాంతం {qw}'
    if 'npt' in ql or 'non-proliferation' in ql: return f'అణు అప్రసార ఒప్పందం {qw}'
    if 'ctbt' in ql: return f'CTBT అణు పరీక్ష నిషేధం {qw}'
    if 'nsg' in ql: return f'NSG అణు సరఫరా సమూహం {qw}'
    if ('india' in ql and 'us' in ql and 'nuclear' in ql) or '123 agreement' in ql: return f'భారత-అమెరికా అణు ఒప్పందం {qw}'
    if 'gujral doctrine' in ql or 'gujral' in ql: return f'గుజ్రాల్ సిద్ధాంతం {qw}'
    if 'saarc' in ql: return f'SAARC సహకారం {qw}'
    if 'brics' in ql: return f'BRICS కూటమి {qw}'
    if 'g20' in ql or 'g-20' in ql: return f'G20 వేదిక {qw}'
    if 'tashkent' in ql: return f'తాష్కెంట్ ఒప్పందం {qw}'
    if 'simla' in ql or 'shimla' in ql: return f'సిమ్లా ఒప్పందం {qw}'
    if 'suez' in ql: return f'సూయెజ్ సంక్షోభం {qw}'
    if 'tibet' in ql: return f'టిబెట్ విషయంలో విధానం {qw}'
    if 'goa' in ql and ('liberat' in ql or 'integrat' in ql or 'annex' in ql): return f'గోవా విముక్తి చర్య {qw}'
    if 'indo-soviet' in ql or ('soviet' in ql and 'india' in ql and 'treaty' in ql): return f'భారత-సోవియట్ స్నేహ ఒప్పందం {qw}'
    if 'soviet' in ql or 'ussr' in ql or 'russia' in ql: return f'భారత-రష్యా సంబంధాలు {qw}'
    if 'china' in ql and '1962' in ql: return f'1962 చైనా యుద్ధం {qw}'
    if 'china' in ql: return f'భారత-చైనా సంబంధాలు {qw}'
    if 'pakistan' in ql and ('war' in ql or '1971' in ql or '1965' in ql or '1999' in ql): return f'భారత-పాక్ యుద్ధం {qw}'
    if 'pakistan' in ql: return f'భారత-పాకిస్తాన్ సంబంధాలు {qw}'
    if 'nehru' in ql and ('foreign' in ql or 'policy' in ql): return f'నెహ్రూ విదేశాంగ విధానం {qw}'
    if 'indo-pacific' in ql: return f'Indo-Pacific భావన {qw}'
    if 'neighbour' in ql or 'neighborhood' in ql or 'neighbourhood' in ql: return f'పొరుగు దేశాల విధానం {qw}'
    if 'foreign policy' in ql and ('define' in ql or 'meaning' in ql or 'primarily' in ql or 'best define' in ql): return f'విదేశాంగ విధానం నిర్వచనం {qw}'
    if 'foreign policy' in ql: return f'విదేశాంగ విధానం {qw}'
    return f'విదేశాంగ విధానం {qw}'

def make_prefix_ch89(q):
    ql = q.lower()
    qw = get_telugu_question_word(q)
    if 'venkatachaliah' in ql or ('chairman' in ql and 'ncrwc' in ql): return f'NCRWC Chairman {qw}'
    if 'ncrwc' in ql and ('year' in ql or 'establish' in ql or 'set up' in ql or 'constitut' in ql or 'when' in ql): return f'NCRWC స్థాపన {qw}'
    if 'ncrwc' in ql and ('term' in ql or 'how many' in ql or 'member' in ql): return f'NCRWC నిర్మాణం {qw}'
    if 'ncrwc' in ql and ('recommend' in ql or 'report' in ql or 'suggest' in ql or 'propose' in ql): return f'NCRWC సిఫారసులు {qw}'
    if 'ncrwc' in ql: return f'NCRWC రాజ్యాంగ సమీక్ష {qw}'
    if 'simultaneous election' in ql or 'one nation one election' in ql or 'one nation, one election' in ql: return f'ఒకేసారి ఎన్నికలు {qw}'
    if 'anti-defection' in ql or 'defection' in ql or 'tenth schedule' in ql or '10th schedule' in ql: return f'పక్ష విరోధ నిషేధ చట్టం {qw}'
    if 'fundamental duties' in ql: return f'ప్రాథమిక విధులు {qw}'
    if 'directive principles' in ql or 'dpsp' in ql: return f'ఆదేశ సూత్రాలు {qw}'
    if 'fundamental rights' in ql: return f'ప్రాథమిక హక్కులు {qw}'
    if 'article 368' in ql: return f'అధికరణ 368 సవరణ అధికారం {qw}'
    if 'women' in ql and ('reservation' in ql or '33%' in ql or '33 %' in ql): return f'మహిళా రిజర్వేషన్ {qw}'
    if 'right to education' in ql: return f'విద్య హక్కు {qw}'
    if 'right to information' in ql or 'rti' in ql: return f'సమాచార హక్కు {qw}'
    if 'lokpal' in ql: return f'లోక్పాల్ సంస్థ {qw}'
    if 'electoral reform' in ql or 'election reform' in ql: return f'ఎన్నికల సంస్కరణలు {qw}'
    if 'proportional representation' in ql: return f'అనుపాత ప్రాతినిధ్య విధానం {qw}'
    if 'coalition' in ql or 'hung parliament' in ql: return f'సంకీర్ణ ప్రభుత్వం {qw}'
    if ('president' in ql and 'rule' in ql) or '356' in ql: return f'రాష్ట్రపతి పాలన {qw}'
    if 'vajpayee' in ql: return f'వాజ్పేయి ప్రభుత్వం {qw}'
    if 'constitution' in ql and ('review' in ql or 'working' in ql): return f'రాజ్యాంగ సమీక్ష {qw}'
    if 'reservation' in ql and ('obc' in ql or 'backward' in ql): return f'OBC రిజర్వేషన్ {qw}'
    if 'reservation' in ql and ('sc' in ql or 'st' in ql): return f'SC/ST రిజర్వేషన్ {qw}'
    return f'రాజ్యాంగ సమీక్ష కమిషన్ {qw}'

def make_prefix_ch90(q):
    ql = q.lower()
    qw = get_telugu_question_word(q)
    if 'kesavananda bharati' in ql or 'kesavananda' in ql: return f'Kesavananda Bharati కేసు {qw}'
    if 'maneka gandhi' in ql or ('maneka' in ql and 'uoi' in ql): return f'Maneka Gandhi కేసు {qw}'
    if 'minerva mills' in ql: return f'Minerva Mills కేసు {qw}'
    if 'golaknath' in ql: return f'Golaknath కేసు {qw}'
    if 'waman rao' in ql: return f'Waman Rao కేసు {qw}'
    if 'sajjan singh' in ql: return f'Sajjan Singh కేసు {qw}'
    if 'shankari prasad' in ql: return f'Shankari Prasad కేసు {qw}'
    if 'adm jabalpur' in ql: return f'ADM జబల్పూర్ కేసు {qw}'
    if 'shah bano' in ql: return f'Shah Bano కేసు {qw}'
    if 'olga tellis' in ql: return f'Olga Tellis కేసు {qw}'
    if 'vishaka' in ql or 'vishakha' in ql: return f'విశాఖ మార్గదర్శకాలు {qw}'
    if 'navtej johar' in ql or 'section 377' in ql or 'decriminaliz' in ql or 'decriminalis' in ql: return f'Navtej Johar కేసు {qw}'
    if 'puttaswamy' in ql or 'right to privacy' in ql: return f'K.S. Puttaswamy గోప్యత హక్కు {qw}'
    if 'unnikrishnan' in ql: return f'Unnikrishnan కేసు {qw}'
    if 'coelho' in ql or 'i.r. coelho' in ql: return f'I.R. Coelho కేసు {qw}'
    if 'habeas corpus' in ql and 'emergency' in ql: return f'అత్యవసర పరిస్థితి హేబియస్ కార్పస్ {qw}'
    if 'habeas corpus' in ql: return f'హేబియస్ కార్పస్ హక్కు {qw}'
    if 'pucl' in ql and 'nota' in ql: return f'PUCL NOTA తీర్పు {qw}'
    if 'adr' in ql and ('criminal' in ql or 'candidate' in ql or 'disclosure' in ql or 'election' in ql): return f'ADR అభ్యర్థి వివరాల తీర్పు {qw}'
    if 'basic structure' in ql: return f'Basic Structure సిద్ధాంతం {qw}'
    if 'article 21' in ql and 'right to life' in ql: return f'అధికరణ 21 జీవన హక్కు {qw}'
    if 'article 21' in ql: return f'అధికరణ 21 {qw}'
    if 'right to life' in ql: return f'జీవన హక్కు {qw}'
    if 'right to food' in ql: return f'ఆహార హక్కు {qw}'
    if 'mgnrega' in ql or 'mnrega' in ql: return f'MGNREGA ఉపాధి హక్కు {qw}'
    if 'right to education' in ql or ('education' in ql and 'free' in ql and 'right' in ql): return f'విద్య హక్కు తీర్పు {qw}'
    if 'privacy' in ql: return f'గోప్యత హక్కు తీర్పు {qw}'
    if 'aadhaar' in ql or 'aadhar' in ql: return f'ఆధార్ చట్టం తీర్పు {qw}'
    if 'article 370' in ql: return f'అధికరణ 370 రద్దు తీర్పు {qw}'
    if 'triple talaq' in ql: return f'ట్రిపుల్ తలాక్ తీర్పు {qw}'
    if 'sexual harassment' in ql: return f'లైంగిక వేధింపు మార్గదర్శకాలు {qw}'
    if 'pil' in ql or 'public interest litigation' in ql: return f'ప్రజాహిత వ్యాజ్యం {qw}'
    if 'fundamental rights' in ql and 'amend' in ql: return f'ప్రాథమిక హక్కులు సవరణ {qw}'
    if 'fundamental rights' in ql: return f'ప్రాథమిక హక్కులు {qw}'
    if 'parliament' in ql and 'amend' in ql and ('unlimited' in ql or 'power' in ql): return f'పార్లమెంట్ సవరణ అధికారం {qw}'
    if 'ninth schedule' in ql or '9th schedule' in ql: return f'తొమ్మిదవ షెడ్యూలు {qw}'
    if 'emergency' in ql: return f'అత్యవసర పరిస్థితి తీర్పు {qw}'
    if '13-judge' in ql or '13 judge' in ql or 'largest bench' in ql: return f'13 మంది న్యాయమూర్తుల ధర్మాసనం {qw}'
    return f'చారిత్రక తీర్పు {qw}'

HANDLERS = {86: make_prefix_ch86, 87: make_prefix_ch87, 88: make_prefix_ch88, 89: make_prefix_ch89, 90: make_prefix_ch90}

def has_telugu(s):
    return any('\u0c00' <= c <= '\u0c7f' for c in s)

def add_prefix(question, ch):
    if has_telugu(question):
        return question
    prefix = HANDLERS[ch](question)
    return f'{prefix} / {question}'

def process_file(filepath, ch):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = 0

    # Match MCQ tuple openings: (int, 'diff', 'question'
    # Handles both single-quoted and situations where question might span lines
    pattern = re.compile(
        r"""(\(\s*\d+\s*,\s*'(?:easy|medium|hard)'\s*,\s*)"""
        r"""('(?:[^'\\]|\\.)*'|"(?:[^"\\]|\\.)*")""",
        re.DOTALL
    )

    def replacer(m):
        nonlocal modified
        prefix_part = m.group(1)
        raw_q = m.group(2)

        if raw_q.startswith("'"):
            q_inner = raw_q[1:-1]
            quote = "'"
        else:
            q_inner = raw_q[1:-1]
            quote = '"'

        # Unescape to get display text
        actual = q_inner.replace("\\'", "'").replace('\\"', '"')

        if has_telugu(actual):
            return m.group(0)

        new_q = add_prefix(actual, ch)
        modified += 1

        # Re-escape for storage
        if quote == "'":
            stored = new_q.replace('\\', '\\\\').replace("'", "\\'")
        else:
            stored = new_q.replace('\\', '\\\\').replace('"', '\\"')

        return f"{prefix_part}{quote}{stored}{quote}"

    new_content = pattern.sub(replacer, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return modified

BASE = '/sessions/vigilant-vibrant-fermat/mnt/mcq_app'
FILES = {
    86: f'{BASE}/seed_polity_ch86.py',
    87: f'{BASE}/seed_polity_ch87.py',
    88: f'{BASE}/seed_polity_ch88.py',
    89: f'{BASE}/seed_polity_ch89.py',
    90: f'{BASE}/seed_polity_ch90.py',
}

for ch, path in FILES.items():
    n = process_file(path, ch)
    print(f'ch{ch}: modified {n} questions')

print('\n--- Verification ---')
for ch, path in FILES.items():
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    pat = re.compile(
        r"""\(\s*\d+\s*,\s*'(?:easy|medium|hard)'\s*,\s*('(?:[^'\\]|\\.)*'|"(?:[^"\\]|\\.)*")""",
        re.DOTALL
    )
    all_qs = pat.findall(content)
    with_telugu = sum(1 for q in all_qs if has_telugu(q))
    print(f'  ch{ch}: {len(all_qs)} total MCQs, {with_telugu} with Telugu prefix')
