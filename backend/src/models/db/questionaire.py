import datetime
import typing

import sqlalchemy
from sqlalchemy.orm import Mapped as SQLAlchemyMapped, mapped_column as sqlalchemy_mapped_column
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.repository.table import Base

class Questionaire(Base):  # type: ignore
    __tablename__ = "questionaire"

    id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(primary_key=True, autoincrement="auto")
    account_id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.ForeignKey("account.id"), nullable=False)
    is_ecommerce_experienced: SQLAlchemyMapped[bool] = sqlalchemy_mapped_column(sqlalchemy.Boolean, nullable=False)
    ecommerce_experience: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=1024), nullable=True)
    is_registered: SQLAlchemyMapped[bool] = sqlalchemy_mapped_column(sqlalchemy.Boolean, nullable=False)
    product_type: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=64), nullable=True)
    website_building_assistance: SQLAlchemyMapped[bool] = sqlalchemy_mapped_column(sqlalchemy.Boolean, nullable=False)
    shipping_assistance: SQLAlchemyMapped[bool] = sqlalchemy_mapped_column(sqlalchemy.Boolean, nullable=False)
    payment_gateway_assistance: SQLAlchemyMapped[bool] = sqlalchemy_mapped_column(sqlalchemy.Boolean, nullable=False)
    additional_comments: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=1024), nullable=True)
    created_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True), nullable=False, server_default=sqlalchemy_functions.now()
    )
    updated_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=True,
        server_onupdate=sqlalchemy.schema.FetchedValue(for_update=True),
    )

    __mapper_args__ = {"eager_defaults": True}

