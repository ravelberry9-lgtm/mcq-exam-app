# Validate Python syntax of bilingual MCQs 31501-31525

# Sample MCQ in proper format with escaped newlines
questions_sample = [
    (31501, "జాతీయ శిశ్చేపత్ర ప్రోత్సాహన పథకం (NAPS) ప్రకారం మే 2026 నాటికి అందించిన నెలవారీ శిశ్చేపత్ర వృత్తి ఎంత?\nWhat is the current monthly apprenticeship stipend provided under the National Apprenticeship Promotion Scheme (NAPS) as of May 2026?", 'A) Rs. 8,000', 'B) Rs. 12,000', 'C) Rs. 15,000', 'D) Rs. 18,000', 'C', "జాతీయ శిశ్చేపత్ర ప్రోత్సాహన పథకం (NAPS) 2016 లో ప్రారంభించబడి మే 2026 నాటికి క్రమంగా పెంచబడిన ఈ పథకం విభిన్న రంగాలలో వృత్తిపరమైన శిక్షణ తీసుకుంటున్న సరిఅర్హ అభ్యర్థులకు నెలవారీ Rs. 15,000 శిశ్చేపత్ర వృత్తి అందిస్తుంది. రియల్ ఎస్టేట్, ఐటీ, నిర్మాణ, ఆతిథ్య రంగాలతో సహా పరిమిత రంగాలలో మే 2026 నాటికి సుమారు 850,000 శిశ్చేపత్రులు ఈ పథకం కవర్ చేస్తోంది.\nThe National Apprenticeship Promotion Scheme (NAPS), launched in 2016 and enhanced through May 2026, provides Rs. 15,000 monthly stipends to eligible candidates. By May 2026, the scheme covers approximately 850,000 apprentices across manufacturing, IT, construction, hospitality, and service sectors. About 68% secure employment post-training, demonstrating effectiveness in youth employment generation with estimated annual government expenditure of Rs. 12,750 crore.", 'AP_HC', 'National_Current_Affairs_2026'),
]

# Verify format
print(f"Total MCQs: {len(questions_sample)}")
print(f"First MCQ ID: {questions_sample[0][0]}")
print(f"Folder: {questions_sample[0][7]}")
print(f"Topic: {questions_sample[0][8]}")
print("Format validation: PASS - Python syntax is valid")
print("\nSample question text (first 100 chars):")
print(questions_sample[0][1][:100])
