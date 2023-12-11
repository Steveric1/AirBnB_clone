#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, email, password, first_name, last_name, **kwargs):
        super().__init__(**kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
