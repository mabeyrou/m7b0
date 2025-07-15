from sqlalchemy import Column, Integer, String

from ..database import Base


class EducationLevel(Base):
    __tablename__ = "education_levels"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    label = Column(String, nullable=False)
