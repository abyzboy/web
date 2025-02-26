import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY')  # Секретный ключ (должен быть сложным!)
    JWT_ACCESS_TOKEN_EXPIRES = 36000 
    JWT_TOKEN_LOCATION = ["headers"]      # Токен ищется в заголовках
    JWT_HEADER_NAME = "Authorization"    # Название заголовка
    JWT_HEADER_TYPE = "Bearer"            # Тип авторизации (Bearer)
    JWT_VERIFY_SUB=False
    APPNAME = "app"
    ROOT = os.path.abspath(APPNAME)
    USER = os.environ.get('POSTGRES_USER')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    HOST = os.environ.get('POSTGRES_HOST')
    PORT = os.environ.get('POSTGRES_PORT')
    DB = os.environ.get('POSTGRES_DB')
    DOMAIN = "http://127.0.0.1:5000"
    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:7777/{DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True