#!/usr/bin/python3                                                                                                                                                                                                                                                           


from flask import Blueprint, request, jsonify
from b_logic.system import System
from p_layer.DataManager import DataManager

review_bp = Blueprint('review', __name__)
D_manager = DataManager()

@review_bp.route('/places/<place_id>/reviews', methods=['POST'])
def create_place_review(place_id):
    data = request.get_json()
    if data.get('rating') <= 0 or data.get('rating') > 5:
        raise ValueError("Rating must be a number from 1 to 5")
    if not data.get('rating'):
        raise ValueError("Rating must be setted!")
    if not data.get('comment'):
        raise ValueError("Must write a coment!")
    if not place_id:
        raise ValueError("Must enter a place id")
    try:
        System.create_review(place_id, data)
        return jsonify({"Message":"Review successfully created."}), 200
    except Exception as e:
        return jsonify({f"Message":"An error creating a review {e}"}), 404

@review_bp.route('/users/<user_id>/reviews', methods=['GET'])
def get_user_review(user_id):
    try:
        reviews = System.get_all(user_id, 'reviews')
        return jsonify({"Message":"Successfully retrieved review.", "Reviews":reviews}), 200
    except:
        return jsonify({"Message":"User not found."}), 404

@review_bp.route('/place/<place_id>/reviews', methods=['GET'])
def get_place_review(place_id):
    try:
        reviews = System.get(place_id, 'reviews')
        return jsonify({"Message":"Successfully retrieved review.", "Reviews":reviews}), 200
    except:
        return jsonify({"Message":"User not found."}), 404

@review_bp.route('/review/<review_id>', methods=['GET'])
def get_review(review_id):
    try:
        reviews = System.get(review_id, 'reviews')
        return jsonify({"Message":"Successfully retrieved review.", "Reviews":reviews}), 200
    except:
        return jsonify({"Message":"User not found."}), 404

@review_bp.route('/review/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    try:
        review = System.update(review_id, data, 'Reviews')
        return jsonify({"Message":"Review Successfully updated", "Reviews":review}), 204
    except:
        return jsonify({"Message": "Review not found"}), 404

@review_bp.route('/review/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    try:
        review = System.get(review_id, 'Reviews')
        if review == None:
            return jsonify({"Message":"Review not found."}), 404
        System.delete(review_id, 'Reviews')
        return jsonify({"Message":"Successfully review deleted."}), 204
    except:
        return jsonify({"Message":"Review not found."}), 404
