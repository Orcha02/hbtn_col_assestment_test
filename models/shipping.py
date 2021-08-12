#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer


class Shipping(BaseModel, Base):
    """This class defines a shipping by various attributes"""
    __tablename__ = "shippings"
    address = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    state = Column(String(128), nullable=False)
    country = Column(String(128), nullable=False)
    cost = Column(Integer, nullable=False)
