import datetime
from typing import Optional

import pydantic
from pydantic import constr, Field

from src.models.schemas.base import BaseSchemaModel


class SurveyInCreate(BaseSchemaModel):

    # Whether the user has e-commerce experience (Required)
    is_ecommerce_experienced: bool = Field(..., description="Does the user have e-commerce experience?")

    # Describe the user's e-commerce experience (Optional)
    ecommerce_experience: Optional[constr(max_length=1024)] = Field(None,
                                                                    description="Description of the e-commerce experience, if any")

    # Whether the user has registered a company (Required)
    is_registered: bool = Field(..., description="Has the user registered a company?")

    # Type of products the user plans to sell (Optional)
    product_type: Optional[constr(max_length=64)] = Field(None, description="Type of products the user plans to sell")

    # Whether the user needs assistance with website building (Required)
    website_building_assistance: bool = Field(..., description="Does the user need assistance with website building?")

    # Whether the user needs assistance with shipping (Required)
    shipping_assistance: bool = Field(..., description="Does the user need assistance with shipping?")

    # Whether the user needs assistance with payment gateway setup (Required)
    payment_gateway_assistance: bool = Field(...,
                                             description="Does the user need assistance with payment gateway setup?")

    # Additional comments (Optional)
    additional_comments: Optional[constr(max_length=1024)] = Field(None,
                                                                   description="Any additional comments or information")


    class Config:
        orm_mode = True