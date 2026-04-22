"""
App Ch76 = Book Ch73: Rights and Liabilities of the Government
Lakshmikanth Indian Polity – seed file
64 MCQs × 8 sections, 1 study note
"""
import importlib

NOTES_HTML = """<!DOCTYPE html>
<html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">
<title>Ch76 – Rights and Liabilities of the Government</title>
<style>
body{margin:0;font-family:'Segoe UI',sans-serif;background:#f5f5f5;color:#212121}
.hdr{background:linear-gradient(135deg,#4a148c,#7b1fa2);color:#fff;padding:32px 24px;text-align:center}
.hdr h1{margin:0;font-size:1.6rem}.hdr p{margin:4px 0 0;opacity:.85;font-size:.95rem}
.wrap{max-width:860px;margin:0 auto;padding:16px}
.sh{background:#7b1fa2;color:#fff;padding:10px 16px;border-radius:6px;margin:20px 0 10px;font-size:1rem;font-weight:700}
.c{background:#fff;border-radius:8px;padding:14px 16px;margin-bottom:10px;box-shadow:0 1px 4px rgba(0,0,0,.08);border-left:5px solid #9c27b0}
.c.b{border-left-color:#1565c0}.c.a{border-left-color:#2e7d32}.c.r{border-left-color:#b71c1c}
.c.p{border-left-color:#4a148c}.c.g{border-left-color:#e65100}.c.gr{border-left-color:#37474f}.c.t{border-left-color:#00695c}
.c h3{margin:0 0 6px;font-size:.97rem;color:#4a148c}.c.b h3{color:#1565c0}.c.a h3{color:#2e7d32}.c.r h3{color:#b71c1c}
.c.p h3{color:#4a148c}.c.g h3{color:#e65100}.c.gr h3{color:#37474f}.c.t h3{color:#00695c}
.fact{margin:4px 0;font-size:.9rem;line-height:1.55}.fact::before{content:"• "}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}
.pill{background:#f3e5f5;color:#4a148c;border-radius:20px;padding:4px 12px;font-size:.82rem;font-weight:600}
</style></head><body>
<div class=\"hdr\"><h1>⚖️ Rights and Liabilities of the Government</h1>
<p>App Chapter 76 &nbsp;|&nbsp; Lakshmikanth Book Ch73</p></div>
<div class=\"wrap\">

<div class=\"sh\">0. Constitutional Framework</div>
<div class=\"c p\"><h3>Art.299 – Contracts by Government</h3>
<p class=\"fact\">All contracts by the Union or a State shall be expressed to be made by the President/Governor respectively</p>
<p class=\"fact\">Executed by a person authorised by the President/Governor</p>
<p class=\"fact\">Failure to comply → contract not enforceable against the Government (not void, but can't bind Govt)</p>
<p class=\"fact\">Art.299 protects Govt from unauthorised/ultra-vires contracts</p></div>
<div class=\"c b\"><h3>Art.300 – Suits by and Against Government</h3>
<p class=\"fact\">Union of India may sue and be sued in the name of "Union of India"</p>
<p class=\"fact\">State Governments may sue and be sued in name of the State</p>
<p class=\"fact\">Based on pre-constitution law: Secretary of State in Council → Dominion of India → Union of India</p>
<p class=\"fact\">Art.300 preserves the right of individuals to sue the Government</p></div>

<div class=\"sh\">1. Doctrine of Sovereign Immunity</div>
<div class=\"c r\"><h3>P&O Steam Navigation Co. Case (1861)</h3>
<p class=\"fact\">P&O Steam Navigation Co. v. Secretary of State for India — Calcutta HC (1861)</p>
<p class=\"fact\">Distinction: Sovereign functions (immunity) vs Non-sovereign functions (liability)</p>
<p class=\"fact\">Sovereign functions = act of state, maintaining army, waging war → no liability</p>
<p class=\"fact\">Non-sovereign functions = commercial, trade, maintenance work → full liability like private person</p></div>
<div class=\"c g\"><h3>Immunity in Independent India</h3>
<p class=\"fact\">Kasturilal v. State of UP (1965) — Supreme Court upheld sovereign immunity doctrine</p>
<p class=\"fact\">Mugger abducted a gold merchant; police negligence; SC: seizure of property = sovereign function → State not liable</p>
<p class=\"fact\">Kasturilal criticised as outdated in a welfare state context</p>
<p class=\"fact\">Trend since 1960s: courts narrowing sovereign immunity, expanding State liability</p></div>

<div class=\"sh\">2. Evolution and Erosion of Sovereign Immunity</div>
<div class=\"c a\"><h3>Vidyawati Case (1962)</h3>
<p class=\"fact\">State of Rajasthan v. Vidyawati (1962) — Government jeep accident caused death</p>
<p class=\"fact\">SC: driving a government vehicle = non-sovereign function → State liable</p>
<p class=\"fact\">First major SC case restricting sovereign immunity post-independence</p></div>
<div class=\"c t\"><h3>Later Cases Narrowing Immunity</h3>
<p class=\"fact\">Nilabati Behera v. State of Orissa (1993) — custodial death → State liable under Art.32/Art.226</p>
<p class=\"fact\">D.K. Basu v. State of WB (1997) — custodial violence guidelines; State liable for compensation</p>
<p class=\"fact\">Rudal Shah v. State of Bihar (1983) — wrongful imprisonment → SC awarded compensation under Art.32</p>
<p class=\"fact\">Chairman, Railway Board v. Chandrima Das (2000) — rape by railway employee → Indian Railways liable</p></div>

<div class=\"sh\">3. Government Contracts (Art.299)</div>
<div class=\"c p\"><h3>Essentials of Valid Government Contract</h3>
<p class=\"fact\">1. Contract expressed to be made by President/Governor (on behalf of)</p>
<p class=\"fact\">2. Executed by a person duly authorised by President/Governor</p>
<p class=\"fact\">3. Must be in writing</p>
<p class=\"fact\">Non-compliance = personal liability of the officer who contracted, NOT government liability</p></div>
<div class=\"c b\"><h3>Art.299(2) – Personal Liability Protection</h3>
<p class=\"fact\">No person making or executing a contract in his personal capacity on behalf of Govt is personally liable</p>
<p class=\"fact\">But if formalities of Art.299(1) not followed → officer personally liable, Govt not bound</p>
<p class=\"fact\">Purpose: protect officers from personal suits for bona fide acts on behalf of Govt</p></div>

<div class=\"sh\">4. Government Property and Torts</div>
<div class=\"c gr\"><h3>Doctrine of Sovereign Immunity vs Welfare State</h3>
<p class=\"fact\">Welfare state paradigm: State performs vast range of activities — immunity is anomalous</p>
<p class=\"fact\">21st Law Commission recommended abolishing distinction between sovereign/non-sovereign</p>
<p class=\"fact\">UK: Crown Proceedings Act 1947 — abolished Crown immunity for most torts</p>
<p class=\"fact\">India: no comprehensive legislation; courts have done case-by-case erosion</p></div>
<div class=\"c r\"><h3>Constitutional Tort</h3>
<p class=\"fact\">Art.32 + Art.226 = constitutional tort remedy for fundamental rights violations by State</p>
<p class=\"fact\">SC can award compensation even in writ jurisdiction for constitutional torts</p>
<p class=\"fact\">Rudul Shah 1983, Nilabati Behera 1993, Sebastian Hongray 1984 — SC awarded damages under Art.32</p>
<p class=\"fact\">Constitutional tort bypasses sovereign immunity doctrine</p></div>

<div class=\"sh\">5. Suits Against Government</div>
<div class=\"c a\"><h3>CPC Section 80 – Notice Requirement</h3>
<p class=\"fact\">Section 80, Code of Civil Procedure: 2-month notice before suing Central/State Govt or public officer</p>
<p class=\"fact\">Notice must specify cause of action, relief sought, name and address of plaintiff</p>
<p class=\"fact\">Failure to give notice → suit not maintainable (subject to amendments allowing urgent cases)</p>
<p class=\"fact\">2002 Amendment to CPC: urgent cases → court may allow suit without notice with permission</p></div>
<div class=\"c g\"><h3>Suit by Government</h3>
<p class=\"fact\">Government can sue any person in civil courts for recovery of dues, breach of contract, etc.</p>
<p class=\"fact\">Government suits filed in name of Union of India / State of [Name]</p>
<p class=\"fact\">Attorney General represents Union in courts; Advocate General represents State</p>
<p class=\"fact\">Limitation Act applies to Govt suits (though Govt used to have longer limitation periods)</p></div>

<div class=\"sh\">6. Special Protections and Privileges</div>
<div class=\"c t\"><h3>Government Privileges in Evidence</h3>
<p class=\"fact\">Section 123, Indian Evidence Act: Cabinet documents, state affairs documents — privilege against disclosure</p>
<p class=\"fact\">Section 124: Official communications — privilege claimed by head of department</p>
<p class=\"fact\">Court can inspect the document to decide whether to uphold the privilege</p>
<p class=\"fact\">Public interest immunity: court balances public interest in disclosure vs public interest in secrecy</p></div>
<div class=\"c p\"><h3>Art.361 – Presidential Immunity</h3>
<p class=\"fact\">President and Governors are not answerable to any court for exercise of their powers and duties</p>
<p class=\"fact\">No criminal proceedings against President/Governor during term of office</p>
<p class=\"fact\">Civil proceedings: 2-month notice required; no arrest or imprisonment during term</p>
<p class=\"fact\">Art.361 does not protect President from impeachment by Parliament</p></div>

<div class=\"sh\">7. Key Facts Quick Revision</div>
<div class=\"c gr\"><h3>Key Articles</h3>
<div class=\"pills\">
<span class=\"pill\">Art.299 – Govt Contracts</span><span class=\"pill\">Art.300 – Suits by/against Govt</span>
<span class=\"pill\">Art.361 – Presidential Immunity</span><span class=\"pill\">P&O Case 1861</span>
<span class=\"pill\">Kasturilal 1965</span><span class=\"pill\">Vidyawati 1962</span>
<span class=\"pill\">Rudul Shah 1983</span><span class=\"pill\">CPC Sec.80</span>
</div></div>
<div class=\"c b\"><h3>Quick Numbers</h3>
<p class=\"fact\">3 essentials for valid Govt contract under Art.299</p>
<p class=\"fact\">2-month notice under CPC Sec.80 before suing Govt</p>
<p class=\"fact\">P&O Case 1861 — first sovereign/non-sovereign distinction</p>
<p class=\"fact\">Kasturilal 1965 — last major SC case upholding broad sovereign immunity</p></div>

</div></body></html>"""

SUMMARY_HTML = """<!DOCTYPE html>
<html lang=\"en\"><head><meta charset=\"UTF-8\">
<title>Summary Ch76 – Rights and Liabilities of the Government</title>
<style>
body{font-family:'Segoe UI',sans-serif;background:#f5f5f5;margin:0;padding:16px;color:#212121}
.box{background:#fff;border-radius:8px;padding:16px;max-width:700px;margin:0 auto;box-shadow:0 1px 4px rgba(0,0,0,.1)}
h2{color:#4a148c;margin-top:0}ul{padding-left:20px}li{margin-bottom:6px;font-size:.93rem}
</style></head><body><div class=\"box\">
<h2>⚖️ Ch76: Rights and Liabilities of the Government — Summary</h2>
<ul>
<li><b>Art.299</b> — Government contracts: expressed in name of President/Governor, executed by authorised person, must be in writing</li>
<li><b>Art.300</b> — Govt can sue and be sued as "Union of India" / State name</li>
<li><b>P&O Case 1861</b> — Sovereign vs Non-sovereign functions distinction (basis of immunity doctrine)</li>
<li><b>Kasturilal 1965</b> — SC upheld sovereign immunity (criticised as anachronistic)</li>
<li><b>Vidyawati 1962</b> — First major SC restriction on immunity; Govt jeep accident = non-sovereign</li>
<li><b>CPC Sec.80</b> — 2-month notice before suing Central/State Govt</li>
<li><b>Constitutional tort</b> — Art.32/226 compensation for fundamental rights violations bypasses immunity</li>
<li><b>Art.361</b> — President/Governor immunity: no criminal proceedings during term</li>
</ul>
</div></body></html>"""

SECTIONS = [
    "Constitutional Framework",
    "Doctrine of Sovereign Immunity",
    "Evolution and Erosion of Sovereign Immunity",
    "Government Contracts (Art.299)",
    "Government Property and Torts",
    "Suits Against Government",
    "Special Protections and Privileges",
    "Key Facts",
]

_MCQ_DATA = [
    # Section 0: Constitutional Framework (8)
    (0,"easy","Art.299 ప్రకారం Government contract ఎవరి పేరిట express చేయాలి? / Under Art.299 all Govt contracts shall be expressed to be made by whom?",
     "Prime Minister/Chief Minister","President/Governor respectively for Union/State","Parliament/State Legislature","Supreme Court/High Court","b",
     "Art.299(1): All contracts by Union → expressed to be made by the President; All contracts by a State → expressed to be made by the Governor of that State. / Art.299: Govt contracts — expressed in name of President (Union) or Governor (State)."),
    (0,"medium","Art.299 contract requirements ఏమిటి? / What are the requirements for a valid government contract under Art.299?",
     "Only oral agreement needed","Must be: (1) expressed in name of President/Governor; (2) executed by duly authorised person; (3) in writing","Only Presidential approval","Only Parliamentary ratification","b",
     "Art.299 essentials: (1) Expressed to be made by President/Governor; (2) Executed by a person duly authorised by President/Governor; (3) Must be in writing. Failure to comply → Govt not bound, personal liability on officer. / Art.299: 3 essentials — expressed by P/G + authorised person + writing."),
    (0,"easy","Art.300 ప్రకారం Union of India ని suit చేయవచ్చా? / Can Union of India be sued under Art.300?",
     "No, cannot be sued","Yes — Union of India may sue and be sued in name 'Union of India'","Only by foreign countries","Only by States","b",
     "Art.300: Union of India may sue and be sued in name 'Union of India'; State Governments may sue and be sued in name of the State. Art.300 preserves right of individuals to sue the Government. / Art.300: Govt can sue/be sued — Union as 'Union of India', State as 'State of [Name]'."),
    (0,"hard","Art.299 comply చేయకపోతే ఏమవుతుంది? / What happens if Art.299 formalities are not complied with?",
     "Contract becomes void","Contract is not enforceable against Government — Government not bound; officer who contracted may be personally liable","Contract is enforceable against officer only","Contract binds Parliament","b",
     "Non-compliance with Art.299: (1) Government is NOT bound by the contract; (2) Contract cannot be enforced against Govt; (3) But the officer who contracted may be personally liable. Note: contract is not automatically void, just can't bind Govt. / Art.299 breach: Govt not bound; officer personally liable."),
    (0,"medium","Art.300 ఏ predecessor provision based గా ఉంది? / On what predecessor does Art.300 base itself?",
     "Completely new provision","Based on pre-constitution law: Secretary of State in Council → Dominion of India → Union of India; preserved continuity of suits","Based on British Crown Proceedings Act","Based on Govt of India Act 1919","b",
     "Art.300 basis: Pre-constitutional law — suits by/against Secretary of State in Council (British period) → became Dominion of India (1947) → Union of India (1950). Art.300 preserves continuity. / Art.300: successor to pre-constitution Secretary of State in Council→Dominion→Union of India."),
    (0,"easy","Union of India ని suit చేసే case లో plaintiff ఎవరికి notice ఇవ్వాలి? / In a suit against Union of India, to whom must notice be given?",
     "To the Prime Minister","To the concerned ministry/department — Section 80 CPC: 2-month notice to Union of India before filing suit","To Parliament","No notice required","b",
     "CPC Section 80: Before suing Central Govt — 2-month notice to the concerned Central Govt officer or Secretary of the Ministry. Before suing State Govt — 2-month notice to State Govt. Failure → suit not maintainable. / CPC Sec.80: 2-month notice to Govt before suit; failure = suit not maintainable."),
    (0,"medium","Art.299(2) officer ని ఏ నుండి protect చేస్తుంది? / What does Art.299(2) protect an officer from?",
     "Criminal prosecution","Personal liability for contracts made in their official capacity on behalf of Govt — they are not personally liable for bona fide Govt contracts","Tax liability","Election disqualification","b",
     "Art.299(2): No person making or executing any such contract (in their official capacity on behalf of Govt) shall be personally liable in respect of it. Purpose: protect officers from personal suits for bona fide official acts. / Art.299(2): officer not personally liable for bona fide Govt contracts made in official capacity."),
    (0,"hard","Art.300 ప్రకారం State suit ఎవరి పేరిట file చేయబడుతుంది? / Under Art.300, in whose name must a State file or defend a suit?",
     "In the CM's name","In the name of the State itself — 'State of [Name]' (e.g., State of Maharashtra)","In the Governor's name","In the AG's name","b",
     "Art.300: State of [Name] may sue or be sued in name of the State (e.g., 'State of Maharashtra'). Not in the Governor's or CM's personal name. / Art.300: State suit — in name of 'State of [Name]'."),

    # Section 1: Doctrine of Sovereign Immunity (8)
    (1,"easy","Sovereign Immunity doctrine ఏ case లో establish అయింది India లో? / In which case was the Sovereign Immunity doctrine first established in India?",
     "Kasturilal 1965","P&O Steam Navigation Co. v. Secretary of State for India (1861) — Calcutta HC","Vidyawati 1962","Rudul Shah 1983","b",
     "P&O Steam Navigation Co. v. Secretary of State for India (1861), Calcutta HC: First established distinction between sovereign functions (immunity) and non-sovereign/commercial functions (liability) in Indian context. / P&O Case 1861 Calcutta HC: first sovereign vs non-sovereign distinction in India."),
    (1,"medium","Sovereign functions vs Non-sovereign functions distinction ఏమిటి? / What is the distinction between sovereign and non-sovereign functions?",
     "Based on budget allocation","Sovereign = acts of state (army, war, waging peace, legislation) → immunity; Non-sovereign = commercial, trade, maintenance activities → full liability like private person","Based on employee grade","Based on revenue generation","b",
     "Sovereign functions: maintaining army, waging war, foreign affairs, legislative acts → State has immunity. Non-sovereign/commercial functions: trade, maintenance work, running factories, transport → State liable like private person. P&O Case 1861 established this. / Sovereign (immunity): army/war; Non-sovereign (liability): trade/commerce/maintenance."),
    (1,"easy","Kasturilal v. State of UP (1965) case ఏమిటి? / What was the Kasturilal case about?",
     "Railway accident","Police seized gold from a merchant (Kasturilal); police kept/lost the gold through negligence; SC held seizure = sovereign function → State not liable","Custodial death","Road accident by Govt vehicle","b",
     "Kasturilal v. State of UP (1965): Police arrested Kasturilal and seized his gold; police negligence led to gold being lost/unaccounted. SC held: police seizure of property = exercise of sovereign power → State not liable. Criticised as outdated in welfare state. / Kasturilal 1965: police seized gold → sovereign function → State not liable."),
    (1,"hard","Kasturilal case ని critics ఎందుకు criticise చేస్తారు? / Why do critics criticise the Kasturilal decision?",
     "Case decided correctly","Anachronistic in welfare state — where State performs vast activities, blanket immunity is unjust; modern SC cases have narrowed this ruling; 21st Law Commission recommended abolition of sovereign/non-sovereign distinction","Kasturilal won","Decision was criminal, not civil","b",
     "Kasturilal criticism: (1) Anachronistic — welfare state does everything, can't claim blanket immunity; (2) Unjust to victims of State negligence; (3) Later SC cases (Nilabati Behera, D.K. Basu) have effectively limited Kasturilal; (4) 21st Law Commission: recommend abolishing the distinction; (5) UK abolished Crown immunity via Crown Proceedings Act 1947. / Kasturilal: criticised as outdated — welfare state can't have blanket immunity."),
    (1,"medium","UK లో Crown Immunity ఏ Act తో abolish అయింది? / Under which Act was Crown immunity abolished in UK?",
     "Crown Rights Act 1950","Crown Proceedings Act 1947 — Crown (Government) can be sued like any person; sovereign immunity largely abolished in England","Crown Liability Act 1960","Government Torts Act 1945","b",
     "UK: Crown Proceedings Act 1947 abolished Crown (Government) immunity for most torts. In England, the Government can be sued like a private person for most tortious acts. India has no equivalent comprehensive legislation — courts do case-by-case erosion. / UK: Crown Proceedings Act 1947 abolished crown immunity; India: no such comprehensive law."),
    (1,"easy","Sovereign function ఉదాహరణ ఏమిటి? / Which of the following is an example of a sovereign function?",
     "Operating a bus service","Maintaining army and defence of the country","Running a canteen","Constructing a building","b",
     "Sovereign functions examples: maintaining army, waging war, foreign affairs, law-making, police power (maintenance of law and order in its strict sense — but courts have narrowed this). Non-sovereign: bus service, canteen, construction. / Sovereign function: army, war, foreign affairs, law-making — State immune."),
    (1,"hard","Non-sovereign function ఉదాహరణ ఏమిటి? / Which is an example of a non-sovereign function where State is liable?",
     "Waging war","Operating a government-owned passenger bus service — commercial activity → State liable for negligence of driver","Making a law","Foreign treaty","b",
     "Non-sovereign functions: commercial/trade/maintenance activities — government bus, canteen, factory, public works, transport → State liable like private party for negligence. Sovereign: war, army, law-making → immunity. / Non-sovereign: commercial activities like Govt bus, factory → State liable for negligence."),
    (1,"medium","Sovereign immunity doctrine India లో ఎలా evolve అయింది? / How has the sovereign immunity doctrine evolved in India?",
     "Expanded over time","Progressively narrowed by courts — from P&O 1861 broad immunity → Kasturilal 1965 → Vidyawati 1962 (before Kasturilal) → post-1983 constitutional tort remedy → courts limit immunity greatly","No change","Fully abolished by legislation","b",
     "Evolution: (1) P&O 1861: sovereign/non-sovereign distinction; (2) Vidyawati 1962: Govt jeep = non-sovereign → liability; (3) Kasturilal 1965: upheld immunity for police seizure; (4) Post-1983: Rudul Shah, Nilabati Behera, D.K. Basu — constitutional tort bypasses immunity; (5) Today: immunity much narrowed, welfare state liability increasing. / Sovereign immunity: progressively narrowed by Indian courts."),

    # Section 2: Evolution and Erosion of Sovereign Immunity (8)
    (2,"easy","Vidyawati case (1962) ఏమిటి? / What was the Vidyawati case about?",
     "Custodial death","State of Rajasthan v. Vidyawati (1962) — Govt jeep driver's negligence caused road accident and death; SC: driving Govt vehicle = non-sovereign function → State liable","Police seizure of property","Railway accident","b",
     "State of Rajasthan v. Vidyawati (1962): Government jeep driver (on official duty) drove negligently, causing death. SC held: driving a government vehicle for official purpose = non-sovereign (commercial/routine) activity → State liable. First major post-independence SC case restricting sovereign immunity. / Vidyawati 1962: Govt jeep accident → non-sovereign → State liable."),
    (2,"medium","Rudul Shah v. State of Bihar (1983) ఏ principle establish చేసింది? / What principle did Rudul Shah (1983) establish?",
     "Sovereign immunity applies to prisons","SC can award monetary compensation under Art.32 for violation of fundamental rights — constitutional tort; Rudul Shah was illegally detained for 14 years after acquittal; SC awarded compensation","Govt jeep case","Police immunity","b",
     "Rudul Shah v. State of Bihar (1983): Rudul Shah acquitted in 1968 but kept in prison until 1982 (14 years). SC under Art.32: awarded monetary compensation for violation of Art.21 (right to life). Established: SC can award compensation in writ jurisdiction for constitutional torts — bypasses sovereign immunity. / Rudul Shah 1983: first SC compensation award under Art.32 for Fundamental Right violation — constitutional tort."),
    (2,"easy","Nilabati Behera v. State of Orissa (1993) ఏమిటి? / What was Nilabati Behera about?",
     "Environmental pollution","Son of Nilabati Behera died in police custody (custodial death); SC awarded compensation under Art.32 — State liable for custodial death, not a sovereign function","Road accident","Railway compensation","b",
     "Nilabati Behera v. State of Orissa (1993): Nilabati Behera's son died in police custody. SC: State liable for custodial death — awarded compensation under Art.32. Held: sovereign immunity does not protect State from constitutional tort liability when fundamental rights violated. / Nilabati Behera 1993: custodial death → State liable → SC awarded compensation under Art.32."),
    (2,"medium","D.K. Basu v. State of WB (1997) ఏమిటి? / What was D.K. Basu (1997) about?",
     "Environmental guidelines","Custodial torture/death guidelines — SC laid down specific guidelines for arrest, detention, custody; State liable for custodial violence; compensation payable for violation of Art.21","PIL on education","Forest protection","b",
     "D.K. Basu v. State of WB (1997): SC issued detailed guidelines for arrest and detention to prevent custodial violence. Held: custodial violence/death = violation of Art.21; State is liable; compensation must be paid. Not a sovereign function — State cannot claim immunity. / D.K. Basu 1997: custodial violence guidelines; State liable for Art.21 violations in custody."),
    (2,"hard","Chairman Railway Board v. Chandrima Das (2000) ఏమిటి? / What was Chandrima Das (2000) about?",
     "Railway land acquisition","Rape of a Bangladeshi national by railway employees on railway premises; SC: Indian Railways (Union of India) liable; rape by employees on employer's premises = non-sovereign act; compensation awarded","Train derailment","Railway contract","b",
     "Chairman, Railway Board v. Chandrima Das (2000): A Bangladeshi national was raped by railway employees in Howrah Station waiting room. SC held: Indian Railways (Union of India) vicariously liable; running railway stations = non-sovereign commercial function; compensation awarded under Art.226. / Chandrima Das 2000: railway employee rape → Indian Railways liable (non-sovereign commercial function)."),
    (2,"easy","Sebastian Hongray v. Union of India (1984) ఏమిటి? / What was Sebastian Hongray about?",
     "Environmental case","SC awarded exemplary costs (compensation) when two persons taken into Army custody disappeared — disappeared/killed in custody → Army violated Art.21; SC ordered compensation","Land reform case","Election petition","b",
     "Sebastian Hongray v. Union of India (1984): Two persons taken into Army custody in Manipur disappeared. Army could not produce them. SC inferred they were killed in custody. Awarded exemplary costs (compensation) under Art.32 for violation of Art.21. / Sebastian Hongray 1984: persons disappeared in Army custody → SC awarded compensation under Art.32."),
    (2,"medium","'Constitutional Tort' అంటే ఏమిటి? / What is a 'Constitutional Tort'?",
     "Tort under IPC","Violation of fundamental rights by State giving rise to right to compensation directly under Art.32 or Art.226 — bypasses sovereign immunity doctrine","Tort under Contract Act","Only available in civil courts","b",
     "Constitutional Tort: When State violates fundamental rights (especially Art.21 — right to life and liberty), a victim can seek compensation directly from SC (Art.32) or HC (Art.226) without going to civil court. Constitutional tort bypasses sovereign immunity — State cannot claim immunity when it violates FRs. / Constitutional Tort: FR violation → right to compensation under Art.32/226; bypasses sovereign immunity."),
    (2,"hard","21st Law Commission ఏ recommendation ఇచ్చింది sovereign immunity పై? / What did the 21st Law Commission recommend on sovereign immunity?",
     "Expand sovereign immunity","Abolish the sovereign/non-sovereign distinction — State should be liable for all tortious acts of its employees regardless of nature of function; recommend enactment of a Government Liability Act","Maintain status quo","Only abolish for criminal cases","b",
     "21st Law Commission (period around 2016-18): recommended abolishing the outdated sovereign/non-sovereign distinction in India. Recommended enacting a Government Liability Act making State liable for all tortious acts of employees, regardless of whether function is sovereign or non-sovereign. / 21st Law Commission: abolish sovereign/non-sovereign distinction; enact Government Liability Act."),

    # Section 3: Government Contracts (Art.299) (8)
    (3,"easy","Art.299 ప్రకారం valid Govt contract కోసం ఎన్ని essentials ఉన్నాయి? / How many essentials are there for a valid Govt contract under Art.299?",
     "Two","Three — (1) expressed in name of President/Governor; (2) executed by duly authorised person; (3) must be in writing","Four","Five","b",
     "Art.299 essentials: (1) Contract expressed to be made by the President (Union) or Governor (State); (2) Executed by a person duly authorised by President/Governor; (3) Must be in writing. All 3 must be satisfied for Government to be bound. / Art.299: 3 essentials — expressed by P/G + authorised person + writing."),
    (3,"medium","Art.299(1) formalities comply చేయని officer ఏమవుతారు? / What happens to an officer who fails to comply with Art.299(1) formalities?",
     "Officer gets protection","Officer may be personally liable for the contract — the Govt is not bound; the other party can sue the officer personally but not the Govt","Govt still bound","Contract automatically void","b",
     "If Art.299(1) formalities not followed: (1) Govt is not bound by the contract; (2) The contract cannot be enforced against Govt; (3) The officer who entered into the contract may be personally liable; (4) The other contracting party can sue the officer personally. / Art.299 breach: Govt not bound; officer personally liable to other party."),
    (3,"easy","Govt contract writing లో ఉండకపోతే ఏమవుతుంది? / What if a Govt contract is not in writing?",
     "Still valid","Not enforceable against the Government — writing is a mandatory requirement under Art.299","Can be ratified later","Valid if both parties agree","b",
     "Art.299 requirement: Government contract MUST be in writing. If not in writing → Government is not bound → Contract not enforceable against Govt. This is a mandatory constitutional requirement. / Art.299: writing mandatory for Govt contract; oral contract not enforceable against Govt."),
    (3,"medium","Government contract 'executive capacity లో' execute అవ్వాలంటే ఏమిటి అర్థం? / What does 'executed in executive capacity' mean for Govt contracts?",
     "Executed by minister personally","Executed by an officer duly authorised by President/Governor — following proper delegation of authority chain within Govt","Executed only by Secretary","Executed by courts","b",
     "Art.299 — executed by authorised person: The officer signing the contract must have been specifically authorised by the President (for Union contracts) or Governor (for State contracts). The authorisation can be by rules, order, or circular. Unauthorised officer's signature → Govt not bound. / Art.299: contract must be executed by officer duly authorised by President/Governor."),
    (3,"hard","Art.299 ఎందుకు Government ని contracts లో protect చేస్తుంది? / Why does Art.299 protect the Government in contracts?",
     "To make contracts difficult","To prevent ultra-vires contracts binding Govt: ensures only authorised officers can bind Govt; formalities prevent fraud/forgery; protects public funds; prevents officers from exceeding authority and binding Govt in unauthorised ways","To help private parties","To ensure taxation","b",
     "Rationale of Art.299: (1) Prevents unauthorised officers from binding Govt; (2) Protects public funds from unauthorised expenditure; (3) Prevents fraud — formal written contracts with authorised signatures are harder to forge; (4) Creates accountability — clear who authorised what; (5) Distinguishes Govt contracts from private ones. / Art.299 purpose: prevent ultra-vires/unauthorised contracts from binding Govt; protect public funds."),
    (3,"easy","Govt contract లో 'written' requirement ఎందుకు ఉంది? / Why is the 'writing' requirement in Art.299?",
     "For tax records","To ensure clarity, prevent disputes, and maintain records — written contracts create clear evidence of terms; prevents fraudulent claims against Govt","To delay contracts","Oral is cheaper","b",
     "Writing requirement in Art.299: (1) Creates clear evidence of terms and conditions; (2) Prevents disputes about what was agreed; (3) Maintains government records/accountability; (4) Prevents fraudulent claims (oral agreements hard to verify); (5) Ensures proper formality for Govt commitments. / Art.299 writing: clarity + evidence + accountability + fraud prevention."),
    (3,"medium","Art.299 ని violate చేసిన officer ని Govt protect చేస్తుందా? / Does the Government protect an officer who violates Art.299?",
     "Always protects","No — Art.299(2) protects officers only for contracts made properly in official capacity. If officer violates Art.299(1), officer is personally liable; Govt protection (Art.299(2)) doesn't apply","Always officer protected","Govt must pay instead","b",
     "Art.299(2) protection: applies only when officer properly follows Art.299(1) formalities (expressed as Govt contract, duly authorised). If officer violates Art.299(1) — not following formalities — Art.299(2) protection doesn't apply → officer personally liable. / Art.299(2): officer protected only if properly followed formalities; breach → officer personally liable."),
    (3,"hard","Government contract law related ఏ English case relevant? / Which English case principle is relevant to Govt contract law?",
     "Donoghue v. Stevenson","Fibrosa v. Fairbairn — frustration of contract; and Secretary of State for India cases established that Govt contracts must follow constitutional formalities; 'executive necessity' doctrine says Govt cannot be estopped from exercising statutory powers","Donoghue principle","Rylands v. Fletcher","b",
     "Govt contract doctrine: (1) Executive necessity — Govt cannot by contract fetter its future legislative/executive discretion; (2) Govt not estopped from exercising statutory powers by prior contract; (3) Promissory estoppel may apply in limited cases (Motilal Sugar Mills v. State of UP). / Govt contracts: Govt cannot fetter future discretion; promissory estoppel applies in limited cases."),

    # Section 4: Government Property and Torts (8)
    (4,"easy","Welfare state లో sovereign immunity anachronistic ఎందుకు? / Why is sovereign immunity anachronistic in a welfare state?",
     "Sovereign states are perfect","Welfare state performs vast range of activities (health, education, transport, housing) beyond traditional sovereign acts — blanket immunity unjust for routine activities causing harm to citizens","Welfare state has no police","Colonial era","b",
     "Welfare state problem: Traditional sovereign immunity was designed for limited night-watchman state (only war, police, courts). Modern welfare state does health care, education, transport, housing, factories — all potentially causing harm. Blanket immunity unjust. Citizens left remediless. / Welfare state: vast activities → blanket sovereign immunity anachronistic and unjust."),
    (4,"medium","India లో Govt torts కి comprehensive legislation ఉందా? / Does India have comprehensive legislation for Government torts?",
     "Yes — Govt Liability Act 2001","No comprehensive legislation — unlike UK (Crown Proceedings Act 1947); India relies on case-by-case judicial evolution; constitutional tort under Art.32/226","Yes — Civil Liability Act 2010","Yes — Tort Reform Act 1995","b",
     "India: No comprehensive Government Liability Act. Unlike UK (Crown Proceedings Act 1947) which abolished Crown immunity, India has no such law. Indian courts have done case-by-case erosion of sovereign immunity. Constitutional tort under Art.32/226 is the main remedy. 21st Law Commission recommended a Government Liability Act. / India: no comprehensive Govt liability law; courts do case-by-case erosion; constitutional tort under Art.32/226."),
    (4,"easy","Government employee negligence లో vicarious liability apply అవుతుందా? / Does vicarious liability apply to Govt for employee negligence?",
     "Never applies","Yes — for non-sovereign functions; Govt (employer) vicariously liable for negligence of its employees (servants) in course of non-sovereign duties; like private employer-employee relationship","Only for IAS officers","Only for police","b",
     "Vicarious liability: Govt can be vicariously liable for torts of its employees in non-sovereign functions — same as private employer for employee's negligence in course of employment. Chandrima Das 2000: Indian Railways vicariously liable for rape by railway employees. / Vicarious liability: Govt liable for employee negligence in non-sovereign functions."),
    (4,"medium","Tort liability లో 'negligence per se' కి example ఏమిటి? / What is an example of 'negligence per se' in Govt liability?",
     "Policy decision error","Government hospital — doctor's negligence causing patient death/injury — State Hospital running = non-sovereign function → State vicariously liable for doctor's negligence","Army promotion decision","Tax assessment error","b",
     "Government hospital negligence: Running a government hospital = non-sovereign/welfare function → State vicariously liable for negligent treatment by doctors. Patient injury due to doctor's negligence → State pays compensation. Distinguished from policy decisions (immunised). / Govt hospital doctor negligence: non-sovereign → State vicariously liable for medical negligence."),
    (4,"hard","'Absolute Liability' doctrine Govt ని కూడా apply అవుతుందా? / Does 'Absolute Liability' doctrine apply to the Government?",
     "Never applies to Govt","Yes — MC Mehta case established absolute liability for inherently dangerous enterprises; if Govt runs inherently dangerous enterprise causing harm → absolute liability regardless of sovereign/non-sovereign distinction","Only private companies","Only nuclear plants","b",
     "Absolute Liability (MC Mehta v. Union of India 1987 / Oleum Gas Leak): SC established: enterprises engaged in inherently dangerous/hazardous activities strictly liable without exception for escape of hazardous material. If Govt runs such enterprise → absolute liability. Goes beyond Rylands v. Fletcher — no exceptions. / Absolute Liability (MC Mehta 1987): inherently dangerous enterprise → Govt absolutely liable; no immunity."),
    (4,"easy","Government property ని damage చేసిన person ని sue చేయవచ్చా? / Can the Government sue a person who damages Government property?",
     "No, Govt cannot sue","Yes — Govt can sue any person for damages to Govt property in civil courts; files suit as Union of India/State of [Name]","Only criminal action possible","Only through police","b",
     "Government can sue: Govt has same right as private citizen to sue for (1) damage to Govt property; (2) breach of contract; (3) recovery of dues; (4) tortious damage. Files suit as 'Union of India' or 'State of [Name]' in civil courts. / Govt can sue: for property damage, contract breach, recovery of dues, like any private person."),
    (4,"medium","Strict liability Govt ని apply అవుతుందా? / Does strict liability apply to the Government?",
     "Never applies","Yes — for non-sovereign activities; Rylands v. Fletcher principle: if Govt accumulates something dangerous on land that escapes and causes harm → strictly liable (no immunity for non-sovereign activities)","Only if Government consents","Only for State Govt","b",
     "Strict liability (Rylands v. Fletcher): If Govt brings onto land anything likely to do mischief if it escapes, and it does escape → strictly liable. Applies to Govt for non-sovereign activities. MC Mehta elevated to Absolute Liability for inherently dangerous activities. / Strict liability: Rylands principle applies to Govt non-sovereign activities."),
    (4,"hard","Policy decisions vs Operational failures — distinguish చేయి? / Distinguish between policy decisions and operational failures in Govt liability.",
     "Both attract same liability","Policy decisions (high-level discretionary choices on how to govern) → generally immunised from tort liability (non-justiciable); Operational failures (implementing the policy negligently) → State liable; 'policy-operational' distinction used in negligence","Both immune","Both attract liability","b",
     "Policy vs Operational: (1) Policy: high-level government decisions on what to do (e.g., whether to build a hospital, what standards to set) → courts reluctant to second-guess, generally immune; (2) Operational: how the policy is implemented (e.g., negligent driving, doctor's negligence in Govt hospital) → State liable. / Policy = immune (discretionary); Operational = State liable (negligent implementation)."),

    # Section 5: Suits Against Government (8)
    (5,"easy","CPC Section 80 ఏమిటి? / What does CPC Section 80 provide?",
     "Stay of Govt suits","2-month notice required before filing civil suit against Central or State Government or any public officer in official capacity; failure to give notice → suit not maintainable","6-month notice","1-year notice","b",
     "CPC Section 80: Before filing any civil suit against (1) Central Govt, (2) State Govt, (3) any public officer in their official capacity — must give 2-month written notice. Notice must specify: cause of action, relief sought, plaintiff's name and address. Failure → suit not maintainable. / CPC Sec.80: 2-month notice before suing Govt; failure = suit not maintainable."),
    (5,"medium","CPC Sec.80 notice లో ఏమేమి specify చేయాలి? / What must be specified in a CPC Sec.80 notice?",
     "Only plaintiff's name","Cause of action + relief sought + name and address of plaintiff/claimant; complete notice enables Govt to consider settling before litigation","Only amount claimed","Only date of incident","b",
     "CPC Sec.80 notice contents: (1) Cause of action — what wrong was done; (2) Relief sought — what the plaintiff wants (money, injunction, declaration); (3) Name and address of the plaintiff; (4) Description of the wrong. Purpose: give Govt opportunity to settle before litigation. / Sec.80 notice: cause of action + relief sought + name/address of plaintiff."),
    (5,"easy","Urgent cases లో Sec.80 notice ఇవ్వకపోవచ్చా? / Can Sec.80 notice be waived in urgent cases?",
     "Never waived","Yes — 2002 Amendment to CPC: courts may allow suit without prior notice in urgent cases if the court is satisfied it is so urgent; court gives leave to sue without notice","Always waived","Only if Govt agrees","b",
     "CPC Sec.80 — 2002 Amendment: Courts may allow urgent suits without prior 2-month notice if plaintiff satisfies court it is urgent (e.g., impending destruction of property, urgent injunction needed). Court gives leave to file without notice. Purpose: balance Govt protection vs urgent justice. / 2002 CPC Amendment: urgent cases — court can allow suit without Sec.80 notice."),
    (5,"medium","Sec.80 notice failure ఏ consequence ఉంది? / What is the consequence of failing to give Sec.80 notice?",
     "Reduced compensation only","Suit is not maintainable — court will dismiss/reject the suit on this ground alone; plaintiff must start afresh with proper notice","Only penalty payable","Delay in trial only","b",
     "Failure to give Sec.80 notice: Suit is NOT maintainable. Court dismisses the suit. The plaintiff must: (1) Give proper 2-month notice; (2) Wait 2 months; (3) Then file fresh suit. Courts have strictly enforced this requirement. / Sec.80 failure: suit not maintainable; plaintiff must restart with proper 2-month notice."),
    (5,"hard","Sec.80 notice ఏ purpose serve చేస్తుంది? / What purpose does Sec.80 notice serve?",
     "Delay tactics only","Gives Govt opportunity to (1) investigate the claim; (2) settle the matter without litigation; (3) take corrective action; (4) prepare defence; reduces unnecessary litigation against Govt","Only revenue purposes","Only historical","b",
     "Purpose of Sec.80 notice: (1) Government can investigate the claim and take corrective action; (2) Government can settle the matter before litigation (avoids court costs); (3) Government can prepare a proper defence; (4) Reduces unnecessary/frivolous litigation against Govt. But has been criticised as causing unnecessary delay for genuine claimants. / Sec.80 notice purpose: give Govt chance to settle/correct before litigation."),
    (5,"easy","Govt suit లో Attorney General ఏ role పోషిస్తారు? / What role does the Attorney General play in Govt suits?",
     "AG decides all Govt suits","AG is the primary law officer of Union of India — represents Union in SC cases; gives legal advice to Govt; assists in Govt suits before SC; AGs of States represent respective State Governments in HC","AG decides damages","AG signs all notices","b",
     "Attorney General of India: primary law officer of Union of India (Art.76). Represents Union in Supreme Court. Assists Govt in important litigation. Advocates General represent State Governments in respective High Courts. / AG: represents Union of India in SC; Advocates General represent States in HCs."),
    (5,"medium","Government suit కి Limitation Act apply అవుతుందా? / Does Limitation Act apply to Government suits?",
     "No — Govt has no limitation","Yes — Limitation Act 1963 applies to Govt suits too (historically Govt had longer limitation periods but now standardised); Govt must file suits within prescribed limitation periods","Govt has 30 years always","Only foreign limitation","b",
     "Limitation Act applies to Govt: The Limitation Act 1963 applies to Government suits. Earlier, Govt had longer limitation periods (30 years for some). Now limitation periods more standardised. Govt must file suits within prescribed time — contract suits within 3 years, property suits within 12 years (generally). / Limitation Act: applies to Govt suits; Govt must file within prescribed limitation periods."),
    (5,"hard","Govt ని sue చేయడం లో 'doctrine of estoppel' apply అవుతుందా? / Does the 'doctrine of estoppel' apply when suing the Government?",
     "Always applies fully","Limited application — Govt cannot be estopped from performing statutory duties/exercising statutory powers; BUT promissory estoppel may apply if Govt makes a clear and unambiguous promise, person acts in reliance, detriment results (Motilal Sugar Mills principle)","Never applies","Only in contract cases","b",
     "Estoppel against Govt: (1) Cannot estop Govt from performing statutory duties; (2) Cannot estop Govt from exercising legislative powers; (3) BUT Promissory Estoppel: if Govt makes clear promise, person acts in reliance to their detriment → Govt may be estopped (Motilal Sugar Mills v. State of UP, 1979). Limited to executive actions, not legislative. / Promissory estoppel against Govt: limited — applies to executive promises if reliance + detriment; not to legislative acts."),

    # Section 6: Special Protections and Privileges (8)
    (6,"easy","Art.361 President ని ఏ నుండి protect చేస్తుంది? / What does Art.361 protect the President from?",
     "Parliamentary impeachment","Criminal proceedings and civil proceedings during term — no criminal proceedings against President/Governor during term; 2-month notice for civil proceedings; no arrest/imprisonment during term","Tax obligations","International law","b",
     "Art.361: (1) President and Governors NOT answerable to any court for exercise of their powers/duties; (2) No criminal proceedings against President/Governor during term; (3) No arrest or imprisonment during term; (4) Civil proceedings: 2-month notice required. Art.361 does NOT protect from Parliamentary impeachment. / Art.361: President/Governor — no criminal proceedings during term; 2-month notice for civil suits."),
    (6,"medium","Art.361 vs Parliamentary Privilege తేడా ఏమిటి? / How is Art.361 different from Parliamentary Privilege?",
     "Same as Parliamentary Privilege","Art.361: Executive immunity — protects President/Governor from courts during term; Parliamentary Privilege (Art.105/194): Legislative immunity — protects MP/MLA from courts for things said/voted in House; different in nature and scope","Art.361 is subset of Art.105","No difference","b",
     "Art.361 vs Parliamentary Privilege: (1) Art.361 = Executive immunity for President/Governor; (2) Art.105/194 = Parliamentary Privilege for MPs/MLAs for legislative proceedings; (3) Art.361: protects from criminal/civil proceedings during term; (4) Art.105: protects from courts for parliamentary speeches/votes. Different in subject matter and scope. / Art.361: Executive immunity; Art.105/194: Parliamentary Privilege — different in nature."),
    (6,"easy","Indian Evidence Act Section 123 ఏమిటి? / What does Section 123 of Indian Evidence Act provide?",
     "Expert witness rules","Unpublished official records — state affairs documents — not to be given in evidence without permission of head of department/minister; government privilege against disclosure of state secrets","Hearsay rule","Document authentication","b",
     "Evidence Act Sec.123: Unpublished official records relating to state affairs shall not be given in evidence — privilege claimed by the head of the department (minister). Public interest immunity: court can inspect the document to decide whether to uphold the privilege. Balance: public interest in disclosure vs public interest in secrecy. / Evidence Act Sec.123: Govt privilege against disclosure of state affairs documents."),
    (6,"medium","Evidence Act Sec.123 claim చేసిన తరువాత court ఏమి చేయవచ్చు? / What can the court do after a Sec.123 privilege claim?",
     "Must accept privilege always","Court can inspect the document itself to decide whether to uphold the privilege; court balances public interest in disclosure vs public interest in maintaining secrecy; court is not bound by Govt's claim","Must reject privilege always","Must refer to President","b",
     "Court's role in Sec.123 privilege: (1) Court can inspect the document in camera (privately); (2) Court balances: public interest in justice/disclosure vs public interest in confidentiality; (3) Court is NOT bound by government's assertion — has independent power to decide; (4) If public interest in disclosure outweighs secrecy → court can order disclosure. / Sec.123: court can inspect document; not bound by Govt's privilege claim; balances competing public interests."),
    (6,"hard","Art.361 Governor ని ఏమి నుండి protect చేయదు? / What does Art.361 NOT protect the Governor from?",
     "Civil suits during term","Personal acts outside official capacity — Art.361 protects only for exercise of powers/duties of office; personal acts (not done as Governor) not protected; also doesn't protect from Removal by President (Art.156), or HC jurisdiction on certain matters","Official decisions","Policy matters","b",
     "Art.361 does NOT protect: (1) Personal acts of Governor unconnected with official duties; (2) Doesn't prevent Removal by President under Art.156; (3) SC examination in exceptional circumstances (B.P. Singhal case 2010 — removal of Governors examined by SC); (4) Post-term liability for official acts (debate exists). / Art.361: protects official acts; NOT personal acts; doesn't prevent Presidential removal or SC review."),
    (6,"easy","Evidence Act Sec.124 ఏమిటి? / What does Evidence Act Section 124 provide?",
     "Expert evidence","Official communications — any public officer may claim privilege against disclosing official communications if disclosure would be against public interest; head of department decides","Witness immunity","Criminal evidence","b",
     "Evidence Act Sec.124: No public officer shall be compelled to disclose communications made to him in official confidence when he considers that the public interests would suffer by the disclosure. More general than Sec.123 (which covers state affairs documents specifically). / Evidence Act Sec.124: public officers can claim privilege against disclosing official communications in public interest."),
    (6,"medium","Art.361 లో civil proceedings కి notice ఎంత? / What notice is required for civil proceedings against President/Governor under Art.361?",
     "No notice needed","2-month notice required before civil proceedings against President/Governor; no arrest or imprisonment during term; same as Sec.80 CPC but specified in Constitution itself for President/Governor","1-month notice","6-month notice","b",
     "Art.361 civil proceedings: Before civil proceedings against President/Governor — 2-month notice required. No arrest or imprisonment during term. Suit can proceed after notice period. President/Governor personally (in individual capacity) can be sued — Art.361 protects them in their official capacity but not personal capacity (debated). / Art.361: 2-month notice for civil proceedings against President/Governor during term."),
    (6,"hard","Art.361 President ని ఏ court accountability నుండి fully protect చేస్తుందా? / Does Art.361 fully protect the President from all court accountability?",
     "Yes, total immunity forever","No — not full immunity: (1) Post-term: personal acts may be liable; (2) Art.361 ≠ protection from impeachment (Parliament's power — Art.61); (3) Courts can review Presidential proclamations under Art.356 (S.R. Bommai 1994); (4) Art.361 protects exercise of powers, not legislative power of President to promulgate ordinances (Art.123) — courts review ordinances","Yes — even after term","Yes, from all courts","b",
     "Art.361 limitations: (1) NOT total immunity — Parliament can impeach under Art.61; (2) Courts can review Presidential proclamations (Art.356 — S.R. Bommai); (3) Presidential ordinances (Art.123) reviewed by courts; (4) Post-term personal liability possible; (5) Art.361 covers exercise of 'powers and duties' not all actions. / Art.361: substantial but NOT total immunity; Parliament impeach, courts review proclamations/ordinances."),

    # Section 7: Key Facts (8)
    (7,"easy","Art.299 ఏ chapter లో ఉంది? / In which part of the Constitution is Art.299?",
     "Part III","Part XII — Finance, Property, Contracts and Suits (Art.264-300A)","Part IV","Part VI","b",
     "Art.299 and Art.300 are in Part XII of the Constitution — Finance, Property, Contracts and Suits (Art.264-300A). This Part deals with financial matters, property rights, government contracts, and suits. / Art.299-300: Part XII of Constitution — Finance, Property, Contracts and Suits."),
    (7,"medium","P&O Case ఏ court లో decided అయింది ఏ year లో? / In which court and year was the P&O case decided?",
     "SC Delhi 1950","Calcutta High Court, 1861 — P&O Steam Navigation Co. v. Secretary of State for India; established sovereign/non-sovereign distinction","Bombay HC 1900","Madras HC 1885","b",
     "P&O Steam Navigation Co. v. Secretary of State for India: Decided by Calcutta High Court (then Calcutta Supreme Court) in 1861. This pre-independence case established the foundational sovereign/non-sovereign functions distinction that has shaped Indian Govt liability law. / P&O Case: Calcutta HC, 1861 — sovereign/non-sovereign distinction."),
    (7,"easy","Rudul Shah case ఏ year లో? / In which year was the Rudul Shah case decided?",
     "1975","1983 — Rudul Shah v. State of Bihar; first SC monetary compensation award under Art.32 for FR violation (14 years illegal detention after acquittal)","1990","2000","b",
     "Rudul Shah v. State of Bihar (1983): SC's landmark decision awarding compensation under Art.32. Rudul Shah was acquitted in 1968 but detained until 1982 — 14 years of illegal imprisonment. SC awarded Rs.35,000 as compensation. First constitutional tort compensation in India. / Rudul Shah 1983: first SC compensation under Art.32 for FR violation."),
    (7,"medium","Kasturilal v. State of UP ఏ year లో? / In which year was Kasturilal decided?",
     "1960","1965 — Kasturilal Ralia Ram Jain v. State of UP; SC upheld sovereign immunity for police seizure of property (gold merchant's case)","1972","1980","b",
     "Kasturilal Ralia Ram Jain v. State of UP (1965): SC held police seizure = sovereign function → State not liable. This is the last major case where SC broadly upheld sovereign immunity. Since then, courts have progressively narrowed immunity. Criticised as anachronistic. / Kasturilal: 1965; last major SC case upholding broad sovereign immunity."),
    (7,"easy","CPC Sec.80 notice period ఎంత? / What is the notice period under CPC Section 80?",
     "1 month","2 months — 2-month written notice must be given before suing Central/State Govt or public officer in official capacity","3 months","6 months","b",
     "CPC Section 80: 2-month notice mandatory before filing suit against: (1) Central Government; (2) State Government; (3) Public officer in official capacity. Notice must specify cause of action, relief sought, name/address of plaintiff. 2002 Amendment: urgent cases — court can waive notice. / Sec.80: 2-month notice before suing Govt; mandatory except urgent cases with court permission."),
    (7,"medium","Vidyawati case ఏ State involved? / Which State was involved in the Vidyawati case?",
     "Uttar Pradesh","Rajasthan — State of Rajasthan v. Vidyawati (1962); Govt jeep driver's negligence caused accident and death; SC: non-sovereign function → Rajasthan State liable","Bihar","Maharashtra","b",
     "State of Rajasthan v. Vidyawati (1962): Rajasthan State Government. A government jeep on official duty driven negligently → accident → death. SC held driving govt vehicle = non-sovereign function → State of Rajasthan liable. First major post-independence SC restriction on sovereign immunity. / Vidyawati 1962: State of Rajasthan; Govt jeep negligence → State liable."),
    (7,"hard","Art.300 ఏ predecessor article ని replace చేసింది? / Which predecessor provision did Art.300 replace?",
     "Govt of India Act 1919 Sec.32","Govt of India Act 1935 Sec.176 and earlier provisions — Secretary of State in Council (British) → Dominion of India (1947) → Union of India (1950); Art.300 preserves continuity of the right to sue/be sued","Constitution (First Amendment)","Art.14 principle","b",
     "Art.300 succession: British India → Secretary of State in Council could be sued; Govt of India Act 1935 Sec.176 provided for suits; 1947: Secretary of State → Dominion of India; 1950: Dominion → Union of India. Art.300 of Constitution continued this tradition of Government being suable. / Art.300: successor to pre-1947 Secretary of State/Dominion → Union of India litigation continuity."),
    (7,"medium","Chairman Railway Board v. Chandrima Das case ఏ year లో? / In which year was the Chandrima Das case?",
     "1995","2000 — Chairman, Railway Board v. Chandrima Das; rape by railway employees on railway premises; SC: Indian Railways (Union of India) vicariously liable; non-sovereign commercial function","1985","2010","b",
     "Chairman, Railway Board v. Chandrima Das (2000): Bangladeshi national raped by railway employees at Howrah Station. SC held Indian Railways (Union of India) vicariously liable — railway stations/operations = non-sovereign commercial function. State cannot claim immunity. Compensation awarded. / Chandrima Das: 2000; Indian Railways liable for rape by employees — non-sovereign commercial function."),
]

def _seed_polity_ch76_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres=False, force=False):
    import datetime as _dt
    ph = "%s" if use_postgres else "?"
    existing = row_to_dict_fn(db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE topic={ph} AND chapter_num={ph}",
        ('Indian_Polity', 76)).fetchone() or {})
    if existing and not force:
        return existing.get('id')
    if existing:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE topic={ph} AND chapter_num={ph}",
            ('Indian_Polity', 76))
    now = _dt.datetime.utcnow().isoformat()
    cur = db_exec_fn(conn,
        f"""INSERT INTO study_notes
            (subject, topic, chapter_num, chapter_title_te, chapter_title_en,
             pages_ref, sections_json, created_at)
            VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
        ('GK', 'Indian_Polity', 76,
         'ప్రభుత్వ హక్కులు-బాధ్యతలు',
         'Rights and Liabilities of the Government',
         'Lakshmikanth Ch.76',
         '[]', now))
    return cur.lastrowid
def _seed_polity_ch76_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres=False, force=False):
    import datetime as _dt
    ph = "%s" if use_postgres else "?"
    _TOPIC = 'Indian_Polity'
    _CH = 76
    note_id = row_to_dict_fn(db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE topic={ph} AND chapter_num={ph}",
        (_TOPIC, _CH)).fetchone() or {}).get('id')
    if not note_id:
        return
    existing = list(db_exec_fn(conn,
        f"SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id={ph}",
        (note_id,)).fetchone() or [0])[0]
    if existing and not force:
        return
    if existing:
        db_exec_fn(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    now = _dt.datetime.utcnow().isoformat()
    for (sec, diff, q, a, b, c, d, ans, exp) in _MCQ_DATA:
        db_exec_fn(conn,
            f"""INSERT INTO chapter_mcqs
                (study_note_id, section_idx, difficulty, exam_type,
                 q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te, created_at)
                VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
            (note_id, sec, diff, 'General', q, a, b, c, d, ans, exp, now))
def seed_polity_ch76(conn, db_exec_fn, row_to_dict_fn, use_postgres=False, force=False):
    _seed_polity_ch76_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force)
    _seed_polity_ch76_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force)
