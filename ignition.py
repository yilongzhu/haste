from app import create_app, db
from app.models import User, Item, Order, Content

application = create_app()

@application.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Item': Item, 'Order': Order, 'Content': Content}