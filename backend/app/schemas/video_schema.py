from ..extensions import ma
from ..models.video import Video

class VideoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Video
        include_relationships = True
        load_instance = True