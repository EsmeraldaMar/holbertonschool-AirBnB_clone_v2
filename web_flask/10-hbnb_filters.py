#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    Routes:
/hbnb_filters: display a HTML filters page
"""
from models import storage
from flask import Flask, render_template


# creates instance of flask class (WSGI app)
app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ displays main HBNB filters HTML page """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
