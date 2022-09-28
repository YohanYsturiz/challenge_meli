import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Item(Base):
    """Item model

    Attributes:
        site (str): country of item
        item_code (int): item code
        price (str): item price
        start_time (date):
        name (str): item name
        description (text): item description
        nickname (str): nick of user
    """

    __tablename__ = "item"

    id = sa.Column(sa.Integer, primary_key=True)
    site = sa.Column(sa.String(50), nullable=False)
    item_code = sa.Column(sa.Integer, nullable=False)
    price = sa.Column(sa.String(50), nullable=False)
    start_time = sa.Column(sa.String(50), nullable=False)
    name = sa.Column(sa.String(50), nullable=False)
    description = sa.Column(sa.String(150), nullable=True)
    nickname = sa.Column(sa.String(150), nullable=True)
    created_at = sa.Column(sa.DateTime(timezone=True), default=func.now())

    def __init__(self, site, item_code, price, start_time, name, description, nickname):
        self.site = site,
        self.item_code = item_code
        self.price = price
        self.start_time = start_time
        self.name = name
        self.description = description
        self.nickname = nickname
        
