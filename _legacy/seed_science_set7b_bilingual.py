import sqlite3, os

SOURCE = 'Science_Set7B_Measurements_Units_Ext'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    ('The SI unit of electric current is\\nతెలుగు: విద్యుత్ ప్రవాహం యొక్క SI ప్రమాణం ఏమిటి?', 'Volt / వోల్ట్', 'Watt / వాట్', 'Ampere / ఆంపియర్', 'Ohm / ఓమ్', 'C', 'M', '', 1),
    ('Which instrument measures atmospheric pressure?\\nతెలుగు: వాతావరణ పీడనాన్ని కొలవడానికి ఏ పరికరం వాడతారు?', 'Thermometer / థర్మామీటర్', 'Barometer / బారోమీటర్', 'Hygrometer / హైగ్రోమీటర్', 'Anemometer / అనెమోమీటర్', 'B', 'M', '', 2),
    ('The SI unit of temperature is\\nతెలుగు: ఉష్ణోగ్రత యొక్క SI ప్రమాణం ఏమిటి?', 'Celsius / సెల్సియస్', 'Fahrenheit / ఫారన్‌హీట్', 'Kelvin / కెల్విన్', 'Rankine / రాంకిన్', 'C', 'M', '', 3),
    ('One nanometre equals\\nతెలుగు: ఒక నానోమీటర్ ఎంత?', '10^-6 m / 10^-6 m', '10^-9 m / 10^-9 m', '10^-12 m / 10^-12 m', '10^-3 m / 10^-3 m', 'B', 'M', '', 4),
    ('The instrument used to measure blood pressure is\\nతెలుగు: రక్తపోటు కొలవడానికి ఉపయోగించే పరికరం ఏమిటి?', 'Stethoscope / స్టెతస్కోప్', 'Sphygmomanometer / స్ఫైగ్మోమానోమీటర్', 'ECG / ECG', 'Thermometer / థర్మామీటర్', 'B', 'M', '', 5),
    ('The unit of electrical resistance is\\nతెలుగు: విద్యుత్ నిరోధం యొక్క ప్రమాణం ఏమిటి?', 'Volt / వోల్ట్', 'Ampere / ఆంపియర్', 'Ohm / ఓమ్', 'Watt / వాట్', 'C', 'M', '', 6),
    ('Mach number measures\\nతెలుగు: మాక్ నంబర్ దేనిని కొలుస్తుంది?', 'Speed relative to sound / శబ్ద వేగానికి సాపేక్ష వేగం', 'Electric charge / విద్యుత్ భారం', 'Magnetic field / అయస్కాంత క్షేత్రం', 'Temperature / ఉష్ణోగ్రత', 'A', 'M', '', 7),
    ('The SI unit of luminous intensity is\\nతెలుగు: కాంతి తీవ్రత యొక్క SI ప్రమాణం ఏమిటి?', 'Lux / లక్స్', 'Lumen / ల్యూమెన్', 'Candela / కాండెలా', 'Watt / వాట్', 'C', 'M', '', 8),
    ('Richter scale measures\\nతెలుగు: రిక్టర్ స్కేల్ దేనిని కొలుస్తుంది?', 'Wind speed / గాలి వేగం', 'Earthquake intensity / భూకంప తీవ్రత', 'Temperature / ఉష్ణోగ్రత', 'Sound level / శబ్ద స్థాయి', 'B', 'M', '', 9),
    ('One light year is the distance\\nతెలుగు: ఒక కాంతి సంవత్సరం అంటే ఏ దూరం?', 'Light travels in one year / కాంతి ఒక సంవత్సరంలో ప్రయాణించే దూరం', 'Between Earth and Sun / భూమి మరియు సూర్యుని మధ్య దూరం', 'Between Earth and Moon / భూమి మరియు చంద్రుని మధ్య దూరం', 'Diameter of Milky Way / పాలపుంత వ్యాసం', 'A', 'M', '', 10),
    ('The unit of frequency is\\nతెలుగు: పౌనఃపున్యం యొక్క ప్రమాణం ఏమిటి?', 'Decibel / డెసిబెల్', 'Hertz / హెర్ట్జ్', 'Joule / జూల్', 'Tesla / టెస్లా', 'B', 'M', '', 11),
    ('The instrument to measure wind speed is\\nతెలుగు: గాలి వేగాన్ని కొలవడానికి ఉపయోగించే పరికరం ఏది?', 'Barometer / బారోమీటర్', 'Hygrometer / హైగ్రోమీటర్', 'Anemometer / అనెమోమీటర్', 'Seismograph / సీస్మోగ్రాఫ్', 'C', 'M', '', 12),
    ('The CGS unit of force is\\nతెలుగు: బలం యొక్క CGS ప్రమాణం ఏమిటి?', 'Newton / న్యూటన్', 'Dyne / డైన్', 'Joule / జూల్', 'Pascal / పాస్కల్', 'B', 'M', '', 13),
    ('One astronomical unit is approximately\\nతెలుగు: ఒక ఖగోళ ప్రమాణం (AU) సుమారు ఎంత?', 'Distance from Earth to Moon / భూమి నుండి చంద్రుని దూరం', 'Distance from Earth to Sun / భూమి నుండి సూర్యుని దూరం', 'Distance from Sun to Mars / సూర్యుని నుండి అంగారకుని దూరం', 'Diameter of Earth / భూమి వ్యాసం', 'B', 'M', '', 14),
    ('The unit of magnetic flux density is\\nతెలుగు: అయస్కాంత అభివాహ సాంద్రత యొక్క ప్రమాణం ఏమిటి?', 'Ampere / ఆంపియర్', 'Weber / వెబర్', 'Tesla / టెస్లా', 'Gauss / గాస్', 'C', 'M', '', 15),
    ('Calorie is a unit of\\nతెలుగు: కేలరీ ఏ రాశి యొక్క ప్రమాణం?', 'Power / శక్తి (వ్యాప్తి)', 'Heat energy / ఉష్ణ శక్తి', 'Pressure / పీడనం', 'Volume / ఘనపరిమాణం', 'B', 'M', '', 16),
    ('The Kelvin scale starts at\\nతెలుగు: కెల్విన్ స్కేల్ ఏ బిందువు నుండి మొదలవుతుంది?', '0°C / 0°C', '100°C / 100°C', 'Absolute zero / సంపూర్ణ శూన్యం (-273.15°C)', 'Boiling point of water / నీటి మరుగు స్థానం', 'C', 'M', '', 17),
    ('The instrument used to measure humidity is\\nతెలుగు: తేమ కొలవడానికి ఉపయోగించే పరికరం ఏది?', 'Thermometer / థర్మామీటర్', 'Barometer / బారోమీటర్', 'Hygrometer / హైగ్రోమీటర్', 'Rain gauge / వర్షమాపని', 'C', 'M', '', 18),
    ('The prefix "mega" represents\\nతెలుగు: "మెగా" అనే ముందు అనుబంధం ఏమి సూచిస్తుంది?', '10^3 / 10^3', '10^6 / 10^6', '10^9 / 10^9', '10^12 / 10^12', 'B', 'M', '', 19),
    ('The SI unit of amount of substance is\\nతెలుగు: పదార్థ పరిమాణం యొక్క SI ప్రమాణం ఏమిటి?', 'Kilogram / కిలోగ్రాం', 'Mole / మోల్', 'Litre / లీటర్', 'Gram / గ్రాం', 'B', 'M', '', 20),
    ('The unit of power is\\nతెలుగు: శక్తి (power) యొక్క ప్రమాణం ఏమిటి?', 'Joule / జూల్', 'Watt / వాట్', 'Newton / న్యూటన్', 'Pascal / పాస్కల్', 'B', 'M', '', 21),
    ('The boiling point of water on the Kelvin scale is\\nతెలుగు: కెల్విన్ స్కేల్‌లో నీటి మరుగు స్థానం ఎంత?', '373 K / 373 K', '273 K / 273 K', '100 K / 100 K', '212 K / 212 K', 'A', 'M', '', 22),
    ('The SI unit of electric charge is\\nతెలుగు: విద్యుత్ భారం యొక్క SI ప్రమాణం ఏమిటి?', 'Ampere / ఆంపియర్', 'Volt / వోల్ట్', 'Coulomb / కూలంబ్', 'Farad / ఫారాడ్', 'C', 'M', '', 23),
    ('The instrument used to measure the depth of the ocean is\\nతెలుగు: సమద్రగర్భ లోతు కొలవడానికి ఉపయోగించే పరికరం ఏది?', 'Sonar / సోనార్', 'Radar / రాడార్', 'Altimeter / అల్టీమీటర్', 'Seismograph / సీస్మోగ్రాఫ్', 'A', 'M', '', 24),
    ('One parsec is equal to approximately\\nతెలుగు: ఒక పార్సెక్ సుమారు ఎంత కాంతి సంవత్సరాలకు సమానం?', '1 / 1', '2.26 / 2.26', '3.26 / 3.26', '10 / 10', 'C', 'M', '', 25),
    ('The unit of capacitance is\\nతెలుగు: కెపాసిటెన్స్ యొక్క ప్రమాణం ఏమిటి?', 'Henry / హెన్రీ', 'Farad / ఫారాడ్', 'Ohm / ఓమ్', 'Weber / వెబర్', 'B', 'M', '', 26),
    ('The instrument used to measure small distances precisely is\\nతెలుగు: చిన్న దూరాలను ఖచ్చితంగా కొలవడానికి ఉపయోగించే పరికరం ఏది?', 'Odometer / ఒడోమీటర్', 'Screw gauge / స్క్రూ గేజ్', 'Speedometer / స్పీడోమీటర్', 'Altimeter / అల్టీమీటర్', 'B', 'M', '', 27),
    ('The decibel scale measures\\nతెలుగు: డెసిబెల్ స్కేల్ దేనిని కొలుస్తుంది?', 'Light intensity / కాంతి తీవ్రత', 'Sound intensity / శబ్ద తీవ్రత', 'Temperature / ఉష్ణోగ్రత', 'Pressure / పీడనం', 'B', 'M', '', 28),
    ('The unit of inductance is\\nతెలుగు: ఇండక్టెన్స్ యొక్క ప్రమాణం ఏమిటి?', 'Farad / ఫారాడ్', 'Ohm / ఓమ్', 'Henry / హెన్రీ', 'Tesla / టెస్లా', 'C', 'M', '', 29),
    ('A galvanometer is used to detect\\nతెలుగు: గాల్వనోమీటర్ దేనిని గుర్తిస్తుంది?', 'Pressure / పీడనం', 'Small electric currents / చిన్న విద్యుత్ ప్రవాహాలు', 'Temperature / ఉష్ణోగ్రత', 'Magnetic field / అయస్కాంత క్షేత్రం', 'B', 'M', '', 30),
    ('The SI unit of pressure is\\nతెలుగు: పీడనం యొక్క SI ప్రమాణం ఏమిటి?', 'Bar / బార్', 'Atmosphere / వాతావరణం', 'Pascal / పాస్కల్', 'Torr / టోర్', 'C', 'M', '', 31),
    ('The instrument used to measure earthquake waves is\\nతెలుగు: భూకంప తరంగాలు కొలవడానికి ఉపయోగించే పరికరం ఏది?', 'Barometer / బారోమీటర్', 'Seismograph / సీస్మోగ్రాఫ్', 'Hygrometer / హైగ్రోమీటర్', 'Anemometer / అనెమోమీటర్', 'B', 'M', '', 32),
    ('The unit of work is\\nతెలుగు: పని యొక్క ప్రమాణం ఏమిటి?', 'Watt / వాట్', 'Newton / న్యూటన్', 'Joule / జూల్', 'Pascal / పాస్కల్', 'C', 'M', '', 33),
    ('One millilitre equals\\nతెలుగు: ఒక మిల్లీలీటర్ ఎంత?', '1 cm^3 / 1 cm^3', '10 cm^3 / 10 cm^3', '100 cm^3 / 100 cm^3', '0.1 cm^3 / 0.1 cm^3', 'A', 'M', '', 34),
    ('Luminosity is measured in\\nతెలుగు: ప్రకాశమానత ఏ ప్రమాణంలో కొలుస్తారు?', 'Watt / వాట్', 'Candela / కాండెలా', 'Lumen / ల్యూమెన్', 'Lux / లక్స్', 'C', 'M', '', 35),
    ('The prefix micro represents\\nతెలుగు: "మైక్రో" అనే ముందు అనుబంధం ఏమి సూచిస్తుంది?', '10^-3 / 10^-3', '10^-6 / 10^-6', '10^-9 / 10^-9', '10^-12 / 10^-12', 'B', 'M', '', 36),
    ('An altimeter is used to measure\\nతెలుగు: అల్టీమీటర్ దేనిని కొలుస్తుంది?', 'Ocean depth / సముద్ర లోతు', 'Altitude / ఎత్తు', 'Wind speed / గాలి వేగం', 'Humidity / తేమ', 'B', 'M', '', 37),
    ('The SI base unit of mass is\\nతెలుగు: ద్రవ్యరాశి యొక్క SI మూల ప్రమాణం ఏమిటి?', 'Gram / గ్రాం', 'Pound / పౌండ్', 'Kilogram / కిలోగ్రాం', 'Tonne / టన్', 'C', 'M', '', 38),
    ('Volt is the unit of\\nతెలుగు: వోల్ట్ ఏ రాశి యొక్క ప్రమాణం?', 'Current / విద్యుత్ ప్రవాహం', 'Resistance / నిరోధం', 'Electric potential / విద్యుత్ పొటెన్షియల్', 'Capacitance / కెపాసిటెన్స్', 'C', 'M', '', 39),
    ('The instrument used to study spectra is\\nతెలుగు: వర్ణపటాలను అధ్యయనం చేయడానికి ఉపయోగించే పరికరం ఏది?', 'Microscope / సూక్ష్మదర్శిని', 'Spectroscope / స్పెక్ట్రోస్కోప్', 'Telescope / దూరదర్శిని', 'Periscope / పెరిస్కోప్', 'B', 'M', '', 40),
    ('One horsepower equals approximately\\nతెలుగు: ఒక హార్స్‌పవర్ సుమారు ఎంత వాట్లకు సమానం?', '746 W / 746 W', '1000 W / 1000 W', '500 W / 500 W', '246 W / 246 W', 'A', 'M', '', 41),
    ('The SI unit of solid angle is\\nతెలుగు: ఘన కోణం యొక్క SI ప్రమాణం ఏమిటి?', 'Radian / రేడియన్', 'Degree / డిగ్రీ', 'Steradian / స్టెరేడియన్', 'Gradian / గ్రేడియన్', 'C', 'M', '', 42),
    ('A lactometer is used to measure\\nతెలుగు: లాక్టోమీటర్ దేనిని కొలుస్తుంది?', 'Temperature of milk / పాల ఉష్ణోగ్రత', 'Purity of milk / పాల స్వచ్ఛత', 'Volume of milk / పాల ఘనపరిమాణం', 'Colour of milk / పాల రంగు', 'B', 'M', '', 43),
    ('The unit of luminous flux is\\nతెలుగు: కాంతి ప్రవాహం యొక్క ప్రమాణం ఏమిటి?', 'Candela / కాండెలా', 'Lux / లక్స్', 'Lumen / ల్యూమెన్', 'Watt / వాట్', 'C', 'M', '', 44),
    ('The instrument used to measure angles is\\nతెలుగు: కోణాలు కొలవడానికి ఉపయోగించే పరికరం ఏది?', 'Vernier caliper / వెర్నియర్ కాలిపర్', 'Sextant / సెక్స్టెంట్', 'Theodolite / థియోడోలైట్', 'Both B and C / B మరియు C రెండూ', 'D', 'M', '', 45),
    ('Nano is equal to\\nతెలుగు: నానో అంటే ఎంత?', '10^-6 / 10^-6', '10^-9 / 10^-9', '10^-12 / 10^-12', '10^-15 / 10^-15', 'B', 'M', '', 46),
    ('The instrument used to measure rainfall is\\nతెలుగు: వర్షపాతాన్ని కొలవడానికి ఉపయోగించే పరికరం ఏది?', 'Barometer / బారోమీటర్', 'Anemometer / అనెమోమీటర్', 'Rain gauge / వర్షమాపని', 'Hygrometer / హైగ్రోమీటర్', 'C', 'M', '', 47),
    ('Which unit is used to measure the wavelength of light?\\nతెలుగు: కాంతి తరంగదైర్ఘ్యాన్ని కొలవడానికి ఉపయోగించే ప్రమాణం ఏది?', 'Metre / మీటర్', 'Nanometre / నానోమీటర్', 'Kilometre / కిలోమీటర్', 'Centimetre / సెంటీమీటర్', 'B', 'M', '', 48),
    ('The unit of electric energy consumed is\\nతెలుగు: వినియోగించిన విద్యుత్ శక్తి యొక్క ప్రమాణం ఏది?', 'Watt / వాట్', 'Joule / జూల్', 'Kilowatt-hour / కిలోవాట్-గంట', 'Ampere / ఆంపియర్', 'C', 'M', '', 49),
    ('The instrument used to measure specific gravity of liquids is\\nతెలుగు: ద్రవాల నిర్దిష్ట గురుత్వాన్ని కొలవడానికి ఉపయోగించే పరికరం ఏది?', 'Lactometer / లాక్టోమీటర్', 'Hydrometer / హైడ్రోమీటర్', 'Barometer / బారోమీటర్', 'Thermometer / థర్మామీటర్', 'B', 'M', '', 50),
]

def seed():
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute("DELETE FROM questions WHERE source_file=?", (SOURCE,))
    cur.executemany(
        """INSERT INTO questions (folder,topic,source_file,question_text,option_a,option_b,option_c,option_d,correct_answer,difficulty,explanation,question_order)
           VALUES ('GK','General_Science',?,?,?,?,?,?,?,?,?,?)""",
        [(SOURCE, *q) for q in questions])
    con.commit()
    n = cur.execute("SELECT COUNT(*) FROM questions WHERE source_file=?",(SOURCE,)).fetchone()[0]
    con.close(); print(f"Inserted {n} from {SOURCE}")

if __name__ == '__main__': seed()