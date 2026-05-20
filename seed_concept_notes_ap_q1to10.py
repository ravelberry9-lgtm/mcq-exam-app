"""
seed_concept_notes_ap_q1to10.py
Individual concept notes for AP CA 2026 questions 32001-32010.
Each note is per-question topic cluster.
"""
import os

def get_db():
    database_url = os.environ.get('DATABASE_URL', '')
    if database_url:
        import psycopg2
        conn = psycopg2.connect(database_url)
        conn.autocommit = True
        return conn, 'pg'
    else:
        import sqlite3
        db_path = os.path.join(os.path.dirname(__file__), 'database.db')
        conn = sqlite3.connect(db_path)
        return conn, 'sqlite'

NOTES = [
    # ── q_32001: AP Budget 2026-27 (covers 32001, 32002) ──
    (
        'q_32001',
        'AP Budget 2026-27',
        'AP బడ్జెట్ 2026-27',
        '''<h2 style="color:#1a237e;font-size:1.1em;border-bottom:2px solid #3949ab;padding-bottom:5px;margin:0 0 10px">AP బడ్జెట్ 2026-27 / AP Budget 2026-27</h2>
<p style="font-size:0.82em;color:#555;margin:0 0 8px"><strong>సమర్పణ:</strong> పయ్యావుల కేశవ్ | <strong>తేదీ:</strong> Feb 28, 2025</p>
<table style="width:100%;border-collapse:collapse;font-size:0.83em;margin-bottom:10px">
<thead><tr style="background:#1a237e;color:#fff"><th style="padding:5px 7px;text-align:left">అంశం / Item</th><th style="padding:5px 7px;text-align:right">మొత్తం (₹ కోట్లు)</th></tr></thead>
<tbody>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">మొత్తం బడ్జెట్ / <strong>Total Budget</strong></td><td style="padding:4px 7px;text-align:right;font-weight:700;color:#1a237e">2,77,830</td></tr>
<tr><td style="padding:4px 7px">రెవెన్యూ రాబడి / Revenue Receipts</td><td style="padding:4px 7px;text-align:right">1,94,140</td></tr>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">రెవెన్యూ వ్యయం / Revenue Expenditure</td><td style="padding:4px 7px;text-align:right">2,19,680</td></tr>
<tr><td style="padding:4px 7px">మూలధన వ్యయం / Capital Outlay</td><td style="padding:4px 7px;text-align:right">58,150</td></tr>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">GST వసూళ్లు (4 నెలలు) / GST Collections</td><td style="padding:4px 7px;text-align:right">16,754 (61% of target)</td></tr>
</tbody></table>
<ul style="font-size:0.82em;color:#333;padding-left:16px;margin:4px 0">
<li><strong>రాజకోశ లోటు / Fiscal Deficit:</strong> GSDP లో 3.5%</li>
<li><strong>విద్య / Education:</strong> ₹31,200 కోట్లు | <strong>ఆరోగ్యం / Health:</strong> ₹18,400 కోట్లు</li>
<li><strong>వ్యవసాయం / Agriculture:</strong> ₹22,600 కోట్లు | <strong>మౌలిక సదుపాయాలు:</strong> ₹24,900 కోట్లు</li>
</ul>'''
    ),

    # ── q_32003: Amaravati Capital ──
    (
        'q_32003',
        'Amaravati Capital',
        'అమరావతి రాజధాని',
        '''<h2 style="color:#1a237e;font-size:1.1em;border-bottom:2px solid #3949ab;padding-bottom:5px;margin:0 0 10px">అమరావతి రాజధాని / Amaravati Capital</h2>
<table style="width:100%;border-collapse:collapse;font-size:0.83em;margin-bottom:10px">
<thead><tr style="background:#1a237e;color:#fff"><th style="padding:5px 7px;text-align:left">అంశం / Item</th><th style="padding:5px 7px;text-align:left">వివరాలు / Detail</th></tr></thead>
<tbody>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">చట్టం / Act</td><td style="padding:4px 7px">Amaravati Capital Region Act — జులై 2, 2024</td></tr>
<tr><td style="padding:4px 7px">ఏకైక రాజధాని ప్రకటన</td><td style="padding:4px 7px">AP శాసనసభ జులై 2, 2024న ఆమోదించింది</td></tr>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">స్థానం / Location</td><td style="padding:4px 7px">కృష్ణా నది తీరం, గుంటూరు జిల్లా, 29 గ్రామాలు</td></tr>
<tr><td style="padding:4px 7px">నగర రూపకల్పన</td><td style="padding:4px 7px">సింగపూర్ సంస్థ (Ascendas-Singbridge)</td></tr>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">పూర్వపు రాజధాని</td><td style="padding:4px 7px">హైదరాబాద్ (2014-2024 ఉమ్మడి)</td></tr>
<tr><td style="padding:4px 7px">APRA 2014 Section</td><td style="padding:4px 7px">Section 5(2) — రాజధాని నిర్ణయం; 2026 సవరణతో అమరావతి ఖరారు</td></tr>
</tbody></table>
<ul style="font-size:0.82em;color:#333;padding-left:16px;margin:4px 0">
<li><strong>Greenfield నగరం</strong> — ఇప్పటికే ఉన్న నగరాన్ని అభివృద్ధి చేయడం కాదు; కొత్తగా నిర్మించే నగరం</li>
<li><strong>CRDA</strong> (Capital Region Development Authority) — రాజధాని ప్రాంత అభివృద్ధి సంస్థ</li>
<li><strong>Land Pooling Scheme</strong> ద్వారా ~33,000 ఎకరాలు సేకరణ (బలవంతంగా కాదు)</li>
<li>APRA Amendment Act 2026 (Act No. 7/2026) — అమరావతిని Jun 2, 2024 నుండి retroactive గా రాజధాని నిర్ణయించింది</li>
</ul>'''
    ),

    # ── q_32004: CRDA (covers 32004, 32005) ──
    (
        'q_32004',
        'CRDA - Capital Region Development Authority',
        'CRDA - రాజధాని ప్రాంత అభివృద్ధి సంస్థ',
        '''<h2 style="color:#1a237e;font-size:1.1em;border-bottom:2px solid #3949ab;padding-bottom:5px;margin:0 0 10px">CRDA — రాజధాని ప్రాంత అభివృద్ధి సంస్థ</h2>
<table style="width:100%;border-collapse:collapse;font-size:0.83em;margin-bottom:10px">
<thead><tr style="background:#1a237e;color:#fff"><th style="padding:5px 7px;text-align:left">అంశం / Item</th><th style="padding:5px 7px;text-align:left">వివరాలు / Detail</th></tr></thead>
<tbody>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">పూర్తి పేరు / Full Name</td><td style="padding:4px 7px"><strong>Capital Region Development Authority</strong></td></tr>
<tr><td style="padding:4px 7px">చట్టం / Act</td><td style="padding:4px 7px">AP Capital Region Development Authority Act, 2014</td></tr>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">అమరావతి ప్రాంతం</td><td style="padding:4px 7px">29 గ్రామాలు, గుంటూరు జిల్లా, కృష్ణా నది తీరం</td></tr>
<tr><td style="padding:4px 7px">Land Pooling</td><td style="padding:4px 7px">~33,000 ఎకరాలు స్వచ్ఛందంగా / Voluntary — బలవంతం కాదు</td></tr>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">రైతులకు ప్రతిఫలం</td><td style="padding:4px 7px">అభివృద్ధి చేసిన ప్లాట్లు + వార్షిక అన్యుటీ / Developed plots + Annuity</td></tr>
<tr><td style="padding:4px 7px">విధులు / Functions</td><td style="padding:4px 7px">నగర ప్రణాళిక, మౌలిక సదుపాయాలు, భూ వినియోగం, యుటిలిటీలు</td></tr>
</tbody></table>
<div style="background:#fff3e0;border-left:3px solid #ff9800;padding:7px 10px;font-size:0.82em;margin-top:6px">
<strong>⚡ పరీక్ష చిట్కా / Exam Tip:</strong> CRDA = <em>Capital Region Development Authority</em> (Central కాదు, Capital!) | AP CRDA Act 2014 కింద స్థాపించబడింది.
</div>'''
    ),

    # ── q_32006: Amarseva Masters Project (covers 32006, 32007) ──
    (
        'q_32006',
        'AP Amarseva Masters Project',
        'AP అమరసేవ మాస్టర్స్ ప్రాజెక్ట్',
        '''<h2 style="color:#1a237e;font-size:1.1em;border-bottom:2px solid #3949ab;padding-bottom:5px;margin:0 0 10px">AP అమరసేవ మాస్టర్స్ ప్రాజెక్ట్</h2>
<div style="display:flex;gap:8px;margin-bottom:10px;flex-wrap:wrap">
<div style="flex:1;min-width:100px;background:#e8eaf6;border-radius:8px;padding:8px;text-align:center">
<div style="font-size:1.4em;font-weight:700;color:#1a237e">₹7,910 కోట్లు</div>
<div style="font-size:0.75em;color:#555">మొత్తం వ్యయం / Total Cost</div>
</div>
<div style="flex:1;min-width:100px;background:#e8f5e9;border-radius:8px;padding:8px;text-align:center">
<div style="font-size:1.4em;font-weight:700;color:#2e7d32">205</div>
<div style="font-size:0.75em;color:#555">యాంబులెన్సులు / Ambulances</div>
</div>
</div>
<table style="width:100%;border-collapse:collapse;font-size:0.83em;margin-bottom:8px">
<thead><tr style="background:#1a237e;color:#fff"><th style="padding:5px 7px;text-align:left">అంశం</th><th style="padding:5px 7px;text-align:left">వివరాలు</th></tr></thead>
<tbody>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">పథకం ఉద్దేశ్యం</td><td style="padding:4px 7px">అత్యవసర ఆరోగ్య సేవలు — Emergency Medical Response</td></tr>
<tr><td style="padding:4px 7px">ప్రభుత్వం / Government</td><td style="padding:4px 7px">TDP-JSP-BJP కూటమి ప్రభుత్వం (2024 నుండి)</td></tr>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">రంగం / Sector</td><td style="padding:4px 7px">ఆరోగ్యం & అత్యవసర సేవలు / Health & Emergency</td></tr>
</tbody></table>
<div style="background:#fff3e0;border-left:3px solid #ff9800;padding:7px 10px;font-size:0.82em">
<strong>⚡ పరీక్ష చిట్కా:</strong> అమరసేవ = ₹7,910 కోట్లు | 205 యాంబులెన్సులు — రెండూ గుర్తుంచుకోండి!
</div>'''
    ),

    # ── q_32008: AP Logistics Policy ──
    (
        'q_32008',
        'AP Logistics & Warehousing Policy 2025-2030',
        'AP లాజిస్టిక్స్ పాలసీ 2025-2030',
        '''<h2 style="color:#1a237e;font-size:1.1em;border-bottom:2px solid #3949ab;padding-bottom:5px;margin:0 0 10px">AP లాజిస్టిక్స్ & వేర్‌హౌసింగ్ పాలసీ 2025-2030</h2>
<table style="width:100%;border-collapse:collapse;font-size:0.83em;margin-bottom:10px">
<thead><tr style="background:#1a237e;color:#fff"><th style="padding:5px 7px;text-align:left">అంశం / Item</th><th style="padding:5px 7px;text-align:left">వివరాలు / Detail</th></tr></thead>
<tbody>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">కాలవ్యవధి / Period</td><td style="padding:4px 7px;font-weight:700;color:#1a237e">2025 – 2030</td></tr>
<tr><td style="padding:4px 7px">వ్యూహాత్మక స్థానం / Strategic Ports</td><td style="padding:4px 7px">విశాఖపట్నం, కృష్ణపట్నం, కాకినాడ పోర్టులు</td></tr>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">దృష్టి / Vision Link</td><td style="padding:4px 7px">Swarnandhra@2047 విజన్‌తో అనుసంధానం</td></tr>
<tr><td style="padding:4px 7px">ముఖ్య లక్ష్యాలు / Goals</td><td style="padding:4px 7px">Multi-modal hubs, Cold chains, Warehousing parks</td></tr>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">నిరీక్షిత ఫలితాలు / Expected</td><td style="padding:4px 7px">పెట్టుబడులు + ఉద్యోగాల కల్పన / Investment + Job creation</td></tr>
</tbody></table>
<div style="background:#fff3e0;border-left:3px solid #ff9800;padding:7px 10px;font-size:0.82em">
<strong>⚡ పరీక్ష చిట్కా:</strong> AP Logistics Policy కాలవ్యవధి = <strong>2025-2030</strong> (2024-2029 కాదు!)
</div>'''
    ),

    # ── q_32009: Women in AP Assembly ──
    (
        'q_32009',
        'Women in AP Legislature',
        'AP శాసనసభలో మహిళలు',
        '''<h2 style="color:#1a237e;font-size:1.1em;border-bottom:2px solid #3949ab;padding-bottom:5px;margin:0 0 10px">AP శాసనసభలో మహిళా ప్రాతినిధ్యం / Women in AP Legislature</h2>
<div style="display:flex;gap:8px;margin-bottom:10px;flex-wrap:wrap">
<div style="flex:1;min-width:90px;background:#e8eaf6;border-radius:8px;padding:8px;text-align:center">
<div style="font-size:1.4em;font-weight:700;color:#1a237e">28.63%</div>
<div style="font-size:0.75em;color:#555">మహిళా ప్రాతినిధ్యం</div>
</div>
<div style="flex:1;min-width:90px;background:#e8f5e9;border-radius:8px;padding:8px;text-align:center">
<div style="font-size:1.4em;font-weight:700;color:#2e7d32">175</div>
<div style="font-size:0.75em;color:#555">మొత్తం స్థానాలు</div>
</div>
<div style="flex:1;min-width:90px;background:#fff3e0;border-radius:8px;padding:8px;text-align:center">
<div style="font-size:1.4em;font-weight:700;color:#e65100">3/25</div>
<div style="font-size:0.75em;color:#555">కేబినెట్ మహిళా మంత్రులు</div>
</div>
</div>
<table style="width:100%;border-collapse:collapse;font-size:0.83em;margin-bottom:8px">
<thead><tr style="background:#1a237e;color:#fff"><th style="padding:5px 7px;text-align:left">అంశం</th><th style="padding:5px 7px;text-align:left">వివరాలు</th></tr></thead>
<tbody>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">జాతీయ సగటు / National Avg</td><td style="padding:4px 7px">AP మహిళా % జాతీయ సగటు కంటే అధికం (Above average)</td></tr>
<tr><td style="padding:4px 7px">ఎన్నికలు / Elections</td><td style="padding:4px 7px">మే 13, 2024 — TDP-JSP-BJP కూటమి 164/175 స్థానాలు గెలిచింది</td></tr>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">హోం మంత్రి / Home Minister</td><td style="padding:4px 7px"><strong>వంగలపూడి అనిత</strong> (TDP, పాయకరాపేట) — Home Affairs, Disaster Management</td></tr>
<tr><td style="padding:4px 7px">పరిశ్రమల మంత్రి / Industries</td><td style="padding:4px 7px"><strong>తి.గ. భారతి</strong> (TDP, కర్నూల్) — Industries & Commerce, Food Processing</td></tr>
<tr style="background:#e8eaf6"><td style="padding:4px 7px">3వ మహిళా మంత్రి</td><td style="padding:4px 7px">25 మంత్రుల కేబినెట్‌లో మొత్తం 3 మహిళా మంత్రులు</td></tr>
</tbody></table>
<div style="background:#fff3e0;border-left:3px solid #ff9800;padding:7px 10px;font-size:0.82em">
<strong>⚡ పరీక్ష చిట్కా:</strong> 3 మహిళా మంత్రులు — వంగలపూడి అనిత (Home) + తి.గ. భారతి (Industries) + మరొకరు | మహిళా ప్రాతినిధ్యం = <strong>28.63%</strong>
</div>'''
    ),

    # ── q_32010: AP TFR ──
    (
        'q_32010',
        'AP Total Fertility Rate (TFR)',
        'AP సంతానోత్పత్తి రేటు (TFR)',
        '''<h2 style="color:#1a237e;font-size:1.1em;border-bottom:2px solid #3949ab;padding-bottom:5px;margin:0 0 10px">AP మొత్తం సంతానోత్పత్తి రేటు / AP Total Fertility Rate</h2>
<div style="display:flex;gap:8px;margin-bottom:10px;flex-wrap:wrap">
<div style="flex:1;min-width:90px;background:#e8eaf6;border-radius:8px;padding:8px;text-align:center">
<div style="font-size:1.6em;font-weight:700;color:#1a237e">1.5</div>
<div style="font-size:0.75em;color:#555">AP TFR (NFHS)</div>
</div>
<div style="flex:1;min-width:90px;background:#fff3e0;border-radius:8px;padding:8px;text-align:center">
<div style="font-size:1.6em;font-weight:700;color:#e65100">2.1</div>
<div style="font-size:0.75em;color:#555">జాతీయ సగటు / National</div>
</div>
<div style="flex:1;min-width:90px;background:#fce4ec;border-radius:8px;padding:8px;text-align:center">
<div style="font-size:1.6em;font-weight:700;color:#c62828">2.1</div>
<div style="font-size:0.75em;color:#555">Replacement Level</div>
</div>
</div>
<ul style="font-size:0.83em;color:#333;padding-left:16px;margin:4px 0 8px">
<li>AP TFR <strong>1.5</strong> — replacement level (2.1) కంటే చాలా తక్కువ</li>
<li><strong>కారణాలు / Reasons:</strong> అక్షరాస్యత, పట్టణీకరణ, మహిళా సాధికారత</li>
<li>AP జనాభా <strong>వయోవృద్ధి</strong> (Aging population) సమస్యను ఎదుర్కొంటోంది</li>
<li><strong>మూలం / Source:</strong> NFHS (National Family Health Survey)</li>
</ul>
<div style="background:#fff3e0;border-left:3px solid #ff9800;padding:7px 10px;font-size:0.82em">
<strong>⚡ పరీక్ష చిట్కా:</strong> AP TFR = <strong>1.5</strong> (జాతీయ సగటు 2.1 కంటే తక్కువ) — NFHS డేటా
</div>'''
    ),
]


def seed():
    conn, db_type = get_db()
    if db_type == 'pg':
        cur = conn.cursor()
        for tag, label, label_te, html in NOTES:
            cur.execute(
                'INSERT INTO concept_notes (tag, label, label_te, html) VALUES (%s,%s,%s,%s) '
                'ON CONFLICT (tag) DO UPDATE SET label=EXCLUDED.label, label_te=EXCLUDED.label_te, html=EXCLUDED.html',
                (tag, label, label_te, html)
            )
        cur.close()
        print(f'[seed_concept_notes_ap_q1to10] Upserted {len(NOTES)} concept notes (pg).')
    else:
        cur = conn.cursor()
        for tag, label, label_te, html in NOTES:
            cur.execute(
                'INSERT OR REPLACE INTO concept_notes (tag, label, label_te, html) VALUES (?,?,?,?)',
                (tag, label, label_te, html)
            )
        conn.commit()
        print(f'[seed_concept_notes_ap_q1to10] Upserted {len(NOTES)} concept notes (sqlite).')


if __name__ == '__main__':
    seed()
