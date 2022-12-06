from fpdf import FPDF
import random
from bingo_repository import BingoRepository
from create_pdf import CreatePdf

class bingoSheets:
    def create_bingo_numbers(self):
        numbers = []
        while len(numbers) < 25:
            number = random.randint(1, 75)
            if number in numbers:
                continue
            numbers.append(number)
        BingoRepository().add("Game name", 4, numbers)
        return numbers

    def create_bingo_sheets(self):
        numbers = self.create_bingo_numbers()
        pdf = CreatePdf()
        pdf.playing_field(20, 20, 160, numbers)
        pdf.save("bingosheets.pdf")

if __name__ == "__main__":
    bingoSheets().create_bingo_sheets()
