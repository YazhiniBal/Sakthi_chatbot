from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Company Bot is Running"

@app.route("/ask/ERP")
def ask():
    return jsonify({
        "question": "ERP",
        "answer": "Enterprise Resource Planning"
    })

app.run()