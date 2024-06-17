#!/usr/bin/python3

from flask import jsonify
from models.reviews import Reviews
from models.users import Users
from models.place import Place
from models.amenities import Amenities
from models.city import City
from p_layer import D_manager


class System:
    """
    A class representing the main system operations.
    """

    def create_review(place_id, data_review):
        """
        Create a new review for a place.

        Args:
            place_id (int): The ID of the place being reviewed.
            data_review (dict): Review data including 'user_id', 'comment', and 'rating'.

        Returns:
            Flask Response: JSON response indicating success or failure.

        Raises:
            ValueError: If user tries to review their own place or attempts multiple reviews on the same place.
        """
        try:
            new_review = Reviews(
                user_id=data_review.get('user_id'),
                place_id=place_id,
                comment=data_review.get('comment'),
                rating=data_review.get('rating')
            )
        except Exception:
            return jsonify({"Message": "Failed to create review."}), 400
        
        place = D_manager.get(place_id, Place)
        if place and place.get('host_id') == new_review.user_id:
            raise ValueError("User cannot review their own place")
        
        existing_review = D_manager.get_all(new_review)
        for review in existing_review:
            if new_review.user_id not in review.get('user_id'):
                raise ValueError("User not found!")
            if new_review.user_id in review.get('id') and place_id in review.get('place_id'):
                raise ValueError("User cannot review multiple times on the same place")
        
        existing_place = D_manager.get_all('Place')
        for place in existing_place:
            if new_review.place_id not in place.get('id'):
                raise ValueError("Place not found!")

        D_manager.save(new_review)

    def create_place(data_place):
        """
        Create a new place.

        Args:
            data_place (dict): Place data including 'name', 'host_id', 'description', etc.

        Returns:
            Flask Response: JSON response indicating success or failure.
        """
        try:
            new_place = Place(
                name=data_place.get('name'),
                host_id=data_place.get('host_id'),
                description=data_place.get('description'),
                rooms=data_place.get('rooms'),
                bathrooms=int(data_place.get('bathrooms')),
                max_guests=int(data_place.get('max_guests')),
                price_per_night=float(data_place.get('price_per_night')),
                latitude=float(data_place.get('latitude')),
                longitude=float(data_place.get('longitude')),
                city_id=data_place.get('city_id'),
                amenity_ids=data_place.get('amenities_ids')
            )
        except Exception:
            return jsonify({"Message": "Failed to create Place."}), 400
        
        D_manager.save(new_place)

    def create_amenities(data_amenities):
        """
        Create a new amenity.

        Args:
            data_amenities (dict): Amenity data including 'name'.

        Returns:
            Flask Response: JSON response indicating success or failure.
        """
        try:
            new_amenity = Amenities(
                name=data_amenities.get('name')
            )
        except Exception:
            return jsonify({"Message": "Failed to create Amenity."}), 400
        
        D_manager.save(new_amenity)

    def create_user(data_user):
        """
        Create a new user.

        Args:
            data_user (dict): User data including 'email', 'password', 'first_name', and 'last_name'.

        Returns:
            Flask Response: JSON response indicating success or failure.

        Raises:
            ValueError: If the email already exists in the system.
        """
        try:
            new_user = Users(
                email=data_user.get('email'),
                password=data_user.get('password'),
                first_name=data_user.get('first_name'),
                last_name=data_user.get('last_name')
            )
        except Exception:
            return jsonify({"Message": "Failed to create User."}), 400
        
        existing_users = D_manager.get_all(new_user)
        for user in existing_users:
            if user.get('email') == data_user.get('email'):
                raise ValueError("Email already exists!")
            
        D_manager.save(new_user)
    
    def create_city(data_city):
        """
        Create a new city.

        Args:
            data_city (dict): City data including 'name' and 'country_code'.

        Returns:
            Flask Response: JSON response indicating success or failure.

        Raises:
            ValueError: If the specified country code does not exist.
        """
        try:
            new_city = City(
                name=data_city.get('name'),
                country_code=data_city.get('country_code')
            )
        except Exception:
            return jsonify({"Message": "Failed to create City."}), 400
        
        countries = D_manager.get_all_country()
        country_found = False
        for country in countries:
            if country.get("alpha-2") == new_city.country_code:
                country_found = True
                break
        
        if not country_found:
            raise ValueError("Country does not exist!")
        
        try:
            D_manager.save(new_city)
            return jsonify({"Message": "City successfully created."}), 201
        except Exception:
            return jsonify({"Message": "Failed to create City."}), 400

    def update(entity_id, entity, entity_type):
        """
        Update an entity.

        Args:
            entity_id (int): The ID of the entity to update.
            entity (object): The entity object to update.
            entity_type (str): The type of entity (e.g., 'Place', 'User').

        Returns:
            None
        """
        D_manager.update(entity_id, entity, entity_type)
    
    def delete(entity_id, entity_type): 
        """
        Delete an entity.

        Args:
            entity_id (int): The ID of the entity to delete.
            entity_type (str): The type of entity (e.g., 'Place', 'User').

        Returns:
            None
        """
        D_manager.get(entity_id, entity_type)
        D_manager.delete(entity_id, entity_type)
    
    def get(entity_id, entity_type):
        """
        Retrieve an entity by ID.

        Args:
            entity_id (int): The ID of the entity to retrieve.
            entity_type (str): The type of entity (e.g., 'Place', 'User').

        Returns:
            object: The retrieved entity object.
        """
        return D_manager.get(entity_id, entity_type)
    
    def get_all(entity_type):
        """
        Retrieve all entities of a given type.

        Args:
            entity_type (str): The type of entity (e.g., 'Place', 'User').

        Returns:
            list: A list of all entities of the specified type.
        """
        return D_manager.get_all(entity_type)
    
    def get_all_countries():
        """
        Retrieve all countries.

        Returns:
            list: A list of dictionaries representing countries.
        """
        return D_manager.get_all_country()
    
    def get_country(entity_id):
        """
        Retrieve a country by ID.

        Args:
            entity_id (int): The ID of the country to retrieve.

        Returns:
            dict: The country information.
        """
        return D_manager.get_country(entity_id)
