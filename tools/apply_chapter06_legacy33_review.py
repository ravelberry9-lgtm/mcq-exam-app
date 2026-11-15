import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "content" / "geography" / "india_ap_chapters" / "6"
BANK = CHAPTER / "Questions.json"
MANIFEST = CHAPTER / "manifest.json"


def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path, value):
    text = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    path.write_bytes(text.replace("\n", "\r\n").encode("utf-8"))


definitions = {
    "Dry-region vegetation with drought-adapted trees and shrubs": (
        "నీటి కొరతను తట్టుకునే చెట్లు, పొదలు గల పొడి ప్రాంత వృక్షసంపద",
        "This is thorn-forest vegetation adapted to seasonal or persistent water stress.",
        "ఇది నీటి కొరతను తట్టుకునే ముళ్ల అడవి (Thorn forest) వృక్షసంపద."
    ),
    "Forest with seasonal leaf shedding as a prominent community trait": (
        "ఒక నిర్దిష్ట కాలంలో ఆకులు రాల్చడం ప్రధాన లక్షణంగా గల అడవి",
        "This defines deciduous forest, whose trees prominently shed leaves during a stressful season.",
        "ఇది ప్రతికూల కాలంలో ఆకులు రాల్చే ఆకురాల్చే అడవి (Deciduous forest) నిర్వచనం."
    ),
    "Salt-tolerant intertidal tree or shrub community": (
        "అలల ప్రభావిత తీర ప్రాంతంలో పెరిగే ఉప్పును తట్టుకునే చెట్లు లేదా పొదల సముదాయం",
        "This defines mangrove forest in the intertidal zone.",
        "ఇది అలల ప్రభావిత ప్రాంతంలోని మడ అడవి (Mangrove forest) నిర్వచనం."
    ),
    "Forest retaining a broadly green canopy through the year with ongoing leaf turnover": (
        "ఆకులు విడివిడిగా మారుతున్నా ఏడాది పొడవునా సాధారణంగా పచ్చని పైకప్పు ఉండే అడవి",
        "This defines evergreen forest; individual leaves still fall and are replaced.",
        "ఇది సతతహరిత అడవి (Evergreen forest) నిర్వచనం; విడివిడిగా ఆకులు రాలి కొత్తవి వస్తూనే ఉంటాయి."
    ),
    "Supporting root descending obliquely from stem or branches": (
        "కాండం లేదా కొమ్మల నుంచి వాలుగా నేలవైపు దిగి మొక్కకు ఆధారం ఇచ్చే వేరు",
        "This defines a stilt root, which provides mechanical support.",
        "ఇది మొక్కకు యాంత్రిక ఆధారం ఇచ్చే ఊత వేరు (Stilt root) నిర్వచనం."
    ),
    "Plant using another plant for support without necessarily parasitising it": (
        "పరాన్నజీవిగా మారకుండానే మరో మొక్కను ఆధారంగా ఉపయోగించి పెరిగే మొక్క",
        "This defines an epiphyte; support does not by itself mean parasitism.",
        "ఇది ఉపజీవి మొక్క (Epiphyte) నిర్వచనం; ఆధారం తీసుకోవడం మాత్రమే పరాన్నజీవిత్వం కాదు."
    ),
    "Large flared structural root at a tree base": (
        "చెట్టు అడుగు భాగంలో పలకలా వెడల్పుగా విస్తరించి ఆధారం ఇచ్చే వేరు",
        "This defines a buttress root at the base of a tree.",
        "ఇది చెట్టు అడుగున పలకలా విస్తరించే పలక వేరు (Buttress root) నిర్వచనం."
    ),
    "Root projecting above wet sediment to aid gas exchange in certain species": (
        "నీటితో నిండిన మట్టి పైకి వచ్చి వాయు మార్పిడికి సహాయపడే ప్రత్యేక వేరు",
        "This defines a pneumatophore, a breathing root of certain wetland species.",
        "ఇది కొన్ని చిత్తడి జాతుల్లో వాయు మార్పిడికి సహాయపడే శ్వాస వేరు (Pneumatophore) నిర్వచనం."
    ),
    "Upper or poleward environmental limit of tree growth": (
        "చెట్లు పెరగగల ఎత్తు లేదా ధ్రువ దిశలోని పర్యావరణ పరిమితి",
        "This defines the treeline, whose position varies with local environmental conditions.",
        "ఇది స్థానిక పర్యావరణాన్ని బట్టి మారే వృక్షరేఖ (Treeline) నిర్వచనం."
    ),
    "Vegetation associated with mountain environmental gradients": (
        "పర్వతాల్లో ఎత్తు, ఉష్ణోగ్రత, తేమ మార్పులతో సంబంధం గల వృక్షసంపద",
        "This defines montane vegetation along mountain environmental gradients.",
        "ఇది పర్వత పర్యావరణ మార్పులతో సంబంధం గల పర్వత వృక్షసంపద (Montane vegetation) నిర్వచనం."
    ),
    "Vegetation above climatic treeline under cold conditions": (
        "చల్లని పరిస్థితుల్లో వాతావరణ వృక్షరేఖకు పైన పెరిగే వృక్షసంపద",
        "This defines alpine vegetation above the climatic treeline.",
        "ఇది వాతావరణ వృక్షరేఖకు పైన పెరిగే ఆల్పైన్ వృక్షసంపద (Alpine vegetation) నిర్వచనం."
    ),
    "Transition zone between ecological communities": (
        "రెండు జీవ సముదాయాల మధ్య ఉండే పర్యావరణ సంధి ప్రాంతం",
        "This defines an ecotone between ecological communities.",
        "ఇది రెండు జీవ సముదాయాల మధ్య పర్యావరణ సంధి (Ecotone) నిర్వచనం."
    ),
}

stems_te = {
    "GEO-ORIG-33-001": "సతతహరిత అడవి (Evergreen forest)ను సరిగ్గా వివరించే వాక్యం ఏది?",
    "GEO-ORIG-33-002": "ఆకురాల్చే అడవి (Deciduous forest)ను సరిగ్గా వివరించే వాక్యం ఏది?",
    "GEO-ORIG-33-003": "ముళ్ల అడవి (Thorn forest)ను సరిగ్గా వివరించే వాక్యం ఏది?",
    "GEO-ORIG-33-004": "మడ అడవి (Mangrove forest)ను సరిగ్గా వివరించే వాక్యం ఏది?",
    "GEO-ORIG-33-005": "శ్వాస వేరు (Pneumatophore)ను సరిగ్గా వివరించే వాక్యం ఏది?",
    "GEO-ORIG-33-006": "ఊత వేరు (Stilt root)ను సరిగ్గా వివరించే వాక్యం ఏది?",
    "GEO-ORIG-33-007": "ఉపజీవి మొక్క (Epiphyte)ను సరిగ్గా వివరించే వాక్యం ఏది?",
    "GEO-ORIG-33-008": "పలక వేరు (Buttress root)ను సరిగ్గా వివరించే వాక్యం ఏది?",
    "GEO-ORIG-33-009": "పర్వత వృక్షసంపద (Montane vegetation)ను సరిగ్గా వివరించే వాక్యం ఏది?",
    "GEO-ORIG-33-010": "ఆల్పైన్ వృక్షసంపద (Alpine vegetation)ను సరిగ్గా వివరించే వాక్యం ఏది?",
    "GEO-ORIG-33-011": "వృక్షరేఖ (Treeline)ను సరిగ్గా వివరించే వాక్యం ఏది?",
    "GEO-ORIG-33-012": "పర్యావరణ సంధి (Ecotone)ను సరిగ్గా వివరించే వాక్యం ఏది?",
}

for qid in ("GEO-ORIG-33-013", "GEO-ORIG-33-014", "GEO-ORIG-33-015"):
    stems_te[qid] = "జాబితా–Iలోని అంశాలను జాబితా–IIలోని నిర్వచనాలతో ఒకదానికొకటి సరిగా జతపరచండి."
for qid in ("GEO-ORIG-33-016", "GEO-ORIG-33-017", "GEO-ORIG-33-018", "GEO-ORIG-33-019", "GEO-ORIG-33-020", "GEO-ORIG-33-021"):
    stems_te[qid] = "I, II వాక్యాలను పరిశీలించి సరైన సమాధానాన్ని ఎంచుకోండి."
stems_te.update({
    "GEO-ORIG-33-022": "సతతహరిత (Evergreen) అనే పదానికి సరైన అర్థం ఏది?",
    "GEO-ORIG-33-023": "కొన్ని మడ జాతుల్లో శ్వాస వేర్లు (Pneumatophores) ఎందుకు ఉపయోగపడతాయి?",
    "GEO-ORIG-33-024": "ఒకే వృక్షరేఖ (Treeline) ఎత్తును అన్ని పర్వతాలకు వర్తింపజేయడానికి ముందు ఏమి పరిశీలించాలి?",
})

combo_te = {"Both I and II":"I, II రెండూ", "I only":"I మాత్రమే", "II only":"II మాత్రమే", "Neither I nor II":"I, II రెండూ కావు"}
combo_expl_en = {"Both I and II":"This option is correct only when both statements are scientifically correct.", "I only":"This option is correct only when statement I is correct and statement II is wrong.", "II only":"This option is correct only when statement II is correct and statement I is wrong.", "Neither I nor II":"This option is correct only when both statements are wrong."}
combo_expl_te = {"Both I and II":"I, II వాక్యాలు రెండూ శాస్త్రీయంగా సరైనప్పుడు మాత్రమే ఈ ఎంపిక సరైంది.", "I only":"I సరైందిగా, II తప్పుగా ఉన్నప్పుడు మాత్రమే ఈ ఎంపిక సరైంది.", "II only":"II సరైందిగా, I తప్పుగా ఉన్నప్పుడు మాత్రమే ఈ ఎంపిక సరైంది.", "Neither I nor II":"I, II వాక్యాలు రెండూ తప్పుగా ఉన్నప్పుడు మాత్రమే ఈ ఎంపిక సరైంది."}

special = {
    "GEO-ORIG-33-013": {
        "options_te":["A–2; B–4; C–1; D–3","A–1; B–3; C–2; D–4","A–3; B–1; C–4; D–2","A–4; B–1; C–3; D–2"],
        "option_explanations_en":["Correct: evergreen–2, deciduous–4, thorn–1 and mangrove–3.","Wrong: evergreen is not dry thorn vegetation, and the remaining pairs also shift definitions.","Wrong: salt-tolerant intertidal vegetation is mangrove, not evergreen; the other pairs are displaced.","Wrong: definition 4 belongs to deciduous forest, not evergreen forest."],
        "option_explanations_te":["ఇది సరైంది: Evergreen–2, Deciduous–4, Thorn–1, Mangrove–3.","ఇది తప్పు: పొడి ప్రాంత drought-adapted vegetation Thorn forestకు చెందుతుంది; Evergreenకు కాదు.","ఇది తప్పు: salt-tolerant intertidal vegetation Mangrove forestకు చెందుతుంది; Evergreenకు కాదు.","ఇది తప్పు: definition 4 ఆకురాల్చే అడవి (Deciduous forest)కు చెందుతుంది; Evergreenకు కాదు."]},
    "GEO-ORIG-33-014": {
        "options_te":["A–4; B–1; C–3; D–2","A–2; B–4; C–1; D–3","A–1; B–3; C–2; D–4","A–3; B–1; C–4; D–2"],
        "option_explanations_en":["Wrong: the above-sediment breathing root is a pneumatophore, not a stilt root.","Correct: pneumatophore–2, stilt root–4, epiphyte–1 and buttress root–3.","Wrong: an epiphyte uses another plant for support, so C must pair with 1.","Wrong: the large flared basal root is a buttress root, so D must pair with 3."],
        "option_explanations_te":["ఇది తప్పు: wet sediment పైకి వచ్చే breathing root Pneumatophore; Stilt root కాదు.","ఇది సరైంది: Pneumatophore–2, Stilt root–4, Epiphyte–1, Buttress root–3.","ఇది తప్పు: మరో మొక్కను ఆధారంగా ఉపయోగించేది Epiphyte; కాబట్టి C–1 కావాలి.","ఇది తప్పు: చెట్టు అడుగున flared root Buttress root; కాబట్టి D–3 కావాలి."]},
    "GEO-ORIG-33-015": {
        "options_te":["A–2; B–4; C–1; D–3","A–1; B–3; C–2; D–4","A–3; B–1; C–4; D–2","A–4; B–1; C–3; D–2"],
        "option_explanations_en":["Correct: montane–2, alpine–4, treeline–1 and ecotone–3.","Wrong: the upper limit of tree growth is treeline, not montane vegetation.","Wrong: a transition between communities is an ecotone, not montane vegetation.","Wrong: vegetation above the climatic treeline is alpine, not montane."],
        "option_explanations_te":["ఇది సరైంది: Montane–2, Alpine–4, Treeline–1, Ecotone–3.","ఇది తప్పు: tree growth upper limit Treeline; Montane vegetation కాదు.","ఇది తప్పు: communities మధ్య transition zone Ecotone; Montane vegetation కాదు.","ఇది తప్పు: climatic treeline పైన ఉండేది Alpine vegetation; Montane కాదు."]},
    "GEO-ORIG-33-022": {
        "options_te":["ఏ చెట్టులోనూ ఏ ఆకు ఎప్పుడూ రాలదు","విడివిడిగా ఆకులు మారినా పైకప్పు సాధారణంగా పచ్చగా ఉంటుంది","ప్రతి జాతి కాక్టస్‌గానే ఉంటుంది","ఏడాది పొడవునా వర్షపాతం ఉండదు"],
        "option_explanations_en":["Evergreen does not mean that no individual leaf ever falls.","This is correct: continuing leaf replacement can retain a broadly green canopy.","Cactus growth is not the definition of evergreen forest.","Absence of rainfall is not the definition of evergreen forest."],
        "option_explanations_te":["సతతహరిత (Evergreen) అంటే ఒక్క ఆకు కూడా రాలదని కాదు.","ఇది సరైంది: ఆకులు విడివిడిగా మారుతున్నా పైకప్పు పచ్చగా కొనసాగవచ్చు.","కాక్టస్ పెరుగుదల సతతహరిత అడవి నిర్వచనం కాదు.","వర్షం లేకపోవడం సతతహరిత అడవి నిర్వచనం కాదు."]},
    "GEO-ORIG-33-023": {
        "options_te":["ప్రతి జాతికి ఒకే రకమైన వేర్లు ఉన్నాయని సూచిస్తాయి","అన్ని వేర్లు తేలియాడే చేపలని నిరూపిస్తాయి","ఆక్సిజన్ తక్కువగా ఉన్న నీటిమునిగిన మట్టి పైన వాయు మార్పిడికి సహాయపడతాయి","అలల ప్రభావాన్ని పూర్తిగా తొలగిస్తాయి"],
        "option_explanations_en":["Mangrove species do not all possess identical root systems.","Roots are plant organs, not fish; the statement is biologically meaningless.","Correct: projecting roots help certain species exchange gases above oxygen-poor sediment.","Breathing roots do not eliminate tides."],
        "option_explanations_te":["అన్ని మడ జాతుల్లో ఒకే రకమైన వేరు వ్యవస్థ ఉండదు.","వేర్లు మొక్క భాగాలు; చేపలు కావు. ఈ వాక్యానికి జీవశాస్త్ర అర్థం లేదు.","ఇది సరైంది: పైకి వచ్చిన వేర్లు oxygen తక్కువగల మట్టి పైన వాయు మార్పిడికి సహాయపడతాయి.","శ్వాస వేర్లు (Pneumatophores) అలల ప్రభావాన్ని తొలగించవు."]},
    "GEO-ORIG-33-024": {
        "options_te":["అక్షాంశం, స్థానిక వాతావరణం, వాలు దిశ, disturbance","అన్ని వాలులకు సమాన తేమ వస్తుందని ఊహించడం","మానవ భూవినియోగాన్ని పట్టించుకోకపోవడం","ప్రపంచమంతటికీ ఒకే స్థిర సంఖ్యను మాత్రమే వాడటం"],
        "option_explanations_en":["Correct: treeline elevation varies with latitude, climate, aspect and disturbance.","Slopes differ in moisture and exposure, so this assumption is unsafe.","Human land use can shift the apparent treeline and cannot be ignored.","There is no single universal treeline altitude."],
        "option_explanations_te":["ఇది సరైంది: అక్షాంశం, climate, aspect, disturbanceతో వృక్షరేఖ ఎత్తు మారుతుంది.","వాలుల తేమ, సూర్యకాంతి exposure ఒకేలా ఉండవు; ఈ ఊహ తప్పు.","మానవ భూవినియోగం కనిపించే వృక్షరేఖను మార్చవచ్చు; దాన్ని విస్మరించకూడదు.","ప్రపంచమంతటికీ వర్తించే ఒకే వృక్షరేఖ ఎత్తు లేదు."]},
}

bank = load(BANK)
reviewed = []
for q in bank["questions"]:
    if q.get("legacy_chapter") != "33":
        continue
    qid = q["id"]
    q["question_te"] = stems_te[qid]
    q["options_en"] = list(q["options"])
    if qid in special:
        q.update(special[qid])
    elif int(qid.rsplit("-", 1)[1]) <= 12:
        q["options_te"] = [definitions[value][0] for value in q["options"]]
        q["option_explanations_en"] = [definitions[value][1] for value in q["options"]]
        q["option_explanations_te"] = [definitions[value][2] for value in q["options"]]
    elif 16 <= int(qid.rsplit("-", 1)[1]) <= 21:
        q["options_te"] = [combo_te[value] for value in q["options"]]
        q["option_explanations_en"] = [combo_expl_en[value] for value in q["options"]]
        q["option_explanations_te"] = [combo_expl_te[value] for value in q["options"]]
    else:
        q["options_te"] = list(q["options"])
        q["option_explanations_en"] = [
            "Check every pair; one wrong pair makes the whole matching code wrong."
            for _ in q["options"]
        ]
        q["option_explanations_te"] = [
            "ప్రతి జతను విడిగా సరిచూడాలి; ఒక్క జత తప్పినా మొత్తం matching code తప్పుతుంది."
            for _ in q["options"]
        ]
    answer_index = q["answer"] - 1
    q["explanation_en"] = q["option_explanations_en"][answer_index]
    q["explanation_te"] = q["option_explanations_te"][answer_index]
    q["language"] = "bilingual"
    q["difficulty"] = q.get("difficulty", "medium")
    q["manual_review_status"] = "manually-reviewed-preserved-legacy"
    q["reviewed_on"] = "2026-11-01"
    q.pop("options", None)
    q.pop("option_explanations", None)
    reviewed.append(qid)

if len(reviewed) != 24:
    raise SystemExit(f"Expected 24 chapter-33 questions, got {len(reviewed)}")

write_json(BANK, bank)
manifest = load(MANIFEST)
manifest["questions_sha256"] = hashlib.sha256(BANK.read_bytes()).hexdigest()
manifest["notes_sha256"] = hashlib.sha256((CHAPTER / "Notes.html").read_bytes()).hexdigest()
manifest["question_count"] = len(bank["questions"])
manifest["release_ready"] = False
manifest["railway_deployed"] = False
write_json(MANIFEST, manifest)
print(json.dumps({"reviewed": len(reviewed), "first": reviewed[0], "last": reviewed[-1]}, indent=2))
