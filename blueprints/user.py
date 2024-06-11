#!/usr/bin/python3

from flask import Blueprint, request, jsonify, abort
#from persistence_layer import DataManager
from business_logic_layer import Users, System
import json


user_bp = Blueprint('user', __name__)


@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    data_user = json.loads(data)
    new_user = User()
    new_user = System.create_user(data_user)
    
  

@user_bp.route('/users', methods=['GET'])
def get_users():
    pass

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user():
    pass

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    pass

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    pass
