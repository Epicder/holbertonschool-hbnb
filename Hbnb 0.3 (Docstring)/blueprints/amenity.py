#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from b_logic.system import System

amenity_bp = Blueprint('amenity', __name__)


@amenity_bp.route('/amenities', methods=['POST'])
def create_amenity():
    """
    Create a new amenity.

    Returns:
        JSON response with success message and status code.
    """
    data = request.get_json()
    try:
        System.create_amenities(data)
        return jsonify({"Message": "Amenity successfully created."}), 201
    except Exception as e:
        return jsonify({"Message": f"An error creating an Amenity {e}"}), 404

@amenity_bp.route('/amenities', methods=['GET'])
def get_amenities():
    """
    Get all amenities.

    Returns:
        JSON response with success message, list of amenities, and status code.
    """
    try:
        amenity = System.get_all('Amenities')
        return jsonify({"Message": "Successfully retrieved amenities.", "Amenities": amenity}), 200
    except:
        return jsonify({"Message": "Amenity not found."}), 404

@amenity_bp.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """
    Get a specific amenity by ID.

    Args:
        amenity_id (str): The ID of the amenity to retrieve.

    Returns:
        JSON response with success message, the retrieved amenity, and status code.
    """
    try:
        amenity = System.get(amenity_id, 'Amenities')
        return jsonify({"Message": "Successfully retrieved amenity.", "Amenities": amenity}), 200
    except:
        return jsonify({"Message": "Amenity not found."}), 404
    
@amenity_bp.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """
    Update an existing amenity.

    Args:
        amenity_id (str): The ID of the amenity to update.

    Returns:
        JSON response with success message and status code.
    """
    data = request.get_json()
    try:
        System.update(amenity_id, data, 'Amenities')
        return jsonify({"Message": "Amenity Successfully updated"}), 200
    except:
        return jsonify({"Message": "User not found"}), 404
    
@amenity_bp.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    """
    Delete an existing amenity.

    Args:
        amenity_id (str): The ID of the amenity to delete.

    Returns:
        JSON response with success message and status code.
    """
    try:
        amenity = System.get(amenity_id, 'Amenities')
        if amenity is None:
            return jsonify({"Message": "Amenity not found."}), 404
        System.delete(amenity_id, 'Amenities')
        return jsonify({"Message": "Deleted amenity successfully."}), 204
    except:
        return jsonify({"Message": "Amenity not found."}), 404
