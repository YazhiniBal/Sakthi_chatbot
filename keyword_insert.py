import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS keywords(
    keyword TEXT,
    answer TEXT
)
""")

keywords = [
("bio-earth", "Bio-Earth is an organic soil conditioner that improves soil fertility."),
("ethanol", "Sakthi Sugars manufactures anhydrous ethanol used for blending with petrol."),
("bagasse", "Bagasse is used as fuel in co-generation power plants."),
("head office", "180, Race Course Road, Coimbatore – 641018, Tamil Nadu, India."),
("career", "Current openings and HR policies are available in the careers section.")
]

cursor.executemany(
    "INSERT INTO keywords VALUES (?, ?)",
    keywords
)

conn.commit()
conn.close()

print("Keywords inserted successfully")