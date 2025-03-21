from flask import Flask
from flask_cors import CORS
from .config import Config
from .api.routes import api

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app)  # Включить CORS для API
    app.config.from_object(config_class)
    # Инициализация расширений
    from app.extensions import db, jwt, bcrypt, cors, ma
    cors.init_app(app)
    db.init_app(app)

    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    with app.app_context():
        db.create_all()
    # Регистрация API
    api.init_app(app)

    return app
