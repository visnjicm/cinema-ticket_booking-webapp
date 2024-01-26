from fpdf import FPDF
import webbrowser
import os

from filesharer import FileSharer


class PdfReport:

    def __init__(self, filename):
        self.file_url = None
        self.filename = filename

    def generate(self, name, ticket_id, price, seat_number):
        # flatmate1_pay = "$" + str(round(flatmate1.pays(bill, flatmate2), 2))
        # flatmate2_pay = "$" + str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        # pdf.image(name="OOP/Project 2/files/house.png", x=10, y=10, w=50, h=50)

        # Insert title
        pdf.set_font(family='Times', size=24, style='BU')
        pdf.cell(w=0, h=80, txt='Your Digital Ticket', border=1, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=22, style='B')
        pdf.cell(w=100, h=40, txt="Name:", border=1, align='L', ln=0)
        pdf.cell(w=150, h=40, txt=str(name), border=1, align='L', ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=20, style='')
        pdf.cell(w=100, h=40, txt="Ticket ID", border=1, align='L', ln=0)
        pdf.cell(w=150, h=40, txt=str(ticket_id), border=1, align='L', ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=40, txt="Price:", border=1, align='L', ln=0)
        pdf.cell(w=150, h=40, txt=str(price), border=1, align='L', ln=1)

        pdf.cell(w=100, h=40, txt="Seat #", border=1, align='L', ln=0)
        pdf.cell(w=150, h=40, txt=str(seat_number), border=1, align='L', ln=1)

        # Open the PDF
        pdf.output(self.filename)
        # webbrowser.open("file:///home/marko/Python/OOP/Project 2/files/" + self.filename)

        # Fileshare
        file_share = FileSharer(filepath=self.filename)
        self.file_url = file_share.share()
        return self.file_url
