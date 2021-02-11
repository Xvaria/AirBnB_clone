#!/usr/bin/python3
import uuid
from datetime import datetime
from time import sleep


class BaseModel:
    """  """
    def __init__(self, id=None, updated_at=None, created_at=None):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @property
    def updated_at(self):
        return self.updated_at

    @updated_at.setter
    def updated_at(self, berga):
        self.updated_at = berga


a = BaseModel()
print(a.created_at)
