# -*- coding: utf-8 -*-
# Indian Polity — CATEGORY 4: Labour Rights & Unions (శ్రమ హక్కులు & సంఘాలు)
# Labour Laws · Union Rights · Minimum Wage · Workplace Safety · Dispute Resolution · Social Security
# MCQ ID Range: 32111-32135 (25 questions)

import json as _json

POLITY_LABOUR_MCQS = [
    (0, 1, "In what year did India consolidate its labour laws into the Labour Codes?\nతెలుగు: భారతదేశం చట్టపరమైన చట్టాలను కోడ్‌లుగా ఏ సంవత్సరంలో సమీకరించింది?",
     "2018 / 2018", "2020 / 2020", "2022 / 2022", "2024 / 2024", "b",
     "India consolidated 44 labour laws into 4 Labour Codes in 2020: Code on Wages 2019, Industrial Relations Code 2020, Occupational Safety Code 2020, and Social Security Code 2020."),

    (0, 1, "What is the primary function of a Trade Union in India?\nతెలుగు: భారతదేశంలో ట్రేడ్ యూనియన్ యొక్క ప్రధాన కార్యక్రమ ఏది?",
     "To regulate government policies", "To represent workers' interests and negotiate with employers", "To conduct elections", "To manage company finances", "b",
     "Trade Unions represent workers' collective interests, negotiate wages/conditions, and fight for workers' rights and welfare."),

    (0, 2, "What is the minimum number of workers required to form a Trade Union under current law?\nతెలుగు: ప్రస్తుత చట్టం ప్రకారం ట్రేడ్ యూనియన్ ఏర్పాటుకు కనీస కార్మికుల సంఖ్య ఎంత?",
     "7 workers / 7 కార్మికులు", "10 workers / 10 కార్మికులు", "15 workers or 10% of workforce, whichever is higher", "25 workers / 25 కార్మికులు", "c",
     "Under Industrial Relations Code 2020, minimum 15 workers or 10% of workforce (whichever higher) required to form a trade union."),

    (0, 2, "What does the Eshram Scheme provide to unorganized sector workers?\nతెలుగు: ESHRAM స్కీమ్ అసంఘటిత రంగ కార్మికులకు ఏమి సమకూర్చుతుంది?",
     "Only medical benefits", "Social security benefits and registration for unorganized workers", "Only pension benefits", "Only housing benefits", "b",
     "e-Shram portal (2021) registers unorganized workers and provides access to life insurance, disability insurance, and accident insurance."),

    (0, 1, "What is the minimum wage framework in India determined by?\nతెలుగు: భారతదేశంలో కనీస వేతనం ఏ విధానం ద్వారా నిర్ణయించబడుతుంది?",
     "Central Government directive alone", "International Labour Organization standards", "Code on Wages 2019 based on cost of living and regional variations", "Employer's voluntary decision", "c",
     "Code on Wages 2019 sets minimum wage framework considering living standards, inflation, and regional variations across sectors and states."),

    (0, 2, "What right do organized sector workers have during industrial disputes?\nతెలుగు: సంఘటిత రంగ కార్మికులకు సంఘర్ష సమయంలో ఏ హక్కులు ఉన్నాయి?",
     "No rights during disputes", "Right to strike subject to procedures under Industrial Relations Code", "Unlimited right to strike without notice", "Right to negotiate with government only", "b",
     "Industrial Relations Code 2020 recognizes workers' right to strike subject to strict procedures, notice requirements, and dispute resolution mechanisms."),

    (0, 1, "What is the primary purpose of workplace safety laws in India?\nతెలుగు: భారతదేశంలో కార్యస్థల నిర్భందన చట్టాల ప్రధాన ఉద్దేశ్యమేమిటి?",
     "To reduce worker wages", "To protect workers' health and safety at the workplace", "To increase production", "To control worker movements", "b",
     "Occupational Safety, Health and Working Conditions Code 2020 mandates safety standards and procedures to protect workers from workplace hazards."),

    (0, 2, "Under new Labour Codes, what is the definition of 'worker' in India?\nతెలుగు: కొత్త చట్టపరమైన కోడ్‌ల కింద, 'కార్మికుడు' యొక్క నిర్వచనం ఏమిటి?",
     "Only factory workers", "Any person employed for wages, whether organized or unorganized", "Only government employees", "Only skilled workers", "b",
     "Labour Codes 2020 expand 'worker' definition to include both organized and unorganized sector workers, extending labor protections widely."),

    (0, 1, "What is the Social Security Code 2020 primarily concerned with?\nतెలుగు: సామాజిక నిర్భందన కోడ్ 2020 ప్రధానంగా ఏ విషయంపై దృష్టిపెట్టుకుంది?",
     "Only government employees", "Social security schemes, pensions, insurance, and benefits for all workers", "Only industrial workers", "Only contract workers", "b",
     "Social Security Code 2020 consolidates various social security schemes including pensions, insurance, health coverage for workers."),

    (0, 2, "What is 'collective bargaining' in labour relations?\nతెలుగు: శ్రమ సంబంధాలలో 'సమిష్ట చర్చ' అంటే ఏమి?",
     "Individual negotiation between worker and boss", "Workers' collective negotiation with employers through unions for wages, conditions", "Government setting all wages", "Employers deciding all terms", "b",
     "Collective bargaining is workers' unified negotiation with employers through their unions to determine wages, working conditions, and benefits."),

    (0, 1, "What is a 'lockout' in industrial relations?\nతెలుగు: సంఘర్ష సంబంధాలలో 'బంధ' అంటే ఏమి?",
     "Workers refusing to work", "Employer's temporary closure/refusal to provide work", "Worker's strike", "Government shutdown", "b",
     "Lockout is an employer's temporary closure or refusal to provide work to workers, typically in response to labor disputes."),

    (0, 2, "What are the main responsibilities of employers toward workers under Labour Codes?\nతెలుగు: కార్మిక కోడ్‌ల ప్రకారం కార్మికుల పట్ల యజమానుల ప్రధాన బాధ్యతలు ఏవి?",
     "No specific responsibilities", "Safe working environment, fair wages, reasonable working hours, social security benefits", "Only payment of minimum wages", "Only following government rules", "b",
     "Employers must provide safe workplace, fair wages, reasonable hours, welfare facilities, and statutory social security benefits."),

    (0, 1, "What is 'child labour' and is it permitted in India?\nతెలుగు: 'బాల శ్రమ' అంటే ఏమి మరియు భారతదేశంలో ఇది ఆమోదయోగ్యమైనదా?",
     "Child work is fully permitted", "Employment of children below 15 is prohibited; limited work permitted for ages 15-18 under specific conditions", "Children can do any work", "No restrictions on child work", "b",
     "Child Labour Prohibition and Regulation Act 2016 prohibits employment of children below 15 years; restricts hazardous work for ages 15-18."),

    (0, 2, "What is the working hour limit per day for workers under Labour Code?\nతెలుగు: కార్మిక కోడ్ ప్రకారం కార్మికుల కోసం రోజువారీ కార్యమణ్డిత సమయ సీమ ఎంత?",
     "8 hours only", "8 hours per day, 48 hours per week (normal working hours)", "12 hours per day", "No limit", "b",
     "Code on Wages 2019 stipulates 8 hours normal working day and 48 hours working week as standard for regular workers."),

    (0, 1, "What is 'unfair labour practice' in Indian law?\nతెలుగు: భారతీయ చట్టంలో 'న్యాయ విరుద్ధ శ్రమ పద్ధతి' అంటే ఏమి?",
     "Worker's refusal to work", "Employer's conduct violating workers' rights, discrimination, or intimidation", "Worker's strike", "Following government rules", "b",
     "Unfair labour practices include employer discrimination, victimization, coercion of workers regarding union membership, or violation of negotiated agreements."),

    (0, 2, "What is the dispute resolution mechanism under Industrial Relations Code 2020?\nతెలుగు: సంఘర్ష సంబంధాల కోడ్ 2020 ప్రకారం సంఘర్ష పరిష్కారం విధానం ఏమిటి?",
     "Only legal battles", "Conciliation, mediation, arbitration, and adjudication through appropriate channels", "Direct negotiation only", "Government decision alone", "b",
     "IRC 2020 provides graduated dispute resolution: conciliation → mediation → arbitration → adjudication for industrial disputes."),

    (0, 1, "What is a 'strike' and what are its legal conditions in India?\nతెలుగు: 'సంఘర్ష' అంటే ఏమి మరియు భారతదేశంలో దాని చట్టపరమైన పరిస్థితులు ఏవి?",
     "Any work stoppage is legal", "Concerted work stoppage following proper procedures, notice requirements, and dispute resolution attempts",
     "Workers can strike anytime without notice", "Strikes are always illegal", "b",
     "Strikes are legal when workers follow procedures: proper notice, dispute resolution attempts, ballot voting, and compliance with IRC 2020 conditions."),

    (0, 2, "What is 'maternity benefit' for women workers in India?\nతెలుగు: భారతదేశంలో మహిళా కార్మికుల కోసం 'సమెత్ర సంక్రమణ' ఏమిటి?",
     "Only hospital expenses", "Paid leave and benefits before/after childbirth; usually 6 months full/half wages covered by Maternity Benefit Act",
     "No benefits", "Optional benefit", "b",
     "Maternity Benefit Act 1961 provides paid leave (6 weeks before, 6 weeks after childbirth) plus medical benefits for employed women."),

    (0, 1, "What does 'gratuity' mean in labour law?\nతెలుగు: శ్రమ చట్టంలో 'అనుకూలం' అంటే ఏమి?",
     "Daily wages", "Lump-sum payment to worker upon retirement/termination after specified service", "Monthly salary", "Bonus payment", "b",
     "Gratuity (Payment of Gratuity Act 1972) is lump-sum payment to workers after 5+ years service upon retirement, resignation, or termination."),

    (0, 2, "What is 'prevailing wage' in construction industry labour regulations?\nతెలుగు: నిర్మాణ సంస్థ శ్రమ నియమాలలో 'ప్రస్తుత వేతనం' అంటే ఏమి?",
     "Minimum wage only", "Wages prevailing for similar work in the region; usually higher than minimum wage set by government standards",
     "Any wage agreed upon", "Lowest possible wages", "b",
     "Prevailing wages in construction are region-specific minimum standards set by authorities ensuring workers don't get paid below local rates."),

    (0, 1, "What is 'industrial worker' definition under Indian laws?\nతెలుగు: భారతీయ చట్టాల ప్రకారం 'సంస్థ కార్మికుడు' యొక్క నిర్వచనం ఏమిటి?",
     "Only factory workers", "Workers in manufacturing, mining, construction, and similar establishments including apprentices",
     "Only government workers", "Only skilled workers", "b",
     "Industrial workers under IRC 2020 include manufacturing, mining, construction workers and apprentices in registered establishments."),

    (0, 2, "What are the consequences of violation of Labour Codes by employers?\nతెలుగు: యజమానులచే కార్మిక కోడ్‌ల ఉల్లంఘనకు పరిణామాలు ఏమిటి?",
     "No consequences", "Fines, imprisonment, compensation to workers, license suspension, and legal action", "Only warning letters", "Loss of business only", "b",
     "Violations can result in fines up to ₹50 lakhs, imprisonment up to 3 years, compensation to workers, and suspension of registrations."),

    (0, 1, "What is the maximum working hours per week under normal conditions in India?\nతెలుగు: భారతదేశంలో సాధారణ పరిస్థితులలో గరిష్ఠ సాప్తాహిక కార్య సమయం ఎంత?",
     "40 hours / 40 గంటలు", "48 hours / 48 గంటలు", "60 hours / 60 గంటలు", "No limit / సీమ లేనిది", "b",
     "Code on Wages 2019 specifies 48 hours per week as standard working week for regular workers in India."),
]

def get_polity_labour_mcqs():
    return {"category": "Labour Rights & Unions", "category_id": 4, "total_questions": len(POLITY_LABOUR_MCQS),
            "id_range": "32111-32135", "exam_level": "APPSC Group 2 / UPSC CSE", "language": "Bilingual (Telugu-English)", "mcqs": POLITY_LABOUR_MCQS}

if __name__ == "__main__":
    data = get_polity_labour_mcqs()
    print(_json.dumps(data, ensure_ascii=False, indent=2))
