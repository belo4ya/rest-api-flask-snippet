from app.extensions import ma
from flask_smorest import fields


class MultipartFile(ma.Schema):
    file = fields.Upload(ma)
