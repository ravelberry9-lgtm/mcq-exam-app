# -*- coding: utf-8 -*-
# Polity MCQs - Regenerated with seed() function
# Total: 61 questions

import os
import sqlite3
import psycopg2
import psycopg2.extras

DATABASE_URL = os.environ.get("DATABASE_URL", "")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
USE_POSTGRES = bool(DATABASE_URL)

POLITY_MCQS = [
    {
        "id": 32136,
        "question_text": 'In which year was the Consumer Protection Act 1986 replaced by a new Act?',
        "option_a": '2015',
        "option_b": '2018',
        "option_c": '2019',
        "option_d": '2020',
        "correct_answer": "C",
        "explanation": 'CPA 2019 replaced 1986 Act with enhanced protections, stricter penalties, faster dispute resolution.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32137,
        "question_text": 'What are the three main categories of consumer rights?',
        "option_a": 'Buying, Selling, Trading',
        "option_b": 'Safety, Information, Choice',
        "option_c": 'Complaint, Refund, Compensation',
        "option_d": 'Quality, Credit, Dispute',
        "correct_answer": "B",
        "explanation": 'CPA 2019 ensures: Safety (hazard protection), Information (disclosure), Choice (product selection freedom).',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32138,
        "question_text": "What is FSSAI's role in consumer protection?",
        "option_a": 'Regulate transportation',
        "option_b": 'Ensure food safety and standards',
        "option_c": 'Regulate consumer disputes',
        "option_d": 'Manage import-export',
        "correct_answer": "B",
        "explanation": 'FSSAI regulates food safety, ensures quality standards, protects consumers from adulterated/unsafe food.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32139,
        "question_text": 'Time limit for filing consumer complaint under CPA 2019?',
        "option_a": '1 year',
        "option_b": '2 years',
        "option_c": '3 years',
        "option_d": '5 years',
        "correct_answer": "B",
        "explanation": 'Consumer can file within 2 years from date of deficiency in service or defect in goods.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32140,
        "question_text": "What is District Consumer Disputes Redressal Commission's jurisdiction?",
        "option_a": 'Up to ₹50 lakhs',
        "option_b": '₹1 crore to ₹10 crores',
        "option_c": 'Up to ₹1 crore',
        "option_d": 'Above ₹10 crores',
        "correct_answer": "C",
        "explanation": 'District Commission handles complaints up to ₹1 crore value.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32141,
        "question_text": 'What does ISI certification ensure for products?',
        "option_a": 'Product origin',
        "option_b": 'Quality, safety, conformity to standards',
        "option_c": 'Product price',
        "option_d": 'Expiry date',
        "correct_answer": "B",
        "explanation": 'ISI mark certifies product conformity with Indian Standards, ensuring quality, safety, reliability.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32142,
        "question_text": 'Role of Central Consumer Authority (May 2026)?',
        "option_a": 'Set product prices',
        "option_b": 'Investigate complaints at national level',
        "option_c": 'Manufacture consumer goods',
        "option_d": 'Import foreign products',
        "correct_answer": "B",
        "explanation": 'Central authority handles complaints exceeding state jurisdiction, ensuring national-level consumer protection.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32143,
        "question_text": 'Which authority ensures e-commerce consumer protection?',
        "option_a": 'RBI',
        "option_b": 'SEBI',
        "option_c": 'Department of Consumer Affairs',
        "option_d": 'Ministry of Commerce',
        "correct_answer": "C",
        "explanation": 'DoCA with Consumer Commissions oversees e-commerce consumer protection guidelines and regulations.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32144,
        "question_text": 'What remedies available for defective products under CPA 2019?',
        "option_a": 'Refund only',
        "option_b": 'Refund, replacement, compensation, or all three',
        "option_c": 'Replacement only',
        "option_d": 'Compensation only',
        "correct_answer": "B",
        "explanation": 'Consumers can seek refund, replacement, compensation for defective products, or combination as applicable.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32145,
        "question_text": 'What are consumer protection tribunals primarily for?',
        "option_a": 'Criminal cases',
        "option_b": 'Fast-track resolution of consumer disputes',
        "option_c": 'Only government matters',
        "option_d": 'Political issues',
        "correct_answer": "B",
        "explanation": 'Consumer tribunals provide speedy, affordable dispute resolution without lengthy court procedures.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32146,
        "question_text": "What is 'product liability' in consumer law?",
        "option_a": "Seller's profit obligation",
        "option_b": "Manufacturer's responsibility for defects causing harm/loss",
        "option_c": 'Product availability',
        "option_d": 'Price setting',
        "correct_answer": "B",
        "explanation": 'Product liability holds manufacturers responsible for defective products causing injury, damage, or economic loss.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32147,
        "question_text": "What does 'warranty' mean in consumer transactions?",
        "option_a": 'Price guarantee',
        "option_b": "Manufacturer's assurance regarding product quality/performance for specified period",
        "option_c": 'Selling promise',
        "option_d": 'Insurance',
        "correct_answer": "B",
        "explanation": 'Warranty guarantees product quality/performance for specified duration; breach allows consumer remedies.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32148,
        "question_text": 'What action against unfair trade practices?',
        "option_a": 'No action possible',
        "option_b": 'Complaint to Consumer Commission with penalties and compensation',
        "option_c": 'Only seller apology',
        "option_d": 'No compensation',
        "correct_answer": "B",
        "explanation": 'Unfair practices (misleading ads, hidden charges) attract Consumer Commission penalties and consumer compensation.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32149,
        "question_text": "What is 'right to be heard' in consumer law?",
        "option_a": 'Complaint suppression',
        "option_b": "Consumer's opportunity to present case before decision in disputes",
        "option_c": "Seller's right",
        "option_d": 'Government right',
        "correct_answer": "B",
        "explanation": 'Consumers have right to be heard in proceedings before authorities deciding their complaints.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32150,
        "question_text": 'What penalties for false advertising of products?',
        "option_a": 'No penalty',
        "option_b": 'Fines, compensation, imprisonment under CPA and IPC',
        "option_c": 'Only civil penalty',
        "option_d": 'Warning only',
        "correct_answer": "B",
        "explanation": 'False advertising attracts penalties up to ₹10 lakhs under CPA and criminal prosecution.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32151,
        "question_text": "What is 'caveat emptor' in consumer law?",
        "option_a": 'Buyer responsibility principle',
        "option_b": "'Seller beware' principle now modified for consumer protection",
        "option_c": 'Free products',
        "option_d": 'No responsibility',
        "correct_answer": "B",
        "explanation": 'Modern consumer law modifies caveat emptor; sellers bear responsibility for product quality/safety.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32152,
        "question_text": 'What is misleading/false claim?',
        "option_a": 'Accurate information',
        "option_b": 'Deceptive claim about product that misleads consumers',
        "option_c": 'True facts',
        "option_d": 'Proper labeling',
        "correct_answer": "B",
        "explanation": 'False claims about products (fake ingredients, exaggerated benefits) violate CPA and attract penalties.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32153,
        "question_text": 'What consumer right addresses quality concerns?',
        "option_a": 'Right to Choose',
        "option_b": 'Right to Safety and Quality Standards',
        "option_c": 'Right to Information',
        "option_d": 'Right to Complaint',
        "correct_answer": "B",
        "explanation": 'Right to Safety ensures products meet prescribed quality and safety standards protecting health.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32154,
        "question_text": 'What is arbitration in consumer disputes?',
        "option_a": 'Court proceedings',
        "option_b": 'Neutral third party deciding dispute based on evidence; faster than courts',
        "option_c": 'Seller negotiation',
        "option_d": 'Government ruling',
        "correct_answer": "B",
        "explanation": 'Arbitration provides quicker, cost-effective dispute resolution through neutral arbitrator.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32155,
        "question_text": 'Who protects consumers from online fraud?',
        "option_a": 'Sellers alone',
        "option_b": 'Consumer Commissions, Police, Cyber Crime Units, Consumer Affairs',
        "option_c": 'Only platforms',
        "option_d": 'Themselves',
        "correct_answer": "B",
        "explanation": 'Multiple authorities (consumer bodies, police, cybercrime) protect consumers from online fraud.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32156,
        "question_text": 'Which section of IT Act 2000 deals with cybercrime offences?',
        "option_a": 'Section 65',
        "option_b": 'Section 66',
        "option_c": 'Section 67',
        "option_d": 'Section 70',
        "correct_answer": "B",
        "explanation": 'Section 66 covers cybercrime including unauthorized access, data theft, up to 3 years imprisonment.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32157,
        "question_text": 'Primary objective of National Cyber Security Policy 2023?',
        "option_a": 'Ban internet',
        "option_b": 'Protect critical infrastructure and ensure cybersecurity across sectors',
        "option_c": 'Regulate government only',
        "option_d": 'Increase speed',
        "correct_answer": "B",
        "explanation": 'Policy protects critical information systems, prevents threats, establishes standards across sectors.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32158,
        "question_text": 'Law governing data protection in India (May 2026)?',
        "option_a": 'IT Act 2000 only',
        "option_b": 'Personal Data Protection Bill 2023 with IT Act provisions',
        "option_c": 'Aadhaar Act 2016',
        "option_d": 'RTI Act 2005',
        "correct_answer": "B",
        "explanation": 'Data protection framework includes IT Act and Personal Data Protection Bill 2023.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32159,
        "question_text": 'Role of CERT-IN in cybersecurity?',
        "option_a": 'Sell products',
        "option_b": 'Coordinate incident response and issue advisories',
        "option_c": 'Regulate ISPs',
        "option_d": 'Military operations',
        "correct_answer": "B",
        "explanation": 'CERT-IN coordinates cyber incident response, issues advisories, provides cybersecurity guidance.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32160,
        "question_text": 'Penalty for unauthorized computer access under IT Act?',
        "option_a": '₹1,000 fine only',
        "option_b": 'Up to 3 years imprisonment and/or ₹5 lakhs fine',
        "option_c": '1 year/₹2 lakhs',
        "option_d": '6 months/₹1 lakh',
        "correct_answer": "B",
        "explanation": 'Section 66 prescribes 3 years imprisonment and/or ₹5 lakhs fine for unauthorized access.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32161,
        "question_text": 'Purpose of Aadhaar in digital identity framework?',
        "option_a": 'Control population',
        "option_b": 'Provide unique identity and enable secure transactions',
        "option_c": 'Replace ID',
        "option_d": 'Monitor activities',
        "correct_answer": "B",
        "explanation": 'Aadhaar provides unique 12-digit identity linked to biometrics enabling secure digital transactions.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32162,
        "question_text": 'Critical information infrastructure requiring special protection?',
        "option_a": 'Social media only',
        "option_b": 'Power, water, finance, communications systems',
        "option_c": 'Entertainment websites',
        "option_d": 'Educational institutions',
        "correct_answer": "B",
        "explanation": 'Critical infrastructure (power, water, finance, telecom) requires enhanced cybersecurity protection.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32163,
        "question_text": 'What is ransomware?',
        "option_a": 'Social media app',
        "option_b": 'Malicious software encrypting data and demanding payment for recovery',
        "option_c": 'Security tool',
        "option_d": 'Antivirus',
        "correct_answer": "B",
        "explanation": 'Ransomware encrypts victim data, criminals demand payment (ransom) for decryption key.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32164,
        "question_text": 'Time limit for websites to remove illegal content after notice (IT Act)?',
        "option_a": 'Immediately',
        "option_b": '24 hours',
        "option_c": '36 hours',
        "option_d": '7 days',
        "correct_answer": "C",
        "explanation": 'Section 79 requires intermediaries remove illegal content within 36 hours of notice.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32165,
        "question_text": 'Which law addresses privacy violation through technology?',
        "option_a": 'IPC only',
        "option_b": 'IT Act 2000 and upcoming Data Protection Bill',
        "option_c": 'Aadhaar Act alone',
        "option_d": 'RTI Act',
        "correct_answer": "B",
        "explanation": 'IT Act and Data Protection Bill address privacy violations, unauthorized data access.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32166,
        "question_text": "What is 'phishing' in cybercrime?",
        "option_a": 'Real fishing',
        "option_b": 'Fraudulent technique to steal credentials through fake websites/emails',
        "option_c": 'Legitimate email',
        "option_d": 'Official communication',
        "correct_answer": "B",
        "explanation": 'Phishing tricks users into revealing sensitive information through fake websites/emails.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32167,
        "question_text": 'Purpose of Digital Signature Certificate?',
        "option_a": 'Email security only',
        "option_b": 'Authentication and integrity verification for digital documents',
        "option_c": 'Password protection',
        "option_d": 'Encryption only',
        "correct_answer": "B",
        "explanation": 'Digital certificates authenticate document origin and ensure integrity in digital transactions.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32168,
        "question_text": "What is 'DDoS attack' and its legal consequence?",
        "option_a": 'Legitimate network test',
        "option_b": 'Overwhelming servers with traffic causing disruption; violates IT Act',
        "option_c": 'Privacy issue',
        "option_d": 'Encryption problem',
        "correct_answer": "B",
        "explanation": 'DDoS attacks disrupt services, violate IT Act Section 66, attract prosecution and fines.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32169,
        "question_text": 'Which section covers obscene content online?',
        "option_a": 'Section 66',
        "option_b": 'Section 67',
        "option_c": 'Section 68',
        "option_d": 'Section 69',
        "correct_answer": "B",
        "explanation": 'Section 67 penalizes publishing obscene material online with up to 3 years imprisonment.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32170,
        "question_text": 'How does GDPR impact Indian businesses?',
        "option_a": 'No impact',
        "option_b": 'Indian companies handling EU data must comply with GDPR standards',
        "option_c": 'Only EU concern',
        "option_d": 'India exempt',
        "correct_answer": "B",
        "explanation": "GDPR applies to any business handling EU residents' data regardless of location.",
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32171,
        "question_text": "What is 'data breach' notification requirement?",
        "option_a": 'Never notify',
        "option_b": 'Companies must notify affected individuals and authorities promptly',
        "option_c": 'Optional',
        "option_d": 'After 1 year',
        "correct_answer": "B",
        "explanation": 'Data Protection Bill mandates prompt notification of breaches to individuals and authorities.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32172,
        "question_text": 'Which agency handles cybercrime in India?',
        "option_a": 'Only local police',
        "option_b": 'Police, CERT-IN, CBI based on jurisdiction and severity',
        "option_c": 'Ministry only',
        "option_d": 'Courts alone',
        "correct_answer": "B",
        "explanation": 'Police, CERT-IN, and CBI handle cybercrime depending on nature and jurisdiction.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32173,
        "question_text": "What is 'social engineering' in cybercrime?",
        "option_a": 'Legitimate hacking',
        "option_b": 'Manipulating people to divulge confidential information',
        "option_c": 'Technology abuse',
        "option_d": 'Network issue',
        "correct_answer": "B",
        "explanation": 'Social engineering manipulates psychology to trick users into revealing sensitive data.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32174,
        "question_text": 'Protection against identity theft?',
        "option_a": 'No protection',
        "option_b": 'Data protection laws, secure passwords, regular monitoring, prompt reporting',
        "option_c": 'Impossible',
        "option_d": 'Insurance only',
        "correct_answer": "B",
        "explanation": 'Data Protection Bill, secure practices, monitoring, prompt reporting offer identity theft protection.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32175,
        "question_text": 'What is cyberstalking and its legal status?',
        "option_a": 'Legitimate online activity',
        "option_b": 'Harassment through internet; illegal under IT Act and IPC',
        "option_c": 'Normal communication',
        "option_d": 'Social media use',
        "correct_answer": "B",
        "explanation": 'Cyberstalking (repeated harassment online) violates IT Act and IPC with criminal penalties.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32176,
        "question_text": 'Role of cybersecurity training for organizations?',
        "option_a": 'Optional luxury',
        "option_b": 'Critical for preventing breaches, ensuring compliance, protecting data',
        "option_c": 'Not important',
        "option_d": 'Only for IT teams',
        "correct_answer": "B",
        "explanation": 'Employee cybersecurity training is essential for preventing breaches and ensuring security compliance.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32177,
        "question_text": 'When was Smart Cities Mission launched?',
        "option_a": '2013',
        "option_b": '2015',
        "option_c": '2017',
        "option_d": '2019',
        "correct_answer": "B",
        "explanation": 'Launched June 25, 2015 for 100 smart cities development.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32178,
        "question_text": 'Primary objective of Smart Cities Mission?',
        "option_a": 'Only highways',
        "option_b": 'Technology-enabled cities with sustainable growth and improved quality of life',
        "option_c": 'Only railways',
        "option_d": 'Real estate promotion',
        "correct_answer": "B",
        "explanation": 'Develops technology-enabled cities ensuring sustainability and better citizen services.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32179,
        "question_text": 'How many cities selected in first phase (June 2015)?',
        "option_a": '20 cities',
        "option_b": '50 cities',
        "option_c": '100 cities',
        "option_d": '200 cities',
        "correct_answer": "B",
        "explanation": 'First phase selected 20 cities, followed by subsequent phases.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32180,
        "question_text": 'Ministry overseeing Smart Cities Mission?',
        "option_a": 'Ministry of Defence',
        "option_b": 'Ministry of Housing and Urban Affairs',
        "option_c": 'Panchayat Raj',
        "option_d": 'Environment',
        "correct_answer": "B",
        "explanation": 'Ministry of Housing and Urban Affairs implements and oversees the mission.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32181,
        "question_text": 'Percentage of central government funding in mission?',
        "option_a": '25%',
        "option_b": '33.33%',
        "option_c": '50%',
        "option_d": '75%',
        "correct_answer": "C",
        "explanation": "Tri-partite funding: 33.33% central, 33.33% state, 33.34% city's resources.",
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32182,
        "question_text": 'Key component of Smart Cities Mission?',
        "option_a": 'Buildings only',
        "option_b": 'Smart governance, digital infrastructure, IoT, sustainable transport',
        "option_c": 'Shopping malls',
        "option_d": 'Defense purposes',
        "correct_answer": "B",
        "explanation": 'Components include governance, digital services, IoT, renewable energy, waste management.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32183,
        "question_text": 'Status of mission as of May 2026?',
        "option_a": 'Not started',
        "option_b": 'Over 90% projects completed, most cities operational',
        "option_c": 'Early stages',
        "option_d": 'Stalled',
        "correct_answer": "B",
        "explanation": 'Significant progress with operational smart city services across India.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32184,
        "question_text": 'Which AP city is developing as smart city?',
        "option_a": 'Visakhapatnam',
        "option_b": 'Amaravati',
        "option_c": 'Vijayawada',
        "option_d": 'Tirupati',
        "correct_answer": "A",
        "explanation": 'Visakhapatnam developing smart infrastructure with IoT systems and digital services.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32185,
        "question_text": "What is 'Pradhan Mantri Awas Yojana' focus?",
        "option_a": 'Only urban areas',
        "option_b": 'Providing affordable housing to all, both urban and rural',
        "option_c": 'Only rural',
        "option_d": 'Commercial buildings',
        "correct_answer": "B",
        "explanation": 'PMAY aims universal housing coverage with sustainable affordability.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32186,
        "question_text": "What does 'urban sprawl' mean in city planning?",
        "option_a": 'Controlled expansion',
        "option_b": 'Uncontrolled expansion reducing agricultural land and infrastructure pressure',
        "option_c": 'Building growth',
        "option_d": 'Migration',
        "correct_answer": "B",
        "explanation": 'Sprawl refers to unplanned horizontal expansion degrading environment and services.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32187,
        "question_text": 'How does waste management feature in smart cities?',
        "option_a": 'Ignored',
        "option_b": 'Integrated waste segregation, recycling, disposal systems with IoT monitoring',
        "option_c": 'Only landfill',
        "option_d": 'Burning only',
        "correct_answer": "B",
        "explanation": 'Smart waste management includes automated segregation, recycling, real-time tracking.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32188,
        "question_text": "What is 'mixed-use development' in urban planning?",
        "option_a": 'Only residential',
        "option_b": 'Integration of residential, commercial, recreational spaces',
        "option_c": 'Only commercial',
        "option_d": 'Only industrial',
        "correct_answer": "B",
        "explanation": 'Mixed-use development combines residential, commercial, entertainment in single area.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32189,
        "question_text": "Role of 'affordable housing' in smart cities?",
        "option_a": 'Not important',
        "option_b": 'Ensuring economic diversity and social inclusivity in urban development',
        "option_c": 'Only for poor',
        "option_d": 'No importance',
        "correct_answer": "B",
        "explanation": 'Affordable housing integrates all economic classes, promotes inclusive development.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32190,
        "question_text": "What is 'public-private partnership' (PPP) in infrastructure?",
        "option_a": 'Government alone',
        "option_b": 'Joint government-private sector projects for efficiency and innovation',
        "option_c": 'Private alone',
        "option_d": 'NGO projects',
        "correct_answer": "B",
        "explanation": "PPP leverages both sectors' strengths for better infrastructure development.",
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32191,
        "question_text": "How does 'smart transportation' improve urban mobility?",
        "option_a": 'No improvement',
        "option_b": 'IoT-enabled traffic management, real-time info, electric vehicles',
        "option_c": 'More vehicles',
        "option_d": 'Fewer roads',
        "correct_answer": "B",
        "explanation": 'Smart transport reduces congestion, emissions through technology-enabled systems.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32192,
        "question_text": "What is 'green building' certification?",
        "option_a": 'Color painted green',
        "option_b": 'Building meeting energy efficiency, sustainability, environmental standards',
        "option_c": 'Plant covered',
        "option_d": 'Tree planting',
        "correct_answer": "B",
        "explanation": 'Green building certification ensures sustainable design, energy efficiency, resource conservation.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32193,
        "question_text": 'Impact of smart cities on citizen participation?',
        "option_a": 'Reduced participation',
        "option_b": 'Enhanced participation through digital platforms, governance transparency',
        "option_c": 'No change',
        "option_d": 'Limited involvement',
        "correct_answer": "B",
        "explanation": 'Smart systems enable real-time citizen feedback, digital governance transparency.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32194,
        "question_text": "What does 'city resilience' mean?",
        "option_a": 'Rapid growth',
        "option_b": "City's capacity to withstand shocks, adapt, recover from challenges",
        "option_c": 'Financial strength',
        "option_d": 'Political power',
        "correct_answer": "B",
        "explanation": 'Resilience enables cities to handle natural disasters, climate impacts, economic shocks.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32195,
        "question_text": 'How does digital governance improve citizen services?',
        "option_a": 'No improvement',
        "option_b": 'Online service delivery, reduced corruption, faster processing, transparency',
        "option_c": 'More bureaucracy',
        "option_d": 'Slower services',
        "correct_answer": "B",
        "explanation": 'Digital systems enable 24/7 services, reduced documentation, increased transparency.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },
    {
        "id": 32196,
        "question_text": "What is 'urban heat island' effect and solution?",
        "option_a": 'Normal phenomenon',
        "option_b": 'Excessive urban heat from development; mitigated through green spaces, cool roofs',
        "option_c": 'Temperature measurement',
        "option_d": 'Weather',
        "correct_answer": "B",
        "explanation": 'Heat island effect mitigated through vegetation, reflective surfaces, water bodies.',
        "topic": "Polity_Specialized_Categories",
        "folder": "National_CA"
    },

]

def seed():
    """Seed {len(POLITY_MCQS)} MCQs to database"""
    if USE_POSTGRES:
        conn = psycopg2.connect(DATABASE_URL)
        conn.autocommit = False
        cur = conn.cursor()
        delete_sql = "DELETE FROM questions WHERE id >= %s AND id <= %s"
        insert_sql = """INSERT INTO questions
            (id, question_text, option_a, option_b, option_c, option_d,
             correct_answer, explanation, topic, folder, difficulty)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (id) DO NOTHING"""
    else:
        conn = sqlite3.connect(
            os.path.join(os.path.dirname(__file__), "database.db")
        )
        cur = conn.cursor()
        delete_sql = "DELETE FROM questions WHERE id >= ? AND id <= ?"
        insert_sql = """INSERT OR IGNORE INTO questions
            (id, question_text, option_a, option_b, option_c, option_d,
             correct_answer, explanation, topic, folder, difficulty)
            VALUES (?,?,?,?,?,?,?,?,?,?,?)"""

    cur.execute(delete_sql, (32136, 32196))

    for q in POLITY_MCQS:
        cur.execute(insert_sql, (
            q["id"], q["question_text"],
            q["option_a"], q["option_b"], q["option_c"], q["option_d"],
            q["correct_answer"], q["explanation"],
            q["topic"], q["folder"], "M"
        ))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    seed()
