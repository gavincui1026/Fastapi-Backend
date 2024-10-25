import datetime

import sqlalchemy
from sqlalchemy.orm import Mapped as SQLAlchemyMapped, mapped_column as sqlalchemy_mapped_column
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.repository.table import Base



class Company(Base):
    __tablename__ = "companies"

    id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(primary_key=True, autoincrement=True)
    account_id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.Integer, sqlalchemy.ForeignKey("account.id"), nullable=False)
    name: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=True)
    description: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.Text, nullable=False)
    type: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=100), nullable=False)
    founded: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.Integer, nullable=False)
    headquarter: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=True)
    ceo: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=100), nullable=True)
    employees: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=50), nullable=True)
    revenue: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=50), nullable=True)
    website: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=True)
    phone: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=20), nullable=True)
    email: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=100), nullable=True)
    linkedin: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=True)
    twitter: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=True)
    status: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=8), nullable=False, default='pending')
    void_check: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=True)
    personal_id: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=True)
    incorporation: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=True)
    account=sqlalchemy.orm.relationship("Account", back_populates="company")
    created_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True), nullable=False, server_default=sqlalchemy_functions.now()
    )
    updated_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True), nullable=True, server_onupdate=sqlalchemy.schema.FetchedValue(for_update=True)
    )

    # 建立与 LinkedAccount 的一对一关系
    linked_account: SQLAlchemyMapped["LinkedAccount"] = sqlalchemy.orm.relationship(
        "LinkedAccount", back_populates="company", uselist=False
    )

class LinkedAccount(Base):
    __tablename__ = "linked_accounts"

    id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(primary_key=True, autoincrement=True)
    company_id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.Integer, sqlalchemy.ForeignKey("companies.id"), nullable=False, unique=True)
    bank_name: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=100), nullable=False)
    account_number: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=20), nullable=False)
    routing_number: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=20), nullable=False)
    institution_number: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=20), nullable=False)
    created_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True), nullable=False, server_default=sqlalchemy_functions.now()
    )
    updated_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True), nullable=True, server_onupdate=sqlalchemy.schema.FetchedValue(for_update=True)
    )

    # 建立与 Company 的一对一关系
    company: SQLAlchemyMapped["Company"] = sqlalchemy.orm.relationship("Company", back_populates="linked_account")

    # 绑定一个函数，用于查询bank name
