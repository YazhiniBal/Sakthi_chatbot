import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

# Delete old table
cursor.execute("DROP TABLE IF EXISTS intents")

# Create table
cursor.execute("""
CREATE TABLE intents(
    intent TEXT,
    keywords TEXT,
    answer TEXT
)
""")

intents = [

("career",
"job,career,vacancy,recruitment,opening,work",
"Yes. Sakthi Sugars offers career opportunities. Please visit the careers section."),

("contact",
"phone,email,contact,call",
"Phone: +91-422-2221551-4 / +91-422-4322222, Email: info@sakthisugars.com"),

("bot",
"who are you,what is your name,whats your name,name",
"I am the Sakthi Sugars Chatbot. I can answer questions about the company and its products."),

("company",
"sakthi sugars,company,about,details,introduction",
"Sakthi Sugars Limited is one of India's leading sugar manufacturing companies, established in 1961. "
"It manufactures sugar, industrial alcohol, ethanol, power and other by-products."),

("location",
"location,located,address,head office,where",
"Head Office: 180, Race Course Road, Coimbatore – 641018, Tamil Nadu, India."),

("greeting",
"hello,good morning,good evening",
"Hello! Welcome to Sakthi Sugars. How may I assist you?"),

("ethanol",
"ethanol,petrol,fuel",
"Sakthi Sugars manufactures anhydrous ethanol used for blending with petrol."),

("bio-earth",
"bio-earth,soil,fertilizer",
"Bio-Earth is an organic soil conditioner used to improve soil fertility.")

]

cursor.executemany(
    "INSERT INTO intents VALUES (?, ?, ?)",
    intents
)

conn.commit()
conn.close()

print("Intent data inserted successfully")