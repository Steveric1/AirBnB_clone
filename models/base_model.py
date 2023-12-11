#!/usr/bin/python3

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
