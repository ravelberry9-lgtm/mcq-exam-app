# seed_polity_ch15.py
# Chapter 15 – President of India
# (భారత రాష్ట్రపతి)
# Lakshmikanth's Indian Polity | APPSC Group 2 Standard
# Total Sections: 8 | Total MCQs: 63 | PYQs: 5
# Difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
# ─────────────────────────────────────────────────────

import json as _json

POLITY_CH15_SECTIONS = [
    {
        "title": "15.1 రాష్ట్రపతి — ఎన్నిక మరియు అర్హతలు",
        "sub": "Art.52–62 · Electoral College · STV · Qualifications · Term · Oath · CJI",
        "audio": ""
    },
    {
        "title": "15.2 రాష్ట్రపతి — తొలగింపు మరియు ఖాళీ",
        "sub": "Art.61 · Impeachment · 14 Days Notice · 2/3 Majority · Art.65 VP Acting",
        "audio": ""
    },
    {
        "title": "15.3 కార్యనిర్వాహక మరియు శాసన అధికారాలు",
        "sub": "Art.53 · Art.74 · Art.77 · Art.86–87 · Art.108 · Art.111 · CoM Advice",
        "audio": ""
    },
    {
        "title": "15.4 ఆర్థిక మరియు న్యాయ అధికారాలు",
        "sub": "Art.72 · Pardoning Power · Pardon/Commutation/Remission · Art.143 · Finance Commission",
        "audio": ""
    },
    {
        "title": "15.5 ఆర్డినెన్స్ అధికారం",
        "sub": "Art.123 · When Parliament Not in Session · 6 Weeks · D.C. Wadhwa · Repromulgation",
        "audio": ""
    },
    {
        "title": "15.6 అత్యవసర అధికారాలు",
        "sub": "Art.352 · National Emergency · Art.356 · President's Rule · Art.360 · Financial Emergency",
        "audio": ""
    },
    {
        "title": "15.7 వీటో అధికారాలు మరియు విచక్షణాధికారాలు",
        "sub": "Absolute Veto · Suspensive Veto · Pocket Veto · Discretionary Powers · Situational Discretion",
        "audio": ""
    },
    {
        "title": "15.8 కఠిన ప్రశ్నలు — APPSC/UPSC PYQs",
        "sub": "Electoral disputes · Art.71 SC · President vs Governor pardoning · Historical PYQs",
        "audio": ""
    },
]

POLITY_CH15_MCQS = [

    # ══════════════ SECTION 0 — Election, Qualifications, Term ══════════════

    (0, 1,
     "Which Article deals with the election of the President of India?\nతెలుగు: భారత రాష్ట్రపతి ఎన్నికకు సంబంధించిన అనుచ్ఛేదం?",
     "Art.52",
     "Art.54 (correct)",
     "Art.56",
     "Art.58",
     "b",
     "Art.54 = election of President through Electoral College. Art.52 establishes that 'There shall be a President of India'. Art.55 = manner of election. Art.56 = term. Art.58 = qualifications."),

    (0, 2,
     "Who are the members of the Electoral College for Presidential election?\nతెలుగు: రాష్ట్రపతి ఎలక్టోరల్ కాలేజ్ సభ్యులు ఎవరు?",
     "Elected MPs of both Houses only / ఉభయ సభల ఎన్నికైన MP లు మాత్రమే",
     "Lok Sabha only / లోక్‌సభ మాత్రమే",
     "Elected MPs (LS+RS) + elected MLAs of all States + elected MLAs of Delhi & Puducherry / ఎన్నికైన MP లు + MLA లు + ఢిల్లీ/పుదుచ్చేరి (correct)",
     "Includes nominated members of RS / RS నామినేటెడ్ సభ్యులు కూడా",
     "c",
     "Art.54 + 70th Amendment (1992): Electoral College = elected MPs of both Houses + elected MLAs of all States + elected MLAs of Delhi (NCT) and Puducherry. NOMINATED members are EXCLUDED. So is Legislative Council MLCs."),

    (0, 1,
     "What method is used in the Presidential election?\nతెలుగు: రాష్ట్రపతి ఎన్నికలో ఏ పద్ధతి?",
     "Direct election / ప్రత్యక్ష ఎన్నిక",
     "Simple majority / సాధారణ మెజారిటీ",
     "Proportional Representation by Single Transferable Vote (STV), secret ballot / అనుపాత ప్రాతినిధ్యం STV (correct)",
     "Only by MPs / MP లు మాత్రమే",
     "c",
     "Art.55(3): Presidential election is by Proportional Representation with Single Transferable Vote (STV) using secret ballot. Voters mark preferences. A candidate must secure quota = (Total valid votes / 2) + 1."),

    (0, 2,
     "What are the qualifications for President of India under Art.58?\nతెలుగు: రాష్ట్రపతి అర్హతలు Art.58?",
     "Indian citizen, 30 years / 30 సంవత్సరాలు",
     "Indian citizen, 35 years, eligible for LS membership, holds no office of profit / 35 సంవత్సరాలు + LS అర్హత + లాభదాయక పదవి లేకుండా (correct)",
     "Indian citizen, 40 years, RS eligible / 40 + RS",
     "Indian citizen, 25 years / 25",
     "b",
     "Art.58: Qualifications — (1) Citizen of India, (2) completed 35 years, (3) eligible for Lok Sabha membership, (4) holds no office of profit under Union/State/local govt. Art.58(2) exempts: President, VP, Governor, Union/State Ministers."),

    (0, 1,
     "What is the term of office of the President of India?\nతెలుగు: రాష్ట్రపతి పదవీ కాలం?",
     "4 years / 4 సం.",
     "5 years / 5 సం. (correct)",
     "6 years / 6 సం.",
     "Until pleasure / అనుగ్రహం వరకు",
     "b",
     "Art.56: President holds office for 5 YEARS from the date of entering office. Art.57 — eligible for re-election (no fixed limit on number of terms in India, unlike US 22nd Amendment)."),

    (0, 2,
     "In whose presence does the President take the oath of office?\nతెలుగు: రాష్ట్రపతి ప్రమాణం ఎవరి సమక్షంలో?",
     "Lok Sabha Speaker / LS స్పీకర్",
     "PM / ప్రధాని",
     "Chief Justice of India — Art.60 / CJI Art.60 (correct)",
     "RS Chairman / RS చైర్మన్",
     "c",
     "Art.60: President takes oath before the CHIEF JUSTICE OF INDIA. In CJI's absence, the most senior judge of the Supreme Court available. The oath of office form is in Art.60 itself."),

    (0, 3,
     "How is the value of an MP's vote calculated in the Presidential election?\nతెలుగు: MP ఓటు విలువ?",
     "Each MP = 1 vote / ప్రతి MP = 1 ఓటు",
     "Total value of all State MLA votes ÷ Total elected MPs of both Houses / మొత్తం MLA ఓట్లు ÷ ఎన్నికైన MP లు (correct)",
     "State population ÷ 1000 / జనాభా ÷ 1000",
     "Number of states ÷ MPs / రాష్ట్రాలు ÷ MP",
     "b",
     "MP vote value = Total value of all State MLA votes ÷ Total number of ELECTED MPs of both Houses. MLA vote value = State population ÷ (Total elected MLAs of state × 1000). Population basis: 1971 Census frozen by 84th Amendment."),

    (0, 2,
     "How many proposers and seconders are required for Presidential nomination?\nతెలుగు: ప్రతిపాదకులు, అనుమోదకులు?",
     "5 + 5",
     "50 proposers + 50 seconders, all from Electoral College / 50 + 50 (correct)",
     "25 + 25",
     "10 + 10",
     "b",
     "Presidential and Vice-Presidential Elections Act 1952: Nomination requires 50 PROPOSERS + 50 SECONDERS, all from Electoral College. Security deposit: ₹15,000. (Earlier requirement was 10+10; raised by 1997 amendment to discourage frivolous candidates)."),

    (0, 3,
     "What is the 'Office of Profit' condition for Presidential candidacy?\nతెలుగు: లాభదాయక పదవి?",
     "Any govt employment forbidden / ఏ ఉద్యోగమైనా నిషేధం",
     "No office of profit under Union/State/local body; but President, VP, Governor, Union/State Ministers are exempted / ఎలాంటి లాభదాయక పదవి (correct)",
     "Only Central govt jobs barred / కేంద్ర ఉద్యోగాలే",
     "Officeholders cannot contest / అధికారులు పోటీ చేయలేరు",
     "b",
     "Art.58(2): Candidate must NOT hold any office of profit under Union/State/local body. EXEMPTIONS: President, Vice-President, Governor of any state, and any Union/State Minister are NOT considered to hold office of profit for this purpose."),

    (0, 2,
     "Can the President resign before the term ends?\nతెలుగు: రాష్ట్రపతి రాజీనామా చేయవచ్చా?",
     "No — must complete 5 years / 5 సం. పూర్తి చేయాలి",
     "Yes — by writing under hand addressed to the Vice President — Art.56(1)(a) / అవును, VP కు లిఖితంగా (correct)",
     "Resignation to LS Speaker / LS స్పీకర్",
     "Resignation to PM / PM",
     "b",
     "Art.56(1)(a): President may resign by writing under his hand addressed to the VICE PRESIDENT. The VP shall forthwith communicate the resignation to the Speaker of Lok Sabha (Art.56(2))."),

    (0, 2,
     "If a successor has not assumed office after President's term ends, what happens?\nతెలుగు: ఉత్తరాధికారి బాధ్యత తీసుకోకపోతే?",
     "Office becomes vacant / ఖాళీ అవుతుంది",
     "PM takes charge / PM",
     "Outgoing President continues until successor assumes — Art.56(1)(c) / మునుపటి రాష్ట్రపతి కొనసాగుతారు (correct)",
     "CJI takes over / CJI",
     "c",
     "Art.56(1)(c): If no successor has entered office at the expiry of term, the OUTGOING President continues to hold office UNTIL a successor enters office. Ensures continuity — no vacuum."),

    (0, 3,
     "How did the 70th Constitutional Amendment 1992 affect Presidential election?\nతెలుగు: 70వ సవరణ ప్రభావం?",
     "Vote value changed / ఓటు విలువ మారింది",
     "Included elected MLAs of Delhi (NCT) and Puducherry in Electoral College / ఢిల్లీ + పుదుచ్చేరి MLA లు (correct)",
     "Direct election introduced / ప్రత్యక్ష ఎన్నిక",
     "Nominated RS members included / RS నామినేటెడ్",
     "b",
     "70th Constitutional Amendment Act 1992: Amended Art.54 to include elected members of Legislative Assemblies of NATIONAL CAPITAL TERRITORY OF DELHI and PUDUCHERRY in the Presidential Electoral College. Effective from 1 June 1995."),

    (0, 2,
     "Where does the President take the oath as per Constitution?\nతెలుగు: రాష్ట్రపతి ప్రమాణం ఎక్కడ?",
     "Parliament House / పార్లమెంట్ హౌస్",
     "Rashtrapati Bhavan only / రాష్ట్రపతి భవన్",
     "Constitution does not specify location; in presence of CJI / రాజ్యాంగంలో స్థలం పేర్కొనలేదు (correct)",
     "Supreme Court / సుప్రీం కోర్టు",
     "c",
     "Art.60 specifies the oath text and presence of CJI but does NOT specify location. Conventionally, oath is taken at Central Hall of Parliament. Newly elected President swears 'preserve, protect and defend the Constitution and the law'."),

    (0, 1,
     "Who pays the salary and allowances of the President?\nతెలుగు: రాష్ట్రపతి జీతం ఎవరు చెల్లిస్తారు?",
     "State governments collectively / రాష్ట్ర ప్రభుత్వాలు",
     "Charged on Consolidated Fund of India (Art.59(3)) / భారత సంఘటిత నిధి నుండి (correct)",
     "Voted by Parliament / పార్లమెంట్ ఓటు ద్వారా",
     "President's own funds / స్వంత నిధులు",
     "b",
     "Art.59(3): Emoluments and allowances of President are CHARGED on the Consolidated Fund of India — non-votable in Parliament. Cannot be DIMINISHED during term (Art.59(4)). Current salary: ₹5 lakh/month."),

    (0, 2,
     "Re-election eligibility of the President is mentioned in?\nతెలుగు: పునర్ ఎన్నిక అర్హత?",
     "Art.55",
     "Art.56",
     "Art.57 (correct)",
     "Art.58",
     "c",
     "Art.57: 'A person who holds, or who has held, office as President shall, subject to the other provisions of this Constitution, be eligible for re-election to that office.' No limit on number of terms (unlike US 22nd Amendment limit of 2 terms)."),

    # ══════════════ SECTION 1 — Impeachment, Removal, Vacancy ══════════════

    (1, 2,
     "What is the procedure for impeachment of the President?\nతెలుగు: రాష్ట్రపతి Impeachment విధానం?",
     "Lok Sabha alone with 2/3 majority / LS మాత్రమే 2/3",
     "Either House: 14-day notice + 2/3 of total membership; other House investigates and passes with 2/3 majority / ఏ సభ నుండైనా 14 రోజుల నోటీస్ + 2/3 (correct)",
     "Only Rajya Sabha / RS మాత్రమే",
     "On Supreme Court recommendation / SC సిఫార్సు",
     "b",
     "Art.61 Impeachment: Initiated in EITHER House by 14-day notice signed by 1/4 of total members. Resolution must pass by 2/3 of TOTAL MEMBERSHIP. Other House investigates (President can defend). Other House must also pass by 2/3 → removal."),

    (1, 2,
     "How many members must sign the Impeachment notice?\nతెలుగు: Impeachment నోటీసుకు సంతకాలు?",
     "1/2 of total membership / 1/2",
     "1/4 of total membership of initiating House / మొత్తం సభ్యత్వంలో 1/4 (correct)",
     "100 members / 100",
     "50 members / 50",
     "b",
     "Art.61(2): Notice for Impeachment must be signed by at least 1/4 (one-fourth) of TOTAL membership of the initiating House. Then 14 days notice. Then resolution moved and passed by 2/3 of total membership."),

    (1, 1,
     "Who acts as President when the office falls vacant?\nతెలుగు: రాష్ట్రపతి పదవి ఖాళీ అయితే?",
     "PM / ప్రధాని",
     "LS Speaker / స్పీకర్",
     "Vice President — Art.65 / ఉపరాష్ట్రపతి (correct)",
     "CJI / CJI",
     "c",
     "Art.65: Vice President acts as President in case of vacancy by death/resignation/impeachment until new President is elected (within 6 months). If VP also unavailable, CJI acts. If CJI unavailable, senior-most SC judge."),

    (1, 3,
     "Key difference between Presidential Impeachment and No-Confidence Motion?\nతెలుగు: Impeachment vs NCM?",
     "Both same / రెండూ ఒకటే",
     "NCM only in LS, against CoM, simple majority. Impeachment in either House, against President, requires 2/3 of total membership of each House and proof of constitutional violation / NCM = LS, Impeachment = ఏ సభైనా (correct)",
     "Impeachment only in LS / LS మాత్రమే",
     "NCM by simple majority / సాధారణ మెజారిటీ",
     "b",
     "NCM: Lok Sabha only, against Council of Ministers, simple majority of present-and-voting. Impeachment: Either House, against President, requires 2/3 of TOTAL membership of each House separately, and ground = 'violation of Constitution'."),

    (1, 3,
     "Is 'violation of Constitution' for Presidential Impeachment defined?\nతెలుగు: 'violation of Constitution' నిర్వచించారా?",
     "Yes, clearly defined / అవును",
     "No — Constitution does not define it; Parliament interprets / కాదు, పార్లమెంట్ నిర్ణయిస్తుంది (correct)",
     "Defined by SC / SC నిర్వచిస్తుంది",
     "Defined by EC / EC",
     "b",
     "Constitution does NOT define what constitutes 'violation of Constitution' for Impeachment purposes. Left to Parliament's interpretation. This vagueness combined with 2/3 supermajority makes Impeachment extremely difficult — never invoked in India."),

    # ══════════════ SECTION 2 — Executive & Legislative Powers ══════════════

    (2, 1,
     "In whom is the executive power of the Union vested?\nతెలుగు: సమాఖ్య కార్యనిర్వాహక అధికారం ఎవరికి?",
     "PM / ప్రధాని",
     "Council of Ministers / CoM",
     "President — Art.53 / రాష్ట్రపతి (correct)",
     "Lok Sabha / LS",
     "c",
     "Art.53(1): The executive power of the Union shall be VESTED in the President and shall be exercised by him directly or through officers SUBORDINATE to him. In practice, exercised on aid and advice of CoM (Art.74)."),

    (2, 2,
     "After 44th Amendment 1978, is CoM advice binding on President?\nతెలుగు: 44వ సవరణ తర్వాత CoM సలహా బాధ్యకరమా?",
     "No — discretion / కాదు",
     "Yes — binding; but President may return ONCE for reconsideration; reconsidered advice is binding / అవును, ఒకసారి తిరిగి పంపించవచ్చు (correct)",
     "Only during war / యుద్ధకాలంలో",
     "RS Chairman decides / RS చైర్మన్",
     "b",
     "42nd Amendment (1976) made CoM advice BINDING. 44th Amendment (1978) added: President may REQUIRE CoM to RECONSIDER advice ONCE. After reconsideration (with or without changes), the advice is binding (Art.74(1) proviso)."),

    (2, 2,
     "Under which Article can President summon, prorogue, dissolve Parliament?\nతెలుగు: సమావేశం, వాయిదా, రద్దు?",
     "Art.80",
     "Art.83",
     "Art.85 (correct)",
     "Art.108",
     "c",
     "Art.85: (1) Summon both Houses; (2)(a) Prorogue session; (2)(b) Dissolve Lok Sabha. Gap between sessions cannot exceed 6 months. Dissolution power exercised on PM's advice; but discretionary if no clear majority or PM has lost confidence."),

    (2, 2,
     "Can President return a Bill without giving assent?\nతెలుగు: రాష్ట్రపతి బిల్లు తిరిగి పంపగలరా?",
     "No, must approve / తప్పనిసరి ఆమోదం",
     "Yes — for non-Money Bills, ONCE for reconsideration; if Parliament passes again, must give assent / అవును, ఒకసారి (correct)",
     "Yes, multiple times / అనేక సార్లు",
     "Only Constitutional Amendment Bills / Constitutional Amendment మాత్రమే",
     "b",
     "Art.111 (Suspensive Veto): President may return any Bill (EXCEPT Money Bill) ONCE for reconsideration. If Parliament re-passes (with or without amendments), President MUST give assent. For Money Bills, only ASSENT or WITHHOLDING — no return."),

    (2, 3,
     "When does the President give a 'Special Address' to Parliament?\nతెలుగు: ప్రత్యేక సందేశం?",
     "Every session's first day / ప్రతి సెషన్ మొదటి రోజు",
     "Only during national emergency / అత్యవసర పరిస్థితిలో",
     "First session of each year and first session after general elections — Art.87 / ప్రతి సం. మొదటి సెషన్ + సాధారణ ఎన్నికల తర్వాత (correct)",
     "Only before Budget session / బడ్జెట్ ముందు",
     "c",
     "Art.87: President addresses joint sitting of both Houses (1) at the commencement of the FIRST SESSION OF EACH YEAR, and (2) at the FIRST SESSION OF EACH NEW LOK SABHA after general elections. Speech outlines government's policy."),

    (2, 2,
     "In whose name is all business of Government of India conducted?\nతెలుగు: కేంద్ర ప్రభుత్వ కార్యాలు ఎవరి పేరున?",
     "PM / ప్రధాని",
     "Parliament / పార్లమెంట్",
     "President — Art.77 / రాష్ట్రపతి (correct)",
     "Council of Ministers / CoM",
     "c",
     "Art.77(1): All EXECUTIVE ACTIONS of the Government of India shall be expressed to be taken in the NAME OF THE PRESIDENT. Art.77(2): Orders authenticated as per rules made by President. Art.77(3): President makes rules for transaction of govt business."),

    (2, 2,
     "What duties must the PM perform towards the President under Art.78?\nతెలుగు: Art.78 PM విధులు?",
     "Send budget draft / బడ్జెట్ ముసాయిదా",
     "Communicate all CoM decisions and legislative proposals; provide information when President asks / అన్ని నిర్ణయాలు తెలపాలి (correct)",
     "Advise on RS nominations / RS నామినేషన్",
     "Send legislative election schedules / ఎన్నికల షెడ్యూల్",
     "b",
     "Art.78: PM's duties to President: (a) communicate to President all DECISIONS of CoM relating to administration and legislative proposals; (b) furnish such INFORMATION on administration as President may call for; (c) submit any matter for CoM consideration if President requires."),

    (2, 3,
     "Pocket Veto applies in which situations?\nతెలుగు: Pocket Veto పరిస్థితులు?",
     "All Bills / అన్ని",
     "Only state bills / రాష్ట్ర బిల్లు",
     "Mainly Private Member Bills and Bills passed after CoM defeat — possible because Art.111 sets no time limit / Art.111 లో సమయం లేదు (correct)",
     "Doesn't apply to any Bill / ఏదీ లేదు",
     "c",
     "POCKET VETO is possible because Art.111 sets NO TIME LIMIT for Presidential decision (unlike US 10 days). President can simply NOT ACT — Bill remains pending indefinitely. Famously used by Zail Singh on 1986 Postal Bill."),

    # ══════════════ SECTION 3 — Pardoning, Reference, Clemency ══════════════

    (3, 1,
     "Under which Article does the President have pardoning power?\nతెలుగు: క్షమాభిక్ష ఏ Article?",
     "Art.70",
     "Art.72 (correct)",
     "Art.74",
     "Art.76",
     "b",
     "Art.72: Pardoning power of President. Covers: (a) Pardon, (b) Reprieve, (c) Respite, (d) Remission, (e) Commutation. Applies to: Union law offences, court-martial sentences, and DEATH SENTENCES (death sentence pardon is Pres-only; Governor cannot)."),

    (3, 2,
     "What are the types of Presidential clemency under Art.72?\nతెలుగు: క్షమాభిక్ష రకాలు?",
     "Pardon and Commutation only / Pardon, Commutation",
     "Pardon, Reprieve, Respite, Remission, Commutation — five types / 5 రకాలు (correct)",
     "Only Pardon / Pardon మాత్రమే",
     "Pardon and Appeal / Pardon, Appeal",
     "b",
     "Five types under Art.72: (1) PARDON = full absolution (record erased); (2) COMMUTATION = lesser punishment (death→life); (3) REMISSION = shorter period (10yr→5yr); (4) RESPITE = lesser sentence due to special factors (pregnancy/disability); (5) REPRIEVE = temporary stay of execution."),

    (3, 2,
     "Key difference between President's and Governor's pardoning powers?\nతెలుగు: రాష్ట్రపతి-గవర్నర్ తేడా?",
     "No difference / తేడా లేదు",
     "Only President can pardon death sentence and court-martial sentences; Governor (Art.161) cannot do either / రాష్ట్రపతికి మాత్రమే మరణ శిక్ష, కోర్ట్ మార్షల్ (correct)",
     "Only Governor can pardon death / గవర్నర్",
     "President only state law / రాష్ట్ర చట్టాలు మాత్రమే",
     "b",
     "Differences: (1) Death sentence — only PRESIDENT (Art.72) can pardon; Governor (Art.161) CANNOT. (2) Court-martial — only President. (3) State law — Governor can pardon any State law offence (Art.161); President can also if relates to Union/concurrent."),

    (3, 3,
     "Can President seek opinion of Supreme Court under Art.143?\nతెలుగు: Art.143 SC అభిప్రాయం?",
     "No, President cannot seek legal opinion / కాదు",
     "Yes — Art.143 Presidential Reference; SC may or may not give opinion; opinion is advisory not binding / అవును, advisory (correct)",
     "Yes — opinion is binding / బాధ్యకరం",
     "Only during emergency / అత్యవసర పరిస్థితిలో",
     "b",
     "Art.143 (Presidential Reference): President may refer to SC any question of (a) law/fact of public importance, or (b) dispute under pre-Constitution treaty. SC MAY (discretion) give opinion. Opinion is ADVISORY — not binding. Famous: Berubari, 2nd Judges Case."),

    (3, 3,
     "Is rejection of mercy petition subject to judicial review?\nతెలుగు: క్షమాభిక్ష తిరస్కరణపై న్యాయసమీక్ష?",
     "No — President's decision is final / కాదు",
     "Yes — Epuru Sudhakar (2006): JR possible; arbitrary rejection invalid / అవును, Epuru Sudhakar (correct)",
     "Only in death sentence cases / మరణ శిక్షలో మాత్రమే",
     "HC can review / HC",
     "b",
     "Epuru Sudhakar v. State of AP (2006): SC held that exercise of clemency power under Art.72/161 is subject to LIMITED judicial review on grounds of: (1) without applying mind, (2) mala fide, (3) on irrelevant considerations, (4) discrimination, (5) arbitrariness."),

    (3, 2,
     "For punishment under State law — who grants clemency?\nతెలుగు: రాష్ట్ర చట్టం - క్షమాభిక్ష?",
     "President (Art.72)",
     "Supreme Court / SC",
     "Governor (Art.161) / గవర్నర్ (correct)",
     "High Court / HC",
     "c",
     "Art.161: Governor can grant pardon, reprieve, respite, remission, commutation for offences against any STATE LAW. Art.72: President can do same for Union law, court-martial, and death sentence. Death sentence pardon is President's exclusive power."),

    # ══════════════ SECTION 4 — Ordinance-Making Power ══════════════

    (4, 1,
     "When can the President promulgate an Ordinance?\nతెలుగు: ఆర్డినెన్స్ ఎప్పుడు?",
     "When Parliament is in session / సమావేశంలో ఉన్నప్పుడు",
     "Only when both Houses of Parliament are NOT in session — Art.123 / రెండు సభలు recess లో (correct)",
     "Only during war / యుద్ధంలో",
     "With permission of one House / ఒక సభ అనుమతితో",
     "b",
     "Art.123: President can promulgate Ordinance ONLY when BOTH Houses (LS + RS) are NOT in session. If even ONE House is in session, ordinance cannot be issued. Need: 'satisfied that circumstances require immediate action'. CoM advice required (binding)."),

    (4, 2,
     "Within what period must a Presidential Ordinance be laid before Parliament?\nతెలుగు: ఆర్డినెన్స్ పార్లమెంట్‌లో ఎప్పుడు?",
     "Within 30 days of reassembly / 30 రోజులు",
     "Within 6 weeks of Parliament reassembling / 6 వారాలు (correct)",
     "3 months / 3 నెలలు",
     "6 months / 6 నెలలు",
     "b",
     "Art.123(2): Ordinance must be laid before both Houses within 6 WEEKS of Parliament reassembling. It CEASES to operate after 6 weeks unless Parliament passes a resolution approving it. Disapproval by either House also makes it cease."),

    (4, 2,
     "What is the maximum life of a Presidential Ordinance?\nతెలుగు: ఆర్డినెన్స్ గరిష్ట జీవితకాలం?",
     "3 months / 3 నెలలు",
     "6 months / 6 నెలలు",
     "6 months + 6 weeks (~7.5 months) / 6 నెలలు + 6 వారాలు (correct)",
     "1 year / 1 సం.",
     "c",
     "Maximum life = 6 months (max gap between sessions per Art.85) + 6 weeks (laying period per Art.123(2)) ≈ 7.5 months. After this, ordinance lapses automatically unless converted into Act."),

    (4, 3,
     "What did D.C. Wadhwa case 1987 rule about Presidential Ordinances?\nతెలుగు: D.C. Wadhwa కేసు?",
     "Ordinances are beyond judicial review / JR అతీతం",
     "REPROMULGATION of Ordinances without Parliament approval is unconstitutional — fraud on Constitution / Repromulgation Constitutional విరుద్ధం (correct)",
     "Cannot be challenged in courts / కోర్టులలో సవాలు చేయలేరు",
     "Ordinances become law automatically / స్వయంచాలకంగా",
     "b",
     "D.C. Wadhwa v. State of Bihar (1987): SC held that systematic REPROMULGATION of Ordinances (Bihar repromulgated 256 ordinances over 1967-81) without seeking Parliament's approval is FRAUD ON CONSTITUTION. Reaffirmed by 7-judge bench in Krishna Kumar Singh (2017)."),

    (4, 2,
     "Limitations on President's Ordinance-making power?\nతెలుగు: ఆర్డినెన్స్ పరిమితులు?",
     "No limitations / పరిమితులు లేవు",
     "Cannot amend Constitution; cannot violate Fundamental Rights; cannot relate to State List subjects / రాజ్యాంగ సవరణ + FR + state list లేదు (correct)",
     "Only during financial crisis / ఆర్థిక సంకటంలో",
     "Only with CoM approval / CoM తో మాత్రమే",
     "b",
     "Limitations: (1) Cannot amend Constitution (Art.368 procedure required); (2) Cannot violate Fundamental Rights (Art.13(2)); (3) Limited to subjects on which Parliament can legislate (Union/Concurrent List); (4) Subject to JR for malafide/colourable exercise."),

    (4, 3,
     "Can an Ordinance be withdrawn without laying before Parliament?\nతెలుగు: Parliament ముందుంచకుండా వెనక్కి?",
     "No, must lay / తప్పనిసరి",
     "Yes — President can withdraw any time / అవును, ఎప్పుడైనా (correct)",
     "Only with CoM recommendation / CoM తో మాత్రమే",
     "Court permission needed / కోర్టు అనుమతి",
     "b",
     "Art.123(2): President can WITHDRAW an Ordinance at any time. Ordinance also automatically ceases: (i) 6 weeks after Parliament reassembles, (ii) earlier if disapproved by resolution of either House. CoM advice required for withdrawal too."),

    (4, 2,
     "Under which Article does the Governor have Ordinance power?\nతెలుగు: గవర్నర్ ఆర్డినెన్స్ Article?",
     "Art.123",
     "Art.213 (correct)",
     "Art.200",
     "Art.167",
     "b",
     "Art.213: Governor's Ordinance-making power — parallel to President's Art.123 for the Union. Issued when state legislature is not in session. Limitations similar; additionally, requires PRESIDENT'S INSTRUCTIONS for certain matters (those needing prior Presidential sanction for bills)."),

    # ══════════════ SECTION 5 — Emergency Powers ══════════════

    (5, 1,
     "Under which Article can National Emergency be proclaimed?\nతెలుగు: జాతీయ అత్యవసర పరిస్థితి Article?",
     "Art.356",
     "Art.352 (correct)",
     "Art.360",
     "Art.365",
     "b",
     "Art.352: NATIONAL EMERGENCY — proclaimed on grounds of (1) War, (2) External Aggression, or (3) Armed Rebellion. 44th Amendment 1978 replaced 'internal disturbance' with 'armed rebellion' (Indira Gandhi's 1975 Emergency was on internal disturbance ground)."),

    (5, 2,
     "Under which Article is President's Rule imposed?\nతెలుగు: రాష్ట్రపతి పాలన Article?",
     "Art.352",
     "Art.356 (correct)",
     "Art.360",
     "Art.355",
     "b",
     "Art.356: PRESIDENT'S RULE (State Emergency) — imposed when constitutional machinery in a state has FAILED. Based on Governor's report or otherwise. Initially 6 months, extendable up to 3 years with Parliament's approval. S.R. Bommai (1994) curbed misuse."),

    (5, 2,
     "Under which Article is Financial Emergency declared?\nతెలుగు: ఆర్థిక అత్యవసర పరిస్థితి?",
     "Art.352",
     "Art.356",
     "Art.360 (correct)",
     "Art.370",
     "c",
     "Art.360: FINANCIAL EMERGENCY — when financial stability or credit of India or any part is threatened. Has NEVER been proclaimed in India. Effects: (a) reduce salaries of all govt servants including SC/HC judges; (b) Centre direct states on financial matters."),

    (5, 3,
     "Is written advice of Cabinet required before proclaiming National Emergency?\nతెలుగు: Cabinet లిఖిత సలహా అవసరమా?",
     "Not required / అవసరం లేదు",
     "Yes — after 44th Amendment 1978, written Cabinet advice is mandatory / అవును (correct)",
     "Only PM advice / PM మాత్రమే",
     "Parliament approval first / Parliament ముందుగా",
     "b",
     "44th Amendment 1978 added safeguard: President can proclaim National Emergency ONLY on the basis of WRITTEN ADVICE of the CABINET (not just PM). Earlier Indira Gandhi proclaimed 1975 Emergency on PM's advice alone — this loophole was closed."),

    (5, 2,
     "Within what period must Parliament approve National Emergency?\nతెలుగు: NE ఆమోద కాలం?",
     "30 days / 30 రోజులు",
     "1 month / 1 నెల",
     "1 month from proclamation; if LS dissolved, RS must approve and reconstituted LS within 30 days (max ~2 months) / 1 నెల + LS రద్దు అయితే 2 నెలలు (correct)",
     "6 months / 6 నెలలు",
     "c",
     "44th Amendment: NE must be approved by both Houses by SPECIAL MAJORITY within ONE MONTH of proclamation. Once approved, in force for 6 months; can be extended 6 months at a time indefinitely. If LS dissolved, RS approves and new LS within 30 days."),

    (5, 3,
     "How can Lok Sabha revoke a National Emergency proclamation?\nతెలుగు: NE రద్దు?",
     "By 2/3 majority / 2/3 మెజారిటీ",
     "By simple majority / సాధారణ మెజారిటీ",
     "By simple majority of total LS membership — 44th Amendment / మొత్తం సభ్యత్వంలో సాధారణ మెజారిటీ (correct)",
     "Only with RS approval / RS తో మాత్రమే",
     "c",
     "44th Amendment 1978: Lok Sabha alone can REVOKE National Emergency by passing a resolution by simple majority of TOTAL membership. RS approval not needed for revocation. Also, 1/10 of LS members can demand a revocation meeting within 14 days."),

    (5, 3,
     "Effect on State powers during National Emergency?\nతెలుగు: NE లో రాష్ట్రాల అధికారాలు?",
     "States dissolved / రాష్ట్రాలు రద్దు",
     "Parliament can legislate on State List; Centre can give executive directions to states / Parliament State List పై చట్టాలు, కేంద్ర ఆదేశాలు (correct)",
     "No effect / ప్రభావం లేదు",
     "Governors dissolved / గవర్నర్లు రద్దు",
     "b",
     "Art.353(a): Parliament gets power to legislate on STATE LIST subjects. Art.353(b): Centre can give executive DIRECTIONS to states. Art.354: Distribution of revenues can be modified. Art.358/359: Fundamental Rights suspended (Art.19 auto under war/aggression)."),

    (5, 2,
     "Maximum duration of President's Rule (Art.356)?\nతెలుగు: PR గరిష్ట కాలం?",
     "6 months",
     "1 year",
     "3 years (with conditions) / 3 సం. (correct)",
     "5 years",
     "c",
     "Art.356 PR: Initially 6 months. Extended by 6 months at a time with Parliamentary approval. MAX = 3 YEARS. Beyond 1 year, only if (a) National Emergency in operation in whole/part of state, AND (b) EC certifies that elections cannot be held."),

    # ══════════════ SECTION 6 — Veto Powers, Discretion, Nominal Head ══════════════

    (6, 2,
     "What is President's 'Absolute Veto'?\nతెలుగు: Absolute Veto?",
     "Block voting on Bill / ఓటింగ్ ఆపడం",
     "President withholds assent — Bill lapses; cannot be overridden by Parliament / ఆమోదం నిరాకరిస్తే Bill రద్దు (correct)",
     "Return Bill to Parliament / తిరిగి పంపించడం",
     "Seek SC opinion / SC అభిప్రాయం",
     "b",
     "ABSOLUTE VETO: President WITHHOLDS ASSENT — Bill simply LAPSES; Parliament cannot override. Used typically for: (a) Private Member Bills where govt opposes, (b) Bills passed by outgoing govt that has lost confidence. (E.g., 1991 PEPSU Appropriation Bill)."),

    (6, 2,
     "What is President's 'Suspensive Veto'?\nతెలుగు: Suspensive Veto?",
     "Refuses assent / ఆమోదం నిరాకరిస్తారు",
     "Leaves Bill undecided / నిర్ణయం తీసుకోరు",
     "Returns Bill for reconsideration; if Parliament passes again, must give assent / తిరిగి పంపిస్తే Parliament మళ్లీ ఆమోదిస్తే తప్పనిసరి (correct)",
     "Sends to RS / RS కు",
     "c",
     "SUSPENSIVE VETO (Art.111): President returns non-Money Bill ONCE for reconsideration with message. Parliament reconsiders and can pass with/without amendments. Once re-passed, President MUST give assent. NOT applicable to Money Bills or Constitutional Amendment Bills (24th Am)."),

    (6, 3,
     "When do the President's Discretionary Powers apply?\nతెలుగు: విచక్షణాధికారాలు?",
     "Never — always follow CoM / ఎప్పుడూ లేవు",
     "PM appointment in hung parliament; refusing dissolution; Art.143 reference; reconsideration of CoM advice / హంగ్ Parliament లో PM నియామకం (correct)",
     "Only in emergency / అత్యవసర పరిస్థితిలో",
     "Only constitutional amendments / Constitutional amendments",
     "b",
     "Discretionary powers: (1) Appointment of PM when no party has clear majority; (2) Dismissing CoM if it can't prove majority; (3) Dissolving LS if CoM lost confidence; (4) Returning Bill once for reconsideration; (5) Art.143 reference; (6) Pocket Veto."),

    (6, 2,
     "Why is the President called 'Nominal Head' of State?\nతెలుగు: 'Nominal Head' ఎందుకు?",
     "No powers / అధికారాలు లేవు",
     "Art.74 makes CoM advice binding — President acts constitutionally, not politically / Art.74 బాధ్యకరం (correct)",
     "Not elected by people / ప్రజలచే ఎన్నుకోబడరు",
     "Cannot vote in Parliament / ఓటు లేదు",
     "b",
     "President is the CONSTITUTIONAL/NOMINAL/TITULAR Head — real executive power lies with CoM headed by PM (REAL EXECUTIVE). Art.74 binds President to CoM advice. Like British convention: 'King reigns but Cabinet rules'. Walter Bagehot's 'Dignified vs Efficient' executive."),

    (6, 3,
     "Who described India's President as 'Dignified Executive'?\nతెలుగు: 'Dignified Executive' ఎవరు?",
     "B.R. Ambedkar / అంబేడ్కర్",
     "J.L. Nehru / నెహ్రూ",
     "Walter Bagehot — British constitutional thinker; framework applied to India / వాల్టర్ బాగెహాట్ (correct)",
     "K.M. Munshi / మున్షి",
     "c",
     "Walter Bagehot (English Constitution, 1867) classified British constitution into 'EFFICIENT' parts (Cabinet — real power) and 'DIGNIFIED' parts (Monarch — symbolic). India's President = Dignified Executive; PM + CoM = Efficient Executive."),

    (6, 3,
     "Difference between 'Pocket Veto' and 'Absolute Veto'?\nతెలుగు: Pocket vs Absolute?",
     "Same thing / ఒకటే",
     "Absolute Veto = explicit refusal of assent; Pocket Veto = no decision taken indefinitely / Absolute = స్పష్ట నిరాకరణ; Pocket = నిర్ణయం లేదు (correct)",
     "Pocket can be overridden by Parliament / Pocket Parliament override చేయగలదు",
     "Absolute means constitutional amendment / Absolute = constitutional amendment",
     "b",
     "ABSOLUTE VETO: President EXPLICITLY refuses assent — Bill lapses formally. POCKET VETO: President takes NO ACTION at all — Bill remains pending indefinitely (possible because Art.111 has no time limit, unlike US 10-day rule). Neither overridable."),

    # ══════════════ SECTION 7 — Disputes, Misc, History ══════════════

    (7, 3,
     "Which court adjudicates disputes relating to Presidential election?\nతెలుగు: ఎన్నిక వివాదం?",
     "High Court / HC",
     "Election Commission / EC",
     "Supreme Court — Art.71 / SC Art.71 (correct)",
     "Parliament / Parliament",
     "c",
     "Art.71: ALL doubts and disputes arising out of or in connection with the election of President or Vice-President shall be inquired into and decided by the SUPREME COURT — and its decision shall be FINAL. SC has original jurisdiction here."),

    (7, 3,
     "Does a vacancy in Electoral College affect Presidential election validity?\nతెలుగు: ఎలక్టోరల్ కాలేజ్‌లో ఖాళీ ప్రభావం?",
     "Yes — election void / ఎన్నిక రద్దు",
     "No — Art.71(4): election not invalid due to any vacancy in Electoral College / రద్దు కాదు (correct)",
     "President decides / రాష్ట్రపతి",
     "Need 90% Electoral College / 90% అవసరం",
     "b",
     "Art.71(4): The election of a President or VP shall NOT BE CALLED IN QUESTION on the ground of the existence of any VACANCY for whatever reason in the Electoral College electing him. Ensures continuity even if state assemblies are under dissolution."),

    (7, 4,
     "Significance of President Zail Singh's Pocket Veto on the Indian Post Office Bill?\nతెలుగు: జైల్ సింగ్ Pocket Veto ప్రాధాన్యత?",
     "President has no return power / అధికారం లేదు",
     "India's Constitution sets no time limit for Presidential decision — inaction itself is Pocket Veto (US has 10-day limit) / Art.111 లో సమయం లేదు (correct)",
     "Bill auto-lapses / స్వయంచాలకంగా రద్దు",
     "Constitutional amendment needed / Constitutional amendment అవసరం",
     "b",
     "Zail Singh (1982-87) demonstrated Pocket Veto in 1986: he NEVER signed and NEVER returned the Indian Post Office (Amendment) Bill 1986 (which would've allowed govt to intercept letters). Indian Constitution Art.111 has NO time limit (US has 10 days)."),

    (7, 3,
     "How many times has the President faced Impeachment proceedings?\nతెలుగు: Impeachment ఎన్నిసార్లు?",
     "Twice / 2 సార్లు",
     "Three times / 3 సార్లు",
     "Never — no President has been impeached / ఎప్పుడూ లేదు (correct)",
     "Five times / 5 సార్లు",
     "c",
     "NO President of India has EVER been impeached. Art.61 requires 2/3 of TOTAL membership of EACH House — extremely difficult threshold. Combined with vague 'violation of Constitution' ground, Impeachment is more theoretical than practical safeguard."),

    (7, 3,
     "Who was the first woman President of India?\nతెలుగు: మొదటి మహిళా రాష్ట్రపతి?",
     "Indira Gandhi / ఇందిరా గాంధీ",
     "Sarojini Naidu / సరోజినీ నాయుడు",
     "Pratibha Patil — 2007–2012 / ప్రతిభా పాటిల్ (correct)",
     "Droupadi Murmu / ద్రౌపది ముర్ము",
     "c",
     "Pratibha Devisingh Patil — 12th President of India (2007–2012) — FIRST WOMAN PRESIDENT. Droupadi Murmu — 15th President (since 2022) — first TRIBAL woman President. Sarojini Naidu was first woman Governor (UP, 1947-49)."),

    (7, 4,
     "Who has been elected President of India the maximum times?\nతెలుగు: అత్యధిక సార్లు ఎన్నికైన?",
     "Rajendra Prasad — twice / రాజేంద్ర ప్రసాద్ 2 సార్లు (correct)",
     "V.V. Giri",
     "No one elected twice / ఎవరూ లేదు",
     "APJ Abdul Kalam",
     "a",
     "Dr Rajendra Prasad — first President of India, served TWO TERMS (1950-57 and 1957-62). The ONLY person to be elected President of India TWICE. Total tenure ~12 years. After 1962, no President has been re-elected."),

    (7, 3,
     "What J&K-related provision existed regarding President's Rule?\nతెలుగు: J&K ప్రత్యేక ప్రావిజన్?",
     "J&K excluded from elections / ఎన్నికల నుండి",
     "Art.356A applied / Art.356A",
     "Pre-2019: Art.370 special procedure for J&K President's Rule; post-Aug 2019 abrogation, Art.356 applies directly / Art.370 ద్వారా (correct)",
     "Governor appointed by state / గవర్నర్ రాష్ట్రం ద్వారా",
     "c",
     "Pre-Aug 2019: J&K had special status under Art.370 — President's Rule needed Art.370(1)(c) + Art.356 combination, with concurrence of state govt. Art.370 ABROGATED on 5 August 2019 — J&K became UT, Art.356 applies directly like other states."),

    (7, 4,
     "How did V.V. Giri win 1969 Presidential election — why historic?\nతెలుగు: V.V. గిరి 1969 ఎన్నిక?",
     "Unanimously elected / ఏకగ్రీవం",
     "Won through second preference votes (STV demonstrated)",
     "Won as independent without Congress support / Congress లేకుండా",
     "Both B and C / B, C రెండూ (correct)",
     "d",
     "V.V. Giri (1969): Stood as INDEPENDENT against official Congress candidate Neelam Sanjiva Reddy. Indira Gandhi gave 'Conscience vote' call splitting Congress. Giri won through SECOND PREFERENCE votes — historic demonstration of STV's importance."),

    (7, 3,
     "Who served as President before first Lok Sabha elections?\nతెలుగు: మొదటి LS ముందు రాష్ట్రపతి?",
     "C. Rajagopalachari / రాజగోపాలాచారి",
     "Rajendra Prasad / రాజేంద్ర ప్రసాద్",
     "Rajagopalachari was last GG; Rajendra Prasad first elected President from Constitutional commencement / రాజేంద్ర ప్రసాద్ (correct)",
     "B.R. Ambedkar / అంబేడ్కర్",
     "c",
     "C. Rajagopalachari was last Governor-General of India (1948-50). On 26 January 1950 (Constitution commencement), Dr Rajendra Prasad was elected first President by the CONSTITUENT ASSEMBLY (acting as provisional Parliament). First general elections were 1951-52."),

    (7, 3,
     "What does Art.59 specify about President's conditions?\nతెలుగు: Art.59 ఏం?",
     "Term / కాలం",
     "Salaries only / జీతం మాత్రమే",
     "Cannot be member of Parliament/State legislature; no office of profit; free official residence; emoluments fixed by Parliament, not reducible / Art.59 conditions (correct)",
     "Election method / ఎన్నిక",
     "c",
     "Art.59: Conditions of President's office: (1) Cannot be member of Parliament/State legislature (deemed to vacate seat on assuming office); (2) No office of profit; (3) Official residence (Rashtrapati Bhavan) free; (4) Emoluments and allowances fixed by Parliament — not reducible during tenure."),

    (7, 4,
     "Under which Article does the President have immunity from legal proceedings?\nతెలుగు: legal immunity?",
     "Art.71",
     "Art.58",
     "Art.361 (correct)",
     "Art.74",
     "c",
     "Art.361: PERSONAL IMMUNITY of President (and Governors) — (a) Not answerable to any court for OFFICIAL acts; (b) NO criminal proceedings during tenure; (c) NO arrest/imprisonment during tenure; (d) Civil proceedings for personal acts allowed only after 2 months' written notice."),
]


# ─────────────────────────────────────────────────────────────
def _seed_polity_ch15_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    """Insert Chapter 15 study note row (idempotent)."""
    existing = db_exec_fn(conn,
        "SELECT id FROM study_notes WHERE topic='Indian_Polity' AND chapter_num=15"
    ).fetchone()
    if existing and not force:
        return

    sections_json = _json.dumps(POLITY_CH15_SECTIONS, ensure_ascii=False)
    ph = '%s' if use_postgres else '?'

    if existing and force:
        db_exec_fn(conn,
            f"UPDATE study_notes SET sections_json={ph}, chapter_title_en={ph}, chapter_title_te={ph} "
            f"WHERE topic='Indian_Polity' AND chapter_num=15",
            (sections_json,
             "President of India",
             "భారత రాష్ట్రపతి")
        )
        return

    db_exec_fn(conn,
        f"""INSERT INTO study_notes
            (subject, topic, subtopic, chapter_num,
             chapter_title_te, chapter_title_en, pages_ref, sections_json)
            VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
        ('GK', 'Indian_Polity', 'Lakshmikanth', 15,
         'భారత రాష్ట్రపతి',
         'President of India',
         'Ch.15',
         sections_json)
    )


def _seed_polity_ch15_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
    """Insert Chapter 15 MCQs (skip if already present)."""
    note_row = db_exec_fn(conn,
        "SELECT id FROM study_notes WHERE topic='Indian_Polity' AND chapter_num=15"
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
    for row in POLITY_CH15_MCQS:
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
