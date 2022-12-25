from database_connection import get_database_connection


class BingoRepository:
    def __init__(self):
        self._connection = get_database_connection()

    def add(self, game_name, id, numbers):
        data = [game_name, id] + numbers
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into sheets values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
        self._connection.commit()

    def get_by_game_name(self, game_name):
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from sheets where game_name = ?", (game_name,))
        sheets = cursor.fetchall()
        return sheets

    def get_game_names(self):
        cursor = self._connection.cursor()
        cursor.execute("select distinct game_name from sheets")
        names = cursor.fetchall()
        names = [row[0] for row in names]
        return names
