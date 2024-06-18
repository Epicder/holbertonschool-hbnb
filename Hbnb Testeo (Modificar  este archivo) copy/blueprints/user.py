#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from models.users import Users
from b_logic.system import System


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
    try:
        System.create_user(data)
        return jsonify({"Message":"User succsessfuly created."}), 201
    except Exception:
        return jsonify({"Message":"Failed to create User."}), 400
    

@user_bp.route('/users', methods=['GET'])
def get_users():
    try:
        users = System.get_all('Users')
        return jsonify({"Message":"Successfully retrieved  all user.", "Users":users}), 200
    except:
        return jsonify({"Message":"User not found."}), 404

@user_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = System.get(user_id, 'Users')
        return jsonify({"Message":"Successfully retrieved user.", "Users":user}), 200
    except:
        return jsonify({"Message":"User not found."}), 404

@user_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    try:
        System.update(user_id, data, 'Users')
        return jsonify({"Message":"User Successfully updated"}), 200
    except:
        return jsonify({"Message": "User not found"}), 404

@user_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = System.get(user_id, 'Users')
        if user == None:
            return jsonify({"Message":"User not found."}), 404
        System.delete(user_id, 'Users')
        return jsonify({"Message":"Successfully user deleted."}), 204
    except:
        return jsonify({"Message":"User not found."}), 404