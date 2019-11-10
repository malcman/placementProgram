import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (insta485/config.py)
app.config.from_object('placemaster.config')

# Overlay settings read from file specified by environment variable. This is
# useful for using different on development and production machines.
# Reference: http://flask.pocoo.org/docs/0.12/config/
app.config.from_envvar('PLACEMASTER_SETTINGS', silent=True)

import placemaster.views  # noqa: E402  pylint: disable=wrong-import-position