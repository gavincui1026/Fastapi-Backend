import fastapi

from src.api.routes.account import router as account_router
from src.api.routes.authentication import router as auth_router
from src.api.routes.job import router as job_router
router = fastapi.APIRouter()

router.include_router(router=account_router)
router.include_router(router=auth_router)
router.include_router(router=job_router)