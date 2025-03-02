# app/services/course_service.py
from app.models.course import Course
from app.schemas.course_schema import CourseSchema
from flask import jsonify, make_response
schema = CourseSchema()
schemas = CourseSchema(many=True)

def get_all_courses():
    courses = Course.query.all()
    response = make_response(jsonify(schemas.dump(courses)))
    response.status_code = 200
    return response

def create_course(title,description, id):
    course = Course(title=title, description=description, author_id=id)
    course.save()
    response = make_response(jsonify(schema.dump(course)))
    response.status = 201
    return response

def get_course_by_id(id):
    try:
        course = Course.query.get_or_404(id)
        response = make_response(jsonify(schema.dump(course)))
        response.status_code = 200
    except :
        response = make_response(jsonify({"msg" : "Нету такого id"}))
        response.status_code = 404
    return response

def delete_course(id):
    try:
        course : Course = Course.query.get(id)
        course.delete()
        response = make_response(jsonify({"msg": "Курс успешно удален"}))
        response.status_code = 200
    except Exception as e:
        response = make_response(jsonify({"msg": "Курс не был найден"}))
        response.status_code = 404
    return response