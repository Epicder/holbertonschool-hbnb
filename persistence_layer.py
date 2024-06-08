#!/usr/bin/python3

from abc import ABC, abstractmethod
from business_logic_layer import Users, Reviews, Place, Amenities, Country, City

class IPersistenceManager(ABC):
       @abstractmethod
       def save(self, instance):
           pass

       @abstractmethod
       def get(self, instance_id, instance_type):
           pass
       
       @abstractmethod
       def get_all(self, instance_type):
           pass

       @abstractmethod
       def update(self, instance):
           pass

       @abstractmethod
       def delete(self, instance_id, instance_type):
           pass
       
class DataManager(IPersistenceManager):
    def __init__(self):
        self.data_lists = {
        Users: [],
        Reviews: [],
        Place : [],
        Amenities: [],
        Country: [],
        City: []
        }
        
    def save(self, instance):
        instance_type = type(instance)
        if instance_type in self.data_lists:
            self.data_lists[instance_type].append(instance)
        else:
            print(f"Invalid Object: {instance_type}")
   
    def get(self, instance_id, instance_type):
        if instance_type in self.data_lists:
            instance_list = self.data_lists[instance_type]
            for instance in instance_list:
                if instance.id == instance_id:
                    return instance

            print(f"Invalid id: {instance_id}")
        else:
            print(f"Invalid Object: {instance_type}")
    
    def get_all(self, instance_type):
        if instance_type in self.data_lists:
            return self.data_lists[instance_type]
        else:
            return print(f"Invalid Object: {instance_type}")
    
    def delete(self, instance_id, instance_type):
        if instance_type in self.data_lists:
            instance_list = self.data_lists[instance_type]
            for instance in instance_list:
                if instance.id == instance_id:
                    self.data_lists[instance_type].remove(instance)
        else:
            print(f"Invalid Objetct: {instance_type}")
        
    
    def update(self, instance):
       pass