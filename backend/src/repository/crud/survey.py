from src.models.db.account import Account
from src.models.db.questionaire import Questionaire
from src.models.schemas.survey import SurveyInCreate
from src.repository.crud.base import BaseCRUDRepository


class SurveyCRUDRepository(BaseCRUDRepository):
    async def create_survey(self, survey_create: SurveyInCreate,user: Account) -> Questionaire:
        new_survey = Questionaire(
            **survey_create.model_dump(),
            account_id=user.id
        )

        self.async_session.add(instance=new_survey)
        await self.async_session.commit()
        await self.async_session.refresh(instance=new_survey)

        return new_survey