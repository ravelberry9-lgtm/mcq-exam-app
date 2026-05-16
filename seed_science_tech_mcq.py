"""
Seed: Science, Space & Technology — Current Affairs 2024-2026
IDs: 26001–26080
Folder: AP_HC
Topic: National_Current_Affairs
Cross-checked: GKToday Science & Technology MCQs (Page 1), ISRO, NASA, PIB
"""

import sqlite3, os

def get_db():
    base = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base, "database.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def seed():
    conn = get_db()
    cur = conn.cursor()

    # Idempotency check
    cur.execute("SELECT COUNT(*) FROM questions WHERE id >= 26001 AND id <= 26080")
    if cur.fetchone()[0] >= 75:
        conn.close()
        return

    ph = "?"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
        },
        {
            "id": 26009,
            "question_text": "India's Gaganyaan programme, if successful, will make India the how-many-th nation to independently send humans to space?",
            "option_a": "3rd",
            "option_b": "4th",
            "option_c": "5th",
            "option_d": "6th",
            "correct_answer": "B",
            "explanation": "Gaganyaan will make India the 4th nation to independently send humans to space, after USA, Russia (USSR), and China. The first crewed mission (Gaganyaan-4) is targeted for 2027–28. Uncrewed test flights (Gaganyaan-1, -2, -3) are planned for 2025–26.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
        },
        # --- Gaganyaan ---
        {
            "id": 26037,
            "question_text": "The first crewed Gaganyaan mission is targeted for which year?",
            "option_a": "2025",
            "option_b": "2026",
            "option_c": "2027–28",
            "option_d": "2030",
            "correct_answer": "C",
            "explanation": "The first crewed Gaganyaan mission (Gaganyaan-4) is targeted for 2027–28. Before this, three uncrewed test flights (Gaganyaan-1, -2, -3) are planned for 2025–26. The European Space Agency (ESA) is also supporting Indian human spaceflight missions.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
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
            "topic": "National_Current_Affairs"
        },
        # --- GSLV S. Ramakrishnan contribution ---
        {
            "id": 26076,
            "question_text": "The 'Shri S. Ramakrishnan Centre of Excellence' at IIT Madras focuses on research critical for which types of missions?",
            "option_a": "Communications and navigation satellites",
            "option_b": "Solar observation missions",
            "option_c": "Spacecraft and launch vehicle thermal management for deep-space missions",
            "option_d": "Geospatial imaging satellites",
            "correct_answer": "C",
            "explanation": "The Shri S. Ramakrishnan Centre at IIT Madras focuses on spacecraft and launch vehicle thermal management, which is crucial for future lunar, Mars, and deep-space missions under ISRO's Atmanirbhar Bharat initiative. ISRO scientists will collaborate with IIT Madras to develop advanced cooling systems.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Atmospheric/climate ---
        {
            "id": 26077,
            "question_text": "Chandrayaan-3's Pragyan rover is named after a Sanskrit word meaning what?",
            "option_a": "Power",
            "option_b": "Explorer",
            "option_c": "Wisdom",
            "option_d": "Light",
            "correct_answer": "C",
            "explanation": "Pragyan is a Sanskrit word meaning 'wisdom'. It is the name of the rover deployed by Chandrayaan-3's lander Vikram after the historic south pole landing on August 23, 2023.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- ASFV spread ---
        {
            "id": 26078,
            "question_text": "African Swine Fever Virus (ASFV) can spread through which route?",
            "option_a": "Airborne transmission only",
            "option_b": "Direct pig-to-human contact",
            "option_c": "Contaminated clothing, equipment, or vehicles",
            "option_d": "Mosquito bites",
            "correct_answer": "C",
            "explanation": "African Swine Fever Virus (ASFV) can spread through contaminated clothing, equipment, or vehicles, as well as through direct contact between infected and healthy pigs. There is no vaccine or treatment for ASF. It does NOT spread to humans.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- ESA ---
        {
            "id": 26079,
            "question_text": "Which organization's 'Earth Explorer' programme includes the Biomass satellite designed to measure global forest carbon?",
            "option_a": "NASA",
            "option_b": "JAXA",
            "option_c": "European Space Agency (ESA)",
            "option_d": "Roscosmos",
            "correct_answer": "C",
            "explanation": "The Biomass satellite is the 7th Earth Explorer satellite under the European Space Agency's (ESA) climate and Earth systems programme. It was launched by Vega C rocket from French Guiana (end of April 2025) to map global forests and measure carbon levels.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Chandrayaan 4 ---
        {
            "id": 26080,
            "question_text": "Chandrayaan-4, India's next planned lunar mission, will aim to achieve what milestone?",
            "option_a": "First Indian rover on Mars",
            "option_b": "Sample return from the Moon",
            "option_c": "First Indian crewed Moon landing",
            "option_d": "Building a permanent Moon base",
            "correct_answer": "B",
            "explanation": "Chandrayaan-4 is India's next planned lunar mission and aims to achieve sample return from the Moon — collecting lunar samples and bringing them back to Earth for study. This will be a significantly more complex mission than Chandrayaan-3 and represents the next step in India's lunar exploration programme.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
    ]

    for q in questions:
        cur.execute(
            f"""INSERT OR IGNORE INTO questions
                (id, question_text, option_a, option_b, option_c, option_d,
                 correct_answer, explanation, folder, topic)
                VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
            (q["id"], q["question_text"], q["option_a"], q["option_b"],
             q["option_c"], q["option_d"], q["correct_answer"],
             q["explanation"], q["folder"], q["topic"])
        )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed()
    print("Science & Technology MCQs seeded: IDs 26001–26080")
