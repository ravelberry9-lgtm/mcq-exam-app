"""Manual explicit-claim inventory; source-reading and semantic review are not automated.
Only writes this chapter's inventory/audits and canonical-reference metadata.
It never regenerates question objects, keys or explanations.
"""
import json
from pathlib import Path
P=Path(__file__).parent
ROOT=P.parents[1]
DATA='''
origin-modern|Marbury is the conventional modern American landmark for judicial review, not proof that no earlier review practice existed anywhere.|P0;T0|assessed|E:POL-751-P297-ORIGIN-01|Only the case–judge association is independently assessed by the preserved origin item.
origin-year|Marbury v. Madison was decided in1803.|P0;T0|assessed|L:marbury-year|The original question supplies the year; the new item actually retrieves it.
origin-marshall|Chief Justice John Marshall is associated with the Marbury opinion.|P0;T0|assessed|E:POL-751-P297-ORIGIN-01|Case–judge association only.
us-unnamed|The US Constitution does not use the phrase judicial review.|P0;T0|held-primary||No independent phrase-search or US constitutional-text question approved.
us-entirely-judge-made|The reader describes American review as entirely judge-made without an express review clause.|P0;T0;T5|held-comparative-qualification||Do not convert absence of the phrase into absence of ArticleIII or supremacy-clause textual foundations.
india-textual-basis|Indian review is supported by multiple operative constitutional provisions rather than one standalone phrase.|P0;P1;P5;P6;T4|partial|E:POL-751-CH-03;E:POL-751-CH-04|Article13and32/226facets are assessed; the entire distributed-design explanation is not independently tested.
india-two-courts|Both Supreme Court and High Courts exercise constitutional review.|P0;P2;P6;T0|assessed|E:POL-751-CH-04|The paired court routes are assessed, not every possible jurisdictional gate.
review-basic-feature|Judicial review is a basic feature protected against destructive constitutional amendment.|P0;P10;P11;T0;T7|assessed|E:POL-751-P299-01|Does not imply that every procedural adjustment to jurisdiction is prohibited.
american-history-framers|Indian framers had nearly150years of American review history before them.|P1|held-historical-inference||A broad historical explanation, not an independently verified motive or numerical exam fact.
american-legitimacy-debate|The reader attributes fierce legitimacy disputes to the absence of a freestanding American review clause.|P1|held-editorial||Attribution of historical causation requires evidence; no question treats it as settled fact.
framers-distributed-deliberately|The reader says deliberate distribution across Articles made judicial review harder to eliminate.|P1;P6;T4|held-editorial||Constitutional structure is visible; the specific intention and redundancy causal explanation are not automatically proven by it.
article13-substantive-rule|Article13makes laws inconsistent with Fundamental Rights void to the extent of inconsistency.|P1;P2;P6;T3:13;T4|assessed|E:POL-751-CH-03|Temporal and Article13(4)questions require their own qualifications.
access-routes|Article32and226provide Supreme Court and High Court rights-enforcement routes.|P1;P6;T3:32;T3:226;T4|assessed|E:POL-751-CH-04|Article226also covers other lawful purposes; Article32is not a general statutory-dispute appeal.
jurisdiction-architecture|Articles131–136provide distinct original/appellate jurisdictional powers.|P1;P6|partial||Individual table rows below are mapped; this general range is not one unlimited review power.
deletion-redundancy|The reader argues that deleting one sentence cannot remove the distributed enforcement machinery.|P1;P6;T4|held-editorial||Do not equate an analytical explanation with a validated amendment procedure.
definition|Review examines legislative and executive/administrative action for constitutional validity.|P2;T1|assessed|E:POL-751-P297-01|Definition only; does not itself prove every subsequent remedial or standing rule.
union-state-actions|Review extends to Union and State legislative/executive action.|P2|partial|E:POL-751-CH-01|The three categories are assessed; each governmental example is not an independent question.
ultra-vires|Action outside lawful constitutional authority may be invalidated.|P2|assessed|E:POL-751-CH-05|Same actual competence/constitutional-limit target; do not clone it just to ask the Latin label.
invalidity-enforcement|A constitutionally invalid norm cannot be enforced merely because the Government wishes to use it.|P2|partial|E:POL-751-P297-01|A definition-level consequence, not all temporal/remedial consequences of invalidity.
quadri-attribution|The reader attributes its three-category classification to Justice Syed Shah Mohamed Quadri.|P2;T1|held-primary-attribution||The classification is assessed; the author attribution has not been independently validated or tested.
review-amendments|Constitutional amendments are subject to the governing review limits.|P2;P10;T1;T7|assessed|E:POL-751-CH-01;E:POL-751-P299-01|Not ordinary Article13scrutiny without the Article13(4)/basic-structure distinction.
review-legislation|Review includes parliamentary and State legislation.|P2;T1|assessed|E:POL-751-CH-01|A category target, not every law's validity.
review-delegated|Delegated legislation is reviewable and must remain within its parent law and Constitution.|P2|assessed|L:delegated-legislation-review|Distinct from identifying Parliament's subordinate-legislation committee.
review-administration|Administrative action is within the classification of review.|P2;T1|assessed|E:POL-751-CH-01|Not exhaustive administrative-law grounds or remedies.
golak-example|Golak Nath illustrates adjudication of amendment power.|P2|canonical|R:6.7.1:POL-671-N004|The actual amendment/Article13relationship is assessed; do not independently credit a year supplied in a stem.
golak-year|The reader dates Golak Nath to1967.|P2|context-unassessed||Relevant existing questions often supply1967; no independent exact-year credit is claimed here.
bank-nationalisation|The Bank Nationalisation case is a listed1970review example.|P2|held-history||Existing R.C.Cooper compensation practice is not a question on the example/year itself.
privy-purses-example|The reader lists a1970Privy Purses case as an example.|P2|held-history-qualification||Distinguish the1970derecognition litigation from the26thAmendment1971abolition; no new case-year question approved.
kesavananda-example|Kesavananda Bharati establishes the basic-structure limitation.|P2;P10;P11;T7|assessed|E:POL-751-P298-01|Preserved local ID remains; related Unit6items also exist.
kesavananda-date|Kesavananda was decided on24April1973.|P2;P13;T9|canonical|R:6.8.1:POL-681-S007|The canonical item actually retrieves the date, rather than supplying it.
minerva-limited-amendment|Minerva Mills invalidated the attempt to make amending power unlimited and exclude review.|P2;P10;T7|canonical|R:6.8.1:POL-681-S008|Do not infer invalidity of every part of the42ndAmendment.
minerva-year|The reader dates Minerva Mills to1980.|P2;P4|canonical|R:6.5.2:POL-652-N014|The existing case–year correctness item actually assesses this year association.
njac-two-enactments|The99thAmendment2014and NJAC Act2014were separate enactments and both were invalidated.|P2;P10;P11;T1;T7|canonical|R:6.8.1:POL-681-P517-003|No clone of the existing three-statement question.
njac-2015-date|The reader dates NJAC invalidation to2015.|P2;P10;T1;T7|context-unassessed|R:6.8.1:POL-681-P517-003|The canonical stem supplies2015; the year is not independently retrieved by its response.
purpose-supremacy|Review protects constitutional supremacy.|P3;P16;T2;T10|assessed|E:POL-751-CH-02|Selected purpose, not a licence for unlimited court supremacy.
purpose-federal|Review helps maintain federal equilibrium.|P3;P16;T2;T10|assessed|E:POL-751-CH-02|The purpose is assessed; every federal mechanism is not thereby covered.
purpose-rights|Review safeguards Fundamental Rights against unconstitutional legislative/executive action.|P3;P16;T2;T10|assessed|E:POL-751-CH-02|Rights and standing remain subject to the applicable constitutional clauses.
gopalan-kania|The reader attributes constitutional-supremacy observations in Gopalan to Chief Justice Kania.|P4|held-primary-attribution||The speaker/observation has not been separately primary-validated for this expansion.
gopalan-year|Gopalan was decided in1950.|P4|canonical|R:6.4.1:POL-6.1.9-P109-09|The canonical Gopalan–Maneka year pair actually assesses1950.
vgrow-sentinel|V.G.Row and Patanjali Sastri are associated with the sentinel-on-the-qui-vive observation.|P4;T2|assessed|L:judicial-observations|Joint observation–case–speaker association; source wording was checked in L.ChandraKumar paragraph57.
vgrow-year|The reader dates V.G.Row to1952.|P4|context-unassessed||The new matching response does not independently retrieve this year.
khanna-kesavananda|The reader attributes continuing rights-enforcement review observations in Kesavananda to Justice Khanna.|P4|held-primary-attribution||Do not treat general agreement with the principle as verification of this precise speaker attribution.
rajasthan-bhagwati|State of Rajasthan and P.N.Bhagwati are associated with the Court's ultimate-interpreter observation.|P4;T2|assessed|L:judicial-observations|Checked against the later official Supreme Court report's attributed quotation.
rajasthan-year|The reader dates State of Rajasthan v.Union to1977.|P4|context-unassessed||A report-year/judgment-year distinction may arise; the matching item does not ask the year.
minerva-adornment|Minerva Mills and Y.V.Chandrachud are associated with the warning about rights without remedies becoming an adornment.|P4;T2|assessed|L:judicial-observations|Official report printed241–242supports the attribution; no exclusive claim about that judge is made.
chandra-ahmadi|The reader attributes the constitutional-limit observation in L.ChandraKumar to Chief Justice Ahmadi.|P4|held-primary-attribution||The case's review doctrine is supported; this exact quote-attribution facet is not independently assessed.
chandra-case-doctrine|L.ChandraKumar preserves constitutional judicial review over tribunal decisions.|P4|canonical|R:7.4.4:POL-744-P329-01|Case–doctrine association only.
chandra-year|The reader dates L.ChandraKumar to1997.|P4|context-unassessed||The compatible case-identification question does not retrieve its year.
bola-name|The prepared paragraph says S.S.Bola v.B.D.Sharma.|P4|held-bibliographic-conflict||The reported case is commonly identified as B.D.Sardana; validate the exact primary case and quoted opinion before adopting any new case-attribution question.
bola-ramaswami|The reader attributes a federal-balance/rights/interpretation observation to Justice Ramaswami in its S.S.Bola citation.|P4|held-primary-attribution||The bibliographic problem and speaker/opinion scope remain open.
bola-year|The reader dates its S.S.Bola reference to1997.|P4|held-history||Not an independently validated/assessed year target here.
phrase-india-unnamed|The reader says the exact phrase judicial review appears nowhere in the Indian Constitution.|P5;T4|held-textual-claim||No complete authoritative phrase-search gate is claimed; this is not the same as Article137's express power of review of judgments.
sixteen-count|The reader calls the constitutional table sixteen Articles.|P5;P6;T4|source-count-qualification||There are16table rows but17distinct named Articles because251and254share one row; do not memorise16as a proven count of individual Articles.
rule-route-jurisdiction|The reader explains review as a substantive rule plus access routes plus jurisdiction.|P6;T4|partial|E:POL-751-CH-03;E:POL-751-CH-04|An explanatory synthesis, not a separate comprehensive operational test.
removing-review-machinery|The reader argues that abolishing review would dismantle constitutional enforcement machinery.|P6;P11|canonical|R:6.8.1:POL-681-P516-001|The compatible item assesses constitutional supremacy and rejects replacement by unlimited Parliament; not every causal assertion is separately tested.
ground-rights|An enactment/action may be reviewed for Fundamental Rights infringement.|P7;T6|assessed|E:POL-751-CH-05|Same existing ground; no clone.
ground-competence|An enactment/action may be reviewed for exceeding the maker's lawful competence.|P7;T6|assessed|E:POL-751-CH-05|Detailed federal rules receive separate table-level treatment.
ground-other-provision|Repugnancy to another constitutional provision may ground review.|P7;T6|assessed|E:POL-751-CH-05|Do not confuse constitutional inconsistency with the particular Article254statutory-repugnancy rule.
due-process-words|Article21uses procedure established by law; USFifth/Fourteenth Amendments have due-process clauses.|P7;T5;T6|canonical|R:6.4.1:POL-6.1.9-P109-06|The canonical wording comparison also rejects an actual textual replacement by Maneka.
india-never-reasonableness|The reader says Indian courts examine only competence and not reasonableness.|P7;T5;T6|source-conflict-corrected-canonically|R:6.4.1:POL-6.1.9-P108-06;R:6.4.1:POL-6.4.1-P113-15|Maneka requires fair/just/reasonable procedure and applicable14/19scrutiny; the blanket exclusion is not a study fact.
us-wide-india-narrow|The reader describes USreview as very wide and India's as limited.|P7;T5;T6|held-comparative-qualification||Historical textbook shorthand is not an unconditional current-law rule about every field of review.
merits-not-policy-substitution|Judicial review of legality is distinguished from simply substituting a court's preferred policy.|P7;P9;P17;T6;T10|partial|R:7.6.1:POL-761-CH-08|The canonical item assesses review with institutional limits; no exhaustive policy-review test is claimed.
third-chamber-criticism|Critics describe the USSupremeCourt as a third chamber/super-legislature/arbiter of policy.|P8;T5|partial|L:countermajoritarian-criticism|Related theoretical criticism; the figurative phrase itself is not independently retrieved by the new item and is not a literal legislative chamber.
uk-parliamentary-supremacy|The reader contrasts Britain's parliamentary supremacy with Indian constitutional limits.|P8;T5|partial|R:6.8.1:POL-681-P516-001|The item assesses constitutional versus unlimited parliamentary supremacy, not every comparative British proposition.
written-limit|The written Constitution constrains Indian Parliament.|P8|partial|R:6.8.1:POL-681-P516-001|One aspect of constitutional supremacy; no separate four-factor recall credit.
federal-limit|Constitutional division of powers constrains parliamentary sovereignty.|P8|partial|L:legislative-lists|The list-distribution response assesses the allocation, not the historical explanation of parliamentary sovereignty.
rights-limit|Fundamental Rights constrain ordinary lawmaking.|P8|assessed|E:POL-751-CH-03|Subject to precise constitutional qualifications, including amendment doctrine and specific savings.
review-limit|Judicial review is itself a constraint on government organs.|P8|assessed|E:POL-751-P297-01|Definition-level coverage only.
synthesis-model|The reader describes India as a synthesis of USjudicial supremacy and UKparliamentary supremacy.|P8;T5;T6|held-conceptual-shorthand||This is comparative explanatory language, not an operative constitutional phrase or proof of unlimited supremacy for either organ.
borrowed-parliamentary|The reader cites Britain's parliamentary system as a constitutional influence.|P9|context-unassessed||Incidental borrowing background is not newly authored as a judicial-review question.
borrowed-federal|The reader cites partial USinfluence on federalism.|P9|context-unassessed||A qualified borrowing claim, not complete identity between the systems.
borrowed-rights|The reader cites the USBillofRights as a source influence for Fundamental Rights.|P9|context-unassessed||No new borrowing-source item or separate coverage credit here.
procedure-source-japan|The reader's British-style description must not change the conventional source association of procedure established by law.|P9|source-qualification-canonical|R:6.1.4:POL-6.1.4-P38-08|The existing matching question associates the formula with Japan, not Britain.
reform-motive|The reader attributes rejection of a broad due-process formula to the desire for social/economic reform.|P9|held-historical-motive||A contextual explanatory claim; it is not independently proven by the wording of Article21alone.
american-economic-history|The reader discusses early20thcentury USjudicial resistance to economic regulation.|P9|held-primary-history||No new American case-history or causal-motive question approved.
maneka-fairness-evolution|Later Article21interpretation incorporates fairness/reasonableness without changing its words.|P9;T6|canonical|R:6.4.1:POL-6.1.9-P108-06;R:6.4.1:POL-6.1.9-P109-06|Do not teach the earlier comparison as an unqualified current exclusion.
article368-limits-not-explicit|The phrase basic structure is not in Article368's text, though the governing doctrine constrains amendment power.|P10;P11;T7|canonical|R:6.7.1:POL-671-N006|The existing two-statement item assesses both propositions.
formal-procedure-not-enough|Following amendment procedure does not permit destruction of basic structure.|P10;P11;T7|canonical|R:6.8.1:POL-681-P516-001|Same actual target; no clone merely changing the example.
amend-not-replace|Limited amendment power does not permit replacing constitutional identity with unlimited power.|P11;T7|canonical|R:6.4.1:POL-6.1.9-P130-09|The limited character of amendment power is independently assessed by the compatible assertion/reason item.
self-referential-description|The reader calls the doctrine self-referential because review protects its own survival.|P11;T7|held-editorial||Analytical description, not a separate constitutional text rule or an independently assessed philosophical label.
article31b-scope|Article31Bexpressly shields specified Ninth Schedule laws from PartIIIrights objections, not all constitutional defects.|P12;T9|assessed|L:article31b-limited-shield|The qualified boundary, not blanket immunity, is assessed.
article31b-identifier|Article31Bis the provision associated with Ninth Schedule validation.|P12;T9|canonical|R:6.4.1:POL-6.1.9-P118-04|This canonical item retrieves the provision identifier; the new scope question does not duplicate that response.
ninth-first-amendment|The First Amendment1951inserted Article31Band the Ninth Schedule.|P12;T8:r1;T9|assessed|E:POL-751-CH-06|Preserve the old localID; an equivalent/superset Unit6item exists, but no retirement was performed.
ninth-original-thirteen|The original Ninth Schedule contained thirteen Acts and Regulations.|P12;T8:r1;T9|assessed|L:ninth-original-count|Historical original count only; no present-total inference.
ninth-current282|The reader states a present total of282entries.|P12;T9|held-dated-count||Do not turn a version-specific count into an unqualified current fact. Last serial284, lettered257Aand omissions require careful enumeration.
state-enactment-versus-insertion|State enactment of an underlying law does not itself amend the Ninth Schedule.|P12;P15|assessed|L:ninth-insertion-mechanism|Corrects the potentially misleading statement that State legislatures add their Acts to the constitutional Schedule.
land-reform-purpose|Early Ninth Schedule protection centrally concerned land reforms and zamindari abolition.|P12|canonical|R:6.7.1:POL-671-P514-002|The same item rejects automatic inclusion of every land law.
other-subjects-possible|The Ninth Schedule is not confined forever to land-reform legislation.|P12|canonical|R:6.7.1:POL-671-P514-002|The existing statement3tests and rejects an exclusive-land-reform restriction.
kesavananda-ninth-evolution|The reader traces the Ninth Schedule's basic-structure qualification through Kesavananda and WamanRao.|P13;T9|partial|R:6.8.1:POL-681-S005|The operative insertion-date cutoff is assessed, not every historical attribution in this compressed narrative.
waman-cutoff|On-or-after24April1973Ninth Schedule insertion amendments are open to the governing basic-structure scrutiny.|P13;P14;T9|assessed|E:POL-751-CH-07;R:6.8.1:POL-681-S005|Use on-or-after, not a shorthand that excludes the cutoff day.
inclusion-not-enactment-date|The inclusion amendment's date, not the underlying statute's enactment date, controls the cutoff.|P13;P15|canonical|R:6.8.1:POL-681-S005|Do not clone the existing two-statement distinction.
waman-date-alone-not-invalid|Being within the reviewable post-cutoff class does not itself establish invalidity.|P13;P15|canonical|R:6.8.1:POL-681-S006|The underlying effect inquiry remains.
waman-year|The reader labels WamanRao as1980.|P13;T9|context-unassessed||Distinguish decision/reasons dates from1981report citations; no new year-recall item is approved.
coelho-basic-rights|Coelho links review of later Ninth Schedule insertions to basic structure and the essence of Articles14,19and21.|P13;P14;T9|canonical|R:6.8.1:POL-681-N002|Primary operative conclusions qualify the reader's looser Article15/or-basic-structure wording.
coelho-every-rights-breach|The reader's wording must not mean that every PartIIIinfringement automatically equals basic-structure damage.|P13;P14|source-conflict-corrected-by-assessment|L:coelho-impact-not-form|Operative conclusion(i)expressly distinguishes the two.
coelho-year|The reader dates Coelho to2007.|P13;T9|context-unassessed||The canonical stem supplies2007and does not independently retrieve it.
coelho-effect-not-form|Actual impact on rights, not merely the amendment's form or Schedule label, drives the inquiry.|P14:1-4;P15|assessed|L:coelho-impact-not-form|No separate exhaustive Coelho checklist credit.
coelho-own-merits|Each new amendment is examined on its own merits and actual impact.|P14:2|partial|L:coelho-impact-not-form|The response tests impact rather than label; it does not independently recite every procedural conclusion.
coelho-rights-essence|The rights test and essence-of-the-right test are applied through basic-structure analysis.|P14:3-4|canonical|R:6.8.1:POL-681-N002|Exact labels alone are not separate extra questions; no blanket PartIIIautomatically-invalid rule.
coelho-upheld-saving|Coelho preserves its stated saving for Ninth Schedule laws whose validity the Supreme Court already upheld.|P14:5|canonical|R:6.8.1:POL-681-N002|The existing statement2tests and rejects mandatory re-examination of every upheld law.
coelho-invalid-reinserted|Earlier PartIII-invalidated laws later inserted after the cutoff remain open to the specified basic-structure challenge.|P14:5|assessed|L:coelho-invalid-reinserted|Distinct second limb of conclusion(v), not the previously-upheld limb.
coelho-finalised-saving|Coelho expressly saves action taken and transactions finalised under the impugned Acts.|P14:6|assessed|L:coelho-finalised-transactions|The saving stays tied to those impugned Acts and operative conclusion(vi), not every completed transaction under every invalid law.
article31b-not-universal|The reader's unconditional-language explanation must not be treated as universal constitutional immunity.|P15|assessed|L:article31b-limited-shield|The actual PartIIIboundary is tested.
ninth-amending-procedure|Parliament adds Ninth Schedule entries through constitutional amendment, not an ordinary State Act or ordinary majority alone.|P15|assessed|L:ninth-insertion-mechanism|The reader's bare-majority wording is misleading; Article368procedure remains.
precutoff-not-all-immunity|Precutoff protection does not imply immunity from every non-PartIIIconstitutional objection.|P15|partial|L:article31b-limited-shield|No exhaustive pre1973saving question or full doctrine credit is claimed.
postcutoff-presumed-knowledge|The reader explains the cutoff through presumed knowledge of Kesavananda after its date.|P15|held-editorial||Do not substitute a presumed-knowledge theory for the operative judicial rule.
constitutional-enforcement-premise|The reader argues that a supreme written Constitution needs an enforcement institution.|P16|held-editorial||A conceptual justification, not proof that only one institutional design is possible.
countermajoritarian|The criticism concerns unelected judges overriding elected legislation.|P16;P17;T10|assessed|L:countermajoritarian-criticism|The criticism is identified without endorsing illegitimacy or unlimited court power.
constitutional-democracy-answer|Constitutional democracy limits current majorities by prior constitutional commitments.|P17;T10|canonical|R:6.8.1:POL-681-P516-001|Constitutional supremacy is assessed; the philosophical terminology is not an independent extra target.
assembly-democratic-description|The reader describes the Constituent Assembly's adoption as a representative democratic act.|P17|held-editorial-history||Not used to erase qualifications about how the Assembly was constituted or to claim direct universal election.
appointment-collegium-wording|The reader describes judges as appointed through the collegium.|P17|partial|R:7.4.1:POL-741-AT-appointment-authority|Formal appointment is presidential; collegium recommendation is not itself the warrant of appointment.
judicial-removal-check|Judicial tenure is constitutionally protected but removal on the specified grounds/procedure remains possible.|P17;T10|canonical|R:7.4.1:POL-741-AT-removal-grounds;R:7.4.1:POL-741-P291-01|Grounds and voting are separately assessed; source rhetoric about impeachment is not exact terminology.
review-curative-check|The reader gives review and curative proceedings as examples of correction within judicial process.|P17;T10|canonical|R:7.4.1:POL-741-P296-01;R:7.4.1:POL-741-AT-curative-boundary|Specific powers are assessed; no claim that internal review exhausts all accountability questions.
public-accountability-debate|The reader notes continuing disputes about overreach and appointment transparency.|P17;T10|held-normative-debate||Criticism is not independently converted into an established legal finding about every appointment.
tn-april2025|The reader describes an April2025two-judge TamilNadu/Governor judgment imposing assent timelines.|P18|held-dated-primary||No current-law MCQ approved without the complete official judgment and subsequent-reference qualifications.
tn-article142|The reader links that judgment's timelines and deemed assent to Article142.|P18|held-dated-primary||Historical description and present legal effect must be separated.
presidential-reference2025|The reader describes a presidential Article143reference around May2025.|P19|held-dated-primary||Requires official reference text; source notes alone are not current-law certification.
reference-fourteen|The reader gives fourteen questions in the2025reference.|P19|held-dated-primary||A precise current/historical number not independently validated here.
reference-subjects|The described reference concerns justiciability and court-imposed timelines under Articles200/201.|P19|held-dated-primary||Do not replace precise questions/answers with the reader's summary.
reference-five-bench|The reader describes a five-judge Constitution Bench for the2025reference.|P19|held-dated-primary||Article145(3)minimum-five rule is separately supported, but it does not verify this historical bench composition.
reference-bench-names|The reader lists Gavai,SuryaKant,VikramNath,NarasimhaandChandurkar.|P19|held-dated-primary||No name-list question approved merely from this prepared narrative.
reference-hearing-August|The reader says the2025reference hearing began inAugust.|P19|held-dated-primary||Unvalidated event chronology.
reference-November20|The reader dates the advisory opinion to20November2025.|P19|held-dated-primary||No independent date question approved.
surya-next-cji|The reader says SuryaKant became CJI four days after that opinion.|P19|held-dated-primary||Depends on two separately verified dates; no inference counted as source validation.
reference-prelaw-review|The reader summarises a restriction on pre-law justiciability of assent decisions.|P19|held-current-law-qualification||Requires the official opinion's exact answers and limits, not a blanket nonjusticiability rule.
reference-no-timelines|The reader says courts should not prescribe assent timelines.|P19|held-current-law-qualification||Requires exact primary scope; not approved as universal immunity from all inaction review.
reference-no-deemed-assent|The reader says there is no constitutional deemed-assent concept.|P19|held-current-law-qualification||Needs official opinion and relationship to the earlier judgment.
reference-inaction-window|The reader describes limited scrutiny for prolonged unexplained indefinite inaction.|P19|held-current-law-qualification||A narrow window whose precise actor/remedy/conditions need primary validation.
reference-selfcorrecting|The reader calls the advisory reference a self-correcting illustration narrowing an earlier judgment.|P20|held-editorial-current-law||Do not assume an advisory reference is procedurally identical to Article137review or automatically rewrites all inter-partes effects.
reference-layer-only|The reader treats the2025narrative as a current-affairs layer rather than a replacement of the core chapter.|P20|editorial-routing||Preserve as an explicitly qualified layer; not an app MCQ claim.
'''

atoms=[]
for line in DATA.strip().splitlines():
 slug,claim,loc,state,target,qual=line.split('|')
 atoms.append({'id':'LAX27-'+slug,'claim_en':claim,'source_locators':['Prepared Ch27 '+x for x in loc.split(';')],'disposition':state,'assessment_tokens':target.split(';') if target else [],'coverage_qualification':qual,'source_exactness_certified':False})

# The source table has16rows but17named Articles. Every row receives an explicit
# bounded match; a supplied Article number is not independently credited as recall.
table=[
('13','Laws inconsistent with Fundamental Rights are void to the extent specified.','E:POL-751-CH-03','Article13(4)and temporal doctrines are separate qualifications.'),
('32','Supreme Court rights-enforcement route and directions/orders/writs.','E:POL-751-CH-04;R:7.4.1:POL-741-P295-01','Not a general appellate remedy for every legal dispute.'),
('131','Specified federal government-party original jurisdiction.','R:7.4.1:POL-741-P293-01;L:federal-government-party-combinations','A question affecting legal rights and the precise party configurations matter.'),
('132','Constitutional appellate jurisdiction with the relevant High Court certificate.','R:7.4.1:POL-741-AT-constitutional-appeal','Substantial constitutional-interpretation question and Article134Aprocedure qualify the shorthand.'),
('133','Civil appellate jurisdiction with cumulative certificate findings.','R:7.4.1:POL-741-AT-civil-appeal-certificate','General importance plus need for Supreme Court decision, not every civil dispute.'),
('134','Criminal appellate jurisdiction.','L:criminal-constitutional-routes','The new response assesses two direct death-sentence configurations, not every statutory/certificate route.'),
('134A','High Court certificate for the specified Supreme Court appeals.','L:certificate-consideration','Mandatory consideration on the specified oral application is not automatic grant.'),
('135','Continuation of specified residual Federal Court jurisdiction.','L:federal-residual-jurisdiction','Response retrieves Article135; the non133/134,existing-law and until-Parliament-otherwise conditions are supplied in its stem/rationale, not independently recalled.'),
('136','Discretionary special leave, subject to the Armed Forces exclusion.','R:7.4.1:POL-741-AT-specialleave-character;R:7.4.1:POL-741-P294-01','Not confined to final High Court judgments; exclusion is the constitutional law-relating-to-ArmedForces category.'),
('143','Presidential advisory references.','R:7.4.1:POL-741-CH-01;R:7.4.1:POL-741-AT-advisory-two-classes','Distinguish may under143(1)from shall under143(2),and advisory from appellate jurisdiction.'),
('226','High Court writ powers for Fundamental Rights and other lawful purposes.','R:7.4.2:POL-742-CH-01;E:POL-751-CH-04','Territorial/remedial requirements still apply; the other-purposes facet is explicitly assessed by the canonical item.'),
('227','High Court superintendence over courts/tribunals within its territorial jurisdiction.','R:7.4.2:POL-742-P317-01;R:7.4.2:POL-742-P317-02','Armed Forces exclusion and rule/approval conditions qualify broad shorthand; no claim of SCadministrative superintendence over every court.'),
('245','Territorial extent of parliamentary and State laws.','L:territorial-law-range;L:extraterritorial-operation','Territorial range and subject-matter competence are distinct; extra-territorial operation alone is not invalidity.'),
('246','Subject-matter allocation among Union,StateandConcurrent Lists.','L:legislative-lists;L:nonstate-territory','Constitutional priority,246(4)and special provisions qualify ordinary list allocation.'),
('251/254','The reader groups central–State conflicts and calls State law void.','L:article251-temporary;L:concurrent-repugnancy;L:presidential-assent-repugnancy','Conflict corrected:251uses temporary inoperation while parliamentary law has effect;254has its specific Concurrent List rule and254(2)exception.'),
('372','Continuance of pre-Constitution laws.','L:preconstitutional-continuance','Subject to Constitution and competent alteration/repeal/amendment; detailed adaptation powers are not supplied-reader claims or independently assessed here.')]
for article,claim,target,qual in table:
 atoms.append({'id':'LAX27-T3-'+article.replace('/','-'),'claim_en':claim,'source_locators':['Prepared Ch27 table3 Article'+article+'row'],'disposition':'assessed_with_primary_qualification','assessment_tokens':target.split(';'),'coverage_qualification':qual,'source_exactness_certified':False})

# Primary qualifications introduced to make the source table safe are inventoried
# separately. Conditions in a stem remain unassessed rather than receiving credit.
for slug,claim,target,credit,qual in [
('134-reversed-acquittal','Reversed acquittal on appeal followed by death sentence is within134(1)(a).','L:criminal-constitutional-routes','assessed','Joint statement-combination target.'),
('134-withdrawn-trial','High Court withdrawal for its own trial followed by conviction and death sentence is within134(1)(b).','L:criminal-constitutional-routes','assessed','Joint statement-combination target.'),
('134-no-universal-conviction','The two asked clauses do not create automatic appeal for every conviction.','L:criminal-constitutional-routes','assessed','The universal third statement is expressly rejected.'),
('134-parliament-enlargement','Article134(2)allows parliamentary statutory enlargement of criminal appeals.','L:criminal-constitutional-routes','explanation-only','Kept in rationale to avoid an overbroad exclusion; no independent response credit.'),
('134a-oral-trigger','Specified immediate oral application requires determination of certificate eligibility.','L:certificate-consideration','assessed','Mandatory consideration, not grant.'),
('134a-own-motion','A High Court may consider the certificate question on its own motion.','L:certificate-consideration','explanation-only','Not independently chosen by the response.'),
('135-not133134','Article135covers the specified matters to which133and134do not apply.','L:federal-residual-jurisdiction','stem-supplied-unassessed','Article identification is the response; no condition-recall credit.'),
('135-existing-law','The relevant Federal Court powers must have been exercisable under existing law immediately before commencement.','L:federal-residual-jurisdiction','stem-supplied-unassessed','Do not infer independent recall from identification of Article135.'),
('135-until-law','Continuation under135is until Parliament otherwise provides.','L:federal-residual-jurisdiction','stem-supplied-unassessed','The condition is given, not retrieved.'),
('245-parliament-range','Parliament may legislate for the whole or any part of India, subject to Constitution.','L:territorial-law-range','assessed','One half of the assessed pairing.'),
('245-state-range','State Legislature may legislate for the whole or any part of that State, subject to Constitution.','L:territorial-law-range','assessed','Other half of the assessed pairing.'),
('245-extra-operation','Extra-territorial operation alone does not invalidate a parliamentary law.','L:extraterritorial-operation','assessed','No universal foreign-matters power is inferred.'),
('246-union','ListIordinary exclusive legislative allocation is parliamentary.','L:legislative-lists','assessed','One matching association, with constitutional qualifications.'),
('246-state','ListIIordinary allocation is State legislative power, subject to constitutional qualifications.','L:legislative-lists','assessed','Not a rule that Parliament can never legislate on State List matters.'),
('246-concurrent','ListIIIordinary allocation permits both parliamentary and State legislation.','L:legislative-lists','assessed','Priority and special rules remain.'),
('246-nonstate','Parliament may legislate on State List matters for territory not included in a State.','L:nonstate-territory','assessed','Article246(4)target.'),
('251-state-power-remains','Articles249/250do not abolish State legislative power.','L:article251-temporary','assessed','True first statement.'),
('251-limited-temporary','Repugnant State provision is inoperative only to the extent of conflict and while the relevant parliamentary law has effect.','L:article251-temporary','assessed','Temporal/extent proposition is one response-level compound rule, not multiple artificially multiplied questions.'),
('254-general','Ordinary Concurrent List repugnancy favours competent parliamentary law and voids State law only to the conflicting extent, subject to clause2.','L:concurrent-repugnancy','assessed','The exception is expressly excluded by the scenario.'),
('254-assent','Reserved-and-assented qualifying State Concurrent List law may prevail within that State over an earlier central law.','L:presidential-assent-repugnancy','assessed','True first statement with stated statutory requirements.'),
('254-parliament-later','Parliament may later override the State law despite presidential assent.','L:presidential-assent-repugnancy','assessed','The false permanent-bar statement tests this actual proviso.'),
('372-subject-constitution','Pre-Constitution laws continue subject to the Constitution.','L:preconstitutional-continuance','assessed','Continuance is not constitutional immunity.'),
('372-competent-change','Continued law lasts until competent alteration,repealoramendment.','L:preconstitutional-continuance','assessed','A joint continuance rule, not separate three-question credit.')]:
 atoms.append({'id':'LAX27-Q-'+slug,'claim_en':claim,'source_locators':['Prepared Ch27 table3 related row; primary constitutional qualification'],'disposition':credit,'assessment_tokens':[target],'coverage_qualification':qual,'source_exactness_certified':False})

# Every explicit historical table row is decomposed into amendment/year and
# insertion-batch facets. Years are supplied in the matching stems; batch count
# and range are a bundled association, not two independently answered targets.
historical=[
('first','First',1951,13,'1–13','ninth-original-count','before'),
('fourth','Fourth',1955,7,'14–20','ninth-early-additions','before'),
('seventeenth','Seventeenth (reader incorrectly prints Seventh)',1964,44,'21–64','ninth-early-additions','before'),
('twentyninth','Twenty-ninth',1972,2,'65–66','ninth-early-additions','before'),
('thirtyfourth','Thirty-fourth',1974,20,'67–86','ninth-middle-additions','after'),
('thirtyninth','Thirty-ninth',1975,38,'87–124','ninth-middle-additions','after'),
('fortieth','Fortieth',1976,64,'125–188','ninth-middle-additions','after'),
('fortyseventh','Forty-seventh',1984,14,'189–202','ninth-later-additions','after'),
('sixtysixth','Sixty-sixth',1990,55,'203–257','ninth-later-additions','after'),
('seventysixth','Seventy-sixth',1994,1,'257A','ninth-lettered-entry','after'),
('seventyeighth','Seventy-eighth',1995,27,'258–284','ninth-later-additions','after')]
for slug,name,year,count,rng,target,phase in historical:
 loc='Prepared Ch27 table8 '+name+'row'
 atoms.append({'id':'LAX27-T8-'+slug+'-year','claim_en':f'{name} Amendment year:{year}.','source_locators':[loc],'disposition':'stem-supplied-unassessed','assessment_tokens':['L:'+target],'coverage_qualification':'Year is supplied in the stem or named amendment; no independent year-recall credit. First-Amendment1951is also assessed by preservedCH06as an amendment/year option.','source_exactness_certified':False})
 atoms.append({'id':'LAX27-T8-'+slug+'-batch','claim_en':f'{name} Amendment historically added{count}entries,range{rng}.','source_locators':[loc],'disposition':'assessed-bundled-association','assessment_tokens':['L:'+target],'coverage_qualification':('Original13count is retrieved; range1–13is explanatory context.' if slug=='first' else 'Entry257Ais retrieved; the amendment/year is supplied and count1is not an independently selected response.' if slug=='seventysixth' else 'The count/range pair is one matching bundle; no independent double credit for count and range.'),'source_exactness_certified':False})
 atoms.append({'id':'LAX27-T8-'+slug+'-phase','claim_en':f'The stated insertion is{phase}24April1973.','source_locators':[loc],'disposition':'context-unassessed','assessment_tokens':['L:'+target],'coverage_qualification':'The amendment year and before/after grouping supply context; the existing cutoff questions assess the general rule, not independent recall of every row’s phase.','source_exactness_certified':False})

bank=json.loads((P/'Questions.json').read_text(encoding='utf8'))
local={q['id']:q for q in bank['questions']}
canon={};references={};nonresolved=[]
for a in atoms:
 a['assessed_by']=[]
 for token in a.pop('assessment_tokens'):
  if not token:continue
  if token.startswith('L:'):chapter='7.5.1';qid='POL-751-AT-'+token[2:]
  elif token.startswith('E:'):chapter='7.5.1';qid=token[2:]
  else:_,chapter,qid=token.split(':',2)
  if chapter=='7.5.1':q=local.get(qid)
  else:
   if chapter not in canon:
    path=ROOT/chapter.rsplit('.',1)[0]/chapter/'Questions.json'
    canon[chapter]={x['id']:x for x in json.loads(path.read_text(encoding='utf-8-sig'))['questions']}
   q=canon[chapter].get(qid)
  if q is None:nonresolved.append({'claim':a['id'],'chapter':chapter,'id':qid});continue
  a['assessed_by'].append({'chapter':chapter,'id':qid,'fact_ids':q.get('fact_ids',[]),'actual_question_target':q.get('assessment_target',q['question_en'])})
  if chapter!='7.5.1':
   r=references.setdefault((chapter,qid),{'chapter':chapter,'id':qid,'fact_ids':q.get('fact_ids',[]),'assessment_target':q.get('assessment_target',q['question_en']),'inventory_claims':[],'source_refs':[],'new_original_count':0,'review':'Actual stem/options compared read-only. Credit is restricted by each inventory claim’s explicit qualifier; related or supplied context is not automatically assessed.'})
   r['inventory_claims'].append(a['id']);r['source_refs'].extend(a['source_locators'])
 a['independent_assessment_credit']=a['disposition'] in ('assessed','canonical','assessed_with_primary_qualification','assessed-bundled-association','source-conflict-corrected-by-assessment','source-conflict-corrected-canonically','source-qualification-canonical') and bool(a['assessed_by'])
for r in references.values():r['source_refs']=sorted(set(r['source_refs']))
assert not nonresolved,nonresolved

scope={'chapter':'7.5.1','source':'content/polity/g2/references/laxmikanth/chapter-027.html','locators':'English p.eng paragraphs0–20, tables0–10; P/Tare zero-based indices. English explicit claims inventoried; the displayed prepared source is bilingual.','gbk_locked_source_access':0,'notes_access':0,'source_exactness_certified':False,'method':'Manual claim decomposition and actual-response matching. Repeated table summaries point to the same claim; historical batches,years,conditions and editorial/current claims are qualified separately. Counts are inventory records, not proof of exhaustive independent assessment.'}
result={'chapter':'7.5.1','scope':scope,'atomic_claims':atoms,'claim_records':len(atoms),'table3_rows':16,'table3_named_articles':17,'historical_table_rows':11,'full_chapter_coverage':False,'all_explicit_reader_sections_considered':True,'qualification':'Remaining unassessed,stem-supplied,editorial and current-law claims are explicit below. This does not certify source exactness or turn a compound matching response into multiple independently answered questions.'}
(P/'reader-atomic-inventory.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
holds=[a for a in atoms if not a['independent_assessment_credit']]
(P/'reader-held-candidates.json').write_text(json.dumps({'chapter':'7.5.1','status':'not_app_questions','held_or_unassessed_claims':holds,'claim_count':len(holds),'question_candidates':[],'qualification':'Some entries are academically safe but supplied/context-only,not independently assessed. Others require primary or dated-law qualification. None is inserted as an unscored/held object in the normal app bank.','full_chapter_coverage':False,'source_exactness_certified':False},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
old={(r['chapter'],r['id']):r for r in bank.get('question_references',[])}
for k,r in references.items():
 if k in old:
  old[k]['inventory_claims']=sorted(set(old[k].get('inventory_claims',[])+r['inventory_claims']))
  old[k]['inventory_coverage_qualification']='See reader-atomic-inventory.json; supplied context and broader background do not gain independent assessment credit.'
 else:old[k]=r
bank['question_references']=list(old.values())
bank['full_chapter_coverage']=False
(P/'Questions.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
from collections import Counter
report={'chapter':'7.5.1','source_scope':scope,'claim_records':len(atoms),'dispositions':dict(Counter(a['disposition'] for a in atoms)),'canonical_references_total':len(old),'unresolved_references':nonresolved,'new_normal_questions':26,'total_normal_questions':len(bank['questions']),'independent_review':'../../_parallel/unit7/second-review-751-reader-expansion.json','review_application':'reader-review-application.json','source_conflicts':['Table3:16rows name17Articles;251/254are grouped.','Article251temporary inoperation must be distinguished from254voidness and254(2)exception.','Table8Seventh1964is corrected to Seventeenth1964in study content only.','India-never-reasonableness comparison is corrected through canonical Maneka questions.','Bare-majority/State-insertion narrative must not replace Article368constitutional amendment.','S.S.Bola bibliographic/speaker claim remains held.'],'existing_ids_removed':[],'potential_existing_overlap_not_retired':[{'local':'POL-751-CH-06','related_canonical':'6.7.1/POL-671-N001','qualification':'Existing local ID preserved. Canonical item adds PMassociation beyond this source claim; retirement/alias handoff is coordinator-owned.'},{'local':'POL-751-P298-01','related_canonical':'6.7.1/POL-671-N006','qualification':'Existing case-identification response retained; source doctrine and basic-structure limits overlap but response targets differ.'}],'remaining_gates':['Locked GBK/source exactness is not certified by this prepared-reader inventory.','Current2025assent-reference narrative requires full primary and temporal qualification before study questions.','Unverified speaker/motive/comparative assertions remain held.','Stem-supplied years and Article135conditions remain unassessed; matching count/range bundles receive only joint response credit.'],'full_chapter_coverage':False,'unit_complete':False,'ui_testing':False}
(P/'reader-coverage-reconciliation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Claim records',len(atoms),'not independently assessed',len(holds),'canonical references',len(old))
