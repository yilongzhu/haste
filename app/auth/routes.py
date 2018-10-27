from flask import render_template, flash, redirect, url_for, request

from app import db
from app.models import User
from app.auth.forms import LoginForm, RegistrationForm
from app.auth import bp

from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(phone=form.phone.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid phone number or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)

    return render_template('auth/login.html', title='Login', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()

    print("Entered route again")
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print("Entered if statement")
        user = User(phone=form.phone.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now registered!')
        return redirect(url_for('auth.login'))
    print("After if statement")

    return render_template('auth/register.html', title='Register', form=form)