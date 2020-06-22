import datetime as dt

from marshmallow import Schema, fields, post_load


class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<Transaction(name={self.description!r})>'.format(self=self)


class UserSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Str()
    created_at = fields.Date()

    @post_load
    def make_income(self, data, **kwargs):
        return User(**data)
