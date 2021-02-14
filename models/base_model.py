#!/usr/bin/python3
""" Base model for all project, create instances
depending of the time created, updated, kwargs, create id, etc. """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Base model for all project, create instances
    depending of the time created, updated, kwargs, create id, etc. """
    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Print the representation in string of an object """
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        """ Update and save the objs to a file """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dict """
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return(self.__dict__)
