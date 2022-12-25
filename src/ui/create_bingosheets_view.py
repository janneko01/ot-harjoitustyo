from tkinter import ttk, constants
from bingosheets import bingoSheets
from bingo_repository import BingoRepository
import os
import sys


class CreateBingosheetsView:
    def __init__(self, root, show_welcome_view):
        self._root = root
        self.show_welcome_view = show_welcome_view
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _create_sheets(self):
        name = self.game_name_entry.get()
        amount = int(self.amount_entry.get())
        bingoSheets().create_bingo_sheets(name, amount)
        if sys.platform.startswith("linux"):
            os.system("xdg-open bingosheets.pdf")
        elif sys.platform.startswith("darwin"):
            os.system("open bingosheets.pdf")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        game_name_label = ttk.Label(master=self._frame, text="Pelin nimi:")
        self.game_name_entry = ttk.Entry(master=self._frame)

        amount_label = ttk.Label(
            master=self._frame, text="Bingolappujen määrä:")
        self.amount_entry = ttk.Entry(master=self._frame)

        create_bingo_sheets_button = ttk.Button(
            master=self._frame,
            text="Luo bingolaput",
            command=self._create_sheets
        )
        back_button = ttk.Button(
            master=self._frame,
            text="<",
            command=self.show_welcome_view
        )

        game_name_label.grid(padx=5, pady=5, sticky=constants.NW)
        self.game_name_entry.grid(padx=5, pady=5, sticky=constants.NE)

        amount_label.grid(padx=5, pady=5, sticky=constants.NW)
        self.amount_entry.grid(padx=5, pady=5, sticky=constants.NE)

        create_bingo_sheets_button.grid(padx=5, pady=5, sticky=constants.NW)
        back_button.grid(padx=5, pady=5, sticky=constants.NW)
