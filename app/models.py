from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(10), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    school = db.Column(db.String(128), index=True)
    requests = db.relationships('Request', backref='author', lazy='dynamic')
    completed_requests = db.relationship('Request', backref='shopper', lazy='dynamic')
     

    def __repr__(self):
        return '<User {}>'.format(self.username) 

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_of_order = db.Column(db.DateTime, default=datetime.utcnow)
    placed = db.Column(db.Boolean, default=false)
    placed_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    fulfilled_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    contents = db.relationship('Content', backref='cart', lazy='dynamic')


class Content(db.Model):
    req_id = db.Column(db.Integer, db.ForeignKey('request.id'))
    item_id = db.relationship('Item', backref = 'order', lazy='dynamic')
    quantity = db.Column(db.Integer, default = 1)


class Item(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('content.id'), index=True, unique=True)
    name = db.Column(db.String(128), unique=True)
    price = db.Column(db.Float)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))