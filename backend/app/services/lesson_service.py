from app.models.lesson import Lesson
from app.models.video import Video
from app.models.course import Course
from app.schemas.video_schema import VideoSchema
from ..schemas.lesson_schema import LessonSchema
from ..extensions import db
from flask import jsonify, make_response

schema = LessonSchema()
schemas = LessonSchema(many=True)
schemas_videos = VideoSchema(many=True)


def get_all_lessons() -> list[Lesson]:
    response = make_response(jsonify(schemas.dump(Lesson.query.all())))
    response.status = 200
    return response

def get_lesson_by_id(id: int) -> Lesson: 
    try:
        lesson = Lesson.query.get_or_404(id)
        response = make_response(jsonify(schema.dump(lesson)))
        response.status_code = 200
    except :
        response = make_response(jsonify({"msg" : "Нету такого id"}))
        response.status_code = 404
    return response

def delete_lesson(id : int) -> None:
    try:
        lesson : Lesson = Lesson.query.get_or_404(id)
        lesson.delete()
        response = make_response(jsonify({"msg": "Урок успешно удален"}))
        response.status_code = 200
    except Exception as e:
        response = make_response(jsonify({"msg": "Урок не был найден"}))
        response.status_code = 404
    return response

def create_lesson(course_id :int, title : str) -> str:
    try:
        course : Course = Course.query.get_or_404(course_id)
    except:
        response = make_response(jsonify({"msg": "Курс не был найден"}))
        response.status_code = 404
        return response
    try:
        lesson : Lesson = Lesson(course_id=course_id, title=title)
        lesson.create()
        response = make_response(jsonify({"msg": "Урок был создан"}))
        response.status_code = 200
    except Exception as e:
        response = make_response(jsonify({"msg" : f"{e}"}))
        response.status_code = 500
    return response


def add_video(id_video : int, id_lesson : int) -> None:
    try:
        video : Video = Video.query.get_or_404(id_video)
        lesson : Lesson = Lesson.query.get_or_404(id_lesson)
        lesson.videos.append(video)
        db.session.commit()
        response = make_response(jsonify({"msg": "Урок добавлен"}))
        response.status_code = 200
    except Exception as e:
        response = make_response(jsonify({"msg" : f"{e}"}))
        response.status_code = 404
    return response


def get_videos(id : int):
    try:
        lesson : Lesson = Lesson.query.get_or_404(id)
        response = make_response(jsonify(schemas_videos.dump(lesson.videos)))
    except:
        print('error')
    return response