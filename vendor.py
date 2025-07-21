# vendor.py
"""
Author:Shaoshuai Li
student number:2652166
Description: Vendor class manages supplier prices for each ingredient.
"""

class Vendor:
    """
    Manages vendor prices for all flower ingredients.
    """
    vendor_prices = {
        "Evergreen Essentials": {
            "Roses": 2.80,
            "Daisies": 1.50,
            "Greenery": 0.95
        },
        "FloraGrow Distributors": {
            "Roses": 1.60,
            "Daisies": 1.20,
            "Greenery": 1.80
        }
    }

    @staticmethod
    def show_prices():
        """Display all vendor prices for each type of supply."""
        for name, items in Vendor.vendor_prices.items():
            print(f"{name}:")
            for k, v in items.items():
                print(f"  {k}: £{v:.2f}/bunch")
            print()
