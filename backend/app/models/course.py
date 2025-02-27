from ..extensions import db, ma
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Course(db.Model):
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    title : Mapped[str] = mapped_column(String(60), nullable=False)
    description : Mapped[str] = mapped_column(String(150), nullable=True)
    author_id : Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
    author = relationship('User', back_populates='authored_courses', uselist=False) # type: ignore
    lessons = relationship('Lesson', back_populates='course')
    students = relationship('User', secondary='user_course_association', back_populates='courses') # type: ignore

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()