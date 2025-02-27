# app/services/course_service.py
from app.models.course import Course

def get_all_courses():
    return Course.query.all()

def create_course(title,description, id):
    course = Course(title=title, description=description, author_id=id)
    course.save()
    return course

def get_course_by_id(id):
    return Course.query.get(id)

def delete_course(id):
    try:
        course : Course = Course.query.get(id)
        course.delete()
        return "Success", 204
    except Exception as e:
        return "Курса нету такого", 400