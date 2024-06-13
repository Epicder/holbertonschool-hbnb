#!/usr/bin/python3

from models.IPersistenceManager import IPersistenceManager
from datetime import datetime
import json

class DataManager(IPersistenceManager):
    def __init__(self):
        self.data_lists = {
        'Users': [],
        'Reviews': [],
        'Place' : [],
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

    def save(self, instance):
        class_name = instance.__class__.__name__
        
        if class_name in self.data_lists:
            self.data_lists[class_name].append(instance.__dict__)
        try:
            with open('data_base.json', mode='w', encoding="utf-8") as file:
                file.write(json.dumps(self.data_lists, indent=4))
        except FileNotFoundError:
            return ("File not found"), 404

        else:
            print(f"Invalid Object: {class_name}")
   
    def get(self, instance_id, instance):
        class_name = instance.__class__.__name__
        if class_name in self.data_lists:
            instance_list = self.data_lists[class_name]
            for instance in instance_list:
                if instance.id == instance_id:
                    instance['created_at'] = datetime.fromisoformat(instance['created_at'])
                    instance['updated_at'] = datetime.fromisoformat(instance['updated_at'])
                    return instance

            print(f"Invalid id: {instance_id}")
        else:
            print(f"Invalid Object: {class_name}")
    
    def get_all(self, instance_type):
        
        if type(instance_type) is not str:
            class_name = instance_type.__class__.__name__
        else:
            class_name = instance_type            

        if class_name in self.data_lists:
            return self.data_lists[class_name]
        else:
            return print(f"Invalid Object: {class_name}")
    
    def delete(self, instance_id, instance):
        class_name = instance.__class__.__name__
        if class_name in self.data_lists:
            instance_list = self.data_lists[class_name]
            for instance in instance_list:
                if instance.get('get') == instance_id:
                    self.data_lists[class_name].remove(instance)
                    try:
                        with open('data_base.json', 'w', encoding="utf-8") as file:
                            file.write(json.dumps(self.data_lists))
                            return ("File update"), 200
                    except FileNotFoundError:
                       return ("File not found"), 404
        else:
            print(f"Invalid Objetct: {class_name}")
        
    
    def update(self, instance):
       class_name = instance.__class__.__name__
       if class_name in self.data_lists:
           instance_list = self.data_lists[class_name]
           for obj_id in instance_list:
               if obj_id.get('id') == instance.get('id'):
                   instance['updated_at'] = datetime.now().isoformat
                   instance_list[obj_id] = instance
                   self.data_lists[class_name] = instance_list
                   try:
                        with open('data_base.json', encoding="utf-8") as file:
                            file.write(json.dumps(self.data_lists))
                            return ("File update"), 200
                   except FileNotFoundError:
                       return ("File not found"), 404
       else:
            print(f"Invalid Objetct: {class_name}")
