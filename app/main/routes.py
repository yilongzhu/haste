from flask import render_template, request, redirect, url_for, flash
from sqlalchemy.sql import collate
from sqlalchemy.sql import func, desc

from app import db
from app.main import bp
from app.models import User, Item, Order, Content
from flask_login import current_user, login_required


def get_total_price(order):
    price = db.engine.execute("SELECT ROUND(SUM(content.quantity * item.price), 2) as sum FROM content JOIN item ON content.item_id=item.id WHERE order_id=:val", {'val': order.id})
    sum = 0
    for row in price:
        sum = row['sum']
    return sum

def get_payout(total):
    return total*.0335 + 1.5


@bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    orders = Order.query.filter(Order.accepted_by==None).order_by(desc(Order.time_of_order)).all()
    quantity_price = []
    for order in orders:
        quantity = Content.query.with_entities(func.sum(Content.quantity).label('total_q')).filter(Content.order_id==order.id)[0].total_q
        sum = get_total_price(order)
        quantity_price.append({'quantity': quantity, 'sum': sum})
        #print(quantity)
        #print(sum)


    return render_template('home.html', rqp=zip(orders, quantity_price))


@bp.route('/neworder', methods=['GET', 'POST'])
@login_required
def new_order():
    newdict = {}
    if request.method == 'POST':
        data = request.form.to_dict()
        #print(data)
        for key in data:
            if data[key] != '':
                newdict[key] = data[key]
                #print("Added to dict")
        if (not newdict):
            flash('Your order is empty.', 'info')
            return redirect(url_for('main.new_order')) 

        order = Order(author=current_user)
        db.session.add(order)
        db.session.commit()

        for key in newdict:
            #print(key, newdict[key])
            if (newdict[key] == 'on'):
                temp = key+"-quantity"
                quantity = 1 if temp not in newdict else int(newdict[temp])
                content = Content(cart=order, item_id=int(key), quantity=int(quantity))
                db.session.add(content)
                db.session.commit()

        return redirect(url_for('main.home'))

    items = Item.query.order_by(collate(Item.name, 'NOCASE')).all()
    return render_template('new_order.html', items=items)


@bp.route('/order/<int:id>', methods=['GET', 'POST'])
@login_required
def order(id):
    if request.method == 'POST':
        order_id = request.form['order_id']
        print(order_id)
        order = Order.query.filter_by(id=order_id).first()
        order.shopper = current_user
        db.session.commit()
        flash("Order accepted!", 'success')
        return redirect(url_for('main.home'))

    order = Order.query.filter_by(id=id).first_or_404()
    items = db.engine.execute("SELECT item.name, item.price, quantity FROM content JOIN item ON content.item_id=item.id WHERE content.order_id=:val", {'val': order.id})
    user = User.query.filter_by(id=order.placed_by).first()
    sum = get_total_price(order)
    payout = get_payout(sum)
    return render_template('order.html', order=order, payout=payout, user=user, items = items, sum=sum)


@bp.route('/order/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_order(id):
    print(id)
    order = Order.query.filter_by(id=id).first()
    db.session.delete(order)
    db.session.commit()
    flash("Order deleted.", 'info')
    return redirect(url_for('main.home')) 


@bp.route('/accepted_orders')
@login_required
def accepted_orders():
    orders = Order.query.filter((Order.shopper==current_user) & (Order.completed==False)).order_by(desc(Order.time_of_order)).all()
    quantity_price = []
    for order in orders:
        quantity = Content.query.with_entities(func.sum(Content.quantity).label('total_q')).filter(Content.order_id==order.id)[0].total_q
        sum = get_total_price(order)
        payout = get_payout(sum)
        quantity_price.append({'quantity': quantity, 'sum': sum, 'payout': payout})
    return render_template('accepted_orders.html', rqp=zip(orders, quantity_price))


@bp.route('/order/<int:id>/complete', methods=['GET', 'POST'])
@login_required
def complete_order(id):
    order = Order.query.filter_by(id=id).first()
    payout = get_payout(get_total_price(order))
    order.completed = True
    new_balance = current_user.balance + payout
    current_user.balance = new_balance
    db.session.commit()

    flash("New balance: ${:0.2f}.".format(new_balance), 'info')
    return redirect(url_for('main.accepted_orders'))