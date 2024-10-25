import fastapi

from src.api.routes.account import router as account_router
from src.api.routes.authentication import router as auth_router
from src.api.routes.survey import router as survery_router
from src.api.routes.oss import router as oss_router
from src.api.routes.company import router as company_router
from src.api.routes.order import router as order_router
# from src.api.routes.website import router as website_router

router = fastapi.APIRouter()

router.include_router(router=account_router)
router.include_router(router=auth_router)
router.include_router(router=survery_router)
router.include_router(router=oss_router)
router.include_router(router=company_router)
router.include_router(router=order_router)
# router.include_router(router=website_router)
