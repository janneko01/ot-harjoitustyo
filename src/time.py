#laskee työaikaan käytetyn ajan ja lisää sen tietokantaan

import time
import database_connection

def start():
    start = time.time()

def stop(explanation):
    stop = time.time()
    usedTime = stop - start
    database_connection.db.execute("INSERT INTO Worktime (time, explanation) VALUES (?, ?)" [usedTime, explanation])