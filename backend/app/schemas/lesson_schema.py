from ..extensions import ma
from ..models.lesson import Lesson

class LessonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Lesson
        include_relationships = True
        load_instance = True