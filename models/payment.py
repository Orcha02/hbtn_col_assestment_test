#!/usr/bin/python3
"""This module defines a class Payment"""
from base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Payment(BaseModel, Base):
    """This class defines a payments by various attributes"""
    __tablename__ = "payments"
    type = Column(String(128), nullable=False)
    date = Column(Integer(128), nullable=False)
    txn_id = Column(String(60), nullable=False)
    total = Column(Integer, nullable=False)
    order_id = Column(String(60), nullable=False, ForeignKey("orders.id"))
    order = relationship("Order", backref="payments", cascade ="all, delete")
