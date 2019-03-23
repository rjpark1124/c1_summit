from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Index!</h1>"


@app.route("/hello")
def hello():
    return "<h1>Hello World!</h1>"


@app.route("/members")
def members():
    return "Members"

if __name__ == "__main__":
    app.run()