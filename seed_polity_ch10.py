# seed_polity_ch10.py
# Chapter 10: Fundamental Duties (ప్రాథమిక విధులు — Prathamika Vidhulu)
# Total MCQs: 48 | PYQs: 7 | Format: Bilingual (Telugu + English)
# Sections:
#   0 = పరిచయం / Introduction (7 MCQs)
#   1 = 11 విధుల జాబితా / List of 11 Duties (11 MCQs)
#   2 = స్వభావం & లక్షణాలు / Nature & Features (6 MCQs)
#   3 = స్వర్ణ సింగ్ కమిటీ / Swaran Singh Committee (4 MCQs)
#   4 = 86వ సవరణ - 11వ విధి / 86th Amendment - 11th Duty (4 MCQs)
#   5 = పోలిక / FR vs FD vs DPSP Comparison (5 MCQs)
#   6 = ముఖ్య కేసులు & PYQs / Cases & PYQs (5 MCQs)
#   7 = కఠిన ప్రశ్నలు / Tough MCQs (4 MCQs)

import json as _json

POLITY_CH10_MCQS = [
    # ───── Section 0: Introduction ─────
    (0, "easy",
     "Fundamental Duties are contained in which Part of the Constitution?\nతెలుగు: ప్రాథమిక విధులు ఏ Part?",
     "Part III", "Part IV", "Part IVA (correct)", "Part V",
     "C",
     "Fundamental Duties are in PART IVA (Article 51A) — added by 42nd Amendment 1976. Part IVA was a NEW PART specifically created to house FDs. Came after Part IV (DPSPs). Compare: FRs = Part III, DPSPs = Part IV, FDs = Part IVA, Local Govts = Part IX/IXA."),

    (0, "easy",
     "In which Article are Fundamental Duties enumerated?\nతెలుగు: FDs ఏ Article?",
     "Article 49", "Article 50", "Article 51",
     "Article 51A (correct)",
     "D",
     "Article 51A — single article containing all FDs as 11 clauses (a-k). Art.51 = DPSP on international peace (NOT to be confused with Art.51A). Art.51A is the ONLY article in Part IVA. All 11 duties listed in single article.",
     "APPSC"),

    (0, "easy",
     "Fundamental Duties were added by which Constitutional Amendment?\nతెలుగు: ఏ సవరణ?",
     "40th Amendment 1976",
     "42nd Amendment 1976 (correct)",
     "44th Amendment 1978",
     "86th Amendment 2002",
     "B",
     "42nd Constitutional Amendment Act 1976 added FDs based on Swaran Singh Committee's recommendations. Initially 10 duties (a-j). 11th duty (k) added by 86th Amendment 2002. The 42nd Amendment was passed during Emergency (1975-77) — also added many other provisions, some later reversed by 44th Am 1978.",
     "APPSC"),

    (0, "medium",
     "Fundamental Duties were borrowed from which country's Constitution?\nతెలుగు: ఎక్కడ నుండి?",
     "USA", "Ireland",
     "USSR (Soviet Union) / USSR (correct)",
     "Japan",
     "C",
     "FDs borrowed from USSR (Soviet) Constitution 1977 — which had detailed catalogue of citizens' duties towards the State. USSR Constitution emphasised citizens' obligations alongside rights. Compare: FRs from US Bill of Rights; DPSPs from Ireland; Parliamentary system from UK; Federal scheme from Canada; Emergency from Weimar.",
     "APPSC"),

    (0, "medium",
     "Which committee recommended Fundamental Duties?\nతెలుగు: ఏ committee?",
     "Balwantrai Mehta Committee",
     "Swaran Singh Committee (correct)",
     "Ashok Mehta Committee", "Verma Committee",
     "B",
     "SWARAN SINGH COMMITTEE 1976 recommended FDs. Set up by Indira Gandhi government during Emergency. Sardar Swaran Singh was senior Cabinet minister. Recommended 8 duties; Parliament added 2 more = 10. Also recommended penalty for breach (not adopted). Verma Committee 2002 was on operationalisation of FDs.",
     "APPSC"),

    (0, "medium",
     "Before 42nd Amendment 1976, how many FDs were in the Constitution?\nతెలుగు: 42వ ముందు ఎన్ని?",
     "5", "8", "10",
     "0 — None at all / అసలు లేవు (correct)",
     "D",
     "Before 42nd Amendment 1976, there were NO Fundamental Duties in the Constitution. India unique — first major constitution with FDs after USSR. Constituent Assembly debated and DROPPED idea of explicit duties — too vague. 1975 Emergency context revived idea. Now FDs are an integral part."),

    (0, "medium",
     "Why are FDs placed AFTER DPSPs in the Constitution?\nతెలుగు: DPSPs తర్వాత ఎందుకు?",
     "Supplementary to DPSPs",
     "Less important than DPSPs",
     "Citizens' duties follow State's duties (DPSPs) — balanced scheme / రాజ్యం + పౌరుల విధులు (correct)",
     "Non-justiciable like DPSPs",
     "C",
     "DPSPs are DIRECTIVES TO STATE (Part IV); FDs are DUTIES OF CITIZENS (Part IVA). Together they form a balanced reciprocal scheme — State has duties towards citizens (DPSPs); citizens have duties towards State/society (FDs). Reflects Ambedkar's vision of balancing rights with corresponding obligations."),

    # ───── Section 1: List of 11 Duties ─────
    (1, "easy",
     "Which clause requires abiding by Constitution, respecting Flag/Anthem?\nతెలుగు: రాజ్యాంగం + పతాకం + గీతం?",
     "Art.51A(a) (correct)", "Art.51A(b)", "Art.51A(c)", "Art.51A(d)",
     "A",
     "Art.51A(a): To ABIDE BY THE CONSTITUTION and respect its IDEALS AND INSTITUTIONS, the NATIONAL FLAG and the NATIONAL ANTHEM. Foundational duty — basis of citizen-State relationship. Bijoe Emmanuel (1986) addressed conflict with Art.25 — Jehovah's Witnesses' refusal to sing anthem protected as religious freedom."),

    (1, "easy",
     "Cherish noble ideals of freedom struggle — which clause?\nతెలుగు: స్వాతంత్ర్య ఆదర్శాలు?",
     "Art.51A(a)",
     "Art.51A(b) (correct)",
     "Art.51A(c)", "Art.51A(d)",
     "B",
     "Art.51A(b): To CHERISH AND FOLLOW the NOBLE IDEALS which inspired our NATIONAL STRUGGLE FOR FREEDOM. Includes Gandhian ideals, freedom fighters' ideals — non-violence, secularism, social justice, dignity, sacrifice. Connects nation's heritage to citizens' values."),

    (1, "medium",
     "Uphold sovereignty, unity, integrity of India — which clause?\nతెలుగు: సార్వభౌమత్వం, ఐక్యత?",
     "Art.51A(b)",
     "Art.51A(c) (correct)",
     "Art.51A(d)", "Art.51A(e)",
     "C",
     "Art.51A(c): To UPHOLD AND PROTECT the SOVEREIGNTY, UNITY AND INTEGRITY of India. Anti-secessionist, anti-disintegration duty. Foundation for laws like UAPA, Sedition law (Sec 124A IPC). Prevents activities promoting separatism."),

    (1, "medium",
     "Defend the country and render national service — which clause?\nతెలుగు: దేశ రక్షణ?",
     "Art.51A(c)",
     "Art.51A(d) (correct)",
     "Art.51A(e)", "Art.51A(f)",
     "D",
     "Art.51A(d): To DEFEND THE COUNTRY and RENDER NATIONAL SERVICE when called upon to do so. Reflects civic duty of military/national service. India hasn't operationalised compulsory military service (allowed under Art.23(2)). Voluntary service through NSS, NCC, Territorial Army."),

    (1, "medium",
     "Promote harmony, brotherhood, renounce practices derogatory to women — clause?\nతెలుగు: సహోదర భావన + మహిళల గౌరవం?",
     "Art.51A(d)",
     "Art.51A(e) (correct)",
     "Art.51A(f)", "Art.51A(g)",
     "B",
     "Art.51A(e): To PROMOTE HARMONY and the SPIRIT OF COMMON BROTHERHOOD amongst all the people of India transcending religious, linguistic and regional or sectional diversities; to RENOUNCE PRACTICES DEROGATORY TO THE DIGNITY OF WOMEN. Implementation: anti-dowry laws, Triple Talaq Act 2019 etc."),

    (1, "medium",
     "Value composite cultural heritage — which clause?\nతెలుగు: సమ్మిళిత సంస్కృతి?",
     "Art.51A(e)",
     "Art.51A(f) (correct)",
     "Art.51A(g)", "Art.51A(h)",
     "F",
     "Art.51A(f): To VALUE AND PRESERVE the RICH HERITAGE of our COMPOSITE CULTURE. Includes art, literature, languages, monuments, traditions. India's diversity is a strength to be preserved. Implementation: ASI work, Sangeet Natak Akademi, Sahitya Akademi, language schemes."),

    (1, "medium",
     "Protect environment, forests, lakes, rivers, wildlife — which clause?\nతెలుగు: పర్యావరణ పరిరక్షణ?",
     "Art.51A(f)",
     "Art.51A(g) (correct)",
     "Art.51A(h)", "Art.51A(i)",
     "B",
     "Art.51A(g): To PROTECT AND IMPROVE the NATURAL ENVIRONMENT including FORESTS, LAKES, RIVERS AND WILDLIFE, and to have COMPASSION FOR LIVING CREATURES. Companion to Art.48A DPSP (environmental protection). M.C. Mehta v. UoI cases used Art.51A(g) + Art.21 + Art.48A to develop environmental jurisprudence. Implementation: EPA 1986, Wildlife Act 1972, Forest Acts."),

    (1, "medium",
     "Develop scientific temper, humanism, spirit of inquiry — which clause?\nతెలుగు: శాస్త్రీయ దృక్పథం?",
     "Art.51A(g)",
     "Art.51A(h) (correct)",
     "Art.51A(i)", "Art.51A(j)",
     "B",
     "Art.51A(h): To DEVELOP the SCIENTIFIC TEMPER, HUMANISM and the SPIRIT OF INQUIRY AND REFORM. Counter to superstitions, blind faith, rigid traditions. Borrowed from Soviet emphasis on scientific worldview. Implemented through education curricula, research institutions, science promotion bodies."),

    (1, "easy",
     "Safeguard public property and abjure violence — which clause?\nతెలుగు: సార్వజనిక ఆస్తి?",
     "Art.51A(g)", "Art.51A(h)",
     "Art.51A(i) (correct)",
     "Art.51A(j)",
     "C",
     "Art.51A(i): To SAFEGUARD PUBLIC PROPERTY and to ABJURE VIOLENCE. Important during protests/agitations — prohibits damage to govt property. Implementation: Prevention of Damage to Public Property Act 1984. Recent debate around bandhs and violent protests."),

    (1, "medium",
     "Strive towards excellence in all spheres — which clause?\nతెలుగు: శ్రేష్ఠత?",
     "Art.51A(h)", "Art.51A(i)",
     "Art.51A(j) (correct)",
     "Art.51A(k)",
     "C",
     "Art.51A(j): To STRIVE TOWARDS EXCELLENCE in all spheres of INDIVIDUAL AND COLLECTIVE ACTIVITY so that the nation constantly RISES TO HIGHER LEVELS of endeavour and achievement. Aspirational duty — promotes meritocracy, civic engagement, professional excellence."),

    (1, "easy",
     "Educational opportunities for children 6-14 by parents — which clause?\nతెలుగు: తల్లిదండ్రుల విధి?",
     "Art.51A(i)", "Art.51A(j)",
     "Art.51A(k) (correct)",
     "Art.51A(l)",
     "C",
     "Art.51A(k): It shall be the DUTY OF EVERY PARENT OR GUARDIAN to PROVIDE OPPORTUNITIES FOR EDUCATION to his child or, as the case may be, ward BETWEEN THE AGE OF 6 AND 14 YEARS. Added by 86th Amendment 2002 — companion to Art.21A FR (free education) and modified Art.45 DPSP (early childhood). Note: 6-14, NOT below 6."),

    # ───── Section 2: Nature & Features ─────
    (2, "medium",
     "Are Fundamental Duties enforceable through courts?\nతెలుగు: Court enforce చేయగలమా?",
     "Yes, like FRs",
     "Yes, only via SC",
     "No, non-justiciable / కాదు, non-justiciable (correct)",
     "Yes, like DPSPs",
     "C",
     "FDs are NON-JUSTICIABLE — cannot be DIRECTLY enforced in courts (no specific writ for FD violation). However: (1) Parliament can make laws to enforce them with penalties; (2) Courts use FDs as INTERPRETIVE TOOL when assessing constitutionality of laws (AIIMS Students Union 2001). Indirect enforcement through legislation."),

    (2, "easy",
     "Fundamental Duties apply to whom?\nతెలుగు: ఎవరికి వర్తిస్తాయి?",
     "Only Government employees",
     "Only Citizens of India / కేవలం పౌరులకే (correct)",
     "Citizens and foreigners",
     "All residents of India",
     "B",
     "FDs apply ONLY to INDIAN CITIZENS — not foreigners. Differs from FRs where some apply to all persons (Art.14, 21, etc.). FDs are aimed at fostering CIVIC COMMITMENT among citizens. Foreigners have visa/legal obligations but not these constitutional duties."),

    (2, "medium",
     "What happens when Fundamental Duties are violated?\nతెలుగు: ఉల్లంఘించినప్పుడు?",
     "Enforceable in courts like FRs",
     "Parliament can prescribe punishment via law / Parliament చట్టం ద్వారా (correct)",
     "Citizenship loss", "Only moral stigma",
     "B",
     "Though FDs are non-justiciable, PARLIAMENT can PRESCRIBE PENALTIES through law for breach. E.g., Prevention of Insults to National Honour Act 1971 (insulting Anthem/Flag — punishment up to 3 years). Sedition (Art.51A(c)). Verma Committee 2002 noted many existing laws already implement FDs indirectly."),

    (2, "hard",
     "Which statement about FDs is correct?\nతెలుగు: సరైన వ్యాఖ్య?",
     "Directly enforceable in courts",
     "Apply to foreigners",
     "Courts can use them to determine constitutionality of laws / Court constitutionality లో ఉపయోగించవచ్చు (correct)",
     "Apply to State",
     "C",
     "AIIMS STUDENTS UNION v. AIIMS (2001): SC held FDs CAN BE USED by courts to DETERMINE CONSTITUTIONALITY of laws. So FDs serve as INTERPRETIVE GUIDE — though not directly enforceable. Other landmarks: M.C. Mehta (1991) used Art.51A(g) for environmental protection; Aruna Roy (2002) on RTI used Art.51A."),

    (2, "easy",
     "Where in Constitution are FDs placed?\nతెలుగు: రాజ్యాంగంలో ఎక్కడ?",
     "After FRs (Part III)",
     "After DPSPs (Part IV) — in new Part IVA / Part IVA (correct)",
     "Before Preamble", "In Part V",
     "B",
     "FDs in Part IVA — newly created by 42nd Am 1976. Sequence: Part III (FRs - Art.12-35); Part IV (DPSPs - Art.36-51); Part IVA (FDs - Art.51A); Part V (Union - President, PM, Parliament, etc.). Logical sequence: rights → state's directives → citizens' duties → governance structures."),

    (2, "medium",
     "How many clauses does Article 51A currently have?\nతెలుగు: ప్రస్తుతం ఎన్ని?",
     "9", "10",
     "11 clauses (a to k) / 11 (a-k) (correct)",
     "12",
     "C",
     "Art.51A currently has 11 CLAUSES (a, b, c, d, e, f, g, h, i, j, k). Original 10 (a-j) added by 42nd Am 1976. 11th (k) — parents' duty for child education — added by 86th Am 2002. Parliament has not added more since."),

    # ───── Section 3: Swaran Singh Committee ─────
    (3, "medium",
     "Who set up the Swaran Singh Committee?\nతెలుగు: Committee ఎవరు?",
     "President Fakhruddin Ali Ahmed",
     "Congress government under Indira Gandhi / ఇందిరా గాంధీ ప్రభుత్వం (correct)",
     "Jayaprakash Narayan",
     "Morarji Desai government",
     "B",
     "SWARAN SINGH COMMITTEE set up by INDIRA GANDHI's CONGRESS GOVERNMENT in 1976 during Emergency. Sardar Swaran Singh — Cabinet Minister (External Affairs/Defence). Reviewed Constitution; recommended FDs and other major reforms. Many recommendations led to 42nd Amendment 1976. Some controversial."),

    (3, "hard",
     "How many FDs did Swaran Singh Committee recommend?\nతెలుగు: Committee ఎన్ని recommend చేసింది?",
     "6", "8 (correct)", "10", "11",
     "B",
     "Swaran Singh Committee recommended 8 FUNDAMENTAL DUTIES. PARLIAMENT added 2 MORE = 10 (Art.51A(a) to (j)) through 42nd Amendment 1976. The 2 added by Parliament: (a) Abide by Constitution + respect Flag/Anthem; (g) Protect environment. Later 11th (k) added in 2002."),

    (3, "medium",
     "Swaran Singh Committee's recommendation on violation of duties?\nతెలుగు: ఉల్లంఘన?",
     "Make justiciable",
     "Parliament should prescribe penalties for breach / శిక్షలు (correct)",
     "Revoke citizenship",
     "Leave as DPSPs-style guidelines",
     "B",
     "Swaran Singh Committee recommended that PARLIAMENT should PRESCRIBE PENALTIES for breach of FDs through suitable legislation — making them indirectly enforceable. This recommendation was NOT accepted in 42nd Amendment — FDs were left non-justiciable. However, individual laws (e.g., Insults to National Honour Act) do penalise specific FD breaches."),

    (3, "hard",
     "Where did Swaran Singh Committee recommend placing FDs?\nతెలుగు: ఎక్కడ ఉంచమని?",
     "In Part III (FRs)", "In separate Schedule",
     "As new Part after DPSPs (Part IV) / DPSPs తర్వాత కొత్త Part (correct)",
     "In Preamble",
     "C",
     "Swaran Singh Committee recommended FDs be placed as a NEW PART after DPSPs (Part IV). 42nd Amendment 1976 followed this — created Part IVA with single Article 51A. This placement reflects logical sequence: State's directives (DPSPs) → Citizens' duties (FDs). Both non-justiciable, both forming 'conscience' of Constitution."),

    # ───── Section 4: 86th Amendment & Art.51A(k) ─────
    (4, "easy",
     "When was 86th Constitutional Amendment passed?\nతెలుగు: 86వ సవరణ?",
     "2000", "2001",
     "2002 (correct)", "2004",
     "C",
     "86th Constitutional Amendment Act 2002 made 3 major changes: (1) Added Art.21A (Right to Education 6-14 — FR); (2) Modified Art.45 DPSP (early childhood care under 6); (3) Added Art.51A(k) (parents' duty for child education). Came into force 1 April 2010 with RTE Act 2009. Single amendment, three connected changes.",
     "APPSC"),

    (4, "medium",
     "11th Fundamental Duty added by 86th Amendment 2002?\nతెలుగు: 11వ విధి?",
     "Environment protection",
     "Parents/guardians provide educational opportunities for children 6-14 / 6-14 విద్యా అవకాశాలు (correct)",
     "Uphold national unity",
     "Develop scientific temper",
     "B",
     "11th FD = Art.51A(k) added by 86th Am 2002: 'It shall be the DUTY OF EVERY PARENT OR GUARDIAN to PROVIDE OPPORTUNITIES FOR EDUCATION to his child or, as the case may be, ward between the AGE OF SIX AND FOURTEEN YEARS.' Connects with Art.21A (state's duty to provide free education) — completes the loop: State + Parents both responsible.",
     "APPSC"),

    (4, "medium",
     "86th Amendment 2002 added which Article AND which Fundamental Duty?\nతెలుగు: ఏ Article + ఏ Duty?",
     "Art.21 and Art.51A(j)",
     "Art.21A and Art.51A(k) / Art.21A + Art.51A(k) (correct)",
     "Art.21A only", "Art.51A(k) only",
     "B",
     "86th Amendment 2002 added BOTH: (1) Art.21A — Right to Education (6-14 years) as FUNDAMENTAL RIGHT; (2) Art.51A(k) — duty of every parent/guardian to provide educational opportunities for children 6-14. State's right + Parent's duty = comprehensive education framework. Implementation: RTE Act 2009."),

    (4, "hard",
     "Per Art.51A(k), educational opportunities for 6-14 children is duty of?\nతెలుగు: విద్యా అవకాశాలు ఎవరి విధి?",
     "Mother only", "Father only",
     "Every parent or guardian / తల్లిదండ్రి లేదా సంరక్షకుడు (correct)",
     "State (Government)",
     "C",
     "Art.51A(k): DUTY OF EVERY PARENT OR GUARDIAN — uses gender-neutral 'parent' (mother/father). Includes 'GUARDIAN' for orphans/parentless children. State's parallel duty is under Art.21A — to PROVIDE free and compulsory education. So child education = JOINT responsibility of State (Art.21A) + Parents (Art.51A(k))."),

    # ───── Section 5: FRs vs FDs vs DPSPs ─────
    (5, "medium",
     "Key difference between FRs and FDs?\nతెలుగు: FRs vs FDs?",
     "FRs only citizens, FDs all",
     "FRs justiciable, FDs non-justiciable / FRs justiciable, FDs not (correct)",
     "FRs in DPSPs, FDs in Part III",
     "FRs unamendable",
     "B",
     "FRs vs FDs: (1) JUSTICIABILITY — FRs JUSTICIABLE (Art.32/226 enforcement); FDs NON-JUSTICIABLE. (2) PART — FRs Part III; FDs Part IVA. (3) APPLICATION — FRs apply to all persons (some) + citizens (some); FDs only citizens. (4) NATURE — FRs are RIGHTS (negative obligations on State); FDs are DUTIES (positive obligations on citizens)."),

    (5, "medium",
     "Key similarity between FDs and DPSPs?\nతెలుగు: FDs vs DPSPs ఉమ్మడి?",
     "Both only citizens",
     "Both non-justiciable / రెండూ Non-justiciable (correct)",
     "Both added by 42nd Am",
     "Both national directives",
     "B",
     "COMMON: Both NON-JUSTICIABLE — cannot be directly enforced in courts. KEY DIFFERENCE: DPSPs are DIRECTIVES TO STATE (Part IV); FDs are DUTIES FOR CITIZENS (Part IVA). DPSPs from Irish Constitution; FDs from USSR. Together they form 'CONSCIENCE OF THE CONSTITUTION' alongside FRs."),

    (5, "hard",
     "Source of FDs is?\nతెలుగు: FDs మూలం?",
     "USA Bill of Rights",
     "USSR Constitution / USSR (correct)",
     "Irish Constitution", "Japanese Constitution",
     "B",
     "FDs borrowed from USSR (SOVIET) Constitution 1977 — first major modern constitution to enumerate citizens' duties to State. Combined with: FRs from US Bill of Rights (1791); DPSPs from Ireland 1937 (drew from Spain); Parliamentary system from UK; Federal scheme from Canada; Emergency from German Weimar. Each major feature has different external influence.",
     "APPSC"),

    (5, "medium",
     "Common feature of FRs and FDs?\nతెలుగు: FRs + FDs ఉమ్మడి?",
     "Both directives for govt", "Both only citizens",
     "Both justiciable",
     "Both can be amended by Parliament / రెండూ Parliament సవరించవచ్చు (correct)",
     "D",
     "FRs and FDs both can be AMENDED BY PARLIAMENT (subject to Basic Structure doctrine). FRs apply to citizens + some to non-citizens; FDs only to citizens. FRs justiciable; FDs not. Both are integral to constitutional scheme — Granville Austin's 'conscience of the Constitution' included FRs + DPSPs (he wrote pre-FDs), but the same logic applies post-FD addition."),

    (5, "hard",
     "Which is NOT true about Fundamental Duties?\nతెలుగు: సరైనది కాని వ్యాఖ్య?",
     "Enforceable through Parliament's law",
     "Apply only to citizens",
     "Directly enforceable through courts / Court ద్వారా నేరుగా (correct)",
     "Added by 42nd Am 1976",
     "C",
     "FDs are NOT directly enforceable through courts (non-justiciable). Hence answer C is INCORRECT statement. Other options TRUE: (A) Parliament can pass laws enforcing FDs with penalties. (B) Apply only to citizens. (D) Added by 42nd Am 1976. So 'directly enforceable through courts' is the FALSE statement."),

    # ───── Section 6: Cases & Implementation ─────
    (6, "hard",
     "Bijoe Emmanuel v. State of Kerala (1986) related to which FD?\nతెలుగు: Bijoe Emmanuel?",
     "Child labour",
     "Refusal to sing National Anthem — Art.51A(a) duty vs Art.25 right / జాతీయ గీతం (correct)",
     "Religious conversion", "Environment",
     "B",
     "BIJOE EMMANUEL v. STATE OF KERALA (1986): Three Jehovah's Witness students did not SING National Anthem (only stood respectfully) due to religious belief. Expelled by school. SC RULED: Right to freedom of religion (Art.25) protects them. Standing respectfully = sufficient. SC upheld Art.51A(a) duty + Art.25 freedom co-exist. Reinstated students. Landmark case on FD-FR balance."),

    (6, "hard",
     "Verma Committee 2002 was on?\nతెలుగు: Verma Committee?",
     "Operationalisation of Fundamental Duties / FDs అమలు (correct)",
     "Constitutional amendment", "FRs extension", "DPSPs implementation",
     "A",
     "JUSTICE J.S. VERMA COMMITTEE 2002 reviewed OPERATIONALISATION of FDs. Reported many EXISTING LAWS already implement FDs: Protection of Civil Rights Act 1955 (Art.51A(e) — women's dignity); Environment Protection Act 1986 (Art.51A(g) — environment); Wildlife Protection Act 1972 — various other acts. Recommended awareness campaigns, education on FDs."),

    (6, "medium",
     "What did SC say in AIIMS Students Union v. AIIMS (2001) about FDs?\nతెలుగు: AIIMS 2001?",
     "FDs justiciable",
     "FDs should be repealed",
     "FDs useful for determining constitutional validity / చట్టాల constitutional validity (correct)",
     "FDs superior to FRs",
     "C",
     "AIIMS STUDENTS UNION v. AIIMS (2001): SC held FDs are USEFUL in determining the CONSTITUTIONAL VALIDITY of laws. While FDs themselves not directly enforceable, COURTS can REFER to them when assessing whether a law is unconstitutional or whether a particular interpretation is preferred. Establishes interpretive role of FDs."),

    (6, "easy",
     "Total number of Fundamental Duties currently?\nతెలుగు: ప్రస్తుతం ఎన్ని?",
     "9", "10",
     "11 (correct)",
     "12",
     "C",
     "Currently 11 FDs in Art.51A: 10 (clauses a-j) added by 42nd Amendment 1976; 11th (clause k) added by 86th Amendment 2002. No further additions since. Constitution makers expected society to evolve with these 11 duties guiding civic behaviour.",
     "APPSC"),

    (6, "medium",
     "Which Act implements Art.51A(e) — duty about women's dignity?\nతెలుగు: Art.51A(e) Act?",
     "Protection of Civil Rights Act 1955 (correct)",
     "Immoral Traffic (Prevention) Act 1956",
     "Environment Protection Act 1986", "Bonded Labour Act 1976",
     "A",
     "Verma Committee 2002: PROTECTION OF CIVIL RIGHTS ACT 1955 (originally Untouchability Offences Act 1955) operationalises Art.51A(e) (harmony, women's dignity) by penalising untouchability practices. Other Acts implementing Art.51A(e): Dowry Prohibition Act 1961, Indecent Representation of Women Act 1986, etc."),

    (6, "medium",
     "Which Act implements Art.51A(g) — environment duty?\nతెలుగు: Art.51A(g) Act?",
     "Forest Conservation Act 1980",
     "Wildlife Protection Act 1972",
     "Environment Protection Act 1986 (correct)",
     "Water Pollution Act 1974",
     "C",
     "ENVIRONMENT PROTECTION ACT 1986 — umbrella legislation operationalising Art.51A(g) (protect natural environment). Empowers Centre to make rules for environmental quality. Companion: Wildlife (Protection) Act 1972, Forest Conservation Act 1980, Water Act 1974, Air Act 1981. EPA 1986 enacted post Bhopal disaster (1984) under Art.253 (international obligations from Stockholm 1972)."),

    (6, "medium",
     "In which Schedule are Fundamental Duties listed?\nతెలుగు: ఏ Schedule?",
     "Third Schedule",
     "Not in any Schedule — directly in Article 51A / ఏ Schedule లోనూ లేదు (correct)",
     "Fourth Schedule", "Ninth Schedule",
     "B",
     "FDs are NOT listed in any Schedule. They are directly in Article 51A (Part IVA). Compare: FRs in Part III (no Schedule); DPSPs in Part IV (no Schedule); Languages in Eighth Schedule; Anti-defection in Tenth Schedule. FDs follow the Articles-based placement, not Schedule-based."),

    # ───── Section 7: PYQ Comprehensive ─────
    (7, "hard",
     "Which is NOT a Fundamental Duty under Article 51A?\nతెలుగు: FD కానిది?",
     "Develop scientific temper",
     "Pay taxes promptly / పన్నులు చెల్లించడం (correct)",
     "Protect natural environment", "Abide by National Anthem",
     "B",
     "PAYING TAXES is NOT among the 11 FDs. It is a general civic obligation under tax laws but NOT a constitutional Fundamental Duty. Other options ARE FDs: Scientific temper (Art.51A(h)); Environment (Art.51A(g)); National Anthem (Art.51A(a)). Many candidates confuse civic duties with constitutional FDs."),

    (7, "hard",
     "Which statements about FDs are correct? (1) Added by 44th Am 1978 (2) Borrowed from USSR (3) Apply only to citizens (4) 11th by 86th Am 2002\nతెలుగు: సరైనవి?",
     "Only 2, 3 and 4 (correct)",
     "Only 1, 2 and 3", "Only 3 and 4", "All",
     "A",
     "Statement 1 is WRONG: FDs added by 42nd AMENDMENT 1976 (not 44th Am 1978 — which removed Right to Property). Statements 2, 3, 4 are TRUE: (2) USSR source. (3) Citizens only. (4) 11th FD by 86th Am 2002. Therefore correct answer: only 2, 3, 4."),

    (7, "hard",
     "What is the FD under Article 51A(g)?\nతెలుగు: Art.51A(g)?",
     "Composite cultural heritage",
     "Protect/improve natural environment (forests, lakes, rivers, wildlife) / పర్యావరణం (correct)",
     "Scientific temper", "Public property",
     "B",
     "Art.51A FD clauses identification: (a) Constitution/Flag/Anthem; (b) freedom struggle ideals; (c) sovereignty/integrity; (d) defend country; (e) brotherhood + women's dignity; (f) composite culture; (g) NATURAL ENVIRONMENT, forests, lakes, rivers, wildlife, compassion to creatures; (h) scientific temper; (i) public property + abjure violence; (j) excellence; (k) parents' duty for education."),

    (7, "hard",
     "Of the 10 FDs added by 42nd Am 1976, how many were per Swaran Singh Committee?\nతెలుగు: Committee ఎన్ని?",
     "10 — all per Committee",
     "8 — Committee recommended 8; Parliament added 2 / 8 + 2 (correct)",
     "6", "5",
     "B",
     "Swaran Singh Committee recommended 8 duties. PARLIAMENT added 2 MORE on its own = total 10 (Art.51A(a)-(j)) through 42nd Amendment 1976. The 2 added by Parliament: (a) Abide by Constitution + Flag/Anthem; (g) Protect environment. Later (2002), 86th Am added 11th (k) — parents' duty for child education. Currently 11 FDs total."),
]



import json as _json


def _seed_polity_ch10_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    import json as _j
    ph = '%s' if use_postgres else '?'
    _sections = [
    {"title": "10.1 ప్రాథమిక విధులు పరిచయం", "sub": "Introduction · Part IVA · Art 51A · 42nd Amdt 1976 · USSR", "audio": ""},
    {"title": "10.2 11 విధుల జాబితా", "sub": "List of 11 Duties · Art 51A(a) to 51A(k) · All Duties", "audio": ""},
    {"title": "10.3 స్వభావం మరియు లక్షణాలు", "sub": "Nature · Features · Non-Justiciable · Moral Obligations", "audio": ""},
    {"title": "10.4 స్వర్ణ సింగ్ కమిటీ", "sub": "Swaran Singh Committee · 1976 · Recommendations · 8 Duties", "audio": ""},
    {"title": "10.5 86వ సవరణ — 11వ విధి", "sub": "86th Amendment 2002 · Art 51A(k) · 11th Duty · Education", "audio": ""},
    {"title": "10.6 FR vs FD vs DPSP పోలిక", "sub": "Comparison · Justiciable · Non-Justiciable · Sources", "audio": ""},
    {"title": "10.7 ముఖ్య కేసులు", "sub": "Cases · PYQs · APPSC · Fundamental Duties enforcement", "audio": ""},
    {"title": "10.8 కఠిన ప్రశ్నలు", "sub": "Tough MCQs · APPSC Style · Verma Committee · Art 51A clauses", "audio": ""}
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
        (10, 'Indian_Polity'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True,
                'message': 'Polity Ch10 notes already seeded.'}
    if row and force:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (10, 'Indian_Polity'))
    if use_postgres:
        conn.commit()

    db_exec_fn(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'Indian_Polity', '', 10,
         'ప్రాథమిక విధులు',
         'Fundamental Duties',
         'Ch.10',
         _j.dumps(_sections, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'Polity Ch10 notes seeded!'}


def _seed_polity_ch10_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
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
        (10, 'Indian_Polity'))
    row = cur.fetchone()
    if not row:
        _seed_polity_ch10_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)
        cur = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (10, 'Indian_Polity'))
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
    for mcq in POLITY_CH10_MCQS:
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

    total = len(POLITY_CH10_MCQS)
    return {
        'success': True,
        'message': f'Polity Ch10 MCQs seeded! Total: {total}',
        'inserted': total,
        'easy': easy, 'medium': medium, 'hard': hard,
        'toughest': toughest, 'pyq': pyq
    }
