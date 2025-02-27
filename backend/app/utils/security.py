from ..extensions import bcrypt

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password(hashed_password, password):
    return bcrypt.check_password_hash(hashed_password, password)


from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask_restx import abort
from app.models.user import User

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        if user.role != "admin":
            abort(403, message="Доступ запрещен")
        return fn(*args, **kwargs)
    return wrapper
