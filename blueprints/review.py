#!/usr/bin/python3                                                                                                                                                                                                                                                            
""" Quiza la implementacion de review NO es asi, tengo que ver mas blueprint para saberlo """

from flask import Blueprint

review_bp = Blueprint('review', __name__)

@place_bp.route('/places/<int:place_id>/', methods=['POST'])
def create_place_review(place_id):
    pass

@place_bp.route('/users/<int:user_id>/', methods=['GET'])
def get_user_review(user_id):
    pass

@place_bp.route('/place/<int:place_id>/', methods=['GET'])
def get_place_review(place_id):
    pass

@place_bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id):
    pass

@place_bp.route('/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    pass

@place_bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    pass
