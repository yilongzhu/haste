from flask import render_template, flash, redirect, url_for, request

from app import db
from app.models import User
from app.auth.forms import LoginForm, RegistrationForm
from app.auth import bp

from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    login_form = LoginForm()
    registration_form = RegistrationForm()

    if registration_form.submit1.data and registration_form.validate_on_submit():
        user = User(phone=registration_form.phone.data, email=registration_form.email.data, school=registration_form.school.data)
        user.set_password(registration_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Please login to continue.')
        return redirect(url_for('auth.index'))
    if login_form.submit2.data and login_form.validate_on_submit():
        user = User.query.filter((User.phone==login_form.username.data) | (User.email==login_form.username.data)).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid phone number or password')
            return redirect(url_for('auth.index'))
        login_user(user, remember=login_form.remember_me.data)
        return redirect(url_for('main.home'))

    return render_template('index.html', login_form=login_form, registration_form=registration_form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.index'))