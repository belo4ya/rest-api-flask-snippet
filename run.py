from flask.cli import AppGroup

from app import create_app

app = create_app(config_name='development')
app.app_context().push()

setup_cli = AppGroup('setup')


@setup_cli.command('auth')
def setup_users():
    from app.blueprints.auth import security
    security.init()


app.cli.add_command(setup_cli)

if __name__ == "__main__":
    app.run()
