from flask import render_template, request
from sqlalchemy.sql import collate
from sqlalchemy.sql import func

from app import db
from app.main import bp
from app.models import Item, Request, Content
from flask_login import current_user, login_required


@bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    requests = Request.query.all()
    return render_template('home.html', requests=requests)


@bp.route('/neworder', methods=['GET', 'POST'])
@login_required
def new_order():
    items = Item.query.order_by(collate(Item.name, 'NOCASE')).all()
    return render_template('new_order.html', items=items)


@bp.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    #items = Item.query.all()
    return render_template('cart.html', items=items)