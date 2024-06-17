#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from b_logic.system import System

country_bp = Blueprint('country', __name__)

@country_bp.route('/countries', methods=['GET'])
def get_countries():
    """
    Get all countries.

    Returns:
        JSON response with success message, list of countries, and status code.
    """
    try:
        countries = System.get_all_countries()
        return jsonify({"Message": "Successfully retrieved all Countries.", "Countries": countries}), 200
    except:
        return jsonify({"Message": "Countries not found."}), 404

@country_bp.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    """
    Get a specific country by country code.

    Args:
        country_code (str): The code of the country to retrieve.

    Returns:
        JSON response with success message, the retrieved country, and status code.
    """
    if not country_code:
        raise ValueError("Code not valid!")
    try:
        country = System.get_country(country_code)
        return jsonify({"Message": "Successfully retrieved Country", "Country": country}), 200
    except:
        return jsonify({"Message": "Country not found."}), 404

@country_bp.route('/countries/<country_code>/cities', methods=['GET'])
def get_country_cities(country_code):
    """
    Get all cities belonging to a specific country.

    Args:
        country_code (str): The code of the country to retrieve cities for.

    Returns:
        JSON response with success message, the country code, list of cities, and status code.
    """
    try:
        cities = System.get_all('City')
        city_list = [city for city in cities if city.get("country_code") == country_code]
        if not city_list:
            raise ValueError(f"There are no cities from {country_code} country")
        return jsonify({"Message": "Successfully retrieved all cities", "Country": country_code, "Cities": city_list}), 200
    except:
        return jsonify({"Message": "Cities not found."}), 404

@country_bp.route('/cities', methods=['POST'])
def create_city():
    """
    Create a new city.

    Returns:
        JSON response with success message and status code.
    """
    data = request.get_json()
    if not data.get("name"):
        raise ValueError("Name not valid!")
    if not data.get("country_code"):
        raise ValueError("Country code not valid!")
    try:
        System.create_city(data)
        return jsonify({"Message": "City successfully created."}), 201
    except Exception:
        return jsonify({"Message": "Failed to create City."}), 400

@country_bp.route('/cities', methods=['GET'])
def get_cities():
    """
    Get all cities.

    Returns:
        JSON response with success message, list of cities, and status code.
    """
    try:
        cities = System.get_all('City')
        return jsonify({"Message": "Successfully retrieved all cities.", "Cities": cities}), 200
    except:
        return jsonify({"Message": "Cities not found."}), 404

@country_bp.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """
    Get a specific city by city ID.

    Args:
        city_id (str): The ID of the city to retrieve.

    Returns:
        JSON response with success message, the retrieved city, and status code.
    """
    if not city_id:
        raise ValueError("ID not valid!")
    try:
        city = System.get(city_id, 'City')
        return jsonify({"Message": "Successfully retrieved city.", "City": city}), 200
    except:
        return jsonify({"Message": "City not found."}), 404

@country_bp.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """
    Update an existing city.

    Args:
        city_id (str): The ID of the city to update.

    Returns:
        JSON response with success message and status code.
    """
    data = request.get_json()
    if not data.get("name"):
        raise ValueError("Name not valid!")
    if not data.get("country_code"):
        raise ValueError("Country code not valid!")
    if not city_id:
        raise ValueError("ID not valid!")
    try:
        System.update(city_id, data, 'City')
        return jsonify({"Message": "City successfully updated"}), 200
    except:
        return jsonify({"Message": "City not found"}), 404

@country_bp.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """
    Delete an existing city.

    Args:
        city_id (str): The ID of the city to delete.

    Returns:
        JSON response with success message and status code.
    """
    if not city_id:
        raise ValueError("ID not valid!")
    try:
        city = System.get(city_id, 'City')
        if city is None:
            return jsonify({"Message": "City not found."}), 404
        System.delete(city_id, 'City')
        return jsonify({"Message": "Successfully deleted City."}), 204
    except:
        return jsonify({"Message": "City not found."}), 404