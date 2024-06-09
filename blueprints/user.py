#!/usr/bin/python3

from flask import Blueprint

user_bp = Blueprint('user', __name__)

def validate_email(email):
    pass

def find_user(user_id):
    pass

@user_bp.route('/users', methods=['POST'])
def create_user():
    pass

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
