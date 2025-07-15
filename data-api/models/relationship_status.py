from sqlalchemy import Column, Integer, String

from database import Base


class RelationshipStatus(Base):
    __tablename__ = "relationship_statuses"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    label = Column(String, nullable=False)
