#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from models.users import Users
from b_logic.system import System

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user with the provided data.

    Returns:
        JSON response with success message and status code.
    """
    data = request.get_json()
    if "@" not in data.get('email') or ".com" not in data.get('email'):
        raise ValueError("Email is not valid!")
    if not data.get('password'):
        raise ValueError("Password is not valid, please try a new one!")
    if not data.get('first_name'):
        raise ValueError("First Name is not valid, please try a new one!")
    if not data.get('last_name'):
        raise ValueError("Last Name is not valid, please try a new one!")
    try:
        System.create_user(data)
        return jsonify({"Message": "User successfully created."}), 201
    except Exception:
        return jsonify({"Message": "Failed to create User."}), 400

@user_bp.route('/users', methods=['GET'])
def get_users():
    """
    Get all users.

    Returns:
        JSON response with success message, list of users, and status code.
    """
    try:
        users = System.get_all('Users')
        return jsonify({"Message": "Successfully retrieved all users.", "Users": users}), 200
    except:
        return jsonify({"Message": "Users not found."}), 404

@user_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get a specific user by user ID.

    Args:
        user_id (str): The ID of the user to retrieve.

    Returns:
        JSON response with success message, the retrieved user, and status code.
    """
    try:
        user = System.get(user_id, 'Users')
        return jsonify({"Message": "Successfully retrieved user.", "User": user}), 200
    except:
        return jsonify({"Message": "User not found."}), 404

@user_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update an existing user.

    Args:
        user_id (str): The ID of the user to update.

    Returns:
        JSON response with success message and status code.
    """
    data = request.get_json()
    try:
        System.update(user_id, data, 'Users')
        return jsonify({"Message": "User successfully updated"}), 200
    except:
        return jsonify({"Message": "User not found"}), 404

@user_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete an existing user.

    Args:
        user_id (str): The ID of the user to delete.

    Returns:
        JSON response with success message and status code.
    """
    try:
        user = System.get(user_id, 'Users')
        if user is None:
            return jsonify({"Message": "User not found."}), 404
        System.delete(user_id, 'Users')
        return jsonify({"Message": "Successfully deleted user."}), 204
    except:
        return jsonify({"Message": "User not found."}), 404