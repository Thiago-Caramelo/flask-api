import datetime as dt

from marshmallow import Schema, fields, post_load
from app.model.user import User


class UserSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    created_at = fields.Date(required=False)

    @post_load
    def make_income(self, data, **kwargs):
        return User(**data)
