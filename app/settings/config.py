from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import random
import string

db = SQLAlchemy()
ma = Marshmallow()

random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(random_str) for i in range(12))


def secret_key(app):
    app.config['SECRET_KEY'] = key


def config_db(app):
    from ..models import user_model, message_model
    db.init_app(app)
    app.app_context().push()
    db.create_all(app=app)
    app.db = db


def config_ma(app):
    ma.init_app(app)


def config_bp(app):
    from ..routes import user_routes, message_routes
    app.register_blueprint(user_routes.bp_users)
    app.register_blueprint(message_routes.bp_messages)