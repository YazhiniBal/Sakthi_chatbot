import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

faqs = [
("What is Sakthi Sugars Limited?",
" Sakthi Sugars Limited is one of India's leading sugar manufacturing companies, established in 1961. The company manufactures sugar, industrial alcohol, ethanol, power, and other by-products."),

("Where is the head office of Sakthi Sugars located?",
"180, Race Course Road, Coimbatore – 641018, Tamil Nadu, India."),

("What products does Sakthi Sugars manufacture?",
"White Sugar, Refined Sugar, Industrial Alcohol, Ethanol, Power (Co-generation), Bio-Earth, Molasses, Bagasse and Press Mud."),

("What types of sugar are produced by Sakthi Sugars?",
"The company produces plantation white sugar and refined sugar meeting international quality standards."),

("Does Sakthi Sugars produce ethanol?",
"Yes. Sakthi Sugars manufactures anhydrous ethanol used for blending with petrol and reducing crude oil imports."),

("How many power plants does Sakthi Sugars operate?",
"The company operates three co-generation power plants with a combined capacity of 92 MW."),

("Where are Sakthi Sugars manufacturing units located?",
"Sakthinagar, Sivaganga and Modakurichi, Tamil Nadu, India."),

("What are the by-products obtained from sugar manufacturing?",
"Molasses, Bagasse, Press Mud and Bio-Earth (Organic fertilizer)."),

("How can customers contact Sakthi Sugars?",
"Phone: +91-422-2221551-4 / +91-422-4322222, Email: info@sakthisugars.com"),

("Does Sakthi Sugars offer career opportunities?",
"Yes. Current openings and HR policies are available on the company's careers section."),

("What is Bio-Earth?",
"Bio-Earth is an organic soil conditioner produced using sugar industry by-products and is used to improve soil fertility."),

("What is bagasse used for?",
"Bagasse is used as fuel in co-generation power plants for electricity production."),

("Is Sakthi Sugars listed on stock exchanges?",
"Yes. Sakthi Sugars Limited is listed on both NSE and BSE."),

("How can suppliers or customers send enquiries?",
"Customers and suppliers can submit enquiries through the contact form available on the official website or contact the respective unit directly.")
]

cursor.executemany(
    "INSERT INTO faq VALUES (?, ?)",
    faqs
)

conn.commit()
conn.close()

print("FAQs inserted successfully.")