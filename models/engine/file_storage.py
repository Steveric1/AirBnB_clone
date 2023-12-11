#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """It represents an abstract storage engine.

    Attributes:
        __file_path (str): Name of the file to save objects to
        __objects (dict): Dictionary of the instances of object.
    """
    __file_path = "file.json"
    __objects = {}
    cls_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                "City": City, "Amenity": Amenity, "Place": Place,
                "Review": Review}

    def all(self):
        """Returns the dictionary objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        prm_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[prm_key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        objects_serialized = {}
        for prm_key, obj in self.__objects.items():
            objects_serialized[prm_key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(objects_serialized, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        Only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file does not exist, no exception should be raised.
        """
        try:
            if self.__file_path:
                with open(self.__file_path) as f:
                    deserialized = json.load(f)
                for key, val in deserialized.items():
                    object = self.cls_dict[val['__class__']](**val)
                    self.__objects[key] = object
        except FileNotFoundError:
            pass
