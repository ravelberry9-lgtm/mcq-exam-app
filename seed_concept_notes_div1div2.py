"""
seed_concept_notes_div1div2.py
AP Current Affairs — Div 1 (Elections & Cabinet) + Div 2 (Govt Schemes)
Question-specific concept notes for all MCQ topics in div1 and div2.

All facts sourced from:
  - div01_elections_cabinet.html (Elections, Cabinet, Constitutional Positions)
  - div02_govt_schemes.html (Super Six, NTR Bharosa, Anna Canteen, etc.)

Created: 2026-05-18
"""


def seed():
    from app import get_db
    db = get_db()
    db.autocommit = True
    cur = db.cursor()

    notes = [

        # ─── DIV 1: ELECTIONS ───────────────────────────────────────────────────

        {
            'tag': 'ap_elections_2024_basic',
            'title': 'AP 2024 Assembly Election — Basic Facts',
            'body': '''2024 AP Legislative Assembly Election — Key Dates & Numbers

Voting Date:    May 13, 2024 (Monday)
Results Date:   June 4, 2024 (same day as Lok Sabha results)
Oath Ceremony:  June 12, 2024 (CM + 24 ministers, Vijayawada/Guntur)
Portfolio Allot: June 14, 2024

Total Assembly Seats: 175
Majority Mark:        88

Voter Turnout:        81.86%
Highest Turnout:      Darsi constituency — 90.91% (Prakasam district)
Lowest Turnout:       Tirupati constituency — 63.32%
Eligible Voters:      ~4.07 crore (approx. 40.7 million)

Note: AP Assembly election was held simultaneously with Lok Sabha 2024.
ECI conducted both on the same date.''',
            'tags_json': '["AP Elections 2024","Voting Date","Turnout","Assembly"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_elections_2024_results',
            'title': 'AP 2024 Election Results — Party-wise Seat Count',
            'body': '''AP 2024 Assembly Election Results (out of 175 seats)

TDP-JSP-BJP COALITION (కూటమి):
  TDP:  Contested 144 → Won 135  (vote share ~45.6%)
  JSP:  Contested  21 → Won  21  (100% strike rate — won ALL seats!)
  BJP:  Contested  10 → Won   8
  TOTAL COALITION: 164/175 seats (>55% vote share)

OPPOSITION:
  YSRCP: Contested 175 → Won 11  (vote share 39.37%)
           [2019: YSRCP won 151 — historic collapse]
  Congress: ~0 seats (~0.7% vote share)
  Others:   0 seats

EXAM TRICKS:
• JSP = 21/21 = 100% — perfect record!
• YSRCP: 151 (2019) → 11 (2024) — largest collapse in AP history
• TDP: 23 (2019) → 135 (2024) — massive comeback
• Coalition 164/175 — one of AP's biggest ever margins''',
            'tags_json': '["AP Elections 2024","TDP","JSP","BJP","YSRCP","Seat Count"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_loksabha_2024',
            'title': 'AP Lok Sabha 2024 Results (25 Seats)',
            'body': '''AP Lok Sabha Election 2024 — Results

Total AP Lok Sabha seats: 25

TDP-JSP-BJP Coalition:
  TDP: Contested 17 → Won 16
  JSP: Contested  2 → Won  2 (100%)
       — Kakinada: Tangella Udaya Srinivas (JSP)
       — Machilipatnam: Vallabhaneni Balasowri (JSP)
  BJP: Contested  6 → Won  3
  COALITION TOTAL: 21/25

YSRCP: Contested 25 → Won 4 [2019: won 22]

IMPORTANT NOTES:
• Pawan Kalyan did NOT contest Lok Sabha — he won Pithapuram ASSEMBLY seat (MLA)
• Araku Lok Sabha seat won by YSRCP (Gumma Tanuja Rani) — NOT BJP
• Kakinada Lok Sabha (covering Pithapuram area) won by JSP's Tangella Udaya Srinivas
• AP Rajya Sabha seats: 11

TDP's coalition support was crucial for NDA's national majority.''',
            'tags_json': '["Lok Sabha 2024","AP","TDP","JSP","Pawan Kalyan","Pithapuram"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_election_records',
            'title': 'AP 2024 Election Special Facts & Records',
            'body': '''AP 2024 Election — Special Facts for Exam

• Highest polling constituency: Darsi (Prakasam district) — 90.91%
• Lowest polling constituency: Tirupati — 63.32%
• Overall turnout: 81.86%
• Coalition margin: 164/175 — historic in AP politics

CBN (Chandrababu Naidu) milestone:
• 4th time as AP CM (1995, 1999, 2014, 2024)
• Called "Chaturtha Naidu Ministry" (Fourth Naidu Ministry)
• TDP founded by NTR (N.T. Rama Rao) on March 29, 1982

Jagan Mohan Reddy (YSRCP):
• Won his OWN seat from Pulivendula — even as YSRCP lost everywhere
• YSRCP had won 151 in 2019 under same Jagan leadership

Alliance "Super Six" slogan:
Annadata Sukhibhava, Talliki Vandanam, Aadabidda Nidhi,
Free Bus, Nirudyoga Bruthi, Deepam 2.0''',
            'tags_json': '["AP Elections 2024","Records","CBN","Darsi","Tirupati","Super Six"]',
            'lang': 'en'
        },

        # ─── DIV 1: CABINET ─────────────────────────────────────────────────────

        {
            'tag': 'ap_cabinet_2024_formation',
            'title': 'AP Cabinet 2024 — Formation & Composition',
            'body': '''Fourth Naidu Cabinet — Formation Details

Oath Ceremony:      June 12, 2024 (Vijayawada / Guntur)
Portfolio Distribution: June 14, 2024
CM sworn in:        N. Chandrababu Naidu (TDP, Kuppam constituency, Chittoor dist.)
Deputy CM:          Pawan Kalyan (JSP, Pithapuram constituency, E. Godavari dist.)

CABINET COMPOSITION (Total: 25 ministers incl. CM):
  TDP ministers:  21
  JSP ministers:   3
  BJP ministers:   1

First-time ministers (fresh faces): 17
Women ministers: 3
  — Vangalapudi Anitha (TDP, Payakaraopet)
  — S. Savitha (TDP, Penukonda)
  — Gummadi Sandhyarani (TDP, Salur — ST constituency)
BC ministers:  8
SC ministers:  2
ST ministers:  1
Muslim minister: 1 (Nasyam Mohammed Farook)

EXAM TRICK: 25 = 1 CM + 24 ministers; JSP got 3, BJP got 1 only''',
            'tags_json': '["AP Cabinet 2024","Composition","CBN","Pawan Kalyan","Ministers"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_cabinet_cm_dcm',
            'title': 'AP CM & DCM — Chandrababu Naidu & Pawan Kalyan',
            'body': '''Chief Minister: N. Chandrababu Naidu (TDP)
• Constituency: Kuppam (Chittoor district)
• 4th time as AP CM (1995, 1999, 2014, 2024)
• Son-in-law of TDP founder NTR
• Portfolios: General Administration (GAD), Law & Order, Public Enterprises

Deputy Chief Minister: Pawan Kalyan (JSP)
• Party: Jana Sena Party (JSP) — he is JSP president
• Constituency: Pithapuram (East Godavari district)
• Won Pithapuram ASSEMBLY seat — did NOT contest Lok Sabha
• Portfolios: Panchayati Raj & Rural Development (PR&RD),
              Rural Water Supply (RWS), Forests, Environment,
              Science & Technology

TDP was founded on March 29, 1982 by NTR (N.T. Rama Rao).
TDP celebrated its 44th Foundation Day in March 2026 (Mangalagiri HQ).''',
            'tags_json': '["Chandrababu Naidu","CM","Pawan Kalyan","DCM","Kuppam","Pithapuram"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_cabinet_key_ministers',
            'title': 'AP Cabinet 2024 — Key Ministers & Portfolios',
            'body': '''AP Cabinet 2024 — Key Ministers (Exam Focus)

NAME                     | PARTY | PORTFOLIO              | CONSTITUENCY
Nara Lokesh              | TDP   | HRD (Education), IT    | Mangalagiri (son of CBN)
Vangalapudi Anitha       | TDP   | Home, Disaster Mgmt    | Payakaraopet
Payyavula Keshav         | TDP   | Finance, Planning, CT  | Uravakonda (Anantapur)
Satya Kumar Yadav        | BJP   | Health, Medical Edu    | Dharmavaram ★ ONLY BJP minister
Nasyam Mohammed Farook   | TDP   | Law & Justice, Minority| Nandyal ★ ONLY Muslim minister
Kolusu Parthasarathy     | TDP   | Housing, I&PR          | Nuzvid (Krishna dist.)
P. Narayana              | TDP   | MAUD, Slum Dev         | Nellore City
Gottipati Ravi Kumar     | TDP   | Energy (Electricity)   | Addanki
Kondapalli Srinivas      | TDP   | MSME, SERP, NRI        | Gajapati Nagar
Mandipalli Ramprasad     | TDP   | Transport, Youth/Sports| Raychoti
Anagani Satya Prasad     | TDP   | Revenue, Stamps & Reg  | Repalle
Nadendla Manohar         | JSP   | Civil Supplies, Consumer| Tenali ★ JSP #2
Kandula Durgesh          | JSP   | Tourism, Culture, Cinema| Nidadavole ★ JSP #3
Nimmala Ramanaidu        | TDP   | Water Resources        | Palakollu (W. Godavari)
B.C. Janardhan Reddy     | TDP   | Roads & Buildings, Infra| Banaganapalle (Nandyal)

Finance Minister 2025-26 Budget:
  Payyavula Keshav presented ₹3,22,359 crore budget on Feb 28, 2025''',
            'tags_json': '["AP Cabinet 2024","Ministers","Portfolio","Finance","Health","Home"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_constitutional_positions',
            'title': 'AP Constitutional & Key Positions 2024-2026',
            'body': '''AP Key Positions — For Exam

POSITION             | PERSON                          | NOTE
Governor             | Justice S. Abdul Nazeer         | Retired SC judge; since Feb 2023
Chief Minister       | N. Chandrababu Naidu            | Since June 12, 2024
Deputy CM            | Pawan Kalyan (JSP)              | Pithapuram MLA
Assembly Speaker     | Chintakayala Ayyannapatrudu     | TDP, Narsipatnam; elected June 2024
Deputy Speaker       | Raghu Rama Krishna Raju         | TDP, Undi; elected Nov 14, 2024
Legislative Council  |                                 |
  Chairman           | Koyye Moshen Raju               | YSRCP; elected Nov 19, 2021; continues
Finance Minister     | Payyavula Keshav                | Budget ₹3,22,359 cr (2025-26)
Chief Secretary      | G. Sai Prasad                   | IAS 1991 batch; since March 1, 2026
                     |   (earlier: Neerab Kumar Prasad Jun-Dec 2024;
                     |             K. Vijayananand Jan-Feb 2026)
DGP                  | Harish Kumar Gupta              | IPS 1992 batch; since Jan 31, 2025
AP Rajya Sabha seats | 11

EXAM TRICK: Governor = Abdul Nazeer (appointed by President of India)''',
            'tags_json': '["AP Governor","Speaker","Chief Secretary","DGP","Constitutional Positions"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_governance_milestones',
            'title': 'AP Governance Milestones 2024-2026 (CBN Government)',
            'body': '''Key Governance Decisions — CBN Government 2024-2026

1. CAPITAL — AMARAVATI (Dec 2025 / Apr 2026):
   • AP Reorganisation Amendment Act 2026 (No.7/2026) passed by both Houses
   • Amaravati declared sole capital (legal backing)
   • Farmers gave 33,000+ acres for construction
   • CRDA = Capital Region Development Authority (est. under CRDA Act 2014)

2. NEW DISTRICTS (Dec 29, 2025 Cabinet):
   • 2 new districts added: Polavaram (HQ: Ramachandrapuram) + Markapur
   • Also: Annammaya district HQ moved from Raychoti → Madanapalle
   • Total districts: 26 → 28 (from Jan 1, 2026)
   • 5 new Revenue Divisions: Nakkapalle, Addanki, Pileru, Banaganapalle, Madakasira

3. AP JAN VISHWAS ACT 2026 (March 2026):
   • Replaces jail terms for minor offences with monetary fines
   • 12 laws amended; 2 obsolete laws repealed
   • Governor Abdul Nazeer gave assent

4. BHARAT NET PROJECT (Feb 22, 2026):
   • MoC signed with Centre: ₹2,432 crore
   • High-speed internet to 5 lakh rural homes in 18 months

5. STATUE OF SACRIFICE, AMARAVATI (Dec 15, 2025):
   • 58-foot statue of Potti Sriramulu
   • 6.8-acre Memorial Park
   • Commemorates his 58-day fast unto death for Telugu state

6. AP DISTRICTS — ZONES (6 Zones, 2 Multi-Zones):
   Multi-Zone 1: Zones 1-3 (North AP + Godavari districts)
   Multi-Zone 2: Zones 4-6 (South AP + Rayalaseema)''',
            'tags_json': '["AP Governance","Amaravati","Districts","Jan Vishwas","BharatNet","Potti Sriramulu"]',
            'lang': 'en'
        },

        # ─── DIV 2: SUPER SIX ───────────────────────────────────────────────────

        {
            'tag': 'ap_super_six_overview',
            'title': 'Super Six — TDP-JSP-BJP Election Guarantees (Overview)',
            'body': '''Super Six — TDP-JSP-BJP Coalition's 6 Election Promises (2024)

#  | SCHEME              | BENEFICIARY               | AMOUNT             | LAUNCH DATE
1  | Deepam 2.0          | BPL/White card families   | 3 free LPG/year    | Nov 1, 2024
2  | Free Bus Travel     | Women + Transgender        | Free APSRTC travel | Aug 15, 2024
3  | Nirudyoga Bruthi    | Unemployed youth           | ₹3,000/month       | Aug 15, 2024 (enroll)
4  | Annadata Sukhibhava | Farmers                   | ₹20,000/year       | Aug 2, 2025
5  | Talliki Vandanam    | School children's mothers  | ₹15,000/year       | Jun 12, 2025
6  | Aadabidda Nidhi     | Women 18-59 yrs           | ₹1,500/month       | 2026 (pending)

LAUNCH ORDER (chronological):
  Aug 15, 2024 → Independence Day: Free Bus + Nirudyoga Bruthi + Anna Canteen relaunch
  Nov 1, 2024  → AP Foundation Day: Deepam 2.0
  Jun 12, 2025 → Govt 1st Anniversary: Talliki Vandanam
  Aug 2, 2025  → Annadata Sukhibhava
  2026 (target)→ Aadabidda Nidhi (NOT yet launched as of mid-2026)

Note: "Navaratnalu" was YSRCP's scheme bundle — NOT TDP's.
TDP's bundle = "Super Six" (Supar Six).''',
            'tags_json': '["Super Six","TDP","Schemes","AP 2024","Election Promises"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_deepam2',
            'title': 'Deepam 2.0 — Free LPG Scheme (Super Six #1)',
            'body': '''Deepam 2.0 — Free LPG Cylinder Scheme

Launch Date:    November 1, 2024 (AP Foundation Day / Statehood Day)
Launch Location: Edupuram, Ichchapuram Mandal, Srikakulam district

KEY DETAILS:
• 3 free LPG cylinders per year per eligible family
• Cylinder cost paid first → refunded within 48 hours to bank account
• Eligible: BPL / White Ration Card families
• Initial fund release: ₹894 crore (to BP, HP, IOC gas companies)
• Annual budget: ₹2,684 crore/year (total for all eligible families)
• Implementing minister: Nadendla Manohar (JSP) — Civil Supplies Minister

HISTORY:
• Deepam 1.0 launched during TDP's first term (2014-19)
• YSRCP discontinued it; TDP relaunched as "2.0" in 2024

EXAM TRICK: Nov 1 = AP Foundation Day. "2.0" = improved re-launch.
First release ₹894 cr ≠ annual ₹2,684 cr (don't confuse these two!)''',
            'tags_json': '["Deepam 2.0","LPG","AP Foundation Day","Srikakulam","Nadendla Manohar"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_free_bus_stree_shakti',
            'title': 'Free Bus Travel (Stree Shakti) — Women\'s Scheme (Super Six #2)',
            'body': '''APSRTC Free Bus Travel for Women — Stree Shakti

Launch Date:     August 15, 2024 (Independence Day)
Beneficiaries:   Women, girls, Transgender persons
Bus Types:       All APSRTC buses (Palle Velugu, Express, etc.) — NOT AC buses
Scope:           Free travel anywhere within AP

OFFICIAL RENAMING (Aug 15, 2025 — 1st Anniversary):
• Scheme officially named "Stree Shakti" (స్త్రీ శక్తి)
• Extended to all 5 APSRTC bus divisions
• CM CBN, DCM Pawan Kalyan, Minister Lokesh participated in symbolic bus ride
  (Undavalli to Vijayawada City Bus Stand)

Implementing Minister: Mandipalli Ramprasad Reddy (TDP) — Transport Minister

ALSO on Aug 15, 2024:
• Nirudyoga Bruthi (Unemployment Allowance) registration began
• Anna Canteen relaunched (Phase 1: 100 canteens, ₹5/plate)

Divyanga Shakti (March 2026):
• Free APSRTC travel extended to persons with disabilities
• Launched by CM CBN at Mangalagiri Bus Stand''',
            'tags_json': '["Stree Shakti","Free Bus","APSRTC","Women","Independence Day","Divyanga Shakti"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_nirudyoga_bruthi',
            'title': 'Nirudyoga Bruthi — Unemployment Allowance (Super Six #3)',
            'body': '''Nirudyoga Bruthi (నిరుద్యోగ భృతి) — Unemployment Allowance

Launch/Registration Start: August 15, 2024

KEY DETAILS:
• Amount: ₹3,000/month
• Target: Unemployed youth and young women in AP
• Condition: Must be AP resident and unemployed

HISTORY:
• TDP had this scheme in 2014-2019 as well; YSRCP discontinued
• Restarted under CBN 2.0 government (2024)

EXAM NOTE: Nirudyoga Bruthi is Super Six #3.
Do NOT confuse with Aadabidda Nidhi (₹1,500/month for women 18-59).
Nirudyoga Bruthi = ₹3,000 for unemployed youth (any gender).
Aadabidda Nidhi = ₹1,500 for BC/SC/ST women aged 18-59 specifically.''',
            'tags_json': '["Nirudyoga Bruthi","Unemployment Allowance","Super Six","AP Schemes"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_annadata_sukhibhava',
            'title': 'Annadata Sukhibhava — Farmer Support Scheme (Super Six #4)',
            'body': '''Annadata Sukhibhava (అన్నదాత సుఖీభవ) — Farmer Income Support

Launch Date:    August 2, 2025
Launch Location: Toorpu Veerapalem, Darsi Mandal, Prakasam district

KEY DETAILS:
• Total annual support: ₹20,000 per farmer per year
• STATE share: ₹14,000/year
• CENTRE share (PM KISAN): ₹6,000/year
• 3 installments: ₹7,000 + ₹7,000 + ₹6,000 = ₹20,000
• 1st installment: ₹7,000 — ₹3,175 crore released
• Farmers covered in 1st installment: 46.86 lakh farmers
• Budget allocation 2024-25: ₹6,300 crore

COMPARISON WITH YSRCP:
• YSR Rythu Bharosa = ₹13,500/year (YSRCP scheme)
• Annadata Sukhibhava = ₹20,000/year (TDP + PM KISAN combined)
• TDP = MORE by ₹6,500/year due to PM KISAN integration

EXAM TRICK: ₹20,000 = ₹14,000 (state) + ₹6,000 (PM KISAN centre)''',
            'tags_json': '["Annadata Sukhibhava","Farmer","PM KISAN","Super Six","₹20000"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_talliki_vandanam',
            'title': 'Talliki Vandanam — Education Scheme for Students\' Mothers (Super Six #5)',
            'body': '''Talliki Vandanam (తల్లికి వందనం) — School Children's Mothers Fund

Launch Date:     June 12, 2025 (Government's 1st Anniversary of oath-taking)
                 [Oath was June 12, 2024 → 1 year later = June 12, 2025]

KEY DETAILS:
• Amount: ₹15,000 per student per year → goes to MOTHER's bank account
• Classes: 1–12, Government & Aided schools (NOT private schools)
• Attendance requirement: minimum 75% attendance
• Mother must have Aadhaar-linked bank account with NPCI
• Eligible students: 69.16 lakh (out of 81 lakh total enrolled)
• Budget 2025-26: ₹9,407 crore

KEY DIFFERENCE vs YSRCP's Amma Vodi:
  Amma Vodi (YSRCP):     ₹15,000 for ONLY ONE child per family (first child)
  Talliki Vandanam (TDP): ₹15,000 for EVERY school-going child in family
→ TDP scheme benefits more children in multi-child families

EXAM TRICK: "Vandanam" = salute/respect. Money goes to MOTHER, not student.
Jun 12, 2025 = exact 1st anniversary of CBN's oath (June 12, 2024).''',
            'tags_json': '["Talliki Vandanam","Education","School","Mothers","Super Six","Amma Vodi"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_aadabidda_nidhi',
            'title': 'Aadabidda Nidhi — Women\'s Monthly Fund (Super Six #6)',
            'body': '''Aadabidda Nidhi (ఆడబిడ్డ నిధి) — Women's Monthly Support

Status as of mid-2026: NOT yet launched (2026 target announced)

KEY DETAILS:
• Amount: ₹1,500/month = ₹18,000/year
• Age group: 18–59 years
• Eligible categories: BC, SC, ST, Minority, EBC women
• Estimated beneficiaries: 80+ lakh women
• Additional benefit: Free bus travel also included

COMPARISON:
  YSRCP's YSR Cheyuta:  ₹18,750/year for women
  TDP's Aadabidda Nidhi: ₹18,000/year (slightly less, but broader coverage planned)

EXAM TRICK: ₹1,500/month × 12 = ₹18,000/year.
This is the ONLY Super Six scheme NOT yet implemented.
Do not confuse: Nirudyoga Bruthi = ₹3,000/month (unemployed ANY gender)
                Aadabidda Nidhi = ₹1,500/month (BC/SC/ST women 18-59 only)''',
            'tags_json': '["Aadabidda Nidhi","Women Welfare","Super Six","Pending","₹1500"]',
            'lang': 'en'
        },

        # ─── DIV 2: NTR BHAROSA PENSION ─────────────────────────────────────────

        {
            'tag': 'ap_ntr_bharosa_pension',
            'title': 'NTR Bharosa Pension — AP Welfare Pension Scheme',
            'body': '''NTR Bharosa Pension (NTR భరోసా పెన్షన్)

LAUNCH DATE: June 13, 2024 (day after oath-taking on June 12, 2024)
PAYMENTS FROM: July 1, 2024 (April-June backlog also paid in July)

KEY AMOUNTS:
• Basic pension (elderly, widows, etc.):  ₹4,000/month
• Fully disabled persons:                ₹15,000/month

COVERAGE:
• 65+ lakh beneficiaries
• 28 categories including:
  Elderly, Widows, Disabled, Fishermen, Weavers,
  Transgender, Artists, PLHIV (HIV+), and more

NAME CHANGE:
• YSRCP name: "YSR Pension Kanuka" (YSR పెన్షన్ కనుక)
• TDP 2024 renamed to: "NTR Bharosa" (after TDP founder NTR)

PAYMENT: Direct Bank Transfer (DBT)

EXAM CRITICAL:
• Basic = ₹4,000 (NOT ₹3,000 — common error in older resources)
• Disabled = ₹15,000
• NTR = Nandamuri Tarak Rama Rao (TDP founder)''',
            'tags_json': '["NTR Bharosa","Pension","₹4000","Disabled","YSR Pension Kanuka","AP Welfare"]',
            'lang': 'en'
        },

        # ─── DIV 2: ANNA CANTEEN ─────────────────────────────────────────────────

        {
            'tag': 'ap_anna_canteen',
            'title': 'Anna Canteen — ₹5 Meal Scheme',
            'body': '''Anna Canteen (అన్నా కేంటీన్) — Subsidized Meals for Poor

TDP RELAUNCH DATE: August 15, 2024 (Independence Day)

KEY DETAILS:
• Price: ₹5 per plate (heavily subsidized nutritious meal)
• Phase 1: 100 Anna Canteens opened
• Location: Municipal/Corporation areas (urban + semi-urban)

HISTORY:
• Launched by TDP during 2014-2019 term
• YSRCP discontinued in 2019
• TDP relaunched on Aug 15, 2024 (same day as Free Bus + Nirudyoga Bruthi)

EXAM TRICK: Three things happened on Aug 15, 2024:
  1. Free Bus travel (Stree Shakti) — launched
  2. Nirudyoga Bruthi — registration started
  3. Anna Canteen — relaunched (100 canteens)
  All on Independence Day!''',
            'tags_json': '["Anna Canteen","₹5 Meal","Independence Day","AP Welfare","TDP"]',
            'lang': 'en'
        },

        # ─── DIV 2: OTHER SCHEMES ────────────────────────────────────────────────

        {
            'tag': 'ap_schemes_comparison',
            'title': 'YSRCP vs TDP Schemes — Comparison Table',
            'body': '''YSRCP Schemes vs TDP (2024+) Schemes — Key Comparisons

CATEGORY    | YSRCP SCHEME              | TDP SCHEME (2024+)
Pension     | YSR Pension Kanuka        | NTR Bharosa (₹4,000 basic; ₹15,000 disabled)
LPG         | (no free LPG scheme)      | Deepam 2.0 (3 cylinders/year)
Women fund  | YSR Cheyuta (₹18,750/yr)  | Aadabidda Nidhi (₹18,000/yr; pending)
Education   | Amma Vodi (₹15,000 — 1   | Talliki Vandanam (₹15,000 — ALL children;
            |  child per family only)   |  pvt. schools excluded)
Farmer      | YSR Rythu Bharosa         | Annadata Sukhibhava
            | (₹13,500/year)            | (₹20,000/year incl. PM KISAN ₹6,000)
Food        | Anna Canteen closed       | Anna Canteen relaunched (₹5/plate)
Housing     | Pedalandariki Illu        | Pedalandariki Illu (continued)
Crop insur. | YSR Sampurna Panta Bima   | Chandranna Bima (₹5 lakh crop insurance)
            | (discontinued)            | (relaunched 2024)
Health      | YSR Arogya Sri (₹5 lakh) | NTR Vaidya Seva + PM-JAY (₹25 lakh; Hybrid)
Sand        | Paid sand (govt. control) | Free Sand Policy (1st state in India for free sand)
Fishermen   | YSR Matsyakara Bharosa    | Matsyakara Seva (₹10,000 during ban Apr-Jun)
Weavers     | YSR Nethanna Bharosa      | Nethanna Bharosa (₹25,000/yr + free electricity)

NETHANNA BHAROSA (Aug 7, 2025 — National Handloom Day):
• Weavers: ₹25,000/year + free electricity
  (Handlooms: 200 units; Power looms: 500 units)
• GST on handloom textiles reimbursed by govt (₹15 crore allocated)
• Annual cost: ₹193 crore/year''',
            'tags_json': '["YSRCP vs TDP","Schemes","Comparison","Nethanna Bharosa","Chandranna Bima"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_health_scheme_2025',
            'title': 'AP New Health Policy 2025 — ₹25 Lakh Coverage',
            'body': '''AP New Health Policy — PM Jan Arogya Yojana + NTR Vaidya Seva (Hybrid)

CABINET APPROVAL: September 4, 2025

KEY DETAILS:
• Coverage: ₹25 lakh per family (total medical care)
  — ₹2.5 lakh: via insurance (any family above poverty line too)
  — ₹2.5 lakh to ₹25 lakh: via NTR Arogya Seva Trust
• Beneficiaries: 5 crore people across AP
• Medical procedures covered: 3,257 types
• Government hospitals: 324 types of procedures
• Claim approval: within 6 hours of hospital admission
• Payment to hospitals: within 15 days

Also known as "Sanjivani" scheme (digital health cards for each citizen)
• Each citizen gets a Digital Health Card
• Pilot at Kuppam; statewide rollout planned

COMPARISON:
  YSR Arogya Sri (YSRCP): ₹5 lakh coverage
  AP New Health Policy (TDP): ₹25 lakh coverage (5x more!)

Working journalists also covered under this scheme.''',
            'tags_json': '["AP Health Policy","₹25 Lakh","Sanjivani","NTR Vaidya Seva","PM-JAY","Cabinet 2025"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_free_sand_policy',
            'title': 'AP Free Sand Policy — First in India',
            'body': '''AP Free Sand Policy (ఉచిత ఇసుక విధానం)

KEY FACTS:
• AP is the FIRST STATE IN INDIA to provide free sand for housing construction
• Free sand for: Individual house construction (not commercial)
• Cost: Only transportation charges paid by the applicant
• Booking: AP Sand Tech App (online booking system)

Under YSRCP: Sand was paid (government-controlled paid supply)
Under TDP (2024+): Free sand policy — major relief for house builders

This was launched under "Pedalandariki Illu" housing expansion.

EXAM TRICK: Free Sand = First state in India = AP TDP policy.''',
            'tags_json': '["Free Sand Policy","AP","First in India","Housing","TDP"]',
            'lang': 'en'
        },

        {
            'tag': 'ap_cii_partnership_summit',
            'title': 'CII-AP Partnership Summit (Vizag, Nov 2025)',
            'body': '''CII-AP 30th Partnership Summit — Visakhapatnam, November 2025

KEY FACTS:
• 3-day summit in Visakhapatnam (Nov 14-15, 2025 + 1 pre-day)
• 613 MOUs/agreements signed
• Investments: ₹13.26 lakh crore across 12 sectors
• Jobs: 16.31 lakh employment opportunities created
• Participants: National & international investors

KEY AGREEMENTS:
• Reliance + Brookfield: 1,000 MW each Data Centers in AP
• World Economic Forum (WEF) + AP Govt: MOU for Centre for
  Energy & Cyber Resilience (signed Nov 15)

CM CBN announcement at summit:
• Next year summit again in Vizag (Nov 14-15, 2026)
• "Andhra Mandapam" (convention center) to be built on Vizag coastline
• AP targeting 160 GW green energy production

AP's green energy target: 160 GW''',
            'tags_json': '["CII Summit","Visakhapatnam","MOUs","Investment","WEF","Green Energy"]',
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
    print(f'[div1div2 notes] Seeded {len(notes)} concept notes for AP CA Div1 + Div2')


if __name__ == '__main__':
    seed()
