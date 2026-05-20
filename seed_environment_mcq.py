"""
Seed: Environment & Climate — Current Affairs 2024-2026
IDs: 25001–25100  (80 original + 20 freshness gap-fill added May 19, 2026)
Folder: AP_HC
Topic: National_Current_Affairs (wildlife, protected areas, COP, species — India-centric)
Cross-checked: GKToday, PIB, IUCN, NTCA, WMO, UNEP, CBD, CITES, Ramsar, UNFCCC
Freshness audit (May 19, 2026): refreshed Ramsar count (85→99), COP30 outcomes
(Belém Package → Global Mutirão + TFFF $6.7B), added 2025-26 events: WMO 1.55°C,
UNEP Emissions Gap 2025 (2.3-2.5°C), CBD COP16.2 Rome + Cali Fund, INC-5.2 Geneva,
UNOC3 Nice + BBNJ ratifications, Ramsar COP15 Victoria Falls, CITES CoP20 Samarkand,
Mission Mausam, ISFR 2023, LA wildfires Jan 2025, Bonn SB62, Shekha Jheel 99th Ramsar.
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

    # Force-refresh: delete and re-insert with correct folder/topic
    cur.execute("DELETE FROM questions WHERE id >= 25001 AND id <= 25100")
    conn.commit()

    ph = '%s' if USE_POSTGRES else '?'
    questions = [
        # --- Wildlife Sanctuaries ---
        {
            "id": 25001,
            "question_text": "Pobitora Wildlife Sanctuary, which has the highest density of Greater One-Horned Rhinoceros in India, is located in which state?",
            "option_a": "Sikkim",
            "option_b": "Assam",
            "option_c": "Manipur",
            "option_d": "Meghalaya",
            "correct_answer": "B",
            "explanation": "Pobitora Wildlife Sanctuary is located in eastern Guwahati, Assam, established in 1998 and spanning 48.81 sq km. It has the highest density of Greater One-Horned Rhinoceros in India and is part of the Indian Rhino Vision 2020 program, a critical biodiversity conservation initiative. The sanctuary protects this endangered species (listed under Schedule I of the Wildlife Protection Act) amid Assam's shifting cultivation pressures and river dynamics, demonstrating India's commitment to species recovery in biodiversity hotspots.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25002,
            "question_text": "Corbett Tiger Reserve, India's oldest tiger reserve, is located in which state?",
            "option_a": "Himachal Pradesh",
            "option_b": "Rajasthan",
            "option_c": "Gujarat",
            "option_d": "Uttarakhand",
            "correct_answer": "D",
            "explanation": "Corbett Tiger Reserve spans 1,288.31 sq km in the Himalayan foothills of Uttarakhand, established in 1936 as Hailey National Park and renamed in 1957 to honor conservationist Jim Corbett. As India's flagship tiger reserve under Project Tiger, it exemplifies habitat protection essential for India's 2070 Net-Zero targets and biodiversity conservation amid climate-driven habitat fragmentation. The reserve's management addresses transboundary water security via rivers Ramganga, Pallaen, and Sonanadi, crucial for downstream Himalayan communities.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25003,
            "question_text": "Karimpuzha Wildlife Sanctuary, which is part of the Nilgiri Biosphere Reserve, is located in which state?",
            "option_a": "Gujarat",
            "option_b": "Odisha",
            "option_c": "Kerala",
            "option_d": "Tamil Nadu",
            "correct_answer": "C",
            "explanation": "Karimpuzha Wildlife Sanctuary covers 227.97 sq km in Malappuram district, Kerala, on the Nilgiri Hills' western slopes and is part of the UNESCO Man and Biosphere Programme Nilgiri Biosphere Reserve. This biodiversity hotspot protects endemic Western Ghats species amid climate change impacts on forest hydrology and water security for Kerala. Its transboundary linkages with Silent Valley NP (Kerala) and Mukurthi NP (Tamil Nadu) demonstrate integrated landscape conservation crucial for species migration corridors.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25004,
            "question_text": "Nagarhole National Park, also known as Rajiv Gandhi National Park, is located in which state?",
            "option_a": "Tamil Nadu",
            "option_b": "Karnataka",
            "option_c": "Odisha",
            "option_d": "Maharashtra",
            "correct_answer": "B",
            "explanation": "Nagarhole National Park spans Kodagu and Mysuru districts in Karnataka and is a Tiger Reserve under Project Tiger, named after the Nagarahole River. This reserve protects critical Western Ghats biodiversity in an area threatened by climate-driven rainfall variability and agricultural encroachment. The park's river systems are vital for water security in the region, aligning with India's broader wetland conservation strategy under the Ramsar Convention.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25005,
            "question_text": "Balpakram National Park, known as the 'Land of Perpetual Winds', is located in which state?",
            "option_a": "Meghalaya",
            "option_b": "Assam",
            "option_c": "Tripura",
            "option_d": "Mizoram",
            "correct_answer": "A",
            "explanation": "Balpakram National Park spans the West Garo Hills district in Meghalaya, 134 km from Shillong, famed for persistent plateau winds that shape its microclimate. The park protects rare species including the Vulnerable Binturong, recently camera-trapped in its buffer zone, demonstrating successful species monitoring. Meghalaya's high rainfall and biodiverse forests are critical for water security in the Northeast India region and support forest carbon sequestration vital to India's 2070 Net-Zero pathway.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25006,
            "question_text": "Indravati National Park, where anti-Naxal operations are conducted, is located in which state?",
            "option_a": "Karnataka",
            "option_b": "Bihar",
            "option_c": "Chhattisgarh",
            "option_d": "Odisha",
            "correct_answer": "C",
            "explanation": "Indravati National Park in Bijapur district, Chhattisgarh protects biodiversity in a region strategically important for water security along the Godavari Basin. The Indravati River, which forms the park's northern and western boundaries (marking the Chhattisgarh–Maharashtra border), is critical for transboundary water management and downstream communities. This reserve exemplifies conservation challenges in India's mineral-rich zones where mining pressures conflict with forest ecosystem protection and climate resilience.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25007,
            "question_text": "India's largest Wildlife Sanctuary, Indian Wild Ass Sanctuary (4,954 sq km), is located in which state?",
            "option_a": "Rajasthan",
            "option_b": "Gujarat",
            "option_c": "Madhya Pradesh",
            "option_d": "Maharashtra",
            "correct_answer": "B",
            "explanation": "The Indian Wild Ass Sanctuary spans 4,954 sq km in Gujarat's Little Rann of Kutch, making it India's largest wildlife sanctuary. This arid-zone reserve protects the endemic Indian Wild Ass (Equus hemionus khur) and supports grassland ecosystems essential for carbon storage in dryland regions. The sanctuary faces climate-driven water scarcity challenges, requiring integrated water management aligned with India's water security and drought resilience goals under the 2070 Net-Zero framework.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25008,
            "question_text": "Keoladeo National Park (Bharatpur Bird Sanctuary), a UNESCO World Heritage Site, is located in which state?",
            "option_a": "Uttar Pradesh",
            "option_b": "Gujarat",
            "option_c": "Rajasthan",
            "option_d": "Haryana",
            "correct_answer": "C",
            "explanation": "Keoladeo National Park (Bharatpur Bird Sanctuary) in Rajasthan is a UNESCO World Heritage Site hosting thousands of migratory birds annually, making it critical for regional biodiversity and migratory species conservation. Climate change is altering migration patterns and water availability in the park, affecting Asia's bird populations. India's wetland protection strategy under the Ramsar Convention (99 sites as of April 2026) positions such reserves as essential for climate-resilient ecosystems.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- New Tiger Reserves ---
        {
            "id": 25009,
            "question_text": "Ratapani Wildlife Sanctuary was declared as Madhya Pradesh's 8th Tiger Reserve in 2025. It acts as a corridor between which two tiger reserves?",
            "option_a": "Kanha and Pench",
            "option_b": "Panna and Satpura",
            "option_c": "Bandhavgarh and Sanjay",
            "option_d": "Bori and Satpura",
            "correct_answer": "B",
            "explanation": "Ratapani Wildlife Sanctuary's 2025 designation as Madhya Pradesh's 8th Tiger Reserve reflects India's commitment to Project Tiger's landscape-connectivity approach. Spanning 890 sq km, it links Panna and Satpura tiger populations, addressing genetic diversity and climate resilience amid habitat fragmentation. This expansion supports India's goal of sustaining 3,682+ tigers (70% of world's wild tigers) and demonstrates the role of corridor management in species adaptation to climate-driven habitat shifts.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25010,
            "question_text": "Madhav National Park in Shivpuri was declared as which number tiger reserve of Madhya Pradesh in March 2025?",
            "option_a": "7th",
            "option_b": "8th",
            "option_c": "9th",
            "option_d": "10th",
            "correct_answer": "C",
            "explanation": "Madhav National Park's March 2025 designation as Madhya Pradesh's 9th Tiger Reserve solidifies MP's leadership in Project Tiger implementation, supporting India's biodiversity conservation targets. This 526 sq km reserve protects forest ecosystems in central India's monsoon belt, increasingly vulnerable to climate variability affecting rainfall patterns. The designation reflects India's strategic prioritization of protected areas as carbon sinks and climate-resilient zones essential for the 2070 Net-Zero commitment.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Assam NP ---
        {
            "id": 25011,
            "question_text": "Shikhna Jwhwlao National Park, notified on February 16, 2025, is the 8th National Park in which state?",
            "option_a": "Arunachal Pradesh",
            "option_b": "Assam",
            "option_c": "Nagaland",
            "option_d": "Meghalaya",
            "correct_answer": "B",
            "explanation": "Shikhna Jwhwlao National Park's February 2025 notification as Assam's 8th and Bodoland Territorial Region's 3rd national park strengthens Northeast India's biodiversity protection network. The park protects endemic species and forest ecosystems vital for regional water security and carbon sequestration. Assam's expanding protected areas align with India's broader strategy to enhance 25.17% forest+tree cover (ISFR 2023) and build climate resilience in flood-prone regions.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- DPS Flamingo Lake ---
        {
            "id": 25012,
            "question_text": "DPS Flamingo Lake was approved as a Conservation Reserve by which state's Wildlife Board, becoming the first wetland linked to Thane Creek Flamingo Sanctuary to receive such protection?",
            "option_a": "Maharashtra",
            "option_b": "Madhya Pradesh",
            "option_c": "Odisha",
            "option_d": "Karnataka",
            "correct_answer": "A",
            "explanation": "Maharashtra's 2025 approval of DPS Flamingo Lake (30 acres) as a conservation reserve protects critical migratory bird habitat threatened by coastal development and climate change. This action addresses ecosystem fragmentation in Mumbai's Thane Creek Flamingo Sanctuary, supporting biodiversity hotspot management aligned with the Ramsar Convention (India's 99 sites as of April 2026). The designation mitigates climate-driven habitat loss affecting Asia's migratory bird populations.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Tiger Statistics ---
        {
            "id": 25013,
            "question_text": "According to the 2022 All India Tiger Estimation, what is the total tiger population in India?",
            "option_a": "2,967",
            "option_b": "3,167",
            "option_c": "3,682",
            "option_d": "4,012",
            "correct_answer": "C",
            "explanation": "The 2022 All India Tiger Estimation (AITE) recorded 3,682 tigers (range 3,167–3,925), representing 70% of global wild tiger population and demonstrating successful Project Tiger conservation. The increase from 2,967 tigers in 2018 reflects landscape connectivity and habitat protection efforts. Climate-resilient tiger habitat management remains essential as species face temperature shifts, prey availability changes, and human-wildlife conflict intensification in India's 2070 Net-Zero pathway.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25014,
            "question_text": "As of March 2025, how many Tiger Reserves exist in India under Project Tiger?",
            "option_a": "52",
            "option_b": "55",
            "option_c": "58",
            "option_d": "62",
            "correct_answer": "C",
            "explanation": "As of March 2025, India's 58 Tiger Reserves under Project Tiger (launched 1973) cover 84,500 sq km and form a biodiversity network supporting species recovery. Managed by the National Tiger Conservation Authority (NTCA), these reserves provide ecosystem services including carbon sequestration and water regulation essential for climate resilience. India's tiger recovery narrative demonstrates how protected areas contribute to both species conservation and climate mitigation targets aligned with the 2070 Net-Zero commitment.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25015,
            "question_text": "Which state has the highest number of tigers in India as per the 2022 tiger census?",
            "option_a": "Karnataka",
            "option_b": "Uttarakhand",
            "option_c": "Madhya Pradesh",
            "option_d": "Assam",
            "correct_answer": "C",
            "explanation": "Madhya Pradesh leads with 785 tigers in the 2022 AITE, reflecting successful multi-reserve landscape management across Kanha, Panna, Satpura, and Bandhavgarh reserves. This concentration demonstrates the state's contribution to India's global species leadership and climate-smart conservation. MP's forest governance, particularly in the Deccan region, exemplifies integration of biodiversity protection with landscape-level climate adaptation amid monsoon variability and deforestation pressures.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Ramsar Sites ---
        {
            "id": 25016,
            "question_text": "As of April 22, 2026 (World Earth Day), what is India's total number of Ramsar sites — the highest in Asia?",
            "option_a": "85",
            "option_b": "92",
            "option_c": "99",
            "option_d": "105",
            "correct_answer": "C",
            "explanation": "As of April 22, 2026, India's 99 Ramsar sites (13,60,805 hectares) represent Asia's largest wetland protection network, surpassing China. These 67 new designations since 2014 strengthen water security in freshwater ecosystems facing climate-driven water stress and monsoon variability. Wetland protection aligns with India's water security strategy under COP commitments, supporting biodiversity while providing ecosystem services crucial for climate resilience and carbon storage.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25017,
            "question_text": "Shekha Jheel Bird Sanctuary, designated as India's 99th Ramsar Site in April 2026, is located in which state?",
            "option_a": "Madhya Pradesh",
            "option_b": "Uttar Pradesh",
            "option_c": "Bihar",
            "option_d": "Rajasthan",
            "correct_answer": "B",
            "explanation": "Shekha Jheel Bird Sanctuary in Aligarh, Uttar Pradesh's April 2026 designation as India's 99th Ramsar site reflects commitment to protecting North India's critical wetland ecosystems amid climate-driven hydrological changes. The Ganges Plain's wetlands face unprecedented water stress from groundwater depletion and monsoon unpredictability. This designation strengthens India's Ramsar network for biodiversity conservation and supports migratory species adaptation to climate shifts affecting wetland productivity.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- New Species ---
        {
            "id": 25018,
            "question_text": "A new wild ginger species named Zingiber jagannathii, honoring Lord Jagannath, was discovered in which state's biosphere reserve?",
            "option_a": "Kerala",
            "option_b": "Odisha",
            "option_c": "Tamil Nadu",
            "option_d": "Jharkhand",
            "correct_answer": "B",
            "explanation": "Zingiber jagannathii was discovered in Similipal Biosphere Reserve, Odisha in August 2024, highlighting India's exceptional 2024 biodiversity record of 683 new faunal species. This discovery in semi-evergreen forests at 758m elevation emphasizes Eastern Ghats' significance as a biodiversity hotspot facing climate-driven habitat fragmentation. The species' restricted range (<1 sq km) exemplifies urgency of protected area expansion to safeguard endemic species in climate-vulnerable forest ecosystems.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25019,
            "question_text": "A new snakehead fish species named 'Channa nachi' was recently discovered in which state?",
            "option_a": "Meghalaya",
            "option_b": "Assam",
            "option_c": "Tripura",
            "option_d": "Sikkim",
            "correct_answer": "A",
            "explanation": "Channa nachi, discovered in Meghalaya's Simsang River system in 2024, exemplifies Northeast India's exceptional freshwater biodiversity and critically highlights climate vulnerability of stream-dependent species. The Garo Hills' high rainfall makes these freshwater ecosystems crucial for regional water security and aquatic species survival. Climate change threatens habitat integrity through temperature fluctuations, precipitation pattern shifts, and flow regime alterations in India's water-rich Northeast region.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25020,
            "question_text": "India added how many new faunal species in the year 2024, a record in the country's biodiversity documentation?",
            "option_a": "433",
            "option_b": "500",
            "option_c": "683",
            "option_d": "812",
            "correct_answer": "C",
            "explanation": "India's 2024 biodiversity milestone of 683 new faunal species (459 new to science, 224 new to India) plus 433 floral taxa reflects exceptional taxonomic capacity supporting CBD targets. Kerala's leadership with 101 species highlights Western Ghats' global significance as a megadiverse region. These discoveries underscore urgency of biodiversity protection amid climate change and habitat loss—essential for meeting the CBD's 2030 goals on species conservation and ecosystem restoration.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25021,
            "question_text": "Three new frog species (Gracixalus patkaiensis, Alcalus fontinalis, Nidirana noadihing) were discovered in 2024 from which Indian state?",
            "option_a": "Meghalaya",
            "option_b": "Nagaland",
            "option_c": "Arunachal Pradesh",
            "option_d": "Manipur",
            "correct_answer": "C",
            "explanation": "Three new frog species discovered in 2024 from Arunachal Pradesh's Kamlang–Namdapha biodiversity hotspot underscore this region's exceptional amphibian diversity—a biodiversity treasure threatened by climate-driven habitat loss. This landscape serves as a transboundary biodiversity corridor linking India, Myanmar, and southern China. Amphibians' sensitivity to temperature and moisture changes makes their conservation critical for monitoring climate impacts on forest ecosystem health in India's 2070 pathway.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25022,
            "question_text": "A study in 2024 proposed that the king cobra be considered as four distinct species. The Western Ghats species was named what?",
            "option_a": "Ophiophagus bungarus",
            "option_b": "Ophiophagus kaalinga",
            "option_c": "Ophiophagus hannah",
            "option_d": "Ophiophagus ghati",
            "correct_answer": "B",
            "explanation": "The 2024 taxonomic revision splitting king cobras into four species (Ophiophagus kaalinga in Western Ghats as Critically Endangered) reveals hidden biodiversity requiring distinct conservation strategies. This discovery emphasizes India's need for species-specific protection frameworks amid climate-driven habitat loss in biodiversity hotspots. Western Ghats' endemic reptile populations face unprecedented threats from deforestation, coffee plantations, and temperature shifts affecting forest microhabitats.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- IUCN Status ---
        {
            "id": 25023,
            "question_text": "What is the IUCN conservation status of the Indian Giant Flying Squirrel (Petaurista philippensis)?",
            "option_a": "Endangered",
            "option_b": "Vulnerable",
            "option_c": "Critically Endangered",
            "option_d": "Least Concern",
            "correct_answer": "D",
            "explanation": "The Indian Giant Flying Squirrel, listed as Least Concern by IUCN and protected under Schedule II of India's Wildlife Protection Act, depends on intact forest canopies. Recent sightings in Uttarakhand's Himalayan forests underscore the species' reliance on continuous forest cover—increasingly threatened by climate-driven tree mortality and fragmentation. Its 60-meter gliding capacity makes it vulnerable to landscape-level habitat discontinuity exacerbated by climate change.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25024,
            "question_text": "What is the IUCN conservation status of the Himalayan Musk Deer (Moschus leucogaster)?",
            "option_a": "Least Concern",
            "option_b": "Vulnerable",
            "option_c": "Endangered",
            "option_d": "Critically Endangered",
            "correct_answer": "C",
            "explanation": "The Himalayan Musk Deer is listed as Endangered by IUCN and receives highest protection under Schedule I of India's Wildlife Protection Act. Poaching pressure on males for their musk gland combined with climate-driven alpine habitat loss (warming-induced treeline shifts, snow pattern changes) threatens populations across India, Nepal, Bhutan, Pakistan, and China. This transboundary species exemplifies need for coordinated international conservation aligned with COP climate commitments.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25025,
            "question_text": "The Saola, nicknamed the 'Asian Unicorn', is native to the Annamite Mountains of which two countries?",
            "option_a": "Thailand and Myanmar",
            "option_b": "Laos and Vietnam",
            "option_c": "Cambodia and Thailand",
            "option_d": "China and Laos",
            "correct_answer": "B",
            "explanation": "The Saola (Critically Endangered, 50–300 individuals), discovered in 1992 in Annamite Mountains along the Vietnam–Laos border, exemplifies biodiversity hotspot vulnerability. This transboundary species faces habitat loss from deforestation, poaching, and climate-driven forest degradation. The Saola's genome mapping (2024) advances conservation genetics research, supporting international recovery efforts aligned with CITES and CBD commitments to prevent species extinction in Southeast Asia's threatened forests.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25026,
            "question_text": "What is the IUCN conservation status of the Binturong (Bearcat)?",
            "option_a": "Least Concern",
            "option_b": "Vulnerable",
            "option_c": "Endangered",
            "option_d": "Critically Endangered",
            "correct_answer": "B",
            "explanation": "The Binturong (Asia's largest civet, Vulnerable status) exemplifies camera-trap discovery success in India's protected areas. The rare Meghalaya sighting in Balpakram's buffer zone indicates forest connectivity recovery in Northeast India. This species' presence signals healthy forest structure amid threats from habitat loss and climate-driven vegetation shifts. Binturong conservation demonstrates India's expanding species monitoring capacity essential for tracking climate impacts on wildlife populations.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25027,
            "question_text": "India has how many threatened species listed on the IUCN Red List?",
            "option_a": "874",
            "option_b": "1,174",
            "option_c": "1,450",
            "option_d": "2,200",
            "correct_answer": "B",
            "explanation": "India's 1,174 IUCN-threatened species (Gharial, Great Indian Bustard, Kashmir Stag, Pygmy Hog, Namdapha Flying Squirrel among Critically Endangered) demand urgent integrated conservation. Climate change exacerbates extinction risk through habitat degradation, prey depletion, and phenological mismatches. India's biodiversity crisis intersects climate action—species conservation contributes to ecosystem carbon storage while building resilience critical for the 2070 Net-Zero pathway and climate adaptation.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25028,
            "question_text": "The Blyde Rondavel Flat Gecko was rediscovered after 34 years in which country?",
            "option_a": "Kenya",
            "option_b": "Nigeria",
            "option_c": "South Africa",
            "option_d": "Botswana",
            "correct_answer": "C",
            "explanation": "The Blyde Rondavel Flat Gecko's 2024 rediscovery in South Africa's Blyde River Canyon—34 years after 1991 discovery—demonstrates climate and habitat fragmentation's impacts on endemic species. This 'lost species' recovery exemplifies reconnecting conservation with biodiversity hotspots under climate stress. South Africa's successes in species recovery align with global CBD targets on halting biodiversity loss, lessons applicable to India's megadiverse regions facing similar climate-driven species threats.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- COP29 ---
        {
            "id": 25029,
            "question_text": "COP29, the UN Climate Change Conference held in November 2024, took place in which city?",
            "option_a": "Sharm el-Sheikh",
            "option_b": "Dubai",
            "option_c": "Baku",
            "option_d": "Istanbul",
            "correct_answer": "C",
            "explanation": "COP29 in Baku (November 2024) established the Baku Climate Unity Pact targeting $1.3 trillion/year from all actors, with $300 billion/year from developed countries by 2035. India criticized the finance goal as 'abysmally poor,' highlighting equity tensions in global climate action. This outcome reflects ongoing challenges in operationalizing climate finance for developing nations' adaptation needs, particularly acute as 2024 recorded 1.55°C warming above pre-industrial levels.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25030,
            "question_text": "What climate finance target for developed countries was agreed upon at COP29 in Baku 2024?",
            "option_a": "$100 billion per year by 2030",
            "option_b": "$300 billion per year by 2035",
            "option_c": "$500 billion per year by 2030",
            "option_d": "$1 trillion per year by 2040",
            "correct_answer": "B",
            "explanation": "COP29's $300 billion/year target by 2035 from developed countries represents critical climate finance commitment amid heated equity debates. India's strong criticism reflects developing nations' stance that adaptation finance remains inadequate for climate-vulnerable regions facing increased extreme weather. The finance architecture directly impacts India's adaptation priorities (water security, renewable energy scaling to 500 GW, disaster resilience) essential for inclusive development aligned with 2070 Net-Zero targets.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25031,
            "question_text": "The 'Baku-Belém Roadmap to 1.3T' was launched at COP29 to scale up climate finance. What does '1.3T' refer to?",
            "option_a": "$1.3 trillion per year from all actors",
            "option_b": "$1.3 trillion total by 2030",
            "option_c": "1.3°C temperature limit",
            "option_d": "1.3 billion tonnes CO2 reduction",
            "correct_answer": "A",
            "explanation": "The Baku–Belém Roadmap targets $1.3 trillion/year from governments, private sector, and multilateral banks for climate action. This ambitious mobilization is essential for transitioning developing economies like India toward renewable energy (500 GW solar target) and climate resilience. The finance framework must support mitigation (fossil fuel phase-out), adaptation (water security, disaster risk reduction), and loss/damage compensation for climate-vulnerable nations.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- COP30 ---
        {
            "id": 25032,
            "question_text": "COP30, held from November 10-22, 2025, took place in which city of Brazil — the heart of the Amazon?",
            "option_a": "São Paulo",
            "option_b": "Rio de Janeiro",
            "option_c": "Manaus",
            "option_d": "Belém",
            "correct_answer": "D",
            "explanation": "COP30 in Belém (November 10-22, 2025)—the first COP in the Amazon—adopted the Global Mutirão decision calling for tripled adaptation finance by 2035 and launched TFFF with $6.7 billion in pledges. This landmark recognizes tropical forests' critical role in climate stabilization and biodiversity protection. The Amazon's deforestation crisis directly threatens global climate targets; Belém's hosting symbolizes urgency of forest conservation aligned with India's tropical forest protection strategies.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25033,
            "question_text": "The final decision package adopted at COP30 in Belém November 2025 was named after which Tupi-Guarani concept meaning 'collective effort'?",
            "option_a": "Mutirão",
            "option_b": "Tupinambá",
            "option_c": "Quilombola",
            "option_d": "Maloca",
            "correct_answer": "A",
            "explanation": "COP30's Global Mutirão package (adopted November 22, 2025) invokes the Indigenous Tupi-Guarani concept of collective community effort, reflecting climate action's need for unified global mobilization. The 150-page decision text emphasizes Indigenous knowledge and community participation essential for climate-resilient forest management. This framing aligns with India's recognition of tribal communities' role in biodiversity conservation and the Paris Agreement's emphasis on just, inclusive climate transitions.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25034,
            "question_text": "The Tropical Forests Forever Facility (TFFF), launched at COP30 Belém on November 6, 2025, mobilized how much in initial pledges by close of COP30?",
            "option_a": "Over $1 billion",
            "option_b": "Over $6.7 billion",
            "option_c": "Over $30 billion",
            "option_d": "Over $100 billion",
            "correct_answer": "B",
            "explanation": "TFFF mobilized $6.7 billion from 66 countries (Norway $3B, Germany €1B, Brazil $1B matched by Indonesia, France €500M) by COP30's close, targeting $125B medium-term. The facility pays up to $4/hectare/year for forest conservation with 20% minimum to Indigenous communities. This mechanism directly supports tropical forest protection critical for global climate stabilization—forests store 2+ years of global CO2 emissions, essential for Paris Agreement targets and nature-positive development transitions.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25035,
            "question_text": "The COP30 'Global Mutirão' decision called for at least tripling of which type of climate finance by 2035?",
            "option_a": "Mitigation finance",
            "option_b": "Technology transfer finance",
            "option_c": "Adaptation finance",
            "option_d": "Loss and damage finance",
            "correct_answer": "C",
            "explanation": "COP30's tripling of adaptation finance by 2035 reflects recognition of climate vulnerability's disproportionate impact on developing nations. India's adaptation priorities—water security amid Himalayan glacier melt, flood/drought resilience, agricultural productivity under monsoon stress—require accelerated finance mobilization. This commitment aligns with India's 2070 Net-Zero pathway incorporating climate-resilient infrastructure, biodiversity protection, and disaster risk reduction essential for climate justice.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- COP sequence ---
        {
            "id": 25036,
            "question_text": "COP31 is scheduled to be hosted in 2026 by which country?",
            "option_a": "Canada",
            "option_b": "Australia",
            "option_c": "Kenya",
            "option_d": "India",
            "correct_answer": "B",
            "explanation": "Australia's 2026 COP31 hosting (following Belém COP30, November 2025) shifts climate leadership focus to the Indo-Pacific region vulnerable to climate impacts. The COP sequence—Dubai (2023), Baku (2024), Belém (2025), Australia (2026)—demonstrates rotating regional responsibility for global climate governance. Australia's unique climate challenges (droughts, wildfires, coral bleaching) align with developing nations' climate vulnerability narratives central to adaptation finance debates.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Project Dolphin ---
        {
            "id": 25037,
            "question_text": "The first Ganges River Dolphin was successfully satellite-tagged on December 18, 2024, in which state?",
            "option_a": "Bihar",
            "option_b": "West Bengal",
            "option_c": "Uttar Pradesh",
            "option_d": "Assam",
            "correct_answer": "D",
            "explanation": "The December 18, 2024 satellite-tagging of India's first Ganges River Dolphin in Assam (led by WII, Assam Forest Department, Aaranyak) marks transformative Project Dolphin progress. Real-time movement tracking reveals river habitat use patterns under climate-driven hydrological stress. Ganges dolphins' endangered status reflects river degradation from pollution, dam operations, and water extraction—conservation directly addressing India's transboundary water security and ecosystem restoration critical for 2070 Net-Zero pathways.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25038,
            "question_text": "Under which project was India's first-ever Ganges River Dolphin satellite-tagging accomplished in 2024?",
            "option_a": "Project Tiger",
            "option_b": "Project Crocodile",
            "option_c": "Project Dolphin",
            "option_d": "Project Aqua",
            "correct_answer": "C",
            "explanation": "Project Dolphin (launched 2020) exemplifies India's integrated aquatic ecosystem conservation combining species protection with river health monitoring. The December 2024 Ganges dolphin satellite-tagging (Assam) advances understanding of freshwater megafauna responses to dam operations and pollution. This project aligns with India's water security strategy and transboundary cooperation frameworks for shared Ganges-Brahmaputra basin management under climate change stress.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Rivers ---
        {
            "id": 25039,
            "question_text": "The Chambal River, home to the National Chambal Sanctuary, flows through which set of states?",
            "option_a": "Uttar Pradesh, Madhya Pradesh and Rajasthan",
            "option_b": "Bihar, Jharkhand and Uttar Pradesh",
            "option_c": "Gujarat, Rajasthan and Haryana",
            "option_d": "Maharashtra, MP and Chhattisgarh",
            "correct_answer": "A",
            "explanation": "The Chambal River (1,024 km, originating Indore's Bhadakla Falls, joining Yamuna at Jalaun) flows through MP, Rajasthan, and UP. The National Chambal Sanctuary protects Gharials and Ganges dolphins amid river degradation from dams and pollution. Transboundary coordination among three states is essential for water management under climate-driven flow stress and flood risks affecting 60+ million downstream users dependent on Chambal-Yamuna water security.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25040,
            "question_text": "The Netravathi River, which flows through Mangaluru, is located in which state?",
            "option_a": "Maharashtra",
            "option_b": "Karnataka",
            "option_c": "Kerala",
            "option_d": "Tamil Nadu",
            "correct_answer": "B",
            "explanation": "The Netravathi River (originating Kudremukh range, Chikkamagaluru, Western Ghats) drains to Arabian Sea south of Mangaluru, Karnataka. This west-flowing river faces climate-driven flow variability from monsoon shifts and deforestation. The river system supports biodiversity and local livelihoods while providing hydropower and irrigation. Western Ghats river conservation aligns with India's water security strategy and carbon sequestration through forest protection.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Yellow Sea ---
        {
            "id": 25041,
            "question_text": "The Yellow Sea, which is seeing increased Chinese activities, is a marginal sea of which ocean?",
            "option_a": "Indian Ocean",
            "option_b": "Atlantic Ocean",
            "option_c": "Arctic Ocean",
            "option_d": "Pacific Ocean",
            "correct_answer": "D",
            "explanation": "The Yellow Sea (Huang Hai/West Sea) is a Western Pacific marginal sea covering 400,000 sq km with 55–120 m depths, bordered by China, North Korea, and South Korea. Climate change is altering temperature regimes, fish stock distributions, and monsoon patterns critical to fisheries. The sea's strategic geopolitical importance intersects with environmental pressures from pollution and overfishing, exemplifying how ocean conservation intersects climate action and maritime security.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25042,
            "question_text": "The Yellow Sea gets its characteristic yellow color from which source?",
            "option_a": "Minerals from sea floor",
            "option_b": "Algae bloom",
            "option_c": "Sand particles from Gobi Desert",
            "option_d": "Industrial effluents",
            "correct_answer": "C",
            "explanation": "Yellow Sea's characteristic color derives from Gobi Desert sand particles blown by winds—a natural indicator of East Asian climate and desertification pressures. Climate change is intensifying dust storms and altering sediment transport patterns affecting ocean productivity. This phenomenon illustrates interconnections between terrestrial desertification, atmospheric circulation shifts, and marine ecosystem health—highlighting urgency of integrated land-ocean climate action.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Pollution ---
        {
            "id": 25043,
            "question_text": "What are 'Nurdles', which were found in large quantities along the Thiruvananthapuram coastline in May 2025?",
            "option_a": "Newly discovered marine insects",
            "option_b": "Tiny plastic pellets used as raw material in plastic manufacturing",
            "option_c": "Heavy metal pollutants from industrial effluents",
            "option_d": "Dead coral fragments",
            "correct_answer": "B",
            "explanation": "Nurdles (1–5 mm plastic pellets: LDPE/HDPE) represent microplastic pollution threatening marine ecosystems and food webs. The May 2025 MSC ELSA 3 sinking along Kerala's coast highlighted pollution risks from shipping accidents—increasingly frequent amid climate-driven storm intensification. Marine animal ingestion of nurdles causes bioaccumulation and toxic exposure. India's plastic pollution crisis intersects climate change, requiring urgent international plastic treaty implementation (INC negotiations ongoing).",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25044,
            "question_text": "The sinking of which cargo ship in May 2025 caused Nurdles pollution along Kerala's Thiruvananthapuram coastline?",
            "option_a": "MSC ELSA 3",
            "option_b": "MV Ever Given",
            "option_c": "SS Prestige",
            "option_d": "MV Wakashio",
            "correct_answer": "A",
            "explanation": "The MSC ELSA 3's May 25, 2025 sinking released nurdles along Thiruvananthapuram, demonstrating ocean pollution risks from maritime shipping amid climate change. Extreme weather intensification increases shipping accidents and spills. This incident underscores India's coastal vulnerability to transboundary pollution and the need for strengthened marine spatial planning, port infrastructure resilience, and international maritime regulation—critical components of ocean health under climate change.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Volcanoes ---
        {
            "id": 25045,
            "question_text": "Poas Volcano, one of the world's most active volcanoes, is located in which country?",
            "option_a": "Japan",
            "option_b": "Indonesia",
            "option_c": "Costa Rica",
            "option_d": "Nicaragua",
            "correct_answer": "C",
            "explanation": "Poas Volcano (Costa Rica, 2,708 m elevation, 1.5 km-wide crater) exemplifies volcanic systems' climate interactions. Active volcanic emissions release sulfur aerosols temporarily cooling the atmosphere while causing regional air quality degradation. Climate change alters volcanic hydrology and gas release patterns; volcanic eruptions impact atmospheric circulation and precipitation. Costa Rica's Poás National Park protects biodiversity in volcanic regions facing ecosystem shifts from climate change and volcanic hazards.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Forests ---
        {
            "id": 25046,
            "question_text": "Teak (Tectona grandis), known as the 'King of Timbers', primarily grows in which type of forest?",
            "option_a": "Tropical Rainforest",
            "option_b": "Moist Deciduous Forest",
            "option_c": "Tropical Evergreen Forest",
            "option_d": "Coniferous Forest",
            "correct_answer": "B",
            "explanation": "Teak thrives in Moist Deciduous Forests where monsoon precipitation and dry seasons regulate growth rings valued for durability. India's 35% global teak holdings (MP and Maharashtra leading) represent critical forest carbon stocks and livelihoods. Climate change threatens teak productivity through altered monsoon patterns and pest pressure. Sustainable teak management aligns with India's ISFR 2023 forest cover expansion (21.76%) and timber economy's transition toward climate-smart forestry.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25047,
            "question_text": "India holds approximately what percentage of the world's planted teak forests?",
            "option_a": "15%",
            "option_b": "25%",
            "option_c": "35%",
            "option_d": "50%",
            "correct_answer": "C",
            "explanation": "India's 35% of global planted teak forests (Asia's 95% total) represents significant renewable timber resource and carbon sequestration potential. Teak plantations contribute to ISFR 2023 goals of 25.17% forest+tree cover through afforestation. Climate-smart teak management—combining yield with biodiversity and water conservation—exemplifies Green Growth strategy aligning forest livelihoods with mitigation and adaptation objectives under India's 2070 Net-Zero targets.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Pobitora details ---
        {
            "id": 25048,
            "question_text": "Tamulidoba Beel, a major wetland that is drying up and threatening waterfowl habitat, is located within which wildlife sanctuary?",
            "option_a": "Kaziranga NP",
            "option_b": "Pobitora Wildlife Sanctuary",
            "option_c": "Manas NP",
            "option_d": "Nameri NP",
            "correct_answer": "B",
            "explanation": "Tamulidoba Beel's drying within Pobitora Wildlife Sanctuary epitomizes climate-driven wetland degradation threatening waterfowl and the rhino habitat. Seasonal water stress, monsoon unpredictability, and hyacinth invasion exemplify complex ecosystem responses to climate change. Wetland restoration through water harvesting and invasive species management is critical for Ramsar site protection (India's 99 sites) and species survival. Pobitora's rehabilitation aligns with water security and biodiversity conservation under 2070 pathways.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- WPA Schedule ---
        {
            "id": 25049,
            "question_text": "The Indian Giant Flying Squirrel is protected under which Schedule of the Wildlife Protection Act, 1972?",
            "option_a": "Schedule I",
            "option_b": "Schedule II",
            "option_c": "Schedule III",
            "option_d": "Schedule IV",
            "correct_answer": "B",
            "explanation": "The Indian Giant Flying Squirrel's Schedule II protection under WPA 1972 reflects intermediate conservation priority despite Least Concern status. This framework allows regulated use while preventing overexploitation. Schedule framework integration with IUCN Red List informs adaptive management responding to climate-driven habitat loss. India's wildlife protection architecture exemplifies how legal frameworks support biodiversity conservation amid ecosystem changes.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25050,
            "question_text": "The Himalayan Musk Deer is listed under which Schedule of India's Wildlife Protection Act, 1972, indicating the highest protection?",
            "option_a": "Schedule IV",
            "option_b": "Schedule III",
            "option_c": "Schedule II",
            "option_d": "Schedule I",
            "correct_answer": "D",
            "explanation": "Schedule I (highest protection, zero hunting) listing of the Endangered Himalayan Musk Deer reflects conservation urgency amid poaching pressure and climate-driven alpine habitat loss. WPA 1972's Schedule framework provides legal enforcement for species survival. International cooperation with Nepal, Bhutan, Pakistan, and China through CITES ensures transboundary musk deer protection aligning with climate adaptation for high-altitude biodiversity hotspots.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- COP General ---
        {
            "id": 25051,
            "question_text": "COP stands for which full form in the context of UN Climate Change Conferences?",
            "option_a": "Conference of Parties",
            "option_b": "Congress of Plenipotentiaries",
            "option_c": "Convention on Pollution",
            "option_d": "Compact of Participants",
            "correct_answer": "A",
            "explanation": "COP (Conference of Parties) is the annual UNFCCC decision-making body where signatories negotiate climate action commitments. The COP sequence—Baku (Nov 2024), Belém (Nov 2025), Australia (2026)—demonstrates evolving climate governance addressing 1.55°C warming (2024 record). India's active participation at COPs advocates for climate justice, renewable energy deployment (500 GW target), and adaptation finance for developing-nation climate resilience.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25052,
            "question_text": "Which country hosted COP28 in 2023?",
            "option_a": "Saudi Arabia",
            "option_b": "Qatar",
            "option_c": "UAE (Dubai)",
            "option_d": "Egypt",
            "correct_answer": "C",
            "explanation": "COP28 (Dubai, November-December 2023) marked historic first loss-and-damage fund operationalization and first global stocktake assessing Paris Agreement progress. The stocktake revealed emissions gap persists despite NDC improvements. Dubai's hosting by an oil-producing nation symbolized tensions between fossil fuel interests and climate action—themes dominating subsequent COPs emphasizing rapid renewable energy transition and developing-nation adaptation priorities.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Biosphere Reserves ---
        {
            "id": 25053,
            "question_text": "Similipal Biosphere Reserve, where a new ginger species was discovered in 2024, is located in which state?",
            "option_a": "Chhattisgarh",
            "option_b": "Jharkhand",
            "option_c": "Odisha",
            "option_d": "West Bengal",
            "correct_answer": "C",
            "explanation": "Similipal Biosphere Reserve (Odisha) exemplifies Eastern Ghats' biodiversity richness through 2024 discovery of Zingiber jagannathii and broader faunal additions (683 species in 2024). UNESCO Man and Biosphere Programme integration supports integrated landscape management addressing climate change impacts on forest hydrology and species ranges. Similipal's semi-evergreen forests are critical carbon sinks and climate-resilient ecosystems supporting India's 25.17% forest+tree cover expansion.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        {
            "id": 25054,
            "question_text": "The Nilgiri Biosphere Reserve is a UNESCO Man and Biosphere Programme site. Which of the following sanctuaries is part of it?",
            "option_a": "Pobitora Wildlife Sanctuary",
            "option_b": "Karimpuzha Wildlife Sanctuary",
            "option_c": "Indravati National Park",
            "option_d": "Balpakram National Park",
            "correct_answer": "B",
            "explanation": "Karimpuzha Wildlife Sanctuary's integration within Nilgiri Biosphere Reserve (UNESCO-MAB, Kerala-Tamil Nadu border) exemplifies transboundary biodiversity governance linking Silent Valley NP and Mukurthi NP. This landscape approach addresses climate-driven species range shifts requiring corridor connectivity. Western Ghats biosphere reserves protect endemic species and water sources vital for downstream communities—ecosystems facing unprecedented pressure from climate-driven temperature increases and monsoon stress.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Binturong ---
        {
            "id": 25055,
            "question_text": "The Binturong (Bearcat), recently camera-trapped in Meghalaya, is described as the largest of which animal group in India?",
            "option_a": "Mongoose family",
            "option_b": "Civet family",
            "option_c": "Weasel family",
            "option_d": "Marten family",
            "correct_answer": "B",
            "explanation": "The Binturong (Asia's largest Vulnerable civet, herbivorous-frugivorous diet) demonstrates forest health through its presence in Balpakram's buffer zone, indicating intact dense forest canopy and prey availability. This camera-trap discovery exemplifies India's expanding species monitoring capacity essential for tracking climate impacts on mesofauna. Binturong conservation reflects ecosystem connectivity needs amid forest fragmentation driving species adaptation challenges in Northeast India's climate-sensitive regions.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Carbon/NDC ---
        {
            "id": 25056,
            "question_text": "NDC in the context of climate agreements stands for?",
            "option_a": "National Development Committee",
            "option_b": "Nationally Determined Contribution",
            "option_c": "Net Decarbonisation Commitment",
            "option_d": "Non-Deforestation Clause",
            "correct_answer": "B",
            "explanation": "Nationally Determined Contributions (NDCs) form the Paris Agreement's cornerstone—each nation's mitigation and adaptation pledges. UNEP Emissions Gap Report 2025 projects full NDC implementation yields only 2.3-2.5°C warming by 2100, requiring 55% emissions cuts by 2035 for 1.5°C alignment. India's NDCs target 500 GW renewables, 2070 Net-Zero, and forest cover expansion—exemplifying how NDCs translate climate commitments into development pathways balancing adaptation and mitigation.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Saola discovery ---
        {
            "id": 25057,
            "question_text": "The Saola was first discovered in 1992 during a joint survey by the Vietnamese Ministry of Forestry and which international organization?",
            "option_a": "IUCN",
            "option_b": "WWF (World Wildlife Fund)",
            "option_c": "WCS (Wildlife Conservation Society)",
            "option_d": "CITES",
            "correct_answer": "B",
            "explanation": "The Saola's 1992 discovery by Vietnamese Ministry of Forestry and WWF revealed an entirely new ungulate species in Annamite Mountains—demonstrating tropical forest biodiversity richness. Its 2024 genome mapping advances conservation genomics for Critically Endangered species recovery. The Saola exemplifies transboundary conservation urgency: habitat loss from deforestation, poaching, and climate-driven forest degradation threaten extinction of this 'Asian Unicorn,' requiring international cooperation on forest protection.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Chambal ---
        {
            "id": 25058,
            "question_text": "The Chambal River originates from which location in Madhya Pradesh?",
            "option_a": "Amarkantak hills",
            "option_b": "Bhadakla Falls near Janapav Hills, Indore",
            "option_c": "Pachmarhi hills",
            "option_d": "Maikala Range",
            "correct_answer": "B",
            "explanation": "Chambal River originates at Bhadakla Falls (843 m elevation, Indore's Janapav Hills) and flows 1,024 km to join Yamuna, supporting 60+ million people across MP, Rajasthan, UP. Climate-driven flow variability, dam operations, and pollution threaten Chambal's ecosystem services. The National Chambal Sanctuary's Gharial and dolphin populations depend on river health—making transboundary water management critical for species survival and millions of livelihoods under climate change stress.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- WII ---
        {
            "id": 25059,
            "question_text": "Which institution led the satellite-tagging of the first Ganges River Dolphin in Assam in December 2024?",
            "option_a": "Bombay Natural History Society (BNHS)",
            "option_b": "Centre for Wildlife Studies (CWS)",
            "option_c": "Wildlife Institute of India (WII)",
            "option_d": "Salim Ali Centre for Ornithology (SACON)",
            "correct_answer": "C",
            "explanation": "WII's December 2024 Ganges dolphin satellite-tagging (partnering Assam Forest Department, Aaranyak) demonstrates India's expanding research capacity for real-time species monitoring. Real-time tracking reveals river habitat use patterns, movement corridors, and responses to hydrological changes. This data advances understanding of climate impacts on Endangered freshwater cetaceans and informs adaptive management for species survival amid river degradation and flow regulation—critical for Project Dolphin's success.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Budget ---
        {
            "id": 25060,
            "question_text": "The central government's 2025–26 budget allocated ₹290 crore (64% of wildlife habitat allocation) for which projects?",
            "option_a": "Project Crocodile and Project Vulture",
            "option_b": "Project Tiger and Project Elephant",
            "option_c": "Project Dolphin and Project Sea Turtle",
            "option_d": "Project Snow Leopard and Project Hangul",
            "correct_answer": "B",
            "explanation": "India's 2025-26 budget allocation of ₹290 crore for Project Tiger and Elephant (18% increase, 64% of ₹450 crore wildlife habitat budget) demonstrates government commitment to megafauna conservation. These flagship projects anchor larger ecosystem protection strategies supporting biodiversity and climate resilience. Budget allocation reflects India's prioritization of species recovery alongside carbon sequestration through forest protection—investments essential for 2070 Net-Zero targets and wildlife-climate action integration.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Corbett details ---
        {
            "id": 25061,
            "question_text": "Jim Corbett National Park was originally established in 1936 under what name?",
            "option_a": "Corbett Wildlife Sanctuary",
            "option_b": "Hailey National Park",
            "option_c": "Ramganga National Park",
            "option_d": "Uttarakhand Forest Reserve",
            "correct_answer": "B",
            "explanation": "Corbett Tiger Reserve's 1936 establishment as Hailey National Park (renamed 1957 for Jim Corbett) represents India's pioneer approach to protected area management. This 1,288 sq km reserve and its river systems (Ramganga, Pallaen, Sonanadi) provide ecosystem services including water regulation and carbon storage. Corbett exemplifies how flagship reserves support landscape-level conservation addressing climate-driven habitat fragmentation and ensuring species survival in Himalayan regions facing accelerated warming.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- NTCA ---
        {
            "id": 25062,
            "question_text": "Project Tiger is managed by which authority in India?",
            "option_a": "Wildlife Crime Control Bureau (WCCB)",
            "option_b": "National Tiger Conservation Authority (NTCA)",
            "option_c": "Central Zoo Authority (CZA)",
            "option_d": "Indian Board for Wildlife (IBWL)",
            "correct_answer": "B",
            "explanation": "NTCA (under Ministry of Environment, Forests and Climate Change) manages Project Tiger, launched in 1973 across 58 reserves covering 84,500 sq km. India's tiger recovery—from near extinction to 3,682 animals (70% of global population) by 2022—demonstrates successful landscape-level conservation. Climate-smart reserve management integrating water security, forest health, and community livelihood supports ecosystem services essential for India's 2070 Net-Zero pathways.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Paris Agreement ---
        {
            "id": 25063,
            "question_text": "The Paris Agreement aims to limit global temperature increase to well below how many degrees Celsius above pre-industrial levels?",
            "option_a": "1°C",
            "option_b": "1.5°C",
            "option_c": "2°C",
            "option_d": "Both 1.5°C and 2°C (with 1.5°C as aspiration)",
            "correct_answer": "D",
            "explanation": "Paris Agreement (2015) targets 'well below 2°C' with 1.5°C aspiration. WMO's March 2025 confirmation that 2024 exceeded 1.5°C (1.55±0.13°C above 1850-1900) signals urgent need for accelerated climate action. The 1.5°C overshoot reflects cumulative anthropogenic emissions and warming commitments in the climate system. India's 2070 Net-Zero target and NDC commitments embody Paris Agreement response, requiring rapid renewable energy deployment and forest protection to bend emissions curves.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- UNFCCC ---
        {
            "id": 25064,
            "question_text": "UNFCCC, under which the annual COP meetings are held, stands for?",
            "option_a": "United Nations Framework Convention on Climate Change",
            "option_b": "United Nations Fund for Carbon Capture",
            "option_c": "Universal Framework for Carbon and Climate Control",
            "option_d": "UN Forum for Climate Cooperation",
            "correct_answer": "A",
            "explanation": "UNFCCC (established 1992, entered force 1994) provides the legal architecture for international climate governance through annual COP meetings. The COP process (Baku 2024, Belém Nov 2025, Australia 2026) negotiates binding commitments on mitigation, adaptation, and finance. India's UNFCCC participation advances climate justice advocacy, renewable energy scaling (500 GW), and developing-nation adaptation finance mobilization essential for equitable climate action.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- TFFF mechanics ---
        {
            "id": 25065,
            "question_text": "Under the Tropical Forests Forever Facility (TFFF) launched at COP30 Belém 2025, what minimum share of payments must go to Indigenous Peoples and local communities?",
            "option_a": "5%",
            "option_b": "10%",
            "option_c": "20%",
            "option_d": "50%",
            "correct_answer": "C",
            "explanation": "TFFF's 20% minimum for Indigenous and local communities reflects recognition of their forest stewardship roles in biodiversity protection and carbon sequestration. The $4/hectare/year payment mechanism incentivizes forest conservation as climate mitigation while supporting community livelihoods. This climate finance approach aligns with India's recognition of tribal communities' conservation contributions in protected areas and integrated biodiversity management—models integrating climate action with development justice.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Ramsar ---
        {
            "id": 25066,
            "question_text": "The Ramsar Convention is related to the conservation of which type of ecosystems?",
            "option_a": "Forests",
            "option_b": "Wetlands",
            "option_c": "Coral Reefs",
            "option_d": "Mountain Grasslands",
            "correct_answer": "B",
            "explanation": "Ramsar Convention (1971) protects wetlands as critical ecosystems providing water storage, flood regulation, carbon sequestration, and biodiversity support. India's 99 Ramsar sites (13,60,805 hectares as of April 2026, Asia's highest) exemplify wetland conservation amid climate-driven hydrological stress. These ecosystems face unprecedented pressure from water extraction, pollution, and extreme weather patterns—wetland restoration and protection are essential for water security and climate resilience in India's water-stressed regions.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- BNHS ---
        {
            "id": 25067,
            "question_text": "The Bombay Natural History Society (BNHS) warned about which environmental risk related to the DPS Flamingo Lake near Navi Mumbai International Airport (NMIA)?",
            "option_a": "Flooding of runway",
            "option_b": "Bird strike risk from displaced flamingos",
            "option_c": "Noise pollution affecting flamingo breeding",
            "option_d": "Air quality degradation from airport emissions",
            "correct_answer": "B",
            "explanation": "BNHS analysis of NMIA-adjacent wetland loss identified cascading risks: displaced flamingo populations seeking alternative habitats raise aviation safety concerns. The DPS Flamingo Lake's 2025 Conservation Reserve approval demonstrates integrative solutions balancing infrastructure development with ecosystem protection. This exemplifies climate-resilient coastal planning where wetland protection provides dual benefits: migratory species conservation and human safety amid extreme weather intensification.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Namdapha ---
        {
            "id": 25068,
            "question_text": "Namdapha National Park, a biodiversity hotspot where three new frog species were discovered, is located in which state?",
            "option_a": "Assam",
            "option_b": "Manipur",
            "option_c": "Arunachal Pradesh",
            "option_d": "Meghalaya",
            "correct_answer": "C",
            "explanation": "Namdapha National Park (Arunachal Pradesh, Kamlang–Namdapha biodiversity hotspot) exemplifies Northeast India's exceptional amphibian diversity—three new frog species discovered in 2024. This landscape's transboundary linkages (India-Myanmar-China) require integrated protection amid climate-driven habitat loss. Amphibians serve as climate change indicators; their sensitivity to temperature and moisture stress reveals ecosystem vulnerability. Namdapha protection supports Indian commitment to CBD 2030 goals on biodiversity conservation.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Western Ghats ---
        {
            "id": 25069,
            "question_text": "Kerala led India's 2024 biodiversity record with how many newly documented species?",
            "option_a": "51",
            "option_b": "68",
            "option_c": "101",
            "option_d": "143",
            "correct_answer": "C",
            "explanation": "Kerala's 2024 leadership with 101 new species (80 new to science, 21 new to India) underscores Western Ghats' extraordinary biodiversity and research capacity. These discoveries—reptiles, amphibians, butterflies, orchids, fungi, lichens—reveal ecosystem complexity threatened by climate-driven habitat loss and fragmentation. Kerala's findings contribute to India's 683 total new faunal species in 2024, advancing global biodiversity knowledge critical for developing climate-smart conservation strategies for megadiverse regions.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- CZA ---
        {
            "id": 25070,
            "question_text": "A 2024 report by the Central Zoo Authority highlighted a gap in conservation breeding for which species in Indian zoos?",
            "option_a": "Indian Giant Flying Squirrel",
            "option_b": "Himalayan Musk Deer",
            "option_c": "Snow Leopard",
            "option_d": "Pygmy Hog",
            "correct_answer": "B",
            "explanation": "CZA's 2024 report identifying Himalayan Musk Deer breeding gap in zoos underscores challenges in ex-situ conservation for climate-vulnerable alpine species. Genetic rescue and captive breeding programs complement in-situ protection amid habitat loss. Musk deer breeding programs require temperature-controlled facilities vulnerable to rising ambient temperatures—exemplifying how climate change complicates zoo-based conservation. Such programs support wild population recovery while preserving genetic diversity essential for species adaptation.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Indravati River ---
        {
            "id": 25071,
            "question_text": "The Indravati River, after which Indravati National Park is named, is a tributary of which major river?",
            "option_a": "Krishna",
            "option_b": "Mahanadi",
            "option_c": "Narmada",
            "option_d": "Godavari",
            "correct_answer": "D",
            "explanation": "Indravati River (originating Dandakaranya range, Odisha) as Godavari tributary manages transboundary flows across Odisha-Chhattisgarh-Maharashtra. The Indravati National Park protects this river's biodiversity amid climate-driven flow variability and dam impacts. River ecosystems face unprecedented stress from flood/drought extremes, thermal pollution, and habitat degradation. Indravati conservation exemplifies transboundary water cooperation essential for Godavari Basin's water security and ecosystem health under climate change.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- WPA ---
        {
            "id": 25072,
            "question_text": "Under India's Wildlife Protection Act 1972, a Wildlife Sanctuary can be declared by which authority?",
            "option_a": "Central Government only",
            "option_b": "State Government only",
            "option_c": "State Government, and Central Government can also declare a National Park",
            "option_d": "District Collector with state approval",
            "correct_answer": "C",
            "explanation": "WPA 1972's decentralized framework—state governments declaring sanctuaries, central government declaring national parks—enables adaptive governance responsive to regional biodiversity and climate conditions. This federal structure supports landscape-scale conservation addressing climate vulnerability through coordinated protection. Recent expansions (58 tiger reserves, 99 Ramsar sites) demonstrate institutional capacity for rapid scaling of climate-resilient protected area networks essential for India's 2070 Net-Zero pathway.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Tiger Census schedule ---
        {
            "id": 25073,
            "question_text": "The All India Tiger Estimation (AITE) is conducted once every how many years?",
            "option_a": "2 years",
            "option_b": "4 years",
            "option_c": "5 years",
            "option_d": "10 years",
            "correct_answer": "B",
            "explanation": "AITE's 4-year cycle provides data to track tiger population trends and evaluate Project Tiger effectiveness. The 2022 AITE (5th edition: 3,682 tigers, up from 2,967 in 2018) demonstrates recovery despite climate-driven habitat pressures. The 6th AITE (started late 2025) will assess how climate change alters tiger populations, prey availability, and human-wildlife conflicts. Such regular monitoring is essential for adaptive management supporting tiger survival amid ecosystem changes.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- COP29 India response ---
        {
            "id": 25074,
            "question_text": "India's reaction to the $300 billion climate finance goal set at COP29 Baku 2024 was to describe it as?",
            "option_a": "A landmark achievement",
            "option_b": "An insufficient but positive step",
            "option_c": "Abysmally poor",
            "option_d": "Highly ambitious",
            "correct_answer": "C",
            "explanation": "India's 'abysmally poor' critique of COP29's $300B/year by 2035 target reflects global equity tensions—developing nations' adaptation needs vastly exceed pledged finance. India's water security challenges (glacier melt, monsoon stress, groundwater depletion), renewable energy transition costs (500 GW target), and climate disaster impacts require proportionate finance. This stance drives demands for loss-and-damage mechanisms and climate reparations reflecting historical emission inequities.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Project Tiger launch ---
        {
            "id": 25075,
            "question_text": "In which year was Project Tiger launched in India?",
            "option_a": "1969",
            "option_b": "1973",
            "option_c": "1980",
            "option_d": "1985",
            "correct_answer": "B",
            "explanation": "Project Tiger (launched 1973, NTCA-managed) transformed conservation policy from hunting to landscape-scale ecosystem protection. This 50+ year initiative grew from near-extinction to 3,682 tigers by 2022, exemplifying long-term institutional commitment. Climate change now challenges tiger survival through habitat degradation, prey depletion, and extreme weather impacts. Project Tiger's evolution toward climate-smart adaptation—corridor connectivity, watershed management, community integration—positions it as model for biodiversity conservation under climate stress.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Simsang River ---
        {
            "id": 25076,
            "question_text": "The Simsang River system, where the new fish species Channa nachi was discovered, is in which state?",
            "option_a": "Assam",
            "option_b": "Manipur",
            "option_c": "Meghalaya",
            "option_d": "Tripura",
            "correct_answer": "C",
            "explanation": "Channa nachi's discovery in Meghalaya's Simsang River system (Garo Hills, near Chokpot village) demonstrates freshwater species richness in Northeast India's high-rainfall regions. Stream-dwelling species face climate threats from temperature increases and precipitation pattern shifts affecting water flow and habitat quality. The Simsang system's biodiversity requires watershed protection and integrated river basin management aligned with India's water security strategy and wetland conservation under Ramsar commitments.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Mangroves ---
        {
            "id": 25077,
            "question_text": "India's Sundarbans mangrove forest, a UNESCO World Heritage Site, is located in which state?",
            "option_a": "Odisha",
            "option_b": "Andhra Pradesh",
            "option_c": "West Bengal",
            "option_d": "Tamil Nadu",
            "correct_answer": "C",
            "explanation": "Sundarbans (West Bengal-Bangladesh, world's largest mangrove, UNESCO World Heritage Site) faces existential climate threats: sea-level rise, salinity intrusion, cyclone intensification, and tiger habitat loss. This 10,000+ sq km ecosystem provides livelihoods for millions while storing massive carbon reserves. India's 2nd-largest mangrove areas require urgent protection through climate adaptation—mangrove restoration, dyke reinforcement, community-based management—essential for coastal resilience and carbon storage under 2070 Net-Zero targets.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Project Dolphin ---
        {
            "id": 25078,
            "question_text": "Project Dolphin was launched in India in which year for the conservation of Gangetic and Irrawaddy dolphins?",
            "option_a": "2015",
            "option_b": "2018",
            "option_c": "2020",
            "option_d": "2022",
            "correct_answer": "C",
            "explanation": "Project Dolphin (2020) addresses freshwater cetacean conservation amid river ecosystem degradation from dams, pollution, and water extraction. The December 2024 Ganges dolphin satellite-tagging breakthrough enables real-time tracking of responses to flow regulation and thermal stress. Dolphin populations serve as indicator species for river health—their recovery signals ecosystem restoration potential. Project Dolphin's integration with water resource management exemplifies climate-smart river governance supporting both species survival and human water security.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Indian Rhino Vision ---
        {
            "id": 25079,
            "question_text": "The 'Indian Rhino Vision 2020' programme is associated with which wildlife sanctuary that has the highest density of Greater One-Horned Rhinoceros?",
            "option_a": "Kaziranga NP",
            "option_b": "Manas NP",
            "option_c": "Pobitora WLS",
            "option_d": "Orang NP",
            "correct_answer": "C",
            "explanation": "Pobitora (48.81 sq km, eastern Guwahati) anchors Indian Rhino Vision 2020, protecting the world's highest Greater One-Horned Rhino density. Climate change threatens Pobitora through monsoon alterations, flooding, and wetland drying (Tamulidoba Beel). This small sanctuary exemplifies conservation challenges in climate-vulnerable regions requiring robust disaster risk reduction, invasive species management, and transboundary cooperation with Bangladesh. Rhino conservation success demonstrates landscape-scale approaches' potential under climate stress.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Eusauropod ---
        {
            "id": 25080,
            "question_text": "Jinchuanloong niedu, a new genus of eusauropod dinosaur discovered from a fossil in Gansu Province, China, dates to which geological period?",
            "option_a": "Late Cretaceous (~70 million years ago)",
            "option_b": "Early Jurassic (~200 million years ago)",
            "option_c": "Middle Jurassic (~165 million years ago)",
            "option_d": "Triassic (~230 million years ago)",
            "correct_answer": "C",
            "explanation": "Jinchuanloong niedu (Middle Jurassic, ~165 million years, Gansu Province, Xinhe Formation) exemplifies paleontological discoveries revealing ancient climate and biodiversity. Dinosaur-era climate shifts inform understanding of current warming trajectories and ecosystem responses to rapid temperature changes. Fossil discoveries demonstrate Earth's capacity for extreme climate variability—lessons applicable to predicting current climate change impacts on biodiversity. Paleoclimate insights support conservation strategy development for species facing unprecedented modern warming.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # ═══════════════════════════════════════════════════════════════
        # 2025-26 Freshness gap-fill (added May 19, 2026) — IDs 25081-25100
        # ═══════════════════════════════════════════════════════════════
        # --- WMO State of Global Climate 2024 ---
        {
            "id": 25081,
            "question_text": "According to the WMO State of the Global Climate 2024 report (released March 2025), what was the 2024 global mean surface temperature above the 1850-1900 pre-industrial baseline?",
            "option_a": "1.28°C",
            "option_b": "1.45°C",
            "option_c": "1.55°C",
            "option_d": "2.10°C",
            "correct_answer": "C",
            "explanation": "WMO's March 2025 confirmation of 2024 warming at 1.55°C (±0.13°C) above 1850-1900 baseline marks a critical climate threshold—first calendar year exceeding Paris Agreement's 1.5°C aspiration. Long-term trend (1.34-1.41°C) shows relentless warming acceleration. This trajectory demands immediate emissions cuts (55% by 2035 per UNEP) and adaptation finance tripling. India's 2070 Net-Zero target and renewable energy (500 GW) represent critical national responses to this accelerating climate crisis.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- UNEP Emissions Gap Report 2025 ---
        {
            "id": 25082,
            "question_text": "The UNEP Emissions Gap Report 2025 'Off Target' projects what warming range by 2100 under full NDC implementation?",
            "option_a": "1.5-1.8°C",
            "option_b": "1.9-2.2°C",
            "option_c": "2.3-2.5°C",
            "option_d": "3.0-3.5°C",
            "correct_answer": "C",
            "explanation": "UNEP's November 2025 'Off Target' report projects 2.3-2.5°C warming even with full NDC implementation—showing critical gap between commitments and climate reality. Achieving 1.5°C requires 55% emissions cuts by 2035; 2°C requires 35%. India's NDC enhancement focusing on renewable energy (500 GW) and forest expansion contributes to global mitigation, but scaling remains urgent. This emissions gap underscores why adaptation finance and loss-and-damage mechanisms are essential complements to mitigation for climate-vulnerable nations.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- CBD COP16 + Rome ---
        {
            "id": 25083,
            "question_text": "The resumed CBD COP16.2 session in Rome (February 25-27, 2025) agreed to mobilize how much in annual biodiversity finance by 2030?",
            "option_a": "$30 billion",
            "option_b": "$100 billion",
            "option_c": "$200 billion",
            "option_d": "$500 billion",
            "correct_answer": "C",
            "explanation": "CBD COP16.2 (Rome, Feb 25-27, 2025) finalized $200 billion/year biodiversity finance roadmap—scaling from $20 billion/year international flows (2025) to $30 billion (2030). This commitment responds to CBD 2030 targets for halting species loss and ecosystem degradation. Biodiversity finance directly supports climate adaptation through ecosystem restoration, wetland protection, and species conservation. India's 99 Ramsar sites and 1,174 threatened species require substantial finance for implementation of CBD targets aligned with climate resilience.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Cali Fund ---
        {
            "id": 25084,
            "question_text": "The 'Cali Fund', launched at CBD COP16.2 in Rome on February 26, 2025, collects contributions from industries using which resource?",
            "option_a": "Fossil fuels",
            "option_b": "Digital Sequence Information (DSI) on genetic resources",
            "option_c": "Rare earth minerals",
            "option_d": "Marine plastics",
            "correct_answer": "B",
            "explanation": "Cali Fund (launched Rome, Feb 26, 2025, UNDP/UNEP) mobilizes pharmaceutical, biotech, and cosmetics industry contributions from Digital Sequence Information (genetic data) usage—with 50% minimum to Indigenous/local communities. This mechanism ensures equitable benefit-sharing from biodiversity while funding conservation. India's 683 newly documented species in 2024 and genetic diversity in biodiversity hotspots position the country as major DSI beneficiary. The fund supports conservation financing while recognizing Indigenous knowledge contributions to climate-resilient ecosystem management.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- INC-5.2 Plastic Treaty ---
        {
            "id": 25085,
            "question_text": "INC-5.2, the resumed UN Plastic Treaty negotiations held in August 2025, took place in which city?",
            "option_a": "Busan",
            "option_b": "Nairobi",
            "option_c": "Geneva",
            "option_d": "Paris",
            "correct_answer": "C",
            "explanation": "INC-5.2 (Geneva, August 5-15, 2025) continued plastic treaty gridlock between High Ambition Coalition (production caps) and oil-producing states (Saudi Arabia, Russia, Iran). The impasse reflects competing economic interests versus environmental urgency—nurdles pollution (Kerala, May 2025) exemplifies costs of inadequate action. India's 2024 plastic crisis intersects climate change and pollution; a binding plastic treaty is essential for ocean health and climate resilience. Continued negotiations are critical for global plastic circularity and pollution prevention.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- UNOC3 Nice ---
        {
            "id": 25086,
            "question_text": "The 3rd UN Ocean Conference (UNOC3) was co-hosted by France and Costa Rica in June 2025 in which city?",
            "option_a": "Lisbon",
            "option_b": "Nice",
            "option_c": "Marseille",
            "option_d": "San José",
            "correct_answer": "B",
            "explanation": "UNOC3 (Nice, June 9-13, 2025) catalyzed BBNJ treaty ratification momentum—19 new signatories brought total to 50+EU, approaching the 60-ratification threshold for entry into force (projected January 2026). This landmark agreement establishes marine protected areas and genetic resource sharing, essential for ocean health and climate resilience. India's ocean governance aligns with BBNJ principles through coastal protection and marine biodiversity conservation, critical as ocean warming and acidification threaten fisheries supporting millions.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- BBNJ Treaty ---
        {
            "id": 25087,
            "question_text": "The BBNJ Agreement (High Seas Treaty) enters into force how many days after the 60th instrument of ratification is deposited at the UN?",
            "option_a": "30 days",
            "option_b": "60 days",
            "option_c": "90 days",
            "option_d": "120 days",
            "correct_answer": "D",
            "explanation": "BBNJ (Biodiversity Beyond National Jurisdiction) enters into force 120 days after 60th ratification—projected for January 2026. This historic agreement establishes high seas marine protected areas and equitable benefit-sharing from marine genetic resources. Entry into force will revolutionize ocean governance for climate adaptation—marine ecosystems are critical carbon sinks. India's ratification will support regional ocean conservation and climate resilience in the Indian Ocean facing warming, acidification, and biodiversity loss.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Ramsar COP15 Zimbabwe ---
        {
            "id": 25088,
            "question_text": "Ramsar COP15, the 15th Meeting of the Conference of the Contracting Parties to the Convention on Wetlands (July 23-31, 2025), was held in which African resort city?",
            "option_a": "Cape Town",
            "option_b": "Kigali",
            "option_c": "Victoria Falls",
            "option_d": "Nairobi",
            "correct_answer": "C",
            "explanation": "Ramsar COP15 (Victoria Falls, July 23-31, 2025) adopted restoration-focused 'Victoria Falls Declaration' (4 goals/18 targets), signaling urgent wetland protection response to climate-driven water stress and ecosystem collapse. India's 99 Ramsar sites (13,60,805 hectares) and budget increases reflect commitment to wetland conservation—critical for water security, biodiversity, and carbon storage. Wetland restoration aligns with climate adaptation strategies addressing monsoon variability and extreme flood/drought cycles under India's 2070 Net-Zero framework.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- CITES CoP20 Samarkand ---
        {
            "id": 25089,
            "question_text": "CITES CoP20, held November 24 - December 5, 2025, was the first Conference of Parties of CITES hosted in Central Asia. Which city hosted it?",
            "option_a": "Astana, Kazakhstan",
            "option_b": "Samarkand, Uzbekistan",
            "option_c": "Bishkek, Kyrgyzstan",
            "option_d": "Tashkent, Uzbekistan",
            "correct_answer": "B",
            "explanation": "CITES CoP20 (Samarkand, Nov 24-Dec 5, 2025) added 77 species to Appendices (okapi, striped hyena, geckos, tarantulas, guggul, ginseng, aloes, brazilwood)—reflecting global urgency to regulate wildlife trade amid climate-driven extinction risk. CITES protects 1,174 threatened species in India from overexploitation. Trade regulation complements habitat protection and climate adaptation, essential for species survival as climate change compounds poaching pressure. Guggul listing demonstrates recognition of medicinal plant value in conservation."
        # --- Mission Mausam ---
        {
            "id": 25090,
            "question_text": "'Mission Mausam', launched by the Government of India on September 14, 2024, has what total outlay for 2024-26?",
            "option_a": "₹500 crore",
            "option_b": "₹1,000 crore",
            "option_c": "₹2,000 crore",
            "option_d": "₹5,000 crore",
            "correct_answer": "C",
            "explanation": "Mission Mausam (₹2,000 crore, 2024-26) advances India's climate-smart weather capabilities through IMD, IITM Pune, and NCMRWF. Enhanced nowcasting, weather modification, and air-quality forecasting support disaster risk reduction, agricultural planning, and renewable energy integration—critical for climate resilience. The program exemplifies India's Green Growth strategy combining weather forecasting innovation with climate adaptation for development. Enhanced early warning systems directly reduce climate disaster impacts on vulnerable populations and agriculture-dependent livelihoods.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- ISFR 2023 ---
        {
            "id": 25091,
            "question_text": "Per the India State of Forest Report (ISFR) 2023 — the 18th edition — India's forest cover is approximately what percentage of its geographical area?",
            "option_a": "19.45%",
            "option_b": "21.76%",
            "option_c": "24.62%",
            "option_d": "27.10%",
            "correct_answer": "B",
            "explanation": "ISFR 2023 (December 2024) documents India's 21.76% forest cover (7,15,343 sq km) and 3.41% tree cover (1,12,014 sq km), totalling 25.17%—a trajectory toward India's afforestation targets. The 1,445 sq km increase since 2021 (Chhattisgarh leading with 684 sq km) demonstrates expanding carbon sinks essential for climate mitigation. Forest cover expansion supports biodiversity protection while contributing to India's 2070 Net-Zero commitment through enhanced carbon sequestration—critical as forests remain threatened by agriculture, mining, and urbanization pressures.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- LA Wildfires Jan 2025 ---
        {
            "id": 25092,
            "question_text": "The deadly Palisades and Eaton wildfires that struck the Los Angeles area in January 2025 were primarily fanned by which wind phenomenon?",
            "option_a": "Chinook winds",
            "option_b": "Foehn winds",
            "option_c": "Santa Ana winds",
            "option_d": "Mistral winds",
            "correct_answer": "C",
            "explanation": "LA's January 2025 wildfires (14 fires, 31 deaths, 18,000+ structures lost) driven by Santa Ana winds (100 mph gusts) exemplify compound climate impacts: intense droughts, low humidity, and fire-prone winds combine catastrophically. Climate change is intensifying wildfire seasons globally—Canada 2024, Australia 2019-20, California annually. These extreme weather cascades foreshadow India's climate vulnerabilities: monsoon shifts, drought-flood cycles, and increasing fire risk in Himalayan and central Indian forests requiring enhanced disaster preparedness and climate adaptation investment.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- NASA 2024 warmest ---
        {
            "id": 25093,
            "question_text": "Per NASA GISS, by how much was Earth's surface temperature in 2024 above the 1951-1980 baseline — confirming 2024 as the warmest year on record?",
            "option_a": "0.85°C",
            "option_b": "1.28°C",
            "option_c": "1.55°C",
            "option_d": "2.10°C",
            "correct_answer": "B",
            "explanation": "NASA GISS confirmed 2024's 1.28°C above 1951-1980 baseline (1.47°C above 1850-1900 pre-industrial), establishing new temperature record. The 15-month streak of consecutive records (June 2023-August 2024) signals accelerating warming trajectory. Ocean heat content reached record highs, intensifying monsoon variability and extreme weather. This warming trajectory directly threatens India's agriculture, water resources, and vulnerable populations—underscoring urgency of rapid renewable energy deployment (500 GW) and climate adaptation financing for resilience.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- La Niña 2025-26 ---
        {
            "id": 25094,
            "question_text": "Per NOAA's ENSO Diagnostic Discussion, which phase of the El Niño-Southern Oscillation prevailed during the 2025-26 northern winter?",
            "option_a": "Strong El Niño",
            "option_b": "Weak La Niña",
            "option_c": "Strong La Niña",
            "option_d": "ENSO-neutral with no anomaly",
            "correct_answer": "B",
            "explanation": "NOAA's weak La Niña forecast (Dec-Feb 2025-26, 51% probability) followed by ENSO-neutral transition and El Niño re-emergence (May-Jul 2026, 82%) directly impacts India's monsoon patterns. La Niña typically enhances monsoon precipitation while El Niño suppresses it—critical for agriculture, hydropower, and water security. This ENSO cycle variation requires adaptive water management and crop planning. India's monsoon predictability and climate adaptation strategies must account for ENSO teleconnections central to South Asian climate variability.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Bonn SB62 ---
        {
            "id": 25095,
            "question_text": "The Bonn Climate Change Conference (SB62), the 62nd session of the UNFCCC Subsidiary Bodies held June 16-26, 2025, achieved progress mainly on which work programme?",
            "option_a": "Loss and Damage Fund operationalisation",
            "option_b": "Just Transition Work Programme",
            "option_c": "Article 6 carbon markets",
            "option_d": "Global Stocktake",
            "correct_answer": "B",
            "explanation": "SB62 (Bonn, June 16-26, 2025) advanced Just Transition Work Programme recognizing human rights, Indigenous knowledge, and participatory processes—critical for equitable climate action. India's agricultural negotiating stance blocked GGA progress, asserting that adaptation finance must prioritize developing nations' food security amid climate stress. This reflects India's position that climate justice requires balancing mitigation with adaptation investment protecting vulnerable populations and agricultural systems facing monsoon uncertainty and water stress.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- WMO Air Quality & Climate Bulletin 2025 ---
        {
            "id": 25096,
            "question_text": "The WMO Air Quality and Climate Bulletin No. 5 (September 2025) emphasised what 'vicious cycle' linking climate and air pollution?",
            "option_a": "Ozone depletion and skin cancer",
            "option_b": "Climate change, wildfires and PM2.5 air pollution",
            "option_c": "Methane leaks and stratospheric warming",
            "option_d": "Coral bleaching and ocean acidification",
            "correct_answer": "B",
            "explanation": "WMO Bulletin No. 5 (September 2025) documented climate-wildfire-PM2.5 feedback cycle: warming intensifies fire seasons; wildfires emit massive PM2.5 concentrations (Chile, Brazil, Ecuador, Canada, Africa, Siberia); aerosols alter atmospheric heating and precipitation. India faces similar dynamics—rising temperatures intensify agricultural burning (Punjab, Haryana) and forest fires (Himalayan regions) creating severe winter air pollution. Breaking this cycle requires integrated climate-air quality strategies combining wildfire prevention, renewable energy transition, and clean cooking fuels in India's Green Growth agenda.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- COP30 sponsor countries ---
        {
            "id": 25097,
            "question_text": "Which country pledged the single largest contribution ($3 billion) to the Tropical Forests Forever Facility (TFFF) launched at COP30 Belém?",
            "option_a": "Germany",
            "option_b": "France",
            "option_c": "Norway",
            "option_d": "United States",
            "correct_answer": "C",
            "explanation": "Norway's $3 billion TFFF pledge (November 2025) demonstrates commitment to tropical forest protection—critical for global climate stabilization. This financing mechanism, supporting forests at $4/hectare/year with 20% minimum to Indigenous communities, recognizes forests' irreplaceable carbon storage and biodiversity value. India's tropical forest protection (through tiger reserves, sacred groves, tribal territories) benefits from TFFF framework. International forest financing aligns with India's afforestation targets and climate adaptation strategy under 2070 Net-Zero commitment.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- COP31 host 2026 ---
        {
            "id": 25098,
            "question_text": "Which country was confirmed to host COP31 in 2026 after resolving a long-running bid dispute with Turkey?",
            "option_a": "Canada",
            "option_b": "Australia (in partnership with Pacific Island states)",
            "option_c": "South Africa",
            "option_d": "India",
            "correct_answer": "B",
            "explanation": "Australia's COP31 hosting (2026, partnering Pacific Island states) shifts climate leadership to Indo-Pacific region facing acute climate impacts: coral bleaching, sea-level rise, intensifying cyclones. Australia's climate challenges—droughts, wildfires, heatwaves—align with global warming patterns expected under 1.5-2°C scenarios. This COP sequence (Dubai, Baku, Belém, Australia, Ethiopia 2027) demonstrates rotating regional responsibility for climate governance, essential for building inclusive global consensus on ambitious climate action.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- CITES CoP20 species count ---
        {
            "id": 25099,
            "question_text": "At CITES CoP20 in Samarkand (Nov-Dec 2025), approximately how many new species were added to the CITES Appendices regulating international wildlife trade?",
            "option_a": "27",
            "option_b": "51",
            "option_c": "77",
            "option_d": "114",
            "correct_answer": "C",
            "explanation": "CITES CoP20's 77 new Appendix species listings (okapi, striped hyena, geckos, tarantulas, guggul, ginseng, aloes, brazilwood) represent urgent response to wildlife trade-driven extinction risk compounded by climate change. Guggul listing reflects recognition of overexploited medicinal plant value. Trade regulation combined with habitat protection and climate adaptation forms integrated approach to species conservation. India's 1,174 IUCN-threatened species require CITES protections preventing international trafficking that exploits climate-stressed wild populations.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
        },
        # --- Ramsar India Tamil Nadu lead ---
        {
            "id": 25100,
            "question_text": "Which Indian state has the highest number of Ramsar Sites as of April 2026, when India's total reached 99 (highest in Asia)?",
            "option_a": "Uttar Pradesh",
            "option_b": "Kerala",
            "option_c": "Tamil Nadu",
            "option_d": "West Bengal",
            "correct_answer": "C",
            "explanation": "Tamil Nadu's 20 Ramsar sites (highest state-level designation) reflect South Indian wetland biodiversity and leadership in protection. India's 99 Ramsar sites (13,60,805 hectares, 67 additions since 2014) position Asia's wetland conservation network. These ecosystems face climate-driven water stress, monsoon variability, and saltwater intrusion—demanding urgent restoration investment. Ramsar wetland protection aligns with water security strategies, biodiversity conservation, and carbon storage critical for India's 2070 Net-Zero pathway and climate resilience under intensifying climate change impacts.",
            "folder": "AP_HC",
            "topic": "International_Current_Affairs"
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
    print("Environment & Climate MCQs seeded: IDs 25001–25100")
