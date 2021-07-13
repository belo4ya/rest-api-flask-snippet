import enum
from app.blueprints.auth import models


class Role(enum.Enum):
    USER = enum.auto()
    ADMIN = enum.auto()


def init():
    init_permissions()
    init_roles()
    init_users()


def init_permissions():
    pass


def init_roles():
    for role in Role.__members__.values():
        models.Role.create(name=role)


def init_users():
    pass
