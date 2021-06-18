from ..settings.config import ma


class MessageSchema(ma.Schema):
    class Meta:
        fields = ('uid', 'active', 'deleted', 'createAt', 'updateAt', 'message', 'chat_id_fk')


message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)