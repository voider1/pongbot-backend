#!venv/bin/python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def get():
    return "Hello, world!"


@app.route("/", methods=["POST"])
def post():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
