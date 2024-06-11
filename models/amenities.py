#!/usr/bin/python3

from basic_data import Basic_data
import uuid

class Amenities:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
