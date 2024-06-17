#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from b_logic.system import System
from p_layer.DataManager import DataManager

place_bp = Blueprint('place', __name__)
D_manager = DataManager()


@place_bp.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    amenity = System.get_all('Amenities')
    for amenity_id in data.get('amenity_ids', []):
        amenity_found = False
        for amenity in amenity:
            if amenity.id == amenity_id:
                amenity_found = True
                break
        if data.get('amenity_ids') not in amenity:
            raise ValueError("Amenity not found!")
    if data.get('description') == "":
        raise TypeError("The place must have a description!")
    if data.get('rooms') <= 0:
        raise ValueError("The place must have at least one room!")
    if data.get('bathrooms') <= 0:
        raise ValueError("The place must have at least one bathroom!")
    if data.get('max_guests') <= 0:
        raise ValueError("The place must have at least one guest!")
    if data.get('price_per_night') <= 0:
        raise ValueError("Price per night must be positive!")
    if not -90 <= data.get('latitude') <= 90:
        raise ValueError("Please enter a latitud between -90 and 90")
    if not -180 <= data.get('longitude') <= 180:
        raise ValueError("Please enter a longitude between -180 and 180")
    try:
        System.create_place(data)
        return jsonify({"Message":"Place successfully created."}), 200
    except Exception as e:
        return jsonify({"Message":"An error creating a place {}".format(e)}), 400


@place_bp.route('/places', methods=['GET'])
def get_places():
    try:
        place = System.get_all('Place')
        return jsonify({"Message":"Successfully retrieved all Places.", "Place":place}), 200
    except:
        return jsonify({"Message":"Places not found."}), 404
    
@place_bp.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    try:
        place = System.get(place_id, 'Place')
        return jsonify({"Message":"Successfully retrieved place", "Place":place}), 200
    except:
        return jsonify({"Message":"Place not found."}), 404

@place_bp.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.get_json()
    try:
        System.update(place_id, data, 'Place')
        return jsonify({"Message":"Place Successfully updated"}), 204
    except:
        return jsonify({"Message": "Place not found"}), 404

@place_bp.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    try:
        place = System.get(place_id, 'Place')
        if place == None:
            return jsonify({"Message":"Place not found."}), 404
        System.delete(place_id, 'Place')
        return jsonify({"Message":"Successfully place deleted."}), 204
    except:
        return jsonify({"Message":"Place not found."}), 404
