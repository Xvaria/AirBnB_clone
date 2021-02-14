#!/usr/bin/python3
""" Save the file, import objects, etc """
from models.base_model import BaseModel
import json


class FileStorage:
    """ Class file storage with methods to load, create, return, etc. """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return all the objects """
        return(FileStorage.__objects)

    def new(self, obj):
        """ Create the new objects """
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ Save the objects into a file """
        sdict = {}
        for k, v in FileStorage.__objects.items():
            sdict[k] = v.to_dict()
        with open(self.__file_path, mode="w") as f:
            json.dump(sdict, f)

    def reload(self):
        """ Reload a file to load objs """
        try:
            with open(self.__file_path, mode="r") as f:
                FileStorage.__objects = json.load(f)
            for val in FileStorage.__objects.values():
                self.new(BaseModel(**val))
        except FileNotFoundError:
            pass
