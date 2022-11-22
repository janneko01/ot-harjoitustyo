
from fpdf import FPDF
import random

class bingoSheets:

    def create_bingo_sheets(amount):
        pdf = FPDF('P', 'mm', 'A4')
        for i in amount:
            pdf.add_page()
            pdf.set_font('helvetica', '', 16)
            numbers = []
            for i in range(25):
                number = random.randrange(1, 100)
                numbers.append(number)
            pdf.cell()


        pdf.output('bingolaput.pdf')