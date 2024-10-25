import random

from src.models.db.account import Account
from src.repository.crud.base import BaseCRUDRepository
from src.models.db.website import Website, APIKey, Product, ProductSelected, Order, Tracking

class WebsiteCRUDRepository(BaseCRUDRepository):
    def random_api_key(self) -> str:
        return "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=32))
    async def create_website(self, website_domain, user: Account) -> None:
        new_website = Website(
            account_id=user.id,
            domain=website_domain,
        )
        self.async_session.add(new_website)
        await self.async_session.flush()
        website_a_key = APIKey(
            key=self.random_api_key(),
            website_id=new_website.id,
            key_type='websiteA'
        )
        website_b_key = APIKey(
            key=self.random_api_key(),
            website_id=new_website.id,
            key_type='websiteB'
        )
        self.async_session.add(website_a_key)
        self.async_session.add(website_b_key)
        await self.async_session.commit()

