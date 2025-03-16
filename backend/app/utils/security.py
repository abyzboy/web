from ..extensions import bcrypt

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password(hashed_password, password):
    return bcrypt.check_password_hash(hashed_password, password)


from functools import wraps
from flask_jwt_extended import get_jwt
from flask import make_response, jsonify

def check_access(role : str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_data_jwt = get_jwt()
            if user_data_jwt["role"] == role:
                return func(*args, **kwargs)
            else:
                response = make_response(jsonify({"message" : "Доступ запрещён"}))
                response.status = 403
                return response
        return wrapper
    return decorator