#!/usr/bin/python3

import ABC
import uuid
from datetime import datetime

class Basic_data(ABC):
    def __init__(self):
        self.id = id
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class Users(Basic_data):
    def __init__(self, email, password, first_name, last_name):
        super.__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        

class Reviews(Basic_data):
    def __init__(self, rating, comment):
        super.__init__()
        self.rating = rating
        self.comment = comment

class Place(Basic_data):
    def __init__(self, host_id, name, description, rooms, bathrooms, max_guests, price_per_night, latitude, longitude, city_id, ammenities_dict):
        super.__init__()
        self.host_id = self.host_id
        self.name = self.name
        self.description = description
        self.romms = rooms
        self.bathroom = bathrooms
        self.max_guests = max_guests
        self.price_per_night = price_per_night
        self.latitude = latitude
        self.longitude = longitue
        self.city_id = city_id
        self.amenities_dict = amenities_dict

class Country:
    def __init__(self, code, name):
        self.code = code
        self.code = name

class City(BasicData):
    def __init__(self, name, country_code):
        super.__init__()
        self.name = name
        self.county_code = country_code
        

class System:
    def __init__(self)
