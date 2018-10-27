from app import ma
from app.models import User
from marshmallow import fields


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


user_schema = UserSchema()
users_schema = UserSchema(many=True)