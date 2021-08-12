#!/usr/bin/python3
"""This module defines a class Payment"""
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Payment(BaseModel, Base):
    """This class defines a payments by various attributes"""
    __tablename__ = "payments"
    type = Column(String(128), nullable=False)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    txn_id = Column(String(60), nullable=False)
    total = Column(Integer, nullable=False)
    order_id = Column(String(60), ForeignKey("orders.id"), nullable=False)
    order = relationship("Order", backref="payments", cascade ="all, delete")
