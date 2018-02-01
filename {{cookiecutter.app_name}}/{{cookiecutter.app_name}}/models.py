from typing import Any

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base: Any = declarative_base()


class Example(Base):
    __tablename__ = 'Example'

    id = Column(Integer, primary_key=True)
    name = Column(String)
