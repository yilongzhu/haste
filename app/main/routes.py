from flask import render_template, request, redirect, url_for
from sqlalchemy.sql import collate
from sqlalchemy.sql import func

from app import db
from app.main import bp
from app.models import Item, Request, Content
from flask_login import current_user, login_required


@bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    requests = Request.query.filter_by(accepted_by=None).all()
    quantity_price = []
    for req in requests:
        quantity = Content.query.with_entities(func.sum(Content.quantity).label('total_q')).filter(Content.req_id==req.id)[0].total_q
        price = db.engine.execute("SELECT ROUND(SUM(content.quantity * item.price), 2) as sum FROM content JOIN item ON content.item_id=item.id WHERE req_id=:val", {'val': req.id})
        sum = 0
        for row in price:
            sum = row['sum']
        quantity_price.append({'quantity': quantity, 'sum': sum})
        print(quantity)
        print(sum)


    return render_template('home.html', rqp=zip(requests, quantity_price))


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
                print("Added to dict")

        req = Request(author=current_user)
        db.session.add(req)
        db.session.commit()

        for key in newdict:
            #print(key, newdict[key])
            if (newdict[key] == 'on'):
                temp = key+"-quantity"
                quantity = 1 if temp not in newdict else int(newdict[temp])
                content = Content(cart=req, item_id=int(key), quantity=int(quantity))
                db.session.add(content)
                db.session.commit()

        return redirect(url_for('main.home'))

    items = Item.query.order_by(collate(Item.name, 'NOCASE')).all()
    return render_template('new_order.html', items=items)


@bp.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    #items = Item.query.all()
    return render_template('cart.html', items=items)