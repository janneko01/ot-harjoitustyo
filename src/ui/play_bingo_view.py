from tkinter import ttk, constants, StringVar, DISABLED
from bingo_repository import BingoRepository


class PlayBingoView:
    def __init__(self, root, play, game_name, show_welcome_view):
        self._root = root
        self._play = play
        self.game_name = game_name
        self._play.start_game(self.game_name)
        self.show_welcome_view = show_welcome_view
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _draw(self):
        sheet, number = self._play.next_number()
        if sheet:
            self.value_number["state"] = DISABLED
            self._winner.set("Voitto kupongissa " + str(sheet + 1))
        n = self._numbers.get()
        if len(n) > 0:
            n += ', '
        n += str(number)
        self._numbers.set(n)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        back_button = ttk.Button(
            master=self._frame,
            text="<",
            command=self.show_welcome_view
        )

        self._numbers = StringVar()
        numbers_label = ttk.Label(self._frame, textvariable=self._numbers)

        self.value_number = ttk.Button(
            master=self._frame,
            text="Arvo numero",
            command=self._draw
        )
        self._winner = StringVar()
        winner_label = ttk.Label(self._frame, textvariable=self._winner)

        back_button.grid(padx=5, pady=5, sticky=constants.NW)
        winner_label.grid(padx=5, pady=5, sticky=constants.NW)
        numbers_label.grid(padx=5, pady=5, sticky=constants.NW)
        self.value_number.grid(padx=5, pady=5, sticky=constants.NW)
