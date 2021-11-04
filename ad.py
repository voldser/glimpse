import sqlite3
import os

db = sqlite3.connect('fish.db', check_same_thread = False)
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS fish (
    id BIGINT,
    name TEXT,
    download BOOLEAN
)""")
a = 0
for i in os.listdir('fish'):
	a += 1
	sql.execute(f"INSERT INTO fish VALUES (?, ?, ?)", (a, i, 0))
	db.commit()
