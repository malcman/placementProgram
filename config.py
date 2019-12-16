"""Configuration for placemaster servers."""
import os
import placemaster.secretKeys as secretKeys


basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    """Specification for Config base."""

    # Secret key for encrypting cookies
    SECRET_KEY = b'\x81d\xef*\x9aL\xe3\x8c\xd4\xae\x7fm|\xc91\xe1\xb5I\xe7\xb5\xe0\x0e\x1d\xee'  # noqa: E501  pylint: disable=line-too-long
    SESSION_COOKIE_NAME = 'login'
    # File Upload to var/uploads/
    UPLOAD_FOLDER = os.path.join(
        basedir,
        'var', 'uploads'
    )
    APPLICATION_ROOT = '/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # OAuth Stuff
    os.environ['REDIRECT_URI'] = 'http://localhost:5000/login/callback'
    # URIs determined by Google
    os.environ['AUTH_URI'] = 'https://accounts.google.com/o/oauth2/auth'
    os.environ['TOKEN_URI'] = 'https://accounts.google.com/o/oauth2/token'
    os.environ['USER_INFO'] = 'https://www.googleapis.com/userinfo/v2/me'
    os.environ['OAUTH_SCOPE'] = 'profile email'  # Could edit for more scopes


class Development(Config):
    """Specification for development server."""

    # So you can use http for oauth, not just https
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    DEBUG = True
    USE_RELOADER = True
    DATABASE_FILENAME = os.path.join(
        basedir,
        'var', 'placemaster.sqlite3'
    )
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILENAME


class Production(Config):
    """Specification for development server."""

    DEBUG = False
    USE_RELOADER = False
    # postgres implementation
    # note: this db needs to be already created by the specified user
    # https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb
    POSTGRES_USER = secretKeys.POSTGRES_USER
    POSTGRES_PW = secretKeys.POSTGRES_PW
    POSTGRES_URL = secretKeys.POSTGRES_URL
    POSTGRES_DB = secretKeys.POSTGRES_DB
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user=POSTGRES_USER,
        pw=POSTGRES_PW,
        url=POSTGRES_URL,
        db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = DB_URL


config = {
    'development': Development,
    'production': Production,

    'default': Development
}
