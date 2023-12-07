#!/usr/bin/env bash

import uuid
from datetime import datetime
import json

"""
AirBnb BaseModel
"""


class BaseModel:
    """
    BaseModel initilization
    """
    unique_key = uuid
    dt = datetime

    def __init__(self, *args, **kwargs):
        self.updated_at = self.dt.now()
        self.id = str(self.unique_key.uuid4())
        self.created_at = self.dt.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, value)

            if "updated_at" in kwargs:
                self.convert_dt_attr(kwargs['updated_at'], 'updated_at')
            if "created_at" in kwargs:
                self.convert_dt_attr(kwargs['created_at'], 'created_at')
        else:
            self.updated_at = self.dt.now()
            self.id = str(self.unique_key.uuid4())
            self.created_at = self.dt.now()

    def convert_dt_attr(self, attr_value, attr_name):
        """updated_at conversion from string to datetime object"""
        try:
            setattr(
                self,
                attr_name,
                self.dt.strptime(attr_value, "%Y-%m-%dT%H:%M:%S.%f")
            )
            return getattr(self, attr_name)
        except ValueError:
            raise ValueError("invalid string or format")

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    def __str__(self):
        """String Representation"""
        class_name = __class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = self.dt.now()

    def dt_format(self, d_time):
        """datetime format method"""
        return d_time.isoformat()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        return {
                **self.__dict__,
                '__class__': self.__class__.__name__,
                'id': str(self.id),
                'created_at': self.dt_format(self.created_at),
                'updated_at': self.dt_format(self.updated_at)
                }


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                   my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
