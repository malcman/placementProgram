"""Definition of user model to be used for account management."""
import datetime
from flask_login import UserMixin
from placemaster.model import db


class User(db.Model, UserMixin):
    """Abstraction of user model."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    avatar = db.Column(db.String(200))
    tokens = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())


__all__ = ['User']
