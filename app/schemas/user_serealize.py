from ..settings.config import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('uid', 'active', 'deleted', 'createAt', 'updateAt', 'name', 'phone', 'chat_id')


user_schema = UserSchema()
users_schema = UserSchema(many=True)