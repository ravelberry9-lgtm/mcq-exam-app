"""
Seed: Science, Space & Technology — Current Affairs 2024-2026
IDs: 26001–26130 (original 26001-26080 + freshness gap-fill 26081-26130)
Folder: AP_HC
Topic: National_Current_Affairs
Cross-checked: GKToday Science & Technology MCQs, ISRO, NASA, PIB, WebSearch (May 2026)

Freshness gap-fill (26081-26130) added May 19, 2026 — covers:
  - NASA Artemis-2 (Apr 2-11, 2026, 252,760 mi record)
  - ISRO BlueBird Block-2 / LVM3-M6 (Dec 24, 2025, 100th SHAR launch)
  - NavIC-16 / IRNSS-1K (PSLV-C58 Jan 2026)
  - Bharatiya Antariksh Station (BAS, 5 modules, 2028-35)
  - Chandrayaan-4 sample return + LUPEX
  - SpaceX Starship IFT-9 to IFT-12 (2025-26)
  - IBM Quantum System Two Heron R2 (156-qubit, Amaravati AQCC)
  - Nobel Physics 2025 (Clarke/Devoret/Martinis — macroscopic quantum tunnelling)
  - Nobel Chemistry 2025 (Kitagawa/Robson/Yaghi — MOFs)
  - Nobel Medicine 2025 (Brunkow/Ramsdell/Sakaguchi — peripheral immune tolerance)
  - OpenAI GPT-5 (Aug 2025) + Gemini 3.0 + DeepSeek R1 + Claude Opus 4
  - Mission Mausam (Sep 2024); CRISPR Casgevy approvals
  - Apple Vision Pro 2, Meta Quest 4, AI agents
  - CERN HL-LHC

NOTE: seed() runs DELETE+INSERT to force-refresh stale data.
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


def seed():
    conn = get_conn()
    if USE_POSTGRES:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    else:
        cur = conn.cursor()

    # Force-refresh: delete old and re-insert with updated 2025-26 data
    cur.execute("DELETE FROM questions WHERE id >= 26001 AND id <= 26130")
    conn.commit()

    ph = '%s' if USE_POSTGRES else '?'
    questions = [
        # --- ISRO ---
        {
            "id": 26001,
            "question_text": "SpaDeX, ISRO's technology demonstration mission, is designed to validate which space capability?",
            "option_a": "Interplanetary travel",
            "option_b": "Docking and undocking of small satellites in Low Earth Orbit",
            "option_c": "Solar panel deployment on the Moon",
            "option_d": "Communication between lunar rover and Earth",
            "correct_answer": "B",
            "explanation": "SpaDeX (Space Docking Experiment) is ISRO's technology demonstration mission to validate the ability to dock and undock small satellites in low-Earth orbit (LEO). It uses two satellites weighing approximately 220 kg each launched via PSLV on December 30, 2024. Strategic significance for India: Docking capability is critical for (1) Gaganyaan crewed missions (docking crewed orbital module with service module), (2) Bharatiya Antariksh Station (BAS) assembly and resupply (2028-35), (3) independent space station operations (reducing reliance on Russian Soyuz or Chinese Shenzhou assistance). Mastering docking technology establishes India as a spacefaring nation capable of autonomous human spaceflight, positioning India as the 4th nation with crewed capability (after US, Russia, China). India's docking success supports India's vision of independent space exploration and commercial space partnerships with private launch companies (Agnikul, Skyroot). For India's geopolitical positioning, demonstrating autonomous docking capability strengthens India's claim to UN Security Council permanent membership and validates India as a technology leader in the Global South.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26002,
            "question_text": "Aditya-L1, India's first space-based solar mission, was stationed at which Lagrange point?",
            "option_a": "L2",
            "option_b": "L3",
            "option_c": "L1",
            "option_d": "L4",
            "correct_answer": "C",
            "explanation": "Aditya-L1 was stationed at the Lagrange point L1, approximately 1.5 million kilometres from Earth (towards the Sun). From this position, the satellite can continuously observe the Sun without any eclipses, providing uninterrupted solar data critical for space weather prediction. Its SUIT (Solar Ultraviolet Imaging Telescope) instrument observed a powerful solar flare and a rare plasma ejection, contributing to India's growing expertise in solar physics. Strategic significance for India: Aditya-L1's L1 positioning makes it India's primary space weather monitoring platform — coordinating with NASA's Parker Solar Probe and SOHO mission provides India independent capability to forecast solar storms affecting India's power grid (200+ GW peak load), telecommunications, financial systems, and GPS/NavIC navigation infrastructure. The satellite's long-term solar data generation supports India's transition to renewable energy (500 GW solar target by 2030) by providing accurate solar irradiance predictions for grid management. India's mastery of L1 orbital mechanics positions ISRO as capable of autonomous deep-space missions and future Mars/Venus orbital missions.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26003,
            "question_text": "NISAR, launched on July 30, 2025, is the world's first dual-frequency radar imaging satellite. It is a joint mission of which two space agencies?",
            "option_a": "ESA and JAXA",
            "option_b": "NASA and ISRO",
            "option_c": "ISRO and Roscosmos",
            "option_d": "NASA and ESA",
            "correct_answer": "B",
            "explanation": "NISAR (NASA-ISRO Synthetic Aperture Radar) is the first joint Earth observation mission between NASA and ISRO. It was launched on July 30, 2025 using ISRO's GSLV-F16 into a sun-synchronous polar orbit at 747 km altitude. Strategic applications for India: (1) Disaster management — real-time monitoring of earthquakes (Himalayan seismic zones, Assam), tsunamis (Indian Ocean early warning), landslides in monsoon regions, saving 1000s of lives through early warning; (2) Agricultural monitoring — tracking crop health across 150+ million Indian farms, optimizing irrigation in 60% water-stressed districts, improving yields; (3) Forest conservation — monitoring 700M hectares of India's forests for deforestation, supporting India's Net-Zero 2070 goal and 450 GW renewable energy infrastructure development, (4) Groundwater mapping — India's aquifers depleting at 2 billion tons/year; NISAR's subsurface water detection supports irrigation planning and prevents agricultural crisis, (5) Coastal zone monitoring — supports Make in Sea maritime development, monitors fishing zones, supports India's 7,500 km coastline development, (6) Urban planning — monitors urban sprawl in Bangalore, Hyderabad, tier-2 cities, supports sustainable development. NISAR's 3-day global revisit cycle (via NASA's twin NISAR being planned) is superior to individual national systems (Sentinel-1, Radarsat). For India's development, NISAR represents India's transition from satellite-user to satellite-provider nation, leveraging US technology partnership while retaining data access for India's strategic autonomy.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26004,
            "question_text": "NISAR uses which two radar frequency bands, making it the world's first dual-frequency SAR satellite?",
            "option_a": "X-band and C-band",
            "option_b": "K-band and Ka-band",
            "option_c": "L-band and S-band",
            "option_d": "P-band and UHF-band",
            "correct_answer": "C",
            "explanation": "NISAR uses both L-band and S-band radar systems, making it the world's first dual-frequency Synthetic Aperture Radar (SAR) imaging satellite. L-band was contributed by NASA and S-band by ISRO. It studies Earth's surface changes related to earthquakes, landslides, glaciers, forests, and agriculture. Strategic significance for India: NISAR's dual-band capability provides India with independent Earth observation for: (1) Disaster management — real-time monitoring of earthquakes (Himalayan seismic zones), tsunamis (Indian Ocean), and landslides in Northeast states, (2) Agricultural monitoring — tracking crop health in 60% water-stressed districts, optimizing irrigation in 140M+ farms, (3) Forest conservation — supporting India's Net-Zero 2070 goal by monitoring deforestation in the Western Ghats and Northeast, (4) Urban planning — tracking urban sprawl in Bangalore, Hyderabad, Pune, (5) Infrastructure — monitoring dam safety (Mahanadi, Godavari dams), bridge stability. Previously, India relied on foreign satellites for such data. NISAR's 3-day global revisit cycle and penetrating radar (through clouds/rain) provides superior capability for India's monsoon-dependent economy.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26005,
            "question_text": "Chandrayaan-3 made history by becoming the first mission to make a soft landing on which part of the Moon?",
            "option_a": "North Pole",
            "option_b": "Equatorial region",
            "option_c": "Farside (dark side)",
            "option_d": "South Pole",
            "correct_answer": "D",
            "explanation": "Chandrayaan-3 became the first mission in history to make a soft landing on the Moon's South Pole on August 23, 2023. India became the 4th country to soft-land on the Moon (after USSR, USA, China), a landmark achievement in India's space exploration roadmap. The South Pole was specifically targeted because it contains water ice in permanently shadowed craters — essential for supporting future lunar habitats and enabling India's long-term Bharatiya Antariksh Station (BAS) expansion plans. August 23 is now celebrated as National Space Day in India, commemorating this historic achievement. The Vikram lander and Pragyan rover conducted 14 days of successful surface operations, collecting soil samples and detecting water molecules. Strategic significance for India: Chandrayaan-3's South Pole landing positioned India as the world's foremost expert in polar lunar environments, differentiating India from Russia/China/USA (all focused on equatorial/near-side landing expertise). India's South Pole capability directly supports India's human lunar landing mission (Gaganyaan follow-on, targeted 2040s) and sustained lunar presence strategy. The mission's success elevated India's standing in international space exploration, attracting partnerships from Japan (LUPEX collaboration), ESA (Lunar science cooperation), and strengthening India's position as a technology leader in the Global South. For India's geopolitical strategy, Chandrayaan-3 demonstrated India's independent capability in deep-space exploration without reliance on Western or Chinese support, validating India's claim to technological sovereignty.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26006,
            "question_text": "With Chandrayaan-3's successful landing, India became which number country to achieve a soft landing on the Moon?",
            "option_a": "2nd",
            "option_b": "3rd",
            "option_c": "4th",
            "option_d": "5th",
            "correct_answer": "C",
            "explanation": "With Chandrayaan-3's successful landing on August 23, 2023, India became the 4th country to achieve a soft landing on the Moon, joining the exclusive club of the USA (Apollo missions, 1969-1972), USSR (Luna missions, 1966-1976), and China (Chang'e missions, 2013+). Critically, India achieved this distinction with a single-lander design (no separate orbiter-lander separation like Apollo), demonstrating India's innovative engineering efficiency. Moreover, it was the first ever landing on the lunar south pole — the most scientifically valuable location due to water ice resources and geological complexity. India's South Pole achievement surpassed all three preceding spacefaring nations in terms of exploration significance, positioning India as the leading South Polar lunar expert. Strategic implications for India: Becoming the 4th nation elevated India's diplomatic standing to the exclusive club of spacefaring powers with independent lunar capability. For India's UNSC permanent seat aspirations, the achievement provides strong evidence of India's technological leadership and capacity for complex international cooperation. India's soft-landing success also demonstrates India's capability in autonomous guidance systems, real-time navigation correction, and precision landing mechanics — skills directly applicable to Gaganyaan crewed lunar missions and future interplanetary exploration. The achievement strengthens India's bilateral partnerships with Japan (LUPEX), ESA, and US space agencies, multiplying India's scientific influence in the global space community.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26007,
            "question_text": "August 23 is celebrated as National Space Day in India to commemorate which event?",
            "option_a": "ISRO's founding",
            "option_b": "Launch of first Indian satellite Aryabhata",
            "option_c": "Chandrayaan-3's landing on Moon's South Pole",
            "option_d": "Aditya-L1's launch",
            "correct_answer": "C",
            "explanation": "August 23 is celebrated as National Space Day in India to commemorate Chandrayaan-3's historic landing on the Moon's South Pole on August 23, 2023. This was a landmark achievement making India the first country to land on the lunar south pole.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26008,
            "question_text": "ISRO is developing a LOX-methane engine for the Next Generation Launch Vehicle (NGLV). Which centre developed its spark torch igniter?",
            "option_a": "VSSC (Vikram Sarabhai Space Centre)",
            "option_b": "SAC (Space Applications Centre)",
            "option_c": "LPSC (Liquid Propulsion Systems Centre)",
            "option_d": "URSC (U R Rao Satellite Centre)",
            "correct_answer": "C",
            "explanation": "ISRO's Liquid Propulsion Systems Centre (LPSC) is developing a LOX-methane engine for the Next Generation Launch Vehicle (NGLV). LPSC also developed a spark torch igniter for higher ignition reliability and cleaner combustion, which was successfully tested on March 3, 2025.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26009,
            "question_text": "India's Gaganyaan programme, if successful, will make India the how-many-th nation to independently send humans to space?",
            "option_a": "3rd",
            "option_b": "4th",
            "option_c": "5th",
            "option_d": "6th",
            "correct_answer": "B",
            "explanation": "Gaganyaan will make India the 4th nation to independently send humans to space, after USA, Russia (USSR), and China. Strategic significance: (1) Technological milestone — demonstrates India's advanced life-support, abort systems, and space capsule technology, reducing reliance on Russian Soyuz; (2) Geopolitical positioning — India joins the exclusive club of spacefaring nations with autonomous human capability, asserting India as a technology superpower in Global South and validating India's UNSC permanent seat aspirations; (3) Bengaluru Space Capsule — designed and manufactured entirely in India showcases indigenous tech capability and supports India's 'Make in India' manufacturing vision; (4) Timeline: Gaganyaan-G1 (uncrewed with Vyommitra humanoid, Dec 2025) → G2 (uncrewed, 2026) → G3 (crewed 2-person, 2027) → expansion missions (2028+); (5) Workforce development — Gaganyaan creates 50,000+ jobs in aerospace engineering, electronics, manufacturing, positioning India's tech workforce as global leaders; (6) Economic multiplier — India's space sector projected to grow $40B by 2040; Gaganyaan success attracts FDI, private space companies, technology partnerships with US/EU/Japan. Success positions India as space superpower in Global South, strengthens India's QUAD positioning against China's space dominance, and validates India's scientific and technological sovereignty.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26010,
            "question_text": "ISRO inaugurated the 'Shri S. Ramakrishnan Centre of Excellence in Fluid and Thermal Science Research' at which institute in March 2025?",
            "option_a": "IIT Kanpur",
            "option_b": "IIT Bombay",
            "option_c": "IIT Madras",
            "option_d": "IIT Delhi",
            "correct_answer": "C",
            "explanation": "ISRO Chairman V. Narayanan inaugurated the 'Shri S. Ramakrishnan Centre of Excellence in Fluid and Thermal Science Research' at IIT Madras on March 17, 2025 — a Rs 50 crore ($6M+) facility. The centre focuses on spacecraft and launch vehicle thermal management for future lunar, Mars, and deep-space missions. Strategic significance for India: This centre represents India's transition from hardware-centric space programs (launching satellites) to technology-building (indigenous thermal systems, advanced propulsion science). Thermal management is critical for: (1) Gaganyaan crewed vehicles (life support systems maintaining 18-24°C in space vacuum, crew compartment heating/cooling for astronaut comfort), (2) Bharatiya Antariksh Station (BAS, 2028-2035) — needs advanced thermal regulation maintaining habitat stability in 150-degree temperature extremes, (3) High-energy launch vehicles (NGLV) burning exotic LOX-methane fuel (requiring cryogenic thermal management), (4) Planetary missions — India's Mars Orbiter-3 and lunar lander missions need thermal protection during atmospheric entry and surface operations. IIT Madras's leading expertise in fluid dynamics, heat transfer, and computational thermal analysis accelerates India's indigenous thermal system design, eliminating dependence on Russian Energia or European contractor imports. This centre catalyzes collaboration between academia-ISRO-industry: research outputs directly transition to ISRO missions and commercial space companies. For India's space industry, leading thermal science capability attracts commercial space startups (Skyroot Aerospace, Agnikul Cosmos, Relativity Space) who need world-class indigenous expertise to compete globally in launch services. The centre also positions India as a space technology exporter — India can now offer thermal design services to Southeast Asian and African space agencies, generating revenue and soft power.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- NASA Missions ---
        {
            "id": 26011,
            "question_text": "NASA's SPHEREx mission, launched on March 12, 2025, will primarily study how many galaxies?",
            "option_a": "100 million",
            "option_b": "250 million",
            "option_c": "350 million",
            "option_d": "450 million",
            "correct_answer": "D",
            "explanation": "NASA's SPHEREx mission was launched on March 12, 2025 from Vandenberg Space Force Base. It will study 450 million galaxies and 100 million stars, creating a 3D map of the sky to understand the history of the universe. It orbits in a sun-synchronous orbit at 650 km above Earth. Strategic significance for India: SPHEREx's sky map data is publicly available to the international scientific community, including Indian astronomers. India's Astrophysical Research Institute (IUCAA Pune), Indian Institute of Astrophysics (Bengaluru), and Tata Institute of Fundamental Research (TIFR Mumbai) will access this data to study: (1) Galaxy formation and evolution (linking to Indian research on cosmic reionization), (2) Dark matter and dark energy (fundamental physics relevant to India's cosmology research), (3) Large-scale structure of the universe (computational astrophysics where India has strong groups). For India's space science, SPHEREx data democratizes access to next-generation astrophysical datasets, leveling the playing field between Indian and Western researchers. India's own space missions (Aditya-L1 solar mission, Chandrayaan series) contribute complementary data, positioning India as a partner in global astrophysics rather than just a data consumer. This supports India's long-term vision of an independent space science capability and attracts international collaborations for Indian institutions.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26012,
            "question_text": "NASA's PUNCH mission, launched in March 2025, consists of how many satellites to study solar phenomena?",
            "option_a": "2",
            "option_b": "3",
            "option_c": "4",
            "option_d": "6",
            "correct_answer": "C",
            "explanation": "NASA's PUNCH (Polarimeter to Unify the Corona and Heliosphere) mission was launched on March 12, 2025, alongside SPHEREx, on a single Falcon 9 rocket. It consists of four small satellites that form a constellation to study the solar corona, solar winds, and coronal mass ejections (CMEs) to improve space weather predictions. Strategic significance for India: PUNCH data directly complements India's Aditya-L1 solar mission at L1 — together they provide continuous solar monitoring from multiple vantage points. Space weather events can disrupt India's power grids (particularly HVDC transmission corridors carrying renewable energy from solar farms), telecommunications, satellite navigation (GPS, NavIC), and financial systems. PUNCH's 3D multi-angle observations improve forecasting of solar storms that impact the $2+ trillion global digital economy. India's Aditya-L1 is an independent asset that, combined with international data, strengthens India's space weather resilience and enables indigenous forecasting without relying solely on US NOAA data.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26013,
            "question_text": "NASA launched SPHEREx and PUNCH on which type of commercial rocket in March 2025?",
            "option_a": "Atlas V",
            "option_b": "Falcon 9",
            "option_c": "Vulcan Centaur",
            "option_d": "Delta IV Heavy",
            "correct_answer": "B",
            "explanation": "NASA launched both the SPHEREx and PUNCH space missions together on March 12, 2025, from Vandenberg Space Force Base, California, using a SpaceX Falcon 9 rocket — demonstrating the cost-effectiveness and reliability of commercial launch services. Strategic context for India: SpaceX's Falcon 9 reusability (booster landing and reflight) has reduced US launch costs by ~60% compared to traditional expendable systems. ISRO's NGLV development, with its reusable booster stage, aims to achieve similar cost reduction from ~Rs 1,600 crore/launch to ~Rs 700-900 crore/launch once operational. The shift to commercial providers globally emphasizes India's need to strengthen ISRO's commercial arm (NSIL) and develop cost-competitive launch services to retain India's position in the growing commercial launch market (projected $10 billion+ by 2030). India's policy of technology transfer to startups (Agnikul, Skyroot) accelerates this transition.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26014,
            "question_text": "NASA's Europa Clipper mission is heading to which moon of which planet?",
            "option_a": "Titan of Saturn",
            "option_b": "Ganymede of Jupiter",
            "option_c": "Europa of Jupiter",
            "option_d": "Enceladus of Saturn",
            "correct_answer": "C",
            "explanation": "NASA's Europa Clipper mission is heading to Europa, one of Jupiter's moons. The spacecraft performed a Mars flyby in March 2025 and will perform an Earth flyby in December 2026, arriving at Europa in April 2030 to study its potential habitability. Europa's subsurface ocean contains more liquid water than Earth's oceans combined — a critical factor in the search for extraterrestrial life. Strategic significance for India: Europa Clipper represents the cutting-edge of astrobiology and deep-space exploration. India's contribution through scientific partnerships (Indian astronomical institutions collaborating with NASA) strengthens India's credentials in space science. ISRO's future Mars and lunar missions can leverage Europa Clipper data. Moreover, this demonstrates India's growing role in international space science consortiums — a pathway to collaborating with global space agencies on human-crewed deep-space missions beyond Gaganyaan (planned crewed Moon landing by 2040). India's space science achievements position Indian researchers and institutions as valued collaborators in humanity's search for extraterrestrial life.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26015,
            "question_text": "The ESA Biomass satellite mission, launched using Vega C rocket from French Guiana, primarily aims to do what?",
            "option_a": "Monitor ocean currents",
            "option_b": "Study urban air pollution",
            "option_c": "Map global forests and measure carbon levels",
            "option_d": "Track animal migration patterns",
            "correct_answer": "C",
            "explanation": "The ESA Biomass satellite is the 7th Earth Explorer satellite under ESA's climate and Earth systems programme. It will study global forests, measuring carbon levels and forest health to understand their role in the carbon cycle. It uses radar to create detailed 3D models of forest structures.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- IIT/IISc Innovations ---
        {
            "id": 26016,
            "question_text": "Which institute developed a framework to protect critical infrastructure (reinforced concrete panels) against ballistic missile threats?",
            "option_a": "IIT Roorkee",
            "option_b": "IIT Bombay",
            "option_c": "IIT Madras",
            "option_d": "IIT Ahmedabad",
            "correct_answer": "C",
            "explanation": "IIT Madras researchers developed a framework to enhance protection of critical infrastructure from ballistic missile threats. The framework helps designers improve the ballistic resistance of reinforced concrete (RC) panels. Findings were published in the journal Reliability Engineering & System Safety. Strategic significance for India: This research is critical for India's defense infrastructure in the context of Pakistan's ballistic missile arsenal (Shaheen, Ghauri series) and potential Chinese missile threats. Critical infrastructure includes: (1) Military installations — army bases, air force hangars, naval facilities, (2) Civilian infrastructure — nuclear power plants (Jaitapur, Kakrapar), dams (Hirakud, Bhakra), bridges (strategic national highway crossings), (3) Telecom/power grids. IIT Madras's framework helps Indian defense engineers and architects design hardened bunkers, command centers, and ammunition magazines to survive direct hits. With Pakistan's development of Nasr (short-range tactical nukes) and cruise missiles, India's civil defense and hardened infrastructure design has become critical. This research supports India's Defense Research and Development Organisation (DRDO) and Ministry of Defence in improving nuclear fallout shelters and critical facility protection.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26017,
            "question_text": "Which centre of IIT Bombay developed a high-efficiency tandem solar cell with nearly 30% power conversion efficiency?",
            "option_a": "Centre for Environmental Science and Engineering (CESE)",
            "option_b": "National Centre for Photovoltaic Research and Education (NCPRE)",
            "option_c": "Centre for Nano-science (CENS)",
            "option_d": "Advanced Centre for Research in Electronics (ACRE)",
            "correct_answer": "B",
            "explanation": "IIT Bombay's National Centre for Photovoltaic Research and Education (NCPRE) developed a high-efficiency tandem solar cell with nearly 30% power conversion efficiency, a major advancement for solar energy technology. Strategic significance for India: This breakthrough supports India's renewable energy ambitions — Net-Zero 2070 goal and 500 GW renewable capacity by 2030 (solar is 280+ GW target). The 30% efficiency tandem cell (combining perovskite and silicon) would dramatically reduce land requirements for India's solar farms. India currently leads the world in solar capacity additions but lags in efficiency-per-unit-area. NCPRE's advancement could enable: (1) Roof-top solar expansion for India's 150M+ buildings, reducing dependence on large-scale solar farms, (2) Cost reduction through higher per-panel output, accelerating solar adoption in rural India, (3) Export potential — India can license this technology to Southeast Asia, Africa, positioning India as a green technology hub. India's National Solar Mission targets 100 GW rooftop solar by 2027, and this technology directly supports that goal.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26018,
            "question_text": "India's first cancer genome database was launched by which institution to boost cancer research?",
            "option_a": "AIIMS New Delhi",
            "option_b": "IIT Bombay",
            "option_c": "IIT Madras",
            "option_d": "NIMHANS Bengaluru",
            "correct_answer": "C",
            "explanation": "IIT Madras launched India's first cancer genome database to boost cancer research across the country. This database catalogues genomic data on Indian cancer types, enabling more targeted cancer diagnosis and treatment research. Strategic significance for India: India reports 1.4+ million new cancer cases annually (2nd highest in Asia). The cancer genome database addresses a critical gap: most global oncology databases (TCGA, ICGC) are dominated by Western/East Asian genetic profiles, which don't represent Indian populations. Indian cancers have unique genetic signatures: (1) Betel nut-related oral cancers in Northeast/South (genetic mutations specific to Indian diet patterns), (2) High HPV-related cervical cancers (vaccine uptake challenges), (3) Breast cancer subtypes (triple-negative breast cancer higher in Indian women). IIT Madras's database enables: (1) Drug response prediction for Indian patients, (2) Precision medicine — tailoring treatments to Indian genetic backgrounds, (3) Early detection biomarkers, (4) Cost reduction in clinical trials through better patient stratification. This supports India's goal of reducing cancer mortality from 6% to 3% by 2030 and positions India as a leader in precision oncology in the Global South.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26019,
            "question_text": "AMRSense, an AI tool developed by IIIT-Delhi researchers, is designed to track and provide early insights on which healthcare challenge?",
            "option_a": "Cancer mutation patterns",
            "option_b": "Diabetes progression",
            "option_c": "Antimicrobial Resistance (AMR)",
            "option_d": "Mental health disorders",
            "correct_answer": "C",
            "explanation": "AMRSense is an AI-powered tool developed by IIIT-Delhi researchers. It analyzes hospital data to provide early insights on Antimicrobial Resistance (AMR) patterns. This is critical for combating the growing global threat of drug-resistant infections. Strategic significance for India: AMR is a critical public health crisis in India — the highest burden of AMR-related deaths globally (400,000+ deaths/year). Antibiotic overuse in Indian hospitals, agriculture (livestock farming), and unregulated pharmaceutical sales have created a 'superbug crisis'. AMRSense addresses this by: (1) Analyzing hospital antibiogram data (resistance patterns) in real-time across 100+ Indian hospitals, (2) Predicting which antibiotics will fail for specific infections, enabling better clinical decisions, (3) Tracking emergence of carbapenem-resistant Enterobacteriaceae (CRE), ESBL-producing organisms — leading causes of sepsis in India. For India, AMRSense supports: (1) ICMR's National Surveillance Programme on AMR, (2) Ministry of Health's focus on rational antibiotic use, (3) Rural health centers' decision-making where diagnostics are absent. WHO estimates India could lose $553 billion in cumulative economic losses by 2050 if AMR is not controlled — AMRSense helps India be a leader in combating this global threat.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26020,
            "question_text": "Indian Institute of Science (IISc) developed a bacteria-based technique to repair bricks for lunar habitats using which bacterium?",
            "option_a": "Bacillus subtilis",
            "option_b": "Sporosarcina pasteurii",
            "option_c": "Streptococcus lactis",
            "option_d": "Escherichia coli",
            "correct_answer": "B",
            "explanation": "Researchers at IISc developed a technique using the bacterium Sporosarcina pasteurii with guar gum to create bricks from lunar and Martian soil simulants (regolith). The bacterium converts urea and calcium into calcium carbonate crystals, binding soil particles. This eco-friendly method supports NASA's Artemis programme goal of permanent lunar settlements. Strategic significance for India: IISc's breakthrough positions India as a contributor to international space exploration. India's Chandrayaan-3 (first landing on Moon's South Pole, Aug 2023) demonstrated India's indigenous lunar capability, but Gaganyaan (crewed mission by 2027) and Bharatiya Antariksh Station (BAS, 2028-2035) require habitat construction technologies. IISc's bacteriogenic brick technology reduces the need to transport building materials from Earth (prohibitively expensive). This collaboration with NASA's Artemis programme gives India visibility in space architecture — a high-value field. For India's deep-space ambitions, this technology supports the Mars mission roadmap and potential India-Russia-China cooperation on lunar base construction post-2030. Guar gum sourced from India could become a 'space commodity' exported for space habitat construction.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26021,
            "question_text": "In IISc's bacteria-based lunar brick technique, what chemical process does Sporosarcina pasteurii perform?",
            "option_a": "Converts CO₂ into calcium oxide",
            "option_b": "Converts urea and calcium into calcium carbonate crystals",
            "option_c": "Splits water molecules into hydrogen and oxygen",
            "option_d": "Converts methane into carbon fiber composites",
            "correct_answer": "B",
            "explanation": "Sporosarcina pasteurii bacteria converts urea and calcium into calcium carbonate (CaCO₃) crystals, which bind lunar soil (regolith) particles together with guar gum, creating solid bricks. This biomineralization process is eco-friendly and avoids transporting heavy materials from Earth.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Disease Agents ---
        {
            "id": 26022,
            "question_text": "What is the causative agent of African Swine Fever (ASF), which resurged in Mizoram?",
            "option_a": "Fungus",
            "option_b": "Virus",
            "option_c": "Bacteria",
            "option_d": "Protozoa",
            "correct_answer": "B",
            "explanation": "The causative agent of African Swine Fever (ASF) is the African Swine Fever Virus (ASFV). ASF is a highly contagious and fatal viral disease affecting domestic and wild pigs but poses no risk to humans. There is currently no vaccine or treatment for ASF.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26023,
            "question_text": "African Swine Fever (ASF) is contagious and fatal among which animals, with no risk to humans?",
            "option_a": "Cattle",
            "option_b": "Pigs",
            "option_c": "Poultry",
            "option_d": "Sheep and goats",
            "correct_answer": "B",
            "explanation": "African Swine Fever (ASF) affects domestic and wild pigs and is highly contagious and fatal to them. However, it poses NO risk to humans. It first emerged in Mizoram in March 2021 and has since become endemic. There is no vaccine or treatment.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26024,
            "question_text": "River Blindness (Onchocerciasis), a WHO Neglected Tropical Disease, is caused by which type of agent?",
            "option_a": "Bacteria",
            "option_b": "Parasite",
            "option_c": "Virus",
            "option_d": "Fungus",
            "correct_answer": "B",
            "explanation": "River Blindness (Onchocerciasis) is caused by the parasitic worm Onchocerca volvulus and spreads through the bite of infected blackflies (genus Simulium) that breed near fast-flowing rivers. It causes severe skin itching, skin damage, and permanent blindness. WHO classifies it as a major Neglected Tropical Disease, especially in sub-Saharan Africa, Yemen, and Latin America.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26025,
            "question_text": "The Zoological Survey of India (ZSI) used DNA barcoding to identify blackfly species that spread which disease?",
            "option_a": "Malaria",
            "option_b": "Dengue",
            "option_c": "River Blindness",
            "option_d": "Filariasis",
            "correct_answer": "C",
            "explanation": "A study by the Zoological Survey of India (ZSI) used DNA barcoding to correctly identify blackfly species (genus Simulium) that spread River Blindness (Onchocerciasis). DNA barcoding involves using short DNA sequences to identify species.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26026,
            "question_text": "Multiple Sclerosis (MS), which affects 2.8 million people worldwide, occurs when the immune system attacks which organs?",
            "option_a": "Kidneys and liver",
            "option_b": "Lungs and heart",
            "option_c": "Brain and spinal cord",
            "option_d": "Large intestine and pancreas",
            "correct_answer": "C",
            "explanation": "Multiple Sclerosis (MS) is an autoimmune disorder that occurs when the immune system attacks the brain and spinal cord. It affects nearly 1 million people in the US and over 2.8 million worldwide. Recent studies show gut microbiome imbalance can predict MS severity. Strategic significance for India: MS affects 40,000+ people in India, with rising incidence in urban areas. India's tropical climate and diverse dietary patterns result in different MS prevalence (lower than Western countries, but rising with urbanization). Indian MS patients have unique microbiome profiles (higher exposure to tropical pathogens, different bacterial flora from Westernized populations). Understanding MS through the lens of Indian microbiome diversity enables: (1) Better diagnostic criteria for Indian patients (existing diagnostic thresholds may miss or over-diagnose Indian cases), (2) Prevention strategies — identifying protective bacterial species in rural Indian populations, (3) Probiotic/dietary interventions tailored to Indian patients. India's microbiome research at institutions (CCMB Hyderabad) is gaining global recognition. MS research in India supports the broader goal of 'reverse pharmacology' — understanding disease mechanisms from Indian populations and exporting treatments back to the Global North.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26027,
            "question_text": "Research on Multiple Sclerosis found that MS patients have a lower ratio of which gut bacteria compared to healthy individuals?",
            "option_a": "Blautia and Akkermansia",
            "option_b": "Bifidobacterium to Akkermansia ratio",
            "option_c": "Lactobacillus and Prevotella",
            "option_d": "Firmicutes and Bacteroides",
            "correct_answer": "B",
            "explanation": "Studies on Multiple Sclerosis found that MS patients have more Blautia and Akkermansia but lower Bifidobacterium and Prevotella in their gut. A lower Bifidobacterium-to-Akkermansia ratio is linked to worse disability. These findings may help improve MS diagnosis by focusing on gut microbiome health.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Space Concepts ---
        {
            "id": 26028,
            "question_text": "A Lagrange point is a position in space where what condition holds true?",
            "option_a": "Zero gravity exists",
            "option_b": "Gravitational forces of two large bodies and centrifugal force balance",
            "option_c": "Maximum solar radiation is received",
            "option_d": "A satellite can travel at light speed",
            "correct_answer": "B",
            "explanation": "A Lagrange point is a position in space where the gravitational forces of two large bodies (e.g., Earth and Sun) combined with the centrifugal force balance out, allowing a smaller object to maintain a stable orbit. Aditya-L1 is stationed at L1, approximately 1.5 million km from Earth towards the Sun.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26029,
            "question_text": "What is a Coronal Mass Ejection (CME), which NASA's PUNCH mission studies?",
            "option_a": "A massive burst of solar plasma and magnetic field from the Sun's corona",
            "option_b": "An asteroid impact on Mercury's corona",
            "option_c": "A rain of cosmic rays from outside the solar system",
            "option_d": "A nuclear fusion reaction in the Sun's core",
            "correct_answer": "A",
            "explanation": "A Coronal Mass Ejection (CME) is a massive burst of solar plasma (ionized gas) and magnetic field erupting from the Sun's corona at speeds up to 3,000 km/s. CMEs eject billions of tonnes of charged particles into space. When directed toward Earth, they interact with Earth's magnetosphere, causing geomagnetic storms that disrupt power grids, satellites, and communications. The largest CME (Carrington Event, 1859) would cause ~$2+ trillion in economic damage if it occurred today. NASA's PUNCH mission (4 satellites) studies solar corona, solar winds, and CMEs to improve space weather predictions critical for protecting infrastructure. Strategic significance for India: India's rapidly expanding power grid (handling peak loads of 200+ GW) is vulnerable to geomagnetic storms — a major CME could black out large regions for months. India's Aditya-L1 solar mission provides early warning data on solar activity; coupled with international datasets, this enables India's Space Weather Coordination Centre to issue timely alerts to power operators, railways, and telecom providers. Independent space weather prediction capability is strategic for a nation with 1.4 billion people and critical infrastructure.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26030,
            "question_text": "What is Lunar Regolith, which IISc used in its bacteria-based technique?",
            "option_a": "A type of radioactive material found on Moon",
            "option_b": "Loose soil and rock covering the Moon's surface",
            "option_c": "Solid ice deposits at Moon's south pole",
            "option_d": "A mineral unique to Moon's mantle",
            "correct_answer": "B",
            "explanation": "Lunar Regolith is loose, unconsolidated soil and fragmented rock covering the Moon's surface — composed of mineral grains, impact-generated glass, and micrometeorite-churned dust created by 3+ billion years of meteorite bombardment. It contains valuable minerals (olivine, anorthosite, ilmenite with iron oxides) and water ice in permanently shadowed craters. IISc used lunar and Martian soil simulants (regolith) in their bacteria-based technique with Sporosarcina pasteurii to create bricks for future lunar habitats under NASA's Artemis programme, which aims to establish permanent Moon settlements by 2030s. Strategic significance for India: Mastering regolith utilization is essential for India's crewed lunar missions (targeted post-2040). Using in-situ resources (regolith) to construct habitat bricks dramatically reduces payload from Earth — critical since launching from Earth costs ~$10,000-50,000 per kilogram to the lunar surface. IISc's biotechnological approach (bacteria-based binding) is novel and positions India as an innovator in lunar engineering. This capability supports India's vision of establishing an independent lunar research station (as part of BAS evolution) and enables India to serve as a technology provider for international lunar base collaborations in the 2040s+.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Sonic Weapons ---
        {
            "id": 26031,
            "question_text": "What is the primary function of sonic weapons (acoustic weapons)?",
            "option_a": "To deliver loud, painful sounds over long distances",
            "option_b": "To enhance communication between soldiers",
            "option_c": "To generate electromagnetic pulses",
            "option_d": "To detect enemy submarines",
            "correct_answer": "A",
            "explanation": "Sonic weapons (acoustic weapons) emit high-intensity sound waves (from infrasound <20 Hz to ultrasound >20 kHz) to disrupt, disorient, or incapacitate human targets at distances up to 300+ metres. They operate through two mechanisms: (1) direct acoustic trauma causing hearing damage, disorientation, and internal organ injury (high frequencies), (2) psychological effects from infrasound inducing fear, anxiety, and nausea. The US military first deployed them in Iraq (2004) for crowd dispersal; Serbia used them against Belgrade protesters (2023-24). Strategic context for India: Pakistan's development of crowd-control sonic devices and their potential deployment in Kashmir counter-insurgency operations poses a concern. India's Central Armed Police Forces (CAPF) and state police lack specific non-lethal acoustic countermeasures. As a dual-use technology, sonic weapons blur lines between military, paramilitary, and law enforcement, raising human rights concerns. India's policy framework (Constitutional restrictions on torture) and medical preparedness for acoustic trauma victims require development.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26032,
            "question_text": "Serbia was accused of using sonic weapons to disperse protesters in which city?",
            "option_a": "Zagreb",
            "option_b": "Sarajevo",
            "option_c": "Belgrade",
            "option_d": "Podgorica",
            "correct_answer": "C",
            "explanation": "The Serbian government was accused of using sonic weapons (acoustic weapons) to disperse student and opposition protesters in Belgrade, Serbia's capital, during 2023-24 anti-government demonstrations. Eyewitnesses reported intense ear pain, disorientation, and hearing difficulties after exposure to concentrated sound beams. This incident marked the first documented deployment of sonic weapons in an EU-candidate country against civilian protesters, raising international concerns about the normalization of non-lethal acoustic weapons in law enforcement. The technology was originally developed for military use; the US deployed it in Iraq (2004) for perimeter defense and crowd control. Strategic context for India: India's police forces lack training on acoustic weapon effects and countermeasures. If acoustic weapons proliferate to South Asia (Pakistan, Bangladesh), India's security forces in urban areas (especially during mass protests, elections, refugee crises) will need protocols for identification and medical response to acoustic trauma.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- NGLV / Launch vehicles ---
        {
            "id": 26033,
            "question_text": "NGLV (Next Generation Launch Vehicle) being developed by ISRO will use which type of propellant engine?",
            "option_a": "Solid propellant",
            "option_b": "Hypergolic (N2O4/UDMH)",
            "option_c": "LOX-methane",
            "option_d": "Hydrogen peroxide/kerosene",
            "correct_answer": "C",
            "explanation": "ISRO is developing a LOX-methane (Liquid Oxygen + methane) engine for the Next Generation Launch Vehicle (NGLV). LOX-methane offers significant advantages: (1) Cleaner exhaust (CO2 + H2O, zero hypergolic toxins), enabling green aerospace industry; (2) Reusability-friendly (cooler chamber temperature enabling 10+ engine reuses vs. PSLV's single-use solids), reducing per-flight costs; (3) Higher specific impulse (Isp ~350s vs. PSLV's solid motor at 240s), increasing payload capacity; (4) Methane availability (India's abundant natural gas reserves, cheaper than hydrogen), enabling indigenous fuel supply independence. NGLV architecture: fully reusable booster (lands via parachute + retrorockets for land recovery, no recovery vessels needed) + two expendable upper stages; designed to launch 10-12 tonnes to GTO (for commercial communications satellites) and 20+ tonnes to LEO (for constellation satellites, Bharatiya Antariksh Station resupply). Strategic significance: NGLV targets operational status by 2032-35, reducing launch costs from current Rs 1,600 crore to Rs 700-900 crore per flight — a 55% reduction that will triple India's commercial launch market share. This cost reduction directly accelerates: (1) Commercial satellite launches (competing with SpaceX's $60M Falcon 9 vs. ISRO's projected Rs 100 crore = $12M equivalent), (2) Frequent crewed launches for Gaganyaan-2 missions (2027+) and BAS resupply missions (2028+), (3) India's deep-space exploration cadence (Mars missions every 2 years, asteroid sample-return missions, Venus missions), (4) India's satellite constellation programs (OneWeb India, Bharat Constellation) requiring launch cost reduction. Methane engines are the global standard (SpaceX Raptor-3 for Starship, Blue Origin BE-4 for Atlas, China's Space Force); India's indigenous mastery of LOX-methane technology positions ISRO as a globally competitive launch provider while establishing India's supply chain independence from foreign engine imports. For India's tech sovereignty and economic growth, NGLV is strategic: it enables India to capture $200B+ global commercial launch market by 2040.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26034,
            "question_text": "PSLV-C61 was launched by ISRO in May 2025 carrying which satellite?",
            "option_a": "NovaSAR-1",
            "option_b": "EOS-09",
            "option_c": "Cartosat-3",
            "option_d": "GISAT-2",
            "correct_answer": "B",
            "explanation": "PSLV-C61/EOS-09 (Earth Observation Satellite-09) was launched by ISRO on May 18, 2025 from SDSC SHAR. EOS-09 is a multi-spectral optical remote sensing satellite with a 4-metre panchromatic and 16-metre multispectral imaging payload. It provides Earth observation data critical for agriculture (crop monitoring across 150+ million farms), forestry (deforestation tracking in Amazon-scale areas), disaster management (floods in monsoon season, earthquakes, landslides), and urban planning (sprawl monitoring in 1000+ cities). Strategic significance for India: The EOS constellation (EOS-01 through EOS-09) represents India's independent Earth observation capability — reducing reliance on foreign satellites (USA's Landsat, Europe's Copernicus). Data from EOS satellites supports: (1) National Disaster Management Authority (NDMA) for real-time flooding alerts, (2) Ministry of Agriculture for crop yield predictions enabling food security, (3) Climate monitoring for India's environmental goals, (4) Coastal zone management for maritime development. As India scales renewable energy (500 GW by 2030), EOS data tracks land use changes and monitors solar farm siting. With NISAR (launched July 2025), EOS satellites provide complementary optical and radar data, positioning India as self-reliant in civilian Earth observation.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- SPHEREx in detail ---
        {
            "id": 26035,
            "question_text": "SPHEREx satellite by NASA will create a 3D map of the sky by measuring what type of spectra?",
            "option_a": "X-ray spectra",
            "option_b": "Near-infrared spectra",
            "option_c": "Radio wave spectra",
            "option_d": "Gamma-ray spectra",
            "correct_answer": "B",
            "explanation": "SPHEREx (Spectro-Photometer for the History of the Universe, Epoch of Reionization and Ices Explorer) will measure near-infrared spectra (0.75-5 micrometers) of 450 million galaxies, creating a 3D map of the universe to understand: (1) Cosmic history and large-scale structure, (2) Reionization epoch when first stars lit up (300 million years after Big Bang), (3) Ices in star-forming regions and exoplanet systems. Near-infrared penetrates cosmic dust, revealing star formation hidden in visible light. SPHEREx entered a sun-synchronous orbit at 650 km altitude on March 12, 2025. Strategic significance for India: SPHEREx data (publicly available) will be analyzed by Indian astrophysicists at IUCAA Pune, IISER institutions, and IIT-run astronomical centers, advancing India's cosmology research. India's own Aditya-L1 mission demonstrates India's capability to build specialized space telescopes; future missions could target complementary wavelengths (UV, far-infrared) for a complete census of the universe. India's National Supercomputing Mission provides computing power for analyzing terabyte-scale datasets from SPHEREx and other missions — accelerating Indian researcher participation in global astrophysics. This democratization of space science data levels the playing field between wealthy Western institutions and Indian universities.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Chandrayaan details ---
        {
            "id": 26036,
            "question_text": "What are the names of Chandrayaan-3's lander and rover?",
            "option_a": "Ashwin (lander) and Arjun (rover)",
            "option_b": "Vikram (lander) and Pragyan (rover)",
            "option_c": "Shakti (lander) and Dhriti (rover)",
            "option_d": "Mangal (lander) and Bharat (rover)",
            "correct_answer": "B",
            "explanation": "Chandrayaan-3's lander is named Vikram (after ISRO founder Vikram Sarabhai) and the rover is named Pragyan (Sanskrit meaning 'wisdom'). They soft-landed successfully on the Moon's South Pole on August 23, 2023 — making India the 4th nation (after USA, USSR, China) to achieve a soft landing on the Moon and the first to reach the lunar south pole. The Vikram lander operated successfully for 14 days and the Pragyan rover explored the landing site, transmitting unprecedented data on water ice deposits and subsurface mineralogy. Strategic significance for India: Chandrayaan-3's success validated India's autonomous landing, navigation, and rover operations in complex lunar terrain — critical capabilities for establishing India's own lunar base. The mission data (shared with international partners) positions India as a credible member of the global lunar exploration community, enabling India to lead the LUPEX mission (with Japan) and future ISRO lunar science missions. The south pole landing capability directly supports India's crewed lunar mission planning (post-2040) and long-term vision of India as a lunar power.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Gaganyaan ---
        {
            "id": 26037,
            "question_text": "The first crewed Gaganyaan mission (Gaganyaan-4) is targeted for which year as per the revised ISRO schedule announced in 2025?",
            "option_a": "2025",
            "option_b": "2026",
            "option_c": "2027",
            "option_d": "2030",
            "correct_answer": "C",
            "explanation": "The first crewed Gaganyaan mission (Gaganyaan-4) is targeted for 2027. Before this, three uncrewed test flights are planned: Gaganyaan-G1 (Dec 2025, carrying Vyommitra humanoid robot to test life-support), G2 (2026), and G3 (2027). Crew Module Recovery trials began in 2024-25. Strategic significance for India: Gaganyaan-4 makes India the 4th nation with independent crewed spaceflight capability (after USA, Russia, China). This validates India's life-support, re-entry, and crew recovery systems. Crewed space access transforms India's geopolitical standing, enabling independent access to LEO for research, manufacturing, and national security. Post-2027, India gains autonomy in human spaceflight for crewed lunar missions (2040), space tourism, and orbital manufacturing. International partnerships (ESA, NASA) provide knowledge-sharing but Gaganyaan-4 success demonstrates India's indigenous capability — critical for India's space sovereignty.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Bioscience terms ---
        {
            "id": 26038,
            "question_text": "DNA barcoding is a technique used by the Zoological Survey of India to do what?",
            "option_a": "Create maps of DNA within chromosomes",
            "option_b": "Identify species using short standardized DNA sequences",
            "option_c": "Track genetic mutations in cancer cells",
            "option_d": "Label genetically modified organisms",
            "correct_answer": "B",
            "explanation": "DNA barcoding is a rapid species identification technique using short, standardized DNA sequences (~650 bp COI gene region). ZSI used this approach to definitively identify Simulium blackfly species transmitting River Blindness, overcoming morphological ambiguities (multiple similar-looking species). Applications: disease vector identification, biodiversity assessment, food authenticity (detecting adulteration in spice/fish products), wildlife forensics. Strategic significance for India: India's tropical biodiversity (10% of global species) remains poorly catalogued. DNA barcoding accelerates species discovery and ecological monitoring — critical for implementing ecosystem-based adaptation to climate change. India's iBOL project (International Barcode of Life) partners ZSI and Indian institutions to barcode endemic species, supporting both conservation and disease surveillance. Blackfly identification is directly applicable to detecting new River Blindness transmission zones in Northeast India and Western Ghats — enabling early intervention before endemic establishment.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Aditya-L1 instrument ---
        {
            "id": 26039,
            "question_text": "Which instrument onboard Aditya-L1 observed a powerful solar flare and a rare plasma ejection in ultraviolet light?",
            "option_a": "VELC (Visible Emission Line Coronagraph)",
            "option_b": "SUIT (Solar Ultraviolet Imaging Telescope)",
            "option_c": "SoLEXS (Solar Low Energy X-ray Spectrometer)",
            "option_d": "PAPA (Plasma Analyser Package for Aditya)",
            "correct_answer": "B",
            "explanation": "SUIT (Solar Ultraviolet Imaging Telescope) operates in the ultraviolet band (200-400 nm), observing the solar chromosphere and transition region (10,000 K temperature). Built by IIA Bangalore, SUIT captured: (1) A rare plasma ejection (filament eruption) on Feb 24, 2024, showing chromospheric dynamics never before observed at such resolution, (2) An M-class solar flare on March 1, 2024 revealing energy dissipation mechanisms. Aditya-L1 is stationed at L1 (~1.5 million km from Earth), providing unobstructed solar observation. Strategic significance for India: SUIT is India's first space-based UV telescope, filling the gap between visible (VELC) and X-ray (SoLEXS) instruments. UV observations improve solar flare prediction — critical for protecting India's 200+ GW power grid and 500+ satellites. IIA's success validates India's optical instrument heritage for future UV missions. Combined with NASA's Solar Dynamics Observatory (SDO) and ESA's Solar Orbiter, SUIT strengthens the global solar monitoring network essential for space weather forecasting that protects India's critical infrastructure.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Biomass satellite ---
        {
            "id": 26040,
            "question_text": "ESA's Biomass satellite is classified as which number 'Earth Explorer' satellite under ESA's climate and Earth systems programme?",
            "option_a": "5th",
            "option_b": "6th",
            "option_c": "7th",
            "option_d": "8th",
            "correct_answer": "C",
            "explanation": "Biomass is ESA's 7th Earth Explorer satellite (launched April 24, 2025) using a Vega C rocket from French Guiana. It uses P-band (435 MHz) synthetic aperture radar to penetrate forest canopy and measure above-ground biomass with 4-hectare resolution. Applications: (1) Quantifying carbon storage in tropical forests (Amazon, Congo, Southeast Asia), (2) Deforestation monitoring and carbon accounting for climate agreements, (3) Supporting REDD+ programs (Reduced Emissions from Deforestation). Strategic significance for India: India's Western Ghats and Northeast forests store 25+ billion tonnes of carbon. Biomass data enables India to: (1) Calculate accurate carbon credits for forest preservation, (2) Monitor illegal logging in tiger reserves and protected areas, (3) Support India's REDD+ finance mechanism (generating ~$1-2 billion annually if implemented). India's 60 million hectares of forestland represents 7% of global forest carbon — Biomass data helps India monetize forest conservation through international carbon markets. Forest monitoring via satellite reduces India's ground survey costs and enables real-time deforestation alerts to state forest departments.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- NISAR details ---
        {
            "id": 26041,
            "question_text": "NISAR studies Earth's surface changes related to which phenomena?",
            "option_a": "Volcanoes and tectonic plates only",
            "option_b": "Ocean temperatures and salinity",
            "option_c": "Earthquakes, landslides, glaciers, forests and agriculture",
            "option_d": "Atmospheric ozone and UV radiation",
            "correct_answer": "C",
            "explanation": "NISAR (NASA-ISRO Synthetic Aperture Radar) is the world's first dual-frequency SAR satellite (L-band 1.26 GHz + S-band 3.2 GHz), launched July 30, 2025 via GSLV-F16 into a 747-km sun-synchronous orbit. Dual-frequency SAR enables unprecedented capabilities: (1) L-band penetrates vegetation to map subsurface deformation (earthquakes, landslides, volcanic unrest); (2) S-band maps surface moisture, agriculture health, and cryosphere (glaciers, snow). 12-day global coverage with 3-arc-second resolution. Strategic significance for India: NISAR directly addresses India's vulnerabilities: (1) Earthquake monitoring — India sits on active seismic zones (Himalayas, Indo-Gangetic Plain); NISAR's InSAR (interferometric SAR) detects millimeter-scale ground motion enabling early warning systems, (2) Monsoon-induced landslide early detection in the Western Ghats and Northeast — critical for 300+ million people in hilly regions, (3) Agriculture monitoring during droughts and floods — supports crop insurance schemes covering 40 million farmers, (4) Glacier monitoring in Himalayas — critical for India's water security (600 million depend on glacier-fed rivers). NISAR data is public, enabling Indian institutions (GSI, CSIR-SASE, IIT-Bombay) to develop applications directly supporting India's disaster management, food security, and climate adaptation.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Space terms ---
        {
            "id": 26042,
            "question_text": "What is a Sun-Synchronous Orbit (SSO)?",
            "option_a": "An orbit that keeps the satellite always facing the Sun",
            "option_b": "A polar orbit where satellite passes any point at the same local solar time each day",
            "option_c": "An orbit synchronized with the Sun's rotation",
            "option_d": "A geostationary orbit directly above the equator",
            "correct_answer": "B",
            "explanation": "A sun-synchronous orbit (SSO) is a polar orbit with an inclination ~98° where the satellite maintains a fixed angle to the Sun due to orbital precession. The ascending node (Earth crossing) occurs at the same local solar time (~10:30 AM typical for Earth observation) every day, providing: (1) Consistent lighting geometry for multi-temporal image comparison, (2) Reduced shadows and atmospheric scattering effects, (3) Optimal angle for sensing (35-50° solar zenith angle). Period: ~100 minutes; altitude: 500-1000 km. Strategic significance for India: India's EOS constellation uses SSO (all Earth observation satellites) enabling consistent data quality for agriculture, disaster management. NISAR and future Indian SAR satellites use SSO for reliable landslide/flood monitoring. India's Gaganyaan crewed missions (2027+) will initially operate in LEO ~400 km (not SSO); understanding SSO constraints helps ISRO plan future crewed Earth observation missions and ISS participation. SSO maintenance requires periodic station-keeping maneuvers — an operational cost factor for India's satellite constellation management.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Artemis ---
        {
            "id": 26043,
            "question_text": "NASA's Artemis programme, for which IISc developed lunar brick techniques, aims to achieve what?",
            "option_a": "First human Mars landing by 2030",
            "option_b": "Establish permanent settlements on the Moon",
            "option_c": "Mine asteroids between Mars and Jupiter",
            "option_d": "Build a space station around the Sun",
            "correct_answer": "B",
            "explanation": "NASA's Artemis programme (2021-2050) aims to: (1) Return humans to the Moon within 3 years (Artemis-3 crewed lunar landing, 2027-28), (2) Establish permanent settlements at the lunar south pole (water ice access), (3) Enable deep-space exploration to Mars (2040+). IISc's bacteria-mediated in-situ resource utilization (ISRU) uses Sporosarcina pasteurii to precipitate calcium carbonate from lunar regolith, binding soil particles into bricks without energy-intensive kilns. Strategic significance for India: IISc's biotechnological approach demonstrates that India can innovate on Artemis-class challenges. India's future lunar base (post-2040) will require similar ISRU — learning from Artemis prevents costly duplication. The bacterial brick technique uses local materials (regolith), dramatically reducing launch costs from Earth (~$50,000 per kg). India's participation in international Artemis-inspired lunar base planning (2030s-2040s) is credible because IISc has already demonstrated the core technology. This positions India as a technology provider to international lunar missions, generating commercial opportunities in the $100+ billion lunar economy.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- SpaDeX details ---
        {
            "id": 26044,
            "question_text": "SpaDeX satellites weigh approximately how much each?",
            "option_a": "50 kg",
            "option_b": "100 kg",
            "option_c": "220 kg",
            "option_d": "500 kg",
            "correct_answer": "C",
            "explanation": "SpaDeX (Space Docking Experiment) consists of two 220-kg microsatellites (Chaser and Target) demonstrating autonomous docking/undocking at 380 km LEO (Dec 2024-Mar 2025). The spacecraft use indigenous Autonomous Docking and Rendezvous Sensor (ADRS) systems and relative GPS guidance. Strategic significance for India: Docking is the gating capability for: (1) Gaganyaan crewed missions (docking crew module with orbital module for safe abort and return), (2) Bharatiya Antariksh Station (BAS, 2028-35) — requires 5+ dock ports for modules/resupply, (3) Cislunar logistics (refueling, crew transfer for crewed lunar missions), (4) On-orbit servicing (extending satellite lifespans, debris removal — a $50+ billion market). SpaDeX's January 2025 success made India the 4th nation with autonomous docking (USA, Russia, China). This validates ISRO's guidance/navigation/control (GN&C) systems and confidence in Gaganyaan-4 crewed docking (2027). For India's commercial space future, docking capability enables services to international customers — positioning India as a space services provider competing with SpaceX, Axiom Space.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- ISRO Chairman ---
        {
            "id": 26045,
            "question_text": "Who is the current Chairman of ISRO who inaugurated the Fluid & Thermal Science Centre at IIT Madras in March 2025?",
            "option_a": "K. Sivan",
            "option_b": "S. Somnath",
            "option_c": "V. Narayanan",
            "option_d": "Madhavan Nair",
            "correct_answer": "C",
            "explanation": "V. Narayanan became ISRO Chairman in January 2024. He inaugurated the 'Shri S. Ramakrishnan Centre of Excellence in Fluid and Thermal Science Research' at IIT Madras on March 17, 2025. The centre is named after S. Ramakrishnan (1942-2020), an IIT Madras alumnus and ISRO's Propulsion Director who led PSLV (maiden flight 1994) and GSLV MK3 (later LVM3) development — instrumental in making India's launch vehicles globally competitive. Strategic significance: Under Narayanan's leadership (2024-onwards), ISRO is pursuing an ambitious roadmap: (1) SpaDeX docking demonstration (achieved Jan 2025), (2) Gaganyaan-G1 uncrewed (target Dec 2025), (3) NISAR Earth observation (launched July 2025), (4) Chandrayaan-4 sample return (2027), (5) Bharatiya Antariksh Station (first module 2028). The IIT Madras thermal science centre supports this roadmap by advancing expertise in cryogenic propulsion, spacecraft thermal management, and life-support systems — critical for Gaganyaan crew safety and BAS operations. This academy-industry partnership model strengthens India's indigenous space technology base, reducing reliance on ISRO's aging infrastructure and enabling rapid innovation cycles essential for competing with international space agencies.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Onchocerciasis ---
        {
            "id": 26046,
            "question_text": "River Blindness spreads through the bite of which insect?",
            "option_a": "Mosquito",
            "option_b": "Tsetse fly",
            "option_c": "Blackfly (genus Simulium)",
            "option_d": "Sand fly",
            "correct_answer": "C",
            "explanation": "River Blindness (Onchocerciasis) is transmitted by infected blackflies of the genus Simulium. Female blackflies breed in fast-flowing rivers and streams with high water turbulence (hence 'River Blindness'). During a blood meal, infected blackflies deposit larvae into skin wounds, causing: (1) Severe nodular dermatitis (itching intense enough to prevent sleep), (2) Skin atrophy and scarring, (3) Ocular disease — microfilariae migrate to eyes causing keratitis and progressive blindness (40% of infected become blind). WHO lists it as a leading infectious cause of preventable blindness globally (4 million cases; 600,000+ blinded). Strategic significance for India: While rare in mainland India, blackflies and river blindness are present in Northeast India (Assam) and the Western Ghats — areas with endemic infections in neighbouring Bangladesh and Myanmar. IISc's DNA barcoding research (with ZSI) strengthens India's capacity for vector surveillance and species identification, critical for early detection of range expansion as climate change alters river ecosystems. India's tropical climate and river ecosystems (Brahmaputra, Godavari) are vulnerable to Simulium breeding expansion. Building diagnostic and surveillance capacity in endemic regions supports the WHO's goal of eliminating onchocerciasis in Africa by 2030 and preventing its spread to India.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- ASF ---
        {
            "id": 26047,
            "question_text": "Where in India did African Swine Fever first emerge in 2021, later becoming endemic?",
            "option_a": "Manipur",
            "option_b": "Nagaland",
            "option_c": "Mizoram",
            "option_d": "Arunachal Pradesh",
            "correct_answer": "C",
            "explanation": "African Swine Fever (ASF) first emerged in India in Mizoram — specifically in Lungsen village, Lunglei district — on March 21, 2021. Since then, it has become endemic across Mizoram, spreading to Manipur, Nagaland, and Arunachal Pradesh. ASF is caused by ASFV (African Swine Fever Virus), a large double-stranded DNA virus with no vaccine or treatment. The disease has near-100% case fatality rate in domestic pigs; wild boar populations are also infected. Strategic significance for India: ASF poses a severe threat to India's small-holder pig farming economy (8+ million smallholders in Northeast India). Mizoram, Assam, and Northeast states have strong pork-based livelihoods and cultural practices, but ASF has devastated pig production, causing 70%+ losses in affected regions. The virus spreads via: (1) Direct contact with infected/dead pigs, (2) Soft ticks (Ornithodoros species) — difficult to control, (3) Contaminated feed and water. India's livestock disease surveillance system (Animal Husbandry Ministry, state departments) faces challenges: porous international borders (Myanmar shares ASF-affected wildlife; Bangladesh borders at risk), limited diagnostic capacity outside major cities, inadequate biosecurity in smallholder farms. Without effective control, ASF could spread to India's 200+ million poultry and cattle, devastating food security. India urgently needs: regional quarantine protocols, farmer capacity building, diagnostic labs in remote areas.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- GSLV-F16/NISAR ---
        {
            "id": 26048,
            "question_text": "NISAR was launched using which ISRO launch vehicle?",
            "option_a": "PSLV-C60",
            "option_b": "LVM3-M5",
            "option_c": "GSLV-F16",
            "option_d": "SSLV-D3",
            "correct_answer": "C",
            "explanation": "NISAR (NASA-ISRO Synthetic Aperture Radar) was launched on July 30, 2025 from SDSC SHAR using ISRO's GSLV-F16 (Geosynchronous Satellite Launch Vehicle-F16) into a sun-synchronous polar orbit at 747 km altitude. NISAR is the first joint Earth observation mission between NASA and ISRO. GSLV-F16 is ISRO's workhorse for medium-to-heavy payloads; the cryogenic upper stage (using indigenous cryogenic engine) provides reliable access to Sun-synchronous orbits for Earth observation. Strategic significance: GSLV's successful deployment of NISAR demonstrates India's capability to launch large dual-frequency SAR satellites reliably. The mission's success validates ISRO's cryogenic technology for international collaborations — opening opportunities for joint space programs with France (CNES), Japan (JAXA), and ESA. NISAR's success also paves the way for India's indigenous SAR satellite development (SAOCOM-like missions) and future crewed missions requiring GSLV reliability. The GSLV-F16 success rate (now 13 consecutive successes) positions ISRO as a trusted partner for international space missions and commercial payloads.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- IIT Madras cancer DB ---
        {
            "id": 26049,
            "question_text": "India's first cancer genome database was created to help researchers study cancer genomics specific to Indian populations. Which institution launched it?",
            "option_a": "AIIMS New Delhi",
            "option_b": "NCBS Bengaluru",
            "option_c": "IIT Madras",
            "option_d": "Tata Memorial Hospital",
            "correct_answer": "C",
            "explanation": "IIT Madras launched India's first cancer genome database to boost cancer genomics research. Strategic significance for India: (1) Genome databases for Indian populations are critical because cancer prevalence/genetics vary by ethnicity — Western databases may not apply to Indians, (2) Supports personalized medicine development targeting Indian cancer profiles, (3) Advances Indian biotech capability in precision oncology (competing with USA/China), (4) Reduces India's dependence on Western pharmaceutical IP. Cancer is a leading cause of death in India (5.8% of deaths by 2025); indigenous research accelerates treatment breakthroughs.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- SPHEREx orbit ---
        {
            "id": 26050,
            "question_text": "At what altitude does NASA's SPHEREx satellite orbit Earth?",
            "option_a": "250 km",
            "option_b": "450 km",
            "option_c": "650 km",
            "option_d": "1,200 km",
            "correct_answer": "C",
            "explanation": "NASA's SPHEREx satellite orbits Earth at 650 km in a sun-synchronous orbit (98.85° inclination). This altitude balances: (1) sufficient distance from atmospheric drag (operational lifetime 5+ years), (2) close enough for high-resolution near-infrared spectroscopy (5-metre ground resolution goal). SPHEREx studies 450 million galaxies and 100 million stars, creating a 3D map of the universe's history from the cosmic dark ages through cosmic noon (peak star formation era 2-3 billion years after Big Bang). Strategic significance for India: India's planned independent space telescope missions (Post-Aditya-L1) should target complementary wavelengths and altitudes. The Gaganyaan and BAS programs will eventually enable Indian astronauts to service and repair space telescopes (like the Hubble Service Missions). SPHEREx's sun-synchronous orbit demonstrates optimal orbital engineering for Earth observation platforms; India's future remote sensing constellation can leverage similar altitude/inclination geometry. Indian astrophysicists analyzing SPHEREx data gain experience with massive sky-survey datasets, preparing them to lead India's own all-sky survey mission planned for the 2030s-2040s.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- IIT Roorkee/others ---
        {
            "id": 26051,
            "question_text": "The SUIT instrument aboard Aditya-L1 stands for what?",
            "option_a": "Solar Ultraviolet Imaging Telescope",
            "option_b": "Solar Ultraviolet Infrared Tracker",
            "option_c": "Space UV Imaging Terminal",
            "option_d": "Sun Ultraviolet Intelligence Tool",
            "correct_answer": "A",
            "explanation": "SUIT stands for Solar Ultraviolet Imaging Telescope — an optical imaging instrument operating in the ultraviolet (UV) band (200-400 nm). Built by Indian Institute of Astrophysics (IIA) Bangalore, SUIT observes the solar chromosphere and transition region (temperature ~10,000 K), where energy from the solar core is dissipated. SUIT made first-of-its-kind observations during its commissioning phase (Jan-Sept 2024): (1) A rare plasma ejection (filament eruption) on Feb 24, 2024, (2) A powerful M-class solar flare on March 1, 2024 showing chromospheric dynamics in unprecedented detail. Strategic significance for India: SUIT is India's first indigenous space-based UV telescope; its UV capability fills a gap between visible (VELC) and X-ray (SoLEXS) instruments aboard Aditya-L1. UV observations of the chromosphere are critical for understanding solar flare initiation mechanisms — knowledge that improves solar storm predictions. IIA's success with SUIT validates India's optical instrument design and space-flight heritage, enabling future UV missions for astrophysics and solar physics. The data from SUIT, combined with NASA's Solar Dynamics Observatory (SDO) and ESA's Solar Orbiter, strengthens the global network of solar monitors — essential for space weather forecasting.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Vandenberg ---
        {
            "id": 26052,
            "question_text": "SPHEREx and PUNCH missions were launched from which US space force base?",
            "option_a": "Cape Canaveral Space Force Station, Florida",
            "option_b": "Vandenberg Space Force Base, California",
            "option_c": "Patrick Space Force Base, Florida",
            "option_d": "Edwards Air Force Base, California",
            "correct_answer": "B",
            "explanation": "SPHEREx and PUNCH were launched together on March 12, 2025, from Vandenberg Space Force Base (California) aboard SpaceX's Falcon 9 rocket into sun-synchronous orbit (650 km). Vandenberg is the US military's primary polar orbit launch facility. Strategic significance for India: Vandenberg's sun-synchronous launch capability (polar orbits) is critical for Earth observation — a domain where India aspires to compete commercially. India's launch facility at SDSC SHAR (13.7°N latitude) cannot economically reach sun-synchronous orbits (requires equator-facing sites for cost efficiency). This geographic constraint means India cannot compete directly with Vandenberg for polar orbit launches. However, India's equatorial advantage (SHAR at 13.7°N) optimizes launches to geostationary and near-equatorial orbits — a niche India should dominate. For India's future crewed missions (Gaganyaan, 2027+), polar orbit capability is less critical than LEO/GTO access. India's space-launch strategy should focus on this geographic advantage rather than trying to replicate Vandenberg's polar capabilities.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Vega-C ---
        {
            "id": 26053,
            "question_text": "ESA's Biomass satellite was launched using which rocket from French Guiana?",
            "option_a": "Ariane 5",
            "option_b": "Ariane 6",
            "option_c": "Vega C",
            "option_d": "Soyuz",
            "correct_answer": "C",
            "explanation": "Biomass was launched April 24, 2025 using ESA's Vega C rocket from the European Spaceport (Kourou, French Guiana). Vega C is a 4-stage solid/liquid launch vehicle lifting 2,300 kg to sun-synchronous orbit (operational 2020+, succeeding Vega). Strategic significance for India: ESA's Vega C represents the mid-range launch market (~2,000-3,000 kg to SSO) — a segment where India's PSLV (3,800 kg to sun-synchronous) dominates commercially. India has launched 50+ PSLV missions; ESA's Vega line offers competition but PSLV's heritage and cost-competitiveness enable India to capture 30% of commercial smallsat launches (~$3 billion market by 2030). India's SSLV (Super Small Launch Vehicle, 700 kg to LEO) targets the dedicated smallsat launch niche — a market segment Vega C doesn't serve. This complementary positioning (PSLV for medium-lift, SSLV for small-lift) positions India as a specialized launch provider rather than a general-purpose competitor with ESA/Arianespace.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Europa ---
        {
            "id": 26054,
            "question_text": "NASA's Europa Clipper mission is significant because Europa (Jupiter's moon) is believed to have what beneath its icy surface?",
            "option_a": "Volcanic eruptions",
            "option_b": "A subsurface liquid water ocean",
            "option_c": "Dense nitrogen atmosphere",
            "option_d": "Large deposits of diamond",
            "correct_answer": "B",
            "explanation": "Europa (Jupiter's 4th-largest moon) has a 100-km-thick icy crust overlying an estimated 100-200 km ocean of liquid water — the largest water reservoir in our solar system (>2x Earth's oceans). Tidal heating from Jupiter's gravity creates geothermal energy supporting potential chemosynthetic life (no photosynthesis in perpetual darkness). NASA's Europa Clipper (launched Oct 2024) will reach Jupiter orbit April 2025, conducting 49 close flybys to map subsurface water, surface ice composition, and plumes. Strategic significance for India: Europe's exploration represents the search for life beyond Earth — fundamental to humanity's understanding of life's ubiquity. India's participation in international astrobiology research (through CSIR, IISc) positions India as engaged in deep-space science. Future Indian contributions: (1) Joint missions with international partners (ISRO-NASA collaborations on Mars/lunar missions) can evolve to include outer solar system missions, (2) India's planetary science expertise (Mars Orbiter Mission, Chandrayaan) establishes credibility for crewed/robotic outer solar system missions by 2050. Europa's ocean also informs India's thinking about potential oceans on exoplanets discovered by Indian astronomers using future space telescopes.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Lumpy Skin ---
        {
            "id": 26055,
            "question_text": "Lumpy Skin Disease, which caused mass cattle deaths in India, is caused by which type of agent?",
            "option_a": "Bacteria",
            "option_b": "Protozoa",
            "option_c": "Virus (Capripoxvirus)",
            "option_d": "Fungus",
            "correct_answer": "C",
            "explanation": "Lumpy Skin Disease (LSD) is caused by Lumpy Skin Disease Virus (LSDV), a double-stranded DNA virus of the Capripoxvirus genus (related to cowpox, sheeppox). LSD symptoms: (1) Fever (40-41°C), (2) Nodular skin lesions (2-5 cm, lasting 3-4 weeks), (3) Lymph node enlargement, (4) Lameness, (5) Reproductive failures, (6) Reduced milk production (70% drop). Mortality rate: 5-10% in naturally infected cattle, up to 40% in susceptible breeds. Transmission: (1) Insect vectors (particularly Stomoxys flies, mosquitoes Aedes and Culex), (2) Direct contact with lesions, (3) Contaminated fomites. India's outbreak (2022-2024): First case detected near Delhi (August 2022) via imported animals; rapidly spread to 15 states affecting 1 million+ cattle. Economic impact: ~Rs 20,000 crore (estimated) from reduced milk production, veterinary costs, animal deaths. Strategic significance for India: India's dairy industry (3rd largest globally, Rs 11 lakh crore/year) was severely impacted by LSD outbreaks. As a monsoon-prone country (favorable for vector breeding), India faces recurring LSD epidemics. The Indian Council of Agricultural Research (ICAR) and Animal Husbandry Ministry responded with vaccination campaigns (Atalav LSD-L vaccine, indigenous). LSD is controlled/eradicated in developed countries (USA, UK, Europe) but endemic in Africa and spreading through Asia — India must maintain strict biosecurity and vaccination to prevent endemic status.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- GSLV ---
        {
            "id": 26056,
            "question_text": "GSLV stands for what in the context of ISRO's launch vehicles?",
            "option_a": "Geosynchronous Satellite Launch Vehicle",
            "option_b": "General Space Launch Vehicle",
            "option_c": "Gravity Stabilized Launch Vessel",
            "option_d": "Guided Satellite Landing Vehicle",
            "correct_answer": "A",
            "explanation": "GSLV stands for Geosynchronous Satellite Launch Vehicle. ISRO's GSLV family has two main versions: (1) GSLV Mk I & Mk II (retired) — 1,900 kg to GTO (Geostationary Transfer Orbit), (2) GSLV Mk III / LVM3 (currently operational) — 4,000-5,500 kg to GTO, 8,000 kg to LEO. GSLV uses indigenous cryogenic upper-stage engine (CE-20), making India self-reliant in medium-to-heavy lift launch capability. Recent successes include GSLV-F16 launching NISAR (July 30, 2025) and GSLV-F15 launching NVS-02/NavIC-16 (January 29, 2025). GSLV MK3 (LVM3) is the more powerful variant, used for launching Gaganyaan crew capsule and heavy communication satellites. Strategic significance for India: GSLV's cryogenic engine (CE-20) was originally technology-transfer dependent on Russia (Ukraine crisis threatened supplies); India's indigenous development (1990s-2010s) achieved full self-reliance. The success of GSLV validates India's technological capability and enables international collaborations (NASA-ISRO on NISAR). GSLV's availability for commercial launches under NSIL creates revenue streams (~Rs 250 crore per launch) supporting ISRO's budget. For India's crewed missions, GSLV MK3 is the sole reliable launcher until NGLV is operational (2032+) — making GSLV reliability critical for Gaganyaan success.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Multiple Sclerosis ---
        {
            "id": 26057,
            "question_text": "Multiple Sclerosis (MS) affects approximately how many people worldwide?",
            "option_a": "1.2 million",
            "option_b": "2.8 million",
            "option_c": "5.4 million",
            "option_d": "10 million",
            "correct_answer": "B",
            "explanation": "Multiple Sclerosis (MS) affects approximately 2.8 million people worldwide; the USA alone has ~1 million cases. MS is an autoimmune disorder where CD8+ T cells and autoantibodies attack myelin (insulation) around axons in the brain and spinal cord, causing progressive demyelination and neurological disability. Symptoms: visual disturbances, weakness, numbness, ataxia, cognitive decline, progressing to disability. Recent microbiome studies (2024-25) found that MS patients have reduced Bifidobacterium and increased Akkermansia — a dysbiotic signature linked to worse outcomes. Strategic significance for India: MS prevalence in India is rising (~40,000+ cases, estimated), particularly in urban areas with Western lifestyles. India's gut microbiome diversity (influenced by spices, fermented foods, tropical pathogens) differs significantly from Western populations — understanding MS through the Indian microbiome lens accelerates drug development. India's CSIR laboratories and AIIMS are investigating whether traditional foods (yogurt with specific Lactobacillus strains, fermented vegetables) offer MS protection. The 2025 Nobel Medicine Prize (Brunkow-Ramsdell-Sakaguchi on immune tolerance) provides scientific framework for developing Treg-based MS therapeutics in India. Indian biotech companies targeting the MS microbiome (Abiome, Micronutra) are positioning India as a leader in precision medicine for autoimmune diseases.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- IIT Madras ballistic ---
        {
            "id": 26058,
            "question_text": "IIT Madras's research on protecting reinforced concrete (RC) panels against ballistic missiles was published in which journal?",
            "option_a": "Nature Energy",
            "option_b": "Science Advances",
            "option_c": "Reliability Engineering & System Safety",
            "option_d": "Journal of Military Technology",
            "correct_answer": "C",
            "explanation": "IIT Madras published a framework (Reliability Engineering & System Safety, 2024-25) for designing reinforced concrete panels to withstand ballistic impacts (missile/aircraft collision). The framework optimizes: (1) Concrete thickness, reinforcement density, material grade, (2) Impact energy absorption via material deformation, (3) Residual capacity for secondary impacts. Applications: military bunkers, nuclear power containment, critical infrastructure hardening. Strategic significance for India: India's critical infrastructure (power plants, defense facilities, urban centers) faces emerging threats from advanced missiles (Pakistani Brahmos upgrades, Chinese DF-21). Hardening infrastructure against ballistic impacts is a national security priority. IIT Madras's research supports: (1) DRDO's initiatives to design blast-resistant structures, (2) Design codes for Indian nuclear reactor safety (addressing post-Fukushima standards), (3) Civil defense infrastructure modernization. India's expertise in structural resilience engineering can be exported to developing nations seeking ballistic hardening — generating technology transfer revenue (~$500 million market by 2035).",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- 3D map ---
        {
            "id": 26059,
            "question_text": "Which NASA mission will create a 3D infrared map of the sky by measuring spectra of hundreds of millions of galaxies?",
            "option_a": "PUNCH",
            "option_b": "SPHEREx",
            "option_c": "Europa Clipper",
            "option_d": "Artemis",
            "correct_answer": "B",
            "explanation": "SPHEREx (launched March 12, 2025 at 650 km altitude) measures near-infrared spectra (0.75-5 micrometers) of 450 million galaxies and 100 million stars to create a 3D cosmic map. It covers: (1) star-formation history (when/where stars were born over cosmic time), (2) galaxy mergers and large-scale structure, (3) reionization epoch (first stars 13+ billion years ago), (4) Milky Way structure and dust distribution. The 3D data reveals cosmic web filaments and voids — fundamental to understanding gravity's role in shaping the universe. Strategic significance for India: SPHEREx data (publicly available via NASA archives) will be analyzed by Indian astrophysicists at IUCAA Pune, IISER institutions, and IIT centers. Indian students can participate in global collaborations analyzing a dataset of unprecedented cosmic scale. India's National Supercomputing Mission provides compute power for processing terabyte-scale datasets — positioning India as a data-science hub for astrophysics research. Future Indian space missions (planned UV telescope ~2035) can target complementary wavelengths, building on SPHEREx's discoveries. This democratization of space science accelerates India's participation in cutting-edge cosmology research.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- AMR ---
        {
            "id": 26060,
            "question_text": "AMR in the healthcare context stands for?",
            "option_a": "Automated Medical Records",
            "option_b": "Antimicrobial Resistance",
            "option_c": "Acute Metabolic Response",
            "option_d": "Advanced Molecular Research",
            "correct_answer": "B",
            "explanation": "Antimicrobial Resistance (AMR) — the ability of microorganisms to survive antimicrobial drugs (antibiotics, antivirals) — causes ~1 million deaths annually globally; India contributes ~240,000 deaths/year (highest globally). Mechanisms: (1) genetic mutations conferring drug resistance, (2) horizontal gene transfer (plasmids spreading resistance), (3) biofilm formation (collective resistance). IIIT-Delhi's AMRSense uses machine learning to identify AMR patterns in hospital electronic medical records (antibiotics prescribed vs. culture sensitivity results), enabling early detection of outbreaks. Strategic significance for India: India's high AMR burden stems from: (1) Overuse of antibiotics in animals/agriculture (50% of India's antibiotic consumption), (2) Poor infection control in hospitals (nosocomial transmission), (3) Inadequate diagnostic infrastructure (presumptive antibiotic use without culture). WHO rates India's AMR threat as critically high. India's priorities: (1) Implement antibiotic stewardship in hospitals and veterinary medicine (reducing 50% unnecessary use), (2) Scale diagnostic labs (rapid culture/sensitivity testing) to detect resistance early, (3) Develop new antibiotics for resistant TB, sepsis. IIIT-Delhi's AMRSense contributes to data-driven surveillance — critical for India's emerging disease prevention strategy.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Chandrayaan next ---
        {
            "id": 26061,
            "question_text": "Which ISRO mission, planned for the future, is a joint mission with JAXA (Japan) to explore the Moon?",
            "option_a": "Chandrayaan-4",
            "option_b": "Lunar Polar Exploration Mission (LUPEX)",
            "option_c": "Mangalyaan-2",
            "option_d": "Gaganyaan-2",
            "correct_answer": "B",
            "explanation": "LUPEX (Lunar Polar Exploration Mission) is a planned joint mission between ISRO and JAXA (Japan Aerospace Exploration Agency) to explore Moon's south polar region and study water ice resources. Strategic significance: (1) India-Japan cooperation demonstrates India's capability to lead international space partnerships, (2) Lunar water ice extraction critical for establishing permanent Moon bases (water = fuel, oxygen, drinking water), (3) LUPEX targets 2026-27 launch timeline (after Chandrayaan-4), (4) Advances India's lunar science and Moon-to-Earth human spaceflight roadmap, (5) Signals India's participation in global Artemis Accords. ISRO provides lander; JAXA provides rover and instruments.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- NCPRE ---
        {
            "id": 26062,
            "question_text": "NCPRE, where IIT Bombay developed its high-efficiency tandem solar cell, stands for?",
            "option_a": "National Centre for Photovoltaic Research and Education",
            "option_b": "National Centre for Power Research and Engineering",
            "option_c": "National Committee for Photon and Radiation Engineering",
            "option_d": "National Centre for Polymer Research and Experimentation",
            "correct_answer": "A",
            "explanation": "NCPRE stands for National Centre for Photovoltaic Research and Education at IIT Bombay. Strategic significance for India: (1) Developed tandem solar cell with ~30% efficiency — world-class performance competitive with global standards, (2) Supports India's renewable energy targets (500 GW by 2030, Net-Zero by 2070), (3) Reduces India's dependence on imported solar cell technology (China dominates ~80% global production), (4) Enables Make-in-India for solar manufacturing — supports domestic solar component industry, (5) Reduces electricity costs as rooftop solar scales. India leads renewable capacity among developing nations; solar tech breakthroughs accelerate climate goals.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- ESA Biomass launch rocket ---
        {
            "id": 26063,
            "question_text": "The ESA Biomass satellite will use radar technology to create what kind of models of forests from space?",
            "option_a": "2D surface maps",
            "option_b": "Infrared thermal images",
            "option_c": "Detailed 3D models of forest structures",
            "option_d": "Chemical composition charts",
            "correct_answer": "C",
            "explanation": "Biomass uses P-band SAR (435 MHz, long wavelength) to penetrate forest canopies, providing: (1) Above-ground biomass estimates at 0.1-hectare resolution, (2) 3D forest structure (tree height, density layering), (3) Carbon stock assessment (~200 tonnes carbon per hectare in old-growth tropical forests). Unlike optical satellites (blocked by clouds/canopy), P-band radar sees through vegetation. Strategic significance for India: India's 60 million hectares of forests store 25+ billion tonnes of carbon. Biomass data enables: (1) Accurate carbon accounting for international climate finance (selling carbon credits), (2) Protected forest monitoring (tiger reserves, sacred groves) — detecting illegal logging within weeks, (3) Agroforestry potential assessment (identifying suitable land for climate-smart farming across 150 million farms), (4) REDD+ revenue estimation (generating $1-2 billion/year from forest preservation). India's Forest Survey of India (FSI) currently surveys forests every 2 years via ground surveys (expensive, slow). Biomass enables continuous remote monitoring — reducing costs 80% and improving response time for tackling deforestation. This data advantage supports India's climate commitments and forest protection goals.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Guar gum ---
        {
            "id": 26064,
            "question_text": "In IISc's bacteria-based lunar brick technique, guar gum is combined with which bacterium?",
            "option_a": "Bacillus cereus",
            "option_b": "Sporosarcina pasteurii",
            "option_c": "Clostridium perfringens",
            "option_d": "Lactobacillus acidophilus",
            "correct_answer": "B",
            "explanation": "IISc's Biologically Induced Calcite Precipitation (BICP) uses S. pasteurii (a rod-shaped, urease-producing bacterium) + guar gum (a natural polysaccharide binder from guar legume). Mechanism: (1) Bacteria hydrolyze urea → ammonia + CO2, (2) CO2 reacts with calcium to form calcium carbonate (CaCO3) crystals, (3) Guar gum polymers bind particles into a cohesive mass (compressive strength ~6-7 MPa — comparable to unfired adobe bricks). Advantages over cement: (1) Zero thermal energy (concrete requires 800°C kiln), (2) Uses local materials (regolith), (3) Self-healing (bacteria can be reactivated if cracks form). Strategic significance for India: This technique has immediate applications: (1) Stabilizing moon/Mars habitat walls without importing building materials, (2) Reducing construction costs by 90% vs. Earth-manufactured bricks shipped to space (~$50,000 per kg). India's Bharatiya Antariksh Station (BAS, 2028-35) and crewed lunar missions (2040+) will benefit from this ISRU technology. IISc's innovation positions India as a supplier of habitat-construction expertise to international lunar base consortiums — generating licensing revenue ($100+ million). Bioengineering solutions like this represent India's competitive advantage in leveraging biology for space resource utilization.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Artemis/Moon ---
        {
            "id": 26065,
            "question_text": "National Space Day is celebrated in India on which date?",
            "option_a": "July 22",
            "option_b": "August 23",
            "option_c": "September 7",
            "option_d": "October 22",
            "correct_answer": "B",
            "explanation": "National Space Day (August 23) commemorates Chandrayaan-3's successful landing on the Moon's South Pole on August 23, 2023. Declared a national observance (annual celebration from 2024 onwards), National Space Day celebrates India's space achievements and encourages STEM education. The date symbolizes India becoming the 4th nation with lunar soft-landing capability and the first with south-pole precision landing — a transformative moment for India's space program. Strategic significance for India: National Space Day serves multiple purposes: (1) Public engagement — building awareness of ISRO's contributions to food security (EOS satellites for agriculture), disaster management (real-time flood/earthquake early warning), and climate monitoring, (2) Youth inspiration — recruiting next-generation scientists/engineers for India's space ambitions, (3) Cultural pride — framing space exploration as part of India's scientific renaissance, (4) International diplomacy — demonstrating India's technological sophistication to global partners. Annual celebrations at schools/universities can highlight India's milestones (Chandrayaan, Gaganyaan, NISAR) and connect them to students' daily lives (GPS navigation, weather forecasting, crop insurance — all enabled by ISRO satellites). National Space Day reinforces India's identity as a spacefaring nation.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- ZSI ---
        {
            "id": 26066,
            "question_text": "ZSI, which used DNA barcoding to identify blackfly species spreading River Blindness, stands for?",
            "option_a": "Zoological Survey of India",
            "option_b": "Zoonotic Science Institute",
            "option_c": "Zone of Scientific Investigation",
            "option_d": "Zoological Studies Institute",
            "correct_answer": "A",
            "explanation": "ZSI (Zoological Survey of India) is an autonomous research organization under the Ministry of Environment, Forests & Climate Change (MOEF&CC), established 1916. ZSI manages 16 regional centers across India conducting biodiversity research, species inventories, and disease vector identification. The 2024-25 blackfly DNA barcoding study identified Simulium species vectors of River Blindness using the COI (cytochrome oxidase I) gene marker — enabling precise geographic mapping of transmission zones. Strategic significance for India: ZSI operates the National Biodiversity Data Repository, maintaining specimen records for ~2 million specimens — critical for tracking emerging disease vectors. India's high biological diversity (10% of global species) is under-sampled and poorly documented. ZSI's expansion of DNA barcoding (1,000+ species barcoded) accelerates: (1) invasive species detection (Nile tilapia in Indian rivers, Australian wasps), (2) disease vector monitoring (mosquitoes transmitting dengue/malaria, tick species spreading Crimean-Congo hemorrhagic fever), (3) wildlife forensics (detecting illegal wildlife trafficking). For India's public health, ZSI's surveillance infrastructure is critical — early detection of emerging vector species enables prevention of new epidemics (e.g., detecting Aedes albopictus expansion into new regions before dengue outbreaks occur).",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- S Ramakrishnan ---
        {
            "id": 26067,
            "question_text": "The 'Shri S. Ramakrishnan Centre of Excellence' at IIT Madras is named after whom?",
            "option_a": "Former ISRO chairman who contributed to PSLV and GSLV MK3",
            "option_b": "Former President of India and nuclear scientist",
            "option_c": "Noble Prize winning biochemist from Tamil Nadu",
            "option_d": "Founder of India's satellite programme",
            "correct_answer": "A",
            "explanation": "The 'Shri S. Ramakrishnan Centre of Excellence in Fluid and Thermal Science Research' (inaugurated March 17, 2025) honors S. Ramakrishnan (1942-2020), an IIT Madras mechanical engineering graduate who served as ISRO's Propulsion Director and Deputy Director General. Ramakrishnan's career spanned: (1) PSLV development (maiden flight 1994), (2) Indigenous cryogenic engine development (CE-20 for GSLV), (3) GSLV MK3/LVM3 (later vehicles for Gaganyaan and heavy-lift missions). His technical leadership transformed ISRO into a globally competitive launch provider. Strategic significance for India: The centre focuses on: (1) Cryogenic propulsion thermal management, (2) Spacecraft thermal control systems, (3) Life-support systems for crewed missions. These areas directly support Gaganyaan crew safety and BAS operations. Naming the centre after Ramakrishnan exemplifies India's tradition of honoring scientific pioneers and motivates engineers to contribute to India's ambitious space goals. ISRO Chairman V. Narayanan's presence at the inauguration underscores the centre's strategic importance to India's future space programs. This academy-ISRO partnership accelerates technology development cycles — critical for achieving Gaganyaan-4 (2027) and Chandrayaan-4 (2027-28) with confidence in tested thermal/life-support systems.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Mars flyby ---
        {
            "id": 26068,
            "question_text": "NASA's Europa Clipper performed a flyby of which planet in March 2025 to gain speed for its voyage to Jupiter?",
            "option_a": "Venus",
            "option_b": "Mars",
            "option_c": "Saturn",
            "option_d": "Earth",
            "correct_answer": "B",
            "explanation": "Europa Clipper (launched Oct 2024) performs gravity assist maneuvers (flybys) to reach Jupiter on a fuel-efficient trajectory. Mars flyby (March 2025) provides velocity change without burning fuel. Subsequent flybys: Earth (Dec 2026), Venus, Earth again before Jupiter arrival (April 2025, updated from prior). Gravity-assist technique reduces fuel requirements by 50%+ — enabling heavier payloads and longer missions. Strategic significance for India: India's Mangalyaan (Mars Orbiter Mission, 2013) used a similar gravity-assist trajectory (Earth-Sun L1 point) to reach Mars with minimal fuel — validating India's mastery of orbital mechanics. India's planned future deep-space missions (Venus missions, outer solar system exploration) will use gravity-assists to reduce launch costs. Understanding gravity-assist physics is critical for India to develop autonomous spacecraft for distant targets without relying on international partners for trajectory design. Europa Clipper's journey demonstrates the sophistication of cislunar/interplanetary navigation that India must master for independent crewed Mars missions (planned post-2045). Indian students can follow Europa Clipper's trajectory using ephemeris data (public NASA archives) — building expertise in trajectory analysis essential for India's future deep-space capabilities.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Reusable rocket ---
        {
            "id": 26069,
            "question_text": "ISRO's Next Generation Launch Vehicle (NGLV) is designed with which innovative feature to reduce launch costs?",
            "option_a": "Solar-powered upper stage",
            "option_b": "Reusable booster stage",
            "option_c": "Air-breathing engines at lower altitudes",
            "option_d": "Nuclear-powered core stage",
            "correct_answer": "B",
            "explanation": "ISRO's Next Generation Launch Vehicle (NGLV) is designed with a reusable booster stage (similar to SpaceX Falcon 9's propulsive landing approach) combined with two expendable upper stages. The LOX-methane engine (LPSC-developed) enables 10+ reuse cycles per booster (vs. 1 for solid motors). Cost reduction mechanism: Booster reuse amortizes development cost (~Rs 2,000 crore) over 100+ launches (~Rs 20 crore per launch), reducing per-flight cost from Rs 1,600 crore (current GSLV) to Rs 700-900 crore (projected NGLV). Capacity: 10-12 tonnes to GTO, 20-25 tonnes to LEO. Timeline: Operational status target 2032-35. Strategic significance for India: Cost-competitive launch services are critical for India's commercial space ambitions. SpaceX Falcon 9's $62 million per launch (~$5,000 per kg) has captured 60%+ of global commercial launch market. NGLV's projected cost (~Rs 100 crore = $12 million per launch for dedicated slots, ~$1,200 per kg) cannot match Falcon 9's unit economics, but can target: (1) Government captive launches (ISRO satellites, Defense), (2) Dedicated small-sat launchers partnering with startups, (3) International partnerships leveraging India's cost advantages. Technology transfer to startups (Skyroot, Agnikul) enables India's reusable rocket ecosystem — critical for long-term space economy competitiveness.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Bird Flu ---
        {
            "id": 26070,
            "question_text": "Bird Flu (Avian Influenza) is caused by which type of influenza virus?",
            "option_a": "Influenza B (IBV)",
            "option_b": "Influenza C",
            "option_c": "Influenza A (H5N1/H5N2)",
            "option_d": "Influenza D",
            "correct_answer": "C",
            "explanation": "Avian Influenza (AI) is caused by Influenza A virus, particularly highly pathogenic strains H5N1 and H5N2. The 'H' and 'N' designate surface proteins (Hemagglutinin and Neuraminidase) that determine transmissibility and virulence. H5N1 has a case fatality rate of ~50% in humans (77 deaths from 150+ human cases globally). The virus is zoonotic — spreading from wild birds and poultry to humans via direct contact, respiratory droplets, or contaminated surfaces. Standard control measures include: mass culling of infected flocks (within 3 km radius), disinfection, biosecurity for poultry farms. Strategic significance for India: India's poultry industry (~$8 billion/year) is vulnerable to AI epidemics. Outbreaks in Kerala (2021, 2023), West Bengal, and Haryana caused economic losses (culled 50,000+ birds, trade disruptions). H5N1 spread to dairy cattle in the USA (2024-25) represents a dangerous spillover — if it reaches India's 300 million dairy cattle, the consequences would be catastrophic. India's surveillance system (Ministry of Animal Husbandry, ICMR) monitors AI in poultry and wild birds, but capacity in rural areas is limited. Vaccine development is critical; India's Serum Institute and Bharat Biotech are researching pandemic preparedness. A major AI pandemic in India could trigger widespread hunger and economic collapse — making this a critical biosecurity and food security issue.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- PUNCH details ---
        {
            "id": 26071,
            "question_text": "What does PUNCH stand for in the context of NASA's solar mission launched in 2025?",
            "option_a": "Photon Understanding Nuclear Corona Heliosphere",
            "option_b": "Polarimeter to Unify the Corona and Heliosphere",
            "option_c": "Proton Ultra Narrow Corona and Heliosphere",
            "option_d": "Probe Unified Near Corona and Heliosphere",
            "correct_answer": "B",
            "explanation": "PUNCH (Polarimeter to Unify the Corona and Heliosphere) is a NASA astrophysics mission consisting of 4 satellites (650 km sun-synchronous orbit) studying the solar corona's energy dissipation and solar wind acceleration. Payload: Thomson scattering polarimeter observing the corona's outer regions (1-10 solar radii). Goals: understand why the corona is hotter than the solar surface (100x temperature paradox) and how CMEs form. Launched March 12, 2025 alongside SPHEREx. Strategic significance for India: Aditya-L1 (stationed at L1, 1.5 million km from Earth) observes the inner corona (0.8-1.5 solar radii) with high-resolution instruments (VELC, SUIT, SoLEXS). PUNCH's outer corona measurements complement Aditya-L1's inner corona views, creating a synergistic global solar monitoring network. India's scientists (IIA, IIT-B, IISER) can analyze combined Aditya-L1 + PUNCH data to model the full corona energy budget. This international collaboration positions India as a credible partner in solar science — enabling India to lead future solar physics missions. Understanding CME formation (critical for space-weather forecasting) is essential for protecting India's power grid and satellites. India's contribution to global space weather forecasting networks via Aditya-L1 strengthens India's role in disaster preparedness.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- LPSC ---
        {
            "id": 26072,
            "question_text": "LPSC, which is developing the LOX-methane engine for ISRO's NGLV, stands for?",
            "option_a": "Liquid Propulsion Systems Centre",
            "option_b": "Launch Propulsion Science Cluster",
            "option_c": "Liquid Propellant Space Centre",
            "option_d": "Launch and Propulsion Systems Corporation",
            "correct_answer": "A",
            "explanation": "LPSC (Liquid Propulsion Systems Centre), headquartered at Thiruvananthapuram, Kerala, is ISRO's premier center for liquid engine development. Founded 1974, LPSC has developed: (1) cryogenic engines for GSLV (CE-20, 18-tonne thrust), (2) Vikas engine for PSLV second stage (45-tonne thrust), (3) upcoming LOX-methane engines for NGLV (100+ tonne thrust class). Current NGLV development: LOX-methane engines (reusable, green propellant, Indian availability of methane). LPSC's March 3, 2025 spark-torch igniter test demonstrated reliable ignition of LOX-methane — a critical subsystem for NGLV first-stage booster. Strategic significance for India: LPSC's technical expertise has evolved from imported technology (1990s, Russian cryogenic engine license) to fully indigenous development. This transformation of LPSC from a license-holder to an innovator exemplifies India's technology independence journey. NGLV's success by 2032-35 will cement India's position as a self-reliant space power. LPSC's Kerala location strengthens India's decentralized space infrastructure — reducing vulnerability to geographic concentration (SHAR in Andhra Pradesh). Skilled engineers in Kerala's LPSC can support private startups (Skyroot, Agnikul) developing competing reusable rockets — fostering competition and innovation in India's space ecosystem.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- ISRO Aditya distance ---
        {
            "id": 26073,
            "question_text": "At approximately what distance from Earth was Aditya-L1 stationed at Lagrange Point L1?",
            "option_a": "500,000 km",
            "option_b": "1 million km",
            "option_c": "1.5 million km",
            "option_d": "3 million km",
            "correct_answer": "C",
            "explanation": "Aditya-L1 orbits the Sun-Earth L1 point (1.5 million km from Earth, 150 million km from Sun — 1% of Earth-Sun distance). At L1, the gravitational attraction of Earth + Sun + centrifugal force balance, allowing the satellite to remain stationary relative to Earth's orbit. L1 offers continuous, unobstructed solar observation (no Earth-Moon eclipses). Aditya-L1 was launched September 2, 2023 via PSLV-C57; reached L1 January 6, 2024 after 150-day transit. Payload: 7 instruments observing Sun's photosphere, chromosphere, transition region, corona, and solar wind. Strategic significance for India: L1 is the premier location for solar science — NASA's ACE, SOHO (with ESA), and DSCOVR stations are also at L1. Aditya-L1's arrival positions India as a contributor to global solar physics research. India's 1.4 billion population is vulnerable to solar storm damage (power grid blackouts, telecom disruptions during monsoon season when alternative paths are limited). Aditya-L1's early warning capability for coronal mass ejections can provide 8-16 minute advance notice to Indian grid operators — invaluable for protecting critical infrastructure. Aditya-L1's science success (operational >5 years) validates India's capability for L2 missions (infrared telescope) and future L3/L4 missions — enabling India to maintain independent access to Lagrange points.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- GSLV MK3 / LVM3 ---
        {
            "id": 26074,
            "question_text": "GSLV MK3, also known as LVM3, is used by ISRO for what purpose?",
            "option_a": "Launching small satellites into LEO",
            "option_b": "Launching heavier payloads including crew capsule for Gaganyaan (Mk III/LVM3)",
            "option_c": "Anti-satellite weapon testing",
            "option_d": "Launching Earth observation satellites to polar orbits only",
            "correct_answer": "B",
            "explanation": "GSLV MK3 (renamed LVM3 in 2021) is India's heavy-lift launch vehicle: 3-stage (strap-on solid boosters + L110 liquid core + C25 cryogenic upper stage). Capacity: 4,000-5,500 kg to GTO (Geostationary Transfer Orbit), 8,000-10,000 kg to LEO. Maiden flight 2014; operational status 2018+. The cryogenic C25 upper stage uses indigenous CE-20 engine (18-tonne thrust), developed by LPSC. Strategic significance for India: LVM3 is India's workhorse for: (1) Heavy communication satellites (GSAT series, 4,000+ kg), (2) NISAR Earth observation (launched July 30, 2025 via GSLV-F16), (3) Gaganyaan crewed missions (launching Crew Module + Service Module for 2027 crewed flight). LVM3's proven reliability (10+ consecutive successes) makes it India's most trusted vehicle for high-value payloads. Gaganyaan-4's reliance on LVM3 means mission success depends on flawless LVM3 operations — underscoring the importance of continued reliability validation. For India's commercial launch business, LVM3 offers a niche: heavy-lift to GTO (~$1.5 billion/year market), where India can compete with SpaceX Falcon Heavy ($90M/flight) by offering ~$50-60M equivalent pricing (leveraging cost advantages). LVM3's success validates India's cryogenic technology parity with Russia/France — a strategic achievement.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- NISAR data ---
        {
            "id": 26075,
            "question_text": "NISAR (NASA-ISRO SAR) is designed to observe every part of Earth's surface once every how many days?",
            "option_a": "3 days",
            "option_b": "6 days",
            "option_c": "12 days",
            "option_d": "30 days",
            "correct_answer": "C",
            "explanation": "NISAR's 12-day repeat-pass interval at 747 km altitude allows global coverage with high revisit frequency. This temporal resolution enables: (1) Earthquake deformation mapping (measuring cm-scale ground motion within days of rupture), (2) Landslide detection in monsoon seasons (changes visible every 12 days vs. monthly optical satellites), (3) Glacier/ice-sheet velocity tracking (acceleration/deceleration indicators), (4) Vegetation change monitoring (forest health, crop stress), (5) Water level fluctuations in reservoirs/wetlands. Dual-frequency capability (L-band for deep penetration, S-band for surface detail) provides complementary information — unique to NISAR. Strategic significance for India: India's monsoon-induced disasters (floods, landslides) claim 5,000+ lives annually. NISAR's 12-day revisit frequency is critical for: (1) Landslide forecasting in Western Ghats + Northeast (monsoon season July-September), (2) Flood inundation mapping in Brahmaputra, Ganges (early warnings reduce deaths), (3) Glacier monitoring in Himalayas (tracking water availability for 600 million people downstream). For agriculture, 12-day updates enable crop-loss assessments for crop insurance settlements faster than current 30-60-day cycles. Data-sharing agreements between NASA/ISRO make NISAR data free for Indian scientists — enabling rapid innovation in disaster-response applications. Indian startups can develop NISAR-based services for agriculture/insurance, creating a $200+ million market opportunity.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Shubhanshu Shukla / Axiom-4 ---
        {
            "id": 26076,
            "question_text": "Group Captain Shubhanshu Shukla became the first Indian to board the International Space Station. He was part of which mission?",
            "option_a": "Gaganyaan-1",
            "option_b": "Axiom Mission 3 (Ax-3)",
            "option_c": "Axiom Mission 4 (Ax-4)",
            "option_d": "SpaceX Crew Dragon Demo-2",
            "correct_answer": "C",
            "explanation": "Shubhanshu Shukla (Group Captain, Indian Air Force, selected for Gaganyaan program) flew to ISS aboard SpaceX Crew Dragon (Ax-4 mission, June 25-July 15, 2025). He was the first Indian to board the ISS — a milestone achieved through India's partnership with Axiom Space (commercial ISS access). Commander: Peggy Whitson (former NASA astronaut); crew also included Polish and Hungarian astronauts. Shukla conducted microgravity experiments and EVA (spacewalk) support. Strategic significance for India: This mission serves multiple strategic purposes: (1) Human spaceflight training — Shukla gains direct experience with ISS operations, emergency procedures, microgravity science (relevant for Gaganyaan-4 in 2027), (2) Soft power demonstration — India's presence on ISS reinforces India's status as a spacefaring nation to global audience, (3) Technology validation — Shukla's physiology monitoring via Indian biomedical instruments validates India's life-support monitoring for Gaganyaan, (4) Diplomatic messaging — India's participation in commercial ISS missions signals India's willingness to collaborate with private space companies (Axiom) and US partners, strengthening India-US space cooperation. Axiom missions represent the future of human spaceflight (private commercial stations replacing ISS 2030+) — India's early participation positions Indian astronauts to work on the next-generation space stations Axiom is building.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26077,
            "question_text": "Shubhanshu Shukla became the second Indian to travel to space after a gap of over 40 years. Who was the first Indian to go to space?",
            "option_a": "Sunita Williams",
            "option_b": "Rakesh Sharma",
            "option_c": "Ravish Malhotra",
            "option_d": "K. Kasturirangan",
            "correct_answer": "B",
            "explanation": "Wing Commander Rakesh Sharma (IAF, pilot) flew aboard Soyuz T-11 to the Salyut-7 space station (April 3-11, 1984) during Indo-Soviet cooperation — making India the 14th nation with human spaceflight capability. Sharma orbited Earth 65 times, conducted materials science experiments, and transmitted to India: 'Saare jahan se accha' (best in the world) — a cultural statement. His flight remained India's sole human spaceflight achievement for 41 years. Shubhanshu Shukla's 2025 ISS flight marked India's re-entry into human spaceflight after 4 decades. Strategic significance for India: Sharma's 1984 mission established India's human spaceflight legacy but was followed by a 40-year gap — a loss of momentum and expertise. India's Gaganyaan-4 (2027) will finally achieve independent crewed spaceflight, ending dependence on Russian vehicles. This gap represents India's decades-long struggle to develop indigenous crewed capability — a goal that could have been achieved 20 years earlier with sustained investment. Shukla's Ax-4 mission bridges the gap and positions Gaganyaan-4 as India's triumphant return to human spaceflight autonomy. Commemorating both Sharma (1984) and Shukla (2025) highlights how delayed Gaganyaan development cost India 40 years of scientific opportunity — emphasizing the importance of sustained commitment to India's current space program.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26078,
            "question_text": "The Axiom Mission 4 (Ax-4) crew was commanded by which former NASA astronaut?",
            "option_a": "Scott Kelly",
            "option_b": "Sunita Williams",
            "option_c": "Peggy Whitson",
            "option_d": "Mike Lopez-Alegria",
            "correct_answer": "C",
            "explanation": "Peggy Whitson (NASA veteran, 10 spaceflights, ISS commander experience) commanded Ax-4. Whitson's transition from NASA to Axiom exemplifies the shift toward commercial space stations. Crew composition: Shubhanshu Shukla (India, mission pilot, Gaganyaan astronaut candidate), Sławosz Uznański-Wiśniewski (Poland, ESA, mission specialist), Tibor Kapu (Hungary, ESA, science specialist). International crew reflects the multiparty nature of commercial spaceflight — nations can purchase seats on commercial vehicles without developing independent launchers. Strategic significance for India: Whitson's leadership of an internationally diverse crew (India, Poland, Hungary, USA) models the collaborative spaceflight model of the future. India's Gaganyaan-4 (2027) will carry Indian astronauts in Indian spacecraft, but future crewed missions may involve international partners. Learning from Axiom's operational model (crew rotations, experiment scheduling, emergency procedures) accelerates India's preparation for hosting international astronauts on BAS (2030+). Axiom is building commercial space stations to replace ISS (2030+) — India's presence on Axiom missions positions Indian industry to bid for BAS module construction contracts and service operations. This commercial participation strengthens India's space economy.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26079,
            "question_text": "Shubhanshu Shukla is associated with India's Gaganyaan programme as one of the selected Gaganyatris. How many Gaganyatris (astronaut candidates) were selected for the Gaganyaan programme?",
            "option_a": "Two",
            "option_b": "Three",
            "option_c": "Four",
            "option_d": "Six",
            "correct_answer": "C",
            "explanation": "Four Gaganyatris (Hindi term for Gaganyaan crew members) were selected in June 2019 from Indian Air Force test pilots: (1) Shubhanshu Shukla, (2) Prashanth Balakrishnan Nair, (3) Ajit Krishnan, (4) Angad Pratap. All received training at Yuri Gagarin Cosmonaut Training Center (Russia, 2019-2024) covering: spacecraft systems, emergency procedures, robotics, EVA simulations. Additional training at European Astronaut Centre (ESA, Germany) and Indian institutions (VJTI Mumbai, ISRO). Shukla's Ax-4 flight (June 2025) provided practical ISS experience — unique training unavailable on the ground. Strategic significance for India: Selecting IAF test pilots ensures flight-rated candidates with emergency-response training. The 4-person cohort is strategically sized: (1) two for Gaganyaan-4 crewed mission (2027), (2) backups for Gaganyaan-5 (2028), (3) expansion of India's astronaut corps for BAS operations (2030+). Russia's training (despite geopolitical tensions with West) demonstrates India's strategic partnership with Russia in human spaceflight. However, India should develop indigenous astronaut training facilities to reduce dependence on Russian centers — ISRO should establish a National Astronaut Training Center by 2030. Shukla's Ax-4 participation shows that commercial ISS missions can serve as supplementary training platforms — reducing training costs and accelerating readiness.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26080,
            "question_text": "Axiom Mission 4 (Ax-4) with Shubhanshu Shukla was launched from Kennedy Space Center on June 25, 2025, using which launch vehicle?",
            "option_a": "United Launch Alliance Vulcan",
            "option_b": "Boeing Starliner",
            "option_c": "SpaceX Falcon 9 with Dragon spacecraft",
            "option_d": "NASA SLS",
            "correct_answer": "C",
            "explanation": "Ax-4 launched June 25, 2025 from Kennedy Space Center LC-39A aboard SpaceX Falcon 9. Dragon capsule carried 4 crew to ISS, docking at the Harmony module. The 20-day mission (extended from original 10-day plan) enabled additional experiments and EVA preparation. Splashdown: July 15, 2025 in the Pacific (150 km southwest of San Diego). Dragon auto-abort and splashdown capabilities demonstrate the redundancy of modern crewed spacecraft — critical for crew safety. Strategic significance for India: Axiom's reliable operations (10+ crewed missions) validate SpaceX Dragon as the primary ISS access vehicle (replacing Russian Soyuz for US crews). For India's Gaganyaan-4, SpaceX Dragon serves as a reference design for crew-vehicle interfaces, emergency egress procedures, and splashdown operations. India's Gaganyaan crew module design borrows lessons from Dragon (heat-shield geometry, parachute systems, capsule stability). The July 15 splashdown in the Pacific, 150 km from shore, demonstrates precision landing — India's Gaganyaan-4 targets splashdown in the Bay of Bengal (off Andhra Pradesh coast, ~80 km from shore), requiring similar landing accuracy. India can request splashdown data from SpaceX/NASA to validate Gaganyaan recovery procedures.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # ════════════════════════════════════════════════════════════
        # FRESHNESS GAP-FILL — 2025-26 Sci-Tech (added May 19, 2026)
        # IDs: 26081-26130
        # ════════════════════════════════════════════════════════════
        # --- NASA Artemis-2 (Apr 2-11, 2026) ---
        {
            "id": 26081,
            "question_text": "NASA's Artemis-2 mission, which made history as the first crewed lunar mission since Apollo 17, was launched on which date in 2026?",
            "option_a": "March 14, 2026",
            "option_b": "April 2, 2026",
            "option_c": "April 11, 2026",
            "option_d": "May 5, 2026",
            "correct_answer": "B",
            "explanation": "NASA's Artemis-2 was launched on April 2, 2026 from Kennedy Space Center using the Space Launch System (SLS) rocket and Orion spacecraft. The 10-day crewed lunar flyby mission looped behind the Moon before splashing down successfully on April 11, 2026 in the Pacific Ocean — the first crewed Moon mission since Apollo 17 in December 1972 (54-year gap). Strategic significance for India: Artemis-2's success validates the SLS and Orion for human deep-space missions, paving the way for Artemis-3 (crewed lunar landing, 2027-28). India's Gaganyaan program (crewed missions starting 2027) and planned crewed lunar landing (2040) will benefit from lessons learned from Artemis, particularly in crew safety protocols and life-support systems. India is not a formal Artemis Accords signatory (unlike USA, Australia, Japan), but the success of Artemis demonstrates the feasibility of India's lunar ambitions. India's participation in international crewed lunar base planning (post-2035) becomes more credible following Artemis success. For India's domestic program, Artemis-2 validates that crewed deep-space missions are achievable; ISRO can accelerate Gaganyaan crewed Moon mission planning with confidence in proven technologies.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26082,
            "question_text": "Artemis-2 carried four astronauts on a lunar flyby. The mission set a new distance record by travelling how far from Earth?",
            "option_a": "1,52,760 miles",
            "option_b": "2,52,760 miles",
            "option_c": "3,52,760 miles",
            "option_d": "4,52,760 miles",
            "correct_answer": "B",
            "explanation": "Artemis-2 travelled 2,52,760 miles (406,800 km) from Earth during its lunar flyby — a new record for the farthest distance ever travelled by humans, surpassing Apollo 13's 1970 record of 248,655 miles. The crew: Reid Wiseman (Commander, NASA, 4 ISS missions), Victor Glover (Pilot, NASA, 1 ISS mission), Christina Koch (Mission Specialist, NASA, 1 ISS + 1 Axiom-2 commercial mission), and Jeremy Hansen (Mission Specialist, CSA — first Canadian to fly to the Moon). Strategic significance for India: The Artemis-2 crew composition reflects NASA's commitment to diversity and international cooperation. India's Gaganyaan crewed program should similarly embrace international cooperation; discussions with France (CNES), Japan (JAXA), and Russia (Roscosmos) on joint crewed missions would strengthen India's position as a spacefaring nation. The record distance traveled (252,760 miles) demonstrates human capability to venture beyond LEO safely — validating ISRO's ambition for crewed Moon missions. India's BAS (launching 2028) will eventually support crewed deep-space missions from an orbital platform, similar to how Artemis missions use lunar gateway stations.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26083,
            "question_text": "Which Canadian astronaut on Artemis-2 became the first non-American to fly to the Moon?",
            "option_a": "Chris Hadfield",
            "option_b": "Jeremy Hansen",
            "option_c": "David Saint-Jacques",
            "option_d": "Joshua Kutryk",
            "correct_answer": "B",
            "explanation": "Jeremy Hansen (CSA) became the first non-American (and first Canadian) to fly to the Moon aboard Artemis-2. Hansen is a former Royal Canadian Air Force fighter pilot with 0 prior spaceflights — a symbolic choice representing the next generation of international astronauts. His selection on the Artemis-2 crew (announced Dec 2022) signaled NASA's commitment to international partnerships in deep-space exploration. Strategic significance for India: Jeremy Hansen's participation exemplifies how nations without independent human spaceflight can still participate in deep-space exploration through partnerships (CSA with NASA). India has three pathways: (1) Independent crewed Moon landing (Gaganyaan evolution to lunar lander, targeted post-2040), (2) Partnership with international programs (joining Artemis Accords, bidding to contribute crew to NASA lunar missions), (3) Commercial partnerships (Indian astronauts contracting with SpaceX/Axiom for deep-space missions post-2030). India's Gaganyaan-4 (2027) validates independent crewed capability, enabling India to negotiate as an equal with NASA on international partnerships. Hansen's success on Artemis-2 demonstrates that non-Apollo nations can participate in lunar exploration — opening opportunities for India to claim a Canadian-like partnership role in future lunar base operations (2035+), where India could contribute modules/services while Canadian/Indian crews participate.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- ISRO BlueBird Block-2 / LVM3-M6 (Dec 24, 2025) ---
        {
            "id": 26084,
            "question_text": "ISRO's LVM3-M6 mission launched on December 24, 2025 from Sriharikota was historic for which reason?",
            "option_a": "First Indian lunar sample-return mission",
            "option_b": "100th launch from Satish Dhawan Space Centre, SHAR, carrying the heaviest commercial payload",
            "option_c": "First indigenous reusable launch vehicle test",
            "option_d": "First Indian astronaut training flight",
            "correct_answer": "B",
            "explanation": "LVM3-M6 (Launch Vehicle Mark 3 Mission 6) on December 24, 2025 marked SHAR's centennial achievement — 100 launches from India's primary spaceport since 1980 (starting with SLV-3 launch of Rohini satellite). The payload: AST SpaceMobile's BlueBird Block-2 (6,500 kg) — the heaviest commercial payload in ISRO's history, surpassing the previous record of ~5,600 kg. BlueBird Block-2 deploys a 64-square-meter phased-array antenna for direct-to-smartphone 5G connectivity from space — bypassing traditional ground infrastructure (critical for remote/maritime regions). Strategic significance for India: SHAR's 100-launch milestone represents 45 years of continuous spaceflight operations — a testament to India's space infrastructure resilience. The centennial launch demonstrates SHAR's commercial reliability to international customers (AST SpaceMobile contracted ISRO for exclusive access). For India's economy: launching the heaviest commercial payload validates India's lift capacity to GTO and attracts more commercial customers. NSIL (ISRO's commercial arm) can leverage this achievement to market LVM3 for heavy-lift missions to international operators. BlueBird Block-2's direct-to-cell capability addresses a market gap — SpaceX Starlink focuses on broadband, while AST/BlueBird target smartphone connectivity. India's participation in this emerging market positions Indian startups to develop complementary services (ground hubs, network operations). The 100th-launch celebration underscores India's space program maturity — comparable to major space powers.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26085,
            "question_text": "The BlueBird Block-2 satellite launched by ISRO's LVM3-M6 in December 2025 was built by which company?",
            "option_a": "SpaceX (USA)",
            "option_b": "AST SpaceMobile (USA)",
            "option_c": "OneWeb (UK)",
            "option_d": "Eutelsat (France)",
            "correct_answer": "B",
            "explanation": "AST SpaceMobile (founded 2017, USA-based) developed BlueBird Block-2 as a direct-to-device satellite — equipped with a 64-square-meter phased-array antenna operating in cellular bands (LTE/5G). The satellite connects unmodified smartphones via a space-based network, eliminating need for cell towers. NSIL (New Space India Limited, ISRO's commercial wing) negotiated the launch contract (worth Rs 115 crore, ~$14 million). Strategic significance for India: AST SpaceMobile's success validates the market for satellite connectivity — a domain where SpaceX Starlink (broadband to terminals) dominates, but direct-to-phone satellite services are nascent. India's OneWeb constellation (now Bharti Group, 400+ satellites in orbit by 2026) provides broadband; complementary direct-to-phone satellite services could enable India to capture the $50 billion satellite telecommunications market. For India's remote regions (Northeast, tribal areas with poor cellular coverage), direct-to-phone satellites provide basic connectivity without infrastructure investment. India's startups (TrustComm, Aryan Space) are developing similar direct-to-device satellites — learning from AST's pioneer efforts. NSIL's commercial contract with AST demonstrates India's willingness to host foreign satellites — building NSIL's reputation as a reliable launch provider. This commercial relationship strengthens India's space industry for the competitive 2030+ era.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- NavIC-16 / IRNSS-1K (GSLV-F15 Jan 2026) ---
        {
            "id": 26086,
            "question_text": "ISRO launched the NavIC navigation satellite NVS-02/IRNSS-1K (also called NavIC-16) on January 29, 2025 using which launch vehicle?",
            "option_a": "PSLV-C58",
            "option_b": "GSLV-F15",
            "option_c": "LVM3-M5",
            "option_d": "SSLV-D3",
            "correct_answer": "B",
            "explanation": "GSLV-F15 launched NVS-02 (NavIC-16) on January 29, 2025 from SHAR into a geostationary orbit at 83°E longitude. NVS-02 is the 8th operational NavIC satellite (constellation target: 9 satellites — 3 geostationary, 6 in inclined geosynchronous orbits). NavIC (Navigation with Indian Constellation) provides positioning/timing accuracy of: (1) 5-10 meters horizontal (vs. GPS's 5-20m), (2) 10-20 nanoseconds timing, covering India and 1,500 km around it. Strategic significance for India: NavIC independence from GPS is critical for India's: (1) Military applications — avoiding US denial (GPS can be jammed/denied in conflict scenarios), (2) Agriculture — precision farming (1-meter accuracy with SBAS augmentation) for 160 million farmers, (3) Autonomous vehicles — self-driving cars require Indian positioning to avoid GPS vulnerabilities, (4) Disaster management — NDMA relies on Indian positioning for flood/earthquake response. With NVS-02, NavIC achieves 8/9 operational capacity — full constellation (2026) ensures continuous coverage (minimum 4-satellite visibility across India). India's SBAS (Satellite Based Augmentation System) augmentation will enable meter-level accuracy by 2027 — supporting autonomous driving in India. NavIC's success validates India's space self-reliance strategy — an essential national capability for a nation of India's size and geopolitical standing.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Bharatiya Antariksh Station (BAS) ---
        {
            "id": 26087,
            "question_text": "The Bharatiya Antariksh Station (BAS), India's planned indigenous space station, will consist of how many modules in its final configuration?",
            "option_a": "3 modules",
            "option_b": "4 modules",
            "option_c": "5 modules",
            "option_d": "6 modules",
            "correct_answer": "C",
            "explanation": "Bharatiya Antariksh Station (BAS) comprises 5 modules in final configuration: (1) Core module (power, propulsion, docking hub), (2-5) Specialized modules (materials science, life sciences, Earth observation, experiments). Modular design enables phased assembly: BAS-1 (core module, 2028) + 4 additional modules (2028-35). Total mass: ~52 tonnes; orbit: 400 km at 51° inclination; crew capacity: 3-4. Strategic significance for India: (1) ISS Independence — India exits ISS co-dependency; operations autonomous from Russian/US partners, (2) Microgravity R&D — pharmaceutical crystallization, semiconductor manufacturing, advanced materials testing (50+ startups bidding for BAS experiments), (3) Space tourism — commercial module enables private astronaut visits (potential $50 billion market), (4) Regional hub — SAARC nations (Bangladesh, Sri Lanka, Nepal) can contribute experiments, building India's diplomatic influence, (5) Deep-space platform — BAS orbital docking/refueling capability supports crewed lunar missions (2040+), (6) Defense applications — Earth observation, signal intelligence, anti-satellite testing (covert military dimension). BAS represents India's aspiration to join USA, Russia, China as independent space station operators. Success by 2035 cements India's status as a spacefaring superpower and enables India to lead international space station networks post-2050.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26088,
            "question_text": "The first module of the Bharatiya Antariksh Station (BAS-1) is targeted to be launched by ISRO in which year?",
            "option_a": "2026",
            "option_b": "2027",
            "option_c": "2028",
            "option_d": "2030",
            "correct_answer": "C",
            "explanation": "BAS-1 (core module) launch targeted for 2028 via 2x LVM3 launches: (1) BAS-1 core module injection to 400 km orbit, (2) Propulsion module for orbit maintenance and crew transfer. Module mass: ~20 tonnes; orbital assembly timeline: 2028-35 (one module every 1-2 years). Approval timeline: September 18, 2024 (Union Cabinet approval); estimated cost Rs 10,000 crore (~$1.2 billion, excluding operational costs). Strategic roadmap: (1) Gaganyaan-4 crewed (2027), (2) BAS-1 orbit (2028), (3) ISS crew exchange missions 2028-2035 (using BAS as stepping stone), (4) Full BAS constellation (5 modules, 2035), (5) Crewed Moon landing (2040). Strategic significance for India: The 2028 BAS-1 launch is critical — it demonstrates India's crewed space infrastructure transition from single-mission (Gaganyaan-4) to sustained operations (ISS-like). The 2027 Gaganyaan-4 → 2028 BAS-1 sequence (back-to-back crewed missions) tests India's launch/recovery infrastructure intensively — accelerating operational learning. ISS partnership during 2028-2035 provides knowledge transfer as ISS deorbits (planned ~2030-2032); India takes over ISS research continuity via BAS. This transition cements India's status as an independent, self-reliant spacefaring nation — comparable to Russia's Mir program capability.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Chandrayaan-4 ---
        {
            "id": 26089,
            "question_text": "Chandrayaan-4, approved by the Union Cabinet, is designed to demonstrate which capability?",
            "option_a": "First crewed Indian Moon landing",
            "option_b": "Lunar sample return to Earth",
            "option_c": "Permanent base on the lunar south pole",
            "option_d": "Lunar farside soft landing",
            "correct_answer": "B",
            "explanation": "Chandrayaan-4 was approved by the Union Cabinet on September 18, 2024 with a budget of Rs 2,104 crore (~$250M). It will demonstrate lunar sample-return technology — collecting 3-5 kg samples from the Moon's south polar region (near Chandrayaan-3 landing site in Aitken Basin) and returning them to Earth. The mission has a complex 5-module architecture (Orbiter, Lander, Ascender, Propulsion Module, Earth Return Module) launched on two separate LVM3 rockets and is targeted for 2027-28. Strategic significance for India: Chandrayaan-4 is a major technology leap — only 3 countries (US Apollo program, USSR Luna 20/24) have successfully returned lunar samples to Earth. India's successful Chandrayaan-4 would position India as the 4th nation with sample-return capability. The mission demonstrates: (1) Rocket-powered lunar ascent (launching from Moon's surface), (2) In-space spacecraft rendezvous and docking, (3) Trans-lunar return trajectory with re-entry and landing, (4) Life support for samples during 3+ day return journey. For India's scientific goals: Chandrayaan-4 samples will reveal water ice concentration, mineral composition, and volatiles in lunar south pole — critical for establishing permanent lunar base (Bharatiya Lunar Station, planned 2035+). For India's global positioning: Sample-return success validates India's technological sophistication and attracts international partnerships (US, Japan, France joint sample analysis). This supports India's crewed Moon landing ambitions (Gaganyaan astronauts to Moon by 2040) and deep-space exploration roadmap (Mars-3 lander, Venus missions).",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- SpaceX Starship IFT-9 to IFT-12 ---
        {
            "id": 26090,
            "question_text": "SpaceX successfully completed the maiden Starship Block-3 orbital test (IFT-12) in 2025. The Starship is the world's most powerful rocket — how tall does the full Super Heavy + Starship stack measure?",
            "option_a": "~100 metres",
            "option_b": "~120 metres",
            "option_c": "~150 metres",
            "option_d": "~200 metres",
            "correct_answer": "B",
            "explanation": "The full SpaceX Super Heavy + Starship stack measures approximately 120 metres (395 feet) — the world's tallest and most powerful rocket ever built, generating ~740 meganewtons (MN) of thrust at lift-off from 33 Raptor 3 engines (Super Heavy first stage) and 6 Raptor 3 vacuum engines (Starship upper stage). Total payload capacity: 150 tonnes to LEO, 50 tonnes to Mars. IFT-7, 8, and 9 experienced mid-flight failures (early 2025), but SpaceX achieved critical milestones: Booster catch with the launch tower's 'Mechazilla' robotic chopsticks and successful Starship upper-stage orbital coast, deorbit, and splashdown through IFT-11 and IFT-12 (late 2025/early 2026). Strategic significance for India: SpaceX's rapid iteration approach (7 orbital tests within 18 months) demonstrates cost-effective innovation through vertical integration and reusability. ISRO's approach is traditionally more conservative (rigorous testing on ground before flight), but ISRO's partnership with Indian startups (Agnikul, Skyroot) can adopt SpaceX's philosophy of learning from flight tests. Starship's 150-tonne LEO capacity vastly exceeds NGLV's projected 10-12 tonnes to GTO; India cannot compete on cost per kg with Starship, but can target: (1) Niche markets (small dedicated launches from Indian spaceport), (2) Government captive launches (ISRO, military), (3) Technology transfer to startups enabling India's reusable rocket ecosystem. Starship's success also emphasizes the urgency of India's NGLV development — without cost-competitive launch services, India risks losing commercial launch market share to SpaceX.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- IBM Quantum System Two / Heron R2 / Amaravati ---
        {
            "id": 26091,
            "question_text": "Andhra Pradesh inaugurated the Amaravati Quantum Computing Centre (AQCC) in January 2026. Which quantum processor does it host?",
            "option_a": "Google Willow (105-qubit)",
            "option_b": "IBM Quantum System Two with Heron R2 (156-qubit)",
            "option_c": "IonQ Forte (32-qubit)",
            "option_d": "Microsoft Majorana 1",
            "correct_answer": "B",
            "explanation": "The Amaravati Quantum Computing Centre (AQCC), inaugurated by the Andhra Pradesh government in January 2026 as the flagship of the 'Quantum Valley' initiative, hosts IBM's Quantum System Two with the 156-qubit Heron R2 processor — the world's largest quantum computer deployed outside the USA. Heron R2 features: improved qubit quality (error rates <0.1%), 3-layer qubit topology enabling higher gate fidelities, modular architecture supporting scaling to 1,000+ qubits. Strategic significance for India: (1) National Quantum Mission (₹6,000 crore, 2023-2032) targets Indian-made quantum chips by 2031; AQCC accelerates this timeline via open-access research, (2) Global quantum race: Google's Willow (105-qubit, error correction breakthrough Dec 2024) vs Microsoft's topological Majorana 1 vs China's Jiuzhang 2.0 (photonic) — India's Heron R2 positions India as a top-5 quantum player, (3) Applications focus: drug discovery (pharma R&D relevant for India's $50B pharma industry), cryptography (Indian financial systems, defense), optimization (logistics for India's 1.4B population supply chains), (4) Public access model (IBM partnership) enables startups (TCS, Infosys) to develop quantum algorithms — key to India's Q-advantage roadmap. Andhra Pradesh's tech ecosystem (already hosting IIIT Hyderabad, T-Hub innovation hub) positions the state as India's quantum innovation hub — attracting global quantum talent and companies.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 26092,
            "question_text": "IBM's Heron R2 processor, deployed at the Amaravati Quantum Computing Centre, has how many qubits?",
            "option_a": "127 qubits",
            "option_b": "133 qubits",
            "option_c": "156 qubits",
            "option_d": "1,121 qubits",
            "correct_answer": "C",
            "explanation": "IBM's Heron R2 processor has 156 qubits, an upgraded version of the earlier 133-qubit Heron R1. It powers IBM Quantum System Two, which is now operational at the Amaravati Quantum Computing Centre (AQCC) — part of Andhra Pradesh's 'Quantum Valley' initiative announced in 2025.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Nobel Physics 2025 ---
        {
            "id": 26093,
            "question_text": "The 2025 Nobel Prize in Physics was awarded jointly to John Clarke, Michel Devoret and John Martinis for their discovery of which quantum phenomenon?",
            "option_a": "Topological phases of matter",
            "option_b": "Macroscopic quantum mechanical tunnelling and energy quantisation in an electric circuit",
            "option_c": "Quantum entanglement in photons",
            "option_d": "Boson-Higgs mechanism",
            "correct_answer": "B",
            "explanation": "The 2025 Nobel Prize in Physics was awarded jointly to John Clarke (UK/US), Michel H. Devoret (France/US) and John M. Martinis (US) for discoveries concerning macroscopic quantum mechanical tunnelling and energy quantisation in superconducting circuits. Their work on Josephson junctions and superconducting qubits (1980s-2000s) laid the foundation for modern quantum computing. Clarke developed techniques to observe quantum tunnelling in macroscopic systems; Devoret and Martinis demonstrated how to control and measure superconducting qubits with unprecedented precision. This breakthrough enabled: (1) Quantum error correction concepts (essential for scaled quantum computers), (2) IBM and Google's superconducting qubit architectures (Heron, Willow), (3) Quantum supremacy demonstrations (Google's 2019 claim). Strategic significance for India: The Nobel recognition underscores superconducting qubits as the dominant quantum computing platform globally. India's National Quantum Mission emphasizes superconducting qubits for indigenous development; Indian institutions (IIT-B, IISER Pune) are collaborating with IBM and Microsoft on quantum computing research. Indian researchers can leverage Clarke-Devoret-Martinis publications to accelerate India's quantum chip development. The Amaravati Quantum Computing Centre's Heron R2 directly benefits from 40 years of superconducting qubit innovation recognized by this Nobel Prize — validating India's strategic choice of superconducting technology.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Nobel Chemistry 2025 ---
        {
            "id": 26094,
            "question_text": "The 2025 Nobel Prize in Chemistry was awarded to Susumu Kitagawa, Richard Robson and Omar Yaghi for developing what?",
            "option_a": "CRISPR/Cas9 gene editing",
            "option_b": "Lithium-ion batteries",
            "option_c": "Metal-Organic Frameworks (MOFs)",
            "option_d": "Click chemistry",
            "correct_answer": "C",
            "explanation": "The 2025 Nobel Prize in Chemistry was awarded jointly to Susumu Kitagawa (Japan), Richard Robson (UK/Australia), and Omar M. Yaghi (Jordan/US) for the development and study of Metal-Organic Frameworks (MOFs). MOFs are crystalline materials composed of organic ligands coordinated to metal centers, creating highly porous structures with specific surface areas up to 7,000 m²/g (vs. activated charcoal at 3,000 m²/g). Applications: (1) Carbon capture (direct air capture of CO2 for climate mitigation), (2) Hydrogen storage (critical for fuel-cell vehicles), (3) Water harvesting from desert air (humanitarian applications), (4) Selective gas separations, (5) Drug delivery in biomedical applications. Strategic significance for India: India's climate target (Net-Zero by 2070) requires carbon capture technologies; MOFs offer a potential solution for direct air capture from India's coal-fired power plants and cement industries (major CO2 emitters). India's mining industry generates waste (high-surface-area minerals) that could be functionalized as MOF precursors — supporting circular economy goals. Indian research institutions (CSIR, IIT-B, IISc) are exploring MOF synthesis for water harvesting in arid regions (Rajasthan, Gujarat) — a climate adaptation strategy crucial for India's water security. The Nobel Prize recognition accelerates India's MOF research funding and attracts global collaborations in materials science.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Nobel Medicine 2025 ---
        {
            "id": 26095,
            "question_text": "The 2025 Nobel Prize in Physiology or Medicine was awarded for discoveries about which immunological concept?",
            "option_a": "mRNA vaccines",
            "option_b": "Peripheral immune tolerance",
            "option_c": "CAR-T cell therapy",
            "option_d": "Innate immunity Toll-like receptors",
            "correct_answer": "B",
            "explanation": "The 2025 Nobel Prize in Physiology or Medicine was awarded jointly to Mary E. Brunkow (US), Fred Ramsdell (US), and Shimon Sakaguchi (Japan) for discoveries concerning peripheral immune tolerance and regulatory T cells (Tregs). They identified the FOXP3 gene as the master regulator of Treg development and function. Tregs are specialized immune cells that suppress autoimmune responses, preventing the immune system from attacking the body's own tissues. Their breakthrough revealed the molecular basis of immune self-tolerance — critical for understanding: (1) Autoimmune diseases (Multiple Sclerosis, Rheumatoid Arthritis, Type-1 Diabetes), (2) Transplant rejection (preventing Treg suppression of donor-specific immunity), (3) Cancer immunotherapy (Treg depletion enhancing anti-tumor immunity). Strategic significance for India: Autoimmune diseases are rising in India (MS ~40,000 cases, RA ~6 million cases) as urbanization increases. The Brunkow-Ramsdell-Sakaguchi discoveries enable development of Treg-based therapies tailored to Indian patient populations. India's biotech industry (Biocon, Dr. Reddy's, Cipla) can develop Treg-engineering therapies (ex-vivo Treg expansion for autoimmune patients). CSIR, IIT-B, and AIIMS are advancing Treg immunology research leveraging this Nobel-recognized framework. The discovery also supports India's vaccine development expertise — understanding Treg biology improves vaccine design to avoid autoimmune side-effects in India's immunization programs.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- OpenAI GPT-5 ---
        {
            "id": 26096,
            "question_text": "OpenAI released GPT-5, its new flagship reasoning model, in which month and year?",
            "option_a": "April 2025",
            "option_b": "August 2025",
            "option_c": "December 2025",
            "option_d": "January 2026",
            "correct_answer": "B",
            "explanation": "OpenAI released GPT-5 on August 7, 2025, introducing several advancements: unified-reasoning (combining analytical and creative thinking), native multimodal input (text, images, audio, video simultaneously), and a Pro tier for extended thinking on complex problems. GPT-5 replaces GPT-4o and the o-series as ChatGPT's default model, representing a 30% improvement in reasoning accuracy over GPT-4o Turbo. Architecture: 140-billion parameter scale (estimated), trained on 2024 diverse datasets including scientific literature, code repositories, and web content. Strategic significance for India: GPT-5's release intensifies the global AI arms race — India's IndiaAI Mission aims to develop BharatGen (sovereign LLM) by 2026-27 to reduce dependence on OpenAI. DeepSeek's R1 (January 2025, cost-effective alternative) demonstrated that high-performance reasoning models can be built outside the USA; India's opportunity is to develop LLMs optimized for Indian languages (Hindi, Tamil, Telugu, Marathi) and use-cases (government, healthcare, agriculture). Indian startups (Matic, Arpit.AI) are building domain-specific LLMs for legal and financial services — an incremental path rather than competing with GPT-5 directly. India's AI strategy should focus on: (1) Foundation models for Indian languages, (2) Federated learning for privacy-preserving AI, (3) Edge AI deployment for offline capabilities in rural India.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Google Gemini 3.0 ---
        {
            "id": 26097,
            "question_text": "Google DeepMind released Gemini 3.0, its most advanced AI model, in which month of 2025?",
            "option_a": "March 2025",
            "option_b": "August 2025",
            "option_c": "October 2025",
            "option_d": "December 2025",
            "correct_answer": "D",
            "explanation": "Google DeepMind released Gemini 3.0 (Gemini 3 Pro and Gemini 3 Ultra variants) in November-December 2025 as its most capable multimodal foundation model. Key features: (1) Native agentic capabilities (can plan and execute multi-step tasks autonomously), (2) 1-million-token context window (vs. GPT-4's 128k, enabling entire book/codebase analysis), (3) Antigravity agent IDE (integrated development environment for building autonomous AI agents), (4) Superior reasoning on mathematical, scientific, and coding tasks. Gemini 3.0 powers Google Search's AI Mode and AI Studio (professional creative tools). Strategic significance for India: Google's Gemini models are available globally via API; Indian developers and enterprises using Gemini 3.0 gain access to frontier AI capabilities for: (1) Drug discovery (Indian pharma companies using Gemini for molecular simulations), (2) Climate modeling (supporting India's Net-Zero 2070 commitments), (3) Code generation (accelerating India's software services exports). However, India's sovereign AI strategy requires indigenous models. India's BharatGen LLM project aims to achieve Gemini-3-level capabilities by 2027-28. Indian researchers participating in Google-CSIR-IISc collaborations on LLM research accelerate India's AI expertise building — a pathway to eventual independence from external foundation models.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- DeepSeek R1 ---
        {
            "id": 26098,
            "question_text": "DeepSeek R1, the open-source reasoning AI model released in January 2025 that triggered a global AI stock-market reaction, was developed by a company from which country?",
            "option_a": "USA",
            "option_b": "China",
            "option_c": "South Korea",
            "option_d": "India",
            "correct_answer": "B",
            "explanation": "DeepSeek R1 was released on January 20, 2025 by DeepSeek, a Hangzhou-based Chinese AI company (founded 2023 by Liang Wenfeng). The open-source reasoning model achieved performance comparable to OpenAI's o1 on benchmark tests (AIME, MATH) using only 671 billion training tokens (vs. o1's estimated 2 trillion+) and ~$5-6 million in training compute costs (vs. o1's estimated $100+ million). This efficiency demonstrated that high-performance reasoning models could be developed without the massive capital budgets dominant in Silicon Valley. Market impact: The 'DeepSeek shock' on January 27, 2025 triggered an ~$1 trillion drop in US tech stocks; NVIDIA lost $600 billion alone as markets reassessed AI scaling costs. Strategic significance for India: DeepSeek's efficiency-first approach validates India's opportunity to develop indigenous LLMs through: (1) Algorithmic innovation (distillation, sparse training, mixture-of-experts) rather than brute-force scaling, (2) Cost-effective compute (leveraging India's computing infrastructure and talent advantages), (3) Open-source philosophy (DeepSeek released R1 model weights openly, accelerating global collaboration). India's BharatGen project should study DeepSeek's architecture; Indian startups (Yext, Arpit AI) can build specialized reasoning models for Indian use-cases without competing on pure scale. China's success with DeepSeek emphasizes India's urgency — India has 6-12 months to establish credible indigenous reasoning capability before the AI capability gap widens further.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Anthropic Claude Opus 4 ---
        {
            "id": 26099,
            "question_text": "Anthropic, the US AI safety company, released Claude Opus 4 — its most capable model — in which month of 2025?",
            "option_a": "March 2025",
            "option_b": "May 2025",
            "option_c": "August 2025",
            "option_d": "November 2025",
            "correct_answer": "B",
            "explanation": "Anthropic released Claude Opus 4 in May 2025 as the most capable model in the Claude family. Key capabilities: (1) Leading-edge reasoning and mathematical problem-solving, (2) Extended thinking mode (internal reasoning before generating output), (3) Hybrid reasoning (combining fast and extended modes), (4) Superior coding assistance (GitHub Copilot alternative), (5) Agentic capabilities (autonomous task execution). Claude Opus 4.5 followed in late 2025 with multi-document analysis and improved cost-efficiency. Architecture: ~400 billion parameter scale (estimated), trained on curated high-quality data emphasizing safety and factuality. Constitutional AI framework (feedback from human raters and AI critique) emphasizes ethical behavior. Strategic significance for India: Anthropic's focus on AI safety and explainability aligns with India's responsible AI framework. India's proposed AI Bill (2024-25) emphasizes transparency and human oversight — areas where Anthropic's Claude models excel compared to pure capability-focused competitors. Indian enterprises (TCS, Infosys, HCL) using Claude for customer service and coding gain access to safety-aligned AI. However, India remains dependent on US-based models; India's sovereign AI strategy should integrate Anthropic's safety principles into BharatGen development. Anthropic's research partnerships with universities (including potential collaborations with IIT-B, IISER) accelerate India's AI safety research — a differentiator for India's LLMs.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Nobel Prize Physics 2025 ---
        {
            "id": 26100,
            "question_text": "The Nobel Prize in Physics 2025 was awarded to John Clauser, Alain Aspect, and Anton Zeilinger for which breakthrough in quantum mechanics?",
            "option_a": "Demonstration of quantum entanglement and Bell inequality violation",
            "option_b": "Invention of the quantum computer",
            "option_c": "Discovery of macroscopic quantum tunnelling in superconductors",
            "option_d": "Development of quantum cryptography protocols",
            "correct_answer": "A",
            "explanation": "The 2025 Nobel Prize in Physics recognized Clauser, Aspect, and Zeilinger for their experimental work on quantum entanglement and Bell's theorem. Their experiments provided definitive proof that quantum mechanics violates local realism — a fundamental assumption of classical physics. This validated Einstein's 'spooky action at a distance' and enabled quantum information science, quantum computing, and quantum cryptography. Significance for India: IISc Bangalore and IIT Bombay have active quantum entanglement research groups. India's National Quantum Mission (2023-31) depends on this fundamental science. Indian physicists (including work at Raja Ramanna Centre for Advanced Technology, Indore) contribute to quantum experiments relevant to quantum sensors and atomic clocks — enabling applications in precision navigation, geophysical surveys, and defense systems critical for India's strategic autonomy.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Nobel Prize Chemistry 2025 ---
        {
            "id": 26101,
            "question_text": "The Nobel Prize in Chemistry 2025 was awarded to Shoichi Yamaguchi, Omar Farha, and Henry Rzepa for groundbreaking work on which materials platform?",
            "option_a": "Metal-Organic Frameworks (MOFs)",
            "option_b": "Covalent-Organic Frameworks (COFs)",
            "option_c": "Graphene and 2D materials",
            "option_d": "Perovskites for solar cells",
            "correct_answer": "A",
            "explanation": "The 2025 Nobel Prize in Chemistry recognized advances in Metal-Organic Frameworks (MOFs) — crystalline materials with metal ions linked by organic ligands forming porous structures with applications in gas storage, carbon capture, catalysis, and drug delivery. MOFs represent a paradigm shift in materials chemistry by combining the regularity of inorganic crystals with the versatility of organic chemistry. Strategic significance for India: Carbon capture using MOFs aligns with India's climate commitments (net-zero by 2070). IIT Delhi, IISc Bangalore, and CSIR-IICT Hyderabad conduct MOF research for: (1) CO2 capture from ambient air (Direct Air Capture — DAC, critical for coal-power-plant emission control and cement industry decarbonization), (2) Hydrogen storage for fuel-cell vehicles (alternative to fossil fuels), (3) Pharmaceutical applications (drug purification, controlled delivery for cancer treatment). India's domestic MOF manufacturing capability reduces import dependency on American and European suppliers.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Nobel Prize Medicine 2025 ---
        {
            "id": 26102,
            "question_text": "The Nobel Prize in Physiology or Medicine 2025 was awarded for discoveries in immune tolerance, specifically regarding which regulatory T cell pathway?",
            "option_a": "Programmed Cell Death protein-1 (PD-1) checkpoint",
            "option_b": "Cytotoxic T-Lymphocyte Antigen 4 (CTLA-4) pathway",
            "option_c": "Foxp3+ regulatory T cell (Treg) development and function",
            "option_d": "Interleukin-2 (IL-2) signaling in immune suppression",
            "correct_answer": "C",
            "explanation": "The 2025 Nobel Prize in Medicine recognized discoveries in peripheral immune tolerance, particularly the development and function of regulatory T cells (Tregs). Tregs — cells expressing the Foxp3 transcription factor — suppress inflammatory responses and maintain immune homeostasis. Understanding Treg biology enables therapeutic targeting: (1) Enhanced Tregs suppress autoimmune disease (lupus, rheumatoid arthritis, Crohn's disease), (2) Reduced Tregs in cancer enable checkpoint inhibitor therapies. Significance for India: India bears a high burden of autoimmune disease and cancer. IIT Bombay and AIIMS Delhi research Treg-modulating therapies for Indian patients. India's biopharmaceutical industry (CIPLA, Lupin, Sun Pharma) developing low-cost immunomodulatory drugs for treating autoimmune conditions endemic in India (leprosy-associated immunological reactions, tuberculosis-associated immunosuppression). Therapeutic Treg expansion offers a precision-medicine pathway aligned with India's Ayushman Bharat initiative for preventive health.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- AlphaFold 3 protein structure prediction ---
        {
            "id": 26103,
            "question_text": "DeepMind released AlphaFold 3 in May 2024, which advanced protein structure prediction to predict structures of what types of biological complexes?",
            "option_a": "Only protein-protein complexes",
            "option_b": "Proteins and nucleic acids (DNA/RNA), plus protein-ligand interactions",
            "option_c": "Membrane proteins exclusively",
            "option_d": "Unfolded proteins in the endoplasmic reticulum",
            "correct_answer": "B",
            "explanation": "AlphaFold 3 (May 2024) expanded beyond protein-only structure prediction to model: (1) Protein-protein interactions (antibody-antigen complexes), (2) Protein-DNA/RNA interactions (transcription factor binding sites), (3) Protein-ligand interactions (drug binding to enzymes), (4) RNA structure (secondary and tertiary), (5) Entire cellular complexes (ribosome, spliceosome-like structures). The model operates at atomic resolution with ~70% accuracy on experimental structures. Strategic significance for India: AlphaFold 3 accelerates drug discovery for Indian-disease targets — malaria, dengue, tuberculosis. IISc Bangalore and IGIB (Institute of Genomics and Integrative Biology, Delhi) use AlphaFold 3 to design: (1) Antimalarial compounds targeting Plasmodium falciparum — endemic in India, (2) Antituberculosis agents against drug-resistant TB (MDR-TB, XDR-TB prevalent in India), (3) Dengue NS5 protease inhibitors. India's biopharmaceutical sector (Aurigene, Lupin, Cipla) leveraging AlphaFold for in-silico drug design reduces time-to-market for affordable treatments addressing India's disease burden.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- CRISPR Casgevy & Gene Therapy Approvals ---
        {
            "id": 26104,
            "question_text": "CRISPR Therapeutics and Vertex Pharmaceuticals' CRISPR Casgevy received FDA approval in December 2023 for treating which genetic blood disorders?",
            "option_a": "Haemophilia A and B",
            "option_b": "Sickle cell disease and transfusion-dependent beta-thalassemia",
            "option_c": "Duchenne muscular dystrophy and spinal muscular atrophy",
            "option_d": "Cystic fibrosis and hemochromatosis",
            "correct_answer": "B",
            "explanation": "CRISPR Casgevy (exagamglogene autotemcel, brand: Casgevy) received FDA approval on December 8, 2023 for: (1) Severe sickle cell disease (SCD) — causing chronic pain, organ damage, early mortality, (2) Transfusion-dependent beta-thalassemia (TDT) — requiring life-long blood transfusions. The CRISPR-Cas9 gene-editing therapy removes patient haematopoietic stem cells, edits the BCL11A gene (fetal haemoglobin regulator) to increase fetal haemoglobin production, and reinfuses edited cells. Clinical trials showed 95% pain-crisis-free rates in SCD patients. Cost: $2-3 million per treatment in the US — highlighting the affordability challenge for India. Strategic significance for India: Sickle cell disease (HbS) affects 30 million Indians, concentrated in tribal and SC/ST populations (Odisha, Chhattisgarh, Maharashtra). Beta-thalassemia major affects ~100,000 Indians requiring monthly transfusions. India lacks affordable CRISPR therapies; importing Casgevy costs $2-3 million per patient — unrealistic for India's public health budget. India's opportunity: (1) Localize CRISPR technology — ICMR and IISc scaling cost to <Rs 10 lakh per patient via PPP models, (2) National gene therapy registry under DrugBank portal for real-world efficacy tracking, (3) Public awareness in high-SCD-prevalence districts (tribal areas) about genetic screening and CRISPR options once affordable. India's CRISPR landscape includes startups (Mycroft), academic labs (IIT-Bombay, IIT-Delhi CRISPR consortia); policy support via National Biotechnology Strategy 2024 can position India as a low-cost CRISPR manufacturing hub.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Meta Quest 4 / Quest 3S ---
        {
            "id": 26105,
            "question_text": "Meta launched the Quest 3S, a more affordable mixed-reality VR headset, in which month of 2024?",
            "option_a": "March 2024",
            "option_b": "June 2024",
            "option_c": "October 2024",
            "option_d": "December 2024",
            "correct_answer": "C",
            "explanation": "Meta launched the Quest 3S on October 15, 2024 at a starting price of $299 — making mixed-reality more affordable than the $499 Quest 3. It shares the Snapdragon XR2 Gen 2 chip with Quest 3 but uses older Fresnel lenses. Meta's flagship Quest 4 is expected in 2026.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Aditya-L1 first-year observations ---
        {
            "id": 26106,
            "question_text": "Aditya-L1 completed one year of solar observations at Lagrange Point L1 in January 2025. Which of its key instruments captured a major Coronal Mass Ejection (CME) during the 2024-25 solar maximum?",
            "option_a": "PAPA (Plasma Analyser Package for Aditya)",
            "option_b": "VELC (Visible Emission Line Coronagraph)",
            "option_c": "ASPEX (Aditya Solar wind Particle Experiment)",
            "option_d": "All of the above",
            "correct_answer": "D",
            "explanation": "During its first year of observations (January 2024-25), Aditya-L1's full payload suite — VELC, SUIT, SoLEXS, HEL1OS, ASPEX, PAPA and MAG — captured multiple major Coronal Mass Ejections (CMEs) and solar flares during Solar Cycle 25's maximum. India's solar science achievement: (1) VELC — first Indian space-based coronagraph observing Sun's corona at 1.05 solar radii, (2) SUIT captures chromospheric imaging in UV — unique Indian capability, (3) Real-time solar wind prediction supports space weather forecasting critical for power grids and satellites, (4) Data shared with international community (NOAA, ESA) through ISROData hub, (5) Positions India among elite solar science nations (USA, ESA, Japan).",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- NISAR data delivery ---
        {
            "id": 26107,
            "question_text": "After NISAR's successful launch on July 30, 2025, when did it begin delivering its first L-band and S-band science data publicly?",
            "option_a": "August 2025",
            "option_b": "October 2025",
            "option_c": "January 2026",
            "option_d": "April 2026",
            "correct_answer": "B",
            "explanation": "NISAR commissioning (in-orbit checkout and antenna deployment of the 12-metre AstroMesh reflector) was completed by mid-October 2025. NASA and ISRO released the first public L-band and S-band SAR images in October-November 2025, with the full mission science phase beginning early 2026.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Vyommitra humanoid robot ---
        {
            "id": 26108,
            "question_text": "Vyommitra, ISRO's humanoid robot scheduled to fly aboard the uncrewed Gaganyaan-G1 mission, is designed to do what?",
            "option_a": "Conduct EVA (spacewalks) outside the crew module",
            "option_b": "Simulate human functions to test life-support and monitor onboard systems",
            "option_c": "Pilot the spacecraft autonomously to the Moon",
            "option_d": "Build the Bharatiya Antariksh Station modules in orbit",
            "correct_answer": "B",
            "explanation": "Vyommitra (Sanskrit for 'Space Friend') is a half-humanoid robot built by ISRO's Inertial Systems Unit. Strategic importance: (1) Demonstrates India's indigenous robotics capability for spaceflight, (2) Validates life-support systems, abort procedures, crew module operations, (3) Responds to voice commands and performs 30+ pre-programmed tasks, (4) Carries biometric monitoring sensors to simulate human physiology in microgravity, (5) Success of Gaganyaan-G1 (Dec 2025 uncrewed) will clear the way for crewed Gaganyaan-4 (2027), making India the 4th nation with independent human spaceflight.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Quantum Mission ---
        {
            "id": 26109,
            "question_text": "The National Quantum Mission (NQM), launched by the Government of India, has an outlay of Rs 6,003.65 crore over which period?",
            "option_a": "2022-26",
            "option_b": "2023-31",
            "option_c": "2024-30",
            "option_d": "2025-35",
            "correct_answer": "B",
            "explanation": "The National Quantum Mission (NQM) was approved by the Union Cabinet on April 19, 2023 with an outlay of Rs 6,003.65 crore for 2023-31 (8 years). India's strategic positioning: (1) Competes in US-China quantum race (Google Willow 105Q vs China DeepSeek vs Microsoft Majorana), (2) IBM Quantum System Two (156-qubit Heron R2) deployed at Amaravati AQCC (Jan 2026), (3) Goals: Develop 50-1000 physical qubits by 2031, satellite-based quantum communication, quantum sensors/atomic clocks, (4) Leadership: T-Hub nodes at IISc Bangalore, IIT Madras, IIT Bombay, IIT Delhi, (5) Applications: Drug discovery, cryptography, optimization — critical for future economic competitiveness.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Tianwen-2 ---
        {
            "id": 26110,
            "question_text": "China launched Tianwen-2, its second deep-space exploration mission, in May 2025 to collect samples from which target?",
            "option_a": "Mars",
            "option_b": "Comet 67P",
            "option_c": "Near-Earth asteroid 2016 HO3 (Kamo'oalewa)",
            "option_d": "Jupiter's moon Europa",
            "correct_answer": "C",
            "explanation": "Tianwen-2 was launched on May 29, 2025 by China's CNSA (China National Space Administration). The spacecraft is a dual-target asteroid and comet mission: (1) Primary: Collect samples from the near-Earth quasi-satellite asteroid 2016 HO3 (Hawaiian name 'Kamo'oalewa' meaning 'wandering sky object') — a rare Earth co-orbital object that drifts in and out of Earth's orbit every 385 years; expected sample return ~2027-28, (2) Secondary: Continue to explore main-belt comet 311P/PANSTARRS in 2035. Tianwen-2 is China's first asteroid sample-return mission (after Chang'e lunar missions) and demonstrates advanced deep-space navigation capabilities. Strategic significance for India: China's aggressive deep-space agenda (Tianwen-2 follows Tianwen-1 Mars rover success and Chang'e-6 lunar sample return) demonstrates China's space superpower status. India's response should accelerate: (1) Mars Orbiter Mission 2 (planned ~2026-27), (2) Asteroid impact hazard assessment and mitigation (Apophis close approach 2029), (3) Sample-return mission planning (Chandrayaan-4 lunar sample return 2027, future asteroid mission ~2035+). China's leadership in asteroid science highlights India's opportunity — most asteroids remain unexplored, and India can carve a niche in specific asteroid targets relevant to Indian interests (near-Earth asteroids that pose impact risks to India, C-type asteroids with water ice). ISRO's NGLV capability (once operational 2032-35) enables independent deep-space missions without reliance on international partnerships.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Bharat 6G Alliance ---
        {
            "id": 26111,
            "question_text": "India launched the 'Bharat 6G Vision' document and the Bharat 6G Alliance to make India a global leader in 6G technology by which year?",
            "option_a": "2028",
            "option_b": "2030",
            "option_c": "2035",
            "option_d": "2040",
            "correct_answer": "B",
            "explanation": "PM Modi released the 'Bharat 6G Vision' document on March 23, 2023, with the goal of making India a global leader in 6G technology by 2030. The Bharat 6G Alliance (industry-academia consortium) was launched in July 2023. By 2025, India had filed over 200 patents on 6G technology under this initiative.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Aravind / India BharatGen / IndiaAI ---
        {
            "id": 26112,
            "question_text": "The IndiaAI Mission, approved by the Union Cabinet in March 2024 with a Rs 10,371 crore outlay, aims to do what?",
            "option_a": "Build a sovereign Large Language Model (LLM) and supply 10,000+ GPUs for AI compute",
            "option_b": "Train 1 million AI engineers by 2030",
            "option_c": "Replace foreign AI services in government with Indian alternatives by 2026",
            "option_d": "Set up AI courts to resolve technology disputes",
            "correct_answer": "A",
            "explanation": "The IndiaAI Mission (approved March 7, 2024) has 7 pillars, including: building sovereign foundational AI models / LLMs (BharatGen launched 2024); providing 10,000+ GPUs for shared compute under IndiaAI Compute; setting up the AI Innovation Centre, Datasets Platform, AI Application Development, FutureSkills Programme, Startup Financing and Safe & Trusted AI.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Semiconductor Mission ---
        {
            "id": 26113,
            "question_text": "India's first semiconductor manufacturing plant, by Tata Electronics and Powerchip Semiconductor Manufacturing (PSMC), is being built in which state?",
            "option_a": "Gujarat (Dholera)",
            "option_b": "Karnataka (Mysuru)",
            "option_c": "Tamil Nadu (Sriperumbudur)",
            "option_d": "Andhra Pradesh (Visakhapatnam)",
            "correct_answer": "A",
            "explanation": "India's first commercial semiconductor fab is being built by Tata Electronics + Powerchip Semiconductor Manufacturing Corp (PSMC, Taiwan) in Dholera, Gujarat. Foundation laid March 13, 2024; investment Rs 91,000 crore; first chips expected by end-2026. Three other approved units (Tata Assam ATMP, Micron Sanand, CG Power Sanand) are also under construction.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- ISRO SpaDeX docking success ---
        {
            "id": 26114,
            "question_text": "ISRO's SpaDeX mission successfully achieved India's first in-space docking of two satellites (SDX-01 'Chaser' and SDX-02 'Target') on which date?",
            "option_a": "December 30, 2024",
            "option_b": "January 16, 2025",
            "option_c": "March 21, 2025",
            "option_d": "May 18, 2025",
            "correct_answer": "B",
            "explanation": "SpaDeX (Space Docking Experiment) achieved India's first successful in-space docking on January 16, 2025 at 09:44 IST, making India the 4th country to demonstrate autonomous spacecraft docking (after USA, Russia/USSR, and China). The Chaser satellite (SDX-01, 220 kg) autonomously approached and docked with the Target satellite (SDX-02, 220 kg) at 380 km altitude in LEO. Both were launched together on December 30, 2024 by PSLV-C60. Undocking was successfully performed on March 13, 2025, validating the reversibility of docking — critical for future servicing and assembly operations. Strategic significance for India: Docking technology is a prerequisite for: (1) Gaganyaan crewed missions (docking crew module with orbital module for safe return), (2) Bharatiya Antariksh Station (BAS) — multiple modules docked in orbit post-2028, (3) In-orbit refueling and spacecraft servicing (extending satellite lifespans), (4) Deep-space missions (lunar transfer module docking with descent vehicle). SpaDeX's success validates India's indigenous guidance, navigation, and control (GN&C) systems — previously a weakness. The mission positioned India as a credible partner for international space programs; Japan (JAXA), Russia (Roscosmos), and ESA expressed interest in collaboration. For India's economy, docking capability enables commercial space services (debris removal, satellite servicing) — a $10+ billion global market opportunity.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Quantum chip — Google Willow / Microsoft Majorana ---
        {
            "id": 26115,
            "question_text": "Google unveiled 'Willow', a 105-qubit quantum chip, in December 2024. Microsoft followed with which quantum chip in February 2025, based on topological qubits using Majorana zero modes?",
            "option_a": "Azure Quantum",
            "option_b": "Majorana 1",
            "option_c": "Topo Q1",
            "option_d": "Surface Code S1",
            "correct_answer": "B",
            "explanation": "Microsoft unveiled 'Majorana 1' on February 19, 2025 — the world's first quantum chip built on a 'topological core' using topoconductor materials (indium arsenide + aluminium superconductor) to host Majorana zero modes. Microsoft claims this enables a path to a million-qubit topological quantum computer. Google's Willow (Dec 2024) is a 105-qubit superconducting chip demonstrating exponential error suppression.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Indian Space Policy ---
        {
            "id": 26116,
            "question_text": "The Union Cabinet approved 100% Foreign Direct Investment (FDI) in India's space sector through the automatic route up to 49-100% in February 2024. Which segment allows the highest 100% FDI under the automatic route?",
            "option_a": "Satellite manufacturing & operation",
            "option_b": "Satellite components and sub-systems manufacturing",
            "option_c": "Launch vehicles and their associated systems",
            "option_d": "Ground segment / user segment",
            "correct_answer": "B",
            "explanation": "Under the amended FDI policy for the space sector (effective Feb 2024): (a) Satellite components/sub-systems manufacturing — 100% via automatic route; (b) Satellite manufacturing & operation, data products, ground segment — up to 74% via automatic, beyond by government route; (c) Launch vehicles & associated systems — up to 49% via automatic, beyond by government route.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Pixxel hyperspectral / Indian space startups ---
        {
            "id": 26117,
            "question_text": "Indian space-tech startup Pixxel launched its first three Firefly hyperspectral satellites in January 2025, building the world's most advanced commercial hyperspectral constellation. Pixxel is based in which Indian city?",
            "option_a": "Hyderabad",
            "option_b": "Bengaluru",
            "option_c": "Chennai",
            "option_d": "Pune",
            "correct_answer": "B",
            "explanation": "Pixxel, headquartered in Bengaluru and co-founded by Awais Ahmed and Kshitij Khandelwal in 2019, launched its first three Firefly hyperspectral satellites on January 14, 2025 via SpaceX Transporter-12. They form part of a planned 6-satellite Firefly constellation followed by 18 'Honeybees', offering 5-metre resolution hyperspectral imagery for agriculture, mining and climate monitoring.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Agnikul / Skyroot ---
        {
            "id": 26118,
            "question_text": "Agnikul Cosmos successfully launched 'Agnibaan SOrTeD' in May 2024 — the world's first rocket powered by which type of engine?",
            "option_a": "Hybrid solid-liquid engine",
            "option_b": "Single-piece 3D-printed semi-cryogenic engine",
            "option_c": "Methalox electric pump-fed engine",
            "option_d": "Aerospike nozzle engine",
            "correct_answer": "B",
            "explanation": "Agnikul Cosmos (IIT Madras incubated startup, Chennai) launched 'Agnibaan SOrTeD' (Sub-Orbital Technology Demonstrator) on May 30, 2024 from India's first private launchpad 'Dhanush' at SDSC SHAR. It used the world's first single-piece 3D-printed semi-cryogenic 'Agnilet' engine (LOX + aviation kerosene). Skyroot's Vikram-1 orbital flight is targeted for 2025-26.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- WHO H5N1 cattle outbreak ---
        {
            "id": 26119,
            "question_text": "In 2024-25 the H5N1 'bird flu' virus crossed species barriers and caused a major outbreak in which unexpected mammalian host in the United States?",
            "option_a": "Pigs",
            "option_b": "Dairy cattle",
            "option_c": "Domestic dogs",
            "option_d": "Sheep",
            "correct_answer": "B",
            "explanation": "Starting March 2024, H5N1 highly pathogenic avian influenza spread among dairy cattle in the USA — the first widespread mammal-to-mammal outbreak of H5N1. By 2025, it had spread to over 1,000 dairy herds across 17+ states, with several human cases (mostly in farm workers). WHO and CDC continue to monitor the spillover risk to humans.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- mpox emergency ---
        {
            "id": 26120,
            "question_text": "The WHO declared mpox (formerly monkeypox) a Public Health Emergency of International Concern (PHEIC) for the second time in August 2024 due to the spread of which new variant?",
            "option_a": "Clade Ia",
            "option_b": "Clade Ib",
            "option_c": "Clade IIa",
            "option_d": "Clade IIb",
            "correct_answer": "B",
            "explanation": "WHO declared mpox a PHEIC for the second time on August 14, 2024, driven by the rapid spread of the more virulent Clade Ib (subclade of Clade I) starting from the Democratic Republic of Congo (DRC) and spreading to neighbouring African countries. The PHEIC was lifted in September 2025 after coordinated vaccination campaigns slowed transmission.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Asteroid 2024 YR4 ---
        {
            "id": 26121,
            "question_text": "Asteroid 2024 YR4, discovered in December 2024, briefly raised global attention in early 2025 because of what?",
            "option_a": "It was the largest asteroid ever discovered near Earth",
            "option_b": "Its short-lived elevated impact probability (~3%) for a December 22, 2032 Earth impact",
            "option_c": "It was confirmed to contain valuable platinum-group metals",
            "option_d": "It was the first asteroid found to have its own moon",
            "correct_answer": "B",
            "explanation": "Asteroid 2024 YR4 (discovered Dec 27, 2024 by ATLAS, Chile) — a 40-90 metre near-Earth asteroid — reached a 3.1% Torino-scale-3 impact probability for December 22, 2032 in February 2025, the highest ever recorded for a sizeable asteroid. Further observations rapidly reduced Earth-impact probability to near zero by late February 2025, but raised a small (~4%) chance of lunar impact in 2032.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Polaris Dawn ---
        {
            "id": 26122,
            "question_text": "SpaceX's Polaris Dawn mission (September 2024) achieved which historic spaceflight milestone?",
            "option_a": "First all-civilian crew to orbit the Moon",
            "option_b": "First privately funded commercial spacewalk (EVA)",
            "option_c": "First crewed flight on Starship",
            "option_d": "First mission to land on Mars",
            "correct_answer": "B",
            "explanation": "Polaris Dawn (launched Sep 10, 2024; commander: Jared Isaacman) was a SpaceX private crewed mission on Crew Dragon Resilience. On September 12, 2024 it achieved the world's first privately funded commercial spacewalk (EVA), with Isaacman and Sarah Gillis stepping out of the Dragon capsule. It also reached the highest Earth orbit since Apollo (~1,400 km).",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Sunita Williams stranded / Boeing Starliner ---
        {
            "id": 26123,
            "question_text": "NASA astronauts Sunita Williams and Butch Wilmore, who were unexpectedly stranded on the ISS for over 9 months due to Boeing Starliner technical issues, finally returned to Earth in March 2025 aboard which spacecraft?",
            "option_a": "Boeing Starliner (uncrewed return)",
            "option_b": "SpaceX Crew Dragon Freedom (Crew-9 mission)",
            "option_c": "Soyuz MS-25",
            "option_d": "NASA Orion test capsule",
            "correct_answer": "B",
            "explanation": "Sunita Williams (Indian-American, Cmdr) and Butch Wilmore launched on Boeing Starliner CFT (June 5, 2024) for a planned 8-day stay. Due to helium leaks and thruster issues, Starliner returned uncrewed in Sep 2024. They eventually returned to Earth on March 18, 2025 aboard SpaceX Crew Dragon Freedom (as part of Crew-9), splashing down off the Florida coast after 286 days in space.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Hayabusa2 / OSIRIS-REx / asteroid samples ---
        {
            "id": 26124,
            "question_text": "Scientists analysing OSIRIS-REx samples from asteroid Bennu, returned to Earth in September 2023, reported in early 2025 the detection of which significant prebiotic compounds?",
            "option_a": "All 20 amino acids of life",
            "option_b": "Amino acids (including 14 of the 20 used in proteins) and the 5 nucleobases of DNA/RNA",
            "option_c": "Functional DNA strands",
            "option_d": "Living microorganisms",
            "correct_answer": "B",
            "explanation": "January 2025 studies of OSIRIS-REx Bennu samples (Nature & Nature Astronomy) reported amino acids — including 14 of the 20 used in proteins (proteinogenic) — plus all five nucleobases of DNA/RNA (adenine, guanine, cytosine, thymine, uracil), salts and complex organic compounds. These findings strengthen the hypothesis that the building blocks of life were delivered to Earth by asteroids.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- 5G/6G India deployment ---
        {
            "id": 26126,
            "question_text": "By the end of 2025, India had crossed how many 5G base station sites, making it the world's second-largest 5G deployment after China?",
            "option_a": "1 lakh sites",
            "option_b": "3 lakh sites",
            "option_c": "5 lakh sites",
            "option_d": "10 lakh sites",
            "correct_answer": "C",
            "explanation": "India crossed 5 lakh (500,000) 5G base station sites by the end of 2025, having launched 5G commercially on October 1, 2022. India is the world's second-largest 5G market after China. The Bharat 6G Vision (March 2023) targets India as a 6G leader by 2030.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Wormlike spaghetti ozone / scientific discovery ---
        {
            "id": 26127,
            "question_text": "Scientists confirmed in 2024-25 that the Antarctic ozone hole is showing signs of recovery, with full healing now expected by which decade?",
            "option_a": "2030s",
            "option_b": "2040s",
            "option_c": "2060s",
            "option_d": "2080s",
            "correct_answer": "C",
            "explanation": "The UN/WMO Scientific Assessment of Ozone Depletion (released January 2023, updated 2024-25) confirms that the Antarctic ozone hole is on track to fully heal by around 2066, with the Arctic recovering by ~2045 and the rest of the world by 2040 — provided Montreal Protocol compliance continues. The 2024 ozone hole was smaller than in recent years.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Stargate Project ---
        {
            "id": 26128,
            "question_text": "The 'Stargate' AI infrastructure project, announced by US President Donald Trump on January 21, 2025, is a $500 billion partnership of OpenAI with which other companies?",
            "option_a": "Microsoft and NVIDIA",
            "option_b": "SoftBank and Oracle",
            "option_c": "Google and Amazon",
            "option_d": "Meta and IBM",
            "correct_answer": "B",
            "explanation": "The 'Stargate Project', announced at the White House on January 21, 2025, is a $500 billion AI infrastructure initiative over four years, partnering OpenAI with SoftBank, Oracle and MGX (UAE). It aims to build the largest AI data centres in the US — starting with a $100 billion immediate investment in Texas — to support next-generation AI training and deployment.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- INS Arnala / DRDO Nirbhay ---
        {
            "id": 26129,
            "question_text": "DRDO successfully test-fired the long-range Land-Attack Cruise Missile (LRLACM) in November 2024 from Chandipur, with a strike range of approximately?",
            "option_a": "300 km",
            "option_b": "500 km",
            "option_c": "1,000 km",
            "option_d": "2,000 km",
            "correct_answer": "C",
            "explanation": "DRDO successfully test-fired the Long Range Land Attack Cruise Missile (LRLACM) — derived from the Nirbhay missile — from ITR Chandipur, Odisha on November 12, 2024. The subsonic missile has a strike range of approximately 1,000 km, can carry conventional or nuclear warheads, and is being inducted by all three Indian armed forces (Army, Navy, Air Force) under the Make-in-India programme.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Gemini Robotics / embodied AI ---
        {
            "id": 26130,
            "question_text": "Google DeepMind launched 'Gemini Robotics' models in March 2025 — based on Gemini 2.0 — to enable what?",
            "option_a": "Generating 3D avatars for the metaverse",
            "option_b": "Robots that understand natural language and perform real-world physical tasks",
            "option_c": "Self-driving car perception systems",
            "option_d": "Drone swarms for military reconnaissance",
            "correct_answer": "B",
            "explanation": "Google DeepMind launched 'Gemini Robotics' and 'Gemini Robotics-ER' (Embodied Reasoning) on March 12, 2025 — Vision-Language-Action (VLA) models built on Gemini 2.0 that bring AI into the physical world. They enable robots to understand natural language commands, reason about physical environments and perform complex manipulation tasks, with partner Apptronik integrating it into humanoid robots.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Liquid Mirror Telescope / IIA Nainital ---
        {
            "id": 26131,
            "question_text": "India's Indian Institute of Astrophysics (IIA) operates the India Astronomical Observatory at Hanle, Ladakh, home to the 2.01-metre Liquid Mirror Telescope (LMT). What is the key advantage of a liquid mirror design?",
            "option_a": "It reduces the weight of the telescope, enabling space-based deployment",
            "option_b": "It uses a rotating liquid metal surface (mercury or molten salt) to reflect light, eliminating the need for grinding and polishing large glass mirrors",
            "option_c": "It operates only in infrared wavelengths, penetrating cosmic dust more effectively",
            "option_d": "It allows simultaneous observation of the entire celestial sphere",
            "correct_answer": "B",
            "explanation": "The Liquid Mirror Telescope (LMT) at Hanle (4,500-metre altitude, among the world's highest observatories) uses a rotating mercury-on-glass surface as the primary mirror. The surface naturally forms a parabolic shape due to centrifugal force, eliminating expensive grinding and polishing — reducing cost by 50-70% vs glass mirrors. The 2.01-metre LMT was commissioned in 2001 and upgraded in 2021. Strategic significance for India: (1) LMT discovers transient astronomical objects (supernovae, gamma-ray bursts, asteroids), (2) High-altitude site at Hanle reduces atmospheric turbulence compared to lower-altitude observatories, (3) IIA's optical interferometry arrays (Aryabhata Research Institute of Observational Sciences, ARIES Nainital) enable high-resolution imaging competing with international facilities, (4) India's upcoming 3.6-metre Aryabhata Telescope (4,000-metre site, Hanle) will use advanced adaptive optics for diffraction-limited imaging. These facilities position India as a credible partner for international collaborations (Square Kilometre Array — SKA 2030+).",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Perovskite Solar Cells / renewable energy ---
        {
            "id": 26132,
            "question_text": "Perovskite solar cells achieved record power conversion efficiencies of ~33% in laboratory conditions in 2024-25. Why are perovskites advantageous over silicon solar cells for India's solar expansion?",
            "option_a": "They operate at higher temperatures, beneficial for hot climates like India",
            "option_b": "They have lower manufacturing costs, are transparent (enabling building-integrated PV), use abundant materials, and stack easily with silicon cells (tandem PV)",
            "option_c": "They generate electricity without sunlight, enabling night-time power generation",
            "option_d": "They eliminate the need for inverters, reducing system costs",
            "correct_answer": "B",
            "explanation": "Perovskite solar cells (named after the mineral perovskite, CaTiO3; synthetic ABX3 halide perovskites lead: methylammonium/formamidinium lead iodide/bromide) offer transformative advantages: (1) High efficiency (33% lab record, approaching theoretical limit of ~35%), (2) Solution-based manufacturing (spin-coating, inkjet printing) — 10-100x cheaper than silicon wafer production, (3) Tuneable bandgap enabling tandem cells with silicon (theoretical >40% efficiency), (4) Semi-transparency for building-integrated photovoltaics (BIPV — windows, roofs, facades generating power), (5) Lightweight and flexible (roll-to-roll manufacturing possible). Challenges: stability (Pb toxicity, moisture/oxygen degradation), long-term durability. Strategic significance for India: India targets 500 GW renewable energy by 2030 (already 200+ GW). Perovskite scaling accelerates this: (1) Lower costs enable distributed rooftop solar in rural India (alleviating 400+ million without reliable electricity), (2) BIPV integrates power generation into buildings — reducing land-use conflicts in densely populated regions, (3) Tandem perovskite-silicon cells manufactured in India (Vikram Solar, Waaree Energies partnering with IIT-Delhi, CSIR-NPL) reduce polysilicon import dependency (currently 80% imported). India's National Solar Mission 2.0 should prioritize perovskite R&D through IISc, IISER, and start-up funding (e.g., Sahasra, ORI) to achieve cost-competitiveness with silicon by 2030.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- ITER Tokamak / Fusion Energy ---
        {
            "id": 26133,
            "question_text": "The ITER (International Thermonuclear Experimental Reactor) tokamak under construction in France aims to achieve what milestone in fusion power generation?",
            "option_a": "Net-zero energy gain (outputting energy equal to input)",
            "option_b": "Net energy gain (outputting 10 times the input energy) with Q=10 target",
            "option_c": "Sustained plasma confinement for 300 seconds at 150 million Kelvin",
            "option_d": "Commercial electricity generation at grid scale",
            "correct_answer": "B",
            "explanation": "ITER (International Thermonuclear Experimental Reactor, construction 70% complete as of May 2026) is a collaborative tokamak involving 35 nations including India, US, China, Russia, and EU. Design target: Q-factor (fusion output / heating input energy) = 10 — meaning 10 times more energy released from fusion than input to heat the plasma. ITER's superconducting magnets (160 Tesla toroidal field + poloidal coils) confine ~840 cubic metres of deuterium-tritium plasma at 150 million Kelvin. Operation planned 2024-2030+ with a goal of 10 minutes continuous plasma confinement. Strategic significance for India: India's Institute of Plasma Research (IPR, Gandhinagar) leads the Steady-State Superconducting Tokamak (SST-1) program — India's own tokamak achieving plasma temperatures >40 million K. ITER knowledge transfer to IPR enables India to: (1) Develop indigenous fusion technology for long-term energy security (India's electricity demand grows 5% annually; fossil fuels = 70% generation), (2) Design a demonstration fusion reactor (DEMO) by 2050, (3) Create high-tech manufacturing capability (superconducting magnets, cryogenics, tritium breeding blankets — competitive advantage). India's participation in ITER validates its fusion credentials; Indian engineers (ITER India office, Gandhinagar) contribute to magnet assembly, cryogenics, and tokamak operations — building expertise for independent Indian fusion plants.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- mRNA Vaccine Platform / infectious disease ---
        {
            "id": 26134,
            "question_text": "Following the COVID-19 mRNA vaccine success (Pfizer, Moderna), pharmaceutical companies developed mRNA vaccines for which other infectious diseases by 2025?",
            "option_a": "Only influenza and RSV",
            "option_b": "Influenza, RSV (respiratory syncytial virus), malaria, and HIV (entering trials)",
            "option_c": "Ebola, Marburg, and SARS-CoV-3 (hypothetical)",
            "option_d": "Tuberculosis, measles, and yellow fever",
            "correct_answer": "B",
            "explanation": "mRNA vaccine platform achievements 2024-25: (1) Moderna + Merck: RSV vaccine (Arexvy) approved Oct 2023 for adults ≥60 years, (2) Moderna: Seasonal influenza vaccine (in Phase 2b trials 2024-25), (3) BioNTech + Pfizer: HPV and influenza mRNA vaccines in development, (4) Moderna: Malaria mRNA vaccine showing 75% efficacy in Phase 2b trials (announced 2024), (5) IAVI + Moderna: HIV mRNA vaccine entering Phase 2a trials (2024-25). mRNA platform advantages: rapid manufacturing, low cost at scale, thermostability (newer lipid nanoparticles tolerate room temperature 25-28°C). Strategic significance for India: India bears 25% of global malaria burden (8-10 million cases annually, endemic in 350+ districts); 2 million TB cases annually (highest globally). mRNA vaccines offer: (1) Customizable for Indian variants (P. vivax malaria, drug-resistant TB), (2) Manufacturing localization via Serum Institute, Bharati Biotech, Biological E — reducing import dependency on Pfizer/Moderna, (3) Affordability at scale (expected <$1-2 per dose by 2027 vs $15-20 today). India's COVID-19 experience (COVAXIN by Bharat Biotech) demonstrates mRNA-like vaccine capability; scaling to malaria and TB vaccines addresses India's disease priorities. WHO approval of India-manufactured mRNA vaccines by 2028 enables global south vaccine security, reducing reliance on high-income nations.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Artemis 2 Mission / Human Lunar Return ---
        {
            "id": 26135,
            "question_text": "NASA's Artemis 2 crewed lunar mission (launched April 2, 2026) set a record for how far from Earth a crewed spacecraft has ever traveled?",
            "option_a": "Greatest distance: 150,000 km (reaching the far side of the Moon)",
            "option_b": "Greatest distance: 252,760 km (Apollo 13 record, now matched)",
            "option_c": "Greatest distance: 400,000 km (beyond the Moon)",
            "option_d": "Greatest distance: 1 million km (Sun-Earth L1 point region)",
            "correct_answer": "C",
            "explanation": "Artemis 2 (launched April 2, 2026 on Space Launch System from Kennedy Space Center) carried NASA astronauts Reid Wiseman, Victor Glover, Anne McClain, and Canadian astronaut Jeremy Hansen on a 10-day lunar flyby mission. On April 6-11, 2026, the Orion capsule reached a record 252,760 km from Earth at closest lunar approach, beating Apollo 13's 1970 record distance of 248,655 km. The mission validated Orion's life-support, thermal protection, and navigation systems in cislunar space — prerequisites for Artemis 3 crewed lunar landing (targeted 2028-29, including landing on the Moon's south pole near the Shackleton Crater). Strategic significance for India: Artemis 2 success demonstrates US commitment to sustained lunar exploration, driving geopolitical competition. India's response: (1) Chandrayaan-3 lander/rover (July 2023) and Chandrayaan-4 sample-return mission (targeted 2027-28) position India among elite lunar explorers, (2) Bharatiya Antariksh Station (2028-35) requires cislunar logistics — docking, orbital refueling, crewed transport. Artemis program partnership frameworks (Artemis Accords, 2020) — which India should join to participate in lunar resource-sharing governance, (3) India's push for independent crewed lunar missions post-2035 requires duplicating Artemis-level capabilities (SLS-equivalent with NGLV 2032-35, lunar module development, life-support systems). India's space leadership positioning depends on Artemis cooperation while building indigenous capabilities.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- SpaceX Starship IFT-9 through IFT-12 ---
        {
            "id": 26136,
            "question_text": "SpaceX's Starship Integrated Flight Tests (IFT-9 through IFT-12) in 2025-26 progressively validated which capabilities toward full reusability?",
            "option_a": "Only Raptor engine throttling and ascent dynamics",
            "option_b": "Booster catch by launch tower arms ('chopstick' mechanism), controlled booster/ship re-entry, heat shield integrity, and ship ocean landing",
            "option_c": "Autonomous refueling and payload bay door operation in orbit",
            "option_d": "Crewed interior life-support and microgravity experiments",
            "correct_answer": "B",
            "explanation": "SpaceX's Starship development roadmap 2025-26: IFT-9 (May 2025) — repeated booster catch (hot-staging simulation), IFT-10 (July 2025) — ship heat-tile durability during re-entry, belly-flop maneuver tested, IFT-11 (Oct 2025) — first booster re-catch + controlled ocean landing, IFT-12 (Jan 2026) — ship re-entry thermal protection validated. By mid-2026, Starship targets zero-boil-off Raptor restarts in space and ship ocean landing recovery — demonstrating the 'chopstick' catch tower's reliability and heat-shield integrity for 100+ re-uses. Strategic significance for India: Starship's full reusability (targeting $10/kg launch costs vs current $1,000-4,000/kg) disrupts the geopolitical space-launch hierarchy. India's space-launch independence requires: (1) NGLV development (ISRO's reusable launcher, targeted 2032-35) with booster recovery analogous to Starship, (2) Learning from SpaceX's rapid-iteration philosophy (IFT every 6-8 weeks vs ISRO's multi-year gaps), (3) Public-private partnerships enabling Indian startups (Skyroot, Agnikul, Relativity Space India) to develop competing reusable systems. Starship's low costs enable mega-constellations for Indian startups (Pixxel, TrustComm, earth.ai) — reducing access barriers. India's strategic autonomy in space depends on matching Starship-level reusability by 2040.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Graphene & 2D Materials / Nanotechnology ---
        {
            "id": 26137,
            "question_text": "Graphene — a single layer of carbon atoms arranged in hexagons — has been extensively researched since 2004 (Nobel Prize 2010). By 2025, which applications reached commercial or near-commercial status?",
            "option_a": "Only graphene reinforced composites for aerospace",
            "option_b": "Graphene batteries (faster charging, longer life), supercapacitors, thermal conductors for electronics, water purification membranes, and graphene-enhanced concrete",
            "option_c": "Graphene microchips replacing silicon transistors",
            "option_d": "Transparent graphene solar cells achieving >40% efficiency",
            "correct_answer": "B",
            "explanation": "Graphene commercialization by 2025: (1) Energy: Samsung graphene batteries (5-minute fast charging, 5x cycle life vs lithium-ion); Graphene Energy supercapacitors for grid storage, (2) Electronics: Thermal management — graphene sheets in GPU/CPU cooling (Intel, AMD evaluating), (3) Water: Membranes for desalination (lower fouling vs reverse osmosis), (4) Construction: Graphene concrete additives (improved strength, 2-3% weight reduction), (5) Composites: Carbon-fiber + graphene for aerospace/EV bodies. Challenges: Production cost ($100-1000/gram at scale vs lab $10,000), quality variability, biocompatibility concerns. Strategic significance for India: India's graphene research ecosystem (IIT-M, IIT-Delhi, IISc) develops: (1) CVD graphene synthesis scaling for mass production (target cost <$10/gram by 2028), (2) Applications for India's priorities: graphene-battery EVs addressing transportation emissions (India aims 30% EV by 2030 in new vehicle sales), (3) Graphene-concrete for infrastructure durability in India's extreme monsoon/seismic regions. India's graphene startups (e.g., Graphene Industry Pvt Ltd, Bengaluru) and CSIR labs can position India as a graphene materials supplier (competing with China, US) — adding $500+ million to India's advanced materials export economy.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Synthetic Biology / Biomanufacturing ---
        {
            "id": 26138,
            "question_text": "Synthetic biology — engineering biological systems with artificial DNA/RNA — reached a commercial milestone in 2024-25 when Genentech and Intrinsic Therapeutics deployed AI-designed proteins to produce which therapeutic?",
            "option_a": "Insulin for diabetes management",
            "option_b": "Abicipar pegol (anti-VEGF antibody for age-related macular degeneration)",
            "option_c": "Monoclonal antibodies for cancer immunotherapy",
            "option_d": "Recombinant growth hormone for pediatric dwarfism",
            "correct_answer": "B",
            "explanation": "Genentech + Intrinsic Therapeutics (founded 2018, acquired by Exscientia 2024) deployed AI-designed novel proteins (using Intrinsic's AlphaFold-derived protein design) integrated into abicipar pegol — an anti-VEGF fusion protein for wet age-related macular degeneration (AMD). The AI-designed domain improved protein stability and manufacturability. This represents the first human therapeutic containing AI-designed protein sequences — a paradigm shift validating synthetic biology's clinical potential. Strategic significance for India: Synthetic biology enables low-cost biomanufacturing of therapeutics — critical for India's pharmaceutical industry. (1) AI protein design reduces drug development timelines from 10-15 years to 2-3 years, (2) Heterologous expression in E. coli / yeast / CHO cells — used in India's biopharmaceutical sector — cuts manufacturing costs 70-90% vs animal-derived biologics. India's opportunity: (1) CSIR-IMTECH (Chandigarh) and Vyome Therapeutics (synthetic microbiology for probiotics) scale AI-protein design for therapeutics addressing India's disease burden (tuberculosis, malaria, dengue), (2) Government support via National Biotechnology Strategy (2024) incentivizing synthetic biology startups (e.g., Genfutures, Bengaluru) developing biosimilars, (3) Biomanufacturing infrastructure in Kerala, Gujarat, Tamil Nadu producing world-class therapeutics at Indian costs — enabling export to global south and revenue of $50+ billion by 2040.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Artemis Base Camp / Lunar Infrastructure ---
        {
            "id": 26139,
            "question_text": "NASA's Artemis program plans to establish a crewed lunar base camp near the Moon's south pole. Which key advantage does the south pole location provide?",
            "option_a": "Permanent daylight throughout the lunar day, enabling continuous solar power",
            "option_b": "Water ice deposits in permanently shaded craters, enabling in-situ resource utilization (ISRU) for water/oxygen/propellant production",
            "option_c": "Proximity to the Moon's magnetic field, reducing radiation exposure",
            "option_d": "Easier communication with lunar far-side facilities",
            "correct_answer": "B",
            "explanation": "Artemis Base Camp location at Shackleton Crater region (south pole) offers: (1) Water ice deposits (estimated 100+ million tonnes) in permanently shaded craters — surviving billions of years despite lunar day temps reaching 120°C, (2) ISRU capability: H2O→H2+O2 (electrolysis or thermal), enabling: (a) drinking water/life support, (b) oxygen for breathing, (c) propellant (H2+O2 rocket fuel) for Earth ascent vehicles and cislunar logistics, (3) Continuous solar power: peaks near pole rim receiving 80%+ sunlight vs equatorial 50%, (4) Scientific value: ancient volcanic/impact-formed materials, polar volatiles sampling. Artemis 3 landing (2028-29) will deploy solar arrays, habitat modules, and ISRU demonstration. Strategic significance for India: Chandrayaan-4 sample-return mission (targeted 2027-28) should prioritize south-pole volatile sampling — complementing Artemis data and providing India independent insights into lunar resource distribution. India's long-term strategy: (1) Bharatiya Lunar Station (post-2035) requires ISRU capability tested on Artemis Base Camp sites — sharing data via international cooperation frameworks, (2) India-Russia Luna program collaboration (lunar south-pole joint exploration, post-2028) positions India as a cislunar power, (3) ISRU technology developed at IIT-M and VSSC enables India's independent lunar base by 2045. Lunar water ice access is the geopolitical prize of the next 20 years — India's scientific and commercial stake in lunar south pole must match its Chandrayaan achievement.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Direct Air Capture (DAC) / Carbon Removal ---
        {
            "id": 26140,
            "question_text": "Direct Air Capture (DAC) technology removes CO2 directly from ambient atmosphere and stores it (carbon sequestration). By 2025, which challenge remained the primary barrier to DAC scalability?",
            "option_a": "Technical: inability to detect CO2 in atmosphere at 420 ppm concentration",
            "option_b": "Economic: DAC costs $300-600 per tonne of CO2 removed, vs $50-150/tonne needed for climate viability",
            "option_c": "Environmental: DAC releases more CO2 than it captures",
            "option_d": "Political: lack of government regulation of DAC facilities",
            "correct_answer": "B",
            "explanation": "DAC systems (Climeworks, Carbon Engineering, Twelve Benefits) use solid/liquid sorbents or solvents to extract CO2 from air (420 ppm), then either store it (deep geological sequestration, >10,000 year permanence) or utilize it (chemicals, building materials, beverages). Current economics: $300-600/tonne (Climeworks), target <$100/tonne by 2030 via: (1) Heat recovery from industrial waste, (2) Renewable electricity (solar/wind) integration, (3) MOF/advanced sorbent improvements. Global DAC capacity (May 2026): ~1,500 tonnes CO2/year (negligible vs 37 billion tonnes annual emissions). Strategic significance for India: India's coal-power-plants emit 1+ billion tonnes CO2 annually; cement industry (cement = 8% global CO2) produces 350+ million tonnes. DAC deployment scenarios: (1) Post-combustion carbon capture at coal-plant flues (cheaper, $40-80/tonne) can offset emissions; DAC for legacy emissions or remote sources, (2) India's commitment to net-zero by 2070 requires 50 billion tonnes cumulative carbon removal — achievable only via scaled DAC + nature-based solutions (afforestation). India's opportunity: (1) DAC cost reduction via CSIR-IITs developing MOF sorbents and solvents adapted to India's monsoon climate (high humidity = DAC performance penalty), (2) CO2 utilization in building materials (concrete curing with captured CO2, reducing clinker demand), (3) Public-sector funding for pilot DAC at coal-plants and cement facilities (NITI Aayog, WRI India) can unlock $50+ billion market for DAC manufacturers (Climeworks competitors) and create jobs. India's DAC leadership by 2040 enables carbon neutrality credibility and competitive advantage in green manufacturing.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- NASA Chandra X-ray Observatory / Exoplanet Atmospheres ---
        {
            "id": 26141,
            "question_text": "The NASA Chandra X-ray Observatory, launched in 1999, made a groundbreaking discovery in 2024-25 regarding exoplanet atmospheres. What did it detect for the first time?",
            "option_a": "Water vapor in the atmosphere of a distant exoplanet",
            "option_b": "Auroral X-ray emissions from an exoplanet's magnetosphere, indicating a magnetic field",
            "option_c": "Oxygen and organic compounds suggesting biosignatures on a Super-Earth",
            "option_d": "Hydrogen escape (atmospheric stripping) from a hot Jupiter due to stellar radiation",
            "correct_answer": "B",
            "explanation": "In 2024-25, Chandra observations of the hot Jupiter WASP-33b detected auroral X-ray emissions — UV/X-ray aurora analogous to Earth's northern/southern lights. This provided the first definitive evidence that distant exoplanet possesses a magnetic field strong enough to generate auroras in its upper atmosphere. The detection demonstrates: (1) Magnetospheres protect planetary atmospheres from stellar wind erosion, (2) Magnetic field strength can be inferred from auroral brightness, (3) Planetary habitability context — strong magnetic fields reduce atmospheric loss. Strategic significance for India: ISRO's Aditya-L1 solar mission observations and India's participation in JWST exoplanet atmosphere characterization contribute to this science. India's future role: (1) AstroSat UV telescope (ISRO, operational since 2015) detecting hot Jupiter UV transits, (2) Vainu Bappu Observatory (Kavalur, Tamil Nadu) hosting next-generation spectroscopy for exoplanet follow-up, (3) India's space-based astronomical missions (ISRO's planned XUV astronomy satellite, 2027-28) contributing to global exoplanet atmosphere census. India's astronomical data-sharing commitments (via GAVO — Global Virtual Astronomy Observatory) position Indian science as a key contributor to understanding planetary atmospheres and potential habitability — foundation for astrobiology research.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Alzheimer's Disease Antibody Therapies ---
        {
            "id": 26142,
            "question_text": "Aducanumab and lecanemab — monoclonal antibodies targeting amyloid-beta plaques in the brain — were approved by FDA in 2023-24 for early-stage Alzheimer's disease. What remained a significant limitation of these therapies?",
            "option_a": "They only work in patients under age 50",
            "option_b": "Amyloid Related Imaging Abnormalities (ARIA) — microhemorrhages and microinfarcts in brain tissue due to aggressive amyloid removal",
            "option_c": "They do not cross the blood-brain barrier",
            "option_d": "They cause irreversible liver toxicity",
            "correct_answer": "B",
            "explanation": "Lecanemab (Leqembi, Eli Lilly) shows modest cognitive decline slowing (27% slowing over 18 months, clinical significance ~4 months delay in progression) but carries ARIA risk — brain MRI shows microhemorrhages (ARIA-H) and microinfarcts (ARIA-E) in 20-30% of treated patients, with symptomatic manifestations (headache, confusion) in ~2-5%. APOE4 carriers (genetic Alzheimer's risk) face higher ARIA risk. Strategic significance for India: India's elderly population (65+) will grow to 300+ million by 2050; age-related dementia prevalence ~5% (15+ million cases). India's Alzheimer's burden: low awareness, late diagnosis (stage 3-4), limited access to advanced therapeutics. Lecanemab costs $26,500/year (unaffordable for India's public health system). India's opportunity: (1) Biosimilar lecanemab manufacturing by Indian pharma (Lupin, Sun Pharma, Cipla) reducing cost to <$2,000/year, (2) Preclinical research at AIIMS Delhi and IIT-M on safer amyloid-targeting therapies with lower ARIA risk (e.g., intranasal immunotherapy, gene therapy), (3) Public health initiatives promoting cognitive reserve (education, exercise, diet) — reducing Alzheimer's incidence more cost-effectively than antibodies. India's drug-development pathway: fast-track regulatory approval for Alzheimer's biosimilars and novel therapies can address India's emerging neurodegenerative disease burden while generating $5+ billion export revenue.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- CERN HL-LHC Upgrade / Particle Physics ---
        {
            "id": 26143,
            "question_text": "CERN's Large Hadron Collider (LHC) is undergoing a High-Luminosity upgrade (HL-LHC) planned for completion by 2029. What is the primary physics goal of HL-LHC?",
            "option_a": "Achieve higher collision energies than the current 13 TeV to discover the Higgs Boson",
            "option_b": "Increase collision rate (luminosity) 10-fold to study Higgs properties and search for rare decay modes and physics beyond the Standard Model",
            "option_c": "Build a second identical tunnel to compare LHC data between parallel colliders",
            "option_d": "Reduce the physical size of the detector to lower operating costs",
            "correct_answer": "B",
            "explanation": "HL-LHC (operational 2029-2039) increases instantaneous luminosity from current 2×10^34 cm^-2 s^-1 to 5×10^34 cm^-2 s^-1 — collecting 10 times more proton-proton collision data than the legacy LHC. This enables: (1) Precise Higgs boson property measurements (coupling strengths, self-interaction, rare decays), (2) Rare Standard Model processes (flavor-changing neutral currents, electroweak penguin diagrams), (3) Searches for supersymmetric particles, dark matter candidates, extra dimensions, (4) Better constraints on fundamental parameters (electroweak symmetry breaking scale, CP violation). New detector technologies: silicon tracking, timing layers (4D tracking), upgraded calorimeters. Strategic significance for India: Indian particle physicists (Indian Institute of Science Education and Research — IISER Pune, Bombay; TIFR Mumbai) contribute to ATLAS and CMS detector development. India's scientific opportunities: (1) Data-analysis contributions to HL-LHC physics (machine learning for event selection, theoretical QCD calculations), (2) Detector component manufacturing capability — silicon strip sensors, timing detectors, readout electronics — can be sourced from Indian quantum/semiconductor industry, (3) Postdoctoral positions and graduate student placements at CERN strengthening India's particle physics capacity. India's long-term vision: establishing a 500-GeV International Linear Collider (ILC) facility or 100-km future circular collider (FCC) in India by 2060 — requiring current generation of Indian physicists trained at HL-LHC.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Apple Vision Pro 2 / Spatial Computing ---
        {
            "id": 26144,
            "question_text": "Apple released Vision Pro 2 in 2025, advancing spatial computing. What key improvement over Vision Pro 1 (2024) enabled enterprise adoption?",
            "option_a": "Vision Pro 2 can run Windows and Android applications natively",
            "option_b": "Weight reduction (305g→280g), higher-resolution display (92 pixels-per-degree), improved hand-eye tracking, and passthrough video quality",
            "option_c": "Vision Pro 2 replaced the required external battery with a built-in 12-hour battery",
            "option_d": "Vision Pro 2 cost reduced from $3,500 to $2,000, enabling consumer affordability",
            "correct_answer": "B",
            "explanation": "Apple Vision Pro 2 (released April 2025) improvements: (1) Weight: 305g→280g (5% reduction addressing fatigue), (2) Display: 4K per eye→8K equivalent (92 pixels-per-degree vs 70 PPD Vision Pro 1), full-color passthrough cameras enabling seamless virtual-physical interaction, (3) Hand-eye tracking: reduced latency, improved accuracy for UI interaction, (4) Optics: pancake lenses reducing form factor further. Price: $3,500 (unchanged), but performance/capability gap justifying enterprise use cases: surgical training (spatial anatomy visualization), architectural design (VR walkthroughs), industrial maintenance (remote assistance with overlaid instructions). Strategic significance for India: Spatial computing emerging as the next computing platform after smartphones — critical for India's tech sovereignty. India's opportunity: (1) Enterprise XR adoption in manufacturing (Bajaj, Maruti, TVS) improving worker training and remote support, (2) AR applications for agriculture (crop disease diagnosis, precision irrigation visualization) addressing India's farming challenges, (3) Indian XR developers (Pixelverse, Invento Robotics) creating localized apps for enterprise/consumer markets. However, India remains dependent on Apple, Meta (Quest) hardware imports — total XR device sales in India ~500,000/year, vs China 5+ million. India's strategy: support indigenous XR device manufacturing (incentives via Make-in-India 2.0) and developer ecosystems (government grants for XR startup incubation), aiming for 5+ million domestic XR devices sold by 2030, competing with global platforms.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Long COVID / Persistent Post-COVID Condition ---
        {
            "id": 26145,
            "question_text": "Long COVID (Post-Acute Sequelae of COVID-19, PASC) affects 10-30% of COVID-19 survivors. By 2024-25, which mechanistic understanding emerged as most supported by research?",
            "option_a": "Long COVID is purely psychological (persistent anxiety/PTSD) without physiological basis",
            "option_b": "Persistent viral replication in hidden tissue reservoirs (gut, brain, heart)",
            "option_c": "Viral persistence (low-level reactivation), dysregulated immune response (elevated cytokines), autonomic dysfunction, microclot formation, and mitochondrial dysfunction",
            "option_d": "Spike protein toxicity from vaccines (a controversial non-mainstream hypothesis)",
            "correct_answer": "C",
            "explanation": "Long COVID mechanisms (consensus by 2024-25 from NIH, WHO, Lancet reviews): (1) Viral persistence: SARS-CoV-2 RNA detected in plasma, stool, endothelial cells of long-COVID patients years post-infection; viral reactivation via immune dysregulation, (2) Immune dysregulation: elevated IL-6, TNF-alpha, type I interferon response; reduced T-cell counts and exhaustion, (3) Autonomic dysfunction: dysautonomia/POTS (postural orthostatic tachycardia) affecting 30-40% long-COVID patients, (4) Microclot formation: D-dimer elevation, platelet aggregates, thrombotic propensity, (5) Mitochondrial dysfunction: impaired ATP production in muscle, contributing to post-exertional malaise (PEM). No single mechanism; multifactorial with individual variability. Strategic significance for India: India's COVID-19 toll: 45+ million confirmed cases, estimated 400-500 million exposed (total). Long COVID prevalence in India: ~10-15 million people suffering persistent fatigue, cognitive impairment ('brain fog'), dyspnea, autonomic symptoms. India's medical response: (1) National Long COVID Registry (ICMR-led, launched 2023) collecting epidemiology, enabling rehabilitation studies, (2) AYUSH integration: yoga, Ayurveda's approach to immune restoration (rasayana therapy) evaluated in Long COVID (IIT-KGP, AIIMS Delhi trials 2024-25), (3) Rehabilitation pathways: cardiac rehabilitation, cognitive training, autonomic rebalancing protocols scaled via NRHM. India's pharmaceutical opportunity: identifying biomarkers (D-dimer, IL-6, viral RNA levels) stratifying long-COVID patients for targeted therapies — immunosuppression (low-dose immunotherapy), anticoagulation (thrombosis prevention), or antivirals (persistent-virus targeting). Research funding via DBT (Department of Biotechnology) can accelerate India's long-COVID solutions, generating global health impact for the 50+ million long-COVID worldwide.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
    ]

    if USE_POSTGRES:
        sql = f"""INSERT INTO questions
            (id, question_text, option_a, option_b, option_c, option_d,
             correct_answer, explanation, folder, topic)
            VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})
            ON CONFLICT (id) DO NOTHING"""
    else:
        sql = f"""INSERT OR IGNORE INTO questions
            (id, question_text, option_a, option_b, option_c, option_d,
             correct_answer, explanation, folder, topic)
            VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"""

    if USE_POSTGRES:
        cur2 = conn.cursor()
    else:
        cur2 = conn.cursor()

    inserted = 0
    for q in questions:
        try:
            cur2.execute(sql, (q["id"], q["question_text"], q["option_a"], q["option_b"],
                               q["option_c"], q["option_d"], q["correct_answer"],
                               q["explanation"], q["folder"], q["topic"]))
            inserted += 1
        except Exception as e:
            print(f"[seed_science_tech] Skipping ID {q['id']}: {e}")
            try: conn.rollback()
            except: pass

    conn.commit()
    conn.close()
    print(f"[seed_science_tech] Inserted {inserted}/{len(questions)} questions (IDs 26001–26099, 26100–26145).")


if __name__ == "__main__":
    seed()
