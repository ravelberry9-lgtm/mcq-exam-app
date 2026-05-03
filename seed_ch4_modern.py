# -*- coding: utf-8 -*-
"""
seed_ch4_modern.py – Chapter 4: గవర్నర్ జనరళ్ళు మరియు వైస్రాయ్‌లు
(Governor Generals & Viceroys of India) — Modern Indian History
topic='Indian_History'  subtopic='Modern'  chapter_num=4
Sections: 8 (SEC 0–7)  |  MCQs: 64 (Easy~24, Medium~28, Hard~12)
"""

import json as _json

# ─────────────────────────────────────────────────────────────────────────────
# SECTIONS  (stored in study_notes.sections_json)
# ─────────────────────────────────────────────────────────────────────────────

CH4M_SECTIONS = [
    {
        "title": "గవర్నర్ జనరళ్ళు — బెంగాల్ (1757–1833)",
        "sub": "Clive · Warren Hastings · Cornwallis · Wellesley · Bentinck (Bengal)",
        "audio": ""
    },
    {
        "title": "వారెన్ హేస్టింగ్స్ & కార్న్‌వాలిస్ సంస్కరణలు",
        "sub": "Regulating Act 1773 · Pitt's India Act 1784 · Permanent Settlement 1793",
        "audio": ""
    },
    {
        "title": "వెల్లెస్లీ నుండి డల్హౌసీ వరకు (1798–1856)",
        "sub": "Subsidiary Alliance · Doctrine of Lapse · Railways · Telegraph",
        "audio": ""
    },
    {
        "title": "మొదటి వైస్రాయ్‌లు (1858–1876)",
        "sub": "Canning · Lawrence · Mayo · Lytton · Delhi Durbar 1877",
        "audio": ""
    },
    {
        "title": "రిప్పన్ నుండి కర్జన్ వరకు (1880–1905)",
        "sub": "Local Self-Govt · INC Founded · Partition of Bengal · ASI",
        "audio": ""
    },
    {
        "title": "మింటో II నుండి ఇర్విన్ వరకు (1905–1931)",
        "sub": "Morley-Minto Reforms · Montagu-Chelmsford · Rowlatt · Gandhi-Irwin Pact",
        "audio": ""
    },
    {
        "title": "విల్లింగ్డన్ నుండి మౌంట్‌బాటన్ వరకు (1931–1947)",
        "sub": "GOI Act 1935 · Cripps Mission · Quit India · Cabinet Mission · Partition",
        "audio": ""
    },
    {
        "title": "త్వరిత పునశ్చరణ — Key Facts",
        "sub": "Firsts · Lasts · Match the GG/Viceroy · Important Events",
        "audio": ""
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# MCQ DATA  — (sec_idx, difficulty, q, a, b, c, d, correct, explanation)
# difficulty: 1=easy, 2=medium, 3=hard
# ─────────────────────────────────────────────────────────────────────────────

CH4M_MCQS = [

    # ── SEC 0: Governor Generals of Bengal ────────────────────────────────────

    (0, 1,
     "బెంగాల్ యొక్క మొదటి గవర్నర్ జనరల్ ఎవరు? / Who was the first Governor General of Bengal?",
     "Lord Cornwallis", "Warren Hastings", "Lord Wellesley", "Lord Dalhousie", "b",
     "Warren Hastings (1772–1785) was the first Governor General of Bengal. He was appointed under the Regulating Act of 1773. / వారెన్ హేస్టింగ్స్ బెంగాల్ యొక్క మొదటి గవర్నర్ జనరల్ (1772–1785), Regulating Act 1773 ద్వారా నియమితులయ్యారు."),

    (0, 1,
     "Regulating Act 1773 ద్వారా ఏ పదవి సృష్టించబడింది? / Which office was created by the Regulating Act 1773?",
     "Viceroy of India", "Secretary of State for India", "Governor General of Bengal", "President of Board of Control", "c",
     "The Regulating Act of 1773 created the office of Governor General of Bengal. Warren Hastings became the first holder of this office. / Regulating Act 1773 'Governor General of Bengal' పదవిని సృష్టించింది. మొదటి గవర్నర్ జనరల్ = Warren Hastings."),

    (0, 2,
     "Pitt's India Act 1784 యొక్క ముఖ్య లక్షణం ఏమిటి? / What was the key feature of Pitt's India Act 1784?",
     "Created Governor General of India post", "Established Board of Control — dual control of Crown and Company", "Abolished EIC", "Introduced Permanent Settlement", "b",
     "Pitt's India Act 1784 established a 'Board of Control' in London, creating a system of dual control — the British Crown (through Board of Control) and the EIC (Court of Directors). / Pitt's India Act 1784: Board of Control సృష్టి — Crown + EIC ద్వంద్వ నియంత్రణ."),

    (0, 2,
     "Lord Cornwallis (1786–1793) యొక్క అతి ముఖ్యమైన సంస్కరణ ఏది? / What was Lord Cornwallis's most important reform?",
     "Subsidiary Alliance", "Permanent Settlement (Zamindari System) 1793", "Doctrine of Lapse", "Abolition of Sati", "b",
     "Lord Cornwallis introduced the Permanent Settlement in 1793 — fixing land revenue permanently with zamindars in Bengal, Bihar and Orissa. He also introduced the Cornwallis Code. / Lord Cornwallis: Permanent Settlement 1793 (జమీందారీ వ్యవస్థ), Cornwallis Code."),

    (0, 2,
     "సహాయక సైన్య విధానం (Subsidiary Alliance) ఎవరు ప్రవేశపెట్టారు? / Who introduced the Subsidiary Alliance policy?",
     "Warren Hastings", "Lord Cornwallis", "Lord Wellesley", "Lord Dalhousie", "c",
     "Lord Wellesley (1798–1805) introduced the Subsidiary Alliance policy. Under this, Indian rulers had to maintain a British subsidiary force and pay for it, losing their right to have independent armies or foreign relations. / Subsidiary Alliance = Lord Wellesley (1798–1805). స్వదేశీ రాజులు British సైన్యం ఖర్చు భరించాలి, స్వతంత్ర సైన్యం నిషేధం."),

    (0, 3,
     "Lord Wellesley తన విస్తరణ విధానాన్ని describe చేయడానికి ఏ సిద్ధాంతాలు ఉపయోగించారు? / Which two doctrines did Lord Wellesley use for expansion?",
     "Subsidiary Alliance only", "Doctrine of Lapse and Subsidiary Alliance", "Subsidiary Alliance and Outright Annexation", "Permanent Settlement and Subsidiary Alliance", "c",
     "Lord Wellesley used two main tools: (1) Subsidiary Alliance — Indian rulers accept British forces; (2) Outright annexation by war (e.g., defeating Tipu Sultan 1799, annexing Mysore). He did NOT use Doctrine of Lapse — that was Dalhousie. / Wellesley: Subsidiary Alliance + Outright annexation. Doctrine of Lapse = Dalhousie."),

    (0, 1,
     "Lord William Bentinck (1828–1835) ఏ సామాజిక సంస్కరణకు ప్రసిద్ధులు? / For which social reform is Lord William Bentinck famous?",
     "Permanent Settlement", "Abolition of Sati (Sati Prohibition Regulation, 1829)", "Subsidiary Alliance", "Doctrine of Lapse", "b",
     "Lord William Bentinck (1828–1835) is most famous for abolishing Sati (Sati Prohibition Regulation, 1829) with help from Raja Ram Mohan Roy. He also suppressed Thuggee and introduced English education policy (Macaulay's Minutes 1835). / Bentinck: Sati నిర్మూలన 1829, Thuggee అణచివేత, English education."),

    (0, 2,
     "Lord Dalhousie (1848–1856) యొక్క 'Doctrine of Lapse' అంటే ఏమిటి? / What is Lord Dalhousie's 'Doctrine of Lapse'?",
     "Land revenue settlement policy", "If an Indian ruler dies without a natural male heir, his state is annexed by British India", "Subsidiary Alliance improvement", "Rights of zamindars", "b",
     "Doctrine of Lapse (Dalhousie, 1848–1856): If an Indian ruler dies without a natural male heir (adopted heirs not accepted), the state lapses to British India. States annexed: Satara (1848), Jaipur, Sambalpur, Baghat, Udaipur, Jhansi, Nagpur. / Doctrine of Lapse = పుత్రసంతానం లేని రాజు రాజ్యం British కి చేరుతుంది."),

    # ── SEC 1: Warren Hastings & Cornwallis Reforms ────────────────────────────

    (1, 1,
     "Warren Hastings పదవీ కాలం ఎప్పటి నుండి ఎప్పటి వరకు? / What was Warren Hastings's tenure?",
     "1765–1772", "1772–1785", "1786–1793", "1798–1805", "b",
     "Warren Hastings served as the first Governor General of Bengal from 1772 to 1785. He was impeached by the British Parliament but acquitted after a 7-year trial. / Warren Hastings: 1772–1785. Parliament impeachment process లో acquitted అయ్యారు."),

    (1, 2,
     "Warren Hastings time లో ప్రవేశపెట్టబడిన Dual Government system రద్దు ఎప్పుడు? / When was the Dual Government system abolished under Warren Hastings?",
     "1765", "1772 — Dual Govt abolished, direct administration started", "1784", "1793", "b",
     "The Dual Government System (introduced by Clive in 1765) — where EIC had Diwani rights but Nawab managed nizamat — was abolished by Warren Hastings in 1772. He took direct administration. / Dual Government = Clive 1765. Warren Hastings 1772 లో రద్దు చేసి direct administration చేపట్టారు."),

    (1, 2,
     "Cornwallis Code (1793) ముఖ్య లక్షణం ఏమిటి? / What was the key feature of the Cornwallis Code (1793)?",
     "Allowed Indians to hold high posts", "Separated judiciary from executive; barred Indians from high positions", "Introduced railways", "Abolished zamindari", "b",
     "The Cornwallis Code (1793) introduced separation of powers (judiciary from executive/revenue), modernised civil administration, but barred Indians from all high civil, military and judicial posts. / Cornwallis Code: judiciary-executive వేర్పాటు, Indians కి high posts నిషేధం."),

    (1, 1,
     "Cornwallis Code లో Indians కి high posts deny చేయడం వల్ల ఏ విమర్శ వచ్చింది? / What criticism arose from Cornwallis's denial of high posts to Indians?",
     "Indians were inefficient", "It was racially discriminatory — the 'Europeanisation of Indian Civil Service'", "Indians didn't want the posts", "It violated Company rules", "b",
     "Cornwallis barred Indians from high civil, military and judicial posts based on racial distrust. This has been called the 'Europeanisation of the Indian Civil Service' and was racially discriminatory. / Cornwallis: Indians ని high posts నుండి తొలగించడం = 'Europeanisation of Civil Service' — racial discrimination విమర్శ."),

    (1, 2,
     "Sir John Shore (1793–1798) యొక్క విధానం ఏమిటి? / What was Sir John Shore's policy?",
     "Active expansion through war", "Policy of Non-Intervention — avoided wars and alliances", "Introduced Subsidiary Alliance", "Introduced Permanent Settlement", "b",
     "Sir John Shore (1793–1798) followed a strict policy of Non-Intervention — he avoided wars and political alliances with Indian states. This was criticised as weakness by later governors. / Sir John Shore: Non-Intervention policy — యుద్ధాలు, రాజకీయ కూటమి నిరాకరించారు."),

    (1, 3,
     "Warren Hastings పై British Parliament లో impeachment process ఎవరు నడిపించారు? / Who led the impeachment process against Warren Hastings in the British Parliament?",
     "William Pitt", "Edmund Burke and Charles James Fox", "Lord Cornwallis", "Henry Dundas", "b",
     "Edmund Burke and Charles James Fox led the famous impeachment proceedings against Warren Hastings in the British Parliament, accusing him of corruption and arbitrary rule in India. The trial lasted 7 years (1788–1795) and Hastings was ultimately acquitted. / Hastings impeachment: Edmund Burke + Charles James Fox. 7 years trial (1788–1795), acquitted."),

    (1, 1,
     "Lord Cornwallis Permanent Settlement ఎక్కడ వర్తించింది? / Where did Lord Cornwallis's Permanent Settlement apply?",
     "Only Bengal", "Bengal, Bihar and Orissa", "All of British India", "Madras only", "b",
     "The Permanent Settlement of 1793 applied to Bengal, Bihar and Orissa. It fixed land revenue permanently with zamindars (landlords). / Permanent Settlement 1793: Bengal, Bihar, Orissa — zamindars తో revenue శాశ్వతంగా నిర్ధారించారు."),

    (1, 2,
     "Lord Minto I (1807–1813) పాలనలో జరిగిన ముఖ్య ఘటన ఏది? / What was a key event during Lord Minto I's tenure (1807–1813)?",
     "Permanent Settlement", "Treaty of Amritsar (1809) with Ranjit Singh — Punjab border fixed at Sutlej River", "Abolition of Sati", "First Anglo-Burmese War", "b",
     "Lord Minto I's most important achievement was the Treaty of Amritsar (1809) with Ranjit Singh of Punjab, which fixed the Sutlej River as the boundary between British India and Ranjit Singh's kingdom. / Lord Minto I: Treaty of Amritsar 1809 with Ranjit Singh — Sutlej River boundary."),

    # ── SEC 2: Wellesley to Dalhousie ──────────────────────────────────────────

    (2, 1,
     "భారతదేశంలో రైల్వేలు మరియు టెలిగ్రాఫ్ ఎవరి కాలంలో ప్రవేశపెట్టబడ్డాయి? / During whose tenure were railways and telegraph introduced in India?",
     "Lord Cornwallis", "Lord William Bentinck", "Lord Dalhousie", "Lord Canning", "c",
     "Lord Dalhousie (1848–1856) introduced railways (first railway: Bombay to Thane, 1853), electric telegraph, uniform postage (anna post), and Public Works Department. / Lord Dalhousie: Railways (first 1853, Bombay-Thane), Telegraph, Anna Post, PWD."),

    (2, 1,
     "భారతదేశంలో మొదటి రైల్వే ఎప్పుడు, ఏ మార్గంలో నడిచింది? / When and on which route did India's first railway run?",
     "1851 — Delhi to Agra", "1853 — Bombay (Bori Bunder) to Thane, 34 km", "1856 — Calcutta to Howrah", "1854 — Madras to Arcot", "b",
     "India's first passenger railway ran on April 16, 1853, from Bombay (Bori Bunder, now CST) to Thane — a distance of 34 km. This was during Lord Dalhousie's tenure. / మొదటి రైల్వే: April 16, 1853 — Bombay (Bori Bunder) నుండి Thane వరకు, 34 km. Lord Dalhousie కాలం."),

    (2, 2,
     "Lord Dalhousie Doctrine of Lapse ద్వారా annex చేసిన రాజ్యాల జాబితా ఏది? / Which states were annexed by Dalhousie using Doctrine of Lapse?",
     "Mysore, Hyderabad, Awadh", "Satara (1848), Jhansi (1854), Nagpur (1854)", "Bengal, Bihar, Orissa", "Punjab, Sindh, Kashmir", "b",
     "States annexed by Dalhousie's Doctrine of Lapse: Satara (1848), Jaitpur, Sambalpur (1849), Baghat (1850), Udaipur (1852), Jhansi (1854), Nagpur (1854). Awadh was annexed by a different reason (misgovernance) in 1856. / Doctrine of Lapse annexations: Satara 1848, Jhansi 1854, Nagpur 1854 — key ones."),

    (2, 2,
     "Lord William Bentinck's Macaulay Minute (1835) ఏ విధానానికి దారితీసింది? / What policy resulted from Macaulay's Minute (1835) under Bentinck?",
     "Religious conversion of Indians", "English as medium of higher education in India (replacing Sanskrit/Persian)", "Establishment of IITs", "Permanent Settlement extension", "b",
     "Macaulay's Minute (1835) under Bentinck recommended English as the medium of higher education in India, replacing Sanskrit and Persian. This led to the famous 'downward filtration theory' of education. / Macaulay's Minute 1835: English medium education — Sanskrit/Persian replace అయింది."),

    (2, 1,
     "Awadh (Oudh) ను ఎవరు, ఏ కారణంతో annex చేశారు? / Who annexed Awadh and on what ground?",
     "Lord Wellesley — Subsidiary Alliance", "Lord Dalhousie (1856) — Misgovernance / Doctrine of Lapse", "Lord Canning — after 1857 revolt", "Lord Cornwallis — Permanent Settlement", "b",
     "Lord Dalhousie annexed Awadh (Oudh) in 1856 on the grounds of misgovernance (not Doctrine of Lapse, as the Nawab had an heir). This was one of the major causes of the 1857 revolt — sepoys from Awadh felt betrayed. / Awadh annexation: Dalhousie 1856 — misgovernance. 1857 revolt కి ఒక ముఖ్య కారణం."),

    (2, 3,
     "Lord Hastings (1813–1823) / Lord Moira యొక్క ముఖ్య విజయాలు ఏవి? / What were Lord Hastings's (Lord Moira's) key achievements (1813–1823)?",
     "Subsidiary Alliance, Permanent Settlement", "Third Anglo-Maratha War victory (1817–19), Nepal War (1814–16), Press freedom for India", "Partition of Bengal, Doctrine of Lapse", "Abolition of Sati, English education", "b",
     "Lord Hastings (Lord Moira, 1813–1823): Won Third Anglo-Maratha War (1817–19) — broke Maratha power permanently. Won Anglo-Nepal War (1814–16) — Nepal ceded Garhwal, Kumaon (border at Sutlej, Mechi). Introduced press freedom. / Lord Hastings: Anglo-Maratha War III, Anglo-Nepal War, Press freedom."),

    (2, 2,
     "'Annexation by Conquest' విధానానికి Lord Dalhousie ఏ రాజ్యాలను annex చేశారు? / Which states did Dalhousie annex by conquest (not Doctrine of Lapse)?",
     "Satara and Jhansi", "Punjab (1849 after 2nd Anglo-Sikh War) and Berar (1853)", "Awadh and Nagpur", "Hyderabad and Mysore", "b",
     "Dalhousie annexed Punjab in 1849 after the Second Anglo-Sikh War (conquest) and Berar from the Nizam in 1853 (assignment/treaty). These were not by Doctrine of Lapse. / Dalhousie conquest annexations: Punjab 1849 (after 2nd Anglo-Sikh War), Berar 1853."),

    # ── SEC 3: First Viceroys (1858–1876) ────────────────────────────────────

    (3, 1,
     "భారతదేశ మొదటి వైస్రాయ్ ఎవరు? / Who was India's first Viceroy?",
     "Lord Dalhousie", "Lord Lawrence", "Lord Canning", "Lord Mayo", "c",
     "Lord Canning became India's first Viceroy after the Crown took over from the EIC following the 1857 revolt. He served from 1858 to 1862. / Lord Canning = మొదటి వైస్రాయ్ (1858–1862), 1857 revolt తర్వాత Crown ప్రత్యక్ష పాలన."),

    (3, 1,
     "Lord Canning కి 'Clemency Canning' అని పేరు ఎందుకు వచ్చింది? / Why was Lord Canning called 'Clemency Canning'?",
     "He was very strict", "He showed mercy to sepoys/rebels after 1857 revolt despite calls for harsh reprisals", "He introduced clemency in law", "He pardoned all criminals", "b",
     "After the 1857 revolt, many British demanded harsh reprisals against all rebels. Lord Canning opposed indiscriminate punishment and showed clemency to those who surrendered — earning the nickname 'Clemency Canning.' / 'Clemency Canning': 1857 తర్వాత rebels పై కఠిన శిక్ష వ్యతిరేకించి mercy చూపించారు."),

    (3, 2,
     "Indian Councils Act 1861 ఏ వైస్రాయ్ కాలంలో వచ్చింది? / During which Viceroy's tenure did the Indian Councils Act 1861 come?",
     "Lord Lawrence", "Lord Canning", "Lord Ripon", "Lord Mayo", "b",
     "Indian Councils Act 1861 came during Lord Canning's tenure. It introduced the portfolio system (ministerial responsibility), enlarged Legislative Councils, and restored some legislative powers to Bombay and Madras. / Indian Councils Act 1861: Lord Canning కాలంలో — portfolio system, enlarged Legislative Councils."),

    (3, 2,
     "Lord Mayo (1869–1872) గురించి ముఖ్యమైన వాస్తవం ఏమిటి? / What is the important fact about Lord Mayo (1869–1872)?",
     "He introduced railways", "He was assassinated in the Andaman Islands by a convict — first Viceroy to be murdered in India", "He introduced Permanent Settlement", "He passed GOI Act 1858", "b",
     "Lord Mayo (1869–1872) was assassinated on February 8, 1872, in the Andaman Islands by a convict named Sher Ali — making him the only Viceroy to be murdered in India. He also conducted India's first census in 1871. / Lord Mayo: Andaman Islands లో Sher Ali చేత హత్య (1872) — మొదటి మరియు ఏకైక హత్యకు గురైన వైస్రాయ్. Also: First census 1871."),

    (3, 1,
     "Lord Lytton (1876–1880) యొక్క Vernacular Press Act 1878 ఏ పేరుతో పిలవబడింది? / By what name was Lord Lytton's Vernacular Press Act 1878 called?",
     "Freedom Act", "Gagging Act — severely restricted Indian language press", "Press Regulation Act", "Publication Control Act", "b",
     "The Vernacular Press Act 1878 (during Lord Lytton's tenure) severely restricted the freedom of Indian-language newspapers. It was called the 'Gagging Act.' It was repealed by Lord Ripon in 1882. / Vernacular Press Act 1878 = 'Gagging Act' — Lord Lytton. 1882 లో Lord Ripon రద్దు చేశారు."),

    (3, 3,
     "Delhi Durbar 1877 ఎవరి కాలంలో జరిగింది మరియు Queen Victoria కి ఏ title ప్రకటించబడింది? / When was Delhi Durbar 1877 held and what title was proclaimed for Queen Victoria?",
     "Lord Canning — Queen of England", "Lord Lytton — Kaiser-i-Hind (Empress of India)", "Lord Mayo — Empress of India", "Lord Ripon — Queen of India", "b",
     "Delhi Durbar 1877 was held during Lord Lytton's tenure. Queen Victoria was proclaimed 'Kaiser-i-Hind' (Empress of India) at this Durbar. This followed the Royal Titles Act 1876. / Delhi Durbar 1877: Lord Lytton కాలంలో. Queen Victoria = Kaiser-i-Hind (Empress of India)."),

    (3, 2,
     "Lord Lawrence (1864–1869) యొక్క ముఖ్య విధానం ఏమిటి? / What was Lord Lawrence's main policy?",
     "Subsidiary Alliance expansion", "Masterly Inactivity — non-interference in Afghanistan affairs", "Partition of Bengal", "Morley-Minto Reforms", "b",
     "Lord Lawrence (1864–1869) followed the 'Masterly Inactivity' policy regarding Afghanistan — non-interference in Afghan affairs to avoid British involvement. / Lord Lawrence: 'Masterly Inactivity' — Afghanistan లో non-interference."),

    (3, 1,
     "Lord Northbrook (1872–1876) కాలంలో జరిగిన Gaekwad of Baroda case ఏమిటి? / What happened in the Gaekwad of Baroda case during Lord Northbrook's tenure?",
     "Gaekwad was given more territory", "Gaekwad was deposed for misrule and attempting to poison the British Resident", "Gaekwad signed Subsidiary Alliance", "Gaekwad won the case", "b",
     "During Lord Northbrook's tenure, the Gaekwad of Baroda was deposed in 1875 for misrule and an attempt to poison Colonel Phayre, the British Resident. / Lord Northbrook: Gaekwad of Baroda ని 1875 లో misrule + British Resident ని poison చేయడానికి attempt చేసినందుకు depose చేశారు."),

    # ── SEC 4: Ripon to Curzon (1880–1905) ────────────────────────────────────

    (4, 1,
     "Lord Ripon (1880–1884) యొక్క Local Self-Government policy ఏమిటి? / What was Lord Ripon's Local Self-Government policy?",
     "He centralised all government", "Resolution of 1882 — introduced elected local bodies (municipalities), called the 'Magna Carta of Local Self-Government'", "He introduced Subsidiary Alliance", "He introduced railways", "b",
     "Lord Ripon's Resolution on Local Self-Government (1882) established elected local bodies. It is called the 'Magna Carta of Local Self-Government in India.' He also repealed the Vernacular Press Act 1878 and passed the 1st Factory Act 1881. / Lord Ripon: Local Self-Govt 1882 (Magna Carta of LSG), Factory Act 1881, Vernacular Press Act repeal."),

    (4, 2,
     "Indian National Congress (INC) ఏ వైస్రాయ్ కాలంలో స్థాపించబడింది? / During which Viceroy's tenure was the Indian National Congress founded?",
     "Lord Ripon", "Lord Lytton", "Lord Dufferin", "Lord Lansdowne", "c",
     "Indian National Congress (INC) was founded on December 28, 1885, during Lord Dufferin's tenure. A.O. Hume played a key role. / INC స్థాపన: December 28, 1885 — Lord Dufferin కాలంలో. A.O. Hume ముఖ్య పాత్ర."),

    (4, 2,
     "Lord Curzon (1899–1905) బెంగాల్‌ను ఏ సంవత్సరంలో విభజించారు? / In which year did Lord Curzon partition Bengal?",
     "1899", "1903", "1905 — October 16", "1907", "c",
     "Lord Curzon partitioned Bengal on October 16, 1905. The partition divided Bengal into East Bengal (predominantly Muslim) and West Bengal (predominantly Hindu). This caused the Swadeshi Movement. / Bengal Partition: October 16, 1905 — Lord Curzon. Swadeshi Movement ప్రేరణ."),

    (4, 1,
     "Ilbert Bill (1883) controversy ఎవరి కాలంలో జరిగింది? / During whose tenure did the Ilbert Bill (1883) controversy occur?",
     "Lord Lytton", "Lord Ripon", "Lord Dufferin", "Lord Curzon", "b",
     "The Ilbert Bill controversy occurred during Lord Ripon's tenure. The bill proposed allowing Indian judges to try British subjects in criminal cases. European opposition forced a compromise (the 'White Mutiny'). / Ilbert Bill 1883: Lord Ripon కాలంలో. Indian judges British subjects ని try చేయవచ్చనే bill — Europeans వ్యతిరేకించారు."),

    (4, 3,
     "Lord Curzon పాలనలో Archaeological Survey of India (ASI) పునర్వ్యవస్థీకరణ మరియు Ancient Monuments Act ఏ సంవత్సరంలో వచ్చింది? / Under Lord Curzon, when were ASI reorganised and Ancient Monuments Act passed?",
     "1899", "1901", "1904", "1907", "c",
     "Under Lord Curzon, the Ancient Monuments Preservation Act was passed in 1904, and the Archaeological Survey of India (ASI) was reorganised under John Marshall. This protected India's historical monuments. / Lord Curzon: Ancient Monuments Act 1904, ASI reorganisation under John Marshall."),

    (4, 2,
     "Lord Lansdowne (1888–1894) కాలంలో ఏ ముఖ్యమైన Act వచ్చింది? / What important Act came during Lord Lansdowne's tenure (1888–1894)?",
     "INC founded", "Indian Councils Act 1892 — expanded Legislative Councils, introduced elections", "Partition of Bengal", "Rowlatt Act", "b",
     "Indian Councils Act 1892 was passed during Lord Lansdowne's tenure. It expanded the Legislative Councils and introduced, for the first time, the principle of election (indirect) to Legislative Councils. / Indian Councils Act 1892: Lord Lansdowne — Legislative Councils విస్తరణ, మొదటిసారి elections సూత్రం ప్రవేశపెట్టారు."),

    (4, 1,
     "బెంగాల్ విభజన 1905 రద్దు ఎవరి కాలంలో జరిగింది? / During whose tenure was the Partition of Bengal 1905 annulled?",
     "Lord Curzon", "Lord Minto II", "Lord Hardinge II (1911)", "Lord Chelmsford", "c",
     "The Partition of Bengal (1905) was annulled by Lord Hardinge II in 1911. The British capital was also moved from Calcutta to Delhi in 1911. / Bengal Partition రద్దు: Lord Hardinge II (1911). Also: Capital Calcutta నుండి Delhi కి 1911 లో మార్చారు."),

    # ── SEC 5: Minto II to Irwin (1905–1931) ─────────────────────────────────

    (5, 1,
     "Morley-Minto Reforms (1909) ఏ ముఖ్య వాస్తవాన్ని ప్రవేశపెట్టాయి? / What key feature did the Morley-Minto Reforms (1909) introduce?",
     "Universal adult franchise", "Separate electorates for Muslims (communal representation)", "Federal structure", "Responsible government", "b",
     "Morley-Minto Reforms (Indian Councils Act 1909) introduced separate electorates for Muslims — a significant communal concession that planted seeds of communalism. Morley = Secretary of State, Minto II = Viceroy. / Morley-Minto Reforms 1909: Muslims కి separate electorates — communalism బీజాలు."),

    (5, 2,
     "Montagu-Chelmsford Reforms (1919) ఏ ముఖ్య feature introduce చేసింది? / What key feature did Montagu-Chelmsford Reforms (1919) introduce?",
     "Full responsible government", "Dyarchy (Diarchy) at provincial level — divided subjects into Reserved and Transferred", "Independence of India", "Permanent Settlement", "b",
     "Montagu-Chelmsford Reforms (Government of India Act 1919) introduced Dyarchy at provincial level — subjects were divided into 'Reserved' (under Governor) and 'Transferred' (under elected ministers). Chelmsford was the Viceroy, Montagu the Secretary of State. / Montagu-Chelmsford 1919: Dyarchy — Reserved (Governor) + Transferred (elected ministers)."),

    (5, 2,
     "Rowlatt Act (1919) కి Indians ఎందుకు వ్యతిరేకించారు? / Why did Indians oppose the Rowlatt Act (1919)?",
     "It increased taxes", "It allowed detention without trial — 'No appeal, no vakeel, no daleel'", "It partitioned Bengal", "It imposed separate electorates", "b",
     "The Rowlatt Act (1919) allowed detention without trial, without right of appeal ('No appeal, no vakeel, no daleel'). Gandhi called for nationwide protests — leading to Jallianwala Bagh massacre (April 13, 1919). / Rowlatt Act 1919: Trial without appeal, detention without warrant. Jallianwala Bagh massacre ప్రేరణ."),

    (5, 1,
     "Jallianwala Bagh massacre (April 13, 1919) సమయంలో వైస్రాయ్ ఎవరు? / Who was the Viceroy during the Jallianwala Bagh massacre (April 13, 1919)?",
     "Lord Irwin", "Lord Reading", "Lord Chelmsford", "Lord Minto II", "c",
     "Lord Chelmsford (1916–1921) was the Viceroy during the Jallianwala Bagh massacre (April 13, 1919). General Dyer ordered the firing, killing hundreds of unarmed civilians. / Jallianwala Bagh Massacre: April 13, 1919 — Lord Chelmsford కాలంలో. General Dyer firing order."),

    (5, 3,
     "Chauri Chaura incident (February 4, 1922) ఎవరి కాలంలో జరిగింది మరియు దాని ప్రభావం ఏమిటి? / During whose tenure did Chauri Chaura occur and what was its impact?",
     "Lord Chelmsford — started Non-Cooperation", "Lord Reading — Gandhi suspended Non-Cooperation Movement after this", "Lord Irwin — ended Civil Disobedience", "Lord Willingdon — ended Quit India", "b",
     "Chauri Chaura incident (February 4, 1922) occurred during Lord Reading's tenure (1921–1926). A mob set fire to a police station, killing 22 policemen. Gandhi suspended the Non-Cooperation Movement because of this violence. / Chauri Chaura: February 4, 1922 — Lord Reading కాలంలో. Gandhi Non-Cooperation Movement suspend చేశారు."),

    (5, 2,
     "Gandhi-Irwin Pact (1931) ఏ event తో ముడిపడి ఉంది? / With which event is the Gandhi-Irwin Pact (1931) associated?",
     "Non-Cooperation Movement", "Salt Satyagraha / Civil Disobedience Movement — Gandhi suspended CDM after this pact", "Quit India Movement", "Swadeshi Movement", "b",
     "Gandhi-Irwin Pact (March 1931): Gandhi agreed to suspend the Civil Disobedience Movement (launched after Dandi March/Salt Satyagraha, March 12, 1930). Irwin agreed to release political prisoners. / Gandhi-Irwin Pact 1931: Civil Disobedience Movement suspend — Lord Irwin (1926–1931) కాలంలో."),

    (5, 1,
     "Dandi March (Salt Satyagraha) ఎవరి వైస్రాయ్ కాలంలో జరిగింది? / During which Viceroy's tenure did the Dandi March (Salt Satyagraha) occur?",
     "Lord Reading", "Lord Chelmsford", "Lord Irwin", "Lord Willingdon", "c",
     "Dandi March / Salt Satyagraha occurred on March 12, 1930, during Lord Irwin's tenure (1926–1931). Gandhi walked 241 miles from Sabarmati to Dandi, breaking the Salt Law on April 6, 1930. / Dandi March: March 12, 1930 — Lord Irwin కాలంలో. 241 miles, Sabarmati నుండి Dandi."),

    (5, 2,
     "Lord Reading (1921–1926) కాలంలో ఏ ముఖ్య విప్లవ సంఘటన జరిగింది? / What key revolutionary incident occurred during Lord Reading's tenure (1921–1926)?",
     "Jallianwala Bagh", "Moplah Rebellion 1921 and Kakori Conspiracy 1925", "Partition of Bengal", "Simon Commission", "b",
     "During Lord Reading's tenure: Moplah Rebellion in Kerala (1921), Chauri Chaura (1922) — non-cooperation suspended, and Kakori Conspiracy (August 9, 1925) — revolutionary train robbery. / Lord Reading: Moplah Rebellion 1921, Chauri Chaura 1922, Kakori Conspiracy 1925."),

    # ── SEC 6: Willingdon to Mountbatten (1931–1947) ──────────────────────────

    (6, 1,
     "Government of India Act 1935 ఏ వైస్రాయ్ కాలంలో పాస్ అయింది? / During which Viceroy's tenure was the Government of India Act 1935 passed?",
     "Lord Irwin", "Lord Willingdon", "Lord Linlithgow", "Lord Reading", "b",
     "Government of India Act 1935 was passed during Lord Willingdon's tenure (1931–1936). It introduced provincial autonomy, federal structure (though not fully implemented), separate electorates, and dyarchy at Centre. / GOI Act 1935: Lord Willingdon (1931–1936). Provincial autonomy, Federal structure, Dyarchy at Centre."),

    (6, 2,
     "Cripps Mission (1942) ఎవరి వైస్రాయ్ కాలంలో వచ్చింది మరియు Indians ఎందుకు తిరస్కరించారు? / During whose tenure did Cripps Mission arrive and why did Indians reject it?",
     "Lord Wavell — offered full independence", "Lord Linlithgow — offered Dominion Status after WWII, not immediate independence; Congress rejected as 'post-dated cheque'", "Lord Mountbatten — Partition plan", "Lord Irwin — offered self-government", "b",
     "Cripps Mission (March–April 1942) came during Lord Linlithgow's tenure. It offered Dominion Status after WWII but not immediate independence. Gandhi called it a 'post-dated cheque on a failing bank.' / Cripps Mission 1942: Lord Linlithgow — WWII తర్వాత Dominion Status — Congress 'post-dated cheque' అని తిరస్కరించింది."),

    (6, 1,
     "Quit India Movement (August 8, 1942) ఎవరి వైస్రాయ్ కాలంలో జరిగింది? / During whose Viceroy tenure did the Quit India Movement occur?",
     "Lord Willingdon", "Lord Linlithgow", "Lord Wavell", "Lord Mountbatten", "b",
     "Quit India Movement was launched on August 8, 1942, during Lord Linlithgow's tenure. Gandhi gave 'Do or Die' slogan at Gowalia Tank, Bombay. The British arrested most Congress leaders the next day. / Quit India: August 8, 1942 — Lord Linlithgow. 'Do or Die' — Gandhi. Congress leaders arrested."),

    (6, 2,
     "Cabinet Mission (1946) ఎవరి వైస్రాయ్ కాలంలో వచ్చింది? / During whose Viceroy tenure did the Cabinet Mission (1946) arrive?",
     "Lord Linlithgow", "Lord Wavell", "Lord Mountbatten", "Lord Irwin", "b",
     "Cabinet Mission (March–June 1946) came during Lord Wavell's tenure (1944–1947). It proposed a united India with a three-tier federal structure but both Congress and League disagreed on key provisions. / Cabinet Mission 1946: Lord Wavell కాలంలో. United India proposal — Congress and League both had objections."),

    (6, 3,
     "Lord Mountbatten (1947) యొక్క Mountbatten Plan ఏమిటి? / What was Lord Mountbatten's Mountbatten Plan?",
     "Complete federation of India", "June 3, 1947 Plan — partition of British India into India and Pakistan, princes to choose", "Cabinet Mission Plan", "GOI Act 1935 implementation", "b",
     "Mountbatten Plan (June 3, 1947): Partition of British India into India and Pakistan. Princely states could accede to either dominion or remain independent. India and Pakistan became independent on August 15, 1947. Radcliffe Line divided Punjab and Bengal. / Mountbatten Plan: June 3, 1947 — India + Pakistan partition. August 15, 1947 Independence."),

    (6, 1,
     "భారత స్వాతంత్ర్యం ఎప్పుడు వచ్చింది మరియు అప్పటి వైస్రాయ్ ఎవరు? / When did India gain independence and who was the Viceroy then?",
     "August 15, 1947 — Lord Wavell", "August 15, 1947 — Lord Mountbatten", "January 26, 1950 — Rajendra Prasad", "August 15, 1946 — Lord Linlithgow", "b",
     "India gained independence on August 15, 1947, with Lord Mountbatten as the last Viceroy (and first Governor General). Jawaharlal Nehru became India's first Prime Minister. / స్వాతంత్ర్యం: August 15, 1947 — Lord Mountbatten (last Viceroy, first GG). Nehru = first PM."),

    (6, 2,
     "Wavell Plan (1945) ఏమిటి? / What was the Wavell Plan (1945)?",
     "Partition plan", "Simla Conference plan — proposed an Executive Council with equal Hindu-Muslim representation; failed due to Jinnah's opposition", "Federal Constitution", "Cripps Mission", "b",
     "Wavell Plan (1945) was proposed at the Simla Conference. Lord Wavell proposed an Executive Council with equal Hindu-Muslim representation. It failed because Jinnah insisted on Muslim League nominees for all Muslim seats. / Wavell Plan 1945: Simla Conference — equal Hindu-Muslim representation. Jinnah's opposition వల్ల fail."),

    # ── SEC 7: Quick Revision — Key Facts ────────────────────────────────────

    (7, 1,
     "భారతదేశ మొదటి గవర్నర్ జనరల్ (Governor General of India) ఎవరు? / Who was the first Governor General of India?",
     "Warren Hastings", "Lord Cornwallis", "Lord William Bentinck", "Lord Canning", "c",
     "Lord William Bentinck was the first Governor General of India (1833–1835) after the Charter Act 1833 changed the designation from 'Governor General of Bengal' to 'Governor General of India.' / మొదటి Governor General of India = Lord William Bentinck (1833–1835). Charter Act 1833 ద్వారా designation మార్పు."),

    (7, 1,
     "British India యొక్క చివరి Viceroy ఎవరు? / Who was the last Viceroy of British India?",
     "Lord Wavell", "Lord Linlithgow", "Lord Mountbatten", "Lord Irwin", "c",
     "Lord Mountbatten was the last Viceroy of British India (February 1947 – August 15, 1947). After independence, he became the first Governor General of independent India until June 1948. / చివరి Viceroy = Lord Mountbatten. స్వాతంత్ర్యం తర్వాత independent India యొక్క మొదటి Governor General."),

    (7, 2,
     "Indian Councils Act 1861 ఏ ముఖ్య మార్పులు తెచ్చింది? / What key changes did the Indian Councils Act 1861 bring?",
     "Introduced dyarchy", "Portfolio system, enlarged Legislative Councils, restored legislative powers to Bombay and Madras", "Introduced elections", "Created Viceroy's post", "b",
     "Indian Councils Act 1861 (Lord Canning): (1) Portfolio System introduced; (2) Legislative Councils enlarged; (3) Bombay and Madras restored legislative powers; (4) Viceroy could issue ordinances. / Indian Councils Act 1861: Portfolio system, expanded LCs, Bombay-Madras powers restored."),

    (7, 1,
     "Permanent Settlement 1793 లో భూమిపై revenue ఎవరికి fixed చేశారు? / With whom was land revenue fixed in the Permanent Settlement 1793?",
     "Ryots (peasants)", "Zamindars (landlords)", "Village headmen", "Government officials", "b",
     "Permanent Settlement 1793 (Lord Cornwallis) fixed land revenue permanently with zamindars (landlords). Zamindars had to pay a fixed revenue to the government; in return they got hereditary rights over land. / Permanent Settlement: Zamindars తో revenue permanently fix — hereditary land rights."),

    (7, 3,
     "Subsidiary Alliance policy లో Indian rulers కి ఏ conditions impose చేయబడ్డాయి? / What conditions were imposed on Indian rulers under Subsidiary Alliance?",
     "Pay tribute only", "Maintain British army at their cost, expel other Europeans, no independent foreign relations, British Resident at court", "Only allow British trade", "Accept British Governor", "b",
     "Subsidiary Alliance (Lord Wellesley): Indian rulers must (1) maintain a British subsidiary force at their expense; (2) expel other European advisors; (3) not have independent foreign relations; (4) accept a British Resident at their court. Violation = annexation. / Subsidiary Alliance: British army maintain, no foreign relations, British Resident accept. Violation = annexation."),

    (7, 2,
     "Lord Ripon యొక్క First Factory Act (1881) ఏమి చేసింది? / What did Lord Ripon's First Factory Act (1881) do?",
     "Allowed child labour", "Restricted child labour (children under 7 cannot work), limited working hours, weekly holiday for factories", "Abolished all factories", "Created new factories", "b",
     "First Factory Act 1881 (Lord Ripon): (1) Children under 7 cannot work in factories; (2) 9-12 year olds limited to 9 hours/day; (3) Prohibited hazardous work for children; (4) Weekly holiday. First legislation for labour welfare in India. / Factory Act 1881: Child labour restriction, working hours limit — first labour welfare law."),

    (7, 2,
     "వైస్రాయ్‌లలో రైల్వేలు ఎక్కువగా అభివృద్ధి చేసిన వారు ఎవరు? / Which Viceroy developed railways most extensively in India?",
     "Lord Canning", "Lord Lawrence", "Lord Dalhousie (Governor General, not Viceroy)", "Lord Curzon", "c",
     "Lord Dalhousie (Governor General, 1848–1856, not technically a Viceroy) is credited with introducing and extensively developing railways in India. First railway: Bombay–Thane 1853. By 1856, several lines were planned/built. / Railways most credit = Lord Dalhousie (GG, not Viceroy). First railway 1853."),

    (7, 1,
     "Simon Commission (1927) ఎవరి వైస్రాయ్ కాలంలో వచ్చింది? / During whose Viceroy's tenure did the Simon Commission (1927) arrive?",
     "Lord Irwin", "Lord Reading", "Lord Willingdon", "Lord Chelmsford", "a",
     "Simon Commission arrived in India in 1927–28 during Lord Irwin's tenure. Indians boycotted it because it had no Indian member. Lala Lajpat Rai was lathi-charged during protests and died (November 17, 1928). / Simon Commission 1927–28: Lord Irwin కాలంలో. No Indian member — boycott. Lala Lajpat Rai lathi-charge."),
]


# ─────────────────────────────────────────────────────────────────────────────
# INNER FUNCTIONS  (called by app.py startup + API routes)
# ─────────────────────────────────────────────────────────────────────────────

def _seed_ch4_modern_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    import datetime as _dt
    ph = "%s" if use_postgres else "?"

    existing_row = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE topic={ph} AND subtopic={ph} AND chapter_num={ph}",
        ('Indian_History', 'Modern', 4)).fetchone()
    existing = row_to_dict_fn(existing_row or {})
    note_id = existing.get('id')

    if note_id and not force:
        return {"success": True, "message": "Chapter 4 Modern notes already exist.", "note_id": note_id}

    sections_json = _json.dumps(CH4M_SECTIONS, ensure_ascii=False)

    if note_id and force:
        db_exec_fn(conn,
            f"UPDATE study_notes SET chapter_title_en={ph}, sections_json={ph} WHERE id={ph}",
            ('Governor Generals & Viceroys of India', sections_json, note_id))
        if not use_postgres:
            conn.commit()
        return {"success": True, "message": "Chapter 4 Modern notes updated (force).", "note_id": note_id}

    cur = db_exec_fn(conn,
        f"""INSERT INTO study_notes
            (subject, topic, subtopic, chapter_num,
             chapter_title_te, chapter_title_en, pages_ref, sections_json)
            VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
        ('GK', 'Indian_History', 'Modern', 4,
         'గవర్నర్ జనరళ్ళు మరియు వైస్రాయ్‌లు',
         'Governor Generals & Viceroys of India',
         'Modern History Ch.4',
         sections_json))

    if not use_postgres:
        conn.commit()
        note_id = cur.lastrowid
    else:
        row = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE topic={ph} AND subtopic={ph} AND chapter_num={ph}",
            ('Indian_History', 'Modern', 4)).fetchone()
        note_id = row_to_dict_fn(row or {}).get('id')

    return {"success": True, "message": "Chapter 4 Modern notes seeded.", "note_id": note_id}


def _seed_ch4_modern_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
    ph = "%s" if use_postgres else "?"

    note_row = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE topic={ph} AND subtopic={ph} AND chapter_num={ph}",
        ('Indian_History', 'Modern', 4)).fetchone()
    note_id = row_to_dict_fn(note_row or {}).get('id')
    if not note_id:
        return {"success": False, "error": "study_notes row for Modern ch4 not found."}

    cnt_row = db_exec_fn(conn,
        f"SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,)).fetchone()
    existing_count = list(row_to_dict_fn(cnt_row or {}).values())[0] if cnt_row else 0
    if existing_count > 0:
        return {
            "success": True,
            "message": f"Chapter 4 Modern MCQs already seeded ({existing_count} questions).",
            "total": existing_count,
        }

    inserted = easy = medium = hard = 0
    for (sec_idx, diff, q, a, b, c, d, correct, expl) in CH4M_MCQS:
        db_exec_fn(conn,
            f"""INSERT INTO chapter_mcqs
                (study_note_id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te)
                VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
            (note_id, sec_idx, diff, q, a, b, c, d, correct, expl))
        inserted += 1
        if diff == 1: easy += 1
        elif diff == 2: medium += 1
        else: hard += 1

    if not use_postgres:
        conn.commit()

    return {
        "success": True,
        "message": f"Chapter 4 Modern MCQs seeded! ({inserted} questions)",
        "total": inserted,
        "easy": easy,
        "medium": medium,
        "hard": hard,
    }


def seed_ch4_modern_notes(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    try:
        return _seed_ch4_modern_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force)
    except Exception as e:
        return {"success": False, "error": str(e)}


def seed_ch4_modern_mcqs(conn, db_exec, row_to_dict, USE_POSTGRES):
    try:
        return _seed_ch4_modern_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES)
    except Exception as e:
        return {"success": False, "error": str(e)}


# ─────────────────────────────────────────────────────────────────────────────
# STANDALONE TEST  (python seed_ch4_modern.py)
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sqlite3, json

    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row

    def _exec(c, sql, params=()):
        cur = c.execute(sql, params)
        c.commit()
        return cur

    def _r2d(row):
        return dict(row) if row else {}

    conn.execute('''CREATE TABLE IF NOT EXISTS study_notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT, topic TEXT, subtopic TEXT, chapter_num INTEGER,
        chapter_title_te TEXT, chapter_title_en TEXT,
        pages_ref TEXT DEFAULT '',
        sections_json TEXT NOT NULL DEFAULT "[]",
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS chapter_mcqs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        study_note_id INTEGER, section_idx INTEGER, difficulty INTEGER,
        q_te TEXT, opt_a TEXT, opt_b TEXT, opt_c TEXT, opt_d TEXT,
        correct TEXT, explanation_te TEXT)''')
    conn.commit()

    print("=== Seeding Notes ===")
    r = _seed_ch4_modern_notes_inner(conn, _exec, _r2d, False, force=True)
    print(r)

    print("\n=== Seeding MCQs ===")
    r2 = _seed_ch4_modern_mcqs_inner(conn, _exec, _r2d, False)
    print(r2)

    cur = conn.execute("SELECT COUNT(*) FROM study_notes WHERE subtopic='Modern' AND chapter_num=4")
    print(f"\nstudy_notes rows: {cur.fetchone()[0]}")
    cur = conn.execute("SELECT COUNT(*) FROM chapter_mcqs")
    print(f"chapter_mcqs rows: {cur.fetchone()[0]}")
    cur = conn.execute("SELECT COUNT(*) FROM chapter_mcqs WHERE difficulty=1")
    e = cur.fetchone()[0]
    cur = conn.execute("SELECT COUNT(*) FROM chapter_mcqs WHERE difficulty=2")
    m = cur.fetchone()[0]
    cur = conn.execute("SELECT COUNT(*) FROM chapter_mcqs WHERE difficulty=3")
    h = cur.fetchone()[0]
    print(f"Easy={e}  Medium={m}  Hard={h}  Total={e+m+h}")
    print(f"\n✅ MODERN CH4 COMPLETE — 8 SECTIONS (SEC 0–7), {e+m+h} MCQs")
