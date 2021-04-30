from sqlalchemy import *
from .base import Base
from sqlalchemy.orm import relationship


class Country(Base):
    __tablename__ = 'countries'
    country_id = Column('country_id', Integer, primary_key=True, autoincrement=True)
    country = Column('country', String(50), nullable=True)
    states = relationship('State')

    def __init__(self, country):
        self.country = country


class State(Base):
    __tablename__ = 'states'
    state_id = Column('state_id', Integer, primary_key=True, autoincrement=True)
    state = Column('state', String(50), nullable=True)
    country_id = Column('country_id', Integer, ForeignKey('countries.country_id'))

    def __init__(self, state, country_id):
        self.state = state
        self.country_id = country_id