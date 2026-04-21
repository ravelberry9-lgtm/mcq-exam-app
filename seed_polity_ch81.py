"""
App Ch81 = Book Ch78: Election Laws
(RPA 1950, RPA 1951, Conduct of Elections Rules 1961, and related statutes)
Lakshmikanth Indian Polity – seed file
64 MCQs × 8 sections, 1 study note
"""

NOTES_HTML = """<!DOCTYPE html>
<html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">
<title>Ch81 – Election Laws</title>
<style>
body{margin:0;font-family:'Segoe UI',sans-serif;background:#f5f5f5;color:#212121}
.hdr{background:linear-gradient(135deg,#37474f,#546e7a);color:#fff;padding:32px 24px;text-align:center}
.hdr h1{margin:0;font-size:1.6rem}.hdr p{margin:4px 0 0;opacity:.85;font-size:.95rem}
.wrap{max-width:860px;margin:0 auto;padding:16px}
.sh{background:#546e7a;color:#fff;padding:10px 16px;border-radius:6px;margin:20px 0 10px;font-size:1rem;font-weight:700}
.c{background:#fff;border-radius:8px;padding:14px 16px;margin-bottom:10px;box-shadow:0 1px 4px rgba(0,0,0,.08);border-left:5px solid #607d8b}
.c.b{border-left-color:#1565c0}.c.a{border-left-color:#2e7d32}.c.r{border-left-color:#b71c1c}
.c.p{border-left-color:#4a148c}.c.g{border-left-color:#e65100}.c.gr{border-left-color:#37474f}.c.t{border-left-color:#00695c}
.c h3{margin:0 0 6px;font-size:.97rem;color:#37474f}.c.b h3{color:#1565c0}.c.a h3{color:#2e7d32}.c.r h3{color:#b71c1c}
.c.p h3{color:#4a148c}.c.g h3{color:#e65100}.c.t h3{color:#00695c}
.fact{margin:4px 0;font-size:.9rem;line-height:1.55}.fact::before{content:"• "}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}
.pill{background:#eceff1;color:#37474f;border-radius:20px;padding:4px 12px;font-size:.82rem;font-weight:600}
</style></head><body>
<div class=\"hdr\"><h1>⚖️ Election Laws</h1>
<p>App Chapter 81 &nbsp;|&nbsp; Lakshmikanth Book Ch78</p></div>
<div class=\"wrap\">

<div class=\"sh\">0. Overview of Election Laws</div>
<div class=\"c p\"><h3>Key Election Laws</h3>
<p class=\"fact\">Representation of People Act 1950 (RPA 1950): Electoral rolls, delimitation of constituencies, allocation of seats</p>
<p class=\"fact\">Representation of People Act 1951 (RPA 1951): Conduct of elections, qualifications/disqualifications, corrupt practices, election petitions</p>
<p class=\"fact\">Conduct of Elections Rules 1961: Procedure for conduct of elections (derived from RPA 1951)</p>
<p class=\"fact\">Election Symbols (Reservation and Allotment) Order 1968: Symbol allotment</p>
<p class=\"fact\">Model Code of Conduct (MCC): Non-statutory code enforced by ECI</p>
<p class=\"fact\">Presidential and Vice-Presidential Elections Act 1952</p>
<p class=\"fact\">Government of NCT of Delhi Act 1991, Puducherry Government Act 1963: UT elections</p></div>
<div class=\"c b\"><h3>Constitutional Basis</h3>
<p class=\"fact\">Art.327: Parliament may legislate on all aspects of elections to Parliament and State Legislatures</p>
<p class=\"fact\">Art.328: State Legislatures may legislate for their own elections (within Art.327 framework)</p>
<p class=\"fact\">Art.324: ECI — superintendence, direction and control of elections</p>
<p class=\"fact\">Art.329: Bar to court interference in elections</p></div>

<div class=\"sh\">1. RPA 1950 — Electoral Rolls</div>
<div class=\"c r\"><h3>RPA 1950 Key Provisions</h3>
<p class=\"fact\">RPA 1950: deals with allocation of seats in Parliament and State Legislatures, delimitation of constituencies, and preparation of electoral rolls</p>
<p class=\"fact\">Electoral Registration Officers (ERO): appointed by ECI for each constituency; prepare and maintain electoral rolls</p>
<p class=\"fact\">Qualifying date for electoral roll: January 1 of the year</p>
<p class=\"fact\">Voter eligibility: 18+ years, Indian citizen, ordinarily resident in constituency</p>
<p class=\"fact\">Service voters: armed forces personnel; can register in home constituency or service constituency</p></div>
<div class=\"c g\"><h3>Overseas Voters (NRIs)</h3>
<p class=\"fact\">RPA (Amendment) Act 2010: NRIs can register as voters in their home constituency</p>
<p class=\"fact\">NRI must be: Indian citizen + passport holder + ordinary residence abroad for employment/education/other reasons</p>
<p class=\"fact\">Must register at their address in India (home constituency)</p>
<p class=\"fact\">Can vote only by being present in person (postal ballot pilot later introduced)</p></div>

<div class=\"sh\">2. RPA 1951 — Conduct of Elections</div>
<div class=\"c a\"><h3>RPA 1951 Key Provisions</h3>
<p class=\"fact\">Sec.8: Disqualification for conviction — 6 years from release for sentence 2+ years</p>
<p class=\"fact\">Sec.9: Disqualification for government contracts, etc.</p>
<p class=\"fact\">Sec.10: Disqualification for office in government company</p>
<p class=\"fact\">Sec.29A: Registration of political parties</p>
<p class=\"fact\">Sec.33: Nomination of candidates</p>
<p class=\"fact\">Sec.34: Deposit of security — candidate deposits Rs.25,000 (LS/RS) or Rs.12,500 (State)</p>
<p class=\"fact\">Sec.62: Right to vote in elections</p>
<p class=\"fact\">Sec.77: Account of election expenses by candidates</p>
<p class=\"fact\">Sec.78: Lodging of account within 30 days</p>
<p class=\"fact\">Sec.80A: High Court to try election petitions</p>
<p class=\"fact\">Sec.100: Grounds for declaring election void</p>
<p class=\"fact\">Sec.123: Corrupt practices</p>
<p class=\"fact\">Sec.126A: Exit poll ban during voting period</p>
<p class=\"fact\">Sec.151A: By-election within 6 months</p></div>

<div class=\"sh\">3. Corrupt Practices (Sec.123)</div>
<div class=\"c t\"><h3>Eight Corrupt Practices under Sec.123</h3>
<p class=\"fact\">1. Bribery: giving/offering gratification to voters/candidates</p>
<p class=\"fact\">2. Undue influence: direct/indirect interference with free exercise of electoral right</p>
<p class=\"fact\">3. Appeal on grounds of religion, race, caste, community, language</p>
<p class=\"fact\">4. Use of religious/national symbols to further prospects</p>
<p class=\"fact\">5. Publication of false statements about candidate's personal character</p>
<p class=\"fact\">6. Hiring/procuring vehicles for conveyance of voters within 2km of polling station</p>
<p class=\"fact\">7. Incurring election expenses in excess of prescribed limit</p>
<p class=\"fact\">8. Obtaining assistance of government servants (booth capturing also included)</p></div>
<div class=\"c p\"><h3>Election Offences (Sec.125-136)</h3>
<p class=\"fact\">Sec.125: Promoting enmity between classes — imprisonment up to 3 years</p>
<p class=\"fact\">Sec.126: Holding public meeting within 48 hours before polling — prohibited</p>
<p class=\"fact\">Sec.130: Going armed to/near polling station — offence</p>
<p class=\"fact\">Sec.132: Breach of official duty — election officials</p>
<p class=\"fact\">Sec.135A: Booth capturing — imprisonment up to 3 years (5 years for second offence)</p></div>

<div class=\"sh\">4. Security Deposit and Forfeiture</div>
<div class=\"c b\"><h3>Candidate Security Deposit</h3>
<p class=\"fact\">Sec.34 RPA 1951: Every candidate must deposit security amount with ECI</p>
<p class=\"fact\">General category candidate: Rs.25,000 (LS or RS election); Rs.12,500 (State Assembly or State Council)</p>
<p class=\"fact\">SC/ST candidates: Rs.12,500 (LS or RS); Rs.6,250 (State Assembly or State Council)</p>
<p class=\"fact\">Deposit forfeited if candidate fails to secure more than 1/6 of total valid votes in constituency</p>
<p class=\"fact\">Purpose: deters non-serious candidates from contesting</p></div>

<div class=\"sh\">5. Election Petitions</div>
<div class=\"c r\"><h3>Election Petition Process</h3>
<p class=\"fact\">Who can file: any candidate or elector from the constituency</p>
<p class=\"fact\">Where: LS + State Assembly → respective High Court; President/VP → Supreme Court</p>
<p class=\"fact\">Time: within 45 days of declaration of election result</p>
<p class=\"fact\">Grounds: corrupt practice, improper nomination, counting error, candidate disqualified, non-compliance with election law</p>
<p class=\"fact\">HC decision: uphold election OR void election and declare petitioner elected OR order fresh election</p>
<p class=\"fact\">Appeal: from HC election judgment → directly to SC (under Art.136)</p></div>
<div class=\"c g\"><h3>Notable Election Petition Cases</h3>
<p class=\"fact\">Indira Gandhi v. Raj Narain (1975): Allahabad HC voided Indira Gandhi's election for corrupt practice (government servant used in election); triggered Emergency</p>
<p class=\"fact\">39th Amendment 1975: retroactively validated Indira Gandhi's election (later struck down after Emergency)</p>
<p class=\"fact\">Srimati Indira Gandhi case: SC upheld Allahabad HC ruling partially — led to 39th Amendment and Emergency</p></div>

<div class=\"sh\">6. Presidential and VP Election Laws</div>
<div class=\"c a\"><h3>Presidential and VP Elections Act 1952</h3>
<p class=\"fact\">Governs procedure for Presidential and VP elections</p>
<p class=\"fact\">Election by PR-STV (Proportional Representation by Single Transferable Vote)</p>
<p class=\"fact\">Nomination papers for President: 50 proposers + 50 seconders (from Electoral College)</p>
<p class=\"fact\">Nomination papers for VP: 20 proposers + 20 seconders (from Parliament members)</p>
<p class=\"fact\">Presidential election petition before SC; VP election also before SC</p></div>
<div class=\"c t\"><h3>PR-STV Method</h3>
<p class=\"fact\">Proportional Representation by Single Transferable Vote</p>
<p class=\"fact\">Quota = (Total valid votes / (Seats to fill + 1)) + 1 (Droop quota)</p>
<p class=\"fact\">Voters rank candidates 1, 2, 3 in order of preference</p>
<p class=\"fact\">If no candidate reaches quota on first count → lowest eliminated → preferences transferred</p>
<p class=\"fact\">Used in: Presidential election, VP election, RS elections, MLC elections</p></div>

<div class=\"sh\">7. Key Facts Quick Revision</div>
<div class=\"c gr\"><h3>Key Sections</h3>
<div class=\"pills\">
<span class=\"pill\">Sec.8 — disqualification (conviction)</span>
<span class=\"pill\">Sec.29A — party registration</span>
<span class=\"pill\">Sec.34 — security deposit</span>
<span class=\"pill\">Sec.47 — forfeiture (1/6 votes)</span>
<span class=\"pill\">Sec.78 — expenditure account (30 days)</span>
<span class=\"pill\">Sec.100 — election void</span>
<span class=\"pill\">Sec.123 — corrupt practices (8)</span>
<span class=\"pill\">Sec.126A — exit poll ban</span>
<span class=\"pill\">Sec.135A — booth capturing</span>
<span class=\"pill\">Sec.151A — by-election 6 months</span>
</div></div>
<div class=\"c r\"><h3>Quick Numbers</h3>
<p class=\"fact\">Security deposit: Rs.25,000 (LS/RS general); Rs.12,500 (SC/ST LS/RS); Rs.12,500 (State general); Rs.6,250 (SC/ST State)</p>
<p class=\"fact\">Forfeiture threshold: less than 1/6 of valid votes</p>
<p class=\"fact\">Election petition: 45 days from result</p>
<p class=\"fact\">By-election: 6 months from vacancy</p>
<p class=\"fact\">Expenditure account: 30 days from result</p>
<p class=\"fact\">Presidential nomination: 50 proposers + 50 seconders</p>
<p class=\"fact\">VP nomination: 20 proposers + 20 seconders</p></div>

</div></body></html>"""

SUMMARY_HTML = """<!DOCTYPE html>
<html lang=\"en\"><head><meta charset=\"UTF-8\">
<title>Summary Ch81 – Election Laws</title>
<style>
body{font-family:'Segoe UI',sans-serif;background:#f5f5f5;margin:0;padding:16px;color:#212121}
.box{background:#fff;border-radius:8px;padding:16px;max-width:700px;margin:0 auto;box-shadow:0 1px 4px rgba(0,0,0,.1)}
h2{color:#37474f;margin-top:0}ul{padding-left:20px}li{margin-bottom:6px;font-size:.93rem}
</style></head><body><div class=\"box\">
<h2>⚖️ Ch81: Election Laws — Summary</h2>
<ul>
<li><b>RPA 1950</b> — electoral rolls, delimitation, allocation of seats</li>
<li><b>RPA 1951</b> — conduct of elections, disqualifications (Sec.8), corrupt practices (Sec.123), election petitions, party registration (Sec.29A)</li>
<li><b>Sec.123</b> — 8 corrupt practices: bribery, undue influence, religious/caste appeals, false statements, vehicle hiring, excess expenditure, Govt servant use, booth capturing</li>
<li><b>Security deposit</b> — Rs.25,000 LS/RS; forfeited if <1/6 votes</li>
<li><b>Election petition</b> — 45 days; LS/Assembly → HC; President/VP → SC</li>
<li><b>Indira Gandhi case (1975)</b> — Allahabad HC voided election; triggered Emergency + 39th Amendment</li>
<li><b>PR-STV</b> — method for President, VP, RS, MLC elections; Droop quota</li>
<li><b>Sec.151A</b> — by-election within 6 months; <b>Sec.126A</b> — exit poll ban during voting</li>
</ul>
</div></body></html>"""

SECTIONS = [
    "Overview of Election Laws",
    "RPA 1950 — Electoral Rolls",
    "RPA 1951 — Conduct of Elections",
    "Corrupt Practices (Sec.123)",
    "Security Deposit and Forfeiture",
    "Election Petitions",
    "Presidential and VP Election Laws",
    "Key Facts",
]

_MCQ_DATA = [
    # Section 0: Overview (8)
    (0,"easy","RPA 1950 vs RPA 1951 main difference ఏమిటి? / What is the main difference between RPA 1950 and RPA 1951?",
     "Same Act, different years","RPA 1950: electoral rolls, delimitation, allocation of seats; RPA 1951: conduct of elections, candidate qualification/disqualification, corrupt practices, election petitions — two different Acts covering different aspects of elections","Only names differ","RPA 1950 is repealed","b",
     "RPA 1950 vs RPA 1951: (1) RPA 1950: Deals with allocation of seats in Parliament/State Legislatures, delimitation of constituencies, preparation and revision of electoral rolls; (2) RPA 1951: Deals with actual conduct of elections, qualifications/disqualifications of candidates, corrupt practices, election offences, and election petitions. Both are essential election laws. / RPA 1950: electoral rolls + delimitation; RPA 1951: conduct of elections + disqualifications + corrupt practices."),
    (0,"medium","Conduct of Elections Rules 1961 ఏ Act ను implement చేస్తాయి? / Which Act do the Conduct of Elections Rules 1961 implement?",
     "RPA 1950","RPA 1951 — Conduct of Elections Rules 1961 contain detailed procedural rules for conducting elections; made by ECI under powers delegated in RPA 1951; cover: nomination, scrutiny, withdrawal, polling, counting, declaration processes","Constitution directly","Companies Act","b",
     "Conduct of Elections Rules 1961: Subordinate legislation (rules) made under RPA 1951. Contain detailed procedural rules for: (1) Nomination and scrutiny; (2) Withdrawal of candidature; (3) Polling station procedures; (4) Counting of votes; (5) Declaration of results. ECI has power to make these rules under RPA 1951. / Conduct of Elections Rules 1961: implement RPA 1951 — detailed procedures for nomination, polling, counting."),
    (0,"easy","Presidential election ఏ Act govern చేస్తుంది? / Which Act governs the Presidential election?",
     "RPA 1951","Presidential and Vice-Presidential Elections Act 1952 — specific Act governing the procedure for election of President and Vice-President; different from LS/State elections; covers: nomination (50 proposers + 50 seconders for President), election petition before SC","Constitution alone","Conduct of Elections Rules","b",
     "Presidential and Vice-Presidential Elections Act 1952: Governs procedure for President and VP elections. Nominations: President — 50 proposers + 50 seconders from Electoral College; VP — 20 proposers + 20 seconders from Parliament members. Election petition: before Supreme Court (not HC). Different from regular parliamentary elections governed by RPA 1951. / President/VP elections: Presidential and Vice-Presidential Elections Act 1952 (not RPA 1951)."),
    (0,"medium","Election Symbols Order 1968 ఏ Order? / What is the Election Symbols (Reservation and Allotment) Order 1968?",
     "ECI circular","ECI order under Art.324 — governs allotment of symbols to parties and candidates; specifies reserved symbols (for recognized parties) and free symbols (for others); ECI decides symbol disputes in party splits","Parliamentary Act","Presidential Order","b",
     "Election Symbols (Reservation and Allotment) Order 1968: ECI order issued under Art.324 + RPA 1951. (1) Reserved symbols: allocated exclusively to recognized national and state parties; (2) Free symbols: available for registered unrecognized parties and independents from a pool; (3) Governs symbol disputes in party splits (which faction gets the symbol); (4) SC upheld ECI's power under this Order in Sadiq Ali case (1972). / Election Symbols Order 1968: ECI order; reserved vs free symbols; party split disputes."),
    (0,"hard","Art.327 ఏ Parliament ని enable చేస్తుంది? / What does Art.327 enable Parliament to do?",
     "Pass anti-defection law","Make provisions with respect to elections to Parliament and State Legislatures — subject to Constitution, Parliament may by law make provision with respect to all matters relating to elections to Parliament/State Legislatures including preparation of electoral rolls, delimitation of constituencies, and all other related matters","Set voting age","Appoint ECI","b",
     "Art.327: Subject to the provisions of the Constitution, Parliament may from time to time by law make provision with respect to all matters relating to, or in connection with, elections to either House of Parliament or to the House or either House of the Legislature of a State. This is the constitutional basis for RPA 1950 and RPA 1951 — Parliament's plenary power over elections. / Art.327: Parliament's plenary power to legislate on all election matters for Parliament AND State Legislatures."),
    (0,"easy","Model Code of Conduct (MCC) ఏ law basis పై? / On what legal basis does the MCC operate?",
     "Constitutional provision Art.324","Non-statutory — not based on any Act of Parliament; based on consensus among political parties; ECI enforces it through powers under Art.324; evolved over time (first for Kerala 1960, national from 1971); SC has upheld ECI's power to enforce MCC without statutory backing","RPA 1951 Sec.125","Supreme Court order","b",
     "MCC basis: Non-statutory (not enacted by Parliament). Historical development: (1) First formulated for Kerala State election 1960; (2) Extended nationally from 1971; (3) Parties consensually agreed to follow; (4) ECI enforces under Art.324 broad power; (5) SC upheld ECI's power to enforce MCC without explicit statute (T.N. Seshan v. Union of India 1995). / MCC: non-statutory; consensus-based; enforced by ECI under Art.324; evolved since 1960."),
    (0,"medium","Government of NCT of Delhi Act 1991 ఏ role పోషిస్తుంది elections లో? / What role does the Government of NCT Delhi Act 1991 play in elections?",
     "Only administrative","Governs elections to Delhi Legislative Assembly — Delhi has special UT with Legislature status; elections to Delhi Assembly governed by this Act + RPA 1951 as applicable; ECI conducts Delhi elections under Art.324","Creates ECI for Delhi","Delimits Delhi","b",
     "Government of NCT of Delhi Act 1991: Governs Delhi's special status as UT with Legislature (not a full state). Elections to Delhi Legislative Assembly are conducted under this Act and RPA 1951 provisions made applicable to it. ECI conducts Delhi elections. Delhi CM/Council of Ministers accountable to Delhi Assembly. / GNCTD Act 1991: governs Delhi (UT with Legislature) elections; ECI conducts; RPA provisions applicable."),
    (0,"hard","Art.328 State Legislature elections self-legislation power ఏమిటి? / What is the State Legislature's power under Art.328?",
     "States can override Parliament","States can make law for their own Legislative Assembly elections — Art.328: subject to Art.327 and Constitution, State Legislature may by law make provision with respect to elections to their own House; BUT Parliament's law (Art.327) prevails in conflict; States cannot contradict RPA 1951","States can abolish elections","States control ECI","b",
     "Art.328: State Legislature may make provision for elections to their own Legislature (State Assembly/Council). BUT: (1) Subordinate to Art.327 (Parliament's law); (2) Cannot contradict Parliament's law (RPA 1951); (3) Parliament's law prevails in case of conflict; (4) State law fills gaps not covered by Parliament's law. In practice, States use this for minor local variations in election procedures. / Art.328: State Legislature's supplementary power for own elections; subordinate to Art.327 (Parliament's law)."),

    # Section 1: RPA 1950 — Electoral Rolls (8)
    (1,"easy","RPA 1950 ఏ subjects cover చేస్తుంది? / What subjects does RPA 1950 cover?",
     "Corrupt practices","Allocation of seats in Parliament/State Legislatures + delimitation of constituencies + preparation and revision of electoral rolls — RPA 1950 is the foundational law for electoral structure","Election petitions","Candidate qualifications","b",
     "RPA 1950 subjects: (1) Allocation of seats in House of People (LS) and Council of States (RS); (2) Allocation of seats in State Legislatures; (3) Delimitation of parliamentary and assembly constituencies (before Delimitation Commission Act was created); (4) Preparation, maintenance, and revision of electoral rolls; (5) Registration of voters. / RPA 1950: allocation of seats + delimitation + electoral rolls."),
    (1,"medium","Electoral Registration Officer (ERO) ఏ role? / What is the role of an Electoral Registration Officer?",
     "Conducts elections","Maintains electoral roll for the constituency — ERO is appointed by ECI; responsible for: preparing electoral roll, enrolling voters, updating roll annually, conducting special camps for enrollment, handling claims and objections, certifying final rolls","Counts votes","Allots symbols","b",
     "Electoral Registration Officer (ERO): Appointed by ECI for each Assembly or Parliamentary constituency. Responsibilities: (1) Prepare and maintain electoral roll; (2) Enroll eligible voters; (3) Update roll annually (summary revision, special revision); (4) Handle claims (inclusion) and objections (exclusion); (5) Certify and publish final rolls. ERO usually is an officer of State/UT government. / ERO: appointed by ECI; maintains electoral roll; enrolls voters; annual revision."),
    (1,"easy","Electoral roll qualifying date ఏమిటి? / What is the qualifying date for electoral roll?",
     "January 26","January 1 of each year — voters must be 18 years as of January 1 to qualify for that year's electoral roll; annual revision based on January 1 qualifying date","March 31","November 1","b",
     "Qualifying date: January 1 of each year. A person must have attained 18 years of age by January 1 to be eligible for enrollment in that year's electoral roll. ECI has conducted Summary Revision with October-November as the reference date for some years. 2022: ECI changed qualifying dates to January 1, April 1, July 1, October 1 (4 qualifying dates per year for quarterly updates). / Qualifying date: January 1 (traditionally); ECI now has 4 qualifying dates per year."),
    (1,"medium","Service voters ఏమిటి? / Who are 'service voters' in election law?",
     "Government employees","Armed forces personnel, state police serving outside state, employees of Govt abroad — service voters can enroll at their home constituency or service constituency; can vote by postal ballot; special provision as they may not be at home during elections","Railway employees","ECI employees","b",
     "Service voters (Sec.20 RPA 1950): (1) Members of armed forces (Army, Navy, Air Force); (2) Members of forces armed with firearms maintained by State Govt serving outside the state; (3) Employees of Indian government posted abroad; (4) Spouse of service voter residing with them. Service voters can: (a) Enroll in home constituency as ordinary voter; OR (b) Enroll as service voter and vote by postal ballot (or proxy). / Service voters: armed forces + state police outside state + Govt employees abroad; can vote by postal ballot."),
    (1,"easy","Overseas voters (NRIs) ఎప్పటి నుండి eligible? / Since when are NRIs eligible to vote?",
     "1991","2010 — RPA (Amendment) Act 2010 gave Indian citizens residing abroad (with valid Indian passport) the right to register as voters in their home constituency in India","2000","1977","b",
     "NRI voting rights: RPA (Amendment) Act 2010. Indian citizens who are residing abroad for employment, education, or other reasons — if they hold a valid Indian passport — can register as voters in their home constituency (the constituency where their address is in India). Originally had to come to India personally to vote. / NRI voting rights: RPA Amendment 2010; register in home constituency; original requirement to vote in person."),
    (1,"medium","Electoral roll preparation process ఏమిటి? / What is the process of preparing electoral rolls?",
     "ECI prepares directly","ERO prepares draft roll → public notice → claims (inclusion applications) → objections (deletion applications) → hearings → disposal → final roll published — under ECI's superintendence; annual revision process","Gram Sabha prepares","Collector prepares independently","b",
     "Electoral roll preparation: (1) ERO prepares draft electoral roll; (2) Published for public inspection; (3) 30-day period for claims (applications for inclusion) and objections (applications for deletion); (4) ERO hears and decides claims/objections; (5) Final electoral roll prepared and published; (6) Certified copies supplied to recognized parties. Process supervised by ECI. / Electoral roll: ERO prepares draft → claims/objections → hearings → final roll; ECI supervision."),
    (1,"hard","Electoral roll deletion ఏ grounds పై? / On what grounds can a person be deleted from electoral roll?",
     "Any reason","(1) Death of voter; (2) Permanent migration from constituency; (3) Not ordinary resident; (4) Disqualification (non-citizen, convicted, unsound mind); (5) Overseas — if registered as overseas voter in same constituency no issue; ERO acts on objection or suo motu after inquiry","Voter's wish only","Only for non-voters","b",
     "Electoral roll deletion grounds: (1) Death; (2) Ceased to be ordinary resident of constituency (migrated); (3) Not a citizen of India; (4) Disqualified (court declared unsound mind, etc.); (5) Registered in more than one place; (6) Other grounds under law. ERO follows due process: notice to affected person → hearing → decision. Wrongful deletion is an offence under election law. / Electoral roll deletion: death + migration + non-citizen + disqualification; due process by ERO."),
    (1,"easy","Electoral roll nominal roll ఏ information contain చేస్తుంది? / What information does the electoral roll contain?",
     "Only name and address","Name, father's/husband's/mother's name, age, sex, address, EPIC number, photograph (in photo electoral roll) — electoral roll is a list of registered voters in a constituency with these details","Only EPIC number","Only address","b",
     "Electoral roll contents: (1) Serial number; (2) Name of voter; (3) Father's/mother's/husband's name; (4) Age and sex; (5) Address; (6) EPIC number (Electoral Photo Identity Card); (7) Photograph (in photo electoral rolls). Electoral rolls are public documents — available for inspection and certified copies available at cost to parties. / Electoral roll: name + father/mother name + age + sex + address + EPIC number + photo."),

    # Section 2: RPA 1951 — Conduct of Elections (8)
    (2,"easy","Sec.8 RPA 1951 ఏమిటి? / What does Section 8 of RPA 1951 provide?",
     "Party registration","Disqualification for conviction — person convicted of specified offences (Sec.8(1)) or convicted and sentenced to 2+ years (Sec.8(3)) is disqualified for 6 years from date of release from prison","Security deposit","Nomination rules","b",
     "Sec.8 RPA 1951: (1) Sec.8(1): Specific offences (promoting enmity, terrorism, untouchability, bribery, election offences, etc.) → disqualified for 6 years from date of conviction (even without 2-year sentence); (2) Sec.8(3): Conviction for any offence + sentence of 2+ years → disqualified for 6 years from date of release from prison. Lily Thomas (2013): Sec.8(4) protecting sitting members struck down. / Sec.8: conviction → 6-year disqualification; Sec.8(1) specific offences; Sec.8(3) 2+ year sentence."),
    (2,"medium","Sec.29A RPA 1951 ఏమిటి? / What is Section 29A of RPA 1951?",
     "Election petition","Registration of political parties with ECI — Sec.29A: any association of citizens wishing to be registered as political party applies to ECI; must commit to democratic, socialist, secular principles; 30-day public notice; ECI registers after examination","Corrupt practice","Nomination process","b",
     "Sec.29A RPA 1951: Registration of political parties. Any association calling itself a political party can apply to ECI. Requirements: (1) 30-day public notice; (2) Party's constitution/rules; (3) Affirmation to uphold democracy, socialism, secularism, sovereignty and integrity of India; (4) ECI examines and registers. Registration ≠ Recognition. / Sec.29A: registration of parties with ECI — 30-day notice + democratic/socialist/secular commitment."),
    (2,"easy","Sec.47 RPA 1951 — security deposit forfeiture ఎప్పుడు? / When is the security deposit forfeited under Sec.47?",
     "If candidate wins","If candidate fails to secure more than 1/6 (one-sixth) of total valid votes polled in the constituency — candidate who gets 1/6 or more of votes retains deposit; less than 1/6 → deposit forfeited","If petition filed","Always forfeited","b",
     "Sec.47 RPA 1951: Security deposit forfeiture. A candidate's deposit (Sec.34) is forfeited to government if the candidate fails to get more than 1/6 (16.67%) of total valid votes polled in the constituency. If candidate gets >1/6 votes → deposit returned after election. Purpose: discourages frivolous candidates. / Sec.47: deposit forfeited if candidate gets <1/6 of valid votes."),
    (2,"medium","Sec.62 RPA 1951 ఏమిటి? / What does Section 62 provide?",
     "Candidate qualification","Right to vote — Sec.62: every person enrolled on electoral roll has right to vote; disqualified person cannot vote; person in lawful custody also cannot vote unless ECI arranges (for some categories)","Party registration","Election dispute","b",
     "Sec.62 RPA 1951: Right to vote. (1) Every person whose name is on the electoral roll and who is not subject to any disqualification has the right to vote; (2) Persons disqualified under law cannot vote; (3) Persons in police/prison custody generally cannot vote. This section gives statutory form to the constitutional right to vote (Art.326). / Sec.62: right to vote for every person on electoral roll who is not disqualified."),
    (2,"hard","Sec.100 RPA 1951 ఏ grounds అవుతాయి election void? / What grounds under Sec.100 declare an election void?",
     "Only corrupt practice","Multiple: (1) Returned candidate not duly qualified; (2) Returned candidate was disqualified; (3) Corrupt practice by returned candidate or with his consent; (4) Improper reception/rejection of votes materially affecting result; (5) Non-compliance with Constitution or RPA provisions materially affecting result","Only expenditure violation","Only nomination error","b",
     "Sec.100 RPA 1951 — grounds for election void: (1) Returned candidate was not qualified; (2) Returned candidate was disqualified; (3) Corrupt practice committed by or with consent of returned candidate or his election agent; (4) Any nomination was improperly rejected; (5) The election was not conducted according to statutory provisions materially affecting result; (6) Improper counting of votes. HC (or SC for President/VP) declares election void. / Sec.100: election void — unqualified candidate, disqualified, corrupt practice, improper conduct materially affecting result."),
    (2,"easy","Sec.126A RPA 1951 ఏమిటి? / What does Section 126A of RPA 1951 provide?",
     "Nomination rules","Exit poll ban — Sec.126A: no person shall conduct, publish, or publicise exit poll results during the period from voting commencement until last phase of voting ends; violation: imprisonment up to 2 years or fine or both","Security deposit","Booth capturing","b",
     "Sec.126A RPA 1951 (inserted by amendment): Exit poll ban. No person shall: (1) Conduct any exit poll; (2) Publish results of exit poll; (3) Publicize or disseminate by any means the result of an exit poll — during the period from voting start of first phase until the last phase voting ends (in multi-phase elections, entire voting period). Violation: imprisonment up to 2 years or fine or both. / Sec.126A: exit poll ban from voting start to last phase end; violation = 2 years imprisonment."),
    (2,"medium","Sec.151A RPA 1951 by-election ఏ time? / What does Section 151A say about by-elections?",
     "By-election optional","Within 6 months of vacancy — Sec.151A: ECI shall fill any vacancy in Parliament or State Legislature through a by-election conducted within 6 months from date of occurrence of vacancy; exception: remaining term less than 1 year","Within 3 months","Within 1 year","b",
     "Sec.151A RPA 1951: By-elections for vacancies. ECI shall cause a by-election to fill a vacancy to the House of People, State Legislature within 6 months of the vacancy arising. Exception: no by-election needed if: (1) Less than 1 year remaining in the term; (2) ECI certifies that it is difficult to hold by-election in time. / Sec.151A: by-election within 6 months of vacancy; exception <1 year remaining term."),
    (2,"hard","Sec.9 and Sec.10 RPA 1951 disqualifications ఏమిటి? / What disqualifications do Sections 9 and 10 provide?",
     "Conviction only","Sec.9: disqualification for dismissal from government service for corruption/disloyalty — dismissed government employee disqualified for 5 years; Sec.10: directorships in government companies — holding director/manager position in a government company = office of profit → disqualification","Only criminal record","Only debt","b",
     "Sec.9 and Sec.10 RPA 1951: (1) Sec.9: Person dismissed from government service for corruption or disloyalty to the State — disqualified for 5 years from date of dismissal; (2) Sec.10: Person holding a director or managing director position in a government company — treated as holding office of profit → disqualified (unless office exempted by Parliament). / Sec.9: dismissed from Govt service (corruption) → 5-year disqualification; Sec.10: Govt company director = office of profit → disqualified."),

    # Section 3: Corrupt Practices (Sec.123) (8)
    (3,"easy","Sec.123 RPA 1951 లో corrupt practices ఎన్ని? / How many corrupt practices are listed in Section 123?",
     "5","8 — Section 123 lists 8 types of corrupt practices; finding of corrupt practice against returned candidate → election void","6","10","b",
     "Section 123 RPA 1951: 8 corrupt practices. (1) Bribery; (2) Undue influence; (3) Religious/community/race/caste appeal to promote enmity; (4) Use of religious symbols or national symbols; (5) Publishing false statement about candidate's personal character; (6) Hiring/procuring vehicles for voters within 2km; (7) Incurring excess election expenditure; (8) Obtaining assistance of government servants. If proved → election void. / Sec.123: 8 corrupt practices; election void if proved against returned candidate."),
    (3,"medium","Bribery corrupt practice ఏమిటి? / What constitutes bribery as a corrupt practice?",
     "Only cash payments","Giving, offering, agreeing to give any gratification to any person to induce that person to vote or not to vote or to vote in a particular way — includes: cash, gifts, free meals, free transport, free liquor (for votes)","Only political favors","Only party membership","b",
     "Bribery (Sec.123(1)): Giving or agreeing to give any gratification (cash, kind, entertainment, liquor, etc.) to: (1) Any person to induce them to exercise their electoral right; (2) Any voter to vote or refrain from voting or vote for a particular candidate; (3) Any person as a reward for having voted/not voted. Includes promises of future gratification (jobs, contracts). / Bribery: giving gratification to induce vote or reward for voting; includes cash, gifts, liquor, jobs."),
    (3,"easy","Undue influence corrupt practice ఏమిటి? / What constitutes undue influence as a corrupt practice?",
     "Political persuasion","Direct or indirect interference or attempt to interfere with free exercise of electoral right — threats: of divine displeasure, social ostracism, injury to person/property/employment; or promising benefits if person votes/abstains","Press criticism","Party campaigning","b",
     "Undue influence (Sec.123(2)): Direct or indirect interference with the free exercise of electoral right. Includes: (1) Threats of divine displeasure or spiritual censure (e.g., 'if you vote for X, God will punish you'); (2) Threats of social ostracism (boycott from community); (3) Threats of injury to person, property, employment; (4) Threats to withdraw benefits previously given if person doesn't vote for candidate. / Undue influence: interference with free vote through threats — divine displeasure, ostracism, injury threats."),
    (3,"medium","Religious/caste appeal corrupt practice ఏమిటి? / What constitutes a religious/caste appeal as corrupt practice?",
     "Any campaign speech","Appeal to voters to vote or not to vote on grounds of religion, race, caste, community, language — OR promotion of enmity or hatred between classes on these grounds in connection with election — candidate or agent's promotion of electoral prospects on grounds of religion/caste","Any criticism","Any cultural reference","b",
     "Religious/caste appeal (Sec.123(3)): An appeal by a candidate or his agent to vote on grounds of: religion, race, caste, community, or language. Also includes: promotion of feelings of enmity or hatred between classes on these grounds in connection with election. This prevents communal vote-seeking. Note: not every reference to religion/caste — must be an appeal to vote/not vote on these grounds. / Religious/caste appeal: Sec.123(3) corrupt practice — appeal to vote on grounds of religion/race/caste/community."),
    (3,"easy","False statements corrupt practice ఏమిటి? / What is the corrupt practice of false statements?",
     "Campaign exaggerations","Publishing false statement about candidate's personal character or conduct — Sec.123(4): publishing false statements likely to prejudice voting for a candidate; covers personal (not political) character; deliberately false publication","Any negative ad","Press reports","b",
     "False statement (Sec.123(4)): Publishing by a candidate or his agent of a statement of fact about the personal character or conduct of any candidate, knowing it to be false or not believing it to be true. Personal character: criminal record, personal behavior. Political statements (about policy positions) are generally not covered — only personal character. / False statements: Sec.123(4) — publishing false facts about candidate's personal character, knowing false."),
    (3,"medium","Vehicle hiring corrupt practice ఏమిటి? / What is the corrupt practice of hiring vehicles?",
     "Arranging party conveyances","Hiring/procuring vehicles/vessels for conveying electors to polling station — Sec.123(5): hiring or obtaining any vehicle or vessel for free conveyance of electors to/from polling station within 2km; this deprives voters of free choice by creating obligation","Providing food","Holding rally","b",
     "Vehicle hiring (Sec.123(5)): Hiring or procuring any vehicle or vessel for the free conveyance of any elector to/from a polling station within a constituency. Restriction particularly applies within 2km of polling station on polling day. Exception: persons walking or bicycling their own way are not covered. Purpose: prevents creating voter obligation through free transport. / Vehicle hiring: Sec.123(5) — hiring vehicles to convey voters to polling station (especially within 2km) = corrupt practice."),
    (3,"hard","Booth capturing Sec.135A ఏ punishment? / What is the punishment for booth capturing under Sec.135A?",
     "Only fine","Imprisonment up to 3 years (or fine or both) for first offence; imprisonment up to 5 years (or fine or both) for second or subsequent offence — Sec.135A: capturing a polling booth by seizing ballot boxes/machines, preventing voting, etc.","Only 6 months","Life imprisonment","b",
     "Booth capturing (Sec.135A RPA 1951): (1) First offence: imprisonment up to 3 years + fine; (2) Second/subsequent offence: imprisonment up to 5 years + fine. Booth capturing includes: seizing polling booth, taking over ballot boxes, EVM, preventing lawful voting, threatening or assaulting election officials or voters. ECI can cancel election in booth(s) where capturing occurred. / Sec.135A: booth capturing — 3 years first offence; 5 years repeat; ECI can cancel booth election."),
    (3,"easy","Sec.126 RPA 1951 ఏమిటి? / What does Section 126 of RPA 1951 prohibit?",
     "Election petition","Public meetings within 48 hours before polling — Sec.126: no person shall convene, hold, attend, join or address any public meeting in a constituency within the 48-hour period ending with the hour fixed for conclusion of polling; violation: up to 2 years imprisonment","Symbol use","Party registration","b",
     "Sec.126 RPA 1951: No public meetings in constituency within 48 hours before end of polling. This 48-hour silence period before elections is to prevent last-minute influence on voters. Violation: imprisonment up to 2 years or fine or both. Also: no sale or distribution of liquor on polling day and one day before (Sec.135B). / Sec.126: no public meetings within 48 hours before polling — 48-hour silence period."),

    # Section 4: Security Deposit and Forfeiture (8)
    (4,"easy","LS election security deposit ఎంత? / How much security deposit must a Lok Sabha candidate pay?",
     "Rs.10,000","Rs.25,000 — general category candidate contesting LS or RS election must deposit Rs.25,000 with ECI; SC/ST candidates: Rs.12,500 (half)","Rs.50,000","Rs.5 lakh","b",
     "Security deposit (Sec.34 RPA 1951): LS/RS election — General candidate: Rs.25,000; SC/ST candidate: Rs.12,500. State Assembly/Council election — General candidate: Rs.12,500; SC/ST candidate: Rs.6,250. Deposit is retained by ECI until election result; returned if candidate gets >1/6 votes; forfeited if <1/6 votes. / LS security deposit: Rs.25,000 (general); Rs.12,500 (SC/ST)."),
    (4,"medium","Deposit forfeiture threshold ఏమిటి? / What is the threshold for deposit forfeiture?",
     "Less than 1/10 votes","Less than 1/6 of total valid votes polled in constituency — Sec.47 RPA 1951: deposit forfeited if candidate fails to get more than one-sixth of total valid votes; candidate must get more than 16.67% to retain deposit","Less than 5% votes","Less than 1/3 votes","b",
     "Deposit forfeiture (Sec.47): Candidate must get MORE than 1/6 (>16.67%) of total valid votes to retain security deposit. If candidate gets 1/6 or less → deposit forfeited. This threshold (1/6) applies to the total valid votes in the constituency, not just the candidates' vote share. / Sec.47: deposit forfeited if candidate gets ≤1/6 of valid votes; must get >1/6 to retain."),
    (4,"easy","State Assembly election security deposit ఎంత? / How much security deposit for a State Assembly election?",
     "Rs.25,000","Rs.12,500 — general category candidate for State Legislative Assembly or State Legislative Council election must deposit Rs.12,500; SC/ST candidates: Rs.6,250","Rs.5,000","Rs.1 lakh","b",
     "State Assembly security deposit: General candidate: Rs.12,500; SC/ST candidate: Rs.6,250. This is half the LS/RS deposit amounts. Purpose: deters frivolous candidates without being prohibitively high for serious but resource-limited candidates. / State Assembly deposit: Rs.12,500 (general); Rs.6,250 (SC/ST) — half of LS amounts."),
    (4,"medium","Security deposit purpose ఏమిటి? / What is the purpose of the security deposit requirement?",
     "Revenue collection","Deters non-serious candidates from contesting — without deposit requirement, anyone could file nominations frivolously; deposit deters those who know they have no chance; forfeiture mechanism filters out candidates who get very few votes","Only administrative","Only legal requirement","b",
     "Security deposit purpose: (1) Deters frivolous candidates — any serious candidate should be able to garner >1/6 votes; (2) Reduces number of candidates on ballot — too many candidates confuses voters; (3) Ensures candidates have some public support before contesting; (4) Revenue collection is secondary. Critics: Rs.25,000 is still very low — many candidates contest knowing they'll forfeit. / Security deposit: deters frivolous candidates; forfeiture discourages those with no public support."),
    (4,"hard","Security deposit ఏ time return చేయబడుతుంది? / When is the security deposit returned to a candidate?",
     "Always returned","Returned if candidate gets more than 1/6 of valid votes — after election result, ECI/Returning Officer returns deposit to candidate or their authorized agent if threshold met; deposit is forfeited to Consolidated Fund of India if candidate gets 1/6 or less","Only if candidate wins","Only after 6 months","b",
     "Security deposit return: After election result, Returning Officer returns the security deposit (Rs.25,000 or Rs.12,500) to the candidate or their authorized representative IF the candidate secured MORE than 1/6 of total valid votes in the constituency. If forfeited → goes to Consolidated Fund of India. Return process: typically within a few weeks of results. / Deposit returned: if >1/6 votes secured; forfeited to CFI if ≤1/6 votes."),
    (4,"easy","Nomination paper ని ఎన్ని proposers sign చేయాలి? / How many proposers must sign a Lok Sabha nomination paper?",
     "10 proposers always","1 proposer for recognized party candidates — for candidates of recognized (national or state) parties: 1 proposer from the constituency; for others (including registered unrecognized parties and independents): 10 proposers from the constituency","5 proposers","50 proposers","b",
     "Nomination proposers (Sec.33 RPA 1951): (1) Recognized party candidates (national or state party): 1 proposer from the constituency; (2) Others (registered unrecognized parties, independents): 10 proposers from the constituency (electors on the roll). This is a key benefit of party recognition — reduces barrier for party candidates. / LS nomination: recognized party candidates — 1 proposer; others (independents/unrecognized) — 10 proposers."),
    (4,"medium","రాష్ట్రపతి ఎన్నిక nomination కి ఎంత మంది proposers అవసరం? / How many proposers and seconders are needed for Presidential election nomination?",
     "10 proposers + 10 seconders","50 proposers + 50 seconders from the Electoral College — Presidential and VP Elections Act 1952: nomination papers for Presidential candidate must be subscribed by at least 50 electors from the Electoral College as proposers and 50 as seconders","25 proposers","100 proposers","b",
     "Presidential election nomination: Under Presidential and Vice-Presidential Elections Act 1952 — at least 50 members of the Electoral College as proposers and at least 50 as seconders. Electoral College: elected MPs + elected MLAs. VP election nomination: 20 proposers + 20 seconders from Parliament members. Security deposit: Rs.15,000 for Presidential election. / Presidential election: 50 proposers + 50 seconders from Electoral College."),
    (4,"hard","VP election nomination ఏ requirement? / What is the nomination requirement for Vice-Presidential election?",
     "50 proposers + 50 seconders","20 proposers + 20 seconders from members of Parliament (both Houses) — VP Electoral College: both elected AND nominated members of both Houses; different from Presidential Electoral College (which excludes nominated members and MLAs)","Only elected MPs","10 proposers + 10 seconders","b",
     "VP election nomination (Presidential and VP Elections Act 1952): At least 20 members of Parliament as proposers and 20 as seconders. VP Electoral College: ALL members of Parliament (elected + nominated from both LS + RS). Different from Presidential Electoral College which includes MLAs but excludes nominated members. Security deposit: Rs.15,000 for VP election too. / VP election: 20 proposers + 20 seconders from ALL Parliament members (elected + nominated, both LS + RS)."),

    # Section 5: Election Petitions (8)
    (5,"easy","Election petition ఏ time limit? / What is the time limit for filing an election petition?",
     "30 days","45 days from result declaration — must be filed within 45 days of the date on which the returning officer makes the declaration of the elected candidate's name (date of publication of result)","90 days","6 months","b",
     "Election petition limitation: 45 days from date of declaration of result (publication of name of elected candidate). Filed in: HC (LS + State Assembly); SC (Presidential + VP elections). This is a mandatory limitation — courts have rarely excused delay. Strict compliance required. / Election petition: 45 days from result declaration; filed in HC (LS/Assembly) or SC (President/VP)."),
    (5,"medium","Election petition ఎవరు file చేయవచ్చు? / Who can file an election petition?",
     "Only losing candidate","Any candidate who contested + any elector of the constituency — RPA 1951 Sec.81: election petition may be presented by any candidate at the election or any elector (registered voter in that constituency)","Only political parties","Only ECI","b",
     "Who can file election petition: (1) Any candidate who contested the election; (2) Any elector registered in that constituency. Can challenge the election of the returned candidate. Must be filed before HC (LS/State Assembly) or SC (President/VP) within 45 days. / Election petition: any candidate + any elector of the constituency can file."),
    (5,"easy","Indira Gandhi v. Raj Narain (1975) ఏమిటి? / What was Indira Gandhi v. Raj Narain (1975) about?",
     "Emergency declaration","Allahabad HC voided Indira Gandhi's LS election (Rae Bareli constituency, 1971) for corrupt practice — government officials (Yashpal Kapoor) used in election campaign; HC declared her election void; she was disqualified for 6 years","Presidential election","State election","b",
     "Indira Gandhi v. Raj Narain (1975): Allahabad HC (Justice Jagmohan Lal Sinha) on June 12, 1975 — voided Indira Gandhi's 1971 Lok Sabha election from Rae Bareli constituency. Ground: use of government servant (Yashpal Kapoor, her PR officer) in election campaign — corrupt practice under Sec.123(7). Triggered: (1) Mrs. Gandhi appealed to SC; (2) SC gave conditional stay; (3) June 25, 1975 — Emergency declared. / Indira Gandhi v. Raj Narain 1975: Allahabad HC voided IG's election; corrupt practice; triggered Emergency."),
    (5,"medium","39th Amendment 1975 ఏ role played? / What role did the 39th Amendment 1975 play in Indira Gandhi case?",
     "Created Electoral Court","Retroactively validated Indira Gandhi's election — placed election of President, VP, PM, Speaker beyond judicial review; created special electoral mechanism; Minnerva Mills struck down parts later; 44th Amendment 1978 (post-Emergency) removed this protection","Created ECI","Changed voting age","b",
     "39th Constitutional Amendment 1975 (enacted during Emergency): (1) Retroactively validated Indira Gandhi's election and all her acts as PM; (2) Placed disputes relating to election of President, VP, PM, Speaker beyond courts' jurisdiction; (3) Created special election tribunal for these high offices; (4) SC (in election reference) found it invalid to the extent it affected fundamental rights. 44th Amendment 1978 removed this protection. Infamously enacted to overcome the Allahabad HC judgment. / 39th Amendment 1975: retroactively validated IG's election; placed PM election beyond courts; struck down/reversed by 44th Amendment 1978."),
    (5,"hard","HC election petition judgment పై appeal ఎక్కడ దాఖలు చేయాలి? / Where does an appeal lie from a HC judgment in an election petition?",
     "To ECI","Directly to Supreme Court — under Art.136 (Special Leave Petition) or Art.133/132; appeal from HC election judgment goes directly to SC; not to any intermediate appellate court; SC can entertain SLP against HC election judgment","To a Divisional Bench","To President","b",
     "Appeal from HC election judgment: Goes directly to Supreme Court under Art.136 (Special Leave Petition) or Art.133 (civil appellate jurisdiction) as applicable. No intermediate appellate court. SC can: (1) Uphold HC judgment; (2) Set aside HC judgment; (3) Modify relief. SC's judgment in election matters is final. / HC election petition judgment: appeal directly to SC (Art.136 SLP); no intermediate appellate court."),
    (5,"easy","Election declared void ఆ తర్వాత ఏ relief? / What relief can be granted when an election is declared void?",
     "Only re-election","Three reliefs: (1) Simply declare election void (re-election ordered by ECI); OR (2) Declare petitioner as elected candidate; OR (3) Declare election void + order fresh election — decision of HC (or SC for President/VP)","Only petitioner elected","No relief possible","b",
     "Relief on election void: HC/SC can grant: (1) Declare the election void — no one elected; ECI conducts fresh election (by-election); (2) Declare election of returned candidate void AND declare that the petitioner (or another candidate) was duly elected; (3) Only void the election — leaving seat vacant for by-election. The appropriate relief depends on the grounds and evidence. / Election void relief: declare void (re-election) OR declare petitioner elected OR void + fresh election."),
    (5,"medium","Election petition trial ఏ court లో? / Before which court is an election petition tried?",
     "District Court","High Court of the State — LS and State Assembly election petitions are tried by HC; originally had election tribunals, then in 1966 Parliament transferred jurisdiction to HCs; Presidential election petition and VP election petition → before SC","Supreme Court directly","ECI tribunal","b",
     "Election petition trial: (1) LS election → respective State's High Court; (2) State Legislative Assembly election → same state's HC; (3) If constituency spans multiple states — HC of that state; (4) Presidential election petition → SC; (5) VP election petition → SC. HCs have exclusive jurisdiction over LS/Assembly election disputes (transferred from Election Tribunals in 1966). / LS/State Assembly election petition: HC of the State; Presidential/VP: SC."),
    (5,"hard","Election petition ప్రక్రియలో 'recrimination' అంటే ఏమిటి? / What is 'recrimination' in election petition?",
     "Filing counter petition","When election petition seeks to have petitioner declared elected instead of void only — returned candidate can recriminate: show petitioner is also guilty of corrupt practice; if petitioner proved guilty, HC cannot declare them elected; both parties can be disqualified if both guilty of corrupt practice","Only appeals","ECI review","b",
     "Recrimination in election petitions: When petitioner seeks to be declared elected (not just void), the returned candidate can file a 'recrimination' — allege that the petitioner also committed corrupt practice. If HC finds: (1) Petitioner also committed corrupt practice → HC cannot declare petitioner elected; (2) Both guilty → both disqualified → fresh election. / Recrimination: returned candidate's counter-allegation that petitioner also committed corrupt practice; if proved → petitioner not declared elected."),

    # Section 6: Presidential and VP Election Laws (8)
    (6,"easy","PR-STV method ఏమిటి? / What is the PR-STV method?",
     "Party-based proportional","Proportional Representation by Single Transferable Vote — voters rank candidates 1, 2, 3 in order of preference; Droop Quota = (Total votes / (seats+1)) + 1; candidate reaching quota is elected; if no quota, lowest eliminated, preferences redistributed","First Past the Post","Block voting","b",
     "PR-STV (Proportional Representation by Single Transferable Vote): (1) Voters rank candidates in order of preference (1, 2, 3, ...); (2) Droop Quota = (Total valid votes / (Number of seats + 1)) + 1; (3) If candidate reaches quota on first count → elected; (4) Surplus transferred to next preferences; (5) If no one reaches quota, lowest candidate eliminated and their votes redistributed per second preferences. Used in India for: Presidential, VP, RS, State Legislative Council elections. / PR-STV: preferential ranking + Droop Quota + surplus/elimination transfer; used for RS, MLC, President, VP elections."),
    (6,"medium","Droop Quota calculation ఏమిటి? / How is the Droop Quota calculated?",
     "50% + 1 votes","(Total valid votes / (Number of seats to fill + 1)) + 1 — for single-seat elections like President: Total votes / 2 + 1 (essentially majority); for multi-seat RS election: divides by number of seats + 1 to find quota per seat","Total votes / total candidates","Total votes / 2","b",
     "Droop Quota formula: (Total valid votes / (Number of seats to be filled + 1)) + 1. For Presidential election (1 seat): Quota = (Total valid votes / 2) + 1. This ensures no more candidates can reach the quota than there are seats. Named after Henry Richmond Droop (19th century English lawyer/mathematician). Used in PR-STV method for RS elections and Presidential election. / Droop Quota: (Total votes / (seats+1)) + 1."),
    (6,"easy","Rajya Sabha elections ఏ method use చేస్తాయి? / What method is used for Rajya Sabha elections?",
     "First Past the Post","Single Transferable Vote (STV) — elected MLAs of State Assembly vote for RS candidates by ranking them in order of preference; STV with Droop Quota method determines winners","Direct election","PR-List system","b",
     "Rajya Sabha elections method: Single Transferable Vote (STV) — same as PR-STV but for RS seats. Elected MLAs of State Legislative Assembly vote for RS candidates from their state. They rank candidates by preference. Droop Quota determines the required votes per seat. Not First-Past-The-Post. This is why smaller parties can win RS seats if they have enough MLAs (e.g., cross-voting issues arise). / RS elections: STV by elected MLAs; Droop Quota; not FPTP."),
    (6,"medium","Presidential election voter weightage ఏమిటి? / How is voter weightage calculated in the Presidential election?",
     "All votes equal","State MLA value: 1 MLA vote = (State population / 1000) / Number of elected MLAs in State Assembly — MP vote: total value of all MLA votes / total elected MPs; ensures proportional representation of states in Presidential election","Only MPs decide","50% population rule","b",
     "Presidential election vote value: (1) MLA vote value = State population (per 1971 census) / (Total elected MLAs × 1000); (2) MP vote value = Total value of all MLA votes across India / Total elected MPs. Purpose: ensures that each state's MLAs' votes collectively equal the MPs' total, giving states proportional representation. Note: 1971 census is used (frozen). Example: UP MLA vote = 208; MP vote = ~723. / Presidential election: MLA vote value proportional to state population; MP vote = total MLA value / total MPs."),
    (6,"easy","Vice-President election Electoral College ఏమిటి? / What is the Electoral College for VP election?",
     "Only elected MPs","All members of Parliament (both elected AND nominated) in a joint sitting — Art.66: VP elected by all members of Parliament (LS + RS) both elected and nominated; unlike Presidential election which includes MLAs but excludes nominated MPs","Only MLAs","Only Lok Sabha","b",
     "VP Electoral College: ALL members of Parliament — both Houses (LS + RS) — and both elected AND nominated members. Total: 543 elected LS + 2 nominated LS + 238 elected RS + 12 nominated RS = 795 members (approximately). Distinguished from Presidential Electoral College (which includes elected MLAs but excludes nominated MPs). / VP Electoral College: ALL MPs — elected + nominated from both LS and RS (no MLAs); unlike Presidential (MLAs included, nominated MPs excluded)."),
    (6,"medium","Presidential election security deposit ఎంత? / How much is the security deposit for Presidential election?",
     "Rs.1 lakh","Rs.15,000 — security deposit for Presidential election nomination under Presidential and VP Elections Act 1952; forfeited if candidate doesn't get 1/6 of first preference votes","Rs.25,000","Rs.5 lakh","b",
     "Presidential election security deposit: Rs.15,000 under Presidential and VP Elections Act 1952. VP election security deposit: Rs.15,000 also. Deposit is forfeited if the candidate does not receive 1/6 of total first preference votes counted. / Presidential/VP election deposit: Rs.15,000 (forfeited if <1/6 first preference votes)."),
    (6,"hard","Presidential election ఏ census population use చేస్తుంది? / Which census population is used for Presidential election vote values?",
     "Latest census","1971 census — MLA vote values frozen at 1971 census figures; this was done by 84th Amendment 2001 (as part of seat freeze until 2026); ensures states that controlled population growth don't lose vote value in Presidential elections","2001 census","2011 census","b",
     "Presidential election population: 1971 census figures are used for calculating MLA vote values. This was part of the freeze on delimitation and representation until the 2031 census (84th Amendment 2001). Using 1971 census protects southern states (lower population growth) from disadvantage. The next revision will be after 2031 census when delimitation happens. / Presidential election: 1971 census used for vote values (frozen by 84th Amendment 2001); next revision after 2031."),
    (6,"easy","Presidential election petition ఏ court? / Before which court is a Presidential election petition filed?",
     "High Court","Supreme Court — Art.71 and Presidential and VP Elections Act 1952: disputes relating to election of President or VP shall be decided by Supreme Court; SC's decision is final","Parliament","ECI","b",
     "Presidential election dispute: Art.71 — any dispute regarding election of President or VP shall be decided by the Supreme Court whose decision shall be final. Presidential and Vice-Presidential Elections Act 1952 provides detailed procedure. SC has original jurisdiction over these petitions. / Presidential election petition: before Supreme Court (Art.71); SC's decision is final."),

    # Section 7: Key Facts (8)
    (7,"easy","Sec.123 corrupt practices ఎన్ని? / How many corrupt practices are listed under Sec.123?",
     "5","8 — bribery; undue influence; religious/caste appeal; use of religious/national symbols; false statements; hiring vehicles; excess expenditure; obtaining Govt servant assistance (+ booth capturing)","6","10","b",
     "Sec.123 RPA 1951: 8 corrupt practices. (1) Bribery; (2) Undue influence; (3) Religious/caste/community/language appeal; (4) Use of religious/national symbols; (5) Publication of false statement about personal character; (6) Hiring vehicles for voters; (7) Excess election expenditure; (8) Obtaining assistance of government servants. If any corrupt practice proved against returned candidate → election void. / Sec.123: 8 corrupt practices; election void if proved."),
    (7,"medium","Indira Gandhi election case ఏ court decided? / Which court decided the Indira Gandhi election case (1975)?",
     "Supreme Court","Allahabad High Court — Justice Jagmohan Lal Sinha; June 12, 1975; voided Indira Gandhi's 1971 LS election from Rae Bareli; ground: use of government servant (Yashpal Kapoor) in election — corrupt practice Sec.123(7)","Election Tribunal","ECI","b",
     "Indira Gandhi election case: Decided by Allahabad High Court (Justice J.M.L. Sinha) on June 12, 1975. Voided Indira Gandhi's election from Rae Bareli constituency (1971 elections). Ground: Yashpal Kapoor (her personal secretary, a government servant) worked in her election campaign before formally resigning from government service — corrupt practice (Sec.123(7)). / IG election case: Allahabad HC, June 12, 1975; Justice JML Sinha; corrupt practice Sec.123(7)."),
    (7,"easy","Security deposit forfeiture threshold ఏమిటి? / What is the security deposit forfeiture threshold?",
     "Less than 5%","Less than 1/6 of valid votes — Sec.47 RPA 1951: deposit forfeited if candidate fails to get more than one-sixth of total valid votes polled","Less than 10%","Less than 25%","b",
     "Deposit forfeiture: Less than 1/6 (16.67%) of total valid votes → forfeited. More than 1/6 → deposit returned. / Deposit forfeiture threshold: <1/6 of valid votes."),
    (7,"medium","PR-STV ఏ elections లో use అవుతుంది? / In which Indian elections is PR-STV used?",
     "Only Lok Sabha","Presidential election + VP election + Rajya Sabha elections + State Legislative Council elections — PR-STV used in all indirect elections in India; FPTP used for all direct elections (LS, State Assembly)","Only State Assembly","Only VP election","b",
     "PR-STV usage in India: (1) Presidential election; (2) Vice-Presidential election; (3) Rajya Sabha elections (by MLAs); (4) State Legislative Council elections (by MLAs for MLA quota). All indirect elections use PR-STV. Direct elections (Lok Sabha, State Assembly) use FPTP. / PR-STV: indirect elections — President, VP, RS, MLC (by MLAs); FPTP: direct elections (LS, State Assembly)."),
    (7,"easy","Booth capturing ఏ section govern చేస్తుంది? / Which section of RPA governs booth capturing?",
     "Sec.123","Sec.135A RPA 1951 — booth capturing is a separate election offence (not just a corrupt practice); imprisonment up to 3 years (first offence) or 5 years (second offence)","Sec.100","Sec.126","b",
     "Booth capturing: Sec.135A RPA 1951. Booth capturing is an election offence (distinct from corrupt practices under Sec.123). Punishment: (1) First offence: up to 3 years imprisonment; (2) Second/subsequent offence: up to 5 years imprisonment. ECI can also cancel the election at affected booths and order re-poll. / Sec.135A: booth capturing; 3 years first, 5 years repeat; ECI can cancel booth election."),
    (7,"medium","Exit poll ban ఏ time period? / During what period are exit polls banned?",
     "Only on polling day","From start of voting in first phase to end of voting in last phase — Sec.126A RPA 1951: entire voting period (including all phases in multi-phase election) is covered by exit poll ban; ban lifted only after last vote cast","1 day before polling","24 hours after polling","b",
     "Exit poll ban period: From when voting begins for first phase of the election until the end of voting in the last phase. In multi-phase elections, the ban covers the entire period. After last vote cast → ban lifted → results of exit polls can be published/broadcast. / Exit poll ban: entire voting period — from first phase start to last phase end."),
    (7,"hard","39th Amendment 1975 ఏ provision add చేసింది? / What did 39th Amendment 1975 add?",
     "Emergency provisions","Placed election of President, VP, PM, Speaker beyond judicial review + retroactively validated Indira Gandhi's election — subsequently reversed by 44th Amendment 1978 (post-Emergency); added Art.329A (since deleted); SC found it unconstitutional in Indira Gandhi vs Union of India reference","Anti-defection law","VP election change","b",
     "39th Amendment 1975: (1) Added Art.329A — election disputes of President, VP, PM, Speaker to be decided by special electoral forum (not courts); (2) Retroactively validated all acts of the President, VP, PM, Speaker (specifically validated IG's election); (3) Removed courts' jurisdiction over these disputes. SC in election reference found parts unconstitutional. 44th Amendment 1978 (post-Emergency) repealed Art.329A and removed this protection. / 39th Amendment 1975: Art.329A — PM/President election beyond courts; retroactively validated IG election; reversed by 44th Amendment 1978."),
    (7,"easy","Nomination withdrawal last date ఏమిటి? / What is the last date for withdrawal of candidature?",
     "On polling day","2 days after scrutiny of nominations — election schedule: nomination → scrutiny (next day after last nomination day) → withdrawal last date (2 days after scrutiny) → polling; candidate can withdraw within this period","7 days before polling","After nomination only","b",
     "Nomination withdrawal: Under Conduct of Elections Rules 1961: Last date for withdrawal is 2 days after the last date for scrutiny of nominations. After this date, the candidate is committed to the election and cannot withdraw. Name published in ballot paper/EVM after withdrawal period closes. / Withdrawal: within 2 days after scrutiny date; cannot withdraw after this deadline."),
]

def _seed_polity_ch81_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres=False, force=False):
    existing = row_to_dict_fn(
        db_exec_fn(conn, "SELECT id FROM study_notes WHERE topic='Indian_Polity' AND chapter_num=81").fetchone() or {}
    )
    if existing and not force:
        return
    if existing and force:
        db_exec_fn(conn, "DELETE FROM study_notes WHERE topic='Indian_Polity' AND chapter_num=81")
    ph = "%s" if use_postgres else "?"
    db_exec_fn(conn,
        f"INSERT INTO study_notes (subject, topic, chapter_num, title, content, summary) VALUES ({ph},{ph},{ph},{ph},{ph},{ph})",
        ("GK", "Indian_Polity", 81,
         "Election Laws",
         NOTES_HTML, SUMMARY_HTML)
    )

def _seed_polity_ch81_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres=False, force=False):
    existing = row_to_dict_fn(
        db_exec_fn(conn, "SELECT id FROM chapter_mcqs WHERE topic='Indian_Polity' AND chapter_num=81").fetchone() or {}
    )
    if existing and not force:
        return
    if existing and force:
        db_exec_fn(conn, "DELETE FROM chapter_mcqs WHERE topic='Indian_Polity' AND chapter_num=81")
    ph = "%s" if use_postgres else "?"
    sql = (f"INSERT INTO chapter_mcqs "
           f"(subject,topic,chapter_num,section_index,difficulty,question_telugu,"
           f"option_a,option_b,option_c,option_d,correct_option,explanation) "
           f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})")
    for sec_idx, diff, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation in _MCQ_DATA:
        db_exec_fn(conn, sql,
            ("GK", "Indian_Polity", 81, sec_idx, diff, q_te,
             opt_a, opt_b, opt_c, opt_d, correct, explanation))

def seed_polity_ch81(conn, db_exec_fn, row_to_dict_fn, use_postgres=False, force=False):
    _seed_polity_ch81_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force)
    _seed_polity_ch81_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force)
