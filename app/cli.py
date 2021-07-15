from flask.cli import AppGroup

from app.blueprints.auth import security

setup_group = AppGroup('setup')


@setup_group.command('auth')
def setup_auth():
    security.init()
