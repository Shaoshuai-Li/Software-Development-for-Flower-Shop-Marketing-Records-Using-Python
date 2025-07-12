# main.py
"""
Author:Shaoshuai Li
Description: Entry point. Handles user interaction and main monthly simulation loop.
"""

from flowershop import FlowerShop
from bouquet import Bouquet
from vendor import Vendor

def input_int(prompt, min_value=0, max_value=None, allow_blank=False):
    """Safely input an integer within range, with error handling."""
    while True:
        value = input(prompt)
        if allow_blank and value.strip() == "":
            return None
        try:
            ivalue = int(value)
            if ivalue < min_value or (max_value is not None and ivalue > max_value):
                print(f"Value must be between {min_value} and {max_value or '∞'}.")
                continue
            return ivalue
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("-"*50)
    print("Welcome to the FlowerShop Simulator!")
    print("-"*50)

    months = input_int("How many months would you like to run the game for? [default: 6]: ", 1)
    if not months:
        months = 6

    shop = FlowerShop()

    bankrupt = False

    for m in range(months):
        print("*" * 70)
        print(f"MONTH {m+1} BEGIN!")
        # Show current staff and add/remove florists
        print(f"Current number of florists: {len(shop.florists)}")
        change = input_int(f"How many florists would you like to hire or fire this month? (positive to hire, negative to fire, 0 to skip): ", -shop.MAX_FLORISTS, shop.MAX_FLORISTS)
        # Handle hiring
        if change > 0:
            for i in range(change):
                while True:
                    name = input("Please input florist name (unique, non-blank): ").strip()
                    if not name:
                        print("Name cannot be blank.")
                        continue
                    try:
                        # Ask for speciality (extension, optional)
                        spec = input("Does this florist have a speciality bouquet? (leave blank for none): ").strip()
                        if spec and spec not in Bouquet.types:
                            print("Invalid bouquet type.")
                            continue
                        shop.add_florist(name, spec if spec else None)
                        break
                    except Exception as e:
                        print("Error:", e)
        elif change < 0:
            to_remove = abs(change)
            for i in range(to_remove):
                while True:
                    name = input("Enter name of florist to remove: ").strip()
                    if name not in [f.name for f in shop.florists]:
                        print("Florist not found.")
                    else:
                        shop.remove_florist(name)
                        print(f"Removed {name}.")
                        break
        if len(shop.florists) < shop.MIN_FLORISTS:
            print("You must have at least one florist. Adding a default florist: 'Default'.")
            shop.add_florist(f"Default{m+1}")

        print("Current staff:", [str(f) for f in shop.florists])

        # Bouquet sales input
        orders = {}
        max_labour = shop.get_total_labour_minutes()
        total_labour = 0
        for btype in Bouquet.types:
            while True:
                qty = input_int(f"{btype} (max demand {Bouquet.types[btype]['demand']}): ", 0, Bouquet.types[btype]['demand'])
                if not shop.can_fulfill_order(btype, qty):
                    print("Insufficient supplies for this bouquet.")
                    continue
                labour_needed = Bouquet.types[btype]['prep_time'] * qty
                if total_labour + labour_needed > max_labour:
                    print("Not enough employee resources to complete this many bouquets.")
                    continue
                orders[btype] = qty
                total_labour += labour_needed
                break

        print("-"*50)
        print("Month in progress...\n")
        # Month end calculations
        try:
            print(f"Cash Balance, Month Start: £{shop.cash:.2f}")
            income = shop.calculate_income(orders)
            shop.cash += income
            print(f"Income: £{income:.2f}")
            emp_cost = shop.pay_florists()
            print(f"+ Employee costs: £{emp_cost:.2f}")
            gh_cost = shop.pay_greenhouse()
            print(f"+ Greenhouse costs: £{gh_cost:.2f}")
            shop.fulfill_orders(orders)
            shop.show_status()
            shop.depreciate_inventory()
            # Restock
            print("The greenhouse has spare capacity and needs to be restocked...")
            vendors_choice = {}
            for flower in shop.inventory:
                while True:
                    choice = input(f"Do you want to purchase {flower} from Evergreen Essentials (0) or FloraGrow Distributors (1)? Press (i) to see price info: ")
                    if choice.lower() == 'i':
                        Vendor.show_prices()
                        continue
                    if choice not in ['0', '1']:
                        print("Invalid input.")
                        continue
                    vendors_choice[flower] = int(choice)
                    break
            restock_cost = shop.restock(vendors_choice)
            print(f"+ Flower restock costs: £{restock_cost:.2f}")
            print(f"End-of-month Cash Balance: £{shop.cash:.2f}")
        except Exception as e:
            print("BANKRUPT! Simulation ends.")
            bankrupt = True
            break

    if not bankrupt:
        print("Congratulations! You have completed the simulation!")

if __name__ == "__main__":
    main()
