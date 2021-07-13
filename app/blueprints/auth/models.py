from werkzeug import security

from app.core.database import Model
from app.extensions import db
from app.blueprints.auth import security


class Permission(Model):
    __tablename__ = 'permissions'
    __repr_attrs__ = ['name']

    name = db.Column(db.String(255), unique=True, nullable=False)


assoc_permission_role = db.Table(
    'permissions_roles',
    Model.metadata,
    db.Column('permission_id', db.Integer, db.ForeignKey('permissions.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id')),
    db.UniqueConstraint('permission_id', 'role_id')
)


class Role(Model):
    __tablename__ = 'roles'
    __repr_attrs__ = ['name']

    name = db.Column(db.Enum(security.Role), unique=True, nullable=False)

    permissions = db.relationship(
        'Permission', secondary=assoc_permission_role, backref='role'
    )


assoc_user_role = db.Table(
    'users_roles',
    Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id')),
    db.UniqueConstraint('user_id', 'role_id')
)


class User(Model):
    __tablename__ = 'users'
    __repr_attrs__ = ['username']

    username = db.Column(db.String(255), index=True, unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    roles = db.relationship('Role', secondary=assoc_user_role, backref='user')

    @classmethod
    def get_by_username(cls, username: str):
        return cls.where(username=username).first()

    @classmethod
    def create(cls, **kwargs):
        if 'password' in kwargs:
            kwargs['password'] = security.generate_password_hash(kwargs['password'])

        return super(User, cls).create(**kwargs)
