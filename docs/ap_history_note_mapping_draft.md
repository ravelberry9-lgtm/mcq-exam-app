# AP History note-section mapping — DRAFT for review

A proposal only: nothing in any database was changed, and no note was rewritten or split. Source chapter and section numbers are kept in the CSV. For chapters 1-12 the ids come from the bundled content database (they differ per environment, so a future import keys on source chapter number + section number). Chapters 13-19 exist only as local HTML files; their section structure is snapshotted in `scripts/ap_source_sections_13_19.json` with file hashes.

- Sections mapped: **338** (chapters 1-12: 225, from the app database; chapters 13-19: 113, from local HTML)
- Confidence: high 237, medium 94, low 7
- Flagged for review: 106; multi-topic sections: 48; scope-boundary: 16; ambiguous: 17; content-review: 2; unapproved: 1
- Mapped at chapter level (no subtopic): 144
- Coverage scope: direct 223, mixed 7, study_aid 61, supplementary 37, supplementary_context 10
- cross_unit_context: 1; supplementary_cross_context: 1

Subtopics shown are the **rationalized** learner-facing subtopics (see `ap_history_subtopic_taxonomy_proposed.md`); the old 314-item draft slug is kept in `draft_subtopic_slug` and every draft item is now a microtopic (`proposed_microtopic_slug`). Nothing is seeded.

Scope rules: Seventeenth-century rulers, Akkanna-Madanna, later monuments, Mughal annexation and the 1687 decline are supporting context. Questions on post-1600 events carry the tag supplementary_context unless needed to explain a development that began in the sixteenth century. Routine lists of chief ministers, ordinary elections, cabinet changes, party succession and administrative events with no demonstrated social-cultural significance are supplementary_context. They stay mapped to Chapter 31 for navigation only. scope_boundary stays on every source Chapter 18 political section until each is reviewed under this rule.

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
- Source 16 — అధ్యాయం 16 — ఆంధ్ర స్వాతంత్ర్యోద్యమం: `supp-asaf-jahis-hyderabad-state` (1), `u3-c17-socio-cultural-awakening` (1), `u3-c19-nationalist-movement-1885-1947` (9), `u4-c23-andhra-movement-origin-growth` (2), `u4-c24-andhra-mahasabhas-leaders` (1), `u4-c27-formation-andhra-state-1953` (2)
- Source 17 — అధ్యాయం 17 — ఆంధ్ర రాష్ట్రం + ఆంధ్రప్రదేశ్ ఏర్పాటు: `u4-c25-press-library-movement` (1), `u4-c27-formation-andhra-state-1953` (2), `u5-c28-visalandhra-movement-mahasabha` (2), `u5-c29-states-reorganisation-commission` (2), `u5-c30-gentlemens-agreement-formation-ap` (9)
- Source 18 — అధ్యాయం 18 — ఆధునిక ఆంధ్రప్రదేశ్: `u5-c31-social-cultural-events-1956-2014` (18)
- Source 19 — అధ్యాయం 19 — బిఫర్కేషన్ + వర్తమాన ఆంధ్రప్రదేశ్: `supp-post-2014-andhra-pradesh` (16)

## Flagged sections

| Src ch | Sec | Heading | Proposed | Conf | Flags | Why |
|---|---|---|---|---|---|---|
| 1 | 4 | The Movius Line | u1-c02-tools-pottery | medium |  | Movius Line contrasts Acheulian handaxe and chopper-chopping-tool traditions (technology); also a Palaeolithic topic. |
| 1 | 5 | Evidence Types & Pioneer Researchers | u1-c02-prehistoric-cultures | low | ambiguous;content_review | Mixes evidence types with pioneer researchers; no single subtopic fits. Ambiguous. |
| 1 | 13 | Key Researchers | u1-c02-prehistoric-cultures | medium |  | Researchers of AP prehistory; no researcher subtopic exists. |
| 1 | 14 | Recent Excavations & Discoveries, 2007–2 | u1-c02-prehistoric-cultures | medium | multi_topic | Recent discoveries across several periods (e.g. Jwalapuram/Toba); multi-period, so chapter level. |
| 2 | 9 | Monuments & Sculpture | u1-c01-archaeology-sites | medium |  | Monuments and sculpture as physical evidence. |
| 2 | 11 | Earliest References to Andhras — Chronol | u1-c01-land-people-identity | medium | ambiguous | Chronological list of earliest references to Andhras; overlaps Chapter 3 'Early Andhra references'. Ambiguous. |
| 2 | 13 | Pre-Aryan Tribal Background of the Andhr | u1-c01-land-people-identity | low | ambiguous;content_review | Pre-Aryan tribal background (Andhra, Pundra, Shabara); ancient ethnography, not Chapter 26's modern tribal culture. Ambiguous. |
| 2 | 15 | Recent Excavations & Discoveries, 2018–2 | u1-c01-archaeology-sites | medium |  | Recent excavations and discoveries 2018-2026. |
| 3 | 5 | Sources for Pre-Satavahana Andhra | u1-c03-pre-satavahana-andhra | medium |  | Sources for the period; overlaps Chapter 1 sources. |
| 3 | 7 | Mulaka Kingdom | u1-c03-assaka-early-references | medium | ambiguous | Mulaka is paired with Assaka in the sources; no separate subtopic. Propose adding one. Ambiguous. |
| 3 | 9 | Megasthenes' Indica on Andhras | u1-c03-assaka-early-references | medium |  | Megasthenes' Indica on the Andhras; also a foreign account. |
| 3 | 11 | Post-Mauryan Transition · క్రీ.పూ. 232–2 | u1-c03-local-rulers-coinage | medium |  | Post-Mauryan transition, c. 232-200 BCE. |
| 3 | 13 | Society, Economy, Religion | u1-c03-pre-satavahana-andhra | medium | multi_topic | Society, economy and religion together; no matching subtopic. |
| 3 | 15 | Key Historical Figures & Researchers | u1-c03-pre-satavahana-andhra | medium |  | Historical figures and researchers. |
| 4 | 8 | Religious Patronage by Dynasty | supp-dynasties-overview | medium |  | Religious patronage by dynasty across all periods; only part falls in 11th-16th c. |
| 4 | 9 | Telugu Literature Growth Timeline | supp-dynasties-overview | medium |  | Telugu literature growth timeline across periods. |
| 4 | 11 | Key Inscriptions Reference | supp-dynasties-overview | medium |  | Key inscriptions reference across dynasties. |
| 5 | 5 | The Capital Debate | u1-c04-political-history | medium | ambiguous | The capital debate (Pratishthana / Dhanyakataka); no capital subtopic. Ambiguous. |
| 5 | 6 | Sources of Satavahana History | u1-c04-satavahanas | medium |  | Sources of Satavahana history (literary, inscriptions, coins). |
| 5 | 13 | Society + Economy | u1-c04-society-economy | medium | ambiguous;multi_topic | Society and economy in one section; should be split at content level. Ambiguous. |
| 5 | 15 | Art + Literature | u1-c04-art-architecture | medium | ambiguous;multi_topic | Art and literature in one section; should be split. Ambiguous. |
| 5 | 17 | Key Historical Figures & Researchers | u1-c04-satavahanas | medium |  | Key figures and researchers. |
| 6 | 5 | Historical Sources | u1-c05-ikshvakus | medium |  | Historical sources of the Ikshvakus. |
| 6 | 15 | Religion — The Dual Structure | u1-c05-religion | medium | ambiguous;multi_topic | Dual Buddhist/Brahmanical religious structure in one section. Ambiguous. |
| 6 | 17 | The Great Stupa | u1-c05-art-architecture | medium |  | The Great Stupa (Mahachaitya) at Nagarjunakonda. |
| 7 | 6 | Chejarla Kapoteshvara — Apsidal Temple | u1-c06-art-inscriptions | medium |  | Chejarla Kapoteshvara apsidal temple, discussed under the Ananda Gotra. |
| 7 | 10 | Vengi / Pedavegi — 700-Year Capital | u1-c06-salankayanas | medium |  | Vengi (Pedavegi) as Salankayana capital: the primary topic. The secondary Chapter 8 link is kept only because section 10.2 itself discusses the later Eastern Chalukya period (a table of Vengi's c. 624-1130 CE role); the shared place name alone would not justif |
| 7 | 12 | Bull Seal + Tutelary Vishnu | u1-c06-religion | medium | multi_topic | Bull seal and tutelary deity Chitrarathasvamin; religion and emblem together. |
| 7 | 13 | Prakrit → Sanskrit Transition | u1-c06-art-inscriptions | medium |  | Prakrit-to-Sanskrit language shift traced through copper plates. |
| 7 | 16 | Bridge to Vishnukundins | u1-c06-political-conditions | medium |  | Bridge to the Vishnukundins: fate of each dynasty. |
| 8 | 4 | Four Capitals — older textbooks cite onl | u1-c07-political-history | medium | ambiguous | Four capitals; no capitals subtopic. Ambiguous. |
| 8 | 5 | Historical Sources | u1-c07-vishnukundins | medium |  | Historical sources. |
| 8 | 9 | Madhava-Vakataka Marriage Alliance | u1-c07-political-history | medium |  | Vakataka marriage alliance. |
| 8 | 20 | Bridge to Eastern Chalukyas | u1-c07-political-history | medium |  | Bridge to the Eastern Chalukyas. |
| 9 | 4 | Three Capitals | u1-c08-vengi-foundation | medium |  | Three capitals; no capitals subtopic. |
| 9 | 5 | Historical Sources | u1-c08-eastern-chalukyas-andhra-cholas | medium |  | Historical sources. |
| 9 | 17 | Religion & Administration | u1-c08-religion | medium | ambiguous;multi_topic | Religion and administration in one section. Ambiguous. |
| 10 | 4 | The Three Capitals | u2-c09-political-history | medium |  | Three capitals; no capitals subtopic. |
| 10 | 5 | Historical Sources | u2-c09-kakatiyas | medium |  | Historical sources. |
| 10 | 15 | Literature & Arts — The Second Wave of T | u2-c09-telugu-literature | medium | ambiguous;multi_topic | Literature and arts together. Ambiguous. |
| 10 | 18 | Religion & Social History | u2-c09-religion | medium | ambiguous;multi_topic | Religion and social history together. Ambiguous. |
| 11 | 5 | Historical Sources | u2-c10-musunuri-reddy-velama | medium |  | Historical sources. |
| 11 | 12 | Kataya Vema + Vira Bhadra Reddi — Last K | u2-c10-reddy-kingdoms | medium | attribution_check ; UNAPPROVED | Provisionally placed under Rajahmundry Reddys (the section title's placement). UNAPPROVED: Kataya Vema attribution unresolved. The section heading calls Kataya Vema and Vira Bhadra the *last* kings of Rajamahendravaram, but the body (12.1) calls Kataya Vema th |
| 11 | 17 | Administration and Economy | u2-c10-administration | medium | ambiguous;multi_topic | Administration and economy together. Ambiguous. |
| 11 | 18 | Religion and Social History | u2-c10-religion | medium | ambiguous;multi_topic | Religion and social history together. Ambiguous. |
| 11 | 20 | Decline — Vijayanagara & Gajapati Conque | u2-c10-velamas-regional-conflicts | medium |  | Decline through Vijayanagara and Gajapati conquests. |
| 12 | 5 | Historical Sources | u2-c11-vijayanagara-andhra | medium |  | Historical sources. |
| 12 | 6 | The Sangama Dynasty, 1336–1485 | u2-c11-foundation-dynasties | medium |  | The Sangama dynasty. |
| 12 | 14 | Aravidu Dynasty + AP-located Capitals, 1 | u2-c11-talikota-decline | medium |  | Aravidu dynasty and AP-located capitals after 1565. |
| 12 | 16 | Administration + Economy | u2-c11-administration | medium | ambiguous;multi_topic | Administration and economy together. Ambiguous. |
| 12 | 18 | Literature + Arts | u2-c11-telugu-literature | medium | ambiguous;multi_topic | Literature and arts together. Ambiguous. |
| 13 | 3 | Historical Background + Founding | u2-c13-establishment-rulers | medium | multi_topic | Bahmani background, the five Deccan sultanates, Golconda fort and Sultan Quli's founding in one long section. |
| 13 | 4 | Dynasty — Seven Sultans | u2-c13-establishment-rulers | medium | scope_boundary | Lists all eight Qutb Shahi rulers, 1518-1687; only the first reigns fall in the 16th century. |
| 13 | 6 | Muhammad Quli Qutb Shah | u2-c13-establishment-rulers | medium | multi_topic;scope_boundary | Muhammad Quli (1580-1612): founding of Hyderabad (1591), poetry, administration; the reign runs past 1600. |
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
| 15 | 7 | Madras Presidency Administration | u3-c16-consolidation-administration | medium |  | Madras Presidency: its formation, administrative order to 1858 and Andhra districts by 1857. |
| 15 | 8 | Thomas Munro and the Ryotwari System | u3-c16-land-revenue-settlements | medium | multi_topic | Munro's career and the ryotwari system in one section. |
| 15 | 10 | Vizianagaram and Local Zamindars | u3-c16-land-revenue-settlements | medium | multi_topic | Vizianagaram Pusapati line, Bobbili (1757), Padmanabham (1794), other zamindaris. |
| 15 | 11 | 1857 Revolt + Tribal Uprisings | u3-c16-impact-1857 | medium | multi_topic | 1857 in Madras Presidency (limited impact), the 1879 Rampa rebellion and other minor uprisings. |
| 15 | 12 | Education & Social Change | u3-c17-education-missionaries | medium | multi_topic | English education, social reform movements and print/Telugu renaissance in one section. |
| 15 | 13 | Economic Changes | u3-c16-economic-effects | medium | multi_topic | Agriculture, trade, railways and the 1876-78 famine. |
| 15 | 14 | Key Sites | u3-c16-british-rule-revolt-1857 | medium | multi_topic | Key sites table spanning the source chapter. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 15 | 15 | Revision | u3-c16-british-rule-revolt-1857 | medium | multi_topic | Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 16 | 1 | Introduction | u3-c19-nationalist-movement-1885-1947 | medium | multi_topic | Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 16 | 2 | Glossary | u3-c19-nationalist-movement-1885-1947 | medium | multi_topic | Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 16 | 3 | Early Phase | u3-c19-early-associations-congress | medium | multi_topic | Founding of the INC (1885), partition of Bengal (1905) and the Andhra response, Surat split (1907). |
| 16 | 4 | Andhra Movement | u4-c23-demand-andhra-province | medium | multi_topic | Andhra Movement from 1913: Tamil dominance in administration and jobs and the push for a separate province. |
| 16 | 6 | Rampa Rebellion | u3-c19-regional-centres-events | medium | cross_unit_context | Rampa Rebellion 1922-24 (Alluri Sitarama Raju): an anti-colonial armed tribal uprising of the nationalist period, so primary is Chapter 19 (microtopic rampa-rebellion). Chapter 26 is secondary tribal context only; it is about folk and tribal culture, not a con |
| 16 | 8 | Simon Commission & Salt Satyagraha | u3-c19-civil-disobedience | high | multi_topic | Simon Commission protest, Prakasam, Salt Satyagraha (1930), Gandhi-Irwin Pact. |
| 16 | 11 | Telangana Movement & Komaram Bheem | supp-asaf-jahis-hyderabad-state | medium | multi_topic;supplementary_cross_context | Komaram Bheem (1901-40): Gond armed movement in princely Hyderabad State against Asaf Jahi administration (Jodeghat, 1940), concerning Gond land, forest and 'jal, jangal, jameen' rights; primary is the supplementary Asaf Jahi / Hyderabad State chapter. Chapter |
| 16 | 12 | Key Leaders — Comprehensive | u3-c19-prominent-leaders | medium |  | Comprehensive list of freedom-movement leaders. |
| 16 | 15 | Socio-cultural & Ideological Currents | u3-c17-socio-cultural-awakening | medium | multi_topic | Umbrella section on socio-cultural and ideological currents with seven subsections: Justice Party/Self-Respect, left and Communist movements, anti-zamindari and Kisan movements, poetry and revolutionary literature, Nataka Samasthalu, women, reform and press. |
| 16 | 16 | Revision | u3-c19-nationalist-movement-1885-1947 | medium | multi_topic | Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 17 | 1 | Introduction | u5-c30-gentlemens-agreement-formation-ap | medium | multi_topic | Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 17 | 2 | Glossary | u5-c30-gentlemens-agreement-formation-ap | medium | multi_topic | Study-aid section (introduction, glossary, revision, practice or summary) that covers the whole source chapter; mapped at chapter level. Assigned to the canonical chapter that receives most of this source chapter's sections. |
| 17 | 3 | Hyderabad State Era | u5-c28-merger-debate | low | ambiguous;multi_topic | Hyderabad State 1948-56 (military governor, Vellodi, Burgula, the 1952 election and Mulki agitation): background to the Telangana merger question. Ambiguous. |
| 17 | 4 | Andhra State Formation | u4-c27-formation-andhra-state | high | multi_topic | Andhra State: context, formation, Bellary dispute, Sri Bagh Pact and the choice of Kurnool. |
| 17 | 5 | Andhra State CMs | u4-c27-formation-andhra-state | medium | multi_topic | Prakasam and B. Gopala Reddy as Andhra State chief ministers. |
| 17 | 8 | Vishalandhra Debate | u5-c28-merger-debate | medium | multi_topic | Visalandhra Mahasabha and idea, Andhra-side arguments, Telangana-side opposition, leaders' views. |
| 17 | 9 | Gentlemen's Agreement | u5-c30-gentlemens-agreement | high | multi_topic | Gentlemen's Agreement: context, eight signatories, fourteen points and significance. |
| 17 | 11 | Mulki Rules | u5-c30-gentlemens-agreement | medium |  | Mulki rules: origin, continuation under the Gentlemen's Agreement, Supreme Court rulings. |
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
| 18 | 14 | Social & Cultural Developments | u5-c31-arts-institutions | high | multi_topic | Literature, cinema and press, social and Dalit movements, Naxalite movement, education, language and cultural identity. |
| 18 | 15 | Major Projects | u5-c31-social-cultural-events-1956-2014 | medium | scope_boundary | Irrigation and IT projects: development history rather than social-cultural. |
| 18 | 16 | All AP CMs | u5-c31-social-cultural-events-1956-2014 | medium | scope_boundary | Reference table of chief ministers, 1956-2014. |

## Learner-facing subtopics with no note section (primary or secondary)

- Chapter 3 — Pre-Satavahana Andhra: 1 of 6: Kharavela and Kalinga
- Chapter 4 — Satavahanas: 1 of 8: Administration
- Chapter 5 — Ikshvakus: 1 of 9: Literature and education
- Chapter 6 — Post-Ikshvaku Minor Dynasties: 2 of 7: Pallava influence and other transitional dynasties; Society and economy
- Chapter 7 — Vishnukundins: 1 of 7: Administration, society and economy
- Chapter 12 — Gajapatis, Bahmanis and Other Regional Powers: 2 of 4: Minor regional powers, forts and political centres; Socio-cultural influence and political transition
- Chapter 14 — Thematic History of Andhradesa, 11th–16th Centuries: 3 of 6: Comparative administration and social structure; Economic conditions: agriculture, irrigation and trade; Music and dance
- Chapter 15 — Europeans, Trading Centres and Company Rule: 1 of 7: European trading companies in Andhra
- Chapter 17 — Socio-Cultural Awakening: 2 of 6: Major reformers; Associations and institutions
- Chapter 18 — Justice Party and Self-Respect Movement: 4 of 5: Leaders, policies and social impact; Self-Respect Movement; Influence in Andhra; Debates and limitations
- Chapter 20 — Socialists, Communists, Anti-Zamindari and Kisan Movements: 4 of 6: Socialists; Peasant organisation and Kisan movement; Labour mobilisation; Relation to the national movement
- Chapter 21 — Nationalist Poetry, Revolutionary Literature and Nataka Samasthalu: 4 of 6: Poets and authors; Newspapers and publications; People's theatre: Praja Natya Mandali and Maa Bhoomi; Folk performance and mobilisation
- Chapter 22 — Women's Participation: 5 of 5: Women reformers and women's organisations; Women in Swadeshi, Home Rule and Gandhian movements; Women in revolutionary and peasant movements; Prominent women and regional events; Social consequences
- Chapter 23 — Origin and Growth of the Andhra Movement: 1 of 5: Andhra University
- Chapter 24 — Andhra Mahasabhas and Prominent Leaders: 2 of 4: Organisational development; Contribution to state formation
- Chapter 25 — Press, Newspapers and the Library Movement: 2 of 4: Telugu newspapers (Krishna Patrika, Andhra Patrika and others); Language and literary organisations
- Chapter 26 — Folk and Tribal Culture: 2 of 5: Tribal customs and festivals; Cultural identity and mobilisation
- Chapter 27 — Formation of Andhra State, 1953: 2 of 5: Background, Dhar Commission and JVP Committee; Madras question
- Chapter 29 — States Reorganisation Commission: 2 of 4: Evidence and arguments on Andhra and Telangana; Conditions for merger and political responses
- Chapter 30 — Gentlemen's Agreement and Formation of Andhra Pradesh: 1 of 5: Hyderabad as capital
- Chapter 31 — Important Social and Cultural Events, 1956–2014: 1 of 7: Women's and civil-society movements

## Bundle note

The review bundle is **incremental**: it contains only the commits made after base commit `e91b270a` (`release/secured-review`) and applies only on top of a repository that already has that commit. It is not a standalone or complete backup.
