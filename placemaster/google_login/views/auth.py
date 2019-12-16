"""Class-based views for google OAuth login, logout."""
import flask
import os
import json
from flask.views import View
from flask_login import login_user, logout_user, current_user
from requests.exceptions import HTTPError
from lib.helpers import get_google_auth
from placemaster import db, login_manager
from placemaster.model.User import User


class LoginView(View):
    """Class based view for login page."""

    url = '/login'
    endpoint = 'login'
    template = 'login.html'

    def dispatch_request(self):
        """Override default View function.

        See https://flask.palletsprojects.com/en/1.1.x/views/ for more info.
        """
        context = {}
        auth_uri = os.environ.get('AUTH_URI', default=False)
        print('AUTH_URI: ', auth_uri)

        if current_user.is_authenticated:
            return flask.redirect(flask.url_for('index'))

        google = get_google_auth()
        auth_url, state = google.authorization_url(
            auth_uri,
            access_type='offline')
        flask.session['oauth_state'] = state
        return flask.render_template(LoginView.template, auth_url=auth_url)


class LogoutView(View):
    """Class based view for logout page."""

    url = '/logout'
    endpoint = 'logout'
    template = None

    def dispatch_request(self):
        """Override default View function."""
        logout_user()
        return flask.redirect(flask.url_for('index'))


class GoogleCallback(View):
    """Perform callback authentication for Google OAuth."""

    url = '/login/callback'
    endpoint = 'google_callback'
    template = None

    def check_callback_errors(self):
        """Check for already logged-in user and response errors.

        Returns error message or redirects if necessary.
        Otherwise, simply returns.
        """
        args = flask.request.args
        logged_in = current_user is not None and current_user.is_authenticated

        # redirect logged in user to index view
        if logged_in:
            flask.redirect(flask.url_for('index'))

        # error handling
        if 'error' in args:
            msg = 'Error encountered.'
            if args.get('error') == 'access_denied':
                msg = "Access was denied."
            return msg

        if 'code' not in args and 'state' not in args:
            return flask.redirect(flask.url_for('login'))

    def dispatch_request(self):
        """Override default View function."""
        issue = self.check_callback_errors()
        if issue:
            return issue

        # get OAuth2Session
        google = get_google_auth(state=flask.session['oauth_state'])

        token_uri = os.environ.get('TOKEN_URI', default=False)
        client_secret = flask.current_app.config['GOOGLE_CLIENT_SECRET']
        user_info = os.environ.get('USER_INFO', default=False)
        try:
            token = google.fetch_token(
                token_uri,
                client_secret=client_secret,
                authorization_response=flask.request.url)
        except HTTPError:
            return 'HTTPError occurred.'
        google = get_google_auth(token=token)
        resp = google.get(user_info)
        if resp.status_code == 200:
            user_data = resp.json()
            email = user_data['email']
            user = User.query.filter_by(email=email).first()
            if user is None:
                user = User()
                user.email = email
            user.name = user_data['name']
            user.tokens = json.dumps(token)
            user.avatar = user_data['picture']
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            return flask.redirect(flask.url_for('index'))
        return 'Could not fetch your information.'


__all__ = ['LoginView', 'LogoutView', 'GoogleCallback']
