from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api

ma = Marshmallow()

jwt = JWTManager()

db = SQLAlchemy()

migrate = Migrate(db=db, directory='migrations')

api = Api()
