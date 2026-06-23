import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

faqs = [

# Greetings
("Hi", "Hello! Welcome to Sakthi Sugars. How can I help you?"),
("Hello", "Hello! How can I assist you today?"),
("Good morning", "Good morning! Welcome to Sakthi Sugars."),
("Good afternoon", "Good afternoon! How may I help you?"),
("Good evening", "Good evening! How can I assist you?"),

# Normal conversation
("How are you?", "I'm doing well. How can I help you with Sakthi Sugars information?"),
("Who are you?", "I am the Sakthi Sugars Chatbot. I can answer questions about the company and its products."),
("Thank you", "You're welcome! Happy to help."),
("Thanks", "You're welcome!"),
("Bye", "Goodbye! Have a great day."),
("See you later", "See you! Feel free to come back if you need any information."),

# Company information
("When was Sakthi Sugars established?",
 "Sakthi Sugars Limited was established in 1961."),

("What products does Sakthi Sugars manufacture?",
 "Sakthi Sugars manufactures sugar, ethanol, industrial alcohol, power, Bio-Earth and other by-products."),

("What is ethanol?",
 "Ethanol is an alcohol produced by Sakthi Sugars and used for blending with petrol."),

("What is molasses?",
 "Molasses is a by-product of sugar manufacturing used in alcohol production."),

("What is press mud?",
 "Press mud is a by-product obtained during sugar manufacturing and is used as organic fertilizer."),

("What is bagasse?",
 "Bagasse is the fibrous residue left after extracting juice from sugarcane and is used as fuel in co-generation plants."),

("How many power plants does Sakthi Sugars have?",
 "Sakthi Sugars operates three co-generation power plants with a combined capacity of 92 MW."),

("Where are the manufacturing units located?",
 "The manufacturing units are located at Sakthinagar, Sivaganga and Modakurichi in Tamil Nadu."),

("How can I contact Sakthi Sugars?",
 "Phone: +91-422-2221551-4 / +91-422-4322222. Email: info@sakthisugars.com"),

("Does Sakthi Sugars offer jobs?",
 "Yes. Career opportunities and openings are available through the company's careers section."),

("Is Sakthi Sugars listed on stock exchanges?",
 "Yes. Sakthi Sugars Limited is listed on NSE and BSE."),

("What is Bio-Earth used for?",
 "Bio-Earth is an organic soil conditioner that improves soil fertility."),

("What is sugarcane?",
 "Sugarcane is the primary raw material used in the manufacture of sugar and ethanol."),

("What is co-generation?",
 "Co-generation is the simultaneous production of electricity and useful heat from bagasse.")
]

cursor.executemany(
    "INSERT INTO faq VALUES (?, ?)",
    faqs
)

conn.commit()
conn.close()

print("Additional FAQs inserted successfully.")