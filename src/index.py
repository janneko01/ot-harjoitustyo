from tkinter import Tk
from ui.ui import UI
from play import Play


def main():
    play = Play()
    window = Tk()
    window.title("Bingo")
    window.geometry("800x500")
    ui_view = UI(window, play)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
