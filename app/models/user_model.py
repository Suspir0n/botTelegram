import datetime
import uuid
from ..settings.config import db


class UserModel(db.Model):
    __tablename__ = 'user'
    active = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)
    createAt = db.Column(db.DateTime, default=datetime.datetime.now())
    updateAt = db.Column(db.DateTime, default=datetime.datetime.now())
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    chat_id = db.Column(db.Integer, primary_key=True, unique=True)

    def __init__(self, name, phone, chat_id):
        self.name = name
        self.phone = phone
        self.chat_id = chat_id