# main.py
"""
Author:Shaoshuai Li
student number:2652166
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
                print(f"Sorry,Value must be between {min_value} and {max_value or '∞'}.Please try again.")
                continue
            return ivalue
        except ValueError:
            print("Please enter a valid integer.")

def main():
    """
    Command‑line entry point running the monthly simulation loop
    """
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
        max_hire = shop.MAX_FLORISTS - len(shop.florists)
        max_fire = len(shop.florists)-1
        while True:
            change = input_int(
                f"How many florists would you like to hire or fire this month? (positive to hire [max {max_hire}], negative to fire [max {max_fire}], 0 to skip): ",
                -max_fire, max_hire
            )
            if change < 0 and abs(change) > max_fire:
                print(f"You must keep at least one florist. You can only remove up to {max_fire} this month.")
                continue
            if change > 0 and change > max_hire:
                print(f"You can only hire up to {max_hire} new florists.")
                continue


            if change == 0 and len(shop.florists) == 0:
                print("You must have at least one florist.")
                continue


            break

        if change > 0:
            for i in range(change):
                while True:
                    name = input("Please input florist name (unique, non-blank): ").strip()
                    #Cannot be blank
                    if not name:
                        print("Sorry,name cannot be blank,Please try again.")
                        continue
                    #Not entirely digital
                    if name.isdigit():
                        print("Sorry,name should be in English. Please re-enter.")
                        continue

                    try:
                        spec = input("Does this florist have a speciality bouquet? (leave blank for none): ").strip()
                        if spec and spec not in Bouquet.types:
                            print("Invalid bouquet type,Please try again.")
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
                        print("Sorry,florist not found.Please try again.")
                    else:
                        shop.remove_florist(name)
                        print(f"Removed {name}.")
                        break
        """
        if len(shop.florists) < shop.MIN_FLORISTS:
            print("You must have at least one florist. Adding a default florist: 'Default'.")
            shop.add_florist(f"Default{m+1}")
        """

        """
        if len(shop.florists) < shop.MIN_FLORISTS:
            print("You must have at least one florist.")
            # 强制进入雇佣流程，直到至少雇佣一位花艺师
            while len(shop.florists) < shop.MIN_FLORISTS:
                name = input("Please input florist name (unique, non-blank): ").strip()
                if not name:
                    print("Name cannot be blank.")
                    continue
                try:
                    spec = input("Does this florist have a speciality bouquet? (leave blank for none): ").strip()
                    if spec and spec not in Bouquet.types:
                        print("Invalid bouquet type.")
                        continue
                    shop.add_florist(name, spec if spec else None)
                except Exception as e:
                    print("Error:", e)
        """

        print("Current staff:", [str(f) for f in shop.florists])


        """
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
        """

        # Bouquet sales input
        temp_inventory = shop.inventory.copy()
        orders = {}
        #max_labour = shop.get_total_labour_minutes()
        #total_labour = 0
        for btype in Bouquet.types:
            while True:
                qty = input_int(
                    f"{btype} (max demand {Bouquet.types[btype]['demand']}): ",
                    0, Bouquet.types[btype]['demand'])
                """

                # 检查 labour
                labour_needed = Bouquet.types[btype]['prep_time'] * qty
                if total_labour + labour_needed > max_labour:
                    print("Not enough employee resources to complete this many bouquets.")
                    continue
                """

                # 检查 & 扣除临时库存
                ok = True
                for fl in ("Greenery", "Roses", "Daisies"):
                    need = Bouquet.types[btype][fl] * qty
                    if temp_inventory[fl] < need:
                        ok = False
                        break
                if not ok:
                    print("Insufficient supplies for this bouquet.")
                    continue

                orders_temp = orders.copy()
                orders_temp[btype] = qty
                if not shop.can_fulfill_orders_with_specialists(orders_temp):
                    print("Not enough employee resources (with specialities) to complete this many bouquets.")
                    continue






                # 合法 —— 更新
                orders[btype] = qty
                #total_labour += labour_needed
                for fl in ("Greenery", "Roses", "Daisies"):
                    temp_inventory[fl] -= Bouquet.types[btype][fl] * qty
                break

            '''
            原来的
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
                '''
        print("-"*50)
        print("Month in progress...\n")
        # Month end calculations
        try:
            print(f"Cash Balance, Month Start: £{shop.cash:.2f}")
            #Income
            income = shop.calculate_income(orders)
            shop.cash += income
            print(f"Income: £{income:.2f}")
            #Employee costs
            emp_cost = shop.pay_florists()
            print(f"Outcome-Employee costs: £{emp_cost:.2f}")

            '''
            gh_cost = shop.pay_greenhouse()
            print(f"+ Greenhouse costs: £{gh_cost:.2f}")
            '''
            # rent
            rent_cost = shop.pay_rent()
            print(f"Outcome-Rent: £{rent_cost:.2f}")

            # 扣库存（售出）
            shop.fulfill_orders(orders)

            # Storage fees (after sales, before depreciation)
            storage_cost = shop.pay_storage_costs()
            print(f"Outcome-Greenhouse costs: £{storage_cost:.2f}")

            #show the status
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
            print(f"Outcome-Flower restock costs: £{restock_cost:.2f}")
            print(f"End-of-month Cash Balance: £{shop.cash:.2f}")
        except Exception as e:
            print("BANKRUPT! Simulation ends.")
            bankrupt = True
            break

    if not bankrupt:
        print("Congratulations! You have completed the simulation!")

if __name__ == "__main__":
    main()
