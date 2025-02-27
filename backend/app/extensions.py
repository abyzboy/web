from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
cors = CORS()
jwt = JWTManager()
bcrypt = Bcrypt()