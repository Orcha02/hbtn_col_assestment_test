#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.order import Order
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    gov_id= Column(Integer, primary_key=True,nullable=False)
    name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=True)
    company = Column(String(128), nullable=True)
    # Relationships
    #orders = relationship('Order', backref='user', cascade='all, delete')
