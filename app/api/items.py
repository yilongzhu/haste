from flask import jsonify

from app import db
from app.api import bp
from app.models import Item
from app.schemas import item_schema, items_schema


@bp.route('/item/<int:id>', methods=['GET'])
def get_item(id):
    item = Imte.query.get_or_404(id)
    return jsonify(item_schema.dump(item).data)


@bp.route('/items/', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify(items_schema.dump(items).data)