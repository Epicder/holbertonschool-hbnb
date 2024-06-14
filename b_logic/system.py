#!/usr/bin/python3

from models.reviews import Reviews
from models.users import Users
from models.place import Place
from models.amenities import Amenities
from models.city import City
from p_layer import D_manager


class System:

    def create_review(place_id, data_review):
        try:
            new_review = Reviews(
                user_id = data_review.get('user_id'),
                place_id = place_id,
                comment = data_review.get('comment'),
                rating = data_review.get('rating')
            )
        except Exception:
            print("An error has occured, please try again!")
        place = D_manager.get(place_id, Place)
        if place and place.get('host_id') == new_review.user_id:
            raise ValueError("User cannot review their own place")
        
        #Lo siguiente debe controlarlo la capa de servicios
        #
        #
        #
        if new_review.rating <= 0:
            raise ValueError("Rating must be a number from 1 to 5")
        if new_review.comment == "":
            raise TypeError("A comment must be written")
        print("Thank you for your review!")
        #
        #
        #
        
        return new_review

    def create_place(data_place):
        
        try:
            new_place = Place(
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
                amenity_ids = data_place.get('amenities_ids')
                )
        except Exception:
            print("Error creating a place, please try again!")
        if new_place.amenity_ids not in D_manager.data_lists['Amenities']:
            raise ValueError("Amenity not found!")
        
        #Lo siguiente debe controlarlo la capa de servicios
        #
        #
        #
        if new_place.description == "":
            raise TypeError("The place must have a description!")
        if new_place.rooms <= 0:
            raise ValueError("The place must have at least one room!")
        if new_place.bathroom <= 0:
            raise ValueError("The place must have at least one bathroom!")
        if new_place.max_guests <= 0:
            raise ValueError("The place must have at least one guest!")
        if new_place.price_per_night <= 0:
            raise ValueError("Price per night must be positive!")
        if not -90 <= new_place.latitude <= 90:
            raise ValueError("Please enter a latitud between -90 and 90")
        if not -180 <= new_place.longitude <= 180:
                raise ValueError("Please enter a longitude between -180 and 180")
        #
        #
        #
        return new_place

    def create_amenities(data_amenities):
        try:
            new_amenity = Amenities(
                name_amenity = data_amenities.get('name')
                )
        except Exception:
            print("Error creaing amenities, please try again!")
        D_manager.data_lists['Amenities'].append(new_amenity.__dict__)

    def create_user(data_user):
        try:
            new_user = Users(
                email = data_user.get('email'),
                password = data_user.get('password'),
                first_name = data_user.get('first_name'),
                last_name = data_user.get('last_name')
            )
        except Exception:
            print("Error creating user, please try again")

        existing_users = D_manager.get_all(new_user)
        for user in existing_users:
            if user.get('email') == data_user.get('email'):
                raise ValueError("Email already exist!")
        return new_user
    
    def create_city(data_city):
        try:
            new_city = City(
                name = data_city.get('name'),
                country_code = data_city.get('country_code')
            )
        except Exception:
            print("Error creaing amenities, please try again!")
        D_manager.data_lists['City'].append(new_city.__dict__)
        #
        #
        # Debe llamar al DataManager y guardar desde aca, no desde la service layer