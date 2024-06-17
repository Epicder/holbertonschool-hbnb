#!/usr/bin/python3

from models.basic_data import Basic_data


class Place(Basic_data):
    """
    Represents a place with basic information.

    Attributes:
        Inherits attributes from Basic_data.

    Args:
        host_id (int): ID of the host.
        name (str): Name of the place.
        description (str): Description of the place.
        rooms (int): Number of rooms.
        bathrooms (int): Number of bathrooms.
        max_guests (int): Maximum number of guests.
        price_per_night (float): Nightly price.
        latitude (float): Latitude coordinate.
        longitude (float): Longitude coordinate.
        city_id (int): ID of the city.
        amenity_ids (list of int): IDs of amenities.

    Note:
        Inherits from Basic_data for shared attributes.
    """
    def __init__(self, host_id, name, description, rooms, bathrooms,
                 max_guests, price_per_night, latitude, longitude, city_id, amenity_ids):
        super().__init__()
        self.host_id = host_id
        self.name = name
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.max_guests = max_guests
        self.price_per_night = price_per_night
        self.latitude = latitude
        self.longitude = longitude
        self.city_id = city_id
        self.amenity_ids = amenity_ids