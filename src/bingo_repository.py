from database_connection import get_database_connection


class BingoRepository:
    def __init__(self):
        self._connection = get_database_connection()

    def add(self, game_name, id, numbers):
        data = [game_name, id] + numbers
        cursor = self._connection.cursor()
        cursor.execute("insert into sheets values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
            
        self._connection.commit()
