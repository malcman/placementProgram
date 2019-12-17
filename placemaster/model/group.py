"""Definition of Member SQLAlchemy abstraction model."""
from placemaster.model import db


class Group(db.Model):
    """Representation of support group in model."""

    __tablename__ = 'groups'
    # primary key across table to be used for queries
    id = db.Column(db.Integer, primary_key=True)
    # group number associated with placement
    # (between 1 - numGroups)
    number = db.Column(db.Integer, unique=False)
    members = db.relationship('Member', backref='group')
    # TODO: revisit data type when integrating
    time = db.Column(db.String(20), nullable=False)
    day = db.Column(db.String(15), nullable=False)
    # for universities with multiple campuses
    campus = db.Column(db.String(50), nullable=True)
    room = db.Column(db.String(50))
    # TODO revisit name? grad vs undergrad
    level = db.Column(db.String(15), nullable=False)
    # placement this group belongs to
    placement_id = db.Column(db.Integer, db.ForeignKey('placements.id'))

    def __repr__(self):
        """Define readable representation for debugging."""
        return 'Group: %s' % self.name


__all__ = ['Group']
