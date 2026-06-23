import pandas as pd
import sqlite3

# Read Excel file
df = pd.read_excel("faqs.xlsx")

# Connect to SQLite database
conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

# Create FAQ table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS faq(
    question TEXT,
    answer TEXT
)
""")

# Optional: Clear old FAQs
cursor.execute("DELETE FROM faq")

# Insert data from Excel into SQLite
for index, row in df.iterrows():

    cursor.execute(
        "INSERT INTO faq VALUES (?, ?)",
        (row["question"], row["answer"])
    )

conn.commit()
conn.close()

print("FAQs imported successfully!")