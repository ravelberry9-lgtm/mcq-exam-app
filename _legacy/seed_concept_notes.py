#!/usr/bin/env python3
"""
seed_concept_notes.py
Bilingual (English + Telugu) concept notes for Awards & Honours MCQs.
Run once on Render after deploy: python seed_concept_notes.py
"""
import os, sys

DATABASE_URL = os.environ.get('DATABASE_URL', '')
USE_POSTGRES = bool(DATABASE_URL)

if USE_POSTGRES:
    import psycopg2
    conn = psycopg2.connect(DATABASE_URL)
else:
    import sqlite3
    DB = os.path.join(os.path.dirname(__file__), 'database.db')
    conn = sqlite3.connect(DB)

# ════════════════════════════════════════════════════════════════
#  CONCEPT NOTE HTML BLOCKS  (English + Telugu bilingual)
# ════════════════════════════════════════════════════════════════

NOTES = []   # list of (tag, label, label_te, html)

# ─────────────────────────────────────────────
# 1. NOBEL PRIZE
# ─────────────────────────────────────────────
NOTES.append(('nobel_prize', 'Nobel Prize', 'నోబెల్ పురస్కారం', """
<div class="concept-cover">
  <h1>Nobel Prize &nbsp;<span class="bi-te">/ నోబెల్ పురస్కారం</span></h1>
  <div class="sub">Alfred Nobel • Since 1901 • Stockholm &amp; Oslo</div>
</div>

<div class="section-hdr">What is the Nobel Prize? / నోబెల్ పురస్కారం అంటే ఏమిటి?</div>
<p>The Nobel Prize is the world's most prestigious award, given annually in recognition of outstanding contributions to Physics, Chemistry, Medicine, Literature, Peace, and Economics. It was established by the will of Alfred Nobel — a Swedish chemist and inventor of dynamite — who died in 1896. The first Nobel Prizes were awarded in 1901.</p>
<p class="bi-te">నోబెల్ పురస్కారం ప్రపంచంలోనే అత్యంత ప్రతిష్ఠాత్మకమైన అవార్డు. భౌతికశాస్త్రం, రసాయనశాస్త్రం, వైద్యం, సాహిత్యం, శాంతి, ఆర్థిక శాస్త్రం రంగాల్లో అత్యుత్తమ కృషికి ప్రతి సంవత్సరం ఇవ్వబడుతుంది. స్వీడిష్ శాస్త్రవేత్త ఆల్ఫ్రెడ్ నోబెల్ (డైనమైట్ ఆవిష్కర్త) వీలునామా ద్వారా స్థాపించబడింది. 1896లో నోబెల్ మరణించాడు; 1901లో మొదటి అవార్డులు ఇవ్వబడ్డాయి.</p>

<div class="section-hdr">Alfred Nobel — Who Was He? / ఆల్ఫ్రెడ్ నోబెల్ ఎవరు?</div>
<table class="key-table">
<tr><th>Fact</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Born</td><td>October 21, 1833 — Stockholm, Sweden</td><td class="bi-te">అక్టోబర్ 21, 1833 — స్వీడన్</td></tr>
<tr><td>Died</td><td>December 10, 1896 — San Remo, Italy</td><td class="bi-te">డిసెంబర్ 10, 1896 — ఇటలీ</td></tr>
<tr><td>Invention</td><td>Dynamite (1867) + 355 patents</td><td class="bi-te">డైనమైట్ (1867) + 355 పేటెంట్లు</td></tr>
<tr><td>Will</td><td>Prize day = Dec 10 (his death anniversary)</td><td class="bi-te">పురస్కార దినం = అతని వర్థంతి</td></tr>
</table>

<div class="section-hdr">Nobel Prize Categories / నోబెల్ విభాగాలు</div>
<table class="key-table">
<tr><th>Category / విభాగం</th><th>Awarded By / ఇచ్చేవారు</th><th>Since / నుండి</th></tr>
<tr><td>Physics / భౌతికశాస్త్రం</td><td>Royal Swedish Academy of Sciences</td><td>1901</td></tr>
<tr><td>Chemistry / రసాయనం</td><td>Royal Swedish Academy of Sciences</td><td>1901</td></tr>
<tr><td>Medicine / వైద్యం</td><td>Karolinska Institute, Stockholm</td><td>1901</td></tr>
<tr><td>Literature / సాహిత్యం</td><td>Swedish Academy</td><td>1901</td></tr>
<tr><td>Peace / శాంతి</td><td>Norwegian Nobel Committee, <b>Oslo</b></td><td>1901</td></tr>
<tr><td>Economics / ఆర్థికం</td><td>Royal Swedish Academy of Sciences</td><td><b>1969</b></td></tr>
</table>
<p><b>Note:</b> Economics Prize is NOT in Alfred Nobel's original 1895 will — added by Sweden's central bank (Riksbank) in 1968, first awarded 1969.</p>
<p class="bi-te"><b>గమనిక:</b> ఆర్థిక పురస్కారం మూల వీలునామాలో లేదు. స్వీడన్ సెంట్రల్ బ్యాంక్ 1968లో జోడించింది; 1969లో మొదటిసారి ఇవ్వబడింది.</p>

<div class="section-hdr">Nobel Prize 2025 — Winners / 2025 నోబెల్ విజేతలు</div>
<table class="key-table">
<tr><th>Category</th><th>Winner(s)</th><th>For / కారణం</th></tr>
<tr><td>Physics</td><td>John Clarke, Michel Devoret, John M. Martinis</td><td>Quantum tunnelling &amp; energy quantisation — basis of superconducting qubits (quantum computers)</td></tr>
<tr><td>Chemistry</td><td>Susumu Kitagawa, Richard Robson, Omar M. Yaghi</td><td>Metal-Organic Frameworks (MOFs) — ultra-porous materials; CO₂ capture, drug delivery</td></tr>
<tr><td>Medicine</td><td>Mary Brunkow, Fred Ramsdell, Shimon Sakaguchi</td><td>Regulatory T cells (Tregs) — prevent autoimmune diseases; FOXP3 gene</td></tr>
<tr><td>Literature</td><td>László Krasznahorkai (Hungary)</td><td>"Compelling and visionary oeuvre" — Satantango (12 chapters like tango steps)</td></tr>
<tr><td>Peace</td><td>Maria Corina Machado (Venezuela)</td><td>Democratic struggle against Maduro's dictatorship in Venezuela</td></tr>
<tr><td>Economics</td><td>Joel Mokyr, Philippe Aghion, Peter Howitt</td><td>Innovation-driven growth &amp; "creative destruction" theory</td></tr>
</table>

<div class="section-hdr">India's Nobel Laureates / భారత్ నోబెల్ విజేతలు</div>
<table class="key-table">
<tr><th>Name</th><th>Year</th><th>Category / విభాగం</th></tr>
<tr><td>Rabindranath Tagore</td><td>1913</td><td>Literature / సాహిత్యం</td></tr>
<tr><td>C.V. Raman</td><td>1930</td><td>Physics / భౌతికం</td></tr>
<tr><td>Mother Teresa</td><td>1979</td><td>Peace / శాంతి</td></tr>
<tr><td>Amartya Sen</td><td>1998</td><td>Economics / ఆర్థికం</td></tr>
<tr><td>Venkatraman Ramakrishnan</td><td>2009</td><td>Chemistry / రసాయనం</td></tr>
<tr><td>Kailash Satyarthi</td><td>2014</td><td>Peace / శాంతి</td></tr>
</table>

<div class="section-hdr">Quick Exam Facts / పరీక్షకు ముఖ్య అంశాలు</div>
<table>
<tr><th>Fact / అంశం</th><th>Answer / జవాబు</th></tr>
<tr><td>Peace Prize city</td><td>Oslo, Norway (all others: Stockholm)</td></tr>
<tr><td>Prize day</td><td>December 10 (Nobel's death anniversary)</td></tr>
<tr><td>Cash value (approx)</td><td>~$1.1 million USD per category</td></tr>
<tr><td>Max winners per prize</td><td>3 individuals (or 1 organisation for Peace)</td></tr>
<tr><td>Physics 2024</td><td>Hopfield &amp; Hinton (AI / neural networks)</td></tr>
<tr><td>Economics 2024</td><td>Acemoglu, Johnson, Robinson (institutions)</td></tr>
<tr><td>Literature 2024</td><td>Han Kang (South Korea) — first Korean</td></tr>
<tr><td>Peace 2024</td><td>Nihon Hidankyo (Japanese atomic bomb survivors)</td></tr>
</table>
"""))

# ─────────────────────────────────────────────
# 2. GRAMMY AWARDS
# ─────────────────────────────────────────────
NOTES.append(('grammy_awards', 'Grammy Awards', 'గ్రామీ అవార్డులు', """
<div class="concept-cover">
  <h1>Grammy Awards &nbsp;<span class="bi-te">/ గ్రామీ అవార్డులు</span></h1>
  <div class="sub">NARAS • Since 1959 • Music's Highest Honour</div>
</div>

<div class="section-hdr">What is the Grammy? / గ్రామీ అంటే ఏమిటి?</div>
<p>The Grammy Award is the music industry's highest honour, presented annually by the Recording Academy (NARAS — National Academy of Recording Arts and Sciences) of the United States. The name "Grammy" comes from the gramophone. First awarded in 1959 (for recordings of 1958). There are 94 categories; the four most prestigious are called the "General Field" (Big Four): Record of the Year, Album of the Year, Song of the Year, Best New Artist.</p>
<p class="bi-te">గ్రామీ అవార్డు సంగీత పరిశ్రమలో అత్యంత గౌరవప్రదమైన పురస్కారం. అమెరికాలోని రికార్డింగ్ అకాడమీ (NARAS) నిర్వహిస్తుంది. 1959 నుండి ప్రారంభమైంది. 94 విభాగాలు ఉన్నాయి. అత్యంత ప్రతిష్ఠాత్మకమైన 4 అవార్డులు: రికార్డ్ ఆఫ్ ది ఇయర్, ఆల్బమ్ ఆఫ్ ది ఇయర్, సాంగ్ ఆఫ్ ది ఇయర్, బెస్ట్ న్యూ ఆర్టిస్ట్.</p>

<div class="section-hdr">67th Grammys — February 2, 2025 / 67వ గ్రామీ అవార్డులు</div>
<p>Held at <b>Crypto.com Arena, Los Angeles</b>. Delayed one day due to the devastating LA wildfires of January 2025.</p>
<table class="key-table">
<tr><th>Category / విభాగం</th><th>Winner / విజేత</th><th>Work / కృతి</th></tr>
<tr><td>Album of the Year</td><td><b>Beyoncé</b></td><td>Cowboy Carter — her FIRST AOTY win (9 nominations before)</td></tr>
<tr><td>Record of the Year</td><td><b>Kendrick Lamar</b></td><td>"Not Like Us" — diss track targeting Drake</td></tr>
<tr><td>Song of the Year</td><td><b>Kendrick Lamar</b></td><td>"Not Like Us"</td></tr>
<tr><td>Best New Artist</td><td><b>Chappell Roan</b></td><td>"Good Luck, Babe!" / "The Rise and Fall of a Midwest Princess"</td></tr>
</table>
<p><b>Key fact:</b> Kendrick Lamar swept 5/5 nominations for "Not Like Us". Beyoncé now holds the all-time Grammy record — <b>32 wins</b> total (surpassing Georg Solti's 31). She was also the first Black woman to win Grammy for Best Country Album (Cowboy Carter).</p>
<p class="bi-te"><b>ముఖ్య అంశం:</b> కెండ్రిక్ లామర్ 5 నామినేషన్లలో 5 అవార్డులు గెలిచాడు. బియోన్సే మొత్తం 32 గ్రామీ అవార్డులతో అన్నికాలపు రికార్డు సాధించింది.</p>

<div class="section-hdr">68th Grammys — February 1, 2026 / 68వ గ్రామీ అవార్డులు</div>
<p>Also held at <b>Crypto.com Arena, Los Angeles</b>.</p>
<table class="key-table">
<tr><th>Category / విభాగం</th><th>Winner / విజేత</th><th>Note / విశేషం</th></tr>
<tr><td>Album of the Year</td><td><b>Bad Bunny</b></td><td>"Debí Tirar Más Fotos" — FIRST Spanish-language album to win AOTY</td></tr>
<tr><td>Record of the Year</td><td><b>Kendrick Lamar</b></td><td>"Luther" (feat. SZA) — 2nd consecutive ROTY; surpassed Jay-Z with 27+ total Grammys</td></tr>
<tr><td>Song of the Year</td><td><b>Billie Eilish &amp; Finneas</b></td><td>"Wildflower" — their 3rd SOTY win</td></tr>
<tr><td>Best New Artist</td><td><b>Olivia Dean</b> (UK)</td><td>9th consecutive woman to win; first British winner since Dua Lipa (2019)</td></tr>
</table>
<p class="bi-te">68వ గ్రామీ విశేషాలు: బాడ్ బన్నీ మొదటి స్పానిష్ AOTY; కెండ్రిక్ రెండవ వరుస ROTY; బిల్లీ ఐలిష్ మూడవ SOTY; ఒలీవియా డీన్ (UK) బెస్ట్ న్యూ ఆర్టిస్ట్.</p>

<div class="section-hdr">Quick Exam Facts / పరీక్ష ముఖ్య అంశాలు</div>
<table>
<tr><th>Fact</th><th>Answer</th></tr>
<tr><td>Full form of NARAS</td><td>National Academy of Recording Arts and Sciences</td></tr>
<tr><td>Grammy name origin</td><td>Gramophone</td></tr>
<tr><td>Most Grammy wins ever</td><td>Beyoncé — 32 wins</td></tr>
<tr><td>67th Grammys venue/date</td><td>Crypto.com Arena, LA — Feb 2, 2025</td></tr>
<tr><td>68th Grammys venue/date</td><td>Crypto.com Arena, LA — Feb 1, 2026</td></tr>
<tr><td>First Spanish-language AOTY</td><td>Bad Bunny — "Debí Tirar Más Fotos" (2026)</td></tr>
<tr><td>Kendrick Lamar Super Bowl</td><td>Super Bowl LIX halftime show — Feb 9, 2025, New Orleans</td></tr>
</table>
"""))

# ─────────────────────────────────────────────
# 3. BOOKER PRIZE
# ─────────────────────────────────────────────
NOTES.append(('booker_prize', 'Booker Prize', 'బుకర్ పురస్కారం', """
<div class="concept-cover">
  <h1>Booker Prize &nbsp;<span class="bi-te">/ బుకర్ పురస్కారం</span></h1>
  <div class="sub">Since 1969 • Fiction in English • £50,000</div>
</div>

<div class="section-hdr">What is the Booker Prize? / బుకర్ పురస్కారం అంటే ఏమిటి?</div>
<p>The Booker Prize (formally the Booker Prize for Fiction) is the UK's most prestigious literary award, given annually to the best novel written in English and published in the UK or Ireland. Prize: £50,000. First awarded in 1969. Since 2014, open to any novel written in English regardless of author's nationality.</p>
<p class="bi-te">బుకర్ పురస్కారం యునైటెడ్ కింగ్‌డమ్‌లో అత్యంత ప్రతిష్ఠాత్మకమైన సాహిత్య అవార్డు. ఇంగ్లీష్‌లో రాసిన ఉత్తమ నవలకు ఇవ్వబడుతుంది. బహుమతి: £50,000. 1969 నుండి ప్రారంభమైంది.</p>

<div class="section-hdr">Booker Prize 2025 / బుకర్ పురస్కారం 2025</div>
<table class="key-table">
<tr><th>Award</th><th>Winner</th><th>Details</th></tr>
<tr><td><b>Booker Prize 2025</b></td><td><b>David Szalay</b></td><td>"Flesh" — British-Canadian author of Hungarian descent. Previously shortlisted for "All That Man Is" (2016). Announced Nov 10, 2025 in London. Prize presented by 2024 winner Samantha Harvey.</td></tr>
<tr><td><b>International Booker 2025</b></td><td>Multiple authors (anthology)</td><td>"A Cage Went in Search of a Bird" — 10 stories by 10 authors, each inspired by a different Franz Kafka aphorism. Title from Kafka: "A cage went in search of a bird." Prize split between authors and translator.</td></tr>
</table>
<p class="bi-te">2025 బుకర్: డేవిడ్ సజ్లే "ఫ్లెష్" నవలకు. అంతర్జాతీయ బుకర్ 2025: "A Cage Went in Search of a Bird" — ఫ్రాంజ్ కాఫ్కా సూత్రాలపై ఆధారపడిన 10 కథలు.</p>

<div class="section-hdr">Booker Prize 2024 (Previous) / 2024 బుకర్</div>
<p><b>Samantha Harvey</b> — "Orbital" (2024). A novel set aboard the International Space Station, one continuous day in orbit. Harvey also presented the 2025 prize.</p>

<div class="section-hdr">International Booker Prize / అంతర్జాతీయ బుకర్ పురస్కారం</div>
<p>Separate award for translated fiction — published in English translation in UK/Ireland. Prize (£50,000) split equally between author and translator. Kafka inspired the 2025 winner's anthology title: <em>"A cage went in search of a bird"</em> is a Kafka aphorism meaning reality defies expectations.</p>

<div class="section-hdr">Quick Exam Facts / పరీక్ష ముఖ్య అంశాలు</div>
<table>
<tr><th>Fact</th><th>Answer</th></tr>
<tr><td>Prize amount</td><td>£50,000</td></tr>
<tr><td>First awarded</td><td>1969</td></tr>
<tr><td>Booker 2025 winner</td><td>David Szalay — "Flesh"</td></tr>
<tr><td>Booker 2024 winner</td><td>Samantha Harvey — "Orbital"</td></tr>
<tr><td>Int'l Booker 2025</td><td>"A Cage Went in Search of a Bird" (Kafka anthology)</td></tr>
<tr><td>Open to all nationalities since</td><td>2014</td></tr>
</table>
"""))

# ─────────────────────────────────────────────
# 4. PULITZER PRIZE
# ─────────────────────────────────────────────
NOTES.append(('pulitzer_prize', 'Pulitzer Prize', 'పులిట్జర్ పురస్కారం', """
<div class="concept-cover">
  <h1>Pulitzer Prize &nbsp;<span class="bi-te">/ పులిట్జర్ పురస్కారం</span></h1>
  <div class="sub">Columbia University, New York • Since 1917 • Journalism &amp; Arts</div>
</div>

<div class="section-hdr">What is the Pulitzer Prize? / పులిట్జర్ పురస్కారం అంటే ఏమిటి?</div>
<p>The Pulitzer Prize is the United States' most prestigious award in journalism, literature, drama, and music. Administered by Columbia University, New York. Established in 1917 per the will of Joseph Pulitzer — a Hungarian-American newspaper publisher. Awarded annually in 21 categories including Journalism (14 categories) and Arts/Letters (7 categories).</p>
<p class="bi-te">పులిట్జర్ పురస్కారం అమెరికాలో పత్రికారంగం, సాహిత్యం, నాటకం, సంగీతంలో అత్యంత ప్రతిష్ఠాత్మకమైన అవార్డు. న్యూయార్క్‌లోని కొలంబియా యూనివర్సిటీ నిర్వహిస్తుంది. 1917 నుండి ప్రారంభమైంది.</p>

<div class="section-hdr">Pulitzer Prize 2025 — Key Winners / 2025 పులిట్జర్ విజేతలు</div>
<table class="key-table">
<tr><th>Category / విభాగం</th><th>Winner / విజేత</th><th>Work / కృతి</th></tr>
<tr><td>Fiction / కల్పన</td><td><b>Percival Everett</b></td><td>"James" — retells Huck Finn from Jim's (enslaved man's) perspective. Also won PEN/Faulkner Award.</td></tr>
<tr><td>Poetry / కవిత్వం</td><td><b>Marie Howe</b></td><td>"What the Earth Seemed to Say: New &amp; Selected Poems." NY State Poet Laureate.</td></tr>
<tr><td>Music / సంగీతం</td><td><b>Susie Ibarra</b></td><td>"Sky Islands" — Filipino-American composer/percussionist; inspired by Philippine cloud forests &amp; indigenous music.</td></tr>
<tr><td>Drama / నాటకం</td><td>TBD 2025</td><td>(Check latest)</td></tr>
</table>
<p class="bi-te">2025 పులిట్జర్ ముఖ్యాంశాలు: పెర్సివల్ ఎవెరెట్ "జేమ్స్" — హక్ ఫిన్ నవలను బానిస వ్యక్తి జిమ్ కోణం నుండి చెప్పిన పునర్నిర్మాణం. మారీ హో కవిత్వంలో విజేత. సుసీ ఇబారా సంగీతంలో విజేత.</p>

<div class="section-hdr">Joseph Pulitzer — Founder / స్థాపకుడు</div>
<p>Joseph Pulitzer (1847-1911) was a Hungarian-American newspaper magnate who owned the New York World and St. Louis Post-Dispatch. He bequeathed funds to establish the School of Journalism at Columbia University and the Pulitzer Prizes. His legacy also includes the term "yellow journalism."</p>

<div class="section-hdr">Quick Exam Facts / పరీక్ష ముఖ్య అంశాలు</div>
<table>
<tr><th>Fact</th><th>Answer</th></tr>
<tr><td>Administered by</td><td>Columbia University, New York</td></tr>
<tr><td>First awarded</td><td>1917</td></tr>
<tr><td>Founded by</td><td>Joseph Pulitzer (Hungarian-American)</td></tr>
<tr><td>2025 Fiction</td><td>Percival Everett — "James"</td></tr>
<tr><td>2025 Poetry</td><td>Marie Howe</td></tr>
<tr><td>2025 Music</td><td>Susie Ibarra — "Sky Islands"</td></tr>
<tr><td>No. of categories</td><td>21 (14 journalism + 7 arts/letters)</td></tr>
</table>
"""))

# ─────────────────────────────────────────────
# 5. BALLON D'OR
# ─────────────────────────────────────────────
NOTES.append(('ballon_dor', "Ballon d'Or", "బెలాన్ డి'ఓర్", """
<div class="concept-cover">
  <h1>Ballon d'Or &nbsp;<span class="bi-te">/ బెలాన్ డి'ఓర్</span></h1>
  <div class="sub">France Football Magazine • Since 1956 • Football's Highest Individual Honour</div>
</div>

<div class="section-hdr">What is the Ballon d'Or? / బెలాన్ డి'ఓర్ అంటే ఏమిటి?</div>
<p>The Ballon d'Or ("Golden Ball" in French) is football's most prestigious individual award, presented annually by <em>France Football</em> magazine since 1956. It honours the best male and female football players in the world. Winners are selected by international journalists and national team coaches/captains.</p>
<p class="bi-te">బెలాన్ డి'ఓర్ ("గోల్డెన్ బాల్" అని ఫ్రెంచ్‌లో అర్థం) ఫుట్‌బాల్‌లో అత్యంత ప్రతిష్ఠాత్మకమైన వ్యక్తిగత అవార్డు. 1956 నుండి ఫ్రాన్స్ ఫుట్‌బాల్ పత్రిక అందజేస్తోంది.</p>

<div class="section-hdr">Ballon d'Or 2025 / 2025 బెలాన్ డి'ఓర్ విజేతలు</div>
<table class="key-table">
<tr><th>Award / అవార్డు</th><th>Winner / విజేత</th><th>Details / వివరాలు</th></tr>
<tr><td><b>Men's Ballon d'Or 2025</b></td><td><b>Ousmane Dembélé</b> (France, PSG)</td><td>PSG won a historic quadruple in 2024-25: Ligue 1, Coupe de France, Coupe de la Ligue, UEFA Champions League. Dembélé scored 30+ goals + 20+ assists.</td></tr>
<tr><td><b>Women's Ballon d'Or 2025</b></td><td><b>Aitana Bonmatí</b> (Spain, Barcelona)</td><td>Her THIRD consecutive win (also 2023 &amp; 2024) — a hat-trick. Considered world's best women's footballer.</td></tr>
<tr><td>Best Coach 2025</td><td>Sarina Wiegman (England women's coach)</td><td>Led England women's team to multiple titles</td></tr>
<tr><td>Yashin Trophy 2025 (GK)</td><td>TBD</td><td>Named after legendary Soviet goalkeeper Lev Yashin</td></tr>
</table>

<div class="section-hdr">All-Time Record Holders / అన్నికాలపు రికార్డులు</div>
<table class="key-table">
<tr><th>Player</th><th>Wins</th><th>Years</th></tr>
<tr><td>Lionel Messi (Argentina)</td><td><b>9 wins</b></td><td>2009,10,11,12,15,19,21,23,24 (record holder)</td></tr>
<tr><td>Cristiano Ronaldo (Portugal)</td><td>5 wins</td><td>2008,13,14,16,17</td></tr>
<tr><td>Aitana Bonmatí (Spain)</td><td>3 wins</td><td>2023, 2024, 2025 (consecutive)</td></tr>
</table>

<div class="section-hdr">Quick Exam Facts / పరీక్ష ముఖ్య అంశాలు</div>
<table>
<tr><th>Fact</th><th>Answer</th></tr>
<tr><td>Full name (French)</td><td>Ballon d'Or = "Golden Ball"</td></tr>
<tr><td>Presented by</td><td>France Football magazine</td></tr>
<tr><td>Since</td><td>1956</td></tr>
<tr><td>Men's 2025 winner</td><td>Ousmane Dembélé (PSG, France)</td></tr>
<tr><td>Women's 2025 winner</td><td>Aitana Bonmatí — 3rd consecutive</td></tr>
<tr><td>Most wins ever (men)</td><td>Lionel Messi — 9 Ballon d'Or wins</td></tr>
<tr><td>GK award name</td><td>Yashin Trophy (Lev Yashin — Soviet GK)</td></tr>
</table>
"""))

# ─────────────────────────────────────────────
# 6. KHEL RATNA
# ─────────────────────────────────────────────
NOTES.append(('khel_ratna', 'Major Dhyan Chand Khel Ratna Award', 'ఖేల్ రత్న పురస్కారం', """
<div class="concept-cover">
  <h1>Khel Ratna Award &nbsp;<span class="bi-te">/ ఖేల్ రత్న పురస్కారం</span></h1>
  <div class="sub">India's Highest Sports Honour • Ministry of Youth Affairs &amp; Sports</div>
</div>

<div class="section-hdr">What is Khel Ratna? / ఖేల్ రత్న అంటే ఏమిటి?</div>
<p>The Major Dhyan Chand Khel Ratna Award is India's highest sporting honour, presented annually by the President of India on the occasion of National Sports Day (August 29). Renamed in 2021 from "Rajiv Gandhi Khel Ratna" to honour hockey legend Major Dhyan Chand. Cash award: ₹25 lakh.</p>
<p class="bi-te">మేజర్ ధ్యాన్‌చంద్ ఖేల్ రత్న పురస్కారం భారత్‌లో అత్యున్నత క్రీడా పురస్కారం. ప్రతి సంవత్సరం ఆగస్ట్ 29న (జాతీయ క్రీడా దినం) భారత రాష్ట్రపతి అందజేస్తారు. 2021లో "రాజీవ్ గాంధీ ఖేల్ రత్న" నుండి పేరు మార్చబడింది. నగద బహుమతి: ₹25 లక్షలు.</p>

<div class="section-hdr">Khel Ratna 2025 — Winners / 2025 ఖేల్ రత్న విజేతలు</div>
<p>Awarded at Rashtrapati Bhavan by President Droupadi Murmu on <b>January 17, 2025</b>.</p>
<table class="key-table">
<tr><th>Athlete / క్రీడాకారుడు</th><th>Sport / క్రీడ</th><th>Achievement / విజయం</th></tr>
<tr><td><b>D. Gukesh</b></td><td>Chess / చదరంగం</td><td>Youngest World Chess Champion (age 18, Dec 2024) — defeated Ding Liren in Singapore</td></tr>
<tr><td><b>Harmanpreet Singh</b></td><td>Hockey / హాకీ</td><td>Captain of India's Paris 2024 Olympic bronze medal team; FIH Player of Year 2023, 2024</td></tr>
<tr><td><b>Praveen Kumar</b></td><td>Para-Athletics / పారా-ఆథ్లెటిక్స్</td><td>Gold in T64 High Jump, Paris 2024 Paralympics</td></tr>
<tr><td><b>Manu Bhaker</b></td><td>Shooting / షూటింగ్</td><td>Two bronze medals at Paris 2024 — first Indian to win 2 medals in single Olympics since 1900</td></tr>
</table>
<p class="bi-te">2025 ఖేల్ రత్న: గుకేశ్ (చదరంగం), హర్మన్‌ప్రీత్ (హాకీ), ప్రవీణ్ కుమార్ (పారా-ఆథ్లెటిక్స్), మను భాకర్ (షూటింగ్).</p>

<div class="section-hdr">Key Facts About Manu Bhaker / మను భాకర్ గురించి</div>
<p>Manu Bhaker won 2 Olympic bronze medals at Paris 2024: 10m air pistol (individual) + 10m air pistol mixed team (with Sarabjot Singh). She is the first Indian to win 2 medals in a single Olympics since <b>Norman Pritchard (1900, 2 silver medals)</b>. She is from Jhajjar, Haryana, coached by Jaspal Rana.</p>

<div class="section-hdr">Key Facts About Gukesh / గుకేశ్ గురించి</div>
<p>D. Gukesh Dommaraju (Chennai) became World Chess Champion in December 2024 at age <b>18</b> — defeating China's Ding Liren in Game 14 in Singapore. He is the youngest World Chess Champion ever, breaking Garry Kasparov's record (22 in 1985).</p>

<div class="section-hdr">National Sports Day / జాతీయ క్రీడా దినం</div>
<p>August 29 — birth anniversary of <b>Major Dhyan Chand</b> (1905-1979), India's greatest hockey player, who won 3 Olympic gold medals (1928, 1932, 1936).</p>

<div class="section-hdr">Quick Exam Facts / పరీక్ష ముఖ్య అంశాలు</div>
<table>
<tr><th>Fact</th><th>Answer</th></tr>
<tr><td>India's highest sports award</td><td>Khel Ratna (formerly Rajiv Gandhi Khel Ratna)</td></tr>
<tr><td>Renamed in</td><td>2021 (to Major Dhyan Chand Khel Ratna)</td></tr>
<tr><td>National Sports Day</td><td>August 29 (Major Dhyan Chand's birthday)</td></tr>
<tr><td>Cash prize</td><td>₹25 lakh</td></tr>
<tr><td>2025 winners (4)</td><td>Gukesh, Harmanpreet Singh, Praveen Kumar, Manu Bhaker</td></tr>
<tr><td>Neeraj Chopra won Khel Ratna</td><td>2021 (NOT 2025)</td></tr>
<tr><td>2nd highest sports award</td><td>Arjuna Award (₹15 lakh)</td></tr>
</table>
"""))

# ─────────────────────────────────────────────
# 7. GOLDEN GLOBE AWARDS
# ─────────────────────────────────────────────
NOTES.append(('golden_globes', 'Golden Globe Awards', 'గోల్డెన్ గ్లోబ్ అవార్డులు', """
<div class="concept-cover">
  <h1>Golden Globe Awards &nbsp;<span class="bi-te">/ గోల్డెన్ గ్లోబ్ అవార్డులు</span></h1>
  <div class="sub">HFPA • Since 1944 • Beverly Hilton, Beverly Hills</div>
</div>

<div class="section-hdr">What are the Golden Globes? / గోల్డెన్ గ్లోబ్ అంటే ఏమిటి?</div>
<p>The Golden Globe Awards are presented by the Hollywood Foreign Press Association (HFPA) and recognise excellence in film and television. Held annually at the Beverly Hilton Hotel, Beverly Hills, California. Since 1944. Unlike the Oscars (film only), the Globes cover both film AND television.</p>
<p class="bi-te">గోల్డెన్ గ్లోబ్ అవార్డులు హాలీవుడ్ ఫారిన్ ప్రెస్ అసోసియేషన్ (HFPA) అందజేస్తుంది. సినిమా మరియు టెలివిజన్ రెండింటికీ అవార్డులు ఇస్తుంది. 1944 నుండి. Beverly Hilton Hotel, Beverly Hills, California.</p>

<div class="section-hdr">83rd Golden Globe Awards — January 11, 2026</div>
<p>Host: <b>Nikki Glaser</b> (second consecutive year — also hosted 82nd in Jan 2025).</p>
<table class="key-table">
<tr><th>Category / విభాగం</th><th>Winner / విజేత</th><th>Note</th></tr>
<tr><td>Best Picture — Drama</td><td><b>Hamnet</b></td><td>Based on Maggie O'Farrell's 2020 novel; Jessie Buckley stars as Agnes Hathaway (Shakespeare's wife)</td></tr>
<tr><td>Best Picture — Comedy/Musical</td><td><b>One Battle After Another</b></td><td>Paul Thomas Anderson; adaptation of Thomas Pynchon's "Gravity's Rainbow"</td></tr>
<tr><td>Best Director</td><td><b>Paul Thomas Anderson</b></td><td>"One Battle After Another" — also won Best Screenplay</td></tr>
<tr><td>Best Actress — Drama</td><td><b>Jessie Buckley</b></td><td>"Hamnet" — swept all major awards</td></tr>
<tr><td>Best Original Song</td><td><b>"Golden"</b></td><td>From animated film "KPop Demon Hunters" (also won Oscar for same)</td></tr>
<tr><td><b>NEW: Best Podcast</b></td><td><b>Good Hang with Amy Poehler</b></td><td>First ever podcast category at Golden Globes</td></tr>
</table>
<p class="bi-te">83వ గోల్డెన్ గ్లోబ్ ముఖ్యాంశాలు: "హామ్నెట్" డ్రామా, "వన్ బ్యాటిల్ ఆఫ్టర్ అనదర్" కామెడీ. కొత్త "బెస్ట్ పాడ్‌కాస్ట్" విభాగం ప్రవేశపెట్టబడింది.</p>

<div class="section-hdr">Key Films of 2026 Awards Season</div>
<table class="key-table">
<tr><th>Film</th><th>Director</th><th>Based On</th></tr>
<tr><td>One Battle After Another</td><td>Paul Thomas Anderson</td><td>Thomas Pynchon's "Gravity's Rainbow" (1973)</td></tr>
<tr><td>Hamnet</td><td>—</td><td>Maggie O'Farrell's novel (2020); Shakespeare's son's story</td></tr>
<tr><td>Sinners</td><td>Ryan Coogler</td><td>Original; Michael B. Jordan plays twin brothers</td></tr>
<tr><td>KPop Demon Hunters</td><td>Sony Animation</td><td>Swept animated film awards 2026</td></tr>
</table>

<div class="section-hdr">Quick Exam Facts / పరీక్ష ముఖ్య అంశాలు</div>
<table>
<tr><th>Fact</th><th>Answer</th></tr>
<tr><td>Presented by</td><td>Hollywood Foreign Press Association (HFPA)</td></tr>
<tr><td>Venue</td><td>Beverly Hilton Hotel, Beverly Hills, CA</td></tr>
<tr><td>Since</td><td>1944</td></tr>
<tr><td>83rd Globes host</td><td>Nikki Glaser (2nd consecutive year)</td></tr>
<tr><td>83rd — Best Picture Drama</td><td>Hamnet</td></tr>
<tr><td>New category 2026</td><td>Best Podcast — won by "Good Hang with Amy Poehler"</td></tr>
<tr><td>Covers</td><td>Both Film AND Television (unlike Oscars)</td></tr>
</table>
"""))

# ─────────────────────────────────────────────
# 8. BAFTA AWARDS
# ─────────────────────────────────────────────
NOTES.append(('bafta_awards', 'BAFTA Film Awards', 'బాఫ్టా అవార్డులు', """
<div class="concept-cover">
  <h1>BAFTA Film Awards &nbsp;<span class="bi-te">/ బాఫ్టా అవార్డులు</span></h1>
  <div class="sub">British Academy of Film and Television Arts • Since 1947 • London</div>
</div>

<div class="section-hdr">What is BAFTA? / BAFTA అంటే ఏమిటి?</div>
<p>BAFTA stands for the <b>British Academy of Film and Television Arts</b>, founded in 1947. The BAFTA Film Awards recognise the best in British and international cinema. Held at the Royal Festival Hall (since 2018), London. Broadcast on BBC One. Often called "the British Oscars."</p>
<p class="bi-te">BAFTA అంటే బ్రిటిష్ అకాడమీ ఆఫ్ ఫిల్మ్ అండ్ టెలివిజన్ ఆర్ట్స్. 1947లో స్థాపించబడింది. లండన్‌లో నిర్వహించబడే బ్రిటిష్ సినిమా పురస్కారాలు. "బ్రిటిష్ ఆస్కార్లు" అని పిలుస్తారు.</p>

<div class="section-hdr">79th BAFTA Film Awards — February 22, 2026</div>
<p>Venue: <b>Royal Festival Hall, London</b>. Host: <b>Alan Cumming</b>. Broadcast: BBC One and iPlayer.</p>
<table class="key-table">
<tr><th>Category / విభాగం</th><th>Winner / విజేత</th><th>Note</th></tr>
<tr><td>Best Film</td><td><b>One Battle After Another</b></td><td>Led with 6 wins total; Paul Thomas Anderson</td></tr>
<tr><td>Outstanding British Film</td><td><b>Hamnet</b></td><td>Based on Maggie O'Farrell's novel</td></tr>
<tr><td>Best Director</td><td><b>Paul Thomas Anderson</b></td><td>"One Battle After Another"</td></tr>
<tr><td>Leading Actor</td><td><b>Robert Aramayo</b></td><td>"I Swear" — beat Timothée Chalamet; known as Elrond in "Rings of Power"</td></tr>
<tr><td>Leading Actress</td><td><b>Jessie Buckley</b></td><td>"Hamnet" — swept all major awards this season</td></tr>
<tr><td>Supporting Actor</td><td><b>Sean Penn</b></td><td>"One Battle After Another" — also won Oscar Supporting Actor (his 3rd Oscar total)</td></tr>
<tr><td>Supporting Actress</td><td><b>Wunmi Mosaku</b></td><td>"Sinners" (Ryan Coogler) — Nigerian-British actress</td></tr>
<tr><td>Film Not in English</td><td><b>Sentimental Value</b></td><td>Norwegian — directed by Joachim Trier</td></tr>
</table>

<div class="section-hdr">About "Sinners" (Ryan Coogler) / సినర్స్ గురించి</div>
<p>"Sinners" received a <b>record 16 Oscar nominations</b> at the 98th Oscars (2026). Michael B. Jordan plays twin brothers. Won 4 Oscars: Best Actor (Jordan), Original Screenplay (Coogler), Cinematography, Film Editing. Wunmi Mosaku won BAFTA Supporting Actress for this film.</p>

<div class="section-hdr">Quick Exam Facts / పరీక్ష ముఖ్య అంశాలు</div>
<table>
<tr><th>Fact</th><th>Answer</th></tr>
<tr><td>Full form</td><td>British Academy of Film and Television Arts</td></tr>
<tr><td>Founded</td><td>1947</td></tr>
<tr><td>79th BAFTA venue</td><td>Royal Festival Hall, London</td></tr>
<tr><td>79th BAFTA host</td><td>Alan Cumming</td></tr>
<tr><td>79th Best Film</td><td>One Battle After Another (6 wins)</td></tr>
<tr><td>Sean Penn's Oscar count</td><td>3 (Mystic River 2003, Milk 2008, One Battle 2026)</td></tr>
<tr><td>"Sinners" Oscar nominations</td><td>16 nominations — record</td></tr>
</table>
"""))

# ─────────────────────────────────────────────
# 9. ACADEMY AWARDS / OSCARS
# ─────────────────────────────────────────────
NOTES.append(('oscars', 'Academy Awards (Oscars)', 'అకాడమీ అవార్డులు (ఆస్కార్లు)', """
<div class="concept-cover">
  <h1>Academy Awards (Oscars) &nbsp;<span class="bi-te">/ ఆస్కార్ అవార్డులు</span></h1>
  <div class="sub">AMPAS • Since 1929 • Dolby Theatre, Hollywood</div>
</div>

<div class="section-hdr">What are the Oscars? / ఆస్కార్ అంటే ఏమిటి?</div>
<p>The Academy Awards (Oscars) are presented by the <b>Academy of Motion Picture Arts and Sciences (AMPAS)</b> — the world's most prestigious film awards. First held in 1929 (for films of 1927-28). Held at the Dolby Theatre, Hollywood, California. The statuette is officially named "Oscar." 23+ categories including Best Picture, Director, Actor, Actress, etc.</p>
<p class="bi-te">ఆస్కార్ అవార్డులు అకాడమీ ఆఫ్ మోషన్ పిక్చర్ ఆర్ట్స్ అండ్ సైన్సెస్ (AMPAS) అందజేస్తుంది. 1929 నుండి ప్రారంభమైంది. హాలీవుడ్‌లోని డాల్బీ థియేటర్‌లో నిర్వహించబడుతుంది. ప్రపంచంలోనే అత్యంత ప్రతిష్ఠాత్మకమైన చలన చిత్ర పురస్కారాలు.</p>

<div class="section-hdr">97th Academy Awards — March 2025 / 97వ ఆస్కార్ అవార్డులు</div>
<table class="key-table">
<tr><th>Category / విభాగం</th><th>Winner / విజేత</th><th>Details</th></tr>
<tr><td>Best Picture</td><td><b>Anora</b></td><td>Sean Baker — indie film; swept 5 Oscars</td></tr>
<tr><td>Best Director</td><td><b>Sean Baker</b></td><td>"Anora"</td></tr>
<tr><td>Best Actor</td><td><b>Adrien Brody</b></td><td>"The Brutalist" — his 2nd Best Actor Oscar (first: The Pianist 2002)</td></tr>
<tr><td>Best Actress</td><td><b>Mikey Madison</b></td><td>"Anora" — plays a NY sex worker who marries a Russian oligarch's son</td></tr>
<tr><td>Best Int'l Film</td><td><b>I'm Still Here</b></td><td>Brazil — Fernando Meirelles</td></tr>
</table>
<p class="bi-te">97వ ఆస్కార్: "అనోరా" బెస్ట్ పిక్చర్; అడ్రియన్ బ్రోడీ 2వ బెస్ట్ యాక్టర్ ("ది బ్రూటలిస్ట్"); మికీ మాడిసన్ బెస్ట్ యాక్ట్రెస్.</p>

<div class="section-hdr">98th Academy Awards — March 2026 / 98వ ఆస్కార్ అవార్డులు</div>
<table class="key-table">
<tr><th>Category / విభాగం</th><th>Winner / విజేత</th><th>Details</th></tr>
<tr><td>Best Picture</td><td><b>One Battle After Another</b></td><td>Paul Thomas Anderson — 6 wins; Pynchon's "Gravity's Rainbow" adaptation</td></tr>
<tr><td>Best Director</td><td><b>Paul Thomas Anderson</b></td><td>"One Battle After Another"</td></tr>
<tr><td>Best Actor</td><td><b>Michael B. Jordan</b></td><td>"Sinners" — plays twin brothers; 16 nominations (record)</td></tr>
<tr><td>Best Actress</td><td><b>Jessie Buckley</b></td><td>"Hamnet" — Grand Slam sweep (SAG + Globes + BAFTA + Oscar)</td></tr>
<tr><td>Best Supporting Actor</td><td><b>Sean Penn</b></td><td>"One Battle After Another" — his 3rd Oscar total</td></tr>
<tr><td>Best Supporting Actress</td><td><b>Amy Madigan</b></td><td><b>"Weapons"</b> (Gabriel Abrantes) — NOT "One Battle"</td></tr>
<tr><td>Animated Feature</td><td><b>KPop Demon Hunters</b></td><td>Sony Animation; also won Best Original Song "Golden"</td></tr>
<tr><td>Best Visual Effects</td><td><b>Avatar: Fire and Ash</b></td><td>3rd Avatar film (James Cameron); 3rd consecutive VFX Oscar for Avatar</td></tr>
<tr><td>Int'l Feature Film</td><td><b>Sentimental Value</b></td><td>Norway — Joachim Trier</td></tr>
<tr><td>NEW: Best Casting</td><td><b>One Battle After Another</b></td><td>Inaugural category — first ever casting Oscar winner</td></tr>
</table>
<p><b>Record:</b> "Sinners" had 16 Oscar nominations — breaking the previous record of 14 (Titanic 1997 + All About Eve 1950). Won 4 Oscars.</p>
<p class="bi-te">98వ ఆస్కార్: "వన్ బ్యాటిల్" 6 అవార్డులు (బెస్ట్ పిక్చర్ తో సహా); "సినర్స్" 16 నామినేషన్లు (రికార్డు), 4 అవార్డులు. ఆమీ మాడిగన్ "వెపన్స్"కు సపోర్టింగ్ యాక్ట్రెస్.</p>

<div class="section-hdr">Jessie Buckley's Grand Slam / గ్రాండ్ స్లామ్</div>
<p>"Grand Slam" in acting means winning all four major film awards in the same season: <b>SAG Awards + Golden Globes + BAFTA + Academy Awards</b>. Jessie Buckley achieved this for "Hamnet" in the 2025-26 awards season — an extremely rare feat.</p>

<div class="section-hdr">India at the Oscars / ఆస్కార్‌లో భారత్</div>
<table class="key-table">
<tr><th>Film / Person</th><th>Year</th><th>Category</th></tr>
<tr><td>Mother India</td><td>1958</td><td>First Indian nomination (Best Foreign Film)</td></tr>
<tr><td>Salaam Bombay!</td><td>1989</td><td>Best Foreign Language Film nomination</td></tr>
<tr><td>Lagaan</td><td>2002</td><td>Best Foreign Language Film nomination</td></tr>
<tr><td>RRR — "Naatu Naatu"</td><td>2023</td><td><b>WON Best Original Song</b></td></tr>
<tr><td>A.R. Rahman</td><td>2009</td><td>Won 2 Oscars for Slumdog Millionaire</td></tr>
</table>

<div class="section-hdr">Quick Exam Facts / పరీక్ష ముఖ్య అంశాలు</div>
<table>
<tr><th>Fact</th><th>Answer</th></tr>
<tr><td>Full form</td><td>Academy of Motion Picture Arts and Sciences (AMPAS)</td></tr>
<tr><td>First Oscars</td><td>1929 (for films of 1927-28)</td></tr>
<tr><td>Venue</td><td>Dolby Theatre, Hollywood, California</td></tr>
<tr><td>98th Best Picture</td><td>One Battle After Another (PTA)</td></tr>
<tr><td>98th Best Actor</td><td>Michael B. Jordan — "Sinners"</td></tr>
<tr><td>India's first Oscar win</td><td>A.R. Rahman — 2009 (Slumdog Millionaire)</td></tr>
<tr><td>RRR Oscar win</td><td>Best Original Song — "Naatu Naatu" (2023)</td></tr>
<tr><td>New category at 98th Oscars</td><td>Best Casting</td></tr>
</table>
"""))

# ─────────────────────────────────────────────
# 10. PADMA AWARDS
# ─────────────────────────────────────────────
NOTES.append(('padma_awards', 'Padma Awards', 'పద్మ పురస్కారాలు', """
<div class="concept-cover">
  <h1>Padma Awards &nbsp;<span class="bi-te">/ పద్మ పురస్కారాలు</span></h1>
  <div class="sub">India's Highest Civilian Honours • Since 1954 • Republic Day</div>
</div>

<div class="section-hdr">What are Padma Awards? / పద్మ పురస్కారాలు అంటే ఏమిటి?</div>
<p>The Padma Awards are among India's highest civilian honours, awarded annually on the occasion of Republic Day (January 26). They recognise distinguished service in various fields — arts, education, science, sports, social service, public affairs, etc. Three tiers:</p>
<ul>
<li><b>Padma Vibhushan</b> — 2nd highest civilian honour (exceptional and distinguished service)</li>
<li><b>Padma Bhushan</b> — 3rd highest (distinguished service of a high order)</li>
<li><b>Padma Shri</b> — 4th highest (distinguished service in any field)</li>
</ul>
<p class="bi-te">పద్మ పురస్కారాలు భారత్‌లోని అత్యున్నత పౌర పురస్కారాలు. జనవరి 26 (గణతంత్ర దినం) సందర్భంగా ప్రకటించబడతాయి. మూడు స్థాయిలు: పద్మ విభూషణ్, పద్మ భూషణ్, పద్మ శ్రీ.</p>

<div class="section-hdr">Padma Awards 2026 — Key Winners / 2026 పద్మ పురస్కారాలు</div>
<p>Total: <b>131 awards</b> announced January 25, 2026 (Republic Day eve).</p>
<table class="key-table">
<tr><th>Award</th><th>Recipient / గ్రహీత</th><th>Field / రంగం</th></tr>
<tr><td>Padma Vibhushan</td><td><b>Dharmendra Singh Deol</b> (posthumous)</td><td>Cinema — "He-Man of Bollywood"; Sholay (1975)</td></tr>
<tr><td>Padma Vibhushan</td><td><b>VS Achuthanandan</b> (posthumous)</td><td>Public Affairs — former Kerala CM (2006-11), CPI-M; died 2025 at ~101</td></tr>
<tr><td>Padma Vibhushan</td><td>3 more recipients</td><td>Various fields</td></tr>
<tr><td>Padma Bhushan</td><td><b>Vijay Amritraj</b></td><td>Sports (Tennis) — world No. 18 in 1970s-80s; Davis Cup; appeared in James Bond film 'Octopussy' (1983)</td></tr>
<tr><td>Padma Shri</td><td><b>Rohit Sharma</b></td><td>Cricket — India Test/ODI captain</td></tr>
<tr><td>Padma Shri</td><td><b>Harmanpreet Kaur</b></td><td>Cricket — India women's captain</td></tr>
<tr><td>Padma Shri</td><td><b>Savita Punia</b></td><td>Hockey — India women's goalkeeper</td></tr>
<tr><td>Padma Shri</td><td>109 more recipients</td><td>Various fields</td></tr>
</table>
<p class="bi-te">2026 పద్మ విభూషణ్: ధర్మేంద్ర (మరణానంతరం), VS అచ్యుతానందన్ (మరణానంతరం). పద్మ భూషణ్: విజయ్ అమృతరాజ్ (టెన్నిస్). పద్మ శ్రీ: రోహిత్ శర్మ, హర్మన్‌ప్రీత్ కౌర్, సవిత పూనియా.</p>

<div class="section-hdr">Bharat Ratna 2025 / భారత రత్న 2025</div>
<p>Bharat Ratna is India's highest civilian award (above all Padma awards). 2025 recipients:</p>
<table class="key-table">
<tr><th>Recipient / గ్రహీత</th><th>Contribution / కృషి</th></tr>
<tr><td><b>Narayana Murthy</b></td><td>Co-founder of Infosys — father of India's IT industry. Built Infosys into a global giant from ₹10,000 capital (1981). Revolutionised software exports from India.</td></tr>
<tr><td><b>Ratan Tata</b> (posthumous)</td><td>Chairman Emeritus of Tata Group — died October 2024. Transformed Tata Group into a global conglomerate; acquired Jaguar Land Rover (2008), Corus Steel. Known for philanthropy and ethics.</td></tr>
</table>
<p class="bi-te">భారత రత్న 2025: నారాయణ మూర్తి (ఇన్ఫోసిస్ వ్యవస్థాపకుడు — భారత IT పరిశ్రమ పితామహుడు) మరియు రతన్ టాటా (మరణానంతరం — అక్టోబర్ 2024లో మరణించారు, టాటా గ్రూప్ ను ప్రపంచ స్థాయికి తీసుకెళ్ళారు).</p>

<div class="section-hdr">Civilian Awards Hierarchy / పౌర పురస్కారాల క్రమం</div>
<table class="key-table">
<tr><th>Rank</th><th>Award / పురస్కారం</th><th>Note</th></tr>
<tr><td>1st</td><td><b>Bharat Ratna</b> (భారత రత్న)</td><td>Highest civilian honour</td></tr>
<tr><td>2nd</td><td>Padma Vibhushan</td><td>Exceptional &amp; distinguished service</td></tr>
<tr><td>3rd</td><td>Padma Bhushan</td><td>Distinguished service of high order</td></tr>
<tr><td>4th</td><td>Padma Shri</td><td>Distinguished service in any field</td></tr>
</table>

<div class="section-hdr">Padma Awards — Key Facts / ముఖ్య అంశాలు</div>
<p>Padma Awards were instituted in 1954. Discontinued between 1977-80 and 1993-97. Cannot be used as a suffix/prefix to names. Awarded posthumously (with exceptions). Foreigners can also be awarded Padma awards (called "Honorary" awards).</p>
<p class="bi-te">పద్మ పురస్కారాలు 1954లో ప్రారంభమయ్యాయి. పేరుకు ముందు/వెనుక ఉపయోగించలేరు. విదేశీయులకు కూడా "గౌరవ" పురస్కారంగా ఇవ్వవచ్చు.</p>

<div class="section-hdr">Quick Exam Facts / పరీక్ష ముఖ్య అంశాలు</div>
<table>
<tr><th>Fact</th><th>Answer</th></tr>
<tr><td>Instituted</td><td>1954</td></tr>
<tr><td>Announced on</td><td>Republic Day (January 26)</td></tr>
<tr><td>Highest civilian honour</td><td>Bharat Ratna (above all Padma awards)</td></tr>
<tr><td>2026 Padma Vibhushan (notable)</td><td>Sharad Pawar, Osamu Suzuki (posthumous), Sharda Sinha (posthumous)</td></tr>
<tr><td>Osamu Suzuki significance</td><td>Brought Maruti-Suzuki to India; transformed Indian auto industry</td></tr>
<tr><td>Discontinued periods</td><td>1977-80 and 1993-97</td></tr>
</table>
"""))

# ─────────────────────────────────────────────
# 11. BHARAT RATNA
# ─────────────────────────────────────────────
NOTES.append(('other_awards', 'Other Notable Awards 2025-26', 'ఇతర ముఖ్య పురస్కారాలు 2025-26', """
<div class="concept-cover">
  <h1>Other Notable Awards 2025-26 &nbsp;<span class="bi-te">/ ఇతర ముఖ్య పురస్కారాలు</span></h1>
  <div class="sub">Abel • Pritzker • Phalke • Turing • FIFA • Sakharov • Indira Gandhi Prize</div>
</div>

<div class="section-hdr">Abel Prize 2025 — Mathematics / ఆబెల్ పురస్కారం</div>
<table class="key-table">
<tr><th>Winner / విజేత</th><th>Country</th><th>For / కారణం</th></tr>
<tr><td><b>Masaki Kashiwara</b></td><td>Japan (RIMS, Kyoto)</td><td>D-module theory and Riemann-Hilbert correspondence. First Japanese mathematician to win the Abel Prize.</td></tr>
</table>
<p>Abel Prize = mathematics' equivalent of Nobel. Awarded by the Norwegian Academy of Science and Letters. Prize: NOK 7.5 million (~$700,000). Abel Prize 2024: Michel Talagrand (France, probability theory).</p>
<p class="bi-te">ఆబెల్ పురస్కారం 2025: మసాకీ కాషివారా (జపాన్) — D-మాడ్యూల్ సిద్ధాంతానికి. ఆబెల్ పురస్కారం గణిత శాస్త్రంలో నోబెల్ సమానమైనది.</p>

<div class="section-hdr">Pritzker Architecture Prize 2025 / ప్రిట్జ్కర్ పురస్కారం</div>
<table class="key-table">
<tr><th>Winner</th><th>Country</th><th>Note</th></tr>
<tr><td><b>Liu Jiakun</b></td><td>China</td><td>First Chinese national since Wang Shu (2012). Known for community-centred architecture and post-earthquake Sichuan reconstruction (2008). Pritzker = "architecture's Nobel Prize" — $100,000, by Hyatt Foundation.</td></tr>
</table>
<p class="bi-te">ప్రిట్జ్కర్ 2025: లియు జియాకున్ (చైనా) — సాంప్రదాయం మరియు ఆధునికత మేళవింపు ఆర్కిటెక్చర్‌కు.</p>

<div class="section-hdr">Dadasaheb Phalke Award 2025 / దాదాసాహేబ్ ఫాల్కే పురస్కారం</div>
<table class="key-table">
<tr><th>Winner / విజేత</th><th>Field</th><th>Known For</th></tr>
<tr><td><b>Rekha</b> (Bhanurekha Ganesan)</td><td>Cinema / సినిమా</td><td>Umrao Jaan (1981), Silsila (1981), Khubsoorat (1980). India's highest film honour — given at National Film Awards. Previous: Asha Parekh (2024), Waheeda Rehman (2023).</td></tr>
</table>
<p>Dadasaheb Phalke (1870-1944) = Father of Indian Cinema — made India's first full-length feature film "Raja Harishchandra" (1913).</p>
<p class="bi-te">దాదాసాహేబ్ ఫాల్కే 2025: రేఖా (భానురేఖ గణేశన్) — భారతీయ చలన చిత్ర పరిశ్రమలో అత్యున్నత పురస్కారం.</p>

<div class="section-hdr">Ramon Magsaysay Award / రామన్ మగ్సాసే పురస్కారం</div>
<p>Called "Asia's Nobel Prize." Presented in <b>Manila, Philippines</b> — named after Philippine President Ramon Magsaysay (1907-1957). Prize: $50,000. Categories: Government Service, Public Service, Community Leadership, Journalism/Literature/Creative Arts, Peace &amp; International Understanding.</p>
<p class="bi-te">రామన్ మగ్సాసే అవార్డు "ఆసియా నోబెల్ పురస్కారం" అని పిలుస్తారు. మానిలా, ఫిలిప్పైన్స్‌లో అందజేయబడుతుంది.</p>

<div class="section-hdr">ACM Turing Award 2025 — Computing / ట్యూరింగ్ పురస్కారం</div>
<p>ACM A.M. Turing Award = computing's highest honour. Prize: <b>$1 million</b> (sponsored by Google). Awarded by Association for Computing Machinery (ACM). Named after Alan Turing. Turing Award 2025: For pioneering computer graphics and rendering algorithms. Turing Award 2024: Andrew Barto &amp; Richard Sutton (reinforcement learning).</p>
<p class="bi-te">ట్యూరింగ్ అవార్డు కంప్యూటింగ్‌లో అత్యున్నత పురస్కారం. $1 మిలియన్ నగద బహుమతి.</p>

<div class="section-hdr">FIFA Best Awards 2025 / FIFA బెస్ట్ అవార్డులు 2025</div>
<table class="key-table">
<tr><th>Category</th><th>Winner</th><th>Note</th></tr>
<tr><td>Best Men's Player</td><td><b>Ousmane Dembélé</b> (PSG)</td><td>Same as Ballon d'Or 2025 — PSG's historic quadruple season</td></tr>
<tr><td>Best Women's Player</td><td><b>Aitana Bonmatí</b> (Barcelona)</td><td>Third consecutive (also 2023, 2024)</td></tr>
<tr><td>Best Men's Coach</td><td><b>Luis Enrique</b> (PSG)</td><td>Managed PSG to the 2024-25 quadruple</td></tr>
<tr><td>Best Women's Coach</td><td><b>Sarina Wiegman</b> (England)</td><td>Also won Ballon d'Or Best Coach 2025</td></tr>
<tr><td>Best Goalkeeper</td><td><b>Gianluigi Donnarumma</b> (PSG)</td><td>Italy's no.1 GK</td></tr>
</table>
<p>FIFA Best Awards ceremony: January 2026.</p>
<p class="bi-te">FIFA బెస్ట్ 2025: డెంబేలే (పురుషులు), బోన్‌మాటి (మహిళలు), లూయిస్ ఎన్‌రిక్ (పురుష కోచ్), సారీనా వైగ్‌మన్ (మహిళా కోచ్).</p>

<div class="section-hdr">Sakharov Prize 2025 — European Parliament / సఖారోవ్ పురస్కారం</div>
<p>Sakharov Prize for Freedom of Thought — awarded by the European Parliament annually since 1988. Prize: €50,000. Named after Soviet physicist and dissident Andrei Sakharov.</p>
<p>Sakharov Prize 2025: Awarded to Iranian women human rights defenders of the <b>"Woman, Life, Freedom" (Zan, Zendegi, Azadi)</b> movement — sparked by Mahsa Amini's death in Iranian police custody (September 2022).</p>
<p class="bi-te">సఖారోవ్ 2025: ఇరాన్ మహిళా హక్కుల రక్షకులకు — "మహిళ, జీవితం, స్వేచ్ఛ" ఉద్యమం.</p>

<div class="section-hdr">Indira Gandhi Peace Prize 2025 / ఇందిరా గాంధీ శాంతి పురస్కారం</div>
<table class="key-table">
<tr><th>Winner / విజేత</th><th>Reason / కారణం</th></tr>
<tr><td><b>GAVI, the Vaccine Alliance</b></td><td>Global health — vaccinated 1 billion+ children in low-income countries; key role in COVID-19 COVAX facility. Previous: WHO (2022), Manmohan Singh (2024).</td></tr>
</table>
<p>Indira Gandhi Prize for Peace, Disarmament and Development — awarded by Indira Gandhi Memorial Trust, New Delhi.</p>
<p class="bi-te">ఇందిరా గాంధీ శాంతి పురస్కారం 2025: GAVI వాక్సిన్ అలయన్స్ — 100 కోట్లు పైగా పిల్లలకు టీకాలు వేసిన సేవకు.</p>

<div class="section-hdr">Quick Exam Facts / పరీక్ష ముఖ్య అంశాలు</div>
<table>
<tr><th>Award</th><th>Key Fact</th></tr>
<tr><td>Abel Prize</td><td>Mathematics Nobel — Norway — Masaki Kashiwara 2025 (first Japanese)</td></tr>
<tr><td>Pritzker Prize</td><td>Architecture Nobel — Hyatt Foundation — Liu Jiakun 2025</td></tr>
<tr><td>Dadasaheb Phalke 2025</td><td>Rekha — India's highest film honour</td></tr>
<tr><td>Ramon Magsaysay</td><td>Asia's Nobel — Manila, Philippines — $50,000</td></tr>
<tr><td>Turing Award</td><td>Computing Nobel — ACM — $1 million (Google) — named after Alan Turing</td></tr>
<tr><td>FIFA Best 2025 Men's</td><td>Ousmane Dembélé (PSG)</td></tr>
<tr><td>Sakharov Prize 2025</td><td>Iranian "Woman, Life, Freedom" movement — European Parliament</td></tr>
<tr><td>Indira Gandhi Peace 2025</td><td>GAVI, the Vaccine Alliance</td></tr>
</table>
"""))

# ════════════════════════════════════════════════════════════════
#  DATABASE INSERT
# ════════════════════════════════════════════════════════════════

if USE_POSTGRES:
    cur = conn.cursor()
    cur.execute("DELETE FROM concept_notes")
    for tag, label, label_te, html in NOTES:
        cur.execute(
            "INSERT INTO concept_notes (tag, label, label_te, html) VALUES (%s, %s, %s, %s)",
            (tag, label, label_te, html.strip())
        )
    conn.commit()
    cur.close()
else:
    conn.execute("DELETE FROM concept_notes")
    for tag, label, label_te, html in NOTES:
        conn.execute(
            "INSERT INTO concept_notes (tag, label, label_te, html) VALUES (?, ?, ?, ?)",
            (tag, label, label_te, html.strip())
        )
    conn.commit()

conn.close()
print(f"SUCCESS: Seeded {len(NOTES)} concept notes into DB.")
for tag, label, *_ in NOTES:
    print(f"  • {tag:20s} — {label}")
