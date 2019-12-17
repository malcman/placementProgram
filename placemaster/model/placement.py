"""Definition of Placement SQLAlchemy abstraction model."""
import datetime
from placemaster.model import db


class Placement(db.Model):
    """Representation of entire placement in model."""

    __tablename__ = 'placements'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    # groups that are a part of this placement
    groups = db.relationship('Group', backref='placement')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        """Define readable representation for debugging."""
        return 'Placement: %s' % self.name


__all__ = ['Placement']
