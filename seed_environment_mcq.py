"""
Seed: Environment & Climate — Current Affairs 2024-2026
IDs: 25001–25080
Folder: AP_HC
Topic: National_Current_Affairs (wildlife, protected areas, COP, species — India-centric)
Cross-checked: GKToday Environment & Biodiversity MCQs (Pages 1-2), PIB, IUCN, NTCA
"""

import os, sys

DATABASE_URL = os.environ.get('DATABASE_URL', '')
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
USE_POSTGRES = bool(DATABASE_URL)

if USE_POSTGRES:
    import psycopg2
    import psycopg2.extras
else:
    import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')


def get_conn():
    if USE_POSTGRES:
        return psycopg2.connect(DATABASE_URL)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _fv(row):
    if row is None:
        return 0
    if isinstance(row, dict):
        return list(row.values())[0]
    return list(row)[0]


def seed():
    conn = get_conn()
    if USE_POSTGRES:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    else:
        cur = conn.cursor()

    # Idempotency check (uses parameterised query for both DB types)
    ph = '%s' if USE_POSTGRES else '?'
    cur.execute(f"SELECT COUNT(*) FROM questions WHERE id >= {ph} AND id <= {ph}", (25001, 25080))
    if _fv(cur.fetchone()) >= 75:
        conn.close()
        return

    ph = '%s' if USE_POSTGRES else '?'
    questions = [
        # --- Wildlife Sanctuaries ---
        {
            "id": 25001,
            "question_text": "Pobitora Wildlife Sanctuary, which has the highest density of Greater One-Horned Rhinoceros in India, is located in which state?",
            "option_a": "Sikkim",
            "option_b": "Assam",
            "option_c": "Manipur",
            "option_d": "Meghalaya",
            "correct_answer": "B",
            "explanation": "Pobitora Wildlife Sanctuary is located in eastern Guwahati, Assam. It was established in 1998 and spans 48.81 sq km. It has the highest density of Greater One-Horned Rhinoceros in India and is part of the Indian Rhino Vision 2020 program.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25002,
            "question_text": "Corbett Tiger Reserve, India's oldest tiger reserve, is located in which state?",
            "option_a": "Himachal Pradesh",
            "option_b": "Rajasthan",
            "option_c": "Gujarat",
            "option_d": "Uttarakhand",
            "correct_answer": "D",
            "explanation": "Corbett Tiger Reserve is located in the foothills of the Himalayas in Uttarakhand. It was established in 1936 as Hailey National Park and renamed Corbett National Park in 1957 to honor Jim Corbett. Its total area is 1,288.31 sq km.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25003,
            "question_text": "Karimpuzha Wildlife Sanctuary, which is part of the Nilgiri Biosphere Reserve, is located in which state?",
            "option_a": "Gujarat",
            "option_b": "Odisha",
            "option_c": "Kerala",
            "option_d": "Tamil Nadu",
            "correct_answer": "C",
            "explanation": "Karimpuzha Wildlife Sanctuary is in Malappuram district, Kerala, covering 227.97 sq km on the western slopes of the Nilgiri Hills. It is part of the Nilgiri Biosphere Reserve under UNESCO's Man and Biosphere Programme and shares boundaries with Silent Valley NP (Kerala) and Mukurthi NP (Tamil Nadu).",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25004,
            "question_text": "Nagarhole National Park, also known as Rajiv Gandhi National Park, is located in which state?",
            "option_a": "Tamil Nadu",
            "option_b": "Karnataka",
            "option_c": "Odisha",
            "option_d": "Maharashtra",
            "correct_answer": "B",
            "explanation": "Nagarhole National Park, also known as Rajiv Gandhi National Park, is a notified Tiger Reserve and part of Project Tiger. It is located in Kodagu and Mysuru districts, Karnataka, and is named after the Nagarahole River.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25005,
            "question_text": "Balpakram National Park, known as the 'Land of Perpetual Winds', is located in which state?",
            "option_a": "Meghalaya",
            "option_b": "Assam",
            "option_c": "Tripura",
            "option_d": "Mizoram",
            "correct_answer": "A",
            "explanation": "Balpakram National Park is located in the West Garo Hills district, Meghalaya, about 134 km from Shillong. It is known as the 'Land of Perpetual Winds' due to strong winds across the plateau. A rare Binturong (bearcat) was recently camera-trapped in its buffer zone.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25006,
            "question_text": "Indravati National Park, where anti-Naxal operations are conducted, is located in which state?",
            "option_a": "Karnataka",
            "option_b": "Bihar",
            "option_c": "Chhattisgarh",
            "option_d": "Odisha",
            "correct_answer": "C",
            "explanation": "Indravati National Park is located in Bijapur district, Chhattisgarh. It is named after the Indravati River, a tributary of the Godavari River. The river forms the northern and western boundaries of the park, also marking the Chhattisgarh–Maharashtra border.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25007,
            "question_text": "India's largest Wildlife Sanctuary, Indian Wild Ass Sanctuary (4,954 sq km), is located in which state?",
            "option_a": "Rajasthan",
            "option_b": "Gujarat",
            "option_c": "Madhya Pradesh",
            "option_d": "Maharashtra",
            "correct_answer": "B",
            "explanation": "The Indian Wild Ass Sanctuary is located in the state of Gujarat with a total area of 4,954 sq km, making it India's largest wildlife sanctuary.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25008,
            "question_text": "Keoladeo National Park (Bharatpur Bird Sanctuary), a UNESCO World Heritage Site, is located in which state?",
            "option_a": "Uttar Pradesh",
            "option_b": "Gujarat",
            "option_c": "Rajasthan",
            "option_d": "Haryana",
            "correct_answer": "C",
            "explanation": "Keoladeo National Park, also called Bharatpur Bird Sanctuary, is located in Rajasthan. It is a UNESCO World Heritage Site famous for hosting thousands of migratory birds each winter.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- New Tiger Reserves ---
        {
            "id": 25009,
            "question_text": "Ratapani Wildlife Sanctuary was declared as Madhya Pradesh's 8th Tiger Reserve in 2025. It acts as a corridor between which two tiger reserves?",
            "option_a": "Kanha and Pench",
            "option_b": "Panna and Satpura",
            "option_c": "Bandhavgarh and Sanjay",
            "option_d": "Bori and Satpura",
            "correct_answer": "B",
            "explanation": "Ratapani Wildlife Sanctuary was declared the 8th tiger reserve of Madhya Pradesh in 2025. It spans over 890 sq km and serves as a vital corridor connecting the tiger populations of Panna and Satpura Tiger Reserves.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25010,
            "question_text": "Madhav National Park in Shivpuri was declared as which number tiger reserve of Madhya Pradesh in March 2025?",
            "option_a": "7th",
            "option_b": "8th",
            "option_c": "9th",
            "option_d": "10th",
            "correct_answer": "C",
            "explanation": "Madhav National Park in Shivpuri was declared Madhya Pradesh's 9th Tiger Reserve in March 2025, making MP the state with the highest number of tiger reserves.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Assam NP ---
        {
            "id": 25011,
            "question_text": "Shikhna Jwhwlao National Park, notified on February 16, 2025, is the 8th National Park in which state?",
            "option_a": "Arunachal Pradesh",
            "option_b": "Assam",
            "option_c": "Nagaland",
            "option_d": "Meghalaya",
            "correct_answer": "B",
            "explanation": "Shikhna Jwhwlao National Park in Assam was declared in 2024 and notified on February 16, 2025. It is the 3rd national park in Bodoland Territorial Region (BTR) and the 8th National Park in Assam.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- DPS Flamingo Lake ---
        {
            "id": 25012,
            "question_text": "DPS Flamingo Lake was approved as a Conservation Reserve by which state's Wildlife Board, becoming the first wetland linked to Thane Creek Flamingo Sanctuary to receive such protection?",
            "option_a": "Maharashtra",
            "option_b": "Madhya Pradesh",
            "option_c": "Odisha",
            "option_d": "Karnataka",
            "correct_answer": "A",
            "explanation": "The Maharashtra State Wildlife Board approved the declaration of DPS Flamingo Lake as a conservation reserve. It is the first wetland linked to the Thane Creek Flamingo Sanctuary (TCFS) to receive such protection. The 30-acre lake is a key feeding and resting site for flamingos during high tide.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Tiger Statistics ---
        {
            "id": 25013,
            "question_text": "According to the 2022 All India Tiger Estimation, what is the total tiger population in India?",
            "option_a": "2,967",
            "option_b": "3,167",
            "option_c": "3,682",
            "option_d": "4,012",
            "correct_answer": "C",
            "explanation": "The 2022 All India Tiger Estimation recorded 3,682 tigers in India (range 3,167–3,925), representing about 70% of the world's wild tiger population. This was up from 2,967 tigers in 2018.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25014,
            "question_text": "As of March 2025, how many Tiger Reserves exist in India under Project Tiger?",
            "option_a": "52",
            "option_b": "55",
            "option_c": "58",
            "option_d": "62",
            "correct_answer": "C",
            "explanation": "As of March 2025, there are 58 Tiger Reserves in India under Project Tiger, covering about 84,500 sq km. Project Tiger was launched in 1973 and is managed by the National Tiger Conservation Authority (NTCA).",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25015,
            "question_text": "Which state has the highest number of tigers in India as per the 2022 tiger census?",
            "option_a": "Karnataka",
            "option_b": "Uttarakhand",
            "option_c": "Madhya Pradesh",
            "option_d": "Assam",
            "correct_answer": "C",
            "explanation": "Madhya Pradesh has the highest number of tigers (785) among all Indian states as per the 2022 All India Tiger Estimation.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Ramsar Sites ---
        {
            "id": 25016,
            "question_text": "After the addition of three new wetlands in 2024, what is India's total number of Ramsar sites?",
            "option_a": "75",
            "option_b": "80",
            "option_c": "85",
            "option_d": "92",
            "correct_answer": "C",
            "explanation": "In 2024, India added three new wetlands to its list of Ramsar Sites: Koonthankulam Bird Sanctuary, Koothankulam Wetland Complex (both in Tamil Nadu), and Hirekera Wetland (Karnataka), increasing the total to 85 Ramsar Sites covering around 14 lakh hectares.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25017,
            "question_text": "Hirekera Wetland, which was added as a new Ramsar Site in 2024, is located in which state?",
            "option_a": "Maharashtra",
            "option_b": "Tamil Nadu",
            "option_c": "Andhra Pradesh",
            "option_d": "Karnataka",
            "correct_answer": "D",
            "explanation": "Hirekera Wetland in Karnataka was added as a new Ramsar Site in 2024. Tamil Nadu also added two new Ramsar sites (Koonthankulam Bird Sanctuary and Koothankulam Wetland Complex) in the same year.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- New Species ---
        {
            "id": 25018,
            "question_text": "A new wild ginger species named Zingiber jagannathii, honoring Lord Jagannath, was discovered in which state's biosphere reserve?",
            "option_a": "Kerala",
            "option_b": "Odisha",
            "option_c": "Tamil Nadu",
            "option_d": "Jharkhand",
            "correct_answer": "B",
            "explanation": "Zingiber jagannathii Sahu & Priyadarshini was discovered in Similipal Biosphere Reserve, Odisha, in August 2024. It was found at 758m elevation in Kulipala's semi-evergreen forest and covers less than 1 sq km. The species honors Lord Jagannath.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25019,
            "question_text": "A new snakehead fish species named 'Channa nachi' was recently discovered in which state?",
            "option_a": "Meghalaya",
            "option_b": "Assam",
            "option_c": "Tripura",
            "option_d": "Sikkim",
            "correct_answer": "A",
            "explanation": "Channa nachi was discovered in Meghalaya, in a shallow slow-flowing stream near Chokpot village, which is part of the Simsang River system. The habitat consists of sand, leaf litter, and pebbles.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25020,
            "question_text": "India added how many new faunal species in the year 2024, a record in the country's biodiversity documentation?",
            "option_a": "433",
            "option_b": "500",
            "option_c": "683",
            "option_d": "812",
            "correct_answer": "C",
            "explanation": "In 2024, India recorded the addition of 683 new faunal species (459 new to science, 224 new to India) and 433 new floral taxa. Kerala led with 101 newly recorded species.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25021,
            "question_text": "Three new frog species (Gracixalus patkaiensis, Alcalus fontinalis, Nidirana noadihing) were discovered in 2024 from which Indian state?",
            "option_a": "Meghalaya",
            "option_b": "Nagaland",
            "option_c": "Arunachal Pradesh",
            "option_d": "Manipur",
            "correct_answer": "C",
            "explanation": "Three new frog species were discovered in early 2024 from the Kamlang–Namdapha biodiversity hotspot landscape in Arunachal Pradesh.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25022,
            "question_text": "A study in 2024 proposed that the king cobra be considered as four distinct species. The Western Ghats species was named what?",
            "option_a": "Ophiophagus bungarus",
            "option_b": "Ophiophagus kaalinga",
            "option_c": "Ophiophagus hannah",
            "option_d": "Ophiophagus ghati",
            "correct_answer": "B",
            "explanation": "A study led by Western Ghats-based scientist P. Gowri Shankar proposed that the king cobra is not one species but four distinct species. The Western Ghats species was named Ophiophagus kaalinga and is severely threatened / Critically Endangered.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- IUCN Status ---
        {
            "id": 25023,
            "question_text": "What is the IUCN conservation status of the Indian Giant Flying Squirrel (Petaurista philippensis)?",
            "option_a": "Endangered",
            "option_b": "Vulnerable",
            "option_c": "Critically Endangered",
            "option_d": "Least Concern",
            "correct_answer": "D",
            "explanation": "The Indian Giant Flying Squirrel is listed as 'Least Concern' by IUCN. It was recently sighted in Ranikhet, Uttarakhand. It can glide up to 60 meters and is protected under Schedule II of the Wildlife Protection Act, 1972.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25024,
            "question_text": "What is the IUCN conservation status of the Himalayan Musk Deer (Moschus leucogaster)?",
            "option_a": "Least Concern",
            "option_b": "Vulnerable",
            "option_c": "Endangered",
            "option_d": "Critically Endangered",
            "correct_answer": "C",
            "explanation": "The Himalayan Musk Deer is listed as Endangered on the IUCN Red List. Males have a musk gland, making them vulnerable to poaching. They are found in India, Nepal, Bhutan, Pakistan, and China. Listed under Schedule I of WPA 1972.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25025,
            "question_text": "The Saola, nicknamed the 'Asian Unicorn', is native to the Annamite Mountains of which two countries?",
            "option_a": "Thailand and Myanmar",
            "option_b": "Laos and Vietnam",
            "option_c": "Cambodia and Thailand",
            "option_d": "China and Laos",
            "correct_answer": "B",
            "explanation": "The Saola (Pseudoryx nghetinhensis), known as the 'Asian Unicorn', is found in the Annamite Mountains along the Vietnam–Laos border. It is Critically Endangered with only 50–300 individuals estimated. It was first discovered in 1992 during a joint survey by Vietnam's Ministry of Forestry and WWF.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25026,
            "question_text": "What is the IUCN conservation status of the Binturong (Bearcat)?",
            "option_a": "Least Concern",
            "option_b": "Vulnerable",
            "option_c": "Endangered",
            "option_d": "Critically Endangered",
            "correct_answer": "B",
            "explanation": "The Binturong, also known as the bearcat, is listed as Vulnerable on the IUCN Red List. It is the largest civet in India. A rare sighting was reported in the buffer zone of Balpakram National Park, Meghalaya.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25027,
            "question_text": "India has how many threatened species listed on the IUCN Red List?",
            "option_a": "874",
            "option_b": "1,174",
            "option_c": "1,450",
            "option_d": "2,200",
            "correct_answer": "B",
            "explanation": "According to the IUCN Red List, India has 1,174 threatened species. Some of the most Critically Endangered include the Gharial, Great Indian Bustard, Kashmir Stag, Pygmy Hog, and Namdapha Flying Squirrel.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25028,
            "question_text": "The Blyde Rondavel Flat Gecko was rediscovered after 34 years in which country?",
            "option_a": "Kenya",
            "option_b": "Nigeria",
            "option_c": "South Africa",
            "option_d": "Botswana",
            "correct_answer": "C",
            "explanation": "The Blyde Rondavel Flat Gecko was rediscovered in the Blyde River Canyon, Mpumalanga Province, South Africa after 34 years. It was first found in 1991 and had been listed as 'Data Deficient' by IUCN. The Endangered Wildlife Trust (EWT) confirmed its rediscovery — it is the 5th lost species found by EWT.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- COP29 ---
        {
            "id": 25029,
            "question_text": "COP29, the UN Climate Change Conference held in November 2024, took place in which city?",
            "option_a": "Sharm el-Sheikh",
            "option_b": "Dubai",
            "option_c": "Baku",
            "option_d": "Istanbul",
            "correct_answer": "C",
            "explanation": "COP29 was held in Baku, Azerbaijan in November 2024. Its main outcome was the Baku Climate Unity Pact, which set a target of at least $1.3 trillion per year from all actors and at least $300 billion/year from developed countries by 2035.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25030,
            "question_text": "What climate finance target for developed countries was agreed upon at COP29 in Baku 2024?",
            "option_a": "$100 billion per year by 2030",
            "option_b": "$300 billion per year by 2035",
            "option_c": "$500 billion per year by 2030",
            "option_d": "$1 trillion per year by 2040",
            "correct_answer": "B",
            "explanation": "At COP29 in Baku 2024, developed countries agreed to lead mobilization of at least $300 billion per year by 2035. The overall target is $1.3 trillion/year from all actors. India criticized this as 'abysmally poor'. The Baku–Belém Roadmap to 1.3T was also launched.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25031,
            "question_text": "The 'Baku-Belém Roadmap to 1.3T' was launched at COP29 to scale up climate finance. What does '1.3T' refer to?",
            "option_a": "$1.3 trillion per year from all actors",
            "option_b": "$1.3 trillion total by 2030",
            "option_c": "1.3°C temperature limit",
            "option_d": "1.3 billion tonnes CO2 reduction",
            "correct_answer": "A",
            "explanation": "The Baku–Belém Roadmap to 1.3T refers to raising at least $1.3 trillion per year from all actors (governments, private sector, multilateral banks) for climate action. This was the overall target set in the Baku Climate Unity Pact at COP29.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- COP30 ---
        {
            "id": 25032,
            "question_text": "COP30, held in November 2025, took place in which city of Brazil?",
            "option_a": "São Paulo",
            "option_b": "Rio de Janeiro",
            "option_c": "Manaus",
            "option_d": "Belém",
            "correct_answer": "D",
            "explanation": "COP30 was held in Belém, Brazil in November 2025 — the heart of the Amazon region. Key outcomes included the Belém Package, over 122 NDC submissions, and the launch of the Belém Mission to 1.5.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25033,
            "question_text": "Which package was approved at COP30 in Belém, 2025?",
            "option_a": "Amazon Pact",
            "option_b": "Belém Package",
            "option_c": "Paris Plus Agreement",
            "option_d": "Brazil Climate Deal",
            "correct_answer": "B",
            "explanation": "The Belém Package was approved at COP30 in Belém, Brazil (November 2025). Other outcomes included the Belém Mission to 1.5 (action-oriented platform), the Global Climate Finance Accountability Framework, and the submission of NDCs by 122+ Parties.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25034,
            "question_text": "The 'Belém Mission to 1.5' launched at COP30 refers to what?",
            "option_a": "A reforestation programme for 1.5 billion trees",
            "option_b": "An action platform to limit global warming to 1.5°C",
            "option_c": "A $1.5 trillion climate fund",
            "option_d": "Reducing carbon emissions by 1.5% annually",
            "correct_answer": "B",
            "explanation": "The Belém Mission to 1.5 is an action-oriented platform launched at COP30 to foster enhanced ambition and international cooperation across mitigation, adaptation, and investment — specifically aligned with limiting global warming to 1.5°C as per the Paris Agreement.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25035,
            "question_text": "COP30 in Belém 2025 called for tripling of which type of climate finance by 2035?",
            "option_a": "Mitigation finance",
            "option_b": "Technology transfer finance",
            "option_c": "Adaptation finance",
            "option_d": "Loss and damage finance",
            "correct_answer": "C",
            "explanation": "COP30 parties agreed to call for efforts to at least triple adaptation finance by 2035 within the New Collective Quantified Goal (NCQG) on climate finance.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- COP sequence ---
        {
            "id": 25036,
            "question_text": "COP31 is scheduled to be hosted in 2026 by which country?",
            "option_a": "Canada",
            "option_b": "Australia",
            "option_c": "Kenya",
            "option_d": "India",
            "correct_answer": "B",
            "explanation": "COP31 is scheduled to be held in Australia in 2026. The COP sequence: COP28 = Dubai (UAE) 2023 → COP29 = Baku (Azerbaijan) Nov 2024 → COP30 = Belém (Brazil) Nov 2025 → COP31 = Australia 2026.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Project Dolphin ---
        {
            "id": 25037,
            "question_text": "The first Ganges River Dolphin was successfully satellite-tagged on December 18, 2024, in which state?",
            "option_a": "Bihar",
            "option_b": "West Bengal",
            "option_c": "Uttar Pradesh",
            "option_d": "Assam",
            "correct_answer": "D",
            "explanation": "India achieved the milestone of satellite-tagging the first-ever Ganges River Dolphin on December 18, 2024, in Assam. This was led by the Wildlife Institute of India (WII) in collaboration with the Assam Forest Department and Aaranyak, under Project Dolphin.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25038,
            "question_text": "Under which project was India's first-ever Ganges River Dolphin satellite-tagging accomplished in 2024?",
            "option_a": "Project Tiger",
            "option_b": "Project Crocodile",
            "option_c": "Project Dolphin",
            "option_d": "Project Aqua",
            "correct_answer": "C",
            "explanation": "The first satellite-tagging of a Ganges River Dolphin was accomplished under Project Dolphin in December 2024 in Assam. Project Dolphin was launched in 2020 for conservation of Gangetic and Irrawaddy dolphins.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Rivers ---
        {
            "id": 25039,
            "question_text": "The Chambal River, home to the National Chambal Sanctuary, flows through which set of states?",
            "option_a": "Uttar Pradesh, Madhya Pradesh and Rajasthan",
            "option_b": "Bihar, Jharkhand and Uttar Pradesh",
            "option_c": "Gujarat, Rajasthan and Haryana",
            "option_d": "Maharashtra, MP and Chhattisgarh",
            "correct_answer": "A",
            "explanation": "The Chambal River flows through Madhya Pradesh, Rajasthan, and Uttar Pradesh. It originates from Bhadakla Falls near Janapav Hills, Indore (MP) and joins the Yamuna in Jalaun district, UP, covering 1,024 km. The National Chambal Sanctuary protects Gharial and Ganges dolphins.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25040,
            "question_text": "The Netravathi River, which flows through Mangaluru, is located in which state?",
            "option_a": "Maharashtra",
            "option_b": "Karnataka",
            "option_c": "Kerala",
            "option_d": "Tamil Nadu",
            "correct_answer": "B",
            "explanation": "Netravathi River (also called Nethravathi Nadi) is a major west-flowing river in Karnataka. It originates in the Kudremukh range of Chikkamagaluru district (Western Ghats) and drains into the Arabian Sea south of Mangaluru.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Yellow Sea ---
        {
            "id": 25041,
            "question_text": "The Yellow Sea, which is seeing increased Chinese activities, is a marginal sea of which ocean?",
            "option_a": "Indian Ocean",
            "option_b": "Atlantic Ocean",
            "option_c": "Arctic Ocean",
            "option_d": "Pacific Ocean",
            "correct_answer": "D",
            "explanation": "The Yellow Sea is a marginal sea of the Western Pacific Ocean. It is called Huang Hai in China and West Sea in North and South Korea. It gets its yellow color from sand particles blown from the Gobi Desert. It covers about 400,000 sq km with depths of 55–120 m.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25042,
            "question_text": "The Yellow Sea gets its characteristic yellow color from which source?",
            "option_a": "Minerals from sea floor",
            "option_b": "Algae bloom",
            "option_c": "Sand particles from Gobi Desert",
            "option_d": "Industrial effluents",
            "correct_answer": "C",
            "explanation": "The Yellow Sea gets its yellow color from sand particles blown in from the Gobi Desert. It is bordered by China on the north and west, and North Korea and South Korea on the east.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Pollution ---
        {
            "id": 25043,
            "question_text": "What are 'Nurdles', which were found in large quantities along the Thiruvananthapuram coastline in May 2025?",
            "option_a": "Newly discovered marine insects",
            "option_b": "Tiny plastic pellets used as raw material in plastic manufacturing",
            "option_c": "Heavy metal pollutants from industrial effluents",
            "option_d": "Dead coral fragments",
            "correct_answer": "B",
            "explanation": "Nurdles are small plastic pellets (1–5 mm) made of LDPE and HDPE, used as raw materials in plastic manufacturing. On May 27, 2025, large amounts were found along Thiruvananthapuram coast after the sinking of Liberian cargo ship MSC ELSA 3 on May 25, 2025. Marine animals can ingest them, causing health problems.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25044,
            "question_text": "The sinking of which cargo ship in May 2025 caused Nurdles pollution along Kerala's Thiruvananthapuram coastline?",
            "option_a": "MSC ELSA 3",
            "option_b": "MV Ever Given",
            "option_c": "SS Prestige",
            "option_d": "MV Wakashio",
            "correct_answer": "A",
            "explanation": "The Liberian cargo ship MSC ELSA 3 sank on May 25, 2025, carrying containers with hazardous materials including plastic pellets (nurdles). By May 27, 2025, large amounts of nurdles were found along the coast of Thiruvananthapuram, Kerala.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Volcanoes ---
        {
            "id": 25045,
            "question_text": "Poas Volcano, one of the world's most active volcanoes, is located in which country?",
            "option_a": "Japan",
            "option_b": "Indonesia",
            "option_c": "Costa Rica",
            "option_d": "Nicaragua",
            "correct_answer": "C",
            "explanation": "Poas Volcano is located in Costa Rica, inside the Poás Volcano National Park. It is a composite stratovolcano standing 2,708 m above sea level with a crater about 1.5 km wide and 300 m deep — one of the world's largest active volcanic craters.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Forests ---
        {
            "id": 25046,
            "question_text": "Teak (Tectona grandis), known as the 'King of Timbers', primarily grows in which type of forest?",
            "option_a": "Tropical Rainforest",
            "option_b": "Moist Deciduous Forest",
            "option_c": "Tropical Evergreen Forest",
            "option_d": "Coniferous Forest",
            "correct_answer": "B",
            "explanation": "Teak grows mainly in Moist Deciduous Forests. India holds 35% of the world's planted teak forests. According to FAO, Madhya Pradesh and Maharashtra have the largest areas of native teak forests in India.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25047,
            "question_text": "India holds approximately what percentage of the world's planted teak forests?",
            "option_a": "15%",
            "option_b": "25%",
            "option_c": "35%",
            "option_d": "50%",
            "correct_answer": "C",
            "explanation": "India holds 35% of the world's planted teak forests, with Asia contributing over 95% of global teak resources, according to the FAO Global Teak Resources and Market Assessment 2022.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Pobitora details ---
        {
            "id": 25048,
            "question_text": "Tamulidoba Beel, a major wetland that is drying up and threatening waterfowl habitat, is located within which wildlife sanctuary?",
            "option_a": "Kaziranga NP",
            "option_b": "Pobitora Wildlife Sanctuary",
            "option_c": "Manas NP",
            "option_d": "Nameri NP",
            "correct_answer": "B",
            "explanation": "Tamulidoba Beel is a major wetland within Pobitora Wildlife Sanctuary, Assam. Its drying up has been highlighted as a major threat to waterfowl habitat. Water hyacinth is another threat to wildlife in the sanctuary.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- WPA Schedule ---
        {
            "id": 25049,
            "question_text": "The Indian Giant Flying Squirrel is protected under which Schedule of the Wildlife Protection Act, 1972?",
            "option_a": "Schedule I",
            "option_b": "Schedule II",
            "option_c": "Schedule III",
            "option_d": "Schedule IV",
            "correct_answer": "B",
            "explanation": "The Indian Giant Flying Squirrel (Petaurista philippensis) is protected under Schedule II of the Wildlife Protection Act (WPA), 1972, and is listed as 'Least Concern' by IUCN.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25050,
            "question_text": "The Himalayan Musk Deer is listed under which Schedule of India's Wildlife Protection Act, 1972, indicating the highest protection?",
            "option_a": "Schedule IV",
            "option_b": "Schedule III",
            "option_c": "Schedule II",
            "option_d": "Schedule I",
            "correct_answer": "D",
            "explanation": "The Himalayan Musk Deer is listed under Schedule I of the Wildlife Protection Act, 1972, which provides the highest level of protection, prohibiting hunting. It is also listed as Endangered by IUCN.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- COP General ---
        {
            "id": 25051,
            "question_text": "COP stands for which full form in the context of UN Climate Change Conferences?",
            "option_a": "Conference of Parties",
            "option_b": "Congress of Plenipotentiaries",
            "option_c": "Convention on Pollution",
            "option_d": "Compact of Participants",
            "correct_answer": "A",
            "explanation": "COP stands for Conference of Parties. It is the annual meeting of countries that have signed the United Nations Framework Convention on Climate Change (UNFCCC). COP29 was held in Baku (2024) and COP30 in Belém, Brazil (2025).",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25052,
            "question_text": "Which country hosted COP28 in 2023?",
            "option_a": "Saudi Arabia",
            "option_b": "Qatar",
            "option_c": "UAE (Dubai)",
            "option_d": "Egypt",
            "correct_answer": "C",
            "explanation": "COP28 was held in Dubai, United Arab Emirates in November–December 2023. It was notable for the first global stocktake under the Paris Agreement. COP29 followed in Baku, Azerbaijan in November 2024.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Biosphere Reserves ---
        {
            "id": 25053,
            "question_text": "Similipal Biosphere Reserve, where a new ginger species was discovered in 2024, is located in which state?",
            "option_a": "Chhattisgarh",
            "option_b": "Jharkhand",
            "option_c": "Odisha",
            "option_d": "West Bengal",
            "correct_answer": "C",
            "explanation": "Similipal Biosphere Reserve is located in Odisha. In August 2024, researchers from Maharaja Sriram Chandra Bhanja Deo University discovered the new wild ginger species Zingiber jagannathii here.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 25054,
            "question_text": "The Nilgiri Biosphere Reserve is a UNESCO Man and Biosphere Programme site. Which of the following sanctuaries is part of it?",
            "option_a": "Pobitora Wildlife Sanctuary",
            "option_b": "Karimpuzha Wildlife Sanctuary",
            "option_c": "Indravati National Park",
            "option_d": "Balpakram National Park",
            "correct_answer": "B",
            "explanation": "Karimpuzha Wildlife Sanctuary in Kerala is part of the Nilgiri Biosphere Reserve under UNESCO's Man and Biosphere Programme. It also shares boundaries with Silent Valley NP (Kerala) and Mukurthi NP (Tamil Nadu).",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Binturong ---
        {
            "id": 25055,
            "question_text": "The Binturong (Bearcat), recently camera-trapped in Meghalaya, is described as the largest of which animal group in India?",
            "option_a": "Mongoose family",
            "option_b": "Civet family",
            "option_c": "Weasel family",
            "option_d": "Marten family",
            "correct_answer": "B",
            "explanation": "The Binturong, also known as the bearcat, is the largest civet in India. It is an omnivorous mammal found in dense forests of South and Southeast Asia. It was camera-trapped in the buffer zone of Balpakram National Park, Meghalaya.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Carbon/NDC ---
        {
            "id": 25056,
            "question_text": "NDC in the context of climate agreements stands for?",
            "option_a": "National Development Committee",
            "option_b": "Nationally Determined Contribution",
            "option_c": "Net Decarbonisation Commitment",
            "option_d": "Non-Deforestation Clause",
            "correct_answer": "B",
            "explanation": "NDC stands for Nationally Determined Contribution. It represents each country's plan to reduce greenhouse gas emissions and adapt to climate change impacts. By the end of COP30 in Belém, over 122 Parties had submitted updated NDCs.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Saola discovery ---
        {
            "id": 25057,
            "question_text": "The Saola was first discovered in 1992 during a joint survey by the Vietnamese Ministry of Forestry and which international organization?",
            "option_a": "IUCN",
            "option_b": "WWF (World Wildlife Fund)",
            "option_c": "WCS (Wildlife Conservation Society)",
            "option_d": "CITES",
            "correct_answer": "B",
            "explanation": "The Saola was first discovered in 1992 during a joint survey by the Vietnamese Ministry of Forestry and the World Wide Fund for Nature (WWF). Its genome was recently mapped by an international team of scientists using tissue fragments from hunter-collected remains.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Chambal ---
        {
            "id": 25058,
            "question_text": "The Chambal River originates from which location in Madhya Pradesh?",
            "option_a": "Amarkantak hills",
            "option_b": "Bhadakla Falls near Janapav Hills, Indore",
            "option_c": "Pachmarhi hills",
            "option_d": "Maikala Range",
            "correct_answer": "B",
            "explanation": "The Chambal River originates from Bhadakla Falls near Janapav Hills in Indore district, Madhya Pradesh, at an elevation of 843 metres. It flows about 1,024 km before joining the Yamuna River in Jalaun district, Uttar Pradesh.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- WII ---
        {
            "id": 25059,
            "question_text": "Which institution led the satellite-tagging of the first Ganges River Dolphin in Assam in December 2024?",
            "option_a": "Bombay Natural History Society (BNHS)",
            "option_b": "Centre for Wildlife Studies (CWS)",
            "option_c": "Wildlife Institute of India (WII)",
            "option_d": "Salim Ali Centre for Ornithology (SACON)",
            "correct_answer": "C",
            "explanation": "The Wildlife Institute of India (WII) led the satellite-tagging of the first Ganges River Dolphin in Assam on December 18, 2024, in collaboration with the Assam Forest Department and Aaranyak NGO, under Project Dolphin.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Budget ---
        {
            "id": 25060,
            "question_text": "The central government's 2025–26 budget allocated ₹290 crore (64% of wildlife habitat allocation) for which projects?",
            "option_a": "Project Crocodile and Project Vulture",
            "option_b": "Project Tiger and Project Elephant",
            "option_c": "Project Dolphin and Project Sea Turtle",
            "option_d": "Project Snow Leopard and Project Hangul",
            "correct_answer": "B",
            "explanation": "In the 2025–26 budget, ₹290 crore (64% of the ₹450 crore Integrated Wildlife Habitats allocation) was earmarked for Project Tiger and Project Elephant, representing an 18% increase over 2024–25 revised estimates.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Corbett details ---
        {
            "id": 25061,
            "question_text": "Jim Corbett National Park was originally established in 1936 under what name?",
            "option_a": "Corbett Wildlife Sanctuary",
            "option_b": "Hailey National Park",
            "option_c": "Ramganga National Park",
            "option_d": "Uttarakhand Forest Reserve",
            "correct_answer": "B",
            "explanation": "Corbett Tiger Reserve was established in 1936 as Hailey National Park and was renamed Corbett National Park in 1957 to honor Jim Corbett. Rivers Ramganga, Pallaen, and Sonanadi flow through it.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- NTCA ---
        {
            "id": 25062,
            "question_text": "Project Tiger is managed by which authority in India?",
            "option_a": "Wildlife Crime Control Bureau (WCCB)",
            "option_b": "National Tiger Conservation Authority (NTCA)",
            "option_c": "Central Zoo Authority (CZA)",
            "option_d": "Indian Board for Wildlife (IBWL)",
            "correct_answer": "B",
            "explanation": "Project Tiger is managed by the National Tiger Conservation Authority (NTCA) under the Ministry of Environment, Forests and Climate Change (MoEFCC). It was launched in 1973 and currently covers 58 Tiger Reserves.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Paris Agreement ---
        {
            "id": 25063,
            "question_text": "The Paris Agreement aims to limit global temperature increase to well below how many degrees Celsius above pre-industrial levels?",
            "option_a": "1°C",
            "option_b": "1.5°C",
            "option_c": "2°C",
            "option_d": "Both 1.5°C and 2°C (with 1.5°C as aspiration)",
            "correct_answer": "D",
            "explanation": "The Paris Agreement (2015) aims to hold global temperature increase to well below 2°C above pre-industrial levels and pursue efforts to limit it to 1.5°C. The 1.5°C target is the aspirational limit referenced in the Belém Mission to 1.5 at COP30.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- UNFCCC ---
        {
            "id": 25064,
            "question_text": "UNFCCC, under which the annual COP meetings are held, stands for?",
            "option_a": "United Nations Framework Convention on Climate Change",
            "option_b": "United Nations Fund for Carbon Capture",
            "option_c": "Universal Framework for Carbon and Climate Control",
            "option_d": "UN Forum for Climate Cooperation",
            "correct_answer": "A",
            "explanation": "UNFCCC stands for United Nations Framework Convention on Climate Change. It is the international treaty under which the annual Conference of Parties (COP) is held. COP29 was in Baku (2024) and COP30 in Belém (2025).",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Coral/Marine ---
        {
            "id": 25065,
            "question_text": "The Global Climate Finance Accountability Framework was launched at which COP?",
            "option_a": "COP27",
            "option_b": "COP28",
            "option_c": "COP29",
            "option_d": "COP30",
            "correct_answer": "D",
            "explanation": "The Global Climate Finance Accountability Framework was launched at COP30 in Belém, Brazil (November 2025) to strengthen transparency, credibility, and trust in climate finance delivery.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Ramsar ---
        {
            "id": 25066,
            "question_text": "The Ramsar Convention is related to the conservation of which type of ecosystems?",
            "option_a": "Forests",
            "option_b": "Wetlands",
            "option_c": "Coral Reefs",
            "option_d": "Mountain Grasslands",
            "correct_answer": "B",
            "explanation": "The Ramsar Convention on Wetlands (1971) is an international treaty for the conservation and sustainable use of wetlands. India has 85 Ramsar sites covering about 14 lakh hectares.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- BNHS ---
        {
            "id": 25067,
            "question_text": "The Bombay Natural History Society (BNHS) warned about which environmental risk related to the DPS Flamingo Lake near Navi Mumbai International Airport (NMIA)?",
            "option_a": "Flooding of runway",
            "option_b": "Bird strike risk from displaced flamingos",
            "option_c": "Noise pollution affecting flamingo breeding",
            "option_d": "Air quality degradation from airport emissions",
            "correct_answer": "B",
            "explanation": "BNHS experts warned that wetland loss near Navi Mumbai International Airport (NMIA) may push birds — particularly flamingos — near the airport, raising bird strike risks. The DPS Flamingo Lake near Thane Creek Flamingo Sanctuary was approved as a Conservation Reserve to address this.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Namdapha ---
        {
            "id": 25068,
            "question_text": "Namdapha National Park, a biodiversity hotspot where three new frog species were discovered, is located in which state?",
            "option_a": "Assam",
            "option_b": "Manipur",
            "option_c": "Arunachal Pradesh",
            "option_d": "Meghalaya",
            "correct_answer": "C",
            "explanation": "Namdapha National Park is located in Arunachal Pradesh. The Kamlang–Namdapha landscape is a biodiversity hotspot where three new frog species (Gracixalus patkaiensis, Alcalus fontinalis, Nidirana noadihing) were discovered in early 2024.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Western Ghats ---
        {
            "id": 25069,
            "question_text": "Kerala led India's 2024 biodiversity record with how many newly documented species?",
            "option_a": "51",
            "option_b": "68",
            "option_c": "101",
            "option_d": "143",
            "correct_answer": "C",
            "explanation": "In 2024's record-breaking biodiversity year, Kerala led all states with 101 newly recorded species — of which 80 were entirely new to science and 21 were documented in India for the first time. Finds included reptiles, amphibians, butterflies, orchids, fungi, and lichens.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- CZA ---
        {
            "id": 25070,
            "question_text": "A 2024 report by the Central Zoo Authority highlighted a gap in conservation breeding for which species in Indian zoos?",
            "option_a": "Indian Giant Flying Squirrel",
            "option_b": "Himalayan Musk Deer",
            "option_c": "Snow Leopard",
            "option_d": "Pygmy Hog",
            "correct_answer": "B",
            "explanation": "The 2024 report 'Plant Breeding Programmes in Indian Zoos: Assessment and Strategic Actions' by the Central Zoo Authority (CZA) highlighted a gap in conservation breeding for the Endangered Himalayan Musk Deer in Indian zoos.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Indravati River ---
        {
            "id": 25071,
            "question_text": "The Indravati River, after which Indravati National Park is named, is a tributary of which major river?",
            "option_a": "Krishna",
            "option_b": "Mahanadi",
            "option_c": "Narmada",
            "option_d": "Godavari",
            "correct_answer": "D",
            "explanation": "The Indravati River is a tributary of the Godavari River. It originates from the Dandakaranya range in Odisha and forms the northern and western boundaries of Indravati National Park in Chhattisgarh.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- WPA ---
        {
            "id": 25072,
            "question_text": "Under India's Wildlife Protection Act 1972, a Wildlife Sanctuary can be declared by which authority?",
            "option_a": "Central Government only",
            "option_b": "State Government only",
            "option_c": "State Government, and Central Government can also declare a National Park",
            "option_d": "District Collector with state approval",
            "correct_answer": "C",
            "explanation": "Under the Wildlife Protection Act 1972, Wildlife Sanctuaries are notified by state governments. However, the Central Government can also declare a National Park. No legislation by the state assembly is needed; declaration is by notification.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Tiger Census schedule ---
        {
            "id": 25073,
            "question_text": "The All India Tiger Estimation (AITE) is conducted once every how many years?",
            "option_a": "2 years",
            "option_b": "4 years",
            "option_c": "5 years",
            "option_d": "10 years",
            "correct_answer": "B",
            "explanation": "The All India Tiger Estimation (AITE) is conducted every 4 years. The 6th edition began in late 2025. The last (5th) estimation in 2022 showed 3,682 tigers, up from 2,967 in 2018.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- COP29 India response ---
        {
            "id": 25074,
            "question_text": "India's reaction to the $300 billion climate finance goal set at COP29 Baku 2024 was to describe it as?",
            "option_a": "A landmark achievement",
            "option_b": "An insufficient but positive step",
            "option_c": "Abysmally poor",
            "option_d": "Highly ambitious",
            "correct_answer": "C",
            "explanation": "India strongly criticized the $300 billion/year by 2035 climate finance goal agreed at COP29 Baku, calling it 'abysmally poor' and insufficient to address climate change. Developing countries broadly expressed discontent with the outcome.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Project Tiger launch ---
        {
            "id": 25075,
            "question_text": "In which year was Project Tiger launched in India?",
            "option_a": "1969",
            "option_b": "1973",
            "option_c": "1980",
            "option_d": "1985",
            "correct_answer": "B",
            "explanation": "Project Tiger was launched in India in 1973. It is managed by the National Tiger Conservation Authority (NTCA) under the Ministry of Environment, Forests and Climate Change (MoEFCC). India now has 58 Tiger Reserves.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Simsang River ---
        {
            "id": 25076,
            "question_text": "The Simsang River system, where the new fish species Channa nachi was discovered, is in which state?",
            "option_a": "Assam",
            "option_b": "Manipur",
            "option_c": "Meghalaya",
            "option_d": "Tripura",
            "correct_answer": "C",
            "explanation": "Channa nachi was discovered in a shallow slow-flowing stream near Chokpot village, which is part of the Simsang River system in Meghalaya. The Simsang River is a major river of the Garo Hills region.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Mangroves ---
        {
            "id": 25077,
            "question_text": "India's Sundarbans mangrove forest, a UNESCO World Heritage Site, is located in which state?",
            "option_a": "Odisha",
            "option_b": "Andhra Pradesh",
            "option_c": "West Bengal",
            "option_d": "Tamil Nadu",
            "correct_answer": "C",
            "explanation": "The Sundarbans, the world's largest mangrove forest, is located in West Bengal (and extends into Bangladesh). It is a UNESCO World Heritage Site and home to the Royal Bengal Tiger. India has the world's second-largest mangrove area.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Project Dolphin ---
        {
            "id": 25078,
            "question_text": "Project Dolphin was launched in India in which year for the conservation of Gangetic and Irrawaddy dolphins?",
            "option_a": "2015",
            "option_b": "2018",
            "option_c": "2020",
            "option_d": "2022",
            "correct_answer": "C",
            "explanation": "Project Dolphin was launched in India in 2020 for the conservation of Gangetic and Irrawaddy dolphins. A landmark under this project was the satellite-tagging of the first Ganges River Dolphin in Assam on December 18, 2024.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Indian Rhino Vision ---
        {
            "id": 25079,
            "question_text": "The 'Indian Rhino Vision 2020' programme is associated with which wildlife sanctuary that has the highest density of Greater One-Horned Rhinoceros?",
            "option_a": "Kaziranga NP",
            "option_b": "Manas NP",
            "option_c": "Pobitora WLS",
            "option_d": "Orang NP",
            "correct_answer": "C",
            "explanation": "Pobitora Wildlife Sanctuary in Assam is part of the Indian Rhino Vision 2020 program and has the highest density of Greater One-Horned Rhinoceros in India. The sanctuary spans 48.81 sq km in eastern Guwahati.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Eusauropod ---
        {
            "id": 25080,
            "question_text": "Jinchuanloong niedu, a new genus of eusauropod dinosaur discovered from a fossil in Gansu Province, China, dates to which geological period?",
            "option_a": "Late Cretaceous (~70 million years ago)",
            "option_b": "Early Jurassic (~200 million years ago)",
            "option_c": "Middle Jurassic (~165 million years ago)",
            "option_d": "Triassic (~230 million years ago)",
            "correct_answer": "C",
            "explanation": "Jinchuanloong niedu is a new genus of eusauropod dinosaur whose fossil was found in the lower Xinhe Formation near Jinchang city, Gansu Province, China, dating to the Middle Jurassic period, approximately 165 million years ago.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
    ]

    for q in questions:
        cur.execute(
            f"""INSERT OR IGNORE INTO questions
                (id, question_text, option_a, option_b, option_c, option_d,
                 correct_answer, explanation, folder, topic)
                VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
            (q["id"], q["question_text"], q["option_a"], q["option_b"],
             q["option_c"], q["option_d"], q["correct_answer"],
             q["explanation"], q["folder"], q["topic"])
        )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed()
    print("Environment & Climate MCQs seeded: IDs 25001–25080")
