"""
Seed: Sports Current Affairs 2024-2026
IDs: 27001–27080
Folder: AP_HC
Topic: National_Current_Affairs
Cross-checked: GKToday Sports MCQs (Page 1), Olympics.com, ICC, PIB
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

    cur.execute("SELECT COUNT(*) FROM questions WHERE id >= 27001 AND id <= 27080")
    if cur.fetchone()[0] >= 75:
        conn.close()
        return

    ph = "?"
    questions = [
        # --- IOC ---
        {
            "id": 27001,
            "question_text": "The headquarter of the International Olympic Committee (IOC) is located in which city and country?",
            "option_a": "Athens, Greece",
            "option_b": "Sydney, Australia",
            "option_c": "Lausanne, Switzerland",
            "option_d": "Brussels, Belgium",
            "correct_answer": "C",
            "explanation": "The International Olympic Committee (IOC) is headquartered in Lausanne, Switzerland. It was founded in 1894 by Pierre de Coubertin to revive the ancient Greek Olympics. Its mission is 'Building a Better World through Sport.'",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27002,
            "question_text": "Kirsty Coventry, elected as the new IOC President in 2025, is from which country?",
            "option_a": "Australia",
            "option_b": "Canada",
            "option_c": "Zimbabwe",
            "option_d": "Kenya",
            "correct_answer": "C",
            "explanation": "Kirsty Coventry from Zimbabwe was elected as the President of the International Olympic Committee (IOC) in 2025 in Greece. She is a former Olympic champion swimmer and became the first woman ever to lead the IOC.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27003,
            "question_text": "Kirsty Coventry's election as IOC President in 2025 is historic because she is?",
            "option_a": "First Asian to lead IOC",
            "option_b": "First woman ever to lead IOC",
            "option_c": "Youngest IOC President ever",
            "option_d": "First African to lead IOC",
            "correct_answer": "B",
            "explanation": "Kirsty Coventry (Zimbabwe) made history in 2025 as the first woman ever to lead the International Olympic Committee (IOC). She is a former Olympic champion swimmer and was elected in Greece.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27004,
            "question_text": "The IOC was founded in which year and by whom?",
            "option_a": "1896, by Baron Pierre de Coubertin",
            "option_b": "1894, by Baron Pierre de Coubertin",
            "option_c": "1900, by Avery Brundage",
            "option_d": "1908, by Lord Killanin",
            "correct_answer": "B",
            "explanation": "The International Olympic Committee (IOC) was founded in 1894 by Baron Pierre de Coubertin to revive the ancient Greek Olympics. The first modern Olympics were held in Athens, Greece in 1896.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Paris Olympics 2024 ---
        {
            "id": 27005,
            "question_text": "How many medals did India win at the Paris Olympics 2024?",
            "option_a": "4 medals",
            "option_b": "5 medals",
            "option_c": "6 medals",
            "option_d": "7 medals",
            "correct_answer": "C",
            "explanation": "India won 6 medals at the Paris Olympics 2024 — 1 Silver and 5 Bronze. India sent a contingent of 117 athletes. The silver came from Neeraj Chopra (javelin throw), and the 5 bronze medals came from Manu Bhaker (2), Swapnil Kusale, Indian hockey team, and Aman Sehrawat.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27006,
            "question_text": "Neeraj Chopra won which medal at the Paris Olympics 2024?",
            "option_a": "Gold",
            "option_b": "Silver",
            "option_c": "Bronze",
            "option_d": "He did not participate",
            "correct_answer": "B",
            "explanation": "Neeraj Chopra won a Silver medal in Javelin Throw at the Paris Olympics 2024. At the Tokyo Olympics 2020, he had won the Gold medal in javelin throw — India's only individual gold at those Games.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27007,
            "question_text": "Manu Bhaker is historic at Paris Olympics 2024 because she?",
            "option_a": "Won India's first Olympic gold in shooting",
            "option_b": "Became first Indian woman to win an Olympic shooting medal (won 2 bronze)",
            "option_c": "Set a world record in 10m air pistol",
            "option_d": "Won the first Olympic gold in women's wrestling",
            "correct_answer": "B",
            "explanation": "Manu Bhaker became the first Indian woman to win an Olympic shooting medal at Paris 2024. She won 2 bronze medals — in Women's 10m Air Pistol and in Mixed Team 10m Air Pistol (with Sarabjot Singh) — making her the first Indian since Independence to win 2 medals in the same Olympics.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27008,
            "question_text": "Manu Bhaker won her second bronze medal at Paris Olympics 2024 in the Mixed Team 10m Air Pistol event partnering which shooter?",
            "option_a": "Sift Kaur Samra",
            "option_b": "Arjun Babuta",
            "option_c": "Sarabjot Singh",
            "option_d": "Aishwary Pratap Singh Tomar",
            "correct_answer": "C",
            "explanation": "Manu Bhaker partnered with Sarabjot Singh to win a Bronze medal in the Mixed Team 10m Air Pistol event at Paris Olympics 2024. This was her second bronze at the same Games, making her the first Indian since Independence to win two medals at a single Olympics.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27009,
            "question_text": "Swapnil Kusale won a Bronze medal at Paris Olympics 2024 in which shooting event?",
            "option_a": "Men's 10m Air Rifle",
            "option_b": "Men's 25m Rapid Fire Pistol",
            "option_c": "Men's 50m Rifle 3 Positions",
            "option_d": "Men's 10m Air Pistol",
            "correct_answer": "C",
            "explanation": "Swapnil Kusale won a Bronze medal at Paris Olympics 2024 in the Men's 50m Rifle 3 Positions event. This was one of India's 5 bronze medals at the Games. India's total Paris 2024 tally was 1 Silver + 5 Bronze = 6 medals.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27010,
            "question_text": "Aman Sehrawat won a Bronze medal at Paris Olympics 2024 in which sport?",
            "option_a": "Boxing (51 kg)",
            "option_b": "Wrestling 57 kg Freestyle",
            "option_c": "Judo 73 kg",
            "option_d": "Weightlifting 73 kg",
            "correct_answer": "B",
            "explanation": "Aman Sehrawat won a Bronze medal in Wrestling (57 kg Freestyle) at Paris Olympics 2024, becoming one of India's youngest Olympic medalists.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Paralympics 2024 ---
        {
            "id": 27011,
            "question_text": "India won how many medals at the Paris Paralympics 2024, which was its best-ever Paralympic performance?",
            "option_a": "19",
            "option_b": "24",
            "option_c": "29",
            "option_d": "35",
            "correct_answer": "C",
            "explanation": "India won 29 medals at the Paris Paralympics 2024 — 7 Gold, 9 Silver, and 13 Bronze. This was India's best-ever Paralympic tally, surpassing the previous record of 19 medals at Tokyo 2020.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Cricket T20 WC 2024 ---
        {
            "id": 27012,
            "question_text": "India won the ICC Men's T20 World Cup 2024 by defeating which team in the final?",
            "option_a": "Australia",
            "option_b": "England",
            "option_c": "Pakistan",
            "option_d": "South Africa",
            "correct_answer": "D",
            "explanation": "India defeated South Africa by 7 runs in the ICC Men's T20 World Cup 2024 final at the Kensington Oval, Barbados. India remained unbeaten throughout the campaign. It was India's first T20 World Cup title since 2007.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27013,
            "question_text": "The ICC Men's T20 World Cup 2024 final was played at which venue?",
            "option_a": "Wankhede Stadium, Mumbai",
            "option_b": "Lord's Cricket Ground, London",
            "option_c": "Kensington Oval, Barbados",
            "option_d": "MCG, Melbourne",
            "correct_answer": "C",
            "explanation": "The ICC Men's T20 World Cup 2024 final between India and South Africa was played at the Kensington Oval in Barbados, West Indies. India won by 7 runs, led by captain Rohit Sharma.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27014,
            "question_text": "Before the 2024 win, when did India last win the ICC Men's T20 World Cup?",
            "option_a": "2010",
            "option_b": "2014",
            "option_c": "2007",
            "option_d": "2016",
            "correct_answer": "C",
            "explanation": "India's previous ICC Men's T20 World Cup title was in 2007 — the inaugural edition. The 2024 victory ended a 17-year wait for India to recapture the T20 world title. The 2024 team was captained by Rohit Sharma.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27015,
            "question_text": "Who captained India in the ICC Men's T20 World Cup 2024?",
            "option_a": "Virat Kohli",
            "option_b": "Hardik Pandya",
            "option_c": "Rohit Sharma",
            "option_d": "KL Rahul",
            "correct_answer": "C",
            "explanation": "Rohit Sharma captained India in the ICC Men's T20 World Cup 2024. India beat South Africa by 7 runs in the final at Barbados. After winning the T20 WC 2024, Rohit Sharma and Virat Kohli announced their retirement from T20 International cricket.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27016,
            "question_text": "The ICC Men's T20 World Cup 2024 was co-hosted by which two nations?",
            "option_a": "Australia and New Zealand",
            "option_b": "India and Sri Lanka",
            "option_c": "USA and West Indies",
            "option_d": "England and Ireland",
            "correct_answer": "C",
            "explanation": "The ICC Men's T20 World Cup 2024 was co-hosted by the USA and West Indies. It was the first time a major ICC event was held in the USA. The final was held at the Kensington Oval, Barbados.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- ICC Champions Trophy 2025 ---
        {
            "id": 27017,
            "question_text": "India won the ICC Champions Trophy 2025, defeating which team in the final?",
            "option_a": "Australia",
            "option_b": "New Zealand",
            "option_c": "England",
            "option_d": "Pakistan",
            "correct_answer": "B",
            "explanation": "India won the ICC Champions Trophy 2025, defeating New Zealand in the final. The tournament was hosted by Pakistan and UAE. This added another ICC trophy to India's growing collection following the T20 WC 2024 title.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- FIFA 2026 ---
        {
            "id": 27018,
            "question_text": "The 2026 FIFA World Cup will be co-hosted by which three countries?",
            "option_a": "Brazil, Argentina, and Uruguay",
            "option_b": "England, France, and Germany",
            "option_c": "Canada, Mexico, and USA",
            "option_d": "Spain, Portugal, and Morocco",
            "correct_answer": "C",
            "explanation": "The 2026 FIFA World Cup will be co-hosted by Canada, Mexico, and the United States — the first time three countries have co-hosted a FIFA World Cup. It will also be the first expanded World Cup featuring 48 teams (up from 32).",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27019,
            "question_text": "The 2026 FIFA World Cup is the first to feature how many teams?",
            "option_a": "32",
            "option_b": "40",
            "option_c": "48",
            "option_d": "64",
            "correct_answer": "C",
            "explanation": "The 2026 FIFA World Cup will feature 48 teams, expanded from the previous 32. This expansion allows more nations — including at least 8 from the Asian Football Confederation (AFC) — to participate.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27020,
            "question_text": "Which country became the first non-host nation to qualify for the 2026 FIFA World Cup?",
            "option_a": "China",
            "option_b": "Japan",
            "option_c": "Australia",
            "option_d": "South Korea",
            "correct_answer": "B",
            "explanation": "Japan became the first non-host nation to qualify for the 2026 FIFA World Cup, joining co-hosts Canada, Mexico, and USA. Japan secured qualification with a 2-0 win over Bahrain, with Daichi Kamada and Takefusa Kubo scoring. It was Japan's 8th consecutive World Cup appearance (since 1998).",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27021,
            "question_text": "Japan's qualification for the 2026 FIFA World Cup made it their how-many-th consecutive World Cup appearance?",
            "option_a": "5th",
            "option_b": "6th",
            "option_c": "7th",
            "option_d": "8th",
            "correct_answer": "D",
            "explanation": "Japan's 2026 FIFA World Cup qualification was its 8th consecutive World Cup appearance since 1998. Japan won 2-0 over Bahrain, with Daichi Kamada and Takefusa Kubo scoring.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Khelo India ---
        {
            "id": 27022,
            "question_text": "The 7th edition of Khelo India Youth Games 2025 was held for the first time in which state?",
            "option_a": "Odisha",
            "option_b": "Karnataka",
            "option_c": "Bihar",
            "option_d": "Punjab",
            "correct_answer": "C",
            "explanation": "The 7th edition of Khelo India Youth Games 2025 was held in Bihar for the first time, from May 4 to 15, 2025. It spanned five districts: Patna, Nalanda, Gaya, Bhagalpur, and Begusarai. More than 8,500 athletes participated in 28 sports. PM Modi launched it via videoconference on May 4, 2025.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27023,
            "question_text": "Khelo India Youth Games 2025 in Bihar was held across how many districts?",
            "option_a": "Three",
            "option_b": "Four",
            "option_c": "Five",
            "option_d": "Seven",
            "correct_answer": "C",
            "explanation": "Khelo India Youth Games 2025 in Bihar was held across 5 districts: Patna, Nalanda, Gaya, Bhagalpur, and Begusarai (May 4–15, 2025). Over 8,500 athletes and 1,500 technical staff participated in 28 sports.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Kho-Kho ---
        {
            "id": 27024,
            "question_text": "The 57th Senior National Kho-Kho Championship 2025 was held in which city of Odisha?",
            "option_a": "Bhubaneswar",
            "option_b": "Cuttack",
            "option_c": "Puri",
            "option_d": "Rourkela",
            "correct_answer": "C",
            "explanation": "The 57th Senior National Kho-Kho Championship 2025 was held at the District Sports Complex in Puri, Odisha, from March 31 to April 4, 2025. A total of 74 teams participated, organized under the Kho Kho Federation of India (KKFI).",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27025,
            "question_text": "The Kho Kho Federation of India (KKFI) organized the 57th Senior National Kho-Kho Championship. How many teams participated?",
            "option_a": "52",
            "option_b": "64",
            "option_c": "74",
            "option_d": "88",
            "correct_answer": "C",
            "explanation": "A total of 74 teams participated in the 57th Senior National Kho-Kho Championship 2025 in Puri, Odisha — including 30 state teams and institutional squads from Airport Authority, Railways, BSF, Maharashtra Police, and CISF.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Handball ---
        {
            "id": 27026,
            "question_text": "Which state won the 47th National Junior Girls' Handball Championship 2025?",
            "option_a": "Rajasthan",
            "option_b": "Madhya Pradesh",
            "option_c": "Gujarat",
            "option_d": "Uttar Pradesh",
            "correct_answer": "D",
            "explanation": "Uttar Pradesh won the 47th National Junior Girls' Handball Championship by defeating Himachal Pradesh 19-17 at KD Singh 'Babu' Stadium in Lucknow (March 26-30, 2025). UP trailed 10-8 at halftime but made a strong comeback.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27027,
            "question_text": "The 47th National Junior Girls' Handball Championship was held at which venue in Lucknow?",
            "option_a": "Ekana Sports Complex",
            "option_b": "KD Singh 'Babu' Stadium",
            "option_c": "Guru Nanak Sports Complex",
            "option_d": "Surya Kumar Yadav Sports Academy",
            "correct_answer": "B",
            "explanation": "The 47th National Junior Girls' Handball Championship was held at KD Singh 'Babu' Stadium in Lucknow, Uttar Pradesh (March 26-30, 2025). UP beat Himachal Pradesh 19-17 in the final.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Archery ---
        {
            "id": 27028,
            "question_text": "India won how many medals at the Archery World Cup 2025 Stage-2 held in Shanghai, China?",
            "option_a": "5",
            "option_b": "7",
            "option_c": "9",
            "option_d": "10",
            "correct_answer": "B",
            "explanation": "India won 7 medals at the Archery World Cup 2025 Stage-2 in Shanghai, China (May 6-11, 2025) — 2 Gold, 1 Silver, and 4 Bronze. Madhura Dhamangaonkar won gold in women's individual compound. Ojas Deotale's team won men's team compound gold.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- ISSF ---
        {
            "id": 27029,
            "question_text": "India finished in which position at the ISSF World Cup Lima 2025 (Rifle and Shotgun)?",
            "option_a": "First",
            "option_b": "Second",
            "option_c": "Third",
            "option_d": "Fourth",
            "correct_answer": "C",
            "explanation": "India finished 3rd at the ISSF World Cup Lima 2025 (Rifle and Shotgun), winning 7 medals — 2 Gold, 4 Silver, 1 Bronze. The tournament was held in Lima, Peru (April 13-22, 2025). China finished 1st and USA 2nd.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27030,
            "question_text": "ISSF stands for?",
            "option_a": "International Shooting Sports Federation",
            "option_b": "Indian Shooting Sports Foundation",
            "option_c": "International Sharpshooters Sports Fraternity",
            "option_d": "International Shooting Sport Federation",
            "correct_answer": "D",
            "explanation": "ISSF stands for International Shooting Sport Federation (note: 'Sport' not 'Sports'). It is the world governing body for Olympic shooting sports. Its headquarters are in Lausanne, Switzerland.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Vandana Katariya ---
        {
            "id": 27031,
            "question_text": "Vandana Katariya, who retired from international hockey, played how many international matches?",
            "option_a": "250",
            "option_b": "280",
            "option_c": "300",
            "option_d": "320",
            "correct_answer": "D",
            "explanation": "Vandana Katariya played 320 international matches in her career spanning over 15 years, making her the most-capped player in Indian women's hockey history. She scored 158 goals. She made her senior team debut in 2009.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27032,
            "question_text": "Vandana Katariya is the first Indian woman to achieve which feat at the Olympics?",
            "option_a": "First Indian woman to win an Olympic gold in hockey",
            "option_b": "First Indian woman to score a hat-trick at the Olympics",
            "option_c": "First Indian woman to captain an Olympic hockey team",
            "option_d": "First Indian woman to score 100 international goals",
            "correct_answer": "B",
            "explanation": "Vandana Katariya is the first and only Indian woman to score a hat-trick at the Olympics. She received the Arjuna Award in 2021 and the Padma Shri in 2022, and the Hockey India Dhanraj Pillay Award for Forward of the Year in 2021 and 2022.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27033,
            "question_text": "In which year was Vandana Katariya awarded the Padma Shri?",
            "option_a": "2018",
            "option_b": "2020",
            "option_c": "2021",
            "option_d": "2022",
            "correct_answer": "D",
            "explanation": "Vandana Katariya was awarded the Padma Shri in 2022. She had earlier received the Arjuna Award in 2021. She is the most-capped Indian women's hockey player with 320 international matches and 158 goals.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Mahendra Gurjar ---
        {
            "id": 27034,
            "question_text": "Mahendra Gurjar set a world record of 61.17 metres in which para-athletics event at the 2025 Nottwil World Para Athletics Grand Prix?",
            "option_a": "F41 Javelin Throw",
            "option_b": "F42 Javelin Throw",
            "option_c": "F54 Discus Throw",
            "option_d": "F46 Shot Put",
            "correct_answer": "B",
            "explanation": "Mahendra Gurjar set a world record of 61.17 metres in the Men's F42 Javelin Throw at the 2025 Nottwil World Para Athletics Grand Prix in Switzerland (May 26, 2025). This surpassed the previous world record of 59.19 m set by Brazil's Roberto Floriani Edenilson in 2022. F42 is the classification for athletes with moderate movement impairment in one leg.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27035,
            "question_text": "The 2025 Nottwil World Para Athletics Grand Prix, where Mahendra Gurjar set a world record, was held in which country?",
            "option_a": "Germany",
            "option_b": "France",
            "option_c": "Switzerland",
            "option_d": "Italy",
            "correct_answer": "C",
            "explanation": "The 2025 Nottwil World Para Athletics Grand Prix was held in Nottwil, Switzerland on May 26, 2025. Mahendra Gurjar won the gold medal in the F42 Javelin Throw with a world record throw of 61.17 metres.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Asian Wrestling ---
        {
            "id": 27036,
            "question_text": "Manisha Bhanwala won India's first gold medal at the Senior Asian Wrestling Championship 2025 in which weight category?",
            "option_a": "48 kg",
            "option_b": "53 kg",
            "option_c": "62 kg",
            "option_d": "68 kg",
            "correct_answer": "C",
            "explanation": "Manisha Bhanwala won gold in the women's 62 kg category at the Senior Asian Wrestling Championship 2025 in Amman, Jordan, defeating Korea's Ok J Kim by 8-7. This was India's first gold at this championship since 2021.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27037,
            "question_text": "The Senior Asian Wrestling Championship 2025 was held in which city?",
            "option_a": "New Delhi",
            "option_b": "Tokyo",
            "option_c": "Astana",
            "option_d": "Amman",
            "correct_answer": "D",
            "explanation": "The Senior Asian Wrestling Championship 2025 was held in Amman, Jordan. India won 1 Gold (Manisha Bhanwala, 62 kg), 1 Silver, and 6 Bronze medals, including 2 in Greco-Roman wrestling.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27038,
            "question_text": "Antim Panghal won a Bronze medal in which weight category at the Senior Asian Wrestling Championship 2025?",
            "option_a": "48 kg",
            "option_b": "50 kg",
            "option_c": "53 kg",
            "option_d": "57 kg",
            "correct_answer": "C",
            "explanation": "Antim Panghal won a Bronze medal in the 53 kg category at the Senior Asian Wrestling Championship 2025 in Amman, Jordan, defeating Taipei's Meng H Hsieh by technical superiority.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Sports Bodies HQ ---
        {
            "id": 27039,
            "question_text": "FIFA, the governing body of world football, is headquartered in which city?",
            "option_a": "Geneva",
            "option_b": "Zurich",
            "option_c": "Bern",
            "option_d": "Lausanne",
            "correct_answer": "B",
            "explanation": "FIFA (Fédération Internationale de Football Association) is headquartered in Zurich, Switzerland. It was founded in 1904 and governs association football worldwide. The 2026 FIFA World Cup will be hosted by Canada, Mexico, and USA.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27040,
            "question_text": "The International Cricket Council (ICC) is headquartered in which city?",
            "option_a": "London, UK",
            "option_b": "Mumbai, India",
            "option_c": "Dubai, UAE",
            "option_d": "Melbourne, Australia",
            "correct_answer": "C",
            "explanation": "The International Cricket Council (ICC) is headquartered in Dubai, UAE. It governs international cricket and organizes major events like the T20 World Cup, Cricket World Cup, and Champions Trophy. India won the ICC T20 World Cup 2024 and ICC Champions Trophy 2025.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27041,
            "question_text": "The Badminton World Federation (BWF) is headquartered in which city?",
            "option_a": "Beijing",
            "option_b": "Bangkok",
            "option_c": "Singapore",
            "option_d": "Kuala Lumpur",
            "correct_answer": "D",
            "explanation": "The Badminton World Federation (BWF) is headquartered in Kuala Lumpur, Malaysia. It is the international governing body for badminton and oversees all international badminton competitions.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27042,
            "question_text": "World Athletics (formerly IAAF), the governing body for track and field sports, is headquartered in which city?",
            "option_a": "Geneva, Switzerland",
            "option_b": "Monaco",
            "option_c": "Paris, France",
            "option_d": "London, UK",
            "correct_answer": "B",
            "explanation": "World Athletics (formerly the International Association of Athletics Federations or IAAF) is headquartered in Monaco. It governs all track and field events, including those in the Olympic Games.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Chess ---
        {
            "id": 27043,
            "question_text": "D Gukesh became the World Chess Champion in December 2024 by defeating which player?",
            "option_a": "Magnus Carlsen (Norway)",
            "option_b": "Fabiano Caruana (USA)",
            "option_c": "Ding Liren (China)",
            "option_d": "Ian Nepomniachtchi (Russia)",
            "correct_answer": "C",
            "explanation": "D Gukesh of India became the World Chess Champion in December 2024 by defeating reigning champion Ding Liren of China. At 18 years of age, Gukesh became the youngest World Chess Champion in history. He received the Khel Ratna Award 2024.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27044,
            "question_text": "D Gukesh became the World Chess Champion in 2024. He is the youngest World Chess Champion ever at what age?",
            "option_a": "16 years",
            "option_b": "17 years",
            "option_c": "18 years",
            "option_d": "19 years",
            "correct_answer": "C",
            "explanation": "D Gukesh became the youngest World Chess Champion in history at 18 years of age in December 2024. He defeated China's Ding Liren in the World Chess Championship match and received the Khel Ratna Award 2024.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        {
            "id": 27045,
            "question_text": "India won both Open and Women's team titles at which Chess Olympiad in 2024?",
            "option_a": "Warsaw",
            "option_b": "Budapest",
            "option_c": "Dubai",
            "option_d": "Chennai",
            "correct_answer": "B",
            "explanation": "India swept the FIDE Chess Olympiad 2024 held in Budapest, Hungary, winning both the Open team and Women's team gold medals. This was a historic double gold for India in international chess.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- 2028 Olympics ---
        {
            "id": 27046,
            "question_text": "The 2028 Summer Olympics will be hosted by which city?",
            "option_a": "London",
            "option_b": "Tokyo",
            "option_c": "Los Angeles",
            "option_d": "Brisbane",
            "correct_answer": "C",
            "explanation": "The 2028 Summer Olympics will be hosted by Los Angeles, USA. The 2032 Summer Olympics are scheduled for Brisbane, Australia. Los Angeles previously hosted the Olympics in 1932 and 1984.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Paris Olympics host ---
        {
            "id": 27047,
            "question_text": "The 2024 Summer Olympics were held in which city?",
            "option_a": "Tokyo",
            "option_b": "Paris",
            "option_c": "London",
            "option_d": "Berlin",
            "correct_answer": "B",
            "explanation": "The 2024 Summer Olympics (XXXIII Olympiad) were held in Paris, France from July 26 to August 11, 2024. India won 6 medals (1 Silver + 5 Bronze) with a contingent of 117 athletes.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Archery medal winners ---
        {
            "id": 27048,
            "question_text": "Madhura Dhamangaonkar won gold at the Archery World Cup 2025 Stage-2 in which event?",
            "option_a": "Women's individual recurve",
            "option_b": "Women's individual compound",
            "option_c": "Mixed team recurve",
            "option_d": "Women's team compound",
            "correct_answer": "B",
            "explanation": "Madhura Dhamangaonkar won a gold medal in the women's individual compound event at the Archery World Cup 2025 Stage-2 in Shanghai, China (May 6-11, 2025). India won 7 medals overall at this event.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- IOC founding place ---
        {
            "id": 27049,
            "question_text": "Kirsty Coventry was elected as IOC President in which country?",
            "option_a": "France",
            "option_b": "Switzerland",
            "option_c": "Greece",
            "option_d": "USA",
            "correct_answer": "C",
            "explanation": "Kirsty Coventry from Zimbabwe was elected as IOC President in Greece. She is the first woman to lead the IOC. Greece holds special significance for the Olympics as the birthplace of the ancient Olympic Games.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- KKFI ---
        {
            "id": 27050,
            "question_text": "KKFI, which organized the 57th Senior National Kho-Kho Championship 2025, stands for?",
            "option_a": "Kho Kho Foundation of India",
            "option_b": "Kho Kho Federation of India",
            "option_c": "Kho Kho Forum of India",
            "option_d": "Kabaddi-Kho Kho Federation of India",
            "correct_answer": "B",
            "explanation": "KKFI stands for Kho Kho Federation of India. It organized the 57th Senior National Kho-Kho Championship in Puri, Odisha (March 31 to April 4, 2025). 74 teams participated including state teams and institutional squads.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Neeraj Chopra ---
        {
            "id": 27051,
            "question_text": "Neeraj Chopra won which medal at the Tokyo Olympics 2020?",
            "option_a": "Silver in Javelin Throw",
            "option_b": "Gold in Javelin Throw",
            "option_c": "Bronze in Javelin Throw",
            "option_d": "Gold in Shot Put",
            "correct_answer": "B",
            "explanation": "Neeraj Chopra won Gold in Javelin Throw at the Tokyo Olympics 2020, becoming the first Indian to win an Olympic gold in track and field. At Paris 2024, he won Silver. He is a Khel Ratna and Padma Shri awardee.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- India hockey Paris ---
        {
            "id": 27052,
            "question_text": "Which Indian sports team won a Bronze medal at the Paris Olympics 2024?",
            "option_a": "Women's Cricket team",
            "option_b": "Men's Football team",
            "option_c": "Men's Hockey team",
            "option_d": "Women's Badminton team",
            "correct_answer": "C",
            "explanation": "The Indian Men's Hockey team won a Bronze medal at the Paris Olympics 2024. India also won hockey bronze at Tokyo 2020, ending a 41-year medal drought in Olympic hockey. India has won 8 Olympic gold medals in hockey (all-time record).",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- World Athletics ---
        {
            "id": 27053,
            "question_text": "The Kho-Kho World Cup 2025, organized by the International Kho Kho Federation, was held in which country?",
            "option_a": "India",
            "option_b": "South Africa",
            "option_c": "UAE",
            "option_d": "England",
            "correct_answer": "A",
            "explanation": "The Kho-Kho World Cup 2025 was held in India. Both the men's and women's Indian Kho-Kho teams won the World Cup in the inaugural edition. India is the dominant force in Kho-Kho internationally.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Khelo India Institutions ---
        {
            "id": 27054,
            "question_text": "Bihar set up which new institution as part of hosting Khelo India Youth Games 2025?",
            "option_a": "Bihar Olympic Academy",
            "option_b": "Bihar Sports University",
            "option_c": "Patna Sports Institute",
            "option_d": "National Sports Authority Bihar",
            "correct_answer": "B",
            "explanation": "Bihar set up new institutions including the Khelo India State Centre of Excellence and Bihar Sports University as part of hosting Khelo India Youth Games 2025. This was the first time Bihar hosted the event.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Tokyo to Paris ---
        {
            "id": 27055,
            "question_text": "India won how many medals at the Tokyo Olympics 2020?",
            "option_a": "5",
            "option_b": "7",
            "option_c": "10",
            "option_d": "12",
            "correct_answer": "B",
            "explanation": "India won 7 medals at the Tokyo Olympics 2020 — 1 Gold (Neeraj Chopra, Javelin), 2 Silver (Mirabai Chanu-Weightlifting, Ravi Dahiya-Wrestling), and 4 Bronze (PV Sindhu-Badminton, Lovlina Borgohain-Boxing, Men's Hockey team, Bajrang Punia-Wrestling). This was India's best Olympic haul at that time. Paris 2024 (6 medals) was slightly fewer.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Nottwil ---
        {
            "id": 27056,
            "question_text": "The F42 classification in para-athletics applies to athletes with which type of impairment?",
            "option_a": "Visually impaired",
            "option_b": "Moderate movement impairment in one leg",
            "option_c": "Wheelchair athletes",
            "option_d": "Upper limb amputation",
            "correct_answer": "B",
            "explanation": "The F42 classification in para-athletics is for athletes with moderate movement impairment in one leg. Mahendra Gurjar set the world record of 61.17m in F42 Javelin Throw at the Nottwil World Para Athletics Grand Prix in Switzerland (May 2025).",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- FIDE ---
        {
            "id": 27057,
            "question_text": "FIDE, the world chess governing body, is headquartered in which city?",
            "option_a": "Moscow",
            "option_b": "New York",
            "option_c": "Lausanne",
            "option_d": "London",
            "correct_answer": "C",
            "explanation": "FIDE (Fédération Internationale des Échecs / International Chess Federation) is headquartered in Lausanne, Switzerland. It is the governing body for international chess and organizes the World Chess Championship, Chess Olympiad, and other events.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Vandana debut ---
        {
            "id": 27058,
            "question_text": "In which year did Vandana Katariya make her senior international hockey debut?",
            "option_a": "2005",
            "option_b": "2007",
            "option_c": "2009",
            "option_d": "2011",
            "correct_answer": "C",
            "explanation": "Vandana Katariya made her senior international hockey debut in 2009 and went on to play 320 international matches over 15+ years. She retired after becoming the most-capped player in Indian women's hockey history with 158 goals.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Japan Kamada Kubo ---
        {
            "id": 27059,
            "question_text": "Which two Japanese footballers scored in the 2026 FIFA World Cup qualification win over Bahrain?",
            "option_a": "Takumi Minamino and Shinji Kagawa",
            "option_b": "Daichi Kamada and Takefusa Kubo",
            "option_c": "Yuya Osako and Wataru Endo",
            "option_d": "Ritsu Doan and Junya Ito",
            "correct_answer": "B",
            "explanation": "Daichi Kamada and Takefusa Kubo scored in the second half as Japan beat Bahrain 2-0 to qualify for the 2026 FIFA World Cup, becoming the first non-host nation to secure their place in the tournament.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Mirabai Chanu ---
        {
            "id": 27060,
            "question_text": "At Paris Olympics 2024, India sent how many athletes in total?",
            "option_a": "95",
            "option_b": "107",
            "option_c": "117",
            "option_d": "128",
            "correct_answer": "C",
            "explanation": "India sent a contingent of 117 athletes to the Paris Olympics 2024. The team won 6 medals — 1 Silver (Neeraj Chopra) and 5 Bronze (Manu Bhaker x2, Swapnil Kusale, Hockey team, Aman Sehrawat).",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Sports federations ---
        {
            "id": 27061,
            "question_text": "The International Handball Federation (IHF) is headquartered in which Swiss city?",
            "option_a": "Zurich",
            "option_b": "Geneva",
            "option_c": "Basel",
            "option_d": "Bern",
            "correct_answer": "C",
            "explanation": "The International Handball Federation (IHF) is headquartered in Basel, Switzerland. It governs international handball. The 47th National Junior Girls' Handball Championship 2025 in India was won by Uttar Pradesh.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Pierre de Coubertin ---
        {
            "id": 27062,
            "question_text": "Pierre de Coubertin, who founded the IOC in 1894, was from which country?",
            "option_a": "Greece",
            "option_b": "Great Britain",
            "option_c": "France",
            "option_d": "Germany",
            "correct_answer": "C",
            "explanation": "Baron Pierre de Coubertin was a French historian and educator who founded the International Olympic Committee (IOC) in 1894 to revive the ancient Greek Olympics. The first modern Olympic Games were held in Athens, Greece in 1896.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- ICC WC 2023 ---
        {
            "id": 27063,
            "question_text": "Who won the ICC Men's Cricket World Cup (ODI) 2023 held in India?",
            "option_a": "India",
            "option_b": "New Zealand",
            "option_c": "South Africa",
            "option_d": "Australia",
            "correct_answer": "D",
            "explanation": "Australia won the ICC Men's Cricket World Cup (ODI) 2023 held in India, defeating India in the final at Narendra Modi Stadium, Ahmedabad by 6 wickets. Australia's Pat Cummins was the leading wicket-taker.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Khelo India launch ---
        {
            "id": 27064,
            "question_text": "Prime Minister Modi launched the 7th Khelo India Youth Games 2025 on which date?",
            "option_a": "April 4, 2025",
            "option_b": "May 4, 2025",
            "option_c": "June 4, 2025",
            "option_d": "March 4, 2025",
            "correct_answer": "B",
            "explanation": "Prime Minister Narendra Modi launched the 7th Khelo India Youth Games on May 4, 2025 through videoconferencing. The games were held in Bihar (first time) from May 4–15, 2025, across 5 districts: Patna, Nalanda, Gaya, Bhagalpur, and Begusarai.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Olympics 2024 opening/closing ---
        {
            "id": 27065,
            "question_text": "Paris Olympics 2024 opening ceremony was held in which unique venue?",
            "option_a": "Stade de France",
            "option_b": "River Seine",
            "option_c": "Champs-Élysées",
            "option_d": "Eiffel Tower plaza",
            "correct_answer": "B",
            "explanation": "The Paris Olympics 2024 opening ceremony was uniquely held on the River Seine (July 26, 2024), with athletes parading on boats along the river through Paris — the first Olympics opening ceremony held outside a stadium.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Deepika Kumari ---
        {
            "id": 27066,
            "question_text": "Deepika Kumari, who won a bronze medal at Archery World Cup 2025 Stage-2, is associated with which archery bow type?",
            "option_a": "Compound bow",
            "option_b": "Recurve bow",
            "option_c": "Longbow",
            "option_d": "Crossbow",
            "correct_answer": "B",
            "explanation": "Deepika Kumari is India's top recurve archer who won a bronze in women's individual recurve at Archery World Cup 2025 Stage-2 in Shanghai. She is a former world number 1 in recurve archery and multiple World Cup winner.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Asian Wrestling gold ---
        {
            "id": 27067,
            "question_text": "Manisha Bhanwala's gold at Asian Wrestling Championship 2025 was India's first gold at the championship since which year?",
            "option_a": "2019",
            "option_b": "2020",
            "option_c": "2021",
            "option_d": "2022",
            "correct_answer": "C",
            "explanation": "Manisha Bhanwala's gold medal at the Senior Asian Wrestling Championship 2025 in Amman, Jordan was India's first gold at the championship since the 2021 edition. She defeated Korea's Ok J Kim 8-7 in the women's 62 kg final.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Vandana Arjuna award ---
        {
            "id": 27068,
            "question_text": "In which year did Vandana Katariya receive the Arjuna Award for her contributions to Indian hockey?",
            "option_a": "2018",
            "option_b": "2019",
            "option_c": "2021",
            "option_d": "2023",
            "correct_answer": "C",
            "explanation": "Vandana Katariya received the Arjuna Award in 2021 for her contributions to Indian hockey. She also received the Padma Shri in 2022 and the Hockey India Dhanraj Pillay Award for Forward of the Year in 2021 and 2022.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- ICC T20 2022 winner ---
        {
            "id": 27069,
            "question_text": "Which country won the ICC Men's T20 World Cup 2022 held in Australia?",
            "option_a": "India",
            "option_b": "Pakistan",
            "option_c": "England",
            "option_d": "Australia",
            "correct_answer": "C",
            "explanation": "England won the ICC Men's T20 World Cup 2022 held in Australia, defeating Pakistan by 5 wickets in the final at Melbourne. India had lost to England in the semi-finals.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Sumit Antil ---
        {
            "id": 27070,
            "question_text": "Para-athlete Sumit Antil won a Gold medal at Paris Paralympics 2024 in which event?",
            "option_a": "F64 Discus Throw",
            "option_b": "F64 Javelin Throw",
            "option_c": "T64 Long Jump",
            "option_d": "F44 Shot Put",
            "correct_answer": "B",
            "explanation": "Sumit Antil won Gold in F64 Javelin Throw at Paris Paralympics 2024, setting a new world record. He had previously won gold at Tokyo 2020. F64 is the classification for single leg amputation below the knee. He is a Khel Ratna awardee.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Gukesh Khel Ratna ---
        {
            "id": 27071,
            "question_text": "D Gukesh received which India's highest sports honour in 2024?",
            "option_a": "Arjuna Award",
            "option_b": "Dhyan Chand Award",
            "option_c": "Khel Ratna (Major Dhyan Chand Khel Ratna Award)",
            "option_d": "Dronacharya Award",
            "correct_answer": "C",
            "explanation": "D Gukesh received the Major Dhyan Chand Khel Ratna Award (India's highest sports honour) in 2024 for becoming World Chess Champion. Other Khel Ratna 2024 recipients included Manu Bhaker, Harmanpreet Singh, and Praveen Kumar.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- 2026 Olympics winter ---
        {
            "id": 27072,
            "question_text": "The 2026 Winter Olympics will be hosted by which city?",
            "option_a": "Oslo, Norway",
            "option_b": "Milan-Cortina, Italy",
            "option_c": "Sapporo, Japan",
            "option_d": "Salt Lake City, USA",
            "correct_answer": "B",
            "explanation": "The 2026 Winter Olympics will be held in Milan-Cortina, Italy. This will be Italy's third Winter Olympics after Cortina d'Ampezzo (1956) and Turin (2006).",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Para World Record Previous ---
        {
            "id": 27073,
            "question_text": "Mahendra Gurjar's world record of 61.17m broke the previous record of 59.19m set by whom?",
            "option_a": "Germany's Thomas Röhler",
            "option_b": "Brazil's Roberto Floriani Edenilson",
            "option_c": "Canada's Scott Martin",
            "option_d": "Australia's Todd Hodgetts",
            "correct_answer": "B",
            "explanation": "Mahendra Gurjar's 61.17m world record in F42 Javelin Throw surpassed the previous world record of 59.19 metres set by Brazil's Roberto Floriani Edenilson in 2022, at the 2025 Nottwil World Para Athletics Grand Prix in Switzerland.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- ISSF host ---
        {
            "id": 27074,
            "question_text": "The ISSF World Cup Lima 2025 was held in which country?",
            "option_a": "Argentina",
            "option_b": "Brazil",
            "option_c": "Colombia",
            "option_d": "Peru",
            "correct_answer": "D",
            "explanation": "The ISSF World Cup for Rifle and Shotgun 2025 was held in Lima, the capital city of Peru (April 13-22, 2025). India finished 3rd with 2 Gold, 4 Silver, and 1 Bronze medal, behind China (1st) and USA (2nd).",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Chess Olympiad ---
        {
            "id": 27075,
            "question_text": "The FIDE Chess Olympiad 2024, which India won both Open and Women's gold, was held in which city?",
            "option_a": "Chennai, India",
            "option_b": "Warsaw, Poland",
            "option_c": "Budapest, Hungary",
            "option_d": "Vienna, Austria",
            "correct_answer": "C",
            "explanation": "The FIDE Chess Olympiad 2024 was held in Budapest, Hungary. India swept both the Open and Women's team gold medals — a historic double. India hosted the Chess Olympiad in Chennai in 2022.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Para India best tally ---
        {
            "id": 27076,
            "question_text": "India's 29 medals at Paris Paralympics 2024 was its best-ever Paralympic tally, surpassing the previous best of how many medals?",
            "option_a": "13",
            "option_b": "17",
            "option_c": "19",
            "option_d": "23",
            "correct_answer": "C",
            "explanation": "India's 29 medals at Paris Paralympics 2024 (7 Gold + 9 Silver + 13 Bronze) surpassed its previous best of 19 medals won at the Tokyo 2020 Paralympics. This represents the rapid growth of India's para-sports program.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- ICC women's T20 WC 2024 ---
        {
            "id": 27077,
            "question_text": "Which country won the ICC Women's T20 World Cup 2024?",
            "option_a": "Australia",
            "option_b": "India",
            "option_c": "New Zealand",
            "option_d": "England",
            "correct_answer": "C",
            "explanation": "New Zealand won the ICC Women's T20 World Cup 2024 held in UAE, defeating South Africa in the final. This was New Zealand's first ICC Women's T20 World Cup title.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- AFC teams ---
        {
            "id": 27078,
            "question_text": "AFC stands for which full form in the context of football's Asian qualifying federation for FIFA World Cup?",
            "option_a": "Africa Football Confederation",
            "option_b": "Asian Football Championship",
            "option_c": "Asian Football Confederation",
            "option_d": "All Football Committee",
            "correct_answer": "C",
            "explanation": "AFC stands for Asian Football Confederation — the governing body for football in Asia. For the 2026 FIFA World Cup, at least 8 AFC teams can qualify due to the expanded 48-team format. Japan was the first AFC team to qualify.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- Manu Bhaker history ---
        {
            "id": 27079,
            "question_text": "Manu Bhaker became the first Indian since Independence to win how many medals at a single Olympics?",
            "option_a": "1",
            "option_b": "2",
            "option_c": "3",
            "option_d": "4",
            "correct_answer": "B",
            "explanation": "Manu Bhaker became the first Indian since Independence to win 2 medals at a single Olympics at Paris 2024 — Bronze in Women's 10m Air Pistol and Bronze in Mixed Team 10m Air Pistol (with Sarabjot Singh). She was also the first Indian woman to win an Olympic shooting medal.",
            "folder": "AP_HC",
            "topic": "National_Current_Affairs"
        },
        # --- ISSF Lima 2nd event ---
        {
            "id": 27080,
            "question_text": "Where was the first ISSF World Cup 2025 (Rifle and Shotgun) held before the Lima event?",
            "option_a": "Baku, Azerbaijan",
            "option_b": "Buenos Aires, Argentina",
            "option_c": "Cairo, Egypt",
            "option_d": "New Delhi, India",
            "correct_answer": "B",
            "explanation": "The first ISSF World Cup 2025 (Rifle and Shotgun) was held in Buenos Aires, Argentina (April 1-10, 2025). The second event was held in Lima, Peru (April 13-22, 2025), where India finished 3rd with 7 medals.",
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
    print("Sports Current Affairs MCQs seeded: IDs 27001–27080")
