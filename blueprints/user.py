#!/usr/bin/python3

from flask import Blueprint, request, jsonify, abort
from persistence_layer import DataManager
from business_logic_layer import Users

user_bp = Blueprint('user', __name__)
persistence_layer = DataManager()


@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('first_name') or not data.get('last_name'):
        abort(400, description="You must have all fields filled")

    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']
    password = data['password']

    all_users = persistence_layer.get_all(Users)
    if any(user._email == email for user in all_users):
        abort(409, description="Email already exists")
    
    new_user = Users(email, password, first_name, last_name)
    persistence_layer.save(new_user)
    
    return jsonify(new_user), 201
    

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
