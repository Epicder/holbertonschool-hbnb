#!/usr/bin/python3

from models.basic_data import Basic_data

class City(Basic_data):
    """
    Represents a city with a name and country code.
    """
    def __init__(self, name, country_code):
        """
        Initializes a new City instance.

        Args:
            name (str): The name of the city.
            country_code (str): The country code associated with the city.
        """
        super().__init__()
        self.name = name
        self.county_code = country_code