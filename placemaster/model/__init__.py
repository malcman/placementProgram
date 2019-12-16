"""Abstraction module for placemaster model."""
from flask_sqlalchemy import SQLAlchemy
from lib.loaders import load_models

# global DB object (imported by models & views & everything else)
db = SQLAlchemy()
# alias for db query function
query = db.session.query


def init_db():
    """Return SQLAlchemy instance with dynamic models."""
    load_models()
    return db
