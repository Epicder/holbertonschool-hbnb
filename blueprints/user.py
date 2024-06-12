#!/usr/bin/python3

from flask import Blueprint, request, jsonify, abort
from models.users import Users
from b_logic.system import System
from p_layer.DataManager import DataManager
import json


user_bp = Blueprint('user', __name__)
D_man = DataManager()

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = System.create_user(data)
    D_man.save(new_user)
    return jsonify(D_man.get_all(new_user))
    

@user_bp.route('/users', methods=['GET'])
def getall_users():
    return "tamoaca"

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user():
    pass

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    pass

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    pass
