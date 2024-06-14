#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from models.users import Users
from b_logic.system import System
from p_layer import D_manager


user_bp = Blueprint('user', __name__)


@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if "@" not in data.get('email') or ".com" not in data.get('email'):
        raise ValueError("Email, not valid!")
    if not data.get('password'):
        raise ValueError("Password not valid, try a new one!")
    if not data.get('first_name'):
        raise ValueError("First Name not valid, try a new one!")
    if not data.get('last_name'):
        raise ValueError("Last Name not valid, try a new one!")
    System.create_user(data)
    

@user_bp.route('/users', methods=['GET'])
def getall_users():
    return D_manager.get_all("Users")

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user():
    pass

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    pass

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = D_manager.get(user_id, 'User')
    if not user:
        return jsonify({"Message": "User not found"}), 404
    D_manager.delete(user_id, 'User')
    return jsonify({"Message":"User successfully deleted"}), 200
