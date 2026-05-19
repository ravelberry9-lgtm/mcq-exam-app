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
            "explanation": "SpaDeX (Space Docking Experiment) is ISRO's technology demonstration mission to validate the ability to dock and undock small satellites in low-Earth orbit (LEO). It uses two satellites weighing approximately 220 kg each. Docking capability is critical for Gaganyaan and future lunar/space station missions.",
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
            "explanation": "Aditya-L1 was stationed at the Lagrange point L1, approximately 1.5 million kilometres from Earth (towards the Sun). From this position, the satellite can continuously observe the Sun without any eclipses. Its SUIT (Solar Ultraviolet Imaging Telescope) instrument observed a powerful solar flare and a rare plasma ejection.",
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
            "explanation": "NISAR (NASA-ISRO Synthetic Aperture Radar) is the first joint Earth observation mission between NASA and ISRO. It was launched on July 30, 2025 using ISRO's GSLV-F16 into a sun-synchronous polar orbit. It is the world's first dual-frequency SAR satellite using both L-band and S-band radar systems.",
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
            "explanation": "NISAR uses both L-band and S-band radar systems, making it the world's first dual-frequency Synthetic Aperture Radar (SAR) imaging satellite. L-band was contributed by NASA and S-band by ISRO. It studies Earth's surface changes related to earthquakes, landslides, glaciers, forests, and agriculture.",
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
            "explanation": "Chandrayaan-3 became the first mission in history to make a soft landing on the Moon's South Pole on August 23, 2023. India became the 4th country to soft-land on the Moon. August 23 is now celebrated as National Space Day in India. Lander: Vikram; Rover: Pragyan.",
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
            "explanation": "With Chandrayaan-3's successful landing on August 23, 2023, India became the 4th country to achieve a soft landing on the Moon, after the USA, USSR (Russia), and China. Moreover, it was the first ever landing on the lunar south pole.",
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
            "explanation": "Gaganyaan will make India the 4th nation to independently send humans to space, after USA, Russia (USSR), and China. The first crewed mission (Gaganyaan-4) is targeted for 2027. Uncrewed test flight Gaganyaan-G1 (with Vyommitra humanoid robot) is scheduled for December 2025, followed by G2 (2026) and G3 (2027) before the crewed flight.",
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
            "explanation": "ISRO Chairman V. Narayanan inaugurated the 'Shri S. Ramakrishnan Centre of Excellence in Fluid and Thermal Science Research' at IIT Madras on March 17, 2025. The centre focuses on spacecraft and launch vehicle thermal management for future lunar, Mars, and deep-space missions.",
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
            "explanation": "NASA's SPHEREx mission was launched on March 12, 2025 from Vandenberg Space Force Base. It will study 450 million galaxies and 100 million stars, creating a 3D map of the sky to understand the history of the universe. It orbits in a sun-synchronous orbit at 650 km above Earth.",
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
            "explanation": "NASA's PUNCH (Polarimeter to Unify the Corona and Heliosphere) mission was launched on March 12, 2025, alongside SPHEREx, on a single Falcon 9 rocket. It consists of four small satellites that study the solar corona, solar winds, and coronal mass ejections (CMEs) to improve space weather predictions.",
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
            "explanation": "NASA launched both the SPHEREx and PUNCH space missions together on March 12, 2025, from Vandenberg Space Force Base, California, using a SpaceX Falcon 9 rocket.",
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
            "explanation": "NASA's Europa Clipper mission is heading to Europa, one of Jupiter's moons. The spacecraft performed a Mars flyby in March 2025 and will perform an Earth flyby in December 2026, arriving at Europa in April 2030 to study its potential habitability (Europa has a subsurface ocean).",
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
            "explanation": "IIT Madras researchers developed a framework to enhance protection of critical infrastructure from ballistic missile threats. The framework helps designers improve the ballistic resistance of reinforced concrete (RC) panels. Findings were published in the journal Reliability Engineering & System Safety.",
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
            "explanation": "IIT Bombay's National Centre for Photovoltaic Research and Education (NCPRE) developed a high-efficiency tandem solar cell with nearly 30% power conversion efficiency, a major advancement for solar energy technology.",
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
            "explanation": "IIT Madras launched India's first cancer genome database to boost cancer research across the country. This database catalogues genomic data on Indian cancer types, enabling more targeted cancer diagnosis and treatment research.",
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
            "explanation": "AMRSense is an AI-powered tool developed by IIIT-Delhi researchers. It analyzes hospital data to provide early insights on Antimicrobial Resistance (AMR) patterns. This is critical for combating the growing global threat of drug-resistant infections.",
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
            "explanation": "Researchers at IISc developed a technique using the bacterium Sporosarcina pasteurii with guar gum to create bricks from lunar and Martian soil simulants (regolith). The bacterium converts urea and calcium into calcium carbonate crystals, binding soil particles. This eco-friendly method supports NASA's Artemis programme goal of permanent lunar settlements.",
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
            "explanation": "Multiple Sclerosis (MS) is an autoimmune disorder that occurs when the immune system attacks the brain and spinal cord. It affects nearly 1 million people in the US and over 2.8 million worldwide. Recent studies show gut microbiome imbalance can predict MS severity.",
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
            "explanation": "A Coronal Mass Ejection (CME) is a massive burst of solar plasma and magnetic field from the Sun's corona. CMEs can affect Earth's magnetosphere and cause geomagnetic storms. NASA's PUNCH mission (4 satellites) studies solar corona, solar winds, and CMEs to improve space weather predictions.",
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
            "explanation": "Lunar Regolith is the loose soil and rock covering the Moon's surface. IISc used lunar and Martian soil simulants (regolith) in their bacteria-based technique to create bricks for future lunar habitats under NASA's Artemis programme, which aims to establish permanent Moon settlements.",
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
            "explanation": "Sonic weapons, also called acoustic weapons, emit loud, painful sounds over long distances. They use audible or inaudible sound waves to disrupt, disorient, or incapacitate people. They were first developed for military use; the US used them in Iraq in 2004. Serbia was recently accused of using them against protesters in Belgrade.",
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
            "explanation": "The Serbian government was accused of using sonic weapons (acoustic weapons) to disperse protesters in Belgrade, Serbia's capital. Sonic weapons emit concentrated sound beams causing discomfort, pain, and disorientation. The US first used sonic weapons in Iraq in 2004.",
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
            "explanation": "ISRO is developing a LOX-methane (Liquid Oxygen + methane) engine for the Next Generation Launch Vehicle (NGLV). This propellant combination is cleaner and supports reusability. NGLV will have a reusable booster stage and two expendable upper stages.",
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
            "explanation": "PSLV-C61/EOS-09 (Earth Observation Satellite-09) was launched by ISRO on May 18, 2025. EOS satellites provide Earth observation data for various applications including agriculture, forestry, disaster management, and urban planning.",
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
            "explanation": "SPHEREx (Spectro-Photometer for the History of the Universe, Epoch of Reionization and Ices Explorer) will measure the near-infrared spectra of hundreds of millions of galaxies, creating a 3D map of the sky to understand the history of the universe. It entered a sun-synchronous orbit 650 km above Earth.",
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
            "explanation": "Chandrayaan-3's lander is named Vikram (after ISRO founder Vikram Sarabhai) and the rover is named Pragyan (meaning 'wisdom' in Sanskrit). They landed on the Moon's South Pole on August 23, 2023.",
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
            "explanation": "The first crewed Gaganyaan mission (Gaganyaan-4) is targeted for 2027. Before this, three uncrewed test flights are planned: Gaganyaan-G1 (Dec 2025, with the Vyommitra humanoid robot), G2 (2026), and G3 (2027). Crew Module Recovery trials began in 2024-25. The European Space Agency (ESA) and NASA also support Indian human spaceflight.",
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
            "explanation": "DNA barcoding is a technique for identifying species using short, standardized DNA sequences from a specific gene region. The Zoological Survey of India (ZSI) used DNA barcoding to correctly identify blackfly species that spread River Blindness (Onchocerciasis).",
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
            "explanation": "The SUIT (Solar Ultraviolet Imaging Telescope) onboard Aditya-L1 made a first-of-its-kind observation of a rare plasma ejection in ultraviolet light and also observed a powerful solar flare. Aditya-L1 is stationed at Lagrange Point L1, approximately 1.5 million km from Earth.",
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
            "explanation": "ESA's Biomass satellite is the 7th Earth Explorer satellite under ESA's climate and Earth systems programme. It was launched using the Vega C rocket from French Guiana (end of April 2025) to study global forests and measure carbon levels.",
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
            "explanation": "NISAR (NASA-ISRO SAR) studies Earth's surface changes related to earthquakes, landslides, glaciers, forests, and agriculture. It is the world's first dual-frequency radar imaging satellite, using both L-band and S-band SAR systems. Launched July 30, 2025 via ISRO's GSLV-F16.",
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
            "explanation": "A Sun-Synchronous Orbit (SSO) is a type of polar orbit where the satellite passes over any given point on Earth's surface at approximately the same local solar time each day. This ensures consistent lighting conditions for imaging. Both SPHEREx and NISAR use sun-synchronous orbits.",
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
            "explanation": "NASA's Artemis programme aims to return humans to the Moon and establish permanent lunar settlements. IISc developed a bacteria-based technique (using Sporosarcina pasteurii) to create and repair bricks from lunar regolith, supporting the Artemis goal of self-sustaining Moon habitats.",
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
            "explanation": "SpaDeX (Space Docking Experiment) uses two satellites weighing approximately 220 kg each in Low Earth Orbit. The mission validates India's docking/undocking capability, a prerequisite for Gaganyaan and future space station missions.",
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
            "explanation": "V. Narayanan is the Chairman of ISRO who inaugurated the 'Shri S. Ramakrishnan Centre of Excellence in Fluid and Thermal Science Research' at IIT Madras on March 17, 2025. The centre is named after S. Ramakrishnan, an IIT Madras alumnus who contributed to PSLV and GSLV MK3 development.",
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
            "explanation": "River Blindness (Onchocerciasis) spreads through the bite of infected blackflies of the genus Simulium. These blackflies breed near fast-flowing rivers and streams. The disease causes severe skin itching, skin damage, and in serious cases, permanent blindness.",
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
            "explanation": "African Swine Fever first emerged in India in Mizoram, specifically in Lungsen village, Lunglei, on March 21, 2021. It has since become endemic in Mizoram. ASF is caused by ASFV (African Swine Fever Virus) and has no vaccine or treatment.",
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
            "explanation": "NISAR (NASA-ISRO Synthetic Aperture Radar) was launched on July 30, 2025, using ISRO's GSLV-F16 into a sun-synchronous polar orbit. NISAR is the first joint Earth observation mission between NASA and ISRO.",
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
            "explanation": "IIT Madras launched India's first cancer genome database to boost cancer research. This database enables the study of genomic patterns of cancers occurring in Indian populations, supporting more targeted diagnosis and treatment strategies.",
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
            "explanation": "NASA's SPHEREx satellite orbits Earth at 650 km above the surface in a sun-synchronous orbit. It studies 450 million galaxies and 100 million stars, creating a 3D map of the universe's history.",
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
            "explanation": "SUIT stands for Solar Ultraviolet Imaging Telescope. It is one of the instruments onboard India's Aditya-L1 solar mission. SUIT made a first-of-its-kind observation of a rare plasma ejection in ultraviolet light and observed a powerful solar flare.",
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
            "explanation": "NASA's SPHEREx and PUNCH missions were launched together on March 12, 2025, from Vandenberg Space Force Base, California, using a Falcon 9 rocket.",
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
            "explanation": "ESA's Biomass satellite was launched using the Vega C rocket from French Guiana (European Spaceport) by the end of April 2025. Vega C is the European Space Agency's small-to-medium payload launch vehicle.",
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
            "explanation": "Europa, one of Jupiter's moons, is believed to harbor a subsurface liquid water ocean beneath its icy surface. This makes it one of the most promising candidates for extraterrestrial life in our solar system. NASA's Europa Clipper (arriving April 2030) will study Europa's potential habitability.",
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
            "explanation": "Lumpy Skin Disease (LSD) is caused by Capripoxvirus, a DNA virus. It primarily affects cattle and buffalo, causing nodular skin lesions, fever, and reduced milk production. It spreads through insects (mosquitoes, flies). Major outbreaks occurred in India between 2022–2024.",
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
            "explanation": "GSLV stands for Geosynchronous Satellite Launch Vehicle. ISRO uses GSLV to launch heavier satellites, including the GSLV-F16 that launched NISAR on July 30, 2025. GSLV MK3 (also called LVM3) is a more powerful version used for heavier payloads.",
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
            "explanation": "Multiple Sclerosis (MS) affects nearly 1 million people in the USA and over 2.8 million people worldwide. It is an autoimmune disorder where the immune system attacks the brain and spinal cord. Recent studies link gut microbiome imbalance to MS severity.",
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
            "explanation": "IIT Madras researchers published their findings on a framework for enhancing protection of reinforced concrete (RC) panels against ballistic missile threats in the journal Reliability Engineering & System Safety. The framework helps designers improve ballistic resistance of infrastructure like military bunkers and nuclear power buildings.",
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
            "explanation": "SPHEREx (launched March 12, 2025) will create a 3D map of the sky by measuring near-infrared spectra of hundreds of millions of galaxies (450 million) and 100 million stars. This will help understand the history and large-scale structure of the universe.",
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
            "explanation": "AMR stands for Antimicrobial Resistance — when bacteria, viruses, fungi, and parasites evolve to resist the effects of medicines (antibiotics, antivirals, etc.), making infections harder to treat. IIIT-Delhi's AMRSense is an AI tool that helps track AMR patterns using hospital data.",
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
            "explanation": "LUPEX (Lunar Polar Exploration Mission) is a planned joint mission between ISRO and JAXA (Japan Aerospace Exploration Agency) to explore the Moon's polar region and study water ice resources. ISRO will provide the lander while JAXA will provide the rover.",
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
            "explanation": "NCPRE stands for National Centre for Photovoltaic Research and Education at IIT Bombay. Researchers there developed a high-efficiency tandem solar cell with nearly 30% power conversion efficiency, a significant advancement in solar energy technology.",
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
            "explanation": "ESA's Biomass satellite uses radar technology to quantify forest biomass and carbon content from space and will also create detailed 3D models of forest structures. It will monitor changes over time, helping climate research and forest conservation efforts.",
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
            "explanation": "In IISc's technique, guar gum is combined with the bacterium Sporosarcina pasteurii to create bricks from lunar and Martian soil simulants. The bacterium converts urea and calcium into calcium carbonate crystals, with guar gum helping to bind the soil particles together.",
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
            "explanation": "National Space Day is celebrated in India on August 23, the date Chandrayaan-3's Vikram lander successfully touched down on the Moon's South Pole in 2023, making India the first country to land on the lunar south pole.",
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
            "explanation": "ZSI stands for Zoological Survey of India. It used DNA barcoding to correctly identify blackfly species (genus Simulium) that spread River Blindness (Onchocerciasis). The Zoological Survey of India is an autonomous organization under India's Ministry of Environment, Forests and Climate Change.",
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
            "explanation": "The centre is named after S. Ramakrishnan, an IIT Madras alumnus and former ISRO Chairman who contributed significantly to the development of PSLV and GSLV MK3. ISRO Chairman V. Narayanan inaugurated the centre at IIT Madras on March 17, 2025.",
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
            "explanation": "NASA's Europa Clipper performed a flyby maneuver at Mars in March 2025 to gain speed and trajectory for its long voyage to Jupiter's moon Europa. It will also perform an Earth flyby in December 2026 before arriving at Europa in April 2030.",
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
            "explanation": "ISRO's Next Generation Launch Vehicle (NGLV) will have a reusable booster stage (similar to SpaceX Falcon 9 concept) with two expendable upper stages. It uses a LOX-methane engine. The reusability is key to reducing the cost of space access.",
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
            "explanation": "Bird Flu (Avian Influenza) is caused by Influenza A virus, particularly strains H5N1 and H5N2. It is zoonotic (can spread from birds to humans under certain conditions). Mass culling of affected poultry is a standard control measure.",
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
            "explanation": "PUNCH stands for Polarimeter to Unify the Corona and Heliosphere. It is a NASA solar mission consisting of four small satellites that study the solar corona, solar winds, and coronal mass ejections (CMEs). It was launched alongside SPHEREx on March 12, 2025.",
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
            "explanation": "LPSC stands for Liquid Propulsion Systems Centre, an ISRO center responsible for developing liquid propulsion systems and engines. LPSC is developing the LOX-methane engine for the Next Generation Launch Vehicle (NGLV) and developed a spark torch igniter tested on March 3, 2025.",
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
            "explanation": "Aditya-L1 was stationed at Lagrange Point L1, approximately 1.5 million km from Earth (towards the Sun). This position allows continuous observation of the Sun without eclipses. India launched Aditya-L1 in September 2023.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- GSLV MK3 / LVM3 ---
        {
            "id": 26074,
            "question_text": "GSLV MK3, also known as LVM3, is used by ISRO for what purpose?",
            "option_a": "Launching small satellites into LEO",
            "option_b": "Launching heavier payloads including crew capsule for Gaganyaan",
            "option_c": "Anti-satellite weapon testing",
            "option_d": "Launching Earth observation satellites to polar orbits only",
            "correct_answer": "B",
            "explanation": "GSLV MK3 (Geosynchronous Satellite Launch Vehicle Mark III), also called LVM3 (Launch Vehicle Mark 3), is ISRO's heaviest launch vehicle. It is used for launching heavier communication satellites to GTO (Geostationary Transfer Orbit) and is also the designated launch vehicle for the Gaganyaan crewed mission.",
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
            "explanation": "NISAR is designed to observe every part of Earth's surface once every 12 days, generating a massive volume of data. This frequent coverage helps track changes over time in glaciers, forests, earthquakes, and more. It is the world's first dual-frequency (L-band + S-band) SAR satellite.",
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
            "explanation": "Group Captain Shubhanshu Shukla became the first Indian to board the International Space Station (ISS) as part of Axiom Mission 4 (Ax-4), launched on June 25, 2025 from Kennedy Space Center aboard SpaceX's Dragon spacecraft. He served as mission pilot. The mission concluded on July 15, 2025 after ~18 days on the ISS.",
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
            "explanation": "Wing Commander Rakesh Sharma was the first Indian to travel to space in 1984 aboard the Soviet Soyuz T-11 mission. Shubhanshu Shukla became the second Indian in space after a gap of over 40 years, as part of Axiom Mission 4 to the ISS in June 2025. Sunita Williams is an Indian-American NASA astronaut.",
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
            "explanation": "Axiom Mission 4 was commanded by Peggy Whitson, a former NASA astronaut and now an Axiom Space employee. The crew also included Shubhanshu Shukla (India/ISRO), Sławosz Uznański-Wiśniewski (Poland/ESA), and Tibor Kapu (Hungary). Shubhanshu Shukla served as mission pilot.",
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
            "explanation": "Four Gaganyatris (astronaut candidates) were selected by ISRO for the Gaganyaan programme: Group Capt. Shubhanshu Shukla, Group Capt. Prashanth Balakrishnan Nair, Group Capt. Ajit Krishnan, and Group Capt. Angad Pratap. All four were trained at Yuri Gagarin Cosmonaut Training Center in Russia.",
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
            "explanation": "Axiom Mission 4 (Ax-4) was launched from Kennedy Space Center on June 25, 2025, using SpaceX's Falcon 9 rocket with Dragon spacecraft. The crew docked with the ISS and returned on July 15, 2025, splashing down in the Pacific Ocean near San Diego. Shubhanshu Shukla became the first Indian to board the ISS.",
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
            "explanation": "NASA's Artemis-2 was launched on April 2, 2026 from Kennedy Space Center using the Space Launch System (SLS) rocket and Orion spacecraft. The 10-day crewed lunar flyby mission concluded with a successful splashdown on April 11, 2026 in the Pacific Ocean off the coast of California — the first crewed Moon mission since Apollo 17 in 1972.",
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
            "explanation": "Artemis-2 travelled 2,52,760 miles (~4,06,800 km) from Earth, looping behind the Moon — a new record for the farthest distance ever travelled by humans, surpassing Apollo 13's 1970 record. The crew: Reid Wiseman (Commander, NASA), Victor Glover (Pilot, NASA), Christina Koch (Mission Specialist, NASA) and Jeremy Hansen (Mission Specialist, CSA — first Canadian to fly to the Moon).",
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
            "explanation": "Jeremy Hansen of the Canadian Space Agency (CSA) became the first non-American (and first Canadian) to fly to the Moon as a Mission Specialist on Artemis-2 (April 2-11, 2026). The launch vehicle was NASA's Space Launch System (SLS) carrying the Orion spacecraft.",
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
            "explanation": "LVM3-M6, launched on December 24, 2025, marked the 100th launch from Satish Dhawan Space Centre (SHAR), Sriharikota. It deployed AST SpaceMobile's BlueBird Block-2 satellite — the heaviest commercial payload (~6,500 kg) ever launched by ISRO. The BlueBird Block-2 is one of the world's largest commercial communication satellites with a 64 sq.m antenna array.",
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
            "explanation": "BlueBird Block-2 was built by AST SpaceMobile (USA). It is one of the largest commercial satellites with a 64 sq.m phased-array antenna designed to deliver direct-to-cell broadband 5G connectivity from space — connecting standard smartphones without ground infrastructure. NSIL signed the commercial launch contract with AST SpaceMobile.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- NavIC-16 / IRNSS-1K (PSLV-C58 Jan 2026) ---
        {
            "id": 26086,
            "question_text": "ISRO launched the NavIC navigation satellite NVS-02/IRNSS-1K (also called NavIC-16) on January 29, 2025 using which launch vehicle?",
            "option_a": "PSLV-C58",
            "option_b": "GSLV-F15",
            "option_c": "LVM3-M5",
            "option_d": "SSLV-D3",
            "correct_answer": "B",
            "explanation": "ISRO launched NVS-02 (the second second-generation NavIC satellite) on January 29, 2025, using GSLV-F15 from Sriharikota. NavIC (Navigation with Indian Constellation) is India's regional satellite navigation system covering India and a 1,500 km region around it, designed as an indigenous alternative to GPS.",
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
            "explanation": "The Bharatiya Antariksh Station (BAS) will have 5 modules. The first module (BAS-1) is targeted for launch in 2028 and the full station is to be operational by 2035. It will orbit Earth at ~400 km and weigh approximately 52 tonnes when complete — India's own crewed space station, supporting microgravity research and crewed missions.",
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
            "explanation": "The first module of Bharatiya Antariksh Station (BAS-1) is targeted for 2028, with the full 5-module station operational by 2035. The Cabinet approved the BAS project in September 2024 as part of the Gaganyaan extension and India's roadmap to a crewed Moon landing by 2040.",
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
            "explanation": "Chandrayaan-4 was approved by the Union Cabinet on September 18, 2024. It will demonstrate lunar sample-return technology — collecting samples from the Moon's south polar region and bringing them back to Earth. The mission has a complex 5-module architecture launched on two separate LVM3 rockets and is targeted for 2027.",
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
            "explanation": "The full SpaceX Super Heavy + Starship stack measures approximately 120 m (~395 ft) — the tallest and most powerful rocket ever built, producing ~74 MN of thrust at lift-off. After failures in IFT-7, 8 and 9 (early 2025), SpaceX achieved Booster catch with the launch tower's 'Mechazilla' chopsticks and successful Starship upper-stage demos through IFT-11 and IFT-12 (late 2025/early 2026).",
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
            "explanation": "The Amaravati Quantum Computing Centre (AQCC), inaugurated by the Andhra Pradesh government in January 2026 as part of the 'Quantum Valley' initiative, hosts IBM's Quantum System Two with the 156-qubit Heron R2 processor — the largest quantum computer deployed in India. The centre is a joint initiative of AP government, IBM and TCS.",
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
            "explanation": "The 2025 Nobel Prize in Physics was awarded jointly to John Clarke (UK/US), Michel H. Devoret (France/US) and John M. Martinis (US) for the discovery of macroscopic quantum mechanical tunnelling and energy quantisation in an electric circuit. Their work on Josephson junctions in the 1980s laid the groundwork for today's superconducting qubits used in quantum computers.",
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
            "explanation": "The 2025 Nobel Prize in Chemistry was awarded jointly to Susumu Kitagawa (Japan), Richard Robson (UK/Australia) and Omar M. Yaghi (Jordan/US) for the development of Metal-Organic Frameworks (MOFs). MOFs are porous crystalline materials with vast internal surface areas, used in carbon capture, hydrogen storage, water harvesting from desert air, and drug delivery.",
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
            "explanation": "The 2025 Nobel Prize in Physiology or Medicine was awarded jointly to Mary E. Brunkow (US), Fred Ramsdell (US) and Shimon Sakaguchi (Japan) for discoveries concerning peripheral immune tolerance. They identified regulatory T cells (Tregs) and the FOXP3 gene — explaining how the immune system avoids attacking the body's own tissues, a foundation for treating autoimmune diseases.",
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
            "explanation": "OpenAI released GPT-5 on August 7, 2025, with default unified-reasoning, native multimodal input (text, images, audio, video) and a Pro tier. It replaced GPT-4o and the o-series as ChatGPT's default model. A 'GPT-5 Pro' tier provides extended reasoning for the most complex tasks.",
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
            "explanation": "Google DeepMind released Gemini 3.0 (with Gemini 3 Pro variant) in November-December 2025 as its most capable multimodal AI model — featuring 'agentic' capabilities, the Antigravity agent IDE, and an expanded 1-million-token context window. It powers Google Search's AI Mode and AI Studio.",
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
            "explanation": "DeepSeek R1 was released on January 20, 2025 by DeepSeek, a Hangzhou-based Chinese AI company. The open-weights reasoning model achieved performance comparable to OpenAI's o1 at a fraction of the training cost, triggering an ~$1 trillion drop in US tech stocks (including a $600 billion loss for NVIDIA) on January 27, 2025.",
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
            "explanation": "Anthropic released Claude Opus 4 in May 2025 as the most capable model in the Claude 4 family, with leading-edge coding, agentic and reasoning abilities. Opus 4 introduced extended thinking and hybrid reasoning modes. Claude Opus 4.5 followed in late 2025.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- AI Agents (Operator, Manus) ---
        {
            "id": 26100,
            "question_text": "OpenAI launched 'Operator', its autonomous AI agent that can browse the web and complete tasks on behalf of users, in which month of 2025?",
            "option_a": "January 2025",
            "option_b": "March 2025",
            "option_c": "July 2025",
            "option_d": "October 2025",
            "correct_answer": "A",
            "explanation": "OpenAI launched 'Operator' on January 23, 2025 as a research preview for ChatGPT Pro subscribers in the US. Built on the Computer-Using Agent (CUA) model, Operator autonomously browses the web, fills forms and books services. China's 'Manus' AI agent (Butterfly Effect AI) launched in March 2025 as a competing general-purpose autonomous agent.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Mission Mausam ---
        {
            "id": 26101,
            "question_text": "Mission Mausam, launched by the Government of India in September 2024 to make India 'weather-ready and climate-smart', is led by which ministry?",
            "option_a": "Ministry of Environment, Forests & Climate Change",
            "option_b": "Ministry of Earth Sciences",
            "option_c": "Ministry of Science and Technology",
            "option_d": "Ministry of Agriculture",
            "correct_answer": "B",
            "explanation": "Mission Mausam was approved by the Union Cabinet on September 11, 2024 with a Rs 2,000 crore outlay for 2024-26. Led by the Ministry of Earth Sciences (MoES) and implemented by IMD, IITM (Pune) and NCMRWF, it aims at high-accuracy weather forecasts, cloud-seeding research and a 'Bharat Forecasting System' to make India weather-ready and climate-smart.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- CRISPR Casgevy ---
        {
            "id": 26102,
            "question_text": "Casgevy (exa-cel), the world's first approved CRISPR/Cas9 gene-editing therapy, treats which conditions?",
            "option_a": "Type-1 diabetes and Crohn's disease",
            "option_b": "Sickle cell disease and transfusion-dependent beta thalassemia",
            "option_c": "Alzheimer's disease and Parkinson's disease",
            "option_d": "Cystic fibrosis and Duchenne muscular dystrophy",
            "correct_answer": "B",
            "explanation": "Casgevy (exagamglogene autotemcel / exa-cel), developed by Vertex Pharmaceuticals and CRISPR Therapeutics, is the world's first approved CRISPR/Cas9 gene-editing therapy. It treats sickle cell disease (SCD) and transfusion-dependent beta thalassemia. Approved by UK MHRA (Nov 2023), US FDA (Dec 2023), EMA (Feb 2024), and expanded to additional countries through 2025.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- HL-LHC ---
        {
            "id": 26103,
            "question_text": "CERN's HL-LHC (High-Luminosity Large Hadron Collider) upgrade, scheduled to start operations in 2030, is designed to do what?",
            "option_a": "Discover the Higgs boson for the first time",
            "option_b": "Increase the LHC's luminosity (collision rate) by a factor of about 10",
            "option_c": "Detect dark matter particles for the first time",
            "option_d": "Replace the LHC with a circular muon collider",
            "correct_answer": "B",
            "explanation": "The High-Luminosity Large Hadron Collider (HL-LHC) is a major CERN upgrade designed to increase the LHC's luminosity (proton collision rate) by approximately 10 times — from ~1 to ~7.5 × 10^34 cm^-2 s^-1. Civil works are nearing completion in 2025-26, with first beams targeted for 2030. It will deliver ~3000/fb integrated luminosity over its lifetime.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Apple Vision Pro 2 ---
        {
            "id": 26104,
            "question_text": "Apple released the Vision Pro 2 (M5 chip variant), the successor to its 2024 mixed-reality headset, in which year?",
            "option_a": "Late 2024",
            "option_b": "Mid 2025",
            "option_c": "Late 2025",
            "option_d": "Early 2026",
            "correct_answer": "C",
            "explanation": "Apple released the updated Vision Pro (M5 chip variant, often called 'Vision Pro 2025') in October 2025 — featuring the new M5 processor, longer battery life and a redesigned Dual Knit Band. A larger redesign with a lighter, lower-cost variant is expected in 2026-27.",
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
            "explanation": "During its first year of observations (January 2024-25), Aditya-L1's full payload suite — VELC, SUIT, SoLEXS, HEL1OS, ASPEX, PAPA and MAG — captured multiple major Coronal Mass Ejections (CMEs) and solar flares during Solar Cycle 25's maximum. VELC was the first Indian space-based coronagraph to observe the Sun's corona at 1.05 solar radii.",
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
            "explanation": "Vyommitra (Sanskrit for 'Space Friend') is a half-humanoid robot built by ISRO's Inertial Systems Unit. It will fly aboard the uncrewed Gaganyaan-G1 test mission (Dec 2025) to simulate human functions, monitor onboard systems, perform life-support experiments and respond to commands — validating crew safety before the crewed Gaganyaan-4 mission.",
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
            "explanation": "The National Quantum Mission (NQM) was approved by the Union Cabinet on April 19, 2023 with an outlay of Rs 6,003.65 crore for 2023-31 (8 years). It aims to develop quantum computers (50-1000 physical qubits), satellite-based secure quantum communication, magnetometers and atomic clocks. Four T-Hubs lead R&D: IISc, IITs Madras-Bombay-Delhi.",
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
            "explanation": "Tianwen-2 was launched on May 29, 2025 by China's CNSA. It is a dual-target mission: first, collect samples from the near-Earth quasi-satellite asteroid 2016 HO3 (Kamo'oalewa) and return them to Earth around 2027, then continue to explore main-belt comet 311P/PANSTARRS through 2035. It is China's first sample-return mission from an asteroid.",
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
            "explanation": "SpaDeX achieved India's first successful in-space docking on January 16, 2025, making India the 4th country to demonstrate docking in space (after USA, Russia/USSR and China). The Chaser (SDX-01) and Target (SDX-02) satellites — ~220 kg each — were launched on December 30, 2024 by PSLV-C60. Undocking was successfully performed on March 13, 2025.",
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
        # --- ISRO POEM-4 / SpaDeX hosted experiments ---
        {
            "id": 26125,
            "question_text": "ISRO's POEM-4 (PSLV Orbital Experimental Module-4), flown on PSLV-C60 in December 2024, hosted 24 experiments including India's first space-grown crop. Which seed was germinated in microgravity?",
            "option_a": "Spinach (Spinacia oleracea)",
            "option_b": "Cowpea (Vigna unguiculata)",
            "option_c": "Tomato (Solanum lycopersicum)",
            "option_d": "Rice (Oryza sativa)",
            "correct_answer": "B",
            "explanation": "On the POEM-4 platform (PSLV-C60, Dec 30, 2024), ISRO's CROPS (Compact Research module for Orbital Plant Studies) successfully germinated cowpea (Vigna unguiculata) seeds in microgravity within 4 days — the first Indian space-grown crop. POEM-4 hosted 24 experiments from ISRO, IN-SPACe-recognised startups and Indian academic institutions.",
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
    print(f"[seed_science_tech] Inserted {inserted}/{len(questions)} questions (IDs 26001–26130).")


if __name__ == "__main__":
    seed()
