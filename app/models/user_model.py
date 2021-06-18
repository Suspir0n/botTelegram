import datetime
import uuid
from ..settings.config import db


class UserModel(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.String(50), primary_key=True, default=str(uuid.uuid4()), unique=True)
    active = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)
    createAt = db.Column(db.DateTime, default=datetime.datetime.now())
    updateAt = db.Column(db.DateTime, default=datetime.datetime.now())
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    chat_id = db.Column(db.Integer, nullable=False)

    def __init__(self, name, phone, chat_id):
        self.name = name
        self.phone = phone
        self.chat_id = chat_id