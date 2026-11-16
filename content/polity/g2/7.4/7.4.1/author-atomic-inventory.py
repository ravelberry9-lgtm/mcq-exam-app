"""Explicit manual claim inventory, not an extraction/coverage-completion algorithm."""
import json
from pathlib import Path
P=Path(__file__).parent
# claim | match against supplied Ch26 | exact prepared-reader locator | disposition | question target (if genuinely assessed)
DATA={
286:"""
Cornwallis described as father of Indian judiciary|absent|none|held-primary-history|
Calcutta Supreme Court under Regulating Act1773 began1774|absent|none|canonical|6.1.3:POL-6.1.3-P13-17
Federal Court arose under Government of India Act1935 and functioned1937|direct|paragraphs0,2|canonical|6.1.3:POL-613-P23-14
Supreme Court inauguration28January1950 distinguished from commencement26January|direct|paragraph2|approved|POL-741-AT-inauguration
Supreme Court replaced Federal Court and Privy Council appellate role|direct|paragraph2|held-unassessed|
Union judiciary PartVChapterIVArticles124–147|direct|paragraph2|approved|POL-741-AT-constitutional-location
Supreme Court motto whence law thence victory|absent|none|held-primary-history|
Building architect Ganesh Bhikaji Deolalikar|absent|none|primary-verified-unassessed|
India has a single integrated judicial hierarchy|direct|paragraphs0–1|held-unassessed|
Supreme Court administratively supervises all courts blanket assertion|conflict|paragraph1 repeats overstatement; contrast Articles227,235|held-source-error|
Composition Article1241 CJI plus Parliament-prescribed other judges|direct|paragraph3|existing|POL-741-P286-01
Parliament may enlarge number of Supreme Court judges by law|direct|paragraph3|canonical|6.7.1:POL-671-P510-002
""",
287:"""
April2024 sanctioned34 judges is a dated count|direct|paragraph3; later prepared notes conflict at38|held-dated|
Original sanctioned strength8 comprisingCJIand7others|direct|paragraph3|held-unassessed|
1956 sanctioned total11|direct|paragraph3|held-historical-detail|
1960 sanctioned total14|direct|paragraph3|held-historical-detail|
1977 sanctioned total18|direct|paragraph3|held-historical-detail|
1986 sanctioned total26|direct|paragraph3|held-historical-detail|
2008 sanctioned total31|direct|paragraph3|held-historical-detail|
2019 sanctioned total34|direct|paragraph3|held-historical-detail|
President appoints judges by warrant hand and seal1242|direct|paragraph5|approved|POL-741-AT-appointment-authority
CJI appointment follows seniority convention rather than express constitutional seniority text|direct|paragraphs10–11|held-primary-and-qualification|
1973ANRay supersession of Shelat Hegde Grover|direct|paragraph10|held-primary-history|
1977MHBeg supersededHRKhanna|direct|paragraph11|held-primary-history|
ADMJabalpur1976Khanna dissent|partial|paragraph11 context|held-primary-history|
OutgoingCJI recommendation travels viaLawMinisterPMPresidentGazette|partial|paragraphs10–11 do not establish all steps|held-administrative-procedure|
ActingCJI126President selects otherSCjudge on vacancy or inability|direct|paragraph20|approved|POL-741-AT-acting-cji
Adhoc127quorum deficiency and priorPresidentconsent andHCchiefconsult|direct|paragraph21|approved|POL-741-AT-adhoc-conditions
""",
288:"""
AdhocHCjudge must qualify forSCappointment|direct|paragraph21|explanation-support-only|POL-741-AT-adhoc-conditions
Adhocjudge gives priority toSCattendance and hasSCprivileges|direct|paragraph21|held-unassessed|
Retiredjudge128requiresPresidentandpersonconsents|direct|paragraph22|approved|POL-741-AT-retired-attendance
Retiredjudge while sitting hasSCpowers but nototherwiseSCjudge|direct|paragraph22|explanation-support-only|POL-741-AT-retired-attendance
Retiredjudge allowances fixed byPresident|direct|paragraph22|held-unassessed|
FirstJudgesCase source1982 versusSPGupta1981|conflict|paragraph6 gives1981|held-source-date-error|
FirstJudgesCase consultation notconcurrence|direct|paragraph6|held-primary-history|
SecondJudgesCase1993concurrence andCJIconsults2seniors|direct|paragraph6|held-primary-history|
ThirdJudgesCase1998CJIconsults4seniorSCjudges|direct|paragraph6|held-primary-history|
Twoadversecollegiumopinions prevent recommendation|direct|paragraph6|held-primary-precise-scope|
Noncompliantconsultationrecommendationnotbinding|direct|paragraph6|held-primary-precise-scope|
Collegium criticisms lacktransparency favouritism|partial|paragraphs8–9 explanatoryanalysis|held-normative-not-bare-fact|
NJAC99thAmendment2014historicalproposal notcurrentappointmentmechanism|direct|paragraph7|canonical|6.8.1:POL-681-P517-003
NJACBill passage13and14August2014|absent|none|held-primary-history|
""",
289:"""
NJACconstitutionalinvalidity16October2015|direct|paragraph7|canonical|6.8.1:POL-681-P517-003
NJACinvalidityrestoredcollegium|direct|paragraph7|canonical|6.8.1:POL-681-P517-003
ListedNJACbenchmembers andChelameswardissent|partial|paragraph7 nofullbenchlist|held-primary-history|
CurrentCJISuryaKantreviewannouncement|absent|none|held-current-unverified|
MoP1998historicalattribution|partial|paragraph6 consultationhistorynotMoPtext|held-primary-history|
Invalidated124ANJACsixmembersCJI2seniorsLawMinister2eminent|partial|paragraph7 generalNJAConly|held-historical-detail|
InvalidatedNJACeminentselectionPMCJILOP|absent|none|held-historical-detail|
InvalidatedNJAConeeminentSCSTOBCminorityorwoman|absent|none|held-historical-detail|
InvalidatedNJACeminent3yearnonrenewabletenure|absent|none|held-historical-detail|
Invalidated124BNJACappointmentsandtransfersfunctions|partial|paragraph7|held-historical-detail|
""",
290:"""
InvalidatedNJACtwomemberveto|absent|none|held-historical-detail|
InvalidatedNJACdifferentHCconsultationprocedure|absent|none|held-historical-detail|
99thAmendmentadded124ABCandchangedlistedjudicialarticles|partial|paragraph7|held-historical-detail|
SCqualificationIndian citizenship|direct|paragraph12|existing|POL-741-P290-01
SCqualification5yearsHCjudge|direct|paragraph12|existing|POL-741-P290-01
SCqualification10yearsHCadvocate|direct|paragraph12|existing|POL-741-P290-01
SCqualificationdistinguishedjuristPresidentopinion|direct|paragraph12|existing|POL-741-P290-01
No minimum appointment age in1243|direct|paragraph12|approved|POL-741-AT-no-minimum-age
1242AagedisputedeterminationParliamentmayprovidebylaw|absent|none|held-primary-unassessed|
15thAmendment1963inserted1242A|absent|none|held-primary-history|
SourceassertsSCsettlesownagedispute without clear statutorymechanism|absent|none|held-primary-qualification|
""",
291:"""
JudgeoathPresidentorappointeeThirdSchedule1246|direct|paragraph13|approved|POL-741-AT-oath-authority
OathfaithConstitutionsovereignty integrity fearfavouraffectionillwill|direct|paragraph13|held-unassessed|
SCretirement65|direct|paragraph15|approved|POL-741-AT-tenure-resignation
SCresignationwrittenPresident|direct|paragraph15|approved|POL-741-AT-tenure-resignation
Removalsame-sessionaddressesbyeachHousespecialdualmajority|direct|paragraph16|existing|POL-741-P291-01
Removalgroundsprovedmisbehaviourorincapacity|direct|paragraph16|held-unassessed|
Sourcecensure/impeachmentterminologynotexactArticle1244language|partial|paragraph16 constitutionalremoval|held-source-terminology|
JudgesInquiryAct1968notice100LS50RS|direct|paragraph17|approved|POL-741-AT-inquiry-notice
SpeakerChairmayadmit/refusenotice|direct|paragraph17|explanation-support-only|POL-741-AT-inquiry-notice
Inquirycommitteethreeprescribedcategories|direct|paragraph17|approved|POL-741-AT-inquiry-committee
Sourceconfusingtotalmembershiplesshalf removalwording|conflict|paragraph16 correctdualmajority|held-source-error|
EffectofLSdissolutiononremovalnotice|absent|none|held-statute-qualification|
Ramaswamiproceedings1991–1993andfailedmotion|partial|paragraphs18–19 containoutdatedonly-attemptclaim|held-history-and-current-qualification|
""",
292:"""
Karnan2017contemptsixmonthsentence|absent|none|held-primary-history|
ParliamentdeterminesSCjudgesalaries125|direct|paragraph14|canonical|6.7.1:POL-671-P509-002
SCsalaryfinancialemergencyexception|direct|paragraph14|held-primary-and-exact-rights-scope|
2018salaryCJI280000other250000|direct|paragraph14|held-dated-money|
SeatDelhiotherplacesCJIwithPresidentapproval130|direct|paragraph23|approved|POL-741-AT-seat
Originalappellateadvisoryrecordwritreviewclassification|direct|paragraph28|existing-partial-coverage|POL-741-P293-01
""",
293:"""
131specifiedUnionStateStatelegalrightsdisputes|direct|paragraphs30–31|existing|POL-741-P293-01
PrivateindividualsnotArticle131parties|direct|paragraph31|held-unassessed|
SourceplacesFRenforcementin131althoughproperroute32|conflict|paragraphs30–34|held-source-error|
SourceplacesPresidentVPelectionin131althoughproperArticle71|conflict|paragraph48|held-source-error|
131provisopreconstitutiontreatydisputesexcluded|direct|paragraph31|held-unassessed|
Interstateriverwaterjurisdictionmaybestatutorilyexcludedunder262|direct|paragraph31|held-exact-statutory-scope|
FinanceCommissionadjustmentsandexpenditurepensionexclusions|direct|paragraph31|held-exact-statutory-scope|
FirstoriginalWestBengalUnion1961coalcase|direct|paragraph31|held-primary-history|
132constitutionalinterpretationHCcertificate134A|direct|table11 constitutionalappeals|approved|POL-741-AT-constitutional-appeal
133civilappealtwocumulativecertificatefindings|direct|table11 civilappeals|approved|POL-741-AT-civil-appeal-certificate
134HCacquittalreversalandsentenceofdeath|direct|table11 criminalappeals|held-unassessed|
""",
294:"""
Openingcriminalappealwordingambiguousacrosspagecontinuation|conflict|table11 criminalappeals|held-source-text-ambiguity|
1970Actextendscriminalappealslifeor10yearswithspecifiedHCproceduralroute|direct|table11 criminalappeals|held-primary-and-unassessed|
136specialleaveisdiscretionarynotappealasofright|direct|paragraphs36–37|held-unassessed|
136mayreachfinalorinterlocutoryjudgmentnotonlyHC|direct|paragraphs36–37 table11|held-unassessed|
1362armedforcescourttribunalexception|direct|table11 criminalappeals|existing|POL-741-P294-01
1431Presidentpublicimportancelaworfactreference|direct|paragraph38|existing|POL-741-CH-01
1431mayreport1432shallreport|direct|paragraph38|approved|POL-741-AT-advisory-two-classes
1432preconstitutioninstrumentdisputes131proviso|direct|paragraph38|approved|POL-741-AT-advisory-two-classes
AdvisoryopinionnotbindingPresident|direct|paragraph38|held-unassessed|
Alladvisoryopinionsbindingalllowercourtsblanketclaim|partial|paragraph40 caveatsrequired|held-legal-qualification|
Source17referencesversuspreparedreader15references|conflict|paragraph39 table13|held-dated-list-conflict|
1951DelhiLaws1958KeralaEducation1960Berubarireferences|direct|table13|held-partly-canonical|6.4.1:POL-6.1.9-P118-10
1963SeaCustomsreference|direct|table13|held-primary-history|
""",
295:"""
1964KeshavSinghreference|direct|table13|canonical|6.4.1:POL-6.1.9-P121-11
1974PresidentialElection1978SpecialCourtsreferences|direct|table13|held-primary-history|
1992Cauvery1993Ayodhyareferences|direct|table13|held-primary-history|
1998judgesconsultationreference|direct|table13|held-primary-history|
2001referenceunreadablename|absent|none|held-unreadable|
2002Gujaratpoll2004Punjabwater2012naturalresourcesreferences|direct|table13|held-primary-history|
2006officeprofit2016NEET2025assentreferencelistitems|absent|table13 noadequatematch|held-primary-and-dated-list|
129courtofrecordcontempt|direct|paragraph41|existing|POL-741-P295-02
Recordedjudgmentsasevidenceandprecedents|direct|paragraph41|held-unassessed|
1971ContemptActcivilversuscriminaldefinitions|direct|paragraph42|held-primary-and-unassessed|
Fairreasonablecriticismnotcontempt|direct|paragraph42|held-primary-and-unassessed|
Statutorysixmonths2000rupeescapblanketSCclaim|partial|paragraph42 repeatscap withoutconstitutionalqualification|held-legal-qualification|
KarnanPrashantBhushancontemptexamples|absent|none|held-primary-history|
32fivewritsforFR|direct|paragraphs32–34|existing|POL-741-P295-01
""",
296:"""
137reviewownjudgment|direct|paragraph46|existing|POL-741-P296-01
Reviewnormally30daysandsamebenchsubjectrules|direct|paragraph46|held-rules-exceptions-unassessed|
Sourceequateslaterbenchprecedentoverrulingwith137review|conflict|paragraph46 contrastreview|held-source-error|
2018SCSTreviewexampleandGolakKesavanandasequence|partial|paragraph46 doesnotvalidateallcaseclaims|held-primary-history|
Curativeexceptionafterreviewdismissal|direct|paragraph46|approved|POL-741-AT-curative-boundary
CurativecaseRupaAshokHurra2002sourceincompletename|conflict|paragraph46 andprimary2024judgment|approved-corrected-study-only|POL-741-AT-curative-boundary
138enlargementUnionListbyParliament|direct|paragraph48|held-unassessed|
1382CentreStateagreementplusParliamentlaw|direct|paragraph48|held-unassessed|
139additionalwritjurisdictionbyParliament|direct|paragraph48|canonical|6.7.1:POL-671-P510-002
139Acommonquestioncasewithdrawalandtransferconditions|direct|paragraph48|held-primary-and-unassessed|
141lawdeclaredbindingcourts|direct|paragraph48|canonical|6.8.1:POL-681-P514-005
142completejusticependingcauseormatter|direct|paragraph48|canonical|6.8.1:POL-681-P514-005
144civiljudicialauthoritiesactinaid|direct|paragraph48|approved|POL-741-AT-aid-authorities
""",
297:"""
145practiceprocedurerulesPresapprovalsubjectParliamentlaw|direct|paragraph24|approved|POL-741-AT-rules-approval
1453minimumfiveconstitutionalinterpretationor143reference|direct|paragraph24|existing|POL-741-CH-02
146staffappointmentsCJIwithconstitutionaldelegationqualification|direct|paragraph27|approved|POL-741-AT-staff-appointment
1462financialservicerulesPresapprovalnotallstaffmatterblanket|partial|paragraph27 summarisespower|held-unassessed-qualification|
1463adminexpenseschargedUnionfund|direct|paragraph27|approved|POL-741-AT-administrative-charge
Severabilitydoctrine|direct|paragraph47|canonical|6.4.1:POL-6.1.9-P94-04
Pithandsubstancedoctrine|direct|paragraph47|canonical|7.5.1:POL-751-P297-DOCTRINE-01
Waiverandeclipsedoctrines|direct|paragraph47|held-canonical-match-pending|
Constitutionalmoralitylegislativecompetenceotherdoctrinelist|partial|paragraph47 notallGBKlabels|held-atomic-definition-needed|
71PresidentVPelectiondisputes|direct|paragraph48|held-unassessed|
317PSCmisconductinquiryPresidentreferenceSCreport|direct|paragraph48|held-unassessed|
Judicialreviewvaliditymeaning|direct|paragraph44|canonical|7.5.1:POL-751-P297-01
JudicialreviewprotectsFRfederalismsupremacy|direct|paragraph44|canonical|7.5.1:POL-751-CH-02
MarburyMadison1803Marshallhistory|partial|paragraph44 doesnotestablishallhistory|held-primary-history|
13inconsistentlawsvoidtotheextent|direct|paragraph44|canonical|7.5.1:POL-751-CH-03
KMMunshiquotationattribution|absent|none|held-primary-quote|
""",
298:"""
Threepurposesofjudicialreview|direct|paragraph44|canonical|7.5.1:POL-751-CH-02
Threecategoriesamendmentlegislationadministrativeaction|direct|paragraph44|canonical|7.5.1:POL-751-CH-01
JudicialreviewgroundsFRcompetenceconstitutionalrepugnancy|direct|paragraph44|canonical|7.5.1:POL-751-CH-05
Listedinterpretivedoctrinesneedindividualdefinitionsnotnamesonly|partial|paragraph47|held-atomic-definition-needed|
AKGopalandate1951sourceerroractual1950|absent|none|held-source-date-error|
GolakNathamendmentofFRnotallamendments|partial|paragraph47 prospectiveoverrulingonly|held-primary-and-qualification|
Banknationalisationprivypursecaseyearsandclaims|absent|none|held-source-history-error|
""",
299:"""
Kesavanandabasicstructurelimitation|direct|paragraph44|canonical|7.5.1:POL-751-P298-01
Kesavananda13judges7to6notninejudge majority|absent|none|held-source-majority-error|
MinervaMillsslimitedamendingpower1980|partial|paragraph44 reviewbasicstructure|held-canonical-match-pending|
Bommai1994secularismbasicstructure|absent|none|held-canonical-match-pending|
LChandraKumar1997not1994|absent|none|canonical-corrected-study-only|7.4.4:POL-744-P329-01
NJACinvalid2015not2016|direct|paragraph7|canonical-corrected-study-only|6.8.1:POL-681-P517-003
USreviewunlimitedIndianreviewlimitedblanketclaim|conflict|paragraph45 table17 alsooverbroad|held-comparative-qualification|
NinthSchedule24April1973not1994cutoff|absent|none|canonical-corrected-study-only|7.5.1:POL-751-CH-07
74(2)163(3)adviceinquirybarnotblanketactionimmunity|absent|none|held-primary-and-qualification|
122212mereproceduralirregularitybarnotallillegality|absent|none|held-primary-and-qualification|
105194privilegesnotblanketjudicialreviewexclusion|absent|none|held-primary-and-qualification|
""",
300:"""
Article212legislativeproceedingreviewexclusionoverbroad|absent|none|held-primary-and-qualification|
Article361personalimmunitiesnotunreviewablegovernmentaction|absent|none|held-primary-and-qualification|
Article392historicaldifficultyremovalnotblanketreviewbar|absent|none|held-primary-and-qualification|
CJIadministersPresidentoathArticle60|absent|none|held-canonical-match-pending|
CJIactsasPresidentondoublevacancyunder1969Act|absent|none|held-canonical-match-pending|
2018AsokPandeymasterofroster|absent|none|held-primary-history|
CJIhasnospecialconstitutionalpowerblanketassertion|conflict|paragraph27andArticle146|held-source-error|
""",
301:"""
Securityoftenureuntilconstitutionalretirementage|direct|paragraph25|approved-partial|POL-741-AT-tenure-resignation
Salarynonvariationfinancialemergencyqualification|direct|paragraph14|held-exact-rights-scope|
121Parliamentconductdiscussionremovalexception|direct|paragraph27|approved|POL-741-AT-parliament-conduct
211Statelegislaturehasnosame-textremovalexception|partial|paragraph27 doesnotlicenseGBKconflation|held-source-error|
1247SCpostretirementpracticebarallcourtsauthoritiesIndia|direct|paragraph27|approved|POL-741-AT-postretirement-practice
220retiredpermanentHCjudgepracticeonlySCandotherHC|conflict|paragraph27contrastsSCbar butGBKanyothercourtwrong|held-source-error|
PostretirementgovernorshipFazlAliFatimaBeeviSathasivamNazeerexamples|absent|none|held-primary-history|
Postretirementelectioneligibilitynotblanketunqualified|absent|none|held-primary-qualification|
129215contemptsafeguard|direct|paragraph27|existing|POL-741-P295-02
UnnamedIASofficercontemptexample|absent|none|held-unreadable|
USlackadvisoryjurisdictioncomparison|direct|table17|held-US-primary-unassessed|
ParliamentenlargesIndiaSCjurisdictioncomparison|direct|table17|held-unassessed|
USnoconstitutionallimitsorunlimitedreviewclaim|conflict|table17repeatsoverstatement|held-comparative-qualification|
""",
302:"""
SCadministrativesuperintendenceHCblanketclaim|conflict|paragraph1alsorepeatsoverstatement|held-source-error|
IndiaSCoriginaljurisdictionnotlimitedfederaldisputes|direct|paragraphs28,32,48|held-unassessed|
Activismdefinitioncreativeprotectionofrights|absent|Ch26; suppliedCh28supplement|canonical|7.6.1:POL-761-P302-01
Schlesinger1947termandjudicialdynamism|absent|Ch26; suppliedCh28supplement|canonical|7.6.1:POL-761-CH-01
SuomotuPILaccessasactivistforms|absent|Ch26; suppliedCh28supplement|canonical|7.6.1:POL-761-CH-03
ActivistArticles14,19,21|absent|Ch26; suppliedCh28supplement|canonical|7.6.1:POL-761-CH-04
Sourcelistedactivismbeneficiariesandcaseexamples|absent|Ch26|held-specific-case-primary|
""",
303:"""
Executivefailureorlegislativevacuumcanjustifyactiverole|absent|Ch26; suppliedCh28supplement|canonical|7.6.1:POL-761-CH-05
Permanentpolicyadministrationjudicialoverreachconcern|absent|Ch26; suppliedCh28supplement|canonical|7.6.1:POL-761-P303-01
Restraintrespectsinstitutionalboundariesnotabdication|absent|Ch26; suppliedCh28supplement|canonical|7.6.1:POL-761-CH-08
Separationofpowersargumentagainstoverreach|absent|Ch26; suppliedCh28supplement|canonical|7.6.1:POL-761-CH-07
AravaliGolfClub2007restraintcaseexample|absent|Ch26|held-primary-history|
Otherdatedactivismcaseexamplesandbroadcriticisms|absent|Ch26|held-specific-case-primary|
""",
304:"""
PILrelaxesstandingforgenuinepublicwrong|absent|Ch26; suppliedCh29supplement|canonical|7.6.2:POL-762-P304-01
PIL32and226routes|partial|paragraphs32–34writroutesnotPILstanding|canonical|7.6.2:POL-762-CH-02
Lettersasepistolaryjurisdiction|absent|Ch26; suppliedCh29supplement|canonical|7.6.2:POL-762-CH-03
Goodfaiththirdpartyforpersonswithoutaccess|absent|Ch26; suppliedCh29supplement|canonical|7.6.2:POL-762-CH-05
SPGuptainitialsorcaseattributionunreadablespan|absent|Ch26|held-unreadable|
CrPC133districtcourtPILgeneralisation|absent|Ch26|held-source-legal-ambiguity|
USoriginPILassertionoversimplified|absent|Ch26|held-primary-history|
SocialactionlitigationalternatePILname|absent|Ch26; suppliedCh29supplement|canonical|7.6.2:POL-762-CH-01
""",
305:"""
PILprivateinterestunsuitable|absent|Ch26; suppliedCh29supplement|canonical|7.6.2:POL-762-CH-06
MalafidePILrejectandcosts|absent|Ch26; suppliedCh29supplement|canonical|7.6.2:POL-762-CH-07
PleaBargaining2006notapplicabletoallcrimes|absent|Ch26|held-current-statute-and-scope|
Judicialbehaviourparagraphmissingwords|absent|Ch26|held-unreadable|
SocialJusticeBench2014compositionanddates|absent|Ch26|held-primary-history|
""",
306:"""
JudicialStandardsAccountabilityBill2010wasproposalnotcurrentAct|absent|Ch26|held-historical-bill-not-law|
Billassetdeclarationproposal|absent|Ch26|held-historical-bill-not-law|
Billcomplaintoversightproposal|absent|Ch26|held-historical-bill-not-law|
Billjudicialstandardsproposal|absent|Ch26|held-historical-bill-not-law|
BillproposedreplacementInquiryAct1968|absent|Ch26|held-historical-bill-not-law|
Billlistremainingambiguousorclippedspan|absent|Ch26|held-unreadable|
GramNyayalayasAct2008commencement2October2009|absent|Ch26; suppliedCh38supplement|held-primary-and-unassessed|
StateGovconsultHCappointsNyayadhikari|absent|Ch26; suppliedCh38supplement|held-primary-and-unassessed|
GramNyayalayasmobilelowcostruralaccess|absent|Ch26; suppliedCh38supplement|held-primary-and-unassessed|
GramNyayalayascivilcriminaljurisdiction|absent|Ch26; suppliedCh38supplement|held-exact-statutory-scope|
Two-yearand20000rupeelimitsasprinted|absent|Ch26|held-dated-or-overbroad-statutory-scope|
""",
307:"""
GramNyayalayaevidentiaryflexibilitynaturaljustice|absent|Ch26; suppliedCh38supplement|held-current-statute-and-scope|
GramNyayalayacriminalappealSessionscivilappealDistrictCourt|absent|Ch26; suppliedCh38supplement|held-source-overbroad-appeal|
LokAdalatfirstGujarat1982history|absent|Ch26; suppliedCh38supplement|held-primary-history|
39Aequaljusticefreelegalaid|absent|Ch26; suppliedCh38supplement|canonical|7.4.4:POL-744-P307-01
LegalServicesAuthoritiesAct1987framework|absent|Ch26; suppliedCh38supplement|canonical|7.4.4:POL-744-CH-01
LokAdalatsettlementawardfinalbindingnotordinaryappeal|absent|Ch26; suppliedCh38supplement|canonical|7.4.4:POL-744-P307-02
LokAdalatnoncompoundableoffenceexception|absent|Ch26; suppliedCh38supplement|canonical|7.4.4:POL-744-CH-02
PermanentLokAdalat2002conditionalmeritsjurisdiction|absent|Ch26; suppliedCh38supplement|canonical|7.4.4:POL-744-CH-03
PermanentLokAdalatpublicutilitywordingspanunreadable|absent|Ch26|held-unreadable|
""",
308:"""
LokAdalateligiblependingandprelitigationcases|absent|Ch26; suppliedCh38supplement|held-unassessed|
LokAdalatnofeerefundbenefits|absent|Ch26; suppliedCh38supplement|held-unassessed|
LokAdalatsettlementfinality|absent|Ch26; suppliedCh38supplement|canonical|7.4.4:POL-744-P307-02
Sourcebreachallowingordinaryappealclaim|absent|Ch26|held-source-error|
FastTrackCourts2000EleventhFinanceCommissionhistory|absent|Ch26; suppliedCh38supplement|held-primary-history|
FastTrackdatedcourtcounts|absent|Ch26|held-dated-statistics|
FamilyCourtsAct1984StateGovconsultHCestablishment|absent|Ch26; suppliedCh38supplement|held-primary-and-unassessed|
FamilyCourtsconciliationfocus|absent|Ch26; suppliedCh38supplement|held-primary-and-unassessed|
FamilyCourtappealHCsubjectstatutoryexceptions|absent|Ch26; suppliedCh38supplement|held-exact-statutory-scope|
FamilyCourtlegalrepresentationnotasofrightnotabsoluteban|absent|Ch26; suppliedCh38supplement|held-source-qualification|
FamilyCourtsdatedcounts|absent|Ch26|held-dated-statistics|
Constitutionbenchatleast5Article1453|direct|paragraph24|existing|POL-741-CH-02
""",
309:"""
Divisionbenchsourceatleast3contrastsSCrulesnormalminimum2|absent|Ch26|held-source-error-and-rules-primary|
Fullbenchmeansalljudgesblanketclaim|absent|Ch26|held-source-error|
Kesavananda13judgebench|absent|Ch26|held-canonical-match-pending|
SenioradvocatesdesignationSCorHC|absent|Ch26|held-primary-rules-unassessed|
AdvocateonRecordfilingactingrequirements|absent|Ch26|held-primary-rules-unassessed|
OrdinaryadvocateappearanceAoRinstructionqualification|absent|Ch26|held-primary-rules-unassessed|
Justiceclocksannouncement26November2017|absent|Ch26|held-primary-history|
SourceNationalJusticeDaylabelversusConstitutionDay|absent|Ch26|held-source-label-error|
2026pendencySC59000HC6300000subordinate46000000|absent|Ch26|held-dated-statistics|
""",
310:"""
FemalejudgepercentagesSC12HC13lower35|absent|Ch26|held-dated-statistics|
JudgespopulationratiosFrance124US108Australia40India17|absent|Ch26|held-dated-statistics|
Governmentlitigation46percent|absent|Ch26|held-dated-statistics|
FirstCJIHarilalKania|partial|paragraph2 nofullCJIlist|held-primary-history|
SecondCJIMPatanjaliSastri|absent|Ch26|held-primary-history|
SuryaKant53rdCJIfrom24November2025currentclaim|absent|Ch26|held-current-claim|
FatimaBeevifirstwomanSCjudgewrongprintedtenuredates|absent|Ch26|held-source-date-error|
YVChandrachudlongestCJItenureduration|absent|Ch26|held-primary-history|
BPSinhasecondlongestCJItenure|absent|Ch26|held-primary-history|
BVNagarathnafutureCJI2027projection|absent|Ch26|held-projection|
KNSinghshortestCJI18daysandageclaim|absent|Ch26|held-primary-history|
KSubbaraoNVRamanaAndhraCJIclaims|absent|Ch26|held-primary-history|
KGBalakrishnanwrongprintedtenure2017–20|absent|Ch26|held-source-date-error|
BRGavaireligionidentityclaim|absent|Ch26|held-primary-and-relevance|
IndiracaseVRIyernameinitialsattributionambiguity|absent|Ch26|held-source-history-ambiguity|
""",
311:"""
IAMCHHyderabadinauguration21December2021asprinted|absent|Ch26|held-date-conflict-primary-needed|
IAMCHfoundersandlifetrusteesnames|absent|Ch26|held-dated-organisational-detail|
SCLivestream27September2022|absent|Ch26|held-primary-history|
SwapnilTripathi2018livestreamaccessjudgment|absent|Ch26|held-primary-history|
GujaratthenKarnatakaHClivestreamsequence|absent|Ch26|held-primary-history|
17July2021programmeversusSCfirstlivestreamambiguity|absent|Ch26|held-source-date-context-ambiguity|
"""
}
UPDATES={
'India has a single integrated judicial hierarchy':('approved','POL-741-AT-integrated-hierarchy'),
'Adhocjudge gives priority toSCattendance and hasSCprivileges':('approved','POL-741-AT-adhoc-priority'),
'1242AagedisputedeterminationParliamentmayprovidebylaw':('approved','POL-741-AT-age-determination-law'),
'138enlargementUnionListbyParliament':('approved','POL-741-AT-union-list-enlargement'),
'1462financialservicerulesPresapprovalnotallstaffmatterblanket':('approved','POL-741-AT-staff-financial-rules'),
'Removalgroundsprovedmisbehaviourorincapacity':('approved','POL-741-AT-removal-grounds'),
'PrivateindividualsnotArticle131parties':('approved','POL-741-AT-original-private-party'),
'136specialleaveisdiscretionarynotappealasofright':('approved','POL-741-AT-specialleave-character'),
'136mayreachfinalorinterlocutoryjudgmentnotonlyHC':('approved','POL-741-AT-specialleave-character'),
'1382CentreStateagreementplusParliamentlaw':('approved','POL-741-AT-enlargement-agreement'),
'139Acommonquestioncasewithdrawalandtransferconditions':('approved','POL-741-AT-common-question-withdrawal'),
'GramNyayalayasAct2008commencement2October2009':('approved','POL-741-AT-gram-commencement'),
'StateGovconsultHCappointsNyayadhikari':('approved','POL-741-AT-gram-appointment'),
'GramNyayalayasmobilelowcostruralaccess':('approved','POL-741-AT-gram-mobile-scope'),
'GramNyayalayascivilcriminaljurisdiction':('approved','POL-741-AT-gram-mobile-scope'),
'GramNyayalayacriminalappealSessionscivilappealDistrictCourt':('approved-corrected-study-only','POL-741-AT-gram-appeal-routes'),
'FamilyCourtsAct1984StateGovconsultHCestablishment':('approved','POL-741-AT-family-establishment'),
'FamilyCourtsconciliationfocus':('approved','POL-741-AT-family-settlement'),
'FamilyCourtappealHCsubjectstatutoryexceptions':('approved','POL-741-AT-family-appeal-boundary'),
'FamilyCourtlegalrepresentationnotasofrightnotabsoluteban':('approved-corrected-study-only','POL-741-AT-family-representation'),
}
atoms=[];refs={}
local={x['id']:x for x in json.loads((P/'Questions.json').read_text(encoding='utf8'))['questions']}
root=P.parents[2]
allq={}
for file in root.rglob('Questions.json'):
    d=json.loads(file.read_text(encoding='utf-8-sig'))
    for item in d.get('questions',[]): allq[(file.parent.name,item['id'])]=item
for page,block in DATA.items():
    for j,line in enumerate(block.strip().splitlines(),1):
        claim,match,loc,disposition,target=line.split('|')
        if claim in UPDATES:disposition,target=UPDATES[claim]
        if claim.startswith('146staffappointments'):loc='Independence numbered safeguard8; table9 (delegation qualified from primaryArticle1461)';match='partial'
        if claim.startswith('1463adminexpenses'):loc='Independence numbered safeguard4; table9'
        if claim.startswith('121Parliamentconduct'):loc='Independence numbered safeguard5'
        if claim.startswith('211Statelegislature'):loc='Independence numbered safeguard5 does not add a State-legislature removal exception'
        if claim.startswith('1462financial'):loc='Independence numbered safeguard8 (financial approval conditions supplied by primaryArticle1462)'
        if claim.startswith('CJIhasnospecial'):loc='Independence numbered safeguard8 and primaryArticle146'
        if claim.startswith('129215contempt'):loc='Independence numbered safeguard7'
        if claim.startswith('SuryaKant53rdCJI'):match='direct';loc='paragraph50; not accepted as current without primary revalidation'
        a={'id':f'GBK741-{page}-{j:02}','gbk_page':page,'gbk_saved_capture':f'gbk-p{page}-transcription.html','claim_or_source_issue':claim,'laxmikanth_match':{'classification':match,'locator':'Prepared Ch26 '+loc,'certified_publisher_original':False},'disposition':disposition,'source_exactness_certified':False,'coverage_proven':False}
        if target:
            if ':' in target:
                ch,qid=target.split(':',1)
                if (ch,qid) not in allq: raise ValueError(('unresolved canonical',ch,qid))
                a['canonical_question_reference']={'chapter':ch,'id':qid}
                refs.setdefault((ch,qid),{'id':qid,'chapter':ch,'gbk_pages':[],'reason':'Same actual tested claim appears in this chapter; reuse the canonical app question rather than clone.','inventory_claims':[]})
                refs[(ch,qid)]['gbk_pages'].append(page);refs[(ch,qid)]['inventory_claims'].append(a['id'])
                # Do not count a broader/historical partial association as complete coverage.
                if disposition.startswith('canonical'):a['coverage_proven']=True
                if claim in ('NJACconstitutionalinvalidity16October2015','LChandraKumar1997not1994','NJACinvalid2015not2016'):
                    a['coverage_proven']=False
                    a['coverage_qualification']='Canonical item tests the invalidity/doctrine association, not independent recall of this exact date; date detail remains unassessed.'
            else:
                if target not in local: raise ValueError(('unresolved local',target))
                a['local_question_id']=target
                if disposition in ('approved','existing','approved-corrected-study-only'):a['coverage_proven']=True
        atoms.append(a)
for r in refs.values():r['gbk_pages']=sorted(set(r['gbk_pages']))
# Reader-only facts are visible, rather than being falsely attributed to a GBK page.
reader_atoms=[{'id':'LAX741-145-open-majority-dissent','claim_or_source_issue':'Open delivery of judgments and majority decision with permitted dissent under1454/5','laxmikanth_match':{'classification':'direct','locator':'Prepared Ch26 paragraph24'},'gbk_match':{'classification':'absent','related_page':297},'local_question_id':'POL-741-AT-open-majority-dissent','coverage_proven':True}]
for slug,claim,loc,why in [
('criminal-withdrawal-death','Article134(1)(b): High Court withdraws a subordinate-court case for trial before itself, convicts and sentences to death','table11 criminal appeals','Stable reader-supported target not yet separately authored; requires exact primary review.'),
('civil-limit-removal','30th Amendment1972 removed the old civil-appeal20000-rupee monetary condition','tables11–12','Historical amendment claim remains unassessed.'),
('review-grounds','Review grounds of discovery of evidence, apparent error and sufficient reason','paragraph46','Reader combines general grounds; criminal/civil procedural distinctions require Supreme Court Rules qualification.'),
('jurisdiction-curtailment','Judicial independence safeguard states that jurisdiction cannot be curtailed','Independence safeguard9','Do not convert this broad textbook summary into an unqualified rule about all statutory jurisdiction.'),
('constitutional-original-floor','Prepared explanation calls the original seven other judges a constitutional floor','paragraph4','Conflict: original wording imposed an until-Parliament-enlarges limit, not a minimum-floor rule.'),
('collegium-no-executive','Prepared explanatory criticism suggests no executive involvement in appointment','paragraphs8–9','Overstatement: formal appointment remains presidential and executive processing remains; analytic criticism is not a bare legal fact.'),
('njac-no-judiciary','Prepared explanatory criticism of NJAC representation','paragraphs8–9','Any claim of no judicial representation is erroneous: historical NJAC includedCJIand2seniorSCjudges.'),
('us-appellate-only-constitutional','Prepared comparative table says US Supreme Court appeals are confined to constitutional cases','tables17–18','Overbroad and not approved as a comparative study fact.'),
('current-strength38','Prepared update claims a2026Actraised sanctioned strength to38','paragraphs51–52; table19','Unverified current statute claim; not accepted merely because present in supplied notes.'),
('current-ordinance','Prepared update claims ordinance17May2026andassentaroundmidAugust2026','paragraph51','Precise current legislative claims require Gazette/official statute verification; held.'),
('current-working32','Prepared update claims working strength32at the time of a2026amendment','paragraph51','Dated operational count, not a stable constitutional fact.'),
('current-cji-letter','Prepared update claims CJIlettertoPM11May2026','paragraph51','Unverified attributed current event; held.'),
('advisory-1982-reference','Jammu and Kashmir Resettlement Act presidential reference1982','table13','Historical reference absent from the GBK inventory list; primary validation and assessment remain open.'),
('contempt-1991-extension','1991 judicial development concerning contempt of subordinate courts','paragraph41; table15','Precise case and jurisdictional scope need primary validation; no blanket extension claim approved.'),
('sanyal-committee','HN Sanyal committee attribution1961/1963','table15','Two-year ambiguity requires primary report or legislative-history evidence.'),
('doctrine-territorial-nexus','Doctrine of territorial nexus','paragraph47; table16','Name alone is not an assessed atomic concept; exact definition and compatible Unit6 question remain to reconcile.'),
('doctrine-colourable','Doctrine of colourable legislation','paragraph47; table16','Definition and actual assessed claim need canonical reconciliation.'),
('doctrine-implied','Doctrine of implied/incidental/ancillary powers','paragraph47; table16','Concept held pending precise definition and canonical reconciliation.'),
('doctrine-precedent','Doctrine of precedent','paragraph47; table16','Article141 canonical question is related; a distinct doctrine question must not be assumed covered by a name list.'),
('doctrine-occupied-field','Doctrine of occupied field','paragraph47; table16','Definition and federal distribution qualification not yet separately assessed.'),
('doctrine-prospective','Doctrine of prospective overruling','paragraph47; table16','Compatible existing Unit6 question POL-681-P515-001; canonical association needs final linkage review.'),
('doctrine-harmonious','Doctrine of harmonious construction','paragraph47; table16','Not assumed assessed from inclusion in the doctrine list.'),
('doctrine-liberal','Doctrine of liberal interpretation','paragraph47; table16','Reader target not separately assessed.'),
]:
    reader_atoms.append({'id':'LAX741-'+slug,'claim_or_source_issue':claim,'laxmikanth_match':{'classification':'direct','locator':'Prepared Ch26 '+loc},'gbk_match':{'classification':'absent-or-partial','qualification':'Additional prepared-reader detail; no invented GBK locator.'},'disposition':'held-unassessed-or-qualified','review_qualification':why,'coverage_proven':False})
for a in reader_atoms:
    if a['id']=='LAX741-doctrine-prospective':
        key=('6.8.1','POL-681-P515-001')
        if key not in allq:raise ValueError(('unresolved reader canonical',key))
        a['canonical_question_reference']={'chapter':key[0],'id':key[1]}
        a['disposition']='canonical'
        a['coverage_proven']=True
        a['review_qualification']='Existing item directly assesses prospective overruling in GolakNath; reuse it instead of authoring a clone.'
        refs[key]={'chapter':key[0],'id':key[1],'gbk_pages':[296,297,298],'reason':'Prepared Ch26 doctrine list and GBK discussion overlap the existing assessed prospective-overruling target.','inventory_claims':[a['id']]}
counts={}
for a in atoms:counts[a['disposition']]=counts.get(a['disposition'],0)+1
obj={'chapter':'7.4.1','inventory_version':'manual-claim-review-1','source_scope':{'gbk_printed_pages':list(range(286,312)),'access':'saved HTML text only; no additional source pass or image view','laxmikanth':'Complete prepared Chapter26 English/Telugu content and tables; locators are zero-based English paragraph indices and table indices, not publisher page claims.','source_exactness_certified':False},'atomic_claims':atoms,'reader_only_claims':reader_atoms,'counts_by_disposition':counts,'full_chapter_coverage':False,'qualification':'This is a substantive claim inventory, not a certificate that unreadable source spans or every historical subdetail have been recovered. Held claims are not app questions; explanation-only facts are not counted as assessed. All currently readable pages are represented; future source repairs require reconciliation.'}
(P/'atomic-inventory.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
bank=json.loads((P/'Questions.json').read_text(encoding='utf8'))
existing={(r.get('chapter'),r['id']):r for r in bank.get('question_references',[])}
for k,r in refs.items():
    if k in existing:
        existing[k]['gbk_pages']=sorted(set(existing[k].get('gbk_pages',[])+r['gbk_pages']))
        existing[k]['inventory_claims']=r['inventory_claims']
    else:existing[k]=r
bank['question_references']=list(existing.values())
(P/'Questions.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(P/'atomic-coverage-review.json').write_text(json.dumps({'chapter':'7.4.1','inventory_claim_count':len(atoms),'reader_only_claim_count':len(reader_atoms),'canonical_references':list(refs.values()),'counts_by_disposition':counts,'full_chapter_coverage':False,'source_exactness_certified':False,'existing_question_retirements':{'performed':False,'reason':'Parent instruction preserves app-resolving IDs pending alias and ExpectedQ handoff. Existing Article32/136 etc broader cross-unit overlaps remain a qualification.'},'remaining_work':['Resolve held source text without inventing missing words.','Validate and author unassessed stable statutory and historical claims using supplied supplements first and primary evidence for gaps.','Review source-error qualifications separately from source transcription.','Complete descriptive PYQ-first workflow and exact source gates under coordinator ownership.'],'review_scope':'All 26 saved GBK pages and prepared Chapter26 were substantively considered; coverage remains false because many individual claims are held, partial or merely explanation support.'},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Manual GBK atoms',len(atoms),'reader additions',len(reader_atoms),'canonical references',len(refs))
