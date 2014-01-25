from flask.ext.script import Manager, prompt_bool


manager = Manager()
manager.add_default_commands()

@manager.command
def create_all():
    if prompt_bool(
            "Are you sure you want to create all tables?",
            default=True):
        from ..models import db
        db.create_all()

@manager.command
def drop_all():
    if prompt_bool(
            "Are you sure you want to drop all tables?",
            default=False):
        from ..models import db
        db.drop_all()

@manager.command
def recreate_all():
    if prompt_bool(
            "Are you sure you want to recreate all tables?",
            default=False):
        from ..models import db
        db.drop_all()
        db.create_all()