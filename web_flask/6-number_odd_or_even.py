#!/usr/bin/python3
'''a script that starts a Flask web application'''
from flask import Flask, render_template

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


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text="is cool"):
    """returns args with default value"""
    args = text.replace("_", " ")
    return f"Python {args}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Displays a HTML page """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """ Dislays a HTML page containing even or odd number """
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
