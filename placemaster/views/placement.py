"""Classes for placement views."""
import flask
from flask.views import View
from flask_login import login_required
from placemaster.model import query


class PlacementView(View):
    """Class-based view for placement page."""

    url = '/placement/<id>'
    endpoint = 'placement'
    template = 'placement.html'

    def dispatch_request(self):
        """Override default View function.

        See https://flask.palletsprojects.com/en/1.1.x/views/ for more info.
        """
        context = {}
        context['placements'] = query(Placement).all()
        return flask.render_template(PlacementView.template)


__all__ = ['PlacementView']
