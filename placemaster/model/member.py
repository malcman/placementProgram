"""Definition of Member SQLAlchemy abstraction model."""
from placemaster.model import db


class Member(db.Model):
    """Representation of Member (participant) in model."""

    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    # for universities with multiple campuses
    campus = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(15))
    # freshman, sophomore, grad, etc.
    year = db.Column(db.String(20))
    # foreign key to group they belong to
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))

    def __repr__(self):
        """Define readable representation for debugging."""
        return 'Member. Name: %s. Email: %s' % (self.name, self.email)


__all__ = ['Member']
