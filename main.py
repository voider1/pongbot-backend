from flask import Flask

app = Flask(__name__)


@app.route("/")
def get():
    pass


@app.route("/", methods=["POST"])
def post():
    pass
