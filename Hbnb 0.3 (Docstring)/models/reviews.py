#!/usr/bin/python3

from models.basic_data import Basic_data

class Reviews(Basic_data):
    """
    Represents a review for a place.

    Attributes:
        Inherits attributes from Basic_data.

    Args:
        rating (float): The rating given by the user (1.0 to 5.0).
        user_id (int): ID of the user who submitted the review.
        place_id (int): ID of the place being reviewed.
        comment (str): Optional comment provided by the user.

    Note:
        Inherits from Basic_data for shared attributes.
    """
    def __init__(self, rating, user_id, place_id, comment):
        super().__init__()
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id
        self.comment = comment