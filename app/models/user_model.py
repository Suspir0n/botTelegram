import datetime
import uuid
from ..settings.config import db


class UserModel(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()), unique=True)
    active = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)
    createAt = db.Column(db.DateTime, default=datetime.datetime.now())
    updateAt = db.Column(db.DateTime, default=datetime.datetime.now())
    name = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    message = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name, phone, message):
        self.name = name
        self.phone = phone
        self.message = message