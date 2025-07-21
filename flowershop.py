# flowershop.py
"""
Author:Shaoshuai Li
Description: Main FlowerShop class to manage cash, inventory, florists, monthly routines.
"""

from bouquet import Bouquet
from florist import Florist
from vendor import Vendor
import math

class FlowerShop:
    """Manages shop inventory, florists, cash, and simulates each month."""
    # Initial constants
    GREENHOUSE_CAPACITY = {"Roses": 100, "Daisies": 150, "Greenery": 200}
    DEPRECIATION = {"Roses": 0.4, "Daisies": 0.15, "Greenery": 0.05}
    GREENHOUSE_COSTS = {"Roses": 2.5, "Daisies": 1.0, "Greenery": 0.4}
    RENT = 1000
    INITIAL_CASH = 7500
    MAX_FLORISTS = 4
    MIN_FLORISTS = 1

    def __init__(self):
        """Initialise with full inventory and initial cash, no florists."""
        self.cash = self.INITIAL_CASH
        self.inventory = self.GREENHOUSE_CAPACITY.copy()
        self.florists = []
        self.month = 1

    # === Employee Management ===
    def add_florist(self, name, speciality=None):
        """Add a florist if max limit is not reached and name is unique."""
        if name in [f.name for f in self.florists]:
            raise ValueError(f"Florist '{name}' already exists.")
        if len(self.florists) >= self.MAX_FLORISTS:
            raise ValueError("Maximum number of florists reached.")
        self.florists.append(Florist(name, speciality))

    def remove_florist(self, name):
        """Remove a florist by name."""
        self.florists = [f for f in self.florists if f.name != name]
    '''
    # === Main monthly simulation logic ===
    def get_total_labour_minutes(self):
        """Total bouquet making time available from all florists.
        Return the bouquet‑making minutes available this month.
        Each florist works ``MONTHLY_HOURS`` hours; multiply by 60 to convert hours to minutes"""
        return sum([Florist.MONTHLY_HOURS * 60 for _ in self.florists])
    '''

    def pay_florists(self):
        """Pay all florists for the month."""
        total = len(self.florists) * Florist.MONTHLY_HOURS * Florist.HOURLY_RATE
        if self.cash < total:
            raise RuntimeError("Not enough cash to pay florists!")
        self.cash -= total
        return total
    '''
    def pay_greenhouse(self):
        """Pay monthly greenhouse rent and variable costs."""
        cost = self.RENT
        for k in self.inventory:
            cost += self.GREENHOUSE_COSTS[k] * self.inventory[k]
        if self.cash < cost:
            raise RuntimeError("Not enough cash to pay greenhouse!")
        self.cash -= cost
        return cost
    '''

    def pay_rent(self):
        """Pay the fixed monthly rent(1000).
        Returns:
            int: The rent amount paid (always ``self.RENT``).
        Raises:
            RuntimeError: If ``cash`` on hand is insufficient.
        """
        if self.cash < self.RENT:
            raise RuntimeError("Not enough cash to pay rent!")
        self.cash -= self.RENT
        return self.RENT

    def pay_storage_costs(self) -> float:
        """Pay variable greenhouse storage costs based on current inventory."""
        cost = sum(self.GREENHOUSE_COSTS[k] * v for k, v in self.inventory.items())
        if self.cash < cost:
            raise RuntimeError("Not enough cash to pay greenhouse storage costs!")
        self.cash -= cost
        return cost


    def depreciate_inventory(self):
        """Apply monthly depreciation, rounding up."""
        for flower in self.inventory:
            loss = math.ceil(self.inventory[flower] * self.DEPRECIATION[flower])
            self.inventory[flower] = max(self.inventory[flower] - loss, 0)

    def restock(self, vendors_choice):
        """
        Restock all ingredients to full capacity using selected vendors.
        vendors_choice: dict with vendor choice for each supply.
        """
        cost = 0
        for flower in self.inventory:
            need = self.GREENHOUSE_CAPACITY[flower] - self.inventory[flower]
            if need > 0:
                # vendor_choice: 0 (Evergreen), 1 (FloraGrow)
                vendor_name = ["Evergreen Essentials", "FloraGrow Distributors"][vendors_choice[flower]]
                price = Vendor.vendor_prices[vendor_name][flower]
                item_cost = need * price
                cost += item_cost
                self.inventory[flower] += need
        if self.cash < cost:
            raise RuntimeError("Not enough cash to restock!")
        self.cash -= cost
        return cost

    def can_fulfill_order(self, bouquet_type, amount):
        """Check if order can be fulfilled with current supplies."""
        reqs = Bouquet.types[bouquet_type]
        for flower in ["Greenery", "Roses", "Daisies"]:
            if self.inventory[flower] < reqs[flower] * amount:
                return False
        return True

    def fulfill_orders(self, order_dict):
        """Deduct ingredients for orders from inventory."""
        for b_type, qty in order_dict.items():
            reqs = Bouquet.types[b_type]
            for flower in ["Greenery", "Roses", "Daisies"]:
                self.inventory[flower] -= reqs[flower] * qty

    def calculate_income(self, order_dict):
        """Calculate total sales income."""
        return sum(Bouquet.types[b]["price"] * qty for b, qty in order_dict.items())

    def show_status(self):
        """Prints shop status."""
        print("Current staff:", [str(f) for f in self.florists])
        print("Greenhouse Quantity:")
        for k, v in self.inventory.items():
            print(f"{k}: {v}")
        print(f"Current cash: £{self.cash:.2f}")

    def can_fulfill_orders_with_specialists(self, order_dict):
        """
        Check if all orders can be fulfilled within the total available labour,
        accounting for florist specialities (specialists make their bouquet in half time).
        Returns True/False.
        """
        # Remaining minutes for each florist (reset monthly)
        florist_minutes = {f: Florist.MONTHLY_HOURS * 60 for f in self.florists}
        for btype, qty in order_dict.items():
            prep_time = Bouquet.types[btype]['prep_time']
            # Priority allocation to specialist florists
            specialists = [f for f in self.florists if f.speciality == btype]
            nonspecialists = [f for f in self.florists if f.speciality != btype]
            remaining_qty = qty

            # Assigned to specialists
            for sp in specialists:
                per_bouquet_time = max(1, prep_time // 2)
                max_bouquets = florist_minutes[sp] // per_bouquet_time
                this_qty = min(max_bouquets, remaining_qty)
                florist_minutes[sp] -= this_qty * per_bouquet_time
                remaining_qty -= this_qty
                if remaining_qty == 0:
                    break

            # Assigned to non-specialists
            if remaining_qty > 0:
                for nsp in nonspecialists:
                    per_bouquet_time = prep_time
                    max_bouquets = florist_minutes[nsp] // per_bouquet_time
                    this_qty = min(max_bouquets, remaining_qty)
                    florist_minutes[nsp] -= this_qty * per_bouquet_time
                    remaining_qty -= this_qty
                    if remaining_qty == 0:
                        break

            if remaining_qty > 0:
                return False

        return True
