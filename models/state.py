#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
storage_type =getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")
        
    else:
        @property
        def cities(self):
            """list of city instances"""
            city_list = []
            city_all = storage.all(City)
            for city in city_all.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
