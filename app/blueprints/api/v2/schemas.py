from app.core.schema import ma, ServiceFieldsMixin
from . import models


class RaccoonSchema(ma.SQLAlchemyAutoSchema, ServiceFieldsMixin):
    class Meta:
        model = models.Raccoon
