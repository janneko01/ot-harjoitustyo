from ui.welcome_view import WelcomeView
from ui.play_bingo_view import PlayBingoView
from ui.create_bingosheets_view import CreateBingosheetsView


class UI:
    def __init__(self, root, play):
        self._root = root
        self._play = play
        self._current_view = None

    def start(self):
        self._show_welcome_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_welcome_view(self):
        self._hide_current_view()
        self._current_view = WelcomeView(
            self._root, self._show_create_bingo_sheets_view, self._show_play_bingo_view)
        self._current_view.pack()

    def _show_play_bingo_view(self):
        game_name = self._current_view.variable.get()
        self._hide_current_view()
        self._current_view = PlayBingoView(
            self._root, self._play, game_name, self._show_welcome_view)
        self._current_view.pack()

    def _show_create_bingo_sheets_view(self):
        self._hide_current_view()
        self._current_view = CreateBingosheetsView(
            self._root, self._show_welcome_view)
        self._current_view.pack()
