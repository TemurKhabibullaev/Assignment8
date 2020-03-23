# Temur Khabibullaev 3/23/2020
from FIFO_LIFO_code import Queues as Q
from FIFO_LIFO_code import Stacks as S

# Creating two instances for amount and price Queues and Stacks
instance_amountQ = Q()
instance_priceQ = Q()

instance_amountS = S()
instance_priceS = S()


def fifo():
    # We'll keep these two temporary variables (QUEUES)
    profit = 0
    inventory = 0

    while True:
        print("""You are in FIFO style. Choose below to proceed!
        MENU:
        1. Add securities in portfolio.
        2. Sell securities from portfolio.
        3. Check profit to date.
        4. Display portfolio.
        5. Enter 5 to exit.""")
        select = int(input("\n>>>"))
        # Process of adding to inventory and price data
        if select == 1:
            amount = int(input("Please specify how many:\n>>>"))
            instance_amountQ.enqueue(int(amount))
            inventory += amount
            price = int(input("Please specify hom much it cost:\n>>>"))
            instance_priceQ.enqueue(int(price))
        # Process of subtracting from inventory and adding to profits
        if select == 2:
            amount_to_sell = int(input("Specify how many will be deleted:\n>>>"))
            # If specified amount is too much
            if amount_to_sell > inventory:
                print("You specified too large amount.")
                break
            else:
                inventory -= amount_to_sell
                last_price = None
                # X is a first number in Queue
                x = instance_amountQ.display()[0]
                # When first number is less than amount to be deleted
                if x < amount_to_sell:
                    # Temporary storage to keep track of surpassing the limits
                    storage = 0
                    # This loop will keep popping the nodes until enough is reached
                    while storage != amount_to_sell and storage < amount_to_sell:
                        selling_item = instance_amountQ.dequeue()
                        storage += selling_item
                        last_price = instance_priceQ.dequeue()
                    # When enough is reached we will push back the difference and count the profit
                    if storage > amount_to_sell:
                        difference = storage - amount_to_sell
                        instance_amountQ.enqueue(difference)
                        instance_priceQ.enqueue(last_price)
                        profit += last_price * amount_to_sell
                # When amount is less than first node in the Queue
                if amount_to_sell < x and amount_to_sell > 0:
                    selling_item = instance_amountQ.dequeue()
                    last_price = instance_priceQ.dequeue()
                    difference = selling_item - amount_to_sell
                    instance_amountQ.enqueue(difference)
                    instance_priceQ.enqueue(last_price)
                    profit += last_price * amount_to_sell
                # In case X equals to amount to sell
                if x == amount_to_sell:
                    selling_item = instance_amountQ.dequeue()
                    last_price = instance_priceQ.dequeue()
                    profit += last_price * selling_item
        # This is to keep track of profits
        if select == 3:
            print("So far you have made:")
            print(profit)
        # This is to show current condition of an inventory
        if select == 4:
            print("Current inventory:")
            print(instance_amountQ.display())
        # Enter 5 to break
        if select == 5:
            break


def lifo():
    # These are temporary variables (STACKS)
    profit = 0
    inventory = 0
    while True:
        print("""You are in LIFO style. Choose below to proceed!
        MENU:
        1. Add securities in portfolio.
        2. Sell securities from portfolio.
        3. Check profit to date.
        4. Display portfolio.
        5. Enter 5 to exit.""")
        select = int(input("\n>>>"))
        # Process of storing in inventory
        if select == 1:
            amount = int(input("Please specify how many:\n>>>"))
            instance_amountS.push(int(amount))
            inventory += amount
            price = int(input("Please specify hom much it cost:\n>>>"))
            instance_priceS.push(int(price))
        # Process to sell items from the inventory
        if select == 2:
            amount_to_sell = int(input("Specify how many will be deleted:\n>>>"))
            # If specified amount is too much
            if amount_to_sell > inventory:
                print("You specified too large amount.")
                break
            # Actual process of selling
            else:
                # Subtracting selling amount from inventory
                inventory -= amount_to_sell
                # Having always changing variable for price
                last_price = None
                # X is the first number in the Stack
                x = instance_amountS.display()[0]
                # If first number is less than intended amount for sell
                if x < amount_to_sell:
                    # Temporary variable to control popping method
                    storage = 0
                    while storage != amount_to_sell and storage < amount_to_sell:
                        selling_item = instance_amountS.pop()
                        storage += selling_item
                        last_price = instance_priceS.pop()
                    # When storage is surpassed do this
                    if storage > amount_to_sell:
                        difference = storage - amount_to_sell
                        instance_amountS.push(difference)
                        instance_priceS.push(last_price)
                        profit += last_price * amount_to_sell
                # When amount for sell is less than first number in Stack
                if amount_to_sell < x and amount_to_sell > 0:
                    # Process is easy
                    selling_item = instance_amountS.pop()
                    last_price = instance_priceS.pop()
                    difference = selling_item - amount_to_sell
                    instance_amountS.push(difference)
                    instance_priceS.push(last_price)
                    profit += last_price * amount_to_sell
                # When it happens that first number equals to selling amount
                if x == amount_to_sell:
                    selling_item = instance_amountS.pop()
                    last_price = instance_priceS.pop()
                    profit += last_price * selling_item
        # Display so far made profit
        if select == 3:
            print("So far you have made:")
            print(profit)
        # Display leftover items
        if select == 4:
            print("Current inventory:")
            print(instance_amountS.display())
        # Quit
        if select == 5:
            break


choice = int(input("Please choose:\n1. FIFO\n2. LIFO\n>>>"))
if choice == 1:
    fifo()
if choice == 2:
    lifo()