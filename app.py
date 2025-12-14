# lab2
# from http.server import SimpleHTTPRequestHandler, HTTPServer

# PORT = 8080

# class MyHandler(SimpleHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(b"Hello from Docker container!")

# if __name__ == "__main__":
#     server = HTTPServer(("0.0.0.0", PORT), MyHandler)
#     print(f"Server running on port {PORT}")
#     server.serve_forever()

# lab3
# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return jsonify({"message": "Hello from Docker Flask service!"})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

# lab4
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
DB_NAME = "messages.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Lab 4: Flask + Database is working!"})

@app.route('/messages', methods=['POST'])
def add_message():
    data = request.get_json()
    text = data.get("text")

    conn = get_db()
    conn.execute("INSERT INTO messages (text) VALUES (?)", (text,))
    conn.commit()
    conn.close()

    return jsonify({"status": "Message saved"})

@app.route('/messages', methods=['GElsT'])
def get_messages():
    conn = get_db()
    rows = conn.execute("SELECT * FROM messages").fetchall()
    conn.close()

    messages = [{"id": row["id"], "text": row["text"]} for row in rows]
    return jsonify(messages)

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT
        )
    """)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)





