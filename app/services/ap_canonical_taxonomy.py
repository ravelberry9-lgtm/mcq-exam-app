"""PROPOSED rationalized learner-facing taxonomy for the 31 canonical chapters. NOT seeded; for review.

Model:  Canonical chapter -> learner-facing subtopic (navigation) -> internal microtopic (filter tag, never navigation).

Every one of the 314 earlier draft subtopics survives as a microtopic (its old slug is kept as the microtopic slug), so no detail is
lost; the learner sees only the grouped subtopics. A question has one primary subtopic and may carry several microtopic tags.
``GROUPS[chapter] = [(key, English, Telugu, [old draft suffixes...]), ...]``; the full subtopic slug is ``<chapter prefix>-<key>``.
"""
import re

from .ap_canonical import CHAPTERS
from .ap_canonical_subtopics import expanded as _draft

GROUPS = {
    1: [("land-people-identity", "Land, people and identity of Andhradesa", "ఆంధ్రదేశం: భూమి, ప్రజలు మరియు గుర్తింపు", ["geography-extent", "people-name-origin", "telugu-identity-language"]),
        ("literary-sources", "Literary sources", "సాహిత్య ఆధారాలు", ["literary-sources"]),
        ("foreign-accounts", "Foreign accounts", "విదేశీయుల రచనలు", ["foreign-accounts"]),
        ("inscriptions", "Inscriptions", "శాసనాలు", ["inscriptions"]),
        ("coins", "Coins", "నాణేలు", ["coins"]),
        ("archaeology-sites", "Archaeological evidence and historical sites", "పురావస్తు ఆధారాలు మరియు చారిత్రక స్థలాలు", ["archaeological-evidence", "important-sites"])],
    2: [("palaeolithic", "Palaeolithic culture", "పురాతన శిలాయుగం (పాలియోలిథిక్)", ["palaeolithic"]),
        ("mesolithic", "Mesolithic culture", "మధ్య శిలాయుగం (మెసోలిథిక్)", ["mesolithic"]),
        ("neolithic-chalcolithic", "Neolithic and Chalcolithic cultures", "నవీన శిలాయుగం (నియోలిథిక్) మరియు రాగి–రాతి యుగం (చాల్కోలిథిక్)", ["neolithic", "chalcolithic"]),
        ("megalithic-iron-age", "Megalithic and Iron Age cultures", "బృహత్‌శిలా సంస్కృతి (మెగాలిథిక్) మరియు ఇనుప యుగం", ["megalithic-iron-age", "burial-practices"]),
        ("tools-pottery", "Tools, technology and pottery", "పనిముట్లు, సాంకేతికత మరియు మట్టి పాత్రలు", ["tools-technology", "pottery"]),
        ("important-sites", "Important prehistoric sites", "ముఖ్య చరిత్రపూర్వ స్థలాలు", ["important-sites"])],
    3: [("assaka-early-references", "Assaka and early references to the Andhras", "అస్సక మరియు ఆంధ్రుల తొలి ప్రస్తావనలు", ["assaka-asmaka", "early-andhra-references"]),
        ("nandas-mauryas", "Nandas and Mauryas", "నందులు మరియు మౌర్యులు", ["nandas-mauryas"]),
        ("ashoka-inscriptions", "Ashoka's inscriptions in Andhra", "ఆంధ్రలో అశోకుని శాసనాలు", ["ashoka-inscriptions", "erragudi-rajulamandagiri"]),
        ("early-buddhism-centres", "Early Buddhism and its centres", "తొలి బౌద్ధమతం మరియు కేంద్రాలు", ["early-buddhism", "bhattiprolu", "amaravati-dhanyakataka-beginnings"]),
        ("kharavela-kalinga", "Kharavela and Kalinga", "ఖారవేలుడు మరియు కళింగ", ["kharavela-hathigumpha"]),
        ("local-rulers-coinage", "Early local rulers and coinage", "తొలి స్థానిక పాలకులు మరియు నాణేలు", ["early-local-rulers", "punch-marked-local-coinage"])],
    4: [("origin-chronology", "Origin, homeland and chronology", "మూలం, జన్మభూమి మరియు కాలక్రమం", ["origin-homeland", "chronology"]),
        ("political-history", "Political history and rulers", "రాజకీయ చరిత్ర మరియు పాలకులు", ["political-history", "important-rulers", "decline"]),
        ("administration", "Administration", "పరిపాలన", ["administration"]),
        ("society-economy", "Society, economy and trade", "సమాజం, ఆర్థిక వ్యవస్థ మరియు వాణిజ్యం", ["society", "economy-trade"]),
        ("religion", "Religion", "మతం", ["religion"]),
        ("literature", "Literature", "సాహిత్యం", ["literature"]),
        ("art-architecture", "Art and architecture", "కళ మరియు వాస్తుశిల్పం", ["art-architecture"]),
        ("coins-inscriptions", "Coins and inscriptions", "నాణేలు మరియు శాసనాలు", ["coinage", "inscriptions"])],
    5: [("origin-chronology", "Origin and chronology", "మూలం మరియు కాలక్రమం", ["origin-chronology"]),
        ("political-history", "Political history and rulers", "రాజకీయ చరిత్ర మరియు పాలకులు", ["important-rulers", "decline"]),
        ("vijayapuri-nagarjunakonda", "Vijayapuri and Nagarjunakonda", "విజయపురి మరియు నాగార్జునకొండ", ["vijayapuri-nagarjunakonda"]),
        ("administration", "Administration", "పరిపాలన", ["administration"]),
        ("society-royal-women", "Society, economy and royal women", "సమాజం, ఆర్థిక స్థితి మరియు రాజస్త్రీలు", ["socio-economic-conditions", "royal-women"]),
        ("religion", "Religion: Buddhism and Brahmanism", "మతం: బౌద్ధం మరియు బ్రాహ్మణ మతం", ["buddhism", "brahmanism"]),
        ("literature-education", "Literature and education", "సాహిత్యం మరియు విద్య", ["literature-education"]),
        ("art-architecture", "Art and architecture", "కళ మరియు వాస్తుశిల్పం", ["art-architecture"]),
        ("inscriptions", "Inscriptions", "శాసనాలు", ["inscriptions"])],
    6: [("early-dynasties", "Brihatphalayanas and Ananda Gotrikas", "బృహత్‌ఫలాయనులు మరియు ఆనంద గోత్రికులు", ["brihatphalayanas", "ananda-gotrikas"]),
        ("salankayanas", "Salankayanas", "శాలంకాయనులు", ["salankayanas"]),
        ("pallava-other-dynasties", "Pallava influence and other transitional dynasties", "పల్లవ ప్రభావం మరియు ఇతర సంధి కాల రాజవంశాలు", ["pallava-influence", "other-transitional-dynasties"]),
        ("political-conditions", "Political conditions of the period", "ఆ కాలపు రాజకీయ పరిస్థితులు", ["political-conditions"]),
        ("society-economy", "Society and economy", "సమాజం మరియు ఆర్థిక వ్యవస్థ", ["society-economy"]),
        ("religion", "Religion", "మతం", ["religion"]),
        ("art-inscriptions", "Art, architecture and inscriptions", "కళ, వాస్తుశిల్పం మరియు శాసనాలు", ["art-architecture", "inscriptions"])],
    7: [("origin-chronology", "Origin and chronology", "మూలం మరియు కాలక్రమం", ["origin-chronology"]),
        ("political-history", "Political history, rulers and decline", "రాజకీయ చరిత్ర, పాలకులు మరియు పతనం", ["important-rulers", "political-expansion", "decline"]),
        ("administration-society", "Administration, society and economy", "పరిపాలన, సమాజం మరియు ఆర్థిక వ్యవస్థ", ["administration", "society-economy"]),
        ("religion", "Religion", "మతం", ["religion"]),
        ("language-literature", "Sanskrit and Telugu development", "సంస్కృత మరియు తెలుగు వికాసం", ["sanskrit-telugu-development"]),
        ("cave-temple-architecture", "Cave-temple art and architecture", "గుహాలయ కళ మరియు వాస్తుశిల్పం", ["cave-temple-architecture"]),
        ("coins-inscriptions", "Coins and inscriptions", "నాణేలు మరియు శాసనాలు", ["coins", "inscriptions"])],
    8: [("vengi-foundation", "Foundation of the Vengi Chalukya kingdom", "వేంగి చాళుక్య రాజ్య స్థాపన", ["vengi-foundation"]),
        ("political-history", "Political history, chronology and rulers", "రాజకీయ చరిత్ర, కాలక్రమం మరియు పాలకులు", ["political-chronology", "important-rulers", "decline-transition"]),
        ("chola-chalukya-relations", "Chola–Chalukya relations", "చోళ–చాళుక్య సంబంధాలు", ["chola-chalukya-relations"]),
        ("administration-society-economy", "Administration, society and economy", "పరిపాలన, సమాజం మరియు ఆర్థిక వ్యవస్థ", ["administration", "society-economy"]),
        ("religion", "Religion", "మతం", ["religion"]),
        ("telugu-literature", "Telugu literature: Nannaya and the Andhra Mahabharata", "తెలుగు సాహిత్యం: నన్నయ మరియు ఆంధ్ర మహాభారతం", ["telugu-nannaya-literature"]),
        ("art-architecture", "Art and architecture (including Pancharamas)", "కళ మరియు వాస్తుశిల్పం (పంచారామాలతో సహా)", ["art-architecture", "temples-pancharamas"]),
        ("telugu-chodas-palnadu", "Telugu Chodas and the Palnadu war", "తెలుగు చోడులు మరియు పల్నాటి యుద్ధం", ["velanati-chodas", "nellore-telugu-chodas", "palnadu-war"]),
        ("inscriptions", "Inscriptions", "శాసనాలు", ["inscriptions"])],
    9: [("political-history", "Political history and rulers", "రాజకీయ చరిత్ర మరియు పాలకులు", ["origin-early-rulers", "rudradeva", "mahadeva", "ganapatideva", "rudramadevi", "prataparudra", "political-expansion"]),
        ("invasions-decline", "Delhi Sultanate invasions and decline", "ఢిల్లీ సుల్తానుల దండయాత్రలు మరియు పతనం", ["delhi-sultanate-invasions", "decline"]),
        ("administration", "Administration (Nayankara system)", "పరిపాలన (నాయంకర వ్యవస్థ)", ["administration-nayankara"]),
        ("economy", "Economy: irrigation, agriculture, crafts and trade", "ఆర్థిక వ్యవస్థ: నీటిపారుదల, వ్యవసాయం, చేతిపనులు మరియు వాణిజ్యం", ["irrigation-agriculture", "crafts-trade-motupalli"]),
        ("society", "Society", "సమాజం", ["society"]),
        ("religion", "Religion", "మతం", ["religion"]),
        ("telugu-literature", "Telugu literature", "తెలుగు సాహిత్యం", ["telugu-literature"]),
        ("dance-music", "Dance and music", "నృత్యం మరియు సంగీతం", ["dance-music"]),
        ("art-architecture", "Art and architecture", "కళ మరియు వాస్తుశిల్పం", ["art-architecture"])],
    10: [("musunuri-nayakas", "Post-Kakatiya conditions and the Musunuri Nayakas", "కాకతీయానంతర పరిస్థితులు మరియు ముసునూరి నాయకులు", ["post-kakatiya-conditions", "musunuri-nayakas"]),
         ("reddy-kingdoms", "Reddy kingdoms (Kondavidu and Rajahmundry)", "రెడ్డి రాజ్యాలు (కొండవీడు మరియు రాజమహేంద్రవరం)", ["kondavidu-reddys", "rajahmundry-reddys"]),
         ("velamas-regional-conflicts", "Recherla Velamas and regional conflicts", "రేచర్ల వెలమలు మరియు ప్రాంతీయ సంఘర్షణలు", ["recharla-velamas", "regional-conflicts"]),
         ("administration", "Administration", "పరిపాలన", ["administration"]),
         ("society-economy", "Society and economy", "సమాజం మరియు ఆర్థిక వ్యవస్థ", ["society-economy"]),
         ("religion", "Religion", "మతం", ["religion"]),
         ("telugu-literature", "Telugu literature", "తెలుగు సాహిత్యం", ["telugu-literature"]),
         ("art-architecture", "Art and architecture", "కళ మరియు వాస్తుశిల్పం", ["art-architecture"])],
    11: [("foundation-dynasties", "Foundation and the four dynasties", "స్థాపన మరియు నాలుగు వంశాలు", ["foundation", "four-dynasties"]),
         ("political-history", "Political history and Andhra campaigns", "రాజకీయ చరిత్ర మరియు ఆంధ్ర దండయాత్రలు", ["important-rulers", "andhra-campaigns-gajapati-bahmani"]),
         ("krishnadevaraya", "Krishnadevaraya", "శ్రీకృష్ణదేవరాయలు", ["krishnadevaraya"]),
         ("talikota-decline", "Battle of Talikota and decline", "తళ్ళికోట యుద్ధం మరియు పతనం", ["battle-of-talikota", "decline"]),
         ("administration", "Administration (Nayankara system)", "పరిపాలన (నాయంకర వ్యవస్థ)", ["administration-nayankara"]),
         ("economy-society", "Economy, trade and society", "ఆర్థిక వ్యవస్థ, వాణిజ్యం మరియు సమాజం", ["economy-trade", "society"]),
         ("religion", "Religion", "మతం", ["religion"]),
         ("telugu-literature", "Telugu literature and the Ashtadiggajas", "తెలుగు సాహిత్యం మరియు అష్టదిగ్గజాలు", ["telugu-literature-ashtadiggajas"]),
         ("art-architecture", "Art and architecture", "కళ మరియు వాస్తుశిల్పం", ["art-architecture"])],
    12: [("gajapati-rule", "Gajapati rule and influence", "గజపతుల పాలన మరియు ప్రభావం", ["gajapati-rule-influence"]),
         ("bahmani-conflicts", "Bahmani–Vijayanagara rivalry and coastal Andhra conflicts", "బహమనీ–విజయనగర పోటీ మరియు కోస్తాంధ్ర సంఘర్షణలు", ["bahmani-vijayanagara-rivalry", "coastal-andhra-conflicts"]),
         ("minor-powers-forts", "Minor regional powers, forts and political centres", "చిన్న ప్రాంతీయ శక్తులు, కోటలు మరియు రాజకీయ కేంద్రాలు", ["minor-regional-powers", "forts-political-centres"]),
         ("socio-cultural-transition", "Socio-cultural influence and political transition", "సామాజిక–సాంస్కృతిక ప్రభావం మరియు రాజకీయ మార్పు", ["socio-cultural-influence", "political-transition"])],
    13: [("establishment-rulers", "Establishment and rulers", "స్థాపన మరియు పాలకులు", ["establishment", "sixteenth-century-rulers", "expansion-into-andhra"]),
         ("administration", "Administration", "పరిపాలన", ["administration"]),
         ("society-economy-trade", "Society, economy and trade", "సమాజం, ఆర్థిక వ్యవస్థ మరియు వాణిజ్యం", ["society-economy", "trade-ports-golconda"]),
         ("religion", "Religion", "మతం", ["religion"]),
         ("language-patronage", "Telugu and Dakhni patronage", "తెలుగు మరియు దక్కనీ భాషల పోషణ", ["telugu-dakhni-patronage"]),
         ("art-architecture", "Art, architecture and city planning", "కళ, వాస్తుశిల్పం మరియు నగర ప్రణాళిక", ["art-architecture"])],
    14: [("administration-society", "Comparative administration and social structure", "తులనాత్మక పరిపాలన మరియు సామాజిక నిర్మాణం", ["comparative-administration", "social-structure"]),
         ("economy", "Economic conditions: agriculture, irrigation and trade", "ఆర్థిక పరిస్థితులు: వ్యవసాయం, నీటిపారుదల మరియు వాణిజ్యం", ["economic-conditions", "agriculture-irrigation", "trade"]),
         ("religious-movements", "Religious movements", "మత ఉద్యమాలు", ["religious-movements"]),
         ("language-literature", "Growth of Telugu and its authors", "తెలుగు భాష వికాసం మరియు కవులు", ["growth-of-telugu", "authors-works"]),
         ("art-architecture", "Sculpture, temple architecture and forts", "శిల్పం, ఆలయ నిర్మాణం మరియు కోటలు", ["sculpture", "temple-architecture", "forts"]),
         ("music-dance", "Music and dance", "సంగీతం మరియు నృత్యం", ["music-dance"])],
    15: [("european-companies", "European trading companies in Andhra", "ఆంధ్రలో యూరోపియన్ వర్తక సంస్థలు", ["portuguese", "dutch", "english", "french"]),
         ("trading-centres-ports", "Trading centres and ports", "వ్యాపార కేంద్రాలు మరియు ఓడరేవులు", ["trading-centres-ports"]),
         ("european-rivalries", "European rivalries and the Carnatic Wars", "యూరోపియన్ పోటీలు మరియు కర్ణాటక యుద్ధాలు", ["european-rivalries"]),
         ("northern-circars", "Northern Circars", "ఉత్తర సర్కార్లు", ["northern-circars"]),
         ("ceded-districts", "Ceded Districts", "దత్త మండలాలు (సీడెడ్ జిల్లాలు)", ["ceded-districts"]),
         ("company-administration-revenue", "Company administration and revenue", "కంపెనీ పాలన మరియు రెవెన్యూ", ["company-administration", "revenue-systems"]),
         ("early-economic-social-impact", "Early economic and social impact", "తొలి ఆర్థిక మరియు సామాజిక ప్రభావం", ["early-economic-social-impact"])],
    16: [("consolidation-administration", "Consolidation of British administration", "బ్రిటిష్ పాలన బలోపేతం", ["consolidation-of-administration"]),
         ("land-revenue-settlements", "Land-revenue settlements (Zamindari and Ryotwari)", "భూ శిస్తు విధానాలు (జమీందారీ మరియు రైత్వారీ)", ["zamindari-ryotwari", "thomas-munro"]),
         ("irrigation-works", "Irrigation works", "నీటిపారుదల పనులు", ["arthur-cotton"]),
         ("economic-effects", "Administrative and economic effects", "పరిపాలనా మరియు ఆర్థిక ప్రభావాలు", ["administrative-economic-effects"]),
         ("revolt-1857", "Revolt of 1857 in Andhra", "ఆంధ్రలో 1857 తిరుగుబాటు", ["revolt-of-1857", "andhra-events-personalities-1857"]),
         ("impact-1857", "Impact of 1857", "1857 ప్రభావం", ["impact-of-1857"])],
    17: [("education-missionaries", "Western education and missionary activity", "పాశ్చాత్య విద్య మరియు మిషనరీ కార్యకలాపాలు", ["western-education", "missionary-activity"]),
         ("print-culture", "Print culture", "ముద్రణ సంస్కృతి", ["print-culture"]),
         ("social-reform", "Social reform and women's reform", "సంఘ సంస్కరణ మరియు మహిళా సంస్కరణ", ["social-reform", "womens-reform"]),
         ("major-reformers", "Major reformers", "ప్రముఖ సంస్కర్తలు", ["veeresalingam", "raghupati-venkataratnam-naidu", "gurajada-apparao"]),
         ("modern-telugu-awakening", "Modern Telugu awakening", "ఆధునిక తెలుగు చైతన్యం", ["modern-telugu-awakening"]),
         ("associations-institutions", "Associations and institutions", "సంఘాలు మరియు సంస్థలు", ["associations-institutions"])],
    18: [("justice-party", "Non-Brahmin movement and the Justice Party", "బ్రాహ్మణేతర ఉద్యమం మరియు జస్టిస్ పార్టీ", ["non-brahmin-origins", "justice-party"]),
         ("leaders-policies", "Leaders, policies and social impact", "నాయకులు, విధానాలు మరియు సామాజిక ప్రభావం", ["important-leaders", "policies-social-impact"]),
         ("self-respect-movement", "Self-Respect Movement", "ఆత్మగౌరవ ఉద్యమం", ["self-respect-movement"]),
         ("influence-in-andhra", "Influence in Andhra", "ఆంధ్రలో ప్రభావం", ["influence-in-andhra"]),
         ("debates-limitations", "Debates and limitations", "చర్చలు మరియు పరిమితులు", ["debates-limitations"])],
    19: [("early-associations-congress", "Early political associations and the Congress in Andhra", "తొలి రాజకీయ సంఘాలు మరియు ఆంధ్రలో కాంగ్రెస్", ["early-political-associations", "congress-and-andhra"]),
         ("swadeshi-home-rule", "Swadeshi–Vandemataram and Home Rule movements", "స్వదేశీ–వందేమాతర మరియు హోమ్ రూల్ (స్వపరిపాలన) ఉద్యమాలు", ["swadeshi-vandemataram", "home-rule"]),
         ("non-cooperation", "Non-Cooperation Movement", "సహాయ నిరాకరణ ఉద్యమం", ["non-cooperation", "chirala-perala-pedanandipadu"]),
         ("civil-disobedience", "Civil Disobedience and Salt Satyagraha", "శాసనోల్లంఘన మరియు ఉప్పు సత్యాగ్రహం", ["civil-disobedience-salt-satyagraha"]),
         ("individual-satyagraha-quit-india", "Individual Satyagraha and Quit India", "వ్యక్తిగత సత్యాగ్రహం మరియు క్విట్ ఇండియా", ["individual-satyagraha", "quit-india"]),
         ("prominent-leaders", "Prominent leaders", "ప్రముఖ నాయకులు", ["prominent-leaders"]),
         ("regional-centres-events", "Regional centres and events", "ప్రాంతీయ కేంద్రాలు మరియు సంఘటనలు", ["regional-centres-events"])],
    20: [("socialists", "Socialists", "సోషలిస్టులు", ["socialists"]),
         ("communist-movement", "Communist movement", "కమ్యూనిస్టు ఉద్యమం", ["communist-movement"]),
         ("peasant-kisan-movement", "Peasant organisation and Kisan movement", "రైతు సంఘటన మరియు కిసాన్ ఉద్యమం", ["peasant-organisation", "kisan-sabhas", "ng-ranga"]),
         ("anti-zamindari-struggles", "Anti-Zamindari and regional agrarian struggles", "జమీందారీ వ్యతిరేక మరియు ప్రాంతీయ వ్యవసాయ పోరాటాలు", ["anti-zamindari-struggles", "regional-agrarian-struggles"]),
         ("labour-mobilisation", "Labour mobilisation", "కార్మిక సమీకరణ", ["labour-mobilisation"]),
         ("relation-to-national-movement", "Relation to the national movement", "జాతీయోద్యమంతో సంబంధం", ["relation-to-national-movement"])],
    21: [("nationalist-revolutionary-writing", "Nationalist poetry and revolutionary writings", "జాతీయ కవిత్వం మరియు విప్లవ రచనలు", ["nationalist-poetry", "revolutionary-writings"]),
         ("poets-authors", "Poets and authors", "కవులు మరియు రచయితలు", ["poets-authors"]),
         ("newspapers-publications", "Newspapers and publications", "పత్రికలు మరియు ప్రచురణలు", ["newspapers-publications"]),
         ("drama-nataka-samajalu", "Drama societies (Nataka Samajalu)", "నాటక సమాజాలు", ["drama-organisations", "nataka-samasthalu"]),
         ("peoples-theatre", "People's theatre: Praja Natya Mandali and Maa Bhoomi", "ప్రజా నాట్య మండలి మరియు మా భూమి", ["praja-natya-mandali", "maa-bhoomi"]),
         ("folk-performance-mobilisation", "Folk performance and mobilisation", "జానపద ప్రదర్శనలు మరియు ప్రజా సమీకరణ", ["folk-performance-mobilisation"])],
    22: [("women-reformers-organisations", "Women reformers and women's organisations", "మహిళా సంస్కర్తలు మరియు మహిళా సంఘాలు", ["women-reformers", "organisations"]),
         ("swadeshi-gandhian-movements", "Women in Swadeshi, Home Rule and Gandhian movements", "స్వదేశీ, హోమ్ రూల్ మరియు గాంధేయ ఉద్యమాల్లో మహిళలు", ["swadeshi-home-rule", "gandhian-movements"]),
         ("revolutionary-peasant-movements", "Women in revolutionary and peasant movements", "విప్లవ మరియు రైతు ఉద్యమాల్లో మహిళలు", ["revolutionary-peasant-movements"]),
         ("prominent-women-regional-events", "Prominent women and regional events", "ప్రముఖ మహిళలు మరియు ప్రాంతీయ సంఘటనలు", ["prominent-women", "regional-events"]),
         ("social-consequences", "Social consequences", "సామాజిక పరిణామాలు", ["social-consequences"])],
    23: [("linguistic-identity-roots", "Roots of linguistic identity and its dimensions", "భాషా గుర్తింపు మూలాలు మరియు దాని కోణాలు", ["linguistic-identity-roots", "political-cultural-dimensions"]),
         ("demand-andhra-province", "Demand for a separate Andhra province", "ప్రత్యేక ఆంధ్ర రాష్ట్ర డిమాండ్", ["demand-for-andhra-province"]),
         ("organisations-conferences", "Early organisations, conferences and resolutions", "తొలి సంస్థలు, సభలు మరియు తీర్మానాలు", ["early-organisations", "important-conferences", "andhra-provincial-congress", "major-resolutions"]),
         ("andhra-university", "Andhra University", "ఆంధ్ర విశ్వవిద్యాలయం", ["andhra-university"]),
         ("sri-bagh-pact", "Sri Bagh Pact", "శ్రీబాగ్ ఒప్పందం", ["sri-bagh-pact"])],
    24: [("sessions-resolutions", "Sessions and resolutions of the Andhra Mahasabha", "ఆంధ్ర మహాసభ సభలు మరియు తీర్మానాలు", ["origin-sessions", "resolutions"]),
         ("organisational-development", "Organisational development", "సంస్థాగత అభివృద్ధి", ["organisational-development"]),
         ("leaders-differences", "Leaders and ideological differences", "నాయకులు మరియు సైద్ధాంతిక విభేదాలు", ["major-leaders", "ideological-differences"]),
         ("contribution-state-formation", "Contribution to state formation", "రాష్ట్ర ఏర్పాటులో పాత్ర", ["contribution-to-state-formation"])],
    25: [("newspapers", "Telugu newspapers (Krishna Patrika, Andhra Patrika and others)", "తెలుగు పత్రికలు (కృష్ణా పత్రిక, ఆంధ్ర పత్రిక మొదలైనవి)", ["krishna-patrika", "andhra-patrika", "other-newspapers"]),
         ("journalists-press-mobilisation", "Journalists, editors and press mobilisation", "పాత్రికేయులు, సంపాదకులు మరియు పత్రికల ప్రజా సమీకరణ", ["journalists-editors", "press-political-mobilisation"]),
         ("library-movement", "Library movement", "గ్రంథాలయోద్యమం", ["library-movement", "ayyanki-venkata-ramanayya", "andhra-desa-library-association", "libraries-public-awakening"]),
         ("literary-organisations", "Language and literary organisations", "భాషా మరియు సాహిత్య సంస్థలు", ["language-literary-organisations"])],
    26: [("folk-performing-arts", "Folk performing arts (Harikatha, Burrakatha, Tholu Bommalata)", "జానపద ప్రదర్శన కళలు (హరికథ, బుర్రకథ, తోలుబొమ్మలాట)", ["folk-traditions", "harikatha", "burrakatha", "tholu-bommalata", "regional-dance-performance"]),
         ("tribal-communities", "Major tribal communities", "ప్రధాన గిరిజన సమూహాలు", ["major-tribal-communities"]),
         ("tribal-customs-festivals", "Tribal customs and festivals", "గిరిజన ఆచారాలు మరియు పండుగలు", ["tribal-customs-festivals"]),
         ("tribal-resistance", "Tribal resistance and context", "గిరిజన ప్రతిఘటన మరియు సందర్భం", ["tribal-resistance"]),
         ("identity-mobilisation", "Cultural identity and mobilisation", "సాంస్కృతిక గుర్తింపు మరియు సమీకరణ", ["identity-mobilisation"])],
    27: [("background-committees", "Background, Dhar Commission and JVP Committee", "నేపథ్యం, ధార్ కమిషన్ మరియు జె.వి.పి. కమిటీ", ["constitutional-political-background", "dhar-commission", "jvp-committee"]),
         ("potti-sriramulu-agitation", "Potti Sriramulu's fast and the agitation", "పొట్టి శ్రీరాములు నిరాహార దీక్ష మరియు ఉద్యమం", ["swami-sitaram", "potti-sriramulu", "fast-and-death", "public-response"]),
         ("madras-question", "Madras question", "మద్రాసు సమస్య", ["madras-question"]),
         ("formation-andhra-state", "Formation of Andhra State and the capital", "ఆంధ్ర రాష్ట్ర ఏర్పాటు మరియు రాజధాని", ["formation-of-andhra-state", "kurnool-capital", "tanguturi-prakasam"]),
         ("consequences", "Consequences", "పరిణామాలు", ["consequences"])],
    28: [("visalandhra-idea", "Visalandhra idea and its arguments", "విశాలాంధ్ర భావన మరియు వాదనలు", ["visalandhra-idea", "linguistic-political-arguments"]),
         ("visalandhra-mahasabha", "Visalandhra Mahasabha and its resolutions", "విశాలాంధ్ర మహాసభ మరియు తీర్మానాలు", ["visalandhra-mahasabha", "meetings-resolutions"]),
         ("supporters-opponents", "Supporters and opponents", "మద్దతుదారులు మరియు వ్యతిరేకులు", ["supporters-opponents"]),
         ("merger-debate", "Andhra–Telangana merger debate", "ఆంధ్ర–తెలంగాణ విలీన చర్చ", ["andhra-telangana-merger-debate"])],
    29: [("src-formation-terms", "Formation, members and terms of reference of the SRC", "రాష్ట్రాల పునర్వ్యవస్థీకరణ సంఘం (SRC) ఏర్పాటు, సభ్యులు మరియు విధివిధానాలు", ["formation-members", "terms-of-reference"]),
         ("evidence-arguments", "Evidence and arguments on Andhra and Telangana", "ఆంధ్ర–తెలంగాణ సాక్ష్యాలు మరియు వాదనలు", ["andhra-telangana-evidence", "arguments-separate-telangana"]),
         ("recommendations", "Recommendations", "సిఫార్సులు", ["recommendations"]),
         ("merger-conditions-responses", "Conditions for merger and political responses", "విలీన షరతులు మరియు రాజకీయ స్పందనలు", ["conditions-for-merger", "political-responses"])],
    30: [("gentlemens-agreement", "Gentlemen's Agreement: negotiations, signatories, provisions and safeguards", "పెద్దమనుషుల ఒప్పందం (జెంటిల్మెన్స్ అగ్రిమెంట్): చర్చలు, సంతకందారులు, నిబంధనలు మరియు రక్షణలు", ["negotiations", "signatories", "provisions", "regional-safeguards"]),
         ("merger-formation", "Merger process and formation of Andhra Pradesh, 1 November 1956", "విలీన ప్రక్రియ మరియు ఆంధ్రప్రదేశ్ ఏర్పాటు (1956 నవంబర్ 1)", ["merger-process", "formation-1-november-1956"]),
         ("hyderabad-capital", "Hyderabad as capital", "హైదరాబాద్ రాజధానిగా", ["hyderabad-capital"]),
         ("implementation-issues", "Implementation issues", "అమలు సమస్యలు", ["implementation-issues"]),
         ("long-term-significance", "Long-term significance", "దీర్ఘకాలిక ప్రాధాన్యత", ["long-term-significance"])],
    31: [("language-education", "Official language and education", "అధికార భాష మరియు విద్య", ["official-language-telugu", "education-universities"]),
         ("literature-theatre", "Literature and theatre", "సాహిత్యం మరియు రంగస్థలం", ["literature", "theatre"]),
         ("cinema", "Cinema", "సినిమా", ["cinema"]),
         ("arts-institutions", "Visual and performing arts, cultural institutions and developments to 2014", "దృశ్య మరియు ప్రదర్శన కళలు, సాంస్కృతిక సంస్థలు మరియు 2014 వరకు పరిణామాలు", ["visual-performing-arts", "cultural-institutions", "cultural-developments-to-2014"]),
         ("dalit-social-movements", "Dalit and social movements", "దళిత మరియు సామాజిక ఉద్యమాలు", ["dalit-social-movements"]),
         ("womens-civil-society", "Women's and civil-society movements", "మహిళా మరియు పౌర సమాజ ఉద్యమాలు", ["womens-movements", "civil-society-movements"]),
         ("regional-identity-movements", "Regional identity movements: Telangana 1969, Jai Andhra 1972 and safeguards", "ప్రాంతీయ గుర్తింపు ఉద్యమాలు: 1969 తెలంగాణ, 1972 జై ఆంధ్ర మరియు రక్షణలు", ["telangana-movement-1969", "jai-andhra-1972", "regional-identity-movements"])],
}

# New microtopics that no old draft subtopic carried: (chapter, group key, micro suffix, English, Telugu, coverage scope).
EXTRA_MICRO = [
    (13, "establishment-rulers", "post-1600-context", "Seventeenth-century rulers, Akkanna–Madanna, Mughal annexation (1687) — supporting context",
     "పదిహేడో శతాబ్దపు పాలకులు, అక్కన్న–మాదన్న, మొఘల్ విలీనం (1687) — అనుబంధ సందర్భం", "supplementary_context"),
    (19, "regional-centres-events", "rampa-rebellion", "Rampa Rebellion, 1922–24", "రంపా తిరుగుబాటు (1922–24)", "direct"),
    (31, "regional-identity-movements", "mulki-rules", "Mulki rules and regional safeguards", "ముల్కీ నిబంధనలు మరియు ప్రాంతీయ రక్షణలు", "direct"),
]

# Normalized learner-facing Telugu for old draft items (chapter, old suffix) -> Telugu. Preserve source spellings in source-text fields only.
TE_OVERRIDES = {
    (2, "palaeolithic"): "పురాతన శిలాయుగం (పాలియోలిథిక్)",
    (2, "mesolithic"): "మధ్య శిలాయుగం (మెసోలిథిక్)",
    (2, "neolithic"): "నవీన శిలాయుగం (నియోలిథిక్)",
    (2, "chalcolithic"): "రాగి–రాతి యుగం (చాల్కోలిథిక్)",
    (2, "megalithic-iron-age"): "బృహత్‌శిలా సంస్కృతి (మెగాలిథిక్) మరియు ఇనుప యుగం",
    (3, "kharavela-hathigumpha"): "ఖారవేలుడు మరియు హాతిగుంఫా శాసనం",
    (3, "punch-marked-local-coinage"): "ముద్రాంకిత (పంచ్-మార్క్డ్) నాణేలు మరియు స్థానిక నాణేలు",
    (11, "battle-of-talikota"): "తళ్ళికోట యుద్ధం (Battle of Talikota)",
    (13, "establishment"): "కుతుబ్ షాహీ అధికార స్థాపన",
    (15, "northern-circars"): "ఉత్తర సర్కార్లు",
    (15, "ceded-districts"): "దత్త మండలాలు (సీడెడ్ జిల్లాలు)",
    (19, "home-rule"): "హోమ్ రూల్ (స్వపరిపాలన) ఉద్యమం",
    (23, "sri-bagh-pact"): "శ్రీబాగ్ ఒప్పందం",
    (27, "jvp-committee"): "జె.వి.పి. కమిటీ (JVP Committee)",
    (29, "formation-members"): "రాష్ట్రాల పునర్వ్యవస్థీకరణ సంఘం (SRC) ఏర్పాటు మరియు సభ్యులు",
}
# Variants that must not appear in learner-facing metadata -> preferred form (checked by tests; also applied generically).
TERM_REPLACEMENTS = [("కుతుబ్‌షాహీ", "కుతుబ్ షాహీ"), ("హాథీగుంఫా", "హాతిగుంఫా"), ("సర్కారులు", "సర్కార్లు"),
                     ("శ్రీబాగ్ ఒడంబడిక", "శ్రీబాగ్ ఒప్పందం"), ("రయొత్వారీ", "రైత్వారీ"), ("రయత్వారీ", "రైత్వారీ"),
                     ("డఖ్ఖనీ", "దక్కనీ"), ("దక్కని", "దక్కనీ")]
# Zero-width characters that are linguistically needed (display only; the search key strips them).
ZW_ALLOWED = ("బృహత్‌శిలా", "బృహత్‌ఫలాయనులు")
_ZW = re.compile("[​‌‍﻿]")


def search_key(te):
    """Telugu text with zero-width characters removed, for search and slugs."""
    return _ZW.sub("", te)


def _norm(te):
    for a, b in TERM_REPLACEMENTS:
        te = te.replace(a, b)
    return te


def build():
    """Full proposal: {chapter number: [subtopic dict]}. Each subtopic carries ``micros`` (old drafts + extras)."""
    chap = {num: slug for _u, num, slug, _e, _t, _c in CHAPTERS}
    draft = {num: {s.split("-", 2)[2]: (s, en, te) for s, en, te in _draft()[chap[num]]} for num in chap}
    out = {}
    for num, groups in GROUPS.items():
        prefix = "-".join(chap[num].split("-")[:2])
        subs = []
        for key, en, te, olds in groups:
            micros = []
            for old in olds:
                full, m_en, m_te = draft[num][old]
                micros.append({"slug": full, "old_suffix": old, "en": m_en, "te": _norm(TE_OVERRIDES.get((num, old), m_te)),
                               "scope": "direct", "from_draft": True})
            for c, k, suffix, m_en, m_te, scope in EXTRA_MICRO:
                if c == num and k == key:
                    micros.append({"slug": f"{prefix}-{suffix}", "old_suffix": None, "en": m_en, "te": m_te, "scope": scope, "from_draft": False})
            subs.append({"slug": f"{prefix}-{key}", "key": key, "en": en, "te": _norm(te), "micros": micros})
        out[num] = subs
    return out


def old_to_new():
    """old draft subtopic slug -> (new subtopic slug, microtopic slug)."""
    m = {}
    for subs in build().values():
        for s in subs:
            for mi in s["micros"]:
                if mi["from_draft"]:
                    m[mi["slug"]] = (s["slug"], mi["slug"])
    return m
