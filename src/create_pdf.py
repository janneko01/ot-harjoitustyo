from fpdf import FPDF

class CreatePdf:
    def __init__(self) -> None:
        self.document = FPDF()
        self.document.set_font('Helvetica', 'b', 28)

    def square(self, x1, y1, size, value=''):
        self.document.line(x1, y1, x1+size, y1)
        self.document.line(x1+size, y1, x1+size, y1+size)
        self.document.line(x1, y1, x1, y1+size)
        self.document.line(x1, y1+size, x1+size, y1+size)
        self.document.text(x1+8, y1+17, str(value))

    def playing_field(self, x, y, size, numbers):
        self.document.add_page()
        self.square(x, y, size)
        for i in range(x, x+size, size//5):
            for j in range(y, y+size, size//5):
                self.square(j+3, i+3, size//5-6, numbers.pop(0))

    def save(self, filename):
        self.document.output(filename)


if __name__ == '__main__':
    p = CreatePdf()
    p.playing_field(20, 20, 160, [x for x in range(1,26)])
    p.save('bingosheets.pdf')
