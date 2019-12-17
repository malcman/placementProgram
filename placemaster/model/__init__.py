"""Abstraction module for placemaster model."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from lib.loaders import load_models

# global DB object (imported by models & views & everything else)
db = SQLAlchemy()
# alias for db query function
query = db.session.query


# def init_db():
#     """Return SQLAlchemy instance with dynamic models."""
#     load_models()
#     return db

def init_db(app=None, db=None):
    """Initialize the global database object used by the app."""
    if isinstance(app, Flask) and isinstance(db, SQLAlchemy):
        load_models()
        db.init_app(app)
    else:
        raise ValueError('Cannot init DB without db and app objects.')
