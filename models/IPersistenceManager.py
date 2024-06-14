#!/usr/bin/python3

from abc import ABC, abstractmethod

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
       def update(self, instance, instance_type):
           pass

       @abstractmethod
       def delete(self, instance_id, instance_type):
           pass
