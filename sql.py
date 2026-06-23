import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

# Remove old table
cursor.execute("DROP TABLE IF EXISTS faq")

# Create new table
cursor.execute("""
CREATE TABLE faq(
    question TEXT,
    answer TEXT
)
""")

# Insert data
cursor.execute(
    "INSERT INTO faq VALUES (?, ?)",
    ("What is ERP?", "Enterprise Resource Planning")
)
cursor.execute(
    "INSERT INTO faq VALUES (?, ?)",
    ("ETHANOL", "Yes, Sakthi Sugars Limited produces ethanol.")
)
conn.commit()

# Read data
cursor.execute("SELECT * FROM faq")
rows = cursor.fetchall()

print(rows)
print("Database created successfully!")
conn.close()