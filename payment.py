#!/usr/bin/python3
"""This module defines a class Payment"""
from base_model import BaseModel, Base
from order import
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Payment(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    'type' = Column(String(128), nullable=False)
    date = Column(Integer(128), nullable=False)
    txn_id = Column(Integer(128))
    total = Column(Integer(128))
    order = relationship("Order", backref="order", cascade ="all, delete")
