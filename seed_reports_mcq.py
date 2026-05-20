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
     "C", "The World Press Freedom Index is published annually by RSF (Reporters Sans Frontières / Reporters Without Borders), headquartered in Paris, France. This index is critical for monitoring global media freedom and democratic governance, particularly relevant as India's independent media faces increasing pressures from digital regulation and political polarization. The index informs international development funding, trade partnerships, and diplomatic relations with countries that violate press freedoms.",
     "AP_HC", "International_Current_Affairs"),

    (28002, "What was India's rank in the World Press Freedom Index 2025?",
     "131", "143", "151", "162",
     "C", "India ranked 151 out of 180 countries in the World Press Freedom Index 2025 published by RSF. This decline reflects growing concerns about press restrictions, particularly regarding reporting on government policies, elections, and sensitive political matters. India's low ranking impacts international perceptions of democratic governance and influences investment climate assessments and diplomatic relations, especially with Western democracies that prioritize media freedom.",
     "AP_HC", "International_Current_Affairs"),

    (28003, "Which country ranked 1st in the World Press Freedom Index 2025?",
     "Norway", "Sweden", "Finland", "Denmark",
     "C", "Finland topped the World Press Freedom Index 2025, with Estonia and Netherlands in the top three. Nordic and Northern European countries consistently rank highest due to strong institutional protections for journalists, transparent governance, and rule of law. This benchmark is significant for emerging democracies like India, which aspires to strengthened press freedoms as part of its democratic consolidation strategy outlined in various human rights and governance reports.",
     "AP_HC", "International_Current_Affairs"),

    (28004, "What was the USA's rank in the World Press Freedom Index 2025?",
     "45", "57", "63", "72",
     "B", "The United States ranked 57th in the World Press Freedom Index 2025 published by RSF. The USA's moderate ranking reflects documented concerns about media polarization, ownership concentration, and threats to journalists' security during election cycles. Comparative analysis shows that even established democracies face press freedom challenges, providing context for India's performance and demonstrating that press freedom requires continuous institutional strengthening regardless of development stage.",
     "AP_HC", "International_Current_Affairs"),

    (28005, "RSF, which publishes the Press Freedom Index, is headquartered in which city?",
     "Geneva", "New York", "Brussels", "Paris",
     "D", "RSF (Reporters Without Borders / Reporters Sans Frontières) is headquartered in Paris, France. As a Paris-based NGO, RSF operates within the European governance framework and draws on European democratic principles, which may influence its assessment methodology and benchmarks. This institutional positioning is important to understand RSF's criteria for evaluating countries like India, where the organization maintains field offices and conducts regular monitoring of journalist safety and media independence.",
     "AP_HC", "International_Current_Affairs"),

    # ── Food Security ──
    (28006, "The Global Report on Food Crises (GRFC) 2025 was published by which body?",
     "FAO alone", "WFP alone", "GNAFC and FSIN", "UNICEF and WHO",
     "C", "The GRFC 2025 was published jointly by GNAFC (Global Network Against Food Crises) and FSIN (Food Security Information Network). This multi-agency collaboration reflects the complexity of global food security, which depends on conflict resolution, climate adaptation, and economic resilience. India's strategic interest in these reports stems from its dual challenge: feeding 1.4+ billion people while transitioning from food importer to net food exporter, making supply chain stability and agricultural productivity critical to national security.",
     "AP_HC", "International_Current_Affairs"),

    (28007, "According to the Global Report on Food Crises 2025, how many people faced acute hunger?",
     "225 million in 45 countries", "261 million in 50 countries", "295 million in 53 countries", "318 million in 58 countries",
     "C", "GRFC 2025 reported that approximately 295 million people in 53 countries/territories faced acute food insecurity. This figure represents a persistent crisis concentrated in Sub-Saharan Africa, the Sahel, and the Middle East—regions experiencing conflict, climate shocks, and economic decline. India's policy makers track this data to justify investments in the Public Distribution System, rural employment schemes, and climate adaptation, recognizing that India's food security depends on both domestic production and stable international supply chains.",
     "AP_HC", "International_Current_Affairs"),

    (28008, "The Global Hunger Index (GHI) is published by which organisations?",
     "FAO and WFP", "Concern Worldwide and Welthungerhilfe", "UNDP and UNICEF", "World Bank and IMF",
     "B", "The Global Hunger Index is published jointly by Concern Worldwide (Ireland) and Welthungerhilfe (Germany). These NGOs partner to measure hunger using multidimensional indicators including malnutrition rates, food availability, and child mortality. India's consistent underperformance on GHI metrics—despite economic growth—indicates that inclusive growth and anti-hunger programs require greater coordination between food grain management, health delivery, and targeted nutrition interventions for vulnerable populations.",
     "AP_HC", "International_Current_Affairs"),

    (28009, "India's rank in the Global Hunger Index 2025 was 102/123, with a score of 25.8, placing India in which category?",
     "Moderate", "Serious", "Alarming", "Extremely Alarming",
     "B", "India ranked 102 out of 123 countries in the Global Hunger Index 2025 with a score of 25.8, placing it in the 'Serious' category (Released October 2025 by Concern Worldwide + Welthungerhilfe). This ranking reflects persistent child malnutrition despite India's agricultural self-sufficiency—a paradox highlighting distribution failures and inadequate health-nutrition linkages. India's serious category rating, shared with Bangladesh and Pakistan, underscores the need for accelerated public health investment and expanded nutrition programs including mid-day meal schemes, POSHAN Abhiyaan, and targeted supplementation.",
     "AP_HC", "International_Current_Affairs"),

    (28010, "The State of Food Security and Nutrition in the World (SOFI) report is jointly published by which five UN bodies?",
     "UN DESA, UNDP, UNICEF, WHO, WFP", "FAO, IFAD, UNICEF, WFP, WHO", "UNESCO, ILO, FAO, WFP, UNHCR", "FAO, WHO, UNCTAD, ILO, UNFPA",
     "B", "The SOFI report is jointly published by FAO, IFAD, UNICEF, WFP, and WHO. This comprehensive inter-agency partnership bridges agricultural production (FAO), rural development (IFAD), child nutrition (UNICEF), food assistance (WFP), and health outcomes (WHO), reflecting the interconnected nature of food security. India uses SOFI data to align its National Nutrition Mission with global best practices and to track progress toward SDG 2 (Zero Hunger), particularly focusing on reducing wasting in children and improving diet diversity in rural populations.",
     "AP_HC", "International_Current_Affairs"),

    # ── Climate Change Performance Index ──
    (28011, "Which organisation publishes the Climate Change Performance Index (CCPI)?",
     "UNEP alone", "Germanwatch, NewClimate Institute and CAN International", "World Bank and IEA", "IPCC",
     "B", "The CCPI is published by Germanwatch, NewClimate Institute, and Climate Action Network (CAN) International. This independent NGO partnership—not affiliated with governments or fossil fuel interests—provides transparent climate action assessment. India values CCPI as an alternative to government-dominated climate metrics, using it to identify sectoral gaps in renewable energy deployment, emissions reduction, and climate policy implementation, while advocating for equity principles in climate accountability frameworks.",
     "AP_HC", "International_Current_Affairs"),

    (28012, "India's rank in the Climate Change Performance Index (CCPI) 2025 was:",
     "4th", "7th", "10th", "15th",
     "C", "India ranked 10th in the CCPI 2025, making it one of the better-performing major economies. This strong performance reflects India's commitment to renewable energy expansion (512 GW capacity), commitment to phase out coal (with targets aligned to 2030/2050 timelines), and adoption of the National Action Plan on Climate Change. India's top-10 ranking strengthens its negotiating position at international climate forums and supports its claim that developing economies are delivering climate action despite historical responsibility differences with developed nations.",
     "AP_HC", "International_Current_Affairs"),

    (28013, "Why are the top 3 positions in the CCPI always left empty?",
     "Data for top countries is classified", "No country performs sufficiently in all four categories", "Countries at top refused data sharing", "Methodological revision is ongoing",
     "B", "The CCPI tradition is that positions 1–3 are intentionally vacant because no country performs sufficiently in all four assessment categories: GHG emissions, energy use, renewable energy, and climate policy. This methodology reflects the rigorous, multidimensional nature of climate action assessment and sends a signal that perfection is not yet achievable at the global level. For India, this framework emphasizes that leadership requires balanced progress across multiple sectors simultaneously—not just renewable energy deployment, but also declining fossil fuel use, policy implementation, and emissions reductions in transport and industry.",
     "AP_HC", "International_Current_Affairs"),

    (28014, "Which country ranked 4th in the Climate Change Performance Index 2025?",
     "Norway", "Germany", "Denmark", "Sweden",
     "C", "Denmark ranked 4th in the CCPI 2025 — effectively the highest real rank since positions 1–3 are kept empty. Denmark's leadership stems from aggressive wind energy deployment (providing 80%+ of electricity), carbon pricing mechanisms, and sustained policy commitment despite economic pressures. India's climate strategists study Denmark's model for scaling renewable grid integration, understanding that India's path to decarbonization must balance energy access for 1.4 billion people with emissions reductions—a challenge more complex than European transitions.",
     "AP_HC", "International_Current_Affairs"),

    (28015, "India's score in the CCPI 2025 for Renewable Energy was categorised as:",
     "Very High", "High", "Medium", "Low",
     "D", "In CCPI 2025, India's renewable energy score was rated 'Low', while GHG emissions and energy use were rated 'High' and climate policy 'Medium'. This uneven profile reveals India's climate paradox: despite massive renewable capacity additions (512 GW by 2025), the grid remains coal-dependent for baseload power, slowing the pace of fossil fuel phase-out. Addressing this gap requires accelerated battery storage deployment, grid modernization, and demand-side management—investments critical to India's 2030 carbon intensity reduction target of 45% versus 2005 levels.",
     "AP_HC", "International_Current_Affairs"),

    # ── Energy & Carbon Reports ──
    (28016, "Which body published the World Energy Investment Report 2025?",
     "IRENA", "IEA", "World Bank", "UNCTAD",
     "B", "The World Energy Investment Report 2025 was published by the IEA (International Energy Agency), headquartered in Paris. The IEA, comprising 31 advanced-economy members, provides authoritative energy outlook data that shapes investment decisions by international financial institutions, sovereign wealth funds, and development banks. India, as a major energy consumer and emerging investor in clean energy, uses IEA's investment data and forecasts to calibrate domestic energy policy, attract foreign capital to renewable projects, and benchmark India's clean energy investment against global standards.",
     "AP_HC", "International_Current_Affairs"),

    (28017, "According to World Energy Investment Report 2025, total global energy investment reached:",
     "$2.1 trillion", "$2.7 trillion", "$3.3 trillion", "$4.0 trillion",
     "C", "Global energy investment reached $3.3 trillion in 2025 according to the IEA report. This record investment reflects the economic imperative of energy transition driven by climate commitments, energy security concerns post-Ukraine conflict, and accelerating renewable technology costs. India's share of this investment—approximately 7-8% of global energy capex—positions it as a major recipient of clean energy funding; however, India's energy investment intensity remains below requirements to meet its 2030-2050 decarbonization commitments and electrification goals.",
     "AP_HC", "International_Current_Affairs"),

    (28018, "In the World Energy Investment Report 2025, clean energy investment was approximately:",
     "$1.1 trillion", "$1.6 trillion", "$2.2 trillion", "$2.8 trillion",
     "C", "Clean energy investment stood at $2.2 trillion — exactly double the fossil fuel investment of $1.1 trillion. This inflection point signals an irreversible energy transition, with market forces now favoring clean energy over carbon-intensive alternatives. India's clean energy investment has accelerated from $13 billion (2015) to $30+ billion annually (2024), driven by government auctions, private equity, and international climate finance; however, India must sustain this momentum to reach the $200 billion annual investment needed by 2030 for its NDC commitments.",
     "AP_HC", "International_Current_Affairs"),

    (28019, "Which country led global clean energy investment according to the IEA World Energy Investment Report 2025?",
     "USA", "Germany", "India", "China",
     "D", "China led global clean energy investment, accounting for a significant share of the $2.2 trillion in clean energy spending. China's dominance—accounting for ~30% of global clean energy capex—reflects both its massive domestic energy demand and strategic position as a global manufacturer of solar, wind, and battery technologies. India, ranking 3rd-4th globally, views China's investment as a competitive benchmark; India's strategy combines domestic investment acceleration with technology partnerships to reduce import dependency and capture downstream manufacturing value in renewable equipment.",
     "AP_HC", "International_Current_Affairs"),

    (28020, "The IEA (International Energy Agency) is headquartered in which city?",
     "Vienna", "Brussels", "Paris", "Geneva",
     "C", "The International Energy Agency (IEA) is headquartered in Paris, France. As an OECD organization, the IEA has traditionally focused on advanced economy energy policy but has expanded capacity to monitor emerging market energy transitions including India's. The IEA's energy efficiency and carbon accounting frameworks increasingly influence Indian policy makers' understanding of energy intensity reduction, helping India track progress toward its Energy Intensity Reduction Target of 33% by 2030 (from 2005 baseline).",
     "AP_HC", "International_Current_Affairs"),

    (28021, "The 'State and Trends of Carbon Pricing 2025' report was published by which organisation?",
     "UNEP", "IEA", "World Bank", "IPCC",
     "C", "The State and Trends of Carbon Pricing 2025 was published by the World Bank. This report tracks the expansion of carbon pricing instruments (ETS, carbon taxes) globally as a policy mechanism for emissions reduction. India's policy discourse increasingly grapples with carbon pricing as a potential tool; while India has not yet adopted a national carbon tax or ETS, pilot carbon offset markets and corporate carbon accounting are growing. The World Bank's data informs India's cost-benefit analysis of market-based climate instruments versus direct command-and-control regulation.",
     "AP_HC", "International_Current_Affairs"),

    (28022, "According to the Carbon Pricing Report 2025, how many active carbon pricing instruments exist globally?",
     "40", "60", "80", "100",
     "C", "There are 80 active carbon pricing instruments globally (up from just 5 in 2005), according to World Bank's Carbon Pricing report 2025. This 16-fold expansion—spanning ETS, carbon taxes, and carbon offset programs—demonstrates mainstreaming of market-based climate policy. India observes this trend as potential future policy; however, applying carbon pricing to a developing economy requires careful attention to competitiveness of export-oriented industries, energy-intensive MSMEs, and energy access for low-income populations, making any future carbon pricing framework uniquely complex.",
     "AP_HC", "International_Current_Affairs"),

    (28023, "The carbon pricing mechanisms cover what percentage of global GHG emissions as per the 2025 World Bank report?",
     "15%", "21%", "28%", "35%",
     "C", "Active carbon pricing mechanisms cover 28% of global greenhouse gas emissions according to the World Bank report 2025. Despite the proliferation of 80 instruments, coverage remains limited to wealthy economies and EU countries, reflecting the political difficulty of carbon pricing in developing nations. India's reluctance to adopt carbon pricing stems from equity principles—developing countries argue they should not bear climate mitigation costs comparable to historical emitters—reinforcing India's diplomatic position that climate finance and technology transfer must accompany any global carbon pricing regime.",
     "AP_HC", "International_Current_Affairs"),

    (28024, "IRENA, which publishes Renewable Energy Statistics, is headquartered in:",
     "Geneva, Switzerland", "Paris, France", "Abu Dhabi, UAE", "Vienna, Austria",
     "C", "IRENA (International Renewable Energy Agency) is headquartered in Abu Dhabi, UAE. This location in a major oil-producing nation signals the global transition away from fossil fuels and the growing strategic importance of renewables in Middle East energy policy. India is an active IRENA member and participant in its renewable energy roadmaps and capacity-building programs; IRENA's data on renewable energy generation costs and deployment trajectories directly inform India's renewable energy auctions and technology acquisition strategies.",
     "AP_HC", "International_Current_Affairs"),

    # ── Social Security & Population ──
    (28025, "According to ILO data, India ranked _____ globally for the number of people covered under social security.",
     "1st", "2nd", "3rd", "5th",
     "B", "India ranked 2nd globally (ILO ILOSTAT) for the absolute number of people covered under social security — approximately 940 million people. India's vast social security coverage reflects its massive formal and informal sector populations and the government's ambitious schemes including PMJDY (Jan Dhan), PMSYM (pension), and PMSBY (insurance). The 940 million figure underscores India's dual development challenge: managing huge absolute numbers while still improving per-capita benefit adequacy and closing gaps in coverage for vulnerable informal workers estimated at 400+ million.",
     "AP_HC", "International_Current_Affairs"),

    (28026, "India's social security coverage grew from 19% (2015) to what percentage by 2025?",
     "45.6%", "54.2%", "64.3%", "72.1%",
     "C", "India's social security coverage grew from 19% in 2015 to 64.3% in 2025 — the fastest expansion in the world. This 45-percentage-point gain over a decade reflects an unprecedented push by the Modi government to universalize access via digital ID (Aadhaar), direct benefit transfers, and mass enrollment in pension, insurance, and savings schemes. This expansion is crucial for India's SDG achievement and poverty reduction targets; however, sustainability challenges include benefit adequacy (many schemes provide nominal coverage without sufficient cash transfers) and ongoing coverage of the poorest quintiles still outside formal schemes.",
     "AP_HC", "International_Current_Affairs"),

    (28027, "UNFPA's State of World Population (SOWP) 2025 report was themed:",
     "The Ageing World", "Population Without Borders", "The Real Fertility Crisis", "7 Billion and Beyond",
     "C", "UNFPA's SOWP 2025 was themed 'The Real Fertility Crisis', highlighting that both very high and very low fertility pose challenges. This theme reflects divergent demographic trends: developed countries face aging and population decline, while Sub-Saharan Africa still faces youth bulges requiring massive investment in education and jobs. India represents a unique transition—fertility falling below replacement (TFR 2.0) while population still growing to 1.45+ billion due to demographic momentum, creating a narrow window for capturing the 'demographic dividend' through education and skill development before aging emerges.",
     "AP_HC", "International_Current_Affairs"),

    (28028, "UNFPA stands for:",
     "UN Food and Population Agency", "UN Fund for Population Activities", "United Nations Population Fund", "Universal Family Planning Agency",
     "C", "UNFPA stands for United Nations Population Fund (formerly United Nations Fund for Population Activities). UNFPA works on sexual and reproductive health, maternal mortality reduction, and gender equality—areas central to India's SDG performance. India has achieved significant declines in maternal mortality (from 212 per 100,000 live births in 2007 to ~97 in 2023) through UNFPA-supported programs and government schemes; however, wide state-level variation and rural-urban divides remain, requiring continued policy attention and targeted health system strengthening.",
     "AP_HC", "International_Current_Affairs"),

    (28029, "According to UNHCR Global Trends 2024, how many people were forcibly displaced worldwide?",
     "97.3 million", "110.8 million", "123.2 million", "135.6 million",
     "C", "UNHCR's Global Trends 2024 reported a record 123.2 million forcibly displaced people worldwide. This figure reflects escalating conflicts in Sudan, Ukraine, Syria, Myanmar, and Gaza, plus climate-induced migration pressures. India hosts approximately 500,000+ registered refugees (mostly from Afghanistan, Myanmar, Sri Lanka) and manages border pressures from climate-vulnerable populations in Bangladesh and Myanmar; India's refugee policy balances humanitarian obligations with domestic security and development resource constraints, requiring careful diplomatic navigation.",
     "AP_HC", "International_Current_Affairs"),

    (28030, "What percentage of forcibly displaced persons globally were children, as per UNHCR 2024?",
     "25%", "33%", "40%", "48%",
     "C", "According to UNHCR Global Trends 2024, children constituted approximately 40% of all forcibly displaced persons. This disproportionate impact on children reflects conflicts targeting civilians and climate disasters affecting population-dense regions in Africa and South Asia. For India, managing child welfare in refugee camps and preventing child trafficking among displaced populations—both internal (droughts, floods) and cross-border—is a key humanitarian and development priority aligned with India's SDG 5 (Gender Equality) and SDG 16 (Peace and Justice) commitments.",
     "AP_HC", "International_Current_Affairs"),

    (28031, "How many people were Internally Displaced Persons (IDPs) according to UNHCR 2024?",
     "61.5 million", "68.2 million", "73.5 million", "80.1 million",
     "C", "73.5 million people were internally displaced within their own countries according to UNHCR's Global Trends 2024. IDPs—displaced by conflict or disaster but within national borders—outnumber refugees by 3:1, reflecting the dominance of internal displacement over cross-border migration. India, with an estimated 6-8 million internal climate migrants annually and conflict-induced IDPs from north-eastern states and Maoist-affected regions, requires robust internal displacement frameworks, social protection programs, and livelihood rehabilitation strategies aligned with disaster management and developmental priorities.",
     "AP_HC", "International_Current_Affairs"),

    (28032, "Which country was the top source of forcibly displaced people according to UNHCR 2024?",
     "Syria", "Afghanistan", "Sudan", "Ukraine",
     "C", "Sudan became the top source of forcibly displaced people globally in 2024, surpassing previous leaders Syria and Afghanistan. Sudan's displacement crisis—driven by the 2023 outbreak of conflict between the SAF and RSF—has created 14+ million displaced, including 7+ million internally and 5+ million refugees in neighboring Egypt, Chad, and South Sudan. This reflects how new conflicts rapidly destabilize regions; India faces similar pressures from Afghanistan refugee flows and potential climate-driven migrations from South/Southeast Asia, requiring strengthened regional humanitarian frameworks and migration management capacity.",
     "AP_HC", "International_Current_Affairs"),

    (28033, "The Global Education Monitoring (GEM) Report is published by which organisation?",
     "UNICEF", "UNESCO", "World Bank", "UNDP",
     "B", "The GEM Report is published by UNESCO (UN Educational, Scientific and Cultural Organization), headquartered in Paris. UNESCO's GEM Report, released annually, tracks progress on SDG 4 (Quality Education) globally and identifies equity gaps in learning outcomes, gender access, and teacher quality. India's education policy makers use GEM data to benchmark performance against peer economies, identify gaps in learning outcomes (only 27% of Grade 3 students in India can read at grade level), and design interventions under the National Education Policy 2020 aimed at universalizing access and improving learning quality.",
     "AP_HC", "International_Current_Affairs"),

    (28034, "According to the UNESCO GEM Report, how many children are out of school globally?",
     "198 million", "235 million", "272 million", "308 million",
     "C", "The UNESCO Global Education Monitoring Report states that approximately 272 million children are currently out of school worldwide. This persists despite universal education goals; out-of-school rates remain high in Sub-Saharan Africa (19%), South/West Asia (11%), and among girls, disabled children, and conflict-affected populations. India, hosting ~28 million out-of-school children, focuses remediation through schemes like Samagra Shiksha, midday meal programs, and scholarship policies; however, quality of schooling and learning outcomes require equal attention alongside enrollment to achieve SDG 4 targets.",
     "AP_HC", "International_Current_Affairs"),

    # ── Economic Reports ──
    (28035, "The UN World Economic Situation and Prospects (WESP) 2025 was published by:",
     "UN DESA", "IMF", "World Bank", "UNCTAD",
     "A", "WESP 2025 is published by UN DESA (Department of Economic and Social Affairs). WESP provides integrated analysis of macroeconomic trends, development financing, and inequality impacts—offering a development-focused perspective distinct from the IMF's financial stability focus. India relies on WESP data to track global growth outlooks, international trade dynamics, and the adequacy of development finance flows to emerging markets, particularly in assessing concessional lending availability and South-South cooperation opportunities.",
     "AP_HC", "International_Current_Affairs"),

    (28036, "What global GDP growth rate did WESP 2025 project for 2025?",
     "1.8%", "2.4%", "3.1%", "3.8%",
     "B", "WESP 2025 projected global GDP growth of 2.4% for 2025. This modest growth—below the 2.9% historical average—reflects geopolitical fragmentation, high debt burdens in advanced economies, and persistent inflation concerns. WESP's projection is crucial for India's export planning and foreign direct investment expectations; India's development strategy depends on robust global growth to absorb exports and support remittances, making India sensitive to any downward revisions in global growth forecasts.",
     "AP_HC", "International_Current_Affairs"),

    (28037, "India's GDP growth rate projected in UN WESP 2025 was:",
     "5.1%", "5.9%", "6.3%", "7.2%",
     "C", "India's GDP growth was projected at 6.3% in WESP 2025, making it the fastest-growing major economy. This projection assumes sustained private investment, government capex, and robust domestic consumption despite global headwinds. India's growth advantage—driven by demographics, digital transformation, and manufacturing relocation from China—is contingent on maintaining macroeconomic stability, expanding exports, and accelerating skill development; any sharp global slowdown could depress India's growth by 1-2 percentage points, impacting poverty reduction and employment targets.",
     "AP_HC", "International_Current_Affairs"),

    (28038, "UNCTAD's 'World of Debt' report revealed global public debt reached:",
     "$78 trillion", "$92 trillion", "$102 trillion", "$115 trillion",
     "C", "UNCTAD's World of Debt report revealed global public debt reached a record $102 trillion. This unprecedented level—exceeding global GDP—reflects pandemic fiscal stimulus, higher interest rates, and structural budget deficits in developed economies. For India, persistently high global debt constrains international development financing available to emerging economies, reduces concessional lending (as developed economies prioritize domestic debt management), and increases risk premiums on sovereign borrowing; India's fiscal consolidation efforts are thus essential to maintain market access and preserve fiscal space for development.",
     "AP_HC", "International_Current_Affairs"),

    (28039, "UNCTAD is headquartered in:",
     "New York, USA", "Geneva, Switzerland", "Vienna, Austria", "Paris, France",
     "B", "UNCTAD (United Nations Conference on Trade and Development) is headquartered in Geneva, Switzerland. UNCTAD, established in 1964 during decolonization, advocates for developing country interests in trade, investment, and development policy—serving as an institutional check on IMF/World Bank orthodoxy. India chairs UNCTAD's Trade and Development Board periodically and uses UNCTAD platforms to advance South-South cooperation, reform global trade rules, and secure technology transfer commitments aligned with India's development agenda and export competitiveness.",
     "AP_HC", "International_Current_Affairs"),

    (28040, "Which report replaced the World Bank's discontinued Ease of Doing Business report?",
     "Global Business Index", "Business Friendly Report", "Business Ready (B-READY)", "World Competitiveness Yearbook",
     "C", "The World Bank replaced the Ease of Doing Business report (discontinued in 2021 due to data irregularities) with the Business Ready (B-READY) report, first edition released in 2024. B-READY focuses on broader regulatory quality, public services, and operational efficiency rather than just compliance costs, providing a more development-relevant assessment. India views B-READY as an opportunity to improve rankings compared to the Ease of Doing Business metrics; India's policy focus on simplifying regulations, digitizing government services, and reducing bureaucratic burden aligns with B-READY assessment criteria, supporting the government's stated objective to rank in the top 50 globally.",
     "AP_HC", "International_Current_Affairs"),

    # ── Fisheries ──
    (28041, "Which organisation published the 'Review of the State of World Marine Fishery Resources 2025'?",
     "UNEP", "UNDP", "FAO", "WWF",
     "C", "The Review of the State of World Marine Fishery Resources is published by FAO (Food and Agriculture Organization), headquartered in Rome. FAO's fisheries assessments are critical for ocean governance, as marine fisheries provide food security for 3+ billion people and livelihoods for 250+ million. India, with the world's second-largest fishing fleet and a 7,500+ km coastline, depends on FAO data to manage its EEZ sustainably, develop aquaculture (already contributing 8+ million tons), and protect coastal community livelihoods as fish stocks deplete from climate change and overfishing.",
     "AP_HC", "International_Current_Affairs"),

    (28042, "According to FAO's marine fisheries report 2025, what percentage of fish stocks are being fished at biologically sustainable levels?",
     "55.2%", "60.1%", "64.5%", "71.3%",
     "C", "64.5% of fish stocks were being fished within biologically sustainable levels according to FAO's marine fisheries report 2025. This means 35.5% are overfished—a critical concern as overfishing undermines food security, particularly in South Asia where fish provides 15-20% of animal protein. India's Blue Revolution initiative targets sustainable aquaculture expansion while implementing stricter EEZ management; however, monitoring compliance remains challenging in India's vast maritime zones, requiring investment in digital fishing vessel tracking and regional fisheries management cooperation.",
     "AP_HC", "International_Current_Affairs"),

    (28043, "What percentage of global marine fish stocks are overfished according to FAO 2025?",
     "18.5%", "28.3%", "35.5%", "42.1%",
     "C", "35.5% of global marine fish stocks are overfished according to FAO's 2025 marine fisheries review. Overfishing, driven by illegal unreported unregulated (IUU) fishing, insufficient enforcement, and weak regional management, threatens 2+ billion livelihoods and fish-dependent food systems. India faces these challenges in the Indian Ocean; strengthening India's Coast Guard capacity, implementing satellite vessel monitoring, prosecuting IUU fishing operations, and cooperating with SAARC nations on fisheries management are essential to protect India's marine resources and coastal communities.",
     "AP_HC", "International_Current_Affairs"),

    (28044, "FAO's biennial fisheries publication covering both marine and aquaculture is known as:",
     "SOFIA", "GRFC", "SOFI", "SIFA",
     "A", "SOFIA (The State of World Fisheries and Aquaculture) is FAO's biennial publication covering global fisheries and aquaculture. SOFIA tracks both capture fisheries (wild-caught) and aquaculture production, providing comprehensive food system analysis. India uses SOFIA data to assess the relative roles of marine and inland fisheries, freshwater aquaculture, and cage farming in achieving nutritional security; SOFIA benchmarks help India prioritize aquaculture development (particularly in ponds and tanks) as a more sustainable path than marine extraction for scaling fish protein supply.",
     "AP_HC", "International_Current_Affairs"),

    # ── Military & Nuclear ──
    (28045, "SIPRI is headquartered in which city?",
     "Stockholm (Solna), Sweden", "Oslo, Norway", "Copenhagen, Denmark", "Helsinki, Finland",
     "A", "SIPRI (Stockholm International Peace Research Institute) is headquartered in Solna, near Stockholm, Sweden. SIPRI, established in 1966, is an independent institute providing data on military expenditure, arms transfers, and nuclear weapons—research critical for peace and security studies. India, engaged in regional security competition with China and Pakistan and modernizing its military (5-6% of budget), uses SIPRI data for comparative military analysis, nuclear deterrence assessments, and transparency in defense procurement and spending justification to international partners.",
     "AP_HC", "International_Current_Affairs"),

    (28046, "According to SIPRI Yearbook 2025, Russia possesses how many nuclear warheads?",
     "4,612", "5,177", "5,459", "6,213",
     "C", "Russia has 5,459 nuclear warheads according to the SIPRI Yearbook 2025. Russia's large nuclear arsenal reflects Cold War legacy and continued nuclear modernization despite geopolitical isolation post-Ukraine invasion. India, with an estimated 170+ nuclear warheads, maintains a smaller but survivable deterrent under a no-first-use doctrine; India's position in the nuclear hierarchy (middle power) informs its approach to nuclear disarmament negotiations at the UN and its diplomatic strategy regarding nuclear non-proliferation frameworks.",
     "AP_HC", "International_Current_Affairs"),

    (28047, "How many nuclear warheads does the USA possess according to SIPRI 2025?",
     "4,823", "5,177", "5,459", "5,800",
     "B", "The USA possesses 5,177 nuclear warheads according to SIPRI Yearbook 2025. The USA and Russia together account for 90%+ of global nuclear warheads; their strategic competition and potential arms control breakdowns (post-New START) are critical global security concerns. India, as a non-signatory to NPT and CTBT, conducts independent nuclear deterrence development; India's nuclear policy emphasizes that disarmament is a global responsibility of all nuclear powers, not just non-nuclear states, shaping India's negotiating stance at nuclear forums.",
     "AP_HC", "International_Current_Affairs"),

    (28048, "Global military expenditure reached what record level in 2024 according to SIPRI?",
     "$1.8 trillion", "$2.1 trillion", "$2.4 trillion", "$2.8 trillion",
     "C", "Global military expenditure reached a record ~$2.4 trillion in 2024 according to SIPRI. This unprecedented spending—4.2% of global GDP and up 50% since 2014—reflects rising geopolitical tensions, regional conflicts (Ukraine, Middle East, South China Sea), and arms races. India, spending approximately $70-72 billion annually (2.8% of budget), is modernizing its military to counter China and Pakistan while managing fiscal constraints; India advocates for reducing global military spending and redirecting resources to development, positioning military efficiency and indigenous defense manufacturing as pathways to cost containment.",
     "AP_HC", "International_Current_Affairs"),

    (28049, "The Global Peace Index is published by which organisation?",
     "SIPRI", "IEP (Institute for Economics and Peace)", "UNDP", "UN Security Council",
     "B", "The Global Peace Index is published by IEP (Institute for Economics and Peace), headquartered in Sydney, Australia. IEP measures peace across 23 indicators covering militarization, violence, and institutional capacity for peace. India's GPI ranking (115 out of 163 in 2025) reflects its internal security challenges (insurgencies, communal tensions) and regional conflicts with Pakistan and tensions with China, making peace indicators relevant to India's stability narrative and counterinsurgency effectiveness in Jammu-Kashmir, northeastern states, and Maoist-affected regions.",
     "AP_HC", "International_Current_Affairs"),

    (28050, "Which country consistently tops the Global Peace Index?",
     "Switzerland", "Denmark", "Iceland", "New Zealand",
     "C", "Iceland consistently tops the Global Peace Index as the world's most peaceful country. Iceland's top ranking reflects minimal military spending, negligible crime, strong institutions, and social cohesion—a model far different from India's context. Yet India observes Iceland's investment in institutional quality, rule of law, and conflict prevention as aspirational; India's justice sector reforms, police modernization, and community policing initiatives are partly motivated by peace index metrics showing that institutional strength and access to justice reduce violence.",
     "AP_HC", "International_Current_Affairs"),

    # ── SDG & Governance ──
    (28051, "India's rank in the India SDG Index 2025 (global) was:",
     "105th", "99th", "112th", "87th",
     "B", "India ranked 99th in the SDG Index 2025 — the first time India entered the top 100. This achievement reflects accelerated progress in poverty reduction, health, education, and renewable energy expansion; however, India still lags on gender equality (SDG 5), inequality (SDG 10), and environmental sustainability (SDGs 13-15). Crossing the top-100 threshold validates India's development strategy and justifies India's push for South-South cooperation and narrative of 'responsible development,' strengthening India's diplomatic credibility on development issues at G20 and UN forums.",
     "AP_HC", "International_Current_Affairs"),

    (28052, "Who publishes the India SDG Index?",
     "Ministry of Statistics", "NITI Aayog", "Planning Commission", "UNDP India",
     "B", "The India SDG Index is published by NITI Aayog (National Institution for Transforming India). NITI Aayog, established as the planning body replacing the Planning Commission, tracks India's SDG progress across 115 indicators across all 17 SDGs, disaggregated by state. This domestic index is crucial for inter-state competition and accountability; states competing for higher SDG Index scores provides incentive structures for policy reform, budget allocation, and service delivery improvements—making the India SDG Index a powerful tool for development federalism and sub-national governance.",
     "AP_HC", "International_Current_Affairs"),

    (28053, "India's SDG overall score improved from 57 in 2018 to what in 2025?",
     "62", "66", "71", "78",
     "C", "India's SDG overall score improved from 57 in 2018 to 71 in 2025 according to NITI Aayog's India SDG Index. This 14-point gain over 7 years, while impressive, requires acceleration to reach 100 (full SDG achievement) by 2030. The improvement reflects gains in poverty (SDG 1), hunger (SDG 2), health (SDG 3), and energy (SDG 7); however, India's weaker performance on gender (SDG 5), inequality (SDG 10), and environmental targets (SDGs 13-15) indicates that inclusive growth and environmental sustainability require intensified policy focus and budget reallocation.",
     "AP_HC", "International_Current_Affairs"),

    (28054, "The Performance Grading Index (PGI) 2.0 for school education is published by:",
     "NITI Aayog", "Ministry of Education", "University Grants Commission", "NCERT",
     "B", "The PGI 2.0 for school education is published by the Ministry of Education, Government of India. PGI 2.0, introduced in 2021, measures school system performance across domains including access, infrastructure, teacher quality, and learning outcomes using 73 indicators—directly supporting India's National Education Policy 2020 implementation. State-level PGI rankings drive competitive federalism, incentivizing states to improve learning outcomes, increase school infrastructure investment, and enhance teacher development programs—critical for India's goal of universal primary completion and improved learning quality.",
     "AP_HC", "International_Current_Affairs"),

    (28055, "Which state/UT topped the Performance Grading Index (PGI) 2.0?",
     "Delhi", "Kerala", "Chandigarh", "Tamil Nadu",
     "C", "Chandigarh (UT) topped the Performance Grading Index (PGI) 2.0. Chandigarh's first-rank position reflects advantages of a smaller, more planned urban polity with concentrated resources, trained teachers, and better infrastructure; however, this advantage underscores the challenge for large states (Uttar Pradesh, Bihar, Madhya Pradesh) with limited resources and vast rural populations. PGI rankings highlight the systemic factors determining education outcomes and guide central and state budgets toward gap-closing investments.",
     "AP_HC", "International_Current_Affairs"),

    (28056, "Which state was at the bottom of the Performance Grading Index (PGI) 2.0?",
     "Bihar", "Meghalaya", "Jharkhand", "Nagaland",
     "B", "Meghalaya was at the bottom of the Performance Grading Index (PGI) 2.0. Meghalaya's lowest ranking reflects systemic challenges in infrastructure, teacher recruitment, training, and learning assessment—common across northeastern and low-capacity states. Low PGI rankings are diagnostic; states use PGI results to identify priority areas (e.g., teacher supply, learning improvement initiatives), access central government support programs like Samagra Shiksha, and attract philanthropic education funding—making PGI actionable for targeted capacity building.",
     "AP_HC", "International_Current_Affairs"),

    (28057, "The PGI 2.0 uses how many indicators across 6 domains?",
     "55 indicators, 800 points", "73 indicators, 1000 points", "80 indicators, 900 points", "65 indicators, 750 points",
     "B", "PGI 2.0 uses 73 indicators spread across 6 domains for a total score of 1000 points. The six domains are: (1) learning outcomes; (2) access; (3) infrastructure and facilities; (4) equity; (5) governance; and (6) teacher management. This multidimensional approach captures education quality holistically, moving beyond enrollment to assess teaching quality, equity (gender, SC/ST, disability), and learning achievement—aligned with India's SDG 4 obligations and National Education Policy targets for universal completion and improved learning quality.",
     "AP_HC", "International_Current_Affairs"),

    (28058, "The Corruption Perceptions Index (CPI) is published by:",
     "World Bank", "Transparency International", "UNDP", "WEF",
     "B", "The Corruption Perceptions Index is published by Transparency International, headquartered in Berlin, Germany. TI's CPI aggregates expert and business perceptions of corruption in public sectors, informing investment decisions and foreign aid allocation. India's CPI performance (rank 96 in 2024) affects India's international credibility on governance; high corruption perceptions, though based on surveys rather than convictions, complicate India's investment promotion and G20 governance narrative. India's anti-corruption programs (PMLA, financial inclusion, digital governance) are partly motivated by CPI benchmarking.",
     "AP_HC", "International_Current_Affairs"),

    (28059, "India's rank in the Corruption Perceptions Index 2024 (released Feb 2025) was:",
     "73", "85", "96", "107",
     "C", "India ranked 96 out of 180 countries in the CPI 2024 with a score of 38 (down from rank 93 / score 39 in 2023, representing a 3-rank slip and 1-point decline). Denmark topped (CPI 90), followed by Finland and Singapore. India's declining trend, while modest, signals concerns among international investors and partners about governance quality. India's slide requires accelerated anti-corruption enforcement, public service reform, and e-governance scaling to improve international perceptions and strengthen India's position as an attractive FDI destination competing with Vietnam and Indonesia.",
     "AP_HC", "International_Current_Affairs"),

    (28060, "Which country topped the Corruption Perceptions Index 2024 (least corrupt)?",
     "Finland", "Norway", "Denmark", "Singapore",
     "C", "Denmark topped the CPI 2024 as the least corrupt country with a score of 90. The scale runs 0-100, with 0 indicating extreme corruption and 100 indicating very clean governance. Nordic countries' dominance reflects strong rule of law, independent judiciaries, free media, and transparent public procurement—institutional features India aims to strengthen through judicial reforms, anti-corruption agencies, and digital governance platforms. India's 38 score, while placing it in the lower-middle range, contrasts with peer emerging markets, highlighting reform urgency.",
     "AP_HC", "International_Current_Affairs"),

    # ── Innovation & Competitiveness ──
    (28061, "The Global Innovation Index (GII) is published by:",
     "WEF", "UNDP", "WIPO", "World Bank",
     "C", "The Global Innovation Index is published by WIPO (World Intellectual Property Organization), headquartered in Geneva. WIPO, as the UN's IP agency, measures innovation ecosystems using 34 indicators including R&D investment, patent activity, educational quality, and creative goods exports. India's GII performance is strategically important as India seeks to transition from manufacturing-led to innovation-driven growth; WIPO data informs India's IP policy, startup ecosystem development, and technology commercialization programs under initiatives like Startup India and Atal Innovation Mission.",
     "AP_HC", "International_Current_Affairs"),

    (28062, "India's rank in the WIPO Global Innovation Index 2025 was:",
     "29th", "38th", "49th", "55th",
     "B", "India ranked 38th out of 139 economies in the GII 2025—improving by one position from rank 39 in 2024 and from rank 81 in 2015, representing a 43-position climb in a decade. India remains the top-performing lower-middle-income economy and leads South Asia. This progress reflects growth in software patents, IT services exports, and startup ecosystems; however, India lags on manufacturing innovation and hardware patents, requiring policy focus on industrial R&D, university-industry collaboration, and design capabilities to capture higher value-add manufacturing segments.",
     "AP_HC", "International_Current_Affairs"),

    (28063, "Which country topped the WIPO Global Innovation Index 2025?",
     "USA", "Germany", "Sweden", "Switzerland",
     "D", "Switzerland topped the GII 2025 for its 15th consecutive year, followed by Sweden and the USA. Switzerland's sustained leadership reflects world-class universities, high R&D intensity (3.7% of GDP), strong IP protection, and a developed-economy innovation ecosystem. India, competing as a lower-middle-income nation, cannot replicate Switzerland's model; instead, India pursues frugal innovation, digital-first approaches, and software-embedded solutions suited to India's resource constraints, population size, and development stage, positioning India as an innovation leader for the Global South.",
     "AP_HC", "International_Current_Affairs"),

    (28064, "The Global Competitiveness Report is published by which organisation?",
     "World Bank", "IMF", "World Economic Forum (WEF)", "OECD",
     "C", "The Global Competitiveness Report is published by the World Economic Forum (WEF), headquartered in Cologny near Geneva, Switzerland. The WEF's Global Competitiveness Index measures 12 pillars of competitiveness including infrastructure, human capital, institutions, macroeconomic stability, and market functioning. India's competitiveness ranking directly influences investor perceptions and capital flows; India's ongoing infrastructure modernization (highways, ports, airports), skills development, and labor market reforms are partly driven by WEF competitiveness metrics, helping India improve manufacturing competitiveness against China and attract global value chain relocation.",
     "AP_HC", "International_Current_Affairs"),

    # ── HDI & Gender ──
    (28065, "The Human Development Index (HDI) is published by:",
     "World Bank", "UNDP", "UNFPA", "UN DESA",
     "B", "The Human Development Index is published by UNDP (United Nations Development Programme). The HDI, introduced in 1990, revolutionized development measurement by moving beyond GDP to include health and education, challenging the notion that economic growth alone determines development. UNDP's HDI framework legitimizes India's focus on social development metrics and validates India's policy priority of expanding health and education access alongside poverty reduction, supporting the government's narrative of 'inclusive growth' at global development forums.",
     "AP_HC", "International_Current_Affairs"),

    (28066, "India's rank in the UNDP Human Development Report 2025 (released May 2025) was:",
     "112", "125", "130", "142",
     "C", "India ranked 130 out of 193 countries in the HDI 2025 report (released May 2025), with an HDI value of 0.685 (up from 0.676 in 2022). It remains in the 'Medium Human Development' category, approaching but not yet reaching the 0.700 threshold for 'High' development classification. India's HDI progress reflects gains in life expectancy (now 72+ years) and education enrollment; however, persisting rural-urban, gender, and caste-based disparities in health and education limit India's HDI score, requiring targeted investments in rural healthcare, girls' education, and SC/ST development programs.",
     "AP_HC", "International_Current_Affairs"),

    (28067, "The HDI measures three dimensions of human development. Which of the following is NOT one of them?",
     "Life expectancy", "Education (years of schooling)", "Per-capita income (GNI)", "Environmental sustainability",
     "D", "HDI measures three dimensions: (1) Life expectancy; (2) Education (mean years + expected years of schooling); and (3) GNI per capita (PPP-adjusted). Environmental sustainability is NOT a direct HDI component, though UNDP publishes supplementary indices (Adjusted HDI, Gender Development Index) that incorporate environmental and equity adjustments. India's exclusion of environmental sustainability from core HDI—while convenient for raising India's score—is a gap India seeks to address through supplementary reporting on ecological sustainability and inclusive development metrics.",
     "AP_HC", "International_Current_Affairs"),

    (28068, "The Gender Gap Report is published by:",
     "UNDP", "UN Women", "World Economic Forum (WEF)", "ILO",
     "C", "The Gender Gap Report is published by the World Economic Forum (WEF). The WEF's Global Gender Gap Index measures gender parity across four pillars: economic participation, education, health, and political empowerment. India's poor performance on gender metrics reflects women's low labor force participation (25% vs. 70%+ globally), political underrepresentation (15-20% of legislatures), and health gaps; addressing gender inequality is critical for India's demographic dividend, labor force expansion, and inclusive growth objectives outlined in India's development strategies.",
     "AP_HC", "International_Current_Affairs"),

    (28069, "India's rank in the WEF Global Gender Gap Report 2025 was:",
     "114th", "122nd", "131st", "138th",
     "C", "India ranked 131 out of 148 countries in the Global Gender Gap Report 2025 (parity score 64.1%)—a drop of 2 ranks from 129 in 2024, mainly due to declining political empowerment. This 2-rank decline, despite reserve provisions (33% quota) for women in local government, indicates that constitutional reservations are insufficient without complementary interventions on female education, workforce participation, and safety. India's low gender parity score constrains its development progress, limits labor force potential by excluding ~50% of population, and undermines demographic dividend realization.",
     "AP_HC", "International_Current_Affairs"),

    (28070, "Which country consistently tops the Global Gender Gap Report?",
     "Norway", "Sweden", "Finland", "Iceland",
     "D", "Iceland consistently tops the Global Gender Gap Report, maintaining its lead for 16+ consecutive years with a near-perfect parity score (0.913 out of 1.0). Iceland's sustained leadership reflects strong gender-inclusive culture, parental leave policies, equal pay enforcement, and high female education/workforce participation. India views Iceland's model as aspirational; India's policies—including maternity benefits expansion, workplace safety initiatives (POSH Act), and women's entrepreneurship support—aim to gradually narrow India's 36-point gender parity gap, though structural social change requires generational effort.",
     "AP_HC", "International_Current_Affairs"),

    # ── Happiness & Logistics ──
    (28071, "The World Happiness Report is published by:",
     "UNDP", "UN Sustainable Development Solutions Network (UNSDSN)", "WHO", "WEF",
     "B", "The World Happiness Report is published by the UN Sustainable Development Solutions Network (UNSDSN), a UN initiative supporting SDG implementation. The report measures life satisfaction/subjective well-being across 146 countries using survey data on income, health, social support, freedom, generosity, and perceptions of corruption. India's low happiness ranking reflects mass poverty, limited social safety nets, and perceptions of limited personal freedom; improving India's happiness score requires sustained improvements in income security, health quality, and governance, making well-being a strategic development metric beyond GDP growth.",
     "AP_HC", "International_Current_Affairs"),

    (28072, "Which country topped the World Happiness Report 2025 for the 8th consecutive year?",
     "Norway", "Iceland", "Denmark", "Finland",
     "D", "Finland topped the World Happiness Report 2025 for the 8th consecutive year (WHR 2018-2025). Finland's consistent leadership reflects strong institutions, universal health/education, work-life balance policies, and low inequality—contrasting starkly with India's mass poverty and inequality. Finland's happiness model, though culturally specific, offers India lessons on the nexus between institutional quality, social trust, and subjective well-being; India's happiness improvements require complementary advances in education access, healthcare quality, economic security, and perceptions of fairness.",
     "AP_HC", "International_Current_Affairs"),

    (28073, "The Logistics Performance Index (LPI) is published by which organisation?",
     "IMF", "UNCTAD", "World Bank", "ILO",
     "C", "The Logistics Performance Index is published by the World Bank. The LPI measures trade logistics performance across six components: customs efficiency, infrastructure quality, tracking/tracing capability, timeliness, competence, and services cost—indicators critical for export competitiveness. India's LPI performance directly affects its ability to attract manufacturing FDI; India's Logistics Division, port modernization programs, and customs digitalization are partly driven by LPI benchmarking to improve India's export cost-competitiveness against Vietnam, Thailand, and Indonesia in global manufacturing supply chains.",
     "AP_HC", "International_Current_Affairs"),

    (28074, "India's rank in the Logistics Performance Index 2023 was:",
     "30th", "38th", "44th", "52nd",
     "B", "India ranked 38th in the Logistics Performance Index 2023, improving from 44th in 2018—a gain of 6 positions in five years. This steady improvement reflects India's infrastructure investments (highways, ports, airports), customs digitalization (ICEGATE), and supply chain development; however, India still lags developed economies and competes with Vietnam (32) and Thailand (30) in regional manufacturing attraction. Further LPI improvement requires accelerated port modernization, inland waterway development, last-mile distribution networks, and reduction of regulatory delays affecting export logistics costs.",
     "AP_HC", "International_Current_Affairs"),

    # ── Health ──
    (28075, "The Global TB Report is published by which organisation?",
     "UNICEF", "WHO", "Ministry of Health India", "UNDP",
     "B", "The Global TB Report is published annually by WHO (World Health Organization). The report tracks TB cases, deaths, treatment success, and drug resistance globally, providing accountability on SDG 3 (Health). India, with the world's largest TB burden (~25% of global cases), uses WHO TB Report data to monitor progress under the National TB Elimination Programme 2017-2025; India's target to achieve TB elimination by 2025 (5 years ahead of global 2030 target) requires sustained political commitment, diagnostics scale-up, and treatment adherence programs.",
     "AP_HC", "International_Current_Affairs"),

    (28076, "According to WHO Global TB Report 2025, India accounts for approximately what share of global TB cases?",
     "16%", "20%", "25%", "32%",
     "C", "India accounts for approximately 25% of global TB cases per WHO Global TB Report 2025, retaining the highest TB burden globally (~27 million cases estimated cumulatively). India's TB incidence fell 21% from 237/100,000 (2015) to 187/100,000 (2024), demonstrating progress; however, absolute case numbers remain high due to India's large population, requiring sustained high-intensity case detection, treatment access in rural areas, and private sector engagement to achieve elimination by 2025.",
     "AP_HC", "International_Current_Affairs"),

    (28077, "India's national target year to eliminate TB (set ahead of the global SDG target of 2030) was:",
     "2023", "2025", "2027", "2030",
     "B", "India set 2025 as its TB elimination target (5 years ahead of the global SDG target of 2030). As of 2025, while full elimination was not achieved, India achieved a 21% drop in incidence and 92% treatment success rate per WHO Global TB Report 2025. India's ambitious target, though ambitious, reflects political commitment under the National TB Elimination Programme; even if full elimination is not achieved by 2025, India's trajectory of declining burden and improving treatment access positions India as a TB control leader, potentially enabling earlier global TB eradication.",
     "AP_HC", "International_Current_Affairs"),

    (28078, "According to NFHS-5 (2019–21), India's Total Fertility Rate (TFR) stood at:",
     "1.8", "2.0", "2.3", "2.5",
     "B", "India's TFR was 2.0 in NFHS-5 (2019–21), falling below the replacement level of 2.1 for the first time. This demographic transition milestone—achieved earlier than India's earlier projections—reflects accelerated education expansion, women's empowerment, contraceptive access, and rising age at marriage/first birth. India's below-replacement fertility, while positive for poverty reduction and education per capita, signals approaching demographic aging; India must capitalize on the 'demographic dividend' window (15-20 years) through aggressive skill development and job creation before India transitions to an aging society requiring different policy priorities.",
     "AP_HC", "International_Current_Affairs"),

    # ── Mixed / Publisher Identification ──
    (28079, "Which of the following reports is published by the IMF?",
     "World Energy Investment Report", "World Economic Outlook", "State and Trends of Carbon Pricing", "Global Report on Food Crises",
     "B", "The World Economic Outlook (WEO) is published by the IMF (International Monetary Fund). IEA publishes WEI Report; World Bank publishes Carbon Pricing; GNAFC+FSIN publish GRFC. The IMF's WEO, released twice yearly, provides macroeconomic forecasts and policy guidance influencing India's fiscal planning; India uses IMF's growth projections, inflation outlooks, and policy recommendations to calibrate domestic monetary and fiscal policy, though India maintains independence in navigating emerging market vulnerabilities distinct from the IMF's advanced-economy focus.",
     "AP_HC", "International_Current_Affairs"),

    (28080, "The Democracy Index which classifies countries into Full Democracy, Flawed Democracy, Hybrid Regime, and Authoritarian is published by:",
     "Freedom House", "Transparency International", "Economist Intelligence Unit (EIU)", "IEP",
     "C", "The Democracy Index is published by the EIU (Economist Intelligence Unit), the research arm of The Economist group. The EIU's Democracy Index, using 60 indicators across five categories (electoral process, civil liberties, functioning government, political participation, political culture), classifies countries into four categories. India's classification as 'Flawed Democracy' since 2010 reflects concerns about civil liberties, minority rights, and institutional independence; however, India's position in the flawed democracy category—rather than hybrid or authoritarian—validates India's democratic institutional framework, though it signals that India must strengthen implementation of democratic principles and protect vulnerable populations.",
     "AP_HC", "International_Current_Affairs"),

    # ── 2025-26 FRESHNESS GAP-FILL (added May 19, 2026) ──

    # EIU Democracy Index 2024 (released Feb 2025)
    (28081, "In the EIU Democracy Index 2024 (released Feb 2025), India's rank and classification were:",
     "39th — Full Democracy", "41st — Flawed Democracy", "53rd — Hybrid Regime", "108th — Authoritarian",
     "B", "India ranked 41st with a score of 7.29 in the EIU Democracy Index 2024, retaining its 'Flawed Democracy' classification since 2010. This consistent flawed democracy rating reflects international concerns about institutional independence, civil liberties, and minority rights protections; however, India's presence in the flawed rather than authoritarian category reflects functioning electoral systems and constitutional frameworks. India's objective of advancing to 'full democracy' requires strengthening judicial independence, expanding media freedom, protecting religious minorities, and ensuring equal implementation of laws across all populations.",
     "AP_HC", "International_Current_Affairs"),

    # Henley Passport Index 2025
    (28082, "Which country topped the Henley Passport Index 2025?",
     "Japan", "Germany", "Singapore", "Switzerland",
     "C", "Singapore topped the Henley Passport Index 2025 with visa-free access to 193 destinations out of 227 globally. The Henley Passport Index, measuring visa-free travel access, reflects economic integration and diplomatic relationships. India's lower ranking (85th with 57 destinations) constrains business mobility, tourism, and emigration options; India's diplomatic engagement and international standing are partially reflected in passport strength, making visa reciprocity negotiations and bilateral travel agreements diplomatic priorities for improving India's soft power and citizen mobility.",
     "AP_HC", "International_Current_Affairs"),

    (28083, "India's rank in the Henley Passport Index 2025 (Q4) was:",
     "59th", "77th", "85th", "97th",
     "C", "India slipped to 85th in the Henley Passport Index 2025 (Q4, Oct 2025), sharing the position with Mauritania and offering visa-free access to 57 countries. India had briefly improved to 77th in Q2 2025 before the Q4 decline. This volatility reflects changing visa policies globally, visa reciprocity agreements, and occasional country withdrawals of visa-free access. India's relatively low passport strength, while reflecting its developing economy status, constrains its citizens' international mobility and reflects India's lower diplomatic clout relative to developed economies; strengthening passport strength requires improving bilateral relations and economic competitiveness.",
     "AP_HC", "International_Current_Affairs"),

    # Global Peace Index 2025
    (28084, "India's rank in the Global Peace Index 2025 published by IEP was:",
     "104th", "115th", "126th", "139th",
     "B", "India ranked 115 out of 163 countries in the Global Peace Index 2025, improving by 1 rank from 116 in 2024. Iceland topped for the 18th consecutive year, followed by Ireland and New Zealand. India's steady GPI ranking (~115 for 5+ years) reflects persistent internal security challenges (terrorism, communal violence, property crime) and regional tensions with Pakistan and China, but also institutional improvements in conflict management. India's GPI improvement trajectory validates counterinsurgency programs, community policing initiatives, and conflict prevention investments; further advancement requires addressing root causes of violence including poverty, unemployment, and grievance redressal mechanisms.",
     "AP_HC", "International_Current_Affairs"),

    # World Happiness Report 2025 — India rank
    (28085, "India's rank in the World Happiness Report 2025 was:",
     "98th", "108th", "118th", "126th",
     "C", "India ranked 118 out of 147 countries in the World Happiness Report 2025 (score 4.389), up from 126 in 2024 (8-rank improvement). India still lagged behind Nepal (92) and Pakistan (109), indicating that India's rapid GDP growth is not translating into proportional increases in subjective well-being. India's relative underperformance on happiness—compared to peer income levels—reflects high inequality, limited social safety nets, and perceptions of limited personal freedom. India's development strategy increasingly must focus on well-being-augmenting investments (health, education, social protection) beyond income growth.",
     "AP_HC", "International_Current_Affairs"),

    # World Happiness Report 2025 — Top 3
    (28086, "The top three countries in the World Happiness Report 2025 were:",
     "Finland, Iceland, Sweden", "Finland, Denmark, Iceland", "Norway, Finland, Denmark", "Denmark, Finland, Switzerland",
     "B", "World Happiness Report 2025: (1) Finland (8th consecutive year, score 7.741); (2) Denmark (7.604); (3) Iceland (7.525). Scores based on GDP per capita, social support, healthy life expectancy, freedom, generosity, and perceptions of corruption. The Nordic dominance reflects not just high incomes but strong social cohesion, universal healthcare, work-life balance, low inequality, and institutional trust. India's bottom quartile happiness performance reflects the challenge of scaling well-being improvements alongside poverty reduction—a problem Nordic nations essentially solved before becoming wealthy.",
     "AP_HC", "International_Current_Affairs"),

    # SDG Index 2025 score
    (28087, "India's score in the UN Sustainable Development Report (SDG Index) 2025, in which it ranked 99th, was approximately:",
     "57", "62", "67", "74",
     "C", "India scored 67 in the SDG Index 2025 published by UN SDSN, ranking 99/167—the first time India entered the global top 100 (up from 109 in 2024 and 120 in 2021), representing a 21-position climb in 4 years. This acceleration reflects India's focused push on poverty reduction, health expansion, and renewable energy; however, India's score of 67 remains 33 points below the 100-point SDG achievement threshold, requiring accelerated progress on all 17 goals through 2030 to meet India's SDG commitments and align with India's development vision statements.",
     "AP_HC", "International_Current_Affairs"),

    # SIPRI 2025 — India warheads
    (28088, "According to SIPRI Yearbook 2025, at the start of 2025 the total global nuclear warhead stockpile (across 9 nuclear states) was approximately:",
     "9,500", "12,241", "15,800", "19,200",
     "B", "SIPRI Yearbook 2025 estimated approximately 12,241 nuclear warheads across the 9 nuclear-armed states (USA, Russia, UK, France, China, India, Pakistan, North Korea, Israel), of which 9,614 were considered potentially operationally available. India and Pakistan's combined 420+ warheads represent a regional security dynamic; India's no-first-use doctrine, while providing strategic stability rhetoric, reflects India's commitment to responsible nuclear stewardship and differentiates India's posture from Pakistan and China, supporting India's diplomatic narrative on nuclear responsibility.",
     "AP_HC", "International_Current_Affairs"),

    # SIPRI 2025 — India and China
    (28089, "According to SIPRI Yearbook 2025, India:",
     "Reduced its arsenal in 2024", "Slightly expanded its arsenal in 2024 and is developing canisterised MIRV-capable missiles", "Joined the NPT", "Achieved nuclear parity with China",
     "B", "SIPRI Yearbook 2025 noted India slightly expanded its nuclear arsenal in 2024 and is developing 'canisterised' (road-mobile) missiles potentially capable of carrying MIRVs (multiple independently-targeted warheads). India's arsenal expansion, while modest, reflects strategic imperatives from China's larger nuclear modernization (estimated 400-500 warheads by 2030) and Pakistan's tactical nuclear development. India's MIRV development, while challenging for arms control dialogues, represents India's strategic determination to maintain credible deterrence against potential adversaries.",
     "AP_HC", "International_Current_Affairs"),

    # UNHCR Mid-Year Trends 2025
    (28090, "According to UNHCR Mid-Year Trends 2025, the number of forcibly displaced people at end-June 2025 was:",
     "97.3 million — first decline in a decade", "110.4 million — slight rise", "117.3 million — first decline in a decade", "131.8 million — record high",
     "C", "UNHCR Mid-Year Trends 2025 reported 117.3 million forcibly displaced at end-June 2025—a decline of 5.9 million (~5%) from end-2024, the first decline in over a decade, driven by returns to Afghanistan, DRC, Sudan and Syria. This reversal reflects political settlements (Syria normalization, Afghanistan Taliban governance stabilization), and improved DRC security. India monitors displacement trends in the Indian Ocean region, particularly Afghanistan, Myanmar, and Bangladesh, to anticipate refugee pressures and plan humanitarian and border management responses for protecting vulnerable populations while securing India's borders.",
     "AP_HC", "International_Current_Affairs"),

    # UNEP Emissions Gap 2025
    (28091, "The UNEP Emissions Gap Report 2025 (released Nov 2025) projected global temperature rise this century, under full implementation of current NDCs, at:",
     "1.5°C", "1.8–2.0°C", "2.3–2.5°C", "3.1–3.5°C",
     "C", "UNEP Emissions Gap Report 2025 projected 2.3–2.5°C warming under full NDC implementation, and up to 2.8°C under current policies (improved from 3.1°C in 2024 report). This improvement reflects accelerated renewable capacity additions, improved emissions tracking, and strengthened climate pledges. India's NDC commits to 45% carbon intensity reduction by 2030; however, UNEP's projections suggest that global warming will likely exceed 1.5°C, making India's climate adaptation—monsoon management, coastal protection, agricultural resilience—as critical as emissions reduction for India's development security.",
     "AP_HC", "International_Current_Affairs"),

    (28092, "According to UNEP Emissions Gap Report 2025, to align with the 1.5°C pathway, global emissions must fall by what percentage by 2035 (vs 2019 levels)?",
     "25%", "35%", "55%", "75%",
     "C", "UNEP Emissions Gap Report 2025: 55% reduction by 2035 (vs 2019) needed for 1.5°C; 35% reduction for 2°C pathway. This accelerated reduction schedule—compared to previous reports assuming 2030 timelines—reflects updated climate science and recognition that 1.5°C is slipping from reach. India's emissions reduction targets (45% carbon intensity by 2030) contribute to global mitigation, but India's per capita emissions remain ~60% below global average, reinforcing India's equity-based argument that developed nations must take deeper reductions proportional to historical responsibility.",
     "AP_HC", "International_Current_Affairs"),

    # WMO State of Global Climate
    (28093, "The WMO State of the Global Climate 2024 report (released March 2025) confirmed which milestone?",
     "2024 was the second-warmest year on record", "2024 was the first calendar year >1.5°C above pre-industrial levels (1.55°C)", "Global warming temporarily reversed", "Glacier melt slowed for the first time",
     "B", "WMO State of the Global Climate 2024 confirmed 2024 as the warmest year in the 175-year record at 1.55±0.13°C above 1850-1900 pre-industrial average—the first calendar year to exceed 1.5°C. This milestone, while symbolic rather than policy-binding (IPCC projections assess long-term trends), signals that India's exposure to climate impacts is accelerating. India faces critical vulnerabilities: monsoon disruption threatens agricultural productivity affecting 260+ million farmers; sea-level rise threatens coastal cities (Mumbai, Kolkata, Chennai); glacier melt threatens Himalayan water supplies for 1 billion people; intensifying heat waves threaten labor productivity.",
     "AP_HC", "International_Current_Affairs"),

    # FAO SOFI 2025
    (28094, "According to FAO SOFI 2025, how many people faced hunger globally in 2024?",
     "Approximately 512 million", "Approximately 673 million (8.2% of population)", "Approximately 828 million", "Approximately 1.1 billion",
     "B", "SOFI 2025 (FAO, IFAD, UNICEF, WFP, WHO) reported ~673 million people faced hunger in 2024 (8.2% of population), down from 8.5% in 2023. Hunger fell in Asia (including India) and Latin America but rose in Africa (>20%) and Western Asia. India's hunger reduction, while modest, reflects improved food grain distribution through PDS and nutritional programs; however, hidden hunger (micronutrient deficiency) affects 300+ million Indians, requiring complementary focus on diet diversity, fortification, and nutrition-sensitive agriculture to achieve comprehensive food security.",
     "AP_HC", "International_Current_Affairs"),

    (28095, "According to FAO SOFI 2025, by 2030 the number of chronically undernourished people is projected at ~512 million, with what share residing in Africa?",
     "About 25%", "About 40%", "About 60%", "About 80%",
     "C", "SOFI 2025 projected 512 million chronically undernourished by 2030, with nearly 60% residing in Africa. This concentration in Africa reflects conflict, climate vulnerability, and weak social protection systems. India, projected to reduce chronic malnutrition below 5% of population by 2030 (from 15%+ in 2015), benefits from agricultural productivity gains, PDS scale-up, and nutrition programs. However, India's success depends on sustaining monsoon stability, protecting smallholder incomes, and ensuring food price stability—all vulnerable to climate variability and global grain market shocks.",
     "AP_HC", "International_Current_Affairs"),

    # Global MPI 2025
    (28096, "The Global Multidimensional Poverty Index (MPI) 2025 is published jointly by UNDP and which institution?",
     "World Bank", "OPHI (Oxford Poverty and Human Development Initiative)", "FAO", "ILO",
     "B", "The Global MPI 2025 is published jointly by UNDP and OPHI (Oxford Poverty and Human Development Initiative). The 2025 edition was titled 'Overlapping Hardships: Poverty and Climate Hazards.' The MPI measures poverty across 10 dimensions (health, education, living standards) using 31 indicators, providing a multidimensional picture beyond income poverty. India's MPI focus aligns with UNDP's emphasis on overlapping deprivations—recognizing that the poorest often face simultaneous health, education, and asset poverty requiring integrated interventions rather than siloed programs.",
     "AP_HC", "International_Current_Affairs"),

    (28097, "According to Global MPI 2025, the percentage of India's population in multidimensional poverty (per 2019-21 data) was approximately:",
     "8.9%", "16.4%", "24.7%", "35.5%",
     "B", "Global MPI 2025 reported 16.4% of India's population (~235.7 million people in 2023) lived in multidimensional poverty, down from 55.1% in 2005-06—a 38-percentage-point reduction in 17 years. An additional 18.7% are vulnerable to multidimensional poverty. This rapid decline validates India's poverty reduction strategy combining agricultural growth, social transfers (MGNREGA, pensions), education expansion, and health access; however, the persistence of 235 million multidimensionally poor and vulnerable 270+ million indicates that India's development path, while progress-oriented, requires sustained multi-sectoral intervention to reach the poorest populations.",
     "AP_HC", "International_Current_Affairs"),

    # B-READY 2024
    (28098, "The first edition of the World Bank's Business Ready (B-READY) report was released in:",
     "2022", "2023", "2024", "2026",
     "C", "The first edition of B-READY was released in October 2024 by the World Bank, covering 50 economies (planned to expand to 180 by 2026, including India). It replaces the discontinued Ease of Doing Business report. B-READY's three-pillar approach (Regulatory Framework, Public Services, Operational Efficiency) reflects a more holistic assessment of business ecosystems; India's opportunities under B-READY include showcasing digital governance advances (GST, e-portal modernization), reduced regulatory delays through single-window clearances, and infrastructure improvements that may yield higher rankings than under the cost-focused Ease of Doing Business metrics.",
     "AP_HC", "International_Current_Affairs"),

    (28099, "The B-READY report assesses economies across how many pillars?",
     "Three (Regulatory Framework, Public Services, Operational Efficiency)", "Five economic pillars", "Seven governance pillars", "Ten business pillars",
     "A", "B-READY is built on three pillars: (i) Regulatory Framework, (ii) Public Services, and (iii) Operational Efficiency, spanning 10 topics covering a firm's complete life cycle (starting, operating, trading, hiring, paying taxes, resolving disputes). This life-cycle approach captures regulatory burden throughout business operations, aligning with India's objective to create a business-friendly ecosystem beyond startup registration. India's B-READY assessment will reveal gaps in contract enforcement, labor regulations, environmental compliance, and tax administration—areas requiring targeted reform for improving India's investment competitiveness.",
     "AP_HC", "International_Current_Affairs"),

    # CCPI 2026 freshness
    (28100, "In the Climate Change Performance Index 2026 (released Nov 2025), India:",
     "Slipped from rank 10 (CCPI 2025) to rank 23, moving from 'high' to 'medium' performers", "Improved from rank 10 to rank 4", "Retained rank 10", "Was excluded from the index",
     "A", "CCPI 2026 (released Nov 2025 at COP30) showed India slipping from rank 10 in CCPI 2025 to rank 23, moving from 'high performers' to 'medium performers.' This 13-rank decline reflects slower renewable energy deployment relative to emissions growth, slowing coal phase-out due to energy demand, and inadequate sectoral emissions reductions in transport and industry. The downslide signals that India's climate ambitions require acceleration; India's strategy of expanding renewable capacity while managing energy access and coal dependence for baseload power faces tightening evaluation by CCPI frameworks prioritizing decarbonization pace.",
     "AP_HC", "International_Current_Affairs"),

    # India SDG Index neighbours
    (28101, "In the UN SDG Index 2025, where India ranked 99th, which neighbour ranked highest in South Asia?",
     "Bangladesh", "Pakistan", "Bhutan", "Nepal",
     "C", "SDG Index 2025 South Asia ranks: Bhutan (74) was highest among India's neighbours, followed by Nepal (85), India (99), Bangladesh (114), and Pakistan (140). China stood at 49. Bhutan's higher rank, despite lower GDP, reflects strategic focus on Gross National Happiness and environmental protection (60% forest cover, net carbon negative); India, with greater resources but larger population and poverty concentration, faces greater implementation challenges. India's regional leadership position despite trailing Bhutan validates India's development scale achievements, though India must accelerate environmental and inequality-focused SDGs to match Bhutan's trajectory.",
     "AP_HC", "International_Current_Affairs"),

    # GII 2025 cluster
    (28102, "Which Indian city ranked highest among Indian innovation clusters in the WIPO GII 2025?",
     "Mumbai (46)", "Delhi (26)", "Bengaluru (21)", "Chennai (84)",
     "C", "GII 2025 listed Bengaluru at rank 21—the highest among Indian innovation clusters—followed by Delhi (26), Mumbai (46) and Chennai (84). India has 4 clusters in the global top 100. Bengaluru's leadership reflects its IT services concentration, startup ecosystem density, and talent density; however, Bengaluru's higher global ranking than India's country rank (38) highlights that innovation is geographically concentrated. India's national innovation strategy requires expanding innovation ecosystems beyond metros to Tier-2/3 cities through technology incubators, R&D parks, and academic-industry collaboration hubs to democratize innovation and distribute development benefits.",
     "AP_HC", "International_Current_Affairs"),

    # CCPI top performers concept
    (28103, "Which country ranked 4th (the effective top) in the Climate Change Performance Index 2026?",
     "Denmark", "Sweden", "Morocco", "United Kingdom",
     "A", "CCPI 2026 (released Nov 2025) retained Denmark at rank 4 (the effective top, since positions 1-3 are conventionally left empty). The UK and Morocco followed in the top tier. Denmark's sustained leadership reflects complete transition to 80%+ wind-powered electricity, carbon pricing, and continuous emissions reduction across all sectors since the 1990s—a 30+ year decarbonization journey. India's much shorter climate action trajectory (accelerated only post-2015), while progressing rapidly on renewable capacity, lacks the sectoral depth and institutional consistency of Denmark's model; India's path requires decade-long commitment to sustained decarbonization across energy, transport, and industrial sectors.",
     "AP_HC", "International_Current_Affairs"),

    # WMO 2025 follow-up
    (28104, "WMO has stated that 2025 is likely to be:",
     "The coldest year of the past decade", "Among the warmest two or three years on record", "Below the 1.5°C threshold", "Tied exactly with 2024",
     "B", "WMO confirmed in late 2025 that 2025 is set to be the second or third warmest year on record, continuing the exceptionally high warming trend after 2024 (the first year >1.5°C). Back-to-back record warm years signal that global warming is accelerating rather than stabilizing; for India, this trajectory means increasingly frequent extreme weather events (heat waves, floods, droughts) requiring intensified climate adaptation. India's National Action Plan on Climate Change Adaptation must shift from mainstreaming to crisis mode—scaling water security, drought-resistant agriculture, flood management, heat stress protocols, and early warning systems to protect vulnerable populations from accelerating climate impacts.",
     "AP_HC", "International_Current_Affairs"),

    # GRFC 2025 — Sudan famine
    (28105, "The Global Report on Food Crises (GRFC) 2025 identified which country as having the world's worst current famine and largest displacement crisis?",
     "Yemen", "Afghanistan", "Sudan", "Ethiopia",
     "C", "GRFC 2025 (GNAFC + FSIN) and UNHCR Global Trends 2024 both identified Sudan as the world's largest displacement and food crisis—with confirmed famine conditions and 14.3 million displaced (6+ million IDPs, 5+ million cross-border refugees). Sudan's humanitarian catastrophe reflects rapid military conflict escalation (2023-2025), destroyed food systems, and humanitarian access restrictions. India's response—humanitarian aid, UNSC engagement, refugee absorption from the region—demonstrates commitment to humanitarian responsibility; however, Sudan's scale and duration highlight the limits of humanitarian aid without conflict resolution, reinforcing India's diplomatic push for ceasefire negotiations and conflict prevention mechanisms.",
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
