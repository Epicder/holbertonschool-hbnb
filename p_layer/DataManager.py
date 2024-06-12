#!/usr/bin/python3

from models.IPersistenceManager import IPersistenceManager

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
        
    def save(self, instance):
        instance_name = instance.__class__.__name__
        if instance_name in self.data_lists:
            self.data_lists[instance_name].append(instance.__dict__)
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
                if instance.id == instance_id:
                    self.data_lists[instance_name].remove(instance)
        else:
            print(f"Invalid Objetct: {instance_name}")
        
    
    def update(self, instance):
       instance_name = instance.__class__.__name__
       if instance_name in self.data_lists:
           instance_list = self.data_lists[instance_name]
           for obj_id in instance_list:
               if obj_id.id == instance.id:
                   instance_list[obj_id] = instance
                   self.data_lists[instance_name] = instance_list
                   break
       else:
            print(f"Invalid Objetct: {instance_name}")
