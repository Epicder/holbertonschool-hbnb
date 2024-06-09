#!/usr/bin/python3

from flask import Blueprint

place_bp = Blueprint('place', __name__)

@place_bp.route('/', methods=['POST'])
def create_place():
    pass

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
