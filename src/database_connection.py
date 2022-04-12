from cgitb import text
import sqlite3

db = sqlite3.connect("worktime.db")
db.isolation_level = None

db.execute("CREATE TABLE Worktime (id INTEGER PRIMARY KEY, time INTEGER, explanation TEXT")

