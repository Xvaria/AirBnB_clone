#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, id=None, created_at=datetime.now(), updated_at=None):
        self.id = str(uuid.uuid4())
        self.created_at = created_at
        self.updated_at = BaseModel.save(self)

    @property
    def updated_at(self):
        return(self.__updated_at)

    @updated_at.setter
    def updated_at(self, time=datetime.now()):
        self.__updated_at = time

    def __str__(self):
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))
    def save(self):
        return(datetime.now())

a = BaseModel()
print(a)
