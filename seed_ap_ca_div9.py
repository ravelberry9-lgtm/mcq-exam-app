"""
seed_ap_ca_div9.py
AP Current Affairs — Chapter 9: పద్మ పురస్కారాలు, కేంద్ర సంస్థలు, AP హైకోర్టు & రాజ్యాంగం
"""

import os
import json

SECTIONS_JSON = json.dumps([
    {
        "id": "div9_s1",
        "title": "పరీక్ష కోసం కీలక భావనలు",
        "summary": "పద్మ పురస్కారాలు, జాతీయ పురస్కారాలు, కేంద్ర సంస్థలు, AP హైకోర్టు, రాజ్యాంగ అంశాలు — పరీక్ష హాట్‌స్పాట్‌లు"
    },
    {
        "id": "div9_s2",
        "title": "పద్మ పురస్కారాలు — AP వ్యక్తులు",
        "summary": "2025: Balakrishna (PB), Nageshwar Reddy (PV-TG), Manda Krishna Madiga (PS-TG) = 7 Telugu; 2026: Nori (PB-USA), 4 AP Shri, 7 TG Shri = 12 Telugu; SP బాలసుబ్రహ్మణ్యం PV 2021; K. విశ్వనాథ్ PV 2017"
    },
    {
        "id": "div9_s3",
        "title": "Oscar & అంతర్జాతీయ పురస్కారాలు",
        "summary": "Oscar 2023: నాటు నాటు (RRR) — MM కీరవాణి; 69వ NFA: అల్లు అర్జున్ Best Actor (Pushpa) — తొలి తెలుగు నటుడు; DSP Best Music (Songs); 70వ NFA: Karthikeya 2 (Best Telugu); 71వ NFA: Bhagavanth Kesari (Best Telugu), Baby (Screenplay+Playback)"
    },
    {
        "id": "div9_s4",
        "title": "సాహిత్య & సాంస్కృతిక పురస్కారాలు",
        "summary": "విశ్వనాథ సత్యనారాయణ — జ్ఞానపీఠ పురస్కారం 1970 (మొదటి తెలుగు జ్ఞానపీఠ); దాదాసాహేబ్ ఫాల్కే 2016 = K. విశ్వనాథ్; సాహిత్య అకాడమి"
    },
    {
        "id": "div9_s5",
        "title": "కేంద్ర విద్యా సంస్థలు — AP",
        "summary": "IIT తిరుపతి (2015), NIT AP-తాడేపల్లిగూడెం (2015), AIIMS మంగళగిరి (2020/2022), CUAP అనంతపురం (2014/2016), IISER తిరుపతి (2015)"
    },
    {
        "id": "div9_s6",
        "title": "AP హైకోర్టు",
        "summary": "AP పునర్విభజన చట్టం 2014 సెక్షన్ 30; జన. 1, 2019 అమరావతిలో ప్రత్యేక AP HC; Justice Dhiraj Singh Thakur (5వ CJ, Jul 2023–Apr 2026); Justice Lisa Gill — 6వ CJ, AP HC తొలి మహిళా CJ (Apr 25, 2026)"
    },
    {
        "id": "div9_s7",
        "title": "రాజ్యాంగం & AP",
        "summary": "ఆర్టికల్ 371-డి (32వ సవరణ 1973); APRA 2014 ముఖ్యాంశాలు; ప్రత్యేక హోదా డిమాండ్; APRA సవరణ 2026"
    },
    {
        "id": "div9_s8",
        "title": "AP జిల్లాలు & రాజ్యాంగ పదవులు",
        "summary": "13→26 జిల్లాలు (ఏప్రిల్ 2022)→28 జిల్లాలు (జన. 1, 2026); గవర్నర్ S. అబ్దుల్ నజీర్; CM చంద్రబాబు (జూన్ 12, 2024); 175 అసెంబ్లీ, 25 LS, 11 RS స్థానాలు"
    },
    {
        "id": "div9_s9",
        "title": "పరీక్ష రేపిడ్ రివిజన్",
        "summary": "పద్మ పురస్కారాలు, పురస్కారాలు, సంస్థలు, హైకోర్టు, రాజ్యాంగం — సంక్షిప్త పట్టిక"
    }
], ensure_ascii=False)

MCQ_DATA = [
    # Section 0 — Key concepts
    {
        "section_idx": 0,
        "difficulty": "easy",
        "question_te": "పద్మ విభూషణ్ భారతదేశంలో ఏ స్థాయి పురస్కారం?",
        "opt_a": "అత్యున్నత పౌర పురస్కారం",
        "opt_b": "రెండవ అత్యున్నత పౌర పురస్కారం",
        "opt_c": "మూడవ అత్యున్నత పౌర పురస్కారం",
        "opt_d": "నాల్గవ అత్యున్నత పౌర పురస్కారం",
        "answer": "B",
        "explanation_te": "పద్మ పురస్కారాల క్రమం: భారత రత్న (అత్యున్నతం) → పద్మ విభూషణ్ (2వ) → పద్మ భూషణ్ (3వ) → పద్మ శ్రీ (4వ). గణతంత్ర దినం (జనవరి 26) నాడు ప్రకటిస్తారు."
    },
    {
        "section_idx": 0,
        "difficulty": "medium",
        "question_te": "పద్మ పురస్కారాలు ఏ సందర్భంగా ప్రకటిస్తారు?",
        "opt_a": "స్వాతంత్ర్య దినం (ఆగస్ట్ 15)",
        "opt_b": "గణతంత్ర దినం (జనవరి 26) సందర్భంగా",
        "opt_c": "రాష్ట్ర ఆవిర్భావ దినం",
        "opt_d": "ప్రధానమంత్రి జన్మదినం",
        "answer": "B",
        "explanation_te": "పద్మ పురస్కారాలు ప్రతి సంవత్సరం గణతంత్ర దినం (జనవరి 26) సందర్భంగా ప్రకటిస్తారు. రాష్ట్రపతి అందిస్తారు."
    },
    # Section 1 — Padma Awards AP personalities
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "SP బాలసుబ్రహ్మణ్యంకు పద్మ విభూషణ్ ఏ సంవత్సరం ఇచ్చారు?",
        "opt_a": "2019",
        "opt_b": "2020",
        "opt_c": "2021 (మరణానంతరం)",
        "opt_d": "2022",
        "answer": "C",
        "explanation_te": "SP బాలసుబ్రహ్మణ్యం (SPB) కి 2021లో పద్మ విభూషణ్ మరణానంతరం (Posthumously) ఇచ్చారు. ఆయన సెప్టెంబర్ 2020లో COVID-19 తో మరణించారు. ఆయన నెల్లూరు జిల్లాకు చెందినవారు."
    },
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "K. విశ్వనాథ్‌కు పద్మ విభూషణ్ ఏ సంవత్సరం ఇచ్చారు?",
        "opt_a": "2010",
        "opt_b": "2017",
        "opt_c": "2019",
        "opt_d": "2021",
        "answer": "B",
        "explanation_te": "కాసినధుని విశ్వనాథ్ (దర్శకుడు) కి 2017లో పద్మ విభూషణ్ ఇచ్చారు. ఆయన 'సంకర్శణం', 'శంకరాభరణం' వంటి చిత్రాలకు ప్రసిద్ధుడు. కృష్ణా జిల్లాకు చెందినవారు."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "చిరంజీవికి పద్మ భూషణ్ ఏ సంవత్సరం ఇచ్చారు?",
        "opt_a": "2000",
        "opt_b": "2006",
        "opt_c": "2010",
        "opt_d": "2014",
        "answer": "B",
        "explanation_te": "చిరంజీవి (మేఘా శ్యామ్) కి 2006లో పద్మ భూషణ్ ఇచ్చారు. ఆయన పశ్చిమ గోదావరి జిల్లాలోని నరసాపురానికి చెందినవారు."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "SS రాజమౌళికి పద్మ శ్రీ ఏ సంవత్సరం ఇచ్చారు?",
        "opt_a": "2009",
        "opt_b": "2012",
        "opt_c": "2015",
        "opt_d": "2018",
        "answer": "B",
        "explanation_te": "SS రాజమౌళికి 2012లో పద్మ శ్రీ ఇచ్చారు. ఆయన రాజమండ్రి (తూర్పు గోదావరి జిల్లా) లో జన్మించారు; తండ్రి కుటుంబ మూలాలు నెల్లూరు జిల్లా కోవూరు. 'బాహుబలి', 'RRR' చిత్రాలకు ప్రసిద్ధుడు."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "K. విశ్వనాథ్‌కు దాదాసాహేబ్ ఫాల్కే పురస్కారం ఏ సంవత్సరం ఇచ్చారు?",
        "opt_a": "2014",
        "opt_b": "2016",
        "opt_c": "2018",
        "opt_d": "2020",
        "answer": "B",
        "explanation_te": "K. విశ్వనాథ్‌కు 2016 సంవత్సరానికి దాదాసాహేబ్ ఫాల్కే పురస్కారం (భారత సినిమా అత్యున్నత పురస్కారం) ఇచ్చారు. ఇది 2017లో ప్రదానం చేశారు."
    },
    {
        "section_idx": 1,
        "difficulty": "hard",
        "question_te": "PV సింధుకు పద్మ భూషణ్ ఏ సంవత్సరం ఇచ్చారు?",
        "opt_a": "2016",
        "opt_b": "2018",
        "opt_c": "2020",
        "opt_d": "2022",
        "answer": "C",
        "explanation_te": "PV సింధుకు 2020లో పద్మ భూషణ్ ఇచ్చారు (రియో 2016 రజత తర్వాత 2015లో పద్మ శ్రీ, తర్వాత 2020లో పద్మ భూషణ్). కోచ్ గోపీచంద్‌కు 2014లో పద్మ భూషణ్."
    },
    # Section 2 — Oscar & International Awards
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "'నాటు నాటు' పాటకు Oscar పురస్కారం ఏ సంవత్సరం వచ్చింది?",
        "opt_a": "2022 (94వ)",
        "opt_b": "2023 (95వ)",
        "opt_c": "2024 (96వ)",
        "opt_d": "2021 (93వ)",
        "answer": "B",
        "explanation_te": "'నాటు నాటు' (RRR చిత్రం) కి 95వ Academy Awards (2023)లో Best Original Song Oscar వచ్చింది. సంగీతం MM కీరవాణి; సాహిత్యం: చంద్రబోస్."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "MM కీరవాణి ఏ జిల్లాకు చెందినవారు?",
        "opt_a": "విశాఖపట్నం",
        "opt_b": "కృష్ణా జిల్లా (కోడూరు)",
        "opt_c": "నెల్లూరు",
        "opt_d": "గుంటూరు",
        "answer": "B",
        "explanation_te": "MM కీరవాణి (Maragathamani Keeravani) కృష్ణా జిల్లాలోని కోడూరులో జన్మించారు. SS రాజమౌళికి బంధువు. 'నాటు నాటు' కి Oscar 2023 సాధించారు."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "'నాటు నాటు' పాటకు Golden Globe పురస్కారం కూడా వచ్చిందా?",
        "opt_a": "లేదు",
        "opt_b": "అవును — 2023 Best Original Song",
        "opt_c": "నామినేషన్ మాత్రమే",
        "opt_d": "2022లో వచ్చింది",
        "answer": "B",
        "explanation_te": "'నాటు నాటు' పాటకు 2023 Golden Globe Awards లో Best Original Song పురస్కారం వచ్చింది — Oscar కంటే ముందే, ఇది Oscar విజయానికి సంకేతంగా నిలిచింది."
    },
    # Section 2 — National Film Awards (additional - corrected facts)
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "తెలుగు నటులలో తొలిసారిగా జాతీయ చలనచిత్ర పురస్కారంలో Best Actor సాధించిన నటుడు ఎవరు?",
        "opt_a": "చిరంజీవి",
        "opt_b": "అల్లు అర్జున్",
        "opt_c": "మహేశ్ బాబు",
        "opt_d": "జూనియర్ NTR",
        "answer": "B",
        "explanation_te": "అల్లు అర్జున్ 69వ జాతీయ చలనచిత్ర పురస్కారాలు (2022)లో Pushpa: The Rise చిత్రానికి Best Actor పురస్కారం సాధించారు — తెలుగు నటులలో ఇది తొలి జాతీయ Best Actor పురస్కారం."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "అల్లు అర్జున్‌కు Best Actor National Award ఏ చిత్రానికి వచ్చింది?",
        "opt_a": "Ala Vaikunthapurramuloo",
        "opt_b": "Pushpa 2: The Rule",
        "opt_c": "Pushpa: The Rise",
        "opt_d": "Arya",
        "answer": "C",
        "explanation_te": "అల్లు అర్జున్‌కు 'Pushpa: The Rise' (2021 డిసెంబర్ విడుదల) చిత్రానికి 69వ జాతీయ పురస్కారాల్లో Best Actor వచ్చింది. ఇదే చిత్రానికి దేవి శ్రీ ప్రసాద్‌కు Best Music (Songs) కూడా వచ్చింది."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "69వ జాతీయ చలనచిత్ర పురస్కారాల్లో Best Music Direction (Songs) ఎవరికి వచ్చింది?",
        "opt_a": "MM కీరవాణి",
        "opt_b": "S. తమన్",
        "opt_c": "దేవి శ్రీ ప్రసాద్ (DSP)",
        "opt_d": "Ilaiyaraaja",
        "answer": "C",
        "explanation_te": "69వ జాతీయ పురస్కారాల్లో దేవి శ్రీ ప్రసాద్ (DSP) కి Pushpa: The Rise చిత్రానికి Best Music Direction (Songs) వచ్చింది. MM కీరవాణి అదే వేడుకలో RRR కి Best Music Direction (Background Music) సాధించారు."
    },
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "71వ జాతీయ చలనచిత్ర పురస్కారాల్లో Best Telugu Film ఏది?",
        "opt_a": "Baby",
        "opt_b": "Karthikeya 2",
        "opt_c": "Bhagavanth Kesari",
        "opt_d": "Pushpa 2",
        "answer": "C",
        "explanation_te": "71వ జాతీయ చలనచిత్ర పురస్కారాల్లో (2023 చిత్రాలకు) Bhagavanth Kesari (బాలకృష్ణ నటించిన చిత్రం; Anil Ravipudi దర్శకత్వం) Best Telugu Film గెలుచుకుంది. 70వ పురస్కారాల్లో Karthikeya 2 Best Telugu Film అయింది."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "71వ జాతీయ పురస్కారాల్లో Baby చిత్రానికి Best Screenplay ఎవరికి వచ్చింది?",
        "opt_a": "అనంద్ దేవరాకొండ",
        "opt_b": "Sai Rajesh",
        "opt_c": "PVNS Rohith",
        "opt_d": "Chandoo Mondeti",
        "answer": "B",
        "explanation_te": "Baby (2023 తెలుగు చిత్రం; దర్శకుడు Sai Rajesh) కి 71వ జాతీయ పురస్కారాల్లో 2 పురస్కారాలు వచ్చాయి: Best Screenplay (Sai Rajesh) + Best Playback Singer Male (PVNS Rohith — 'Premistunna'). అనంద్ దేవరాకొండ నటించిన చిత్రం."
    },

    # Section 3 — Literary & Cultural Awards
    {
        "section_idx": 3,
        "difficulty": "easy",
        "question_te": "తెలుగు భాషలో మొదటి జ్ఞానపీఠ పురస్కారం ఎవరికి వచ్చింది?",
        "opt_a": "విశ్వనాథ సత్యనారాయణ",
        "opt_b": "శ్రీశ్రీ",
        "opt_c": "C. నారాయణ రెడ్డి",
        "opt_d": "K. విశ్వనాథ్",
        "answer": "A",
        "explanation_te": "విశ్వనాథ సత్యనారాయణకు 1970లో జ్ఞానపీఠ పురస్కారం వచ్చింది — ఇది తెలుగు భాషలో మొదటిది. 'రామాయణ కల్పవృక్షం' రచన ముఖ్యం."
    },
    {
        "section_idx": 3,
        "difficulty": "medium",
        "question_te": "దాదాసాహేబ్ ఫాల్కే పురస్కారం ఏ రంగంలో ఇస్తారు?",
        "opt_a": "సాహిత్యం",
        "opt_b": "భారత సినిమా (జీవిత కాల సేవ)",
        "opt_c": "క్రీడలు",
        "opt_d": "శాస్త్ర విజ్ఞానం",
        "answer": "B",
        "explanation_te": "దాదాసాహేబ్ ఫాల్కే పురస్కారం భారత సినిమాలో జీవిత కాల సేవకు ఇస్తారు. ఇది సినిమా రంగంలో అత్యున్నత జాతీయ పురస్కారం. 2016కు K. విశ్వనాథ్‌కు ఇచ్చారు."
    },
    # Section 4 — Central Educational Institutions
    {
        "section_idx": 4,
        "difficulty": "easy",
        "question_te": "IIT తిరుపతి ఏ జిల్లాలో ఉంది?",
        "opt_a": "వైఎస్సార్ కడప జిల్లా",
        "opt_b": "తిరుపతి జిల్లా (యేర్పేడు)",
        "opt_c": "అనంతపురం జిల్లా",
        "opt_d": "చిత్తూరు జిల్లా",
        "answer": "B",
        "explanation_te": "IIT తిరుపతి తిరుపతి జిల్లాలోని యేర్పేడులో ఉంది. 2015లో స్థాపించారు. తొమ్మిది IIT లలో ఒకటి."
    },
    {
        "section_idx": 4,
        "difficulty": "medium",
        "question_te": "AIIMS మంగళగిరి ఏ జిల్లాలో ఉంది?",
        "opt_a": "తిరుపతి జిల్లా",
        "opt_b": "గుంటూరు జిల్లా",
        "opt_c": "కృష్ణా జిల్లా",
        "opt_d": "విశాఖపట్నం జిల్లా",
        "answer": "B",
        "explanation_te": "AIIMS మంగళగిరి గుంటూరు జిల్లాలో ఉంది. 2022లో పూర్తి స్థాయిలో ప్రారంభించారు. PMSSY (Pradhan Mantri Swasthya Suraksha Yojana) కింద స్థాపించారు."
    },
    {
        "section_idx": 4,
        "difficulty": "medium",
        "question_te": "NIT ఆంధ్రప్రదేశ్ ఏ జిల్లాలో ఉంది?",
        "opt_a": "కాకినాడ",
        "opt_b": "ఏలూరు జిల్లా (తాడేపల్లిగూడెం దగ్గర)",
        "opt_c": "విశాఖపట్నం",
        "opt_d": "రాజమహేంద్రవరం",
        "answer": "B",
        "explanation_te": "NIT ఆంధ్రప్రదేశ్ ఏలూరు జిల్లాలో (తాడేపల్లిగూడెం సమీపంలో) ఉంది. 2015లో స్థాపించారు. 31 NITs లో ఒకటి."
    },
    {
        "section_idx": 4,
        "difficulty": "hard",
        "question_te": "CUAP (Central University of Andhra Pradesh) ఏ జిల్లాలో ఉంది?",
        "opt_a": "నెల్లూరు",
        "opt_b": "అనంతపురం (నందేడు)",
        "opt_c": "కర్నూలు",
        "opt_d": "చిత్తూరు",
        "answer": "B",
        "explanation_te": "CUAP (Central University of Andhra Pradesh) అనంతపురం జిల్లాలోని నందేడులో ఉంది. 2014లో స్థాపించి 2016లో తాత్కాలిక ప్యాంపస్ ప్రారంభించారు."
    },
    # Section 5 — AP High Court
    {
        "section_idx": 5,
        "difficulty": "easy",
        "question_te": "AP పునర్విభజన తర్వాత ప్రత్యేక AP హైకోర్టు ఎప్పుడు ప్రారంభమైంది?",
        "opt_a": "జూన్ 2, 2014",
        "opt_b": "జనవరి 1, 2019",
        "opt_c": "మార్చి 2, 2019",
        "opt_d": "నవంబర్ 1, 2019",
        "answer": "B",
        "explanation_te": "AP పునర్విభజన చట్టం 2014 (Section 30) ప్రకారం, జనవరి 1, 2019 నుండి అమరావతిలో ప్రత్యేక ఆంధ్రప్రదేశ్ హైకోర్టు ప్రారంభమైంది. 2014-2018 వరకు హైదరాబాద్ హైకోర్టు రెండు రాష్ట్రాలకు పనిచేసింది."
    },
    {
        "section_idx": 5,
        "difficulty": "medium",
        "question_te": "AP పునర్విభజన చట్టం 2014 లో హైకోర్టు గురించిన నిబంధన ఏ సెక్షన్ లో ఉంది?",
        "opt_a": "సెక్షన్ 3",
        "opt_b": "సెక్షన్ 15",
        "opt_c": "సెక్షన్ 30",
        "opt_d": "సెక్షన్ 45",
        "answer": "C",
        "explanation_te": "APRA 2014 సెక్షన్ 30 ప్రకారం ప్రత్యేక AP హైకోర్టు ఏర్పాటు చేయాలి. 2014–2018 వరకు నాలుగేళ్ళు హైదరాబాద్ హైకోర్టే రెండు రాష్ట్రాలకు పనిచేసింది."
    },
    # Section 6 — Constitution & AP
    {
        "section_idx": 6,
        "difficulty": "easy",
        "question_te": "ఆర్టికల్ 371-డి ఏ రాష్ట్రానికి వర్తిస్తుంది?",
        "opt_a": "తెలంగాణ",
        "opt_b": "ఆంధ్రప్రదేశ్",
        "opt_c": "తమిళనాడు",
        "opt_d": "కర్నాటక",
        "answer": "B",
        "explanation_te": "ఆర్టికల్ 371-డి ఆంధ్రప్రదేశ్‌కు వర్తిస్తుంది. 32వ రాజ్యాంగ సవరణ (1973) ద్వారా చేర్చారు. స్థానిక ఉద్యోగాలు, విద్య లో రిజర్వేషన్ కల్పిస్తుంది."
    },
    {
        "section_idx": 6,
        "difficulty": "medium",
        "question_te": "ఆర్టికల్ 371-డి ఏ రాజ్యాంగ సవరణ ద్వారా వచ్చింది?",
        "opt_a": "25వ సవరణ",
        "opt_b": "32వ సవరణ (1973)",
        "opt_c": "42వ సవరణ",
        "opt_d": "44వ సవరణ",
        "answer": "B",
        "explanation_te": "ఆర్టికల్ 371-డి 32వ రాజ్యాంగ సవరణ (1973) ద్వారా చేర్చారు. దీని ప్రకారం 1975లో Presidential Order జారీ అయింది — స్థానిక ఉద్యోగ రక్షణకు ప్రాతిపదిక."
    },
    {
        "section_idx": 6,
        "difficulty": "medium",
        "question_te": "AP కి 'ప్రత్యేక హోదా' (Special Category Status) ఎందుకు ఇవ్వలేదు?",
        "opt_a": "AP అభ్యర్థించలేదు",
        "opt_b": "14వ ఆర్థిక సంఘం SCS ప్రమాణాలు మార్చింది; NITI Aayog SCS ముగించింది",
        "opt_c": "కేంద్రం వ్యతిరేకించింది మాత్రమే",
        "opt_d": "AP అర్హత లేదు",
        "answer": "B",
        "explanation_te": "14వ ఆర్థిక సంఘం SCS ప్రమాణాలు మార్చింది; NITI Aayog 2015లో Planning Commission స్థానంలో వచ్చి SCS విధానం ముగించింది. కేంద్రం 'Special Assistance' ప్యాకేజ్ ఇచ్చింది."
    },
    # Section 7 — AP Districts & Constitutional positions
    {
        "section_idx": 7,
        "difficulty": "easy",
        "question_te": "AP లో ఏప్రిల్ 2022 తర్వాత జిల్లాల సంఖ్య ఎన్ని?",
        "opt_a": "13",
        "opt_b": "23",
        "opt_c": "26",
        "opt_d": "28",
        "answer": "C",
        "explanation_te": "ఏప్రిల్ 4, 2022న AP లో 13 జిల్లాలు 26 జిల్లాలుగా పునర్వ్యవస్థీకరించారు (YSRCP ప్రభుత్వం). తర్వాత జనవరి 1, 2026న మరో 2 జోడించి 28 జిల్లాలు చేశారు."
    },
    {
        "section_idx": 7,
        "difficulty": "medium",
        "question_te": "జనవరి 1, 2026న AP లో ఏ కొత్త జిల్లాలు ఏర్పడ్డాయి?",
        "opt_a": "పోలవరం + ఏలూరు",
        "opt_b": "పోలవరం + మార్కాపురం",
        "opt_c": "ఏలూరు + నంద్యాల",
        "opt_d": "శ్రీ సత్యసాయి + పార్వతీపురం",
        "answer": "B",
        "explanation_te": "జనవరి 1, 2026న AP లో పోలవరం మరియు మార్కాపురం రెండు కొత్త జిల్లాలు ఏర్పడ్డాయి — మొత్తం 28 జిల్లాలు అయ్యాయి (TDP ప్రభుత్వం)."
    },
    {
        "section_idx": 7,
        "difficulty": "medium",
        "question_te": "AP అసెంబ్లీలో మొత్తం స్థానాల సంఖ్య ఎన్ని?",
        "opt_a": "119",
        "opt_b": "147",
        "opt_c": "175",
        "opt_d": "196",
        "answer": "C",
        "explanation_te": "AP శాసనసభలో మొత్తం 175 స్థానాలు. లోక్‌సభలో 25 స్థానాలు (2026 delimitation వరకు), రాజ్యసభలో 11 స్థానాలు."
    },
    # Section 1 — 2025 Padma Awards
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "Nandamuri Balakrishna కి 2025లో ఏ పద్మ పురస్కారం వచ్చింది?",
        "opt_a": "పద్మ శ్రీ",
        "opt_b": "పద్మ భూషణ్",
        "opt_c": "పద్మ విభూషణ్",
        "opt_d": "భారత రత్న",
        "answer": "B",
        "explanation_te": "Nandamuri Balakrishna కి 2025లో పద్మ భూషణ్ (Art రంగంలో) వచ్చింది. ఆయన NTR గారి పుత్రుడు; 100+ తెలుగు చిత్రాల్లో నటించారు. ఆంధ్రప్రదేశ్ నుండి."
    },
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "2025లో పద్మ విభూషణ్ పొందిన తెలంగాణ వైద్య నిపుణుడు ఎవరు?",
        "opt_a": "Dr. Duvvur Nageshwar Reddy",
        "opt_b": "Dr. Guduru Venkat Rao",
        "opt_c": "Dr. Nori Dattatreyudu",
        "opt_d": "Dr. Palkonda Vijay Anand Reddy",
        "answer": "A",
        "explanation_te": "Dr. Duvvur Nageshwar Reddy కి 2025లో పద్మ విభూషణ్ (Medicine) వచ్చింది — తెలంగాణ నుండి. ఆయన Asian Institute of Gastroenterology వ్యవస్థాపకుడు; ప్రముఖ గ్యాస్ట్రోఎంటెరాలజిస్ట్."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "2025 Padma Shri — Public Affairs రంగంలో తెలంగాణ నుండి ఎవరికి వచ్చింది?",
        "opt_a": "Kethavath Somlal",
        "opt_b": "Manda Krishna Madiga",
        "opt_c": "Kurella Vittalacharya",
        "opt_d": "Dasari Kondappa",
        "answer": "B",
        "explanation_te": "Manda Krishna Madiga కి 2025 Padma Shri (Public Affairs) వచ్చింది. ఆయన Madiga Reservation Porata Samithi వ్యవస్థాపకుడు; SC వర్గీకరణ ఉద్యమ నేత. తెలంగాణ నుండి."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "2025 Padma Awards లో తెలుగు రాష్ట్రాల నుండి మొత్తం ఎంత మంది గ్రహీతలు ఉన్నారు?",
        "opt_a": "5",
        "opt_b": "6",
        "opt_c": "7",
        "opt_d": "9",
        "answer": "C",
        "explanation_te": "2025 Padma Awards: AP నుండి 5 (Balakrishna-PB, Madugula-PS, KL Krishna-PS, Miriyala-PS posthumous, Vadiraj-PS) + Telangana నుండి 2 (Nageshwar Reddy-PV, Manda Krishna Madiga-PS) = మొత్తం 7 మంది."
    },
    {
        "section_idx": 1,
        "difficulty": "hard",
        "question_te": "2025 Padma Shri — Burrakatha కళాకారుడు మరణానంతరం పురస్కారం పొందినవారు ఎవరు?",
        "opt_a": "Madugula Nagaphani Sarma",
        "opt_b": "Vadiraj Panchamukhi",
        "opt_c": "Miriyala Apparao",
        "opt_d": "K.L. Krishna",
        "answer": "C",
        "explanation_te": "Miriyala Apparao (తాడేపల్లిగూడెం) కి 2025 Padma Shri మరణానంతరం ఇచ్చారు — Art (Burrakatha) రంగంలో; 5 దశాబ్దాల బుర్రకథ సేవకు గుర్తింపు. Andhra Pradesh నుండి."
    },

    # Section 1 — 2026 Padma Awards (inserted as additional section 1 MCQs)
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "2026 Padma Awards లో తెలుగు రాష్ట్రాల నుండి మొత్తం ఎంత మంది గ్రహీతలు ఉన్నారు?",
        "opt_a": "7",
        "opt_b": "9",
        "opt_c": "11",
        "opt_d": "12",
        "answer": "D",
        "explanation_te": "2026 Padma Awards (జన. 25, 2026 ప్రకటన): AP నుండి 4 Padma Shri + Telangana నుండి 7 Padma Shri + USA (తెలుగు) నుండి 1 Padma Bhushan = మొత్తం 12 మంది. Telangana: Chandramouli Gaddamanugu, Deepika Reddy, Guduru Venkat Rao, Krishnamurty Balasubramanian, Kumarasamy Thangaraj, Palkonda Vijay Anand Reddy, Rama Reddy Mamidi."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "2026 Padma Bhushan పొందిన తెలుగు వైద్యుడు ఎవరు?",
        "opt_a": "Dr. Guduru Venkat Rao",
        "opt_b": "Dr. Nori Dattatreyudu",
        "opt_c": "Dr. Palkonda Vijay Anand Reddy",
        "opt_d": "Dr. Kumarasamy Thangaraj",
        "answer": "B",
        "explanation_te": "Dr. Nori Dattatreyudu కి 2026లో Padma Bhushan ఇచ్చారు — Medicine రంగంలో. ఆయన USA లో ఉంటున్న తెలుగు వైద్యుడు. మిగిలిన ముగ్గురు Padma Shri గ్రహీతలు."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "2026 లో Literature & Education రంగంలో AP కి Padma Shri వచ్చిన వ్యక్తి ఎవరు?",
        "opt_a": "Shri Maganti Murali Mohan",
        "opt_b": "Shri Gadde Babu Rajendra Prasad",
        "opt_c": "Shri Vempaty Kutumba Sastry",
        "opt_d": "Shri Garimella Balakrishna Prasad",
        "answer": "C",
        "explanation_te": "Shri Vempaty Kutumba Sastry కి 2026లో Literature & Education రంగంలో Padma Shri వచ్చింది — Andhra Pradesh నుండి. Gadde Babu, Garimella, Maganti — ముగ్గురికీ Art రంగంలో Padma Shri."
    },
    {
        "section_idx": 1,
        "difficulty": "hard",
        "question_te": "2026 లో AP నుండి Padma Shri మరణానంతరం (Posthumous) పొందిన వ్యక్తి ఎవరు?",
        "opt_a": "Shri Maganti Murali Mohan",
        "opt_b": "Shri Vempaty Kutumba Sastry",
        "opt_c": "Shri Garimella Balakrishna Prasad",
        "opt_d": "Shri Gadde Babu Rajendra Prasad",
        "answer": "C",
        "explanation_te": "Shri Garimella Balakrishna Prasad కి 2026లో Padma Shri మరణానంతరం (Posthumously) ఇచ్చారు — Art రంగంలో, Andhra Pradesh నుండి. Telangana నుండి Rama Reddy Mamidi కి కూడా Posthumous Padma Shri (Animal Husbandry)."
    },
    {
        "section_idx": 1,
        "difficulty": "hard",
        "question_te": "2026 Padma Shri లో Telangana నుండి Animal Husbandry రంగంలో ఎవరు పురస్కారం పొందారు?",
        "opt_a": "Shri Chandramouli Gaddamanugu",
        "opt_b": "Shri Kumarasamy Thangaraj",
        "opt_c": "Shri Guduru Venkat Rao",
        "opt_d": "Shri Rama Reddy Mamidi",
        "answer": "D",
        "explanation_te": "Shri Rama Reddy Mamidi కి 2026 Padma Shri Animal Husbandry (పాడి పరిశ్రమ) రంగంలో మరణానంతరం ఇచ్చారు — Telangana నుండి. Kumarasamy Thangaraj మరియు Krishnamurty Balasubramanian — Science & Engineering రంగంలో Telangana నుండి Padma Shri."
    },

    # Section 5 — AP HC Chief Justice (additional)
    {
        "section_idx": 5,
        "difficulty": "easy",
        "question_te": "AP హైకోర్టు చరిత్రలో తొలి మహిళా ప్రధాన న్యాయమూర్తి ఎవరు?",
        "opt_a": "Justice B.V. Nagarathna",
        "opt_b": "Justice Hima Kohli",
        "opt_c": "Justice Lisa Gill",
        "opt_d": "Justice Indira Banerjee",
        "answer": "C",
        "explanation_te": "Justice Lisa Gill AP హైకోర్టు 6వ ప్రధాన న్యాయమూర్తి — ఏప్రిల్ 25, 2026 నుండి పదవిలో. AP HC చరిత్రలో తొలి మహిళా CJ. Punjab & Haryana HC నుండి బదిలీ అయ్యారు."
    },
    {
        "section_idx": 5,
        "difficulty": "medium",
        "question_te": "Justice Lisa Gill AP HC CJ గా ఏ తేదీన పదవి స్వీకరించారు?",
        "opt_a": "జనవరి 1, 2026",
        "opt_b": "మార్చి 1, 2026",
        "opt_c": "ఏప్రిల్ 25, 2026",
        "opt_d": "జూన్ 2, 2026",
        "answer": "C",
        "explanation_te": "Justice Dhiraj Singh Thakur (5వ CJ) ఏప్రిల్ 24, 2026న పదవీ విరమణ చేశారు. Justice Lisa Gill ఏప్రిల్ 25, 2026 నుండి AP HC 6వ CJ గా పదవి స్వీకరించారు. SC కొలీజియం సిఫారసు మేరకు నియమించారు."
    },
    {
        "section_idx": 5,
        "difficulty": "medium",
        "question_te": "Justice Lisa Gill AP HC కి రాకముందు ఏ హైకోర్టులో పనిచేశారు?",
        "opt_a": "Delhi HC",
        "opt_b": "Bombay HC",
        "opt_c": "Punjab & Haryana HC",
        "opt_d": "Madras HC",
        "answer": "C",
        "explanation_te": "Justice Lisa Gill Punjab & Haryana High Court నుండి AP HC కి బదిలీ అయ్యారు. మార్చి 2026లో AP HC న్యాయమూర్తిగా ప్రమాణస్వీకారం చేసి, ఏప్రిల్ 25, 2026న CJ పదవి చేపట్టారు."
    },
    {
        "section_idx": 5,
        "difficulty": "hard",
        "question_te": "AP HC 5వ ప్రధాన న్యాయమూర్తి (Justice Dhiraj Singh Thakur) ఏ తేదీన పదవీ విరమణ చేశారు?",
        "opt_a": "జనవరి 24, 2026",
        "opt_b": "మార్చి 24, 2026",
        "opt_c": "ఏప్రిల్ 24, 2026",
        "opt_d": "మే 24, 2026",
        "answer": "C",
        "explanation_te": "Justice Dhiraj Singh Thakur జులై 28, 2023న AP HC 5వ CJ గా పదవి స్వీకరించి ఏప్రిల్ 24, 2026న పదవీ విరమణ చేశారు. ఆ తర్వాత రోజు Justice Lisa Gill 6వ CJ గా బాధ్యతలు స్వీకరించారు."
    },

    # Section 8 — Rapid revision
    {
        "section_idx": 8,
        "difficulty": "hard",
        "question_te": "APRA 2014 ప్రకారం AP కి ఏ హామీ ఇచ్చారు?",
        "opt_a": "భారత రత్న",
        "opt_b": "హైదరాబాద్ రాజధానిగా ఉంచడం",
        "opt_c": "పోలవరం జాతీయ ప్రాజెక్టు హోదా + నష్ట పరిహారం + రాజ్యసభ స్థానాలు",
        "opt_d": "వేర్వేరు శాసనసభ ఎన్నికలు",
        "answer": "C",
        "explanation_te": "APRA 2014 ముఖ్య హామీలు: పోలవరం జాతీయ ప్రాజెక్టు హోదా; రాయలసీమ, ఉత్తరాంధ్ర నష్ట పరిహారం; AP పారిశ్రామిక ప్రోత్సాహాలు; రాజ్యసభ స్థానాల పెంపు హామీ."
    },
    {
        "section_idx": 8,
        "difficulty": "hard",
        "question_te": "SP బాలసుబ్రహ్మణ్యం ఏ జిల్లాకు చెందినవారు?",
        "opt_a": "కృష్ణా జిల్లా",
        "opt_b": "నెల్లూరు జిల్లా",
        "opt_c": "గుంటూరు జిల్లా",
        "opt_d": "చిత్తూరు జిల్లా",
        "answer": "B",
        "explanation_te": "SP బాలసుబ్రహ్మణ్యం (సిపిళ్ళ పార్వతీశ్వర బాలసుబ్రహ్మణ్యం) నెల్లూరు జిల్లాలో జన్మించారు. 40,000+ పాటలు 16 భాషల్లో పాడారు. 2021 పద్మ విభూషణ్ (మరణానంతరం)."
    },
]


def _seed_ap_ca_div9_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed study notes for AP CA Division 9."""
    ph = '%s' if USE_POSTGRES else '?'
    try:
        conn.execute("""CREATE TABLE IF NOT EXISTS study_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT, subject TEXT NOT NULL DEFAULT 'GK',
            topic TEXT NOT NULL DEFAULT 'AP_Current_Affairs', subtopic TEXT DEFAULT '',
            chapter_num INTEGER NOT NULL, chapter_title_te TEXT NOT NULL DEFAULT '',
            chapter_title_en TEXT NOT NULL DEFAULT '', pages_ref TEXT DEFAULT '',
            sections_json TEXT NOT NULL DEFAULT '[]', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")
        if USE_POSTGRES: conn.commit()
    except Exception: pass
    import json as _json
    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (9, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if row and not force: return {'success': True, 'already_exists': True}
    if row and force:
        note_id = row_to_dict(row)['id']
        db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
        db_exec(conn, f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (9, 'AP_Current_Affairs'))
        if USE_POSTGRES: conn.commit()
    db_exec(conn,
        f"INSERT INTO study_notes (subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'AP_Current_Affairs', 'Division9', 9,
         'పద్మ పురస్కారాలు, కేంద్ర సంస్థలు, AP హైకోర్టు & రాజ్యాంగం',
         'Padma Awards, Central Institutions, AP HC & Constitution',
         '', _json.dumps(SECTIONS_JSON, ensure_ascii=False)))
    if USE_POSTGRES: conn.commit()
    return {'success': True, 'message': 'AP CA Div9 notes seeded!'}
def _seed_ap_ca_div9_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed MCQs for AP CA chapter 9."""
    ph = '%s' if USE_POSTGRES else '?'
    cur = db_exec(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (9, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if not row:
        _seed_ap_ca_div9_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        cur = db_exec(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (9, 'AP_Current_Affairs'))
        row = cur.fetchone()
    if not row:
        print(f"[div9-mcqs] study_note not found — skipping")
        return
    note_id = row_to_dict(row)['id']
    cur2 = db_exec(conn, f"SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    count = list(cur2.fetchone())[0]
    if count > 0 and not force:
        return
    db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    insert_sql = (
        f"INSERT INTO chapter_mcqs "
        f"(study_note_id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    )
    diff_map = {'easy': 1, 'medium': 2, 'hard': 3, 1: 1, 2: 2, 3: 3}
    for mcq in MCQ_DATA:
        diff = diff_map.get(mcq.get('difficulty', 'medium'), 2)
        q_te = mcq.get('question_te', mcq.get('question_te', ''))
        db_exec(conn, insert_sql, (
            note_id,
            mcq['section_idx'],
            diff,
            q_te,
            mcq['opt_a'], mcq['opt_b'], mcq['opt_c'], mcq['opt_d'],
            str(mcq['answer']).lower(),
            mcq['explanation_te']
        ))
    if USE_POSTGRES:
        conn.commit()
    return {'success': True, 'message': f'AP CA Div9 MCQs seeded! Total: {len(MCQ_DATA)}'}

# Additional MCQs for div9 appended
_EXTRA_MCQ_DATA = [
    # Padma Awards additional
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "2025 పద్మ విభూషణ్ పొందిన తెలుగు నటుడు ఎవరు?",
        "opt_a": "అల్లు అర్జున్",
        "opt_b": "మోహన్ బాబు",
        "opt_c": "బాలకృష్ణ (నందమూరి బాలకృష్ణ)",
        "opt_d": "చిరంజీవి",
        "answer": "C",
        "explanation_te": "2025లో నందమూరి బాలకృష్ణ పద్మ విభూషణ్ పురస్కారం పొందారు. ఇది తెలుగు సినిమాకు గొప్ప గౌరవం."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "SP బాలసుబ్రహ్మణ్యం ఏ సంవత్సరం పద్మ విభూషణ్ పొందారు?",
        "opt_a": "2019",
        "opt_b": "2020",
        "opt_c": "2021",
        "opt_d": "2022",
        "answer": "C",
        "explanation_te": "2021లో SP బాలసుబ్రహ్మణ్యం పద్మ విభూషణ్ పొందారు (మరణానంతర పురస్కారం). 2020 సెప్టెంబర్‌లో ఆయన COVID-19 తో మరణించారు."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "K. విశ్వనాథ్ దాదాసాహేబ్ ఫాల్కే పురస్కారం ఏ సంవత్సరం పొందారు?",
        "opt_a": "2014",
        "opt_b": "2016",
        "opt_c": "2018",
        "opt_d": "2020",
        "answer": "B",
        "explanation_te": "K. విశ్వనాథ్ 2016లో (67వ Dadasaheb Phalke Award) దాదాసాహేబ్ ఫాల్కే పురస్కారం పొందారు. ఆయన తెలుగు సినిమా దర్శకుడు."
    },
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "పద్మ పురస్కారాలు ఏ తేదీన ప్రకటిస్తారు?",
        "opt_a": "స్వాతంత్ర్య దినం (ఆగస్టు 15)",
        "opt_b": "గణతంత్ర దినం (జనవరి 26)",
        "opt_c": "హోలీ",
        "opt_d": "క్రిస్మస్",
        "answer": "B",
        "explanation_te": "పద్మ పురస్కారాలు ప్రతి సంవత్సరం గణతంత్ర దినోత్సవం (జనవరి 26) సందర్భంగా ప్రకటిస్తారు. పురస్కారాలు మార్చి/ఏప్రిల్ లో రాష్ట్రపతి భవన్‌లో ప్రదానం జరుగుతుంది."
    },
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "2023 ఆస్కార్ అవార్డు గెలిచిన తెలుగు పాట ఏది?",
        "opt_a": "జై హో",
        "opt_b": "నాటు నాటు (RRR)",
        "opt_c": "బాహుబలి థీమ్",
        "opt_d": "ఆర్యా",
        "answer": "B",
        "explanation_te": "RRR చిత్రంలోని 'నాటు నాటు' పాట 2023 ఆస్కార్ (95వ అకాడమీ అవార్డుల) లో Best Original Song విభాగంలో గెలిచింది. MM కీరవాణి సంగీతం."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "69వ జాతీయ చలనచిత్ర పురస్కారాల్లో Best Actor ఎవరు?",
        "opt_a": "రామ్ చరణ్ (RRR)",
        "opt_b": "అల్లు అర్జున్ (పుష్ప-ది రైజ్)",
        "opt_c": "NTR Jr (RRR)",
        "opt_d": "మహేష్ బాబు",
        "answer": "B",
        "explanation_te": "అల్లు అర్జున్ 69వ జాతీయ చలనచిత్ర పురస్కారాల్లో (Pushpa: The Rise చిత్రానికి) Best Actor పురస్కారం పొందారు — తొలి తెలుగు నటుడు ఈ అవార్డు గెలిచిన వారు."
    },
    {
        "section_idx": 3,
        "difficulty": "easy",
        "question_te": "విశ్వనాధ సత్యనారాయణ జ్ఞానపీఠ్ పురస్కారం ఏ సంవత్సరం పొందారు?",
        "opt_a": "1960",
        "opt_b": "1970",
        "opt_c": "1980",
        "opt_d": "1990",
        "answer": "B",
        "explanation_te": "విశ్వనాధ సత్యనారాయణ 'రామాయణ కల్పవృక్షం' రచనకు 1970లో జ్ఞానపీఠ్ పురస్కారం పొందారు. ఇది మొదటి తెలుగు జ్ఞానపీఠ్."
    },
    {
        "section_idx": 3,
        "difficulty": "medium",
        "question_te": "సి నారాయణ రెడ్డి (సినారె) జ్ఞానపీఠ్ పురస్కారం ఏ సంవత్సరం పొందారు?",
        "opt_a": "1982",
        "opt_b": "1988",
        "opt_c": "1992",
        "opt_d": "1998",
        "answer": "B",
        "explanation_te": "సి నారాయణ రెడ్డి (Sinaree) 1988లో జ్ఞానపీఠ్ పురస్కారం పొందారు. తెలుగులో రెండవ జ్ఞానపీఠ్ గ్రహీత."
    },
    {
        "section_idx": 4,
        "difficulty": "easy",
        "question_te": "IIT తిరుపతి ఏ సంవత్సరంలో స్థాపించబడింది?",
        "opt_a": "2014",
        "opt_b": "2015",
        "opt_c": "2018",
        "opt_d": "2020",
        "answer": "B",
        "explanation_te": "IIT తిరుపతి 2015లో AP Reorganisation Act 2014 ప్రకారం AP కి ఒక IIT మంజూరు అయి స్థాపించబడింది."
    },
    {
        "section_idx": 4,
        "difficulty": "medium",
        "question_te": "AIIMS మంగళగిరి ఎక్కడ ఉంది?",
        "opt_a": "విశాఖపట్నం",
        "opt_b": "మంగళగిరి (గుంటూరు జిల్లా)",
        "opt_c": "తిరుపతి",
        "opt_d": "కాకినాడ",
        "answer": "B",
        "explanation_te": "AIIMS మంగళగిరి గుంటూరు జిల్లాలో మంగళగిరిలో ఉంది. AP కి APRA 2014 ప్రకారం AIIMS మంజూరైంది, 2022లో సర్వీసులు ప్రారంభించింది."
    },
    {
        "section_idx": 5,
        "difficulty": "easy",
        "question_te": "AP High Court (ప్రత్యేక) ఎప్పుడు ప్రారంభమైంది?",
        "opt_a": "2016 జనవరి 1",
        "opt_b": "2019 జనవరి 1",
        "opt_c": "2014 జూన్ 2",
        "opt_d": "2017 నవంబర్ 1",
        "answer": "B",
        "explanation_te": "AP High Court అమరావతిలో జనవరి 1, 2019న ప్రత్యేకంగా ఏర్పాటైంది. APRA 2014 సెక్షన్ 30 ప్రకారం ఏర్పాటైంది."
    },
    {
        "section_idx": 5,
        "difficulty": "medium",
        "question_te": "AP High Court తొలి మహిళా Chief Justice ఎవరు?",
        "opt_a": "జస్టిస్ ప్రభా శ్రీదేవన్",
        "opt_b": "జస్టిస్ లీసా గిల్ (Lisa Gill)",
        "opt_c": "జస్టిస్ హిమా కోహ్లి",
        "opt_d": "జస్టిస్ బి.వి. నాగరత్న",
        "answer": "B",
        "explanation_te": "జస్టిస్ లీసా గిల్ ఏప్రిల్ 25, 2026న AP High Court తొలి మహిళా Chief Justice గా నియమితులయ్యారు."
    },
    {
        "section_idx": 6,
        "difficulty": "easy",
        "question_te": "ఆర్టికల్ 371-D ఏ రాష్ట్రానికి సంబంధించినది?",
        "opt_a": "తెలంగాణ",
        "opt_b": "ఆంధ్రప్రదేశ్",
        "opt_c": "కర్ణాటక",
        "opt_d": "ఒడిశా",
        "answer": "B",
        "explanation_te": "ఆర్టికల్ 371-D ఆంధ్రప్రదేశ్‌కి సంబంధించినది. ఇది 32వ రాజ్యాంగ సవరణ 1973 ద్వారా చేర్చబడింది. విద్య, ఉద్యోగాలలో స్థానిక పౌరులకు రక్షణ కల్పిస్తుంది."
    },
    {
        "section_idx": 6,
        "difficulty": "medium",
        "question_te": "ఆర్టికల్ 371-D ఏ రాజ్యాంగ సవరణ ద్వారా జోడించబడింది?",
        "opt_a": "28వ సవరణ 1972",
        "opt_b": "32వ సవరణ 1973",
        "opt_c": "42వ సవరణ 1976",
        "opt_d": "100వ సవరణ 2015",
        "answer": "B",
        "explanation_te": "ఆర్టికల్ 371-D 32వ రాజ్యాంగ సవరణ 1973 ద్వారా AP కి ప్రత్యేక రక్షణ కోసం జోడించబడింది. G.O.610 తర్వాత 6 Zones విద్య, ఉద్యోగాలలో రోస్టర్ సిస్టమ్ అమలు చేయడానికి."
    },
    {
        "section_idx": 7,
        "difficulty": "easy",
        "question_te": "ప్రస్తుత AP గవర్నర్ ఎవరు?",
        "opt_a": "జస్టిస్ S. అబ్దుల్ నజీర్",
        "opt_b": "బిస్వభూషణ్ హరిచందన్",
        "opt_c": "నవంబర్ నయనా పటేల్",
        "opt_d": "ఇ.ఎస్.ఎల్ నరసిమ్హన్",
        "answer": "A",
        "explanation_te": "జస్టిస్ S. అబ్దుల్ నజీర్ ప్రస్తుత AP గవర్నర్. ఆయన సుప్రీంకోర్టు మాజీ న్యాయమూర్తి, 2023 జనవరిలో నియమితులయ్యారు."
    },
    {
        "section_idx": 7,
        "difficulty": "easy",
        "question_te": "AP లో మొత్తం శాసనసభ స్థానాలు ఎన్ని?",
        "opt_a": "119",
        "opt_b": "175",
        "opt_c": "150",
        "opt_d": "294",
        "answer": "B",
        "explanation_te": "AP లో మొత్తం 175 శాసనసభ (Assembly) స్థానాలు ఉన్నాయి. 25 లోక్‌సభ మరియు 11 రాజ్యసభ స్థానాలు ఉన్నాయి."
    },
    {
        "section_idx": 7,
        "difficulty": "medium",
        "question_te": "AP లో ప్రస్తుత జిల్లాల సంఖ్య (2026 జనవరి నాటికి)?",
        "opt_a": "13",
        "opt_b": "25",
        "opt_c": "26",
        "opt_d": "28",
        "answer": "D",
        "explanation_te": "జనవరి 1, 2026 నుండి AP లో మొత్తం 28 జిల్లాలు ఉన్నాయి. 2022 ఏప్రిల్‌లో 13→26 చేసి, తర్వాత 2 మరిన్ని జిల్లాలు జోడించడంతో 28 అయ్యాయి."
    },
    {
        "section_idx": 8,
        "difficulty": "easy",
        "question_te": "AP లో ప్రస్తుత ముఖ్యమంత్రి ఎవరు?",
        "opt_a": "వై.ఎస్. జగన్ మోహన్ రెడ్డి",
        "opt_b": "చంద్రబాబు నాయుడు (నారా చంద్రబాబు నాయుడు)",
        "opt_c": "కె. కేశవ్ రావు",
        "opt_d": "పవన్ కళ్యాణ్",
        "answer": "B",
        "explanation_te": "చంద్రబాబు నాయుడు జూన్ 12, 2024న AP ముఖ్యమంత్రిగా ప్రమాణ స్వీకారం చేశారు. TDP-BJP-JSP కూటమి 2024 ఎన్నికల్లో ఘన విజయం సాధించింది."
    },
    {
        "section_idx": 8,
        "difficulty": "medium",
        "question_te": "2026 AP Reorganisation Amendment Act ఏ తేదీన రాష్ట్రపతి ఆమోదం పొందింది?",
        "opt_a": "ఏప్రిల్ 1, 2026",
        "opt_b": "ఏప్రిల్ 2, 2026",
        "opt_c": "ఏప్రిల్ 6, 2026",
        "opt_d": "ఏప్రిల్ 13, 2026",
        "answer": "C",
        "explanation_te": "AP Reorganisation Amendment Act 2026 (Act No. 7/2026) రాష్ట్రపతి ఏప్రిల్ 6, 2026న ఆమోదించారు. ఇది అమరావతిని అధికారిక రాజధానిగా గుర్తించింది."
    },
    {
        "section_idx": 8,
        "difficulty": "hard",
        "question_te": "APRA 2014 ప్రకారం అమలులోకి వచ్చిన తేదీ నుండి అమరావతి రాజధాని Retrospective గా ఏ తేదీ నుండి వర్తిస్తుంది?",
        "opt_a": "జూన్ 2, 2014",
        "opt_b": "అక్టోబర్ 1, 2018",
        "opt_c": "జూన్ 2, 2024",
        "opt_d": "ఏప్రిల్ 6, 2026",
        "answer": "C",
        "explanation_te": "2026 సవరణ చట్టం జూన్ 2, 2024 నుండి (Retrospectively) అమరావతిని AP రాజధానిగా గుర్తించింది. ఇది 2024 ఎన్నికల తర్వాత TDP ప్రభుత్వం అమరావతి రాజధాని అవ్వాలని నిర్ణయించిన తేదీ."
    }
]

MCQ_DATA = MCQ_DATA + _EXTRA_MCQ_DATA
