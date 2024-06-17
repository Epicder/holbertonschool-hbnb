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
    pass

@amenity_bp.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    pass
@amenity_bp.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    pass
@amenity_bp.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    pass
