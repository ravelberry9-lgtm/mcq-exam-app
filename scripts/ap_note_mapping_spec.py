"""Reviewed DRAFT mapping of the 225 AP History note sections (source chapters 1-12) to the canonical structure.

Key: (source chapter, section) -> (canonical chapter number or 'supp-...' slug, subtopic suffix or None, confidence, reason, secondaries)
* subtopic None  = mapped at chapter level (study aid, framework, or no matching subtopic).
* secondaries    = [(canonical chapter number, subtopic suffix or None), ...]
* confidence     = high | medium | low. Anything medium/low, or combining two subtopics, is also listed in the review sheet.
Headings alone were not trusted: the section text was spot-checked for every ambiguous section (see ``reason``).
Sections not listed here are generic study aids (see GENERIC_HEADINGS) and map at chapter level with high confidence.
"""
SUPP = "supp-dynasties-overview"
SUPP_ASAF = "supp-asaf-jahis-hyderabad-state"
SUPP_POST = "supp-post-2014-andhra-pradesh"
SUPP_MODERN = "supp-modern-ap-political-administrative-1956-2014"
MAJORITY = "MAJORITY"   # study aids of a source chapter that spans several canonical chapters follow the chapter receiving most of its substantive sections
DEFAULT_CHAPTER = {1: 2, 2: 1, 3: 3, 4: SUPP, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10, 12: 11,
                   13: 13, 14: SUPP_ASAF, 15: MAJORITY, 16: MAJORITY, 17: MAJORITY, 18: 31, 19: SUPP_POST}
AID = "AID"         # a study-aid section (key sites, key figures, timeline) in a multi-target source chapter

GENERIC_HEADINGS = (
    "Introduction", "Introduction — Why a Three-Dynasty Chapter", "Terminology Primer", "Glossary", "Revision", "MCQs — Practice", "Practice MCQs",
    "Previous Year Question Patterns — APPSC Group 1/2", "Summary & Exam Tips", "Legacy & Chapter Summary", "MCQs",
)
GENERIC_REASON = "Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level."

H, M, L = "high", "medium", "low"
SPEC = {
    # ── source ch1 Prehistoric -> canonical 2 ─────────────────────────
    (1, 3): (2, None, H, "Three-age/periodisation framework spanning all prehistoric periods.", [(2, "tools-technology")]),
    (1, 4): (2, "tools-technology", M, "Movius Line contrasts Acheulian handaxe and chopper-chopping-tool traditions (technology); also a Palaeolithic topic.", [(2, "palaeolithic")]),
    (1, 5): (2, None, L, "Mixes evidence types with pioneer researchers; no single subtopic fits. Ambiguous.", [(1, "archaeological-evidence")]),
    (1, 6): (2, "palaeolithic", H, "Lower Palaeolithic / Acheulian.", []),
    (1, 7): (2, "palaeolithic", H, "Middle Palaeolithic.", []),
    (1, 8): (2, "palaeolithic", H, "Upper Palaeolithic.", []),
    (1, 9): (2, "mesolithic", H, "Mesolithic period.", []),
    (1, 10): (2, "neolithic", H, "Neolithic period and Southern Neolithic complex.", []),
    (1, 11): (2, "megalithic-iron-age", H, "Megalithic / Iron Age culture; burial types also appear here.", [(2, "burial-practices")]),
    (1, 12): (2, "important-sites", H, "District-wise prehistoric sites table.", []),
    (1, 13): (2, None, M, "Researchers of AP prehistory; no researcher subtopic exists.", []),
    (1, 14): (2, None, M, "Recent discoveries across several periods (e.g. Jwalapuram/Toba); multi-period, so chapter level.", [(2, "important-sites")]),
    # ── source ch2 Introduction and sources -> canonical 1 ────────────
    (2, 3): (1, None, H, "Classification tree of all source types; framework for the chapter.", []),
    (2, 4): (1, "literary-sources", H, "Indian literary sources.", []),
    (2, 5): (1, "foreign-accounts", H, "Foreign accounts (Greek, Roman, Chinese).", []),
    (2, 6): (1, "archaeological-evidence", H, "Overview of archaeological sources.", []),
    (2, 7): (1, "inscriptions", H, "Epigraphy.", []),
    (2, 8): (1, "coins", H, "Numismatics.", []),
    (2, 9): (1, "archaeological-evidence", M, "Monuments and sculpture as physical evidence.", [(1, "important-sites")]),
    (2, 10): (1, "people-name-origin", H, "Name and origin of the Andhras: five theories.", []),
    (2, 11): (1, "people-name-origin", M, "Chronological list of earliest references to Andhras; overlaps Chapter 3 'Early Andhra references'. Ambiguous.", [(3, "early-andhra-references")]),
    (2, 12): (1, "telugu-identity-language", H, "Origin of Telugu / Andhra language.", []),
    (2, 13): (1, "people-name-origin", L, "Pre-Aryan tribal background (Andhra, Pundra, Shabara); ancient ethnography, not Chapter 26's modern tribal culture. Ambiguous.", []),
    (2, 14): (1, "important-sites", H, "District-wise historical-source sites.", []),
    (2, 15): (1, "archaeological-evidence", M, "Recent excavations and discoveries 2018-2026.", [(1, "important-sites")]),
    # ── source ch3 Pre-Satavahana -> canonical 3 ──────────────────────
    (3, 3): (3, None, H, "Chronological framework for the whole chapter.", []),
    (3, 4): (3, "early-andhra-references", H, "Andhra identity in early literature.", [(1, "people-name-origin")]),
    (3, 5): (3, None, M, "Sources for the period; overlaps Chapter 1 sources.", [(1, "literary-sources"), (1, "inscriptions")]),
    (3, 6): (3, "assaka-asmaka", H, "Assaka Mahajanapada.", []),
    (3, 7): (3, "assaka-asmaka", M, "Mulaka is paired with Assaka in the sources; no separate subtopic. Propose adding one. Ambiguous.", []),
    (3, 8): (3, "nandas-mauryas", H, "Mauryan rule in Andhra; Ashokan edicts are covered here.", [(3, "ashoka-inscriptions"), (3, "erragudi-rajulamandagiri")]),
    (3, 9): (3, "early-andhra-references", M, "Megasthenes' Indica on the Andhras; also a foreign account.", [(1, "foreign-accounts")]),
    (3, 10): (3, "bhattiprolu", H, "Bhattiprolu / Kuberaka kingdom.", [(3, "early-local-rulers")]),
    (3, 11): (3, "early-local-rulers", M, "Post-Mauryan transition, c. 232-200 BCE.", [(3, "nandas-mauryas")]),
    (3, 12): (3, "early-buddhism", H, "Early Buddhist sites in Andhra.", [(3, "amaravati-dhanyakataka-beginnings")]),
    (3, 13): (3, None, M, "Society, economy and religion together; no matching subtopic.", []),
    (3, 14): (3, None, H, "District-wise pre-Satavahana sites.", [(1, "important-sites")]),
    (3, 15): (3, None, M, "Historical figures and researchers.", []),
    # ── source ch4 Dynasties overview -> supplementary reference ──────
    (4, 2): (SUPP, None, H, "Master table of all dynasties; cross-cutting reference.", []),
    (4, 3): (SUPP, None, H, "Master chronology diagram.", []),
    (4, 4): (SUPP, None, H, "Dynasty succession tree.", []),
    (4, 5): (SUPP, None, H, "Capital cities map; some capitals lie outside present AP.", []),
    (4, 6): (SUPP, None, H, "Greatest king of each dynasty.", []),
    (4, 7): (SUPP, None, H, "'Firsts' in Andhra history.", []),
    (4, 8): (SUPP, None, M, "Religious patronage by dynasty across all periods; only part falls in 11th-16th c.", [(14, "religious-movements")]),
    (4, 9): (SUPP, None, M, "Telugu literature growth timeline across periods.", [(1, "telugu-identity-language"), (14, "growth-of-telugu")]),
    (4, 10): (SUPP, None, H, "King mnemonics.", []),
    (4, 11): (SUPP, None, M, "Key inscriptions reference across dynasties.", [(1, "inscriptions")]),
    (4, 12): (SUPP, None, H, "Complete king lists.", []),
    # ── source ch5 Satavahanas -> canonical 4 ─────────────────────────
    (5, 3): (4, "chronology", H, "Satavahana chronology.", []),
    (5, 4): (4, "origin-homeland", H, "Origin debate.", []),
    (5, 5): (4, "political-history", M, "The capital debate (Pratishthana / Dhanyakataka); no capital subtopic. Ambiguous.", [(4, "origin-homeland")]),
    (5, 6): (4, None, M, "Sources of Satavahana history (literary, inscriptions, coins).", [(4, "inscriptions"), (4, "coinage")]),
    (5, 7): (4, "political-history", H, "Foundation phase under the early Satavahanas.", [(4, "important-rulers")]),
    (5, 8): (4, "important-rulers", H, "Other notable kings.", []),
    (5, 9): (4, "important-rulers", H, "Gautamiputra Satakarni.", [(4, "political-history")]),
    (5, 10): (4, "inscriptions", H, "Key Satavahana inscriptions.", []),
    (5, 11): (4, "political-history", H, "Territorial extent of the empire.", []),
    (5, 12): (4, "coinage", H, "Satavahana coinage.", []),
    (5, 13): (4, "society", M, "Society and economy in one section; should be split at content level. Ambiguous.", [(4, "economy-trade")]),
    (5, 14): (4, "religion", H, "Religion under the Satavahanas.", []),
    (5, 15): (4, "art-architecture", M, "Art and literature in one section; should be split. Ambiguous.", [(4, "literature")]),
    (5, 16): (4, None, H, "District-wise Satavahana sites.", [(1, "important-sites")]),
    (5, 17): (4, None, M, "Key figures and researchers.", []),
    # ── source ch6 Ikshvakus -> canonical 5 ───────────────────────────
    (6, 3): (5, "origin-chronology", H, "Origins; Suryavamsha claim.", []),
    (6, 4): (5, "vijayapuri-nagarjunakonda", H, "Capital Vijayapuri.", []),
    (6, 5): (5, None, M, "Historical sources of the Ikshvakus.", [(5, "inscriptions")]),
    (6, 6): (5, "important-rulers", H, "The four kings.", []),
    (6, 7): (5, "important-rulers", H, "Founder, Chamtamula I.", [(5, "origin-chronology")]),
    (6, 8): (5, "important-rulers", H, "Greatest king, Virapurushadatta.", []),
    (6, 9): (5, "important-rulers", H, "Ehuvula Chamtamula II, temple builder.", [(5, "brahmanism")]),
    (6, 10): (5, "important-rulers", H, "Last king, Rudrapurushadatta.", [(5, "decline")]),
    (6, 11): (5, "inscriptions", H, "Ikshvaku inscriptions.", []),
    (6, 12): (5, "royal-women", H, "Queens as Buddhist patrons.", [(5, "buddhism")]),
    (6, 13): (5, "administration", H, "Administration.", []),
    (6, 14): (5, "socio-economic-conditions", H, "Society and economy.", []),
    (6, 15): (5, "buddhism", M, "Dual Buddhist/Brahmanical religious structure in one section. Ambiguous.", [(5, "brahmanism")]),
    (6, 16): (5, "vijayapuri-nagarjunakonda", H, "Vijayapuri city plan.", []),
    (6, 17): (5, "art-architecture", M, "The Great Stupa (Mahachaitya) at Nagarjunakonda.", [(5, "vijayapuri-nagarjunakonda"), (5, "buddhism")]),
    (6, 18): (5, "art-architecture", H, "Ikshvaku art, 'Later Amaravati' style.", []),
    (6, 19): (5, None, H, "Ikshvaku sites in AP.", [(1, "important-sites")]),
    (6, 20): (5, "decline", H, "Decline and successors.", []),
    # ── source ch7 Minor dynasties -> canonical 6 ─────────────────────
    (7, 3): (6, None, H, "Comparative overview of the three dynasties.", []),
    (7, 4): (6, "brihatphalayanas", H, "Brihatphalayanas.", []),
    (7, 5): (6, "ananda-gotrikas", H, "Anandagotras.", []),
    (7, 6): (6, "art-architecture", M, "Chejarla Kapoteshvara apsidal temple, discussed under the Ananda Gotra.", [(6, "ananda-gotrikas")]),
    (7, 7): (6, "salankayanas", H, "Salankayanas: introduction and founder.", []),
    (7, 8): (6, "salankayanas", H, "Hastivarman and Samudragupta's southern campaign (Allahabad pillar).", [(6, "political-conditions")]),
    (7, 9): (6, "salankayanas", H, "Later Salankayana kings.", []),
    (7, 10): (6, "salankayanas", M, "Vengi (Pedavegi) as Salankayana capital: the primary topic. The secondary Chapter 8 link is kept only because section 10.2 itself discusses the later Eastern Chalukya period (a table of Vengi's c. 624-1130 CE role); the shared place name alone would not justify it.", [(8, "vengi-foundation")]),
    (7, 11): (6, "religion", H, "Salankayana religion, Shaiva to Vaishnava.", []),
    (7, 12): (6, "religion", M, "Bull seal and tutelary deity Chitrarathasvamin; religion and emblem together.", [(6, "salankayanas")]),
    (7, 13): (6, "inscriptions", M, "Prakrit-to-Sanskrit language shift traced through copper plates.", [(7, "sanskrit-telugu-development")]),
    (7, 14): (6, "religion", H, "Buddhism to Brahmanism transformation.", []),
    (7, 15): (6, None, H, "Sites map of the three dynasties.", [(1, "important-sites")]),
    (7, 16): (6, "political-conditions", M, "Bridge to the Vishnukundins: fate of each dynasty.", [(7, "origin-chronology")]),
    # ── source ch8 Vishnukundins -> canonical 7 ───────────────────────
    (8, 3): (7, "origin-chronology", H, "Origin and name.", []),
    (8, 4): (7, "political-expansion", M, "Four capitals; no capitals subtopic. Ambiguous.", [(7, "origin-chronology")]),
    (8, 5): (7, None, M, "Historical sources.", [(7, "inscriptions")]),
    (8, 6): (7, "origin-chronology", H, "Dynasty chronology.", []),
    (8, 7): (7, "important-rulers", H, "Early kings Madhavavarman I and Govindavarman I.", []),
    (8, 8): (7, "important-rulers", H, "Madhavavarman II, eleven Ashvamedhas.", [(7, "political-expansion")]),
    (8, 9): (7, "political-expansion", M, "Vakataka marriage alliance.", [(7, "important-rulers")]),
    (8, 10): (7, "important-rulers", H, "Later kings.", []),
    (8, 11): (7, "religion", H, "Religion.", []),
    (8, 12): (7, "inscriptions", H, "Tummalagudem plates.", []),
    (8, 13): (7, "inscriptions", H, "Chikkulla and Polamuru plates.", []),
    (8, 14): (7, "cave-temple-architecture", H, "Undavalli caves.", []),
    (8, 15): (7, "cave-temple-architecture", H, "Mogalrajapuram and Bhairavakonda caves.", []),
    (8, 16): (7, "sanskrit-telugu-development", H, "Literature; Janashrayi Chandovichiti.", []),
    (8, 17): (7, "coins", H, "Coinage and lion emblem.", []),
    (8, 18): (7, None, H, "Vishnukundin sites in AP.", [(1, "important-sites")]),
    (8, 19): (7, "decline", H, "Chalukya conquest and decline.", []),
    (8, 20): (7, "decline", M, "Bridge to the Eastern Chalukyas.", [(8, "vengi-foundation")]),
    # ── source ch9 Eastern Chalukyas -> canonical 8 ───────────────────
    (9, 3): (8, "vengi-foundation", H, "Founding of the dynasty; why 624.", []),
    (9, 4): (8, "vengi-foundation", M, "Three capitals; no capitals subtopic.", []),
    (9, 5): (8, None, M, "Historical sources.", [(8, "inscriptions")]),
    (9, 6): (8, "political-chronology", H, "30 kings over 500 years.", []),
    (9, 7): (8, "important-rulers", H, "Kubja Vishnuvardhana.", [(8, "vengi-foundation")]),
    (9, 8): (8, "important-rulers", H, "Vijayaditya II.", []),
    (9, 9): (8, "important-rulers", H, "Gunaga Vijayaditya III.", []),
    (9, 10): (8, "important-rulers", H, "Chalukya Bhima I, Pancharama builder.", [(8, "temples-pancharamas")]),
    (9, 11): (8, "important-rulers", H, "Amma II.", []),
    (9, 12): (8, "important-rulers", H, "Vimaladitya, Jain patron.", [(8, "religion")]),
    (9, 13): (8, "important-rulers", H, "Rajaraja Narendra.", [(8, "telugu-nannaya-literature")]),
    (9, 14): (8, "telugu-nannaya-literature", H, "Nannaya and the Andhra Mahabharatam.", [(1, "telugu-identity-language")]),
    (9, 15): (8, "temples-pancharamas", H, "Pancharama kshetras.", []),
    (9, 16): (8, "art-architecture", H, "General Eastern Chalukya art and architecture; mapped to the general subtopic, not forced into Pancharamas.", [(8, "temples-pancharamas")]),
    (9, 17): (8, "religion", M, "Religion and administration in one section. Ambiguous.", [(8, "administration")]),
    (9, 18): (8, None, H, "Eastern Chalukya sites.", [(1, "important-sites")]),
    (9, 19): (8, "chola-chalukya-relations", H, "Kulottunga I and the Chola merger.", []),
    (9, 20): (8, "decline-transition", H, "End of the dynasty; Velanati Chodas rise in the last phase.", [(8, "velanati-chodas")]),
    # ── source ch10 Kakatiyas -> canonical 9 ──────────────────────────
    (10, 3): (9, "origin-early-rulers", H, "Origins and founding.", []),
    (10, 4): (9, "political-expansion", M, "Three capitals; no capitals subtopic.", []),
    (10, 5): (9, None, M, "Historical sources.", []),
    (10, 6): (9, None, H, "Table of the five sovereigns; whole-dynasty overview.", []),
    (10, 7): (9, "rudradeva", H, "Rudradeva (Prataparudra I).", []),
    (10, 8): (9, "mahadeva", H, "Mahadeva.", []),
    (10, 9): (9, "ganapatideva", H, "Ganapati Deva.", []),
    (10, 10): (9, "rudramadevi", H, "Rudrama Devi.", []),
    (10, 11): (9, "prataparudra", H, "Prataparudra II.", [(9, "delhi-sultanate-invasions")]),
    (10, 12): (9, "art-architecture", H, "Thousand Pillar Temple.", []),
    (10, 13): (9, "art-architecture", H, "Warangal Fort and Kakatiya Thoranam.", []),
    (10, 14): (9, "art-architecture", H, "Ramappa temple.", []),
    (10, 15): (9, "telugu-literature", M, "Literature and arts together. Ambiguous.", [(9, "dance-music"), (9, "art-architecture")]),
    (10, 16): (9, "administration-nayankara", H, "Nayankara system and administration.", []),
    (10, 17): (9, "crafts-trade-motupalli", H, "Economy and Motupalli Abhayasasana.", [(9, "irrigation-agriculture")]),
    (10, 18): (9, "religion", M, "Religion and social history together. Ambiguous.", [(9, "society")]),
    (10, 19): (9, None, H, "Kakatiya sites in AP.", []),
    (10, 20): (9, "delhi-sultanate-invasions", H, "The five sieges, 1303-1323.", [(9, "decline")]),
    # ── source ch11 Reddys, Musunuris -> canonical 10 ─────────────────
    (11, 3): (10, "post-kakatiya-conditions", H, "Post-Kakatiya vacuum, 1323-1336.", []),
    (11, 4): (10, None, H, "Comparison of the three successor dynasties.", []),
    (11, 5): (10, None, M, "Historical sources.", []),
    (11, 6): (10, "musunuri-nayakas", H, "Musunuri Nayakas overview.", []),
    (11, 7): (10, "musunuri-nayakas", H, "Prolaya and Kapaya Nayaka.", []),
    (11, 8): (10, "kondavidu-reddys", H, "Kondaveedu Reddi overview.", []),
    (11, 9): (10, "kondavidu-reddys", H, "Prolaya Vema Reddi.", []),
    (11, 10): (10, "kondavidu-reddys", H, "Anavema, Komati Vema and Pedakomati Vema.", []),
    (11, 11): (10, "rajahmundry-reddys", H, "Rajamahendravaram Reddi branch.", []),
    (11, 12): (10, "rajahmundry-reddys", M, "Provisionally placed under Rajahmundry Reddys (the section title's placement).", []),
    (11, 13): (10, "recharla-velamas", H, "Recharla Velamas of Rachakonda and Devarakonda.", []),
    (11, 14): (10, "telugu-literature", H, "Srinatha.", [(14, "authors-works")]),
    (11, 15): (10, "telugu-literature", H, "Other literary figures.", [(14, "authors-works")]),
    (11, 16): (10, "art-architecture", H, "Forts and monuments.", [(14, "forts")]),
    (11, 17): (10, "administration", M, "Administration and economy together. Ambiguous.", [(10, "society-economy")]),
    (11, 18): (10, "religion", M, "Religion and social history together. Ambiguous.", [(10, "society-economy")]),
    (11, 19): (10, None, H, "Sites in AP.", []),
    (11, 20): (10, "regional-conflicts", M, "Decline through Vijayanagara and Gajapati conquests.", [(12, "gajapati-rule-influence")]),
    # ── source ch12 Vijayanagara -> canonical 11 ──────────────────────
    (12, 3): (11, "foundation", H, "Foundation and the Vidyaranya debate.", []),
    (12, 4): (11, "four-dynasties", H, "Four dynasties overview.", []),
    (12, 5): (11, None, M, "Historical sources.", []),
    (12, 6): (11, "four-dynasties", M, "The Sangama dynasty.", [(11, "important-rulers")]),
    (12, 7): (11, "important-rulers", H, "Devaraya I and II.", []),
    (12, 8): (11, "four-dynasties", H, "Saluva and Tuluva transitions.", [(11, "important-rulers")]),
    (12, 9): (11, "krishnadevaraya", H, "Krishnadevaraya as emperor.", []),
    (12, 10): (11, "andhra-campaigns-gajapati-bahmani", H, "Krishnadevaraya's campaigns.", [(11, "krishnadevaraya"), (12, "gajapati-rule-influence")]),
    (12, 11): (11, "telugu-literature-ashtadiggajas", H, "Amuktamalyada and the Ashtadiggajas.", [(14, "authors-works")]),
    (12, 12): (11, "important-rulers", H, "Achyutadevaraya, Sadashiva and Aliya Ramaraya.", [(11, "four-dynasties")]),
    (12, 13): (11, "battle-of-talikota", H, "Battle of Talikota, 1565.", []),
    (12, 14): (11, "decline", M, "Aravidu dynasty and AP-located capitals after 1565.", [(11, "four-dynasties")]),
    (12, 15): (11, "art-architecture", H, "Hampi monuments.", []),
    (12, 16): (11, "administration-nayankara", M, "Administration and economy together. Ambiguous.", [(11, "economy-trade")]),
    (12, 17): (11, "religion", H, "Religion and the Wagoner 'Hindu Sultanate' thesis.", []),
    (12, 18): (11, "telugu-literature-ashtadiggajas", M, "Literature and arts together. Ambiguous.", [(11, "art-architecture")]),
    (12, 19): (11, None, H, "Vijayanagara sites in AP.", []),
    (12, 20): (11, "decline", H, "Decline and successor states.", []),
}

# ── source chapters 13-19 (local HTML files, not in the app database) ───────────
SPEC.update({
    # source ch13 Qutb Shahis -> canonical 13
    (13, 3): (13, "establishment", M, "Bahmani background, the five Deccan sultanates, Golconda fort and Sultan Quli's founding in one long section.", [(12, "bahmani-vijayanagara-rivalry")]),
    (13, 4): (13, "sixteenth-century-rulers", M, "Lists all eight Qutb Shahi rulers, 1518-1687; only the first reigns fall in the 16th century.", []),
    (13, 5): (13, "sixteenth-century-rulers", H, "Ibrahim Quli (1550-80): Vijayanagara exile, Golconda reforms and his role at Talikota (1565).", [(11, "battle-of-talikota")]),
    (13, 6): (13, "sixteenth-century-rulers", M, "Muhammad Quli (1580-1612): founding of Hyderabad (1591), poetry, administration; the reign runs past 1600.", [(13, "telugu-dakhni-patronage"), (13, "art-architecture")]),
    (13, 7): (13, "art-architecture", H, "Charminar, 1591.", []),
    (13, 8): (13, "art-architecture", M, "Planning of Hyderabad city (1591).", []),
    (13, 9): (13, "art-architecture", M, "Mecca Masjid (completed well after the 16th century) and other monuments; supporting context.", []),
    (13, 10): (13, "art-architecture", M, "Qutb Shahi tombs, mostly 17th-century construction; supporting context.", []),
    (13, 11): (13, "administration", M, "Central and provincial administration, economy, Golconda diamonds and merchant guilds in one section.", [(13, "society-economy"), (13, "trade-ports-golconda")]),
    (13, 12): (13, "religion", H, "Religious tolerance; the Hindu ministers Akkanna and Madanna (17th century) and their murder; Hindu-Muslim harmony.", []),
    (13, 13): (13, "telugu-dakhni-patronage", H, "Telugu literature and Dakhni under Qutb Shahi patronage.", []),
    (13, 14): (13, None, M, "Decline and Mughal annexation, 1636-1687: after the official 11th-16th century boundary; supporting context.", []),
    (13, 15): (13, None, M, "Legacy and AP sites table; mostly 17th-century context.", []),
    # source ch14 Asaf Jahis -> supplementary reference (secondary links only where the content justifies them)
    (14, 3): (SUPP_ASAF, None, H, "Mughal Hyderabad Suba, 1687-1724.", []),
    (14, 4): (SUPP_ASAF, None, H, "Asaf Jah I and the founding of the dynasty.", []),
    (14, 5): (SUPP_ASAF, None, H, "The seven Nizams.", []),
    (14, 6): (SUPP_ASAF, None, H, "British-Nizam relations.", []),
    (14, 7): (SUPP_ASAF, None, H, "Salar Jung I's reforms.", []),
    (14, 8): (SUPP_ASAF, None, H, "Education, culture, architecture and the arts under the Nizams (1908-1948); the period precedes Chapter 31's 1956-2014 span, so no secondary link.", []),
    (14, 9): (SUPP_ASAF, None, H, "Mir Osman Ali Khan, the last Nizam.", []),
    (14, 10): (SUPP_ASAF, None, H, "Razakar movement, 1938-1948. Hyderabad's 1948 integration into India is not the 1956 formation of Andhra Pradesh, so no formation-chapter link is added.", []),
    (14, 11): (SUPP_ASAF, None, H, "Operation Polo and the merger of Hyderabad into India (1948); no formation-chapter link added, for the same reason.", []),
    (14, 12): (SUPP_ASAF, None, H, "Telangana armed struggle 1946-51: a Communist-led peasant revolt against jagirdars, doras and Razakar violence; its content matches Chapter 20.", [(20, "communist-movement"), (20, "regional-agrarian-struggles")]),
    (14, 13): (SUPP_ASAF, None, H, "Economy and society of Hyderabad State.", []),
    (14, 14): (SUPP_ASAF, None, H, "Key sites (AP and Telangana).", []),
    (14, 15): (SUPP_ASAF, None, H, "Key historical figures.", []),
    # source ch15 British coastal Andhra -> canonical 15-17 by section content
    (15, 3): (15, "trading-centres-ports", M, "Late Mughal decline 1687-1740, European settlements on the Andhra coast, and why the British won.", [(15, "european-rivalries")]),
    (15, 4): (15, "european-rivalries", H, "Carnatic Wars, 1746-1763.", []),
    (15, 5): (15, "northern-circars", H, "Cession of the Northern Circars, 1766.", []),
    (15, 6): (15, "ceded-districts", H, "Ceded Districts, 1800.", []),
    (15, 7): (16, "consolidation-of-administration", M, "Madras Presidency: its formation, administrative order to 1858 and Andhra districts by 1857.", [(15, "company-administration")]),
    (15, 8): (16, "thomas-munro", M, "Munro's career and the ryotwari system in one section.", [(16, "zamindari-ryotwari"), (15, "revenue-systems")]),
    (15, 9): (16, "arthur-cotton", H, "Arthur Cotton and irrigation.", []),
    (15, 10): (16, "zamindari-ryotwari", M, "Vizianagaram Pusapati line, Bobbili (1757), Padmanabham (1794), other zamindaris.", [(15, "northern-circars")]),
    (15, 11): (16, "impact-of-1857", M, "1857 in Madras Presidency (limited impact), the 1879 Rampa rebellion and other minor uprisings.", [(16, "revolt-of-1857"), (26, "tribal-resistance")]),
    (15, 12): (17, "western-education", M, "English education, social reform movements and print/Telugu renaissance in one section.", [(17, "social-reform"), (17, "print-culture"), (17, "modern-telugu-awakening")]),
    (15, 13): (16, "administrative-economic-effects", M, "Agriculture, trade, railways and the 1876-78 famine.", [(15, "early-economic-social-impact")]),
    (15, 14): (AID, None, M, "Key sites table spanning the source chapter.", []),
    # source ch16 Freedom movement -> canonical 17-22 (and 23-27) by section content
    (16, 3): (19, "congress-and-andhra", M, "Founding of the INC (1885), partition of Bengal (1905) and the Andhra response, Surat split (1907).", [(19, "swadeshi-vandemataram")]),
    (16, 4): (23, "demand-for-andhra-province", M, "Andhra Movement from 1913: Tamil dominance in administration and jobs and the push for a separate province.", [(23, "linguistic-identity-roots"), (23, "important-conferences")]),
    (16, 5): (19, "non-cooperation", H, "Non-Cooperation 1920-22, including Duggirala Gopalakrishnayya and Chauri Chaura.", []),
    (16, 6): (19, "rampa-rebellion", M, "Rampa Rebellion 1922-24 (Alluri Sitarama Raju): an anti-colonial armed tribal uprising of the nationalist period, so primary is Chapter 19 (microtopic rampa-rebellion). Chapter 26 is secondary tribal context only; it is about folk and tribal culture, not a container for every tribal rebellion. Decision: reviewer, 2026-10-04.", [(26, "tribal-resistance")]),
    (16, 7): (24, "origin-sessions", H, "Andhra Mahasabha (Telangana) from 1928: Telugu language and culture under Nizam rule.", []),
    (16, 8): (19, "civil-disobedience-salt-satyagraha", H, "Simon Commission protest, Prakasam, Salt Satyagraha (1930), Gandhi-Irwin Pact.", []),
    (16, 9): (23, "sri-bagh-pact", H, "Sri Bagh Pact.", []),
    (16, 10): (19, "quit-india", H, "Quit India Movement, 1942.", []),
    (16, 11): (SUPP_ASAF, None, M, "Komaram Bheem (1901-40): Gond armed movement in princely Hyderabad State against Asaf Jahi administration (Jodeghat, 1940), concerning Gond land, forest and 'jal, jangal, jameen' rights; primary is the supplementary Asaf Jahi / Hyderabad State chapter. Chapter 26 is secondary for Gond culture and social setting. Secondary Chapter 19 (regional-centres-events) is justified by subsection 11.5, which covers other Hyderabad State freedom leaders (Shoebullah Khan, Swami Ramananda Tirtha, Kaloji, Dasarathi). Not presented as an event of the Andhra Movement. Decision: reviewer, 2026-10-04.", [(26, "major-tribal-communities"), (19, "regional-centres-events")]),
    (16, 12): (19, "prominent-leaders", M, "Comprehensive list of freedom-movement leaders.", [(24, "major-leaders")]),
    (16, 13): (27, "fast-and-death", H, "Potti Sriramulu's fast and death, 1952.", [(27, "potti-sriramulu")]),
    (16, 14): (27, "formation-of-andhra-state", H, "Formation of Andhra State, 1953.", []),
    (16, 15): (17, None, M, "Umbrella section on socio-cultural and ideological currents with seven subsections: Justice Party/Self-Respect, left and Communist movements, anti-zamindari and Kisan movements, poetry and revolutionary literature, Nataka Samasthalu, women, reform and press.",
               [(18, "justice-party"), (20, "communist-movement"), (20, "anti-zamindari-struggles"), (21, "nationalist-poetry"), (21, "nataka-samasthalu"), (22, None), (17, "social-reform"), (25, "press-political-mobilisation")]),
    # source ch17 Andhra State + AP formation -> canonical 25-30 by section content
    (17, 3): (28, "andhra-telangana-merger-debate", L, "Hyderabad State 1948-56 (military governor, Vellodi, Burgula, the 1952 election and Mulki agitation): background to the Telangana merger question. Ambiguous.", [(SUPP_ASAF, None), (30, "regional-safeguards")]),
    (17, 4): (27, "formation-of-andhra-state", H, "Andhra State: context, formation, Bellary dispute, Sri Bagh Pact and the choice of Kurnool.", [(27, "kurnool-capital"), (23, "sri-bagh-pact")]),
    (17, 5): (27, "tanguturi-prakasam", M, "Prakasam and B. Gopala Reddy as Andhra State chief ministers.", [(27, "consequences")]),
    (17, 6): (29, "formation-members", H, "States Reorganisation Commission (Fazl Ali), 1953-55.", [(29, "terms-of-reference")]),
    (17, 7): (29, "recommendations", H, "SRC recommendations, 1955.", []),
    (17, 8): (28, "andhra-telangana-merger-debate", M, "Visalandhra Mahasabha and idea, Andhra-side arguments, Telangana-side opposition, leaders' views.", [(28, "visalandhra-mahasabha"), (28, "linguistic-political-arguments"), (28, "supporters-opponents")]),
    (17, 9): (30, "provisions", H, "Gentlemen's Agreement: context, eight signatories, fourteen points and significance.", [(30, "signatories"), (30, "negotiations"), (30, "long-term-significance")]),
    (17, 10): (30, "formation-1-november-1956", H, "Formation of Andhra Pradesh, 1 November 1956.", []),
    (17, 11): (30, "regional-safeguards", M, "Mulki rules: origin, continuation under the Gentlemen's Agreement, Supreme Court rulings.", []),
    (17, 12): (25, None, M, "Press, Library Movement, folk arts and tribal culture as the cultural base of the Andhra Movement (four subsections).", [(25, "library-movement"), (25, "press-political-mobilisation"), (26, "folk-traditions"), (26, "major-tribal-communities"), (23, "political-cultural-dimensions")]),
    (17, 13): (AID, None, M, "Key figures of 1948-56 across the source chapter.", []),
    (17, 14): (AID, None, M, "Key sites across the source chapter.", []),
    (17, 15): (AID, None, M, "Timeline graphic for 1948-56.", []),
    # source ch18 Modern AP 1956-2014 -> canonical 31 (political sections are outside the stated 'social and cultural' scope)
    (18, 3): (31, "mulki-rules", M, "Chief ministers 1956-67 (Sanjiva Reddy, Sanjivaiah, Brahmananda Reddy): these sections are not merely routine chronology. Section 3 covers implementation of the Gentlemen's Agreement, the regional council and continued Mulki protections (3.1), which directly affected regional safeguards, public employment and Andhra-Telangana relations after state formation, so Chapter 31 is primary (decision: reviewer, 2026-10-04). Ordinary chief-minister chronology in the section is secondary supplementary context. Mixed.", [(SUPP_MODERN, None), (30, "implementation-issues")]),
    (18, 4): (31, "telangana-movement-1969", H, "1969 Jai Telangana agitation.", []),
    (18, 5): (31, "jai-andhra-1972", H, "1972-73 Jai Andhra agitation.", []),
    (18, 6): (31, "regional-identity-movements", M, "Six-Point Formula (1973), Article 371-D and G.O. 610: the settlement of the 1969-73 agitations.", [(31, "telangana-movement-1969"), (31, "jai-andhra-1972"), (30, "regional-safeguards")]),
    (18, 7): (31, "regional-identity-movements", M, "Chief ministers 1973-82: implementation of the Six-Point Formula after the 1969-73 agitations (7.1) shaped regional safeguards, public employment and regional identity, so Chapter 31 is primary (decision: reviewer, 2026-10-04); ordinary chief-minister and government chronology is secondary supplementary context. Mixed.", [(SUPP_MODERN, None)]),
    (18, 8): (SUPP_MODERN, None, H, "NTR and the founding of the TDP, 1982-83: party and electoral history; no demonstrated social-cultural significance in this section, so supplementary political-administrative context.", []),
    (18, 9): (31, "mulki-rules", M, "NTR's three terms: the Jayabharat Reddy committee on Article 371-D violations and G.O. 610 (9.1) concern regional-employment safeguards and Andhra-Telangana relations, so Chapter 31 is primary (decision: reviewer, 2026-10-04); NTR's party and government chronology is secondary supplementary context. Mixed.", [(SUPP_MODERN, None)]),
    (18, 10): (SUPP_MODERN, None, H, "Naidu's IT era, 1995-2004: governance and economic-policy chronology; supplementary political-administrative context.", []),
    (18, 11): (SUPP_MODERN, None, H, "YSR welfare era, 2004-09: governance chronology; supplementary political-administrative context.", []),
    (18, 12): (31, "regional-identity-movements", H, "Telangana movement, 2001-2014.", []),
    (18, 13): (31, "regional-identity-movements", M, "2014 bifurcation overview: the culmination of the regional-identity movements, so Chapter 31 is primary; the post-2014 consequences it summarises are kept as a secondary link to the supplementary post-2014 chapter. Mixed.", [(SUPP_POST, None)]),
    (18, 14): (31, "cultural-developments-to-2014", H, "Literature, cinema and press, social and Dalit movements, Naxalite movement, education, language and cultural identity.", [(31, "literature"), (31, "cinema"), (31, "dalit-social-movements"), (31, "education-universities"), (31, "official-language-telugu")]),
    (18, 15): (SUPP_MODERN, None, H, "Irrigation and IT projects: development and administrative history; supplementary political-administrative context.", []),
    (18, 16): (SUPP_MODERN, None, H, "Reference table of chief ministers, 1956-2014: routine chronology; supplementary political-administrative context.", []),
    (18, 17): (31, None, H, "Key sites.", []),
    # source ch19 Bifurcation and post-2014 -> supplementary post-syllabus reference
    (19, 3): (SUPP_POST, None, H, "AP Reorganisation Act 2014; the Act is the outcome of the 2001-14 Telangana movement mapped in Chapter 31.", [(31, "regional-identity-movements")]),
    (19, 4): (SUPP_POST, None, H, "Post-bifurcation AP.", []),
    (19, 5): (SUPP_POST, None, H, "Naidu's term 2014-19.", []),
    (19, 6): (SUPP_POST, None, H, "Amaravati capital plan.", []),
    (19, 7): (SUPP_POST, None, H, "Jagan's tenure 2019-24.", []),
    (19, 8): (SUPP_POST, None, H, "Three-capitals controversy.", []),
    (19, 9): (SUPP_POST, None, H, "2022 district reorganisation.", []),
    (19, 10): (SUPP_POST, None, H, "2024 elections.", []),
    (19, 11): (SUPP_POST, None, H, "Telangana and AP over ten years.", []),
    (19, 12): (SUPP_POST, None, H, "Key development projects.", []),
    (19, 13): (SUPP_POST, None, H, "Recent chief ministers.", []),
    (19, 14): (SUPP_POST, None, H, "Key sites.", []),
})

# Flags (a section may carry several, separated by ';'): multi_topic, scope_boundary, content_review, attribution_check.
# 'ambiguous' is added automatically from the reason text.
FLAGS = {k: "multi_topic" for k in [
    (1, 14), (3, 13), (5, 13), (5, 15), (6, 15), (7, 12), (9, 17), (10, 15), (10, 18), (11, 17), (11, 18), (12, 16), (12, 18),
    (13, 3), (13, 6), (13, 11), (15, 3), (15, 8), (15, 10), (15, 11), (15, 12), (15, 13), (16, 3), (16, 4), (16, 8), (16, 11), (16, 15),
    (17, 3), (17, 4), (17, 5), (17, 8), (17, 9), (17, 12), (18, 6), (18, 14)]}
for k in [(13, 4), (13, 6), (13, 9), (13, 10), (13, 12), (13, 14), (13, 15), (18, 3), (18, 7), (18, 9), (18, 13)]:
    FLAGS[k] = (FLAGS.get(k, "") + ";scope_boundary").lstrip(";")
for k in [(1, 5), (2, 13)]:
    FLAGS[k] = "content_review"
FLAGS[(11, 12)] = "attribution_check"

# Rows that must stay unapproved until a content reviewer confirms them. approval_status 'unapproved' + the reason.
UNAPPROVED = {
    (11, 12): "Kataya Vema attribution unresolved. The section heading calls Kataya Vema and Vira Bhadra the *last* kings of Rajamahendravaram, "
              "but the body (12.1) calls Kataya Vema the *founder* of the Rajamahendravaram branch, 1395-1414; section 10 dates the branch to 1402 "
              "and section 11 says he founded it after Komati Vema seized the Kondavidu throne; the three sections disagree on date and role. "
              "Not checked against external references yet. Mapping below is provisional. Both conflicting source statements are kept verbatim in docs/ap_history_kataya_vema_audit.md. No questions or factual summaries from this section.",
}

FLAGS[(16, 6)] = (FLAGS.get((16, 6), "") + ";cross_unit_context").lstrip(";")
FLAGS[(16, 11)] = (FLAGS.get((16, 11), "") + ";supplementary_cross_context").lstrip(";")

# Coverage scope (separate from the primary chapter): does the section count as direct syllabus coverage?
#   direct | mixed (contains direct and supplementary material; decide per question) | supplementary_context | study_aid
# Default is direct. Supplementary chapters are 'supplementary' in the builder.
COVERAGE = {}
# Unit 2 ends with the 16th century: post-1600 Qutb Shahi material is supporting context, not direct coverage.
for k in [(13, 4), (13, 6), (13, 10), (13, 11), (13, 12), (13, 13)]:
    COVERAGE[k] = "mixed"
for k in [(13, 9), (13, 14), (13, 15)]:
    COVERAGE[k] = "supplementary_context"
# Source chapter 18: pure political/administrative chronology goes to the fourth supplementary chapter (coverage 'supplementary' is derived).
# Mixed sections keep one primary home (dominant content), retain a secondary, and are never split.
for k in [(18, 3), (18, 7), (18, 9), (18, 13)]:
    COVERAGE[k] = "mixed"
RULE_NOTES = {
    "qutb_shahi": "Seventeenth-century rulers, Akkanna-Madanna, later monuments, Mughal annexation and the 1687 decline are supporting context. Questions on post-1600 events carry the tag supplementary_context unless needed to explain a development that began in the sixteenth century.",
    "chapter_18": "Pure political or administrative chronology of 1956-2014 (ordinary chief-minister lists and chronology, elections and party chronology, cabinet changes, routine government succession, administrative developments without substantial social-cultural consequences) is mapped to the fourth supplementary chapter, which never counts toward direct syllabus completion. Chapter 31 keeps material that directly concerns or substantially shaped language, education, literature, theatre, cinema, arts, social reform, Dalit, women's, peasant or civil-society movements, regional identity, the 1969 Telangana agitation, the 1972 Jai Andhra movement, Mulki and regional safeguards, the Six-Point Formula, G.O. 610 and regional employment, and the developments leading to the 2014 reorganisation. Source 18 sections 3, 7 and 9 therefore have Chapter 31 as primary (mixed) with the supplementary chapter as secondary.",
    "komaram_bheem": "Source 16.11 stays unsplit and multi-topic. Future MCQs do not inherit its primary mapping: each question is mapped individually (Komaram Bheem, Gond rights, forest restrictions, resistance to Nizam administration: supplementary Asaf Jahi primary, Chapter 26 secondary; Gond culture: Chapter 26; individual Hyderabad State freedom leaders: Chapter 19 where historically appropriate with Hyderabad supplementary context; purely Telangana/Hyderabad regional politics outside the direct Andhra syllabus: supplementary context). The question importer or content review must enforce this.",
    "question_scope": "Questions inherit scope from the specific fact tested, not from the containing note section. A mixed section may yield direct questions and supplementary_context questions.",
}
