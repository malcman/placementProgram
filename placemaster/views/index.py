"""
placemaster index view.

URLs include:
/
"""
import json
import flask
import placemaster
import placemaster.helpers as helpers
from flask_login import LoginManager, login_required, login_user
from flask_login import logout_user, current_user, UserMixin
from requests.exceptions import HTTPError


db = placemaster.db


@placemaster.app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    """Display landing view for placemaster."""
    return flask.render_template('index.html')


@placemaster.app.route('/login')
def login():
    """Log user in with google, or return to login page."""
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for('index'))
    google = helpers.get_google_auth()
    auth_url, state = google.authorization_url(
        helpers.Auth.AUTH_URI, access_type='offline')
    flask.session['oauth_state'] = state
    print('OAUTH STATE: ', flask.session['oauth_state'])
    print(flask.session)
    return flask.render_template('login.html', auth_url=auth_url)


@placemaster.app.route('/logout')
@login_required
def logout():
    """Log out currently authenticated user."""
    logout_user()
    return flask.redirect(flask.url_for('index'))


@placemaster.app.route('/login/callback')
def callback():
    """Perform callback function for google oauth."""
    print('Session: ', flask.session)

    args = flask.request.args
    if current_user is not None and current_user.is_authenticated:
        return flask.redirect(flask.url_for('index'))
    if 'error' in args:
        msg = 'Error encountered.'
        if args.get('error') == 'access_denied':
            msg = "Access was denied."
        return msg

    if 'code' not in args and 'state' not in args:
        return flask.redirect(flask.url_for('login'))
    else:
        google = helpers.get_google_auth(state=flask.session['oauth_state'])
        try:
            token = google.fetch_token(
                helpers.Auth.TOKEN_URI,
                client_secret=helpers.Auth.CLIENT_SECRET,
                authorization_response=flask.request.url)
        except HTTPError:
            return 'HTTPError occurred.'
        google = helpers.get_google_auth(token=token)
        resp = google.get(helpers.Auth.USER_INFO)
        if resp.status_code == 200:
            user_data = resp.json()
            email = user_data['email']
            user = helpers.User.query.filter_by(email=email).first()
            if user is None:
                user = helpers.User()
                user.email = email
            user.name = user_data['name']
            user.tokens = json.dumps(token)
            user.avatar = user_data['picture']
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return flask.redirect(flask.url_for('index'))
        return 'Could not fetch your information.'
