import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY

def create_pdf(report_text: str) -> bytes:
    """
    Takes the markdown report text and converts it into a PDF byte stream.
    For simplicity, we convert basic markdown to paragraphs.
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    
    Story = []
    
    # Split text by newlines and create paragraphs
    # This is a basic conversion; rich markdown parsing requires more complex handling
    for line in report_text.split('\n'):
        line = line.strip()
        if not line:
            Story.append(Spacer(1, 12))
            continue
            
        if line.startswith('# '):
            p = Paragraph(f"<b><font size=18>{line[2:]}</font></b>", styles['Heading1'])
            Story.append(p)
            Story.append(Spacer(1, 12))
        elif line.startswith('## '):
            p = Paragraph(f"<b><font size=14>{line[3:]}</font></b>", styles['Heading2'])
            Story.append(p)
            Story.append(Spacer(1, 10))
        elif line.startswith('### '):
            p = Paragraph(f"<b><font size=12>{line[4:]}</font></b>", styles['Heading3'])
            Story.append(p)
            Story.append(Spacer(1, 8))
        else:
            p = Paragraph(line, styles['Normal'])
            Story.append(p)
            
    doc.build(Story)
    
    pdf_value = buffer.getvalue()
    buffer.close()
    return pdf_value
