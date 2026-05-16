"""
Seed: Israel–Iran–America War 2025–2026 MCQs
IDs 30001–30080 | Topic: National_Current_Affairs
Covers: Twelve-Day War (June 2025) + 2026 Iran War (Feb 28, 2026 – present)
Run standalone: python seed_mideast_war_mcq.py
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
    # ══════════════════════════════════════════
    # SECTION A: THE TWELVE-DAY WAR (JUNE 2025)
    # ══════════════════════════════════════════

    (30001, "The Twelve-Day War between Israel and Iran lasted from:",
     "June 1–12, 2025", "June 13–24, 2025", "June 20–July 1, 2025", "July 4–15, 2025",
     "B", "The Twelve-Day War lasted from June 13 to June 24, 2025. It began when Israel launched a surprise attack on Iran's nuclear and military facilities and ended with a ceasefire brokered under US pressure.",
     "AP_HC", "International_Current_Affairs"),

    (30002, "Which country launched the surprise attack that started the Twelve-Day War in June 2025?",
     "United States", "Israel", "Saudi Arabia", "UK",
     "B", "Israel launched the surprise attack on June 13, 2025, targeting Iran's nuclear facilities (Natanz, Isfahan, Fordow), military bases, and assassinating key IRGC generals and nuclear scientists.",
     "AP_HC", "International_Current_Affairs"),

    (30003, "Which three Iranian nuclear facilities were targeted during the Twelve-Day War?",
     "Arak, Qom, Bushehr", "Natanz, Isfahan, Fordow", "Parchin, Saghand, Gachin", "Tehran, Tabriz, Shiraz",
     "B", "Israel (and later the US on June 22) targeted Iran's key nuclear facilities: Natanz (main enrichment plant), Isfahan (research centre), and Fordow (underground plant near Qom). All three were extensively damaged.",
     "AP_HC", "International_Current_Affairs"),

    (30004, "What was Iran's retaliatory operation name during the Twelve-Day War against Israel?",
     "Operation True Promise I", "Operation True Promise II", "Operation True Promise III", "Operation Iron Sword",
     "C", "Iran's retaliation in the Twelve-Day War was called 'Operation True Promise III' — involving 550+ ballistic missiles and 1,000+ suicide drones targeting Israeli cities, military bases, energy infrastructure, and government sites.",
     "AP_HC", "International_Current_Affairs"),

    (30005, "How many ballistic missiles did Iran fire during the Twelve-Day War?",
     "150+", "350+", "550+", "900+",
     "C", "Iran retaliated with over 550 ballistic missiles and over 1,000 suicide drones during the Twelve-Day War (June 2025), hitting civilian population centres, hospitals, and military/energy/government sites in Israel.",
     "AP_HC", "International_Current_Affairs"),

    (30006, "On which date did the United States directly bomb Iranian nuclear sites during the Twelve-Day War?",
     "June 15, 2025", "June 18, 2025", "June 22, 2025", "June 24, 2025",
     "C", "The United States bombed three Iranian nuclear sites (Natanz, Isfahan, Fordow) on June 22, 2025, during the Twelve-Day War. Iran then retaliated by firing missiles at the US military base Al Udeid in Qatar.",
     "AP_HC", "International_Current_Affairs"),

    (30007, "After the US bombed its nuclear sites on June 22, 2025, Iran retaliated by striking which US military base?",
     "Incirlik Air Base, Turkey", "Diego Garcia, Indian Ocean", "Al Udeid Air Base, Qatar", "Camp Arifjan, Kuwait",
     "C", "Iran fired missiles at Al Udeid Air Base in Qatar — the largest US military base in the Middle East — in retaliation for the US strikes on its nuclear facilities on June 22, 2025.",
     "AP_HC", "International_Current_Affairs"),

    (30008, "Which IRGC commander (Chief of IRGC) was killed during the Twelve-Day War?",
     "Qasem Soleimani", "Hossein Salami", "Yahya Rahim Safavi", "Mohammad Jafari",
     "B", "Hossein Salami, the Commander-in-Chief of the IRGC (Islamic Revolutionary Guard Corps), was killed during Israel's attacks in the Twelve-Day War (June 2025).",
     "AP_HC", "International_Current_Affairs"),

    (30009, "Which head of Iran's IRGC Aerospace Force was killed in the Twelve-Day War?",
     "Esmail Qaani", "Ali Fadavi", "Amir Ali Hajizadeh", "Mohammad Pakpour",
     "C", "Amir Ali Hajizadeh, Commander of the IRGC Aerospace Force (responsible for Iran's missile and drone programme), was killed during Israel's strikes in the Twelve-Day War.",
     "AP_HC", "International_Current_Affairs"),

    (30010, "Iran's Chief of Staff of the Armed Forces, killed in the Twelve-Day War, was:",
     "Abdolrahim Mousavi", "Mohammad Bagheri", "Yahya Rahim Safavi", "Gholam Ali Rashid",
     "B", "Mohammad Bagheri, Chief of Staff of Iran's Armed Forces, was killed during Israel's attacks in the Twelve-Day War (June 2025). Gholam Ali Rashid (another senior general) was also killed.",
     "AP_HC", "International_Current_Affairs"),

    (30011, "How many leading Iranian nuclear scientists did Israel assassinate during the Twelve-Day War?",
     "At least 3", "At least 5", "At least 10", "At least 20",
     "C", "Israel assassinated at least 10 leading Iranian nuclear scientists during the Twelve-Day War, using commandos and Mossad operatives inside Iran.",
     "AP_HC", "International_Current_Affairs"),

    (30012, "What happened to Iran's President Masoud Pezeshkian during the Twelve-Day War?",
     "He was killed in an Israeli airstrike", "He was arrested", "He was wounded in action (WIA)", "He fled the country",
     "C", "Iranian President Masoud Pezeshkian was wounded in action (WIA) during the Twelve-Day War (June 2025). He had been elected President in mid-2024 after Ebrahim Raisi's death.",
     "AP_HC", "International_Current_Affairs"),

    (30013, "On the day before the Twelve-Day War, the IAEA declared Iran non-compliant with nuclear obligations. This resolution was put forward by which four countries?",
     "USA, UK, France, Russia", "USA, UK, France, Germany", "USA, Israel, UK, Germany", "USA, France, China, Russia",
     "B", "On June 12, 2025 (the day before Israel attacked), the IAEA Board passed a resolution declaring Iran non-compliant with its nuclear obligations. The resolution was put forward by USA, UK, France, and Germany (the E3+US group).",
     "AP_HC", "International_Current_Affairs"),

    (30014, "After the Twelve-Day War, Iran took which major step regarding its nuclear oversight?",
     "Invited IAEA for full inspection", "Signed new nuclear deal with Russia", "Suspended cooperation with the IAEA", "Transferred nuclear materials to Syria",
     "C", "Iran suspended cooperation with the IAEA after the Twelve-Day War, accusing the agency of sharing information about nuclear facility locations with Israel, which Iran said enabled the targeted strikes.",
     "AP_HC", "International_Current_Affairs"),

    (30015, "How many Mossad (Israeli intelligence) agents did Iran claim to arrest during the Twelve-Day War?",
     "200+", "400+", "700+", "1,000+",
     "C", "Iran claimed to have arrested over 700 Mossad agents during the Twelve-Day War, and reportedly executed 5 of them. Israel's Mossad was credited with intelligence and commando operations inside Iran.",
     "AP_HC", "International_Current_Affairs"),

    (30016, "Israeli civilian casualties in the Twelve-Day War were:",
     "5 civilians killed, 500 wounded", "32 civilians + 1 soldier killed, 3,238 wounded", "120 civilians killed, 8,000 wounded", "200 civilians killed",
     "B", "Israel suffered 32 civilians and 1 off-duty soldier killed, with 3,238 wounded in the Twelve-Day War. Iran's retaliation with 550+ missiles and 1,000+ drones targeted Israeli cities.",
     "AP_HC", "International_Current_Affairs"),

    (30017, "The ceasefire that ended the Twelve-Day War on June 24, 2025 was brokered by:",
     "United Nations", "Qatar and Egypt", "USA (under US pressure)", "Pakistan",
     "C", "The ceasefire on June 24, 2025 was agreed under US pressure. The US played the role of both a combatant (bombing nuclear sites on June 22) and ceasefire broker — a unique dual role in this conflict.",
     "AP_HC", "International_Current_Affairs"),

    (30018, "During the Twelve-Day War, Iran imposed an internet blackout. The Iranian government did this primarily to:",
     "Protect government networks from Israeli cyber attacks", "Prevent protests from spreading and restrict flow of information", "Save bandwidth for military communications", "Block Israeli propaganda",
     "B", "The Iranian government imposed internet blackouts during the Twelve-Day War to prevent protests from spreading and to restrict the flow of information about casualties and military losses to both domestic and international audiences.",
     "AP_HC", "International_Current_Affairs"),

    (30019, "Which Iranian aircraft were destroyed by Israel during the Twelve-Day War?",
     "MiG-29s and Su-27s", "F-14 Tomcats and F-5 Tigers", "F-4 Phantoms and Mirage jets", "Su-35s and MiG-31s",
     "B", "Israel destroyed 5 F-14 Tomcat fighter jets, 2 F-5 Tiger jets, and 8 AH-1 Cobra helicopters belonging to Iran during the Twelve-Day War. Iran's F-14s are American-era jets supplied before the 1979 revolution.",
     "AP_HC", "International_Current_Affairs"),

    (30020, "The Fordow nuclear plant in Iran is significant because it is:",
     "Located near Tehran, Iran's largest city", "Built underground inside a mountain near Qom", "A light water reactor given by Russia", "A plutonium reprocessing facility near the sea",
     "B", "The Fordow Fuel Enrichment Plant is located underground inside a mountain near Qom, making it extremely hardened and difficult to destroy from the air. Despite this, US strikes on June 22, 2025 damaged it.",
     "AP_HC", "International_Current_Affairs"),

    # ══════════════════════════════════════════
    # SECTION B: THE 2026 IRAN WAR
    # ══════════════════════════════════════════

    (30021, "The 2026 Iran War officially began on:",
     "January 15, 2026", "February 28, 2026", "March 15, 2026", "April 1, 2026",
     "B", "The 2026 Iran War began on February 28, 2026, when the United States and Israel launched coordinated airstrikes on Iran, targeting military and government sites. The surprise attacks were launched while US-Iran nuclear negotiations were ongoing.",
     "AP_HC", "International_Current_Affairs"),

    (30022, "The 2026 Iran War attacks by the USA and Israel were launched while what diplomatic activity was in progress?",
     "UN Security Council emergency meeting on Iran", "US-Iran nuclear negotiations (indirect talks)", "JCPOA re-signing ceremony", "IAEA inspection of Natanz",
     "B", "The US-Israel attacks on February 28, 2026 were launched as a surprise during ongoing US-Iran nuclear negotiations — a diplomatic deception that shocked the international community.",
     "AP_HC", "International_Current_Affairs"),

    (30023, "Which major Iranian leader was killed in the US-Israel airstrikes during the 2026 Iran War?",
     "Masoud Pezeshkian (President)", "Mojtaba Khamenei (Supreme Leader's son)", "Ali Khamenei (Supreme Leader)", "Naim Qassem (Hezbollah)",
     "C", "Ali Khamenei, Iran's Supreme Leader since 1989, was killed in the US-Israel strikes during the 2026 Iran War. He had been Supreme Leader for over 35 years since succeeding Ayatollah Khomeini.",
     "AP_HC", "International_Current_Affairs"),

    (30024, "Ali Larijani, killed in the 2026 Iran War, was notable as:",
     "Iran's IRGC Navy Commander", "Iran's Foreign Minister", "Former Speaker of Iran's Parliament and senior official", "Iran's nuclear chief",
     "C", "Ali Larijani, killed during the 2026 Iran War, was a highly influential Iranian politician — former Speaker of the Islamic Consultative Assembly (Parliament) and a senior advisor to the Supreme Leader.",
     "AP_HC", "International_Current_Affairs"),

    (30025, "In response to the 2026 US-Israel attacks, Iran closed which critical global waterway?",
     "Suez Canal", "Strait of Malacca", "Bab-el-Mandeb Strait", "Strait of Hormuz",
     "D", "Iran closed the Strait of Hormuz in retaliation for the US-Israel attacks. This triggered the '2026 Strait of Hormuz Crisis'. Approximately 20% of global oil trade passes through this narrow strait between Iran and Oman.",
     "AP_HC", "International_Current_Affairs"),

    (30026, "The Strait of Hormuz, which Iran closed in 2026, lies between Iran and which country on the opposite shore?",
     "UAE", "Oman", "Qatar", "Bahrain",
     "B", "The Strait of Hormuz is a narrow waterway between Iran (to the north) and Oman (to the south). It is the world's most important oil chokepoint — about 20% of global oil and 30% of global LNG passes through it.",
     "AP_HC", "International_Current_Affairs"),

    (30027, "During the 2026 Iran War, Iran fired missiles and drones at US military bases in multiple Arab countries. Which of the following was NOT among those countries?",
     "Bahrain", "Kuwait", "Egypt", "Saudi Arabia",
     "C", "Iran targeted US military bases in Bahrain, Jordan, Kuwait, Qatar, Saudi Arabia, and UAE. Egypt was NOT targeted — it does not host a major US military base targeted in this conflict.",
     "AP_HC", "International_Current_Affairs"),

    (30028, "Britain's military base struck by an Iranian drone during the 2026 Iran War is located on which island?",
     "Malta", "Cyprus", "Crete", "Sardinia",
     "B", "Britain's Akrotiri military base on Cyprus was struck by an Iranian drone during the 2026 Iran War. The UK Sovereign Base Areas of Akrotiri and Dhekelia are located on the island of Cyprus.",
     "AP_HC", "International_Current_Affairs"),

    (30029, "Iranian missiles fired during the 2026 war were intercepted over which NATO country?",
     "Greece", "Romania", "Turkey", "Poland",
     "C", "Iranian ballistic missiles were intercepted over Turkey during the 2026 Iran War. Turkey, a NATO member, cooperated with allied air defences to intercept the missiles despite not being a direct participant in the war.",
     "AP_HC", "International_Current_Affairs"),

    (30030, "How many US soldiers were killed in the 2026 Iran War (as of April 30, 2026)?",
     "5", "10", "15", "25",
     "C", "15 US soldiers were killed in the 2026 Iran War (as of April 30, 2026 report), with 538 military personnel wounded. The US also had 17+ military sites damaged.",
     "AP_HC", "International_Current_Affairs"),

    (30031, "Israel's economic damage from the 2026 Iran War was estimated at approximately:",
     "$5 billion", "$20 billion", "$50 billion", "$100 billion",
     "C", "Israel's economic damage from the 2026 Iran War was estimated at approximately $50 billion as of April 30, 2026. Israel suffered 18 soldiers and 28 civilians killed, with 8,524 injured.",
     "AP_HC", "International_Current_Affairs"),

    (30032, "According to HRANA (Human Rights Activists News Agency), how many people were killed in Iran in the 2026 Iran War?",
     "1,250 killed", "2,100 killed", "3,636 killed", "5,500 killed",
     "C", "HRANA reported 3,636 killed in Iran (1,221 military personnel, 1,701 civilians, and 714 unclassified) with 26,500 injured, as of the April 30, 2026 report.",
     "AP_HC", "International_Current_Affairs"),

    (30033, "How many Iranian ballistic missile launchers were destroyed in the 2026 Iran War (per US and Israel)?",
     "50+", "100+", "190+", "300+",
     "C", "According to US and Israel, 190+ ballistic missile launchers were destroyed in the 2026 Iran War, along with 155 naval vessels destroyed or damaged. Iran also lost 6,000+ military personnel per US-Israel estimates.",
     "AP_HC", "International_Current_Affairs"),

    (30034, "Who mediated the conditional ceasefire announced on April 8, 2026, in the Iran War?",
     "Turkey", "Qatar", "Pakistan", "Oman",
     "C", "Pakistan mediated the conditional ceasefire declared on April 8, 2026 between the conflicting parties. Despite the ceasefire, both sides continued small-scale attacks on each other.",
     "AP_HC", "International_Current_Affairs"),

    (30035, "The 2026 Lebanon War was a direct consequence of the 2026 Iran War. How many civilians and militants were killed in Lebanon?",
     "500+", "1,000+", "2,000+", "5,000+",
     "B", "The 2026 Lebanon War (escalation of Hezbollah-Israel conflict) killed more than 2,000 civilians and militants. Hezbollah alone lost 1,000–1,900 fighters in this phase of the conflict.",
     "AP_HC", "International_Current_Affairs"),

    (30036, "Which event on May 7, 2026 showed the ceasefire of April 8 was fragile?",
     "Iran fired missiles at Tel Aviv", "Israel struck Beirut, killing an alleged Hezbollah leader", "USA bombed Fordow again", "Iran closed Hormuz again",
     "B", "On May 7, 2026 — despite the April 8 conditional ceasefire — Israel conducted a large strike on Beirut, targeting and killing an alleged Hezbollah leader. This showed the ceasefire was conditional and fragile.",
     "AP_HC", "International_Current_Affairs"),

    (30037, "US Defense Secretary during the 2026 Iran War was:",
     "Lloyd Austin", "Mark Esper", "Pete Hegseth", "James Mattis",
     "C", "Pete Hegseth served as US Secretary of Defense during the 2026 Iran War, under President Donald Trump's second administration. He was a former Fox News host who was controversially appointed to the role.",
     "AP_HC", "International_Current_Affairs"),

    (30038, "The 2026 US military buildup in the Middle East was described as the largest since which earlier conflict?",
     "Gulf War (1991)", "Afghanistan War (2001)", "2003 US invasion of Iraq", "Libya intervention (2011)",
     "C", "The Trump administration launched the largest US military buildup in the Middle East since the 2003 US-led invasion of Iraq, including deploying two aircraft carrier strike groups to the region.",
     "AP_HC", "International_Current_Affairs"),

    (30039, "How many aircraft carrier strike groups did the US deploy to the Middle East for the 2026 Iran War?",
     "One", "Two", "Three", "Four",
     "B", "The US deployed two aircraft carrier strike groups to the Middle East as part of the largest military buildup in the region since 2003. This massive naval force, combined with the Israeli Air Force, conducted the sustained strikes.",
     "AP_HC", "International_Current_Affairs"),

    (30040, "Iran's Supreme Leader Ali Khamenei had been in power since which year before being killed in the 2026 war?",
     "1979", "1981", "1989", "1997",
     "C", "Ali Khamenei became Supreme Leader of Iran in 1989, succeeding Ayatollah Khomeini who died that year. He held the position for over 35 years until his assassination in the 2026 Iran War.",
     "AP_HC", "International_Current_Affairs"),

    (30041, "Which son of Ali Khamenei was wounded (WIA) in the 2026 Iran War?",
     "Mojtaba Khamenei", "Mujtada Khamenei", "Mustafa Khamenei", "Mahmoud Khamenei",
     "A", "Mojtaba Khamenei, the son of Supreme Leader Ali Khamenei, was wounded in action (WIA) during the 2026 Iran War. He had been rumoured as a potential successor to his father before the war.",
     "AP_HC", "International_Current_Affairs"),

    (30042, "The Hezbollah Secretary General who led the organisation during the 2026 Lebanon War (after Hassan Nasrallah's death in 2024) was:",
     "Imad Mughniyeh", "Hashem Safieddine", "Naim Qassem", "Ibrahim Aqil",
     "C", "Naim Qassem became Hezbollah's Secretary General after Hassan Nasrallah was killed by Israel in September 2024. Qassem led Hezbollah during the 2026 Lebanon War phase of the Iran-Israel conflict.",
     "AP_HC", "International_Current_Affairs"),

    # ══════════════════════════════════════════
    # SECTION C: BACKGROUND & CONTEXT
    # ══════════════════════════════════════════

    (30043, "The JCPOA (Joint Comprehensive Plan of Action), Iran's 2015 nuclear deal, was agreed between Iran and the group known as P5+1. Which countries comprise P5+1?",
     "USA, UK, France, Russia, China + Germany", "G7 countries minus Japan", "USA, UK, France, Israel, Russia, China", "UN Security Council members + Australia",
     "A", "P5+1 = Five permanent members of the UN Security Council (USA, UK, France, Russia, China) + Germany. The JCPOA was signed in 2015 — Iran froze its nuclear program in exchange for sanctions relief.",
     "AP_HC", "International_Current_Affairs"),

    (30044, "In which year did the USA unilaterally withdraw from the JCPOA nuclear deal?",
     "2017", "2018", "2019", "2020",
     "B", "US President Donald Trump unilaterally withdrew the US from the JCPOA on May 8, 2018 (his first term). Iran then resumed uranium enrichment, gradually raising it toward weapons-grade levels.",
     "AP_HC", "International_Current_Affairs"),

    (30045, "Israel bombed the Iranian consulate in Damascus (Syria) in April 2024, killing senior IRGC officials. This was located in which part of Damascus?",
     "Iranian Embassy compound", "Consulate annexe near the embassy", "IRGC command centre in suburbs", "Syrian Defence Ministry building",
     "B", "Israel bombed the Iranian consulate annexe adjacent to the Iranian Embassy in Damascus, Syria in April 2024. The strike killed several senior IRGC officers including General Mohammad Reza Zahedi.",
     "AP_HC", "International_Current_Affairs"),

    (30046, "Iran's first-ever direct missile and drone attack on Israel (April 13–14, 2024) was called:",
     "Operation True Promise I", "Operation Al-Aqsa Flood", "Operation Iron Fist", "Operation True Promise II",
     "A", "Iran's first direct attack on Israel (April 13–14, 2024) was called 'Operation True Promise I'. It involved approximately 300 drones and missiles, most of which were intercepted by Israel, US, UK, France, and Jordan.",
     "AP_HC", "International_Current_Affairs"),

    (30047, "What percentage of Iran's uranium enrichment level had Iran reached before the wars began (as of 2024-25)?",
     "20%", "40%", "60%", "90%",
     "C", "Iran had enriched uranium to approximately 60% purity before the wars — just below the 90%+ threshold for weapons-grade uranium. This was far beyond the 3.67% limit under the JCPOA.",
     "AP_HC", "International_Current_Affairs"),

    (30048, "The 2026 Iran War was launched DURING which specific diplomatic activity?",
     "IAEA Board of Governors meeting in Vienna", "US-Iran nuclear negotiations", "G20 emergency summit on Middle East", "UN-sponsored Gaza peace talks",
     "B", "The February 28, 2026 US-Israel attacks were launched as a surprise DURING ongoing negotiations between Iran and the US on Iran's nuclear program. The timing shocked the international community.",
     "AP_HC", "International_Current_Affairs"),

    (30049, "The January 2026 Iranian protests, which saw security forces massacre thousands of civilians, were the largest in Iran since:",
     "The Green Movement (2009)", "Mahsa Amini protests (2022)", "1979 Islamic Revolution", "Iran-Iraq War (1980-88)",
     "C", "The 2025-2026 Iranian protests were described as the largest in Iran since the 1979 Islamic Revolution. The crackdown in January 2026 (with thousands of civilians killed) triggered US President Trump to threaten military action.",
     "AP_HC", "International_Current_Affairs"),

    (30050, "Which IRGC general, commander of Quds Force (overseeing proxy wars), was killed by the US in a drone strike in Baghdad in January 2020?",
     "Hossein Salami", "Amir Ali Hajizadeh", "Qasem Soleimani", "Esmail Qaani",
     "C", "Qasem Soleimani, head of the IRGC Quds Force and architect of Iran's proxy strategy across the Middle East, was killed in a US drone strike at Baghdad International Airport on January 3, 2020. Esmail Qaani succeeded him.",
     "AP_HC", "International_Current_Affairs"),

    # ══════════════════════════════════════════
    # SECTION D: KEY FIGURES, WEAPONS & ORGS
    # ══════════════════════════════════════════

    (30051, "The IRGC (Islamic Revolutionary Guard Corps) is Iran's elite military force. Which of the following is NOT an IRGC component?",
     "IRGC Ground Forces", "IRGC Aerospace Force (missiles/drones)", "IRGC Quds Force (foreign ops)", "IRGC Naval Aviation Wing",
     "D", "The IRGC has Ground Forces, Aerospace Force (missiles and drones), Naval Force, and Quds Force (overseas operations). 'IRGC Naval Aviation Wing' is not a standard component — the IRGC has a naval force but aviation falls under Aerospace.",
     "AP_HC", "International_Current_Affairs"),

    (30052, "Iran's 'Axis of Resistance' is a network of Iran-backed proxy groups. Which of the following is NOT part of the Axis of Resistance?",
     "Hezbollah (Lebanon)", "Hamas (Gaza)", "Houthis (Yemen)", "Muslim Brotherhood (Egypt)",
     "D", "The Axis of Resistance includes Hezbollah (Lebanon), Hamas (Gaza), Houthis (Yemen), and Popular Mobilization Forces/Islamic Resistance in Iraq. The Muslim Brotherhood in Egypt is NOT part of this axis.",
     "AP_HC", "International_Current_Affairs"),

    (30053, "Iran's primary suicide drone (loitering munition) used against Israel and in the Twelve-Day War is known as:",
     "Bayraktar TB2", "Shahed-136", "Mohajer-6", "Ababil-3",
     "B", "The Shahed-136 (also called Geran-2 when used by Russia) is Iran's primary kamikaze/loitering munition drone. Iran used thousands of Shahed-series drones in operations against Israel. Russia also used Shaheds against Ukraine.",
     "AP_HC", "International_Current_Affairs"),

    (30054, "Hassan Nasrallah, the long-time Hezbollah Secretary General, was killed by Israel in which month and year?",
     "July 2024", "September 2024", "November 2024", "January 2025",
     "B", "Hezbollah Secretary General Hassan Nasrallah was killed by Israel in September 2024 in a massive airstrike on Hezbollah's headquarters in Beirut's southern suburbs. Naim Qassem succeeded him.",
     "AP_HC", "International_Current_Affairs"),

    (30055, "Israel's Iron Dome, David's Sling, and Arrow systems together form Israel's multi-tier missile defence. Which system is designed to intercept long-range ballistic missiles?",
     "Iron Dome", "David's Sling", "Arrow (Hetz)", "Trophy (APS)",
     "C", "The Arrow (Hetz) system is Israel's upper-tier defence against long-range ballistic missiles. Iron Dome handles short-range rockets; David's Sling handles medium-range missiles. All were used during Iran's attacks.",
     "AP_HC", "International_Current_Affairs"),

    (30056, "The Houthis, who attacked Israel and US shipping in the Twelve-Day War period, operate from which country?",
     "Iraq", "Syria", "Yemen", "Libya",
     "C", "The Houthis (officially Ansar Allah) control northern Yemen including the capital Sanaa. They are backed by Iran and attacked Israel with drones and missiles during the conflict, and targeted shipping in the Red Sea.",
     "AP_HC", "International_Current_Affairs"),

    (30057, "Popular Mobilization Forces (PMF), also called Hashd al-Shaabi, who fought alongside Iran in the 2026 war, are based in:",
     "Syria", "Lebanon", "Iraq", "Yemen",
     "C", "The Popular Mobilization Forces (PMF/Hashd al-Shaabi) are Iran-backed Shia militia groups based in Iraq. They are part of Iran's Axis of Resistance and attacked US bases in Iraq and across the region.",
     "AP_HC", "International_Current_Affairs"),

    (30058, "The US military's main base in Qatar, targeted by Iran in the Twelve-Day War, is:",
     "Camp Arifjan", "Al Dhafra Air Base", "Al Udeid Air Base", "NSA Bahrain",
     "C", "Al Udeid Air Base in Qatar is the largest US military base in the Middle East, hosting approximately 10,000+ US military personnel and a major forward command centre. Iran fired missiles at it after the US struck its nuclear sites.",
     "AP_HC", "International_Current_Affairs"),

    (30059, "Israel's military intelligence agency (the 'Institute for Intelligence and Special Operations') which ran operations inside Iran during the Twelve-Day War is called:",
     "Shin Bet", "Aman", "Mossad", "Unit 8200",
     "C", "Mossad is Israel's national intelligence agency responsible for foreign intelligence and covert operations. During the Twelve-Day War, Mossad ran covert operations inside Iran, including assassinating nuclear scientists.",
     "AP_HC", "International_Current_Affairs"),

    (30060, "The Natanz Nuclear Facility in Iran is primarily known as:",
     "Iran's only light-water reactor (power generation)", "Iran's main uranium enrichment plant", "Iran's plutonium reprocessing facility", "Iran's nuclear weapons assembly site",
     "B", "The Natanz Fuel Enrichment Plant is Iran's main uranium enrichment facility, located in Isfahan Province. It contains both above-ground and underground cascades of centrifuges and was the primary target in multiple strikes.",
     "AP_HC", "International_Current_Affairs"),

    # ══════════════════════════════════════════
    # SECTION E: INDIA & GLOBAL IMPACT
    # ══════════════════════════════════════════

    (30061, "India's External Affairs Minister met Iranian FM Seyyed Abbas Araghchi on May 15, 2026 in New Delhi for bilateral discussions. India's EAM is:",
     "Rajnath Singh", "Amit Shah", "S. Jaishankar", "Subrahmanyam Jaishankar",
     "C", "S. Jaishankar (Dr. Subrahmanyam Jaishankar) is India's External Affairs Minister. He held a bilateral meeting with Iranian Foreign Minister Seyyed Abbas Araghchi in New Delhi on May 15, 2026.",
     "AP_HC", "International_Current_Affairs"),

    (30062, "The Iran-Israel war directly impacted India due to the closure of the Strait of Hormuz because India:",
     "Has a military base in Oman near the Strait", "Imports significant quantities of oil and LNG from the Gulf", "Exports goods to Iran through the Strait", "Runs the Chabahar-Zahedan railway through the Strait",
     "B", "India imports a significant portion of its crude oil from Gulf countries (UAE, Saudi Arabia, Iraq, Kuwait) — most of which passes through the Strait of Hormuz. The 2026 closure severely impacted India's energy imports.",
     "AP_HC", "International_Current_Affairs"),

    (30063, "Chabahar Port, developed by India in Iran, is strategically important because it:",
     "Allows India to access the Strait of Hormuz directly", "Provides India access to Afghanistan and Central Asia bypassing Pakistan", "Is Iran's main oil export terminal", "Is the eastern terminal of the North-South Transport Corridor",
     "B", "Chabahar Port in Iran's Sistan-Baluchestan province gives India access to Afghanistan and Central Asia, bypassing Pakistan. India has invested heavily in this port and the Chabahar-Zahedan rail link.",
     "AP_HC", "International_Current_Affairs"),

    (30064, "India's position on the Iran-Israel-USA conflict has been to:",
     "Support Israel unconditionally as a strategic partner", "Support Iran as it supplies oil to India", "Call for dialogue, diplomacy and de-escalation without taking sides", "Abstain on all UN resolutions related to the conflict",
     "C", "India has consistently called for dialogue, diplomacy, and de-escalation without taking sides in the Iran-Israel-USA conflict. India has significant interests with both sides — strategic ties with Israel and energy/Chabahar ties with Iran.",
     "AP_HC", "International_Current_Affairs"),

    (30065, "The closure of the Strait of Hormuz in 2026 caused global oil prices to spike dramatically. Approximately what percentage of global oil passes through the Strait?",
     "10%", "15%", "20%", "30%",
     "C", "Approximately 20% of global crude oil (and 30% of global LNG) passes through the Strait of Hormuz daily — about 17-21 million barrels per day. Its closure in 2026 caused a major global energy crisis.",
     "AP_HC", "International_Current_Affairs"),

    # ══════════════════════════════════════════
    # SECTION F: MIXED / HIGHER ORDER
    # ══════════════════════════════════════════

    (30066, "Which of the following is the CORRECT chronological order of key events in the Iran-Israel escalation?",
     "October 7 Hamas attack → JCPOA withdrawal → Twelve-Day War → 2026 Iran War", "JCPOA withdrawal → October 7 Hamas attack → Twelve-Day War → 2026 Iran War", "Twelve-Day War → October 7 attack → JCPOA withdrawal → 2026 Iran War", "JCPOA withdrawal → Twelve-Day War → October 7 attack → 2026 Iran War",
     "B", "Correct order: JCPOA withdrawal (2018) → October 7 Hamas attack (2023) → Twelve-Day War (June 2025) → 2026 Iran War (Feb 28, 2026). The 2024 Iran-Israel missile exchanges also occurred between the Hamas attack and the Twelve-Day War.",
     "AP_HC", "International_Current_Affairs"),

    (30067, "The Twelve-Day War and the 2026 Iran War are both considered part of which broader ongoing crisis?",
     "The War on Terror (2001-present)", "The Middle Eastern Crisis (2023-present)", "The Arab Spring aftermath", "The Iran Nuclear Standoff (2018-present)",
     "B", "Both the Twelve-Day War (June 2025) and the 2026 Iran War are considered part of the 'Middle Eastern Crisis (2023-present)', which began with the Hamas attack on Israel on October 7, 2023.",
     "AP_HC", "International_Current_Affairs"),

    (30068, "The US CENTCOM (Central Command) commander during the 2026 Iran War was:",
     "Frank McKenzie", "Kenneth McKenzie", "Michael Kurilla", "Erik Kurilla",
     "C", "General Michael Kurilla served as the US CENTCOM (United States Central Command) commander during the 2026 Iran War, overseeing US military operations across the Middle East.",
     "AP_HC", "International_Current_Affairs"),

    (30069, "Israel's current (2026) Prime Minister, who has led Israel through both the Twelve-Day War and the 2026 Iran War, is:",
     "Yair Lapid", "Naftali Bennett", "Benny Gantz", "Benjamin Netanyahu",
     "D", "Benjamin Netanyahu, Israel's longest-serving Prime Minister, led Israel through the Gaza War (2023-25), Twelve-Day War (June 2025), and the 2026 Iran War. He faces ICC arrest warrant for actions in Gaza.",
     "AP_HC", "International_Current_Affairs"),

    (30070, "Israel's Defense Minister during the Twelve-Day War and 2026 Iran War is:",
     "Yoav Gallant", "Benny Gantz", "Israel Katz", "Moshe Yaalon",
     "C", "Israel Katz serves as Israel's Defense Minister during this period. He succeeded Yoav Gallant (who was dismissed by Netanyahu in November 2024). Eyal Zamir serves as IDF Chief of Staff.",
     "AP_HC", "International_Current_Affairs"),

    (30071, "The Iran-Israel proxy war that preceded the direct conflicts involved Iran supporting which two main groups against Israel?",
     "ISIS and Al-Qaeda", "Hamas (Gaza) and Hezbollah (Lebanon)", "Houthis (Yemen) and Islamic Jihad", "Palestinian Authority and PFLP",
     "B", "Iran's main proxies against Israel are Hamas in Gaza and Hezbollah in Lebanon. Iran also supports Houthis in Yemen and PMF in Iraq, but Hamas and Hezbollah are the primary anti-Israel proxies.",
     "AP_HC", "International_Current_Affairs"),

    (30072, "Iran's supreme nuclear enrichment facility Natanz is located in which Iranian province?",
     "Tehran Province", "Isfahan Province", "Khuzestan Province", "Bushehr Province",
     "B", "The Natanz Fuel Enrichment Plant is located in Isfahan Province, Iran. It is Iran's main uranium enrichment facility and was one of the primary targets in both the Twelve-Day War and earlier strikes.",
     "AP_HC", "International_Current_Affairs"),

    (30073, "Which country hosted the US military base Al Udeid, struck by Iran in the Twelve-Day War?",
     "Saudi Arabia", "Bahrain", "UAE", "Qatar",
     "D", "Al Udeid Air Base is located in Qatar, about 30 km southwest of Doha. It is the largest US military base in the Middle East and hosts the CENTCOM forward headquarters. Iran struck it with missiles after the US bombed Iranian nuclear sites.",
     "AP_HC", "International_Current_Affairs"),

    (30074, "During the Twelve-Day War, approximately how many suicide drones (loitering munitions) did Iran fire at Israel?",
     "200+", "500+", "1,000+", "2,000+",
     "C", "Iran fired over 1,000 suicide drones (loitering munitions) along with 550+ ballistic missiles at Israel during the Twelve-Day War (June 2025), as part of Operation True Promise III.",
     "AP_HC", "International_Current_Affairs"),

    (30075, "The 2026 Iran protests (Jan 2026) that triggered US military threats were described as the largest since 1979. What was the immediate cause of these protests?",
     "Iran's nuclear deal failure", "Economic collapse and currency crash", "Continued government repression and massacre of civilians in ongoing unrest", "Death of a prominent reformist leader",
     "C", "The 2025-2026 Iranian protests were an extension of growing unrest. In January 2026, Iranian security forces massacred thousands of civilians in their crackdown on the growing protest movement. This prompted Trump to threaten military action.",
     "AP_HC", "International_Current_Affairs"),

    (30076, "Which entity declared Iran non-compliant with nuclear obligations the day before the Twelve-Day War began?",
     "UN Security Council", "IAEA (International Atomic Energy Agency) Board of Governors", "G7 foreign ministers", "ICJ (International Court of Justice)",
     "B", "The IAEA Board of Governors passed a resolution on June 12, 2025 (the day before the Twelve-Day War began) declaring Iran non-compliant with its nuclear safeguards obligations. The resolution was tabled by USA, UK, France, and Germany.",
     "AP_HC", "International_Current_Affairs"),

    (30077, "The conditional ceasefire of April 8, 2026, mediated by Pakistan, was between which parties?",
     "Israel and Hezbollah only", "USA, Israel, Iran and its regional allies", "Iran and Saudi Arabia", "UN-brokered ceasefire between all parties",
     "B", "Pakistan mediated a conditional ceasefire on April 8, 2026 between the USA + Israel on one side and Iran + its regional allies (Hezbollah, Houthis, PMF) on the other side. Both sides continued small-scale attacks.",
     "AP_HC", "International_Current_Affairs"),

    (30078, "How many Hezbollah fighters were killed in the 2026 Lebanon War phase (per US-Israel estimates)?",
     "500 fighters", "1,000 fighters", "1,900 fighters", "3,000 fighters",
     "C", "Per US and Israel estimates, approximately 1,900 Hezbollah fighters were killed in the 2026 Lebanon War phase of the conflict. The broader 2026 Lebanon war killed 2,000+ civilians and militants combined.",
     "AP_HC", "International_Current_Affairs"),

    (30079, "What was the significance of Iran striking the Akrotiri military base on Cyprus during the 2026 Iran War?",
     "Cyprus is a member of the Axis of Resistance", "It targeted a British sovereign base area — effectively attacking a NATO/EU member state's military asset", "It was the first time a Middle Eastern country struck Europe", "Akrotiri houses Israel's air defence radar",
     "B", "Akrotiri is a British Overseas Territory (Sovereign Base Area) on Cyprus. By striking it with a drone, Iran was attacking a military asset of the United Kingdom — a NATO and EU member — significantly widening the conflict geographically.",
     "AP_HC", "International_Current_Affairs"),

    (30080, "The US stated multiple rationales for launching the 2026 war on Iran. Which of the following was NOT a stated US rationale?",
     "To prevent Iran from building a nuclear weapon", "To destroy Iran's ballistic missile capabilities", "To seize Iran's oil resources and redistribute them", "To forestall an imminent Iranian threat",
     "C", "While the US cited multiple rationales — preventing nuclear weapons, destroying missile capabilities, forestalling threats, and regime change — 'seizing Iran's oil and redistributing it' was NOT a stated official US rationale (though critics alleged this as a motive).",
     "AP_HC", "International_Current_Affairs"),
]


def seed():
    conn = get_conn()
    if USE_POSTGRES:
        cur_chk = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    else:
        cur_chk = conn.cursor()

    # Force-refresh: delete and re-insert to fix folder/topic if wrong
    cur_chk.execute("DELETE FROM questions WHERE id >= 30001 AND id <= 30080")
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
            print(f"[seed_mideast_war_mcq] Skipping ID {q[0]}: {e}")
            try:
                conn.rollback()
            except:
                pass

    conn.commit()
    print(f"[seed_mideast_war_mcq] Inserted {inserted}/{len(QUESTIONS)} questions (IDs 30001–30080).")
    conn.close()


if __name__ == '__main__':
    seed()
