#!/usr/bin/python3

from models.basic_data import Basic_data

class Users(Basic_data):
    """
    Represents a user with basic information.

    Attributes:
        Inherits attributes from Basic_data.

    Args:
        email (str): User's email address.
        password (str): User's password.
        first_name (str): User's first name.
        last_name (str): User's last name.

    Note:
        Inherits from Basic_data for shared attributes.
    """
    def __init__(self, email, password, first_name, last_name):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name