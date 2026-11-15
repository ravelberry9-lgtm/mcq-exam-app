import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "content" / "geography" / "india_ap_chapters" / "5"
BANK = CHAPTER / "Questions.json"

SOURCES = [
    "https://www.nrcs.usda.gov/resources/education-and-teaching-materials/soil-facts",
    "https://icar.gov.in/sites/default/files/2025-11/December_2025%20Indian%20Farming.pdf",
    "https://apsac.ap.gov.in/?page_id=179",
]

CARDS = {
    "delta": ("Godavari–Krishna delta alluvium", "గోదావరి–కృష్ణా డెల్టా ఒండ్రు నేల (Delta alluvium)", "River deposits range from sand to clay; drainage and salinity vary locally.", "నదీ నిక్షేపాలు ఇసుక నుంచి బంకమట్టి వరకు మారుతాయి; పారుదల, లవణత స్థానికంగా మారతాయి.", "ap-alluvial-soils", ["IA05-P302-F04"]),
    "red": ("inland red soil", "అంతర్భాగ ఎర్ర నేల (Red soil)", "Oxidised iron colours many weathered crystalline-rock soils red.", "శైథిల్యమైన స్ఫటిక శిల నేలలకు ఆక్సీకృత ఇనుము (Oxidised iron) ఎర్ర రంగు ఇస్తుంది.", "ap-red-soils", ["IA05-P301-F03", "IA05-P301-F04"]),
    "black": ("black-soil shrink–swell behaviour", "నల్ల నేల ఉబ్బడం–కుంచడం (Shrink–swell)", "Smectitic clay retains moisture, swells when wet and cracks when dry.", "స్మెక్టైట్ బంకమట్టి (Smectitic clay) తేమను నిల్వచేసి తడిగా ఉబ్బి, ఎండినప్పుడు పగుళ్లు ఏర్పరుస్తుంది.", "ap-black-soils", ["IA05-P302-F02", "IA05-P302-F03"]),
    "laterite": ("lateritic upland soil", "ఎత్తుభాగ లేటరైట్ నేల (Lateritic soil)", "Strong weathering and leaching relatively enrich iron and aluminium oxides.", "తీవ్ర శైథిల్యం, క్షాళనం (Leaching) వల్ల ఇనుము–అల్యూమినియం ఆక్సైడ్లు సాపేక్షంగా పెరుగుతాయి.", "ap-lateritic-soils", ["IA05-P303-F02"]),
    "sand": ("sandy texture", "ఇసుక కణనిర్మాణం (Sandy texture)", "Coarse particles commonly favour rapid infiltration but weak water and nutrient retention.", "ముతక కణాలు సాధారణంగా వేగమైన చొరబాటుకు దోహదపడినా నీరు, పోషక నిల్వ తక్కువగా ఉంటుంది.", "texture-structure", ["IA05-P289-F06", "IA05-P289-F07"]),
    "clay": ("clayey texture", "బంకమట్టి కణనిర్మాణం (Clayey texture)", "Fine particles retain water strongly and can create drainage and workability constraints.", "సూక్ష్మ కణాలు నీటిని బలంగా పట్టుకొని పారుదల, దున్నే పనిలో ఇబ్బందులు కలిగించవచ్చు.", "texture-structure", ["IA05-P289-F06", "IA05-P289-F07"]),
    "loam": ("loamy texture", "లోమ్ కణనిర్మాణం (Loamy texture)", "Loam is a balanced mixture of sand, silt and clay, not pure organic matter.", "లోమ్ (Loam) అనేది ఇసుక, సిల్ట్, బంకమట్టి సమతుల్య మిశ్రమం; స్వచ్ఛ సేంద్రియ పదార్థం కాదు.", "loam-texture", ["IA05-P291-F09"]),
    "compact": ("soil compaction", "నేల బిగుసుకుపోవడం (Soil compaction)", "Compression raises bulk density and restricts pore space, roots, air and water movement.", "ఒత్తిడి వల్ల ఘనత్వం పెరిగి రంధ్రాలు, వేర్ల పెరుగుదల, గాలి–నీటి కదలిక తగ్గుతాయి.", "texture-structure", ["IA05-P289-F08"]),
    "salinity": ("salinity stress", "లవణత ఒత్తిడి (Salinity stress)", "High soluble-salt concentration makes water uptake more difficult for plants.", "అధిక కరిగే లవణాల సాంద్రత మొక్కలు నీటిని గ్రహించడం కష్టతరం చేస్తుంది.", "saline-sodic", ["IA05-P294-F04", "IA05-P294-F05"]),
    "waterlog": ("waterlogging", "నీరు నిలవడం (Waterlogging)", "Prolonged root-zone saturation displaces air and limits oxygen supply.", "వేర్ల మండలంలో ఎక్కువకాలం నీరు నిలిస్తే గాలి తొలగి ఆక్సిజన్ సరఫరా తగ్గుతుంది.", "soil-water-air", ["IA05-P290-F01"]),
    "erosion": ("topsoil erosion", "పైమట్టి కోత (Topsoil erosion)", "Water or wind detaches and transports fertile surface material.", "నీరు లేదా గాలి సారవంతమైన ఉపరితల పదార్థాన్ని వేరు చేసి తరలిస్తుంది.", "erosion-process", ["IA05-P296-F01"]),
    "organic": ("organic-matter addition", "సేంద్రియ పదార్థం చేర్పు (Organic-matter addition)", "Well-managed organic inputs can improve aggregation and biological activity.", "సరైన నిర్వహణతో చేర్చిన సేంద్రియ పదార్థం కణగుంపులు, జీవక్రియను మెరుగుపరుస్తుంది.", "humus-organic-matter", ["IA05-P289-F05"]),
    "sheet": ("sheet erosion", "పలుచని పొర కోత (Sheet erosion)", "Runoff removes a thin, relatively uniform layer over a broad area.", "ప్రవాహం విశాల ప్రాంతం నుంచి పలుచని, సుమారు సమానమైన మట్టి పొరను తొలగిస్తుంది.", "water-erosion-types", ["IA05-P296-F02"]),
    "rill": ("rill erosion", "చిన్న గాడుల కోత (Rill erosion)", "Runoff forms small channels that ordinary tillage can usually erase.", "ప్రవాహం సాధారణ దున్నుతో చెరిపేయగల చిన్న గాడులను ఏర్పరుస్తుంది.", "water-erosion-types", ["IA05-P296-F02"]),
    "gully": ("gully erosion", "పెద్ద గాడుల కోత (Gully erosion)", "Large persistent channels cannot be removed by ordinary tillage.", "సాధారణ దున్నుతో తొలగించలేని పెద్ద, నిలకడైన గాడులు ఏర్పడతాయి.", "water-erosion-types", ["IA05-P296-F02"]),
    "bank": ("riverbank erosion", "నదీ గట్టు కోత (Riverbank erosion)", "Channel flow and bank failure remove material from a river or stream bank.", "ప్రవాహం, గట్టు కూలడం వల్ల నది లేదా వాగు గట్టు పదార్థం తొలగుతుంది.", "bank-coastal-erosion", ["IA05-P296-F04"]),
    "contour": ("contour cultivation", "సమోన్నత సాగు (Contour cultivation)", "Operations follow equal-elevation lines across a slope and slow downslope runoff.", "వాలకు అడ్డంగా సమాన ఎత్తు రేఖలను అనుసరించే పనులు దిగువ ప్రవాహాన్ని నెమ్మదిస్తాయి.", "conservation-practices", ["IA05-P297-F04"]),
    "terrace": ("terracing", "మెట్ల సాగు (Terracing)", "A slope is reshaped into steps that shorten effective slope length and need safe outlets.", "వాలను మెట్లుగా మార్చి ప్రభావవంతమైన వాలు పొడవును తగ్గిస్తారు; సురక్షిత నీటి వెలికితీత అవసరం.", "conservation-practices", ["IA05-P297-F05"]),
    "cover": ("cover crop", "కవచ పంట (Cover crop)", "Living vegetation protects soil between or with main crops.", "ప్రధాన పంటల మధ్య లేదా వాటితో పాటు జీవ వృక్ష ఆవరణం నేలను కాపాడుతుంది.", "conservation-practices", ["IA05-P297-F09"]),
    "mulch": ("mulching", "మల్చింగ్ (Mulching)", "Residue or other cover on the surface reduces raindrop impact and evaporation.", "ఉపరితలంపై పంట అవశేషం లేదా ఇతర కప్పు వర్షబిందువు ఢీకొట్టడం, ఆవిరీభవనాన్ని తగ్గిస్తుంది.", "conservation-practices", ["IA05-P297-F03"]),
    "salinisation": ("salinisation", "లవణీకరణ (Salinisation)", "Soluble salts accumulate when salt input and upward movement exceed leaching and drainage.", "లవణ ప్రవేశం, పైకి కదలిక క్షాళనం, పారుదలను మించినప్పుడు కరిగే లవణాలు పేరుకుంటాయి.", "saline-sodic", ["IA05-P294-F04", "IA05-P294-F05"]),
    "mining": ("nutrient mining", "పోషకాల నికర క్షయం (Nutrient mining)", "Crop and erosion outputs repeatedly exceed nutrient replenishment.", "పంటల తొలగింపు, కోత ద్వారా పోయే పోషకాలు తిరిగి చేర్చేవాటిని వరుసగా మించుతాయి.", "erosion-causes", ["IA05-P297-F01"]),
}


def option_set(keys, answer):
    correct = keys[0]
    ordered = list(keys[1:])
    ordered.insert(answer - 1, correct)
    en = [CARDS[key][0] for key in ordered]
    te = [CARDS[key][1] for key in ordered]
    exp_en = []
    exp_te = []
    for key in ordered:
        card = CARDS[key]
        if key == correct:
            exp_en.append(f"Correct. {card[2]}")
            exp_te.append(f"సరైనది. {card[3]}")
        else:
            exp_en.append(f"This describes {card[0]}, not {CARDS[correct][0]}. {card[2]}")
            exp_te.append(f"ఇది {card[1]}ను వివరిస్తుంది; {CARDS[correct][1]}ను కాదు. {card[3]}")
    return en, te, exp_en, exp_te


def direct_record(old, key, distractors, question_en, question_te):
    options_en, options_te, exp_en, exp_te = option_set([key, *distractors], old["answer"])
    card = CARDS[key]
    return {
        **{k: old[k] for k in ("id", "chapter", "origin", "label", "legacy_chapter", "legacy_section")},
        "language": "bilingual", "kind": "concept", "difficulty": "moderate",
        "fact_ids": card[5], "question_en": question_en, "question_te": question_te,
        "options_en": options_en, "options_te": options_te, "answer": old["answer"],
        "option_explanations_en": exp_en, "option_explanations_te": exp_te,
        "explanation_en": card[2], "explanation_te": card[3], "section": card[4],
        "related_sections": [], "source_paragraph": card[2], "source_urls": SOURCES,
        "reviewed_on": "2026-11-01", "manual_review_status": "reviewed",
    }


def literal_record(old, *, question_en, question_te, options_en, options_te, option_explanations_en,
                   option_explanations_te, explanation_en, explanation_te, section, fact_ids,
                   difficulty="moderate", kind="application"):
    return {
        **{k: old[k] for k in ("id", "chapter", "origin", "label", "legacy_chapter", "legacy_section")},
        "language": "bilingual", "kind": kind, "difficulty": difficulty, "fact_ids": fact_ids,
        "question_en": question_en, "question_te": question_te, "options_en": options_en,
        "options_te": options_te, "answer": old["answer"],
        "option_explanations_en": option_explanations_en,
        "option_explanations_te": option_explanations_te,
        "explanation_en": explanation_en, "explanation_te": explanation_te,
        "section": section, "related_sections": [], "source_paragraph": explanation_en,
        "source_urls": SOURCES, "reviewed_on": "2026-11-01", "manual_review_status": "reviewed",
    }


def combo_options(qid, answer, correct_en, correct_te):
    options_en = ["Statement I only", "Statement II only", "Both statements I and II", "Neither statement I nor II"]
    options_te = ["వాక్యం I మాత్రమే", "వాక్యం II మాత్రమే", "I, II రెండూ", "I, II రెండూ కాదు"]
    correct_codes = {
        "GEO-ORIG-30-016": 3, "GEO-ORIG-30-017": 1, "GEO-ORIG-30-018": 2,
        "GEO-ORIG-30-019": 3, "GEO-ORIG-30-020": 3, "GEO-ORIG-30-021": 1,
        "GEO-ORIG-31-016": 3, "GEO-ORIG-31-017": 1, "GEO-ORIG-31-018": 2,
        "GEO-ORIG-31-019": 4, "GEO-ORIG-31-020": 3, "GEO-ORIG-31-021": 1,
    }
    correct_code = correct_codes[qid]
    if correct_code != answer:
        options_en[correct_code - 1], options_en[answer - 1] = options_en[answer - 1], options_en[correct_code - 1]
        options_te[correct_code - 1], options_te[answer - 1] = options_te[answer - 1], options_te[correct_code - 1]
    option_explanations_en = []
    option_explanations_te = []
    for index in range(1, 5):
        if index == answer:
            option_explanations_en.append(f"Correct. {correct_en}")
            option_explanations_te.append(f"సరైనది. {correct_te}")
        else:
            option_explanations_en.append(f"Incorrect combination. {correct_en}")
            option_explanations_te.append(f"తప్పు కలయిక. {correct_te}")
    return options_en, options_te, option_explanations_en, option_explanations_te


def main() -> None:
    data = json.loads(BANK.read_text(encoding="utf-8"))
    old = {q["id"]: q for q in data["questions"] if q["id"].startswith("GEO-ORIG-")}
    rewritten = {}
    direct_specs = [
        ("GEO-ORIG-30-001", "delta", ["red", "laterite", "black"], "Which description best identifies the Godavari–Krishna delta alluvial setting?", "గోదావరి–కృష్ణా డెల్టా ఒండ్రు నేల (Delta alluvium)ను సరిగ్గా గుర్తించే వివరణ ఏది?"),
        ("GEO-ORIG-30-002", "red", ["delta", "black", "laterite"], "Which description best identifies an inland red-soil setting?", "అంతర్భాగ ఎర్ర నేల (Red soil)ను సరిగ్గా గుర్తించే వివరణ ఏది?"),
        ("GEO-ORIG-30-003", "black", ["delta", "red", "laterite"], "Which behaviour most clearly identifies a shrink–swell black soil?", "ఉబ్బే–కుంచే నల్ల నేల (Shrink–swell black soil)ను స్పష్టంగా గుర్తించే లక్షణం ఏది?"),
        ("GEO-ORIG-30-004", "laterite", ["delta", "red", "black"], "Which process best identifies a lateritic upland profile?", "ఎత్తుభాగ లేటరైట్ నేల (Lateritic soil)ను సరిగ్గా గుర్తించే ప్రక్రియ ఏది?"),
        ("GEO-ORIG-30-005", "sand", ["clay", "loam", "compact"], "Which description best identifies sandy texture?", "ఇసుక కణనిర్మాణం (Sandy texture)ను సరిగ్గా గుర్తించే వివరణ ఏది?"),
        ("GEO-ORIG-30-006", "clay", ["sand", "loam", "compact"], "Which description best identifies clayey texture?", "బంకమట్టి కణనిర్మాణం (Clayey texture)ను సరిగ్గా గుర్తించే వివరణ ఏది?"),
        ("GEO-ORIG-30-007", "loam", ["sand", "clay", "compact"], "Which description best identifies loamy texture?", "లోమ్ కణనిర్మాణం (Loamy texture)ను సరిగ్గా గుర్తించే వివరణ ఏది?"),
        ("GEO-ORIG-30-008", "compact", ["sand", "clay", "loam"], "Which change best identifies soil compaction?", "నేల బిగుసుకుపోవడం (Soil compaction)ను సరిగ్గా గుర్తించే మార్పు ఏది?"),
        ("GEO-ORIG-30-009", "salinity", ["erosion", "organic", "waterlog"], "Which process directly causes osmotic water stress in saline soil?", "లవణ నేలలో ద్రవాభిసరణ నీటి ఒత్తిడి (Osmotic water stress)ను నేరుగా కలిగించే ప్రక్రియ ఏది?"),
        ("GEO-ORIG-30-010", "waterlog", ["salinity", "erosion", "organic"], "Which condition best identifies waterlogging?", "నీరు నిలవడం (Waterlogging)ను సరిగ్గా గుర్తించే పరిస్థితి ఏది?"),
        ("GEO-ORIG-30-011", "erosion", ["salinity", "organic", "waterlog"], "Which process best identifies topsoil erosion?", "పైమట్టి కోత (Topsoil erosion)ను సరిగ్గా గుర్తించే ప్రక్రియ ఏది?"),
        ("GEO-ORIG-30-012", "organic", ["salinity", "erosion", "waterlog"], "Which management input can improve soil aggregation and biological activity?", "నేల కణగుంపులు, జీవక్రియను మెరుగుపరచగల నిర్వహణ చర్య ఏది?"),
        ("GEO-ORIG-31-001", "sheet", ["rill", "gully", "bank"], "Which description identifies sheet erosion?", "పలుచని పొర కోత (Sheet erosion)ను గుర్తించే వివరణ ఏది?"),
        ("GEO-ORIG-31-002", "rill", ["sheet", "gully", "bank"], "Which description identifies rill erosion?", "చిన్న గాడుల కోత (Rill erosion)ను గుర్తించే వివరణ ఏది?"),
        ("GEO-ORIG-31-003", "gully", ["sheet", "rill", "bank"], "Which description identifies gully erosion?", "పెద్ద గాడుల కోత (Gully erosion)ను గుర్తించే వివరణ ఏది?"),
        ("GEO-ORIG-31-004", "bank", ["sheet", "rill", "gully"], "Which description identifies riverbank erosion?", "నదీ గట్టు కోత (Riverbank erosion)ను గుర్తించే వివరణ ఏది?"),
        ("GEO-ORIG-31-005", "contour", ["terrace", "cover", "mulch"], "Which description identifies contour cultivation?", "సమోన్నత సాగు (Contour cultivation)ను గుర్తించే వివరణ ఏది?"),
        ("GEO-ORIG-31-006", "terrace", ["contour", "cover", "mulch"], "Which description identifies terracing?", "మెట్ల సాగు (Terracing)ను గుర్తించే వివరణ ఏది?"),
        ("GEO-ORIG-31-007", "cover", ["contour", "terrace", "mulch"], "Which description identifies a cover crop?", "కవచ పంట (Cover crop)ను గుర్తించే వివరణ ఏది?"),
        ("GEO-ORIG-31-008", "mulch", ["contour", "terrace", "cover"], "Which description identifies mulching?", "మల్చింగ్ (Mulching)ను గుర్తించే వివరణ ఏది?"),
        ("GEO-ORIG-31-009", "waterlog", ["salinisation", "compact", "mining"], "Which condition best identifies waterlogging?", "నీరు నిలవడం (Waterlogging)ను సరిగ్గా గుర్తించే పరిస్థితి ఏది?"),
        ("GEO-ORIG-31-010", "salinisation", ["waterlog", "compact", "mining"], "Which process best identifies salinisation?", "లవణీకరణ (Salinisation)ను సరిగ్గా గుర్తించే ప్రక్రియ ఏది?"),
        ("GEO-ORIG-31-011", "compact", ["waterlog", "salinisation", "mining"], "Which change best identifies soil compaction?", "నేల బిగుసుకుపోవడం (Soil compaction)ను సరిగ్గా గుర్తించే మార్పు ఏది?"),
        ("GEO-ORIG-31-012", "mining", ["waterlog", "salinisation", "compact"], "Which process best identifies nutrient mining?", "పోషకాల నికర క్షయం (Nutrient mining)ను సరిగ్గా గుర్తించే ప్రక్రియ ఏది?"),
    ]
    for spec in direct_specs:
        qid, key, distractors, question_en, question_te = spec
        rewritten[qid] = direct_record(old[qid], key, distractors, question_en, question_te)

    # The remaining legacy IDs are individually reviewed matching, statement and application items.
    set_specs = [
        ("GEO-ORIG-30-013", "A–2; B–4; C–1; D–3", "A–2; B–4; C–1; D–3", "A. Delta alluvium; B. Red soil; C. Black soil; D. Laterite — 1. Shrink–swell clay; 2. River deposit; 3. Leached Fe–Al enrichment; 4. Oxidised-iron colour", "A. డెల్టా ఒండ్రు; B. ఎర్ర నేల; C. నల్ల నేల; D. లేటరైట్ — 1. ఉబ్బే–కుంచే బంకమట్టి; 2. నదీ నిక్షేపం; 3. క్షాళిత Fe–Al సాంద్రీకరణ; 4. ఆక్సీకృత ఇనుము రంగు", "ap-soil-map", ["IA05-P301-F03", "IA05-P302-F03", "IA05-P302-F04", "IA05-P303-F02"]),
        ("GEO-ORIG-30-014", "A–2; B–4; C–1; D–3", "A–2; B–4; C–1; D–3", "A. Sandy; B. Clayey; C. Loam; D. Compacted — 1. Balanced sand–silt–clay; 2. Coarse and rapidly draining; 3. Compressed pore space; 4. Fine and strongly water-retentive", "A. ఇసుక; B. బంకమట్టి; C. లోమ్; D. బిగుసుకున్న నేల — 1. సమతుల్య ఇసుక–సిల్ట్–బంకమట్టి; 2. ముతక, వేగమైన పారుదల; 3. ఒత్తిడితో తగ్గిన రంధ్రాలు; 4. సూక్ష్మ, బలమైన నీటి నిల్వ", "texture-structure", ["IA05-P289-F06", "IA05-P289-F08", "IA05-P291-F09"]),
        ("GEO-ORIG-30-015", "A–2; B–4; C–1; D–3", "A–2; B–4; C–1; D–3", "A. Salinity; B. Waterlogging; C. Erosion; D. Organic input — 1. Surface removal; 2. Osmotic stress; 3. Better aggregation; 4. Oxygen shortage", "A. లవణత; B. నీరు నిలవడం; C. కోత; D. సేంద్రియ చేర్పు — 1. ఉపరితల తొలగింపు; 2. ద్రవాభిసరణ ఒత్తిడి; 3. మెరుగైన కణగుంపులు; 4. ఆక్సిజన్ కొరత", "soil-water-air", ["IA05-P289-F05", "IA05-P290-F01", "IA05-P294-F04", "IA05-P296-F01"]),
        ("GEO-ORIG-31-013", "A–2; B–4; C–1; D–3", "A–2; B–4; C–1; D–3", "A. Sheet; B. Rill; C. Gully; D. Bank — 1. Large persistent channel; 2. Thin broad removal; 3. River-bank loss; 4. Small tillage-removable channel", "A. పలుచని పొర; B. చిన్న గాడి; C. పెద్ద గాడి; D. గట్టు — 1. పెద్ద నిలకడైన గాడి; 2. విశాల పలుచని తొలగింపు; 3. నదీ గట్టు నష్టం; 4. దున్నుతో చెరిగే చిన్న గాడి", "water-erosion-types", ["IA05-P296-F02", "IA05-P296-F04"]),
        ("GEO-ORIG-31-014", "A–2; B–4; C–1; D–3", "A–2; B–4; C–1; D–3", "A. Contour; B. Terrace; C. Cover crop; D. Mulch — 1. Living cover; 2. Equal-elevation operations; 3. Surface residue; 4. Stepped slope", "A. సమోన్నత సాగు; B. మెట్లు; C. కవచ పంట; D. మల్చ్ — 1. జీవ ఆవరణం; 2. సమాన ఎత్తు చర్యలు; 3. ఉపరితల అవశేషం; 4. మెట్ల వాలు", "conservation-practices", ["IA05-P297-F03", "IA05-P297-F04", "IA05-P297-F05", "IA05-P297-F09"]),
        ("GEO-ORIG-31-015", "A–2; B–4; C–1; D–3", "A–2; B–4; C–1; D–3", "A. Waterlogging; B. Salinisation; C. Compaction; D. Nutrient mining — 1. Pore reduction; 2. Oxygen shortage; 3. Outputs exceed inputs; 4. Salt accumulation", "A. నీరు నిలవడం; B. లవణీకరణ; C. బిగుసుకుపోవడం; D. పోషకాల క్షయం — 1. రంధ్రాల తగ్గుదల; 2. ఆక్సిజన్ కొరత; 3. చేర్పుకంటే నష్టం ఎక్కువ; 4. లవణాల పేరుకుపోవడం", "erosion-causes", ["IA05-P290-F01", "IA05-P294-F04", "IA05-P297-F01"]),
    ]
    match_options_en = ["A–1; B–2; C–3; D–4", "A–3; B–1; C–4; D–2", "A–4; B–3; C–2; D–1", "A–2; B–4; C–1; D–3"]
    match_options_te = match_options_en[:]
    for qid, correct_en, correct_te, lists_en, lists_te, section, facts in set_specs:
        answer = old[qid]["answer"]
        options_en = match_options_en[:]
        options_te = match_options_te[:]
        current = options_en.index(correct_en)
        options_en[current], options_en[answer - 1] = options_en[answer - 1], options_en[current]
        options_te[current], options_te[answer - 1] = options_te[answer - 1], options_te[current]
        exp_en = ["Correct one-to-one matching." if i == answer else "This code mismatches at least one concept and process." for i in range(1, 5)]
        exp_te = ["సరైన ఒకదానికి-ఒకటి జత." if i == answer else "ఈ కోడ్ కనీసం ఒక భావన–ప్రక్రియ జతను తప్పుగా కలుపుతుంది." for i in range(1, 5)]
        rewritten[qid] = literal_record(old[qid], question_en=f"Match List I with List II: {lists_en}", question_te=f"జాబితా Iను జాబితా IIతో సరిపోల్చండి: {lists_te}", options_en=options_en, options_te=options_te, option_explanations_en=exp_en, option_explanations_te=exp_te, explanation_en=f"The correct code is {correct_en}.", explanation_te=f"సరైన కోడ్ {correct_te}.", section=section, fact_ids=facts, kind="matching")

    statement_specs = [
        ("GEO-ORIG-30-016", "I. Delta alluvium is deposited by rivers. II. Red colour commonly reflects oxidised iron.", "I. డెల్టా ఒండ్రు నేల (Delta alluvium) నదుల నిక్షేపం. II. ఎర్ర రంగు సాధారణంగా ఆక్సీకృత ఇనుమును సూచిస్తుంది.", "Both statements are correct.", "రెండు వాక్యాలూ సరైనవి.", "ap-red-soils", ["IA05-P302-F04", "IA05-P301-F04"]),
        ("GEO-ORIG-30-017", "I. Black soil commonly shows shrink–swell behaviour. II. Laterite is produced by the same shrink–swell process.", "I. నల్ల నేల సాధారణంగా ఉబ్బడం–కుంచడం చూపుతుంది. II. అదే ఉబ్బడం–కుంచడం ప్రక్రియతో లేటరైట్ ఏర్పడుతుంది.", "Statement I is correct; statement II is false because laterite forms through intense weathering and leaching.", "వాక్యం I సరైనది; II తప్పు. లేటరైట్ తీవ్రమైన శైథిల్యం, క్షాళనం (Leaching) వల్ల ఏర్పడుతుంది.", "laterite-formation", ["IA05-P292-F06", "IA05-P293-F02"]),
        ("GEO-ORIG-30-018", "I. Sandy texture is dominated by fine clay particles. II. Clayey texture generally retains water more strongly than sandy texture.", "I. ఇసుక కణనిర్మాణంలో సూక్ష్మ బంకమట్టి కణాలే అధికం. II. బంకమట్టి కణనిర్మాణం సాధారణంగా ఇసుక కంటే నీటిని బలంగా నిల్వచేస్తుంది.", "Statement I is false and statement II is correct.", "వాక్యం I తప్పు; II సరైనది.", "texture-structure", ["IA05-P289-F06", "IA05-P289-F07"]),
        ("GEO-ORIG-30-019", "I. Loam is a balanced sand–silt–clay mixture. II. Compaction reduces pore space and restricts roots.", "I. లోమ్ (Loam) ఇసుక–సిల్ట్–బంకమట్టి సమతుల్య మిశ్రమం. II. నేల బిగుసుకుపోవడం రంధ్రాలను తగ్గించి వేర్లను అడ్డుకుంటుంది.", "Both statements are correct.", "రెండు వాక్యాలూ సరైనవి.", "texture-structure", ["IA05-P289-F08", "IA05-P291-F09"]),
        ("GEO-ORIG-30-020", "I. High soluble salts can make plant water uptake difficult. II. Waterlogging can limit root-zone oxygen.", "I. అధిక కరిగే లవణాలు మొక్కల నీటి గ్రహణాన్ని కష్టతరం చేస్తాయి. II. నీరు నిలవడం వేర్ల మండలంలో ఆక్సిజన్‌ను తగ్గిస్తుంది.", "Both statements are correct.", "రెండు వాక్యాలూ సరైనవి.", "saline-sodic", ["IA05-P290-F01", "IA05-P294-F04"]),
        ("GEO-ORIG-30-021", "I. Erosion removes fertile surface material. II. Organic inputs necessarily remove that same surface material.", "I. కోత సారవంతమైన ఉపరితల పదార్థాన్ని తొలగిస్తుంది. II. సేంద్రియ చేర్పు తప్పనిసరిగా అదే ఉపరితలాన్ని తొలగిస్తుంది.", "Statement I is correct; statement II is false because managed organic inputs can improve aggregation.", "వాక్యం I సరైనది; II తప్పు. సరైన సేంద్రియ చేర్పు కణగుంపులను మెరుగుపరచగలదు.", "erosion-process", ["IA05-P289-F05", "IA05-P296-F01"]),
        ("GEO-ORIG-31-016", "I. Sheet erosion removes a thin layer broadly. II. Rills are small channels often removable by ordinary tillage.", "I. పలుచని పొర కోత విశాల ప్రాంతం నుంచి పలుచని పొరను తొలగిస్తుంది. II. చిన్న గాడులను సాధారణ దున్నుతో చెరిపేయవచ్చు.", "Both statements are correct.", "రెండు వాక్యాలూ సరైనవి.", "water-erosion-types", ["IA05-P296-F02"]),
        ("GEO-ORIG-31-017", "I. Gullies are large persistent channels. II. Riverbank erosion is identical to gully erosion.", "I. పెద్ద గాడులు నిలకడైన పెద్ద కాలువలు. II. నదీ గట్టు కోత, పెద్ద గాడుల కోత పూర్తిగా ఒకటే.", "Statement I is correct; statement II is false because bank erosion removes channel-bank material.", "వాక్యం I సరైనది; II తప్పు. గట్టు కోత ప్రవాహ మార్గపు గట్టు పదార్థాన్ని తొలగిస్తుంది.", "bank-coastal-erosion", ["IA05-P296-F02", "IA05-P296-F04"]),
        ("GEO-ORIG-31-018", "I. Contour cultivation reshapes every slope into steps. II. Terracing reshapes a slope into stepped surfaces.", "I. సమోన్నత సాగు ప్రతి వాలను మెట్లుగా మారుస్తుంది. II. మెట్ల సాగు వాలను మెట్ల ఉపరితలాలుగా మారుస్తుంది.", "Statement I is false and statement II is correct.", "వాక్యం I తప్పు; II సరైనది.", "conservation-practices", ["IA05-P297-F04", "IA05-P297-F05"]),
        ("GEO-ORIG-31-019", "I. A cover crop is only dead surface residue. II. Mulch is only living vegetation.", "I. కవచ పంట కేవలం చనిపోయిన ఉపరితల అవశేషం. II. మల్చ్ కేవలం జీవ వృక్ష ఆవరణం.", "Both statements are false: a cover crop is living vegetation, while mulch is surface cover such as residue.", "రెండు వాక్యాలూ తప్పు: కవచ పంట జీవ వృక్ష ఆవరణం; మల్చ్ ఉపరితల అవశేషం వంటి కప్పు.", "conservation-practices", ["IA05-P297-F03", "IA05-P297-F09"]),
        ("GEO-ORIG-31-020", "I. Waterlogging reduces aeration through saturation. II. Salinisation is soluble-salt accumulation.", "I. నీరు నిలవడం వల్ల గాలి సరఫరా తగ్గుతుంది. II. లవణీకరణ అంటే కరిగే లవణాలు పేరుకుపోవడం.", "Both statements are correct.", "రెండు వాక్యాలూ సరైనవి.", "saline-sodic", ["IA05-P290-F01", "IA05-P294-F04"]),
        ("GEO-ORIG-31-021", "I. Compaction reduces pore space through compression. II. Nutrient mining is the same physical compression process.", "I. బిగుసుకుపోవడం ఒత్తిడితో రంధ్రాలను తగ్గిస్తుంది. II. పోషకాల నికర క్షయం కూడా అదే భౌతిక ఒత్తిడి ప్రక్రియ.", "Statement I is correct; statement II is false because nutrient mining means losses exceed replenishment.", "వాక్యం I సరైనది; II తప్పు. పోషకాల నికర క్షయం అంటే తిరిగి చేర్చేవాటికంటే నష్టం ఎక్కువ కావడం.", "erosion-causes", ["IA05-P289-F08", "IA05-P297-F01"]),
    ]
    for qid, question_en, question_te, correct_en, correct_te, section, facts in statement_specs:
        opts_en, opts_te, exps_en, exps_te = combo_options(qid, old[qid]["answer"], correct_en, correct_te)
        rewritten[qid] = literal_record(old[qid], question_en=question_en, question_te=question_te, options_en=opts_en, options_te=opts_te, option_explanations_en=exps_en, option_explanations_te=exps_te, explanation_en=correct_en, explanation_te=correct_te, section=section, fact_ids=facts, kind="multiple-statements")

    applications = {
        "GEO-ORIG-30-022": ("Why can plants suffer water stress even when saline soil is wet?", "లవణ నేల తడిగా ఉన్నా మొక్కలు నీటి ఒత్తిడికి ఎందుకు గురవుతాయి?", ["Wetness makes every form of water equally available.", "Salts permanently remove all oxygen from the atmosphere.", "All crops have identical salt tolerance.", "High soluble-salt concentration lowers the ease of root water uptake."], ["తడి ఉండటం వల్ల నీటి రూపాలన్నీ సమానంగా లభిస్తాయి.", "లవణాలు వాతావరణంలోని ఆక్సిజన్ మొత్తాన్ని శాశ్వతంగా తొలగిస్తాయి.", "పంటలన్నింటికీ ఒకే లవణ సహనం ఉంటుంది.", "అధిక కరిగే లవణాల సాంద్రత వేర్లు నీటిని గ్రహించడం కష్టతరం చేస్తుంది."], "saline-sodic", ["IA05-P294-F04"]),
        "GEO-ORIG-30-023": ("Why should visibly different parts of a delta field be sampled separately?", "డెల్టా పొలంలో స్పష్టంగా వేరుగా కనిపించే భాగాల నుంచి నమూనాలను విడిగా ఎందుకు తీసుకోవాలి?", ["A delta is chemically uniform.", "Texture, drainage and salt distribution can vary within the field.", "Sampling depth never affects interpretation.", "A district name fixes every nutrient value."], ["డెల్టా మొత్తం రసాయనపరంగా ఒకేలా ఉంటుంది.", "పొలంలో కణనిర్మాణం, పారుదల, లవణ విస్తరణ మారవచ్చు.", "నమూనా లోతు ఫలితంపై ఎప్పుడూ ప్రభావం చూపదు.", "జిల్లా పేరు ప్రతి పోషక విలువను నిర్ణయిస్తుంది."], "ap-alluvial-soils", ["IA05-P302-F04"]),
        "GEO-ORIG-30-024": ("Which claim about black-soil crop suitability must be rejected?", "నల్ల నేలలో పంట అనుకూలత గురించి ఏ వాదనను తిరస్కరించాలి?", ["Every black soil guarantees high cotton yield without water, drainage or nutrient management.", "Drainage affects crop performance.", "Rainfall timing affects crop performance.", "Variety and management affect crop performance."], ["నీరు, పారుదల, పోషక నిర్వహణ లేకున్నా ప్రతి నల్ల నేల అధిక పత్తి దిగుబడికి హామీ ఇస్తుంది.", "పారుదల పంట పనితీరును ప్రభావితం చేస్తుంది.", "వర్షపాతం సమయం పంట పనితీరును ప్రభావితం చేస్తుంది.", "రకం, నిర్వహణ పంట పనితీరును ప్రభావితం చేస్తాయి."], "black-properties", ["IA05-P292-F07", "IA05-P292-F09"]),
        "GEO-ORIG-31-022": ("Why can contour cultivation reduce erosion on a suitable slope?", "అనుకూల వాలులో సమోన్నత సాగు (Contour cultivation) కోతను ఎందుకు తగ్గిస్తుంది?", ["Across-slope rows interrupt runoff paths and reduce flow velocity.", "It makes every slope vertical.", "It removes all soil organisms.", "It guarantees that extreme floods cause no damage."], ["వాలకు అడ్డంగా ఉన్న వరుసలు ప్రవాహ మార్గాన్ని విభజించి వేగాన్ని తగ్గిస్తాయి.", "ఇది ప్రతి వాలను నిలువుగా మారుస్తుంది.", "ఇది నేల జీవులన్నిటినీ తొలగిస్తుంది.", "తీవ్ర వరదలు నష్టం చేయవని హామీ ఇస్తుంది."], "conservation-practices", ["IA05-P297-F04"]),
        "GEO-ORIG-31-023": ("Which degradation pair should be checked first on a heavily irrigated farm with poor drainage?", "అధిక నీటిపారుదల, బలహీన పారుదల ఉన్న పొలంలో ముందుగా ఏ క్షీణత జంటను పరీక్షించాలి?", ["Waterlogging and salt accumulation", "Guaranteed improvement in aeration", "Absence of sea tides alone", "Complete absence of evaporation"], ["నీరు నిలవడం మరియు లవణాలు పేరుకుపోవడం", "గాలి సరఫరా తప్పక మెరుగుపడటం", "సముద్ర అలలు లేకపోవడం మాత్రమే", "ఆవిరీభవనం పూర్తిగా లేకపోవడం"], "saline-sodic", ["IA05-P294-F03", "IA05-P294-F05"]),
        "GEO-ORIG-31-024": ("Why does a check dam require safe overflow and maintenance?", "చిన్న అడ్డుకట్టకు (Check dam) సురక్షిత అదనపు ప్రవాహ మార్గం, నిర్వహణ ఎందుకు అవసరం?", ["Every check dam stores unlimited water.", "Sediment can never accumulate.", "Downstream effects are impossible.", "Flood inflow may exceed capacity, and sediment can reduce storage or damage the structure."], ["ప్రతి చిన్న అడ్డుకట్ట పరిమితిలేని నీటిని నిల్వ చేస్తుంది.", "అవక్షేపం ఎప్పుడూ చేరదు.", "దిగువ ప్రవాహ ప్రభావాలు అసాధ్యం.", "వరద ప్రవాహం సామర్థ్యాన్ని మించవచ్చు; అవక్షేపం నిల్వను తగ్గించి నిర్మాణాన్ని దెబ్బతీయవచ్చు."], "water-harvesting", ["IA05-P297-F07", "IA05-P298-F05"]),
    }
    for qid, (qen, qte, oen, ote, section, facts) in applications.items():
        answer = old[qid]["answer"]
        correct_en = oen[answer - 1]
        correct_te = ote[answer - 1]
        exp_en = [("Correct. " if i == answer else "Incorrect. ") + (correct_en if i == answer else "This does not explain the process; " + correct_en) for i in range(1, 5)]
        exp_te = [("సరైనది. " if i == answer else "తప్పు. ") + (correct_te if i == answer else "ఇది ప్రక్రియను వివరించదు; " + correct_te) for i in range(1, 5)]
        rewritten[qid] = literal_record(old[qid], question_en=qen, question_te=qte, options_en=oen, options_te=ote, option_explanations_en=exp_en, option_explanations_te=exp_te, explanation_en=correct_en, explanation_te=correct_te, section=section, fact_ids=facts, difficulty="hard")

    if set(rewritten) != set(old):
        missing = sorted(set(old) - set(rewritten))
        extra = sorted(set(rewritten) - set(old))
        raise SystemExit(f"Legacy review incomplete. missing={missing}, extra={extra}")
    data["questions"] = [rewritten.get(q["id"], q) for q in data["questions"]]
    BANK.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
