#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],\
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],\
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return(self.__dict__)
