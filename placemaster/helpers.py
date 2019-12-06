"""Index and login/logout views for placemaster."""
import flask
import datetime
import placemaster
import placemaster.secretKeys as secretKeys
from requests_oauthlib import OAuth2Session
from flask_login import UserMixin


db = placemaster.db


class User(placemaster.db.Model, UserMixin):
    """Abstraction of user login for postgres db."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    avatar = db.Column(db.String(200))
    tokens = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())

db.create_all()

class Auth:
    """Google Authorization Credentials."""

    CLIENT_ID = (secretKeys.GOOGLE_CLIENT_ID)  # Keep the parentheses
    CLIENT_SECRET = secretKeys.GOOGLE_CLIENT_SECRET
    REDIRECT_URI = 'http://127.0.0.1:5000/login/callback'

    # URIs determined by Google
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    SCOPE = ['profile', 'email']  # Could edit for more available scopes


@placemaster.login_manager.user_loader
def load_user(user_id):
    """Let user with flask_login api."""
    return User.query.get(int(user_id))


def get_google_auth(state=None, token=None):
    """O-Auth Session creation."""
    if token:
        return OAuth2Session(Auth.CLIENT_ID, token=token)
    if state:
        return OAuth2Session(
            Auth.CLIENT_ID,
            state=state,
            redirect_uri=Auth.REDIRECT_URI)
    oauth = OAuth2Session(
        Auth.CLIENT_ID,
        redirect_uri=Auth.REDIRECT_URI,
        scope=Auth.SCOPE)
    return oauth
