#!/usr/bin/python3
from models.base_model import BaseModel
import json

class FileStorage:
    ''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return(FileStorage.__objects)

    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__+ "." + obj.id] = obj

    def save(self):
        try:
            sdict = {}
            for k, v in FileStorage.__objects.items():
                sdict[k] = v.to_dict()
            with open(self.__file_path, mode="w") as f:
                json.dump(sdict, f)
        except:
            pass

    def reload(self):
        try:
            with open(self.__file_path, mode="r") as f:
                FileStorage.__objects = json.load(f)
            for val in FileStorage.__objects.values():
                self.new(BaseModel(**val))
        except:
            pass
