from sqlalchemy import Column, Integer, ForeignKey, DateTime, func

from database.engine import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    soc_dem_profile_id = Column(Integer, ForeignKey("soc_dem_profiles.id"))

    created_at = Column(DateTime, default=func.now())
