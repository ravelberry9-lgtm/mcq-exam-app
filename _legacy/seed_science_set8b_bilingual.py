import sqlite3, os

SOURCE = 'Science_Set8B_Light_Sound_Wave_Ext'
DB = os.path.join(os.path.dirname(__file__), 'database.db')

questions = [
    ('The speed of light in vacuum is\\nతెలుగు: శూన్యంలో కాంతి వేగం ఎంత?', '3×10^6 m/s / 3×10^6 m/s', '3×10^8 m/s / 3×10^8 m/s', '3×10^10 m/s / 3×10^10 m/s', '3×10^4 m/s / 3×10^4 m/s', 'B', 'M', '', 1),
    ('Which mirror is used in vehicle rear-view mirrors?\\nతెలుగు: వాహనాల రియర్‌వ్యూ అద్దాలలో ఏ అద్దం వాడతారు?', 'Concave / అవతల వంపు', 'Plane / సమతల', 'Convex / ఉబ్బు', 'Parabolic / పరావలయ', 'C', 'M', '', 2),
    ('A concave lens always forms a\\nతెలుగు: పుటముఖ కటకం ఎల్లప్పుడూ ఏ రకమైన ప్రతిబింబాన్ని ఏర్పరుస్తుంది?', 'Real and inverted image / వాస్తవ మరియు తలక్రిందుల ప్రతిబింబం', 'Virtual and magnified image / కల్పిత మరియు వివర్ధిత ప్రతిబింబం', 'Virtual and diminished image / కల్పిత మరియు సంకుచిత ప్రతిబింబం', 'Real and erect image / వాస్తవ మరియు నిటారు ప్రతిబింబం', 'C', 'M', '', 3),
    ('The bending of light as it passes from one medium to another is\\nతెలుగు: కాంతి ఒక మాధ్యమం నుండి మరొకదానికి వెళ్ళేటప్పుడు వంగడాన్ని ఏమంటారు?', 'Reflection / పరావర్తనం', 'Refraction / వక్రీభవనం', 'Diffraction / విభేదనం', 'Dispersion / వ్యాప్తి', 'B', 'M', '', 4),
    ('The phenomenon of splitting of white light into seven colours is\\nతెలుగు: తెల్ల కాంతి ఏడు రంగులుగా విడిపోవడాన్ని ఏమంటారు?', 'Reflection / పరావర్తనం', 'Refraction / వక్రీభవనం', 'Dispersion / వ్యాప్తి', 'Scattering / వెదజల్లడం', 'C', 'M', '', 5),
    ('Sound travels fastest in\\nతెలుగు: శబ్దం ఏ మాధ్యమంలో అత్యంత వేగంగా ప్రయాణిస్తుంది?', 'Air / గాలి', 'Water / నీరు', 'Vacuum / శూన్యం', 'Solids / ఘన పదార్థాలు', 'D', 'M', '', 6),
    ('The unit of sound intensity is\\nతెలుగు: శబ్ద తీవ్రత యొక్క ప్రమాణం ఏమిటి?', 'Hertz / హెర్ట్జ్', 'Decibel / డెసిబెల్', 'Watt / వాట్', 'Newton / న్యూటన్', 'B', 'M', '', 7),
    ('The frequency range audible to humans is\\nతెలుగు: మనుషులకు వినిపించే పౌనఃపున్య పరిధి ఏమిటి?', '20 Hz - 20000 Hz / 20 Hz - 20000 Hz', '0 Hz - 100 Hz / 0 Hz - 100 Hz', '100 Hz - 1000 Hz / 100 Hz - 1000 Hz', '20000 Hz - 40000 Hz / 20000 Hz - 40000 Hz', 'A', 'M', '', 8),
    ('Which colour has the longest wavelength?\\nతెలుగు: ఏ రంగుకు అత్యంత పొడవైన తరంగదైర్ఘ్యం ఉంటుంది?', 'Violet / ఊదా', 'Blue / నీలం', 'Green / పచ్చ', 'Red / ఎరుపు', 'D', 'M', '', 9),
    ('The Doppler effect is observed when there is relative motion between\\nతెలుగు: డాప్లర్ ప్రభావం ఎప్పుడు గమనించబడుతుంది?', 'Source and observer / మూలం మరియు పరిశీలకుడు', 'Wave and medium / తరంగం మరియు మాధ్యమం', 'Light and glass / కాంతి మరియు గాజు', 'Sound and water / శబ్దం మరియు నీరు', 'A', 'M', '', 10),
    ('A convex lens is used to correct\\nతెలుగు: కుంభాకార కటకం ఏ దోషాన్ని సరిచేస్తుంది?', 'Myopia / సమీప దృష్టి లోపం', 'Hypermetropia / దూర దృష్టి లోపం', 'Astigmatism / అసమ దృష్టి లోపం', 'Presbyopia / వయో దృష్టి లోపం', 'B', 'M', '', 11),
    ('Light is a form of\\nతెలుగు: కాంతి ఏ రకమైన శక్తి?', 'Sound energy / శబ్ద శక్తి', 'Mechanical energy / యాంత్రిక శక్తి', 'Electromagnetic energy / విద్యుదయస్కాంత శక్తి', 'Nuclear energy / అణు శక్తి', 'C', 'M', '', 12),
    ('The angle of incidence equals the angle of reflection is the law of\\nతెలుగు: పతన కోణం పరావర్తన కోణానికి సమానం అనే నియమం ఏది?', 'Refraction / వక్రీభవనం', 'Reflection / పరావర్తనం', 'Diffraction / విభేదనం', 'Dispersion / వ్యాప్తి', 'B', 'M', '', 13),
    ('Ultrasound has frequency above\\nతెలుగు: అతిశబ్దం (ultrasound) పౌనఃపున్యం ఎంతకంటే ఎక్కువగా ఉంటుంది?', '2000 Hz / 2000 Hz', '20000 Hz / 20000 Hz', '200 Hz / 200 Hz', '200000 Hz / 200000 Hz', 'B', 'M', '', 14),
    ('The persistence of sound in a room after the source stops is called\\nతెలుగు: మూలం ఆగిన తర్వాత గదిలో శబ్దం కొనసాగడాన్ని ఏమంటారు?', 'Echo / ప్రతిధ్వని', 'Reverberation / ప్రతిశ్రుతి', 'Resonance / అనునాదం', 'Diffraction / విభేదనం', 'B', 'M', '', 15),
    ('A plane mirror forms an image that is\\nతెలుగు: సమతల అద్దం ఏర్పరిచే ప్రతిబింబం ఎలా ఉంటుంది?', 'Real and inverted / వాస్తవ మరియు తలక్రిందుల', 'Virtual and diminished / కల్పిత మరియు సంకుచిత', 'Virtual and same size / కల్పిత మరియు అదే పరిమాణం', 'Real and erect / వాస్తవ మరియు నిటారు', 'C', 'M', '', 16),
    ('Which phenomenon causes the sky to appear blue?\\nతెలుగు: ఆకాశం నీలంగా కనిపించడానికి కారణమైన దృగ్విషయం ఏది?', 'Refraction / వక్రీభవనం', 'Reflection / పరావర్తనం', 'Scattering of light / కాంతి వెదజల్లడం', 'Dispersion / వ్యాప్తి', 'C', 'M', '', 17),
    ('Infrasound has frequency below\\nతెలుగు: అవ్వనోచ్చర శబ్దం (infrasound) పౌనఃపున్యం ఎంతకంటే తక్కువగా ఉంటుంది?', '20 Hz / 20 Hz', '200 Hz / 200 Hz', '2000 Hz / 2000 Hz', '20000 Hz / 20000 Hz', 'A', 'M', '', 18),
    ('The focal length of a concave mirror is\\nతెలుగు: పుటముఖ అద్దం యొక్క ఫోకల్ దూరం ఎలా ఉంటుంది?', 'Positive / ధనాత్మకం', 'Negative / ఋణాత్మకం', 'Zero / శూన్యం', 'Infinite / అనంతం', 'B', 'M', '', 19),
    ('Total internal reflection occurs when light travels from\\nతెలుగు: పూర్ణ అంతరిక పరావర్తనం ఎప్పుడు జరుగుతుంది?', 'Denser to rarer medium at critical angle / దట్టమైన మాధ్యమం నుండి తేలికైనదానికి క్రిటికల్ కోణంలో', 'Rarer to denser medium / తేలికైన నుండి దట్టమైన మాధ్యమానికి', 'Air to vacuum / గాలి నుండి శూన్యానికి', 'Water to air always / నీటి నుండి గాలికి ఎల్లప్పుడూ', 'A', 'M', '', 20),
    ('Optical fibres use the principle of\\nతెలుగు: ఆప్టికల్ ఫైబర్‌లు ఏ సూత్రాన్ని ఉపయోগిస్తాయి?', 'Reflection / పరావర్తనం', 'Total internal reflection / పూర్ణ అంతరిక పరావర్తనం', 'Refraction / వక్రీభవనం', 'Diffraction / విభేదనం', 'B', 'M', '', 21),
    ('Resonance occurs when applied frequency equals\\nతెలుగు: అనువర్తిత పౌనఃపున్యం ఏదానికి సమానమైనప్పుడు అనునాదం కలుగుతుంది?', 'Half the natural frequency / సహజ పౌనఃపున్యం సగం', 'Natural frequency of object / వస్తువు యొక్క సహజ పౌనఃపున్యం', 'Double the natural frequency / సహజ పౌనఃపున్యం రెట్టింపు', 'Speed of sound / శబ్ద వేగం', 'B', 'M', '', 22),
    ('Which lens is used in a magnifying glass?\\nతెలుగు: వివర్ధక కటకంలో (magnifying glass) ఏ కటకం వాడతారు?', 'Concave lens / పుటముఖ కటకం', 'Convex lens / కుంభాకార కటకం', 'Plane glass / సమతల గాజు', 'Bifocal lens / ద్వినాభి కటకం', 'B', 'M', '', 23),
    ('SONAR stands for\\nతెలుగు: SONAR అంటే ఏమిటి?', 'Sound navigation and ranging / శబ్ద నావిగేషన్ మరియు పరిధి కొలత', 'Sound observation and recording / శబ్ద పరిశీలన మరియు రికార్డింగ్', 'Sound output and analysis reactor / శబ్ద అవుట్పుట్ విశ్లేషణ', 'Solar navigation and radio / సోలార్ నావిగేషన్ రేడియో', 'A', 'M', '', 24),
    ('The colour of light depends on its\\nతెలుగు: కాంతి రంగు దేనిపై ఆధారపడి ఉంటుంది?', 'Amplitude / వ్యాప్తి', 'Frequency / పౌనఃపున్యం', 'Speed / వేగం', 'Phase / దశ', 'B', 'M', '', 25),
    ('A periscope uses\\nతెలుగు: పెరిస్కోప్ ఏ నియమాన్ని ఉపయోగిస్తుంది?', 'Two prisms or plane mirrors / రెండు ప్రిజాలు లేదా సమతల అద్దాలు', 'Convex lenses / కుంభాకార కటకాలు', 'Concave mirrors / పుటముఖ అద్దాలు', 'Optical fibres / ఆప్టికల్ ఫైబర్లు', 'A', 'M', '', 26),
    ('Echo is heard when sound reflects from\\nతెలుగు: ప్రతిధ్వని ఎప్పుడు వినిపిస్తుంది?', 'A wall at least 17 m away / కనీసం 17 మీ దూరంలో గోడ నుండి పరావర్తనం అయినప్పుడు', 'Any object / ఏ వస్తువు నుండి అయినా', 'Only from water / నీటి నుండి మాత్రమే', 'Only in space / అంతరిక్షంలో మాత్రమే', 'A', 'M', '', 27),
    ('The phenomenon of light bending around obstacles is\\nతెలుగు: కాంతి అడ్డంకుల చుట్టూ వంగడాన్ని ఏమంటారు?', 'Refraction / వక్రీభవనం', 'Reflection / పరావర్తనం', 'Diffraction / విభేదనం', 'Polarisation / ధ్రువీభవనం', 'C', 'M', '', 28),
    ('The SI unit of frequency is\\nతెలుగు: పౌనఃపున్యం యొక్క SI ప్రమాణం ఏమిటి?', 'Decibel / డెసిబెల్', 'Hertz / హెర్ట్జ్', 'Ampere / ఆంపియర్', 'Pascal / పాస్కల్', 'B', 'M', '', 29),
    ('The process by which light vibrations are restricted to one plane is\\nతెలుగు: కాంతి కంపనాలను ఒక తలంలో మాత్రమే పరిమితం చేయడాన్ని ఏమంటారు?', 'Diffraction / విభేదనం', 'Interference / వ్యతికరణం', 'Polarisation / ధ్రువీభవనం', 'Scattering / వెదజల్లడం', 'C', 'M', '', 30),
    ('A myopic person is prescribed\\nతెలుగు: సమీప దృష్టి లోపం గల వ్యక్తికి ఏ కటకం సూచిస్తారు?', 'Convex lens / కుంభాకార కటకం', 'Concave lens / పుటముఖ కటకం', 'Plane glass / సమతల గాజు', 'Bifocal lens / ద్వినాభి కటకం', 'B', 'M', '', 31),
    ('The speed of sound in air at 0°C is approximately\\nతెలుగు: 0°C వద్ద గాలిలో శబ్ద వేగం సుమారు ఎంత?', '330 m/s / 330 m/s', '200 m/s / 200 m/s', '500 m/s / 500 m/s', '1000 m/s / 1000 m/s', 'A', 'M', '', 32),
    ('Visible light spectrum ranges from\\nతెలుగు: కనిపించే కాంతి వర్ణపటం ఏ పరిధిలో ఉంటుంది?', '100 nm to 400 nm / 100 nm నుండి 400 nm', '400 nm to 700 nm / 400 nm నుండి 700 nm', '700 nm to 1000 nm / 700 nm నుండి 1000 nm', '1 nm to 10 nm / 1 nm నుండి 10 nm', 'B', 'M', '', 33),
    ('In a convex mirror, the image is always\\nతెలుగు: ఉబ్బు అద్దంలో ప్రతిబింబం ఎల్లప్పుడూ ఎలా ఉంటుంది?', 'Real and inverted / వాస్తవ మరియు తలక్రిందుల', 'Virtual erect and diminished / కల్పిత నిటారు మరియు సంకుచిత', 'Real erect and magnified / వాస్తవ నిటారు మరియు వివర్ధిత', 'Virtual inverted / కల్పిత తలక్రిందుల', 'B', 'M', '', 34),
    ('Sound cannot travel through\\nతెలుగు: శబ్దం ఏ మాధ్యమం గుండా ప్రయాణించలేదు?', 'Air / గాలి', 'Water / నీరు', 'Vacuum / శూన్యం', 'Steel / ఉక్కు', 'C', 'M', '', 35),
    ('The critical angle depends on\\nతెలుగు: క్రిటికల్ కోణం దేనిపై ఆధారపడి ఉంటుంది?', 'Refractive index of the medium / మాధ్యమం యొక్క వక్రీభవన సూచిక', 'Speed of light / కాంతి వేగం', 'Colour of light / కాంతి రంగు', 'Angle of incidence / పతన కోణం', 'A', 'M', '', 36),
    ('Laser is an example of\\nతెలుగు: లేజర్ ఏ రకమైన కాంతికి ఉదాహరణ?', 'Incoherent light / అసంగత కాంతి', 'Coherent monochromatic light / సంగత ఏకవర్ణ కాంతి', 'White light / తెల్ల కాంతి', 'Diffracted light / విభేదిత కాంతి', 'B', 'M', '', 37),
    ('Rainbows are formed due to\\nతెలుగు: ఇంద్రధనుస్సు ఏ దృగ్విషయం వల్ల ఏర్పడుతుంది?', 'Reflection only / కేవలం పరావర్తనం', 'Refraction only / కేవలం వక్రీభవనం', 'Dispersion refraction and reflection / వ్యాప్తి వక్రీభవనం మరియు పరావర్తనం', 'Diffraction only / కేవలం విభేదనం', 'C', 'M', '', 38),
    ('Beats in sound are produced due to\\nతెలుగు: శబ్దంలో బీట్స్ ఏ కారణంగా ఉత్పత్తి అవుతాయి?', 'Same frequencies / ఒకే పౌనఃపున్యాలు', 'Slightly different frequencies / స్వల్పంగా వేర్వేరు పౌనఃపున్యాలు', 'Very different frequencies / చాలా వేర్వేరు పౌనఃపున్యాలు', 'Same amplitudes / ఒకే వ్యాప్తులు', 'B', 'M', '', 39),
    ('The power of a lens is measured in\\nతెలుగు: కటకం యొక్క శక్తిని ఏ ప్రమాణంలో కొలుస్తారు?', 'Metre / మీటర్', 'Dioptre / డయాప్టర్', 'Watt / వాట్', 'Hertz / హెర్ట్జ్', 'B', 'M', '', 40),
    ('The phenomenon of light spreading into regions of shadow is\\nతెలుగు: కాంతి నీడ ప్రాంతాలలోకి వ్యాపించే దృగ్విషయం ఏది?', 'Dispersion / వ్యాప్తి', 'Polarisation / ధ్రువీభవనం', 'Diffraction / విభేదనం', 'Interference / వ్యతికరణం', 'C', 'M', '', 41),
    ('UV rays have wavelength\\nతెలుగు: UV కిరణాల తరంగదైర్ఘ్యం?', 'Greater than visible light / కనిపించే కాంతి కంటే ఎక్కువ', 'Less than visible light / కనిపించే కాంతి కంటే తక్కువ', 'Same as visible light / కనిపించే కాంతికి సమానం', 'Same as infrared / పరారుణ కంటే సమానం', 'B', 'M', '', 42),
    ('A kaleidoscope uses\\nతెలుగు: కాలిడోస్కోప్ ఏ సూత్రాన్ని ఉపయోగిస్తుంది?', 'Refraction / వక్రీభవనం', 'Multiple reflections / బహు పరావర్తనాలు', 'Dispersion / వ్యాప్తి', 'Total internal reflection / పూర్ణ అంతరిక పరావర్తనం', 'B', 'M', '', 43),
    ('The loudness of sound depends on its\\nతెలుగు: శబ్దం గాఢత దేనిపై ఆధారపడి ఉంటుంది?', 'Frequency / పౌనఃపున్యం', 'Amplitude / వ్యాప్తి', 'Speed / వేగం', 'Wavelength / తరంగదైర్ఘ్యం', 'B', 'M', '', 44),
    ('Gamma rays have the\\nతెలుగు: గామా కిరణాలకు ఏమి ఉంటుంది?', 'Longest wavelength / అత్యంత పొడవైన తరంగదైర్ఘ్యం', 'Shortest wavelength / అత్యంత తక్కువ తరంగదైర్ఘ్యం', 'Medium wavelength / మధ్యమ తరంగదైర్ఘ్యం', 'Same as X-rays / X-కిరణాలకు సమానం', 'B', 'M', '', 45),
    ('When two waves interfere constructively the resultant amplitude\\nతెలుగు: రెండు తరంగాలు రచనాత్మకంగా వ్యతికరించినప్పుడు ఫలిత వ్యాప్తి?', 'Decreases / తగ్గుతుంది', 'Increases / పెరుగుతుంది', 'Remains same / అలాగే ఉంటుంది', 'Becomes zero / శూన్యమవుతుంది', 'B', 'M', '', 46),
    ('The splitting of white light by a prism is due to\\nతెలుగు: ప్రిజం ద్వారా తెల్ల కాంతి విడిపోవడానికి కారణం?', 'Different speeds of different colours / వేర్వేరు రంగుల వేర్వేరు వేగాలు', 'Same speed of all colours / అన్ని రంగుల ఒకే వేగం', 'Reflection by the prism / ప్రిజం ద్వారా పరావర్తనం', 'Absorption by the prism / ప్రిజం ద్వారా శోషణ', 'A', 'M', '', 47),
    ('RADAR uses which type of waves?\\nతెలుగు: రాడార్ ఏ రకమైన తరంగాలను వాడుతుంది?', 'Sound waves / శబ్ద తరంగాలు', 'Radio waves / రేడియో తరంగాలు', 'Light waves / కాంతి తరంగాలు', 'UV waves / UV తరంగాలు', 'B', 'M', '', 48),
    ('The image formed by a convex mirror is\\nతెలుగు: ఉబ్బు అద్దం ద్వారా ఏర్పడే ప్రతిబింబం ఎలా ఉంటుంది?', 'Always behind the mirror / ఎల్లప్పుడూ అద్దం వెనక', 'Always in front of the mirror / ఎల్లప్పుడూ అద్దం ముందు', 'At the focus / ఫోకస్ వద్ద', 'At infinity / అనంతంలో', 'A', 'M', '', 49),
    ('The process by which sound of one frequency causes another body to vibrate at same frequency is\\nతెలుగు: ఒక పౌనఃపున్యపు శబ్దం మరో వస్తువును అదే పౌనఃపున్యంలో కంపింపజేయడాన్ని ఏమంటారు?', 'Reverberation / ప్రతిశ్రుతి', 'Resonance / అనునాదం', 'Echo / ప్రతిధ్వని', 'Doppler effect / డాప్లర్ ప్రభావం', 'B', 'M', '', 50),
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