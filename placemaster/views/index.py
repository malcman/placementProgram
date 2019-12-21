"""Classes for index views."""
import flask
from flask.views import View
from flask_login import login_required

from placemaster.model import query, db
from placemaster.model.placement import Placement


class IndexView(View):
    """Class based view for index page."""

    url = '/'
    endpoint = 'index'
    template = 'index.html'
    decorators = [login_required]

    def dispatch_request(self):
        """Override default View function.

        See https://flask.palletsprojects.com/en/1.1.x/views/ for more info
        on pluggable views.

        Lists all placements for this user,
        or allows creation of new placement.
        """
        context = {}
        context['placements'] = query(Placement).all()
        print(context['placements'])
        return flask.render_template(IndexView.template, **context)


__all__ = ['IndexView']
