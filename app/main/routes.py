from flask import render_template, request
from sqlalchemy import desc
from app.main import bp
from flask_login import current_user, login_required


@bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html')