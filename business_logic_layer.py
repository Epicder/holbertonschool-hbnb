#!/usr/bin/python3

from abc import ABC
import uuid
from datetime import datetime

class Basic_data(ABC):
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class Users(Basic_data):
    def __init__(self, id, created_at, updated_at, email, password, first_name, last_name):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

class Reviews(Basic_data):
    def __init__(self, id, created_at, updated_at, rating, user_id, place_id, comment):
        super().__init__()
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id
        self.comment = comment

class Place(Basic_data):
    def __init__(self, id, created_at, updated_at, host_id, name, description, rooms, bathrooms,\
                max_guests, price_per_night, latitude, longitude, city_id, amenities_list):
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

class Country:
    def __init__(self, code, name):
        self.code = code
        self.name = name

class City(Basic_data):
    def __init__(self, id, created_at, updated_at, name, country_code):
        super().__init__()
        self.name = name
        self.county_code = country_code

class Amenities:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name

class System:

    def create_review(data_reviwe):
        try:
            new_review = Reviews(
                new_review.user_id = data_reviwe.get('user_id')
                new_review.place_id = data_reviwe.get('place_id')
                new_review.comment = data_reviwe.get('comment')
                new_review.rating = data_reviwe.get('rating')
            )
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
                new_plance.name = data_place.get('name')
                new_plance.host_id = data_place.get('host_id')
                new_plance.description = data_place.get('description')
                new_plance.rooms = data_place.get('rooms')
                new_plance.bathroom = int(data_place.get('bathrooms'))
                new_plance.max_guests = int(data_place.get('max_guests'))
                new_plance.price_per_night =  float(data_place.get('precie_per_nigth'))
                new_plance.latitude = float(data_place.get('latitude'))
                new_plance.longitude = float(data_place.get('longitude'))
                new_plance.city_id = data_place.get('city_id')
                new_plance.amenities_list = data_place.get('amenities_list')
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

    def create_amenities(data_amenities):
        new_amenities = Amenities()
        new_amenities.id = data_amenities.get('id')
        new_amenities = data_amenities.get('name')

        return new_amenities

    def create_user(data_user):
        new_user = Users()
        new_user.email = data_user.get('email')
        new_user.password = data_user.get('password')
        new_user.first_name = data_user.get('first_name')
        new_user.last_name = data_user.get('last_name')

        return new_user


    """
    def create_review(user_id, place_id):
        new_review = Reviews()
        new_review.user_id = user_id
        new_review.place_id = place_id
        new_review.comment = input("Leave a review of the place: ")
        while True:
            try:
                new_review.rating = int(input("Leave a rating between 1 and 5: "))
                if 1 <= new_review.rating <= 5:
                    break
            except ValueError:
                print("Please enter a rating between 1 and 5")
        print("Thank you for your review!")
        return new_review

    def create_place(host_id, city_id, amenities_list):
        new_plance = Place()
        new_plance.city_id = city_id
        new_plance.name = input("Select a name for your place: ")
        new_plance.description = input("Description of the place: ")
        while True:
            try:
                new_plance.rooms = int(input("Number of rooms: "))
                if new_plance.rooms > 0:
                    break
            except ValueError:
                print("Please enter a positive number")
        while True:
            try:
                new_plance.bathroom = int(input("Number of bathrooms: "))
                if new_plance.bathroom > 0:
                    break
            except ValueError:
                print("Please enter a valid number")
        while True:
            try:
                new_plance.max_guests = int(input("Max guests?: "))
                if new_plance.max_guests > 0:
                    break
            except ValueError:
                print("Please enter a valid number")
        while True:
            try:
                new_plance.price_per_night = float(input("Price per night?: "))
                if new_plance.price_per_night > 0:
                    break
            except ValueError:
                print("Please enter a valid price")
        while True:
            try:
                new_plance.latitude = float(input("Latitude?: "))
                if -90 <= new_plance.latitude <= 90:
                    break
            except ValueError:
                print("Please enter a latitud between -90 and 90")
        while True:
            try:
                new_plance.longitude = float(input("Longitude?: "))
                if -180 <= new_plance.longitude <= 180:
                    break
            except ValueError:
                print("Please enter a longitude between -180 and 180")

        pass  ## Falta Agregar el sistema de amenities, el que las crea y luego como agregarlas aca.
    """
~                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ~                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ~                                                                                                                                     
