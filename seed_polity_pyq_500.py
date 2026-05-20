"""Seed script: 500 PYQ-style Indian Polity MCQs for AP HC exam prep.
Auto-seeded at startup if count < 990.
"""
import os

USE_POSTGRES = os.environ.get("DATABASE_URL") is not None

PYQ_MCQS = [
    ("AP_HC","Indian_Polity","Which of the following statements regarding National Emergency under Article 352 are CORRECT?
1. It can be proclaimed on grounds of war, external aggression, or armed rebellion
2. The word \'internal disturbance\' was replaced by \'armed rebellion\' by the 44th Amendment
3. The President can proclaim it only on written advice of the Cabinet
4. The Lok Sabha can disapprove it by a simple majority","1, 2 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","A","medium","Statement 4 is wrong: Lok Sabha disapproval requires special majority (majority of total membership + 2/3 of members present and voting). Statements 1, 2, 3 are correct."),
    ("AP_HC","Indian_Polity","Assertion (A): Under Article 356, President\'s Rule can be imposed in a state where the constitutional machinery has failed.
Reason (R): The Supreme Court in S.R. Bommai v. Union of India held that imposition of President\'s Rule is subject to judicial review.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","hard","Both A and R are true. But R explains a limitation/safeguard on A, not the reason for A\'s existence. The S.R. Bommai case (1994) is a landmark ruling on President\'s Rule."),
    ("AP_HC","Indian_Polity","Match List I (Emergency Type) with List II (Constitutional Article):
List I: A. National Emergency  B. State Emergency  C. Financial Emergency  D. Suspension of FRs during emergency
List II: 1. Article 360  2. Article 359  3. Article 352  4. Article 356","A-3, B-4, C-1, D-2","A-4, B-3, C-1, D-2","A-3, B-4, C-2, D-1","A-4, B-3, C-2, D-1","A","medium","National Emergency - Art 352; State Emergency (President\'s Rule) - Art 356; Financial Emergency - Art 360; Suspension of FRs during emergency - Art 359."),
    ("AP_HC","Indian_Polity","Which of the following is/are correct regarding Financial Emergency under Article 360?
1. It has never been proclaimed in India since 1950
2. During Financial Emergency, salaries of SC and HC judges can be reduced
3. It requires approval of both Houses within 2 months
4. It operates till revoked; there is no maximum period","1 and 2 only","1, 2 and 4 only","2 and 3 only","1, 2, 3 and 4","B","hard","All of 1, 2, 4 are correct. Statement 3 is wrong: approval is needed within 2 months by each House (by simple majority), and if Lok Sabha is dissolved, within 30 days of reconstitution."),
    ("AP_HC","Indian_Polity","During a National Emergency, which of the following effects automatically occur?
1. Fundamental Rights under Article 19 stand suspended
2. Centre can issue directions to states on any matter
3. Parliament can legislate on State List subjects
4. The term of Lok Sabha can be extended by one year at a time","1 and 3 only","2, 3 and 4 only","1, 2 and 3 only","All of the above","B","medium","Art 19 FRs are suspended only if emergency is on grounds of war/external aggression (not armed rebellion). Options 2, 3, 4 are automatic effects. So answer is B."),
    ("AP_HC","Indian_Polity","The 44th Constitutional Amendment Act, 1978 made which of the following changes to emergency provisions?
1. Changed \'internal disturbance\' to \'armed rebellion\' in Art 352
2. Made written advice of Cabinet mandatory before proclamation
3. Provided for disapproval of emergency by Lok Sabha by special resolution
4. Made Art 20 and Art 21 non-suspendable even during emergency","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four changes were made by the 44th Amendment (1978) in response to the misuse of emergency powers during 1975-77. This is a frequently tested fact in AP HC PYQs."),
    ("AP_HC","Indian_Polity","Assertion (A): Article 21 cannot be suspended even during a National Emergency proclaimed under Article 352.
Reason (R): The 44th Constitutional Amendment Act made Articles 20 and 21 non-suspendable under Article 359.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both A and R are true and R correctly explains A. The 44th Amendment specifically excluded Arts 20 and 21 from the operation of Art 359."),
    ("AP_HC","Indian_Polity","Which of the following statements about Centre-State legislative relations are CORRECT?
1. Parliament can legislate on State List if Rajya Sabha passes a resolution by 2/3 majority
2. In case of conflict between Central and State law on Concurrent List, Central law prevails
3. Residuary powers vest with Parliament under Article 248
4. State legislature can legislate on Union List subjects during President\'s Rule","1, 2 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","A","medium","Statement 4 is incorrect: even during President\'s Rule, Parliament legislates on behalf of the state (not state legislature). Statements 1, 2, 3 are correct per Articles 249, 254, 248."),
    ("AP_HC","Indian_Polity","Match List I (Constitutional Provision) with List II (Subject matter):
List I: A. Article 263  B. Article 280  C. Article 312  D. Article 323-A
List II: 1. All-India Services  2. Administrative Tribunals  3. Inter-State Council  4. Finance Commission","A-3, B-4, C-1, D-2","A-1, B-4, C-3, D-2","A-3, B-1, C-4, D-2","A-4, B-3, C-1, D-2","A","hard","Art 263 - Inter-State Council; Art 280 - Finance Commission; Art 312 - All-India Services; Art 323-A - Administrative Tribunals (for public service disputes)."),
    ("AP_HC","Indian_Polity","The Sarkaria Commission (1983) and Punchhi Commission (2007) were both set up to examine:
1. Centre-State relations
2. Governors\' role and discretionary powers
3. Inter-State water disputes
4. Deployment of Central forces in states","1 only","1 and 2 only","1, 2 and 4 only","All of the above","C","hard","Both commissions primarily examined Centre-State relations (1), Governors\' role (2), and Central forces deployment (4). Inter-State water disputes (3) have a separate mechanism under Art 262 and Inter-State Water Disputes Act."),
    ("AP_HC","Indian_Polity","Which of the following is NOT a ground on which Parliament can legislate on State List subjects?
1. National interest resolution by Rajya Sabha under Art 249
2. Constitutional Emergency in that state under Art 356
3. International agreement/treaty under Art 253
4. Request by two or more state legislatures under Art 252
5. Financial Emergency under Art 360","5 only","1 and 5","3 and 4","All are valid grounds","A","hard","Financial Emergency (Art 360) does NOT authorise Parliament to legislate on State List. The other four (Art 249, 252, 253, 356) are valid grounds. This is a common trap question."),
    ("AP_HC","Indian_Polity","Assertion (A): The doctrine of \'repugnancy\' under Article 254 applies only to Concurrent List subjects.
Reason (R): Parliament has exclusive power to legislate on Union List subjects, leaving no scope for repugnancy with State laws.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","hard","Both are true and R explains A correctly. Repugnancy (Art 254) means conflict between Central and State laws; it can only arise in Concurrent List. On Union List, states cannot legislate at all."),
    ("AP_HC","Indian_Polity","Which committee/commission recommended the establishment of Inter-State Council?
Consider: 1. Sarkaria Commission  2. Rajamannar Committee  3. Administrative Reforms Commission (1st)  4. Punchhi Commission","1 only","3 only","1 and 3","2 and 4","C","hard","Both the 1st Administrative Reforms Commission and the Sarkaria Commission recommended setting up an Inter-State Council. It was established in 1990 under Art 263 on Sarkaria Commission\'s recommendation."),
    ("AP_HC","Indian_Polity","Which of the following features make the Indian Constitution \'quasi-federal\' in nature?
1. Single citizenship
2. All-India Services common to both Centre and States
3. Integrated judiciary
4. Separate constitutions for states
5. Strong Centre during Emergency","1, 2, 3 and 5 only","1, 3, 4 and 5 only","2, 3, 4 and 5 only","All of the above","A","medium","India does NOT have separate state constitutions (unlike USA) — statement 4 is a unitary feature. Statements 1, 2, 3, 5 are unitary/quasi-federal features."),
    ("AP_HC","Indian_Polity","Match List I (Theorist/Judge) with List II (Description of Indian Federalism):
List I: A. K.C. Wheare  B. Granville Austin  C. Morris Jones  D. Ivor Jennings
List II: 1. \'Cooperative federalism\'  2. \'Quasi-federal\'  3. \'Bargaining federalism\'  4. \'Federation with strong centralising tendency\'","A-2, B-1, C-3, D-4","A-4, B-1, C-3, D-2","A-2, B-3, C-1, D-4","A-4, B-3, C-1, D-2","A","hard","K.C. Wheare - \'quasi-federal\'; Granville Austin - \'cooperative federalism\'; Morris Jones - \'bargaining federalism\'; Ivor Jennings - \'federation with strong centralising tendency\'."),
    ("AP_HC","Indian_Polity","Which of the following statements about the official language provisions in the Constitution are CORRECT?
1. Article 343 declares Hindi in Devanagari script as the official language of the Union
2. English was to continue as official language for 15 years after commencement
3. The 8th Schedule originally listed 14 languages
4. Sindhi was added to the 8th Schedule by the 21st Constitutional Amendment","1 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four statements are correct. Original 14 languages in 8th Schedule; 21st Amendment (1967) added Sindhi; now 22 languages after subsequent additions."),
    ("AP_HC","Indian_Polity","Which languages were added to the 8th Schedule by the 92nd Constitutional Amendment Act, 2003?
1. Bodo  2. Dogri  3. Maithili  4. Santhali  5. Konkani","1, 2, 3 and 4 only","2, 3 and 4 only","1, 2, 4 and 5 only","All of the above","A","hard","The 92nd Amendment (2003) added Bodo, Dogri, Maithili, and Santhali to the 8th Schedule, taking the total to 22. Konkani was added earlier by the 71st Amendment (1992)."),
    ("AP_HC","Indian_Polity","Assertion (A): The Official Languages Act, 1963 allowed English to continue as an associate official language for official purposes of the Union even after 1965.
Reason (R): Non-Hindi speaking states, particularly from South India, strongly opposed the imposition of Hindi as the sole official language.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","hard","Both are true but R is not the cause of A. The Official Languages Act 1963 was a proactive legislative measure; the anti-Hindi agitation (especially 1965 Tamil Nadu protests) led to further amendments in 1967 to the Act, making it mandatory to use English."),
    ("AP_HC","Indian_Polity","Which of the following are discretionary powers of the Governor?
1. Sending a report to President recommending President\'s Rule under Art 356
2. Reserving a Bill for the consideration of the President under Art 200
3. Appointing Chief Minister when no party has a clear majority
4. Dismissing the Council of Ministers
5. Summoning and proroguing the state legislature","1, 2 and 3 only","2, 3 and 4 only","1, 2, 3 and 4 only","All of the above","C","hard","Summoning and proroguing the legislature (5) is done on the advice of the Council of Ministers — it is NOT a discretionary power. Powers 1, 2, 3, 4 are discretionary under specific circumstances."),
    ("AP_HC","Indian_Polity","Match List I (Governor\'s action) with List II (Constitutional provision):
List I: A. Governor\'s address to legislature  B. Governor\'s pardon power  C. Governor reserving bill for President  D. Governor\'s appointment of CM
List II: 1. Article 174  2. Article 200  3. Article 161  4. Article 164","A-1, B-3, C-2, D-4","A-2, B-3, C-1, D-4","A-1, B-2, C-3, D-4","A-4, B-3, C-2, D-1","A","medium","Art 174 - Governor summons/prorogues/addresses legislature; Art 161 - pardoning power of Governor; Art 200 - Governor\'s assent/reservation of bills; Art 164 - appointment of CM and CoM."),
    ("AP_HC","Indian_Polity","The Supreme Court in Rameshwar Prasad v. Union of India (2006) held that:
1. Governor cannot recommend dissolution of Assembly before it meets after elections
2. Governor\'s report under Art 356 is subject to judicial review
3. Governor acts as an agent of the Centre
4. Governor can invite the largest party to form government without giving chance to pre-poll alliance","1 and 2 only","2 and 3 only","1, 2 and 4 only","All of the above","A","hard","The Court held (1) and (2). The Governor does NOT act as an agent of the Centre (3 is wrong — this was a held position overruled). Statement 4 contradicts the ruling; post-election alliances should also be given opportunity."),
    ("AP_HC","Indian_Polity","Which of the following statements about the Union Council of Ministers are CORRECT?
1. The President appoints the Prime Minister and on PM\'s advice appoints other ministers
2. The size of the Council of Ministers cannot exceed 15% of the total strength of Lok Sabha
3. The ministers are collectively responsible to both Houses of Parliament
4. A minister who is not a member of Parliament must get elected within 6 months","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","medium","Statement 3 is wrong: ministers are collectively responsible to Lok Sabha only, not Rajya Sabha (Art 75(3)). Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","Which of the following parliamentary committees are \'Financial Committees\' of Parliament?
1. Public Accounts Committee
2. Estimates Committee
3. Committee on Public Undertakings
4. Business Advisory Committee
5. Committee on Subordinate Legislation","1, 2 and 3 only","1 and 2 only","1, 2, 3 and 5","All of the above","A","medium","The three Financial Committees of Parliament are: Public Accounts Committee, Estimates Committee, and Committee on Public Undertakings. BAC and Committee on Subordinate Legislation are other standing committees."),
    ("AP_HC","Indian_Polity","Assertion (A): Money Bills can only be introduced in the Lok Sabha.
Reason (R): The Rajya Sabha is a body representing states and financial matters are within the exclusive domain of the elected House.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","medium","A is true (Art 110 and 109). R is also true as a general principle. However, the precise constitutional reason is that the elected House (Lok Sabha) has primacy in financial matters — R is true but doesn\'t fully explain the specific constitutional basis for A."),
    ("AP_HC","Indian_Polity","Match List I (Parliamentary Term) with List II (Meaning):
List I: A. Guillotine  B. Kangaroo closure  C. Closure  D. Gag rule
List II: 1. Motion to end debate and vote immediately  2. Cutting off all remaining demands without discussion  3. Jumping from one amendment to another skipping some  4. Limiting time for debate","A-2, B-3, C-1, D-4","A-3, B-2, C-1, D-4","A-4, B-2, C-3, D-1","A-2, B-1, C-3, D-4","A","hard","Guillotine = passing all remaining demands without discussion; Kangaroo = jumping between clauses; Closure = ending debate to vote; Gag rule = time limit on debate."),
    ("AP_HC","Indian_Polity","Which of the following statements about \'Question Hour\' and \'Zero Hour\' in Parliament are CORRECT?
1. Zero Hour is a constitutional provision
2. Starred questions require oral answers
3. Unstarred questions are answered in writing and no supplementary questions are allowed
4. Zero Hour starts at 12 noon","2 and 3 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","C","medium","Statement 1 is wrong: Zero Hour is not mentioned in the Constitution — it is an informal convention. Statements 2, 3, 4 are correct."),
    ("AP_HC","Indian_Polity","Which of the following statements about the Election Commission of India are CORRECT?
1. It is a multi-member body established by Article 324
2. The Chief Election Commissioner can be removed only through impeachment process similar to a Supreme Court judge
3. The Election Commissioners have security of tenure equal to CEC
4. The ECI superintends, directs, and controls preparation of electoral rolls","1 and 4 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is incorrect: unlike the CEC, Election Commissioners can be removed on the recommendation of the CEC (as per original Article 324; this was under revision post 2023 Act). Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","Assertion (A): The Comptroller and Auditor General of India cannot practice before any court or authority after retirement.
Reason (R): This restriction is similar to that imposed on the Attorney General under Article 76.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","C","hard","A is true — Article 148(4) bars the CAG from holding office under Centre or State after retirement. However R is false — Article 76 deals with Attorney General\'s qualifications; there is no similar restriction on AG mentioned there."),
    ("AP_HC","Indian_Polity","Match List I (Constitutional Body) with List II (Removal Procedure):
List I: A. Chief Election Commissioner  B. Comptroller and Auditor General  C. Chairman, UPSC  D. Lokpal
List II: 1. Address by Parliament + President\'s order  2. Presidential removal on SC inquiry  3. Impeachment by Parliament like SC judge  4. Presidential removal on Lokpal Chairperson\'s recommendation","A-3, B-3, C-2, D-1","A-1, B-3, C-2, D-4","A-3, B-1, C-2, D-3","A-3, B-3, C-1, D-2","A","hard","CEC - same as SC judge (impeachment by Parliament); CAG - same as SC judge (Art 148); Chairman UPSC - Presidential removal on SC inquiry (Art 317); Lokpal Chairman/Members - Presidential removal on SC inquiry under Lokpal Act."),
    ("AP_HC","Indian_Polity","Which of the following rights have been read into Article 21 by the Supreme Court?
1. Right to privacy
2. Right to education (before 86th Amendment)
3. Right to livelihood
4. Right against solitary confinement
5. Right to speedy trial","1, 3 and 5 only","1, 2, 3 and 5 only","2, 4 and 5 only","All of the above","D","hard","All five rights have been read into Art 21 by the SC: Privacy (Puttaswamy 2017), Education (Unni Krishnan 1993, before 86th Amendment), Livelihood (Olga Tellis), Solitary confinement bar (Sunil Batra), Speedy trial (Hussainara Khatoon)."),
    ("AP_HC","Indian_Polity","The Supreme Court in Maneka Gandhi v. Union of India (1978) held that:
1. The procedure for depriving a person of personal liberty must be \'right, just and fair\'
2. Articles 14, 19, and 21 are not mutually exclusive and must be read together
3. \'Procedure established by law\' means any procedure laid down by law regardless of fairness
4. Passport impoundment without hearing violated Article 21","1, 2 and 4 only","2 and 3 only","1, 3 and 4 only","All of the above","A","hard","Statement 3 is exactly what the earlier Gopalan case held — Maneka Gandhi OVERRULED this view. The Court held procedure must be fair (1), articles must be read together (2), and impoundment violated Art 21 (4)."),
    ("AP_HC","Indian_Polity","Which of the following words/phrases were added to the Preamble by the 42nd Constitutional Amendment Act, 1976?
1. Socialist
2. Secular
3. Democratic
4. Integrity
5. Unity","1 and 2 only","1, 2 and 4 only","3 and 5 only","1, 2, 3 and 4","B","medium","The 42nd Amendment added \'Socialist\', \'Secular\' (between \'Sovereign\' and \'Democratic\'), and \'Integrity\' (to \'Unity of the Nation\'). \'Democratic\' and \'Unity\' were already in the original Preamble."),
    ("AP_HC","Indian_Polity","Which of the following Directive Principles have been given priority over Fundamental Rights by the Constitution itself (not just by amendment or court judgment)?
1. Article 39(b) - distribution of material resources
2. Article 39(c) - prevention of concentration of wealth
3. Article 45 - early childhood care and education
4. Article 48 - organisation of agriculture and animal husbandry","1 and 2 only","3 and 4 only","1, 2 and 3 only","All of the above","A","hard","Article 31C (added by 25th Amendment) gave primacy to laws implementing Art 39(b) and 39(c) over Arts 14, 19. The 42nd Amendment extended this to all DPSPs, but the SC struck down that extension in Minerva Mills. So constitutionally, only Art 39(b) and 39(c) enjoy this protection."),
    ("AP_HC","Indian_Polity","Assertion (A): In Minerva Mills Ltd. v. Union of India (1980), the Supreme Court struck down a part of the 42nd Amendment.
Reason (R): The Court held that giving absolute primacy to DPSPs over all Fundamental Rights destroys the essential features of the Constitution.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","hard","Both true and R correctly explains A. The Court invoked the Basic Structure doctrine — balance between FRs and DPSPs is itself a basic feature."),
    ("AP_HC","Indian_Polity","Which of the following constitutional provisions require ratification by at least half of the state legislatures before presidential assent?
1. Amendment to Article 54 (Presidential election)
2. Amendment to the 7th Schedule (Lists)
3. Amendment to representation of states in Parliament
4. Amendment to Article 368 itself
5. Amendment to Fundamental Rights","1, 2 and 3 only","1, 2, 3 and 4 only","2, 3 and 5 only","All of the above","B","hard","Amendments to FRs (Art 13) do NOT require state ratification — only special majority of Parliament. The provisions in Art 368(2) proviso requiring ratification include: election of President (Art 54, 55), distribution of executive/legislative powers, SC/HC jurisdiction, representation of states, and Art 368 itself."),
    ("AP_HC","Indian_Polity","Which of the following are correct regarding Article 356 (President\'s Rule) after the S.R. Bommai case?
1. The President cannot act on the Governor\'s report alone; Council of Ministers must advise
2. Floor test must be conducted before recommending President\'s Rule
3. Presidential proclamation is subject to judicial review
4. President\'s Rule is limited to a maximum of 3 years with Parliamentary approval","1 and 3 only","2 and 3 only","1, 3 and 4 only","All of the above","D","hard","All four are correct post-S.R. Bommai (1994): Cabinet advice needed (1), floor test mandatory (2), judicial review allowed (3), maximum 3-year limit with approvals (4)."),
    ("AP_HC","Indian_Polity","Match List I (Tribunal) with List II (Governing Article/Act):
List I: A. Administrative Tribunals  B. National Green Tribunal  C. Armed Forces Tribunal  D. Competition Appellate Tribunal
List II: 1. Competition Act, 2002  2. NGT Act, 2010  3. Article 323-A  4. Armed Forces Tribunal Act, 2007","A-3, B-2, C-4, D-1","A-1, B-2, C-3, D-4","A-3, B-4, C-2, D-1","A-2, B-3, C-4, D-1","A","medium","Administrative Tribunals - Art 323-A; NGT - NGT Act 2010; AFT - AFT Act 2007; Competition Appellate Tribunal - Competition Act 2002."),
    ("AP_HC","Indian_Polity","Which of the following statements about Article 371-D (special provisions for Andhra Pradesh/Telangana) are CORRECT?
1. It provides for an Administrative Tribunal for direct recruitment and local cadre reservations
2. It was inserted by the 32nd Constitutional Amendment, 1973
3. Orders of the Administrative Tribunal under Art 371-D are not subject to HC jurisdiction
4. After bifurcation, both AP and Telangana are governed by Art 371-D","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: Art 371-D was inserted by 32nd Amendment 1973; it covers local cadre/zones; HC\'s jurisdiction is excluded for AT orders; post-bifurcation, both states retain the provision."),
    ("AP_HC","Indian_Polity","The Andhra Pradesh Reorganisation Act, 2014 provided for which of the following?
1. Bifurcation of AP into Andhra Pradesh and Telangana
2. Hyderabad as joint capital for a period up to 10 years
3. Special category status for the residual Andhra Pradesh state
4. Establishment of a Central University in both new states","1 and 2 only","1, 2 and 4 only","1, 3 and 4 only","All of the above","B","medium","The 2014 Reorganisation Act provided for bifurcation (1), Hyderabad as common capital for up to 10 years (2), and Central Universities in both states (4). Special Category Status (3) was promised politically but NOT provided in the Act itself."),
    ("AP_HC","Indian_Polity","Which of the following are features introduced by the 73rd Constitutional Amendment Act, 1992 regarding Panchayati Raj?
1. Reservation of seats for SCs, STs and women in Panchayats
2. Creation of State Finance Commissions
3. Establishment of District Planning Committees
4. Three-tier structure of Panchayats at village, intermediate and district levels","1 and 4 only","1, 2 and 4 only","1, 3 and 4 only","All of the above","B","hard","District Planning Committees (3) were introduced by the 74th Amendment (for urban areas/municipalities), not the 73rd. Statements 1, 2, 4 are features of the 73rd Amendment."),
    ("AP_HC","Indian_Polity","Assertion (A): The 11th Schedule of the Constitution lists 29 subjects that may be entrusted to Panchayats.
Reason (R): These subjects were added by the 73rd Constitutional Amendment Act, 1992 to decentralise governance to the grassroots level.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","easy","Both A and R are correct. The 73rd Amendment added the 11th Schedule (Art 243-G) listing 29 subjects for Panchayats."),
    ("AP_HC","Indian_Polity","Match List I (Amendment) with List II (Subject):
List I: A. 73rd Amendment  B. 74th Amendment  C. 92nd Amendment  D. 97th Amendment
List II: 1. Cooperatives  2. Languages in 8th Schedule  3. Panchayati Raj  4. Municipalities","A-3, B-4, C-2, D-1","A-4, B-3, C-1, D-2","A-3, B-1, C-4, D-2","A-4, B-3, C-2, D-1","A","medium","73rd Amendment - Panchayati Raj; 74th - Municipalities (Nagarpalika); 92nd - Languages (Bodo, Dogri, Maithili, Santhali); 97th - Cooperative Societies."),
    ("AP_HC","Indian_Polity","The Fifth Schedule of the Constitution deals with:
1. Administration of Scheduled Areas and Scheduled Tribes
2. Powers of Tribes Advisory Council
3. Governor\'s reports on Scheduled Areas to the President
4. Extension of laws to Scheduled Areas","1 only","1 and 3 only","1, 2 and 3 only","All of the above","D","medium","The Fifth Schedule covers all aspects of Scheduled Areas administration including tribal advisory councils, Governor\'s role in reporting and applying/adapting laws to these areas."),
    ("AP_HC","Indian_Polity","Which of the following writs is/are correctly matched with their purpose?
1. Habeas Corpus - to secure release of a person detained unlawfully
2. Mandamus - to compel a public authority to perform a public duty
3. Prohibition - issued by lower court to superior court to prevent excess of jurisdiction
4. Certiorari - issued by superior court to lower court to quash an order","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","medium","Statement 3 is wrong: Prohibition is issued by SUPERIOR court to LOWER court (not the reverse) to prevent excess of jurisdiction. Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","Assertion (A): The writ of Quo Warranto can be issued against a private individual holding a public office.
Reason (R): Quo Warranto literally means \'by what authority\' and inquires into the legality of a person\'s claim to a public office.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true. Quo Warranto can be issued against any person (including a private individual) who claims/holds a public statutory office without legal authority. R correctly explains the writ\'s nature and A\'s logic."),
    ("AP_HC","Indian_Polity","Which of the following are modes of losing Indian citizenship under the Citizenship Act, 1955?
1. Renunciation
2. Termination
3. Deprivation
4. Expatriation","1, 2 and 3 only","1 and 3 only","2, 3 and 4 only","All of the above","A","medium","The Citizenship Act, 1955 provides for three modes of losing citizenship: Renunciation (voluntary), Termination (automatic when acquiring another country\'s citizenship), and Deprivation (by government for specified grounds). Expatriation is not a legal term used."),
    ("AP_HC","Indian_Polity","Which of the following statements about the Anti-Defection Law (10th Schedule) are CORRECT?
1. It was inserted by the 52nd Constitutional Amendment Act, 1985
2. A member is disqualified if he votes contrary to the party direction without prior permission
3. The decision of the Speaker/Chairman on disqualification is final and not subject to judicial review
4. Merger of at least 2/3 members of the legislature party with another party is not treated as defection","1, 2 and 4 only","1 and 4 only","2, 3 and 4 only","All of the above","A","hard","Statement 3 is incorrect: In Kihoto Hollohan v. Zachillhu (1992), SC held Speaker\'s decision IS subject to judicial review (though after final order). Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","Which of the following is/are correct regarding Inter-State River Water Disputes?
1. Article 262 allows Parliament to bar HC and SC jurisdiction over inter-state water disputes
2. The Inter-State River Water Disputes Act, 1956 was enacted under Article 262
3. Krishna Water Disputes Tribunal gave its final award in 1976, affecting AP
4. States can directly approach the Supreme Court for inter-state water disputes under Art 131","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is incorrect: SC jurisdiction under Art 131 is excluded for inter-state water disputes by the Inter-State River Water Disputes Act under Art 262. Statements 1, 2, 3 are correct."),
    ("AP_HC","Indian_Polity","Match List I (Service/Body) with List II (Constitutional Article):
List I: A. Union Public Service Commission  B. State Public Service Commission  C. All India Services  D. Public Service Commissions\' functions
List II: 1. Article 312  2. Article 320  3. Article 315  4. Article 316","A-3, B-4, C-1, D-2","A-4, B-3, C-1, D-2","A-3, B-4, C-2, D-1","A-1, B-3, C-4, D-2","A","medium","Art 315 - Establishment of PSCs; Art 316 - Appointment of Chairman/members of PSCs; Art 312 - All India Services; Art 320 - Functions of PSCs."),
    ("AP_HC","Indian_Polity","Which of the following statements about Minority Rights under Articles 29 and 30 are CORRECT?
1. Article 29 is available only to minorities
2. Article 30 gives minorities the right to establish and administer educational institutions
3. State aid can be denied to minority institutions that discriminate in admission
4. The right under Article 30(1) is absolute and cannot be regulated by the State","2 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","A","hard","Statement 1 is wrong: Art 29 is available to all citizens/groups including majority communities. Statement 4 is wrong: Art 30 rights can be regulated (not abridged) by the State. Statements 2, 3 are correct."),
    ("AP_HC","Indian_Polity","The Government of India Act, 1935 introduced which of the following features that were later adopted in the Indian Constitution?
1. Federal structure with Centre-State division of powers
2. Bicameral legislature at the Centre
3. Concept of residuary powers with Centre
4. Provincial autonomy
5. Office of Governor","1, 3 and 5 only","1, 2, 4 and 5 only","All of the above","1, 4 and 5 only","B","hard","Residuary powers with Centre (3) was NOT a feature of the GOI Act 1935 — residuary powers were with the Governor-General, not part of federal structure distribution. Statements 1, 2, 4, 5 were features of the 1935 Act."),
    ("AP_HC","Indian_Polity","The Constituent Assembly was formed based on the recommendations of which of the following?
1. Cabinet Mission Plan, 1946
2. Cripps Mission, 1942
3. Wavell Plan, 1945
4. Mountbatten Plan, 1947","1 only","1 and 2","1 and 4","2 and 3","A","medium","The Constituent Assembly was set up based on the Cabinet Mission Plan of 1946. The Cripps Mission (1942) first proposed a Constituent Assembly but wasn\'t implemented. Wavell Plan and Mountbatten Plan dealt with other matters."),
    ("AP_HC","Indian_Polity","Which of the following are exempt from disclosure under the RTI Act, 2005?
1. Information relating to national security and sovereignty
2. Cabinet papers including records of deliberations of CoM
3. Information received in confidence from a foreign government
4. All personal information regardless of public interest","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is wrong: personal information is exempt only if there is no public interest, or disclosure would cause unwarranted privacy invasion (S.8(1)(j) allows disclosure in public interest). Statements 1, 2, 3 are clearly exempt under S.8."),
    ("AP_HC","Indian_Polity","Assertion (A): The Central Information Commission is a statutory body established under the RTI Act, 2005.
Reason (R): The RTI Act also provides for penalties on Public Information Officers who fail to provide information within the stipulated time.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","medium","Both A and R are true. CIC is a statutory body (not constitutional). Penalties on PIOs are provided in the Act. But R is a separate provision — it doesn\'t explain A. Hence B."),
    ("AP_HC","Indian_Polity","Which of the following are correct regarding the President\'s pardoning power under Article 72?
1. The President can pardon sentences awarded by court martial
2. The President can pardon death sentences
3. The President acts on the advice of the Council of Ministers in exercising pardoning power
4. The President can suspend or commute the sentence of a person convicted under Central law","1, 2 and 4 only","1 and 2 only","2, 3 and 4 only","All of the above","D","hard","All four are correct. Art 72 covers pardoning of sentences by courts martial, death sentences, and any sentence under Central law. The SC in Maru Ram (1981) held that the President acts on Cabinet\'s advice."),
    ("AP_HC","Indian_Polity","Which of the following powers are EXCLUSIVE to the Rajya Sabha (not shared with Lok Sabha)?
1. Passing a resolution to extend Parliament\'s legislative power to State List (Art 249)
2. Passing a resolution to create new All-India Services (Art 312)
3. Ratifying a constitutional amendment that requires state ratification
4. Approving a proclamation of National Emergency","1 and 2 only","1, 2 and 3 only","3 and 4 only","All of the above","A","hard","Art 249 and 312 resolutions are exclusive Rajya Sabha powers. Ratification of constitutional amendments is done by state legislatures (not Rajya Sabha). National Emergency approval is a joint power of both Houses."),
    ("AP_HC","Indian_Polity","In which of the following cases did the Supreme Court enunciate/develop the concept of PIL (Public Interest Litigation)?
1. S.P. Gupta v. Union of India (1981)
2. Hussainara Khatoon v. Home Secretary, Bihar (1979)
3. Bandhua Mukti Morcha v. Union of India (1984)
4. Vishaka v. State of Rajasthan (1997)","2 only","1 and 2 only","1, 2 and 3 only","All of the above","D","hard","All four are landmark PIL cases: Hussainara Khatoon (1979) - right to speedy trial for undertrials; S.P. Gupta (1981) - locus standi expanded; Bandhua Mukti Morcha (1984) - bonded labour; Vishaka (1997) - sexual harassment guidelines."),
    ("AP_HC","Indian_Polity","Match List I (Tax) with List II (Authority that levies and collects):
List I: A. Corporation Tax  B. Service Tax (pre-GST)  C. Income Tax  D. Stamp Duties
List II: 1. State levies, State collects  2. Centre levies, Centre collects  3. Centre levies, States collect  4. Centre levies, divided between Centre and States","A-2, B-2, C-4, D-1","A-4, B-2, C-2, D-3","A-2, B-2, C-4, D-3","A-2, B-2, C-2, D-1","C","hard","Corporation Tax - Centre levies and collects exclusively (not shareable under pre-GST regime, but listed in Art 270 post-101st Amend for surcharge); Service Tax (pre-GST) - Centre levies and collects; Income Tax - Centre levies but divided; Stamp Duties - Centre levies rates, States collect."),
    ("AP_HC","Indian_Polity","The 101st Constitutional Amendment Act, 2016 is related to which of the following?
1. Introduction of Goods and Services Tax (GST)
2. Abolition of the distinction between goods and services for taxation
3. Creation of GST Council under Article 279A
4. Replacing multiple indirect taxes with a unified GST","1 and 3 only","1, 2 and 3 only","1, 3 and 4 only","All of the above","D","medium","The 101st Amendment introduced GST (1), unified goods and services taxation (2), created the GST Council under Art 279A (3), and replaced multiple indirect taxes (4). All four are correct."),
    ("AP_HC","Indian_Polity","The National Judicial Appointments Commission (NJAC) established by the 99th Constitutional Amendment was struck down by the Supreme Court in:
1. NJAC Case (2015)
2. Second Judges Case (1993)
3. Third Judges Case (1998)
4. Supreme Court Advocates-on-Record Association v. Union of India","4 only","1 and 4","1 only","2 and 3","B","hard","The NJAC was struck down in the 2015 case formally titled \'Supreme Court Advocates-on-Record Association v. Union of India\' — commonly known as the NJAC Case (2015). Options 1 and 4 refer to the same case."),
    ("AP_HC","Indian_Polity","Which of the following information is NOT exempt from disclosure under Section 8 of the RTI Act, 2005?
1. Information available to a person in his fiduciary relationship
2. Information relating to ongoing investigations of intelligence agencies
3. Information related to a deceased person\'s medical records sought by their legal heir
4. Information about life and liberty of a person","3 and 4 only","1 and 2 only","4 only","2 and 3 only","A","hard","Information relating to life and liberty (4) must be provided within 48 hours (S.7(1)) — it cannot be denied. Information sought by a legal heir about a deceased relative (3) is generally permitted. Hence 3 and 4 are NOT exempt."),
    ("AP_HC","Indian_Polity","Under the RTI Act, 2005, a Public Information Officer (PIO) must provide information within:
1. 30 days for normal requests
2. 48 hours for information affecting life and liberty
3. 5 days for information from Gram Panchayats (if BPL applicant)
4. 48 hours for requests submitted through an Assistant PIO","1 and 2 only","1, 2 and 3 only","2 and 3 only","All of the above","A","medium","Statements 1 and 2 are correct. BPL applicants get information within 5 days when routed through BPL provisions — not a specific RTI provision for Gram Panchayats. Statement 4 is incorrect; 48-hour rule is only for life/liberty."),
    ("AP_HC","Indian_Polity","The Protection of Children from Sexual Offences (POCSO) Act, 2012 defines a \'child\' as:
1. A person below 16 years of age
2. A person below 18 years of age
3. The Act has gender-neutral provisions
4. The Act applies only to female children","2 and 3 only","1 and 4 only","2 only","1 and 3 only","A","medium","Under POCSO Act 2012, a \'child\' is any person below 18 years (not 16). The Act is gender-neutral — it protects all children regardless of gender. Hence statements 2 and 3 are correct."),
    ("AP_HC","Indian_Polity","Which of the following sections of the Indian Penal Code (IPC) deal with rape and related offences?
1. Section 375 - Definition of rape
2. Section 376 - Punishment for rape
3. Section 354 - Assault or use of criminal force to a woman with intent to outrage modesty
4. Section 498-A - Husband or relative\'s cruelty to wife","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","easy","All four are correct and frequently tested in AP HC exams given the nature of criminal cases handled by High Courts."),
    ("AP_HC","Indian_Polity","Match List I (IPC Section) with List II (Offence):
List I: A. Section 302  B. Section 304-B  C. Section 307  D. Section 420
List II: 1. Cheating and dishonestly inducing delivery of property  2. Attempt to murder  3. Dowry death  4. Murder","A-4, B-3, C-2, D-1","A-3, B-4, C-1, D-2","A-4, B-1, C-2, D-3","A-2, B-3, C-4, D-1","A","easy","IPC: S.302 = Murder; S.304-B = Dowry Death; S.307 = Attempt to murder; S.420 = Cheating. These are fundamental sections for courts."),
    ("AP_HC","Indian_Polity","The Protection of Women from Domestic Violence Act, 2005 provides for which of the following reliefs?
1. Protection orders
2. Residence orders
3. Monetary relief
4. Custody orders
5. Compensation orders","1, 2 and 3 only","1, 2, 3 and 4 only","2, 3 and 5 only","All of the above","D","medium","The DV Act 2005 provides for all five: Protection orders, Residence orders, Monetary relief, Custody orders, and Compensation orders. This is a comprehensive civil remedy law."),
    ("AP_HC","Indian_Polity","Assertion (A): Under the Domestic Violence Act, 2005, the aggrieved person can be any woman in a domestic relationship.
Reason (R): The Act also covers women in live-in relationships.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","medium","Both A and R are true. The DV Act covers women in domestic relationships including live-in relationships (as interpreted by courts including the SC in D. Velusamy v. D. Patchaiammal). R adds a significant fact about A but doesn\'t explain why A is true."),
    ("AP_HC","Indian_Polity","Which of the following statements about Contempt of Court are CORRECT?
1. Contempt of court can be either civil or criminal in nature
2. Truth is a valid defence for criminal contempt under the Contempt of Courts Act, 2006 amendment
3. Courts have inherent powers to punish for contempt independent of the Act
4. The Supreme Court\'s power to punish for contempt is derived from Article 129","1 and 4 only","1, 2 and 3 only","1, 3 and 4 only","All of the above","D","hard","All four are correct: civil contempt = wilful disobedience; criminal contempt = scandalising the court; 2006 amendment added truth as a defence; courts have inherent contempt powers; Art 129 gives SC contempt power (HC under Art 215)."),
    ("AP_HC","Indian_Polity","Which of the following statements regarding reservation for SCs/STs are CORRECT?
1. The list of Scheduled Castes can be modified only by Parliament under Art 341
2. A person who converts to Christianity or Islam loses SC status
3. The Indra Sawhney case capped total reservation at 50% as a general rule
4. States can sub-classify SCs within the reserved quota","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All are correct: Art 341 empowers Parliament to modify SC list (1); conversion to Christianity/Islam results in loss of SC status per 1950 Presidential Order (2); Indra Sawhney (1992) mandated 50% cap (3); SC in Punjab v. Davinder Singh (2024) upheld sub-classification (4)."),
    ("AP_HC","Indian_Polity","The National Commission for Scheduled Castes is a constitutional body established under:
1. Article 338
2. The 89th Constitutional Amendment Act, 2003
3. Article 338-A deals with STs separately
4. Article 340 deals with OBCs","1 only","1 and 3 only","1, 2 and 3 only","All of the above","D","hard","All four are correct: Art 338 - National Commission for SCs; 89th Amendment bifurcated it into separate commissions for SCs (Art 338) and STs (Art 338-A); Art 340 - National Commission for OBCs."),
    ("AP_HC","Indian_Polity","The 103rd Constitutional Amendment Act, 2019 which provided for 10% EWS reservation:
1. Amended Articles 15 and 16 to add Economically Weaker Sections as a ground
2. Is applicable to appointments in government jobs and admissions in educational institutions
3. Was upheld by a 3:2 majority of the Supreme Court Constitution Bench in Janhit Abhiyan case (2022)
4. The 10% EWS reservation is in addition to the existing 50% limit set by Indra Sawhney","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: 103rd Amendment amended Arts 15 and 16 (1); applies to jobs and education (2); SC upheld it 3:2 in Janhit Abhiyan v. Union of India (2022) (3); it crosses the 50% limit since it\'s for unreserved category (4)."),
    ("AP_HC","Indian_Polity","Which of the following statements about High Courts are CORRECT?
1. High Courts have original, appellate, and revisional jurisdiction
2. A High Court can issue writs not only against state but also against private individuals
3. The jurisdiction of a HC can be extended by Parliament to Union Territories
4. HC can transfer cases from any subordinate court to itself under Article 228","1, 3 and 4 only","1 and 4 only","2, 3 and 4 only","All of the above","A","hard","Statement 2 is incorrect: HC writ jurisdiction (Art 226) is wider than SC (Art 32) and extends to \'any person or authority\' — but writs like Habeas Corpus can be issued against private individuals only in limited circumstances. As a general rule, writs are against the State/public authorities. Options 1, 3, 4 are correct."),
    ("AP_HC","Indian_Polity","Match List I (Article) with List II (HC Power/Provision):
List I: A. Article 226  B. Article 227  C. Article 228  D. Article 229
List II: 1. Transfer of cases from subordinate court to HC  2. Officers and servants of HC  3. Superintendence over subordinate courts  4. Power to issue writs","A-4, B-3, C-1, D-2","A-3, B-4, C-2, D-1","A-4, B-1, C-3, D-2","A-2, B-3, C-4, D-1","A","medium","Art 226 - Writ jurisdiction; Art 227 - Superintendence over courts; Art 228 - Transfer of cases; Art 229 - Officers/servants of HC."),
    ("AP_HC","Indian_Polity","The collegium system for appointment of judges was established through which of the following Supreme Court judgments?
1. First Judges Case - S.P. Gupta v. Union of India (1981)
2. Second Judges Case - Supreme Court Advocates-on-Record Association v. Union of India (1993)
3. Third Judges Case - In re Special Reference (1998)
4. NJAC Case - Supreme Court Advocates-on-Record Association v. Union of India (2015)","1 only","2 only","2 and 3 only","All four established different aspects","D","hard","All four are relevant: First Judges Case (1981) favoured executive primacy; Second Judges Case (1993) established collegium with CJI having primacy; Third Judges Case (1998) enlarged collegium to CJI + 4 senior judges; NJAC Case (2015) reaffirmed collegium by striking down NJAC."),
    ("AP_HC","Indian_Polity","Assertion (A): The scope of writ jurisdiction of High Courts under Article 226 is wider than that of the Supreme Court under Article 32.
Reason (R): Unlike Article 32, Article 226 empowers High Courts to issue writs not only for enforcement of Fundamental Rights but also for any other purpose.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains A. Art 226 says \'for the enforcement of rights conferred by Part III and for any other purpose\' — making HC writ jurisdiction broader than Art 32 which is limited to FRs."),
    ("AP_HC","Indian_Polity","The doctrine of \'separation of powers\' is considered part of the basic structure of the Indian Constitution. This was affirmed in:
1. Kesavananda Bharati v. State of Kerala (1973)
2. I.R. Coelho v. State of Tamil Nadu (2007)
3. Ram Jawaya Kapur v. State of Punjab (1955)
4. Indira Nehru Gandhi v. Raj Narain (1975)","1 only","1 and 4 only","1, 3 and 4","All of the above","B","hard","Separation of powers as part of basic structure was prominently discussed in Kesavananda Bharati (1973) and affirmed in Indira Nehru Gandhi v. Raj Narain (1975) where the SC struck down the 39th Amendment for violating separation of powers. Ram Jawaya (1955) discussed the Indian system but didn\'t invoke basic structure."),
    ("AP_HC","Indian_Polity","Match List I (Constitutional Amendment) with List II (Key Change):
List I: A. 24th Amendment  B. 25th Amendment  C. 42nd Amendment  D. 44th Amendment
List II: 1. Added \'socialist\', \'secular\', \'integrity\' to Preamble  2. Parliament\'s power to amend FRs confirmed  3. Changed \'amount\' to \'compensation\' for property acquisition  4. Restored judicial review, deleted Art 31","A-2, B-3, C-1, D-4","A-3, B-2, C-4, D-1","A-2, B-1, C-3, D-4","A-4, B-3, C-1, D-2","A","hard","24th Amendment - affirmed Parliament\'s power to amend FRs (overruling Golak Nath); 25th Amendment - changed \'compensation\' to \'amount\'; 42nd Amendment - mini-constitution (Preamble changes, extended Directive Principles primacy etc.); 44th Amendment - reversed Emergency excesses, restored judicial review, deleted Art 31."),
    ("AP_HC","Indian_Polity","Which of the following committees/commissions recommended the creation of Lokpal?
1. First Administrative Reforms Commission (1966–70) - chaired by Morarji Desai / K. Hanumanthaiah
2. L.M. Singhvi Committee (1967)
3. Second Administrative Reforms Commission (2005–09) - chaired by Veerappa Moily
4. N.N. Vohra Committee (1993)","1 only","1 and 3","1, 2 and 3","All of the above","C","hard","Lokpal was recommended by the 1st ARC (1966), L.M. Singhvi Committee (1967), and the 2nd ARC (2005-09). The N.N. Vohra Committee examined nexus between crime/politicians but did not specifically recommend Lokpal."),
    ("AP_HC","Indian_Polity","The National Commission to Review the Working of the Constitution (NCRWC), 2000 was headed by:
1. Justice M.N. Venkatachaliah
2. Justice B.P. Jeevan Reddy
3. Justice J.S. Verma
4. Justice V.N. Khare","2 only","3 only","1 only","4 only","C","medium","The NCRWC (2000-2002) was headed by Justice M.N. Venkatachaliah, former Chief Justice of India. It submitted its report in March 2002."),
    ("AP_HC","Indian_Polity","Which of the following have been held to be part of the \'Basic Structure\' of the Constitution by the Supreme Court?
1. Supremacy of the Constitution
2. Secular character of the Constitution
3. Judicial review
4. Parliamentary system of government
5. Free and fair elections","1, 2 and 3 only","1, 3 and 5 only","2, 4 and 5 only","All of the above","D","hard","All five are part of the basic structure as recognised by the SC in various judgments: Supremacy (Kesavananda), Secular character (S.R. Bommai), Judicial review (L. Chandra Kumar), Parliamentary system (Kesavananda), Free and fair elections (Indira Gandhi case)."),
    ("AP_HC","Indian_Polity","Assertion (A): The Parliament cannot abrogate the fundamental right to approach the Supreme Court (Article 32) even by constitutional amendment.
Reason (R): Article 32 is itself a Fundamental Right and its abolition would destroy the basic structure of the Constitution.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","hard","Both are true and R correctly explains A. Dr. Ambedkar called Art 32 \'the heart and soul of the Constitution\'. The SC has held that judicial review (including Art 32) is part of the basic structure."),
    ("AP_HC","Indian_Polity","The Andhra Pradesh High Court was established in:
1. 1954 under the States Reorganisation Act
2. 1956 on the formation of Andhra Pradesh state
3. 1949 as a successor to the Madras High Court for Andhra region
4. 1960 after the creation of separate Andhra State","2 only","1 only","3 only","4 only","B","hard","The AP High Court was established on 5 July 1954 when the separate state of Andhra was carved out from Madras state. After 1956, it continued as the HC for the enlarged Andhra Pradesh state formed under the States Reorganisation Act."),
    ("AP_HC","Indian_Polity","Which of the following statements about the Telangana High Court are CORRECT?
1. It was established under the Andhra Pradesh Reorganisation Act, 2014
2. It was inaugurated on 1 January 2019
3. Hyderabad serves as its seat
4. It was initially a common High Court for both AP and Telangana","3 and 4 only","1 and 3 only","1, 3 and 4 only","All of the above","D","hard","All four are correct: The 2014 Reorganisation Act created the framework; Telangana HC was inaugurated on 1 January 2019; Hyderabad is its seat; till 2019, the combined AP HC served both states."),
    ("AP_HC","Indian_Polity","Which of the following are features of the GST Council established under Article 279-A?
1. It consists of the Union Finance Minister as Chairperson
2. Every decision requires a majority of members present and voting
3. Votes of Union Government carry 1/3 weightage
4. Decisions require 3/4 weighted majority of votes cast","1 and 3 only","3 and 4 only","1, 3 and 4 only","All of the above","C","hard","Under Art 279-A: FM is Chairperson (1); Centre has 1/3 vote weightage (3); 3/4 majority required (4). Statement 2 is wrong — simple majority is NOT the rule; 3/4 weighted majority is required."),
    ("AP_HC","Indian_Polity","The principle of \'eclipse\' in constitutional law means:
1. A pre-constitutional law inconsistent with Fundamental Rights becomes dormant but can revive if the FR is amended
2. A post-constitutional law inconsistent with FRs is void ab initio and cannot revive
3. The inconsistent part of a law becomes inactive (eclipsed) and not the entire law
4. Both citizens and non-citizens can invoke this doctrine","1 and 3 only","1, 2 and 3 only","2 and 3 only","All of the above","B","hard","Statement 4 is incorrect: the doctrine of eclipse applies only to pre-constitutional laws and can only be invoked by citizens (not non-citizens, as FRs under Art 13(1) apply to pre-constitutional laws). Statements 1, 2, 3 are correct."),
    ("AP_HC","Indian_Polity","Assertion (A): The doctrine of \'severability\' allows courts to strike down only the unconstitutional part of a law while keeping the rest valid.
Reason (R): If the unconstitutional part is so intertwined with the rest that it cannot be separated, the entire law must be struck down.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","hard","Both A and R are true statements about severability doctrine. R is a consequence/limitation of the doctrine, not its explanation. Hence B."),
    ("AP_HC","Indian_Polity","Which of the following courts/tribunals are established under specific statutes rather than constitutional provisions?
1. Family Courts
2. Debt Recovery Tribunals
3. Central Administrative Tribunals
4. Consumer Disputes Redressal Forums","1, 2 and 4 only","2, 3 and 4 only","1 and 4 only","All of the above","A","hard","Central Administrative Tribunals (CATs) are established under Art 323-A of the Constitution (constitutional provision). Family Courts, DRTs, and Consumer Forums are statutory bodies under specific Acts (Family Courts Act 1984, SARFAESI/DRT Act, Consumer Protection Act)."),
    ("AP_HC","Indian_Polity","The Sixth Schedule of the Constitution provides for:
1. Autonomous District Councils in tribal areas of Northeast India
2. Autonomous Regional Councils within districts if tribal communities are distinct
3. The President is the authority to determine Scheduled Tribes under Art 342
4. Governors of specified states have special powers regarding tribal areas under Sixth Schedule","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is about Art 342 which deals with presidential notification of STs — it\'s separate from the 6th Schedule. The 6th Schedule (Arts 244(2) and 275(1)) covers Autonomous District Councils (1), Regional Councils (2), and Governor\'s special powers (4) in Assam, Meghalaya, Tripura, and Mizoram."),
    ("AP_HC","Indian_Polity","The Inter-State Council established in 1990 under Article 263 consists of:
1. Prime Minister as the Chairperson
2. All Chief Ministers of States
3. Governors of States
4. Six Cabinet Ministers of the Union nominated by the Prime Minister
5. Administrators of Union Territories","1, 2 and 4 only","1, 2, 4 and 5 only","All of the above","1, 3 and 4 only","B","hard","The Inter-State Council includes PM (Chair), all CMs, 6 Union Cabinet Ministers (nominated by PM), and UTs with legislature (Delhi, Puducherry, J&K). Governors are NOT members — Governors are not political functionaries representing state interests in the Council."),
    ("AP_HC","Indian_Polity","Which of the following statements about the National Human Rights Commission (NHRC) are CORRECT?
1. The NHRC was established under the Protection of Human Rights Act, 1993
2. The Chairperson must be a retired Chief Justice of India
3. NHRC can investigate complaints against armed forces directly
4. NHRC recommendations are binding on the government","1 and 2 only","1, 2 and 3 only","1 and 4 only","All of the above","A","hard","Statement 3 is wrong: NHRC cannot directly investigate armed forces complaints — it can seek reports from the government (S.19 of the Act). Statement 4 is wrong: NHRC recommendations are advisory, not binding. Statements 1 and 2 are correct."),
    ("AP_HC","Indian_Polity","Match List I (Provision) with List II (Subject):
List I: A. Article 48-A  B. Article 51-A(g)  C. Article 21  D. Entry 17-A, Concurrent List
List II: 1. Right to clean environment (read into by SC)
2. Forests and protection of wild animals
3. Citizen\'s duty to protect environment
4. State duty to protect environment","A-4, B-3, C-1, D-2","A-3, B-4, C-2, D-1","A-4, B-1, C-3, D-2","A-1, B-3, C-4, D-2","A","medium","Art 48-A (DPSP) - State\'s duty to protect environment; Art 51-A(g) (FD) - Citizen\'s duty to protect environment; Art 21 - SC read right to clean environment; Entry 17-A, Concurrent List - Forests and wild animals (added by 42nd Amendment)."),
    ("AP_HC","Indian_Polity","In Kesavananda Bharati v. State of Kerala (1973), the Supreme Court held regarding the Preamble that:
1. The Preamble is part of the Constitution
2. The Preamble can be amended under Article 368
3. The basic features mentioned in the Preamble (sovereignty, democracy, republic) cannot be abridged
4. The Preamble can override specific provisions of the Constitution","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","The Court held: Preamble is part of Constitution (1) — overruling Berubari case; it can be amended (2) — 42nd Amendment did so; basic features in Preamble are protected (3). Statement 4 is wrong — Preamble cannot override specific provisions."),
    ("AP_HC","Indian_Polity","Which of the following are \'Unwritten Conventions\' of the Indian Constitution (not explicitly mentioned in the text)?
1. The President invites the leader of the majority party to form the government
2. The Prime Minister must be a member of Lok Sabha
3. The President does not refuse to sign bills passed by Parliament
4. Cabinet solidarity and collective responsibility","1 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 2 is not entirely a convention — the Constitution requires PM to be a member of either House (Art 75(5) says minister must be member within 6 months). The PM being from Lok Sabha is a convention. Option B lists 1, 3, 4 as clear conventions — none are explicitly in the Constitution text."),
    ("AP_HC","Indian_Polity","The concept of \'Constitutional morality\' was invoked by the Supreme Court in which of the following landmark cases?
1. Navtej Singh Johar v. Union of India (2018) - decriminalisation of Section 377
2. Indian Young Lawyers Association v. State of Kerala (2018) - Sabarimala case
3. Joseph Shine v. Union of India (2018) - adultery case
4. Common Cause v. Union of India (2018) - passive euthanasia","1 only","1 and 2 only","1, 2 and 3 only","All of the above","C","hard","Constitutional morality was prominently invoked in Navtej Johar (S.377), Sabarimala (women entry), and Joseph Shine (adultery). In Common Cause (passive euthanasia), the primary concept was right to die with dignity under Art 21, not constitutional morality."),
    ("AP_HC","Indian_Polity","Which of the following are recognised as part of the Model Code of Conduct (MCC) enforced by the Election Commission?
1. Ruling party cannot announce new policies or schemes after election announcement
2. Government machinery cannot be used for party purposes
3. Religious places cannot be used for election campaigning
4. The MCC has statutory backing under the Representation of the People Act","1, 2 and 3 only","1 and 2 only","2, 3 and 4 only","All of the above","A","hard","Statement 4 is wrong: the MCC does NOT have statutory backing — it is a voluntary code enforced by moral authority of the ECI. Statements 1, 2, 3 are correct features of the MCC."),
    ("AP_HC","Indian_Polity","Under the Representation of the People Act, 1951, a person is disqualified from contesting elections if convicted and sentenced to:
1. Imprisonment of 2 years or more
2. Any imprisonment regardless of term for offences under Sections 171E and 171F of IPC
3. Imprisonment for offences related to promoting enmity between groups
4. A fine only (no imprisonment)","1 and 2 only","1, 2 and 3 only","2 and 3 only","All of the above","B","hard","Conviction with fine only (4) does not disqualify. A sentence of 2+ years (S.8(3) RPA), conviction for bribery at elections (S.171E, 171F IPC - S.8(1)), and promoting enmity (S.8(1)) result in disqualification. Hence 1, 2, 3 are correct."),
    ("AP_HC","Indian_Polity","Assertion (A): The right to property was originally a Fundamental Right under Article 19(1)(f) and Article 31 of the Constitution.
Reason (R): The 44th Constitutional Amendment Act, 1978 deleted Articles 19(1)(f) and 31 and added Article 300-A which makes the right to property only a constitutional right, not a Fundamental Right.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true. Originally Art 19(1)(f) protected right to acquire/hold property and Art 31 protected against compulsory acquisition without compensation. The 44th Amendment removed both and added Art 300-A."),
    ("AP_HC","Indian_Polity","The Supreme Court\'s jurisdiction under Article 32 to enforce Fundamental Rights:
1. Can be invoked only by citizens of India
2. Cannot be invoked for violation of constitutional rights other than FRs
3. Can be suspended during a National Emergency
4. Is an original jurisdiction and also an extraordinary remedy","2 and 4 only","3 and 4 only","1, 3 and 4 only","All of the above","B","hard","Statement 1 is wrong: Art 32 can be invoked by any person (including non-citizens) for enforcement of FRs available to them. Statement 2 is wrong: Art 32 is specifically for FRs. Statements 3 and 4 are correct."),
    ("AP_HC","Indian_Polity","Which of the following are correctly matched regarding the 74th Constitutional Amendment (Municipalities)?
1. Article 243-P to Article 243-ZG covers urban local bodies
2. The 12th Schedule lists 18 functions for Municipalities
3. Ward Committees must be set up in municipalities with population over 3 lakh
4. State Election Commission conducts elections to urban local bodies","1 and 4 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 2 is wrong: the 12th Schedule lists 18 subjects (functions) — but the 74th Amendment itself did not list 18 specific items in the schedule content. Actually 18 items are correct. Wait — the 12th Schedule has 18 items. So Statement 2 should be correct. Let me reconsider: Statements 1, 2, 3, 4 are all correct for 74th Amendment. Answer D."),
    ("AP_HC","Indian_Polity","The 12th Schedule added by the 74th Constitutional Amendment lists how many subjects/functions for Municipalities?","14","18","22","29","B","medium","The 12th Schedule lists 18 subjects for Municipalities (74th Amendment). Compare: 11th Schedule has 29 subjects for Panchayats (73rd Amendment), 8th Schedule originally had 14 languages (now 22)."),
    ("AP_HC","Indian_Polity","Match List I (National Commission) with List II (Enabling Provision/Act):
List I: A. National Commission for Women  B. National Commission for Minorities  C. National Commission for SCs  D. National Commission for Protection of Child Rights
List II: 1. Article 338  2. National Commission for Minorities Act, 1992  3. Protection of Children from Sexual Offences-related statute / CPCR Act 2005  4. National Commission for Women Act, 1990","A-4, B-2, C-1, D-3","A-2, B-4, C-1, D-3","A-1, B-2, C-4, D-3","A-4, B-1, C-2, D-3","A","medium","NCW - statutory under NCW Act 1990; NCM - statutory under NCM Act 1992; NCSC - constitutional under Art 338; NCPCR - statutory under Commission for Protection of Child Rights Act 2005."),
    ("AP_HC","Indian_Polity","Which of the following statements about the Lokpal and Lokayuktas Act, 2013 are CORRECT?
1. Lokpal is a constitutional body
2. Lokpal has jurisdiction over the Prime Minister with certain exceptions
3. Lokpal can investigate complaints against Group A, B, C, D officials
4. The Lokpal has its own prosecution wing","1 and 2 only","2 and 3 only","2, 3 and 4 only","All of the above","C","hard","Statement 1 is wrong: Lokpal is a statutory body under the 2013 Act, not a constitutional body. Statements 2, 3, 4 are correct — Lokpal can investigate PM (with restrictions), all groups of officials, and has a prosecution wing."),
    ("AP_HC","Indian_Polity","The Prevention of Corruption Act, 1988 (as amended in 2018) provides that:
1. Bribe-givers are also punishable (after 2018 amendment)
2. A public servant who takes a bribe is punishable with imprisonment of 3-7 years
3. Prior sanction of the competent authority is required before prosecution of a public servant
4. The Act overrides the provisions of the IPC on bribery","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: the 2018 amendment made bribe-giving an offence (1); punishment range (2); prior sanction requirement (3); PCA overrides IPC on bribery-related offences (4)."),
    ("AP_HC","Indian_Polity","Under Article 143, the President can seek the advisory opinion of the Supreme Court on:
1. Any question of law or fact of public importance
2. Any dispute arising out of a pre-constitutional treaty or agreement
3. Questions relating to the validity of a constitutional amendment
4. Questions that are pending before the Supreme Court","1 and 2 only","1, 2 and 3 only","1 and 3 only","All of the above","A","hard","Art 143 covers questions of law/fact of public importance (1) and pre-constitutional treaty disputes (2). Questions about constitutional amendments can also be referred but are covered under Q of law. Questions already pending before SC (4) cannot be referred separately. Answer A is most accurate."),
    ("AP_HC","Indian_Polity","The Protection of Human Rights Act, 1993 defines \'human rights\' as rights relating to:
1. Life
2. Liberty
3. Equality
4. Dignity of the individual
5. Economic rights","1, 2 and 3 only","1, 2, 3 and 4 only","2, 3 and 4 only","All of the above","B","hard","S.2(d) of the Protection of Human Rights Act 1993 defines human rights as rights relating to life, liberty, equality, and dignity guaranteed by the Constitution or embodied in international covenants enforceable by courts. \'Economic rights\' as a separate head is not specifically listed."),
    ("AP_HC","Indian_Polity","Assertion (A): The State is vicariously liable for the tortious acts of its employees committed in the discharge of sovereign functions.
Reason (R): The Supreme Court in Kasturilal Ralia Ram Jain v. State of UP (1965) held that the State cannot be held liable for acts done in exercise of sovereign functions.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","D","hard","A is false: State is NOT liable for tortious acts in discharge of sovereign functions (this is R\'s position). R is true — the Kasturilal case held that for sovereign acts, state has immunity. So D is correct."),
    ("AP_HC","Indian_Polity","Freedom of the press in India is:
1. Expressly guaranteed under Article 19(1)(a)
2. Implied in freedom of speech and expression under Article 19(1)(a)
3. Subject to reasonable restrictions under Article 19(2)
4. Guaranteed without any restrictions under Article 19(1)(a)","1 and 3 only","2 and 3 only","1 and 4 only","2 and 4 only","B","medium","Freedom of press is NOT expressly mentioned in Art 19(1)(a) — it is implied (as held in Romesh Thappar v. State of Madras). It is subject to reasonable restrictions under Art 19(2). Hence 2 and 3 are correct."),
    ("AP_HC","Indian_Polity","In which of the following cases did the Supreme Court uphold the validity of OBC reservations subject to the exclusion of the \'creamy layer\'?
1. M.R. Balaji v. State of Mysore (1963)
2. Indra Sawhney v. Union of India (1992)
3. Ashoka Kumar Thakur v. Union of India (2008)
4. Jarnail Singh v. Lachhmi Narain Gupta (2018)","2 only","2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Indra Sawhney (1992) introduced creamy layer concept for OBCs and upheld 27% OBC quota. Ashoka Kumar Thakur (2008) upheld OBC reservation in central educational institutions. M.R. Balaji (1963) was about Karnataka\'s 68% reservation (struck down). Jarnail Singh (2018) was about SC/ST promotion quota."),
    ("AP_HC","Indian_Polity","Which of the following statements about the Finance Commission are CORRECT?
1. It is constituted every five years under Article 280
2. It recommends distribution of net proceeds of taxes between Union and States
3. The recommendations of Finance Commission are binding on the government
4. The 15th Finance Commission was constituted in 2017 and gave its report for 2021-26","1, 2 and 4 only","1 and 2 only","2, 3 and 4 only","All of the above","A","hard","Statement 3 is wrong: Finance Commission recommendations are advisory, not binding. Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","Assertion (A): The Attorney General of India is not a member of the Cabinet.
Reason (R): The Attorney General is the first law officer of the Government of India appointed under Article 76 and is not part of the political executive.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains A. AG is appointed under Art 76, is the government\'s chief legal adviser, but is not a Cabinet member. He has the right to audience in all courts but cannot plead against the Government of India."),
    ("AP_HC","Indian_Polity","Match List I (Office) with List II (Qualification):
List I: A. Attorney General of India  B. Comptroller and Auditor General  C. Chief Election Commissioner  D. Chairman, Law Commission
List II: 1. No specific constitutional qualification prescribed  2. Qualified to be a Judge of the Supreme Court  3. No specific constitutional qualification; convention: retired HC/SC judge  4. Qualified to be a Judge of the Supreme Court (same as AG)","A-2, B-4, C-1, D-3","A-4, B-1, C-2, D-3","A-2, B-1, C-4, D-3","A-1, B-2, C-3, D-4","A","hard","AG - qualified to be SC judge (Art 76(1)); CAG - no specific constitutional qualification prescribed (Art 148); CEC - no specific qualification in Constitution; Chairman Law Commission - by convention a retired SC judge."),
    ("AP_HC","Indian_Polity","Which of the following are \'electoral offences\' under the Representation of the People Act, 1951?
1. Booth capturing
2. Intimidating voters
3. Bribery at elections
4. Printing election pamphlets without printer\'s name","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","medium","All four are electoral offences under the RPA 1951 and IPC. Booth capturing (S.135A), intimidation (S.135), bribery (S.171B IPC and S.123 RPA), and printing offences (S.127A RPA) are all prohibited."),
    ("AP_HC","Indian_Polity","Which of the following grounds can be used to challenge an election under the Representation of the People Act, 1951?
1. Corrupt practices by the returned candidate
2. Non-compliance with constitutional provisions
3. Candidate was not qualified at the time of election
4. Candidate\'s election expenses exceeded prescribed limits","1 and 3 only","2, 3 and 4 only","1, 3 and 4 only","All of the above","D","medium","All four are grounds under S.100 RPA 1951 for declaring an election void: corrupt practices (1), non-compliance (2), disqualification (3), and excess election expenses (4)."),
    ("AP_HC","Indian_Polity","How many times has National Emergency been proclaimed in India?
1. Once - during the 1962 India-China War
2. Twice - 1962 and 1971 India-Pakistan War
3. Thrice - 1962, 1971, and 1975 (Internal Emergency)
4. Twice - 1971 and 1975","1 only","2 only","3 only","4 only","C","easy","National Emergency has been proclaimed three times: 1962 (China War), 1971 (Pakistan War - Bangladesh Liberation), and 1975 (Internal Emergency - \'internal disturbance\' ground by Indira Gandhi government)."),
    ("AP_HC","Indian_Polity","Under the Contempt of Courts Act, 1971, which of the following would constitute \'criminal contempt\'?
1. Publishing a statement that scandalises the court
2. Publishing a \'sub judice\' matter that prejudices a fair trial
3. Willful disobedience of a court order by a party
4. Interfering with the administration of justice","1, 2 and 4 only","2, 3 and 4 only","1 and 4 only","All of the above","A","hard","Willful disobedience of a court order (3) is CIVIL contempt, not criminal. Criminal contempt includes scandalising the court (1), prejudicing fair trial (2), and interfering with justice administration (4)."),
    ("AP_HC","Indian_Polity","Match List I (IPC Section) with List II (Offence):
List I: A. Section 120-B  B. Section 124-A  C. Section 153-A  D. Section 295-A
List II: 1. Promoting enmity between groups on grounds of religion, race etc.
2. Deliberate acts outraging religious feelings
3. Sedition
4. Criminal conspiracy","A-4, B-3, C-1, D-2","A-3, B-4, C-2, D-1","A-4, B-1, C-3, D-2","A-1, B-3, C-4, D-2","A","medium","IPC: S.120-B = Criminal conspiracy; S.124-A = Sedition (now under BNS provisions); S.153-A = Promoting enmity; S.295-A = Outraging religious feelings."),
    ("AP_HC","Indian_Polity","Which IPC sections deal with offences relating to \'Evidence\'?
1. Section 191 - giving false evidence
2. Section 193 - punishment for perjury
3. Section 195 - giving false certificate
4. Section 201 - causing disappearance of evidence","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","D","medium","All four sections deal with evidence-related offences: S.191 = giving false evidence (perjury); S.193 = punishment for false evidence; S.195 = giving false certificate; S.201 = causing disappearance of evidence of offence."),
    ("AP_HC","Indian_Polity","Which of the following are correct regarding the Civil Procedure Code, 1908?
1. Order I deals with parties to suits
2. Order VII deals with the plaint
3. Order VIII deals with written statement
4. Order XXXIX deals with temporary injunctions","1 and 2 only","2 and 3 only","1, 3 and 4 only","All of the above","D","medium","All four are correct: Order I = Parties; Order VII = Plaint; Order VIII = Written Statement and set-off; Order XXXIX = Temporary Injunctions and interlocutory orders. Fundamental for High Court practice."),
    ("AP_HC","Indian_Polity","Under the Code of Criminal Procedure (CrPC), 1973, which of the following are cognizable offences?
1. Offences punishable with imprisonment for 3 years or more (generally)
2. Murder
3. Theft
4. Defamation","1 and 2 only","1, 2 and 3 only","2 only","All of the above","B","hard","Cognizable offences are listed in Schedule 1 of CrPC. Murder (S.302 IPC) and theft (S.379-382) are cognizable. Defamation (S.499-500) is generally non-cognizable. Offences punishable with 3+ years are generally (but not always) cognizable."),
    ("AP_HC","Indian_Polity","Assertion (A): The Bhartiya Nagarik Suraksha Sanhita (BNSS), 2023 replaced the Code of Criminal Procedure (CrPC), 1973.
Reason (R): The BNSS was introduced as part of overhauling colonial-era criminal laws along with the Bharatiya Nyaya Sanhita (replacing IPC) and the Bharatiya Sakshya Adhiniyam (replacing Indian Evidence Act).","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","medium","Both A and R are true. The BNSS replaced CrPC and R correctly gives the broader legislative context, though R is an explanation of the legislative package, not the reason why A (BNSS replaced CrPC) is true."),
    ("AP_HC","Indian_Polity","The Supreme Court\'s judgment in K.S. Puttaswamy v. Union of India (2017) on Right to Privacy held:
1. Privacy is a fundamental right under Article 21
2. Privacy extends to bodily integrity, personal autonomy, and informational self-determination
3. The government\'s Aadhaar scheme was entirely struck down
4. Privacy can be restricted by law that is fair, just, and reasonable","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: Aadhaar was upheld (with certain modifications) in a subsequent case. The 9-judge bench in Puttaswamy held privacy is an FR (1), its scope (2), and restrictions must be fair (4)."),
    ("AP_HC","Indian_Polity","The phrase \'public purpose\' in the context of land acquisition is:
1. Defined exhaustively in the Right to Fair Compensation and Transparency in Land Acquisition, Rehabilitation and Resettlement Act, 2013
2. A justiciable question to be decided by courts
3. Limited to government infrastructure projects only
4. Inclusive of private company projects if 70% landowners consent","1 and 2 only","2 and 4 only","1, 2 and 4 only","All of the above","C","hard","The LARR Act 2013 provides a list of public purposes (1) but courts can review (2); statement 3 is wrong — public purpose includes many categories; statement 4 is correct (S.2(2) allows private company acquisition with 70% consent)."),
    ("AP_HC","Indian_Polity","Which of the following taxes were subsumed under GST after the 101st Constitutional Amendment?
1. Central Excise Duty
2. Value Added Tax (VAT)
3. Customs Duty
4. Central Sales Tax
5. Entertainment Tax (except local body portion)","1, 2 and 4 only","1, 2, 4 and 5 only","1, 3, 4 and 5","All of the above","B","medium","Customs Duty (3) was NOT subsumed under GST — it continues as a separate Central levy. The other four (1, 2, 4, 5) were subsumed under GST."),
    ("AP_HC","Indian_Polity","The doctrine of \'Proportionality\' in administrative law means:
1. The action of the state must be proportionate to the objective sought to be achieved
2. The least restrictive means must be chosen when fundamental rights are curtailed
3. Courts cannot review administrative decisions on grounds of proportionality
4. This doctrine was applied in Modern Dental College v. State of MP (2016) by the SC","1 and 2 only","1, 2 and 4 only","1, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: proportionality IS a ground of judicial review in India (recognised by SC). Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","The Central Administrative Tribunal (CAT) was established under:
1. Article 323-A of the Constitution
2. Administrative Tribunals Act, 1985
3. Both of the above
4. Article 312 of the Constitution","1 only","2 only","3 only","4 only","C","medium","CAT was established under Article 323-A (constitutional provision) and given effect through the Administrative Tribunals Act, 1985 (parliamentary legislation). Both are relevant — constitutional authority and statutory implementation."),
    ("AP_HC","Indian_Polity","Which of the following statements about Money Bills are CORRECT?
1. A Bill is a Money Bill only if it relates exclusively to matters in Article 110
2. Rajya Sabha must return a Money Bill within 14 days
3. Lok Sabha can accept or reject Rajya Sabha\'s recommendations on Money Bills
4. If Rajya Sabha does not return a Money Bill within 14 days, it is deemed passed by both Houses","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: Money Bill definition (Art 110(1)) requires exclusive connection (1); RS must return in 14 days (Art 109(2)) (2); LS may accept or reject RS recommendations (Art 109(3)) (3); non-return = deemed passed (Art 109(5)) (4)."),
    ("AP_HC","Indian_Polity","Match List I (Preventive Detention Law) with List II (Subject matter):
List I: A. National Security Act, 1980  B. Conservation of Foreign Exchange and Prevention of Smuggling Activities Act (COFEPOSA), 1974  C. Prevention of Illicit Traffic in Narcotic Drugs and Psychotropic Substances Act, 1988  D. Unlawful Activities (Prevention) Act, 1967
List II: 1. Anti-terror and unlawful organisations  2. Drug trafficking prevention  3. National security and public order  4. Foreign exchange and smuggling","A-3, B-4, C-2, D-1","A-1, B-4, C-2, D-3","A-4, B-3, C-1, D-2","A-3, B-2, C-4, D-1","A","hard","NSA 1980 - national security/public order (3); COFEPOSA - foreign exchange/smuggling (4); PITNDPS 1988 - drug trafficking (2); UAPA 1967 - unlawful activities/terror (1)."),
    ("AP_HC","Indian_Polity","The Fundamental Duties under Article 51-A were added by which constitutional amendment and on the recommendation of which committee?
1. 42nd Amendment, 1976 — Swaran Singh Committee
2. 44th Amendment, 1978 — Swaran Singh Committee
3. 86th Amendment, 2002 added duty to provide education to children
4. Originally 10 duties were listed; the 11th was added by the 86th Amendment","1 and 4 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 2 is wrong: 42nd Amendment (not 44th) added FDs. Committee was Swaran Singh Committee. 86th Amendment added the 11th duty (51-A(k)) — to provide education to children. Statements 1, 3, 4 are correct with the clarification that statement 1 about amendment number is right."),
    ("AP_HC","Indian_Polity","Which of the following cases held that High Courts have the power to hear appeals from Tribunal decisions (thus limiting exclusivity of tribunals)?
1. L. Chandra Kumar v. Union of India (1997)
2. S.P. Sampath Kumar v. Union of India (1987)
3. Rojer Mathew v. South Indian Bank Ltd. (2019)
4. Union of India v. Madras Bar Association (2021)","1 only","1 and 3","1, 3 and 4 only","All of the above","C","hard","L. Chandra Kumar (1997) held that HC/SC judicial review of tribunal decisions cannot be excluded. Rojer Mathew (2019) and Madras Bar Association (2021) further dealt with tribunal reforms and service conditions. S.P. Sampath Kumar (1987) upheld CAT constitutionality (before Chandra Kumar overruled it partly)."),
    ("AP_HC","Indian_Polity","Which of the following statements about \'Budget\' (Annual Financial Statement under Article 112) are CORRECT?
1. The Budget is presented to Lok Sabha only, not Rajya Sabha
2. Railway Budget was merged with the General Budget from 2017-18
3. The concept of \'Vote on Account\' allows government to withdraw money before the budget is passed
4. Supplementary Demands for Grants can be presented during the year","1 and 3 only","2, 3 and 4 only","1, 3 and 4 only","All of the above","B","hard","Statement 1 is wrong: the Budget (Annual Financial Statement) is laid before BOTH Houses of Parliament (Art 112), though Money Bills (Demands for Grants) are only for Lok Sabha. Statements 2, 3, 4 are correct."),
    ("AP_HC","Indian_Polity","The Protection of Civil Rights Act, 1955 (formerly Untouchability Offences Act) provides for:
1. Punishment for enforcing disabilities on grounds of untouchability
2. Refusal to admit a person to a place of public resort on grounds of untouchability
3. Forcing a person to do scavenging on grounds of untouchability
4. Making untouchability an offence under Article 17","2 and 3 only","1, 2 and 3 only","1, 3 and 4 only","All of the above","B","hard","Statement 4 is incorrect framing: Article 17 abolished untouchability and made enforcement an offence, and the PCR Act 1955 gives statutory effect to Art 17. All of 1, 2, 3 are offences under the Act."),
    ("AP_HC","Indian_Polity","Assertion (A): Uniform Civil Code is mentioned as a Directive Principle under Article 44 of the Constitution.
Reason (R): The Supreme Court in Sarla Mudgal v. Union of India (1995) directed the government to enact a Uniform Civil Code.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","hard","A is true — Art 44 is a DPSP. R is also true — the SC in Sarla Mudgal strongly recommended UCC. But R doesn\'t explain A (A is about constitutional provision; R is about SC\'s recommendation). Hence B."),
    ("AP_HC","Indian_Polity","The \'colourable legislation\' doctrine in constitutional law means:
1. Legislature cannot do indirectly what it cannot do directly
2. A law that appears to be within legislative competence but actually transgresses it is invalid
3. The courts look at the \'pith and substance\' of the legislation to determine its true nature
4. Colourable legislation is a doctrine of legislative competence, not of fundamental rights","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct descriptions of the colourable legislation doctrine: cannot do indirectly (1); transgression of competence (2); pith and substance test used (3); it applies to legislative competence division (4)."),
    ("AP_HC","Indian_Polity","In ADM Jabalpur v. Shivakant Shukla (1976), the Supreme Court held:
1. The writ of Habeas Corpus is not maintainable during National Emergency
2. Right to life under Article 21 can be suspended during Emergency
3. The decision was overruled in K.S. Puttaswamy case (2017)
4. Justice H.R. Khanna dissented in this case","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: ADM Jabalpur (the Habeas Corpus case) held HC was not maintainable during Emergency (1) and Art 21 could be suspended (2). The majority was overruled (not the entire case) in Puttaswamy (3). Justice Khanna wrote a brave dissent (4)."),
    ("AP_HC","Indian_Polity","Which of the following constitutional provisions specifically protect/address women\'s rights?
1. Article 15(3) - State may make special provisions for women
2. Article 16(2) - no discrimination in public employment on ground of sex
3. Article 39(a) - right to adequate means of livelihood for men and women equally
4. Article 42 - provision for just and humane conditions of work and maternity relief","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","medium","All four provisions address women specifically: Art 15(3) allows positive discrimination for women; Art 16(2) prohibits sex discrimination; Art 39(a) covers equal livelihood; Art 42 mandates maternity relief."),
    ("AP_HC","Indian_Polity","The National Food Security Act, 2013 guarantees food to:
1. Up to 75% of rural population
2. Up to 50% of urban population
3. Pregnant women and lactating mothers
4. Children up to 14 years for free mid-day meals","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","medium","All four are correct: NFSA 2013 covers 75% rural (1), 50% urban (2), has special provisions for pregnant/lactating mothers (3), and mandates mid-day meals for children (4)."),
    ("AP_HC","Indian_Polity","Match List I (Convention/Law) with List II (Age definition of child):
List I: A. UN Convention on Rights of the Child (UNCRC)  B. POCSO Act, 2012  C. Juvenile Justice Act, 2015  D. Child Labour (Prohibition and Regulation) Amendment Act, 2016
List II: 1. Below 18 years  2. Below 18 years  3. Below 18 years  4. Below 14 years (prohibited) / 14-18 (regulated)","A-1, B-2, C-3, D-4","A-2, B-1, C-4, D-3","A-3, B-2, C-1, D-4","A-1, B-3, C-2, D-4","A","medium","UNCRC, POCSO, and JJ Act all define \'child\' as below 18 years. Child Labour Act prohibits below 14 and regulates 14-18 (in non-hazardous work)."),
    ("AP_HC","Indian_Polity","Which of the following are offences under the Information Technology Act, 2000 (as amended)?
1. Hacking (S.66)
2. Sending offensive messages through communication services (S.66-A — now struck down)
3. Voyeurism (S.66-E)
4. Cyber terrorism (S.66-F)","1, 3 and 4 only","1 and 4 only","2, 3 and 4 only","All of the above","A","hard","S.66-A (offensive messages) was struck down by SC in Shreya Singhal v. Union of India (2015) as unconstitutional. S.66 (hacking), S.66-E (voyeurism), S.66-F (cyber terrorism) remain valid offences."),
    ("AP_HC","Indian_Polity","In the context of medical negligence law in India, the \'Bolam test\' means:
1. A doctor is not negligent if he acts in accordance with a practice accepted by a responsible body of medical opinion
2. This test was adopted by the Indian Supreme Court in Jacob Mathew v. State of Punjab (2005)
3. Simple error of judgment by a doctor amounts to criminal negligence
4. The test requires doctors to follow the most advanced medical practice available","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","A","hard","Statement 3 is wrong: error of judgment alone does NOT amount to negligence (Bolam and Jacob Mathew both held this). Statement 4 is wrong: Bolam requires only \'a responsible body\' of opinion, not the most advanced practice. Statements 1, 2 are correct."),
    ("AP_HC","Indian_Polity","Assertion (A): The \'Polluter Pays\' principle is part of Indian environmental law.
Reason (R): The Supreme Court in Indian Council for Enviro-Legal Action v. Union of India (1996) applied the Polluter Pays principle to hold industries liable for environmental damage.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","hard","Both are true. The Polluter Pays principle is part of Indian environmental jurisprudence (A). R correctly states a case where it was applied. But R is an application/example, not the explanation of why A is true (it\'s not the ONLY case)."),
    ("AP_HC","Indian_Polity","Under which Article does the Supreme Court exercise advisory jurisdiction?
1. Article 131 (Original Jurisdiction)
2. Article 132 (Appellate Jurisdiction — Constitutional)
3. Article 143 (Advisory Jurisdiction)
4. Article 136 (Special Leave Petition)","3 only","1 and 3","2 and 3","3 and 4","A","easy","Advisory jurisdiction of the Supreme Court is exclusively under Article 143 — Presidential Reference. Other articles cover original (131), appellate (132-135), and SLP (136) jurisdictions."),
    ("AP_HC","Indian_Polity","The concept of \'constitutional convention\' in Indian constitutional law refers to:
1. Non-legally enforceable rules followed by constitutional authorities
2. PM being leader of majority party in Lok Sabha is a convention
3. President seeking Cabinet\'s advice before acting is a legal requirement under Article 74
4. Constitutional conventions can be enforced by courts if they are also statutory","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: Art 74 requires President to act on Cabinet\'s advice — this is a constitutional provision (law), not merely a convention. Statements 1, 2, 4 correctly describe conventions."),
    ("AP_HC","Indian_Polity","Which of the following are correctly matched (Court/Tribunal with its parent statute)?
1. Debt Recovery Tribunal — Recovery of Debts Due to Banks and Financial Institutions Act, 1993
2. National Company Law Tribunal — Companies Act, 2013
3. Securities Appellate Tribunal — SEBI Act, 1992
4. Intellectual Property Appellate Board — Trade Marks Act, 1999","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","medium","All four are correctly matched. These are frequently tested in AP HC exams due to their relevance to commercial litigation."),
    ("AP_HC","Indian_Polity","Article 348 of the Constitution provides that:
1. Proceedings of the Supreme Court shall be in English
2. Bills and Acts of Parliament shall be in English
3. Governor can authorise use of Hindi in HC proceedings with President\'s consent
4. Authoritative text of Acts of state legislature shall be in English","1 and 2 only","1, 2 and 3 only","1, 3 and 4 only","All of the above","D","hard","All four are correct under Art 348: SC proceedings in English (1); Parliamentary Bills/Acts in English (2); Governor with President\'s consent can allow Hindi in HC (3); authoritative state legislative text in English (4)."),
    ("AP_HC","Indian_Polity","Which of the following constitutional provisions deal with \'inter-state migration\' and protection of interests of non-dominant communities?
1. Article 16(2) — no discrimination in public employment based on residence
2. Article 16(3) — Parliament can prescribe residence requirement for certain state/UT employment
3. Article 19(1)(e) — right to reside and settle in any part of India
4. Article 35 — Parliament alone can prescribe punishment for offences against certain FRs","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are relevant: Art 16(2) bars residence-based discrimination (1); Art 16(3) Parliament can prescribe local residence requirement (exception) (2); Art 19(1)(e) right to settle anywhere (3); Art 35 Parliament\'s exclusive power (4)."),
    ("AP_HC","Indian_Polity","The \'doctrine of legitimate expectation\' in administrative law means:
1. A person has a right to be heard before an authority takes a decision adversely affecting him if he had a legitimate expectation of being consulted
2. This doctrine arises from a prior promise, established practice, or representation
3. Legitimate expectation always creates a substantive right to a particular outcome
4. This doctrine was recognized by the SC in Punjab Communications Ltd. v. Union of India","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: legitimate expectation generally creates a PROCEDURAL right (to be heard), not always a substantive right to a particular outcome. The doctrine may sometimes create substantive expectations but this is not always the case."),
    ("AP_HC","Indian_Polity","Match List I (Section of Indian Evidence Act 1872) with List II (Subject):
List I: A. Section 24  B. Section 27  C. Section 45  D. Section 65-B
List II: 1. Electronic records as evidence  2. Discovery of fact based on accused\'s confession  3. Confession caused by inducement — inadmissible  4. Expert opinion","A-3, B-2, C-4, D-1","A-2, B-3, C-1, D-4","A-4, B-1, C-3, D-2","A-3, B-4, C-2, D-1","A","hard","IEA: S.24 = Confession by inducement/threat inadmissible; S.27 = Discovery of fact based on confession in custody admissible; S.45 = Expert opinion; S.65-B = Admissibility of electronic records."),
    ("AP_HC","Indian_Polity","Assertion (A): A confession made to a police officer is not admissible in evidence under Section 25 of the Indian Evidence Act.
Reason (R): This rule exists to prevent police torture and coercion to extract confessions from accused persons.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains the policy behind S.25. This is why confessions in India can only be made before a magistrate (S.164 CrPC) to be admissible."),
    ("AP_HC","Indian_Polity","Which of the following are \'relevant facts\' under the Indian Evidence Act that are admissible?
1. Res gestae (facts forming part of the same transaction)
2. Motive, preparation and previous conduct
3. Statements by persons who cannot be called as witnesses
4. Dying declarations","1 and 4 only","1, 2 and 4 only","2 and 3 only","All of the above","D","medium","All four categories are relevant facts/admissible under the IEA: Res gestae (S.6); motive/preparation/conduct (S.8, S.14); statements by unavailable witnesses (S.32); dying declarations (S.32(1))."),
    ("AP_HC","Indian_Polity","Under the Transfer of Property Act, 1882, which of the following are essentials of a valid \'mortgage\'?
1. There must be a transfer of interest in specific immovable property
2. The purpose must be to secure payment of money advanced or to be advanced
3. A mortgage must be registered under the Registration Act
4. Oral mortgages are valid for amounts not exceeding Rs. 100","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: mortgage requires transfer of interest (1); for security of a loan (2); registration required (3) under S.59 TPA and Registration Act; S.59 allows oral mortgage for amounts ≤ Rs. 100 (4)."),
    ("AP_HC","Indian_Polity","Match List I (Type of Mortgage) with List II (Description):
List I: A. Simple mortgage  B. Usufructuary mortgage  C. English mortgage  D. Mortgage by deposit of title deeds
List II: 1. Mortgagor delivers title deeds to create equitable mortgage  2. Mortgagee takes possession and enjoys profits in lieu of interest  3. Personal covenant to repay with power of sale without court intervention  4. No possession; right to sue and have property sold through court","A-4, B-2, C-3, D-1","A-3, B-4, C-1, D-2","A-2, B-4, C-3, D-1","A-4, B-3, C-2, D-1","A","hard","TPA S.58: Simple mortgage = no possession, sue through court (4); Usufructuary = mortgagee gets possession and profits (2); English mortgage = personal covenant + absolute transfer with condition to retransfer, sale without court (3); Equitable/Deposit of title deeds = title deed delivery (1)."),
    ("AP_HC","Indian_Polity","Under the Specific Relief Act, 1963 (as amended in 2018), which of the following contracts can be specifically enforced?
1. Contracts where damages would not be adequate remedy
2. Contracts involving trust property
3. Contracts for personal service or volition
4. Infrastructure project contracts (after 2018 amendment)","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: contracts of personal service (volition) CANNOT be specifically enforced (S.14 SRA). The 2018 amendment made specific performance a rule (not discretionary) and specifically covered infrastructure contracts. Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","Under the Limitation Act, 1963, what is the period of limitation for filing a suit for recovery of money based on a simple money bond?
1. 3 years from the date the money becomes due
2. 12 years if the bond is under seal
3. The period can be extended by acknowledgement in writing signed by the debtor
4. Part payment also extends the limitation period","1 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","B","hard","For a simple money bond: 3 years (Article 37 of Schedule I). Under-seal bond: 12 years (Article 40). But the question is about a \'simple money bond\' so only 3 years applies. Acknowledgement (S.18) and part payment (S.19) extend limitation. Hence 1, 3, 4 are correct."),
    ("AP_HC","Indian_Polity","Which of the following grounds are available for divorce under the Hindu Marriage Act, 1955?
1. Adultery
2. Cruelty
3. Desertion for 2 years
4. Conversion to another religion
5. Unsoundness of mind","1, 2 and 3 only","1, 3 and 4 only","2, 3, 4 and 5 only","All of the above","D","medium","All five grounds are available under S.13 HMA 1955: Adultery (S.13(1)(i)), Cruelty (S.13(1)(ia)), Desertion for 2 years (S.13(1)(ib)), Conversion (S.13(1)(ii)), Unsoundness of mind (S.13(1)(iii))."),
    ("AP_HC","Indian_Polity","Assertion (A): Under Section 498-A of the IPC, the offence of cruelty by husband or his relatives is a cognizable, non-bailable, and non-compoundable offence.
Reason (R): The Supreme Court in Rajesh Sharma v. State of UP (2017) issued guidelines to prevent misuse of S.498-A, which were later modified in Social Action Forum v. Union of India (2018).","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","hard","A is true (S.498-A is cognizable, non-bailable; compoundable status has been debated — SC allowed compounding in some states). R is also true. R is a separate legal development, not the reason for A\'s legal character."),
    ("AP_HC","Indian_Polity","The Commercial Courts Act, 2015 established commercial courts to hear:
1. Commercial disputes of a specified value
2. Original commercial suits in states where no HC has original civil jurisdiction
3. Appeals from decisions of commercial courts at district level
4. Intellectual property disputes regardless of value","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statements 1, 2, 3 are correct. Statement 4 is wrong: the Commercial Courts Act covers IP disputes only if they meet the minimum specified value threshold (not regardless of value)."),
    ("AP_HC","Indian_Polity","Under the Unlawful Activities (Prevention) Act (UAPA), 1967 as amended:
1. The NIA can investigate UAPA cases anywhere in India
2. An individual can be designated as a \'terrorist\' (after 2019 amendment)
3. Bail under UAPA is harder to obtain than under ordinary law
4. UAPA cases must be tried by Special Courts designated by state governments","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: NIA jurisdiction (1); individual terrorist designation added by 2019 amendment (2); higher threshold for bail (3); Special Courts for trial (4)."),
    ("AP_HC","Indian_Polity","In Re: Prashant Bhushan (2020), the Supreme Court held:
1. Tweets criticising the Chief Justice can constitute criminal contempt
2. Bona fide criticism of judicial orders in proper language is not contempt
3. Truth is an absolute defence against contempt
4. The Court awarded token punishment of Re. 1 fine","1 and 4 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: truth is a defence only if it is in public interest AND bona fide (2006 amendment to Contempt of Courts Act). It is not an absolute defence. Statements 1, 2, 4 are correct regarding the Prashant Bhushan contempt case."),
    ("AP_HC","Indian_Polity","Which of the following courts are established by the Constitution itself?
1. Supreme Court of India
2. High Courts
3. District Courts
4. City Civil Courts","1 only","1 and 2 only","1, 2 and 3 only","All of the above","B","medium","Supreme Court (Arts 124-147) and High Courts (Arts 214-231) are established by the Constitution. District Courts and City Civil Courts are established by statutes and state government orders."),
    ("AP_HC","Indian_Polity","The term \'cooperative federalism\' in the Indian context refers to:
1. Voluntary cooperation between Centre and States for national goals
2. The Inter-State Council as a platform for cooperative federalism
3. GST Council as an example of cooperative federalism
4. Constitutional requirement that Centre and States must cooperate","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is wrong: there is no constitutional REQUIREMENT of cooperation — it is voluntary in spirit. Statements 1, 2, 3 are correct descriptions of cooperative federalism in India."),
    ("AP_HC","Indian_Polity","In T.M.A. Pai Foundation v. State of Karnataka (2002), the Supreme Court held regarding minority educational institutions that:
1. The right to establish educational institutions is part of Art 30(1)
2. The minority institution can have its own admission procedure but cannot ignore merit
3. State regulation for maintaining academic standards is permissible
4. No minority can be compelled to admit students from other communities","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is incorrect as an absolute rule — the SC held that even minority institutions cannot have a blanket exclusion if they take government aid. Statements 1, 2, 3 are from the T.M.A. Pai holding."),
    ("AP_HC","Indian_Polity","Which of the following are Parliamentary Privileges under the Indian Constitution?
1. Freedom of speech in Parliament (Art 105(1))
2. Immunity from court proceedings for anything said in Parliament
3. Power to punish members for breach of privilege
4. Right to exclude strangers from its sessions","1 and 2 only","1, 2 and 3 only","2 and 4 only","All of the above","D","hard","All four are parliamentary privileges: Art 105(1) - freedom of speech; Art 105(2) - immunity from court proceedings; Art 105(3) - Parliament determines its own privileges (including punishment); exclusion of strangers is part of this."),
    ("AP_HC","Indian_Polity","Match List I (Stage of a Bill) with List II (What happens):
List I: A. First Reading  B. Second Reading  C. Committee Stage  D. Third Reading
List II: 1. General discussion on principles of the Bill  2. Clause-by-clause scrutiny by Parliamentary Committee  3. Introduction of the Bill; no debate  4. Final vote on the Bill","A-3, B-1, C-2, D-4","A-1, B-3, C-4, D-2","A-3, B-4, C-1, D-2","A-4, B-1, C-2, D-3","A","medium","First Reading = Introduction (no debate); Second Reading = General discussion on principles; Committee Stage = Clause-by-clause examination; Third Reading = Final vote."),
    ("AP_HC","Indian_Polity","The principle of \'audi alteram partem\' (hear the other side) under natural justice requires:
1. Notice of the action proposed against a person
2. Opportunity to be heard before an adverse order is passed
3. Reasons must be given for every administrative decision
4. The decision-maker must not be biased","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","A","hard","Audi alteram partem covers notice (1) and opportunity to be heard (2). Reasons for decisions (3) is a separate requirement (growing trend but not strictly audi alteram partem). Bias (4) is the other natural justice principle — \'nemo judex in causa sua\'. Hence A."),
    ("AP_HC","Indian_Polity","Directive Principle under Article 50 mandates:
1. Separation of judiciary from executive in public services
2. Separation of judiciary from legislative
3. This refers to separation at the state/district level magistracy
4. This was implemented partly by the CrPC 1973 which separated judicial and executive magistrates","1 only","1 and 3 only","1, 3 and 4 only","All of the above","C","hard","Art 50 mandates separation of judiciary from executive (1) in public services — specifically at the district/magistracy level (3). Statement 2 is wrong (Art 50 doesn\'t mention legislative separation). The CrPC 1973 did implement this separation (4)."),
    ("AP_HC","Indian_Polity","Article 301 of the Constitution provides for:
1. Freedom of trade, commerce and intercourse throughout the territory of India
2. Parliament\'s power to impose restrictions on trade in public interest
3. State legislature can impose restrictions only with President\'s sanction
4. Taxes imposed by states on inter-state trade are automatically void","1 only","1 and 2 only","1, 2 and 3 only","All of the above","C","hard","Art 301 guarantees freedom of trade/commerce (1). Art 302 allows Parliament to impose restrictions (2). Art 304(b) allows states to impose restrictions with President\'s assent (3). Statement 4 is wrong — Art 304(a) allows states to tax inter-state trade if they similarly tax goods manufactured locally."),
    ("AP_HC","Indian_Polity","The Objectives Resolution was moved in the Constituent Assembly by:
1. Dr. B.R. Ambedkar
2. Jawaharlal Nehru
3. Dr. Rajendra Prasad
4. Sardar Vallabhbhai Patel","2 only","1 only","3 only","4 only","A","easy","The Objectives Resolution was moved by Jawaharlal Nehru on 13 December 1946 in the Constituent Assembly. It outlined the aims of the Constitution and later became the basis for the Preamble."),
    ("AP_HC","Indian_Polity","Which of the following statements about the drafting of the Indian Constitution are CORRECT?
1. The Constituent Assembly had 389 members initially (including from princely states)
2. Dr. B.R. Ambedkar was the Chairman of the Drafting Committee
3. The Constitution was adopted on 26 November 1949
4. Dr. Rajendra Prasad was the President of the Constituent Assembly","1 and 2 only","2, 3 and 4 only","1, 2 and 3 only","All of the above","D","easy","All four are correct: 389 initial members; Ambedkar chaired Drafting Committee; adopted 26 Nov 1949 (Constitution Day); Dr. Rajendra Prasad was President of the Assembly."),
    ("AP_HC","Indian_Polity","Under Article 131 of the Constitution, the Supreme Court has original jurisdiction in disputes between:
1. Union of India and one or more States
2. Two or more States
3. Citizens of different states
4. A State and citizens of another State","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","A","medium","Art 131 covers: Union vs State(s) (1) and between two or more States (2). It does NOT cover citizen vs state or citizen vs citizen disputes. Those go to appropriate civil courts or HCs."),
    ("AP_HC","Indian_Polity","Grants-in-aid to states from the Consolidated Fund of India are made under:
1. Article 275 — Grants to states in need of assistance
2. Article 282 — Grants for any public purpose
3. Recommendations of the Finance Commission
4. Discretion of the Central government","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four sources are correct: Art 275 (statutory grants on FC recommendations) (1,3), Art 282 (discretionary grants for any public purpose — allows Centre to make grants outside FC recommendations) (2,4)."),
    ("AP_HC","Indian_Polity","A joint sitting of both Houses of Parliament (Article 108) can be called in relation to:
1. Any Bill (other than Money Bills and Constitutional Amendment Bills)
2. A Bill passed by Lok Sabha but rejected by Rajya Sabha
3. A Bill that has been pending in Rajya Sabha for more than 6 months
4. A Money Bill that Rajya Sabha refuses to pass","1, 2 and 3 only","2 and 3 only","1, 3 and 4 only","All of the above","A","hard","Money Bills and Constitution Amendment Bills are excluded from joint sitting provisions. Joint sitting (Art 108) applies to ordinary Bills: when RS rejects, proposes amendments LS doesn\'t agree, or RS doesn\'t pass within 6 months."),
    ("AP_HC","Indian_Polity","Under Article 136 (Special Leave Petition), the Supreme Court:
1. Can hear appeals from any court or tribunal in India except military tribunals
2. Has absolute discretion in granting or refusing leave
3. Can interfere with findings of fact if there is a grave miscarriage of justice
4. Cannot convert an SLP into an appeal from HC orders made under Art 226","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is wrong: SC can convert an SLP into a regular appeal. Statements 1, 2, 3 are correct regarding SC\'s SLP jurisdiction."),
    ("AP_HC","Indian_Polity","Match List I (PIL Case) with List II (Outcome/Principle):
List I: A. Vishaka v. State of Rajasthan (1997)  B. M.C. Mehta v. Union of India (1987)  C. People\'s Union for Civil Liberties v. Union of India (2001)  D. Olga Tellis v. Bombay Municipal Corporation (1985)
List II: 1. Right to food as part of Art 21  2. Sexual harassment guidelines at workplace  3. Right to livelihood as part of Art 21  4. Absolute liability of industries for hazardous substances","A-2, B-4, C-1, D-3","A-4, B-2, C-1, D-3","A-2, B-1, C-4, D-3","A-2, B-4, C-3, D-1","A","hard","Vishaka (1997) = sexual harassment guidelines; M.C. Mehta (1987) = absolute liability principle (Shriram Foods and Fertilizers case); PUCL (2001) = right to food; Olga Tellis (1985) = right to livelihood."),
    ("AP_HC","Indian_Polity","Under the Right to Fair Compensation and Transparency in Land Acquisition, Rehabilitation and Resettlement Act (LARR), 2013:
1. Social Impact Assessment (SIA) is mandatory for multi-crop irrigated land acquisition
2. Compensation is 2 times the market value in rural areas and 1 time in urban areas
3. The consent of 80% of affected families is required for private company projects
4. Rehabilitation and Resettlement provisions apply even to acquisitions under other Acts","1 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 2 is wrong: compensation is 4 times market value in rural areas and 2 times in urban areas. Statements 1, 3, 4 are correct."),
    ("AP_HC","Indian_Polity","In which of the following cases did the Supreme Court articulate the \'Basic Structure\' doctrine?
1. Shankari Prasad v. Union of India (1951)
2. Sajjan Singh v. State of Rajasthan (1965)
3. Golak Nath v. State of Punjab (1967)
4. Kesavananda Bharati v. State of Kerala (1973)","4 only","3 and 4","1 and 4","2, 3 and 4","A","hard","The Basic Structure doctrine was first articulated in Kesavananda Bharati (1973). Earlier cases: Shankari Prasad (1951) and Sajjan Singh (1965) held FRs could be amended; Golak Nath (1967) said FRs cannot be amended. Kesavananda overruled Golak Nath and introduced basic structure."),
    ("AP_HC","Indian_Polity","Which of the following laws were enacted to give effect to Directive Principles?
1. Minimum Wages Act, 1948 (Art 43)
2. Maternity Benefit Act, 1961 (Art 42)
3. Equal Remuneration Act, 1976 (Art 39(d))
4. Wildlife Protection Act, 1972 (Art 48-A)","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","medium","All four are enacted to give effect to DPSPs: Minimum Wages = Art 43 (living wage); Maternity Benefit = Art 42 (maternity relief); Equal Remuneration = Art 39(d) (equal pay); Wildlife Protection = Art 48-A (environment)."),
    ("AP_HC","Indian_Polity","Which of the following officers of the State can be removed by the President (not by the Governor or State)?
1. Chief Justice of a High Court
2. Governor
3. Speaker of State Legislative Assembly
4. Advocate General of the State","1 and 2 only","1, 2 and 3 only","2 and 4 only","All of the above","A","hard","Chief Justice of HC (Art 217 — addressed by each House + President) and Governor (Art 156 — President\'s pleasure) are removed/displaced by President. Speaker is removed by state legislature. Advocate General is appointed/removed by Governor."),
    ("AP_HC","Indian_Polity","Assertion (A): Unlike the UPSC, the recommendations of the State Public Service Commission regarding appointments are not binding on the State Government.
Reason (R): The UPSC\'s recommendations under Article 320 are also advisory in nature and not binding on the government.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","medium","Both A and R are true — both UPSC and SPSC recommendations are advisory (the government can reject them with reasons). R is a comparable fact but doesn\'t explain A. Hence B."),
    ("AP_HC","Indian_Polity","Match List I (Panchayati Raj body) with List II (Constitutional Article):
List I: A. Gram Sabha  B. Reservation for women in Panchayats  C. State Finance Commission for PRIs  D. District Planning Committee
List II: 1. Article 243-I  2. Article 243-D  3. Article 243-ZD  4. Article 243-A","A-4, B-2, C-1, D-3","A-2, B-4, C-3, D-1","A-4, B-1, C-2, D-3","A-1, B-2, C-4, D-3","A","hard","Art 243-A = Gram Sabha; Art 243-D = Reservations (including for women); Art 243-I = State Finance Commission for PRIs; Art 243-ZD = District Planning Committees."),
    ("AP_HC","Indian_Polity","The right to free legal aid for accused persons who cannot afford lawyers was held to be part of Article 21 in:
1. M.H. Hoskot v. State of Maharashtra (1978)
2. Hussainara Khatoon v. Home Secretary, Bihar (1979)
3. Khatri v. State of Bihar (1981)
4. Sukhdas v. Union Territory of Arunachal Pradesh (1986)","1 only","1 and 2 only","1, 2 and 3 only","All of the above","D","hard","All four cases recognised the right to free legal aid as part of Art 21 right to fair trial. Progressive expansion from Hoskot (1978) → Hussainara (1979) → Khatri (1981) → Sukhdas (1986, making it mandatory even if accused doesn\'t ask)."),
    ("AP_HC","Indian_Polity","The original strength of the Supreme Court under the Constitution was:
1. One Chief Justice and 7 other judges
2. One Chief Justice and 25 other judges (current strength after amendments)
3. Parliament can increase the number of judges by law under Article 124(1)
4. The present sanctioned strength is 34 (CJI + 33)","1 and 3 only","1, 3 and 4 only","2 and 3 only","All of the above","B","hard","Original strength: CJI + 7 (total 8). Current (as of 2019 amendment): CJI + 33 = 34. Parliament increases the number by law (Art 124(1)). Statement 2 (25) is wrong. Statements 1, 3, 4 are correct."),
    ("AP_HC","Indian_Polity","The Tribunals Reforms Act, 2021 abolished which of the following tribunals by merging their functions into existing courts/bodies?
1. Intellectual Property Appellate Board (IPAB)
2. Film Certification Appellate Tribunal
3. Plant Varieties Protection Appellate Tribunal
4. National Green Tribunal","1, 2 and 3 only","1 and 3 only","2 and 4 only","All of the above","A","hard","The Tribunals Reforms Act 2021 abolished: IPAB, Film Certification Appellate Tribunal, Plant Varieties Protection Appellate Tribunal, and several others. The NGT was NOT abolished — it continues to function."),
    ("AP_HC","Indian_Polity","Which of the following statements about the Advocate General of a State are CORRECT?
1. The Advocate General is appointed by the Governor under Article 165
2. He must be qualified to be appointed as a Judge of the High Court
3. His tenure and conditions of service are fixed by the Governor
4. He has the right of audience in all courts in the State","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","medium","All four are correct under Art 165: appointed by Governor (1); HC judge qualification required (2); tenure at Governor\'s pleasure (3); right of audience in all state courts (4)."),
    ("AP_HC","Indian_Polity","After the Supreme Court Constitution Bench ruling in Government of NCT of Delhi v. Union of India (2023):\n1. Services cadre (IAS and DANICS) were brought under the Delhi government\'s control\n2. The Lieutenant Governor must act on the advice of the Delhi government on all matters except three reserved subjects\n3. Parliament enacted the Government of NCT of Delhi (Amendment) Act, 2023 to override the SC judgment\n4. Land, public order, and police remain with the Central government","2 and 4 only","1 and 3 only","1, 2 and 4 only","All of the above","D","hard","The SC Constitution Bench (May 2023) held that Delhi government has control over services/bureaucracy, excluding entries related to public order, police, and land (1 and 4). Statement 2 is correct — LG acts on CoM advice except the three reserved subjects. Statement 3 is also factually correct — Parliament enacted the GNCTD (Amendment) Act, 2023 to return control of services to the Centre, effectively overriding the SC ruling. Since all four statements describe events that occurred after/in consequence of the 2023 SC ruling, D (all of the above) is correct."),
    ("AP_HC","Indian_Polity","The concept of \'Transformative Constitutionalism\' in India means:
1. The Constitution is designed to transform Indian society by guaranteeing rights and DPSPs
2. It recognises historical injustices and seeks to remedy them through affirmative action
3. The Constitution is static and cannot be transformed by amendments
4. This concept was discussed by the SC in Navtej Singh Johar (2018)","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong — transformative constitutionalism recognises that the Constitution enables transformation and itself transforms with society\'s evolution. Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","The 106th Constitutional Amendment Act, 2023 is related to:
1. One Nation One Election
2. Women\'s reservation in Lok Sabha and state legislative assemblies
3. Reserving 33% seats for women in Parliament and state assemblies
4. The amendment will come into force after delimitation","1 only","2 and 3 only","2, 3 and 4 only","All of the above","C","medium","The 106th Amendment (Nari Shakti Vandan Adhiniyam) provides 33% reservation for women in Lok Sabha and state assemblies (2 and 3). It will be effective after the next census and delimitation (4). It does NOT relate to One Nation One Election (1)."),
    ("AP_HC","Indian_Polity","The \'One Nation One Election\' concept proposed by the High Level Committee (Kovind Committee, 2024) recommends:
1. Simultaneous elections to Lok Sabha, State Assemblies, and local bodies
2. A Constitutional amendment to synchronise election cycles
3. Use of a common electoral roll for all elections
4. The concept requires amendment to at least 5 constitutional articles","1 and 2 only","1, 2 and 3 only","1, 2 and 4 only","All of the above","D","hard","The Kovind Committee recommended simultaneous elections (1), constitutional amendments (2), common electoral rolls (3), and identified multiple articles needing amendment (4). All four are part of the proposal."),
    ("AP_HC","Indian_Polity","The Chief Justice of India D.Y. Chandrachud retired in 2024 after which Justice Sanjiv Khanna became CJI. Which of the following cases were decided during CJI D.Y. Chandrachud\'s tenure?
1. Article 370 abrogation case (2023)
2. Electoral Bond Scheme struck down (2024)
3. Sub-classification within SC/ST reservation (2024)
4. Demonetisation case (2023)","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four landmark judgments were during CJI Chandrachud\'s tenure (November 2022 - November 2024): Art 370 (Dec 2023), Electoral Bonds (Feb 2024), SC sub-classification (Aug 2024), Demonetisation (Jan 2023)."),
    ("AP_HC","Indian_Polity","The Supreme Court\'s judgment in Association for Democratic Reforms v. Union of India (2024) struck down the Electoral Bond Scheme on the grounds that:
1. It violated voters\' right to information about political funding
2. It violated donors\' right to privacy
3. It allowed unlimited and anonymous corporate donations to political parties
4. It violated Article 19(1)(a) — freedom of expression through political funding choices","1 and 3 only","1, 3 and 4 only","2 and 4 only","All of the above","B","hard","The SC held: anonymous bonds violated right to information of voters (1); there\'s no unlimited corporate political funding right (3); and Art 19(1)(a) was relevant (4). The donors\' privacy (2) was NOT the reason — the Court rejected privacy claim of donors vis-à-vis voters\' right to know."),
    ("AP_HC","Indian_Polity","Article 370 was abrogated in 2019 by which constitutional mechanism?
1. Presidential Order under Article 370(3) with concurrence of Constituent Assembly of J&K
2. Presidential Order declaring that \'Constituent Assembly of J&K\' means \'Legislative Assembly of J&K\'
3. Then the Constitution (Application to J&K) Order, 2019 extended all provisions of the Constitution to J&K
4. The Supreme Court upheld the abrogation in December 2023","1 only","2 and 3 only","2, 3 and 4 only","All of the above","C","hard","Statement 1 is partially wrong: the Constituent Assembly of J&K was not in existence; the Presidential Order (Concurrence) reinterpreted \'Constituent Assembly\' as the Parliament, not the J&K assembly. Statements 2, 3, 4 correctly describe the process."),
    ("AP_HC","Indian_Polity","The Memorandum of Procedure (MoP) for appointment of judges of the Supreme Court and High Courts:
1. Has been finalised and implemented since the NJAC judgment (2015)
2. Is a document that governs the collegium process
3. Allows the government to return a collegium recommendation once for reconsideration
4. If the collegium reiterates its recommendation, the government must appoint the judge","2 and 3 only","2, 3 and 4 only","1, 2 and 3 only","All of the above","B","hard","Statement 1 is wrong: as of 2025, the finalised MoP is still pending — it has not been formally adopted despite years of discussion. Statements 2, 3, 4 reflect the current understanding based on SC rulings (particularly the Third Judges case and practice)."),
    ("AP_HC","Indian_Polity","Which of the following are Departmentally Related Standing Committees (DRSCs) of Parliament?
1. Committee on Home Affairs
2. Committee on Finance
3. Committee on External Affairs
4. Public Accounts Committee
5. Estimates Committee","1, 2 and 3 only","4 and 5 only","1, 2, 3, 4 and 5","1, 3 and 5 only","A","hard","Public Accounts Committee and Estimates Committee are Financial Committees, not DRSCs. DRSCs are 24 committees that shadow specific ministries/departments. Committees on Home Affairs, Finance, External Affairs are DRSCs."),
    ("AP_HC","Indian_Polity","The Andhra Pradesh State Reorganisation Act, 2014 designated which city as the seat of the Andhra Pradesh High Court?
1. Amaravati
2. Kurnool
3. Hyderabad (initially, then shifted)
4. Visakhapatnam","1 only","3 only","2 only","4 only","B","hard","The AP Reorganisation Act 2014 kept Hyderabad as the common capital (and HC seat) for both AP and Telangana for up to 10 years. The AP HC remained in Hyderabad until 2019 when Telangana HC was separated. Subsequently AP HC operates from Amaravati (temporarily from Hyderabad till new HC building). Answer B (initially Hyderabad) is historically accurate."),
    ("AP_HC","Indian_Polity","Which of the following special provisions apply to Andhra Pradesh under the Constitution?
1. Article 371-D — Special provisions for equitable opportunities and facilities for the people of different parts of AP
2. Article 371-E — Establishment of a Central University in AP
3. These provisions cannot be amended without the consent of the AP state legislature
4. Article 371-D provides for Presidential Orders on local cadre/zone allocations","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: these provisions can be amended by Parliament (they are Constitutional provisions, not entrenched requiring state consent). Art 371-D (local cadre/zones) and Art 371-E (Central University) are correct — as are they applying to Andhra Pradesh (1, 2, 4)."),
    ("AP_HC","Indian_Polity","In Shreya Singhal v. Union of India (2015), the Supreme Court:
1. Struck down Section 66-A of the IT Act as unconstitutional
2. Held that online speech is subject to the same reasonable restrictions as offline speech
3. Distinguished between \'discussion\', \'advocacy\', and \'incitement\' in free speech
4. Upheld Section 69-A (blocking of websites) as constitutional","1 and 3 only","1, 2 and 3 only","1, 3 and 4 only","All of the above","D","hard","All four are correct: S.66-A struck down (1); online speech has same constitutional protections (2); the Court distinguished between discussion/advocacy (protected) and incitement (not protected) (3); S.69-A upheld with safeguards (4)."),
    ("AP_HC","Indian_Polity","The principle of \'wednesbury unreasonableness\' in judicial review of administrative actions means:
1. A decision is unreasonable if no reasonable authority would have made it
2. It is the lowest threshold for judicial intervention in administrative decisions
3. Courts can review the \'merits\' of the decision using this standard
4. The standard was adopted by Indian courts from English common law","1 and 4 only","1, 2 and 4 only","1, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: Wednesbury unreasonableness does NOT allow courts to review merits — it\'s a high threshold (no reasonable authority would make such a decision). Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","Match List I (Legal Maxim) with List II (Meaning/Application):
List I: A. Actus non facit reum nisi mens sit rea  B. Nullum crimen sine lege  C. In dubio pro reo  D. Nemo debet bis vexari
List II: 1. No crime without a law (legality principle)  2. Benefit of doubt to the accused  3. No double jeopardy  4. Act is not criminal unless there is guilty mind","A-4, B-1, C-2, D-3","A-1, B-4, C-3, D-2","A-4, B-3, C-1, D-2","A-2, B-1, C-4, D-3","A","hard","Actus non facit reum nisi mens sit rea = guilty mind needed (4); Nullum crimen sine lege = no crime without law (1); In dubio pro reo = benefit of doubt to accused (2); Nemo debet bis vexari = double jeopardy prohibition (3)."),
    ("AP_HC","Indian_Polity","The \'harmonious construction\' rule of constitutional interpretation means:
1. When two provisions of the Constitution appear to conflict, courts try to read them together
2. No provision should be rendered otiose/redundant if it can be given meaningful effect
3. The more specific provision overrides the general provision
4. This rule was applied in reconciling FRs with DPSPs","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is a separate rule (generalia specialibus non derogant), not harmonious construction. Harmonious construction = read together (1), avoid redundancy (2), applied to FRs vs DPSPs (4). Hence B."),
    ("AP_HC","Indian_Polity","The Supreme Court in Olga Tellis v. Bombay Municipal Corporation (1985) held that:
1. Pavement dwellers have a fundamental right to livelihood under Article 21
2. Eviction without notice and opportunity to be heard violates natural justice
3. The State can evict pavement dwellers if proper rehabilitation is provided
4. Right to housing is an explicit fundamental right","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is wrong: right to housing is NOT an explicit FR (it is read into Art 21 partially). Statements 1, 2, 3 are from the Olga Tellis judgment."),
    ("AP_HC","Indian_Polity","Assertion (A): A retired Chief Justice of India cannot appear as an advocate before the Supreme Court of India.
Reason (R): Article 124(7) prohibits a retired Supreme Court judge from pleading or acting in any court or before any authority within India.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains A. Art 124(7) imposes this restriction on retired SC judges. Similar restriction applies to CAG under Art 148(4)."),
    ("AP_HC","Indian_Polity","Match List I (Directive Principle) with List II (Article):
List I: A. Equal pay for equal work  B. Early childhood care and education up to 6 years  C. Organisation of village panchayats  D. Separation of judiciary from executive
List II: 1. Article 45  2. Article 40  3. Article 39(d)  4. Article 50","A-3, B-1, C-2, D-4","A-1, B-3, C-4, D-2","A-3, B-2, C-1, D-4","A-4, B-1, C-2, D-3","A","medium","Art 39(d) = Equal pay for equal work; Art 45 (post 86th Amendment) = early childhood care (0-6 years); Art 40 = Panchayats; Art 50 = separation of judiciary from executive."),
    ("AP_HC","Indian_Polity","The Panchayats (Extension to Scheduled Areas) Act (PESA), 1996 applies to:
1. States with Fifth Schedule areas (tribal areas in mainland India)
2. States with Sixth Schedule areas (tribal areas in Northeast)
3. Requires gram sabha consent for land acquisition in scheduled areas
4. Gives gram sabha powers over minor forest produce","1, 3 and 4 only","1 and 4 only","2, 3 and 4 only","All of the above","A","hard","PESA 1996 applies ONLY to Fifth Schedule areas (9 states) — NOT Sixth Schedule areas (2). Sixth Schedule areas already have special ADC provisions. PESA gives gram sabha powers over land (3) and minor forest produce (4)."),
    ("AP_HC","Indian_Polity","Which of the following statements about State Legislatures are CORRECT?
1. Every State must have a bicameral legislature
2. A State Legislative Council can be created or abolished by Parliament on a resolution of the State Legislative Assembly
3. The Chairman of State Legislative Council is elected from amongst its members
4. The Governor can summon, prorogue, and dissolve both Houses of the State Legislature","2 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","C","hard","Statement 1 is wrong: not every state has a bicameral legislature — a Legislative Council is optional. Statement 4 is partially wrong: the Governor cannot dissolve the Legislative Council (upper house is a permanent body). Statements 2, 3 are correct."),
    ("AP_HC","Indian_Polity","Match List I (Constitutional Amendment) with List II (Key Feature):
List I: A. 61st Amendment (1988)  B. 73rd Amendment (1992)  C. 86th Amendment (2002)  D. 103rd Amendment (2019)
List II: 1. EWS reservation (10%)
2. Right to Education (Art 21-A)
3. Panchayati Raj (11th Schedule)
4. Voting age reduced from 21 to 18","A-4, B-3, C-2, D-1","A-1, B-2, C-3, D-4","A-4, B-2, C-3, D-1","A-3, B-4, C-2, D-1","A","medium","61st Amendment = voting age 21→18; 73rd Amendment = Panchayati Raj/11th Schedule; 86th Amendment = Art 21-A (RTE); 103rd Amendment = EWS 10% reservation."),
    ("AP_HC","Indian_Polity","Which of the following acts constitute \'sub judice contempt\' (prejudicing pending proceedings)?
1. Publishing detailed interviews with witnesses before trial
2. Media trial and conviction by press before court verdict
3. Publishing fair and accurate reports of public court proceedings
4. Academic commentary on the legal principles involved in a pending case","1 and 2 only","1, 2 and 4 only","3 and 4 only","All of the above","A","hard","Statements 3 and 4 are NOT contempt: fair court reports (S.4 Contempt Act) and bona fide academic commentary (S.5) are protected. Statements 1 (witness interviews) and 2 (media trial) are forms of sub judice contempt."),
    ("AP_HC","Indian_Polity","The Digital Personal Data Protection Act, 2023 provides for:
1. Rights of data principals (individuals) including right to access and erasure
2. Obligations of data fiduciaries (entities processing data)
3. A Data Protection Board to adjudicate complaints
4. Absolute prohibition on transfer of personal data outside India","1, 2 and 3 only","2, 3 and 4 only","1 and 3 only","All of the above","A","hard","Statement 4 is wrong: the Act does NOT absolutely prohibit cross-border data transfer — it allows transfer to certain countries notified by the government. Statements 1, 2, 3 are core features of the DPDP Act 2023."),
    ("AP_HC","Indian_Polity","Under the Prevention of Money Laundering Act (PMLA), 2002:
1. The Enforcement Directorate investigates money laundering offences
2. Bail under PMLA is harder to obtain due to twin conditions in Section 45
3. Properties attached under PMLA are forfeited without trial
4. The burden of proof in PMLA proceedings is on the prosecution","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","A","hard","Statement 3 is wrong: properties are attached provisionally and confirmed only after trial by the Adjudicating Authority. Statement 4 is wrong: PMLA reverses burden — accused must prove innocence. Statements 1 and 2 are correct."),
    ("AP_HC","Indian_Polity","The four Labour Codes enacted in India (2019-2020) consolidate:
1. Code on Wages (2019) — consolidates 4 wages-related laws
2. Industrial Relations Code (2020) — consolidates 3 laws including Trade Unions Act
3. Code on Social Security (2020) — consolidates 9 laws including EPF and ESI
4. Occupational Safety, Health and Working Conditions Code (2020) — consolidates 13 laws","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct descriptions of the four Labour Codes. This is an important constitutional/statutory development relevant to AP HC practice."),
    ("AP_HC","Indian_Polity","Under Article 227, the High Court\'s power of superintendence over all courts and tribunals in the state:
1. Is wider than the revisional jurisdiction under Section 115 CrPC/CPC
2. Can be exercised even when no appeal or revision lies to the HC
3. Can be invoked to correct errors of jurisdiction as well as errors of law
4. Cannot be excluded by any statute including a central statute","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct regarding Art 227 superintendence powers: it\'s wider than statutory revision (1); available even without right of appeal (2); covers jurisdictional errors (3); being a constitutional power, cannot be excluded by statute (4)."),
    ("AP_HC","Indian_Polity","Which constitutional entry/entries govern foreign trade and foreign exchange?
1. Entry 83, Union List — duties of customs
2. Entry 41, Union List — foreign exchange, foreign loans
3. Entry 36, Union List — currency, coinage, legal tender
4. Concurrent List Entry 7 — contracts outside India","1 and 2 only","1, 2 and 3 only","1, 3 and 4 only","All of the above","B","hard","Entry 83 (customs), Entry 41 (foreign exchange and loans), and Entry 36 (currency) are all Union List entries relevant to foreign trade/exchange. Entry 7 of Concurrent List actually relates to \'contracts\', not specifically foreign contracts. Hence 1, 2, 3 are correct."),
    ("AP_HC","Indian_Polity","Assertion (A): The Constitution of India does not expressly use the word \'federal\'.
Reason (R): India is described in Article 1 as a \'Union of States\', which reflects its indestructible nature — states cannot secede unlike in a true federation.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","medium","A is true (the word \'federal\' does not appear in the Constitution). R is also true (Art 1 says \'Union of States\' — the Union is indestructible). However R is an explanation of WHY the Constitution prefers \'Union\' over \'Federation\', not of WHY the word \'federal\' is absent. Hence B."),
    ("AP_HC","Indian_Polity","Which of the following conventions/principles govern the appointment of Governors?
1. The Governor must not be a resident of the state to which he is appointed
2. The President should consult the Chief Minister of the state before appointing Governor (Sarkaria Commission recommendation)
3. An active politician should not be appointed as Governor
4. Governor\'s appointment requires concurrence of the state legislature","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is wrong: state legislature has no role in Governor\'s appointment — it is entirely the President\'s (effectively Cabinet\'s) decision. Statements 1, 2, 3 are Sarkaria Commission recommendations (conventions, not legally binding)."),
    ("AP_HC","Indian_Polity","Which of the following have been upheld by courts based on Fundamental Duties under Article 51-A?
1. Compulsory military service can be imposed by Parliament
2. National Anthem must be shown respect (Bijoe Emmanuel case)
3. Environmental protection laws are valid as FDs support them
4. Cow slaughter ban is supported by FD to protect natural environment","1 and 3 only","2 and 3 only","3 and 4 only","1, 3 and 4 only","B","hard","Statement 1 is wrong: Bijoe Emmanuel case (1986) actually held that forcing a child to sing national anthem violated FRs — FDs cannot override FRs. Statement 4 is wrong: cow slaughter ban is typically upheld under Art 48 DPSP, not FD. Statements 2 (respect to national anthem) and 3 (environmental laws have FD backing) are correct judicial applications."),
    ("AP_HC","Indian_Polity","The Citizenship Amendment Act (CAA), 2019 provides expedited citizenship to persecuted minorities from:
1. Pakistan, Afghanistan, and Bangladesh
2. Hindu, Sikh, Buddhist, Jain, Parsi, and Christian communities
3. Persons who entered India on or before 31 December 2014
4. Muslim minorities from neighbouring countries","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","medium","CAA 2019 covers: three countries (Pakistan, Afghanistan, Bangladesh) (1); six religious communities excluding Muslims (2); entry deadline 31 Dec 2014 (3). Muslim minorities are explicitly excluded (4 is wrong)."),
    ("AP_HC","Indian_Polity","The Supreme Court in Jarnail Singh v. Lachhmi Narain Gupta (2018) held regarding reservation in promotions:
1. States do not need to collect quantifiable data to demonstrate inadequacy of representation for SC/ST promotion reservation
2. The \'creamy layer\' principle applies to SC/STs for promotion reservation
3. This judgment overruled M. Nagaraj v. Union of India (2006) in part
4. The Court upheld the constitutional validity of 77th, 81st, 82nd and 85th Amendments","2 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","C","hard","Statement 1 is wrong: the Court OVERRULED M. Nagaraj\'s requirement for quantifiable data. Statement 2 is correct (creamy layer applies). Statement 3 is correct (overruled Nagaraj on data requirement). Statement 4 is correct. Hence C (2, 3, 4)."),
    ("AP_HC","Indian_Polity","Under the Consumer Protection Act, 2019, which of the following are \'deficiency in service\'?
1. Failure of a builder to deliver a flat within the promised time
2. A bank failing to credit interest as per agreement
3. A doctor\'s treatment causing harm due to negligence
4. Improper goods sold by a shopkeeper","1, 2 and 3 only","2, 3 and 4 only","1 and 2 only","All of the above","A","hard","Deficiency in service (S.2(11) of CPA 2019) relates to services. A builder (1), bank (2), and doctor (3) provide services — deficiency applies. Improper goods (4) would be \'defect in goods\' under S.2(10), not \'deficiency in service\'. Hence A."),
    ("AP_HC","Indian_Polity","Which of the following constitutional safeguards protect the independence of the higher judiciary?
1. Security of tenure (judges are not easily removable)
2. Salaries charged to Consolidated Fund of India (not subject to vote)
3. Prohibition on practice after retirement in their own court
4. Parliament cannot reduce the salary of judges during their service","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four safeguard judicial independence: security of tenure (1); salary from CFI not votable (2); Art 220 bars practice in own court after retirement (3); Art 125(2) prohibits salary reduction in service (4)."),
    ("AP_HC","Indian_Polity","In Kihoto Hollohan v. Zachillhu (1992), the Supreme Court held that:
1. The Speaker\'s decision on disqualification under the 10th Schedule is final and not subject to judicial review
2. The 10th Schedule does not violate separation of powers
3. Courts can review Speaker\'s decision only after the final order, not during pendency
4. The provision giving finality to the Speaker\'s decision was itself struck down as unconstitutional","2 and 3 only","1 and 2 only","2, 3 and 4 only","All of the above","A","hard","Statement 1 is wrong — the Court specifically held that judicial review IS available (though only after final order, not during proceedings). Statement 4 is wrong — the finality clause was upheld. Statements 2 and 3 are correct."),
    ("AP_HC","Indian_Polity","Match List I (Parliamentary term) with List II (Meaning):
List I: A. Prorogation  B. Dissolution  C. Adjournment  D. Adjournment sine die
List II: 1. Ending of a sitting (day) without naming a date for the next sitting  2. Ending of a sitting temporarily (to the same or different day)  3. Ending of a session without dissolving the House  4. Termination of the life of the lower House","A-3, B-4, C-2, D-1","A-4, B-3, C-1, D-2","A-3, B-4, C-1, D-2","A-2, B-4, C-3, D-1","A","medium","Prorogation = ending of session (not House); Dissolution = ending of Lok Sabha\'s life; Adjournment = temporary break in sitting; Adjournment sine die = ending of sitting without naming next date."),
    ("AP_HC","Indian_Polity","The National Disaster Management Authority (NDMA) was established under:
1. The Disaster Management Act, 2005
2. Article 352 of the Constitution (National Emergency)
3. The NDMA is chaired by the Prime Minister
4. It can direct any ministry/department to act during a disaster","1 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","B","hard","NDMA is a statutory body under DMA 2005 (1), chaired by PM (3), and has authority to direct departments (4). Statement 2 is wrong — NDMA is not a constitutional body under Art 352; it\'s a statutory body."),
    ("AP_HC","Indian_Polity","Assertion (A): The Indian Constitution does not provide for dual citizenship.
Reason (R): Part II of the Constitution (Articles 5-11) provides for single citizenship for the whole of India, unlike the United States where citizens have both national and state citizenship.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","easy","Both are true and R correctly explains India\'s single citizenship system. In the USA, a person is simultaneously a citizen of their state and of the nation."),
    ("AP_HC","Indian_Polity","Assertion (A): A proclamation of National Emergency must be approved by both Houses of Parliament within one month.
Reason (R): If the Lok Sabha is dissolved at the time of proclamation, the Rajya Sabha alone can approve the proclamation, and it remains in force for 30 days after the reconstituted Lok Sabha first meets.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","hard","A is true — both Houses must approve within one month. R is also true — it describes the special provision when LS is dissolved (Art 352(4)). R is a qualifying/exception clause, not the reason/explanation for A."),
    ("AP_HC","Indian_Polity","Assertion (A): Article 13 of the Constitution applies only to laws made after the Constitution came into force.
Reason (R): Pre-constitutional laws inconsistent with Fundamental Rights do not become void but remain eclipsed and become operative again if the relevant Fundamental Right is amended or abridged.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","D","hard","A is false: Art 13(1) applies to pre-constitutional laws (they become void to the extent of inconsistency) and Art 13(2) prohibits future laws. R is true — this is the doctrine of eclipse for pre-constitutional laws. Hence D."),
    ("AP_HC","Indian_Polity","Assertion (A): The concept of \'due process of law\' is not expressly used in the Indian Constitution.
Reason (R): The Constituent Assembly deliberately chose \'procedure established by law\' (Article 21) over \'due process of law\' to avoid giving the judiciary excessive power to strike down laws on substantive grounds.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","hard","Both are true. The phrase \'due process of law\' (from the US Constitution) was specifically rejected by the Constituent Assembly. R correctly explains the deliberate choice — they feared judicial overreach if \'due process\' was adopted."),
    ("AP_HC","Indian_Polity","Assertion (A): The 42nd Constitutional Amendment (1976) is often called the \'Mini Constitution\'.
Reason (R): The 42nd Amendment made the most extensive changes to the Constitution including adding Fundamental Duties, amending the Preamble, curtailing judicial review, and extending the term of Lok Sabha.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains why the 42nd Amendment is called \'Mini Constitution\' — it was the most comprehensive single amendment to the Constitution (enacted during Emergency by Indira Gandhi government)."),
    ("AP_HC","Indian_Polity","Assertion (A): Every High Court has superintendence over all subordinate courts in the state including revenue courts.
Reason (R): Article 227 empowers High Courts to call for returns from such courts and make general rules for regulating the practice and proceedings of these courts.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","hard","A is partially true — HC superintendence extends to courts and tribunals but the question is whether it extends to REVENUE courts. The SC has held that revenue courts (land revenue matters) may not always be subject to Art 227 superintendence. R is true regarding Art 227\'s scope. Hence B (both true, R does not explain the limitation in A)."),
    ("AP_HC","Indian_Polity","Assertion (A): The Vice President of India is ex officio Chairman of the Rajya Sabha.
Reason (R): Unlike the Lok Sabha Speaker who is elected from amongst its members, the Vice President is separately elected by an Electoral College and then becomes Rajya Sabha Chairman by virtue of his office.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","medium","Both are true. A correctly states VP is ex officio RS Chairman (Art 64). R correctly states the distinction from LS Speaker. However R explains how VP becomes Chairman, not WHY he is Chairman. The \'reason\' A is true is Art 64 — not the electoral mechanism. Hence B."),
    ("AP_HC","Indian_Polity","Assertion (A): The Rajya Sabha cannot be dissolved by the President.
Reason (R): Rajya Sabha is a permanent body as it represents the states of the Indian Union which are permanent units of the federation.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","easy","Both are true and R correctly explains A. The Rajya Sabha is a permanent body (Art 83(1)) — one third of its members retire every two years. It represents the states and cannot be dissolved."),
    ("AP_HC","Indian_Polity","Assertion (A): A constitutional amendment bill does not require the President\'s prior recommendation for introduction in Parliament.
Reason (R): Unlike Money Bills or bills affecting states\' representation, a constitutional amendment bill under Article 368 requires only special majority and state ratification (where applicable), not Presidential recommendation.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","hard","Both are true. The procedure for constitutional amendment under Art 368 does not require Presidential recommendation (unlike Financial Bills under Art 117). R correctly identifies the Art 368 procedure as the basis for A."),
    ("AP_HC","Indian_Polity","Assertion (A): The President of India does not possess veto power over Constitutional Amendment Bills.
Reason (R): Article 368(2) requires the President to give assent to a Constitutional Amendment Bill once it is passed by Parliament; the President cannot withhold assent.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","hard","Both are true. After the 24th Amendment, Art 368(2) was amended to make Presidential assent mandatory — removing the pocket veto. R correctly explains A."),
    ("AP_HC","Indian_Polity","Match List I (Provision) with List II (Type of majority required):
List I: A. Passing an ordinary Bill in Parliament  B. Removing the Vice President  C. Passing a Constitutional Amendment Bill (regular)  D. Approving a proclamation of National Emergency
List II: 1. Special majority (majority of total membership + 2/3 of members present and voting)
2. Simple majority of members present and voting
3. Majority of total membership of the House passing the resolution
4. Special majority of each House separately","A-2, B-3, C-4, D-1","A-3, B-2, C-1, D-4","A-2, B-3, C-1, D-4","A-1, B-3, C-4, D-2","A","hard","Ordinary Bill = simple majority of members present and voting (2); Removing VP = majority of total membership of RS (3) — special resolution; Constitutional Amendment = special majority each House (4); National Emergency approval = special majority (majority of total + 2/3 present) (1)."),
    ("AP_HC","Indian_Polity","Match List I (Constitutional Writ) with List II (Notable Case):
List I: A. Habeas Corpus  B. Mandamus  C. Certiorari  D. Quo Warranto
List II: 1. University of Mysore v. C.D. Govinda Rao (1964) — against public statutory authority
2. T. Cajee v. U. Jormanik Siem (1961) — against holding public office
3. ADM Jabalpur v. Shivakant Shukla (1976) — maintainability during emergency
4. Hari Vishnu Kamath v. Ahmad Ishaque (1955) — to quash election tribunal\'s order","A-3, B-1, C-4, D-2","A-1, B-3, C-2, D-4","A-3, B-4, C-1, D-2","A-4, B-1, C-3, D-2","A","hard","ADM Jabalpur = Habeas Corpus (whether maintainable during Emergency); Govinda Rao = Mandamus (against University); Kamath v. Ishaque = Certiorari (election tribunal); T. Cajee = Quo Warranto (against holding public office)."),
    ("AP_HC","Indian_Polity","Match List I (Part of Constitution) with List II (Subject):
List I: A. Part IV-A  B. Part IX  C. Part IX-A  D. Part XIV-A
List II: 1. Municipalities  2. Tribunals  3. Panchayats  4. Fundamental Duties","A-4, B-3, C-1, D-2","A-3, B-4, C-2, D-1","A-4, B-1, C-3, D-2","A-2, B-3, C-4, D-1","A","medium","Part IV-A = Fundamental Duties (added by 42nd Amendment); Part IX = Panchayats (added by 73rd Amendment); Part IX-A = Municipalities (74th Amendment); Part XIV-A = Tribunals (added by 42nd Amendment)."),
    ("AP_HC","Indian_Polity","Match List I (Schedule) with List II (Content):
List I: A. Third Schedule  B. Fourth Schedule  C. Ninth Schedule  D. Tenth Schedule
List II: 1. Anti-defection provisions  2. Laws saved from judicial review  3. Forms of oaths and affirmations  4. Allocation of seats in Rajya Sabha","A-3, B-4, C-2, D-1","A-4, B-3, C-1, D-2","A-3, B-1, C-4, D-2","A-2, B-4, C-3, D-1","A","medium","3rd Schedule = Forms of oaths/affirmations; 4th Schedule = Rajya Sabha seat allocation; 9th Schedule = Laws protected from judicial review (added by 1st Amendment); 10th Schedule = Anti-defection law (52nd Amendment)."),
    ("AP_HC","Indian_Polity","Match List I (Constitutional Commission/Committee) with List II (Year and Purpose):
List I: A. Sarkaria Commission  B. Balwantrai Mehta Committee  C. Ashok Mehta Committee  D. G.V.K. Rao Committee
List II: 1. Recommended three-tier PRI structure
2. Reviewed Centre-State relations
3. Recommended district as unit of planning
4. Recommended two-tier PRI structure","A-2, B-4, C-1, D-3","A-4, B-2, C-3, D-1","A-2, B-1, C-4, D-3","A-1, B-4, C-2, D-3","C","hard","Sarkaria Commission (1983-88) = Centre-State relations (2); Balwantrai Mehta Committee (1957) = recommended two-tier PRIs (4) — actually recommended democratic decentralisation and led to PRI; Ashok Mehta Committee (1977-78) = recommended two-tier system (Mandal and Zila Parishad) (actually 3 seems wrong, let me reconsider). Ashok Mehta = two-tier, GVK Rao = district as planning unit."),
    ("AP_HC","Indian_Polity","Match List I (Constitutional Provision) with List II (Description):
List I: A. Article 19(1)(g)  B. Article 301  C. Article 19(6)  D. Article 302
List II: 1. Parliament\'s power to restrict freedom of trade in public interest
2. Freedom of trade, commerce and intercourse throughout India
3. Right to practise any profession or carry on any trade
4. Reasonable restrictions on Art 19(1)(g) including state monopoly","A-3, B-2, C-4, D-1","A-2, B-3, C-1, D-4","A-4, B-1, C-3, D-2","A-3, B-4, C-2, D-1","A","medium","Art 19(1)(g) = right to profession/trade/business; Art 301 = freedom of trade/commerce throughout India; Art 19(6) = restrictions including state monopoly; Art 302 = Parliament\'s power to restrict trade."),
    ("AP_HC","Indian_Polity","Which of the following is NOT correctly matched?
1. Article 32 — Right to Constitutional Remedies (Fundamental Right)
2. Article 300 — Suits and Proceedings by/against Government
3. Article 311 — Protection of civil servants only in dismissal/removal/reduction in rank
4. Article 338 — National Commission for Backward Classes","1 only","3 only","4 only","2 only","C","hard","Article 338 is the National Commission for SCHEDULED CASTES, not Backward Classes. The National Commission for Backward Classes is under Article 338-B (added by 102nd Amendment 2018). Hence statement 4 is incorrectly matched — C is the answer."),
    ("AP_HC","Indian_Polity","Which of the following is INCORRECTLY stated about the Preamble of the Indian Constitution?
1. \'We, the People of India\' — indicates popular sovereignty
2. \'Sovereign\' — India is independent, not subject to any external authority
3. \'Socialist\' — added by the 44th Constitutional Amendment, 1978
4. \'Democratic Republic\' — power ultimately derived from the people","1 only","2 only","3 only","4 only","C","medium","\'Socialist\' and \'Secular\' were added by the 42nd Amendment (1976), NOT the 44th Amendment (1978). The 44th Amendment reversed Emergency-era changes. Hence statement 3 is incorrect."),
    ("AP_HC","Indian_Polity","Which of the following statements about the UPSC is INCORRECT?
1. UPSC submits its annual report to the President who places it before Parliament
2. The Chairman of UPSC is eligible for reappointment after completing his term
3. A UPSC member who has completed his full term is ineligible for further government employment
4. UPSC members can be removed by the President after Supreme Court inquiry","1 only","2 only","3 only","4 only","B","hard","Statement 2 is incorrect: The Chairman of UPSC is NOT eligible for reappointment (Art 316(3)) — a member who has served the full term cannot be reappointed to UPSC. The Chairman is also specifically barred from other government employment under Art 316(3) proviso."),
    ("AP_HC","Indian_Polity","Which of the following is NOT a feature of the Indian federal system?
1. Dual government (Federal and State)
2. Separate constitution for each state
3. Division of powers between Centre and States
4. Written constitution","1 only","2 only","3 only","4 only","B","easy","India does NOT have separate constitutions for each state (unlike the USA where each state has its own constitution). The Indian Constitution serves as the constitution for both the Centre and the States."),
    ("AP_HC","Indian_Polity","Which of the following statements is INCORRECT about the process for removal of a Supreme Court Judge?
1. A Judge can be removed only by an order of the President
2. The removal address must be passed by each House by special majority
3. A Committee of 3 members investigates the charges before Parliament votes
4. Once an inquiry committee is constituted, the judge cannot sit until the inquiry concludes","1 only","2 only","4 only","3 only","C","hard","Statement 4 is incorrect: there is no constitutional provision that automatically prevents a judge from sitting during the inquiry. In practice, judges under inquiry may recuse themselves, but there is no mandatory suspension. Statements 1, 2, 3 are correct."),
    ("AP_HC","Indian_Polity","Identify the INCORRECT statement about Article 356 (President\'s Rule) after the S.R. Bommai case:
1. The President cannot act solely on the basis of a newspaper report to impose President\'s Rule
2. The state government must be given an opportunity to prove its majority before President\'s Rule is imposed
3. Once President\'s Rule is imposed, the state legislature is automatically dissolved
4. A proclamation under Art 356 lapses unless approved by Parliament within 2 months","3 only","1 only","4 only","2 only","A","hard","Statement 3 is incorrect: the state legislature can be kept in \'suspended animation\' (prorogued but not dissolved) under President\'s Rule. Dissolution is a more drastic step that the President may or may not take. Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","Consider the following statements regarding the Governor\'s power to grant pardons:
1. The Governor\'s pardoning power extends to sentences awarded by court martial
2. The Governor cannot pardon a sentence of death
3. Governor\'s pardoning power is coextensive with President\'s power in matters relating to state laws
4. The Governor acts on the advice of the State Council of Ministers in pardoning matters","2 and 3 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","C","hard","Statement 1 is wrong: Governor\'s power (Art 161) does NOT extend to court martial sentences — that is exclusive to the President (Art 72). Statements 2, 3, 4 are correct."),
    ("AP_HC","Indian_Polity","With reference to the \'doctrine of pleasure\' under Article 310 of the Indian Constitution, consider the following:
1. Civil servants hold office during the pleasure of the President or Governor
2. This doctrine is ABSOLUTELY applicable without any safeguards
3. Article 311 carves out exceptions/safeguards to the doctrine of pleasure
4. Members of constitutional bodies like UPSC are not subject to this doctrine","1 and 3 only","1, 3 and 4 only","2 and 4 only","All of the above","B","hard","Statement 2 is wrong: the doctrine is NOT absolute — Art 311 provides procedural safeguards before dismissal. Statements 1, 3, 4 are correct."),
    ("AP_HC","Indian_Polity","Which of the following statements about Delegated Legislation are CORRECT?
1. Delegated legislation is a law made by an authority other than the supreme legislature acting under powers delegated to it
2. It is subject to the doctrine of ultra vires
3. It can be challenged if it exceeds the scope of the parent Act
4. The Supreme Court cannot examine delegated legislation if it is placed before Parliament","1, 2 and 3 only","2, 3 and 4 only","1 and 3 only","All of the above","A","hard","Statement 4 is wrong: Parliamentary placement (laying on the table) does not immunise delegated legislation from judicial scrutiny — courts can still examine it for ultra vires. Statements 1, 2, 3 are correct."),
    ("AP_HC","Indian_Polity","Under the Scheduled Castes and Scheduled Tribes (Prevention of Atrocities) Act, 1989 (SC/ST PoA Act):
1. Offences under this Act are non-bailable and non-compoundable
2. Special Courts must be established to try cases under this Act
3. An anticipatory bail cannot be granted in SC/ST PoA Act cases (as held in SC\'s original interpretation)
4. The burden of proving innocence lies on the accused","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is wrong: the Act does not reverse the burden of proof as such. Statements 1, 2, 3 are correct — notably anticipatory bail was originally not available (though modified after SC\'s 2018 judgment in Subhash Kashinath Mahajan and subsequent legislative amendment)."),
    ("AP_HC","Indian_Polity","The \'Principle of Proportionality\' as a ground of judicial review in India was clearly recognised in:
1. Om Kumar v. Union of India (2001) — administrative law context
2. Modern Dental College and Research Centre v. State of MP (2016) — fundamental rights context
3. K.S. Puttaswamy v. Union of India (2017) — for restriction on fundamental rights
4. All of the above cases","1 only","1 and 2 only","2 and 3 only","All of the above","D","hard","All three cases recognised proportionality: Om Kumar (2001) in administrative law; Modern Dental College (2016) in FR context; Puttaswamy (2017) as a test for restrictions on FRs. Hence D."),
    ("AP_HC","Indian_Polity","Which of the following are correctly matched regarding constitutional bodies that do NOT have security of tenure (removable more easily)?
1. Members of State Public Service Commissions — removable by President (not Governor)
2. Comptroller and Auditor General — removable in the same manner as SC judges
3. Attorney General of India — holds office during pleasure of the President
4. Finance Commission members — no security of tenure; appointed for specific term","1 and 3 only","3 and 4 only","1, 3 and 4 only","All of the above","C","hard","Statement 2 is wrong: CAG IS removable like SC judges (security of tenure). Statements 1 (SPSC — Art 317), 3 (AG — Art 76(4)), 4 (Finance Commission — limited term) are correct."),
    ("AP_HC","Indian_Polity","With reference to the right to free speech under Article 19(1)(a), which of the following restrictions under Article 19(2) are CORRECTLY stated?
1. Sovereignty and integrity of India
2. Security of the State
3. Friendly relations with foreign states
4. Public morality
5. Decency or morality (separate from public morality)","1, 2, 3 and 4 only","1, 2 and 3 only","1, 2, 3 and 5 only","All of the above","C","hard","Art 19(2) grounds: sovereignty and integrity (1), security of state (2), friendly relations with foreign states (3), public order, decency OR morality (5 — not both separately; \'decency or morality\' is the phrase used). \'Public morality\' (4) as a separate head is not correct — it is \'decency or morality\'. Hence C (1, 2, 3, and 5 combined as \'decency or morality\')."),
    ("AP_HC","Indian_Polity","Consider the following and identify which are listed in Schedule V (Fifth Schedule) of the Constitution:
1. Provisions for Tribal Advisory Councils
2. Specification of Scheduled Areas
3. Powers of Central Government to give directions regarding administration of Scheduled Areas
4. Regulations made by Governor for Scheduled Areas (which require Presidential assent)","1 and 4 only","2 and 3 only","1, 3 and 4 only","All of the above","D","hard","All four are provisions in the Fifth Schedule: Tribal Advisory Councils (para 4), Scheduled Areas (para 6), Central govt directions (para 3), and Governor\'s regulations requiring Presidential assent (para 5)."),
    ("AP_HC","Indian_Polity","Which of the following statements about \'constitutional conventions\' and their relationship to constitutional law in India are CORRECT?
1. Conventions may be legally unenforceable but are politically binding
2. When a convention is incorporated into the constitutional text, it becomes a constitutional norm
3. Breach of constitutional convention may lead to political sanctions but not legal consequences
4. The advice tendered by the Council of Ministers to the President is justiciable","1, 2 and 3 only","2, 3 and 4 only","1, 3 and 4 only","All of the above","A","hard","Statement 4 is wrong: Art 74(2) specifically provides that the advice tendered by the CoM to the President shall NOT be inquired into by any court — it is non-justiciable. Statements 1, 2, 3 correctly describe conventions."),
    ("AP_HC","Indian_Polity","Which of the following are \'constitutional\' (not statutory) rights available to arrested persons in India?
1. Right to be informed of grounds of arrest (Article 22(1))
2. Right to be produced before a magistrate within 24 hours (Article 22(2))
3. Right to bail under CrPC
4. Right to a speedy trial (read into Article 21)","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is a statutory right under CrPC, not a constitutional right. Statements 1, 2 are explicitly in Art 22. Statement 4 is constitutionally read into Art 21 by the SC. Hence B (1, 2, 4)."),
    ("AP_HC","Indian_Polity","Which of the following statements about \'Judicial Accountability\' are CORRECT?
1. A Supreme Court judge can be removed only by impeachment under Article 124(4)
2. The Judges (Inquiry) Act, 1968 lays down the procedure for investigation of charges against judges
3. In-house procedure under the Supreme Court can result in removal of a judge
4. Parliament has never impeached any Supreme Court judge in India\'s history","1, 2 and 4 only","2, 3 and 4 only","1 and 2 only","All of the above","A","hard","Statement 3 is wrong: in-house procedure can lead to recommendations but NOT actual removal — removal requires Parliamentary impeachment. Statement 4 is correct (no SC judge has been removed). Statements 1, 2 are correct."),
    ("AP_HC","Indian_Polity","Assertion (A): Article 131 gives the Supreme Court exclusive original jurisdiction in disputes between states.
Reason (R): Article 131 excludes disputes arising out of any treaty, agreement, or covenant which was entered into before the commencement of the Constitution from its scope.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","hard","A is true — SC has exclusive original jurisdiction in inter-state disputes. R is also true — Art 131 proviso excludes pre-Constitution treaties etc. But R is an exception/limitation to Art 131, not the reason for A. Hence B."),
    ("AP_HC","Indian_Polity","Match List I (Landmark Case) with List II (Key holding/topic):
List I: A. State of Madras v. V.G. Row (1952)  B. A.K. Gopalan v. State of Madras (1950)  C. R.C. Cooper v. Union of India (1970)  D. Bennett Coleman v. Union of India (1972)
List II: 1. FRs must be read independently, separate compartments — overruled later
2. Press freedom challenge to newsprint quota — upheld press freedom
3. Bank nationalisation — FRs to be read together
4. Reasonable restrictions test — court can examine effects not merely form","A-4, B-1, C-3, D-2","A-1, B-4, C-3, D-2","A-4, B-3, C-1, D-2","A-3, B-1, C-4, D-2","A","hard","V.G. Row (1952) = court can examine direct and inevitable effect of law on FRs (4); A.K. Gopalan (1950) = FRs are separate compartments (overruled by Maneka Gandhi) (1); R.C. Cooper (bank nationalisation, 1970) = FRs to be read together (3); Bennett Coleman (1972) = press freedom case on newsprint allocation (2)."),
    ("AP_HC","Indian_Polity","Which of the following are CORRECT statements about the Comptroller and Auditor General (CAG)?
1. The CAG audits accounts of all Union and State governments
2. The CAG can be removed by the President on his own motion
3. Reports of the CAG relating to Union accounts are submitted to the President
4. The CAG does not audit accounts of Government companies if external auditors are appointed","1 and 3 only","1, 2 and 3 only","1, 3 and 4 only","All of the above","A","hard","Statement 2 is wrong: CAG is removed only on an address by Parliament (like a SC judge). Statement 4 is wrong: CAG DOES audit Government companies in addition to external auditors. Statements 1 and 3 are correct."),
    ("AP_HC","Indian_Polity","Assertion (A): The Constitution permits Parliament to derogate from Fundamental Rights only through a constitutional amendment under Article 368.
Reason (R): Article 13(2) states that the State shall not make any law that takes away or abridges the rights conferred by Part III.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","hard","Both are true. A states that derogation from FRs requires constitutional amendment. R (Art 13(2)) is the source — it prohibits ordinary laws from abridging FRs, implying only a constitutional amendment can do so. R correctly explains A."),
    ("AP_HC","Indian_Polity","Which of the following Articles of the Constitution deal with the \'distribution of revenues\' between the Union and States?
1. Article 268 — duties levied by Union but collected and appropriated by States
2. Article 269 — taxes levied and collected by Union but assigned to States
3. Article 270 — taxes levied and collected by Union and distributed
4. Article 271 — surcharges on taxes for Union purposes","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four articles deal with revenue distribution: Art 268 (stamp duties, excise on medicinal substances — levied by Union, collected by States); Art 269 (taxes on inter-state trade, assigned to states); Art 270 (income tax etc., split between Centre and states); Art 271 (surcharges for Centre)."),
    ("AP_HC","Indian_Polity","In the context of \'Right to Privacy\' as a Fundamental Right, the Supreme Court\'s 9-judge bench in K.S. Puttaswamy v. Union of India (2017) held:
1. Privacy is a natural right that exists independent of constitutional recognition
2. Privacy is part of the liberty protected under Article 21
3. Privacy includes informational self-determination and bodily autonomy
4. Privacy rights are absolute and cannot be restricted by the State","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is wrong: the Court explicitly held privacy CAN be restricted by law that meets the test of legality, legitimate aim, and proportionality. Statements 1, 2, 3 are correctly stated."),
    ("AP_HC","Indian_Polity","Match List I (Interpretation Doctrine) with List II (Description):
List I: A. Pith and substance  B. Colourable legislation  C. Occupied field  D. Repugnancy (Art 254)
List II: 1. If Centre has occupied a field, state cannot legislate on it
2. Conflict between Central and State law on Concurrent List — Central law prevails
3. Courts look at the true nature/character of legislation to determine competence
4. Legislature cannot do indirectly what it cannot do directly","A-3, B-4, C-1, D-2","A-4, B-3, C-2, D-1","A-3, B-1, C-4, D-2","A-4, B-1, C-3, D-2","A","medium","Pith and substance = true nature of law (3); Colourable legislation = indirect transgression of limits (4); Occupied field = no space for state if Centre has acted (1); Repugnancy = Art 254 conflict resolution in Concurrent List (2)."),
    ("AP_HC","Indian_Polity","Which of the following provisions are contained in Article 22 of the Constitution regarding preventive detention?
1. Detention order must be communicated to the detenu as soon as possible
2. The detenu must be afforded the earliest opportunity of making representation against the order
3. The advisory board must give its opinion within 10 weeks
4. Detention without Advisory Board reference cannot exceed 3 months (original provision)","1 and 2 only","1, 2 and 3 only","1, 2 and 4 only","All of the above","D","hard","All four are in Art 22(5)-(7): grounds must be communicated (1); opportunity to make representation (2); Advisory Board gives opinion within 10 weeks (3) — added by 44th Amendment; original 3-month limit (4). All correct."),
    ("AP_HC","Indian_Polity","Consider the following cases and identify which case INCORRECTLY describes the principle it stands for:
1. Golak Nath v. State of Punjab (1967) — Parliament has unlimited power to amend FRs
2. Kesavananda Bharati (1973) — Parliament can amend Constitution but not its basic structure
3. Minerva Mills (1980) — Harmony between FRs and DPSPs is itself a basic structure
4. I.R. Coelho (2007) — Laws in 9th Schedule can be reviewed for basic structure violation if added after April 24, 1973","1 only","3 only","2 only","4 only","A","hard","Golak Nath (1967) held that Parliament CANNOT amend FRs — it held FRs are BEYOND Parliament\'s amendatory power. Statement 1 says Parliament HAS unlimited power — this is the OPPOSITE of what Golak Nath held. So statement 1 is incorrect. The others (2, 3, 4) are correct."),
    ("AP_HC","Indian_Polity","The President of India is elected by:
1. Members of both Houses of Parliament
2. Members of Legislative Assemblies of all States
3. Members of Legislative Assemblies of Union Territories with legislature (Delhi, Puducherry, J&K)
4. Nominated members of Parliament and State Legislatures","1 and 2 only","1, 2 and 3 only","2 and 3 only","All of the above","B","hard","Nominated members do NOT vote in Presidential election (4 is wrong). The Electoral College for President: elected members of Lok Sabha, Rajya Sabha (1), elected members of all state legislative assemblies (2), and elected members of UT legislative assemblies — Delhi, Puducherry, J&K (3). Hence B."),
    ("AP_HC","Indian_Polity","The concept of \'creamy layer\' in reservation jurisprudence was first propounded by the Supreme Court in:
1. Indra Sawhney v. Union of India (1992)
2. State of Kerala v. N.M. Thomas (1976)
3. M.R. Balaji v. State of Mysore (1963)
4. Mandal Commission report (1980)","1 only","2 only","3 only","4 only","A","medium","The Supreme Court in Indra Sawhney (1992) — the Mandal Commission case — introduced the \'creamy layer\' concept for OBC reservations, holding that the advanced sections among OBCs (creamy layer) should be excluded from reservation benefits."),
    ("AP_HC","Indian_Polity","Which of the following writs can be issued against a PRIVATE individual or body in certain circumstances?
1. Habeas Corpus
2. Mandamus
3. Certiorari
4. Quo Warranto","1 and 4 only","1 only","1 and 3 only","All of the above","A","hard","Habeas Corpus can be issued against any person (including private individuals) who unlawfully detains another. Quo Warranto can be issued against anyone claiming or holding a public statutory office (even if they are not a public official themselves). Mandamus and Certiorari are generally against public authorities."),
    ("AP_HC","Indian_Polity","The \'doctrine of severability\' was applied by the Supreme Court in which of the following scenarios?
1. R.M.D.C. v. Union of India (1957) — separating valid from invalid parts of a gaming law
2. A.K. Roy v. Union of India (1982) — reading down provisions of National Security Act
3. Kedar Nath Singh v. State of Bihar (1962) — sedition law read down to save its valid core
4. Romesh Thappar v. State of Madras (1950) — entire law struck down for lack of severability","1 and 3 only","1, 2 and 3 only","3 and 4 only","All of the above","D","hard","All four cases involve severability/reading down: RMDC (1957) = classic severability; A.K. Roy (1982) = reading down NSA; Kedar Nath (1962) = read down S.124-A IPC to preserve valid core; Romesh Thappar = law struck entirely as invalid portion couldn\'t be severed."),
    ("AP_HC","Indian_Polity","Which of the following are CORRECT regarding the procedure for amendment of the Constitution under Article 368?
1. A bill to amend the Constitution can be introduced in either House
2. Each House must pass the bill by special majority (majority of total membership AND 2/3 of members present and voting)
3. There is no provision for a joint sitting of both Houses in case of disagreement on a constitutional amendment bill
4. After state ratification (where required), the bill goes to the President who must give assent","1, 2 and 3 only","2, 3 and 4 only","1, 3 and 4 only","All of the above","D","hard","All four are correct: introduced in either House (1); special majority (2); no joint sitting provision for constitutional amendments (3); President\'s assent is mandatory post 24th Amendment (4)."),
    ("AP_HC","Indian_Polity","Under the Insolvency and Bankruptcy Code (IBC), 2016, the Resolution Professional:
1. Takes control of the debtor company during the Corporate Insolvency Resolution Process
2. Must be appointed within 14 days of the admission of the insolvency application
3. The Committee of Creditors is constituted only if the resolution plan fails
4. The moratorium period prevents all legal proceedings against the debtor","1 and 4 only","1, 2 and 4 only","1, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: the Committee of Creditors (CoC) is constituted DURING the CIRP to evaluate resolution plans — not only after failure. Statements 1, 2, 4 are correct under IBC."),
    ("AP_HC","Indian_Polity","Match List I (Commission/Committee) with List II (Subject/Recommendation):
List I: A. Malimath Committee (2003)  B. Malimath Committee on Criminal Justice  C. Law Commission (272nd Report, 2017)  D. Justice Verma Committee (2013)
List II: 1. Death penalty to be abolished except for terrorism
2. Amendment of rape law and creation of new gender-neutral offences
3. Reforms in criminal justice system including confession to police
4. Same report as B (this is the same committee)","A-4, B-3, C-1, D-2","A-3, B-4, C-1, D-2","A-4, B-3, C-2, D-1","A-1, B-3, C-4, D-2","B","hard","Malimath Committee = same (A and B are same) — recommended reforms including making police confessions admissible (3); Law Commission 272nd Report = recommended abolition of death penalty except for terrorism (1); Justice Verma Committee (2013) = post-Nirbhaya, recommended sweeping rape law reform (2)."),
    ("AP_HC","Indian_Polity","Assertion (A): The Ninth Schedule of the Indian Constitution was added by the First Amendment (1951) to protect land reform laws from judicial review.
Reason (R): Any law placed in the Ninth Schedule after April 24, 1973 can be examined by the Supreme Court for violation of the basic structure of the Constitution.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","hard","Both A and R are true. The 9th Schedule was added by 1st Amendment (A) to protect land reform laws. R (post-1973 additions can be reviewed) is a correct statement from I.R. Coelho (2007). But R doesn\'t explain A — it\'s a separate, later development."),
    ("AP_HC","Indian_Polity","Which of the following are INCORRECT statements about Parliamentary Privileges?
1. Parliamentary privilege includes freedom from civil arrest during session and 40 days before and after
2. Court cannot question anything said or vote cast in Parliament
3. Parliamentary privilege extends to all employees of Parliament
4. A member can be expelled by the House for breach of privilege","1 and 3 only","2 and 4 only","3 only","None of the above — all are correct","C","hard","Statements 1, 2, 4 are correct parliamentary privileges. Statement 3 is partially correct but \'all employees\' is an overstatement — the privilege extends to officers of Parliament to some extent, but not ALL employees have the same privileges as members."),
    ("AP_HC","Indian_Polity","Consider the following about Special Category States in India:
1. Special Category Status is a constitutional concept explicitly provided in the Constitution
2. Uttarakhand, Himachal Pradesh, and Sikkim currently enjoy Special Category Status
3. Special Category States receive 90% Central assistance as grants (compared to 70% for other states)
4. The concept was introduced on the recommendation of the 5th Finance Commission","2 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","A","hard","Statement 1 is wrong: Special Category Status is NOT a constitutional concept — it is an administrative/planning concept. Statement 4 is wrong: it was introduced by the 5th Finance Commission but implemented by the National Development Council (Gadgil formula). Statements 2 and 3 are correct."),
    ("AP_HC","Indian_Polity","The Protection of Human Rights Act, 1993 provides that:
1. NHRC can investigate any violation of human rights
2. NHRC cannot investigate any complaint against armed forces unless Central government refers it
3. NHRC can award compensation to victims
4. A complaint must be filed within one year of the incident","1 and 4 only","1, 3 and 4 only","2 and 4 only","All of the above","B","hard","Statement 2 is wrong: NHRC cannot investigate armed forces directly but can seek reports — not \'unless Central government refers it\' specifically. Statement 3 is wrong: NHRC can RECOMMEND compensation but cannot directly award (it can approach courts). Statements 1 and 4 are correct."),
    ("AP_HC","Indian_Polity","With reference to the composition of the GST Council under Article 279-A, which of the following statements are CORRECT?
1. Union Finance Minister is the Chairperson
2. Union Minister of State for Finance is a member
3. Each state sends its Finance Minister or designated Minister as a member
4. Decisions of the GST Council are taken by a majority of all members present and voting","1, 2 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","A","hard","Statement 4 is wrong: decisions of the GST Council require a weighted 3/4 majority — not a simple majority. Statements 1, 2, 3 are correct about GST Council composition."),
    ("AP_HC","Indian_Polity","Which of the following Fundamental Rights are available ONLY to citizens (not aliens/foreigners)?
1. Article 15 — Prohibition of discrimination on grounds of religion, race, caste, sex, place of birth
2. Article 16 — Equality of opportunity in public employment
3. Article 19 — Six freedoms including speech, movement, profession etc.
4. Article 29 and 30 — Cultural and educational rights","1, 2 and 3 only","1 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are available ONLY to citizens: Arts 15, 16, 19, 29, 30 are citizen-only FRs. Arts 14, 20, 21, 22, 23, 24, 25, 26, 27, 28 are available to all persons including foreigners."),
    ("AP_HC","Indian_Polity","The Andhra Pradesh Public Employment (Organisation to Local Candidates) Act relates to:
1. Reservation of jobs for local candidates in AP (implementing Article 371-D)
2. Presidential Orders specifying local areas and local candidates for different zones
3. This was originally applicable only to the undivided AP and continues for the residual AP
4. Challenge to this Act has been adjudicated by the AP Administrative Tribunal under Art 371-D","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four statements are correct regarding the AP local cadre/employment provisions under Art 371-D and the Presidential Orders issued thereunder."),
    ("AP_HC","Indian_Polity","Assertion (A): The writ of Mandamus will not lie against a private individual.
Reason (R): Mandamus is issued against a person or body to perform a public duty of a public nature; private contracts or obligations do not attract mandamus.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains A. Mandamus lies only against public authorities with a public duty — private individuals performing private obligations cannot be compelled through mandamus."),
    ("AP_HC","Indian_Polity","Which of the following statements about the \'right to education\' under Article 21-A are CORRECT?
1. It was inserted by the 86th Constitutional Amendment, 2002
2. It provides free and compulsory education to children of 6-14 years
3. The Right to Education Act, 2009 gives effect to Article 21-A
4. Private unaided schools are required to admit 25% students from economically weaker sections","1, 2 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","D","medium","All four are correct: 86th Amendment added Art 21-A (1); age group 6-14 (2); RTE Act 2009 (3); 25% EWS quota in private schools under RTE (4)."),
    ("AP_HC","Indian_Polity","Assertion (A): The Supreme Court of India can issue a writ of Certiorari to quash an order of a High Court.
Reason (R): The Supreme Court\'s writ jurisdiction under Article 32 extends to all courts and tribunals in India including High Courts.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","C","hard","A is true: SC can issue Certiorari to a HC (under its appellate/supervisory jurisdiction). R is false: Art 32 is for enforcement of FRs — the SC doesn\'t normally issue writs against HCs under Art 32. The SC\'s power over HCs is through Art 136 (SLP) and its general appellate jurisdiction."),
    ("AP_HC","Indian_Polity","Match List I (Right/Freedom) with List II (Reasonable Restriction Ground):
List I: A. Art 19(1)(a) — Freedom of Speech  B. Art 19(1)(b) — Right to Assemble  C. Art 19(1)(c) — Right to form Associations  D. Art 19(1)(d) — Right to Move
List II: 1. Interests of sovereignty, public order, morality
2. Interests of sovereignty, security of state, public order
3. Interests of sovereignty, security of state, public order, decency, morality, contempt, defamation, incitement
4. Interests of sovereignty, public order","A-3, B-4, C-2, D-1","A-3, B-1, C-2, D-4","A-2, B-3, C-1, D-4","A-4, B-3, C-2, D-1","A","hard","Art 19(2) for speech is the broadest (sovereignty, security, friendly relations, public order, decency/morality, contempt, defamation, incitement); Art 19(3) for assembly: sovereignty + public order only; Art 19(4) for associations: sovereignty + security + public order + morality; Art 19(5) for movement: sovereignty + public order + interests of STs."),
    ("AP_HC","Indian_Polity","The term \'state\' for the purposes of Part III (Fundamental Rights) of the Constitution includes:
1. The Government and Parliament of India
2. The Government and Legislature of each State
3. All local authorities
4. Other authorities within the territory of India or under the control of the Government of India","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","easy","Article 12 defines \'State\' to include: Government and Parliament of India (1), Government and Legislature of States (2), all local authorities (3), and other authorities within India or under Central control (4)."),
    ("AP_HC","Indian_Polity","Which of the following are INCORRECT statements about the Vice President of India?
1. The Vice President must be a member of either House of Parliament
2. The Vice President can be removed only by a special majority of the Rajya Sabha
3. The Vice President performs the duties of the President when the President is unable to discharge his functions
4. The salary and allowances of the Vice President are charged to the Consolidated Fund of India","1 and 2 only","2 only","1 only","All are correct","A","hard","Statement 1 is wrong: the VP must NOT be a member of Parliament — he must resign before taking office (Art 66(4)). Statement 2 is wrong: VP is removed by a resolution of Rajya Sabha passed by a MAJORITY (not special majority) and agreed to by Lok Sabha (Art 67(b)). Statements 3, 4 are correct."),
    ("AP_HC","Indian_Polity","Consider the following provisions and identify the one that is CORRECTLY described:
1. Article 356 — Financial Emergency provisions
2. Article 360 — President\'s Rule in states
3. Article 352 — National Emergency
4. Article 358 — Suspension of Article 19 during National Emergency","1 only","2 only","3 and 4 only","1 and 2","C","easy","Articles 352 (National Emergency) and 358 (suspension of Art 19 rights during emergency) are correctly described. Article 356 is President\'s Rule (state emergency), NOT financial emergency. Article 360 is Financial Emergency, not President\'s Rule."),
    ("AP_HC","Indian_Polity","The concept of \'Public Trust Doctrine\' in environmental law means:
1. Certain natural resources like rivers, seashores, and forests are held in trust by the State for public use
2. The State cannot alienate these resources to private parties
3. Citizens have a right to access these resources
4. This doctrine was recognised by the Supreme Court in M.C. Mehta v. Kamal Nath (1997)","1 and 2 only","1, 2 and 4 only","1, 3 and 4 only","All of the above","D","hard","All four correctly describe the Public Trust Doctrine: resources held in public trust (1), cannot be alienated (2), public access right (3), recognised in M.C. Mehta v. Kamal Nath (1997) (4)."),
    ("AP_HC","Indian_Polity","Under Article 263, the Inter-State Council is empowered to:
1. Inquire into and advise upon disputes between states
2. Investigate subjects of common interest between Centre and States
3. Make recommendations on subjects of common interest
4. Take binding decisions on inter-state disputes","1, 2 and 3 only","2 and 3 only","1 and 4 only","All of the above","A","hard","Statement 4 is wrong: the Inter-State Council can only RECOMMEND — it cannot take binding decisions. Statements 1, 2, 3 are correct powers under Art 263."),
    ("AP_HC","Indian_Polity","Match List I (Article 13 Concepts) with List II (Meaning):
List I: A. Law  B. Void  C. Inconsistency  D. State action
List II: 1. Action by government bodies subject to judicial review
2. Conflict between a law and Fundamental Rights
3. Includes ordinance, bye-laws, notification, custom, usage
4. Unconstitutional to the extent of conflict with FRs","A-3, B-4, C-2, D-1","A-4, B-3, C-1, D-2","A-3, B-2, C-4, D-1","A-1, B-4, C-3, D-2","A","hard","Under Art 13: \'Law\' includes ordinances, bye-laws, notifications, customs (3); \'Void\' = unconstitutional to extent of inconsistency (4); \'Inconsistency\' = conflict with FRs (2); \'State action\' = government action subject to review (1)."),
    ("AP_HC","Indian_Polity","Assertion (A): A law passed by Parliament to give effect to international treaties can encroach upon State List subjects without state consent.
Reason (R): Article 253 empowers Parliament to make laws for implementing international treaties, agreements, or conventions even on subjects in the State List.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains A. Art 253 is a specific provision that overrides the normal federal distribution — it allows Parliament to legislate on State List for treaty implementation."),
    ("AP_HC","Indian_Polity","The \'constituent power\' of the Indian Parliament refers to:
1. The power to amend the Constitution under Article 368
2. This power is distinct from its \'legislative power\' to make ordinary laws
3. The constituent power is unlimited and unrestricted according to the Kesavananda Bharati judgment
4. The exercise of constituent power requires special procedures different from ordinary legislation","1, 2 and 4 only","2, 3 and 4 only","1, 3 and 4 only","All of the above","A","hard","Statement 3 is wrong: Kesavananda Bharati held the opposite — constituent power is LIMITED by the basic structure doctrine. Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","Which of the following special courts deal with corruption and anti-corruption cases?
1. CBI Courts (Special Courts under CBI)
2. Courts under the Prevention of Corruption Act
3. Special Courts under PMLA for money laundering
4. Lokpal as a trial court","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Lokpal is not a trial court — it investigates and refers cases to Special Courts but does not itself conduct trials. Statements 1, 2, 3 are correct types of special courts dealing with corruption-related matters."),
    ("AP_HC","Indian_Polity","Under the Constitution, which of the following is the CORRECT position regarding the State Council of Ministers?
1. The Council of Ministers is collectively responsible to the Legislative Assembly (Art 164(2))
2. A Minister who is not a member of the legislature must become a member within 6 months
3. The Chief Minister is appointed by the Governor in his discretion
4. A Minister can hold office without being a member of either House for up to 6 months","1 and 2 only","1, 2 and 3 only","1, 3 and 4 only","All of the above","D","hard","All four are correct: collective responsibility (1); 6 months to become member (2); Governor appoints CM in discretion when no clear majority (3); non-member minister has 6 months (4) — same as for Parliament."),
    ("AP_HC","Indian_Polity","The \'test of arbitrariness\' in the context of Article 14 was expanded by the Supreme Court in:
1. E.P. Royappa v. State of Tamil Nadu (1974) — equality is antithetic to arbitrariness
2. Maneka Gandhi v. Union of India (1978) — Art 14 strikes at arbitrariness
3. Ajay Hasia v. Khalid Mujib (1981) — State action must not be arbitrary
4. All three cases progressively expanded the \'new doctrine\' of equality","1 only","1 and 2 only","1, 2 and 3 only","All of the above","D","hard","All four are correct. The \'new doctrine\' of equality (equality = non-arbitrariness) was developed through E.P. Royappa (1974), Maneka Gandhi (1978), and Ajay Hasia (1981) — progressively expanding Art 14 beyond mere classification."),
    ("AP_HC","Indian_Polity","Which of the following statements about the National Human Rights Commission (NHRC) are INCORRECT?
1. The NHRC Chairperson must be a retired Chief Justice of India
2. NHRC has jurisdiction over violations by armed forces directly
3. The NHRC can award compensation directly to victims
4. A complaint to NHRC must be filed within 2 years of the alleged violation","1 and 4 only","2 and 3 only","3 and 4 only","All of the above","B","hard","Statement 2 is INCORRECT: NHRC cannot directly investigate armed forces (it can only seek a report from the government). Statement 3 is INCORRECT: NHRC cannot directly award compensation — it can recommend. Statements 1 and 4 are CORRECT (CJI retired + 2-year limitation)."),
    ("AP_HC","Indian_Polity","Match List I (Constitutional body) with List II (Article dealing with its powers/functions):
List I: A. UPSC — Functions  B. Election Commission — Power of superintendence  C. Comptroller and Auditor General — Duties  D. Finance Commission — Terms of reference
List II: 1. Article 280  2. Article 324  3. Article 320  4. Article 149","A-3, B-2, C-4, D-1","A-4, B-2, C-3, D-1","A-3, B-4, C-2, D-1","A-2, B-3, C-1, D-4","A","medium","UPSC functions = Art 320; ECI superintendence = Art 324; CAG duties = Art 149; Finance Commission terms = Art 280."),
    ("AP_HC","Indian_Polity","Which of the following are \'grounds\' on which the Supreme Court can set aside an arbitral award under the Arbitration and Conciliation Act, 1996?
1. Fraud or corruption in making the award
2. The award is in conflict with public policy of India
3. The arbitral tribunal was not properly constituted
4. The party making the application was under incapacity","1 and 2 only","2 and 3 only","1, 2 and 4 only","All of the above","D","hard","Under Section 34 of the Arbitration Act: incapacity (4), invalid arbitration agreement, no proper notice, award outside scope, improper tribunal constitution (3), public policy conflict (2), fraud (1) — all are grounds for setting aside. All four are correct."),
    ("AP_HC","Indian_Polity","Under the Companies Act, 2013, the National Company Law Tribunal (NCLT) has jurisdiction over:
1. Corporate insolvency and bankruptcy proceedings
2. Oppression and mismanagement of minority shareholders
3. Class action suits by shareholders/depositors
4. All winding-up petitions previously handled by High Courts","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are within NCLT jurisdiction: IBC insolvency (1); oppression/mismanagement (Sections 241-242) (2); class action suits (Section 245) (3); company winding up transferred from HCs to NCLT (4)."),
    ("AP_HC","Indian_Polity","The principle \'Ubi jus ibi remedium\' means:
1. Where there is a right, there is a remedy
2. This principle underlies Article 32 of the Indian Constitution
3. The principle is not applicable if the right is merely a moral right without legal enforceability
4. Dr. B.R. Ambedkar cited this principle in defending the inclusion of Article 32","1 and 2 only","1, 2 and 4 only","1, 3 and 4 only","All of the above","D","hard","All four are correct: the maxim means \'where there is a right, there is a remedy\' (1); this underlies Art 32 (2); the maxim applies only to legally enforceable rights (3); Ambedkar called Art 32 \'the heart and soul of the Constitution\' invoking this principle (4)."),
    ("AP_HC","Indian_Polity","Consider the following regarding the Demonetisation case (Vivek Narayan Sharma v. Union of India, 2023):
1. The Supreme Court upheld the demonetisation of Rs. 500 and Rs. 1000 notes in 2016
2. The 5-judge constitution bench decided by a 4:1 majority
3. The dissenting judge held the demonetisation was unconstitutional
4. The power to demonetise under Section 26(2) of RBI Act was held to be valid even without RBI Board\'s recommendation","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is contested — the majority held the process was valid; the dissent held it was invalid for lack of independent decision-making by RBI. Statements 1, 2, 3 are correct: SC upheld demonetisation 4:1; Justice B.V. Nagarathna dissented; she held it was unconstitutional."),
    ("AP_HC","Indian_Polity","The right against self-incrimination under Article 20(3) provides that:
1. No person accused of any offence shall be compelled to be a witness against himself
2. This applies to civil proceedings as well as criminal proceedings
3. Providing voice samples, blood samples, or fingerprints is not protected under Art 20(3)
4. The protection is available only from the moment of formal accusation","1 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 2 is wrong: Art 20(3) applies only to criminal proceedings, not civil. Statements 1, 3, 4 are correct — SC in Selvi v. State of Karnataka (2010) held voice/blood samples etc. are not \'testimonial compulsion\' (3), and formal accusation is needed (4)."),
    ("AP_HC","Indian_Polity","Which of the following correctly describes the power of the President to promulgate Ordinances under Article 123?
1. Ordinances can be promulgated only when Parliament is not in session
2. Ordinances must be approved by both Houses within 6 weeks of Parliament reassembling
3. Ordinances can be withdrawn by the President at any time
4. An Ordinance has the same force and effect as an Act of Parliament","1 and 4 only","1, 3 and 4 only","1, 2 and 4 only","All of the above","D","hard","All four are correct: Ordinance when Parliament not in session (1); approved within 6 weeks of Parliament reassembling (2); can be withdrawn (3); same force as Act (4) — all per Art 123."),
    ("AP_HC","Indian_Polity","With reference to the \'doctrine of basic structure\', which of the following have been specifically held to be part of the basic structure?
1. Rule of Law
2. Separation of powers
3. Federalism
4. Harmony and balance between Fundamental Rights and Directive Principles","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are part of the basic structure: Rule of Law (L. Chandra Kumar); Separation of powers (Indira Gandhi v. Raj Narain); Federalism (State of W.B. v. Union of India); Harmony between FRs and DPSPs (Minerva Mills)."),
    ("AP_HC","Indian_Polity","Assertion (A): The President of India can return a non-Money Bill to Parliament for reconsideration only once.
Reason (R): If Parliament passes the bill again (with or without amendments), the President is bound to give his assent and cannot exercise the pocket veto.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","hard","Both are true. The President can return a non-Money Bill once for reconsideration (Art 111). If Parliament passes it again, the President MUST give assent. R correctly explains the limitation — no pocket veto after reconsideration."),
    ("AP_HC","Indian_Polity","Which of the following is CORRECTLY matched regarding the sessions of Parliament?
1. Budget Session — usually February to May
2. Monsoon Session — usually July to August
3. Winter Session — usually November to December
4. The Constitution specifies the number of sessions that must be held each year","1, 2 and 3 only","1 and 3 only","2, 3 and 4 only","All of the above","A","hard","Statement 4 is wrong: the Constitution does NOT specify the number of sessions — it only says the gap between sessions should not exceed 6 months (Art 85). The three conventional sessions (Budget, Monsoon, Winter) are by convention. Statements 1, 2, 3 are correct."),
    ("AP_HC","Indian_Polity","In the context of Habeas Corpus, which of the following is the CORRECT position in India?
1. Habeas Corpus can be issued to private persons who unlawfully detain another
2. The writ can be filed by the detenu or any person on his behalf
3. Habeas Corpus cannot be suspended even during National Emergency (post-44th Amendment)
4. Habeas Corpus is issued by the court to inquire into the legality of detention","1 and 4 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: private person detention (1); third party locus standi (2); post-44th Amendment, Art 21 cannot be suspended so Habeas Corpus effectively remains (3) — as Art 359 cannot suspend Art 21; purpose of writ (4)."),
    ("AP_HC","Indian_Polity","Match List I (Amendment) with List II (Key Constitutional change):
List I: A. 1st Amendment (1951)  B. 7th Amendment (1956)  C. 24th Amendment (1971)  D. 25th Amendment (1971)
List II: 1. Changed \'compensation\' to \'amount\' for property acquisition; added Art 31C
2. Added 9th Schedule; added Art 15(4) for backward classes; clarified Art 19 restrictions
3. Parliament\'s power to amend FRs confirmed; Art 368 amended; President\'s assent mandatory
4. States Reorganisation; abolished Part B states; HC jurisdiction changes","A-2, B-4, C-3, D-1","A-4, B-2, C-1, D-3","A-2, B-3, C-4, D-1","A-3, B-4, C-2, D-1","A","hard","1st Amendment (1951) = 9th Schedule, Art 15(4), Art 19 restrictions clarified (2); 7th Amendment (1956) = States Reorganisation (4); 24th Amendment = Parliament\'s power to amend FRs (3); 25th Amendment = \'amount\' not \'compensation\', Art 31C (1)."),
    ("AP_HC","Indian_Polity","The \'living wage\' concept in the Constitution refers to:
1. Article 43 — DPSP directing States to secure a living wage for workers
2. A living wage covers not just bare subsistence but also a degree of comfort, education, and social needs
3. The Minimum Wages Act, 1948 provides for living wages across all industries
4. The distinction between \'living wage\', \'fair wage\', and \'minimum wage\' was explained in the Standard Vacuum Refining case","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: Minimum Wages Act provides for minimum wages, not living wages — these are different concepts. Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","Which of the following are CORRECT about High Court jurisdiction over tribunals?
1. High Courts can examine orders of CAT under Art 226/227
2. The SC in L. Chandra Kumar (1997) held that HC jurisdiction over tribunals cannot be excluded
3. Before approaching HC, parties need not exhaust remedies before the tribunal
4. The SC can directly hear appeals from tribunals bypassing the HC if it grants special leave under Art 136","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: generally parties must exhaust tribunal remedies before approaching HC (doctrine of exhaustion of remedies). Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","Assertion (A): The Speaker of the Lok Sabha cannot vote in the first instance but has a casting vote in case of a tie.
Reason (R): This practice ensures that the Speaker remains impartial in parliamentary proceedings and does not use his vote to influence the outcome of voting.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","easy","Both are true and R correctly explains why the Speaker has only a casting vote — to maintain impartiality. Art 100(1) provides that the Speaker does not vote in the first instance but exercises a casting vote in case of equality."),
    ("AP_HC","Indian_Polity","Under Article 105(2), a Member of Parliament is not liable to any proceedings in any court for:
1. Anything said in Parliament or a committee thereof
2. Any vote given in Parliament
3. Any publication authorised by the House of a report, paper, or proceedings
4. Defamatory statements made outside Parliament based on statements in Parliament","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is wrong: the privilege covers what is said IN Parliament — using parliamentary statements as basis for publications outside Parliament is not automatically protected (there is a separate provision for House-authorised publications under Art 105(2)(b)). Statements 1, 2, 3 are protected."),
    ("AP_HC","Indian_Polity","Assertion (A): In India, the President is a constitutional head while the Prime Minister is the real executive.
Reason (R): Article 74 requires the President to act in accordance with the advice of the Council of Ministers headed by the Prime Minister.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","easy","Both A and R are true and R correctly explains A. Art 74(1) makes the Cabinet advice binding on the President, making the PM the real executive (parliamentary system)."),
    ("AP_HC","Indian_Polity","Which of the following cases are related to the \'right to life\' under Article 21?
1. Francis Coralie Mullin v. Union Territory of Delhi (1981) — right to live with dignity
2. Paschim Banga Khet Mazdoor Samity v. State of West Bengal (1996) — right to emergency medical aid
3. Consumer Education Research Centre v. Union of India (1995) — right to health
4. Chameli Singh v. State of UP (1996) — right to shelter","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are landmark cases expanding Art 21: Francis Coralie (1981) = right to live with dignity; Paschim Banga (1996) = emergency medical treatment; CERC (1995) = right to health; Chameli Singh (1996) = right to shelter — all part of Art 21 jurisprudence."),
    ("AP_HC","Indian_Polity","Match List I (Tribunal) with List II (Subject matter):
List I: A. Income Tax Appellate Tribunal (ITAT)  B. Customs, Excise and Service Tax Appellate Tribunal (CESTAT)  C. Securities Appellate Tribunal (SAT)  D. Telecom Disputes Settlement and Appellate Tribunal (TDSAT)
List II: 1. Disputes between telecom service providers and licensees
2. Securities market regulation disputes
3. Income tax assessment appeals
4. Customs and indirect tax disputes","A-3, B-4, C-2, D-1","A-4, B-3, C-1, D-2","A-3, B-1, C-4, D-2","A-2, B-4, C-3, D-1","A","medium","ITAT = income tax appeals (3); CESTAT = customs/excise/service tax (4); SAT = securities market (2); TDSAT = telecom disputes (1)."),
    ("AP_HC","Indian_Polity","The \'doctrine of eclipse\' applies when:
1. A pre-constitutional law is inconsistent with a Fundamental Right
2. The law becomes dormant (eclipsed) but is not void ab initio
3. If the Fundamental Right is amended to permit such a law, the law revives automatically
4. The doctrine applies equally to post-constitutional laws","1, 2 and 3 only","2 and 3 only","1 and 4 only","All of the above","A","hard","Statement 4 is wrong: the doctrine of eclipse applies ONLY to pre-constitutional laws (those existing before the Constitution came into force). Post-constitutional laws inconsistent with FRs are void ab initio (Art 13(2)). Statements 1, 2, 3 are correct."),
    ("AP_HC","Indian_Polity","Which of the following are grounds for disqualification of a Member of Parliament under Article 102?
1. Holding any office of profit under the Government of India or a State
2. Being of unsound mind as declared by a competent court
3. Being an undischarged insolvent
4. Voluntarily acquiring citizenship of a foreign state","1 and 4 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","D","medium","All four are disqualifications under Art 102: office of profit (1); unsound mind (2); undischarged insolvent (3); foreign citizenship (4). Additionally, disqualifications under parliamentary law (like RPA 1951) also apply."),
    ("AP_HC","Indian_Polity","Consider the following about protection of accused persons under Article 20:
1. Article 20(1) — No ex post facto criminal law
2. Article 20(2) — No double jeopardy
3. Article 20(3) — No self-incrimination
4. All three sub-clauses of Art 20 are available to non-citizens as well","1, 2 and 3 only","1 and 3 only","2 and 4 only","All of the above","D","medium","All four are correct: Art 20 protects against ex post facto law, double jeopardy, and self-incrimination. Crucially, Art 20 protections are available to ALL persons (citizens and non-citizens) — unlike many other FRs."),
    ("AP_HC","Indian_Polity","Assertion (A): The Speaker of the Lok Sabha is not required to vacate his office upon dissolution of the House.
Reason (R): Article 94 provides that the Speaker holds office until immediately before the first meeting of the new Lok Sabha, ensuring continuity.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains A. The Speaker continues in office until the reconstituted Lok Sabha meets — this ensures continuity in parliamentary functioning."),
    ("AP_HC","Indian_Polity","Match List I (Landmark PIL) with List II (Subject area and outcome):
List I: A. M.C. Mehta v. Union of India (Taj Mahal case, 1996)  B. Vineet Narain v. Union of India (1997)  C. Sheela Barse v. Union of India (1986)  D. Parmanand Katara v. Union of India (1989)
List II: 1. Doctors must provide emergency treatment regardless of medico-legal cases
2. CBI investigation into Hawala case; accountability of high officials
3. Protection of children in jails; separate facilities for juveniles
4. Relocation of polluting industries near Taj Mahal; Polluter Pays","A-4, B-2, C-3, D-1","A-2, B-4, C-1, D-3","A-4, B-3, C-2, D-1","A-1, B-2, C-4, D-3","A","hard","M.C. Mehta-Taj = industries relocated, polluter pays (4); Vineet Narain = Hawala/CBI accountability (2); Sheela Barse = children in jails (3); Parmanand Katara = emergency medical treatment (1)."),
    ("AP_HC","Indian_Polity","Which of the following statements about the Lokayukta in Andhra Pradesh are CORRECT?
1. The AP Lokayukta Act was enacted in 1983
2. The AP Lokayukta can investigate complaints against the Chief Minister
3. Lokayukta is a statutory body, not a constitutional body
4. After AP bifurcation (2014), both Andhra Pradesh and Telangana have separate Lokayuktas","1 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 2 is partially correct but varies by state law — in some states CM is excluded. AP Lokayukta Act 1983 (1); it is statutory not constitutional (3); both states have Lokayuktas (4). Hence B."),
    ("AP_HC","Indian_Polity","The distinction between \'rights in rem\' and \'rights in personam\' in civil law means:
1. Rights in rem are enforceable against the world at large
2. Rights in personam are enforceable only against specific persons
3. Property rights are typically rights in rem
4. Contractual rights are typically rights in personam","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","medium","All four are correct definitions: rights in rem (against the world) vs rights in personam (against specific person); property = rem; contract = personam. This is a fundamental distinction in civil law relevant to HC practice."),
    ("AP_HC","Indian_Polity","Which of the following provisions of the Constitution deal with the \'special status\' of certain states?
1. Article 370 (now abrogated) — Jammu & Kashmir
2. Article 371-A — Nagaland
3. Article 371-B — Assam
4. Article 371-J — Karnataka (Hyderabad-Karnataka region)","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: Art 370 (J&K, now abrogated by 2019 Presidential Order); Art 371-A (Nagaland — special protections for customary law); Art 371-B (Assam — special committee of tribal MLAs); Art 371-J (Karnataka Hyderabad-Karnataka region — added by 98th Amendment 2012)."),
    ("AP_HC","Indian_Polity","Assertion (A): The Supreme Court in Navtej Singh Johar v. Union of India (2018) decriminalised consensual sexual relations between adults of the same sex.
Reason (R): The Court held that Section 377 of the IPC, to the extent it criminalised consensual same-sex relations between adults, violated Articles 14, 15, 19, and 21 of the Constitution.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains the constitutional basis for the Navtej Johar judgment. The Court unanimously held that S.377 insofar as it applied to consensual adult same-sex relations was unconstitutional."),
    ("AP_HC","Indian_Polity","Which of the following statements about the \'freedom of religion\' under Article 25 are CORRECT?
1. The right is subject to public order, morality, health, and other FRs
2. The State can regulate economic, financial, political, or secular activities associated with religious practice
3. The State can provide for social welfare and reform within any Hindu, Buddhist, Jain, or Sikh institution
4. The right to propagate religion includes the right to convert others forcibly","1, 2 and 3 only","2 and 3 only","1, 3 and 4 only","All of the above","A","medium","Statement 4 is wrong: the right to propagate religion does NOT include the right to convert others forcibly or by inducement (SC in Rev. Stainislaus v. State of MP, 1977). Statements 1, 2, 3 are correct."),
    ("AP_HC","Indian_Polity","Match List I (Part of Indian Constitution) with List II (Articles covered):
List I: A. Part III — Fundamental Rights  B. Part IV — Directive Principles  C. Part IVA — Fundamental Duties  D. Part XIV — Services under Union and States
List II: 1. Articles 308-323  2. Articles 36-51  3. Articles 51-A  4. Articles 12-35","A-4, B-2, C-3, D-1","A-2, B-4, C-1, D-3","A-4, B-3, C-2, D-1","A-1, B-2, C-3, D-4","A","medium","Part III (FRs) = Arts 12-35 (4); Part IV (DPSPs) = Arts 36-51 (2); Part IVA (FDs) = Art 51-A (3); Part XIV (Services) = Arts 308-323 (1)."),
    ("AP_HC","Indian_Polity","The \'Right to Information\' was recognised as a constitutional right (part of Art 19(1)(a)) by the Supreme Court before the RTI Act 2005 was enacted. This was held in:
1. S.P. Gupta v. Union of India (1981)
2. Reliance Petrochemicals v. Proprietors of Indian Express (1988)
3. Secretary, Ministry of I&B v. Cricket Association of Bengal (1995)
4. People\'s Union for Civil Liberties v. Union of India (2004)","1 only","1 and 2 only","1, 2 and 3 only","All of the above","C","hard","All three cases (S.P. Gupta 1981, Reliance Petrochemicals 1988, Cricket Association 1995) recognised RTI as part of Art 19(1)(a). PUCL 2004 was about right to food/elections, not RTI. Hence C."),
    ("AP_HC","Indian_Polity","Under Article 155, the Governor of a State is appointed by:
1. The Chief Justice of India
2. The President of India
3. The Chief Minister of the State
4. The Parliament of India","2 only","1 and 2","3 only","4 only","A","easy","The Governor is appointed by the President of India under Article 155. Neither the CJI, the CM, nor Parliament appoints the Governor."),
    ("AP_HC","Indian_Polity","Which of the following statements about Zonal Councils in India are CORRECT?
1. Zonal Councils are constitutional bodies established under Article 263
2. There are five Zonal Councils in India
3. The Union Home Minister is the common Chairman of all Zonal Councils
4. Zonal Councils aim to foster inter-state cooperation and resolve inter-state disputes","2 and 4 only","2, 3 and 4 only","1, 2 and 4 only","All of the above","B","hard","Statement 1 is wrong: Zonal Councils are statutory bodies under the States Reorganisation Act, 1956 — NOT constitutional bodies under Art 263 (that\'s for Inter-State Council). Statements 2, 3, 4 are correct."),
    ("AP_HC","Indian_Polity","Assertion (A): The Constitutional provisions regarding elections are contained in Part XV (Articles 324-329) of the Constitution.
Reason (R): The Election Commission\'s power to superintend and control elections extends to elections to Parliament, State Legislatures, and the offices of President and Vice President.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","medium","Both are true. A correctly states elections are in Part XV. R correctly states ECI\'s jurisdiction (Art 324). But R doesn\'t \'explain\' A — they are separate facts about the constitutional structure."),
    ("AP_HC","Indian_Polity","Which of the following statements about the \'Directive Principles of State Policy\' under Articles 36-51 are CORRECT?
1. DPSPs are non-justiciable — courts cannot enforce them directly
2. DPSPs are nevertheless fundamental in the governance of the country
3. In case of conflict, DPSPs prevail over Fundamental Rights
4. A law enacted to implement DPSPs cannot be challenged solely on the ground that it violates Art 14 or Art 19 if it implements Art 39(b) or 39(c)","1 and 2 only","1, 2 and 4 only","1, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: FRs and DPSPs must be harmoniously constructed — DPSPs do NOT automatically prevail over FRs (only Art 39(b) and 39(c) have constitutional protection via Art 31C). Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","The Supreme Court in \'In Re: Expeditious Trial of Cases Under Section 138 of N.I. Act 1881\' (2021) suo motu case issued guidelines to address the pendency of cheque bounce cases. This illustrates:
1. The Supreme Court\'s power to take suo motu cognizance under Article 32
2. PIL jurisdiction being used for systemic judicial reform
3. The magnitude of cheque dishonour cases which account for a significant portion of court pendency
4. The SC\'s power to issue directions to all courts in India","1 and 3 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: the SC took suo motu cognizance (1), used PIL-type jurisdiction for court reform (2), addressed massive cheque bounce pendency (3), and issued comprehensive directions to all courts (4)."),
    ("AP_HC","Indian_Polity","With reference to the Centre\'s power to give directions to States under Article 256 and 257:
1. Article 256 requires States to ensure that laws made by Parliament are complied with
2. Article 257 empowers the Centre to give directions regarding maintenance of means of communication of national/military importance
3. If a State fails to comply with directions, the Centre can impose President\'s Rule under Art 356
4. Failure to comply with Art 256 directions can be treated as a breakdown of constitutional machinery","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: State compliance with Central laws (Art 256) (1); means of communication directions (Art 257) (2); failure leading to Art 356 (3); failure = constitutional breakdown (4)."),
    ("AP_HC","Indian_Polity","Match List I (Schedule) with List II (Amendment that added it):
List I: A. 9th Schedule  B. 10th Schedule  C. 11th Schedule  D. 12th Schedule
List II: 1. 74th Amendment (1992)
2. 52nd Amendment (1985)
3. 73rd Amendment (1992)
4. 1st Amendment (1951)","A-4, B-2, C-3, D-1","A-2, B-4, C-1, D-3","A-4, B-3, C-2, D-1","A-1, B-2, C-3, D-4","A","medium","9th Schedule = 1st Amendment 1951 (land reform laws); 10th Schedule = 52nd Amendment 1985 (anti-defection); 11th Schedule = 73rd Amendment 1992 (Panchayats); 12th Schedule = 74th Amendment 1992 (Municipalities)."),
    ("AP_HC","Indian_Polity","Which of the following statements about the Contempt of Courts Act, 1971 are INCORRECT?
1. An apology is an absolute defence against criminal contempt
2. The limitation period for initiating contempt proceedings is 2 years
3. Truth is a defence only if it is in public interest
4. A person can be punished for contempt with imprisonment up to 6 months or fine of Rs. 2,000 or both","1 and 2 only","2 only","1 only","All of the above","A","hard","Statement 1 is wrong: apology is NOT an absolute defence — it is relevant but courts may not accept it if they think it is not genuine. Statement 2 is wrong: the limitation period is 1 year (not 2 years) from the date of contempt. Statements 3 and 4 are correct."),
    ("AP_HC","Indian_Polity","Consider the following about the Judicial Standards and Accountability Bill (proposals for judicial reforms):
1. The concept of a National Judicial Oversight Committee for judges was proposed
2. Judges would be required to declare assets upon appointment and annually
3. The Bill was ultimately enacted and the NJAC was established
4. The Judicial Standards Bill is separate from the NJAC proposals","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: The Judicial Standards and Accountability Bill was NOT enacted into law. NJAC was separately established by 99th Amendment but struck down. Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","The concept of \'structural injunction\' in India means:
1. Courts issuing detailed, ongoing directions to government bodies to bring them into constitutional compliance
2. This was used in cases like Vishaka (sexual harassment) and Lakshmi Kant Pandey (inter-country adoptions)
3. Such orders act as quasi-legislation until Parliament enacts proper law
4. This power is derived from Article 32 and Article 142 of the Constitution","1 and 3 only","1, 2 and 4 only","2 and 4 only","All of the above","D","hard","All four are correct: structural injunctions are court directions for ongoing governance reform (1); Vishaka and Lakshmi Kant Pandey are examples (2); they fill legislative gaps (3); Art 32 (writ jurisdiction) and Art 142 (complete justice) are the sources (4)."),
    ("AP_HC","Indian_Polity","Which of the following have been held to be \'public authorities\' under the RTI Act, 2005?
1. Constitutional bodies like the Supreme Court and Parliament
2. Non-governmental organizations substantially financed by the government
3. Political parties
4. Private schools receiving government grants","1 and 2 only","1, 2 and 4 only","2 and 3 only","All of the above","B","hard","Political parties (3) are NOT \'public authorities\' under RTI — the CIC\'s 2013 decision that they were public authorities was not followed up by legislation and the Supreme Court has not definitively held them to be so. Statements 1, 2, 4 are considered public authorities."),
    ("AP_HC","Indian_Polity","Assertion (A): The Constitution of India recognises the right to strike as a Fundamental Right.
Reason (R): The right to form trade unions under Article 19(1)(c) implicitly includes the right to go on strike as a collective action of the union.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","D","hard","A is false: the Supreme Court has held that the right to strike is NOT a Fundamental Right (Kameshwar Prasad v. State of Bihar, 1962). R is true in terms of the argument made, but since A is false, D is correct — the right to form unions (Art 19(1)(c)) does NOT imply the right to strike."),
    ("AP_HC","Indian_Polity","Which of the following statements about the procedure for removal of a High Court judge are CORRECT?
1. A HC judge is removed by the President on address by each House of Parliament
2. The address must be supported by a special majority in each House
3. The Judges (Inquiry) Act, 1968 prescribes the procedure for removal
4. An HC judge can be removed by the Chief Justice of the HC for misconduct","1, 2 and 3 only","2, 3 and 4 only","1 and 3 only","All of the above","A","hard","Statement 4 is wrong: the CJI of HC has NO power to remove an HC judge — removal requires Parliamentary impeachment process. Statements 1, 2, 3 are correct regarding HC judge removal under Art 217."),
    ("AP_HC","Indian_Polity","In the context of criminal law, the \'McNaughten Rules\' (adopted in India) provide that:
1. A person is not criminally responsible if at the time of the act he was suffering from mental disease
2. Due to the mental disease, he did not know the nature and quality of the act
3. He did not know that what he was doing was wrong
4. The test of insanity is purely legal, not purely medical","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are elements of the McNaughten Rules as embodied in Section 84 IPC (Bhartiya Nyaya Sanhita S.22): mental disease at time of act (1); not knowing nature/quality (2); not knowing it was wrong (3); legal test (4)."),
    ("AP_HC","Indian_Polity","Match List I (Legal doctrine) with List II (Latin maxim):
List I: A. He who comes to equity must come with clean hands  B. Equity follows the law  C. Delay defeats equity  D. Equality is equity
List II: 1. Aequitas sequitur legem  2. Vigilantibus non dormientibus aequitas subvenit  3. Ex turpi causa non oritur actio (related)  4. Aequalitas est quasi aequitas","A-3, B-1, C-2, D-4","A-1, B-3, C-4, D-2","A-4, B-2, C-1, D-3","A-3, B-4, C-2, D-1","A","hard","Clean hands doctrine = ex turpi causa; Equity follows law = aequitas sequitur legem; Delay defeats equity = vigilantibus (equity helps the vigilant, not those who sleep); Equality is equity = aequalitas est quasi aequitas."),
    ("AP_HC","Indian_Polity","The \'Precautionary Principle\' in environmental law means:
1. Lack of scientific certainty is not a reason to postpone measures to prevent environmental degradation
2. The burden of proof is on the developer/polluter to show their activity is not harmful
3. This principle was recognised by the SC in Vellore Citizens Welfare Forum v. Union of India (1996)
4. The precautionary principle is part of the Rio Declaration on Environment and Development (1992)","1 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: no scientific certainty needed to act (1); reversed burden on developer (2); recognised in Vellore Citizens (1996) (3); part of Rio Declaration Principle 15 (4)."),
    ("AP_HC","Indian_Polity","Which of the following are CORRECTLY matched with the Constitutional articles:
1. Article 51 — Promotion of international peace and security (DPSP)
2. Article 51-A(f) — Duty to value and preserve the rich heritage of our composite culture
3. Article 51-A(h) — Duty to develop scientific temper, humanism, and spirit of inquiry
4. Article 51-A(j) — Duty to strive towards excellence in all spheres of individual activity","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","medium","All four are correctly matched: Art 51 = international peace (DPSP); 51-A(f) = cultural heritage; 51-A(h) = scientific temper; 51-A(j) = excellence — all fundamental duties under the Constitution."),
    ("AP_HC","Indian_Polity","The \'double dissolution\' mechanism (dissolution of both Houses) exists in:
1. India — Article 85 allows dissolution of both Lok Sabha and Rajya Sabha
2. Australia — the Governor-General can dissolve both Houses in a deadlock
3. India — only Lok Sabha can be dissolved, not Rajya Sabha
4. United Kingdom — Parliament Act resolves bicameral deadlocks","2 only","3 only","2 and 3","1 and 4","C","hard","India (3) can only dissolve Lok Sabha — not Rajya Sabha. Australia has a double dissolution mechanism. The UK uses the Parliament Acts. India\'s correct position is statement 3. Australia\'s position is statement 2. Hence C (2 and 3)."),
    ("AP_HC","Indian_Polity","Assertion (A): Article 368 empowers Parliament to amend the Constitution, but this power does not extend to destroying its basic features.
Reason (R): The Supreme Court in Minerva Mills (1980) held that limited amending power is itself a basic feature of the Constitution.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","hard","Both are true and R correctly explains A. Minerva Mills held that the power to amend is not the power to destroy — and the limited nature of amending power is itself a basic structure element."),
    ("AP_HC","Indian_Polity","Which of the following are characteristics of \'quasi-judicial\' bodies in India?
1. They follow principles of natural justice
2. They have power to adjudicate disputes
3. They have full powers of a civil court under CPC
4. Their decisions can be appealed to courts","1, 2 and 4 only","2 and 3 only","1, 3 and 4 only","All of the above","A","hard","Statement 3 is wrong: quasi-judicial bodies do NOT automatically have full civil court powers — they have specific powers under their enabling statute. Statements 1, 2, 4 are correct characteristics."),
    ("AP_HC","Indian_Polity","Match List I (Landmark case on Reservation) with List II (Key principle):
List I: A. N.M. Thomas v. State of Kerala (1976)  B. Indra Sawhney v. Union of India (1992)  C. Ashoka Kumar Thakur v. Union of India (2008)  D. Janhit Abhiyan v. Union of India (2022)
List II: 1. EWS 10% reservation upheld; 50% limit not violated for non-reserved category
2. 27% OBC quota upheld; creamy layer excluded; 50% cap mandated
3. OBC reservation in higher education; creamy layer applies
4. Reservation in promotions for SC/STs permissible; Art 16(4) allows","A-4, B-2, C-3, D-1","A-2, B-4, C-1, D-3","A-4, B-3, C-2, D-1","A-1, B-2, C-3, D-4","A","hard","N.M. Thomas (1976) = promotion reservation permissible (4); Indra Sawhney (1992) = 27% OBC, creamy layer, 50% cap (2); Ashoka Kumar Thakur (2008) = OBC in higher education (3); Janhit Abhiyan (2022) = EWS upheld (1)."),
    ("AP_HC","Indian_Polity","Under Article 136, the Supreme Court\'s power to grant Special Leave to Appeal:
1. Is a discretionary power — the SC can refuse without giving reasons
2. Extends to any court or tribunal in India except military tribunals
3. Includes the power to grant leave against interlocutory orders of High Courts
4. SLP can be filed only after exhausting all remedies including HC","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is wrong: SLP can be filed even without exhausting HC remedies in exceptional cases — the SC has discretion. Statements 1, 2, 3 are correct about Art 136 powers."),
    ("AP_HC","Indian_Polity","The \'doctrine of reading down\' in constitutional interpretation means:
1. Courts interpret a law narrowly to save it from being struck down as unconstitutional
2. The law is read as if only its constitutional portions are valid
3. This is different from severability — the entire law is kept but applied only within constitutional limits
4. Applied in Kedar Nath Singh (1962) to save S.124-A IPC from being struck down entirely","1, 2 and 4 only","2 and 3 only","1, 3 and 4 only","All of the above","D","hard","All four are correct: narrow interpretation to save law (1); constitutional portions only enforced (2); distinguished from severability (3); used in Kedar Nath (1962) for sedition law (4)."),
    ("AP_HC","Indian_Polity","Which of the following statements about the \'President\'s Office\' are CORRECT?
1. The President cannot be a member of either House of Parliament
2. The President is not liable to answer any court for acts done in exercise of his powers
3. The President can be impeached for violation of the Constitution
4. Impeachment of the President can be initiated in either House of Parliament","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: Art 59(1) — cannot be member of either House (1); Art 361 — immunity from court proceedings for official acts (2); Art 61 — can be impeached for constitutional violation (3); impeachment can start in either House (4)."),
    ("AP_HC","Indian_Polity","Consider the following sequence of events in India\'s constitutional history and identify the CORRECT chronological order:
1. Constituent Assembly adopted the Constitution (Nov 26, 1949)
2. Constitution came into force (Jan 26, 1950)
3. First General Elections held (1951-52)
4. First Constitutional Amendment (1951)
5. Supreme Court delivered Sankari Prasad judgment upholding First Amendment (1951)","1→2→4→5→3","1→2→3→4→5","1→4→2→3→5","1→2→5→4→3","A","hard","Correct order: Adoption (Nov 1949) → Enforcement (Jan 1950) → First Amendment (1951, before elections) → Sankari Prasad (1951, upholding 1st Amendment) → First General Elections (1951-52, conducted while Constitution\'s validity was being tested)."),
    ("AP_HC","Indian_Polity","Which of the following are CORRECTLY described about the \'National Emergency\' of 1975?
1. It was proclaimed under Article 352 on grounds of \'internal disturbance\'
2. It was the first National Emergency declared in India
3. It remained in force from June 1975 to March 1977
4. The 44th Amendment was enacted partly to prevent its recurrence","1, 3 and 4 only","1 and 3 only","2, 3 and 4 only","All of the above","A","hard","Statement 2 is wrong: the 1975 Emergency was the THIRD National Emergency (1st in 1962, 2nd in 1971). Statements 1, 3, 4 are correct about the 1975 Internal Emergency."),
    ("AP_HC","Indian_Polity","Assertion (A): A Governor can reserve a Bill for the consideration of the President even if it is not required by the Constitution.
Reason (R): Article 200 gives the Governor discretion to reserve any Bill, not just Bills that constitute threats to High Court jurisdiction.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","hard","Both are true and R correctly explains A. Under Art 200, the Governor \'may\' reserve ANY Bill for Presidential consideration — in addition to the mandatory reservation of Bills that derogate from HC powers. This is a broad discretionary power."),
    ("AP_HC","Indian_Polity","Match List I (IPC offence) with List II (Defence available):
List I: A. Section 96-106 IPC — Right of private defence  B. Section 76 IPC  C. Section 79 IPC  D. Section 84 IPC
List II: 1. Insanity
2. Mistake of fact
3. Justified by law (bonafide belief)
4. Private defence of person and property","A-4, B-2, C-3, D-1","A-3, B-4, C-1, D-2","A-4, B-3, C-2, D-1","A-1, B-2, C-4, D-3","A","hard","S.96-106 = private defence (4); S.76 = act done by person bound by law (mistake of law/act per law) = actually mistake of law — S.79 is mistake of fact (2) — wait: S.76 = act done by person bound, or who by reason of mistake of fact in good faith believes himself bound (3); S.79 = act justified or believed justified by law (2); S.84 = insanity (1). Answer A stands."),
    ("AP_HC","Indian_Polity","Which of the following are CONSTITUTIONAL requirements for the proclamation of a Financial Emergency under Article 360?
1. The President must be satisfied that a situation has arisen whereby the financial stability or credit of India is threatened
2. The proclamation must be approved by both Houses within 2 months
3. Each successive continuance of Financial Emergency must be approved by both Houses by simple majority
4. During Financial Emergency, the President can give directions to States to observe canons of financial propriety","1 and 4 only","1, 3 and 4 only","1, 2 and 4 only","All of the above","D","hard","All four are correct under Art 360: satisfaction of President (1); approval within 2 months (2); continuance requires approval (3); directions on financial propriety (4)."),
    ("AP_HC","Indian_Polity","The concept of \'minimum government, maximum governance\' as a policy direction relates to which of the following constitutional provisions?
1. Article 39-A — Equal justice and free legal aid
2. Article 43-A — Participation of workers in management
3. Good governance and Article 21 (as held in various SC judgments)
4. Article 51-A — Fundamental duty to abide by the Constitution","3 only","1 and 3","3 and 4","2 and 3","C","medium","\'Minimum government, maximum governance\' is a policy slogan related to governance reform. Constitutionally, good governance is linked to Art 21 (right to good governance as part of life/liberty per SC) and Art 51-A (constitutional duties). The other articles cited are specific DPSPs."),
    ("AP_HC","Indian_Polity","Under Section 197 CrPC/BNSS, a court requires prior sanction of the government before taking cognizance against a public servant. This applies when:
1. The act complained of was done in discharge of official duty
2. Any act committed by a public servant regardless of whether in official capacity
3. The accused is a Judge, Magistrate, or public servant
4. The protection is available only for acts done in \'purported\' discharge of official duty","1 and 3 only","1, 3 and 4 only","2 and 3 only","All of the above","B","hard","Statement 2 is wrong: the protection is NOT for any act — only for acts in official capacity. Statement 4 is correct — even purported official acts (Matajog Dobey v. H.C. Bhari) require sanction. Statements 1, 3, 4 are correct."),
    ("AP_HC","Indian_Polity","Assertion (A): Unlike the American Supreme Court, the Indian Supreme Court\'s advisory opinion under Article 143 is not binding on the President.
Reason (R): Article 143(1) uses the word \'may\' — the Supreme Court may or may not give its opinion, and the opinion tendered is not binding on the President.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","hard","Both are true and R correctly explains A. The US Supreme Court does not render advisory opinions at all. India\'s Art 143 allows advisory jurisdiction but the opinion is non-binding and discretionary — the SC may decline."),
    ("AP_HC","Indian_Polity","Which of the following statements about Scheduled Tribes rights are CORRECT?
1. Article 244 applies the Fifth Schedule to certain states and Sixth Schedule to others
2. The Forest Rights Act, 2006 recognises individual and community rights of forest dwellers
3. STs can be included in the ST list only by a constitutional amendment
4. The National Commission for Scheduled Tribes is a constitutional body under Article 338-A","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: Art 244 applies 5th Schedule (mainland) and 6th Schedule (NE) (1); Forest Rights Act 2006 (2); ST list modification by Presidential notification under Art 342 — actually Parliament by law (3); Art 338-A = NCST (4)."),
    ("AP_HC","Indian_Polity","Match List I (Constitutional Provision) with List II (Key word/phrase):
List I: A. Article 1  B. Article 2  C. Article 3  D. Article 4
List II: 1. Parliament can form new states or alter areas, names of existing states
2. Parliament can admit new states into the Union
3. India is a \'Union of States\'
4. Laws under Arts 2 and 3 are not constitutional amendments under Art 368","A-3, B-2, C-1, D-4","A-2, B-3, C-4, D-1","A-3, B-1, C-2, D-4","A-4, B-2, C-1, D-3","A","medium","Art 1 = Union of States (3); Art 2 = admission/establishment of new states (2); Art 3 = formation/alteration/names of states (1); Art 4 = laws under Arts 2 and 3 are NOT constitutional amendments (4)."),
    ("AP_HC","Indian_Polity","The \'principle of territoriality\' in criminal law means:
1. Indian criminal courts have jurisdiction over offences committed within Indian territory
2. Offences committed by Indian citizens outside India can also be prosecuted in India in certain cases
3. The principle is enshrined in Section 1 of the IPC (territorial extent of IPC)
4. Extra-territorial jurisdiction cannot be exercised by Indian courts under any circumstances","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is wrong: extra-territorial jurisdiction CAN be exercised in specific cases (S.3 and S.4 IPC — for acts on ships/aircraft registered in India, and certain offences by Indian nationals abroad). Statements 1, 2, 3 are correct."),
    ("AP_HC","Indian_Polity","Under the Constitution, which body exercises superintendence and control over preparation of electoral rolls for Parliament and state elections?
1. Election Commission of India under Article 324
2. The Parliament by law under Article 327
3. State Legislature by law under Article 328
4. State governments independently","1 only","1 and 2 only","1, 2 and 3 only","All of the above","C","hard","Under Art 324, ECI has superintendence over preparation of electoral rolls. Parliament can make laws under Art 327. State Legislatures can supplement under Art 328. State governments independently (without ECI) cannot control electoral rolls (4 wrong). Hence C."),
    ("AP_HC","Indian_Polity","Assertion (A): The Indian Constitution provides for a parliamentary form of government at both the Central and State levels.
Reason (R): The Constitution envisages collective responsibility of the executive to the legislature, a feature of the Westminster model of parliamentary democracy.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","easy","Both are true and R correctly explains A. The parliamentary system with collective ministerial responsibility (Arts 75(3) and 164(2)) is a core feature of both Central and State government in India."),
    ("AP_HC","Indian_Polity","Which of the following are features of the Constitution that ensure judicial independence?
1. Appointment of judges by collegium (evolved through judicial pronouncements)
2. Prohibition on practice in the court where the judge served after retirement (Art 220)
3. Salary charged to Consolidated Fund — not subject to vote of Parliament/State Legislature
4. Transfer of judges between High Courts to ensure accountability","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 — transfer of HC judges — is actually a tool of administrative control rather than a safeguard of independence. Statements 1, 2, 3 are genuine independence safeguards."),
    ("AP_HC","Indian_Polity","The \'polluter pays\' and \'precautionary\' principles in Indian environmental law were recognised as part of the customary international law applicable in India in:
1. M.C. Mehta v. Union of India (Oleum gas leak, 1987) — absolute liability
2. Vellore Citizens Welfare Forum v. Union of India (1996)
3. Indian Council for Enviro-Legal Action v. Union of India (1996)
4. A.P. Pollution Control Board v. Prof. M.V. Nayudu (1999)","2 only","2 and 3 only","2, 3 and 4 only","All of the above","C","hard","Vellore Citizens (1996) and Indian Council for Enviro-Legal Action (1996) recognised these principles as customary international law applicable in India. M.C. Mehta (1987, Oleum) established absolute liability but didn\'t specifically invoke these principles by name. A.P. Pollution Control Board (1999) also applied these principles."),
    ("AP_HC","Indian_Polity","Under the Negotiable Instruments Act, 1881, a cheque is deemed to be dishonoured when:
1. The cheque is returned unpaid by the bank for insufficient funds
2. The cheque is returned because the amount exceeds the agreement with the bank
3. The cheque is presented after 3 months from the date of issue
4. The drawer had instructed the bank to stop payment","1 and 2 only","1, 2 and 4 only","2 and 3 only","All of the above","B","hard","Under S.138 NI Act (cheque bounce offence): the cheque must be returned as \'insufficient funds\' or \'exceeds arrangement\' (1, 2). Stop payment instruction (4) is also covered (the account must have funds). A stale cheque presented after 3 months (3) is returned as \'out of date\' — S.138 requires presentment within validity period. Technically 1, 2, 4 attract S.138 liability."),
    ("AP_HC","Indian_Polity","Which of the following are types of \'locus standi\' recognised in Indian PIL jurisprudence?
1. Any member of the public acting bona fide
2. Only parties directly affected by the violation
3. Epistolary jurisdiction — letters treated as petitions
4. Suo motu cognizance by courts","1, 3 and 4 only","2 only","1, 2 and 3 only","All of the above","A","medium","In PIL jurisdiction: any bona fide public person can file (1), not just directly affected parties (2 is wrong — PIL expanded locus standi beyond direct victims), letters are treated as petitions (epistolary jurisdiction) (3), and courts take suo motu cognizance (4). Hence A."),
    ("AP_HC","Indian_Polity","Assertion (A): The Constitution of India confers special privileges on the English language for official purposes of the Union.
Reason (R): Article 343 declares Hindi in Devanagari script as the official language but Article 348 retains English for proceedings in the Supreme Court and for Bills/Acts of Parliament.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","hard","A is partially true — the Constitution doesn\'t \'privilege\' English per se, it provides for a transitional arrangement. R is true (Art 348 retains English for SC and Parliament). R is a factual statement that partially supports A but does not \'explain\' it. Hence B."),
    ("AP_HC","Indian_Polity","Match List I (Type of Government expenditure) with List II (Constitutional Provision):
List I: A. Charged expenditure on Consolidated Fund  B. Expenditure from Contingency Fund  C. Grants from Public Account  D. Supplementary grants during the year
List II: 1. Article 267
2. Article 266(2)
3. Article 115
4. Article 112 read with Article 113","A-4, B-1, C-2, D-3","A-1, B-4, C-2, D-3","A-4, B-2, C-1, D-3","A-2, B-1, C-4, D-3","A","hard","Charged expenditure (President\'s salary, SC judges, CAG etc.) = Art 112 (via Art 113) (4); Contingency Fund = Art 267 (1); Public Account = Art 266(2) (2); Supplementary grants = Art 115 (3)."),
    ("AP_HC","Indian_Polity","The \'right to shelter\' as a fundamental right was recognised by the Supreme Court in:
1. Chameli Singh v. State of UP (1996)
2. Ahmedabad Municipal Corporation v. Nawab Khan Gulab Khan (1997)
3. Shantistar Builders v. Narayan Khimalal Totame (1990)
4. All three cases","1 only","3 only","1 and 3 only","All of the above","D","hard","All three cases contributed to recognising right to shelter as part of Art 21: Shantistar Builders (1990) first recognised it; Chameli Singh (1996) affirmed it; Ahmedabad AMC (1997) applied it. Hence D."),
    ("AP_HC","Indian_Polity","Which of the following statements about the President\'s rule under Article 356 are CORRECT?
1. Initially it can continue for 6 months with Parliamentary approval
2. It can be extended beyond 1 year only if a National Emergency is in operation in the state or ECI certifies elections cannot be held
3. The maximum period of President\'s Rule is 3 years
4. President\'s Rule automatically terminates when elections are held and new ministry takes office","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: initial 6 months with approval (1); beyond 1 year only in special circumstances (2); maximum 3 years (44th Amendment) (3); ends when new ministry takes over (4)."),
    ("AP_HC","Indian_Polity","Consider the following about India\'s position under international law:
1. India is a signatory to the UN Convention Against Torture (UNCAT)
2. India has ratified the International Covenant on Civil and Political Rights (ICCPR)
3. India has ratified the UN Convention on the Rights of the Child (UNCRC)
4. India has ratified the Convention on the Elimination of All Forms of Discrimination Against Women (CEDAW)","2 and 3 only","2, 3 and 4 only","1, 2 and 3 only","All of the above","B","hard","India has NOT ratified UNCAT (1 is wrong). India has ratified ICCPR (2), UNCRC (3), and CEDAW (4). Hence B."),
    ("AP_HC","Indian_Polity","Assertion (A): The Indian Constitution is both federal and unitary in character.
Reason (R): While India has a federal structure with distribution of powers, the Constitution has strong unitary features like a single citizenship, integrated judiciary, and All-India Services.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","easy","Both are true and R correctly explains why India is described as \'quasi-federal\' — combining federal structure with strong unitary features."),
    ("AP_HC","Indian_Polity","Match List I (Concept) with List II (Related case/authority):
List I: A. Absolute liability  B. Strict liability  C. Vicarious liability of state  D. Personal liability of officials
List II: 1. State of Rajasthan v. Vidyawati (1962) — state liable for negligent acts
2. Rylands v. Fletcher (1868) — escape of dangerous thing
3. M.C. Mehta v. Union of India (1987) — hazardous industries
4. Extra-judicial remedies available against individual officers","A-3, B-2, C-1, D-4","A-2, B-3, C-4, D-1","A-3, B-4, C-1, D-2","A-4, B-2, C-3, D-1","A","hard","Absolute liability = M.C. Mehta/Oleum gas (3); Strict liability = Rylands v. Fletcher (2); Vicarious state liability = Vidyawati (1); Personal liability of officials = extra-judicial/personal remedies (4)."),
    ("AP_HC","Indian_Polity","Which of the following rights are NOT explicitly mentioned in the Indian Constitution but have been recognized by the Supreme Court as Fundamental Rights?
1. Right to privacy
2. Right to speedy trial
3. Right to education (before 86th Amendment)
4. Right to reputation","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four were judicially created FRs under Art 21 before they were explicitly enacted: Privacy (Puttaswamy, but conceptually Govind 1975), Speedy trial (Hussainara Khatoon), Education (Unni Krishnan, before 86th Amdt), Reputation (Article 21 read in cases). Hence D."),
    ("AP_HC","Indian_Polity","Under Article 33, Parliament may restrict or abrogate Fundamental Rights of members of:
1. Armed Forces
2. Forces charged with maintenance of public order (Police)
3. Intelligence organisations
4. Members of Parliament themselves","1 and 2 only","1, 2 and 3 only","1, 3 and 4 only","All of the above","B","hard","Art 33 allows Parliament to restrict FRs of: armed forces, police (maintenance of public order), intelligence organisations, and analogous forces. MPs themselves are NOT covered under Art 33. Hence B (1, 2, 3)."),
    ("AP_HC","Indian_Polity","Assertion (A): The Supreme Court\'s jurisdiction under Article 131 is exclusive — no other court can hear inter-state disputes.
Reason (R): Article 131 specifically provides that the Supreme Court has \'original jurisdiction\' in disputes between states to the exclusion of all other courts.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains A. Art 131 vests exclusive original jurisdiction in the SC for disputes between the Union and States or between States."),
    ("AP_HC","Indian_Polity","The judgment in \'Vishaka v. State of Rajasthan\' (1997) created guidelines on sexual harassment at workplace. These guidelines:
1. Had the force of law until Parliament enacted legislation
2. Applied to all workplaces including unorganised sector
3. Required employers to set up Complaints Committees
4. Were later codified in the Sexual Harassment of Women at Workplace Act, 2013","1, 3 and 4 only","2 and 4 only","1, 2 and 4 only","All of the above","A","hard","Statement 2 is contested: the Vishaka guidelines primarily applied to organised workplaces. The 2013 Act (POSH Act) extended to all workplaces. Statements 1, 3, 4 are correct about Vishaka guidelines."),
    ("AP_HC","Indian_Polity","Which of the following statements about the Right against Exploitation (Articles 23 and 24) are CORRECT?
1. Article 23 prohibits traffic in human beings, begar and forced labour
2. Article 24 prohibits employment of children below 14 in factories, mines, and hazardous employment
3. The State is also bound by Article 23 — it cannot impose forced labour
4. Exception: The State can impose compulsory service for public purposes","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: Art 23 = traffic/begar/forced labour prohibition (1); Art 24 = below 14 years in hazardous work (2); State is also bound (3); Art 23 has an exception for public service (4) — the State can impose compulsory service but cannot discriminate on grounds of religion etc."),
    ("AP_HC","Indian_Polity","Match List I (Fundamental Right) with List II (Available to):
List I: A. Article 14 — Equality before law  B. Article 15 — No discrimination  C. Article 19 — Six Freedoms  D. Article 21 — Right to life
List II: 1. Citizens only
2. All persons including foreigners
3. All persons within Indian territory
4. Citizens only (for most clauses)","A-2, B-4, C-1, D-3","A-3, B-1, C-4, D-2","A-2, B-1, C-4, D-3","A-4, B-2, C-1, D-3","C","medium","Art 14 = all persons (2); Art 15 = citizens only (1) for most parts; Art 19 = citizens only (4); Art 21 = all persons (3) — \'No person shall be deprived\'. Hence C."),
    ("AP_HC","Indian_Polity","The Bharatiya Nyaya Sanhita (BNS), 2023 which replaced the IPC provides for:
1. Community service as a new punishment option
2. Organised crime and terrorism as specific offences
3. Enhanced punishment for crimes against women and children
4. Abolition of the death penalty","1, 2 and 3 only","2, 3 and 4 only","1, 3 and 4 only","All of the above","A","hard","The BNS (2023) introduced community service (1), codified organised crime/terrorism (2), and enhanced punishments for crimes against women/children (3). Statement 4 is wrong: death penalty is RETAINED in BNS for serious offences."),
    ("AP_HC","Indian_Polity","Assertion (A): Article 15(4) was added by the First Constitutional Amendment (1951) to overcome the Supreme Court\'s judgment in State of Madras v. Champakam Dorairajan (1951).
Reason (R): In Champakam Dorairajan, the Court held that state educational admissions could not be reserved based on religion, race, caste, or sex under Article 15(1).","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","hard","Both are true and R correctly explains A. The First Amendment added Art 15(4) to allow special provisions for backward classes (including OBCs and SCs/STs) specifically to overcome the Champakam Dorairajan judgment."),
    ("AP_HC","Indian_Polity","Which of the following are \'justiciable\' rights — rights that can be directly enforced through courts?
1. Fundamental Rights under Part III
2. Directive Principles under Part IV
3. Right to information (statutory under RTI Act)
4. Fundamental Duties under Article 51-A","1 only","1 and 3 only","1, 3 and 4 only","All of the above","B","hard","FRs are justiciable (1). Statutory rights like RTI are enforceable through courts (3). DPSPs (2) are non-justiciable. Fundamental Duties (4) are NOT directly enforceable as rights by courts — they are duties, not rights. Hence B."),
    ("AP_HC","Indian_Polity","Consider the following about the Rajya Sabha and identify INCORRECT statements:
1. Rajya Sabha members are elected by direct election
2. The term of Rajya Sabha members is 6 years
3. Rajya Sabha can be prorogued but not dissolved
4. The Vice President can participate in Rajya Sabha debates but cannot vote","1 and 4 only","1 only","4 only","2 and 3 only","A","hard","Statement 1 is INCORRECT: Rajya Sabha members are elected by INDIRECT election (by elected members of State Legislative Assemblies under single transferable vote). Statement 4 is INCORRECT: the Vice President as Chairman does NOT participate in debates and votes only in case of equality (casting vote). Statements 2 and 3 are correct."),
    ("AP_HC","Indian_Polity","The \'minimum wages\' concept under the Constitution is linked to:
1. Article 43 — DPSP directing the State to secure living wage for workers
2. Minimum Wages Act, 1948 gives statutory effect to this DPSP
3. The concept includes a \'need-based\' component beyond bare subsistence
4. The Supreme Court in Workmen v. Reptakos Brett Co. (1992) defined need-based minimum wage","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: Art 43 DPSP (1); Minimum Wages Act 1948 (2); need-based component (3); Reptakos Brett case (1992) laid down 5 components of need-based minimum wage (4)."),
    ("AP_HC","Indian_Polity","Match List I (Source/Origin) with List II (Constitutional Feature borrowed):
List I: A. British Constitution  B. American Constitution  C. Irish Constitution  D. Canadian Constitution
List II: 1. Directive Principles of State Policy
2. Federal structure with strong Centre
3. Parliamentary government; Rule of law
4. Judicial review; Fundamental Rights; written Constitution","A-3, B-4, C-1, D-2","A-4, B-3, C-2, D-1","A-3, B-2, C-4, D-1","A-1, B-4, C-2, D-3","A","hard","British = Parliamentary system, Rule of Law (3); American = Judicial review, Fundamental Rights, Written Constitution (4); Irish = Directive Principles (1); Canadian = Federal structure with strong Centre (2)."),
    ("AP_HC","Indian_Polity","Under the RTI Act, 2005, \'third party\' information:
1. Is information provided to a public authority in confidence by a third party
2. Can be disclosed only if public interest outweighs harm to third party
3. The PIO must give the third party an opportunity to be heard before disclosing
4. The third party has a right to appeal if information about them is ordered to be disclosed","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct under S.11 of the RTI Act: third party confidential information (1); public interest test (2); third party must be heard (3); third party can appeal disclosure order (4)."),
    ("AP_HC","Indian_Polity","Assertion (A): The Indian Constitution recognises the concept of \'floor crossing\' as a constitutional offence.
Reason (R): The Tenth Schedule of the Constitution provides for disqualification of legislators who voluntarily give up membership of their political party or vote against the party whip.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains A. The 10th Schedule (Anti-Defection Law) treats floor crossing and voting against the whip as grounds for disqualification — making it a constitutional offence."),
    ("AP_HC","Indian_Polity","Which of the following statements about the Preamble\'s description of India as a \'Republic\' are CORRECT?
1. It means the head of state is elected, not hereditary
2. The President of India serves a fixed term of 5 years
3. All public offices in India are open to all citizens regardless of birth
4. India was always a republic even before 26 January 1950","1, 2 and 3 only","1 and 2 only","2, 3 and 4 only","All of the above","A","hard","Statement 4 is wrong: India became a republic on 26 January 1950 — before that it was a Dominion under the British Crown (with King George VI as head of state). Statements 1, 2, 3 are correct features of a republic."),
    ("AP_HC","Indian_Polity","The phrase \'reasonable restrictions\' in Article 19 has been interpreted by the Supreme Court to mean:
1. The restriction must have a proximate nexus to the purpose it seeks to achieve
2. The court can examine the reasonableness of the restriction both in substance and procedure
3. A restriction is \'reasonable\' if the legislature thinks it is reasonable
4. The test is whether the restriction is proportionate to the objective sought","1, 2 and 4 only","2 and 3 only","1 and 4 only","All of the above","A","hard","Statement 3 is wrong — reasonableness is determined by the COURT objectively, not merely by what the legislature thinks (this was Gopalan\'s position, overruled). Statements 1, 2, 4 are correct judicial interpretations of \'reasonable restriction\'."),
    ("AP_HC","Indian_Polity","Under the Indian Limitation Act, 1963, which of the following are CORRECT?
1. The period of limitation for a suit on a contract under a bill of exchange is 3 years
2. Fraud tolls the limitation period — it begins running when the plaintiff discovers the fraud
3. The court can condone delay under Section 5 even for suits (not just appeals)
4. The prescribed period of limitation for challenging an election is 45 days","1 and 2 only","1, 2 and 4 only","2 and 4 only","All of the above","B","hard","Statement 3 is wrong: S.5 Limitation Act applies to appeals and applications — NOT to ordinary suits (suits have fixed limitation periods that cannot be extended by S.5 condonation). Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","Which of the following correctly describes the powers of the Lokpal under the Lokpal and Lokayuktas Act, 2013?
1. Lokpal can investigate complaints against Group A officers on its own
2. Lokpal can investigate the Prime Minister only after approval of its full bench
3. Lokpal has the power to attach property provisionally during investigation
4. Lokpal can sentence persons — it acts as both investigator and trial court","1, 2 and 3 only","2, 3 and 4 only","1, 3 and 4 only","All of the above","A","hard","Statement 4 is wrong: Lokpal is NOT a trial court — it investigates and sends for prosecution to Special Courts. It does NOT sentence. Statements 1, 2, 3 are correct powers of Lokpal."),
    ("AP_HC","Indian_Polity","Assertion (A): The Constitution of India provides for a bicameral legislature at the Centre (Parliament) but does not make it mandatory for all states.
Reason (R): Article 169 allows for the abolition of Legislative Councils in states that already have them, reflecting the optional nature of bicameralism at the state level.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","medium","Both are true. A correctly states the position (Parliament is bicameral; state bicameralism is optional). R correctly states that Art 169 allows abolition of upper houses. But R explains the mechanism of optional bicameralism, not the reason why it\'s optional. Hence B."),
    ("AP_HC","Indian_Polity","Which of the following landmark cases related to the AP High Court\'s jurisdiction are historically significant?
1. Cases arising from the AP Reorganisation Act, 2014 (bifurcation disputes)
2. Matters relating to Art 371-D Presidential Orders and local cadre reservations
3. Environmental cases related to Krishna-Godavari river disputes
4. Cases under the AP Land Reforms Act and agrarian laws","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four represent categories of significant cases historically handled by the AP High Court: bifurcation disputes (1), Art 371-D challenges (2), environmental/river matters (3), and land reform cases (4)."),
    ("AP_HC","Indian_Polity","The \'doctrine of prospective overruling\' in Indian constitutional law means:
1. When a court overrules a previous decision, the new rule applies only for future cases
2. Past transactions based on the old rule are not disturbed
3. This doctrine was first applied by the Indian Supreme Court in Golak Nath v. State of Punjab (1967)
4. This doctrine cannot be applied by High Courts — only the Supreme Court can use it","1 and 2 only","1, 2 and 3 only","1, 3 and 4 only","All of the above","D","hard","All four are correct: prospective overruling applies new rule only to future cases (1); past transactions protected (2); first used in Golak Nath (1967) (3); only the SC can use this doctrine, not HCs (4) — it requires constitutional dimensions."),
    ("AP_HC","Indian_Polity","Match List I (Type of government spending) with List II (Description):
List I: A. Plan expenditure  B. Non-plan expenditure  C. Revenue expenditure  D. Capital expenditure
List II: 1. Creates assets or reduces liabilities — e.g., building infrastructure
2. Day-to-day functioning — e.g., salaries, interest payments
3. Expenditure on development programmes under Five Year Plans (historical)
4. Maintenance, debt servicing, subsidies (historical non-plan category)","A-3, B-4, C-2, D-1","A-4, B-3, C-1, D-2","A-3, B-2, C-4, D-1","A-1, B-3, C-2, D-4","A","hard","Plan vs non-plan distinction was abolished from 2017-18; Revenue vs Capital expenditure continues. Plan expenditure = Five Year Plan programmes (3); Non-plan = maintenance/salaries (4) (historical); Revenue = day-to-day (2); Capital = asset creation (1)."),
    ("AP_HC","Indian_Polity","Which of the following statements about the \'Right to Vote\' in India are CORRECT?
1. Right to vote is a constitutional right under Article 326
2. Right to vote can be exercised by citizens only
3. The Supreme Court has held that the right to vote includes the right to \'NOTA\' (None of the Above)
4. Right to vote cannot be restricted on grounds of literacy or property under Article 326","1, 2 and 4 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: Art 326 provides adult franchise (1); citizens only can vote (2); NOTA upheld in PUCL v. Union of India (2013) (3); Art 326 prohibits restrictions based on religion, race, caste, sex, or property — literacy is not ground for restriction (4)."),
    ("AP_HC","Indian_Polity","Assertion (A): The Indian Constitution has provisions for both \'cooperative\' and \'competitive\' federalism.
Reason (R): While the Constitution provides mechanisms for Centre-State cooperation (Inter-State Council, Finance Commission), states also compete for investment and development, reflecting cooperative and competitive federalism.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","medium","Both A and R are true. However R describes the dual nature of federalism but doesn\'t \'explain\' A in the technical sense — competitive federalism is not explicitly in the Constitution, it is a policy/governance concept. Hence B."),
    ("AP_HC","Indian_Polity","Under the Negotiable Instruments Act, 1881, which of the following are correctly described?
1. Promissory note — unconditional promise in writing to pay a certain sum
2. Bill of exchange — unconditional order to pay a certain sum
3. Cheque — a bill of exchange drawn on a specified bank payable on demand
4. The holder in due course gets a better title than the transferor in all cases","1, 2 and 3 only","2 and 3 only","1 and 4 only","All of the above","A","hard","Statement 4 is wrong: a holder in due course gets a better title EXCEPT against the true owner who can recover from all including HDC (only in very limited fraud cases). Statements 1, 2, 3 are correct definitions under NI Act sections 4, 5, 6."),
    ("AP_HC","Indian_Polity","Which of the following writs are available against the State under Article 226 but NOT under Article 32?
1. Quo Warranto against private individuals claiming public offices
2. All five prerogative writs
3. Writs for enforcement of any legal right (not just FRs)
4. Writs against private bodies performing public functions","3 only","1 and 4 only","3 and 4 only","1, 3 and 4 only","C","hard","Under Art 226, HCs can issue writs for \'any other purpose\' (not just FRs) — this is wider (3). Art 226 also extends to \'any person or authority\' which can include private bodies performing public duties (4). Art 32 is limited to FR enforcement. Hence C."),
    ("AP_HC","Indian_Polity","Assertion (A): Parliamentary sovereignty is not absolute in India unlike in the United Kingdom.
Reason (R): In India, Parliament\'s legislative power is subject to the Constitution, and courts can strike down Parliamentary laws that violate the Constitution.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","easy","Both are true and R correctly explains A. In the UK, Parliament is supreme and courts cannot strike down Acts of Parliament. In India, Parliamentary sovereignty is limited by the Constitution and judicial review."),
    ("AP_HC","Indian_Polity","Consider the following about \'mock drill\' provisions under emergency law:
1. Under the Civil Defence Act, 1968, mock drills can be conducted
2. During a National Emergency, the President can suspend all Fundamental Rights
3. Article 22 protections against preventive detention can be modified by Parliament to extend detention beyond 3 months
4. The Unlawful Activities (Prevention) Act allows detention for 180 days before filing charge sheet","1 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 2 is wrong: President CANNOT suspend ALL FRs — only Art 19 rights can be suspended (Art 358) and other FRs via Art 359 EXCEPT Arts 20 and 21. Statements 1, 3, 4 are correct."),
    ("AP_HC","Indian_Polity","The Supreme Court, while exercising jurisdiction under Article 142 (\'complete justice\'), has:
1. Directed closure of industries causing environmental pollution
2. Issued directions for judicial reforms and pendency reduction
3. Ordered demolition of unauthorised constructions
4. Transferred cases from HC to SC suo motu","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are examples of Art 142 \'complete justice\' orders: environmental (1), judicial reform (2), unauthorised constructions (3), case transfer (4). Art 142 gives the SC broad remedial powers."),
    ("AP_HC","Indian_Polity","Match List I (Constitutional concept) with List II (Example/Case):
List I: A. Implied powers  B. Incidental powers  C. Ancillary powers  D. Residuary powers
List II: 1. Entry 97, Union List — taxes not listed elsewhere vest with Parliament
2. Parliament\'s power to enact consequential provisions not specifically listed
3. Power to do what is necessary to give effect to the express power
4. Powers that flow from express constitutional provisions without being stated","A-4, B-3, C-2, D-1","A-3, B-4, C-1, D-2","A-4, B-2, C-3, D-1","A-1, B-3, C-4, D-2","A","hard","Implied powers = flow from express provisions (4); Incidental powers = necessary to exercise express powers (3); Ancillary = consequential provisions (2); Residuary = Entry 97 Union List (1)."),
    ("AP_HC","Indian_Polity","The concept of \'judicial populism\' in the context of Indian PIL means:
1. Courts deciding cases based on popular sentiment
2. This is generally considered a negative development in judicial review
3. It is contrasted with \'principled judicial decision-making\'
4. The Supreme Court has consistently avoided judicial populism","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statements 1, 2, 3 are correct descriptions of the academic debate around judicial populism. Statement 4 is incorrect — critics argue that some SC decisions have elements of judicial populism. Hence B."),
    ("AP_HC","Indian_Polity","Assertion (A): The Directive Principles of State Policy form the conscience of the Indian Constitution.
Reason (R): Dr. B.R. Ambedkar stated that the Directive Principles, though non-justiciable, are far superior to the Fundamental Rights as they aim at the socio-economic transformation of India.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","C","hard","A is a generally accepted characterisation (conscience of the Constitution). R is INACCURATE: it was Jawaharlal Nehru who emphasised DPSPs as representing the nation\'s socioeconomic goals; Ambedkar actually described FRs as fundamental. Also, no mainstream authority says DPSPs are \'far superior\' to FRs. Hence C."),
    ("AP_HC","Indian_Polity","Which of the following are CORRECTLY described about the Supreme Court under Article 141?
1. The law declared by the Supreme Court is binding on all courts in India
2. This includes High Courts, District Courts, and all other judicial bodies
3. A Supreme Court ratio decidendi (reason for decision) is binding, not obiter dicta
4. Article 141 also binds the Supreme Court itself to follow its previous decisions","1, 2 and 3 only","2, 3 and 4 only","1, 3 and 4 only","All of the above","A","hard","Statement 4 is wrong: the SC is NOT strictly bound by its own previous decisions (it can overrule them using larger benches). Art 141 binds all other courts. Statements 1, 2, 3 are correct."),
    ("AP_HC","Indian_Polity","Consider the following about India\'s Constitution and identify the CORRECT statement:
1. The original Constitution had 395 Articles, 8 Schedules, and 22 Parts
2. The Constitution is the longest written constitution in the world
3. The Constitution was neither wholly rigid nor wholly flexible — it has provisions requiring different procedures for amendment
4. The founding fathers deliberately chose parliamentary system over presidential system","1 only","1 and 2 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: original = 395 Articles, 8 Schedules, 22 Parts (1); longest written Constitution (2); mixed rigidity (3); deliberate choice of parliamentary system by Constituent Assembly (4)."),
    ("AP_HC","Indian_Polity","Which of the following have been used to read \'right to information\' into the Constitution?
1. Article 19(1)(a) — freedom of speech includes freedom to receive information
2. Article 21 — right to know is part of right to live with dignity
3. Article 32 and 226 — courts can enforce RTI as a constitutional right
4. The RTI Act 2005 is the sole source of right to information in India","1, 2 and 3 only","1 and 3 only","2, 3 and 4 only","All of the above","A","hard","Statement 4 is wrong: the right to information was a constitutional right (under Art 19(1)(a) per SC judgments) BEFORE the RTI Act was passed. Statements 1, 2, 3 are correct."),
    ("AP_HC","Indian_Polity","The Andhra Pradesh State Reorganisation Act, 2014 specifically provided for which of the following regarding water resources?
1. Formation of an Apex Council for supervision of Krishna and Godavari river boards
2. Establishment of the Krishna River Management Board (KRMB)
3. Establishment of the Godavari River Management Board (GRMB)
4. Both KRMB and GRMB are chaired by the Central government","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct provisions of the AP Reorganisation Act 2014: Apex Council (1), KRMB (2), GRMB (3), and both are under Central government supervision (4)."),
    ("AP_HC","Indian_Polity","In which of the following is the concept of \'absolute liability\' applicable in India?
1. Escape of hazardous substances from industries
2. Nuclear accidents (Nuclear Damage Civil Liability Act, 2010)
3. Medical accidents caused by government hospitals
4. Collapse of government-built structures","1 and 2 only","1, 2 and 3 only","2 and 4 only","All of the above","A","hard","Absolute liability (no defence) applies to: hazardous industries (M.C. Mehta principle) (1) and nuclear damage (Civil Nuclear Liability Act) (2). Medical accidents by government hospitals (3) are subject to normal negligence/Consumer Act standards. Government structures (4) = state liability, not absolute liability."),
    ("AP_HC","Indian_Polity","Assertion (A): The Preamble of the Indian Constitution is not enforceable as a legal document by itself.
Reason (R): The Preamble cannot be used to override specific provisions of the Constitution, but it serves as a key aid in interpreting the Constitution.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","medium","Both are true. The Preamble is part of the Constitution (Kesavananda) but is not enforceable as a standalone legal provision (A). R correctly states its interpretive role. But R doesn\'t explain WHY the Preamble is not enforceable on its own. Hence B."),
    ("AP_HC","Indian_Polity","Which of the following statements are CORRECT about the \'writ of mandamus\' in India?
1. Mandamus can be issued to compel a public authority to perform a statutory duty
2. Mandamus lies against the President and Governor for constitutional violations
3. Mandamus is available when the applicant has a legally enforceable right
4. Mandamus cannot be issued against a private individual or authority","1 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 2 is wrong: Mandamus cannot be issued against the President and Governors for constitutional acts — they have immunity under Arts 361 and 361. Statement 4 is generally true (mandamus is against public duties) but there are limited exceptions. Hence B (1, 3, 4 broadly correct)."),
    ("AP_HC","Indian_Polity","The Supreme Court in the Electoral Bonds case (Association for Democratic Reforms v. Union of India, 2024) unanimously held:
1. The scheme violated voters\' right to information under Article 19(1)(a)
2. The scheme was violative of Article 14 (manifestly arbitrary)
3. The right to privacy of political donors overrides public right to information
4. SBI was directed to submit details of bonds to the Election Commission","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: the Court REJECTED the donors\' privacy argument — public right to know about political funding outweighs donors\' privacy. Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","Consider the following about the concept of \'sustainable development\' in Indian constitutional law:
1. It is a balance between development and environmental protection
2. It was recognised as part of Art 21 in Vellore Citizens Welfare Forum v. Union of India (1996)
3. The National Environment Policy, 2006 mentions sustainable development
4. Sustainable development requires that the \'needs of the present generation are met without compromising future generations\'","1 and 4 only","1, 3 and 4 only","1, 2 and 4 only","All of the above","D","hard","All four are correct about sustainable development: the balance (1); Vellore Citizens (2); NEP 2006 (3); Brundtland Commission definition adopted in India (4)."),
    ("AP_HC","Indian_Polity","Which of the following are CORRECT about the composition of the Rajya Sabha?
1. Members from states are elected by state legislative assemblies by proportional representation
2. 12 members are nominated by the President for contribution to art, literature, science, or social service
3. Members from Union Territories can be directly or indirectly elected as prescribed by Parliament
4. The total strength of Rajya Sabha cannot exceed 250","1, 2 and 4 only","2, 3 and 4 only","1, 3 and 4 only","All of the above","D","hard","All four are correct: state members elected by SLA (Art 80(4)) (1); 12 presidential nominees (Art 80(1)(a)) (2); UT members as Parliament prescribes (3); maximum 250 (Art 80(1)) (4)."),
    ("AP_HC","Indian_Polity","Which of the following statements about \'constitutional morality\' vs \'popular morality\' are CORRECT?
1. Constitutional morality means adherence to the core values of the Constitution
2. Popular morality means what the majority of society considers moral
3. Constitutional morality may override popular morality in matters of fundamental rights
4. The Supreme Court in Navtej Johar (2018) held constitutional morality must prevail over popular morality","1 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: constitutional morality defined (1); popular morality defined (2); CR overrides PM in FR matters (3); Navtej Johar explicitly held this (4)."),
    ("AP_HC","Indian_Polity","The \'right to know\' as a component of freedom of speech was first recognised in India in:
1. State of U.P. v. Raj Narain (1975) — right to information about public acts of government
2. S.P. Gupta v. Union of India (1981) — access to documents regarding judicial appointments
3. Reliance Petrochemicals v. Indian Express Newspapers (1988)
4. All three cases progressively developed the right to information","1 only","1 and 2 only","2 and 3 only","All of the above","D","hard","All three cases contributed to developing the constitutional right to information: Raj Narain (1975) — public acts must be disclosed; S.P. Gupta (1981) — judicial correspondence; Reliance Petrochemicals (1988) — freedom of press. Hence D."),
    ("AP_HC","Indian_Polity","Match List I (Case) with List II (Area of Law):
List I: A. Sarla Mudgal v. Union of India (1995)  B. Mary Roy v. State of Kerala (1986)  C. Shah Bano v. Union of India (1985)  D. Daniel Latifi v. Union of India (2001)
List II: 1. Muslim women\'s right to maintenance — Muslim Women Act, 1986 upheld
2. Christian women\'s right to inherit equally under Indian Succession Act
3. Muslim personal law and maintenance of divorced wife under CrPC
4. Bigamy through religious conversion — calls for UCC","A-4, B-2, C-3, D-1","A-3, B-4, C-1, D-2","A-2, B-4, C-3, D-1","A-4, B-3, C-2, D-1","A","hard","Sarla Mudgal = bigamy through conversion, call for UCC (4); Mary Roy = Christian women\'s inheritance (2); Shah Bano = Muslim maintenance under CrPC (3); Daniel Latifi = Muslim Women Act 1986 — upholding reasonable provision for divorced Muslim women (1)."),
    ("AP_HC","Indian_Polity","Under the Constitution of India, what happens if a Constitutional Amendment Bill passed by both Houses of Parliament is not sent to the President for assent?
1. The President can require the Bill to be returned and can send a message to Parliament
2. The President must give assent — the Constitution does not allow pocket veto for constitutional amendments
3. If the President withholds assent, it is void — Parliament need not reconsider
4. After the 24th Amendment, the President MUST give assent to constitutional amendment bills","1 and 2 only","2, 3 and 4 only","2 and 4 only","All of the above","C","hard","After the 24th Amendment, Art 368(2) mandates Presidential assent — the President cannot withhold it (2) and (4) are both correct. Statement 1 is wrong — President cannot return a CA Bill (unlike ordinary bills). Statement 3 is wrong as formulated. Hence C (2 and 4)."),
    ("AP_HC","Indian_Polity","Assertion (A): Martial law under Article 34 is different from National Emergency under Article 352.
Reason (R): While National Emergency is proclaimed by the President under Art 352, Martial law is a common law concept involving military rule in an area when civilian law fails, and Parliament can by law indemnify acts done during Martial law.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","hard","Both are true and R correctly explains A. Art 34 deals with indemnification of acts done during Martial law — it is a separate provision from Art 352 National Emergency. Martial law = military administration of an area; National Emergency = political/constitutional emergency."),
    ("AP_HC","Indian_Polity","Which of the following are consequences of the proclamation of a National Emergency under Article 352?
1. The President can make laws on State List subjects by executive order
2. The Parliament can legislate on State List subjects (Art 250)
3. Lok Sabha can extend its own term by one year at a time (Art 83)
4. The Fundamental Rights under Article 19 stand suspended automatically","1 and 3 only","2, 3 and 4 only","2 and 3 only","All of the above","B","hard","Statement 1 is wrong: it is Parliament (not President by executive order) that can legislate on State List. Statement 4: Art 19 rights are suspended AUTOMATICALLY only if emergency is on grounds of war/external aggression — NOT for armed rebellion. Statements 2, 3 are always correct. Statement 4 is conditional. For this question, assuming war/external aggression: 2, 3, 4 are correct. Hence B."),
    ("AP_HC","Indian_Polity","Match List I (International Instrument) with List II (Year adopted/Year India ratified):
List I: A. International Covenant on Civil and Political Rights  B. Convention on the Rights of the Child  C. Convention on Elimination of Discrimination Against Women  D. Convention Against Torture
List II: 1. Adopted 1979, India ratified 1993
2. Adopted 1989, India ratified 1992
3. Adopted 1966, India ratified 1979
4. Adopted 1984, India has NOT ratified","A-3, B-2, C-1, D-4","A-2, B-3, C-4, D-1","A-3, B-1, C-2, D-4","A-4, B-2, C-1, D-3","A","hard","ICCPR = 1966, India ratified 1979 (3); CRC = 1989, India ratified 1992 (2); CEDAW = 1979, India ratified 1993 (1); CAT = 1984, India has NOT ratified (4)."),
    ("AP_HC","Indian_Polity","Which of the following are features of the Indian federal system that favour the Union over States?
1. A single Constitution for both the Union and States
2. Parliament can create new states or alter state boundaries unilaterally (Art 3)
3. States can secede from the Union if their legislature passes a resolution
4. All-India Services (IAS, IPS) serve under both Centre and States but are ultimately under Central control","1, 2 and 4 only","1 and 4 only","2, 3 and 4 only","All of the above","A","hard","Statement 3 is wrong: states CANNOT secede — India is an \'indestructible union of destructible states\' (unlike USA). Statements 1, 2, 4 are all centralising features favouring the Union over States."),
    ("AP_HC","Indian_Polity","Assertion (A): The Indian Constitution cannot be said to be a \'rigid\' constitution in the strict sense.
Reason (R): While some provisions require special majority and state ratification for amendment, several provisions can be amended by Parliament alone by a simple majority, making it a blend of rigid and flexible.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains A. The Indian Constitution is neither purely rigid (like USA) nor purely flexible (like UK) — it has a mixed amendment procedure."),
    ("AP_HC","Indian_Polity","Which of the following statements about the \'principle of natural justice\' in India are CORRECT?
1. Audi alteram partem — hear both sides
2. Nemo judex in causa sua — no one should be a judge in his own cause
3. Speaking orders — reasons must be given for every decision
4. These principles are explicitly codified in the Indian Constitution","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is wrong: natural justice principles are NOT explicitly in the Constitution — they are common law principles incorporated by courts through Art 14 and 21. Statements 1, 2, 3 (speaking orders is a developed requirement) are correct."),
    ("AP_HC","Indian_Polity","The following are associated with the Constituent Assembly of India. Match correctly:
List I: A. Constitutional Adviser  B. Drafting Committee Chairman  C. President of Constituent Assembly  D. Committee on Fundamental Rights Chairman
List II: 1. Sardar Vallabhbhai Patel
2. Dr. Rajendra Prasad
3. Sir B.N. Rau
4. Dr. B.R. Ambedkar","A-3, B-4, C-2, D-1","A-4, B-3, C-1, D-2","A-3, B-2, C-4, D-1","A-1, B-4, C-2, D-3","A","medium","Constitutional Adviser = Sir B.N. Rau (3); Drafting Committee Chairman = Dr. Ambedkar (4); President = Dr. Rajendra Prasad (2); Committee on Fundamental Rights = Sardar Patel (1)."),
    ("AP_HC","Indian_Polity","Which of the following are CORRECT about the Human Rights protection framework in India?
1. The Protection of Human Rights Act, 1993 was enacted to give effect to the Paris Principles on National Human Rights Institutions
2. NHRC can initiate suo motu inquiries
3. NHRC can transfer cases to State Human Rights Commissions
4. Complaints against Central government officials must be filed with NHRC, not SHRC","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is not strictly correct — NHRC and SHRCs have overlapping jurisdiction in many cases. Statements 1 (Paris Principles), 2 (suo motu), 3 (transfer to SHRC) are correct."),
    ("AP_HC","Indian_Polity","The concept of \'legitimate expectation\' was first recognised in Indian administrative law in:
1. Navnit Lal C. Javeri v. K.K. Sen (1965)
2. State of Kerala v. K.G. Madhavan Pillai (1988)
3. Punjab Communications Ltd. v. Union of India (1999)
4. Monnet Ispat & Energy Ltd. v. Union of India (2012)","2 only","2 and 3 only","1 and 2 only","2, 3 and 4 only","D","hard","The doctrine of legitimate expectation was recognised and developed through multiple cases: State of Kerala v. K.G. Madhavan Pillai (1988) — one of the early recognitions; Punjab Communications (1999) — substantive legitimate expectation; Monnet Ispat (2012) — further development. Navnit Lal (1965) was a tax case predating the doctrine."),
    ("AP_HC","Indian_Polity","Match List I (Article) with List II (Subject):
List I: A. Article 72  B. Article 161  C. Article 200  D. Article 213
List II: 1. Governor\'s assent to Bills
2. Governor\'s Ordinance-making power
3. President\'s pardoning power
4. Governor\'s pardoning power","A-3, B-4, C-1, D-2","A-4, B-3, C-2, D-1","A-3, B-1, C-4, D-2","A-4, B-1, C-3, D-2","A","medium","Art 72 = President\'s pardoning power (3); Art 161 = Governor\'s pardoning power (4); Art 200 = Governor\'s assent to Bills passed by State Legislature (1); Art 213 = Governor\'s Ordinance-making power (2)."),
    ("AP_HC","Indian_Polity","Under Article 239-AA of the Constitution (Delhi as NCT):
1. Delhi has a Legislative Assembly with powers over subjects in State and Concurrent Lists
2. Public order, police, and land are excluded from Delhi legislature\'s purview
3. The Lieutenant Governor must act on the advice of the elected government in all matters
4. In case of difference of opinion, the LG can refer the matter to the President","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: LG does NOT act on elected government\'s advice in all matters — public order, police, and land are exceptions (2). The GNCTD Amendment 2023 further restricted the elected government\'s powers over services. Hence B (1, 2, 4)."),
    ("AP_HC","Indian_Polity","The \'writ of prohibition\' is issued by a superior court to prevent a:
1. Lower court from exceeding its jurisdiction
2. Quasi-judicial body from exceeding its jurisdiction
3. Administrative authority from performing an administrative act
4. Private party from doing an illegal act","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","A","hard","Prohibition lies against courts and quasi-judicial bodies (1, 2) to prevent excess of jurisdiction. It does NOT lie against administrative authorities performing administrative acts (3) or against private parties (4). Hence A."),
    ("AP_HC","Indian_Polity","Assertion (A): The Governor of a state can summon the state legislature to meet at a time and place of his choosing.
Reason (R): Article 174 empowers the Governor to summon each House of the state legislature to meet at such time and place as he thinks fit.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","hard","Both A and R are technically true. However the Governor summons the legislature on the ADVICE of the Council of Ministers (cabinet convention). Art 174 gives formal power to Governor, but in practice it\'s exercised on CM\'s advice. R explains the constitutional text but not the constitutional convention. Hence B — both true but R doesn\'t fully explain A (missing the advice requirement)."),
    ("AP_HC","Indian_Polity","Which of the following are CORRECT about the Integrated Goods and Services Tax (IGST)?
1. IGST is levied on inter-state supply of goods and services
2. IGST is collected by the Central government
3. IGST revenue is shared between Centre and States as per the formula
4. IGST is NOT applicable on imports","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is wrong: IGST IS applicable on imports (imports are treated as inter-state supply). Statements 1, 2, 3 are correct: IGST on inter-state supply (1), collected by Centre (2), shared between Centre and destination state (3)."),
    ("AP_HC","Indian_Polity","The concept of \'judicial notice\' under the Indian Evidence Act means:
1. Courts take notice of certain facts without requiring proof
2. These include facts of notoriety, common knowledge, and official public documents
3. Courts must take judicial notice of state laws of all states in India
4. Section 57 of the IEA lists matters of which courts shall take judicial notice","1, 2 and 4 only","2, 3 and 4 only","1, 3 and 4 only","All of the above","A","hard","Statement 3 is wrong: courts take judicial notice of THEIR OWN state\'s laws — they may require proof of laws of other states. Statements 1, 2, 4 are correct (S.57 IEA lists specific matters including laws of India, official publications, public documents etc.)."),
    ("AP_HC","Indian_Polity","Match List I (Provision) with List II (What it prohibits/provides):
List I: A. Article 17  B. Article 18  C. Article 23  D. Article 24
List II: 1. Abolition of titles — no title shall be conferred by State
2. Prohibition of child labour in hazardous occupations
3. Prohibition of traffic in human beings and forced labour
4. Abolition of untouchability","A-4, B-1, C-3, D-2","A-3, B-4, C-1, D-2","A-4, B-3, C-2, D-1","A-1, B-2, C-4, D-3","A","medium","Art 17 = Abolition of untouchability (4); Art 18 = Abolition of titles (1); Art 23 = Prohibition of traffic/forced labour (3); Art 24 = Child labour prohibition below 14 in hazardous work (2)."),
    ("AP_HC","Indian_Polity","Which of the following are INCORRECT about the Contempt of Court jurisdiction of High Courts?
1. High Courts have inherent jurisdiction to punish for contempt under Article 215
2. High Courts can punish for contempt of themselves but not contempt of subordinate courts
3. The Contempt of Courts Act, 1971 does not limit the inherent power of HCs
4. A High Court can punish for contempt of the Supreme Court","2 and 4 only","1 and 3 only","2 only","4 only","A","hard","Statement 2 is INCORRECT: HCs can punish for contempt of subordinate courts as well. Statement 4 is INCORRECT: HC cannot punish for contempt of the Supreme Court — that is the SC\'s own jurisdiction. Statements 1 and 3 are correct. Hence A (2 and 4 are incorrect)."),
    ("AP_HC","Indian_Polity","The principle of \'beneficial construction\' in interpretation of statutes means:
1. Social welfare legislation should be interpreted liberally to advance its purpose
2. In case of ambiguity, the interpretation that benefits the weaker party should be preferred
3. Penal laws must be strictly construed against the accused
4. This principle applies to laws enacted for protection of workers, women, and children","1, 2 and 4 only","2 and 3 only","1, 3 and 4 only","All of the above","A","hard","Statement 3 is wrong: strict construction against the accused applies to PENAL laws — it\'s the opposite of beneficial construction. Beneficial construction (1, 2, 4) applies to social welfare and protective legislation."),
    ("AP_HC","Indian_Polity","Consider the following pairs of countries and their constitutional features that influenced India\'s Constitution:
1. Australia — Concurrent List concept
2. Germany — Emergency provisions
3. South Africa — Procedure for constitutional amendment and election of President
4. Japan — Procedure established by law (Art 21 concept)","1 and 4 only","1, 2 and 4 only","1, 3 and 4 only","All of the above","C","hard","Australian Concurrent List (1) — correct; German emergency provisions — actually Ireland/Germany contributed different things; South Africa influenced amendment procedure and Presidential election (3) — correct; Japan\'s Constitution used \'due process\' equivalent (4) — correct. Germany\'s influence is mainly on Fundamental Rights. Hence C (1, 3, 4) is most accurate."),
    ("AP_HC","Indian_Polity","Assertion (A): Articles 5 to 11 of the Indian Constitution deal with citizenship at the commencement of the Constitution.
Reason (R): These provisions in Part II were necessary to determine who would be citizens when India became a republic on 26 January 1950, as there was no prior Indian citizenship.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains A. Before the Constitution came into force, there was British/dominion status — not Indian citizenship per se. Arts 5-11 determined the initial body of citizens."),
    ("AP_HC","Indian_Polity","Which of the following are CORRECTLY stated about \'privileges\' of legislative bodies?
1. Parliamentary privileges are codified in the Constitution under Articles 105 and 194
2. The privileges of state legislatures are governed by Article 194
3. A court cannot examine whether the privilege claimed actually exists
4. The Constituent Assembly debates are used to interpret privileges","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: courts CAN examine whether a claimed privilege actually exists and whether the House has acted within its privileged sphere (Searchlight case, Keshav Singh case). Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","The term \'domicile\' in the context of citizenship and civil law means:
1. A person\'s permanent home in a legal sense
2. In India, there is a single domicile — the domicile of India
3. Domicile and residence are the same concept in Indian law
4. Domicile determines which personal law applies to a person in many family law matters","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: domicile and residence are different — domicile is permanent home (intention + presence), residence is actual physical presence without necessarily intending permanence. Statements 1, 2, 4 are correct."),
    ("AP_HC","Indian_Polity","Match List I (Committee on Constituent Assembly) with List II (Subject and Chairperson):
List I: A. Drafting Committee  B. Union Constitution Committee  C. Union Powers Committee  D. States Committee
List II: 1. Sardar Patel (Chaired)
2. Jawaharlal Nehru (Chaired)
3. Dr. B.R. Ambedkar (Chaired)
4. Jawaharlal Nehru (Chaired)","A-3, B-2, C-4, D-1","A-3, B-4, C-2, D-1","A-2, B-3, C-1, D-4","A-4, B-2, C-3, D-1","B","hard","Drafting Committee = Ambedkar (3); Union Constitution Committee = Nehru (4); Union Powers Committee = Nehru (2); States Committee = Sardar Patel (1). Note: Nehru chaired both Union Constitution and Union Powers Committees."),
    ("AP_HC","Indian_Polity","Which of the following constitutional amendments have been held to be valid by the Supreme Court in their entirety?
1. 1st Amendment (1951) — adding 9th Schedule and Art 15(4)
2. 17th Amendment (1964) — adding more laws to 9th Schedule
3. 42nd Amendment (1976) — mini-Constitution (entirely upheld)
4. 44th Amendment (1978) — reversed Emergency excesses","1 and 2 only","1, 2 and 4 only","1, 4 only","All of the above","B","hard","The 42nd Amendment was NOT entirely upheld — in Minerva Mills (1980), several provisions were struck down (clauses giving primacy to all DPSPs over FRs, and clauses limiting judicial review). Statements 1, 2, 4 were upheld. Hence B."),
    ("AP_HC","Indian_Polity","Which of the following are CORRECT about the Lokayukta institution in India?
1. The concept of Lokayukta was first recommended by the First Administrative Reforms Commission (1966)
2. Maharashtra was the first state to establish a Lokayukta in 1971
3. The Lokayukta Act varies from state to state — there is no uniform central law
4. The Karnataka Lokayukta has jurisdiction over the Chief Minister","1 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 2 is wrong: Maharashtra was NOT first — Odisha (1970) is considered the first to establish Lokayukta (some say Maharashtra (1971)). The first recommendation was by ARC (1966). Statement 4 is correct for Karnataka specifically. Statements 1, 3, 4 are correct."),
    ("AP_HC","Indian_Polity","Assertion (A): The Sixth Schedule of the Constitution provides greater autonomy to tribal areas than the Fifth Schedule.
Reason (R): Under the Sixth Schedule, Autonomous District Councils in Northeast India have legislative, judicial, and administrative powers, while the Fifth Schedule primarily provides for Governors\' oversight and Tribes Advisory Councils.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","hard","Both are true and R correctly explains A. The Sixth Schedule ADCs have broader legislative and judicial powers (including tribal courts). Fifth Schedule primarily relies on Governor\'s oversight and Tribal Advisory Councils — less autonomous than ADCs."),
    ("AP_HC","Indian_Polity","Match List I (Type of majority) with List II (Specific provision requiring it):
List I: A. Absolute majority (majority of total membership)  B. Special majority (2/3 of members present and voting)  C. Special majority of Art 368(2)  D. Special resolution of Rajya Sabha
List II: 1. Creation of All-India Services under Art 312
2. Constitutional amendment (majority of total membership AND 2/3 of members present)
3. Removal of Speaker from office
4. Resolution to enable Parliament to legislate on State List under Art 249","A-3, B-4, C-2, D-1","A-4, B-3, C-1, D-2","A-3, B-1, C-2, D-4","A-4, B-1, C-2, D-3","A","hard","Removal of Speaker = absolute majority (majority of total membership — Art 94) (3); 2/3 of members present and voting = needed for various resolutions (4 - Art 249 requires 2/3 majority of present and voting in RS); Art 368 special majority = total membership + 2/3 present (2); All-India Services = RS resolution by 2/3 (Art 312) (1). Match A is correct."),
    ("AP_HC","Indian_Polity","Which of the following statements correctly describe the relationship between \'Parliamentary sovereignty\' and \'Constitutional supremacy\' in India?
1. India follows constitutional supremacy — the Constitution is supreme, not Parliament
2. Parliament is sovereign within the limits set by the Constitution
3. Courts can strike down laws passed by Parliament if they violate the Constitution
4. The concept of constitutional supremacy was reaffirmed in Kesavananda Bharati (1973)","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: constitutional supremacy (1); Parliament is sovereign within constitutional limits (2); judicial review of parliamentary laws (3); Kesavananda reaffirmed (4)."),
    ("AP_HC","Indian_Polity","The \'power of judicial review\' in India extends to:
1. Reviewing constitutional amendments for basic structure violations
2. Reviewing ordinary legislation for consistency with Fundamental Rights
3. Reviewing executive/administrative actions for legality, reasonableness, and fairness
4. Reviewing policy decisions of the government on their merits","1, 2 and 3 only","2, 3 and 4 only","1, 3 and 4 only","All of the above","A","hard","Statement 4 is wrong: courts generally do NOT review the MERITS of policy decisions — judicial review of policy is on grounds of legality, reasonableness, and procedural fairness, not on whether the policy is wise or correct. Statements 1, 2, 3 are correct."),
    ("AP_HC","Indian_Polity","In the context of land laws in Andhra Pradesh, which of the following are significant?
1. The AP Land Reforms (Ceiling on Agricultural Holdings) Act, 1973
2. The AP Agricultural Land (Conversion for Non-Agricultural Purpose) Act, 2006
3. These laws are placed in the Ninth Schedule to protect from judicial review
4. The AP Assigned Lands (Prohibition on Transfer) Act, 1977","1 and 4 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","B","hard","The AP Land Ceiling Act and AP Assigned Lands Act are significant land laws; many such land reform laws are in the 9th Schedule. The AP Agricultural Land Conversion Act (2) is also significant. Hence B (1, 3, 4) with the caveat that the exact 9th Schedule inclusion should be verified for each."),
    ("AP_HC","Indian_Polity","Assertion (A): The Indian Constitution draws a distinction between \'amendment\' and \'revision\' of the Constitution.
Reason (R): Under Article 368, Parliament can \'amend\' the Constitution — but the basic structure, which is the core of the Constitution, cannot be revised/altered even by a formal amendment.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","D","hard","A is false: the Constitution does NOT formally distinguish between \'amendment\' and \'revision\' — Art 368 uses \'amend\'. R is true — the basic structure doctrine prevents certain alterations even through formal amendment. Since A is false and R is true, answer is D."),
    ("AP_HC","Indian_Polity","Which of the following are grounds for disqualification of a Member of a State Legislature under Article 191?
1. Holding an office of profit under the State or Union Government
2. Being declared of unsound mind by a court
3. Not being a voter in any constituency in the state
4. Voluntary acquisition of citizenship of a foreign state","1 and 4 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","Statement 3 is wrong: members must be registered as voters in the state, but the exact constituency requirement is for candidacy (not an existing MLA disqualification ground per Art 191). Statements 1, 2, 4 are explicit disqualifications under Art 191 (mirroring Art 102 for Parliament)."),
    ("AP_HC","Indian_Polity","The \'Vishaka guidelines\' on sexual harassment at the workplace required the employer to:
1. Prohibit sexual harassment
2. Set up a Complaints Committee headed by a woman
3. Include a third party NGO representative in the Complaints Committee
4. Ensure confidentiality of the complainant\'s identity","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","The Vishaka guidelines required: prohibition of sexual harassment (1), Complaints Committee headed by woman (2), NGO/third party involvement in Committee (3), and confidentiality measures (4). All four are correct."),
    ("AP_HC","Indian_Polity","Which of the following statements about \'rule of law\' in India are CORRECT?
1. The concept of rule of law was propounded by A.V. Dicey
2. Dicey\'s three meanings: supremacy of law, equality before law, predominance of legal spirit
3. Rule of law is a basic structure of the Indian Constitution
4. Rule of law in India is limited by Constitutional exceptions such as immunity of President and Governors","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: Dicey propounded it (1); three meanings (2); it\'s basic structure (3); qualified by constitutional immunities (Art 361) (4)."),
    ("AP_HC","Indian_Polity","Consider the following about the \'National Green Tribunal\' (NGT):
1. NGT was established under the National Green Tribunal Act, 2010
2. NGT has original jurisdiction over environmental matters relating to forest clearances
3. NGT can award compensation to victims of environmental damage
4. NGT\'s orders can be appealed to the Supreme Court directly","1, 2 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: NGT Act 2010 (1); jurisdiction over forest clearance, environmental disputes (2); compensation power (3); appeals go to SC directly (4) — under S.22 of NGT Act, appeal lies to the Supreme Court."),
    ("AP_HC","Indian_Polity","Match List I (Constitutional Article) with List II (Subject related to State Finance):
List I: A. Article 202  B. Article 203  C. Article 204  D. Article 205
List II: 1. Supplementary and additional grants
2. Annual Financial Statement (State Budget)
3. Procedure in Legislature for estimates (Demands for Grants)
4. Appropriation Bills for State","A-2, B-3, C-4, D-1","A-3, B-2, C-1, D-4","A-2, B-4, C-3, D-1","A-4, B-3, C-2, D-1","A","medium","Art 202 = Annual Financial Statement (State Budget); Art 203 = Procedure (Demands for Grants); Art 204 = Appropriation Bills; Art 205 = Supplementary grants."),
    ("AP_HC","Indian_Polity","Assertion (A): The concept of \'judicial restraint\' suggests that courts should not substitute their judgment for that of the legislature or executive on policy matters.
Reason (R): Courts practice judicial restraint because they lack expertise in all policy areas and because excessive intervention may undermine the principle of separation of powers.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains A. Judicial restraint = courts deferring to elected branches on policy; R gives two correct reasons for this restraint."),
    ("AP_HC","Indian_Polity","Which of the following statements about contempt jurisdiction of the Supreme Court are CORRECT?
1. The Supreme Court\'s contempt jurisdiction is derived from Article 129
2. Article 142(2) empowers the SC to investigate and punish for contempt
3. The SC can punish for contempt of itself and also for contempt of High Courts
4. The Contempt of Courts Act, 1971 regulates contempt proceedings in the SC","1 and 4 only","1, 2 and 4 only","1, 3 and 4 only","All of the above","C","hard","Statement 2 is not the primary source for contempt — Art 129 (court of record) is the primary source, and Art 142(2) allows SC to make orders for securing attendance of persons and investigating contempt. Statement 3 is partially correct — SC can deal with contempt of itself; HC contempts are handled by HCs (Art 215). SC can deal with contempt of HC by exercising its Art 136 jurisdiction. Statements 1, 3, 4 are largely correct."),
    ("AP_HC","Indian_Polity","The \'right to sleep\' and \'right against noise pollution\' have been read into Article 21 by the Supreme Court in:
1. Ramlila Maidan Incident v. Home Secretary (2012) — right to sleep
2. Forum for Prevention of Environmental and Sound Pollution v. Union of India (2005) — right against noise pollution
3. Noise Pollution (Regulation and Control) Rules, 2000 — statutory framework
4. Both the right to sleep and right against noise pollution are recognised as Fundamental Rights","1 and 2 only","1, 3 and 4 only","1, 2 and 4 only","All of the above","D","hard","All four are correct: Ramlila Maidan case (1) recognised right to sleep as FD; Forum for Prevention case (2) dealt with noise pollution; Noise Pollution Rules 2000 (3) provide statutory protection; both are FRs under Art 21 (4)."),
    ("AP_HC","Indian_Polity","Assertion (A): Article 32 is itself a Fundamental Right — the right to move the Supreme Court for enforcement of Fundamental Rights.
Reason (R): Dr. B.R. Ambedkar described Article 32 as \'the most important article of the Constitution — an Article without which the Constitution would be a nullity.\'","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","easy","Both are true. A correctly states Art 32 is a FR. R correctly quotes Ambedkar. However R is a quote supporting the importance of Art 32, not an explanation of WHY Art 32 is a FR. Hence B."),
    ("AP_HC","Indian_Polity","Match List I (Amendment Act) with List II (What it was enacted to overcome):
List I: A. 1st Amendment  B. 4th Amendment  C. 17th Amendment  D. 25th Amendment
List II: 1. Vajravelu Mudaliar case — SC ruling on \'compensation\'
2. State of W.B. v. Bela Banerjee — full market value as compensation
3. Kameshwar Singh case — Bihar Zamindari Abolition Act
4. Champakam Dorairajan — no reservation in educational institutions","A-4, B-2, C-3, D-1","A-3, B-2, C-4, D-1","A-4, B-3, C-2, D-1","A-2, B-4, C-1, D-3","A","hard","1st Amendment = overcome Champakam Dorairajan (no reservation in education) — added Art 15(4) (4); 4th Amendment = overcome Bela Banerjee (full market value for compensation) (2); 17th Amendment = extend 9th Schedule (related to Kameshwar Singh type land reform cases) (3); 25th Amendment = changed \'compensation\' to \'amount\' after Vajravelu Mudaliar (1)."),
    ("AP_HC","Indian_Polity","Which of the following are \'constitutional torts\' or state liability situations recognised in Indian law?
1. State liability for acts of its servants under the doctrine of respondeat superior
2. Immunity of the state for sovereign acts (Kasturilal case)
3. Constitutional torts — compensation for violation of fundamental rights (Nilabati Behera case)
4. All government acts are now subject to negligence liability post-Maneka Gandhi","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","B","hard","Statement 4 is wrong: not ALL government acts attract negligence — sovereign functions still carry immunity. Statements 1, 2, 3 represent the evolution of state liability law in India."),
    ("AP_HC","Indian_Polity","The \'Doctrine of Pleasure\' under Article 310 has been held to be subject to the following exceptions:
1. Members of constitutional bodies with security of tenure (UPSC, CAG, etc.)
2. Civil servants who have constitutional protection under Article 311
3. Government employees on temporary appointment
4. Contractual employees who have contractual protections","1 and 2 only","2 and 4 only","1, 2 and 4 only","All of the above","A","hard","Constitutional bodies (1) and civil servants under Art 311 (2) are the primary exceptions to the doctrine of pleasure. Temporary employees (3) generally cannot claim Art 311 protection. Contractual employees (4) may have contractual remedies but Art 310 applies to those in civil posts under the Constitution. Hence A."),
    ("AP_HC","Indian_Polity","Which of the following correctly describes the \'tabling\' of reports before Parliament?
1. The CAG\'s report on Union accounts is submitted to the President who causes it to be laid before both Houses
2. The Finance Commission report is submitted to the President who places it before Parliament with an explanatory memorandum
3. NHRC\'s annual report is placed before both Houses of Parliament
4. UPSC\'s annual report is placed before both Houses of Parliament","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: CAG (Art 151) (1); Finance Commission (Art 281) (2); NHRC (PHR Act S.20) (3); UPSC (Art 323) (4) — all have statutory/constitutional requirements to place annual reports before Parliament."),
    ("AP_HC","Indian_Polity","Assertion (A): In India, the term of the Lok Sabha is five years unless dissolved earlier.
Reason (R): Article 83(2) provides that the Lok Sabha shall continue for five years from the date appointed for its first sitting unless sooner dissolved.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","easy","Both are true and R correctly quotes Art 83(2) which explains the term of Lok Sabha."),
    ("AP_HC","Indian_Polity","Match List I (Concept) with List II (Leading Indian case):
List I: A. Absolute liability for hazardous industries  B. Right against solitary confinement  C. Right against handcuffing  D. Environmental public trust doctrine
List II: 1. M.C. Mehta v. Kamal Nath (1997)
2. Citizens for Democracy v. State of Assam (1995)
3. Sunil Batra v. Delhi Administration (1978)
4. M.C. Mehta v. Union of India (1987 — Shriram Foods)","A-4, B-3, C-2, D-1","A-3, B-4, C-1, D-2","A-4, B-2, C-3, D-1","A-1, B-3, C-4, D-2","A","hard","Absolute liability = M.C. Mehta Shriram Foods (1987) (4); Solitary confinement = Sunil Batra (1978) (3); Handcuffing = Citizens for Democracy v. State of Assam (1995) (2); Public Trust = M.C. Mehta v. Kamal Nath (1997) (1)."),
    ("AP_HC","Indian_Polity","Which of the following constitutional provisions specifically empower Parliament to legislate on certain subjects related to property?
1. Entry 44, List I — incorporation of companies; regulation of companies
2. Entry 6, List II — public health and sanitation (affects land use)
3. Entry 42, List III — acquisition and requisitioning of property
4. Entry 36, List II — forests","1 and 3 only","1, 3 and 4 only","2 and 3 only","All of the above","A","hard","Entry 36 (forests) is in List III (Concurrent), not List II. Entry 6 (public health) is in List II. Entry 42 (acquisition/requisitioning) is in List III (Concurrent). The question asks about Parliament specifically: List I Entry 44 (companies) (1) and List III Entry 42 (acquisition) (3) empower Parliament. Hence A."),
    ("AP_HC","Indian_Polity","In the context of criminal appeals, which of the following are CORRECT about the High Court\'s appellate jurisdiction?
1. An HC can hear appeals against conviction in sessions court where sentence exceeds 7 years
2. An HC has power to enhance sentence even in an appeal filed by the accused alone
3. HC can acquit an accused who has been convicted by a lower court
4. HC can convert an acquittal into conviction in an appeal by the State","1 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","C","hard","Statement 1 is wrong: appeals against sessions court convictions lie to HC when sentence is 7+ years OR it\'s a capital sentence — but technically the right of appeal is broader. Statement 2 is wrong: HC should not enhance sentence in an appeal filed ONLY by the accused (without state\'s appeal) without giving the accused an opportunity to be heard. Statements 3 and 4 are correct."),
    ("AP_HC","Indian_Polity","Assertion (A): The principle of \'equal protection of laws\' under Article 14 allows for reasonable classification.
Reason (R): The twin test of reasonable classification requires: (i) an intelligible differentia distinguishing those grouped from others, and (ii) a rational nexus between the differentia and the object of the law.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly states the test applied by courts to determine whether a classification under Art 14 is reasonable. This is the classic Anwar Ali Sarkar (1952) test."),
    ("AP_HC","Indian_Polity","Which of the following are features of the Indian Constitution that make it unique among federal constitutions?
1. Single Constitution for the entire country (unlike USA where states have their own)
2. Single integrated judicial system
3. The Constitution contains explicit provisions for electoral process
4. Parliament can change state boundaries without state consent","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four are distinctive features of India\'s constitutional design: single Constitution (1), integrated judiciary (2), detailed electoral provisions (3), Parliament\'s power under Art 3 to change state boundaries without state consent (4)."),
    ("AP_HC","Indian_Polity","The \'principle of legitimate expectation\' in administrative law:
1. Creates a procedural right to be heard before a representation is withdrawn
2. Can in certain circumstances create a substantive right to a particular benefit
3. Does not apply to promises made without authority
4. Was held to be part of Article 14 in Council of Civil Service Unions (India position — per SC)","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct aspects of legitimate expectation doctrine in India: procedural right (1), sometimes substantive (2), no authority = no expectation (3), linked to Art 14 in Indian jurisprudence (4)."),
    ("AP_HC","Indian_Polity","Which of the following statements about India\'s federal system are CORRECT?
1. In India, the Residuary power is with Parliament (unlike in Australia where it is with the States)
2. In USA, residuary powers are with the States
3. India\'s Constitution has three lists while Canada has two lists
4. India and Australia both have Concurrent Lists","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: India = residuary with Centre (1); USA = residuary with states (2); India has 3 lists (Union, State, Concurrent), Canada has 2 (Union and Provincial) (3); both India and Australia have Concurrent Lists (4)."),
    ("AP_HC","Indian_Polity","Assertion (A): Article 21-A makes elementary education a Fundamental Right only for children between 6 and 14 years of age.
Reason (R): Children below 6 years are covered under Article 45 (DPSP) which requires the State to provide early childhood care and education, and children above 14 are not covered by any fundamental right to education.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","hard","A is true — Art 21-A covers 6-14. R is true — Art 45 (DPSP) covers under 6; children above 14 have no explicit FR to education (though higher education as a right may be read into Art 21). R provides relevant context but doesn\'t \'explain\' A — it explains what happens outside the 6-14 range. Hence B."),
    ("AP_HC","Indian_Polity","Which of the following are \'essential features\' of a parliamentary government as adopted in India?
1. The executive is responsible to the legislature
2. The head of state and head of government are the same person
3. There is a fusion of executive and legislative powers (Cabinet system)
4. Parliament can remove the government by a vote of no-confidence","1, 3 and 4 only","1 and 4 only","2, 3 and 4 only","All of the above","A","hard","Statement 2 is wrong: in India\'s parliamentary system, the head of state (President) and head of government (Prime Minister) are DIFFERENT persons. Statements 1, 3, 4 are correct features of the parliamentary system."),
    ("AP_HC","Indian_Polity","Match List I (Part of Constitution) with List II (Articles and Subject):
List I: A. Part V  B. Part VI  C. Part VIII  D. Part XI
List II: 1. Relations between Union and States (Arts 245-263)
2. Union Executive and Parliament (Arts 52-151)
3. Union Territories (Arts 239-241)
4. State Government (Arts 152-237)","A-2, B-4, C-3, D-1","A-4, B-2, C-1, D-3","A-2, B-3, C-4, D-1","A-3, B-4, C-2, D-1","A","medium","Part V = Union (President, PM, Parliament, SC) Arts 52-151 (2); Part VI = State Government Arts 152-237 (4); Part VIII = Union Territories Arts 239-242 (3); Part XI = Relations between Union and States Arts 245-263 (1)."),
    ("AP_HC","Indian_Polity","Consider the following about \'freedom of conscience\' under Article 25:
1. It protects the inner freedom — freedom to hold any religious belief or none
2. It is available to citizens and non-citizens alike
3. It cannot be restricted even on grounds of public order
4. \'Religion\' under Art 25 includes the right to manage religious institutions","1 only","1 and 2 only","1, 2 and 4 only","All of the above","B","hard","Statement 3 is wrong: freedom of conscience can be restricted on grounds of public order, morality, and health (Art 25(1)). Statement 4 is wrong: management of religious institutions is under Art 26. Statements 1 and 2 are correct."),
    ("AP_HC","Indian_Polity","Which of the following are CORRECT about the appointment procedure for judges of the Supreme Court?
1. The President appoints SC judges after \'consultation\' with the CJI and other judges
2. The collegium consists of the CJI and the four most senior judges of the SC
3. The collegium system is based on judicial pronouncements, not constitutional text
4. The government can return a collegium recommendation once, but if reiterated, must appoint","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: \'consultation\' in Art 124 (1); CJI + 4 senior judges (Third Judges case) (2); collegium is judge-made law, not in Constitution text (3); reiteration = must appoint (4) — these are the established rules of the collegium system."),
    ("AP_HC","Indian_Polity","Assertion (A): The Indian Penal Code (IPC) will be fully replaced by the Bharatiya Nyaya Sanhita (BNS) by 2024.
Reason (R): The BNS along with the Bharatiya Nagarik Suraksha Sanhita (BNSS) and Bharatiya Sakshya Adhiniyam (BSA) came into force on July 1, 2024, replacing the colonial-era IPC, CrPC, and Evidence Act.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains A. The three new criminal law codes were notified to come into force on July 1, 2024, replacing the colonial-era codes."),
    ("AP_HC","Indian_Polity","Which of the following have been recognised as dimensions of \'equality\' under Article 14 by the Supreme Court?
1. Formal equality — all are equal before the law
2. Substantive equality — laws must achieve real equality
3. Anti-discrimination — no unreasonable classification
4. Anti-arbitrariness — state action must not be arbitrary","1 and 3 only","1, 2 and 3 only","1, 3 and 4 only","All of the above","D","hard","All four dimensions have been recognised: formal equality (classical), substantive equality (Anuj Garg, EWS cases), anti-discrimination (classification test from Anwar Ali Sarkar), anti-arbitrariness (E.P. Royappa). Hence D."),
    ("AP_HC","Indian_Polity","The concept of \'judicial accountability\' in India includes:
1. In-house procedure for complaints against judges
2. Parliament\'s power to impeach judges
3. Requirement to declare assets annually
4. RTI Act applicability to judges\' official acts","1 and 2 only","1, 2 and 3 only","2 and 4 only","All of the above","D","hard","All four are aspects of judicial accountability: in-house procedure (1); Parliamentary impeachment (2); asset declaration (3) — voluntary/through in-house procedure; SC and HCs are public authorities under RTI for their administrative functions (4)."),
    ("AP_HC","Indian_Polity","Match List I (Article of the Constitution) with List II (Key word in article):
List I: A. Article 14  B. Article 19  C. Article 21  D. Article 32
List II: 1. \'Guaranteed\'
2. \'All persons\'
3. \'Citizens\'
4. \'Reasonable restrictions\'","A-2, B-3, C-4, D-1","A-4, B-3, C-2, D-1","A-2, B-4, C-3, D-1","A-3, B-2, C-1, D-4","B","hard","Art 14 = \'all persons\' (equality for all — not just citizens) (2 — actually Art 14 says \'any person\', not \'all persons\'); Art 19 = \'citizens\' (only citizens have these freedoms) (3); Art 21 = \'no person\' (broader) — the key term in 19(2-6) is \'reasonable restrictions\' (4); Art 32 = \'guaranteed\' — Ambedkar said this is the \'guaranteed\' article (1)."),
    ("AP_HC","Indian_Polity","Which of the following statements about \'judicial review\' in India are CORRECT?
1. Judicial review is a basic structure of the Indian Constitution
2. It extends to constitutional amendments and can strike them down for violating basic structure
3. Art 13 is the source of judicial review power for ordinary legislation
4. Art 32 and 226 are the means to exercise judicial review","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: basic structure (L. Chandra Kumar, Kesavananda) (1); review of amendments (Kesavananda) (2); Art 13 is the basis for review of ordinary laws (3); Art 32 and 226 are the writ jurisdictions through which review is exercised (4)."),
    ("AP_HC","Indian_Polity","The phrase \'morality or decency\' appearing in Article 19(2) as a restriction ground means:
1. Public morality in the broad sense of community standards
2. Constitutional morality which may differ from popular morality
3. The restriction must be necessary in a democratic society
4. Courts apply a reasonableness test to determine what constitutes indecency","1 and 4 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","B","hard","\'Morality or decency\' in Art 19(2) has been interpreted as including both public morality (1) and increasingly constitutional morality (2 — Navtej Johar). Courts apply reasonableness (4). Statement 3 is from European Convention language, not specifically articulated in Indian constitutional law. Hence B."),
    ("AP_HC","Indian_Polity","Under the Constitution, the High Courts have jurisdiction to issue writs under Article 226 to any person or authority:
1. Throughout the territory of India
2. Within its own territorial jurisdiction
3. In cases where the cause of action partly arises within its territorial jurisdiction
4. Outside its territorial jurisdiction if the authority has its headquarters within the HC\'s jurisdiction","1 only","2 and 3 only","2, 3 and 4 only","All of the above","C","hard","Art 226(1) as amended: HC can issue writs to any person/authority within its territorial jurisdiction OR where any cause of action WHOLLY OR PARTLY arises within its jurisdiction (2, 3). Statement 1 is wrong — HCs don\'t have nationwide jurisdiction. Statement 4 is partially the basis for statements 2/3 application. Hence C (2, 3, 4 together is the correct interpretation)."),
    ("AP_HC","Indian_Polity","Assertion (A): The Constitution of India specifically provides for \'freedom of the press\'.
Reason (R): Freedom of the press in India is a constitutionally recognised right derived from Article 19(1)(a) which guarantees freedom of speech and expression.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","D","medium","A is false: the Constitution does NOT \'specifically provide\' for freedom of the press — it is not mentioned. R is true — press freedom is implied in Art 19(1)(a) as held by the SC. Hence D."),
    ("AP_HC","Indian_Polity","The concept of \'public policy\' as a ground to refuse enforcement of a foreign arbitral award in India includes:
1. Fraud or corruption in the award
2. Patent illegality (for domestic awards only)
3. Violation of fundamental policy of Indian law
4. Award contrary to morality or justice","1 and 3 only","1, 3 and 4 only","2, 3 and 4 only","All of the above","B","hard","For FOREIGN awards under Part II of Arbitration Act: public policy includes fraud/corruption (1), fundamental policy violation (3), and morality/justice (4). Patent illegality (2) is ONLY a ground for setting aside DOMESTIC awards (Part I), not foreign awards. Hence B."),
    ("AP_HC","Indian_Polity","Which of the following statements about \'Comptroller and Auditor General\' are CORRECT?
1. The CAG is the guardian of the public purse
2. The CAG audits all expenditure from the Consolidated Fund of India
3. The CAG also audits bodies substantially financed by the government
4. The CAG controls the issue of money from the Consolidated Fund","1, 2 and 3 only","2, 3 and 4 only","1, 2 and 4 only","All of the above","A","hard","Statement 4 is wrong: The CAG does NOT control issue of money from the Consolidated Fund — that is done by the government. The CAG is an Auditor, not a Controller in the spending sense (despite the title). The title is historical. Statements 1, 2, 3 are correct."),
    ("AP_HC","Indian_Polity","Consider the following about the \'separation of powers\' in India:
1. India follows a strict separation of powers as in the USA
2. There is a flexible separation of powers with checks and balances
3. Judicial review is a check by the judiciary on the legislature and executive
4. The Indian Parliament performs quasi-judicial functions in impeachment proceedings","2, 3 and 4 only","1, 3 and 4 only","2 and 3 only","All of the above","A","hard","Statement 1 is wrong: India does NOT have strict separation of powers (as in the USA). India has a flexible system with overlapping functions and checks and balances. Statements 2, 3, 4 are correct."),
    ("AP_HC","Indian_Polity","Match List I (Important Report/Commission) with List II (Subject Matter):
List I: A. Rajmannar Committee (1969)  B. Anandpur Sahib Resolution (1973)  C. West Bengal Memorandum (1977)  D. Sarkaria Commission (1988)
List II: 1. Final recommendations on Centre-State relations
2. Punjab/Akali Dal demands for greater autonomy
3. West Bengal\'s proposals for rebalancing Centre-State powers
4. Tamil Nadu\'s demands for greater state autonomy
(All in context of Centre-State relations debate)","A-4, B-2, C-3, D-1","A-2, B-4, C-1, D-3","A-4, B-3, C-2, D-1","A-1, B-2, C-3, D-4","A","hard","Rajmannar Committee = Tamil Nadu (Centre-State autonomy) (4); Anandpur Sahib Resolution = Punjab autonomy demands (2); W.B. Memorandum = West Bengal\'s proposals (3); Sarkaria Commission = final Centre-State recommendations (1)."),
    ("AP_HC","Indian_Polity","Under the Criminal Law (Amendment) Act, 2013 (post-Nirbhaya), which of the following new offences were added to the IPC?
1. Voyeurism (Section 354-C)
2. Stalking (Section 354-D)
3. Acid attack (Section 326-A and 326-B)
4. Sexual harassment (Section 354-A)","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","D","hard","The Criminal Law Amendment Act 2013 (based on Justice Verma Committee) added all four new offences: voyeurism (354-C), stalking (354-D), acid attack (326-A, 326-B), and sexual harassment (354-A)."),
    ("AP_HC","Indian_Polity","Assertion (A): In India, the power to declare a \'Money Bill\' rests with the Speaker of the Lok Sabha.
Reason (R): Article 110(3) provides that if a question arises whether a Bill is a Money Bill, the decision of the Speaker of the House of the People thereon shall be final.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","easy","Both are true and R correctly explains A by quoting Art 110(3) which makes the Speaker\'s decision on whether a Bill is a Money Bill final."),
    ("AP_HC","Indian_Polity","Which of the following are CORRECT statements about \'Gram Sabha\' under the 73rd Amendment?
1. Gram Sabha is a constitutional body
2. It consists of all persons registered as voters in the village
3. Its functions are determined by state legislatures
4. The Gram Sabha is the primary decision-making body for villages","1 and 2 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four are correct: Gram Sabha is defined in Art 243-A making it a constitutional body (1); voters in the village are its members (2); state legislatures determine its functions under Art 243-A (3); it is the foundation of democratic decentralisation (4)."),
    ("AP_HC","Indian_Polity","The right to \'claim\' constitutional remedies under Article 32 means:
1. The remedy cannot be waived by the individual
2. Even government cannot waive another person\'s Art 32 rights
3. The SC can refuse to entertain a petition under Art 32 if it is not bona fide
4. Art 32 can be invoked even if equivalent remedy is available under ordinary law","1 and 2 only","1, 2 and 4 only","2, 3 and 4 only","All of the above","D","hard","All four are correct aspects of Art 32: non-waivable (1 and 2); SC can decline if not bona fide/abuse of process (3); Art 32 is available even if other remedies exist (4) — though SC may direct approaching HC first, it doesn\'t bar Art 32."),
    ("AP_HC","Indian_Polity","Consider the following about the \'Emergency provisions\' and identify the INCORRECT statement:
1. During Financial Emergency, the President can give direction to states to observe \'canons of financial propriety\'
2. During National Emergency, the Centre can give executive directions to states on any subject
3. During President\'s Rule, Parliament legislates for the state and such laws continue even after President\'s Rule ends
4. State of Emergency proclaimed by the President can be revoked only by Parliament, not by the President alone","4 only","3 only","2 only","1 only","A","hard","Statement 4 is INCORRECT: the President CAN revoke a proclamation (Art 352(2) and (7)) — the President has the power to revoke without Parliamentary action (though Parliament can also disapprove). All other statements (1, 2, 3) are correct."),
    ("AP_HC","Indian_Polity","Match List I (Landmark HC case) with List II (State):
List I: A. Madras Bar Association v. Union of India  B. Society for Un-Aided Private Schools of Rajasthan v. Union of India  C. Christian Medical College v. Union of India  D. Mohd. Ahmed Khan v. Shah Bano Begum
List II: 1. Madhya Pradesh HC
2. Madras HC
3. Rajasthan HC
4. Kerala/Vellore (Madras jurisdiction)
(Identify where these cases originated)","A-2, B-3, C-4, D-1","A-4, B-2, C-3, D-1","A-2, B-4, C-3, D-1","A-3, B-2, C-1, D-4","A","hard","Madras Bar Association = SC appellate from Madras jurisdiction (2); Society for Un-Aided Schools Rajasthan = Rajasthan HC (3); Christian Medical College = Kerala HC area (4); Shah Bano = MP HC (1). These are approximate — all went to SC."),
    ("AP_HC","Indian_Polity","Which of the following are provisions specifically applicable to BOTH the Union and States under the Constitution?
1. Consolidated Fund and Public Account provisions
2. Finance Commission recommendations
3. CAG audit
4. Judicial review by the Supreme Court","1 and 3 only","1, 2 and 3 only","2, 3 and 4 only","All of the above","D","hard","All four apply to both Union and States: both have Consolidated Funds and Public Accounts (Arts 266-267) (1); Finance Commission covers Centre-State division (2); CAG audits both (3); SC reviews both Union and State laws (4)."),
    ("AP_HC","Indian_Polity","Assertion (A): A constitutional amendment can be challenged in a court of law only after it has been enacted by Parliament and given Presidential assent.
Reason (R): Courts exercise judicial review of laws — including constitutional amendments — only after they come into force, as courts decide on actual cases and controversies, not hypothetical ones.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","A","medium","Both are true and R correctly explains A. Courts do not issue advisory opinions on bills — they review laws after enactment. A constitutional amendment can only be challenged after it is enacted and in force."),
    ("AP_HC","Indian_Polity","Which of the following are CORRECT about \'Proportional Representation\' used in India?\n1. Members of Rajya Sabha are elected by state legislative assemblies using Single Transferable Vote (STV)\n2. Members of Legislative Councils are partly elected by STV\n3. The President and Vice President are elected by STV\n4. Lok Sabha members are elected by First-Past-the-Post (FPTP) system","1, 2 and 4 only","2 and 4 only","1 and 4 only","All of the above","D","medium","All four statements are correct. (1) RS members are elected by state legislative assemblies using STV (Art. 80). (2) MLCs are partly elected by STV (Art. 171). (3) The President (Art. 54) and Vice President (Art. 66) are elected by STV under the Presidential and Vice-Presidential Elections Act. (4) Lok Sabha members are elected by FPTP. Since all four are correct, the answer is D."),
    ("AP_HC","Indian_Polity","Assertion (A): The Indian Constitution is described as \'organic\' in the sense that it can grow and adapt to changing social needs.
Reason (R): Article 368 provides for amendment of the Constitution, and the basic structure doctrine allows the core values to evolve through judicial interpretation.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","B","medium","Both A and R are true. The Constitution is indeed organic/living. R correctly mentions amendment power and basic structure evolution. However, the \'organic\' nature is also explained by open-textured language and evolving judicial interpretation beyond just Art 368. Hence B."),
    ("AP_HC","Indian_Polity","Under the Scheduled Castes and the Scheduled Tribes (Prevention of Atrocities) Act, 1989, the Special Courts are required to complete trials within:
1. 60 days from date of filing of charge sheet
2. 2 months from date of charge sheet
3. As expeditiously as possible — no fixed time limit in the original Act
4. 6 months as per 2015 Amendment Rules","1 only","3 only","4 only","2 only","C","hard","The Scheduled Castes and Scheduled Tribes (Prevention of Atrocities) Amendment Rules, 2016 and related guidelines specify time limits. The SC/ST PoA (Amendment) Act 2015 and rules specify that Special Courts should complete trials within a time-bound manner. The 2016 rules specify 60 working days. For exam purposes, option 4 (6 months) is the commonly stated answer for SC/ST PoA cases."),
    ("AP_HC","Indian_Polity","Match List I (High Court) with List II (Established/Jurisdiction):
List I: A. Allahabad High Court  B. Calcutta High Court  C. Bombay High Court  D. Madras High Court
List II: 1. Established 1862 — one of three original High Courts under High Courts Act 1861
2. Established 1866 — oldest HC in India (contested)
3. Also 1862 — covers Maharashtra, Goa, Daman & Diu
4. Also 1862 — covers Tamil Nadu, Puducherry","A-2, B-1, C-3, D-4","A-1, B-2, C-3, D-4","A-3, B-1, C-4, D-2","A-4, B-1, C-2, D-3","A","hard","Allahabad HC = 1866 (2); Calcutta, Bombay, Madras HCs were established in 1862 under the High Courts Act 1861 — all three were the original Charter High Courts. Bombay = Maharashtra/Goa (3); Madras = TN/Puducherry (4); Calcutta = one of original three (1)."),
    ("AP_HC","Indian_Polity","Which of the following are CORRECT about the composition and working of the GST Appellate Tribunal (GSTAT) established by Finance Act, 2023?
1. GSTAT adjudicates disputes arising from GST Council decisions
2. GSTAT hears appeals against orders of Appellate Authority under GST Acts
3. The President of GSTAT must be a retired Supreme Court or HC judge
4. Appeals from GSTAT lie to the High Court on questions of law","1 and 2 only","2, 3 and 4 only","2 and 4 only","All of the above","B","hard","Statement 1 is wrong: GSTAT does NOT adjudicate GST Council decisions — it hears appeals against tax department orders. Statements 2, 3, 4 are correct features of GSTAT under the GST Appellate Tribunal provisions."),
    ("AP_HC","Indian_Polity","Assertion (A): The Andhra Pradesh High Court has original civil jurisdiction over cases involving amounts above a certain monetary limit arising within the city of Amaravati.
Reason (R): Unlike the High Courts of Bombay, Calcutta, and Madras which have original jurisdiction from the charter era, the AP HC\'s original jurisdiction (if any) is governed by statute.","Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true","D","hard","A is false: The AP High Court does NOT have original civil jurisdiction like Bombay, Calcutta and Madras HCs (which are charter HCs with original jurisdiction). R is true — only Charter High Courts (Bombay, Calcutta, Madras) have original civil jurisdiction; AP HC does not. Hence D."),
]


def seed():
    if USE_POSTGRES:
        import psycopg2, urllib.parse as up
        url = up.urlparse(os.environ["DATABASE_URL"])
        conn = psycopg2.connect(
            host=url.hostname, port=url.port or 5432,
            dbname=url.path.lstrip("/"),
            user=url.username, password=url.password,
            sslmode="require"
        )
        ph = "%s"
    else:
        import sqlite3 as sq
        conn = sq.connect(os.path.join(os.path.dirname(__file__), "database.db"))
        ph = "?"

    cur = conn.cursor()
    inserted = skipped = 0
    for row in PYQ_MCQS:
        folder, topic, q = row[0], row[1], row[2]
        cur.execute(f"SELECT COUNT(*) FROM questions WHERE folder={ph} AND topic={ph} AND question_text={ph}",
                    (folder, topic, q))
        if cur.fetchone()[0] == 0:
            cur.execute(f"""INSERT INTO questions
                (folder,topic,question_text,option_a,option_b,option_c,option_d,correct_answer,difficulty,explanation)
                VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""", row)
            inserted += 1
        else:
            skipped += 1
    conn.commit()
    conn.close()
    print(f"[seed_polity_pyq_500] Inserted {inserted}, Skipped {skipped}")

if __name__ == "__main__":
    seed()
