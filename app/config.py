import datetime
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

SPEC_UI = {
    'OPENAPI_URL_PREFIX': '/doc',
    'OPENAPI_REDOC_PATH': '/redoc',
    'OPENAPI_REDOC_URL': 'https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js',
    'OPENAPI_SWAGGER_UI_PATH': '/swagger-ui',
    'OPENAPI_SWAGGER_UI_URL': 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/',
    'OPENAPI_RAPIDOC_PATH': '/rapidoc',
    'OPENAPI_RAPIDOC_URL': 'https://unpkg.com/rapidoc/dist/rapidoc-min.js',
}


class _BaseConfig:
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'super secret-secret YEK')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super secret-secret YEK')
    JWT_ACCESS_TOKEN_EXPIRES = os.getenv('JWT_ACCESS_TOKEN_EXPIRES', datetime.timedelta(hours=12))

    API_TITLE = 'My API'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.3'

    @classmethod
    def setup_ui_specs(cls):
        for k, v in SPEC_UI.items():
            setattr(cls, k, v)


_BaseConfig.setup_ui_specs()


class DevelopmentConfig(_BaseConfig):
    DEBUG = True
    FLASK_ENV = 'development'

    SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOPMENT_DATABASE')


class TestingConfig(_BaseConfig):
    DEBUG = True
    FLASK_ENV = 'development'
    TESTING = True

    SQLALCHEMY_DATABASE_URI = os.getenv('TESTING_DATABASE')


class ProductionConfig(_BaseConfig):
    DEBUG = False
    FLASK_ENV = 'production'

    SQLALCHEMY_DATABASE_URI = os.getenv('PRODUCTION_DATABASE')


CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
