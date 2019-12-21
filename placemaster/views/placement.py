"""Classes for placement views."""
import flask
from flask.views import View
from flask_login import login_required
from placemaster.model import query, db
from placemaster.model.placement import Placement


class PlacementView(View):
    """Class-based view for placement page."""

    methods = ['GET', 'POST']
    url = '/placement/<id>/'
    endpoint = 'placement'
    template = 'placement.html'

    def dispatch_request(self, id):
        """Override default View function.

        See https://flask.palletsprojects.com/en/1.1.x/views/ for more info.
        """
        context = {}
        context['placement'] = query(Placement).filter_by(
            id=id).first()
        return flask.render_template(PlacementView.template, **context)


class CreatePlacement(View):
    """Class-based endpoint for placement creation."""

    methods = ['POST']
    url = '/placement/create/'
    endpoint = 'create_placement'
    template = 'placement.html'

    def dispatch_request(self):
        """Handle form POST action for account creation."""
        context = {}
        newPlacement = Placement()
        newPlacement.name = flask.request.form['placementTitle']
        print(newPlacement.name)
        db.session.add(newPlacement)
        db.session.commit()
        return flask.redirect(
            flask.url_for('placement', id=newPlacement.id)
        )


__all__ = ['PlacementView', 'CreatePlacement']
