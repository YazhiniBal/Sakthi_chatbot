import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM keywords")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()