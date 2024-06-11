#!/usr/bin/python3

from flask import Flask, request, jsonify, abort
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from blueprints.user import user_bp
from blueprints.countries_and_cities import country_bp
from blueprints.place import place_bp
from blueprints.review import review_bp
from blueprints.amenity import amenity_bp

app = Flask(__name__)
auth = HTTPBasicAuth()

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(country_bp, url_prefix='/countries')
app.register_blueprint(place_bp, url_prefix='/places')
app.register_blueprint(review_bp, url_prefix='/reviews')
app.register_blueprint(amenity_bp, url_prefix='/amenities')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
