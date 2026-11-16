"""Manually authored content; mechanical JSON merge only. No source access."""
import json
import re
from pathlib import Path
P=Path(__file__).parent
CON='https://www.legislative.gov.in/static/uploads/2025/07/359f70a69695affb9d72f8393102bd2e.pdf'
HIST='https://www.sci.gov.in/about-department/history/'
INQ='https://www.indiacode.nic.in/bitstream/123456789/1539/2/A1968-51.pdf'
CUR='https://api.sci.gov.in/supremecourt/2022/36401/36401_2022_5_1501_50787_Judgement_26-Feb-2024.pdf'
rows=[]
def add(slug,page,lax,article,fen,fte,qe,qt,oe,ot,key,ee,et,why,fmt='single-best-answer',primary=CON):
    rows.append(dict(slug=slug,page=page,lax=lax,article=article,fen=fen,fte=fte,qe=qe,qt=qt,oe=oe,ot=ot,key=key,ee=ee,et=et,why=why,fmt=fmt,primary=primary))

add('inauguration',286,'paragraph 2','SCI History: inauguration',
'The Supreme Court was ceremonially inaugurated on 28 January 1950; its constitutional coming into existence on 26 January is a distinct event.',
'సుప్రీంకోర్టు ప్రారంభోత్సవం 1950 జనవరి 28న జరిగింది; రాజ్యాంగం అమల్లోకి వచ్చిన జనవరి 26న దాని ఆవిర్భావం వేరే ఘట్టం.',
'On which date was the Supreme Court of India ceremonially inaugurated?',
'భారత సుప్రీంకోర్టు ప్రారంభోత్సవం ఏ తేదీన జరిగింది?',
['26 January 1950','28 January 1950','15 August 1947','26 November 1949'],
['1950 జనవరి 26','1950 జనవరి 28','1947 ఆగస్టు 15','1949 నవంబరు 26'],2,
'The official Court history distinguishes existence from inauguration. The Constitution commenced on 26 January 1950, while the inaugural sitting took place on 28 January. Independence Day and the adoption of the Constitution are different milestones.',
'అధికారిక కోర్టు చరిత్ర ఆవిర్భావాన్ని ప్రారంభోత్సవం నుంచి వేరు చేస్తుంది. రాజ్యాంగం 1950 జనవరి 26న అమల్లోకి వచ్చింది; ప్రారంభ సమావేశం జనవరి 28న జరిగింది. స్వాతంత్ర్య దినం, రాజ్యాంగ ఆమోదం వేర్వేరు ఘట్టాలు.',
'Only option 2 answers inauguration; option 1 confuses constitutional commencement, 3 independence and 4 adoption.',primary=HIST)

add('constitutional-location',286,'paragraph 2','Part V, Chapter IV, Articles 124–147',
'The Union judiciary is dealt with in Part V, Chapter IV, Articles 124–147.',
'కేంద్ర న్యాయవ్యవస్థను ఐదవ భాగంలోని నాలుగవ అధ్యాయం, ప్రకరణలు 124–147 వివరిస్తాయి.',
'Which location in the Constitution deals with the Union judiciary?',
'రాజ్యాంగంలో కేంద్ర న్యాయవ్యవస్థకు సంబంధించిన భాగం ఏది?',
['Part VI, Articles 214–231','Part XIV-A, Articles 323A–323B','Part V, Articles 124–147','Part III, Articles 12–35'],
['ఆరవ భాగం, ప్రకరణలు 214–231','పద్నాలుగవ భాగం-A, ప్రకరణలు 323A–323B','ఐదవ భాగం, ప్రకరణలు 124–147','మూడవ భాగం, ప్రకరణలు 12–35'],3,
'Part V Chapter IV contains the Union judiciary provisions. Part VI Chapter V concerns High Courts; Part XIV-A concerns tribunals. Part III contains fundamental rights, including Article 32, but does not constitute the whole Union judiciary chapter.',
'ఐదవ భాగంలోని నాలుగవ అధ్యాయంలో కేంద్ర న్యాయవ్యవస్థ నిబంధనలు ఉన్నాయి. ఆరవ భాగంలోని ఐదవ అధ్యాయం హైకోర్టులకు, పద్నాలుగవ భాగం-A ట్రిబ్యునళ్లకు సంబంధించినవి. మూడవ భాగంలో ప్రకరణ 32 సహా ప్రాథమిక హక్కులు ఉంటాయి; అది కేంద్ర న్యాయవ్యవస్థ అధ్యాయం మొత్తానికి సమానం కాదు.',
'Option 3 alone matches the exact chapter range; the other ranges describe different constitutional subjects.')

add('appointment-authority',287,'paragraph 5','Article 124(2)',
'Supreme Court judges are appointed by the President by warrant under the President’s hand and seal, subject to the constitutional provision as judicially interpreted.',
'రాజ్యాంగ నిబంధనపై న్యాయస్థానాల వ్యాఖ్యానానికి లోబడి, రాష్ట్రపతి తన సంతకం, ముద్రతో కూడిన అధికారపత్రం ద్వారా సుప్రీంకోర్టు న్యాయమూర్తులను నియమిస్తారు.',
'Who formally appoints a judge of the Supreme Court by warrant under hand and seal?',
'తన సంతకం, ముద్రతో కూడిన అధికారపత్రం ద్వారా సుప్రీంకోర్టు న్యాయమూర్తిని అధికారికంగా ఎవరు నియమిస్తారు?',
['President of India','Chief Justice of India acting alone','Speaker of the Lok Sabha','Union Law Minister acting alone'],
['భారత రాష్ట్రపతి','ఒంటరిగా భారత ప్రధాన న్యాయమూర్తి','లోక్‌సభ స్పీకర్','ఒంటరిగా కేంద్ర న్యాయశాఖ మంత్రి'],1,
'Article 124(2) places the formal appointment with the President. The collegium concerns recommendations and consultation as developed in the Judges Cases; it does not replace the President as appointing authority. Neither the Speaker nor the Law Minister alone appoints a judge.',
'ప్రకరణ 124(2) ప్రకారం అధికారిక నియామకం రాష్ట్రపతి చేస్తారు. న్యాయమూర్తుల కేసుల్లో అభివృద్ధి చెందిన కొలీజియం విధానం సిఫారసులు, సంప్రదింపులకు సంబంధించినది; అది నియామక అధికారిగా రాష్ట్రపతి స్థానాన్ని భర్తీ చేయదు. స్పీకర్ గానీ న్యాయశాఖ మంత్రి ఒంటరిగా గానీ న్యాయమూర్తిని నియమించరు.',
'Option 1 is the constitutional appointing authority; recommendation and processing are not formal appointment.')

add('acting-cji',287,'paragraph 20','Article 126',
'When the CJI office is vacant or its duties cannot be performed owing to absence or otherwise, the President may appoint another Supreme Court judge to perform those duties.',
'ప్రధాన న్యాయమూర్తి పదవి ఖాళీగా ఉన్నప్పుడు లేదా గైర్హాజరు తదితర కారణాలతో విధులు నిర్వహించలేనప్పుడు, ఆ విధులు నిర్వహించడానికి మరో సుప్రీంకోర్టు న్యాయమూర్తిని రాష్ట్రపతి నియమించవచ్చు.',
'The CJI is temporarily unable to perform the duties of office. Under Article 126, which arrangement is constitutionally available?',
'ప్రధాన న్యాయమూర్తి తాత్కాలికంగా పదవీ విధులు నిర్వహించలేకపోతున్నారు. ప్రకరణ 126 ప్రకారం ఏ ఏర్పాటు చేయవచ్చు?',
['The Law Minister automatically acts as CJI','The senior-most High Court judge automatically assumes the office','The Lok Sabha elects an acting CJI','The President appoints another Supreme Court judge to perform the duties'],
['న్యాయశాఖ మంత్రి స్వయంచాలకంగా ప్రధాన న్యాయమూర్తిగా వ్యవహరిస్తారు','అత్యంత సీనియర్ హైకోర్టు న్యాయమూర్తి స్వయంచాలకంగా బాధ్యతలు చేపడతారు','లోక్‌సభ తాత్కాలిక ప్రధాన న్యాయమూర్తిని ఎన్నుకుంటుంది','ఆ విధులు నిర్వహించడానికి రాష్ట్రపతి మరో సుప్రీంకోర్టు న్యాయమూర్తిని నియమిస్తారు'],4,
'Article 126 deals with an acting CJI, including a vacancy and temporary inability. It authorises a presidential appointment of another Supreme Court judge. This differs from Article 127 ad hoc attendance to meet a lack of quorum and from Article 128 attendance by a retired judge.',
'ప్రకరణ 126 ఖాళీ లేదా తాత్కాలిక అసమర్థత సందర్భంలో తాత్కాలిక ప్రధాన న్యాయమూర్తి ఏర్పాటును వివరిస్తుంది. మరో సుప్రీంకోర్టు న్యాయమూర్తిని రాష్ట్రపతి నియమించవచ్చు. ఇది కోరం లేనప్పుడు ప్రకరణ 127 కింద తాత్కాలిక న్యాయమూర్తి హాజరు, ప్రకరణ 128 కింద పదవీ విరమణ చేసిన న్యాయమూర్తి హాజరు కంటే భిన్నమైనది.',
'Only option 4 satisfies both appointing authority and eligible office; none of the automatic or electoral alternatives is in Article126.',fmt='application')

add('adhoc-conditions',288,'paragraph 21','Article 127',
'For lack of quorum, the CJI may request a qualified High Court judge to attend as an ad hoc Supreme Court judge after prior presidential consent and consultation with that High Court’s Chief Justice.',
'కోరం లేనప్పుడు, రాష్ట్రపతి ముందస్తు సమ్మతి, సంబంధిత హైకోర్టు ప్రధాన న్యాయమూర్తితో సంప్రదింపు తరువాత సుప్రీంకోర్టు న్యాయమూర్తి అర్హత గల హైకోర్టు న్యాయమూర్తిని తాత్కాలికంగా హాజరు కావాలని భారత ప్రధాన న్యాయమూర్తి కోరవచ్చు.',
'Consider Article 127 ad hoc judges: 1. Lack of quorum is the specified occasion. 2. Previous consent of the President is required. 3. The Chief Justice of the relevant High Court must be consulted. Which statements are correct?',
'ప్రకరణ 127 కింద తాత్కాలిక న్యాయమూర్తుల గురించి పరిశీలించండి: 1. కోరం లేకపోవడం నిర్దేశిత సందర్భం. 2. రాష్ట్రపతి ముందస్తు సమ్మతి అవసరం. 3. సంబంధిత హైకోర్టు ప్రధాన న్యాయమూర్తిని సంప్రదించాలి. సరైన వాక్యాలు ఏవి?',
['1 only','2 and 3 only','1, 2 and 3','1 and 2 only'],
['1 మాత్రమే','2, 3 మాత్రమే','1, 2, 3','1, 2 మాత్రమే'],3,
'All three are Article 127 safeguards. The requested High Court judge must also be duly qualified for Supreme Court appointment; the CJI’s written request specifies the period. The arrangement is not an unrestricted executive power to fill an ordinary permanent vacancy. The invalidated NJAC substitutions must not be read as operative law.',
'మూడూ ప్రకరణ 127 నిర్దేశించిన రక్షణలే. కోరిన హైకోర్టు న్యాయమూర్తికి సుప్రీంకోర్టు నియామక అర్హత కూడా ఉండాలి; హాజరు కాలాన్ని ప్రధాన న్యాయమూర్తి లిఖితపూర్వకంగా పేర్కొంటారు. ఇది సాధారణ శాశ్వత ఖాళీని భర్తీ చేసే అపరిమిత కార్యనిర్వాహక అధికారం కాదు. చెల్లనివిగా ప్రకటించిన ఎన్‌జేఏసీ మార్పులను అమల్లో ఉన్న చట్టంగా చదవకూడదు.',
'All three conditions are express; each distractor incorrectly omits a required condition.',fmt='statement-combination')

add('retired-attendance',288,'paragraph 22','Article 128',
'A retired judge’s attendance under Article 128 requires the CJI’s request, previous presidential consent and the person’s consent; while sitting the person has Supreme Court powers but is not otherwise deemed a Supreme Court judge.',
'ప్రకరణ 128 కింద పదవీ విరమణ చేసిన న్యాయమూర్తి హాజరుకు ప్రధాన న్యాయమూర్తి అభ్యర్థన, రాష్ట్రపతి ముందస్తు సమ్మతి, ఆ వ్యక్తి సమ్మతి అవసరం; విచారణలో కూర్చున్నప్పుడు సుప్రీంకోర్టు అధికారాలు ఉంటాయి గానీ ఇతర సందర్భాల్లో సుప్రీంకోర్టు న్యాయమూర్తిగా పరిగణించరు.',
'A retired Supreme Court judge is requested to sit under Article 128. Which statement is correct?',
'ప్రకరణ 128 కింద విచారణలో కూర్చోవాలని పదవీ విరమణ చేసిన సుప్రీంకోర్టు న్యాయమూర్తిని కోరారు. సరైన వాక్యం ఏది?',
['The person must serve even without consent','Previous presidential consent and the person’s consent are required','The person automatically receives a fresh permanent appointment','The person may sit only after election by both Houses'],
['ఆ వ్యక్తి సమ్మతి లేకున్నా సేవ చేయాలి','రాష్ట్రపతి ముందస్తు సమ్మతి, ఆ వ్యక్తి సమ్మతి అవసరం','ఆ వ్యక్తికి స్వయంచాలకంగా కొత్త శాశ్వత నియామకం లభిస్తుంది','రెండు సభలు ఎన్నుకున్న తరువాత మాత్రమే కూర్చోవచ్చు'],2,
'Article 128 is consensual attendance, not compulsory recall or a fresh permanent appointment. During the authorised sitting the judge enjoys the jurisdiction, powers and privileges of a Supreme Court judge, but is not otherwise deemed to be one. A retired High Court judge must also satisfy the specified Supreme Court qualification.',
'ప్రకరణ 128 సమ్మతితో హాజరు కావడానికి సంబంధించినది; బలవంతపు పునర్నియామకం లేదా కొత్త శాశ్వత నియామకం కాదు. అనుమతించిన విచారణలో సుప్రీంకోర్టు న్యాయమూర్తి అధికార పరిధి, అధికారాలు, ప్రత్యేక హక్కులు ఉంటాయి; ఇతర సందర్భాల్లో ఆ హోదా ఉన్నట్లుగా పరిగణించరు. పదవీ విరమణ చేసిన హైకోర్టు న్యాయమూర్తికి నిర్దేశిత సుప్రీంకోర్టు అర్హత కూడా అవసరం.',
'Option2 identifies both necessary consents; options1,3,4 substitute compulsion, permanent appointment or election.',fmt='application')

add('no-minimum-age',290,'paragraph 12','Article 124(3)',
'Article 124(3) prescribes no minimum age for appointment as a Supreme Court judge.',
'సుప్రీంకోర్టు న్యాయమూర్తి నియామకానికి ప్రకరణ 124(3) కనీస వయస్సును నిర్దేశించదు.',
'Apart from the citizenship and professional qualifications in Article 124(3), what minimum age does that provision prescribe for appointment as a Supreme Court judge?',
'ప్రకరణ 124(3)లో పౌరసత్వం, వృత్తిపరమైన అర్హతలతో పాటు సుప్రీంకోర్టు న్యాయమూర్తి నియామకానికి ఎంత కనీస వయస్సును నిర్దేశించారు?',
['No minimum age is prescribed','Thirty-five years','Forty years','Forty-five years'],
['కనీస వయస్సును నిర్దేశించలేదు','ముప్పై ఐదేళ్లు','నలభై ఏళ్లు','నలభై ఐదేళ్లు'],1,
'The constitutional qualification clause specifies citizenship and alternative legal experience or distinguished-jurist status, but no minimum age. The retirement age of 65 in Article 124(2) is a different rule; it must not be converted into an appointment minimum.',
'రాజ్యాంగ అర్హతల నిబంధన పౌరసత్వం, ప్రత్యామ్నాయ న్యాయ అనుభవం లేదా విశిష్ట న్యాయవేత్త హోదాను పేర్కొంటుంది; కనీస వయస్సును పేర్కొనదు. ప్రకరణ 124(2)లోని 65 ఏళ్ల పదవీ విరమణ వయస్సు వేరే నియమం; దానిని నియామక కనీస వయస్సుగా మార్చకూడదు.',
'Only option1 follows the absence of a constitutional minimum; the numeric distractors are unsupported.')

add('oath-authority',291,'paragraph 13','Article 124(6); Third Schedule',
'A Supreme Court judge takes the prescribed oath or affirmation before the President or a person appointed by the President, in the Third Schedule form.',
'సుప్రీంకోర్టు న్యాయమూర్తి మూడవ షెడ్యూల్‌లోని నమూనా ప్రకారం రాష్ట్రపతి లేదా రాష్ట్రపతి నియమించిన వ్యక్తి సమక్షంలో ప్రమాణం లేదా ధృవీకరణ చేస్తారు.',
'Which pair correctly states the authority and prescribed form for a Supreme Court judge’s oath?',
'సుప్రీంకోర్టు న్యాయమూర్తి ప్రమాణానికి సంబంధించిన అధికారి, నిర్దేశిత నమూనాను సరిగ్గా తెలిపే జత ఏది?',
['CJI alone — Second Schedule','Speaker or nominee — Fourth Schedule','Prime Minister — Third Schedule','President or presidential appointee — Third Schedule'],
['ప్రధాన న్యాయమూర్తి మాత్రమే — రెండవ షెడ్యూల్','స్పీకర్ లేదా ఆయన ప్రతినిధి — నాలుగవ షెడ్యూల్','ప్రధానమంత్రి — మూడవ షెడ్యూల్','రాష్ట్రపతి లేదా ఆయన నియమించిన వ్యక్తి — మూడవ షెడ్యూల్'],4,
'Article 124(6) requires an oath or affirmation before entering office, before the President or a person appointed by the President. The form is in the Third Schedule. The Second Schedule concerns emoluments and related provisions; the Fourth allocates Rajya Sabha seats.',
'ప్రకరణ 124(6) ప్రకారం పదవీ బాధ్యతలు చేపట్టే ముందు రాష్ట్రపతి లేదా ఆయన నియమించిన వ్యక్తి సమక్షంలో ప్రమాణం లేదా ధృవీకరణ చేయాలి. నమూనా మూడవ షెడ్యూల్‌లో ఉంటుంది. రెండవ షెడ్యూల్ వేతనాలు తదితర అంశాలకు, నాలుగవది రాజ్యసభ స్థానాల కేటాయింపుకు సంబంధించినది.',
'Option4 gets both halves right; option3 has correct schedule but wrong authority, and1/2 misstate both.',fmt='matching')

add('tenure-resignation',291,'paragraph 15','Article 124(2), proviso (a)',
'A Supreme Court judge holds office until age 65 and may resign by writing under hand addressed to the President.',
'సుప్రీంకోర్టు న్యాయమూర్తి 65 ఏళ్ల వయస్సు వరకు పదవిలో ఉంటారు; రాష్ట్రపతికి తన సంతకంతో లిఖితపూర్వక రాజీనామా సమర్పించవచ్చు.',
'Which combination correctly states a Supreme Court judge’s retirement age and the addressee of a resignation?',
'సుప్రీంకోర్టు న్యాయమూర్తి పదవీ విరమణ వయస్సు, రాజీనామా సమర్పించాల్సిన వ్యక్తిని సరిగ్గా తెలిపే జత ఏది?',
['62 years — Governor','65 years — President','65 years — CJI','62 years — President'],
['62 ఏళ్లు — గవర్నర్','65 ఏళ్లు — రాష్ట్రపతి','65 ఏళ్లు — ప్రధాన న్యాయమూర్తి','62 ఏళ్లు — రాష్ట్రపతి'],2,
'Article 124(2) sets the retirement age at 65 and permits resignation addressed to the President. The age 62 belongs to High Court tenure under Article 217, not Supreme Court tenure. The CJI is not the constitutional addressee of a Supreme Court judge’s resignation.',
'ప్రకరణ 124(2) పదవీ విరమణ వయస్సును 65 ఏళ్లుగా నిర్ణయించి, రాష్ట్రపతికి రాజీనామా సమర్పించడానికి అనుమతిస్తుంది. 62 ఏళ్ల పరిమితి ప్రకరణ 217 కింద హైకోర్టు పదవీకాలానికి సంబంధించినది; సుప్రీంకోర్టుకు కాదు. సుప్రీంకోర్టు న్యాయమూర్తి రాజీనామాను అందుకోవాల్సిన రాజ్యాంగ అధికారి ప్రధాన న్యాయమూర్తి కాదు.',
'Option2 alone has both correct elements;3 has correct age but wrong addressee,1/4 use HC age.',fmt='matching')

add('inquiry-notice',291,'paragraph 17','Judges (Inquiry) Act 1968, section 3(1)',
'A notice of removal motion under the Judges (Inquiry) Act requires at least 100 Lok Sabha members or 50 Rajya Sabha members; the presiding officer may admit or refuse it.',
'న్యాయమూర్తుల విచారణ చట్టం కింద తొలగింపు తీర్మానం నోటీసుకు కనీసం 100 మంది లోక్‌సభ సభ్యులు లేదా 50 మంది రాజ్యసభ సభ్యుల సంతకాలు అవసరం; సభాధ్యక్షుడు దానిని అనుమతించవచ్చు లేదా తిరస్కరించవచ్చు.',
'Under the Judges (Inquiry) Act, 1968, what is the minimum number of members needed to sign the notice of a judge-removal motion in the Lok Sabha and Rajya Sabha respectively?',
'న్యాయమూర్తుల విచారణ చట్టం, 1968 ప్రకారం న్యాయమూర్తి తొలగింపు తీర్మానం నోటీసుపై లోక్‌సభ, రాజ్యసభల్లో వరుసగా కనీసం ఎంతమంది సభ్యులు సంతకం చేయాలి?',
['50 and 25','100 and 100','100 and 50','50 and 100'],
['50, 25','100, 100','100, 50','50, 100'],3,
'Section 3 requires at least 100 Lok Sabha members or 50 Rajya Sabha members. These are notice thresholds, not the special majority ultimately required by Article 124(4). A validly signed notice does not compel admission: the Speaker or Chairman may admit or refuse it after the statutory consideration.',
'సెక్షన్ 3 ప్రకారం లోక్‌సభలో కనీసం 100 మంది లేదా రాజ్యసభలో 50 మంది సభ్యులు అవసరం. ఇవి నోటీసుకు అవసరమైన సంఖ్యలు; ప్రకరణ 124(4) కింద తుది ఆమోదానికి అవసరమైన ప్రత్యేక మెజారిటీ కాదు. తగిన సంతకాలు ఉన్నంత మాత్రాన అనుమతి తప్పనిసరి కాదు; చట్టప్రకారం పరిశీలించిన తరువాత స్పీకర్ లేదా చైర్మన్ అనుమతించవచ్చు లేదా తిరస్కరించవచ్చు.',
'Only option3 states both statutory thresholds; remaining options reverse or reduce/equalise them.',primary=INQ)

add('inquiry-committee',291,'paragraph 17','Judges (Inquiry) Act 1968, section 3(2)',
'The three-member inquiry committee comprises a person chosen among the CJI and other Supreme Court judges, a Chief Justice of a High Court, and a distinguished jurist.',
'ముగ్గురు సభ్యుల విచారణ కమిటీలో ప్రధాన న్యాయమూర్తి, ఇతర సుప్రీంకోర్టు న్యాయమూర్తులలో ఒకరు; ఒక హైకోర్టు ప్రధాన న్యాయమూర్తి; ఒక విశిష్ట న్యాయవేత్త ఉంటారు.',
'Which composition follows section 3(2) of the Judges (Inquiry) Act, 1968?',
'న్యాయమూర్తుల విచారణ చట్టం, 1968లో సెక్షన్ 3(2) ప్రకారం కమిటీ నిర్మాణం ఏది?',
['A CJI/other Supreme Court judge, a High Court Chief Justice and a distinguished jurist','Three Union Ministers','The President, Prime Minister and CJI','Two MPs and the Attorney-General'],
['ప్రధాన న్యాయమూర్తి/మరో సుప్రీంకోర్టు న్యాయమూర్తి, ఒక హైకోర్టు ప్రధాన న్యాయమూర్తి, ఒక విశిష్ట న్యాయవేత్త','ముగ్గురు కేంద్ర మంత్రులు','రాష్ట్రపతి, ప్రధానమంత్రి, ప్రధాన న్యాయమూర్తి','ఇద్దరు ఎంపీలు, అటార్నీ జనరల్'],1,
'After admission, the presiding officer constitutes the statutory three-member committee to investigate the grounds. Its categories are a Supreme Court judge including the CJI, a High Court Chief Justice and a distinguished jurist. Political executive or parliamentary membership does not substitute for these prescribed categories.',
'నోటీసును అనుమతించిన తరువాత ఆరోపణలపై విచారణకు సభాధ్యక్షుడు చట్టబద్ధమైన ముగ్గురు సభ్యుల కమిటీని ఏర్పాటు చేస్తారు. సభ్యుల వర్గాలు: ప్రధాన న్యాయమూర్తి సహా ఒక సుప్రీంకోర్టు న్యాయమూర్తి, ఒక హైకోర్టు ప్రధాన న్యాయమూర్తి, ఒక విశిష్ట న్యాయవేత్త. ఈ నిర్దేశిత వర్గాల స్థానంలో రాజకీయ కార్యనిర్వాహక లేదా పార్లమెంటు సభ్యులను చేర్చలేరు.',
'Option1 matches all three statutory categories;2–4 substitute constitutionally important but statutorily unqualified office combinations.',primary=INQ)

add('seat',292,'paragraph 23','Article 130',
'The Supreme Court sits in Delhi or another place or places appointed by the CJI with the President’s approval.',
'సుప్రీంకోర్టు ఢిల్లీలో లేదా రాష్ట్రపతి ఆమోదంతో ప్రధాన న్యాయమూర్తి నిర్ణయించే ఇతర ప్రదేశంలో లేదా ప్రదేశాల్లో సమావేశమవుతుంది.',
'The Supreme Court is to sit at a place outside Delhi under Article 130. Which approval arrangement applies?',
'ప్రకరణ 130 కింద సుప్రీంకోర్టు ఢిల్లీ వెలుపల సమావేశం కావాలి. ఏ ఆమోద ఏర్పాటు వర్తిస్తుంది?',
['The Governor alone selects the place','A State Assembly resolution is sufficient','The Union Cabinet alone relocates the Court','The CJI appoints the place with the President’s approval'],
['గవర్నర్ ఒక్కరే ప్రదేశాన్ని ఎంచుకుంటారు','రాష్ట్ర శాసనసభ తీర్మానం సరిపోతుంది','కేంద్ర మంత్రివర్గం ఒక్కటే కోర్టును తరలిస్తుంది','రాష్ట్రపతి ఆమోదంతో ప్రధాన న్యాయమూర్తి ప్రదేశాన్ని నిర్ణయిస్తారు'],4,
'Article 130 combines the CJI’s choice with presidential approval. It permits another place or places; it does not automatically create a separate regional Supreme Court or require a State legislature to confer jurisdiction. The question concerns the constitutional seat arrangement, not administrative proposals.',
'ప్రకరణ 130 ప్రకారం ప్రధాన న్యాయమూర్తి నిర్ణయానికి రాష్ట్రపతి ఆమోదం అవసరం. మరో ప్రదేశం లేదా ప్రదేశాల్లో సమావేశానికి ఇది అనుమతిస్తుంది; ప్రత్యేక ప్రాంతీయ సుప్రీంకోర్టు స్వయంచాలకంగా ఏర్పడదు. అధికార పరిధి కోసం రాష్ట్ర శాసనసభ అనుమతి అవసరమని ఈ నిబంధన చెప్పదు. ప్రశ్న రాజ్యాంగంలోని సమావేశ స్థల ఏర్పాటుకు సంబంధించినది.',
'Only4 contains both required actors in their correct roles.',fmt='application')

add('constitutional-appeal',293,'table 11, constitutional cases','Article 132(1)',
'An Article 132 appeal from a High Court requires its Article 134A certificate that the case involves a substantial question of law as to constitutional interpretation; the proceeding may be civil, criminal or other.',
'ప్రకరణ 132 కింద హైకోర్టు నుంచి అప్పీల్‌కు, రాజ్యాంగ వ్యాఖ్యానంపై గంభీర న్యాయ ప్రశ్న ఉన్నట్లు ప్రకరణ 134A ప్రకారం హైకోర్టు ధ్రువపత్రం అవసరం; విచారణ సివిల్, క్రిమినల్ లేదా ఇతర రకమైనదైనా కావచ్చు.',
'A High Court decides a criminal proceeding involving a substantial question of constitutional interpretation. Which statement about Article 132 is correct?',
'రాజ్యాంగ వ్యాఖ్యానంపై గంభీర న్యాయ ప్రశ్న ఉన్న క్రిమినల్ విచారణలో హైకోర్టు నిర్ణయం ఇచ్చింది. ప్రకరణ 132 గురించి సరైన వాక్యం ఏది?',
['It is unavailable because the proceeding is criminal','It may apply with the requisite High Court certificate under Article 134A','It requires every case to involve a death sentence','It requires the President to refer the appeal'],
['విచారణ క్రిమినల్ కాబట్టి అది వర్తించదు','ప్రకరణ 134A కింద అవసరమైన హైకోర్టు ధ్రువపత్రంతో అది వర్తించవచ్చు','ప్రతి కేసులో మరణశిక్ష ఉండాలి','రాష్ట్రపతి అప్పీల్‌ను సూచించాలి'],2,
'Article 132 covers civil, criminal or other proceedings when the High Court certifies the substantial constitutional-interpretation question under Article 134A. It should not be confused with the narrower criminal appeal routes under Article 134 or the President’s advisory reference under Article 143.',
'ప్రకరణ 134A కింద హైకోర్టు గంభీర రాజ్యాంగ వ్యాఖ్యాన ప్రశ్న ఉన్నట్లు ధ్రువీకరిస్తే, సివిల్, క్రిమినల్ లేదా ఇతర విచారణలకు ప్రకరణ 132 వర్తిస్తుంది. దీనిని ప్రకరణ 134లోని ప్రత్యేక క్రిమినల్ అప్పీల్ మార్గాలు లేదా ప్రకరణ 143లోని రాష్ట్రపతి సలహా సూచనతో కలపకూడదు.',
'Option2 alone preserves the certificate and inclusive proceeding scope;1 excludes a permitted category,3 imports death-sentence route,4 imports advisory jurisdiction.',fmt='application')

add('civil-appeal-certificate',293,'table 11, civil cases','Article 133(1)',
'A civil appeal under Article 133(1) requires the High Court to certify both a substantial question of law of general importance and that in its opinion the question needs Supreme Court decision.',
'ప్రకరణ 133(1) కింద సివిల్ అప్పీల్‌కు సాధారణ ప్రాధాన్యం గల గంభీర న్యాయ ప్రశ్న ఉందని, తన అభిప్రాయంలో ఆ ప్రశ్నపై సుప్రీంకోర్టు నిర్ణయం అవసరమని హైకోర్టు ధ్రువీకరించాలి.',
'For a civil appeal under Article 133(1), which certificate findings are required? 1. A substantial question of law of general importance. 2. In the High Court’s opinion, the question needs decision by the Supreme Court.',
'ప్రకరణ 133(1) కింద సివిల్ అప్పీల్ ధ్రువపత్రానికి ఏ నిర్ధారణలు అవసరం? 1. సాధారణ ప్రాధాన్యం గల గంభీర న్యాయ ప్రశ్న ఉండటం. 2. హైకోర్టు అభిప్రాయంలో ఆ ప్రశ్నపై సుప్రీంకోర్టు నిర్ణయం అవసరం కావడం.',
['1 only','2 only','Both 1 and 2','Neither 1 nor 2'],
['1 మాత్రమే','2 మాత్రమే','1, 2 రెండూ','1 కాదు, 2 కాదు'],3,
'Both conditions are cumulative. Mere disagreement with a factual finding or a high monetary value does not by itself satisfy the constitutional certificate test. This route is distinct from the Supreme Court’s discretionary special leave under Article 136.',
'రెండు షరతులూ కలిపి అవసరం. వాస్తవ నిర్ధారణతో విభేదించడం లేదా దావా విలువ ఎక్కువగా ఉండటం మాత్రమే రాజ్యాంగ ధ్రువపత్ర ప్రమాణాన్ని నెరవేర్చదు. ఈ మార్గం ప్రకరణ 136 కింద సుప్రీంకోర్టు విచక్షణాత్మక ప్రత్యేక అనుమతికి భిన్నం.',
'Both1and2 are express cumulative findings; single-condition distractors omit a required limb.',fmt='statement-combination')

add('advisory-two-classes',294,'paragraph 38','Article 143(1) and (2)',
'The Supreme Court may report its opinion on an Article 143(1) public-importance reference, but shall report on a dispute referred under Article 143(2), which concerns the Article 131 proviso category.',
'ప్రకరణ 143(1) కింద ప్రజా ప్రాధాన్య సూచనపై సుప్రీంకోర్టు అభిప్రాయం తెలియజేయవచ్చు; ప్రకరణ 131 మినహాయింపు వర్గానికి చెందిన వివాదాన్ని ప్రకరణ 143(2) కింద సూచిస్తే అభిప్రాయం తెలియజేయాలి.',
'Which distinction between the two clauses of Article 143 is accurate?',
'ప్రకరణ 143లోని రెండు ఖండికల మధ్య సరైన భేదం ఏది?',
['Both require the Court to answer every reference','Clause (1) is for private appeals; clause (2) is for criminal appeals','Clause (1) gives binding decrees to the President; clause (2) gives no opinion','Clause (1) uses “may report”; clause (2) uses “shall report” for its specified dispute category'],
['రెండింటిలోనూ ప్రతి సూచనకు సమాధానం తప్పనిసరి','ఖండిక (1) వ్యక్తిగత అప్పీళ్లకు, ఖండిక (2) క్రిమినల్ అప్పీళ్లకు సంబంధించినవి','ఖండిక (1) రాష్ట్రపతికి బద్ధమైన డిక్రీ ఇస్తుంది; ఖండిక (2) అభిప్రాయం ఇవ్వదు','ఖండిక (1) అభిప్రాయం తెలియజేయవచ్చని, ఖండిక (2) తన నిర్దిష్ట వివాద వర్గంపై తెలియజేయాలని చెబుతాయి'],4,
'Article 143(1) concerns a law or fact question of such nature and public importance that the President considers it expedient to obtain the opinion; the Court may report. Clause (2) concerns the pre-Constitution instrument disputes excluded by the proviso to Article 131 and uses shall. An advisory opinion is not an appellate decree against a litigant.',
'ప్రకరణ 143(1) స్వభావం, ప్రజా ప్రాధాన్యం దృష్ట్యా అభిప్రాయం పొందడం సముచితమని రాష్ట్రపతి భావించే న్యాయ లేదా వాస్తవ ప్రశ్నకు సంబంధించినది; కోర్టు అభిప్రాయం తెలియజేయవచ్చు. ఖండిక (2) ప్రకరణ 131 మినహాయింపులోని రాజ్యాంగ పూర్వ ఒప్పంద తదితర వివాదాలకు సంబంధించినది; అభిప్రాయం తెలియజేయాలని చెబుతుంది. సలహా అభిప్రాయం కక్షిదారుపై అప్పీల్ డిక్రీ కాదు.',
'Option4 reflects the express may/shall contrast;1 overstates1431,2/3 misclassify advisory jurisdiction.')

add('curative-boundary',296,'paragraph 46','Rupa Ashok Hurra; Supreme Court Rules 2013 Order XLVIII',
'A curative petition is an exceptional, tightly controlled remedy after dismissal of review, associated with Rupa Ashok Hurra; it is not an ordinary second appeal.',
'సమీక్ష పిటిషన్ తిరస్కరణ తరువాత క్యూరేటివ్ పిటిషన్ అసాధారణమైన, కఠిన నియంత్రణలున్న పరిహారం; ఇది రూపా అశోక్ హుర్రా కేసుతో సంబంధించింది, సాధారణ రెండవ అప్పీల్ కాదు.',
'After a review petition is dismissed, a litigant treats a curative petition as an automatic second appeal on the same merits. Which assessment is correct?',
'సమీక్ష పిటిషన్ తిరస్కరణ తరువాత అదే అంశాలపై క్యూరేటివ్ పిటిషన్‌ను స్వయంచాలక రెండవ అప్పీల్‌గా ఒక కక్షిదారు భావించారు. సరైన అంచనా ఏది?',
['Incorrect: curative jurisdiction is exceptional and subject to stringent safeguards','Correct: every dismissed review must receive a full fresh appeal','Correct: a curative petition lies directly to the President','Incorrect only because curative petitions are a High Court remedy'],
['సరికాదు: క్యూరేటివ్ అధికార పరిధి అసాధారణమైనది; కఠిన రక్షణలు వర్తిస్తాయి','సరైనది: తిరస్కరించిన ప్రతి సమీక్షకు పూర్తిస్థాయి కొత్త అప్పీల్ తప్పనిసరి','సరైనది: క్యూరేటివ్ పిటిషన్‌ను నేరుగా రాష్ట్రపతికి సమర్పిస్తారు','క్యూరేటివ్ పిటిషన్ హైకోర్టు పరిహారం కాబట్టి మాత్రమే సరికాదు'],1,
'Rupa Ashok Hurra developed the exceptional mechanism to prevent abuse of process and cure gross miscarriage of justice even after review dismissal. Order XLVIII imposes safeguards, including prescribed certification and initial circulation. It is not a routine rehearing. GBK’s incomplete case-name form is not adopted as an academic fact.',
'సమీక్ష తిరస్కరణ తరువాత కూడా న్యాయప్రక్రియ దుర్వినియోగాన్ని నివారించి, తీవ్రమైన అన్యాయాన్ని సరిచేయడానికి రూపా అశోక్ హుర్రా కేసులో ఈ అసాధారణ విధానం అభివృద్ధి చెందింది. నిర్దేశిత ధ్రువీకరణ, ప్రాథమిక సర్క్యులేషన్ సహా ఆర్డర్ XLVIII రక్షణలు విధిస్తుంది. ఇది సాధారణ పునర్విచారణ కాదు. జీబీకేలో అసంపూర్ణంగా ఉన్న కేసు పేరును అధ్యయన వాస్తవంగా స్వీకరించలేదు.',
'Option1 alone states the exceptional boundary;2 makes a nonautomatic remedy automatic,3/4 assign it to the wrong institution.',fmt='application',primary=CUR)

add('aid-authorities',296,'paragraph 48','Article 144',
'All civil and judicial authorities in India shall act in aid of the Supreme Court under Article 144.',
'ప్రకరణ 144 ప్రకారం భారతదేశంలోని సివిల్, న్యాయ అధికారులందరూ సుప్రీంకోర్టుకు సహాయంగా వ్యవహరించాలి.',
'Under Article 144, who must act in aid of the Supreme Court?',
'ప్రకరణ 144 ప్రకారం సుప్రీంకోర్టుకు సహాయంగా ఎవరు వ్యవహరించాలి?',
['Only High Court judges','All civil and judicial authorities in the territory of India','Only Union ministries, excluding States','Only authorities named in an Article 143 reference'],
['హైకోర్టు న్యాయమూర్తులు మాత్రమే','భారత భూభాగంలోని సివిల్, న్యాయ అధికారులందరూ','రాష్ట్రాలను మినహాయించి కేంద్ర మంత్రిత్వశాఖలు మాత్రమే','ప్రకరణ 143 సూచనలో పేర్కొన్న అధికారులు మాత్రమే'],2,
'Article 144 expressly extends the duty to all civil and judicial authorities in India. It is broader than High Courts or Union departments alone. It supports effective implementation of the Court’s functions; it does not turn every authority into an appellate court.',
'ప్రకరణ 144 భారతదేశంలోని సివిల్, న్యాయ అధికారులందరికీ ఈ విధిని స్పష్టంగా విస్తరిస్తుంది. ఇది హైకోర్టులు లేదా కేంద్ర శాఖలకు మాత్రమే పరిమితం కాదు. కోర్టు విధులు సమర్థంగా అమలవడానికి ఇది తోడ్పడుతుంది; ప్రతి అధికారిని అప్పీల్ కోర్టుగా మార్చదు.',
'Option2 reproduces scope accurately;1/3/4 impose restrictions absent from the provision.')

add('rules-approval',297,'paragraph 24','Article 145(1)',
'Subject to parliamentary law, the Supreme Court may make practice and procedure rules with the President’s approval.',
'పార్లమెంటు చట్టానికి లోబడి, రాష్ట్రపతి ఆమోదంతో సుప్రీంకోర్టు తన ఆచరణ, ప్రక్రియ నియమాలను రూపొందించవచ్చు.',
'Which statement correctly describes the Supreme Court’s rule-making under Article 145(1)?',
'ప్రకరణ 145(1) కింద సుప్రీంకోర్టు నియమాల రూపకల్పనను సరిగ్గా తెలిపే వాక్యం ఏది?',
['Rules are made by each Governor for the Supreme Court','Rules need no presidential approval and override parliamentary law','The Court makes rules with presidential approval, subject to parliamentary law','Only the Lok Sabha Speaker may issue procedural rules'],
['సుప్రీంకోర్టుకు ప్రతి గవర్నర్ నియమాలు రూపొందిస్తారు','రాష్ట్రపతి ఆమోదం అవసరం లేదు; నియమాలు పార్లమెంటు చట్టాన్ని అధిగమిస్తాయి','పార్లమెంటు చట్టానికి లోబడి రాష్ట్రపతి ఆమోదంతో కోర్టు నియమాలు రూపొందిస్తుంది','లోక్‌సభ స్పీకర్ మాత్రమే ప్రక్రియ నియమాలు జారీ చేయవచ్చు'],3,
'Article 145(1) gives the Court rule-making power over practice and procedure, with presidential approval and subject to parliamentary law. Institutional autonomy therefore operates within constitutional checks. This general power differs from Article 146 staff-service rules, where specified financial rules particularly require presidential approval.',
'ప్రకరణ 145(1) రాష్ట్రపతి ఆమోదం, పార్లమెంటు చట్టానికి లోబడి ఆచరణ, ప్రక్రియపై నియమాల రూపకల్పన అధికారాన్ని కోర్టుకు ఇస్తుంది. సంస్థాగత స్వయంప్రతిపత్తి రాజ్యాంగ నియంత్రణల మధ్య పనిచేస్తుంది. ఇది ప్రకరణ 146లోని సిబ్బంది సేవా నియమాలకు భిన్నం; అక్కడ నిర్దిష్ట ఆర్థిక నియమాలకు ప్రత్యేకంగా రాష్ట్రపతి ఆమోదం అవసరం.',
'Only3 preserves both checks and the correct rule-maker;2 erases both checks.')

add('open-majority-dissent',297,'paragraph 24','Article 145(4) and (5)',
'Supreme Court judgments are delivered in open court; judgments and Article 143 opinions require concurrence of a majority present at the hearing, without preventing a dissenting judgment or opinion.',
'సుప్రీంకోర్టు తీర్పులను బహిరంగ న్యాయస్థానంలో ప్రకటించాలి; తీర్పులు, ప్రకరణ 143 అభిప్రాయాలకు విచారణలో ఉన్న న్యాయమూర్తుల మెజారిటీ సమ్మతి అవసరం, భిన్నాభిప్రాయం ప్రకటించడాన్ని ఇది నిరోధించదు.',
'Consider Article 145: 1. No Supreme Court judgment is delivered except in open court. 2. A majority may decide, while a non-concurring judge may deliver a dissent. Which are correct?',
'ప్రకరణ 145ను పరిశీలించండి: 1. సుప్రీంకోర్టు తీర్పును బహిరంగ న్యాయస్థానంలోనే ప్రకటించాలి. 2. మెజారిటీ నిర్ణయించవచ్చు; సమ్మతించని న్యాయమూర్తి భిన్నాభిప్రాయం ప్రకటించవచ్చు. సరైనవి ఏవి?',
['1 only','2 only','Neither 1 nor 2','Both 1 and 2'],
['1 మాత్రమే','2 మాత్రమే','1 కాదు, 2 కాదు','1, 2 రెండూ'],4,
'Article 145(4) governs open-court delivery of judgments and reports of advisory opinions. Clause (5) requires concurrence of a majority of judges present at the hearing but expressly preserves dissent. It does not require unanimity or prohibit separate judicial reasons.',
'ప్రకరణ 145(4) తీర్పుల బహిరంగ ప్రకటనకు, సలహా అభిప్రాయ నివేదికకు వర్తిస్తుంది. ఖండిక (5) విచారణలో ఉన్న న్యాయమూర్తుల మెజారిటీ సమ్మతిని కోరుతూ భిన్నాభిప్రాయాన్ని స్పష్టంగా రక్షిస్తుంది. ఏకగ్రీవతను కోరదు; వేరు న్యాయ కారణాలను నిషేధించదు.',
'Both clauses are correctly paraphrased;1/2 alone omit another true safeguard.',fmt='statement-combination')

add('staff-appointment',297,'paragraph 27, independence safeguard on staff','Article 146(1)',
'Supreme Court staff appointments are made by the CJI or another judge or officer whom the CJI directs, subject to the Article 146(1) proviso about prescribed UPSC consultation.',
'సుప్రీంకోర్టు సిబ్బంది నియామకాలను ప్రధాన న్యాయమూర్తి లేదా ఆయన ఆదేశించిన మరో న్యాయమూర్తి లేదా అధికారి చేస్తారు; నిర్దేశిత యూపీఎస్సీ సంప్రదింపుపై ప్రకరణ 146(1) మినహాయింపు వర్తిస్తుంది.',
'Who makes Supreme Court staff appointments under Article 146(1), subject to its proviso?',
'ప్రకరణ 146(1)లోని మినహాయింపుకు లోబడి సుప్రీంకోర్టు సిబ్బంది నియామకాలను ఎవరు చేస్తారు?',
['The CJI, or another judge or officer directed by the CJI','The Lok Sabha Secretariat','Every State Public Service Commission jointly','The Chief Election Commissioner'],
['ప్రధాన న్యాయమూర్తి లేదా ఆయన ఆదేశించిన మరో న్యాయమూర్తి లేదా అధికారి','లోక్‌సభ సచివాలయం','అన్ని రాష్ట్ర పబ్లిక్ సర్వీస్ కమిషన్లు సంయుక్తంగా','ప్రధాన ఎన్నికల కమిషనర్'],1,
'Article 146(1) gives the CJI the power with an express ability to direct another judge or officer. The proviso permits presidential rules requiring UPSC consultation for specified appointments of persons not already attached to the Court. Therefore saying that the CJI must personally make every appointment without any qualification would be too broad.',
'ప్రకరణ 146(1) ప్రధాన న్యాయమూర్తికి ఈ అధికారాన్ని ఇస్తూ, మరో న్యాయమూర్తి లేదా అధికారిని ఆదేశించే అవకాశాన్ని స్పష్టంగా కల్పిస్తుంది. ఇప్పటికే కోర్టుకు అనుబంధంగా లేని వ్యక్తుల నిర్దిష్ట నియామకాలకు యూపీఎస్సీ సంప్రదింపు అవసరమని రాష్ట్రపతి నియమాలు విధించవచ్చని మినహాయింపు చెబుతుంది. అందువల్ల ప్రతి నియామకాన్ని ఎటువంటి పరిమితి లేకుండా ప్రధాన న్యాయమూర్తే స్వయంగా చేయాలని చెప్పడం అతివ్యాప్తి.',
'Only1 includes the constitutional appointment/delegation mechanism; the others have no Article146 staff role.')

add('administrative-charge',297,'paragraph 27, charged expenditure','Article 146(3)',
'Supreme Court administrative expenses, including staff salaries, allowances and pensions, are charged upon the Consolidated Fund of India; Court fees form part of that Fund.',
'సిబ్బంది జీతాలు, భత్యాలు, పెన్షన్లు సహా సుప్రీంకోర్టు పరిపాలనా వ్యయాలు భారత సంచిత నిధిపై భారితమవుతాయి; కోర్టు ఫీజులు ఆ నిధిలో భాగమవుతాయి.',
'Which statement follows Article 146(3) regarding Supreme Court administration?',
'సుప్రీంకోర్టు పరిపాలన విషయంలో ప్రకరణ 146(3)కు అనుగుణమైన వాక్యం ఏది?',
['Staff expenses are charged on every State’s Consolidated Fund','Administrative expenses are charged on the Consolidated Fund of India','All staff expenses require an annual Lok Sabha vote as voted expenditure','Court fees belong personally to the CJI'],
['సిబ్బంది వ్యయాలు ప్రతి రాష్ట్ర సంచిత నిధిపై భారితమవుతాయి','పరిపాలనా వ్యయాలు భారత సంచిత నిధిపై భారితమవుతాయి','సిబ్బంది వ్యయాలన్నింటికీ ఓటు వ్యయంగా ఏటా లోక్‌సభ ఆమోదం అవసరం','కోర్టు ఫీజులు ప్రధాన న్యాయమూర్తికి వ్యక్తిగతంగా చెందుతాయి'],2,
'Article 146(3) charges administrative expenses, including the listed staff payments, on the Consolidated Fund of India and credits Court fees to it. Charged expenditure is distinct from expenditure submitted to the House’s vote. This question concerns administration, not merely the separate Article 125 judicial-salary provision already tested elsewhere.',
'ప్రకరణ 146(3) పేర్కొన్న సిబ్బంది చెల్లింపులు సహా పరిపాలనా వ్యయాలను భారత సంచిత నిధిపై భారితం చేసి, కోర్టు ఫీజులను అందులో జమ చేస్తుంది. భారిత వ్యయం సభ ఓటుకు సమర్పించే వ్యయానికి భిన్నమైనది. ఈ ప్రశ్న పరిపాలనకు సంబంధించినది; వేరే చోట పరీక్షించిన ప్రకరణ 125 న్యాయమూర్తుల జీతాలకు మాత్రమే సంబంధించినది కాదు.',
'Only2 states the right fund and charging rule;1 changes fund,3 changes expenditure treatment,4 misappropriates fees.')

add('parliament-conduct',301,'paragraphs 25–27, conduct safeguard','Article 121',
'Discussion in Parliament of Supreme Court or High Court judges’ conduct in discharge of duties is barred except upon a motion for presenting an address to the President praying for removal.',
'విధి నిర్వహణలో సుప్రీంకోర్టు లేదా హైకోర్టు న్యాయమూర్తుల ప్రవర్తనపై పార్లమెంటులో చర్చ నిషిద్ధం; తొలగింపును కోరుతూ రాష్ట్రపతికి అభ్యర్థన సమర్పించే తీర్మానం సందర్భంలో మినహాయింపు ఉంది.',
'Which exception does Article 121 permit to the parliamentary restriction on discussion of a judge’s conduct in discharge of duties?',
'విధి నిర్వహణలో న్యాయమూర్తి ప్రవర్తనపై పార్లమెంటు చర్చ ఆంక్షకు ప్రకరణ 121 ఏ మినహాయింపును అనుమతిస్తుంది?',
['Any question-hour question','Any ordinary budget debate','A motion for presenting an address to the President praying for removal','A State Minister’s request'],
['ఏ ప్రశ్నోత్తరాల ప్రశ్ననైనా','ఏ సాధారణ బడ్జెట్ చర్చనైనా','తొలగింపును కోరుతూ రాష్ట్రపతికి అభ్యర్థన సమర్పించే తీర్మానాన్ని','రాష్ట్ర మంత్రి అభ్యర్థనను'],3,
'Article 121 specifies the removal-address motion exception. Routine parliamentary scrutiny cannot be used to discuss a judge’s conduct in discharge of duties. Article 211 is a separate State-legislature prohibition and should not be supplied with a removal-motion exception that its text does not contain.',
'ప్రకరణ 121 తొలగింపు అభ్యర్థన తీర్మానాన్ని మినహాయింపుగా నిర్దేశిస్తుంది. సాధారణ పార్లమెంటు పరిశీలన పేరుతో విధి నిర్వహణలో న్యాయమూర్తి ప్రవర్తనను చర్చించలేరు. ప్రకరణ 211 రాష్ట్ర శాసనసభలకు వేరు నిషేధం; దాని పాఠ్యంలో లేని తొలగింపు తీర్మాన మినహాయింపును దానికి జోడించకూడదు.',
'Only3 is the express constitutional exception;1/2/4 are ordinary political processes not exceptions.')

add('postretirement-practice',301,'paragraph 27, post-retirement practice','Article 124(7)',
'A person who has held office as a Supreme Court judge may not plead or act in any court or before any authority in India; this advocacy bar is distinct from Article 128 judicial attendance.',
'సుప్రీంకోర్టు న్యాయమూర్తిగా పనిచేసిన వ్యక్తి భారతదేశంలోని ఏ కోర్టులోనూ, ఏ అధికారి ఎదుటనూ న్యాయవాదిగా వాదించకూడదు లేదా వ్యవహరించకూడదు; ఈ నిషేధం ప్రకరణ 128 కింద న్యాయమూర్తిగా హాజరుకు భిన్నం.',
'A former Supreme Court judge proposes to represent a private client before an Indian tribunal. Which statement is correct under Article 124(7)?',
'సుప్రీంకోర్టు మాజీ న్యాయమూర్తి భారతదేశంలోని ఒక ట్రిబ్యునల్ ముందు వ్యక్తిగత కక్షిదారుకు ప్రాతినిధ్యం వహించాలని భావించారు. ప్రకరణ 124(7) ప్రకారం సరైన వాక్యం ఏది?',
['It is allowed whenever the tribunal is outside Delhi','It is allowed after a two-year waiting period','It is allowed if the CJI informally agrees','Pleading or acting before an authority in India is barred'],
['ట్రిబ్యునల్ ఢిల్లీ వెలుపల ఉంటే అనుమతి ఉంది','రెండేళ్ల నిరీక్షణ తరువాత అనుమతి ఉంది','ప్రధాన న్యాయమూర్తి అనధికారికంగా అంగీకరిస్తే అనుమతి ఉంది','భారతదేశంలో ఒక అధికారి ఎదుట న్యాయవాదిగా వాదించడం లేదా వ్యవహరించడం నిషిద్ధం'],4,
'Article 124(7) bars pleading or acting in any court or before any authority within India after holding Supreme Court judicial office. It contains no two-year expiry or Delhi-only limit. Article 128 concerns sitting as a judge by the prescribed process; it does not authorise private advocacy.',
'సుప్రీంకోర్టు న్యాయమూర్తిగా పనిచేసిన తరువాత భారతదేశంలోని ఏ కోర్టులోనూ, ఏ అధికారి ఎదుటనూ న్యాయవాదిగా వాదించడం లేదా వ్యవహరించడాన్ని ప్రకరణ 124(7) నిషేధిస్తుంది. రెండేళ్ల తరువాత ముగింపు లేదా ఢిల్లీకి మాత్రమే పరిమితి లేదు. ప్రకరణ 128 నిర్దేశిత విధానంలో న్యాయమూర్తిగా విచారణలో కూర్చోవడానికి సంబంధించినది; వ్యక్తిగత న్యాయవాద వృత్తికి అనుమతి కాదు.',
'Option4 applies the all-India court/authority bar;1/2 invent territorial/time exceptions and3 invents an informal waiver.',fmt='application')

GRAM='https://thc.nic.in/Central%20Governmental%20Acts/Gram%20Nyayalayas%20Act,%202008.pdf'
FAMILY='https://www.indiacode.nic.in/bitstream/123456789/1844/1/A1984__66.pdf'
add('gram-commencement',306,'Ch38 paragraph20; commencement absent there','Department of Justice: implementation from2October2009',
'The Gram Nyayalayas Act,2008 came into force on2October2009; the Act’s short-title year is distinct from its commencement date.',
'గ్రామ న్యాయాలయాల చట్టం, 2008 అమలు 2009 అక్టోబరు 2న ప్రారంభమైంది; చట్టం పేరులోని సంవత్సరం, అమలు ప్రారంభ తేదీ వేర్వేరు.',
'When did the Gram Nyayalayas Act,2008 come into force?',
'గ్రామ న్యాయాలయాల చట్టం, 2008 ఎప్పుడు అమల్లోకి వచ్చింది?',
['2October2008','26January2009','2October2009','15August2010'],
['2008 అక్టోబరు 2','2009 జనవరి 26','2009 అక్టోబరు 2','2010 ఆగస్టు 15'],3,
'The Department of Justice records2October2009 as commencement. The short title says2008; the enactment is Act4of2009. Short-title year, assent/enactment and commencement should not be treated as the same event.',
'అమలు ప్రారంభాన్ని న్యాయశాఖ 2009 అక్టోబరు 2గా నమోదు చేసింది. సంక్షిప్త పేరు 2008ను సూచిస్తుంది; ఇది 2009లోని 4వ చట్టం. సంక్షిప్త పేరులోని సంవత్సరం, ఆమోదం/చట్టరూపం, అమలు ప్రారంభాన్ని ఒకే ఘట్టంగా భావించకూడదు.',
'Option3 matches the official commencement;1 confuses the short-title year and2/4 are unrelated national-day distractors.',primary='https://dashboard.doj.gov.in/gn/introduction')

add('gram-appointment',306,'Ch38 paragraph21; table7','Gram Nyayalayas Act2008 sections5–7',
'The State Government appoints a Nyayadhikari in consultation with the High Court; eligibility is that of appointment as a Judicial Magistrate of the first class.',
'హైకోర్టుతో సంప్రదించి రాష్ట్ర ప్రభుత్వం న్యాయాధికారిని నియమిస్తుంది; ప్రథమ శ్రేణి జ్యుడీషియల్ మేజిస్ట్రేట్‌గా నియామక అర్హత ఉండాలి.',
'Which pair correctly identifies appointment of a Nyayadhikari and the required judicial eligibility?',
'న్యాయాధికారి నియామకం, అవసరమైన న్యాయ అర్హతను సరిగ్గా తెలిపే జత ఏది?',
['State Government in consultation with High Court — eligible as Judicial Magistrate first class','Gram Sabha alone — elected sarpanch','President alone — qualified Supreme Court judge','District Collector alone — any revenue officer'],
['హైకోర్టుతో సంప్రదించి రాష్ట్ర ప్రభుత్వం — ప్రథమ శ్రేణి జ్యుడీషియల్ మేజిస్ట్రేట్ అర్హత','గ్రామసభ మాత్రమే — ఎన్నికైన సర్పంచ్','రాష్ట్రపతి మాత్రమే — సుప్రీంకోర్టు న్యాయమూర్తి అర్హత','జిల్లా కలెక్టర్ మాత్రమే — ఏ రెవెన్యూ అధికారి అయినా'],1,
'Sections5and6 prescribe State Government appointment in consultation with the High Court and first-class Judicial Magistrate eligibility. Nyayadhikari is a judicial office, not an elected panchayat or executive-revenue office. Section7 links service conditions to that magistrate category.',
'సెక్షన్లు 5, 6 ప్రకారం హైకోర్టుతో సంప్రదించి రాష్ట్ర ప్రభుత్వం నియమించాలి; ప్రథమ శ్రేణి జ్యుడీషియల్ మేజిస్ట్రేట్ అర్హత అవసరం. న్యాయాధికారి న్యాయ పదవి; ఎన్నికైన పంచాయతీ లేదా కార్యనిర్వాహక రెవెన్యూ పదవి కాదు. సెక్షన్ 7 సేవా నిబంధనలను ఆ మేజిస్ట్రేట్ వర్గంతో అనుసంధానిస్తుంది.',
'Option1 matches both statutory components;2/4 replace judicial office with local/executive administration,3 imports apex-court appointments.',fmt='matching',primary=GRAM)

add('gram-mobile-scope',306,'Ch38 paragraph21; table7','Gram Nyayalayas Act2008 sections9,11–13',
'Gram Nyayalayas hold mobile proceedings in villages and exercise both civil and criminal jurisdiction only in the manner and extent provided by the Act.',
'గ్రామ న్యాయాలయాలు గ్రామాల్లో సంచార విచారణలు నిర్వహిస్తాయి; చట్టం నిర్దేశించిన విధానం, పరిమితుల్లో సివిల్, క్రిమినల్ అధికార పరిధులను రెండింటినీ వినియోగిస్తాయి.',
'Consider Gram Nyayalayas:1.They may hold mobile court proceedings near the parties or cause of action.2.They exercise both civil and criminal jurisdiction as provided by the Act.Which are correct?',
'గ్రామ న్యాయాలయాల గురించి పరిశీలించండి: 1. కక్షిదారులు లేదా వివాద కారణానికి సమీపంలో సంచార కోర్టు విచారణలు నిర్వహించవచ్చు. 2. చట్టం నిర్దేశించిన మేరకు సివిల్, క్రిమినల్ అధికార పరిధులను రెండింటినీ వినియోగిస్తాయి. సరైనవి ఏవి?',
['1only','2only','Neither1nor2','Both1and2'],
['1 మాత్రమే','2 మాత్రమే','1 కాదు, 2 కాదు','1, 2 రెండూ'],4,
'Section9 requires periodic village visits and publicity when holding mobile courts outside headquarters. Section11 gives both civil and criminal jurisdiction, qualified by the Act; sections12and13 define the respective scope. Mobility does not create unlimited jurisdiction over every dispute.',
'సెక్షన్ 9 ప్రకారం కాలానుగుణంగా గ్రామాలకు వెళ్లాలి; ప్రధాన కేంద్రం వెలుపల సంచార కోర్టు నిర్వహిస్తే తేదీ, ప్రదేశానికి విస్తృత ప్రచారం చేయాలి. సెక్షన్ 11 చట్టానికి లోబడి సివిల్, క్రిమినల్ అధికార పరిధులను ఇస్తుంది; సెక్షన్లు 12, 13 వాటి పరిధులను నిర్దేశిస్తాయి. సంచార స్వభావం ప్రతి వివాదంపై అపరిమిత అధికారాన్ని ఇవ్వదు.',
'Both are correct within statutory limits;1/2alone omit a true feature and3 denies both.',fmt='statement-combination',primary=GRAM)

add('gram-appeal-routes',307,'Ch38 paragraph22; table7','Gram Nyayalayas Act2008 sections33–34',
'Subject to statutory exclusions, Gram Nyayalaya criminal appeals lie to the Court of Session, while civil appeals lie to the District Court.',
'చట్టబద్ధమైన మినహాయింపులకు లోబడి గ్రామ న్యాయాలయం క్రిమినల్ అప్పీళ్లు సెషన్స్ కోర్టుకు, సివిల్ అప్పీళ్లు జిల్లా కోర్టుకు వెళ్తాయి.',
'Where an appeal is permitted by the Gram Nyayalayas Act, which pair correctly states the criminal and civil appellate forums respectively?',
'గ్రామ న్యాయాలయాల చట్టం అప్పీల్‌కు అనుమతించినప్పుడు, క్రిమినల్, సివిల్ అప్పీల్ వేదికలను వరుసగా సరిగ్గా తెలిపే జత ఏది?',
['District Court — Court of Session','Court of Session — District Court','High Court — Supreme Court','Gram Sabha — District Collector'],
['జిల్లా కోర్టు — సెషన్స్ కోర్టు','సెషన్స్ కోర్టు — జిల్లా కోర్టు','హైకోర్టు — సుప్రీంకోర్టు','గ్రామసభ — జిల్లా కలెక్టర్'],2,
'Section33 sends permitted criminal appeals to the Court of Session; section34 sends permitted civil appeals to the District Court. These are qualified routes: the statute excludes specified categories, including certain guilty-plea/fine cases and certain civil orders. GBK’s undifferentiated Sessions-court appeal statement is not adopted.',
'సెక్షన్ 33 అనుమతించిన క్రిమినల్ అప్పీళ్లను సెషన్స్ కోర్టుకు, సెక్షన్ 34 అనుమతించిన సివిల్ అప్పీళ్లను జిల్లా కోర్టుకు పంపుతుంది. ఇవి షరతులతో కూడిన మార్గాలు: నిర్దిష్ట నేర అంగీకార/జరిమానా కేసులు, కొన్ని సివిల్ ఉత్తర్వులు తదితర వర్గాలకు చట్టం మినహాయింపులు విధిస్తుంది. అన్ని అప్పీళ్లు సెషన్స్ కోర్టుకే అన్న జీబీకే సాధారణీకరణను స్వీకరించలేదు.',
'Option2 assigns both routes correctly;1 reverses them,3 jumps directly to higher courts,4 substitutes nonjudicial offices.',fmt='matching',primary=GRAM)

add('family-establishment',308,'Ch38 paragraph18; table6','Family Courts Act1984 section3',
'The State Government establishes Family Courts after consultation with the High Court; establishment is required for a city or town exceeding one million population and may be extended elsewhere.',
'హైకోర్టుతో సంప్రదించిన తరువాత రాష్ట్ర ప్రభుత్వం కుటుంబ న్యాయస్థానాలను ఏర్పాటు చేస్తుంది; జనాభా పది లక్షలకు మించిన నగరం లేదా పట్టణానికి ఏర్పాటు తప్పనిసరి, ఇతర ప్రాంతాల్లోనూ ఏర్పాటు చేయవచ్చు.',
'Consider section3of the Family Courts Act,1984:1.The State Government acts after consultation with the High Court.2.Establishment is obligatory for a city or town whose population exceeds one million.Which are correct?',
'కుటుంబ న్యాయస్థానాల చట్టం, 1984లోని సెక్షన్ 3ను పరిశీలించండి: 1. హైకోర్టుతో సంప్రదించిన తరువాత రాష్ట్ర ప్రభుత్వం వ్యవహరిస్తుంది. 2. జనాభా పది లక్షలకు మించిన నగరం లేదా పట్టణానికి ఏర్పాటు తప్పనిసరి. సరైనవి ఏవి?',
['1only','2only','Both1and2','Neither1nor2'],
['1 మాత్రమే','2 మాత్రమే','1, 2 రెండూ','1 కాదు, 2 కాదు'],3,
'Both statements follow section3. The Act also permits Family Courts in other areas considered necessary. The threshold says exceeds one million, not merely equals it. Establishment after consultation under section3 should be distinguished from appointment of judges with High Court concurrence under section4.',
'రెండు వాక్యాలూ సెక్షన్ 3కు అనుగుణం. అవసరమని భావించే ఇతర ప్రాంతాల్లోనూ కుటుంబ న్యాయస్థానాలను ఏర్పాటు చేయవచ్చు. పరిమితి పది లక్షలకు మించి అని చెబుతుంది; సమానంగా ఉంటే చాలని కాదు. సెక్షన్ 3లో సంప్రదింపు తరువాత కోర్టు ఏర్పాటు, సెక్షన్ 4లో హైకోర్టు సమ్మతితో న్యాయమూర్తుల నియామకం వేర్వేరు.',
'Both1and2are express;single-statementoptionsdroponecorrectcondition.',fmt='statement-combination',primary=FAMILY)

add('family-settlement',308,'Ch38 paragraphs16,19','Family Courts Act1984 section9',
'A Family Court must endeavour in the first instance to assist and persuade parties toward settlement where possible consistently with the nature and circumstances of the case.',
'కేసు స్వభావం, పరిస్థితులకు అనుగుణంగా సాధ్యమైనప్పుడు మొదట కక్షిదారులకు సహకరించి, రాజీకి ఒప్పించడానికి కుటుంబ న్యాయస్థానం ప్రయత్నించాలి.',
'At the beginning of a suitable matrimonial proceeding, which approach best reflects section9of the Family Courts Act?',
'అనుకూలమైన వైవాహిక విచారణ ప్రారంభంలో కుటుంబ న్యాయస్థానాల చట్టంలోని సెక్షన్ 9కు ఏ విధానం అనుగుణం?',
['Assist and persuade parties toward settlement, consistently with the case circumstances','Compel a settlement regardless of consent or circumstances','Refuse every contested case because only settlements are possible','Transfer every matter immediately to a Lok Adalat'],
['కేసు పరిస్థితులకు అనుగుణంగా కక్షిదారులకు సహకరించి రాజీకి ఒప్పించే ప్రయత్నం చేయడం','సమ్మతి లేదా పరిస్థితులతో సంబంధం లేకుండా బలవంతంగా రాజీ చేయించడం','రాజీ మాత్రమే సాధ్యం కాబట్టి ప్రతి వివాదాస్పద కేసును తిరస్కరించడం','ప్రతి విషయాన్ని వెంటనే లోక్ అదాలత్‌కు బదిలీ చేయడం'],1,
'Section9 places a qualified duty to attempt settlement in the first instance. It promotes conciliation, not coerced agreement. If settlement fails, the Family Court remains a statutory adjudicatory court with its own jurisdiction; it is not merely an ordinary Lok Adalat.',
'సెక్షన్ 9 మొదట రాజీకి ప్రయత్నించే విధిని పరిస్థితులకు లోబడి విధిస్తుంది. ఇది సయోధ్యను ప్రోత్సహిస్తుంది; బలవంతపు ఒప్పందాన్ని కాదు. రాజీ విఫలమైతే కుటుంబ న్యాయస్థానం తన అధికార పరిధిలో తీర్పు ఇవ్వగల చట్టబద్ధమైన కోర్టుగానే కొనసాగుతుంది; అది కేవలం సాధారణ లోక్ అదాలత్ కాదు.',
'Only1keeps the statutory endeavour and circumstances qualification;2coerces,3deniesadjudication,4inventsmandatorytransfer.',fmt='application',primary='https://www.kja.gov.in/kjauploads/media/familycourtsact_1984_1646973227.pdf')

add('family-representation',308,'Ch38 paragraph19; table6','Family Courts Act1984 section13',
'Section13 gives a Family Court litigant no entitlement as of right to legal-practitioner representation; the Court may seek a legal expert as amicus curiae in the interests of justice.',
'సెక్షన్ 13 ప్రకారం కుటుంబ న్యాయస్థానంలో న్యాయవాది ప్రాతినిధ్యాన్ని హక్కుగా కోరలేరు; న్యాయ ప్రయోజనాల కోసం కోర్టు న్యాయ నిపుణుడి సహాయాన్ని అమికస్ క్యూరీగా కోరవచ్చు.',
'Which statement accurately reflects section13of the Family Courts Act?',
'కుటుంబ న్యాయస్థానాల చట్టంలోని సెక్షన్ 13ను సరిగ్గా తెలిపే వాక్యం ఏది?',
['Every party has an unconditional statutory right to a lawyer','Legal expertise can never assist the Court','Only advocates may file or conduct any proceeding','There is no representation entitlement as of right; the Court may seek a legal expert as amicus curiae'],
['ప్రతి కక్షిదారుకు షరతుల్లేని చట్టబద్ధమైన న్యాయవాది హక్కు ఉంది','న్యాయ నిపుణుల సహాయం కోర్టుకు ఎప్పటికీ అందకూడదు','న్యాయవాదులు మాత్రమే ఏ విచారణనైనా దాఖలు చేయవచ్చు లేదా నిర్వహించవచ్చు','ప్రాతినిధ్యాన్ని హక్కుగా కోరలేరు; కోర్టు న్యాయ నిపుణుడి సహాయాన్ని అమికస్ క్యూరీగా కోరవచ్చు'],4,
'The phrase as of right is essential. Section13 restricts an automatic entitlement and expressly permits the Court to seek a legal expert’s assistance as amicus curiae when necessary in the interests of justice. It should not be rewritten as an absolute prohibition on all legal assistance.',
'హక్కుగా అనే పదబంధం కీలకం. సెక్షన్ 13 స్వయంచాలక హక్కును పరిమితం చేస్తూ, న్యాయ ప్రయోజనాలకు అవసరమైతే అమికస్ క్యూరీగా న్యాయ నిపుణుడి సహాయాన్ని కోరడానికి కోర్టుకు స్పష్టంగా అనుమతిస్తుంది. దానిని అన్ని రకాల న్యాయ సహాయంపై సంపూర్ణ నిషేధంగా మార్చకూడదు.',
'Option4preservesthequalificationandproviso;1createsunconditionalright,2deniesexpressassistance,3invertsaccessrule.',primary='https://thc.nic.in/Central%20Governmental%20Acts/Family%20Courts%20Act,%201984.pdf')

add('family-appeal-boundary',308,'Ch38 paragraph19; table6 (exceptions supplied by statute)','Family Courts Act1984 section19(1),(2),(6)',
'A permitted Family Court appeal under section19(1) lies to the High Court on facts and law; interlocutory orders and consent decrees/orders are not within that general appeal route.',
'సెక్షన్ 19(1) కింద అనుమతించిన కుటుంబ న్యాయస్థాన అప్పీల్ వాస్తవాలు, చట్టం రెండింటిపై హైకోర్టుకు వెళ్తుంది; మధ్యంతర ఉత్తర్వులు, సమ్మతి డిక్రీలు/ఉత్తర్వులు ఆ సాధారణ అప్పీల్ మార్గంలోకి రావు.',
'Which statement correctly qualifies an appeal under section19of the Family Courts Act?',
'కుటుంబ న్యాయస్థానాల చట్టంలోని సెక్షన్ 19 కింద అప్పీల్‌ను సరైన పరిమితులతో తెలిపే వాక్యం ఏది?',
['Every order, including every interlocutory order, is appealable to a District Court','Every consent decree must be appealed to the Supreme Court','Subject to statutory exclusions, appeal lies to the High Court on facts and law','No Family Court judgment can ever be appealed'],
['ప్రతి మధ్యంతర ఉత్తర్వు సహా ప్రతి ఉత్తర్వుపై జిల్లా కోర్టుకు అప్పీల్ చేయవచ్చు','ప్రతి సమ్మతి డిక్రీపై సుప్రీంకోర్టుకు అప్పీల్ తప్పనిసరి','చట్టబద్ధమైన మినహాయింపులకు లోబడి వాస్తవాలు, చట్టం రెండింటిపై హైకోర్టుకు అప్పీల్ చేయవచ్చు','కుటుంబ న్యాయస్థానం తీర్పుపై ఎప్పటికీ అప్పీల్ చేయలేరు'],3,
'Section19(1) provides the High Court route on facts and law for judgments/orders that are not interlocutory, subject to subsection2. Consent decrees/orders are excluded, and the Act separately treats maintenance orders under the specified criminal-procedure chapter. Subsection6 requires at least two High Court judges for an appeal under subsection1. Thus the prepared reader’s short summary needs statutory qualifications.',
'సెక్షన్ 19(1), ఉపసెక్షన్ 2కు లోబడి మధ్యంతరమైనవి కాని తీర్పులు/ఉత్తర్వులపై వాస్తవాలు, చట్టం రెండింటిపై హైకోర్టు అప్పీల్ మార్గాన్ని కల్పిస్తుంది. సమ్మతి డిక్రీలు/ఉత్తర్వులు మినహాయించబడ్డాయి; నిర్దేశిత క్రిమినల్ ప్రక్రియ అధ్యాయంలోని భరణ ఉత్తర్వులకు చట్టం వేరే ఏర్పాటు చేస్తుంది. ఉపసెక్షన్ 1 అప్పీల్‌ను కనీసం ఇద్దరు హైకోర్టు న్యాయమూర్తులు విచారించాలని ఉపసెక్షన్ 6 చెబుతుంది. అందువల్ల సిద్ధం చేసిన పాఠ్యంలోని సంక్షిప్త వివరణకు చట్టపరమైన పరిమితులు జోడించాలి.',
'Option3 identifies the proper forum and preserves exclusions;1 chooses the wrong court and ignores interlocutory exclusion,2 ignores consent exclusion and4 denies the statutory route.',primary='https://kja.gov.in/kjauploads/media/compendium_on_high_court_procedures_1647329697.pdf')

add('removal-grounds',291,'paragraph16','Article124(4)',
'The constitutional grounds for removal of a Supreme Court judge are proved misbehaviour or incapacity, not mere disagreement with a judgment.',
'సుప్రీంకోర్టు న్యాయమూర్తి తొలగింపుకు రాజ్యాంగ ఆధారాలు నిరూపిత దుష్ప్రవర్తన లేదా అసమర్థత; కేవలం తీర్పుతో విభేదించడం ఆధారం కాదు.',
'A judge’s decision is politically unpopular, but neither proved misbehaviour nor incapacity is established. Which assessment follows Article124(4)?',
'ఒక న్యాయమూర్తి నిర్ణయం రాజకీయంగా జనాదరణ పొందలేదు; అయితే నిరూపిత దుష్ప్రవర్తన లేదా అసమర్థత ఏదీ నిర్ధారణ కాలేదు. ప్రకరణ 124(4) ప్రకారం సరైన అంచనా ఏది?',
['Unpopularity alone is an additional constitutional ground','The Union Cabinet may dismiss the judge for loss of confidence','The stated facts do not establish either constitutional removal ground','A simple resolution of one House removes the judge automatically'],
['జనాదరణ లేకపోవడమే అదనపు రాజ్యాంగ ఆధారం','విశ్వాసం కోల్పోయారని కేంద్ర మంత్రివర్గం న్యాయమూర్తిని తొలగించవచ్చు','పేర్కొన్న వాస్తవాలు ఏ రాజ్యాంగ తొలగింపు ఆధారాన్నీ నిర్ధారించవు','ఒక సభ సాధారణ తీర్మానం న్యాయమూర్తిని స్వయంచాలకంగా తొలగిస్తుంది'],3,
'Article124(4) limits removal to proved misbehaviour or incapacity, through the prescribed parliamentary addresses and presidential order. Judicial disagreement is handled through legal remedies where available, not a cabinet confidence test. The separate voting majority question does not by itself test these substantive grounds.',
'ప్రకరణ 124(4) నిర్దేశిత పార్లమెంటు అభ్యర్థనలు, రాష్ట్రపతి ఉత్తర్వు ద్వారా నిరూపిత దుష్ప్రవర్తన లేదా అసమర్థతపై మాత్రమే తొలగింపును అనుమతిస్తుంది. న్యాయ నిర్ణయంతో విభేదాన్ని అందుబాటులోని న్యాయ పరిహారాల ద్వారా పరిష్కరించాలి; మంత్రివర్గ విశ్వాస పరీక్ష ద్వారా కాదు. వేరుగా ఉన్న ఓటింగ్ మెజారిటీ ప్రశ్న ఒక్కటే ఈ మూల ఆధారాలను పరీక్షించదు.',
'Option3 applies the two substantive grounds;1 invents a third ground,2 imports ministerial responsibility,4 ignores the constitutional procedure.',fmt='application')

add('original-private-party',293,'paragraphs30–31','Article131',
'Article131’s exclusive federal original jurisdiction requires the specified governments or States as parties and a question on which a legal right depends; a private company is not a qualifying governmental party.',
'ప్రకరణ 131లో ప్రత్యేక సమాఖ్య ప్రారంభ అధికార పరిధికి నిర్దేశిత ప్రభుత్వాలు లేదా రాష్ట్రాలు కక్షిదారులుగా ఉండాలి; చట్టపరమైన హక్కు ఆధారపడే ప్రశ్న ఉండాలి. వ్యక్తిగత కంపెనీ ఆ ప్రభుత్వ కక్షిదారు వర్గంలోకి రాదు.',
'A private company sues the Union over a contractual payment and invokes Article131 solely because the Union is a defendant. Which is correct?',
'ఒప్పంద చెల్లింపుపై వ్యక్తిగత కంపెనీ కేంద్రంపై దావా వేసి, కేంద్రం ప్రతివాది కాబట్టే ప్రకరణ 131ను ఆశ్రయించింది. సరైన వాక్యం ఏది?',
['Article131 necessarily applies whenever the Union is sued','The private company does not satisfy Article131’s specified-party requirement','Every Union contract dispute is an Article143 reference','Article131 covers only criminal prosecutions'],
['కేంద్రంపై దావా వేస్తే ప్రతి సందర్భంలో ప్రకరణ 131 తప్పనిసరిగా వర్తిస్తుంది','వ్యక్తిగత కంపెనీ ప్రకరణ 131లోని నిర్దేశిత కక్షిదారు షరతును నెరవేర్చదు','ప్రతి కేంద్ర ఒప్పంద వివాదం ప్రకరణ 143 సూచన అవుతుంది','ప్రకరణ 131 క్రిమినల్ ప్రాసిక్యూషన్లకు మాత్రమే వర్తిస్తుంది'],2,
'Article131 concerns the Union–State and inter-State party combinations specified in its text, involving a question of law or fact on which a legal right depends. The presence of the Union alone does not bring a private litigant into this exclusive original jurisdiction. This does not deny other lawful civil remedies.',
'ప్రకరణ 131 తన పాఠ్యంలో నిర్దేశించిన కేంద్ర–రాష్ట్ర, రాష్ట్రాల మధ్య కక్షిదారు సమూహాలకు, చట్టపరమైన హక్కు ఆధారపడే న్యాయ లేదా వాస్తవ ప్రశ్నకు వర్తిస్తుంది. కేంద్రం కక్షిదారుగా ఉండటమే వ్యక్తిగత కక్షిదారును ఈ ప్రత్యేక ప్రారంభ అధికార పరిధిలోకి తీసుకురాదు. దీనివల్ల ఇతర చట్టబద్ధమైన సివిల్ పరిహారాలు నిరాకరించబడవు.',
'Option2 identifies the failed party condition;1 ignores it,3 confuses advisory procedure and4 wrongly calls federal jurisdiction criminal.',fmt='application')

add('specialleave-character',294,'paragraphs36–37; table11','Article136(1), subject to clause(2)',
'Special leave is discretionary and can concern orders in any cause or matter from courts or tribunals within India, subject to the Armed Forces exception; it is not confined to final High Court judgments.',
'సాయుధ దళాల మినహాయింపుకు లోబడి భారతదేశంలోని కోర్టులు లేదా ట్రిబ్యునళ్ల ఏ వివాదం లేదా విషయంలోని ఉత్తర్వులపైనా ప్రత్యేక అనుమతి విచక్షణాత్మకంగా లభించవచ్చు; తుది హైకోర్టు తీర్పులకు మాత్రమే పరిమితం కాదు.',
'Which description of Article136 special leave is correct, subject to its military-court/tribunal exception?',
'సైనిక కోర్టు/ట్రిబ్యునల్ మినహాయింపుకు లోబడి ప్రకరణ 136 ప్రత్యేక అనుమతిని సరిగ్గా తెలిపేది ఏది?',
['An automatic appeal as of right in every case','A power confined to final High Court judgments in civil suits','An appeal available only after a presidential reference','A discretionary power that is not confined to final High Court judgments'],
['ప్రతి కేసులో హక్కుగా లభించే స్వయంచాలక అప్పీల్','సివిల్ దావాల్లో తుది హైకోర్టు తీర్పులకు మాత్రమే పరిమితమైన అధికారం','రాష్ట్రపతి సూచన తరువాత మాత్రమే లభించే అప్పీల్','తుది హైకోర్టు తీర్పులకు మాత్రమే పరిమితం కాని విచక్షణాత్మక అధికారం'],4,
'The Supreme Court may grant special leave; it is not bound to do so merely because a litigant applies. Its exceptional reach can include interlocutory orders and tribunals, rather than only final High Court judgments. Article136(2)’s Armed Forces exception remains, which is separately tested in the existing bank.',
'సుప్రీంకోర్టు ప్రత్యేక అనుమతి ఇవ్వవచ్చు; కక్షిదారు దరఖాస్తు చేసినంత మాత్రాన ఇవ్వాల్సిన బాధ్యత లేదు. దాని అసాధారణ పరిధిలో తుది హైకోర్టు తీర్పులే కాక మధ్యంతర ఉత్తర్వులు, ట్రిబ్యునళ్లు కూడా ఉండవచ్చు. ప్రకరణ 136(2)లో సాయుధ దళాల మినహాయింపు కొనసాగుతుంది; ఇప్పటికే ఉన్న బ్యాంకులో దానిని వేరుగా పరీక్షించారు.',
'Option4 captures discretion and reach;1 makes leave automatic,2 improperly narrows it,3 imports Article143.',fmt='single-best-answer')

add('enlargement-agreement',296,'paragraph48 (parliamentary-law condition supplied by Constitution)','Article138(2)',
'Further Supreme Court jurisdiction under Article138(2) needs a special Union–State agreement and parliamentary law providing for its exercise.',
'ప్రకరణ 138(2) కింద సుప్రీంకోర్టుకు మరింత అధికార పరిధి కల్పించడానికి ప్రత్యేక కేంద్ర–రాష్ట్ర ఒప్పందం, దాని వినియోగాన్ని కల్పించే పార్లమెంటు చట్టం అవసరం.',
'The Union and a State sign a special agreement conferring additional jurisdiction on the Supreme Court under Article138(2). What further condition does the Article require?',
'ప్రకరణ 138(2) కింద సుప్రీంకోర్టుకు అదనపు అధికార పరిధి ఇవ్వడానికి కేంద్రం, ఒక రాష్ట్రం ప్రత్యేక ఒప్పందం చేసుకున్నాయి. ఆ ప్రకరణ మరే షరతును కోరుతుంది?',
['Parliament must by law provide for exercise of that jurisdiction','Only the Governor’s private approval is needed','No further condition exists','Every State Assembly must ratify it as a constitutional amendment'],
['ఆ అధికార పరిధి వినియోగాన్ని పార్లమెంటు చట్టం ద్వారా కల్పించాలి','గవర్నర్ వ్యక్తిగత ఆమోదం మాత్రమే అవసరం','మరో షరతు లేదు','ప్రతి రాష్ట్ర శాసనసభ దానిని రాజ్యాంగ సవరణగా ఆమోదించాలి'],1,
'The agreement is not sufficient alone. Article138(2) expressly conditions the further jurisdiction on Parliament making law for its exercise. Clause(1) separately concerns further powers over Union List matters conferred by parliamentary law; neither clause is an automatic constitutional amendment.',
'ఒప్పందం ఒక్కటే సరిపోదు. మరింత అధికార పరిధి వినియోగానికి పార్లమెంటు చట్టం చేయాలని ప్రకరణ 138(2) స్పష్టమైన షరతు విధిస్తుంది. ఖండిక (1) వేరుగా కేంద్ర జాబితా విషయాలపై పార్లమెంటు చట్టంతో కల్పించే అదనపు అధికారాలకు సంబంధించినది; ఏ ఖండికా స్వయంచాలక రాజ్యాంగ సవరణ కాదు.',
'Option1 gives the missing express condition;2/3 omit Parliament and4 substitutes an inapplicable ratification route.',fmt='application')

add('common-question-withdrawal',296,'paragraph48 (precise conditions supplied by Constitution)','Article139A(1)',
'Article139A(1) permits withdrawal of cases with the same or substantially the same substantial questions of law of general importance pending before the Supreme Court and one or more High Courts, or before two or more High Courts.',
'సుప్రీంకోర్టు, ఒకటి లేదా అంతకంటే ఎక్కువ హైకోర్టుల్లో గానీ, రెండు లేదా అంతకంటే ఎక్కువ హైకోర్టుల్లో గానీ పెండింగ్‌లో ఉన్న కేసుల్లో సాధారణ ప్రాధాన్యం గల గంభీర న్యాయ ప్రశ్నలు ఒకేలా లేదా దాదాపు ఒకేలా ఉంటే ప్రకరణ 139A(1) కింద వాటిని ఉపసంహరించవచ్చు.',
'Cases before two High Courts involve substantially the same questions of law, which the Supreme Court finds to be substantial questions of general importance. Under Article139A(1), what may the Supreme Court do?',
'రెండు హైకోర్టుల కేసుల్లో దాదాపు ఒకే న్యాయ ప్రశ్నలు ఉన్నాయి; అవి సాధారణ ప్రాధాన్యం గల గంభీర ప్రశ్నలని సుప్రీంకోర్టు సంతృప్తి చెందింది. ప్రకరణ 139A(1) కింద సుప్రీంకోర్టు ఏమి చేయవచ్చు?',
['Dismiss both cases without determining the questions','Require a constitutional amendment before acting','Withdraw the cases and dispose of them itself, subject to the provision','Refer the cases to the Finance Commission'],
['ప్రశ్నలను నిర్ణయించకుండా రెండు కేసులనూ కొట్టివేయవచ్చు','వ్యవహరించే ముందు రాజ్యాంగ సవరణను కోరాలి','నిబంధనకు లోబడి కేసులను ఉపసంహరించి తానే పరిష్కరించవచ్చు','కేసులను ఆర్థిక సంఘానికి సూచించవచ్చు'],3,
'Article139A(1) provides withdrawal to the Supreme Court in the specified common-question situation. The Court may act on its own motion or the specified applications. After determining the questions of law, its proviso permits return of a withdrawn case to the High Court for disposal in conformity with that determination. Clause(2) separately provides inter-High-Court transfer for the ends of justice.',
'నిర్దేశిత ఉమ్మడి న్యాయ ప్రశ్నల సందర్భంలో ప్రకరణ 139A(1) కేసులను సుప్రీంకోర్టుకు ఉపసంహరించడానికి అనుమతిస్తుంది. కోర్టు స్వప్రేరణతో లేదా నిర్దేశిత దరఖాస్తులపై వ్యవహరించవచ్చు. న్యాయ ప్రశ్నలను నిర్ణయించిన తరువాత, ఆ నిర్ణయానికి అనుగుణంగా పరిష్కరించడానికి ఉపసంహరించిన కేసును హైకోర్టుకు తిరిగి పంపవచ్చని మినహాయింపు చెబుతుంది. ఖండిక (2) న్యాయ ప్రయోజనాల కోసం హైకోర్టుల మధ్య బదిలీకి వేరే ఏర్పాటు చేస్తుంది.',
'Option3 follows the specified conditions;1 denies lawful adjudication,2 ignores existing power,4 names a body without this judicial role.',fmt='application')

add('integrated-hierarchy',286,'paragraphs0–1; table0','Constitution PartsVandVI; appellate hierarchy',
'India’s integrated judiciary is a single hierarchy in which the same courts administer Union and State laws; this does not mean the Supreme Court appoints or administratively controls every subordinate judge.',
'భారత సమీకృత న్యాయవ్యవస్థలో ఒకే కోర్టు శ్రేణి కేంద్ర, రాష్ట్ర చట్టాలను అమలు చేస్తుంది; ప్రతి దిగువ న్యాయమూర్తిని సుప్రీంకోర్టే నియమిస్తుందని లేదా పరిపాలనాపరంగా నియంత్రిస్తుందని దీని అర్థం కాదు.',
'Which feature best expresses India’s integrated judicial system?',
'భారత సమీకృత న్యాయవ్యవస్థను ఉత్తమంగా తెలిపే లక్షణం ఏది?',
['Separate court hierarchies exclusively administer Union and State laws','Only the Supreme Court may apply Union laws','The same judicial hierarchy administers both Union and State laws','Every subordinate judge is appointed directly by the Supreme Court'],
['వేర్వేరు కోర్టు శ్రేణులు కేంద్ర, రాష్ట్ర చట్టాలను విడివిడిగా మాత్రమే అమలు చేస్తాయి','సుప్రీంకోర్టు మాత్రమే కేంద్ర చట్టాలను అమలు చేయవచ్చు','ఒకే న్యాయస్థాన శ్రేణి కేంద్ర, రాష్ట్ర చట్టాలను రెండింటినీ అమలు చేస్తుంది','ప్రతి దిగువ న్యాయమూర్తిని సుప్రీంకోర్టు నేరుగా నియమిస్తుంది'],3,
'An integrated hierarchy supplies courts that apply both Union and State law, with the Supreme Court at the apex. It differs from a dual system of separate federal and State court hierarchies. Administrative control and appointments remain allocated by specific provisions, including Articles233–235 and High Court powers; integration is not blanket Supreme Court administrative superintendence.',
'సమీకృత శ్రేణిలో కోర్టులు కేంద్ర, రాష్ట్ర చట్టాలను రెండింటినీ అమలు చేస్తాయి; అగ్రస్థానంలో సుప్రీంకోర్టు ఉంటుంది. ఇది వేర్వేరు సమాఖ్య, రాష్ట్ర కోర్టు శ్రేణుల ద్వంద్వ వ్యవస్థకు భిన్నం. పరిపాలనా నియంత్రణ, నియామకాలు ప్రకరణలు 233–235, హైకోర్టు అధికారాలు సహా నిర్దిష్ట నిబంధనల ప్రకారమే ఉంటాయి; సమీకరణ అంటే సుప్రీంకోర్టుకు సర్వవ్యాప్త పరిపాలనా పర్యవేక్షణ కాదు.',
'Option3states the integrated law-administering hierarchy;1describes duality,2excludes competent other courts,4confuses integration with appointment control.')

add('adhoc-priority',288,'paragraph21','Article127(2)',
'A High Court judge requested to attend as an ad hoc Supreme Court judge must attend in priority to the other duties of the High Court office.',
'సుప్రీంకోర్టు తాత్కాలిక న్యాయమూర్తిగా హాజరు కావాలని కోరిన హైకోర్టు న్యాయమూర్తి, తన హైకోర్టు పదవిలోని ఇతర విధుల కంటే ఆ హాజరుకు ప్రాధాన్యం ఇవ్వాలి.',
'A High Court judge validly requested to attend the Supreme Court under Article127has a conflicting High Court assignment. What rule does Article127(2) prescribe?',
'ప్రకరణ 127 కింద చట్టబద్ధంగా సుప్రీంకోర్టుకు హాజరు కావాలని కోరిన హైకోర్టు న్యాయమూర్తికి అదే సమయంలో హైకోర్టు పని ఉంది. ప్రకరణ 127(2) ఏ నియమాన్ని నిర్దేశిస్తుంది?',
['Supreme Court attendance has priority over the other duties of that office','The High Court assignment must always prevail','Attendance is optional even after the constitutional request','The judge loses all judicial powers while attending'],
['ఆ పదవిలోని ఇతర విధుల కంటే సుప్రీంకోర్టు హాజరుకు ప్రాధాన్యం ఉంటుంది','హైకోర్టు పనికే ఎల్లప్పుడూ ప్రాధాన్యం ఇవ్వాలి','రాజ్యాంగబద్ధమైన అభ్యర్థన తరువాత కూడా హాజరు పూర్తిగా ఐచ్ఛికం','హాజరైనప్పుడు న్యాయమూర్తి న్యాయ అధికారాలన్నీ కోల్పోతారు'],1,
'Article127(2) makes attendance the judge’s duty in priority to the other duties of office. During the attendance the judge enjoys Supreme Court jurisdiction, powers and privileges and discharges its judicial duties. This priority follows a valid Article127request; it is not a general executive direction to a High Court judge.',
'ప్రకరణ 127(2) ఆ పదవిలోని ఇతర విధుల కంటే హాజరుకు ప్రాధాన్యం ఇవ్వడాన్ని న్యాయమూర్తి విధిగా నిర్దేశిస్తుంది. హాజరు సమయంలో సుప్రీంకోర్టు అధికార పరిధి, అధికారాలు, ప్రత్యేక హక్కులు కలిగి న్యాయ విధులు నిర్వహిస్తారు. ఈ ప్రాధాన్యం చెల్లుబాటయ్యే ప్రకరణ 127 అభ్యర్థన తరువాత వర్తిస్తుంది; హైకోర్టు న్యాయమూర్తికి సాధారణ కార్యనిర్వాహక ఆదేశం కాదు.',
'Option1follows the express priority rule;2reverses it,3denies the duty and4denies the express judicial powers.',fmt='application')

add('age-determination-law',290,'no corresponding rule in preparedCh26','Article124(2A)',
'Article124(2A) permits Parliament by law to provide the authority and manner for determining a Supreme Court judge’s age.',
'సుప్రీంకోర్టు న్యాయమూర్తి వయస్సును నిర్ణయించే అధికారి, విధానాన్ని పార్లమెంటు చట్టం ద్వారా కల్పించవచ్చని ప్రకరణ 124(2A) చెబుతుంది.',
'Under Article124(2A), who may by law provide the authority and manner for determining a Supreme Court judge’s age?',
'ప్రకరణ 124(2A) ప్రకారం సుప్రీంకోర్టు న్యాయమూర్తి వయస్సును నిర్ణయించే అధికారి, విధానాన్ని చట్టం ద్వారా ఎవరు కల్పించవచ్చు?',
['The Governor','The CJI by a personal administrative direction alone','The State Legislature','Parliament'],
['గవర్నర్','వ్యక్తిగత పరిపాలనా ఆదేశం ద్వారా ప్రధాన న్యాయమూర్తి మాత్రమే','రాష్ట్ర శాసనసభ','పార్లమెంటు'],4,
'Article124(2A) uses an enabling parliamentary-law formula. The question asks who may provide the mechanism, not whether Parliament has enacted a particular current mechanism or how a particular dispute was resolved. It must not be confused with Article217(3)’s distinct High Court age-dispute rule.',
'ప్రకరణ 124(2A) పార్లమెంటు చట్టం ద్వారా ఏర్పాటు చేసే అవకాశాన్ని కల్పిస్తుంది. ప్రశ్న ఆ విధానాన్ని ఎవరు కల్పించవచ్చనే దాని గురించే; ప్రస్తుతానికి నిర్దిష్ట చట్టం చేశారా లేదా ఒక వివాదం ఎలా పరిష్కరించారనే దాని గురించి కాదు. దీనిని ప్రకరణ 217(3)లోని హైకోర్టు వయస్సు వివాదానికి వేరు నియమంతో కలపకూడదు.',
'Option4is the express law-making authority;1imports a State office,2substitutes personal direction and3substitutes the wrong legislature.')

add('union-list-enlargement',296,'paragraph48','Article138(1)',
'Parliament may by law confer further Supreme Court jurisdiction and powers regarding Union List matters under Article138(1).',
'ప్రకరణ 138(1) కింద కేంద్ర జాబితా విషయాలపై సుప్రీంకోర్టుకు అదనపు అధికార పరిధి, అధికారాలను పార్లమెంటు చట్టం ద్వారా కల్పించవచ్చు.',
'Parliament proposes to confer further Supreme Court jurisdiction regarding a Union List matter. Which constitutional route directly supports this?',
'కేంద్ర జాబితా విషయంపై సుప్రీంకోర్టుకు అదనపు అధికార పరిధి కల్పించాలని పార్లమెంటు ప్రతిపాదించింది. దీనికి నేరుగా ఆధారమయ్యే రాజ్యాంగ మార్గం ఏది?',
['A unilateral State executive order under Article162','Parliamentary law under Article138(1)','Only a presidential advisory reference under Article143','Only an informal agreement of all High Courts'],
['ప్రకరణ 162 కింద రాష్ట్ర కార్యనిర్వాహక శాఖ ఏకపక్ష ఉత్తర్వు','ప్రకరణ 138(1) కింద పార్లమెంటు చట్టం','ప్రకరణ 143 కింద రాష్ట్రపతి సలహా సూచన మాత్రమే','అన్ని హైకోర్టుల అనధికారిక ఒప్పందం మాత్రమే'],2,
'Article138(1) expressly permits parliamentary law to confer further jurisdiction and powers over Union List matters. Article143 obtains advice rather than conferring this jurisdiction. Article138(2) is a separate special Union–State agreement route, itself requiring a parliamentary-law provision for exercise.',
'ప్రకరణ 138(1) కేంద్ర జాబితా విషయాలపై అదనపు అధికార పరిధి, అధికారాలను పార్లమెంటు చట్టం కల్పించవచ్చని స్పష్టంగా చెబుతుంది. ప్రకరణ 143 ఈ అధికార పరిధిని కల్పించదు; సలహా పొందే ఏర్పాటు. ప్రకరణ 138(2) ప్రత్యేక కేంద్ర–రాష్ట్ర ఒప్పందానికి వేరు మార్గం; దాని వినియోగానికి కూడా పార్లమెంటు చట్ట నిబంధన అవసరం.',
'Option2is the express power;1and4lack the constitutional actor/method and3confuses advisory jurisdiction.',fmt='application')

add('staff-financial-rules',297,'Independence safeguard8; primary supplies approval distinction','Article146(2) proviso',
'Rules under Article146(2), insofar as they concern Supreme Court staff salaries, allowances, leave or pensions, require the President’s approval.',
'ప్రకరణ 146(2) కింద సుప్రీంకోర్టు సిబ్బంది జీతాలు, భత్యాలు, సెలవులు లేదా పెన్షన్లకు సంబంధించిన మేరకు నియమాలకు రాష్ట్రపతి ఆమోదం అవసరం.',
'The authorised rule-maker frames Supreme Court staff rules concerning leave and pensions under Article146(2). Which approval does its proviso require?',
'ప్రకరణ 146(2) కింద అధీకృత నియమకర్త సుప్రీంకోర్టు సిబ్బంది సెలవులు, పెన్షన్లపై నియమాలు రూపొందించారు. దాని మినహాయింపు ఏ ఆమోదాన్ని కోరుతుంది?',
['Approval of the Governor','Approval of the Lok Sabha Speaker','Approval of the President','No approval because all staff rules are entirely exempt'],
['గవర్నర్ ఆమోదం','లోక్‌సభ స్పీకర్ ఆమోదం','రాష్ట్రపతి ఆమోదం','సిబ్బంది నియమాలన్నింటికీ పూర్తిగా మినహాయింపు ఉన్నందున ఆమోదం అవసరం లేదు'],3,
'The Article146(2) proviso expressly identifies salaries, allowances, leave and pensions for presidential approval. The general staff-service rule-making power is subject to parliamentary law. This question tests the financial/leave-pension approval check, distinct from who appoints staff under clause(1) or which fund bears expenses under clause(3).',
'ప్రకరణ 146(2) మినహాయింపు రాష్ట్రపతి ఆమోదానికి జీతాలు, భత్యాలు, సెలవులు, పెన్షన్లను స్పష్టంగా గుర్తిస్తుంది. సాధారణ సిబ్బంది సేవా నియమాల రూపకల్పన పార్లమెంటు చట్టానికి లోబడి ఉంటుంది. ఈ ప్రశ్న ఆర్థిక/సెలవు–పెన్షన్ ఆమోద నియంత్రణను పరీక్షిస్తుంది; ఖండిక (1)లో సిబ్బందిని ఎవరు నియమిస్తారు, ఖండిక (3)లో వ్యయాలు ఏ నిధిపై భారితమవుతాయనే వాటికి ఇది భిన్నం.',
'Option3is the express approval;1and2substitute other constitutional offices and4erases the proviso.',fmt='application')

def load(name): return json.loads((P/name).read_text(encoding='utf-8-sig'))
def save(name,obj): (P/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
q=load('Questions.json'); f=load('Fact-register.json'); e=load('Explanations.json')
review=[]
for r in rows:
    if r['slug']=='family-appeal-boundary':
        r['qe']='Under section 19(1) and (2) of the Family Courts Act, which ordinarily admits an appeal to the High Court? 1. A contested final non-interlocutory judgment in a civil spousal-property dispute. 2. A valid consent decree. 3. An interlocutory order.'
        r['qt']='కుటుంబ న్యాయస్థానాల చట్టంలోని సెక్షన్ 19(1), (2) ప్రకారం సాధారణంగా దేనిపై హైకోర్టుకు అప్పీల్ చేయవచ్చు? 1. భార్యాభర్తల ఆస్తికి సంబంధించిన సివిల్ వివాదంలో, మధ్యంతరమైనది కాని, వాదోపవాదాల తరువాత ఇచ్చిన తుది తీర్పు. 2. చెల్లుబాటయ్యే సమ్మతి డిక్రీ. 3. మధ్యంతర ఉత్తర్వు.'
        r['oe']=['1and2only','2and3only','1only','1,2and3']
        r['ot']=['1, 2 మాత్రమే','2, 3 మాత్రమే','1 మాత్రమే','1, 2, 3']
        r['fmt']='statement-combination'
        r['why']='Only item1 is within the ordinary section19appeal route on the stated facts. Item2 is a valid consent decree excluded by subsection2; item3 is interlocutory and excluded by subsection1. Therefore option3 is correct; the other combinations include one or both barred categories.'
    if r['slug']=='administrative-charge':
        r['fen']='Supreme Court administrative expenses, including staff salaries, allowances and pensions, are charged upon the Consolidated Fund of India.'
        r['fte']='సిబ్బంది జీతాలు, భత్యాలు, పెన్షన్లు సహా సుప్రీంకోర్టు పరిపాలనా వ్యయాలు భారత సంచిత నిధిపై భారితమవుతాయి.'
    if r['slug']=='retired-attendance':
        r['fen']='Attendance by a retired judge requested under Article128 requires previous presidential consent and that person’s consent; it is not an automatic fresh permanent appointment.'
        r['fte']='ప్రకరణ 128 కింద కోరిన పదవీ విరమణ చేసిన న్యాయమూర్తి హాజరుకు రాష్ట్రపతి ముందస్తు సమ్మతి, ఆ వ్యక్తి సమ్మతి అవసరం; అది స్వయంచాలక కొత్త శాశ్వత నియామకం కాదు.'
    if r['slug']=='no-minimum-age':r['qt']='పౌరసత్వం, వృత్తిపరమైన అర్హతలతో పాటు సుప్రీంకోర్టు న్యాయమూర్తి నియామకానికి ప్రకరణ 124(3) ఏ కనీస వయస్సును నిర్దేశిస్తుంది?'
    if r['slug']=='original-private-party':
        for field in ('fte','qt','et'):r[field]=r[field].replace('వ్యక్తిగత కంపెనీ','ప్రైవేటు కంపెనీ')
        r['ot']=[x.replace('వ్యక్తిగత కంపెనీ','ప్రైవేటు కంపెనీ') for x in r['ot']]
    if r['slug']=='acting-cji':
        r['oe']=['The senior-most Supreme Court judge assumes the duties without a presidential appointment','The President appoints any serving High Court judge without first appointing that person to the Supreme Court','The full Supreme Court alone elects an acting CJI','The President appoints another Supreme Court judge to perform the duties']
        r['ot']=['రాష్ట్రపతి నియామకం లేకుండానే అత్యంత సీనియర్ సుప్రీంకోర్టు న్యాయమూర్తి విధులు చేపడతారు','ముందుగా సుప్రీంకోర్టుకు నియమించకుండానే ఏ సిట్టింగ్ హైకోర్టు న్యాయమూర్తినైనా రాష్ట్రపతి నియమిస్తారు','పూర్తి సుప్రీంకోర్టు ఒక్కటే తాత్కాలిక ప్రధాన న్యాయమూర్తిని ఎన్నుకుంటుంది','ఆ విధులు నిర్వహించడానికి రాష్ట్రపతి మరో సుప్రీంకోర్టు న్యాయమూర్తిని నియమిస్తారు']
        r['why']='Option 4 has the correct presidential appointment and Supreme Court-judge eligibility. Option 1 omits appointment, 2 substitutes a judge not yet on the Supreme Court, and 3 invents election by the Court.'
    if r['slug']=='inquiry-committee':
        r['oe']=['A CJI/other Supreme Court judge, a High Court Chief Justice and a distinguished jurist','The CJI and the two senior-most Supreme Court judges','The Speaker, Union Law Minister and Attorney-General','A High Court Chief Justice and two Members of Parliament']
        r['ot']=['ప్రధాన న్యాయమూర్తి/మరో సుప్రీంకోర్టు న్యాయమూర్తి, ఒక హైకోర్టు ప్రధాన న్యాయమూర్తి, ఒక విశిష్ట న్యాయవేత్త','ప్రధాన న్యాయమూర్తి, అత్యంత సీనియర్ ఇద్దరు సుప్రీంకోర్టు న్యాయమూర్తులు','స్పీకర్, కేంద్ర న్యాయశాఖ మంత్రి, అటార్నీ జనరల్','ఒక హైకోర్టు ప్రధాన న్యాయమూర్తి, ఇద్దరు పార్లమెంటు సభ్యులు']
        r['why']='Option 1 matches all three statutory categories. Option 2 confuses an all-Supreme-Court grouping with the inquiry committee; 3 and 4 substitute political or law officers for mandatory judicial/jurist categories.'
    if r['slug']=='staff-appointment':
        r['oe']=['The CJI, or another judge or officer directed by the CJI','The Union Law Minister on the Attorney-General’s recommendation','The President in every case, without any role for the CJI','The UPSC alone for every staff post']
        r['ot']=['ప్రధాన న్యాయమూర్తి లేదా ఆయన ఆదేశించిన మరో న్యాయమూర్తి లేదా అధికారి','అటార్నీ జనరల్ సిఫారసుపై కేంద్ర న్యాయశాఖ మంత్రి','ప్రధాన న్యాయమూర్తికి పాత్ర లేకుండా ప్రతి సందర్భంలో రాష్ట్రపతి','ప్రతి సిబ్బంది పదవికి యూపీఎస్సీ మాత్రమే']
        r['why']='Option 1 states the constitutional CJI/delegation mechanism. Option 2 invents ministerial appointment, 3 removes the CJI, and 4 turns the qualified consultation proviso into universal UPSC appointment.'
    if r['slug']=='original-private-party':
        r['oe'][3]='Article131 becomes available only after the company first appeals from a High Court'
        r['ot'][3]='కంపెనీ ముందుగా హైకోర్టు నుంచి అప్పీల్ చేసిన తరువాత మాత్రమే ప్రకరణ 131 అందుబాటులోకి వస్తుంది'
        r['why']='Option 2 identifies the failed party condition; 1 ignores it, 3 confuses advisory procedure and 4 wrongly turns original jurisdiction into an appellate route.'
    if r['slug']=='common-question-withdrawal':
        r['oe']=['Automatically quash both proceedings without deciding the questions','Transfer them only if every State Government consents','Withdraw the cases and dispose of them itself, subject to the provision','Direct each High Court to disregard the other case and prohibit withdrawal']
        r['ot']=['ప్రశ్నలను నిర్ణయించకుండానే రెండు విచారణలనూ స్వయంచాలకంగా రద్దు చేయవచ్చు','ప్రతి రాష్ట్ర ప్రభుత్వం సమ్మతిస్తే మాత్రమే వాటిని బదిలీ చేయవచ్చు','నిబంధనకు లోబడి కేసులను ఉపసంహరించి తానే పరిష్కరించవచ్చు','ప్రతి హైకోర్టు మరో కేసును పట్టించుకోకూడదని ఆదేశించి ఉపసంహరణను నిషేధించవచ్చు']
        r['why']='Option 3 follows the express common-question withdrawal power. Option 1 invents automatic quashing, 2 invents universal State consent, and 4 denies the statutory coordination mechanism.'
    for field in ('fen','qe','ee','why'):
        r[field]=re.sub(r'(?<=[A-Za-z])(?=\d)|(?<=\d)(?=[A-Za-z])',' ',r[field])
        r[field]=re.sub(r'(\d) ([A-Z])\b',r'\1\2',r[field])
        r[field]=re.sub(r'([?:.])(?=\d)',r'\1 ',r[field])
        r[field]=re.sub(r'(?<=\d)\.(?=[A-Za-z])','. ',r[field])
    r['oe']=[re.sub(r'(?<=[A-Za-z])(?=\d)|(?<=\d)(?=[A-Za-z])',' ',x) for x in r['oe']]
    r['oe']=[re.sub(r'(\d) ([A-Z])\b',r'\1\2',x) for x in r['oe']]
    if r['slug']=='staff-appointment':r['lax']='Independence numbered safeguard8, Freedom to Appoint its Staff; table9'
    if r['slug']=='administrative-charge':r['lax']='Independence numbered safeguard4, Expenses Charged on Consolidated Fund; table9'
    if r['slug']=='parliament-conduct':r['lax']='Independence numbered safeguard5, Conduct of Judges Cannot be Discussed'
    if r['slug']=='family-establishment':r['why']='Both statements are express statutory conditions; each single-statement option drops another correct condition.'
    if r['slug']=='family-settlement':r['why']='Option 1 preserves both the settlement endeavour and the circumstances qualification; option 2 coerces, 3 denies adjudication and 4 invents mandatory transfer.'
    if r['slug']=='family-representation':r['why']='Option 4 preserves the qualification and proviso; option 1 creates an unconditional right, 2 denies expressly permitted assistance and 3 inverts the access rule.'
    fid='POL-741-'+r['slug']; qid='POL-741-AT-'+r['slug']
    fact=dict(id=fid,fact_en=r['fen'],fact_te=r['fte'],sources=[f"GBK p{r['page']}",f"Prepared Laxmikanth Ch26 {r['lax']}",r['primary']+' | '+r['article']],status='validated_atomic_manual_review',gbk_locator={'file':f"gbk-p{r['page']}-transcription.html",'printed_page':r['page']},laxmikanth_match={'classification':'direct','locator':r['lax'],'qualification':'Supplied prepared chapter, not certified publisher facsimile.'},primary_authority={'url':r['primary'],'locator':r['article']},question_ids=[qid])
    fact['source_exactness_certified']=False
    fact['study_validation']='Supplied prepared reader checked first; primary constitutional/statutory or official judicial evidence qualifies the academic claim.'
    if r['slug'] in ('retired-attendance','constitutional-appeal','staff-appointment','enlargement-agreement','common-question-withdrawal'):
        fact['gbk_locator']['classification']='partial'
        fact['gbk_locator']['qualification']='Saved GBK text supports the topic/core rule; precise consent, cross-reference or conditions in this academic claim are supplemented from the reader and primary authority, not invented into the transcription.'
    item=dict(id=qid,kind='original-pagewise',source_page=r['page'],fact_ids=[fid],format=r['fmt'],difficulty='moderate',question_en=r['qe'],question_te=r['qt'],options_en=r['oe'],options_te=r['ot'],answer=r['key'],explanation_id=qid,status='approved_manual_atomic_review',source_type='original-authored-not-PYQ',primary_fact_chapter='7.4.1')
    exp=dict(en=r['ee'],te=r['et'],fact_ids=[fid],references=[{'url':r['primary'],'locator':r['article']}, {'source':'Prepared Laxmikanth Chapter26','locator':r['lax']}])
    if r['slug'] in ('staff-appointment','staff-financial-rules','constitutional-appeal','enlargement-agreement','common-question-withdrawal','oath-authority'):
        fact['laxmikanth_match']['classification']='partial'
        fact['laxmikanth_match']['qualification']='Supplied reader supports the core rule; precise constitutional cross-reference, delegation, schedule or cumulative conditions are supplied by the cited primary provision.'
    if r['slug']=='age-determination-law':
        fact['laxmikanth_match']={'classification':'absent','locator':'Prepared Ch26','qualification':'The supplied chapter gives no corresponding age-determination mechanism; the narrow enabling rule is verified directly from Article124(2A), without asserting enactment of any current implementing law.'}
    if r['slug'].startswith(('gram-','family-')):
        fact['sources'][1]='Prepared Laxmikanth '+r['lax']
        fact['laxmikanth_match']={'classification':'absent','locator':'Prepared Ch26','supplement':{'chapter':38,'classification':'partial' if r['slug'] in ('gram-commencement','family-appeal-boundary') else 'direct','locator':r['lax']},'qualification':'Ch26 alone does not cover these courts; supplied Ch38 consulted first, then primary statute. Commencement and appeal exclusions require the cited primary evidence.'}
        exp['references'][1]={'source':'Prepared Laxmikanth Chapter38','locator':r['lax']}
        if r['slug'] in ('gram-appointment','family-establishment'):fact['gbk_locator']['qualification']='Core topic present; precise statutory categories and population/eligibility conditions supplemented from prepared Ch38 and primary Act.'
    if r['slug']=='open-majority-dissent':
        fact['sources']=[x for x in fact['sources'] if not x.startswith('GBK')]
        fact['gbk_locator']={'classification':'absent','qualification':'Related Article145 discussion at p297 does not state these clauses; this is an independently supported prepared-reader addition.'}
        item['source_page']=None
        item['kind']='original-supplied-reader'
    f['facts']=[x for x in f['facts'] if x['id']!=fid]+[fact]
    q['questions']=[x for x in q['questions'] if x['id']!=qid]+[item]
    e['explanations'][qid]=exp
    review.append({'question_id':qid,'independently_solved_answer':r['key'],'solution_and_distractor_check':r['why'],'bilingual_check':'Manually compared stem, four options, quantifiers and explanation; Telugu uses matching constitutional actors and conditions.','tested_claim':fid,'dedup_review':'All current Questions.json stems searched across g2, including Unit6; no compatible existing standalone question on this precise target found. Existing broader article-identification questions were not counted as coverage of this target.','review_result':'approved','source_exactness_certified':False})
    review[-1]['dedup_review']='All current g2 Questions.json stems and options searched, including read-only Unit6 files; actual tested target compared, with broader article-identification or explanation-only coverage excluded.'
    if r['slug']=='curative-boundary':review[-1]['related_but_distinct']={'chapter':'6.4.1','id':'POL-6.1.9-P93-06','reason':'Canonical item tests why a fresh Article32 petition cannot attack a final SCjudgment; this item instead tests the exceptional/nonautomatic nature of curative jurisdiction. Curative facts merely mentioned in an explanation would not count as assessed.'}
    if r['slug'] in ('rules-approval','staff-appointment','staff-financial-rules'):
        review[-1]['related_but_distinct']={'chapter':'6.4.1','id':'POL-6.1.9-P93-07','reason':'Existing matching item tests only rules–Article145 and staff–Article146 associations. It does not assess presidential approval, CJI/delegation or the financial/leave-pension approval proviso tested by this new item.'}
q['status']='manual_atomic_expansion_reviewed_existing_ids_retained_coverage_incomplete'
q['full_chapter_coverage']=False
f['full_chapter_coverage']=False
save('Questions.json',q);save('Fact-register.json',f);save('Explanations.json',e)
save('atomic-question-review.json',{'chapter':'7.4.1','method':'Manual solution and option exclusion for each authored item; structural validation is supplementary.','new_approved_count':len(rows),'reviews':review,'existing_question_ids_preserved':True,'source_exactness_certified':False,'full_chapter_coverage':False})
print('Authored',len(rows),'distinct questions; current local bank',len(q['questions']))
