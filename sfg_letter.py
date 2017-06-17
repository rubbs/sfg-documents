
# -*- coding: utf-8 -*-
import cStringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Table, ListFlowable, ListItem
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import (
    black,
    purple,
    white,
    yellow
)

# import time module
import time

from reportlab.lib.styles import getSampleStyleSheet

class SfgLetter(object):

    def __init__(self):
        ## set member variables to default values and create header
        # create pdf file
        self.output = cStringIO.StringIO()
        self.p = canvas.Canvas(self.output, pagesize=A4)
        self.width, self.height = A4

        # set absender
        self.shipper_name = 'Ruben Schwarz'
        self.shipper_position = '1. Vorsitzender'
        self.shipper_address = 'Hauptstr. 19/1, 75391 Gechingen'
        self.shipper_email = 'ruben.schwarz@sportfreunde-gechingen.de'

        # set recipient
        self.recipient_firstname = 'Fred'
        self.recipient_surname = 'Feuerstein'
        self.recipient_street = 'Hauptstr. 1'
        self.recipient_city = '12345 Musterstadt'

        #self.styles = getSampleStyleSheet()
        self.styles = self.get_styles()

    def get_pdf(self):
        ## fill in sfg header
        self.createParagraph('Sportfreunde Gechingen 1921 e.V.', 36, 23, self.styles['title'])

        self.createParagraph(self.shipper_name + ', ' + self.shipper_position, 116, 32, self.styles['footnote'])
        self.createParagraph(self.shipper_address, 116, 35.5, self.styles['footnote'])
        self.createParagraph(self.shipper_email, 116, 39, self.styles['footnote'])

        self.p.drawImage('resources/sfg-logo.jpg', 22*mm, 256*mm, width=13*mm, height=25*mm)
        self.p.drawImage('resources/sfgHeadl.jpg', 38*mm, 257*mm, width=75*mm, height=12*mm)
        self.p.drawImage('resources/sfgHeadr.jpg', 113*mm, 269*mm, width=75*mm, height=12*mm)

        # absender fuer fensterkuvert
        self.createParagraph('Sf Gechingen, Eichendorffstr. 1, 75391 Gechingen', 21, 49, self.styles['footnote'])
        self.p.line(21*mm, 246*mm, 79*mm, 246*mm)


        ## recipient
        self.createParagraph(self.recipient_firstname + ' ' + self.recipient_surname, 21, 65)
        self.createParagraph(self.recipient_street, 21, 71)
        self.createParagraph(self.recipient_city, 21, 79)
        #self.p.drawString(21*mm, 231*mm, self.recipient_firstname + ' ' + self.recipient_surname)
        #self.p.drawString(21*mm, 226*mm, self.recipient_street)
        #self.p.drawString(21*mm, 219*mm, self.recipient_city)

        ## date
        self.createParagraph(time.strftime("%d.%m.%Y"), 170, 100)

        ## anrede
        # TODO anrede anpassen
        self.createParagraph('Sehr geehrter Herr ' + self.recipient_surname + ',', 27, 113)

        # betreffzeile

        # Inhalt
        # Inhalt wird in tabelle gestellt um absatz zu machen

        yOffset = 173

        styles = self.styles

        bestaetigung = Paragraph('hiermit bestätige ich den Eingang Ihres Kündigungsschreibens bezüglich folgender Mitgliedschaften bei den Sportfreunden Gechingen:', styles['default'])
        content = Paragraph('<bullet>The rain in spain</bullet>', styles["default"])
        terminations = []

        # TODO create termination entries
        for x in range(0,2):
            terminations.append(Paragraph("sublist item " + `x`, styles["default"]))

        content = ListFlowable(terminations ,
             bulletType='bullet',
             start='square',
             ),

        satzung = Paragraph('Gemäß § 7 der Vereinssatzung ist eine Kündigung der Mitgliedschaft nur zum Ende des laufenden Kalenderjahres möglich und wirksam, wenn diese bis spätestens 30.11. schriftlich erklärt worden und beim Vereinsvorsitzenden eingegangen ist. Ihre Vereinsmitgliedschaft endet damit am 31.12.2016.', styles['default'])
        wunsch = Paragraph('Die Sportfreunde Gechingen bedauern den zum Jahresende anstehenden Austritt sehr und wünschen Ihnen für die Zukunft Gesundheit und alles Gute.', styles['default'])

        data= [[bestaetigung],[content],[satzung],[wunsch]]
        table = Table(data, colWidths=[160 * mm])

        # calculate y offset
        yOffset += (len(terminations) * 6)

        table.wrapOn(self.p, self.width, self.height)
        table.drawOn(self.p, *self.coord(25, yOffset, mm))


        #grusszeile
        yOffset += 15
        self.createParagraph('Mit sportlichen Grüßen', 27, yOffset)

        yOffset += 25
        self.createParagraph('Ruben Schwarz', 27, yOffset)
        yOffset += 3
        self.createParagraph('1. Vorsitzender', 27, yOffset, self.styles['footnote'])



        #self.createParagraph(content, 27, 170)



        self.p.showPage()
        self.p.save()

        pdf_out = self.output.getvalue()
        self.output.close()

        return pdf_out

    def get_styles(self):
        styles= {
            'default': ParagraphStyle(
                'default',
                fontName='Times-Roman',
                fontSize=14,
                leading=16,
                leftIndent=0,
                rightIndent=0,
                firstLineIndent=0,
                alignment=TA_LEFT,
                spaceBefore=0,
                spaceAfter=0,
                bulletFontName='Times-Roman',
                bulletFontSize=14,
                bulletIndent=0,
                textColor= black,
                backColor=None,
                wordWrap=None,
                borderWidth= 0,
                borderPadding= 0,
                borderColor= None,
                borderRadius= None,
                allowWidows= 1,
                allowOrphans= 0,
                textTransform=None,  # 'uppercase' | 'lowercase' | None
                endDots=None,
                splitLongWords=1,
            ),
        }
        styles['footnote'] = ParagraphStyle(
            'footnote',
            parent=styles['default'],
            fontName='Helvetica',
            fontSize=8,
            leading=8,
        )
        styles['title'] = ParagraphStyle(
            'title',
            parent=styles['default'],
            fontName='Helvetica-Bold',
            fontSize=13,
            leading=14,
        )
        return styles

    def createParagraph(self, ptext, x, y, style=None):
        """"""
        if not style:
            style = self.styles['default']
        p = Paragraph(ptext, style=style)
        p.wrapOn(self.p,  160*mm, self.height)
        p.drawOn(self.p, *self.coord(x, y, mm))

    def coord(self, x, y, unit=1):
        """
        # http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height -  y * unit
        return x, y
