import imp


import sqlite3

connection = sqlite3.connect()
connection.row_factoy = sqlite3.Row
