#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from b_logic.system import System
from p_layer import DataManager

place_bp = Blueprint('place', __name__)
D_manager = DataManager()


@place_bp.route('/', methods=['POST'])
def create_place():
    data = request.get_json()
    new_place = System.create_place(data)
    D_manager.save(new_place)
    return jsonify({"Elpleis":"Quedo guardao"}), 201

@place_bp.route('/', methods=['GET'])
def get_places():
    pass
@place_bp.route('/<int:place_id>', methods=['GET'])
def get_place(place_id):
    pass

@place_bp.route('/<int:place_id>', methods=['PUT'])
def update_place(place_id):
    pass

@place_bp.route('/<int:place_id>', methods=['DELETE'])
def delete_place(place_id):
    pass
