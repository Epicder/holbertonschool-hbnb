#!/usr/bin/python3

from flask import Blueprint

user_bp = Blueprint('user', __name__)

def validate_email(email):
    pass

def find_user(user_id):
    pass

@app.route('/users', methods=['POST'])
def create_user():
    pass

@app.route('/users', methods=['GET'])
def get_users():
    pass

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user():
    pass

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    pass

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    pass
