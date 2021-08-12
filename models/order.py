#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Order(BaseModel, Base):
    """This class defines a order by various attributes"""
    __tablename__ = "orders"
    date = Column(DateTime, default=datetime.datetime.utcnow)
    total = Column(Integer, nullable=False)
    subtotal = Column(Integer, nullable=False)
    taxes = Column(String(128), nullable=False)
    user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
    shipping_id = Column(String(60), nullable=False, ForeignKey("shippings.id"))
    user = relationship("User", backref="orders", cascade="all, delete")
    shipping = relationship("Shipping", backref="orders", cascade="all, delete")
