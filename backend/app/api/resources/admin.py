from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from ...utils.security import admin_required
from app.services.auth_service import AuthService

api = Namespace("admin", description="Админка")

@api.route("/admin")
class AdminResource(Resource):
    @admin_required
    @jwt_required()
    def get(self):
        return {"message": "Только для админов"}