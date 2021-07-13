import enum
from app.blueprints.auth import models
from app.extensions import db


class PERMISSIONS(enum.Enum):
    CAN_READ = enum.auto()
    CAN_CREATE = enum.auto()
    CAN_EDIT = enum.auto()
    CAN_DELETE = enum.auto()


class ROLES(enum.Enum):
    VIEWER = enum.auto()
    USER = enum.auto()
    ADMIN = enum.auto()


VIEWER_PERMISSIONS = {
    PERMISSIONS.CAN_READ
}


USER_PERMISSIONS = {
    *VIEWER_PERMISSIONS,
    PERMISSIONS.CAN_CREATE,
    PERMISSIONS.CAN_EDIT
}


ADMIN_PERMISSIONS = {
    *USER_PERMISSIONS,
    PERMISSIONS.CAN_DELETE
}


ROLES_PERMISSIONS = {
    ROLES.VIEWER: VIEWER_PERMISSIONS,
    ROLES.USER: USER_PERMISSIONS,
    ROLES.ADMIN: ADMIN_PERMISSIONS,
}


def init():
    init_permissions()
    init_roles()
    init_users()
    db.session.commit()


def init_permissions():
    for permission in PERMISSIONS.__members__.values():
        models.Permission.create(name=permission)


def init_roles():
    for role in ROLES.__members__.values():
        models.Role.create(name=role, permissions=ROLES_PERMISSIONS[role])


def init_users():
    user = {
        'username': 'admin',
        'password': 'admin',
        'roles': models.Role.where(name__in=['admin']).all(),
    }
    models.User.create(**user)
