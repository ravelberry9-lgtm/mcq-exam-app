"""Add a fear-to-safeguard study table to AP History Chapter 28.

Revision ID: p2k3l4m5n6o7
Revises: o1j2k3l4m5n6
"""
from alembic import op
import sqlalchemy as sa


revision = "p2k3l4m5n6o7"
down_revision = "o1j2k3l4m5n6"
branch_labels = None
depends_on = None

MARKER = '<section class="apsche-second-pass-ch28" data-source="APSCHE second slow pass presentation audit">'
ADDITION = MARKER + r'''
<h2>APSCHE రెండో పరిశీలన — తెలంగాణ భయం నుంచి రక్షణకు</h2>
<blockquote><strong>మూల పరిరక్షణ:</strong> Chapter 28లోని RR/HR facts, Gentlemen’s Agreement clauses, figures, MCQs మార్చబడలేదు. ఇప్పటికే ఉన్న విషయాన్ని పరీక్షకు సులభంగా పోల్చుకునే presentation tableగా మాత్రమే ఇక్కడ అమర్చాం.</blockquote>
<table><thead><tr><th>విలీనంపై తెలంగాణలో వ్యక్తమైన భయం</th><th>పెద్దమనుషుల ఒప్పందంలో సంబంధిత రక్షణ</th></tr></thead><tbody>
<tr><td>తెలంగాణ మిగులు ఆదాయం ఇతర ప్రాంత అవసరాలకు మళ్లవచ్చు</td><td>తెలంగాణ ఆదాయ మిగులు తెలంగాణ అభివృద్ధికే వినియోగించాలి</td></tr>
<tr><td>విద్యలో ముందున్న ఆంధ్ర విద్యార్థులు అవకాశాలను అధికంగా పొందవచ్చు</td><td>తెలంగాణ విద్యాసంస్థల్లో స్థానిక విద్యార్థులకు రక్షణ; విద్యా సౌకర్యాల అభివృద్ధి</td></tr>
<tr><td>ప్రభుత్వ ఉద్యోగాల్లో తెలంగాణ వాటా తగ్గవచ్చు</td><td>జనాభా నిష్పత్తి, స్థానికత/నివాస నియమాలకు రక్షణ</td></tr>
<tr><td>ఉర్దూ పరిపాలనా స్థానం ఒక్కసారిగా తొలగిపోవచ్చు</td><td>ఉర్దూ కొనసాగింపుకు నిర్ణీత కాల రక్షణ</td></tr>
<tr><td>వ్యవసాయ భూములు బయటివారి చేతుల్లోకి వెళ్లవచ్చు</td><td>తెలంగాణ వ్యవసాయ భూముల విక్రయంపై ప్రాంతీయ నియంత్రణ</td></tr>
<tr><td>సాగునీరు, ప్రణాళిక, అభివృద్ధిలో తెలంగాణకు ప్రాధాన్యం తగ్గవచ్చు</td><td>ప్రాంతీయ మండలి ద్వారా ప్రణాళిక, నీటిపారుదల, అభివృద్ధి అంశాల్లో స్వరం</td></tr>
<tr><td>రాష్ట్ర మంత్రివర్గంలో తెలంగాణకు తగిన భాగస్వామ్యం ఉండకపోవచ్చు</td><td>60:40 మంత్రివర్గ నిష్పత్తి; ముఖ్యమంత్రి–ఉపముఖ్యమంత్రి ప్రాంతీయ సమతుల్యత; కీలక శాఖల్లో తెలంగాణ మంత్రులకు స్థానం</td></tr>
</tbody></table>
<p><strong>చదివే పద్ధతి:</strong> ఒప్పంద నిబంధనను ఒంటరిగా బట్టీ పట్టకండి. మొదట భయాన్ని గుర్తించండి; తరువాత ఆ భయానికి ఇచ్చిన పరిపాలనా సమాధానాన్ని జత చేయండి. అప్పుడు revenue–education–jobs–language–land–regional council–cabinet అనే క్రమం కథలా గుర్తుంటుంది.</p>
</section>'''


def upgrade():
    bind = op.get_bind(); meta = sa.MetaData()
    subjects = sa.Table("subjects", meta, autoload_with=bind)
    chapters = sa.Table("chapters", meta, autoload_with=bind)
    notes = sa.Table("notes", meta, autoload_with=bind)
    subject_id = bind.execute(sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")).scalar_one()
    chapter_id = bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id == subject_id, chapters.c.chapter_num == 28)).scalar_one()
    note = bind.execute(sa.select(notes).where(notes.c.chapter_id == chapter_id).order_by(notes.c.section_num)).mappings().first()
    original = note["body_te"] or ""
    if MARKER in original: raise RuntimeError("Chapter 28 already has second-pass marker")
    updated = original + "\n\n" + ADDITION
    if not updated.startswith(original): raise RuntimeError("Source-preservation guard failed")
    bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=updated))


def downgrade():
    bind = op.get_bind(); meta = sa.MetaData()
    subjects = sa.Table("subjects", meta, autoload_with=bind)
    chapters = sa.Table("chapters", meta, autoload_with=bind)
    notes = sa.Table("notes", meta, autoload_with=bind)
    subject_id = bind.execute(sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")).scalar_one()
    chapter_id = bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id == subject_id, chapters.c.chapter_num == 28)).scalar_one()
    note = bind.execute(sa.select(notes).where(notes.c.chapter_id == chapter_id).order_by(notes.c.section_num)).mappings().first()
    body = note["body_te"] or ""; marker_at = body.find("\n\n" + MARKER)
    if marker_at < 0: raise RuntimeError("Cannot safely remove Chapter 28 second-pass enrichment")
    bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=body[:marker_at]))
