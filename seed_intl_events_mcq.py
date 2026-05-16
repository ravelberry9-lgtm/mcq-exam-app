"""
Seed: International Events, Appointments & Developments MCQs
IDs 29001–29080 | Topic: National_Current_Affairs
Run standalone: python seed_intl_events_mcq.py
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
    # ── Global Elections & Leadership ──
    (29001, "Donald Trump was elected as the _____ President of the United States in November 2024.",
     "45th", "46th", "47th", "48th",
     "C", "Donald Trump won the US Presidential Election on November 5, 2024, becoming the 47th President. He was inaugurated on January 20, 2025, with JD Vance as Vice President.",
     "General_Science", "National_Current_Affairs"),

    (29002, "Who became the Prime Minister of the United Kingdom after the Labour Party's landslide victory in July 2024?",
     "Boris Johnson", "Rishi Sunak", "Keir Starmer", "Jeremy Corbyn",
     "C", "Keir Starmer became UK Prime Minister after Labour won the July 4, 2024 general election with a landslide, defeating Rishi Sunak's Conservative Party.",
     "General_Science", "National_Current_Affairs"),

    (29003, "Sanae Takaichi, elected as Japan's first female Prime Minister in October 2025, was Japan's _____ Prime Minister.",
     "100th", "102nd", "104th", "106th",
     "C", "Sanae Takaichi was elected Japan's first female Prime Minister on October 21, 2025, becoming the 104th PM. Her LDP formed a coalition with Japan Innovation Party (Ishin).",
     "General_Science", "National_Current_Affairs"),

    (29004, "Who became Canada's Prime Minister in March 2025, succeeding Justin Trudeau?",
     "Chrystia Freeland", "Mark Carney", "Pierre Poilievre", "Jagmeet Singh",
     "B", "Mark Carney, former Governor of Bank of Canada and Bank of England, became Canada's Prime Minister on March 14, 2025 after Justin Trudeau resigned in January 2025.",
     "General_Science", "National_Current_Affairs"),

    (29005, "Friedrich Merz became the Chancellor of Germany after which party won the February 2025 elections?",
     "SPD", "FDP", "CDU/CSU", "Greens",
     "C", "Friedrich Merz of CDU/CSU won the German federal elections held on February 23, 2025, succeeding Olaf Scholz (SPD) whose coalition had collapsed.",
     "General_Science", "National_Current_Affairs"),

    (29006, "South Korean President Yoon Suk-yeol was impeached in December 2024 after declaring:",
     "Emergency economic policy", "Martial law", "State of war", "Presidential emergency",
     "B", "President Yoon Suk-yeol declared martial law on December 3, 2024. The National Assembly voted to impeach him on December 14, 2024. The Constitutional Court upheld the impeachment on April 4, 2025.",
     "General_Science", "National_Current_Affairs"),

    (29007, "Who won South Korea's snap presidential election held on June 3, 2025?",
     "Han Duck-soo", "Lee Jae-myung", "Yoon Suk-yeol", "Hong Joon-pyo",
     "B", "Lee Jae-myung of the Democratic Party won South Korea's snap presidential election on June 3, 2025, following the impeachment and removal of Yoon Suk-yeol.",
     "General_Science", "National_Current_Affairs"),

    (29008, "Sushila Karki was sworn as interim Prime Minister of Nepal in 2025. She was previously Nepal's first:",
     "Foreign Minister", "Defence Minister", "Chief Justice", "Finance Minister",
     "C", "Sushila Karki, 73, was Nepal's first woman Chief Justice (2016-17), known for her zero-tolerance stance on corruption. She became interim PM after mass protests forced KP Sharma Oli to resign.",
     "General_Science", "National_Current_Affairs"),

    (29009, "Andrew Holness won a _____ term as Prime Minister of Jamaica in the September 2025 elections.",
     "First", "Second", "Third", "Fourth",
     "C", "Andrew Holness won a third term as PM of Jamaica, with his Jamaica Labour Party (JLP) winning 34 of 63 seats. Jamaica recorded a 43% drop in killings in 2025 under his tenure.",
     "General_Science", "National_Current_Affairs"),

    (29010, "Sheikh Hasina resigned as Prime Minister of Bangladesh on August 5, 2024, after student-led protests. Who heads Bangladesh's interim government?",
     "General Waker-Uz-Zaman", "Muhammad Yunus", "Kamal Hossain", "Mirza Fakhrul Islam",
     "B", "Nobel laureate economist Muhammad Yunus was invited to head Bangladesh's interim government after Sheikh Hasina fled to India on August 5, 2024, following student-led mass protests.",
     "General_Science", "National_Current_Affairs"),

    # ── Pope & Vatican ──
    (29011, "Pope Francis, who passed away on April 21, 2025, was the first pope from which continent?",
     "Asia", "Africa", "North America", "South America",
     "D", "Pope Francis (Jorge Mario Bergoglio, born in Argentina) was the first pope from Latin America (South America). He served from 2013 to 2025 and died at the age of 88.",
     "General_Science", "National_Current_Affairs"),

    (29012, "Pope Leo XIV, elected on May 8, 2025, holds the distinction of being the:",
     "First African pope", "First Asian pope", "First American pope", "First Eastern European pope",
     "C", "Pope Leo XIV (birth name: Robert Francis Prevost, born in Chicago, USA) is the first American pope in history. He is also the first Augustinian to become pope.",
     "General_Science", "National_Current_Affairs"),

    # ── Syria / Global Conflicts ──
    (29013, "Bashar al-Assad fled Syria on December 8, 2024, as rebel forces captured Damascus. Which group led the rebel coalition?",
     "ISIS", "Al-Qaeda", "HTS (Hayat Tahrir al-Sham)", "Free Syrian Army",
     "C", "Hayat Tahrir al-Sham (HTS), led by Ahmed al-Sharaa (also known as Abu Mohammad al-Jolani), captured Damascus on December 8, 2024. Assad fled to Russia, ending 54 years of Assad family rule.",
     "General_Science", "National_Current_Affairs"),

    (29014, "The Gaza ceasefire Phase 1 agreement was reached on January 15, 2025. Which three countries mediated it?",
     "USA, UK, France", "Qatar, Egypt, USA", "Saudi Arabia, Jordan, USA", "UN, Egypt, Qatar",
     "B", "The Phase 1 ceasefire between Israel and Hamas was mediated by Qatar, Egypt, and the United States. It began on January 19, 2025 and involved a hostage-prisoner exchange.",
     "General_Science", "National_Current_Affairs"),

    # ── India – Operation Sindoor ──
    (29015, "India launched Operation Sindoor on May 7, 2025, in response to which terrorist attack?",
     "Uri attack", "Pulwama attack", "Pahalgam attack", "Pathankot attack",
     "C", "India launched Operation Sindoor on May 7, 2025, with precision strikes on 9 terror infrastructure sites in Pakistan and PoK, in response to the Pahalgam terrorist attack (April 22, 2025) in which 26 tourists were killed.",
     "General_Science", "National_Current_Affairs"),

    (29016, "How many terror infrastructure sites in Pakistan and Pakistan-occupied Kashmir were struck during Operation Sindoor?",
     "5", "7", "9", "12",
     "C", "Operation Sindoor targeted 9 terror infrastructure sites in Pakistan and PoK on May 7, 2025. India-Pakistan ceasefire was announced on May 10, 2025.",
     "General_Science", "National_Current_Affairs"),

    # ── BRICS ──
    (29017, "Which of the following countries did NOT join BRICS as a new member on January 1, 2024?",
     "Saudi Arabia", "Egypt", "Turkey", "Iran",
     "C", "The new BRICS members who joined on January 1, 2024 were: Saudi Arabia, UAE, Egypt, Iran, and Ethiopia. Turkey did NOT join BRICS in 2024.",
     "General_Science", "National_Current_Affairs"),

    (29018, "The BRICS Summit 2024 was held in which city?",
     "Beijing, China", "Moscow, Russia", "Kazan, Russia", "New Delhi, India",
     "C", "The BRICS Summit 2024 was held in Kazan, Russia, in October 2024. After the new members joined in January 2024, BRICS expanded to 10 members.",
     "General_Science", "National_Current_Affairs"),

    # ── WHO & Health ──
    (29019, "The WHO declared a polio outbreak in which country in 2025, a nation that had been polio-free since 2000?",
     "Fiji", "Papua New Guinea", "Solomon Islands", "Vanuatu",
     "B", "WHO declared a polio outbreak in Papua New Guinea after poliovirus was found in healthy children in Lae city during routine screening. Low immunisation rates led to the return after the country was polio-free since 2000.",
     "General_Science", "National_Current_Affairs"),

    (29020, "Suriname became the first country in the Amazon region to receive WHO malaria-free certification on:",
     "January 15, 2025", "March 28, 2025", "June 30, 2025", "September 12, 2025",
     "C", "WHO certified Suriname malaria-free on June 30, 2025 — making it the first Amazon region country to achieve this recognition, after nearly 70 years of efforts.",
     "General_Science", "National_Current_Affairs"),

    (29021, "The World Health Assembly (WHA) of WHO passed a resolution titled 'Skin Diseases as a Global Public Health Priority'. Skin diseases affect approximately how many people worldwide?",
     "500 million", "1.1 billion", "1.9 billion", "2.5 billion",
     "C", "Skin diseases affect approximately 1.9 billion people globally. The WHO World Health Assembly passed the resolution calling for a Global Action Plan focused on prevention, detection, treatment, and care.",
     "General_Science", "National_Current_Affairs"),

    # ── International Bodies & HQs ──
    (29022, "Where is the headquarters of the International Atomic Energy Agency (IAEA) located?",
     "Geneva, Switzerland", "New York, USA", "Vienna, Austria", "Brussels, Belgium",
     "C", "The IAEA is headquartered in Vienna, Austria. Its Statute was approved on October 23, 1956 and came into force on July 29, 1957. It has 178 member countries.",
     "General_Science", "National_Current_Affairs"),

    (29023, "ICAO was established under which international convention of 1944?",
     "Geneva Convention", "Vienna Convention", "Montreal Convention", "Chicago Convention",
     "D", "The International Civil Aviation Organization (ICAO) was established under the Chicago Convention of 1944. Its headquarters are in Montreal, Canada. It is a UN specialized agency.",
     "General_Science", "National_Current_Affairs"),

    (29024, "Where is the headquarters of UNODC (United Nations Office on Drugs and Crime)?",
     "Geneva, Switzerland", "New York, USA", "Vienna, Austria", "Brussels, Belgium",
     "C", "UNODC is headquartered in Vienna, Austria. It was established in 1997 by merging the UN Drug Control Programme and Centre for International Crime Prevention.",
     "General_Science", "National_Current_Affairs"),

    (29025, "Khaled el-Anani, nominated as the next Director-General of UNESCO, is from which country?",
     "Morocco", "Tunisia", "Egypt", "Algeria",
     "C", "Khaled el-Anani, former Egyptian Minister of Tourism and Antiquities, was nominated as the next Director-General of UNESCO. UNESCO is headquartered in Paris, France.",
     "General_Science", "National_Current_Affairs"),

    (29026, "The New Development Bank (NDB) was established by BRICS nations. Where is its headquarters?",
     "Beijing, China", "Mumbai, India", "Shanghai, China", "Moscow, Russia",
     "C", "The NDB (also known as BRICS Development Bank) is headquartered in Shanghai, China. It was set up by Brazil, Russia, India, China, and South Africa to fund infrastructure and sustainable development.",
     "General_Science", "National_Current_Affairs"),

    (29027, "MERCOSUR, the South American trade bloc, was established by which treaty?",
     "Treaty of Montevideo", "Treaty of Asunción", "Treaty of Buenos Aires", "Treaty of Brasilia",
     "B", "MERCOSUR (Southern Common Market) was established in 1991 through the Treaty of Asunción. Its headquarters are in Montevideo, Uruguay. Original members: Argentina, Brazil, Paraguay, Uruguay.",
     "General_Science", "National_Current_Affairs"),

    (29028, "The International Electrotechnical Commission (IEC), established in 1906, is headquartered in:",
     "London, UK", "Paris, France", "Geneva, Switzerland", "Vienna, Austria",
     "C", "IEC is headquartered in Geneva, Switzerland. India hosted the 89th IEC General Meeting at Bharat Mandapam, New Delhi, in September 2025 — the 4th time India hosted.",
     "General_Science", "National_Current_Affairs"),

    (29029, "The Codex Alimentarius Commission (CAC), which sets international food standards, was jointly established by:",
     "WHO and UNICEF", "FAO and WHO", "World Bank and FAO", "WTO and FAO",
     "B", "The Codex Alimentarius Commission was established jointly by FAO (Food and Agriculture Organization) and WHO. India's role in Millets Group Standards was appreciated at the 88th Executive Committee session in Rome, July 2025.",
     "General_Science", "National_Current_Affairs"),

    (29030, "Who is the WTO Director General, who was reappointed for a second term through 2027, and holds the distinction of being the first woman and first African to lead WTO?",
     "Christine Lagarde", "Kristalina Georgieva", "Ngozi Okonjo-Iweala", "Amina Mohammed",
     "C", "Ngozi Okonjo-Iweala (Nigeria) is the WTO Director General, reappointed for a second term through 2027. She is the first African and first woman to lead the World Trade Organization.",
     "General_Science", "National_Current_Affairs"),

    # ── India International ──
    (29031, "India launched Operation Sagar Bandhu to provide HADR assistance to Sri Lanka after which natural disaster?",
     "Cyclone Ditwah", "Cyclone Michaung", "Cyclone Remal", "Cyclone Biparjoy",
     "A", "India launched Operation Sagar Bandhu after Cyclone Ditwah made landfall in Sri Lanka on November 27, 2025. The IAF delivered approximately 12 tonnes of relief including tents, blankets, and ready-to-eat food.",
     "General_Science", "National_Current_Affairs"),

    (29032, "BHISHM Cubes were gifted by India to Maldives on the occasion of Maldives' 60th Independence Day. BHISHM stands for:",
     "Bharat Health Initiative for Sahyog, Hita & Maitri", "Bharat Humanitarian Initiative for Safety, Health & Medicine", "Bharat Health Infrastructure for Surge, Hazard & Management", "Bharat Help Initiative for Stabilisation, Health & Medicine",
     "A", "BHISHM = Bharat Health Initiative for Sahyog, Hita & Maitri. The PM gifted 2 BHISHM cubes to Maldivian President Mohamed Muizzu. Each cube handles 200 emergency cases and includes AI systems and surgical tools.",
     "General_Science", "National_Current_Affairs"),

    (29033, "India is the first country to hold two ISA (International Seabed Authority) contracts for exploring which mineral deposit in the Indian Ocean?",
     "Polymetallic nodules", "Cobalt-rich crusts", "Polymetallic sulphides", "Phosphorite nodules",
     "C", "India became the first country to hold two ISA contracts for polymetallic sulphides in the Indian Ocean. These deposits contain copper, zinc, gold, and silver — essential for clean energy and high-tech applications.",
     "General_Science", "National_Current_Affairs"),

    (29034, "Which Indian agency represents India as the national central bureau for Interpol matters?",
     "NIA (National Investigation Agency)", "RAW (Research and Analysis Wing)", "CBI (Central Bureau of Investigation)", "IB (Intelligence Bureau)",
     "C", "The CBI (Central Bureau of Investigation) is India's national central bureau for Interpol. India was elected to the Interpol Asian Committee at the 25th Asian Regional Conference held in Singapore.",
     "General_Science", "National_Current_Affairs"),

    (29035, "The India-UK Free Trade Agreement was signed in which month of 2025?",
     "January 2025", "March 2025", "May 2025", "August 2025",
     "C", "The India-UK Free Trade Agreement (FTA) was signed on May 6, 2025, after about 3 years of negotiations (beginning 2022). It covers goods, services, digital trade, and investment.",
     "General_Science", "National_Current_Affairs"),

    (29036, "LeadIT (Leadership Group for Industry Transition) was launched jointly by India and which country in 2019?",
     "Germany", "Sweden", "Norway", "Denmark",
     "B", "LeadIT was launched in 2019 by India and Sweden, supported by the World Economic Forum (WEF). It targets net-zero emissions from heavy industries by 2050. Its secretariat is hosted by the Stockholm Environment Institute.",
     "General_Science", "National_Current_Affairs"),

    (29037, "India re-elected to Part II of ICAO Council represents states that:",
     "Have most aircraft in service", "Contribute most to international civil air navigation facilities", "Have the most airports", "Carry most international passengers",
     "B", "Part II of the ICAO Council represents states contributing most to international civil air navigation facilities. India has been a founding ICAO member since 1944 — 81 years of uninterrupted Council presence.",
     "General_Science", "National_Current_Affairs"),

    (29038, "Which pilgrimage to Tibet was resumed by India in 2025 after a 5-year gap, as part of India-China rapprochement?",
     "Mansarovar Yatra via Nathu La", "Kailash Mansarovar Yatra", "Kang Rinpoche Yatra", "Tso Mapham Pilgrimage",
     "B", "The Kailash Mansarovar Yatra was resumed in 2025 after a 5-year pause, as part of India-China confidence-building measures. India and China also restored visas, flights, and resumed water-data sharing on rivers.",
     "General_Science", "National_Current_Affairs"),

    (29039, "Russia formally recognised the Taliban government of Afghanistan on July 3, 2025. Which country does this make Russia in terms of recognising the Taliban?",
     "First country", "Second country", "Third country", "Fifth country",
     "A", "Russia became the first country in the world to formally recognise the Taliban government (which took power in 2021). Russia removed Taliban from its list of outlawed organisations and accepted Afghanistan's ambassador.",
     "General_Science", "National_Current_Affairs"),

    (29040, "The Bagram Air Base, which the Taliban rejected returning to the US in 2025, is located north of which city in Afghanistan?",
     "Kandahar", "Herat", "Kabul", "Mazar-i-Sharif",
     "C", "Bagram Air Base is located north of Kabul, Afghanistan. It is the largest airbase in Afghanistan, originally built by the Soviet Union and later used by the US as its largest military installation in Afghanistan.",
     "General_Science", "National_Current_Affairs"),

    # ── Countries in News ──
    (29041, "China's Tianwen-2 mission was launched to collect samples from which asteroid?",
     "Bennu", "Ryugu", "2016HO3", "Apophis",
     "C", "China launched the Tianwen-2 probe on a Long March 3-B rocket to collect samples from asteroid 2016HO3 and explore the main-belt comet 311P. The mission continues till end of 2027.",
     "General_Science", "National_Current_Affairs"),

    (29042, "Iran's Bushehr plant is the country's only operational nuclear power facility. It was completed by which country in 2011?",
     "China", "North Korea", "Russia", "France",
     "C", "Bushehr nuclear plant, Iran's only operational nuclear facility, was completed by Russia in May 2011. Russia announced plans to build eight more nuclear plants in Iran under an existing agreement.",
     "General_Science", "National_Current_Affairs"),

    (29043, "The South Pars gas field, the world's largest natural gas field, is jointly owned by Iran and which country?",
     "Kuwait", "Iraq", "Saudi Arabia", "Qatar",
     "D", "South Pars gas field, located in Bushehr province in the Persian Gulf, is jointly owned by Iran and Qatar. Iran is the world's 3rd largest gas producer (~275 billion cubic metres/year).",
     "General_Science", "National_Current_Affairs"),

    (29044, "Israel's 'Samson Option' refers to which defense doctrine?",
     "Cyber warfare first-strike capability", "Massive nuclear retaliation if facing existential threat", "Iron Dome missile defence expansion", "Pre-emptive conventional military strikes",
     "B", "The Samson Option is Israel's alleged doctrine of massive nuclear retaliation if the country faces an existential threat. Israel follows 'amimut' (deliberate ambiguity) — neither confirming nor denying nuclear weapons.",
     "General_Science", "National_Current_Affairs"),

    (29045, "Typhoon Danas made a rare direct landfall in which country's Chiayi County — the first recorded typhoon strike there?",
     "Japan", "Philippines", "Taiwan", "Vietnam",
     "C", "Typhoon Danas made a rare and unusual direct landfall in Chiayi County, Taiwan — the first recorded typhoon strike in the area. Gusts reached up to 222 km/h.",
     "General_Science", "National_Current_Affairs"),

    (29046, "Mount Lewotobi Laki-laki, which erupted sending ash 10 km high, is located on which island of Indonesia?",
     "Java", "Sumatra", "Bali", "Flores",
     "D", "Mount Lewotobi Laki-laki is an active stratovolcano located on Flores island in East Nusa Tenggara province, Indonesia. It is part of the twin-peaked Lewotobi volcanic complex within the Pacific Ring of Fire.",
     "General_Science", "National_Current_Affairs"),

    (29047, "Hawaii became the first US state to introduce a 'Green Fee'. This fee applies to all of the following EXCEPT:",
     "Hotel stays", "Short-term rentals", "Domestic flights", "Cruise ship passengers",
     "C", "Hawaii's Green Fee applies to hotel stays, short-term rentals, and cruise ship passengers. Domestic flights are not part of the fee. It funds climate resiliency, conservation, and invasive species control.",
     "General_Science", "National_Current_Affairs"),

    (29048, "Japan's AI law of May 2025 (Act on Promotion of Research, Development and Utilisation of AI) differs from the EU AI Act because it:",
     "Bans AI completely", "Takes a strict risk-level regulatory approach", "Encourages voluntary responsibility instead of heavy regulation", "Limits AI to government use only",
     "C", "Unlike the EU AI Act (2024) which divides AI into risk levels and imposes strict rules, Japan's approach encourages coordination and voluntary responsibility — a flexible model.",
     "General_Science", "National_Current_Affairs"),

    (29049, "Saudi Arabia's TOURISE platform was launched to redefine tourism for the next how many years?",
     "10 years", "25 years", "50 years", "100 years",
     "C", "Saudi Arabia launched TOURISE as a global platform for the next 50 years of tourism. The inaugural TOURISE Summit was scheduled for Riyadh, November 2025.",
     "General_Science", "National_Current_Affairs"),

    (29050, "According to the UN World Urbanisation Prospects 2025, which city became the world's most populous with approximately 42 million people?",
     "Tokyo", "Dhaka", "Beijing", "Jakarta",
     "D", "Jakarta became the world's most populous city (42 million) according to the UN World Urbanisation Prospects 2025. Dhaka is 2nd (37M) and Tokyo slipped to 3rd (33M). The change is due to a new standard definition of urban areas.",
     "General_Science", "National_Current_Affairs"),

    # ── Agreements & Initiatives ──
    (29051, "The EU's Carbon Border Adjustment Mechanism (CBAM) is part of which broader EU climate strategy?",
     "Green Deal 2030", "Fit for 55", "Net Zero Europe", "Carbon Zero Initiative",
     "B", "CBAM is part of the EU's 'Fit for 55' strategy — targeting a 55% reduction in greenhouse gas emissions by 2030. It targets carbon-intensive imports like steel, aluminium, and cement. Full enforcement begins 2026.",
     "General_Science", "National_Current_Affairs"),

    (29052, "The Blue NDC Challenge was launched by France and Brazil at which international conference?",
     "COP29 in Baku", "2nd UN Ocean Conference", "3rd UN Ocean Conference (UNOC3)", "G20 Environment Ministers Meeting",
     "C", "France and Brazil launched the Blue NDC Challenge at the 3rd United Nations Ocean Conference (UNOC3). The initiative urges countries to put oceans at the centre of their climate strategies ahead of COP30 in Belém, Brazil.",
     "General_Science", "National_Current_Affairs"),

    (29053, "NATO's annual Baltic Operations exercise BALTOPS 25 was held in which country?",
     "Norway", "Latvia", "Estonia", "Poland",
     "B", "NATO's BALTOPS 25 (Baltic Operations 2025) was held in Latvia. It is a large-scale multinational drill focused on rapid-response and interoperability across the Baltic Sea region.",
     "General_Science", "National_Current_Affairs"),

    (29054, "Russia announced it will launch the world's first nuclear power system with a closed fuel cycle by 2030. Where will it be built?",
     "St. Petersburg", "Novosibirsk", "Tomsk Region", "Chelyabinsk",
     "C", "Putin announced Russia will build the world's first closed fuel cycle nuclear power system in the Tomsk Region by 2030. It will reuse up to 95% of spent fuel, reducing waste and uranium demand.",
     "General_Science", "National_Current_Affairs"),

    (29055, "The SoLAR Phase II initiative on solar irrigation was launched by IWMI and which other organisation?",
     "World Bank", "IRENA", "SDC (Swiss Agency for Development and Cooperation)", "UNDP",
     "C", "SoLAR Phase II (Solar Irrigation for Agricultural Resilience) was launched by IWMI (International Water Management Institute) and SDC (Swiss Agency for Development and Cooperation). It covers India, Bangladesh, Kenya, and Ethiopia.",
     "General_Science", "National_Current_Affairs"),

    (29056, "The UK's 'One-In, One-Out' migration scheme is an agreement with which country about Channel crossings?",
     "Belgium", "Germany", "Netherlands", "France",
     "D", "The One-In-One-Out Scheme is a migration agreement between the UK and France. France takes back asylum seekers who crossed illegally; for each one returned, the UK grants asylum to one eligible migrant from France.",
     "General_Science", "National_Current_Affairs"),

    (29057, "ICAR launched 'Maitri 2.0', the second edition of the Brazil-India Cross-Incubation Programme. It relates to which sector?",
     "Defence", "Agritech", "Pharmaceuticals", "Space Technology",
     "B", "ICAR (Indian Council of Agricultural Research) launched Maitri 2.0 in New Delhi. It is the Brazil-India Cross-Incubation Programme in Agritech, building on the 77-year agricultural partnership between India and Brazil.",
     "General_Science", "National_Current_Affairs"),

    (29058, "The SICA (Central American Integration System) was established in 1991 through which protocol?",
     "Managua Protocol", "Panama Protocol", "Tegucigalpa Protocol", "Guatemala Protocol",
     "C", "SICA was established in 1991 through the Tegucigalpa Protocol, amending the Charter of the Organization of Central American States (ODECA) of 1962. India-SICA Foreign Ministers met in New York.",
     "General_Science", "National_Current_Affairs"),

    (29059, "The term 'Girmitiyas' refers to Indian indentured labourers who went to British colonies. The word 'Girmitiya' is derived from the Indian pronunciation of:",
     "Guarantee", "Agreement", "Government", "Grammar",
     "B", "The term 'Girmitiya' comes from 'girmit' — an Indian pronunciation of 'agreement'. These labourers signed agreements (girmit) to work in British colonies like Fiji, Mauritius, Trinidad, and Guyana.",
     "General_Science", "National_Current_Affairs"),

    (29060, "Which word was named Oxford University Press's Word of the Year 2025?",
     "Aura farming", "Biohack", "Rage bait", "Clickbait",
     "C", "Oxford University Press named 'Rage bait' as Word of the Year 2025. Its online usage rose three times, referring to content designed to provoke anger to increase views and traffic. It beat shortlisted words like 'aura farming' and 'biohack'.",
     "General_Science", "National_Current_Affairs"),

    # ── More International Bodies ──
    (29061, "IFAD (International Fund for Agricultural Development) is a specialised agency of which international body?",
     "World Bank", "IMF", "United Nations", "WTO",
     "C", "IFAD is an international financial institution and a specialised agency of the United Nations. Its primary objective is to eradicate poverty and hunger in rural areas of developing countries.",
     "General_Science", "National_Current_Affairs"),

    (29062, "Palau, which hosted the world's first live underwater interview in October 2025, is an archipelago located east of which country?",
     "Australia", "Japan", "Philippines", "Indonesia",
     "C", "Palau is an archipelago of around 340 islands located east of the Philippines in the Pacific Ocean. President Surangel Whipps Jr conducted the world's first live underwater interview to raise ocean protection awareness.",
     "General_Science", "National_Current_Affairs"),

    (29063, "OmanSat-1, Oman's first communications satellite, was developed in partnership with which company?",
     "Boeing Space", "SpaceX", "Airbus Defence and Space", "ISRO",
     "C", "OmanSat-1 was developed in partnership with Airbus Defence and Space, built on Airbus' OneSat platform. It will operate in the Ka frequency band covering Oman, Middle East, East Africa, and Asia.",
     "General_Science", "National_Current_Affairs"),

    (29064, "The Dorjilung Hydroelectric Power Project (1,125 MW) signed between Tata Power and DGPC (Druk Green Power Corporation) is located in which country?",
     "Nepal", "Bangladesh", "Bhutan", "Myanmar",
     "C", "The Dorjilung Hydroelectric Power Project (1,125 MW) is located in Lhuentse and Mongar districts of Bhutan on the Kurichhu River. It will be Bhutan's 2nd-largest hydropower project. World Bank is financing it.",
     "General_Science", "National_Current_Affairs"),

    (29065, "West Seti Hydropower Project (750 MW) is located on which river in Nepal?",
     "Karnali River", "Gandaki River", "Seti River", "Koshi River",
     "C", "The West Seti Hydropower Project is a 750 MW storage-based hydroelectric project on the Seti River (a tributary of the Karnali) in Nepal. It is being developed by NHPC (India) under a PPP model.",
     "General_Science", "National_Current_Affairs"),

    (29066, "The India-China rapprochement in 2025 included restoring several bilateral ties. Which of the following was NOT resumed as part of this rapprochement?",
     "Kailash Mansarovar Yatra", "Direct flights between India and China", "BCIM Economic Corridor project", "Water-data sharing on rivers",
     "C", "The BCIM (Bangladesh-China-India-Myanmar) Economic Corridor project was NOT resumed. India-China restored: Kailash Mansarovar Yatra, direct flights, visas, and water-data sharing (Brahmaputra river data).",
     "General_Science", "National_Current_Affairs"),

    (29067, "LeadIT 2.0, launched at COP28, focuses on inclusive transition for which type of industries?",
     "Agriculture and farming", "Mining and extraction", "Heavy industries (steel, cement, chemicals)", "Digital and IT sector",
     "C", "LeadIT targets net-zero emissions from heavy industries (like steel, cement, and chemicals) by 2050. LeadIT 2.0 (launched at COP28) focuses on inclusive transition, low-carbon technology transfer, and financial support for emerging economies.",
     "General_Science", "National_Current_Affairs"),

    (29068, "Which African country launched a five-year (2025-2029) livestock vaccination drive targeting cattle, goats, sheep, and chickens to curb zoonotic diseases?",
     "Nigeria", "Kenya", "Tanzania", "Ethiopia",
     "C", "Tanzania launched a nationwide 5-year livestock vaccination campaign (2025-2029) targeting 19 million cattle, 17 million goats and sheep, and 40 million chickens. Tanzania has 36.6 million cattle — 2nd largest in Africa.",
     "General_Science", "National_Current_Affairs"),

    (29069, "Trump's 'Liberation Day' (April 2, 2025) referred to the announcement of:",
     "US withdrawal from NATO", "Reciprocal tariffs on imports", "US sanctions on China", "US withdrawal from WTO",
     "B", "US President Donald Trump called April 2, 2025 'Liberation Day' when he announced sweeping reciprocal tariffs on imports from countries worldwide, significantly affecting global trade.",
     "General_Science", "National_Current_Affairs"),

    (29070, "Muhammad Yunus, who heads Bangladesh's interim government, is associated with which field?",
     "Military and defence", "Micro-finance and economics (Nobel laureate)", "Medicine and public health", "Law and judiciary",
     "B", "Muhammad Yunus is a Nobel Peace Prize laureate (2006) known for pioneering micro-finance through Grameen Bank. He was invited to head Bangladesh's interim government after Sheikh Hasina fled in August 2024.",
     "General_Science", "National_Current_Affairs"),

    # ── More miscellaneous ──
    (29071, "Ahmed al-Sharaa, who leads Syria's interim government after Assad's fall, was previously known by what nom de guerre?",
     "Abu Bakr al-Baghdadi", "Abu Mohammad al-Jolani", "Abu Ibrahim al-Hashimi", "Abu Umar al-Shami",
     "B", "Ahmed al-Sharaa is the real name of Abu Mohammad al-Jolani, the HTS leader who led the rebel coalition that captured Damascus on December 8, 2024, ending Assad's rule.",
     "General_Science", "National_Current_Affairs"),

    (29072, "India hosted the 89th General Meeting of IEC at Bharat Mandapam in New Delhi. How many times had India hosted this meeting before?",
     "Once (1997)", "Twice (1960, 1997)", "Three times (1960, 1997, 2013)", "Four times (1960, 1980, 1997, 2013)",
     "C", "India hosted the IEC General Meeting three times before: 1960, 1997, and 2013. The 2025 hosting at Bharat Mandapam was the 4th time India hosted the IEC General Meeting.",
     "General_Science", "National_Current_Affairs"),

    (29073, "MERCOSUR's original founding member countries included all EXCEPT:",
     "Argentina", "Chile", "Brazil", "Uruguay",
     "B", "MERCOSUR's original founding members (1991 Treaty of Asunción) are Argentina, Brazil, Paraguay, and Uruguay. Chile is only an associate member, not a founding member.",
     "General_Science", "National_Current_Affairs"),

    (29074, "The Interpol Asian Committee meets annually to guide coordinated action on regional security. India was elected to this committee at the 25th Asian Regional Conference in which city?",
     "Tokyo, Japan", "Bangkok, Thailand", "Singapore", "Kuala Lumpur, Malaysia",
     "C", "India was elected to the Interpol Asian Committee at the 25th Asian Regional Conference held in Singapore. The CBI represented India at this conference.",
     "General_Science", "National_Current_Affairs"),

    (29075, "Which country's President declared martial law in December 2024 and was subsequently impeached by the National Assembly?",
     "Taiwan", "Thailand", "South Korea", "Myanmar",
     "C", "South Korean President Yoon Suk-yeol declared martial law on December 3, 2024. The National Assembly voted to impeach him on December 14, 2024. The Constitutional Court upheld the impeachment on April 4, 2025.",
     "General_Science", "National_Current_Affairs"),

    (29076, "To Lam became the new General Secretary of which country's Communist Party in 2024, after Nguyen Phu Trong passed away?",
     "China", "Laos", "Vietnam", "Cambodia",
     "C", "To Lam became Vietnam's Communist Party General Secretary in 2024, succeeding Nguyen Phu Trong who died in July 2024. Vietnam has a single-party political system led by the Communist Party.",
     "General_Science", "National_Current_Affairs"),

    (29077, "The Pahalgam terrorist attack on April 22, 2025, in which 26 tourists were killed, occurred in which Indian Union Territory?",
     "Jammu & Kashmir", "Ladakh", "Himachal Pradesh", "Uttarakhand",
     "A", "The Pahalgam terrorist attack occurred in the Baisaran meadow near Pahalgam in Jammu & Kashmir on April 22, 2025. 26 tourists were killed, which prompted India to launch Operation Sindoor on May 7, 2025.",
     "General_Science", "National_Current_Affairs"),

    (29078, "The Central American Integration System (SICA) was established by amending the Charter of which earlier organisation?",
     "CELAC", "ODECA (Organization of Central American States)", "CACM", "PARLACEN",
     "B", "SICA was established in 1991 by the Tegucigalpa Protocol which amended the Charter of ODECA (Organization of Central American States), originally founded in 1962.",
     "General_Science", "National_Current_Affairs"),

    (29079, "Pope Leo XIV (Robert Francis Prevost), the first American pope, previously served as bishop in which country?",
     "Brazil", "Mexico", "Argentina", "Peru",
     "D", "Before becoming Pope Leo XIV, Robert Francis Prevost (born in Chicago, USA) served as a bishop in Peru. He is also the first Augustinian to become pope.",
     "General_Science", "National_Current_Affairs"),

    (29080, "The EU's CBAM (Carbon Border Adjustment Mechanism) was in its transitional phase from 2023 to 2025. When does full enforcement begin?",
     "2025", "2026", "2027", "2028",
     "B", "CBAM full enforcement begins in 2026 (transitional phase was 2023-2025). It is part of the EU's 'Fit for 55' strategy targeting 55% GHG reduction by 2030. India has expressed deep reservations about CBAM.",
     "General_Science", "National_Current_Affairs"),
]


def seed():
    conn = get_conn()
    if USE_POSTGRES:
        cur_chk = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    else:
        cur_chk = conn.cursor()

    cur_chk.execute("SELECT COUNT(*) FROM questions WHERE id >= 29001 AND id <= 29080")
    existing = _fv(cur_chk.fetchone())
    if existing >= 75:
        print(f"[seed_intl_events_mcq] {existing}/80 questions already present — skipping.")
        conn.close()
        return

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
            print(f"[seed_intl_events_mcq] Skipping ID {q[0]}: {e}")
            try:
                conn.rollback()
            except:
                pass

    conn.commit()
    print(f"[seed_intl_events_mcq] Inserted {inserted}/{len(QUESTIONS)} questions (IDs 29001–29080).")
    conn.close()


if __name__ == '__main__':
    seed()
