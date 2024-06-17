#!/usr/bin/python3

from models.basic_data import Basic_data
import uuid

class Amenities:
    """
    Class representing amenities.

    Attributes:
        id (str): A unique identifier generated using UUID4.
        name (str): The name of the amenity.
    """

    def __init__(self, name):
        """
        Initialize a new instance of Amenities.

        Args:
            name (str): The name of the amenity.
        """
        self.id = str(uuid.uuid4())
        self.name = name