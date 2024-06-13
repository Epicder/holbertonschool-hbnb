#!/usr/bin/python3

from abc import ABC
import uuid
from datetime import datetime

class Basic_data(ABC):
    def __init__(self):
        self.id = uuid.uuid4()
        self.id = str(self.id)
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
