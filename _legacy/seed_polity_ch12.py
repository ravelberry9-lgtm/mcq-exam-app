# seed_polity_ch12.py
# Chapter 12: Basic Structure of the Constitution (రాజ్యాంగ మూల నిర్మాణం)
# Standard : APPSC Group 2 | Source: Lakshmikanth Indian Polity
# Total MCQs: 45 | PYQs: 10 | Format: Bilingual (Telugu + English)
# Sections:
#   0 = పూర్వ-కేశవానంద కేసులు / Pre-Kesavananda Cases (7 MCQs)
#   1 = కేశవానంద భారతి కేసు 1973 / Kesavananda Bharati Case 1973 (8 MCQs)
#   2 = మూల నిర్మాణ అంశాలు / Elements of Basic Structure (7 MCQs)
#   3 = కేశవానంద తర్వాత ముఖ్య కేసులు / Post-Kesavananda Landmark Cases (8 MCQs)
#   4 = 42వ సవరణ మరియు మూల నిర్మాణం / 42nd Amendment & Basic Structure (5 MCQs)
#   5 = వ్యాప్తి మరియు అనువర్తనం / Scope and Application (5 MCQs)
#   6 = కఠిన ప్రశ్నలు / Tough MCQs (5 MCQs)

import json as _json

POLITY_CH12_SECTIONS = [
    {"title": "12.1 పూర్వ-కేశవానంద కేసులు", "sub": "Shankari Prasad 1951 · Sajjan Singh 1964 · Golaknath 1967 · 24th & 25th Amendments", "audio": ""},
    {"title": "12.2 కేశవానంద భారతి కేసు 1973", "sub": "13-Judge Bench · 7:6 Majority · Basic Structure Doctrine · A.N. Ray Appointment", "audio": ""},
    {"title": "12.3 మూల నిర్మాణ అంశాలు", "sub": "Elements · Supremacy · Republic · Federalism · Secularism · Judicial Independence · Parliamentary System", "audio": ""},
    {"title": "12.4 కేశవానంద తర్వాత ముఖ్య కేసులు", "sub": "Indira Gandhi 1975 · Minerva Mills 1980 · Waman Rao 1981 · IR Coelho 2007 · NJAC 2015", "audio": ""},
    {"title": "12.5 42వ సవరణ మరియు మూల నిర్మాణం", "sub": "42nd Amendment 1976 · Emergency · Art 368(4)(5) · Minerva Mills 1980 · Restoration", "audio": ""},
    {"title": "12.6 వ్యాప్తి మరియు అనువర్తనం", "sub": "Scope · Only Amendments · Ordinary Laws · German Grundnorm · Evolving List", "audio": ""},
    {"title": "12.7 కఠిన ప్రశ్నలు", "sub": "Tough MCQs · Art 13 vs BS · Omnibus Criticism · Parliament's Unlimited Power · Eternity Clause", "audio": ""},
]

POLITY_CH12_MCQS = [
    # ───── Section 0: Pre-Kesavananda Cases ─────
    (0, 1,
     "What did SC hold in Shankari Prasad v. UoI (1951)?\nతెలుగు: Shankari Prasad 1951?",
     "Amendments fall under 'law' in Art.13(2) — FRs cannot be amended",
     "Amendments do NOT fall under 'law' in Art.13(2) — Parliament can amend FRs / Art.13(2) వర్తించదు, Parliament FRs సవరించవచ్చు (correct)",
     "FRs unamendable", "Art.368 not applicable",
     "b",
     "Shankari Prasad v. Union of India (1951): SC unanimously held Constitutional Amendments DO NOT fall within 'law' in Art.13(2). Distinguished CONSTITUENT POWER (Art.368) from LEGISLATIVE POWER (ordinary Art.245). Parliament CAN AMEND any provision including FRs via Art.368. Upheld 1st Amendment 1951 adding Art.31A, 31B. First major amendment case."),

    (0, 1,
     "Sajjan Singh v. State of Rajasthan (1964) involved which amendment?\nతెలుగు: Sajjan Singh 1964?",
     "42nd Amendment", "24th Amendment",
     "17th Amendment / 17వ సవరణ (correct)",
     "1st Amendment",
     "c",
     "Sajjan Singh v. State of Rajasthan (1964): Involved 17th Constitutional Amendment 1964 (which had added land reform laws to 9th Schedule). 5-judge SC bench reaffirmed Shankari Prasad — Parliament can amend FRs via Art.368. Majority 5:2. JUSTICES HIDAYATULLAH AND MUDHOLKAR DISSENTED — Mudholkar mentioned 'BASIC FEATURES' for the first time — seeds of BS doctrine."),

    (0, 2,
     "What did 11 judges decide in Golaknath v. State of Punjab (1967)?\nతెలుగు: Golaknath?",
     "Parliament can amend FRs — upheld earlier cases",
     "Amending FRs prohibited — 'primacy'",
     "Parliament CANNOT amend FRs — 6:5 majority; Prospective Overruling applied / 6:5 majority, Prospective Overruling (correct)",
     "FRs+DPSPs together form Basic Structure",
     "c",
     "I.C. Golaknath v. State of Punjab (1967): 11-judge SC bench (6:5 majority) OVERRULED Shankari Prasad and Sajjan Singh — held Parliament has NO POWER TO AMEND FRs. CJ Subba Rao called FRs 'TRANSCENDENTAL.' Applied DOCTRINE OF PROSPECTIVE OVERRULING — earlier amendments remain valid; future amendments cannot abridge FRs. Triggered 24th Amendment 1971."),

    (0, 2,
     "What was the purpose of 24th Constitutional Amendment 1971?\nతెలుగు: 24వ సవరణ?",
     "Land reforms",
     "Overturn Golaknath and clarify Parliament can amend any provision including FRs + mandatory Presidential assent / Golaknath rev (correct)",
     "Executive control over judicial appointments",
     "Add 'Socialist' and 'Secular' to Preamble",
     "b",
     "24th Constitutional Amendment 1971 — direct response to Golaknath 1967: (1) Inserted Art.13(4) — Art.13 does NOT apply to amendments; (2) Amended Art.368 — explicitly stated Parliament can amend 'any provision of this Constitution'; (3) Inserted Art.368(3) — Parliament's amending power explicitly extends; (4) Made President's ASSENT MANDATORY for amendment bills (Art.368(2) proviso)."),

    (0, 2,
     "What did 25th Amendment 1971 introduce?\nతెలుగు: 25వ సవరణ?",
     "Art.31D — minority rights",
     "Art.31C — laws implementing DPSPs (Art.39b,c) cannot be challenged under Art.14 or 19 / Art.31C (correct)",
     "Art.31B — 9th Schedule protection",
     "Art.31A — property acquisition",
     "b",
     "25th Constitutional Amendment 1971 inserted Art.31C: Laws implementing DPSP Art.39(b) (material resources) AND Art.39(c) (prevention of wealth concentration) cannot be challenged under Art.14, Art.19. ALSO replaced 'compensation' with 'amount' in Art.31(2). Highly controversial — gave DPSP-implementing laws immunity from FR challenges. This amendment was central to the Kesavananda Bharati case."),

    (0, 3,
     "Correct sequence of SC judgments before Kesavananda?\nతెలుగు: సరైన క్రమం?",
     "Golaknath → Shankari Prasad → Sajjan Singh",
     "Shankari Prasad → Sajjan Singh → Golaknath / SP → SS → GN (correct)",
     "Sajjan Singh → Golaknath → SP",
     "SP → Golaknath → Sajjan Singh",
     "b",
     "Chronological sequence on FR amendment: (1) SHANKARI PRASAD 1951 — Parliament CAN amend FRs (1st Am 1951); (2) SAJJAN SINGH 1964 — UPHELD Shankari Prasad (17th Am 1964); (3) GOLAKNATH 1967 — Parliament CANNOT amend FRs (REVERSED). Then 24th Amendment 1971 → KESAVANANDA 1973 → BS doctrine. Standard exam sequence question.",
     "APPSC"),

    (0, 3,
     "Why is Sajjan Singh 1964 important besides upholding Shankari Prasad?\nతెలుగు: Sajjan Singh ప్రాముఖ్యత?",
     "First formal use of 'Basic Structure' term by Justice Sikri",
     "Justice Mudholkar in dissent introduced concept of 'basic features' that cannot be amended / Justice Mudholkar — 'basic features' (correct)",
     "Decided validity of 24th Amendment",
     "Explained operation of Arts.358-359",
     "b",
     "Sajjan Singh 1964 dissent: Justice MUDHOLKAR (and Hidayatullah J) questioned whether 'Constitution' could be substantially altered through ordinary amendment procedure. Mudholkar specifically mentioned that there might be 'BASIC FEATURES' which cannot be amended — first judicial mention of what would later become 'Basic Structure.' Influenced subsequent doctrine. Reference: 'Whatever the form of words used, this Article (Art.368) does not entitle Parliament to abrogate the very Constitution that gave it birth.'"),

    # ───── Section 1: Kesavananda Bharati 1973 ─────
    (1, 1,
     "How many judges in Kesavananda Bharati (1973) and what majority?\nతెలుగు: ఎంత మంది, ఏ majority?",
     "9 — 6:3", "11 — 8:3",
     "13 — 7:6 majority / 13 న్యాయమూర్తులు 7:6 (correct)",
     "7 — 4:3",
     "c",
     "KESAVANANDA BHARATI v. STATE OF KERALA (1973): LARGEST EVER constitutional bench — 13 JUDGES (Chief Justice S.M. Sikri + 12 judges). Razor-thin 7:6 MAJORITY. Heard for 68 days (October 1972 - March 1973). Judgment delivered 24 April 1973. CJ Sikri's last day in office. Spread across multiple opinions — about 700 pages of judgment.",
     "APPSC"),

    (1, 2,
     "Key ruling of Kesavananda Bharati case?\nతెలుగు: ప్రధాన నిర్ణయం?",
     "Parliament can amend any provision — upheld Golaknath",
     "Parliament can amend any provision INCLUDING FRs — but CANNOT destroy Basic Structure / FRs సవరించవచ్చు, BS ఉల్లంఘించరాదు (correct)",
     "Parliament cannot amend FRs", "Art.368 struck down",
     "b",
     "Kesavananda Bharati 1973 (7:6 majority): OVERRULED Golaknath 1967 — Parliament CAN amend any provision including FRs via Art.368. CRITICAL LIMITATION: Cannot DESTROY or ABROGATE the BASIC STRUCTURE of the Constitution. Found halfway between Golaknath (Parliament can't amend FRs) and 24th Am claim (Parliament can amend anything). BS doctrine = enduring legacy.",
     "APPSC"),

    (1, 2,
     "Who was CJ during Kesavananda and what happened after?\nతెలుగు: CJ ఎవరు? తర్వాత?",
     "CJ Gajendragadkar; judicial review abolished",
     "CJ S.M. Sikri; retired same day; Indira Gandhi superseded 3 senior judges, appointed A.N. Ray as CJ / Sikri retire, Ray supersession (correct)",
     "CJ A.N. Ray; Collegium introduced",
     "CJ Chandrachud; 44th Am passed",
     "b",
     "CJ S.M. SIKRI retired on 25 April 1973 — DAY AFTER Kesavananda judgment. Justices SHELAT, GROVER, HEGDE (all in majority that upheld BS doctrine) were SUPERSEDED for CJ-ship. Indira Gandhi appointed A.N. RAY (who had been in minority/dissent) directly as CJ — first time seniority broken for CJ position. Triggered 'JUDICIAL INDEPENDENCE' crisis. Three superseded judges resigned in protest."),

    (1, 2,
     "What did SC decide about Art.31C (25th Am) in Kesavananda?\nతెలుగు: Art.31C ఏం?",
     "Fully valid", "Completely struck down",
     "First part (DPSP implementation protected) VALID; second part (declaration ousts judicial review) STRUCK DOWN / మొదటి భాగం valid; రెండవ భాగం రద్దు (correct)",
     "Only economic laws",
     "c",
     "On Art.31C in Kesavananda: (1) Part PROTECTING laws implementing Art.39(b)/(c) DPSPs from Art.14/19 challenge = UPHELD as VALID. (2) Part saying 'no law containing a declaration that it is for giving effect to such policy shall be called in question in any court on the ground that it does not give effect to such policy' = STRUCK DOWN as VIOLATING BASIC STRUCTURE — court must retain power to determine whether law actually implements DPSPs."),

    (1, 2,
     "What did CJ A.N. Ray attempt in 1975?\nతెలుగు: 1975 Ray attempt?",
     "Extended Kesavananda",
     "Heard Minerva Mills",
     "Constituted 13-judge bench to OVERRULE Kesavananda — dissolved within a day / 13 judges bench Kesavananda overrule (correct)",
     "Introduced NJAC",
     "c",
     "10-11 NOVEMBER 1975: CJ A.N. Ray constituted a 13-JUDGE BENCH supposedly to RECONSIDER Kesavananda. Was an attempt to OVERRULE BS doctrine. Lawyer NANI PALKHIVALA (Kesavananda counsel) argued against. Within TWO DAYS bench dissolved without any reasoned order, after vigorous resistance by senior judges and bar. Proved DURABILITY of Kesavananda. Aborted attempt during 1975 Emergency.",
     "APPSC"),

    (1, 3,
     "Original subject matter of Kesavananda Bharati case?\nతెలుగు: అసలు విషయం?",
     "Religious freedom",
     "Acquisition of Edneer Mutt property under Kerala Land Reform Act / Edneer Mutt ఆస్తి (correct)",
     "Right to elementary education", "OBC reservation",
     "b",
     "KESAVANANDA BHARATI was the Sripadagalvaru (head/pontiff) of EDNEER MUTT in Kasaragod district, Kerala. KERALA LAND REFORMS (Amendment) ACT 1969 + 1971 affected the Mutt's properties. He approached SC under Art.32 in 1970 citing violations of Art.25 (religious freedom), Art.26 (religious affairs), Art.14, 19, 31 (property). Case grew into the most consequential constitutional case in Indian history. He died in 2020 — petition lives on as eternal precedent."),

    (1, 3,
     "Which key elements were FIRST identified as Basic Structure in Kesavananda?\nతెలుగు: BS మొదటి అంశాలు?",
     "Constitutional supremacy, Republic-Democratic form, Secularism, Separation of Powers, FRs / రాజ్యాంగ ఆధిపత్యం + ప్రజాస్వామ్యం + లౌకికత (correct)",
     "Federal sovereignty only",
     "Only Arts.14, 19, 21", "Only Rule of Law",
     "a",
     "In Kesavananda 1973, different judges identified different BS elements (non-exhaustive). Broadly: (1) Supremacy of Constitution; (2) Sovereign, Democratic, Republican character; (3) Secular character; (4) Federal character (some judges); (5) Separation of Powers between Legislature, Executive, Judiciary; (6) Fundamental Rights as a whole (or Arts.14, 19, 21 'golden triangle'); (7) Rule of Law; (8) Principle of equality."),

    # ───── Section 2: Elements of Basic Structure ─────
    (2, 1,
     "Which are part of Basic Structure?\nతెలుగు: ఏవి BS?",
     "Supremacy of Constitution, Secularism, Judicial Review, Democracy / రాజ్యాంగ ఆధిపత్యం, లౌకికత, JR, ప్రజాస్వామ్యం (correct)",
     "Panchayati Raj, Property Right, DPSPs, OBC reservations",
     "RTE, Environment, All FRs",
     "1st, 2nd, 10th Schedules",
     "a",
     "Confirmed BS elements (evolving list — non-exhaustive): (1) Supremacy of Constitution; (2) Sovereign-Democratic-Republican character; (3) Secularism; (4) Federal character; (5) Separation of Powers; (6) Judicial Review; (7) Independence of Judiciary; (8) Rule of Law; (9) Free and Fair Elections; (10) Harmony between FRs and DPSPs; (11) Parliamentary form of Government. Court adds case by case.",
     "APPSC"),

    (2, 2,
     "Which BS element firmly established in SR Bommai v. UoI (1994)?\nతెలుగు: SR Bommai BS?",
     "Judicial Review",
     "Secularism — Art.356 can dismiss anti-secular state governments / లౌకికత, Art.356 (correct)",
     "Federal character", "Rule of Law",
     "b",
     "S.R. BOMMAI v. UoI (1994): 9-judge SC bench firmly established 'SECULARISM' as part of Basic Structure. Held: (1) Secularism includes equal treatment of all religions; (2) ART.356 (President's Rule) PROCLAMATION IS JUDICIALLY REVIEWABLE; (3) States pursuing ANTI-SECULAR policies can be dismissed under Art.356. Came in context of Ayodhya dispute and 1992-93 communal riots. Reinforced FEDERAL character also."),

    (2, 2,
     "What did L. Chandra Kumar v. UoI (1997) add to BS?\nతెలుగు: Chandra Kumar?",
     "Enhanced Secularism",
     "Judicial review powers of HC and SC are Basic Structure — cannot be ousted by tribunals / SC, HC JR అధికారాలు BS (correct)",
     "Direct election of President",
     "Strengthened amendment power",
     "b",
     "L. CHANDRA KUMAR v. UoI (1997): 7-judge SC bench. Established that JUDICIAL REVIEW POWERS of Supreme Court (Art.32, 136) AND HIGH COURTS (Art.226, 227) are PART OF BASIC STRUCTURE — being essential remedial organs. ADMINISTRATIVE TRIBUNALS Act 1985 provisions ousting High Court jurisdiction were partly STRUCK DOWN. Tribunals can be initial adjudicators but final judicial review must rest with HC/SC."),

    (2, 2,
     "Parliamentary form of govt as BS established in which case?\nతెలుగు: Parliamentary form BS?",
     "IR Coelho 2007", "Kesavananda Bharati 1973",
     "Indira Nehru Gandhi v. Raj Narain 1975 / Indira Gandhi v. Raj Narain (correct)",
     "SR Bommai 1994",
     "c",
     "INDIRA NEHRU GANDHI v. RAJ NARAIN (1975): SC established that DEMOCRACY, FREE AND FAIR ELECTIONS, and PARLIAMENTARY FORM OF GOVERNMENT are PART OF BASIC STRUCTURE. STRUCK DOWN clause (4) of Art.329A (added by 39th Amendment 1975) which had retroactively validated Indira Gandhi's election after Allahabad HC had set it aside. Famous Justice H.R. Khanna applied BS test — first post-Kesavananda strikedown of an amendment."),

    (2, 3,
     "BS ground for striking down 99th Amendment in NJAC case (2015)?\nతెలుగు: NJAC ఏ BS?",
     "Federal character violation",
     "Secularism violation",
     "Independence of Judiciary violation / న్యాయ స్వాతంత్ర్యం ఉల్లంఘన (correct)",
     "FR violation",
     "c",
     "NJAC CASE (Supreme Court Advocates-on-Record Association v. UoI, 2015): 5-judge SC bench (4:1 majority) STRUCK DOWN 99th Constitutional Amendment 2014 + NJAC Act 2014. Held: NATIONAL JUDICIAL APPOINTMENTS COMMISSION (NJAC) — which allowed executive members (Law Minister + 2 eminent persons) to participate in higher judiciary appointments — VIOLATED 'INDEPENDENCE OF JUDICIARY' = Basic Structure. Restored COLLEGIUM system. Justice Chelameswar lone dissenter.",
     "APPSC"),

    (2, 3,
     "What did Indra Sawhney 1992 add to BS doctrine?\nతెలుగు: Indra Sawhney 1992?",
     "Judicial independence",
     "Reservations cannot exceed 50% — Equality is BS element / 50% cap, Equality BS (correct)",
     "Secularism", "Right to vote",
     "b",
     "INDRA SAWHNEY v. UoI (1992 — Mandal case): 9-judge SC bench. (1) OBC RESERVATION (27%) upheld; (2) Total reservations should NOT EXCEED 50% — to maintain EQUALITY (BS element); (3) Mandated CREAMY LAYER exclusion for OBC; (4) No reservation in promotions (later modified by 77th Am for SC/ST). Connected RESERVATION JURISPRUDENCE to BS — EQUALITY PRINCIPLE itself is BS, so excessive reservations violating equality would breach BS."),

    (2, 3,
     "'Separation of Powers' as BS was established in which case?\nతెలుగు: Separation of Powers BS?",
     "Kesavananda Bharati 1973", "Minerva Mills 1980",
     "Indira Nehru Gandhi v. Raj Narain 1975 / Indira Gandhi v. Raj Narain (correct)",
     "Waman Rao 1981",
     "c",
     "INDIRA NEHRU GANDHI v. RAJ NARAIN (1975): Established 'SEPARATION OF POWERS' as part of Basic Structure. 39th Amendment 1975 attempted to OUST judicial power to decide election disputes of PM/President/VP/Speaker. SC held this violates Separation of Powers — Legislature cannot exercise JUDICIAL POWER over individual disputes. Also reinforced: democracy, free/fair elections, rule of law are BS.",
     "APPSC"),

    # ───── Section 3: Post-Kesavananda Cases ─────
    (3, 1,
     "What did SC decide in Minerva Mills v. UoI (1980)?\nతెలుగు: Minerva Mills?",
     "Struck down Art.368(4) and (5) of 42nd Amendment / 42వ Art.368(4)(5) రద్దు (correct)",
     "42nd Amendment fully valid",
     "DPSPs got priority over FRs",
     "Kesavananda overruled",
     "a",
     "MINERVA MILLS v. UoI (1980): 5-judge SC bench (CJ Y.V. Chandrachud). STRUCK DOWN: (1) Art.368(4) — 'no judicial review of constitutional amendments' = VIOLATES BS; (2) Art.368(5) — 'no limitation on Parliament's amending power' = VIOLATES BS; (3) Extension of Art.31C to ALL DPSPs by 42nd Am — restored to only Art.39(b)/(c). Reaffirmed Kesavananda. Held HARMONY between FR and DPSP itself is BS — neither can dominate.",
     "APPSC"),

    (3, 1,
     "What did Waman Rao v. UoI (1981) rule about 9th Schedule?\nతెలుగు: Waman Rao 9వ Schedule?",
     "Laws added to 9th Schedule AFTER Kesavananda are subject to JR / 1973 తర్వాత చేర్చిన చట్టాలు JR (correct)",
     "9th Schedule laws never subject to JR",
     "Entire 9th Schedule struck down",
     "9th Schedule only applies to central laws",
     "a",
     "WAMAN RAO v. UoI (1981): SC drew a 'WAMAN RAO LINE' on 9th Schedule. Laws added to 9th Schedule BEFORE 24 APRIL 1973 (Kesavananda judgment date) are FULLY PROTECTED from FR-based challenges. Laws added AFTER that date are SUBJECT TO BASIC STRUCTURE test. Important date: 24 April 1973. Reaffirmed and elaborated in I.R. Coelho (2007)."),

    (3, 2,
     "What did 9-judge bench rule in IR Coelho v. State of TN (2007)?\nతెలుగు: IR Coelho 2007?",
     "9th Schedule completely struck down",
     "Laws added to 9th Schedule after Kesavananda subject to review if violating Arts.14,19,20,21 or BS / 1973 తర్వాత చట్టాలు Arts.14,19,20,21 + BS test (correct)",
     "9th Schedule only for land reforms",
     "9th Schedule never reviewable",
     "b",
     "I.R. COELHO v. STATE OF TN (2007): 9-judge SC Constitution Bench. Two-stage test for post-1973 9th Schedule laws: (1) Whether they VIOLATE Articles 14, 19, 20, 21 (FR test); (2) If yes, whether the violation also breaches BS. Either way, judicial review available. 9th Schedule protection is NOT absolute. Major curb on misuse of 9th Schedule for FR-violative laws. Examples: Tamil Nadu reservation 69% subject to review."),

    (3, 2,
     "Which Amendment did SC strike down in Indira Nehru Gandhi v. Raj Narain (1975)?\nతెలుగు: Indira Gandhi ఏ సవరణ?",
     "42nd Amendment 1976",
     "44th Amendment 1978",
     "39th Amendment 1975 / 39వ సవరణ (correct)",
     "25th Amendment 1971",
     "c",
     "39th Amendment 1975 — passed during Emergency to: (1) Insert Art.329A — placing PM/President/VP/Speaker election disputes BEYOND JUDICIAL REVIEW; (2) Retroactively validated Indira Gandhi's election after Allahabad HC's Raj Narain judgment had set it aside. SC STRUCK DOWN Art.329A(4) and (5) as violating BS (democracy, free fair elections, rule of law, separation of powers). Justice Khanna's main judgment.",
     "APPSC"),

    (3, 2,
     "How did SR Bommai apply BS to Art.356?\nతెలుగు: SR Bommai Art.356?",
     "Art.356 is part of BS",
     "Dismissal under Art.356 is judicially reviewable; anti-secular state governments can be dismissed / JR + anti-secular dismissal (correct)",
     "Art.356 completely struck down",
     "Use of Art.356 never violates BS",
     "b",
     "S.R. BOMMAI v. UoI (1994): 9-judge SC bench. (1) Art.356 PROCLAMATION IS JUDICIALLY REVIEWABLE — court can examine MATERIAL on which it was based and MALA FIDES; (2) ASSEMBLIES SHOULD NOT BE DISSOLVED until BOTH HOUSES of Parliament APPROVE PR; (3) ANTI-SECULAR state governments can be dismissed under Art.356 (Secularism is BS); (4) SC can revive dismissed governments. Crucial federal safeguard."),

    (3, 3,
     "Key difference between First Judges Case (1981) and Second Judges Case (1993)?\nతెలుగు: First vs Second Judges?",
     "Both endorsed executive primacy",
     "First Judges: executive primacy. Second Judges: CJI Collegium recommendation binding / First = executive, Second = collegium (correct)",
     "Both endorsed Collegium",
     "Both endorsed NJAC",
     "b",
     "FIRST JUDGES CASE (S.P. Gupta v. UoI 1981, 7 judges): EXECUTIVE PRIMACY in higher judicial appointments — CJI's recommendation NOT BINDING on President. SECOND JUDGES CASE (1993, 9 judges): OVERRULED First Judges — CJI-led COLLEGIUM of senior judges' recommendation BINDING on executive. THIRD JUDGES CASE (1998 advisory opinion): Clarified Collegium structure (CJI + 4 senior judges for SC; CJI + 4 senior judges for HC). NJAC 2015 attempted reversal — struck down."),

    (3, 3,
     "Correct sequence of major post-Kesavananda BS cases?\nతెలుగు: BS క్రమం?",
     "Minerva Mills → Indira Gandhi → Waman Rao → SR Bommai → NJAC",
     "Indira Gandhi (1975) → Minerva Mills (1980) → Waman Rao (1981) → SR Bommai (1994) → IR Coelho (2007) → NJAC (2015) (correct)",
     "Waman Rao → Indira Gandhi → SR Bommai → Minerva Mills → NJAC",
     "SR Bommai → Minerva Mills → NJAC → Waman Rao → Indira Gandhi",
     "b",
     "CHRONOLOGICAL: (1) Kesavananda Bharati 1973 [BS doctrine]; (2) INDIRA NEHRU GANDHI v. Raj Narain 1975 [Art.329A struck down — democracy, free fair elections as BS]; (3) MINERVA MILLS 1980 [Art.368(4)/(5) struck down]; (4) WAMAN RAO 1981 [9th Schedule line]; (5) Indra Sawhney 1992 [50% cap]; (6) S.R. BOMMAI 1994 [Secularism BS]; (7) Second Judges 1993, Third Judges 1998 [Collegium]; (8) L. Chandra Kumar 1997 [Tribunals JR]; (9) IR COELHO 2007 [9th Schedule reviewable]; (10) NJAC 2015 [Collegium restored].",
     "APPSC"),

    # ───── Section 4: 42nd Amendment & Basic Structure ─────
    (4, 1,
     "Which two provisions did 42nd Amendment 1976 add to Art.368?\nతెలుగు: 42వ Art.368 ఏవి?",
     "Art.368(1) and (2)",
     "Art.368(3) and (4)",
     "Art.368(4) and Art.368(5) / 368(4), (5) (correct)",
     "Art.368(6) and (7)",
     "c",
     "42nd Constitutional Amendment 1976 added two clauses to Art.368: (1) Art.368(4): 'No amendment of this Constitution shall be CALLED IN QUESTION in ANY COURT on ANY GROUND.' (2) Art.368(5): 'There shall be NO LIMITATION WHATEVER on the constituent power of Parliament to amend by way of addition, variation or repeal the provisions of this Constitution under this article.' BOTH struck down by Minerva Mills 1980 as violating BS."),

    (4, 2,
     "How did 42nd Amendment 1976 expand Art.31C?\nతెలుగు: 42వ Art.31C విస్తరణ?",
     "Removed Art.31C entirely",
     "Extended Art.31C protection from Art.39(b),(c) to ALL DPSPs / అన్ని DPSPs కి (correct)",
     "Applied Art.31C to all FRs",
     "Limited Art.31C to state laws",
     "b",
     "Pre-42nd: Art.31C (25th Am 1971) protected only laws implementing Art.39(b) and (c) from Art.14/19 challenge. 42nd Am 1976 EXPANDED: 'principles specified in clauses (b) and (c) of article 39' → 'ALL OR ANY of the principles laid down in PART IV.' Now ANY law implementing ANY DPSP got immunity. EXCESSIVE shielding! STRUCK DOWN in Minerva Mills 1980 — restored Art.31C to original Art.39(b)/(c) only."),

    (4, 2,
     "What did SC say about FR-DPSP relationship in Minerva Mills 1980?\nతెలుగు: Minerva Mills FR-DPSP?",
     "DPSPs always prevail",
     "FRs always prevail",
     "Balance/harmony between FRs and DPSPs is itself Basic Structure / Harmony BS (correct)",
     "FRs and DPSPs identical",
     "c",
     "Minerva Mills 1980: FRs and DPSPs are COMPLEMENTARY, not in conflict. 'GOLDEN TRIANGLE' = Art.14 + 19 + 21. HARMONIOUS CONSTRUCTION required between FR (Part III) and DPSP (Part IV). 42nd Amendment's subordination of FRs to ALL DPSPs disturbed this HARMONY — itself a BS element. CJ Chandrachud famously called FR-DPSP balance 'the conscience of the Constitution.'"),

    (4, 2,
     "Key changes brought by 44th Amendment 1978?\nతెలుగు: 44వ సవరణ?",
     "Removed Socialist/Secular from Preamble",
     "Struck down Art.368(4)/(5)",
     "Property right removed from FRs → Art.300A; Emergency procedure tightened; Arts.20, 21 unsuspendable in Emergency / Property + Emergency + Art.20/21 (correct)",
     "Fully reversed 42nd Amendment",
     "c",
     "44th Constitutional Amendment 1978 (Janata Party post-Emergency): (1) REMOVED Right to Property (Art.19(1)(f) + Art.31) from FRs; added Art.300A as constitutional/legal right; (2) Tightened EMERGENCY: 'armed rebellion' replaced 'internal disturbance' (Art.352); written Cabinet advice for NE proclamation; Special Majority for Parliament approval of NE; (3) Articles 20, 21 CANNOT be SUSPENDED even during NE; (4) Various pro-individual-liberty safeguards.",
     "APPSC"),

    (4, 3,
     "Why is 42nd Amendment called 'Mini Constitution'?\nతెలుగు: 'Mini Constitution' ఎందుకు?",
     "Amended only Preamble",
     "Made 59 sweeping changes maximizing parliamentary supremacy / 59 సవరణలు పార్లమెంట్ ఆధిపత్యం (correct)",
     "Introduced 42 FRs",
     "Introduced 42 DPSPs",
     "b",
     "42nd Constitutional Amendment 1976 (Indira Gandhi during Emergency) — called 'MINI CONSTITUTION' because of 59 SWEEPING CHANGES: (1) Added FUNDAMENTAL DUTIES (Art.51A, Part IVA); (2) 'SOCIALIST, SECULAR, INTEGRITY' to Preamble; (3) Declared ABSOLUTE amendment power (Art.368(4)/(5)); (4) DPSPs over FRs (Art.31C extension); (5) Extended LS/State Assembly terms 5→6 years; (6) Added Tribunals (Art.323A/B); (7) Limited judicial review. Most touched almost every Part. Many struck down by Minerva Mills 1980."),

    # ───── Section 5: BS Doctrine Theory ─────
    (5, 1,
     "To what type of actions does BS doctrine apply?\nతెలుగు: BS ఏ చర్యలకు?",
     "Only ordinary legislation",
     "Only constitutional amendments / Constitutional amendments మాత్రమే (correct)",
     "Only Presidential orders",
     "All executive actions",
     "b",
     "BASIC STRUCTURE doctrine applies ONLY to CONSTITUTIONAL AMENDMENTS (Art.368). NOT to ordinary legislation. For ordinary laws: Art.13 applies — laws void if violate FRs. For constitutional amendments: BS doctrine — amendments void if destroy BS. Two parallel tests for two different types of state action. Cannot conflate them.",
     "APPSC"),

    (5, 2,
     "BS doctrine inspired by which country's concept?\nతెలుగు: BS ఎక్కడ నుండి?",
     "USA",
     "UK",
     "Germany (Grundnorm/Eternity Clause) / జర్మనీ (correct)",
     "Australia",
     "c",
     "Justice Mudholkar in Sajjan Singh 1964 dissent referenced GERMAN BASIC LAW (Grundgesetz 1949), Article 79(3) — the 'ETERNITY CLAUSE' which makes certain core provisions (human dignity, federal character, democratic order) UNAMENDABLE. Kesavananda 1973 drew on this concept (though not literally). Other inspirations: Hans Kelsen's GRUNDNORM theory; US constitutional precedents; UK doctrine of parliamentary sovereignty (which India rejected)."),

    (5, 2,
     "Is BS doctrine explicitly written in Constitution?\nతెలుగు: BS రాజ్యాంగంలో రాశారా?",
     "Yes — in Art.368(3)",
     "Yes — in Art.13(1A)",
     "No — judicial doctrine through interpretation / కాదు, judicial doctrine (correct)",
     "Yes — in 9th Schedule",
     "c",
     "BS Doctrine is NOWHERE EXPLICITLY WRITTEN in the Indian Constitution. It is a PURE JUDICIAL CONSTRUCTION — developed through SC's interpretation, starting from Kesavananda Bharati 1973. The list of BS elements is EVOLVING and OPEN-ENDED — court adds new elements case by case. Critics argue this gives SC unlimited power; supporters say it's a necessary safeguard. India has no German-style 'Eternity Clause' but court has effectively created one."),

    (5, 2,
     "Nature of Basic Structure elements list?\nతెలుగు: BS జాబితా స్వభావం?",
     "Definitive — finalized in 1973",
     "Decided by Parliament",
     "Evolving — SC identifies new elements case by case / Evolving list (correct)",
     "Precisely written in Constitution",
     "c",
     "BS list is EVOLVING (non-exhaustive). Kesavananda 1973 began with 7-8 elements. Indira Gandhi 1975 added: Democracy, Free & Fair Elections, Parliamentary form, Separation of Powers. Minerva Mills 1980: Harmony FR-DPSP, limited amending power. S.R. Bommai 1994: Secularism. L. Chandra Kumar 1997: HC/SC judicial review. NJAC 2015: Judicial independence. Recently: Federal cooperation, judicial appointment. Open-ended adds flexibility but creates uncertainty."),

    (5, 3,
     "Is Universal Adult Suffrage part of Basic Structure?\nతెలుగు: సార్వజనీన ఓటు హక్కు?",
     "No — Parliament law can change",
     "Specifically named in Kesavananda 1973",
     "Yes — part of 'Free and Fair Elections' BS element (Indira Gandhi 1975) / Free Fair Elections BS (correct)",
     "No — elections are ordinary law",
     "c",
     "INDIRA GANDHI v. Raj Narain 1975 established DEMOCRACY, FREE & FAIR ELECTIONS, REPRESENTATIVE GOVERNMENT as BS. UNIVERSAL ADULT SUFFRAGE (Art.326 — voting age now 18 since 61st Am) is the FOUNDATION of democracy — so impliedly part of BS through 'Democracy' and 'Free and Fair Elections.' Voting age can be technically changed by amendment, but eliminating universal suffrage would violate BS."),

    # ───── Section 6: BS Misc and Application ─────
    (6, 3,
     "To which does BS doctrine NOT apply?\nతెలుగు: BS ఏది వర్తించదు?",
     "Constitutional amendments",
     "Amendments like 38th Amendment 1975",
     "Ordinary legislation and executive actions / సాధారణ చట్టాలు, కార్యనిర్వాహక చర్యలు (correct)",
     "9th Schedule laws (post-Kesavananda)",
     "c",
     "BS doctrine APPLIES TO: (1) Constitutional Amendments (Art.368); (2) Laws added to 9th Schedule AFTER 24 April 1973 (per IR Coelho 2007). BS doctrine DOES NOT apply to: (a) ORDINARY LEGISLATION — judged under Art.13 (FR test); (b) EXECUTIVE ACTIONS — judged under FRs/Art.226 grounds. Two parallel adjudicatory regimes. Mixing them confuses the test.",
     "APPSC"),

    (6, 3,
     "Main criticism of BS doctrine and its defense?\nతెలుగు: BS విమర్శ, రక్షణ?",
     "Criticism: incomprehensible; Defense: understandable",
     "Criticism: SC becomes 'Super Parliament' with unlimited power; Defense: necessary check against 42nd Amendment-type abuse / SC Super Parliament vs 42వ సవరణ నుండి రక్షణ (correct)",
     "Criticism: copied from Germany; Defense: indigenous",
     "Criticism: doesn't evolve; Defense: stability needed",
     "b",
     "CRITICISMS: (1) SC becomes 'SUPER PARLIAMENT' — strikes down democratically-passed amendments; (2) BS is VAGUE — no precise definition; (3) Open-ended list creates UNCERTAINTY; (4) Counter-majoritarian dilemma. DEFENSES: (1) Protected Constitution from 42nd Amendment power-grab and Emergency abuse; (2) Protects FRs, democracy, secularism — direct citizen benefits; (3) Constitutional supremacy needs ultimate guardian; (4) Permits gradual evolution. Famously balanced by Justice Khanna's view: 'Constitution is not just a document for transient majorities.'"),

    (6, 3,
     "Difference between Art.13(2) and Basic Structure doctrine?\nతెలుగు: Art.13(2) vs BS?",
     "Same test",
     "Art.13(2): ordinary laws void for FR violation; BS: amendments void for BS violation — TWO PARALLEL TESTS / రెండు వేర్వేరు పరీక్షలు (correct)",
     "Art.13(2) subordinate to BS",
     "BS overruled Art.13(2)",
     "b",
     "TWO PARALLEL TESTS: (1) ARTICLE 13(2): Any 'LAW' (ordinary statute, ordinance, by-law, regulation, notification) inconsistent with FRs → VOID. Test applied by courts under Art.32/226. (2) BS DOCTRINE: Any CONSTITUTIONAL AMENDMENT (under Art.368) destroying BS → VOID. Different scope: 'law' in Art.13(2) DOES NOT INCLUDE constitutional amendments (per Shankari Prasad, reaffirmed in Kesavananda). Two parallel adjudicatory regimes that work together to protect Constitution.",
     "APPSC"),

    (6, 3,
     "Closest constitutional concept to BS doctrine in India?\nతెలుగు: BS కి దగ్గర concept?",
     "Art.368(2) — Special Majority",
     "Art.368(3) — State ratification",
     "No exact equivalent — entirely judicial construction / రాజ్యాంగంలో సమాన concept లేదు (correct)",
     "Art.13(1) — pre-constitution laws void",
     "c",
     "India has NO 'ETERNITY CLAUSE' equivalent to Germany's Art.79(3). Constitutional Articles closest in spirit: Art.368(2) — supermajority for federal provisions; but doesn't define unamendable elements. BS doctrine is ENTIRELY a JUDICIAL CONSTRUCTION starting from Kesavananda 1973. SC has effectively read in an 'implied transcendence' protecting Constitution's core from being amended into oblivion."),

    (6, 3,
     "Historical significance of Kesavananda Bharati 1973?\nతెలుగు: Kesavananda చారిత్రక ప్రాముఖ్యత?",
     "International protection",
     "Protection from state govts",
     "Protects Constitution from amendments that would destroy it — prevents constitutional dictatorship / రాజ్యాంగ నాశనం నుండి రక్షణ (correct)",
     "Judicial corruption protection",
     "c",
     "50+ years after Kesavananda 1973, its enduring legacy is PROTECTION OF CONSTITUTIONAL SUPREMACY. During 1975-77 Emergency, 42nd Amendment attempted constitutional dictatorship by maximising Parliament's power. Without Kesavananda's BS doctrine, those changes might have been permanent — democracy itself could have been abolished by simple super-majority. Minerva Mills 1980 used BS to RESTORE balance. Hence Kesavananda is the SAFEGUARD against legislative tyranny — the 'eternal guardian' of constitutional democracy in India.",
     "APPSC"),
]


def _seed_polity_ch12_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    import json as _j
    ph = '%s' if use_postgres else '?'
    _sections = POLITY_CH12_SECTIONS
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
        (12, 'Indian_Polity'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True,
                'message': 'Polity Ch12 notes already seeded.'}
    if row and force:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (12, 'Indian_Polity'))
    if use_postgres:
        conn.commit()

    db_exec_fn(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'Indian_Polity', '', 12,
         'రాజ్యాంగ మూల నిర్మాణం',
         'Basic Structure of the Constitution',
         'Ch.12',
         _j.dumps(_sections, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'Polity Ch12 notes seeded!'}


def _seed_polity_ch12_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
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
        (12, 'Indian_Polity'))
    row = cur.fetchone()
    if not row:
        _seed_polity_ch12_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)
        cur = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (12, 'Indian_Polity'))
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
    for mcq in POLITY_CH12_MCQS:
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

    total = len(POLITY_CH12_MCQS)
    return {
        'success': True,
        'message': f'Polity Ch12 MCQs seeded! Total: {total}',
        'inserted': total,
        'easy': easy, 'medium': medium, 'hard': hard,
        'toughest': toughest, 'pyq': pyq
    }
