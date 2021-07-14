from flask.cli import AppGroup

from app.blueprints.auth import security

setup_cli = AppGroup('setup')


@setup_cli.command('auth')
def setup_auth():
    security.init()
