from flask import Flask
from flask_cors import CORS
from .config import Config
from .api.routes import api
from .models.all_models import *

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Инициализация расширений
    from app.extensions import db, jwt, bcrypt
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    CORS(app)  # Включить CORS для API
    with app.app_context():
        db.create_all()
    # Регистрация API
    api.init_app(app)

    return app