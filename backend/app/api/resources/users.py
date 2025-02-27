from flask_restx import Namespace, Resource, fields
from ...services import user_service
from flask_jwt_extended import jwt_required


api = Namespace("USERS", description="Операции с пользователями")

user_model = api.model('USER', 
    {"id": fields.Integer(readonly=True),
    "email": fields.String(required=True),
    "username": fields.String(required=True),
    "password": fields.String(required=True),
    "is_verified": fields.Boolean(),
    "role" : fields.String(default='user'),})

@api.route("/")
class UserList(Resource):
    @api.doc("Список пользователей")
    @api.marshal_list_with(user_model)
    def get(self):
        """Получить всех пользователей"""
        return user_service.get_all_users()

@api.route("/<int:user_id>")
@api.param("user_id", "ID user")
class UserDetail(Resource):
    @api.doc("Получить пользователя ID")
    @api.marshal_with(user_model)
    def get(self, user_id):
        """Получить user по ID"""
        return user_service.get_user_by_id(user_id)

    @api.doc("Удалить user")
    @api.response(204, "user удален")
    @jwt_required()
    def delete(self, user_id):
        """Удалить user"""
        user_service.delete_course(user_id)
        return "", 204