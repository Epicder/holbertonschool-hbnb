#!/usr/bin/python3

from models.IPersistenceManager import IPersistenceManager
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
        instance_name = instance.__class__.__name__
        if instance_name in self.data_lists:
            self.data_lists[instance_name].append(instance.__dict__)
        try:
            with open('data_base.json', mode='w', encoding="utf-8") as file:
                file.write(json.dumps(self.data_lists))
        except FileNotFoundError:
            return ("File not found"), 404

        else:
            print(f"Invalid Object: {instance_name}")
   
    def get(self, instance_id, instance):
        instance_name = instance.__class__.__name__
        if instance_name in self.data_lists:
            instance_list = self.data_lists[instance_name]
            for instance in instance_list:
                if instance.id == instance_id:
                    return instance

            print(f"Invalid id: {instance_id}")
        else:
            print(f"Invalid Object: {instance_name}")
    
    def get_all(self, instance_type):
        instance_name = instance_type.__class__.__name__
        if instance_name in self.data_lists:
            return self.data_lists[instance_name]
        else:
            return print(f"Invalid Object: {instance_name}")
    
    def delete(self, instance_id, instance):
        instance_name = instance.__class__.__name__
        if instance_name in self.data_lists:
            instance_list = self.data_lists[instance_name]
            for instance in instance_list:
                if instance.get('get') == instance_id:
                    self.data_lists[instance_name].remove(instance)
        else:
            print(f"Invalid Objetct: {instance_name}")
        
    
    def update(self, instance):
       instance_name = instance.__class__.__name__
       if instance_name in self.data_lists:
           instance_list = self.data_lists[instance_name]
           for obj_id in instance_list:
               if obj_id.get('id') == instance.get('id'):
                   instance_list[obj_id] = instance
                   self.data_lists[instance_name] = instance_list
                   try:
                        with open('data_base.json', encoding="utf-8") as file:
                            file.write(json.dumps(self.data_lists))
                            return ("File update"), 200
                   except FileNotFoundError:
                       return ("File not found"), 404
       else:
            print(f"Invalid Objetct: {instance_name}")
