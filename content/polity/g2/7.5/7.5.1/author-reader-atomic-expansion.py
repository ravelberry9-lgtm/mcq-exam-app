"""Manually authored questions and reviews; mechanical merge, no source reads.
Do not rerun after independent reviewer corrections without reconciling them.
"""
import json
from pathlib import Path
P=Path(__file__).parent
C='https://www.legislative.gov.in/static/uploads/2025/07/359f70a69695affb9d72f8393102bd2e.pdf'
CO='https://api.sci.gov.in/judgment/judis/28469.pdf'
LC='https://aphc.gov.in/docs/imp_judgements/L_Chandra_Kumar_vs_Union_Of_India_And_Others_on_18_March_1997.PDF'
MM='https://cdnbbsr.s3waas.gov.in/s3ec0490f1f4972d133619a60c30f3559e/documents/aor_notice_circular/3.pdf'
RJ='https://api.sci.gov.in/jonew/judis/11570.pdf'
rows=[]
def add(slug,loc,match,primary,provision,fen,fte,qe,qt,oe,ot,key,ee,et,solve,fmt='single-best-answer',difficulty='moderate'):
 rows.append(dict(slug=slug,loc=loc,match=match,primary=primary,provision=provision,fen=fen,fte=fte,qe=qe,qt=qt,oe=oe,ot=ot,key=key,ee=ee,et=et,solve=solve,fmt=fmt,difficulty=difficulty))

add('marbury-year','paragraph0; table0','direct',LC,'paragraph56',
'The Marbury v. Madison landmark affirming American judicial review dates to1803.',
'అమెరికాలో న్యాయ సమీక్షను ధృవీకరించిన మార్బరీ వర్సెస్ మాడిసన్ ప్రముఖ తీర్పు1803లో వెలువడింది.',
'In which year was Marbury v. Madison, the landmark American judicial-review decision, delivered?',
'అమెరికాలో న్యాయ సమీక్షకు సంబంధించి ప్రముఖమైన మార్బరీ వర్సెస్ మాడిసన్ తీర్పు ఏ సంవత్సరంలో వెలువడింది?',
['1776','1787','1865','1803'],['1776','1787','1865','1803'],4,
'The decision dates to1803 and was delivered by Chief Justice John Marshall. The existing chapter question supplies1803 as context while asking for the case–judge association; this item independently tests the year. Independence in1776 and the Constitution’s drafting in1787 are separate historical events.',
'ఈ తీర్పు1803లో ప్రధాన న్యాయమూర్తి జాన్ మార్షల్ ద్వారా వెలువడింది. అధ్యాయంలోని పాత ప్రశ్న1803ను సందర్భంలో ఇస్తూ కేసు–న్యాయమూర్తి జతను అడుగుతుంది; ఈ ప్రశ్న సంవత్సరాన్ని ప్రత్యేకంగా పరీక్షిస్తుంది.1776స్వాతంత్ర్యం,1787రాజ్యాంగ రచన వేర్వేరు ఘట్టాలు.',
'Option4 is1803. Options1and2 are familiar American founding dates;3 is a later constitutional-history distractor.',difficulty='easy')

add('delegated-legislation-review','paragraph2','direct',C,'Articles13(3)(a),245–246; subordinate norms subject to lawful authority',
'Judicial review of legislation includes delegated legislation; a statutory rule has no blanket immunity from review merely because a Minister issued it.',
'శాసనాల న్యాయ సమీక్షలో అధీన శాసనాలు కూడా చేరుతాయి; మంత్రి జారీ చేశారనే కారణంతో చట్టబద్ధ నియమానికి సమీక్ష నుంచి సంపూర్ణ మినహాయింపు లభించదు.',
'A statutory rule is challenged as exceeding the parent Act and violating a Fundamental Right. The Government argues that delegated legislation is outside judicial review. Which is correct?',
'మూల చట్టం ఇచ్చిన అధికారాన్ని మించి, ప్రాథమిక హక్కును ఉల్లంఘించిందని ఒక చట్టబద్ధ నియమాన్ని సవాలు చేశారు. అధీన శాసనం న్యాయ సమీక్ష పరిధిలో లేదని ప్రభుత్వం వాదించింది. సరైనది ఏది?',
['The argument succeeds whenever a Minister signed the rule','Only Acts of Parliament can be reviewed','Delegated legislation is reviewable; its authority and constitutional validity may be examined','The rule becomes a constitutional amendment'],
['మంత్రి సంతకం చేసిన ప్రతి సందర్భంలో వాదన నెగ్గుతుంది','పార్లమెంటు చట్టాలను మాత్రమే సమీక్షించవచ్చు','అధీన శాసనాన్ని సమీక్షించవచ్చు; దాని అధికార ఆధారం, రాజ్యాంగబద్ధతను పరిశీలించవచ్చు','నియమం రాజ్యాంగ సవరణగా మారుతుంది'],3,
'The supplied classification expressly includes subordinate or delegated legislation. Rules must stay within the enabling law and the Constitution. Article13(3)(a) includes rules, regulations and similar instruments with the force of law. The case is about legal limits, not a court substituting its preferred policy.',
'సిద్ధం చేసిన వర్గీకరణలో అధీన లేదా అప్పగించిన శాసనాలను స్పష్టంగా చేర్చారు. నియమాలు అధికారాన్ని ఇచ్చిన చట్టం, రాజ్యాంగానికి లోబడి ఉండాలి. ప్రకరణ13(3)(a) చట్టబలం గల నియమాలు, నిబంధనలు తదితరాలను చేర్చుతుంది. ఇక్కడ విషయం చట్టపరమైన పరిమితులు; కోర్టు తనకు నచ్చిన విధానాన్ని బదులు పెట్టడం కాదు.',
'Option3 preserves review of the norm and the parent-law/constitutional limits.1 creates ministerial immunity,2 excludes State and delegated laws,4 confuses delegated and constituent power.',fmt='application')

add('judicial-observations','paragraph4; table2','direct',LC,'paragraph57; Minerva Mills official reportp241; Rajasthan quotation in1994SCR644',
'The supplied judicial-review observations associate V.G. Row with Patanjali Sastri’s sentinel role, Minerva Mills with Chandrachud’s rights-without-remedies warning, and State of Rajasthan with Bhagwati’s ultimate-interpreter role.',
'న్యాయ సమీక్ష వ్యాఖ్యల్లో వీ.జీ.రో కేసు పతంజలి శాస్త్రి చెప్పిన అప్రమత్త కాపలా పాత్రతో, మినర్వా మిల్స్ చంద్రచూడ్ చెప్పిన పరిహారం లేని హక్కుల హెచ్చరికతో, రాజస్థాన్ రాష్ట్రం కేసు భగవతి చెప్పిన అంతిమ వ్యాఖ్యాత పాత్రతో సంబంధించాయి.',
'Match the observation with its case–judge association. A. Sentinel on the qui vive B. Fundamental Rights become a mere adornment without judicial remedies C. Court as ultimate interpreter of constitutional limits.1.V.G. Row—Patanjali Sastri 2.Minerva Mills—Y.V.Chandrachud 3.State of Rajasthan v.Union—P.N.Bhagwati. Choose A–B–C.',
'వ్యాఖ్యను కేసు–న్యాయమూర్తి జతతో సరిపోల్చండి. A. నిరంతరం అప్రమత్తంగా ఉండే కాపలా B. న్యాయ పరిహారం లేకపోతే ప్రాథమిక హక్కులు అలంకారప్రాయమవుతాయి C. రాజ్యాంగ పరిమితులకు కోర్టు అంతిమ వ్యాఖ్యాత.1.వీ.జీ.రో—పతంజలి శాస్త్రి 2.మినర్వా మిల్స్—వై.వి.చంద్రచూడ్ 3.రాజస్థాన్ రాష్ట్రం వర్సెస్ కేంద్రం—పి.ఎన్.భగవతి. A–B–C క్రమాన్ని ఎంచుకోండి.',
['1–2–3','2–1–3','1–3–2','3–2–1'],['1–2–3','2–1–3','1–3–2','3–2–1'],1,
'The three associations are correctly ordered1–2–3. L.Chandra Kumar reproduces the V.G.Row observation with Sastri’s attribution; the official Minerva Mills report contains Chandrachud’s warning; the Court’s1994reported judgment reproduces Bhagwati’s State of Rajasthan passage. These are particular attributed observations, not claims that only those judges recognised review.',
'మూడు జతల సరైన క్రమం1–2–3. ఎల్.చంద్రకుమార్ తీర్పు వీ.జీ.రో వ్యాఖ్యను శాస్త్రి పేరుతో ఉటంకిస్తుంది; అధికారిక మినర్వా మిల్స్ నివేదికలో చంద్రచూడ్ హెచ్చరిక ఉంది;1994నాటి కోర్టు నివేదిక రాజస్థాన్ రాష్ట్రం కేసులో భగవతి వ్యాఖ్యను పునరుత్పత్తి చేస్తుంది. ఇవి నిర్దిష్ట వ్యాఖ్యల అనుబంధాలు మాత్రమే; ఆ న్యాయమూర్తులే సమీక్షను గుర్తించారని అర్థం కాదు.',
'A maps1,B maps2,C maps3. Each other permutation attaches at least one observation to a different case/speaker.',fmt='matching',difficulty='hard')

add('criminal-constitutional-routes','table3 rowArticle134','partial',C,'Article134(1)(a),(b) and(2)',
'Article134(1)(a),(b) expressly cover High Court reversal of acquittal followed by death sentence and withdrawal for its own trial followed by conviction and death sentence.',
'హైకోర్టు నిర్దోషిత్వ ఉత్తర్వును రద్దు చేసి మరణశిక్ష విధించడం, లేదా తానే విచారించడానికి కేసును తెప్పించుకుని దోషిగా నిర్ధారించి మరణశిక్ష విధించడం ప్రకరణ134(1)(a),(b)లో స్పష్టంగా ఉన్నాయి.',
'Which situations are expressly covered by Article134(1)(a),(b) itself?1.A High Court reverses an acquittal on appeal and sentences the accused to death.2.It withdraws a subordinate-court case for its own trial, convicts and sentences the accused to death.3.Every criminal conviction, irrespective of the sentence or procedural route.',
'ప్రకరణ134(1)(a),(b) పాఠ్యంలోనే ఏ సందర్భాలు స్పష్టంగా ఉన్నాయి?1.హైకోర్టు అప్పీల్‌లో నిర్దోషిత్వ ఉత్తర్వును రద్దు చేసి నిందితునికి మరణశిక్ష విధించింది.2.అధీన కోర్టు కేసును తానే విచారించడానికి తెప్పించుకుని దోషిగా నిర్ధారించి మరణశిక్ష విధించింది.3.శిక్ష లేదా ప్రక్రియతో సంబంధం లేకుండా ప్రతి క్రిమినల్ నేర నిర్ధారణ.',
['1only','2only','1,2and3','1and2only'],['1 మాత్రమే','2 మాత్రమే','1,2,3','1,2 మాత్రమే'],4,
'Both specified death-sentence routes are in clauses(a)and(b). They are not an automatic appeal for every conviction. Clause(c)separately addresses High Court fitness certification; clause(2)permits Parliament to enlarge criminal appellate powers. Thus the answer does not deny statutory enlargement beyond the two routes asked.',
'రెండు నిర్దిష్ట మరణశిక్ష మార్గాలూ(a),(b)ఖండికల్లో ఉన్నాయి. ప్రతి నేర నిర్ధారణకు స్వయంచాలక అప్పీల్ అని కాదు.(c)ఖండిక హైకోర్టు అప్పీల్ యోగ్యత ధ్రువీకరణకు వేరు ఏర్పాటు చేస్తుంది; ఖండిక(2) క్రిమినల్ అప్పీల్ అధికారాలను పార్లమెంటు విస్తరించవచ్చని చెబుతుంది. కాబట్టి ప్రశ్నించిన రెండు మార్గాలకు మించి చట్టబద్ధ విస్తరణ లేదని సమాధానం చెప్పదు.',
'Statements1and2 exactly match the asked clauses;3 is overbroad. Option4 alone includes both required routes while excluding the universal claim.',fmt='statement-combination')

add('certificate-consideration','table3 rowArticle134A','partial',C,'Article134A(a),(b)',
'An immediate oral application by or for an aggrieved party requires the High Court to determine whether the relevant appeal certificate may be given; it does not require automatic grant.',
'బాధిత పక్షం లేదా దాని తరఫున వెంటనే మౌఖిక దరఖాస్తు చేస్తే సంబంధిత అప్పీల్ ధ్రువపత్రం ఇవ్వవచ్చా అనే ప్రశ్నను హైకోర్టు నిర్ణయించాలి; స్వయంచాలకంగా ధ్రువపత్రం ఇవ్వాలని కాదు.',
'Immediately after a relevant judgment, an aggrieved party orally applies under Article134A. What must the High Court do?',
'సంబంధిత తీర్పు వెలువడిన వెంటనే బాధిత పక్షం ప్రకరణ134A కింద మౌఖికంగా దరఖాస్తు చేసింది. హైకోర్టు ఏమి చేయాలి?',
['Grant the certificate automatically without applying its legal test','Determine whether the relevant certificate may be given, as soon as may be','Reject it because only a written application can be considered','Wait for the President to certify the case'],
['చట్టపరమైన ప్రమాణాన్ని వర్తింపజేయకుండా స్వయంచాలకంగా ధ్రువపత్రం ఇవ్వాలి','సంబంధిత ధ్రువపత్రం ఇవ్వవచ్చా అనే ప్రశ్నను వీలైనంత త్వరగా నిర్ణయించాలి','లిఖిత దరఖాస్తునే పరిశీలించవచ్చు కాబట్టి తిరస్కరించాలి','రాష్ట్రపతి కేసును ధ్రువీకరించే వరకు వేచి ఉండాలి'],2,
'Article134A distinguishes consideration from grant. The High Court may act on its own motion and shall determine the certificate question on the specified immediate oral application. The certificate still depends on the relevant Article132,133or134(1)(c)test. Existing constitutional-appeal practice identifies the certificate route but does not test this procedural trigger.',
'ప్రకరణ134A పరిశీలనను ధ్రువపత్రం మంజూరు నుంచి వేరు చేస్తుంది. హైకోర్టు స్వప్రేరణతో వ్యవహరించవచ్చు; నిర్దేశిత తక్షణ మౌఖిక దరఖాస్తుపై ధ్రువపత్రం ప్రశ్నను నిర్ణయించాలి. మంజూరు సంబంధిత ప్రకరణ132,133లేదా134(1)(c)ప్రమాణంపైనే ఆధారపడుతుంది. పాత రాజ్యాంగ అప్పీల్ ప్రశ్న ధ్రువపత్ర మార్గాన్ని గుర్తిస్తుంది; ఈ ప్రక్రియా సందర్భాన్ని పరీక్షించదు.',
'Option2 states mandatory determination without automatic grant.1 confuses grant and consideration,3 denies the express oral route,4 invents presidential certification.',fmt='application',difficulty='hard')

add('federal-residual-jurisdiction','table3 rowArticle135','partial',C,'Article135',
'Until Parliament otherwise provides, Article135 preserves specified pre-Constitution Federal Court jurisdiction for the Supreme Court in matters to which Articles133and134do not apply.',
'పార్లమెంటు వేరుగా కల్పించే వరకు, ప్రకరణలు133,134వర్తించని విషయాల్లో రాజ్యాంగ పూర్వ ఫెడరల్ కోర్టు నిర్దిష్ట అధికార పరిధిని ప్రకరణ135 సుప్రీంకోర్టుకు కొనసాగిస్తుంది.',
'Which Article preserves for the Supreme Court the specified residual jurisdiction exercisable by the Federal Court immediately before the Constitution, until Parliament otherwise provides?',
'పార్లమెంటు వేరుగా కల్పించే వరకు, రాజ్యాంగానికి వెంటనే ముందు ఫెడరల్ కోర్టు వినియోగించగల నిర్దిష్ట అవశేష అధికార పరిధిని సుప్రీంకోర్టుకు ఏ ప్రకరణ కొనసాగిస్తుంది?',
['Article131','Article134A','Article135','Article143'],['ప్రకరణ131','ప్రకరణ134A','ప్రకరణ135','ప్రకరణ143'],3,
'Article135 concerns existing-law Federal Court jurisdiction in matters outside Articles133and134. It is not the Article131federal-dispute jurisdiction, Article134Acertification procedure or Article143advisory reference. The continuation is expressly subject to Parliament providing otherwise.',
'ప్రకరణ135, ప్రకరణలు133,134పరిధిలోకి రాని విషయాల్లో అప్పటి చట్టం కింద ఫెడరల్ కోర్టు అధికార పరిధికి సంబంధించినది. ఇది ప్రకరణ131సమాఖ్య వివాద అధికారం, ప్రకరణ134Aధ్రువపత్ర ప్రక్రియ లేదా ప్రకరణ143సలహా సూచన కాదు. పార్లమెంటు వేరుగా కల్పించే అవకాశానికి ఈ కొనసాగింపు స్పష్టంగా లోబడి ఉంటుంది.',
'Option3 identifies the residual continuation provision.1 concerns government-party disputes,2 certificates,4 advisory references.',difficulty='easy')

add('territorial-law-range','table3 rowArticle245','partial',C,'Article245(1)',
'Subject to the Constitution, Parliament may legislate for all or part of India, while a State Legislature may legislate for all or part of that State.',
'రాజ్యాంగానికి లోబడి పార్లమెంటు భారతదేశం మొత్తం లేదా కొంత భాగానికి, రాష్ట్ర శాసనసభ ఆ రాష్ట్రం మొత్తం లేదా కొంత భాగానికి చట్టాలు చేయవచ్చు.',
'Which pairing correctly states the ordinary territorial range in Article245(1), subject to the Constitution?',
'రాజ్యాంగానికి లోబడి ప్రకరణ245(1)లోని సాధారణ ప్రాదేశిక పరిధిని సరిగ్గా తెలిపే జత ఏది?',
['Parliament—whole/part of India; State Legislature—whole/part of that State','Parliament—Delhi alone; State Legislature—any foreign country','Parliament—Union Territories alone; State Legislature—all India','Parliament—its own State alone; State Legislature—only its capital'],
['పార్లమెంటు—భారతదేశం మొత్తం/కొంత భాగం; రాష్ట్ర శాసనసభ—ఆ రాష్ట్రం మొత్తం/కొంత భాగం','పార్లమెంటు—ఢిల్లీ మాత్రమే; రాష్ట్ర శాసనసభ—ఏ విదేశమైనా','పార్లమెంటు—కేంద్రపాలిత ప్రాంతాలు మాత్రమే; రాష్ట్ర శాసనసభ—భారతదేశం అంతా','పార్లమెంటు—తన రాష్ట్రం మాత్రమే; రాష్ట్ర శాసనసభ—రాజధాని మాత్రమే'],1,
'Article245(1) sets the ordinary territorial ranges while making both subject to the Constitution. Territorial range must be distinguished from subject-matter competence under Article246. A legislature does not gain a subject-matter power merely because an event occurs within its territory.',
'ప్రకరణ245(1) సాధారణ ప్రాదేశిక పరిధులను నిర్దేశిస్తూ రెండింటినీ రాజ్యాంగానికి లోబరుస్తుంది. ప్రాదేశిక పరిధిని ప్రకరణ246లోని విషయాధికారంతో వేరు చేయాలి. ఒక ఘటన తన భూభాగంలో జరిగిందనే కారణంతో శాసనసభకు ఆ అంశంపై అధికారం లభించదు.',
'Option1 gets both territorial ranges right;2–4 improperly narrow Parliament and/or enlarge or narrow State reach.',fmt='matching',difficulty='easy')

add('extraterritorial-operation','table3 rowArticle245, primary qualification','partial',C,'Article245(2)',
'Article245(2) says a parliamentary law is not invalid merely on the ground of extra-territorial operation; this does not immunise it from other constitutional limits.',
'భారత భూభాగం వెలుపల అమలవుతుందనే కారణంతోనే పార్లమెంటు చట్టం చెల్లదని చెప్పలేమని ప్రకరణ245(2) చెబుతుంది; ఇతర రాజ్యాంగ పరిమితుల నుంచి మినహాయింపు ఇవ్వదు.',
'A parliamentary law is challenged solely because it has extra-territorial operation. Which response follows Article245(2)?',
'భారత భూభాగం వెలుపల అమలవుతుందనే కారణంతో మాత్రమే పార్లమెంటు చట్టాన్ని సవాలు చేశారు. ప్రకరణ245(2) ప్రకారం సరైన స్పందన ఏది?',
['Every such law is automatically void','Only a State Legislature may make such a law','The Constitution contains no relevant rule','That ground alone does not invalidate the law; other constitutional requirements remain'],
['అటువంటి ప్రతి చట్టం స్వయంచాలకంగా చెల్లదు','రాష్ట్ర శాసనసభ మాత్రమే అటువంటి చట్టం చేయవచ్చు','దీనిపై రాజ్యాంగంలో నిబంధన లేదు','ఆ కారణం ఒక్కటే చట్టాన్ని చెల్లనిదిగా చేయదు; ఇతర రాజ్యాంగ అవసరాలు కొనసాగుతాయి'],4,
'The clause expressly protects a parliamentary law against invalidity merely on this ground. It is not a declaration that Parliament can disregard Fundamental Rights, competence or every India-related constitutional limitation. The narrow textual rule is tested without assuming unlimited authority over foreign matters.',
'ఈ కారణంతో మాత్రమే పార్లమెంటు చట్టం చెల్లదని ప్రకటించకుండా ఖండిక స్పష్టంగా రక్షిస్తుంది. ప్రాథమిక హక్కులు, విషయాధికారం లేదా భారతదేశ సంబంధిత రాజ్యాంగ పరిమితులన్నింటినీ పార్లమెంటు విస్మరించవచ్చని కాదు. విదేశీ విషయాలపై అపరిమిత అధికారాన్ని ఊహించకుండా పాఠ్యంలోని పరిమిత నియమాన్ని పరీక్షించారు.',
'Option4 states the limited protection;1 reverses it,2 assigns it to States and3 denies the express provision.',fmt='application')

add('legislative-lists','table3 rowArticle246','partial',C,'Article246(1)–(3)',
'Article246 ordinarily assigns ListI to Parliament, ListII to States subject to constitutional qualifications, and ListIII to both; special provisions and constitutional exceptions remain.',
'ప్రకరణ246 సాధారణంగా మొదటి జాబితాను పార్లమెంటుకు, రాజ్యాంగ పరిమితులకు లోబడి రెండవ జాబితాను రాష్ట్రాలకు, మూడవ జాబితాను రెండింటికీ కేటాయిస్తుంది; ప్రత్యేక నిబంధనలు, రాజ్యాంగ మినహాయింపులు కొనసాగుతాయి.',
'Match the ordinary distribution under Article246. A.ListI B.ListII C.ListIII.1.Parliament and State Legislatures 2.Parliament 3.State Legislatures, subject to constitutional qualifications.Choose A–B–C.',
'ప్రకరణ246 కింద సాధారణ అధికార విభజనను జతపరచండి. A.మొదటి జాబితా B.రెండవ జాబితా C.మూడవ జాబితా.1.పార్లమెంటు, రాష్ట్ర శాసనసభలు 2.పార్లమెంటు 3.రాజ్యాంగ పరిమితులకు లోబడి రాష్ట్ర శాసనసభలు.A–B–C క్రమాన్ని ఎంచుకోండి.',
['1–2–3','2–3–1','3–2–1','2–1–3'],['1–2–3','2–3–1','3–2–1','2–1–3'],2,
'The correct mapping is Union List—Parliament; State List—States under the constitutional arrangement; Concurrent List—both. Article246’s priority clauses and other provisions qualify the distribution. The question does not state that Parliament can never legislate on a State List matter or replace the separate GST rule in Article246A.',
'సరైన జత కేంద్ర జాబితా—పార్లమెంటు; రాష్ట్ర జాబితా—రాజ్యాంగ ఏర్పాటు ప్రకారం రాష్ట్రాలు; ఉమ్మడి జాబితా—రెండూ. ప్రకరణ246లోని ప్రాధాన్య ఖండికలు, ఇతర నిబంధనలు ఈ విభజనను పరిమితం చేస్తాయి. రాష్ట్ర జాబితాపై పార్లమెంటు ఎప్పటికీ చట్టం చేయలేదని లేదా ప్రకరణ246Aలోని వేరు జీఎస్టీ నియమాన్ని ఇది భర్తీ చేస్తుందని ప్రశ్న చెప్పదు.',
'A maps2,B maps3,C maps1, so option2. The other permutations exchange Union/State/Concurrent authority.',fmt='matching')

add('nonstate-territory','table3 rowArticle246, primary qualification','partial',C,'Article246(4)',
'Parliament may legislate for territory not included in a State even on a State List matter under Article246(4).',
'ప్రకరణ246(4) కింద రాష్ట్రంలో భాగం కాని భారత భూభాగానికి రాష్ట్ర జాబితా విషయంపైనా పార్లమెంటు చట్టం చేయవచ్చు.',
'A matter is in the State List, but Parliament legislates for a part of India not included in a State. Which provision directly addresses its competence?',
'ఒక అంశం రాష్ట్ర జాబితాలో ఉన్నప్పటికీ, రాష్ట్రంలో భాగం కాని భారత భూభాగానికి పార్లమెంటు చట్టం చేసింది. దాని అధికారాన్ని నేరుగా తెలిపే నిబంధన ఏది?',
['Article246(4)permits such parliamentary legislation','Article246always prohibits Parliament because the label is State List','Only a constitutional amendment can ever permit it','Only a High Court may legislate for that territory'],
['ప్రకరణ246(4) అటువంటి పార్లమెంటు చట్టాన్ని అనుమతిస్తుంది','రాష్ట్ర జాబితా అనే పేరు వల్ల ప్రకరణ246 పార్లమెంటును ఎల్లప్పుడూ నిషేధిస్తుంది','రాజ్యాంగ సవరణ మాత్రమే ఎప్పుడైనా అనుమతించగలదు','ఆ భూభాగానికి హైకోర్టు మాత్రమే చట్టం చేయవచ్చు'],1,
'Article246(4) supplies the express territorial exception. The ordinary State List allocation must therefore not be memorised as an absolute bar to Parliament in every territorial setting. This does not erase other special constitutional arrangements for particular Union Territories.',
'ప్రకరణ246(4) స్పష్టమైన ప్రాదేశిక మినహాయింపును కల్పిస్తుంది. అందువల్ల సాధారణ రాష్ట్ర జాబితా కేటాయింపును ప్రతి భూభాగ సందర్భంలోనూ పార్లమెంటుపై సంపూర్ణ నిషేధంగా గుర్తుంచుకోకూడదు. నిర్దిష్ట కేంద్రపాలిత ప్రాంతాల ఇతర ప్రత్యేక రాజ్యాంగ ఏర్పాట్లను ఇది తొలగించదు.',
'Option1 is the express exception.2 treats ordinary allocation as absolute,3 ignores an existing clause and4 confuses adjudication with legislation.',fmt='application')

add('article251-temporary','table3 grouped251/254 row','conflict',C,'Article251',
'Articles249and250 do not remove State legislative power; repugnant State law is inoperative only to the extent of conflict and while the relevant parliamentary law continues to have effect under Article251.',
'ప్రకరణలు249,250 రాష్ట్ర శాసనాధికారాన్ని తొలగించవు; ప్రకరణ251 ప్రకారం సంబంధిత పార్లమెంటు చట్టం అమల్లో ఉన్నంతకాలం, విరుద్ధత మేరకు మాత్రమే రాష్ట్ర చట్టం అమలు నిలుస్తుంది.',
'Consider Article251:1.A State retains its constitutional power to legislate despite Articles249/250.2.A conflicting State provision is inoperative to the extent of repugnancy while the relevant parliamentary law has effect.3.The entire State Act is permanently void in every such case.Which are correct?',
'ప్రకరణ251ను పరిశీలించండి:1.ప్రకరణలు249/250 ఉన్నప్పటికీ రాష్ట్రం తన రాజ్యాంగ శాసనాధికారాన్ని కలిగి ఉంటుంది.2.సంబంధిత పార్లమెంటు చట్టం అమల్లో ఉన్నంతకాలం విరుద్ధత మేరకు రాష్ట్ర నిబంధన అమలు నిలుస్తుంది.3.ప్రతి అటువంటి సందర్భంలో రాష్ట్ర చట్టం మొత్తం శాశ్వతంగా చెల్లదు.సరైనవి ఏవి?',
['1only','2and3only','1and2only','1,2and3'],['1 మాత్రమే','2,3 మాత్రమే','1,2 మాత్రమే','1,2,3'],3,
'The Constitution uses inoperative and a temporal qualification in Article251; it does not impose permanent wholesale invalidity. State legislative competence continues. The supplied table groups251with254and says void, which must be qualified by the distinct text of each Article.',
'ప్రకరణ251లో రాజ్యాంగం అమలు నిలిచిపోవడం అనే భావనతో పాటు కాల పరిమితిని ఉపయోగిస్తుంది; శాశ్వతంగా చట్టం మొత్తం చెల్లదని కాదు. రాష్ట్ర శాసనాధికారం కొనసాగుతుంది. సిద్ధం చేసిన పట్టిక251ను254తో కలిపి చెల్లదు అని చెప్పడాన్ని ప్రతి ప్రకరణంలోని వేరు పాఠ్యం ప్రకారం సవరించి అర్థం చేసుకోవాలి.',
'1and2 are express;3 incorrectly makes limited temporal inoperation permanent whole-Act invalidity. Option3 is the only correct combination.',fmt='statement-combination',difficulty='hard')

add('concurrent-repugnancy','table3 grouped251/254 row','partial',C,'Article254(1), subject to(2)',
'In the ordinary Concurrent List repugnancy case under Article254(1), parliamentary law prevails and the State law is void to the extent of repugnancy, subject to clause(2).',
'ప్రకరణ254(1) కింద సాధారణ ఉమ్మడి జాబితా విరుద్ధత సందర్భంలో పార్లమెంటు చట్టానికి ప్రాధాన్యం ఉంటుంది; ఖండిక(2)కు లోబడి విరుద్ధత మేరకు రాష్ట్ర చట్టం చెల్లదు.',
'A State law on a Concurrent List matter conflicts with a competent parliamentary law, and Article254(2)’s exception is not satisfied. Which result follows?',
'ఉమ్మడి జాబితా విషయంపై రాష్ట్ర చట్టం, అధికార పరిధిలో చేసిన పార్లమెంటు చట్టానికి విరుద్ధంగా ఉంది; ప్రకరణ254(2) మినహాయింపు నెరవేరలేదు. ఏ ఫలితం వర్తిస్తుంది?',
['The State law always prevails merely because it is later','The Governor may disregard the parliamentary law','The whole State Act necessarily fails even where provisions are separable','Parliamentary law prevails; State law is void to the extent of repugnancy'],
['తరువాత చేసినందువల్లనే రాష్ట్ర చట్టానికే ఎల్లప్పుడూ ప్రాధాన్యం','గవర్నర్ పార్లమెంటు చట్టాన్ని పట్టించుకోనవసరం లేదు','నిబంధనలు వేరు చేయగలిగినా రాష్ట్ర చట్టం మొత్తం తప్పనిసరిగా చెల్లదు','పార్లమెంటు చట్టానికి ప్రాధాన్యం; విరుద్ధత మేరకు రాష్ట్ర చట్టం చెల్లదు'],4,
'Article254(1) supplies the general Concurrent List rule, with clause(2)expressly preserved. The extent-of-repugnancy language prevents automatic destruction of every independent provision. Chronology alone or a Governor’s preference does not create the special presidential-assent exception.',
'ఖండిక(2)ను స్పష్టంగా కొనసాగిస్తూ ప్రకరణ254(1) సాధారణ ఉమ్మడి జాబితా నియమాన్ని ఇస్తుంది. విరుద్ధత మేరకు అనే భాష ప్రతి స్వతంత్ర నిబంధనను స్వయంచాలకంగా నాశనం చేయదు. తరువాత చేసిన తేదీ ఒక్కటే లేదా గవర్నర్ అభిప్రాయం ప్రత్యేక రాష్ట్రపతి ఆమోద మినహాయింపును సృష్టించవు.',
'Option4 states priority and limited invalidity.1 ignores the ordinary rule,2 invents executive waiver,3 ignores the limited extent.',fmt='application')

add('presidential-assent-repugnancy','table3 grouped251/254 row, omitted exception','partial',C,'Article254(2) and proviso',
'A qualifying State Concurrent List law reserved for presidential consideration and receiving assent may prevail in that State over an earlier central law; Parliament retains power to override it later.',
'రాష్ట్రపతి పరిశీలనకు రిజర్వు చేసి ఆమోదం పొందిన అర్హమైన రాష్ట్ర ఉమ్మడి జాబితా చట్టం, ఆ రాష్ట్రంలో పూర్వ కేంద్ర చట్టంపై ప్రాధాన్యం పొందవచ్చు; తరువాత దానిని అధిగమించే చట్టం చేసే అధికారం పార్లమెంటుకు కొనసాగుతుంది.',
'Consider Article254(2):1.A qualifying State Concurrent List law reserved for and receiving presidential assent may prevail in that State over an earlier central law.2.Parliament is permanently barred from legislating on the same matter thereafter.Which is correct?',
'ప్రకరణ254(2)ను పరిశీలించండి:1.రాష్ట్రపతి పరిశీలనకు రిజర్వు చేసి ఆమోదం పొందిన అర్హమైన రాష్ట్ర ఉమ్మడి జాబితా చట్టం, ఆ రాష్ట్రంలో పూర్వ కేంద్ర చట్టంపై ప్రాధాన్యం పొందవచ్చు.2.ఆ తరువాత అదే అంశంపై చట్టం చేయకుండా పార్లమెంటుకు శాశ్వత నిషేధం ఉంటుంది.సరైనది ఏది?',
['1only','2only','Both1and2','Neither1nor2'],['1 మాత్రమే','2 మాత్రమే','1,2 రెండూ','1 కాదు,2 కాదు'],1,
'Statement1captures the qualified territorial exception. The proviso explicitly allows Parliament to enact a later law on the same matter, including adding to, amending, varying or repealing the State law. Presidential assent does not confer permanent superiority or cure every other constitutional defect.',
'మొదటి వాక్యం షరతులతో కూడిన ప్రాదేశిక మినహాయింపును తెలుపుతుంది. రాష్ట్ర చట్టానికి చేర్పు, సవరణ, మార్పు లేదా రద్దు సహా అదే అంశంపై తరువాత చట్టం చేయడానికి మినహాయింపు నిబంధన పార్లమెంటుకు స్పష్టంగా అనుమతిస్తుంది. రాష్ట్రపతి ఆమోదం శాశ్వత ఆధిక్యాన్ని ఇవ్వదు; ఇతర రాజ్యాంగ లోపాలన్నింటినీ సరిచేయదు.',
'Statement1 is correct;2 contradicts the express parliamentary-override proviso. Option1 therefore follows.',fmt='statement-combination',difficulty='hard')

add('preconstitutional-continuance','table3 rowArticle372','partial',C,'Article372(1), read with Article13',
'Pre-Constitution law continues under Article372(1), subject to the Constitution, until altered, repealed or amended by a competent legislature or authority.',
'ప్రకరణ372(1) కింద రాజ్యాంగ పూర్వ చట్టం రాజ్యాంగానికి లోబడి, అధికారమున్న శాసనసభ లేదా సంస్థ మార్చే, రద్దు చేసే లేదా సవరించే వరకు కొనసాగుతుంది.',
'An ordinary law was in force immediately before the Constitution commenced. What is the general rule under Article372(1)?',
'రాజ్యాంగం అమల్లోకి రావడానికి వెంటనే ముందు ఒక సాధారణ చట్టం అమల్లో ఉంది. ప్రకరణ372(1) కింద సాధారణ నియమం ఏది?',
['It automatically becomes a constitutional amendment','It continues subject to the Constitution until competently altered, repealed or amended','Every such law necessarily lapsed on26January1950','It becomes immune from Fundamental Rights review'],
['అది స్వయంచాలకంగా రాజ్యాంగ సవరణ అవుతుంది','అధికారమున్న వ్యవస్థ మార్చే, రద్దు చేసే లేదా సవరించే వరకు రాజ్యాంగానికి లోబడి కొనసాగుతుంది','అటువంటి ప్రతి చట్టం1950జనవరి26న తప్పనిసరిగా ముగిసింది','ప్రాథమిక హక్కుల సమీక్ష నుంచి మినహాయింపు పొందుతుంది'],2,
'Article372avoids a legal vacuum by continuing existing law, but expressly makes continuation subject to the Constitution. Article13and other constitutional requirements remain relevant. This general rule is distinct from the special Article35(b)continuation of specified laws already tested in Unit6.',
'ప్రకరణ372 అమల్లోని చట్టాలను కొనసాగించి చట్టపరమైన శూన్యతను నివారిస్తుంది; అయితే కొనసాగింపును స్పష్టంగా రాజ్యాంగానికి లోబరుస్తుంది. ప్రకరణ13, ఇతర రాజ్యాంగ అవసరాలు వర్తిస్తాయి. ఈ సాధారణ నియమం యూనిట్6లో ఇప్పటికే పరీక్షించిన నిర్దిష్ట చట్టాల ప్రకరణ35(b)ప్రత్యేక కొనసాగింపుకు భిన్నం.',
'Option2 states continuity plus constitutional subordination.1 changes the law’s rank,3 creates universal lapse,4 erases the constitutional qualification.',fmt='application')

add('ninth-insertion-mechanism','paragraphs12,15; table9, actor/procedure qualification','partial',C,'Articles31B,368; Ninth Schedule amendment footnotes',
'A State legislature’s enactment of a law does not itself insert the law into the Ninth Schedule; insertion is effected through a parliamentary constitutional amendment.',
'రాష్ట్ర శాసనసభ చట్టం చేయడం ఒక్కటే దానిని తొమ్మిదవ షెడ్యూల్‌లో చేర్చదు; పార్లమెంటు రాజ్యాంగ సవరణ ద్వారా చేర్పు జరుగుతుంది.',
'A State Assembly passes an ordinary Act declaring that its new land law is inserted into the Ninth Schedule. Which assessment is correct?',
'తన కొత్త భూ చట్టాన్ని తొమ్మిదవ షెడ్యూల్‌లో చేర్చినట్లు రాష్ట్ర శాసనసభ సాధారణ చట్టం చేసింది. సరైన అంచనా ఏది?',
['The State declaration alone amends the constitutional Schedule','The Governor may insert it by assent alone','Ninth Schedule insertion requires a parliamentary constitutional amendment; the State Act alone is insufficient','Every State land law enters the Schedule automatically'],
['రాష్ట్ర ప్రకటన ఒక్కటే రాజ్యాంగ షెడ్యూల్‌ను సవరిస్తుంది','గవర్నర్ ఆమోదం ఒక్కటే దానిని చేర్చగలదు','తొమ్మిదవ షెడ్యూల్ చేర్పుకు పార్లమెంటు రాజ్యాంగ సవరణ అవసరం; రాష్ట్ర చట్టం ఒక్కటే సరిపోదు','ప్రతి రాష్ట్ర భూ చట్టం స్వయంచాలకంగా షెడ్యూల్‌లో చేరుతుంది'],3,
'The distinction is between the legislature enacting the underlying law and Parliament amending the constitutional Schedule. Article368procedure cannot be replaced by an ordinary State enactment or a bare ordinary parliamentary majority. A valid insertion is still subject to the applicable basic-structure review qualifications.',
'మూల చట్టాన్ని చేసే శాసనసభను, రాజ్యాంగ షెడ్యూల్‌ను సవరించే పార్లమెంటును వేరు చేయాలి. ప్రకరణ368 ప్రక్రియ స్థానంలో సాధారణ రాష్ట్ర చట్టం లేదా పార్లమెంటు సాధారణ మెజారిటీ ఒక్కటిని పెట్టలేరు. చెల్లుబాటయ్యే చేర్పుకూ వర్తించే ప్రాథమిక నిర్మాణ సమీక్ష పరిమితులు ఉంటాయి.',
'Option3 identifies both the actor and constitutional mechanism.1/2grant unilateral State insertion and4confuses enactment with inclusion.',fmt='application')

add('ninth-original-count','paragraph12; table8 first row; table9','direct',C,'Ninth Schedule first footnote: original entries1–13, First Amendment1951 section14',
'The Ninth Schedule originally received thirteen Acts and Regulations through the First Amendment1951.',
'మొదటి సవరణ1951ద్వారా తొమ్మిదవ షెడ్యూల్‌లో మొదట పదమూడు చట్టాలు, రెగ్యులేషన్లు చేరాయి.',
'How many Acts and Regulations were originally included when the Ninth Schedule was added in1951?',
'1951లో తొమ్మిదవ షెడ్యూల్‌ను చేర్చినప్పుడు మొదట ఎన్ని చట్టాలు, రెగ్యులేషన్లు అందులో ఉన్నాయి?',
['7','20','44','13'],['7','20','44','13'],4,
'The original entry range was1through13, confirmed by the official constitutional footnote to the First Amendment’s section14. Later amendments enlarged the Schedule. This is an historical original count, not a claim about the present total or the highest current serial number.',
'మొదటి సవరణలోని సెక్షన్14కు అధికారిక రాజ్యాంగ పాదసూచిక ధ్రువీకరించినట్లు మొదటి వరుస సంఖ్యలు1నుంచి13వరకు ఉన్నాయి. తరువాతి సవరణలు షెడ్యూల్‌ను విస్తరించాయి. ఇది తొలి చారిత్రక సంఖ్య; ప్రస్తుత మొత్తం లేదా ప్రస్తుతం చివరి వరుస సంఖ్య గురించి చెప్పడం కాదు.',
'Option4 is the original13.7and44are later addition counts;20is a later serial endpoint.',difficulty='easy')

add('ninth-early-additions','table8 rowsFourth, printedSeventh1964, TwentyNinth','conflict',C,'Ninth Schedule footnotes: Fourth1955s5; Seventeenth1964s3; Twenty-ninth1972s2',
'Historically the Fourth Amendment1955 added entries14–20(7); Seventeenth1964 entries21–64(44); Twenty-ninth1972 entries65–66(2). The prepared table’s Seventh1964 label is erroneous.',
'చారిత్రకంగా నాలుగవ సవరణ1955 ద్వారా14–20(7), పదిహేడవ సవరణ1964 ద్వారా21–64(44), ఇరవై తొమ్మిదవ సవరణ1972 ద్వారా65–66(2)చేర్పులు జరిగాయి. సిద్ధం చేసిన పట్టికలో ఏడవ సవరణ1964అనే పేరు తప్పు.',
'Match the Ninth Schedule additions. A.Fourth Amendment1955 B.Seventeenth Amendment1964 C.Twenty-ninth Amendment1972.1.44entries(21–64)2.2entries(65–66)3.7entries(14–20).Choose A–B–C.',
'తొమ్మిదవ షెడ్యూల్ చేర్పులను జతపరచండి. A.నాలుగవ సవరణ1955 B.పదిహేడవ సవరణ1964 C.ఇరవై తొమ్మిదవ సవరణ1972.1.44చేర్పులు(21–64)2.2చేర్పులు(65–66)3.7చేర్పులు(14–20).A–B–C క్రమాన్ని ఎంచుకోండి.',
['1–3–2','3–1–2','3–2–1','2–1–3'],['1–3–2','3–1–2','3–2–1','2–1–3'],2,
'The mapping is3–1–2. Official Ninth Schedule footnotes identify the amendments and historical ranges. The1964addition was by the Seventeenth Amendment, not the Seventh. These are counts added then, not counts of provisions currently operative; later omissions must not be silently ignored when discussing present totals.',
'సరైన జత3–1–2. అధికారిక తొమ్మిదవ షెడ్యూల్ పాదసూచికలు సవరణలు, చారిత్రక పరిధులను గుర్తిస్తాయి.1964చేర్పు పదిహేడవ సవరణ ద్వారా జరిగింది; ఏడవ సవరణ ద్వారా కాదు. ఇవి అప్పట్లో చేర్చిన సంఖ్యలు; ప్రస్తుతం అమల్లో ఉన్న మొత్తం కాదు. ప్రస్తుత సంఖ్యను చెప్పేటప్పుడు తరువాతి తొలగింపులను విస్మరించకూడదు.',
'A maps3,B maps1,C maps2. The other code permutations assign at least one amendment the wrong historical addition range/count.',fmt='matching',difficulty='hard')

add('ninth-middle-additions','table8 rowsThirtyFourth,ThirtyNinth,Fortieth','direct',C,'Ninth Schedule amendment footnotes: Thirty-fourth1974s2; Thirty-ninth1975s5; Fortieth1976s3',
'The Thirty-fourth Amendment1974 added20entries(67–86), Thirty-ninth1975 added38(87–124), and Fortieth1976 added64(125–188).',
'ముప్పై నాలుగవ సవరణ1974 ద్వారా20చేర్పులు(67–86), ముప్పై తొమ్మిదవ సవరణ1975 ద్వారా38(87–124), నలభైవ సవరణ1976 ద్వారా64(125–188)జరిగాయి.',
'Match the historical Ninth Schedule addition counts. A.Thirty-fourth Amendment1974 B.Thirty-ninth Amendment1975 C.Fortieth Amendment1976.1.64(125–188)2.20(67–86)3.38(87–124).Choose A–B–C.',
'తొమ్మిదవ షెడ్యూల్ చారిత్రక చేర్పుల సంఖ్యలను జతపరచండి. A.ముప్పై నాలుగవ సవరణ1974 B.ముప్పై తొమ్మిదవ సవరణ1975 C.నలభైవ సవరణ1976.1.64(125–188)2.20(67–86)3.38(87–124).A–B–C క్రమాన్ని ఎంచుకోండి.',
['1–2–3','3–2–1','2–3–1','2–1–3'],['1–2–3','3–2–1','2–3–1','2–1–3'],3,
'The correct order is2–3–1. The ranges identify what each amendment historically inserted. Later omission of entries87,92and130is a separate event, so historical insertion counts must not be presented as present operative counts. These associations do not confer constitutional immunity beyond the governing review doctrine.',
'సరైన క్రమం2–3–1. ప్రతి సవరణ చారిత్రకంగా చేర్చిన పరిధిని సంఖ్యలు సూచిస్తాయి. తరువాత87,92,130చేర్పుల తొలగింపు వేరే ఘట్టం; అందువల్ల చారిత్రక చేర్పుల సంఖ్యలను ప్రస్తుతం అమల్లో ఉన్న సంఖ్యలుగా చెప్పకూడదు. ఈ జతలు వర్తించే సమీక్ష సిద్ధాంతానికి మించి రాజ్యాంగ మినహాయింపు ఇవ్వవు.',
'A maps2,B maps3,C maps1. Other permutations assign a different amendment’s entry range/count.',fmt='matching',difficulty='hard')

add('ninth-later-additions','table8 rowsFortySeventh,SixtySixth,SeventyEighth','direct',C,'Ninth Schedule footnotes: Forty-seventh1984s2; Sixty-sixth1990s2; Seventy-eighth1995s2',
'The Forty-seventh Amendment1984 added14entries(189–202), Sixty-sixth1990 added55(203–257), and Seventy-eighth1995 added27(258–284).',
'నలభై ఏడవ సవరణ1984 ద్వారా14చేర్పులు(189–202), అరవై ఆరవ సవరణ1990 ద్వారా55(203–257), డెబ్బై ఎనిమిదవ సవరణ1995 ద్వారా27(258–284)జరిగాయి.',
'Match the historical Ninth Schedule additions. A.Forty-seventh Amendment1984 B.Sixty-sixth Amendment1990 C.Seventy-eighth Amendment1995.1.14(189–202)2.55(203–257)3.27(258–284).Choose A–B–C.',
'తొమ్మిదవ షెడ్యూల్ చారిత్రక చేర్పులను జతపరచండి. A.నలభై ఏడవ సవరణ1984 B.అరవై ఆరవ సవరణ1990 C.డెబ్బై ఎనిమిదవ సవరణ1995.1.14(189–202)2.55(203–257)3.27(258–284).A–B–C క్రమాన్ని ఎంచుకోండి.',
['1–2–3','2–1–3','1–3–2','3–2–1'],['1–2–3','2–1–3','1–3–2','3–2–1'],1,
'Official amendment footnotes confirm1–2–3. These are historical insertions, and serial284is the endpoint of the1995batch. A highest serial number alone cannot prove the present number of surviving entries, because the Schedule also contains a lettered entry and omissions.',
'అధికారిక సవరణ పాదసూచికలు1–2–3జతను ధ్రువీకరిస్తాయి. ఇవి చారిత్రక చేర్పులు;284అనేది1995చేర్పుల చివరి వరుస సంఖ్య. షెడ్యూల్‌లో అక్షరం కలిగిన చేర్పు, తొలగింపులు కూడా ఉన్నందున చివరి వరుస సంఖ్య ఒక్కటే ప్రస్తుతం మిగిలిన మొత్తం చేర్పులను నిరూపించదు.',
'A maps1,B maps2,C maps3; the remaining permutations exchange at least two amendments’ insertion batches.',fmt='matching',difficulty='hard')

add('ninth-lettered-entry','table8 SeventySixth row','direct',C,'Ninth Schedule entry257A; Seventy-sixth Amendment1994',
'The Seventy-sixth Amendment1994 inserted the Tamil Nadu reservation legislation as Ninth Schedule entry257A.',
'డెబ్బై ఆరవ సవరణ1994 తమిళనాడు రిజర్వేషన్ చట్టాన్ని తొమ్మిదవ షెడ్యూల్‌లో257Aచేర్పుగా చేర్చింది.',
'The Seventy-sixth Amendment1994inserted the Tamil Nadu reservation legislation under which Ninth Schedule entry?',
'డెబ్బై ఆరవ సవరణ1994 తమిళనాడు రిజర్వేషన్ చట్టాన్ని తొమ్మిదవ షెడ్యూల్‌లో ఏ చేర్పు కింద చేర్చింది?',
['202','257','284','257A'],['202','257','284','257A'],4,
'The lettered entry is257A. The existing Unit6question asks which amendment placed the Tamil Nadu law in the Schedule; this item instead tests the specific entry identifier. Lettered additions and later omissions explain why a last serial number and the number of actual entries need not be identical.',
'అక్షరం కలిగిన చేర్పు257A. యూనిట్6లోని పాత ప్రశ్న తమిళనాడు చట్టాన్ని ఏ సవరణ షెడ్యూల్‌లో చేర్చిందని అడుగుతుంది; ఈ ప్రశ్న నిర్దిష్ట చేర్పు గుర్తింపును పరీక్షిస్తుంది. అక్షరం కలిగిన చేర్పులు, తరువాతి తొలగింపుల వల్ల చివరి వరుస సంఖ్య, వాస్తవ చేర్పుల మొత్తం తప్పనిసరిగా సమానంగా ఉండవు.',
'Option4 is257A.257is the preceding numeric endpoint;202and284are endpoints of other historical insertion batches.',difficulty='hard')

add('coelho-impact-not-form','paragraph14points1–4; paragraph15','direct',CO,'Conclusions(i)–(iv), especially direct impact/effect test',
'Coelho examines actual impact on rights and basic structure; a PartIIIinfringement does not automatically equal basic-structure damage merely by its form or label.',
'కోయెల్హో ప్రకారం హక్కులు, ప్రాథమిక నిర్మాణంపై వాస్తవ ప్రభావాన్ని పరిశీలించాలి; రూపం లేదా పేరు వల్లనే ప్రతి మూడవ భాగం ఉల్లంఘన స్వయంచాలకంగా ప్రాథమిక నిర్మాణ నష్టం కాదు.',
'For an otherwise reviewable post-cutoff Ninth Schedule insertion, which approach best reflects Coelho’s impact test?',
'గడువు తరువాత తొమ్మిదవ షెడ్యూల్‌లో చేసిన, ఇతర షరతుల ప్రకారం సమీక్షించగల చేర్పుకు కోయెల్హో ప్రభావ పరీక్షను ఏ విధానం సరిగ్గా తెలుపుతుంది?',
['Treat the Schedule label alone as conclusive immunity','Examine actual effect on the relevant rights and whether the basic structure is damaged','Invalidate every PartIIIinfringement automatically without the basic-structure inquiry','Examine only the statute’s title and ignore its effects'],
['షెడ్యూల్ పేరు ఒక్కటే తుది మినహాయింపుగా భావించడం','సంబంధిత హక్కులపై వాస్తవ ప్రభావాన్ని, ప్రాథమిక నిర్మాణానికి నష్టం జరిగిందా అని పరిశీలించడం','ప్రాథమిక నిర్మాణ విచారణ లేకుండా ప్రతి మూడవ భాగం ఉల్లంఘనను స్వయంచాలకంగా చెల్లనిదిగా చేయడం','చట్టం శీర్షికను మాత్రమే పరిశీలించి ప్రభావాలను విస్మరించడం'],2,
'Coelho’s operative conclusions distinguish a rights infringement from basic-structure damage and require the actual impact inquiry. The rights test and essence-of-the-right test concern substance, not a protective label. Reviewability, invalidity and finalised-transaction savings are separate questions; a date or label alone does not answer all of them.',
'కోయెల్హో తుది నిర్ధారణలు హక్కు ఉల్లంఘనను ప్రాథమిక నిర్మాణ నష్టం నుంచి వేరు చేసి వాస్తవ ప్రభావ విచారణను కోరుతాయి. హక్కుల పరీక్ష, హక్కు సారాంశ పరీక్ష అంశసారానికి సంబంధించినవి; రక్షణ పేరుకు కాదు. సమీక్షించగలగడం, చెల్లకపోవడం, పూర్తయిన లావాదేవీల రక్షణ వేర్వేరు ప్రశ్నలు; తేదీ లేదా పేరు ఒక్కటే అన్నింటికీ సమాధానం కాదు.',
'Option2 follows the direct-effect inquiry.1gives blanket immunity,3conflates every rights breach with basic-structure damage,4substitutes form for effect.',fmt='application',difficulty='hard')

add('coelho-invalid-reinserted','paragraph14point5','direct',CO,'Conclusion(v), second limb',
'A law held to violate PartIIIand later inserted in the Ninth Schedule after24April1973 remains open to the specified basic-structure challenge under Coelho.',
'మూడవ భాగాన్ని ఉల్లంఘించిందని నిర్ధారించిన చట్టాన్ని1973ఏప్రిల్24తరువాత తొమ్మిదవ షెడ్యూల్‌లో చేర్చినా, కోయెల్హో ప్రకారం నిర్దిష్ట ప్రాథమిక నిర్మాణ సవాలు కొనసాగవచ్చు.',
'A law held to violate PartIIIis later inserted into the Ninth Schedule after24April1973. Under Coelho, which statement is correct?',
'మూడవ భాగాన్ని ఉల్లంఘించిందని నిర్ధారించిన చట్టాన్ని1973ఏప్రిల్24తరువాత తొమ్మిదవ షెడ్యూల్‌లో చేర్చారు. కోయెల్హో ప్రకారం సరైనది ఏది?',
['It remains open to challenge for basic-structure damage on the specified rights-based test','Its insertion necessarily cures every constitutional defect','The earlier adverse ruling becomes a guarantee of permanent immunity','Only Parliament may examine its constitutional validity'],
['నిర్దిష్ట హక్కుల ఆధారిత పరీక్షపై ప్రాథమిక నిర్మాణ నష్టానికి సవాలు చేయవచ్చు','చేర్పు తప్పనిసరిగా ప్రతి రాజ్యాంగ లోపాన్నీ సరిచేస్తుంది','పూర్వ ప్రతికూల తీర్పే శాశ్వత మినహాయింపుకు హామీ అవుతుంది','దాని రాజ్యాంగబద్ధతను పార్లమెంటు మాత్రమే పరిశీలించవచ్చు'],1,
'Conclusion(v)distinguishes two situations. Laws already upheld by the Supreme Court receive its stated saving; a law held violative of PartIIIand later inserted after the cutoff is still open to the specified challenge. The existing canonical question tests the already-upheld limb, whereas this item tests the earlier-invalidated limb.',
'నిర్ధారణ(v)రెండు సందర్భాలను వేరు చేస్తుంది. సుప్రీంకోర్టు ఇప్పటికే చెల్లుబాటును సమర్థించిన చట్టాలకు పేర్కొన్న రక్షణ ఉంటుంది; మూడవ భాగాన్ని ఉల్లంఘించిందని నిర్ధారించి, గడువు తరువాత చేర్చిన చట్టంపై నిర్దిష్ట సవాలు కొనసాగవచ్చు. పాత కానానికల్ ప్రశ్న ఇప్పటికే సమర్థించిన చట్టం భాగాన్ని పరీక్షిస్తుంది; ఈ ప్రశ్న పూర్వం చెల్లదని నిర్ధారించిన భాగాన్ని పరీక్షిస్తుంది.',
'Option1 matches the second limb of conclusion(v).2/3turn insertion or prior invalidity into absolute immunity;4excludes judicial adjudication.',fmt='application',difficulty='hard')

add('coelho-finalised-transactions','paragraph14point6','direct',CO,'Conclusion(vi)',
'Coelho expressly saved action taken and transactions finalised under the impugned Acts from challenge under its stated conclusion.',
'సవాలు చేసిన చట్టాల ఫలితంగా చేపట్టిన చర్యలు, పూర్తయిన లావాదేవీలను తన నిర్దిష్ట తుది నిర్ధారణ ప్రకారం సవాలు నుంచి కోయెల్హో స్పష్టంగా రక్షించింది.',
'Which saving did Coelho expressly state regarding the impugned Acts?',
'సవాలు చేసిన చట్టాల విషయంలో కోయెల్హో ఏ రక్షణను స్పష్టంగా పేర్కొంది?',
['Every pending and future dispute was permanently barred','Every completed transaction had to be reopened automatically','Action taken and transactions finalised as a result of those Acts were not to be challenged','Only transactions approved personally by the President were saved'],
['పెండింగ్, భవిష్యత్తు వివాదాలన్నింటిపై శాశ్వత నిషేధం','పూర్తయిన ప్రతి లావాదేవీని స్వయంచాలకంగా తిరిగి తెరవాలి','ఆ చట్టాల ఫలితంగా చేపట్టిన చర్యలు, పూర్తయిన లావాదేవీలను సవాలు చేయరాదు','రాష్ట్రపతి వ్యక్తిగతంగా ఆమోదించిన లావాదేవీలకే రక్షణ'],3,
'Conclusion(vi)is a specific finality saving. It must not be enlarged into immunity for every future action, or into a universal rule that completed transactions under any unconstitutional law can never be questioned. The wording here stays tied to Coelho’s impugned Acts and its operative conclusion.',
'నిర్ధారణ(vi)నిర్దిష్ట తుది స్థితి రక్షణ. దానిని ప్రతి భవిష్యత్తు చర్యకు మినహాయింపుగా లేదా ఏ రాజ్యాంగ విరుద్ధ చట్టం కింద పూర్తయిన లావాదేవీనైనా ఎప్పటికీ ప్రశ్నించలేమనే సర్వసాధారణ నియమంగా విస్తరించకూడదు. ఇక్కడి భాష కోయెల్హోలో సవాలు చేసిన చట్టాలు, దాని తుది నిర్ధారణకే పరిమితమవుతుంది.',
'Option3 paraphrases the specific saving.1adds future blanket immunity,2reverses finality,4invents presidential approval.',difficulty='hard')

add('countermajoritarian-criticism','paragraphs16–17; table10','direct',C,'Articles124,217: appointed courts; constitutional-democracy analysis in supplied reader',
'The counter-majoritarian criticism of judicial review concerns unelected judges invalidating laws made by elected representatives; it does not itself prove constitutional review illegitimate.',
'న్యాయ సమీక్షపై కౌంటర్-మెజారిటేరియన్ విమర్శ ఎన్నిక కాని న్యాయమూర్తులు ఎన్నికైన ప్రతినిధుల చట్టాలను చెల్లనివిగా చేయడంపై ఉంటుంది; ఆ విమర్శ ఒక్కటే రాజ్యాంగ సమీక్ష చట్టవిరుద్ధమని నిరూపించదు.',
'What is the counter-majoritarian difficulty commonly raised against judicial review?',
'న్యాయ సమీక్షపై సాధారణంగా ప్రస్తావించే కౌంటర్-మెజారిటేరియన్ సమస్య ఏమిటి?',
['Every judicial decision must receive a public referendum','Only the executive can interpret a written Constitution','The Constitution forbids courts from examining statutes','Unelected judges may invalidate legislation enacted by elected representatives'],
['ప్రతి న్యాయ నిర్ణయానికి ప్రజాభిప్రాయ సేకరణ అవసరం','లిఖిత రాజ్యాంగాన్ని కార్యనిర్వాహక శాఖ మాత్రమే వ్యాఖ్యానించగలదు','చట్టాలను పరిశీలించకుండా రాజ్యాంగం కోర్టులను నిషేధిస్తుంది','ఎన్నిక కాని న్యాయమూర్తులు ఎన్నికైన ప్రతినిధులు చేసిన చట్టాలను చెల్లనివిగా చేయవచ్చు'],4,
'The criticism concerns the tension between electoral majorities and appointed courts. The reader’s constitutional-democracy answer is that elected power remains subject to prior constitutional limits. Identifying the criticism does not establish unlimited judicial power or erase democratic accountability concerns.',
'ఈ విమర్శ ఎన్నికల మెజారిటీలు, నియమిత కోర్టుల మధ్య ఉన్న ఉద్రిక్తతకు సంబంధించినది. ఎన్నికైన అధికారం ముందుగా నిర్దేశించిన రాజ్యాంగ పరిమితులకు లోబడి ఉంటుందనేది పాఠ్యంలోని రాజ్యాంగ ప్రజాస్వామ్య సమాధానం. విమర్శను గుర్తించడం అపరిమిత న్యాయాధికారాన్ని స్థాపించదు; ప్రజాస్వామ్య జవాబుదారీతనం ఆందోళనలను తొలగించదు.',
'Option4 identifies the actual democratic-theory criticism.1requires a referendum not posited by the concept,2and3replace review with executive monopoly or prohibition.',difficulty='easy')

add('article31b-limited-shield','paragraph12; table9','partial',C,'Article31B: rights conferred by this Part; subject to governing basic-structure doctrine',
'Article31B’s express validation addresses PartIIIrights objections, not a blanket cure for every constitutional defect such as lack of legislative competence.',
'ప్రకరణ31Bలోని స్పష్టమైన చెల్లుబాటు రక్షణ మూడవ భాగం హక్కుల అభ్యంతరాలకు సంబంధించినది; శాసనాధికారం లేకపోవడం వంటి ప్రతి రాజ్యాంగ లోపాన్నీ సరిచేసే సంపూర్ణ రక్షణ కాదు.',
'A lawyer argues that Article31B automatically cures every constitutional defect, including absence of legislative competence, simply because a law appears in the Ninth Schedule. Which assessment is correct?',
'ఒక చట్టం తొమ్మిదవ షెడ్యూల్‌లో ఉన్నందున శాసనాధికారం లేకపోవడం సహా ప్రతి రాజ్యాంగ లోపాన్నీ ప్రకరణ31B స్వయంచాలకంగా సరిచేస్తుందని న్యాయవాది వాదించారు. సరైన అంచనా ఏది?',
['Correct: Article31Boverrides the entire Constitution without limits','Incorrect: its express shield concerns PartIIIrights objections and is not universal constitutional immunity','Correct: every listed Act becomes a constitutional provision','Incorrect only because the Ninth Schedule protects executive orders alone'],
['సరైనది: ప్రకరణ31B పరిమితులు లేకుండా మొత్తం రాజ్యాంగాన్ని అధిగమిస్తుంది','సరికాదు: దాని స్పష్టమైన రక్షణ మూడవ భాగం హక్కుల అభ్యంతరాలకు సంబంధించినది; అది సర్వవ్యాప్త రాజ్యాంగ మినహాయింపు కాదు','సరైనది: జాబితాలోని ప్రతి చట్టం రాజ్యాంగ నిబంధన అవుతుంది','తొమ్మిదవ షెడ్యూల్ కార్యనిర్వాహక ఉత్తర్వులను మాత్రమే రక్షిస్తుంది కాబట్టి మాత్రమే సరికాదు'],2,
'Article31Brefers to inconsistency with or abridgement of rights conferred by PartIII. That wording must not be enlarged into immunity against every constitutional ground. The applicable Coelho/basic-structure qualifications also remain. The question identifies the shield’s subject, rather than assuming all Ninth Schedule laws are unreviewable.',
'ప్రకరణ31B మూడవ భాగం కల్పించిన హక్కులకు విరుద్ధత లేదా వాటి తగ్గింపును ప్రస్తావిస్తుంది. ఆ భాషను ప్రతి రాజ్యాంగ ఆధారం నుంచి మినహాయింపుగా విస్తరించకూడదు. వర్తించే కోయెల్హో/ప్రాథమిక నిర్మాణ పరిమితులు కూడా కొనసాగుతాయి. ఈ ప్రశ్న రక్షణ విషయాన్ని గుర్తిస్తుంది; తొమ్మిదవ షెడ్యూల్ చట్టాలన్నీ సమీక్షించలేనివని ఊహించదు.',
'Option2 preserves the text’s PartIIIboundary.1claims total override,3changes statutory rank,4misidentifies the protected instruments.',fmt='application',difficulty='hard')

add('federal-government-party-combinations','table3 rowArticle131','partial',C,'Article131(b),(c), with legal-right question requirement',
'Article131includes Union and one or more States on one side against one or more other States, and disputes between two or more States, where the specified legal-right condition is met.',
'నిర్దేశిత చట్టపరమైన హక్కు షరతు నెరవేరితే, ఒకవైపు కేంద్రం, ఒకటి లేదా ఎక్కువ రాష్ట్రాలు మరోవైపు ఇతర రాష్ట్రాలతో ఉన్న వివాదాలు, రెండు లేదా ఎక్కువ రాష్ట్రాల మధ్య వివాదాలు ప్రకరణ131లో చేరుతాయి.',
'Subject to Article131’s legal-right requirement, which government-party combinations are expressly included?1.Union and one or more States on one side versus one or more other States.2.Two or more States.3.An ordinary private company versus another private company.',
'ప్రకరణ131లోని చట్టపరమైన హక్కు షరతుకు లోబడి ఏ ప్రభుత్వ కక్షిదారు సమూహాలు స్పష్టంగా చేరుతాయి?1.ఒకవైపు కేంద్రం, ఒకటి లేదా ఎక్కువ రాష్ట్రాలు; మరోవైపు ఒకటి లేదా ఎక్కువ ఇతర రాష్ట్రాలు.2.రెండు లేదా ఎక్కువ రాష్ట్రాలు.3.ఒక సాధారణ ప్రైవేటు కంపెనీ, మరో ప్రైవేటు కంపెనీ.',
['1and2only','1and3only','2and3only','1,2and3'],['1,2 మాత్రమే','1,3 మాత్రమే','2,3 మాత్రమే','1,2,3'],1,
'Clauses(b)and(c)provide the first two government-party configurations; the dispute must involve a question on which the existence or extent of a legal right depends. The private-company pair does not qualify. Existing practice identifies a simple Union–State dispute and excludes a private claimant; this item tests the additional multi-government configurations.',
'ఖండికలు(b),(c)మొదటి రెండు ప్రభుత్వ కక్షిదారు ఏర్పాట్లను కల్పిస్తాయి; చట్టపరమైన హక్కు ఉనికి లేదా పరిధి ఆధారపడే ప్రశ్న వివాదంలో ఉండాలి. ప్రైవేటు కంపెనీల జతకు అర్హత లేదు. పాత సాధనలో సాధారణ కేంద్ర–రాష్ట్ర వివాదాన్ని గుర్తించి, వ్యక్తిగత కక్షిదారును మినహాయించారు; ఈ ప్రశ్న అదనపు బహుళ ప్రభుత్వ ఏర్పాట్లను పరీక్షిస్తుంది.',
'1and2are express government-party combinations;3is a private dispute. Option1alone has the correct set.',fmt='statement-combination')

def read(n):return json.loads((P/n).read_text(encoding='utf-8-sig'))
def save(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
bank=read('Questions.json');facts=read('Fact-register.json');ex=read('Explanations.json');reviews=[]
import re
def prose(t):
 for old,new in [('ListIII','List III'),('ListII','List II'),('ListI','List I'),('PartIII','Part III')]:t=t.replace(old,new)
 t=re.sub(r'(?<=[A-Za-z])(?=\d)|(?<=\d)(?=[A-Za-z])',' ',t)
 t=re.sub(r'(\d) ([A-Z])\b',r'\1\2',t)
 t=re.sub(r'([?:.])(?=\d)',r'\1 ',t)
 t=re.sub(r'(?<=\d)\.(?=[A-Za-z])','. ',t)
 return t
for r in rows:
 fid='POL-751-'+r['slug'];qid='POL-751-AT-'+r['slug']
 for k in ('fen','qe','ee','solve'):r[k]=prose(r[k])
 r['oe']=[prose(x) for x in r['oe']]
 fact={'id':fid,'fact_en':r['fen'],'fact_te':r['fte'],'sources':['Supplied prepared Laxmikanth Ch27 '+r['loc'],r['primary']+' | '+r['provision']],'source_match':{'classification':r['match'],'prepared_locator':r['loc'],'qualification':'Prepared reader is not certified publisher-original. Primary evidence supplies precise constitutional limits; conflicts are corrected only in study content, not source transcription.'},'status':'academic_validated_manual_review_pending_independent_second_review','assessment_target':r['fen'],'question_ids':[qid],'source_exactness_certified':False}
 if r['slug']=='judicial-observations':fact['sources'].extend([MM+' | Chandrachud majority opinion, reportp241',RJ+' | State of Rajasthan quotation attributed to Bhagwati'])
 question={'id':qid,'kind':'original-supplied-reader','source_page':None,'source_scope':'Prepared Ch27 and cited primary qualification; no locked GBK/Notes/image reading','source_type':'original-authored-not-PYQ','fact_ids':[fid],'tested_fact_ids':[fid],'format':r['fmt'],'difficulty':r['difficulty'],'question_en':r['qe'],'question_te':r['qt'],'options_en':r['oe'],'options_te':r['ot'],'answer':r['key'],'explanation_id':qid,'assessment_target':r['fen'],'coverage_limit':'Only the actual assessed association/rule; supplied context and explanation-only facts are not independently counted.','status':'approved_manual_solution_pending_independent_second_review'}
 facts['facts']=[x for x in facts['facts'] if x['id']!=fid]+[fact]
 bank['questions']=[x for x in bank['questions'] if x['id']!=qid]+[question]
 sources=[{'url':r['primary'],'locator':r['provision']},{'source':'Supplied prepared Ch27','locator':r['loc']}]
 if r['slug']=='judicial-observations':sources.extend([{'url':MM,'locator':'Chandrachud majority opinion, reportp241'},{'url':RJ,'locator':'State of Rajasthan quotation attributed to Bhagwati at reportpp644ff'}])
 ex['explanations'][qid]={'en':r['ee'],'te':r['et'],'fact_ids':[fid],'references':sources}
 reviews.append({'question_id':qid,'solved_answer':r['key'],'all_option_solution':r['solve'],'bilingual_review':'Manually compared both stems, four options and separate explanations, including actors, temporal and extent qualifications.','actual_assessed_facet':r['fen'],'source_locator':r['loc'],'source_match':r['match'],'primary_url':r['primary'],'primary_locator':r['provision'],'dedup_review':'All current g2 normal-bank stems and options searched read-only. Related but distinct examples and mere distractor mentions were not counted as equivalent assessed targets.','result':'approved_manual_academic_review','source_exactness_certified':False})
 related={
 'marbury-year':('7.5.1','POL-751-P297-ORIGIN-01','Old item supplies1803in its stem and tests the case–judge pair, not the year.'),
 'delegated-legislation-review':('7.2.4','POL-724-P246-01','Old item identifies the parliamentary committee, not the judicial reviewability of a delegated norm.'),
 'certificate-consideration':('7.4.1','POL-741-AT-constitutional-appeal','Old item tests the certificate route for a constitutional appeal, not mandatory consideration after the immediate oral application.'),
 'legislative-lists':('6.1.3','POL-613-N004','Existing matching item identifies Article246as successor to legislative-list distribution, not the respective powers for ListsI/II/III.'),
 'preconstitutional-continuance':('6.4.1','POL-6.1.9-P125-02','Existing item tests special Article35(b)laws and parliamentary continuation; new item tests the general Article372rule subject to Constitution and competent authority.'),
 'ninth-insertion-mechanism':('6.7.1','POL-671-P514-002','Existing item tests historical land-reform use and lack of automatic inclusion; new item tests the State-enactment versus parliamentary constitutional-amendment actor/procedure distinction.'),
 'ninth-lettered-entry':('6.4.1','POL-641-N006','Existing item retrieves the76thAmendment; the new stem supplies that amendment and tests the entry257Aidentifier.'),
 'coelho-impact-not-form':('6.8.1','POL-681-N002','Existing item tests basic-structure/rights review and the saving for laws already upheld; new item distinguishes actual impact from form and every-rights-breach automatic invalidity.'),
 'coelho-invalid-reinserted':('6.8.1','POL-681-N002','Existing item tests the previously-upheld limb; new item tests the earlier-invalidated-then-inserted limb.'),
 'federal-government-party-combinations':('7.4.1','POL-741-P293-01','Existing item identifies Article131in a simple Union–State dispute; the new item tests clauses(b)/(c)multi-government configurations. The private-party exclusion is related background, not the new coverage claim.')}
 if r['slug'] in related:
  ch,other,why=related[r['slug']];reviews[-1]['related_but_distinct']={'chapter':ch,'id':other,'reason':why}
bank['status']='manual_atomic_reader_expansion_with_canonical_reuse_independent_review_pending'
bank['full_chapter_coverage']=False;facts['full_chapter_coverage']=False
save('Questions.json',bank);save('Fact-register.json',facts);save('Explanations.json',ex)
save('reader-atomic-question-review.json',{'chapter':'7.5.1','new_questions':len(rows),'existing_ids_preserved':True,'reviews':reviews,'full_chapter_coverage':False,'source_exactness_certified':False,'ui_testing':False})
print('New questions',len(rows),'bank',len(bank['questions']),'facts',len(facts['facts']))
