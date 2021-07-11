import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))


class _BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(_BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class TestingConfig(_BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ''


class ProductionConfig(_BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ''


CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
