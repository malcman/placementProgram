"""Classes for index views."""
import flask
from flask.views import View
from flask_login import login_required


class IndexView(View):
    """Class based view for index page."""

    url = '/'
    endpoint = 'index'
    template = 'index.html'
    decorators = [login_required]

    def dispatch_request(self):
        """Override default View function.

        See https://flask.palletsprojects.com/en/1.1.x/views/ for more info.
        """
        return flask.render_template(IndexView.template)


__all__ = ['IndexView']
