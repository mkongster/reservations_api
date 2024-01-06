import enum
from app.database import db


class UserType(enum.Enum):
    provider = 1
    client = 2


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.Enum(UserType), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'username': self.username}


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer)
    confirmed = db.Column(db.Boolean, default=False, nullable=False)
    slot_datetime = db.Column(db.DateTime, nullable=False)
