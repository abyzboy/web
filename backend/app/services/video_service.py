# app/services/course_service.py
from app.models.video import Video
from app.models.lesson import Lesson
from app.schemas.video_schema import VideoSchema
from flask import jsonify, make_response
schema = VideoSchema()
schemas = VideoSchema(many=True)

def get_all_videos():
    videos = Video.query.all()
    response = make_response(jsonify(schemas.dump(videos)))
    response.status_code = 200
    return response

def create_video(path, id):
    video : Video = Video(path=path, lesson_id=id)
    response = make_response(jsonify({"msg":" VIDEO SUCCES"}))
    response.status_code = 200
    video.create()
    return response
