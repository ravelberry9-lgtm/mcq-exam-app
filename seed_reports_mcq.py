"""
Seed: Reports & Indices Current Affairs MCQs
IDs 28001–28080 | Topic: National_Current_Affairs
Run standalone: python seed_reports_mcq.py
Auto-run: called from app.py init_db()
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
     "General_Science", "National_Current_Affairs"),

    (28002, "What was India's rank in the World Press Freedom Index 2025?",
     "131", "143", "151", "162",
     "C", "India ranked 151 out of 180 countries in the World Press Freedom Index 2025 published by RSF.",
     "General_Science", "National_Current_Affairs"),

    (28003, "Which country ranked 1st in the World Press Freedom Index 2025?",
     "Norway", "Sweden", "Finland", "Denmark",
     "C", "Finland topped the World Press Freedom Index 2025. The top three positions were Finland, Estonia, and Netherlands.",
     "General_Science", "National_Current_Affairs"),

    (28004, "What was the USA's rank in the World Press Freedom Index 2025?",
     "45", "57", "63", "72",
     "B", "The United States ranked 57th in the World Press Freedom Index 2025 published by RSF.",
     "General_Science", "National_Current_Affairs"),

    (28005, "RSF, which publishes the Press Freedom Index, is headquartered in which city?",
     "Geneva", "New York", "Brussels", "Paris",
     "D", "RSF (Reporters Without Borders / Reporters Sans Frontières) is headquartered in Paris, France.",
     "General_Science", "National_Current_Affairs"),

    # ── Food Security ──
    (28006, "The Global Report on Food Crises (GRFC) 2025 was published by which body?",
     "FAO alone", "WFP alone", "GNAFC and FSIN", "UNICEF and WHO",
     "C", "The GRFC 2025 was published jointly by GNAFC (Global Network Against Food Crises) and FSIN (Food Security Information Network).",
     "General_Science", "National_Current_Affairs"),

    (28007, "According to the Global Report on Food Crises 2025, how many people faced acute hunger?",
     "225 million in 45 countries", "261 million in 50 countries", "295 million in 53 countries", "318 million in 58 countries",
     "C", "GRFC 2025 reported that approximately 295 million people in 53 countries/territories faced acute food insecurity.",
     "General_Science", "National_Current_Affairs"),

    (28008, "The Global Hunger Index (GHI) is published by which organisations?",
     "FAO and WFP", "Concern Worldwide and Welthungerhilfe", "UNDP and UNICEF", "World Bank and IMF",
     "B", "The Global Hunger Index is published jointly by Concern Worldwide (Ireland) and Welthungerhilfe (Germany).",
     "General_Science", "National_Current_Affairs"),

    (28009, "India ranked 105 in the Global Hunger Index 2024, placing it in which category?",
     "Moderate", "Serious", "Alarming", "Extremely Alarming",
     "B", "India ranked 105 out of 127 countries in the Global Hunger Index 2024, placing it in the 'Serious' category.",
     "General_Science", "National_Current_Affairs"),

    (28010, "The State of Food Security and Nutrition in the World (SOFI) report is jointly published by which five UN bodies?",
     "UN DESA, UNDP, UNICEF, WHO, WFP", "FAO, IFAD, UNICEF, WFP, WHO", "UNESCO, ILO, FAO, WFP, UNHCR", "FAO, WHO, UNCTAD, ILO, UNFPA",
     "B", "The SOFI report is jointly published by FAO, IFAD, UNICEF, WFP, and WHO.",
     "General_Science", "National_Current_Affairs"),

    # ── Climate Change Performance Index ──
    (28011, "Which organisation publishes the Climate Change Performance Index (CCPI)?",
     "UNEP alone", "Germanwatch, NewClimate Institute and CAN International", "World Bank and IEA", "IPCC",
     "B", "The CCPI is published by Germanwatch, NewClimate Institute, and Climate Action Network (CAN) International.",
     "General_Science", "National_Current_Affairs"),

    (28012, "India's rank in the Climate Change Performance Index (CCPI) 2025 was:",
     "4th", "7th", "10th", "15th",
     "C", "India ranked 10th in the CCPI 2025, making it one of the better-performing major economies.",
     "General_Science", "National_Current_Affairs"),

    (28013, "Why are the top 3 positions in the CCPI always left empty?",
     "Data for top countries is classified", "No country performs sufficiently in all four categories", "Countries at top refused data sharing", "Methodological revision is ongoing",
     "B", "The CCPI tradition is that positions 1–3 are intentionally vacant because no country performs sufficiently in all four assessment categories: GHG emissions, energy use, renewable energy, and climate policy.",
     "General_Science", "National_Current_Affairs"),

    (28014, "Which country ranked 4th in the Climate Change Performance Index 2025?",
     "Norway", "Germany", "Denmark", "Sweden",
     "C", "Denmark ranked 4th in the CCPI 2025 — effectively the highest real rank since positions 1–3 are kept empty.",
     "General_Science", "National_Current_Affairs"),

    (28015, "India's score in the CCPI 2025 for Renewable Energy was categorised as:",
     "Very High", "High", "Medium", "Low",
     "D", "In CCPI 2025, India's renewable energy score was rated 'Low', while GHG emissions and energy use were rated 'High' and climate policy 'Medium'.",
     "General_Science", "National_Current_Affairs"),

    # ── Energy & Carbon Reports ──
    (28016, "Which body published the World Energy Investment Report 2025?",
     "IRENA", "IEA", "World Bank", "UNCTAD",
     "B", "The World Energy Investment Report 2025 was published by the IEA (International Energy Agency), headquartered in Paris.",
     "General_Science", "National_Current_Affairs"),

    (28017, "According to World Energy Investment Report 2025, total global energy investment reached:",
     "$2.1 trillion", "$2.7 trillion", "$3.3 trillion", "$4.0 trillion",
     "C", "Global energy investment reached $3.3 trillion in 2025 according to the IEA report.",
     "General_Science", "National_Current_Affairs"),

    (28018, "In the World Energy Investment Report 2025, clean energy investment was approximately:",
     "$1.1 trillion", "$1.6 trillion", "$2.2 trillion", "$2.8 trillion",
     "C", "Clean energy investment stood at $2.2 trillion — exactly double the fossil fuel investment of $1.1 trillion.",
     "General_Science", "National_Current_Affairs"),

    (28019, "Which country led global clean energy investment according to the IEA World Energy Investment Report 2025?",
     "USA", "Germany", "India", "China",
     "D", "China led global clean energy investment, accounting for a significant share of the $2.2 trillion in clean energy spending.",
     "General_Science", "National_Current_Affairs"),

    (28020, "The IEA (International Energy Agency) is headquartered in which city?",
     "Vienna", "Brussels", "Paris", "Geneva",
     "C", "The International Energy Agency (IEA) is headquartered in Paris, France.",
     "General_Science", "National_Current_Affairs"),

    (28021, "The 'State and Trends of Carbon Pricing 2025' report was published by which organisation?",
     "UNEP", "IEA", "World Bank", "IPCC",
     "C", "The State and Trends of Carbon Pricing 2025 was published by the World Bank.",
     "General_Science", "National_Current_Affairs"),

    (28022, "According to the Carbon Pricing Report 2025, how many active carbon pricing instruments exist globally?",
     "40", "60", "80", "100",
     "C", "There are 80 active carbon pricing instruments globally (up from just 5 in 2005), according to World Bank's Carbon Pricing report 2025.",
     "General_Science", "National_Current_Affairs"),

    (28023, "The carbon pricing mechanisms cover what percentage of global GHG emissions as per the 2025 World Bank report?",
     "15%", "21%", "28%", "35%",
     "C", "Active carbon pricing mechanisms cover 28% of global greenhouse gas emissions according to the World Bank report 2025.",
     "General_Science", "National_Current_Affairs"),

    (28024, "IRENA, which publishes Renewable Energy Statistics, is headquartered in:",
     "Geneva, Switzerland", "Paris, France", "Abu Dhabi, UAE", "Vienna, Austria",
     "C", "IRENA (International Renewable Energy Agency) is headquartered in Abu Dhabi, UAE.",
     "General_Science", "National_Current_Affairs"),

    # ── Social Security & Population ──
    (28025, "According to ILO data, India ranked _____ globally for the number of people covered under social security.",
     "1st", "2nd", "3rd", "5th",
     "B", "India ranked 2nd globally (ILO ILOSTAT) for the absolute number of people covered under social security — approximately 940 million people.",
     "General_Science", "National_Current_Affairs"),

    (28026, "India's social security coverage grew from 19% (2015) to what percentage by 2025?",
     "45.6%", "54.2%", "64.3%", "72.1%",
     "C", "India's social security coverage grew from 19% in 2015 to 64.3% in 2025 — the fastest expansion in the world.",
     "General_Science", "National_Current_Affairs"),

    (28027, "UNFPA's State of World Population (SOWP) 2025 report was themed:",
     "The Ageing World", "Population Without Borders", "The Real Fertility Crisis", "7 Billion and Beyond",
     "C", "UNFPA's SOWP 2025 was themed 'The Real Fertility Crisis', highlighting that both very high and very low fertility pose challenges.",
     "General_Science", "National_Current_Affairs"),

    (28028, "UNFPA stands for:",
     "UN Food and Population Agency", "UN Fund for Population Activities", "United Nations Population Fund", "Universal Family Planning Agency",
     "C", "UNFPA stands for United Nations Population Fund (formerly United Nations Fund for Population Activities).",
     "General_Science", "National_Current_Affairs"),

    (28029, "According to UNHCR Global Trends 2024, how many people were forcibly displaced worldwide?",
     "97.3 million", "110.8 million", "123.2 million", "135.6 million",
     "C", "UNHCR's Global Trends 2024 reported a record 123.2 million forcibly displaced people worldwide.",
     "General_Science", "National_Current_Affairs"),

    (28030, "What percentage of forcibly displaced persons globally were children, as per UNHCR 2024?",
     "25%", "33%", "40%", "48%",
     "C", "According to UNHCR Global Trends 2024, children constituted approximately 40% of all forcibly displaced persons.",
     "General_Science", "National_Current_Affairs"),

    (28031, "How many people were Internally Displaced Persons (IDPs) according to UNHCR 2024?",
     "61.5 million", "68.2 million", "73.5 million", "80.1 million",
     "C", "73.5 million people were internally displaced within their own countries according to UNHCR's Global Trends 2024.",
     "General_Science", "National_Current_Affairs"),

    (28032, "Which country was the top source of forcibly displaced people according to UNHCR 2024?",
     "Syria", "Afghanistan", "Sudan", "Ukraine",
     "C", "Sudan became the top source of forcibly displaced people globally in 2024, surpassing previous leaders Syria and Afghanistan.",
     "General_Science", "National_Current_Affairs"),

    (28033, "The Global Education Monitoring (GEM) Report is published by which organisation?",
     "UNICEF", "UNESCO", "World Bank", "UNDP",
     "B", "The GEM Report is published by UNESCO (UN Educational, Scientific and Cultural Organization), headquartered in Paris.",
     "General_Science", "National_Current_Affairs"),

    (28034, "According to the UNESCO GEM Report, how many children are out of school globally?",
     "198 million", "235 million", "272 million", "308 million",
     "C", "The UNESCO Global Education Monitoring Report states that approximately 272 million children are currently out of school worldwide.",
     "General_Science", "National_Current_Affairs"),

    # ── Economic Reports ──
    (28035, "The UN World Economic Situation and Prospects (WESP) 2025 was published by:",
     "UN DESA", "IMF", "World Bank", "UNCTAD",
     "A", "WESP 2025 is published by UN DESA (Department of Economic and Social Affairs).",
     "General_Science", "National_Current_Affairs"),

    (28036, "What global GDP growth rate did WESP 2025 project for 2025?",
     "1.8%", "2.4%", "3.1%", "3.8%",
     "B", "WESP 2025 projected global GDP growth of 2.4% for 2025.",
     "General_Science", "National_Current_Affairs"),

    (28037, "India's GDP growth rate projected in UN WESP 2025 was:",
     "5.1%", "5.9%", "6.3%", "7.2%",
     "C", "India's GDP growth was projected at 6.3% in WESP 2025, making it the fastest-growing major economy.",
     "General_Science", "National_Current_Affairs"),

    (28038, "UNCTAD's 'World of Debt' report revealed global public debt reached:",
     "$78 trillion", "$92 trillion", "$102 trillion", "$115 trillion",
     "C", "UNCTAD's World of Debt report revealed global public debt reached a record $102 trillion.",
     "General_Science", "National_Current_Affairs"),

    (28039, "UNCTAD is headquartered in:",
     "New York, USA", "Geneva, Switzerland", "Vienna, Austria", "Paris, France",
     "B", "UNCTAD (United Nations Conference on Trade and Development) is headquartered in Geneva, Switzerland.",
     "General_Science", "National_Current_Affairs"),

    (28040, "Which report replaced the World Bank's discontinued Ease of Doing Business report?",
     "Global Business Index", "Business Friendly Report", "Business Ready (B-READY)", "World Competitiveness Yearbook",
     "C", "The World Bank replaced the Ease of Doing Business report (discontinued in 2021 due to data irregularities) with the Business Ready (B-READY) report, first edition released in 2024.",
     "General_Science", "National_Current_Affairs"),

    # ── Fisheries ──
    (28041, "Which organisation published the 'Review of the State of World Marine Fishery Resources 2025'?",
     "UNEP", "UNDP", "FAO", "WWF",
     "C", "The Review of the State of World Marine Fishery Resources is published by FAO (Food and Agriculture Organization), headquartered in Rome.",
     "General_Science", "National_Current_Affairs"),

    (28042, "According to FAO's marine fisheries report 2025, what percentage of fish stocks are being fished at biologically sustainable levels?",
     "55.2%", "60.1%", "64.5%", "71.3%",
     "C", "64.5% of fish stocks were being fished within biologically sustainable levels according to FAO's marine fisheries report 2025.",
     "General_Science", "National_Current_Affairs"),

    (28043, "What percentage of global marine fish stocks are overfished according to FAO 2025?",
     "18.5%", "28.3%", "35.5%", "42.1%",
     "C", "35.5% of global marine fish stocks are overfished according to FAO's 2025 marine fisheries review.",
     "General_Science", "National_Current_Affairs"),

    (28044, "FAO's biennial fisheries publication covering both marine and aquaculture is known as:",
     "SOFIA", "GRFC", "SOFI", "SIFA",
     "A", "SOFIA (The State of World Fisheries and Aquaculture) is FAO's biennial publication covering global fisheries and aquaculture.",
     "General_Science", "National_Current_Affairs"),

    # ── Military & Nuclear ──
    (28045, "SIPRI is headquartered in which city?",
     "Stockholm (Solna), Sweden", "Oslo, Norway", "Copenhagen, Denmark", "Helsinki, Finland",
     "A", "SIPRI (Stockholm International Peace Research Institute) is headquartered in Solna, near Stockholm, Sweden.",
     "General_Science", "National_Current_Affairs"),

    (28046, "According to SIPRI Yearbook 2025, Russia possesses how many nuclear warheads?",
     "4,612", "5,177", "5,459", "6,213",
     "C", "Russia has 5,459 nuclear warheads according to the SIPRI Yearbook 2025.",
     "General_Science", "National_Current_Affairs"),

    (28047, "How many nuclear warheads does the USA possess according to SIPRI 2025?",
     "4,823", "5,177", "5,459", "5,800",
     "B", "The USA possesses 5,177 nuclear warheads according to SIPRI Yearbook 2025.",
     "General_Science", "National_Current_Affairs"),

    (28048, "Global military expenditure reached what record level in 2024 according to SIPRI?",
     "$1.8 trillion", "$2.1 trillion", "$2.4 trillion", "$2.8 trillion",
     "C", "Global military expenditure reached a record ~$2.4 trillion in 2024 according to SIPRI.",
     "General_Science", "National_Current_Affairs"),

    (28049, "The Global Peace Index is published by which organisation?",
     "SIPRI", "IEP (Institute for Economics and Peace)", "UNDP", "UN Security Council",
     "B", "The Global Peace Index is published by IEP (Institute for Economics and Peace), headquartered in Sydney, Australia.",
     "General_Science", "National_Current_Affairs"),

    (28050, "Which country consistently tops the Global Peace Index?",
     "Switzerland", "Denmark", "Iceland", "New Zealand",
     "C", "Iceland consistently tops the Global Peace Index as the world's most peaceful country.",
     "General_Science", "National_Current_Affairs"),

    # ── SDG & Governance ──
    (28051, "India's rank in the India SDG Index 2025 (global) was:",
     "105th", "99th", "112th", "87th",
     "B", "India ranked 99th in the SDG Index 2025 — the first time India entered the top 100.",
     "General_Science", "National_Current_Affairs"),

    (28052, "Who publishes the India SDG Index?",
     "Ministry of Statistics", "NITI Aayog", "Planning Commission", "UNDP India",
     "B", "The India SDG Index is published by NITI Aayog (National Institution for Transforming India).",
     "General_Science", "National_Current_Affairs"),

    (28053, "India's SDG overall score improved from 57 in 2018 to what in 2025?",
     "62", "66", "71", "78",
     "C", "India's SDG overall score improved from 57 in 2018 to 71 in 2025 according to NITI Aayog's India SDG Index.",
     "General_Science", "National_Current_Affairs"),

    (28054, "The Performance Grading Index (PGI) 2.0 for school education is published by:",
     "NITI Aayog", "Ministry of Education", "University Grants Commission", "NCERT",
     "B", "The PGI 2.0 for school education is published by the Ministry of Education, Government of India.",
     "General_Science", "National_Current_Affairs"),

    (28055, "Which state/UT topped the Performance Grading Index (PGI) 2.0?",
     "Delhi", "Kerala", "Chandigarh", "Tamil Nadu",
     "C", "Chandigarh (UT) topped the Performance Grading Index (PGI) 2.0.",
     "General_Science", "National_Current_Affairs"),

    (28056, "Which state was at the bottom of the Performance Grading Index (PGI) 2.0?",
     "Bihar", "Meghalaya", "Jharkhand", "Nagaland",
     "B", "Meghalaya was at the bottom of the Performance Grading Index (PGI) 2.0.",
     "General_Science", "National_Current_Affairs"),

    (28057, "The PGI 2.0 uses how many indicators across 6 domains?",
     "55 indicators, 800 points", "73 indicators, 1000 points", "80 indicators, 900 points", "65 indicators, 750 points",
     "B", "PGI 2.0 uses 73 indicators spread across 6 domains for a total score of 1000 points.",
     "General_Science", "National_Current_Affairs"),

    (28058, "The Corruption Perceptions Index (CPI) is published by:",
     "World Bank", "Transparency International", "UNDP", "WEF",
     "B", "The Corruption Perceptions Index is published by Transparency International, headquartered in Berlin, Germany.",
     "General_Science", "National_Current_Affairs"),

    (28059, "India's rank in the Corruption Perceptions Index 2024 was:",
     "73", "85", "93", "107",
     "C", "India ranked 93 out of 180 countries in the Corruption Perceptions Index 2024.",
     "General_Science", "National_Current_Affairs"),

    (28060, "Which country topped the Corruption Perceptions Index 2024 (least corrupt)?",
     "Finland", "Norway", "Denmark", "Singapore",
     "C", "Denmark topped the CPI 2024 as the least corrupt country. The scale goes from 0 (highly corrupt) to 100 (very clean).",
     "General_Science", "National_Current_Affairs"),

    # ── Innovation & Competitiveness ──
    (28061, "The Global Innovation Index (GII) is published by:",
     "WEF", "UNDP", "WIPO", "World Bank",
     "C", "The Global Innovation Index is published by WIPO (World Intellectual Property Organization), headquartered in Geneva.",
     "General_Science", "National_Current_Affairs"),

    (28062, "India's rank in the Global Innovation Index 2024 was:",
     "29th", "39th", "49th", "55th",
     "B", "India ranked 39th in the Global Innovation Index 2024, a dramatic improvement from 81st in 2015.",
     "General_Science", "National_Current_Affairs"),

    (28063, "Which country topped the Global Innovation Index 2024?",
     "USA", "Germany", "Sweden", "Switzerland",
     "D", "Switzerland topped the Global Innovation Index 2024.",
     "General_Science", "National_Current_Affairs"),

    (28064, "The Global Competitiveness Report is published by which organisation?",
     "World Bank", "IMF", "World Economic Forum (WEF)", "OECD",
     "C", "The Global Competitiveness Report is published by the World Economic Forum (WEF), headquartered in Cologny near Geneva, Switzerland.",
     "General_Science", "National_Current_Affairs"),

    # ── HDI & Gender ──
    (28065, "The Human Development Index (HDI) is published by:",
     "World Bank", "UNDP", "UNFPA", "UN DESA",
     "B", "The Human Development Index is published by UNDP (United Nations Development Programme).",
     "General_Science", "National_Current_Affairs"),

    (28066, "India's rank in the Human Development Index (HDI) 2025 report was:",
     "112", "125", "134", "142",
     "C", "India ranked 134 out of 193 countries in the HDI 2025 report, classified as 'Medium Human Development'.",
     "General_Science", "National_Current_Affairs"),

    (28067, "The HDI measures three dimensions of human development. Which of the following is NOT one of them?",
     "Life expectancy", "Education (years of schooling)", "Per-capita income (GNI)", "Environmental sustainability",
     "D", "HDI measures Life Expectancy, Education (mean + expected years of schooling), and GNI per capita. Environmental sustainability is NOT a direct HDI measure.",
     "General_Science", "National_Current_Affairs"),

    (28068, "The Gender Gap Report is published by:",
     "UNDP", "UN Women", "World Economic Forum (WEF)", "ILO",
     "C", "The Gender Gap Report is published by the World Economic Forum (WEF).",
     "General_Science", "National_Current_Affairs"),

    (28069, "India's rank in the Gender Gap Report 2024 was:",
     "114th", "122nd", "129th", "138th",
     "C", "India ranked 129 out of 146 countries in the Global Gender Gap Report 2024 published by WEF.",
     "General_Science", "National_Current_Affairs"),

    (28070, "Which country consistently tops the Global Gender Gap Report?",
     "Norway", "Sweden", "Finland", "Iceland",
     "D", "Iceland consistently tops the Global Gender Gap Report. It has led the index for over a decade.",
     "General_Science", "National_Current_Affairs"),

    # ── Happiness & Logistics ──
    (28071, "The World Happiness Report is published by:",
     "UNDP", "UN Sustainable Development Solutions Network (UNSDSN)", "WHO", "WEF",
     "B", "The World Happiness Report is published by the UN Sustainable Development Solutions Network (UNSDSN).",
     "General_Science", "National_Current_Affairs"),

    (28072, "Which country topped the World Happiness Report 2025 for the 8th consecutive year?",
     "Norway", "Iceland", "Denmark", "Finland",
     "D", "Finland topped the World Happiness Report 2025 for the 8th consecutive year.",
     "General_Science", "National_Current_Affairs"),

    (28073, "The Logistics Performance Index (LPI) is published by which organisation?",
     "IMF", "UNCTAD", "World Bank", "ILO",
     "C", "The Logistics Performance Index is published by the World Bank.",
     "General_Science", "National_Current_Affairs"),

    (28074, "India's rank in the Logistics Performance Index 2023 was:",
     "30th", "38th", "44th", "52nd",
     "B", "India ranked 38th in the Logistics Performance Index 2023, improving from 44th in 2018.",
     "General_Science", "National_Current_Affairs"),

    # ── Health ──
    (28075, "The Global TB Report is published by which organisation?",
     "UNICEF", "WHO", "Ministry of Health India", "UNDP",
     "B", "The Global TB Report is published annually by WHO (World Health Organization).",
     "General_Science", "National_Current_Affairs"),

    (28076, "India accounts for approximately what percentage of global tuberculosis cases?",
     "16%", "20%", "26%", "32%",
     "C", "India accounts for approximately 26% of global TB cases, making it the country with the highest TB burden.",
     "General_Science", "National_Current_Affairs"),

    (28077, "India's target to eliminate tuberculosis is by which year (5 years ahead of global SDG target)?",
     "2023", "2025", "2027", "2030",
     "B", "India aims to eliminate TB by 2025, which is 5 years ahead of the global SDG target of 2030.",
     "General_Science", "National_Current_Affairs"),

    (28078, "According to NFHS-5 (2019–21), India's Total Fertility Rate (TFR) stood at:",
     "1.8", "2.0", "2.3", "2.5",
     "B", "India's TFR was 2.0 in NFHS-5 (2019–21), falling below the replacement level of 2.1 for the first time.",
     "General_Science", "National_Current_Affairs"),

    # ── Mixed / Publisher Identification ──
    (28079, "Which of the following reports is published by the IMF?",
     "World Energy Investment Report", "World Economic Outlook", "State and Trends of Carbon Pricing", "Global Report on Food Crises",
     "B", "The World Economic Outlook (WEO) is published by the IMF (International Monetary Fund). IEA publishes WEI Report; World Bank publishes Carbon Pricing; GNAFC+FSIN publish GRFC.",
     "General_Science", "National_Current_Affairs"),

    (28080, "The Democracy Index which classifies countries into Full Democracy, Flawed Democracy, Hybrid Regime, and Authoritarian is published by:",
     "Freedom House", "Transparency International", "Economist Intelligence Unit (EIU)", "IEP",
     "C", "The Democracy Index is published by the EIU (Economist Intelligence Unit), the research arm of The Economist group.",
     "General_Science", "National_Current_Affairs"),
]


def seed():
    conn = get_conn()
    if USE_POSTGRES:
        cur_chk = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    else:
        cur_chk = conn.cursor()

    # Force-refresh: delete and re-insert with 2025 updated data
    if USE_POSTGRES:
        cur_chk.execute("DELETE FROM questions WHERE id >= 28001 AND id <= 28080")
    else:
        cur_chk.execute("DELETE FROM questions WHERE id >= 28001 AND id <= 28080")
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
    print(f"[seed_reports_mcq] Inserted {inserted}/{len(QUESTIONS)} questions (IDs 28001–28080).")
    conn.close()


if __name__ == '__main__':
    seed()
