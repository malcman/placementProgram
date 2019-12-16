"""Configuration for placemaster development server."""
import os
# file containing keys to connect to google oauth and postgres
# from . import secretKeys

APPLICATION_ROOT = '/'
DEBUG = True
USE_RELOADER = True


# sqlite implementation
# Database file is var/placemaster.sqlite3
DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'placemaster.sqlite3'
)
# os.environ['CLIENT_ID'] = (secretKeys.GOOGLE_CLIENT_ID)  # Keep the parentheses
# os.environ['CLIENT_SECRET'] = secretKeys.GOOGLE_CLIENT_SECRET
os.environ['REDIRECT_URI'] = 'http://localhost:5000/login/callback'
# URIs determined by Google
os.environ['AUTH_URI'] = 'https://accounts.google.com/o/oauth2/auth'
os.environ['TOKEN_URI'] = 'https://accounts.google.com/o/oauth2/token'
os.environ['USER_INFO'] = 'https://www.googleapis.com/userinfo/v2/me'
os.environ['OAUTH_SCOPE'] = 'profile email'  # Could edit for more available scopes


# File Upload to var/uploads/
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'uploads'
)

# Secret key for encrypting cookies
SECRET_KEY = b'\x81d\xef*\x9aL\xe3\x8c\xd4\xae\x7fm|\xc91\xe1\xb5I\xe7\xb5\xe0\x0e\x1d\xee'  # noqa: E501  pylint: disable=line-too-long
SESSION_COOKIE_NAME = 'login'

# So you can use http for oauth, not just https
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
