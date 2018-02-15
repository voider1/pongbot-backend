from flask import Flask, json, request

app = Flask(__name__)


@app.route("/")
def get():
    return "Hello, world!"


@app.route("/", methods=["POST"])
def post():
    pass
