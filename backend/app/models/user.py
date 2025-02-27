from ..extensions import db, ma
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
class User(db.Model):
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    username : Mapped[str] = mapped_column(String(50), nullable=False)
    password : Mapped[str] = mapped_column(String(200), nullable=False)
    is_verified : Mapped[bool] = mapped_column(Boolean(), default=False)
    role : Mapped[str] = mapped_column(String(20), default='user') 
    authored_courses  = relationship('Course', back_populates='author')
    
    courses = relationship('Course', secondary='user_course_association', back_populates='students') 

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        for courses in self.authored_courses:
            db.session.delete(courses)
        db.session.delete(self)
        db.session.commit()