from sqlalchemy import Column, Integer, String

from database import Base


class EmploymentStatus(Base):
    __tablename__ = "employment_statuses"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    label = Column(String, nullable=False)
