from flask import Flask, request, jsonify, render_template
import sqlite3
import difflib

app = Flask(__name__)
last_topic = ""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin")
def admin():

    return render_template("admin.html")
@app.route("/add_faq", methods=["POST"])
def add_faq():

    question = request.form["question"]
    answer = request.form["answer"]

    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO faq VALUES (?, ?)",
        (question, answer)
    )

    conn.commit()
    conn.close()

    return "FAQ Added Successfully!"

@app.route("/api/ask")
def api_ask():

    global last_topic

    question = request.args.get("question")

    if not question:
        return jsonify({"answer": "Please enter a question."})

    question = question.lower()

    # ===== MEMORY =====
    if "sakthi sugars" in question:
        last_topic = "sakthi sugars"

    if "where" in question and last_topic == "sakthi sugars":
        return jsonify({
            "answer": "Sakthi Sugars Limited is located at 180, Race Course Road, Coimbatore – 641018, Tamil Nadu, India."
        })

    if "products" in question and last_topic == "sakthi sugars":
        return jsonify({
            "answer": "Sakthi Sugars manufactures sugar, industrial alcohol, ethanol, power and by-products."
        })

    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()


    # ===== INTENT SEARCH =====
    cursor.execute("SELECT keywords, answer FROM intents")

    rows = cursor.fetchall()

    words = question.split()

    for row in rows:

        keywords = row[0].split(",")

        for keyword in keywords:

            if keyword.strip() in question.lower():

                answer = row[1]
                cursor.execute(
               "INSERT INTO chat_history(question, answer) VALUES (?, ?)",
                (question, answer)
                )

                conn.commit()
                conn.close()

                return jsonify({
                    "answer": answer
                })

    # ===== FAQ SEARCH =====
    cursor.execute("SELECT question, answer FROM faq")

    faq_rows = cursor.fetchall()

    questions = [row[0].lower() for row in faq_rows]

    match = difflib.get_close_matches(
        question,
        questions,
        n=1,
        cutoff=0.6
    )

    if match:

        for row in faq_rows:

            if row[0].lower() == match[0]:

                answer = row[1]
                cursor.execute(
               "INSERT INTO chat_history(question, answer) VALUES (?, ?)",
                (question, answer)
                )

                conn.commit()
                conn.close()

                return jsonify({
                    "answer": answer
                })

    # ===== KEYWORD SEARCH =====
    cursor.execute("SELECT keyword, answer FROM keywords")

    keyword_rows = cursor.fetchall()

    for row in keyword_rows:

        keyword = row[0].lower()

        if keyword in question:

            answer = row[1]
            cursor.execute(
               "INSERT INTO chat_history(question, answer) VALUES (?, ?)",
                (question, answer)
                )

            conn.commit()
            conn.close()

            return jsonify({
                "answer": answer
            })
    cursor.execute(
               "INSERT INTO chat_history(question, answer) VALUES (?, ?)",
                (question, answer)
                )
    conn.commit()
    conn.close()

    return jsonify({
        "answer": "Sorry, I don't know the answer to that question."
    })


app.run(debug=True)