import fastapi

router = fastapi.APIRouter(prefix="/website", tags=["website"])
from src.api.dependencies.repository import get_repository
from src.repository.crud.website import WebsiteCRUDRepository