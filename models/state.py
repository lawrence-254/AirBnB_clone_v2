#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """
        Getter attribute for filestorage that returns a list of City instances
        where state_id == State.id
        """
        cities = []
        for each in storage.all('City').values():
            if each.state_id == self.id:
                cities.append(each)
            return cities

    @property
    def cities(self):
        """Getter method to retrieve a list of City objects linked to this State"""
        city_list = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
                return city_list


    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete-orphan",
                              backref="state")
