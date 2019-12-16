"""Initializer for google_login Flask blueprint package."""
import flask
from .views import init_views


def create_google_login_blueprint():
    """Create and return flask blueprint for google oauth."""
    google_bp = flask.Blueprint(
        'google_auth',
        __name__,
        template_folder='templates'
    )
    # get google_login module name
    module_name = __name__.split('.')[-1]

    # add views to this blueprint
    init_views(google_bp, module_name)
    return google_bp
