from flask_restx import Namespace, Resource, fields
from ...services import video_service
from flask_jwt_extended import jwt_required, get_jwt_identity
api = Namespace("Vide", description="Управление videos")



video_model = api.model("Video", {"id": fields.Integer(readonly=True),
    "lesson_id": fields.Integer(),
    "path": fields.String(required=True)})

@api.route("/")
class VideoList(Resource):
    @api.doc("Список уроков")
    def get(self):
        """Получить все уроки"""
        return video_service.get_all_videos()

    @api.doc("Создать новый урок")
    @api.expect(video_model)
    @jwt_required()
    def post(self):
        """Создать новый урок"""
        course_id = api.payload['lesson_id']
        path = api.payload["path"]
        return video_service.create_video(path, course_id)