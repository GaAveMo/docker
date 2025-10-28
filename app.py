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
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Docker Flask service!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




