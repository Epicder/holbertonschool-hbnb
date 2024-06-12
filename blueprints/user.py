#!/usr/bin/python3

from flask import Blueprint, request, jsonify, abort
from models.users import Users
from b_logic.system import System
from p_layer.DataManager import DataManager


user_bp = Blueprint('user', __name__)
D_manager = DataManager()

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = System.create_user(data)
    D_manager.save(new_user)
    new_user.id = 123123
    return jsonify({"Message":"User succsessfuly created."}), 201
    

@user_bp.route('/users', methods=['GET'])
def getall_users():
    pass

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
