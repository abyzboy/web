from app.models.lesson import Lesson
from app.models.video import Video
from app.models.course import Course
from flask import jsonify


def get_all_lessons() -> list[Lesson]:
    return Lesson.query.all()

def get_lesson_by_id(id: int) -> Lesson: 
    return Lesson.query.get(id)

def delete_lesson(id : int) -> None:
    lesson : Lesson = Lesson.query.get(id)
    lesson.delete()

def create_lesson(course_id :int, title : str) -> str:
    course : Course = Course.query.get(course_id)
    lesson : Lesson = Lesson(course_id=course_id, title=title)
    lesson.create()
    course.lessons.append(lesson)
    return lesson


def add_video(video, lesson : Lesson) -> None:
    lesson.videos.append(video)