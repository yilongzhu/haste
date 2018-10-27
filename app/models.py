from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(10), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(48))
    last_name = db.Column(db.String(48))
    school = db.Column(db.String(128), index=True)
    orders = db.relationship('Order', foreign_keys='[Order.placed_by]', backref='author', lazy='dynamic')
    completed_orders = db.relationship('Order', foreign_keys='[Order.accepted_by]', backref='shopper', lazy='dynamic')
    balance = db.Column(db.Float, default=0)
     

    def __repr__(self):
        return '<User {}>'.format(self.email) 

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_of_order = db.Column(db.DateTime, default=datetime.utcnow)
    placed_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    accepted_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    completed = db.Column(db.Boolean, default=False)
    contents = db.relationship('Content', backref='cart', lazy='dynamic')


class Content(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    quantity = db.Column(db.Integer, default=1)


class Item(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True)
    price = db.Column(db.Float)
    in_content = db.relationship('Content', backref='item', lazy='dynamic')


@login.user_loader
def load_user(id):
    return User.query.get(int(id))