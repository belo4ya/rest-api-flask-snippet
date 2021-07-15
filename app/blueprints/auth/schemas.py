from marshmallow import fields

from app.extensions import ma


class CredentialsSchema(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)


class AccessTokenSchema(ma.Schema):
    access_token = fields.String(required=True)


class UserClaimsSchema(ma.Schema):
    id = fields.Integer()
    username = fields.String()
    roles = fields.Function(lambda obj: [role.name.name for role in obj.roles] if obj else [])
