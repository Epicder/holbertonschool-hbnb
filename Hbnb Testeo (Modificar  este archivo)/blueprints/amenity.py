#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from b_logic.system import System
from p_layer.DataManager import DataManager

amenity_bp = Blueprint('amenity', __name__)
D_manager = DataManager()


@amenity_bp.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.get_json()
    try:
        System.create_amenities(data)
        return jsonify({"Message":"Amenity successfully created."}), 201
    except Exception as e:
        return jsonify({f"Message":"An error creating an Amenity {e}"}), 404

@amenity_bp.route('/amenities', methods=['GET'])
def get_amenities():
    try:
        amenity = System.get_all('Amenities')
        return jsonify({"Message":"Successfully retrieved amenities.", "Amenities":amenity}), 200
    except:
        return jsonify({"Message":"Amenity not found."}), 404

@amenity_bp.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    try:
        amenity = System.get(amenity_id, 'Amenities')
        return jsonify({"Message":"Successfully retrieved amenity.", "Amenities":amenity}), 200
    except:
        return jsonify({"Message":"User not found."}), 404
    
@amenity_bp.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    try:
        System.update(amenity_id, data, 'Amenities')
        return jsonify({"Message":"Amenity Successfully updated"}), 200
    except:
        return jsonify({"Message": "User not found"}), 404
    
@amenity_bp.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    try:
        amenity = System.get(amenity_id, 'Amenities')
        if amenity == None:
            return jsonify({"Message":"Amenity not found."}), 404
        System.delete(amenity_id, 'Amenities')
        return jsonify({"Message":"Deleted amenity succesfully."}), 200
    except:
        return jsonify({"Message":"Amenity not found."}), 404