from flask import render_template, request
from sqlalchemy import desc
from app.main import bp
from app.models import Share


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    requests = Request.query.order_by(desc(Share.timestamp)).all()
    return render_template('index.html', user_id=user_id, requests=requests)