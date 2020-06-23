from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime as dt
from app import db


class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True,
                   default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(200))
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=dt.datetime.now)

    def __repr__(self):
        return '<User %r>' % self.name
