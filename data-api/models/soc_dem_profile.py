from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    func,
)

from database.engine import Base


class SocDemProfile(Base):
    __tablename__ = "soc_dem_profiles"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    age = Column(Integer)
    workclass = Column(String)
    education = Column(String)
    education_num = Column(Integer)
    marital_status = Column(String)
    occupation = Column(String)
    capital_gain = Column(Integer)
    capital_loss = Column(Integer)
    hours_per_week = Column(Integer)

    income = Column(String, nullable=True)  # target

    was_used_for_training = Column(Boolean, default=False)

    created_at = Column(DateTime, default=func.now())
