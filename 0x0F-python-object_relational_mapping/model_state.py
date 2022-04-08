#!/usr/bin/python3
"""
Contain class definition of a State and an instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Class definition of state that inherit of Base
    """
    __tablename__ = 'states'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
