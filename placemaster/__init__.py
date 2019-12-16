"""Initialization for placemaster program."""
import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
from placemaster.views import init_views
from placemaster.google_login import create_google_login_blueprint
from placemaster.model import init_db
from placemaster.model.User import User


# create extensions but do not yet initialize them with an app instance
db = init_db()  # pylint: disable=invalid-name
login_manager = LoginManager()  # pylint: disable=invalid-name


def create_app(config_name):
    """Create application with specific configuration settings.

    Factory function that allows for dynamic creation of placemaster
    application with dev and production settings.
    """
    # app is a single object used by all the code modules in this package
    app = flask.Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])

    # Read specific instance values
    # must be ./instance/config.py
    # contains GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET
    app.config.from_pyfile('config.py')

    # Overlay settings read from file specified by environment variable. This is
    # useful for using different on development and production machines.
    # Reference: http://flask.pocoo.org/docs/0.12/config/
    app.config.from_envvar('PLACEMASTER_SETTINGS', silent=True)

    # initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # add views defined in views package
    init_views(app)

    # add blueprint packages

    # google oauth
    google_bp = create_google_login_blueprint()
    app.register_blueprint(google_bp)

    login_manager.login_view = "google_auth.login"
    login_manager.session_protection = "strong"  # because we are using oauth

    @login_manager.user_loader
    def load_user(user_id):
        """Verify authentication for views that require login."""
        return User.query.get(int(user_id))

    return app
