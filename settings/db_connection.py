from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(
    environ.get(
        "CHALLANGE_DB", "postgresql://postgres:postgres@localhost:5436/challengedb"
    ),
    echo=True,
    future=True,
)


def save_all(objs):
    with Session(engine) as session:
        session.add_all(objs)
        session.commit()
