# Lesson 8 outline — వాతావరణం: పొరలు, సూర్యశక్తి, ఉష్ణోగ్రత, పీడనం, పవనాలు, తేమ, మేఘాలు, వర్షం, వాయురాశులు, తుఫానులు

Title line: `# అధ్యాయం 8: వాతావరణ పొరలు, ఉష్ణోగ్రత, పీడనం, పవనాలు, మేఘాలు, వర్షపాతం మరియు చక్రవాతాలు`

## Scope (Lessons 8 and 9 were planned together; they share old notes 14/15 and banks 14.json/15.json)
- IN (this lesson): book ch.13–19 on printed pages 57–78: temperature (p57–59: instruments, horizontal/vertical distribution, lapse rate, inversion, ranges, records, isotherms, isolines, contours), pressure (p60), humidity and precipitation incl. rainfall types (p61–62), tropical and temperate cyclones, anticyclones, frost/fog/smog/sleet/virga (p62–64), clouds (p65–66), atmosphere layers and composition (p67–68), winds: forces, 7 pressure belts, planetary winds, three cells, monsoon as a seasonal wind, local winds, jet streams (p69–74), air masses (p75–77), fronts (p78).
- Insolation, heat budget, albedo, day length, heat transfer, temperature scales (bank pages "55–56" of geo2.1) are NOT in $S/book/pages (p055–p056 there are coastal landforms of Lesson 7). Teach them from NCERT XI *Fundamentals of Physical Geography* ch.9 "Solar Radiation, Heat Balance and Temperature" + NASA Earth Observatory; the questions on "P055/P056" set the depth.
- OUT → Lesson 9 (world climate regions): book p79–107 (11 natural/climatic regions), Köppen and other classifications, climate normals/anomalies/statistics, applied climatology and climate change. In this lesson: at most one sentence + `[పాఠం 9: …](lesson-09#id)` (Lesson 9 ids are fixed in S/pipe/L09/OUTLINE.md: climate-statistics, classification, koppen-india, equatorial, tropical-monsoon, tropical-marine, savanna, hot-desert, temperate-grassland, mediterranean, china-type, british-type, laurentian, taiga, tundra, applied-climate).
- OUT (finished lessons own; one sentence + link, never re-teach):
  - `lesson-02#latlong-heatzones` — Torrid/Temperate/Frigid zones, 23½°/66½°, 5 belts.
  - `lesson-02#motion-coriolis` — Coriolis effect: what it is, right in N / left in S, zero at Equator, max at poles, Coriolis 1835, Foucault. (This lesson owns only Coriolis *as a wind force*: PGF + Coriolis = geostrophic, speed dependence, friction weakening it.)
  - `lesson-02#seasons-why`, `lesson-02#seasons-polar`, `lesson-02#seasons-overhead-sun` — seasons from axial tilt, polar day/Midnight Sun, overhead Sun. `lesson-02#motion-revolution` / `lesson-03#motion-perihelion-aphelion` — perihelion ~3–4 Jan, aphelion ~4–6 Jul.
  - `lesson-02#seasons-aurora`, `lesson-03#sun-storms-aurora` — aurora. `lesson-03#sun-wind-flare-cme` — solar wind.
  - `lesson-03#meteor-stages` — meteoroid/meteor/meteorite words. (This lesson owns only *where* meteors ablate: mesosphere.)
  - `lesson-03#inner-greenhouse` — greenhouse effect as a planetary idea (Venus). This lesson: one line on greenhouse gases trapping longwave; climate change → Lesson 9.
  - `lesson-01#heights-temperature` — world/India temperature records (Death Valley 56.7 °C 1913, Vostok −89.2 °C 1983, Al Azizia 58 °C cancelled 2012, Phalodi 51.0 °C 2016). This lesson adds only what Lesson 1 lacks: Klinck (Greenland) −69.6 °C N-Hemisphere record, Verkhoyansk/Oymyakon "pole of cold", annual range.
  - `lesson-01#reading-contours` — contour lines, close = steep. This lesson lists contour only as one row of the isoline table + link.
  - `lesson-05#magnitude` — magnitude vs intensity (isoseismal row links here). `lesson-03#tides-storm-surge` — storm surge (cyclone section links).
- Book p92 "monsoon" definition and mechanism questions stay here (`#monsoon-winds`); the monsoon *climate region* is Lesson 9.

Question ids below are short: `O14-001` = GEO-ORIG-14-001; `P067-001` = WG14-P067-001 or WG15-P0xx-xxx (page numbers are unique across the two banks: p55–66 and p69–78 = WG15, p67–68 and p92–107 = WG14). Machine list: `S/pipe/L08/work/map.py` (writes map_L08.json, map_L09.json).

Total budget: 19,950 words (Part A 6,650 · Part B 6,600 · Part C 6,700). Hard floor 18,000, ceiling 20,500. 614 bank questions stay in this lesson, so the budget is at the top of the band.

---

## Section list

### PART A — గాలి పొరలు, సూర్యశక్తి, ఉష్ణోగ్రత — ~6,650 words · writer outputs title, intro, terms, sections 1–7

| # | Heading | id | Purpose | Owns | Words |
|---|---|---|---|---|---|
| 0 | `::: intro` + `::: terms` | — | what/why; terms box for the WHOLE lesson from OWNERS.md (B and C send extras) | — | 650 |
| 1 | Weather, Climate ఒకటేనా? | `#weather-climate` | the frame: weather vs climate, elements, controls; who measures | Weather (వాతావరణం) = short-term state; Climate (శీతోష్ణస్థితి) = long-term statistical character incl. variability and extremes; elements (temperature, pressure, wind, humidity, cloud, precipitation); controls (latitude, altitude, distance from sea, ocean currents, prevailing winds, relief) — list only, each taught later; WMO (Geneva, UN agency, 1950) vs IMD (1875, New Delhi) vs IITM (Pune); climate normal/anomaly = one line + link `lesson-09#climate-statistics` | 450 |
| 2 | గాలిలో ఏమేమి ఉన్నాయి? | `#composition` | composition, mass distribution, no sharp top, homosphere/heterosphere | dry-air table N₂ 78.08, O₂ 20.95, Ar 0.93, CO₂ ~0.042% (changing), Ne, He, CH₄ ~0.0002%, Kr, H₂, O₃ trace; water vapour 0–~4% variable, not in dry-air table; aerosols/dust as condensation nuclei (preview `#precipitation`); trace ≠ unimportant (CO₂, O₃); mass: ~50% below ~5.5 km, ~99% below ~30–32 km; no sharp edge, thins into space; homosphere (turbulent mixing, uniform major gases) to homopause ~80–100 km, heterosphere above (diffusive separation, light gases up); three bases of division (temperature → layers, ionisation → D/E/F, mixing → homo/hetero) — one table; IGY 1 Jul 1957–31 Dec 1958 (Sputnik 1957 one line) | 850 |
| 3 | గాలి పొరలు ఎన్ని? ఎత్తుకు వెళ్తే ఎందుకు చల్లగా, మళ్లీ వేడిగా? | `#layers` | the five temperature layers in one table + why temperature turns | Troposphere (ట్రోపో ఆవరణం): ~8 km poles, ~18 km Equator, varies with season; ~75–80% mass, nearly all water vapour → weather; lapse rate (ఉష్ణోగ్రత క్షీణత రేటు) definition owned in `#temperature-distribution` (preview); tropopause temp varies (~−80 °C over Equator, ~−45 °C poles); tall Cb tops can poke into stratosphere; Stratosphere to ~50 km, ozone 15–35 km, UV absorption → warming with height, calm → jet aircraft cruise in lower stratosphere, stratopause ~0 °C (varies); Mesosphere 50–80/85 km, coldest near mesopause (~−90 to −100 °C), meteors ablate here (link `lesson-03#meteor-stages`), "ignorosphere" (hard to observe); Thermosphere: very high kinetic temperature but very thin air (no felt heat), aurora (link); Exosphere: H, He, exobase ~500–1,000 km, ~10,000 km teaching extent, geocorona (UV glow of H); order T-S-M-Th-E; nacreous/noctilucent clouds = preview + link `#clouds` | 1,200 |
| 4 | Ionosphere ఒక పొరా? Radio తరంగాలు ఎలా తిరిగి వస్తాయి? | `#ionosphere` | ionisation-defined region overlapping meso/thermo; radio | ionisation definition; ~60/75 km to ~1,000 km; varies with Sun/day-night; D region (~60–90 km, daytime absorption of HF, disappears/weak at night), E (~90–150 km; Kennelly–Heaviside 1902 prediction, Appleton confirmed 1924 V), sporadic E (patches, day or night), F (>150 km; F1 + F2 by day, merge at night; F2 key for long-distance HF; "Appleton layer"; Appleton Nobel 1947); book "G layer ~480 km" not in modern D-E-F scheme; upper ionosphere ions shift O⁺ → H⁺/He⁺ (one line) | 600 |
| 5 | సూర్యుడి నుంచి వచ్చిన శక్తి ఎటు వెళ్తుంది? | `#insolation` | radiation basics + heat budget + what makes insolation vary | solar radiation = EM energy (UV, visible, IR); Insolation (సూర్యపుటం/ఇన్సొలేషన్) = incoming solar radiation; Earth intercepts ~1 in 2.2 billion of Sun's output; solar constant/TSI ~1361 W/m² (old 1.94 cal/cm²/min) not truly constant; shortwave in, longwave (terrestrial radiation) out because Earth is cooler; albedo definition, Earth ~0.30 (NCERT 35 units), surface albedo table as ranges (fresh snow high, ocean low); budget NASA: 29% reflected, 23% absorbed by atmosphere, 48% by surface vs NCERT 35/14/51 (changing table); radiation budget = in SW, out SW, out LW; geothermal tiny; greenhouse gases absorb LW (one line + link `lesson-03#inner-greenhouse`); factors: angle of incidence (spread + longer path), day length (more toward pole in summer; equator ~12 h; Arctic Circle 24 h — link `lesson-02#seasons-polar`), atmospheric transparency (cloud, dust, aerosols: reflect, scatter, absorb), Earth–Sun distance (perihelion Jan/aphelion Jul one line + link; seasons from tilt, link) | 1,200 |
| 6 | వేడి ఎలా ప్రయాణిస్తుంది? ఉష్ణోగ్రతను ఎలా కొలుస్తారు? | `#heat-transfer` | modes of heating the air + scales + instruments + daily timing | conduction (ground → lowest air), convection (vertical), advection (horizontal; book "ఉష్ణప్రవాహం"), radiation (no medium; only mode in vacuum); sensible vs latent heat (latent owned `#humidity`, preview); PYQ APPSC Gr-2 2024 match (advection–horizontal, conduction–lower layers…); scales: 0 °C = 32 °F, 100 °C = 212 °F, F = 9/5 C + 32, 0 °F ≈ −17.8 °C, 37 °C = 98.6 °F, K = °C + 273.15 (no degree sign); instruments: thermometer, max–min (Six's) thermometer, thermograph, pyrometer (radiation, very high temperature), Bourdon tube = pressure-sensing element (book's "aircraft thermometer" mixes principles — one line), Sun's temperature from spectra not a thermometer; daily max ~2 pm (after solar noon, lag), min near sunrise (book 4 am) | 800 |
| 7 | ఉష్ణోగ్రత ఎక్కడ ఎంత? ఎత్తుకు వెళ్తే ఎంత తగ్గుతుంది? | `#temperature-distribution` | horizontal + vertical distribution, inversion, ranges, records | horizontal: latitude, land–sea, currents, altitude, winds, advection; heat zones one line + link `lesson-02#latlong-heatzones`; book's warm/cold temperate split (23½–45°, 45–66½°) and "11 regions" = old teaching subdivisions → link `lesson-09#classification`; vertical: environmental lapse rate definition, standard 6.5 °C/km (book 6.4 °C/km = 1 °C per 165 m); inversion: definition + where (valleys at night/cold-air pooling, snow surfaces, winter early mornings, city/industrial smog layers) — book "heat islands" wording corrected; book's descriptive bands (cold/cool/warm/hot) as vocabulary only; diurnal range (DTR) = max − min (34 − 18 = 16 °C), large in deserts, small humid equator/coast/cloudy nights; annual range = warmest-month mean − coldest-month mean, largest in high-latitude continental interiors (Verkhoyansk, Siberia), smallest at Equator; records: link `lesson-01#heights-temperature`; add N-Hemisphere official low −69.6 °C Klinck, Greenland (1991, WMO 2020), Verkhoyansk −67.8 °C / Oymyakon −67.7 °C as inhabited "pole of cold" (not world record) | 950 |

### PART B — సమరేఖలు, పీడనం, పవనాలు — ~6,600 words · sections 8–15

| # | Heading | id | Purpose | Owns | Words |
|---|---|---|---|---|---|
| 8 | పటంలో సమాన విలువల గీతలు: Isotherm, Isobar … | `#isolines` | isoline idea + isotherms read + one table of all iso-words | isoline/isopleth (సమాన విలువ రేఖ); isotherm (సమోష్ణోగ్రత రేఖ) definition; January and July maps; E–W trend from latitude; bend poleward over oceans in winter… (state the rule: over continents they bend equatorward in winter and poleward in summer; over oceans the reverse — V wording); more regular in S-Hemisphere (more ocean) — PYQ TGPSC Gr-2 2025; table: isobar (pressure), isobath (depth), isohyet (rain), isohaline (salinity), isohel (sunshine), isoneph (cloud), isonif/isochion (snow), isoryme (frost), isobront (thunder), isochrone (time), isoseismal (equal intensity; magnitude vs intensity link `lesson-05#magnitude`), isotach (wind speed), isogon (wind direction), isodop (Doppler velocity; zero isodop = 0), isohypse (equal geopotential height on upper-air chart), contour (link `lesson-01#reading-contours`); hypsographic curve (area vs elevation/depth); streamline (tangent = flow direction) | 650 |
| 9 | గాలికి బరువు ఉందా? Pressure ఎందుకు మారుతుంది? | `#pressure` | pressure definition, history, instruments, units, extremes, controls | pressure = weight of air column per area; Galileo (air has weight) → Torricelli 1643 mercury barometer; mercury barometer (column height), aneroid (no liquid, evacuated capsule), barograph, microbarograph; psychrometer row → `#humidity`; units 1 hPa = 1 mb; standard 1013.25 hPa = 760 mm Hg = 29.92 in; 900–1030 hPa ordinary range not limits; records WMO: highest 1083.8 hPa Agata, Siberia (31 Dec 1968, below 750 m), 1089.1 hPa Tosontsengel, Mongolia (2001, above 750 m); lowest 870 hPa Typhoon Tip (12 Oct 1979); total mass ~5.1×10¹⁸ kg (book's "56 × 10…" figure wrong); falls with height (~1 hPa per 8–10 m near sea level only); temperature: heating + rising → thermal low (not temperature alone); humidity: H₂O 18 vs dry air ~29 → moist air lighter, but pressure need not always fall; isobar = preview, definition owned `#wind-forces` | 800 |
| 10 | గాలిని ఏ శక్తులు కదిలిస్తాయి? | `#wind-forces` | wind measurement + the four forces + balanced winds | wind = horizontal air motion; named from where it comes (westerly from west); units; wind vane (direction, siting), cup anemometer (speed), combined units; Beaufort scale 0–12 (Beaufort 1805, visual effects); upper air: radiosonde/GPS balloon, radar; isobar (సమభార రేఖ) definition; PGF (పీడన ప్రవణత బలం): pressure difference per distance, high → low, perpendicular to isobars, starts the wind; close isobars = strong gradient (not exact speed); Coriolis as a wind force: recall + link `lesson-02#motion-coriolis`; adds: acts at right angles, changes direction not speed, grows with speed and latitude, Ferrel's law wording; geostrophic wind = PGF + Coriolis balance, parallel to isobars aloft; friction: slows wind, stronger over land, weakens Coriolis → surface wind crosses isobars toward low; curved flow: centripetal acceleration (book "centrifugal" = apparent outward force in rotating frame), gradient wind = PGF + Coriolis + curvature; summary table force → effect | 950 |
| 11 | భూమి మీద పీడన మేఖలలు ఎన్ని? ఎందుకు ఏర్పడ్డాయి? | `#pressure-belts` | 7 belts, thermal vs dynamic origin, shifts | wind classes by duration: permanent (planetary), seasonal, local (book) — monsoon = seasonal; 7 belts = 1 equatorial low + 2 subtropical highs + 2 subpolar lows + 2 polar highs; equatorial low ~0–5°/10° = ITCZ (full form), doldrums (weak mean surface wind, strong convection); subtropical highs ~25–35° (book 23½–35°), horse latitudes, subsidence → dry → most hot deserts on west sides of continents (Sahara, Kalahari, Atacama, Australian; Thar) — the climate region itself is Lesson 9 `#hot-desert`; Patagonia dry from Andes rain shadow; subpolar lows ~60° (book 45–66½°): convergence, polar front cyclones; polar highs (cold dense sinking); thermal (equatorial low, polar high) vs dynamic (subtropical high, subpolar low) origin; belts shift ~5–10° with overhead Sun and break into cells over land | 750 |
| 12 | Trade winds, Westerlies, Polar easterlies ఎలా వీస్తాయి? | `#planetary-winds` | the three planetary winds + three-cell model | trade winds 0–30°: NE trades (N), SE trades (S), "easterlies", steady, Hadley cell surface branch, rain on east coasts/windward slopes; Hadley cell (George Hadley 1735): ITCZ ascent → poleward aloft → subtropical subsidence → trades back; westerlies 30–60°: from SW (N) / NW (S), variable (cyclones, jets, land), Roaring Forties (40°S), Furious Fifties, Shrieking/Screaming Sixties, stronger and steadier in S-Hemisphere (ocean); bring winter rain to west coasts (Mediterranean link `lesson-09#mediterranean`); Ferrel cell (William Ferrel 1856) 30–60°, thermally indirect, maintained by eddies, surface flow poleward-eastward; polar easterlies 60–90°: from NE (N) / SE (S), polar high → subpolar low, cold, weak; polar cell smallest/weakest; polar front where polar easterlies meet westerlies → temperate cyclones (preview `#temperate-cyclones`); one diagram-as-table: belt → wind → cell | 950 |
| 13 | Monsoon అంటే వర్షమా, గాలా? | `#monsoon-winds` | monsoon as seasonal wind reversal (mechanism only) | word from Arabic *mausim* = season; core meaning = seasonal reversal of prevailing winds, not "rain"; rainy season ≠ monsoon; basic summer sequence: land heats faster → low over land → moist oceanic flow → uplift → rain; modern additions: ITCZ/monsoon trough shift north, cross-equatorial flow (Somali jet one line V), tropical easterly jet + Tibetan high (link `#jet-streams`), relief; South Asia: summer SW (ocean → land, moist), winter NE (land → sea, dry; rain on Tamil Nadu/south AP coast); land–sea breeze is the daily version (link `#local-winds`); world monsoon climates, Indian seasons (IMD four), Australia → Lesson 9 `#tropical-monsoon` | 500 |
| 14 | ఒక్క ప్రాంతానికే పరిమితమైన గాలులు: Local winds | `#local-winds` | daily breezes + foehn family + named hot/cold winds in one table | local winds from local heating/cooling, relief; strong prevailing wind can suppress them; sea breeze (day, sea → land; land low pressure; return flow aloft land → sea; cools coastal cities incl. Visakhapatnam, Chennai), land breeze (night, weaker/shallower); valley breeze = anabatic (day upslope), mountain breeze = katabatic (night downslope, cold-air pooling, inversion — link `#temperature-distribution`); Foehn (ఫోన్): warm dry leeward downslope, adiabatic compression + moisture lost on windward side (not friction), Alps, warming varies; Chinook ("snow eater", east of Rockies, USA + Canada), Santa Ana (Great Basin high → S. California, wildfire), Zonda (Argentina lee of Andes), Berg (South Africa, hot dry offshore — book wrongly lists as cold); hot winds: Sirocco (Sahara → S. Europe, dusty, becomes humid after the sea, "blood rain"), regional names Ghibli (Libya), Chili (Tunisia), Khamsin (Egypt), Leveche (SE Spain), Brickfielder (Australia, hot) vs Black Roller (US dust) as separate names; Simoom (Arabia/Sahara, intensely hot dusty); Harmattan (dry dusty NE from Sahara to W. Africa coast, winter, "Doctor wind", but dust irritates lungs); Nor'westers / Kalbaisakhi (pre-monsoon thunderstorms, West Bengal, Assam, Bihar, Jharkhand, Odisha; "mango showers" in Kerala/Karnataka = different, one line V); Loo (hot dry afternoon wind NW/N India, May–June, heatstroke); cold winds: Mistral (Rhône valley, S. France), Bora (N. Adriatic, gusty downslope), Bise (Switzerland–France), Pampero (Pampas), Norte (Mexico/Gulf), Buran/Purga (Siberia/Russia, snowstorm), Southerly Buster (NSW coast), Blizzard = a snow-wind condition, not a named local wind; one table name–region–hot/cold–note; book names not found in standard sources (Lavender, Puna, …) not taught | 1,250 |
| 15 | Jet streams అంటే ఏమిటి? మన వాతావరణాన్ని ఎలా నడిపిస్తాయి? | `#jet-streams` | jets: what, why, where, speed, effects, history | narrow band of very strong upper wind (3-D, core speed max), meanders/splits/merges; cause: strong horizontal temperature gradient + Coriolis + pressure; mostly west → east; height ~8–14 km (book 9–12 km); subtropical jet ~30° (poleward edge of Hadley cell), polar-front jet ~50–60° (book "40–60"), may merge; speeds vary, cores can exceed 400 km/h (book 144 typical, 480 max); stronger in winter (bigger pole–Equator contrast), weaker and poleward in summer; tropical easterly jet over India in summer (east → west, ~13–15°N, monsoon) V; effects: steers cyclones/air masses, deepens lows, Rossby-wave blocking → heat waves/cold spells/droughts/floods, aircraft time-fuel saving, clear-air turbulence; monsoon–jet link (STJ shifts north of Himalaya before onset) but not the only cause; history: Wasaburo Ōishi (1920s balloons, Japan) V, Seilkopf "Strahlströmung" 1939, WWII B-29 pilots 1944; book's APPSC Gr-1 2022 PYQ (statements on trade winds) solved here | 750 |

### PART C — తేమ, మేఘాలు, వర్షం, వాయురాశులు, వాతాగ్రాలు, చక్రవాతాలు — ~6,700 words · sections 16–23 + closing

| # | Heading | id | Purpose | Owns | Words |
|---|---|---|---|---|---|
| 16 | గాలిలో తేమ ఎంత ఉంది? Relative humidity, Dew point | `#humidity` | humidity measures, saturation, latent heat | humidity (ఆర్ద్రత) = water vapour in air; sources: evaporation from water bodies (~90%), transpiration (~10%), sublimation (ice → vapour); hygrometer, sling psychrometer (wet/dry bulb → RH); specific humidity (g/kg of moist air) vs mixing ratio (per dry air) vs absolute humidity (g/m³, changes when air expands); relative humidity (సాపేక్ష ఆర్ద్రత) = actual / saturation vapour × 100 (30/50 = 60%); RH rises when air cools without added vapour (saturation capacity falls); 100% = saturated; 0% ideal limit; dew point (తుషార స్థానం) = temperature at which air saturates on cooling; condensation (ద్రవీభవనం in book) / deposition; latent heat: absorbed in evaporation, released in condensation (energy of storms — preview `#tropical-cyclones`); sensible heat definition (thermometer-felt) | 800 |
| 17 | మంచు, పొగమంచు, Smog, Sleet ఎలా ఏర్పడతాయి? | `#condensation-forms` | surface and near-surface forms + odd precipitation types | dew; frost/hoar frost = vapour deposits directly as ice on cold surface (ground frost possible even when screen air > 0 °C); frozen dew ≠ frost; book "white frost" = hoar frost; mist (visibility ≥1 km, <~10 km) vs fog (<1 km) (book 1–2 km); fog is not precipitation; fog vs stratus (touches ground or not) — link `#clouds`; types of fog one line (radiation, advection — Grand Banks detail in `lesson-09#laurentian`); smog: smoke + fog (London 1952 V), photochemical smog (NOx + hydrocarbons + sunlight → ozone; Delhi winter is mainly particulate) V; haze (dry particles); glaze (supercooled rain freezing on impact) vs hoar frost; sleet: US = ice pellets, UK/India = rain–snow mix; snow can reach ground when air slightly above 0 °C; hail (strong Cb updraft, layers) — owner here; virga (evaporates before ground, can precede microburst) | 650 |
| 18 | మేఘాలు ఎన్ని రకాలు? ఆకాశం చూసి వాతావరణం చెప్పగలమా? | `#clouds` | cloud definition + WMO 10 genera by height + special high clouds | cloud = suspended droplets/ice crystals; ceilometer measures cloud-base height (aerosol backscatter only with calibration); WMO 10 genera (book "9"); height families in temperate zone: high ~5–13 km, middle 2–7 km, low 0–2 km (book 6–12 / 2–6 / <2), higher in tropics lower near poles; cumulus/Cb span levels; high: cirrus (ice, silky filaments, "mare's tails", fair weather but can signal warm front, virga), cirrostratus (thin veil, halo around Sun/Moon — not a guarantee of rain), cirrocumulus (small grains/ripples, mackerel sky); middle: altostratus (grey sheet, dim Sun, thickens to nimbostratus ahead of warm front), altocumulus (rounded masses with shading, corona; castellanus = instability); low: stratocumulus (lumpy rolls), stratus (uniform grey layer, drizzle; book "300 km" is ~300 m), nimbostratus (thick dark, steady rain/snow); vertical: cumulus (flat base, cauliflower top; can grow to congestus), cumulonimbus (thunder, lightning, hail, gusts; updraft + downdraft; anvil = incus, flattened by tropopause; "king of clouds" nickname; not only evenings; height varies, 7 km not a ceiling); clouds above the troposphere: nacreous = polar stratospheric clouds (polar winter stratosphere, help chlorine activation → ozone hole), noctilucent (mesosphere ~76–85 km, high-latitude summer twilight, ice on meteor dust, shine by sunlight); APPSC 2020 matching PYQ solved; one table genus–height–look–weather; cloudburst one line (IMD: ≥100 mm/h over small area) V | 1,050 |
| 19 | వర్షం ఎలా పడుతుంది? మూడు రకాల వర్షపాతం | `#precipitation` | from cloud to rain + three lifting types | precipitation (అవపాతం) forms: rain, drizzle, freezing rain, sleet, snow, hail; condensation nuclei (dust, salt; book ఆర్ద్రతాగ్రాహక కేంద్రకాలు V term); droplets too small to fall, must grow (collision–coalescence in warm clouds, ice-crystal process in cold clouds); drop vs drizzle boundary ~0.5 mm, raindrops up to ~5 mm, large drops ~9 m/s (book 29 km/h ≈ 8 m/s); adiabatic cooling of rising air (preview owner here: rising air expands and cools without heat loss); convectional rain: surface heating → buoyant rise → cooling → Cb showers, afternoon in equatorial belt (not exact time daily), Indian summer/pre-monsoon storms; orographic (relief) rain: windward slope heavy, leeward rain shadow (descending air compresses, warms, RH falls) — Western Ghats windward vs Deccan/Rayalaseema rain shadow; book term ఓరోగ్రాఫిక్; cyclonic/frontal rain: convergence + ascent in lows (tropical and temperate cyclones — owners later), along fronts; mid-latitude interiors get all types; book's "katabatic heating" phrase = adiabatic warming on descent | 750 |
| 20 | వాయురాశులు (Air masses) అంటే ఏమిటి? cP, mT కోడ్ ఎలా చదవాలి? | `#air-masses` | air mass, source region, codes, modification | air mass (వాయురాశి) = large body, relatively uniform temperature and humidity horizontally; source region: large uniform surface, weak winds, long residence (Siberia, N. Canada, Sahara, tropical oceans); classification (Bergeron 1928 V): first letter c (continental, dry) / m (maritime, moist); P polar, T tropical, A/AA arctic/antarctic (colder than P), E equatorial in some schemes; cP (Siberia, interior Canada; cold dry), mP (N. Pacific, N. Atlantic, Southern Ocean; cool moist), cT (Sahara, SW USA, Australian/Thar deserts; hot dry), mT (tropical Atlantic, Pacific, Indian Ocean; warm moist); trajectory + modification: sensible heat, evaporation, latent heat release; k = colder than surface → heated from below → unstable → cumulus, showers; w = warmer than surface → cooled from below → stable → stratus, fog, drizzle; u/s suffix in some schemes; code order: source surface → thermal origin → k/w → u/s (cPk, mPw, cTw…); book diagram's uppercase K/W and the "friction makes stable/unstable" line corrected (thermal contrast primary; friction affects wind/mixing); stability definition (parcel sinks back vs keeps rising); jet steers air masses (link) | 850 |
| 21 | రెండు వాయురాశులు కలిసే చోట ఏమవుతుంది? Fronts | `#fronts` | front definition + 4 types with weather | front (వాతాగ్రం) = 3-D sloping transition zone between contrasting air masses (density difference stops quick mixing); no single width (book "3–5 to 90 km" just examples); polar front (polar vs subtropical air, cyclones, polar jet) vs ITCZ (convergence belt, not an air-mass front); cold front (శీతల వాతాగ్రం): cold replaces warm, steep, rapid lift, narrow band of showers/thunderstorms; warm front (కవోష్ణ వాతాగ్రం): warm advances over cold, gentle slope, cirrus → altostratus → nimbostratus, widespread steady rain; stationary front (స్థిర వాతాగ్రం): neither replaces, prolonged rain; occluded front (అధివిష్ట వాతాగ్రం): cold front catches warm front, warm sector lifted off the ground; frontal passage → temperature, wind, pressure, rain change; one table | 600 |
| 22 | ఉష్ణమండల చక్రవాతం ఎలా పుడుతుంది? మన తీరాన్ని ఎందుకు తాకుతుంది? | `#tropical-cyclones` | tropical cyclone: definition, structure, energy, conditions, seasons, names, India | cyclone (చక్రవాతం) = low pressure with inward spiralling winds, anticlockwise N / clockwise S; tropical cyclone = organised warm-core non-frontal low over tropical oceans; energy = latent heat of condensation; eye (calm, sinking) vs eyewall (strongest wind, rain); conditions: SST ≳26.5–27 °C to ~50 m depth, Coriolis enough (≥~5° from Equator), low vertical wind shear, moist mid-troposphere, pre-existing disturbance — necessary not sufficient; weakens over land/cold water (no moisture supply); size: eye vs storm width vs height (Cb tops to 12–15 km); seasons: summer–autumn peak; North Indian Ocean bimodal: pre-monsoon Mar–May and post-monsoon Oct–Dec (Bay of Bengal > Arabian Sea); names by basin: hurricane (Atlantic/Caribbean, NE Pacific), typhoon (NW Pacific → China, Japan, Philippines; Philippine "bagyo" = generic word, Baguio = city), cyclone (Indian Ocean, S. Pacific, Australia; "willy-willy" old Australian name for dust devils/cyclones V; PYQ TG-SI 2023 → Australia); tornado ≠ tropical cyclone (small, from thunderstorm, land, USA "tornado alley"); IMD intensity categories table (depression … super cyclonic storm); naming: WMO/ESCAP Panel, 13 countries, list of 169 names from 2020 (changing); RSMC New Delhi; AP: coastline exposure, storm surge (link `lesson-03#tides-storm-surge`), INCOIS one line (link `lesson-05#tsunami`) | 950 |
| 23 | సమశీతోష్ణ చక్రవాతం వేరేనా? ప్రతిచక్రవాతం అంటే? | `#temperate-cyclones` | extratropical (frontal/wave) cyclone + comparison + anticyclone | extratropical/temperate cyclone: forms on the polar front as a wave on an air-mass boundary (Norwegian model, Bjerknes 1919 V), energy from horizontal temperature contrast (baroclinic), warm + cold + occluded fronts, cold-core/asymmetric, ~2,000 km across, over land and sea, all year but stronger in cool season, moves west → east with westerlies/jet, rain spread along fronts; Mediterranean winter rain/Western Disturbances to N. India (one line, V); comparison table tropical vs temperate (region, energy, fronts, core, season, size, height, isobars circular vs elongated — book "V-shape" not universal, wind max at eyewall vs along fronts, track westward-recurving vs eastward, speed — no universal ranking); book p63 table mixes eye diameter, storm width and height — state correct items only; extratropical transition (tropical storm moves poleward, becomes frontal); anticyclone (ప్రతిచక్రవాతం): high in centre, outward winds, clockwise N / anticlockwise S, subsiding air, clear skies, large day–night range, no rain; PYQ APPSC Gr-1 2022 ("no clear frontal system" is the wrong statement) solved | 700 |
| — | pairs / selfcheck / sources | `#pairs` `#selfcheck` `#sources` | closing per lesson-format.md; **no `#recap`** | — | 350 |

---

## Fact ledger
Source key: BK pNN = student's book (S/book/pages/pNNN.txt); NCERT = NCERT XI *Fundamentals of Physical Geography* ch.8 (composition & structure), ch.9 (solar radiation, heat balance, temperature), ch.10 (circulation & weather systems), ch.11 (water in the atmosphere); WMO = WMO Archive of Weather and Climate Extremes / International Cloud Atlas; NOAA/NWS JetStream; NASA = NASA Earth Observatory energy budget; IMD = IMD cyclone FAQ / glossary; NOAA GML = CO₂ trends; V = writer must verify (or write the safe "సుమారు" form).

### `#weather-climate`
- Weather = state of the atmosphere at a place over a short time (hours–days); Climate = long-term statistical character (averages, seasonal pattern, variability, extremes) — commonly over 30 years. NCERT ch.8, WMO. [O14-005 006 018]
- Elements: temperature, pressure, wind, humidity, clouds, precipitation. NCERT.
- Controls: latitude, altitude, distance from sea (continentality), ocean currents, prevailing winds and air masses, relief. NCERT, BK p57.
- WMO: UN specialised agency, HQ Geneva, Convention in force 1950 (World Meteorological Day 23 March). IMD est. 1875, HQ New Delhi. IITM Pune (est. 1962 V). [P056-020]

### `#composition`
- Dry air by volume: N₂ 78.08%, O₂ 20.95% (book 20.94), Ar 0.93%, CO₂ ~0.042% (≈420+ ppm; NOAA global mean 2024 ≈ 423 ppm V) — book 0.03% is decades old; Ne 0.0018, He 0.0005, CH₄ ~0.0002% (≈1.9 ppm V), Kr, H₂, O₃ trace. BK p68, NOAA GML. [O14-009 010 020 P068-022 023]
- Water vapour: 0 to ~4% by volume (humid tropics high, deserts/polar near 0); not in a "dry-air" table; nearly all in troposphere. BK p68 (0.4% average), NCERT. [O14-012 P068-025 026]
- Ozone: trace gas; stratospheric layer absorbs most harmful UV. Trace ≠ unimportant (CO₂, O₃, CH₄ radiative/chemical effects). [O14-011 015 021 P068-024]
- Mass: ~50% below ~5.5 km; ~99% below ~30–32 km (NCERT "32 km"); book wording "39 km" read as OCR noise. No sharp top; density thins into space. BK p67, NCERT. [P067-001 004 005]
- Homosphere: turbulent mixing keeps major-gas ratios nearly uniform up to homopause ~80–100 km; heterosphere above: molecular diffusion, gases layered by weight (N₂, O, He, H upward). Book: tropo+strato+meso = homosphere; thermo+exo = heterosphere. BK p68. [P068-016..019]
- Three bases of division: temperature (5 layers), ionisation (D/E/F), mixing/composition (homo/hetero). [P068-027 P067-003]
- International Geophysical Year: 1 July 1957 – 31 December 1958 (book "1957–62" wrong). Sputnik 1 launched 4 Oct 1957 during IGY; Telstar 1962 one line only if needed. [P068-020 021]

### `#layers`
- Order by temperature: troposphere → stratosphere → mesosphere → thermosphere → exosphere. [P067-002 O14-013]
- Troposphere: ~8 km at poles, ~18 km at Equator (book 8/18), average ~13 km; tropopause height varies with latitude and season; ~75–80% of atmospheric mass (book 80%), almost all water vapour and aerosols → weather ("mixing layer"/"turbulent layer"); temperature falls with height (lapse rate, owner `#temperature-distribution`). BK p67, NCERT. [O14-001 016 P067-006..011]
- Very tall cumulonimbus tops can overshoot into the lower stratosphere (weather not absolutely confined). NOAA. [P067-009]
- Tropopause temperature varies: about −80 °C over Equator, ~−45 °C over poles (NCERT); book "−80" one value. [P067-012]
- Stratosphere: to ~50 km (stratopause); ozone mostly 15–35 km (NCERT); temperature rises with height because ozone absorbs UV; stable, few clouds → jet aircraft cruise in lower stratosphere; stratopause near 0 °C (varies). BK p67. [O14-002 016 P067-013..016]
- Mesosphere: ~50 to 80–85 km; temperature falls to the coldest values in the atmosphere at mesopause (~−90 to −100 °C; book −100 °C at 80 km); meteors heat, vaporise, fragment (ablation) here — not "only friction"; nicknamed "ignorosphere" (too high for balloons, too low for satellites). BK p67, NASA. [O14-003 017 P067-020..024]
- Thermosphere: from ~80–85 km to ~500–1,000 km; kinetic temperature can exceed 1,000 °C but density so low that little heat is transferred; temperature rises with height; aurora, ISS orbits here (~400 km) V. NCERT, NASA. [O14-004 P068-013]
- Exosphere: outermost; mainly H and He; exobase ~500–1,000 km (book "1,000 km Exobase"); upper extent ~10,000 km as teaching value (not a wall); geocorona = UV glow of neutral hydrogen around Earth (scattering of solar Lyman-alpha). BK p68, NASA. [P068-009..015]
- p67 matching: troposphere–weather; stratosphere–ozone warming; mesosphere–meteor ablation; ionosphere–radio reflection. [P067-030]

### `#ionosphere`
- Ionisation = removal of electrons from atoms/molecules by solar UV/X-rays → ions + free electrons. [P067-025]
- Ionosphere ≈ 60–1,000 km, overlaps mesosphere and thermosphere; defined by ionisation, not temperature; boundaries vary with solar activity, day/night. BK p67 (book: thermosphere = ionosphere). [O14-022 P067-003 026]
- Radio: can reflect, refract or absorb depending on frequency and conditions. [P067-027]
- D region ~60/75–90/95 km: daytime only, absorbs HF/MF, reflects LF; weak at night. BK p67 (70–90), NOAA SWPC. [P067-028]
- E region ~90/95–150 km (book 90–160): Kennelly–Heaviside layer (predicted 1902 by Arthur Kennelly, USA, and Oliver Heaviside, UK); regular daytime E. BK p67. [P067-029]
- Sporadic E (Es): thin transient patches of high electron density in E region, day or night, varies with latitude/season. BK p68. [P068-001 002]
- F region above ~150 km to ~500+ km; F1 (~150–200 km) and F2 (~200–400+ km) by day, merge at night; F2 most important for long-distance HF; "Appleton layer" = F (F2) layer, Edward Appleton (Nobel Physics 1947). BK p68. [P068-003..006]
- Book "G layer ~480 km" is not part of the modern D-E-F scheme. [P068-007]
- Topside ionosphere: O⁺ gives way to H⁺ and He⁺ with height. [P068-008]

### `#insolation`
- Solar radiation: EM energy from the Sun, mainly UV, visible, near-IR. Insolation = incoming solar radiation received by Earth (or a given surface). NCERT ch.9. [O15-001 P055-002 005]
- Earth intercepts about one two-billionth (≈1 in 2.2 billion) of the Sun's output. NCERT ("1 in 2,000 million"). [P055-003]
- Total solar irradiance at mean Earth–Sun distance ≈ 1361 W/m² (NASA/SORCE; old "solar constant" 1.94 cal/cm²/min); varies slightly with solar cycle. V wording. [P055-014]
- Solar radiation shortwave; Earth (cooler) emits longwave infrared = terrestrial radiation. Earth heats the atmosphere mainly from below. NCERT. [O15-003 013 017 P055-006..008]
- Albedo = fraction of incident shortwave reflected; Earth's Bond albedo ≈ 0.29–0.30 (NASA); NCERT uses 35 units. Surface albedo values are ranges (fresh snow ~0.8–0.9, ocean ~0.06, forest ~0.1–0.2) V. [O15-002 016 P055-009..011]
- Energy budget (NASA): of 100 units, ~29 reflected (by clouds, air, surface), ~23 absorbed by atmosphere, ~48 absorbed by surface; NCERT: 35 reflected, 14 atmosphere, 51 surface. Changing/model block. [P055-004]
- Radiation budget flows: incoming solar, reflected shortwave, outgoing longwave; geothermal heat flux is tiny compared with absorbed solar. [P055-012 013]
- Oblique rays: same energy over larger area + longer path through atmosphere → less heating. NCERT. [P055-015]
- Day length: Equator ~12 h all year; in summer daylight increases poleward; Arctic/Antarctic Circles = edge of 24-h day (book table: 66½° → 24 h); link `lesson-02#seasons-polar`. [P056-001..004]
- Clouds, dust, aerosols reduce direct sunlight by reflection, scattering, absorption (transparency). [P056-005]
- Perihelion early Jan, aphelion early Jul; seasons from axial tilt, not distance — one line + link. [P056-006..008]

### `#heat-transfer`
- Conduction: contact, warms lowest air layer; convection: vertical transfer by rising warm air (mainly troposphere); advection: horizontal transfer by wind (major in mid-latitudes); radiation: EM waves, no medium needed — only mode through vacuum. NCERT. [P056-009..012]
- APPSC Group-2 2024 PYQ (book p59) match: advection–horizontal heating, conduction–lower layers, insolation–direct, convection–vertical. BK p59.
- Sensible heat = heat transfer with measurable temperature change. [O15-004]
- Scales: water freezes 0 °C/32 °F, boils 100 °C/212 °F (standard pressure); °F = 9/5 × °C + 32; 0 °F ≈ −17.8 °C; 37 °C = 98.6 °F; K = °C + 273.15, written "K" without degree sign. [P056-013..016]
- Instruments: maximum–minimum thermometer (Six's) retains extremes; thermograph records continuously; pyrometer estimates very high temperature from emitted radiation (furnaces, mines/industry per book); Sun's temperature from spectra and radiation laws; Bourdon tube = pressure-sensing elastic tube (used in some gauges) — book's "aircraft thermometer with spirit in Bourdon tube" mixes principles. BK p57. [P056-017 018 P057-001..004]
- Daily maximum usually mid-afternoon (~2 pm, after solar noon, because ground keeps gaining heat); minimum near sunrise (book 4 am) — weather can shift these. BK p57. [P056-019 P057-005 006]

### `#temperature-distribution`
- Horizontal distribution = variation place to place at similar height; advection moves warm/cold air; controls latitude, altitude, distance from sea, ocean currents, winds, cloud. BK p57. [P057-007..009]
- Heat zones: Torrid 23½°N–23½°S, Temperate 23½°–66½°, Frigid 66½°–90°; 5 belts; owner `lesson-02#latlong-heatzones` — fact lines here only for the book's extra subdivision: warm temperate 23½°–45°, cool temperate 45°–66½° (old textbook teaching split). BK p57. [P057-010..014]
- Environmental lapse rate = rate actual air temperature falls with height; standard ~6.5 °C/km (ISA); book 6.4 °C per 1,000 m (= 1 °C per 165 m, NCERT). [P057-015 016]
- Inversion = temperature rises with height through a layer; favoured by long clear calm winter nights, snow/ice surfaces, valleys (cold air drains down — mountain breeze), polluted city/industrial air traps smog. Book lists 4 places and calls cities "heat islands" — urban heat island is a different idea (city warmer than countryside) V wording. BK p57. [P057-017]
- Book descriptive bands (very cold <−10, cold, cool, warm, hot >30 °C) — vocabulary only. BK p57. [P057-018]
- Diurnal range = daily max − min (34 − 18 = 16 °C); large in dry deserts/interiors (strong day heating + night radiative cooling); small in humid equatorial, coastal, cloudy places. BK p57–58. [P057-019 P058-001 002]
- Annual range = mean of warmest month − mean of coldest month (do not mix a daily extreme with monthly means); largest in mid/high-latitude continental interiors (Verkhoyansk ~+15 °C Jul vs ~−45 °C Jan monthly means V; book "+38 summer"), smallest near Equator. BK p58. [P058-003..005]
- Records: owner `lesson-01#heights-temperature` (56.7 °C Death Valley; −89.2 °C Vostok; Al Azizia cancelled 2012). New here: Northern Hemisphere official low −69.6 °C, Klinck station, Greenland (22 Dec 1991; WMO 2020). Verkhoyansk −67.8 °C (1892) / Oymyakon −67.7 °C (1933) — "pole of cold", coldest inhabited places, not world record (book −67.7 at Verkhoyansk). Book's Oymyakon "−50, 500 people, reindeer" = one line colour, no numbers in fact lines. WMO. [P058-006..010]

### `#isolines`
- Isoline/isopleth = line joining equal values. Isotherm = equal temperature for same time/period; global maps use January and July. BK p58. [P058-011 012 015]
- Isotherms run broadly E–W (latitude controls insolation); bend where land meets sea (land–sea heating difference); more regular in Southern Hemisphere (more ocean). Book: bend north over oceans, south over land — teach with season (in January, N-Hemisphere: isotherms bend equatorward over continents, poleward over oceans; July reverse) V NCERT ch.9 fig. TGPSC Gr-2 2025 PYQ: a and b correct (c wrong). BK p58–59. [P058-013 014]
- Table rows: isobar–pressure; isobath–depth; isobront–thunderstorm (same phase/time or thunder days); isohaline–salinity; isohyet–precipitation over a period; isohel–sunshine; isoneph–cloudiness; isonif/isochion–snow; isoryme–frost; isochrone–equal time; isoseismal–equal earthquake intensity (magnitude vs intensity link `lesson-05#magnitude`); isotach–wind speed; isogon–wind direction (book "QVGA" OCR); isodop–equal Doppler radial velocity (zero isodop = 0 radial velocity); isohypse–equal geopotential height on a pressure surface (book uses it for contour); contour–equal elevation on topographic map; close = steep (link). BK p58–59. [P058-016..021 P059-001..009 012 014 015]
- Hypsographic curve: share of Earth's surface by elevation/depth (vertical axis elevation/depth, horizontal area %). Book "హిప్సోగ్రాఫిక్". [P059-010 011]
- Streamline: tangent at each point = instantaneous flow direction. [P059-013]

### `#pressure`
- Atmospheric pressure (వాతావరణ పీడనం) = force of the weight of the air column above unit area; barometer reads that column's effect. BK p60. [P060-001 002]
- Galileo argued air has weight (and studied pump limits); his pupil Evangelista Torricelli made the mercury barometer (1643). BK p60. [P060-003]
- Mercury barometer: pressure = height of mercury column; aneroid: no liquid, evacuated flexible metal capsule (dial, needle); barograph: graph over time; microbarograph: small/rapid changes. BK p60. [P060-004..007]
- 1 hPa = 1 mb; standard sea-level 1013.25 hPa = 760 mm Hg = 29.92 in Hg (book 1013.2). 900–1030 hPa = broad ordinary range, not limits. BK p60. [P060-009..011]
- WMO records: highest 1083.8 hPa, Agata, Krasnoyarsk, Russia, 31 Dec 1968 (below 750 m); 1089.1 hPa Tosontsengel, Mongolia, 19 Dec 2001 (above 750 m, reduced to sea level); lowest (excluding tornadoes) 870 hPa, Typhoon Tip, 12 Oct 1979. BK p60 (1083; "870"). [P060-012..014]
- Total mass of atmosphere ≈ 5.1 × 10¹⁸ kg (≈ 5.1 × 10¹⁵ tonnes); book's "56 × 10… tonnes / 56 crore tonnes" wrong. NOAA/NCAR. [P060-015]
- Pressure falls with height (less air above); "1 mb per 10 m" (book, NCERT) only near sea level. [P060-016 017]
- Heating with rising/mass redistribution → thermal low; temperature alone does not fix pressure. [P060-018]
- Water vapour molecular mass 18 vs dry air ~29 → moist air less dense at same T, P; humidity does not always lower barometric pressure. BK p60. [P060-019 020]

### `#wind-forces`
- Wind = horizontal air movement (vertical = air currents); not straight high → low because of rotation, friction, curvature. BK p69. [P069-001 002]
- Wind named by direction it comes FROM (westerly = from west); speed needs a unit (m/s, km/h, knots). [P069-003..005]
- Wind vane = direction (exposed site, ~10 m standard V); cup anemometer = speed from rotation rate; combined units exist. Beaufort scale: empirical, visual effects, 0–12 (Francis Beaufort, 1805). Upper-air: radiosonde/GPS balloon tracking, radar, remote sensing; balloon drift gives speed/direction. BK p69. [P069-006..014 033]
- Pressure gradient = pressure difference per horizontal distance; PGF acts high → low, perpendicular to isobars; isobar = line of equal pressure; close isobars → strong gradient, faster wind (not exact speed — friction, curvature, stability). BK p69. [O15-009 020 P069-015..019 026]
- Coriolis as wind force: right in N, left in S; zero at Equator; increases poleward and with speed; acts at right angles, changes direction not speed; named after Gaspard-Gustave de Coriolis; "Ferrel's law" = same rule. Owner of the effect: `lesson-02#motion-coriolis`. [O15-010 020 023 P069-022..025 027..029]
- Geostrophic wind: PGF balanced by Coriolis, parallel to isobars (upper air). Friction slows surface wind, weakens Coriolis → surface wind crosses isobars toward low; friction stronger over rough land than sea. [P069-020 021 030 P070-001..003]
- Curved flow needs inward (centripetal) acceleration; centrifugal = apparent outward force in rotating frame (book term అపకేంద్ర బలం); gradient wind = PGF + Coriolis + curvature. BK p70. [P069-031 032 P070-004 005]

### `#pressure-belts`
- Book: winds by duration — permanent (planetary), seasonal, local; monsoon = seasonal. BK p70. [P070-006 007]
- 7 belts: equatorial low (1), subtropical highs (2), subpolar lows (2), polar highs (2); idealised; shift seasonally and break over land. BK p70. [P070-008..010]
- Equatorial low: ITCZ = Inter-Tropical Convergence Zone; warm moist air rises; doldrums = weak, variable mean surface winds but vigorous convection. BK p70 (0–5°/10°). [P070-011..014]
- Subtropical highs ~25°–35° (book 23½°–35°); "horse latitudes"; descending, warming air → dry → most hot deserts (Sahara, Arabian, Thar, Kalahari, Namib, Atacama, Australian, Sonoran/Mojave) — but also cold currents, rain shadow, continentality (Patagonia = Andes rain shadow). BK p70–71. [P070-015..017 P071-001 002]
- Subpolar lows ~60° (book 45°–66½°): convergence of westerlies and polar easterlies, polar-front cyclones; polar highs: very cold dense air sinks. BK p70. [P070-018 019]

### `#planetary-winds`
- Trades: from subtropical high to equatorial low; NE in N-Hemisphere, SE in S-Hemisphere; called easterlies; steady; surface branch of Hadley cell; rain on windward east coasts/slopes, dry west sides. BK p70. [P070-020..024]
- Hadley cell (George Hadley, 1735): ITCZ ascent → poleward upper flow → subsidence ~30° → trades. BK p71. [P071-003..005]
- Westerlies: subtropical high → subpolar low, ~30°–60°; from SW (N), NW (S); disturbed by cyclones, anticyclones, jets, land; S-Hemisphere stronger, more continuous (ocean): Roaring Forties (~40°S), Furious Fifties, Shrieking/Screaming Sixties. Bring winter rain to west coasts (Mediterranean shift). BK p71. [P071-006..015]
- Ferrel cell 30°–60°: thermally indirect, maintained by mid-latitude eddies; surface flow poleward and eastward (William Ferrel, 1856). [P071-016..018]
- Polar easterlies: polar high → subpolar low; from NE (N) / SE (S); cold, weak. Polar front = where they meet westerlies → strong contrast → cyclones. Polar cell: sinking cold air over pole; smallest, weakest. BK p71. [P071-019..024]

### `#monsoon-winds`
- Seasonal winds: prevailing direction/circulation changes markedly between seasons. BK p71. [P071-025]
- Monsoon: from Arabic *mausim* (season); core = seasonal reversal of winds; rainy season is a result, not the definition. BK p92. [P092-001 002]
- Basic summer sequence: land heats faster → low pressure over land → moist ocean air flows in → rises → rain; modern view adds ITCZ shift, cross-equatorial flow, upper-air (jets, Tibetan high), relief. NCERT India Physical Env. ch.4. [P092-005 006]
- South Asia: winter NE/easterly land → ocean (dry; NE monsoon rain on Tamil Nadu and south coastal AP); summer SW ocean → land (moist); explained by seasonal pressure reorganisation + land–sea contrast + circulation shifts. BK p72. [P072-001..003]

### `#local-winds`
- Local winds from local heating/cooling and relief; strong prevailing winds can suppress/skew them. BK p72. [P072-004 005]
- Sea breeze: day, sea → land (land warms, air rises, lower pressure), return flow aloft land → sea; land breeze: night, land → sea, weaker/shallower (smaller night contrast). Valley (anabatic): day upslope; mountain (katabatic): night downslope → cold-air pooling, inversion. BK p72. [O15-011 012 015 021 P072-006..015]
- Foehn: warm, dry leeward downslope; warming by adiabatic compression on descent, plus moisture/latent heat lost on windward side; not friction; Alps; warming varies by event. Chinook: lee (east) of Rockies, USA and Canada, "snow eater". Santa Ana: Great Basin high → S. California coast, wildfires. Zonda: Argentina, lee of Andes. BK p72. [P072-016..027]
- Sirocco: Sahara/N. Africa → Mediterranean/S. Europe; hot dry dusty near Africa, humid after crossing the sea; "blood rain" = red dust in rain; regional names Ghibli (Libya), Chili (Tunisia), Khamsin (Egypt), Leveche (SE Spain); Brickfielder (SE Australia hot dry) and Black Roller (US dust) are separate names. BK p73. [P073-001..009 P096-003 004]
- Simoom/Simoon: intensely hot, dry, dust-laden desert wind (Arabia, Sahara); book month windows only tendencies. BK p73. [P073-010 011]
- Harmattan: dry, dusty NE trade wind from Sahara to W. African coast (Nov–Mar V), "Doctor wind" (relief from humidity) but dust irritates lungs. BK p73. [P073-012 013]
- Nor'westers = severe pre-monsoon convective thunderstorms; Kalbaisakhi (Bengal); West Bengal, Assam, Bihar, Jharkhand, Odisha. BK p73. [P073-014..016]
- Loo: hot dry afternoon wind, NW/N India (Punjab, Haryana, Delhi, UP), May–June; dehydration, heatstroke. BK p73. [P073-017 018]
- Mistral: cold dry N/NW wind down the Rhône valley, S. France; Bora: cold gusty downslope NE, N. Adriatic (Croatia → Italy side), book speeds 128–196 km/h; Bise (Switzerland–France, cold N/NE); Pampero (Argentina–Uruguay Pampas, cold S/SW); Norte (Mexico/Gulf, cold northerly surge); Buran, Purga (Siberia/Russian tundra, winter snowstorms); Southerly Buster (NSW coast, sudden cool southerly after heat). BK p73–74. [P073-019 020 025..028 P074-001 002 P096-001 002]
- Blizzard = severe snow + wind condition in many cold regions (N. America, Europe, Asia, polar) — not a named local wind. Berg wind = hot dry downslope/offshore (South Africa), wildfire danger — book lists it among cold winds. BK p73. [P073-021..024]
- Book names not verifiable in standard sources (Puna, Lavender, others on p74) → not taught. [P072-028 P073-029 P074-003 → retire list]
- Matching set: Sirocco–Sahara/Mediterranean; Harmattan–W. Africa; Loo–NW India; Chinook–Rockies. [P073-030]

### `#jet-streams`
- Jet stream = narrow, elongated band of very strong horizontal wind in upper troposphere/near tropopause; 3-D, speed max at core; meanders, shifts, splits, merges; mostly west → east. BK p74, NOAA. [P074-004..006 009 P077-016 017]
- Cause: strong horizontal temperature gradient (thermal wind), with Coriolis, pressure gradients, momentum, waves. [P074-007 008]
- Height ~8–14 km (book 9,000–12,000 m; lower at high latitudes). [P074-010 011]
- Subtropical jet ~30° (poleward edge of Hadley cell); polar (polar-front) jet ~50°–60° (book "40–60"/"60°"); may merge. [P074-012..014 018..020 P077-018 019]
- Speed varies; typical cores >100 km/h, strongest can exceed 400 km/h (book: average 144, up to 480 km/h); stronger in winter (greater pole–Equator contrast), weaker and poleward in summer. BK p74. [P074-015..017]
- Effects: steers storms and air masses, helps deepen lows, blocking → persistent heat/cold/drought/rain; aircraft eastbound save time/fuel; clear-air turbulence near shear zones. Monsoon: interacts (STJ south of Himalaya in winter, jumps north before onset; tropical easterly jet in summer V) but not the only cause. BK p74, NCERT India ch.4. [P074-021..025 P077-020 021]
- History: balloons in 1920s (Wasaburo Ōishi, Japan) V, term "Strahlströmung" by Heinrich Seilkopf 1939, confirmed by WWII bomber pilots (1944). [P074-026 027]
- Book APPSC Gr-1 2022 PYQ (p74) on trade winds: printed key conflicts with evidence → retire. [P074-028]

### `#humidity`
- Humidity = water vapour in air; hygrometer measures; sling psychrometer (wet/dry bulb) estimates RH. BK p61, p60. [P061-001 002 P060-008]
- Sources: evaporation ~90%, transpiration ~10% (book); sublimation = ice → vapour directly. BK p61. [P061-003 004]
- Specific humidity = vapour mass / moist-air mass (g/kg); mixing ratio = vapour / dry-air mass; absolute humidity = vapour mass per volume (g/m³), changes if air expands. BK p61. [P061-005..008]
- RH = actual vapour (pressure) / saturation vapour (pressure) × 100 (30/50 → 60%); depends on temperature; cooling raises RH; 100% = saturated; 0% = ideal no-vapour limit. BK p61. [O15-005 014 018 022 P061-009..013 015]
- Dew point = temperature to which air must cool (constant pressure, no vapour change) to saturate. BK p61 (తుషారస్థాయి). [O15-006 P061-014]
- Evaporation: liquid → vapour, absorbs latent heat; condensation: vapour → liquid, releases latent heat. [O15-007 008 019]

### `#condensation-forms`
- Snow = ice crystals/flakes; can reach ground with surface air slightly above 0 °C. BK p64. [P064-004 005]
- Frost = deposition of vapour directly as ice on surfaces below 0 °C; ground frost possible with screen air above 0 °C; frozen dew = liquid dew that froze; hoar frost (book "white frost") = deposited crystals; glaze = supercooled rain/drizzle freezing on impact. BK p64. [P064-006..009 015]
- Mist: visibility ≥1 km (WMO; upper ~5–10 km V); fog: <1 km; fog is not precipitation (droplets suspended); book "mist 1–2 km". BK p64, WMO. [P064-010..012]
- Smog = smoke + fog (term ~1905 V); photochemical smog = NOx + hydrocarbons + sunlight → ground-level ozone. BK p64. [P064-013 014]
- Sleet: US = ice pellets; British/Indian usage = rain–snow mix (book: freezes before reaching ground, road accidents). BK p64. [P064-016]
- Hail: grows in strong Cb updrafts with supercooled droplets. [P064-017]
- Virga = precipitation evaporating before reaching ground (book "DY" OCR); can precede microburst. BK p64. [P064-018 019]
- Haze: suspended fine dry particles (book's "ice-crystal curtain" wording wrong) V.

### `#clouds`
- Cloud = visible suspension of water droplets, ice crystals or both. Ceilometer measures cloud-base height; aerosol backscatter needs calibration. BK p65. [P065-001..003]
- WMO: 10 genera (book "9 types"). Temperate heights: high ~5–13 km, middle 2–7 km, low 0–2 km (WMO International Cloud Atlas; bank says 5–15); book 6–12/2–6/<2; higher in tropics, lower near poles; cumulus and Cb are not confined to one band. BK p65. [P065-004..007 P066-020 021]
- High: cirrus (ice; white delicate filaments, hooks — "mare's tails"; virga, no significant rain); cirrostratus (thin veil, halo; may signal warm front, not a guarantee); cirrocumulus (small grains/ripples, "mackerel sky", similar altocumulus pattern). Middle: altostratus (grey/bluish sheet, Sun dim; thickens into nimbostratus); altocumulus (rounded masses with shading, corona; castellanus → instability). Low: stratocumulus (lumpy rolls); nimbostratus (thick dark, continuous rain/snow); stratus (uniform grey layer, drizzle; forms by gentle cooling/lift; fog touches ground, stratus base above it; book "300 km" = ~300 m). Vertical: cumulus (flat base, cauliflower top; can grow → congestus → showers); cumulonimbus (deep convective, updraft + downdraft, heavy showers, thunder, lightning, gusts, hail; anvil = WMO "incus", flattened by stable tropopause; "king of clouds" informal; any time of day; tops 12+ km). BK p65–66. [O15-024 P065-008..023 P066-001..014 022]
- APPSC 2020 PYQ (book p66) match: cirrus–silky, cirrostratus–milky veil, cirrocumulus–small globular, cumulus–cauliflower. BK p66. [P066-022]
- Nacreous = polar stratospheric clouds (PSC), ~15–25 km, polar winter (Antarctic and Arctic); surfaces help chlorine activation → ozone depletion. BK p67. [P067-017..019]
- Noctilucent: ice clouds in mesosphere/mesopause ~76–85 km; high-latitude summer twilight; not self-luminous (sunlit); ice on meteor dust; not a Cb subtype. BK p66–67. [P066-015..019]

### `#precipitation`
- Precipitation = rain, drizzle, freezing rain, sleet, snow, hail reaching ground. BK p61. [P061-016]
- Condensation nuclei (dust, salt, smoke); cloud droplets too small to fall, must grow; precipitation may evaporate below (virga). BK p61. [O15-024 P061-017]
- Drizzle/rain boundary ~0.5 mm; raindrops ~0.5–5 mm (book); terminal speed of large drops ~9 m/s, not one speed (book 29 km/h). BK p61. [P061-018 019]
- Orographic: moist air forced up terrain, adiabatic cooling, windward rain; leeward descending air compresses, warms, RH falls → rain shadow (Western Ghats → Deccan, Rayalaseema). BK p61. [P061-020 021]
- Convectional: surface heating → buoyant ascent → adiabatic cooling → saturation → showers/thunder; frequent in equatorial belt (strong heating, moisture, instability) but not at an exact hour; Indian hot-season storms. BK p61–62. [P061-022 P062-001 002]
- Mid-latitude interiors: convection, fronts, cyclones and orographic all operate. [P062-003]
- Cyclonic rain: low-pressure convergence, ascent, cooling; both tropical and extratropical cyclones. BK p62. [P062-004 005]

### `#air-masses`
- Air mass = large body (1000s of km) with relatively uniform temperature and humidity (horizontal, synoptic scale). Source region: large uniform surface, weak disturbance, long residence. BK p75. [P075-001..005]
- Modification: cold mass over warmer surface → heat, moisture gained → unstable; warm over colder → cooled from below → stable; trajectory, travel time, surface matter. BK p75–76. [P075-006..008 P076-009..013]
- Notation: c continental (dry), m maritime (moist); P polar, T tropical; A arctic (colder, drier than P); E equatorial in some schemes (NOAA intro uses A/P/T). cP cold dry (interior Canada, Siberia); mP cool/cold moist (N. Pacific, N. Atlantic, Southern Ocean); cT hot dry (Sahara, SW USA/N. Mexico, Australian, Thar); mT warm moist (tropical Atlantic, Pacific, Indian Oceans). BK p75–77. [P075-009..024 028 P076-001..008 P077-006 007 011 012]
- cP moving south: lower layers warm, still dry; mP over warmer sea → cumuliform showers; "mP always heavy rain" wrong; mT needs lifting to rain. [P075-019 021 022 P076-008]
- k = air colder than surface (heated from below) → unstable → cumulus, showers, gusts; w = warmer than surface (cooled from below) → stable → stratus, fog, drizzle; u/s in some schemes; standard letters lowercase; order: source surface → thermal origin → k/w → u/s (cPk, mPw, cPku, cTw); longer code not "more accurate". BK p76–77. [P076-014..027 P077-001..005 008..010 013..015]
- Stability = tendency of a lifted parcel to return (stable) or keep rising (unstable); book's friction-based stability text replaced: thermal contrast primary, friction affects wind/mixing. BK p76. [P076-024..026]
- Boundary between air masses = front; jet streams steer air masses; frontal passage changes temperature, wind, pressure, precipitation. [P075-025..027]

### `#fronts`
- Front = 3-D sloping transition zone between air masses of different density/temperature/humidity; they do not mix quickly; width varies (no universal value). BK p78. [P078-001..005]
- Polar front: polar vs subtropical air, linked to mid-latitude cyclones and polar jet; ITCZ = trade-wind convergence belt, not an ordinary air-mass front. BK p78. [P078-006..009]
- Cold front: cold replaces warm, undercuts → rapid lift, narrow band of showers/thunderstorms; warm front: warm air advances, gentle slope → widespread layered cloud, steady rain; stationary: neither replaces, slow/parallel winds, prolonged cloud/rain; occluded: cold front catches warm front, warm-sector air lifted off ground. BK p78. [P078-010..020]

### `#tropical-cyclones`
- Tropical cyclone = organised, rotating, closed low-level low over tropical waters; warm core, non-frontal; anticlockwise N / clockwise S. BK p62. [P062-006 007]
- Lower central pressure → stronger gradient, but intensity judged by sustained wind. [P062-008]
- Energy: latent heat of condensation from warm-ocean moisture. Eye calm (sinking air) vs eyewall strongest winds/rain. [P062-009 010 P063-004 015]
- Genesis: SST ≥ ~26.5 °C through ~50 m (NCERT "27 °C"); Coriolis enough (rare within ~5° of Equator); low vertical wind shear; pre-existing disturbance; necessary not sufficient. BK p62, NCERT. [P062-011..014]
- Seasons: warm-season peak, varies by basin; North Indian Ocean: pre-monsoon Mar–May and post-monsoon Oct–Dec (book "May–Dec"). [P062-015 016 P063-010]
- Names: hurricane — N. Atlantic/Caribbean, NE Pacific; typhoon — NW Pacific (China, Japan, Philippines); cyclone/cyclonic storm — Indian Ocean, S. Pacific/Australia; "bagyo" generic Filipino word, Baguio a city (book "బగువోలు"); "willy-willy" Australia (TG-SI Mains 2023 PYQ → Australia; today mainly dust devils V); tornado = separate small rotating column from a thunderstorm, mostly over land (USA). BK p62, p64. [P062-017..021 P094-010 P104-004 005]
- Forms over tropical/subtropical oceans away from Equator; Cb tops near tropopause 12–15 km; size highly variable, eye ≠ storm size; isobars nearly circular; track westward in easterlies, may recurve poleward and east. [P063-002 008 012 014 017 019]
- IMD categories (max sustained 3-min wind): Depression 31–49 km/h (17–27 kt), Deep Depression 50–61, Cyclonic Storm 62–88, Severe CS 89–117, Very Severe CS 118–166, Extremely Severe CS 167–221, Super Cyclonic Storm ≥222 km/h. IMD. V.
- Naming: WMO/ESCAP Panel on Tropical Cyclones (13 members: Bangladesh, India, Iran, Maldives, Myanmar, Oman, Pakistan, Qatar, Saudi Arabia, Sri Lanka, Thailand, UAE, Yemen); list of 169 names adopted 2020; RSMC New Delhi (IMD) issues names. IMD. V (changing).

### `#temperate-cyclones`
- Extratropical cyclone: forms in mid/high-latitude baroclinic zones along the polar front as a wave on an air-mass boundary; energy from horizontal temperature contrast; warm, cold, later occluded fronts; cold-core/tilted, asymmetric; all year, stronger in cool season; ~2,000 km across (NOAA/NWS; book 1,000–3,000 km); wind/rain along fronts far from centre; isobars elongated (book "V-shaped" not universal); moves west → east in westerlies; anticlockwise N / clockwise S. BK p62–64. [P062-022 P063-001 003 005 007 009 011 013 016 018 020 P064-001..003]
- Speed: both kinds can be slow or fast — no universal ranking. Book p63 size row mixes eye diameter, storm width and height. [P063-021 023]
- Extratropical transition: warm-core tropical cyclone moving poleward becomes a frontal, baroclinic system. [P063-022]
- Anticyclone: high pressure centre, outward spiralling winds, clockwise N / anticlockwise S, subsidence → clear, dry, large day–night range. BK p64.
- APPSC Gr-1 2022 PYQ (book p64): wrong statement = "they have no clear frontal system". BK p64.
- Western Disturbances = extratropical lows bringing winter rain/snow to NW India V (one line).

---

## Changing / model-dependent facts (need `::: changing` + `::: exam` "how to answer")
| Fact | Book | Current standard | Section | How to answer |
|---|---|---|---|---|
| CO₂ share of dry air | 0.03% | ~0.042% (≈423 ppm, NOAA 2024 V) and rising | `#composition` | old-book options → 0.03%; "current" → ~0.04%; it changes every year |
| Mass in lowest layers | 99% within 39 km (OCR) | ~99% within ~30–32 km (NCERT 32) | `#composition` | pick ~30–32 km |
| IGY | 1957–62 | 1 Jul 1957–31 Dec 1958 | `#composition` | 1957–58 |
| Lapse rate | 6.4 °C/1,000 m (1 °C/165 m) | ISA 6.5 °C/km | `#temperature-distribution` | both appear; choose whichever is offered |
| Energy budget / albedo | — (NCERT 35/14/51; albedo 35) | NASA 29/23/48; albedo ~0.30 | `#insolation` | NCERT numbers in old papers; "modern NASA" → 29–30% |
| Solar constant | (old) 1.94 cal/cm²/min | TSI ~1361 W/m² (2011 revision; earlier 1366) | `#insolation` | 1361–1367 W/m² family; "~2 cal/cm²/min" old form |
| N-Hemisphere lowest | Verkhoyansk −67.7 | Klinck, Greenland −69.6 °C (WMO 2020) | `#temperature-distribution` | "official N-Hemisphere record" → Klinck; "pole of cold / coldest inhabited" → Verkhoyansk/Oymyakon |
| Pressure extremes | Agata 1083 mb; 870 mb | 1083.8 hPa (<750 m); 1089.1 hPa Tosontsengel (>750 m); 870 hPa Tip 1979 | `#pressure` | match the category in the option |
| Cloud genera | 9 | WMO 10 | `#clouds` | 10 |
| Cloud height bands | 6–12 / 2–6 / <2 km | WMO temperate 5–13 / 2–7 / 0–2 km | `#clouds` | use bands only for temperate zone; heights vary with latitude |
| Mist/fog visibility | mist 1–2 km; fog <1 km | WMO: fog <1 km, mist ≥1 km | `#condensation-forms` | <1 km = fog |
| Jet speed/height | 9–12 km; 144 / 480 km/h | 8–14 km; >400 km/h cores possible | `#jet-streams` | approximate ranges only |
| Cyclone SST threshold | — | 26.5 °C (NOAA) / 27 °C (NCERT) | `#tropical-cyclones` | either; never "20 °C" |
| N. Indian Ocean cyclone names | — | 169-name list from 2020, 13 countries (V) | `#tropical-cyclones` | as of 2025; check current affairs for new storm names |
| IMD intensity categories | — | IMD 7-step scale (V numbers) | `#tropical-cyclones` | Super Cyclonic ≥222 km/h |

## Traps (max 1 per section; real confusions only)
| Section | Trap |
|---|---|
| `#weather-climate` | Climate is not "average weather" only — it includes variability and extremes over ~30 years. |
| `#composition` | Water vapour is absent from the dry-air table, yet it is the main weather gas (0–4%). |
| `#layers` | Thermosphere is "very hot" by kinetic temperature but you would not feel heat — air is too thin. |
| `#ionosphere` | Ionosphere is not a sixth temperature layer; it overlaps mesosphere and thermosphere. |
| `#insolation` | Earth is closest to the Sun in January — seasons come from tilt, not distance. |
| `#heat-transfer` | Advection = horizontal; convection = vertical. |
| `#temperature-distribution` | Annual range uses monthly means; diurnal range uses one day's max and min. |
| `#isolines` | Isohyet = rain, isohel = sunshine, isohaline = salinity (similar spellings). |
| `#pressure` | Moist air is lighter than dry air at the same temperature and pressure. |
| `#wind-forces` | Coriolis changes direction, not speed, and is zero at the Equator. |
| `#pressure-belts` | Subtropical high and subpolar low are dynamic, not thermal, in origin. |
| `#planetary-winds` | Westerlies come FROM the west (SW in north, NW in south); trades come from the east. |
| `#monsoon-winds` | Monsoon = seasonal wind reversal, not "rain". |
| `#local-winds` | Berg is hot, not cold; Harmattan is dry, not humid. |
| `#jet-streams` | Jets are stronger in winter, not summer. |
| `#humidity` | Cooling air raises RH even though no water is added. |
| `#condensation-forms` | Fog <1 km visibility; mist ≥1 km. |
| `#clouds` | Nimbostratus gives steady rain; cumulonimbus gives thunder showers and hail. |
| `#precipitation` | Leeward rain shadow is dry because descending air warms, not because "the clouds are used up" only. |
| `#air-masses` | k = air colder than the surface → unstable (not "warm"). |
| `#fronts` | Cold front = steep, short heavy showers; warm front = gentle, long steady rain. |
| `#tropical-cyclones` | A tornado is not a tropical cyclone. |
| `#temperate-cyclones` | Temperate cyclones have fronts; mature tropical cyclones do not. |

## Question ids → section (740 in banks: 614 stay here, 126 MOVE-L09)
(Generated by work/map.py; full machine list in work/map_L08.json, work/groups.txt.)
- `#weather-climate` (4): O14-005 006 018, P056-020
- `#composition` (24): O14-009 010 011 012 015 020 021, P067-001..005, P068-016..027
- `#layers` (31): O14-001 002 003 004 013 016 017, P067-006..016 020..024 030, P068-009..015
- `#ionosphere` (14): O14-022, P067-025..029, P068-001..008
- `#insolation` (28): O15-001 002 003 013 016 017, P055-002..015, P056-001..008
- `#heat-transfer` (18): O15-004, P056-009..019, P057-001..006
- `#temperature-distribution` (23): P057-007..019, P058-001..010
- `#isolines` (26): P058-011..021, P059-001..015
- `#pressure` (20): P060-001..020
- `#wind-forces` (42): O15-009 010 020 023, P069-001..033, P070-001..005
- `#pressure-belts` (16): P070-006..019, P071-001 002
- `#planetary-winds` (27): P070-020..024, P071-003..024
- `#monsoon-winds` (8): P071-025, P072-001..003, P092-001 002 005 006
- `#local-winds` (66): O15-011 012 015 021, P072-004..028, P073-001..030, P074-001..003, P096-001..004
- `#jet-streams` (31): P074-004..028, P077-016..021
- `#humidity` (23): O15-005 006 007 008 014 018 019 022, P061-001..015
- `#condensation-forms` (16): P064-004..019
- `#clouds` (48): P065-001..023, P066-001..022, P067-017..019
- `#precipitation` (13): O15-024, P061-016..022, P062-001..005
- `#air-masses` (70): P075-001..028, P076-001..027, P077-001..015
- `#fronts` (20): P078-001..020
- `#tropical-cyclones` (19): P062-006..021, P094-010, P104-004 005
- `#temperate-cyclones` (27): P062-022, P063-001..023, P064-001..003

## MOVE-L09 (126 ids → Lesson 9; MCQ CHECK flags them MOVE-L09, link null, no fixes; record in S/pipe/L08/mcq/moves.json)
- climate statistics (6): O14-007 O14-008 O14-014 O14-019 O14-023 P055-001
- applied climatology (1): O14-024
- classification / Köppen (2): P095-011 P105-002
- tropical monsoon climate (25): P092-003 004 007..012, P093-001..012, P094-001..005
- tropical marine (4): P094-006..009
- Mediterranean (31): P095-001..010 012, P096-005..012, P097-001..012
- China / Gulf / Natal type (22): P103-001..012, P104-001..003 006..012
- British / Marine West Coast type (23): P105-001 003..012, P106-001..012
- Laurentian (12): P107-001..012
(Lesson 9 section for each id: S/pipe/L08/work/map_L09.json and S/pipe/L09/OUTLINE.md.)

Kept here although printed on climate-region pages: P092-001 002 005 006 (monsoon definition/mechanism → `#monsoon-winds`), P094-010, P104-004 005 (cyclone names → `#tropical-cyclones`), P096-001..004 (Mistral, Bora, Sirocco family → `#local-winds`).

## Retire suggestions (8)
- P072-028 — "audit decision on the book's spelling" of a wind name: meta-question about the book, no exam value.
- P073-029 — "Puna" unverified name: hold item, not a fact.
- P074-003 — Lavender/other p74 spellings: hold item.
- P074-028 — "why the printed APPSC 2022 item is excluded": meta-question.
- P073-011 — fixed months of Simoom as "audit interpretation": keep only "Simoom is hot, dry, dusty" (P073-010).
- P057-004 — Bourdon tube "misleading mixture of instrument principles": meta; P057-003 already tests Bourdon = pressure.
- P068-021 — Sputnik/Telstar chronology: space history, not atmosphere.
- P065-003 — ceilometer aerosol-backscatter calibration caution: instrument-engineering detail.
Also consider: P063-023 (problem with printed table) and P076-026 (friction–stability revision) — keep only if writers can state the correct fact in one sentence each.

## Book errors to correct in prose (one sentence each, no reviewer words)
IGY 1957–62 → 1957–58; CO₂ 0.03% → ~0.04% today; atmosphere mass "56 × 10…" → 5.1 × 10¹⁸ kg; stratus "300 km" → ~300 m; cloud genera 9 → 10; Berg listed as cold → hot; G layer; jet stream latitude "40–60" → polar jet ~50–60°; cities as "heat islands" in the inversion list (urban heat island is a different idea); mist 1–2 km → ≥1 km; Bourdon-tube aircraft thermometer; "uppercase K/W" codes; friction as cause of air-mass stability; p63 cyclone size table; Verkhoyansk −67.7 as world N-Hemisphere record (Klinck −69.6 °C); "V-shaped isobars" as rule.
