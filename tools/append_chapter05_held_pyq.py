import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "content" / "geography" / "india_ap_chapters" / "5" / "Questions.json"

RECORD = {
    "id": "IA05-HELD-TGPSC-2024-G2-BLACK-SOIL",
    "chapter": "IA-05",
    "origin": "printed-book-pyq",
    "label": "TGPSC 2024 Group-II; printed source only; official final key not yet verified",
    "language": "bilingual",
    "kind": "multiple-statements",
    "difficulty": "moderate",
    "fact_ids": ["IA05-P293-F01"],
    "question_en": "With reference to black soils (Regur) found in India, consider the following statements. a. Black soils form the third-largest major soil group in India. b. Their parent material was derived from Cretaceous-period lava. c. They have a high water-retention capacity. d. They are deficient in iron. Which statements are correct?",
    "question_te": "భారతదేశంలో కనిపించే నల్ల నేలలు—రేగర్ (Regur) గురించి కింది వాక్యాలను పరిశీలించండి. a. నల్ల నేలలు భారతదేశంలోని ప్రధాన నేల సమూహాల్లో మూడవ అతిపెద్ద సమూహం. b. ఇవి క్రెటేషియస్ కాలం (Cretaceous period) నాటి లావా నుంచి మాతృ పదార్థాన్ని పొందాయి. c. ఇవి అధిక నీటి నిల్వ సామర్థ్యం (Water-retention capacity) కలిగి ఉంటాయి. d. వీటిలో ఇనుము (Iron) లోపం ఉంటుంది. సరైన వాక్యాలు ఏవి?",
    "options_en": ["a and c only", "a, b and c only", "b, c and d only", "a, b and d only"],
    "options_te": ["a, c మాత్రమే", "a, b, c మాత్రమే", "b, c, d మాత్రమే", "a, b, d మాత్రమే"],
    "answer": 2,
    "scored": False,
    "answer_status": "held-unverified-official-final-key",
    "option_explanations_en": [
        "This omits statement b, which the printed source treats as correct through the Deccan lava parent-material association.",
        "This is the printed book's keyed combination; it remains unscored until the official final key is verified.",
        "This includes statement d, but black soil is not defined by iron deficiency.",
        "This includes statement d and omits the well-established high water-retention statement c."
    ],
    "option_explanations_te": [
        "ఇది b వాక్యాన్ని వదులుతుంది; దక్కన్ లావా మాతృ పదార్థ సంబంధం ఆధారంగా ముద్రిత మూలం bను సరైనదిగా తీసుకుంది.",
        "ఇది పుస్తకంలో ఇచ్చిన సమాధాన కలయిక; అధికారిక తుది సమాధాన కీ ధృవీకరణ వరకు స్కోరింగ్‌లో ఉండదు.",
        "ఇది dను చేర్చుతుంది; కానీ ఇనుము లోపం నల్ల నేల నిర్వచన లక్షణం కాదు.",
        "ఇది dను చేర్చి, నల్ల నేల అధిక నీటి నిల్వ లక్షణమైన cను వదులుతుంది."
    ],
    "explanation_en": "The book marks option 2. Statements a and c fit the broad textbook classification; b refers to the Deccan lava parent-material association but compresses a long eruption interval into 'Cretaceous'; d is not defensible as a defining property. The item is preserved exactly but held unscored until an official TGPSC paper and final key are opened.",
    "explanation_te": "పుస్తకం 2వ ఎంపికను సూచించింది. a, c వాక్యాలు స్థూల పాఠ్య వర్గీకరణకు సరిపోతాయి. bలో దక్కన్ లావా మాతృ పదార్థ సంబంధాన్ని మొత్తం ‘క్రెటేషియస్’గా సంక్షిప్తం చేశారు. dను నిర్వచన లక్షణంగా సమర్థించలేం. అధికారిక TGPSC ప్రశ్నపత్రం, తుది సమాధాన కీ తెరిచి ధృవీకరించే వరకు ఈ ప్రశ్న స్కోరింగ్‌లో ఉండదు.",
    "section": "printed-pyq-black-soil",
    "related_sections": ["black-formation", "black-properties"],
    "source_paragraph": "Printed page 293 TGPSC 2024 Group-II black-soil statements question; answer 2 is printed by the book.",
    "source_page": 293,
    "source_urls": [],
    "reviewed_on": "2026-11-01",
    "manual_review_status": "held-pending-official-paper-and-final-key"
}


def main() -> None:
    data = json.loads(BANK.read_text(encoding="utf-8"))
    indexes = {question["id"]: index for index, question in enumerate(data["questions"])}
    if RECORD["id"] in indexes:
        data["questions"][indexes[RECORD["id"]]] = RECORD
    else:
        data["questions"].append(RECORD)
    BANK.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
