# seed_polity_ch11.py
# Chapter 11: Amendment of the Constitution (రాజ్యాంగ సవరణ)
# Total MCQs: 53 | PYQs: 9 | Format: Bilingual (Telugu + English)
# Sections:
#   0 = ప్రాథమిక అంశాలు / Basic Facts — Art 368, Procedure (6 MCQs)
#   1 = సాధారణ మెజారిటీ / Simple Majority Amendments (5 MCQs)
#   2 = ప్రత్యేక మెజారిటీ / Special Majority Amendments (5 MCQs)
#   3 = ప్రత్యేక మెజారిటీ + రాష్ట్రాల ఆమోదం / Special Majority + State Ratification (5 MCQs)
#   4 = మూల నిర్మాణ సిద్ధాంతం / Basic Structure Doctrine (10 MCQs — incl. Sajjan Singh 1964, Waman Rao 1981)
#   5 = ముఖ్య సవరణలు భాగం I / Important Amendments Part I — 1st to 69th (8 MCQs)
#   6 = ముఖ్య సవరణలు భాగం II / Important Amendments Part II — 73rd to 104th incl. 86th (9 MCQs)
#   7 = కఠిన ప్రశ్నలు / Tough MCQs (5 MCQs)

import json as _json

POLITY_CH11_MCQS = [
    # ───── Section 0: Basic Facts — Art 368 ─────
    (0, "easy",
     "Power and procedure to amend Constitution is in which Article?\nతెలుగు: సవరణ Article?",
     "Article 356", "Article 360", "Article 368 (correct)", "Article 370",
     "C",
     "Article 368 (Part XX) deals with POWER and PROCEDURE for CONSTITUTIONAL AMENDMENT. Specifies three modes: (1) Simple Majority [outside Art.368]; (2) Special Majority of Parliament [Art.368]; (3) Special Majority + State Ratification [Art.368]. Title of Part XX: 'Amendment of the Constitution.'"),

    (0, "easy",
     "Who can introduce a Constitutional Amendment Bill?\nతెలుగు: ఎవరు ప్రవేశపెట్టవచ్చు?",
     "Only Union Cabinet",
     "Either House of Parliament — government or private member / ఏ సభలోనైనా (correct)",
     "Only President", "Only Rajya Sabha",
     "B",
     "Constitutional Amendment Bill can be introduced in EITHER HOUSE of Parliament (LS or RS) by a GOVERNMENT MEMBER (Minister) or PRIVATE MEMBER. Crucially, STATE LEGISLATURES CANNOT introduce Constitutional Amendment Bills. Bill cannot be initiated outside Parliament — no referendum, no people's initiative."),

    (0, "medium",
     "What is 'Special Majority' for Constitutional Amendment?\nతెలుగు: Special Majority?",
     "2/3 of present and voting only",
     "2/3 of present & voting AND majority of total membership of each House / 2/3 + మొత్తం సభ్యత్వం 50%+ (correct)",
     "3/4 of total membership", "2/3 of combined Houses",
     "B",
     "SPECIAL MAJORITY = TWO conditions in EACH HOUSE: (1) Majority of TOTAL MEMBERSHIP (>50%) of the House; AND (2) Majority of NOT LESS THAN 2/3 of MEMBERS PRESENT AND VOTING. Both required. Higher than ordinary majority but lower than '2/3 of total membership' (Art.61 Impeachment standard)."),

    (0, "medium",
     "What if two Houses disagree on Constitutional Amendment Bill?\nతెలుగు: అభిప్రాయ భేదం?",
     "Resolved through Joint Sitting",
     "Lok Sabha decision final", "President mediates",
     "Bill lapses — no Joint Sitting / Bill రద్దు (correct)",
     "D",
     "There is NO PROVISION FOR JOINT SITTING (Art.108) for Constitutional Amendment Bills. Both Houses MUST SEPARATELY pass with Special Majority. If one House rejects or doesn't pass, the Bill LAPSES. This is a major safeguard — neither House can override the other."),

    (0, "hard",
     "How did 24th Amendment 1971 change President's role under Art.368?\nతెలుగు: 24వ సవరణ President?",
     "Gave veto power",
     "President's assent MANDATORY — removed power to withhold / తప్పనిసరి అనుమతి (correct)",
     "Excluded President from process",
     "6-month suspension power",
     "B",
     "24th Constitutional Amendment 1971 [post-Golaknath]: (1) Made PRESIDENT'S ASSENT MANDATORY for Constitutional Amendment Bills — President must give assent (cannot withhold or return); (2) Inserted Art.13(4) and Art.368(3) — clarified Parliament's power to amend any provision INCLUDING Fundamental Rights. Negated Golaknath (1967)."),

    (0, "medium",
     "Which is correct about Constitutional Amendment?\nతెలుగు: సరైన వ్యాఖ్య?",
     "State legislatures can introduce",
     "State ratification always needed",
     "No time limit for state ratification / కాల పరిమితి లేదు (correct)",
     "Referendum required",
     "C",
     "There is NO TIME LIMIT prescribed for state ratification of constitutional amendments. States can ratify whenever they wish. State legislatures CANNOT introduce amendment bills. State ratification is required ONLY for federal amendments (Art.54, 55, 73, 162, 7th Schedule, etc.). No referendum mechanism in India for constitutional amendments."),

    # ───── Section 1: Simple Majority Amendments ─────
    (1, "medium",
     "Which provision can be amended by Simple Majority — outside Art.368?\nతెలుగు: Simple Majority Art.368 బయట?",
     "Electoral process",
     "Formation of new states — Art.2 & 3 / కొత్త రాష్ట్రాలు (correct)",
     "Election of President", "Distribution of legislative powers",
     "B",
     "FORMATION OF NEW STATES (Art.2 — admission/establishment of new states; Art.3 — alteration of areas, boundaries, names of existing states) is by Simple Majority of Parliament — NOT under Art.368. Other simple-majority items: creation/abolition of Legislative Councils (Art.169), citizenship laws (Art.5-11), MP salaries, Rules of Procedure of Parliament."),

    (1, "medium",
     "Creating/abolishing State Legislative Councils requires?\nతెలుగు: శాసనమండళ్ళ?",
     "State legislature resolution + Parliament Simple Majority / రాష్ట్ర తీర్మానం + Parliament (correct)",
     "Parliament Special Majority",
     "Special Majority + Half states",
     "Only Parliament Simple Majority",
     "A",
     "Art.169 — Abolition or creation of Legislative Councils: STATE LEGISLATIVE ASSEMBLY passes resolution by special majority (majority of total membership + 2/3 of present-and-voting). Then PARLIAMENT enacts law by SIMPLE MAJORITY. NOT considered amendment of Constitution under Art.368. Recent examples: Andhra Pradesh, Telangana council debates."),

    (1, "hard",
     "Which can be amended by Simple Majority?\nతెలుగు: Simple Majority?",
     "Fifth Schedule (Scheduled Areas)",
     "Seventh Schedule (Union-State Lists)",
     "First Schedule (names of States) — via Art.3/4 / మొదటి షెడ్యూల్ (correct)",
     "Ninth Schedule",
     "C",
     "FIRST SCHEDULE (states/UTs names) and FOURTH SCHEDULE (RS seat allocation) can be amended by SIMPLE MAJORITY via Art.3/4 (formation of new states). Recent: J&K reorganisation 2019 modified First Schedule. Fifth Schedule (Scheduled Areas) ALSO simple majority via Para 7. SEVENTH Schedule and NINTH Schedule require Special Majority + state ratification (7th) or just Special Majority (9th)."),

    (1, "medium",
     "MPs' salaries and allowances can be amended by which majority?\nతెలుగు: MP జీతాలు?",
     "Special Majority", "Special Majority + State Ratification",
     "Simple Majority / Simple Majority (correct)",
     "Unanimous decision",
     "C",
     "Art.106: Salaries, allowances, pensions of MPs are determined BY PARLIAMENT BY LAW from time to time — through ORDINARY LEGISLATION (Simple Majority). Outside Art.368. Various Members' Salaries Acts have done this. Same applies to Ministers' salaries (Art.75(6)) and President/VP salaries (Art.59/97)."),

    (1, "medium",
     "Citizenship provisions (Art.5-11) can be amended by which majority?\nతెలుగు: పౌరసత్వం?",
     "Special Majority + State Ratification", "Special Majority",
     "Simple Majority (correct)",
     "No amendment needed",
     "C",
     "Citizenship Act 1955 and provisions implementing Art.5-11 can be amended by SIMPLE MAJORITY (Art.11 explicitly empowers Parliament). Multiple Citizenship (Amendment) Acts: 1986, 2003, 2005, 2015, 2019. Outside Art.368 scope. Same for emergency administration of Scheduled Areas (5th Schedule), Tribal Areas (6th Schedule) — simple majority."),

    # ───── Section 2: Special Majority Amendments ─────
    (2, "medium",
     "Which majority is required to amend Fundamental Rights?\nతెలుగు: FRs మెజారిటీ?",
     "Simple Majority",
     "Special Majority / ప్రత్యేక మెజారిటీ (correct)",
     "Special Majority + Half states", "Cannot amend",
     "B",
     "Fundamental Rights (Art.12-35) can be amended by SPECIAL MAJORITY (Art.368). Confirmed by 24th Amendment 1971; subject to BASIC STRUCTURE limit per Kesavananda Bharati 1973. So FRs CAN be amended but the BASIC STRUCTURE features they form (e.g., Art.14 equality framework, Art.21 right to life, etc.) cannot be destroyed."),

    (2, "medium",
     "Which does NOT require Special Majority under Art.368?\nతెలుగు: Special Majority కానిది?",
     "Fundamental Rights", "DPSPs",
     "Quorum rules in Parliament / Quorum (correct)",
     "Constitutional structure",
     "C",
     "QUORUM RULES (e.g., Art.100(3) — quorum is 1/10 of total members) can be amended by SIMPLE MAJORITY — outside Art.368 scope. FRs (Art.12-35), DPSPs (Art.36-51), and structural provisions (Parliament, Cabinet, Judiciary) require SPECIAL MAJORITY. So quorum is the odd one out — falls under Parliament's procedural rules."),

    (2, "hard",
     "Which requires Special Majority ONLY (no state ratification)?\nతెలుగు: రాష్ట్రాల ఆమోదం అవసరం లేనిది?",
     "Manner of election of President", "Distribution in 7th Schedule",
     "Representation of States in Parliament",
     "Fundamental Rights / FRs (correct)",
     "D",
     "FUNDAMENTAL RIGHTS amendment requires SPECIAL MAJORITY ONLY — no state ratification needed (since FRs are about citizen-state relationship, not federal-state distribution). Election of President (Art.54, 55), 7th Schedule, Representation of States in Parliament (Art.81, 82) ARE federal in nature and NEED state ratification. Rule: federal provisions need ratification."),

    (2, "medium",
     "Amending SC/HC provisions requires which majority?\nతెలుగు: SC, HC?",
     "Simple Majority",
     "Special Majority (correct)",
     "Special Majority + Half states", "2/3 of total",
     "B",
     "Most provisions relating to Supreme Court (Art.124-147) and High Courts (Art.214-231) require SPECIAL MAJORITY only. EXCEPT some HIGH COURT JUDGES jurisdiction matters that may need state ratification (e.g., Art.241 — HCs for Union Territories). Generally SC/HC structural provisions are SPECIAL MAJORITY. Recent example: 99th Amendment (NJAC) was struck down as basic structure violation."),

    (2, "medium",
     "10th Schedule (Anti-defection) amendment requires?\nతెలుగు: 10th Schedule?",
     "Simple Majority",
     "Special Majority (correct)",
     "Special Majority + State Ratification", "Presidential order",
     "B",
     "10th SCHEDULE (Anti-defection law — added by 52nd Amendment 1985) requires SPECIAL MAJORITY for amendment. Notably 91st Amendment 2003 amended 10th Schedule (removed 1/3 'split' exemption; added Cabinet size cap) by Special Majority. NOT subject to state ratification — anti-defection is parliamentary matter."),

    # ───── Section 3: Special Majority + State Ratification ─────
    (3, "medium",
     "For state ratification, how many states must ratify?\nతెలుగు: ఎన్ని రాష్ట్రాలు?",
     "2/3 of states",
     "More than half (>50%) / 50% కంటే ఎక్కువ (correct)",
     "3/4 of states", "1/3 of states",
     "B",
     "Art.368 proviso: For federal amendments, NOT LESS THAN HALF OF THE STATES must ratify by RESOLUTION OF THEIR LEGISLATURES (passed by SIMPLE MAJORITY). 'Half of states' = > 50% = currently 14+ out of 28 states + UTs with legislatures. ANY half can ratify — no specific states required. No time limit."),

    (3, "medium",
     "Procedure to amend manner of Presidential election?\nతెలుగు: రాష్ట్రపతి ఎన్నిక?",
     "Simple Majority", "Special Majority only",
     "Special Majority + Ratification by half states / Special + 50% రాష్ట్రాలు (correct)",
     "President's personal approval",
     "C",
     "Manner of election of President (Art.54, 55) is a FEDERAL PROVISION — affects state representation in Electoral College. Requires SPECIAL MAJORITY (Art.368) + RATIFICATION BY HALF OF STATES. Same with Art.66 (VP election) since that involves federal scheme. 70th Amendment 1992 (added Delhi/Puducherry to Electoral College) followed this procedure.",
     "APPSC"),

    (3, "medium",
     "7th Schedule (Union/State/Concurrent Lists) amendment?\nతెలుగు: 7th Schedule?",
     "Simple Majority", "Special Majority only",
     "Special Majority + Half states ratification / Special + States (correct)",
     "Only state ratification",
     "C",
     "7th SCHEDULE distributes legislative powers between Centre and States (Union List, State List, Concurrent List). Quintessential FEDERAL provision. Requires SPECIAL MAJORITY + RATIFICATION BY HALF OF STATES. 101st Amendment 2016 (GST) needed this — which is why GST Council decisions, GST procedure emerged from federal consensus."),

    (3, "hard",
     "Which require Special Majority + state ratification: (1) Election of President (2) SC jurisdiction (3) 7th Schedule (4) State representation (5) Art.368?\nతెలుగు: ఏవి?",
     "Only 1, 3, 4, 5 / 1, 3, 4, 5 (correct)",
     "Only 1, 2, 3", "Only 2, 3, 4, 5", "All",
     "A",
     "REQUIRE state ratification: (1) Election of PRESIDENT (Art.54, 55); (3) 7th SCHEDULE (lists); (4) State REPRESENTATION in Parliament (Art.81, 82, 80); (5) Art.368 ITSELF (the amendment procedure). DO NOT require ratification: (2) SC JURISDICTION (Art.124, 246) — generally Special Majority only. Other ratification items: extent of EXECUTIVE POWER (Art.73, 162); HCs for UTs."),

    (3, "medium",
     "Procedure to amend Art.368 itself?\nతెలుగు: Art.368 సవరణ?",
     "Simple Majority", "Special Majority only",
     "Special Majority + Half states / Special + States (correct)",
     "Constituent Assembly",
     "C",
     "Art.368 itself (the amendment procedure article) requires SPECIAL MAJORITY + STATE RATIFICATION for amendment — listed as one of the entrenched federal provisions. Logical: any change to amendment procedure must have BOTH parliamentary and federal consent. Protects integrity of basic constitutional structure."),

    # ───── Section 4: Cases & Basic Structure ─────
    (4, "medium",
     "Shankari Prasad v. UoI (1951) held?\nతెలుగు: Shankari Prasad?",
     "Parliament cannot amend FRs",
     "Parliament can amend any provision including FRs / Parliament FRs సవరించవచ్చు (correct)",
     "FRs are part of Basic Structure",
     "Amendment power is limited",
     "B",
     "SHANKARI PRASAD v. UNION OF INDIA (1951): SC unanimously held that PARLIAMENT HAS POWER UNDER Art.368 to amend ANY PROVISION of Constitution INCLUDING FUNDAMENTAL RIGHTS. 'Law' in Art.13 doesn't include constitutional amendment. Upheld 1st Amendment 1951 (which had added Art.31A, 31B). FIRST major case on amendment power."),

    (4, "medium",
     "Sajjan Singh v. State of Rajasthan (1964) held?\nతెలుగు: Sajjan Singh?",
     "Parliament cannot amend FRs",
     "Upheld Shankari Prasad — Parliament can amend any provision including FRs / Shankari Prasad సమర్థన (correct)",
     "Basic Structure Doctrine propounded",
     "State ratification needed for FR amendment",
     "B",
     "SAJJAN SINGH v. STATE OF RAJASTHAN (1964): 5-judge SC bench UPHELD Shankari Prasad (1951) — Parliament can amend any provision under Art.368 including FRs. However, two judges (Hidayatullah J. and Mudholkar J.) expressed DOUBTS — laying seeds of basic structure doctrine. Mudholkar mentioned 'BASIC FEATURES.' Eventually Golaknath 1967 reversed; then Kesavananda 1973 propounded BS doctrine."),

    (4, "medium",
     "Golaknath v. State of Punjab (1967) held?\nతెలుగు: Golaknath?",
     "Parliament can amend FRs",
     "Parliament CANNOT amend FRs — they are transcendental / Parliament FRs సవరించలేదు (correct)",
     "Announced Basic Structure Doctrine",
     "Amendment power unlimited",
     "B",
     "I.C. GOLAKNATH v. STATE OF PUNJAB (1967): 11-judge SC bench (6:5 majority) OVERRULED Shankari Prasad and Sajjan Singh — held Parliament has NO POWER TO AMEND FUNDAMENTAL RIGHTS. Used 'doctrine of prospective overruling' to save earlier amendments. FRs called 'TRANSCENDENTAL.' Triggered 24th Amendment 1971 which restored Parliament's power. Then Kesavananda 1973 established BS doctrine."),

    (4, "easy",
     "In which case was Basic Structure Doctrine propounded?\nతెలుగు: Basic Structure ఏ కేసు?",
     "Shankari Prasad (1951)", "Golaknath (1967)",
     "Kesavananda Bharati v. State of Kerala (1973) (correct)",
     "Minerva Mills (1980)",
     "C",
     "KESAVANANDA BHARATI v. STATE OF KERALA (1973): 13-judge SC bench (LARGEST EVER), 7:6 majority. PROPOUNDED 'BASIC STRUCTURE DOCTRINE' — Parliament can amend ANY part of Constitution INCLUDING FRs (overruling Golaknath) BUT cannot DESTROY/ALTER its BASIC STRUCTURE. Watershed case in Indian constitutional law. Petitioner: Swami Kesavananda Bharati of Kerala (head of Edneer Mutt).",
     "APPSC"),

    (4, "medium",
     "Elements of 'Basic Structure' per Kesavananda Bharati?\nతెలుగు: Basic Structure అంశాలు?",
     "Constitutional supremacy, Secularism, Democracy, Judicial Review (correct)",
     "Only FRs", "Only Federal features", "DPSPs and FRs",
     "A",
     "BASIC STRUCTURE elements (evolving list — not exhaustive): Constitutional supremacy; Sovereign-democratic-republican nature; Secular character; Federal character; Separation of powers; Judicial review; Free and fair elections; Independence of judiciary; Rule of law; Harmony between FRs and DPSPs; Welfare state; Parliamentary system; Effective access to justice; Federal balance. Court added items case-by-case."),

    (4, "medium",
     "What did 42nd Amendment 1976 attempt regarding amendment power?\nతెలుగు: 42వ సవరణ?",
     "Limited the power",
     "Declared amendment power absolute and beyond judicial review / అపరిమితం, JR అతీతం (correct)",
     "Tried to repeal Art.368", "Made state ratification mandatory",
     "B",
     "42nd Amendment 1976 added Art.368(4) and (5): 'No amendment of this Constitution... shall be called in question in any court... There shall be no limitation whatever on the constituent power of Parliament.' Declared amendment power ABSOLUTE — beyond JR. STRUCK DOWN in Minerva Mills (1980) as violating BASIC STRUCTURE. Indira Gandhi-Emergency-era assertion of power."),

    (4, "medium",
     "Minerva Mills v. UoI (1980) held?\nతెలుగు: Minerva Mills?",
     "Rejected Basic Structure",
     "Struck down Art.368(4)/(5) of 42nd Am — amendment power LIMITED / 42వ Art.368(4)/(5) రద్దు (correct)",
     "DPSPs supreme over FRs", "Unlimited amendment power",
     "B",
     "MINERVA MILLS v. UoI (1980): 5-judge SC bench struck down (a) Art.368(4) and (5) inserted by 42nd Am — declaring 'no limitation' on amendment power VIOLATES BASIC STRUCTURE; (b) Extension of Art.31C to all DPSPs by 42nd Am — restored to only Art.39(b)/(c). Reaffirmed that HARMONY BETWEEN FR AND DPSP is part of basic structure. Justice P.N. Bhagwati, Y.V. Chandrachud."),

    (4, "hard",
     "Indira Nehru Gandhi v. Raj Narain (1975) added what to Basic Structure?\nతెలుగు: Indira Gandhi v. Raj Narain?",
     "Parliamentary democracy",
     "Free and fair elections / Free and fair elections (correct)",
     "Independence of judiciary", "Federal character",
     "B",
     "INDIRA NEHRU GANDHI v. RAJ NARAIN (1975): SC HELD that FREE AND FAIR ELECTIONS are PART OF BASIC STRUCTURE. STRUCK DOWN clause (4) of Art.329A added by 39th Amendment 1975 (which had retroactively validated Indira Gandhi's election after Allahabad HC had set it aside). Justice Khanna applied Basic Structure test. First case after Kesavananda BS doctrine to actually strike down an amendment."),

    (4, "hard",
     "IR Coelho v. State of TN (2007) added what?\nతెలుగు: IR Coelho?",
     "FRs are Basic Structure",
     "Laws added to 9th Schedule after April 24, 1973 subject to JR if violate Basic Structure / 1973 తర్వాత JR (correct)",
     "Amendment power absolute", "Federal provisions need ratification",
     "B",
     "I.R. COELHO v. STATE OF TAMIL NADU (2007): 9-judge SC Constitution Bench. Laws added to 9th SCHEDULE AFTER 24 APRIL 1973 (Kesavananda Bharati judgment date) are SUBJECT TO JUDICIAL REVIEW for VIOLATION OF BASIC STRUCTURE — particularly FRs forming basic structure. Laws added BEFORE 24 April 1973 remain immune. Major curb on misuse of 9th Schedule."),

    (4, "hard",
     "Waman Rao v. UoI (1981) on 9th Schedule?\nతెలుగు: Waman Rao?",
     "All 9th Schedule laws subject to JR",
     "All 9th Schedule laws fully protected — date irrelevant",
     "Laws BEFORE April 24, 1973 fully protected; AFTER subject to BS test / 1973 ముందు రక్షణ (correct)",
     "9th Schedule abolished",
     "C",
     "WAMAN RAO v. UoI (1981): SC refined 9th Schedule protection. Laws added BEFORE 24 April 1973 (Kesavananda date) are FULLY PROTECTED from FR-based challenges. Laws added AFTER 24 April 1973 are subject to BASIC STRUCTURE test. This was reaffirmed and elaborated in I.R. Coelho (2007). Important date: 24 APRIL 1973 = the cut-off for 9th Schedule immunity."),

    # ───── Section 5: Major Amendments ─────
    (5, "medium",
     "Which Amendment added 9th Schedule for land reform protection?\nతెలుగు: 9th Schedule?",
     "1st Amendment 1951 (correct)",
     "4th Amendment 1955", "7th Amendment 1956", "24th Amendment 1971",
     "A",
     "1st CONSTITUTIONAL AMENDMENT 1951 added 9th SCHEDULE plus Art.31B — to protect land reform laws (Bihar Land Reforms Act 1950 and similar zamindari abolition laws). Also added: reasonable restrictions on Art.19(1)(a), Art.15(4) for SC/ST/SEBC special provisions. Originally 13 laws in 9th Schedule; now 280+. Most contentious early amendment.",
     "APPSC"),

    (5, "medium",
     "7th Amendment 1956 was for?\nతెలుగు: 7వ సవరణ?",
     "FR expansion",
     "States Reorganisation — abolished A, B, C, D categories / రాష్ట్రాల పునర్వ్యవస్థీకరణ (correct)",
     "Emergency provisions",
     "DPSP extension",
     "B",
     "7th Amendment 1956 implemented STATES REORGANISATION ACT 1956. Abolished pre-1956 A/B/C/D categorisation of states (Part A, Part B, Part C, Part D). Created 14 STATES + 6 UNION TERRITORIES on linguistic basis. Andhra State (1953) had earlier been formed as first linguistic state; SR Act extended this nationwide. Major federal restructuring."),

    (5, "medium",
     "24th Amendment 1971 achieved?\nతెలుగు: 24వ సవరణ?",
     "Removed Right to Property",
     "Clarified Parliament can amend any provision including FRs + made President's assent mandatory / FRs + President assent (correct)",
     "Strengthened Emergency", "Repealed 42nd Am",
     "B",
     "24th Amendment 1971 (in response to GOLAKNATH 1967): Inserted Art.13(4) and Art.368(3) — explicitly stating Parliament's power under Art.368 EXTENDS to ANY PROVISION including FRs. Also: made PRESIDENT'S ASSENT MANDATORY for amendment bills. Aimed to overturn Golaknath. Kesavananda Bharati (1973) accepted this part but added Basic Structure limit."),

    (5, "easy",
     "Why is 42nd Amendment 1976 called 'Mini Constitution'?\nతెలుగు: Mini Constitution ఎందుకు?",
     "Very small amendment",
     "Brought most sweeping changes / అత్యంత విస్తృత మార్పులు (correct)",
     "Drafted new Constitution",
     "CA decision",
     "B",
     "42nd Amendment 1976 brought MOST SWEEPING CHANGES — touching nearly every part of Constitution. Major changes: (1) Added FUNDAMENTAL DUTIES (Art.51A, Part IVA); (2) Added 'SOCIALIST, SECULAR, INTEGRITY' to Preamble; (3) Strengthened DPSPs; (4) Limited judicial review; (5) Extended Lok Sabha/State Assembly term to 6 years; (6) Made amendment power absolute; (7) Added Tribunals (Art.323A/B). Hence 'Mini Constitution.'",
     "APPSC"),

    (5, "easy",
     "44th Amendment 1978 main change?\nతెలుగు: 44వ సవరణ?",
     "Added Fundamental Duties",
     "Removed Right to Property from FRs (Art.19(1)(f) + Art.31) / ఆస్తి హక్కు తొలగింపు (correct)",
     "Introduced GST", "DPSPs above FRs",
     "B",
     "44th Amendment 1978 (Janata Government, post-Emergency): (1) REMOVED Right to Property from FRs (deleted Art.19(1)(f) and Art.31); added Art.300A as constitutional/legal right; (2) Tightened Emergency provisions — 'armed rebellion' replaced 'internal disturbance' for Art.352; (3) Strengthened Art.20/21 protection (cannot suspend even in NE); (4) Reversed many controversial 42nd Am provisions. Major reform Amendment.",
     "APPSC"),

    (5, "medium",
     "52nd Amendment 1985 added?\nతెలుగు: 52వ సవరణ?",
     "73rd Schedule (Panchayati Raj)",
     "10th Schedule — Anti-defection law / 10th Schedule Anti-defection (correct)",
     "Art.21A — Right to Education", "9th Schedule — Land reforms",
     "B",
     "52nd Amendment 1985 added 10th SCHEDULE — ANTI-DEFECTION LAW. Members elected on party ticket who DEFECT to another party LOSE their membership. Decided by Speaker/Chairman. Aimed to curb 'aaya ram gaya ram' culture. Modified by 91st Amendment 2003 (removed 1/3 split exemption; only 2/3 merger now exempt). Later upheld in Kihoto Hollohan (1992)."),

    (5, "easy",
     "61st Amendment 1989 changed?\nతెలుగు: 61వ సవరణ?",
     "Voting age 25 to 21",
     "Voting age 21 to 18 / ఓటు వయసు 21 → 18 (correct)",
     "Increased LS seats", "Extended RS term",
     "B",
     "61st Amendment 1989 reduced VOTING AGE from 21 to 18 YEARS through amendment of Article 326. Significantly expanded electorate by including young adults. Came into effect 28 March 1989. Aimed at involving youth in political process. India's voting age now aligned with most democracies.",
     "APPSC"),

    (5, "medium",
     "69th Amendment 1991 decided?\nతెలుగు: 69వ సవరణ?",
     "Mumbai special status",
     "Designated Delhi as NCT + Legislative Assembly + CoM / ఢిల్లీ NCT (correct)",
     "All UTs got Assemblies", "Delhi as 28th state",
     "B",
     "69th Amendment 1991: Designated DELHI as 'NATIONAL CAPITAL TERRITORY' (NCT). Added Art.239AA — gave Delhi a Legislative Assembly and Council of Ministers. Special UT status — NOT a full state. Centre retains control over public order, police, land. Subject to Lt Governor's role. Modified again by 2018 Govt of NCT of Delhi (Amendment) Act."),

    # ───── Section 6: Recent Major Amendments ─────
    (6, "easy",
     "73rd Amendment 1992 added?\nతెలుగు: 73వ సవరణ?",
     "Nagar Panchayats",
     "Constitutional status to Panchayati Raj — 11th Schedule / Panchayati Raj (correct)",
     "Cooperative societies", "Financial Emergency",
     "B",
     "73rd Amendment 1992 gave CONSTITUTIONAL STATUS to PANCHAYATI RAJ — added Part IX (Art.243-243O). Added 11th SCHEDULE listing 29 SUBJECTS for panchayat work. Mandatory three-tier system (Gram, Intermediate, District), regular elections, 33% reservation for women (now 50% in many states), reservation for SCs/STs. Operationalised Art.40 (Gandhian DPSP).",
     "APPSC"),

    (6, "easy",
     "74th Amendment 1992 introduced?\nతెలుగు: 74వ సవరణ?",
     "Panchayati Raj",
     "Constitutional status to Urban Local Bodies — 12th Schedule / Urban Local Bodies (correct)",
     "Women reservations", "GST Council",
     "B",
     "74th Amendment 1992 gave CONSTITUTIONAL STATUS to URBAN LOCAL BODIES — Nagar Panchayats, Municipal Councils, Municipal Corporations. Added Part IXA (Art.243P-243ZG); 12th SCHEDULE listing 18 SUBJECTS. Companion to 73rd Amendment. Together they decentralised governance to 3rd tier. Recent: 2024 elections show how this devolution operates.",
     "APPSC"),

    (6, "medium",
     "86th Amendment 2002 brought?\nతెలుగు: 86వ సవరణ?",
     "Education in DPSP",
     "Art.21A — Free education 6-14 as FR + Art.51A(k) parents' duty / Art.21A + Art.51A(k) (correct)",
     "Increased reservation in higher education",
     "Transferred education to local bodies",
     "B",
     "86th Amendment 2002: (1) Added Art.21A — Right to free and compulsory EDUCATION FOR CHILDREN 6-14 as FUNDAMENTAL RIGHT; (2) Modified Art.45 DPSP — now early childhood care for under-6; (3) Added Art.51A(k) — Fundamental Duty of every parent/guardian to provide educational opportunities to child 6-14. RTE Act 2009 implements. Came into force 1 April 2010."),

    (6, "medium",
     "91st Amendment 2003 added?\nతెలుగు: 91వ సవరణ?",
     "Private institution reservations",
     "Strengthened anti-defection + Cabinet size limit (15% or min 12) / Cabinet size 15% (correct)",
     "Urban Local Body powers",
     "Judges' appointment",
     "B",
     "91st Amendment 2003: (1) STRENGTHENED Anti-defection — REMOVED 1/3 split exemption (Para 3 of 10th Schedule); now only 2/3 merger protects from disqualification; (2) Limited CABINET SIZE — Centre + States: not exceeding 15% of total LS/Assembly strength (minimum 12 for states). Disqualified members cannot become Ministers. Curbed 'jumbo cabinets' used to accommodate defectors."),

    (6, "medium",
     "97th Amendment 2011 added?\nతెలుగు: 97వ సవరణ?",
     "EWS reservation",
     "Right to form cooperative societies — Art.19(1)(c); Art.43B DPSP; Part IXB / సహకార సంఘాలు (correct)",
     "Social-economic justice DPSP",
     "Online voting",
     "B",
     "97th Amendment 2011: (1) Added 'COOPERATIVE SOCIETIES' to Art.19(1)(c) — making formation of cooperatives a FR; (2) Added Art.43B (DPSP) — promoting cooperatives; (3) Added Part IXB (Art.243ZH-ZT) — constitutional status to cooperatives. Vipulbhai Chaudhary (2013): Part IXB partly STRUCK DOWN for not getting state ratification (since affected State List subjects). Art.19(1)(c) and Art.43B remain valid."),

    (6, "easy",
     "101st Amendment 2016 introduced?\nతెలుగు: 101వ సవరణ?",
     "Panchayati Raj status",
     "GST — Goods and Services Tax / GST (correct)",
     "Constitutional status to OBC Commission", "10% EWS",
     "B",
     "101st Amendment 2016 introduced GOODS AND SERVICES TAX (GST). Added Art.246A (concurrent power of Centre+State to levy GST), Art.269A (IGST), Art.279A (GST COUNCIL). 'ONE NATION — ONE TAX.' Effective 1 July 2017. GST Council = federal forum (Centre + all states). Simplified indirect tax — replaced 17 taxes. Major federal cooperative achievement.",
     "APPSC"),

    (6, "medium",
     "102nd Amendment 2018 introduced?\nతెలుగు: 102వ సవరణ?",
     "SC/ST Commission status",
     "NCBC constitutional status — Art.338B / NCBC Constitutional (correct)",
     "27% OBC reservation", "NCW status",
     "B",
     "102nd Amendment 2018: Gave CONSTITUTIONAL STATUS to NATIONAL COMMISSION FOR BACKWARD CLASSES (NCBC) — added Art.338B. Earlier NCBC was statutory (1993 Act). Also added Art.342A — President to specify socially and educationally backward classes for Central List (subject to Parliament's modification). Mandatory consultation with NCBC for OBC policy. Companion to 105th Amendment 2021 on state OBC powers."),

    (6, "easy",
     "103rd Amendment 2019 introduced?\nతెలుగు: 103వ సవరణ?",
     "SC/ST promotion reservation",
     "10% EWS reservation — Art.15(6), 16(6) / 10% EWS (correct)",
     "Private sector reservation", "5% additional OBC",
     "B",
     "103rd Amendment 2019: Added Art.15(6) and Art.16(6) — provided 10% RESERVATION for ECONOMICALLY WEAKER SECTIONS (EWS) of unreserved categories in education and government jobs. Family income < ₹8 lakh (current rules). Property limits also apply. CONSTITUTIONALLY UPHELD in Janhit Abhiyan v. UoI (Nov 2022) by 3:2 majority. Crosses 50% reservation cap.",
     "APPSC"),

    (6, "medium",
     "104th Amendment 2020 decided?\nతెలుగు: 104వ సవరణ?",
     "LS seats 543 to 600",
     "Extended SC/ST reservation in legislatures by 10 years (till 2030) + Removed Anglo-Indian nomination / SC/ST 10 సం. + Anglo-Indian తొలగింపు (correct)",
     "Constitutional status to OBC", "Removed 'Socialist' from Preamble",
     "B",
     "104th Amendment 2020: (1) EXTENDED reservation of seats for SC/ST in Lok Sabha and State Legislative Assemblies by 10 years — till 25 January 2030 (under Art.334); (2) DISCONTINUED nomination of ANGLO-INDIAN community to LS and State Assemblies (Art.331, 333). The Anglo-Indian nomination provision was originally meant for 10 years but had been periodically extended. Now ended."),

    # ───── Section 7: PYQ Comprehensive ─────
    (7, "hard",
     "Which does NOT require state ratification?\nతెలుగు: రాష్ట్రాల ఆమోదం అవసరం లేనిది?",
     "Manner of election of President",
     "Distribution of 7th Schedule",
     "Fundamental Rights / FRs (correct)",
     "Extent of executive power of Union/States",
     "C",
     "FRs amendment requires only SPECIAL MAJORITY — NO state ratification. Why? FRs concern citizen-state relationship, not federal balance. Other 3 options ARE federal in nature: Election of President (Art.54-55), 7th Schedule (legislative distribution), Extent of executive power (Art.73, 162) — all require state ratification. Standard exam question on amendment procedure."),

    (7, "hard",
     "Which is correct about Constitutional Amendment procedure?\nతెలుగు: సరైనది?",
     "State legislature can introduce",
     "No amendments during Emergency",
     "Centre-State legislative distribution by Simple Majority",
     "After State ratification, no need to re-present to Parliament — goes directly to President / రాష్ట్రాల ఆమోదం తర్వాత నేరుగా President కు (correct)",
     "D",
     "Standard procedure: Bill in Parliament → Pass with Special Majority by both Houses (separately) → If federal: ratification by half of state legislatures (any time, no limit) → Goes DIRECTLY to PRESIDENT for assent (24th Am made assent mandatory). State legislatures CANNOT introduce; amendments can be made during Emergency (42nd was during Emergency); Centre-State distribution = Special Majority + ratification (NOT simple)."),

    (7, "hard",
     "Key distinction between 42nd and 44th Amendments?\nతెలుగు: 42వ vs 44వ?",
     "Republic Day vs Independence Day",
     "42nd = Indira Gandhi (Congress) Emergency-era expansion; 44th = Morarji Desai (Janata) reversed many provisions + removed Right to Property / 42వ = విస్తరణ; 44వ = తిరోగమనం (correct)",
     "SC/ST vs OBC reservation",
     "GST vs Panchayati Raj",
     "B",
     "42nd Amendment 1976 (INDIRA GANDHI/Congress, during EMERGENCY): MAJOR EXPANSION — added FDs, Socialist-Secular-Integrity in Preamble, declared absolute amendment power, strengthened DPSPs, extended LS term to 6 years, added tribunals. 44th Amendment 1978 (MORARJI DESAI/Janata, post-Emergency): REVERSED many controversial 42nd Am provisions; removed Right to Property; tightened Emergency procedures (Cabinet written advice for NE; armed rebellion replaces internal disturbance)."),

    (7, "hard",
     "Which Amendment-Outcome pair is INCORRECT?\nతెలుగు: తప్పు జంట?",
     "42nd Am 1976 → Added 'Socialist, Secular, Integrity' to Preamble",
     "52nd Am 1985 → 10th Schedule (Anti-defection)",
     "86th Am 2002 → Art.21A (Right to Education 6-14)",
     "101st Am 2016 → Constitutional status to Panchayati Raj / 101 = Panchayati Raj (correct = INCORRECT pair)",
     "D",
     "INCORRECT pair: 101st Amendment 2016 introduced GST (NOT Panchayati Raj). Panchayati Raj got constitutional status through 73rd Amendment 1992 (Urban Local Bodies through 74th Amendment 1992). Other pairs ARE correct: 42nd → Socialist-Secular-Integrity in Preamble; 52nd → 10th Schedule (Anti-defection); 86th → Art.21A (RTE)."),

    (7, "hard",
     "Correct sequence of Basic Structure cases?\nతెలుగు: BS క్రమం?",
     "Shankari Prasad (1951) → Golaknath (1967) → Kesavananda Bharati (1973) → Minerva Mills (1980) (correct)",
     "Golaknath → Shankari Prasad → KB → MM",
     "KB → SP → GN → MM",
     "MM → GN → KB → SP",
     "A",
     "CHRONOLOGICAL SEQUENCE: (1) SHANKARI PRASAD 1951 — Parliament can amend FRs. (2) SAJJAN SINGH 1964 — upheld Shankari Prasad. (3) GOLAKNATH 1967 — Parliament CANNOT amend FRs. (4) 24th Amendment 1971 — restored Parliament's power. (5) KESAVANANDA BHARATI 1973 — Basic Structure Doctrine — Parliament can amend FRs but not destroy Basic Structure. (6) MINERVA MILLS 1980 — limited power; harmony FR-DPSP is BS. (7) IR Coelho 2007 — 9th Schedule post-1973 subject to BS test."),
]



import json as _json


def _seed_polity_ch11_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    import json as _j
    ph = '%s' if use_postgres else '?'
    _sections = [
    {"title": "11.1 ప్రాథమిక అంశాలు — Art 368", "sub": "Art 368 · Part XX · Amendment Procedure · Constitutional Law", "audio": ""},
    {"title": "11.2 సాధారణ మెజారిటీ సవరణలు", "sub": "Simple Majority · Art 4 · Art 169 · Art 239A · Schedules", "audio": ""},
    {"title": "11.3 ప్రత్యేక మెజారిటీ సవరణలు", "sub": "Special Majority · 2/3 + 1/2 · Art 368 · Most Provisions", "audio": ""},
    {"title": "11.4 రాష్ట్రాల ఆమోదం అవసరమయ్యే సవరణలు", "sub": "State Ratification · Half States · Federal Provisions · Art 54 · Art 75", "audio": ""},
    {"title": "11.5 మూల నిర్మాణ సిద్ధాంతం", "sub": "Basic Structure · Shankari Prasad · Sajjan Singh · Golaknath · Kesavananda", "audio": ""},
    {"title": "11.6 ముఖ్య సవరణలు భాగం I (1-69వ)", "sub": "1st Amendment · 7th · 9th · 24th · 25th · 42nd · 44th · 52nd · 61st · 69th", "audio": ""},
    {"title": "11.7 ముఖ్య సవరణలు భాగం II (73-104వ)", "sub": "73rd · 74th · 86th · 91st · 97th · 99th · 100th · 101st · 102nd · 103rd · 104th", "audio": ""},
    {"title": "11.8 కఠిన ప్రశ్నలు", "sub": "Tough MCQs · Waman Rao 1981 · IR Coelho · Amendment Sequences", "audio": ""}
]
    try:
        conn.execute("""CREATE TABLE IF NOT EXISTS study_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL DEFAULT 'GK',
            topic TEXT NOT NULL DEFAULT '',
            subtopic TEXT NOT NULL DEFAULT '',
            chapter_num INTEGER NOT NULL DEFAULT 0,
            chapter_title_te TEXT NOT NULL DEFAULT '',
            chapter_title_en TEXT NOT NULL DEFAULT '',
            pages_ref TEXT NOT NULL DEFAULT '',
            sections_json TEXT NOT NULL DEFAULT '[]',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")
        if use_postgres: conn.commit()
    except Exception:
        pass

    cur = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (11, 'Indian_Polity'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True,
                'message': 'Polity Ch11 notes already seeded.'}
    if row and force:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (11, 'Indian_Polity'))
    if use_postgres:
        conn.commit()

    db_exec_fn(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'Indian_Polity', '', 11,
         'రాజ్యాంగ సవరణ',
         'Amendment of the Constitution',
         'Ch.11',
         _j.dumps(_sections, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'Polity Ch11 notes seeded!'}


def _seed_polity_ch11_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
    ph = '%s' if use_postgres else '?'

    try:
        conn.execute("""CREATE TABLE IF NOT EXISTS chapter_mcqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            study_note_id INTEGER NOT NULL,
            section_idx INTEGER NOT NULL DEFAULT 0,
            difficulty INTEGER NOT NULL DEFAULT 1,
            exam_type TEXT NOT NULL DEFAULT 'General',
            q_te TEXT NOT NULL,
            opt_a TEXT NOT NULL,
            opt_b TEXT NOT NULL,
            opt_c TEXT NOT NULL,
            opt_d TEXT NOT NULL,
            correct TEXT NOT NULL,
            explanation_te TEXT NOT NULL DEFAULT '',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")
        if use_postgres: conn.commit()
    except Exception:
        pass

    cur = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (11, 'Indian_Polity'))
    row = cur.fetchone()
    if not row:
        _seed_polity_ch11_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)
        cur = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (11, 'Indian_Polity'))
        row = cur.fetchone()

    note_id = row_to_dict_fn(row)['id']
    db_exec_fn(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))

    insert_sql = (
        f"INSERT INTO chapter_mcqs "
        f"(study_note_id, section_idx, difficulty, exam_type, "
        f"q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    )

    diff_map = {"easy": 1, "medium": 2, "hard": 3, "toughest": 4,
                 1: 1, 2: 2, 3: 3, 4: 4}
    easy = medium = hard = toughest = pyq = 0
    for mcq in POLITY_CH11_MCQS:
        sec_idx, diff, q, a, b, c, d, correct, expl = mcq[:9]
        exam_type = mcq[9] if len(mcq) > 9 else 'General'
        diff_int = diff_map.get(diff, 2) if not isinstance(diff, int) else diff
        db_exec_fn(conn, insert_sql,
                   (note_id, sec_idx, diff_int, exam_type, q, a, b, c, d,
                    str(correct).lower(), expl))
        if exam_type in ('APPSC', 'UPSC'):
            pyq += 1
        elif diff_int == 1: easy += 1
        elif diff_int == 2: medium += 1
        elif diff_int == 3: hard += 1
        elif diff_int == 4: toughest += 1

    if use_postgres: conn.commit()
    conn.commit()

    total = len(POLITY_CH11_MCQS)
    return {
        'success': True,
        'message': f'Polity Ch11 MCQs seeded! Total: {total}',
        'inserted': total,
        'easy': easy, 'medium': medium, 'hard': hard,
        'toughest': toughest, 'pyq': pyq
    }
