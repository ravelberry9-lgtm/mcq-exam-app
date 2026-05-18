"""
seed_concept_notes_div3div4.py
Question-specific concept notes for AP Current Affairs Divisions 3 & 4
Coverage: January 2025 – April 2026 (AP events only)

Each note is tagged to a specific MCQ topic. Facts drawn exclusively from:
  - div03_events_jan_aug2025.html
  - div04_events_aug2025_apr2026.html
"""


def seed():
    from app import get_db
    db = get_db()
    db.autocommit = True
    cur = db.cursor()

    notes = [
        # ─────────────────────────────────────────────────────────────────
        # DIVISION 3: JANUARY–AUGUST 2025
        # ─────────────────────────────────────────────────────────────────
        {
            'tag': 'pm_modi_vizag_jan8_2025',
            'title': 'PM Modi Visakhapatnam Visit — January 8, 2025',
            'body': '''PM Modi Vizag Visit — January 8, 2025
Date: January 8, 2025 (జనవరి 8, 2025)
Location: Andhra University Engineering College Grounds, Visakhapatnam

Projects launched (Foundation Stone / Inauguration):
1. NTPC Green Hydrogen Hub — ₹1,85,000 crore
   Location: Pudimadaka (పుడిమడక), near Visakhapatnam
   India's largest single Green Hydrogen investment
2. Road Projects — 10 projects worth ₹4,593 crore (శంకుస్థాపన)
3. Railway Projects — 6 projects worth ₹6,028 crore (శంకుస్థాపన)

Total Package: ₹2 lakh crore+ (₹1,85,000 + ₹4,593 + ₹6,028 crore)
Focus: Green Energy + Infrastructure (Roads + Railways)

Exam-critical numbers:
• NTPC Green H2 Hub = ₹1,85,000 crore (Pudimadaka)
• Road projects = 10, worth ₹4,593 crore
• Railway projects = 6, worth ₹6,028 crore
• Total = ₹2 lakh crore+

Context: This was PM Modi's first AP visit in 2025. The second AP visit was
May 2, 2025 at Amaravati (₹58,000 crore).''',
            'tags_json': '["PM Modi","Vizag","NTPC","Green Hydrogen","Infrastructure","Jan 2025"]',
            'lang': 'en'
        },

        {
            'tag': 'pm_modi_amaravati_may2_2025',
            'title': 'PM Modi Amaravati Visit — May 2, 2025 (₹58,000 Crore)',
            'body': '''PM Modi Amaravati Visit — May 2, 2025
Date: May 2, 2025 (మే 2, 2025)
Location: Amaravati, Andhra Pradesh

Projects launched (Foundation Stones):
1. AP Legislative Assembly Building (శాసనసభ భవనం) — foundation stone
2. AP High Court Building (హైకోర్టు భవనం) — foundation stone
3. AP Secretariat (సచివాలయం) — foundation stone
4. Amaravati World-Class Transport Network — 320 km roads — ₹17,400 crore
5. Land Pooling Scheme Roads — 1,281 km — ₹20,400 crore
6. DRDO Missile Testing Centre (రక్షణ సంస్థ) — first ever in AP

Total Package: ₹58,000 crore

Key differences between two visits:
• Jan 8 = Visakhapatnam — Green Energy + Roads + Railways (₹2 lakh crore+)
• May 2 = Amaravati — Legislature + Courts + Secretariat + Roads (₹58,000 crore)

Swarna Andhra@2047 Vision:
• Released: December 13, 2024
• Target: AP GDP = ₹308 lakh crore by 2047
• Annual Growth Rate target: 15%''',
            'tags_json': '["PM Modi","Amaravati","Capital","DRDO","Swarna Andhra","May 2025"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_budget_2025_26',
            'title': 'AP Budget 2025-26 — ₹3,22,359 Crore',
            'body': '''AP Budget 2025-26
Presented by: Payyavula Keshav (పయ్యావుల కేశవ్), Finance Minister, TDP
Date of Presentation: February 28, 2025 (ఫిబ్రవరి 28, 2025)
Budget Session Duration: February 24–28, 2025

Total Budget Size: ₹3,22,359 crore (రూ.3,22,359 కోట్లు)

Key Allocations:
• Talliki Vandanam (తల్లికి వందనం) = ₹9,407 crore
• Priority sectors: Amaravati construction, Super Six schemes,
  Infrastructure, Agriculture

Super Six Schemes (TDP election promises):
1. Talliki Vandanam — ₹15,000 per mother per student per year
2. Annadata Sukhibhava — ₹20,000 per farmer per year
3. Stree Shakti — Free bus travel for women
4. NTR Bharosa Pension — ₹4,000/month (elderly/disabled)
5. Yuva Vikasam — Employment for youth
6. Deepam-2 — Free LPG cylinders

Exam trick: Budget = ₹3,22,359 crore | Date = Feb 28, 2025 | FM = Payyavula Keshav''',
            'tags_json': '["AP Budget","Payyavula Keshav","Super Six","Talliki Vandanam","2025-26"]',
            'lang': 'en'
        },

        {
            'tag': 'rinl_vizag_steel_revival',
            'title': 'RINL Vizag Steel Plant Revival — ₹11,440 Crore',
            'body': '''RINL Vizag Steel Plant — Revival Package
Full Name: Rashtriya Ispat Nigam Limited (రాష్ట్రీయ ఇస్పాత్ నిగమ్ లిమిటెడ్)
Location: Gandhiagar area (గాంధీనగర్), Visakhapatnam
Significance: India's only coastal-shore integrated steel plant

Revival Package:
• Central Government funding: ₹11,440 crore (రూ.11,440 కోట్లు)
• Decision: TDP-BJP government reversed YSRCP-era privatisation plan

Blast Furnace Timeline:
• Early 2025: 2 Blast Furnaces restarted
• By August 2025: All 3 Blast Furnaces at full capacity

Workforce: 20,000+ employees (ఉద్యోగులు)

Historical context:
• YSRCP government had sought to privatise RINL
• TDP-BJP reversed the decision; Central govt committed ₹11,440 crore
• Major political issue in coastal AP due to employment at stake

Key exam numbers:
• Revival fund = ₹11,440 crore
• 3 Blast Furnaces by August 2025
• 20,000+ employees''',
            'tags_json': '["RINL","Vizag Steel","Blast Furnace","₹11440 crore","TDP","Revival"]',
            'lang': 'en'
        },

        {
            'tag': 'polavaram_project_funds',
            'title': 'Polavaram National Project — Central Funds 2025-26',
            'body': '''Polavaram National Project (పోలవరం జాతీయ ప్రాజెక్ట్)
River: Godavari (గోదావరి నది)
District: West Godavari (పశ్చిమ గోదావరి జిల్లా)
National Project Status: Since 2010 (2010 నుండి జాతీయ ప్రాజెక్ట్)

Significance: Central Government bears construction cost (not AP state)

Financial Details:
• Union Budget 2025-26 Allocation: ₹5,936 crore
• Pending Balance Grant (total unpaid): ₹12,157.53 crore

Benefits when completed:
• 36 TMC water storage
• 3.27 lakh acres irrigation
• Drinking water supply
• Hydroelectric power generation

Key exam trick:
• Central allocation (2025-26) = ₹5,936 crore
• Pending/Balance grant = ₹12,157.53 crore (do not confuse these two!)
• National Project since 2010 — Central govt funds construction''',
            'tags_json': '["Polavaram","Godavari","National Project","₹5936 crore","Irrigation","AP Water"]',
            'lang': 'en'
        },

        {
            'tag': 'yogandhra_2025_guinness',
            'title': 'Yogandhra 2025 — Guinness Record Yoga Event, Vizag (June 21)',
            'body': '''Yogandhra (యోగాంధ్ర) — International Yoga Day 2025
Date: June 21, 2025 (అంతర్జాతీయ యోగా దినోత్సవం)
Location: Visakhapatnam Beach Road
Route: RK Beach → Bheemunipatnam (28 km coastal stretch)

Key Numbers:
• Participants: 3,00,105 (3.01 lakh / 3.01 లక్షలు) — OFFICIAL GUINNESS COUNT
• IMPORTANT: The TARGET was 5 lakh participants; the ACTUAL/OFFICIAL count = 3,00,105
• Coastal stretch: 28 km (28 కి.మీ.)
• Guinness Record: World's Largest Open-Air Yoga Gathering (officially confirmed)

VIPs who participated:
• PM Narendra Modi
• CM Nara Chandrababu Naidu

Common mistake to avoid:
• WRONG: "5 lakh participants" (this was the target, not the record)
• CORRECT: 3,00,105 participants (Guinness-confirmed count)

Exam trick:
Date = June 21 | Location = Vizag 28 km coastline | Count = 3.01 lakh (3,00,105)
Record type = Largest Open-Air Yoga Gathering | Guinness = YES (officially confirmed)''',
            'tags_json': '["Yogandhra","Yoga Day","Guinness Record","Visakhapatnam","PM Modi","June 2025"]',
            'lang': 'en'
        },

        {
            'tag': 'ins_arnala_commission',
            'title': 'INS Arnala — India\'s First Shallow-Water ASW Corvette (June 2025)',
            'body': '''INS Arnala (INS అర్నాల) — Indian Navy
Commission date: June 19, 2025
Location: Naval Dockyard, Visakhapatnam
Command: Eastern Naval Command (తూర్పు నావల్ కమాండ్)

Senior Official at commissioning: Chief of Defence Staff General Anil Chauhan

Technical Specifications:
• Length: 77 metres (77 మీటర్లు)
• Displacement: 1,490+ tonnes (gross tonnage)
• Propulsion: Diesel Engine + Waterjet combination
  — Largest Indian Navy vessel to use this propulsion type (ఘనత)

Classification: Shallow-Water Anti-Submarine Warfare Craft (ASW-SWC)

Historic First:
• India's FIRST Shallow-Water ASW Corvette/Craft
• Largest Indian Navy vessel with Diesel Engine-Waterjet propulsion

Roles/Missions:
• Sub-Surface Surveillance
• Search and Rescue
• Low-Intensity Maritime Operations (LIMO)

Key exam numbers:
• Length = 77 metres | Weight = 1,490+ tonnes
• First Shallow-Water ASW = YES (India's first)
• Command = Eastern Naval Command, Visakhapatnam''',
            'tags_json': '["INS Arnala","Navy","ASW","Corvette","Visakhapatnam","Eastern Naval Command","June 2025"]',
            'lang': 'en'
        },

        {
            'tag': 'super_six_launch_dates_2025',
            'title': 'Super Six Scheme Launch Dates 2025 — Talliki Vandanam, Annadata, Stree Shakti',
            'body': '''Super Six Scheme Launch Dates (2025)

1. TALLIKI VANDANAM (తల్లికి వందనం) — June 12, 2025
   • Occasion: Government's 1st Anniversary (June 12, 2024 → 2025)
   • Benefit: ₹15,000 per mother per government school student per year
   • Beneficiaries: 69.16 lakh mothers (69.16 లక్షల తల్లులు)
   • Mode: Direct Bank Transfer

2. ANNADATA SUKHIBHAVA (అన్నదాత సుఖీభవ) — August 2, 2025
   • Amount: ₹20,000 per farmer per year (రైతుకు సంవత్సరానికి ₹20,000)
   • First instalment release: ₹3,175 crore to 46.86 lakh farmers
   • Launch location: East Veerayyapalem, Darsi Mandal, Prakasam District
   • Breakdown: State ₹14,000 + PM KISAN ₹6,000 = ₹20,000

3. STREE SHAKTI (స్త్రీ శక్తి) — Free Bus Scheme — August 15, 2025
   • Free bus travel for women and Transgender persons on all APSRTC buses
   • Official naming: The free bus scheme was given the official name "Stree Shakti"
     on August 15, 2025 (its 1st anniversary); scheme itself started August 15, 2024
   • 5 bus categories covered: Palle Velugu, Ultra Palle Velugu,
     City Ordinary, Metro Express, Express
   • VIPs who traveled by bus: CM Naidu, Deputy CM Pawan Kalyan, Minister Lokesh

Exam trick:
• June 12 = Talliki Vandanam | Aug 2 = Annadata | Aug 15 = Stree Shakti official naming
• Annadata launch district = Prakasam (Darsi Mandal)''',
            'tags_json': '["Super Six","Talliki Vandanam","Annadata Sukhibhava","Stree Shakti","TDP","AP Schemes 2025"]',
            'lang': 'en'
        },

        {
            'tag': 'bhishma_aiims_mangalagiri',
            'title': 'BHISHMA / Arogya Maitri Cube — AIIMS Mangalagiri (July 19, 2025)',
            'body': '''BHISHMA — Bharat Health Initiative for Sahayog, Hita and Maitri
Also known as: Arogya Maitri Cube (ఆరోగ్య మైత్రి క్యూబ్)
Date in AP: July 19, 2025
Location: AIIMS Mangalagiri, Guntur District (AIIMS మంగళగిరి)

AP allocation: 3 BHISHMA units deployed at AIIMS Mangalagiri

Joint initiative by:
• Ministry of Defence + Ministry of Health and Family Welfare

Technical specifications:
• Comprises 72 mini-cubes forming a mini hospital
• Total weight: 1 tonne (1 టన్ను)
• Deployment time: 10 minutes (10 నిమిషాల్లో ఆసుపత్రి)
• Transport modes: Road, Drone, Parachute, Helicopter

Use case: Disaster management, emergency medical services in remote areas
Concept: Portable hospital that can be rapidly deployed anywhere

Key exam numbers:
• 72 cubes | 1 tonne weight | Deployed in 10 minutes
• AP location = AIIMS Mangalagiri
• AP units = 3 BHISHMA units
• Date in AP = July 19, 2025''',
            'tags_json': '["BHISHMA","Arogya Maitri","AIIMS Mangalagiri","Disaster Management","Portable Hospital"]',
            'lang': 'en'
        },

        {
            'tag': 'nethanna_bharosa_handloom_day_2025',
            'title': 'Nethanna Bharosa & Handloom Museum — August 7, 2025',
            'body': '''Nethanna Bharosa (నేత్తన్న భరోసా) — Weaver Support Scheme
Date: August 7, 2025 (11th National Handloom Day / జాతీయ హాండ్‌లూమ్ దినోత్సవం)
Location: Mangalagiri, Guntur District

Annual assistance: ₹25,000 per weaver family per year (₹25,000/చేనేత కుటుంబం/సంవత్సరం)

Free Electricity provisions:
• Handlooms (మగ్గాలు): 200 units free per month
• Power looms (మరమగ్గాలు): 500 units free per month
• Annual cost to government: ₹193 crore

GST reimbursement:
• Government reimburses 5% GST on handloom fabrics
• ₹15 crore released for this

Handloom Museum announcement:
• CM Chandrababu announced setting up a Handloom Museum in Amaravati

Weaversala Project:
• Led by Minister Nara Lokesh
• Digital platform to promote handloom products

Additional scheme on same day (related to division 3 notes):
• Swachh Survekshan Awards 2024 for AP — July 12, 2025
  (5 AP cities won Super Swachh League Cities awards)

Exam trick:
• Date = Aug 7, 2025 | Amount = ₹25,000/family
• Free electricity: Handloom = 200 units | Power loom = 500 units
• Location = Mangalagiri | Handloom Museum = Amaravati (announced)''',
            'tags_json': '["Nethanna Bharosa","Handloom","Weavers","August 7","National Handloom Day","₹25000","Amaravati Museum"]',
            'lang': 'en'
        },

        {
            'tag': 'quantum_valley_amaravati_overview',
            'title': 'Amaravati Quantum Valley — Full Timeline (Aug 2025 to Apr 2026)',
            'body': '''Amaravati Quantum Valley (అమరావతి క్వాంటం వ్యాలీ)
Location: Amaravati, Andhra Pradesh

FULL TIMELINE (exam-critical):
• August 2025: LTIMindtree + 50+ companies joined; project planning began
  (This is Division 3 scope — idea/planning phase)
• November 2025: AP Quantum Computing Policy released
• February 7, 2026: FOUNDATION STONE laid by CM Chandrababu + Union Minister Jitendra Singh
• April 14, 2026: IBM Quantum System Two INAUGURATION target
  (World Quantum Day + Dr. Ambedkar Jayanti)

IBM Quantum System Two:
• Processor: 156-qubit Heron (IBM's most advanced quantum processor)
• Partners: IBM + TCS (Tata Consultancy Services) — KEY PARTNERS
  Also: L&T, CDAC, CDOT, IITs, 50+ organisations
• Significance: South Asia's most powerful quantum computer

Main quantum computer:
• IBM Quantum System Two with 156-qubit Heron processor — primary hardware
• Main partners: IBM (hardware) + TCS (IT services)
• Other partners: L&T, CDAC, CDOT, IITs, 50+ technology firms
• Foundation Stone: Feb 7, 2026 — CM Chandrababu + Union Minister Jitendra Singh
• Inauguration target: April 14, 2026 (World Quantum Day + Ambedkar Jayanti)

Timeline:
• Aug 2025: LTIMindtree + 50+ firms joined the initiative (planning phase)
• Nov 2025: AP Quantum Computing Policy released
• Feb 7, 2026: Foundation Stone laid
• Apr 14, 2026: Inauguration target

Common mistakes:
WRONG: "Microsoft Quantum / Google Sycamore is the builder" → CORRECT: IBM + TCS
WRONG: "August 2025 = inauguration" → CORRECT: Aug 2025 = planning; Inauguration = Apr 14, 2026
WRONG: "Foundation Stone 2025" → CORRECT: Foundation Stone = Feb 7, 2026

Time from idea to inauguration: ~8 months (August 2025 → April 2026 = record time)''',
            'tags_json': '["Quantum Valley","Amaravati","IBM","TCS","156-qubit","BQRF","Apr 2026","Heron processor"]',
            'lang': 'en'
        },

        # ─────────────────────────────────────────────────────────────────
        # DIVISION 4: AUGUST 2025 – APRIL 2026
        # ─────────────────────────────────────────────────────────────────

        {
            'tag': 'cii_30th_partnership_summit_2025',
            'title': 'CII 30th Partnership Summit — Visakhapatnam, Nov 14-15, 2025',
            'body': '''CII 30th Partnership Summit (30వ CII పార్టనర్‌షిప్ సమ్మిట్)
Organisation: CII = Confederation of Indian Industry
Edition: 30th (30వ ఎడిషన్)
Date: November 14-15, 2025 (నవంబర్ 14-15, 2025)
Location: Visakhapatnam, Andhra Pradesh

VIPs:
• Inaugurated by: Vice President C.P. Radhakrishnan (ఉప రాష్ట్రపతి)
• Presided: Piyush Goyal — Commerce & Industry Minister, GOI
• Co-chaired: CM Nara Chandrababu Naidu

Key Statistics:
• Countries participating: 45 countries (45 దేశాలు) — NOTE: NOT 61
• Delegates: 2,000+ delegates (2000 పైగా ప్రతినిధులు)
• Investment target: ₹10 lakh crore (₹10 లక్షల కోట్లు)

What is CII Partnership Summit?
CII (Confederation of Indian Industry) holds an annual international business
summit to attract investments into India. States compete to host it. The 30th
edition was held in AP — a major recognition for the state.

Common mistake: "61 countries" is WRONG → Correct = 45 countries (from HTML notes)

Exam trick:
• 30th edition | Vizag | Nov 14-15, 2025
• VP inaugurated | 45 countries | ₹10 lakh crore target
• CII = Confederation of Indian Industry (singular "Industry" not "Industries")''',
            'tags_json': '["CII","Partnership Summit","Visakhapatnam","VP Radhakrishnan","Investment","45 Countries","Nov 2025"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_28_districts_jan2026',
            'title': 'AP 28 Districts — Polavaram & Markapur New Districts (Jan 1, 2026)',
            'body': '''AP 28 Districts — Reorganisation 2026
Two new districts added: Polavaram and Markapur

KEY DATES (all three are separate events):
• December 29, 2025 = AP Cabinet approved 2 new districts
• December 31, 2025 = Official Gazette Notification issued
• January 1, 2026 = New districts became effective (అమల్లోకి వచ్చాయి)

New District 1: POLAVARAM DISTRICT
• HQ (Headquarters): Rampachodavaram (రాంపచోడవరం) — NOT Polavaram town
• Parent district: Carved from West Godavari/East Godavari region

New District 2: MARKAPUR DISTRICT
• HQ: Markapur
• Carved from: Prakasam District (ప్రకాశం జిల్లా నుండి విభజన)
  (Markapur + Kanigiri Revenue Divisions combined)

AP District History:
• Undivided AP (before 2014) → 23 districts
• After bifurcation 2014 → Residuary AP = 13 districts
• YSRCP, April 4, 2022 → 26 districts (carved 13 into 26)
• TDP-BJP, January 1, 2026 → 28 districts (added Polavaram + Markapur)

Exam critical mistakes to avoid:
WRONG: "AP has 26 districts" (after Jan 1, 2026 → 28 districts)
WRONG: "Cabinet approval date = Effective date" → Cabinet Dec 29, Effective Jan 1
WRONG: "Polavaram District HQ = Polavaram" → Correct HQ = Rampachodavaram''',
            'tags_json': '["AP Districts","28 Districts","Polavaram District","Markapur","Rampachodavaram","Jan 2026"]',
            'lang': 'en'
        },

        {
            'tag': 'potti_sriramulu_statue_amaravati',
            'title': 'Potti Sriramulu Balidana Vigraham — 58-ft Statue, Amaravati',
            'body': '''Potti Sriramulu Balidana Vigraham (బలిదాన విగ్రహం)
Announced by: CM Nara Chandrababu Naidu
Announcement date: December 15, 2025 (73rd Death Anniversary / వర్ధంతి)
Statue location: AMARAVATI (6.8 acres allocated) — NOT Nellore
Target inauguration: March 16, 2026 (Birth Anniversary / జన్మదినం)

Statue details:
• Name: Balidana Vigraham / Statue of Sacrifice (అమరాజీవి పొట్టి శ్రీరాముల స్మారకం)
• Height: 58 feet (58 అడుగులు) — Bronze statue
• Why 58 feet? He died on the 58th day of his hunger strike (Dec 15, 1952)

Potti Sriramulu — Key Facts:
• Born: March 16, 1901 — Nellore (నెల్లూరు జన్మస్థలం)
• Died: December 15, 1952 — on the 58th day of hunger strike — at Madanapalle
• Demand: Separate Telugu-speaking state (Andhra State)
• Result: Andhra State formed October 1, 1953
• AP Formation: November 1, 1956 (Andhra + Hyderabad combined)
• AP Foundation Day = November 1 (in honour of Potti Sriramulu's sacrifice)

Common mistakes:
WRONG: "Statue in Nellore" → Nellore = birthplace only; Statue = Amaravati
WRONG: "58 = his age" → 58 = days of hunger strike before death''',
            'tags_json': '["Potti Sriramulu","Statue","Amaravati","58 feet","Andhra State","Dec 15","Balidana"]',
            'lang': 'en'
        },

        {
            'tag': 'ifr_2026_visakhapatnam',
            'title': 'International Fleet Review (IFR) 2026 — Visakhapatnam, Feb 18, 2026',
            'body': '''International Fleet Review 2026 (అంతర్జాతీయ ఫ్లీట్ రివ్యూ)
Date: February 18, 2026 (ఫిబ్రవరి 18, 2026)
Location: Visakhapatnam (off the sea coast)
Theme: "United Through Oceans"

Who reviewed: President Droupadi Murmu
Reviewed from: INS Sumedha — an Indigenous Offshore Patrol Vessel (OPV)

Participating Nations: 74 countries (74 దేశాలు)
Naval Assets:
• 85 ships total (85 నౌకలు)
• 66 Indian ships + 19 foreign ships
• 3 submarines (submarines)
• 60+ aircraft

India's Ocean Vision announced: MAHASAGAR
Full form: Mutual and Holistic Advancement for Security and Growth Across Regions

India's IFR History (all 3):
• 1st IFR = 2001
• 2nd IFR = 2016
• 3rd IFR = 2026 (Visakhapatnam) ← exam answer

Why Visakhapatnam? It is home to Eastern Naval Command (HQ).

Note on theme: "United Through Oceans" was also the theme of IFR 2016 —
Indian Navy deliberately repeated it.

Exam trick:
Date = Feb 18, 2026 | 74 countries | 85 ships | "United Through Oceans"
Review vessel = INS Sumedha (OPV) | India's 3rd IFR''',
            'tags_json': '["IFR 2026","International Fleet Review","Visakhapatnam","President Murmu","INS Sumedha","MAHASAGAR","74 countries"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_reorganisation_amendment_act_2026',
            'title': 'AP Reorganisation (Amendment) Act 2026 — Amaravati Sole Capital',
            'body': '''AP Reorganisation (Amendment) Act, 2026
Passed by: Indian Parliament — April 2026 (ఏప్రిల్ 2026)
Section amended: Section 5 of AP Reorganisation Act, 2014
Key decision: Amaravati declared Sole and Permanent Capital of AP

Background — 3 Capitals Controversy:
YSRCP government (2019-2024) proposed 3 capitals:
• Amaravati = Legislative Capital (శాసన రాజధాని)
• Kurnool = Judicial Capital (న్యాయ రాజధాని)
• Visakhapatnam = Executive Capital (కార్యనిర్వాహక రాజధాని)

TDP-BJP government (from June 2024) reversed this:
• Decided Amaravati as the ONLY capital
• Got AP Assembly to pass unanimous resolution
• Got Parliament to pass Amendment Act (April 2026)

Legal chain:
• 2014: AP Reorganisation Act (original act — bifurcation of AP and TS)
• 2026: AP Reorganisation (Amendment) Act — Section 5 amended → Amaravati = Sole Capital

Exam trick:
• Section 5 of 2014 Act = Capital city provision
• 2026 Amendment = Amaravati only (not 3 capitals)
• YSRCP proposed 3 capitals; TDP reversed to 1 (Amaravati)''',
            'tags_json': '["AP Reorganisation Act","Amaravati","Capital","Amendment 2026","Section 5","YSRCP","3 Capitals"]',
            'lang': 'en'
        },

        {
            'tag': 'am_green_kakinada_green_ammonia',
            'title': 'AM Green Kakinada — World\'s Largest Green Ammonia Plant',
            'body': '''AM Green Kakinada — Green Ammonia Plant
Company: AM Green (subsidiary of Greenko Group, Hyderabad-based renewable energy company)
Location: Near Kakinada Port, on Nagarjuna Fertilisers site (495 acres)
Timeline: Announced/under construction ~ January 2026

Capacity: 1.5 MTPA (Million Tonnes Per Annum) — final target
Investment: ₹13,000 crore ($10 billion total project)
Record: World's Largest Green Ammonia Plant

Export markets:
• Germany (Uniper company partnership agreement)
• Japan
• Singapore

Jobs: 8,000+ during construction phase

What is Green Ammonia?
• Regular ammonia = made using fossil fuels (carbon-intensive)
• Green Ammonia = Renewable energy (solar/wind) → water electrolysis
  → Green Hydrogen → Haber-Bosch process → Ammonia (NH3)
• Carbon emissions = zero → hence "Green"

Significance:
• India exporting clean energy molecules to Europe/Asia for first time
• Part of India's Green Energy export strategy

Exam trick:
• World's Largest (not India's largest; not Asia's largest)
• 1.5 MTPA capacity | ₹13,000 crore
• AM Green = Greenko Group subsidiary
• Exports: Germany, Japan, Singapore''',
            'tags_json': '["AM Green","Green Ammonia","Kakinada","World Largest","Greenko","1.5 MTPA","₹13000 crore"]',
            'lang': 'en'
        },

        {
            'tag': 'auto_driverla_sevalo_2025',
            'title': 'Auto Driverla Sevalo — Oct 4, 2025 (₹15,000/year for Drivers)',
            'body': '''Auto Driverla Sevalo Scheme (ఆటో డ్రైవర్ల సేవాలో)
Launch date: October 4, 2025 (అక్టోబర్ 4, 2025)
Launched by: AP Government (TDP-BJP)
Former name: Vahana Mitra (వాహన మిత్ర) — renamed by TDP government

Benefits:
• Annual financial support: ₹15,000 per year (₹15,000 ఏటా)
• Eligible vehicles: Auto-rickshaws, Cabs (Taxis), Maxi Cabs
• Total eligible beneficiaries: 2.9 lakh drivers (2.9 లక్షల మంది)

Additional plan:
• Uber-style government app in pilot phase
• Pilot cities: Visakhapatnam and Vijayawada

Exam trick:
• Date = October 4, 2025 | Amount = ₹15,000/year
• 2.9 lakh beneficiary drivers
• Old name = Vahana Mitra; New name = Auto Driverla Sevalo
• For Auto, Cab, Maxi Cab drivers (not truck/bus drivers)''',
            'tags_json': '["Auto Drivers","Vahana Mitra","Auto Driverla Sevalo","₹15000","Oct 2025","TDP Scheme"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_dgp_cs_appointments_2025_26',
            'title': 'AP DGP & Chief Secretary Appointments 2025-26',
            'body': '''AP DGP — Harish Kumar Gupta
Current DGP: Harish Kumar Gupta (హరీష్ కుమార్ గుప్తా)
IPS Batch: 1992, AP cadre
Appointment as DGP: January 31, 2025
Tenure: 2 years fixed term (Supreme Court mandated)

DGP timeline:
• June 2024: TDP government appointed Ch. Dwarka Thirumal Rao (1989 batch) as DGP
• January 31, 2025: After Ch. Dwarka Thirumal Rao moved to APSRTC MD post,
  Harish Kumar Gupta became DGP again (he was earlier appointed by EC for elections)

AP Chief Secretary — Timeline 2024-2026:
1. Neerab Kumar Prasad (1987 IAS) — June 2024 to December 31, 2024
2. K. Vijayananд (K. విజయానంద్, 1992 IAS) — January 1, 2025 to February 28, 2026
   (got 3-month extension; original term ended November 30, 2025)
3. G. Sai Prasad (G. సాయి ప్రసాద్, 1991 IAS) — March 1, 2026 onwards

AP High Court Chief Justice:
• Justice Dhiraj Singh Thakur — CJ until April 24, 2026
• Justice Lisa Gill — Took oath March 13, 2026; became CJ April 25, 2026
• Justice Lisa Gill = AP HC's first woman Chief Justice

Exam trick:
• Current DGP = Harish Kumar Gupta (1992 IPS, from Jan 31, 2025)
• CS since Mar 1, 2026 = G. Sai Prasad (1991 IAS)
• AP HC first woman CJ = Justice Lisa Gill''',
            'tags_json': '["AP DGP","Harish Kumar Gupta","Chief Secretary","G Sai Prasad","K Vijayananд","AP HC","Lisa Gill"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_foundation_day_tdp_facts',
            'title': 'AP Foundation Day 2025 (69th) & TDP 44th Anniversary',
            'body': '''AP Foundation Day — November 1, 2025
Date: November 1, 2025
Anniversary: 69th Foundation Day (69వ రాష్ట్ర అవతరణ దినోత్సవం)
Calculation: AP formed November 1, 1956; 2025 − 1956 = 69 years

CRITICAL: Do NOT say 70th anniversary — that is November 1, 2026!

AP Formation history:
• October 1, 1953: Andhra State formed (Potti Sriramulu's sacrifice)
• November 1, 1956: Andhra Pradesh formed (Andhra + Hyderabad State merged)
• AP Foundation Day = November 1 (celebrates Nov 1, 1956 merger)

Telugu Desam Party (TDP):
• Founded: March 29, 1982
• Founder: N.T. Rama Rao (NTR)
• 2026 March = TDP's 44th Foundation Day (1982 → 2026 = 44 years)
• CM Chandrababu Naidu = NTR's son-in-law (NTR's daughter = Nara Bhuvaneswari)

ISTC @ IMU Visakhapatnam (September 20, 2025):
• Full name: International Seafarers Training Centre
• Location: Indian Maritime University (IMU) campus, Visakhapatnam
• Significance: First such advanced seafarers training centre in South Asia

AP Universal Health Policy (September 4, 2025):
• AP Cabinet approved Universal Health Policy on September 4, 2025
• Extension of Aarogya Sri / NTR Vaidya Seva
• Coverage: ₹25 lakh treatment (5 crore AP citizens)''',
            'tags_json': '["AP Foundation Day","69th","TDP","NTR","Chandrababu","ISTC Vizag","Universal Health","Nov 2025"]',
            'lang': 'en'
        },

        {
            'tag': 'bharatnet_ap_apbil',
            'title': 'BharatNet AP — ₹2,432 Crore (APBIL, Phase 3)',
            'body': '''BharatNet Project — Andhra Pradesh
Phase: BharatNet Phase 3 (Amended)
Funds allocated to AP: ₹2,432 crore (రూ.2,432 కోట్లు)
Timeline: Announced February 2026

Implementing agency: APBIL
Full form of APBIL: Andhra Pradesh BharatNet Infrastructure Limited

Funding source: Digital Bharat Nidhi (DBN) — renamed from USOF (Universal Service Obligation Fund)

Goal:
• Provide high-speed optical fiber broadband connectivity to all Gram Panchayats in AP
• Last-mile connectivity for rural Andhra Pradesh

BharatNet is a national programme:
• Nationwide: Connecting all gram panchayats with optical fiber
• AP's share: ₹2,432 crore

Exam trick:
• AP BharatNet fund = ₹2,432 crore
• Implementing body = APBIL (Andhra Pradesh BharatNet Infrastructure Limited)
• Funding = Digital Bharat Nidhi
• Purpose = Gram Panchayat broadband connectivity''',
            'tags_json': '["BharatNet","APBIL","₹2432 crore","Digital Bharat Nidhi","Rural Broadband","AP 2026"]',
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
    print(f'[div3div4 notes] seeded {len(notes)} concept notes')


if __name__ == '__main__':
    seed()
