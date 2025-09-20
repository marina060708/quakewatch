from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to QuakeWatch!"

@app.route("/health")
def health():
    return jsonify(status="ok", message="QuakeWatch is healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
