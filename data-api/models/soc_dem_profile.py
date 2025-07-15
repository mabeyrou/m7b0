from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    ForeignKey,
    DateTime,
    func,
)

from ..database import Base


class SocDemProfile(Base):
    __tablename__ = "soc_dem_profiles"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    age = Column(Integer)
    workclass_id = Column(Integer, ForeignKey("employment_statuses.id"))
    education_id = Column(Integer, ForeignKey("education_levels.id"))
    education_num = Column(Integer)
    relationship_id = Column(Integer, ForeignKey("relationship_statuses.id"))
    capital_gain = Column(Integer)
    capital_loss = Column(Integer)
    hours_per_week = Column(Integer)

    income = Column(Integer, nullable=True)

    was_used_for_training = Column(Boolean, default=False)

    created_at = Column(DateTime, default=func.now())
