from sqlalchemy.orm import Session
from .base import CRUDBase
from models.user import User
from models.soc_dem_profile import SocDemProfile
from schemas.soc_dem_profile import SocDemProfileCreate
from schemas.user import UserUpdate


class CRUDUser(CRUDBase[User, SocDemProfileCreate, UserUpdate]):
    def create(self, db: Session, *, obj_in: SocDemProfileCreate) -> User:
        """
        Crée un profil socio-démographique, puis crée un utilisateur associé.
        """
        profile_obj = SocDemProfile(**obj_in.dict())
        db.add(profile_obj)
        db.commit()
        db.refresh(profile_obj)

        user_obj = self.model(soc_dem_profile_id=profile_obj.id)
        db.add(user_obj)
        db.commit()
        db.refresh(user_obj)

        return user_obj


user_crud = CRUDUser(User)
