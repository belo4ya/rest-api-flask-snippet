from functools import wraps
from typing import Optional

from flask_jwt_extended import create_access_token, jwt_required, current_user
from werkzeug.security import check_password_hash

from app.core import exceptions
from app.extensions import jwt, db
from . import models, schemas
from .security import ROLES, PERMISSIONS, ROLES_PERMISSIONS


@jwt.user_identity_loader
def user_identity_lookup(identity):
    return identity


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return models.User.get_by_username(identity)


@jwt.additional_claims_loader
def add_claims_to_access_token(identity):
    user = models.User.get_by_username(identity)
    if user is None:
        return {'user': None}

    return {'user': schemas.UserClaimsSchema().dump(user)}


def sign_up(username, password) -> Optional[str]:
    if models.User.get_by_username(username):
        raise exceptions.BadCredentials(
            f"The user '{username}' already exists."
        )

    models.User.create(
        username=username,
        password=password
    )
    db.session.commit()

    return create_access_token(username)


def sign_in(username, password) -> Optional[str]:
    user = models.User.get_by_username(username)
    if user is None:
        raise exceptions.BadCredentials(
            f"The user '{username}' not found."
        )

    if not check_password_hash(user.password, password):
        raise exceptions.BadCredentials(
            f'Failed to log in, password may be incorrect.'
        )

    return create_access_token(user.username)


def has_access(
        permissions: Optional[list[PERMISSIONS]] = None,
        roles: Optional[list[ROLES]] = None,
        **jwt_kwargs
):
    def requires_access_decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            func_out = jwt_required(**jwt_kwargs)(func)(*args, **kwargs)  # применение декоратора jwt_required

            if _has_permissions(permissions, roles):
                return func_out

            raise exceptions.AccessDenied(
                "You don't have the permission to access the requested resource."
                " It is either read-protected or not readable by the server."
            )

        return decorated

    return requires_access_decorator


def _has_permissions(
        permissions: Optional[list[PERMISSIONS]] = None,
        roles: Optional[list[ROLES]] = None,
) -> bool:
    if not permissions and not roles:
        return False

    expected_permissions = _get_expected_permissions(permissions, roles)
    existing_permissions = _get_existing_permissions(current_user)
    return expected_permissions & existing_permissions == expected_permissions


def _get_expected_permissions(
        permissions: Optional[list[PERMISSIONS]] = None,
        roles: Optional[list[ROLES]] = None
) -> set[PERMISSIONS]:
    expected_permissions = set()
    if permissions:
        expected_permissions.update(permissions)
    if roles:
        for role in roles:
            expected_permissions.update(ROLES_PERMISSIONS[role])

    return expected_permissions


def _get_existing_permissions(user: models.User) -> set[PERMISSIONS]:
    existing_permissions = set()
    for role in user.roles:
        existing_permissions.update([permission.name for permission in role.permissions])

    return existing_permissions
