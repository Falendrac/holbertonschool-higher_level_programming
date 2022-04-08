#!/usr/bin/python3
"""
Contain class definition of a City and an instance Base = declarative_base()
"""


from sqlalchemy import Column, ForeignKey, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    Class definition of City that inherit of Base
    And union with states.
    """
    __tablename__ = 'cities'
    id = Column(
        Integer, Sequence('user_id_seq'), primary_key=True, nullable=False
        )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
