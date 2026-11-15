import json
from pathlib import Path


path = Path("content/geography/india_ap_chapters/7/Questions.json")
bank = json.loads(path.read_text(encoding="utf-8"))

# Each item below was written and judged separately from the printed-table ledger.
new_questions = [
    {
        "id": "IA07-029", "chapter": "IA-07", "origin": "book-audit-original", "kind": "matching-set", "difficulty": "hard", "language": "bilingual",
        "label": "Original PYQ-style practice; not an official previous-year question", "source_page": 337,
        "fact_ids": ["p337-land-use-statistics"], "section": "p337-statistics", "related_sections": ["water-resource-basics"],
        "question_te": "పుట 337లోని ముద్రిత గణాంకాల ప్రకారం సరైన జతల సముదాయం ఏది?",
        "question_en": "According to the printed statistics on page 337, which set of pairs is correct?",
        "options_te": ["భౌగోళిక విస్తీర్ణం—306.65 million ha; Net sown area—122.29 million ha", "భూవినియోగ నివేదికల పరిధి—328.76 million ha; Gross irrigated area—141.71 million ha", "భౌగోళిక విస్తీర్ణం—328.76 million ha; Net sown area—141.71 million ha", "మొత్తం పంటభూమి—141.71 million ha; Gross irrigated area—219.36 million ha"],
        "options_en": ["Geographical area—306.65 million ha; net sown area—122.29 million ha", "Land-use reporting area—328.76 million ha; gross irrigated area—141.71 million ha", "Geographical area—328.76 million ha; net sown area—141.71 million ha", "Total cropped area—141.71 million ha; gross irrigated area—219.36 million ha"],
        "answer": 3,
        "explanation_te": "పుట 337 పట్టికలో దేశ భౌగోళిక విస్తీర్ణం 328.76 million hectares, Net sown area 141.71 million hectares. Gross irrigated area 122.29 million hectares; reporting area 306.65 million hectares.",
        "explanation_en": "The table gives 328.76 million hectares as geographical area and 141.71 million hectares as net sown area. Gross irrigated area is 122.29 million hectares and reporting area is 306.65 million hectares.",
        "option_explanations_te": ["ఇవి geographical area, gross irrigated area విలువలను కలిపాయి.", "Reporting area, geographical area విలువలు తారుమారయ్యాయి.", "రెండు జతలూ ముద్రిత పట్టికతో సరిపోతాయి.", "Total cropped area, gross irrigated area రెండూ తప్పుగా జతచేశారు."],
        "option_explanations_en": ["It mixes the geographical-area and gross-irrigated-area values.", "The reporting-area and geographical-area values are reversed.", "Both pairs reproduce the printed table.", "Both total-cropped-area and gross-irrigated-area values are mismatched."],
        "source_urls": ["https://cwc.gov.in/"], "manual_review_status": "manually-authored-2026-11-01"
    },
    {
        "id": "IA07-030", "chapter": "IA-07", "origin": "book-audit-original", "kind": "statement-set", "difficulty": "hard", "language": "bilingual",
        "label": "Original PYQ-style practice; not an official previous-year question", "source_page": 338,
        "fact_ids": ["p338-irrigation-source-shares"], "section": "irrigation-sources-canals", "related_sections": ["canal-register"],
        "question_te": "పుట 338లోని historical snapshot ప్రకారం సాగునీటి వనరుల వాటాల descending order ఏది?",
        "question_en": "In the historical snapshot printed on page 338, what is the descending order of irrigation-source shares?",
        "options_te": ["Canals 65% > Wells 25% > Tanks 5% = Other 5%", "Wells 65% > Canals 25% > Tanks 5% = Other 5%", "Wells 55% > Canals 35% > Tanks 5% = Other 5%", "Wells 65% > Tanks 25% > Canals 5% = Other 5%"],
        "options_en": ["Canals 65% > wells 25% > tanks 5% = other 5%", "Wells 65% > canals 25% > tanks 5% = other 5%", "Wells 55% > canals 35% > tanks 5% = other 5%", "Wells 65% > tanks 25% > canals 5% = other 5%"],
        "answer": 2,
        "explanation_te": "ముద్రిత snapshotలో Wells 65%, Canals 25%, Tanks 5%, Other sources 5%. ఇవి current universal sharesగా కాక, పుస్తక కాలపు valuesగా చదవాలి.",
        "explanation_en": "The printed snapshot assigns 65% to wells, 25% to canals, and 5% each to tanks and other sources. These are period-specific values, not timeless universal shares.",
        "option_explanations_te": ["Wells, Canals వాటాలు తారుమారయ్యాయి.", "ఇదే ముద్రిత descending order.", "55:35 values పుస్తక పట్టికలో లేవు.", "Tanksకు 25%, Canalsకు 5% ఇవ్వడం తప్పు."],
        "option_explanations_en": ["It reverses the well and canal shares.", "This is the printed descending order.", "The table does not give 55:35.", "It wrongly assigns 25% to tanks and 5% to canals."],
        "source_urls": [], "manual_review_status": "manually-authored-2026-11-01"
    },
    {
        "id": "IA07-031", "chapter": "IA-07", "origin": "book-audit-original", "kind": "matching-set", "difficulty": "hard", "language": "bilingual",
        "label": "Original PYQ-style practice; not an official previous-year question", "source_page": 339,
        "fact_ids": ["p338-p339-north-india-canals"], "section": "canal-register", "related_sections": ["irrigation-sources-canals"],
        "question_te": "క్రింది State–Canal సముదాయాల్లో పూర్తిగా సరైనది ఏది?",
        "question_en": "Which State–Canal set is entirely correct?",
        "options_te": ["Punjab—Upper Bari Doab, Sirhind; Haryana—Western Yamuna; Bihar—Sone, Kosi", "Punjab—Sone, Kosi; Haryana—Upper Ganga; Bihar—Sirhind, Bhakra", "Rajasthan—Upper Bari Doab; Uttar Pradesh—Indira Gandhi; Gujarat—Western Yamuna", "Bihar—Malaprabha; Punjab—Kangsabati; Haryana—Mettur"],
        "options_en": ["Punjab—Upper Bari Doab, Sirhind; Haryana—Western Yamuna; Bihar—Sone, Kosi", "Punjab—Sone, Kosi; Haryana—Upper Ganga; Bihar—Sirhind, Bhakra", "Rajasthan—Upper Bari Doab; Uttar Pradesh—Indira Gandhi; Gujarat—Western Yamuna", "Bihar—Malaprabha; Punjab—Kangsabati; Haryana—Mettur"],
        "answer": 1,
        "explanation_te": "Upper Bari Doab, Sirhind Punjabకు; Western Yamuna Haryanaకు; Sone, Kosi Biharకు చెందిన canal systems.",
        "explanation_en": "Upper Bari Doab and Sirhind belong to Punjab, Western Yamuna to Haryana, and Sone and Kosi to Bihar.",
        "option_explanations_te": ["అన్ని జతలు సరైనవి.", "మూడు రాష్ట్రాల canal systemsను పరస్పరం మార్చింది.", "Upper Bari Doab Punjabలో, Indira Gandhi Rajasthanలో, Western Yamuna Haryanaలో ఉన్నాయి.", "Malaprabha Karnatakaలో, Kangsabati West Bengalలో, Mettur Tamil Naduలో ఉన్నాయి."],
        "option_explanations_en": ["All pairs are correct.", "It swaps the canal systems among all three states.", "Upper Bari Doab is in Punjab, Indira Gandhi in Rajasthan, and Western Yamuna in Haryana.", "Malaprabha is in Karnataka, Kangsabati in West Bengal, and Mettur in Tamil Nadu."],
        "source_urls": [], "manual_review_status": "manually-authored-2026-11-01"
    },
    {
        "id": "IA07-032", "chapter": "IA-07", "origin": "book-audit-original", "kind": "matching-set", "difficulty": "hard", "language": "bilingual",
        "label": "Original PYQ-style practice; not an official previous-year question", "source_page": 339,
        "fact_ids": ["p339-south-west-canals"], "section": "canal-register", "related_sections": ["irrigation-sources-canals"],
        "question_te": "క్రింది జతలలో తప్పుగా జతచేసిన State–Canal ఏది?",
        "question_en": "Which State–Canal pair is incorrectly matched?",
        "options_te": ["Karnataka—Tungabhadra, Ghataprabha", "Kerala—Malampuzha, Neyyar", "Tamil Nadu—Mettur, Bhavani", "Maharashtra—Kangsabati, Mayurakshi"],
        "options_en": ["Karnataka—Tungabhadra, Ghataprabha", "Kerala—Malampuzha, Neyyar", "Tamil Nadu—Mettur, Bhavani", "Maharashtra—Kangsabati, Mayurakshi"],
        "answer": 4,
        "explanation_te": "Kangsabati, Mayurakshi systems West Bengalకు చెందినవి. Maharashtra పట్టికలో Pravara, Tapti, Gangapur, Girna ఉన్నాయి.",
        "explanation_en": "Kangsabati and Mayurakshi belong to West Bengal. The Maharashtra register lists Pravara, Tapti, Gangapur and Girna.",
        "option_explanations_te": ["ఈ Karnataka జత సరైనది.", "ఈ Kerala జత సరైనది.", "ఈ Tamil Nadu జత సరైనది.", "ఇవి West Bengal systems; Maharashtraవి కావు."],
        "option_explanations_en": ["This Karnataka pair is correct.", "This Kerala pair is correct.", "This Tamil Nadu pair is correct.", "These are West Bengal systems, not Maharashtra systems."],
        "source_urls": [], "manual_review_status": "manually-authored-2026-11-01"
    },
    {
        "id": "IA07-033", "chapter": "IA-07", "origin": "book-audit-original", "kind": "statement-set", "difficulty": "hard", "language": "bilingual",
        "label": "Original PYQ-style practice; not an official previous-year question", "source_page": 340,
        "fact_ids": ["p340-global-water-table"], "section": "world-water-print", "related_sections": ["water-resource-basics"],
        "question_te": "పుట 340లోని printed global-water table గురించి సరైన statement ఏది?",
        "question_en": "Which statement correctly represents the printed global-water table on page 340?",
        "options_te": ["Oceans/saline lakes 97.20%; ice/glaciers 2.15%; groundwater 0.64%", "Oceans/saline lakes 96.20%; ice/glaciers 3.15%; groundwater 0.64%", "Ice/glaciers 97.20%; oceans/saline lakes 2.15%; groundwater 0.64%", "Groundwater 2.15%; ice/glaciers 0.64%; atmosphere 0.0085%"],
        "options_en": ["Oceans/saline lakes 97.20%; ice/glaciers 2.15%; groundwater 0.64%", "Oceans/saline lakes 96.20%; ice/glaciers 3.15%; groundwater 0.64%", "Ice/glaciers 97.20%; oceans/saline lakes 2.15%; groundwater 0.64%", "Groundwater 2.15%; ice/glaciers 0.64%; atmosphere 0.0085%"],
        "answer": 1,
        "explanation_te": "ముద్రిత tableలో oceans/saline lakes 97.20%, ice/glaciers 2.15%, groundwater 0.64%. ఇవి rounded historical values; all water, freshwater denominatorsను కలపకూడదు.",
        "explanation_en": "The printed table gives 97.20% for oceans/saline lakes, 2.15% for ice/glaciers and 0.64% for groundwater. These are rounded historical values; all-water and freshwater denominators must not be mixed.",
        "option_explanations_te": ["మూడు విలువలూ printed tableతో సరిపోతాయి.", "96.20%, 3.15% values printed tableవి కావు.", "Ocean, ice shares తారుమారయ్యాయి.", "Groundwater, ice, atmosphere values తప్పుగా కలిశాయి."],
        "option_explanations_en": ["All three values match the printed table.", "The table does not give 96.20% and 3.15%.", "It reverses the ocean and ice shares.", "It mismatches the groundwater, ice and atmospheric values."],
        "source_urls": [], "manual_review_status": "manually-authored-2026-11-01"
    },
    {
        "id": "IA07-034", "chapter": "IA-07", "origin": "book-audit-original", "kind": "matching-set", "difficulty": "hard", "language": "bilingual",
        "label": "Original PYQ-style practice; not an official previous-year question", "source_page": 341,
        "fact_ids": ["p341-bhakra-beas-dvc-components"], "section": "bhakra-beas-dvc", "related_sections": ["landmark-projects"],
        "question_te": "క్రింది project-component classificationలో సరైనది ఏది?",
        "question_en": "Which project-component classification is correct?",
        "options_te": ["Beas Project—Pong, Pandoh, Beas–Sutlej Link; DVC—Tilaiya, Konar, Maithon, Panchet", "Beas Project—Tilaiya, Konar; DVC—Pong, Pandoh", "Bhakra–Nangal—Damodar; DVC—Sutlej", "Beas Project—Sardar Sarovar, Indira Sagar; DVC—Mettur, Bhavani"],
        "options_en": ["Beas Project—Pong, Pandoh, Beas–Sutlej Link; DVC—Tilaiya, Konar, Maithon, Panchet", "Beas Project—Tilaiya, Konar; DVC—Pong, Pandoh", "Bhakra–Nangal—Damodar; DVC—Sutlej", "Beas Project—Sardar Sarovar, Indira Sagar; DVC—Mettur, Bhavani"],
        "answer": 1,
        "explanation_te": "Pong dam, Pandoh dam, Beas–Sutlej Link Beas Projectలో భాగాలు. Tilaiya, Konar, Maithon, Panchet Damodar Valley Corporation (DVC) dams.",
        "explanation_en": "Pong Dam, Pandoh Dam and the Beas–Sutlej Link form the Beas Project; Tilaiya, Konar, Maithon and Panchet are DVC dams.",
        "option_explanations_te": ["రెండు component sets సరైనవి.", "Beas, DVC components తారుమారయ్యాయి.", "Bhakra–Nangal Sutlejపై; DVC Damodar systemలో ఉంది.", "Narmada, Tamil Nadu projectsను తప్పుగా చేర్చింది."],
        "option_explanations_en": ["Both component sets are correct.", "It reverses the Beas and DVC components.", "Bhakra–Nangal is on the Sutlej; DVC is in the Damodar system.", "It wrongly inserts Narmada and Tamil Nadu projects."],
        "source_urls": [], "manual_review_status": "manually-authored-2026-11-01"
    },
    {
        "id": "IA07-035", "chapter": "IA-07", "origin": "book-audit-original", "kind": "matching-set", "difficulty": "hard", "language": "bilingual",
        "label": "Original PYQ-style practice; not an official previous-year question", "source_page": 343,
        "fact_ids": ["p343-kwdt-gwdt-allocations"], "section": "allocation-tables", "related_sections": ["tribunals"],
        "question_te": "పుట 343లోని printed tribunal allocation tables ప్రకారం సరైన సముదాయం ఏది?",
        "question_en": "According to the printed tribunal-allocation tables on page 343, which set is correct?",
        "options_te": ["KWDT-I: Maharashtra—585 TMC, Karnataka—734 TMC, undivided AP—811 TMC", "KWDT-I: Maharashtra—734 TMC, Karnataka—811 TMC, undivided AP—585 TMC", "GWDT: Maharashtra—625 TMC, undivided MP—889 TMC, Odisha—20 TMC", "GWDT: Karnataka—293 TMC, Odisha—20 TMC, undivided AP—625 TMC"],
        "options_en": ["KWDT-I: Maharashtra—585 TMC, Karnataka—734 TMC, undivided AP—811 TMC", "KWDT-I: Maharashtra—734 TMC, Karnataka—811 TMC, undivided AP—585 TMC", "GWDT: Maharashtra—625 TMC, undivided MP—889 TMC, Odisha—20 TMC", "GWDT: Karnataka—293 TMC, Odisha—20 TMC, undivided AP—625 TMC"],
        "answer": 1,
        "explanation_te": "Printed KWDT-I tableలో Maharashtra 585, Karnataka 734, undivided Andhra Pradesh 811 TMC. ఇవి post-bifurcation current entitlementగా నేరుగా వాడకూడదు.",
        "explanation_en": "The printed KWDT-I table gives Maharashtra 585, Karnataka 734 and undivided Andhra Pradesh 811 TMC. These should not be treated directly as present post-bifurcation entitlements.",
        "option_explanations_te": ["మూడు KWDT-I values సరైనవి.", "మూడు valuesను తారుమారుచేసింది.", "GWDTలో Maharashtra 889, undivided MP 625, Odisha 293 TMC.", "GWDTలో Karnataka 20, Odisha 293, undivided AP 1173 TMCగా print ఉంది."],
        "option_explanations_en": ["All three KWDT-I values are correct.", "It permutes all three values.", "GWDT prints Maharashtra 889, undivided MP 625 and Odisha 293 TMC.", "GWDT prints Karnataka 20, Odisha 293 and undivided AP 1173 TMC."],
        "source_urls": [], "manual_review_status": "manually-authored-2026-11-01"
    },
    {
        "id": "IA07-036", "chapter": "IA-07", "origin": "book-audit-original", "kind": "matching-set", "difficulty": "hard", "language": "bilingual",
        "label": "Original PYQ-style practice; not an official previous-year question", "source_page": 347,
        "fact_ids": ["p346-p349-telangana-project-rivers"], "section": "telangana-projects", "related_sections": ["joint-barrages"],
        "question_te": "క్రింది Telangana project–river/system జతల సముదాయాల్లో పూర్తిగా సరైనది ఏది?",
        "question_en": "Which Telangana project–river/system set is entirely correct?",
        "options_te": ["Sriramsagar—Godavari; Singur—Manjira; Rajolibanda—Tungabhadra; Palamuru–Rangareddy—Krishna/Srisailam lift", "Sriramsagar—Krishna; Singur—Godavari; Rajolibanda—Manjira; Palamuru–Rangareddy—Pennar", "Devadula—Krishna lift; Nizam Sagar—Tungabhadra; Sitarama—Manjira", "Ellampalli—Pennar; Ichampalli—Kaveri; Sammakka–Saralamma—Mahanadi"],
        "options_en": ["Sriramsagar—Godavari; Singur—Manjira; Rajolibanda—Tungabhadra; Palamuru–Rangareddy—Krishna/Srisailam lift", "Sriramsagar—Krishna; Singur—Godavari; Rajolibanda—Manjira; Palamuru–Rangareddy—Pennar", "Devadula—Krishna lift; Nizam Sagar—Tungabhadra; Sitarama—Manjira", "Ellampalli—Pennar; Ichampalli—Kaveri; Sammakka–Saralamma—Mahanadi"],
        "answer": 1,
        "explanation_te": "Sriramsagar Godavariపై, Singur Manjiraపై, Rajolibanda Tungabhadra systemలో, Palamuru–Rangareddy Krishna/Srisailam lift scheme.",
        "explanation_en": "Sriramsagar is on the Godavari, Singur on the Manjira, Rajolibanda in the Tungabhadra system, and Palamuru–Rangareddy is a Krishna/Srisailam lift scheme.",
        "option_explanations_te": ["నాలుగు జతలూ సరైనవి.", "నదులు, systems అన్నీ తప్పుగా మార్చారు.", "Devadula, Sitarama Godavari lifts; Nizam Sagar Manjiraపై ఉంది.", "Ellampalli, Ichampalli, Sammakka–Saralamma Godavari systemకు చెందినవి."],
        "option_explanations_en": ["All four pairs are correct.", "All rivers and systems are wrongly reassigned.", "Devadula and Sitarama are Godavari lifts; Nizam Sagar is on the Manjira.", "Ellampalli, Ichampalli and Sammakka–Saralamma belong to the Godavari system."],
        "source_urls": [], "manual_review_status": "manually-authored-2026-11-01"
    },
    {
        "id": "IA07-037", "chapter": "IA-07", "origin": "book-audit-original", "kind": "matching-set", "difficulty": "hard", "language": "bilingual",
        "label": "Original PYQ-style practice; not an official previous-year question", "source_page": 348,
        "fact_ids": ["p348-joint-barrage-shares"], "section": "joint-barrages", "related_sections": ["telangana-projects"],
        "question_te": "పుట 348లోని Telangana–Maharashtra printed shares ప్రకారం సరైన జతల సముదాయం ఏది?",
        "question_en": "According to the printed Telangana–Maharashtra shares on page 348, which set is correct?",
        "options_te": ["Lower Penganga—12:88; Chanaka–Korata—80:20; Rajapet—50:50", "Lower Penganga—88:12; Chanaka–Korata—20:80; Rajapet—70:30", "Pinpahad—38:62; Lendi—30:70; Rajapet—80:20", "Lower Penganga—50:50; Pinpahad—12:88; Lendi—80:20"],
        "options_en": ["Lower Penganga—12:88; Chanaka–Korata—80:20; Rajapet—50:50", "Lower Penganga—88:12; Chanaka–Korata—20:80; Rajapet—70:30", "Pinpahad—38:62; Lendi—30:70; Rajapet—80:20", "Lower Penganga—50:50; Pinpahad—12:88; Lendi—80:20"],
        "answer": 1,
        "explanation_te": "Printed tableలో Telangana:Maharashtra shares Lower Penganga 12:88, Chanaka–Korata 80:20, Rajapet 50:50. అలాగే Pinpahad 30:70, Lendi 38:62.",
        "explanation_en": "The printed Telangana:Maharashtra shares are Lower Penganga 12:88, Chanaka–Korata 80:20 and Rajapet 50:50; Pinpahad is 30:70 and Lendi 38:62.",
        "option_explanations_te": ["మూడు shares సరైనవి.", "Sharesను తారుమారుచేసి Rajapetను కూడా తప్పుగా ఇచ్చింది.", "Pinpahad, Lendi values పరస్పరం మార్చి Rajapetను తప్పుగా ఇచ్చింది.", "మూడు barragesకు తప్పు shares ఇచ్చింది."],
        "option_explanations_en": ["All three shares are correct.", "It reverses shares and also misstates Rajapet.", "It swaps the Pinpahad and Lendi values and misstates Rajapet.", "It assigns wrong shares to all three barrages."],
        "source_urls": [], "manual_review_status": "manually-authored-2026-11-01"
    },
    {
        "id": "IA07-038", "chapter": "IA-07", "origin": "book-audit-original", "kind": "matching-set", "difficulty": "hard", "language": "bilingual",
        "label": "Original PYQ-style practice; not an official previous-year question", "source_page": 365,
        "fact_ids": ["p365-ap-tank-river-pairs"], "section": "ap-pairs", "related_sections": ["ap-projects"],
        "question_te": "పుట 365 జతలలో పూర్తిగా సరైన set ఏది?",
        "question_en": "Which set reproduces the page 365 pairs correctly?",
        "options_te": ["Mantha Sagar—Nellore; Kumbham—Prakasam; Bukkapatnam—Sri Sathya Sai", "Mantha Sagar—Prakasam; Kumbham—Nellore; Bukkapatnam—Nandyal", "Polavaram—Krishna; Annavaram—Godavari; Nellore—Pampa", "Hirapuram—Pennar; Vijayawada Barrage—Vamsadhara; Sangam—Godavari"],
        "options_en": ["Mantha Sagar—Nellore; Kumbham—Prakasam; Bukkapatnam—Sri Sathya Sai", "Mantha Sagar—Prakasam; Kumbham—Nellore; Bukkapatnam—Nandyal", "Polavaram—Krishna; Annavaram—Godavari; Nellore—Pampa", "Hirapuram—Pennar; Vijayawada Barrage—Vamsadhara; Sangam—Godavari"],
        "answer": 1,
        "explanation_te": "Mantha Sagar Nellore, Kumbham Prakasam, Bukkapatnam Sri Sathya Sai జిల్లాలకు జతచేశారు. River pairsలో Polavaram–Godavari, Vijayawada–Krishna, Annavaram–Pampa ఉన్నాయి.",
        "explanation_en": "Mantha Sagar is paired with Nellore, Kumbham with Prakasam and Bukkapatnam with Sri Sathya Sai. River pairs include Polavaram–Godavari, Vijayawada–Krishna and Annavaram–Pampa.",
        "option_explanations_te": ["మూడు pairs సరైనవి.", "మూడు districtsను తప్పుగా మార్చింది.", "Polavaram–Godavari, Annavaram–Pampa, Nellore–Pennar కావాలి.", "Hirapuram–Vamsadhara, Vijayawada–Krishna; Sangam district pair Nandyal."],
        "option_explanations_en": ["All three pairs are correct.", "It wrongly permutes all three districts.", "The correct pairs are Polavaram–Godavari, Annavaram–Pampa and Nellore–Pennar.", "Hirapuram pairs with Vamsadhara and Vijayawada with Krishna; Sangam is paired with Nandyal district."],
        "source_urls": [], "manual_review_status": "manually-authored-2026-11-01"
    },
    {
        "id": "IA07-039", "chapter": "IA-07", "origin": "book-audit-original", "kind": "statement-set", "difficulty": "hard", "language": "bilingual",
        "label": "Original PYQ-style practice; not an official previous-year question", "source_page": 354,
        "fact_ids": ["p354-discharge-conversions"], "section": "water-units", "related_sections": [],
        "question_te": "నీటి discharge units గురించి సరైన statement ఏది?",
        "question_en": "Which statement about water-discharge units is correct?",
        "options_te": ["1 cusec = 1 m³/s; 1 cumec ≈ 0.0283 cusec", "1 cusec ≈ 0.0283168 m³/s; 1 cumec ≈ 35.3147 cusecs", "1 TMC/day = 1 cusec; 1 cumec = 1 litre/s", "Cusec volume unit మాత్రమే; cumec area unit"],
        "options_en": ["1 cusec = 1 m³/s; 1 cumec ≈ 0.0283 cusec", "1 cusec ≈ 0.0283168 m³/s; 1 cumec ≈ 35.3147 cusecs", "1 TMC/day = 1 cusec; 1 cumec = 1 litre/s", "Cusec is only a volume unit; cumec is an area unit"],
        "answer": 2,
        "explanation_te": "Cusec అంటే cubic foot per second; cumec అంటే cubic metre per second. అందువల్ల 1 cusec ≈ 0.0283168 m³/s, 1 cumec ≈ 35.3147 cusecs.",
        "explanation_en": "A cusec is a cubic foot per second and a cumec a cubic metre per second; therefore 1 cusec is about 0.0283168 m³/s and 1 cumec about 35.3147 cusecs.",
        "option_explanations_te": ["Conversionను తలకిందులు చేసింది.", "రెండు conversions సరైనవి.", "TMC/day సుమారు 11,574 cusecs; cumec 1 litre/s కాదు.", "Cusec, cumec రెండూ discharge-rate units."],
        "option_explanations_en": ["It reverses the conversion.", "Both conversions are correct.", "One TMC/day is about 11,574 cusecs; one cumec is not one litre/s.", "Both cusec and cumec are discharge-rate units."],
        "source_urls": [], "manual_review_status": "manually-authored-2026-11-01"
    },
    {
        "id": "IA07-040", "chapter": "IA-07", "origin": "book-audit-original", "kind": "matching-set", "difficulty": "hard", "language": "bilingual",
        "label": "Original PYQ-style practice; not an official previous-year question", "source_page": 366,
        "fact_ids": ["p366-himalayan-links"], "section": "himalayan-links", "related_sections": ["peninsular-links"],
        "question_te": "క్రింది setsలో పూర్తిగా Himalayan Component links మాత్రమే ఉన్నది ఏది?",
        "question_en": "Which set consists entirely of Himalayan Component links?",
        "options_te": ["Kosi–Mechi; Ghaghara–Yamuna; Manas–Sankosh–Tista–Ganga", "Ken–Betwa; Par–Tapi–Narmada; Damanganga–Pinjal", "Mahanadi–Godavari; Kosi–Ghaghara; Bedti–Varada", "Srisailam–Pennar; Farakka–Sundarbans; Kaveri–Vaigai–Gundar"],
        "options_en": ["Kosi–Mechi; Ghaghara–Yamuna; Manas–Sankosh–Tista–Ganga", "Ken–Betwa; Par–Tapi–Narmada; Damanganga–Pinjal", "Mahanadi–Godavari; Kosi–Ghaghara; Bedti–Varada", "Srisailam–Pennar; Farakka–Sundarbans; Kaveri–Vaigai–Gundar"],
        "answer": 1,
        "explanation_te": "Kosi–Mechi, Ghaghara–Yamuna, Manas–Sankosh–Tista–Ganga మూడు Himalayan Componentలో ఉన్నాయి. Ken–Betwa సహా మిగిలిన optionsలో Peninsular links ఉన్నాయి.",
        "explanation_en": "Kosi–Mechi, Ghaghara–Yamuna and Manas–Sankosh–Tista–Ganga are all Himalayan Component links. The other options include Peninsular links, including Ken–Betwa.",
        "option_explanations_te": ["మూడు links Himalayan Componentలో ఉన్నాయి.", "మూడు Peninsular links.", "Kosi–Ghaghara మాత్రమే Himalayan; మిగతావి Peninsular.", "Farakka–Sundarbans మాత్రమే Himalayan; మిగతావి Peninsular."],
        "option_explanations_en": ["All three belong to the Himalayan Component.", "All three are Peninsular links.", "Only Kosi–Ghaghara is Himalayan; the others are Peninsular.", "Only Farakka–Sundarbans is Himalayan; the others are Peninsular."],
        "source_urls": ["https://nwda.gov.in/"], "manual_review_status": "manually-authored-2026-11-01"
    }
]

existing = {q["id"] for q in bank["questions"]}
for question in new_questions:
    if question["id"] not in existing:
        bank["questions"].append(question)

# Correct a semantic wording defect found during the final individual review.
for question in bank["questions"]:
    if question["id"] == "IA07-028":
        question["explanation_te"] = "రెండవ setలోని మూడు links Peninsular Componentకు చెందినవి. ఇతర setsలో Himalayan links కలిశాయి."
        question["explanation_en"] = "All three links in the second set belong to the Peninsular Component; each other set mixes in Himalayan links."

path.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="")
