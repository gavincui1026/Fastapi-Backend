import fastapi
import sqlalchemy

from src.models.db.account import Account
from src.models.db.company import Company
from src.models.schemas.company import CompanyInCreate
from src.repository.crud.base import BaseCRUDRepository

class CompanyCRUDRepository(BaseCRUDRepository):
    async def is_company_created(self, user: Account) -> None:
        company = await self.async_session.execute(sqlalchemy.select(Company).where(Company.account_id == user.id))
        if company.scalar_one_or_none():
            raise ValueError("Company already created")
    async def create_company(self, company_create: CompanyInCreate, user: Account) -> None:
        new_company = Company(
            account_id=user.id,
            description=company_create.basicInfo.description,
            type=company_create.basicInfo.type,
            founded=company_create.basicInfo.founded,
            ceo=company_create.basicInfo.ceo,
            website=company_create.basicInfo.website,
            employees=company_create.basicInfo.employees,
            phone=company_create.contactInfo.phone,
            email=company_create.contactInfo.email,
            linkedin=company_create.contactInfo.social.linkedin,
            twitter=company_create.contactInfo.social.twitter,
            void_check=company_create.documents.voidCheck,
            personal_id=company_create.documents.personalId,
            incorporation=company_create.documents.incorporation,
        )
        self.async_session.add(new_company)
        await self.async_session.commit()

    async def read_company(self, user: Account) -> Company:
        company = await self.async_session.execute(sqlalchemy.select(Company).where(Company.account_id == user.id).options(sqlalchemy.orm.selectinload(Company.linked_account)))
        company = company.scalar_one_or_none()
        if not company:
            raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND, detail="Company not found")
        if company.status == 'pending':
            raise fastapi.HTTPException(status_code=fastapi.status.HTTP_400_BAD_REQUEST, detail="Company is pending")
        return company