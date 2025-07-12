# vendor.py
"""
Author:Shaoshuai Li
Description: Vendor class manages supplier prices for each ingredient.
"""

class Vendor:
    """
    Manages vendor prices for all flower ingredients.
    """
    vendor_prices = {
        "Evergreen Essentials": {
            "Roses": 2.80,
            "Daises": 1.50,
            "Greenery": 0.95
        },
        "FloraGrow Distributors": {
            "Roses": 1.60,
            "Daises": 1.20,
            "Greenery": 1.80
        }
    }

    @staticmethod
    def show_prices():
        """Prints the current vendor prices."""
        for name, items in Vendor.vendor_prices.items():
            print(f"{name}:")
            for k, v in items.items():
                print(f"  {k}: £{v:.2f}/bunch")
            print()
