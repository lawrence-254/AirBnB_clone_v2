#!/usr/bin/python3
'''a script that starts a Flask web application'''


from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/', strict_slashes=False)
def hello():
    """
    returns 'Hello HBNB!'
    """
    return 'Hello HBNB!'

app.run(host='0.0.0.0', port='5000')
