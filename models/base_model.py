#!/usr/bin/python3

# import models
# import uuid
# from datetime import datetime
#
# """
# AirBnb BaseModel
# """
#
#
# class BaseModel:
#     """
#     BaseModel initialization
#     """
#     unique_key = uuid
#     dt = datetime
#
#     def __init__(self, *args, **kwargs):
#         """
#         Initializes BaseModel instance.
#         """
#         if kwargs:
#             if "__class__" in kwargs:
#                 del kwargs["__class__"]
#
#             for key, value in kwargs.items():
#                 if key in ["created_at", "updated_at"] and type(value) == str:
#                     kwargs[key] = self.str_to_d_time(value)
#
#             self.__dict__.update(kwargs)
#         else:
#             self.id = str(self.unique_key.uuid4())
#             self.created_at = self.dt.now()
#             self.updated_at = self.dt.now()
#             models.storage.new(self)
#
#     def __str__(self):
#         """String Representation"""
#         class_name = __class__.__name__
#         return f"[{class_name}] ({self.id}) {self.__dict__}"
#
#     def __repr__(self):
#         """
#         returns string repr
#         """
#         return (self.__str__())
#
#     def save(self):
#         """updates the public instance attribute updated_at
#         with the current datetime"""
#         self.updated_at = self.dt.now()
#         models.storage.save()
#
#     def str_to_d_time(self, d_string, format="%Y-%m-%dT%H:%M:%S.%f"):
#         """
#         Converts a string to a datetime object.
#         """
#         try:
#             return datetime.strptime(d_string, format)
#         except ValueError:
#             raise ValueError("Invalid string or format")
#
#     def dt_format(self, d_time):
#         """
#         Formats a datetime object.
#         """
#         return d_time.isoformat()
#
#     def to_dict(self):
#         """
#         Returns a dictionary containing all keys/values
#         of __dict__ of the instance.
#         """
#         return {
#             **self.__dict__,
#             '__class__': self.__class__.__name__,
#             'created_at': self.dt_format(self.created_at),
#             'updated_at': self.dt_format(self.updated_at)
#         }
"""Defining the BaseModel class."""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for all other subclasses.
    Defines all common attributes and methods for subclasses.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel."""
        date_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, date_format)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """A string representation of the instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute and save the instance."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values."""
        v_dict = self.__dict__.copy()
        v_dict["created_at"] = self.created_at.isoformat()
        v_dict["updated_at"] = self.updated_at.isoformat()
        v_dict["__class__"] = self.__class__.__name__
        return v_dict
