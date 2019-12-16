"""Abstract model definitions for placemaster app.

To be used with SQLAlchemy and flask-login.
"""
import datetime
from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    """Abstraction of user login for postgres db."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    avatar = db.Column(db.String(200))
    tokens = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
