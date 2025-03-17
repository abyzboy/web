from ..extensions import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Video(db.Model):
    id : Mapped[int] = mapped_column(Integer(), primary_key=True)
    path : Mapped[str] = mapped_column(String(100), nullable=False)
    lesson_id : Mapped[int] = mapped_column(Integer(), ForeignKey('lesson.id'))
    lesson = relationship('Lesson', back_populates='videos', uselist=False)
    
    def create(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()