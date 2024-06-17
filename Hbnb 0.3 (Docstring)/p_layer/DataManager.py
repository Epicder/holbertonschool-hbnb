#!/usr/bin/python3

from flask import jsonify
from models.IPersistenceManager import IPersistenceManager
from datetime import datetime
import json


class DataManager(IPersistenceManager):
    """
    Data manager class for handling persistence operations.

    Attributes:
        data_lists (dict): Dictionary storing lists of different entity types.

    Methods:
        save(entity):
            Saves an entity to the data storage.
        
        get(entity_id, entity_type):
            Retrieves a specific entity by its ID and type.

        get_all(entity_type):
            Retrieves all entities of a specific type.

        delete(entity_id, entity):
            Deletes an entity from the data storage.

        update(entity_id, entity, entity_type):
            Updates an entity in the data storage.

        get_all_country():
            Retrieves all countries from a separate JSON file.

        get_country(entity_id):
            Retrieves a specific country by its alpha-2 code.

    Note:
        Inherits from IPersistenceManager for method signatures.
    """

    def __init__(self):
        """
        Initializes DataManager with an empty data_lists dictionary,
        or loads data from 'data_base.json' if the file exists.
        """
        self.data_lists = {
            'Users': [],
            'Reviews': [],
            'Place': [],
            'Amenities': [],
            'Country': [],
            'City': []
        }
        try:
            with open('data_base.json', encoding="utf-8") as file:
                self.data_lists = json.load(file)
        except FileNotFoundError:
            with open('data_base.json', 'w', encoding="utf-8") as file:
                file.write(json.dumps(self.data_lists))

    def save(self, entity):
        """
        Saves an entity to the data storage.

        Args:
            entity (object): The entity object to be saved.

        Returns:
            Response: JSON response indicating success or failure.

        Raises:
            FileNotFoundError: If 'data_base.json' file is not found.
        """
        class_name = entity.__class__.__name__
        if class_name in self.data_lists:
            self.data_lists[class_name].append(entity.__dict__)
        try:
            with open('data_base.json', 'w', encoding="utf-8") as file:
                file.write(json.dumps(self.data_lists, indent=4))
        except FileNotFoundError:
            return jsonify("File not found"), 404
   
    def get(self, entity_id, entity_type):
        """
        Retrieves a specific entity by its ID and type.

        Args:
            entity_id (str or int): The ID of the entity to retrieve.
            entity_type (str or type): The type (class name) of the entity.

        Returns:
            dict or None: The entity dictionary if found, otherwise None.
        """
        if type(entity_type) is not str:
            class_name = entity_type.__class__.__name__
        else:
            class_name = entity_type
            
        if class_name in self.data_lists:
            entity_list = self.data_lists[class_name]
            for entity in entity_list:
                if entity.get('id') == entity_id:
                    return entity

    def get_all(self, entity_type):
        """
        Retrieves all entities of a specific type.

        Args:
            entity_type (str or type): The type (class name) of the entities.

        Returns:
            list: List of entity dictionaries.
        """
        if type(entity_type) is not str:
            class_name = entity_type.__class__.__name__
        else:
            class_name = entity_type
        if class_name in self.data_lists:
            return self.data_lists[class_name]
    
    def delete(self, entity_id, entity):
        """
        Deletes an entity from the data storage.

        Args:
            entity_id (str or int): The ID of the entity to delete.
            entity (str or type): The type (class name) of the entity.

        Returns:
            Response: JSON response indicating success or failure.

        Raises:
            FileNotFoundError: If 'data_base.json' file is not found.
        """
        if type(entity) is not str:
            class_name = entity.__class__.__name__
        else:
            class_name = entity
        if class_name in self.data_lists:
            entity_list = self.data_lists[class_name]
            for entity in entity_list:
                if entity.get('id') == entity_id:
                    self.data_lists[class_name].remove(entity)
            try:
                with open('data_base.json', 'w', encoding="utf-8") as file:
                    file.write(json.dumps(self.data_lists, indent=4))
            except FileNotFoundError:
                return jsonify("File not found"), 404

    def update(self, entity_id, entity, entity_type):
        """
        Updates an entity in the data storage.

        Args:
            entity_id (str or int): The ID of the entity to update.
            entity (dict): Dictionary containing updated entity data.
            entity_type (str): The type (class name) of the entity.

        Returns:
            Response: JSON response indicating success or failure.

        Raises:
            FileNotFoundError: If 'data_base.json' file is not found.
        """
        if entity_type in self.data_lists:
            entity_list = self.data_lists[entity_type]
            for item in entity_list:
                if entity_id == item.get('id'):
                    item['updated_at'] = datetime.now().isoformat()
                    for key, value in entity.items():
                        item[key] = value
                    break
            try:
                with open('data_base.json', 'w', encoding="utf-8") as file:
                    file.write(json.dumps(self.data_lists, indent=4))
            except FileNotFoundError:
                return jsonify("File not found"), 404

    def get_all_country(self):
        """
        Retrieves all countries from 'all_countries.json' file.

        Returns:
            list: List of country dictionaries.

        Raises:
            FileNotFoundError: If 'all_countries.json' file is not found.
        """
        try:
            with open('all_countries.json', encoding="utf-8") as file:
                countries = json.load(file)
        except FileNotFoundError:
                return jsonify("File not found"), 404
        return countries
    
    def get_country(self, entity_id):
        """
        Retrieves a specific country by its alpha-2 code.

        Args:
            entity_id (str): Alpha-2 code of the country to retrieve.

        Returns:
            dict or None: Country dictionary if found, otherwise None.
        """
        countries = DataManager.get_all_country()
        for country in countries:
            if country.get("alpha-2") == entity_id:
                return country