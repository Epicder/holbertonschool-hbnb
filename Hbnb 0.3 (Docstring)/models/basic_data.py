#!/usr/bin/python3

from abc import ABC
import uuid
from datetime import datetime

class Basic_data(ABC):
    """
    Abstract base class representing basic data with common attributes.

    Attributes:
        id (str): A unique identifier generated using UUID4.
        created_at (str): ISO formatted timestamp representing the creation time.
        updated_at (str): ISO formatted timestamp representing the last update time.
    """

    def __init__(self):
        """
        Initialize a new instance of Basic_data with default attribute values.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()