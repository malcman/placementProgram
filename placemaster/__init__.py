"""Initialization for placemaster program."""
import flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__, instance_relative_config=True)  # pylint: disable=invalid-name


# db = SQLAlchemy(app)  # pylint: disable=invalid-name
# login_manager = LoginManager(app)  # pylint: disable=invalid-name
# login_manager.login_view = "login"
# login_manager.session_protection = "strong"  # because we are using oauth

# Read settings from config module (placemaster/config.py)
app.config.from_object('placemaster.config')

# Read specific instance values
# must be ./instance/config.py
# contains GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET
app.config.from_pyfile('config.py')

# Overlay settings read from file specified by environment variable. This is
# useful for using different on development and production machines.
# Reference: http://flask.pocoo.org/docs/0.12/config/
app.config.from_envvar('PLACEMASTER_SETTINGS', silent=True)


import placemaster.views  # noqa: E402  pylint: disable=wrong-import-position
