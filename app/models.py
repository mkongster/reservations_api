import enum
from .database import db


class UserType(enum.Enum):
    provider = 1
    client = 2


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.Enum(UserType), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'username': self.username, 'type': self.type.name}


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer)
    confirmed = db.Column(db.Boolean, default=False, nullable=False)
    slot_datetime = db.Column(db.DateTime, nullable=False)
    last_reserved_by = db.Column(db.Integer)
    last_reserved_datetime = db.Column(db.DateTime)

    def to_dict(self):
        return {
            'id': self.id,
            'provider_id': self.provider_id,
            'client_id': self.client_id,
            'confirmed': self.confirmed,
            'slot_datetime': self.slot_datetime,
            'last_reserved_by': self.last_reserved_by, 
            'last_reserved_datetime': self.last_reserved_datetime
        }
