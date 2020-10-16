from flask import Flask
from app import db
from app import create_app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Command, prompt_bool



app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@MigrateCommand.command
def create():
    """Create Application Database if don't exists"""
    db.create_all()
    from alembic.config import Config
    from alembic import command
    alembic_cfg = Config("migrations/alembic.ini")
    alembic_cfg.set_main_option("script_location", "migrations")
    command.stamp(alembic_cfg, "head")

@MigrateCommand.command
def destroy():
    """Destroy Application database"""
    if prompt_bool(
        "Are you sure you want to destroy all your data"
        ):
        db.drop_all()
        

if __name__ == '__main__':
    manager.run()