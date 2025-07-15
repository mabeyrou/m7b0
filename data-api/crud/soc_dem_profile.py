from .base import CRUDBase
from models.soc_dem_profile import SocDemProfile
from schemas.soc_dem_profile import (
    SocDemProfileCreate,
    SocDemProfileUpdate,
)

soc_dem_profile_crud = CRUDBase[
    SocDemProfile, SocDemProfileCreate, SocDemProfileUpdate
](SocDemProfile)
