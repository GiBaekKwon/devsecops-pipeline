from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

API_SECRET_KEY = os.environ.get("API_SECRET_KEY", "")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")

def get_db():
    conn = sqlite3.connect("test.db")
    return conn

@app.route("/")
def index():
    return jsonify({"status": "ok", "message": "DevSecOps Test App"})

@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    conn = get_db()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    result = cursor.fetchall()
    return jsonify(result)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
