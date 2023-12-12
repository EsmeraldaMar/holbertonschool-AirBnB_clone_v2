#!/usr/bin/python3
"""
Starts a web flask application
Fetches data from the storage engine
Route:
/states_list: display a HTML page with
 a list of all states and related cities.
"""
from models import storage
from flask import Flask, render_template

# creates instance of flask class (WSGI app)
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Displays an HTML page with a list of all state
    objects in DB storage, states are sorted by name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
