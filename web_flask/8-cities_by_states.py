#!/usr/bin/python3
"""
Starts a web flask application
Fetches data from the storage engine
Route:
/cities_by_states: display a HTML page:
with a list of all states and related cities.
"""
from models import storage
from flask import Flask, render_template

# creates instance of flask class (WSGI app)
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Displays an HTML page with a list of all state and related cities
    objects in DB storage, states are sorted by name.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
