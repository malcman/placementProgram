"""Manager script for placemaster app."""
import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from placemaster import create_app
from placemaster.model import db
from placemaster.model.user import User
from placemaster.model.group import Group
from placemaster.model.member import Member
from placemaster.model.placement import Placement

models = {
    'User': User,
    'Group': Group,
    'Member': Member,
    'Placement': Placement
}

# app = create_app(os.getenv('PLACEMASTER_SETTINGS') or 'default')
app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    """Create app context to use in terminal shell."""
    return dict(app=app, db=db, **models)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
