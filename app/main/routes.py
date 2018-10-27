from flask import render_template, request
from sqlalchemy import desc

from app import db
from app.main import bp
from app.models import Item
from flask_login import current_user, login_required


@bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html')


@bp.route('/neworder', methods=['GET', 'POST'])
@login_required
def new_order():
    items = Item.query.all()
    return render_template('new_order.html', items=items)


@bp.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    #items = Item.query.all()
    return render_template('cart.html', items=items)