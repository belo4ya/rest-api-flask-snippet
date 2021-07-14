from functools import wraps
from typing import Optional

from flask_jwt_extended import create_access_token, jwt_required
from werkzeug import security

from app.core import exceptions
from app.extensions import jwt, db
from . import models, schemas


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

    return {'user': schemas.UserClaims().dump(user)}


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

    if not security.check_password_hash(user.password, password):
        raise exceptions.BadCredentials(
            f'Failed to log in, password may be incorrect.'
        )

    return create_access_token(user.username)


def has_access(permissions=None, **jwt_kwargs):
    def requires_access_decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            with_jwt = jwt_required(**jwt_kwargs)(func)
            if permissions:
                print(permissions)

            return with_jwt(*args, **kwargs)

        return decorated

    return requires_access_decorator
