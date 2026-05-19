"""
Seed: Reports & Indices Current Affairs MCQs
IDs 28001–28105 | Topic: National_Current_Affairs
Run standalone: python seed_reports_mcq.py
Auto-run: called from app.py init_db()
Last refresh: 2026-05-19 — replaced 2024 indices with 2025 values; added MCQs
28081–28105 for UNEP, SOFI, WMO, MPI, B-READY, GII 2025, Henley, GPI 2025,
Gender Gap 2025, HDI 2025, EIU 2024, Happiness 2025, WHO TB 2025.
"""

import os, sys

DATABASE_URL = os.environ.get('DATABASE_URL', '')
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
USE_POSTGRES = bool(DATABASE_URL)

if USE_POSTGRES:
    import psycopg2
    import psycopg2.extras
else:
    import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')


def get_conn():
    if USE_POSTGRES:
        return psycopg2.connect(DATABASE_URL)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _fv(row):
    if row is None:
        return 0
    if isinstance(row, dict):
        return list(row.values())[0]
    return list(row)[0]


QUESTIONS = [
    # ── Press Freedom ──
    (28001, "Which organisation publishes the World Press Freedom Index?",
     "UNESCO", "UNDP", "Reporters Without Borders (RSF)", "Freedom House",
     "C", "The World Press Freedom Index is published annually by RSF (Reporters Sans Frontières / Reporters Without Borders), headquartered in Paris, France.",
     "AP_HC", "International_Current_Affairs"),

    (28002, "What was India's rank in the World Press Freedom Index 2025?",
     "131", "143", "151", "162",
     "C", "India ranked 151 out of 180 countries in the World Press Freedom Index 2025 published by RSF.",
     "AP_HC", "International_Current_Affairs"),

    (28003, "Which country ranked 1st in the World Press Freedom Index 2025?",
     "Norway", "Sweden", "Finland", "Denmark",
     "C", "Finland topped the World Press Freedom Index 2025. The top three positions were Finland, Estonia, and Netherlands.",
     "AP_HC", "International_Current_Affairs"),

    (28004, "What was the USA's rank in the World Press Freedom Index 2025?",
     "45", "57", "63", "72",
     "B", "The United States ranked 57th in the World Press Freedom Index 2025 published by RSF.",
     "AP_HC", "International_Current_Affairs"),

    (28005, "RSF, which publishes the Press Freedom Index, is headquartered in which city?",
     "Geneva", "New York", "Brussels", "Paris",
     "D", "RSF (Reporters Without Borders / Reporters Sans Frontières) is headquartered in Paris, France.",
     "AP_HC", "International_Current_Affairs"),

    # ── Food Security ──
    (28006, "The Global Report on Food Crises (GRFC) 2025 was published by which body?",
     "FAO alone", "WFP alone", "GNAFC and FSIN", "UNICEF and WHO",
     "C", "The GRFC 2025 was published jointly by GNAFC (Global Network Against Food Crises) and FSIN (Food Security Information Network).",
     "AP_HC", "International_Current_Affairs"),

    (28007, "According to the Global Report on Food Crises 2025, how many people faced acute hunger?",
     "225 million in 45 countries", "261 million in 50 countries", "295 million in 53 countries", "318 million in 58 countries",
     "C", "GRFC 2025 reported that approximately 295 million people in 53 countries/territories faced acute food insecurity.",
     "AP_HC", "International_Current_Affairs"),

    (28008, "The Global Hunger Index (GHI) is published by which organisations?",
     "FAO and WFP", "Concern Worldwide and Welthungerhilfe", "UNDP and UNICEF", "World Bank and IMF",
     "B", "The Global Hunger Index is published jointly by Concern Worldwide (Ireland) and Welthungerhilfe (Germany).",
     "AP_HC", "International_Current_Affairs"),

    (28009, "India's rank in the Global Hunger Index 2025 was 102/123, with a score of 25.8, placing India in which category?",
     "Moderate", "Serious", "Alarming", "Extremely Alarming",
     "B", "India ranked 102 out of 123 countries in the Global Hunger Index 2025 with a score of 25.8, placing it in the 'Serious' category. (Released October 2025 by Concern Worldwide + Welthungerhilfe.)",
     "AP_HC", "International_Current_Affairs"),

    (28010, "The State of Food Security and Nutrition in the World (SOFI) report is jointly published by which five UN bodies?",
     "UN DESA, UNDP, UNICEF, WHO, WFP", "FAO, IFAD, UNICEF, WFP, WHO", "UNESCO, ILO, FAO, WFP, UNHCR", "FAO, WHO, UNCTAD, ILO, UNFPA",
     "B", "The SOFI report is jointly published by FAO, IFAD, UNICEF, WFP, and WHO.",
     "AP_HC", "International_Current_Affairs"),

    # ── Climate Change Performance Index ──
    (28011, "Which organisation publishes the Climate Change Performance Index (CCPI)?",
     "UNEP alone", "Germanwatch, NewClimate Institute and CAN International", "World Bank and IEA", "IPCC",
     "B", "The CCPI is published by Germanwatch, NewClimate Institute, and Climate Action Network (CAN) International.",
     "AP_HC", "International_Current_Affairs"),

    (28012, "India's rank in the Climate Change Performance Index (CCPI) 2025 was:",
     "4th", "7th", "10th", "15th",
     "C", "India ranked 10th in the CCPI 2025, making it one of the better-performing major economies.",
     "AP_HC", "International_Current_Affairs"),

    (28013, "Why are the top 3 positions in the CCPI always left empty?",
     "Data for top countries is classified", "No country performs sufficiently in all four categories", "Countries at top refused data sharing", "Methodological revision is ongoing",
     "B", "The CCPI tradition is that positions 1–3 are intentionally vacant because no country performs sufficiently in all four assessment categories: GHG emissions, energy use, renewable energy, and climate policy.",
     "AP_HC", "International_Current_Affairs"),

    (28014, "Which country ranked 4th in the Climate Change Performance Index 2025?",
     "Norway", "Germany", "Denmark", "Sweden",
     "C", "Denmark ranked 4th in the CCPI 2025 — effectively the highest real rank since positions 1–3 are kept empty.",
     "AP_HC", "International_Current_Affairs"),

    (28015, "India's score in the CCPI 2025 for Renewable Energy was categorised as:",
     "Very High", "High", "Medium", "Low",
     "D", "In CCPI 2025, India's renewable energy score was rated 'Low', while GHG emissions and energy use were rated 'High' and climate policy 'Medium'.",
     "AP_HC", "International_Current_Affairs"),

    # ── Energy & Carbon Reports ──
    (28016, "Which body published the World Energy Investment Report 2025?",
     "IRENA", "IEA", "World Bank", "UNCTAD",
     "B", "The World Energy Investment Report 2025 was published by the IEA (International Energy Agency), headquartered in Paris.",
     "AP_HC", "International_Current_Affairs"),

    (28017, "According to World Energy Investment Report 2025, total global energy investment reached:",
     "$2.1 trillion", "$2.7 trillion", "$3.3 trillion", "$4.0 trillion",
     "C", "Global energy investment reached $3.3 trillion in 2025 according to the IEA report.",
     "AP_HC", "International_Current_Affairs"),

    (28018, "In the World Energy Investment Report 2025, clean energy investment was approximately:",
     "$1.1 trillion", "$1.6 trillion", "$2.2 trillion", "$2.8 trillion",
     "C", "Clean energy investment stood at $2.2 trillion — exactly double the fossil fuel investment of $1.1 trillion.",
     "AP_HC", "International_Current_Affairs"),

    (28019, "Which country led global clean energy investment according to the IEA World Energy Investment Report 2025?",
     "USA", "Germany", "India", "China",
     "D", "China led global clean energy investment, accounting for a significant share of the $2.2 trillion in clean energy spending.",
     "AP_HC", "International_Current_Affairs"),

    (28020, "The IEA (International Energy Agency) is headquartered in which city?",
     "Vienna", "Brussels", "Paris", "Geneva",
     "C", "The International Energy Agency (IEA) is headquartered in Paris, France.",
     "AP_HC", "International_Current_Affairs"),

    (28021, "The 'State and Trends of Carbon Pricing 2025' report was published by which organisation?",
     "UNEP", "IEA", "World Bank", "IPCC",
     "C", "The State and Trends of Carbon Pricing 2025 was published by the World Bank.",
     "AP_HC", "International_Current_Affairs"),

    (28022, "According to the Carbon Pricing Report 2025, how many active carbon pricing instruments exist globally?",
     "40", "60", "80", "100",
     "C", "There are 80 active carbon pricing instruments globally (up from just 5 in 2005), according to World Bank's Carbon Pricing report 2025.",
     "AP_HC", "International_Current_Affairs"),

    (28023, "The carbon pricing mechanisms cover what percentage of global GHG emissions as per the 2025 World Bank report?",
     "15%", "21%", "28%", "35%",
     "C", "Active carbon pricing mechanisms cover 28% of global greenhouse gas emissions according to the World Bank report 2025.",
     "AP_HC", "International_Current_Affairs"),

    (28024, "IRENA, which publishes Renewable Energy Statistics, is headquartered in:",
     "Geneva, Switzerland", "Paris, France", "Abu Dhabi, UAE", "Vienna, Austria",
     "C", "IRENA (International Renewable Energy Agency) is headquartered in Abu Dhabi, UAE.",
     "AP_HC", "International_Current_Affairs"),

    # ── Social Security & Population ──
    (28025, "According to ILO data, India ranked _____ globally for the number of people covered under social security.",
     "1st", "2nd", "3rd", "5th",
     "B", "India ranked 2nd globally (ILO ILOSTAT) for the absolute number of people covered under social security — approximately 940 million people.",
     "AP_HC", "International_Current_Affairs"),

    (28026, "India's social security coverage grew from 19% (2015) to what percentage by 2025?",
     "45.6%", "54.2%", "64.3%", "72.1%",
     "C", "India's social security coverage grew from 19% in 2015 to 64.3% in 2025 — the fastest expansion in the world.",
     "AP_HC", "International_Current_Affairs"),

    (28027, "UNFPA's State of World Population (SOWP) 2025 report was themed:",
     "The Ageing World", "Population Without Borders", "The Real Fertility Crisis", "7 Billion and Beyond",
     "C", "UNFPA's SOWP 2025 was themed 'The Real Fertility Crisis', highlighting that both very high and very low fertility pose challenges.",
     "AP_HC", "International_Current_Affairs"),

    (28028, "UNFPA stands for:",
     "UN Food and Population Agency", "UN Fund for Population Activities", "United Nations Population Fund", "Universal Family Planning Agency",
     "C", "UNFPA stands for United Nations Population Fund (formerly United Nations Fund for Population Activities).",
     "AP_HC", "International_Current_Affairs"),

    (28029, "According to UNHCR Global Trends 2024, how many people were forcibly displaced worldwide?",
     "97.3 million", "110.8 million", "123.2 million", "135.6 million",
     "C", "UNHCR's Global Trends 2024 reported a record 123.2 million forcibly displaced people worldwide.",
     "AP_HC", "International_Current_Affairs"),

    (28030, "What percentage of forcibly displaced persons globally were children, as per UNHCR 2024?",
     "25%", "33%", "40%", "48%",
     "C", "According to UNHCR Global Trends 2024, children constituted approximately 40% of all forcibly displaced persons.",
     "AP_HC", "International_Current_Affairs"),

    (28031, "How many people were Internally Displaced Persons (IDPs) according to UNHCR 2024?",
     "61.5 million", "68.2 million", "73.5 million", "80.1 million",
     "C", "73.5 million people were internally displaced within their own countries according to UNHCR's Global Trends 2024.",
     "AP_HC", "International_Current_Affairs"),

    (28032, "Which country was the top source of forcibly displaced people according to UNHCR 2024?",
     "Syria", "Afghanistan", "Sudan", "Ukraine",
     "C", "Sudan became the top source of forcibly displaced people globally in 2024, surpassing previous leaders Syria and Afghanistan.",
     "AP_HC", "International_Current_Affairs"),

    (28033, "The Global Education Monitoring (GEM) Report is published by which organisation?",
     "UNICEF", "UNESCO", "World Bank", "UNDP",
     "B", "The GEM Report is published by UNESCO (UN Educational, Scientific and Cultural Organization), headquartered in Paris.",
     "AP_HC", "International_Current_Affairs"),

    (28034, "According to the UNESCO GEM Report, how many children are out of school globally?",
     "198 million", "235 million", "272 million", "308 million",
     "C", "The UNESCO Global Education Monitoring Report states that approximately 272 million children are currently out of school worldwide.",
     "AP_HC", "International_Current_Affairs"),

    # ── Economic Reports ──
    (28035, "The UN World Economic Situation and Prospects (WESP) 2025 was published by:",
     "UN DESA", "IMF", "World Bank", "UNCTAD",
     "A", "WESP 2025 is published by UN DESA (Department of Economic and Social Affairs).",
     "AP_HC", "International_Current_Affairs"),

    (28036, "What global GDP growth rate did WESP 2025 project for 2025?",
     "1.8%", "2.4%", "3.1%", "3.8%",
     "B", "WESP 2025 projected global GDP growth of 2.4% for 2025.",
     "AP_HC", "International_Current_Affairs"),

    (28037, "India's GDP growth rate projected in UN WESP 2025 was:",
     "5.1%", "5.9%", "6.3%", "7.2%",
     "C", "India's GDP growth was projected at 6.3% in WESP 2025, making it the fastest-growing major economy.",
     "AP_HC", "International_Current_Affairs"),

    (28038, "UNCTAD's 'World of Debt' report revealed global public debt reached:",
     "$78 trillion", "$92 trillion", "$102 trillion", "$115 trillion",
     "C", "UNCTAD's World of Debt report revealed global public debt reached a record $102 trillion.",
     "AP_HC", "International_Current_Affairs"),

    (28039, "UNCTAD is headquartered in:",
     "New York, USA", "Geneva, Switzerland", "Vienna, Austria", "Paris, France",
     "B", "UNCTAD (United Nations Conference on Trade and Development) is headquartered in Geneva, Switzerland.",
     "AP_HC", "International_Current_Affairs"),

    (28040, "Which report replaced the World Bank's discontinued Ease of Doing Business report?",
     "Global Business Index", "Business Friendly Report", "Business Ready (B-READY)", "World Competitiveness Yearbook",
     "C", "The World Bank replaced the Ease of Doing Business report (discontinued in 2021 due to data irregularities) with the Business Ready (B-READY) report, first edition released in 2024.",
     "AP_HC", "International_Current_Affairs"),

    # ── Fisheries ──
    (28041, "Which organisation published the 'Review of the State of World Marine Fishery Resources 2025'?",
     "UNEP", "UNDP", "FAO", "WWF",
     "C", "The Review of the State of World Marine Fishery Resources is published by FAO (Food and Agriculture Organization), headquartered in Rome.",
     "AP_HC", "International_Current_Affairs"),

    (28042, "According to FAO's marine fisheries report 2025, what percentage of fish stocks are being fished at biologically sustainable levels?",
     "55.2%", "60.1%", "64.5%", "71.3%",
     "C", "64.5% of fish stocks were being fished within biologically sustainable levels according to FAO's marine fisheries report 2025.",
     "AP_HC", "International_Current_Affairs"),

    (28043, "What percentage of global marine fish stocks are overfished according to FAO 2025?",
     "18.5%", "28.3%", "35.5%", "42.1%",
     "C", "35.5% of global marine fish stocks are overfished according to FAO's 2025 marine fisheries review.",
     "AP_HC", "International_Current_Affairs"),

    (28044, "FAO's biennial fisheries publication covering both marine and aquaculture is known as:",
     "SOFIA", "GRFC", "SOFI", "SIFA",
     "A", "SOFIA (The State of World Fisheries and Aquaculture) is FAO's biennial publication covering global fisheries and aquaculture.",
     "AP_HC", "International_Current_Affairs"),

    # ── Military & Nuclear ──
    (28045, "SIPRI is headquartered in which city?",
     "Stockholm (Solna), Sweden", "Oslo, Norway", "Copenhagen, Denmark", "Helsinki, Finland",
     "A", "SIPRI (Stockholm International Peace Research Institute) is headquartered in Solna, near Stockholm, Sweden.",
     "AP_HC", "International_Current_Affairs"),

    (28046, "According to SIPRI Yearbook 2025, Russia possesses how many nuclear warheads?",
     "4,612", "5,177", "5,459", "6,213",
     "C", "Russia has 5,459 nuclear warheads according to the SIPRI Yearbook 2025.",
     "AP_HC", "International_Current_Affairs"),

    (28047, "How many nuclear warheads does the USA possess according to SIPRI 2025?",
     "4,823", "5,177", "5,459", "5,800",
     "B", "The USA possesses 5,177 nuclear warheads according to SIPRI Yearbook 2025.",
     "AP_HC", "International_Current_Affairs"),

    (28048, "Global military expenditure reached what record level in 2024 according to SIPRI?",
     "$1.8 trillion", "$2.1 trillion", "$2.4 trillion", "$2.8 trillion",
     "C", "Global military expenditure reached a record ~$2.4 trillion in 2024 according to SIPRI.",
     "AP_HC", "International_Current_Affairs"),

    (28049, "The Global Peace Index is published by which organisation?",
     "SIPRI", "IEP (Institute for Economics and Peace)", "UNDP", "UN Security Council",
     "B", "The Global Peace Index is published by IEP (Institute for Economics and Peace), headquartered in Sydney, Australia.",
     "AP_HC", "International_Current_Affairs"),

    (28050, "Which country consistently tops the Global Peace Index?",
     "Switzerland", "Denmark", "Iceland", "New Zealand",
     "C", "Iceland consistently tops the Global Peace Index as the world's most peaceful country.",
     "AP_HC", "International_Current_Affairs"),

    # ── SDG & Governance ──
    (28051, "India's rank in the India SDG Index 2025 (global) was:",
     "105th", "99th", "112th", "87th",
     "B", "India ranked 99th in the SDG Index 2025 — the first time India entered the top 100.",
     "AP_HC", "International_Current_Affairs"),

    (28052, "Who publishes the India SDG Index?",
     "Ministry of Statistics", "NITI Aayog", "Planning Commission", "UNDP India",
     "B", "The India SDG Index is published by NITI Aayog (National Institution for Transforming India).",
     "AP_HC", "International_Current_Affairs"),

    (28053, "India's SDG overall score improved from 57 in 2018 to what in 2025?",
     "62", "66", "71", "78",
     "C", "India's SDG overall score improved from 57 in 2018 to 71 in 2025 according to NITI Aayog's India SDG Index.",
     "AP_HC", "International_Current_Affairs"),

    (28054, "The Performance Grading Index (PGI) 2.0 for school education is published by:",
     "NITI Aayog", "Ministry of Education", "University Grants Commission", "NCERT",
     "B", "The PGI 2.0 for school education is published by the Ministry of Education, Government of India.",
     "AP_HC", "International_Current_Affairs"),

    (28055, "Which state/UT topped the Performance Grading Index (PGI) 2.0?",
     "Delhi", "Kerala", "Chandigarh", "Tamil Nadu",
     "C", "Chandigarh (UT) topped the Performance Grading Index (PGI) 2.0.",
     "AP_HC", "International_Current_Affairs"),

    (28056, "Which state was at the bottom of the Performance Grading Index (PGI) 2.0?",
     "Bihar", "Meghalaya", "Jharkhand", "Nagaland",
     "B", "Meghalaya was at the bottom of the Performance Grading Index (PGI) 2.0.",
     "AP_HC", "International_Current_Affairs"),

    (28057, "The PGI 2.0 uses how many indicators across 6 domains?",
     "55 indicators, 800 points", "73 indicators, 1000 points", "80 indicators, 900 points", "65 indicators, 750 points",
     "B", "PGI 2.0 uses 73 indicators spread across 6 domains for a total score of 1000 points.",
     "AP_HC", "International_Current_Affairs"),

    (28058, "The Corruption Perceptions Index (CPI) is published by:",
     "World Bank", "Transparency International", "UNDP", "WEF",
     "B", "The Corruption Perceptions Index is published by Transparency International, headquartered in Berlin, Germany.",
     "AP_HC", "International_Current_Affairs"),

    (28059, "India's rank in the Corruption Perceptions Index 2024 (released Feb 2025) was:",
     "73", "85", "96", "107",
     "C", "India ranked 96 out of 180 countries in the CPI 2024 with a score of 38 (down from rank 93 / score 39 in 2023). Denmark topped, followed by Finland and Singapore.",
     "AP_HC", "International_Current_Affairs"),

    (28060, "Which country topped the Corruption Perceptions Index 2024 (least corrupt)?",
     "Finland", "Norway", "Denmark", "Singapore",
     "C", "Denmark topped the CPI 2024 as the least corrupt country. The scale goes from 0 (highly corrupt) to 100 (very clean).",
     "AP_HC", "International_Current_Affairs"),

    # ── Innovation & Competitiveness ──
    (28061, "The Global Innovation Index (GII) is published by:",
     "WEF", "UNDP", "WIPO", "World Bank",
     "C", "The Global Innovation Index is published by WIPO (World Intellectual Property Organization), headquartered in Geneva.",
     "AP_HC", "International_Current_Affairs"),

    (28062, "India's rank in the WIPO Global Innovation Index 2025 was:",
     "29th", "38th", "49th", "55th",
     "B", "India ranked 38th out of 139 economies in the GII 2025 — improving by one position from rank 39 in 2024 and from rank 81 in 2015. India remains the top-performing lower-middle-income economy.",
     "AP_HC", "International_Current_Affairs"),

    (28063, "Which country topped the WIPO Global Innovation Index 2025?",
     "USA", "Germany", "Sweden", "Switzerland",
     "D", "Switzerland topped the GII 2025 (its 15th consecutive year at the top), followed by Sweden and the USA.",
     "AP_HC", "International_Current_Affairs"),

    (28064, "The Global Competitiveness Report is published by which organisation?",
     "World Bank", "IMF", "World Economic Forum (WEF)", "OECD",
     "C", "The Global Competitiveness Report is published by the World Economic Forum (WEF), headquartered in Cologny near Geneva, Switzerland.",
     "AP_HC", "International_Current_Affairs"),

    # ── HDI & Gender ──
    (28065, "The Human Development Index (HDI) is published by:",
     "World Bank", "UNDP", "UNFPA", "UN DESA",
     "B", "The Human Development Index is published by UNDP (United Nations Development Programme).",
     "AP_HC", "International_Current_Affairs"),

    (28066, "India's rank in the UNDP Human Development Report 2025 (released May 2025) was:",
     "112", "125", "130", "142",
     "C", "India ranked 130 out of 193 countries in the HDI 2025 report, with an HDI value of 0.685 (up from 0.676 in 2022). It remains in the 'Medium Human Development' category, close to the 0.700 threshold for 'High'.",
     "AP_HC", "International_Current_Affairs"),

    (28067, "The HDI measures three dimensions of human development. Which of the following is NOT one of them?",
     "Life expectancy", "Education (years of schooling)", "Per-capita income (GNI)", "Environmental sustainability",
     "D", "HDI measures Life Expectancy, Education (mean + expected years of schooling), and GNI per capita. Environmental sustainability is NOT a direct HDI measure.",
     "AP_HC", "International_Current_Affairs"),

    (28068, "The Gender Gap Report is published by:",
     "UNDP", "UN Women", "World Economic Forum (WEF)", "ILO",
     "C", "The Gender Gap Report is published by the World Economic Forum (WEF).",
     "AP_HC", "International_Current_Affairs"),

    (28069, "India's rank in the WEF Global Gender Gap Report 2025 was:",
     "114th", "122nd", "131st", "138th",
     "C", "India ranked 131 out of 148 countries in the Global Gender Gap Report 2025 (parity score 64.1%) — a drop of 2 ranks from 129 in 2024, mainly due to falling political empowerment. Iceland topped for the 16th consecutive year.",
     "AP_HC", "International_Current_Affairs"),

    (28070, "Which country consistently tops the Global Gender Gap Report?",
     "Norway", "Sweden", "Finland", "Iceland",
     "D", "Iceland consistently tops the Global Gender Gap Report. It has led the index for over a decade.",
     "AP_HC", "International_Current_Affairs"),

    # ── Happiness & Logistics ──
    (28071, "The World Happiness Report is published by:",
     "UNDP", "UN Sustainable Development Solutions Network (UNSDSN)", "WHO", "WEF",
     "B", "The World Happiness Report is published by the UN Sustainable Development Solutions Network (UNSDSN).",
     "AP_HC", "International_Current_Affairs"),

    (28072, "Which country topped the World Happiness Report 2025 for the 8th consecutive year?",
     "Norway", "Iceland", "Denmark", "Finland",
     "D", "Finland topped the World Happiness Report 2025 for the 8th consecutive year.",
     "AP_HC", "International_Current_Affairs"),

    (28073, "The Logistics Performance Index (LPI) is published by which organisation?",
     "IMF", "UNCTAD", "World Bank", "ILO",
     "C", "The Logistics Performance Index is published by the World Bank.",
     "AP_HC", "International_Current_Affairs"),

    (28074, "India's rank in the Logistics Performance Index 2023 was:",
     "30th", "38th", "44th", "52nd",
     "B", "India ranked 38th in the Logistics Performance Index 2023, improving from 44th in 2018.",
     "AP_HC", "International_Current_Affairs"),

    # ── Health ──
    (28075, "The Global TB Report is published by which organisation?",
     "UNICEF", "WHO", "Ministry of Health India", "UNDP",
     "B", "The Global TB Report is published annually by WHO (World Health Organization).",
     "AP_HC", "International_Current_Affairs"),

    (28076, "According to WHO Global TB Report 2025, India accounts for approximately what share of global TB cases?",
     "16%", "20%", "25%", "32%",
     "C", "India accounts for approximately 25% of global TB cases per WHO Global TB Report 2025, retaining the highest TB burden globally. India's TB incidence fell 21% from 237/lakh (2015) to 187/lakh (2024).",
     "AP_HC", "International_Current_Affairs"),

    (28077, "India's national target year to eliminate TB (set ahead of the global SDG target of 2030) was:",
     "2023", "2025", "2027", "2030",
     "B", "India set 2025 as its TB elimination target (5 years ahead of the global SDG target of 2030). As of 2025, while the target was not fully met, India achieved a 21% drop in incidence and 92% treatment coverage per WHO Global TB Report 2025.",
     "AP_HC", "International_Current_Affairs"),

    (28078, "According to NFHS-5 (2019–21), India's Total Fertility Rate (TFR) stood at:",
     "1.8", "2.0", "2.3", "2.5",
     "B", "India's TFR was 2.0 in NFHS-5 (2019–21), falling below the replacement level of 2.1 for the first time.",
     "AP_HC", "International_Current_Affairs"),

    # ── Mixed / Publisher Identification ──
    (28079, "Which of the following reports is published by the IMF?",
     "World Energy Investment Report", "World Economic Outlook", "State and Trends of Carbon Pricing", "Global Report on Food Crises",
     "B", "The World Economic Outlook (WEO) is published by the IMF (International Monetary Fund). IEA publishes WEI Report; World Bank publishes Carbon Pricing; GNAFC+FSIN publish GRFC.",
     "AP_HC", "International_Current_Affairs"),

    (28080, "The Democracy Index which classifies countries into Full Democracy, Flawed Democracy, Hybrid Regime, and Authoritarian is published by:",
     "Freedom House", "Transparency International", "Economist Intelligence Unit (EIU)", "IEP",
     "C", "The Democracy Index is published by the EIU (Economist Intelligence Unit), the research arm of The Economist group.",
     "AP_HC", "International_Current_Affairs"),

    # ── 2025-26 FRESHNESS GAP-FILL (added May 19, 2026) ──

    # EIU Democracy Index 2024 (released Feb 2025)
    (28081, "In the EIU Democracy Index 2024 (released Feb 2025), India's rank and classification were:",
     "39th — Full Democracy", "41st — Flawed Democracy", "53rd — Hybrid Regime", "108th — Authoritarian",
     "B", "India ranked 41st with a score of 7.29 in the EIU Democracy Index 2024, retaining its 'Flawed Democracy' classification (held since 2010). India has been classified as a flawed democracy since 2010.",
     "AP_HC", "International_Current_Affairs"),

    # Henley Passport Index 2025
    (28082, "Which country topped the Henley Passport Index 2025?",
     "Japan", "Germany", "Singapore", "Switzerland",
     "C", "Singapore topped the Henley Passport Index 2025 with visa-free access to 193 destinations out of 227 globally.",
     "AP_HC", "International_Current_Affairs"),

    (28083, "India's rank in the Henley Passport Index 2025 (Q4) was:",
     "59th", "77th", "85th", "97th",
     "C", "India slipped to 85th in the Henley Passport Index 2025 (Q4, Oct 2025), sharing the position with Mauritania and offering visa-free access to 57 countries. India had briefly improved to 77th in Q2 2025.",
     "AP_HC", "International_Current_Affairs"),

    # Global Peace Index 2025
    (28084, "India's rank in the Global Peace Index 2025 published by IEP was:",
     "104th", "115th", "126th", "139th",
     "B", "India ranked 115 out of 163 countries in the Global Peace Index 2025, improving from rank 116 in 2024. Iceland topped the index for the 18th consecutive year, followed by Ireland and New Zealand.",
     "AP_HC", "International_Current_Affairs"),

    # World Happiness Report 2025 — India rank
    (28085, "India's rank in the World Happiness Report 2025 was:",
     "98th", "108th", "118th", "126th",
     "C", "India ranked 118 out of 147 countries in the World Happiness Report 2025 (score 4.389), up from 126 in 2024. India still lagged behind Nepal (92) and Pakistan (109).",
     "AP_HC", "International_Current_Affairs"),

    # World Happiness Report 2025 — Top 3
    (28086, "The top three countries in the World Happiness Report 2025 were:",
     "Finland, Iceland, Sweden", "Finland, Denmark, Iceland", "Norway, Finland, Denmark", "Denmark, Finland, Switzerland",
     "B", "World Happiness Report 2025: 1) Finland (8th consecutive year), 2) Denmark, 3) Iceland. Scores based on GDP per capita, social support, healthy life expectancy, freedom, generosity, and perceptions of corruption.",
     "AP_HC", "International_Current_Affairs"),

    # SDG Index 2025 score
    (28087, "India's score in the UN Sustainable Development Report (SDG Index) 2025, in which it ranked 99th, was approximately:",
     "57", "62", "67", "74",
     "C", "India scored 67 in the SDG Index 2025 published by UN SDSN, ranking 99/167 — the first time India entered the global top 100 (up from 109th in 2024 and 120th in 2021).",
     "AP_HC", "International_Current_Affairs"),

    # SIPRI 2025 — India warheads
    (28088, "According to SIPRI Yearbook 2025, at the start of 2025 the total global nuclear warhead stockpile (across 9 nuclear states) was approximately:",
     "9,500", "12,241", "15,800", "19,200",
     "B", "SIPRI Yearbook 2025 estimated approximately 12,241 nuclear warheads across the 9 nuclear-armed states (USA, Russia, UK, France, China, India, Pakistan, North Korea, Israel), of which 9,614 were considered potentially operationally available.",
     "AP_HC", "International_Current_Affairs"),

    # SIPRI 2025 — India and China
    (28089, "According to SIPRI Yearbook 2025, India:",
     "Reduced its arsenal in 2024", "Slightly expanded its arsenal in 2024 and is developing canisterised MIRV-capable missiles", "Joined the NPT", "Achieved nuclear parity with China",
     "B", "SIPRI Yearbook 2025 noted India slightly expanded its nuclear arsenal in 2024 and is developing 'canisterised' missiles potentially capable of carrying multiple warheads (MIRVs).",
     "AP_HC", "International_Current_Affairs"),

    # UNHCR Mid-Year Trends 2025
    (28090, "According to UNHCR Mid-Year Trends 2025, the number of forcibly displaced people at end-June 2025 was:",
     "97.3 million — first decline in a decade", "110.4 million — slight rise", "117.3 million — first decline in a decade", "131.8 million — record high",
     "C", "UNHCR Mid-Year Trends 2025 reported 117.3 million forcibly displaced at end-June 2025 — a decline of 5.9 million (~5%) from end-2024, the first decline in over a decade, driven by returns to Afghanistan, DRC, Sudan and Syria.",
     "AP_HC", "International_Current_Affairs"),

    # UNEP Emissions Gap 2025
    (28091, "The UNEP Emissions Gap Report 2025 (released Nov 2025) projected global temperature rise this century, under full implementation of current NDCs, at:",
     "1.5°C", "1.8–2.0°C", "2.3–2.5°C", "3.1–3.5°C",
     "C", "UNEP Emissions Gap Report 2025 projected 2.3–2.5°C warming under full NDC implementation, and up to 2.8°C under current policies (improved from 3.1°C projected in 2024).",
     "AP_HC", "International_Current_Affairs"),

    (28092, "According to UNEP Emissions Gap Report 2025, to align with the 1.5°C pathway, global emissions must fall by what percentage by 2035 (vs 2019 levels)?",
     "25%", "35%", "55%", "75%",
     "C", "UNEP Emissions Gap Report 2025: 55% reduction by 2035 (vs 2019) needed for 1.5°C; 35% reduction needed for the 2°C pathway.",
     "AP_HC", "International_Current_Affairs"),

    # WMO State of Global Climate
    (28093, "The WMO State of the Global Climate 2024 report (released March 2025) confirmed which milestone?",
     "2024 was the second-warmest year on record", "2024 was the first calendar year >1.5°C above pre-industrial levels (1.55°C)", "Global warming temporarily reversed", "Glacier melt slowed for the first time",
     "B", "WMO State of the Global Climate 2024 confirmed 2024 as the warmest year in the 175-year record at 1.55±0.13°C above the 1850-1900 pre-industrial average — the first calendar year to exceed 1.5°C.",
     "AP_HC", "International_Current_Affairs"),

    # FAO SOFI 2025
    (28094, "According to FAO SOFI 2025, how many people faced hunger globally in 2024?",
     "Approximately 512 million", "Approximately 673 million (8.2% of population)", "Approximately 828 million", "Approximately 1.1 billion",
     "B", "SOFI 2025 (FAO, IFAD, UNICEF, WFP, WHO) reported ~673 million people faced hunger in 2024 (8.2% of population), down from 8.5% in 2023. Hunger fell in Asia and LatAm but rose in Africa (>20%) and Western Asia.",
     "AP_HC", "International_Current_Affairs"),

    (28095, "According to FAO SOFI 2025, by 2030 the number of chronically undernourished people is projected at ~512 million, with what share residing in Africa?",
     "About 25%", "About 40%", "About 60%", "About 80%",
     "C", "SOFI 2025 projected 512 million chronically undernourished by 2030, with nearly 60% residing in Africa.",
     "AP_HC", "International_Current_Affairs"),

    # Global MPI 2025
    (28096, "The Global Multidimensional Poverty Index (MPI) 2025 is published jointly by UNDP and which institution?",
     "World Bank", "OPHI (Oxford Poverty and Human Development Initiative)", "FAO", "ILO",
     "B", "The Global MPI 2025 is published jointly by UNDP and OPHI (Oxford Poverty and Human Development Initiative). The 2025 edition was titled 'Overlapping Hardships: Poverty and Climate Hazards'.",
     "AP_HC", "International_Current_Affairs"),

    (28097, "According to Global MPI 2025, the percentage of India's population in multidimensional poverty (per 2019-21 data) was approximately:",
     "8.9%", "16.4%", "24.7%", "35.5%",
     "B", "Global MPI 2025 reported 16.4% of India's population (~235.7 million people in 2023) lived in multidimensional poverty, down from 55.1% in 2005-06. An additional 18.7% are vulnerable to multidimensional poverty.",
     "AP_HC", "International_Current_Affairs"),

    # B-READY 2024
    (28098, "The first edition of the World Bank's Business Ready (B-READY) report was released in:",
     "2022", "2023", "2024", "2026",
     "C", "The first edition of B-READY was released in October 2024 by the World Bank, covering 50 economies (planned to expand to 180 by 2026). It replaces the discontinued Ease of Doing Business report.",
     "AP_HC", "International_Current_Affairs"),

    (28099, "The B-READY report assesses economies across how many pillars?",
     "Three (Regulatory Framework, Public Services, Operational Efficiency)", "Five economic pillars", "Seven governance pillars", "Ten business pillars",
     "A", "B-READY is built on three pillars: (i) Regulatory Framework, (ii) Public Services, and (iii) Operational Efficiency, across 10 topics covering a firm's life cycle.",
     "AP_HC", "International_Current_Affairs"),

    # CCPI 2026 freshness
    (28100, "In the Climate Change Performance Index 2026 (released Nov 2025), India:",
     "Slipped from rank 10 (CCPI 2025) to rank 23, moving from 'high' to 'medium' performers", "Improved from rank 10 to rank 4", "Retained rank 10", "Was excluded from the index",
     "A", "CCPI 2026 (released Nov 2025 at COP30) showed India slipping from rank 10 in CCPI 2025 to rank 23, moving from the 'high performers' group to 'medium performers'.",
     "AP_HC", "International_Current_Affairs"),

    # India SDG Index neighbours
    (28101, "In the UN SDG Index 2025, where India ranked 99th, which neighbour ranked highest in South Asia?",
     "Bangladesh", "Pakistan", "Bhutan", "Nepal",
     "C", "SDG Index 2025 South Asia ranks: Bhutan (74) was highest among India's neighbours, followed by Nepal (85), India (99), Bangladesh (114), and Pakistan (140). China stood at 49.",
     "AP_HC", "International_Current_Affairs"),

    # GII 2025 cluster
    (28102, "Which Indian city ranked highest among Indian innovation clusters in the WIPO GII 2025?",
     "Mumbai (46)", "Delhi (26)", "Bengaluru (21)", "Chennai (84)",
     "C", "GII 2025 listed Bengaluru at rank 21 — the highest among Indian innovation clusters — followed by Delhi (26), Mumbai (46) and Chennai (84). India has 4 clusters in the global top 100.",
     "AP_HC", "International_Current_Affairs"),

    # CCPI top performers concept
    (28103, "Which country ranked 4th (the effective top) in the Climate Change Performance Index 2026?",
     "Denmark", "Sweden", "Morocco", "United Kingdom",
     "A", "CCPI 2026 (released Nov 2025) retained Denmark at rank 4 (the effective top, since positions 1-3 are conventionally left empty). The UK and Morocco followed in the top tier.",
     "AP_HC", "International_Current_Affairs"),

    # WMO 2025 follow-up
    (28104, "WMO has stated that 2025 is likely to be:",
     "The coldest year of the past decade", "Among the warmest two or three years on record", "Below the 1.5°C threshold", "Tied exactly with 2024",
     "B", "WMO confirmed in late 2025 that 2025 is set to be the second or third warmest year on record, continuing the exceptionally high warming trend after 2024 (the first year >1.5°C).",
     "AP_HC", "International_Current_Affairs"),

    # GRFC 2025 — Sudan famine
    (28105, "The Global Report on Food Crises (GRFC) 2025 identified which country as having the world's worst current famine and largest displacement crisis?",
     "Yemen", "Afghanistan", "Sudan", "Ethiopia",
     "C", "GRFC 2025 (GNAFC + FSIN) and UNHCR Global Trends 2024 both identified Sudan as the world's largest displacement and food crisis — with confirmed famine conditions and 14.3 million displaced.",
     "AP_HC", "International_Current_Affairs"),
]


def seed():
    conn = get_conn()
    if USE_POSTGRES:
        cur_chk = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    else:
        cur_chk = conn.cursor()

    # Force-refresh: delete and re-insert with 2025-26 updated data
    # Range widened to 28105 on 2026-05-19 (added 25 new MCQs for fresh 2025 indices)
    if USE_POSTGRES:
        cur_chk.execute("DELETE FROM questions WHERE id >= 28001 AND id <= 28105")
    else:
        cur_chk.execute("DELETE FROM questions WHERE id >= 28001 AND id <= 28105")
    conn.commit()

    ph = '%s' if USE_POSTGRES else '?'
    sql = f"""INSERT {'INTO' if USE_POSTGRES else 'OR IGNORE INTO'} questions
        (id, question_text, option_a, option_b, option_c, option_d,
         correct_answer, explanation, folder, topic)
        VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})
        {'ON CONFLICT DO NOTHING' if USE_POSTGRES else ''}"""

    if USE_POSTGRES:
        cur = conn.cursor()
    else:
        cur = conn.cursor()

    inserted = 0
    for q in QUESTIONS:
        try:
            cur.execute(sql, q)
            inserted += 1
        except Exception as e:
            print(f"[seed_reports_mcq] Skipping ID {q[0]}: {e}")
            try:
                conn.rollback()
            except:
                pass

    conn.commit()
    print(f"[seed_reports_mcq] Inserted {inserted}/{len(QUESTIONS)} questions (IDs 28001–28105).")
    conn.close()


if __name__ == '__main__':
    seed()
