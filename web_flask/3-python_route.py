#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
    /python/<text>: display “Python ”,
    followed by the value of the text variable
    default value of text is “is cool”
"""
from flask import Flask
# creates instance of flask class (WSGI app)
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints Hello HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
    """ Prints C and <text> """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text):
    """ Prints Python and <text> """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
