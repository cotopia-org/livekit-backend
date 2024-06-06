from typing import Annotated

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from api.utils.auth import get_current_active_user
from api.utils.role import create_da_role, get_da_role_by_id, delete_da_role
from db.db_setup import get_db
from schemas.role import Role, RoleBase
from schemas.user import User

router = fastapi.APIRouter()


@router.post("/roles/create", response_model=Role, status_code=201)
async def create_role(
    role: RoleBase,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: Session = Depends(get_db),
):
    return create_da_role(db=db, role=role)


@router.delete("/permissions/{permission_id}/delete", status_code=204)
async def delete_permission(
    permission_id: int,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: Session = Depends(get_db),
):
    db_permission = get_da_permission_by_id(db=db, permission_id=permission_id)
    if db_permission is None:
        raise HTTPException(
            status_code=404, detail=f"Permission (id = {permission_id}) not found!"
        )
    else:
        if True:  # check permission to to this
            delete_da_permission(db=db, permission_id=permission_id)
        else:
            raise HTTPException(
                status_code=403, detail="You are not allowed to do this!"
            )
