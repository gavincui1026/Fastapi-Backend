import datetime
from typing import Optional

import pydantic
from pydantic import constr, HttpUrl, EmailStr

from src.models.schemas.base import BaseSchemaModel


class SocialLinks(BaseSchemaModel):
    linkedin: Optional[HttpUrl]=None
    twitter: Optional[HttpUrl]=None

class ContactInfo(BaseSchemaModel):
    phone: constr(max_length=13,min_length=10)  # 简单的电话格式验证
    email: EmailStr
    social: Optional[SocialLinks]

class BasicInfo(BaseSchemaModel):
    description: constr(max_length=300)  # 限制描述最大300字符
    type: constr(max_length=50)  # 公司类型
    founded: int  # 公司成立年份
    website: Optional[HttpUrl]=None  # 网站链接
    employees: Optional[constr(max_length=10)]  # 公司员工数量，设置为字符串并限制最大长度
    ceo: Optional[str]  # 可选的CEO字段

class Documents(BaseSchemaModel):
    incorporation: str  # 存储文档的唯一ID
    voidCheck: str
    personalId: str

class CompanyInCreate(BaseSchemaModel):
    basicInfo: BasicInfo
    contactInfo: ContactInfo
    documents: Documents

class BankAccountInResponse(BaseSchemaModel):
    bankName: constr(max_length=50)
    accountNumber: constr(max_length=50)
    routingNumber: constr(max_length=50)
    institutionNumber: constr(max_length=50)


class ContactInfoInResponse(BaseSchemaModel):
    phone: constr(max_length=13,min_length=10)
    email: EmailStr
    social: Optional[SocialLinks]=None

class CompanyInResponse(BaseSchemaModel):
    """
      name: "TechInnovate Solutions",
      description: "TechInnovate Solutions is a cutting-edge technology company specializing in artificial intelligence and machine learning solutions. We develop innovative products that help businesses optimize their operations and make data-driven decisions.",
      type: "Technology",
      founded: "2010",
      headquarters: "San Francisco, CA",
      ceo: "Jane Doe",
      employees: "500-1000",
      website: "https://www.techinnovatesolutions.com",
    """
    name: Optional[constr(max_length=255)]
    description: constr(max_length=300)
    type: constr(max_length=50)
    founded: int
    headquarter: Optional[constr(max_length=255)]
    ceo: Optional[str]
    employees: Optional[constr(max_length=10)]
    website: Optional[HttpUrl]=None
    contact: Optional[ContactInfoInResponse]
    linkedAccount: Optional[BankAccountInResponse]
    status: str
