"""
Author: Shaoshuai Li
Description: Bouquet class defines types of bouquets, their ingredient requirements, and time to prepare.
"""

class Bouquet:
    """Defines a type of bouquet with ingredient requirements and preparation time."""
    types = {
        "Fern-tastic": {
            "Greenery": 4, "Roses": 0, "Daises": 2, "prep_time": 20, "price": 15.5, "demand": 175
        },
        "Be-Leaf in Yourself": {
            "Greenery": 2, "Roses": 1, "Daises": 3, "prep_time": 30, "price": 11.75, "demand": 100
        },
        "You Rose to the Occasion": {
            "Greenery": 2, "Roses": 4, "Daises": 2, "prep_time": 45, "price": 22.5, "demand": 250
        }
    }
