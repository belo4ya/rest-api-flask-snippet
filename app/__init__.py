import flask

from . import config, extensions, cli
from .blueprints import auth_bp, api_bp


def create_app(config_name: str = 'default') -> flask.Flask:
    app = flask.Flask(__name__)

    register_config(app, config_name)

    register_extensions(app)

    register_blueprints(app)

    register_cli_commands(app)

    register_blueprints_views_in_doc(app)

    return app


def register_config(app: flask.Flask, config_name: str) -> None:
    app.config.from_object(config.CONFIG[config_name])


def register_extensions(app: flask.Flask) -> None:
    extensions.ma.init_app(app)
    extensions.jwt.init_app(app)
    extensions.db.init_app(app)
    extensions.migrate.init_app(app)
    extensions.api.init_app(app)


def register_blueprints(app: flask.Flask) -> None:
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)


def register_cli_commands(app: flask.Flask) -> None:
    app.cli.add_command(cli.setup_group)


def register_blueprints_views_in_doc(app: flask.Flask) -> None:
    pass
    # bp = api_bp._blueprints[1][0]
    # print(bp._blueprints[0][0].url_default_functions)
    # bp.register_views_in_doc(extensions.api, app, extensions.api.spec)
    # extensions.api.spec.tag({'name': bp.name, 'description': bp.description})
