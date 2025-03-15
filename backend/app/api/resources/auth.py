from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app.services.auth_service import AuthService
from flask import request

api = Namespace("auth", description="Аутентификация и регистрация")

# Модель для Swagger
login_model = api.model("Login", {
    "email": fields.String(required=True),
    "password": fields.String(required=True),
})

register_model = api.model("Login", {
    "email": fields.String(required=True),
    "password": fields.String(required=True),
    "username": fields.String(required=True)
})


@api.route("/refresh")
class Refresh(Resource):
    @api.doc(description="Обновить access-токен с помощью refresh-токена")
    @jwt_required(refresh=True)  # Требуется refresh-токен (не access!)
    def post(self):
        """Обновить access-токен"""
        current_user_id = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user_id)
        return {"access_token": new_access_token}, 200

@api.route("/register", methods=['POST', 'GET'])
class Register(Resource):
    @api.expect(register_model)
    def post(self):
        """Регистрация пользователя"""
        d = request.get_json()
        print(d)
        email = d["email"]
        username = d["username"]
        password = d["password"]
        return AuthService.register_user(username, email, password), 201

@api.route("/login", methods=['POST', 'GET'])
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Логин пользователя"""
        email = api.payload["email"]
        password = api.payload["password"]
        return AuthService.login_user(email, password), 200