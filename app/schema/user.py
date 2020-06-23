import datetime as dt

from marshmallow import Schema, fields, post_load
from app.model.user import User


class UserSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    email = fields.Str()
    created_at = fields.Date()


class CreateUserSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Str(required=True)

    @post_load
    def make_income(self, data, **kwargs):
        return User(**data)
