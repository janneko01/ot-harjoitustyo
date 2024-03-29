import os
import sqlite3

dirname = os.path.dirname("bingo.db")

connection = sqlite3.connect("bingo.db")
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
