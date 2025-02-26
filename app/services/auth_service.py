from app.models.user import User
from app.utils.security import hash_password, check_password
from flask_jwt_extended import create_access_token, create_refresh_token

class AuthService:
    @staticmethod
    def register_user(username, email, password):
        if User.query.filter_by(email=email).first():
            return {"message": "Пользователь уже существует"}, 400
        
        hashed_password = hash_password(password)
        user = User(username=username, password=hashed_password, email=email)
        user.save()
        return {"message": "Пользователь создан"}

    @staticmethod
    def login_user(email, password):
        user = User.query.filter_by(email=email).first()
        if not user or not check_password(user.password, password):
            return {"message": "Неверные учетные данные"}, 401
        
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }