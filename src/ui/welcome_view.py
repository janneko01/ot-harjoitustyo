from tkinter import ttk, constants, StringVar
from bingo_repository import BingoRepository


class WelcomeView:
    def __init__(self, root, show_create_bingo_sheets_view, show_play_bingo_view):
        self._root = root
        self.show_create_bingo_sheets_view = show_create_bingo_sheets_view
        self.show_play_bingo_view = show_play_bingo_view
        self._frame = None
        self.games = BingoRepository().get_game_names()
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self.variable = StringVar(self._frame)
        self.variable.set(self.games[0])
        game_select = ttk.OptionMenu(self._frame, self.variable, *self.games)

        play_now_button = ttk.Button(
            master=self._frame,
            text="Pelaa nyt",
            command=self.show_play_bingo_view
        )

        create_bingo_sheets_button = ttk.Button(
            master=self._frame,
            text="Luo bingolappuja",
            command=self.show_create_bingo_sheets_view
        )

        game_select.grid(padx=5, pady=5, sticky=constants.NW)
        play_now_button.grid(padx=5, pady=5, sticky=constants.NE)
        create_bingo_sheets_button.grid(padx=5, pady=5, sticky=constants.NW)
