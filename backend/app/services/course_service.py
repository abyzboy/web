# app/services/course_service.py
from app.models.course import Course
from app.models.user import User
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

def add_user(user_id, course_id):
    course : Course
    user : User
    try:
        course = Course.query.get_or_404(course_id)
    except:
        response = make_response(jsonify({"msg": "Нету такого курса"}))
        response.status_code = 404
        return response
    try:
        user = User.query.get_or_404(user_id)
    except:
        response = make_response(jsonify({"msg": "Нету такого пользователя"}))
        response.status_code = 404
        return response
    try:
        course.students.append(user)
        course.save()
        response = make_response(jsonify({"msg": "Успешно"}))
        response.status = 200
    except Exception as e:
        response = make_response(jsonify({"msg" :str(e)}))
        response.status = 500
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

def put_course(id, title, description):
    try:
        course : Course = Course.query.get(id)
        course.title = title
        course.description = description
        course.save()
        response = make_response(jsonify({"msg": "Курс успешно изменен"}))
        response.status_code = 200
    except Exception as e:
        response = make_response(jsonify({"msg": "Курс не был найден"}))
        response.status_code = 404
    return response

def get_course_by_user(user_id):
    try:
        user : User = User.query.get_or_404(user_id)
        response = make_response(jsonify(schemas.dump(user.courses)))
        response.status_code = 200
    except:
        response = make_response(jsonify({'msg': 'Error not found user'}))
        response.status = 404
    return response