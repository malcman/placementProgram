"""Configuration for placemaster development server."""
import os
# file containing keys to connect to google oauth and postgres
import placemaster.secretKeys as secretKeys

APPLICATION_ROOT = '/'
DEBUG = True
USE_RELOADER = True

# postgres
# note: this db needs to be already created by the specified user
# https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb
SQLALCHEMY_TRACK_MODIFICATIONS = False
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

# Secret key for encrypting cookies
SECRET_KEY = b'\x81d\xef*\x9aL\xe3\x8c\xd4\xae\x7fm|\xc91\xe1\xb5I\xe7\xb5\xe0\x0e\x1d\xee'  # noqa: E501  pylint: disable=line-too-long
SESSION_COOKIE_NAME = 'login'

# So you can use http, not just https
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
