from flask import Flask, jsonify, render_template, redirect
import os
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/hello")
def hello():
    return "<h1>Hello World HELLO WORLD!</h1>"


@app.route("/members")
def members():
    return "Members"

if __name__ == "__main__":
    app.run(debug=True)