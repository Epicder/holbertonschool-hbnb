#!/usr/bin/python3

from abc import ABC
import uuid
from datetime import datetime
from persistence_layer import DataManager

data_manager = DataManager()

class Basic_data(ABC):
    def __init__(self):
        self._id = uuid.uuid4()
        self._created_at = datetime.now()
        self._updated_at = datetime.now()

class Users(Basic_data):
    def __init__(self, email, password, first_name, last_name):
        super().__init__()
        self._email = email
        self._password = password
        self._first_name = first_name
        self._last_name = last_name

class Reviews(Basic_data):
    def __init__(self, rating, user_id, place_id, comment):
        super().__init__()
        self._rating = rating
        self._user_id = user_id
        self._place_id = place_id
        self._comment = comment

class Place(Basic_data):
    def __init__(self, host_id, name, description, rooms, bathrooms,\
                max_guests, price_per_night, latitude, longitude, city_id):# Falta el dato que le pasamos al amenity 
        super().__init__()
        self._host_id = host_id
        self._name = name
        self._description = description
        self._rooms = rooms
        self._bathroom = bathrooms
        self._max_guests = max_guests
        self._price_per_night = price_per_night
        self._latitude = latitude
        self._longitude = longitude
        self._city_id = city_id
        self._amenities_list = #falta el dato, e implemantear en create amenity

class Country:
    def __init__(self, code, name):
        self._code = code
        self._name = name

class City(Basic_data):
    def __init__(self, name, country_code):
        super().__init__()
        self._name = name
        self._county_code = country_code

class Amenities:
    def __init__(self, name):
        self._id = uuid.uuid4()
        self._name = name

class System:

    def create_review(data_reviwe):
        try:
            new_review = Reviews(
                user_id = data_reviwe.get('user_id'),
                place_id = data_reviwe.get('place_id'),
                comment = data_reviwe.get('comment'),
                rating = data_reviwe.get('rating')
            )
            place = data_manager.get(new_review._place_id, Place) # Cambio aca
            if place and place.host_id == new_review._user_id:
                raise ValueError("User cannot review their own place")
            if new_review.rating <= 0:
                raise ValueError("Rating must be a number from 1 to 5")
            if new_review.comment == "":
                raise TypeError("A comment must be written")
            print("Thank you for your review!")
        except Exception:
            print("An error has occured, please try again!")
        return new_review

    def create_place(data_place):

        try:
            new_plance = Place(
                name = data_place.get('name'),
                host_id = data_place.get('host_id'),
                description = data_place.get('description'),
                rooms = data_place.get('rooms'),
                bathroom = int(data_place.get('bathrooms')),
                max_guests = int(data_place.get('max_guests')),
                price_per_night =  float(data_place.get('precie_per_nigth')),
                latitude = float(data_place.get('latitude')),
                longitude = float(data_place.get('longitude')),
                city_id = data_place.get('city_id'),
                amenities_list = data_place.get('amenities_list')
                )
            if new_plance.description == "":
                raise TypeError("The place must have a description!")
            if new_plance.rooms <= 0:
                raise ValueError("The place must have at least one room!")
            if new_plance.bathroom <= 0:
                raise ValueError("The place must have at least one bathroom!")
            if new_plance.max_guests <= 0:
                raise ValueError("The place must have at least one guest!")
            if new_plance.price_per_night <= 0:
                raise ValueError("Price per night must be positive!")
            if not -90 <= new_plance.latitude <= 90:
                raise ValueError("Please enter a latitud between -90 and 90")
            if not -180 <= new_plance.longitude <= 180:
                    raise ValueError("Please enter a longitude between -180 and 180")
        except Exception:
            print("Error creating a place, please try again!")
        return new_plance

    def create_amenities(data_amenities):# Hay que arreglarlo
        try:
            new_amenities = Amenities(
                name_amenity = data_amenities.get('name')
                )
        except Exception:
            print("Error creaing amenities, please try again!")
        return new_amenities

    def create_user(data_user):
        try:
            new_user = Users(
                email = data_user.get('email'),
                password = data_user.get('password'),
                first_name = data_user.get('first_name'),
                last_name = data_user.get('last_name')
                )
            existing_users = data_manager.get_all(Users)
            for user in existing_users:
                if user.email == data_user.get('email'):
                    raise ValueError("Email already exist!")
        except Exception:
            print("Error creating user, please try again")
        return new_user
