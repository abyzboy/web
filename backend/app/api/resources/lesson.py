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
    def get(self):
        """Получить все уроки"""
        return lesson_service.get_all_lessons()

    @api.doc("Создать курс")
    @api.expect(lesson_model)
    @jwt_required()
    def post(self):
        """Создать новый урок"""
        course_id = api.payload['course_id']
        title = api.payload["title"]
        return lesson_service.create_lesson(course_id, title)

@api.route("/<int:lesson_id>")
@api.param("lesson_id", "ID урок")
class LessonDetail(Resource):
    @api.doc("Получить урок по ID")
    def get(self, lesson_id):
        """Получить урок по ID"""
        return lesson_service.get_lesson_by_id(lesson_id)

    @api.doc("Удалить урок")
    @jwt_required()
    def delete(self, lesson_id):
        """Удалить урок"""
        return lesson_service.delete_lesson(lesson_id)



