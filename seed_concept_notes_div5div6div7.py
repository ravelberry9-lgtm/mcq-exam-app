"""
seed_concept_notes_div5div6div7.py
===================================
Rich concept notes for AP Current Affairs Divisions 5, 6, 7.
Sources (ground truth — HTML notes):
  div05_arts_culture.html
  div06_economy_industries.html
  div07_history_freedom_fighters.html

Created: 2026-05-18
All facts cite the HTML source files above. NO invented data.

Usage:
    from mcq_app.seed_concept_notes_div5div6div7 import seed
    seed()
"""


def seed():
    from app import get_db
    db = get_db()
    db.autocommit = True
    cur = db.cursor()

    notes = [

        # ================================================================
        # DIV 5 — AP ARTS & CULTURE
        # ================================================================

        {
            'tag': 'gi_tag_concept',
            'title': 'GI Tag — Geographical Indication (భౌగోళిక సూచన గుర్తు)',
            'body': '''GI Tag (Geographical Indication) — Overview
=============================================
Legal basis: TRIPS Agreement (1994) + India's GI of Goods (Registration & Protection) Act, 1999
Registered at: Geographical Indications Registry, Chennai
Validity: 10 years (renewable)

Key distinction:
- Patent: protects an individual/company invention
- GI Tag: protects the entire regional community's product

Why important:
- Prevents counterfeit goods using the name
- Provides economic security to artisans
- Example: "Tirupati Laddu" name can only be used by TTD; unauthorized use = legal violation

AP Total GI Tags: 21
  - Handicrafts (హస్తకళలు): 15
  - Food/Agricultural (ఆహారం): 6

Exam trick: Kalamkari has TWO separate GI tags — Srikalahasti style and Machilipatnam style are registered separately.''',
            'tags_json': '["GI Tag","Geographical Indication","Handicrafts","AP"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_gi_tags_complete_list',
            'title': 'AP GI Tags — Complete List (21 Tags)',
            'body': '''AP GI Tags — Complete List
===========================
Total: 21 (15 Handicrafts + 6 Food/Agricultural)

HANDICRAFTS (15):
1. Srikalahasti Kalamkari — Srikalahasti, Tirupati district; hand-drawn; mythological scenes
2. Machilipatnam Kalamkari — Machilipatnam, Krishna district; block printing; floral & geometric
3. Tolu Bommalata — AP Leather Puppetry; GI tag; animal leather (goat skin) semi-transparent figures
4. Kondapalli Bommalu — Kondapalli, Krishna district; Ponniki (Albizzia lebbeck) wood; 16th century
5. Etikoppaka Bommalu — Etikoppaka, Alluri Sitarama Raju district; 400+ years; lac varnish finish
6. Uppada Jamdani Saree — Uppada, East Godavari; double-sided identical design (unique in world)
7. Venkatagiri Sarees — Venkatagiri, Nellore; gold zari; very fine weave
8. Dharmavaram Pattu Sarees — Dharmavaram, Anantapur; gold zari; traditional patterns
9. Mangalagiri Sarees — Mangalagiri, Guntur; distinctive dark border; thick cotton
10. Bobbili Veena — Bobbili, Vizianagaram district; made from single jackfruit log (ekandi veena)
11. Buditi Ganta & Brass (ఇత్తడి) — traditional bells and brassware
12. Udayagiri Knife (ఉదయగిరి చాకు-కత్తి) — Udayagiri, Nellore district
13. Durgi Stone Sculptures — Durgi, Guntur district
14. Allagadda Stone Sculptures — Allagadda, Kurnool district
15. Narsapur Crochet Lace — Narsapur, West Godavari (Dr. B.R. Ambedkar Konaseema)

FOOD / AGRICULTURAL (6):
1. Tirupati Laddu — TTD (Tirumala Tirupati Devasthanams); most famous GI
2. Bandaru Laddu (Banadar) — Machilipatnam, Krishna district
3. Atreyapuram Pootharekulu — Atreyapuram, Konaseema district; rice paper + jaggery; see-through thin
4. Guntur Sannam Mirchi — Guntur district; premium red chilli variety; exports worldwide
5. Banganapalle Mango — Banganapalle, Nandyal district; low fibre; sweet; thin skin
6. Araku Valley Arabica Coffee — Alluri Sitarama Raju + Parvathipuram Manyam districts; shade-grown; organic; tribal cultivation

District GI Map (key):
Krishna: Kondapalli Bommalu + Machilipatnam Kalamkari + Bandaru Laddu
East Godavari: Uppada Jamdani
Vizianagaram: Bobbili Veena
Nellore: Venkatagiri Sarees + Udayagiri Knife
Anantapur: Dharmavaram Pattu
Guntur: Mangalagiri + Durgi Sculptures + Guntur Mirchi
Tirupati: Tirupati Laddu + Srikalahasti Kalamkari
Kurnool: Allagadda Sculptures
Nandyal: Banganapalle Mango
Konaseema: Atreyapuram Pootharekulu
Alluri SR Raju: Etikoppaka Bommalu + Araku Coffee''',
            'tags_json': '["GI Tag","AP","Handicrafts","Food","Kalamkari","Kuchipudi"]',
            'lang': 'en'
        },

        {
            'tag': 'kuchipudi_classical_dance',
            'title': 'Kuchipudi Classical Dance — Full Profile',
            'body': '''Kuchipudi — AP Classical Dance Form
======================================
Origin: Kuchipudi village, Krishna district, Andhra Pradesh
Founded: 17th century under guidance of Siddhendra Yogi
Originally performed by: Brahmin boys in temple precincts; later on stage

Three components:
1. Nritta — pure rhythmic movement (no expression/emotion)
2. Nritya — expressive dance with bhava/rasa (emotion)
3. Natya — dramatic element with story, characters, dialogue

Unique feature: Plate Dance (Tarangam) — dancer balances pot of milk on head, feet on rim of brass plate while dancing. Found ONLY in Kuchipudi worldwide.

UNESCO Recognition:
- Year: 2008
- Category: Intangible Cultural Heritage (ICH) of Humanity
- Convention: UNESCO 2003 Convention for Safeguarding ICH
- Distinction: ICH (dance/knowledge) ≠ World Heritage Site (buildings/monuments like Taj Mahal)

Guinness World Record:
- 7,002 dancers — AP Social Welfare Residential Educational Institutions Society
- Venue: Andhra University grounds, Visakhapatnam
- Date: April 11, 2017
- This is the AP-held record (not the Hyderabad 2023 record of 3,782 by Telangana)

Prominent artists:
- Vempati Chinasatyam — brought Kuchipudi to national stage
- Yamini Krishnamurti, Shobha Naidu, Radha Reddy & Raja Reddy (Padma Bhushan)
- Deepika Reddy — Padma Shri 2026; 5 decades of Kuchipudi promotion worldwide''',
            'tags_json': '["Kuchipudi","UNESCO","Classical Dance","GI","ICH","Guinness"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_folk_arts_overview',
            'title': 'AP Folk Arts — Dappu, Burrakatha, Harikatha, Dhimsa',
            'body': '''AP Folk Arts Overview
======================
1. DAPPU (డప్పు)
- Single-sided percussion instrument (charmavadyam); played by SC communities (Madiga, Mala)
- Occasions: festivals, processions, weddings
- 2025 Guinness Record: 2,000+ Dappu artists performing simultaneously
  Venue: Vijayawada Utsav 2025 — Dussehra Carnival Walk
  Route: Indira Gandhi Maidan → Benji Circle (3 km)
  Date: September 22, 2025
  Certificate: Presented to CM Nara Chandrababu Naidu

2. BURRAKATHA (బుర్రకథ)
- "Burra" = a gourd-shaped instrument; "Katha" = story
- Three performers: Lead storyteller (Kathaakudu) + Rajaa (jester, left) + Haasyakaadu (comic, right)
- Historical significance: Used in 1940s–50s to spread independence movement messages
- Recognized by APCBL (Andhra Pradesh Cultural Bureau of Literature)

3. HARIKATHA (హరికథ)
- "Hari" = Vishnu; "Katha" = story
- Solo performance: one artist combines story + song + dance + humor + philosophy
- Instrument: Tambura
- Duration: 4–6 hours per performance; audience interaction is integral
- Mainly Bhagavatam stories

4. DHIMSA DANCE (దిమ్సా)
- Tribal women's folk dance of Visakhapatnam Agency (Parvathipuram Manyam, Alluri SR Raju districts)
- "Dhimsa" = "to play/dance" in tribal language
- Women form a crescent/semi-circle, arms on each other's shoulders
- Occasion: nature worship, harvest festivals
- Instruments: pithala (brass instruments) — Kiridi

5. KOLATTAM (కోలాటం)
- "Kola" = stick; "aatam" = play
- Group dance (8–40 participants); each holds two sticks or chains
- Beat sticks together while moving in circle; mostly performed by women
- Occasions: Deepawali, Sankranti, weddings

6. YAKSHAGANA (యక్షగానం)
- Musical drama with elaborate costumes; predominantly East & West Godavari districts

7. LAMBADI DANCE (లంబాడీ నృత్యం)
- Banjara (Sugali/Lambada) women's traditional dance; colorful embroidered dress with mirrors''',
            'tags_json': '["Folk Arts","Dappu","Burrakatha","Dhimsa","Kolattam","AP","Guinness"]',
            'lang': 'en'
        },

        {
            'tag': 'vijayawada_utsav_2025_guinness',
            'title': 'Vijayawada Utsav 2025 — Dappu Guinness Record',
            'body': '''Vijayawada Utsav 2025 — Dappu Guinness World Record
=====================================================
Event: Vijayawada Utsav 2025 (Vijayawada Dussehra Carnival Walk)
Start date: September 22, 2025
Duration: 11 days
Total events: 284 programs
Artists: 3,000+ (including 2,000+ Dappu artists)

Guinness Record achieved:
- Category: Largest Dappu Assembly (largest percussion folk artist procession)
- Dappu artists: 2,000+
- Route: Indira Gandhi Maidan → Benji Circle (3 km)
- Guinness certificate presented to CM Nara Chandrababu Naidu

Art forms displayed:
Dappu, Nasik Drums, Kalika, Lambadi, Dhimsa, Kolattam, Kuchipudi, Kathakali, Aghora, Gorilla Dance

Significance: First time such a large-scale carnival walk (like those held in foreign countries) was held in Vijayawada''',
            'tags_json': '["Dappu","Guinness","Vijayawada","Utsav","Folk Arts","2025"]',
            'lang': 'en'
        },

        {
            'tag': 'kummari_saare_guinness',
            'title': "Kummari Saare Guinness Record — World's Smallest Motorized Potter's Wheel",
            'body': """Kummari Saare Guinness World Record
=====================================
Record category: World's Smallest Motorized Potter's Wheel
Artist: Thirumalaneedhi Sai (తిరుమలనీడి సాయి), Tuni, Kakinada district
Certification date: December 9, 2025

Dimensions:
- Length: 67 mm
- Width: 50 mm
- Height: 47 mm
- Weight: 91 grams

Materials used: Plastic sheet + DC motor + iron wheel + small battery
Assembled in: approximately 1 hour
Demonstration: Made a small clay pot with it

Process: Sai recorded video on June 10; sent to Guinness organizers; after multiple verifications, certificate issued December 9, 2025

Previous record by same artist:
- 2023: 33-gram world's smallest washing machine — also a Guinness record

Significance: Demonstrates AP artisanal innovation in traditional craft (pottery) using modern micro-engineering""",
            'tags_json': '["Guinness","Pottery","Kummari","Tuni","Kakinada","2025"]',
            'lang': 'en'
        },

        {
            'tag': 'unesco_tentative_list_2025_ap',
            'title': 'UNESCO Tentative List 2025 — Tirumala & Erra Matti Dibbalu (AP)',
            'body': '''UNESCO Tentative List — AP Sites (August 27, 2025)
====================================================
What is Tentative List?
- First step in UNESCO World Heritage Site nomination process
- Country must list sites on Tentative List before formal nomination
- Being on Tentative List ≠ World Heritage Site designation (that takes years more)
- Process: Tentative List → Nomination File → UNESCO World Heritage Committee review → WHS status

AP Sites Added (August 27, 2025):

1. TIRUMALA HILLS (తిరుమల కొండలు)
Location: Tirupati, Sri Satyasai district
Geological significance:
- Eparchaean Unconformity: 2.5 billion-year-old rocks meeting Proterozoic strata (unique geological contact)
- Silathoranam (సిలాతోరణం): Natural stone arch — 1.5 billion years old (one of world's oldest natural arches)
Category: Natural Heritage (geological)

2. ERRA MATTI DIBBALU (ఎర్రమట్టి దిబ్బలు)
Location: Bheemunipatnam (Bhimili), Visakhapatnam district
Area: 1,500 acres of coastal land
What it is: Red laterite sand dunes — red color due to iron oxidation (ferruginous sand)
Global uniqueness: Only 3 such coastal geomorphological formations in the world
National recognition: National Geo-Heritage Monument
First studied: 1886 by William King
Category: Natural Heritage (geomorphological)

India total: 7 sites added to UNESCO Tentative List in 2025 from India''',
            'tags_json': '["UNESCO","Tentative List","Tirumala","Erra Matti Dibbalu","Silathoranam","2025"]',
            'lang': 'en'
        },

        {
            'tag': 'telugu_cultural_centre_amaravati',
            'title': 'Telugu Cultural Centre — Amaravati (₹119.27 Crore)',
            'body': '''Telugu Cultural Centre — Amaravati
=====================================
Approval: CRDA 59th meeting, CM Chandrababu Naidu presiding
Date of approval: March 10, 2026

Financial details:
- Total cost: ₹119.27 crore
- Construction mode: EPC (Engineering, Procurement, Construction)

Location details:
- Area: 5 acres at Neerukonda, Amaravati
- Built-up area: 95,170 sq. ft.
- Structure: G+1 (Ground + 1 floor)
- Standard: Green Building norms

Facilities:
1. 2,000-seat air-conditioned Auditorium
2. 1,000-capacity Open-Air Theatre
3. Telugu Language Museum

Implementing agency: Amaravati Growth and Infrastructure Corporation
Purpose: Showcase Telugu cultural heritage to the world; anchor cultural identity of the new capital''',
            'tags_json': '["Telugu Cultural Centre","Amaravati","CRDA","Culture","2026"]',
            'lang': 'en'
        },

        {
            'tag': 'nettanna_bharosa_handloom',
            'title': 'Nettanna Bharosa — Handloom Weavers Support Scheme (₹25,000/year)',
            'body': '''Nettanna Bharosa Scheme — AP Handloom Support
================================================
Announced by: CM Nara Chandrababu Naidu
Date: August 7, 2025 (National Handloom Day — Jatiya Chenetha Dinotsavam)
Venue: Mangalagiri, Guntur district

Key benefits:
1. Annual financial support: ₹25,000 per handloom weaver family/year
2. Free electricity:
   - Handlooms (chenetha maggam): 200 units free
   - Power looms (maramaggam): 500 units free
3. GST reimbursement: 5% GST on handloom fabric paid by government (≈₹15 crore)

Budget: ₹193 crore per year (total scheme cost)

Additional announcement:
- Handloom Museum to be set up in Amaravati capital city

Context: National Handloom Day is observed on August 7 every year since 2015 (commemorating Swadeshi Movement launched August 7, 1905)

Exam point: ₹25,000 per family is the key number; announcement date August 7, 2025''',
            'tags_json': '["Handloom","Nettanna Bharosa","AP","Weavers","2025","Mangalagiri"]',
            'lang': 'en'
        },

        {
            'tag': 'avakai_festival_2026',
            'title': 'Avakai Festival — Amaravati Cinema, Culture & Literature Festival 2026',
            'body': '''Avakai Festival — January 2026
================================
Full name: Avakai: Amaravati Festival of Cinema, Culture & Literature
Dates: January 8–10, 2026 (3 days)
Venue: Punnami Ghat + Bhavani Island, Vijayawada

Scale:
- 28 special events/programs
- 4 workshops
- Entry: FREE (no ticket required)

Focus areas:
- Telugu Cinema
- Culture
- Food (Avakai = raw mango pickle, iconic Telugu food symbol)
- Literature

Significance: First major cultural festival of AP combining cinema, culture, literature, and food under one umbrella; reflects AP government's cultural promotion agenda for Amaravati''',
            'tags_json': '["Avakai","Festival","Vijayawada","Cinema","Culture","Literature","2026"]',
            'lang': 'en'
        },

        {
            'tag': 'padma_awards_ap_artists',
            'title': 'Padma Awards — AP Artists 2025 & 2026',
            'body': '''Padma Awards — AP Artists (2025 & 2026)
==========================================
Padma Award hierarchy:
1. Padma Vibhushan — highest (after Bharat Ratna)
2. Padma Bhushan — second highest
3. Padma Shri — third highest
Announced: Republic Day (January 26) each year

AP Artists Awarded:

2025 Awards:
- Nandamuri Balakrishna — Padma Bhushan — Field: Cinema/Art
  Career: 5 decades in Telugu cinema; son of legendary NTR

- Madugula Nagaphani Sharma — Padma Shri — Field: Art
  Profile: AP traditional artist

2026 Awards:
- Deepika Reddy — Padma Shri — Field: Kuchipudi Dance
  Achievement: 5 decades of promoting Kuchipudi dance worldwide
  Context: Brings Kuchipudi (UNESCO 2008 ICH) to global audiences

Key distinction:
- Balakrishna got Padma BHUSHAN (2nd highest) in 2025
- Deepika Reddy got Padma SHRI (3rd) in 2026''',
            'tags_json': '["Padma Award","Balakrishna","Deepika Reddy","AP","2025","2026","Kuchipudi"]',
            'lang': 'en'
        },

        {
            'tag': 'telugu_language_classical_status',
            'title': 'Telugu Language — Classical Language Status & Literature',
            'body': '''Telugu Language — Key Facts
==============================
Classical Language (శాస్త్రీయ భాష) status: Granted in 2008
Rank: 6th Indian language to receive Classical Language status
(After Tamil, Sanskrit, Kannada, Malayalam, Odia)

Eligibility criteria for Classical Language:
1. 1,500+ years of recorded history
2. Ancient literature considered a valuable heritage
3. Independent development (not borrowed from another language)

Famous nickname: "Italian of the East" — because all Telugu words end in vowels

Jnanpith Award winners from AP:
- Viswanatha Satyanarayana (1970) — "Ramayana Kalpavriksham"
- C. Narayana Reddy (1988) — "Visswambhara"

Key Telugu poets (exam table):
- Nannaya (11th c.) — Adi Kavi; first Telugu Mahabharata translation
- Tikkana (13th c.) — completed Mahabharata
- Potana (15th c.) — Srimad Bhagavatam (Telugu)
- Sri Krishna Devaraya (1509–1529) — "Andhrabhoja"; court had Ashtadiggajas poets''',
            'tags_json': '["Telugu","Classical Language","Literature","Jnanpith","2008"]',
            'lang': 'en'
        },

        # ================================================================
        # DIV 6 — AP ECONOMY, INDUSTRIES & INFRASTRUCTURE
        # ================================================================

        {
            'tag': 'ap_gsdp_snapshot_2024_25',
            'title': 'AP GSDP & Economy Snapshot 2024-25',
            'body': '''AP Economy — Key Numbers 2024-25
===================================
GSDP (current prices): ₹16.41 lakh crore
GSDP nominal growth: 12.5% (over 2023-24)
GSDP real growth rate: 8.21%
National rank (real growth): 7th in India

Share of national GDP: 4.72%
Population share: 3.78%
(AP produces more than its population proportion — key exam comparison)

Per capita income: ₹2,66,240
vs national average: 1.3× the national average
National economy rank: 9th in India

Budget 2025-26: ₹3,22,359 crore
GST collections (first 4 months of 2025-26): ₹16,754 crore (61% of annual target — exceeded estimates)

GSVA sectoral contribution (2024-25):
- Services (Tertiary): 41.64%
- Agriculture (Primary): 37.20%
- Industry (Secondary): 21.16%

Note: GSDP vs GSVA — GSVA excludes taxes; used for sectoral analysis''',
            'tags_json': '["GSDP","Economy","AP","Budget","2024","2025"]',
            'lang': 'en'
        },

        {
            'tag': 'swarnandhra_2047_vision',
            'title': 'Swarnandhra 2047 Vision Document — Targets & Launch',
            'body': '''Swarnandhra 2047 — Vision Document
=====================================
Launched by: CM Nara Chandrababu Naidu
Date: December 14, 2024
Context: 2047 = India's centenary of independence (Amrit Kaal)

Economic Targets (2024-25 vs 2047):
-----------------------------------
GSDP: ₹16.41 lakh crore (~$200 bn) → $2.4 Trillion
Per Capita Income: ₹2.66 lakh (~$3,200) → $43,000
Annual Growth Rate: 8.21% → 15% sustained annually

10 Guiding Principles:
1. Poverty elimination
2. Water security (river interlinking)
3. Agriculture-technology integration
4. Energy cost reduction
5. Global logistics hub
6. Deep-tech integration
7. Skill development
8. HRD (Human Resource Development)
9. Cleanliness / Sanitation
10. Green energy hub

Implementation:
- Vision Action Plan (VAP) Units in all 175 Assembly constituencies

Significance: Master blueprint for AP's transformation by 2047''',
            'tags_json': '["Swarnandhra","2047","Vision","Economy","Chandrababu","AP"]',
            'lang': 'en'
        },

        {
            'tag': 'amns_nakkapalli_steel_plant',
            'title': 'ArcelorMittal Nippon Steel (AMNS) — Nakkapalli Steel Plant',
            'body': '''AMNS — Greenfield Integrated Steel Plant
==========================================
Company: ArcelorMittal Nippon Steel India (AMNS India)
Project type: Greenfield Integrated Steel Plant

Location:
- Village: Rajayya Peta
- Mandal: Nakkapalli
- District: Anakapalli
- State: Andhra Pradesh

Investment: ₹1,50,000 crore (₹1.5 lakh crore)
Capacity: 24 MT (Million Tonnes) per annum — in two phases

Groundbreaking ceremony:
- Date: March 23, 2026
- Presided by: CM Nara Chandrababu Naidu

CM's quote at ceremony:
"Vishakha Ukku — Andhrula Hakku" — we fought and achieved Vizag Steel;
now without asking, India's largest single industry is coming to Nakkapalli.

Significance:
- One of the world's largest steel plants
- India's single largest industrial project
- Creates massive direct and indirect employment in Uttarandhra (North AP)
- Located near Visakhapatnam coast — raw materials can arrive by sea

Comparison: RINL (Vizag Steel Plant) is a separate CPSE (Central Public Sector Enterprise) under Ministry of Steel; AMNS is a private investment''',
            'tags_json': '["AMNS","ArcelorMittal","Nippon Steel","Nakkapalli","Anakapalli","Steel","Investment","2026"]',
            'lang': 'en'
        },

        {
            'tag': 'google_ai_hub_visakhapatnam',
            'title': 'Google AI Hub — Visakhapatnam ($15 Billion Investment)',
            'body': '''Google AI Hub — Visakhapatnam
================================
MoU signed: October 14, 2025
Venue of signing: Taj Mansingh Hotel, New Delhi

Attendees at signing:
- AP CM: Nara Chandrababu Naidu
- Union Finance Minister: Nirmala Sitharaman
- Union IT Minister: Ashwini Vaishnaw
- AP IT Minister: Nara Lokesh
- Google Cloud CEO: Thomas Kurian

Investment details:
- Amount: $15 billion (≈ ₹1.25 lakh crore)
- Duration: 5 years
- Location: Visakhapatnam, AP

Historic significance:
- "Largest AI Hub outside the United States" — America-sized AI hub in Vizag
- Will make Visakhapatnam a global AI destination

Context: Part of AP's broader technology investment drive alongside IBM Quantum (Amaravati) and BQRF''',
            'tags_json': '["Google","AI Hub","Visakhapatnam","Investment","2025","Thomas Kurian"]',
            'lang': 'en'
        },

        {
            'tag': 'ibm_quantum_bqrf_amaravati',
            'title': 'IBM Quantum Computer (AQCC) & BQRF — Amaravati Quantum Hub',
            'body': '''IBM Quantum Computer — Amaravati AQCC
=======================================
Approval: September 2025
Location: Amaravati Quantum Computing Centre (AQCC), Amaravati
Specifications: 133-Qubit Quantum Computer, 5K Gates
Installed by: IBM (at IBM's own expense)
Space provided: 2,000 sq. ft. at rent of ₹30 per sq. ft.

Significance:
- IBM installing quantum computer at its own cost in a government/academic facility
- Gives AP access to world-class quantum computing infrastructure

---

BQRF — Bharat Quantum Reference Facilities
============================================
Full name: Bharat Quantum Reference Facilities
Date inaugurated: April 14, 2026 (World Quantum Day)
Inaugurated by: CM Nara Chandrababu Naidu

Locations (India's FIRST Quantum Hardware Test Beds):
1. SRM University, Amaravati
2. Medha Towers, Vijayawada

What BQRF are: Small quantum computers built with indigenous (domestic) technology
Significance: India's first-ever quantum hardware test beds — manufactured in India

Combined significance of IBM + BQRF:
AP has two types of quantum systems —
(1) IBM's imported 133-qubit system (AQCC Amaravati) — high-end
(2) Domestically-built BQRF systems (SRM + Medha) — India's first indigenous quantum hardware''',
            'tags_json': '["IBM","Quantum","BQRF","Amaravati","Qubit","2025","2026","World Quantum Day"]',
            'lang': 'en'
        },

        {
            'tag': 'cii_ap_summit_2025',
            'title': 'CII-AP 30th Partnership Summit — November 2025, Visakhapatnam',
            'body': '''CII-AP 30th Partnership Summit — 2025
======================================
Event: CII-Andhra Pradesh 30th Partnership Summit
Dates: November 14–15, 2025
Venue: Visakhapatnam, AP
Organized by: CII (Confederation of Indian Industry) + AP Government

Key outcomes:
- Total investment agreements: ₹13.26 lakh crore
- MoUs signed: 613
- Employment opportunities: 16.31 lakh (1.631 million)
- Sectors covered: 12
- Countries represented: 45

Context:
- Largest CII-AP summit in 30-year history
- National and international industrialists came to understand AP's potential
- Reflects AP government's "red carpet for industries" policy
- Held just weeks after Google AI Hub MoU (October 14, 2025)

Exam tip:
- 613 MoUs | ₹13.26 lakh crore | 16.31 lakh jobs | 45 countries — all four numbers are frequently asked''',
            'tags_json': '["CII","Summit","Visakhapatnam","Investment","MoU","2025","AP"]',
            'lang': 'en'
        },

        {
            'tag': 'renew_power_ap_mou',
            'title': 'ReNew Power MoU — ₹82,000 Crore Renewable Energy Investment',
            'body': '''ReNew Power MoU — AP Renewable Energy
=======================================
Company: ReNew Power (India's largest renewable energy company)
MoU signed: November 2025 (during CII Summit period)
Investment committed: ₹82,000 crore
Sector: Renewable Energy (Solar + Wind projects in AP)

Context:
- Part of AP's push to become "Green Energy Hub"
- AP's current RE installed capacity: 9 GW
- AP's RE potential: 82.5 GW (Solar: 38 GW + Wind: 44 GW)
- Green Hydrogen target by 2030: 500 ktpa (kilo tonnes per annum) or 2 MT green ammonia

AP's RE Policy (2023):
- Target: 500 ktpa hydrogen OR 2 MT green ammonia
- Investment needed: $10–15 billion
- Implementation: NGEL + NREDCAP JV; 25 GW RE capacity''',
            'tags_json': '["ReNew Power","Renewable Energy","Investment","AP","Solar","Wind","2025"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_agriculture_rankings',
            'title': 'AP Agriculture Rankings — Cocoa, Shrimp, Crops',
            'body': '''AP Agriculture & Aquaculture Rankings
========================================
CROPS WHERE AP RANKS 1st IN INDIA:
- Chilli (Mirchi) — Guntur Sannam variety is world-renowned
- Cocoa (Chocolate crop) — 41% of India's total (47,060 hectares out of 1.14 lakh ha nationally)
  Source: Rajya Sabha, March 13, 2026 (Union Agriculture Minister Bhageerath Chaudhary)
- Oil Palm (Ayal Palm)
- Papaya
- Tomato
- Lemon (Nimma)

AP RANKS 2nd IN INDIA:
- Mango — (Banganapalle mango famous)
- Cashew (Jeedipappu)
- Sweet Orange

AP RANKS 4th IN INDIA:
- Coconut (Kobbari)

AQUACULTURE (Fisheries):
- AP is India's largest shrimp producer
- AP's share of national shrimp production: 70%
- AP's share of national fish+shrimp production: 10%
- Total production (2024-25): 41.3 lakh tonnes (4.13 MT)
- Marine exports (FY25): ₹28,466 crore ($3.21 billion)
- Total exports (FY25): ₹1,84,277 crore ($20.78 billion)

New investment in aquaculture:
- Kings Infra Ventures: India's first AI-driven Aquaculture Technology Park in AP (₹2,500 crore)''',
            'tags_json': '["Agriculture","AP","Cocoa","Shrimp","Aquaculture","Exports","Rankings"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_heavy_minerals_resources',
            'title': 'AP Heavy Minerals — 359.79 MT in 25 Deposits',
            'body': '''AP Heavy Minerals — Parliamentary Disclosure
==============================================
Source: Union Minister of Science & Technology Jitendra Singh, Lok Sabha, March 11, 2026

Total Heavy Mineral deposits in AP:
- Quantity: 359.79 Million Tonnes (MT)
- Number of deposits: 25
- Location: Mainly coastal districts (Srikakulam, Vizianagaram coast)

Mineral-wise breakdown:
1. Ilmenite (ఇల్మెనైట్): 178.75 MT — LARGEST deposit
2. Sillimanite: 81.85 MT
3. Garnet (గార్నెట్): 67.30 MT
4. Zircon: 12.75 MT
5. Rutile: 11.46 MT
6. Monazite: 4.05 MT

India total: 1,309 MT (8 states)
AP's share: 359.79 / 1,309 = ~27.5% of India's heavy minerals

Industrial uses:
- Ilmenite → titanium production, aerospace, paint (TiO2)
- Zircon → ceramics, semiconductors, nuclear
- Monazite → rare earth elements (restricted — Central Government controlled)
- Garnet → abrasives, water filtration

Note: AP Barites — AP ranks #1 in India AND in the world for Barites production
Barites location: Kadapa district''',
            'tags_json': '["Heavy Minerals","Ilmenite","Barites","AP","Mining","Coastal","2026"]',
            'lang': 'en'
        },

        {
            'tag': 'amaravati_capital_act_2026',
            'title': 'Amaravati Capital Act No.7/2026 — Legal Capital Status',
            'body': '''Amaravati Capital — Legal Recognition Act
==========================================
Full name: Andhra Pradesh Reorganisation (Amendment) Act, 2026
Act number: No. 7 of 2026

Legislative history:
- Lok Sabha approval: April 1, 2026
- Rajya Sabha approval: April 2, 2026
- Presidential assent: April 6, 2026 (President Droupadi Murmu)

Effective date: Retroactively from June 2, 2024 (date TDP government took power)

Background:
- AP Reorganisation Act 2014 bifurcated AP and Telangana
- Hyderabad remained joint capital for 10 years (until June 2, 2024)
- New AP needed a new designated capital
- This act formally names Amaravati as the capital city of AP

Physical details of Amaravati:
- Built on: 33,000 acres of farmer-donated land
- Location: Near Krishna River, Guntur district
- Conceived as: Greenfield planned capital city (like Chandigarh, Canberra)

Significance: Gives legal certainty to farmers who donated land and to investors who invested in Amaravati''',
            'tags_json': '["Amaravati","Capital","Act","2026","AP","Reorganisation","Legal"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_ports_airports_infrastructure',
            'title': 'AP Ports & Airports — Complete Infrastructure List',
            'body': '''AP Ports — Complete List
==========================
MAJOR PORT (Central Government):
- Visakhapatnam Port Authority (VPA) — India's largest Eastern Coast port

NON-MAJOR PORTS (State Government):
1. Krishnapatnam Port — 2nd largest non-major port; Electronics & Coal
2. Gangavaram Port — near Visakhapatnam; private
3. Kakinada Port — Oil & Gas; SEZ port
4. Rava Port — Dr. B.R. Ambedkar Konaseema district

GREENFIELD PORTS (Under Construction — PPP model):
1. Bhavanapadu — Srikakulam district
2. Ramayapatnam — Nellore district
3. Machilipatnam — Krishna district
4. Kakinada SEZ Port

AP Ports rank: 3rd highest cargo volume in India; 2nd among non-major ports

AP Airports — Complete List
============================
International Airports:
1. Visakhapatnam International Airport — AP's largest
2. Tirupati International Airport — pilgrimage center
3. Vijayawada International Airport — Gannavaram, Krishna district

Domestic Airports:
4. Rajahmundry — tourism hub
5. Donakonda — Prakasam district

Under Construction:
6. Bhogapuram Airport — near Visakhapatnam; GMR Group; Phase 1 target Jan-Jun 2026

National Highways:
- August 2, 2025: 29 NH projects launched (272 km) at Mangalagiri; ₹5,233+ crore
- Connects Sri City, Krishnapatnam Port, Tirupati Airport

APLINK: AP Logistics Infrastructure Corporation — coordinates ports, airports, roads, warehouses, industrial parks on single platform''',
            'tags_json': '["Ports","Airports","Infrastructure","AP","Visakhapatnam","Krishnapatnam","Bhogapuram"]',
            'lang': 'en'
        },

        # ================================================================
        # DIV 7 — AP HISTORY & FREEDOM FIGHTERS
        # ================================================================

        {
            'tag': 'ap_ancient_dynasties_timeline',
            'title': 'AP Ancient & Medieval Dynasties — Chronological Table',
            'body': '''AP Dynasties — Chronological Overview
========================================
1. SATAVAHANAS (సాతవాహనులు)
Period: 2nd century BCE – 2nd century CE
Capital: Amaravati (Dhanyakataka), Pratishthana (modern Paithan, Maharashtra)
Greatest ruler: Gautamiputra Satakarni — defeated Sakas, Pahlavas, Yavanas; called "Raja of Kings"
Cultural legacy: Built Amaravati Mahasthupa (Buddhist); Nasik Inscription (by his mother)
Key art: Amaravati Sculpture School — white marble; influenced South India, Sri Lanka, Southeast Asia

2. IKSHVAKUS (ఇక్ష్వాకులు)
Period: 3rd century CE
Capital: Vijayapuri (Nagarjunakonda)
Notable: Successors of Satavahanas; patronized Buddhism; Nagarjunakonda excavations

3. EASTERN CHALUKYAS OF VENGI (పూర్వ చాళుక్యులు)
Period: 7th century – 1130 CE
Capital: Vengi (near Eluru, West Godavari)
Legacy: Patrons of Telugu literature; term "Telugu Desam" originated in this era

4. KAKATIYAS (కాకతీయులు)
Period: 1000 – 1323 CE
Capital: Warangal (Orugallu)
Key rulers:
- Ganapati Deva (1199–1262) — unified Telugu regions
- Rudramadevi — first woman ruler of Telugu land; Marco Polo mentioned her
Notable monuments: Thousand Pillar Temple (Warangal); Warangal Fort
Fall: 1323 CE — defeated by Delhi Sultan Ghiyasuddin Tughlaq

5. VIJAYANAGARA EMPIRE (విజయనగర సామ్రాజ్యం)
Period: 1336 – 1646 CE
Capital: Hampi (Vijayanagara)
Founded by: Harihara I + Bukka Raya I (1336)
Greatest ruler: Sri Krishna Devaraya (1509–1529) — "Andhrabhoja"; Ashtadiggajas poets court; "Manucharitra"
Fall: Battle of Talikota (1565) — defeated by Deccan Sultanates coalition (Bijapur, Ahmadnagar, Bidar, Golconda)
Note: Hampi is now a UNESCO World Heritage Site (in Karnataka, on AP border)

6. REDDI KINGDOM (రెడ్డి రాజ్యం)
Period: 14th–15th century
Capital: Kondavidu
Region: Coastal Andhra; succeeded Vijayanagara in coastal areas

7. QUTB SHAHIS (కుతుబ్ షాహీలు)
Period: 1518 – 1687 CE
Capital: Golconda / Hyderabad
Legacy: Blend of Telugu and Persian culture; fell to Aurangzeb in 1687

8. NIZAMS (నిజాంలు)
Period: 1724 – 1948
Capital: Hyderabad
Dynasty: Asaf Jahi
End: 1948 Police Action (Operation Polo) — Hyderabad State merged into Indian Union''',
            'tags_json': '["Dynasties","History","AP","Satavahanas","Kakatiyas","Vijayanagara","Qutb Shahis"]',
            'lang': 'en'
        },

        {
            'tag': 'alluri_sitarama_raju_profile',
            'title': 'Alluri Sitarama Raju — Manyam Veerudu (Freedom Fighter)',
            'body': '''Alluri Sitarama Raju — Full Profile
======================================
Born: May 4, 1897 (some sources say 1898)
Birthplace: Pandragi village, Visakhapatnam district
Died: May 7, 1924 — Koyyuru, East Godavari district (now Alluri Sitarama Raju district)
Cause of death: Shot by British police

Title: "Manyam Veerudu" (మన్యం వీరుడు) — Hero of the Forest/Tribal region

Rampa Rebellion (రంప తిరుగుబాటు):
- Period: 1922–1924
- Region: Visakhapatnam and East Godavari tribal areas (Agency/hill regions)
- Cause: Against oppressive British forest laws that restricted tribal people from collecting forest produce
- Method: Armed resistance — initially bows, arrows, axes; later seized British rifles
- Notable attacks: Police stations at Chintapalli, Krishnadevipeta, Rajavommangi

Death:
- British police caught and shot him on May 7, 1924, at Koyyuru
- Aged 26–27 years

Modern recognition:
- 125th birth anniversary: 2022 — PM Narendra Modi unveiled 30-foot bronze statue at Bhimavaram
- Rampa Rebellion centenary: 2022
- Alluri Sitarama Raju district named after him (Visakhapatnam Agency split)

Exam caution:
- Birth MONTH = MAY (not July — July 4 is wrong)
- Birth year: 1897 OR 1898 — both acceptable
- Death date: May 7, 1924 (exam often asks this)

Film connections: RRR (2022) — Ram Charan's character inspired by Alluri''',
            'tags_json': '["Alluri","Freedom Fighter","Rampa Rebellion","AP","Tribal","1922","1924"]',
            'lang': 'en'
        },

        {
            'tag': 'potti_sriramulu_profile',
            'title': 'Potti Sriramulu — Amarajeevi (Freedom Fighter & Andhra State Martyr)',
            'body': '''Potti Sriramulu — Full Profile
================================
Born: March 16, 1901
Birthplace: Madras (Chennai); ancestral home in Nellore/Prakasam area
(Note: Some textbooks cite Pallipad near Nellore, but birth city was Madras)

Died: December 15, 1952
Death city: Chennapattanam (Madras)
Death cause: 58th day of hunger strike

Title: "Amarajeevi" (అమరజీవి) — Immortal Soul

Gandhi connection:
- Potti Sriramulu was a devoted follower of Mahatma Gandhi
- Trained at Sabarmati Ashram
- Participated in Salt Satyagraha (Dandi March)

Hunger Strike for Separate Andhra State:
- Start date: October 19, 1952
- End date: December 15, 1952
- Duration: 58 days
- Demand: Separate Andhra State (separate from Madras Presidency)

Aftermath:
- His death caused massive public outrage and violence across Telugu regions
- PM Nehru announced acceptance of separate Andhra State on December 19, 1952
- Andhra State formed: October 1, 1953; Capital: Kurnool

Annual observance: December 15 = Amarajeevi Day (Amarajeevi Dinam) in AP

Key numbers:
- Birth: March 16, 1901
- Hunger strike start: October 19, 1952
- Death: December 15, 1952 (58th day)
- Andhra State formation: October 1, 1953''',
            'tags_json': '["Potti Sriramulu","Amarajeevi","Freedom Fighter","Andhra State","Hunger Strike","1952","1953"]',
            'lang': 'en'
        },

        {
            'tag': 'uyyalavada_narasimha_reddy_profile',
            'title': 'Uyyalavada Narasimha Reddy — 1846 Revolt (Pre-1857 Uprising)',
            'body': '''Uyyalavada Narasimha Reddy — Profile
======================================
Period: 1806–1847
Region: Kurnool district, Rayalaseema

Armed Revolt:
- Period: 1846–1847
- Region: Rayalaseema (Kurnool district)
- Against: British colonial rule; heavy taxation
- Significance: THIS REVOLT WAS 10 YEARS BEFORE THE 1857 SEPOY MUTINY
  — making it one of the earliest organized armed anti-British uprisings

British suppression:
- British officer Faiz Ali arrested him
- Executed (hanged) in Madras in 1847

Legacy:
- Kurnool district has a memorial complex being developed (2024 onwards)
- "1857 se pehle ka vidroh" — exam frequently asks this point

Film: "Sye Raa Narasimha Reddy" (2019) — Chiranjeevi starred in this biopic

Exam point:
- Revolt: 1846–47 (not 1857)
- 10 years BEFORE the First War of Independence
- Executed: 1847''',
            'tags_json': '["Uyyalavada","Freedom Fighter","1846","Rayalaseema","Kurnool","Pre-1857"]',
            'lang': 'en'
        },

        {
            'tag': 'prakasam_panthulu_profile',
            'title': 'Tanguturi Prakasam Panthulu — Andhra Kesari',
            'body': '''Tanguturi Prakasam Panthulu — Profile
=======================================
Born: 1872, Ongole, Prakasam district (then Nellore district)
Died: May 20, 1957

Title: "Andhra Kesari" (ఆంధ్ర కేసరి) — Lion of Andhra

Famous historic act:
- When British police pointed guns at him in the Assembly,
  he tore open his shirt and said "Shoot here!" (pointing to his chest)
- Became a symbol of fearlessness (nirbhayata)

Political career:
1. Chief Minister of Madras Presidency: 1946–1947
2. First Chief Minister of Andhra State: 1953–1954
   (When Andhra State was formed on October 1, 1953, Prakasam became the first CM)

Note: Prakasam Panthulu was CM of Andhra State (1953–54), not of Andhra Pradesh (which was formed 1956)
AP's first CM was Neelam Sanjeeva Reddy (November 1, 1956)''',
            'tags_json': '["Prakasam","Andhra Kesari","Freedom Fighter","Chief Minister","Andhra State","AP"]',
            'lang': 'en'
        },

        {
            'tag': 'kandukuri_veeresalingam_profile',
            'title': 'Kandukuri Veeresalingam — Social Reformer of AP',
            'body': '''Kandukuri Veeresalingam Panthulu — Profile
============================================
Born: April 16, 1848, Rajahmundry (East Godavari district)
Died: May 27, 1919

Title: Known as "Telugu Arya Bhata" and father of Telugu social reform

Key contributions:
1. Widow Remarriage Movement — organized and performed first widow remarriage in Telugu society (1881)
2. Women's Education — established schools for women
3. Social reforms — fought against child marriage, caste discrimination
4. Rationalist approach to religion and society

Literary works:
- "Rajasekhara Charitra" — credited as the first Telugu novel
- "Satyavadi" — Telugu newspaper/journal he edited

Historical significance:
- Among the first modern social reformers of Telugu society
- Inspired later freedom fighters and reformers
- Predated Gandhi's social work by several decades''',
            'tags_json': '["Kandukuri","Veeresalingam","Social Reform","Widow Remarriage","Telugu","History"]',
            'lang': 'en'
        },

        {
            'tag': 'arthur_cotton_irrigation_pioneer',
            'title': 'Sir Arthur Cotton — Irrigation Pioneer of AP',
            'body': '''Sir Arthur Cotton — Profile
=============================
Role: British irrigation engineer who built dams on AP rivers
Period of work in India: 19th century

Key projects:
1. Godavari Anicut (Dam) — 1847
   Location: Rajahmundry (Rajamahendravaram)
   Significance: Transformed Godavari delta agriculture; one of the most successful irrigation projects in Indian history

2. Krishna Anicut (Dam) — also constructed

Legacy:
- Credited with transforming Godavari and Krishna deltas into highly productive agricultural zones
- Statue at Rajahmundry in his honor — revered by local people
- Though British, he is celebrated in AP as a hero for agricultural development

Exam point: Godavari Dam = 1847 (NOT 1852; common error)''',
            'tags_json': '["Arthur Cotton","Irrigation","Godavari","Dam","1847","AP","British"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_state_formation_timeline',
            'title': 'AP State Formation — Complete Timeline (1920–2026)',
            'body': '''AP State Formation — Complete Chronological Timeline
======================================================
1920: Visakhapatnam Congress Session — first resolution demanding separate Andhra State

1946: Andhra movement intensified; Nehru gave assurance

Oct 19, 1952: Potti Sriramulu begins hunger strike in Madras (Chennai)

Dec 15, 1952: Potti Sriramulu dies on 58th day → massive public outrage

Dec 19, 1952: PM Nehru announces acceptance of separate Andhra State

Oct 1, 1953: ANDHRA STATE FORMED
- Separated from Madras Presidency
- Capital: KURNOOL
- First CM: Tanguturi Prakasam Panthulu

1955: Fazl Ali Commission (States Reorganisation Commission) report — recommends reorganization of states on linguistic basis

Nov 1, 1956: ANDHRA PRADESH STATE FORMED
- Andhra State + Telugu-speaking districts of Hyderabad State merged
- Capital: HYDERABAD
- First CM: Neelam Sanjeeva Reddy

1956: States Reorganisation Act 1956 implemented nationwide

June 2, 2014: AP BIFURCATION
- AP Reorganisation Act 2014
- AP + Telangana created as two separate states
- Hyderabad: Shared capital for 10 years (until June 2, 2024)
- New AP capital: Amaravati (announced)

Nov 1, 2024: AP Formation Day — 68th anniversary (1956 to 2024 = 68 years)

Apr 6, 2026: AP Reorganisation Amendment Act 2026 (No. 7/2026)
- Amaravati legally designated as AP's capital
- President Droupadi Murmu signed
- Retroactive from June 2, 2024

CRITICAL DISTINCTIONS:
Andhra State: Oct 1, 1953 | Capital: Kurnool | CM: Prakasam
Andhra Pradesh: Nov 1, 1956 | Capital: Hyderabad | CM: Neelam Sanjeeva Reddy
AP Formation Day = November 1 (celebrated annually)''',
            'tags_json': '["AP Formation","Andhra State","1953","1956","Potti Sriramulu","Kurnool","Hyderabad"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_key_personalities_quick_ref',
            'title': 'AP Key Personalities — Quick Reference (Neelam, Viswanatha, Arthur Cotton)',
            'body': '''AP Key Personalities — Quick Reference
========================================
1. NEELAM SANJEEVA REDDY
Role: AP's FIRST Chief Minister
Date: November 1, 1956 (when AP was formed)
Later: President of India (1977–1982)
Party: Indian National Congress

2. TANGUTURU PRAKASAM PANTHULU
Role: First CM of Andhra State (1953–54); NOT first CM of AP
Title: Andhra Kesari
Notable: "Shoot here!" moment of fearlessness

3. VISWANATHA SATYANARAYANA
Period: 1895–1976
Award: Jnanpith Award (1970)
Famous work: "Ramayana Kalpavriksham" (epic poem)
Title: Kavishri, Kavi Samrat

4. C. NARAYANA REDDY (Sinaare)
Period: 1931–2017
Award: Jnanpith Award (1988)
Famous work: "Visswambhara" (poem)
Also composed: Many Telugu film songs

5. SIR ARTHUR COTTON
Role: British irrigation engineer
Key project: Godavari Dam (1847) — transformed AP agriculture

6. DURGA BAI DESHMUKH
Born: Rajahmundry
Role: Women's education activist; Planning Commission member; Gandhian

7. BULLUSLU SAMBAMURTHI
Profile: Freedom fighter; politician; Kakinada (East Godavari) leader
Role: Speaker of Madras Legislative Assembly

8. KRISHNA DEVARAYA
Period: 1509–1529 CE
Empire: Vijayanagara
Title: "Andhrabhoja" (patron of Telugu arts/poetry)
Court: Ashtadiggajas (8 celebrated Telugu poets)
Poet himself: Wrote "Amuktamalyada" in Telugu''',
            'tags_json': '["Neelam","Prakasam","Viswanatha","AP","Chief Minister","Personalities","History"]',
            'lang': 'en'
        },

    ]

    for n in notes:
        cur.execute("""
            INSERT INTO concept_notes (tag, title, body, tags_json, lang)
            VALUES (%(tag)s, %(title)s, %(body)s, %(tags_json)s, %(lang)s)
            ON CONFLICT (tag) DO UPDATE
              SET title=EXCLUDED.title, body=EXCLUDED.body,
                  tags_json=EXCLUDED.tags_json, lang=EXCLUDED.lang
        """, n)

    cur.close()
    print(f'[div5div6div7 notes] seeded {len(notes)} concept notes')
