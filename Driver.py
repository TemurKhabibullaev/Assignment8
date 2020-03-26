# Temur Khabibullaev 3/23/2020

from FIFO_LIFO_code import UniversalMethod as U

# Creating instance
instance_amount = U()


def universal_method():
    # These are temporary variables
    profit = 0
    inventory = 0
    initial_price = None
    one_time = 1

    while True:
        if choice == 1:
            print("You are in FIFO style.")
        else:
            print("You are in LIFO style.")
        select = int(input("""Choose below to proceed!
           MENU:
           1. Add securities in portfolio.
           2. Sell securities from portfolio.
           3. Check profit to date.
           4. Display portfolio.
           5. Enter 5 to exit.\n>>>"""))
        # Process of storing in inventory
        if select == 1:
            amount = int(input("Please specify how many:\n>>>"))
            if choice == 2:
                instance_amount.add_head(int(amount))
            else:
                instance_amount.add_end(int(amount))
            inventory += amount
            if one_time == 0:
                next_stock_price = int(input("Please specify its price:\n>>>"))
                profit += (initial_price - next_stock_price) * amount
            if one_time == 1:
                price = int(input("Please specify hom much is your first stock costs:\n>>>"))
                one_time -= 1
                initial_price = price
        # Process to sell items from the inventory
        if select == 2:
            amount_to_sell = int(input("Specify how many will be sold:\n>>>"))
            stock_price_ = int(input("Hom much are they?:\n>>>"))
            # If specified amount is too much
            if amount_to_sell > inventory:
                print("You specified too large amount.")
                break
            # Actual process of selling
            else:
                # Subtracting selling amount from inventory
                inventory -= amount_to_sell
                # X is the first number in the Stack
                x = instance_amount.display()[0]
                # If first number is less than intended amount for sell
                if x < amount_to_sell:
                    # Temporary variable to control popping method
                    storage = 0
                    while storage != amount_to_sell and storage < amount_to_sell:
                        selling_item = instance_amount.del_head()
                        storage += selling_item
                    # When storage is surpassed do this
                    if storage > amount_to_sell:
                        difference = storage - amount_to_sell
                        if choice == 2:
                            instance_amount.add_head(difference)
                        else:
                            instance_amount.add_end(difference)
                        profit += (stock_price_ - initial_price) * amount_to_sell
                    if storage == amount_to_sell:
                        profit += (stock_price_ - initial_price) * amount_to_sell
                # When amount for sell is less than first number in Stack
                if amount_to_sell < x and amount_to_sell > 0:
                    # Process is easy
                    selling_item = instance_amount.del_head()
                    difference = selling_item - amount_to_sell
                    if choice == 2:
                        instance_amount.add_head(difference)
                    else:
                        instance_amount.add_end(difference)
                    profit += (stock_price_ - initial_price) * amount_to_sell
                # When it happens that first number equals to selling amount
                if x == amount_to_sell:
                    selling_item = instance_amount.del_head()
                    profit += (stock_price_ - initial_price) * selling_item
        # Display so far made profit
        if select == 3:
            print("So far you have made:")
            print(profit)
        # Display leftover stocks
        if select == 4:
            print("Current number of particular stock in portfolio:")
            print(instance_amount.display())
        # Quit
        if select == 5:
            break


choice = int(input("Please choose:\n1. FIFO\n2. LIFO\n>>>"))
if choice == 1:
    universal_method()
if choice == 2:
    universal_method()
