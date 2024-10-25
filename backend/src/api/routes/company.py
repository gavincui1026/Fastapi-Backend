import fastapi

from src.api.dependencies.repository import get_repository
from src.api.dependencies.token import get_current_user
from src.models.db.account import Account
from src.models.db.company import Company
from src.models.schemas.company import CompanyInCreate, CompanyInResponse, ContactInfoInResponse, SocialLinks, \
    BankAccountInResponse
from src.repository.crud.company import CompanyCRUDRepository

router = fastapi.APIRouter(prefix="/company", tags=["company"])

@router.post(
    path="/submit",
    name="company:submit",
    status_code=fastapi.status.HTTP_201_CREATED,
    description="Submit company information",
)
async def submit_company(
        company: CompanyInCreate,
        current_user: Account = fastapi.Depends(get_current_user),
        company_repo: CompanyCRUDRepository = fastapi.Depends(get_repository(repo_type=CompanyCRUDRepository)),
):
    try:
        await company_repo.is_company_created(user=current_user)
    except ValueError as e:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_400_BAD_REQUEST, detail=str(e))
    await company_repo.create_company(company_create=company, user=current_user)
    return fastapi.Response(status_code=fastapi.status.HTTP_201_CREATED, content="Company created successfully!")

@router.get(
    path="/read-company",
    name="company:read",
    description="Read company information",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=CompanyInResponse,
)
async def read_company(
        current_user: Account = fastapi.Depends(get_current_user),
        company_repo: CompanyCRUDRepository = fastapi.Depends(get_repository(repo_type=CompanyCRUDRepository)),
):
    company: Company = await company_repo.read_company(user=current_user)
    return CompanyInResponse(
        name=company.name,
        description=company.description,
        type=company.type,
        founded=company.founded,
        headquarter=company.headquarter,
        ceo=company.ceo,
        employees=company.employees,
        website=company.website,
        contact=ContactInfoInResponse(
            phone=company.phone,
            email=company.email,
            social=SocialLinks(
                linkedin=company.linkedin,
                twitter=company.twitter
            ),
        ),
        linkedAccount=BankAccountInResponse(
            bankName=company.linked_account.bank_name,
            accountNumber=f"{'*' * (len(company.linked_account.account_number) - 4)}{company.linked_account.account_number[-4:]}",  # 隐藏部分银行账号
            routingNumber=company.linked_account.routing_number,
            institutionNumber=company.linked_account.institution_number
        ),
        status=company.status

    )