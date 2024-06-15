#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from b_logic.system import System
from p_layer.DataManager import DataManager

place_bp = Blueprint('place', __name__)
D_manager = DataManager()


@place_bp.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    System.create_place(data)

           # if new_place.description == "":
           # raise TypeError("The place must have a description!")
       # if new_place.rooms <= 0:
          #  raise ValueError("The place must have at least one room!")
       # if new_place.bathroom <= 0:
         #   raise ValueError("The place must have at least one bathroom!")
       # if new_place.max_guests <= 0:
         #   raise ValueError("The place must have at least one guest!")
      #  if new_place.price_per_night <= 0:
         #   raise ValueError("Price per night must be positive!")
       # if not -90 <= new_place.latitude <= 90:
          #  raise ValueError("Please enter a latitud between -90 and 90")
       # if not -180 <= new_place.longitude <= 180:
              #  raise ValueError("Please enter a longitude between -180 and 180")

@place_bp.route('/places', methods=['GET'])
def get_places():
    pass
@place_bp.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    pass

@place_bp.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    pass

@place_bp.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    pass
