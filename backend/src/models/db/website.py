import datetime

import sqlalchemy
from sqlalchemy.orm import Mapped as SQLAlchemyMapped, mapped_column as sqlalchemy_mapped_column, relationship
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.repository.table import Base




class Website(Base):
    __tablename__ = "websites"

    id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(primary_key=True, autoincrement=True)
    account_id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.ForeignKey("account.id"), nullable=False)
    domain: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=False)
    woo_commerce_key: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=True)
    # Relationships
    account: SQLAlchemyMapped["Account"] = relationship("Account", back_populates="websites")
    products_selected: SQLAlchemyMapped[list["ProductSelected"]] = relationship("ProductSelected", back_populates="website")
    api_keys: SQLAlchemyMapped[list["APIKey"]] = relationship("APIKey", back_populates="website")
    # Timestamps
    created_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=False,
        server_default=sqlalchemy_functions.now()
    )
    updated_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=False,
        server_default=sqlalchemy_functions.now(),
        onupdate=sqlalchemy_functions.now()
    )


class APIKey(Base):
    __tablename__ = "api_keys"

    id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(primary_key=True, autoincrement=True)
    key: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=False, unique=True, index=True)
    website_id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.ForeignKey("websites.id"), nullable=False)
    key_type: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=16), nullable=False) # websiteA or websiteB
    # Relationships
    website: SQLAlchemyMapped["Website"] = relationship("Website", back_populates="api_keys")
    # Timestamps
    created_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=False,
        server_default=sqlalchemy_functions.now()
    )
    updated_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=False,
        server_default=sqlalchemy_functions.now(),
        onupdate=sqlalchemy_functions.now()
    )



class Product(Base):
    __tablename__ = "products"

    # Product basic information
    id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(primary_key=True, autoincrement=True)

    # 对应 Excel 的 "商品标题*"
    name: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=False)

    # 对应 Excel 的 "商品主图" 或 "商品图片*"
    picture: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=False)

    # 对应 Excel 的 "商品描述"
    description: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.Text, nullable=False)

    # 对应 Excel 的 "SEO描述" 作为简短描述
    short_description: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.Text, nullable=True)

    # SEO 相关字段 (新增)
    # 对应 Excel 的 "SEO标题"
    seo_title: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=True)

    # 对应 Excel 的 "SEO描述"
    seo_description: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.Text, nullable=True)

    # Product pricing
    # 对应 Excel 可能的价格字段
    regular_price: SQLAlchemyMapped[float] = sqlalchemy_mapped_column(sqlalchemy.Float, nullable=False)  # 保留此字段
    sale_price: SQLAlchemyMapped[float] = sqlalchemy_mapped_column(sqlalchemy.Float, nullable=True)  # 保留此字段
    cost: SQLAlchemyMapped[float] = sqlalchemy_mapped_column(sqlalchemy.Float, nullable=False)  # 保留此字段

    # Inventory and SKU
    # 对应 Excel 的 "商品条形码"
    sku: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=100), nullable=True)

    # 对应 Excel 的 "商品库存"
    stock_quantity: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.Integer, nullable=True)

    # 管理库存 (保留)
    manage_stock: SQLAlchemyMapped[bool] = sqlalchemy_mapped_column(sqlalchemy.Boolean, nullable=False,
                                                                    server_default="1")

    # Product type and status (保留)
    product_type: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=50), nullable=False,
                                                                   server_default="simple")
    status: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=50), nullable=False,
                                                             server_default="publish")

    # Categories and tags
    # 对应 Excel 的 "分类名" (保持索引)
    categories: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=True,
                                                                 index=True)

    # Relationships (保留)
    products_selected: SQLAlchemyMapped[list["ProductSelected"]] = relationship("ProductSelected",
                                                                                back_populates="product")

    # Timestamps
    created_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=False,
        server_default=sqlalchemy_functions.now()
    )
    updated_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=False,
        server_default=sqlalchemy_functions.now(),
        onupdate=sqlalchemy_functions.now()
    )


class ProductSelected(Base):
    __tablename__ = "products_selected"

    id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(primary_key=True, autoincrement=True)
    website_id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.ForeignKey("websites.id"), nullable=False)
    product_id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.ForeignKey("products.id"), nullable=False)

    # Relationships
    website: SQLAlchemyMapped["Website"] = relationship("Website", back_populates="products_selected")
    product: SQLAlchemyMapped["Product"] = relationship("Product", back_populates="products_selected")
    orders: SQLAlchemyMapped[list["Order"]] = relationship("Order", back_populates="product_selected")

    # Timestamps
    created_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=False,
        server_default=sqlalchemy_functions.now()
    )
    updated_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=False,
        server_default=sqlalchemy_functions.now(),
        onupdate=sqlalchemy_functions.now()
    )


class Order(Base):
    __tablename__ = "orders"

    id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(primary_key=True, autoincrement=True)
    product_selected_id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.ForeignKey("products_selected.id"), nullable=False)
    status: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=False)
    # Possible statuses: pending, unpaid, processing, shipped, delivered

    # Relationships
    product_selected: SQLAlchemyMapped["ProductSelected"] = relationship("ProductSelected", back_populates="orders")
    tracking: SQLAlchemyMapped["Tracking"] = relationship("Tracking", back_populates="order")

    # Timestamps
    created_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=False,
        server_default=sqlalchemy_functions.now()
    )
    updated_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=False,
        server_default=sqlalchemy_functions.now(),
        onupdate=sqlalchemy_functions.now()
    )

class Tracking(Base):
    __tablename__ = "trackings"

    id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(primary_key=True, autoincrement=True)
    carrier: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=False)
    tracking_number: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=255), nullable=False)
    order_id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.ForeignKey("orders.id"), nullable=False)
    order: SQLAlchemyMapped["Order"] = relationship("Order", back_populates="tracking")