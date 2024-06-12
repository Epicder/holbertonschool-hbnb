#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from b_logic.system import System
from p_layer import DataManager

amenity_bp = Blueprint('amenity', __name__)
D_manager = DataManager()


@amenity_bp.route('/', methods=['POST'])
def create_amenity():
    data = request.get_json()
    new_amen = System.create_amenities(data)
    D_manager.save(new_amen)
    return jsonify({"Ameniti":"Quedo guardao"}), 201

@amenity_bp.route('/', methods=['GET'])
def get_amenities():
    pass

@amenity_bp.route('/<int:amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    pass
@amenity_bp.route('/<int:amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    pass
@amenity_bp.route('/<int:amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    pass
