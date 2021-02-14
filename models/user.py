#!/usr/bin/python3
""" User data """
from models.base_model import BaseModel


class User(BaseModel):
    """ Public class attributes about user data """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
