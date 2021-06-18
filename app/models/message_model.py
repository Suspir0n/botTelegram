import datetime
import uuid
from ..settings.config import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref


class MessageModel(db.Model):
    __tablename__ = 'message'
    uid = db.Column(db.String(50), primary_key=True, default=str(uuid.uuid4()), unique=True)
    active = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)
    createAt = db.Column(db.DateTime, default=datetime.datetime.now())
    updateAt = db.Column(db.DateTime, default=datetime.datetime.now())
    message = db.Column(db.String(500), nullable=False)
    chat_id_fk = db.Column(db.Integer, ForeignKey('user.chat_id'))
    chat_id = db.relationship('UserModel', backref=backref('message', uselist=False))

    def __init__(self, message, chat_id_fk):
        self.message = message
        self.chat_id_fk = chat_id_fk