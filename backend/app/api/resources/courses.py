from flask_restx import Namespace, Resource, fields
from ...services import course_service
from flask_jwt_extended import jwt_required, get_jwt_identity
api = Namespace("courses", description="Управление курсами")

# Модель для документации Swagger
course_model = api.model("Course", {
    "id": fields.Integer(readonly=True),
    "title": fields.String(required=True),
    "description": fields.String(required=True),
    "author_id": fields.Integer(readonly=True)
})

@api.route("/")
class CourseList(Resource):
    @api.doc("Список курсов")
    def get(self):
        """Получить все курсы"""
        return course_service.get_all_courses()

    @api.doc("Создать курс")
    @api.expect(course_model)
    @jwt_required()
    def post(self):
        """Создать новый курс"""
        id = get_jwt_identity()
        title = api.payload["title"]
        description = api.payload["description"]
        return course_service.create_course(title, description, id)

@api.route("/<int:course_id>")
@api.param("course_id", "ID курса")
class CourseDetail(Resource):
    @api.doc("Получить курс по ID")
    def get(self, course_id):
        """Получить курс по ID"""
        return course_service.get_course_by_id(course_id)

    @api.doc("Удалить курс")
    @jwt_required()
    def delete(self, course_id):
        """Удалить курс"""
        return course_service.delete_course(course_id)