
from tkinter import ttk, constants

class WelcomeView:
    def __init__ (self, root, show_create_bingo_sheets_view):
        self._root = root
        self.show_create_bingo_sheets_view = show_create_bingo_sheets_view
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        #self.pack = ttk.Frame(master=self._root)

        play_now_button = ttk.Button(
            master=self._frame,
            text="Pelaa nyt"
        )
        #play_now_button.pack()
        create_bingo_sheets_button = ttk.Button(
            master=self._frame,
            text="Luo bingolappuja",
            command=self.show_create_bingo_sheets_view
        )

        play_now_button.grid(padx=5, pady=5, sticky=constants.NE)
        create_bingo_sheets_button.grid(padx=5, pady=5, sticky=constants.NE)

