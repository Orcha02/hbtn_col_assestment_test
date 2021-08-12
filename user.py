#!/usr/bin/python3
"""This module defines a class User"""
from base_model import BaseModel, Base
from order import Order
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    gov_id= Column(int(20), primary_key=True,nullable=False)
    name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=True)
    company = Column(String(128), nullable=True)
    # Relationships
    order = relationship('Order', backref='user', cascade='all, delete')
