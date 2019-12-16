# """
# placemaster index view.

# URLs include:
# /
# """
# import os
# import json
# import flask
# from requests.exceptions import HTTPError
# import placemaster
# from placemaster.model import get_db
# from ..helpers import check_login, starter, get_google_auth

# # postgres
# # from flask_login import LoginManager, login_required, login_user
# # from flask_login import logout_user, current_user, UserMixin


# @placemaster.app.route('/', methods=['GET', 'POST'])
# def index():
#     """Display landing view for placemaster."""
#     context = {}
#     success = starter(context)
#     if success is not None:
#         return success
#     return flask.render_template('index.html', **context)


# @placemaster.app.route('/login')
# def login():
#     """Log user in with google, or return to login page."""
#     context = {}
#     auth_uri = os.environ.get('AUTH_URI', default=False)
#     if check_login(context):
#         return flask.redirect(flask.url_for('index'))
#     google = get_google_auth()
#     auth_url, state = google.authorization_url(
#         auth_uri,
#         access_type='offline')
#     flask.session['oauth_state'] = state
#     return flask.render_template('login.html', auth_url=auth_url)


# @placemaster.app.route('/logout')
# def logout():
#     """Log out currently authenticated user."""
#     # logout_user()
#     flask.session.clear()
#     return flask.redirect(flask.url_for('index'))


# @placemaster.app.route('/login/callback')
# def callback():
#     """Perform callback function for google oauth."""
#     args = flask.request.args
#     logged_in = check_login({})

#     # redirect logged in user to index view
#     username = flask.session.get('username', None)
#     if username is not None and logged_in:
#         return flask.redirect(flask.url_for('index'))

#     # error handling
#     if 'error' in args:
#         msg = 'Error encountered.'
#         if args.get('error') == 'access_denied':
#             msg = "Access was denied."
#         return msg

#     if 'code' not in args and 'state' not in args:
#         return flask.redirect(flask.url_for('login'))

#     # successful callback
#     else:
#         # get OAuth2Session
#         google = get_google_auth(state=flask.session['oauth_state'])

#         token_uri = os.environ.get('TOKEN_URI', default=False)
#         client_secret = placemaster.app.config['GOOGLE_CLIENT_SECRET']
#         user_info = os.environ.get('USER_INFO', default=False)
#         try:
#             token = google.fetch_token(
#                 token_uri,
#                 client_secret=client_secret,
#                 authorization_response=flask.request.url)
#         except HTTPError:
#             return 'HTTPError occurred.'
#         google = get_google_auth(token=token)
#         resp = google.get(user_info)
#         if resp.status_code == 200:
#             cur = get_db().cursor()
#             # get user's data
#             user_data = resp.json()
#             # save name as current user
#             flask.session['username'] = user_data['name']

#             # check to see if this user already exists
#             fullname = user_data['name']
#             sql = 'SELECT fullname FROM users WHERE fullname=?'
#             cur.execute(sql, (flask.session['username'],))

#             # add unknown user
#             if not cur.fetchall():
#                 email = user_data['email']
#                 tokens = json.dumps(token)
#                 avatar = user_data['picture']
#                 sql = 'INSERT INTO users(fullname, email, avatar, tokens)'
#                 sql += 'VALUES (?,?,?,?)'
#                 cur.execute(sql, (fullname, email, avatar, tokens))
#             cur.close()
#             return flask.redirect(flask.url_for('index'))
#         return 'Could not fetch your information.'
