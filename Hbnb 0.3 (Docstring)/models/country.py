#!/usr/bin/python3

class Country:
    """
    Represents a country with a code and name.
    """
    def __init__(self, code, name):
        """
        Initializes a new Country instance.

        Args:
            code (str): The country code.
            name (str): The name of the country.
        """
        self.code = code
        self.name = name