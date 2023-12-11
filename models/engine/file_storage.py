#!/usr/bin/python3
"""file storage for AirBnB Clone Project"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:

    """ This is the storage for the AirBnB Clone Project
    class Methods:
        all: Return the dictionary object
        new: Set in object with the key id
        save: Serialize object dictionary to json string
        reload: Desserialize json to objec dictionary

    class Attribute:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - store object dictionary
    """
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                  "City": City, "Amenity": Amenity, "Place": Place,
                  "Review": Review}

    def all(self):
        """Return the dictionary object"""
        return self.__objects

    def new(self, obj):
        """Creating dictionary from an existing object"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Save/serialize obj dictionaries to json file"""
        serialized_obj = {}

        for key, value in self.__objects.items():
            serialized_obj[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """Retrieving -> Deserialized json (string) to object (dictionary)"""
        try:

            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                deserialized = json.load(file)
            for key, value in deserialized.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
