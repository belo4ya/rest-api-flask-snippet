from marshmallow import fields

from app.extensions import ma


class Credentials(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)


class AccessToken(ma.Schema):
    access_token = fields.String(required=True)
