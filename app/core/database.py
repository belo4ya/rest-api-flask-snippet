from datetime import datetime

from flask_jwt_extended import current_user, verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError
from sqlalchemy_mixins import AllFeaturesMixin

from app.extensions import db


def get_current_user_id():
    try:
        verify_jwt_in_request()
        id_ = current_user.id
        return id_
    except (RuntimeError, NoAuthorizationError):
        return None


class Model(db.Model, AllFeaturesMixin):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @db.declared_attr
    def created_by(self):
        return db.Column(
            db.BigInteger,
            db.ForeignKey('users.id'),
            default=get_current_user_id,
            nullable=True
        )

    @db.declared_attr
    def updated_by(self):
        return db.Column(
            db.BigInteger,
            db.ForeignKey('users.id'),
            default=get_current_user_id,
            onupdate=get_current_user_id,
            nullable=True
        )


Model.set_session(db.session)
