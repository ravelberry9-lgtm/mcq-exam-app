# AP History note-section mapping — DRAFT for review

A proposal only: nothing in any database was changed, and no note was rewritten or split. Source chapter and section numbers are kept in the CSV. For chapters 1-12 the ids come from the bundled content database (they differ per environment, so a future import keys on source chapter number + section number). Chapters 13-19 exist only as local HTML files; their section structure is snapshotted in `scripts/ap_source_sections_13_19.json` with file hashes.

- Sections mapped: **338** (chapters 1-12: 225, from the app database; chapters 13-19: 113, from local HTML)
- Confidence: high 237, medium 94, low 7
- Flagged for review: 106; multi-topic sections: 48; scope-boundary: 16; ambiguous: 19; content-review: 2; unapproved: 1
- Mapped at chapter level (no subtopic): 143

Rules used: one primary chapter and subtopic per section; multi-topic sections keep secondary links and a `multi_topic` flag and are not split; a shared place name is not a cross-topic link; the supplementary reference chapters are outside the 31 core chapters.

## Where each source chapter went

- Source 1 — Prehistoric Cultures of AP: `u1-c02-prehistoric-cultures` (17)
- Source 2 — Introduction to Andhras & Sources: `u1-c01-region-people-sources` (17)
- Source 3 — Pre-Satavahana Andhra: `u1-c03-pre-satavahana-andhra` (17)
- Source 4 — Overview of Andhra Dynasties: `supp-dynasties-overview` (12)
- Source 5 — Satavahana Dynasty: `u1-c04-satavahanas` (19)
- Source 6 — Ikshvakus: `u1-c05-ikshvakus` (21)
- Source 7 — Minor Dynasties of AP: `u1-c06-post-ikshvaku-minor-dynasties` (17)
- Source 8 — Vishnukundin Dynasty: `u1-c07-vishnukundins` (21)
- Source 9 — Eastern Chalukyas: `u1-c08-eastern-chalukyas-andhra-cholas` (21)
- Source 10 — Kakatiyas: `u2-c09-kakatiyas` (21)
- Source 11 — Reddy Kingdoms & Musunuri Nayakas: `u2-c10-musunuri-reddy-velama` (21)
- Source 12 — Vijayanagara Empire: `u2-c11-vijayanagara-andhra` (21)
- Source 13 — అధ్యాయం 13 — కుతుబ్‌ షాహీ రాజవంశం: `u2-c13-qutb-shahis` (16)
- Source 14 — అధ్యాయం 14 — ఆసఫ్‌ జాహీ నిజాములు: `supp-asaf-jahis-hyderabad-state` (16)
- Source 15 — అధ్యాయం 15 — తీరాంధ్రలో బ్రిటిష్ పాలన: `u3-c15-europeans-company-rule` (4), `u3-c16-british-rule-revolt-1857` (10), `u3-c17-socio-cultural-awakening` (1)
- Source 16 — అధ్యాయం 16 — ఆంధ్ర స్వాతంత్ర్యోద్యమం: `u3-c17-socio-cultural-awakening` (1), `u3-c19-nationalist-movement-1885-1947` (9), `u4-c23-andhra-movement-origin-growth` (2), `u4-c24-andhra-mahasabhas-leaders` (1), `u4-c26-folk-tribal-culture` (1), `u4-c27-formation-andhra-state-1953` (2)
- Source 17 — అధ్యాయం 17 — ఆంధ్ర రాష్ట్రం + ఆంధ్రప్రదేశ్ ఏర్పాటు: `u4-c25-press-library-movement` (1), `u4-c27-formation-andhra-state-1953` (2), `u5-c28-visalandhra-movement-mahasabha` (2), `u5-c29-states-reorganisation-commission` (2), `u5-c30-gentlemens-agreement-formation-ap` (9)
- Source 18 — అధ్యాయం 18 — ఆధునిక ఆంధ్రప్రదేశ్: `u5-c31-social-cultural-events-1956-2014` (18)
- Source 19 — అధ్యాయం 19 — బిఫర్కేషన్ + వర్తమాన ఆంధ్రప్రదేశ్: `supp-post-2014-andhra-pradesh` (16)

## Flagged sections

| Src ch | Sec | Heading | Proposed | Conf | Flags | Why |
|---|---|---|---|---|---|---|
| 1 | 4 | The Movius Line | u1-c02-tools-technology | medium |  | Movius Line contrasts Acheulian handaxe and chopper-chopping-tool traditions (technology); also a Palaeolithic topic. |
| 1 | 5 | Evidence Types & Pioneer Researchers | u1-c02-prehistoric-cultures | low | ambiguous;content_review | Mixes evidence types with pioneer researchers; no single subtopic fits. Ambiguous. |
| 1 | 13 | Key Researchers | u1-c02-prehistoric-cultures | medium |  | Researchers of AP prehistory; no researcher subtopic exists. |
| 1 | 14 | Recent Excavations & Discoveries, 2007–2 | u1-c02-prehistoric-cultures | medium | multi_topic | Recent discoveries across several periods (e.g. Jwalapuram/Toba); multi-period, so chapter level. |
| 2 | 9 | Monuments & Sculpture | u1-c01-archaeological-evidence | medium |  | Monuments and sculpture as physical evidence. |
| 2 | 11 | Earliest References to Andhras — Chronol | u1-c01-people-name-origin | medium | ambiguous | Chronological list of earliest references to Andhras; overlaps Chapter 3 'Early Andhra references'. Ambiguous. |
| 2 | 13 | Pre-Aryan Tribal Background of the Andhr | u1-c01-people-name-origin | low | ambiguous;content_review | Pre-Aryan tribal background (Andhra, Pundra, Shabara); ancient ethnography, not Chapter 26's modern tribal culture. Ambiguous. |
| 2 | 15 | Recent Excavations & Discoveries, 2018–2 | u1-c01-archaeological-evidence | medium |  | Recent excavations and discoveries 2018-2026. |
| 3 | 5 | Sources for Pre-Satavahana Andhra | u1-c03-pre-satavahana-andhra | medium |  | Sources for the period; overlaps Chapter 1 sources. |
| 3 | 7 | Mulaka Kingdom | u1-c03-assaka-asmaka | medium | ambiguous | Mulaka is paired with Assaka in the sources; no separate subtopic. Propose adding one. Ambiguous. |
| 3 | 9 | Megasthenes' Indica on Andhras | u1-c03-early-andhra-references | medium |  | Megasthenes' Indica on the Andhras; also a foreign account. |
| 3 | 11 | Post-Mauryan Transition · క్రీ.పూ. 232–2 | u1-c03-early-local-rulers | medium |  | Post-Mauryan transition, c. 232-200 BCE. |
| 3 | 13 | Society, Economy, Religion | u1-c03-pre-satavahana-andhra | medium | multi_topic | Society, economy and religion together; no matching subtopic. |
| 3 | 15 | Key Historical Figures & Researchers | u1-c03-pre-satavahana-andhra | medium |  | Historical figures and researchers. |
| 4 | 8 | Religious Patronage by Dynasty | supp-dynasties-overview | medium |  | Religious patronage by dynasty across all periods; only part falls in 11th-16th c. |
| 4 | 9 | Telugu Literature Growth Timeline | supp-dynasties-overview | medium |  | Telugu literature growth timeline across periods. |
| 4 | 11 | Key Inscriptions Reference | supp-dynasties-overview | medium |  | Key inscriptions reference across dynasties. |
| 5 | 5 | The Capital Debate | u1-c04-political-history | medium | ambiguous | The capital debate (Pratishthana / Dhanyakataka); no capital subtopic. Ambiguous. |
| 5 | 6 | Sources of Satavahana History | u1-c04-satavahanas | medium |  | Sources of Satavahana history (literary, inscriptions, coins). |
| 5 | 13 | Society + Economy | u1-c04-society | medium | ambiguous;multi_topic | Society and economy in one section; should be split at content level. Ambiguous. |
| 5 | 15 | Art + Literature | u1-c04-art-architecture | medium | ambiguous;multi_topic | Art and literature in one section; should be split. Ambiguous. |
| 5 | 17 | Key Historical Figures & Researchers | u1-c04-satavahanas | medium |  | Key figures and researchers. |
| 6 | 5 | Historical Sources | u1-c05-ikshvakus | medium |  | Historical sources of the Ikshvakus. |
| 6 | 15 | Religion — The Dual Structure | u1-c05-buddhism | medium | ambiguous;multi_topic | Dual Buddhist/Brahmanical religious structure in one section. Ambiguous. |
| 6 | 17 | The Great Stupa | u1-c05-art-architecture | medium |  | The Great Stupa (Mahachaitya) at Nagarjunakonda. |
| 7 | 6 | Chejarla Kapoteshvara — Apsidal Temple | u1-c06-art-architecture | medium |  | Chejarla Kapoteshvara apsidal temple, discussed under the Ananda Gotra. |
| 7 | 10 | Vengi / Pedavegi — 700-Year Capital | u1-c06-salankayanas | medium |  | Vengi (Pedavegi) as Salankayana capital: the primary topic. The secondary Chapter 8 link is kept only because section 10.2 itself discusses the later Eastern Chalukya period (a table of Vengi's c. 624-1130 CE role); the shared place name alone would not justif |
| 7 | 12 | Bull Seal + Tutelary Vishnu | u1-c06-religion | medium | multi_topic | Bull seal and tutelary deity Chitrarathasvamin; religion and emblem together. |
| 7 | 13 | Prakrit → Sanskrit Transition | u1-c06-inscriptions | medium |  | Prakrit-to-Sanskrit language shift traced through copper plates. |
| 7 | 16 | Bridge to Vishnukundins | u1-c06-political-conditions | medium |  | Bridge to the Vishnukundins: fate of each dynasty. |
| 8 | 4 | Four Capitals — older textbooks cite onl | u1-c07-political-expansion | medium | ambiguous | Four capitals; no capitals subtopic. Ambiguous. |
| 8 | 5 | Historical Sources | u1-c07-vishnukundins | medium |  | Historical sources. |
| 8 | 9 | Madhava-Vakataka Marriage Alliance | u1-c07-political-expansion | medium |  | Vakataka marriage alliance. |
| 8 | 20 | Bridge to Eastern Chalukyas | u1-c07-decline | medium |  | Bridge to the Eastern Chalukyas. |
| 9 | 4 | Three Capitals | u1-c08-vengi-foundation | medium |  | Three capitals; no capitals subtopic. |
| 9 | 5 | Historical Sources | u1-c08-eastern-chalukyas-andhra-cholas | medium |  | Historical sources. |
| 9 | 17 | Religion & Administration | u1-c08-religion | medium | ambiguous;multi_topic | Religion and administration in one section. Ambiguous. |
| 10 | 4 | The Three Capitals | u2-c09-political-expansion | medium |  | Three capitals; no capitals subtopic. |
| 10 | 5 | Historical Sources | u2-c09-kakatiyas | medium |  | Historical sources. |
| 10 | 15 | Literature & Arts — The Second Wave of T | u2-c09-telugu-literature | medium | ambiguous;multi_topic | Literature and arts together. Ambiguous. |
| 10 | 18 | Religion & Social History | u2-c09-religion | medium | ambiguous;multi_topic | Religion and social history together. Ambiguous. |
| 11 | 5 | Historical Sources | u2-c10-musunuri-reddy-velama | medium |  | Historical sources. |
| 11 | 12 | Kataya Vema + Vira Bhadra Reddi — Last K | u2-c10-rajahmundry-reddys | medium | attribution_check ; UNAPPROVED | Provisionally placed under Rajahmundry Reddys (the section title's placement). UNAPPROVED: Kataya Vema attribution unresolved. The section heading calls Kataya Vema and Vira Bhadra the *last* kings of Rajamahendravaram, but the body (12.1) calls Kataya Vema th |
| 11 | 17 | Administration and Economy | u2-c10-administration | medium | ambiguous;multi_topic | Administration and economy together. Ambiguous. |
| 11 | 18 | Religion and Social History | u2-c10-religion | medium | ambiguous;multi_topic | Religion and social history together. Ambiguous. |
| 11 | 20 | Decline — Vijayanagara & Gajapati Conque | u2-c10-regional-conflicts | medium |  | Decline through Vijayanagara and Gajapati conquests. |
| 12 | 5 | Historical Sources | u2-c11-vijayanagara-andhra | medium |  | Historical sources. |
| 12 | 6 | The Sangama Dynasty, 1336–1485 | u2-c11-four-dynasties | medium |  | The Sangama dynasty. |
| 12 | 14 | Aravidu Dynasty + AP-located Capitals, 1 | u2-c11-decline | medium |  | Aravidu dynasty and AP-located capitals after 1565. |
| 12 | 16 | Administration + Economy | u2-c11-administration-nayankara | medium | ambiguous;multi_topic | Administration and economy together. Ambiguous. |
| 12 | 18 | Literature + Arts | u2-c11-telugu-literature-ashtadiggajas | medium | ambiguous;multi_topic | Literature and arts together. Ambiguous. |
| 13 | 3 | Historical Background + Founding | u2-c13-establishment | medium | multi_topic | Bahmani background, the five Deccan sultanates, Golconda fort and Sultan Quli's founding in one long section. |
| 13 | 4 | Dynasty — Seven Sultans | u2-c13-sixteenth-century-rulers | medium | scope_boundary | Lists all eight Qutb Shahi rulers, 1518-1687; only the first reigns fall in the 16th century. |
| 13 | 6 | Muhammad Quli Qutb Shah | u2-c13-sixteenth-century-rulers | medium | multi_topic;scope_boundary | Muhammad Quli (1580-1612): founding of Hyderabad (1591), poetry, administration; the reign runs past 1600. |
| 13 | 8 | Hyderabad City Planning | u2-c13-art-architecture | medium |  | Planning of Hyderabad city (1591). |
| 13 | 9 | Mecca Masjid + Other Monuments | u2-c13-art-architecture | medium | scope_boundary | Mecca Masjid (completed well after the 16th century) and other monuments; supporting context. |
| 13 | 10 | Qutb Shahi Tombs | u2-c13-art-architecture | medium | scope_boundary | Qutb Shahi tombs, mostly 17th-century construction; supporting context. |
| 13 | 11 | Administration + Economy | u2-c13-administration | medium | multi_topic | Central and provincial administration, economy, Golconda diamonds and merchant guilds in one section. |
| 13 | 12 | Religion + Society | u2-c13-religion | high | scope_boundary | Religious tolerance; the Hindu ministers Akkanna and Madanna (17th century) and their murder; Hindu-Muslim harmony. |
| 13 | 14 | Decline + Mughal Annexation | u2-c13-qutb-shahis | medium | scope_boundary | Decline and Mughal annexation, 1636-1687: after the official 11th-16th century boundary; supporting context. |
| 13 | 15 | Legacy + AP Sites | u2-c13-qutb-shahis | medium | scope_boundary | Legacy and AP sites table; mostly 17th-century context. |
| 15 | 1 | Introduction | u3-c16-british-rule-revolt-1857 | medium | multi_topic | Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 15 | 2 | Glossary | u3-c16-british-rule-revolt-1857 | medium | multi_topic | Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 15 | 3 | Historical Background | u3-c15-trading-centres-ports | medium | multi_topic | Late Mughal decline 1687-1740, European settlements on the Andhra coast, and why the British won. |
| 15 | 7 | Madras Presidency Administration | u3-c16-consolidation-of-administration | medium |  | Madras Presidency: its formation, administrative order to 1858 and Andhra districts by 1857. |
| 15 | 8 | Thomas Munro and the Ryotwari System | u3-c16-thomas-munro | medium | multi_topic | Munro's career and the ryotwari system in one section. |
| 15 | 10 | Vizianagaram and Local Zamindars | u3-c16-zamindari-ryotwari | medium | multi_topic | Vizianagaram Pusapati line, Bobbili (1757), Padmanabham (1794), other zamindaris. |
| 15 | 11 | 1857 Revolt + Tribal Uprisings | u3-c16-impact-of-1857 | medium | multi_topic | 1857 in Madras Presidency (limited impact), the 1879 Rampa rebellion and other minor uprisings. |
| 15 | 12 | Education & Social Change | u3-c17-western-education | medium | multi_topic | English education, social reform movements and print/Telugu renaissance in one section. |
| 15 | 13 | Economic Changes | u3-c16-administrative-economic-effects | medium | multi_topic | Agriculture, trade, railways and the 1876-78 famine. |
| 15 | 14 | Key Sites | u3-c16-british-rule-revolt-1857 | medium | multi_topic | Key sites table spanning the source chapter. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 15 | 15 | Revision | u3-c16-british-rule-revolt-1857 | medium | multi_topic | Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 16 | 1 | Introduction | u3-c19-nationalist-movement-1885-1947 | medium | multi_topic | Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 16 | 2 | Glossary | u3-c19-nationalist-movement-1885-1947 | medium | multi_topic | Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 16 | 3 | Early Phase | u3-c19-congress-and-andhra | medium | multi_topic | Founding of the INC (1885), partition of Bengal (1905) and the Andhra response, Surat split (1907). |
| 16 | 4 | Andhra Movement | u4-c23-demand-for-andhra-province | medium | multi_topic | Andhra Movement from 1913: Tamil dominance in administration and jobs and the push for a separate province. |
| 16 | 6 | Rampa Rebellion | u3-c19-regional-centres-events | medium | ambiguous | Alluri Sitarama Raju and the Rampa rebellion 1922-24: an armed tribal revolt in the nationalist era that equally fits Chapter 26 'tribal resistance'. Ambiguous. |
| 16 | 8 | Simon Commission & Salt Satyagraha | u3-c19-civil-disobedience-salt-satyagraha | high | multi_topic | Simon Commission protest, Prakasam, Salt Satyagraha (1930), Gandhi-Irwin Pact. |
| 16 | 11 | Telangana Movement & Komaram Bheem | u4-c26-tribal-resistance | medium | ambiguous;multi_topic | Komaram Bheem's Gond armed movement (1928-40, Jodeghat) and other Telangana freedom leaders; also regional nationalist history. Ambiguous. |
| 16 | 12 | Key Leaders — Comprehensive | u3-c19-prominent-leaders | medium |  | Comprehensive list of freedom-movement leaders. |
| 16 | 15 | Socio-cultural & Ideological Currents | u3-c17-socio-cultural-awakening | medium | multi_topic | Umbrella section on socio-cultural and ideological currents with seven subsections: Justice Party/Self-Respect, left and Communist movements, anti-zamindari and Kisan movements, poetry and revolutionary literature, Nataka Samasthalu, women, reform and press. |
| 16 | 16 | Revision | u3-c19-nationalist-movement-1885-1947 | medium | multi_topic | Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 17 | 1 | Introduction | u5-c30-gentlemens-agreement-formation-ap | medium | multi_topic | Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 17 | 2 | Glossary | u5-c30-gentlemens-agreement-formation-ap | medium | multi_topic | Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 17 | 3 | Hyderabad State Era | u5-c28-andhra-telangana-merger-debate | low | ambiguous;multi_topic | Hyderabad State 1948-56 (military governor, Vellodi, Burgula, the 1952 election and Mulki agitation): background to the Telangana merger question. Ambiguous. |
| 17 | 4 | Andhra State Formation | u4-c27-formation-of-andhra-state | high | multi_topic | Andhra State: context, formation, Bellary dispute, Sri Bagh Pact and the choice of Kurnool. |
| 17 | 5 | Andhra State CMs | u4-c27-tanguturi-prakasam | medium | multi_topic | Prakasam and B. Gopala Reddy as Andhra State chief ministers. |
| 17 | 8 | Vishalandhra Debate | u5-c28-andhra-telangana-merger-debate | medium | multi_topic | Visalandhra Mahasabha and idea, Andhra-side arguments, Telangana-side opposition, leaders' views. |
| 17 | 9 | Gentlemen's Agreement | u5-c30-provisions | high | multi_topic | Gentlemen's Agreement: context, eight signatories, fourteen points and significance. |
| 17 | 11 | Mulki Rules | u5-c30-regional-safeguards | medium |  | Mulki rules: origin, continuation under the Gentlemen's Agreement, Supreme Court rulings. |
| 17 | 12 | Cultural Foundations of the Andhra Movem | u4-c25-press-library-movement | medium | multi_topic | Press, Library Movement, folk arts and tribal culture as the cultural base of the Andhra Movement (four subsections). |
| 17 | 13 | Key Figures | u5-c30-gentlemens-agreement-formation-ap | medium | multi_topic | Key figures of 1948-56 across the source chapter. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 17 | 14 | Key Sites | u5-c30-gentlemens-agreement-formation-ap | medium | multi_topic | Key sites across the source chapter. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 17 | 15 | SVG Timeline | u5-c30-gentlemens-agreement-formation-ap | medium | multi_topic | Timeline graphic for 1948-56. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 17 | 16 | Revision | u5-c30-gentlemens-agreement-formation-ap | medium | multi_topic | Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 18 | 3 | Early INC Era | u5-c31-social-cultural-events-1956-2014 | medium | scope_boundary | Chief ministers 1956-83 (Sanjiva Reddy to Brahmananda Reddy): political history; includes implementation of the Gentlemen's Agreement. |
| 18 | 6 | Six-Point Formula | u5-c31-regional-identity-movements | medium | multi_topic | Six-Point Formula (1973), Article 371-D and G.O. 610: the settlement of the 1969-73 agitations. |
| 18 | 7 | Late INC Era | u5-c31-social-cultural-events-1956-2014 | medium | scope_boundary | Chief ministers 1973-82; political history. |
| 18 | 8 | NTR & TDP Revolution | u5-c31-social-cultural-events-1956-2014 | low | scope_boundary | NTR and the TDP, 1982-83: political history, outside the syllabus's 'social and cultural' scope. |
| 18 | 9 | NTR's Three Terms | u5-c31-social-cultural-events-1956-2014 | low | scope_boundary | NTR's three terms: political history, outside the syllabus's 'social and cultural' scope. |
| 18 | 10 | Naidu's IT Era | u5-c31-social-cultural-events-1956-2014 | low | scope_boundary | Naidu's IT era, 1995-2004: governance history, outside the syllabus's 'social and cultural' scope. |
| 18 | 11 | YSR Welfare Era | u5-c31-social-cultural-events-1956-2014 | low | scope_boundary | YSR welfare era, 2004-09: governance history, outside the syllabus's 'social and cultural' scope. |
| 18 | 13 | 2014 Bifurcation Overview | u5-c31-regional-identity-movements | medium | scope_boundary | 2014 bifurcation overview: sits on the boundary of the syllabus. |
| 18 | 14 | Social & Cultural Developments | u5-c31-cultural-developments-to-2014 | high | multi_topic | Literature, cinema and press, social and Dalit movements, Naxalite movement, education, language and cultural identity. |
| 18 | 15 | Major Projects | u5-c31-social-cultural-events-1956-2014 | medium | scope_boundary | Irrigation and IT projects: development history rather than social-cultural. |
| 18 | 16 | All AP CMs | u5-c31-social-cultural-events-1956-2014 | medium | scope_boundary | Reference table of chief ministers, 1956-2014. |

## Canonical subtopics with no note section (primary or secondary)

- Chapter 1 — Andhra Region, People and Historical Sources: 1 of 9: Geographical extent and historical meaning of Andhradesa
- Chapter 2 — Prehistoric Cultures of Andhra: 2 of 9: Chalcolithic; Pottery
- Chapter 3 — Pre-Satavahana Andhra: 2 of 11: Kharavela and the Hathigumpha inscription; Punch-marked and local coinage
- Chapter 4 — Satavahanas: 2 of 13: Administration; Decline
- Chapter 5 — Ikshvakus: 1 of 12: Literature and education
- Chapter 6 — Post-Ikshvaku Minor Dynasties: 3 of 10: Pallava influence; Other transitional dynasties; Society and economy
- Chapter 7 — Vishnukundins: 2 of 11: Administration; Society and economy
- Chapter 8 — Eastern Chalukyas of Vengi and Andhra Cholas: 3 of 15: Society and economy; Nellore Telugu Chodas; Palnadu War
- Chapter 11 — Vijayanagara and Andhra: 1 of 13: Society
- Chapter 12 — Gajapatis, Bahmanis and Other Regional Powers: 5 of 7: Coastal Andhra conflicts; Minor regional powers; Forts and political centres; Socio-cultural influence; Political transition
- Chapter 13 — Qutb Shahis and Sixteenth-Century Andhra: 1 of 9: Expansion into Andhra
- Chapter 14 — Thematic History of Andhradesa, 11th–16th Centuries: 8 of 12: Comparative administration; Social structure; Economic conditions; Agriculture and irrigation; Internal and overseas trade; Sculpture; Temple architecture; Music and dance
- Chapter 15 — Europeans, Trading Centres and Company Rule: 4 of 11: Portuguese; Dutch; English; French
- Chapter 16 — Establishment of British Rule and the Impact of 1857: 1 of 8: Events and personalities connected to Andhra
- Chapter 17 — Socio-Cultural Awakening: 6 of 10: Missionary activity; Kandukuri Veeresalingam; Raghupati Venkataratnam Naidu; Gurajada Apparao; Women's reform; Important associations and institutions
- Chapter 18 — Justice Party and Self-Respect Movement: 6 of 7: Origins of the Non-Brahmin movement; Important leaders; Policies and social impact; Self-Respect Movement; Influence in Andhra; Debates and limitations
- Chapter 19 — Nationalist Movement in Andhra, 1885–1947: 4 of 11: Early political associations; Home Rule; Chirala–Perala and Pedanandipadu; Individual Satyagraha
- Chapter 20 — Socialists, Communists, Anti-Zamindari and Kisan Movements: 6 of 9: Socialist organisations and leaders; Peasant organisation; Kisan Sabhas; N. G. Ranga; Labour mobilisation; Relationship with the national movement
- Chapter 21 — Nationalist Poetry, Revolutionary Literature and Nataka Samasthalu: 7 of 9: Revolutionary writings; Important poets and authors; Newspapers and literary publications; Drama organisations; Praja Natya Mandali; Maa Bhoomi; Folk performance in political mobilisation
- Chapter 22 — Women's Participation: 8 of 8: Women social reformers; Women in Swadeshi and Home Rule; Women in Gandhian movements; Women in revolutionary and peasant movements; Organisations; Prominent women; Regional events; Social consequences
- Chapter 23 — Origin and Growth of the Andhra Movement: 4 of 9: Early organisations; Andhra Provincial Congress; Andhra University; Major resolutions
- Chapter 24 — Andhra Mahasabhas and Prominent Leaders: 4 of 6: Resolutions; Organisational development; Ideological differences; Contribution to state formation
- Chapter 25 — Press, Newspapers and the Library Movement: 8 of 10: Krishna Patrika; Andhra Patrika; Other newspapers; Journalists and editors; Ayyanki Venkata Ramanayya; Andhra Desa Library Association; Language and literary organisations; Libraries as centres of public awakening
- Chapter 26 — Folk and Tribal Culture: 6 of 9: Harikatha; Burrakatha; Tholu Bommalata; Regional dance and performance traditions; Tribal customs and festivals; Role in social identity and mobilisation
- Chapter 27 — Formation of Andhra State, 1953: 6 of 12: Constitutional and political background; Dhar Commission; JVP Committee; Swami Sitaram; Madras question; Public response
- Chapter 28 — Visalandhra Movement and Visalandhra Mahasabha: 2 of 6: Visalandhra idea; Important meetings and resolutions
- Chapter 29 — States Reorganisation Commission: 4 of 7: Andhra and Telangana evidence; Arguments for a separate Telangana; Conditions suggested for merger; Political responses
- Chapter 30 — Gentlemen's Agreement and Formation of Andhra Pradesh: 2 of 9: Merger process; Hyderabad as capital
- Chapter 31 — Important Social and Cultural Events, 1956–2014: 5 of 14: Theatre; Visual and performing arts; Cultural institutions; Women's movements; Civil-society movements

## Bundle note

The review bundle is **incremental**: it contains only the commits made after base commit `e91b270a` (`release/secured-review`) and applies only on top of a repository that already has that commit. It is not a standalone or complete backup.
