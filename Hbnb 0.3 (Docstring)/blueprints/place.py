#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from b_logic.system import System

place_bp = Blueprint('place', __name__)

@place_bp.route('/places', methods=['POST'])
def create_place():
    """
    Create a new place with specified amenities and details.

    Returns:
        JSON response with success message and status code.
    """
    data = request.get_json()
    amenities = System.get_all('Amenities')
    
    # Validate presence of specified amenity IDs in the system
    for amenity_id in data.get('amenity_ids', []):
        amenity_found = False
        for amenity in amenities:
            if amenity.get("id") == amenity_id:
                amenity_found = True
                break
        if not amenity_found:
            raise ValueError("Amenity not found!")
    
    # Validate required fields and conditions for the place
    if data.get('description') == "":
        raise TypeError("The place must have a description!")
    if not data.get('rooms') or data.get('rooms') <= 0:
        raise ValueError("The place must have at least one room!")
    if not data.get('bathrooms') or data.get('bathrooms') <= 0:
        raise ValueError("The place must have at least one bathroom!")
    if not data.get('max_guests') or data.get('max_guests') <= 0:
        raise ValueError("The place must have at least one guest!")
    if not data.get('price_per_night') or data.get('price_per_night') <= 0:
        raise ValueError("Price per night must be positive!")
    if not data.get('latitude') or not -90 <= data.get('latitude') <= 90:
        raise ValueError("Please enter a latitude between -90 and 90")
    if not data.get('longitude') or not -180 <= data.get('longitude') <= 180:
        raise ValueError("Please enter a longitude between -180 and 180")
    
    try:
        System.create_place(data)
        return jsonify({"Message": "Place successfully created."}), 200
    except Exception as e:
        return jsonify({"Message": f"An error creating a place {e}"}), 400


@place_bp.route('/places', methods=['GET'])
def get_places():
    """
    Get all places.

    Returns:
        JSON response with success message, list of places, and status code.
    """
    try:
        places = System.get_all('Place')
        return jsonify({"Message": "Successfully retrieved all Places.", "Places": places}), 200
    except:
        return jsonify({"Message": "Places not found."}), 404
    
@place_bp.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    """
    Get a specific place by place ID.

    Args:
        place_id (str): The ID of the place to retrieve.

    Returns:
        JSON response with success message, the retrieved place, and status code.
    """
    try:
        place = System.get(place_id, 'Place')
        return jsonify({"Message": "Successfully retrieved place", "Place": place}), 200
    except:
        return jsonify({"Message": "Place not found."}), 404

@place_bp.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    """
    Update an existing place.

    Args:
        place_id (str): The ID of the place to update.

    Returns:
        JSON response with success message, updated place details, and status code.
    """
    data = request.get_json()
    try:
        updated_place = System.update(place_id, data, 'Place')
        return jsonify({"Message": "Place successfully updated", "Updated Place": updated_place}), 200
    except:
        return jsonify({"Message": "Place not found"}), 404

@place_bp.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    """
    Delete an existing place.

    Args:
        place_id (str): The ID of the place to delete.

    Returns:
        JSON response with success message and status code.
    """
    try:
        place = System.get(place_id, 'Place')
        if place is None:
            return jsonify({"Message": "Place not found."}), 404
        System.delete(place_id, 'Place')
        return jsonify({"Message": "Successfully deleted place."}), 204
    except:
        return jsonify({"Message": "Place not found."}), 404