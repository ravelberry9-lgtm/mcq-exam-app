# Fact ledger — time group (sources 05, 06, 07, 29, 30, 31, 38, 39 + shared)

| # | Fact | Src | Status | Note |
|---|---|---|---|---|
| 1 | Local sky meridian; Solar noon = Sun crosses meridian, ≈ highest elevation, not overhead | 05 | keep | time-why-differ |
| 2 | Local mean solar time = averaged; "Mean" = సగటు | 05,29 | keep | time-4min |
| 3 | Apparent solar time differs slightly | 29 | fix | added cause (orbit eccentricity, tilt) and ≈16 min (USNO eqtime) |
| 4 | Horizon definition | 05 | keep | used in trap; handoff for altitude |
| 5 | Earth rotates W→E, east gets sun first | 05,29 | keep | |
| 6 | 360/24 = 15°/h; 1° = 4 min; 1440/360 | 05,17,29 | keep | |
| 7 | Same-side subtract, opposite sides add | 05 | keep | with why |
| 8 | 10°W Mon 23:00 → 20°E Tue 01:00 | 05 | keep | example 4 |
| 9 | 0° 12:00 → 80°E 17:20 | 05,38 | keep | |
| 10 | 30°E 14:00 → 78°E 17:12 | 05,38 | keep | |
| 11 | 10°W Sun 11:20 → 75°W Sun 07:00; book's 4h40 wrong | 05,38 | keep | |
| 12 | 75°E 12:00 → 90°E 13:00 | 05,29,36 | drop | duplicate of 15° = 1 h teaching; covered by table |
| 13 | 192 min = 3 h 12 min, not 3.12 | 05,38 | keep | trap |
| 14 | 0° 07:00, local 11:00 → 60°E | 05,38 | keep | example 5 |
| 15 | 80°E LMT ≠ Amaravati official time | 05,06,38 | keep | trap |
| 16 | Pretoria–Hyderabad legal clock difference ≠ 3h12 | 38 | drop | covered by LMT vs civil trap; Pretoria not named elsewhere |
| 17 | 60°E/75°E July 10 00:30 → July 9 example | 17 | drop | duplicate of midnight-crossing ex. 4 |
| 18 | UTC definition, offset | 06 | keep | |
| 19 | IST = UTC + 05:30; CSIR-NPL | 06,30,32 | keep | verified NPL |
| 20 | Standard meridian 82°30′E; 82.5×4 = 330 | 06,30,38 | keep | |
| 21 | Not every place on that line | 06 | keep | implicit (Vijayawada/Vizag) |
| 22 | Civil time; towns share standard time | 06 | keep | time-zones |
| 23 | DST shifts clock, not rotation | 06,17 | keep | trap |
| 24 | UTC Mon 22:00 → IST Tue 03:30 | 06,36 | keep | problem 1 |
| 25 | Country zone counts need scope/date | 06,16,38 | fix | gave verified dated values + exam block |
| 26 | Australia AWST +8, ACST +9:30, AEST +10; Lord Howe | 06,17 | keep | Lord Howe +10:30 |
| 27 | +05:45 = 345 min, +06:30 = 390, +09:30 = 570; 5:30 ≠ 5.30 | 06 | keep | trap (06:30 omitted from list — kept 345, 570) |
| 28 | 180°E +12, 180°W −12 → 24 h gap → need date line | 07 | keep | |
| 29 | IDL bends for islands/countries; ≠ 180° exactly | 07,31 | keep | named Siberia, Aleutians, Kiribati (NOAA, USNO) |
| 30 | Westward +1 day, eastward −1 day | 07,31,39 | keep | |
| 31 | Date-line rule separate from flight duration | 07,39 | keep | problems section |
| 32 | Why near 180° (opposite PM, ocean) | 31 | keep | |
| 33 | India morning / America night picture | 29 | keep | |
| 34 | Sidereal day 23 h 56 min 4 s | 29,18 | keep | with why |
| 35 | Longitude ≠ exact sunrise; latitude, season, horizon | 29,36 | keep | trap |
| 36 | Arunachal sunrise before Gujarat | 29 | keep | ~2 h (NCERT) |
| 37 | India extremes ~2 h LMT difference | 30 | keep | 68°7′, 97°25′; computed 1 h 57 min |
| 38 | Chaos if each town own time | 30 | keep | |
| 39 | 82½° passes near Mirzapur, UP | 30 | keep | NCERT |
| 40 | easternmost 97°25′ vs standard 82°30′; 77°6′/82°32′ distractors | 30 | fix | exam block; 82°33′ framing added |
| 41 | 30′ = half degree (arcminute) | 30 | keep | + 1′ = 4 s added |
| 42 | GMT vs UTC; IST = GMT + 5:30; UTC 06:00 → IST 11:30 | 30,17 | keep | (06:00 example dropped as dup of problem 1) |
| 43 | London summer not UTC (BST = GMT + 1) | 30,17 | keep | |
| 44 | AP: Vijayawada, Vizag same clock, different solar time | 30 | keep | computed 12:08 / 11:57 |
| 45 | 24 × 15° ideal model; fractional offsets | 38,39 | keep | |
| 46 | France overseas territories, Réunion +4 | 38,17 | fix | kept general point; Réunion example dropped (detail beyond exam) |
| 47 | USA 4 / 9 (BTS 2021) | 17,38 | keep | |
| 48 | Russia 2014: 11 zones UTC+2..+12; 2010 change historical | 17,38,16 | keep | exam block |
| 49 | UK GMT/BST, overseas territories | 17,38 | keep | |
| 50 | Time-zone map is dated | 39,17 | keep | merged into "count changes" line |
| 51 | Nepal +5:45; India 12:00 → Nepal 12:15 | 17,19 | keep | |
| 52 | Date line: July 10 → 9 east; Dec 31 → Jan 1 west | 17 | keep | problem 5 |
| 53 | Same instant can have two calendar dates | 39 | keep | problem 6 |
| 54 | Prime Meridian chosen 1884 | 17 | keep | time-4min |
| 55 | "France 12, US 11, UK 9, Australia 9" totals | 16 | drop | source itself says unverified; replaced by verified scoped values |
| A1 | IST effective 1 Jan 1906; Madras time 1802 Goldingham (+5:21:14); Calcutta time to 1948; Bombay to 1955; official 1947 | — | add | LiveHistoryIndia (dated qualifier) |
| A2 | Chaibagan time IST + 1 | — | add | Down To Earth |
| A3 | NPL 2018 Current Science: IST-I +5:30, IST-II +6:30, boundary 89°52′E | — | add | Down To Earth |
| A4 | Govt 19 Dec 2018 Lok Sabha (Harsh Vardhan), HLC: no two zones, strategic reasons | — | add | ThePrint |
| A5 | China single zone UTC+8 over ~60° | — | add | common knowledge (73°E–135°E); not separately web-verified |
| A6 | Kiribati Line Islands UTC + 14; offsets −12 to +14 | — | add | USNO (1995 shift); +14 widely documented |
| A7 | Kiribati 1995 line shift to ~150°W | — | add | USNO |
| A8 | Samoa 2011 switched, skipped Fri 30 Dec | — | add | EarthSky; USNO page summary said "no Dec 31" — EarthSky/tz list say 30 Dec, used 30 |
| A9 | IDL no international legal status | — | add | USNO, NOAA |
| A10 | Magellan crew 1519–22 lost a day | — | add | USNO |
| A11 | Equation of time ≈ up to 16 min | — | add | USNO eqtime |
| A12 | Worked problems 2–4, 6 (Nepal, Australia, London flight, 165°E/W) | — | add | computed |

## Verified facts with URL
- IST UTC+5:30, NPL maintains — https://www.nplindia.res.in/clockcode/html/ ; https://www.nplindia.in/index.php/indian-standard-time/
- IDL facts (1995 Kiribati, 2011 Samoa, Magellan, no legal force, 1921 Admiralty line) — https://aa.usno.navy.mil/faq/international_date
- IDL basics, 1884 — https://oceanservice.noaa.gov/facts/international-date-line.html
- NPL two zones 2018 — https://www.downtoearth.org.in/news/science-technology/india-s-timekeeper-says-country-needs-two-time-zones-61846
- Govt rejection 19 Dec 2018 — https://theprint.in/governance/no-separate-time-zone-for-northeastern-states-for-strategic-reasons-says-centre/166258
- IST history — https://livehistoryindia.com/story/eras/indian-standard-time
- Samoa 30 Dec 2011 — https://earthsky.org/human-world/friday-december-30-2011-struck-from-samoan-calendar/
- Mirzapur/82°30′E/68°7′–97°25′ — NCERT Class 9 Ch 1 (fetch blocked; confirmed via multiple NCERT-solution pages in search)
