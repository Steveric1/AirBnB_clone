#!/usr/bin/python3
"""Filestorage for the AirBnB Clone Project"""

import json
from models.base_model import BaseModel

class FileStorage:
    
    """This is the storage for the AirBnb Clone Project
    class methods:
       all: Return the dictionary object
       new: Set in object with the key id
       save: Serialize object dictionary to json string
       reload: Desserialize json to objec dictionary
    
    class Attribute:
       __file_path: string - path to the JSON file (ex: file.json)
       __objects: dictionary - empty but will store all objects by <class name>.id 
       (ex: to store a BaseModel object with id=12121212, 
       the key will be BaseModel.12121212)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary object"""
        return self.__objects

    def new(self, obj):
        """Creating dictionary from an existing object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Save/serialize obj dictionaries to json file"""
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)
    def reload(self):
        """Retrieving -> Deserialized json (string) to object (dictionary)"""
        try:
            if self.__file_path:
                with open(self.__file_path, 'r', encoding="UTF-8") as file:
                    deserialize = json.load(file)
                #will come back to this later for the implementation
        except FileNotFoundError:
            pass