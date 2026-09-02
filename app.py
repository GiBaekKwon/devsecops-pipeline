from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# 취약점 1: 하드코딩된 시크릿 (Gitleaks가 탐지해야 할 대상)
API_SECRET_KEY = "AKIAZQ3EXPLR8K2NVJ4M"
DB_PASSWORD = "Sup3r$ecretP@ssw0rd2024"

def get_db():
    conn = sqlite3.connect("test.db")
    return conn

@app.route("/")
def index():
    return jsonify({"status": "ok", "message": "DevSecOps Test App"})

@app.route("/user")
def get_user():
    # 취약점 2: SQL Injection (Semgrep이 탐지해야 할 대상)
    user_id = request.args.get("id")
    conn = get_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    # 취약점 3: 디버그 모드 + 모든 인터페이스 바인딩
    app.run(host="0.0.0.0", port=5000, debug=True)
