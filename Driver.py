# Temur Khabibullaev 3/23/2020
from FIFO_LIFO_code import Queues as Q
from FIFO_LIFO_code import Stacks as S

# Creating two instances for amount and price Queues and Stacks
instance_amount_Q = Q()
instance_price_Q = Q()

instance_amount_S = S()
instance_price_S = S()

# We'll keep these two temporary variables
profit = 0
inventory = 0

while True:
    print("""Welcome! Choose below to proceed!
    MENU:
    1. Add to the inventory.
    2. Sell items in inventory.
    3. Check profit to date.
    4. Display inventory.
    5. Enter 5 to exit.""")
    select = int(input("\n>>>"))
    # Process of adding to inventory and price data
    if select == 1:
        amount = int(input("Please specify how many:\n>>>"))
        instance_amount.enqueue(int(amount))
        inventory += amount
        price = int(input("Please specify hom much it cost:\n>>>"))
        instance_price.enqueue(int(price))
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
            x = instance_amount.display()[0]
            # When first number is less than amount to be deleted
            if x < amount_to_sell:
                # Temporary storage to keep track of surpassing the limits
                storage = 0
                # This loop will keep popping the nodes until enough is reached
                while storage != amount_to_sell and storage < amount_to_sell:
                    selling_item = instance_amount.dequeue()
                    storage += selling_item
                    last_price = instance_price.dequeue()
                # When enough is reached we will push back the difference and count the profit
                if storage > amount_to_sell:
                    difference = storage - amount_to_sell
                    instance_amount.enqueue(difference)
                    instance_price.enqueue(last_price)
                    profit += (last_price * 0.1) * amount_to_sell
            # When amount is less than first node in the Queue
            if amount_to_sell < x and amount_to_sell > 0:
                selling_item = instance_amount.dequeue()
                last_price = instance_price.dequeue()
                difference = selling_item - amount_to_sell
                instance_amount.enqueue(difference)
                instance_price.enqueue(last_price)
                profit += (last_price * 0.1) * amount_to_sell
            # In case X equals to amount to sell
            if x == amount_to_sell:
                selling_item = instance_amount.dequeue()
                last_price = instance_price.dequeue()
                profit += (last_price * 0.1) * selling_item
    # This is to keep track of profits
    if select == 3:
        print("So far you have made:")
        print(profit)
    # This is to show current condition of an inventory
    if select == 4:
        print(instance_amount.display())
    # Enter 5 to break
    if select == 5:
        break
