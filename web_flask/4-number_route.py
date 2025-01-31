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
    return "C {}".format(args)


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text="is cool"):
    """returns args with default value"""
    args = text.replace("_", " ")
    return "Python {}".format(args)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display  only if n is an integer"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
