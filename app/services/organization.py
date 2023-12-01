from sqlalchemy.orm import Session
from app.models.organization import Organization
from app.repositories.organization import get_by_name
from app.schemas.organization import OrganizationCreate


async def organization_create(dto: OrganizationCreate, db: Session):
    if get_by_name(db, dto.name):
        return {"error": "organization already exists"}

    new_organization = Organization(
        name=dto.name,
        created_by="system",
        updated_by="system",
    )
    db.add(new_organization)
    db.commit()
    db.refresh(new_organization)

    return new_organization


async def organization_view(dto: OrganizationCreate, db: Session):
    if not get_by_name(db, dto.name):
        return {"error": "the name does not exist"}

    return get_by_name(db, dto.name)