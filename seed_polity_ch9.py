# ─────────────────────────────────────────────────────────────────────────────
# seed_polity_ch9.py
# Chapter 9 – Directive Principles of State Policy (Art 36–51) · Part IV
# Lakshmikanth's Indian Polity | APPSC Group 2 Standard
# Total MCQs: 75 | PYQs: 15 | Format: Bilingual (Telugu + English)
# ─────────────────────────────────────────────────────────────────────────────

import json as _json

POLITY_CH9_MCQS = [
    # ───── Section 0: DPSP Introduction ─────
    (0, 1,
     "In which Part of Constitution are DPSPs contained?\nతెలుగు: DPSPs ఏ Part?",
     "Part III", "Part IV (correct)", "Part IVA", "Part V",
     "b",
     "DIRECTIVE PRINCIPLES OF STATE POLICY (DPSPs) are contained in PART IV of the Constitution, covering Articles 36-51. Non-justiciable but fundamental in governance (Art.37). Borrowed from Irish Constitution 1937. Aim: socio-economic democracy. Part IVA = Fundamental Duties (Art.51A)."),

    (0, 1,
     "DPSPs were borrowed from which country's Constitution?\nతెలుగు: ఏ దేశం నుండి?",
     "USA", "Ireland (correct)", "Canada", "Australia",
     "b",
     "Concept of DPSPs borrowed from IRISH (Eire) Constitution 1937. Ireland in turn drew from Spanish Constitution. The framework of non-enforceable but morally binding principles is unique. Indian Constitution makers added many Indian-specific principles like Gandhian goals (panchayats, prohibition).",
     "APPSC"),

    (0, 2,
     "What is the nature of DPSPs under Article 37?\nతెలుగు: Art.37 స్వభావం?",
     "Justiciable by courts",
     "Non-justiciable but fundamental in governance / Non-justiciable, fundamental (correct)",
     "Completely optional", "Only for State Govts",
     "b",
     "Art.37: 'The provisions in this Part shall NOT be ENFORCEABLE by any court, but the principles laid down therein are NEVERTHELESS FUNDAMENTAL in the governance of the country and it shall be the DUTY OF THE STATE to apply these principles in making laws.' Defining feature of DPSPs."),

    (0, 2,
     "Who described DPSPs as 'cheque payable at the bank's convenience'?\nతెలుగు: 'Cheque' అని ఎవరు?",
     "T.T. Krishnamachari", "K.T. Shah (correct)",
     "B.R. Ambedkar", "Jawaharlal Nehru",
     "b",
     "K.T. SHAH (member of Constituent Assembly, economist) described DPSPs as 'A CHEQUE ON A BANK PAYABLE ONLY WHEN THE RESOURCES OF THE BANK PERMIT' — meaning DPSPs are dependent on State's resources and political will. Other critical descriptions: T.T. Krishnamachari called them 'pious wishes'; Nazirudin Ahmed called them 'pious superfluities'."),

    (0, 1,
     "Definition of 'State' in Article 36 is same as which Article?\nతెలుగు: Art.36 'State' ఏ Article?",
     "Article 10", "Article 12 (correct)", "Article 13", "Article 19",
     "b",
     "Article 36: 'State' for purposes of DPSPs has the SAME MEANING as in Art.12 (used for Fundamental Rights). Includes: Government and Parliament of India, Government and Legislature of every State, all local authorities, and other authorities under Government control."),

    (0, 3,
     "B.R. Ambedkar compared DPSPs to which historical document?\nతెలుగు: అంబేడ్కర్ ఏ document?",
     "'Instruments of Instructions' in GoI Act 1935 / GoI Act 1935 (correct)",
     "Administrative rules in GoI Act 1919",
     "Irish Constitution principles", "Magna Carta",
     "a",
     "Ambedkar in CA debate compared DPSPs to the 'INSTRUMENTS OF INSTRUCTIONS' issued under Government of India Act 1935 — directions to Governor-General and Governors on exercise of discretionary powers. The 1935 Act required these officials to act in conformity with such instructions — though they were not legally enforceable."),

    (0, 3,
     "Which amendment added clause (2) to Article 38?\nతెలుగు: Art.38(2) ఏ సవరణ?",
     "25th Amdt 1971",
     "42nd Amdt 1976",
     "44th Amdt 1978 — minimise inequalities in income, status, opportunities (correct)",
     "86th Amdt 2002",
     "c",
     "44th Amendment 1978 added Art.38(2): 'The State shall, in particular, strive to MINIMISE INEQUALITIES in INCOME, and endeavour to ELIMINATE INEQUALITIES in STATUS, FACILITIES and OPPORTUNITIES, not only amongst individuals but also amongst groups of people residing in different areas or engaged in different vocations.' Reflects post-Emergency commitment to socio-economic equity."),

    # ───── Section 1: Socialistic DPSPs (Art 38-43B) ─────
    (1, 2,
     "What does Article 38 direct?\nతెలుగు: Art.38?",
     "Free legal aid",
     "Social order securing social, economic, political justice / సామాజిక-ఆర్థిక-రాజకీయ న్యాయం (correct)",
     "Living wage", "Village panchayats",
     "b",
     "Art.38: Welfare state provision. (1) State shall STRIVE to PROMOTE WELFARE OF PEOPLE by securing a SOCIAL ORDER in which JUSTICE — social, economic, political — shall inform all institutions of national life. (2) Strive to MINIMISE INEQUALITIES in income, status, facilities and opportunities (added by 44th Am). Foundation Socialistic DPSP."),

    (1, 2,
     "What does Article 39(a) direct?\nతెలుగు: Art.39(a)?",
     "Equal pay",
     "Equal right to adequate means of livelihood for men and women / జీవనోపాధికి సమాన హక్కు (correct)",
     "Living wage for workers", "Free legal aid",
     "b",
     "Art.39(a): 'The State shall direct its policy towards securing that the citizens, MEN AND WOMEN equally, have the RIGHT TO AN ADEQUATE MEANS OF LIVELIHOOD.' Socialistic DPSP — economic justice with gender equality. Olga Tellis v. BMC (1985) read this with Art.21 to recognise right to livelihood as part of right to life."),

    (1, 2,
     "What does Article 39(b) direct?\nతెలుగు: Art.39(b)?",
     "Equal pay",
     "Material resources of community distributed for common good / భౌతిక వనరులు ఉమ్మడి మేలు కోసం (correct)",
     "Free legal aid", "Living wage",
     "b",
     "Art.39(b): 'Ownership and control of the MATERIAL RESOURCES of the community are so distributed as best to subserve the COMMON GOOD.' One of two DPSPs given protection under Art.31C from Art.14/19 challenge. Central to land reforms, nationalisation cases. Recently reinterpreted in Property Owners Association (2024) — narrowed scope."),

    (1, 2,
     "What does Article 39(c) direct?\nతెలుగు: Art.39(c)?",
     "Uniform Civil Code",
     "Prevention of concentration of wealth and means of production / సంపద కేంద్రీకరణ నివారణ (correct)",
     "Protection of agriculture", "Maternity relief",
     "b",
     "Art.39(c): 'Operation of the economic system does NOT result in concentration of WEALTH and MEANS OF PRODUCTION to the COMMON DETRIMENT.' Socialistic DPSP — anti-monopoly principle. Together with Art.39(b), protected under Art.31C. Underlies competition laws, anti-monopoly regulation."),

    (1, 1,
     "Article 39A on equal justice and free legal aid was added by which Amendment?\nతెలుగు: Art.39A?",
     "24th Amdt 1971",
     "42nd Amdt 1976 (correct)",
     "44th Amdt 1978", "86th Amdt 2002",
     "b",
     "Art.39A added by 42nd CONSTITUTIONAL AMENDMENT 1976: 'The State shall secure that the operation of the legal system promotes JUSTICE, on a basis of EQUAL OPPORTUNITY, and shall, in particular, provide FREE LEGAL AID, by suitable legislation or schemes...' Implementation: Legal Services Authorities Act 1987 (NALSA). Hussainara Khatoon (1979) elevated this to FR via Art.21.",
     "APPSC"),

    (1, 2,
     "What does Article 42 direct?\nతెలుగు: Art.42?",
     "Living wage",
     "Just and humane conditions of work and maternity relief / న్యాయమైన పని పరిస్థితులు + మాతృత్వ సహాయం (correct)",
     "Workers' participation", "Right to work",
     "b",
     "Art.42: 'The State shall make provision for securing JUST AND HUMANE CONDITIONS OF WORK and for MATERNITY RELIEF.' Socialistic DPSP — labour protection. Implementation: Maternity Benefit Act 1961 (revised 2017 — 26 weeks paid leave), Factories Act 1948, Equal Remuneration Act 1976."),

    (1, 1,
     "Article 43A on workers' participation in management added by?\nతెలుగు: Art.43A?",
     "25th Amdt 1971",
     "42nd Amdt 1976 (correct)",
     "44th Amdt 1978", "97th Amdt 2011",
     "b",
     "Art.43A added by 42nd Amendment 1976: 'The State shall take steps, by suitable legislation or in any other way, to secure the PARTICIPATION OF WORKERS in the MANAGEMENT of UNDERTAKINGS, establishments or other organisations engaged in any industry.' Industrial democracy principle. Limited implementation in India."),

    (1, 2,
     "Article 43B on cooperative societies was added by?\nతెలుగు: Art.43B?",
     "42nd Amdt 1976", "86th Amdt 2002",
     "97th Amdt 2011 (correct)", "99th Amdt 2014",
     "c",
     "Art.43B added by 97th Constitutional Amendment 2011: 'The State shall endeavour to PROMOTE VOLUNTARY FORMATION, AUTONOMOUS FUNCTIONING, DEMOCRATIC CONTROL and PROFESSIONAL MANAGEMENT of COOPERATIVE SOCIETIES.' Same Amendment also added Part IXB (Art.243ZH-243ZT) on cooperatives. Vipulbhai Chaudhary (2013): Part IXB partially struck down for lack of state ratification.",
     "APPSC"),

    (1, 2,
     "What does Article 39(d) direct?\nతెలుగు: Art.39(d)?",
     "Children's healthy development",
     "Equal justice for women",
     "Equal pay for equal work for men and women / సమాన పని కు సమాన వేతనం (correct)",
     "Environment protection",
     "c",
     "Art.39(d): 'EQUAL PAY FOR EQUAL WORK for both men and women.' Read with Art.14 (equality), gives a strong gender-equality basis. Randhir Singh v. UoI (1982): SC enforced this principle through Art.14 + Art.16 — even though Art.39(d) itself non-justiciable. Implementation: Equal Remuneration Act 1976.",
     "APPSC"),

    (1, 2,
     "What does Article 41 direct?\nతెలుగు: Art.41?",
     "Education only",
     "Right to work, education, public assistance in unemployment/old age/sickness/disablement / పని, విద్య, పబ్లిక్ సహాయం (correct)",
     "Work and maternity", "Work and living wage",
     "b",
     "Art.41: 'The State shall, within the limits of its economic capacity and development, make EFFECTIVE PROVISION for securing the RIGHT TO WORK, to EDUCATION and to PUBLIC ASSISTANCE in cases of UNEMPLOYMENT, OLD AGE, SICKNESS and DISABLEMENT, and in other cases of undeserved want.' Foundation for MGNREGA, NSAP (pensions), education laws."),

    (1, 2,
     "What does Article 43 direct?\nతెలుగు: Art.43?",
     "Environment protection",
     "Living wage, work conditions, leisure for all workers / జీవన వేతనం, విశ్రాంతి (correct)",
     "Village panchayats", "Cattle slaughter ban",
     "b",
     "Art.43: 'The State shall endeavour to secure, by suitable legislation or economic organisation or in any other way, to all WORKERS, agricultural, industrial or otherwise, work, a LIVING WAGE, conditions of work ensuring a DECENT STANDARD OF LIFE and FULL ENJOYMENT OF LEISURE and social and cultural opportunities.' Cottage industries promoted as part of Art.43."),

    (1, 3,
     "42nd Amendment 1976 added which new DPSP Articles?\nతెలుగు: 42వ సవరణ DPSPs?",
     "Art.38(2), Art.39A",
     "Art.39A, Art.43A, Art.48A (correct)",
     "Art.44, Art.46, Art.47", "Art.40, Art.41, Art.42",
     "b",
     "42nd Amendment 1976 added 3 NEW DPSPs: (1) Art.39A — Equal justice & free legal aid; (2) Art.43A — Workers' participation in management; (3) Art.48A — Environment protection, forests, wildlife. Also amended Art.31C to extend protection to all DPSPs (struck down by Minerva Mills 1980)."),

    (1, 1,
     "What does Article 39(e) direct?\nతెలుగు: Art.39(e)?",
     "Right to work",
     "Health/strength of workers and children not abused / కార్మికులు, పిల్లల ఆరోగ్యం (correct)",
     "Equal pay", "Maternity relief",
     "b",
     "Art.39(e): 'The HEALTH AND STRENGTH OF WORKERS, men and women, and the TENDER AGE OF CHILDREN are NOT ABUSED and citizens are not forced by economic necessity to enter avocations unsuited to their age or strength.' Anti-exploitation principle. Read with Art.24 (child labour ban) and Art.42 (humane conditions)."),

    (1, 1,
     "What does Article 39(f) direct?\nతెలుగు: Art.39(f)?",
     "Adult education",
     "Children given opportunities for healthy development; protected against exploitation / పిల్లలకు అభివృద్ధి అవకాశాలు (correct)",
     "Vocational training", "Public assistance",
     "b",
     "Art.39(f) [substituted by 42nd Am 1976]: 'CHILDREN are given OPPORTUNITIES and FACILITIES to DEVELOP in a HEALTHY MANNER and in conditions of FREEDOM AND DIGNITY and that childhood and youth are PROTECTED AGAINST EXPLOITATION and against MORAL AND MATERIAL ABANDONMENT.' Foundation for child rights legislation. NCPCR oversight."),

    (1, 2,
     "What does Article 43 promote besides living wage?\nతెలుగు: Art.43 cottage industries?",
     "Heavy industries",
     "Cottage industries on individual or co-operative basis in rural areas / కుటీర పరిశ్రమలు (correct)",
     "Big PSUs", "Foreign investment",
     "b",
     "Art.43 second part: 'State shall ENDEAVOUR to PROMOTE COTTAGE INDUSTRIES on an INDIVIDUAL OR COOPERATIVE BASIS in RURAL AREAS.' Reflects Gandhian vision of decentralised production. KVIC (Khadi & Village Industries Commission) implements this. Combines Socialistic + Gandhian features in single Article."),

    # ───── Section 2: Gandhian DPSPs ─────
    (2, 1,
     "Which Article relates to organisation of village panchayats?\nతెలుగు: గ్రామ పంచాయితీలు?",
     "Article 38", "Article 40 (correct)",
     "Article 43", "Article 46",
     "b",
     "Art.40: 'The State shall take steps to ORGANISE VILLAGE PANCHAYATS and ENDOW them with such POWERS and AUTHORITY as may be necessary to enable them to function as UNITS OF SELF-GOVERNMENT.' GANDHIAN DPSP — Gandhi's vision of 'GRAM SWARAJYA'. Operationalised by 73rd Amendment 1992 (Panchayati Raj constitutional status — Part IX, Art.243-243O)."),

    (2, 2,
     "Article 46 directs promotion of educational/economic interests of?\nతెలుగు: Art.46?",
     "Women and children",
     "SC, ST and weaker sections / SC, ST + బలహీన వర్గాలు (correct)",
     "OBC and Minorities", "Disabled and elderly",
     "b",
     "Art.46: 'The State shall PROMOTE WITH SPECIAL CARE the EDUCATIONAL AND ECONOMIC INTERESTS of the WEAKER SECTIONS of the people, and IN PARTICULAR, of the SCHEDULED CASTES and SCHEDULED TRIBES, and shall PROTECT them from SOCIAL INJUSTICE and ALL FORMS OF EXPLOITATION.' GANDHIAN DPSP. Foundation for SC/ST welfare schemes, scholarships, anti-atrocity laws."),

    (2, 2,
     "Which Article relates to prohibition of cow slaughter?\nతెలుగు: గోహత్య నిషేధం?",
     "Article 47", "Article 48 (correct)",
     "Article 48A", "Article 49",
     "b",
     "Art.48: 'The State shall endeavour to ORGANISE AGRICULTURE AND ANIMAL HUSBANDRY on MODERN AND SCIENTIFIC LINES, and shall, in particular, take steps for PRESERVING AND IMPROVING THE BREEDS, and PROHIBITING THE SLAUGHTER OF COWS AND CALVES and other milch and draught cattle.' GANDHIAN DPSP. State laws on cow slaughter banning are based on this. Recent contentious — challenged but generally upheld."),

    (2, 2,
     "What does Article 47 direct?\nతెలుగు: Art.47?",
     "Village panchayats",
     "Nutrition, raising living standard, prohibition of intoxicating drinks / పౌష్టికాహారం + మద్యపాన నిషేధం (correct)",
     "Scientific agriculture", "Equal pay",
     "b",
     "Art.47: 'The State shall regard the RAISING OF THE LEVEL OF NUTRITION and the STANDARD OF LIVING of its people and the IMPROVEMENT OF PUBLIC HEALTH as among its primary duties and, in particular, the State shall endeavour to bring about PROHIBITION OF the consumption EXCEPT FOR MEDICINAL PURPOSES of INTOXICATING DRINKS and of DRUGS which are injurious to health.' Has BOTH Socialistic (nutrition/health) AND Gandhian (prohibition) features. Bihar, Gujarat dry states base prohibition on this."),

    (2, 1,
     "What does Article 40 direct?\nతెలుగు: Art.40 ఏం?",
     "Free legal aid",
     "Organize village panchayats with self-government powers / గ్రామ పంచాయితీలు, స్వయంపాలన (correct)",
     "Cottage industries", "Agriculture science",
     "b",
     "Art.40 — GANDHIAN DPSP — already covered above. Operationalised by 73rd Amendment 1992 making Panchayati Raj a constitutional reality across India. Three-tier system: Gram Panchayat, Mandal/Block Panchayat, Zilla Parishad. 11th Schedule lists 29 subjects for panchayat work.",
     "APPSC"),

    (2, 2,
     "Which DPSP groups together represent Gandhian DPSPs?\nతెలుగు: గాంధేయ DPSPs?",
     "38, 39, 41",
     "40, 43, 46, 47, 48 (correct)",
     "44, 45, 50, 51", "37, 41, 42",
     "b",
     "GANDHIAN DPSPs reflecting Gandhi's social-economic vision: (40) Village panchayats; (43) Cottage industries; (46) SC/ST/weaker sections welfare; (47) Prohibition; (48) Cow protection + scientific agriculture. SOCIALISTIC: 38, 39, 39A, 41, 42, 43, 43A, 43B, 47. LIBERAL-INTELLECTUAL: 44, 45, 48, 48A, 49, 50, 51. (Some Articles fit multiple categories.)"),

    (2, 3,
     "Which DPSP first in Gandhian category protects from social injustice and exploitation?\nతెలుగు: అన్యాయం, దోపిడీ నుండి?",
     "Art.40", "Art.43",
     "Art.46 (correct)",
     "Art.47",
     "c",
     "Art.46 specifically protects WEAKER SECTIONS (especially SC/ST) from SOCIAL INJUSTICE and ALL FORMS OF EXPLOITATION. While other Articles (23, 24 — anti-trafficking, anti-child-labour) deal with specific exploitation, Art.46 provides broader social-protection mandate. Foundation for SC/ST POA Act 1989."),

    (2, 3,
     "When and how was 73rd Amendment connected to Article 40?\nతెలుగు: 73వ సవరణ Art.40?",
     "1976",
     "1992 — gave constitutional status to Panchayati Raj per Art.40 vision / 1992 Panchayati Raj (correct)",
     "2002", "1971",
     "b",
     "73rd Constitutional Amendment 1992: Operationalised Art.40's vision by giving CONSTITUTIONAL STATUS to PANCHAYATI RAJ INSTITUTIONS. Added Part IX (Art.243-243O) and 11th Schedule. Mandatory 3-tier system, regular elections, SC/ST/women reservations. Companion 74th Amendment did same for Municipalities (Part IXA, 12th Schedule). Major realisation of a Gandhian DPSP."),

    # ───── Section 3: Liberal-Intellectual DPSPs & Others ─────
    (3, 1,
     "Which Article relates to Uniform Civil Code?\nతెలుగు: UCC Article?",
     "Article 43",
     "Article 44 (correct)",
     "Article 45", "Article 50",
     "b",
     "Art.44: 'The State shall ENDEAVOUR to secure for the citizens a UNIFORM CIVIL CODE throughout the territory of India.' LIBERAL-INTELLECTUAL DPSP. Most controversial — touches on personal laws (Hindu, Muslim, Christian). Implemented partially: Goa has UCC (Portuguese Civil Code legacy); Uttarakhand UCC 2024 first state UCC under Indian Constitution. SC has urged UCC in Sarla Mudgal (1995), Shah Bano (1985).",
     "APPSC"),

    (3, 2,
     "Original Article 45 (pre-86th Amendment) directed?\nతెలుగు: Original Art.45?",
     "Care for children below 6",
     "Free education up to age 10",
     "Free and compulsory education up to 14 years / 14 సం. వరకు (correct)",
     "Free education up to 18",
     "c",
     "ORIGINAL Art.45 (1950): 'The State shall endeavour to provide, within a period of TEN YEARS from the commencement of this Constitution, for FREE AND COMPULSORY EDUCATION for all CHILDREN UNTIL THEY COMPLETE THE AGE OF FOURTEEN YEARS.' Was the most time-bound DPSP! Failed deadline. Eventually 86th Amendment 2002 made it FR (Art.21A) for 6-14, and modified Art.45."),

    (3, 2,
     "Article 48A on environment protection added by?\nతెలుగు: Art.48A?",
     "24th Amdt 1971",
     "42nd Amdt 1976 (correct)",
     "44th Amdt 1978", "86th Amdt 2002",
     "b",
     "Art.48A added by 42nd Amendment 1976: 'The State shall endeavour to PROTECT AND IMPROVE THE ENVIRONMENT and to SAFEGUARD the FORESTS and WILD LIFE of the country.' Companion to Art.51A(g) Fundamental Duty. M.C. Mehta v. UoI cases used Art.48A + Art.21 to develop environmental jurisprudence. Foundation for Environment Protection Act 1986, Forest Conservation Act 1980, Wildlife Protection Act 1972.",
     "APPSC"),

    (3, 1,
     "Which Article directs protection of monuments of national importance?\nతెలుగు: స్మారక చిహ్నాలు?",
     "Art.48",
     "Art.49 (correct)",
     "Art.50", "Art.51",
     "b",
     "Art.49: 'It shall be the OBLIGATION of the State to PROTECT EVERY MONUMENT OR PLACE OR OBJECT of ARTISTIC OR HISTORIC INTEREST, declared by or under law made by Parliament, to be of NATIONAL IMPORTANCE, from spoliation, disfigurement, destruction, removal, disposal or export.' LIBERAL-INTELLECTUAL DPSP. Implementation: Ancient Monuments Act 1958, Antiquities Act 1972. ASI (Archaeological Survey of India) maintenance."),

    (3, 2,
     "Which Article directs separation of judiciary from executive?\nతెలుగు: న్యాయ-కార్యనిర్వాహక వేర్పాటు?",
     "Art.44", "Art.48A",
     "Art.50 (correct)", "Art.51",
     "c",
     "Art.50: 'The State shall take steps to SEPARATE THE JUDICIARY FROM THE EXECUTIVE in the public services of the State.' LIBERAL-INTELLECTUAL DPSP — judicial independence. Implementation: Criminal Procedure Code 1973 separated criminal courts (judicial magistrates under judiciary) from district administration (executive magistrates). Earlier district collectors performed both functions."),

    (3, 1,
     "Which Article relates to promotion of international peace?\nతెలుగు: అంతర్జాతీయ శాంతి?",
     "Art.49", "Art.50",
     "Art.51 (correct)",
     "Art.38",
     "c",
     "Art.51: 'The State shall endeavour to (a) PROMOTE INTERNATIONAL PEACE AND SECURITY; (b) MAINTAIN JUST AND HONOURABLE RELATIONS between nations; (c) FOSTER RESPECT FOR INTERNATIONAL LAW and treaty obligations; (d) ENCOURAGE SETTLEMENT OF INTERNATIONAL DISPUTES BY ARBITRATION.' LIBERAL-INTELLECTUAL DPSP. India's NAM, peacekeeping, treaty observance reflect this.",
     "APPSC"),

    (3, 2,
     "Which is NOT a Liberal-Intellectual DPSP?\nతెలుగు: Liberal-Intellectual కానిది?",
     "Art.44 — UCC", "Art.50 — Judiciary-Executive separation",
     "Art.46 — SC/ST educational interests / Art.46 (correct)",
     "Art.48A — Environment",
     "c",
     "Art.46 (educational/economic interests of SC/ST and weaker sections) is GANDHIAN DPSP. LIBERAL-INTELLECTUAL DPSPs: Art.44 (UCC), Art.45 (now early childhood care), Art.48 (scientific agriculture — also has Gandhian element of cow slaughter ban), Art.48A (environment), Art.49 (monuments), Art.50 (judiciary), Art.51 (international peace)."),

    (3, 3,
     "Article 41 directs right to what?\nతెలుగు: Art.41 ఏ హక్కులు?",
     "Education only",
     "Work, education, and public assistance in unemployment/old age/sickness / పని, విద్య, పబ్లిక్ సహాయం (correct)",
     "Work and maternity", "Work and living wage",
     "b",
     "Art.41: Within limits of economic capacity, State shall provide right to (1) WORK, (2) EDUCATION, (3) PUBLIC ASSISTANCE in cases of UNEMPLOYMENT, OLD AGE, SICKNESS, DISABLEMENT and undeserved want. Has elements of social security. Implementation: MGNREGA (right to work), various pension schemes (NSAP), insurance schemes."),

    (3, 2,
     "Article 45 today (post-86th Amendment) directs?\nతెలుగు: Art.45 ప్రస్తుతం?",
     "Free education up to 14",
     "Early childhood care and education for children below 6 / 6 సం. లోపు పిల్లలకు (correct)",
     "Education till 20", "Vocational education",
     "b",
     "86th Amendment 2002 SUBSTITUTED Art.45: 'The State shall endeavour to PROVIDE EARLY CHILDHOOD CARE AND EDUCATION for all CHILDREN UNTIL THEY COMPLETE THE AGE OF SIX YEARS.' Original Art.45 (6-14 free education) became FR Art.21A. Now: pre-primary care covered by Art.45, primary by Art.21A. Implementation: Anganwadis under ICDS, NEP 2020 vision.",
     "APPSC"),

    (3, 2,
     "Which Article directs scientific agriculture?\nతెలుగు: శాస్త్రీయ వ్యవసాయం?",
     "Art.46", "Art.47",
     "Art.48 (correct)", "Art.49",
     "c",
     "Art.48 directs: (1) ORGANIZE AGRICULTURE AND ANIMAL HUSBANDRY on MODERN SCIENTIFIC LINES; (2) PRESERVE AND IMPROVE BREEDS; (3) PROHIBIT slaughter of cows, calves, milch and draught cattle. Combines LIBERAL-INTELLECTUAL (scientific agriculture) and GANDHIAN (cow protection) elements. Foundation for ICAR research, Operation Flood, animal husbandry programs."),

    (3, 3,
     "Which DPSP relates to obtaining women's just maternity benefits?\nతెలుగు: మాతృత్వ సహాయం?",
     "Art.39A",
     "Art.42 (correct)",
     "Art.43A", "Art.46",
     "b",
     "Art.42: 'just and humane conditions of work and for MATERNITY RELIEF.' Implementation: MATERNITY BENEFIT ACT 1961 (amended 2017 — paid maternity leave extended from 12 to 26 WEEKS for first 2 children, plus 12 weeks for adoption/surrogacy). One of the most progressive maternity laws globally. ESI Act for organised sector also."),

    (3, 4,
     "After 86th Amendment 2002, education-related DPSP/FR structure is?\nతెలుగు: విద్యా structure?",
     "All in DPSP",
     "Pre-6 = Art.45 DPSP; 6-14 = Art.21A FR; Higher = Art.41 (general right to education) / 6 ముందు DPSP, 6-14 FR (correct)",
     "All in FR", "Only state law",
     "b",
     "86th Amendment 2002 reorganised education rights: (1) BEFORE 6 years: Art.45 DPSP (Early childhood care). (2) AGES 6-14: Art.21A FUNDAMENTAL RIGHT (Right to Education) — implemented by RTE Act 2009. (3) HIGHER: General Art.41 DPSP and Art.21 (read-in) cover broader education. Also added Art.51A(k) Fundamental Duty for parents to provide education."),

    (3, 1,
     "Where can a citizen of India enforce DPSPs?\nతెలుగు: DPSPs ఎక్కడ enforce?",
     "Supreme Court via Art.32",
     "Cannot enforce — non-justiciable / Enforce చేయలేదు (correct)",
     "High Court via Art.226", "Lower courts",
     "b",
     "Per Art.37, DPSPs are NON-JUSTICIABLE — citizens CANNOT directly enforce them in any court. However, courts have used DPSPs as INTERPRETIVE TOOLS — reading them with FRs to expand meaning (e.g., Art.21 + Art.39A → right to free legal aid; Art.21 + Art.41 → right to livelihood; Art.21 + Art.48A → right to clean environment). Indirect enforcement through harmonious construction."),

    (3, 2,
     "Article 39A directs equal justice and?\nతెలుగు: Art.39A?",
     "Equal pay", "Equal vote",
     "Free legal aid / ఉచిత న్యాయ సహాయం (correct)",
     "Equal property",
     "c",
     "Art.39A (added 1976): 'EQUAL JUSTICE and FREE LEGAL AID' — ensure operation of legal system promotes justice on basis of equal opportunity, and provide free legal aid by suitable legislation/schemes to ensure no citizen denied justice due to economic disabilities. Implementation: Legal Services Authorities Act 1987 → NALSA, SLSAs, DLSAs. Read with Art.21 (Hussainara Khatoon 1979) → free legal aid is FR."),

    # ───── Section 4: Cases & Conflicts (FR-DPSP) ─────
    (4, 3,
     "Champakam Dorairajan case (1951) was about?\nతెలుగు: Champakam 1951?",
     "Conflict between Art.19 and DPSP",
     "Religion-based reservations vs Art.29(2) / Communal GO vs Art.29(2) (correct)",
     "Property right abolition", "Art.32 scope",
     "b",
     "STATE OF MADRAS v. CHAMPAKAM DORAIRAJAN (1951): Madras 'Communal GO' allocated college seats by religion/caste. SC struck down as violating Art.29(2) (no admission denial on grounds of religion/race/caste/language). HELD: FR PREVAILS over DPSP in conflict. Was the FIRST FR-DPSP conflict case. Triggered 1st Constitutional Amendment 1951 adding Art.15(4).",
     "APPSC"),

    (4, 3,
     "1st Constitutional Amendment 1951 added which clause?\nతెలుగు: 1వ సవరణ?",
     "Art.14(3)",
     "Art.15(4) (correct)",
     "Art.16(4)", "Art.19(2)",
     "b",
     "1st Constitutional Amendment 1951 (in response to Champakam): Added Art.15(4) permitting State to make special provisions for advancement of SOCIALLY AND EDUCATIONALLY BACKWARD CLASSES (SEBC) or SC/ST. Also added Art.31A, 31B, 9th Schedule (for land reform laws). Restricted scope of Art.19(1)(a) by adding 'public order' to Art.19(2). Crucial early amendment."),

    (4, 3,
     "Golak Nath case (1967) ruled?\nతెలుగు: Golak Nath 1967?",
     "Parliament can amend any right",
     "Parliament cannot amend Fundamental Rights / Parliament FR సవరించలేదు (correct)",
     "DPSPs prevail over FRs", "DPSPs are justiciable",
     "b",
     "I.C. GOLAK NATH v. STATE OF PUNJAB (1967): 11-judge SC bench (6:5 majority) held Parliament has NO POWER TO AMEND FUNDAMENTAL RIGHTS (Part III) — even via constitutional amendment. Used 'doctrine of prospective overruling' to save earlier amendments. Restricted amending power. OVERRULED by 24th Amendment 1971 (and subsequently by Kesavananda Bharati 1973 with basic-structure doctrine)."),

    (4, 3,
     "What did 24th Constitutional Amendment 1971 do?\nతెలుగు: 24వ సవరణ?",
     "Added Art.31C",
     "Overruled Golak Nath; Parliament can amend any part of Constitution / Golak Nath overrule (correct)",
     "Added 9th Schedule", "Gave DPSPs precedence",
     "b",
     "24th Amendment 1971: Amended Art.13 and Art.368 to overrule Golak Nath. Inserted Art.13(4): 'Nothing in this article shall apply to any amendment of this Constitution made under Article 368.' And Art.368(3): Parliament's amending power explicitly extends to 'any provision of this Constitution.' Restored Parliament's full amending power — but Kesavananda 1973 added Basic Structure limit."),

    (4, 3,
     "Article 31C (added by 25th Amendment 1971) provided?\nతెలుగు: Art.31C?",
     "9th Schedule protection",
     "All DPSPs immune from Art.14/19 challenge",
     "Laws implementing Art.39(b) and 39(c) immune from Art.14/19 challenge / Art.39(b), 39(c) रक्षण (correct)",
     "FRs prevail over DPSPs",
     "c",
     "Art.31C [25th Amendment 1971]: 'Notwithstanding anything in Art.13, no law giving effect to the policy of the State towards securing the principles specified in CLAUSES (b) AND (c) OF ARTICLE 39 shall be deemed to be void on the ground that it is inconsistent with, or takes away or abridges any of the rights conferred by Art.14, 19...' Originally also said no court could question — Kesavananda 1973 struck down that part. Limited to Art.39(b) and (c)."),

    (4, 3,
     "How did 42nd Amendment 1976 extend Article 31C?\nతెలుగు: 42వ సవరణ Art.31C?",
     "Only from Art.14",
     "Extended Art.31C protection to laws implementing ALL DPSPs / అన్ని DPSPs (correct)",
     "Only from Art.21", "Whole Part IV",
     "b",
     "42nd Amendment 1976 EXPANDED Art.31C: Replaced 'principles specified in clauses (b) and (c) of article 39' with 'ALL or ANY of the principles laid down in PART IV.' This meant ANY law implementing ANY DPSP was protected from Art.14/19 challenge. Excessive shielding! STRUCK DOWN in Minerva Mills (1980) — only Art.39(b)/(c) protection survives."),

    (4, 3,
     "Minerva Mills case (1980) ruled?\nతెలుగు: Minerva Mills 1980?",
     "42nd Amendment fully unconstitutional",
     "42nd Amendment's extension of Art.31C to all DPSPs is unconstitutional / 42వ Art.31C విస్తరణ రాజ్యాంగ విరుద్ధం (correct)",
     "DPSPs prevail over FRs", "No FR-DPSP conflict",
     "b",
     "MINERVA MILLS v. UoI (1980): SC struck down (a) 42nd Am's extension of Art.31C to ALL DPSPs as VIOLATING BASIC STRUCTURE — restored Art.31C to only Art.39(b)/(c). (b) Sections of 42nd Am that gave Parliament unlimited amending power. KEY HOLDING: HARMONY between FR and DPSP IS PART OF BASIC STRUCTURE — neither can be made to dominate the other. Watershed case.",
     "APPSC"),

    (4, 3,
     "Kesavananda Bharati (1973) clarified FR-DPSP relation as?\nతెలుగు: Kesavananda?",
     "DPSPs prevail",
     "FRs prevail",
     "Both part of Basic Structure; Basic Structure cannot be destroyed / రెండూ Basic Structure (correct)",
     "Never any conflict",
     "c",
     "KESAVANANDA BHARATI v. STATE OF KERALA (1973): 13-judge SC bench (7:6 majority). PROPOUNDED 'BASIC STRUCTURE DOCTRINE' — Parliament can amend any part of Constitution INCLUDING FRs (overruling Golak Nath) BUT cannot DESTROY/ALTER its BASIC STRUCTURE. Both FRs and DPSPs are envisioned as integral; specific DPSPs (Art.39(b),(c)) and FR balance form basic features.",
     "APPSC"),

    (4, 2,
     "I.R. Coelho case (2007) decided?\nతెలుగు: Coelho 9th Schedule?",
     "All 9th Schedule laws immune",
     "Laws added to 9th Schedule after 24 April 1973 subject to JR / 1973 తర్వాత JR (correct)",
     "9th Schedule unconstitutional", "Only DPSPs",
     "b",
     "I.R. COELHO v. State of Tamil Nadu (2007): 9-judge SC bench. Laws added to 9th SCHEDULE AFTER 24 APRIL 1973 (Kesavananda judgment date) are subject to JUDICIAL REVIEW for VIOLATION OF BASIC STRUCTURE — particularly Part III FRs forming basic structure. Laws added BEFORE that date remain immune (subject to certain limits). Major curb on misuse of 9th Schedule."),

    (4, 3,
     "Unnikrishnan case (1993) elevated which right from DPSP?\nతెలుగు: Unnikrishnan ఏ హక్కు?",
     "Right to work",
     "Right to education / విద్యా హక్కు (correct)",
     "Right to health", "Clean environment",
     "b",
     "UNNIKRISHNAN J.P. v. STATE OF AP (1993): SC HELD that RIGHT TO EDUCATION FLOWS FROM ART.21 (Right to Life). Used DPSP Art.45 read with Art.21 to make education a FR. Subsequently reaffirmed in Mohini Jain (1992). Eventually formalised by 86th Amendment 2002 as Art.21A. Classic example of court-driven elevation of DPSP to FR through Art.21 reading.",
     "APPSC"),

    (4, 3,
     "Which Articles 31A, 31B, 31C — when added?\nతెలుగు: 31A, 31B, 31C?",
     "All by 1st Amendment",
     "31A & 31B by 1st Am (1951); 31C by 25th Am (1971) / 31A, 31B = 1st; 31C = 25th (correct)",
     "Reverse", "All by 42nd Am",
     "b",
     "Art.31A & Art.31B added by 1st Constitutional Amendment 1951 (Champakam aftermath; protect land reform laws). Art.31A: saves laws on land reforms, estate acquisition from Art.14/19/31 challenge. Art.31B: 9th Schedule protection. Art.31C added by 25th Constitutional Amendment 1971: protect laws implementing Art.39(b)/(c) from Art.14/19 challenge. (Original Art.31 — Right to Property — removed by 44th Am 1978.)"),

    (4, 2,
     "Art.31A saves what?\nతెలుగు: Art.31A?",
     "Land reform laws from Art.14/19 challenge / భూ సంస్కరణ చట్టాలు (correct)",
     "9th Schedule laws", "All DPSP laws", "Art.32 challenge",
     "a",
     "Art.31A: Saves FIVE categories of laws from Art.14/19 challenges: (1) ACQUISITION OF ESTATES; (2) Taking over management of property by State; (3) Amalgamation of corporations; (4) Modification of rights of corporation members; (5) Modification/extinguishment of mining leases. Aimed at zamindari abolition and land reforms. Bihar's first land reform law. Different from 9th Schedule (Art.31B)."),

    # ───── Section 5: 9th Schedule, Art.31A, 31B, 31C ─────
    (5, 2,
     "9th Schedule was added by which Amendment?\nతెలుగు: 9th Schedule?",
     "42nd Amendment 1976",
     "1st Amendment 1951 (correct)",
     "44th Amendment 1978", "25th Amendment 1971",
     "b",
     "1st Constitutional Amendment 1951 added: (a) Article 31B; (b) NINTH SCHEDULE — list of laws immunised from Art.13 challenge. Initially 13 laws (Bihar Land Reforms etc.). Currently 280+ laws — includes Tamil Nadu reservation 69%, etc. Originally allowed without limit, but I.R. Coelho 2007 made post-1973 inclusions reviewable for basic structure violation."),

    (5, 2,
     "Article 31B saves what?\nతెలుగు: Art.31B?",
     "Land reform from Art.14/19",
     "Laws listed in 9th Schedule from FR challenge / 9th Schedule చట్టాలు (correct)",
     "All DPSP laws", "Art.32 challenge",
     "b",
     "Art.31B: 'Without prejudice to the generality of the provisions contained in article 31A, none of the Acts and Regulations specified in the Ninth Schedule... shall be deemed to be VOID or ever to have become void on the ground that such Act, Regulation or provision is INCONSISTENT WITH, OR TAKES AWAY OR ABRIDGES any of the rights conferred by any provisions of this Part [III]...' Wider scope than Art.31A. Subject to I.R. Coelho post-1973 review."),

    (5, 3,
     "Correct grouping of 31A, 31B, 31C?\nతెలుగు: 31A, 31B, 31C అమెండ్‌మెంట్?",
     "All by 1st Amendment",
     "31A & 31B by 1st (1951); 31C by 25th (1971) (correct)",
     "31A & 31C by 1st; 31B by 25th", "All by 42nd",
     "b",
     "Standard exam answer: Art.31A & Art.31B → 1st Amendment 1951 (post-Champakam); Art.31C → 25th Amendment 1971 (post-Bank Nationalisation cases). All three are 'savings' Articles for laws implementing socialistic policies — protecting from FR challenges. Art.31A (5 specific land categories), Art.31B (9th Schedule list), Art.31C (laws for Art.39(b)/(c))."),

    (5, 2,
     "What did Art.31C originally protect (before 42nd extension)?\nతెలుగు: Art.31C original?",
     "All DPSPs",
     "Laws implementing Art.39(b) and Art.39(c) only / Art.39(b), 39(c) మాత్రమే (correct)",
     "Only land reforms", "All Part III",
     "b",
     "Original Art.31C [25th Am 1971]: Saves laws implementing Art.39(b) (material resources distribution) AND Art.39(c) (prevention of wealth concentration) from challenge under Art.14, 19, 31. Original 25th Am had clause: 'no law containing a declaration that it is for giving effect to such policy shall be called in question in any court' — this part STRUCK DOWN by Kesavananda 1973. 42nd Am extended to ALL DPSPs (struck down in Minerva Mills 1980)."),

    (5, 1,
     "First law placed in 9th Schedule was?\nతెలుగు: మొదటి 9th Schedule చట్టం?",
     "Mineral Acts",
     "Land reform laws like Bihar Land Reforms Act / భూ సంస్కరణ (correct)",
     "Banking laws", "Education laws",
     "b",
     "Initial 9th Schedule (1951) had 13 LAND REFORM laws including: Bihar Land Reforms Act 1950, UP Zamindari Abolition Acts, Madras Estates Acts, etc. Purpose: prevent court challenges (some had been struck down on Art.31 grounds). Now 280+ laws including Tamil Nadu Reservation Act (extends 50% to 69%). Some recent additions controversial post-Coelho 2007."),

    # ───── Section 6: FR-DPSP Comparison ─────
    (6, 2,
     "Who described FRs and DPSPs as 'conscience of the Constitution'?\nతెలుగు: 'Conscience' ఎవరు?",
     "Ambedkar",
     "Granville Austin (correct)",
     "Nehru", "K.M. Munshi",
     "b",
     "GRANVILLE AUSTIN (American political scientist, scholar of Indian Constitution): In 'The Indian Constitution: Cornerstone of a Nation' (1966), described FRs and DPSPs together as the 'CONSCIENCE OF THE CONSTITUTION' and the 'CORE OF THE COMMITMENT TO THE SOCIAL REVOLUTION.' Both seen as integral parts achieving political + socio-economic democracy. Influential characterisation."),

    (6, 1,
     "Who described DPSPs as 'pious wishes'?\nతెలుగు: 'Pious wishes' ఎవరు?",
     "T.T. Krishnamachari (correct)",
     "Ambedkar", "K.T. Shah", "Nazirudin Ahmed",
     "a",
     "T.T. KRISHNAMACHARI in Constituent Assembly described DPSPs as 'PIOUS WISHES' — sceptical view that without judicial enforceability, they'd remain merely aspirational. Other critical descriptions: K.T. Shah ('cheque payable at bank's convenience'); Naziruddin Ahmad ('pious superfluities'); K.C. Wheare ('manifesto of aims'). DPSP-supporters argued non-justiciability necessary given resource constraints."),

    (6, 2,
     "Key difference between FRs and DPSPs?\nతెలుగు: ముఖ్య తేడా?",
     "DPSPs justiciable",
     "FRs = negative obligations; DPSPs = positive obligations / FR Negative, DPSP Positive (correct)",
     "FRs on State; DPSPs on citizens", "FRs in Concurrent List",
     "b",
     "MANY DIFFERENCES: (1) FRs justiciable, DPSPs not. (2) FRs are NEGATIVE OBLIGATIONS on State (don't violate); DPSPs are POSITIVE OBLIGATIONS (must work towards). (3) FRs aim at POLITICAL democracy; DPSPs at SOCIO-ECONOMIC democracy. (4) FRs grant RIGHTS to individuals; DPSPs are DIRECTIVES to State. (5) FRs derive from US Bill of Rights; DPSPs from Irish Constitution."),

    (6, 2,
     "Ambedkar's vision for DPSPs?\nతెలుగు: Ambedkar దృష్టి?",
     "Pious wishes",
     "Transform political democracy into socio-economic democracy / రాజకీయ ప్రజాస్వామ్యాన్ని socio-economic గా మార్చడం (correct)",
     "Western tradition", "Mere moral obligations",
     "b",
     "AMBEDKAR's vision (CA debates): 'POLITICAL DEMOCRACY cannot last unless there lies at the base of it SOCIAL DEMOCRACY... If we adopt the Constitution and lay down equal political rights without equal economic rights, the people having the second class will rise to power and topple the structure.' DPSPs were the means to achieve socio-economic democracy. Hence 'fundamental in governance' even if non-justiciable."),

    (6, 3,
     "Courts' approach to FR-DPSP conflicts?\nతెలుగు: సమన్వయ approach?",
     "DPSPs always prevail",
     "FRs always prevail",
     "Harmonious construction — give practical meaning to both / Harmonious Construction (correct)",
     "Parliament resolution",
     "c",
     "Post-Champakam (1951) → 'FR prevails'. Then 1st, 25th, 42nd Amendments tried to give DPSP precedence. Kesavananda (1973) and Minerva Mills (1980) settled on HARMONIOUS CONSTRUCTION — give practical meaning to BOTH without destroying either. Both are PART OF BASIC STRUCTURE. Court reads them together creatively (Art.21 expansion). Balance is itself a basic feature — neither dominates."),

    (6, 1,
     "Why are DPSPs 'fundamental in governance' despite being non-justiciable?\nతెలుగు: ఎందుకు fundamental?",
     "Higher than FRs",
     "Guidelines for law-making; State must apply them while making laws / చట్టాలకు మార్గదర్శకాలు (correct)",
     "President-enforceable", "SC-enforceable",
     "b",
     "Art.37 SAYS DPSPs are 'NEVERTHELESS FUNDAMENTAL IN THE GOVERNANCE of the country and IT SHALL BE THE DUTY OF THE STATE to apply these principles in MAKING LAWS.' So while courts can't enforce them, the State (legislature, executive) MUST consider them when making laws and policies. They are political/moral commitments. Hence 'Directive Principles of STATE POLICY' — directing State's policies."),

    (6, 1,
     "Who pioneered DPSPs concept globally — borrowed from where?\nతెలుగు: DPSPs ఎక్కడ నుండి?",
     "USA Bill of Rights",
     "Irish Constitution 1937 (drew from Spanish Constitution) / Ireland 1937 (correct)",
     "British Common Law", "Soviet Constitution",
     "b",
     "DPSPs borrowed from IRISH (Eire) Constitution 1937, which had drawn the concept from SPANISH Constitution. Several democracies (Pakistan, Ghana, Bangladesh, Nepal) have adopted similar 'directive principles' inspired by Indian model. UN Universal Declaration of Human Rights 1948 has similar 'aspirational' rights. DPSPs were innovative — combined justiciable and non-justiciable rights in single constitution."),

    # ───── Section 7: PYQ Comprehensive ─────
    (7, 3,
     "Which is NOT a Socialistic DPSP?\nతెలుగు: Socialistic కానిది?",
     "Art.39A — Free legal aid", "Art.41 — Right to work",
     "Art.44 — Uniform Civil Code (correct)",
     "Art.43A — Workers' management",
     "c",
     "Art.44 (UCC) is LIBERAL-INTELLECTUAL DPSP. SOCIALISTIC: 38, 39, 39A, 41, 42, 43, 43A, 43B, 47. GANDHIAN: 40, 43, 46, 47, 48. LIBERAL-INTELLECTUAL: 44, 45, 48, 48A, 49, 50, 51. (Some Articles like 43, 47 fit multiple). Standard categorisation: Lakshmikanth tripartite scheme."),

    (7, 3,
     "Which DPSP classification is correct?\nతెలుగు: సరైన classification?",
     "Art.40 — Socialistic", "Art.50 — Gandhian",
     "Art.48A — Liberal-Intellectual (correct)",
     "Art.47 — Liberal-Intellectual",
     "c",
     "Art.48A (Environment protection) is LIBERAL-INTELLECTUAL. CORRECT pairings: Art.40 (panchayats) — Gandhian. Art.50 (judiciary-executive separation) — Liberal-Intellectual. Art.47 (nutrition + prohibition) — has Socialistic AND Gandhian features."),

    (7, 3,
     "Which is NOT a DPSP?\nతెలుగు: DPSP కానిది?",
     "Uniform Civil Code", "Separation of judiciary",
     "Prohibition of Untouchability / అంటరానితనం (correct)",
     "International peace",
     "c",
     "PROHIBITION OF UNTOUCHABILITY is a FUNDAMENTAL RIGHT (Art.17), NOT a DPSP. UCC (Art.44), separation of judiciary-executive (Art.50), international peace (Art.51) are DPSPs. Watch out for FR-DPSP confusion in MCQs — Art.17 is firmly in Part III as FR (Right to Equality)."),

    (7, 3,
     "Which Amendment introduced Art.31C protecting DPSP-implementing laws?\nతెలుగు: Art.31C ఏ సవరణ?",
     "24th Amdt 1971",
     "25th Amdt 1971 (correct)",
     "42nd Amdt 1976", "44th Amdt 1978",
     "b",
     "25th Constitutional Amendment 1971 added Article 31C protecting laws implementing Art.39(b)/(c) from Art.14/19 challenges. Companion to: 24th Am 1971 (overruled Golak Nath); 26th Am 1971 (abolished privy purses). Kesavananda (1973) struck down the 'no court can question' part of original Art.31C. 42nd Am 1976 expanded to all DPSPs — struck down by Minerva Mills 1980.",
     "APPSC"),

    (7, 2,
     "Right to Education Act 2009 implements which Article?\nతెలుగు: RTE Act?",
     "Right to Information Act 2005",
     "Right of Children to Free and Compulsory Education Act 2009 — Art.21A + Art.45 / RTE = Art.21A (correct)",
     "POCSO Act 2012", "Juvenile Justice Act 2015",
     "b",
     "Right of Children to Free and Compulsory Education Act 2009 (RTE Act) — implements Art.21A (Fundamental Right since 86th Am 2002) and Art.45 (DPSP). Free and compulsory education for children aged 6-14. Came into force 1 April 2010. Mandates 25% reservation for disadvantaged in private schools. Norms for teacher-student ratio, infrastructure.",
     "APPSC"),

    (7, 3,
     "Art.39A, Art.43A, Art.48A added by which Amendment?\nతెలుగు: 39A, 43A, 48A?",
     "1st Amdt 1951", "25th Amdt 1971",
     "42nd Amdt 1976 (correct)",
     "44th Amdt 1978",
     "c",
     "42nd Constitutional Amendment 1976 (Indira Gandhi's Emergency-era amendment) added 3 new DPSPs: (1) Art.39A — Equal justice & free legal aid; (2) Art.43A — Workers' participation in management; (3) Art.48A — Environment protection. Also added Art.51A (Fundamental Duties) — Part IVA. Made many other changes. Many provisions reversed by 44th Am 1978.",
     "APPSC"),

    (7, 2,
     "Part IV (DPSPs) spans which Articles?\nతెలుగు: Part IV ఏ Articles?",
     "Art.12 to Art.35",
     "Art.36 to Art.51 (correct)",
     "Art.52 to Art.78", "Art.243 to Art.243ZT",
     "b",
     "DPSPs in Part IV: Art.36 to Art.51 — 16 articles (with sub-clauses making more). Art.36 = State definition. Art.37 = nature (non-justiciable, fundamental). Art.38-51 = specific DPSPs. Subsequent amendments (1st, 25th, 42nd, 44th, 86th, 97th) modified or added Articles. Part IVA = Fundamental Duties (Art.51A) added by 42nd Am."),

    (7, 2,
     "Art.39A implemented through which Act?\nతెలుగు: Art.39A అమలు?",
     "Legal Services Authorities Act 1987 (correct)",
     "Advocates Act 1961", "CrPC 1973", "Consumer Protection Act 1986",
     "a",
     "LEGAL SERVICES AUTHORITIES ACT 1987 implements Art.39A (Equal Justice & Free Legal Aid). Created NALSA (National Legal Services Authority) at apex; SLSAs (state); DLSAs (district). Provides free legal aid to: SC/ST, women, children, disabled, victims, persons in custody, persons with annual income below threshold. Also runs Lok Adalats. Hussainara Khatoon (1979) read Art.39A with Art.21 making free legal aid an FR for indigent accused.",
     "APPSC"),
]



import json as _json


def _seed_polity_ch9_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    import json as _j
    ph = '%s' if use_postgres else '?'
    _sections = [
    {"title": "9.1 DPSP పరిచయం — Art 36-37", "sub": "DPSP Basics · Part IV · Art 36 · Art 37 · Non-Justiciable", "audio": ""},
    {"title": "9.2 సోషలిస్ట్ DPSP లు", "sub": "Socialistic DPSPs · Art 38-39 · Equal Pay · Maternity", "audio": ""},
    {"title": "9.3 గాంధేయ DPSP లు", "sub": "Gandhian DPSPs · Art 40-48 · Panchayats · Cottage Industries", "audio": ""},
    {"title": "9.4 ఉదారవాద DPSP లు", "sub": "Liberal-Intellectual DPSPs · Art 44-51 · UCC · International Peace", "audio": ""},
    {"title": "9.5 FR vs DPSP వివాదం మరియు కేసులు", "sub": "FR-DPSP Conflict · Golaknath · Kesavananda · Minerva Mills", "audio": ""},
    {"title": "9.6 రక్షిత నిబంధనలు — Art 31A-31C", "sub": "Art 31A · Art 31B · Art 31C · 9th Schedule · Saving Clauses", "audio": ""},
    {"title": "9.7 FR vs DPSP పోలిక", "sub": "Comparison · Justiciable vs Non-Justiciable · Granville Austin", "audio": ""},
    {"title": "9.8 కఠిన ప్రశ్నలు", "sub": "Difficult MCQs · APPSC Style · Art 38(2) · Instruments of Instructions", "audio": ""}
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
        (9, 'Indian_Polity'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True,
                'message': 'Polity Ch9 notes already seeded.'}
    if row and force:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (9, 'Indian_Polity'))
    if use_postgres:
        conn.commit()

    db_exec_fn(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'Indian_Polity', '', 9,
         'రాజ్య నిర్దేశక సూత్రాలు',
         'Directive Principles of State Policy',
         'Ch.9',
         _j.dumps(_sections, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'Polity Ch9 notes seeded!'}


def _seed_polity_ch9_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
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
        (9, 'Indian_Polity'))
    row = cur.fetchone()
    if not row:
        _seed_polity_ch9_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)
        cur = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (9, 'Indian_Polity'))
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
    for mcq in POLITY_CH9_MCQS:
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

    total = len(POLITY_CH9_MCQS)
    return {
        'success': True,
        'message': f'Polity Ch9 MCQs seeded! Total: {total}',
        'inserted': total,
        'easy': easy, 'medium': medium, 'hard': hard,
        'toughest': toughest, 'pyq': pyq
    }
