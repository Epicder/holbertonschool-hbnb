#!/usr/bin/python3

from flask import Flask, request, jsonify, abort
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
