from flask_restx import Namespace, Resource, fields
from ...services import lesson_service
from flask_jwt_extended import jwt_required, get_jwt_identity
api = Namespace("Lesson", description="Управление уроками")

# Модель для документации Swagger
lesson_model = api.model("Lesson", {
    "id": fields.Integer(readonly=True),
    "title": fields.String(required=True),
    "course_id": fields.Integer()
})

@api.route("/")
class LessonList(Resource):
    @api.doc("Список уроков")
    @api.marshal_list_with(lesson_model)
    def get(self):
        """Получить все уроки"""
        return lesson_service.get_all_lessons()

    @api.doc("Создать курс")
    @api.expect(lesson_model)
    @api.marshal_with(lesson_model)
    @jwt_required()
    def post(self):
        """Создать новый урок"""
        course_id = api.payload['course_id']
        title = api.payload["title"]
        return lesson_service.create_lesson(course_id, title), 201

@api.route("/<int:lesson_id>")
@api.param("lesson_id", "ID урок")
class LessonDetail(Resource):
    @api.doc("Получить урок по ID")
    @api.marshal_with(lesson_model)
    def get(self, lesson_id):
        """Получить урок по ID"""
        return lesson_service.get_lesson_by_id(lesson_id)

    @api.doc("Удалить урок")
    @api.response(204, "урок удален")
    @jwt_required()
    def delete(self, lesson_id):
        """Удалить урок"""
        return lesson_service.delete_lesson(lesson_id)



