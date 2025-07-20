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
        :parameter name:Florist's name.
        :parameter speciality:The bouquet type the florist specialises in .
        """
        self.name = name
        self.speciality = speciality

    def __repr__(self):
        '''Return readable representation used in staff lists'''
        return f"{self.name}" + (f" (specialised in {self.speciality})" if self.speciality else "")
