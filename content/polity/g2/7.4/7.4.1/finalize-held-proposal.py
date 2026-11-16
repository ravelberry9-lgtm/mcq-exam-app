import json,re
from pathlib import Path
P=Path(__file__).parent
p=P/'held-expansion-v2-proposal.json';d=json.loads(p.read_text(encoding='utf8'))
replacements={'JudgesCases':'Judges Cases','A.First':'A. First','B.Second':'B. Second','C.Third':'C. Third','concurrence.Choose':'concurrence. Choose','old₹':'old ₹','FifteenthAmendment':'Fifteenth Amendment','ThirtiethAmendment':'Thirtieth Amendment','Forty-secondAmendment':'Forty-second Amendment','Forty-fourthAmendment':'Forty-fourth Amendment','OrderXLVIIrule':'Order XLVII rule','CPCOrder':'CPC Order','non-AoRadvocate':'non-AoR advocate','AoRor':'AoR or','Court.Which':'Court. Which','AdvocatesAct':'Advocates Act','DistrictCollector':'District Collector','UnionLawMinister':'Union Law Minister','GramPanchayat':'Gram Panchayat','OrderVIrule':'Order VI rule','Onejudge':'One judge','Twojudges':'Two judges','Threejudges':'Three judges','Fivejudges':'Five judges','A.Wilful':'A. Wilful','B.Publication':'B. Publication','Acriminal;Bcivil':'A civil; B civil','Bothautomaticallyimmune':'Both automatically immune','Bothonlycivil':'Both only criminal','Acivil;Bcriminal':'A civil; B criminal','President’sRuleinoneState':'President’s Rule in one State','Anyordinarycabinetresolution':'Any ordinary cabinet resolution','EveryNationalEmergencyautomatically':'Every National Emergency automatically','Onlythecourt’sdailybudgetregister':'Only the court’s daily budget register','Onlyawebsitecauselist':'Only a website cause list','Preservationandauthoritativeevidentiarycharacterofjudicialrecords':'Preservation and authoritative evidentiary character of judicial records','Automaticabolitionofappeals':'Automatic abolition of appeals','NyayalayasAct':'Nyayalayas Act','Executivepleasurealone':'Executive pleasure alone','Partydiscipline':'Party discipline','Policeinstructionsalone':'Police instructions alone','Principlesofnaturaljustice':'Principles of natural justice','CourtsAct':'Courts Act','Customsduty,forexpenaltyandcitizenship':'Customs duty, forex penalty and citizenship','Landceiling,taxevasionandpublicrecruitment':'Land ceiling, tax evasion and public recruitment','Matrimonialstatus,spousalpropertyandminor-custodyproceedings':'Matrimonial status, spousal property and minor-custody proceedings','Parliamentaryelection,industriallicenceandcriminalpardon':'Parliamentary election, industrial licence and criminal pardon','asaprivatewritappeal':'as a private writ appeal','asanordinaryappealasofright':'as an ordinary appeal as of right','asajudicialappointment':'as a judicial appointment','PSCmember':'PSC member','Governoractingalone':'Governor acting alone','ChiefMinister':'Chief Minister','StateAssemblySpeaker':'State Assembly Speaker','M.PatanjaliSastri':'M. Patanjali Sastri','HarilalKania':'Harilal Kania','S.R.Das':'S. R. Das','M.H.Kania':'M. H. Kania','MehrChandMahajan':'Mehr Chand Mahajan','Y.V.Chandrachud':'Y. V. Chandrachud','M.Fathima':'M. Fathima','Alllegislativeactsareimmuneevenifconstitutionallyillegal':'All legislative acts are immune even if constitutionally illegal','Courtsmayannuleveryproceedingforanyminorproceduraldeparture':'Courts may annul every proceeding for any minor procedural departure','LegislativeprivilegeautomaticallyoverridestheentireConstitution':'Legislative privilege automatically overrides the entire Constitution','Mereproceduralirregularityisdifferentfromsubstantiveillegalityorconstitutionalviolation':'Mere procedural irregularity is different from substantive illegality or constitutional violation','30 daysforfiling;disposalwithinsixmonthsoffiling':'30 days for filing; disposal within six months of filing','Sixmonthsforfiling;30 daysfordisposal':'Six months for filing; 30 days for disposal','Oneyeartoappeal;nofixeddisposalrule':'One year to appeal; no fixed disposal rule','Filinganddisposalbothalwayswithinsevendays':'Filing and disposal both always within seven days'}
def fix(v):
 if isinstance(v,str):
  for a,b in replacements.items():v=v.replace(a,b)
  return re.sub(r'(?<=\))(?=of\b|power\b|misbehaviour\b)', ' ',v)
 if isinstance(v,list):return [fix(x) for x in v]
 if isinstance(v,dict):return {k:fix(x) for k,x in v.items()}
 return v
d=fix(d)
# This is a proposal, never an app-bank authoring operation.
deferred={'civil-appeal-thirtieth','civil-criminal-review-grounds','gram-appeal-periods','family-jurisdiction-set'}
for q,f,r in zip(d['question_candidates'],d['fact_candidates'],d['manual_reviews']):
 slug=q['id'].removeprefix('POL-741-SUPP-')
 if slug=='notice-admission-discretion':f['source_hold_ids']=r['source_hold_ids']=['GBK741-291-09']
 if slug in deferred:
  q['independent_review_ready']=False;q['scope_status']='deferred_reader_only_target_no_demonstrated_GBK_claim_match'
  f['status']='deferred_reader_only_target';r['result']='deferred_scope_not_completion_blocker'
 else:q['scope_status']='recorded_GBK_claim_target_pending_independent_review'
 if slug=='contempt-classification':
  q['options_en']=['A criminal; B civil','Both automatically immune','Both only civil','A civil; B criminal']
d['scope_correction']='Intensive Laxmikanth-only expansion deferred per user request D. Four unmatched reader-only targets retained as deferred proposals, not completion blockers. GBK claim scope remains mandatory; primary support does not certify exact source text.'
d['independent_review_ready']=sum(q['independent_review_ready'] for q in d['question_candidates'])
d['deferred_reader_only_targets']=len(deferred)
assert len(d['question_candidates'])==28
for q in d['question_candidates']:
 assert len(q['options_en'])==len(q['options_te'])==4 and 1<=q['answer']<=4
 assert q['explanation_id'] in d['explanations']
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Ready',d['independent_review_ready'],'deferred',len(deferred),'primary gate',d['primary_locator_holds'])
