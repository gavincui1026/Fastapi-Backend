import fastapi

from src.api.dependencies.repository import get_repository


router = fastapi.APIRouter(prefix="/order", tags=["order"])

@router.post(
    path="/submit",
    name="order:submit",
    status_code=fastapi.status.HTTP_201_CREATED,
    description="Submit order information",
)
async def upload_order(
        request: fastapi.Request,
):
    print(await request.body())