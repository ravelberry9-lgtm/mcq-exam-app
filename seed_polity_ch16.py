# seed_polity_ch16.py
# Chapter 16 – Vice President of India
# (భారత ఉపరాష్ట్రపతి)
# Lakshmikanth's Indian Polity | APPSC Group 2 Standard
# Total Sections: 8 | Total MCQs: 45 | PYQs: 5
# Difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
# ─────────────────────────────────────────────────────

import json as _json

POLITY_CH16_SECTIONS = [
    {
        "title": "16.1 ఉపరాష్ట్రపతి — ఎన్నిక మరియు అర్హతలు",
        "sub": "Art.63–66 · Electoral College (Both Houses MPs incl. Nominated) · STV · Qualifications",
        "audio": ""
    },
    {
        "title": "16.2 పదవీ కాలం మరియు తొలగింపు",
        "sub": "Art.67 · 5 Years · Resignation to President · RS Effective Majority + LS Simple Majority · 14 Days Notice",
        "audio": ""
    },
    {
        "title": "16.3 రాజ్యసభ చైర్మన్ పాత్ర",
        "sub": "Art.64 · Ex-officio Chairman · Casting Vote · Not RS Member · Joint Sitting · Art.89",
        "audio": ""
    },
    {
        "title": "16.4 తాత్కాలిక రాష్ట్రపతి బాధ్యతలు",
        "sub": "Art.65 · Acting President · Vacancy · Absence · Salary Continues as Chairman · CJI if Both Vacant",
        "audio": ""
    },
    {
        "title": "16.5 వేతనం, ప్రమాణం మరియు హక్కులు",
        "sub": "Art.69 · Oath by President · Salary as RS Chairman · Official Residence · Perks",
        "audio": ""
    },
    {
        "title": "16.6 రాష్ట్రపతి vs ఉపరాష్ట్రపతి — పోలిక",
        "sub": "Electoral College · Qualifications · Resignation · Removal · Oath · Salary · Differences",
        "audio": ""
    },
    {
        "title": "16.7 ముఖ్యమైన ఉపరాష్ట్రపతులు",
        "sub": "Radhakrishnan · Zakir Husain · V.V. Giri · B.D. Jatti · M. Hidayatullah · Hamid Ansari · Dhankhar",
        "audio": ""
    },
    {
        "title": "16.8 కఠిన ప్రశ్నలు — APPSC/UPSC PYQs",
        "sub": "Electoral College Details · Removal Procedure · Comparison Questions · PYQ Analysis",
        "audio": ""
    },
]

POLITY_CH16_MCQS = [

    # ══════════════ SECTION 0 — Election & Qualifications ══════════════

    (0, 1,
     "Which Article establishes the office of Vice President of India?\nతెలుగు: ఉపరాష్ట్రపతి పదవి Article?",
     "Art.52",
     "Art.63 (correct)",
     "Art.66",
     "Art.69",
     "b",
     "Art.63: 'There shall be a Vice President of India.' Art.64: VP is ex-officio Chairman of Rajya Sabha. Art.65: VP acts as President. Art.66: Election method. Art.67: Term/removal. Art.69: Oath."),

    (0, 1,
     "Who forms the Electoral College for Vice Presidential election?\nతెలుగు: ఉపరాష్ట్రపతి ఎలక్టోరల్ కాలేజ్?",
     "Elected MPs + State MLAs / MP లు + MLA లు",
     "Only elected MPs of both Houses / ఎన్నికైన MP లు మాత్రమే",
     "All members of both Houses — elected AND nominated / ఎన్నికైన + నామినేటెడ్ MP లు (correct)",
     "Only Rajya Sabha members / RS మాత్రమే",
     "c",
     "Art.66(1): VP elected by ALL members (elected + nominated) of BOTH Houses of Parliament. State MLAs do NOT participate. Compare: Presidential election uses elected MPs + elected MLAs (NO nominated members)."),

    (0, 2,
     "Do State Legislative Assembly members (MLAs) participate in VP election?\nతెలుగు: VP ఎన్నికలో MLA లు?",
     "Yes, all states / అన్ని రాష్ట్రాల MLA లు",
     "Yes, only 28 states / 28 రాష్ట్రాలు",
     "No — MLAs do NOT participate / కాదు, MLA లు పాల్గొనరు (correct)",
     "Yes, only Delhi & Puducherry / ఢిల్లీ + పుదుచ్చేరి",
     "c",
     "MLAs do NOT participate in VP election. KEY DIFFERENCE: President election = MPs (elected only) + MLAs (elected only); VP election = MPs only (both elected AND nominated). Reason: VP has only ceremonial-federal role of presiding RS."),

    (0, 1,
     "Do nominated members of Parliament vote in VP election?\nతెలుగు: నామినేటెడ్ సభ్యులు VP ఎన్నికలో?",
     "No / కాదు",
     "Yes — nominated members DO participate / అవును, పాల్గొంటారు (correct)",
     "Only RS nominated / RS నామినేటెడ్ మాత్రమే",
     "Only LS nominated / LS నామినేటెడ్",
     "b",
     "In VP election, nominated members of BOTH Houses DO PARTICIPATE — UNLIKE Presidential election where nominated members are EXCLUDED. This is a key difference between the two elections."),

    (0, 1,
     "Qualifications for VP under Art.66(3)?\nతెలుగు: ఉపరాష్ట్రపతి అర్హతలు?",
     "Indian citizen, 35 years, eligible for LS / 35 సం. + LS",
     "Indian citizen, 30 years, eligible for RS / 30 సం. + RS",
     "Indian citizen, 35 years, eligible for RS membership, no office of profit / 35 సం. + RS అర్హత + లాభదాయక పదవి లేదు (correct)",
     "Indian citizen, 25 years, eligible for RS / 25 సం. + RS",
     "c",
     "Art.66(3) Qualifications: (1) Citizen of India; (2) 35 years completed; (3) Eligible for RAJYA SABHA membership (NOT LS — key difference from President's Art.58 LS qualification); (4) No office of profit."),

    (0, 2,
     "Key qualification difference between VP and President?\nతెలుగు: అర్హత తేడా?",
     "VP 30 years; President 35 years / 30 vs 35",
     "VP eligible for RS; President eligible for LS / VP=RS, President=LS (correct)",
     "VP needs 40 years / 40 సం.",
     "VP must be Parliament member / Parliament సభ్యుడు",
     "b",
     "KEY DIFFERENCE: President (Art.58) must be eligible for LS membership; VP (Art.66(3)) must be eligible for RS membership. Age 35 same for both. All other qualifications similar (citizen, no office of profit)."),

    (0, 1,
     "Method of VP election?\nతెలుగు: VP ఎన్నిక పద్ధతి?",
     "Direct election by citizens / ప్రజలచే ప్రత్యక్ష",
     "Simple majority FPTP / FPTP",
     "Proportional Representation by Single Transferable Vote (STV), secret ballot / STV రహస్య బ్యాలెట్ (correct)",
     "Show of hands / చేతులెత్తడం",
     "c",
     "Art.66(1): VP election uses Proportional Representation with Single Transferable Vote (STV) using secret ballot — same method as Presidential election. Quota = (Total valid votes / 2) + 1."),

    (0, 2,
     "How many proposers and seconders are required for VP nomination?\nతెలుగు: VP నామినేషన్ ప్రతిపాదకులు?",
     "25 + 25, ₹10,000 / 25 + 25",
     "50 + 50, ₹15,000 / 50 + 50",
     "20 proposers + 20 seconders + ₹15,000 deposit / 20 + 20 + ₹15,000 (correct)",
     "100 + 100 / 100 + 100",
     "c",
     "VP nomination: 20 proposers + 20 seconders (from Electoral College i.e. MPs) + ₹15,000 security deposit. Compare: Presidential election needs 50 proposers + 50 seconders (from full Electoral College of MPs+MLAs)."),

    (0, 3,
     "Who adjudicates disputes regarding VP election?\nతెలుగు: VP ఎన్నిక వివాదాలు?",
     "President / రాష్ట్రపతి",
     "High Court / HC",
     "Supreme Court — Art.71 / SC (correct)",
     "Election Commission / EC",
     "c",
     "Art.71: Disputes arising out of election of President AND Vice President shall be inquired into and decided by the Supreme Court — SC has original jurisdiction. Decision is FINAL."),

    (0, 2,
     "Who conducts the Vice Presidential election?\nతెలుగు: VP ఎన్నిక ఎవరు నిర్వహిస్తారు?",
     "VP has no role for Election Commission / EC పాత్ర లేదు",
     "Election Commission of India conducts and fixes the date / ECI నిర్వహిస్తుంది (correct)",
     "President directly conducts / రాష్ట్రపతి",
     "Lok Sabha Speaker / LS స్పీకర్",
     "b",
     "ELECTION COMMISSION OF INDIA conducts the VP election — same as Presidential election. EC fixes nomination/polling/counting dates. Returning Officer is appointed by EC by rotation between Secretary General of LS and RS."),

    # ══════════════ SECTION 1 — Term, Resignation, Removal ══════════════

    (1, 1,
     "Term of office of the Vice President?\nతెలుగు: VP పదవీ కాలం?",
     "4 years",
     "5 years (correct)",
     "6 years",
     "Decided by Parliament / Parliament నిర్ణయిస్తుంది",
     "b",
     "Art.67(a): VP holds office for 5 YEARS from the date of entering office. Eligible for re-election (no limit on terms)."),

    (1, 1,
     "To whom does the VP submit resignation?\nతెలుగు: VP రాజీనామా ఎవరికి?",
     "LS Speaker / LS స్పీకర్",
     "RS Chairman / RS చైర్మన్",
     "President — Art.67(a) / రాష్ట్రపతి (correct)",
     "PM / ప్రధాని",
     "c",
     "Art.67(a): VP resigns by writing under his hand to the PRESIDENT. Compare: President resigns by writing to the VICE PRESIDENT. So they resign to each other!"),

    (1, 2,
     "Procedure for removal of the Vice President?\nతెలుగు: VP తొలగింపు విధానం?",
     "Constitutional amendment only / రాజ్యాంగ సవరణ",
     "RS special majority + LS agreement / RS Special Majority + LS",
     "RS Effective Majority resolution + 14 days notice + LS Simple Majority agreement / RS Effective + 14 రోజులు + LS Simple (correct)",
     "Both Houses 2/3 majority / రెండు సభలలో 2/3",
     "c",
     "Art.67(b) VP Removal: Step 1 — Resolution moved in RS by Effective Majority (>50% of total RS membership). Step 2 — 14 days notice given. Step 3 — LS agrees by Simple Majority. NO specific ground required (unlike Presidential Impeachment)."),

    (1, 2,
     "How many days' notice is required before a VP removal resolution?\nతెలుగు: VP తొలగింపు నోటీసు?",
     "7 days / 7",
     "10 days / 10",
     "14 days advance notice — Art.67(b) / 14 రోజులు (correct)",
     "30 days / 30",
     "c",
     "Art.67(b): At least 14 DAYS' ADVANCE NOTICE must be given before moving resolution for VP removal. Same notice period as Presidential Impeachment (Art.61)."),

    (1, 3,
     "What majority is required in RS for VP removal?\nతెలుగు: VP తొలగింపు RS మెజారిటీ?",
     "2/3 of present and voting / 2/3 హాజరైన",
     "2/3 of total RS membership / 2/3 మొత్తం",
     "Effective Majority — majority of total RS membership / Effective Majority (correct)",
     "2/3 of total Parliament / 2/3 Parliament",
     "c",
     "Art.67(b): RS passes resolution by EFFECTIVE MAJORITY = majority of TOTAL RS membership (i.e. >50% of all members). LS then agrees by SIMPLE MAJORITY. This is LESS stringent than Presidential Impeachment which needs 2/3 of total membership in both Houses."),

    (1, 3,
     "Key difference between Presidential Impeachment and VP Removal?\nతెలుగు: Impeachment vs VP Removal?",
     "Both need 2/3 majority / రెండూ 2/3",
     "President needs 1/4 notice + 2/3 in both Houses for constitutional violation; VP removal: no ground required + RS Effective Majority + LS agreement / President = ground+2/3; VP = no ground+Effective (correct)",
     "Both decided in RS only / RS మాత్రమే",
     "VP needs court / VP కు కోర్టు",
     "b",
     "Differences: (1) GROUND — President needs 'violation of Constitution'; VP removal NO ground needed. (2) NOTICE — President 1/4 of House; VP 14 days. (3) MAJORITY — President 2/3 of total in BOTH Houses; VP RS Effective Majority + LS Simple Majority. (4) STARTING HOUSE — President any House; VP only RS."),

    # ══════════════ SECTION 2 — VP as RS Chairman ══════════════

    (2, 1,
     "Under which Article is VP the ex-officio Chairman of RS?\nతెలుగు: VP RS Chairman Article?",
     "Art.63",
     "Art.64 (correct)",
     "Art.65",
     "Art.89",
     "b",
     "Art.64: VP is ex-officio Chairman of Rajya Sabha. Art.89(1) confirms this. Art.65 = Acting President when Pres. office vacant. Art.63 = Office of VP. Art.69 = Oath."),

    (2, 1,
     "Is the VP a member of Rajya Sabha?\nతెలుగు: VP RS సభ్యుడా?",
     "Yes, RS member / అవును",
     "No — VP is NOT a member of RS, only its Chairman / కాదు, చైర్మన్ మాత్రమే (correct)",
     "Yes, as nominated / నామినేటెడ్",
     "Member when needed / అవసరమైనప్పుడు",
     "b",
     "VP, though Chairman of RS, is NOT A MEMBER of RS. Therefore CANNOT vote in normal proceedings. Only has CASTING VOTE in case of tie. (Compare LS Speaker who IS an LS member but follows same convention not to vote ordinarily.)"),

    (2, 2,
     "When can the VP/RS Chairman cast a vote?\nతెలుగు: VP ఓటు ఎప్పుడు?",
     "Every voting / ప్రతి ఓటింగ్",
     "Only when has RS membership / RS సభ్యత్వం ఉన్నప్పుడు",
     "Only in case of tie — Casting Vote / Tie అయినప్పుడు Casting Vote (correct)",
     "Important Bills only / ముఖ్యమైన బిల్లులు",
     "c",
     "Art.100(1): RS Chairman/VP does NOT vote in ordinary proceedings (since not a member). Casts Casting Vote ONLY when there is a TIE — to break the deadlock. Same convention as LS Speaker."),

    (2, 2,
     "Does the VP preside over a Joint Sitting of Parliament?\nతెలుగు: Joint Sitting లో అధ్యక్షత?",
     "Yes, VP presides as RS Chairman / VP అధ్యక్షత",
     "No — Speaker of Lok Sabha presides over Joint Sitting (Art.118) / LS స్పీకర్ అధ్యక్షత (correct)",
     "President decides / రాష్ట్రపతి",
     "VP and Speaker alternate / మారు మారు",
     "b",
     "Art.118(4): SPEAKER OF LOK SABHA presides over Joint Sitting (Art.108). NOT the VP/RS Chairman. If Speaker absent, Deputy Speaker; if both absent, Deputy Chairman of RS; if all absent, any other member chosen."),

    (2, 2,
     "What power does the VP have over Money Bills?\nతెలుగు: VP & Money Bill?",
     "VP decides / VP నిర్ణయిస్తారు",
     "Money Bill can be introduced in RS / RS లో",
     "VP has no special power — Speaker of LS certifies Money Bills (Art.110(3)) / VP కు అధికారం లేదు (correct)",
     "VP can veto / Veto వేయగలరు",
     "c",
     "VP has NO special power over Money Bills. Art.110(3): LS SPEAKER certifies whether a Bill is a Money Bill — final decision. Money Bills can only be introduced in LS. RS can only RECOMMEND amendments within 14 days."),

    (2, 3,
     "Can VP preside over RS when removal resolution against them is pending?\nతెలుగు: VP తొలగింపు pending లో?",
     "Yes always / అవును",
     "No, cannot sit / కూర్చోలేరు",
     "Can preside generally; cannot preside over debate on the removal motion itself / సాధారణంగా అవును, కానీ removal చర్చపై కాదు (correct)",
     "Yes but members cannot participate / అవును, సభ్యులు పాల్గొనరు",
     "c",
     "Art.92(1): When a resolution for VP's removal is under consideration, VP shall NOT preside, though may speak/take part in proceedings (but cannot vote even in casting). General Chair duties continue otherwise."),

    (2, 2,
     "Who decides disqualification of RS members under Anti-Defection Law?\nతెలుగు: RS Anti-Defection ఎవరు?",
     "LS Speaker / LS స్పీకర్",
     "RS Chairman (VP) / RS Chairman (VP) (correct)",
     "President / రాష్ట్రపతి",
     "Supreme Court / SC",
     "b",
     "10th Schedule (52nd Amendment 1985): Disqualification of LS members → LS Speaker; Disqualification of RS members → RS Chairman (VP). Kihoto Hollohan (1992) made these decisions subject to JUDICIAL REVIEW."),

    # ══════════════ SECTION 3 — VP as Acting President ══════════════

    (3, 1,
     "Under which Article does VP act as President?\nతెలుగు: VP Acting President?",
     "Art.63",
     "Art.64",
     "Art.65 (correct)",
     "Art.67",
     "c",
     "Art.65: VP acts as President when (a) Presidential office is VACANT (death/resignation/removal), or (b) President is UNABLE to discharge functions due to absence/illness/any other cause. Acts until new President elected (within 6 months of vacancy)."),

    (3, 2,
     "What salary does VP receive while acting as President?\nతెలుగు: Acting President జీతం?",
     "VP salary / VP జీతం",
     "Receives President's salary and emoluments / రాష్ట్రపతి జీతం (correct)",
     "Both combined / రెండూ",
     "No salary / జీతం లేదు",
     "b",
     "Art.65(3): While acting/discharging Presidential functions, VP receives all SALARY, ALLOWANCES, PRIVILEGES of the President — and resides in Rashtrapati Bhavan. Does NOT get VP/RS Chairman salary during this period."),

    (3, 2,
     "Who acts as President when both President and VP offices are vacant?\nతెలుగు: ఇద్దరూ ఖాళీ అయితే?",
     "LS Speaker / LS స్పీకర్",
     "RS Deputy Chairman / RS Deputy",
     "Chief Justice of India (CJI) / CJI (correct)",
     "PM / ప్రధాని",
     "c",
     "Art.65 read with President (Discharge of Functions) Act 1969: If both President and VP offices are vacant, CHIEF JUSTICE OF INDIA acts as President. If CJI also unavailable, the senior-most Supreme Court judge available acts."),

    (3, 3,
     "Who acted as President when Fakhruddin Ali Ahmed died in 1977?\nతెలుగు: 1977 ఎవరు Acting?",
     "V.V. Giri",
     "N. Sanjiva Reddy",
     "B.D. Jatti — VP at that time / B.D. జట్టీ (correct)",
     "Morarji Desai",
     "c",
     "When President Fakhruddin Ali Ahmed DIED IN OFFICE in February 1977, B.D. Jatti (Basappa Danappa Jatti — then VP) acted as President from 11 Feb 1977 till 25 July 1977 — until N. Sanjiva Reddy was elected unanimously as new President."),

    (3, 3,
     "Why did V.V. Giri resign as VP in 1969?\nతెలుగు: V.V. గిరి రాజీనామా?",
     "Health reasons / ఆరోగ్యం",
     "To contest 1969 Presidential election as independent / రాష్ట్రపతి ఎన్నికలో పోటీ (correct)",
     "Differences with PM / PM తో విభేదాలు",
     "Party direction / పార్టీ ఆదేశం",
     "b",
     "V.V. Giri resigned as VP in 1969 to contest the Presidential election as an INDEPENDENT against official Congress candidate Neelam Sanjiva Reddy. After his resignation, M. Hidayatullah (CJI) acted as President. Giri won via SECOND PREFERENCE votes under STV."),

    # ══════════════ SECTION 4 — Oath, Salary, Residence ══════════════

    (4, 1,
     "In whose presence does the VP take oath of office?\nతెలుగు: VP ప్రమాణం?",
     "CJI / CJI",
     "President — Art.69 / రాష్ట్రపతి (correct)",
     "LS Speaker / LS స్పీకర్",
     "RS Deputy Chairman / Deputy Chairman",
     "b",
     "Art.69: VP takes oath before the PRESIDENT or person appointed by the President. Compare: President takes oath before CJI (Art.60). VP swears to 'bear true faith and allegiance to the Constitution... and faithfully discharge duties.'"),

    (4, 2,
     "In what capacity does the VP receive salary?\nతెలుగు: VP జీతం హోదా?",
     "Separate VP salary / ప్రత్యేక జీతం",
     "Salary as RS Chairman — no separate VP salary / RS Chairman హోదాలో (correct)",
     "Half of President's salary / రాష్ట్రపతి సగం",
     "Special salary fixed by Parliament / ప్రత్యేక Parliament జీతం",
     "b",
     "VP has NO separate salary as VP per se. Receives salary, allowances, perks AS CHAIRMAN OF RAJYA SABHA. This is unique — Constitution doesn't provide a 'VP-specific' salary. Currently ₹4 lakh/month + perks. Charged on Consolidated Fund."),

    (4, 1,
     "Official residence of the VP?\nతెలుగు: VP అధికారిక నివాసం?",
     "Rashtrapati Bhavan / రాష్ట్రపతి భవన్",
     "PM's residence / PM నివాసం",
     "6, Maulana Azad Road, New Delhi (correct)",
     "10 Janpath / 10 జనపథ్",
     "c",
     "VP's official residence is 6, MAULANA AZAD ROAD, NEW DELHI. While acting as President, VP resides at Rashtrapati Bhavan. Vice President's House (Upa-Rashtrapati Nivas) is the proper name."),

    (4, 3,
     "Can the VP address both Houses of Parliament?\nతెలుగు: ఉభయ సభలలో ప్రసంగం?",
     "Only RS / RS మాత్రమే",
     "Only LS / LS మాత్రమే",
     "Both Houses but cannot vote — not a member of either / ఉభయ సభలలో, ఓటు లేదు (correct)",
     "No power / అధికారం లేదు",
     "c",
     "VP can speak/address either House of Parliament but CANNOT VOTE in either (not a member of either House). Only has casting vote as RS Chairman. Compare: PM/Ministers can speak in both Houses but vote only in their own."),

    # ══════════════ SECTION 5 — President vs VP Comparisons ══════════════

    (5, 2,
     "Electoral College difference between Presidential and VP elections?\nతెలుగు: Electoral College తేడా?",
     "Same EC for both / రెండింటికీ ఒకటే",
     "President: Elected MPs + Elected MLAs; VP: All MPs (elected + nominated) — NO MLAs / రాష్ట్రపతి = MP+MLA, VP = MP మాత్రమే (correct)",
     "VP: only MLAs / VP = MLA లు మాత్రమే",
     "Both use MPs and MLAs / రెండింటికీ MP+MLA",
     "b",
     "President EC: Elected members of Parliament (LS+RS) + Elected MLAs of all states + Elected MLAs of NCT Delhi & Puducherry. NOMINATED EXCLUDED. VP EC: ALL MPs of both Houses (elected + NOMINATED). NO MLAs. This is THE KEY DIFFERENCE."),

    (5, 2,
     "What qualification is COMMON to both President and VP?\nతెలుగు: ఉమ్మడి అర్హత?",
     "LS membership eligibility / LS అర్హత",
     "RS membership eligibility / RS అర్హత",
     "35 years of age, Indian citizen, no office of profit / 35 సం. + పౌరుడు + లాభదాయక పదవి లేదు (correct)",
     "30 years / 30 సం.",
     "c",
     "COMMON to both: (1) Citizen of India, (2) 35 years completed, (3) No office of profit. DIFFERENCE: President eligible for LS membership (Art.58); VP eligible for RS membership (Art.66(3))."),

    (5, 3,
     "How does the oath differ between President and VP?\nతెలుగు: ప్రమాణం తేడా?",
     "Both before CJI / రెండూ CJI",
     "President: oath before CJI (Art.60); VP: oath before President (Art.69) / President = CJI; VP = President (correct)",
     "Both before President / రెండూ President",
     "Both before LS Speaker / LS స్పీకర్",
     "b",
     "Art.60: President's oath BEFORE CJI (or senior-most SC judge available). Art.69: VP's oath BEFORE PRESIDENT (or person appointed by President). Both swear allegiance to Constitution and faithful discharge of duties."),

    (5, 2,
     "Common feature between Presidential Impeachment and VP Removal?\nతెలుగు: ఉమ్మడి అంశం?",
     "Both 2/3 majority / రెండూ 2/3",
     "Both 1/4 notice / 1/4 నోటీసు",
     "Both require 14 days advance notice / రెండూ 14 రోజులు (correct)",
     "Both need constitutional violation / రాజ్యాంగ ఉల్లంఘన",
     "c",
     "COMMON: 14 DAYS' ADVANCE NOTICE required in both. DIFFERENCES: (1) Ground — President needs 'violation of Constitution'; VP no specific ground. (2) Initiating House — President any House; VP only RS. (3) Majority — President 2/3 of total in BOTH; VP RS Effective Majority + LS Simple Majority."),

    # ══════════════ SECTION 6 — Historical Personalities ══════════════

    (6, 1,
     "Who was the first Vice President of India?\nతెలుగు: మొదటి ఉపరాష్ట్రపతి?",
     "Zakir Husain / జాకీర్ హుసేన్",
     "V.V. Giri / V.V. గిరి",
     "Dr. Sarvepalli Radhakrishnan — 1952–62 / డా. రాధాకృష్ణన్ (correct)",
     "B.D. Jatti / B.D. జట్టీ",
     "c",
     "Dr. Sarvepalli Radhakrishnan — first VP of India (1952–1962) — served TWO terms. Subsequently elected 2nd President (1962–1967). His birthday (5 Sep) is celebrated as Teachers' Day. Famous philosopher."),

    (6, 2,
     "Which VPs later became Presidents of India?\nతెలుగు: VP నుండి President?",
     "V.V. Giri & Zakir Husain only / V.V. గిరి, జాకీర్ హుసేన్",
     "Radhakrishnan, Zakir Husain, V.V. Giri, R. Venkataraman, K.R. Narayanan / 5 మంది (correct)",
     "Hamid Ansari & Venkaiah Naidu / హమీద్ అన్సారీ, వెంకయ్య నాయుడు",
     "Only Zakir Husain / జాకీర్ హుసేన్",
     "b",
     "VPs who later became Presidents (5): (1) Radhakrishnan (2nd Pres), (2) Zakir Husain (3rd Pres), (3) V.V. Giri (4th Pres), (4) R. Venkataraman (8th Pres), (5) K.R. Narayanan (10th Pres). Most recent VPs (Hamid Ansari, Venkaiah Naidu, Jagdeep Dhankhar) did NOT become Presidents."),

    (6, 2,
     "Who served as VP for the longest period?\nతెలుగు: ఎక్కువ కాలం?",
     "Dr. Radhakrishnan (2 terms)",
     "Hamid Ansari — 2 terms (2007–2017) / హమీద్ అన్సారీ (correct)",
     "Venkaiah Naidu / వెంకయ్య నాయుడు",
     "Krishna Kant / కృష్ణ కాంత్",
     "b",
     "HAMID ANSARI served two consecutive terms 2007–2017 = 10 YEARS — longest continuous tenure as VP in India. Dr. Radhakrishnan also served two terms 1952–1962 (~10 years) but Ansari is generally cited as having longest continuous tenure."),

    (6, 3,
     "What position did M. Hidayatullah hold before VP?\nతెలుగు: హిదాయతుల్లా VP ముందు?",
     "Chief Justice of India and acted as President / CJI + Acting President (correct)",
     "LS Speaker / LS స్పీకర్",
     "PM / ప్రధాని",
     "Governor / గవర్నర్",
     "a",
     "M. Hidayatullah: Was CJI (1968–70). When V.V. Giri resigned VP to contest Presidential election (1969), Hidayatullah as CJI acted as President (~1 month). Later became VP (1979–84). Acted as President AGAIN in 1982 during Zail Singh's heart surgery. Unique distinction: CJI + VP."),

    # ══════════════ SECTION 7 — Misc, Vote Value, Procedures ══════════════

    (7, 3,
     "Vote value of an MP in VP election?\nతెలుగు: MP ఓటు విలువ?",
     "Equal to MLA / MLA కి సమానం",
     "Each MP's vote value is 1 / ప్రతి MP = 1 (correct)",
     "Based on state population / జనాభా ఆధారంగా",
     "Based on MP seniority / Seniority",
     "b",
     "In VP election, EACH MP'S VOTE VALUE = 1. Unlike Presidential election where MP/MLA vote values differ (based on state population), VP election has equal weightage since only MPs participate (no MLAs). Quota = (Total valid votes / 2) + 1."),

    (7, 3,
     "In which House must VP removal resolution be introduced?\nతెలుగు: తొలగింపు ఏ సభలో?",
     "LS only / LS మాత్రమే",
     "Rajya Sabha only — Art.67(b) / RS మాత్రమే (correct)",
     "Either House / ఏ సభైనా",
     "Both simultaneously / రెండూ ఒకేసారి",
     "b",
     "Art.67(b): VP removal resolution must be initiated ONLY IN RAJYA SABHA (since VP chairs RS). After RS Effective Majority, LS agrees by Simple Majority. Compare: Presidential Impeachment (Art.61) can be initiated in EITHER House."),

    (7, 4,
     "Must VP election be held immediately when office falls vacant?\nతెలుగు: VP ఖాళీ అయితే తక్షణ ఎన్నిక?",
     "Yes, within 30 days / 30 రోజుల్లో",
     "Yes, within 6 months / 6 నెలల్లో",
     "No specific time limit in Constitution — unlike Presidential vacancy (6-month limit) / రాజ్యాంగంలో కాల పరిమితి లేదు (correct)",
     "Yes, within 90 days / 90 రోజుల్లో",
     "c",
     "NO SPECIFIC TIME LIMIT prescribed for filling VP vacancy in the Constitution. Constitutional lacuna! Compare: Presidential vacancy MUST be filled within 6 MONTHS (Art.62(1)). VP vacancy is filled 'as soon as possible' by convention."),

    (7, 3,
     "Correct statement about Zakir Husain?\nతెలుగు: జాకీర్ హుసేన్?",
     "First VP / మొదటి VP",
     "VP then President; died while serving as President / VP, తర్వాత President; పదవిలో మరణం (correct)",
     "Two terms VP / రెండు పదవీ కాలాలు",
     "First Muslim VP only / మొదటి ముస్లిం VP",
     "b",
     "Zakir Husain: 2nd VP (1962–67) → 3rd President (1967–69). DIED IN OFFICE on 3 May 1969 while serving as President — first President to die in office. (Fakhruddin Ali Ahmed in 1977 was second). Was first Muslim President of India."),

    (7, 4,
     "Is VP elected by direct election of RS members only?\nతెలుగు: VP RS సభ్యుల ప్రత్యక్ష ఎన్నికా?",
     "Yes, only RS / RS మాత్రమే",
     "No — VP elected by ALL MPs (both Houses, elected + nominated) — indirect election; no MLAs / కాదు, MP లందరూ (correct)",
     "Only LS+RS elected / LS+RS ఎన్నికైన",
     "Single vote / ఒక ఓటు",
     "b",
     "VP election is INDIRECT: by ALL MPs of both Houses (elected + nominated members), via STV with secret ballot. Common misconceptions: (1) NOT direct (citizens don't vote); (2) NOT RS-only (LS members also vote); (3) MLAs do NOT participate."),
]


# ─────────────────────────────────────────────────────────────
def _seed_polity_ch16_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    """Insert Chapter 16 study note row (idempotent)."""
    existing = db_exec_fn(conn,
        "SELECT id FROM study_notes WHERE topic='Indian_Polity' AND chapter_num=16"
    ).fetchone()
    if existing and not force:
        return

    sections_json = _json.dumps(POLITY_CH16_SECTIONS, ensure_ascii=False)
    ph = '%s' if use_postgres else '?'

    if existing and force:
        db_exec_fn(conn,
            f"UPDATE study_notes SET sections_json={ph}, chapter_title_en={ph}, chapter_title_te={ph} "
            f"WHERE topic='Indian_Polity' AND chapter_num=16",
            (sections_json,
             "Vice President of India",
             "భారత ఉపరాష్ట్రపతి")
        )
        return

    db_exec_fn(conn,
        f"""INSERT INTO study_notes
            (subject, topic, subtopic, chapter_num,
             chapter_title_te, chapter_title_en, pages_ref, sections_json)
            VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
        ('GK', 'Indian_Polity', 'Lakshmikanth', 16,
         'భారత ఉపరాష్ట్రపతి',
         'Vice President of India',
         'Ch.16',
         sections_json)
    )


def _seed_polity_ch16_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
    """Insert Chapter 16 MCQs (skip if already present)."""
    note_row = db_exec_fn(conn,
        "SELECT id FROM study_notes WHERE topic='Indian_Polity' AND chapter_num=16"
    ).fetchone()
    if not note_row:
        return
    note_id = row_to_dict_fn(note_row)['id']

    already = db_exec_fn(conn,
        "SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id=?", (note_id,)
    ).fetchone()
    if already and list(already)[0] > 0:
        return

    diff_map = {"easy": 1, "medium": 2, "hard": 3, "toughest": 4,
                1: 1, 2: 2, 3: 3, 4: 4}

    ph = '%s' if use_postgres else '?'
    for row in POLITY_CH16_MCQS:
        sec_idx, diff_raw, q, a, b, c, d, correct, explanation = row[:9]
        exam_type = row[9] if len(row) > 9 else 'General'
        diff_int = diff_map.get(diff_raw, 2)
        db_exec_fn(conn,
            f"""INSERT INTO chapter_mcqs
                (study_note_id, section_idx, difficulty, exam_type,
                 q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te)
                VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
            (note_id, sec_idx, diff_int, exam_type,
             q, a, b, c, d, str(correct).lower(), explanation)
        )
