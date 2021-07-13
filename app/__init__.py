import flask

from . import config, extensions
from .blueprints import auth_bp, api_bp


def create_app(config_name: str = 'default') -> flask.Flask:
    app = flask.Flask(__name__)

    register_config(app, config_name)

    register_extensions(app)

    register_blueprints(app)

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
