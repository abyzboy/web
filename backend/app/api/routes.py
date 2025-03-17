from flask_restx import Api
from app.api.resources.courses import api as courses_ns  # Импорт Namespace для курсов
from app.api.resources.users import api as users_ns      # Импорт Namespace для пользователей
from app.api.resources.auth import api as auth_ns        # Импорт Namespace для аутентификации
from app.api.resources.test import api as test_ns
from app.api.resources.lesson import api as lesson_ns
from app.api.resources.video import api as video_ns
# Создание объекта Api с настройками
api = Api(
    version="1.0",                  # Версия API
    title="Courses API",            # Название API
    description="REST API для управления курсами и пользователями",  # Описание
    doc="/docs",                    # Путь к Swagger-документации
    security="Bearer Auth",         # Глобальная настройка безопасности (например, JWT)
    authorizations={                # Конфигурация авторизации для Swagger
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Пример: Bearer <JWT-токен>"
        }
    }
)

# Регистрация Namespace (групп эндпоинтов)
api.add_namespace(courses_ns, path="/api/v1/courses")  # Курсы
api.add_namespace(users_ns, path="/api/v1/users")       # Пользователи
api.add_namespace(auth_ns, path="/api/v1/auth")         # Аутентификация
api.add_namespace(test_ns, path="/api/v1/test")
api.add_namespace(lesson_ns, path='/api/v1/lessons')
api.add_namespace(video_ns, path='/api/v1/videos')