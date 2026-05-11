# seed_polity_ch8.py
# Chapter 8: Fundamental Rights (Part II)
# (ప్రాథమిక హక్కులు - రెండవ భాగం)
# Standard : APPSC Group 2 | Source: Lakshmikanth Indian Polity
# Total MCQs: 46 | PYQs: 7
# Format   : Bilingual (Telugu + English)
# Difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
# PYQ: 10th element (index 9) = 'APPSC' or 'UPSC'
# ─────────────────────────────────────────────

import json as _json

POLITY_CH8_MCQS = [
    # ───── Section 0: Article 23 — Forced Labour ─────
    (0, 1,
     "What does Article 23 prohibit?\nతెలుగు: Art.23 ఏం నిషేధిస్తుంది?",
     "Child labour only / పిల్లల చాకిరీ మాత్రమే",
     "Human trafficking and forced labour (begar) / మానవ అక్రమ రవాణా + Begar (correct)",
     "Religious discrimination / మత వివక్ష",
     "Untouchability / అంటరానితనం",
     "b",
     "Article 23: Prohibits (a) TRAFFIC IN HUMAN BEINGS, and (b) BEGAR and other similar forms of FORCED LABOUR. Available to ALL persons (citizens + non-citizens). UNIQUE FR — enforceable against private individuals too (not just against State). Implementation: Bonded Labour Act 1976, Immoral Traffic (Prevention) Act 1956."),

    (0, 1,
     "When was Bonded Labour System Abolition Act enacted?\nతెలుగు: BLSA Act?",
     "1956", "1966", "1976 (correct)", "1986",
     "c",
     "Bonded Labour System (Abolition) Act 1976 — abolished BONDED/wage slavery. Enacted to implement Art.23. Released bonded labourers freed from all obligations and any debts cancelled. Also: Immoral Traffic (Prevention) Act 1956 (related to Art.23) for trafficking."),

    (0, 2,
     "Can the State impose compulsory service under Article 23?\nతెలుగు: State compulsory service?",
     "Can impose for any reason",
     "Yes for public purposes; but no discrimination on religion/race/caste/class / Public purposes కోసం, Religion/Race/Caste/Class వివక్ష లేకుండా (correct)",
     "Cannot impose at all",
     "Only women exempted",
     "b",
     "Art.23(2): State CAN impose COMPULSORY SERVICE for PUBLIC PURPOSES (e.g., national service, military service, anti-flood/famine work) — BUT shall not discriminate on grounds of religion, race, caste or class only. Conscription is constitutionally permissible. India hasn't operationalised compulsory military service."),

    (0, 2,
     "Against whom is Article 23 enforceable?\nతెలుగు: Art.23 ఎవరిపై?",
     "Only Indian citizens",
     "Only against the State",
     "All persons (citizens + non-citizens); enforceable against private individuals too / అందరిపై + Private individuals పైనా (correct)",
     "Only minorities",
     "c",
     "Art.23 is UNIQUE among FRs — enforceable against the STATE (Art.12 def) AND PRIVATE INDIVIDUALS. Most FRs operate only against State. Available to BOTH citizens and non-citizens. Reason: trafficking and forced labour usually occur in private spheres — needs broader enforcement."),

    (0, 3,
     "What did SC hold in PUDR v. UoI 1982?\nతెలుగు: PUDR Case 1982?",
     "Art.23 only physical coercion",
     "Non-payment of minimum wages = forced labour; economic compulsion suffices / Minimum wages చెల్లించకపోతే forced labour (correct)",
     "Art.23 doesn't apply to private individuals",
     "Only Govt employees",
     "b",
     "PEOPLE'S UNION FOR DEMOCRATIC RIGHTS v. UoI (1982) [Asiad Workers Case]: SC EXPANDED Art.23 — held NON-PAYMENT OF MINIMUM WAGES to a worker = FORCED LABOUR under Art.23. Physical force NOT required; ECONOMIC COMPULSION (working under economic necessity for less than minimum wage) is sufficient. Justice Bhagwati, social activism era."),

    (0, 4,
     "Assertion-Reason: Art.23 is enforceable against private individuals; most FRs only against State?\nతెలుగు: Assertion-Reason?",
     "Both correct, R explains A (correct)",
     "Both correct, R doesn't explain A",
     "A correct, R wrong",
     "A wrong, R correct",
     "a",
     "BOTH CORRECT and R explains A. Art.23 is UNIQUE — applies horizontally (against private persons) because trafficking and forced labour are typically perpetrated by private individuals/employers. Most FRs apply only against 'State' (Art.12 definition). Other horizontally-operating FRs: Art.15(2), Art.17, Art.24."),

    (0, 2,
     "Which Article prohibits begar and other forms of forced labour? [APPSC]\nతెలుగు: Begar నిషేధం Article?",
     "Article 22", "Article 23 (correct)", "Article 24", "Article 25",
     "b",
     "Article 23: Traffic in human beings and begar. APPSC frequently asks this. 'Begar' = Hindi/Persian term for unpaid forced labour (historically demanded by zamindars from peasants). Bonded Labour System Abolition Act 1976 is implementing legislation. Penalty under various laws.",
     "APPSC"),

    # ───── Section 1: Article 24 — Child Labour ─────
    (1, 1,
     "Below what age does Article 24 prohibit factory/mine employment?\nతెలుగు: Art.24 వయసు?",
     "Below 12", "Below 14 (correct)", "Below 16", "Below 18",
     "b",
     "Art.24: No child BELOW 14 YEARS shall be employed in any FACTORY, MINE or any HAZARDOUS EMPLOYMENT. Implemented through Child Labour (Prohibition & Regulation) Act 1986 [amended 2016]. Applies to ALL employers — State and private. Hazardous list specified by Ministry of Labour."),

    (1, 2,
     "Under 2016 Child Labour Amendment, what is prohibited for ages 14-18?\nతెలుగు: 2016 సవరణ 14-18?",
     "All work",
     "Hazardous employment only / Hazardous employment మాత్రమే (correct)",
     "Only factory work", "Only government work",
     "b",
     "Child Labour (Prohibition and Regulation) AMENDMENT 2016: (1) Below 14 = TOTAL BAN on all occupations except family enterprise (non-hazardous) after school hours and entertainment industry (with safeguards). (2) AGES 14-18 ('ADOLESCENTS') = banned only from HAZARDOUS occupations. (3) Penalties enhanced."),

    (1, 3,
     "Connection between Article 24 and Article 21A?\nతెలుగు: Art.24 + Art.21A?",
     "Unrelated",
     "Art.21A = free education 6-14; Art.24 = protection from hazardous work — together form child protection / Art.21A + Art.24 = పిల్లల రక్షణ (correct)",
     "Art.21A = child labour ban", "Art.24 = free education",
     "b",
     "Art.24 (1950 original): protects children below 14 from hazardous work. Art.21A (added by 86th Amendment 2002): right to FREE AND COMPULSORY EDUCATION for ages 6-14. Combined: child cannot be in hazardous work + must be in school. RTE Act 2009 implements Art.21A. Coherent child protection framework."),

    (1, 2,
     "Which Article prohibits child labour below 14 in factories? [APPSC]\nతెలుగు: 14 కింద ఏ Article?",
     "Article 23", "Article 24 (correct)", "Article 25", "Article 21A",
     "b",
     "Article 24: Prohibits employment of children below 14 in factories, mines, hazardous employment. Distinct from: Art.23 = forced labour (any age); Art.21A = right to education 6-14. APPSC frequently confuses these — note specific scope of each.",
     "APPSC"),

    # ───── Section 2: Articles 25-26 — Religious Freedom ─────
    (2, 1,
     "What right does Article 25 guarantee?\nతెలుగు: Art.25 హక్కు?",
     "Right to establish religion only",
     "Freedom of conscience, profession, practice, propagation / మనస్సాక్షి + ఆచరణ + ప్రచారం (correct)",
     "State support to all religions",
     "Religious courts",
     "b",
     "Art.25: Subject to public order, morality, health and other Part III provisions, all persons are equally entitled to FREEDOM OF CONSCIENCE and the right to FREELY PROFESS, PRACTISE and PROPAGATE religion. Available to ALL persons (citizens + non-citizens). Subject to reasonable restrictions and State's power to regulate secular activities."),

    (2, 1,
     "Why is Shirur Math Case (1954) significant?\nతెలుగు: Shirur Math?",
     "Minority educational institutions",
     "Distinguished 'matters of religion' (protected) vs 'secular activities' (State can regulate) — Art.25 & 26 / Religion vs Secular distinction (correct)",
     "Art.17 untouchability", "Citizenship",
     "b",
     "COMMISSIONER, HRE v. SHIRUR MUTT (1954): SC laid down 'ESSENTIAL RELIGIOUS PRACTICES' DOCTRINE. Distinguished: (a) MATTERS OF RELIGION (essential religious practices) — fully protected; (b) SECULAR ACTIVITIES associated with religion (e.g., financial management) — State can regulate. Foundational case for Art.25/26 jurisprudence."),

    (2, 2,
     "What did SC hold in Rev. Stainislaus v. State of MP (1977)?\nతెలుగు: Stainislaus 1977?",
     "Right to forcibly convert under Art.25",
     "'Propagation' = peaceful sharing/teaching; force/fraud/allurement excluded; State anti-conversion laws valid / Propagation = peaceful, force కాదు (correct)",
     "Anti-conversion laws unconstitutional",
     "Propagation = conversion",
     "b",
     "Rev. Stainislaus v. State of MP (1977): SC interpreted 'PROPAGATE' in Art.25 as the right to TRANSMIT/SPREAD one's religion through peaceful means/persuasion/teaching — NOT a fundamental right to CONVERT others. Force/fraud/allurement-based conversion not protected. State laws prohibiting forcible conversion (e.g., MP, Odisha freedom of religion acts) are CONSTITUTIONALLY VALID."),

    (2, 2,
     "What rights do religious denominations have under Article 26?\nతెలుగు: Art.26 హక్కులు?",
     "Collect religious taxes",
     "Establish institutions, manage religious affairs, acquire/administer property / 4 హక్కులు (correct)",
     "Religious instruction in state schools",
     "Amend Constitution",
     "b",
     "Art.26: Every religious DENOMINATION (a section of religion with distinct beliefs) has 4 RIGHTS, subject to public order, morality, health: (a) ESTABLISH and MAINTAIN institutions for religious/charitable purposes; (b) MANAGE its OWN AFFAIRS in matters of religion; (c) ACQUIRE movable/immovable PROPERTY; (d) ADMINISTER such property as per law."),

    (2, 3,
     "What can the State do under Article 25(2)(b)?\nతెలుగు: Art.25(2)(b) State?",
     "Prohibit all religions",
     "Throw open Hindu temples to all Hindus including SCs/STs / Hindu temples అన్ని Hindus కు తెరవడం (correct)",
     "Teach Hinduism in govt schools",
     "Cannot regulate minorities",
     "b",
     "Art.25(2)(b): State can make laws (i) regulating/restricting any economic, financial, political or secular activity associated with religious practice, (ii) providing for SOCIAL WELFARE AND REFORM, INCLUDING THROWING OPEN HINDU RELIGIOUS INSTITUTIONS of a public character to ALL CLASSES AND SECTIONS OF HINDUS. Constitutional basis for temple entry laws."),

    (2, 2,
     "Which is correct about Article 25?\nతెలుగు: Art.25 సరైనది?",
     "Only Indian citizens",
     "Subject to public order, morality, health / Public order, Morality, Health (correct)",
     "Prohibits propagation",
     "Cannot regulate secular activities",
     "b",
     "Art.25 features: (1) Available to ALL persons (citizens + non-citizens); (2) SUBJECT TO public order, morality, health and other Part III provisions; (3) Protects PROPAGATION (peaceful sharing only — Stainislaus 1977); (4) State CAN REGULATE secular activities associated with religion (Shirur Mutt 1954); (5) State CAN make laws for social reform (Art.25(2)(b)).",
     "UPSC"),

    # ───── Section 3: Article 27, 28 — Religious Taxes & Instruction ─────
    (3, 1,
     "What does Article 27 prohibit?\nతెలుగు: Art.27 నిషేధం?",
     "Practising religion",
     "Compelled payment of taxes for promoting any particular religion / మత ప్రచారానికి taxes (correct)",
     "Religious instruction in govt schools",
     "Establishing minority schools",
     "b",
     "Art.27: 'No person shall be compelled to pay any TAXES, the proceeds of which are SPECIFICALLY APPROPRIATED in payment of expenses for the PROMOTION OR MAINTENANCE of any particular religion or religious denomination.' FEES (for secular benefits like roads near temples) are PERMITTED — the prohibition is on RELIGION-SPECIFIC TAX. Reflects SECULARISM."),

    (3, 1,
     "In which schools is religious instruction completely prohibited under Article 28?\nతెలుగు: Art.28 ఏ schools?",
     "State recognised schools",
     "Minority schools",
     "Wholly State-maintained schools / పూర్తిగా రాజ్య నిధులతో (correct)",
     "Aided schools",
     "c",
     "Art.28: (1) WHOLLY STATE-MAINTAINED schools — religious instruction TOTALLY PROHIBITED. (2) State-AIDED but managed by trust/endowment — religious instruction PERMITTED if directed by trust/endowment. (3) State-RECOGNISED — religious instruction allowed but no compulsion (consent of student/guardian needed). (4) Minority schools — Art.30 freedom."),

    (3, 2,
     "What is the consent requirement under Article 28?\nతెలుగు: Art.28 consent?",
     "State permission needed",
     "Student/guardian consent mandatory for religious instruction/worship / విద్యార్థి/guardian consent తప్పనిసరి (correct)",
     "Court permission",
     "Parents must permit",
     "b",
     "Art.28(3): No person attending any STATE-RECOGNISED OR STATE-AIDED institution shall be REQUIRED to take part in any religious instruction or attend any religious worship WITHOUT his/her consent (or guardian's consent if minor). Forces VOLUNTARY participation only — protects individual conscience."),

    # ───── Section 4: Articles 29-30 — Cultural/Educational Rights ─────
    (4, 1,
     "Who has right to establish minority educational institutions under Article 30?\nతెలుగు: Art.30 ఎవరికి?",
     "Only religious minorities",
     "Only linguistic minorities",
     "All minorities — religious AND linguistic / మత + భాషా మైనారిటీలు (correct)",
     "Only Scheduled Castes",
     "c",
     "Art.30(1): All minorities, whether based on RELIGION OR LANGUAGE, shall have the right to ESTABLISH AND ADMINISTER educational institutions of their choice. Covers BOTH religious minorities (Muslims, Christians, Sikhs, Buddhists, Parsis, Jains) AND linguistic minorities (state-specific). State CANNOT discriminate against minority institutions when granting aid."),

    (4, 1,
     "What is TMA Pai Foundation case (2002) about?\nతెలుగు: TMA Pai 2002?",
     "Preamble amendment",
     "Minority status determined STATE-WISE — not nationwide / మైనారిటీ హోదా రాష్ట్ర స్థాయిలో (correct)",
     "Art.21 interpretation", "Presidential election",
     "b",
     "TMA PAI FOUNDATION v. State of Karnataka (2002): 11-judge SC bench. KEY HOLDINGS: (1) Minority status determined STATE-WISE (not nationally) — Sikhs minority outside Punjab, majority within. (2) Right to establish + administer minority institutions (autonomy in admissions/fees/staff). (3) Reasonable State regulations allowed. (4) Art.30 protects minority unaided institutions from quota/fee fixation."),

    (4, 2,
     "Article 29(2) prohibits denial of admission on which grounds in state-aided institutions?\nతెలుగు: Art.29(2) ఆధారాలు?",
     "Only religion and caste",
     "Religion, Race, Caste, Language / మతం, జాతి, కులం, భాష (correct)",
     "Religion only", "Caste and Language only",
     "b",
     "Art.29(2): No CITIZEN shall be DENIED ADMISSION into any educational institution maintained by the State or receiving aid out of State funds, on grounds ONLY of RELIGION, RACE, CASTE, LANGUAGE or any of them. Notably absent: SEX, place of birth (covered by Art.15). Available to citizens only."),

    (4, 3,
     "Key distinction between Article 29 and Article 30?\nతెలుగు: Art.29 vs Art.30?",
     "Both only minorities",
     "Art.29 = 'any section of citizens' (incl. majorities); Art.30 = only minorities / Art.29 = అన్ని, Art.30 = minorities (correct)",
     "Reverse", "Identical",
     "b",
     "Art.29(1) text: 'Any SECTION OF CITIZENS having distinct LANGUAGE, SCRIPT, CULTURE shall have the right to CONSERVE the same' — applies to BOTH minorities and majority sub-groups. Art.30(1): 'All MINORITIES (religious or linguistic) shall have the right to ESTABLISH AND ADMINISTER EDUCATIONAL INSTITUTIONS' — only minorities. Different scope and different rights."),

    (4, 2,
     "Which Article gives minorities right to establish/administer educational institutions? [APPSC]\nతెలుగు: విద్యా సంస్థల హక్కు Article?",
     "Article 28", "Article 29", "Article 30 (correct)", "Article 31",
     "c",
     "Article 30: Both religious AND linguistic minorities can establish and administer educational institutions. Two-fold protection: (1) Right to establish/administer; (2) Equal treatment in State aid (Art.30(2)). Frequently asked in APPSC. Implemented through NCMEI Act 2004 — National Commission for Minority Educational Institutions.",
     "APPSC"),

    # ───── Section 5: Ninth Schedule & Art.31C ─────
    (5, 1,
     "Ninth Schedule was added by which amendment?\nతెలుగు: Ninth Schedule ఏ సవరణ?",
     "42nd Amendment 1976", "1st Amendment 1951 (correct)",
     "44th Amendment 1978", "25th Amendment 1971",
     "b",
     "FIRST CONSTITUTIONAL AMENDMENT 1951 added: (a) NINTH SCHEDULE — to protect land reform laws from court challenges by inserting Art.31B. Bihar Land Reforms Act 1950 was the first law placed there. Currently 280+ laws. Used to immunise laws from FR challenges. Subject to basic structure review post-Coelho (2007)."),

    (5, 2,
     "What did SC hold in IR Coelho (2007)?\nతెలుగు: IR Coelho 2007?",
     "All Ninth Schedule laws immune",
     "Laws added AFTER 24 April 1973 can be challenged if violating Basic Structure / 1973 తర్వాత Basic Structure violate చేస్తే challenge చేయవచ్చు (correct)",
     "Ninth Schedule should be abolished",
     "Art.31B unconstitutional",
     "b",
     "IR COELHO v. State of Tamil Nadu (2007): 9-judge SC bench. Ninth Schedule laws ADDED AFTER 24 APRIL 1973 (date of Kesavananda Bharati judgment) are SUBJECT TO JUDICIAL REVIEW for violation of BASIC STRUCTURE (Part III FRs that form basic structure). Laws added BEFORE this date remain immune (subject to certain limits). Major curb on misuse of Ninth Schedule."),

    (5, 3,
     "Art.31C protects laws implementing which DPSPs?\nతెలుగు: Art.31C ఏ DPSPs?",
     "Art.38 and 40",
     "Art.39(b) and 39(c) / Art.39(b), 39(c) (correct)",
     "Art.44 and 45", "Art.36 and 37",
     "b",
     "Art.31C [25th Amendment 1971]: Laws implementing DPSP Articles 39(b) (equitable distribution of MATERIAL RESOURCES of community) and 39(c) (PREVENTION OF CONCENTRATION OF WEALTH and means of production) are PROTECTED from challenge under Art.14 and Art.19. Kesavananda Bharati (1973) STRUCK DOWN the second part (which had said 'no law shall be called in question on ground of inconsistency') as violating basic structure. So Art.31C is now subject to JR for basic structure violation."),

    # ───── Section 6: Article 32 — Writs ─────
    (6, 1,
     "How did Dr. Ambedkar describe Article 32?\nతెలుగు: Ambedkar Art.32?",
     "Foot of Constitution",
     "Heart and Soul of the Constitution / Heart and Soul (correct)",
     "Superstructure", "Introduction",
     "b",
     "Dr. B.R. AMBEDKAR in Constituent Assembly: 'If I was asked to name any particular Article in this Constitution as the most important — an Article without which this Constitution would be a nullity — I could not refer to any other Article except this one (Art.32). It is the very SOUL of the Constitution and the very HEART of it.' Hence Art.32 is itself a FR (only such enforcement mechanism in any constitution)."),

    (6, 1,
     "What is Habeas Corpus writ used for?\nతెలుగు: Habeas Corpus?",
     "Compel official to perform duty",
     "Release person from illegal detention / అక్రమ నిర్బంధం నుండి విడుదల (correct)",
     "Quash inferior court decision",
     "Challenge unlawful office occupancy",
     "b",
     "HABEAS CORPUS ('You shall have the body'): Court orders the person who has detained another to PRODUCE the detainee before court and JUSTIFY the detention. If detention is illegal — release. Can be issued against State and PRIVATE PARTIES. Available to ALL persons. Suspended in Emergency was upheld in ADM Jabalpur (1976) — overruled by 44th Amendment + Puttaswamy."),

    (6, 1,
     "Against whom can Mandamus NOT be issued?\nతెలుగు: Mandamus ఎవరిపై వేయలేరు?",
     "District Collector", "Public Corporation",
     "President / Governor / రాష్ట్రపతి / గవర్నర్ (correct)",
     "Municipal Commissioner",
     "c",
     "MANDAMUS ('we command') — directs public official/body to perform a public/legal duty. CANNOT be issued against: (1) PRESIDENT or GOVERNOR (Art.361 immunity); (2) Private individuals/bodies (no public duty); (3) When duty is discretionary; (4) To enforce contractual obligation; (5) To restrain legislature (no legal duty to legislate). Issued only against public authorities for public duty."),

    (6, 2,
     "Difference between Prohibition and Certiorari writs?\nతెలుగు: Prohibition vs Certiorari?",
     "Same purpose",
     "Prohibition = BEFORE decision; Certiorari = AFTER decision; both for judicial/quasi-judicial bodies / Prohibition ముందు, Certiorari తర్వాత (correct)",
     "Reverse order",
     "Both against private individuals",
     "b",
     "PROHIBITION ('do not do'): Issued by SC/HC to LOWER COURT or QUASI-JUDICIAL body PREVENTING it from EXCEEDING its jurisdiction or assuming jurisdiction it doesn't have. PREVENTIVE. Issued BEFORE decision. CERTIORARI ('to be certified'): Issued to QUASH a DECISION already made by lower court/tribunal — corrective, AFTER the decision. Both apply only to JUDICIAL/QUASI-JUDICIAL bodies — NOT to administrative or private bodies."),

    (6, 2,
     "Who has locus standi to file Quo Warranto?\nతెలుగు: Quo Warranto ఎవరు?",
     "Only aggrieved person",
     "Only directly affected",
     "Any member of public — no aggrieved party required / ఎవరైనా ఫైల్ చేయవచ్చు (correct)",
     "Only Attorney General",
     "c",
     "QUO WARRANTO ('by what authority?'): Court inquires into the legality of a person's claim to a public office. WIDE LOCUS STANDI — ANY MEMBER OF PUBLIC can apply (no need to show personal injury). This is unlike Mandamus/Certiorari which need aggrieved party. Reflects PUBLIC INTEREST in lawful occupancy of public office. Issued only for public offices held without legal authority/qualification."),

    (6, 3,
     "Difference between Art.32 SC writs and Art.226 HC writs?\nతెలుగు: Art.32 vs Art.226?",
     "Art.32 wider",
     "Art.226 (HC) WIDER — FR + any other purpose; Art.32 (SC) = only FR enforcement / HC scope ఎక్కువ (correct)",
     "Same scope", "Art.32 superior",
     "b",
     "Art.32: SC can issue writs ONLY for ENFORCEMENT OF FUNDAMENTAL RIGHTS. Art.32 itself is a FR. Art.226: HC can issue writs for FR enforcement AND for 'ANY OTHER PURPOSE' — includes ordinary legal rights, statutory rights, public law remedies. Art.226 SCOPE WIDER. But Art.32 is FR (cannot be denied); Art.226 discretionary. SC under Art.32 has direct jurisdiction; can also issue writs under Art.142 (complete justice)."),

    (6, 2,
     "Which writ prevents inferior court from exceeding jurisdiction?\nతెలుగు: Jurisdiction exceed రిట్?",
     "Habeas Corpus", "Mandamus",
     "Prohibition (correct)", "Certiorari",
     "c",
     "Prohibition: Issued by superior court (SC/HC) to inferior judicial/quasi-judicial body PREVENTING it from EXCEEDING jurisdiction. PREVENTIVE writ — before decision. Different from Certiorari which QUASHES a decision after it's made. Habeas Corpus = release illegally detained. Mandamus = compel public duty. Each writ has distinct purpose.",
     "UPSC"),

    (6, 2,
     "Which writ is considered the most important? [APPSC]\nతెలుగు: అత్యంత ముఖ్యమైన?",
     "Mandamus",
     "Habeas Corpus — protects personal liberty / Habeas Corpus (correct)",
     "Certiorari", "Quo Warranto",
     "b",
     "HABEAS CORPUS is considered the MOST IMPORTANT writ — it's the BULWARK OF PERSONAL LIBERTY. Protects individuals from arbitrary/illegal detention. Available to all (citizens + non-citizens). Even if the detainee can't approach court, anyone (relative/friend) can file on their behalf. Operates against State and private parties. Frequently called 'GREAT WRIT OF LIBERTY'.",
     "APPSC"),

    # ───── Section 7: Articles 33-35 & Emergency ─────
    (7, 1,
     "Who has power to make laws to enforce Part III FRs under Article 35?\nతెలుగు: Art.35 అధికారం?",
     "State legislatures",
     "Parliament only (NOT state legislatures) / Parliament మాత్రమే (correct)",
     "President", "Supreme Court",
     "b",
     "Art.35: Notwithstanding anything in the Constitution, ONLY PARLIAMENT (not state legislatures) shall have power to make laws for: (a) prescribing residence requirements (Art.16(3)), specifying public services in States (Art.32(3)), restrictions on FRs of armed forces etc. (Art.33), indemnifying State servants for acts during martial law (Art.34); (b) prescribing PUNISHMENTS for violations of Art.17 (Untouchability) and Art.23 (Forced Labour). Reserves these matters for uniform Central legislation."),

    (7, 2,
     "Which FRs can NEVER be suspended even during Emergency?\nతెలుగు: Suspend చేయలేని FRs?",
     "Art.14 and 19", "Art.17 and 32",
     "Articles 20 and 21 / Art.20, 21 (correct)",
     "Art.25 and 30",
     "c",
     "Art.20 (Protection in respect of conviction — ex post facto, double jeopardy, self-incrimination) and Art.21 (Right to Life and Personal Liberty) CANNOT be suspended even during NATIONAL EMERGENCY. Established by 44th AMENDMENT 1978 (in response to ADM Jabalpur 1976 which had allowed Art.21 suspension during 1975 Emergency). Other FRs can be suspended via Presidential Order under Art.359."),

    (7, 3,
     "For whom can Parliament restrict/abrogate FRs under Article 33?\nతెలుగు: Art.33 ఎవరికి?",
     "Only IAS officers and Judges",
     "Armed Forces, Para-military, Intelligence agencies, Police maintaining public order / 4 categories (correct)",
     "Central Govt employees only",
     "All persons",
     "b",
     "Art.33: Parliament can RESTRICT or ABROGATE FRs of: (a) members of ARMED FORCES, (b) members of forces charged with maintenance of PUBLIC ORDER (police, paramilitary), (c) persons employed in ANY BUREAU/intelligence organization, (d) persons employed in connection with TELECOMMUNICATION SYSTEMS for above forces. Purpose: ensure DISCIPLINE and proper discharge of duties. Implementing laws: Army Act, Air Force Act, Navy Act, BSF Act, etc."),

    (7, 4,
     "Which of these are correct: (1) Art.19 auto-suspended in NE; (2) Art.359 needs Order; (3) Art.35 = state legs; (4) Art.20, 21 never suspended?\nతెలుగు: ఏది సరైనది?",
     "Only 1, 2 and 4 / 1, 2, 4 సరైనవి (correct)",
     "Only 1, 2 and 3", "All four", "Only 2 and 4",
     "a",
     "1 ✓: Art.19 auto-suspended on War/External Aggression NE proclamation under Art.358 (44th Am: only war/external aggression, not armed rebellion). 2 ✓: Art.359 — President MUST issue specific Order to suspend enforcement of FRs (not auto). 3 ✗: Art.35 reserves law-making to PARLIAMENT ONLY (not state legislatures). 4 ✓: Art.20 and 21 NEVER suspended (44th Am safeguard)."),

    (7, 2,
     "Which FRs cannot be suspended during Emergency? [APPSC]\nతెలుగు: Emergency లో?",
     "Art.14 and 15", "Art.17 and 18",
     "Articles 20 and 21 / Art.20, 21 (correct)",
     "Art.25 and 26",
     "c",
     "Art.20 + Art.21 = ABSOLUTE protection. NEVER suspended even during NATIONAL EMERGENCY. 44th Amendment 1978 enshrined this. Art.20 covers: ex post facto law prohibition, double jeopardy, self-incrimination protection. Art.21: right to life and personal liberty. Critical safeguards established post-1975 Emergency abuses (ADM Jabalpur). Frequently asked APPSC.",
     "APPSC"),
]



import json as _json


def _seed_polity_ch8_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    import json as _j
    ph = '%s' if use_postgres else '?'
    _sections = [
    {"title": "8.1 ఆర్టికల్ 23: బలవంతపు వెట్టి చాకిరీ నిషేధం", "sub": "Art 23 · Forced Labour · Trafficking · Bonded Labour", "audio": ""},
    {"title": "8.2 ఆర్టికల్ 24: బాలల చాకిరీ నిషేధం", "sub": "Art 24 · Child Labour · Factories · Mines · Hazardous", "audio": ""},
    {"title": "8.3 ఆర్టికల్ 25-26: మతస్వాతంత్ర్యం", "sub": "Art 25 · Art 26 · Freedom of Religion · Conscience", "audio": ""},
    {"title": "8.4 ఆర్టికల్ 27-28: మతం మరియు విద్య", "sub": "Art 27 · Art 28 · Religious Taxation · Institutions", "audio": ""},
    {"title": "8.5 ఆర్టికల్ 29-30: సాంస్కృతిక మరియు విద్యా హక్కులు", "sub": "Art 29 · Art 30 · Minority Rights · Language · Script", "audio": ""},
    {"title": "8.6 ఆర్టికల్ 31A-31C: రక్షిత చట్టాలు", "sub": "Art 31A · Art 31B · Art 31C · 9th Schedule · Property", "audio": ""},
    {"title": "8.7 ఆర్టికల్ 32: రాజ్యాంగ పరిహారాల హక్కు", "sub": "Art 32 · Writs · Habeas Corpus · Mandamus · Certiorari", "audio": ""},
    {"title": "8.8 ఆర్టికల్ 33-35 మరియు అత్యవసర నిలుపు", "sub": "Art 33 · Art 34 · Art 35 · Emergency · FR Suspension", "audio": ""}
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
        (8, 'Indian_Polity'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True,
                'message': 'Polity Ch8 notes already seeded.'}
    if row and force:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (8, 'Indian_Polity'))
    if use_postgres:
        conn.commit()

    db_exec_fn(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'Indian_Polity', '', 8,
         'ప్రాథమిక హక్కులు భాగం II',
         'Fundamental Rights Part II',
         'Ch.8',
         _j.dumps(_sections, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'Polity Ch8 notes seeded!'}


def _seed_polity_ch8_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
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
        (8, 'Indian_Polity'))
    row = cur.fetchone()
    if not row:
        _seed_polity_ch8_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)
        cur = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (8, 'Indian_Polity'))
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
    for mcq in POLITY_CH8_MCQS:
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

    total = len(POLITY_CH8_MCQS)
    return {
        'success': True,
        'message': f'Polity Ch8 MCQs seeded! Total: {total}',
        'inserted': total,
        'easy': easy, 'medium': medium, 'hard': hard,
        'toughest': toughest, 'pyq': pyq
    }
