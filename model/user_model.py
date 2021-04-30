from sqlalchemy import *
from .base import Base
from sqlalchemy.orm import relationship
from .state_model import State
import datetime
from sqlalchemy.types import Date

# A User Class to model user details
class User(Base):
    __tablename__ = 'users'
    id = Column('id', String(70), primary_key=True)    
    first_name = Column('first_name', String(50), nullable=True)
    last_name = Column('last_name', String(50), nullable=True)
    user_name = Column('user_name', String(50), nullable=True, unique=True)
    email = Column('email', String(100), nullable=True, unique=True)
    password = Column('password', String(100), nullable=True)
    phone_number = Column('phone_number', String(20), nullable=True)
    date_of_birth = Column(Date, nullable=False)
    state_id = Column('state_id', Integer, ForeignKey(State.state_id))
    version = Column('version', Integer, nullable = False)

    def __init__(self, id=id, first_name=None, last_name=None, user_name=None, email=None, password=None, phone_number=None, date_of_birth=None, state_id=None, version=None):       
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.state_id = state_id
        self.version = version






