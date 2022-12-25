from bingo_repository import BingoRepository
import random

class play:
    def __init__(self, gameName):
        self.numbers = []
        self.sheets = BingoRepository.get_by_game_name(gameName)

    def start_game(self):
        pass

    def draw_number(self):
        while True:
            number = random.randrange(1, 75)
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

            # Vino ylös tarkastukset
            for i in range(5):
                oikein = 0
                if sheet[2 + 5*i + i] in self.numbers:
                    oikein += 1
                if oikein > 4:
                    return sheet[1]

            # Vino alas tarkastukset
            for i in range(5):
                oikein = 0
                if sheet[2 + 5*i + (4-i)] in self.numbers:
                    oikein += 1
                if oikein > 4:
                    return sheet[1]
