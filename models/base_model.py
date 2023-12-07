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
                'created_at': self.dt_format(self.created_at),
                'updated_at': self.dt_format(self.updated_at)
                }
