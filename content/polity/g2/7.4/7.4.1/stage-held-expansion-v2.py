"""Stage follow-on candidates ONLY. Never edits Questions/Facts/Explanations.
The coordinator must independently review and explicitly integrate selected items.
No locked source, Notes or images are accessed.
"""
import json
from pathlib import Path
P=Path(__file__).parent
C='https://www.legislative.gov.in/static/uploads/2025/07/359f70a69695affb9d72f8393102bd2e.pdf'
RULES='https://cdnbbsr.s3waas.gov.in/s3ec0490f1f4972d133619a60c30f3559e/uploads/2024/01/2024011691-1.pdf'
HIST='https://www.sci.gov.in/about-department/history/'
INQ='https://www.indiacode.nic.in/bitstream/123456789/1539/2/A1968-51.pdf'
CONT='https://www.indiacode.nic.in/bitstream/123456789/15384/1/the_contempt_of_courts_act%2C_1971.pdf'
GRAM='https://thc.nic.in/Central%20Governmental%20Acts/Gram%20Nyayalayas%20Act,%202008.pdf'
FAM='https://www.indiacode.nic.in/bitstream/123456789/1844/1/A1984__66.pdf'
rows=[]
def add(slug,held,reader,match,url,loc,fe,ft,qe,qt,oe,ot,key,ee,et,review,fmt='single-best-answer',level='moderate',ready=True):
 rows.append(dict(slug=slug,held=held,reader=reader,match=match,url=url,loc=loc,fe=fe,ft=ft,qe=qe,qt=qt,oe=oe,ot=ot,key=key,ee=ee,et=et,review=review,fmt=fmt,level=level,ready=ready))

add('original-eight',['GBK741-287-02'],'Ch26 paragraph3; table1','direct',HIST,'History: original Constitution envisaged CJI plus7puisne judges',
'The original Supreme Court composition envisaged the CJI and seven other judges, eight in total, until Parliament enlarged the number.',
'మొదటి రాజ్యాంగ ఏర్పాటు ప్రధాన న్యాయమూర్తి, మరో ఏడుగురు న్యాయమూర్తులు కలిపి ఎనిమిది మందిని ఊహించింది; పార్లమెంటు తరువాత సంఖ్యను పెంచవచ్చు.',
'What was the Supreme Court’s original total strength envisaged in the Constitution, including the CJI?',
'ప్రధాన న్యాయమూర్తితో కలిపి రాజ్యాంగం మొదట ఊహించిన సుప్రీంకోర్టు మొత్తం బలం ఎంత?',
['7','8','11','14'],['7','8','11','14'],2,
'The original arrangement was one CJI plus seven puisne judges. Seven is the number of other judges, not the total. Parliament could enlarge the number by law. The original wording must not be described as a permanent minimum floor or confused with a later sanctioned strength.',
'మొదటి ఏర్పాటు ఒక ప్రధాన న్యాయమూర్తి, మరో ఏడుగురు సాధారణ న్యాయమూర్తులు. ఏడు అనేది ఇతర న్యాయమూర్తుల సంఖ్య; మొత్తం కాదు. పార్లమెంటు చట్టం ద్వారా సంఖ్యను పెంచవచ్చు. మొదటి పాఠ్యాన్ని శాశ్వత కనీస పరిమితిగా లేదా తరువాతి మంజూరు బలంగా భావించకూడదు.',
'2correct:8includesCJI;1omitsCJI;3/4are later totals.',level='easy')

add('apex-replacement',['GBK741-286-05'],'Ch26 paragraph2','direct','https://cdnbbsr.s3waas.gov.in/s3ec0490f1f4972d133619a60c30f3559e/uploads/2024/07/2024071334.pdf','Official Supreme Court report, Court Buildings, introductory paragraph',
'The Supreme Court succeeded the Federal Court and the Judicial Committee of the Privy Council’s apex appellate role in the new constitutional system.',
'కొత్త రాజ్యాంగ వ్యవస్థలో సుప్రీంకోర్టు ఫెడరల్ కోర్టు, ప్రివీ కౌన్సిల్ న్యాయ కమిటీ యొక్క అగ్ర అప్పీల్ పాత్రలను స్వీకరించింది.',
'Which pair identifies the earlier apex institutions whose roles the Supreme Court succeeded in the1950constitutional system?',
'1950రాజ్యాంగ వ్యవస్థలో సుప్రీంకోర్టు పాత్రలు స్వీకరించిన పూర్వ అగ్ర సంస్థలను ఏ జత గుర్తిస్తుంది?',
['Federal Court and every State High Court','Calcutta High Court and the Election Commission','Federal Court and Judicial Committee of the Privy Council','Constituent Assembly and Public Service Commission'],
['ఫెడరల్ కోర్టు, ప్రతి రాష్ట్ర హైకోర్టు','కలకత్తా హైకోర్టు, ఎన్నికల కమిషన్','ఫెడరల్ కోర్టు, ప్రివీ కౌన్సిల్ న్యాయ కమిటీ','రాజ్యాంగ పరిషత్తు, పబ్లిక్ సర్వీస్ కమిషన్'],3,
'The new Supreme Court replaced the Federal Court and the final Privy Council appeal arrangement. High Courts continued in the integrated system. This tests institutional succession, not the separate26January constitutional commencement versus28January inauguration dates.',
'కొత్త సుప్రీంకోర్టు ఫెడరల్ కోర్టు, తుది ప్రివీ కౌన్సిల్ అప్పీల్ ఏర్పాటును భర్తీ చేసింది. హైకోర్టులు సమీకృత వ్యవస్థలో కొనసాగాయి. ఈ ప్రశ్న సంస్థాగత వారసత్వాన్ని పరీక్షిస్తుంది; జనవరి26రాజ్యాంగ ఆవిర్భావం, జనవరి28ప్రారంభోత్సవం అనే వేరు తేదీలను కాదు.',
'3correct;1wronglyabolishesHCs;2/4pair institutions outside this succession.',level='easy')

add('building-architect',['GBK741-286-08'],'Absent from Ch26','absent','https://cdnbbsr.s3waas.gov.in/s3ec0490f1f4972d133619a60c30f3559e/uploads/2024/07/2018-19.pdf','Supreme Court annual report2018–19, Building, Precincts and Architecture',
'Chief Architect Ganesh Bhikaji Deolalikar designed the original Supreme Court building.',
'ముఖ్య వాస్తుశిల్పి గణేష్ భికాజీ దేవ్‌లాలికర్ అసలు సుప్రీంకోర్టు భవనాన్ని రూపొందించారు.',
'Who designed the original building of the Supreme Court of India?',
'భారత సుప్రీంకోర్టు అసలు భవనాన్ని ఎవరు రూపొందించారు?',
['Ganesh Bhikaji Deolalikar','Edwin Lutyens','Herbert Baker','Le Corbusier'],
['గణేష్ భికాజీ దేవ్‌లాలికర్','ఎడ్విన్ ల్యూటెన్స్','హెర్బర్ట్ బేకర్','లే కార్బూసియర్'],1,
'The Court’s own annual report names Ganesh Bhikaji Deolalikar as the chief architect. The other names are associated with major architectural projects in India but are not the designer identified for this building. The primary evidence fills an absent prepared-reader detail without certifying the locked source’s wording.',
'కోర్టు స్వంత వార్షిక నివేదిక గణేష్ భికాజీ దేవ్‌లాలికర్‌ను ముఖ్య వాస్తుశిల్పిగా పేర్కొంటుంది. ఇతర పేర్లు భారతదేశంలోని ప్రముఖ నిర్మాణాలతో సంబంధం ఉన్నప్పటికీ ఈ భవనానికి పేర్కొన్న రూపకర్తలు కాదు. సిద్ధం చేసిన పాఠ్యంలో లేని వివరాన్ని ప్రాథమిక ఆధారం భర్తీ చేస్తుంది; లాక్ చేసిన మూల పాఠ్య ఖచ్చితత్వాన్ని ధ్రువీకరించదు.',
'1is officially named;2/3NewDelhi architects and4Chandigarh architect are plausible but incorrect alternatives.',level='easy')

add('oath-duties',['GBK741-291-02'],'Ch26 paragraph13','direct',C,'Article124(6); Third Schedule formIV',
'A Supreme Court judge’s oath includes fidelity to the Constitution, sovereignty/integrity, impartial performance and upholding the Constitution and laws.',
'సుప్రీంకోర్టు న్యాయమూర్తి ప్రమాణంలో రాజ్యాంగ విధేయత, సార్వభౌమత్వం/సమగ్రత, నిష్పాక్షిక విధి నిర్వహణ, రాజ్యాంగం-చట్టాల పరిరక్షణ ఉంటాయి.',
'Which undertakings belong to a Supreme Court judge’s prescribed oath?1.Uphold India’s sovereignty and integrity.2.Perform judicial duties without fear or favour, affection or ill-will.3.Always support the governing political party.',
'సుప్రీంకోర్టు న్యాయమూర్తి నిర్దేశిత ప్రమాణంలో ఏ బాధ్యతలు ఉంటాయి?1.భారత సార్వభౌమత్వం, సమగ్రతను కాపాడటం.2.భయం, పక్షపాతం, అనురాగం లేదా ద్వేషం లేకుండా న్యాయ విధులు నిర్వర్తించడం.3.పాలక రాజకీయ పార్టీకి ఎల్లప్పుడూ మద్దతివ్వడం.',
['1only','2and3only','1,2and3','1and2only'],['1 మాత్రమే','2,3 మాత్రమే','1,2,3','1,2 మాత్రమే'],4,
'The oath secures constitutional fidelity and impartiality, not party loyalty. It also requires upholding the Constitution and laws. The existing oath item asks who administers it and the Schedule; this item tests the substantive undertakings rather than repeating that authority question.',
'ఈ ప్రమాణం రాజ్యాంగ విధేయత, నిష్పాక్షికతను నిర్ధారిస్తుంది; పార్టీ విధేయతను కాదు. రాజ్యాంగం, చట్టాలను కాపాడటం కూడా ఇందులో ఉంటుంది. పాత ప్రమాణ ప్రశ్న ప్రమాణం చేయించే అధికారి, షెడ్యూల్‌ను అడుగుతుంది; ఈ ప్రశ్న ఆ అధికారి ప్రశ్నను పునరావృతం చేయకుండా మూల బాధ్యతలను పరీక్షిస్తుంది.',
'1and2true;3contradictsconstitutional impartiality.4is the correct combination.',fmt='statement-combination')

add('notice-admission-discretion',['GBK741-291-02'],'Ch26 paragraph17','direct',INQ,'Judges(Inquiry)Act1968section3(1)',
'A removal-motion notice with the required signatures does not compel admission; the Speaker or Chairman may admit or refuse after the statutory consideration.',
'అవసరమైన సంతకాలు ఉన్న తొలగింపు తీర్మానం నోటీసును తప్పనిసరిగా అనుమతించాల్సిన అవసరం లేదు; చట్టప్రకారం పరిశీలించి స్పీకర్ లేదా చైర్మన్ అనుమతించవచ్చు లేదా తిరస్కరించవచ్చు.',
'A judge-removal notice has the required100LokSabha signatures. Does that fact alone compel the Speaker to admit it?',
'న్యాయమూర్తి తొలగింపు నోటీసుకు అవసరమైన100మంది లోక్‌సభ సభ్యుల సంతకాలు ఉన్నాయి. ఆ కారణం ఒక్కటే దానిని అనుమతించాలని స్పీకర్‌ను నిర్బంధిస్తుందా?',
['No; the Speaker may admit or refuse it after the statutory consideration','Yes; signatures themselves remove the judge','Yes; the Speaker has no admission decision','No; only the Chief Election Commissioner may admit it'],
['లేదు; చట్టప్రకారం పరిశీలించి స్పీకర్ అనుమతించవచ్చు లేదా తిరస్కరించవచ్చు','అవును; సంతకాలే న్యాయమూర్తిని తొలగిస్తాయి','అవును; అనుమతిపై స్పీకర్‌కు నిర్ణయాధికారం లేదు','లేదు; ప్రధాన ఎన్నికల కమిషనర్ మాత్రమే అనుమతించవచ్చు'],1,
'The signature threshold and admission decision are different stages. Section3authorises admission or refusal after considering the material and such consultation as the presiding officer thinks fit. A notice does not itself remove the judge. The current bank separately tests100/50signature thresholds and committee composition.',
'సంతకాల పరిమితి, నోటీసు అనుమతి వేర్వేరు దశలు. సమాచారం, సభాధ్యక్షుడు సముచితమని భావించే సంప్రదింపులను పరిశీలించిన తరువాత అనుమతి లేదా తిరస్కరణకు సెక్షన్3అధికారం ఇస్తుంది. నోటీసు ఒక్కటే న్యాయమూర్తిని తొలగించదు. ప్రస్తుత బ్యాంకులో100/50సంతకాల పరిమితి, కమిటీ నిర్మాణాన్ని వేరుగా పరీక్షించారు.',
'1correct;2confusesnoticewithremoval,3deniesexpressdiscretion,4invents the wrong constitutional authority.',fmt='application')

add('retired-judge-allowances',['GBK741-288-05'],'Ch26 paragraph22','direct',C,'Article128',
'Allowances of a retired judge attending under Article128are determined by the President.',
'ప్రకరణ128కింద విచారణకు హాజరయ్యే పదవీ విరమణ చేసిన న్యాయమూర్తి భత్యాలను రాష్ట్రపతి నిర్ణయిస్తారు.',
'Who determines the allowances of a retired judge requested to sit in the Supreme Court under Article128?',
'ప్రకరణ128కింద సుప్రీంకోర్టులో విచారణకు హాజరు కావాలని కోరిన పదవీ విరమణ చేసిన న్యాయమూర్తి భత్యాలను ఎవరు నిర్ణయిస్తారు?',
['The Governor of the former HighCourt State','The President','The LokSabha Speaker','The retired judge unilaterally'],
['పూర్వ హైకోర్టు రాష్ట్ర గవర్నర్','రాష్ట్రపతి','లోక్‌సభ స్పీకర్','పదవీ విరమణ చేసిన న్యాయమూర్తి ఏకపక్షంగా'],2,
'Article128assigns allowance determination to the President. This is distinct from the two consents needed for attendance and from Parliament’s general judicial-salary lawmaking. While attending, the person has the specified Supreme Court powers and privileges without thereby receiving a fresh permanent appointment.',
'ప్రకరణ128 భత్యాల నిర్ణయాన్ని రాష్ట్రపతికి అప్పగిస్తుంది. ఇది హాజరుకు అవసరమైన రెండు సమ్మతులు, సాధారణ న్యాయమూర్తి వేతనాలపై పార్లమెంటు చట్టం చేయడం నుంచి భిన్నం. హాజరు సమయంలో నిర్దిష్ట సుప్రీంకోర్టు అధికారాలు, ప్రత్యేక హక్కులు ఉంటాయి; కొత్త శాశ్వత నియామకం లభించినట్లు కాదు.',
'2isexpress;1/3wrongoffices;4removesconstitutional determination.',level='easy')

add('cji-seniority-fitness',['GBK741-287-10'],'Ch26 paragraphs10–11; table5, qualified','partial','https://api.sci.gov.in/jonew/judis/43070.pdf','Official SC2015NJAC judgment, MoPsummary paragraph3.1(search-index text)',
'The MoP convention is appointment of the senior-most Supreme Court judge considered fit as CJI; it is not an express constitutional seniority-alone election rule.',
'ఎంఓపీ సంప్రదాయం ప్రకారం తగినవారిగా భావించే అత్యంత సీనియర్ సుప్రీంకోర్టు న్యాయమూర్తిని ప్రధాన న్యాయమూర్తిగా నియమిస్తారు; రాజ్యాంగంలో సీనియారిటీ ఒక్కటే ఎన్నిక నియమంగా లేదు.',
'Which statement most accurately describes the conventional criterion for CJI appointment in the MoP?',
'ఎంఓపీలో ప్రధాన న్యాయమూర్తి నియామకానికి సంబంధించిన సంప్రదాయ ప్రమాణాన్ని ఏ వాక్యం అత్యంత ఖచ్చితంగా తెలుపుతుంది?',
['Every retiring HighCourt ChiefJustice must be elected CJI','Seniority is irrelevant in all circumstances','The senior-most SupremeCourt judge considered fit is the conventional choice','The Constitution requires a nationwide judicial election'],
['పదవీ విరమణ చేసే ప్రతి హైకోర్టు ప్రధాన న్యాయమూర్తిని ఎన్నుకోవాలి','అన్ని సందర్భాల్లో సీనియారిటీకి సంబంధం లేదు','తగినవారిగా భావించే అత్యంత సీనియర్ సుప్రీంకోర్టు న్యాయమూర్తి సంప్రదాయ ఎంపిక','దేశవ్యాప్త న్యాయ ఎన్నికను రాజ్యాంగం కోరుతుంది'],3,
'The official judgment’s MoPsummary retains both seniority and fitness. Formal appointment remains presidential. The prepared reader overstates the position if it makes seniority alone an unconditional textual mandate; this question preserves the qualification and treats it as a convention/procedural norm.',
'అధికారిక తీర్పులోని ఎంఓపీ సారాంశం సీనియారిటీ, అర్హమైన స్థితి రెండింటినీ ఉంచుతుంది. అధికారిక నియామకం రాష్ట్రపతి చేస్తారు. సీనియారిటీ ఒక్కటే షరతుల్లేని రాజ్యాంగ ఆదేశమని సిద్ధం చేసిన పాఠ్యాన్ని చదివితే అది అతివ్యాప్తి అవుతుంది; ఈ ప్రశ్న పరిమితిని ఉంచి సంప్రదాయ/ప్రక్రియా నియమంగా పరిగణిస్తుంది.',
'3correct;1wrongcourt/process,2ignoresconvention,4invents election.')

add('judges-cases-principles',['GBK741-288-07','GBK741-288-08','GBK741-288-09'],'Ch26 paragraph6; tables3–4','direct','https://api.sci.gov.in/jonew/judis/43070.pdf','Historical JudgesCases discussion; precise first/second/third case primary locators still to be reconciled',
'FirstJudgesCase distinguished consultation from concurrence; the Second accorded primacy through concurrence; the Third required the expanded plural consultation associated with CJI plus four seniors.',
'మొదటి న్యాయమూర్తుల కేసు సంప్రదింపును సమ్మతి నుంచి వేరు చేసింది; రెండవది సమ్మతి ద్వారా ప్రాధాన్యాన్ని ఇచ్చింది; మూడవది ప్రధాన న్యాయమూర్తి, నలుగురు సీనియర్లతో సంబంధించే విస్తృత సమష్టి సంప్రదింపును కోరింది.',
'Match the JudgesCases with the supplied principles. A.FirstCase B.SecondCase C.ThirdCase.1.Expanded CJI-plus-four consultation2.Consultation not concurrence3.Judicial primacy through concurrence.Choose A–B–C.',
'న్యాయమూర్తుల కేసులను సిద్ధాంతాలతో జతపరచండి. A.మొదటి కేసు B.రెండవ కేసు C.మూడవ కేసు.1.ప్రధాన న్యాయమూర్తి, నలుగురితో విస్తృత సంప్రదింపు2.సంప్రదింపు అంటే సమ్మతి కాదు3.సమ్మతి ద్వారా న్యాయ ప్రాధాన్యం.A–B–C క్రమాన్ని ఎంచుకోండి.',
['1–2–3','2–1–3','3–2–1','2–3–1'],['1–2–3','2–1–3','3–2–1','2–3–1'],4,
'The standard historical sequence maps2–3–1. Dates should be separately labelled: S.P.Gupta was decided in1981but is often reported in1982; the later cases are1993and1998. This proposal does not independently test those dates or every MoPconsultation/dissent qualification. Primary locator verification remains an explicit gate.',
'సాధారణ చారిత్రక క్రమం2–3–1. తేదీలను వేరుగా గుర్తించాలి: ఎస్.పి.గుప్తా తీర్పు1981లో వెలువడినా1982నివేదికల్లో ప్రస్తావిస్తారు; తరువాతి కేసులు1993,1998. ఈ ప్రతిపాదన ఆ తేదీలను లేదా ప్రతి ఎంఓపీ సంప్రదింపు/వ్యతిరేక అభిప్రాయ పరిమితిని ప్రత్యేకంగా పరీక్షించదు. ఖచ్చిత ప్రాథమిక ఆధార స్థానాల ధ్రువీకరణ ఇంకా అవసరం.',
'A2,B3,C1gives4. Other codes transpose at least one historical principle. Reader-direct; precise primary-locator gate deliberately not concealed.',fmt='matching',ready=False)

add('criminal-appeal-1970',['GBK741-294-02'],'Ch26 table11 criminal appeals','direct','https://upload.indiacode.nic.in/view-casepdf?id=AC_CEN_3_3_00001_197028_1517807317180&type=act','SC(Enlargement of Criminal Appellate Jurisdiction)Act1970section2(a)',
'The1970Act gives a statutory appeal when a HighCourt reverses acquittal on appeal and imposes life imprisonment or at least ten years.',
'హైకోర్టు అప్పీల్‌లో నిర్దోషిత్వ ఉత్తర్వును రద్దు చేసి జీవిత ఖైదు లేదా కనీసం పదేళ్ల కారాగార శిక్ష విధిస్తే1970చట్టం చట్టబద్ధ అప్పీల్‌ను కల్పిస్తుంది.',
'A HighCourt reverses an acquittal on appeal and imposes ten years’ imprisonment. An accused is told that only a death sentence can provide an appeal as of right. Which qualification is relevant?',
'హైకోర్టు అప్పీల్‌లో నిర్దోషిత్వ ఉత్తర్వును రద్దు చేసి పదేళ్ల కారాగార శిక్ష విధించింది. హక్కుగా అప్పీల్‌కు మరణశిక్ష మాత్రమే ఆధారమని నిందితునికి చెప్పారు. ఏ పరిమితి గమనించాలి?',
['The1970Act also provides the specified life-or-at-least-ten-years statutory route','No statutory enlargement is constitutionally possible','Only the President can commute this into an appeal','Every sentence of any length has an automatic appeal'],
['1970చట్టం నిర్దిష్ట జీవిత ఖైదు/కనీసం పదేళ్ల చట్టబద్ధ మార్గాన్నీ కల్పిస్తుంది','రాజ్యాంగపరంగా చట్టబద్ధ విస్తరణ అసాధ్యం','రాష్ట్రపతి మాత్రమే దీన్ని అప్పీల్‌గా మార్చగలరు','ఎంతకాలం శిక్షకైనా స్వయంచాలక అప్పీల్ ఉంటుంది'],1,
'Section2(a)adds the specified reversal-of-acquittal route for life imprisonment or not less than ten years. Section2(b)also covers the specified withdrawal-for-own-trial route. This supplements Article134(1), rather than denying its death-sentence routes or converting every conviction into an automatic appeal.',
'సెక్షన్2(a) నిర్దోషిత్వ ఉత్తర్వు రద్దు సందర్భంలో జీవిత ఖైదు లేదా కనీసం పదేళ్ల శిక్షకు నిర్దిష్ట మార్గాన్ని చేర్చుతుంది. సెక్షన్2(b) తానే విచారించడానికి కేసును తెప్పించుకున్న నిర్దిష్ట మార్గాన్నీ కల్పిస్తుంది. ఇది ప్రకరణ134(1)కు అదనం; దాని మరణశిక్ష మార్గాలను నిరాకరించదు లేదా ప్రతి నేర నిర్ధారణనూ స్వయంచాలక అప్పీల్‌గా మార్చదు.',
'1matchesstatute;2denies134(2)/theAct;3wrongfunction;4overgeneralises all convictions.',fmt='application')

add('civil-appeal-thirtieth',['LAX741-civil-limit-removal'],'Ch26 tables11–12','direct','https://www.legislative.gov.in/static/uploads/2025/07/d6970667d71b0cdaad2ad22b9d44d39c.pdf','Constitution(ThirtiethAmendment)Act1972,objects and section2',
'The ThirtiethAmendmentAct1972 replaced the old monetary civil-appeal test in Article133with the general-importance/need-for-SCdecision certificate test.',
'ముప్పైవ సవరణ చట్టం1972 ప్రకరణ133లోని పాత ధన విలువ సివిల్ అప్పీల్ ప్రమాణం స్థానంలో సాధారణ ప్రాధాన్యం/సుప్రీంకోర్టు నిర్ణయం అవసరం అనే ధ్రువపత్ర పరీక్షను తెచ్చింది.',
'Which amendment replaced the old₹20,000valuation test for the Article133civil-appeal certificate route?',
'ప్రకరణ133సివిల్ అప్పీల్ ధ్రువపత్ర మార్గంలో పాత₹20,000ధన విలువ ప్రమాణాన్ని ఏ సవరణ భర్తీ చేసింది?',
['FifteenthAmendment1963','ThirtiethAmendment1972','Forty-secondAmendment1976','Forty-fourthAmendment1978'],
['పదిహేనవ సవరణ1963','ముప్పైవ సవరణ1972','నలభై రెండవ సవరణ1976','నలభై నాలుగవ సవరణ1978'],2,
'The official amendment’s objects expressly reject valuation as the rational yardstick and replace it with the relevant question-of-law certificate findings. Its short title is1972although assent was on22February1973and commencement was notified thereafter. The question tests the amendment identity, not those distinct dates.',
'అధికారిక సవరణ ఉద్దేశాలు ధన విలువను తగిన ప్రమాణంగా తిరస్కరించి సంబంధిత న్యాయ ప్రశ్న ధ్రువపత్ర నిర్ధారణలను ప్రవేశపెడతాయి.1973ఫిబ్రవరి22న ఆమోదం పొందినా సంక్షిప్త పేరు1972; అమలు ప్రారంభాన్ని తరువాత ప్రకటించారు. ఈ ప్రశ్న సవరణ గుర్తింపును పరీక్షిస్తుంది; ఆ వేరు తేదీలను కాదు.',
'2is the documented replacement;1 concerns other judicial changes,3/4are different later amendments.',level='easy')

add('review-thirty-days',['GBK741-296-02'],'Ch26 paragraph46','direct',RULES,'OrderXLVIIrule2; distinguish possible procedural relief from the ordinary prescribed period',
'The ordinary prescribed period for an SCreview petition under OrderXLVIIrule2is thirty days from the judgment/order sought to be reviewed.',
'సమీక్ష కోరే తీర్పు/ఉత్తర్వు తేదీ నుంచి సుప్రీంకోర్టు సమీక్ష పిటిషన్‌కు ఆర్డర్XLVIIనియమం2సాధారణంగా ముప్పై రోజుల కాలాన్ని నిర్దేశిస్తుంది.',
'What ordinary filing period does OrderXLVIIrule2prescribe for a SupremeCourt review petition, measured from the judgment or order sought to be reviewed?',
'సమీక్ష కోరే తీర్పు లేదా ఉత్తర్వు నుంచి లెక్కిస్తే, సుప్రీంకోర్టు సమీక్ష పిటిషన్‌కు ఆర్డర్XLVIIనియమం2ఏ సాధారణ దాఖలు కాలాన్ని నిర్దేశిస్తుంది?',
['15days','60days','30days','90days'],['15రోజులు','60రోజులు','30రోజులు','90రోజులు'],3,
'The rule states thirty days. This is distinct from the different special-leave limitation rules. The item asks the ordinary prescribed period, not whether delay can ever receive procedural relief; it does not make every review an automatic oral rehearing or an appeal.',
'నియమం ముప్పై రోజులను పేర్కొంటుంది. ఇది వేర్వేరు ప్రత్యేక అనుమతి అప్పీల్ గడువులకు భిన్నం. ప్రశ్న సాధారణ నిర్దేశిత కాలాన్నే అడుగుతుంది; ఆలస్యానికి ఎప్పటికీ ప్రక్రియా ఉపశమనం లభించదని కాదు. ప్రతి సమీక్ష స్వయంచాలక మౌఖిక పునర్విచారణ లేదా అప్పీల్ అవుతుందని కూడా కాదు.',
'3is30days;1/2/4are other familiar periods but not this rule.',level='easy')

add('civil-criminal-review-grounds',['LAX741-review-grounds'],'Ch26 paragraph46, primary qualification','partial',RULES,'OrderXLVIIrule1',
'SCcivil review uses the CPCOrderXLVIIrule1grounds; criminal review is restricted by the rule to error apparent on the face of the record.',
'సుప్రీంకోర్టు సివిల్ సమీక్షకు సీపీసీ ఆర్డర్XLVIIనియమం1ఆధారాలు వర్తిస్తాయి; క్రిమినల్ సమీక్షను రికార్డుపై స్పష్టమైన తప్పు ఆధారానికి సంబంధిత నియమం పరిమితం చేస్తుంది.',
'Which pair accurately reflects OrderXLVIIrule1of the SupremeCourt Rules?',
'సుప్రీంకోర్టు నియమాల్లోని ఆర్డర్XLVIIనియమం1ను ఏ జత సరిగ్గా తెలుపుతుంది?',
['Civil—any fresh appeal; criminal—any policy disagreement','Civil—no review; criminal—unlimited rehearing','Civil—President’s discretion; criminal—Governor’s permission','Civil—CPCOrderXLVIIrule1grounds; criminal—error apparent on the face of the record'],
['సివిల్—ఏ కొత్త అప్పీల్ అయినా; క్రిమినల్—ఏ విధాన విభేదమైనా','సివిల్—సమీక్ష లేదు; క్రిమినల్—అపరిమిత పునర్విచారణ','సివిల్—రాష్ట్రపతి విచక్షణ; క్రిమినల్—గవర్నర్ అనుమతి','సివిల్—సీపీసీ ఆర్డర్XLVIIనియమం1ఆధారాలు; క్రిమినల్—రికార్డుపై స్పష్టమైన తప్పు'],4,
'The express rule distinguishes civil and criminal review grounds. A general list of discovery,error and sufficient reason must not be copied as an unqualified rule for every criminal review. Review is not an ordinary merits appeal; admissibility and relevant procedural safeguards remain.',
'స్పష్టమైన నియమం సివిల్, క్రిమినల్ సమీక్ష ఆధారాలను వేరు చేస్తుంది. కొత్త ఆధారం, తప్పు, తగిన కారణం అనే సాధారణ జాబితాను ప్రతి క్రిమినల్ సమీక్షకూ షరతుల్లేకుండా వర్తింపజేయకూడదు. సమీక్ష సాధారణ అంశసార అప్పీల్ కాదు; అంగీకార, సంబంధిత ప్రక్రియా రక్షణలు కొనసాగుతాయి.',
'4is the exact distinction;1/2turnreviewintoappeal/unlimitedrehearing,3assigns judicial review to executive permission.',fmt='matching',level='hard')

add('aor-filing-and-appearance',['GBK741-309-05','GBK741-309-06'],'Absent from Ch26','absent',RULES,'OrderIVrules1(b),7(c); scope is advocates, not denial of party-in-person routes',
'Among advocates, only an Advocate-on-Record may file appearance or act for a party; another advocate may appear/plead if instructed by the AoR or permitted by Court.',
'న్యాయవాదులలో అడ్వకేట్-ఆన్-రికార్డ్ మాత్రమే కక్షిదారు తరఫున హాజరు నమోదు లేదా వ్యవహార నిర్వహణ చేయగలరు; ఇతర న్యాయవాది ఏఓఆర్ సూచనతో లేదా కోర్టు అనుమతితో హాజరై వాదించవచ్చు.',
'Under the SupremeCourt Rules, consider advocates’ roles:1.Only an Advocate-on-Record may file an appearance or act for a party.2.A non-AoRadvocate may appear and plead when instructed by the AoRor permitted by the Court.Which are correct?',
'సుప్రీంకోర్టు నియమాల ప్రకారం న్యాయవాదుల పాత్రలను పరిశీలించండి:1.అడ్వకేట్-ఆన్-రికార్డ్ మాత్రమే కక్షిదారు తరఫున హాజరు నమోదు లేదా వ్యవహార నిర్వహణ చేయగలరు.2.ఏఓఆర్ సూచనతో లేదా కోర్టు అనుమతితో ఇతర న్యాయవాది హాజరై వాదించవచ్చు.సరైనవి ఏవి?',
['Both1and2','1only','2only','Neither1nor2'],['1,2 రెండూ','1 మాత్రమే','2 మాత్రమే','1 కాదు,2 కాదు'],1,
'Filing/acting and appearing/pleading are different roles. Rules7(c)and1(b)provide the respective qualifications. Saying that every enrolled advocate may act without an AoRis wrong, but saying that no non-AoRcan ever address the Court is also wrong. Party-in-person arrangements are not abolished by an advocate-role question.',
'దాఖలు/వ్యవహార నిర్వహణ, హాజరు/వాదన వేర్వేరు పాత్రలు. నియమాలు7(c),1(b)వాటికి సంబంధించిన పరిమితులను కల్పిస్తాయి. నమోదు అయిన ప్రతి న్యాయవాదీ ఏఓఆర్ లేకుండానే వ్యవహరించవచ్చనడం తప్పు; ఏ ఇతర న్యాయవాదీ ఎప్పటికీ కోర్టులో వాదించలేరనడం కూడా తప్పు. న్యాయవాదుల పాత్రల ప్రశ్న స్వయంగా వాదించుకునే కక్షిదారు ఏర్పాట్లను రద్దు చేయదు.',
'Both statements track the separate rules;1only/2onlyomitatrueclause andneitherdeniesboth.',fmt='statement-combination')

add('senior-advocate-designation',['GBK741-309-04'],'Absent from Ch26','absent','https://upload.indiacode.nic.in/showfile?actid=AC_CEN_3_46_00001_196125_1517807320172&filename=a1961-25.pdf&type=actfile','AdvocatesAct1961section16(2)',
'The SupremeCourt or a HighCourt may designate a consenting advocate as senior advocate under section16(2), subject to the statutory distinction criteria.',
'చట్టంలోని ప్రత్యేక గుర్తింపు ప్రమాణాలకు లోబడి, సమ్మతించే న్యాయవాదిని సుప్రీంకోర్టు లేదా హైకోర్టు సెక్షన్16(2)కింద సీనియర్ న్యాయవాదిగా గుర్తించవచ్చు.',
'Under section16(2)of the AdvocatesAct, which institutions may designate a consenting advocate as senior advocate?',
'న్యాయవాదుల చట్టంలోని సెక్షన్16(2)ప్రకారం సమ్మతించే న్యాయవాదిని సీనియర్ న్యాయవాదిగా ఏ సంస్థలు గుర్తించవచ్చు?',
['Only a DistrictCollector','SupremeCourt or a HighCourt','Only the UnionLawMinister','Any GramPanchayat'],
['జిల్లా కలెక్టర్ మాత్రమే','సుప్రీంకోర్టు లేదా హైకోర్టు','కేంద్ర న్యాయశాఖ మంత్రి మాత్రమే','ఏ గ్రామ పంచాయతీ అయినా'],2,
'Section16(2)identifies the SupremeCourt and HighCourts and requires the advocate’s consent and the stated merit/distinction considerations. Senior designation is not the same as AoRregistration or a general licence to file/act without the Court’s professional rules.',
'సెక్షన్16(2) సుప్రీంకోర్టు, హైకోర్టులను గుర్తిస్తూ న్యాయవాది సమ్మతి, పేర్కొన్న ప్రతిభ/ప్రత్యేక గుర్తింపు ప్రమాణాలను కోరుతుంది. సీనియర్ గుర్తింపు ఏఓఆర్ నమోదుకు సమానం కాదు; కోర్టు వృత్తి నియమాలను పట్టించుకోకుండా దాఖలు/నిర్వహణకు సాధారణ అనుమతి కూడా కాదు.',
'2isthestatutorypair;1/3/4arenotdesignationcourts.',level='easy')

add('ordinary-bench-two',['GBK741-309-01'],'Ch26 paragraph24, numerical rule supplied by primary','partial',RULES,'OrderVIrule1; SCorder1March2021confirms current rule and single-judge exceptions',
'Subject to other provisions of the Rules, the ordinary SupremeCourt bench under OrderVIrule1consists of not less than two judges.',
'ఇతర నియమ నిబంధనలకు లోబడి, ఆర్డర్VIనియమం1కింద సాధారణ సుప్రీంకోర్టు ధర్మాసనంలో కనీసం ఇద్దరు న్యాయమూర్తులు ఉంటారు.',
'Subject to express exceptions and larger-bench requirements, what is the ordinary minimum under OrderVIrule1of the SupremeCourt Rules?',
'స్పష్టమైన మినహాయింపులు, పెద్ద ధర్మాసన అవసరాలకు లోబడి సుప్రీంకోర్టు నియమాల్లోని ఆర్డర్VIనియమం1సాధారణ కనీస బలం ఎంత?',
['Onejudge','Threejudges','Twojudges','Fivejudges'],['ఒక న్యాయమూర్తి','ముగ్గురు న్యాయమూర్తులు','ఇద్దరు న్యాయమూర్తులు','ఐదుగురు న్యాయమూర్తులు'],3,
'The ordinary rule says not less than two. Specific single-judge categories and larger-bench requirements remain exceptions or additional rules. This corrects a blanket at-least-three division-bench claim without suggesting that every SupremeCourt matter must always be heard by exactly two judges.',
'సాధారణ నియమం కనీసం ఇద్దరు అని చెబుతుంది. నిర్దిష్ట ఏకన్యాయమూర్తి వర్గాలు, పెద్ద ధర్మాసన అవసరాలు మినహాయింపులు లేదా అదనపు నియమాలుగా కొనసాగుతాయి. ప్రతి సుప్రీంకోర్టు విషయాన్నీ సరిగ్గా ఇద్దరే ఎల్లప్పుడూ విచారించాలనకుండా, విభాగ ధర్మాసనం కనీసం ముగ్గురు అనే సాధారణీకరణను ఇది సరిచేస్తుంది.',
'3isordinaryminimum2;1belongs toexpresssinglejudgeexceptions,2isnotordinaryminimum,4constitutionalbenchminimumisadifferentrule.',level='easy')

add('contempt-classification',['GBK741-295-10'],'Ch26 paragraph42','direct',CONT,'ContemptofCourtsAct1971section2(b),(c)',
'Wilful breach of an undertaking to Court is within civil contempt; publication prejudicing or interfering/tending to interfere with judicial proceedings is within criminal contempt.',
'కోర్టుకు ఇచ్చిన హామీని ఉద్దేశపూర్వకంగా ఉల్లంఘించడం సివిల్ ధిక్కారంలోకి వస్తుంది; న్యాయ విచారణకు భంగం కలిగించే లేదా కలిగించే ధోరణి గల ప్రచురణ క్రిమినల్ ధిక్కారంలోకి వస్తుంది.',
'Which best matches the statutory definitions? A.Wilful breach of an undertaking given to a court. B.Publication prejudicing or interfering with the due course of a judicial proceeding.',
'చట్ట నిర్వచనాలకు ఉత్తమంగా సరిపోయేది ఏది? A.కోర్టుకు ఇచ్చిన హామీని ఉద్దేశపూర్వకంగా ఉల్లంఘించడం. B.న్యాయ విచారణ సక్రమ క్రమానికి భంగం కలిగించే ప్రచురణ.',
['Acriminal;Bcivil','Bothautomaticallyimmune','Bothonlycivil','Acivil;Bcriminal'],['Aక్రిమినల్;Bసివిల్','రెండింటికీ స్వయంచాలక మినహాయింపు','రెండూ సివిల్ మాత్రమే','Aసివిల్;Bక్రిమినల్'],4,
'The first description tracks section2(b),the second section2(c). The question classifies the stated statutory descriptions; it does not claim that all possible conduct must fall into mutually exclusive factual boxes. Fair-comment and other statutory safeguards remain and must be considered in an actual case.',
'మొదటి వివరణ సెక్షన్2(b),రెండవది సెక్షన్2(c)కు సరిపోతాయి. ప్రశ్న పేర్కొన్న చట్ట వివరణలను వర్గీకరిస్తుంది; సాధ్యమైన ప్రతి చర్య వాస్తవంగా పరస్పరం వేరైన పెట్టెల్లోనే చేరాలని కాదు. న్యాయమైన వ్యాఖ్య తదితర చట్ట రక్షణలు కొనసాగుతాయి; వాస్తవ కేసులో వాటిని పరిశీలించాలి.',
'4matchesdefinitions;1reversesthem,2inventsblanketimmunity,3deniesthecriminalcategory.',fmt='matching')

add('fair-criticism-final-case',['GBK741-295-11'],'Ch26 paragraph42','direct','https://www.indiacode.nic.in/bitstream/123456789/1514/1/197170.pdf','ContemptofCourtsAct1971section5',
'Section5protects fair comment on the merits of a case heard and finally decided from contempt liability under its stated rule.',
'విచారణ పూర్తయి తుది నిర్ణయం వెలువడిన కేసు అంశసారంపై న్యాయమైన వ్యాఖ్యకు సెక్షన్5తన పేర్కొన్న నియమం మేరకు ధిక్కార బాధ్యత నుంచి రక్షణ ఇస్తుంది.',
'Which conduct falls within section5’s express fair-criticism safeguard?',
'సెక్షన్5లోని స్పష్టమైన న్యాయమైన విమర్శ రక్షణలోకి ఏ చర్య వస్తుంది?',
['Fair comment on the merits of a case heard and finally decided','Wilful disobedience of a court order','Threatening a witness to obstruct a pending trial','Every publication about any pending case irrespective of its effects'],
['విచారణ పూర్తయి తుది నిర్ణయం వెలువడిన కేసు అంశసారంపై న్యాయమైన వ్యాఖ్య','కోర్టు ఉత్తర్వును ఉద్దేశపూర్వకంగా ఉల్లంఘించడం','పెండింగ్ విచారణను అడ్డుకోవడానికి సాక్షిని బెదిరించడం','ప్రభావాలతో సంబంధం లేకుండా ఏ పెండింగ్ కేసుపైనా ప్రతి ప్రచురణ'],1,
'The statutory safeguard protects fair comment on a finally decided case’s merits. It is not a licence for disobedience,witness intimidation or every prejudicial pending-case publication. The question is confined to section5and does not purport to override other applicable confidentiality or publication restrictions.',
'చట్ట రక్షణ తుది నిర్ణయం వెలువడిన కేసు అంశసారంపై న్యాయమైన వ్యాఖ్యకు వర్తిస్తుంది. ఇది ఆదేశ ఉల్లంఘనకు, సాక్షి బెదిరింపుకు లేదా ప్రతి పెండింగ్ కేసు ప్రభావిత ప్రచురణకు అనుమతి కాదు. ప్రశ్న సెక్షన్5కే పరిమితం; ఇతర గోప్యత లేదా ప్రచురణ పరిమితులను అధిగమిస్తుందని చెప్పదు.',
'1istheexpresssafeconduct;2/3areobstructiveacts,4removesallstatutoryconditions.')

add('financial-emergency-direction',['GBK741-292-03'],'Ch26 paragraph14; independence safeguard3','partial',C,'Article360(4)(b)',
'During a FinancialEmergency the President may direct reduction of salaries and allowances of Union-service classes including SupremeCourt and HighCourt judges under Article360(4)(b).',
'ఆర్థిక అత్యవసర పరిస్థితిలో ప్రకరణ360(4)(b)కింద సుప్రీంకోర్టు, హైకోర్టు న్యాయమూర్తులు సహా కేంద్ర వ్యవహారాలతో సంబంధిత వర్గాల జీతాలు, భత్యాలు తగ్గించాలని రాష్ట్రపతి ఆదేశించవచ్చు.',
'Which proclamation supplies the express Article360(4)(b)power concerning reduction of SupremeCourt/HighCourt judges’ salaries and allowances?',
'సుప్రీంకోర్టు/హైకోర్టు న్యాయమూర్తుల జీతాలు, భత్యాల తగ్గింపుపై ప్రకరణ360(4)(b)లోని స్పష్టమైన అధికారానికి ఏ ప్రకటన ఆధారం?',
['President’sRuleinoneState','FinancialEmergency','Anyordinarycabinetresolution','EveryNationalEmergencyautomatically'],
['ఒక రాష్ట్రంలో రాష్ట్రపతి పాలన','ఆర్థిక అత్యవసర పరిస్థితి','ఏ సాధారణ మంత్రివర్గ తీర్మానమైనా','ప్రతి జాతీయ అత్యవసర పరిస్థితి స్వయంచాలకంగా'],2,
'Article360(4)(b)explicitly includes SupremeCourt and HighCourt judges. The item tests that financial-emergency power. It deliberately does not restate an overbroad salary,allowance,leave,pension non-variation proposition as if each protection had identical constitutional wording or no other qualification.',
'ప్రకరణ360(4)(b) సుప్రీంకోర్టు, హైకోర్టు న్యాయమూర్తులను స్పష్టంగా చేర్చుతుంది. ప్రశ్న ఆ ఆర్థిక అత్యవసర అధికారాన్ని పరీక్షిస్తుంది. జీతం, భత్యం, సెలవు, పెన్షన్ మార్పులన్నింటికీ ఒకే రాజ్యాంగ భాష లేదా ఇతర పరిమితులేమీ లేవన్నట్లు అతివ్యాప్తి వాక్యాన్ని పునరావృతం చేయదు.',
'2isArticle360;1is356,4confuses352,3lacks the constitutional trigger.',level='easy')

add('court-record-evidence',['GBK741-295-09'],'Ch26 paragraph41','direct',C,'Article129court-of-record status; evidentiary meaning supported directly by the supplied reader',
'A court of record preserves its judicial proceedings for perpetual memory and their evidentiary authority; the status is not merely a computerised-case-list label.',
'కోర్ట్ ఆఫ్ రికార్డ్ తన న్యాయ విచారణల శాశ్వత జ్ఞాపకం, సాక్ష్యాధికారానికి రికార్డులను నిల్వ చేస్తుంది; అది కేవలం కంప్యూటర్ కేసుల జాబితా పేరు కాదు.',
'Apart from the associated contempt power, what does the Court-of-Record description principally signify here?',
'సంబంధిత ధిక్కార అధికారంతో పాటు ఇక్కడ కోర్ట్ ఆఫ్ రికార్డ్ వర్ణన ప్రధానంగా ఏ భావాన్ని సూచిస్తుంది?',
['Onlythecourt’sdailybudgetregister','Onlyawebsitecauselist','Preservationandauthoritativeevidentiarycharacterofjudicialrecords','Automaticabolitionofappeals'],
['కోర్టు రోజువారీ బడ్జెట్ రిజిస్టర్ మాత్రమే','వెబ్‌సైట్ కేసుల జాబితా మాత్రమే','న్యాయ రికార్డుల పరిరక్షణ, ప్రామాణిక సాక్ష్య స్వభావం','అప్పీళ్ల స్వయంచాలక రద్దు'],3,
'The supplied reader distinguishes the enduring evidentiary record from the separate contempt power. Article129provides the constitutional status but does not itself spell out every common-law evidentiary consequence. This item assesses the record function; it does not say that no judgment can ever be reviewed or overruled.',
'సిద్ధం చేసిన పాఠ్యం శాశ్వత సాక్ష్య రికార్డును వేరు ధిక్కార అధికారం నుంచి వేరు చేస్తుంది. ప్రకరణ129 రాజ్యాంగ హోదాను ఇస్తుంది; ప్రతి సాధారణ న్యాయ సాక్ష్య ఫలితాన్ని తన పాఠ్యంలోనే వివరించదు. ప్రశ్న రికార్డు విధిని పరీక్షిస్తుంది; ఏ తీర్పునూ ఎప్పటికీ సమీక్షించలేమని లేదా అధిగమించలేమని చెప్పదు.',
'3istherecordfunction;1/2reduceroletoadministrative/digitalrecordkeeping;4confuses record status with finality.',level='easy')

add('gram-natural-justice',['GBK741-307-01'],'Ch38 paragraph22; table7; absentCh26','partial',GRAM,'GramNyayalayasAct2008section30',
'Section30guides GramNyayalayas by natural justice, subject to HighCourt rules; the positive guiding principle can be taught without claiming an unverified universal exemption from the replacement evidence statute.',
'సెక్షన్30 హైకోర్టు నియమాలకు లోబడి గ్రామ న్యాయాలయాలకు సహజ న్యాయాన్ని మార్గదర్శకంగా నిర్దేశిస్తుంది; కొత్త సాక్ష్య చట్టం నుంచి సర్వసాధారణ మినహాయింపు ఉందని ధ్రువీకరించని వాదన లేకుండానే ఈ సూత్రాన్ని బోధించవచ్చు.',
'Which positive guiding principle does section30of the GramNyayalayasAct specify, subject to HighCourt rules?',
'హైకోర్టు నియమాలకు లోబడి గ్రామ న్యాయాలయాల చట్టం సెక్షన్30ఏ సానుకూల మార్గదర్శక సూత్రాన్ని నిర్దేశిస్తుంది?',
['Executivepleasurealone','Partydiscipline','Policeinstructionsalone','Principlesofnaturaljustice'],
['కార్యనిర్వాహక ఇష్టమే','పార్టీ క్రమశిక్షణ','పోలీసు సూచనలే','సహజ న్యాయ సూత్రాలు'],4,
'Natural justice is the express guiding principle. The old provision refers to the IndianEvidenceAct1872; current replacement/saving questions require separate cross-statute qualification. This narrow item does not claim that all modern proceedings are automatically outside every evidence-law requirement.',
'సహజ న్యాయం స్పష్టమైన మార్గదర్శక సూత్రం. పాత నిబంధన భారత సాక్ష్య చట్టం1872ను ప్రస్తావిస్తుంది; ప్రస్తుత భర్తీ/రక్షణ అంశాలకు వేరు చట్టాల అనుసంధాన పరిశీలన అవసరం. ఈ పరిమిత ప్రశ్న ప్రతి ఆధునిక విచారణకూ అన్ని సాక్ష్య చట్ట అవసరాల నుంచి స్వయంచాలక మినహాయింపు ఉందని చెప్పదు.',
'4isthestatutoryprinciple;1/2/3substitute nonjudicial or partisan directions.',level='easy')

add('gram-appeal-periods',['GBK741-307-02'],'Ch38 paragraph22; table7, filing period primary supplement','partial',GRAM,'Sections33(4),(5),34(3),(4)',
'Permitted GramNyayalaya appeals have an ordinary thirty-day filing period, with sufficient-cause late-admission provision; the statute prescribes disposal within six months of filing.',
'అనుమతించిన గ్రామ న్యాయాలయ అప్పీళ్లకు సాధారణ దాఖలు కాలం ముప్పై రోజులు; తగిన కారణంతో ఆలస్యంగా స్వీకరించే ఏర్పాటు ఉంది. దాఖలు నుంచి ఆరు నెలల్లో పరిష్కారాన్ని చట్టం నిర్దేశిస్తుంది.',
'For an appeal permitted by the GramNyayalayasAct, which pair correctly distinguishes ordinary filing and statutory disposal periods?',
'గ్రామ న్యాయాలయాల చట్టం అనుమతించిన అప్పీల్‌కు సాధారణ దాఖలు, చట్ట నిర్దేశిత పరిష్కార కాలాలను ఏ జత సరిగ్గా వేరు చేస్తుంది?',
['30daysforfiling;disposalwithinsixmonthsoffiling','Sixmonthsforfiling;30daysfordisposal','Oneyeartoappeal;nofixeddisposalrule','Filinganddisposalbothalwayswithinsevendays'],
['దాఖలుకు30రోజులు; దాఖలు నుంచి ఆరు నెలల్లో పరిష్కారం','దాఖలుకు ఆరు నెలలు; పరిష్కారానికి30రోజులు','అప్పీల్‌కు ఒక సంవత్సరం; పరిష్కార నియమం లేదు','దాఖలు, పరిష్కారం రెండూ ఎల్లప్పుడూ ఏడు రోజుల్లో'],1,
'Criminal appeals use the Court ofSession route and civil appeals the DistrictCourt route, subject to exclusions already tested elsewhere. Both provisions distinguish thirty-day presentation from six-month disposal. Late presentation may be entertained for sufficient cause; the item does not guarantee every case is actually disposed within that period.',
'క్రిమినల్ అప్పీళ్లకు సెషన్స్ కోర్టు, సివిల్ అప్పీళ్లకు జిల్లా కోర్టు మార్గాలు వర్తిస్తాయి; ఇతరచోట పరీక్షించిన మినహాయింపులు ఉంటాయి. రెండు నిబంధనలూ ముప్పై రోజుల దాఖలును ఆరు నెలల పరిష్కారం నుంచి వేరు చేస్తాయి. తగిన కారణంతో ఆలస్య దాఖలును స్వీకరించవచ్చు; ప్రతి కేసూ వాస్తవంగా ఆ గడువులో పూర్తవుతుందని ప్రశ్న హామీ ఇవ్వదు.',
'1hascorrectdistinctperiods;2reversesthem;3/4inventtimelines.',fmt='matching')

add('family-gram-act-years',['GBK741-306-07','GBK741-308-07'],'Ch38 paragraphs16,20; tables6–7','direct',FAM,'Statutory short title; GramNyayalayasAct2008section1shorttitle',
'The statutory short titles are FamilyCourtsAct1984and GramNyayalayasAct2008; short-title year is distinct from commencement.',
'చట్టాల సంక్షిప్త పేర్లు కుటుంబ న్యాయస్థానాల చట్టం1984, గ్రామ న్యాయాలయాల చట్టం2008; సంక్షిప్త పేరులోని సంవత్సరం, అమలు ప్రారంభం వేర్వేరు.',
'Which pairing of statutory short-title years is correct?',
'చట్టాల సంక్షిప్త పేర్లలోని సంవత్సరాల సరైన జత ఏది?',
['FamilyCourts1987—GramNyayalayas2008','FamilyCourts1984—GramNyayalayas2008','FamilyCourts2008—GramNyayalayas1984','FamilyCourts1984—GramNyayalayas1987'],
['కుటుంబ న్యాయస్థానాలు1987—గ్రామ న్యాయాలయాలు2008','కుటుంబ న్యాయస్థానాలు1984—గ్రామ న్యాయాలయాలు2008','కుటుంబ న్యాయస్థానాలు2008—గ్రామ న్యాయాలయాలు1984','కుటుంబ న్యాయస్థానాలు1984—గ్రామ న్యాయాలయాలు1987'],2,
'The two short-title years are1984and2008. The GramNyayalayasAct was enacted as Act4of2009and commenced on2October2009; those facts do not change its short-title year. FamilyCourts commencement also must not be assumed identical in every jurisdiction merely from the1984title.',
'సంక్షిప్త పేర్లలోని రెండు సంవత్సరాలు1984,2008. గ్రామ న్యాయాలయాల చట్టం2009లోని4వ చట్టంగా రూపుదిద్దుకుని2009అక్టోబరు2న అమల్లోకి వచ్చింది; ఆ విషయాలు దాని సంక్షిప్త పేరులోని సంవత్సరాన్ని మార్చవు.1984అనే పేరు ఆధారంగా కుటుంబ న్యాయస్థానాల అమలు ప్రారంభం ప్రతి పరిధిలో ఒకటేనని కూడా ఊహించకూడదు.',
'2correctsbothyears;1/4substituteLSA1987;3reversescourtstatutes.',fmt='matching',level='easy')

add('family-jurisdiction-set',['GBK741-308-07'],'Ch38 paragraph18; table6','direct',FAM,'FamilyCourtsAct1984section7explanation',
'FamilyCourt jurisdiction includes the specified matrimonial-status, spousal-property and minor-custody/guardianship proceedings.',
'కుటుంబ న్యాయస్థానం అధికార పరిధిలో నిర్దిష్ట వైవాహిక స్థితి, భార్యాభర్తల ఆస్తి, మైనర్ సంరక్షణ/అభిరక్షణ విచారణలు ఉంటాయి.',
'Which set is within the FamilyCourtsAct’s specified family jurisdiction?',
'కుటుంబ న్యాయస్థానాల చట్టంలోని నిర్దిష్ట కుటుంబ అధికార పరిధిలో ఏ సమూహం చేరుతుంది?',
['Customsduty,forexpenaltyandcitizenship','Landceiling,taxevasionandpublicrecruitment','Matrimonialstatus,spousalpropertyandminor-custodyproceedings','Parliamentaryelection,industriallicenceandcriminalpardon'],
['కస్టమ్స్ సుంకం, విదేశీ మారక జరిమానా, పౌరసత్వం','భూ గరిష్ఠ పరిమితి, పన్ను ఎగవేత, ప్రజా ఉద్యోగ నియామకం','వైవాహిక స్థితి, భార్యాభర్తల ఆస్తి, మైనర్ అభిరక్షణ విచారణలు','పార్లమెంటు ఎన్నిక, పారిశ్రామిక అనుమతి, నేర క్షమాభిక్ష'],3,
'Section7enumerates family-related proceedings, including matrimonial status, specified property disputes between parties to a marriage, and guardianship/custody/access to a minor. The answer is not an exhaustive list: maintenance and other stated categories also appear. The unrelated public-law subjects are not converted into family jurisdiction.',
'సెక్షన్7 కుటుంబ సంబంధిత విచారణలను పేర్కొంటుంది; వైవాహిక స్థితి, వివాహ పక్షాల మధ్య నిర్దిష్ట ఆస్తి వివాదాలు, మైనర్ సంరక్షణ/అభిరక్షణ/కలుసుకునే హక్కు అందులో ఉన్నాయి. సమాధానం పూర్తి జాబితా కాదు; భరణం, ఇతర నిర్దిష్ట వర్గాలూ ఉంటాయి. సంబంధం లేని ప్రజా న్యాయ అంశాలు కుటుంబ అధికార పరిధిగా మారవు.',
'3isthestatutoryfamilyset;1/2/4mixunrelatedtax,executiveorelectionfunctions.',level='easy')

add('preconstitution-federal-exception',['GBK741-293-05'],'Ch26 paragraphs31,38','direct',C,'Article131proviso; Article143(2)',
'A dispute within the Article131proviso’s pre-Constitution instrument category is excluded from that original jurisdiction but may be referred by the President under Article143(2).',
'ప్రకరణ131మినహాయింపులోని రాజ్యాంగ పూర్వ ఒప్పంద తదితర పత్రాల వివాద వర్గం ఆ ప్రారంభ అధికార పరిధికి మినహాయింపు; అయితే రాష్ట్రపతి ప్రకరణ143(2)కింద సూచించవచ్చు.',
'A Union–State dispute falls within Article131’s proviso excluding the specified pre-Constitution instrument category. Which constitutional route may the President use to refer it for the SupremeCourt’s opinion?',
'ఒక కేంద్ర–రాష్ట్ర వివాదం ప్రకరణ131లోని నిర్దిష్ట రాజ్యాంగ పూర్వ పత్రాల మినహాయింపు వర్గంలో చేరింది. సుప్రీంకోర్టు అభిప్రాయానికి దానిని సూచించడానికి రాష్ట్రపతి ఏ రాజ్యాంగ మార్గాన్ని వినియోగించవచ్చు?',
['Article32asaprivatewritappeal','Article136asanordinaryappealasofright','Article124asajudicialappointment','Article143(2)reference'],
['వ్యక్తిగత రిట్ అప్పీల్‌గా ప్రకరణ32','హక్కుగా సాధారణ అప్పీల్‌గా ప్రకరణ136','న్యాయ నియామకంగా ప్రకరణ124','ప్రకరణ143(2)సూచన'],4,
'Article143(2)expressly links to the dispute category mentioned in the proviso to Article131. This item tests that jurisdictional bridge, not simply the may/shall contrast already tested in the bank. The exclusion must be tied to the proviso’s precise category, not every modern treaty or every Union–State dispute.',
'ప్రకరణ143(2),ప్రకరణ131మినహాయింపులో పేర్కొన్న వివాద వర్గాన్ని స్పష్టంగా అనుసంధానిస్తుంది. ఈ ప్రశ్న ఆ అధికార పరిధి అనుసంధానాన్ని పరీక్షిస్తుంది; బ్యాంకులో ఇప్పటికే పరీక్షించిన ఇవ్వవచ్చు/ఇవ్వాలి అనే భేదాన్ని మాత్రమే కాదు. మినహాయింపును నిర్దిష్ట వర్గానికే పరిమితం చేయాలి; ప్రతి ఆధునిక ఒప్పందం లేదా ప్రతి కేంద్ర–రాష్ట్ర వివాదానికి కాదు.',
'4isthespecifiedbridge;1/2wronglyconvertitintoordinaryrightsappeal;3isappointmentpower.',fmt='application')

add('state-psc-reference',['GBK741-297-11'],'Ch26 paragraph48','direct',C,'Article317(1), distinguish other grounds in317(3)',
'For the Article317(1)misbehaviour route concerning a StatePSCmember, the SupremeCourt inquiry follows a reference made by the President.',
'రాష్ట్ర పబ్లిక్ సర్వీస్ కమిషన్ సభ్యుని దుష్ప్రవర్తనపై ప్రకరణ317(1)మార్గంలో, రాష్ట్రపతి చేసిన సూచన తరువాత సుప్రీంకోర్టు విచారణ జరుగుతుంది.',
'Under the Article317(1)misbehaviour route for a StatePSCmember, who makes the reference for SupremeCourt inquiry?',
'రాష్ట్ర పబ్లిక్ సర్వీస్ కమిషన్ సభ్యునిపై ప్రకరణ317(1)దుష్ప్రవర్తన మార్గంలో సుప్రీంకోర్టు విచారణకు ఎవరు సూచన చేస్తారు?',
['President','Governoractingalone','ChiefMinister','StateAssemblySpeaker'],['రాష్ట్రపతి','గవర్నర్ ఒక్కరే','ముఖ్యమంత్రి','రాష్ట్ర శాసనసభ స్పీకర్'],1,
'The President makes the reference even for a StateCommission. The State context does not transfer the constitutional removal-reference role to the Governor. The item is expressly confined to misbehaviour under317(1); it does not assert that every alternative ground under317(3)requires the same inquiry.',
'రాష్ట్ర కమిషన్ విషయంలోనూ రాష్ట్రపతి సూచన చేస్తారు. రాష్ట్ర సందర్భం ఉందనే కారణంతో రాజ్యాంగ తొలగింపు-సూచన పాత్ర గవర్నర్‌కు బదిలీ కాదు. ప్రశ్న స్పష్టంగా317(1)దుష్ప్రవర్తనకే పరిమితం;317(3)లోని ప్రతి ఇతర ఆధారానికీ అదే విచారణ అవసరమని చెప్పదు.',
'1isexpressPresidentreference;2confusesStateappointment/suspensionroles,3/4arenotreferenceauthorities.',level='easy')

add('first-two-chief-justices',['GBK741-310-04','GBK741-310-05'],'Ch26 paragraph2partial; historical identity supplement','partial','https://www.sci.gov.in/former-chief-justices/','First two listed CJIs; Sastri profile explicitly gives CJI7Nov1951–3Jan1954',
'Harilal J.Kania was the first CJI; M.Patanjali Sastri succeeded him as the second.',
'హరిలాల్ జె.కానియా మొదటి ప్రధాన న్యాయమూర్తి; ఆయన తరువాత ఎం.పతంజలి శాస్త్రి రెండవ ప్రధాన న్యాయమూర్తిగా వచ్చారు.',
'Which pair correctly names the first and second ChiefJustices of India?',
'భారత మొదటి, రెండవ ప్రధాన న్యాయమూర్తులను వరుసగా సరిగ్గా తెలిపే జత ఏది?',
['M.PatanjaliSastri—HarilalKania','HarilalKania—M.PatanjaliSastri','S.R.Das—M.H.Kania','MehrChandMahajan—Y.V.Chandrachud'],
['ఎం.పతంజలి శాస్త్రి—హరిలాల్ కానియా','హరిలాల్ కానియా—ఎం.పతంజలి శాస్త్రి','ఎస్.ఆర్.దాస్—ఎం.హెచ్.కానియా','మెహర్ చంద్ మహాజన్—వై.వి.చంద్రచూడ్'],2,
'The official history identifies Kania as the first CJI and the former-CJI list/profile establishes Sastri as his successor. Website list dates can describe total SupremeCourt service, not only CJIservice; those must not be confused when making tenure questions. This item asks identities/order, not tenure arithmetic.',
'అధికారిక చరిత్ర కానియాను మొదటి ప్రధాన న్యాయమూర్తిగా గుర్తిస్తుంది; పూర్వ ప్రధాన న్యాయమూర్తుల జాబితా/ప్రొఫైల్ శాస్త్రిని ఆయన వారసుడిగా నిర్ధారిస్తాయి. వెబ్‌సైట్ జాబితా తేదీలు ప్రధాన న్యాయమూర్తి కాలాన్నే కాక మొత్తం సుప్రీంకోర్టు సేవను సూచించవచ్చు; పదవీకాల ప్రశ్నల్లో వాటిని కలపకూడదు. ఇక్కడ గుర్తింపులు/క్రమమే ప్రశ్న; కాల గణన కాదు.',
'2correct;1reversesorder;3/4name later officeholders.',fmt='matching',level='easy')

add('fathima-supreme-service',['GBK741-310-07'],'Absent from Ch26 historical update','absent','https://www.sci.gov.in/former-justices/','JusticeM.FathimaBeevi row:6October1989–29April1992',
'Justice M.Fathima Beevi served on the SupremeCourt from1989to1992;1997–2001must not be used as her SupremeCourt tenure.',
'జస్టిస్ ఎం.ఫాతిమా బీవీ సుప్రీంకోర్టులో1989నుంచి1992వరకు సేవ చేశారు;1997–2001ను ఆమె సుప్రీంకోర్టు పదవీకాలంగా ఉపయోగించకూడదు.',
'Which period corresponds to Justice M.Fathima Beevi’s SupremeCourt service in the official former-justices list?',
'అధికారిక పూర్వ న్యాయమూర్తుల జాబితా ప్రకారం జస్టిస్ ఎం.ఫాతిమా బీవీ సుప్రీంకోర్టు సేవకు ఏ కాలం సరిపోతుంది?',
['1950–1951','1997–2001','1989–1992','2007–2010'],['1950–1951','1997–2001','1989–1992','2007–2010'],3,
'The official Court list gives6October1989to29April1992. The1997–2001period is not her SupremeCourt service and must not be silently inherited from a defective source association. The stem supplies her name; this response tests the service-period correction, not independent recall of who was first woman judge.',
'అధికారిక కోర్టు జాబితా1989అక్టోబరు6నుంచి1992ఏప్రిల్29వరకు చూపిస్తుంది.1997–2001ఆమె సుప్రీంకోర్టు సేవ కాదు; లోపభూయిష్ట మూల అనుబంధం నుంచి దానిని అలాగే స్వీకరించకూడదు. ప్రశ్న ఆమె పేరును ఇస్తుంది; సమాధానం సేవా కాల సవరణను పరీక్షిస్తుంది, మొదటి మహిళా న్యాయమూర్తి ఎవరో ప్రత్యేకంగా గుర్తించడం కాదు.',
'3isofficialSCperiod;2isnotSCservice;1/4areotherjudicial-historyperiods.',level='easy')

add('legislative-irregularity-illegality',['GBK741-299-10','GBK741-299-11','GBK741-300-01'],'Ch26comparative section onlypartial; primary supplies correct rule','partial','https://api.sci.gov.in/supremecourt/2012/36970/36970_2012_Judgement_09-May-2018.pdf','Official SCjudgment,discussion of RajaRamPal and Articles122/212',
'The procedural-irregularity bar is not a blanket exclusion of review for substantive illegality or constitutional violation in legislative proceedings.',
'శాసన ప్రక్రియలో కేవలం విధాన లోపంపై ఉన్న ఆంక్ష, మూల చట్టవిరుద్ధత లేదా రాజ్యాంగ ఉల్లంఘనపై సమీక్షను సంపూర్ణంగా నిషేధించదు.',
'Which distinction correctly qualifies the Article122/212bar on judicial inquiry into legislative proceedings?',
'శాసన విచారణలపై న్యాయ పరిశీలనకు ప్రకరణలు122/212విధించే ఆంక్షను ఏ భేదం సరిగ్గా పరిమితం చేస్తుంది?',
['Alllegislativeactsareimmuneevenifconstitutionallyillegal','Courtsmayannuleveryproceedingforanyminorproceduraldeparture','LegislativeprivilegeautomaticallyoverridestheentireConstitution','Mereproceduralirregularityisdifferentfromsubstantiveillegalityorconstitutionalviolation'],
['రాజ్యాంగపరంగా చట్టవిరుద్ధమైనా అన్ని శాసన చర్యలకు మినహాయింపు','ఏ చిన్న ప్రక్రియా వ్యత్యాసానికైనా కోర్టులు ప్రతి విచారణనూ రద్దు చేయవచ్చు','శాసన ప్రత్యేక హక్కు స్వయంచాలకంగా మొత్తం రాజ్యాంగాన్ని అధిగమిస్తుంది','కేవలం ప్రక్రియా లోపం మూల చట్టవిరుద్ధత లేదా రాజ్యాంగ ఉల్లంఘనకు భిన్నం'],4,
'The SupremeCourt’s RajaRamPal discussion preserves limited judicial review despite institutional comity. Mere procedural irregularity is protected by the stated constitutional bar, while illegality/constitutional transgression is not converted into automatic immunity. The answer does not invite courts to supervise every internal procedural choice.',
'రాజా రామ్ పాల్‌పై సుప్రీంకోర్టు వివరణ సంస్థాగత గౌరవాన్ని ఉంచుతూ పరిమిత న్యాయ సమీక్షను కొనసాగిస్తుంది. కేవలం ప్రక్రియా లోపానికి పేర్కొన్న రాజ్యాంగ ఆంక్ష వర్తిస్తుంది; చట్టవిరుద్ధత/రాజ్యాంగ అతిక్రమణ స్వయంచాలక మినహాయింపుగా మారదు. ప్రతి అంతర్గత ప్రక్రియా ఎంపికను పర్యవేక్షించాలని సమాధానం కోర్టులను కోరదు.',
'4statescontrollingdistinction;1/3claimunlimitedimmunity,2erases the procedural-irregularity limitation.',level='hard')

# Only the proposal file is produced. Existing bank bytes remain untouched.
import re
def clean(s):
 for a,b in [('SupremeCourt','Supreme Court'),('HighCourt','High Court'),('LokSabha','Lok Sabha'),('GramNyayalaya','Gram Nyayalaya'),('FamilyCourt','Family Court'),('ChiefJustice','Chief Justice'),('StatePSC','State PSC'),('FinancialEmergency','Financial Emergency'),('FirstCase','First Case'),('SecondCase','Second Case'),('ThirdCase','Third Case'),('Twenty','Twenty'),('CivilCourt','Civil Court')]:s=s.replace(a,b)
 s=re.sub(r'(?<=[A-Za-z])(?=\d)|(?<=\d)(?=[A-Za-z])',' ',s)
 s=re.sub(r'\b(Article|section|Section)\s*(\d+)\s*([A-Z])(?=[a-z]|\b)',lambda m:m[1]+' '+m[2]+m[3]+' ',s)
 s=re.sub(r'([?:.])(?=\d)',r'\1 ',s)
 s=re.sub(r'(?<=\d)\.(?=[A-Za-z])','. ',s)
 return re.sub(r' {2,}',' ',s)
questions=[];facts=[];ex={};reviews=[]
for r in rows:
 fid='POL-741-SF-'+r['slug'];qid='POL-741-SUPP-'+r['slug']
 facts.append({'id':fid,'fact_en':clean(r['fe']),'fact_te':r['ft'],'source_hold_ids':r['held'],'prepared_match':{'classification':r['match'],'locator':r['reader']},'primary':{'url':r['url'],'locator':r['loc']},'status':'staged_for_independent_review','primary_locator_gate_open':not r['ready'],'source_exactness_certified':False})
 questions.append({'id':qid,'kind':'original-source-supported-supplement-proposal','source_type':'original-authored-not-PYQ','fact_ids':[fid],'tested_fact_ids':[fid],'source_page':None,'format':r['fmt'],'difficulty':r['level'],'question_en':clean(r['qe']),'question_te':r['qt'],'options_en':[clean(x) for x in r['oe']],'options_te':r['ot'],'answer':r['key'],'explanation_id':qid,'status':'proposal_not_in_app_bank','independent_review_ready':r['ready'],'coverage_limit':'Only the selected response target; supplied dates/conditions and explanation context are not independently credited.'})
 ex[qid]={'en':clean(r['ee']),'te':r['et'],'fact_ids':[fid],'references':[{'source':'Supplied prepared reader','locator':r['reader']},{'url':r['url'],'locator':r['loc']}]}
 reviews.append({'id':qid,'manual_solution':r['key'],'all_option_review':clean(r['review']),'bilingual_review':'Manually compared the two stems,4choices and separate rationales; constitutional actors,conditions and temporal scope preserved.','source_hold_ids':r['held'],'primary_locator_gate_open':not r['ready'],'result':'ready_for_independent_review' if r['ready'] else 'reader_supported_primary_locator_still_open','source_exactness_certified':False})
payload={'chapter':'7.4.1','status':'staged_only_no_app_bank_mutation','question_candidates':questions,'fact_candidates':facts,'explanations':ex,'manual_reviews':reviews,'candidates':len(questions),'independent_review_ready':sum(r['ready'] for r in rows),'primary_locator_holds':sum(not r['ready'] for r in rows),'existing_corrected_bank_untouched':True,'old_authoring_scripts_not_run':True,'source_access':'Held register,freely readable prepared Ch26/38and official primary material only. No GBKPDF/Notes/capture/image re-reading.','dedup_scope':'Read-only all current g2normal-bank stems and all4options; canonical resolutions are separately recorded. Related article identifiers or supplied context are not assumed to assess the new response target.','full_chapter_coverage':False,'source_exactness_certified':False,'unit_complete':False}
(P/'held-expansion-v2-proposal.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Staged',len(questions),'ready',payload['independent_review_ready'],'primary-locator holds',payload['primary_locator_holds'])
