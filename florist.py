# florist.py
"""
Author: Shaoshuai Li
Description: Florist class records information of each florist.
"""

class Florist:
    """
    Represents a florist working at the shop.
    """
    HOURLY_RATE = 17.5
    MONTHLY_HOURS = 80

    def __init__(self, name, speciality=None):
        """
        :param name: Florist's name.
        :param speciality: The bouquet type the florist specialises in (optional).
        """
        self.name = name
        self.speciality = speciality

    def __repr__(self):
        return f"{self.name}" + (f" (specialised in {self.speciality})" if self.speciality else "")
