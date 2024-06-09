#!/usr/bin/python3

from flask import Blueprint

country_bp = Blueprint('country', __name__)

@country_bp.route('/', methods=['GET'])
def get_countries():
    pass

@country_bp.route('/<string:country_code>', methods=['GET'])
def get_country(country_code):
    pass

@country_bp.route('/<string:country_code>/cities', methods=['GET'])
def get_country_cities(country_code):
    pass

@country_bp.route('/cities', methods=['POST'])
def create_city():
    pass

@country_bp.route('/cities', methods=['GET'])
def get_cities():
    pass

@country_bp.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    pass

@country_bp.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    pass

@country_bp.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    pass
