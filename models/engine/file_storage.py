#!/usr/bin/python3
from models.base_model import BaseModel
import json

class FileStorage:
    ''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return(self.__dict__)

    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__+ "." + obj.id] = obj

    def save(self):
        try:
            with open(self.__file_path, mode="w") as f:
                sdict = {}
                for k, v in self.__objects.items():
                    sdict[k] = v.to_dict()
                json.dump(sdict, f)
        except:
            pass

    def reload(self):
        try:
            with open(self.__file_path) as f:
                FileStorage.__objects = json.load(f)
        except:
            pass
