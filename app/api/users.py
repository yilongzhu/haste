from flask import jsonify

from app import db
from app.api import bp
from app.models import User
from app.schemas import user_schema


@bp.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user_schema.dump(user).data)


@bp.route('/user/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(user_schema.dump(users).data)