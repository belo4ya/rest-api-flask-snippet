import enum

from werkzeug import security

from app.core.database import Model
from app.extensions import db


class _Role(enum.Enum):
    USER = enum.auto()
    ADMIN = enum.auto()


class Role(Model):
    __tablename__ = 'roles'

    enum = _Role
    name = db.Column(db.Enum(enum), unique=True, nullable=False)

    def __repr__(self):
        return str(self.name)

    @classmethod
    def init(cls):
        for role in cls.enum.__members__.values():
            cls.create(name=role)


class User(Model):
    __tablename__ = 'users'

    username = db.Column(db.String(255), index=True, unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Integer, db.ForeignKey('roles.id'), default=Role.enum.USER)

    @classmethod
    def get_by_username(cls, username: str):
        return cls.where(username=username).first()

    @classmethod
    def create(cls, **kwargs):
        if 'password' in kwargs:
            kwargs['password'] = security.generate_password_hash(kwargs['password'])

        return super(User, cls).create(**kwargs)
