# AP History subtopic taxonomy — DRAFT for bilingual review

Nothing here is seeded. The subtopics stay a draft until you approve them; the importer will not create any. Source-support counts come from the draft note-section mapping (`ap_history_note_mapping_draft.csv`); a count of 0 is a fact about the current notes, not a verdict that the subtopic is wrong (some are exam topics the notes do not yet cover).

- Subtopics: **314** in 31 chapters. Flagged for a decision: 181. Flag counts: duplicate 7, overlap 62, narrow 32, note_driven 14, no_source 114, telugu_review 19, by_design 12
- Flags: `duplicate` same concept, different name; `overlap` overlaps another subtopic; `narrow` one person/event/paper; `note_driven` exists mainly for one current note heading; `no_source` no note section maps here; `telugu_review` Telugu wording needs a decision; `by_design` overlap is deliberate (thematic chapter 14).

## Chapters with too many or too few subtopics

- Chapter 8 — Eastern Chalukyas of Vengi and Andhra Cholas: 15 subtopics, 3 without source. Includes the new `art-architecture`; several subtopics overlap and some have no source.
- Chapter 9 — Kakatiyas: 17 subtopics, 0 without source. Highest count; six per-ruler subtopics could be reduced.
- Chapter 12 — Gajapatis, Bahmanis and Other Regional Powers: 7 subtopics, 5 without source. Thin source coverage: most subtopics have no note section.
- Chapter 14 — Thematic History of Andhradesa, 11th–16th Centuries: 12 subtopics, 8 without source. Thematic chapter: no_source is expected because questions keep one primary dynasty chapter.
- Chapter 17 — Socio-Cultural Awakening: 10 subtopics, 6 without source. 
- Chapter 18 — Justice Party and Self-Respect Movement: 7 subtopics, 6 without source. 
- Chapter 20 — Socialists, Communists, Anti-Zamindari and Kisan Movements: 9 subtopics, 6 without source. 
- Chapter 21 — Nationalist Poetry, Revolutionary Literature and Nataka Samasthalu: 9 subtopics, 7 without source. 
- Chapter 22 — Women's Participation: 8 subtopics, 8 without source. 
- Chapter 24 — Andhra Mahasabhas and Prominent Leaders: 6 subtopics, 4 without source. Low count and overlaps chapter 23.
- Chapter 25 — Press, Newspapers and the Library Movement: 10 subtopics, 8 without source. 
- Chapter 26 — Folk and Tribal Culture: 9 subtopics, 6 without source. 
- Chapter 27 — Formation of Andhra State, 1953: 12 subtopics, 6 without source. 
- Chapter 28 — Visalandhra Movement and Visalandhra Mahasabha: 6 subtopics, 2 without source. Low count; the merger debate also lives in chapters 29 and 30.
- Chapter 29 — States Reorganisation Commission: 7 subtopics, 4 without source. Several subtopics have no source.
- Chapter 31 — Important Social and Cultural Events, 1956–2014: 14 subtopics, 5 without source. Spans 58 years; subtopics overlap with chapters 21, 22 and 25.

## Pairs to merge or decide (duplicate or overlapping concepts)

- ch21 `drama-organisations` — Drama organisations: Same concept as `nataka-samasthalu` in this chapter (drama societies). Keep one.
- ch21 `nataka-samasthalu` — Nataka Samasthalu: Same concept as `drama-organisations`; the Telugu term Nataka Samajalu is the one used in the notes.
- ch23 `major-resolutions` — Major resolutions: Same concept as ch24 `resolutions` (Andhra Mahasabha resolutions). Decide which chapter owns resolutions.
- ch24 `resolutions` — Resolutions: See ch23 `major-resolutions`.
- ch25 `libraries-public-awakening` — Libraries as centres of public awakening: Three library subtopics in one chapter (library-movement, andhra-desa-library-association, libraries-public-awakening).
- ch27 `potti-sriramulu` — Potti Sriramulu: Overlaps `fast-and-death` (his fast and death are the event). Keep either a person subtopic or the event.
- ch27 `fast-and-death` — Potti Sriramulu's fast and death: See `potti-sriramulu`.

## Subtopics that exist mainly for one note heading

- ch5 `royal-women` — Royal women (1 section). Maps one note section.
- ch7 `sanskrit-telugu-development` — Sanskrit and Telugu development (1 section). One note section.
- ch8 `chola-chalukya-relations` — Chola–Chalukya relations and the Chalukya-Chola period (1 section). One note section.
- ch9 `rudradeva` — Rudradeva (1 section). Per-ruler subtopics: six rulers in one chapter. Consider 'Early rulers' + 'Ganapatideva' + 'Rudramadevi' + 'Prataparudra'.
- ch9 `mahadeva` — Mahadeva (1 section). See `rudradeva`.
- ch9 `ganapatideva` — Ganapatideva (1 section). Major ruler; keep if exams ask per-ruler.
- ch9 `rudramadevi` — Rudramadevi (1 section). Major ruler; keep.
- ch9 `prataparudra` — Prataparudra (1 section). See `rudradeva`.
- ch9 `crafts-trade-motupalli` — Crafts, trade and Motupalli (1 section). Motupalli is the note heading; the subtopic is broader in intent.
- ch11 `andhra-campaigns-gajapati-bahmani` — Andhra campaigns; Gajapati and Bahmani conflicts (1 section). Overlaps ch12 subtopics.
- ch16 `thomas-munro` — Thomas Munro (1 section). One person; ryotwari is already a subtopic.
- ch16 `arthur-cotton` — Arthur Cotton (1 section). One person; irrigation works would be the broader subtopic.
- ch27 `tanguturi-prakasam` — Tanguturi Prakasam (1 section). One person; maps one note section.
- ch31 `cultural-developments-to-2014` — Major cultural developments up to 2014 (1 section). Catch-all that overlaps literature, theatre, cinema, visual-performing-arts.

## Telugu translations needing review

Evidence is how often each spelling appears in the current notes (chapters 1-12 in the app database, 13-19 in the local HTML files). No automatic translation is used at render time; whichever form is chosen becomes the one the bank uses.

| Ch | Subtopic | Current Telugu | Issue | Suggestion |
|---|---|---|---|---|
| 2 | `palaeolithic` | పురా శిలాయుగం | The notes use 'దిగువ శిలాయుగం' (10 times), 'పాషాణయుగం' (1); 'పురా శిలాయుగం' appears 0 times. Pick one term for the Palaeolithic and apply it to Mesolithic/Neolithic/Chalcolithic too. | Decide: దిగువ/మధ్య/ఎగువ శిలాయుగం, or పాత రాతి యుగం. |
| 2 | `chalcolithic` | తామ్ర శిలాయుగం | 0 occurrences of this form or 'తామ్ర యుగం' or 'చాల్కోలిథిక్' in the notes; term to be confirmed. | Reviewer to choose. |
| 2 | `megalithic-iron-age` | మహాశిలా (మెగాలిథిక్) మరియు ఇనుప యుగ సంస్కృతులు | The notes use 'మెగాలిథిక్' (72) not 'మహాశిలా' (0); 'బృహత్శిలా' 2. | Prefer the form learners see in the notes. |
| 3 | `kharavela-hathigumpha` | ఖారవేలుడు మరియు హాథీగుంఫా శాసనం | Notes spell 'హాతిగుంఫా' (8) and 'ఖారవేల' (11) / 'ఖారవేలుడు' (9); the subtopic uses 'హాథీగుంఫా' (0). | Use 'హాతిగుంఫా' if the notes are the standard. |
| 3 | `punch-marked-local-coinage` | ఆహత (పంచ్-మార్క్డ్) మరియు స్థానిక నాణేలు | 'ఆహత' is a rare form (0 in notes); notes use 'పంచ్‌మార్క్' (7) / 'పంచ్-మార్క్డ్' (4). | Drop the 'ఆహత' gloss or keep both. |
| 8 | `temples-pancharamas` | దేవాలయాలు మరియు పంచారామాలు | Consistent ('పంచారామ' 50). No issue. |  |
| 9 | `administration-nayankara` | పరిపాలన మరియు నాయంకర వ్యవస్థ | 'నాయంకర' 79 vs 'నాయకత్వ' 58 (the latter is a different word, not a variant). | No change; keep 'నాయంకర'. |
| 10 | `musunuri-nayakas` | ముసునూరి ప్రోలయ నాయకుడు, కాపయ నాయకుడు మరియు ఓరుగల్లు విముక్తి | Notes spell Musunuri three ways: 'మూసూరి' 42, 'మునుసూరి' 23, 'ముసునూరి' 16. The subtopic uses the spelling in the minority. | Choose one spelling for the whole bank; 'ముసునూరి' is the established Telugu spelling but the notes disagree. |
| 11 | `battle-of-talikota` | తళ్ళికోట యుద్ధం | Notes use 'తాలికోట' 40, 'తాళికోట' 38, 'తళ్ళికోట' 8. The subtopic uses the rarest form. | Choose one; 'తళ్ళికోట' is common in Telugu textbooks but the notes use others. |
| 13 | `establishment` | కుతుబ్‌షాహీ అధికార స్థాపన | Notes: 'కుతుబ్ షాహీ' 77, 'కుతుబ్షాహీ' 11, 'కుతుబ్ షాహి' 2. The subtopic uses a zero-width joiner form. | Use 'కుతుబ్ షాహీ' with a space; avoid ZWJ in slugs/search. |
| 13 | `telugu-dakhni-patronage` | తెలుగు మరియు దక్కనీ భాషల పోషణ | Notes: 'డఖ్ఖనీ' 14, 'దక్కనీ' 7, 'దక్కని' 3. | Choose one. |
| 15 | `northern-circars` | ఉత్తర సర్కారులు | Notes: 'ఉత్తర సర్కార్' 32, 'ఉత్తర సర్కార్లు' 16, 'ఉత్తర సర్కారులు' 1. | Use 'ఉత్తర సర్కార్లు'. |
| 15 | `ceded-districts` | దత్త మండలాలు | Notes use 'సీడెడ్' 34 / 'సీడెడ్ డిస్ట్రిక్ట్స్' 27 and 'దత్త మండలాలు' 0-1. | Use the learner-facing 'రాయలసీమ (దత్త మండలాలు)' or the notes' term. |
| 16 | `zamindari-ryotwari` | జమీందారీ మరియు రైత్వారీ విధానాలు | Notes: 'రయొత్వారీ' 23, 'రైత్వారీ' 2, 'రయత్వారీ' 1. | Use 'రయత్వారీ' or 'రైత్వారీ' consistently. |
| 23 | `sri-bagh-pact` | శ్రీబాగ్ ఒడంబడిక | Notes use 'శ్రీబాగ్ ఒప్పందం' 16 and 'ఒడంబడిక' 0. | Use 'శ్రీబాగ్ ఒప్పందం'. |
| 30 | `(chapter)` | పెద్దమనుషుల ఒప్పందం మరియు ఆంధ్రప్రదేశ్ ఏర్పాటు | Notes use 'జెంటిల్మెన్స్ అగ్రిమెంట్' 42 and 'పెద్దమనుషుల ఒప్పందం' 0. | Pick the learner-facing form for the title and subtopics. |
| 27 | `dhar-commission` | ధార్ కమిషన్ | 'ధార్ కమిషన్' 1 vs 'ధార్ కమీషన్' 0. | Keep, once the spelling is confirmed. |
| 27 | `jvp-committee` | జె.వి.పి. కమిటీ | The notes write 'JVP' in Latin letters 7 times; the Telugu form 'జె.వి.పి' has 0. | Decide the transliteration for the committee name. |
| 29 | `(chapter)` | రాష్ట్రాల పునర్వ్యవస్థీకరణ సంఘం | 'SRC' appears in Latin letters 81 times and 'రాష్ట్రాల పునర్వ్యవస్థీకరణ' 9 times. | Decide whether the learner-facing name uses the abbreviation. |
| 19 | `home-rule` | స్వపరిపాలన (హోమ్ రూల్) ఉద్యమం | 'హోమ్ రూల్' 0 vs 'స్వపరిపాలన' 5 in the notes. | Reviewer to choose. |

## Full taxonomy: Unit → Chapter → subtopic (English / Telugu / classification)

### Unit 1

#### Chapter 1 — Andhra Region, People and Historical Sources (bridge)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Geographical extent and historical meaning of Andhradesa | ఆంధ్రదేశ భౌగోళిక విస్తీర్ణం మరియు చారిత్రక అర్థం | 0/0 | no_source |
| Andhra people and origin of the name | ఆంధ్రులు మరియు పేరు పుట్టుక | 3/1 |  |
| Development of Telugu identity and language | తెలుగు గుర్తింపు మరియు భాష వికాసం | 1/2 |  |
| Literary sources | సాహిత్య ఆధారాలు | 1/1 |  |
| Inscriptions | శాసనాలు | 1/2 | overlap |
| Coins | నాణేలు | 1/0 | overlap |
| Archaeological evidence | పురావస్తు ఆధారాలు | 3/1 |  |
| Foreign accounts | విదేశీయుల రచనలు | 1/1 |  |
| Important historical sites | ముఖ్య చారిత్రక స్థలాలు | 1/8 | overlap |

#### Chapter 2 — Prehistoric Cultures of Andhra (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Palaeolithic | పురా శిలాయుగం | 3/1 | telugu_review |
| Mesolithic | మధ్య శిలాయుగం | 1/0 |  |
| Neolithic | నవీన శిలాయుగం | 1/0 |  |
| Chalcolithic | తామ్ర శిలాయుగం | 0/0 | no_source;telugu_review |
| Megalithic and Iron Age cultures | మహాశిలా (మెగాలిథిక్) మరియు ఇనుప యుగ సంస్కృతులు | 1/0 | telugu_review |
| Tools and technologies | పనిముట్లు మరియు సాంకేతికత | 1/1 |  |
| Pottery | మట్టి పాత్రలు | 0/0 | overlap;no_source |
| Burial practices | ఖననాచారాలు | 0/1 |  |
| Important prehistoric sites in Andhra | ఆంధ్రలోని ముఖ్య చరిత్రపూర్వ స్థలాలు | 1/1 |  |

#### Chapter 3 — Pre-Satavahana Andhra (bridge)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Assaka / Asmaka | అస్సక / అశ్మక | 2/0 |  |
| Early Andhra references | ఆంధ్రుల తొలి ప్రస్తావనలు | 2/1 |  |
| Nandas and Mauryas | నందులు మరియు మౌర్యులు | 1/1 |  |
| Ashoka's Andhra inscriptions | ఆంధ్రలో అశోకుని శాసనాలు | 0/1 | overlap |
| Erragudi and Rajulamandagiri | ఎర్రగుడి మరియు రాజులమందగిరి | 0/1 | narrow |
| Bhattiprolu | భట్టిప్రోలు | 1/0 |  |
| Early Buddhism | తొలి బౌద్ధమతం | 1/0 |  |
| Amaravati / Dhanyakataka beginnings | అమరావతి / ధాన్యకటకం ఆరంభాలు | 0/1 | overlap;narrow |
| Kharavela and the Hathigumpha inscription | ఖారవేలుడు మరియు హాథీగుంఫా శాసనం | 0/0 | no_source;telugu_review |
| Early local rulers | తొలి స్థానిక పాలకులు | 1/1 |  |
| Punch-marked and local coinage | ఆహత (పంచ్-మార్క్డ్) మరియు స్థానిక నాణేలు | 0/0 | overlap;no_source;telugu_review |

#### Chapter 4 — Satavahanas (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Origin and homeland theories | మూలం మరియు జన్మభూమి సిద్ధాంతాలు | 1/1 |  |
| Chronology | కాలక్రమం | 1/0 |  |
| Political history | రాజకీయ చరిత్ర | 3/1 |  |
| Important rulers | ముఖ్య పాలకులు | 2/1 |  |
| Administration | పరిపాలన | 0/0 | no_source |
| Society | సమాజం | 1/0 |  |
| Economy, agriculture, guilds and trade (including Indo-Roman trade) | ఆర్థిక వ్యవస్థ, వ్యవసాయం, వర్తక శ్రేణులు మరియు వాణిజ్యం (ఇండో-రోమన్ వాణిజ్యంతో సహా) | 0/1 |  |
| Coinage | నాణేల వ్యవస్థ | 1/1 |  |
| Religion | మతం | 1/0 |  |
| Prakrit and literature | ప్రాకృతం మరియు సాహిత్యం | 0/1 |  |
| Amaravati art and architecture | అమరావతి కళ మరియు వాస్తుశిల్పం | 1/0 |  |
| Inscriptions | శాసనాలు | 1/1 |  |
| Decline | పతనం | 0/0 | no_source |

#### Chapter 5 — Ikshvakus (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Origin and chronology | మూలం మరియు కాలక్రమం | 1/1 |  |
| Important rulers | ముఖ్య పాలకులు | 5/0 |  |
| Vijayapuri and Nagarjunakonda | విజయపురి మరియు నాగార్జునకొండ | 2/1 |  |
| Administration | పరిపాలన | 1/0 |  |
| Socio-economic conditions | సామాజిక-ఆర్థిక పరిస్థితులు | 1/0 |  |
| Buddhism | బౌద్ధమతం | 1/2 | overlap |
| Brahmanism | బ్రాహ్మణ మతం | 0/2 |  |
| Royal women | రాజవంశ స్త్రీలు | 1/0 | narrow;note_driven |
| Literature and education | సాహిత్యం మరియు విద్య | 0/0 | no_source |
| Art and architecture | కళ మరియు వాస్తుశిల్పం | 2/0 |  |
| Inscriptions | శాసనాలు | 1/1 |  |
| Decline | పతనం | 1/1 |  |

#### Chapter 6 — Post-Ikshvaku Minor Dynasties (bridge)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Brihatphalayanas | బృహత్‌ఫలాయనులు | 1/0 |  |
| Ananda Gotrikas | ఆనంద గోత్రికులు | 1/1 |  |
| Salankayanas | శాలంకాయనులు | 4/1 |  |
| Pallava influence | పల్లవుల ప్రభావం | 0/0 | no_source |
| Other transitional dynasties | ఇతర పరివర్తన రాజవంశాలు | 0/0 | overlap;no_source |
| Political conditions | రాజకీయ పరిస్థితులు | 1/1 |  |
| Society and economy | సమాజం మరియు ఆర్థిక వ్యవస్థ | 0/0 | no_source |
| Religion | మతం | 3/0 |  |
| Inscriptions | శాసనాలు | 1/0 |  |
| Art and architecture | కళ మరియు వాస్తుశిల్పం | 1/0 |  |

#### Chapter 7 — Vishnukundins (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Origin and chronology | మూలం మరియు కాలక్రమం | 2/2 |  |
| Important rulers | ముఖ్య పాలకులు | 3/1 |  |
| Political expansion | రాజకీయ విస్తరణ | 2/1 |  |
| Administration | పరిపాలన | 0/0 | no_source |
| Society and economy | సమాజం మరియు ఆర్థిక వ్యవస్థ | 0/0 | no_source |
| Religion | మతం | 1/0 |  |
| Sanskrit and Telugu development | సంస్కృతం మరియు తెలుగు వికాసం | 1/1 | note_driven;telugu_review |
| Cave and temple architecture | గుహలు మరియు దేవాలయ వాస్తుశిల్పం | 2/0 | overlap |
| Coins | నాణేలు | 1/0 |  |
| Inscriptions | శాసనాలు | 2/1 |  |
| Decline | పతనం | 2/0 |  |

#### Chapter 8 — Eastern Chalukyas of Vengi and Andhra Cholas (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Foundation of the Vengi kingdom | వేంగి రాజ్య స్థాపన | 2/3 |  |
| Political chronology | రాజకీయ కాలక్రమం | 1/0 |  |
| Important rulers | ముఖ్య పాలకులు | 7/0 | overlap |
| Chola–Chalukya relations and the Chalukya-Chola period | చోళ–చాళుక్య సంబంధాలు మరియు చాళుక్య-చోళ యుగం | 1/0 | note_driven |
| Administration | పరిపాలన | 0/1 |  |
| Society and economy | సమాజం మరియు ఆర్థిక వ్యవస్థ | 0/0 | no_source |
| Religion | మతం | 1/1 |  |
| Growth of Telugu; Nannaya and early Telugu literature | తెలుగు వికాసం; నన్నయ మరియు తొలి తెలుగు సాహిత్యం | 1/1 |  |
| Art and architecture | కళ మరియు వాస్తుశిల్పం | 1/0 | overlap |
| Temples and Pancharamas | దేవాలయాలు మరియు పంచారామాలు | 1/2 | overlap;narrow;telugu_review |
| Velanati Chodas | వెలనాటి చోడులు | 0/1 |  |
| Nellore Telugu Chodas | నెల్లూరు తెలుగు చోడులు | 0/0 | no_source |
| Palnadu War | పల్నాటి యుద్ధం | 0/0 | narrow;no_source |
| Inscriptions | శాసనాలు | 0/1 |  |
| Decline and transition | పతనం మరియు పరివర్తన | 1/0 |  |

### Unit 2

#### Chapter 9 — Kakatiyas (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Origin and early rulers | మూలం మరియు తొలి పాలకులు | 1/0 | overlap |
| Rudradeva | రుద్రదేవుడు | 1/0 | narrow;note_driven |
| Mahadeva | మహాదేవుడు | 1/0 | narrow;note_driven |
| Ganapatideva | గణపతిదేవుడు | 1/0 | narrow;note_driven |
| Rudramadevi | రుద్రమదేవి | 1/0 | narrow;note_driven |
| Prataparudra | ప్రతాపరుద్రుడు | 1/0 | narrow;note_driven |
| Political expansion | రాజకీయ విస్తరణ | 1/0 | overlap |
| Delhi Sultanate invasions | ఢిల్లీ సుల్తానుల దండయాత్రలు | 1/1 |  |
| Administration and the Nayankara system | పరిపాలన మరియు నాయంకర వ్యవస్థ | 1/0 | telugu_review |
| Irrigation and agriculture | నీటిపారుదల మరియు వ్యవసాయం | 0/1 |  |
| Crafts, trade and Motupalli | చేతివృత్తులు, వాణిజ్యం మరియు మోటుపల్లి | 1/0 | note_driven |
| Society | సమాజం | 0/1 |  |
| Religion | మతం | 1/0 |  |
| Telugu literature | తెలుగు సాహిత్యం | 1/0 |  |
| Dance and music | నృత్యం మరియు సంగీతం | 0/1 |  |
| Art and architecture | కళ మరియు వాస్తుశిల్పం | 3/1 |  |
| Decline | పతనం | 0/1 |  |

#### Chapter 10 — Musunuri Nayakas, Reddy Kingdoms and Velama Chiefs (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Post-Kakatiya political conditions | కాకతీయానంతర రాజకీయ పరిస్థితులు | 1/0 |  |
| Musunuri Prolaya Nayaka, Kapaya Nayaka and the liberation of Warangal | ముసునూరి ప్రోలయ నాయకుడు, కాపయ నాయకుడు మరియు ఓరుగల్లు విముక్తి | 2/0 | telugu_review |
| Kondavidu Reddys | కొండవీడు రెడ్డిలు | 3/0 | overlap |
| Rajahmundry Reddys | రాజమహేంద్రవరం రెడ్డిలు | 2/0 |  |
| Recharla Velamas (Rachakonda and Devarakonda) | రేచర్ల వెలమలు (రాచకొండ మరియు దేవరకొండ) | 1/0 |  |
| Administration | పరిపాలన | 1/0 |  |
| Society and economy | సమాజం మరియు ఆర్థిక వ్యవస్థ | 0/2 |  |
| Religion | మతం | 1/0 |  |
| Telugu literature | తెలుగు సాహిత్యం | 2/0 |  |
| Art and architecture | కళ మరియు వాస్తుశిల్పం | 1/0 |  |
| Regional conflicts | ప్రాంతీయ సంఘర్షణలు | 1/0 | overlap |

#### Chapter 11 — Vijayanagara and Andhra (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Foundation | స్థాపన | 1/0 |  |
| Four dynasties | నాలుగు రాజవంశాలు | 3/2 | overlap |
| Important rulers | ముఖ్య పాలకులు | 2/2 |  |
| Sri Krishnadevaraya | శ్రీకృష్ణదేవరాయలు | 1/1 |  |
| Andhra campaigns; Gajapati and Bahmani conflicts | ఆంధ్రలో సైనిక దండయాత్రలు; గజపతి మరియు బహమనీ సంఘర్షణలు | 1/0 | overlap;note_driven |
| Administration and the Nayankara system | పరిపాలన మరియు నాయంకర వ్యవస్థ | 1/0 |  |
| Economy and trade | ఆర్థిక వ్యవస్థ మరియు వాణిజ్యం | 0/1 |  |
| Society | సమాజం | 0/0 | no_source |
| Religion | మతం | 1/0 |  |
| Telugu literature and the Ashtadiggajas | తెలుగు సాహిత్యం మరియు అష్టదిగ్గజాలు | 2/0 | narrow |
| Art and architecture | కళ మరియు వాస్తుశిల్పం | 1/1 |  |
| Battle of Talikota | తళ్ళికోట యుద్ధం | 1/1 | overlap;telugu_review |
| Decline | పతనం | 2/0 |  |

#### Chapter 12 — Gajapatis, Bahmanis and Other Regional Powers (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Gajapati rule and influence in Andhra | ఆంధ్రలో గజపతుల పాలన మరియు ప్రభావం | 0/2 | overlap |
| Bahmani–Vijayanagara rivalry | బహమనీ–విజయనగర వైరం | 0/1 | overlap |
| Coastal Andhra conflicts | తీరాంధ్ర సంఘర్షణలు | 0/0 | no_source |
| Minor regional powers | చిన్న ప్రాంతీయ శక్తులు | 0/0 | no_source |
| Forts and political centres | కోటలు మరియు రాజకీయ కేంద్రాలు | 0/0 | no_source |
| Socio-cultural influence | సామాజిక-సాంస్కృతిక ప్రభావం | 0/0 | no_source |
| Political transition | రాజకీయ పరివర్తన | 0/0 | no_source |

#### Chapter 13 — Qutb Shahis and Sixteenth-Century Andhra (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Establishment of Qutb Shahi power | కుతుబ్‌షాహీ అధికార స్థాపన | 1/0 | telugu_review |
| Important sixteenth-century rulers | పదహారో శతాబ్దపు ముఖ్య పాలకులు | 3/0 |  |
| Expansion into Andhra | ఆంధ్రలో విస్తరణ | 0/0 | overlap;no_source |
| Administration | పరిపాలన | 1/0 |  |
| Society and economy | సమాజం మరియు ఆర్థిక వ్యవస్థ | 0/1 |  |
| Trade, ports and Golconda commerce | వాణిజ్యం, రేవులు మరియు గోల్కొండ వర్తకం | 0/1 |  |
| Religion | మతం | 1/0 |  |
| Telugu and Dakhni patronage | తెలుగు మరియు దక్కనీ భాషల పోషణ | 1/1 | telugu_review |
| Art and architecture | కళ మరియు వాస్తుశిల్పం | 4/1 |  |

#### Chapter 14 — Thematic History of Andhradesa, 11th–16th Centuries (thematic)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Comparative administration | తులనాత్మక పరిపాలన | 0/0 | no_source;by_design |
| Social structure | సామాజిక నిర్మాణం | 0/0 | no_source;by_design |
| Economic conditions | ఆర్థిక పరిస్థితులు | 0/0 | overlap;no_source;by_design |
| Agriculture and irrigation | వ్యవసాయం మరియు నీటిపారుదల | 0/0 | no_source;by_design |
| Internal and overseas trade | అంతర్గత మరియు విదేశీ వాణిజ్యం | 0/0 | no_source;by_design |
| Religious movements | మత ఉద్యమాలు | 0/1 | by_design |
| Growth of Telugu | తెలుగు వికాసం | 0/1 | by_design |
| Major authors and works | ముఖ్య కవులు మరియు రచనలు | 0/3 | by_design |
| Sculpture | శిల్పకళ | 0/0 | overlap;no_source;by_design |
| Temple architecture | దేవాలయ వాస్తుశిల్పం | 0/0 | no_source;by_design |
| Forts | కోటలు | 0/1 | by_design |
| Music and dance | సంగీతం మరియు నృత్యం | 0/0 | no_source;by_design |

### Unit 3

#### Chapter 15 — Europeans, Trading Centres and Company Rule (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Portuguese | పోర్చుగీసువారు | 0/0 | narrow;no_source |
| Dutch | డచ్చివారు | 0/0 | narrow;no_source |
| English | ఆంగ్లేయులు | 0/0 | narrow;no_source |
| French | ఫ్రెంచివారు | 0/0 | narrow;no_source |
| European trading centres and ports | యూరోపియన్ వ్యాపార కేంద్రాలు మరియు రేవులు | 1/0 |  |
| European rivalries | యూరోపియన్ల మధ్య పోటీ | 1/1 |  |
| Northern Circars | ఉత్తర సర్కారులు | 1/1 | telugu_review |
| Ceded Districts | దత్త మండలాలు | 1/0 | telugu_review |
| Andhra under the East India Company | ఈస్టిండియా కంపెనీ పాలనలో ఆంధ్ర | 0/1 |  |
| Revenue systems | శిస్తు (రెవెన్యూ) విధానాలు | 0/1 | overlap |
| Early economic and social impact | తొలి ఆర్థిక మరియు సామాజిక ప్రభావం | 0/1 |  |

#### Chapter 16 — Establishment of British Rule and the Impact of 1857 (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Consolidation of British administration | బ్రిటిష్ పరిపాలన స్థిరీకరణ | 1/0 |  |
| Zamindari and Ryotwari systems | జమీందారీ మరియు రైత్వారీ విధానాలు | 1/1 | overlap;telugu_review |
| Thomas Munro | థామస్ మన్రో | 1/0 | narrow;note_driven |
| Arthur Cotton | ఆర్థర్ కాటన్ | 1/0 | narrow;note_driven |
| Administrative and economic effects | పరిపాలనా మరియు ఆర్థిక ప్రభావాలు | 1/0 |  |
| Revolt of 1857 | 1857 తిరుగుబాటు | 0/1 |  |
| Events and personalities connected to Andhra | ఆంధ్రకు సంబంధించిన సంఘటనలు మరియు వ్యక్తులు | 0/0 | no_source |
| Impact of 1857 on Andhra | ఆంధ్రపై 1857 ప్రభావం | 1/0 |  |

#### Chapter 17 — Socio-Cultural Awakening (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Western education | పాశ్చాత్య విద్య | 1/0 |  |
| Missionary activity | క్రైస్తవ మిషనరీ కార్యకలాపాలు | 0/0 | no_source |
| Print culture | ముద్రణ సంస్కృతి | 0/1 |  |
| Social reform | సామాజిక సంస్కరణ | 0/2 |  |
| Kandukuri Veeresalingam | కందుకూరి వీరేశలింగం | 0/0 | narrow;no_source |
| Raghupati Venkataratnam Naidu | రఘుపతి వెంకటరత్నం నాయుడు | 0/0 | narrow;no_source |
| Gurajada Apparao | గురజాడ అప్పారావు | 0/0 | narrow;no_source |
| Women's reform | మహిళా సంస్కరణ | 0/0 | overlap;no_source |
| Modern Telugu cultural awakening | ఆధునిక తెలుగు సాంస్కృతిక చైతన్యం | 0/1 |  |
| Important associations and institutions | ముఖ్య సంఘాలు మరియు సంస్థలు | 0/0 | no_source |

#### Chapter 18 — Justice Party and Self-Respect Movement (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Origins of the Non-Brahmin movement | బ్రాహ్మణేతర ఉద్యమ మూలాలు | 0/0 | no_source |
| Justice Party | జస్టిస్ పార్టీ | 0/1 |  |
| Important leaders | ముఖ్య నాయకులు | 0/0 | overlap;no_source |
| Policies and social impact | విధానాలు మరియు సామాజిక ప్రభావం | 0/0 | no_source |
| Self-Respect Movement | ఆత్మగౌరవ ఉద్యమం | 0/0 | no_source |
| Influence in Andhra | ఆంధ్రలో ప్రభావం | 0/0 | no_source |
| Debates and limitations | చర్చలు మరియు పరిమితులు | 0/0 | no_source |

#### Chapter 19 — Nationalist Movement in Andhra, 1885–1947 (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Early political associations | తొలి రాజకీయ సంఘాలు | 0/0 | no_source |
| Indian National Congress and Andhra | భారత జాతీయ కాంగ్రెస్ మరియు ఆంధ్ర | 1/0 |  |
| Swadeshi and Vandemataram | స్వదేశీ మరియు వందేమాతర ఉద్యమాలు | 0/1 |  |
| Home Rule | స్వపరిపాలన (హోమ్ రూల్) ఉద్యమం | 0/0 | no_source;telugu_review |
| Non-Cooperation | సహాయ నిరాకరణ | 1/0 |  |
| Chirala–Perala and Pedanandipadu | చీరాల–పేరాల మరియు పెదనందిపాడు | 0/0 | narrow;no_source |
| Civil Disobedience and Salt Satyagraha | శాసనోల్లంఘన మరియు ఉప్పు సత్యాగ్రహం | 1/0 |  |
| Individual Satyagraha | వ్యక్తిగత సత్యాగ్రహం | 0/0 | no_source |
| Quit India | క్విట్ ఇండియా ఉద్యమం | 1/0 |  |
| Prominent leaders | ప్రముఖ నాయకులు | 1/0 | overlap |
| Regional centres and events | ప్రాంతీయ కేంద్రాలు మరియు సంఘటనలు | 1/1 |  |

#### Chapter 20 — Socialists, Communists, Anti-Zamindari and Kisan Movements (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Socialist organisations and leaders | సోషలిస్టు సంస్థలు మరియు నాయకులు | 0/0 | no_source |
| Communist movement | కమ్యూనిస్టు ఉద్యమం | 0/2 |  |
| Peasant organisation | రైతు సంఘటన | 0/0 | no_source |
| Anti-Zamindari struggles | జమీందారీ వ్యతిరేక పోరాటాలు | 0/1 |  |
| Kisan Sabhas | కిసాన్ సభలు | 0/0 | overlap;no_source |
| N. G. Ranga | ఎన్. జి. రంగా | 0/0 | no_source |
| Labour mobilisation | కార్మిక సమీకరణ | 0/0 | no_source |
| Important regional agrarian struggles | ముఖ్య ప్రాంతీయ రైతాంగ పోరాటాలు | 0/1 | overlap |
| Relationship with the national movement | జాతీయోద్యమంతో సంబంధం | 0/0 | no_source |

#### Chapter 21 — Nationalist Poetry, Revolutionary Literature and Nataka Samasthalu (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Nationalist poetry | జాతీయ కవిత్వం | 0/1 |  |
| Revolutionary writings | విప్లవ రచనలు | 0/0 | no_source |
| Important poets and authors | ముఖ్య కవులు మరియు రచయితలు | 0/0 | no_source |
| Newspapers and literary publications | వార్తాపత్రికలు మరియు సాహిత్య ప్రచురణలు | 0/0 | no_source |
| Drama organisations | నాటక సంస్థలు | 0/0 | duplicate;overlap;no_source |
| Nataka Samasthalu | నాటక సమాజాలు | 0/1 | duplicate;overlap |
| Praja Natya Mandali | ప్రజా నాట్య మండలి | 0/0 | narrow;no_source |
| Maa Bhoomi | మా భూమి | 0/0 | narrow;no_source |
| Folk performance in political mobilisation | రాజకీయ చైతన్యంలో జానపద ప్రదర్శనలు | 0/0 | no_source |

#### Chapter 22 — Women's Participation (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Women social reformers | మహిళా సంఘ సంస్కర్తలు | 0/0 | overlap;no_source |
| Women in Swadeshi and Home Rule | స్వదేశీ మరియు హోమ్ రూల్ ఉద్యమాల్లో మహిళలు | 0/0 | overlap;no_source |
| Women in Gandhian movements | గాంధేయ ఉద్యమాల్లో మహిళలు | 0/0 | overlap;no_source |
| Women in revolutionary and peasant movements | విప్లవ మరియు రైతాంగ ఉద్యమాల్లో మహిళలు | 0/0 | no_source |
| Organisations | సంస్థలు | 0/0 | no_source |
| Prominent women | ప్రముఖ మహిళలు | 0/0 | no_source |
| Regional events | ప్రాంతీయ సంఘటనలు | 0/0 | no_source |
| Social consequences | సామాజిక పరిణామాలు | 0/0 | no_source |

### Unit 4

#### Chapter 23 — Origin and Growth of the Andhra Movement (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Roots of linguistic identity | భాషా గుర్తింపు మూలాలు | 0/1 |  |
| Demand for a separate Andhra province | ప్రత్యేక ఆంధ్ర ప్రాంతం కోసం డిమాండ్ | 1/0 |  |
| Early organisations | తొలి సంస్థలు | 0/0 | no_source |
| Important conferences | ముఖ్య సభలు | 0/1 | overlap |
| Andhra Provincial Congress | ఆంధ్ర ప్రాంతీయ కాంగ్రెస్ | 0/0 | no_source |
| Andhra University | ఆంధ్ర విశ్వవిద్యాలయం | 0/0 | no_source |
| Major resolutions | ముఖ్య తీర్మానాలు | 0/0 | duplicate;overlap;no_source |
| Sri Bagh Pact | శ్రీబాగ్ ఒడంబడిక | 1/1 | telugu_review |
| Political and cultural dimensions | రాజకీయ మరియు సాంస్కృతిక కోణాలు | 0/1 |  |

#### Chapter 24 — Andhra Mahasabhas and Prominent Leaders (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Origin and sessions of the Andhra Mahasabhas | ఆంధ్ర మహాసభల ఆవిర్భావం మరియు సమావేశాలు | 1/0 | overlap |
| Resolutions | తీర్మానాలు | 0/0 | duplicate;overlap;no_source |
| Organisational development | సంస్థాగత అభివృద్ధి | 0/0 | no_source |
| Major leaders | ప్రముఖ నాయకులు | 0/1 |  |
| Ideological differences | సైద్ధాంతిక భేదాలు | 0/0 | no_source |
| Contribution to state formation | రాష్ట్ర ఏర్పాటుకు తోడ్పాటు | 0/0 | no_source |

#### Chapter 25 — Press, Newspapers and the Library Movement (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Krishna Patrika | కృష్ణా పత్రిక | 0/0 | narrow;no_source |
| Andhra Patrika | ఆంధ్ర పత్రిక | 0/0 | narrow;no_source |
| Other newspapers | ఇతర పత్రికలు | 0/0 | no_source |
| Journalists and editors | పాత్రికేయులు మరియు సంపాదకులు | 0/0 | no_source |
| Press and political mobilisation | పత్రికలు మరియు రాజకీయ చైతన్యం | 0/2 |  |
| Library Movement | గ్రంథాలయోద్యమం | 0/1 |  |
| Ayyanki Venkata Ramanayya | అయ్యంకి వెంకటరమణయ్య | 0/0 | narrow;no_source |
| Andhra Desa Library Association | ఆంధ్ర దేశ గ్రంథాలయ సంఘం | 0/0 | overlap;no_source |
| Language and literary organisations | భాషా మరియు సాహిత్య సంస్థలు | 0/0 | no_source |
| Libraries as centres of public awakening | ప్రజా చైతన్య కేంద్రాలుగా గ్రంథాలయాలు | 0/0 | duplicate;overlap;no_source |

#### Chapter 26 — Folk and Tribal Culture (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Folk traditions of Andhra | ఆంధ్ర జానపద సంప్రదాయాలు | 0/1 | overlap |
| Harikatha | హరికథ | 0/0 | narrow;no_source |
| Burrakatha | బుర్రకథ | 0/0 | narrow;no_source |
| Tholu Bommalata | తోలుబొమ్మలాట | 0/0 | narrow;no_source |
| Regional dance and performance traditions | ప్రాంతీయ నృత్య మరియు ప్రదర్శన సంప్రదాయాలు | 0/0 | no_source |
| Major tribal communities | ప్రధాన గిరిజన తెగలు | 0/1 |  |
| Tribal customs and festivals | గిరిజన ఆచారాలు మరియు పండుగలు | 0/0 | no_source |
| Tribal resistance (where directly relevant) | గిరిజన ప్రతిఘటన (నేరుగా సంబంధించిన చోట) | 1/2 |  |
| Role in social identity and mobilisation | సామాజిక గుర్తింపు మరియు చైతన్యంలో పాత్ర | 0/0 | no_source |

#### Chapter 27 — Formation of Andhra State, 1953 (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Constitutional and political background | రాజ్యాంగ మరియు రాజకీయ నేపథ్యం | 0/0 | no_source |
| Dhar Commission | ధార్ కమిషన్ | 0/0 | no_source;telugu_review |
| JVP Committee | జె.వి.పి. కమిటీ | 0/0 | no_source;telugu_review |
| Swami Sitaram | స్వామి సీతారాం | 0/0 | narrow;no_source |
| Potti Sriramulu | పొట్టి శ్రీరాములు | 0/1 | duplicate;overlap |
| Madras question | మద్రాసు సమస్య | 0/0 | no_source |
| Potti Sriramulu's fast and death | పొట్టి శ్రీరాములు నిరాహార దీక్ష మరియు మరణం | 1/0 | duplicate;overlap |
| Public response | ప్రజా స్పందన | 0/0 | no_source |
| Formation of Andhra State | ఆంధ్ర రాష్ట్ర ఏర్పాటు | 2/0 |  |
| Kurnool as capital | కర్నూలు రాజధానిగా | 0/1 |  |
| Tanguturi Prakasam | టంగుటూరి ప్రకాశం | 1/0 | narrow;note_driven |
| Consequences | పరిణామాలు | 0/1 |  |

### Unit 5

#### Chapter 28 — Visalandhra Movement and Visalandhra Mahasabha (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Visalandhra idea | విశాలాంధ్ర భావన | 0/0 | no_source |
| Linguistic and political arguments | భాషా మరియు రాజకీయ వాదనలు | 0/1 | overlap |
| Visalandhra Mahasabha | విశాలాంధ్ర మహాసభ | 0/1 |  |
| Prominent supporters and opponents | ప్రముఖ మద్దతుదారులు మరియు వ్యతిరేకులు | 0/1 |  |
| Andhra–Telangana merger debate | ఆంధ్ర–తెలంగాణ విలీన చర్చ | 2/0 | overlap |
| Important meetings and resolutions | ముఖ్య సమావేశాలు మరియు తీర్మానాలు | 0/0 | no_source |

#### Chapter 29 — States Reorganisation Commission (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Formation and members | ఏర్పాటు మరియు సభ్యులు | 1/0 |  |
| Terms of reference | విధివిధానాలు (నిబంధనలు) | 0/1 |  |
| Andhra and Telangana evidence | ఆంధ్ర మరియు తెలంగాణ సాక్ష్యాలు | 0/0 | no_source |
| Recommendations | సిఫారసులు | 1/0 |  |
| Arguments for a separate Telangana | ప్రత్యేక తెలంగాణ కోసం వాదనలు | 0/0 | overlap;no_source |
| Conditions suggested for merger | విలీనానికి సూచించిన షరతులు | 0/0 | overlap;no_source |
| Political responses | రాజకీయ స్పందనలు | 0/0 | no_source |

#### Chapter 30 — Gentlemen's Agreement and Formation of Andhra Pradesh (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Negotiations | చర్చలు | 0/1 | overlap |
| Signatories | సంతకందారులు | 0/1 | overlap;narrow |
| Provisions | ఒప్పంద నిబంధనలు | 1/0 | overlap |
| Regional safeguards | ప్రాంతీయ రక్షణలు | 1/2 | overlap |
| Merger process | విలీన ప్రక్రియ | 0/0 | overlap;no_source |
| Formation on 1 November 1956 | 1956 నవంబరు 1న ఏర్పాటు | 1/0 |  |
| Hyderabad as capital | హైదరాబాద్ రాజధానిగా | 0/0 | no_source |
| Implementation issues | అమలులో సమస్యలు | 0/1 |  |
| Long-term significance | దీర్ఘకాలిక ప్రాధాన్యం | 0/1 |  |

#### Chapter 31 — Important Social and Cultural Events, 1956–2014 (direct)

| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |
|---|---|---|---|
| Official language and Telugu development | అధికార భాష మరియు తెలుగు అభివృద్ధి | 0/1 | overlap |
| Education and universities | విద్య మరియు విశ్వవిద్యాలయాలు | 0/1 |  |
| Literature | సాహిత్యం | 0/1 |  |
| Theatre | రంగస్థలం | 0/0 | overlap;no_source |
| Cinema | సినిమా | 0/1 |  |
| Visual and performing arts | చిత్ర మరియు ప్రదర్శన కళలు | 0/0 | no_source |
| Cultural institutions | సాంస్కృతిక సంస్థలు | 0/0 | no_source |
| Dalit and social movements | దళిత మరియు సామాజిక ఉద్యమాలు | 0/1 |  |
| Women's movements | మహిళా ఉద్యమాలు | 0/0 | overlap;no_source |
| Civil-society movements | పౌర సమాజ ఉద్యమాలు | 0/0 | no_source |
| Telangana movement of 1969 | 1969 తెలంగాణ ఉద్యమం | 1/1 | overlap |
| Jai Andhra Movement of 1972 | 1972 జై ఆంధ్ర ఉద్యమం | 1/1 | overlap |
| Regional identity movements | ప్రాంతీయ గుర్తింపు ఉద్యమాలు | 3/1 | overlap |
| Major cultural developments up to 2014 | 2014 వరకు ముఖ్య సాంస్కృతిక పరిణామాలు | 1/0 | overlap;note_driven |

