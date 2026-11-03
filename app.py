from flask import Flask, jsonify, request

app = Flask(__name__)
notes = []  # notes are stored in memory (simple on purpose)


@app.route("/")
def home():
    return "Hello from my Notes API!"


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)


@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json()
    notes.append(data)
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)