from marshmallow import fields

from app.core.schema import ma, ServiceFieldsMixin
from . import models


class RaccoonSchema(ma.SQLAlchemyAutoSchema, ServiceFieldsMixin):
    class Meta:
        model = models.Raccoon


class MeowSchema(ma.Schema):
    meow = fields.String(required=True)
