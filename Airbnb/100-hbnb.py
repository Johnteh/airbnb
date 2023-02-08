#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb: HBnB home page.
"""
import os
from models import storage
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://{}:{}@{}/{}".format(os.environ.get("HBNB_MYSQL_USER"), os.environ.get("HBNB_MYSQL_PWD"), os.environ.get("HBNB_MYSQL_HOST"), os.environ.get("HBNB_MYSQL_DB"))
                                      

db = SQLAlchemy(app)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)

            
@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)

@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with a list of all states and related cities.
    States/cities are sorted by name.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")

@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)




@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)