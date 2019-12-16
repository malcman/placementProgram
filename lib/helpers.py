"""Helper functions for placemaster."""
import hashlib
import os
import shutil
import tempfile
import flask
# import placemaster
# import placemaster.secretKeys as secretKeys
# from placemaster.model import get_db
from requests_oauthlib import OAuth2Session
# import datetime
# from flask_login import UserMixin


# db = placemaster.db


# SQLAlchemy userloader
# @placemaster.login_manager.user_loader
# def load_user(user_id):
#     """Let user with flask_login api."""
#     return User.query.get(int(user_id))


# sqlite starter helper
# def starter(context):
#     """Check login and get context."""
#     if not check_login(context):
#         return flask.redirect(flask.url_for('login'))

#     if flask.request.method == 'POST':
#         handle_basic_actions()
#     return None


# def verify_post_request():
#     """Aborts with 403 if username is not in session."""
#     if 'username' not in flask.session:
#         flask.abort(403)


# def sha256sum(filename):
#     """Return sha256 hash of file content, similar to UNIX sha256sum."""
#     content = open(filename, 'rb').read()
#     sha256_obj = hashlib.sha256(content)
#     return sha256_obj.hexdigest()


# def check_login(context):
#     """
#     Check if there is a logged in user.

#     If so, sets context['logged_in'] to True and returns,
#     Else sets context['logged_in'] to False and redirects to login page.
#     """
#     if 'username' in flask.session:
#         cur = get_db().cursor()
#         sql = 'SELECT fullname FROM users WHERE fullname=?'
#         cur.execute(sql, (flask.session['username'],))
#         if cur.fetchall():
#             context['logged_in'] = True
#             context['logname'] = flask.session['username']
#             cur.close()
#             return True
#         cur.close()
#     flask.session.pop('username', None)
#     context['logged_in'] = False
#     return False


# def store_file():
#     """Store uploaded file and return hashed name."""
#     dummy, temp_filename = tempfile.mkstemp()
#     file = flask.request.files["file"]
#     file.save(temp_filename)

#     # Compute filename
#     hash_txt = sha256sum(temp_filename)
#     dummy, suffix = os.path.splitext(file.filename)
#     hash_filename_basename = hash_txt + suffix
#     hash_filename = os.path.join(
#         flask.current_app.config["UPLOAD_FOLDER"],
#         hash_filename_basename
#     )

#     # Move temp file to permanent location
#     shutil.move(temp_filename, hash_filename)
#     return hash_filename_basename


# def handle_basic_actions():
#     """Determine which helper to call based on submit name."""
#     verify_post_request()
#     cur = get_db().cursor()

#     # if 'key' in flask.request.form:
#     # call handler

#     cur.close()


def get_google_auth(state=None, token=None):
    """O-Auth Session creation."""
    client_id = flask.current_app.config['GOOGLE_CLIENT_ID']
    redirect = os.environ.get('REDIRECT_URI', default=False)
    oauth_scope = os.environ.get('OAUTH_SCOPE', default=False)
    if token:
        return OAuth2Session(client_id, token=token)
    if state:
        return OAuth2Session(
            client_id,
            state=state,
            redirect_uri=redirect)
    oauth = OAuth2Session(
        client_id,
        redirect_uri=redirect,
        scope=oauth_scope)
    return oauth
