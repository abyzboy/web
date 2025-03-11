from app.models.user import User
from app.schemas.user_schema import UserSchema
from flask import jsonify, make_response
schema = UserSchema()
schemas = UserSchema(many=True)

def get_all_users():
    users =  User.query.all()
    response = make_response(jsonify(schemas.dump(users)))
    response.status_code = 200
    return response

def get_user_by_id(id):
    try:
        user = User.query.get_or_404(id)
        response = make_response(jsonify(schema.dump(user)))
        response.status_code = 200
    except:
        response = make_response(jsonify({"msg" : "Нету такого id"}))
        response.status_code = 404
    return response

def delete_user(id):
    try:
        user : User = User.query.get_or_404(id)
        user.delete()
        response = make_response(jsonify({"msg": "Урок успешно удален"}))
        response.status_code = 200
    except:
        response = make_response(jsonify({"msg": "Урок не был найден"}))
        response.status_code = 404
    return response