from app import create_app, db
from app.models import User, Requests

application = create_app()

@application.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Requests': Requests}