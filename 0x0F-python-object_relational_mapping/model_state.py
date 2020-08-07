#!/usr/bin/env python3
"""Sets up an ORM for the table, states"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    ------------
    CLASS: STATE
    ------------
    DESCRIPTION:
        Creates and connects an ORM to
        manage data.
    ARGS:
        Nil.
    """
    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
