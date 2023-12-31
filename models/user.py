#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User

    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name

    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
