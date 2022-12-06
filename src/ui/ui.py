from tkinter import Tk, ttk, constants
from bingosheets import bingoSheets

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        label = ttk.Label(master=self._root, text="Tervetuloa bingoon!")
        pelaa = ttk.Button(master=self._root, text="Pelaa nyt")
        luo = ttk.Button(
            master=self._root,
            text="Luo bingolappuja",
            command=self._handle_button_click
            )

        label.pack(side=constants.TOP)
        pelaa.pack(side=constants.LEFT)
        luo.pack(side=constants.LEFT)

    def _handle_button_click(self):
        bingoSheets().create_bingo_sheets()

window = Tk()
window.title("Bingo")

ui = UI(window)
ui.start()

window.mainloop()