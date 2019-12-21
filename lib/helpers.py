"""Helper functions for placemaster."""
import hashlib
import os
import shutil
import tempfile
import flask
from requests_oauthlib import OAuth2Session


def sha256sum(filename):
    """Return sha256 hash of file content, similar to UNIX sha256sum."""
    content = open(filename, 'rb').read()
    sha256_obj = hashlib.sha256(content)
    return sha256_obj.hexdigest()


def store_file(file):
    """Store uploaded file and return hashed name.

    file parameter can be grabbed from flask.request.files['formname']
    Returns hashed filename which can be securely stored in db
    """
    dummy, temp_filename = tempfile.mkstemp()
    file.save(temp_filename)

    # Compute filename
    hash_txt = sha256sum(temp_filename)
    dummy, suffix = os.path.splitext(file.filename)
    hash_filename_basename = hash_txt + suffix
    hash_filename = os.path.join(
        flask.current_app.config["UPLOAD_FOLDER"],
        hash_filename_basename
    )

    # Move temp file to permanent location
    shutil.move(temp_filename, hash_filename)
    return hash_filename_basename


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
