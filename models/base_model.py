import uuid
from datetime import datetime
import json

"""
AirBnb BaseModel
"""


class BaseModel:
    """
    BaseModel initialization
    """
    unique_key = uuid
    dt = datetime

    def __init__(self, *args, **kwargs):
        """
        Initializes BaseModel instance.
        """
        self.updated_at = self.dt.now()
        self.id = str(self.unique_key.uuid4())
        self.created_at = self.dt.now()

        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]

            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"] and type(value) == str:
                    kwargs[key] = self.str_to_d_time(value)

            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def str_to_d_time(self, d_string, format="%Y-%m-%dT%H:%M:%S.%f"):
        """
        Converts a string to a datetime object.
        """
        try:
            return datetime.strptime(d_string, format)
        except ValueError:
            raise ValueError("Invalid string or format")

    def to_json(self):
        """
        Returns a JSON representation of the BaseModel instance.
        """
        return json.dumps(self.to_dict(), indent=4)

    def __str__(self):
        """
        String Representation of the BaseModel instance.
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = self.dt.now()

    def dt_format(self, d_time):
        """
        Formats a datetime object.
        """
        return d_time.isoformat()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        return {
            **self.__dict__,
            '__class__': self.__class__.__name__,
            'created_at': self.dt_format(self.created_at),
            'updated_at': self.dt_format(self.updated_at)
        }
