from sys import prefix

import fastapi

from src.api.dependencies.repository import get_repository
from src.api.dependencies.token import get_current_user
from src.models.db.account import Account
from src.models.schemas.survey import SurveyInCreate
from src.repository.crud.survey import SurveyCRUDRepository

router = fastapi.APIRouter(prefix="/surveys", tags=["surveys"])

@router.post(
    path="/fill-survey",
    name="surveys:fill-survey",
    status_code=fastapi.status.HTTP_201_CREATED,
    description="Fill a survey",
)
async def fill_survey(
        survey: SurveyInCreate,
        current_user: Account = fastapi.Depends(get_current_user),
        survey_repo: SurveyCRUDRepository = fastapi.Depends(get_repository(repo_type=SurveyCRUDRepository)),
):
    await survey_repo.create_survey(survey_create=survey, user=current_user)
    return fastapi.Response(status_code=fastapi.status.HTTP_201_CREATED, content="Survey created successfully!")
