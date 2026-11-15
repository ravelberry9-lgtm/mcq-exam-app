# Chapter 3 (Solar System) — fact coverage

Source: ch03/FINAL/lesson_03_rebuilt.md — 838 `::: fact` blocks, numbered F001–F838 in lesson order (see facts.txt). Existing = mcq03/FINAL/solar_bilingual.patched.json (531 original + 7 historical), matched to facts by meaning; section from links.json. Ids are shortened: `P004-F010` = GEO-BOOK-P004-F010, `SP-005` = SOLAR-PRACTICE-005, `EXT-0159` = APPSC-EXT-0159. New = new_questions.json (GEO-NEW-03-xxx).


## Totals

- Facts: 838. Already tested by existing questions: 442. Previously untested facts now covered by new questions: 349. Left without a question: 47 (all with a reason in the Note column; unexplained: 0).
- New questions: 163. Answer key spread: A=41, B=41, C=41, D=40.
- Format mix: single 86, statement 37, match 31, assertion-reason 5, sequence 4. Assertion–reason keys: A=1, B=1, C=2, D=1.
- Validator (build.py): 0 length flags (correct option at least 30% longer than the mean distractor, TE and EN), 0 errors, 0 warnings.

## How the mapping was done

- Every `::: fact` line was read against every existing question in its lesson section and neighbouring sections (stem, options, key; match questions judged by their section and list topic, so a few of their pairs may test facts marked "—") and matched by meaning; "(partial)" means only part of the fact is tested; "(explanation)" means it appears only in an explanation.
- New questions were written only for facts with no existing test, or where the existing test missed the exam-relevant part (e.g. Pluto: which IAU condition it fails; Ceres vs Vesta as "largest asteroid").
- Each new question lists its facts (`_facts` in the q_*.py sources); several facts per question via statement and match formats. `chapter_excerpt` (te) holds the lesson fact lines tested, word for word.

## "How to answer in the exam" questions (definition-dependent or changed classifications)

- N021, N022, N057, N064, N074, N090, N103, N107, N161: these now ask the fact directly, with the defining condition in the stem (no quoted-question wrappers): nearest galaxy regardless of size (N021); closest planet by average distance (N022); which IAU condition Pluto fails (N057); IAU 2015 nominal solar temperature, with the old 5778 K key in the explanation (N064); Venus day vs year (N074); largest asteroid once Ceres counts as a dwarf planet (N090); coldest planet by 1-bar mean (N103); minus sign in rotation tables (N107); axis angle with the orbital plane (N161).

## Validator results (build.py)

- Length check, TE and EN: correct option never ≥30% longer than the mean distractor and never the strictly longest option — 0 flags (71 + 98 found in the first pass, all rebalanced).
- Key patterns: match keys never in list order or reverse order; 13 distinct keys over 31 match questions (most frequent 4×); sequence keys never 1-2-3-4; assertion–reason keys A=1, B=1, C=2, D=1; answers A=41, B=41, C=41, D=40.
- Giveaway checks: absolute words (only/always/never/all/every/any; ఎప్పుడూ/అన్నీ/ఏ ఒక్క) in distractors or statements — 0; a capitalised stem word or year appearing in exactly one option (checked on the English stem) — 0; key breaking the option template (ending word, opening word, semicolon, digits, brackets, hedge) while the three distractors agree — 0; no ×, ÷ or = in any explanation or option explanation (TE and EN); no Telugu script in English fields; negative stems carry NOT / **bold**; 4 options and 4 option explanations, exactly one marked సరైనది / Correct; learning tables 3–8 rows, uniform width.

## Why/how question per section

- 137 of 164 fact sections have at least one why/how/how-to-answer question (new or existing; ids below). 
- 27 sections have none. They are list-type sections (missions, records, names, dates) where a why/how would be artificial: address-spheres (7), universe-galaxy (3), universe-milky-way (7), distances-nearest-star (4), sky-astrology (4), stars-main-sequence (6), stars-sun-future (3), stars-black-hole-history (3), stars-quasar (4), formation-schmidt-weizsacker (5), inner-rocky (5), inner-motion (5), inner-mars-features (5), outer-jupiter (5), small-bodies-impacts-missions (5), compare-distance (3), compare-records-size (4), compare-records-moons (2), moon-chandrayaan (11), tides-uses (5), history-planet-names (8), history-astronomy-terms (6), missions-satellite-payload (6), missions-aditya (5), missions-mars (6), missions-voyager-new-horizons (6), missions-venus-orbiter (3).

| Section | Why/how question(s) |
|---|---|
| address-geography | P002-F008 |
| address-geographers | N002 |
| address-spheres | — |
| address-our-address | SP-004 |
| universe-what | P002-F016 |
| universe-galaxy | — |
| universe-milky-way | — |
| universe-nebula | P003-F006 |
| universe-theories | P003-F001 |
| universe-bigbang | N007 (sequence) |
| universe-redshift | P003-F002 |
| universe-cmb | N010 |
| universe-steady-state | N011 |
| universe-oscillating-inflation | P003-F025 |
| universe-dark | P003-F010 |
| distances-units | SP-001 |
| distances-au | SP-002 |
| distances-light-time | SP-003, N015 |
| distances-light-year | N016 |
| distances-parallax | N017 |
| distances-parsec | N019, SP-077 |
| distances-nearest-star | — |
| distances-nearest-galaxy | N021 |
| distances-closest-planet | N022, SP-005 |
| sky-star-planet | N023 |
| sky-constellation | SP-006 |
| sky-asterism | P004-F007 |
| sky-polaris | N026 |
| sky-brightness | N028 |
| sky-brightest | P004-F071 |
| sky-inferior-superior | N030 |
| sky-ecliptic-zodiac | N032 |
| sky-astrology | — |
| stars-birth | N033 |
| stars-main-sequence | — |
| stars-end-paths | N035 |
| stars-red-giant-white-dwarf | N036 |
| stars-sun-future | — |
| stars-chandrasekhar | N039 |
| stars-dwarfs | N040 |
| stars-binary-nova | SP-085 |
| stars-supernova | N042 |
| stars-neutron-pulsar | P010-F014 |
| stars-quark-star | P010-F015 |
| stars-black-hole | P011-F007 |
| stars-black-hole-history | — |
| stars-quasar | — |
| formation-nebular-model | N048, SP-007 |
| formation-rocky-giant | N049 |
| formation-ages | N051 |
| formation-hypotheses | N052 |
| formation-kant-laplace | N053 |
| formation-encounter | N054 |
| formation-schmidt-weizsacker | — |
| formation-planet-definition | N056, SP-011 |
| formation-pluto-reclassification | N057 |
| sun-what | P006-F012 |
| sun-fusion | N061 |
| sun-interior | N062, P006-F016 |
| sun-atmosphere | N063, SP-017 |
| sun-temperature-exam | N064 |
| sun-spectrum | N066 |
| sun-sunspots-cycle | N067 |
| sun-wind-flare-cme | SP-018 |
| sun-storms-aurora | P007-F004 |
| inner-rocky | — |
| inner-motion | — |
| inner-mercury | N071 |
| inner-venus | P007-F021 |
| inner-greenhouse | SP-020, N075 |
| inner-earth | N076 |
| inner-earth-shape | N158 |
| inner-mars | P008-F007, N078 |
| inner-mars-features | — |
| inner-compare | SP-024 |
| outer-giants | N080 |
| outer-colours | P008-F019 |
| outer-rings | P008-F015 |
| outer-jupiter | — |
| outer-galilean | N083, N084 |
| outer-saturn | N159 |
| outer-uranus | N157 |
| outer-neptune | N160 |
| outer-moon-counts | SP-029 |
| asteroid-belt | N088 |
| ceres | N090 |
| kuiper | P010-F007 |
| oort | N093 |
| comet-structure | N094 |
| comet-tails | P009-F012 |
| halley | P009-F016 |
| sl9 | N096 |
| meteor-stages | N163 |
| small-bodies-compare | N162 |
| meteor-shower | SP-035 |
| small-bodies-impacts-missions | — |
| compare-mass-weight | N101, SP-047 |
| compare-diameter | SP-048, N077 |
| compare-size | SP-083 |
| compare-motion | N071, N074 |
| compare-distance | — |
| compare-checklist | N102 |
| compare-records-size | — |
| compare-records-density | N102, N159 |
| compare-records-temperature | N103, N104 |
| compare-records-spin | SP-094 |
| compare-records-moons | — |
| motion-rotation-revolution | P024-F011 |
| motion-sidereal-solar-day | N106 |
| motion-retrograde-rotation | N107 |
| motion-same-direction | N108 |
| motion-mercury-venus-day | N074 |
| motion-kepler-laws | SP-041, SP-042 |
| motion-why-orbit | N110 |
| motion-perihelion-aphelion | N111 |
| seasons-tilt | N161 |
| seasons-cause | SP-049 |
| seasons-dates | N114 |
| seasons-equinox-day | N115 |
| seasons-vijayawada | N116, SP-052 |
| seasons-ap-heat | N117 |
| seasons-distance | SP-053 |
| moon-size | N118 |
| moon-gravity | N119, P022-F009 |
| moon-origin | N120 (theory match) |
| moon-phases | SP-055, SP-060 |
| moon-month | N122 |
| moon-oneface | N123, SP-058 |
| moon-surface | P022-F021 |
| moon-chandrayaan | — |
| eclipse-what | P024-F012 |
| eclipse-not-monthly | SP-062, N126 |
| eclipse-shadow-parts | N127 |
| eclipse-solar-types | SP-064 |
| eclipse-lunar-types | N129 |
| eclipse-safety | SP-066 |
| eclipse-saros-count | P024-F008, P024-F010 |
| eclipse-phases-vs | SP-072 |
| tides-what | SP-067 |
| tides-moon-vs-sun | N132 |
| tides-two-a-day | N133 |
| tides-spring-neap | N134 |
| tides-range-calc | N135, SP-070 |
| tides-local-factors | N136 (explanation) |
| tides-storm-surge | SP-071 |
| tides-uses | — |
| tides-phases-eclipse | SP-072 |
| history-geocentric | N139, P012-F012 |
| history-indian | P012-F015 |
| history-heliocentric | N142 |
| history-galileo | P012-F018 |
| history-kepler-newton | N144, P012-F019 |
| history-planet-names | — |
| history-astronomy-terms | — |
| history-who-first | N147 |
| missions-types | N148 |
| missions-satellite-payload | — |
| missions-l1 | N150 |
| missions-aditya | — |
| missions-sun-international | SP-090 |
| missions-mars | — |
| missions-dart | N154, P009-F007 |
| missions-voyager-new-horizons | — |
| missions-venus-orbiter | — |

## Notes for the editor

- Ids: N001–N163 below = GEO-NEW-03-001 … 163. Sections in new questions use the lesson anchors directly (e.g. `outer-saturn`); `link` is `#section`.
- Facts outside the lesson used only in distractors/explanations (all standard): Delhi ≈ 28.6°N (N026 table), Mercury mean surface 167°C (from the existing bank, N103), IMD season months (N112 table), Hawking had no Nobel (N045). No numbers were invented; arithmetic (parallax 0.3″ → 3.3 pc, 60 kg → 588 N / 96 N, tide 6:00 → 6:50, range 1.8 − (−0.3) = 2.1 m, inverse square 1/9) was checked by hand.
- N156 (Venus Orbiter Mission) carries an as-of date (November 2026) because launch dates can move.
- GEO-BOOK-P004-M007 rewrite is in m007_fix.json (key unchanged; List II gains a fifth value, 38.8 AU, used by two sorted-order trap options so the item cannot be solved by sorting numbers).

## Fact-by-fact table

| Fact | Section | Fact (short) | Existing | New | Note |
|---|---|---|---|---|---|
| F001 | address-geography | Geography అనే పదం గ్రీకు భాషలోని Geo (భూమి), Graphein (వర్ణించడం) అనే పదాల నుంచి… | P002-F001 | — |  |
| F002 | address-geography | భూగోళశాస్త్రం ప్రదేశాలు (Places), అవి పరుచుకున్న తీరు (Spatial patterns), వాటిని… | P002-F002 | — |  |
| F003 | address-geography | ప్రకృతి వ్యవస్థలను చదివేది Physical geography; జనాభా, నివాసాలు, ఆర్థిక కార్యకలాప… | P002-F008, F009, M001 | — |  |
| F004 | address-geographers | Geography అనే పదాన్ని పుస్తకం పేరుగా వాడి, నీడ కోణంతో భూమి చుట్టుకొలతను అంచనా వే… | P002-F003 | N001 |  |
| F005 | address-geographers | Anthropogeographie గ్రంథ రచయిత Friedrich Ratzel; ఆయనను Father of Human geography… | P002-F019 | — |  |
| F006 | address-geographers | Environmental determinism (పర్యావరణ నిర్ణయవాదం) Ratzel ఆలోచనలతో ముడిపడి ఉంది; Po… | P002-F020 (Vidal only) | N001 |  |
| F007 | address-geographers | Areal differentiation ఆలోచన Richard Hartshorne ది. | — | N001 |  |
| F008 | address-geographers | Eratosthenes Alexandria లో నీడ కోణం సుమారు 7.2° కొలిచాడు; 360 ÷ 7.2 = 50. | — | N002 |  |
| F009 | address-geographers | Perspective on the Nature of Geography (1959) గ్రంథ రచయిత Richard Hartshorne. | P002-F021 | N001 |  |
| F010 | address-spheres | Crust (భూపటలం), దాని కింద ఉన్న Mantle పై భాగం కలిసిన గట్టి రాతి పొరను Lithospher… | P002-F004 | — |  |
| F011 | address-spheres | భూమి లోపలి పొరలు పై నుంచి లోపలికి: Crust, Mantle, Outer core (ద్రవం), Inner core… | — | N003 |  |
| F012 | address-spheres | భూమి ఉపరితలంలో సుమారు 71% నీరు; ఆ నీటిలో సుమారు 97% సముద్రాల్లో ఉంది. | P007-F022 (71% only) | N003 |  |
| F013 | address-spheres | Atmosphere లో సుమారు 78% Nitrogen, 21% Oxygen ఉంటాయి. | P002-M002 (partial) | N003 |  |
| F014 | address-spheres | ద్రవం, మంచు, ఆవిరి రూపాల్లో భూమిపై ఉన్న మొత్తం నీటిని Hydrosphere (జలమండలం) అంటా… | P002-F005 | — |  |
| F015 | address-spheres | భూమిని ఆవరించిన వాయువుల పొరను Atmosphere (వాయుమండలం) అంటారు. | P002-F006 | — |  |
| F016 | address-spheres | జీవులు, అవి నివసించే ప్రాంతాలు కలిసిన మండలాన్ని Biosphere (జీవమండలం) అంటారు. | P002-F007 | — |  |
| F017 | address-our-address | మన చిరునామా క్రమం: Earth → Solar System → Milky Way → Local Group → Laniakea Sup… | SP-004 | — |  |
| F018 | address-our-address | Solar System లో ఎనిమిది గ్రహాలు ఉన్నాయి; Pluto ను 2006 లో IAU Dwarf planet గా మా… | P005-F003, P010-F006 | — |  |
| F019 | address-our-address | సూర్యుడు, అతని చుట్టూ తిరిగే గ్రహాలు, వాటి చంద్రులు, Dwarf planets, Asteroids, C… | SP-004 (implicit) | — |  |
| F020 | address-our-address | మన Solar System ఉన్న Galaxy పేరు Milky Way (పాలపుంత). | P003-F008 | — |  |
| F021 | universe-what | విశ్వం (Universe) వయస్సు సుమారు 1,380 కోట్ల సంవత్సరాలు (13.8 billion years). | P002-F011, SP-073 | — |  |
| F022 | universe-what | సౌర కుటుంబం (Solar System) వయస్సు సుమారు 460 కోట్ల సంవత్సరాలు (4.6 billion years… | P002-F012, SP-073 | — |  |
| F023 | universe-what | విశ్వం పుట్టుక, పరిణామం, నిర్మాణాన్ని అధ్యయనం చేసే శాస్త్రం Cosmology (విశ్వవిజ్… | EXT-0174 | — |  |
| F024 | universe-what | మనకు వెలుగు, సమాచారం చేరగలిగిన విశ్వ భాగాన్ని Observable universe (పరిశీలించగల వ… | P002-F016 | — |  |
| F025 | universe-what | Observable universe వ్యాసం సుమారు 93 billion (9,300 కోట్ల) కాంతి సంవత్సరాలు. | — | — | low exam value (observable-universe size); not tested |
| F026 | universe-galaxy | Gravity వల్ల కలిసి ఉండే నక్షత్రాలు, వాయువు, ధూళి, Dark matter ల పెద్ద వ్యవస్థను … | P003-F007 | — |  |
| F027 | universe-galaxy | ఆకారాన్ని బట్టి Galaxies ప్రధాన రకాలు: Spiral, Elliptical, Lenticular, Irregular… | — | N004 |  |
| F028 | universe-galaxy | Galaxies ను ఆకారం ఆధారంగా వర్గీకరించిన శాస్త్రవేత్త Edwin Hubble. | — | N004 |  |
| F029 | universe-milky-way | Milky Way (పాలపుంత) ఒక Barred spiral galaxy; ఇందులో సుమారు 100–400 billion నక్షత… | P003-M003 (partial) | N004 |  |
| F030 | universe-milky-way | Milky Way మధ్యలో ఉన్న భారీ Black hole పేరు Sagittarius A*. | — | N005 |  |
| F031 | universe-milky-way | సూర్యుడు Milky Way మధ్యభాగం చుట్టూ ఒకసారి తిరగడానికి పట్టే కాలాన్ని Galactic yea… | P006-F013 | — |  |
| F032 | universe-milky-way | సూర్యుడు Milky Way లోని Orion Arm (Orion Spur / Local Arm) లో, మధ్యభాగం నుంచి సు… | P003-F009 | N005 |  |
| F033 | universe-milky-way | వెలుగు ఒక సంవత్సరంలో ప్రయాణించే దూరాన్ని Light-year (కాంతి సంవత్సరం) అంటారు; ఇది… | P006-F002 | — |  |
| F034 | universe-milky-way | Milky Way కి సమీపంలోని పెద్ద Galaxy Andromeda (M31), ఒక Spiral galaxy; దూరం సుమా… | P004-F003, SP-075 | — |  |
| F035 | universe-milky-way | సూర్యుడి తరువాత భూమికి అతి దగ్గరి నక్షత్రం Proxima Centauri; దూరం సుమారు 4.2 కాం… | P004-F002 | — |  |
| F036 | universe-nebula | నక్షత్రాల మధ్య వాయువు, ధూళి కణాలు మేఘంలా చేరిన ప్రాంతాన్ని Nebula (నిహారిక) అంటా… | P003-F005 | — |  |
| F037 | universe-nebula | జీవిత చివరలో నక్షత్రం వదిలిన వాయు పొరలతో ఏర్పడిన మేఘాన్ని Planetary nebula అంటార… | P003-F006 | N006 |  |
| F038 | universe-nebula | Supernova పేలుడు మిగిల్చిన Nebula ను Supernova remnant అంటారు; ఉదాహరణ Crab Nebul… | — | N006 |  |
| F039 | universe-nebula | వెలుగును బట్టి Nebulae రకాలు: Emission (ఉదా. Orion Nebula), Reflection, Dark (ఉద… | P003-M002 (partial) | N006 |  |
| F040 | universe-theories | General theory of relativity ని Albert Einstein 1915 లో ప్రతిపాదించాడు; ఇది Grav… | P003-F001 | — |  |
| F041 | universe-theories | విశ్వ ఆవిర్భావానికి నేడు ఆమోదించిన ప్రధాన సిద్ధాంతం Big Bang. | P002-F013 | — |  |
| F042 | universe-theories | Einstein 1917 Static నమూనాలో విశ్వం కూలకుండా ఉండేందుకు Cosmological constant చేర… | P003-M001 (partial) | — |  |
| F043 | universe-bigbang | విస్తరిస్తున్న విశ్వం ఆలోచనను Georges Lemaître 1927 లో ప్రతిపాదించాడు. | P002-F014 | N007 |  |
| F044 | universe-bigbang | Lemaître 1931 లో "Primeval atom" (ఆదిమ పరమాణువు) ఆలోచన చెప్పాడు; ఆయనను Father of… | P002-M004 (partial) | — |  |
| F045 | universe-bigbang | George Gamow, Ralph Alpher 1948 లో Big Bang ను అభివృద్ధి చేశారు; Hydrogen, Heliu… | — | N007 |  |
| F046 | universe-bigbang | Ralph Alpher, Robert Herman 1948 లో Big Bang నుంచి మిగిలిన Radiation ఉండాలని ముం… | — | — | minor name (Alpher–Herman CMB prediction); CMB origin tested in N010 |
| F047 | universe-bigbang | "Big Bang" అనే పేరును Fred Hoyle 1949 లో BBC రేడియోలో వాడాడు. | — | N007 |  |
| F048 | universe-redshift | అల శిఖరం నుంచి తరువాతి శిఖరం వరకు ఉన్న దూరాన్ని తరంగదైర్ఘ్యం (Wavelength) అంటారు… | P002-F015 (implicit) | — |  |
| F049 | universe-redshift | దూర Galaxies వెలుగులో Wavelength పెరిగి ఎరుపు వైపు జరగడాన్ని Redshift అంటారు. | P002-F015, P003-F002 | — |  |
| F050 | universe-redshift | Galaxy దూరం ఎంత ఎక్కువైతే దాని Redshift అంత ఎక్కువ; ఈ సంబంధాన్ని Edwin Hubble 19… | P002-F015 | N007 |  |
| F051 | universe-redshift | Hubble's Law సూత్రం v = H₀ × d; Hubble constant (H₀) సుమారు 70 km/s per Mpc. | — | N008 |  |
| F052 | universe-redshift | మన వైపు వస్తున్న వస్తువు వెలుగు నీలం వైపు జరగడాన్ని Blueshift అంటారు; ఉదాహరణ And… | — | N008 |  |
| F053 | universe-redshift | IAU 2018 లో Hubble's Law ను "Hubble–Lemaître law" అని పిలవాలని సిఫార్సు చేసింది. | — | N008 |  |
| F054 | universe-cmb | Big Bang నుంచి మిగిలిన Radiation ను Cosmic Microwave Background (CMB) అంటారు; దా… | SP-074, P003-F004 | N010, N011 |  |
| F055 | universe-cmb | CMB Big Bang తరువాత సుమారు 3,80,000 ఏళ్లకు, Electrons కేంద్రకాలతో కలిసి Atoms ఏర… | — | N010 |  |
| F056 | universe-cmb | CMB ను 1965 లో Arno Penzias, Robert Wilson Bell Labs లో కనుగొన్నారు; వీరికి 1978… | P002-M004 (partial) | N009 |  |
| F057 | universe-cmb | CMB ను కొలిచిన యాత్రలు: COBE (NASA, 1989), WMAP (NASA, 2001), Planck (ESA, 2009)… | — | N009 |  |
| F058 | universe-cmb | COBE కొలతల కోసం John Mather, George Smoot కు 2006 లో Nobel బహుమతి వచ్చింది. | — | N009 |  |
| F059 | universe-cmb | Big Bang లో ఏర్పడిన తొలి (Primordial) పదార్థంలో Mass పరంగా సుమారు 75% Hydrogen, … | — | N010 |  |
| F060 | universe-steady-state | Steady-state theory ని 1948 లో Hermann Bondi, Thomas Gold, Fred Hoyle ప్రతిపాదిం… | EXT-0159 | N012 |  |
| F061 | universe-steady-state | Steady-state ప్రకారం విశ్వం విస్తరిస్తున్నా కొత్త పదార్థం పుడుతూ ఉండటం వల్ల దాని… | P003-F003 | N011 |  |
| F062 | universe-steady-state | 1965 లో CMB దొరికిన తరువాత Steady-state theory బలహీనపడింది. | P003-F004 (implicit) | N011 |  |
| F063 | universe-steady-state | Quasi-steady state cosmology ని 1993 లో Fred Hoyle, Geoffrey Burbidge, Jayant Na… | — | N012 |  |
| F064 | universe-oscillating-inflation | విశ్వం విస్తరిస్తూ, కుంచించుకుంటూ చక్రంలా సాగుతుందని చెప్పేది Oscillating (Pulsa… | P003-F025 | N013 |  |
| F065 | universe-oscillating-inflation | Inflation theory ని Alan Guth 1980 లో ప్రతిపాదించాడు; ఇది Big Bang కు ఒక చేర్పు,… | — | N013 |  |
| F066 | universe-oscillating-inflation | విశ్వం ముగింపుపై మూడు ఆలోచనలు: Big Crunch (తిరిగి కూలడం), Big Freeze / Heat deat… | — | N013 |  |
| F067 | universe-dark | కనిపించకపోయినా Gravity ప్రభావం ద్వారా గుర్తించే పదార్థాన్ని Dark matter (కృష్ణ ప… | P003-F010, SP-076 | — |  |
| F068 | universe-dark | విశ్వం విస్తరణ వేగం పెరగడానికి కారణంగా భావించే శక్తిని Dark energy (కృష్ణ శక్తి)… | SP-076 | — |  |
| F069 | universe-dark | విశ్వంలో సుమారు 68% Dark energy, 27% Dark matter, 5% Normal matter (NASA). | — | N014 |  |
| F070 | universe-dark | విశ్వం విస్తరణ వేగం పెరుగుతోందని 1998 లో కనుగొన్నందుకు Perlmutter, Schmidt, Ries… | — | N014 |  |
| F071 | distances-units | AU, Light-year, Parsec మూడూ Distance units (దూర ప్రమాణాలు). | SP-001 | — |  |
| F072 | distances-units | చిన్న నుంచి పెద్దకు క్రమం: AU < Light-year < Parsec. | P006-M001 (partial) | — |  |
| F073 | distances-au | భూమికి, సూర్యుడికి మధ్య ఉన్న సగటు దూరాన్ని Astronomical Unit (AU) అంటారు. | P009-F017 | — |  |
| F074 | distances-au | 1 AU ≈ 14.96 కోట్ల km (149.6 million km), అంటే సుమారు 15 కోట్ల km. | SP-002, P004-F033 | — |  |
| F075 | distances-au | IAU 2012 లో 1 AU ను సరిగ్గా 149,597,870,700 m గా స్థిరం చేసింది. | P006-F001 | — |  |
| F076 | distances-au | భూమి సుమారు జనవరి 3 న సూర్యుడికి అత్యంత దగ్గరగా (Perihelion), సుమారు జూలై 4 న అత… | — | N111 |  |
| F077 | distances-au | ఋతువులు (Seasons) భూమి అక్షం సుమారు 23.5° వంగి ఉండటం వల్ల వస్తాయి; సూర్యుడి నుంచ… | — | — | duplicate of a fact tested elsewhere (seasons from tilt: SP-049, SP-053, N117) |
| F078 | distances-light-time | కాంతి వేగం సెకనుకు సుమారు 3 లక్షల km (300,000 km/s = 3 × 10⁸ m/s). | SP-003 | — |  |
| F079 | distances-light-time | సూర్యకాంతి భూమికి చేరడానికి సుమారు 8 నిమిషాల 20 సెకన్లు (సుమారు 499 సెకన్లు) పడు… | SP-003, P006-F005 | N015 |  |
| F080 | distances-light-time | చంద్రుడి వెలుగు భూమికి చేరడానికి సుమారు 1.3 సెకన్లు పడుతుంది. | P022-F011 | N015 |  |
| F081 | distances-light-time | సూర్యకాంతి Neptune (నెప్ట్యూన్) ను చేరడానికి సుమారు 4 గంటలు పడుతుంది. | — | N015 |  |
| F082 | distances-light-year | కాంతి Vacuum లో ఒక సంవత్సరంలో ప్రయాణించే దూరాన్ని Light-year (కాంతి సంవత్సరం) అం… | P006-F002 | N016 |  |
| F083 | distances-light-year | 1 Light-year ≈ 9.46 లక్షల కోట్ల km (9.46 trillion km, 9.46 × 10¹² km). | P006-F002 (explanation) | N016 |  |
| F084 | distances-light-year | Light-year నిర్వచనంలో సంవత్సరం అంటే Julian year, అంటే 365.25 రోజులు. Leap year న… | — | N016 |  |
| F085 | distances-parallax | మనం చూసే చోటు మారితే దగ్గరి వస్తువు Background ముందు పక్కకు కదిలినట్టు కనిపిస్తు… | P006-F004 | — |  |
| F086 | distances-parallax | రెండు చూసే చోట్ల మధ్య దూరాన్ని Baseline అంటారు. నక్షత్ర Parallax లో Baseline భూమ… | — | N017 |  |
| F087 | distances-parallax | ఆరు నెలల తేడాతో కనిపించే మొత్తం Shift లో సగమే Parallax angle (p). | — | N017 |  |
| F088 | distances-parallax | నక్షత్రం ఎంత దగ్గరగా ఉంటే దాని Parallax angle అంత పెద్దది. | — | N018, N019 |  |
| F089 | distances-parallax | 1 Degree = 3,600 Arcseconds. | — | — | unit fact used inside N017 (arcseconds) |
| F090 | distances-parallax | Friedrich Bessel 1838 లో 61 Cygni నక్షత్రం Parallax ను కొలిచాడు; దీన్నే మొదటి వి… | — | N018 |  |
| F091 | distances-parallax | Parallax పద్ధతి దగ్గరి నక్షత్రాలకే పనిచేస్తుంది. ESA పంపిన Hipparcos (1989), Gai… | — | N018 |  |
| F092 | distances-parsec | Parallax angle 1 Arcsecond ఉన్న నక్షత్రం దూరాన్ని 1 Parsec (pc) అంటారు. | P006-M001 (partial) | N019 |  |
| F093 | distances-parsec | 1 Parsec ≈ 3.26 Light-years. | P006-F003, SP-077 | N019 |  |
| F094 | distances-parsec | దూరం (Parsecs) = 1 ÷ Parallax angle (Arcseconds). దూరం రెట్టింపు అయితే కోణం సగం. | — | N017 |  |
| F095 | distances-parsec | Parsec అనే పేరు Parallax, Arcsecond అనే రెండు పదాల నుంచి వచ్చింది. | — | — | name origin of parsec; low exam value |
| F096 | distances-parsec | 1 kpc = 1,000 pc; 1 Mpc = 10 లక్షల pc. Galaxies దూరాలకు ఇవి వాడతారు. | — | — | unit detail (kpc, Mpc); low exam value |
| F097 | distances-parsec | Milky Way వెడల్పు సుమారు 1 లక్ష Light-years (సుమారు 30 kpc). | — | — | low exam value (Milky Way width) |
| F098 | distances-nearest-star | భూమికి అత్యంత దగ్గరి నక్షత్రం సూర్యుడు. | P004-F001 | — |  |
| F099 | distances-nearest-star | సూర్యుడి తరువాత భూమికి దగ్గరి నక్షత్రం Proxima Centauri; దూరం సుమారు 4.24 Light-… | P004-F002, P004-M001 | N015 |  |
| F100 | distances-nearest-star | Proxima Centauri ఒక Red dwarf; ఇది Alpha Centauri అనే మూడు నక్షత్రాల వ్యవస్థలో భ… | — | N020 |  |
| F101 | distances-nearest-star | Proxima b అనే Exoplanet ను 2016 లో కనుగొన్నారు; ఇది Proxima Centauri యొక్క Habit… | — | N020 |  |
| F102 | distances-nearest-galaxy | మనకు దగ్గరి పెద్ద Galaxy Andromeda (M31); దూరం సుమారు 25 లక్షల Light-years (2.5 … | P004-F003, SP-075 | N021 |  |
| F103 | distances-nearest-galaxy | Milky Way కు దగ్గరి Spiral galaxy Andromeda. ఇది కంటికి కనిపిస్తుంది, మన వైపు వస… | P004-F003 | — |  |
| F104 | distances-nearest-galaxy | Large Magellanic Cloud (సుమారు 1.6 లక్షల Light-years), Small Magellanic Cloud (స… | — | N021 |  |
| F105 | distances-nearest-galaxy | NASA ప్రకారం 2003 లో కనుగొన్న Canis Major Dwarf Galaxy సుమారు 25,000 Light-years… | — | N021 |  |
| F106 | distances-nearest-galaxy | Milky Way, Andromeda, Triangulum (M33), 50 కి పైగా Dwarf galaxies కలిసిన గుంపును… | — | N021 |  |
| F107 | distances-closest-planet | సూర్యుడికి దగ్గరి గ్రహం Mercury (బుధుడు); సూర్యుడికి అత్యంత దూరమైన గ్రహం Neptune… | SP-019, P005-F016 | — |  |
| F108 | distances-closest-planet | 2006 లో IAU Pluto ను Dwarf planet గా మార్చింది; అప్పటి నుంచి సౌర కుటుంబంలో గ్రహా… | P005-F003 | N057 |  |
| F109 | distances-closest-planet | భూమికి అత్యంత దగ్గరగా వచ్చే గ్రహం Venus (శుక్రుడు); అప్పుడు దూరం సుమారు 3.8 కోట్… | P005-F014, SP-005 | N022 |  |
| F110 | distances-closest-planet | సగటు దూరం లెక్కిస్తే భూమికి దగ్గరి గ్రహం Mercury (బుధుడు) (Stockman, Monroe, Cor… | SP-005 | N022 |  |
| F111 | sky-star-planet | నక్షత్రం (Star) తన Core లో జరిగే Nuclear fusion వల్ల తన వెలుగును తానే తయారు చేసు… | P003-F011 (contrast) | N023 |  |
| F112 | sky-star-planet | సూర్యుడి Core లో వేడి సుమారు 1.5 కోట్ల °C (15 million °C). | — | — | in N023 context; Sun core temperature not separately tested (low value) |
| F113 | sky-star-planet | గ్రహం (Planet) నక్షత్రం వెలుగును తిరిగి పంపడం (Reflection) వల్ల మెరుస్తుంది; దాన… | P003-F011 | N023 |  |
| F114 | sky-star-planet | IAU 2006 లో గ్రహానికి మూడు నియమాలు పెట్టింది. ఆ ప్రకారం Solar System లో గ్రహాలు … | P005-F001 | — |  |
| F115 | sky-star-planet | నక్షత్రాలు మినుకుమినుకుమనడానికి (Twinkling) కారణం Atmospheric refraction; గ్రహాల… | — | N023 |  |
| F116 | sky-constellation | IAU (అంతర్జాతీయ ఖగోళ సమాఖ్య) ఆకాశాన్ని 88 Constellations (నక్షత్రరాశులు) గా విభజ… | P004-F006, P004-F005, SP-006 | — |  |
| F117 | sky-constellation | Ptolemy (సుమారు క్రీ.శ. 150) Almagest లో 48 Constellations రాశారు; IAU 88 లో మిగ… | — | N024 |  |
| F118 | sky-constellation | 88 Constellations జాబితాను IAU 1922 లో ఒప్పుకుంది. | P004-M003 (partial) | N024 |  |
| F119 | sky-constellation | Eugène Delporte గీసిన Constellation హద్దులను IAU 1928 లో ఆమోదించింది; అవి 1930 ల… | — | N024 |  |
| F120 | sky-constellation | ఆకాశ విస్తీర్ణం ప్రకారం అతి పెద్ద Constellation Hydra (సుమారు 1,303 Square degre… | P004-F009 | — |  |
| F121 | sky-asterism | సప్తర్షి మండలం (Big Dipper, The Plough) Ursa Major (ఉర్సా మేజర్) Constellation ల… | P004-F007 | N025 |  |
| F122 | sky-asterism | సులభంగా గుర్తుపట్టగలిగే నక్షత్రాల ఆకారాన్ని Asterism అంటారు; దీనికి IAU హద్దులు … | P004-F007, P004-M002 | — |  |
| F123 | sky-asterism | Summer Triangle అనే Asterism మూడు Constellations లోని Vega, Deneb, Altair నక్షత్… | — | N025 |  |
| F124 | sky-asterism | సప్తర్షుల్లో వసిష్ఠుడు (Mizar), అరుంధతి (Alcor) పక్కపక్కనే కనిపించే నక్షత్రాల జం… | — | N025 |  |
| F125 | sky-polaris | ధ్రువ నక్షత్రం (Polaris) Ursa Minor (ఉర్సా మైనర్) Constellation లో ఉంది. | P004-F008, SP-079 | — |  |
| F126 | sky-polaris | ధ్రువ నక్షత్రం North celestial pole (ఉత్తర ఖగోళ ధ్రువం) కు దగ్గరగా ఉండటం వల్ల ఉత… | — | N026 |  |
| F127 | sky-polaris | సప్తర్షి మండలంలోని Dubhe, Merak అనే రెండు Pointer నక్షత్రాలు ధ్రువ నక్షత్రం వైపు… | — | N026 |  |
| F128 | sky-polaris | ఉత్తర అర్ధగోళంలో ధ్రువ నక్షత్రం Horizon (క్షితిజం) నుంచి కనిపించే ఎత్తు ఆ ప్రదేశ… | — | N026 |  |
| F129 | sky-polaris | Polaris దూరం సుమారు 430 Light-years; ప్రకాశంలో అది సుమారు 48 వ స్థానంలో ఉంటుంది. | P004-M002 (partial) | — |  |
| F130 | sky-polaris | భూమి Axis సుమారు 26,000 సంవత్సరాలకు ఒకసారి ఒక వృత్తం గీస్తుంది; ఈ కదలికను Preces… | — | N027 |  |
| F131 | sky-polaris | Precession ను సుమారు క్రీ.పూ. 130 లో Hipparchus కనుగొన్నారు. | — | N027 |  |
| F132 | sky-polaris | Polaris తరువాత ధ్రువ నక్షత్రాలు: Gamma Cephei (సుమారు క్రీ.శ. 4000), Alderamin (… | — | N027 |  |
| F133 | sky-brightness | భూమి నుంచి ఒక నక్షత్రం ఎంత ప్రకాశంగా కనిపిస్తుందో దాన్ని Apparent brightness అంట… | — | N028 |  |
| F134 | sky-brightness | నక్షత్రం ప్రతి సెకనుకు విడుదల చేసే మొత్తం శక్తిని Luminosity అంటారు; దీన్ని Watt… | — | — | definition in N028 table (luminosity) |
| F135 | sky-brightness | Magnitude స్కేలులో అంకె చిన్నదైతే ప్రకాశం ఎక్కువ; కంటికి కనిపించే పరిమితి సుమారు… | — | N028 |  |
| F136 | sky-brightness | 10 Parsecs దూరం నుంచి ఒక నక్షత్రం కనిపించే Magnitude ను Absolute magnitude అంటార… | — | N028 |  |
| F137 | sky-brightness | దూరం రెట్టింపు అయితే కనిపించే ప్రకాశం నాలుగో వంతు అవుతుంది (Inverse square law). | — | N028 |  |
| F138 | sky-brightness | సూర్యుడు భూమికి సుమారు 15 కోట్ల km దూరంలో ఉన్నాడు; ఆయన వెలుగు భూమికి చేరడానికి స… | P006-F005 | — |  |
| F139 | sky-brightness | సూర్యుడిని మినహాయిస్తే భూమికి అత్యంత దగ్గరి నక్షత్రం Proxima Centauri (సుమారు 4.… | P004-F002 | — |  |
| F140 | sky-brightest | రాత్రి ఆకాశంలో అత్యంత ప్రకాశవంతంగా కనిపించే నక్షత్రం Sirius (సిరియస్, Dog Star, … | P004-F004, SP-080 | — |  |
| F141 | sky-brightest | రాత్రి ఆకాశంలో రెండో ప్రకాశవంతమైన నక్షత్రం Canopus (అగస్త్య); మూడోది Alpha Centa… | — | N029 |  |
| F142 | sky-brightest | ఉత్తర ఖగోళ అర్ధగోళంలో అత్యంత ప్రకాశవంతమైన నక్షత్రం Arcturus (స్వాతి). | — | N029 |  |
| F143 | sky-brightest | సూర్యుడు, చంద్రుడు తరువాత ఆకాశంలో అత్యంత ప్రకాశవంతంగా కనిపించేది Venus (శుక్రుడు… | P011-F017 | — |  |
| F144 | sky-brightest | Betelgeuse (Orion), Antares (Scorpius) Red supergiants; Rigel (Orion) Blue super… | — | N029 |  |
| F145 | sky-brightest | పుస్తకాల్లో "అతి పెద్ద నక్షత్రం" జవాబు UY Scuti (Scutum Constellation లోని Red s… | P004-F071 | — |  |
| F146 | sky-brightest | తెలిసిన నక్షత్రాల్లో అతి బరువైనది, అత్యధిక Luminosity ఉన్నది R136a1 (Large Magel… | — | N029 |  |
| F147 | sky-inferior-superior | భూమి Orbit కు లోపల తిరిగే Mercury (బుధుడు), Venus (శుక్రుడు) లను Inferior planet… | SP-078, P005-F011 | N030 |  |
| F148 | sky-inferior-superior | భూమి Orbit కు బయట తిరిగే Mars (కుజుడు) నుంచి Neptune (నెప్ట్యూన్) వరకు ఐదు గ్రహా… | P005-F012 | — |  |
| F149 | sky-inferior-superior | Mercury, Venus, Earth, Mars లను Terrestrial planets అంటారు; Jupiter, Saturn Gas … | P005-F006, F007, F009, F010 | — |  |
| F150 | sky-inferior-superior | Inferior planets ఎప్పుడూ సూర్యుడి దగ్గరే కనిపిస్తాయి; శుక్రుడి Greatest elongati… | — | N030 |  |
| F151 | sky-inferior-superior | తెల్లవారుజామున తూర్పున కనిపించే శుక్రుడిని (Venus) వేగుచుక్క (Morning star) అంటా… | P011-F016 (name only) | N030 |  |
| F152 | sky-inferior-superior | Opposition Superior planets కు మాత్రమే వస్తుంది; Transit, Inferior conjunction I… | — | N031 |  |
| F153 | sky-inferior-superior | Transit of Venus చివరిసారి 2012 లో, తరువాత 2117 లో; Transit of Mercury చివరిసారి… | — | N031 |  |
| F154 | sky-ecliptic-zodiac | సూర్యుడు ఏడాదంతా నక్షత్రాల మధ్య కదులుతున్నట్లు కనిపించే దారిని Ecliptic (క్రాంతి… | — | — | definition in N032 table (ecliptic) |
| F155 | sky-ecliptic-zodiac | భూమి తన Axis మీద తిరగడం Rotation (భ్రమణం, సుమారు 24 గంటలు); సూర్యుడి చుట్టూ తిరగ… | SP-037 | — |  |
| F156 | sky-ecliptic-zodiac | భూమి Revolution వల్ల సూర్యుడు Ecliptic వెంట కదులుతున్నట్లు కనిపిస్తాడు. | — | N032 |  |
| F157 | sky-ecliptic-zodiac | Ecliptic, Celestial equator మధ్య కోణం సుమారు 23.5°; అవి కలిసే రెండు బిందువులు Eq… | — | N032 |  |
| F158 | sky-ecliptic-zodiac | Ecliptic వెంట ఉండే నక్షత్రాల పట్టీని రాశిచక్రం (Zodiac) అంటారు; Babylon ప్రజలు ద… | — | — | in N032 table (Babylon, 12 signs) |
| F159 | sky-ecliptic-zodiac | IAU హద్దుల ప్రకారం Ecliptic 13 Constellations గుండా వెళ్తుంది; 13 వది Ophiuchus. | — | N032 |  |
| F160 | sky-ecliptic-zodiac | Sayana, Nirayana రాశి పద్ధతుల మధ్య తేడాను అయనాంశం (Ayanamsa) అంటారు; ఇప్పుడు అది… | — | N032 |  |
| F161 | sky-astrology | ఖగోళశాస్త్రం (Astronomy) పరిశీలనలు, కొలతలు, ఆధారాలతో అంతరిక్ష వస్తువులను అధ్యయనం… | P012-F001 | — |  |
| F162 | sky-astrology | జ్యోతిషం (Astrology) నక్షత్రాలు, గ్రహాల స్థానాలు భవిష్యత్తును చెబుతాయనే నమ్మకం; … | P012-F002 | — |  |
| F163 | sky-astrology | 2005 లో Eris దొరికిన తరువాత, 2006 లో IAU Pluto ను Dwarf planet గా మార్చింది. | P010-F008 | N057 |  |
| F164 | sky-astrology | ఆర్యభటుడు (జననం క్రీ.శ. 476) ఆర్యభటీయం రాశారు; భూమి తన Axis మీద తిరుగుతుందని చెప… | — | — | in N141 table (Aryabhata born 476) |
| F165 | stars-birth | నక్షత్రాలు వాయువు, ధూళితో ఉన్న చల్లని Molecular cloudsలో పుడతాయి. | — | N033 |  |
| F166 | stars-birth | Gravity వల్ల కుంచించుకుపోయి వేడెక్కుతున్న, ఇంకా Fusion మొదలుకాని దశను Protostar … | — | N033 |  |
| F167 | stars-birth | Hydrogen fusion మొదలవ్వాలంటే Core Temperature సుమారు 1 కోటి డిగ్రీలు (10 million… | — | N033 |  |
| F168 | stars-birth | నక్షత్రం పుట్టుక క్రమం: Molecular cloud → Protostar → Main-sequence star. | — | N033 |  |
| F169 | stars-main-sequence | Core లో Hydrogen నుంచి Helium తయారయ్యే దీర్ఘ దశను Main sequence అంటారు. | P010-F009 | — |  |
| F170 | stars-main-sequence | సూర్యుడు G2 V రకం Main-sequence నక్షత్రం (Yellow dwarf). | — | N034 |  |
| F171 | stars-main-sequence | నక్షత్రం Initial mass ఎక్కువైతే దాని జీవిత కాలం తక్కువ. | P011-F006 | — |  |
| F172 | stars-main-sequence | Spectral classes, అతి వేడి నుంచి అతి చల్లని వరకు: O, B, A, F, G, K, M. సూర్యుడు … | — | N034 |  |
| F173 | stars-main-sequence | నక్షత్రాల Temperature, Luminosity ను చూపే గ్రాఫ్ Hertzsprung-Russell (H-R) diagr… | — | N034 |  |
| F174 | stars-main-sequence | సూర్యుడి Main-sequence జీవితం సుమారు 1,000 కోట్ల సంవత్సరాలు (10 billion years); … | — | N034 |  |
| F175 | stars-end-paths | సుమారు 8 solar masses కంటే తక్కువ Initial mass ఉన్న నక్షత్రాలు చివరికి White dwa… | P010-F017 | — |  |
| F176 | stars-end-paths | సుమారు 8 solar masses కంటే ఎక్కువ Initial mass ఉన్న నక్షత్రాలు Core-collapse sup… | P010-F017, P010-F013 | N035 |  |
| F177 | stars-end-paths | సూర్యుడి Mass లో సగం కంటే తక్కువ ఉన్న Red dwarfs Red giant కావు; చివరికి నేరుగా … | — | N035 |  |
| F178 | stars-end-paths | 8 solar masses కంటే భారీ నక్షత్రాలు Supergiants గా ఉబ్బుతాయి. Betelgeuse (ఆరుద్ర… | P010-M003 (partial) | — |  |
| F179 | stars-end-paths | Iron Fusion శక్తి ఇవ్వదు. అందుకే భారీ నక్షత్రం Core లో Iron పేరుకోగానే Core coll… | — | N035 |  |
| F180 | stars-red-giant-white-dwarf | Core లో Hydrogen తగ్గాక బయటి పొరలు విస్తరించి, ఉపరితలం చల్లబడిన పెద్ద దశను Red g… | P010-F010 | — |  |
| F181 | stars-red-giant-white-dwarf | Red giant వదిలిన బయటి వాయు పొరలు ఏర్పరిచే మేఘాన్ని Planetary nebula అంటారు. | SP-088 | N036 |  |
| F182 | stars-red-giant-white-dwarf | Planetary nebula అనే పేరు William Herschel పెట్టాడు; ఆ మేఘాలు టెలిస్కోప్‌లో గ్రహ… | — | N036 |  |
| F183 | stars-red-giant-white-dwarf | Uranus గ్రహాన్ని 1781లో William Herschel కనుగొన్నాడు. | — | N036 |  |
| F184 | stars-red-giant-white-dwarf | Nebula రకాలు: Emission, Reflection, Dark, Planetary nebula, Supernova remnant (ఉ… | — | — | duplicate of a fact tested elsewhere (nebula types: N006) |
| F185 | stars-red-giant-white-dwarf | సూర్యుడిలాంటి నక్షత్రం చివరికి మిగిల్చే చిన్న, దట్టమైన, వేడి Core ను White dwarf… | P010-F012 | — |  |
| F186 | stars-red-giant-white-dwarf | White dwarf పూర్తిగా చల్లబడితే Black dwarf అవుతుందని భావిస్తారు; ఇప్పటివరకు ఒక్క… | P011-F005 | — |  |
| F187 | stars-sun-future | సూర్యుడి భవిష్యత్ క్రమం: Main sequence (ఇప్పుడు) → Red giant → Planetary nebula … | P010-F011, SP-088 | N037 |  |
| F188 | stars-sun-future | సుమారు 500 కోట్ల సంవత్సరాల (5 billion years) తరువాత సూర్యుడు Red giant అవుతాడు. | — | N037 |  |
| F189 | stars-sun-future | Red giant అయిన సూర్యుడు Mercury (బుధుడు), Venus (శుక్రుడు) ను మింగేస్తాడు; భూమిన… | — | N037 |  |
| F190 | stars-chandrasekhar | Rotation లేని White dwarf గరిష్ఠ Mass సుమారు 1.4 solar masses; దీన్ని Chandrasek… | P011-F008 | N039 |  |
| F191 | stars-chandrasekhar | White dwarf ను కూలిపోకుండా నిలబెట్టేది Electron degeneracy pressure. | — | N038, N039 |  |
| F192 | stars-chandrasekhar | సుబ్రహ్మణ్యన్ చంద్రశేఖర్ 1930లో ఇంగ్లాండ్‌కు ఓడ ప్రయాణంలో ఈ హద్దును లెక్కించారు. | — | N038 |  |
| F193 | stars-chandrasekhar | చంద్రశేఖర్‌కు 1983 Physics Nobel Prize నక్షత్రాల నిర్మాణం, పరిణామంపై సైద్ధాంతిక … | P011-F011 | — |  |
| F194 | stars-chandrasekhar | NASA Chandra X-ray Observatory (1999) కు చంద్రశేఖర్ పేరు పెట్టారు. | — | N038 |  |
| F195 | stars-chandrasekhar | రెండు Electrons ఒకే స్థితిలో ఉండలేవు అనే నియమం Pauli exclusion principle (Wolfga… | — | — | in N038 explanation (Pauli principle) |
| F196 | stars-chandrasekhar | Chandrasekhar limit ను Arthur Eddington 1935లో Royal Astronomical Society సమావేశ… | — | N038 |  |
| F197 | stars-chandrasekhar | చంద్రశేఖర్ University of Chicago లో పనిచేశారు; 1968లో Padma Vibhushan పొందారు. | — | — | in N038 table (Padma Vibhushan 1968); low value |
| F198 | stars-dwarfs | Red dwarf చిన్న, చల్లని Main-sequence నక్షత్రం; దానిలో Hydrogen fusion జరుగుతుంద… | P011-F003 | — |  |
| F199 | stars-dwarfs | Milky Way గెలాక్సీలో సుమారు 75% నక్షత్రాలు Red dwarfs. | — | N040 |  |
| F200 | stars-dwarfs | సూర్యుడికి అతి దగ్గరి నక్షత్రం Proxima Centauri ఒక Red dwarf; దూరం సుమారు 4.2 li… | P004-F002 | — |  |
| F201 | stars-dwarfs | Brown dwarf కు Hydrogen fusion ఎక్కువ కాలం నడిపేంత Mass లేదు. దాని Mass Jupiter … | P011-F004 | N040 |  |
| F202 | stars-dwarfs | Brown dwarf పై హద్దు సుమారు 80 Jupiter masses, అంటే 0.08 solar masses. దీని కంటే… | — | N040 |  |
| F203 | stars-dwarfs | Galaxy అంటే Gravity తో కలిసి ఉండే కోట్లాది నక్షత్రాలు, వాయువు, ధూళి గుంపు; మన Ga… | P003-F007 | — |  |
| F204 | stars-dwarfs | Proxima Centauri ని 1915లో Robert Innes కనుగొన్నాడు. | — | N020 |  |
| F205 | stars-binary-nova | రెండు నక్షత్రాలు పరస్పర Gravity తో ఒకదాని చుట్టూ ఒకటి తిరిగే వ్యవస్థను Binary sy… | P011-F001 | — |  |
| F206 | stars-binary-nova | Binary system లో White dwarf ఉపరితలం మీద పేరుకున్న వాయువు పేలి వెలుగు ఒక్కసారిగా… | P011-F001, SP-085 | N041 |  |
| F207 | stars-binary-nova | Nova తరువాత White dwarf సాధారణంగా అలాగే మిగులుతుంది; మళ్లీ పేలవచ్చు. | P011-F002 | N041 |  |
| F208 | stars-binary-nova | T Coronae Borealis ("Blaze star") సుమారు 80 ఏళ్లకు ఒకసారి పేలే Recurrent nova; చ… | — | N041 |  |
| F209 | stars-supernova | Supernova కు రెండు దారులు: భారీ నక్షత్రం Core collapse, White dwarf thermonuclea… | P010-F016, SP-085 | — |  |
| F210 | stars-supernova | Spectrum లో Hydrogen గీతలు లేని Supernova ను Type I అని, ఉన్న దాన్ని Type II అని… | — | N042 |  |
| F211 | stars-supernova | Type Ia Supernova లో Binary system లోని White dwarf Chandrasekhar limit చేరి పూర… | P011-F002 | N039 |  |
| F212 | stars-supernova | Type II Supernova భారీ నక్షత్రం Core collapse వల్ల జరుగుతుంది; Neutron star లేదా… | SP-085 | N042 |  |
| F213 | stars-supernova | Type Ia Supernovae ను Standard candles అంటారు; వాటితో దూరం కొలుస్తారు. | — | N042 |  |
| F214 | stars-supernova | Type Ia ల ద్వారా విశ్వం విస్తరణ వేగం పెరుగుతోందని కనుగొన్నందుకు 2011 Physics Nob… | — | N014 |  |
| F215 | stars-supernova | SN 1054 అవశేషం Crab Nebula; Milky Way లో కంటికి కనిపించిన చివరి Supernova SN 160… | — | N042 |  |
| F216 | stars-neutron-pulsar | భారీ నక్షత్రం Core కూలిపోయి, దాదాపు Neutrons తో మాత్రమే నిండిన చిన్న, అతి దట్టమై… | P010-F013 | — |  |
| F217 | stars-neutron-pulsar | Neutron star వ్యాసం సుమారు 20 km; అయినా దాని Mass సూర్యుడి Mass కంటే ఎక్కువ ఉండవ… | — | N043 |  |
| F218 | stars-neutron-pulsar | తిరుగుతూ, Radiation పుంజం భూమి వైపు తిరిగినప్పుడల్లా పల్స్ లాగా కనిపించే Neutron… | SP-086, P010-F014 | — |  |
| F219 | stars-neutron-pulsar | మొదటి Pulsar (PSR B1919+21) ను 1967లో Jocelyn Bell గుర్తించారు; 1974 Nobel Anton… | — | N043 |  |
| F220 | stars-neutron-pulsar | Neutron ను 1932లో James Chadwick కనుగొన్నాడు; Neutron star ఆలోచనను 1934లో Walter… | — | N043 |  |
| F221 | stars-neutron-pulsar | Crab Nebula మధ్యలోని Crab Pulsar, SN 1054 Supernova మిగిల్చిన Neutron star. | — | N043 |  |
| F222 | stars-quark-star | ప్రధానంగా విడిపోయిన Quarks తో ఉన్నట్లు ఊహించే దట్టమైన వస్తువును Quark star అంటార… | P010-F015 | — |  |
| F223 | stars-black-hole | Event horizon అనేది Black hole చుట్టూ ఉండే సరిహద్దు; దాని లోపలి నుంచి వెలుగు కూడ… | P011-F007 | — |  |
| F224 | stars-black-hole | Black hole మొదటి చిత్రాన్ని Event Horizon Telescope 2019 ఏప్రిల్ 10న విడుదల చేసి… | — | N044, N046 |  |
| F225 | stars-black-hole | Milky Way మధ్యలోని Supermassive black hole పేరు Sagittarius A*; Mass సూర్యుడి Ma… | — | N005 |  |
| F226 | stars-black-hole | Event horizon Radius ను Schwarzschild radius అంటారు; Black hole మధ్యలో Mass అంతా… | — | N044 |  |
| F227 | stars-black-hole | Black hole గా అంగీకరించిన మొదటి వస్తువు Cygnus X-1. | — | N044 |  |
| F228 | stars-black-hole | Gravitational waves ను మొదట 2015లో LIGO గుర్తించింది (రెండు Black holes కలయిక); … | — | N045 |  |
| F229 | stars-black-hole | 2020 Physics Nobel: Roger Penrose (Black hole సిద్ధాంతం), Reinhard Genzel, Andre… | — | N045 |  |
| F230 | stars-black-hole-history | వెలుగు తప్పించుకోలేని "Dark star" ఆలోచనను 1783లో John Michell చెప్పాడు. | — | N046 |  |
| F231 | stars-black-hole-history | Black hole అనే పదాన్ని John Wheeler 1967లో ప్రాచుర్యంలోకి తెచ్చాడు. | P011-F010 | N046 |  |
| F232 | stars-black-hole-history | Black holes Quantum ప్రభావాల వల్ల నెమ్మదిగా Radiation విడుదల చేసి Mass కోల్పోతాయ… | P011-F009 | N046 |  |
| F233 | stars-quasar | Supermassive black hole వైపు పడుతున్న పదార్థం వేడెక్కి వెలిగే, దూరంలోని అతి ప్రక… | SP-087 | N047 |  |
| F234 | stars-quasar | Quasar అంటే Quasi-stellar radio source; మొదటి Quasar 3C 273 ను 1963లో Maarten Sc… | — | N047 |  |
| F235 | stars-quasar | "Quasar" అనే పేరును 1964లో Hong-Yee Chiu పెట్టాడు; 3C 273 దూరం సుమారు 240 కోట్ల … | — | N047 |  |
| F236 | stars-quasar | దూరంగా వెళ్లే వస్తువు వెలుగు ఎర్ర వైపుకు జరగడాన్ని Redshift అంటారు; ఇది Doppler … | P002-F015 | — |  |
| F237 | formation-nebular-model | సౌర కుటుంబం (Solar System) సుమారు 460 కోట్ల సంవత్సరాల (4.6 billion years) క్రితం… | P002-F012, SP-007 | N048 |  |
| F238 | formation-nebular-model | దగ్గరలోని నక్షత్రం పేలుడు (Supernova) నుంచి వచ్చిన Shockwave మేఘం కుంచించుకోవడాన… | — | N048 |  |
| F239 | formation-nebular-model | మేఘం Gravity వల్ల కుంచించుకుపోయి, మధ్యలో సూర్యుడు, చుట్టూ ఉన్న Disk లో గ్రహాలు ఏ… | SP-007 | — |  |
| F240 | formation-nebular-model | యువ నక్షత్రం చుట్టూ గ్రహాలు ఏర్పడే వాయువు–ధూళి పళ్లాన్ని Protoplanetary disk అంట… | P003-F013 | — |  |
| F241 | formation-nebular-model | చిన్న కణాలు చేరుతూ పెద్ద వస్తువుగా పెరగడాన్ని Accretion అంటారు. | SP-008, P003-F014 | — |  |
| F242 | formation-nebular-model | గ్రహాలు ఏర్పడటానికి ఇటుకల్లా ఉపయోగపడిన చిన్న ఘన వస్తువులను Planetesimals అంటారు. | P003-F015, SP-082 | — |  |
| F243 | formation-nebular-model | సౌర కుటుంబం మొత్తం Mass లో 99% కంటే ఎక్కువ సూర్యుడిలోనే ఉంది. | P006-M002 (partial) | N048 |  |
| F244 | formation-rocky-giant | సూర్యుడికి దగ్గర వేడి వల్ల రాళ్లు, లోహాలు మాత్రమే గట్టిగా మిగిలాయి; అందుకే లోపలి… | — | N049 |  |
| F245 | formation-rocky-giant | యువ సౌర కుటుంబంలో నీరు మంచుగా గడ్డకట్టగలిగిన సరిహద్దును Frost line (Snow line) అ… | — | N049 |  |
| F246 | formation-rocky-giant | Frost line అవతల మంచుతో పెద్దవైన ముద్దలు Hydrogen, Helium వాయువును లాగి Gas giant… | — | N049 |  |
| F247 | formation-rocky-giant | Jupiter, Saturn, Uranus, Neptune లను కలిపి Jovian planets (Outer planets) అంటారు… | P005-F006, F007 | — |  |
| F248 | formation-rocky-giant | Uranus (యురేనస్), Neptune (నెప్ట్యూన్) లను Ice giants అంటారు; వీటిలో నీరు, Ammon… | — | N049 |  |
| F249 | formation-ages | భూమి (Earth) వయస్సు సుమారు 454 కోట్ల సంవత్సరాలు (4.54 billion years). | EXT-0139 | — |  |
| F250 | formation-ages | 1956 లో Clair Patterson, Canyon Diablo Meteorite Lead ను భూమి Lead తో పోల్చి భూమ… | — | N050, N051 |  |
| F251 | formation-ages | Radioactive element లో సగం మారిపోవడానికి పట్టే కాలాన్ని Half-life అంటారు; Uraniu… | — | N050 |  |
| F252 | formation-ages | రాళ్లలోని Radioactive elements ఎంత మారాయో కొలిచి వయస్సు లెక్కించే పద్ధతిని Radio… | — | N051 |  |
| F253 | formation-ages | Zircon అనేది Uranium ను బంధించుకునే చాలా గట్టి ఖనిజ స్ఫటికం; భూమి మీద అతి పాత వయ… | — | — | definition in N051 table (zircon) |
| F254 | formation-ages | Gneiss అంటే పాత రాయి లోపలి వేడి, ఒత్తిడితో మారి ఏర్పడిన చారల రాయి. | — | — | definition in N051 table (gneiss) |
| F255 | formation-ages | భూమి మీద ఇప్పటివరకు దొరికిన అతి పాత రాయి Canada లోని Acasta Gneiss (సుమారు 403 క… | — | N050, N051 |  |
| F256 | formation-ages | భూమి మీద దొరికిన అతి పాత ఖనిజం Western Australia లోని Jack Hills Zircon స్ఫటికాల… | — | N050 |  |
| F257 | formation-ages | యువ భూమిని Theia అనే Mars అంత వస్తువు ఢీకొట్టగా ఎగిరిన ముక్కలతో చంద్రుడు ఏర్పడ్డ… | P022-F002, F003 | — |  |
| F258 | formation-ages | చంద్రుడి పుట్టుకపై పాత సిద్ధాంతాలు: Fission (George Darwin), Capture, Co-accreti… | P022-F004 | — |  |
| F259 | formation-hypotheses | సూర్యుడిని తోకచుక్క ఢీకొట్టి గ్రహాలు పుట్టాయని Buffon 1749 లో చెప్పాడు. | P003-F020 | — |  |
| F260 | formation-hypotheses | Nebular hypothesis ను Immanuel Kant 1755 లో, Pierre-Simon Laplace 1796 లో ప్రతిప… | P003-F016, P003-M005 | N052 |  |
| F261 | formation-hypotheses | Planetesimal hypothesis ను T. C. Chamberlin, F. R. Moulton ప్రతిపాదించారు. | P003-F017 | — |  |
| F262 | formation-hypotheses | Tidal hypothesis ను James Jeans ప్రతిపాదించాడు; Harold Jeffreys దాన్ని సవరించాడు… | P003-F018 | N052 |  |
| F263 | formation-hypotheses | Binary star hypothesis ను Henry Norris Russell చెప్పాడు; R. A. Lyttleton దాన్ని … | P003-M006 (partial) | N052 |  |
| F264 | formation-hypotheses | Interstellar dust hypothesis ను Otto Schmidt (రష్యా) 1944 లో ప్రతిపాదించాడు. | — | — | duplicate of a fact tested elsewhere (Otto Schmidt 1944: P003-F019, N055) |
| F265 | formation-hypotheses | Meteoritic hypothesis ను Norman Lockyer 1890 లో "The Meteoritic Hypothesis" పుస్… | P003-F021 | — |  |
| F266 | formation-hypotheses | సూర్యుడు, గ్రహాలు ఒకే మేఘం నుంచి పుట్టాయనే సిద్ధాంతాలు Monistic; రెండో వస్తువు స… | — | N052 |  |
| F267 | formation-kant-laplace | వేగం పెరిగిన Nebula నుంచి Rings విడిపోయి గ్రహాలయ్యాయని Laplace (1796) చెప్పాడు. | P003-F016 | — |  |
| F268 | formation-kant-laplace | సూర్యుడిలో Mass ఎక్కువైనా Angular momentum గ్రహాల దగ్గర ఎక్కువగా ఉండటాన్ని Angul… | — | N053 |  |
| F269 | formation-kant-laplace | Angular momentum బలం కాదు; అది Mass, వేగం, మధ్య నుంచి దూరం మీద ఆధారపడే "తిరుగుడు… | — | N053 |  |
| F270 | formation-kant-laplace | యువ సూర్యుడి Magnetic field, Solar wind కలిసి ఆయన తిరిగే వేగాన్ని తగ్గించడాన్ని … | — | N053 |  |
| F271 | formation-encounter | Planetesimal hypothesis ప్రకారం దగ్గరగా వెళ్లిన నక్షత్రం సూర్యుడి నుంచి లాగిన పద… | P003-F017 | N054 |  |
| F272 | formation-encounter | Tidal hypothesis ప్రకారం దగ్గరగా వెళ్లిన నక్షత్రం సూర్యుడి నుంచి చుట్ట (Cigar) ఆ… | P003-F018 | N054 |  |
| F273 | formation-encounter | Ross Gunn తన "On the Origin of the Solar System" పత్రాన్ని 1932 జనవరి 15 న Physi… | P003-F023 | — |  |
| F274 | formation-encounter | Henry Norris Russell 1935 లో "The Solar System and Its Origin" పుస్తకంలో సూర్యుడ… | P003-F022 | — |  |
| F275 | formation-encounter | సూర్యుడి నుంచి లాగిన వేడి వాయువు గ్రహాలుగా గడ్డకట్టకుండా చెల్లాచెదురవుతుందని 193… | — | N054 |  |
| F276 | formation-schmidt-weizsacker | Otto Schmidt (రష్యా) 1944 లో సూర్యుడు పట్టుకున్న వాయువు–ధూళి మేఘం నుంచి గ్రహాలు … | P003-F019 | N055 |  |
| F277 | formation-schmidt-weizsacker | Otto Schmidt 1948 లో ఇచ్చిన నాలుగు ఉపన్యాసాలు 1949 లో "A Theory of Earth's Origi… | P003-F024 | — |  |
| F278 | formation-schmidt-weizsacker | Carl Friedrich von Weizsäcker (జర్మనీ) 1944 లో Nebula లోని సుడుల (Eddies) మధ్య గ… | P003-F019 | N055 |  |
| F279 | formation-schmidt-weizsacker | Planetesimals నుంచి గ్రహాలు పెరిగే ఆధునిక నమూనాకు Viktor Safronov పునాది వేశాడు. | — | N055 |  |
| F280 | formation-schmidt-weizsacker | గ్రహాల మధ్య దూరాలు ఒక క్రమంలో పెరగడాన్ని Titius–Bode law అంటారు. | — | N055 |  |
| F281 | formation-planet-definition | గ్రహం (Planet) నిర్వచనాన్ని IAU 2006 ఆగస్టు 24 న Prague లో ఆమోదించింది. | P010-F006 | — |  |
| F282 | formation-planet-definition | IAU నిర్వచనం ప్రకారం గ్రహం సూర్యుడి చుట్టూ తిరగాలి, సొంత Gravity తో దాదాపు గుండ్… | SP-009, P005-F001 | N056, N057 |  |
| F283 | formation-planet-definition | మొదటి రెండు నియమాలు ఉండి, Orbit దారిని ఖాళీ చేసుకోని, Satellite కాని వస్తువును D… | P005-F002, SP-011, SP-093 | N056 |  |
| F284 | formation-planet-definition | IAU గుర్తించిన ఐదు Dwarf planets: Ceres, Pluto, Haumea, Makemake, Eris. | P005-F004 | N058 |  |
| F285 | formation-planet-definition | గ్రహమూ కాని, Dwarf planet కూ కాని, Satellite కూ కాని సూర్యుడి చుట్టూ తిరిగే చిన్… | — | N056 |  |
| F286 | formation-pluto-reclassification | Pluto ను 1930 లో Lowell Observatory లో Clyde Tombaugh కనుగొన్నాడు; పేరు సూచించిం… | P009-F001 | N059 |  |
| F287 | formation-pluto-reclassification | Pluto అతి పెద్ద చంద్రుడు Charon; 2015 లో New Horizons Pluto దగ్గరగా వెళ్లింది. | — | N059 |  |
| F288 | formation-pluto-reclassification | Neptune అవతల ఉండే Dwarf planets ను Plutoids అంటారు (2008): Pluto, Eris, Makemake… | — | N058 |  |
| F289 | formation-pluto-reclassification | Ceres ను 1801 లో Giuseppe Piazzi, Eris ను 2005 లో Mike Brown బృందం కనుగొన్నారు. | — | N058 |  |
| F290 | formation-pluto-reclassification | Orbit దారిని ఖాళీ చేసుకోనందుకు IAU 2006 లో Pluto ను Dwarf planet గా గుర్తించింది… | P005-F003 | N057 |  |
| F291 | sun-what | సూర్యుడు ఒక నక్షత్రం (Star); ఆయన వర్గం G2 V (G-type main-sequence star, Yellow d… | P006-F006 | — |  |
| F292 | sun-what | నక్షత్రాల వర్గాలు వేడి నుంచి చల్లని వైపు: O, B, A, F, G, K, M. సూర్యుడు G వర్గం. | P006-F006 (class) | — |  |
| F293 | sun-what | Mass ప్రకారం సూర్యుడిలో సుమారు 73% Hydrogen, సుమారు 25% Helium ఉన్నాయి. | P006-F007 | N060 |  |
| F294 | sun-what | ఆవేశ కణాలుగా విడిపోయిన వేడి వాయువును Plasma అంటారు. ఇది పదార్థం నాలుగో స్థితి. స… | — | N060 |  |
| F295 | sun-what | సూర్యుడి Diameter సుమారు 13.9 లక్షల km. ఇది భూమి Diameter కు సుమారు 109 రెట్లు. | P006-F009 | N060 |  |
| F296 | sun-what | సూర్యుడి Mass భూమి Mass కు సుమారు 3,33,000 రెట్లు; Volume సుమారు 13 లక్షల రెట్లు… | P006-F010, F011 | — |  |
| F297 | sun-what | భూమి నుంచి సూర్యుడి సగటు దూరం సుమారు 15 కోట్ల km. దీన్ని 1 AU (Astronomical Unit… | P004-F033 | — |  |
| F298 | sun-what | Solar System మొత్తం Mass లో సుమారు 99.8% సూర్యుడిదే. | — | N060 |  |
| F299 | sun-what | సూర్యుడి వయస్సు సుమారు 460 కోట్ల సంవత్సరాలు (4.6 billion years). | P002-F012 | — |  |
| F300 | sun-what | సూర్యుడి Equator సుమారు 25 రోజుల్లో, ధ్రువ ప్రాంతాలు సుమారు 36 రోజుల్లో తిరుగుతా… | P006-F012 | — |  |
| F301 | sun-what | సూర్యుడు Milky Way కేంద్రం చుట్టూ ఒకసారి తిరగడానికి సుమారు 23 కోట్ల సంవత్సరాలు ప… | P006-F013 | — |  |
| F302 | sun-fusion | సూర్యుడి శక్తికి మూలం Core లో జరిగే Nuclear fusion (కేంద్రక సంలీనం). | SP-013, P006-F008 | N061 |  |
| F303 | sun-fusion | Nuclear fusion లో నాలుగు Hydrogen Nuclei (Protons) కలిసి ఒక Helium Nucleus ఏర్పడ… | SP-013 | N061 |  |
| F304 | sun-fusion | E = mc² లో E = శక్తి, m = Mass, c = కాంతి వేగం. | — | N061 |  |
| F305 | sun-interior | సూర్యుడి లోపలి పొరల క్రమం: Core → Radiative zone → Convective zone. | SP-014, P006-F021 | — |  |
| F306 | sun-interior | Radiative zone లో శక్తి Radiation ద్వారా ప్రయాణిస్తుంది. Convective zone లో Conv… | P006-F015, F016 | N062 |  |
| F307 | sun-interior | Radiative zone Temperature లోపల సుమారు 70 లక్షల °C నుంచి బయట సుమారు 20 లక్షల °C … | — | N062 |  |
| F308 | sun-interior | Core లో పుట్టిన శక్తి Radiative zone ను దాటడానికే సుమారు 1,70,000 సంవత్సరాలు పడు… | — | N062 |  |
| F309 | sun-atmosphere | సూర్యుడి వాతావరణ పొరల క్రమం (లోపల నుంచి బయటకు): Photosphere → Chromosphere → Tra… | P006-F018, F019, F021 | — |  |
| F310 | sun-atmosphere | మనకు కనిపించే సూర్యకాంతి ఎక్కువగా Photosphere (కాంతిమండలం) నుంచి వస్తుంది. దాని … | SP-015, P006-F017 | N063 |  |
| F311 | sun-atmosphere | సంపూర్ణ సూర్యగ్రహణంలో అంచు చుట్టూ ఎర్రగా కనిపించే పొర Chromosphere. ఆ ఎరుపు వేడి… | — | N063 |  |
| F312 | sun-atmosphere | Chromosphere, Corona మధ్య ఉండే సన్నని పొరను Transition region అంటారు. ఇందులో Tem… | P006-F019 | — |  |
| F313 | sun-atmosphere | Corona (కిరీట వాతావరణం) సూర్యుడి అత్యంత బయటి పొర. దాని Temperature లక్షల డిగ్రీల… | P006-F020, SP-017 | — |  |
| F314 | sun-atmosphere | Corona ను సంపూర్ణ సూర్యగ్రహణ సమయంలో లేదా Coronagraph తో చూడవచ్చు. | — | N063 |  |
| F315 | sun-atmosphere | Aditya-L1 భారత్ మొదటి సౌర యాత్ర. ISRO దీన్ని 2 సెప్టెంబర్ 2023 న ప్రయోగించింది. … | SP-089, P007-F010 | — |  |
| F316 | sun-temperature-exam | సూర్యుడి Effective temperature సుమారు 5,800 K (సుమారు 5,500°C). | EXT-0176 (as 5778 K) | N064 |  |
| F317 | sun-temperature-exam | IAU 2015 Resolution B3 సూర్యుడి Nominal effective temperature ను 5772 K గా నిర్ణ… | — | N064 |  |
| F318 | sun-temperature-exam | పాత పుస్తకాలు, పాత పరీక్షల జవాబు కీల్లో సూర్యుడి Temperature 5778 K గా ఉంది. | EXT-0176 | N064 |  |
| F319 | sun-spectrum | సూర్యకాంతి Spectrum లో కనిపించే నల్లని Absorption lines ను Fraunhofer lines అంటా… | P007-F009 | N066 |  |
| F320 | sun-spectrum | Fraunhofer lines సూర్యుడి వాతావరణంలోని వాయువులు కొన్ని Wavelengths ను పీల్చుకోవడ… | — | N066 |  |
| F321 | sun-spectrum | ఈ గీతలను 1802 లో Wollaston మొదట చూశాడు. 1814 నుంచి Fraunhofer 500 కి పైగా గీతలను… | — | N065 |  |
| F322 | sun-spectrum | 1859 లో Kirchhoff, Bunsen ఈ నల్లని గీతలు మూలకాలు వెలుగును పీల్చుకోవడం వల్ల వస్తా… | — | N065, N066 |  |
| F323 | sun-spectrum | 18 ఆగస్టు 1868 సూర్యగ్రహణాన్ని Pierre Janssen గుంటూరు నుంచి పరిశీలించి కొత్త పసు… | — | N065 |  |
| F324 | sun-sunspots-cycle | Photosphere లో చుట్టూ కంటే తక్కువ వేడిగా ఉండే ప్రాంతాలు నల్లగా కనిపిస్తాయి. వాటి… | SP-016, P007-F007 | N067 |  |
| F325 | sun-sunspots-cycle | Sunspot మధ్యలోని నల్లని భాగం Umbra; చుట్టూ ఉన్న తేలికైన భాగం Penumbra. | — | N067 |  |
| F326 | sun-sunspots-cycle | Sunspots లో బలమైన Magnetic field వేడి Plasma పైకి రావడాన్ని అడ్డుకుంటుంది. అందుక… | — | N067 |  |
| F327 | sun-sunspots-cycle | Chromosphere లో ప్రకాశంగా కనిపించే Magnetic చురుకైన ప్రాంతాలను Plages అంటారు. | P007-F008 | — |  |
| F328 | sun-sunspots-cycle | Sunspots సంఖ్య సుమారు 11 సంవత్సరాలకు ఒకసారి పెరిగి తగ్గుతుంది. దీన్ని Solar cycl… | — | N068 |  |
| F329 | sun-sunspots-cycle | Sunspot cycle ను 1843 లో Heinrich Schwabe ప్రచురించాడు. | — | N068 |  |
| F330 | sun-sunspots-cycle | సూర్యుడి Magnetic poles సుమారు 11 ఏళ్లకు ఒకసారి తారుమారవుతాయి. పూర్తి అయస్కాంత చ… | — | N068 |  |
| F331 | sun-sunspots-cycle | Solar Cycle 25 గరిష్ఠ దశ (Solar maximum) కు చేరిందని NASA, NOAA 2024 అక్టోబర్‌లో… | — | N068 |  |
| F332 | sun-wind-flare-cme | సూర్యుడి Corona నుంచి నిరంతరం ప్రవహించే Charged particles (ప్రధానంగా Protons, El… | SP-018, P007-F001 | — |  |
| F333 | sun-wind-flare-cme | Magnetic శక్తి ఒక్కసారిగా విడుదలై Electromagnetic radiation అకస్మాత్తుగా పెరగడాన… | P007-F002, SP-092 | — |  |
| F334 | sun-wind-flare-cme | Corona నుంచి భారీ Plasma మేఘం Magnetic field తో కలిసి అంతరిక్షంలోకి దూసుకుపోవడాన… | P007-F003, SP-092 | — |  |
| F335 | sun-wind-flare-cme | Solar flare లను బలాన్ని బట్టి A, B, C, M, X తరగతులుగా విభజిస్తారు. X అత్యంత బలమై… | — | N069 |  |
| F336 | sun-wind-flare-cme | Magnetic field పట్టి ఉంచిన Plasma తోరణాలను Prominences అంటారు. సూర్యబింబం ముందు … | — | N069 |  |
| F337 | sun-storms-aurora | భూమి చుట్టూ ఉన్న అయస్కాంత ప్రాంతాన్ని Magnetosphere అంటారు. ఇది Solar wind లోని … | — | N070 |  |
| F338 | sun-storms-aurora | సూర్యుడి నుంచి వచ్చే హానికర UV, X-rays ను భూమి Atmosphere పీల్చుకుంటుంది; UV ని … | — | — | duplicate of a fact tested elsewhere (ozone blocks UV: N076) |
| F339 | sun-storms-aurora | బలమైన CME భూమి Magnetosphere ను ఢీకొన్నప్పుడు Geomagnetic storm (భూ అయస్కాంత తుఫ… | — | N070 |  |
| F340 | sun-storms-aurora | సౌర తుఫానులు Satellites, Radio సమాచారం, GPS, విద్యుత్ వ్యవస్థలను దెబ్బతీయగలవు. | — | — | in N070 table (storm effects) |
| F341 | sun-storms-aurora | సూర్యుడి నుంచి వచ్చిన శక్తివంతమైన కణాలు పై వాతావరణంలోని Oxygen, Nitrogen ను ఢీకొ… | P007-F004 | — |  |
| F342 | sun-storms-aurora | ఉత్తర అర్ధగోళంలోని Aurora ను Aurora borealis, దక్షిణ అర్ధగోళంలోని Aurora ను Auro… | P007-F005, F006 | — |  |
| F343 | sun-storms-aurora | Aurora లో ఆకుపచ్చ, ఎరుపు రంగులు Oxygen నుంచి; నీలం, గులాబీ రంగులు Nitrogen నుంచి… | — | N070 |  |
| F344 | sun-storms-aurora | 1 సెప్టెంబర్ 1859 న Richard Carrington ఒక పెద్ద Flare ను చూశాడు. దాని తరువాత వచ్… | — | N070 |  |
| F345 | inner-rocky | Mercury (బుధుడు), Venus (శుక్రుడు), భూమి (Earth), Mars (కుజుడు) లను Rocky planet… | P005-F008 | — |  |
| F346 | inner-rocky | సూర్యుడికి, Asteroid Belt కు మధ్య ఉన్నందున ఈ నాలుగు గ్రహాలను Inner planets అని క… | EXT-0175, P005-F006 | — |  |
| F347 | inner-rocky | Terrestrial planets సూర్యుడికి దగ్గరి వేడి ప్రాంతంలో ఏర్పడ్డాయి. అక్కడ రాయి, లోహ… | P005-F008 | — |  |
| F348 | inner-rocky | సౌర కుటుంబం ఏర్పడిన వాయువు–ధూళి పళ్లాన్ని Solar nebula అంటారు. | — | — | definition (solar nebula) used in N108 |
| F349 | inner-rocky | Jupiter, Saturn లను Gas giants అంటారు; Uranus, Neptune లను Ice giants అంటారు. ఈ … | SP-012 | — |  |
| F350 | inner-motion | గ్రహం తన Axis చుట్టూ తాను తిరగడాన్ని Rotation (భ్రమణం) అంటారు; సూర్యుడి చుట్టూ త… | SP-037 | — |  |
| F351 | inner-motion | ఒక సూర్యోదయం నుంచి తరువాతి సూర్యోదయం వరకు పట్టే కాలాన్ని Solar day (సౌర దినం) అం… | — | — | definition (solar day) used in N106 |
| F352 | inner-motion | గ్రహం Axis, Orbital plane కు లంబంగా ఉన్న రేఖతో చేసే కోణాన్ని Axial tilt (అక్ష వం… | P008-F025, P008-M007 | — |  |
| F353 | inner-motion | భూమి Orbit ఉన్న తలాన్ని Ecliptic plane అంటారు. | — | — | definition (ecliptic plane) used in N108 |
| F354 | inner-motion | ఉత్తర అర్ధగోళంలో Summer solstice సుమారు జూన్ 21, Winter solstice సుమారు డిసెంబర్… | — | — | duplicate of a fact tested elsewhere (solstice/equinox dates: SP-050, SP-051, N113, N114) |
| F355 | inner-mercury | సూర్యుడికి అతి దగ్గరి గ్రహం, ఎనిమిది గ్రహాల్లో అతి చిన్న గ్రహం Mercury (బుధుడు). | SP-019 | — |  |
| F356 | inner-mercury | Mercury (బుధుడు) చుట్టూ ఉండే అతి పలుచని వాయు పొరను Exosphere అంటారు. | P007-F015 | — |  |
| F357 | inner-mercury | బుధుడి (Mercury) Solar day సుమారు 176 భూ రోజులు; ఇది దాని సంవత్సరం (సుమారు 88 రో… | — | N071 |  |
| F358 | inner-mercury | ఎనిమిది గ్రహాల్లో Orbit Eccentricity అత్యధికంగా ఉన్నది Mercury (బుధుడు), సుమారు … | P007-F018 | N072 |  |
| F359 | inner-mercury | బుధుడి (Mercury) Rotation, Revolution మధ్య 3:2 Spin-orbit resonance ఉంది: 2 Revo… | — | N071 |  |
| F360 | inner-mercury | గ్రహం సూర్యుడికి అత్యంత దగ్గరి స్థానం Perihelion; అత్యంత దూరపు స్థానం Aphelion. | P022-F012 (lunar analogue only) | — |  |
| F361 | inner-mercury | వృత్తానికి అత్యంత దగ్గరి Orbit (Eccentricity అత్యల్పం) శుక్రుడి (Venus)ది, సుమార… | — | N072 |  |
| F362 | inner-mercury | బుధుడి (Mercury) Axial tilt సుమారు 0.034° (= 2′); ధ్రువాల దగ్గరి నీడ గుంతల్లో Wa… | P008-F027 | N072 |  |
| F363 | inner-mercury | బుధుడికి (Mercury) Natural moons లేవు. | P004-F076, P007-F017 | N072 |  |
| F364 | inner-venus | Size, Mass లో భూమికి దగ్గరగా ఉండటం వల్ల శుక్రుడిని (Venus) భూమి జంట గ్రహం (Earth… | SP-084, P011-F016, EXT-0138 | — |  |
| F365 | inner-venus | శుక్రుడి (Venus) Atmosphere లో సుమారు 96.5% Carbon dioxide ఉంటుంది; దాని మేఘాలు … | P007-F019 | N073 |  |
| F366 | inner-venus | ఎనిమిది గ్రహాల్లో అత్యంత వేడి గ్రహం Venus (శుక్రుడు); సగటు నేల Temperature సుమార… | P005-F013, P004-F064 | N073 |  |
| F367 | inner-venus | Venus (శుక్రుడు) Retrograde rotation చేస్తుంది; అందుకే అక్కడ సూర్యుడు పడమరన ఉదయి… | P007-F020, SP-040 | — |  |
| F368 | inner-venus | తన Axis మీద అత్యంత నెమ్మదిగా తిరిగే గ్రహం Venus (శుక్రుడు); ఒక Rotation కు సుమార… | SP-039, P011-F013 | — |  |
| F369 | inner-venus | శుక్రుడి (Venus) మీద ఎత్తైన పర్వత శ్రేణి Maxwell Montes (సుమారు 11 km). | — | N073 |  |
| F370 | inner-venus | శుక్రుడిని (Venus) Morning star (వేగుచుక్క), Evening star అంటారు; అది నక్షత్రం క… | P011-F016 (explanation) | — |  |
| F371 | inner-venus | Venus నేల పటాన్ని Radar తో తయారుచేసింది NASA Magellan (1990–1994); Venus మీద దిగ… | P007-F021 (radar) | N073 |  |
| F372 | inner-greenhouse | Atmosphere లోని వాయువులు నేల నుంచి వెలువడే Infrared radiation ను పట్టి ఉంచి నేలన… | SP-020 | N075 |  |
| F373 | inner-greenhouse | దట్టమైన CO₂ Atmosphere వల్ల కలిగే బలమైన Greenhouse effect కారణంగా Venus (శుక్రుడ… | SP-020 | — |  |
| F374 | inner-greenhouse | ముఖ్యమైన Greenhouse gases: Water vapour, CO₂, Methane, Nitrous oxide, Ozone, CFC… | — | N075 |  |
| F375 | inner-earth | ఎనిమిది గ్రహాల్లో సగటు Density (Mean density) అత్యధికంగా ఉన్న గ్రహం భూమి (Earth)… | P004-F013, P004-F057 | N102 |  |
| F376 | inner-earth | భూమి ఉపరితల వైశాల్యంలో సుమారు 71% నీరు, సుమారు 29% నేల ఉంటుంది. | P007-F022, F023 | — |  |
| F377 | inner-earth | భూమి Magnetic field సూర్యుడి నుంచి వచ్చే Charged particles ను పక్కకు మళ్లిస్తుంద… | — | N076 |  |
| F378 | inner-earth | భూమి పొరలు: Crust, Mantle, Outer core (ద్రవం), Inner core (ఘనం). | P002-M002 (partial) | N003 |  |
| F379 | inner-earth | గ్రహం మీద నీరు ద్రవంగా ఉండగలిగే దూరపు పట్టీని Habitable zone (Goldilocks zone) అ… | — | N076 |  |
| F380 | inner-earth | Ozone పొర సూర్యుడి నుంచి వచ్చే హానికరమైన Ultraviolet (UV) కిరణాలను అడ్డుకుంటుంది… | — | N076 |  |
| F381 | inner-earth-shape | ధ్రువాల దగ్గర కొంచెం చదునుగా, భూమధ్యరేఖ దగ్గర కొంచెం ఉబ్బినట్టు ఉండే భూమి ఆకారాన… | — | N077, N158 |  |
| F382 | inner-earth-shape | భూమి భూమధ్యరేఖ వ్యాసం (Equatorial diameter) సుమారు 12,756 km; ధ్రువ వ్యాసం సుమార… | — | N158 | duplicate of a fact tested elsewhere (Earth diameters: SP-048, N077) |
| F383 | inner-earth-shape | భూమి తన Axis మీద తిరగడం (Rotation) వల్ల పగలు, రాత్రి ఏర్పడతాయి. | P004-F011 | — |  |
| F384 | inner-earth-shape | భూమి చుట్టుకొలతను మొదటిసారి లెక్కించినది Eratosthenes (సుమారు క్రీ.పూ. 240); చంద… | — | N002 |  |
| F385 | inner-mars | Mars నేల, ధూళిలోని Iron oxide (ఇనుప తుప్పు) వల్ల అది ఎర్రగా కనిపిస్తుంది; అందుకే… | SP-021, P008-F001 | — |  |
| F386 | inner-mars | కుజుడికి (Mars) పలుచని Atmosphere ఉంది; అందులో ప్రధాన వాయువు Carbon dioxide (సుమ… | P008-F002 | — |  |
| F387 | inner-mars | కుజుడి (Mars) Axial tilt సుమారు 25.2°; అందుకే అక్కడ కూడా ఋతువులు ఏర్పడతాయి. | P008-F003 | — |  |
| F388 | inner-mars | కుజుడి (Mars) ధ్రువాల దగ్గర మంచు టోపీలు (Polar ice caps) ఉన్నాయి; ఇవి ఎక్కువగా న… | — | N078 |  |
| F389 | inner-mars | Mars నేల కింద నీటి మంచు ఉందని 2008 లో NASA Phoenix lander నిర్ధారించింది. | — | N078 |  |
| F390 | inner-mars | 2018 లో NASA Curiosity rover, Mars మీది Gale crater రాళ్లలో Organic molecules కన… | P008-F007 (inference only) | N078 |  |
| F391 | inner-mars-features | Olympus Mons కుజుడి (Mars) మీద ఉన్న, సౌర కుటుంబంలో తెలిసిన అతి పెద్ద Volcano. | P008-F005 | — |  |
| F392 | inner-mars-features | Olympus Mons ఒక Shield volcano; దాని ఎత్తు Everest కు దాదాపు మూడు రెట్లు. | — | N079 |  |
| F393 | inner-mars-features | Valles Marineris కుజుడి (Mars) మీద ఉన్న, సౌర కుటుంబంలో అతి పెద్ద Canyon system (… | P008-F006 | N079 |  |
| F394 | inner-mars-features | కుజుడికి (Mars) Phobos, Deimos అనే రెండు Natural moons ఉన్నాయి; వీటిని 1877 లో A… | SP-022, P008-F004 | N079 |  |
| F395 | inner-mars-features | కుజుడి (Mars) రెండు చంద్రుల్లో పెద్దది Phobos; చిన్నది Deimos. | — | N079 |  |
| F396 | inner-compare | Natural moons సంఖ్య: Mercury (బుధుడు) 0, Venus (శుక్రుడు) 0, భూమి (Earth) 1, Mar… | P004-F076–F079 | — |  |
| F397 | inner-compare | నాలుగు రాతి గ్రహాల్లో అతి పెద్దది భూమి (Earth); అతి చిన్నది Mercury (బుధుడు). | P005-F018 | — |  |
| F398 | outer-giants | Jupiter (గురుడు), Saturn (శని) లను Gas giants అంటారు; వీటిలో ఎక్కువ భాగం Hydroge… | P005-F009, SP-012 | N080 |  |
| F399 | outer-giants | నాలుగు Giant planets కూ భూమిలాంటి గట్టి నేల (Solid surface) లేదు. | — | N080 |  |
| F400 | outer-giants | Jupiter (గురుడు), Saturn (శని), Uranus (యురేనస్), Neptune (నెప్ట్యూన్) లను Giant… | SP-012 | N080 |  |
| F401 | outer-colours | Uranus (యురేనస్) Atmosphere లోని Methane ఎరుపు కాంతిని పీల్చుకోవడం వల్ల అది Blue… | P008-F019 | — |  |
| F402 | outer-colours | Neptune (నెప్ట్యూన్) సహజ రంగు లేత Greenish-blue; Voyager 2 పాత చిత్రాల్లో గాఢ నీ… | SP-030, P008-F026 | — |  |
| F403 | outer-colours | Jupiter (గురుడు) పై తెలుపు, గోధుమ, నారింజ Cloud bands; Saturn (శని) పై లేత పసుపు… | P008-F036, F037 | — |  |
| F404 | outer-rings | Jupiter (గురుడు), Saturn (శని), Uranus (యురేనస్), Neptune (నెప్ట్యూన్) — నాలుగు … | SP-027, P005-F017 | — |  |
| F405 | outer-rings | Saturn (శని) Rings ప్రధానంగా మంచు ముక్కలతో, కొంత రాయి, ధూళితో ఏర్పడ్డాయి. | P008-F015 | — |  |
| F406 | outer-rings | Jupiter (గురుడు) Rings ను 1979 లో Voyager 1 కనుగొంది. | — | N081 |  |
| F407 | outer-rings | Saturn (శని) వలయాలను 1610 లో Galileo మొదట చూశాడు; అవి వలయాలు అని 1655 లో Christi… | — | N081 |  |
| F408 | outer-rings | Saturn (శని) A ring, B ring మధ్య ఉన్న ఖాళీని Cassini Division అంటారు; దాన్ని 167… | — | N081 |  |
| F409 | outer-rings | Saturn (శని) ప్రధాన వలయాలు A, B, C; అన్నింటికంటే బయటి మసక వలయం E ring. | — | — | low exam value (A, B, C, E rings) |
| F410 | outer-jupiter | Jupiter (గురుడు) Diameter, Mass రెండింటిలో Solar System లో అతి పెద్ద గ్రహం. | P008-F010, P004-F019 | — |  |
| F411 | outer-jupiter | Jupiter (గురుడు) తన Axis పై సుమారు 9.9 గంటల్లో ఒకసారి తిరుగుతుంది; ఇది ఎనిమిది గ… | P004-F043, P011-F012 | N082 |  |
| F412 | outer-jupiter | Great Red Spot అనేది Jupiter (గురుడు) Atmosphere లోని భారీ తుఫాను (Storm). దీన్న… | P008-F011 | N082 |  |
| F413 | outer-jupiter | Great Red Spot ఇప్పుడు భూమి వెడల్పుకు సుమారు 1.3 రెట్లు; ఇది నెమ్మదిగా చిన్నదవుత… | — | N082 |  |
| F414 | outer-jupiter | Jupiter (గురుడు) సూర్యుడిని ఒక చుట్టు చుట్టడానికి సుమారు 11.9 ఏళ్లు, Saturn (శని… | P004-F051, F052 | N082 |  |
| F415 | outer-galilean | Io, Europa, Ganymede, Callisto లను Galilean moons అంటారు; వీటిని Galileo 1610 లో… | P008-F012 | — |  |
| F416 | outer-galilean | Ganymede (గానిమీడ్) Solar System లో అతి పెద్ద చంద్రుడు; దాని Diameter బుధుడి (Me… | SP-025, P008-F013 | N083 |  |
| F417 | outer-galilean | Io (ఐయో) Solar System లో అత్యధిక అగ్నిపర్వత చర్య (Volcanic activity) ఉన్న ప్రదేశ… | SP-026 (distractor) | N084 |  |
| F418 | outer-galilean | Callisto (కాలిస్టో) Solar System లో మూడో పెద్ద చంద్రుడు; దాని ఉపరితలం పూర్తిగా ప… | — | N084 |  |
| F419 | outer-galilean | Io లోపలి వేడికి కారణం Tidal heating; Jupiter Gravity దాన్ని పదే పదే సాగదీసి, ముడ… | — | N084 |  |
| F420 | outer-galilean | Europa (యూరోపా) మంచు పొర కింద ఉప్పు నీటి సముద్రం ఉందని బలమైన ఆధారాలు ఉన్నాయి. | SP-026 (distractor) | N084 |  |
| F421 | outer-saturn | Saturn (శని) Mean density సుమారు 0.69 g/cm³; ఇది నీటి Density కంటే తక్కువ, ఎనిమి… | P004-F060, P004-F014 | N085, N102, N159 |  |
| F422 | outer-saturn | Titan (టైటాన్) Saturn (శని) చంద్రుల్లో అతి పెద్దది; దానికి దట్టమైన Nitrogen Atmo… | P008-F014 | — |  |
| F423 | outer-saturn | Titan ఉపరితలంపై ద్రవ Methane, Ethane సరస్సులు, సముద్రాలు ఉన్నాయి. భూమి తరువాత ఉప… | SP-026 | — |  |
| F424 | outer-saturn | Cassini Spacecraft 2004 లో Saturn చేరి 2017 వరకు పనిచేసింది; దానితో వెళ్లిన Huyg… | — | N085 |  |
| F425 | outer-saturn | Saturn (శని) ఏడు పెద్ద చంద్రులు: Mimas, Enceladus, Tethys, Dione, Rhea, Titan, I… | P008-F016 | — |  |
| F426 | outer-saturn | Enceladus (ఎన్సెలడస్) దక్షిణ ధ్రువం నుంచి నీటి ఆవిరి, మంచు కణాల Plumes వస్తాయి; … | — | N085 |  |
| F427 | outer-uranus | Uranus (యురేనస్) ను William Herschel 1781 లో Telescope తో కనుగొన్నాడు. | P008-F017 | — |  |
| F428 | outer-uranus | Uranus (యురేనస్) Axial tilt సుమారు 98°; అందుకే అది పక్కకు ఒరిగి తిరుగుతున్నట్లు … | SP-028, P008-F018 | N157 |  |
| F429 | outer-uranus | Uranus (యురేనస్), Venus (శుక్రుడు) Retrograde rotation చేస్తాయి; అంటే చాలా గ్రహా… | P004-F045 | N157 |  |
| F430 | outer-uranus | Uranus (యురేనస్) ను 1986 లో, Neptune (నెప్ట్యూన్) ను 1989 లో సందర్శించిన ఏకైక Sp… | — | N086 |  |
| F431 | outer-uranus | భూమితో సహా చాలా గ్రహాలు పడమర నుంచి తూర్పుకు తిరుగుతాయి; Uranus (యురేనస్), Venus … | — | N157 | duplicate of a fact tested elsewhere (retrograde rotation: SP-040, N107) |
| F432 | outer-uranus | Uranus (యురేనస్) ఐదు ప్రధాన చంద్రులు Miranda, Ariel, Umbriel, Titania, Oberon; వ… | P008-F020 | N086 |  |
| F433 | outer-neptune | Neptune (నెప్ట్యూన్) స్థానాన్ని Le Verrier లెక్కలతో ఊహించాడు; Galle 1846 లో Tele… | P008-F021 | N160 |  |
| F434 | outer-neptune | లెక్కల ద్వారా ముందుగా ఊహించి కనుగొన్న మొదటి గ్రహం Neptune (నెప్ట్యూన్). | — | N087, N160 |  |
| F435 | outer-neptune | Solar System లో అత్యంత వేగమైన గాలులు Neptune (నెప్ట్యూన్) పై వీస్తాయి; గంటకు 2,0… | — | N087 |  |
| F436 | outer-neptune | Great Dark Spot అనేది 1989 లో Voyager 2 Neptune (నెప్ట్యూన్) పై చూసిన పెద్ద తుఫా… | P008-F023 | — |  |
| F437 | outer-neptune | Triton (ట్రైటాన్) Neptune (నెప్ట్యూన్) చంద్రుల్లో అతి పెద్దది; అది Retrograde or… | P008-F022 | N087 |  |
| F438 | outer-moon-counts | NASA ప్రకారం Saturn (శని) కి 293 చంద్రులు ఉన్నాయి (2026 ఆగస్టు నాటికి); ఇది ఏ గ్… | P004-F073, SP-029 | — |  |
| F439 | outer-moon-counts | NASA ప్రకారం Jupiter (గురుడు) కి 115, Uranus (యురేనస్) కి 29, Neptune (నెప్ట్యూన… | P004-F072, F074, F075 | — |  |
| F440 | asteroid-belt | Mars (కుజుడు), Jupiter (గురుడు) Orbits మధ్యలో ఉండే ప్రాంతాన్ని Main Asteroid Bel… | SP-031, P009-F002 | — |  |
| F441 | asteroid-belt | Main Asteroid Belt సూర్యుడి నుంచి సుమారు 2 నుంచి 3.2 AU దూరంలో ఉంది. | — | — | in N088 table (belt at 2–3.2 AU) |
| F442 | asteroid-belt | Asteroids (గ్రహశకలాలు) సుమారు 460 కోట్ల సంవత్సరాల క్రితం Solar System ఏర్పడినప్ప… | P009-F003 | N088 |  |
| F443 | asteroid-belt | Jupiter (గురుడు) Gravity వల్ల Asteroid Belt లో గ్రహం ఏర్పడలేదు. | — | N088 |  |
| F444 | asteroid-belt | Jupiter తో పాటు అదే Orbit లో తిరిగే Asteroids ను Trojan asteroids అంటారు. Orbit … | P009-F005 (NEA only) | N089 |  |
| F445 | asteroid-belt | Asteroids లో మూడు రకాలు: C-type (Carbon), S-type (Stony), M-type (Metallic). వీట… | — | N089 |  |
| F446 | asteroid-belt | అన్ని Asteroids మొత్తం Mass చంద్రుడి Mass కంటే తక్కువ. | — | N088 |  |
| F447 | asteroid-belt | ఈ రోజు అతి పెద్ద Asteroid Vesta (వ్యాసం సుమారు 530 km). Dawn అంతరిక్ష నౌక 2011–2… | — | N089, N090 |  |
| F448 | ceres | Asteroid Belt (ప్రధాన గ్రహశకలాల పట్టీ) లో ఉన్న Dwarf planet (మరుగుజ్జు గ్రహం) Ce… | SP-010, P005-F005, P009-F018 | N090 |  |
| F449 | ceres | Ceres Radius సుమారు 476 km; Diameter సుమారు 950 km. | P009-F004 (largest object) | N091 |  |
| F450 | ceres | Ceres ను Giuseppe Piazzi 1801 లో కనుగొన్నాడు. Asteroid Belt లో కనుగొన్న మొదటి వస… | — | N090 |  |
| F451 | ceres | Asteroid అనే పేరును 1802 లో William Herschel పెట్టాడు. దాని అర్థం "నక్షత్రం లాంట… | — | N091 |  |
| F452 | ceres | NASA ప్రకారం Asteroid Belt మొత్తం Mass లో సుమారు 25% Ceres దే. | — | N090 |  |
| F453 | ceres | NASA Dawn అంతరిక్ష నౌక 2015 లో Ceres ను చేరింది. ఒక Dwarf planet దగ్గరకు వెళ్లిన… | — | N091 |  |
| F454 | kuiper | Kuiper Belt (కైపర్ పట్టీ) Neptune (నెప్ట్యూన్) అవతల, సూర్యుడి నుంచి సుమారు 30 ను… | — | — | in N092 explanation and table (Kuiper Belt 30–50 AU) |
| F455 | kuiper | Kuiper Belt కు Gerard Kuiper (1951) పేరు పెట్టారు. Kenneth Edgeworth (1940ల్లో) … | — | N092 |  |
| F456 | kuiper | Pluto (ప్లూటో) ను 1930 లో Clyde Tombaugh కనుగొన్నాడు. Pluto నే మొదటి Kuiper Belt… | P009-F001 | N092 |  |
| F457 | kuiper | Pluto తరువాత రెండో KBO, 1992 QB1, ను 1992 లో David Jewitt, Jane Luu కనుగొన్నారు. | — | N092 |  |
| F458 | kuiper | Neptune 3 సార్లు సూర్యుడిని చుట్టేసరికి Pluto 2 సార్లు చుట్టుతుంది (3:2 Orbital … | P010-F007 | — |  |
| F459 | kuiper | Eris ను Mike Brown బృందం 2005 లో కనుగొంది. దాని Mass Pluto కంటే కొంచెం ఎక్కువ. | P010-F008 | N092 |  |
| F460 | kuiper | Eris Kuiper Belt అవతల ఉన్న Scattered disc లో ఉన్న Dwarf planet. దాని సగటు దూరం స… | — | N092 |  |
| F461 | kuiper | Jupiter-family comets (20 సంవత్సరాల లోపు) ఎక్కువగా Kuiper Belt నుంచి వస్తాయి. Ha… | P009-F013 | — |  |
| F462 | oort | Oort Cloud (ఊర్ట్ మేఘం) మంచు వస్తువుల Spherical shell (గోళాకార కవచం). ఇది Solar … | SP-032 | N093 |  |
| F463 | oort | Oort Cloud ను Jan Oort 1950 లో ప్రతిపాదించాడు. | — | N093 |  |
| F464 | oort | Long-period comets (200 సంవత్సరాల కంటే ఎక్కువ కాలం) Oort Cloud నుంచి వస్తాయి. | P009-F014 | N093 |  |
| F465 | oort | NASA అంచనా ప్రకారం Oort Cloud లోపలి అంచు సుమారు 2,000 నుంచి 5,000 AU. బయటి అంచు … | — | N093 |  |
| F466 | comet-structure | మంచు, దుమ్ము, రాయి కలిసిన చిన్న వస్తువును Comet (తోకచుక్క, ధూమకేతువు) అంటారు. దీ… | P009-F009 | N094 |  |
| F467 | comet-structure | Comet మధ్యలో ఉండే గట్టి భాగాన్ని Nucleus అంటారు. | P009-F009 | — |  |
| F468 | comet-structure | Comet Orbit బాగా సాగిన Ellipse. అందుకే అది సూర్యుడి దగ్గరకు వచ్చి మళ్లీ దూరంగా వ… | — | — | definition (elongated comet orbit); low value |
| F469 | comet-structure | Solid నేరుగా Gas గా మారడాన్ని Sublimation అంటారు. సూర్యుడి దగ్గర Comet మంచు ఇలాగ… | — | N094 |  |
| F470 | comet-structure | Comet Nucleus చుట్టూ ఏర్పడే Gas, దుమ్ము మేఘాన్ని Coma అంటారు. | P009-F010 | N094 |  |
| F471 | comet-structure | 200 సంవత్సరాల కంటే తక్కువ కాలంలో సూర్యుడిని చుట్టి వచ్చే Comets ను Short-period … | — | — | in N093 table (200-year boundary) |
| F472 | comet-tails | Comet (తోకచుక్క) తోక సూర్యుడికి వ్యతిరేక దిశలో ఉంటుంది. | SP-033, P009-F011 | — |  |
| F473 | comet-tails | Comet కు రెండు తోకలు ఉంటాయి: Ion tail (నీలం, తిన్నగా), Dust tail (తెలుపు/పసుపు, … | P009-M003 (partial) | — |  |
| F474 | comet-tails | Charge ఉన్న Atom లేదా Molecule ను Ion అంటారు. సూర్యుడి UV వెలుగు Comet Gas ను Io… | — | — | definition (ion); low value |
| F475 | comet-tails | Ion tail ను Solar wind సూర్యుడికి సరిగ్గా వ్యతిరేక దిశలో తిన్నగా నెడుతుంది. | P009-F011 | — |  |
| F476 | comet-tails | బరువైన దుమ్ము కణాలు Comet దారి వెంట వెనకబడటం వల్ల Dust tail వంపు తిరిగి ఉంటుంది. | P009-F012 | — |  |
| F477 | comet-tails | Comet సూర్యుడికి దగ్గరయ్యే కొద్దీ తోక పొడవు పెరుగుతుంది; దూరమయ్యే కొద్దీ తగ్గుతు… | — | N094 |  |
| F478 | halley | Halley's Comet (హేలీ తోకచుక్క) సుమారు 76 సంవత్సరాలకు ఒకసారి వచ్చే Short-period c… | P009-F015 | — |  |
| F479 | halley | Comet లేదా గ్రహం సూర్యుడికి అత్యంత దగ్గరగా ఉండే స్థానం Perihelion; అత్యంత దూరంగా… | — | N111 |  |
| F480 | halley | Halley's Comet 1910 లో, తరువాత 1986 లో వచ్చింది. మళ్లీ 2061 లో వస్తుందని అంచనా. | — | N095 |  |
| F481 | halley | Edmond Halley 1705 లో Newton Gravity నియమాలతో లెక్కించి, ఈ Comet 1758 లో తిరిగి … | P009-F016 | — |  |
| F482 | halley | Halley's Comet కాలం గ్రహాల Gravity వల్ల 74.42 నుంచి 79.25 సంవత్సరాల మధ్య మారుతుం… | — | — | in N095 explanation (period 74.42–79.25 years) |
| F483 | halley | 1986 లో ESA అంతరిక్ష నౌక Giotto Halley's Comet Nucleus కు సుమారు 600 km దూరం వరక… | — | — | Giotto 1986 flyby: explanation only (N095); the match question built on it was solvable by sorting years, replaced |
| F484 | halley | Eta Aquariids (మే), Orionids (అక్టోబర్) Meteor showers Halley's Comet దుమ్ము వల్… | — | — | in N095 table (Eta Aquariids, Orionids) |
| F485 | sl9 | Shoemaker–Levy 9 Comet ముక్కలు 16 నుంచి 22 జూలై 1994 మధ్య Jupiter (గురుడు) ను ఢీ… | — | N096 |  |
| F486 | sl9 | Shoemaker–Levy 9 ను Carolyn Shoemaker, Gene Shoemaker, David Levy 1993 లో కనుగొన… | — | N096 |  |
| F487 | sl9 | 1992 లో Jupiter కు చాలా దగ్గరగా వెళ్లినప్పుడు Tidal force వల్ల Shoemaker–Levy 9 … | — | N096 |  |
| F488 | sl9 | Solar System లో రెండు వస్తువులు ఢీకొనడాన్ని మనుషులు నేరుగా గమనించిన మొదటి సంఘటన … | — | N096 |  |
| F489 | meteor-stages | అంతరిక్షంలో తిరిగే చిన్న రాతి లేదా లోహపు ముక్కను Meteoroid (ఉల్కాకణం) అంటారు. IA… | P010-F001 | N097 |  |
| F490 | meteor-stages | Meteoroid భూమి Atmosphere లో మండుతున్నప్పుడు కనిపించే వెలుగు గీతను Meteor (ఉల్క)… | P010-F002, SP-034 | — |  |
| F491 | meteor-stages | Atmosphere లో Meteoroid పై పొర కాలి రాలిపోవడాన్ని Ablation అంటారు. | — | N097, N163 |  |
| F492 | meteor-stages | పూర్తిగా కాలిపోకుండా నేలను చేరిన ముక్కను Meteorite (ఉల్కాశిల) అంటారు. | P010-F003, SP-095 | N163 |  |
| F493 | meteor-stages | Venus (శుక్రుడు) కంటే ఎక్కువ కాంతితో వెలిగే Meteor ను Fireball అంటారు. | — | N097 |  |
| F494 | meteor-stages | Meteorites మూడు రకాలు: Stony, Iron, Stony-iron. అతి పెద్ద Meteorite Hoba (Namibi… | — | N097 |  |
| F495 | meteor-stages | Meteors ఎక్కువగా Mesosphere (సుమారు 50 నుంచి 85 km ఎత్తు) లో మండిపోతాయి. | P010-F004 | N163 |  |
| F496 | small-bodies-compare | Asteroid ప్రధానంగా రాయి, లోహం; Comet లో మంచు ఎక్కువ కాబట్టి సూర్యుడి దగ్గర దానిక… | SP-036 (partial) | N162 |  |
| F497 | small-bodies-compare | సుమారు 1 మీటర్ కంటే చిన్న రాతి ముక్క Meteoroid; అంతకంటే పెద్దది Asteroid. | — | N097, N162 |  |
| F498 | meteor-shower | భూమి Comet (లేదా Asteroid) వదిలిన దుమ్ము దారిని దాటినప్పుడు ఒకేసారి చాలా Meteors… | SP-035 | — |  |
| F499 | meteor-shower | భూమి ఏటా దాదాపు అదే తేదీకి అదే దుమ్ము దారిని దాటుతుంది కాబట్టి Meteor shower ఏటా… | SP-035 | — |  |
| F500 | meteor-shower | Meteor shower కు, దాని Radiant కనిపించే Constellation పేరు పెడతారు (Perseids – P… | — | N098 |  |
| F501 | meteor-shower | Quadrantids జనవరిలో, Lyrids ఏప్రిల్‌లో (Thatcher Comet), Eta Aquariids మేలో, Ori… | — | N098 |  |
| F502 | meteor-shower | Perseids (ఆగస్టు) Swift–Tuttle Comet దుమ్ము వల్ల వస్తాయి. | — | N098 |  |
| F503 | meteor-shower | Leonids (నవంబర్) Tempel–Tuttle Comet దుమ్ము వల్ల వస్తాయి. | — | N098 |  |
| F504 | meteor-shower | Geminids (డిసెంబర్) (3200) Phaethon అనే Asteroid వల్ల వస్తాయి. | — | N098 |  |
| F505 | small-bodies-impacts-missions | సుమారు 6.6 కోట్ల సంవత్సరాల క్రితం Mexico లోని Chicxulub దగ్గర Asteroid ఢీకొనడం D… | — | N099 |  |
| F506 | small-bodies-impacts-missions | 30 జూన్ 1908 న Siberia లోని Tunguska మీద ఒక చిన్న Asteroid లేదా Comet ముక్క గాలి… | — | N099 |  |
| F507 | small-bodies-impacts-missions | Maharashtra లోని Buldhana జిల్లాలో ఉన్న Lonar సరస్సు Basalt రాతిలో Meteorite ఢీక… | — | N099 |  |
| F508 | small-bodies-impacts-missions | Comet మీద మొదటిసారి Lander (Philae) ను దింపిన యాత్ర ESA Rosetta (67P Comet, 2014… | — | N100 |  |
| F509 | small-bodies-impacts-missions | Asteroid నమూనాను భూమికి తెచ్చిన మొదటి యాత్ర JAXA Hayabusa (Itokawa, 2010); NASA … | — | N100 |  |
| F510 | compare-mass-weight | వస్తువులో ఉన్న పదార్థం పరిమాణాన్ని Mass (ద్రవ్యరాశి) అంటారు. దాన్ని kg లో కొలుస్… | SP-047 | — |  |
| F511 | compare-mass-weight | వస్తువు మీద Gravity పెట్టే లాగుడు బలాన్ని Weight (భారం) అంటారు. అది ఒక Force. దా… | — | N101 |  |
| F512 | compare-mass-weight | Weight = Mass × g. భూమి మీద g సుమారు 9.8 m/s²; చంద్రుడి మీద సుమారు 1.6 m/s². | — | N101 |  |
| F513 | compare-mass-weight | Volume (ఘనపరిమాణం) SI ప్రమాణం m³. 1 litre = 1,000 cm³. | — | — | unit fact (m³, litre) in N101 table |
| F514 | compare-mass-weight | Density (సాంద్రత) = Mass ÷ Volume. | — | — | formula in N101 and N102 explanations |
| F515 | compare-mass-weight | చంద్రుడి మీద వస్తువు Mass మారదు. Weight సుమారు ఆరో వంతు అవుతుంది. | SP-047, P022-F009 | N101 |  |
| F516 | compare-diameter | భూమి Equatorial diameter సుమారు 12,756 km. Polar diameter సుమారు 12,714 km. Mean… | SP-048 | N077 |  |
| F517 | compare-diameter | భూమి Equatorial radius సుమారు 6,378 km. Polar radius సుమారు 6,357 km. Mean radiu… | — | N077 |  |
| F518 | compare-diameter | భూమి Equatorial circumference (భూమధ్యరేఖ చుట్టుకొలత) సుమారు 40,075 km. Polar cir… | — | N077 |  |
| F519 | compare-size | Diameter ప్రకారం పెద్ద నుంచి చిన్న: Jupiter (గురుడు), Saturn (శని), Uranus (యురే… | SP-044, P004-F010 | — |  |
| F520 | compare-size | Jupiter (గురుడు), Saturn (శని) ను Gas giants అంటారు. Uranus (యురేనస్), Neptune (… | SP-012 | — |  |
| F521 | compare-size | Uranus (యురేనస్) Diameter Neptune (నెప్ట్యూన్) కంటే ఎక్కువ. కానీ Neptune Mass, D… | SP-045, P008-F024, P004-F021 | — |  |
| F522 | compare-size | Jupiter (గురుడు) Mass భూమికి సుమారు 318 రెట్లు. Volume సుమారు 1,321 రెట్లు. | SP-083 | — |  |
| F523 | compare-size | నాలుగు రాతి గ్రహాల్లో (Terrestrial planets) భూమి (Earth) అతి పెద్దది. ఎనిమిది గ్… | P004-F017 | — |  |
| F524 | compare-motion | Mercury (బుధుడు) సంవత్సరం సుమారు 88 రోజులు. ఎనిమిది గ్రహాల్లో అతి చిన్న సంవత్సరం… | P004-F047, P005-F019 | — |  |
| F525 | compare-motion | Neptune (నెప్ట్యూన్) సంవత్సరం సుమారు 165 భూ సంవత్సరాలు. ఎనిమిది గ్రహాల్లో అతి పె… | P004-F054, P011-F014 | — |  |
| F526 | compare-motion | Venus (శుక్రుడు), Uranus (యురేనస్) Retrograde rotation చూపుతాయి. Venus మీద సూర్య… | P004-F040, SP-040 | — |  |
| F527 | compare-motion | Venus (శుక్రుడు) Sidereal rotation (సుమారు 243 రోజులు) దాని Revolution (సుమారు 2… | P004-F040, P004-F048 | N074 |  |
| F528 | compare-motion | Mercury (బుధుడు) సూర్యుడి చుట్టూ 2 సార్లు తిరిగే లోపు తన Axis మీద 3 సార్లు తిరుగ… | — | N071 |  |
| F529 | compare-motion | భూమి Axis నిలువు గీత నుంచి 23½° (సుమారు 23.4°) వంగి ఉంది. Orbital plane తో అది 6… | SP-054 | — |  |
| F530 | compare-distance | సూర్యుడి నుంచి గ్రహాల క్రమం: Mercury (బుధుడు), Venus (శుక్రుడు), భూమి (Earth), M… | P004-F010 (order), P005-F016 | — |  |
| F531 | compare-distance | Jupiter (గురుడు) సూర్యుడి నుంచి సుమారు 5.2 AU దూరంలో ఉంది. Neptune (నెప్ట్యూన్) … | P004-F027, F030 | — |  |
| F532 | compare-distance | Orbit లో సూర్యుడికి అతి దగ్గరి బిందువు Perihelion; అతి దూరపు బిందువు Aphelion. | — | N111 |  |
| F533 | compare-checklist | పోలిక ప్రశ్నలో జవాబు ఏ లక్షణం (Diameter, Mass, Density, Temperature, Rotation) అ… | — | N102 |  |
| F534 | compare-records-size | Jupiter (గురుడు) Diameter, Mass, Volume మూడింటిలోనూ అతి పెద్ద గ్రహం. | P004-F019, P008-F010 | N102 |  |
| F535 | compare-records-size | Mercury (బుధుడు) ఎనిమిది గ్రహాల్లో అతి చిన్నది. Mars (కుజుడు) రెండో అతి చిన్నది. | SP-019, P004-F015, P004-F018 | — |  |
| F536 | compare-records-size | Ganymede (Jupiter చంద్రుడు) సౌర కుటుంబంలో అతి పెద్ద చంద్రుడు. Titan (Saturn చంద్… | P011-F015 | N083 |  |
| F537 | compare-records-size | Jupiter నాలుగు Galilean moons: Io, Europa, Ganymede, Callisto (Galileo, 1610). | P008-F012 | — |  |
| F538 | compare-records-density | Giant planets లో అత్యధిక Density Neptune (నెప్ట్యూన్) ది (సుమారు 1.64 g/cm³). రా… | P004-F062, P004-F058 | — |  |
| F539 | compare-records-temperature | ఏ గ్రహం Atmosphere లోనైనా నమోదైన అతి తక్కువ Temperature Uranus (యురేనస్) ది: సుమ… | SP-096, P005-F015 | N103 |  |
| F540 | compare-records-temperature | 1 bar level వద్ద సగటు Temperature: Neptune (నెప్ట్యూన్) సుమారు −200°C, Uranus (య… | P004-F069, F070 | N103, N104 |  |
| F541 | compare-records-temperature | Neptune (నెప్ట్యూన్) సూర్యుడి నుంచి తీసుకునే వేడికి సుమారు 2.6 రెట్లు వేడిని బయట… | — | N104 |  |
| F542 | compare-records-spin | Jupiter (గురుడు) తన Axis మీద అతి వేగంగా తిరిగే గ్రహం: సుమారు 9 గంటల 55 నిమిషాలు. | P004-F043, P011-F012 | — |  |
| F543 | compare-records-spin | అతి పొడవైన Solar day Mercury (బుధుడు) ది: సుమారు 176 భూ రోజులు. | SP-094, P007-F016 | — |  |
| F544 | compare-records-moons | Saturn (శని) కి అత్యధిక చంద్రులు: 293 (NASA, 2026 ఆగస్టు నాటికి). | P004-F073 | — |  |
| F545 | compare-records-moons | Mercury (బుధుడు), Venus (శుక్రుడు) కు సహజ చంద్రులు (Natural moons) లేవు. | P004-F076, F077, P007-F017 | — |  |
| F546 | motion-rotation-revolution | గ్రహం తన Axis (అక్షం) చుట్టూ తిరగడాన్ని Rotation (భ్రమణం) అంటారు. Rotation వల్ల … | P004-F011, SP-037 | — |  |
| F547 | motion-rotation-revolution | భూమి పశ్చిమం నుంచి తూర్పుకు Rotation చేస్తుంది. Equator దగ్గర ఈ వేగం గంటకు సుమార… | — | N105 |  |
| F548 | motion-rotation-revolution | గ్రహం సూర్యుడి చుట్టూ Orbit (కక్ష్య) లో తిరగడాన్ని Revolution (పరిభ్రమణం) అంటారు… | P004-F012 | — |  |
| F549 | motion-rotation-revolution | భూమి Revolution కాలం సుమారు 365¼ రోజులు. Revolution వేగం సెకనుకు సుమారు 30 km. | — | N105 |  |
| F550 | motion-rotation-revolution | ఏటా మిగిలే ¼ రోజు నాలుగేళ్లకు ఒక రోజు అవుతుంది. అందుకే నాలుగేళ్లకు ఒకసారి Leap y… | — | N105 |  |
| F551 | motion-sidereal-solar-day | దూర నక్షత్రాలతో పోల్చి భూమి ఒకసారి తిరగడానికి సుమారు 23 గంటల 56 నిమిషాలు పడుతుంద… | SP-038, P004-F041 | N106 |  |
| F552 | motion-sidereal-solar-day | సూర్యుడు మళ్లీ ఆకాశంలో అదే అత్యంత ఎత్తైన స్థానానికి రావడానికి సగటున 24 గంటలు పడు… | SP-038 | N106 |  |
| F553 | motion-sidereal-solar-day | Solar day, Sidereal day కంటే సుమారు 4 నిమిషాలు ఎక్కువ. కారణం: ఒక రోజులో భూమి తన … | — | N106 |  |
| F554 | motion-sidereal-solar-day | ఒక సంవత్సరంలో సుమారు 366¼ Sidereal days, సుమారు 365¼ Solar days ఉంటాయి. | — | N106 |  |
| F555 | motion-retrograde-rotation | Venus (శుక్రుడు), Uranus (యురేనస్) సాధారణ దిశకు వ్యతిరేకంగా, Clockwise గా (తూర్ప… | SP-040, P007-F020 | N107 |  |
| F556 | motion-retrograde-rotation | మిగతా ఆరు గ్రహాలు, భూమితో సహా, పశ్చిమం నుంచి తూర్పుకు (Anticlockwise) తిరుగుతాయి… | SP-040 | — |  |
| F557 | motion-retrograde-rotation | Venus (శుక్రుడు) మీద సూర్యుడు పశ్చిమాన ఉదయించి తూర్పున అస్తమిస్తాడు. | — | N074 |  |
| F558 | motion-retrograde-rotation | గ్రహాల పట్టికల్లో Rotation period ముందు ఉండే మైనస్ గుర్తు, ఆ గ్రహం Retrograde (వ… | — | N107 |  |
| F559 | motion-retrograde-rotation | Uranus (యురేనస్) Axis వంపు సుమారు 98°. అది పక్కకు పడుకుని తిరిగే గ్రహం. | SP-028, P008-F018 | N107 |  |
| F560 | motion-retrograde-rotation | Venus (శుక్రుడు) Axis వంపు సుమారు 177°; అది దాదాపు తలకిందులుగా తిరుగుతుంది. | P008-F028 | N107 |  |
| F561 | motion-same-direction | సౌర కుటుంబం మీద ఉత్తరం వైపు నుంచి చూస్తే, ఎనిమిది గ్రహాలూ సూర్యుడి చుట్టూ ఒకే ది… | — | N108 |  |
| F562 | motion-same-direction | భూమి Orbit ఉండే తలాన్ని Ecliptic plane (క్రాంతి తలం) అంటారు. మిగతా గ్రహాల Orbita… | — | N108 |  |
| F563 | motion-same-direction | సౌర కుటుంబం Solar Nebula (సౌర నీహారిక) అనే తిరిగే వాయువు–ధూళి మేఘం నుంచి పుట్టిం… | — | N108 |  |
| F564 | motion-same-direction | Venus (శుక్రుడు), Uranus (యురేనస్) Rotation వ్యతిరేక దిశలో ఉంటుంది. వాటి Revolut… | — | N108 |  |
| F565 | motion-mercury-venus-day | Venus (శుక్రుడు) మీద ఒక Rotation (సుమారు 243 రోజులు), దాని సంవత్సరం (సుమారు 225 … | P004-F040, P004-F048 | N074 |  |
| F566 | motion-mercury-venus-day | Venus (శుక్రుడు) మీద సూర్యోదయం నుంచి సూర్యోదయానికి (Solar day) సుమారు 117 భూ రోజ… | — | N074 |  |
| F567 | motion-mercury-venus-day | Mercury (బుధుడు) Rotation సుమారు 58.6 భూ రోజులు (కొన్ని పుస్తకాల్లో 59), సంవత్సర… | P004-F039 | N071 |  |
| F568 | motion-mercury-venus-day | Mercury (బుధుడు) రెండు సంవత్సరాల్లో మూడుసార్లు తన చుట్టూ తిరుగుతుంది. అందుకే దాన… | — | N071 |  |
| F569 | motion-kepler-laws | Ellipse ఎంత సాగి ఉందో చెప్పే సంఖ్య Eccentricity (ఉత్కేంద్రత). వృత్తానికి 0. భూమి… | P007-F018 (Mercury) | — |  |
| F570 | motion-kepler-laws | గ్రహాల్లో అత్యధిక Eccentricity Mercury (బుధుడు): సుమారు 0.206. అత్యల్పం Venus (శ… | P007-F018 | — |  |
| F571 | motion-kepler-laws | Kepler గ్రహ చలన నియమాలు మూడు. Tycho Brahe రాసిపెట్టిన కచ్చితమైన పరిశీలనల నుంచి K… | — | N142 |  |
| F572 | motion-kepler-laws | Kepler మొదటి, రెండో నియమాలను 1609 లో Astronomia Nova లో ప్రచురించాడు. | — | N109 |  |
| F573 | motion-kepler-laws | Kepler మూడో నియమాన్ని 1619 లో Harmonices Mundi లో ప్రచురించాడు. | — | N109 |  |
| F574 | motion-kepler-laws | Kepler మొదటి నియమం (Law of ellipses / Law of orbits): గ్రహాల Orbits Ellipses (దీ… | P012-F017 | N109 |  |
| F575 | motion-kepler-laws | Kepler రెండో నియమం (Law of equal areas / Law of areas): సూర్యుణ్ణి, గ్రహాన్ని కల… | SP-041 | N109 |  |
| F576 | motion-kepler-laws | Kepler మూడో నియమం (Law of periods / Law of harmonies): గ్రహం Orbital period వర్గ… | SP-042 | N109 |  |
| F577 | motion-kepler-laws | Ptolemy Geocentric model (భూకేంద్రక) ఇచ్చాడు. Copernicus 1543 లో Heliocentric mo… | P012-F014, P012-F016, SP-081 | — |  |
| F578 | motion-kepler-laws | Galileo 1610 లో టెలిస్కోప్ తో Jupiter నాలుగు చంద్రులను కనుగొన్నాడు. | P012-F018 | — |  |
| F579 | motion-kepler-laws | Newton 1687 లో Principia లో Gravity నియమం ఇచ్చి, Kepler నియమాలకు కారణం చూపించాడు… | P012-F019 | — |  |
| F580 | motion-why-orbit | సూర్యుడి Gravity గ్రహాన్ని లోపలికి లాగడం, గ్రహం ముందుకు కదులుతూ ఉండటం — ఈ రెండూ … | — | N110 |  |
| F581 | motion-why-orbit | వలయంలో తిరిగే వస్తువును మధ్య వైపు లాగే బలం Centripetal force (అభికేంద్ర బలం). గ్… | — | N110 |  |
| F582 | motion-why-orbit | Newton మొదటి చలన నియమాన్నే Law of inertia అంటారు. అంతరిక్షంలో రాపిడి లేనందున గ్ర… | — | N110 |  |
| F583 | motion-why-orbit | భూమి ఉపరితలం నుంచి Escape velocity (పలాయన వేగం) సెకనుకు సుమారు 11.2 km. | — | — | in N110 table (escape velocity 11.2 km/s) |
| F584 | motion-perihelion-aphelion | భూమి ఏటా సుమారు జనవరి 3–4 న Perihelion (రవినీచం) కు వస్తుంది; అప్పుడు సూర్యుడి న… | — | N111 |  |
| F585 | motion-perihelion-aphelion | భూమి ఏటా సుమారు జూలై 4–6 న Aphelion (రవిఉచ్చం) కు వస్తుంది; అప్పుడు దూరం సుమారు … | — | N111 |  |
| F586 | motion-perihelion-aphelion | భూమి జనవరిలో (Perihelion) అత్యంత వేగంగా, సెకనుకు సుమారు 30.3 km తో కదులుతుంది. జ… | — | N111 |  |
| F587 | motion-perihelion-aphelion | భూమిపై ఋతువులకు ప్రధాన కారణం భూమి Axis వంపు (సుమారు 23.5°); సూర్యుడి నుంచి దూరం … | SP-053 | — |  |
| F588 | motion-perihelion-aphelion | చంద్రుడు లేదా ఉపగ్రహం Orbit లో భూమికి అత్యంత దగ్గరి బిందువు Perigee (భూనీచం); అత… | P022-F012, F013 | — |  |
| F589 | seasons-tilt | భూమి Rotation (భ్రమణం) పడమర నుంచి తూర్పుకు జరుగుతుంది; ఒక చుట్టుకు సుమారు 24 గంట… | P004-F011 | — |  |
| F590 | seasons-tilt | భూమి Revolution (పరిభ్రమణం)కు సుమారు 365¼ రోజులు పడుతుంది. Orbit లో భూమి సగటు వే… | — | — | duplicate of a fact tested elsewhere (365¼ days: N105) |
| F591 | seasons-tilt | భూమి Axis, Orbital planeకు లంబంగా ఉన్న రేఖ (Normal) నుంచి సుమారు 23.44° వంగి ఉంద… | SP-054, P008-F025 | N161 |  |
| F592 | seasons-tilt | భూమి Axis, Orbital planeతో సుమారు 66.56° కోణం చేస్తుంది (90° − 23.44° = 66.56°). | SP-054 (distractor 66.56°) | N161 |  |
| F593 | seasons-tilt | Orbital plane నే Plane of the Ecliptic అని కూడా అంటారు. | — | N161 | definition (plane of the ecliptic); low value |
| F594 | seasons-cause | భూమి Axial tilt, భూమి Revolution కలిసి ఋతువులకు (Seasons) ప్రధాన కారణం. | SP-049 | — |  |
| F595 | seasons-cause | భూమి సూర్యుడి చుట్టూ తిరిగేటప్పుడు దాని Axis ఎప్పుడూ ఒకే దిశ (ఈ రోజు Polaris వైప… | — | N112 |  |
| F596 | seasons-cause | ఉత్తర అర్ధగోళం (Northern Hemisphere), దక్షిణ అర్ధగోళం (Southern Hemisphere)లో ఋత… | — | N112 |  |
| F597 | seasons-cause | IMD ప్రకారం భారతదేశంలో నాలుగు ఋతువులు: శీతాకాలం, వేసవి (Pre-monsoon), నైరుతి Mon… | — | N112 |  |
| F598 | seasons-dates | Equator నుంచి ఉత్తరానికి లేదా దక్షిణానికి ఉన్న దూరాన్ని డిగ్రీలలో చెప్పే కొలత La… | — | — | definition (latitude); used in N116 |
| F599 | seasons-dates | Summer Solstice (జూన్ 21) రోజు సూర్యుడు Tropic of Cancer (కర్కట రేఖ, 23.44°N) మీ… | SP-050 | N113 |  |
| F600 | seasons-dates | Winter Solstice (డిసెంబర్ 22) రోజు సూర్యుడు Tropic of Capricorn (మకర రేఖ, 23.44°… | — | N114 |  |
| F601 | seasons-dates | Vernal Equinox (మార్చి 21), Autumnal Equinox (సెప్టెంబర్ 23) రోజుల్లో సూర్యుడు E… | SP-051 | — |  |
| F602 | seasons-dates | Arctic Circle 66.56°N (66½°N) వద్ద, Antarctic Circle 66.56°S వద్ద ఉన్నాయి. | — | — | in N113 table (Arctic, Antarctic circles) |
| F603 | seasons-dates | రెండు Tropics మధ్య భాగం Torrid Zone (ఉష్ణ మండలం). Andhra Pradesh ఈ Zone లో ఉంది. | — | N113 |  |
| F604 | seasons-dates | December solstice తరువాత ఆరు నెలలు ఉత్తరాయణం; June solstice తరువాత ఆరు నెలలు దక్… | — | N114 |  |
| F605 | seasons-dates | Tropic of Cancer భారతదేశంలో 8 రాష్ట్రాల గుండా వెళ్తుంది: Gujarat, Rajasthan, Mad… | — | N113 |  |
| F606 | seasons-equinox-day | Equinox రోజు భూమి మీద చాలా చోట్ల పగలు 12 గంటల కంటే కొన్ని నిమిషాలు ఎక్కువ ఉంటుంద… | — | N115 |  |
| F607 | seasons-equinox-day | Atmosphereలో వెలుగు వంగడం (Refraction), సూర్యబింబం పై అంచు ఆధారంగా సూర్యోదయం–సూర… | — | N115 |  |
| F608 | seasons-equinox-day | పగలు, రాత్రి నిజంగా సమానంగా ఉండే రోజును Equilux అంటారు; ఉత్తర అర్ధగోళంలో ఇది మార… | — | N115 |  |
| F609 | seasons-vijayawada | విజయవాడ Latitude సుమారు 16.5°N; ఇది Equator, Tropic of Cancer మధ్య ఉంది. | — | N116 |  |
| F610 | seasons-vijayawada | రెండు Tropics మధ్య ఉన్న ప్రదేశాల్లో మధ్యాహ్న సూర్యుడు ఏడాదికి రెండుసార్లు తల మీద… | SP-052 | N116 |  |
| F611 | seasons-vijayawada | విజయవాడలో సూర్యుడు సుమారు మే 6–7, ఆగస్టు 7 (±1 రోజు) తేదీల్లో మధ్యాహ్నం తల మీద ఉ… | SP-052 (twice a year only) | N116 |  |
| F612 | seasons-vijayawada | Tropic of Cancerకు ఉత్తరాన ఉన్న ప్రదేశాల్లో (ఉదా. Delhi) సూర్యుడు ఎప్పుడూ తల మీద… | — | N116 |  |
| F613 | seasons-ap-heat | AP లో ఏప్రిల్–మే నెలలు అత్యంత వేడిగా ఉంటాయి; జూన్‌లో నైరుతి రుతుపవనాల (Southwest… | — | N117 |  |
| F614 | seasons-ap-heat | ఋతువును బట్టి దిశ మార్చుకునే గాలులను Monsoon (రుతుపవనాలు) అంటారు. Southwest Mons… | — | N117 |  |
| F615 | seasons-ap-heat | రోహిణి కార్తె సుమారు మే 25 నుంచి జూన్ 8 వరకు ఉండే, ఏడాదిలో అత్యంత వేడి కాలంగా పే… | — | N117 |  |
| F616 | seasons-ap-heat | ఒక ప్రదేశంలో వేడి సూర్యకిరణాల కోణం, పగటి పొడవుతో పాటు మేఘాలు, వర్షం, నేలలో తేమ, … | — | N117 |  |
| F617 | seasons-distance | భూమి సూర్యుడికి అత్యంత దగ్గరగా ఉండే Perihelion ఏటా సుమారు జనవరి 3న వస్తుంది (దూర… | SP-053 | — |  |
| F618 | seasons-distance | భూమి సూర్యుడికి అత్యంత దూరంగా ఉండే Aphelion ఏటా సుమారు జూలై 4–6న వస్తుంది (దూరం … | — | N111 |  |
| F619 | seasons-distance | భూమి Orbit లో Perihelion దగ్గర అత్యంత వేగంగా, Aphelion దగ్గర అత్యంత నెమ్మదిగా కద… | — | N111 |  |
| F620 | moon-size | భూమికి ఉన్న ఏకైక Natural satellite (సహజ ఉపగ్రహం) చంద్రుడు (Moon). | P022-F001 | — |  |
| F621 | moon-size | భూమి–చంద్రుడి సగటు దూరం సుమారు 3,84,400 km. | P022-F010 | — |  |
| F622 | moon-size | చంద్రుడు భూమికి అత్యంత దగ్గరగా ఉండే స్థానం Perigee; అత్యంత దూరంగా ఉండే స్థానం Ap… | P022-F012, F013 | — |  |
| F623 | moon-size | చంద్రుడి Diameter సుమారు 3,475 km; ఇది భూమి Diameter లో సుమారు 27%. | P022-F006 | N118 |  |
| F624 | moon-size | చంద్రుడి Mass భూమి Mass లో సుమారు 1/81 వంతు. | P022-F007 | N118 |  |
| F625 | moon-size | చంద్రుడి Density సుమారు 3.34 g/cm³; భూమి Density సుమారు 5.51 g/cm³. చంద్రుడి ఇను… | — | N118 |  |
| F626 | moon-size | చంద్రుడి వయస్సు సుమారు 450 కోట్ల సంవత్సరాలు (4.5 billion years). | P022-F005 | — |  |
| F627 | moon-gravity | చంద్రుడి ఉపరితల Gravity భూమి Gravity లో సుమారు 1/6 (సుమారు 1.62 m/s²; భూమి మీద స… | P022-F008 | N119 |  |
| F628 | moon-gravity | చంద్రుడి Escape velocity సుమారు 2.38 km/s; భూమిది సుమారు 11.2 km/s. | — | N119 |  |
| F629 | moon-gravity | Gravity బలహీనం కాబట్టి చంద్రుడి మీద చెప్పుకోదగ్గ Atmosphere లేదు; అందుకే అక్కడ శ… | — | N119 |  |
| F630 | moon-origin | చంద్రుడి పుట్టుకకు ఈ రోజు ప్రధాన వివరణ Giant-impact hypothesis (మహా ఢీకొట్టుడు స… | P022-F002 | — |  |
| F631 | moon-origin | Giant-impact సుమారు 450 కోట్ల సంవత్సరాల క్రితం, భూమి పుట్టిన కొద్ది కాలానికే జరి… | P022-F002 | — |  |
| F632 | moon-origin | Giant-impact లో భూమిని ఢీకొట్టిన Mars పరిమాణపు వస్తువు పేరు Theia; ఈ పేరు 2000 ల… | P022-F003 | N120 |  |
| F633 | moon-origin | Giant-impact సిద్ధాంతాన్ని 1975 లో William Hartmann, Donald Davis ప్రతిపాదించారు… | — | N120 |  |
| F634 | moon-origin | Fission (విడిపోవడం) సిద్ధాంతాన్ని George Darwin 19వ శతాబ్దం చివర్లో ప్రతిపాదించా… | P022-F004 | N120 |  |
| F635 | moon-origin | Capture (పట్టుకోవడం) సిద్ధాంతాన్ని 1909 లో T.J.J. See ప్రచారం చేశాడని పుస్తకాలు … | — | N120 |  |
| F636 | moon-phases | చంద్రుడికి సొంత వెలుగు లేదు; Sunlight ను Reflect (పరావర్తనం) చేయడం వల్ల వెలుగుతా… | SP-055, P023-F012 | — |  |
| F637 | moon-phases | సూర్యుడి వెలుగు పడిన చంద్రుడి సగంలో, భూమి నుంచి మనకు కనిపించే భాగం మారడం వల్ల చం… | SP-055, P023-F012 | — |  |
| F638 | moon-phases | అమావాస్య (New moon) రోజు సూర్యుడు, చంద్రుడు, భూమి దాదాపు ఒకే వరుసలో ఉంటారు; మధ్య… | P023-F009, F010 | — |  |
| F639 | moon-phases | First quarter, Last quarter లో భూమి నుంచి సూర్యుడు, చంద్రుడి దిశల మధ్య కోణం సుమా… | P023-F011 | — |  |
| F640 | moon-phases | పౌర్ణమి చంద్రుడు సుమారు సూర్యాస్తమయానికి ఉదయించి, సూర్యోదయానికి అస్తమిస్తాడు. | SP-060 | — |  |
| F641 | moon-phases | Perigee దగ్గర వచ్చే పౌర్ణమిని వాడుకలో Supermoon అంటారు; Apogee దగ్గర వచ్చే పౌర్ణ… | P022-F014 | N121 |  |
| F642 | moon-phases | చంద్రకళల చక్రంలో ఎనిమిది దశలు ఉంటాయి. అమావాస్య నుంచి పౌర్ణమికి సుమారు 14.77 రోజు… | SP-056, P023-F013 | N121 |  |
| F643 | moon-phases | చంద్రుడు రోజూ సుమారు 50 నిమిషాలు ఆలస్యంగా ఉదయిస్తాడు. | — | N121 |  |
| F644 | moon-month | తన చుట్టూ తాను తిరగడం Rotation (భ్రమణం); వేరే దాని చుట్టూ తిరగడం Revolution (పరి… | SP-037 | — |  |
| F645 | moon-month | దూర నక్షత్రాలతో పోల్చి చంద్రుడు భూమి చుట్టూ ఒక Revolution పూర్తి చేసే కాలం Sider… | SP-057, P022-F015 | N122 |  |
| F646 | moon-month | ఒక అమావాస్య నుంచి తరువాతి అమావాస్య వరకు ఉండే కాలం Synodic month (చాంద్రమాసం) — స… | SP-057, P022-F016 | N122 |  |
| F647 | moon-month | ఆ మధ్యలో భూమి సూర్యుడి చుట్టూ ముందుకు కదలడం వల్ల Synodic month, Sidereal month క… | — | N122 |  |
| F648 | moon-oneface | చంద్రుడి Rotation కాలం (తన Axis మీద), Revolution కాలం (భూమి చుట్టూ) రెండూ సుమారు… | SP-058, P022-F017 | N123 |  |
| F649 | moon-oneface | భూమి Gravity చంద్రుడి Rotation ను నెమ్మదింపజేసి Revolution కాలానికి సమానం చేసింద… | — | N123 |  |
| F650 | moon-oneface | Libration వల్ల భూమి నుంచి, వేర్వేరు సమయాల్లో కలిపి, చంద్రుడి ఉపరితలంలో సుమారు 59… | P022-F018 | — |  |
| F651 | moon-oneface | చంద్రుడి Far side (అవతలి ముఖం) కు కూడా Sunlight పడుతుంది; అక్కడా పగలు, రాత్రి ఉం… | SP-059 | N123 |  |
| F652 | moon-surface | చంద్రుడి మీద ముదురు మచ్చలు Lava చల్లారి ఏర్పడిన Basalt మైదానాలు; వీటిని Maria (ఏ… | P022-F021 | — |  |
| F653 | moon-surface | చంద్రుడి మీద గుంతలు Craters; అంతరిక్ష రాళ్లు ఢీకొట్టడం వల్ల ఏర్పడతాయి. చంద్రుడి … | — | — | craters / regolith; low exam value |
| F654 | moon-surface | Apollo 11 Lunar module Eagle 20 July 1969 (UTC) న Sea of Tranquility (Mare Tranq… | P022-F019, F020 | N124 |  |
| F655 | moon-surface | చంద్రుడి మీద మొదటి అడుగు Neil Armstrong వేశాడు (21 July 1969, UTC); Buzz Aldrin … | — | N124 |  |
| F656 | moon-surface | Apollo 11 ను 16 July 1969 న Saturn V రాకెట్‌తో ప్రయోగించారు; Command module పేరు… | — | N124 |  |
| F657 | moon-surface | Apollo Missions లో మొత్తం 12 మంది చంద్రుడి మీద నడిచారు; చివరిది Apollo 17 (1972)… | — | N124 |  |
| F658 | moon-surface | చంద్రుడి మీద అత్యంత ఎత్తైన స్థానం సుమారు 10,786 m (Far side, Engel'gardt Crater … | P022-F025 | — |  |
| F659 | moon-chandrayaan | Chandrayaan-1 భారత్ మొదటి చంద్ర Mission; 22 October 2008 న PSLV-C11 తో ప్రయోగించ… | P022-F022 | — |  |
| F660 | moon-chandrayaan | Chandrayaan-1 పై ఉన్న పరికరాలు చంద్రుడిపై Water molecules, Hydroxyl ఆధారాలు చూపా… | — | N125 |  |
| F661 | moon-chandrayaan | Chandrayaan-1 Moon Impact Probe ఢీకొట్టిన స్థానం పేరు Jawahar Sthal (14 November… | — | N125 |  |
| F662 | moon-chandrayaan | Chandrayaan-2 ను 22 July 2019 న ప్రయోగించారు; దాని Vikram lander Soft landing వి… | P022-F023 | — |  |
| F663 | moon-chandrayaan | Chandrayaan-3 ను 14 July 2023 న LVM3-M4 తో ప్రయోగించారు; 23 August 2023 న Soft l… | P022-F024 | — |  |
| F664 | moon-chandrayaan | Chandrayaan-3 లో Vikram lander, Pragyan rover, Propulsion module ఉన్నాయి. | P023-F002 | — |  |
| F665 | moon-chandrayaan | Chandrayaan-3 దిగిన స్థానం పేరు Statio Shiv Shakti (Shiv Shakti Point); ఇది సుమా… | P023-F001, F004 | — |  |
| F666 | moon-chandrayaan | Chandrayaan-3 ChaSTE చంద్రుడి ఉపరితలంపై సుమారు 70°C, కొన్ని సెంటీమీటర్ల లోతులో స… | — | N125 |  |
| F667 | moon-chandrayaan | భారత్ ప్రతి సంవత్సరం 23 August ను National Space Day (జాతీయ అంతరిక్ష దినం) గా జర… | P023-F003 | — |  |
| F668 | moon-chandrayaan | చంద్రుడిపై Soft landing చేసిన నాలుగో దేశం భారత్ (Soviet Union, United States, Ch… | P023-F005 | — |  |
| F669 | moon-chandrayaan | ప్రపంచంలో మొదటి Robotic lunar rover Lunokhod 1 (Soviet Union, 1970); Far side పై… | P023-F006, F007 | — |  |
| F670 | eclipse-what | సూర్యగ్రహణం (Solar eclipse)లో క్రమం సూర్యుడు – చంద్రుడు – భూమి; చంద్రుడు మధ్యలో … | SP-061, P023-F019 | — |  |
| F671 | eclipse-what | చంద్రగ్రహణం (Lunar eclipse)లో క్రమం సూర్యుడు – భూమి – చంద్రుడు; భూమి మధ్యలో ఉంటు… | P023-F018, P024-F006 | — |  |
| F672 | eclipse-what | సూర్యగ్రహణం అమావాస్య (New moon) రోజున, చంద్రగ్రహణం పౌర్ణమి (Full moon) రోజున వస్… | SP-063, P023-F018, F019 | — |  |
| F673 | eclipse-what | గ్రహణాలు నీడ వల్ల వస్తాయని ఆర్యభట (Aryabhata, ఆర్యభటీయం, క్రీ.శ. 499) వివరించాడు… | — | N141 |  |
| F674 | eclipse-not-monthly | చంద్రుడి Orbit, భూమి Orbital plane (Ecliptic, క్రాంతివృత్తం)కు సుమారు 5.1° (కొన్… | SP-062, P024-F001 | — |  |
| F675 | eclipse-not-monthly | చంద్రుడి Orbit, Ecliptic planeను దాటే రెండు బిందువులను Nodes అంటారు: Ascending n… | P024-F002 | N126 |  |
| F676 | eclipse-not-monthly | అమావాస్య లేదా పౌర్ణమి, చంద్రుడు ఒక Node దగ్గర ఉన్నప్పుడు వస్తేనే గ్రహణం వస్తుంది… | SP-062 | N126 |  |
| F677 | eclipse-not-monthly | సూర్యుడు ఏడాదికి రెండుసార్లు, సుమారు ప్రతి 173 రోజులకు, ఒక Node దగ్గరకు వస్తాడు;… | — | N126 |  |
| F678 | eclipse-shadow-parts | నీడలో కాంతి మూలం (సూర్యుడు) పూర్తిగా కప్పబడే చిక్కని భాగాన్ని Umbra అంటారు. | SP-065, P024-F003 | — |  |
| F679 | eclipse-shadow-parts | నీడలో కాంతి మూలం కొంత భాగం మాత్రమే కప్పబడే లేత భాగాన్ని Penumbra అంటారు. | SP-065, P024-F004 | — |  |
| F680 | eclipse-shadow-parts | చంద్రుడి Umbra మొన దాటిన తరువాతి ప్రాంతాన్ని Antumbra అంటారు. ఇక్కడి నుంచి Annul… | P024-F005 | N127 |  |
| F681 | eclipse-shadow-parts | సూర్యుడు చంద్రుడి కన్నా సుమారు 400 రెట్లు పెద్దవాడు, సుమారు 400 రెట్లు దూరంలో ఉన… | — | N127 |  |
| F682 | eclipse-shadow-parts | చంద్రుడు Perigee (దగ్గర) దగ్గర ఉంటే Total solar eclipse, Apogee (దూరం) దగ్గర ఉంట… | SP-064 | N127 |  |
| F683 | eclipse-solar-types | సూర్యగ్రహణాలు నాలుగు రకాలు: Total, Partial, Annular, Hybrid. | — | N128 |  |
| F684 | eclipse-solar-types | చంద్రుడి Umbra భూమి మీద కదులుతూ గీసే సన్నని దారిని Path of totality అంటారు. దీని… | — | N128 |  |
| F685 | eclipse-solar-types | Total solar eclipseలో Totality గరిష్ఠంగా సుమారు 7½ minutes మాత్రమే ఉంటుంది. | P023-F020 | N128 |  |
| F686 | eclipse-solar-types | సూర్యుడి బయటి పొర Corona, Total solar eclipse లోని Totality సమయంలో మాత్రమే కళ్లక… | SP-017 (corona) | — |  |
| F687 | eclipse-solar-types | భారత్‌లో చివరి Total solar eclipse 22 July 2009; తరువాతిది 20 March 2034. తరువాత… | — | N128 |  |
| F688 | eclipse-lunar-types | చంద్రగ్రహణాలు మూడు రకాలు: Penumbral, Partial, Total. | — | N129 |  |
| F689 | eclipse-lunar-types | Total lunar eclipseలో భూమి Atmosphere నీలం వెలుగును చెదరగొట్టి (Scattering), ఎరు… | — | N129 |  |
| F690 | eclipse-lunar-types | చంద్రగ్రహణం భూమిలో రాత్రి ఉన్న సగం మొత్తం నుంచి కనిపిస్తుంది; సూర్యగ్రహణం నీడ దా… | — | N129 |  |
| F691 | eclipse-lunar-types | Total lunar eclipse లో Totality గరిష్ఠంగా సుమారు 1 గంట 45 నిమిషాలు ఉంటుంది. | — | N129 |  |
| F692 | eclipse-safety | సూర్యగ్రహణాన్ని ISO 12312-2 ప్రమాణం ఉన్న Eclipse glasses లేదా Pinhole projector … | SP-066 | N130 |  |
| F693 | eclipse-safety | సూర్యుడిని నేరుగా చూడడం వల్ల Retina దెబ్బతినడాన్ని Solar retinopathy అంటారు. | — | N130 |  |
| F694 | eclipse-safety | చంద్రగ్రహణాన్ని నేరుగా కళ్లతో చూడడం సురక్షితం. | — | N130 |  |
| F695 | eclipse-saros-count | ఒక అమావాస్య నుంచి తరువాతి అమావాస్య వరకు పట్టే సుమారు 29.53 రోజులను Synodic month… | SP-057 | — |  |
| F696 | eclipse-saros-count | Saros చక్రం = 223 Synodic months = సుమారు 18 సంవత్సరాలు 11 రోజులు 8 గంటలు (6,585… | P024-F007 | N131 |  |
| F697 | eclipse-saros-count | 223 Synodic months ≈ 242 Draconic months ≈ 239 Anomalistic months; అందుకే Saros … | P024-M002 (partial) | — |  |
| F698 | eclipse-saros-count | Saros చక్రాన్ని Babylon ఖగోళ శాస్త్రవేత్తలు గుర్తించారు; "Saros" పేరును Edmond H… | — | N131 |  |
| F699 | eclipse-saros-count | Sarosలోని అదనపు 8 గంటల వల్ల తరువాతి సూర్యగ్రహణ దారి సుమారు 120° పడమరకు జరుగుతుంద… | P024-F008 | — |  |
| F700 | eclipse-saros-count | ఒక Calendar yearలో ప్రపంచవ్యాప్తంగా కనీసం 4, గరిష్ఠంగా 7 గ్రహణాలు రావచ్చు. సూర్య… | P024-F009 | N131 |  |
| F701 | eclipse-phases-vs | చంద్రకళలు చంద్రుడి వెలిగిన సగంలో మనకు కనిపించే భాగం మారడం వల్ల వస్తాయి; భూమి నీడ… | SP-055 | — |  |
| F702 | eclipse-phases-vs | అమావాస్య నుంచి పౌర్ణమి వరకు కళలు పెరిగే కాలం Waxing (శుక్ల పక్షం); పౌర్ణమి నుంచి… | SP-056, P023-F013, F014 | — |  |
| F703 | eclipse-phases-vs | Tides (ఆటుపోట్లు) చంద్రుడి, సూర్యుడి Gravity వల్ల వస్తాయి; చంద్రుడు దగ్గరగా ఉండట… | SP-067 | — |  |
| F704 | eclipse-phases-vs | Spring tides అమావాస్య, పౌర్ణమి రోజుల్లో వస్తాయి; Neap tides First quarter, Last … | SP-068, SP-069 | — |  |
| F705 | eclipse-phases-vs | Spring tides రావడానికి గ్రహణం అవసరం లేదు; ప్రతి అమావాస్య, పౌర్ణమికీ వస్తాయి. | SP-072 | — |  |
| F706 | tides-what | సముద్రంలో నీళ్లు రోజూ ఒక క్రమంలో పైకి లేచి, కిందికి దిగడాన్ని Tides (ఆటుపోట్లు) … | SP-067 | — |  |
| F707 | tides-what | నీళ్లు అత్యధిక ఎత్తులో ఉన్న స్థితి High tide (పోటు). అత్యల్ప ఎత్తులో ఉన్న స్థితి… | SP-069 (implicit) | — |  |
| F708 | tides-what | Tides కు ప్రధాన కారణం చంద్రుడి Gravity. సూర్యుడి Gravity కూడా కొంత కారణం. | SP-067 | — |  |
| F709 | tides-moon-vs-sun | Tides కు కారణం Tidal force. అంటే భూమి ఒక వైపుకూ, అవతలి వైపుకూ చంద్రుడు, సూర్యుడి… | SP-067 | N132 |  |
| F710 | tides-moon-vs-sun | సూర్యుడి Mass చంద్రుడి కంటే సుమారు 2.7 కోట్ల రెట్లు ఎక్కువ. కానీ సూర్యుడు చంద్రు… | — | N132 |  |
| F711 | tides-moon-vs-sun | Tidal force దూరం Cube కు విలోమంగా తగ్గుతుంది (Inverse cube law). అందుకే దగ్గరగా … | — | N132 |  |
| F712 | tides-moon-vs-sun | సూర్యుడి Tidal force చంద్రుడి Tidal force లో సుమారు సగం (NOAA). | SP-067 (explanation) | N132 |  |
| F713 | tides-two-a-day | భూమి మీద రెండు Tidal bulges (ఉబ్బులు) ఉంటాయి: ఒకటి చంద్రుడి వైపు, రెండోది దానికి… | — | N133 |  |
| F714 | tides-two-a-day | Lunar day (చాంద్ర దినం) సుమారు 24 గంటల 50 నిమిషాలు. చాలా తీరాల్లో ఈ కాలంలో రెండు… | — | N133 |  |
| F715 | tides-two-a-day | రెండు వరుస High tides మధ్య కాలం సుమారు 12 గంటల 25 నిమిషాలు. పోటు రోజూ సుమారు 50 … | — | N133 |  |
| F716 | tides-two-a-day | చంద్రుడు భూమికి అతి దగ్గరగా ఉండే స్థానం Perigee, అతి దూరంగా ఉండే స్థానం Apogee. … | — | — | perigee tides higher; not tested (low value) |
| F717 | tides-two-a-day | Tides మూడు రకాలు: Semi-diurnal (రోజుకు రెండు), Diurnal (రోజుకు ఒకటి), Mixed (రెం… | — | N133 |  |
| F718 | tides-spring-neap | అమావాస్య (New moon), పౌర్ణమి (Full moon) దగ్గర సూర్యుడు, భూమి, చంద్రుడు ఒకే వరుస… | SP-068 | N134 |  |
| F719 | tides-spring-neap | First quarter (శుక్ల అష్టమి), Third quarter (కృష్ణ అష్టమి) దగ్గర సూర్యుడు, చంద్ర… | SP-069 | N134 |  |
| F720 | tides-spring-neap | Spring tide నెలకు రెండుసార్లు, Neap tide నెలకు రెండుసార్లు వస్తాయి. రెండింటి మధ్… | — | N134 |  |
| F721 | tides-spring-neap | Sidereal month సుమారు 27.3 రోజులు (నక్షత్రాలతో పోల్చి). Synodic month సుమారు 29.… | SP-057 | — |  |
| F722 | tides-spring-neap | చంద్రకళలు ఎనిమిది. Third quarter ను Last quarter అని కూడా అంటారు. | P023-F014 | — |  |
| F723 | tides-range-calc | Tidal range = High tide ఎత్తు − Low tide ఎత్తు. ఉదాహరణ: 2.4 m − 0.7 m = 1.7 m. | SP-070 | N135 |  |
| F724 | tides-range-calc | Tide ఎత్తులను కొలిచే స్థిరమైన సున్నా మట్టాన్ని Chart datum అంటారు. దాని కంటే కిం… | — | N135 |  |
| F725 | tides-local-factors | తీరం ఆకారం, సముద్రం లోతు, అడుగు నేల ఘర్షణ (Friction), వాతావరణం (Weather) వల్ల ఒక… | — | N136 |  |
| F726 | tides-local-factors | భారతదేశంలో అత్యధిక Tidal range Gulf of Khambhat (గుజరాత్) లో ఉంటుంది. భావ్‌నగర్ … | — | N136 |  |
| F727 | tides-local-factors | ప్రపంచంలో అత్యధిక Tidal range Bay of Fundy (Canada) లో ఉంటుంది: సుమారు 16 m. | — | N136 |  |
| F728 | tides-local-factors | భారతదేశంలో Indian Tide Tables ను Survey of India ఏటా ప్రచురిస్తుంది. | — | — | publisher of the Indian Tide Tables not verifiable (lesson names both Survey of India and NHO); removed from N136, not tested |
| F729 | tides-storm-surge | తుఫాను గాలులు, తక్కువ Air pressure వల్ల సముద్ర నీటిమట్టం అసాధారణంగా పెరగడాన్ని S… | SP-071 | N137 |  |
| F730 | tides-storm-surge | Storm surge, మామూలు Tide కలిపి వచ్చే మొత్తం నీటిమట్టాన్ని Storm tide అంటారు. | — | N137 |  |
| F731 | tides-storm-surge | దివిసీమ ఉప్పెన: 1977 నవంబర్ 19, కృష్ణా జిల్లా. సుమారు 10,000 మందికి పైగా మృతి. | — | N137 |  |
| F732 | tides-storm-surge | Tsunami కి కారణం సముద్రం అడుగున భూకంపం. Storm surge కి కారణం తుఫాను. Tides కి కా… | SP-071 | N137 |  |
| F733 | tides-uses | భారతదేశంలో Tidal energy కి ముఖ్యమైన ప్రాంతాలు మూడు: Gulf of Khambhat, Gulf of Ku… | — | N138 |  |
| F734 | tides-uses | భారతదేశంలో అత్యధిక Tidal energy సామర్థ్యం Gulf of Khambhat లో ఉంది (సుమారు 7,000… | — | N138 |  |
| F735 | tides-uses | భారతదేశ మొత్తం Tidal సామర్థ్యం సుమారు 12,455 MW (IIT Madras, 2014 అధ్యయనం; 2019 … | — | N138 |  |
| F736 | tides-uses | 2019 ఆగస్టు లో MNRE Ocean energy (Tidal, Wave, OTEC, Salinity gradient — అన్ని ర… | — | N138 |  |
| F737 | tides-uses | ప్రపంచంలో అతి పెద్ద Tidal power plant Sihwa Lake (South Korea, 254 MW). మొదటి పె… | — | N138 |  |
| F738 | tides-phases-eclipse | చంద్రకళలకు కారణం వెలిగిన చంద్ర భాగంలో మనకు కనిపించే భాగం మారడం; గ్రహణానికి కారణం… | SP-072 | — |  |
| F739 | history-geocentric | Geocentric model (భూకేంద్ర నమూనా) ప్రకారం భూమి కదలకుండా కేంద్రంలో ఉంటుంది. సూర్య… | P012-F014 | — |  |
| F740 | history-geocentric | Aristotle (క్రీ.పూ. 4వ శతాబ్దం) చంద్ర గ్రహణంలో కనిపించే వంపు నీడను ఆధారంగా చూపి … | P012-F012 | — |  |
| F741 | history-geocentric | భూమి చుట్టుకొలతను మొదట కొలిచింది Eratosthenes (సుమారు క్రీ.పూ. 240, Alexandria).… | P002-F003 | N002 |  |
| F742 | history-geocentric | గ్రహం నక్షత్రాల మధ్య కొన్ని రోజులు వెనక్కి వెళ్తున్నట్టు కనిపించడాన్ని Retrograd… | — | N139 |  |
| F743 | history-geocentric | Ptolemy సుమారు క్రీ.శ. 150 లో Almagest గ్రంథంలో Geocentric model ను పూర్తి లెక్క… | P012-F014 | N139 |  |
| F744 | history-geocentric | Ptolemy Model లో ప్రతి గ్రహం Epicycle అనే చిన్న వృత్తంలో తిరుగుతుంది. ఆ వృత్తం క… | — | N139 |  |
| F745 | history-geocentric | భూమి సూర్యుడి చుట్టూ తిరుగుతుందని మొదట చెప్పినట్టు మనకు తెలిసిన వ్యక్తి Aristarc… | P012-F013 | N147 |  |
| F746 | history-indian | భూమి తన Axis మీద తాను తిరగడం Rotation. దీనికి సుమారు 24 గంటలు పడుతుంది. దీని వల్… | P004-F011 | — |  |
| F747 | history-indian | భూమి సూర్యుడి చుట్టూ తిరగడం Revolution. దీనికి సుమారు 365¼ రోజులు (ఒక సంవత్సరం) … | P004-F012 | — |  |
| F748 | history-indian | Aryabhata సుమారు క్రీ.శ. 499 లో Kusumapura (Pataliputra) లో Aryabhatiya గ్రంథం ర… | P012-F015 | N140 |  |
| F749 | history-indian | నక్షత్రాలు రోజూ పడమరకు జరుగుతున్నట్టు కనిపించడానికి భూమి Rotation కారణమని Aryabh… | P012-F015 | N141 |  |
| F750 | history-indian | గ్రహణాలు భూమి, చంద్రుడి నీడల వల్ల వస్తాయని, చంద్రుడు సూర్యుడి వెలుగుతో మెరుస్తాడ… | — | N141 |  |
| F751 | history-indian | భారతదేశ మొదటి ఉపగ్రహం Aryabhata ను ISRO తయారుచేసింది. 1975 ఏప్రిల్ 19 న సోవియట్ … | — | N141 |  |
| F752 | history-indian | Varahamihira Pancha Siddhantika లో ఐదు ఖగోళ సిద్ధాంతాలను వివరించాడు. ఆయన మరో గ్ర… | — | N140 |  |
| F753 | history-indian | సంప్రదాయం ప్రకారం Varahamihira విక్రమాదిత్యుడి ఆస్థానంలోని నవరత్నాల్లో ఒకడు. | — | — | in N141 table (Varahamihira, nine gems) |
| F754 | history-indian | Brahmagupta క్రీ.శ. 628 లో Brahmasphuta Siddhanta గ్రంథం రాశాడు. సున్నాను ఒక సంఖ… | — | N140 |  |
| F755 | history-indian | Bhaskara II (భాస్కరాచార్యుడు) గ్రంథం Siddhanta Shiromani. దాని నాలుగు భాగాలు Lil… | — | N140 |  |
| F756 | history-indian | Bhaskara I (సుమారు 600 – 680) Aryabhatiya కు వ్యాఖ్యానం రాశాడు; ఆయన గ్రంథం Mahab… | — | — | in N140 table (Bhaskara I) |
| F757 | history-indian | మన పాత Astronomers Ujjain గుండా పోయే రేఖను ప్రధాన రేఖ (Prime meridian) గా తీసుకు… | — | N141 |  |
| F758 | history-heliocentric | Heliocentric model (సూర్యకేంద్ర నమూనా) ప్రకారం సూర్యుడు మధ్యలో ఉంటాడు. భూమితో సహ… | P012-F016, SP-081 | — |  |
| F759 | history-heliocentric | Copernicus (1473 – 1543, పోలాండ్) 1543 లో De revolutionibus orbium coelestium గ్… | P012-F016 | — |  |
| F760 | history-heliocentric | Copernicus Model లో గ్రహాల Orbits వృత్తాలు. Orbits Ellipse అని తరువాత Kepler చూప… | — | N142 |  |
| F761 | history-heliocentric | Tycho Brahe (1546 – 1601, డెన్మార్క్) Telescope లేకుండా, Ven దీవిలోని Uraniborg … | — | N142 |  |
| F762 | history-heliocentric | Tycho Brahe 1572 లో ఒక Supernova (Tycho's Star) ను, 1577 లో ఒక Comet ను గమనించాడ… | — | N142 |  |
| F763 | history-heliocentric | Tycho Brahe నమోదు చేసిన Mars పరిశీలనలతోనే Kepler (1571 – 1630, జర్మనీ) గ్రహ చలన … | SP-081 (order) | N142 |  |
| F764 | history-galileo | Telescope ను కనిపెట్టినవాడిగా పరీక్షల్లో ఆశించే పేరు Hans Lippershey (1608, Neth… | — | N143 |  |
| F765 | history-galileo | Galileo 1609 లో తన Telescope తయారుచేసుకుని ఆకాశాన్ని గమనించడం మొదలుపెట్టాడు. చంద… | — | N143 |  |
| F766 | history-galileo | Galileo 1610 జనవరిలో Jupiter నాలుగు పెద్ద చంద్రులు Io, Europa, Ganymede, Callist… | P012-F018, P008-F012 | N143 |  |
| F767 | history-galileo | Galileo 1610 చివర్లో Venus (శుక్రుడు) దశలను గమనించాడు. అవి Venus సూర్యుడి చుట్టూ… | — | N143 |  |
| F768 | history-galileo | Galileo ను 1633 లో Church విచారించి, జీవితాంతం House arrest లో ఉంచింది. ఆయన 1642… | — | N143 |  |
| F769 | history-galileo | Stellar parallax ను మొదట కొలిచింది Friedrich Bessel (1838). Aberration of starli… | — | N018 |  |
| F770 | history-kepler-newton | Kepler మొదటి నియమం: గ్రహం Orbit ఒక Ellipse; సూర్యుడు ఒక Focus దగ్గర ఉంటాడు. | P012-F017 | — |  |
| F771 | history-kepler-newton | Kepler గ్రహ చలన మొదటి రెండు నియమాలను 1609 లో (Astronomia Nova), మూడో నియమాన్ని 1… | — | — | duplicate of a fact tested elsewhere (Kepler 1609 / 1619: N109) |
| F772 | history-kepler-newton | Newton 1687 లో Principia గ్రంథంలో మూడు చలన నియమాలను, Law of universal gravitatio… | P012-F019 | N144 |  |
| F773 | history-kepler-newton | Gravity బలం దూరం వర్గానికి విలోమంగా తగ్గుతుంది (Inverse-square law): F = G m₁m₂ … | — | N144 |  |
| F774 | history-kepler-newton | Gravitational constant (G) ను మొదట కొలిచింది Henry Cavendish (1798). | — | N144 |  |
| F775 | history-kepler-newton | గ్రహాలు సూర్యుడి చుట్టూ తిరగడానికి కారణం సూర్యుడి Gravity అని Newton వివరించాడు. | P012-F019 | — |  |
| F776 | history-planet-names | Earth ఒక్కటే ఇంగ్లీష్ పేరు గ్రీకు లేదా రోమన్ పురాణాల నుంచి రాని గ్రహం. ఆ పేరుకు … | P007-F024 | N145 |  |
| F777 | history-planet-names | కంటికి కనిపించే ఐదు గ్రహాలకు దేవుళ్ల పేర్లు Babylonians, గ్రీకులు ముందే పెట్టారు… | P012-F004–F010 | — |  |
| F778 | history-planet-names | Uranus (యురేనస్) పేరు గ్రీకు ఆకాశ దేవుడిది. మిగతా ఆరు గ్రహాల (Mercury, Venus, Ma… | P012-F009 | — |  |
| F779 | history-planet-names | గ్రీకు పేర్లు: Mercury = Hermes, Venus = Aphrodite, Mars = Ares, Jupiter = Zeus,… | P012-M002, M003 (partial) | N145 |  |
| F780 | history-planet-names | Uranus కు Herschel పెట్టిన పేరు Georgium Sidus. Uranus అనే పేరును Johann Bode సూ… | — | N145 |  |
| F781 | history-planet-names | Neptune స్థానాన్ని Le Verrier (ఫ్రాన్స్), John Couch Adams (ఇంగ్లండ్) లెక్కలతో చ… | — | N087, N160 |  |
| F782 | history-planet-names | Pluto ను 1930 లో Clyde Tombaugh (Lowell Observatory, అమెరికా) కనుగొన్నాడు. ఆ పేర… | P009-F001, P012-F011 | — |  |
| F783 | history-planet-names | తెలుగు గ్రహ పేర్లు నవగ్రహాల సంప్రదాయం నుంచి వచ్చాయి. వారాల పేర్లు (మంగళవారం, బుధ… | — | — | Telugu weekday names; background only |
| F784 | history-astronomy-terms | నక్షత్రాలు, గ్రహాలు, Galaxies ను పరిశీలనలతో అధ్యయనం చేసే శాస్త్రాన్ని Astronomy … | P012-F001 | — |  |
| F785 | history-astronomy-terms | Universe పుట్టుక, నిర్మాణం గురించి చదివే శాస్త్రం Cosmology. నక్షత్రాలను Physics… | EXT-0174 | N146 |  |
| F786 | history-astronomy-terms | భూమి మీది ప్రదేశాలు, వాటి మధ్య సంబంధాలను అధ్యయనం చేసే శాస్త్రాన్ని Geography (భూ… | P002-F002 | — |  |
| F787 | history-astronomy-terms | పగలు, రాత్రి భూమి Rotation వల్ల వస్తాయి. ఋతువులు భూమి Axis సుమారు 23.5° వాలి ఉండ… | SP-049 | — |  |
| F788 | history-astronomy-terms | అంతరిక్ష యాత్రికుడిని అమెరికాలో Astronaut, రష్యాలో Cosmonaut, చైనాలో Taikonaut, … | P012-F003 | N146 |  |
| F789 | history-astronomy-terms | అంతరిక్షంలోకి వెళ్లిన మొదటి మనిషి Yuri Gagarin (1961 ఏప్రిల్ 12, Vostok 1). మొదట… | — | N146 |  |
| F790 | history-who-first | Uranus ను 1781 లో William Herschel Telescope తో కనుగొన్నాడు. Neptune ను 1846 లో … | P008-F017, P008-F021 | N147 |  |
| F791 | history-who-first | Copernicus ను Father of modern astronomy అని, Galileo ను Father of observational… | — | N147 |  |
| F792 | missions-types | గ్రహం, సూర్యుడు లేదా ఒక బిందువు చుట్టూ Orbit లో తిరుగుతూ పరిశీలించే Spacecraft న… | P008-F008 | N148 |  |
| F793 | missions-types | గ్రహం లేదా చంద్రుడి నేల మీద దిగి, దిగిన చోటనే పరిశోధించే Spacecraft ను Lander అం… | — | N148 |  |
| F794 | missions-types | నేల మీద దిగి, కదులుతూ పరిశోధించే వాహనాన్ని Rover అంటారు. | P008-F009 | N148 |  |
| F795 | missions-types | భారతదేశపు మొదటి Impactor Chandrayaan-1 లోని Moon Impact Probe; ఇది 2008 నవంబర్ 1… | — | N125, N148 |  |
| F796 | missions-satellite-payload | Satellite మోసుకెళ్లే Camera లేదా పరిశోధన పరికరాన్ని Payload అంటారు. | P003-F012 (satellite) | N149 |  |
| F797 | missions-satellite-payload | PSLV నాలుగో Stage (PS4) ను Experiment platform గా మార్చిన దాన్ని POEM (PSLV Orbi… | — | N149 |  |
| F798 | missions-satellite-payload | మొదటి POEM (POEM-1) 2022 జూన్ 30 న PSLV-C53 తో వెళ్లింది. | — | N149 |  |
| F799 | missions-satellite-payload | PSLV-C58 (2024 జనవరి 1) ప్రధాన Satellite XPoSat (X-ray Polarimeter Satellite). | — | N149 |  |
| F800 | missions-satellite-payload | WESAT (Women Engineered Satellite) ను LBS Institute of Technology for Women (కేర… | G1 | — |  |
| F801 | missions-satellite-payload | WESAT 2024 జనవరి 1 న PSLV-C58 మిషన్ లో POEM-3 మీద వెళ్లి, Solar irradiance ను, U… | G1 | N149 |  |
| F802 | missions-l1 | భూమి-సూర్యుడి వ్యవస్థలో ఐదు Lagrange points ఉన్నాయి: L1, L2, L3, L4, L5. వీటిని … | — | N150 |  |
| F803 | missions-l1 | L1 బిందువు భూమి నుంచి సూర్యుడి వైపు సుమారు 15 లక్షల km (1.5 million km) దూరంలో ఉ… | P007-F012 | N150 |  |
| F804 | missions-l1 | L1 దగ్గర ఉన్న Spacecraft కు సూర్యుడు ఎప్పుడూ కనిపిస్తాడు; గ్రహణాలు అడ్డు రావు. | — | N150 |  |
| F805 | missions-l1 | James Webb Space Telescope Sun-Earth L2 దగ్గర ఉంది. | — | N150 |  |
| F806 | missions-l1 | L4, L5 స్థిరమైన Lagrange points; అక్కడ చేరిన సహజ చిన్న వస్తువులను Trojans అంటారు… | — | N150 |  |
| F807 | missions-aditya | Aditya-L1 భారతదేశపు మొదటి Space-based solar observatory. | P007-F010 | N151 |  |
| F808 | missions-aditya | Aditya-L1 ను ISRO 2023 సెప్టెంబర్ 2 న శ్రీహరికోట నుంచి PSLV-C57 తో ప్రయోగించింది… | SP-089 | N151 |  |
| F809 | missions-aditya | Aditya-L1 2024 జనవరి 6 న Sun-Earth L1 చుట్టూ Halo orbit లోకి చేరింది. | SP-089, P007-F011 | — |  |
| F810 | missions-aditya | Aditya-L1 లో ఏడు Payloads ఉన్నాయి: నాలుగు Remote sensing (VELC, SUIT, SoLEXS, HE… | — | N151 |  |
| F811 | missions-aditya | Aditya-L1 లోని అతి పెద్ద Payload VELC (Visible Emission Line Coronagraph). | — | N151 |  |
| F812 | missions-sun-international | Parker Solar Probe NASA యాత్ర; 2018 ఆగస్టు 12 న ప్రయోగించారు. దీనికి Solar wind … | P007-F013 | N152 |  |
| F813 | missions-sun-international | Parker Solar Probe 2021 ఏప్రిల్ 28 న మొదటిసారి సూర్యుడి Corona లోకి ప్రవేశించింద… | — | N152 |  |
| F814 | missions-sun-international | Parker Solar Probe 2024 డిసెంబర్ 24 న సూర్యుడి ఉపరితలం నుంచి సుమారు 61 లక్షల km … | — | — | in N152 explanation and table (Parker 24 Dec 2024) |
| F815 | missions-sun-international | SOHO ESA, NASA కలిసి చేసిన యాత్ర; 1995 నుంచి L1 దగ్గర సూర్యుడిని పరిశీలిస్తోంది. | — | N152 |  |
| F816 | missions-sun-international | Solar Orbiter ESA-NASA యాత్ర; 2025 లో సూర్యుడి ధ్రువాల చిత్రాలను మొదటిసారి తీసిం… | — | N152 |  |
| F817 | missions-sun-international | Proba-3 European Space Agency (ESA) యాత్ర; ISRO దీన్ని 2024 డిసెంబర్ 5 న PSLV-C5… | SP-090 | N152 |  |
| F818 | missions-sun-international | Proba-3 లో రెండు Spacecraft లు సుమారు 150 మీటర్ల దూరంలో Formation flying చేస్తూ … | SP-090, P007-F014 | — |  |
| F819 | missions-mars | Mangalyaan (Mars Orbiter Mission) ను ISRO 2013 నవంబర్ 5 న PSLV-C25 తో ప్రయోగించి… | P008-F008 | N153 |  |
| F820 | missions-mars | Mangalyaan 2014 సెప్టెంబర్ 24 న Mars Orbit లోకి చేరింది. | — | N153 |  |
| F821 | missions-mars | Mars Orbit చేరిన మొదటి ఆసియా దేశం భారత్; మొదటి ప్రయత్నంలోనే చేరిన మొదటి దేశం కూడ… | — | N153 |  |
| F822 | missions-mars | Mars కు రెండు చంద్రులు ఉన్నాయి: Phobos, Deimos. | P008-F004 | — |  |
| F823 | missions-mars | Perseverance NASA Rover; 2021 ఫిబ్రవరి 18 న Mars మీద Jezero Crater లో దిగింది. | P008-F009 | N153 |  |
| F824 | missions-mars | Ingenuity వేరే గ్రహం మీద Powered, controlled flight చేసిన మొదటి విమానం; 72 సార్ల… | — | N153 |  |
| F825 | missions-dart | DART (Double Asteroid Redirection Test) NASA చేసిన మొదటి Planetary defence పరీక్… | P009-F007 | — |  |
| F826 | missions-dart | DART 2022 సెప్టెంబర్ 26 న (UTC) Didymos చుట్టూ తిరిగే Dimorphos అనే చిన్న Astero… | SP-091, P009-F006 | N154 |  |
| F827 | missions-dart | DART ఢీకొట్టిన తరువాత Dimorphos Orbit కాలం 32 నిమిషాలు తగ్గింది (11 గం 55 ని నుం… | — | N154 |  |
| F828 | missions-dart | వేగంగా ఢీకొట్టి Asteroid దారి మార్చే పద్ధతిని Kinetic impactor అంటారు. | P009-F007 | N154 |  |
| F829 | missions-dart | DART ఫలితాన్ని దగ్గరగా పరిశీలించడానికి ESA పంపిన యాత్ర Hera. | — | N154 |  |
| F830 | missions-voyager-new-horizons | Voyager 2 ను 1977 ఆగస్టు 20 న, Voyager 1 ను 1977 సెప్టెంబర్ 5 న NASA ప్రయోగించిం… | P008-F017 (Voyager 2, partial) | N155 |  |
| F831 | missions-voyager-new-horizons | Voyager 1 2012 లో Interstellar space లోకి ప్రవేశించిన మొదటి Spacecraft; భూమి నుం… | — | N155 |  |
| F832 | missions-voyager-new-horizons | Uranus, Neptune లను దగ్గరగా దాటిన ఏకైక Spacecraft Voyager 2. | P008-F017 (explanation) | N086 |  |
| F833 | missions-voyager-new-horizons | Voyager 1, 2 లలో భూమి గురించిన సందేశంతో Golden Record ఉంది. | — | N155 |  |
| F834 | missions-voyager-new-horizons | Saturn చుట్టూ తిరిగిన Orbiter Cassini; Jupiter చుట్టూ తిరిగిన Orbiter లు Galileo… | — | N155 |  |
| F835 | missions-voyager-new-horizons | New Horizons 2015 జూలై 14 న Pluto పక్క నుంచి వెళ్లింది. | — | N059, N155 |  |
| F836 | missions-venus-orbiter | Venus Orbiter Mission (Shukrayaan) కు కేంద్ర మంత్రిమండలి 2024 సెప్టెంబర్ 18 న ₹1… | — | N156 |  |
| F837 | missions-venus-orbiter | Venus Orbiter Mission ప్రయోగం 2028 మార్చి Launch window కు ప్లాన్ చేశారు (2026 న… | — | N156 |  |
| F838 | missions-venus-orbiter | సౌర కుటుంబంలో అత్యంత వేడి గ్రహం Venus (శుక్రుడు); కారణం దట్టమైన Carbon dioxide A… | SP-020 | N156 |  |

## Per section (facts / existing-covered / covered by new / new questions)

| Section | Facts | Existing | New-covered | New Qs |
|---|---|---|---|---|
| address-geography | 3 | 3 | 0 | 0 |
| address-geographers | 6 | 4 | 5 | 2 |
| address-spheres | 7 | 6 | 3 | 1 |
| address-our-address | 4 | 4 | 0 | 0 |
| universe-what | 5 | 4 | 0 | 0 |
| universe-galaxy | 3 | 1 | 2 | 1 |
| universe-milky-way | 7 | 6 | 3 | 1 |
| universe-nebula | 4 | 3 | 3 | 1 |
| universe-theories | 3 | 3 | 0 | 0 |
| universe-bigbang | 5 | 2 | 3 | 1 |
| universe-redshift | 6 | 3 | 4 | 1 |
| universe-cmb | 6 | 2 | 6 | 2 |
| universe-steady-state | 4 | 3 | 4 | 2 |
| universe-oscillating-inflation | 3 | 1 | 3 | 1 |
| universe-dark | 4 | 2 | 2 | 1 |
| distances-units | 2 | 2 | 0 | 0 |
| distances-au | 5 | 3 | 1 | 0 |
| distances-light-time | 4 | 3 | 3 | 1 |
| distances-light-year | 3 | 2 | 3 | 1 |
| distances-parallax | 7 | 1 | 5 | 2 |
| distances-parsec | 6 | 2 | 3 | 1 |
| distances-nearest-star | 4 | 2 | 3 | 1 |
| distances-nearest-galaxy | 5 | 2 | 4 | 1 |
| distances-closest-planet | 4 | 4 | 3 | 1 |
| sky-star-planet | 5 | 3 | 3 | 1 |
| sky-constellation | 5 | 3 | 3 | 1 |
| sky-asterism | 4 | 2 | 3 | 1 |
| sky-polaris | 8 | 2 | 6 | 2 |
| sky-brightness | 7 | 2 | 4 | 1 |
| sky-brightest | 7 | 3 | 4 | 1 |
| sky-inferior-superior | 7 | 4 | 5 | 2 |
| sky-ecliptic-zodiac | 7 | 1 | 4 | 1 |
| sky-astrology | 4 | 3 | 1 | 0 |
| stars-birth | 4 | 0 | 4 | 1 |
| stars-main-sequence | 6 | 2 | 4 | 1 |
| stars-end-paths | 5 | 3 | 3 | 1 |
| stars-red-giant-white-dwarf | 7 | 4 | 3 | 1 |
| stars-sun-future | 3 | 1 | 3 | 1 |
| stars-chandrasekhar | 8 | 2 | 5 | 2 |
| stars-dwarfs | 7 | 4 | 4 | 1 |
| stars-binary-nova | 4 | 3 | 3 | 1 |
| stars-supernova | 7 | 3 | 6 | 1 |
| stars-neutron-pulsar | 6 | 2 | 4 | 1 |
| stars-quark-star | 1 | 1 | 0 | 0 |
| stars-black-hole | 7 | 1 | 6 | 2 |
| stars-black-hole-history | 3 | 2 | 3 | 1 |
| stars-quasar | 4 | 2 | 3 | 1 |
| formation-nebular-model | 7 | 6 | 3 | 1 |
| formation-rocky-giant | 5 | 1 | 4 | 1 |
| formation-ages | 10 | 3 | 5 | 2 |
| formation-hypotheses | 8 | 6 | 4 | 1 |
| formation-kant-laplace | 4 | 1 | 3 | 1 |
| formation-encounter | 5 | 4 | 3 | 1 |
| formation-schmidt-weizsacker | 5 | 3 | 4 | 1 |
| formation-planet-definition | 5 | 4 | 4 | 1 |
| formation-pluto-reclassification | 5 | 2 | 5 | 3 |
| sun-what | 11 | 9 | 4 | 1 |
| sun-fusion | 3 | 2 | 3 | 1 |
| sun-interior | 4 | 2 | 3 | 1 |
| sun-atmosphere | 7 | 5 | 3 | 1 |
| sun-temperature-exam | 3 | 2 | 3 | 1 |
| sun-spectrum | 5 | 1 | 5 | 2 |
| sun-sunspots-cycle | 8 | 2 | 7 | 2 |
| sun-wind-flare-cme | 5 | 3 | 2 | 1 |
| sun-storms-aurora | 8 | 2 | 4 | 1 |
| inner-rocky | 5 | 4 | 0 | 0 |
| inner-motion | 5 | 2 | 0 | 0 |
| inner-mercury | 9 | 6 | 6 | 2 |
| inner-venus | 8 | 7 | 4 | 1 |
| inner-greenhouse | 3 | 2 | 2 | 1 |
| inner-earth | 6 | 3 | 5 | 1 |
| inner-earth-shape | 4 | 1 | 3 | 1 |
| inner-mars | 6 | 4 | 3 | 1 |
| inner-mars-features | 5 | 3 | 4 | 1 |
| inner-compare | 2 | 2 | 0 | 0 |
| outer-giants | 3 | 2 | 3 | 1 |
| outer-colours | 3 | 3 | 0 | 0 |
| outer-rings | 6 | 2 | 3 | 1 |
| outer-jupiter | 5 | 4 | 4 | 1 |
| outer-galilean | 6 | 4 | 5 | 2 |
| outer-saturn | 6 | 4 | 3 | 2 |
| outer-uranus | 6 | 4 | 5 | 2 |
| outer-neptune | 5 | 3 | 4 | 2 |
| outer-moon-counts | 2 | 2 | 0 | 0 |
| asteroid-belt | 8 | 3 | 6 | 2 |
| ceres | 6 | 2 | 6 | 2 |
| kuiper | 8 | 4 | 5 | 1 |
| oort | 4 | 2 | 4 | 1 |
| comet-structure | 6 | 3 | 3 | 1 |
| comet-tails | 6 | 4 | 1 | 0 |
| halley | 7 | 2 | 2 | 1 |
| sl9 | 4 | 0 | 4 | 1 |
| meteor-stages | 7 | 4 | 6 | 2 |
| small-bodies-compare | 2 | 1 | 2 | 1 |
| meteor-shower | 7 | 2 | 5 | 1 |
| small-bodies-impacts-missions | 5 | 0 | 5 | 2 |
| compare-mass-weight | 6 | 2 | 3 | 1 |
| compare-diameter | 3 | 1 | 3 | 1 |
| compare-size | 5 | 5 | 0 | 0 |
| compare-motion | 6 | 5 | 2 | 0 |
| compare-distance | 3 | 2 | 1 | 0 |
| compare-checklist | 1 | 0 | 1 | 1 |
| compare-records-size | 4 | 4 | 2 | 0 |
| compare-records-density | 1 | 1 | 0 | 0 |
| compare-records-temperature | 3 | 2 | 3 | 2 |
| compare-records-spin | 2 | 2 | 0 | 0 |
| compare-records-moons | 2 | 2 | 0 | 0 |
| motion-rotation-revolution | 5 | 2 | 3 | 1 |
| motion-sidereal-solar-day | 4 | 2 | 4 | 1 |
| motion-retrograde-rotation | 6 | 4 | 5 | 1 |
| motion-same-direction | 4 | 0 | 4 | 1 |
| motion-mercury-venus-day | 4 | 2 | 4 | 1 |
| motion-kepler-laws | 11 | 8 | 6 | 1 |
| motion-why-orbit | 4 | 0 | 3 | 1 |
| motion-perihelion-aphelion | 5 | 2 | 3 | 1 |
| seasons-tilt | 5 | 3 | 3 | 1 |
| seasons-cause | 4 | 1 | 3 | 1 |
| seasons-dates | 8 | 2 | 5 | 2 |
| seasons-equinox-day | 3 | 0 | 3 | 1 |
| seasons-vijayawada | 4 | 2 | 4 | 1 |
| seasons-ap-heat | 4 | 0 | 4 | 1 |
| seasons-distance | 3 | 1 | 2 | 0 |
| moon-size | 7 | 6 | 3 | 1 |
| moon-gravity | 3 | 1 | 3 | 1 |
| moon-origin | 6 | 4 | 4 | 1 |
| moon-phases | 8 | 7 | 3 | 1 |
| moon-month | 4 | 3 | 3 | 1 |
| moon-oneface | 4 | 3 | 3 | 1 |
| moon-surface | 7 | 3 | 4 | 1 |
| moon-chandrayaan | 11 | 8 | 3 | 1 |
| eclipse-what | 4 | 3 | 1 | 0 |
| eclipse-not-monthly | 4 | 3 | 3 | 1 |
| eclipse-shadow-parts | 5 | 4 | 3 | 1 |
| eclipse-solar-types | 5 | 2 | 4 | 1 |
| eclipse-lunar-types | 4 | 0 | 4 | 1 |
| eclipse-safety | 3 | 1 | 3 | 1 |
| eclipse-saros-count | 6 | 5 | 3 | 1 |
| eclipse-phases-vs | 5 | 5 | 0 | 0 |
| tides-what | 3 | 3 | 0 | 0 |
| tides-moon-vs-sun | 4 | 2 | 4 | 1 |
| tides-two-a-day | 5 | 0 | 4 | 1 |
| tides-spring-neap | 5 | 4 | 3 | 1 |
| tides-range-calc | 2 | 1 | 2 | 1 |
| tides-local-factors | 4 | 0 | 3 | 1 |
| tides-storm-surge | 4 | 2 | 4 | 1 |
| tides-uses | 5 | 0 | 5 | 1 |
| tides-phases-eclipse | 1 | 1 | 0 | 0 |
| history-geocentric | 7 | 5 | 5 | 1 |
| history-indian | 12 | 4 | 8 | 2 |
| history-heliocentric | 6 | 3 | 4 | 1 |
| history-galileo | 6 | 1 | 6 | 1 |
| history-kepler-newton | 6 | 3 | 3 | 1 |
| history-planet-names | 8 | 5 | 4 | 1 |
| history-astronomy-terms | 6 | 5 | 3 | 1 |
| history-who-first | 2 | 1 | 2 | 1 |
| missions-types | 4 | 2 | 4 | 1 |
| missions-satellite-payload | 6 | 3 | 5 | 1 |
| missions-l1 | 5 | 1 | 5 | 1 |
| missions-aditya | 5 | 3 | 4 | 1 |
| missions-sun-international | 7 | 3 | 5 | 1 |
| missions-mars | 6 | 3 | 5 | 1 |
| missions-dart | 5 | 3 | 4 | 1 |
| missions-voyager-new-horizons | 6 | 2 | 6 | 1 |
| missions-venus-orbiter | 3 | 1 | 3 | 1 |
