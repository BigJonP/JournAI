from flask import Flask, request, jsonify
from utils.db import create_users_table, create_journal_table, add_user, add_journal_entry
from models.sentiment import sentiment_pipeline, emotion_pipeline

app = Flask(__name__)


@app.route("/journal", methods=["POST"])
def journal():
    entry = request.json["entry"]
    print("entry:", entry)
    sentiment = sentiment_pipeline(entry)[0]["label"]
    emotion = emotion_pipeline(entry)[0]["label"]
    print("sentiment:", sentiment)
    print("emotion:", emotion)
    add_journal_entry(1, entry, sentiment, emotion)
    return jsonify({"message": "Journal entry received"}), 200


if __name__ == "__main__":
    create_users_table()
    create_journal_table()
    add_user("John", "Doe", "john.doe@example.com", "password")
    app.run(debug=True)
