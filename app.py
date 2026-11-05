
from flask import Flask, jsonify, request, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
notes = []

@app.route("/")
def home():
    return "Hello, version 2!"

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

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
