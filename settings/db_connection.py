from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from settings.base import Config

engine = create_engine(
    Config.DATABASE,
    echo=True,
    future=True,
)


def save(obj):
    with Session(engine) as session:
        session.add(obj)
        session.commit()
