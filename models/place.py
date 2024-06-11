#!/usr/bin/python3

from models.basic_data import Basic_data

class Place(Basic_data):
    def __init__(self, host_id, name, description, rooms, bathrooms,\
                max_guests, price_per_night, latitude, longitude, city_id, amenities_list):# Falta el dato que le pasamos al amenity 
        super().__init__()
        self.host_id = host_id
        self.name = name
        self.description = description
        self.rooms = rooms
        self.bathroom = bathrooms
        self.max_guests = max_guests
        self.price_per_night = price_per_night
        self.latitude = latitude
        self.longitude = longitude
        self.city_id = city_id
        self.amenities_list = amenities_list
