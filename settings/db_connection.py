import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(
    os.getenv("CHALLANGE_DB"),
    echo=True,
    future=True
)

def save(obj):
    with Session(engine) as session:
        session.add(obj)
        session.commit()