
import cStringIO
from reportlab.pdfgen import canvas




def create_termination(name):
    output = cStringIO.StringIO()
    p = canvas.Canvas(output)
    p.drawString(100, 100, name)
    p.showPage()
    p.save()

    pdf_out = output.getvalue()
    output.close()

    return pdf_out
