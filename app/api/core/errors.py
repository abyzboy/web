from flask_jwt_extended.exceptions import JWTExtendedException
from flask_restx import Api

api = Api()

@api.errorhandler(JWTExtendedException)
def handle_jwt_error(error):
    return {"message": "Ошибка аутентификации"}, 401