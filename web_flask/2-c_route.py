#!/usr/bin/python3
'''a script that starts a Flask web application'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """returns 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """returns args"""
    args = text.replace("_", " ")
    return f"C {args}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
