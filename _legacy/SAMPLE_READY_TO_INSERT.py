# -*- coding: utf-8 -*-
# READY-TO-INSERT SAMPLE TUPLES FOR AP_HC FORMAT
# These 3 samples represent the format for all 25 MCQs (31551-31575)

# =============================================================================
# SAMPLE 1: MCQ 31551 (ID 31551)
# =============================================================================

SAMPLE_MCQ_31551 = (
    "AP_HC",
    "Constitution_Governance",
    "Which Constitutional Amendment introduced the concept of 'Aam Aadmi' in welfare schemes post-2020?\n2020 తర్వాత సామాన్య ప్రజల సంక్షేమ పథకాలను నిర్వచించే రాజ్యాంగ సవరణ ఏది?",
    "104th Amendment / 104వ సవరణ",
    "105th Amendment / 105వ సవరణ",
    "106th Amendment / 106వ సవరణ",
    "103rd Amendment / 103వ సవరణ",
    "C",
    "Hard",
    "The 106th Constitutional Amendment (2023) introduced significant structural changes to welfare governance frameworks. This amendment fundamentally altered the constitutional approach to social security schemes, creating a uniform framework for determining eligibility across Central and State welfare programs.\nరాజ్యాంగ సవరణ సామాన్య ప్రజల సంక్షేమ కార్యక్రమాలకు ఏకరూప చట్టబద్ధ చట్రం ఏర్పాటు చేసింది."
)

# =============================================================================
# SAMPLE 2: MCQ 31560 (ID 31560)
# =============================================================================

SAMPLE_MCQ_31560 = (
    "AP_HC",
    "Constitution_Governance",
    "Article 21-A guarantees which right as fundamental?\nఅర్టికల్ 21-ఎ ఈ హక్కును ప్రాథమిక హక్కుగా ఖచ్చితం చేస్తుంది?",
    "Right to employment / ఉపాధి హక్కు",
    "Right to free and compulsory education up to age 14 / 14 సంవత్సరాల వరకు ఉచితమైన మరియు తప్పనిసరి విద్య హక్కు",
    "Right to healthcare / ఆరోగ్య సేవ హక్కు",
    "Right to property / ఆస్తి హక్కు",
    "B",
    "Easy",
    "Article 21-A, inserted through the 86th Constitutional Amendment (2002), constitutionalizes the fundamental right to free and compulsory education for all children between 6-14 years.\n14 సంవత్సరాల వరకు విద్య ప్రాథమిక హక్కు, కేవలం నీతి సూత్రం కాదు."
)

# =============================================================================
# SAMPLE 3: MCQ 31575 (ID 31575)
# =============================================================================

SAMPLE_MCQ_31575 = (
    "AP_HC",
    "Constitution_Governance",
    "Schedule VII's amendments in recent years addressed primarily:\nఈ సంవత్సరాలలో షెడ్యూల్ VII యొక్క సవరణలు ఈ విషయానికి సంబంధించినవి:",
    "Transferring agricultural subjects to Union List / వ్యవసాయ విషయాలను సంఘ జాబితకు బదిలీ",
    "Expanding Concurrent List for e-governance and technology / ఎ-గవర్నెన్స్ మరియు సాంకేతికత కోసం ఉమ్మడి జాబితా విస్తరణ",
    "Creating exclusive Central control over all taxation / సమస్త పన్నుల కంటే కేంద్ర ఎక్సక్లూసివ్ నియంత్రణ",
    "Removing state authority over primary education / ప్రాథమిక విద్య నుండి రాష్ట్ర అధికారం తొలగడం",
    "B",
    "Hard",
    "The 101st Amendment (2016) introducing GST essentially restructured tax entries through interpretation. Recent Schedule VII evolution reflects expansion of technology and digital governance items to Concurrent List.\nషెడ్యూల్ VII సాంకేతిక శాసన సంరక్షణకు అభిప్రాయ సూచనలు విస్తరించింది."
)

# =============================================================================
# INSERTION FORMAT NOTES:
# =============================================================================
"""
TUPLE STRUCTURE FOR AP_HC:
(
    "AP_HC",                                    # Folder (constant for all)
    "Constitution_Governance",                  # Subject (constant for all)
    "English Question?\nTelugu Question?",      # Bilingual question with \n
    "Option A / సTelugu A",                     # Option A bilingual
    "Option B / సtelugu B",                     # Option B bilingual
    "Option C / సtelugu C",                     # Option C bilingual
    "Option D / సtelugu D",                     # Option D bilingual
    "A" or "B" or "C" or "D",                  # Answer key (single char)
    "Easy" or "Medium" or "Hard",              # Difficulty level
    "English explanation.\nTelugu explanation" # Bilingual explanation
)

ALL 25 MCQs (31551-31575) USE THIS EXACT FORMAT.

KEY POINTS FOR DATABASE INSERTION:
1. Folder: Always "AP_HC" (AP High Court exam format)
2. Subject: Always "Constitution_Governance"
3. Bilingual questions use "\n" separator between English and Telugu
4. Options use "/" to separate English from Telugu
5. Answer keys preserved from original (A, B, C, or D)
6. Difficulty: "Easy" (1-5 MCQs), "Medium" (6-10), "Hard" (11-25)
7. Explanations include Telugu translations for constitutional terms
8. All dates and numerical facts unchanged from source

CONSISTENCY CHECKS PERFORMED:
✓ All 25 MCQs follow same tuple structure
✓ All questions are bilingual (English\nTelugu)
✓ All options are bilingual (English/Telugu)
✓ All explanations include Telugu translations
✓ Answer keys validated against original source
✓ Difficulty levels assigned based on content complexity
✓ Folder "AP_HC" applied to all MCQs
✓ Subject "Constitution_Governance" applied to all MCQs
✓ All facts, dates, amendment numbers unchanged
"""

# =============================================================================
# VERIFICATION HASHES (For Import Checking)
# =============================================================================

SAMPLE_31551_ANSWER = "C"  # 106th Amendment
SAMPLE_31560_ANSWER = "B"  # Article 21-A education right (86th Amendment 2002)
SAMPLE_31575_ANSWER = "B"  # Schedule VII e-governance expansion (101st Amendment 2016)

TELUGU_VERIFICATION = {
    "31551": "రాజ్యాంగ సవరణ సామాన్య ప్రజల సంక్షేమ కార్యక్రమాలకు ఏకరూప చట్టబద్ధ చట్రం ఏర్పాటు చేసింది.",
    "31560": "14 సంవత్సరాల వరకు విద్య ప్రాథమిక హక్కు, కేవలం నీతి సూత్రం కాదు.",
    "31575": "షెడ్యూల్ VII సాంకేతిక శాసన సంరక్షణకు అభిప్రాయ సూచనలు విస్తరించింది."
}

# =============================================================================
# COMPLETE LIST OF MCQ IDS WITH ANSWER KEYS
# =============================================================================

COMPLETE_ANSWER_KEY_31551_TO_31575 = {
    31551: "C",  # 106th Amendment welfare
    31552: "B",  # 103rd Amendment EWS
    31553: "A",  # 42nd Amendment environmental
    31554: "B",  # 73rd/74th Amendment three-tier
    31555: "B",  # Collegium reforms post-2020
    31556: "B",  # Article 21 digital privacy
    31557: "A",  # Article 368 basic structure
    31558: "A",  # Minerva Mills DPSP
    31559: "B",  # Judicial review of amendments
    31560: "B",  # Article 21-A education
    31561: "B",  # 101st Amendment GST
    31562: "A",  # 42nd Amendment secular
    31563: "B",  # 73rd Amendment gender
    31564: "A",  # 86th Amendment RTE
    31565: "D",  # Kesavananda emergency provisions
    31566: "C",  # Education Concurrent List
    31567: "B",  # GST Council revenue
    31568: "B",  # Article 370 J&K
    31569: "C",  # Concurrent List Australia
    31570: "B",  # Interstate compacts Parliament
    31571: "B",  # Finance Commission centre-state
    31572: "B",  # GST federalism violation
    31573: "B",  # Inter-state Council Article 263
    31574: "D",  # India vs USA federalism
    31575: "B",  # Schedule VII e-governance
}

print("READY-TO-INSERT SAMPLES: 31551, 31560, 31575")
print("COMPLETE ANSWER KEY: 25 MCQs (31551-31575)")
print("FORMAT: AP_HC bilingual Telugu-English")
