from app import ma
from app.models import User, Item
from marshmallow import fields


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class ItemSchema(ma.ModelSchema):
    class Meta:
        model = Item

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)