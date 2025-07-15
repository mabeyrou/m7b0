from schemas.soc_dem_profile import (
    SocDemProfileRead,
    SocDemProfileCreate,
    SocDemProfileUpdate,
)
from routes.base_router import create_crud_router
from crud.soc_dem_profile import soc_dem_profile_crud

router = create_crud_router(
    crud_service=soc_dem_profile_crud,
    schema_create=SocDemProfileCreate,
    schema_read=SocDemProfileRead,
    schema_update=SocDemProfileUpdate,
    prefix="/profiles",
    tags=["profiles"],
)
