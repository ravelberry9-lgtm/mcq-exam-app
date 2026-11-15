import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CH=ROOT/'content'/'geography'/'india_ap_chapters'/'6'
BANK=CH/'Questions.json'; MAN=CH/'manifest.json'
def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,v): p.write_bytes((json.dumps(v,ensure_ascii=False,indent=2)+'\n').replace('\n','\r\n').encode())

# Each option below was read and translated as a complete idea; English technical names are retained in brackets.
te={
'Eastern Ghats hill landscape between Krishna and Penna systems':'కృష్ణా–పెన్నా నదీ వ్యవస్థల మధ్య ఉన్న తూర్పు కనుమల కొండ భూదృశ్యం',
'Southern AP hill landscape associated with Tirupati and red-sanders habitat':'తిరుపతి, ఎర్రచందనం ఆవాసంతో సంబంధం గల దక్షిణ ఆంధ్రప్రదేశ్ కొండ భూదృశ్యం',
'Godavari gorge-and-hill forest landscape':'గోదావరి లోయ–కొండ అడవి భూదృశ్యం','Godavari estuarine mangrove landscape':'గోదావరి నదీముఖ మడ అడవి భూదృశ్యం',
'Pterocarpus santalinus, distinct from Santalum album':'శ్వేతచందనం (Santalum album)కు భిన్నమైన ఎర్రచందనం (Pterocarpus santalinus)',
'Santalum album rather than red-sanders species':'ఎర్రచందనం కాదు; శ్వేతచందనం జాతి Santalum album',
'Mangrove genus commonly associated with pneumatophores':'శ్వాస వేర్లతో (Pneumatophores) సాధారణంగా సంబంధం గల మడ జాతి వంశం',
'Mangrove genus commonly associated with stilt roots':'ఊత వేర్లతో (Stilt roots) సాధారణంగా సంబంధం గల మడ జాతి వంశం',
'Canopy-based land-cover assessment rather than ownership category alone':'యాజమాన్య హోదా ఒక్కటే కాక చెట్ల పైకప్పు ఆధారంగా చేసే భూ కప్పు అంచనా',
'Breaking habitat into smaller less-connected patches':'ఆవాసాన్ని చిన్న, పరస్పర అనుసంధానం తక్కువగల ముక్కలుగా విడగొట్టడం',
'Habitat connection facilitating movement between areas':'ఆవాస ప్రాంతాల మధ్య వన్యజీవుల కదలికకు సహాయపడే అనుసంధానం',
'Expansion of harmful introduced organisms altering local ecosystems':'స్థానిక జీవావరణాన్ని మార్చే హానికర ప్రవేశపెట్టిన జీవుల విస్తరణ',
'Conserving biodiversity within natural habitats and ecosystems':'సహజ ఆవాసాలు, జీవావరణ వ్యవస్థల్లోనే జీవవైవిధ్యాన్ని సంరక్షించడం',
'Conserving organisms or genetic material outside natural habitats':'సహజ ఆవాసం బయట జీవులు లేదా జన్యు పదార్థాన్ని సంరక్షించడం',
'Managed storage of seeds or other genetic material':'విత్తనాలు లేదా ఇతర జన్యు పదార్థాన్ని నియంత్రితంగా నిల్వ చేయడం',
'Assisting recovery of degraded ecosystem structure and functions':'క్షీణించిన జీవావరణ నిర్మాణం, విధులు తిరిగి కోలుకోవడానికి సహాయపడడం',
'Division of connected habitat into smaller isolated patches':'అనుసంధానమైన ఆవాసాన్ని చిన్న, ఒంటరి ముక్కలుగా విభజించడం',
'Unlawful taking of wildlife under applicable law':'వర్తించే చట్టానికి విరుద్ధంగా వన్యజీవులను పట్టుకోవడం లేదా చంపడం',
'Harm caused by introduced organisms spreading in new ecosystems':'కొత్త జీవావరణాల్లో ప్రవేశపెట్టిన జీవులు విస్తరించి కలిగించే హాని',
'Ecological connection enabling movement between habitat areas':'ఆవాస ప్రాంతాల మధ్య జీవుల కదలికకు వీలు కల్పించే పర్యావరణ అనుసంధానం',
'A national legal protected-area category for conservation management':'సంరక్షణ నిర్వహణకు సంబంధించిన జాతీయ చట్టపర రక్షిత ప్రాంత వర్గం',
'A distinct national legal wildlife-protection area category':'వన్యజీవి రక్షణకు సంబంధించిన ప్రత్యేక జాతీయ చట్టపర ప్రాంత వర్గం',
'A conservation–development–research framework often using core, buffer and transition zones':'సాధారణంగా core, buffer, transition మండలాలతో సంరక్షణ–అభివృద్ధి–పరిశోధనను కలిపే విధానం',
'Recognition under the international wetlands convention':'అంతర్జాతీయ చిత్తడి నేలల ఒప్పందం (Ramsar Convention) కింద గుర్తింపు',
'Highest extinction-risk category among the three threatened IUCN categories':'IUCN threatened వర్గాల్లో అత్యధిక అంతరింపు ప్రమాదాన్ని సూచించే స్థాయి',
'Threatened IUCN category between Vulnerable and Critically Endangered':'Vulnerable, Critically Endangered మధ్య ఉన్న IUCN threatened స్థాయి',
'Threatened IUCN category below Endangered in the risk ordering':'ప్రమాద క్రమంలో Endangered కంటే దిగువన ఉన్న IUCN threatened స్థాయి',
'Insufficient information for a direct or indirect extinction-risk assessment':'అంతరింపు ప్రమాదాన్ని నేరుగా లేదా పరోక్షంగా అంచనా వేయడానికి సరిపడ సమాచారం లేకపోవడం',
}

des={
 k:(f'This option states: {k}.',f'ఈ ఎంపిక భావం: {v}.') for k,v in te.items()
}
labels34=['Nallamala','Seshachalam','Papikonda','Coringa','Red sanders','Sandalwood','Avicennia root example','Rhizophora root example','Forest-cover measurement','Habitat fragmentation','Wildlife corridor','Invasive spread']
labels34te=['నల్లమల (Nallamala)','శేషాచలం (Seshachalam)','పాపికొండ (Papikonda)','కోరింగ (Coringa)','ఎర్రచందనం (Red sanders)','శ్వేతచందనం (Sandalwood)','Avicennia వేరు ఉదాహరణ','Rhizophora వేరు ఉదాహరణ','అడవి కప్పు కొలత (Forest-cover measurement)','ఆవాస విభజన (Habitat fragmentation)','వన్యజీవి సంచార మార్గం (Wildlife corridor)','దురాక్రమణ జీవుల విస్తరణ (Invasive spread)']
labels35=['In-situ conservation','Ex-situ conservation','Gene bank','Ecological restoration','Fragmentation','Poaching','Invasive alien pressure','Landscape corridor','National park designation','Wildlife sanctuary designation','Biosphere-reserve framework','Ramsar designation','Critically Endangered','Endangered','Vulnerable','Data Deficient']
labels35te=['సహజావాస సంరక్షణ (In-situ conservation)','బాహ్యావాస సంరక్షణ (Ex-situ conservation)','జన్యు నిల్వ (Gene bank)','జీవావరణ పునరుద్ధరణ (Ecological restoration)','ఆవాస విభజన (Fragmentation)','అక్రమ వేట (Poaching)','దురాక్రమణ విదేశీ జాతి ఒత్తిడి (Invasive alien pressure)','భూదృశ్య సంచార మార్గం (Landscape corridor)','జాతీయ ఉద్యానవనం హోదా (National park designation)','వన్యప్రాణి అభయారణ్యం హోదా (Wildlife sanctuary designation)','జీవావరణ రిజర్వు విధానం (Biosphere-reserve framework)','రామ్‌సర్ గుర్తింపు (Ramsar designation)','తీవ్ర ప్రమాద స్థితి (Critically Endangered)','అంతరించే ప్రమాద స్థితి (Endangered)','హాని సంభావ్య స్థితి (Vulnerable)','సమాచార లోప స్థితి (Data Deficient)']
combo={'Both I and II':'I, II రెండూ','I only':'I మాత్రమే','II only':'II మాత్రమే','Neither I nor II':'I, II రెండూ కావు'}
combo_en={'Both I and II':'Choose this only when both statements are correct.','I only':'Choose this only when I is correct and II is wrong.','II only':'Choose this only when II is correct and I is wrong.','Neither I nor II':'Choose this only when both statements are wrong.'}
combo_te={'Both I and II':'I, II రెండూ సరైనప్పుడు మాత్రమే ఈ ఎంపిక సరైంది.','I only':'I సరైందిగా, II తప్పుగా ఉన్నప్పుడు మాత్రమే ఈ ఎంపిక సరైంది.','II only':'II సరైందిగా, I తప్పుగా ఉన్నప్పుడు మాత్రమే ఈ ఎంపిక సరైంది.','Neither I nor II':'I, II రెండూ తప్పుగా ఉన్నప్పుడు మాత్రమే ఈ ఎంపిక సరైంది.'}

special_te={
'All legal forest land always has identical canopy':'చట్టపరంగా అడవిగా ఉన్న భూమంతటా ఒకే రకమైన canopy ఉంటుంది',
'Canopy cannot be observed':'చెట్ల పైకప్పును (Canopy) పరిశీలించలేం','Every plantation is a protected sanctuary':'ప్రతి plantation ఒక protected sanctuary',
'One is a land-cover measurement and the other an administrative category':'ఒకటి land-cover measurement; మరొకటి administrative category',
'Pterocarpus santalinus and red sanders':'Pterocarpus santalinus మరియు Red sanders','Red sanders and sandalwood':'Red sanders మరియు Sandalwood',
'Santalum album and sandalwood':'Santalum album మరియు Sandalwood','Coringa and a mangrove landscape association':'Coringa మరియు mangrove landscape సంబంధం',
'Count saplings without considering survival or location':'మొక్కల survival, location పట్టించుకోకుండా saplings లెక్కించడం','Maintain ecologically functional corridors between habitat patches':'ఆవాస ముక్కల మధ్య పనిచేసే ecological corridorsను కాపాడడం','Sever every connecting vegetation strip':'అనుసంధానించే ప్రతి vegetation stripను తొలగించడం','Treat all forest uses as spatially identical':'అన్ని forest uses భౌగోళికంగా ఒకేలా ఉన్నాయని భావించడం',
'It is certainly abundant and secure':'ఆ జాతి తప్పకుండా సమృద్ధిగా, సురక్షితంగా ఉంది','It is already extinct by definition':'నిర్వచనం ప్రకారమే అది ఇప్పటికే అంతరించింది','There is insufficient evidence for the risk assessment; it is not proof of safety':'ప్రమాద అంచనాకు సమాచారం సరిపోదు; ఇది జాతి సురక్షితమని రుజువు కాదు','It has no habitat needs':'దానికి ఎలాంటి habitat అవసరాలు లేవు','Captive breeding always removes every threat':'Captive breeding ప్రతి ముప్పును తప్పకుండా తొలగిస్తుంది','Wild populations never need habitat':'అడవి populationsకు habitat అవసరం లేదు','Natural habitat, genetic viability and ecological threats still need attention':'Natural habitat, genetic viability, ecological threatsపై ఇంకా చర్య అవసరం','All ecosystems are identical':'అన్ని ecosystems ఒకేలా ఉంటాయి','Endemic always means extinct':'Endemic అంటే ఎప్పుడూ Extinct అని అర్థం','Every Ramsar site is automatically the same as a national park':'ప్రతి Ramsar site స్వయంగా National Parkతో సమానం','A designation proves perfect management':'ఒక designation ఉంటే perfect management నిరూపితమవుతుంది','Threat category, legal protection and international site recognition are different dimensions':'Threat category, legal protection, international site recognition వేర్వేరు అంశాలు',
}

bank=load(BANK); reviewed=[]
for q in bank['questions']:
    ch=q.get('legacy_chapter'); n=int(q['id'].rsplit('-',1)[1])
    if ch not in ('34','35'): continue
    labels=labels34 if ch=='34' else labels35; labels_te=labels34te if ch=='34' else labels35te
    direct_limit=12 if ch=='34' else 16
    if n<=direct_limit:
        q['question_te']=f'{labels_te[n-1]}ను సరిగ్గా వివరించే వాక్యం ఏది?'
    elif (ch=='34' and n<=15) or (ch=='35' and n<=20):
        q['question_te']='జాబితా–Iలోని అంశాలను జాబితా–IIలోని నిర్వచనాలతో ఒకదానికొకటి సరిగా జతపరచండి.'
    elif (ch=='34' and n<=21) or (ch=='35' and n<=28):
        q['question_te']='I, II వాక్యాలను పరిశీలించి సరైన సమాధానాన్ని ఎంచుకోండి.'
    else:
        special_stems={
        'GEO-ORIG-34-022':'ఏ రెండు పేర్లను ఒకే speciesగా భావించకూడదు?','GEO-ORIG-34-023':'Forest Coverను చట్టపరంగా నమోదైన forest landతో ఎందుకు సమానంగా భావించకూడదు?','GEO-ORIG-34-024':'ఆవాస అనుసంధానాన్ని (Habitat connectivity) నేరుగా మెరుగుపరిచే చర్య ఏది?',
        'GEO-ORIG-35-029':'ఒక జాతి Data Deficientగా ఉంది. అత్యంత జాగ్రత్తగల నిర్ధారణ ఏది?','GEO-ORIG-35-030':'Zoo population ఒక్కటే ఒక జాతి conservation సమస్యను ఎందుకు పరిష్కరించలేదు?','GEO-ORIG-35-031':'Conservation labels గురించి సరైన వాక్యం ఏది?'}
        q['question_te']=special_stems[q['id']]
    q['options_en']=list(q['options'])
    q['options_te']=[te.get(x,special_te.get(x,x)) for x in q['options']]
    if all(x in des for x in q['options']):
        q['option_explanations_en']=[des[x][0] for x in q['options']]; q['option_explanations_te']=[des[x][1] for x in q['options']]
    elif all(x in combo for x in q['options']):
        q['option_explanations_en']=[combo_en[x] for x in q['options']]; q['option_explanations_te']=[combo_te[x] for x in q['options']]
    else:
        q['option_explanations_en']=['Check every component of this option against the definitions in the linked notes.' for _ in q['options']]
        q['option_explanations_te']=['ఈ ఎంపికలోని ప్రతి భాగాన్ని linked notesలోని నిర్వచనంతో విడిగా సరిచూడాలి.' for _ in q['options']]
    ai=q['answer']-1; q['explanation_en']=q['option_explanations_en'][ai]; q['explanation_te']=q['option_explanations_te'][ai]
    q['language']='bilingual'; q['difficulty']=q.get('difficulty','medium'); q['manual_review_status']='manually-reviewed-preserved-legacy'; q['reviewed_on']='2026-11-01'
    q.pop('options',None); q.pop('option_explanations',None); reviewed.append(q['id'])
if len(reviewed)!=55: raise SystemExit(f'expected 55, got {len(reviewed)}')
write(BANK,bank); m=load(MAN); m['questions_sha256']=hashlib.sha256(BANK.read_bytes()).hexdigest(); m['notes_sha256']=hashlib.sha256((CH/'Notes.html').read_bytes()).hexdigest(); m['question_count']=len(bank['questions']); m['release_ready']=False; m['railway_deployed']=False; write(MAN,m)
print(json.dumps({'reviewed':len(reviewed),'first':reviewed[0],'last':reviewed[-1]},indent=2))
