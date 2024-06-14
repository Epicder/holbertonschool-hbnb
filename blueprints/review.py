#!/usr/bin/python3                                                                                                                                                                                                                                                           


from flask import Blueprint, request, jsonify
from b_logic.system import System
from p_layer.DataManager import DataManager

review_bp = Blueprint('review', __name__)
D_manager = DataManager()

@review_bp.route('/places/<int:place_id>/reviews', methods=['POST'])
def create_place_review(place_id):
    data = request.get_json()
    if new_review.rating <= 0 or new_review.rating > 5:
        raise ValueError("Rating must be a number from 1 to 5")
    if not data.get('rating'):
        raise ValueError("Rating must be setted!")
    if not data.get('comment'):
        raise ValueError("Must write a coment!")
    if not place_id:
        raise ValueError("Must enter a place id")
    
    
    print("Thank you for your review!")

    new_review = System.create_review(place_id, data)
    D_manager.save(new_review)
    return jsonify({"Message":"Review successfully created."}), 201

@review_bp.route('/users/<int:user_id>/reviews', methods=['GET'])
def get_user_review(user_id):
    pass

@review_bp.route('/place/<int:place_id>/reviews', methods=['GET'])
def get_place_review(place_id):
    pass

@review_bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id):
    pass

@review_bp.route('/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    pass

@review_bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    pass
