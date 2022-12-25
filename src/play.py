from bingo_repository import BingoRepository
import random


class Play:
    def __init__(self):
        self.numbers = []
        self.sheets = None

    def start_game(self, game_name):
        self.numbers = []
        self.sheets = BingoRepository().get_by_game_name(game_name)

    def draw_number(self):
        if len(self.numbers) >= 75:
            return -1
        while True:
            number = random.randint(1, 75)
            if number not in self.numbers:
                self.numbers.append(number)
                return number

    def checkBingo(self):
        for sheet in self.sheets:
            # Vaakasuorat tarkastukset
            for i in range(5):
                oikein = 0
                for j in range(5):
                    if sheet[2 + 5*i + j] in self.numbers:
                        oikein += 1
                if oikein > 4:
                    return sheet[1]

            # Pystysuorat tarkastukset
            for i in range(5):
                oikein = 0
                for j in range(5):
                    if sheet[2 + 5*j + i] in self.numbers:
                        oikein += 1
                if oikein > 4:
                    return sheet[1]

            # Vino alas tarkastukset
            oikein = 0
            for i in range(5):
                if sheet[2 + 5*i + i] in self.numbers:
                    oikein += 1
            if oikein > 4:
                return sheet[1]

            # Vino ylös tarkastukset
            oikein = 0
            for i in range(5):
                if sheet[2 + 5*i + (4-i)] in self.numbers:
                    oikein += 1
            if oikein > 4:
                return sheet[1]

        return None

    def next_number(self):
        number = self.draw_number()
        sheet = self.checkBingo()
        return sheet, number
