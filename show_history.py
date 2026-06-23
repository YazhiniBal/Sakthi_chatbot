import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

cursor.execute("""
SELECT question, answer
FROM chat_history
ORDER BY id DESC
""")

rows = cursor.fetchall()

for row in rows:
    print("Question:", row[0])
    print("Answer:", row[1])
    print("----------------")

conn.close()