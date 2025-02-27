from flask_restx import Namespace, Resource, fields
from flask import jsonify
api = Namespace("Test", description="Тест для проверки работы бэкэнда")

@api.route('/')
class Test(Resource):
    @api.doc("Список пользователей")
    def get(self):
        """Получить ответ от бэка"""
        return jsonify({"message": "Hello from Flask!"})