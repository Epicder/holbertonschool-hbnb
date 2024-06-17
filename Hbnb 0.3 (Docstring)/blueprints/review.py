#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from b_logic.system import System
from p_layer.DataManager import DataManager

review_bp = Blueprint('review', __name__)
D_manager = DataManager()

@review_bp.route('/places/<place_id>/reviews', methods=['POST'])
def create_place_review(place_id):
    """
    Create a new review for a specific place.

    Args:
        place_id (str): The ID of the place for which the review is being created.

    Returns:
        JSON response with success message and status code.
    """
    data = request.get_json()
    if data.get('rating') <= 0 or data.get('rating') > 5:
        raise ValueError("Rating must be a number from 1 to 5")
    if not data.get('rating'):
        raise ValueError("Rating must be set!")
    if not data.get('comment'):
        raise ValueError("Must write a comment!")
    if not place_id:
        raise ValueError("Must enter a place id")
    try:
        System.create_review(place_id, data)
        return jsonify({"Message": "Review successfully created."}), 200
    except Exception as e:
        return jsonify({"Message": f"An error creating a review {e}"}), 404

@review_bp.route('/users/<user_id>/reviews', methods=['GET'])
def get_user_review(user_id):
    """
    Get all reviews written by a specific user.

    Args:
        user_id (str): The ID of the user whose reviews are being retrieved.

    Returns:
        JSON response with success message, list of user's reviews, and status code.
    """
    try:
        all_reviews = System.get_all('Reviews')
        reviews = [review for review in all_reviews if review['user_id'] == user_id]
        return jsonify({"Message": "Successfully retrieved user reviews.", "Reviews": reviews}), 200
    except Exception as e:
        return jsonify({"Message": f"User not found. {e}"}), 404

@review_bp.route('/place/<place_id>/reviews', methods=['GET'])
def get_place_review(place_id):
    """
    Get all reviews for a specific place.

    Args:
        place_id (str): The ID of the place whose reviews are being retrieved.

    Returns:
        JSON response with success message, list of place's reviews, and status code.
    """
    try:
        all_reviews = System.get_all('Reviews')
        reviews = [review for review in all_reviews if review['place_id'] == place_id]
        return jsonify({"Message": "Successfully retrieved place reviews.", "Reviews": reviews}), 200
    except Exception as e:
        return jsonify({"Message": f"Place not found. {e}"}), 404

@review_bp.route('/review/<review_id>', methods=['GET'])
def get_review(review_id):
    """
    Get a specific review by review ID.

    Args:
        review_id (str): The ID of the review to retrieve.

    Returns:
        JSON response with success message, the retrieved review, and status code.
    """
    try:
        review = System.get(review_id, 'Reviews')
        return jsonify({"Message": "Successfully retrieved review.", "Review": review}), 200
    except Exception as e:
        return jsonify({"Message": f"Review not found. {e}"}), 404

@review_bp.route('/review/<review_id>', methods=['PUT'])
def update_review(review_id):
    """
    Update an existing review.

    Args:
        review_id (str): The ID of the review to update.

    Returns:
        JSON response with success message, updated review details, and status code.
    """
    data = request.get_json()
    try:
        updated_review = System.update(review_id, data, 'Reviews')
        return jsonify({"Message": "Review successfully updated", "Updated Review": updated_review}), 200
    except:
        return jsonify({"Message": "Review not found"}), 404

@review_bp.route('/review/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    """
    Delete an existing review.

    Args:
        review_id (str): The ID of the review to delete.

    Returns:
        JSON response with success message and status code.
    """
    try:
        review = System.get(review_id, 'Reviews')
        if review is None:
            return jsonify({"Message": "Review not found."}), 404
        System.delete(review_id, 'Reviews')
        return jsonify({"Message": "Successfully deleted review."}), 204
    except:
        return jsonify({"Message": "Review not found."}), 404