#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            returns the list of City instances
            with state_id equals to the current State.id
            """
            from models import storage
            city_list = []
            city_dict = storage.all(City)

            for city in city_dict.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
        cities = relationship("City", cascade="delete, delete-orphan",
                              backref="state")
    else:
        name = ""
