from schemas.user import UserRead, UserUpdate
from schemas.soc_dem_profile import (
    SocDemProfileCreate,
)
from routes.base_router import create_crud_router
from crud.user import user_crud

router = create_crud_router(
    crud_service=user_crud,
    schema_create=SocDemProfileCreate,
    schema_read=UserRead,
    schema_update=UserUpdate,
    prefix="/users",
    tags=["users"],
)
